# «Кровные узы» («Двери во тьму», `dveri-vo-tmu-ru`) — сверка переноса (часть ties)

Источник — официальное русское издание «Двери во тьму» (скан без текстового слоя): страницы распознаны
`pdftoppm -r 200` + `tesseract -l rus`, каждое число сверено по изображению страницы или по английскому
оригиналу `doors-to-darkness-en` (Р-213, Р-216). Фанатский «Развеять мрак» не использовался.

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 5 «Кровные узы» (Том Линч), с приложением А | 76–95 | 75–94 |
| «Материалы для игроков»: «Узы 1» … «Узы 6» | 121–125 | 120–124 |
| «Готовые персонажи» (десять сыщиков сборника) | 126–135 | 125–134 |

Смещение `dveri-vo-tmu-ru`: печатная = физическая + 1 на всех страницах части (75→76, 81→82, 87→88, 93→94,
120→121, 124→125). Печатные страницы совпадают с английским оригиналом (печатная = физическая − 1).

## Заголовки книги

`…/` = `dveri-vo-tmu-ru/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 5. Кровные узы (Том Линч) | 76 | сценарий `…/scenario/ties-that-bind` (summary) |
| Введение | 76 | сценарий: summary; город `coc:location:ipswich` |
| Хранителю на заметку: время и темп (врезка) | 76 | сценарий: advice, keeper_info (ход событий); таблица «График Хаккета» |
| Информация для Хранителя | 76 | сценарий: keeper_info; `…/character/ties-thaddeus-waters`; `…/creature/ties-mother-byakhee`; `…/item/ties-byakhee-eggs`; `…/location/ties-fountain` |
| Вовлечение сыщиков | 76–77 | сценарий: hook; сцена `…/scene/ties-aftermath` (вход на месте убийства) |
| Карта 1. Стройка | 77 | карта `…/map/ties-map-1-construction-site` (`app/maps/dveri-ties-map-1.jpg`, 5 меток на подписи); места `ties-carrington-estate`, `ties-main-building`, `ties-garage-and-stables`, `ties-cellar`, `ties-rose-garden`, `ties-fountain` |
| Место вандализма | 77 | сцена `…/scene/ties-scene-of-vandalism`; `…/character/ties-enid-carrington` |
| Семейство Кэррингтонов (Энид, Милбёрн, Уильям, Мэри) | 77–78 | `…/character/ties-enid-carrington`, `ties-milburne-carrington`, `ties-william-carrington`, `ties-mary-carrington`; сцена `ties-scene-of-vandalism` |
| Фонтан | 78 | место `…/location/ties-fountain`; сцена `ties-scene-of-vandalism` |
| Камни | 78 | сцена `…/scene/ties-the-rocks`; предмет `…/item/ties-byakhee-eggs`; место `…/location/ties-cellar` |
| Дальнейшее изучение яиц | 78, 81 | сцена `ties-the-rocks`; `…/character/ties-foreman` |
| Материал «Узы 1» (в главе) | 80 | `…/handout/ties-1-hackett-letter` |
| Вмешательство полиции | 81 | сцена `…/scene/ties-police-involvement` |
| Куда, куда вы удалились? | 81 | сцена `…/scene/ties-where-hast-thou-gone`; `…/character/ties-alfred-hackett`; `…/location/ties-dorothy-upman-hall` |
| Материал «Узы 2» (в главе) | 81 | `…/handout/ties-2-hackett-note` |
| Развитие событий | 81–82 | сцена `…/scene/ties-developing-events`; `…/location/ties-borden-arms-hotel`, `ties-hackett-room`; `…/character/ties-pansy-osborne`, `ties-carl-briden` |
| Детёныш | 82 | сцена `…/scene/ties-the-hatchling`; существо `…/creature/ties-byakhee-hatchling` |
| График Хаккета (врезка с таблицей) | 82 | сценарий: таблица «График Хаккета» (7 строк) |
| Мама? Мама! | 82–83 | сцена `…/scene/ties-mama`; `…/creature/ties-mother-byakhee`; `…/character/ties-construction-workers` (гибель сторожей) |
| Совет Хранителю (абзац в тексте) | 83 | сцена `ties-mama` |
| Материал «Узы 3» (в главе) | 83 | `…/handout/ties-3-briden-notes` |
| Хранителю на заметку: добавить жути и загадочности (врезка) | 84 | сцена `ties-mama`; сценарий: advice |
| Последствия | 84 | сцена `…/scene/ties-aftermath`; `…/location/ties-arkham-sanitarium` |
| Место преступления: номер Хаккета (улики № 1–4) | 84 | сцена `…/scene/ties-crime-scene-room`; место `ties-hackett-room` |
| Сбивчивые показания | 84, 86 | сцена `…/scene/ties-fragmented-testimony` |
| Сведения Уилла Кэррингтона | 86 | сцена `…/scene/ties-will-carrington`; `…/location/ties-orne-library`, `ties-miskatonic-university` |
| Эндрю Леман | 86, 88 | сцена `…/scene/ties-andrew-leman`; `…/character/ties-andrew-leman`, `ties-sam-malowski`; `…/location/ties-kingsport-tenement` |
| Материал «Узы 4» (в главе) | 87 | `…/handout/ties-4-essex-folklore` |
| Карта 2. Болотный остров | 88 | карта `…/map/ties-map-2-marsh-island` (`app/maps/dveri-ties-map-2.jpg`, 16 меток: 4 подписи, 6 деревьев, 6 параменталей); места `ties-marsh-island`, `ties-central-clearing`, `ties-formula-trees`, `ties-bedroom-hut`, `ties-kitchen-hut`, `ties-workshop-hut` |
| Поход на соляные болота | 88–90 | сцены `…/scene/ties-salt-marshes` и `…/scene/ties-wizard-huts` (вторая — хижины, с. 90; название дано нами); места `ties-ipswich-environs`, `ties-salt-marshes`, `ties-marsh-island`; `…/creature/ties-wilderness-paramentals`; `…/item/ties-bone-whistle` |
| Хранителю на заметку: придать атмосферу поискам (врезка) | 89 | сцена `ties-salt-marshes`; место `ties-salt-marshes` (скелет 0/1d2) |
| Материал «Узы 5» (в главе) | 91 | `…/handout/ties-5-byakhee-spell` (связь с `coc:spell:summon-bind-byakhee`) |
| Хранителю на заметку: сотворить заклинание (врезка) | 92 | сцена `ties-wizard-huts`; сценарий: advice |
| Материалы «Узы 6» (в главе) | 92 | `…/handout/ties-6-wizard-notebook` |
| Место преступления: поместье Кэррингтонов | 92 | сцена `…/scene/ties-crime-scene-estate`; места `ties-carrington-estate`, `ties-cellar`, `ties-main-building` |
| Итоги | 92–93 | сцена `…/scene/ties-finale`; сценарий: conclusion |
| Хранителю на заметку: подмога для мамы (врезка) | 93 | сцена `ties-finale`; сценарий: advice; `ties-mother-byakhee` (legend) |
| Хранителю на заметку: как тут победить? (врезка) | 93 | сцена `ties-finale`; сценарий: advice |
| Успех сыщиков | 93 | сцена `ties-finale`; сценарий: conclusion |
| Провал сыщиков | 93 | сцена `ties-finale`; сценарий: conclusion |
| Награды | 93 | сценарий: conclusion (четыре награды Рассудка и сноска); шаг «Награды» |
| Приложение А: персонажи Хранителя и чудовища | 94 | — |
| Энид Кэррингтон, 51 год, железная леди | 94 | `…/character/ties-enid-carrington` (статблок) |
| Уильям Кэррингтон, 21 год, студент-оккультист | 94 | `…/character/ties-william-carrington` (статблок) |
| Эндрю Леман, 43 года, жертва насмешек | 94 | `…/character/ties-andrew-leman` (статблок) |
| Типичный строитель | 94 | `…/character/ties-construction-workers` (групповой профиль, 6 имён, Р-151) |
| Лесные параментали | 95 | `…/creature/ties-wilderness-paramentals` (статблок) |
| Самка бьякхи, встревоженная мать | 95 | `…/creature/ties-mother-byakhee` (`instance_of` `coc:creature:byakhee`) |
| Материалы для игроков: «Узы 1» | 121 | `…/handout/ties-1-hackett-letter` (источник текста) |
| «Узы 2», «Узы 3» | 122 | `…/handout/ties-2-hackett-note`, `…/handout/ties-3-briden-notes` |
| «Узы 4» | 123 | `…/handout/ties-4-essex-folklore` |
| «Узы 5» | 124 | `…/handout/ties-5-byakhee-spell` |
| «Узы 6» | 125 | `…/handout/ties-6-wizard-notebook` («Чернота 1» на той же странице — часть black) |
| Готовые персонажи (десять сыщиков) | 126–135 | существующие записи `…/character/<slug>`; в ссылках сценария (не дублировались) |

Город — новая общая запись `kb/locations/ipswich.json` (Р-190); поместье Кэррингтонов — `part_of` Ипсвич (вывод из
текста), болота и остров — в области «Окрестности Ипсвича» (Р-209). Места в Аркхэме (отель, психбольница,
Мискатоникский университет) и Кингспорте (доходный дом Лемана) — книжные записи с `part_of` на общие города.

## Записи (64)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `ties-that-bind` |
| scene | 16 | `ties-scene-of-vandalism`, `-the-rocks`, `-police-involvement`, `-where-hast-thou-gone`, `-developing-events`, `-the-hatchling`, `-mama`, `-aftermath`, `-crime-scene-room`, `-fragmented-testimony`, `-will-carrington`, `-andrew-leman`, `-salt-marshes`, `-wizard-huts`, `-crime-scene-estate`, `-finale` |
| location | 22 | общий город `coc:location:ipswich`; книги: `ties-carrington-estate`, `-main-building`, `-garage-and-stables`, `-cellar`, `-rose-garden`, `-fountain`, `-borden-arms-hotel`, `-hackett-room`, `-arkham-sanitarium`, `-miskatonic-university`, `-dorothy-upman-hall`, `-orne-library`, `-kingsport-tenement`, `-ipswich-environs`, `-salt-marshes`, `-marsh-island`, `-central-clearing`, `-formula-trees`, `-bedroom-hut`, `-kitchen-hut`, `-workshop-hut` |
| map | 2 | `ties-map-1-construction-site`, `ties-map-2-marsh-island` |
| character | 12 | статблоки: `ties-enid-carrington`, `-william-carrington`, `-andrew-leman`, `-construction-workers`; без статблока: `-milburne-carrington`, `-mary-carrington`, `-alfred-hackett`, `-carl-briden`, `-pansy-osborne`, `-foreman` (имя придумано, Р-150), `-sam-malowski`, `-thaddeus-waters` |
| creature | 3 | `ties-mother-byakhee`, `ties-byakhee-hatchling`, `ties-wilderness-paramentals` |
| item | 2 | `ties-byakhee-eggs`, `ties-bone-whistle` |
| handout | 6 | `ties-1-hackett-letter`, `-2-hackett-note`, `-3-briden-notes`, `-4-essex-folklore`, `-5-byakhee-spell`, `-6-wizard-notebook` |
| organization | 0 | организаций в сценарии нет (полиция Ипсвича и Аркхэма, шериф округа Эссекс — только упомянуты) |

Картинки карт: `app/maps/dveri-ties-map-1.jpg` (884×1028), `app/maps/dveri-ties-map-2.jpg` (830×938) — вырезки по рамке
со страниц 200 dpi; метки проверены глазами на вырезке с нанесёнными кружками.

## Расхождения изданий и опечатки

- Лесные параментали: потеря Рассудка в тексте сцены — 1/1d6 (с. 88), в статблоке — 0/1d8 (с. 95); так и в оригинале.
  `errata` у существа; в сцене — значение текста.
- Лесные параментали: СИЛ 35 + ТЕЛ 35 = 70 → БкУ −1, Комплекция −1; напечатано 0 и 0 (так и в оригинале). `errata`,
  оставлено как напечатано (Р-36 — без большинства).
- Самка бьякхи: урон «Ближнего боя» напечатан «1d6» без БкУ (оригинал так же), у общего профиля — 1d6 + БкУ;
  `adds_db: false` как напечатано, пометка в `quality.notes`. Шанс манёвра «Укус и захват» отдельно не напечатан.
- Русское издание: в «Информации для Хранителя» (с. 76) находки убирают «в запертый сарай», дальше везде — погреб.
- Меры: сколы бортика фонтана «примерно в полуметре друг от друга» (оригинал — about four feet, ≈1,2 м); вода
  «по щиколотку» (calf-deep); прочие переводы футов и миль в метры сходятся (6 м, 3,5 м, 3 м, 2 м, менее 10 км).
- Уильям: в русском тексте с. 86 — «старший брат» Мэри, в оригинале — «the middle child».
- Материал «Узы 6»: первая фраза в русском издании — «Тварь можно изгнать и без выполнения задания. Это необязательно»,
  в оригинале — «Creature does not always complete task. Sometimes not necessary».
- Опечатка оригинала в сноске к наградам («Dr. Biden, Hawkins») в русском издании исправлена («доктор Брайден,
  Хаккет») — не записывалась (Р-39).
- В оригинале параментали сравниваются с параменталями из «Secrets of San Francisco» (с. 89); в русском издании
  отсылки нет.

## Не взято

- Иллюстрации (с. 79 — «Камни», Пэт Лобойко; с. 85 — «Номер Хаккета», Джонатан Вайк; с. 89 — «Поход на соляные болота»,
  Джонатан Вайк; с. 90 — «Болотный колдун», Джонатан Вайк; с. 94 — «Бьякхи», Пэт Лобойко) и картинки раздаток (рисунок
  детёныша в «Узы 3», иллюстрация в «Узы 4»): картинки в записи не добавлялись (поле `images` необязательно; можно
  добавить позже `pipeline/art/add_images.py`).
- Полиция Ипсвича, полиция Аркхэма, шериф округа Эссекс и их начальник, декан Колледжа естествознания, отделение
  геологии, биологическое отделение, коллега доктора Брайдена, Гарвард — только упомянуты: текстом в сценарии,
  сценах и местах, записей нет.
- Кобыла Лемана, итальянская статуя, стальная дверь (18 пунктов здоровья), строительные леса — текстом в сценах и
  местах (не отдельные записи).
- Костяной кинжал из материала «Узы 5» в сценарии не встречается — только текст раздатки.
- Способ изгнания бьякхи из «Узы 6» — без механики в книге: только текст раздатки, записи заклинания нет.
- Значки легенды под Картой 2 (образцы «дерева» и «П») метками не отмечены — это ключ, а не место.

## Кандидаты в общие записи

- Мискатоникский университет (с библиотекой Орна и общежитием имени Дороти Апмен) и Аркхэмская психбольница заведены
  книжными записями `ties-*` с `part_of` на Аркхэм: при появлении в других книгах — переезд в общие (Р-154); схема id
  мест Аркхэма — открытый вопрос владельца.

## Предложения

`proposals-ties.json` — 10 предложений: Аркхэму — абзац описания о «Кровных узах», ссылки на сценарий и Ипсвич,
источник книги; Кингспорту — абзац о Лемане, ссылки на сценарий и доходный дом, эпоха 1920-е, источник книги;
дороге в Ипсвич из «Побега из Иннсмута» — ссылка на город. Пробный прогон `pipeline/integrate/apply.py --dry-run`:
10 правок ложатся (3 записи).
