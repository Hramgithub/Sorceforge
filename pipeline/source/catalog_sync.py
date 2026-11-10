"""The owner's library catalogue → pipeline/source/catalog.json (Р-210).

Every work of the library (`1_Библиотека`) has a `_описание.md` with a YAML front matter (work, type, kind, era,
editions…). This script reads them all and writes one list. The viewer's landing page shows it as the progress of the
base: «добавлено в базу» when a registered book (books.json) lies in the work's folder and has records, otherwise
«известно». Local paths stay in this repository file, never on the page.

Usage: python pipeline/source/catalog_sync.py [<library root>]
"""
from __future__ import annotations

import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
DEFAULT = pathlib.Path(r"C:\_Hobby\Yandex.Disk\НРИ\1_Зов Ктулху\1_Библиотека")


def front(text: str) -> dict:
    m = re.match(r"---\s*\n(.*?)\n---", text, re.S)
    out = {}
    if not m:
        return out
    for line in m.group(1).splitlines():
        k = re.match(r"^(\w+):\s*(.*)$", line)
        if not k:
            continue
        key, val = k.group(1), k.group(2).strip()
        if val.startswith("["):
            out[key] = [v.strip().strip("'\"") for v in val.strip("[]").split(",") if v.strip()]
        else:
            out[key] = val.strip("'\"")
    return out


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    lib = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    works = []
    for p in sorted(lib.rglob("_описание.md")):
        f = front(p.read_text(encoding="utf-8", errors="replace"))
        folder = str(p.parent.relative_to(lib))
        works.append({"work": f.get("work") or p.parent.name, "type": f.get("type") or folder.split("\\")[0],
                      "kind": f.get("kind") or None, "era": f.get("era") or None, "editions": f.get("editions") or [],
                      "folder": folder})
    out = ROOT / "pipeline" / "source" / "catalog.json"
    out.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(works)} работ → {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
