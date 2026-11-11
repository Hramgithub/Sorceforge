# «Ужас в Иннсмуте» (The Innsmouth Terror) — сверка покрытия (Р-219, Р-134)

Книга `innsmouth-terror-en` (Community Content, John Hedge, EN 7e, текстовый слой чистый, числа сверены по изображениям с. 29–31 и листов сыщиков). Печатная страница = физическая − 4 (физ. 1 — обложка, физ. 2–4 — текст обложки, титул и содержание без номеров, физ. 5 = с. 1, с. 39 = физ. 43; физ. 44 — реклама подкаста, физ. 45 — афиши других сценариев, физ. 46 — пустая). Пять листов сыщиков — отдельные PDF `[EN 7e] 3500905-*.pdf` (по 3 с.), в `books.json` не записаны: в `sources` они указаны записью `innsmouth-terror-en` без страниц, с именем файла в `note`.

Записи: `kb/books/innsmouth-terror-en/` — сценарий 1, сцены 25, персонажи 19 (14 НИП и групп + 5 готовых сыщиков), места 17, предметы 12, раздатки 3, существо 1, организация 1. Предложения к чужим записям — `proposals-terror.json` (37). Карт в книге нет.

Префиксы: `sc` — `innsmouth-terror-en/scene/`, `ch` — `…/character/`, `loc` — `…/location/`, `it` — `…/item/`, `h` — `…/handout/`, `S` — сценарий `innsmouth-terror-en/scenario/innsmouth-terror`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, текст обложки («The booklet contains…») | физ. 1–2 | S `summary` |
| Титул (авторы, права) | физ. 3 | не взято (см. ниже) |
| Contents; Content Warnings | физ. 4 | S `summary` (предупреждения, инструменты безопасности) |
| Эпиграф из «The Shadow over Innsmouth» | физ. 5 | не взято (цитата Лавкрафта) |
| Introduction | 1 | S `summary` |
| Preparing for play | 1 | S `advice` |
| Keeper Information (Obed Marsh, три клятвы, гибриды, Джинни, Баззлдон) | 2 | S `keeper_info`; ch `ginny-dubois`, `pa-bazzledon` |
| Table 1: timeline of events | 2 | S `tables` «Таблица 1: хронология событий» |
| The Innsmouth Terror (техноколор, сюжет фильма, ход съёмок, примечание о немом кино) | 3 | S `keeper_info`, `advice`; it `technicolor-camera`, `film-reel` |
| Involving the Investigators (+ примечание об SEU) | 3 | S `hook`; h `1a-letter-internal`, `1b-letter-external`; `coc:organization:society-for-the-exploration-of-the-unexplained` (предложения) |
| Dramatis Personae — Genevieve ‘Ginny’ Dubois | 4 | ch `ginny-dubois` |
| P.A. Bazzledon | 4 | ch `pa-bazzledon` |
| Anna Díaz | 5 | ch `anna-diaz` |
| Christopher McGuire | 5 | ch `christopher-mcguire` |
| Sammy Brewster | 6 | ch `sammy-brewster` |
| The Crew | 6 | ch `film-crew-member`; организация `bazzledon-productions` |
| Minor NPCs: Diane Loring, Henry Armitage, Karen Jeffries, Franc Turner, Jeremiah Brewster, Pete, Zadok Allen | 6 | ch `diane-loring`, `karen-jeffries`, `franc-turner`, `pete`; Армитедж, Джеремайя Брюстер, Зэдок Аллен — записи «Побега из Иннсмута» (`pobeg-iz-innsmuta-ru/character/genri-armitedzh`, `dzheremayya-bryuster`, `zedok-allen`) + предложения |
| Start: Arkham — Orne Library (Miskatonic University) (+ примечания Хранителю) | 7–8 | sc `orne-library`; `coc:location:orne-library`; it `atlantean-jewel` |
| The Arkham Advertiser (+ примечание о Карен) | 8–9 | sc `arkham-advertiser`; loc `arkham-advertiser` |
| The Miskatonic Playhouse (+ примечание об «Испуге на сцене») | 9 | sc `miskatonic-playhouse`; loc `miskatonic-playhouse` |
| Handout 1-a: letter (в главе) | 10 | h `1a-letter-internal` |
| Innsmouth — Arrival (+ примечание о машине) | 11 | sc `arrival` |
| The Gilman House Hotel | 12 | sc `gilman-house`; `coc:location:innsmouth-703-otel-dom-gilmana` |
| The Production Train Car | 12 | sc `production-train-car`; loc `production-train`, `production-train-sleeper-car` |
| Investigation — The Producer’s Office | 13 | sc `producers-office`; it `spare-keys` |
| Around the Train | 14 | sc `around-the-train` |
| Bazzledon’s Office | 14 | sc `bazzledon-office`; loc `production-train-bazzledon-office`; it `bazzledon-papers`, `fat-tony-letter`, `bazzledon-floor-safe`; ch `fat-tony` |
| Ginny’s Trailer (+ Handout 2 в главе, примечание LLFRFL) | 15 | sc `ginny-trailer`; loc `production-train-ginny-trailer`; h `2-sammy-note`; it `playhouse-fire-article` |
| McGuire’s Lab (+ примечание о химикатах) | 16 | sc `mcguire-lab`; loc `production-train-mcguire-lab`; it `mcguire-cave-map`, `technicolor-camera` |
| On Set (+ два примечания) | 17 | sc `on-set`; loc `film-set-field` |
| The Railway Entrance | 18 | sc `railway-entrance`; loc `railway-entrance`; it `broken-binoculars` |
| The Cave System; Moving Through the Caves | 18 | sc `cave-system`; loc `cave-system` |
| Table 2: encounters in the caves | 19 | loc `cave-system` `tables`; S `tables` (ссылка `from`, Р-136) |
| The Brewster Residence (+ примечание о виновнике) | 20 | sc `brewster-residence`; loc `brewster-house`, `brewster-house-ginny-room`, `brewster-house-basement`, `brewster-house-garden-shed` |
| Stumbling onto Set (+ примечание) | 21 | sc `stumbling-onto-set`; loc `cave-film-set` |
| Into Innsmouth | 22 | sc `into-innsmouth` |
| The General Store | 22 | sc `general-store`; ch `pete`; `coc:location:innsmouth-702-bakaleynyy-magazin` (вывод из текста) |
| The Fire Station | 23 | sc `fire-station`; `coc:location:innsmouth-503-pozharnaya-chast`, `…-506-opasnyy-most` (вывод) |
| The Esoteric Order of Dagon | 24 | sc `esoteric-order-of-dagon`; `coc:location:innsmouth-207-ezotericheskiy-orden-dagona`; ch `innsmouth-hybrid-resident` |
| Entering through the Caves | 24 | sc `entering-through-the-caves`; loc `eod-cave-entrance` |
| The Epic Finale (+ примечание) | 25 | sc `epic-finale`; loc `sacrifice-cliff` |
| The Last Train out of Innsmouth | 25 | sc `last-train` |
| Врезка «MVR Class B1 ‘Olmstead’, steam locomotive» | 26 | it `olmstead-locomotive` |
| What if they’re captured? (врезка) | 27 | sc `playing-the-hero` |
| Playing the Hero | 27 | sc `playing-the-hero`; it `tum-eez` |
| Epilogue — Did the investigators escape…?; Was the final scene filmed? | 28 | sc `epilogue`; S `conclusion` |
| Rewards | 28 | S `conclusion` |
| Characters and Monsters — Arkham Residents: Diane Loring, Dr. Henry Armitage, Karen Jeffries, Franc Turner | 29 | ch `diane-loring`, `karen-jeffries`, `franc-turner`; Армитедж — предложение (статблок) |
| Film Crew: Ginny Dubois, Anna Díaz | 29 | ch `ginny-dubois` (с заклинанием Breath of the Deep), `anna-diaz` |
| P.A. Bazzledon, Christopher McGuire, Average Crew Member | 30 | ch `pa-bazzledon` (Mental Suggestion), `christopher-mcguire`, `film-crew-member` |
| Innsmouth Residents: Sammy Brewster, Jeremiah Brewster, Zadok Allen | 30 | ch `sammy-brewster`; Джеремайя и Зэдок — варианты статблоков в предложениях |
| Average Human Resident, Average Hybrid Resident | 31 | ch `innsmouth-human-resident`, `innsmouth-hybrid-resident` |
| Monsters: Shoggoth | 31 | `coc:creature:shoggoth` (числа совпадают, Р-79); правило поглощения — sc `brewster-residence` |
| Star Spawn of Cthulhu (+ примечание автора) | 31 | `coc:creature:star-spawn-of-cthulhu` (числа совпадают, Р-79); хватание — sc `playing-the-hero`; примечание — it `tum-eez` |
| Deep One | 31 | `innsmouth-terror-en/creature/deep-one` (свой профиль, `instance_of`) |
| Pre-generated Investigators: Hugo ‘Shrimpy’ Hargreaves | 32 | ch `hugo-hargreaves` |
| Patty Gillian | 33 | ch `patty-gillian` |
| Ian Torres | 34 | ch `ian-torres` |
| Tiffany Quispe | 35 | ch `tiffany-quispe` |
| Margaret ‘Maggie’ Myers | 36 | ch `margaret-myers` |
| Handouts: Handout 1-a: letter (internal) | 37 | h `1a-letter-internal` |
| Handout 1-b: letter (external) | 38 | h `1b-letter-external` |
| Handout 2: note; Handout 2: note (plain text) | 39 | h `2-sammy-note` |
| Лист сыщика `3500905-Hugo__Shrimpy__Hargreaves.pdf` (3 с.) | — | ch `hugo-hargreaves`, вариант «Лист сыщика» |
| Лист сыщика `3500905-Patty_Gillian.pdf` | — | ch `patty-gillian`, вариант |
| Лист сыщика `3500905-Ian_Torres.pdf` | — | ch `ian-torres`, вариант |
| Лист сыщика `3500905-Tiffany_Zachmann-1.pdf` («Tiffany Zachmann») | — | ch `tiffany-quispe`, вариант; имя — в `aliases` |
| Лист сыщика `3500905-Margaret_Maggie_Myers.pdf` | — | ch `margaret-myers`, вариант |

## Не взято

- Титул и выходные данные (физ. 3), правовые оговорки, эпиграф Лавкрафта (физ. 5), реклама подкаста Miskatonic Playhouse (физ. 44), афиши других сценариев (физ. 45), пустая страница (физ. 46) — не материал игры.
- Иллюстрации и портреты книги и листов (Диана Лоринг, Армитедж, Карен, Франк, Пит, Зэдок, Джеремайя, готовые сыщики, бланк письма) — картинки в `app/art/` не входят в файлы этой части; можно добавить `pipeline/art/add_images.py` при сведении.
- Отдельные записи шоггота и звёздного отродья — числа совпадают со справочными (Р-79); особенности сценария записаны в сценах.
- Безымянные эпизодические фигуры без статблока — водитель автобуса, портье «Дома Гилмана», старуха-торговка виски, мать Джинни, головорезы из Нью-Йорка, щупальцевые твари в пещерах (1d3 щупальца, Драка 50%, 1d3) — текстом в сценах, отдельных записей нет.
- Мелкие вещи без механики — кусок золотого сплава (строка таблицы 2), тиара Джеремайи, костюмы лягушачьих созданий, дерринджер из сейфа — текстом в записях таблицы, сцен и сейфа.
- Третья страница каждого листа сыщика (краткие правила) и пустые поля листа («Fellow Investigators», «Gear & Possessions») — общие правила/пустые поля.
- «Drive Train» (Вождение поезда) — навыка нет в справочнике; записан текстом.
- Заклинание «Summon Star Spawn» (у Джеремайи): в книге только название, механики нет — запись заклинания не заведена (черновик невозможен; вопрос в отчёте).

## Технический долг

- `pipeline/source/books.json`: у `innsmouth-terror-en` нет `offset`; верное — `"offset": -4` (печатная = физическая − 4; в pages.py физическая = печатная − `offset`). Листы сыщиков стоит записать отдельными книгами (`innsmouth-terror-pregens-en` или по листу).
- Р-154: Джеремайя Брюстер, Зэдок Аллен и Генри Армитедж теперь встречаются в нескольких книгах — кандидаты в общие записи `coc:character:*`; пока дополнены предложениями.
