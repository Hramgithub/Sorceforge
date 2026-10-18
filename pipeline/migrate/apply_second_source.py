"""Apply image-checked locations of existing creatures in another book (second source).

Input: JSONL with {"id", "page", "verdict": same|differs|absent, "differences": [...], "note"}.
- same / differs: the book's source gets the checked physical page, printed page
  (physical + offset) and verified=true; for "differs" the book's values are listed in
  quality.notes (the record's values stay canonical, decision R-19);
- absent: the book's source is removed.
Each difference is {"field", "book"} (older files use "rulebook" instead of "book").

Usage: python pipeline/migrate/apply_second_source.py --kb kb/creatures --checked <jsonl>
       [--book-id keeper-rulebook-ru --offset 21 --title «Книге хранителя»]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, required=True)
    ap.add_argument("--checked", type=Path, required=True)
    ap.add_argument("--book-id", default="keeper-rulebook-ru")
    ap.add_argument("--offset", type=int, default=21, help="printed page = physical page + offset")
    ap.add_argument("--title", default="«Книге хранителя»", help="book name in the prepositional case")
    ap.add_argument("--canon", default="основного источника", help="whose values the record keeps, for the note")
    a = ap.parse_args()
    for line in a.checked.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        c = json.loads(line)
        p = a.kb / f"{c['id'].split(':')[-1]}.json"
        rec = json.loads(p.read_text(encoding="utf-8"))
        others = [s for s in rec["sources"] if s["book_id"] != a.book_id]
        if c["verdict"] == "absent":
            rec["sources"] = others
            note = f"в {a.title} статблока нет"
        else:
            rec["sources"] = others + [{"book_id": a.book_id, "physical_page": c["page"],
                                        "printed_page": c["page"] + a.offset if c["page"] else None,
                                        "method": "book_text", "verified": True}]
            if c["verdict"] == "differs":
                diffs = "; ".join(f"{d['field']} {d.get('book', d.get('rulebook'))}" for d in c.get("differences", []))
                note = f"в {a.title} другие значения: {diffs}; в записи — значения {a.canon} (Р-19)"
            else:
                note = None
        q = rec.setdefault("quality", {"needs_review": False, "flags": [], "notes": None})
        if note:
            q["notes"] = "; ".join(x for x in (q.get("notes"), note) if x)
        p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"{c['verdict']:8} {p.stem}")


if __name__ == "__main__":
    main()
