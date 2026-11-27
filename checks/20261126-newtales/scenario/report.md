# Целостность сценариев — 2026-11-26

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
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
| Ночная война | `new-tales-miskatonic-valley-2e-en` | 122–143 | 30 | 19 (6) | 8 (3) | 2 (2) | 2 | 20 | 0 | 0 | 4 |
| Загубленная юность | `new-tales-miskatonic-valley-2e-en` | 29–54 | 27 | 53 (9) | 9 (2) | 4 (4) | 6 | 24 | 4 | 0 | 1 |
| Вечная злоба | `new-tales-miskatonic-valley-2e-en` | 101–121 | 16 | 34 (7) | 4 (1) | 6 (6) | 6 | 29 | 2 | 0 | 0 |
| Доказательство жизни | `new-tales-miskatonic-valley-2e-en` | 74–100 | 21 | 35 (7) | 5 (1) | 3 (3) | 13 | 30 | 5 | 0 | 0 |
| Дух предприятия | `new-tales-miskatonic-valley-2e-en` | 55–68 | 18 | 33 (7) | 1 (0) | 2 (2) | 5 | 32 | 4 | 0 | 0 |
| Шальная полночь | `new-tales-miskatonic-valley-2e-en` | 9–28 | 24 | 45 (12) | 4 (2) | 5 (5) | 6 | 43 | 2 | 0 | 0 |

## Находки по сценариям

### Ночная война (`new-tales-miskatonic-valley-2e-en/scenario/the-night-war`) — 4

- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-medical-tent` В медицинской палатке — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-artillery` Артобстрел — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-nightmare-ends` Конец первого кошмара — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-gas` Газ! — сцена без участников

### Загубленная юность (`new-tales-miskatonic-valley-2e-en/scenario/wasted-youth`) — 1

- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/youth-talking-to-students` Разговоры с другими учениками — сцена без участников

