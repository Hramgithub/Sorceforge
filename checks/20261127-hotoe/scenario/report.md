# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 1 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 30 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Танцоры в вечернем тумане: Лондон, 1923 | `hotoe-book-2-en` | 9–33 | 12 | 10 (5) | 3 (2) | 13 (13) | 6 | 30 | 4 | 0 | 3 |
| Цветы зла: Париж и Пуасси, 1923 | `hotoe-book-2-en` | 103–132 | 19 | 20 (14) | 2 (1) | 9 (9) | 6 | 41 | 7 | 0 | 3 |
| Ноктюрн: Лозанна, 1923 | `hotoe-book-2-en` | 183–207 | 17 | 11 (5) | 0 (0) | 4 (4) | 6 | 21 | 4 | 0 | 3 |
| Нота в ноту: Милан, 1923 | `hotoe-book-2-en` | 213–231 | 11 | 16 (4) | 0 (0) | 5 (5) | 3 | 21 | 4 | 0 | 2 |
| Поезд рока: Лондон и окрестности, 1923 | `hotoe-book-2-en` | 34–44 | 10 | 8 (5) | 0 (0) | 1 (1) | 3 | 11 | 0 | 0 | 2 |
| Дует холодный ветер: Триест, 1923 | `hotoe-book-3-en` | 86–115 | 22 | 18 (4) | 4 (3) | 5 (5) | 5 | 18 | 4 | 0 | 2 |
| Смерть (и любовь) в гондоле: Венеция, 1923 | `hotoe-book-3-en` | 9–40 | 25 | 23 (7) | 1 (1) | 4 (4) | 4 | 32 | 6 | 0 | 2 |
| В городе колоколов и башен | `hotoe-book-3-en` | 119–128 | 7 | 7 (6) | 2 (1) | 10 (10) | 2 | 22 | 2 | 0 | 2 |
| Избушка в лесу: Белград и Орашац, 1923 | `hotoe-book-3-en` | 205–238 | 21 | 22 (5) | 4 (3) | 1 (1) | 4 | 24 | 3 | 0 | 2 |
| Тёмный крестоносец | `hotoe-book-3-en` | 51–73 | 23 | 24 (5) | 3 (2) | 2 (2) | 13 | 25 | 5 | 0 | 2 |
| На волосок: Константинополь, 1923 | `hotoe-book-4-en` | 41–85 | 27 | 26 (7) | 5 (0) | 4 (4) | 11 | 28 | 4 | 0 | 2 |
| Туман рассеивается: снова Лондон, 1923 | `hotoe-book-4-en` | 87–87 | 9 | 12 (6) | 3 (1) | 3 (3) | 4 | 9 | 1 | 0 | 2 |
| Ужас в Восточном экспрессе | `hotoe-book-1-en` | 60–60 | 0 | 17 (15) | 7 (5) | 6 (6) | 9 | 15 | 0 | 0 | 1 |
| Кроваво-красная феска: Лондон 1893 | `hotoe-book-2-en` | 51–85 | 25 | 45 (6) | 4 (3) | 10 (10) | 8 | 49 | 6 | 0 | 1 |
| Хлеб и камень | `hotoe-book-3-en` | 135–163 | 18 | 28 (4) | 2 (1) | 8 (8) | 8 | 30 | 4 | 0 | 1 |
| Изъятие: София, 1923 | `hotoe-book-4-en` | 10–40 | 19 | 27 (6) | 2 (1) | 1 (1) | 9 | 25 | 7 | 0 | 1 |
| Экспресс Страны грёз: Страна грёз, 1923 | `hotoe-book-2-en` | 134–177 | 24 | 16 (7) | 11 (2) | 7 (7) | 8 | 38 | 4 | 0 | 0 |
| Sanguis Omnia Vincet: Константинополь, 330 год | `hotoe-book-3-en` | 167–196 | 23 | 25 (5) | 8 (4) | 2 (2) | 1 | 39 | 4 | 0 | 0 |
| Синий поезд, чёрная ночь: через Европу, 1923 | `hotoe-book-4-en` | 88–114 | 13 | 21 (17) | 6 (3) | 2 (2) | 10 | 14 | 2 | 0 | 0 |
| Симулякр на свободе: Стамбул, 2013 | `hotoe-book-4-en` | 129–165 | 21 | 20 (3) | 4 (1) | 6 (6) | 14 | 22 | 4 | 0 | 0 |

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

### Поезд рока: Лондон и окрестности, 1923 (`hotoe-book-2-en/scenario/the-doom-train`) — 2

- [low] `scenes.no_people` `hotoe-book-2-en/scene/doom-alexis-family` Семья Алексис — сцена без участников
- [low] `scenes.no_people` `hotoe-book-2-en/scene/doom-train-set` Игрушечная железная дорога — сцена без участников

### Дует холодный ветер: Триест, 1923 (`hotoe-book-3-en/scenario/cold-wind-blowing`) — 2

- [low] `scenes.no_people` `hotoe-book-3-en/scene/trieste-arriving` Прибытие в Триест — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/trieste-looking-up-winckelmann` Поиски Винкельмана — сцена без участников

### Смерть (и любовь) в гондоле: Венеция, 1923 (`hotoe-book-3-en/scenario/death-and-love-in-a-gondola`) — 2

- [low] `scenes.no_people` `hotoe-book-3-en/scene/venice-the-latin-manuscript` Латинская рукопись — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/venice-researching-the-gremancis` Изыскания о Гременчи — сцена без участников

### В городе колоколов и башен (`hotoe-book-3-en/scenario/in-a-city-of-bells-and-towers`) — 2

- [low] `scenes.no_people` `hotoe-book-3-en/scene/zagreb-a-gift` Подарок — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/zagreb-what-they-meet` Что они встречают — сцена без участников

### Избушка в лесу: Белград и Орашац, 1923 (`hotoe-book-3-en/scenario/little-cottage-in-the-wood`) — 2

- [low] `scenes.no_people` `hotoe-book-3-en/scene/belgrade-into-the-woods` В лес — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/belgrade-making-a-connection` Как добраться до поезда — сцена без участников

### Тёмный крестоносец (`hotoe-book-3-en/scenario/the-dark-crusader`) — 2

- [low] `scenes.no_people` `hotoe-book-3-en/scene/crusader-drunken-rabble` Пьяный сброд — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/crusader-crypt-and-tunnel` Крипта и туннель — сцена без участников

### На волосок: Константинополь, 1923 (`hotoe-book-4-en/scenario/by-the-skin-of-the-teeth`) — 2

- [low] `scenes.no_people` `hotoe-book-4-en/scene/constantinople-arrival` Прибытие в Константинополь — сцена без участников
- [low] `scenes.no_people` `hotoe-book-4-en/scene/constantinople-police` Полиция — сцена без участников

### Туман рассеивается: снова Лондон, 1923 (`hotoe-book-4-en/scenario/the-fog-lifts`) — 2

- [low] `scenes.no_people` `hotoe-book-4-en/scene/foglifts-scroll-of-the-left-hand` Свиток Левой руки — сцена без участников
- [low] `scenes.no_people` `hotoe-book-4-en/scene/foglifts-conclusion` Заключение кампании — сцена без участников

### Ужас в Восточном экспрессе (`hotoe-book-1-en/scenario/horror-on-the-orient-express`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Кроваво-красная феска: Лондон 1893 (`hotoe-book-2-en/scenario/the-blood-red-fez`) — 1

- [low] `scenes.no_people` `hotoe-book-2-en/scene/fez-british-consul` Британский консул — сцена без участников

### Хлеб и камень (`hotoe-book-3-en/scenario/bread-and-stone`) — 1

- [low] `scenes.no_people` `hotoe-book-3-en/scene/vinkovci-crusaders-tomb` Гробница крестоносца — сцена без участников

### Изъятие: София, 1923 (`hotoe-book-4-en/scenario/repossession`) — 1

- [low] `scenes.no_people` `hotoe-book-4-en/scene/sofia-library-research` Работа в библиотеке — сцена без участников

