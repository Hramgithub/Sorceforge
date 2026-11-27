# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 19 |
| `scenes.none` | У сценария нет сцен | 1 |
| `scenes.no_place` | Сцена без места | 1 |
| `scenes.no_people` | Сцена без участников | 8 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Дети страха | `children-of-fear-en` | 324–324 | 0 | 9 (1) | 7 (5) | 0 (0) | 0 | 16 | 2 | 0 | 8 |
| Глава 5. Пир и голод | `children-of-fear-en` | 188–220 | 21 | 3 (0) | 6 (2) | 4 (0) | 5 | 25 | 2 | 0 | 5 |
| Глава 8. Сердце мира | `children-of-fear-en` | 307–323 | 16 | 12 (0) | 6 (2) | 3 (0) | 8 | 24 | 2 | 0 | 5 |
| Глава 4. Старые кости | `children-of-fear-en` | 156–185 | 20 | 3 (0) | 9 (2) | 8 (0) | 7 | 23 | 2 | 0 | 3 |
| Глава 1. Город увядающего великолепия | `children-of-fear-en` | 36–48 | 10 | 7 (2) | 0 (0) | 5 (5) | 4 | 24 | 2 | 0 | 3 |
| Глава 7. Духи земли | `children-of-fear-en` | 277–297 | 14 | 11 (0) | 6 (1) | 6 (0) | 8 | 29 | 6 | 0 | 2 |
| Глава 2. К Вратам Солнца | `children-of-fear-en` | 53–90 | 22 | 15 (1) | 5 (1) | 6 (0) | 11 | 28 | 4 | 0 | 2 |
| Глава 6. Освобождение | `children-of-fear-en` | 230–263 | 15 | 8 (0) | 5 (1) | 5 (0) | 6 | 27 | 2 | 0 | 1 |

## Находки по сценариям

### Дети страха (`children-of-fear-en/scenario/the-children-of-fear`) — 8

- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → children-of-fear-en/scenario/song-of-the-lost-and-forgotten
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → children-of-fear-en/location/song-tarim-basin
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → children-of-fear-en/location/song-mountain-passes
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → coc:location:chakdara
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → coc:location:peshawar
- [high] `plot.bad_ref` шаг «Приложения» → coc:spell:open-the-gates-of-agartha
- [high] `plot.bad_ref` шаг «Приложения» → coc:spell:send-vision
- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Глава 5. Пир и голод (`children-of-fear-en/scenario/feast-and-famine`) — 5

- [high] `plot.bad_ref` шаг «Перемена обстановки» → coc:spell:mask-of-reason
- [high] `plot.bad_ref` шаг «Свидание с дакини: свиток» → coc:spell:open-the-gates-of-agartha
- [high] `plot.bad_ref` шаг «Дальнейший путь» → children-of-fear-en/scenario/song-of-the-lost-and-forgotten
- [low] `scenes.no_people` `children-of-fear-en/scene/feast-entering-tibet` Въезд в Тибет — сцена без участников
- [low] `scenes.no_people` `children-of-fear-en/scene/feast-visions-in-the-dark-derge` Видения во тьме: Дерге — сцена без участников

### Глава 8. Сердце мира (`children-of-fear-en/scenario/the-heart-of-the-world`) — 5

- [high] `plot.bad_ref` шаг «Последний ритуал» → coc:spell:the-closing-of-the-way
- [low] `scenes.no_people` `children-of-fear-en/scene/heart-getting-to-danakosha-lake` Путь к озеру Данакоша — сцена без участников
- [low] `scenes.no_people` `children-of-fear-en/scene/heart-any-old-port` Любой порт — сцена без участников
- [low] `scenes.no_people` `children-of-fear-en/scene/heart-into-the-jungle` В джунгли — сцена без участников
- [low] `scenes.no_place` `children-of-fear-en/scene/heart-brain-food` Пища для ума — сцена без места

### Глава 4. Старые кости (`children-of-fear-en/scenario/old-bones`) — 3

- [high] `plot.bad_ref` шаг «Начистоту» → coc:spell:enchant-sacred-instruments
- [high] `plot.bad_ref` шаг «Необязательная встреча: демон-скорпион» → coc:spell:summon-bind-scorpion-demon
- [high] `plot.bad_ref` шаг «Дальше в путь» → children-of-fear-en/scenario/song-of-the-lost-and-forgotten

### Глава 1. Город увядающего великолепия (`children-of-fear-en/scenario/the-city-of-decaying-splendor`) — 3

- [high] `plot.bad_ref` шаг «Опоздавшие» → children-of-fear-en/character/sofian-bazaz-wain
- [high] `plot.bad_ref` шаг «Видения во тьме» → coc:spell:send-vision
- [low] `scenes.no_people` `children-of-fear-en/scene/peking-an-unseasonable-storm` Необычный град — сцена без участников

### Глава 7. Духи земли (`children-of-fear-en/scenario/spirits-of-the-earth`) — 2

- [high] `plot.bad_ref` шаг «Зарытое сокровище» → coc:spell:the-closing-of-the-way
- [low] `scenes.no_people` `children-of-fear-en/scene/spirits-getting-to-patna` Дорога в Патну — сцена без участников

### Глава 2. К Вратам Солнца (`children-of-fear-en/scenario/to-the-gates-of-the-sun`) — 2

- [high] `plot.bad_ref` шаг «Шаг за шагом — дальше» → children-of-fear-en/scenario/song-of-the-lost-and-forgotten
- [low] `scenes.no_people` `children-of-fear-en/scene/gates-visions-in-the-dark` Видения во тьме: Сиань и коридор Ганьсу — сцена без участников

### Глава 6. Освобождение (`children-of-fear-en/scenario/liberation`) — 1

- [high] `plot.bad_ref` шаг «Проведение ритуала» → coc:spell:open-the-gates-of-agartha

