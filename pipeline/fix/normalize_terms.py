"""Bring kb text to the Keeper Rulebook terms and one file format.

- Characteristic abbreviations as in the Russian Keeper Rulebook: «РАЗ» and «ВЕЛ» (SIZ) → «ТЕЛ», «ОЗ» (HP) → «ПЗ»
  (whole uppercase words only, so «раз», «озеро» and the like are untouched).
- Every kb JSON file is written as UTF-8, 2-space indent, LF line endings.

Usage: python pipeline/fix/normalize_terms.py [--kb kb] [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

TERMS = [(re.compile(r"(?<![А-ЯЁа-яё])(?:РАЗ|ВЕЛ)(?![А-ЯЁа-яё])"), "ТЕЛ"),
         (re.compile(r"(?<![А-ЯЁа-яё])ОЗ(?![А-ЯЁа-яё])"), "ПЗ")]


def fix(value, counter: list[int]):
    if isinstance(value, str):
        new = value
        for pattern, repl in TERMS:
            new = pattern.sub(repl, new)
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
    strings = rewritten = 0
    for p in sorted(a.kb.rglob("*.json")):
        counter = [0]
        before = p.read_bytes()
        rec = fix(json.loads(before.decode("utf-8")), counter)
        after = (json.dumps(rec, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        strings += counter[0]
        if after != before:
            rewritten += 1
            if not a.dry_run:
                p.write_bytes(after)
    print(f"{strings} strings with terms fixed; {rewritten} files rewritten" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
