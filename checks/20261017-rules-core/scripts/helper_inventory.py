"""Inventory of the Keeper web helper data (git_coc/web_helper_coc_gm/public/docs).

Reports per section: entry count, source distribution, verification flags,
duplicate files, and how many fact fields are typed vs stored as strings.
Writes JSON only; no book text is copied.

Usage: python helper_inventory.py --docs <public/docs> --out <inventory.json>
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path

SECTIONS = {
    "equipment": "equipment/data/equipment-details",
    "grimoire": "magic/data/grimoire-details",
    "spell": "magic/data/spell-details",
    "monster": "monsters/data/monsters",
    "mania": "sanity-health/data/mania-details",
    "phobia": "sanity-health/data/phobia-details",
}

# Fields that look like editorial text written for the app rather than taken from the book.
EDITORIAL_FIELDS = {
    "mania": ["gmShortDescription", "sceneTrigger", "keeperExample", "mechanicalReminder", "psychoanalysisHint", "safetyNote"],
    "phobia": ["gmShortDescription", "sceneTrigger", "keeperExample", "mechanicalReminder", "psychoanalysisHint"],
    "equipment": ["description"],
}


def load_dir(path: Path) -> list[dict]:
    return [json.loads(p.read_text(encoding="utf-8")) | {"_file": p.name} for p in sorted(path.glob("*.json"))]


def source_key(entry: dict) -> str:
    for key in ("sourceSet", "source_set"):
        if entry.get(key):
            return str(entry[key])
    src = entry.get("source")
    if isinstance(src, list) and src:
        src = src[0]
    if isinstance(src, dict):
        return str(src.get("book") or src.get("source") or src.get("chapter") or "unknown")[:60]
    return "unknown"


def flag_count(entries: list[dict]) -> dict:
    out = collections.Counter()
    for e in entries:
        if e.get("needsVerification") is True:
            out["needsVerification"] += 1
        dq = e.get("dataQuality") or e.get("data_quality")
        if isinstance(dq, dict) and dq.get("needsManualVerification"):
            out["needsManualVerification"] += 1
        flags = (dq or {}).get("flags", []) if isinstance(dq, dict) else []
        for f in flags:
            out["flag:" + str(f)[:40]] += 1
        for f in e.get("qualityFlags") or []:
            out["qualityFlag:" + str(f)[:40]] += 1
    return dict(out.most_common(15))


def monster_model_fit(entries: list[dict]) -> dict:
    fit = collections.Counter()
    for e in entries:
        fit["total"] += 1
        fit["has_stat_block_string"] += isinstance(e.get("stat_block"), str)
        fit["has_characteristics_typed"] += isinstance(e.get("characteristics"), (list, dict))
        fit["combat_is_string"] += isinstance(e.get("combat"), str)
        fit["skills_is_string"] += isinstance(e.get("skills"), str)
        fit["spells_is_string"] += isinstance(e.get("spells"), str)
        fit["sanity_loss_is_string"] += isinstance(e.get("sanity_loss"), str)
        fit["has_raw_source_text"] += bool(e.get("raw_source_text"))
    return dict(fit)


def weapons(docs: Path) -> list[dict]:
    site = json.loads((docs / "weapons/data/weapons_for_site.json").read_text(encoding="utf-8"))
    items: list[dict] = []

    def walk(x):
        if isinstance(x, dict):
            if "damage" in x and "skill" in x:
                items.append(x)
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)

    walk(site)
    return items


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    report: dict = {"sections": {}}
    for kind, rel in SECTIONS.items():
        entries = load_dir(a.docs / rel)
        sec = {
            "entries": len(entries),
            "sources": dict(collections.Counter(source_key(e) for e in entries).most_common()),
            "flags": flag_count(entries),
            "editorial_fields": [f for f in EDITORIAL_FIELDS.get(kind, []) if any(f in e for e in entries)],
        }
        if kind == "monster":
            sec["model_fit"] = monster_model_fit(entries)
        report["sections"][kind] = sec
    w = weapons(a.docs)
    report["sections"]["weapon"] = {
        "entries": len(w),
        "sources": dict(collections.Counter(str(x.get("sourceSet")) for x in w).most_common()),
        "flags": flag_count(w),
        "model_fit": {"damage_is_string": sum(isinstance(x.get("damage"), str) for x in w),
                      "cost_is_string": sum(isinstance(x.get("cost"), str) for x in w)},
    }
    cards = json.loads((a.docs / "reference/data/reference_cards_for_site.json").read_text(encoding="utf-8"))
    cards = cards if isinstance(cards, list) else next(v for v in cards.values() if isinstance(v, list))
    report["sections"]["reference_card"] = {
        "entries": len(cards),
        "with_page": sum(1 for c in cards if any(isinstance(s, dict) and s.get("page") for s in (c.get("source") or []))),
        "flags": flag_count(cards),
    }
    dupes = sorted(p.name for p in a.docs.rglob("* 3.json"))
    report["duplicate_files"] = {"count": len(dupes), "files": dupes}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    for k, v in report["sections"].items():
        print(k, v["entries"], v.get("sources", ""))
    print("duplicate files:", len(dupes))


if __name__ == "__main__":
    main()
