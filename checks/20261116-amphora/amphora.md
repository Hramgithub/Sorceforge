# The Second Amphora (`second-amphora-en`) — сверка переноса

Enrique Camino, Entente Cthulhiana, Miskatonic Repository, 2019; наши дни (октябрь 2018), `axes.era` `modern`.
PDF — 32 страницы; печатная страница = физической (offset 0): «3» на физ. 3, «22» на физ. 22, «29» на физ. 29;
обложка (с. 1) и с. 2 без номера. Русского перевода в базе нет (проверено по `kb/books/*-ru/`: амфора, Кайшер, Гротон, Arabimpo).

Записей: 60 — сценарий 1, сцены 12, персонажи 13 (4 прегена, 5 NPC, 4 групповых профиля), существо 1, места 11,
карты 2, организация 1, предметы 7, раздатки 11, книга 1. Картинки: 12 (`app/art/*/amphora-*.webp`), карты —
`app/maps/amphora-house-floor-plan.jpg`, `app/maps/amphora-main-room-detail.jpg`; рамки вырезки — `amphora-boxes.json`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «The Second Amphora» | 1 | сценарий `second-amphora-en/scenario/second-amphora` (sources); картинка — atmosphere.json |
| Number of players 2-4 / 1-2 sessions / Modern Day | 2 | сценарий: summary |
| Выходные данные, «A note on gender», источники иллюстраций, фонд в Варшаве | 3 | сценарий: sources (note); раздатка `amphora-draft` (набатейская надпись) |
| Introduction / For the Keeper / What has happened until now | 4 | сценарий: keeper_info |
| Playing in another era or place | 4 | сценарий: advice |
| Playing with pre-gens or with your own PCs | 4 | сценарий: hook, advice; прегены (legend, sources) |
| The Second Amphora / Preamble | 5 | сцена `preamble` |
| врезка «The lloigor and the djinn» | 5 | сценарий: keeper_info; существо `djinn` (abilities, legend) |
| The Assault | 6–7 | сцена `the-assault`; места `baltimore`, `antiques-flat`; `swat-team`, `yusuf-mansour`; раздатка `amphora-draft`; предмет `locker-key` |
| Alone with the Amphora | 7 | сцена `alone-with-the-amphora`; предмет `heart-amphora` |
| The Locker | 7–8 | сцена `the-locker`; место `central-bus-station`; `cody-wells`, `station-arab-men`; раздатки `house-photograph`, `strange-diagram`, `dates-list`, `sticky-note`; предмет `groton-road-map` |
| Their Orders | 8 | сцена `orders-and-the-house` |
| About the House | 8 | сцена `orders-and-the-house`; раздатка `encrypted-email`; организация `arabimpo` |
| врезка «Managing the times» | 8 | сцена `orders-and-the-house`; сценарий: advice |
| First Vision | 9 | сцена `first-vision`; места `ruined-mosque`, `aden` |
| The House in the Woods | 10 | сцена `the-house-in-the-woods`; места `groton`, `house-in-the-woods` |
| врезка «Strange Event» (ящик с ножами) | 11 | сцена `the-house-in-the-woods` |
| Lower Floor / Upper Floor | 11 | место `house-in-the-woods`; сцена `the-house-in-the-woods` |
| Firewood Cellar | 11 | место `firewood-cellar` |
| The Main Room | 11–12 | место `main-room`; предмет `ashes-amphora` |
| врезка «Strange Event» (прибор бьёт отмеченного) | 12 | сцена `the-house-in-the-woods` |
| The Library | 12, 14–15 | сцена `the-library`; место `house-library`; раздатки `engraving-daemons`, `engraving-beast`, `engraving-old-man`; предметы `amber-dagger`, `library-computer`, `ritual-dvds`; `ritual-participants`, `tariq-haddad` |
| План «Upper floor / Lower floor» | 13 | карта `house-floor-plan` (13 меток) |
| врезка о тени на второй записи | 16 | сцена `the-library`; предмет `ritual-dvds` |
| The Basement | 16 | сцена `the-basement`; место `ritual-basement`; книга `tome/demons` |
| Текст книги «Демоны» | 16–17 | раздатка `demons-book-page` |
| Second Vision | 18 | сцена `second-vision` |
| Схемы и подпись к ним | 19 | раздатка `sand-diagram`; `strange-diagram` |
| The Specialist | 20–21 | сцены `the-specialist`, `the-djinn`; `abdul-kaisher`, `abdul-companions`, `suleiman-al-hadrami` |
| врезка «Strange Event» (песчаная буря) | 20 | сцена `the-specialist` |
| Развязка; «Warsaw, December 8th, 2019» | 21 | сцена `the-djinn`; сценарий: conclusion |
| врезка «On the atmosphere» | 22 | сценарий: advice |
| The lloigor in human form / in beast form (reptile) | 22 | существо `djinn` (statblock, variants) |
| Gaming-aids / Disclaimer | 23 | раздатки (quality.notes) |
| Draft of the amphora | 23 | раздатка `amphora-draft` |
| Strange diagram and photograph of the house | 24 | раздатки `strange-diagram`, `house-photograph` |
| Engravings on the library’s walls | 25–26 | раздатки `engraving-beast`, `engraving-old-man`, `engraving-daemons` |
| Text describing the beginning of the ritual | 27–28 | раздатка `demons-book-page` |
| Main room - detail | 29 | карта `main-room-detail` |
| Pre-generated PCs | 30 | прегены (legend) |
| PC 1 – Archaeologist | 30 | `morgan-hale` |
| PC 2 – Antiquarian | 31 | `jordan-reese` |
| PC 3 – U.S. Customs and Border Protection (CBP) Agent | 31 | `taylor-brooks` |
| PC 4 – Private Security Agent | 32 | `casey-dawson` |

## Не взято

- Иллюстрации-атмосфера и копии раздаток в тексте глав (обложка, фон с. 9, виньетка с. 18, фото человека с чашей с. 19, копии схемы, гравюры и арабской страницы на с. 8, 14, 17, 19, фон с. 28) — `atmosphere.json` с причинами.
- Человек с газетой и уборщица на автовокзале — мелкая атмосфера без действия; остались текстом в сцене `the-locker` и в групповом профиле `station-arab-men`.
- NPC-путники во втором сне (если сыщиков меньше четырёх) — без описания, только замена недостающих сыщиков; текстом в сцене `second-vision`.
- Каменная поилка с силуэтами животных в квартире, видеокамера и глиняная чаша в подвале, порошок мудреца — без механики; текстом в местах и сценах.
- Офисы «Арабимпо» в Адене, Эр-Рияде и Балтиморе — только упомянуты; текстом в организации.
- Таблиц в книге нет; в сценарий добавлена наша сводка потерь Рассудка (помечено в quality.notes).

## Опечатки и сомнения

- с. 22: у облика зверя ПЗ «N/A» (по формуле 37) — `errata` у существа `djinn`, как напечатано.
- с. 22: Уклонение 26% (13/5) у обоих обликов при ЛВК 42 — как напечатано (заметка).
- с. 30–32: Скорость прегенов без возрастной поправки (PC 1, 42 года: 7) — приём книги (Р-161).
- с. 30: «Born in: Siracusa, NY» — испанское написание Сиракьюса; с. 31: «Norfolk, VI» (у Виргинии VA); с. 31: «Escopeta Cal. 12 shotgun» (испанское слово); с. 32: «dm» вместо «dmg» — в quality.notes прегенов.
- с. 16: арабское заглавие в текстовом слое разорвано; по изображению — «الشياطين».
- Наград Рассудка книга не даёт.

## Термины (English → Russian)

| English | Русский |
|---|---|
| The Second Amphora | «Вторая амфора» |
| amphora (first / second) | амфора (амфора с сердцем джинна / амфора с прахом джинна) |
| djinn | джинн |
| desert devil | демон пустыни |
| lloigor | ллойгор (как в базе) |
| the wise man | мудрец (имя придумано: Сулейман аль-Хадрами) |
| Master (обращение Абдула) | учитель |
| the specialist | специалист |
| Abdul Kaisher | Абдул Кайшер |
| officiant | ведущий обряда |
| travellers | путники |
| the chosen ones | избранные |
| the marked PC | отмеченный сыщик |
| Strange Event | Странное событие |
| censers (ashtrays) | курильницы (пепельницы) |
| the four elements | четыре стихии |
| luggage locker / cabinet 314 | камера хранения / ячейка 314 |
| central bus station | центральный автовокзал |
| SWAT team | бойцы спецназа (SWAT) |
| amber dagger | янтарный кинжал |
| First Vision / Second Vision | Первое видение / Второе видение |
| The House in the Woods | Дом в лесу |
| main room | главная комната |
| library | библиотека |
| basement | подвал (для обрядов) |
| firewood cellar | дровяной погреб |
| elevating platform | подъёмная платформа |
| Ceremony (calendar entry) | «Церемония» |
| Demons (book, الشياطين) | «Демоны» |
| Arabimpo, Inc. | «Арабимпо, Инк.» |
| Groton (Vermont) | Гротон (Вермонт) |
| Aden / Adan | Аден / Адан |
| Al Habilayn | Аль-Хабилайн |
| abandoned mosque / temple ruins | руины мечети / руины храма |
| Kevlar vest | кевларовый жилет |
| 9 mm. Automatic | 9-мм автоматический пистолет |
| Cal. 12 shotgun, semi-automatic | полуавтоматический дробовик 12-го калибра |
| CBP Agent | агент Службы таможенного и пограничного контроля США (CBP) |
| Private Security Agent | сотрудник частной охраны |
| Entente Cthulhiana | Entente Cthulhiana (не переводится) |
