# Целостность сценариев — 2026-11-25

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 6 |
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
| Набросок 1: Призраки Винегар-Хилла | `convicts-cthulhu-en` | 77–78 | 0 | 5 (0) | 2 (2) | 0 (0) | 1 | 6 | 0 | 0 | 1 |
| Набросок 2: Огни Ботани-Бей | `convicts-cthulhu-en` | 79–82 | 0 | 7 (0) | 2 (2) | 0 (0) | 3 | 4 | 0 | 0 | 1 |
| Набросок 3: Призраки Севера | `convicts-cthulhu-en` | 83–84 | 0 | 6 (0) | 3 (3) | 0 (0) | 0 | 4 | 0 | 0 | 1 |
| Набросок 4: Губительное наводнение | `convicts-cthulhu-en` | 85–86 | 0 | 3 (0) | 3 (3) | 0 (0) | 1 | 2 | 0 | 0 | 1 |
| Набросок 5: Чудовище глубинки | `convicts-cthulhu-en` | 87–88 | 0 | 0 (0) | 2 (2) | 0 (0) | 0 | 2 | 0 | 0 | 1 |
| Набросок 6: Сон за сном | `convicts-cthulhu-en` | 87–90 | 0 | 1 (0) | 5 (4) | 0 (0) | 1 | 1 | 0 | 0 | 1 |
| Неласковый приём | `convicts-cthulhu-en` | 66–75 | 11 | 10 (1) | 3 (3) | 4 (2) | 1 | 14 | 1 | 0 | 1 |

## Находки по сценариям

### Набросок 1: Призраки Винегар-Хилла (`convicts-cthulhu-en/scenario/seed-1-the-ghosts-of-vinegar-hill`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Набросок 2: Огни Ботани-Бей (`convicts-cthulhu-en/scenario/seed-2-the-lights-of-botany-bay`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Набросок 3: Призраки Севера (`convicts-cthulhu-en/scenario/seed-3-ghosts-of-the-north`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Набросок 4: Губительное наводнение (`convicts-cthulhu-en/scenario/seed-4-the-baleful-flood`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Набросок 5: Чудовище глубинки (`convicts-cthulhu-en/scenario/seed-5-the-hinterland-monster`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Набросок 6: Сон за сном (`convicts-cthulhu-en/scenario/seed-6-dream-sequence`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Неласковый приём (`convicts-cthulhu-en/scenario/un-fresh-off-the-boat`) — 1

- [low] `scenes.no_people` `convicts-cthulhu-en/scene/the-powder-magazine` Пороховой погреб — сцена без участников

