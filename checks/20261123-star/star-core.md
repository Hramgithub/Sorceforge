# The Star on the Shore — часть core: сверка покрытия

Книга `star-on-the-shore-en` (Ben Burns, Dark Cult Games по лицензии Chaosium, 2017). Скан без текстового слоя: текст, числа, имена и
статблоки прочитаны по изображениям страниц. Печатная страница = физическая − 3 (с. 5 «Introduction» — физ. 8; с. 51 «Upper Tunnels» — физ. 54;
с. 74 «Player Aids» — физ. 77). Страницы части: с. 1–13 (физ. 4–16; и физ. 1–7 без номеров), 51–64 (физ. 54–67), 74–96 (физ. 77–99).
Русский текст — наш перевод (`translated`); имена мест и людей города согласованы с записями части town.

## Заголовок книги → запись

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул, плейтестеры, оглавление, эпиграф | физ. 1–7 (с. 1) | `scenario/the-star-on-the-shore` (sources); картинки — `atmosphere-core.json` |
| Introduction | 5 | `scenario/the-star-on-the-shore` (summary, hook, advice); `scene/star-the-case`; `character/timothy-jennings` |
| Prologue | 5–6 | `scene/star-prologue` |
| Keeper’s Secret | 6–10 | `scenario/the-star-on-the-shore` (keeper_info); `character/jim-rahn`, `character/sam-rahn`, `character/michael-thomas`; `item/small-statue`, `item/great-statue`; `creature/star-spawn`; `organization/rockport-cult` |
| The Case | 10–12 | `scene/star-the-case`; `character/timothy-jennings`; раздатки 1–4 |
| The Trip (Train, Car) | 12–13 | `scene/star-the-trip` |
| City of Rockport | 13, 16 | `scene/star-city-of-rockport`; предложение к `coc:location:rockport` (`proposals-core.json`) |
| Upper Tunnels | 51–53 | `location/upper-tunnels`, `location/upper-tunnels-t1` … `-t8`, `location/upper-tunnels-t7-t9-passage`; `scene/star-upper-tunnels` |
| T1 … T8 | 51–53 | `location/upper-tunnels-t1` … `upper-tunnels-t8` |
| Passageway from T7 to T9 | 53 | `location/upper-tunnels-t7-t9-passage`; `scene/star-crates-passage` |
| T9 – The Underground Chapel | 53–55 | `location/upper-tunnels-t9-underground-chapel`; `scene/star-underground-chapel` |
| Upper Tunnels Map | 52 | `map/upper-tunnels` (картинка `app/maps/star-core-upper-tunnels.jpg`) |
| Spells (Breath of the Deep, Grasp of Cthulhu — у Томаса) | 55 | `character/michael-thomas` (abilities, spells) |
| Roy Collins, Betty Jones, Joyce Walker; статблоки Deep Ones, Rev. Michael Thomas (Hybrid), Joyce Walker, Roy Collins | 55 | `character/roy-collins`, `character/betty-jones`, `character/joyce-walker`, `character/michael-thomas`, `creature/deep-ones` |
| Lower Tunnels | 56 | `location/lower-tunnels`; `item/gas-tanks`; `scene/star-lower-tunnels` |
| LT-1 … LT-4 | 56, 58 | `location/lower-tunnels-lt-1` … `lt-4`; `scene/star-star-spawn-lair` |
| Lower Tunnels Map | 57 | `map/lower-tunnels` (картинка `app/maps/star-core-lower-tunnels.jpg`) |
| Star Spawn (статблок) | 58 | `creature/star-spawn` |
| Reference Section / Notes on Running the Star on the Shore | 59 | `scenario/the-star-on-the-shore` (advice; таблица «Четыре группы горожан») |
| (время суток) | 60 | `scenario/…` (advice); `scene/star-city-of-rockport` (mechanics) |
| Events | 60 | `scenario/…` (таблица «События»); `scene/star-cult-attack`, `scene/star-star-spawn-rampage` |
| Dreams (Dream 1–3, дополнительные сны) | 61 | `scene/star-dream-1-lighthouses`, `scene/star-dream-2-web`, `scene/star-dream-3-help-me` |
| Cultist Summary / The Cultists | 62 | `organization/rockport-cult` (members); `scenario/…` (таблица «Культисты»); `character/generic-cultist` |
| Generic Cultist (статблок) | 62 | `character/generic-cultist` |
| Spells | 63 | `scenario/…` (таблица «Заклинания сценария»); ссылки на `coc:spell:grasp-of-cthulhu`, `breath-of-the-deep`, `contact-star-spawn-of-cthulhu`, `banishment-of-yde-etad` |
| Final Scenarios (Dynamite, Guns Blazing, Destroying the Statues, Casting Banishment of Yde Etad, Freezing…, Coolant, Harpoons; Harpoon, Harpoon Launcher) | 64 | `scene/star-final-scenarios`; `scenario/…` (conclusion); предложение к `coc:weapon:harpoon` |
| Player Aids: Handout #1 … #20 | 74–78 | `handout/handout-1-podium-inscription` … `handout/handout-20-red-symbol` (текст как напечатан + перевод, картинки) |
| Player Aids: Rockport Report (Issue 34) | 79 | `handout/rockport-report` |
| Maps: Keeper Map (копия) | 80 | карта части town `map/keeper-map-rockport` (с. 14–15) — не дублировалась |
| Maps: Player Map | 81 | `map/rockport-player-map` (картинка `app/maps/star-core-rockport-player-map.jpg`) |
| Maps: Congregational Church (Location 21), 224 School Street (Location 34), Police Station (Location 1) | 82 | планы части town `map/congregational-church-plan`, `map/224-school-street-plan`, `map/police-station-plan` (те же планы на с. 35, 47, 17) — не дублировались |
| Maps: Upper Tunnels, Lower Tunnels (для игроков) | 83 | `map/upper-tunnels`, `map/lower-tunnels` (источник с. 83 в sources) |
| Pre-Generated Characters (10 листов) | 84–93 | `character/alex-yellop`, `alexander-hawkey`, `alice-crow`, `bill-robertson`, `foralz-bowes`, `jamie-hancock`, `kaylin-poillucci`, `alester-bradley`, `lucas-vandergon`, `sven-berglowe` (портреты) |
| Reference Notes | 94 | `scenario/…` (sources, quality.notes: переводы фраз на языке Мифов) |
| Keeper’s Notes (пустая страница), задняя обложка | 95–96 | не взято (пусто); обложка — `atmosphere-core.json` |

## Не взято

- Пустые страницы физ. 2–3, 98 («Keeper’s Notes» — пустой бланк для заметок): содержания нет.
- Список плейтестеров (физ. 5) — не игровой материал; упомянут в sources сценария.
- Мелкий служебный текст бланка телеграммы (раздатка 4) — не читается на скане.
- Подписи улиц на карте игроков (Main Street, Granite Street, Railroad Street и др.) — меток не получили: записей улиц нет.
- Копии карты Хранителя и планов зданий в разделе «Maps» (с. 80, 82) — те же картинки, что у карт части town; отдельных записей не заведено, чтобы не было дублей.
- Атмосферные иллюстрации — в `atmosphere-core.json` (14 страниц), в т. ч. портрет «Officer Wild» (с. 13) — его должна взять запись части town `character/michael-wild`.

## Опечатки и сомнения книги (в errata записей)

- `character/timothy-jennings`: на с. 9 «Dr. Timothy Jennings of the Dark Wing Detectives», на с. 5 — сотрудник Музея изящных искусств.
- `location/upper-tunnels-t3`: «Bailey Bro’s Ships and Fishing» — такого заведения нет; по смыслу «Bradley Brothers Ships and Fishing» (место 28).
- `scene/star-lower-tunnels`: «retreat back to T-1» в LT-3 — по смыслу LT-1 (исправлено в тексте, `fixed: true`).
- `character/michael-thomas`: в статблоке «Breath of the Deep One», в тексте — «Breath of the Deep»; Скорость 8 при СИЛ 65 и ЛВК 60 > ТЕЛ 50 (по правилам 9).
- `character/joyce-walker`: СИЛ + ТЕЛ = 80 — БкУ −1 и Комплекция −1; напечатано None и 0.
- `creature/star-spawn`: ПЗ 78 при (ВЫН 130 + ТЕЛ 400)/10 = 53; БкУ 7d6 и Комплекция 8 при СИЛ + ТЕЛ = 640 (+8d6, 9); шанс атак не напечатан — вопрос владельцу (Р-36).
- `character/alex-yellop`: заголовок «ALEX YELLOP», в тексте трижды «Axel».
- `character/bill-robertson`: ПМ 13 при МОЩ 70 (14).
- `character/kaylin-poillucci`: Скорость 9 при СИЛ = ТЕЛ (по правилам 8).
- `handout/handout-17-buried-bronze-plaque`: в тексте места 6 шифр «Sr ght gbb qrrc, nag sbhaq bhe tbq.», на рисунке — «JR QHT GBB QRRC, NAQ SBHAQ BHE TBQ.» (верный ROT13 — вариант рисунка).
- `organization/rockport-cult`: Синди Альварес — в списке культистов, но в «Events» — среди тех, кто может помочь.
- Без errata (пометки в quality.notes): раздатка 10 — «in 1915» (OCR давал 1918, на скане 1915); газета — «президент Франклин Д. Рузвельт» в 1921 году (анахронизм книги); раздатка 9 — «Nymph» против «HMS Nymphe» в «Key to the Abyss»; раздатка 20 в тексте книги нигде не упомянута; координаты на постаменте названы «GPS coordinates».
- Расхождение с частью town: в описании Габриэля (место 14) в дневнике заклинание «Mass Charm», в разделе «Spells» — «Mass Suggestion»; Габриэль творит «Control Birds», которого нет в разделе «Spells».

## Термины этой книги (English → русский)

| English | Русский |
|---|---|
| The Star on the Shore | «Звезда на берегу» |
| Star Spawn | звёздное отродье (вид — «Звёздное отродье Ктулху») |
| Deep One / Deep One Hybrid | глубоководный / гибрид глубоководного |
| Keeper’s Secret | Тайна Хранителя |
| The Case / The Trip | Дело / Дорога в Рокпорт |
| Upper Tunnels / Lower Tunnels | Верхние туннели / Нижние туннели |
| chamber (T1–T8) | камера |
| The Underground Chapel | подземная часовня |
| small statue / great (main) statue | малая статуя Ктулху / большая статуя Ктулху |
| the bridge / rubber band (между мирами) | мост / резинка |
| summoning circles | круги призыва |
| Chapel of Contemplation | Часовня созерцания (по «Призраку») |
| Church of our Lord, Granter of Secrets (GoS) | Церковь Господа нашего, Дарующего тайны (по «Призраку») |
| The Cultists / Cultist Summary | Культ Ктулху в Рокпорте / культисты |
| Generic Cultist | Культист Рокпорта (типовой) |
| Events / Dreams / Final Scenarios | События / Сны / Как победить звёздное отродье |
| Summon Spirit Animal | Призыв духа-зверя (форма части town) |
| Mass Suggestion / Mass Charm | Массовое обаяние (форма части town; в книге путаница названий) |
| Shadow Protection | Защита тенями |
| Control Birds | Власть над птицами (форма части town) |
| Obscuring Shadows | Скрывающие тени (форма части town) |
| Contact Star Spawn | Связь со звёздным отродьем |
| Grasp of Cthulhu / Breath of the Deep / Banishment of Yde Etad | Хватка Ктулху / Дыхание глубин / Изгнание Йде Итад (общие записи) |
| Harpoon / Harpoon Launcher | гарпун / гарпунная пушка |
| coolant (portable coolants) | охладитель (переносные охладители) |
| Resistance roll vs STR 80 | проверка противоборства против СИЛ 80 |
| POW resistance | встречная проверка МОЩ |
| penalty die | штрафная кость |
| Rockport Report | «Рокпорт рипорт» |
| Museum of Fine Arts | Музей изящных искусств |
| Dark Wing Detectives | Dark Wing Detectives (не переводится) |
| Dark Young | тёмная молодь (общая запись) |
| Law Student / Private Eye / Gambler / Psychologist | студент-юрист / частный сыщик / азартный игрок / психолог |
| Maritime Mechanic / Freelance Researcher / Lounge Singer | судовой механик / вольный исследователь / певица в лаунж-баре |
| Professor/Hunter / Doctor / Vagrant | профессор и охотник / врач / бродяга |
| Ann’s Eyes (маяки острова Тэтчер) | «Глаза Энн» |
| minutemen | минитмены |

Имена мест и людей города — как в записях части town: Дом Вудса, Бэрскин-Нек, Красный сарай («Мотив № 1»), церковь Олд-Слуп,
Гранитная компания Рокпорта, Художественная ассоциация Рокпорта, Межштатная рыбная корпорация, Дом ведьмы, Рэйвен «Шэдоуз» Алексис,
Марджори «Вулф» Остин, Деандра Райт, Пекка Мюллюлуома, Театр Рокпорта, пристань Брэдли, «Суда и рыбалка братьев Брэдли».

Текст заклинаний книги (раздел «Spells», с. 63) лежит в `scenario/the-star-on-the-shore`, таблица «Заклинания сценария» (`tables[3]`), строки названы так же, как у части town; заклинания Томаса — в `character/michael-thomas` (abilities).

> Ведущий (2026-11-23): «Sr ght gbb qrrc…» у раздатки 17 — ошибка распознавания, на скане места 6 напечатан верный ROT13 «Jr qht gbb qrrc…»; errata снята. Портреты Уайлда и Гордана добавлены (art-lead.json).
