# manco — «The Cursed Idol of Manco Capác» (Р-221)

Сценарий The Yellow Hand (2025), Джаред Тэллис и Джей Сойдэлиус; 52 страницы, 1937 год, Нью-Йорк и Бриджпорт.

- Издание: 7-я редакция (характеристики в процентах, доли 1/2 и 1/5, Комплекция, БкУ) — статблоки перенесены полностью.
- Страницы: печатный номер = физический (смещение 0; проверено по номерам на изображениях с. 9, 16, 33–37, 44–46).
- Числа — по английскому оригиналу (текстовый слой; статблоки, клетки ПЗ, реестр раздатки 11, обложка раздатки 13 —
  по изображениям страниц). Русский текст — по переводу владельца `2_Обработка\идол манко\document.html`; флаг
  `translated` у всех записей. Где перевод владельца расходится с книгой в числах (ПЗ: Капуто 12 вместо 13, Головорез 10
  вместо 12, Патрульные 11 вместо 12, Демон 15 при 15 клетках), взято по книге. Термины владельца сохранены: «Пылающая
  Рука», «Хранитель Огня», «Призрак», «Круг Ночи», «Старая таверна» (Ye Olde Tavern); curator — «куратор» (у владельца
  и «хранительница»: алиас — чтобы не путать с Хранителем).
- Эпоха `1930s`, ruleset `core` (книга — для 7-й редакции, «pulp-style», правила Pulp Cthulhu не используются).
- Новый общий город (Р-190): `coc:location:bridgeport` (`kb/locations/bridgeport.json`). Нью-Йорк — существующий
  `coc:location:new-york`; районы — записи «Масок» (Нижний Манхэттен, Мидтаун, Бруклин, Окрестности Нью-Йорка, Бронкс,
  Центральный парк); Синг-Синг и Нью-Йоркская публичная библиотека — записи «Масок» (дополнения — предложениями).
- Карты (8): `B/map/new-york-vicinity` (20 меток), `manhattan` (30), `museum` (31), `cox-apartments` (25),
  `cross-tenement` (3), `abandoned-church` (6, одна вычисленная), `bridgeport` (7), `bas` (21); картинки
  `app/maps/manco-*.jpg` (вырезки страниц 150 dpi); метки проверены глазами на наложении.
- Предложения: `proposals-manco.json` — 32 правки (Нью-Йорк: эпоха 1930s, таблица «Нью-Йорк в 1937 году», ссылки,
  источник; Синг-Синг, публичная библиотека, Центральный парк «Масок»: абзац 1937 года, источники; ссылки районов
  «Масок» на новые места; `source_variants` оружия: кинжал, кастет, ракетница, пистолет .38). `apply.py --dry-run` — проходит.

Сокращение `B/` = `cursed-idol-of-manco-capac-en/`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул, эпиграф Лавкрафта | 1, 3 | `B/scenario/cursed-idol-of-manco-capac` (sources); эпиграф — не взят (см. ниже) |
| Table of Contents; Credits; Note (адаптация с Tales of Menace & Mystery) | 4 | `B/scenario/…` (summary, advice) |
| Tales of Menace & Mystery: About…, Adventures and Articles, About the Time Period, врезка A Different Role-Playing Game | 5 | `B/organization/tales-of-menace-and-mystery`; `B/scenario/…` (hook, advice) |
| Иллюстрация «5 Tudor Place» | 6 | `B/location/tales-bullpen` |
| The Bullpen; The Pitch; The Editor: Stanley M. Liebowitz; The Owner: Esther Beauchamp | 7 | `B/location/tales-bullpen`; `B/character/stanley-liebowitz`, `B/character/esther-beauchamp` |
| The Ghost; The Truth; The Attorney: Phillip J. Cox; Chester K. Bancroft; Player Characters + The Ghost | 8 | `B/character/the-ghost` (Кокс — алиас), `B/character/chester-bancroft`; `B/location/cox-apartment`, `B/location/bancroft-apartment` |
| План квартир Кокса и Бэнкрофта, Bottom Floor Entrance; подпись «Donnerwetter Incident» | 9 | `B/map/cox-apartments`; подпись — в `B/character/the-ghost` (quality.notes) |
| Prologue; Background; The Expedition; The Return; врезки The Legend, The Cursed Artifact | 11 | `B/scenario/…` (keeper_info); `B/creature/demon-of-pacaritambo` (legend); `B/item/idol-of-manco-capac` |
| Scenario Flowchart: Locations, Timeline, The Ritual | 12 | `B/scenario/…` (tables «Хронология», «Блок-схема: места и персонажи», keeper_info) |
| Scenario Flowchart: Characters, Clues & Handouts | 13 | `B/scenario/…` (tables «Блок-схема…», «Улики и раздаточные материалы») |
| Act 1 The Lost Idol; Scene 1: The Museum of Antiquities; врезки Characters, Keeper Note | 15 | `B/scene/museum-arrival`; `B/character/andrew-turner`, `irene-cooper`, `lucas-steel` |
| Museum Security | 15, 17 | `B/scene/museum-security` |
| New York Map + Travel Times | 16 | `B/map/new-york-vicinity`; `B/scenario/…` (table «Время в пути») |
| Security Guards | 17 | `B/scene/security-guards`; `B/character/douglas-payne`, `robert-moore` |
| Security Records | 17 | `B/scene/museum-security` |
| Museum Curator | 17 | `B/scene/museum-curator` |
| Empire of the Sun Exhibit | 17 | `B/scene/empire-of-the-sun-exhibit`; `B/item/meteorite-encasing`, `B/item/incan-reference-tomes` |
| Investigating the Museum Staff | 17 | `B/scene/investigating-museum-staff` |
| Act 2 Search for the Missing Idol; Scene 1: Travel; врезки Keeper Note, Characters | 19 | `B/scene/travel`; `B/character/angelo-caputo`, `nick-romano`, `thomas-cross` |
| Scene 2: Research and Connections; Deeper Research | 19–20 | `B/scene/research-and-connections` |
| Scene 3: Long Island; Encounter: The Burning Hand | 20 | `B/scene/burning-hand-encounter`; `B/character/henchmen` |
| Thomas Cross’ Apartment; Outside; The Tenement; The Apartment | 20 | `B/scene/cross-apartment`; `B/location/cross-tenement`, `cross-apartment`; `B/item/curtis-receipt`, `cross-calendar`, `amulet-of-protection` |
| Unwanted Guests; Meeting the Enforcer | 20–21 | `B/scene/unwanted-guests` |
| The Romano Estate; Meeting Nick Romano | 21 | `B/scene/romano-estate`; `B/location/romano-estate` |
| Abandoned Church; The House | 21 | `B/scene/abandoned-church`; `B/location/church-wooden-house`; `B/item/museum-plans`, `warped-box` |
| Scene 4: Upstate New York; Sing Sing Prison; The Interview; врезка Characters | 22–23 | `B/scene/sing-sing`; `B/character/joseph-bennet`, `sing-sing-inmate`, `phil-brady`, `jordan-reed`, `milton-thames`, `henry-curtis` |
| Scene 5: Bridgeport, Connecticut; Bridgeport Police Station; The Police Captain | 23–24 | `B/scene/bridgeport-police-station`; `B/location/bridgeport-police-station` |
| Врезка Keeper Note (Lily, Archie, Florence, Ryland) | 24 | `B/character/lily-bennet`, `archie-bennet`, `florence-taylor`, `ryland-bennet`; `B/scene/bennet-home` |
| The Detective | 24 | `B/scene/the-detective` |
| Joseph Bennet’s Home; Using Stealth; The Direct Approach; Looking Upstairs | 24–25 | `B/scene/bennet-home`; `B/location/bennet-house`; `B/item/bennet-jewels` |
| Bridgeport Archaeological Society; Reception; Library; Main Offices | 25–26 | `B/scene/bridgeport-archaeological-society`; `B/character/penelope-brown`; `B/item/bas-master-keys`, `thames-notebook` |
| Curtis’ Antiquities; The Storefront; The Rear of the Shop; Heading Outside | 26 | `B/scene/curtis-antiquities`; `B/character/timothy-guiles`, `beat-cops`; `B/item/curtis-office-papers` |
| Calling Ye Olde Tavern | 26 | `B/scene/calling-ye-olde-tavern`; `B/location/ye-olde-tavern` |
| The Tongue Point Lighthouse; The Attack | 27 | `B/scene/tongue-point-lighthouse`; `B/location/tongue-point-lighthouse` |
| Act 3 Race to the Museum; The Ghost; врезки The Ritual, Characters | 29 | `B/scene/the-ghost`; `B/scenario/…` (keeper_info); `B/character/lorenzo-romano`, `the-firekeeper` |
| Scene 1: Travel (акт 3) | 29 | `B/scene/race-travel`; `B/scenario/…` (table «Время в пути») |
| Scene 2: Consequences | 29–30 | `B/scene/consequences`; `B/character/bystanders` |
| Врезки The Idol, The Amulet, The Firekeeper | 30 | `B/item/meteorite-encasing`, `B/item/amulet-of-protection`, `B/character/the-firekeeper` |
| Scene 3: The Demon of Pacaritambo; Before 6pm | 30 | `B/scene/before-6pm` |
| After 6pm; Smashing the Idol; Sealing in the Demon | 30–31 | `B/scene/after-6pm`; `B/item/idol-of-manco-capac` |
| Врезка Possession: Mechanics, Resisting Possession | 31 | `B/creature/demon-of-pacaritambo` (ability «Одержимость»); `B/scene/after-6pm` |
| Scene 4: Epilogue; If PCs Succeed; If PCs Fail; What Happens to Irene Cooper?; What Happens to The Firekeeper? | 31 | `B/scene/epilogue`; `B/scenario/…` (conclusion) |
| Locations — Getting to / Arriving in / Staying in / Getting Around in New York; New York; Contact; Locations of Interest | 32 | предложение: таблица «Нью-Йорк в 1937 году» в `coc:location:new-york`; `B/character/speedy-durante`; `B/location/nypd-headquarters`; Центральный парк — предложение к записи «Масок» |
| Карта Нью-Йорка | 33 | `B/map/manhattan` |
| Manhattan — Museum of Antiquities; 1. Museum Entry … 5. Main Exhibit Hall; план | 34 | `B/location/museum-of-antiquities`, `museum-1-entry` … `museum-5-main-exhibit-hall`; `B/map/museum` |
| New York Public Library | 35 | предложение к `masks-of-nyarlathotep-en/location/america-new-york-public-library` |
| Upstate New York — Sing Sing Prison | 35 | предложение к `masks-of-nyarlathotep-en/location/america-sing-sing` |
| Long Island — Romano Family Estate | 35 | `B/location/romano-estate` |
| Brooklyn — Thomas Cross’ Apartment; The Apartment; поэтажный план | 35 | `B/location/cross-tenement`, `cross-apartment`; `B/map/cross-tenement` |
| Queens — Abandoned Church; The Church; The Wooden House; план | 36 | `B/location/abandoned-church`, `church-hidden-chamber`, `church-wooden-house`; `B/map/abandoned-church` |
| Карта Bridgeport | 36 | `B/map/bridgeport`; `coc:location:bridgeport` |
| Bridgeport — Bridgeport Police Station; The Archaeologist’s House; Curtis’ Antiquities | 36 | `B/location/bridgeport-police-station`, `bennet-house`, `curtis-antiquities` |
| Bridgeport Archaeological Society; Reception; Main Offices; Dorms; Library; Exhibits; план | 37 | `B/location/bas`, `B/location/bridgeport-environs`; `B/map/bas` |
| Handout #1 | 38 | `B/handout/01-invitation` |
| Handouts #2, #3, #4 | 39 | `B/handout/02-red-hook-article`, `03-cursed-expedition-article`, `04-eye-ripper-article` |
| Handouts #7, #8, #9, #10, #14 | 40 | `B/handout/07-amulet-of-protection`, `08-burning-hand-amulet`, `09-encasing-warm-half`, `10-encasing-museum-half`, `14-matchbook` |
| Handouts #5, #6, #12; Bridgeport Map | 41 | `B/handout/05-burning-hand-note`, `06-incan-parchment`, `12-bennet-journal`, `bridgeport-map` |
| Handouts #11, #13 | 42 | `B/handout/11-sales-ledger`, `13-incan-history-excerpt` |
| Organizations: BAS, Desanti Family, Romano Family, The Burning Hand, The Circle of Night | 43 | `B/organization/bridgeport-archaeological-society`, `desanti-family`, `romano-family`, `burning-hand`, `circle-of-night` |
| NPCs: Lucas Steel, Irene Cooper, Angelo Caputo, Henchman | 44 | `B/character/lucas-steel`, `irene-cooper`, `angelo-caputo`, `henchmen` |
| NPCs: Thomas Cross, Cultist, Henry Curtis, Beat Cops | 45 | `B/character/thomas-cross`, `cultists`, `henry-curtis`, `beat-cops` |
| NPCs: Bystanders, Milton Thames, The Ghost, The Demon of Pacaritambo | 46 | `B/character/bystanders`, `milton-thames`, `the-ghost`; `B/creature/demon-of-pacaritambo` |
| Pre-Generated Characters: Sam Steele, Nathan Peterson | 47 | `B/character/sam-steele`, `nathan-peterson` |
| Pre-Generated Characters: Delilah Miller, Luther Deveraux | 48 | `B/character/delilah-miller`, `luther-deveraux` |
| Задняя обложка (3 акта, 6–12 часов, 4 готовых персонажа) | 52 | `B/scenario/…` (summary) |

Персонажи, упомянутые только в раздатках, тоже заведены: `B/character/rocky-barone`, `bruce-pickering` (раздатка 2),
`cassandra-miles`, `henry-palmer`, `miles-cambridge` (раздатка 3).

## Не взято

- Эпиграф Лавкрафта (с. 3) и рекламные страницы The Yellow Hand (с. 49–51: Once Upon…, Draconicus, Sentience, Ashland,
  Redacted, контакты) — не материал сценария.
- Иллюстрации без игровой информации (с. 2, 10, 14, 18, 28; дирижабль на с. 9; портреты) — картинки в записи не
  добавлялись (`images` не заполнены; можно добавить `pipeline/art/add_images.py`, в том числе рисунки раздаток 6–10, 14).
- Пещера на горе Кондор-Туко (Перу) отдельной записью не заведена: для места без города нужен общий город (Куско в базе
  нет), а сюжет там не разыгрывается; пещера описана в `B/item/idol-of-manco-capac`, раздатках 3, 12, 13 и в keeper_info.
- Безымянные эпизодические роли без статблока и своей механики оставлены текстом сцен: хозяин доходного дома, бармен
  «Старой таверны», швейцар общества, двое неодержимых в лавке, охрана Синг-Синга; ресторан «Розати» — упоминание.
- Реальные исторические лица, упомянутые мимоходом (комиссар Льюис Валентайн, мэр Фьорелло Ла Гуардия, Аль Капоне в
  обрывке газеты под раздаткой 2), Хьюго Бошан (дед Эстер), Хизер Беннет (жертва) — только в текстах записей.
- «Ultio Dei» (связь Хранителя Огня) и «Трое» (главы Пылающей Руки) — упомянуты по одному разу, без описания: текстом в
  `B/character/the-firekeeper` и `B/organization/burning-hand`.
- Заклинание на пергаменте (раздатка 6) и «любые два заклинания» Демона — книга не называет заклинаний; новых заклинаний нет.

## Опечатки и сомнения книги (errata в записях)

- ПЗ по клеткам не сходятся с (ВЫН+ТЕЛ)/10: Лукас Стил 10 (ожид. 11), Культисты 10 (11), Генри Кёртис 13 (11), Демон 15 (19).
- ПМ ≠ МОЩ/5: Культисты 13 (11), Демон 9 (30), Сэм Стил 14 (12), Лютер Деверо 13 (11).
- Скорость: Томас Кросс 8 (7), Прохожие 8 (9), Культисты 9 (8), Милтон Темз 9 (8). Призрак: БкУ +1d6 и Комплекция +2
  при СИЛ+ТЕЛ 160 (ожид. +1d4 и 1). Натан Питерсон: Рассудок 70 при МОЩ 60; пистолет .38 с уроном 1d6.
- Сэм Стил: «.38 Revolver 50% (25/5)» — пятая исправлена на 10 (Р-35).
- Время в пути: карта (с. 16) и текст (с. 19) расходятся (40/45 мин, 20/25 мин) — в таблице оба числа.
- Номера раздаток 9 и 10 в списке блок-схемы переставлены относительно текста и рисунков.
- Ссылки не туда: «The Legend on p5» (врезка на с. 11); амулет «see page 25» (врезка на с. 30); «Residents NPC stats»
  (профиль называется Bystanders); «Ye Olde Inn» (с. 13) вместо Ye Olde Tavern; выставка «Legacy of the Inca Exhibit»
  (с. 34) вместо «Empire of the Sun»; экспедиция вышла в августе (с. 11) / в октябре (раздатка 3).
- Без errata, в quality.notes: кевларовая броня Призрака в 1937 году; Ред-Хук статья относит к Куинсу; музей назван
  двухэтажным, а на плане три этажа; план на с. 35 не подписан (отнесён к доходному дому Кросса — вывод).

## Вопросы владельцу

1. Демон Пакаритамбо заведён как `supernatural` («демон, заточённый в идоле»); если считать его существом Мифов —
   сменить категорию.
2. Пещеру Пакаритамбо (Перу) завести отдельной записью, если появится общий город Куско (или «Окрестности Лимы»?).
