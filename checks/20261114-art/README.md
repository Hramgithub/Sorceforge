# Картинки для записей (Р-241) — задание помощникам

Owner's decision Р-241 (`docs/project-goal.md` §6): pictures of the source books are added to **existing records** —
portraits of characters, art of creatures, handouts, items, tomes. Atmosphere illustrations (scenes, places, decoration)
are **not** imported, only listed. Pictures the book itself says are AI-made are skipped (Р-240). Read
`.claude/skills/kb-art/SKILL.md` (the workflow and the display rules) and the `images` part of `docs/conventions.md`.

## Input for your books

- `checks/20261114-completeness/findings.json`, entries of your books with
  - `"check": "art.record_without"` — a page with picture(s) no record carries, and records of that page without
    `images` (`ids`); these are the main candidates;
  - `"check": "art.uncovered"` — a page with picture(s) no record carries and no such record on it; usually
    atmosphere, but a portrait or a handout of a record cited on another page also lands here (e.g. a character's
    portrait printed one page before its text, a handout in the «Maps and Handouts» appendix).
- Book PDF: `pipeline/source/books.json` → `pdf`; pages are physical (`page` in findings).
- Poppler: `C:\Tools\Poppler\poppler-26.02.0\Library\bin` (`pdfimages`, `pdftoppm`, `pdftotext`).

## Work

1. For every candidate page extract the pictures: `pdfimages -f N -l N -png "<pdf>" .cache/art/<book_id>/pNNN`
   (or render the page `pdftoppm -r 150 -f N -l N -png` and crop, when a picture is cut into pieces or has text
   over it). Drop decorations, frames, backgrounds, small bits (< 250 px).
2. Look at each picture (Read the PNG; a contact sheet of several is fine) together with the page text
   (`python -B pipeline/source/pages.py show <book_id> <page> --physical`): whom/what does it show? Use captions,
   names on the page, the handout number, the record list of the page (`ids`). Match only when sure; a portrait
   without a caption is matched when the page is that character's entry and only one character fits.
3. Decide:
   - **record art** → a mapping item `{target, src, kind, caption, source, name}`:
     `kind` — `portrait` (person), `art` (creature, deity), `handout` (player handout as printed),
     `illustration` (item, tome, other picture of a record), `plan` (plan of a record place only when that place
     has no `map` record; maps of scenarios are `map` records — skip them); `caption` — short, neutral, no spoilers
     (empty for a plain portrait); `source` — «<book title from books.json>, с. <printed> (физ. <physical>)»;
     `name` — `<book short prefix>-<record slug>` (no overwrite of existing art files).
     A shared record (`coc:creature:*`, `coc:character:*`) that already has a picture from another book gets this
     one too only if it clearly shows the same being; one picture per book per record.
   - **atmosphere** (scene, landscape, place, decoration, a picture of something with no record) → an item in
     your atmosphere list `{book_id, physical_page, what}` (what — 3–8 Russian words).
   - **handout without a record** → do not create records; list it in your report as a candidate.
4. `python -B pipeline/art/add_images.py checks/20261114-art/<unit>.json --dry-run`, then without `--dry-run`
   (copies go to `app/art/`, proposals to `checks/20261114-art/<unit>-proposals.json`). **Do not apply the proposals**
   — the lead applies them. Do not edit kb records.
5. Write `checks/20261114-art/<unit>-atmosphere.json` (a JSON list) and `checks/20261114-art/<unit>.md` (Russian):
   per book — pages looked at, pictures added (record → kind), atmosphere count, doubts, handout candidates.

## Scans (books without a text layer, added 2026-11-14 evening)

The completeness check did not look for pictures in long scans (every page is one image), so these books have no
candidate list: go through all pages yourself. Render thumbnails (`pdftoppm -r 40 -png`, contact sheets of 6–9 pages,
≤ 800 px wide) to find pages with pictures, then render those pages at 150–200 dpi and crop each picture by a frame
(fractions of the page; save frames to `checks/20261114-art/<unit>-boxes.json`). Match with records by the page's text
(OCR `.cache/ocr/<book_id>/NNN.txt` when present, otherwise read the page image) and by the records citing that page.
Small portraits are taken when the character has no larger picture (Р-245). List atmosphere pages as usual.

Never commit. Do not touch other units' books. Final report: counts by book (added by kind / atmosphere / doubts).
