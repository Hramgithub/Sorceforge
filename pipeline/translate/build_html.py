"""Assemble the translated version of an English book into one HTML file (Р-251).

Input folder (the translation of one book), one Markdown file per physical page or per chapter, in book order:
  NNN.md          text of page NNN (or of a chapter starting there) in Markdown; tables in Markdown table syntax;
                  a picture is a line  ![caption](img/<file>)  — the file lies in the folder's img/;
                  a handout is a block starting with  > **Раздатка …**  (shown framed);
                  a stat block — a fenced block ```stat … ``` (shown monospaced in a frame).
  meta.json       {"title_ru", "title_en", "book_id", "authors", "publisher", "year", "note", "printed_offset"}
                  NNN is the physical page of the PDF; "printed_offset" (default 0) — printed page = physical − it,
                  for the page footer «с. N оригинала»; "unnumbered" (list of physical pages) — pages without a
                  printed number, their footer names the PDF page.
Pictures are embedded (base64, JPEG ≤ 1400 px), so the result is one file.

Usage: python pipeline/translate/build_html.py <folder> <output.html>
"""
from __future__ import annotations

import base64
import datetime
import html
import io
import json
import re
import sys
from pathlib import Path

import markdown
from PIL import Image

MAX_SIDE = 1400

CSS = """
:root { --bg:#fbf9f4; --fg:#1f1d1a; --muted:#6b665d; --line:#ddd6c8; --card:#fff; --accent:#7a4b12; }
@media (prefers-color-scheme: dark) { :root { --bg:#191816; --fg:#ece8df; --muted:#a59f93; --line:#3a362f; --card:#23211d; --accent:#e0b060; } }
body { margin:0; background:var(--bg); color:var(--fg); font:17px/1.6 Georgia, 'PT Serif', serif; }
main { max-width: 880px; margin: 0 auto; padding: 32px 18px 80px; }
header.book { border-bottom: 2px solid var(--line); margin-bottom: 28px; }
header.book h1 { font-size: 34px; margin: 0 0 4px; }
header.book .sub { color: var(--muted); font-style: italic; }
.note { font-size: 14px; color: var(--muted); border: 1px solid var(--line); border-radius: 8px; padding: 10px 14px; margin: 14px 0; }
nav.toc { font-size: 15px; columns: 2; margin: 16px 0 28px; }
nav.toc a { color: var(--accent); text-decoration: none; display: block; }
h1, h2, h3, h4 { font-family: system-ui, sans-serif; line-height: 1.25; }
h1 { font-size: 28px; margin-top: 48px; } h2 { font-size: 22px; margin-top: 36px; } h3 { font-size: 18px; }
img { max-width: 100%; height: auto; display: block; margin: 14px auto 4px; border-radius: 4px; }
figure { margin: 18px 0; } figcaption { text-align: center; color: var(--muted); font-size: 14px; }
table { border-collapse: collapse; width: 100%; margin: 14px 0; font: 15px/1.4 system-ui, sans-serif; }
th, td { border: 1px solid var(--line); padding: 5px 8px; vertical-align: top; text-align: left; }
th { background: var(--card); }
blockquote { background: var(--card); border: 1px solid var(--line); border-left: 4px solid var(--accent); margin: 16px 0; padding: 10px 16px; }
pre.stat { background: var(--card); border: 1px solid var(--line); padding: 10px 14px; white-space: pre-wrap; font: 14px/1.45 ui-monospace, Consolas, monospace; }
.page { color: var(--muted); font: 12px system-ui, sans-serif; text-align: right; margin-top: 24px; border-top: 1px dashed var(--line); }
"""


def embed(img: Path) -> str:
    im = Image.open(img)
    im.thumbnail((MAX_SIDE, MAX_SIDE))
    if im.mode not in ("RGB", "L"):
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.convert("RGBA").split()[-1])
        im = bg
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def page_html(md_text: str, folder: Path) -> str:
    md_text = re.sub(r"```stat\n(.*?)```", lambda m: '<pre class="stat">' + html.escape(m.group(1)) + "</pre>", md_text, flags=re.S)
    out = markdown.markdown(md_text, extensions=["tables", "sane_lists"])

    def img(m):
        cap, src = html.unescape(m.group(1)), m.group(2)
        p = folder / src
        if not p.exists():
            return f'<p class="note">[нет картинки {html.escape(src)}]</p>'
        figcap = f"<figcaption>{html.escape(cap)}</figcaption>" if cap else ""
        return f'<figure><img src="{embed(p)}" alt="{html.escape(cap)}">{figcap}</figure>'
    out = re.sub(r'<p>\s*<img alt="([^"]*)" src="([^"]+)"\s*/?>\s*</p>', img, out)
    return out


def main() -> int:
    folder, target = Path(sys.argv[1]), Path(sys.argv[2])
    meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
    pages = sorted(p for p in folder.glob("*.md") if re.match(r"^\d+", p.stem))
    body, toc = [], []
    for p in pages:
        text = p.read_text(encoding="utf-8")
        h = page_html(text, folder)
        for lvl, title in re.findall(r"<h([12])>(.*?)</h\1>", h):
            anchor = f"s{len(toc) + 1}"
            h = h.replace(f"<h{lvl}>{title}</h{lvl}>", f'<h{lvl} id="{anchor}">{title}</h{lvl}>', 1)
            toc.append((lvl, re.sub("<[^>]+>", "", title), anchor))
        phys = int(re.match(r"^(\d+)", p.stem).group(1))
        printed = phys - int(meta.get("printed_offset", 0))
        label = f"с. {printed} оригинала" if printed >= 1 and phys not in meta.get("unnumbered", []) else f"стр. {phys} PDF оригинала (без номера)"
        body.append(h + f'<div class="page">{label}</div>')
    toc_html = "".join(f'<a href="#{a}">{"&nbsp;&nbsp;" if l == "2" else ""}{html.escape(t)}</a>' for l, t, a in toc)
    note = meta.get("note") or ("Перевод выполнен для личного некоммерческого использования. Это не официальное издание; "
                                "оригинал принадлежит правообладателю.")
    doc = f"""<!doctype html>
<html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(meta['title_ru'])}</title><style>{CSS}</style></head>
<body><main>
<header class="book"><h1>{html.escape(meta['title_ru'])}</h1>
<div class="sub">{html.escape(meta.get('title_en', ''))} — {html.escape(meta.get('authors', ''))}, {html.escape(meta.get('publisher', ''))} {html.escape(str(meta.get('year', '')))}</div>
<p class="note">{html.escape(note)} Перевод: Sourcefold, {datetime.date.today().isoformat()}. Термины и имена — как в базе знаний Sourcefold.</p>
</header>
<nav class="toc">{toc_html}</nav>
{''.join(body)}
</main></body></html>
"""
    target.write_text(doc, encoding="utf-8")
    print(f"{target} — {len(pages)} стр., {len(toc)} разделов, {target.stat().st_size // 1024} КБ")
    return 0


if __name__ == "__main__":
    sys.exit(main())
