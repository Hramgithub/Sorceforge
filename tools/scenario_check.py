"""Integrity of every scenario as a work: plot, scenes, characters, clues and handouts, pictures, pages.

Read-only. A scenario's family is the scenario record, its scenes (`arc.scenario`), every record they refer to, and the
book records whose source pages lie inside the scenario's page span (from the first to the last page that the
scenario and its scenes cite). For each scenario:
  plot       summary, keeper information, hook, steps, conclusion; step references that do not resolve;
  scenes     scenes without place, without participants, without outcome; scenes no step and no other scene leads to;
  characters book characters of the scenario's pages that neither the scenario nor any of its scenes names;
  clues      handouts and items of the scenario's pages that no scene and no step uses; handouts without text and picture;
  art        characters, creatures and handouts of the family with and without pictures;
  pages      pages of the span with text (≥ 120 words) that no record cites.
Writes `report.md` (one row per scenario, then findings by scenario) and `findings.json`.

Usage:
  python tools/scenario_check.py                         → checks/<today>-scenarios/
  python tools/scenario_check.py --books dveri-vo-tmu-ru  only these books
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit import COMMON, Audit  # noqa: E402
from completeness import BOOKS, WORD_RE, text_of_book, printed_list, phys, ru  # noqa: E402
from kblib import ROOT  # noqa: E402

CHECKS = {
    "plot.missing": "Нет части сюжета (summary / keeper_info / hook / steps / conclusion)",
    "plot.bad_ref": "Шаг сюжета ссылается на несуществующую запись",
    "scenes.none": "У сценария нет сцен",
    "scenes.no_place": "Сцена без места",
    "scenes.no_people": "Сцена без участников",
    "scenes.no_outcome": "Сцена без итога (outcome)",
    "scenes.unreached": "Сцену не называет ни шаг сюжета, ни другая сцена",
    "people.lost": "Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены",
    "clues.unused": "Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг",
    "clues.empty": "Раздатка без текста и без картинки",
    "pages.gap": "Страница сценария с текстом, которую не цитирует ни одна запись",
}


def refs_in(v, a: Audit, path="") -> set[str]:
    return {t for _, t in a._refs(v, path)}


class ScenarioCheck:
    def __init__(self, a: Audit, only: set[str] | None):
        self.a, self.only = a, only
        self.rows, self.findings = [], []
        self.scenes = defaultdict(list)
        for i, r in a.recs.items():
            if r.get("kind") == "scene":
                s = (r.get("arc") or {}).get("scenario")
                if s:
                    self.scenes[s].append(i)
        # book records by (book, physical page)
        self.on_page = defaultdict(lambda: defaultdict(set))
        for i, r in a.recs.items():
            for s in r.get("sources") or []:
                bid = s.get("book_id")
                if bid in BOOKS and isinstance(s.get("physical_page"), int):
                    self.on_page[bid][s["physical_page"]].add(i)
        self.texts = {}
        # first page of every scenario by book; and the family of every scenario (to leave others' records alone)
        self.starts = defaultdict(list)
        self.families = {}
        for i, r in a.recs.items():
            if r.get("kind") != "scenario":
                continue
            bid = next((s["book_id"] for s in r.get("sources") or [] if s.get("book_id") in BOOKS), None)
            if bid:
                st = self.start(i, bid)
                if st:
                    self.starts[bid].append((st, i))
            fam = {i} | set(self.scenes.get(i, []))
            for x in list(fam):
                body = {k: v for k, v in a.recs[x].items() if k not in ("sources", "corrections", "errata", "quality", "arc", "id")}
                fam |= refs_in(body, a)
            self.families[i] = fam
        for v in self.starts.values():
            v.sort()

    def add(self, check, sid, summary, conf, i=None, **extra):
        f = {"check": check, "scenario": sid, "scenario_name": self.a.name(sid), "book": self.a.book(sid),
             "summary": summary, "confidence": conf}
        if i:
            f.update(id=i, name=self.a.name(i))
        f.update({k: v for k, v in extra.items() if v not in (None, "", [])})
        self.findings.append(f)

    def start(self, sid: str, bid: str) -> int | None:
        """The scenario's title page: its own cited page nearest before its first scene (a page of the book's contents
        or introduction that the record also cites is not the start)."""
        own = [s["physical_page"] for s in self.a.recs[sid].get("sources") or []
               if s.get("book_id") == bid and isinstance(s.get("physical_page"), int)]
        sc = [s["physical_page"] for i in self.scenes.get(sid, []) for s in self.a.recs[i].get("sources") or []
              if s.get("book_id") == bid and isinstance(s.get("physical_page"), int)]
        if sc:
            before = [p for p in own if p <= min(sc)]
            return max(before) if before else min(sc)
        return max(own) if len(own) > 1 and max(own) - min(own) > 20 else (min(own) if own else None)

    def span(self, sid: str, bid: str) -> tuple[int, int] | None:
        """Pages of the scenario's chapter: from its first page to the last page of its scenes (appendix pages that the
        scenario cites in notes are left out — they would cover the chapters of other scenarios)."""
        own = [s["physical_page"] for s in self.a.recs[sid].get("sources") or []
               if s.get("book_id") == bid and isinstance(s.get("physical_page"), int)]
        sc = [s["physical_page"] for i in self.scenes.get(sid, []) for s in self.a.recs[i].get("sources") or []
              if s.get("book_id") == bid and isinstance(s.get("physical_page"), int)]
        if not own and not sc:
            return None
        first = self.start(sid, bid)
        last = max(sc) if sc else max(own)
        # other scenarios of the book that start inside: stop before them
        for o in self.starts.get(bid, []):
            if o[1] != sid and first < o[0] <= last:
                last = o[0] - 1
        return (first, max(first, last))

    def one(self, sid: str):
        a, r = self.a, self.a.recs[sid]
        bid = next((s["book_id"] for s in r.get("sources") or [] if s.get("book_id") in BOOKS), None)
        scenes = sorted(self.scenes.get(sid, []), key=lambda i: (a.recs[i].get("arc") or {}).get("order") or 0)
        solo = bool(r.get("solo"))
        row = {"scenario": sid, "name": a.name(sid), "book": a.book(sid), "solo": solo, "scenes": len(scenes)}
        # --- plot
        miss = [k for k in ("summary", "keeper_info", "hook", "conclusion") if not ru(r.get(k))]
        if not r.get("steps") and not solo:
            miss.append("steps")
        if solo:
            miss = [m for m in miss if m in ("summary",)]
        if miss:
            self.add("plot.missing", sid, "нет: " + ", ".join(miss), "high" if "summary" in miss or len(miss) > 2 else "medium")
        for st in r.get("steps") or []:
            for t in st.get("refs") or []:
                if t not in a.recs:
                    self.add("plot.bad_ref", sid, f"шаг «{st.get('title')}» → {t}", "high")
        # --- family
        fam_refs = refs_in({k: v for k, v in r.items() if k not in ("sources", "corrections", "errata", "quality")}, a)
        stepped = refs_in(r.get("steps") or [], a)
        reached = set(stepped)
        for i in scenes:
            sr = a.recs[i]
            body = {k: v for k, v in sr.items() if k not in ("sources", "corrections", "errata", "quality", "arc", "id")}
            out = refs_in(body, a)
            fam_refs |= out
            reached |= {t for t in out if a.recs.get(t, {}).get("kind") == "scene"}
            if not solo:
                if not sr.get("where"):
                    self.add("scenes.no_place", sid, "сцена без места", "low", i)
                if not sr.get("participants"):
                    self.add("scenes.no_people", sid, "сцена без участников", "low", i)
                if not ru(sr.get("outcome")):
                    self.add("scenes.no_outcome", sid, "сцена без итога", "low", i)
        if not scenes and not solo:
            self.add("scenes.none", sid, "у сценария нет сцен (arc.scenario)", "high")
        if r.get("steps"):
            for i in scenes:
                if i not in reached:
                    self.add("scenes.unreached", sid, "сцену не называет ни шаг, ни другая сцена", "medium", i)
        fam = {sid} | set(scenes) | fam_refs
        # --- book records of the scenario's pages
        sp = self.span(sid, bid) if bid else None
        row["pages"] = f"{sp[0]}–{sp[1]}" if sp else "—"
        local = set()
        if sp:
            for p in range(sp[0], sp[1] + 1):
                local |= {i for i in self.on_page[bid].get(p, ()) if a.book(i) != COMMON or a.recs[i].get("kind") == "character"}
        # records of other scenarios' families are not ours; a record linked to any member of the family (in or out,
        # e.g. a resident of a place of the scenario, a member of its cult) is not lost
        other_fam = set().union(*(f for o, f in self.families.items() if o != sid)) if self.families else set()
        used_in_text = ru(r.get("keeper_info")) + ru(r.get("conclusion")) + ru(r.get("summary"))
        fam_own = {x for x in fam if x in a.recs and a.book(x) != COMMON}     # shared cities do not make a link
        for i in sorted(local - fam - other_fam):
            k = a.recs[i].get("kind")
            linked = any(s in fam_own for s, _ in a.inc.get(i, [])) or any(t in fam_own for _, t in a.out.get(i, []))
            if linked:
                continue
            if k == "character":
                if a.name(i) and a.name(i) in used_in_text:
                    continue
                ins = []
                if not ins:
                    self.add("people.lost", sid, "персонаж страниц сценария не назван ни в сценарии, ни в сценах", "medium", i)
            elif k in ("handout", "item"):
                ins = []
                if not ins:
                    self.add("clues.unused", sid, f"{k} страниц сценария не использует ни сцена, ни шаг", "medium" if k == "handout" else "low", i)
        fam |= {i for i in local if a.recs[i].get("kind") in ("character", "creature", "handout", "item")}
        # --- clues and art
        kinds = Counter()
        pics = Counter()
        for i in fam:
            k = a.recs.get(i, {}).get("kind")
            if k in ("character", "creature", "handout", "item", "location", "map"):
                kinds[k] += 1
                if a.recs[i].get("images") or k == "map":
                    pics[k] += 1
            if k == "handout" and not ru(a.recs[i].get("text")) and not a.recs[i].get("images"):
                self.add("clues.empty", sid, "раздатка без текста и картинки", "high", i)
        for k in ("character", "creature", "handout", "item", "location", "map"):
            row[k] = f"{kinds[k]}" + (f" ({pics[k]})" if k in ("character", "creature", "handout") else "")
        # --- pages
        if sp and bid:
            if bid not in self.texts:
                self.texts[bid] = text_of_book(bid, BOOKS[bid])[0]
            texts = self.texts[bid]
            cited = {p for p, ids in self.on_page[bid].items() if ids}
            gaps = [p for p in range(sp[0], sp[1] + 1) if texts and p <= len(texts) and p not in cited
                    and len(WORD_RE.findall(texts[p - 1])) >= 120]
            if gaps and not solo:
                self.add("pages.gap", sid, "страницы без записей: физ. " + ", ".join(map(str, gaps)), "medium" if len(gaps) > 1 else "low",
                         pages=gaps)
            row["gaps"] = len(gaps) if not solo else 0
        row["findings"] = sum(1 for f in self.findings if f["scenario"] == sid)
        self.rows.append(row)

    def run(self):
        for sid, r in sorted(self.a.recs.items()):
            if r.get("kind") == "scenario" and (not self.only or self.a.book(sid) in self.only):
                self.one(sid)


def report(c: ScenarioCheck) -> str:
    cnt = Counter(f["check"] for f in c.findings)
    L = [f"# Целостность сценариев — {datetime.date.today().isoformat()}", "",
         "Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они "
         "ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.", "",
         "## Итог по проверкам", "", "| Проверка | Что ищется | Находок |", "|---|---|---|"]
    L += [f"| `{k}` | {t} | {cnt.get(k, 0)} |" for k, t in CHECKS.items()]
    L += ["", "## Сценарии", "",
          "| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(c.rows, key=lambda r: (-r["findings"], r["book"])):
        L.append(f"| {r['name']}{' (соло)' if r['solo'] else ''} | `{r['book']}` | {r['pages']} | {r['scenes']} | {r['character']} | "
                 f"{r['creature']} | {r['handout']} | {r['item']} | {r['location']} | {r['map']} | {r.get('gaps', '—')} | {r['findings']} |")
    L += ["", "## Находки по сценариям", ""]
    by = defaultdict(list)
    for f in c.findings:
        by[f["scenario"]].append(f)
    order = {"high": 0, "medium": 1, "low": 2}
    for sid in sorted(by, key=lambda s: -len(by[s])):
        fs = sorted(by[sid], key=lambda f: (order[f["confidence"]], f["check"]))
        L += [f"### {c.a.name(sid)} (`{sid}`) — {len(fs)}", ""]
        for f in fs:
            head = f"`{f['id']}` {f['name']} — " if f.get("id") else ""
            L.append(f"- [{f['confidence']}] `{f['check']}` {head}{f['summary']}")
        L.append("")
    return "\n".join(L) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=f"checks/{datetime.date.today().strftime('%Y%m%d')}-scenarios")
    ap.add_argument("--books", default="")
    a = ap.parse_args()
    c = ScenarioCheck(Audit(), set(a.books.split(",")) - {""} or None)
    c.run()
    out = ROOT / a.out
    out.mkdir(parents=True, exist_ok=True)
    (out / "findings.json").write_text(json.dumps({"scenarios": c.rows, "findings": c.findings}, ensure_ascii=False, indent=2) + "\n",
                                       encoding="utf-8", newline="\n")
    (out / "report.md").write_text(report(c), encoding="utf-8", newline="\n")
    print(f"сценариев: {len(c.rows)}")
    for k, v in sorted(Counter(f["check"] for f in c.findings).items()):
        print(f"{k} — {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
