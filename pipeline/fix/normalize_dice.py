"""Write dice the same way everywhere in kb: 6d6, 1d100, (2d6+6)×5 (owner decision R-27).

Replaces the Russian «к» and the capital «D» between digits («6к6», «6 к 6», «6D6») with a lowercase «d»
in every string of the given kb files. Text without digits on both sides is left alone, and «к» counts only before
a die size, so ratios like «1 к 1» stay as written. Files are written in the kb format (tools/kblib.py).

Usage: python pipeline/fix/normalize_dice.py (<files|dirs> | --changed | --all) [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import read, scope, scope_args, write  # noqa: E402

DICE = re.compile(r"(?<=\d)\s*(?:D|[кК](?=\s*(?:100|20|12|10|[2-468])(?!\d)))\s*(?=\d)")


def fix(value, counter: list[int]):
    if isinstance(value, str):
        new = DICE.sub("d", value)
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
    files = strings = 0
    for p in scope(ap, a):
        counter = [0]
        rec = fix(read(p), counter)
        if counter[0]:
            files += 1
            strings += counter[0]
            if not a.dry_run:
                write(p, rec)
    print(f"{strings} strings in {files} files" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
