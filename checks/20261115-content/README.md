# Сверка остального контента — задание помощникам

The owner asked for the same detailed check as for scenarios, now for everything else: rules, tables, spells, tomes,
creatures, weapons and equipment, occupations, skills, talents, archetypes, organizations, guides (cities, districts,
places, NPCs of guides), terms. Scenarios are already checked (`checks/20261114-scenarios/`). Read-only: do not edit kb.

## For every part of your book(s) outside the scenarios

1. Find the import coverage files of the book: Grep `checks/` for the book id — files with a table
   «Заголовок книги | Страница | Где в базе» and a «Не взято» list. Find the book's records: Grep `kb/` for the book id
   in `sources` (`python -B tools/status.py` lists books; records of shared kinds live in `kb/<kind>/`).
2. Read the book part by part (`python -B pipeline/source/pages.py show <book_id> <pages> --physical`; OCR books:
   `.cache/ocr/<book_id>/NNN.txt`; scans: `pages.py image`). For every heading, entry, table, sidebar, list:
   - is there a record (or a record field) holding it? (rule → `kb/rules`, roll table → `kb/tables`, spell, tome, creature,
     weapon, occupation, skill, talent, place, NPC…);
   - spot-check numbers: for every entry type check 3–5 entries fully (all numbers of a stat block, spell cost and time,
     tome Mythos/Sanity/weeks, weapon damage/range/cost, occupation skills and credit rating, table rows and dice);
   - for long lists (spells, creatures, occupations, weapons, places of a guide) — check that EVERY entry of the book's
     list/index has a record (script it: names from the text vs `name.en`/`name.ru`/aliases), and every number at
     least for a sample;
   - pictures: portraits, creature art, item pictures belong to records (Р-241, Р-245: small portraits too when the
     record has no picture); atmosphere is listed in `pipeline/art/atmosphere.json`.
3. Verdict per part: **есть** / **частично** (what exactly is lost or wrong) / **нет** (no record) / **не нужно**
   (credits, essays without game data, bibliography, decided by an Р-decision — cite it). Wrong numbers are losses too
   (say printed vs base; book misprints stay as printed and must be in `errata`).
4. Write `checks/20261115-content/<unit>.md` (Russian): per part — one line «цел» or a table of losses
   «что | стр. | вид | где должно быть / что не так | важность (высокая — неверное правило или число, которое ломает игру;
   средняя — нет записи или поля с игровыми данными; низкая — текст, картинка, мелочь)». At the end — totals.

Do not commit; the lead commits. Do the work yourself (no sub-agents). Keep scripts in scratchpad\<unit>\ (the
scratchpad is shared). View at most 2–3 small images per step; if resumed after a network error, continue where you stopped.
