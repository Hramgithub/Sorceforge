"""Layers 1-2 of the rules core check: locate each helper entry in the Keeper
Rulebook PDF text layer and compare numbers exactly and titles/keywords fuzzily.

Only entries whose source is the Keeper Rulebook are checked; entries from other
books are counted as "other_source". Output contains page numbers, scores and
the helper's own values, never book text.

Usage:
  python check_entries.py --docs <public/docs> --pages <dir with pNNN.txt>
                          --quality <pdf_text_quality.json> --out <entries.json>
"""
from __future__ import annotations

import argparse
import collections
import difflib
import json
import re
from pathlib import Path

LAT2CYR = str.maketrans({"a": "а", "e": "е", "o": "о", "p": "р", "c": "с", "x": "х", "y": "у",
                         "k": "к", "m": "м", "t": "т", "b": "в", "h": "н", "ё": "е", "d": "к"})
WORD = re.compile(r"[а-я]{3,}")
DICE = re.compile(r"(\d{1,2})\s*[кk]\s*(\d{1,3})")
MULTI = re.compile(r"(?<![\d,.])(\d{2,6})(?:[,.]00)?(?![\d])")

CHAPTERS = [(1, 12), (2, 20), (3, 25), (4, 50), (5, 76), (6, 92), (7, 125), (8, 143), (9, 159), (10, 170),
            (11, 206), (12, 218), (13, 247), (14, 256), (15, 322), (16, 363), (99, 396)]


def chapter_of(page: int) -> int | None:
    found = None
    for ch, start in CHAPTERS:
        if page >= start:
            found = ch
    return None if found == 99 else found


OCR_DICE = re.compile(r"(?<![A-Za-zА-Яа-яЁё])([\dlI]{1,2})\s?([dDдДкКkK])\s?([\dlIO]{1,3})(?![A-Za-zА-Яа-яЁё])")
OCR_NUM = re.compile(r"(?<![A-Za-zА-Яа-яЁё])(?=[\dlIO]*\d)[\dlIO]{2,6}(?![A-Za-zА-Яа-яЁё])")


def fix_ocr_digits(text: str) -> str:
    """Repair typical OCR confusions inside numeric tokens: l/I -> 1, O -> 0 (e.g. 'ldl0' -> '1d10')."""
    digits = str.maketrans({"l": "1", "I": "1", "O": "0"})
    text = OCR_DICE.sub(lambda m: f"{m.group(1).translate(digits)}к{m.group(3).translate(digits)}", text)
    return OCR_NUM.sub(lambda m: m.group(0).translate(digits), text)


def norm(text: str) -> str:
    text = fix_ocr_digits(text)
    text = text.lower().translate(LAT2CYR)
    text = text.replace("­", "").replace("-\n", "").replace("­", "")
    return re.sub(r"\s+", " ", text)


def numbers(text: str) -> set[str]:
    t = norm(text)
    out = {f"{a}к{b}" for a, b in DICE.findall(t)}
    t = DICE.sub(" ", t)
    out |= set(MULTI.findall(t))
    return out


def tokens(text: str) -> list[str]:
    return WORD.findall(norm(text))


class Book:
    def __init__(self, pages_dir: Path, quality: dict):
        self.text: dict[int, str] = {}
        self.toks: dict[int, set[str]] = {}
        self.nums: dict[int, set[str]] = {}
        self.index: dict[str, set[int]] = collections.defaultdict(set)
        self.grade = {p["page"]: p["grade"] for p in quality["pages"]}
        for f in sorted(pages_dir.glob("p*.txt")):
            p = int(f.stem[1:])
            raw = f.read_text(encoding="utf-8")
            self.text[p] = norm(raw)
            self.toks[p] = set(tokens(raw))
            self.nums[p] = numbers(raw)
            for t in self.toks[p]:
                self.index[t].add(p)
        self.vocab_by_key: dict[tuple[str, int], list[str]] = collections.defaultdict(list)
        for t in self.index:
            self.vocab_by_key[(t[0], len(t))].append(t)
        self._fuzzy_cache: dict[str, list[str]] = {}

    def fuzzy(self, tok: str) -> list[str]:
        if tok in self.index:
            return [tok]
        if tok not in self._fuzzy_cache:
            pool = [w for dl in (-1, 0, 1) for w in self.vocab_by_key.get((tok[0], len(tok) + dl), [])]
            self._fuzzy_cache[tok] = difflib.get_close_matches(tok, pool, n=3, cutoff=0.8)
        return self._fuzzy_cache[tok]

    def pages_for(self, title_toks: list[str]) -> dict[int, float]:
        hits: dict[int, int] = collections.Counter()
        for t in set(title_toks):
            pages = set()
            for alt in self.fuzzy(t):
                pages |= self.index[alt]
            for p in pages:
                hits[p] += 1
        n = max(len(set(title_toks)), 1)
        return {p: c / n for p, c in hits.items()}

    def window_nums(self, p: int) -> set[str]:
        return self.nums.get(p, set()) | self.nums.get(p + 1, set())


def entry_specs(docs: Path) -> list[dict]:
    """Return entries as {kind, id, title, numbers_from, keywords_from, pages_hint, source_ok}."""
    out = []

    def load(rel):
        return [json.loads(p.read_text(encoding="utf-8")) for p in sorted((docs / rel).glob("*.json"))]

    for e in load("equipment/data/equipment-details"):
        out.append({"kind": "equipment", "id": e["id"], "title": e["title"],
                    "facts": [e.get("price", {}).get("raw", "")], "keeper": True})
    for e in load("magic/data/grimoire-details"):
        out.append({"kind": "grimoire", "id": e["id"], "title": e["title"],
                    "facts": [str(e.get(k) or "") for k in ("sanityLoss", "mythosGain", "occultGain", "mythosRating", "studyTime")],
                    "keeper": e.get("sourceSet") == "keeper_rulebook"})
    for e in load("magic/data/spell-details"):
        out.append({"kind": "spell", "id": e["id"], "title": e["title"],
                    "facts": [json.dumps(e.get("cost"), ensure_ascii=False), json.dumps(e.get("castingTime"), ensure_ascii=False)],
                    "keeper": e.get("sourceSet") == "keeper_rulebook"})
    for e in load("monsters/data/monsters"):
        stats = e.get("stats") or {}
        out.append({"kind": "monster", "id": e["id"], "title": e["name"],
                    "facts": [json.dumps(stats, ensure_ascii=False)],
                    "keeper": str(e.get("source_set", "")).startswith("keeper_rulebook")})
    for rel, kind in (("sanity-health/data/phobia-details", "phobia"), ("sanity-health/data/mania-details", "mania")):
        for e in load(rel):
            out.append({"kind": kind, "id": e["id"], "title": e["title"], "facts": [],
                        "keeper": "GMentor" not in json.dumps(e.get("source"), ensure_ascii=False)})
    site = json.loads((docs / "weapons/data/weapons_for_site.json").read_text(encoding="utf-8"))
    stack = [site]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            if "damage" in x and "skill" in x:
                out.append({"kind": "weapon", "id": x["id"], "title": x["title"],
                            "facts": [str(x.get(k) or "") for k in ("damage", "range", "cost", "ammo", "malfunction")],
                            "keeper": x.get("sourceSet") == "keeper_book_core"})
            stack.extend(x.values())
        elif isinstance(x, list):
            stack.extend(x)
    cards = json.loads((docs / "reference/data/reference_cards_for_site.json").read_text(encoding="utf-8"))
    cards = cards if isinstance(cards, list) else next(v for v in cards.values() if isinstance(v, list))
    for c in cards:
        pages = sorted({int(s["page"]) for s in c.get("source") or [] if isinstance(s, dict) and str(s.get("page", "")).isdigit()})
        out.append({"kind": "reference_card", "id": c["id"], "title": c["title"],
                    "facts": [c.get("summary", "")], "keywords": c.get("summary", ""),
                    "pages_hint": pages, "keeper": True})
    return out


def check(book: Book, spec: dict) -> dict:
    res = {"kind": spec["kind"], "id": spec["id"], "title": spec["title"]}
    if not spec["keeper"]:
        res["status"] = "other_source"
        return res
    want = set().union(*(numbers(f) for f in spec["facts"])) if spec["facts"] else set()
    res["numbers"] = sorted(want)
    if spec["kind"] == "reference_card":
        kws = [t for t in set(tokens(spec["keywords"])) if len(t) >= 5]
        best = None
        for hint in spec.get("pages_hint") or []:
            for p in (hint - 1, hint, hint + 1):  # printed vs physical page offsets are unknown
                if p not in book.toks:
                    continue
                kw = sum(1 for t in kws if book.fuzzy(t) and any(a in book.toks[p] for a in book.fuzzy(t))) / max(len(kws), 1)
                nr = len(want & book.window_nums(p)) / len(want) if want else 1.0
                cand = (kw, nr, p)
                if best is None or cand > best:
                    best = cand
        if best is None:
            res["status"] = "no_page_ref"
            return res
        kw, nr, p = best
        res.update(page=p, keyword_recall=round(kw, 2), number_recall=round(nr, 2), page_grade=book.grade.get(p))
        res["status"] = "match" if kw >= 0.5 and nr == 1.0 else "needs_review"
        return res
    ttoks = tokens(spec["title"])
    if not ttoks:
        res["status"] = "title_not_tokenizable"
        return res
    cands = {p: s for p, s in book.pages_for(ttoks).items() if s >= 0.6}
    if not cands:
        res["status"] = "title_not_found"
        return res
    scored = []
    for p, s in cands.items():
        nr = len(want & book.window_nums(p)) / len(want) if want else 1.0
        scored.append((s, nr, -p))
    s, nr, negp = max(scored)
    p = -negp
    res.update(page=p, chapter=chapter_of(p), title_score=round(s, 2), number_recall=round(nr, 2),
               missing_numbers=sorted(want - book.window_nums(p)), page_grade=book.grade.get(p))
    if book.grade.get(p) in ("empty", "garbage"):
        res["status"] = "unverifiable_page_text"
    elif nr == 1.0:
        res["status"] = "match"
    else:
        res["status"] = "numbers_mismatch"
    return res


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", type=Path, required=True)
    ap.add_argument("--pages", type=Path, required=True)
    ap.add_argument("--quality", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    book = Book(a.pages, json.loads(a.quality.read_text(encoding="utf-8")))
    results = [check(book, s) for s in entry_specs(a.docs)]
    summary: dict = collections.defaultdict(collections.Counter)
    for r in results:
        summary[r["kind"]][r["status"]] += 1
    a.out.write_text(json.dumps({"summary": {k: dict(v) for k, v in summary.items()}, "entries": results},
                                ensure_ascii=False, indent=1), encoding="utf-8")
    for k, v in summary.items():
        print(k, dict(v))


if __name__ == "__main__":
    main()
