"""Build the read-only knowledge base viewer: embed all records into one HTML file.

Sources: kb/<kind>/*.json and kb/books/*/<kind>/*.json for creatures, characters, skills,
occupations, spells, tomes, weapons, locations and maps (images in app/maps/); template tools/kb.template.html (placeholder
__DATA__); book titles from pipeline/source/books.json. Also renders the public landing page app/index.html from tools/landing.template.html
(placeholders __COUNT_<kind>__ and __UPDATED__).

Usage: python tools/build_viewer.py [--kb kb] [--template tools/kb.template.html] [--out app/kb.html]
"""
from __future__ import annotations

import argparse
import datetime
import json
import os
import time
from pathlib import Path


def load(kb: Path, kind: str) -> list[dict]:
    paths = sorted((kb / kind).glob("*.json")) + sorted((kb / "books").glob(f"*/{kind}/*.json"))
    return [json.loads(p.read_text(encoding="utf-8")) for p in paths]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser()
    ap.add_argument("--kb", type=Path, default=root / "kb")
    ap.add_argument("--template", type=Path, default=root / "tools" / "kb.template.html")
    ap.add_argument("--out", type=Path, default=root / "app" / "kb.html")
    a = ap.parse_args()
    data = {"maps": load(a.kb, "maps"), "creatures": load(a.kb, "creatures"), "characters": load(a.kb, "characters"), "skills": load(a.kb, "skills"),
            "occupations": load(a.kb, "occupations"), "spells": load(a.kb, "spells"), "tomes": load(a.kb, "tomes"), "weapons": load(a.kb, "weapons"), "locations": load(a.kb, "locations"),
            "items": load(a.kb, "items"), "handouts": load(a.kb, "handouts"), "organizations": load(a.kb, "organizations"), "scenes": load(a.kb, "scenes"),
            "scenarios": load(a.kb, "scenarios")}
    # book titles for display come from the one list of books (Р-148); only titles go to the page, never local paths
    books = json.loads((root / "pipeline" / "source" / "books.json").read_text(encoding="utf-8"))
    data["books"] = {k: v["title"] for k, v in books.items()}
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = a.template.read_text(encoding="utf-8").replace("__DATA__", payload)
    # written beside and swapped in: on Windows the page may be open in tools/kb_server.py at this moment
    tmp = a.out.with_suffix(".html.tmp")
    tmp.write_text(html, encoding="utf-8", newline="\n")
    for attempt in range(20):
        try:
            os.replace(tmp, a.out)
            break
        except OSError:
            if attempt == 19:
                raise
            time.sleep(0.25)
    landing = (root / "tools" / "landing.template.html").read_text(encoding="utf-8")
    for kind, records in data.items():
        landing = landing.replace(f"__COUNT_{kind}__", str(len(records)))
    months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    today = datetime.date.today()
    landing = landing.replace("__UPDATED__", f"{today.day} {months[today.month - 1]} {today.year}")
    (a.out.parent / "index.html").write_text(landing, encoding="utf-8", newline="\n")
    print(f"{len(data['creatures'])} creatures, {len(data['characters'])} characters, "
          f"{len(data['skills'])} skills, {len(data['occupations'])} occupations, {len(data['spells'])} spells, {len(data['tomes'])} tomes, {len(data['weapons'])} weapons, {len(data['locations'])} locations -> {a.out}")


if __name__ == "__main__":
    main()
