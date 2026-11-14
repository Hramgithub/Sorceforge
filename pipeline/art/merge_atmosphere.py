"""Merge a unit's atmosphere list into pipeline/art/atmosphere.json (Р-241).

A unit list is a JSON list of {book_id, physical_page, what}. Pages already in the main list get status «atmosphere»
and the description; new pages are added. Pages of the unit's books that the unit took as record art are not touched
here (the completeness check drops them once the record carries the picture).

Usage: python pipeline/art/merge_atmosphere.py checks/20261114-art/<unit>-atmosphere.json [...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

MAIN = Path(__file__).with_name("atmosphere.json")


def main() -> int:
    doc = json.loads(MAIN.read_text(encoding="utf-8"))
    by = {(p["book_id"], p["physical_page"]): p for p in doc["pages"]}
    added = updated = 0
    for f in sys.argv[1:]:
        for it in json.loads(Path(f).read_text(encoding="utf-8")):
            key = (it["book_id"], int(it["physical_page"]))
            p = by.get(key)
            if p is None:
                p = by[key] = {"book_id": key[0], "physical_page": key[1], "summary": ""}
                added += 1
            else:
                updated += 1
            p["status"] = "atmosphere"
            what = it.get("what") or it.get("note") or ""
            if what:
                p["what"] = what if not p.get("what") or what in p["what"] else p["what"] + "; " + what
    doc["pages"] = sorted(by.values(), key=lambda p: (p["book_id"], p["physical_page"]))
    MAIN.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"обновлено {updated}, добавлено {added}, всего {len(doc['pages'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
