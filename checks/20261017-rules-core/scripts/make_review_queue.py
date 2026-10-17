"""Build the layer-3 (semantic review) queue from layer-2 results.

Queue = entries with numbers_mismatch, title_not_found, title_not_tokenizable,
needs_review, no_page_ref, plus a seeded control sample of "match" entries.
Each item carries the helper's fact fields and the PDF pages to look at.
Unverifiable pages (empty/garbage text layer) are excluded: they need MinerU.

Usage: python make_review_queue.py --docs <public/docs> --entries <entries.json>
                                   --out <review_queue.json> [--control 25] [--seed 20261017]
"""
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

REVIEW_STATUSES = {"numbers_mismatch", "title_not_found", "title_not_tokenizable", "needs_review", "no_page_ref"}
CHAPTER_PAGES = {  # physical PDF pages of the chapter where the kind is expected
    "equipment": (363, 395), "weapon": (363, 395), "grimoire": (206, 217), "spell": (218, 246),
    "monster": (256, 321), "phobia": (143, 158), "mania": (143, 158), "reference_card": None,
}
DROP_FIELDS = {"searchText", "search_text", "normalizedTitle", "_file", "image", "images", "imagePath",
               "gmShortDescription", "sceneTrigger", "keeperExample", "mechanicalReminder",
               "psychoanalysisHint", "safetyNote", "tags", "families", "dataQuality", "data_quality"}


def helper_index(docs: Path) -> dict[tuple[str, str], dict]:
    idx: dict[tuple[str, str], dict] = {}
    dirs = {"equipment": "equipment/data/equipment-details", "grimoire": "magic/data/grimoire-details",
            "spell": "magic/data/spell-details", "monster": "monsters/data/monsters",
            "phobia": "sanity-health/data/phobia-details", "mania": "sanity-health/data/mania-details"}
    for kind, rel in dirs.items():
        for p in (docs / rel).glob("*.json"):
            e = json.loads(p.read_text(encoding="utf-8"))
            idx[(kind, e["id"])] = e
    stack = [json.loads((docs / "weapons/data/weapons_for_site.json").read_text(encoding="utf-8"))]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            if "damage" in x and "skill" in x:
                idx[("weapon", x["id"])] = x
            stack.extend(x.values())
        elif isinstance(x, list):
            stack.extend(x)
    cards = json.loads((docs / "reference/data/reference_cards_for_site.json").read_text(encoding="utf-8"))
    cards = cards if isinstance(cards, list) else next(v for v in cards.values() if isinstance(v, list))
    for c in cards:
        idx[("reference_card", c["id"])] = c
    return idx


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", type=Path, required=True)
    ap.add_argument("--entries", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--control", type=int, default=25)
    ap.add_argument("--seed", type=int, default=20261017)
    a = ap.parse_args()
    results = json.loads(a.entries.read_text(encoding="utf-8"))["entries"]
    idx = helper_index(a.docs)
    queue = [r for r in results if r["status"] in REVIEW_STATUSES]
    matches = sorted((r for r in results if r["status"] == "match"), key=lambda r: (r["kind"], r["id"]))
    control = random.Random(a.seed).sample(matches, min(a.control, len(matches)))
    items = []
    for r, reason in [(r, r["status"]) for r in queue] + [(r, "control_match") for r in control]:
        e = idx[(r["kind"], r["id"])]
        facts = {k: v for k, v in e.items() if k not in DROP_FIELDS}
        if r.get("page"):
            pages = [p for p in (r["page"] - 1, r["page"], r["page"] + 1) if p >= 1]
        elif r["kind"] == "reference_card":
            hints = sorted({int(s["page"]) for s in e.get("source") or [] if isinstance(s, dict) and str(s.get("page", "")).isdigit()})
            pages = sorted({q for h in hints for q in (h - 1, h, h + 1, h + 2)})
        else:
            lo, hi = CHAPTER_PAGES[r["kind"]]
            pages = list(range(lo, hi + 1))
        items.append({"kind": r["kind"], "id": r["id"], "reason": reason, "layer2": {k: r.get(k) for k in ("page", "number_recall", "missing_numbers", "keyword_recall")},
                      "pages": pages, "helper_facts": facts})
    a.out.write_text(json.dumps({"seed": a.seed, "count": len(items), "items": items}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("queue:", len(items), "control:", len(control))


if __name__ == "__main__":
    main()
