"""Write dice the same way everywhere in kb: 6d6, 1d100, (2d6+6)×5 (owner decision R-27).

Replaces the Russian «к» and the capital «D» between digits («6к6», «6 к 6», «6D6») with a lowercase «d»
in every string of every kb JSON file. Text without digits on both sides is left alone.

Usage: python pipeline/fix/normalize_dice.py [--kb kb] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

DICE = re.compile(r"(?<=\d)\s*[кКD]\s*(?=\d)")


def fix(value, counter: list[int]):
    if isinstance(value, str):
        new = DICE.sub("d", value)
        if new != value:
            counter[0] += 1
        return new
    if isinstance(value, list):
        return [fix(v, counter) for v in value]
    if isinstance(value, dict):
        return {k: fix(v, counter) for k, v in value.items()}
    return value


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=Path(__file__).resolve().parents[2] / "kb")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = strings = 0
    for p in sorted(a.kb.rglob("*.json")):
        counter = [0]
        rec = fix(json.loads(p.read_text(encoding="utf-8")), counter)
        if counter[0]:
            files += 1
            strings += counter[0]
            if not a.dry_run:
                p.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{strings} strings in {files} files" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
