"""Extract the PDF text layer page by page (Poppler pdftotext) and score its quality.

Writes per-page text to a local cache (not committed) and a per-page quality
summary JSON (committed). No book text is written to the summary.

Usage:
  python pdf_text_quality.py --pdf <book.pdf> --pdftotext <pdftotext.exe>
                             --cache <dir> --out <quality.json>
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

WORD = re.compile(r"\S+")
GOOD = re.compile(r"^[А-Яа-яЁё]{3,}[.,:;!?»)]?$|^[«(]?[А-Яа-яЁё]{3,}$")
NUM = re.compile(r"\d")


def page_count(pdf: Path, pdftotext: Path) -> int:
    pdfinfo = pdftotext.with_name("pdfinfo.exe")
    out = subprocess.run([str(pdfinfo), str(pdf)], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    return int(re.search(r"^Pages:\s+(\d+)", out, re.M).group(1))


def score(text: str) -> dict:
    words = WORD.findall(text)
    good = sum(1 for w in words if GOOD.match(w))
    return {
        "chars": len(text),
        "words": len(words),
        "good_ratio": round(good / len(words), 3) if words else 0.0,
        "has_digits": bool(NUM.search(text)),
    }


def grade(s: dict) -> str:
    if s["words"] < 20:
        return "empty"
    if s["good_ratio"] >= 0.6:
        return "good"
    if s["good_ratio"] >= 0.4:
        return "noisy"
    return "garbage"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pdf", type=Path, required=True)
    ap.add_argument("--pdftotext", type=Path, required=True)
    ap.add_argument("--cache", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    a.cache.mkdir(parents=True, exist_ok=True)
    n = page_count(a.pdf, a.pdftotext)
    pages = []
    for p in range(1, n + 1):
        cached = a.cache / f"p{p:03d}.txt"
        if not cached.exists():
            text = subprocess.run(
                [str(a.pdftotext), "-f", str(p), "-l", str(p), "-layout", "-enc", "UTF-8", str(a.pdf), "-"],
                capture_output=True,
            ).stdout.decode("utf-8", "replace")
            cached.write_text(text, encoding="utf-8")
        s = score(cached.read_text(encoding="utf-8"))
        s["page"] = p
        s["grade"] = grade(s)
        pages.append(s)
    summary = {g: sum(1 for x in pages if x["grade"] == g) for g in ("good", "noisy", "garbage", "empty")}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps({"pdf_pages": n, "summary": summary, "pages": pages}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("pages:", n, summary)


if __name__ == "__main__":
    main()
