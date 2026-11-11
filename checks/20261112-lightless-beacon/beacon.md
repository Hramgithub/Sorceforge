# «Погасший маяк» — сверка заголовков (часть beacon, Р-215)

Книга `lightless-beacon-ru` (официальное русское издание, 44 физические страницы, текстовый слой). Страницы ниже —
печатные; **физическая = печатная + 1** (обложка — физ. 1, без номера; «9» в колонтитуле стоит на физ. 10). Английский
оригинал записан как `lightless-beacon-en` с тем же сдвигом. Официальная раздатка («Раздатка\[RU 7e] раздатка.pdf»,
6 листов) — распечатка с. 24–29 книги, поэтому источник раздаточных материалов — страницы книги.

Префиксы id: `lightless-beacon-ru/<вид>/beacon-…`; сценарий — `lightless-beacon-ru/scenario/lightless-beacon`;
общий город — `coc:location:rockport` (новый, Р-190).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул «Погасший маяк. Когда погасли огни», Ли Карр и Линн Харди | 1–2 | `scenario/lightless-beacon` (`name`, `aliases`, `summary`) |
| Титры | 3 | не взято (см. ниже) |
| Содержание | 4 | не взято (см. ниже) |
| Вступление | 5 | `scenario/lightless-beacon` — `summary` |
| Проведение игры | 5 | `scenario/lightless-beacon` — `advice` («Проведение игры») |
| Описание сценария | 6 | `scenario/lightless-beacon` — `summary`, `keeper_info` |
| Структура сценария | 6 | `scenario/lightless-beacon` — `advice` (пункты «•»), `steps` |
| О сыщиках | 6 | `scenario/lightless-beacon` — `advice` («О сыщиках»), `hook`; готовые сыщики `character/antique-dealer`, `bureau-agent`, `marine-biologist`, `artist` (уже в базе, не дублированы) |
| Торговец антиквариатом / Агент Бюро / Морской биолог / Художник (черты, роль в сценарии) | 6–7 | уже в записях прегенов (`background.traits`, `legend`); в `hook` сценария |
| Меньше четырёх игроков? | 7 | `scenario/lightless-beacon` — `advice` |
| Введение расходования Удачи (врезка) | 7 | `scenario/lightless-beacon` — `advice`; ссылка `coc:rule:spending-luck` |
| Дополнительные или альтернативные сыщики; полезные навыки | 8 | `scenario/lightless-beacon` — `hook`, `advice` |
| Предыстория | 8–9 | `scenario/lightless-beacon` — `keeper_info`; `character/beacon-george-cassidy`, `beacon-samuel-smith`, `beacon-michael-turner`; `location/beacon-wreck` |
| Карта Рокпорта и Фолли-Пойнт | 8, 24 | `map/beacon-rockport-folly-point` (картинка `app/maps/beacon-rockport-folly-point.jpg`, 8 меток); `coc:location:rockport`, `location/beacon-rockport-outskirts`, `beacon-folly-point`, `beacon-island`, `beacon-granite-quarries`, `beacon-cape-pond` |
| Подготовка к игре (текст для чтения вслух) | 9 | `scene/beacon-setting-up` |
| Начало: бурные воды | 9–10 | `scene/beacon-choppy-waters`; `location/beacon-wreck` |
| Мёртвый остров | 10 | `scene/beacon-dead-island`; `location/beacon-island`, `beacon-north-pier` |
| Карта острова Бикон (ключ 1–9) | 10, 25 | `map/beacon-island` (12 меток); места 1–9: `location/beacon-south-pier`, `beacon-lighthouse`, `beacon-keepers-house`, `beacon-shower`, `beacon-outhouse`, `beacon-generator-shed`, `beacon-workshop`, `beacon-thicket`, `beacon-north-pier` |
| Хранителю на заметку (сыщики могут разделиться) | 11 | `scene/beacon-dead-island` |
| Если идти по следам | 11 | `scene/beacon-following-tracks`; `item/beacon-improvised-weapons` |
| Создание напряжения (врезка) | 11 | `scene/beacon-dead-island`; `scenario/lightless-beacon` — `advice` |
| Заросли | 11 | `scene/beacon-thicket`; `item/beacon-turner-badge`, `beacon-turner-revolver`, `beacon-youngling-needles`; `character/beacon-michael-turner` |
| Южный пирс | 12 | `scene/beacon-south-pier`; `item/beacon-yellow-rowboats`, `beacon-binoculars` |
| Хранителю на заметку (поездка на материк) | 12 | `scene/beacon-south-pier` |
| Обезумевшие сыщики (врезка) | 12 | `scenario/lightless-beacon` — таблица «Обезумевшие сыщики», `advice` |
| Дом смотрителя маяка | 13 | `scene/beacon-keepers-house`; `location/beacon-keepers-house` |
| Коридор | 13 | `scene/beacon-keepers-house`; `location/beacon-hallway`; `item/beacon-innsmouth-gold-coins` |
| Хранителю на заметку (комбинированные проверки) | 13 | `scene/beacon-keepers-house` |
| Кабинет | 13–14 | `scene/beacon-study`; `location/beacon-study`; `item/beacon-shadow-watercolour`, `beacon-thicket-watercolour`, `beacon-coin-bills-and-letters`, `beacon-cassidy-colt` (коробка и пули); `handout/beacon-1-tilton-letter`, `beacon-2-cassidy-diary` |
| Хранителю на заметку (почерк Кэссиди) | 14 | `scene/beacon-study`, `handout/beacon-2-cassidy-diary` |
| Кухня | 14 | `scene/beacon-kitchen`; `location/beacon-kitchen`; `item/beacon-kitchen-knife` |
| Спальня | 14 | `scene/beacon-bedroom`; `location/beacon-bedroom`; `handout/beacon-3-turner-notebook` |
| Кладовая | 14 | `location/beacon-pantry`; `scene/beacon-keepers-house` |
| Карта маяка острова Бикон (ключи 1–12, 21–25) | 15, 26 | `map/beacon-lighthouse` (18 меток); места: `location/beacon-hallway` (1, 3, 12), `beacon-bedroom` (2), `beacon-study` (4, 10, 11), `beacon-kitchen` (5, 6), `beacon-pantry` (7), `beacon-lighthouse` (8, заголовок), `beacon-spiral-staircase` (9, 22), `beacon-keepers-house` (21), `beacon-technical-room` (23), `beacon-lamp-room` (24), `beacon-balcony` (25) |
| Материал: Маяк 1 | 16, 27 | `handout/beacon-1-tilton-letter`; `character/beacon-anna-tilton`; `organization/beacon-newburyport-society` |
| Материал: Маяк 2 | 17, 28 | `handout/beacon-2-cassidy-diary` |
| Техническое помещение маяка (+ заметка Хранителю) | 18 | `scene/beacon-technical-room`; `location/beacon-technical-room`; `item/beacon-maintenance-log`, `beacon-spare-lamps`, `beacon-radio`; `organization/beacon-coast-guard` |
| Материал: Маяк 3 | 18, 29 | `handout/beacon-3-turner-notebook` |
| Маяк Бикон (+ заметка Хранителю о Торговце) | 18–19 | `scene/beacon-lamp-room`; `location/beacon-lamp-room`; `item/beacon-cassidy-purse`, `beacon-cassidy-colt`, `beacon-youngling-needles`, `beacon-spare-lamps` |
| Нападение амфибий | 20 | `scene/beacon-amphibious-assault` |
| Сквозь лес (+ заметка Хранителю) | 20 | `scene/beacon-through-the-woods` |
| В осаде (+ две заметки Хранителю) | 20–21 | `scene/beacon-under-siege` |
| Хранителю на заметку (не больше двух штрафных костей) | 21 | `scene/beacon-amphibious-assault` |
| Финал (+ заметка Хранителю) | 21 | `scene/beacon-finale`; `scenario/lightless-beacon` — `conclusion`; `organization/beacon-bureau-of-investigation`, `beacon-coast-guard` |
| Итоги и награды | 21 | `scenario/lightless-beacon` — `conclusion` (награды Рассудка) |
| Эпилог | 21 | `scenario/lightless-beacon` — `conclusion` |
| Описание монстров; Детёныши; Тактика детёнышей | 22 | `creature/detenysh` (уже в базе); описание и тактика — в предложениях (`proposals-beacon.json`); тактика также в `scene/beacon-amphibious-assault` |
| Детёныш, глубоководный кошмар (статблок) | 22–23 | `creature/detenysh` (уже в базе) |
| Глубоководный гибрид, испорченное Иннсмутом потомство | 23 | `creature/glubokovodnyy-gibrid` (уже в базе, `same_as` `coc:creature:deep-one-hybrid`); описание и роль — в предложениях |
| Карты на всю страницу | 24–26 | источники `map/*` (вторые `sources`) |
| Собранные раздаточные материалы | 27–29 | источники `handout/*` (третьи `sources`) |
| Листы готовых сыщиков | 30–41 | уже в базе: `character/antique-dealer` (30–32), `artist` (33–35), `bureau-agent` (36–38), `marine-biologist` (39–41) |
| Грег Стэффорд (1948–2018) | 42 | не взято (см. ниже) |

Сверх заголовков: организация Эзотерический орден Дагона — существующая запись
`pobeg-iz-innsmuta-ru/organization/ezotericheskiy-orden-dagona` (ссылки из сценария и монет; источник «Маяка» — в
предложениях), без дубля.

## Не взято

- Титры (с. 3): авторы, редактура, художники, вёрстка, плейтестеры, правовая информация — не игровые данные; авторы
  названы в `summary` сценария.
- Содержание (с. 4): навигация книги, все её разделы есть в таблице выше.
- Посвящение Грегу Стэффорду (с. 1, 42): памятный текст без игровых данных.
- Иллюстрации и подписи к ним («На соседней странице: Погасший маяк» — с. 4–5; «Кабинет в доме смотрителя» — с. 13;
  «Детёныш и труп гибрида» — с. 19; «Детёныш» — с. 22): картинки в `app/art/` не входят в эту часть (папка не моя);
  при желании их добавит владелец через `pipeline/art/add_images.py`.
- Картинки раздаточных материалов (`images` у handout) — по той же причине; тексты раздаток перенесены дословно.
- На картах без меток: врезка «Ньюберипорт», «Ипсвич», «Эссекс» (записей этих городов нет — вопрос владельцу),
  «Атлантический океан», номера дорог 1, 127, 128, 133, масштаб, роза ветров, заголовок карты; на карте острова —
  подпись «Прибл. 650 ярдов» (перенесена в описания как «около 650 м»); на плане маяка — «Боковая проекция», «План
  первого этажа», размеры в футах, строка бюро «Говард и Роубсон» (бюро упомянуто в описаниях Фолли-Пойнт и маяка).
- Пароход «Графство Эссекс» отдельной записи не получил (только в текстах сцен и сценария): кроме названия и
  крушения, в книге о нём ничего нет.
- Отдельных записей двух глубоководных гибридов (погибший в фонарной комнате и ждущий в Фолли-Пойнт) нет: книга не
  даёт им имён и своих статблоков, они — участники сцен со ссылкой на `creature/glubokovodnyy-gibrid`.
