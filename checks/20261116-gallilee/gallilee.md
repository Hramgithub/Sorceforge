# «Galilee Springs» (`gallilee-springs-en`) — сверка полноты (Р-134, Р-251)

Часть `gallilee`, вся книга. В PDF 8 страниц (кэш текста даёт 9-ю пустую — `pdftoppm` её не знает). На с. 3–8 напечатаны
номера 2–7 (печатная = физическая − 1), на с. 1–2 номеров нет; в `pipeline/source/books.json` у книги нет `offset`
(должно быть `-1`; файл не правился — вопрос ведущему). Источник — английский оригинал; русский текст — наш перевод
(флаг `translated`). Записи — `kb/books/gallilee-springs-en/` (34): сценарий 1, сцены 10, персонажи 6 (3 сыщика-`pregen`
без статблоков, Мэри, 2 групповых профиля), существа 3, организации 2, предметы 5, раздатка 1, места 6.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Galilee Springs», Sean Liddle | 1 | `scenario/galilee-springs` (sources); картинка — `atmosphere.json` |
| Introduction or «How to use this mini-scenario» | 2 | `scenario.advice` («Как пользоваться мини-сценарием») |
| How to Use This (10 пунктов) | 2 | `scenario.advice` — пункты «•» |
| Galilee Springs | 3 | `scenario`, `location/galilee-springs` |
| Background: Year 1975; Location: Galilee Springs, California (Fictional) | 3 | `scenario.summary`; `location/galilee-springs`; `axes.era` `other` |
| Summary for Players | 3 | `handout/summary-for-players` (текст целиком, ru + en); `scenario.hook`; `scene/prologue-morning` |
| Background/Summary/Notes for the GM | 3 | `scenario.keeper_info`; `location/galilee-springs`, `galilee-springs-campground`; `organization/coordinators`, `mythos-protection-system`; `item/water-supply-drugs`, `wild-mushroom-spores` |
| Albert Ramirez / Michael Gonzales | 4 | `character/albert-ramirez` (`legend`, `background.secret`); `creature/hatteras-deep-one`; `item/mary-dream-journal` |
| Jeffrey Gacy / Travis Adams | 4 | `character/jeffrey-gacy`; `creature/empty-rabbit-costume` |
| Jack Kroll / James Oster | 4 | `character/jack-kroll`; `creature/tree-spider` |
| (без заголовка) день игры: мойка, барбекю, микрофоны, воспоминания | 4 | `scenario.keeper_info` («День игры»); `scene/car-wash`, `scene/barbecue`; `character/mary-ramirez` |
| (без заголовка) разговор наедине, 15 минут | 4 | `scene/talking-in-secret` |
| (без заголовка) город меняется | 4–5 | `scene/town-revealed`; `location/galilee-springs`, `galilee-springs-high-school` |
| (без заголовка) объявление, толпа | 5 | `scene/announcement`; `character/galilee-springs-townsfolk` |
| (без заголовка) шоссе, пустыня, погоня, грузовик, ограда | 5 | `scene/desert-chase`; `location/galilee-springs-desert`; `item/camping-axes-and-shovels`, `military-truck-gear`; `character/coordinators-squad` |
| Timeline (вводные один на один) | 6 | `scenario.advice`, `scene/prologue-morning` |
| Prologue: Morning | 6 | `scene/prologue-morning` |
| Part 1: Car Wash | 6 | `scene/car-wash` (проверка Идеи, НОВЫЕ листы сыщиков) |
| Part 4: Flight | 6 | `scene/flight` (план города, Вождение автомобиля, проверки Рассудка каждые 3 хода); `location/galilee-springs-town-hall` |
| Part 5: The End | 7 | `scene/the-end`; `scenario.conclusion`; `scenario.advice` («Растянуть игру») |
| Epilogue | 7 | `scene/epilogue`; `location/dome-town`; `scenario.conclusion` |
| Послесловие (контакты, Anti-Photon Publishing, Summer 2019) | 8 | `scenario.summary` (издатель, год); остальное — «Не взято» |

Страницы в таблице — физические (страница PDF); печатная = физическая − 1. В списке опечаток ниже — печатные.

## Опечатки и расхождения книги

- Хронология: Prologue, Part 1, Part 4, Part 5, Epilogue — частей 2 и 3 нет (`scenario.errata`).
- Жена Альберта: Mary (с. 3) и Marie (с. 5) (`character/mary-ramirez.errata`).
- Вопрос жён об «Asclepius Portage»: на барбекю (с. 3) или в конце мойки (с. 5) — обе версии: сцены `car-wash` и `barbecue` (`errata`).
- Направления: кемпинг — на северо-запад (с. 2), на север (с. 4), на запад (с. 5); другие города — на юг (с. 4), на восток (с. 5) (`location/galilee-springs.errata`).
- Название: файл — «Gallilee Springs», обложка и текст — «Galilee Springs» (в `aliases`).
- Числа без значений: ни одного статблока и ни одной величины потери Рассудка (так задумано автором, вступление на физ. с. 2).

## Термины (English → Russian)

| English | Русский |
|---|---|
| Galilee Springs / Gallilee Springs | Галили-Спрингс |
| The Coordinators | Координаторы |
| a team of Coordinators / The Coordinators (6) | Отряд Координаторов |
| Town Council | городской совет |
| Mythos Protection System | Система защиты от Мифов |
| federal government department assigned to dealing with mythos events | федеральное ведомство по делам Мифов |
| Asclepius Portage | Переправа Асклепия |
| dream journal | дневник снов |
| wild mushroom spores | споры диких грибов |
| psychotropic drugs (in the water supply) | психотропные вещества (в водопроводе) |
| fund raising car wash | благотворительная мойка машин |
| camping / hunting / recreational area, campground | кемпинг |
| camping trip | поход |
| bowling alley | боулинг |
| community center | общественный центр |
| city hall / town hall | ратуша |
| air raid siren speakers | динамики сирен воздушной тревоги |
| hidden microphones / hidden speakers | скрытые микрофоны / скрытые громкоговорители |
| hard packed desert | плотно утрамбованная пустыня |
| electrical fencing … military grade barbed wire | электрическая ограда … армейская колючая проволока |
| geodesic dome | геодезический купол |
| re-education / brainwashing | перевоспитание / промывка мозгов |
| reintegrated into the Mythos Protection System | «реинтегрируются» в Систему защиты от Мифов |
| NEW character sheets | НОВЫЕ листы сыщиков |
| batons | дубинки |
| two way radio, walkie talkies | рация, портативные рации |
| deep one / fish like man | глубоководный / похожий на рыбу человек |
| very tall spider like creature (looks like a tree) | Паук-дерево (имя придумано) |
| person in a rabbit headed costume | Пустой кроличий костюм (имя придумано) |
| SAN roll / sanity check | проверка Рассудка |
| idea roll | проверка Идеи |
| drive skill / driving rolls | проверка Вождения автомобиля |
| GM | Хранитель |
| Albert Ramirez / Michael Gonzales | Альберт Рамирес / Майкл Гонсалес |
| Jeffrey Gacy / Travis Adams | Джеффри Гейси / Трэвис Адамс |
| Jack Kroll / James Oster | Джек Кролл / Джеймс Остер |
| Mary (Marie) | Мэри (Мари) |
| Sean Liddle | Шон Лиддл |

## Не взято

- Физ. с. 2, юридическая оговорка (товарный знак Chaosium, программа OBS Community Content, логотип Miskatonic Repository) — не игровой материал.
- Физ. с. 8, адрес электронной почты автора и «Hope you enjoy the scenario. More to come.» — не игровой материал (издатель и год — в `summary`).
- Две другие жены, дети, люди в зелёной форме, люди в костюмах и врачи, невидимый голос на гауптвахте, диктор объявления — без имён и без чисел; текстом в сценах и сценарии.
- Языческое шествие (сон Джеффри) — текстом у персонажа и существа; записи `organization` не заведено (книга ничего о нём не говорит).
- Нечеловеческие существа под куполом — текстом в `location/dome-town` (книга их не называет).
- Боулинг, общественный центр, продуктовый магазин, кафе, фабрика, гаражи, медицинское учреждение — только упоминания; текстом в записи города и сценах.
- Городской совет (Town Council) — текстом у Координаторов и города; отдельной организации нет.
- Мыс Хаттерас — ссылка на общую запись `coc:location:hatteras` в `refs` сценария (это деревня на мысе; правки общей записи не предлагались).

## Картинки

- Единственная картинка — обложка (физ. с. 1, фото грибов): атмосфера (`atmosphere.json`). Вопрос владельцу: отдать ли её
  предмету «Споры диких грибов» — книга снимок с ним прямо не связывает.

## Проверки

- `python tools/check.py kb/books/gallilee-springs-en` — ошибок 0, предупреждений 0.
- `tools/completeness.py` (`completeness/`) — 1 находка: картинка обложки (физ. с. 1) → в `atmosphere.json`.
- `tools/scenario_check.py` (`scenario/`) — 0 находок.
