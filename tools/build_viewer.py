"""Build the read-only knowledge base viewer: embed all records into one HTML file.

Sources: kb/<kind>/*.json and kb/books/*/<kind>/*.json for creatures, characters, skills,
occupations, spells, tomes, weapons, rule tables, rules, locations and maps (images in app/maps/); template tools/kb.template.html (placeholder
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
            "scenarios": load(a.kb, "scenarios"), "tables": load(a.kb, "tables"), "rules": load(a.kb, "rules"), "archetypes": load(a.kb, "archetypes"), "talents": load(a.kb, "talents")}
    # book titles for display come from the one list of books (Р-148); only titles go to the page, never local paths
    books = json.loads((root / "pipeline" / "source" / "books.json").read_text(encoding="utf-8"))
    data["books"] = {k: v["title"] for k, v in books.items()}
    # editions of one work (the Russian volume II and player materials of «Masks») are one book in filters and guides
    data["works"] = {k: v["work"] for k, v in books.items() if v.get("work")}
    data["workTitles"] = {k: v["work_title"] for k, v in books.items() if v.get("work_title")}
    # chapters of rules books (first printed page, title): the rules list groups by them (Р-180, Р-182)
    data["chapters"] = {k: v["chapters"] for k, v in books.items() if v.get("chapters")}
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
    landing = landing.replace("__PROGRESS__", progress_html(root, books))
    (a.out.parent / "index.html").write_text(landing, encoding="utf-8", newline="\n")
    print(f"{len(data['creatures'])} creatures, {len(data['characters'])} characters, "
          f"{len(data['skills'])} skills, {len(data['occupations'])} occupations, {len(data['spells'])} spells, {len(data['tomes'])} tomes, {len(data['weapons'])} weapons, {len(data['tables'])} tables, {len(data['rules'])} rules, {len(data['locations'])} locations -> {a.out}")


KIND_RU = {"creature": "существа", "character": "персонажи", "location": "места", "scene": "сцены", "scenario": "сценарии",
           "item": "предметы", "handout": "раздатки", "organization": "организации", "map": "карты", "rule": "правила",
           "table": "таблицы", "spell": "заклинания", "tome": "книги Мифов", "weapon": "оружие", "skill": "навыки",
           "occupation": "профессии", "archetype": "архетипы", "talent": "таланты", "term": "термины"}


def progress_html(root: Path, books: dict) -> str:
    """The progress of the base (Р-210): every work of the owner's library catalogue (pipeline/source/catalog.json) —
    «добавлено в базу» when a registered book lies in its folder and has records, otherwise «известно»."""
    import html as h
    cat_path = root / "pipeline" / "source" / "catalog.json"
    if not cat_path.exists():
        return ""
    works = json.loads(cat_path.read_text(encoding="utf-8"))
    # records by book and kind
    by_book: dict = {}
    for p in (root / "kb").rglob("*.json"):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for b in {s.get("book_id") for s in r.get("sources") or []}:
            by_book.setdefault(b, {}).setdefault(r.get("kind"), 0)
            by_book[b][r.get("kind")] += 1
    # a book belongs to the work whose folder holds its file (the longest such folder)
    folder_of = {}
    for bid, b in books.items():
        pdf = (b.get("pdf") or "").replace("/", "\\")
        if "1_Библиотека\\" in pdf:
            folder_of[bid] = pdf.split("1_Библиотека\\", 1)[1].rsplit("\\", 1)[0]
    counts: dict = {}
    for bid, folder in folder_of.items():
        owners = [w for w in works if folder == w["folder"] or folder.startswith(w["folder"] + "\\")]
        if not owners:
            continue
        w = max(owners, key=lambda w: len(w["folder"]))
        for k, n in by_book.get(bid, {}).items():
            counts.setdefault(w["folder"], {}).setdefault(k, 0)
            counts[w["folder"]][k] += n
    order = ["Правила", "Кампании", "Сборники", "Сценарии", "Сеттинги", "Монографии", "Журналы", "Путеводители",
             "Атмосфера", "Карты", "Прочее", "_Другие системы"]
    types = sorted({w["type"] for w in works}, key=lambda t: (order.index(t) if t in order else 99, t))
    added_total = sum(1 for w in works if counts.get(w["folder"]))
    parts = [f'<p class="muted">Каталог библиотеки: {len(works)} книг и сценариев, добавлено в базу — {added_total}. '
             'Статус «добавлено» — когда у книги есть записи в базе; число рядом — сколько и каких.</p>']
    for t in types:
        ws = [w for w in works if w["type"] == t]
        ws.sort(key=lambda w: (not counts.get(w["folder"]), w["work"].lower()))
        added = sum(1 for w in ws if counts.get(w["folder"]))
        rows = []
        for w in ws:
            c = counts.get(w["folder"])
            what = ", ".join(f"{KIND_RU.get(k, k)} {n}" for k, n in sorted(c.items(), key=lambda x: -x[1])) if c else ""
            status = '<span class="st added">добавлено в базу</span>' if c else '<span class="st known">известно</span>'
            era = h.escape((w.get("era") or "")[:60])
            ed = h.escape(", ".join(w.get("editions") or []))
            rows.append(f"<tr><td>{h.escape(w['work'])}</td><td>{ed}</td><td>{era}</td><td>{status}</td><td class=\"what\">{h.escape(what)}</td></tr>")
        label = t.lstrip("_")
        parts.append(f'<details{" open" if added else ""}><summary>{h.escape(label)} <span class="muted">— {added} из {len(ws)}</span></summary>'
                     '<table class="progress"><tr><th>Книга</th><th>Издания</th><th>Эпоха</th><th>Статус</th><th>В базе</th></tr>'
                     + "".join(rows) + "</table></details>")
    return "\n".join(parts)


if __name__ == "__main__":
    main()
