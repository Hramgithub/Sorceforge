"""Coverage map: Keeper Rulebook chapters vs content present in the web helper.

Counts helper records per book chapter, using the helper's own source fields
(reference cards, skills, sanity rule cards) and the known chapter of each
entity section. Writes JSON only.

Usage: python coverage.py --docs <public/docs> --out <coverage.json>
"""
from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

CHAPTERS = {
    1: "Введение", 2: "Г. Ф. Лавкрафт и Мифы", 3: "Создание сыщиков", 4: "Навыки", 5: "Игровая система",
    6: "Бой", 7: "Погони", 8: "Рассудок", 9: "Магия", 10: "Ход игры", 11: "Книги Мифов",
    12: "Гримуар (заклинания)", 13: "Артефакты и инопланетные устройства", 14: "Чудовища, твари и боги",
    15: "Сценарии", 16: "Приложения (снаряжение, оружие, справки)",
}
SECTION_CHAPTER = {"equipment": 16, "weapon_core": 16, "grimoire_core": 11, "spell_core": 12,
                   "monster_core": 14, "phobia": 8, "mania": 8}
CH = re.compile(r"Глава\s+(\d{1,2})", re.I)


def chapter_nums(obj) -> set[int]:
    return {int(m) for m in CH.findall(json.dumps(obj, ensure_ascii=False))}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    d = a.docs
    per = collections.defaultdict(collections.Counter)

    cards = json.loads((d / "reference/data/reference_cards_for_site.json").read_text(encoding="utf-8"))
    cards = cards if isinstance(cards, list) else next(v for v in cards.values() if isinstance(v, list))
    for c in cards:
        for ch in chapter_nums(c.get("source")) or {0}:
            per[ch]["reference_cards"] += 1
    skills = json.loads((d / "reference/data/reference_skills.json").read_text(encoding="utf-8"))
    skills = skills if isinstance(skills, list) else next(v for v in skills.values() if isinstance(v, list))
    per[4]["skills"] += len(skills)
    rules = d / "sanity-health/data/sanity-rule-cards.json"
    if rules.exists():
        r = json.loads(rules.read_text(encoding="utf-8"))
        r = r if isinstance(r, list) else next((v for v in r.values() if isinstance(v, list)), [])
        per[8]["sanity_rule_cards"] += len(r)

    inv = json.loads((a.out.parent / "inventory.json").read_text(encoding="utf-8"))["sections"]
    per[16]["equipment"] += inv["equipment"]["sources"].get("keeper_rulebook", 0)
    per[16]["weapons"] += inv["weapon"]["sources"].get("keeper_book_core", 0)
    per[11]["grimoires"] += inv["grimoire"]["sources"].get("keeper_rulebook", 0)
    per[12]["spells"] += inv["spell"]["sources"].get("keeper_rulebook", 0)
    per[14]["monsters"] += sum(v for k, v in inv["monster"]["sources"].items() if k.startswith("keeper_rulebook"))
    per[8]["phobias"] += inv["phobia"]["entries"]
    per[8]["manias"] += sum(v for k, v in inv["mania"]["sources"].items() if "GMentor" not in k)

    occupations = [p for p in d.rglob("*.json") if re.search(r"occupation|profession|profess", p.name, re.I)]
    rows = []
    for ch, title in CHAPTERS.items():
        counts = dict(per.get(ch, {}))
        rows.append({"chapter": ch, "title": title, "helper_records": counts, "total": sum(counts.values())})
    out = {"chapters": rows, "unassigned_reference_cards": per[0].get("reference_cards", 0),
           "occupation_files": [p.name for p in occupations],
           "notes": ["Chapter 15 (scenarios) is excluded by the helper's own design."]}
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    for r in rows:
        print(r["chapter"], r["total"], r["helper_records"])
    print("occupation files:", len(occupations), "unassigned cards:", out["unassigned_reference_cards"])


if __name__ == "__main__":
    main()
