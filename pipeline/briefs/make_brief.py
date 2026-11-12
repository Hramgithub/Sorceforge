"""Make the brief of one extraction unit from an import plan (Р-139).

The brief is pipeline/briefs/extract.md filled from the plan, with docs/conventions.md appended verbatim:
the rules of writing are never retold by hand.

Plan (JSON, kept in the import's check folder, example: pipeline/briefs/examples/):
  {"book_id", "goal", "decision", "check_dir", "models": [paths], "extra": "text",
   "units": [{"name", "pages", "target", "owns": [paths or globs], "sites"}]}

Usage: python pipeline/briefs/make_brief.py <plan.json> <unit> [--out <file>]
       (default output: .cache/briefs/<book_id>-<unit>.md; prints the path)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("plan", type=Path)
    ap.add_argument("unit")
    ap.add_argument("--out", type=Path)
    a = ap.parse_args()
    plan = json.loads(a.plan.read_text(encoding="utf-8"))
    units = {u["name"]: u for u in plan["units"]}
    if a.unit not in units:
        sys.exit(f"нет части {a.unit}; в плане: {', '.join(units)}")
    u = units[a.unit]
    books = json.loads((ROOT / "pipeline/source/books.json").read_text(encoding="utf-8"))
    table = "| Unit | Pages | Target | Main sites |\n|---|---|---|---|\n" + "\n".join(
        f"| {x['name']} | {x['pages']} | {x.get('target', '')} | {x.get('sites', '')} |" for x in plan["units"])
    # a plan may cover several books: a unit's own "book_id" wins over the plan's
    book_id = u.get("book_id") or plan["book_id"]
    fill = {
        "book_id": book_id,
        "book_title": books.get(book_id, {}).get("title", book_id),
        "goal": plan["goal"],
        "decision": plan.get("decision", ""),
        "unit": u["name"],
        "target": u.get("target", ""),
        "pages": u["pages"],
        "check_dir": plan["check_dir"],
        "models": "\n".join(f"  - `{m}`" for m in plan.get("models", [])) or "  - (none yet: this is the pilot)",
        "owns": "\n".join(f"- `{o}`" for o in u["owns"]),
        "extra": plan.get("extra", ""),
        "units_table": table,
        "conventions": (ROOT / "docs/conventions.md").read_text(encoding="utf-8"),
    }
    text = (HERE / "extract.md").read_text(encoding="utf-8")
    for k, v in fill.items():
        text = text.replace("{{" + k + "}}", v)
    left = [p for p in ("{{",) if p in text]
    if left:
        sys.exit("в шаблоне остались незаполненные места {{…}}")
    out = a.out or ROOT / ".cache" / "briefs" / f"{book_id}-{u['name']}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8", newline="\n")
    print(out)


if __name__ == "__main__":
    main()
