# Целостность сценариев — 2026-11-25

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 6 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 4 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Фармакопея доктора Макдеда | `convicts-tol-11-en` | 9–22 | 10 | 20 (0) | 3 (2) | 1 (0) | 3 | 14 | 1 | 0 | 2 |
| Набросок 1: Призраки Винегар-Хилла | `convicts-cthulhu-en` | 77–78 | 0 | 5 (0) | 2 (2) | 0 (0) | 1 | 6 | 0 | 0 | 1 |
| Набросок 2: Огни Ботани-Бей | `convicts-cthulhu-en` | 79–82 | 0 | 7 (0) | 2 (2) | 0 (0) | 3 | 4 | 0 | 0 | 1 |
| Набросок 3: Призраки Севера | `convicts-cthulhu-en` | 83–84 | 0 | 6 (0) | 3 (3) | 0 (0) | 0 | 4 | 0 | 0 | 1 |
| Набросок 4: Губительное наводнение | `convicts-cthulhu-en` | 85–86 | 0 | 3 (0) | 3 (3) | 0 (0) | 1 | 2 | 0 | 0 | 1 |
| Набросок 5: Чудовище глубинки | `convicts-cthulhu-en` | 87–88 | 0 | 0 (0) | 2 (2) | 0 (0) | 0 | 2 | 0 | 0 | 1 |
| Набросок 6: Сон за сном | `convicts-cthulhu-en` | 87–90 | 0 | 1 (0) | 5 (4) | 0 (0) | 1 | 1 | 0 | 0 | 1 |
| Неласковый приём | `convicts-cthulhu-en` | 66–75 | 11 | 10 (1) | 3 (3) | 4 (2) | 1 | 14 | 1 | 0 | 1 |
| Ночь каторжных мертвецов | `convicts-tol-06-en` | 4–13 | 16 | 6 (0) | 4 (3) | 1 (0) | 4 | 15 | 1 | 0 | 1 |
| Ночные ужасы | `convicts-tol-01-en` | 2–4 | 4 | 9 (0) | 1 (1) | 1 (1) | 1 | 6 | 1 | 0 | 0 |
| Ужас триколора | `convicts-tol-02-en` | 5–6 | 6 | 6 (1) | 3 (3) | 0 (0) | 2 | 3 | 0 | 0 | 0 |
| Сияет, как золото | `convicts-tol-03-en` | 5–8 | 4 | 10 (0) | 2 (1) | 1 (1) | 2 | 8 | 2 | 0 | 0 |
| Великий смотр | `convicts-tol-04-en` | 2–8 | 7 | 7 (2) | 0 (0) | 3 (3) | 0 | 19 | 0 | 0 | 0 |
| Исчезающий прапорщик | `convicts-tol-04-en` | 9–14 | 7 | 6 (1) | 7 (7) | 1 (1) | 5 | 7 | 0 | 0 | 0 |
| Опасные жилы | `convicts-tol-07-en` | 3–12 | 13 | 5 (1) | 5 (1) | 1 (1) | 4 | 8 | 0 | 0 | 0 |
| Джентльмен-преследователь | `convicts-tol-08-en` | 8–20 | 18 | 14 (0) | 1 (1) | 1 (0) | 10 | 16 | 0 | 0 | 0 |
| Ужас сиротской школы | `convicts-tol-09-en` | 8–22 | 10 | 27 (0) | 4 (2) | 0 (0) | 8 | 12 | 1 | 0 | 0 |
| Гибель, пришедшая в Файв-Док | `convicts-tol-10-en` | 3–14 | 10 | 5 (1) | 2 (1) | 0 (0) | 7 | 6 | 1 | 0 | 0 |
| Падшие звёзды | `convicts-tol-12-en` | 8–19 | 10 | 10 (2) | 3 (1) | 0 (0) | 4 | 7 | 1 | 0 | 0 |
| Похоронный звон | `convicts-tol-15-en` | 4–21 | 11 | 13 (0) | 2 (1) | 1 (1) | 8 | 11 | 1 | 0 | 0 |

## Находки по сценариям

### Фармакопея доктора Макдеда (`convicts-tol-11-en/scenario/dispensatory-of-doctor-macdead`) — 2

- [low] `scenes.no_people` `convicts-tol-11-en/scene/travel-to-parramatta` Дорога в Парраматту — сцена без участников
- [low] `scenes.no_people` `convicts-tol-11-en/scene/gossip-and-rumours` Сплетни и слухи Парраматты — сцена без участников

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

### Ночь каторжных мертвецов (`convicts-tol-06-en/scenario/night-of-the-convict-dead`) — 1

- [low] `scenes.no_people` `convicts-tol-06-en/scene/a-dog-named-governor` Пёс по кличке Губернатор — сцена без участников

