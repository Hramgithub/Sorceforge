"""Consistency pass over kb creatures after translation (owner decisions R-32, R-33).

- Move wording in statblock.move.raw: «летая» → «полёт», «плавая» → «плавание», «паря» → «парение».
- Flag `parse_uncertain` («опечатка книги») is set exactly on records that have `errata`.
- Skill names: a skill whose `name` is a known alias or a near variant of a kb/skills name gets the kb/skills Russian name.
- Reports strings that still contain English words (outside names, aliases, spell lists, ids and sources).

Usage: python pipeline/fix/consistency.py [--kb kb] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MOVE = [(re.compile(r"\bлетая\b"), "полёт"), (re.compile(r"\bплавая\b"), "плавание"), (re.compile(r"\bпаря\b"), "парение")]
SKILL_FIX = {"Внимательность": "Внимание", "Слесарное дело": "Взлом"}
LAT = re.compile(r"[A-Za-z]{4,}")
SKIP = {"en", "aliases", "spells", "sources", "id", "schema", "kind", "category", "target", "type", "refs", "skill", "dice",
        "flags", "era", "ruleset", "mode", "ref", "formula", "same_as", "book_id", "method"}


def english(v, path, out):
    if isinstance(v, dict):
        for k, x in v.items():
            if k not in SKIP:
                english(x, f"{path}.{k}", out)
    elif isinstance(v, list):
        for i, x in enumerate(v):
            english(x, f"{path}[{i}]", out)
    elif isinstance(v, str) and LAT.search(re.sub(r"\b\d*d\d+\b", "", v)):
        out.append((path, v[:90]))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=Path(__file__).resolve().parents[2] / "kb")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    changed, moves, flags, skills, eng = 0, 0, 0, 0, []
    for p in sorted(list(a.kb.glob("creatures/*.json")) + list(a.kb.glob("books/*/creatures/*.json"))):
        before = p.read_bytes()
        r = json.loads(before.decode("utf-8"))
        sb = r.get("statblock") or {}
        mv = sb.get("move")
        if mv and mv.get("raw"):
            new = mv["raw"]
            for pat, repl in MOVE:
                new = pat.sub(repl, new)
            if new != mv["raw"]:
                mv["raw"] = new
                moves += 1
        q = r.setdefault("quality", {"needs_review": False, "flags": [], "notes": None})
        fl = q.setdefault("flags", [])
        has = bool(r.get("errata"))
        if has and "parse_uncertain" not in fl:
            fl.append("parse_uncertain"); flags += 1
        if not has and "parse_uncertain" in fl:
            fl.remove("parse_uncertain"); flags += 1
        for s in sb.get("skills", []):
            for wrong, right in SKILL_FIX.items():
                if s["name"].startswith(wrong):
                    s["name"] = right + s["name"][len(wrong):]
                    skills += 1
        english({k: v for k, v in r.items() if k not in ("name", "aliases", "sources", "corrections", "errata")}, r["id"], eng)
        after = (json.dumps(r, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        if after != before:
            changed += 1
            if not a.dry_run:
                p.write_bytes(after)
    print(f"files changed {changed}; move wording {moves}; parse_uncertain flags fixed {flags}; skill names {skills}")
    print(f"strings with English left: {len(eng)}")
    for path, text in eng[:60]:
        print(f"  {path}: {text}")


if __name__ == "__main__":
    main()
