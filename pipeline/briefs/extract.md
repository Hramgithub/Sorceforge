# Brief: {{book_title}} — unit «{{unit}}»

Repository: `C:\_Hobby\_work\Sorceforge` — Call of Cthulhu 7e knowledge base, JSON records in git.
Goal of this import: {{goal}}
Decision: {{decision}}. Your unit: **{{unit}}** — {{target}}. Pages: **{{pages}}**.

## Read before writing

- The rules of writing records — appended at the end of this brief (`docs/conventions.md`, verbatim). They win over
  anything else, including this brief.
- Models to copy (done records of the same kind):
{{models}}
- Schemas: `schemas/<kind>.schema.json`, `schemas/common.schema.json`, guide `schemas/README.md`.

## Source

Book `{{book_id}}`. Read it with the page tool (printed page numbers):

```
python pipeline/source/pages.py show {{book_id}} {{pages}}
python pipeline/source/pages.py grep {{book_id}} "<regex>" --pages {{pages}}
python pipeline/source/pages.py image {{book_id}} <page> --dpi 150      # tables, maps, sidebars, scans
```

Two-column text and sidebars can come out of order: when numbers or a table matter, check the page image.
Python: `python -I`; PowerShell mangles Cyrillic and `$` in `python -c` — write `.py` files in your scratch folder.

## What you own

You may create and edit only:
{{owns}}

Everything else is read-only for you: shared records (cities, districts, places of other units, characters from
other books), `tools/`, `app/`, `schemas/`, `docs/`. A change they need goes to your proposals file
`{{check_dir}}/proposals-{{unit}}.json` (format: `pipeline/integrate/README.md`).

{{extra}}

## Done means

1. Every heading of pages {{pages}} has a place in the base: `{{check_dir}}/{{unit}}.md` — a table
   «Заголовок книги | Страница | Где в базе», plus «Не взято» with the reason for anything not moved
   (nothing is dropped silently).
2. `python tools/check.py <your files>` — 0 errors. Ids you reference exist (the check looks across the whole base).
3. No git commands, no viewer rebuild — the lead integrates, checks and commits.

## Units (who owns what)

{{units_table}}

## Report (your final message)

Short, in English: files created and changed, counts by kind, proposals file and how many proposals,
misprints and doubts found, anything you could not place.

---

{{conventions}}
