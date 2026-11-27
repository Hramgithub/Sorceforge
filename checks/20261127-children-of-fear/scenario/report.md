# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 1 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 5 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Глава 8. Сердце мира | `children-of-fear-en` | 307–323 | 16 | 16 (7) | 6 (3) | 3 (3) | 8 | 24 | 2 | 0 | 2 |
| Глава 7. Духи земли | `children-of-fear-en` | 277–297 | 14 | 15 (8) | 8 (5) | 6 (6) | 8 | 32 | 6 | 0 | 1 |
| Дети страха | `children-of-fear-en` | 324–324 | 0 | 15 (14) | 7 (6) | 0 (0) | 0 | 20 | 2 | 0 | 1 |
| Глава 1. Город увядающего великолепия | `children-of-fear-en` | 36–48 | 10 | 8 (5) | 0 (0) | 5 (5) | 4 | 25 | 2 | 0 | 1 |
| Глава 2. К Вратам Солнца | `children-of-fear-en` | 53–90 | 22 | 19 (12) | 5 (2) | 6 (6) | 14 | 30 | 4 | 0 | 1 |
| Глава 5. Пир и голод | `children-of-fear-en` | 188–220 | 21 | 6 (4) | 6 (5) | 4 (4) | 9 | 52 | 2 | 0 | 0 |
| Глава 6. Освобождение | `children-of-fear-en` | 230–263 | 15 | 9 (5) | 5 (4) | 5 (5) | 7 | 30 | 2 | 0 | 0 |
| Глава 4. Старые кости | `children-of-fear-en` | 156–185 | 20 | 6 (3) | 9 (5) | 8 (8) | 7 | 32 | 2 | 0 | 0 |
| Глава 3. Песнь утраченного и забытого | `children-of-fear-en` | 98–144 | 17 | 31 (10) | 13 (9) | 11 (11) | 9 | 47 | 8 | 0 | 0 |

## Находки по сценариям

### Глава 8. Сердце мира (`children-of-fear-en/scenario/the-heart-of-the-world`) — 2

- [low] `scenes.no_people` `children-of-fear-en/scene/heart-getting-to-danakosha-lake` Путь к озеру Данакоша — сцена без участников
- [low] `scenes.no_people` `children-of-fear-en/scene/heart-any-old-port` Любой порт — сцена без участников

### Глава 7. Духи земли (`children-of-fear-en/scenario/spirits-of-the-earth`) — 1

- [low] `scenes.no_people` `children-of-fear-en/scene/spirits-getting-to-patna` Дорога в Патну — сцена без участников

### Дети страха (`children-of-fear-en/scenario/the-children-of-fear`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Глава 1. Город увядающего великолепия (`children-of-fear-en/scenario/the-city-of-decaying-splendor`) — 1

- [low] `scenes.no_people` `children-of-fear-en/scene/peking-an-unseasonable-storm` Необычный град — сцена без участников

### Глава 2. К Вратам Солнца (`children-of-fear-en/scenario/to-the-gates-of-the-sun`) — 1

- [low] `scenes.no_people` `children-of-fear-en/scene/gates-visions-in-the-dark` Видения во тьме: Сиань и коридор Ганьсу — сцена без участников

