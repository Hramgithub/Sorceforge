# Целостность сценариев — 2026-11-23

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 2 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 5 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Звезда на берегу | `star-on-the-shore-en` | 8–67 | 16 | 64 (9) | 3 (0) | 21 (0) | 15 | 58 | 3 | 0 | 6 |
| Ключ к Бездне | `star-on-the-shore-en` | 68–76 | 4 | 4 (2) | 9 (1) | 2 (2) | 4 | 9 | 0 | 0 | 1 |

## Находки по сценариям

### Звезда на берегу (`star-on-the-shore-en/scenario/the-star-on-the-shore`) — 6

- [high] `clues.empty` `star-on-the-shore-en/handout/handout-14-constellation` Раздатка 14: созвездие на картинах — раздатка без текста и картинки
- [high] `clues.empty` `star-on-the-shore-en/handout/handout-3-statue-drawing` Раздатка 3: рисунок статуи — раздатка без текста и картинки
- [high] `clues.empty` `star-on-the-shore-en/handout/handout-18-deep-one-drawing` Раздатка 18: рисунок глубоководного — раздатка без текста и картинки
- [high] `clues.empty` `star-on-the-shore-en/handout/handout-20-red-symbol` Раздатка 20: красный знак — раздатка без текста и картинки
- [high] `clues.empty` `star-on-the-shore-en/handout/handout-19-star-spawn-drawing` Раздатка 19: рисунок звёздного отродья — раздатка без текста и картинки
- [low] `scenes.no_people` `star-on-the-shore-en/scene/star-dream-2-web` Сон 2: паутина — сцена без участников

### Ключ к Бездне (`star-on-the-shore-en/scenario/key-to-the-abyss`) — 1

- [low] `scenes.no_people` `star-on-the-shore-en/scene/abyss-research` Поиски в оккультной библиотеке — сцена без участников

