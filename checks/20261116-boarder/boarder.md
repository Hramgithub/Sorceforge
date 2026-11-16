# Dead Boarder (`dead-boarder-en`) — перенос в базу (Р-251)

Chaosium, 2016; концепция — Todd Gardiner, текст — Todd Gardiner with Mike Mason, редактура — Mike Mason, карта — Todd Gardiner.
Расширенная демонстрационная игра для «Зова Ктулху» 7-й редакции: воскресенье, 21 июня 1931 года (летнее солнцестояние),
Великая депрессия, пансион Ма Шэнкс на краю Федерал-Хилла, **Провиденс (Род-Айленд)** — город в книге назван прямо
(в брифе — «неназванный город»); места книги `part_of` общей записи `coc:location:providence`.
Русского перевода сценария в базе нет (проверено по ключевым именам: Гардинер, Мадейра, Шэнкс, Скиргайла, «Мёртвый жилец/постоялец»;
в каталоге библиотеки «The Dead Boarder» значится также в сборнике «Gateways to Terror», которого в базе нет).

Страницы: PDF 32 страницы; **печатная страница = физической, смещение 0** («4» на физ. 4, «21» на листе сыщика физ. 21).
Без номеров: обложка (физ. 1), выходные данные (физ. 2), оглавление (физ. 3) — в `sources` `printed_page: null`.

## Записи (51)

- сценарий 1: `scenarios/dead-boarder` («Мёртвый жилец»; таблицы «Расписание игры», «Возможные приступы безумия»)
- сцены 10: `getting-ready-to-play`, `opening-scene`, `examining-the-body`, `tarp-candles-paper`, `looking-around-the-room`,
  `reading-the-books`, `speaking-to-mrs-madeira`, `the-monster-rises`, `combat`, `more-police-arrive`
- персонажи 17: прегены `landlord` (Фрэнки Соуза), `bookstore-owner` (Лесли Холлис), `business-associate` (Сидни Доннелли),
  `nosy-neighbor` (Мэрион Фогель), `tough-guy` (Ники Скиргайла), `beat-cop` (Терри Конти) — имена придуманы (Р-150),
  подходят и мужчине, и женщине, `player_chooses: name, sex`; `james-gardiner`, `loretta-shanks`, `tommy`, `mrs-madeira`,
  `milligan`, `malone` (статблоки), `anikke-skirgaila`, `dovana-skirgaila`, `petras-skirgaila`, `konstantinas-skirgaila`,
  `double-barrel-angelo`
- существо 1: `creatures/gardiner-thing` (Тварь-Гардинер; уникальное, общей записи нет)
- организации 2: `the-mob` (Мафия Провиденса), `providence-police` (Полиция Провиденса)
- книги 2: `tomes/book-of-dreams` (книга Мифов, заклинания → `coc:spell:flesh-ward`, `coc:spell:mind-transfer`),
  `tomes/gardiners-dream-journal` (оккультная)
- предметы 13: `obsidian-knives`, `bloodstained-paper`, `oriental-rug`, `ornate-bookcase`, `squid-bookend`, `wardrobe-revolver`,
  `wooden-box`, `gardiners-pockets`, `laudanum-and-cocaine`, `ledgers`, `correspondence`, `dreamers-dictionary`, `loaned-books`
- раздатка 2: `handout-1-greek-chant` (греческий как напечатан), `handout-2-chant-translation` (английский как напечатан + наш перевод)
- места 2: `ma-shanks-boarding-house` (Провиденс), `gardiners-room` (в пансионе)
- карта 1: `maps/gardiners-room` (`app/maps/boarder-gardiners-room.png`, 984 × 1353; 8 меток на напечатанных подписях + 3 без подписи, `printed: false`)

Картинки (8, применены через `art-proposals.json`): раздатки 1 и 2 (с. 19), листы шести сыщиков как `card` (с. 21–31; на листах силуэт вместо портрета) —
`app/art/handouts/boarder-handout-*.webp`, `app/art/characters/boarder-*.webp`.
Атмосфера: иллюстраций в книге нет (обложка — только надпись; кроме раздаток, карты и листов картинок в PDF нет); в `atmosphere.json` — одна просмотренная запись: копии раздаток в тексте (с. 12), не берутся (единственная находка `completeness`, `art.uncovered`).

Предложения к общим записям — `proposals.json` (4 правки, 1 запись `coc:location:providence`: абзац о «Мёртвом жильце», источник, 2 ссылки; пробный прогон проходит).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Dead Boarder — An Extended Demo for Call of Cthulhu» | физ. 1 | сценарий (`aliases`, `sources`) |
| Credits | физ. 2 | сценарий (`summary`, `sources`) |
| Table of Contents | физ. 3 | сценарий (`sources`) |
| a Call of Cthulhu Extended Demo Scenario (цели демонстрации) | 4 | сценарий (`advice`) |
| Dead Boarder («A grisly discovery…») | 5 | сценарий (`summary`) |
| Introduction | 5 | сценарий (`summary`, `keeper_info`) |
| Keeper Considerations | 5 | сценарий (`advice`) |
| Rules Notes | 5 | сценарий (`advice`); сцена `getting-ready-to-play` |
| Fitting a Two Hour Time Limit | 5–6 | таблица сценария «Расписание игры»; `advice` |
| Scenario Background | 6 | сценарий (`keeper_info`); Джеймс Гардинер; Тварь-Гардинер; «Книга снов» |
| Ma Shanks’ Boarding House | 6 | место `ma-shanks-boarding-house`; предложение к Провиденсу |
| Player Characters | 7 | сценарий (`advice`, `keeper_info`); сцена `getting-ready-to-play` |
| The Landlord (or Landlady) | 7 | преген `landlord` |
| The Bookshop Owner (+ список одолженных книг) | 7 | преген `bookstore-owner`; предметы `dreamers-dictionary`, `loaned-books` |
| Nosy Neighbor | 7 | преген `nosy-neighbor` |
| Business Associate | 7 | преген `business-associate`; предметы `obsidian-knives`, `ledgers`; `the-mob` |
| The Tough Guy/Dame | 7 | преген `tough-guy` |
| The Beat Cop | 7–8 | преген `beat-cop` |
| Other Residents | 8 | Ма Шэнкс, Скиргайла (4), Томми, миссис Мадейра, Гардинер; сценарий (`keeper_info`) |
| The Extra Police | 8 | сценарий (`keeper_info`); Миллиган, Мэлоун; `providence-police`; сцена `more-police-arrive` |
| Getting Ready to Play | 8 | сцена `getting-ready-to-play` |
| Opening Scene | 9 | сцена `opening-scene` |
| Calling for more police | 9 | сцена `opening-scene`; Томми |
| Taking a Closer Look | 9 | сцена `examining-the-body`; место `gardiners-room` |
| Examining the Body (No roll / First Aid Regular, Hard / Spot Hidden / карманы) | 9–10 | сцена `examining-the-body`; предметы `obsidian-knives`, `gardiners-pockets` |
| The Tarp, Candles, and Piece of Paper | 10 | сцена `tarp-candles-paper`; предметы `bloodstained-paper`, `oriental-rug` |
| Looking Around the Room: Wardrobe | 10–11 | сцена `looking-around-the-room`; `wooden-box`, `wardrobe-revolver` |
| Bed; Nightstand | 11 | сцена `looking-around-the-room`; `dreamers-dictionary`, `laudanum-and-cocaine`, дневник |
| Ornate bookcase (книгодержатель, тайник) | 11 | `ornate-bookcase`, `squid-bookend`, `loaned-books`, `ledgers`, `obsidian-knives`, «Книга снов»; сцена `looking-around-the-room` |
| Upholstered chair; Window | 11 | место `gardiners-room`; сцена `looking-around-the-room`; метки карты без подписи |
| Handout 1; Handout 2 | 12 | раздатки 1 и 2 (`sources`; картинки — из приложения, с. 19) |
| Table and two wooden chairs; Cabinets and counter; Long table by the door | 13 | место `gardiners-room`; сцена `looking-around-the-room`; `correspondence` |
| Gardiner’s Dream Journal (врезка) | 13 | книга `gardiners-dream-journal`; сцена `reading-the-books` |
| The Book of Dreams (текст; Language (Greek), Occult; Keeper note) | 13–14 | книга `book-of-dreams`; сцена `reading-the-books` |
| Speaking to Mrs. Madeira; What Mrs. Madeira knows | 14–15 | сцена `speaking-to-mrs-madeira`; `mrs-madeira` |
| The Book of Dreams (врезка: чтение, Spells — Prepare The Body, Travel To Dreamlands) | 15 | книга `book-of-dreams` (`reading`, `spells`, описание вариантов) |
| The Monster Rises! (+ Possible bouts of madness) | 15–16 | сцена `the-monster-rises`; таблица сценария «Возможные приступы безумия»; прегены (`description`) |
| Combat (Tactics, Targeting the head) | 16 | сцена `combat`; Тварь-Гардинер (`legend`, способности) |
| More police Arrive | 17 | сцена `more-police-arrive` |
| Conclusion (эпилог, 1d6 Рассудка) | 17 | сценарий (`conclusion`) |
| Appendix A: NPCs and Monster — Detective Lt. Milligan | 17 | `milligan` |
| Patrolman Malone | 17 | `malone` |
| Gardiner-Thing, monster from dreams (Special Powers: Song of Lost Dreams; атаки, Armor, Spells, Skills, Sanity Loss) | 17–18 | существо `gardiner-thing` |
| References | 18 | сценарий (`advice`, «Источники») |
| Collected Handouts: Handout 1, Handout 2 | 19 | раздатки 1 и 2 (текст как напечатан, картинки) |
| Map: Gardiner’s Room | 20 | карта `gardiners-room`; место `gardiners-room` |
| Pre-Generated Investigators: листы (Characteristics, Skills, Weapons, Combat) | 21, 23, 25, 27, 29, 31 | прегены (`statblock`, картинка-лист) |
| Обороты листов: The Landlord or Landlady*, The Bookstore Owner, Business Associate, Nosy Neighbor, The Tough Guy, The Beat Cop (Roleplaying hooks, Other tenants) | 22, 24, 26, 28, 30, 32 | прегены (`legend`, `description`, `background.secret`) |

## Не взято

- Колонтитулы «Call of Cthulhu Demo Game», строки об авторском праве и сайт Chaosium в выходных данных — оформление (авторы — в `summary` и `sources` сценария).
- Копии раздаток 1–2 в тексте (с. 12) — дубль приложения (с. 19): страница в `sources` раздаток, картинки взяты из приложения.
- Силуэты вместо портретов на листах — портретов в книге нет; листы целиком — картинки `card`.
- Реальные книги из комнаты («Мифы и легенды Древней Греции и Рима» Э. М. Беренс, «Толкование сновидений» Фрейда, книги о финансах, путеводители) и банковский управляющий Гардинера, муж миссис Мадейры, богатый коллекционер — без своих записей, текстом в предметах и сценах.
- Рэндольф Картер (сравнение в предыстории) и Страна грёз — записей в базе нет (нет `coc:character:randolph-carter`, нет записи места «Страна грёз»); остаются текстом.
- Варианты заклинаний «Prepare The Body» и «Travel To Dreamlands» — своих записей в справочнике нет (`kb/spells/` мне не принадлежит); описаны полностью в «Книге снов», ссылки — на исходные заклинания. Кандидаты в общие записи: `coc:spell:prepare-the-body` (`variant_of` Flesh Ward), `coc:spell:travel-to-dreamlands` (`variant_of` Mind Transfer), как уже заведённый `mind-transfer-sacred-flame`.
- Полицейский участок, куда бежит Томми, — без записи (в книге без названия), в `based_at` полиции — Провиденс с пометкой.

## Опечатки и сомнения

- Томми: на листе управляющего (с. 22) «10-year-old», везде (с. 8, 24, 26, 28, 32) — 11 лет; `errata` Томми и управляющего, в записи — 11.
- Лейтенант Миллиган и патрульный Мэлоун: Build 0 при СИЛ 70 + ТЕЛ 65 = 135 (по таблице 1 при напечатанном БкУ +1d4) — `errata`, как напечатано (Р-161).
- Тварь-Гардинер: Build 0 при СИЛ 90 + ТЕЛ 60 = 150 и БкУ +1d4 — исправлено на 1 по большинству (Р-36), `errata` `fixed: true` + `corrections`. Скорость 7 (по формуле было бы 8) — как напечатано, пометка.
- Отметки на шкалах листов не совпадают с числами в рамках: крутой парень — ПЗ 12 в рамке, обведено 11 (с. 29); патрульный — ПМ 14, обведено 11 (с. 31); владелец книжной лавки — ПМ 10, обведено 11 (с. 23). В записях — числа в рамках, `errata`.
- Крутой парень «живёт на первом этаже» (с. 7), а комната семьи Скиргайла — на втором (с. 6) — `errata` прегена.
- Врезка «Fitting a Two Hour Time Limit»: текст говорит «comfortably fits into a one-hour slot», расписание — на два часа (90 и 110 минут) — `errata` сценария.
- Срок заказа обсидиановых ножей: «some months back» (с. 7) и «about a year ago» (с. 26) — пометка у делового партнёра.
- Владелец книжной лавки не видел Гардинера «неделю» (с. 24), остальные — два дня: взгляд персонажа, не правилось.
- После потери 5+ Рассудка книга просит «Idea roll» (по «Книге хранителя» — проверка ИНТ) — как напечатано, пометка сцены.
- Список заклинаний книги «Travel To Dream Lands», заголовок — «Travel To Dreamlands» — пометка книги.
- Греческий текст раздатки 1 напечатан с пропущенными пробелами и «Sothoth» латиницей — как напечатано.
- Карта: «Wardobe» (Wardrobe) — метка как напечатано, `note`.
- «Painting» управляющего понято как малярное дело (вывод); «Business» делового партнёра стоит в строках Art/Craft — записано как Искусство/ремесло (коммерция).
- Языки на листах: у любопытного соседа родной — немецкий, у крутого парня (родился в Литве) родной — английский, литовский — иностранный; как напечатано.
- Профессия делового партнёра в справочнике — «Бутлегер/головорез» (по «bootlegger», с. 7) — вывод; у управляющего, любопытного соседа и крутого парня профессии справочника нет.
- Что «Книгу снов» Гардинер купил на распродаже наследства (лист букиниста, с. 24), книга прямо не говорит — пометка, не утверждается.

## Термины книги (English → Russian)

| English | Русский |
|---|---|
| Dead Boarder | «Мёртвый жилец» (псевдоним «Мёртвый постоялец») |
| An Extended Demo for Call of Cthulhu | расширенная демонстрационная игра «Зова Ктулху» |
| boarding house / Ma Shanks’ Boarding House | пансион / пансион Ма Шэнкс |
| boarder / tenant / resident | жилец |
| room-and-half-board | комната с половинным пансионом |
| Loretta “Ma” Shanks | Лоретта «Ма» Шэнкс |
| The Landlord (or Landlady) | управляющий (управляющая) пансионом |
| The Bookshop Owner / Book Store Owner / Bookseller | владелец (владелица) книжной лавки / букинист |
| Business Associate | деловой партнёр (деловая партнёрша) |
| Nosy Neighbor | любопытный сосед (любопытная соседка) |
| The Tough Guy/Dame | крутой парень (крутая дамочка) |
| would-be hoodlum | будущий хулиган |
| The Beat Cop | патрульный полицейский (официальная профессия) |
| The Extra Police | подкрепление (полиции) |
| Detective Lt. Milligan | лейтенант Миллиган (детектив-лейтенант) |
| Patrolman / Officer Malone | патрульный Мэлоун |
| James Gardiner | Джеймс Гардинер |
| Mrs. Madeira | миссис Мадейра |
| Tommy | Томми |
| Skirgaila family: Anikke, Dovana, Petras, Konstantinas | семья Скиргайла: Аникке, Дована, Пятрас, Константинас |
| “Double Barrel” Angelo | Анджело «Двустволка» |
| the Mob / local gangsters | мафия (запись «Мафия Провиденса») / местные гангстеры |
| speakeasy | подпольный бар (спикизи) |
| bootlegger / bootleg spirits | бутлегер / подпольный спирт |
| “cook the books” / false ledger / accounting ledgers / forged receipts | «подправить бухгалтерию» / поддельная книга учёта / бухгалтерские книги / поддельные квитанции |
| “orchids” (slang) | «орхидеи» (дорогие вещи) |
| Federal Hill | Федерал-Хилл (как в базе) |
| Providence, Rhode Island | Провиденс, Род-Айленд (как в базе) |
| Summer Solstice | летнее солнцестояние |
| Gardiner-Thing, monster from dreams | Тварь-Гардинер, чудовище из снов |
| entity from beyond / otherworldly entity | сущность из-за пределов / потусторонняя сущность |
| ancient sorcerer | древний колдун |
| Song of Lost Dreams | Песнь утраченных снов |
| dazed / distracted | в оцепенении / теряет сосредоточенность |
| throat-orifice | горло-отверстие |
| Grab book (mnvr) | Схватить книгу (манёвр) |
| ritually scarred skin / swirls / scarification | кожа в ритуальных шрамах / завитки / нанесение шрамов |
| The Book of Dreams | «Книга снов» |
| Dream Land (в «Книге снов») | Земля снов |
| “dream book” | «книга снов» (в снах монаха) |
| Dreamlands | Страна грёз (по глоссарию) |
| “free thy mind from thy fleshy prison” | «освободить разум из темницы плоти» |
| “render thy body still” | «упокоить тело» |
| “thy vessel is pure and prepared as living armor” | «сосуд чист и приготовлен как живая броня» |
| petitioner / vessel | проситель / сосуд |
| Prepare The Body (Flesh Ward variant) | «Подготовка тела» (вариант Защиты плоти) |
| Travel To Dreamlands / Dream Lands (Mind Transfer variant) | «Путешествие в Страну грёз» (вариант Переноса разума) |
| Gardiner’s Dream Journal | «Дневник снов Гардинера» |
| “the Tome” | «Том» |
| “powerful being” | «могущественное существо» |
| The Dreamer’s Dictionary | «Словарь сновидца» |
| Myths and Legends of Ancient Greece and Rome (E.M. Berens) | «Мифы и легенды Древней Греции и Рима» (Э. М. Беренс) |
| The Interpretation of Dreams (Sigmund Freud) | «Толкование сновидений» (Зигмунд Фрейд) |
| A Primer in Greek Vocabulary | «Начальный словарь греческого языка» |
| Dream Interpretation (навык листа) | толкование снов |
| Handout 1 / Handout 2 | раздатка 1 / раздатка 2 |
| The Gate and the Key | Врата и Ключ |
| tarpaulin | брезент |
| black candles | чёрные свечи |
| obsidian blade / knives | обсидиановый клинок / нож |
| ornate bookcase / secret compartment | резной книжный шкаф / тайник |
| bookend (human-like squid creature) | книгодержатель-спрут |
| Oriental rug | восточный ковёр |
| wardrobe / nightstand / upholstered chair / wall-mounted cabinets / long table by the door | платяной шкаф / тумбочка / мягкое кресло / шкафчики / длинный стол у двери |
| laudanum / cocaine | лауданум / кокаин |
| jar of pennies | банка с монетами |
| Plutomania | плутомания (тяга к богатству) |
| paranoia / delusion / psychosomatic loss of vision | паранойя / бред / психосоматическая потеря зрения |
| Sanity roll / Idea roll / Know roll | проверка Рассудка / проверка Идеи / проверка Знаний |
| Regular / Hard / Extreme success | обычный / трудный / чрезвычайный успех |
| pushing the roll / pushed roll | повторная проверка |
| Luck spending / spending Luck | трата Удачи |
| bout of madness / temporary insanity / involuntary action | приступ безумия / временное безумие / непроизвольное действие |
| outnumbered / point-blank / firing into melee | численное превосходство / стрельба в упор / стрельба в гущу рукопашной |
| bonus die / penalty die | бонусная кость / штрафная кость |
| opposed POW / STR roll | встречная проверка МОЩ / СИЛ |
