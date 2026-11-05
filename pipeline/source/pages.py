"""Read a source book by its pages (Р-139): text, search, page images and crops.

Books are registered in pipeline/source/books.json: book_id → pdf path, offset (printed page − offset = physical
page in the PDF), language, edition, notes. Edition (Р-147): `original` — the publisher's original; `official` —
an official translation; `trusted` — a translation the owner marked as reliable; `machine` — a machine translation,
never a source (the tool refuses to read it). The text layer is taken once with Poppler `pdftotext -layout` into the local cache
`.cache/sources/<book_id>/` (not in git); page images go there too. Pages are printed pages unless --physical.

A new book is registered with `register`: its edition comes from the owner's folder it lies in
(pipeline/source/library.json, Р-149); a file with «машинн» in its name is a machine translation and is refused.

Usage:
  python pipeline/source/pages.py register <book_id> <pdf> --title "…" [--offset N] [--edition E]
  python pipeline/source/pages.py text  <book_id> [--force]          take the text layer into the cache
  python pipeline/source/pages.py show  <book_id> 76 80-82 [--physical]
  python pipeline/source/pages.py grep  <book_id> <regex> [--pages 76-97]
  python pipeline/source/pages.py image <book_id> <page> [--dpi 150] [--physical]
  python pipeline/source/pages.py crop  <png> x0 y0 x1 y1 [--rotate 90]   fractions of width and height
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOKS = Path(__file__).with_name("books.json")
CACHE = ROOT / ".cache" / "sources"
POPPLER = Path(r"C:\Tools\Poppler\poppler-26.02.0\Library\bin")


def tool(name: str) -> str:
    found = shutil.which(name) or (POPPLER / f"{name}.exe")
    if not Path(found).exists():
        sys.exit(f"нет {name}: поставь Poppler или поправь POPPLER в {__file__}")
    return str(found)


def book(book_id: str) -> dict:
    books = json.loads(BOOKS.read_text(encoding="utf-8"))
    if book_id not in books:
        sys.exit(f"книга {book_id} не записана в {BOOKS.relative_to(ROOT)}; известны: {', '.join(books)}")
    b = books[book_id]
    if b.get("edition") not in ("original", "official", "trusted"):
        sys.exit(f"{book_id}: издание «{b.get('edition')}» не источник (Р-147): нужен оригинал, официальный перевод или перевод, отмеченный владельцем")
    return b


def register(a) -> None:
    """Add a book to books.json; the edition is the one of the owner's folder the PDF lies in (Р-149)."""
    pdf = Path(a.pdf).resolve()
    if not pdf.exists():
        sys.exit(f"нет файла {pdf}")
    lib_doc = json.loads(BOOKS.with_name("library.json").read_text(encoding="utf-8"))
    # the owner's files carry the edition in front of the name: «[RU 7e] …», «[RU-ИИ 7e] …», «[EN 6e] …» (Р-164)
    tag = re.match(r"^\[([A-Za-zА-Яа-я-]+)", pdf.name)
    by_tag = lib_doc.get("tags", {}).get(tag.group(1)) if tag else None
    if by_tag == "machine" or re.search("машинн", pdf.name, re.I):
        sys.exit(f"{pdf.name}: машинный перевод — не источник (Р-147)")
    lib = lib_doc["folders"]
    home = next((f for f in lib if str(pdf).lower().startswith(f["path"].lower() + "\\")), None)
    edition = a.edition or by_tag or (home or {}).get("edition")
    if not edition:
        sys.exit(f"{pdf} лежит вне папок pipeline/source/library.json: укажи --edition (original, official, trusted), если владелец подтвердил издание")
    books = json.loads(BOOKS.read_text(encoding="utf-8"))
    if a.book in books:
        sys.exit(f"{a.book} уже записана")
    books[a.book] = {"title": a.title, "edition": edition, "pdf": str(pdf), "lang": (home or {}).get("lang", "ru" if a.book.endswith("-ru") else "en")}
    if a.offset is not None:
        books[a.book]["offset"] = a.offset
    BOOKS.write_text(json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"{a.book}: {a.title}, издание {edition}")


def pages_arg(items: list[str]) -> list[int]:
    out = []
    for a in items:
        x, _, y = a.partition("-")
        out += list(range(int(x), int(y or x) + 1))
    return out


def text_pages(book_id: str) -> list[str]:
    """Physical pages of the cached text layer; page 1 is index 0."""
    t = CACHE / book_id / "text.txt"
    if not t.exists():
        sys.exit(f"нет текста: сначала `python pipeline/source/pages.py text {book_id}`")
    return t.read_text(encoding="utf-8").split("\f")


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("register"); s.add_argument("book"); s.add_argument("pdf"); s.add_argument("--title", required=True)
    s.add_argument("--offset", type=int); s.add_argument("--edition", choices=["original", "official", "trusted"])
    s = sub.add_parser("text"); s.add_argument("book"); s.add_argument("--force", action="store_true")
    s = sub.add_parser("show"); s.add_argument("book"); s.add_argument("pages", nargs="+"); s.add_argument("--physical", action="store_true")
    s = sub.add_parser("grep"); s.add_argument("book"); s.add_argument("pattern"); s.add_argument("--pages", nargs="*")
    s = sub.add_parser("image"); s.add_argument("book"); s.add_argument("page", type=int); s.add_argument("--dpi", type=int, default=150); s.add_argument("--physical", action="store_true")
    s = sub.add_parser("crop"); s.add_argument("png"); s.add_argument("box", nargs=4, type=float); s.add_argument("--rotate", type=int, default=0); s.add_argument("--out")
    a = ap.parse_args()

    if a.cmd == "crop":
        from PIL import Image
        Image.MAX_IMAGE_PIXELS = None
        im = Image.open(a.png)
        w, h = im.size
        x0, y0, x1, y1 = a.box
        c = im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))
        if a.rotate:
            c = c.rotate(a.rotate, expand=True)
        out = Path(a.out or Path(a.png).with_name(Path(a.png).stem + f"-crop-{x0:g}-{y0:g}.png"))
        c.save(out)
        print(out, c.size)
        return

    if a.cmd == "register":
        register(a)
        return
    b = book(a.book)
    off = 0 if getattr(a, "physical", False) else b.get("offset", 0)
    folder = CACHE / a.book
    folder.mkdir(parents=True, exist_ok=True)
    if a.cmd == "text":
        t = folder / "text.txt"
        if t.exists() and not a.force:
            print(f"уже есть: {t}")
            return
        subprocess.run([tool("pdftotext"), "-layout", "-enc", "UTF-8", b["pdf"], str(t)], check=True)
        print(f"{t}: страниц {len(t.read_text(encoding='utf-8').split(chr(12)))}")
    elif a.cmd == "show":
        pages = text_pages(a.book)
        for n in pages_arg(a.pages):
            i = n - off
            print(f"===== с. {n} (физ. {i}) =====")
            print(pages[i - 1] if 0 < i <= len(pages) else "<нет такой страницы>")
    elif a.cmd == "grep":
        pages = text_pages(a.book)
        want = set(pages_arg(a.pages)) if a.pages else None
        pat = re.compile(a.pattern)
        for i, page in enumerate(pages, 1):
            n = i + b.get("offset", 0)
            if want and n not in want:
                continue
            for line in page.split("\n"):
                if pat.search(line):
                    print(f"с. {n}: {line.strip()[:300]}")
    elif a.cmd == "image":
        i = a.page - off
        prefix = folder / f"p{a.page:03d}{'-phys' if a.physical else ''}"
        subprocess.run([tool("pdftoppm"), "-f", str(i), "-l", str(i), "-r", str(a.dpi), "-png", "-singlefile", b["pdf"], str(prefix)], check=True)
        print(f"{prefix}.png")


if __name__ == "__main__":
    main()
