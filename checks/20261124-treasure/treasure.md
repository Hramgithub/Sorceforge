# Treasure for the Watcher — сверка переноса (часть «treasure»)

Книга `treasure-for-the-watcher-en` (Paul Owen, Miskatonic Repository, 2021; Down Darker Trails, Дикий Запад 1870-х), 14 страниц PDF,
плюс папка книги: `Maps\` (4 JPG) и `Прегены\` (6 PDF-листов без текстового слоя). Русского перевода сценария в базе нет
(поиск по именам и местам в `kb/books/*-ru/` — пусто).

Страницы: печатная = физической (смещение 0); обложка (физ. 1) без номера, на физ. 2 напечатано «2».
Все записи — `kb/books/treasure-for-the-watcher-en/` (109): сценарий 1, сцены 17, персонажи 27 (из них прегены 6), существа 5,
места 31, карты 4, предметы 17, раздатка 4, организации 2, книга Мифов 1. Картинки — 13 (`art.json`, применены), атмосфера — 3 (`atmosphere.json`).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка | 1 | `scenario/treasure-for-the-watcher` (sources); картинка — `atmosphere.json` |
| Титул, выходные данные, тестировщики | 2 | `scenario/treasure-for-the-watcher` (sources); фон — `atmosphere.json` |
| Introduction | 3 | `scenario/treasure-for-the-watcher`: summary, advice («Место действия», Поэтон) |
| Background | 3 | `scenario/treasure-for-the-watcher`: keeper_info; `creature/the-watcher`; `character/raymond-gilman` |
| The Investigators | 3 | `scenario/treasure-for-the-watcher`: hook, advice; прегены — 6 записей `character/*` (role pregen) |
| Dramatis Personae: Hector Pemberton | 3 | `character/hector-pemberton` |
| Dramatis Personae: Raymond Gilman (+портрет) | 3 | `character/raymond-gilman` (портрет) |
| Dramatis Personae: John Sampson (+портрет) | 3–4 | `character/john-sampson` (портрет) |
| Chief Standing Buffalo | 4 | `character/chief-standing-buffalo` |
| Garretsburg (+карта) | 4 | `location/garretsburg`; `map/garretsburg` |
| Important Buildings 1. Golden Mountain Saloon | 4 | `location/garretsburg-1-golden-mountain-saloon`; `character/doug-mcadam` |
| 2. Doctor’s Surgery | 4 | `location/garretsburg-2-doctors-surgery` |
| 3. Midwestern Bank & Assay Office | 4 | `location/garretsburg-3-midwestern-bank`; `character/jackson-ferris` |
| 4. Mount Gold Baptist Church | 4 | `location/garretsburg-4-mount-gold-baptist-church` |
| Схема погони (картинка) | 5 | `scenario/…` таблица «Карта погони»; картинка у `scene/chase` |
| 5. The Blacksmith’s Forge | 5 | `location/garretsburg-5-blacksmiths-forge` |
| 6. Sheriff’s Office and Jail | 5 | `location/garretsburg-6-sheriffs-office` |
| 7. Mayor’s Mansion | 5 | `location/garretsburg-7-mayors-mansion`; `character/jayne-greig` |
| The Robbery | 5 | `scene/robbery` |
| Chase | 5 | `scene/chase`; `creature/horse` |
| Wounded | 5 | `scene/wounded`; `character/hettie-jarrod` |
| Midwestern Bank | 5 | `scene/bank`; `character/fred-solomon`; `item/stolen-gold-and-silver` |
| Карта Devil’s Lake Region | 6 | `map/devils-lake-region`; `location/devils-lake-region` и места на карте |
| Dead Man Riding | 6 | `scene/dead-man-riding`; `character/kevin-lewis`, `character/john-henry` |
| Lakefront | 6–7 | `location/lakefront`; `scene/lakefront`; `item/lakefront-spears-and-arrows`, `item/lakefront-ledger`; `handout/lakefront-diary`, `handout/lakefront-note` |
| Dreams | 7 | `scene/dreams`; `creature/the-watcher` (способность «Сны») |
| The Carters | 7 | `scene/carters` |
| Sioux Reservation | 7 | `location/sioux-reservation`; `scene/sioux-reservation`; `character/sioux-braves`; `organization/sioux` |
| Devil’s Lake | 7–8 | `location/devils-lake-settlement`; `scene/devils-lake-arrival`; `location/devils-lake` (озеро) |
| History | 8 | `location/devils-lake-settlement` (history); `scene/devils-lake-arrival` |
| Карта Devil’s Lake | 8 | `map/devils-lake` |
| Important Buildings 1. Sheriff’s Office and Jail | 8 | `location/devils-lake-1-sheriffs-office` |
| 2. The Lake Inn, Saloon | 8 | `location/devils-lake-2-lake-inn`; `character/fredrick-cole` |
| 3. Community Building and Church | 8–9 | `location/devils-lake-3-church`; `scene/church`; `character/colin-barton`; `organization/esoteric-order-of-dagon-devils-lake`; `item/church-gold-figurine`, `item/church-altar-book`, `item/church-trident` |
| 4. Stables and Carters | 9 | `location/devils-lake-4-stables`; `character/amos-wilkes` |
| 5. Blacksmith | 9 | `location/devils-lake-5-blacksmith`; `character/seth-greaves`; `item/casting-molds`; `handout/forge-note` |
| 6. Fish Processing Warehouse | 9 | `location/devils-lake-6-fish-warehouse`, `location/devils-lake-warehouse-cave`; `scene/fish-warehouse`; `character/kidnapped-children` |
| 7. Raymond Gilman’s House (пункты 1–5) | 9–10 | `location/devils-lake-7-raymond-gilman-house`, `location/devils-lake-gilman-caves`; `scene/raymond-gilman-house`; предметы `gilman-wife-portraits`, `cave-gold-idol`, `innsmouth-painting`, `gilman-ledgers`, `gilman-notebook`, `regional-map-red-pin`; `handout/note-to-thomas-gilman` |
| Врезка Civilizations of the Sea | 9 | `tome/civilizations-of-the-sea` |
| 8. Thomas Gilman’s House | 10 | `location/devils-lake-8-thomas-gilman-house`; `character/thomas-gilman`, `character/marcia-gilman` |
| The Devils Ride Out | 10 | `scene/devils-ride-out` |
| Keeper’s Option | 10 | `scene/escaped-child` |
| Quarrytown | 10–11 | `location/quarrytown`, `location/quarrytown-dynamite-shed`; `scene/quarrytown`; `character/vernon-tasker`, `character/gary-baker`; `item/quarry-dynamite`; `location/oberon` |
| Рисунок паровоза | 10 | картинка у `item/gold-train` |
| Портрет бородатого мужчины без подписи | 10 | `atmosphere.json` (кого изображает — неизвестно, вопрос владельцу) |
| Wellsburg Gorge | 11 | `location/wellsburg-gorge`, `location/wellsburg`; `scene/wellsburg-gorge`; `item/gold-train`; рисунки динамита и моста — у `item/quarry-dynamite` и `location/wellsburg-gorge` |
| Карта Wellsburg Gorge | 12 | `map/wellsburg-gorge` |
| The End | 12 | `scenario/…` conclusion, шаг «Развязка» |
| Rewards and Penalties | 12 | `scenario/…` conclusion |
| Appendices (10 секретов) | 12 | `scenario/…` таблица «Секреты сценария»; `item/fossilised-pearl`, `location/grand-forks` |
| Characters and Monsters: Raymond Gilman | 13 | `character/raymond-gilman` (статблок) |
| Horse | 13 | `creature/horse` |
| Average Deep One (+рисунок) | 13 | `creature/deep-ones` (рисунок) |
| Average Deep One Hybrid | 13 | `creature/deep-one-hybrids` |
| Deep One Gang | 14 | `creature/deep-one-gang` (варианты 1–6) |
| Прегены: US Marshall, Cowboy, Doctor, Lawyer, Preacher, Scout | отдельные PDF | `character/herbert-dowle`, `dylan-james`, `betty-julia-bone`, `marian-harlowe`, `marlon-mccain`, `chatan` (портреты) |
| Maps\*.jpg | — | картинки карт `app/maps/treasure-*.jpg` (ужаты до 1600 px) |

Подписи карты округи без текста в книге: Maddock → `location/maddock`; Northern Pacific RR → `location/northern-pacific-railroad`;
Grand Forks → `location/grand-forks`; Sioux → `location/sioux-reservation`.

## Не взято

- Логотип Miskatonic Repository, фон страниц (Nymgyu), список тестировщиков — оформление; авторы и копирайт — в sources сценария.
- Безымянные люди без записей (описаны текстом в местах и сценах): шериф Гаррецбурга и два его помощника, врач и кузнец
  Гаррецбурга, служанка и горничные Гилмана, слуги Томаса, два убитых возчика, рабочие и вооружённые люди Кворритауна,
  экипаж поезда (3 машиниста, 2 охранника), мэр Гранд-Форкса, глубоководная в пещере, похожая на жену Гилмана.
- Маленькая лавка на главной улице Девилс-Лейка, брод к юго-востоку от Лейкфронта и брод у Уэллсбурга — без своих записей, текстом.
- Листы прегенов: столбец «Insane» у Рассудка (= Рассудок / 5), «Quick Reference Rules» и пустая 3-я страница — общие
  правила листа, не данные сценария.
- Карты внутри PDF (с. 4, 6, 8, 12) — те же, что JPG папки `Maps`; картинки карт взяты из JPG.

## Опечатки и сомнения

- С. 3, «The Investigators»: после «They are:» список готовых сыщиков не напечатан — взяты листы папки «Прегены» (`errata` сценария).
- С. 12, секрет 10: «Mayor of Grand Forest», на карте — «Grand Forks» (`errata` сценария; один город — вывод из текста).
- С. 13, гибрид: Уклонение «30%(12/5)» — доли от 25%; исправлено на 30% (15/6) по Р-77 (`errata`, fixed).
- С. 14, глубоководный 3: БкУ «1d4» без плюса — молча «+1d4» (Р-39); ПЗ 14 при ВЫН 60 / ТЕЛ 75 — округление вверх (Р-161).
- С. 13, лошадь: ПЗ не напечатаны — 19 выведено (Р-41, `corrections`); «..130», «..50» — лишние точки опущены.
- С. 5: на коней вскакивают пятеро бандитов, Пембертон говорит о четверых в банке, в банде шестеро (с. 8, 14) — не согласовано (пометка в сцене).
- С. 9: список заклинаний «Civilizations of the Sea» кончается запятой — возможно, обрезан.
- Прегены: у Ковбоя, Врача, Юриста и Проповедника графа навыка «Brawl» пуста — взят базовый 25% (Р-41, `corrections`);
  у Проповедника место рождения «Providence, MA» (как напечатано); Уклонение Юриста 52% и Ковбоя 50% выше половины ЛВК — так на листах.
- С. 13: «Average Deep One» без брони, а банда (с. 14) — броня 1; профили разные, оба как напечатаны.

## Технический долг для ведущего

- Листы прегенов не записаны в `pipeline/source/books.json`: источник записей прегенов — `treasure-for-the-watcher-en`
  с `physical_page: null` и именем файла в `note`. Если ведущий запишет листы отдельными книгами (например,
  `treasure-for-the-watcher-pregens-en`), источники шести прегенов нужно переписать.
- Смещение страниц книги — 0 (печатная = физической).

## Термины (English → русский)

| English | Русский |
|---|---|
| Treasure for the Watcher | Сокровище для Стража |
| The Watcher | Страж |
| The Giver in the Lake / The Giver of the Lake | Даритель в озере / Даритель озера |
| Five Watchers | Пять Стражей (как в базе) |
| Star Spawn of Cthulhu | звёздное отродье Ктулху (как в базе) |
| Deep One / Deep One Hybrid | глубоководный / гибрид глубоководного (как в базе) |
| Deep One Gang | банда глубоководных |
| Esoteric Order of Dagon | Эзотерический орден Дагона (как в базе) |
| Civilizations of the Sea | «Цивилизации моря» |
| Arthur McInnes | Артур Макиннес |
| Garretsburg | Гаррецбург |
| Pawheton (Down Darker Trails) | Поэтон |
| Devil’s Lake (lake) | озеро Девилс-Лейк |
| Devil’s Lake (settlement) | Девилс-Лейк (посёлок) |
| Devil’s Lake Region | округа Девилс-Лейк |
| Lakefront | Лейкфронт |
| Sioux Reservation | резервация сиу |
| Sioux / braves | сиу / воины |
| Chief Standing Buffalo | вождь Стоящий Бизон |
| Quarrytown | Кворритаун |
| Schreiber Stone Quarry | каменоломня Шрайбера |
| Wellsburg / Wellsburg Gorge | Уэллсбург / ущелье Уэллсбург |
| Maddock / Oberon / Grand Forks | Мэддок / Оберон / Гранд-Форкс |
| Northern Pacific RR | Северная Тихоокеанская железная дорога |
| Midwestern Bank & Assay Office | банк «Мидвестерн» и пробирная контора |
| Golden Mountain Saloon | салун «Золотая гора» |
| Doctor’s Surgery | приёмная врача |
| Mount Gold Baptist Church | баптистская церковь «Маунт-Голд» |
| Mayor’s Mansion | особняк мэра |
| Sheriff’s Office and Jail | контора шерифа и тюрьма |
| The Lake Inn | салун «Лейк-инн» |
| Community Building and Church | общинный дом и церковь |
| Stables and Carters | конюшня и извоз |
| Fish Processing Warehouse | рыбоперерабатывающий склад |
| The Carters | возчики |
| Dead Man Riding | Мёртвый всадник |
| The Devils Ride Out | Банда выезжает |
| Keeper’s Option | вариант Хранителя |
| effigies | изваяния |
| Inbreeds | выродки |
| the look | «тот самый облик» |
| US Marshal(l) / deputies | маршал США / помощники |
| Preacher / Scout / Cowboy / Lawyer / Doctor | проповедник / разведчик / ковбой / юрист / врач |
| Rope Use / Trap / Gambling / Drive Wagon/Coach (навыки листа DDT) | Обращение с верёвкой / Ловушки / Азартные игры / Управление повозкой |
| Language (Deep One Speech) / (R’lyeh Glyphs) | Язык (речь глубоководных) / Язык (глифы Р’льеха) |
| Hard success / Bonus Die / Social Skill roll | трудный успех / бонусная кость / проверка социального навыка |
| Hector Pemberton, Raymond / Thomas / Marcia Gilman, John Sampson | Гектор Пембертон, Реймонд / Томас / Марша Гилман, Джон Сэмпсон |
| Doug McAdam, Jackson Ferris, Jayne Greig, Hettie Jarrod, Fred Solomon, John Henry, Kevin Lewis | Даг Макадам, Джексон Феррис, Джейн Грейг, Хетти Джаррод, Фред Соломон, Джон Генри, Кевин Льюис |
| Fredrick Cole, Colin Barton, Amos Wilkes, Seth Greaves, Vernon Tasker, Gary Baker | Фредрик Коул, Колин Бартон, Эймос Уилкс, Сет Гривз, Вернон Таскер, Гэри Бейкер |
| Herbert Dowle, Dylan James, Betty Julia Bone, Marian Harlowe, Marlon McCain, Chatan | Герберт Доул, Дилан Джеймс, Бетти Джулия Боун, Мэриан Харлоу, Марлон Маккейн, Чатан |
