# «Shadows of Leningrad» → база (часть leningrad, Р-221)

Книга `shadows-of-leningrad-en` (Mike Ferguson, Age of Cthulhu Vol. III, Goodman Games 2010), 49 страниц. Русский текст
и имена — перевод владельца `2_Обработка\1938 Тени Ленинграда\document.html`; числа — по английским страницам.

- **Редакция: 5-я** (Call of Cthulhu 5.6.1: характеристики 3–18, Таблица сопротивления, проверки Идеи/Удачи/Знания ×5).
  По Р-221 сюжет перенесён целиком, а характеристики персонажей и существ — только текстом в `description`
  («Характеристики (5-я редакция, как напечатано): …»), без статблоков 7e.
- Эпоха — 1920-е (зима 1927 года; «A 1920's Adventure»). Название в `books.json` и папке владельца — «…1938», в книге
  года 1938 нет.
- Страницы: печатный номер = физический − 1 (с. 1 на физ. 2; оглавление без offset — ведущему поставить `offset: -1`).
- Текстовый слой PDF частично закодирован шрифтом (сдвиг символов на 29); прочитан расшифровкой по шрифту, числа и
  раздатки сверены по изображениям страниц.
- Записи: `kb/books/shadows-of-leningrad-en/` — сценарий, 26 сцен, 8 раздаток, 24 предмета, 1 книга Мифов,
  2 организации, 23 персонажа (из них 5 готовых сыщиков, 2 групповых профиля), 7 существ, 39 мест, 6 карт; общий город
  `kb/locations/leningrad.json` (новый, Р-190).
- Карты: `app/maps/leningrad-orkonov-estate.jpg`, `leningrad-revolution-hospital.jpg`, `leningrad-state-museum.jpg`,
  `leningrad-orkonov-catacombs.jpg`, `leningrad-mariinsky-theatre.jpg`, `leningrad-frozen-temple.jpg` — вырезки
  страниц 46–48 (200 dpi); метки на каждом номере и подписи, проверены глазами по наложению.
- Предложения общих записей: `proposals-leningrad.json` (10; пробный прогон apply.py — ложатся все).

Префикс id ниже: `L/` = `shadows-of-leningrad-en/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка | 0 (физ. 1) | `L/scenario/shadows-of-leningrad` (sources) |
| Титул, выходные данные, Table of Contents | 1 | сценарий (summary, sources); этот файл |
| Introduction | 2 | сценарий (summary, keeper_info); `coc:location:leningrad` (history) |
| Keeper Information | 2–4 | сценарий (keeper_info); `L/organization/cult-of-ithaqua`; `L/creature/yeti`; `L/character/vasilii-orkonov`, `alexei-orkonov`, `charlotte-geoffrey`; `L/tome/book-of-dark-winter` |
| Investigation Summary (обзор сцен) | 4 | сценарий (summary, steps) |
| Investigations in Leningrad | 4–5 | сценарий (advice) |
| Врезка «But I Don’t Speak Russian! What Are They Saying???» | 4 | сценарий (advice) |
| A Note on Skills | 5 | сценарий (advice) |
| Weather | 5 | сценарий (advice); город |
| Player Beginning; We’re Here For The Paintings / Book / Girl / Justice | 5–6 | сценарий (hook, таблица «Почему сыщики едут в Ленинград») |
| Прибытие, Piotr Datsyuk (статблок) | 6 | `L/scene/arrival`; `L/character/piotr-datsyuk`; `L/location/leningrad-railway-station`, `angleterre-hotel` |
| Поминальная служба, общие сведения | 6–7 | `L/scene/memorial-service`; `L/location/tikhvin-cemetery` |
| Vladimir Yezhov, Associate Museum Curator | 7–8 | `L/character/vladimir-yezhov` |
| Врезка «So How Secret Is The Secret Police?» | 7 | `L/organization/ogpu`; сценарий (advice) |
| Dmitri Skoblin, “Artist” And OGPU Agent | 8 | `L/character/dmitri-skoblin` |
| Genrikh Rabohkov, Communist Party Official | 8 | `L/character/genrikh-rabohkov` |
| Boris Churin, Director Of The Arts | 8–9 | `L/character/boris-churin` |
| One / Two (ключ и медальон) | 9 | `L/scene/memorial-service`; `L/item/bad-wolf-medallion` |
| Scene 1 – The Orkonov Estate | 9–10 | `L/scene/orkonov-estate`; `L/location/orkonov-estate`; `L/map/orkonov-estate` |
| Джона: вопросы, медальон; статблок | 10–11 | `L/character/jonah`; `L/creature/yeti` |
| Врезка «The Medallion of the Bad Wolf» | 10 | `L/item/bad-wolf-medallion` |
| Area 1-1 – The Parlor | 11 | `L/location/orkonov-1-1-parlor`; `L/item/painting-parlor` |
| Area 1-2 – Kitchen | 11–12 | `L/location/orkonov-1-2-kitchen`; `L/item/cuckoo-clock`, `small-bloody-knife` |
| Врезка «Oh, You’re Looking At The Paintings?» | 11 | сценарий (advice); `L/scene/orkonov-estate` |
| Area 1-3 – The Pantry | 12 | `L/location/orkonov-1-3-pantry` |
| Area 1-4 – The Dining Room | 12 | `L/location/orkonov-1-4-dining-room`; `L/handout/handout-c-police-notes` |
| Area 1-5 – Charlotte Geoffrey’s Tower Studio | 12–13 | `L/location/orkonov-1-5-tower-studio`; `L/item/painting-tower-studio`, `enchanted-paints` |
| Area 1-6 – Guest Bedroom | 13 | `L/location/orkonov-1-6-guest-bedroom`; `L/item/geoffrey-letters`; `L/character/justin-geoffrey`; «People of the Monolith» — предложение copies в `coc:tome:people-of-the-monolith` |
| Area 1-7 – Servant’s Quarters | 13–14 | `L/location/orkonov-1-7-servants-quarters` |
| Area 1-8 – Master Bedroom | 14 | `L/location/orkonov-1-8-master-bedroom`; `L/item/orkonov-safe-contents` |
| Area 1-9 – Bathroom | 14 | `L/location/orkonov-1-9-bathroom` |
| Area 1-10 – Children’s Bedroom | 14–15 | `L/location/orkonov-1-10-childrens-bedroom`; `L/item/elena-churin-letters` |
| Wrapping Up Scene 1 | 15 | `L/scene/orkonov-estate` |
| Scene 2 – The Revolution Hospital | 15 | `L/location/revolution-hospital`; `L/map/revolution-hospital` |
| Area 2-1 – Reception Area, North Wing; Scene Summary | 15–16 | `L/scene/hospital-reception`; `L/location/hospital-2-1-reception` |
| Area 2-2 – Dr. Morozov’s Office | 16 | `L/scene/hospital-morozov`; `L/location/hospital-2-2-morozov-office`; `L/character/kirill-morozov`; `L/item/coroners-report` |
| Area 2-3 – Dr. Rybin’s Office | 16–17 | `L/scene/hospital-rybin`; `L/location/hospital-2-3-rybin-office`; `L/character/mikhail-rybin` |
| Area 2-4 – Storage; Four Disguised Cultists | 17–18 | `L/scene/hospital-storage`; `L/location/hospital-2-4-storage`; `L/character/disguised-cultists` |
| Area 2-5 – The Cells Of The Mad | 18 | `L/location/hospital-2-5-cells-of-the-mad`; `L/scene/hospital-katarina` |
| Area 2-6 – The Sins Of The Father | 18 | `L/scene/hospital-alexei`; `L/location/hospital-2-6-alexei-cell` |
| Area 2-7 – Cell 5B; Katarina, Little Vampire | 18–19 | `L/scene/hospital-katarina`; `L/location/hospital-2-7-cell-5b`; `L/character/katarina-orkonova` |
| Wrapping Up Scene 2 | 19–20 | `L/scene/hospital-katarina` |
| Scene 3 – The State Museum; Scene Summary | 20 | `L/scene/museum-entrance`; `L/location/state-museum`; `L/map/state-museum` |
| Area 3-1 – The Main Entrance Hall | 20–21 | `L/scene/museum-entrance`; `L/location/museum-3-1-main-entrance-hall` |
| Врезка «I Don’t Know Much About Art, But…» | 21 | `L/scene/museum-entrance`; сценарий (advice) |
| Area 3-2 – Vladimir Yezhov’s Office; Buying the Paintings | 21–22 | `L/scene/museum-yezhov-office`; `L/location/museum-3-2-yezhov-office`; `L/item/yezhov-correspondence`, `cracks-in-time` |
| Area 3-3 – Yuri Kamzanov’s Office | 22 | `L/scene/museum-kamzanov-office`; `L/location/museum-3-3-kamzanov-office`; `L/item/kamzanov-letter`; `L/character/yuri-kamzanov` |
| Area 3-4 – The Rossi Wing; 3 Enchanted Pythons | 22–23 | `L/scene/museum-rossi-wing`; `L/location/museum-3-4-rossi-wing`; `L/item/darkness-serpentine`; `L/creature/enchanted-pythons` |
| Area 3-5 – The Benois Wing; Ghast | 23–25 | `L/scene/museum-benois-wing`; `L/location/museum-3-5-benois-wing`; `L/item/relentless`, `red-shadow`, `swan-lake-tickets`; `L/creature/ghast` |
| Scene Summary (после музея) | 25 | `L/scene/museum-benois-wing` |
| Scene 4 – Return To The Orkonov Estate; Scene Summary | 25 | `L/scene/estate-return`; `L/location/church-ruins`; `L/map/orkonov-catacombs` |
| Area 4-1 – The Sanctum Of Learning | 25–26 | `L/scene/sanctum-of-learning`; `L/location/orkonov-4-1-sanctum-of-learning`; `L/item/orkonov-family-chronicle`, `bone-scroll-cases`; `L/handout/handout-g-mikhail-note`; `L/character/mikhail-orkonov` |
| Area 4-2 – Descent Into Darkness; 3 Zombies | 26–27 | `L/scene/descent-into-darkness`; `L/location/orkonov-4-2-descent-into-darkness`; `L/creature/zombies` |
| Area 4-3 – Chamber Of Enlightment; Book of Dark Winter | 27–28 | `L/scene/chamber-of-enlightenment`; `L/location/orkonov-4-3-chamber-of-enlightenment`; `L/tome/book-of-dark-winter`; `L/item/churin-business-card` |
| Area 4-4 – The Moon Chamber; Moon-Beast | 28–29 | `L/scene/moon-chamber`; `L/location/orkonov-4-4-moon-chamber`; `L/item/silver-moon-medallion`, `domination-serum`; `L/creature/moon-beast` |
| Wrapping Up Scene 4 | 29 | `L/scene/moon-chamber` |
| Scene 5 – The Mariinsky Theatre; Scene Summary | 29 | `L/scene/swan-lake`; `L/location/mariinsky-theatre`; `L/map/mariinsky-theatre` |
| Area 5-1 – Swan Lake, The Bloody Version; Staff – Mystic Focus; 4 Mad Cultists | 29–30 | `L/scene/swan-lake`; `L/location/theatre-5-1-auditorium`; `L/item/mystic-focus-staff`; `L/character/mad-cultists` |
| Area 5-2 – The Dressing Rooms | 30–31 | `L/scene/dressing-rooms`; `L/location/theatre-5-2-dressing-rooms`; `L/item/elena-locker` |
| Area 5-3 – Boris Churin’s Office; Boris Churin (статблок) | 31–32 | `L/scene/churin-office`; `L/location/theatre-5-3-churin-office`; `L/character/boris-churin` |
| Wrapping Up Scene 5 | 32 | `L/scene/churin-office` |
| Scene 6 – The Frozen Temple Of The Khanate; Getting to the Temple | 32–33 | `L/scene/road-to-temple`; `L/location/leningrad-environs`, `frozen-temple`; `L/map/frozen-temple` |
| Врезка «Sometimes You Want Something Quieter» | 32 | сценарий (таблица «Более спокойные финалы»); `L/scene/road-to-temple` |
| Scene Summary; Area 6-1 – The Ruins Of The Frozen Temple; The Summoning | 33–34 | `L/scene/frozen-temple-ritual`; `L/location/frozen-temple` |
| The Last Battle | 34 | `L/scene/last-battle` |
| Ithaqua; Up to 3 Gnoph-Keh; Elena Orkonov; 2 Yeti Servants | 34–35 | `L/creature/ithaqua`, `gnoph-kehs`, `yeti`; `L/character/elena-orkonova` |
| Conclusion | 35 | `L/scene/finale`; сценарий (conclusion) |
| Appendix I: Pregenerated Characters & A Note On Skills | 35 | сценарий (advice) |
| Reginald Masters | 36 | `L/character/reginald-masters` |
| Leon Sterndale | 37 | `L/character/leon-sterndale` |
| Mycroft Booth | 38 | `L/character/mycroft-booth` |
| Colleen Palmer | 39 | `L/character/colleen-palmer` |
| Albion Fitzgerald | 40 | `L/character/albion-fitzgerald` |
| Appendix II: Player Handouts A, B | 41 | `L/handout/handout-a-arkham-advertiser`, `handout-b-kamzanov-telegram` |
| Player Handouts C, D | 42 | `L/handout/handout-c-police-notes`, `handout-d-one-happy-family` |
| Player Handouts E, F | 43 | `L/handout/handout-e-they-live`, `handout-f-temple-map` |
| Player Handouts G, H | 44 | `L/handout/handout-g-mikhail-note`, `handout-h-parchment` |
| Appendix III: Maps (Orkonov Estate, Revolution Hospital) | 45 | `L/map/orkonov-estate`, `L/map/revolution-hospital` |
| Maps (State Museum, Return to the Orkonov Estate) | 46 | `L/map/state-museum`, `L/map/orkonov-catacombs` |
| Maps (Mariinsky Theatre, Frozen Temple of the Khanate) | 47 | `L/map/mariinsky-theatre`, `L/map/frozen-temple` |
| Задняя обложка | 48 | сценарий (sources) |

## Не взято

- Статблоки 7e — не созданы: оригинал 5-й редакции (Р-221); все числа сохранены текстом как напечатаны.
- Картинки раздаток A–H, портреты готовых сыщиков и иллюстрации книги — в `app/art/` не добавлены: эта папка не
  принадлежит части (нужен `pipeline/art/add_images.py`); текст раздаток перенесён полностью, рисунки D и E описаны.
- Йозеф Гутман (раздатка A), настоящий врач «доктор Третьяк», убитые в музее культисты, настоящие санитары, монгольский
  воин и казак (скелеты) — без отдельных записей: упомянуты мимоходом, сведения — в текстах раздатки, мест и сцен.
- Картины «Этюд в багровых тонах» и «Дама в терниях» и ранняя картина в спальне хозяев — без записей: без механики,
  упомянуты в персонаже Шарлотты и в месте 1-8.
- Подписи карт «5 feet / 10 feet», «N» (роза ветров) и названия карт — не метки (масштаб и заголовки).
- Выходные данные (авторы, художники, тестировщики) и реклама серии на задней обложке — не перенесены (не игровой
  материал).

## Кандидаты в новые общие записи

- `coc:creature:moon-beast` — общего лунного зверя нет (есть только профиль «Ящика Пандоры»); профиль сценария без
  `instance_of`.
- Йети — общей записи нет; профиль `L/creature/yeti` заведён в книге.
- Заклинания: Contact Ithaqua (Связь с божеством: Итакуа) — ссылки сейчас на семейство `coc:spell:contact-deity`;
  Enchant Spear (Зачаровать копьё) — сейчас без ссылки в тексте лунного зверя.

## Опечатки и сомнения книги

- Медальон: по проверке Истории — IX век (с. 9), во врезке — VII век (с. 10).
- Дата службы: раздатка A — воскресенье 21 ноября, раздатка B — 7 ноября.
- ПЗ не сходятся с (ВЫН + ТЕЛ)/2 5-й редакции: Катерина 13 (≈11), лунный зверь 14 (17), зомби 14 (15), питоны 15 (16),
  безумные культисты 14 (13), Борис 14 (13); Альбион — Удача 75% при МОЩ 14 (70%); Коллин — «Archaelogy 6 %».
- Дубинка Петра Дацюка — 1d10 + БкУ (у культистов та же дубинка 1d4 + БкУ).
- В кабинете Владимира тубус «охотно покажет Юрий» — вероятно, вместо Владимира (с. 22).
- «Chamber Of Enlightment» — опечатка заголовка (с. 28).
