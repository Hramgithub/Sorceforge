# Целостность сценариев — 2026-11-16

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 6 |
| `scenes.none` | У сценария нет сцен | 1 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 1 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Готика газового света | `gothic-by-gaslight-en` | 1–5 | 0 | 19 (8) | 0 (0) | 0 (0) | 1 | 3 | 1 | 0 | 6 |
| Прятки с Хайдом | `gothic-by-gaslight-en` | 17–20 | 10 | 22 (4) | 0 (0) | 1 (1) | 5 | 7 | 1 | 0 | 2 |

## Находки по сценариям

### Готика газового света (`gothic-by-gaslight-en/scenario/gothic-by-gaslight`) — 6

- [high] `plot.bad_ref` шаг ««Дитя Франкенштейна» (1887)» → gothic-by-gaslight-en/scenario/the-childe-of-frankenstein
- [high] `plot.bad_ref` шаг ««Дитя Франкенштейна» (1887)» → gothic-by-gaslight-en/location/book-club-library
- [high] `plot.bad_ref` шаг ««Леди Немо» (1894)» → gothic-by-gaslight-en/scenario/lady-nemo
- [high] `plot.bad_ref` шаг ««Графиня» (1896)» → gothic-by-gaslight-en/scenario/the-countess
- [high] `plot.bad_ref` шаг ««Графиня» (1896)» → gothic-by-gaslight-en/character/the-countess
- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Прятки с Хайдом (`gothic-by-gaslight-en/scenario/hyde-and-seek`) — 2

- [high] `plot.bad_ref` шаг «Акт II: по следу Хайда» → gothic-by-gaslight-en/location/book-club-library
- [low] `scenes.no_people` `gothic-by-gaslight-en/scene/hyde-act-2-jekyll-home` Акт II: дом доктора Джекила — сцена без участников

