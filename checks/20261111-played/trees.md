# «Среди древних деревьев» («Книга хранителя», `keeper-rulebook-ru`) — сверка переноса (часть trees)

Источник — официальное русское издание «Книги хранителя» (скан с шумным текстовым слоем; `pages.py show`). Текст
сверен по изображениям страниц (`pages.py image`, 150 dpi) и по распознанной копии сценария из папки владельца
(`2_Обработка\1925 Среди древних деревьев\среди древних деревьев_распознан_сжатие_через акробат.pdf` — тот же скан,
только чище текстовый слой; как источник не используется). Английское издание (`keeper-rulebook-en`, «Amidst the
Ancient Trees», с. 346–363, печатная = физическая − 1) — для английских названий и сверки чисел: все статблоки и
потери Рассудка совпадают с русскими. Карты взяты из официальной раздатки
`[RU 7e] Раздатка _Среди древних деревьев_ и _Багровые письмена_.pdf` (с. 2 и 3; с. 1 — карточки «Сонного зова»,
с. 4–5 — «Багровые письмена», не наша часть). Отдельный скан главы (`[RU 7e] среди древних деревьев.pdf`) — та же
съёмка, что в книге; не понадобился: в скане книги все 18 страниц есть.

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 15, «Среди древних деревьев» | 344–361 | 321–338 |
| Раздатка: карточки «Сонного зова» | 361 (в книге) | раздатка, с. 1 |
| Раздатка: карта «Раскопки, хижина Тёрнера и озеро» | 354 (в книге) | раздатка, с. 2 |
| Раздатка: карта «Южный Вермонт» | 350 (в книге) | раздатка, с. 3 |

Смещение на этом участке: **печатная = физическая + 23** (по `page_map`; проверено на 344–361).

Записи — `kb/books/keeper-rulebook-ru/<вид>/trees-*`; ниже `…/` = `keeper-rulebook-ru/`. Город — общий
`coc:location:bennington` (новый, Р-190).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Среди древних деревьев (вступление) | 344 | сценарий `…/scenario/trees-amidst-the-ancient-trees` (summary) |
| Введение | 344 | сценарий: summary, hook, advice (навыки, перечитать гл. 14); город `coc:location:bennington` |
| Предыстория | 344–345 | сценарий: keeper_info; `…/creature/trees-thing-in-the-lake` (legend); `…/character/trees-joseph-turner` (legend); `…/organization/trees-turner-gang`; `…/item/trees-crystal-shard` |
| Недавние события | 345–346 | сценарий: keeper_info; `…/character/trees-lucas-strong`, `…/character/trees-sidney-harris`, `…/character/trees-jane-strong` (legend); `…/organization/trees-strong-survey-team`, `…/organization/trees-vermont-water-board`, `…/organization/trees-harris-gang`; места `…/location/trees-somerset`, `…/location/trees-somerset-reservoir` |
| Действующие лица | 346 | сценарий: keeper_info (абзац «Действующие лица»); записи всех названных персонажей (22), организаций и `…/creature/trees-thing-in-the-lake` |
| Хронология событий (День 0 — День 3) | 346 | сценарий: таблица «Хронология событий» (15 строк); персонажи (legend) |
| Мотивы сыщиков | 346–347 | сценарий: hook; таблица «Возможные мотивы сыщиков» |
| Возможные мотивы сыщиков: Первый, Второй, Третий, Четвёртый (с «Информацией для Хранителя») | 347 | раздатки `…/handout/trees-motive-1-debts`, `…/handout/trees-motive-2-brother`, `…/handout/trees-motive-3-fired`, `…/handout/trees-motive-4-old-score` (текст для игрока + информация для Хранителя в description); таблица сценария |
| Врезка о случайном распределении мотивов (награда 1d6) | 347 | сценарий: advice, conclusion, таблица «Возможные мотивы сыщиков» (intro) |
| День 1. Инструктаж (зачитываемый текст, пункты шерифа, Стронг) | 347–348 | сцена `…/scene/trees-briefing`; место `…/location/trees-bennington-police-station`; `…/character/trees-sheriff-jenkins`; `…/organization/trees-search-posse` |
| День 1. Инструктаж: лавка Спенса, подшивка «Беннингтон баннер», слухи, главная площадь | 348 | сцена `…/scene/trees-preparations`; места `…/location/trees-spence-store`, `…/location/trees-bennington-library`, `…/location/trees-bennington-banner-office`; `…/organization/trees-bennington-banner`; таблица «Слухи Беннингтона (лето 1925 года)» у города (в сценарии — ссылка `from`) |
| Врезка о слухах («Советуем Хранителю…») | 348 | сцена `…/scene/trees-preparations`; таблица слухов у города (последние строки); сценарий: advice |
| Начало маршрута — место перестрелки | 349 | сцена `…/scene/trees-shootout-site`; место `…/location/trees-2-shootout-site` |
| Врезка о проверках Чтения следов | 349 | сцена `…/scene/trees-shootout-site`; сценарий: advice |
| День 1. Встреча с охотниками | 349 | сцена `…/scene/trees-meeting-hunters`; место `…/location/trees-3-hunters`; `…/character/trees-alistair-lawson`, `…/character/trees-george-lawson` |
| День 1. Первая ночь | 349–350 | сцена `…/scene/trees-first-night`; таблица «Карточки «Сонного зова»» |
| Карта «Южный Вермонт: ужас и смерть в Зелёных горах» (ключ 1–11) | 350 | карта `…/map/trees-southern-vermont` (метки 1–11, «Беннингтон», «Сомерсет»); места 2–11 и город (номер 1) |
| День 2. Дорога через лес | 350 | сцена `…/scene/trees-forest-day-2`; место `…/location/trees-forest` |
| День 2. Труп художника | 350 | сцена `…/scene/trees-artist-body`; место `…/location/trees-4-artist-body`; `…/character/trees-escaped-artist`; `…/item/trees-bloody-hunting-knife` |
| День 2. Грузовик | 350–351 | сцена `…/scene/trees-truck`; место `…/location/trees-6-turn-to-dig-site`; `…/character/trees-james-stanton`; `…/item/trees-survey-truck`, `…/item/trees-dynamite` |
| Врезка «Повторные проверки навыков в лесу» | 351 | сценарий: таблица «Повторные проверки навыков в лесу» (6 строк) |
| Иллюстрация «Труп художника» | 351 | не взято (см. ниже) |
| День 2. Первый похититель | 351–352 | сцена `…/scene/trees-first-kidnapper`; место `…/location/trees-5-shell-casings`; `…/character/trees-eugene-clayton` |
| Врезка «Погоня за похитителем в лесу» | 352 | сцена `…/scene/trees-first-kidnapper` (список •); сценарий: таблица «Погоня за похитителем в лесу» |
| День 2. Вторая ночь | 352 | сцена `…/scene/trees-second-night`; `…/character/trees-louis`; `…/organization/trees-search-posse` (другая группа) |
| День 3. Дорога через лес | 352 | сцена `…/scene/trees-forest-day-3`; место `…/location/trees-forest` |
| День 3. Лагерь художников | 352–354 | сцена `…/scene/trees-artists-camp`; место `…/location/trees-7-artists-camp`; `…/character/trees-artists`; предметы `…/item/trees-artists-notebook`, `…/item/trees-brian-hall-hat-and-rifle` |
| Список картин и иллюстрация «Картины, найденные в лагере художников»; проверка Рассудка за картину | 353–354 | `…/item/trees-artists-paintings` (список •, механика); сцена `…/scene/trees-artists-camp` |
| Карта «Раскопки, хижина Тёрнера и озеро» (ключ 1–5) | 354 | карта `…/map/trees-dig-site` (метки 1–5 и все 18 подписей); места `…/location/trees-dig-1-office` … `…/location/trees-dig-5-tool-shed`, `…/location/trees-dig-pit`, `…/location/trees-lake-stakes` |
| День 3. Убежище | 354 | сцена `…/scene/trees-hideout`; место `…/location/trees-8-hideout`; `…/character/trees-christopher-dobbs`, `…/character/trees-sidney-harris`; `…/item/trees-ransom-bag` |
| День 3. Хижина Тёрнера | 354 | сцена `…/scene/trees-turner-cabin`; место `…/location/trees-10-turner-cabin`; `…/item/trees-civil-war-rifle` |
| Иллюстрация «Вот что сыщики найдут в хижине Тёрнера»; погреб, гробы, находки | 355–356 | сцена `…/scene/trees-turner-cabin` (список •); место `…/location/trees-turner-cabin-cellar`; предметы `…/item/trees-stone-caskets`, `…/item/trees-gang-trinkets`, `…/item/trees-glaaki-spine`, `…/item/trees-turner-diary`, `…/item/trees-green-dust`; `…/character/trees-august`, `…/character/trees-jacob` |
| Последний абзац дневника Тёрнера (зачитать вслух) | 355 | раздатка `…/handout/trees-turner-diary-passage` |
| День 3. У озера (с речью художников) | 356 | сцена `…/scene/trees-lake`; места `…/location/trees-11-lake`, `…/location/trees-lake-stakes` |
| Иллюстрация «УБЕЙТЕ НАС! ВЫРВИТЕ ШИПЫ! МОЛЮ!» | 356 | не взято (см. ниже); подпись — в тексте сцены `…/scene/trees-lake` |
| День 3. Место раскопок; Попытка пойти напрямик | 356–357 | сцена `…/scene/trees-dig-site`; место `…/location/trees-9-dig-site`; `…/character/trees-richard-gibson` |
| На месте раскопок (пять бараков) | 357 | сцена `…/scene/trees-dig-site` (список •); места `…/location/trees-dig-1-office` … `…/location/trees-dig-5-tool-shed`; `…/item/trees-survey-papers`, `…/item/trees-dynamite`, `…/item/trees-pulley-system` |
| Иллюстрация «Место раскопок» | 357 | не взято (см. ниже) |
| Объяснение Карла и ловушка | 358 | сцена `…/scene/trees-karl-trap`; `…/character/trees-carl-white` |
| Сыщики попадают в плен | 358 | сцена `…/scene/trees-karl-trap`; место `…/location/trees-dig-4-storeroom` |
| Другие пленники и охрана | 358 | сцена `…/scene/trees-karl-trap` (пункты •); `…/character/trees-jane-strong`, `…/character/trees-brian-hall`, `…/character/trees-arthur-hall` (legend) |
| Иллюстрация «Кристалл» | 358 | не взято (см. ниже); описание кристалла — `…/item/trees-crystal-shard` |
| Побег | 358–359 | сцена `…/scene/trees-escape` |
| Более осторожный подход | 359 | сцена `…/scene/trees-cautious-approach`; `…/creature/trees-thing-in-the-lake` (способность «Осушение кристалла») |
| Итоги (награды Рассудка) | 359 | сценарий: conclusion (пункты •) |
| Врезка «Примечание об опасности» | 359 | сценарий: advice; `…/organization/trees-turner-gang`; `…/item/trees-civil-war-rifle` |
| Персонажи Хранителя (вступление) | 359 | сценарий: advice |
| Джозеф Тёрнер и его банда, неживые служители (слабости) | 359 | `…/organization/trees-turner-gang` (description); `…/character/trees-joseph-turner` |
| Джозеф Тёрнер, избранный служитель Гла’аки (статблок) | 360 | `…/character/trees-joseph-turner` (statblock, `instance_of` `coc:creature:servant-of-glaaki`) |
| Август, Джейкоб, Винсент и Луис, банда Тёрнера | 360 | `…/character/trees-august`, `…/character/trees-jacob`, `…/character/trees-vincent`, `…/character/trees-louis` (`instance_of` служителя Гла’аки) |
| Геологи Стронга, служители Гла’аки | 360 | `…/character/trees-carl-white`, `…/character/trees-james-stanton`, `…/character/trees-dean-walters`, `…/character/trees-richard-gibson` (`instance_of` служителя Гла’аки) |
| Сидней Харрис и Юджин Клейтон, похитители в бегах (статблок) | 360 | `…/character/trees-sidney-harris`, `…/character/trees-eugene-clayton` (общий статблок, своя атака оружием) |
| Лукас Стронг, глава совета по водным ресурсам (статблок) | 360 | `…/character/trees-lucas-strong` |
| Джейн Стронг, жертва похищения, 16 лет (статблок) | 360 | `…/character/trees-jane-strong` |
| Алистер Лоусон и Брайан Холл, отцы (статблок) | 360 | `…/character/trees-alistair-lawson`, `…/character/trees-brian-hall` (общий статблок; errata БкУ и Комплекции) |
| Джордж Лоусон (14) и Артур Холл (12), сыновья (статблок) | 360 | `…/character/trees-george-lawson`, `…/character/trees-arthur-hall` |
| Гла’аки, Великий Древний | 360 | `…/creature/trees-thing-in-the-lake` (`instance_of` `coc:creature:glaaki`, параметры — с. 315) |
| Наглядные материалы «Сонный зов»: Бессонная ночь, Лесная тропа, Хижина во тьме, Обитатель озера | 361 | раздатки `…/handout/trees-dream-1-restless-night`, `…/handout/trees-dream-2-forest-path`, `…/handout/trees-dream-3-cabin-in-darkness`, `…/handout/trees-dream-4-thing-in-the-lake`; сценарий: таблица «Карточки «Сонного зова»» |

## Записи

103 файла: сценарий 1, сцен 19, мест 27 (город `coc:location:bennington` в `kb/locations/`, «Окрестности Беннингтона»
и 25 мест книги), карт 2, персонажей 22, существо 1, организаций 6, предметов 16, раздаток 9. Картинки карт —
`app/maps/trees-southern-vermont.jpg`, `app/maps/trees-dig-site.jpg`. Книг Мифов нет: дневник Тёрнера не имеет
параметров книги Мифов — это предмет (улика) плюс раздатка с зачитываемым абзацем.

Связь с общими записями: Гла’аки (`coc:creature:glaaki`) — `instance_of` у обитателя озера; служитель Гла’аки
(`coc:creature:servant-of-glaaki`) — `instance_of` у Тёрнера, его банды и геологов; заклинания Тёрнера —
`coc:spell:dominate`, `coc:spell:wither-limb`, `coc:spell:create-barrier-of-naach-tith` (все уже были); медведь —
`coc:creature:bear`; оружие — `coc:weapon:30-06-bolt-action-rifle`, `coc:weapon:shotgun-12-gauge-2b`,
`coc:weapon:dynamite-stick`. Новых заклинаний нет.

## Опечатки и сомнения

- Алистер Лоусон и Брайан Холл: БкУ «+1d4» и Комплекция «1» при СИЛ 50 + ТЕЛ 65 = 115 (по правилам — 0 и 0); так же в
  английском оригинале. Оставлено как напечатано, `errata` у обоих.
- Тёрнер: урон ножа «1d6 + 1 + БкУ» не совпадает ни с одним ножом таблицы оружия (средний 1d4+2, большой 1d8; 1d6+1 —
  топорик/серп) — ссылки на оружие у атаки нет, пометка в `quality.notes`. Уклонение 15% (у типового служителя 10%) —
  как напечатано.
- Джейн Стронг: Рассудок 64 при МОЩ 65 — как напечатано (не опечатка по правилам).
- Расстояние по следу к трупу художника: русское «около километра», английское «a half-mile» — пометка в сцене.
- Номера карты 5 «Гильзы» и 6 «Поворот к месту раскопок» текст сценария не расшифровывает: связь с утёсом Юджина
  Клейтона и со сценой «Грузовик» — вывод из текста (Р-41), пометки в записях мест.
- Озеро без подписи на карте «Южный Вермонт» (между номерами 6 и 9) — вероятно, Сомерсетское водохранилище; книга не
  говорит, метки нет.
- Карточки «Хижина во тьме» и «Обитатель озера»: потеря в квадратных скобках напечатана с сокращением Рассудка; в
  `handout.text` заменено словами «пунктов рассудка» (Р-146), пометка в записях.

## Придумано нами (флаг `editorial_text`)

- Имена художников (Р-150, Р-151): сбежавший художник — «Генри Колдуэлл»; группа — 5 имён в `names`.
- Названия: «Окрестности Беннингтона» (Р-209), «Лес на краю парка Грин-Маунтин», «Озеро Гла’аки», «Встреча с
  охотниками» (в ключе — «Охотники»), «Поисковый отряд шерифа».

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Иллюстрации «Инструктаж», «Труп художника», «Картины, найденные в лагере художников», «Вот что сыщики найдут в хижине Тёрнера», «УБЕЙТЕ НАС!…», «Место раскопок», «Кристалл», щупальце на с. 360 | 348, 351, 353, 355, 356, 357, 358, 360 | картинки не переносились (`images` записей не заполнялись); содержание подписей — в текстах сцен и предметов |
| Брат Джон (второй мотив), подпольный ростовщик (первый мотив) | 347 | упомянуты только в тексте мотивов, записей персонажей не получили (текст — в раздатках) |
| «Другая группа добровольцев» | 351, 352 | безымянная группа без параметров — текстом в сцене «Вторая ночь», таблице повторных проверок и организации «Поисковый отряд шерифа» |
| Городки на карте «Южный Вермонт» (Манчестер, Арлингтон, Шафтсбери и др.), реки (в том числе подпись «Мискатоник»), границы штатов и округов | 350 | в тексте сценария не упоминаются; записей таких мест нет, меток нет (как на карте Гарлема в «Масках») |
| Ссылки на страницы книги в тексте («стр. 351», «стр. 88», «стр. 89», «стр. 337» и т. п.) | 349–356 | заменены ссылками на сцены и записи правил (`coc:rule:luck-rolls`, `coc:rule:bonus-and-penalty-dice`, `coc:creature:bear`) |

## Предложения правок общих записей

`checks/20261111-played/proposals-trees.json` — 6 правок одной записи `coc:location:boston`: абзац в описании
(охотники и художники из Бостона), источник, 4 ссылки (сценарий, художники, Алистер Лоусон, Брайан Холл).
Пробный прогон `pipeline/integrate/apply.py --dry-run` — ложится.
