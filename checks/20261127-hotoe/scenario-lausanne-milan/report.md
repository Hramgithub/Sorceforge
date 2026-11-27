# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 1 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 14 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Танцоры в вечернем тумане: Лондон, 1923 | `hotoe-book-2-en` | 9–33 | 12 | 9 (4) | 3 (2) | 13 (13) | 6 | 28 | 4 | 0 | 3 |
| Цветы зла: Париж и Пуасси, 1923 | `hotoe-book-2-en` | 103–132 | 19 | 20 (14) | 2 (1) | 9 (9) | 6 | 41 | 7 | 0 | 3 |
| Ноктюрн: Лозанна, 1923 | `hotoe-book-2-en` | 183–207 | 17 | 10 (4) | 0 (0) | 4 (4) | 6 | 21 | 4 | 0 | 3 |
| Нота в ноту: Милан, 1923 | `hotoe-book-2-en` | 213–231 | 11 | 15 (4) | 0 (0) | 5 (5) | 3 | 21 | 4 | 0 | 2 |
| Кроваво-красная феска: Лондон 1893 | `hotoe-book-2-en` | 51–85 | 25 | 44 (5) | 4 (3) | 10 (10) | 8 | 38 | 6 | 0 | 2 |
| Поезд рока: Лондон и окрестности, 1923 | `hotoe-book-2-en` | 34–44 | 10 | 7 (3) | 0 (0) | 1 (1) | 3 | 11 | 0 | 0 | 2 |
| Экспресс Страны грёз: Страна грёз, 1923 | `hotoe-book-2-en` | 134–177 | 24 | 16 (7) | 11 (2) | 7 (7) | 8 | 38 | 4 | 0 | 0 |

## Находки по сценариям

### Танцоры в вечернем тумане: Лондон, 1923 (`hotoe-book-2-en/scenario/dancers-in-an-evening-fog`) — 3

- [low] `scenes.no_people` `hotoe-book-2-en/scene/london-makryats-shop` Лавка Макрьята — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/london-researches` Изыскания в Лондоне — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/london-leaving-england` Отъезд из Англии — сцена без участников

### Цветы зла: Париж и Пуасси, 1923 (`hotoe-book-2-en/scenario/les-fleurs-du-mal`) — 3

- [low] `scenes.no_people` `hotoe-book-2-en/scene/paris-stopping-in-paris` Остановка в Париже — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/paris-poissy-town-hall` Ратуша Пуасси и путь к особняку — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/paris-a-dream-of-trains` Сон о поездах — сцена без участников

### Ноктюрн: Лозанна, 1923 (`hotoe-book-2-en/scenario/nocturne`) — 3

- [low] `scenes.no_people` `hotoe-book-2-en/scene/lausanne-taking-the-drug` Наркотик снов — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/lausanne-dream-wasteland` Поезд сна и пустошь — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/lausanne-waking-world` Мир яви — сцена без участников

### Нота в ноту: Милан, 1923 (`hotoe-book-2-en/scenario/note-for-note`) — 2

- [low] `scenes.no_people` `hotoe-book-2-en/scene/milan-centro` Центр Милана — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/milan-the-performance` Утро премьеры — сцена без участников

### Кроваво-красная феска: Лондон 1893 (`hotoe-book-2-en/scenario/the-blood-red-fez`) — 2

- [high] `plot.bad_ref` шаг «Братья кожи» → hotoe-book-4-en/character/selim-makryat
- [low] `scenes.no_people` `hotoe-book-2-en/scene/fez-british-consul` Британский консул — сцена без участников

### Поезд рока: Лондон и окрестности, 1923 (`hotoe-book-2-en/scenario/the-doom-train`) — 2

- [low] `scenes.no_people` `hotoe-book-2-en/scene/doom-alexis-family` Семья Алексис — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/doom-train-set` Игрушечная железная дорога — сцена без участников

