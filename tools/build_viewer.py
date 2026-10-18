"""Build the read-only creatures viewer: embed kb/creatures/*.json into one HTML file.

Usage: python tools/build_viewer.py [--kb kb/creatures] [--template app/creatures.template.html]
                                     [--out app/creatures.html]
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=root / "kb" / "creatures")
    ap.add_argument("--template", type=Path, default=root / "app" / "creatures.template.html")
    ap.add_argument("--out", type=Path, default=root / "app" / "creatures.html")
    a = ap.parse_args()
    records = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(a.kb.glob("*.json"))]
    payload = json.dumps(records, ensure_ascii=False).replace("</", "<\\/")
    html = a.template.read_text(encoding="utf-8").replace("__DATA__", payload)
    a.out.write_text(html, encoding="utf-8")
    print(f"{len(records)} creatures -> {a.out}")


if __name__ == "__main__":
    main()
