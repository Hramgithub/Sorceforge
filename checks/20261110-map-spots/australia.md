# Метки на картах (Р-206): часть australia — «Маски Ньярлатхотепа» (EN 7e), глава 6 «Австралия», с. 449–518

Семь карт главы получили метки. Кружки с номерами (склад Рэндольфа, главный вход, штаб Хастона) найдены поиском колец
по картинке; подписи — распознаванием `tesseract` и по сетке вырезок. Каждая метка проверена глазами по увеличенной
вырезке с нарисованным центром и рамкой `spot_shape`.

| Карта | Меток | Номеров в ключе | Новых мест | Не поставлено |
|---|---|---|---|---|
| `australia-commonwealth-of-australia` (с. 451) | 10: 7 подписей городов + 3 стрелки пароходных путей | ключа нет | 0 | подписи без записей (см. «Не взято») |
| `australia-randolph-shipping` (с. 465) | 4 (1–4) | 4 | 0 | — |
| `australia-canning-basin` (с. 470) | 10: 5 мест + 5 колодцев | ключа нет | 0 | «Great Sandy Desert» — сама пустыня, которую показывает карта; подписи без записей |
| `australia-city-environs` (с. 479) | 24: колодцы 22–36 + 6 названных колодцев + 3 места | 15 (колодцы 22–36) | 15 (колодцы 22–36) | Сахара-Уэлл, озёра, холмы, звёзды засад |
| `australia-hustons-main-entrance` (с. 487) | 4 (1–4) | 5 (1–4 и значок «Ancient blocks») | 0 | значок «Ancient blocks» — без номера |
| `australia-portion-of-the-city` (с. 490) | 14 (все подписи в рамках) | ключ условных знаков | 0 | значки генераторов и завалов |
| `australia-hustons-headquarters` (с. 499) | 14 (1, 2, 3 ×7, 4–8) | 8 | 0 | — |
| Итого | 80 | — | 15 | — |

Все номера ключей, которые напечатаны на картах, получили метки. Номера планов — предметы и части одного здания или
места (склад, главный вход, штаб): метки с `text` (Р-155). Колодцы тропы Каннинга 22–36 получили свои записи (решение
ведущего по Р-206 «записи для всех номеров»); туземные колодцы без номеров — метки с `text` на «Тропу Каннинга».
Подписи схемы города и мест на картах пустыни ведут на уже заведённые записи.

## Записи

- Карты (7): `spots`, `spot_shape`, `quality.notes`, `corrections` (spots, spot_shape).
- `kb/books/masks-of-nyarlathotep-en/locations/australia-hustons-headquarters.json`: снята ошибочная `errata` «текст — семь
  клеток, план — шесть»: на плане с. 499 номер 3 напечатан семь раз (3 + 2 + 2), как и в тексте с. 498; в описание
  добавлено «семь больших кубических клеток (3)», флаг `parse_uncertain` снят, правка — в `corrections`.
- Новые места (15): `kb/books/masks-of-nyarlathotep-en/locations/australia-well-22.json` … `australia-well-36.json` —
  «Колодец N» (с подписью карты, если есть: 24 Curara Soaks, 26 Tiwa, 33 Gunowaggi, 34 Nibil, 35 Minjoo, 36 Wanda),
  `part_of` — «Тропа Каннинга», `number`, описание по с. 477 и 479 (у 34 — ещё с. 480), флаг `translated`.
- `australia-canning-stock-route.json`: таблица «Карта «Ближние окрестности Города Великой Расы»: колодцы 22–36» со
  ссылками строк на колодцы, `refs` на 15 колодцев.
- Метка «Nibil Well» карты бассейна Каннинг ведёт на «Колодец 34 (Нибил)».
- Предложения: `proposals-australia.json` — 1 (`append` в `where` сцены «Путь Уикрофта» → «Колодец 34 (Нибил)»);
  пробный прогон `apply.py --dry-run`: 1 правка.

## Метки по картам

### Австралийский Союз (`…/map/australia-commonwealth-of-australia`, `label` 6,0 × 1,8 %)

| Метка | x, y | Запись | Пометка |
|---|---|---|---|
| DARWIN | 47.17, 17.58 | Дарвин | |
| Port Hedland | 26.35, 37.5 | Порт-Хедленд | |
| Concudgerie | 27.3, 39.1 | Кункуджери | на карте «Concudgerie» |
| City of the Great Race | 40.8, 37.2 | Город Великой Расы | |
| PERTH | 25.0, 61.69 | Перт | |
| Fremantle | 25.66, 63.51 | Перт | Фримантл — порт Перта, псевдоним записи |
| SYDNEY | 80.3, 60.82 | Сидней | |
| To London and Colombo | 9.3, 60.2 | Лондон | у Коломбо записи нет |
| To Hong Kong and Shanghai | 42.3, 7.0 | Гонконг | Шанхай — во второй половине подписи |
| To Hong Kong | 55.3, 6.0 | Гонконг | |

### «Перевозки Рэндольфа» (`…/map/australia-randolph-shipping`, `circle` 2,7 × 4,2 %)

1 (72.77, 15.8) — койка; 2 (62.5, 15.94) — ящик со странным устройством; 3 (40.62, 39.35) — ящик с идолом Ктулху;
4 (74.46, 57.97) — бюро. Все — на «Склад «Перевозок Рэндольфа»» с `text`.

### Тропы и колодцы бассейна Каннинг (`…/map/australia-canning-basin`, `label` 7,0 × 2,4 %)

| Метка | x, y | Запись | Пометка |
|---|---|---|---|
| Port Headland | 9.35, 36.9 | Порт-Хедленд | на карте «Port Headland», в тексте — Port Hedland |
| DINGO FALLS | 36.1, 51.4 | Водопады Динго | |
| Cuncudgerie | 35.75, 55.5 | Кункуджери | |
| DEATH CAMP | 58.9, 51.0 | Мёртвый лагерь | |
| CITY OF THE GREAT RACE | 71.2, 48.7 | Город Великой Расы | |
| Bungabinni Well | 67.32, 53.6 | Тропа Каннинга (`text`) | с. 480 |
| Nibil Well | 66.9, 55.9 | Колодец 34 (Нибил) | с. 480 |
| Mallowa Well | 63.43, 58.1 | Тропа Каннинга (`text`) | с. 480 |
| Separation Well | 67.97, 66.8 | Тропа Каннинга (`text`) | |
| Nimberra Well | 61.3, 72.9 | Тропа Каннинга (`text`) | «Нимберра-Уэлл» — псевдоним записи; с. 480 |

### Ближние окрестности Города Великой Расы (`…/map/australia-city-environs`, `label` 2,8 × 1,6 %)

| Метка | x, y | Запись | Пометка |
|---|---|---|---|
| CITY OF THE GREAT RACE | 76.4, 39.5 | карта `australia-portion-of-the-city` | подпись самого города, который показывает карта: метка открывает схему города |
| DEATH CAMP | 43.7, 45.0 | Мёртвый лагерь | |
| GREAT SANDY DESERT | 82.0, 15.2 | Большая Песчаная пустыня | |
| 22–36 | см. запись карты | «Колодец 22» … «Колодец 36» (`australia-well-N`) | 24 — Curara Soaks, 26 — Tiwa, 33 — Gunowaggi, 34 — Nibil, 35 — Minjoo, 36 — Wanda |
| Nimberra Well | 26.3, 92.4 | Тропа Каннинга (`text`) | |
| Separation Well | 56.2, 81.0 | Тропа Каннинга (`text`) | |
| Nurgurga Native Well | 50.9, 72.7 | Тропа Каннинга (`text`) | |
| Nangabbittajarra Native Well | 42.0, 66.6 | Тропа Каннинга (`text`) | |
| Mallowa Native Well | 61.0, 64.4 | Тропа Каннинга (`text`) | |
| Bungabinni Native Well | 82.2, 56.6 | Тропа Каннинга (`text`) | |

### Главный вход Хастона (`…/map/australia-hustons-main-entrance`, `circle` 2,7 × 2,1 %)

1 (57.35, 46.56) — грузовики; 2 (15.99, 64.1) — склад под брезентом; 3 (17.37, 76.26) — генератор; 4 (28.92, 85.68) —
лестница в город. Все — на «Главный вход Хастона» с `text`.

### Часть Города Великой Расы (`…/map/australia-portion-of-the-city`, `label` 8,0 × 5,8 %)

Current Excavations → «Текущие раскопки»; Huston’s Headquarters → «Штаб Хастона»; Kakakatak’s Chamber → «Покои
Какакатак»; The Purple Dome Temple → «Храм Пурпурной полусферы»; Unexplored Lower Levels → «Город Великой Расы»
(`note`: своей записи нет); Beyond the Bottomless Shaft и The Shaft Into Darkness → «Провал во тьму» (`text`); Second
Entrance → «Второй вход»; Blue Great Plaza и Red Great Plaza → «Большие площади» (`text`); The Nursery → «Детская»;
Titan Horror → «Титанический ужас»; Huston’s Entrance → «Главный вход Хастона»; The Bunkhouse → «Бараки».

### Штаб Хастона (`…/map/australia-hustons-headquarters`, `circle` 2,5 × 4,4 %)

1 — шкафчик; 2 — место отдыха зомби; 3 — клетка (семь меток); 4 — футляры с документами; 5 — кучи снаряжения; 6 — стол
Хастона; 7 — покоритель разума; 8 — хронометр. Все — на «Штаб Хастона» с `text`.

## Заголовки книги

Полная сверка заголовков с. 449–518 сделана при переносе главы: `checks/20261109-masks/australia.md`. Эта часть
касается только карт:

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Commonwealth of Australia (карта) | 451 | `…/map/australia-commonwealth-of-australia`, 10 меток |
| Randolph Shipping Co. (план, Explanation 1–4) | 465 | `…/map/australia-randolph-shipping`, метки 1–4 на склад |
| Trails and Wells of the Canning Basin (карта) | 470 | `…/map/australia-canning-basin`, 10 меток |
| The Close Environs of the City of the Great Race (карта) | 479 | `…/map/australia-city-environs`, 24 метки |
| Huston’s Main Entrance (карта, Explanation 1–4) | 487 | `…/map/australia-hustons-main-entrance`, метки 1–4 |
| A Portion of the City (схема) | 490 | `…/map/australia-portion-of-the-city`, 14 меток |
| Huston’s Headquarters (план, Explanation 1–8) | 499 | `…/map/australia-hustons-headquarters`, 14 меток |

## Не взято

- Карта страны: подписи городов без записей (Derby, Broome, Onslow, Albany, Alice Springs, Townsville, Rockhampton,
  Brisbane, Port Augusta, Adelaide, Canberra и «Fed. Dist.», Melbourne, Hobart, Port Moresby), штатов (Western Australia,
  Northern Territory, Queensland, South Australia, New South Wales, Victoria, Tasmania), New Guinea, Sunda Islands,
  морей, океанов и заливов; стрелки «To Singapore», «To Capetown», «To Auckland», «To Wellington» и стрелка на
  северо-восток (подпись неразборчива, похоже «To Kokopo») — записей этих мест нет; заголовок, легенда, масштаб.
- Бассейн Каннинг: колодцы без описания в главе (Welcome Water, Escape Well, Discovery Well, Joanna Spring, Adverse
  Well, Sahara Well, Family Well, Jupiter Well, Surprise Well, Patience Well, Sunday Well), горы (Mount Alexander, Mount
  Morris, Cuncudgerie Hill, Mount Macpherson, Mount McLarty, Mount Bruce), озёра (Lake Gregory, Lake Disappointment,
  Percival Lakes), городки Pilbarra и Marble Bar, Eighty Mile Beach, Gibson Desert, Little Sandy Desert — записей нет;
  «Great Sandy Desert» — сама пустыня, которую показывает карта (`shows`); легенда.
- Окрестности города: Sahara Well (на пути Уикрофта, в тексте не названа), озёра Percival, Dora, Auld, Blanche, George,
  Winifred, Helen Hill, Slate Range, Cronin Hills, Escarpment, Gibson Desert — записей нет; звёзды «Ambush Point» —
  значки легенды (засада описана в сцене «Засада»); заголовок с надписью о колодцах 22–36, легенда, масштаб.
- Главный вход: значок «Ancient blocks» (пятая строка ключа) — без номера на карте, рассыпан по всей картинке.
- Схема города: значки генераторов, завалов, линий ламп и кабеля, цветные треугольники входов и спусков — условные знаки
  ключа (описаны в «Цепочках огней»); подпись «This is a schematic map…».
- Склад Рэндольфа: подписи «Warehouse», «Dock», «Beach», «Road», фотография «Randolph Shipping Co. 1924».
- Штаб Хастона: подписи этажей, ключ знаков (портьера, раздвижная дверь, окно), «Drop-off with a 30-foot fall and no
  rail», «All arrows point up ramps», «On a failed group Luck roll, zombie miners are sleeping in Location 2» (смысл — в
  описании места и в пояснении метки 2).

## Опечатки и сомнения

- Карта страны: «Concudgerie» вместо Cuncudgerie; карта бассейна Каннинг: «Port Headland» вместо Port Hedland — метки
  поставлены как напечатано, пометка — в `note` меток (по Р-39 в `errata` не записаны).
- Штаб Хастона: прежняя `errata` записи («план показывает шесть клеток») была ошибкой — клеток на плане семь, как в
  тексте; снята с записью в `corrections`.
- Колодцы на карте окрестностей: у номеров 22, 23, 25, 27–32 названий нет; названия 24, 26, 33–36 — как на карте, по-русски
  транслитерацией (наш перевод), английское — в скобках.

## Вопросы владельцу

1. Туземные колодцы без номеров (Нимберра, Сепарейшн, Нургурга, Нангаббиттаджарра, Маллова, Бунгабинни) остались
   метками с `text` на «Тропу Каннинга»: номеров у них нет, глава упоминает их одной-двумя фразами. Нужны ли им свои записи?

Подпись «City of the Great Race» на карте окрестностей открывает схему «Часть Города Великой Расы» — так решил ведущий.
