# Целостность сценариев — 2026-11-26

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 10 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ночная война | `new-tales-miskatonic-valley-2e-en` | 122–143 | 30 | 13 (0) | 8 (0) | 2 (0) | 2 | 20 | 0 | 0 | 8 |
| Загубленная юность | `new-tales-miskatonic-valley-2e-en` | 29–54 | 27 | 47 (3) | 9 (2) | 4 (4) | 6 | 23 | 4 | 0 | 2 |
| Вечная злоба | `new-tales-miskatonic-valley-2e-en` | 101–121 | 16 | 28 (0) | 4 (1) | 6 (0) | 6 | 29 | 2 | 0 | 0 |
| Доказательство жизни | `new-tales-miskatonic-valley-2e-en` | 74–100 | 21 | 29 (1) | 5 (1) | 3 (3) | 13 | 30 | 5 | 0 | 0 |
| Дух предприятия | `new-tales-miskatonic-valley-2e-en` | 55–68 | 18 | 27 (1) | 1 (0) | 2 (2) | 5 | 32 | 4 | 0 | 0 |

## Находки по сценариям

### Ночная война (`new-tales-miskatonic-valley-2e-en/scenario/the-night-war`) — 8

- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-crossing` Через поля Ночной войны — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-medical-tent` В медицинской палатке — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-artillery` Артобстрел — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-nightmare-ends` Конец первого кошмара — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-stretcher-bearers` Санитары с носилками — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-sentinels` Часовые — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-sniper` Снайпер! — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/nightwar-gas` Газ! — сцена без участников

### Загубленная юность (`new-tales-miskatonic-valley-2e-en/scenario/wasted-youth`) — 2

- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/youth-talking-to-students` Разговоры с другими учениками — сцена без участников
- [low] `scenes.no_people` `new-tales-miskatonic-valley-2e-en/scene/youth-meeting-the-families` Встречи с семьями — сцена без участников

