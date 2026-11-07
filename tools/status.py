"""Summary of the knowledge base for README and the handoff: records by kind, pictures, books, open marks.

Usage: python tools/status.py [--md]
  --md  print Markdown tables ready to paste
"""
from __future__ import annotations

import argparse
import collections
import json
import subprocess
import sys

from kblib import ROOT, records

KIND_RU = {
    "creature": "Существа", "character": "Персонажи", "skill": "Навыки", "occupation": "Профессии",
    "spell": "Заклинания", "tome": "Книги Мифов", "weapon": "Оружие", "location": "Места", "map": "Карты",
    "scenario": "Сценарии", "scene": "Сцены", "item": "Предметы", "handout": "Документы для игроков",
    "organization": "Организации",
}


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", action="store_true")
    a = ap.parse_args()
    kinds, pics, flags, books = collections.Counter(), collections.Counter(), collections.Counter(), collections.Counter()
    by_book = collections.defaultdict(collections.Counter)
    for _, r in records():
        k = r.get("kind")
        if not k:
            continue
        kinds[k] += 1
        if r.get("images"):
            pics[k] += 1
        for f in (r.get("quality") or {}).get("flags", []):
            flags[f] += 1
        src = (r.get("sources") or [{}])[0].get("book_id")
        if src:
            books[src] += 1
            by_book[src][k] += 1
    reg = json.loads((ROOT / "pipeline/source/books.json").read_text(encoding="utf-8"))
    reg = reg.get("books", reg)
    decisions = [l.split("|")[1].strip() for l in (ROOT / "docs/project-goal.md").read_text(encoding="utf-8").splitlines()
                 if l.startswith("| Р-")]
    head = subprocess.run(["git", "log", "-1", "--format=%h %cs"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    order = [k for k in KIND_RU if k in kinds] + sorted(k for k in kinds if k not in KIND_RU)
    if a.md:
        print(f"Состояние на {head}; решения {decisions[0]}…{decisions[-1]}.\n")
        print("| Вид | Записей | С картинкой |\n|---|---|---|")
        for k in order:
            print(f"| {KIND_RU.get(k, k)} | {kinds[k]} | {pics[k] or '—'} |")
        print(f"| **Всего** | **{sum(kinds.values())}** | **{sum(pics.values())}** |\n")
        print("| Книга (первый источник записи) | Записей | Что |\n|---|---|---|")
        for b, n in books.most_common():
            what = ", ".join(f"{KIND_RU.get(k, k).lower()} {c}" for k, c in by_book[b].most_common())
            print(f"| {(reg.get(b) or {}).get('title', b)} | {n} | {what} |")
    else:
        print(f"git {head}; решения {decisions[0]}…{decisions[-1]} ({len(decisions)})")
        print("записей:", sum(kinds.values()), {k: kinds[k] for k in order})
        print("с картинкой:", sum(pics.values()), {k: pics[k] for k in order if pics[k]})
        print("пометки:", dict(flags))
        print("книг-источников:", len(books), "| в реестре:", len(reg), "| без записей:",
              sorted(b for b in reg if b not in books))
    return 0


if __name__ == "__main__":
    sys.exit(main())
