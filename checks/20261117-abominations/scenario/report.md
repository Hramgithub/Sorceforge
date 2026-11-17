# Целостность сценариев — 2026-11-17

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
| Адский отель | `petersens-abominations-en` | 11–35 | 16 | 13 (7) | 4 (3) | 5 (5) | 10 | 35 | 5 | 0 | 3 |
| Голос в трубке | `petersens-abominations-en` | 154–179 | 19 | 42 (12) | 9 (9) | 2 (2) | 9 | 16 | 5 | 0 | 2 |
| Кошмары цифровой эпохи | `petersens-abominations-en` | 1–7 | 0 | 0 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 1 |
| Мохол | `petersens-abominations-en` | 109–138 | 19 | 30 (12) | 3 (3) | 1 (1) | 8 | 34 | 2 | 0 | 0 |
| Панацея | `petersens-abominations-en` | 74–98 | 22 | 28 (12) | 7 (4) | 2 (2) | 9 | 42 | 2 | 0 | 0 |
| Заброшенный корабль | `the-derelict-en` | 5–23 | 11 | 18 (12) | 1 (1) | 1 (1) | 14 | 23 | 3 | 0 | 0 |

## Находки по сценариям

### Адский отель (`petersens-abominations-en/scenario/hotel-hell`) — 3

- [low] `scenes.no_people` `petersens-abominations-en/scene/hotel-ground-floor` Отель: первый этаж — сцена без участников
- [low] `scenes.no_people` `petersens-abominations-en/scene/hotel-hoodoo-mountain` Поход к горе Худу — сцена без участников
- [low] `scenes.no_people` `petersens-abominations-en/scene/hotel-prospector-cabins` Старательские хижины — сцена без участников

### Голос в трубке (`petersens-abominations-en/scenario/voice-over-the-phone`) — 2

- [low] `scenes.no_people` `petersens-abominations-en/scene/voice-analyzing-green-fluid` Анализ зелёной жидкости — сцена без участников
- [low] `scenes.no_people` `petersens-abominations-en/scene/voice-vehicular-revelations` Что рассказали машины — сцена без участников

### Кошмары цифровой эпохи (`petersens-abominations-en/scenario/petersens-abominations`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

