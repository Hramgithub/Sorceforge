# Аркхэм (arkham-en): часть appendices — приложения A–C и газета «Arkham Advertiser»

Книга `arkham-en`, физ. с. 248–258 (печатные 247–257); газета-вкладка — `arkham-advertiser-en`, с. 1–4 (текстового слоя нет,
набрано по изображениям 200 dpi). Р-234. Русский текст — наш перевод с английского (`translated`, Р-21); машинный перевод
как источник не использовался (Р-147). Сборка: `.cache/appendices/build.py` (данные — `data_tables.py`, `data_paper.py`),
картинки — `.cache/appendices/img.py`, черновики типовых персонажей — `.cache/appendices/npc.py`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 5: Appendices (титульная страница) | 247 | — (только заголовок, текста нет) |
| Appendix A: Arkham Names & Chronology — вступление, «Choose or roll 1D10» | 248 | `coc:table:arkham-names` (1d10: 1–5 → таблица 1, 6–10 → таблица 2) |
| Table 1 (choose or roll 1D100) | 248 | `coc:table:arkham-names-1` (100 фамилий, Abbott — Jermyn) |
| Table 2 (choose or roll 1D100) | 248 | `coc:table:arkham-names-2` (100 фамилий, Johnston — Wyman) |
| Lovecraftian Chronology (1643–1935) | 249–250 | `coc:table:arkham-chronology` (48 строк, дата — в `roll`) |
| Appendix B: Game Aids — вступление | 251 | пересказано в описаниях записей ниже |
| Weather Generator | 251 | повтор гл. 1 (с. 17, «Weather Generator», врезка в «About Arkham / Climate») — запись части overview (город); не дублируется |
| Arkham Hotels: Short Stay Rooms | 251 | повтор гл. 3 (с. 38, «Short Stay Rooms») — часть overview; гостиницы — места 130, 136, 634, 710, 724, 728 |
| Table: Arkham Reputations; Applying the Modifiers; Status Check (Luck Roll) | 251 | повтор гл. 3 (с. 30–32, репутация) — правило части overview; не дублируется |
| Coven Rites | 251 | повтор гл. 3 (с. 51, Аркхэмский ковен) — часть overview; не дублируется |
| Miskatonic Area Travel Distances (страница-таблица) | 252 | `arkham-en/handout/appendix-travel-distances` (23 места, 253 пары, картинка `app/art/handouts/arkham-travel-distances.webp`) |
| Generic NPCs: Bartender, Businessperson, Criminal Low-End, Criminal Mobster, Doctor | 253 | черновики `.cache/appendices/npc/generic-*.json` (см. «Передать ведущему») |
| Generic NPCs: Farmer, Flapper, Handyman/Superintendent, Hotel Staff, Librarian, Mechanic | 254 | то же |
| Generic NPCs: Mortuary Attendant, Police Patrol Officer, Police Sergeant, Priest, Professor | 255 | то же |
| Generic NPCs: Ruffian, Shop Assistant, Student, Taxicab Driver, Teacher | 256 | то же |
| Appendix C: Bibliography & Resources (библиография, Websites) | 257 | `coc:rule:arkham-bibliography` (таблицы «Библиография», «Сайты») |
| Other Resources; сборники сценариев Chaosium; Chaosium Call of Cthulhu Licensees | 257 | `coc:rule:arkham-bibliography` (три таблицы) |
| Врезка «Using the Arkham Advertiser» (гл. 3) | 40 | `arkham-en/handout/advertiser-1922-page-1` (описание, источник) |
| «Arkham Advertiser», 13 сентября 1922 года, с. 1 | вкладка 1 | `arkham-en/handout/advertiser-1922-page-1` (+ `app/art/handouts/arkham-advertiser-1922-1.webp`) |
| с. 2: выходные данные; Arkham Authors…; Lecture Canceled; Dr. Peaslee Returns…; Angry Exchanges…; Pharaoh’s Scholar Program; D. A. to Depose Colleague…; реклама | вкладка 2 | `arkham-en/handout/advertiser-1922-page-2` (+ `…-2.webp`) |
| с. 3: M.U. Co-Eds…; Amusements; Amateur Vaudeville; KWIZ; Book Ends; реклама | вкладка 3 | `arkham-en/handout/advertiser-1922-page-3` (+ `…-3.webp`) |
| с. 4: Ring Sent…; Injunction Stops Lithium Mine; Births; Deaths; Classified; реклама; комикс | вкладка 4 | `arkham-en/handout/advertiser-1922-page-4` (+ `…-4.webp`) |

## Передать ведущему: типовые персонажи (Generic NPCs)

21 запись персонажа готова, но лежит вне `kb/`: часть не владеет `kb/books/arkham-en/characters/`. Файлы —
`.cache/appendices/npc/generic-<slug>.json` (id `arkham-en/character/generic-<slug>`); их нужно перенести в
`kb/books/arkham-en/characters/` как есть. Проверены `tools/check.py` на копии базы — ошибок 0, предупреждений 0.
Каждый — групповой типаж (`stock_type`, 5 придуманных имён по Р-151, флаг `editorial_text`), статблок как напечатан,
навыки и оружие связаны со справочниками. Опечатки — в `errata` (см. ниже).

## Не взято

- Тексты реальных новостей 1922 года в газете (телеграфные сообщения: Смирна, выборы в Массачусетсе кроме аркхэмского абзаца,
  «бунты из-за соломенных шляп», присяга Сэмюэла, миссис Хардинг, Киплинг, Иззи Эйнштейн, брачная клятва епископалов,
  Ирландия, черви и ток, опыт Майкельсона, радио, спорт и таблица лиг, шахтёры в Калифорнии, Амундсен, «недостающее звено»,
  «Новости коротко») — в записях только заголовки с «[…]»; к Аркхэму и игре не относятся, сам текст — на картинках страниц.
- Фотографии и рисунки газеты (Лодж и Кокс, карта Смирны, миссис Хардинг, Пизли, Фрэнсис Тейлор, стрелковый клуб, рекламные
  картинки) — только в картинках страниц; иллюстрации приложений (значок полиции Аркхэма, с. 255; фоновые рисунки) — не взяты.
- Повторы игровых пособий Приложения B (погода, гостиницы, репутация, обряды ковена) — не дублируются: это перепечатка
  глав 1 и 3 (часть overview). Отличий в тексте нет (сверено с с. 17, 30–32, 38–39, 51).
- Biographies (с. 258, физ. 259: Майк Мейсон, Кит Хербер) — за пределами страниц части и не игровой материал.

## Кандидаты на слияние (Р-154)

- Газета «Arkham Advertiser» уже общая (`coc:location:arkham-advertiser`; место 131 ведёт часть northside). Другие номера газеты в
  других книгах — разные раздаточные материалы, не дубли: `pobeg-iz-innsmuta-ru/handout/arkham-advertiser-spetsvypusk`,
  `mothers-love-ru/handout/arkham-advertiser-1928`, `shadows-of-leningrad-en/handout/handout-a-arkham-advertiser`.
- `keeper-rulebook-ru/character/crimson-keziah-mason` ↔ `arkham-en/character/frenchhill-keziah-mason` — одна и та же Кеция Мейсон
  (кандидат в общую `coc:character:keziah-mason`; хронология ссылается на запись путеводителя).
- Типовой «Police, Patrol Officer» похож на `keepers-companion-en/character/hammer-arkham-police` (полиция Аркхэма в «Будь у меня
  молоток») — числа другие, это не дубль, только сходство.

## Ссылки, оставленные текстом (записей нет)

- Места таблицы расстояний: Bass Ridge, Bolton, Dean’s Corners, Essex, Foxfield, Gloucester, Manchester, Marblehead,
  Martin’s Beach, Mayottville, Newburyport, Ross’s Corners (есть только термин и место «Мартинс-Бич» другой книги).
- Хронология: Уилбур, Лавиния и Старый Уэйтли, Абия Хоудли, Аллан Хэлси, Натаниэль Уингейт Пизли, Уолтер Гилмен,
  Альберт Уилмарт (есть его дом, 816), Генри Эйкли, Рэндольф Картер, Сентинел-Хилл, ферма Гарднера.
- Газета: Локсли-холл (кампус), Пизли и Джастин Бич, Натаниэль Уорд, доктор Бетнелл, Фердинанд К. Эшли, Дэвид Эдмунд,
  Герберт Уэст и Гордон Стюарт, Адам Гланси, «Нук-Эндс», похоронное бюро «Уайтчепел» (Whitechapel Mortuary), Минерва
  Коулман, Уильям Пинтер, мисс А. Уэйт. Если часть campus заведёт Локсли-холл, Пизли и Уорда — ссылки стоит добавить.

## Опечатки и сомнения

- Coven Rites: «April 31* (Beltane eve)» (с. 251 и с. 51) — в апреле 30 дней; канун Белтейна — 30 апреля. Касается записи
  ковена части overview.
- Врезка «Using the Arkham Advertiser» (с. 40): номер газеты назван «Thursday, September 13, 1922», а в шапке газеты — среда
  (верно для 1922 года); в `errata` раздатки с. 1.
- Фамилии: «tHoughton» (табл. 1, № 89) исправлено молча (Р-39); «Olne» (табл. 2, № 25) и «Russel» (№ 49) — как напечатано.
- Расстояния: «as the crow files» — опечатка (flies), оставлена в английском тексте.
- Типовые персонажи: у Уклонения бармена и делового человека в столбце урона «+1D4+2»; у мелкого преступника «knife club 1D4+2»;
  фермер — Драка и Топор «50% (25/5)» (пятая должна быть 10); служащий гостиницы — Драка «15% (12/5)» (доли подходят к 25%);
  механик — Драка «65% (30/12)» (доли подходят к 60%); профессор — ПМ 12 при МОЩ 55 (по правилам 11, оставлено как напечатано).
- Газета, с. 3: директор труппы «Andrey Lamont», в путеводителе — Andrew Lamont.
- «Аркхэм Адвертайзер» в общей записи (из «Innsmouth Terror») — владелица Карен Джеффрис; в номере 1922 года издатель и главный
  редактор — Харви Гедни (как и в путеводителе, с. 90). Это разные издания и, вероятно, разные годы; решать при сведении места 131.

## Предложения

`checks/20261114-arkham/proposals-appendices.json` — пусто: обратные ссылки (город, газета, места) показывает просмотрщик;
записей части overview для погоды, гостиниц, репутации и ковена ещё нет — к ним стоит добавить источник `arkham-en`,
физ. с. 252 («Appendix B: Game Aids», повтор) при сведении.
