# Целостность сценариев — 2026-11-16

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 9 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| В плену тумана | `fogbound-en` | 8–24 | 32 | 23 (5) | 4 (3) | 14 (14) | 12 | 38 | 5 | 0 | 9 |

## Находки по сценариям

### В плену тумана (`fogbound-en/scenario/fogbound`) — 9

- [low] `scenes.no_people` `fogbound-en/scene/daniels-flat-search` Обыск квартиры Дэниела — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/researching-porthollow` Сведения о Портхоллоу — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/entering-porthollow` Въезд в Портхоллоу — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/there-is-no-escape` Выхода нет — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/sleeping-in-porthollow` Сон в Портхоллоу — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/daniels-cottage-search` Обыск коттеджа Дэниела — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/cattle-barn` Коровник — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/the-caves` Пещеры и потайная дверь — сцена без участников
- [low] `scenes.no_people` `fogbound-en/scene/tunnel-traps` Ловушки туннелей — сцена без участников

