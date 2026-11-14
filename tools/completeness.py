"""Completeness of the imported books: what of each source book is in the base and what is not.

Read-only. For every book of `pipeline/source/books.json` that records cite:
  text     pages with text that no record cites (sources, page numbers in source notes, images), as runs of pages
           with their first headings — the places where a chapter, a character or a handout may have been missed;
  art      pictures of the PDF (Poppler `pdfimages -list`, decorations repeated on 3+ pages dropped) on pages whose
           picture no record carries; a character, creature or handout cited on that page without `images` is named;
  links    characters nobody refers to, scenes without a place, handouts and items no scene or scenario uses;
  context  records without a description, handouts without text and picture, scenarios without summary or time.
Scans without a text layer: pages are counted from the PDF and the OCR cache (`.cache/ocr/<book>/NNN.txt`).

Writes `report.md` (a table by book, then the findings by book) and `findings.json` to the output folder.

Usage:
  python tools/completeness.py                                 write to checks/<today>-completeness/
  python tools/completeness.py --books arkham-en,tide-ru       only these books
  python tools/completeness.py --min-words 120 --out checks/x  thresholds and folder
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "pipeline" / "source"))
from audit import COMMON, Audit, STRUCT  # noqa: E402
from kblib import ROOT  # noqa: E402
import pages  # noqa: E402

BOOKS = json.loads((ROOT / "pipeline/source/books.json").read_text(encoding="utf-8"))
CACHE = ROOT / ".cache" / "sources"
OCR = ROOT / ".cache" / "ocr"

PAGE_RE = re.compile(r"(?:(?<![А-Яа-яЁёA-Za-z])(?:сс?|стр|pp?)\.\s*)((?:\d{1,4}(?:\s*[–\-]\s*\d{1,4})?(?:\s*(?:,|и)\s*)?)+)")
PHYS_RE = re.compile(r"физ\.\s*(\d{1,4})")
WORD_RE = re.compile(r"[A-Za-zА-Яа-яЁё]{3,}")
HEAD_RE = re.compile(r"^[A-ZА-ЯЁ][^.!?;:]{2,60}$")
SERVICE_RE = re.compile(r"\b(CREDITS|INDEX|Index|Contents|CONTENTS|Biographies|Kickstarter|Backers|Patrons)\b|Оглавление|Содержание|"
                        r"Указатель|Над книгой работали|Благодарност|Выходные данные|Авторы", re.I)
ART_KINDS ={"character", "creature", "handout", "item", "location", "map", "scene", "tome", "organization"}

CHECKS = {
    "text.gap": ("text", "Страницы с текстом, которые не цитирует ни одна запись"),
    "art.uncovered": ("art", "Картинки книги на странице, где ни одна запись не несёт картинку"),
    "art.record_without": ("art", "Страница с картинкой, которую не несёт ни одна запись, а персонаж, существо, раздатка, предмет или книга этой страницы — без `images`"),
    "links.character_unused": ("links", "Персонаж без связей: ни сцена, ни сценарий, ни другая запись на него не ссылаются, своих связей нет"),
    "links.scene_no_place": ("links", "Сцена без места (`where`)"),
    "links.unused": ("links", "Раздатка или предмет, которые не использует ни сцена, ни сценарий"),
    "context.no_description": ("context", "Запись без описания"),
    "context.handout_empty": ("context", "Раздатка без текста и без картинки"),
    "context.scenario_thin": ("context", "Сценарий без краткого содержания (`summary`) или сведений для хранителя (`keeper_info`/`steps`)"),
    "context.incomplete": ("context", "Запись помечена `incomplete`"),
}
CLASSES = {"text": "Тексты", "art": "Картинки", "links": "Связи", "context": "Контекст"}


def ru(v) -> str:
    if isinstance(v, dict):
        return (v.get("ru") or v.get("en") or "").strip()
    if isinstance(v, list):
        return " ".join(ru(x) for x in v)
    return v.strip() if isinstance(v, str) else ""


def printed_list(s: str) -> list[int]:
    out = []
    for m in PAGE_RE.finditer(s or ""):
        for part in re.split(r"\s*(?:,|и)\s*", m.group(1)):
            x, _, y = re.sub(r"\s", "", part).replace("–", "-").partition("-")
            if x.isdigit():
                a, b = int(x), int(y) if y.isdigit() else int(x)
                if 0 < a <= b and b - a <= 40:
                    out += range(a, b + 1)
    return out


def phys(b: dict, printed: int) -> int:
    return pages.physical_of(b, printed)[0]


def pdf_pages(b: dict) -> int:
    try:
        out = subprocess.run([pages.tool("pdfinfo"), b["pdf"]], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120).stdout
        m = re.search(r"^Pages:\s+(\d+)", out, re.M)
        return int(m.group(1)) if m else 0
    except Exception:
        return 0


def text_of_book(bid: str, b: dict) -> tuple[list[str] | None, str]:
    """Page texts (index 0 = physical page 1) and where they came from."""
    t = CACHE / bid / "text.txt"
    if t.exists():
        p = t.read_text(encoding="utf-8").split("\f")
        if sum(len(WORD_RE.findall(x)) for x in p) > 50 * max(1, len(p)) * 0.2:
            return p, "текст"
    o = OCR / bid
    if o.is_dir():
        files = sorted(o.glob("*.txt"))
        if files:
            n = max(int(f.stem) for f in files if f.stem.isdigit())
            p = [""] * n
            for f in files:
                if f.stem.isdigit():
                    p[int(f.stem) - 1] = f.read_text(encoding="utf-8", errors="replace")
            return p, "OCR"
    return None, "скан"


def images_of_book(bid: str, b: dict) -> dict[int, list[tuple[int, int]]]:
    """Pictures by physical page: (width, height); decorations (one object on 3+ pages) and small ones dropped."""
    cache = CACHE / bid / "images.list"
    if not cache.exists():
        try:
            out = subprocess.run([pages.tool("pdfimages"), "-list", b["pdf"]], capture_output=True, text=True,
                                 encoding="utf-8", errors="replace", timeout=600).stdout
        except Exception:
            return {}
        cache.parent.mkdir(parents=True, exist_ok=True)
        cache.write_text(out, encoding="utf-8")
    rows = []
    for line in cache.read_text(encoding="utf-8").splitlines()[2:]:
        f = line.split()
        if len(f) < 12 or f[2] != "image" or not f[0].isdigit():
            continue
        rows.append((int(f[0]), int(f[3]), int(f[4]), f[10] + ":" + f[11]))
    on_pages = defaultdict(set)
    size_pages = defaultdict(set)
    for p, w, h, obj in rows:
        on_pages[obj].add(p)
        size_pages[(w, h)].add(p)
    npages = len({p for p, *_ in rows}) or 1
    # page scans: one picture size on half the pages or more is the page itself, not an illustration
    scans = {s for s, ps in size_pages.items() if len(ps) >= max(5, npages // 2)}
    out = defaultdict(list)
    for p, w, h, obj in rows:
        if len(on_pages[obj]) >= 3 or (w, h) in scans or w < 250 or h < 250 or w * h < 120000:
            continue
        if (w, h) not in out[p]:
            out[p].append((w, h))
    return out


class Completeness:
    def __init__(self, a: Audit, min_words: int, only: set[str] | None):
        self.a, self.min_words, self.only = a, min_words, only
        self.findings: list[dict] = []
        self.rows: list[dict] = []
        self.title_to_id = sorted(((b["title"], i) for i, b in BOOKS.items() if b.get("title")), key=lambda x: -len(x[0]))
        # records citing each book; cited physical pages; pages whose picture a record carries
        self.of_book: dict[str, list[str]] = defaultdict(list)
        self.cited: dict[str, set[int]] = defaultdict(set)
        self.by_page: dict[str, dict[int, set[str]]] = defaultdict(lambda: defaultdict(set))
        self.art_pages: dict[str, set[int]] = defaultdict(set)
        for i, r in a.recs.items():
            for s in r.get("sources") or []:
                bid = s.get("book_id")
                if bid not in BOOKS:
                    continue
                b = BOOKS[bid]
                if i not in self.of_book[bid]:
                    self.of_book[bid].append(i)
                ps = set()
                if isinstance(s.get("physical_page"), int):
                    ps.add(s["physical_page"])
                for k in ("entry_page",):
                    if isinstance(s.get(k), int):
                        ps.add(phys(b, s[k]))
                ps |= {phys(b, n) for n in printed_list(s.get("note") or "")}
                self.cited[bid] |= ps
                for p in ps:
                    self.by_page[bid][p].add(i)
            for img in r.get("images") or []:
                src = img.get("source") or ""
                bid = self.book_of_source(src, r)
                if not bid:
                    continue
                m = PHYS_RE.search(src)
                ps = {int(m.group(1))} if m else {phys(BOOKS[bid], n) for n in printed_list(src)}
                self.art_pages[bid] |= ps
            if r.get("kind") == "map":                   # a map record carries the picture of its page
                for s in r.get("sources") or []:
                    if s.get("book_id") in BOOKS and isinstance(s.get("physical_page"), int):
                        self.art_pages[s["book_id"]].add(s["physical_page"])

    def book_of_source(self, src: str, r: dict) -> str | None:
        for t, i in self.title_to_id:
            if t in src:
                return i
        m = re.match(r"^([a-z0-9-]+),", src)
        if m and m.group(1) in BOOKS:
            return m.group(1)
        bs = [s.get("book_id") for s in r.get("sources") or [] if s.get("book_id") in BOOKS]
        return bs[0] if len(set(bs)) == 1 else None

    def add(self, check: str, bid: str, summary: str, conf: str, i: str | None = None, **extra):
        f = {"class": CHECKS[check][0], "check": check, "book": bid, "summary": summary, "confidence": conf}
        if i:
            f.update(id=i, name=self.a.name(i), file=self.a.rel(i))
        f.update({k: v for k, v in extra.items() if v not in (None, "", [])})
        self.findings.append(f)

    def label(self, b: dict, p: int) -> str:
        off = pages.offset_at(b, p)
        return f"с. {p + off} (физ. {p})" if off not in (None, 0) else f"с. {p}"

    # --- text and art, per book ----------------------------------------------------------------------------------
    def book(self, bid: str):
        b = BOOKS[bid]
        texts, kind = text_of_book(bid, b)
        n = len(texts) if texts else pdf_pages(b)
        cited = {p for p in self.cited[bid] if 1 <= p <= n}
        # a solo scenario (Р-230) holds all its paragraphs in one table: it covers its book from its first page on
        for i in self.of_book[bid]:
            r = self.a.recs[i]
            if r.get("kind") == "scenario" and r.get("solo"):
                first = min((s["physical_page"] for s in r.get("sources") or [] if s.get("book_id") == bid
                             and isinstance(s.get("physical_page"), int)), default=None)
                if first:
                    cited |= set(range(first, n + 1))
        row = {"book": bid, "title": b.get("title", bid), "lang": b.get("lang") or bid.rsplit("-", 1)[-1],"pages": n, "text": kind,
               "records": len(self.of_book[bid]), "cited": len(cited), "gap_pages": 0, "gap_words": 0,
               "art_pages": 0, "art_uncovered": 0}
        if texts:
            words = [len(WORD_RE.findall(t)) for t in texts]
            gaps = [p for p in range(1, n + 1) if p not in cited and words[p - 1] >= self.min_words]
            runs: list[list[int]] = []
            for p in gaps:
                if runs and p - runs[-1][-1] <= 2 and all(q in gaps or words[q - 1] < self.min_words for q in range(runs[-1][-1] + 1, p)):
                    runs[-1].append(p)
                else:
                    runs.append([p])
            for run in runs:
                w = sum(words[p - 1] for p in run)
                heads = []
                for p in run:
                    for line in texts[p - 1].split("\n"):
                        l = re.sub(r"\s{3,}.*$", "", line.strip())
                        if HEAD_RE.match(l) and 1 <= len(l.split()) <= 7 and not l.isdigit() and l not in heads:
                            heads.append(l)
                        if len(heads) >= 4:
                            break
                    if len(heads) >= 4:
                        break
                near = sorted({self.a.name(i) for q in (run[0] - 1, run[-1] + 1) for i in self.by_page[bid].get(q, ())})[:3]
                conf = "high" if len(run) >= 3 or w >= 1500 else "medium" if len(run) == 2 or w >= 600 else "low"
                if SERVICE_RE.search(" ".join(heads)) or run[0] <= 4 or run[-1] >= n - 2:
                    conf = "low"                          # credits, contents, index, covers
                span = self.label(b, run[0]) + (f" — {self.label(b, run[-1])}" if len(run) > 1 else "")
                self.add("text.gap", bid, f"{span}: {len(run)} стр., {w} слов не цитирует ни одна запись", conf,
                         pages=run, headings="; ".join(heads), near="; ".join(near))
            row["gap_pages"] = len(gaps)
            row["gap_words"] = sum(words[p - 1] for p in gaps)
        if b.get("pdf") and not (kind != "текст" and n > 20):   # a long scan is pictures of pages: not counted
            pics = images_of_book(bid, b)
            have = self.art_pages[bid]
            row["art_pages"] = len(pics)
            for p, sizes in sorted(pics.items()):
                if p in have or p > n:
                    continue
                recs = sorted(self.by_page[bid].get(p, ()))
                bare = [i for i in recs if self.a.recs[i].get("kind") in ART_KINDS and not self.a.recs[i].get("images")]
                main = [i for i in bare if self.a.recs[i]["kind"] in ("character", "creature", "handout", "item", "tome")]
                big = max(w * h for w, h in sizes)
                size = ", ".join(f"{w}×{h}" for w, h in sizes[:4]) + ("…" if len(sizes) > 4 else "")
                row["art_uncovered"] += 1
                who = ", ".join(f"{self.a.name(i)} ({self.a.recs[i]['kind']})" for i in (main or bare)[:5])
                if main:
                    self.add("art.record_without", bid, f"{self.label(b, p)}: {len(sizes)} карт. ({size}); без картинки: {who}",
                             "high" if big >= 300000 else "medium", page=p, ids=main[:8])
                else:
                    self.add("art.uncovered", bid, f"{self.label(b, p)}: {len(sizes)} карт. ({size})"
                             + (f"; на странице: {who or ', '.join(self.a.name(i) for i in recs[:3])}" if recs else "; страницу не цитирует никто"),
                             "medium" if big >= 600000 else "low", page=p)
        self.rows.append(row)

    # --- links and context, per record ---------------------------------------------------------------------------
    def records(self):
        a = self.a
        for i, r in a.recs.items():
            bid = a.book(i)
            if bid == COMMON:
                srcs = [s.get("book_id") for s in r.get("sources") or []]
                bid = srcs[0] if srcs else COMMON
            if self.only and bid not in self.only:
                continue
            k = r.get("kind")
            ins = [(s, p) for s, p in a.inc.get(i, []) if s != i and p.split(".")[0] not in STRUCT]
            outs = [(p, t) for p, t in a.out.get(i, []) if t != i and p.split(".")[0] not in STRUCT | {"occupation_ref"}]
            if k == "character" and a.book(i) != COMMON and not ins and not outs:
                self.add("links.character_unused", bid, "персонаж ни с кем не связан", "low", i)
            if k == "scene" and not r.get("where"):
                self.add("links.scene_no_place", bid, f"сцена без места; сценарий {(r.get('arc') or {}).get('scenario')}", "low", i)
            if k in ("handout", "item") and a.book(i) != COMMON and not ins:
                self.add("links.unused", bid, f"{k}: ни одна запись на него не ссылается", "low", i)
            if k in ("character", "creature", "location", "scenario", "handout", "item", "tome", "organization", "spell") \
                    and not ru(r.get("description")) and not ru(r.get("summary")) and not ru(r.get("background")) \
                    and not ru(r.get("text")) and not ru(r.get("definition")):
                self.add("context.no_description", bid, f"{k} без описания", "medium" if k in ("character", "scenario", "creature") else "low", i)
            if k == "handout" and not ru(r.get("text")) and not r.get("images"):
                self.add("context.handout_empty", bid, "раздатка без текста и картинки", "high", i)
            if k == "scenario":
                miss = [f for f in ("summary",) if not ru(r.get(f))]
                if not ru(r.get("keeper_info")) and not r.get("steps") and not r.get("solo"):
                    miss.append("keeper_info/steps")
                if miss:
                    self.add("context.scenario_thin", bid, "нет: " + ", ".join(miss), "medium", i)
            if "incomplete" in ((r.get("quality") or {}).get("flags") or []):
                self.add("context.incomplete", bid, ((r.get("quality") or {}).get("notes") or "")[:200], "low", i)

    def run(self):
        for bid in sorted(self.of_book):
            if self.only and bid not in self.only:
                continue
            print(f"… {bid}", file=sys.stderr)
            self.book(bid)
        self.records()


def report(c: Completeness, out: Path, limit: int) -> str:
    by_book = defaultdict(list)
    for f in c.findings:
        by_book[f["book"]].append(f)
    cnt = Counter(f["check"] for f in c.findings)
    L = [f"# Полнота перенесённых книг — {datetime.date.today().isoformat()}", "",
         "Создано `python tools/completeness.py`; база не менялась. Пороги: страница с текстом — "
         f"от {c.min_words} слов; картинка — от 250×250, повторённые на 3+ страницах не считаются.", "",
         "## Итог по проверкам", "", "| Проверка | Что ищется | Находок |", "|---|---|---|"]
    for k, (cls, title) in CHECKS.items():
        L.append(f"| `{k}` | {title} | {cnt.get(k, 0)} |")
    L += ["", "## Книги", "",
          "| Книга | Язык | Текст | Стр. | Записей | Цитир. стр. | Стр. без записей (слов) | Стр. с картинками | без записи | Находок |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(c.rows, key=lambda r: -r["gap_words"]):
        L.append(f"| {r['title']} (`{r['book']}`) | {r['lang']} | {r['text']} | {r['pages']} | {r['records']} | {r['cited']} | "
                 f"{r['gap_pages']} ({r['gap_words']}) | {r['art_pages']} | {r['art_uncovered']} | {len(by_book.get(r['book'], []))} |")
    L += ["", "## Находки по книгам", ""]
    order = {"high": 0, "medium": 1, "low": 2}
    for bid in sorted(by_book, key=lambda b: -len(by_book[b])):
        fs = sorted(by_book[bid], key=lambda f: (f["class"], order[f["confidence"]], f.get("page", 0)))
        L += [f"### {BOOKS.get(bid, {}).get('title', bid)} (`{bid}`) — {len(fs)}", ""]
        for cls in CLASSES:
            part = [f for f in fs if f["class"] == cls]
            if not part:
                continue
            L.append(f"**{CLASSES[cls]}** ({len(part)})")
            L.append("")
            for f in part[:limit]:
                head = f"`{f['id']}` {f['name']} — " if f.get("id") else ""
                tail = "".join(f"; {k}: {f[k]}" for k in ("headings", "near") if f.get(k))
                L.append(f"- [{f['confidence']}] {head}{f['summary']}{tail}")
            if len(part) > limit:
                L.append(f"- … ещё {len(part) - limit} (все — в findings.json)")
            L.append("")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=f"checks/{datetime.date.today().strftime('%Y%m%d')}-completeness")
    ap.add_argument("--books", default="")
    ap.add_argument("--min-words", type=int, default=120)
    ap.add_argument("--limit", type=int, default=60)
    a = ap.parse_args()
    only = set(a.books.split(",")) - {""} or None
    c = Completeness(Audit(), a.min_words, only)
    c.run()
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    (out / "findings.json").write_text(json.dumps({"books": c.rows, "findings": c.findings}, ensure_ascii=False, indent=2) + "\n",
                                       encoding="utf-8", newline="\n")
    (out / "report.md").write_text(report(c, out, a.limit), encoding="utf-8", newline="\n")
    for k, v in sorted(Counter(f["check"] for f in c.findings).items()):
        print(f"{k} — {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
