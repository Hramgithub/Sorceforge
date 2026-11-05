"""Bring kb text to the Keeper Rulebook terms and one file format.

- Characteristic abbreviations as in the Russian Keeper Rulebook: «РАЗ» and «ВЕЛ» (SIZ) → «ТЕЛ», «ОЗ» (HP) → «ПЗ», «ЛОВ» (DEX) → «ЛВК»
  (whole uppercase words only, so «раз», «озеро» and the like are untouched).
- Every given kb JSON file is written in the kb format: UTF-8, 2-space indent, LF line endings (tools/kblib.py).

Usage: python pipeline/fix/normalize_terms.py (<files|dirs> | --changed | --all) [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import dump, read, scope, scope_args  # noqa: E402

TERMS = [(re.compile(r"(?<![А-ЯЁа-яё])(?:РАЗ|ВЕЛ)(?![А-ЯЁа-яё])"), "ТЕЛ"),
         (re.compile(r"(?<![А-ЯЁа-яё])ОЗ(?![А-ЯЁа-яё])"), "ПЗ"),
         (re.compile(r"(?<![А-ЯЁа-яё])ЛОВ(?![А-ЯЁа-яё])"), "ЛВК")]


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
        # quoted as it was: a correction's «from» and a misprint's «printed» keep the old writing
        return {k: v if k in ("from", "printed") else fix(v, counter) for k, v in value.items()}
    return value


def main() -> None:
    ap = argparse.ArgumentParser()
    scope_args(ap)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    strings = rewritten = 0
    for p in scope(ap, a):
        counter = [0]
        before = p.read_bytes()
        after = dump(fix(read(p), counter)).encode("utf-8")
        strings += counter[0]
        if after != before:
            rewritten += 1
            if not a.dry_run:
                p.write_bytes(after)
    print(f"{strings} strings with terms fixed; {rewritten} files rewritten" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
