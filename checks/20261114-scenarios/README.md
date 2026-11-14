# Целостность сценариев — задание помощникам

The owner asked: take every scenario as a work and check that nothing was lost — plot, scenes, characters, clues,
handouts, pictures. The mechanical check is done (`python tools/scenario_check.py` → `report.md`, `findings.json` in this
folder: links inside the base are consistent). Your job is the reading check: the book against the base.

## For every scenario of your books

1. Find the scenario record (`kb/books/<book_id>/scenarios/*.json`; campaign chapters too) and its row and findings in
   `report.md`. Find the import coverage file of that scenario, if any: Grep `checks/` for the book id and the scenario
   name — files with a table «Заголовок книги | Страница | Где в базе» (they list every heading → record, «Не взято»).
2. Read the scenario in the book page by page (`python -B pipeline/source/pages.py show <book_id> <pages> --physical`;
   OCR books: `.cache/ocr/<book_id>/NNN.txt`; scans: `pages.py image`). Note every:
   - part of the plot (introduction, keeper information, hooks, every section/scene, conclusion, rewards);
   - named character (NPC, pregen, group profile), creature, organization;
   - clue: handout, item, document, tome, a fact the investigators must learn (is it in a scene's text, `leads_to`,
     handout or item?);
   - place, map, table;
   - picture: portrait, creature art, handout picture (atmosphere pictures are not imported — Р-241; maps are `map` records).
3. Check each against the base (Grep by name, `name.en`, aliases; the scenario's steps and scenes). Decide:
   - **есть** — the record holds it (spot-check a number or a key fact on 2–3 records);
   - **частично** — the record exists but loses something that matters for play (a clue, a stat block, a sanity
     cost, a scene branch, a handout text) — say what exactly;
   - **нет** — nothing in the base;
   - **не нужно** — credits, design notes, atmosphere picture, decided by an Р-decision (cite it).
4. Do not edit kb. Write `checks/20261114-scenarios/<unit>.md` (Russian): per scenario — a short verdict line
   («цел» / «потери: N»), then a table of losses «что | стр. | вид | где должно быть | важность (высокая — без этого сценарий
   не провести, средняя, низкая)». Scenarios whose coverage file already lists every heading and your spot-checks agree —
   one line «цел, сверка по <file>».

Final report to the lead (Russian): per book — scenarios checked, how many whole, the list of high-importance losses.
View at most 2–3 small images per step; the network is unstable — if resumed after an error, continue where you stopped.
