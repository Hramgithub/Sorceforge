# «Fogbound» (`fogbound-en`) — сверка переноса (Р-251, Р-134)

Источник: английский оригинал, 35 страниц PDF (Rob Leigh, Isolation Games, Miskatonic Repository, 2020; наше время, Кембридж и Корнуолл). Русского издания в базе нет (проверено по `kb/`: Портхоллоу, Харботтл, Кинкейд, Фулчард, Удока, Вечный берег — не найдены).

Номера страниц: печатный номер стоит внизу страницы начиная с физ. 2 («1»); «с. 3» — на физ. 4, «с. 24» — на физ. 25, «с. 34» — на физ. 35. Смещение для `books.json`: **offset −1** (физическая = печатная + 1). Обложка (физ. 1) — без номера.

Записи: `kb/books/fogbound-en/` — 126 (сценарий 1, сцены 32, персонажи 23, существа 2, организация 1, места 35, предметы 12, книга Мифов 1, раздатки 14, карты 5). Картинки — 21 (`art.json`, применены: 5 портретов, арт оживших пиратов, карта Макгаффри, 14 раздаток); карты — 5 файлов `app/maps/fogbound-*.jpg` (вырезки векторных карт, рамки — `fogbound-boxes.json`); атмосфера — `atmosphere.json` (11 картинок). Предложения к общим записям — `proposals-fogbound.json` (4: Бристоль, Лондон, Р’льех; пробный прогон проходит).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| обложка «Fogbound» | 1 (физ.) | `scenario/fogbound` (sources); картинка — `atmosphere.json` |
| выходные данные (Written by Rob Leigh…) | 1 | `scenario/fogbound` (sources); логотип — `atmosphere.json` |
| Table of Contents | 2 | `scenario/fogbound` (sources) |
| Introduction | 3 | `scenario/fogbound` (summary) |
| Keeper’s Information | 3–4 | `scenario/fogbound` (keeper_info); `organization/harbottles-crew`; `character/john-mcguffry`, `andrea-fulchard`, `daniel-kinkaid` |
| Porthollow Location (карта) | 4 | `map/porthollow-location-map`; `location/roseland-peninsula`, `cornwall` |
| The Idol of R’lyeh | 4–5 | `item/idol-of-rlyeh`; `location/eternal-shore`; keeper_info |
| Dramatis Personae: Steven Kinkaid, Ndidi Udoka, Zachary Westland | 5 | `character/steven-kinkaid`, `ndidi-udoka`, `zachary-westland` (портреты) |
| Charles Douglas, Jane Burroughs, Tim Murdoch, Sally Murdoch, Louis Prachet, James Prachet, Malcolm Eames, Daniel Kinkaid, Andrea Fulchard | 6–7 | одноимённые `character/*` |
| Involving the Investigators | 7 | `scenario/fogbound` (hook) |
| How it All Plays Out | 7 | `scenario/fogbound` (advice) |
| Part One: His Brother’s Keeper | 7–8 | `scene/brothers-keeper`; `location/udoka-museum`, `cambridge-england` |
| The Photograph of the Map | 8 | `scene/udoka-museum-search`; `item/mcguffry-map`; `handout/handout-01-photo-of-the-map` |
| The Udoka Museum | 8 | `scene/udoka-museum-search`; `location/udoka-museum` |
| Daniel’s Flat | 8–9 | `scene/daniels-flat-search`; `location/daniels-flat`; `item/cottage-booking-note`, `book-receipt`, `museum-floorplan` |
| Part Two: Research and Investigation | 9 | `scene/books-daniel-bought` (вступление части); advice |
| The Books Daniel Bought | 9 | `scene/books-daniel-bought`; `item/porthollow-treasure-book`, `harbottles-legacy-book`; `handout/handout-03-daniels-books` |
| Researching Porthollow | 9 | `scene/researching-porthollow`; `handout/handout-05…`, `handout-14…` |
| Talking to Zachary Westland | 9–10 | `scene/talking-to-zachary`; `location/zachary-apartment` |
| Researching John McGuffry | 10 | `scene/researching-mcguffry`; `character/john-mcguffry`, `henry` |
| John McGuffry’s Fate and the Strange Coins (врезка) | 10 | `scene/researching-mcguffry`; `item/strange-coins` |
| Researching Pete Harbottle, or the Porthollow Treasure | 10–11 | `scene/researching-harbottle`; `character/pete-harbottle`; `item/pirate-treasure` |
| Investigating the Occult and Mythos Side of the Legend | 11 | `scene/occult-and-mythos-research` |
| Part Three: Porthollow | 11 | `scene/entering-porthollow`; `location/porthollow`, `roseland-peninsula`, `cornwall` |
| Entering Porthollow | 12 | `scene/entering-porthollow` |
| Suggested Scene: Welcome to Porthollow | 12 | `scene/welcome-to-porthollow`; `character/howard-enys` |
| Suggested Scene: There is No Escape | 12 | `scene/there-is-no-escape` |
| The Current State of Porthollow | 12, 14 | `scene/porthollow-in-the-fog`; `location/porthollow` |
| Map of Porthollow | 13 | `map/porthollow-keeper-map` (22 метки: 1–10, районы, тропа, входы в пещеры) |
| Sleeping in Porthollow | 14 | `scene/sleeping-in-porthollow`; раздатки 9–10 |
| Areas of Porthollow (таблица d10) | 14 | `location/porthollow` — таблица «Район, ушедший на Вечный берег»; ссылка `from` в сценарии |
| Supernatural Inhabitants (врезка) | 14 | `scene/porthollow-in-the-fog`; `creature/troglodytes` (legend); advice |
| The Eternal Shore | 14–15 | `scene/entering-the-eternal-shore`; `location/eternal-shore` |
| Area 1: The High Road; The Village Shop | 15 | `location/high-road`, `village-shop` |
| Area 2: The Village Green; The Rumrunner Pub | 15–16 | `location/village-green`, `rumrunner-pub`; `scene/rumrunner-survivors` |
| The Rumrunner Survivors (врезка) | 16 | `scene/rumrunner-survivors`; персонажи выживших; `character/tomas` |
| The Village Hall | 17 | `location/village-hall`; `scene/village-hall-massacre` |
| Area 3: The Docks; Boat Sheds; Souvenir Shop; Jetties | 17 | `location/docks`, `boat-sheds`, `souvenir-shop`, `jetties`; `scene/boat-shed-ambush`, `souvenir-shop-madman`; `character/kenneth-teague` |
| Area 4: The Hillside; The Chapel of St. Andrew | 17 | `location/hillside`, `chapel-of-st-andrew`; `scene/chapel-vicar` |
| Suggested Scene: Bells in the Dark | 17–18 | `scene/bells-in-the-dark` |
| The Prachet’s Cottage | 18 | `location/prachet-cottage`; `scene/samantha-in-the-cottage`; `character/samantha-prachet` |
| Daniel’s Cottage; Andrea’s Journal (с врезкой характеристик) | 18 | `location/daniels-cottage`; `scene/daniels-cottage-search`; `tome/andreas-journal`; `item/glow-sticks` |
| Area 5: The Farm; The Farmyard; Footpath to the Caves | 18 | `location/farm`, `farmyard`, `footpath-to-the-caves`; `scene/cattle-barn` |
| The Caves | 19 | `location/caves`, `sea-cave`; `scene/the-caves`; `item/harbottle-symbols` |
| Harbottle’s Tunnels | 19 | `location/harbottles-tunnels` |
| Decreasing Difficulty (врезка) | 19 | `location/harbottles-tunnels`; `scene/tunnel-traps`; advice |
| Entrance | 20 | `location/tunnel-entrance`; `scene/reddingtons-remains`; `item/reddington-backpack`; `character/reddington-walton-brown` |
| Trapped Hallway | 20 | `location/trapped-hallway`; `scene/tunnel-traps` |
| Barricade Room | 20–21 | `location/barricade-room` |
| Map of the Caves and Tunnels | 20 | `map/caves-and-tunnels-map` (19 меток) |
| Store Room | 21 | `location/store-room`; `scene/daniel-in-the-store-room` |
| Blade Trap | 21 | `location/blade-trap`; `scene/tunnel-traps` |
| Banquet Room | 21 | `location/banquet-room`; `scene/banquet-of-the-dead`; `creature/reanimated-pirates` |
| Deadfall Trap | 21 | `location/deadfall-trap`; `scene/tunnel-traps` |
| Treasure Vault | 21 | `location/treasure-vault`; `item/pirate-treasure` |
| Suggested Scene: Confronting Andrea | 22 | `scene/confronting-andrea` |
| The Idol of R’lyeh (врезка: пробуждение, 50 ПМ, деактивация, уничтожение) | 22 | `item/idol-of-rlyeh` (mechanics); `scene/confronting-andrea` |
| Endings, Good and Bad | 22 | `scenario/fogbound` (conclusion) |
| The Ritual is Stopped and the Idol is Deactivated | 22 | `scene/ritual-stopped` |
| The Ritual is Completed | 23 | `scene/ritual-completed` |
| Rewards and Repercussions (награды Рассудка) | 23 | `scenario/fogbound` (conclusion); награды — также у Стивена и Ндиди |
| NPCs: Steven Kinkaid, Ndidi Udoka, Zachary Westland | 24 | статблоки в `character/*` |
| Porthollow Survivors | 24 | `character/porthollow-survivors` (групповой профиль, имена придуманы) |
| Andrea Fuchard, Daniel Kinkaid, Kenneth Teague | 24 | `character/andrea-fulchard`, `daniel-kinkaid`, `kenneth-teague` |
| Thralled Villagers | 25 | `character/thralled-villagers` (групповой профиль) |
| Troglodytes (Special Powers: Stride the Shore, Enthrall) | 25 | `creature/troglodytes` |
| Reanimated Pirates (Special Powers: Resistant to harm) | 25 | `creature/reanimated-pirates` (instance_of `coc:creature:skeleton`) |
| Handouts #1–#14 | 26–33 | `handout/handout-01…14` (картинки — вырезки страниц; #1 — фото карты) |
| Handout #5: Map of Porthollow | 28 | также `map/porthollow-player-map` (17 меток) |
| Handout #11: A Map of the Caves | 31 | также `map/caves-tourist-map` |
| карта Макгаффри (страница без текста) | 34 | `item/mcguffry-map` (картинка) |

## Опечатки и сомнения

- Имя колдуньи: «Andrea Fuchard» (с. 6 и статблок на с. 24) против «Fulchard» (везде остальное) — в записи «Fulchard», вариант в aliases и errata (`character/andrea-fulchard`).
- «Samatha» вместо «Samantha» (с. 6, 16, 18) — оба варианта в aliases `character/samantha-prachet`.
- «Varyan» вместо «Veryan» (с. 16); «McGuffty» вместо «McGuffry» (с. 11) — словесные, в aliases/пометках.
- С. 7: «they will be met by Daniel» — по смыслу Стивен (Дэниел пропал); исправлено в пересказе, errata у `scene/brothers-keeper`.
- Кеннет Тиг: ПМ 8 при МОЩ 20 (ожидается 4) — как напечатано, errata; Уклонение «20% (10/2)» — пятая исправлена на 4 (Р-35).
- Порабощённые жители: БкУ 0 и Комплекция 0 при СИЛ 60 + ТЕЛ 65 = 125 (ожидается +1d4 и 1) — как напечатано, errata.
- Ожившие пираты: ПМ 0 при МОЩ 05 (ожидается 1) — как напечатано, errata.
- Раздатка 7: корабль Харботтла нашли «in 1669» — противоречит 1686–1698; errata (не исправлено, текст раздатки).
- Раздатка 12, запись 245: «in 1768» вместо 1698; errata (не исправлено).
- Оглавление называет карту «Map of the Tunnels», на странице — «Map of the Caves and Tunnels» (отмечено в записи карты).
- Сомнение: тело Реддингтона «almost 40 years old» при исчезновении в 1976 и наше время (2020) — около 44 лет; оставлено как в книге.
- Навык «Security» (с. 8) в правилах нет; переведён «Охранные системы», оставлен текстом (Р-126).
- Стоковые фото портретов сопоставлены по порядку картинок на страницах 6–7 и внешности из описаний (мужчина под 40 — Стивен, женщина — Ндиди, старик — Закари; мужчина в капюшоне — Дэниел, женщина — Андреа).

## Не взято

- «С.», герр Миллар (Прага), Вайслер, «Книга Внешней Тьмы» (Book of the Outer Dark), «a singular Mythos text», «a very obscure tome» — только упоминания без данных; остаются в тексте раздатки 12 и сцены «Оккультная и мифологическая сторона легенды».
- Мать Макгаффри, Томас и Анна (письмо, раздатка 6) — без имени/роли, только в тексте раздатки.
- Шесть коттеджей для отдыха, шлюпка, информационная табличка у тропы — в описаниях мест (`hillside`, `jetties`, `footpath-to-the-caves`), отдельных записей нет.
- Длинные раздатки (3, 4, 6, 7, 12, 13) при переносе были даны пересказом; при переводе книги (2026-11-16) в записи вписаны полный текст как напечатан и полный перевод. Тексты для чтения вслух — в переведённой книге (`translation/`).
- Фоновые текстуры раздаток (серая бумага, 12 картинок на физ. 27–34) — оформление, не взяты.
- На картах не стали метками: ключи-легенды, заголовки карт, масштаб «200m», стрелка «North», подпись «A player version of this map is included on page 28».
- Атмосферные картинки (обложка, логотип, заставка, музей, библиотека, дорога в тумане, две фигуры в тумане, вход в пещеру, чудовище из моря, «Весёлый Роджер») — в `atmosphere.json`; поэтому `completeness` оставляет 10 находок `art.*`.
- `scenario_check`: 9 сцен без участников (обыск квартиры и коттеджа, изыскания, въезд, «Выхода нет», сон, коровник, пещеры, ловушки) — в книге там действительно нет персонажей.

## Термины (English → русский)

| English | Русский |
|---|---|
| Fogbound | В плену тумана |
| Porthollow | Портхоллоу |
| Eternal Shore | Вечный берег |
| Idol of R’lyeh | Идол Р’льеха |
| Sunken R’lyeh | Затонувший Р’льех |
| troglodytes; Spindly Hunters | троглодиты; Долговязые охотники |
| Thralled Villagers; thrall(s); Murderous Puppets | порабощённые жители; порабощённый(-е); марионетки-убийцы |
| Reanimated Pirates; Skeletal Horrors | ожившие пираты; скелеты-страшилища |
| Stride the Shore | Шаг по Берегу |
| Enthrall | Порабощение |
| Resistant to harm | Сопротивление урону (как у общего скелета) |
| Seize (mnvr) | Хватка (манёвр) |
| Shell-shocked Villagers; Porthollow Survivors | потрясённые жители; выжившие в Портхоллоу |
| Kindly Brother / Concerned Curator / Retired Historian / Maniacal Sorceress / Reformed Burglar / Homicidal Madman | Заботливый брат / Встревоженная хранительница / Историк на покое / Безумная колдунья / Исправившийся взломщик / Безумец-убийца |
| Hangman’s Wager | «Ставка висельника» |
| Smiling Pete Harbottle | «Улыбчивый» Пит Харботтл |
| McGuffry Map | карта Макгаффри |
| Porthollow Treasure; Legend of Porthollow | сокровище Портхоллоу; легенда Портхоллоу |
| Harbottle’s Tunnels | туннели Харботтла |
| The Caves; Porthollow Cliff Caves; Sea Cave(s) | пещеры в утёсах; Пещеры в утёсах Портхоллоу; морской грот (морские пещеры) |
| The Udoka Museum | Музей Удоки |
| The Rumrunner (pub) | паб «Ромовоз» |
| The High Road / The Village Green / The Docks / The Hillside / The Farm | Главная дорога / Деревенский луг / Пристань / Склон холма / Ферма |
| Village Shop / Village Hall / Boat Sheds / Souvenir Shop / Jetties / Farmyard / Footpath to the Caves | деревенский магазин / деревенский клуб / лодочные сараи / сувенирная лавка / причалы / фермерский двор / тропа к пещерам |
| Chapel of St. Andrew | часовня Святого Андрея |
| The Prachet’s Cottage / Daniel’s Cottage | коттедж Прачетов / коттедж Дэниела |
| Entrance / Trapped Hallway / Hidden Pit / Barricade Room / Store Room / Blade Trap / Banquet Room / Deadfall Trap / Treasure Vault | вход в туннели / зал-ловушка / скрытая яма / зал с баррикадой / кладовая / ловушка с лезвиями / пиршественный зал / ловушка с камнепадом / сокровищница |
| demi-culverin | полукулеврина |
| glow sticks | светящиеся палочки |
| Andrea’s Journal | дневник Андреа |
| Contact the Great Sleeper | Связь с Великим Спящим |
| Book of the Outer Dark | Книга Внешней Тьмы |
| The Porthollow Treasure (book) / Harbottle’s Legacy | «Сокровище Портхоллоу» / «Наследие Харботтла» |
| Aklo | акло |
| Security (skill) | Охранные системы |
| Roseland Peninsula / Veryan / Veryan Green / Trewartha / Carne / Truro / Parson’s Green / Arbury | полуостров Роузленд / Верьян / Верьян-Грин / Треварта / Карн / Труро / Парсонс-Грин / Арбери |
| Steven / Daniel Kinkaid | Стивен / Дэниел Кинкейд |
| Ndidi Udoka | Ндиди Удока |
| Zachary Westland | Закари Уэстленд |
| Reddington Walton-Brown | Реддингтон Уолтон-Браун |
| Andrea Fulchard | Андреа Фулчард |
| Charles Douglas / Jane Burroughs | Чарльз Дуглас / Джейн Берроуз |
| Tim / Sally Murdoch | Тим / Салли Мёрдок |
| Louis / James / Samantha Prachet | Луис / Джеймс / Саманта Прачет |
| Malcolm Eames | Малкольм Имз |
| Kenneth Teague | Кеннет Тиг |
| Howard Enys | Говард Энис |
| Tomas | Томас |
| John McGuffry / Henry | Джон Макгаффри / Генри |
| Samuel Hornby | Сэмюэл Хорнби |

Из глоссария и базы взяты: Keeper = Хранитель, Investigator = сыщик, Sanity Roll = проверка Рассудка, Hard/Extreme = трудный/чрезвычайный успех (проверка), bonus/penalty die = бонусная/штрафная кость, Credit Rating = Средства, Navigate = Ориентирование, Indefinite Insanity = бессрочное безумие, Star Spawn = звёздное отродье Ктулху, R’lyeh = Р’льех, заклинания — по общим записям («Дыхание глубин», «Связь с божеством: Ктулху», «Сотворить туман Р’льеха», «Покорение», «Защита плоти», «Знак Старших богов», «Сотворить барьер Наах-Тита»).
