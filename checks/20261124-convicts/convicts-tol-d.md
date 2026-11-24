# Convicts & Cthulhu — Ticket of Leave #11, #12, #15 (часть tol-d)

Книги `convicts-tol-11-en`, `convicts-tol-12-en`, `convicts-tol-15-en` (оригинал, Cthulhu Reborn, 2018–2019). Печатная
страница = физической во всех трёх выпусках: **offset 0** (с. 1 — титул с номером «1»; последние физические страницы —
пустые: #11 физ. 26, #12 физ. 23, #15 физ. 27). Перевода на русский нет; весь русский текст — наш (`translated`).
#11 и #12 — 7-я редакция со статблоками; **#15 в библиотеке — «unstatted» версия** (без игровых чисел; «statted» версия
на сайте Cthulhu Reborn не зарегистрирована).

Записей: #11 — 59, #12 — 38, #15 — 40 (всего 137). Карты: 3 (`app/maps/convicts-tol-d-*.jpg`), картинки записей: 12
(`app/art/**/convicts-tol-d-*.webp`, сопоставление `art-tol-d.json`, применено). Атмосфера — `atmosphere-tol-d.json`
(14 страниц). Предложения — `proposals-tol-d.json` (3, к `convicts-tol-01-en/character/john-styles`). Черновик общей записи
заклинания — `new-shared-spell-enchant-ritual-bell-tol-d.json` (`coc:spell:enchant-ritual-bell`).

## #11 The Dispensatory of Doctor Macdead (`convicts-tol-11-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Introduction | 1 | `organization/colonial-medical-service`; `scenario/dispensatory-of-doctor-macdead` (summary) |
| The Colonial Medical Service | 2 | `organization/colonial-medical-service` |
| Questionable Practitioners | 2 | `organization/colonial-medical-service` |
| Sample Colonial-Era Medicines and their Uses (from the schedule of Medicines) | 3 | `rule/sample-colonial-era-medicines` (+ картинка перечня) |
| An Unworthy Rabble | 4 | `organization/colonial-medical-service` |
| The Colonial Surgeons | 4 | `organization/colonial-medical-service` (members) |
| John White (NSW Colonial Surgeon: 1788—1794) | 4 | `character/john-white` |
| William Balmain (NSW Colonial Surgeon: 1795—1801) | 4–5 | `character/william-balmain` |
| Thomas Jamison (NSW Colonial Surgeon: 1802—1811) | 5–6 | `convicts-cthulhu-en/character/thomas-jamison` (абзац «В „Отпускном билете“ № 11», при сведении; в `organization/colonial-medical-service` — ссылка) |
| A Campaign Frame: Investigators of the Colonial Medical Service | 5 | `rule/campaign-frame-colonial-medical-service` |
| The Hospital at Parramatta | 6 | `location/parramatta-hospital` |
| Map of Parramatta Hospital | 6 | `map/parramatta-hospital-map` (9 меток) + места `male-ward`, `female-ward`, `guard-huts`, `hospital-dispensary`, `convict-huts`, `surgeons-buildings` |
| The Hospital Buildings | 6–7 | `location/parramatta-hospital` и места построек |
| Surgeons of Parramatta | 7 | `location/parramatta-hospital` (абзац «Хирурги Парраматты»; Харрис и Уэнтуорт — refs на core) |
| The Hospital Staff | 7 | `location/parramatta-hospital` |
| Scenario Seed: The Dispensatory of Doctor Macdead | 7 | `scenario/dispensatory-of-doctor-macdead` |
| Keeper's Introduction | 7–8 | `scenario` keeper_info; `character/james-macdead` |
| A Convict Named Macdead? | 8 | `character/james-macdead` (legend) |
| The Corruption of Doctor Macdead | 8 | `scenario` keeper_info; `character/james-macdead`; `tome/dispensatory-of-the-damned` |
| The Best-Laid Plans … | 8–9 | `scenario` keeper_info; `character/maggie-miles` |
| The Dispensatory (врезка) | 9 | `tome/dispensatory-of-the-damned` (+ картинка); ссылки — `rule/further-source-material` |
| Involving the Investigators | 9–10 | `scene/summons-by-jamison`; `item/jamisons-list` |
| The True Nature of the Threat | 10 | `scenario` keeper_info |
| Getting Started: Travelling to Parramatta | 10–11 | `scene/travel-to-parramatta` |
| Parramatta Investigations | 11 | `scene/travel-to-parramatta` |
| Investigating at the Parramatta Hospital | 11–12 | `scene/parramatta-hospital-investigation`; `character/barnabas-ritter`, `john-wiley`, `maggie-miles` |
| Gossip and Rumours around Parramatta | 12 | `scene/gossip-and-rumours`; таблица сценария «Слухи Парраматты» |
| Tracking Down Initial Sufferers | 12–13 | `scene/tracking-initial-sufferers` |
| Thomas Bradbury / Mary Hart / William Green / Ann Gabel | 13–14 | `character/thomas-bradbury`, `mary-hart`, `william-green`, `ann-gabel` (+ `george-hart`, `eleanor-childs`, `joseph-mitchell`, `jeremiah-pettitt`; места `bradbury-house`, `hart-farm`, `mitchell-house`, `pettitt-farm`) |
| Clues and Information | 14–15 | `scene/tracking-initial-sufferers` |
| Other Victims | 15–16 | `scene/other-victims`; `character/richard-lift`, `isaac-jones`, `john-langley`, `amelia-lemon`, `thomas-kelly`; `location/langley-shack` |
| The Man in the Red Boat | 15 | `character/george-ball`; `scene/other-victims` |
| Halting the Transformations | 16 | `scenario` keeper_info; `tome/dispensatory-of-the-damned` |
| Investigating "Doctor Macdead" | 16–17 | `scene/investigating-macdead`; `location/macdead-house`; `item/macdead-convict-records` |
| At Coal River | 17 | `scene/at-coal-river` |
| Escape! | 17–18 | `scene/at-coal-river`; `location/macdead-hideout` |
| The Lurking Threat: Thralls of the Dispensatory | 18 | `scene/thralls-of-the-dispensatory` |
| The Corrupt Nurse: Maggie Miles | 19 | `character/maggie-miles` |
| The Malicious Wardsman: John Wiley | 19 | `character/john-wiley` |
| The Mad Doctor: James Macdead | 19–20 | `character/james-macdead` |
| The Book’s Last Stand: Defeating the Horror | 20 | `scene/books-last-stand`; `item/tub-of-alien-parts`; `location/assistant-surgeons-storeroom` |
| Mythos Options | 20 | `scenario` keeper_info; `scene/books-last-stand` |
| Option A: Transpiercer From Yuggoth | 20–21 | `scenario` keeper_info; `creature/thing-in-the-dispensatory` (legend); `scene/books-last-stand` |
| Option B: The Beast of Nine Parts | 21–22 | то же |
| Option C: The Elevation of Doctor Macdead | 22–23 | `organization/cult-of-the-rancid-tome`; `handout/burned-letter`; `scene/books-last-stand` |
| Additional Clue (×3) | 21, 22, 23 | `scenario` keeper_info; `handout/burned-letter` |
| Rewards and Penalties | 23 | `scenario` conclusion |
| Statistics | 23 | статблоки: `character/william-ascott`, `john-wiley`, `maggie-miles`, `james-macdead` |
| The Thing in the Dispensatory of the Damned | 24–25 | `creature/thing-in-the-dispensatory` (+ арт); таблица 1d8 — в `scenario` tables «Метаморфозы „Отворяющих врата“» |
| Further Source Material (Histories, Online, The Medical Text) | 25 | `rule/further-source-material` |

## #12 Fallen Stars (`convicts-tol-12-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Introduction | 1–2 | `rule/the-scientific-elite` |
| The Scientific Elite | 2 | `rule/the-scientific-elite` |
| Sir Joseph Banks (1743—1820) | 3 | `character/joseph-banks` (+ портрет) |
| Exploring the Blue Mountains | 2–3 | `rule/exploring-the-blue-mountains` |
| The Convict Explorers | 4 | `rule/the-convict-explorers` |
| The Everingham Expedition of 1795 | 4 | `rule/the-convict-explorers`; `character/matthew-everingham` |
| Matthew Everingham (1768—1817) | 4 | `character/matthew-everingham` |
| The Wanderings of John Wilson, and The Expedition of 1798 | 4–5 | `rule/the-convict-explorers`; `character/john-wilson`, `john-price` |
| Blue Mountains Crossings – historical questions | 5 | `rule/exploring-the-blue-mountains` |
| Scenario: Fallen Stars | 6 | `scenario/fallen-stars` |
| The Star That Came To Earth | 6 | `scenario` hook |
| Keeper's Introduction | 6 | `scenario` keeper_info |
| Elder Things in Australia | 7 | `rule/elder-things-in-australia`; `location/elder-thing-outpost` |
| Call and Response | 7 | `rule/elder-things-in-australia` |
| Inside the Meteorite | 7 | `rule/elder-things-in-australia`; `location/meteorite` |
| Involving the Investigators | 7–8 | `scenario` keeper_info; `character/alistair-morrant`; `scene/gathering-at-freemasons-arms` (список профессий из ToL #5) |
| Keeper’s Timeline of Events | 8 | `scenario` tables «Хронология событий для Хранителя» |
| William Paterson (1755-1810) | 9 | `convicts-cthulhu-en/character/william-paterson` (биография, роль в сценарии и портрет — при сведении; в `rule/the-scientific-elite` — ссылка) |
| Getting Started | 9–10 | `scene/gathering-at-freemasons-arms`; `item/expedition-maps-and-journals` |
| A Much-Revered Aboriginal | 10 | `scene/much-revered-aboriginal`; `character/burraga` |
| Travelling to the Blue Mountains | 10–11 | `scene/much-revered-aboriginal` |
| Day 1 / Day 2 | 11 | `scene/much-revered-aboriginal`, `scene/day-2-nepean` |
| Day 3; Encounter: Aboriginal Settlement | 11–12 | `scene/aboriginal-settlement`; `location/gundungurra-settlement`; `character/junba` |
| First People of the Blue Mountains Region (Reprinted from ToL #7) | 12 | `convicts-tol-07-en/rule/first-peoples-of-the-blue-mountains` (перепечатка; запись #12 слита при сведении) |
| What Brought The Star Here? | 12 | `rule/elder-things-in-australia` |
| Day 4 | 12–13 | `scene/day-4-approach`; `location/crash-site` |
| The Crash Site (карта) | 13 | `map/crash-site-map` (10 меток + 2 без подписи) |
| Days 5 & 6: Exploring the Crash Site | 14 | `scene/exploring-crash-site` |
| The Meteorite | 14 | `location/meteorite`; `item/elder-thing-mummy` |
| The Dead Aboriginal Men | 14–15 | `character/dead-gundungurra-men` |
| The Metal Cannisters | 15 | `item/stasis-cannisters`; `item/proto-shoggoth-cannister` |
| Planning for Salvage | 15, 17 | `scene/exploring-crash-site` |
| The Alien Plant Virus (The Viral Reaction, Rolling CON, Cold) | 16 | `rule/alien-plant-virus` |
| Day 7; Encounter: Dingoes Ate My Elder Thing | 17 | `scene/dingo-attack`; `creature/mutated-dingo-pack` |
| Day 8 | 17–18 | `scene/day-8-return` |
| The Proto-Shoggoth (врезка) | 18 | `creature/proto-shoggoth-fallen-stars`; `item/proto-shoggoth-cannister` |
| Day 9; Encounter: Yowie Attack | 18–19 | `scene/yowie-attack`; `creature/blue-mountain-yowies` |
| Day 10 / Day 11 | 19 | `scene/quarantine` |
| Rewards and Penalties | 20 | `scenario` conclusion; Кристалл — `item/stasis-cannisters` → `coc:rule:crystal-of-the-elder-things` |
| The Price of Failure | 20 | `scenario` conclusion |
| Statistics: Lt. Alistair Morrant | 20–21 | `character/alistair-morrant` |
| Burraga | 21 | `character/burraga` |
| Mutated Dingo Pack | 21 | `creature/mutated-dingo-pack` |
| Proto-Shoggoth | 22 | `creature/proto-shoggoth-fallen-stars` (instance_of `coc:creature:proto-shoggoth`) |
| Three Blue Mountain Yowies | 22 | `creature/blue-mountain-yowies` (варианты #1–#3; instance_of core `yowie`) |

## #15 The Death Knells (`convicts-tol-15-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Introduction; Music in the Convict Era | 1 | `rule/music-in-the-convict-era` |
| Music of the First Nations | 2 | `rule/music-in-the-convict-era` |
| New Occupation: Musician | 2 | `rule/new-occupation-musician` (без чисел — «unstatted») |
| Military Band Music | 2 | `rule/music-in-the-convict-era` |
| Other Military Music | 3 | `rule/music-in-the-convict-era` |
| The Mystery of the Commissariat’s Bells | 3 | `rule/mystery-of-the-commissariats-bells` |
| Civilian Music; вырезка «Sydney Gazette» 1803 | 3 | `rule/music-in-the-convict-era` (+ картинка вырезки) |
| Scenario: The Death Knells | 4 | `scenario/death-knells` |
| Gamemaster’s Introduction | 4 | `scenario` keeper_info; `scene/three-dead-men` |
| The Truth of the Matter | 4 | `scenario` keeper_info; `character/charles-sedgwick`, `matthew-sedgwick` |
| One Man’s Conspiracy | 4–5 | `scenario` keeper_info; `character/matthew-sedgwick` |
| A Brother’s Coldness | 5 | `scenario` keeper_info; `character/charles-sedgwick` |
| The Tale of Charles and Matthew Sedgwick | 5 | `scenario` tables «История Чарльза и Мэтью Седжвиков»; `character/black-richard` |
| Involving the Investigators | 6 | `scene/three-dead-men` |
| Getting Started: Three Dead Men | 6, 8 | `scene/three-dead-men`; `item/leather-garottes`, `ms-handkerchief`, `french-boarding-axe`, `harbour-bell` |
| Timeline of Recent Events | 7 | `scenario` tables «Хронология недавних событий» |
| A Trail of Blood | 8 | `scene/trail-of-blood`; `character/mrs-hanrahan` |
| Asking The Night Watch | 8–9 | `scene/asking-the-night-watch` (Стайлз — запись tol-a, предложения) |
| The House on Mulgrave Street | 9 | `location/matthew-sedgwick-house`; `scene/house-on-mulgrave-street` |
| Death is a Cold Mistress | 9 | то же |
| Sedgwick’s Current Diary | 10 | `handout/matthew-sedgwick-journal`; `item/matthew-old-journals` |
| Other Clues in the House | 10 | `item/melted-handbells`; `location/matthew-sedgwick-house` |
| Extract from Matthew Sedgwick’s Journal (text version) | 11 | `handout/matthew-sedgwick-journal` (текст полностью + перевод) |
| Questions around Sydney Town; About the Sedgwick Brothers and Matthew’s Recent Antics | 10, 12 | `scene/questions-around-sydney` |
| What the Reverend Knows | 12 | `scene/questions-around-sydney` (Марсден — core) |
| Shops and Auction Houses | 12 | `scene/questions-around-sydney`; `character/david-bevan` |
| The Flattened Convict | 12–13 | `scene/questions-around-sydney` |
| The Commissariat | 13 | `scene/the-commissariat`; `item/ritual-bells` |
| Charles Sedgwick and his Convict Crew | 14 | `scene/charles-and-his-convict-crew`; `character/charles-convict-crew` |
| The Boss Man | 14–15 | `scene/charles-and-his-convict-crew`; `character/charles-sedgwick` |
| Searching Charles’ Belongings | 15 | `item/charles-flute-scores` |
| What Happens Next? | 15–16 | `scene/a-cold-fate` |
| A Cold Fate | 16 | `scene/a-cold-fate`; `character/john-kettle`, `callum-mcallister` |
| Following Charles and his Convict Crew | 16 | `scene/following-charles` |
| Charles’ Warehouse is on The Rocks | 17 | `location/charles-warehouse` |
| Cold Combat at the Warehouse | 17–18 | `scene/following-charles` |
| A Nocturnal Sailing Trip | 18 | `scene/nocturnal-sailing-trip` |
| карта (без заголовка) | 19 | `map/sydney-to-georges-river-map` (17 меток) |
| The Grove Near Georges River | 19–20 | `location/grove-near-georges-river`, `location/georges-river-pier` |
| The Summoning Ritual: Ringing Out The Death Knells | 20 | `scene/summoning-ritual` |
| Rewards and Penalties | 21 | `scenario` conclusion |
| Statistics; Sgt. Charles Sedgwick* | 21 | `character/charles-sedgwick` (только оружие и заклинания) |
| Ensign John Kettle / Private Callum McAllister | 22 | `character/john-kettle`, `callum-mcallister` |
| Ye Lively Nightshades | 22–23 | `creature/lively-nightshades` |
| New Spell: Enchant Ritual Bell | 22 | черновик `new-shared-spell-enchant-ritual-bell-tol-d.json`; механика — `item/ritual-bells` |
| The Thing From The Pit | 23 | `creature/thing-from-the-pit` (+ арт) |
| Further Reading (Books, Online Resources) | 23–24 | `rule/further-reading-music` |
| Extract from Matthew Sedgwick's Journal (prop version) | 25–26 | `handout/matthew-sedgwick-journal` (2 картинки) |

## Не взято

- Выходные данные, «Tickets-of-Leave are small self-contained additions…», лицензия Chaosium Fan Material Policy и
  реклама «Like what you've read…» (с. 1 и последняя страница каждого выпуска) — не материал игры.
- #11 с. 3: построчная расшифровка исторического перечня лекарств 1807 года — это скан-иллюстрация, обрезанная краями
  страницы; суть и пример групп взяты в `rule/sample-colonial-era-medicines`, сам скан — картинкой записи.
- #15: игровые числа (статблоки Чарльза, Кеттла, Макаллистера, Теней, Твари, стоимость заклинания, награды Рассудка,
  навыки профессии «Музыкант») — их нет в этой («unstatted») версии PDF; нужна регистрация «statted» версии
  (www.cthulhureborn.com/download) — вопрос ведущему.
- #15 с. 11: подпись «Port Dalrymple in 1808» под текстом дневника — посторонняя подпись без картинки, отмечена в
  `handout/matthew-sedgwick-journal` (quality.notes).
- Декоративные рамки врезок (pdfimages видит их как картинки 536×1492 и т. п.) — не иллюстрации; их показывает
  `completeness-tol-d` в `art.record_without`.
- Атмосферные иллюстрации (обложки, гравюры, ноты, старая карта #12 с. 19) — в `atmosphere-tol-d.json`.

## Опечатки и сомнения книги

- #11: с. 10 ссылается на статистику «Lt Jeremy Hale» на с. 23, а там «Lt. William Ascott» — одна запись, Хейл в псевдонимах (errata).
- #11: Макдед, Драка «30% (25/10)» — доли от 50%; исправлено на 30% (15/6) по Р-77 (errata, fixed).
- #11: Тварь из «Фармакопеи» — БкУ +3d6 / Комплекция 4 при СИЛ 150 + ТЕЛ 200 (ожидается +5d6/6); ПМ 100 при МОЩ 100 (ожидается 20) — как напечатано (errata).
- #11: «The Elevation of James Macdead» (с. 18) вместо «…of Doctor Macdead» — мелочь, не записана.
- #12: прото-шоггот — БкУ +3d6 / Комплекция 4 при СИЛ 165 + ТЕЛ 135 (ожидается +5d6/6); Укус «25% (15/5)» → 25% (12/5) (fixed); врезка говорит о плоти четырёх видов, статблок — трёх (errata).
- #12: динго-мутанты — ПЗ 12 при ВЫН 55 + ТЕЛ 35 (ожидается 9) — как напечатано (errata).
- #12: имя «Alastair» (с. 7) / «Alistair» (остальное) Морранта (errata); размер метеорита: 5 м / «over 5–6.5 m» / «более 10 м» до входа в атмосферу (errata у `location/meteorite`).
- #15: хронология (с. 5) называет схваченного в 1796 году «Sgt. Matthew Sedgwick» — это Чарльз; с. 23 «The Thing that Matthew Sedgwick wishes to summon» — тоже Чарльз (в quality.notes).
- #15: в дневнике «chanty comprises four verses», напечатаны три (errata у раздатки).
- #15: названия атак Теней «Cold Grab, Black Vapour, Doleful Wail» не совпадают с описаниями «Extreme Cold, Black Vapour, Paralysing Wail» (quality.notes).

## Связи с другими частями

- Записи core, на которые ссылаются наши: `convicts-cthulhu-en/character/{thomas-jamison, john-harris, darcy-wentworth, bennelong, william-paterson, john-hunter, samuel-marsden, john-palmer, simeon-lord, typical-convict}`, `convicts-cthulhu-en/location/{parramatta, toongabbie, coal-river, prospect-hill, sydney-hospital, freemasons-arms, blue-mountains, botany-bay, georges-river, the-rocks, government-commissariat, government-wharf, nsw-corps-barracks-and-parade, paymasters-general-store, government-house, field-of-mars, kissing-point, lane-cove, south-head, cooks-river, cape-banks, point-solander}`, `convicts-cthulhu-en/organization/nsw-corps`. Пока нет только `convicts-cthulhu-en/creature/yowie` (её ждёт `creature/blue-mountain-yowies`).
- Биографии из выпусков, которые лучше влить в записи core при сведении (Р-125): Томас Джеймисон (#11, с. 5–6 — сейчас в `organization/colonial-medical-service`), Уильям Патерсон (#12, с. 9 — в `rule/the-scientific-elite` с портретом). Предложением их не оформить: записи core появились во время работы, их текст неизвестен.
- `character/joseph-banks` (#12) — если core заведёт Бэнкса (сид «The Lights of Botany Bay»), слить (Р-154).
- `rule/first-people-of-the-blue-mountains` — врезка перепечатана из ToL #7 (часть tol-b): возможный дубль.
- Джон Стайлз — запись tol-a (`convicts-tol-01-en/character/john-styles`); дополнения — `proposals-tol-d.json`.
- Карта #15: метки North Head, Port Jackson Bay, Pinchgut I., Banks Town ведут на `coc:location:sydney` (записей нет).

## Термины (английский → русский, наш выбор)

| English | Русский |
|---|---|
| Ticket of Leave | отпускной билет («Отпускной билет» № N — выпуск) |
| convict / emancipist / free settler | каторжник / эмансипист / вольный поселенец |
| NSW Corps | Корпус Нового Южного Уэльса |
| Colonial Medical Service (CMS) | Колониальная медицинская служба |
| Colonial Surgeon / Principal Surgeon / Assistant Surgeon / Head Surgeon | колониальный хирург / главный хирург / помощник хирурга / главный хирург больницы |
| wardsman / convict nurse | санитар / сиделка-каторжница |
| Dispensatory of the Damned | «Фармакопея проклятых» |
| The Thing in the Book / in the Dispensatory | Тварь в книге / Тварь из «Фармакопеи проклятых» |
| Gate Openers | Отворяющие врата |
| thrall | раб (книги) |
| Transpiercer From Yuggoth | Пронзатель с Юггота |
| The Beast of Nine Parts | Зверь из девяти частей |
| Herald of the Outer Dark | Вестник Внешней Тьмы |
| Cult of the Rancid Tome | Культ Прогорклого Тома |
| The Elevation of Doctor Macdead | Возвышение доктора Макдеда |
| Coal River / Parramatta / Toongabbie / Rose Hill / Prospect Hill / Hawkesbury | Коул-Ривер / Парраматта / Тунгабби / Роуз-Хилл / Проспект-Хилл / Хоксбери |
| Fallen Stars / falling star | «Падшие звёзды» / падшая звезда |
| Blue Mountains / Mt. Irvine / Nepean | Голубые горы / гора Ирвин / Непин |
| Gundungurra / Darug | гандангарра / даруг |
| Clever Men / Women | знахари |
| Yowie / Blue Mountain Yowies | йови / голубогорские йови |
| Elder Thing / proto-Shoggoth | Старец / прото-шоггот (как в базе) |
| stasis cannister | стазис-контейнер |
| Alien Plant Virus | инопланетный растительный вирус |
| Mutated Dingo Pack | стая динго-мутантов |
| The Death Knells | «Похоронный звон» |
| Night Watch / Harbour Night Watch | Ночная стража / Портовая ночная стража |
| Harbour Bell | Портовый колокол |
| Government Commissariat | Правительственный комиссариат |
| Lively Nightshades | Живые Ночные Тени |
| The Thing From The Pit | Тварь из Ямы |
| Zu-chequon / Xuxikuan / Sue-Siobhán | Зу-Чекуон / Шушикуан / Сью-Шивон |
| Enchant Ritual Bell | Зачаровать ритуальный колокол |
| Black Richard | «Чёрный Ричард» |
| Game Moderator / GM | Хранитель |
| Musician (occupation) | музыкант |
