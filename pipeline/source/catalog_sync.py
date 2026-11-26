"""The owner's library catalogue → pipeline/source/catalog.json (Р-210).

Every work of the library (`1_Библиотека`) has a `_описание.md` with a YAML front matter (work, type, kind, era,
editions…). This script reads them all and writes one list with the progress of the base. A work is «добавлено в базу»
(`added: true`) when it has records in kb/:
  1. a registered book (books.json) lies in the work's folder (the longest such folder) and has records — `via: folder`;
  2. or the work is named in pipeline/source/catalog_links.json (work folder → record ids and/or book ids, checked by
     hand): the work lives inside another book (the Russian Keeper Rulebook, a collection, a starter set, a magazine) or
     its book is registered from another folder (`2_Обработка`) — `via: link`.
Otherwise the work is «известно». `in_base` gives the records by kind; `books` / `records` — what was counted.
Title matching (scenario names and aliases, book titles against the work title) only prints suggestions (--suggest);
a suggestion becomes a status only after it is checked and written to catalog_links.json, so no false «added» appears.
Local paths stay in this repository file, never on the page.

Usage: python pipeline/source/catalog_sync.py [<library root>] [--suggest]
"""
from __future__ import annotations

import json
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "pipeline" / "source"
DEFAULT = pathlib.Path(json.loads((SRC / "library.json").read_text(encoding="utf-8"))["folders"][0]["path"])
LIB_PART = "1_Библиотека\\"


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


def norm(s: str) -> str:
    """Title key: lower case, ё→е, no accents, punctuation and articles dropped."""
    s = unicodedata.normalize("NFKD", s.lower().replace("ё", "е"))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^\w]+", " ", s).strip()
    s = re.sub(r"^(the|a|an) ", "", s)
    return s


def titles(work: str, folder: str) -> set[str]:
    """«Некрополис (Necropolis)» → {некрополис, necropolis, некрополис necropolis}; also the folder's last part."""
    out = set()
    for t in (work, folder.rsplit("\\", 1)[-1]):
        out.add(norm(t))
        m = re.match(r"^(.*?)\s*\((.*)\)\s*$", t)
        if m:
            out.add(norm(m.group(1)))
            out.add(norm(m.group(2)))
    return {t for t in out if len(t) >= 4}


def load_kb():
    """Records by book (book_id → {kind: n}), scenario-like records, and an index id → record summary."""
    by_book: dict = {}
    recs: dict = {}
    for p in (ROOT / "kb").rglob("*.json"):
        try:
            r = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        if not isinstance(r, dict) or "id" not in r:
            continue
        for b in {s.get("book_id") for s in r.get("sources") or []}:
            by_book.setdefault(b, {}).setdefault(r.get("kind"), 0)
            by_book[b][r.get("kind")] += 1
        up = []
        for v in (r.get("arc"), r.get("part_of")):  # arc: {"scenario": id, "part", "order"}; part_of: id
            for x in (v if isinstance(v, list) else [v]):
                x = x.get("scenario") if isinstance(x, dict) else x
                if isinstance(x, str):
                    up.append(x)
        recs[r["id"]] = {"kind": r.get("kind"), "name": r.get("name") or {}, "aliases": r.get("aliases") or [],
                         "up": up, "refs": r.get("refs") or []}
    return by_book, recs


def scenario_counts(ids: list[str], recs: dict) -> dict:
    """Linked records with what belongs to them. A scenario brings the records whose `arc`/`part_of` is it and the
    records of the same book it refers to (characters, places, handouts); any other record (a pregen, a handout)
    counts alone."""
    for i in ids:
        if i not in recs:
            raise SystemExit(f"catalog_links.json: no record {i}")
    take = set(ids)
    scen = {i for i in ids if recs[i]["kind"] == "scenario"}
    done: set = set()
    while scen - done:  # chapters of a campaign (part_of) and their scenes (arc), down to the last level
        new = scen - done
        done |= new
        for i in new:
            prefix = i.split("/", 1)[0] + "/"
            take.update(x for x in recs[i]["refs"] if isinstance(x, str) and x.startswith(prefix) and x in recs)
        kids = {k for k, r in recs.items() if any(u in new for u in r["up"])}
        take |= kids
        scen |= {k for k in kids if recs[k]["kind"] == "scenario"}
    out: dict = {}
    for k in take:
        out[recs[k]["kind"]] = out.get(recs[k]["kind"], 0) + 1
    return out


def add_counts(a: dict, b: dict) -> None:
    for k, n in b.items():
        a[k] = a.get(k, 0) + n


def main() -> int:
    sys.stdout.reconfigure(encoding="utf-8")
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    lib = pathlib.Path(args[0]) if args else DEFAULT
    works = []
    for p in sorted(lib.rglob("_описание.md")):
        f = front(p.read_text(encoding="utf-8", errors="replace"))
        folder = str(p.parent.relative_to(lib))
        works.append({"work": f.get("work") or p.parent.name, "type": f.get("type") or folder.split("\\")[0],
                      "kind": f.get("kind") or None, "era": f.get("era") or None, "editions": f.get("editions") or [],
                      "folder": folder})

    books = json.loads((SRC / "books.json").read_text(encoding="utf-8"))
    links_path = SRC / "catalog_links.json"
    links = json.loads(links_path.read_text(encoding="utf-8")).get("links", {}) if links_path.exists() else {}
    by_book, recs = load_kb()
    folders = {w["folder"] for w in works}
    for f in links:
        if f not in folders:
            raise SystemExit(f"catalog_links.json: no work folder {f}")

    # 1. a registered book lies in the work's folder (the longest such folder)
    for w in works:
        w.update(added=False, via=None, books=[], records=[], in_base={})
    wmap = {w["folder"]: w for w in works}
    for bid, b in books.items():
        pdf = (b.get("pdf") or "").replace("/", "\\")
        if LIB_PART not in pdf:
            continue
        folder = pdf.split(LIB_PART, 1)[1].rsplit("\\", 1)[0]
        owners = [f for f in folders if folder == f or folder.startswith(f + "\\")]
        if owners and by_book.get(bid):
            w = wmap[max(owners, key=len)]
            w["books"].append(bid)
            add_counts(w["in_base"], by_book[bid])
            w["via"] = "folder"
    # 2. hand-checked links
    for f, link in links.items():
        w = wmap[f]
        for bid in link.get("books", []):
            if bid not in books:
                raise SystemExit(f"catalog_links.json: no book {bid}")
            if bid not in w["books"] and by_book.get(bid):
                w["books"].append(bid)
                add_counts(w["in_base"], by_book[bid])
        if link.get("records"):
            w["records"] = list(link["records"])
            add_counts(w["in_base"], scenario_counts(link["records"], recs))
        w["via"] = w["via"] or "link"
    for w in works:
        w["added"] = bool(w["in_base"])
        if not w["added"]:
            w["via"] = None
        w["books"].sort()
        w["in_base"] = dict(sorted(w["in_base"].items(), key=lambda x: (-x[1], x[0] or "")))

    out = SRC / "catalog.json"
    out.write_text(json.dumps(works, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    added = sum(w["added"] for w in works)
    print(f"{len(works)} работ, добавлено в базу — {added} (по папке {sum(w['via'] == 'folder' for w in works)}, "
          f"по связям {sum(w['via'] == 'link' for w in works)}) → {out.relative_to(ROOT)}")

    if "--suggest" in sys.argv:
        # 3. suggestions only: titles of scenario records and of registered books that match a work still «известно»
        names: dict = {}
        for rid, r in recs.items():
            if r["kind"] != "scenario":
                continue
            for t in [r["name"].get("en"), r["name"].get("ru"), *[a for a in r["aliases"] if isinstance(a, str)]]:
                if t:
                    names.setdefault(norm(t), set()).add(rid)
        for bid, b in books.items():
            if by_book.get(bid) and b.get("title"):
                names.setdefault(norm(b["title"]), set()).add("book:" + bid)
        for w in works:
            if w["added"]:
                continue
            hit = sorted({x for t in titles(w["work"], w["folder"]) for x in names.get(t, ())})
            if hit:
                print(f"? {w['folder']} ← {', '.join(hit)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
