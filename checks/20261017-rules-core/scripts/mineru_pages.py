"""Turn MinerU content_list.json outputs into per-page text files and merge them
over the PDF text-layer cache, so check_entries.py can re-run on MinerU text.

For every range folder under <run>/output, reads */ocr/*_content_list.json,
groups blocks by page (page_idx is relative to the range start), flattens
tables (HTML cells -> " | " separated rows) and writes pNNN.txt (physical page).
Also writes a quality JSON where MinerU pages are graded "mineru".

Usage: python mineru_pages.py --run <run dir> --base-pages <pdf_text dir>
                              --base-quality <pdf_text_quality.json>
                              --out-pages <dir> --out-quality <json>
"""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path

ROW = re.compile(r"<tr[^>]*>(.*?)</tr>", re.S | re.I)
CELL = re.compile(r"<t[dh][^>]*>(.*?)</t[dh]>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")


def table_text(table_html: str) -> str:
    rows = []
    for row in ROW.findall(table_html or ""):
        cells = [html.unescape(TAG.sub("", c)).strip() for c in CELL.findall(row)]
        rows.append(" | ".join(cells))
    return "\n".join(rows)


def block_text(block: dict) -> str:
    kind = block.get("type")
    if kind == "table":
        parts = [" ".join(block.get("table_caption") or []), table_text(block.get("table_body", "")),
                 " ".join(block.get("table_footnote") or [])]
        return "\n".join(p for p in parts if p)
    if kind in ("text", "title", "list", "equation", "header", "footer", "page_number"):
        text = block.get("text") or ""
        if not text and isinstance(block.get("list_items"), list):
            text = "\n".join(block["list_items"])
        return text
    if kind == "image":
        return " ".join(block.get("image_caption") or [])
    return block.get("text") or ""


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", type=Path, required=True)
    ap.add_argument("--base-pages", type=Path, required=True)
    ap.add_argument("--base-quality", type=Path, required=True)
    ap.add_argument("--out-pages", type=Path, required=True)
    ap.add_argument("--out-quality", type=Path, required=True)
    a = ap.parse_args()
    a.out_pages.mkdir(parents=True, exist_ok=True)
    for f in a.base_pages.glob("p*.txt"):
        shutil.copyfile(f, a.out_pages / f.name)
    replaced: list[int] = []
    for range_dir in sorted((a.run / "output").glob("p*-*")):
        start = int(range_dir.name[1:4])
        for cl in range_dir.rglob("*_content_list.json"):
            pages: dict[int, list[str]] = {}
            for block in json.loads(cl.read_text(encoding="utf-8")):
                pages.setdefault(start + int(block.get("page_idx", 0)), []).append(block_text(block))
            for p, texts in pages.items():
                (a.out_pages / f"p{p:03d}.txt").write_text("\n".join(t for t in texts if t), encoding="utf-8")
                replaced.append(p)
    quality = json.loads(a.base_quality.read_text(encoding="utf-8"))
    for page in quality["pages"]:
        if page["page"] in replaced:
            page["grade"] = "mineru"
    quality["mineru_pages"] = sorted(replaced)
    a.out_quality.write_text(json.dumps(quality, ensure_ascii=False, indent=1), encoding="utf-8")
    print("pages replaced by MinerU text:", len(replaced))


if __name__ == "__main__":
    main()
