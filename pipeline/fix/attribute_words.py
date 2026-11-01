"""Sanity, Move, Build and Luck are written as words in our texts (Р-146).

«РАС» → «Рассудок» / «Рассудка», «СКО» → «Скорость» / «Скорости», «SAN» → «Рассудок», «MOV» → «Скорость», by the words
around them. Text quoted as printed stays: `raw`, a correction's `from`/`to`/`reason`, a misprint's `printed`,
`source_variants`. Every changed field gets a `corrections` item. What no rule fits is listed for a hand fix.

Usage: python pipeline/fix/attribute_words.py (<files|dirs> | --changed | --all) [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import read, scope, scope_args, write  # noqa: E402

W = r"(?<![А-ЯЁа-яё])"
E = r"(?![А-ЯЁа-яё])"
SAN = rf"{W}(?:РАС{E}|SAN\b)"
MOV = rf"{W}(?:СКО{E}|MOV\b)"
# (pattern, replacement) in order; the genitive after a word or a number that governs it, else the nominative
RULES = [
    (re.compile(rf"([Пп]отер[яиюе]\s+){SAN}"), r"\1Рассудка"),
    (re.compile(rf"((?:пункт(?:ов|а)?|максимума?|проверк[уаи])\s+){SAN}"), r"\1Рассудка"),
    (re.compile(rf"((?:\d|d\d+)\s*){SAN}(?!\s*\d)"), r"\1Рассудка"),
    (re.compile(rf"(\|\s*){SAN}(\s*\|)"), r"\1Рассудок\2"),
    (re.compile(SAN), "Рассудок"),
    (re.compile(rf"((?:[кК]|до|от)\s+){MOV}"), r"\1Скорости"),
    (re.compile(MOV), "Скорость"),
]
ANY = re.compile(rf"{SAN}|{MOV}")
KEEP = {"raw", "from", "to", "reason", "printed"}


def fix(value, path, changes):
    if isinstance(value, dict):
        return {k: (v if k in KEEP or k == "source_variants" or k == "corrections" else fix(v, f"{path}.{k}" if path else k, changes))
                for k, v in value.items()}
    if isinstance(value, list):
        return [fix(v, f"{path}[{i}]", changes) for i, v in enumerate(value)]
    if isinstance(value, str) and ANY.search(value):
        new = value
        for pat, repl in RULES:
            new = pat.sub(repl, new)
        changes.append((path, value, new))
        return new
    return value


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    scope_args(ap)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    files = fields = 0
    for p in scope(ap, a):
        rec = read(p)
        changes: list[tuple[str, str, str]] = []
        new = fix(rec, "", changes)
        if not changes:
            continue
        files += 1
        fields += len(changes)
        for path, old, text in changes:
            words = sorted(set(m.group(0) for m in ANY.finditer(old)))
            new.setdefault("corrections", []).append({"field": path, "from": ", ".join(words), "to": "словами: Рассудок, Скорость",
                                                      "reason": "в наших текстах Рассудок и Скорость пишутся словами", "ref": "Р-146"})
            if a.dry_run:
                print(f"{p.name}: {path}: …{old[:0]}{text[:160]}")
        if not a.dry_run:
            write(p, new)
    print(f"{fields} fields in {files} files" + (" (dry run)" if a.dry_run else ""))


if __name__ == "__main__":
    main()
