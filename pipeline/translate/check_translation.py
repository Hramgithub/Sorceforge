"""Check a page-by-page translation folder against its English source (Р-251).

Per physical page: English words of the text layer vs Russian words of NNN.md (flags pages below the ratio),
statblocks, handouts, tables, pictures; and for the whole folder: missing pages, picture links to files that do
not exist, the forbidden speed label «СКО», meta.json fields. Used after any translator — Claude helper or Codex.

    python -I -B pipeline/translate/check_translation.py <translation dir> <book_id> [--pages 1-23] [--min 0.7]

Exit code 1 when something must be fixed (missing page, broken picture, «СКО», no meta.json).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def page_range(spec: str | None, total: int) -> list[int]:
    if not spec:
        return list(range(1, total + 1))
    out: list[int] = []
    for part in spec.split(","):
        a, _, b = part.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("book")
    ap.add_argument("--pages", help="physical pages to expect, e.g. 1-49 (default: all pages of the book)")
    ap.add_argument("--min", type=float, default=0.7, help="flag pages with RU/EN word ratio below this")
    a = ap.parse_args()

    tr = Path(a.folder)
    if not tr.is_absolute():
        tr = ROOT / tr
    src = ROOT / ".cache" / "sources" / a.book / "text.txt"
    if not src.exists():
        print(f"нет текста книги: python pipeline/source/pages.py text {a.book}")
        return 1
    en_pages = src.read_text(encoding="utf-8").split("\f")
    if en_pages and not en_pages[-1].strip():
        en_pages = en_pages[:-1]
    pages = page_range(a.pages, len(en_pages))

    bad = 0
    meta = tr / "meta.json"
    if not meta.exists() and (not a.pages or pages[0] == 1):
        print("НЕТ meta.json"); bad += 1
    elif meta.exists():
        m = json.loads(meta.read_text(encoding="utf-8"))
        miss = [k for k in ("title_ru", "title_en", "book_id", "authors", "publisher", "year") if k not in m]
        if miss:
            print("meta.json без полей:", ", ".join(miss)); bad += 1

    totals = dict(stat=0, hand=0, tbl=0, img=0)
    low = []
    print("стр.   EN    RU  доля  статблоки раздатки таблицы картинки")
    for p in pages:
        f = tr / f"{p:03d}.md"
        en = len(re.findall(r"[A-Za-z]{2,}", en_pages[p - 1])) if p <= len(en_pages) else 0
        if not f.exists():
            print(f"{p:03d} {en:5d}     —  НЕТ ФАЙЛА"); bad += 1
            continue
        t = f.read_text(encoding="utf-8")
        for link in re.findall(r"!\[[^\]]*\]\(([^)\s]+)", t):
            if not (tr / link).exists():
                print(f"{p:03d}: картинки нет на диске — {link}"); bad += 1
        if re.search(r"\bСКО\b", t):
            print(f"{p:03d}: «СКО» — в статблоках пишется «Скорость:»"); bad += 1
        body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
        ru = len(re.findall(r"[А-Яа-яЁё]{2,}", body))
        r = ru / en if en else 0.0
        c = dict(stat=t.count("```stat"), hand=t.count("**Раздатка"),
                 tbl=len(re.findall(r"^\|[-: |]+\|\s*$", t, re.M)), img=len(re.findall(r"!\[", t)))
        for k in totals:
            totals[k] += c[k]
        flag = "  <<<" if en >= 40 and r < a.min else ""
        if flag:
            low.append(p)
        print(f"{p:03d} {en:5d} {ru:5d}  {r:4.2f}  {c['stat']:9d} {c['hand']:8d} {c['tbl']:7d} {c['img']:8d}{flag}")
    print(f"\nвсего: статблоков {totals['stat']}, раздаток {totals['hand']}, таблиц {totals['tbl']}, картинок {totals['img']}")
    if low:
        print("короткие страницы (проверить глазами, не пропущено ли):", ", ".join(f"{p:03d}" for p in low))
    print("ИСПРАВИТЬ: " + str(bad) if bad else "ошибок нет")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
