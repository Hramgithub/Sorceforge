"""Apply image-checked Keeper Rulebook locations to Malleus-sourced creatures.

Input: JSONL with {"id", "page", "verdict": same|differs|absent, "differences": [...], "note"}.
- same / differs: the keeper-rulebook-ru source gets the checked physical page, printed page
  (+21 in chapter 14) and verified=true; for "differs" the rulebook values are listed in
  quality.notes (Malleus values stay canonical, decision R-19);
- absent: the keeper-rulebook-ru source is removed (the creature is Malleus-only).

Usage: python pipeline/migrate/apply_second_source.py --kb kb/creatures --checked <jsonl>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

CH14_OFFSET = 21


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, required=True)
    ap.add_argument("--checked", type=Path, required=True)
    a = ap.parse_args()
    for line in a.checked.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        c = json.loads(line)
        p = a.kb / f"{c['id'].split(':')[-1]}.json"
        rec = json.loads(p.read_text(encoding="utf-8"))
        others = [s for s in rec["sources"] if s["book_id"] != "keeper-rulebook-ru"]
        if c["verdict"] == "absent":
            rec["sources"] = others
            note = "в «Книге хранителя» статблока нет; источник — только Malleus Keeper Deck"
        else:
            rec["sources"] = others + [{"book_id": "keeper-rulebook-ru", "physical_page": c["page"],
                                        "printed_page": c["page"] + CH14_OFFSET if c["page"] else None,
                                        "method": "book_text", "verified": True}]
            if c["verdict"] == "differs":
                diffs = "; ".join(f"{d['field']} {d['rulebook']}" for d in c.get("differences", []))
                note = f"в «Книге хранителя» другие значения: {diffs}; в записи — значения Malleus (Р-19)"
            else:
                note = None
        q = rec.setdefault("quality", {"needs_review": False, "flags": []})
        if note:
            q["notes"] = "; ".join(x for x in (q.get("notes"), note) if x)
        p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{c['verdict']:8} {p.stem}")


if __name__ == "__main__":
    main()
