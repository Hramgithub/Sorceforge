"""Add pictures to kb records (Р-165): shrink copies into app/art/ and write proposals that add them to `images`.

The mapping is a JSON list, one item per picture:
  {"target": "<record id>", "src": "<original file>", "kind": "art|portrait|card|handout|plan|illustration|photo",
   "caption": "…", "source": "where it comes from"}
Each picture is saved as app/art/<record kind>s/<record slug>[-<n>].webp, at most 1400 px on the long side, WebP
quality 80; the originals stay where they are. The proposals file is written next to the mapping
(<mapping>-proposals.json) for pipeline/integrate/apply.py.

Usage: python pipeline/art/add_images.py <mapping.json> [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools"))
from kblib import ROOT, index, read  # noqa: E402

MAX_SIDE, QUALITY = 1400, 80


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("mapping", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    from PIL import Image
    Image.MAX_IMAGE_PIXELS = None
    where = index()
    items = json.loads(a.mapping.read_text(encoding="utf-8"))
    taken: dict[str, int] = {}
    props, size = [], 0
    for it in items:
        if it["target"] not in where:
            print(f"нет записи {it['target']}")
            return 1
        src = Path(it["src"])
        if not src.exists():
            print(f"нет файла {src}")
            return 1
        rec = read(where[it["target"]])
        slug = rec["id"].split("/")[-1].split(":")[-1]
        n = taken.get(rec["id"], len(rec.get("images") or []))
        taken[rec["id"]] = n + 1
        rel = f"art/{rec['kind']}s/{slug}{'-' + str(n + 1) if n else ''}.webp"
        out = ROOT / "app" / rel
        if not a.dry_run:
            im = Image.open(src)
            im = im.convert("RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB")
            im.thumbnail((MAX_SIDE, MAX_SIDE))
            out.parent.mkdir(parents=True, exist_ok=True)
            im.save(out, "WEBP", quality=QUALITY, method=6)
            size += out.stat().st_size
        props.append({"target": it["target"], "op": "append", "path": "images",
                      "value": {"file": rel, "kind": it["kind"], "caption": it.get("caption"), "source": it.get("source")},
                      "reason": "картинка записи", "ref": "Р-165", "correction": False})
    dst = a.mapping.with_name(a.mapping.stem + "-proposals.json")
    if not a.dry_run:
        dst.write_text(json.dumps({"schema": "sourcefold.proposals.v0", "by": f"картинки из {a.mapping.name}", "proposals": props},
                                  ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"картинок: {len(props)}, записей: {len(taken)}, объём копий: {size / 1e6:.1f} МБ → {dst.relative_to(ROOT) if dst.is_relative_to(ROOT) else dst}"
          + (" (пробный прогон)" if a.dry_run else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
