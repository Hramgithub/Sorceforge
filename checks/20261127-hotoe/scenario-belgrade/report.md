# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 11 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Дует холодный ветер: Триест, 1923 | `hotoe-book-3-en` | 86–115 | 22 | 18 (3) | 4 (3) | 5 (5) | 5 | 18 | 4 | 0 | 2 |
| Смерть (и любовь) в гондоле: Венеция, 1923 | `hotoe-book-3-en` | 9–40 | 25 | 23 (7) | 1 (1) | 4 (4) | 4 | 32 | 6 | 0 | 2 |
| В городе колоколов и башен | `hotoe-book-3-en` | 119–128 | 7 | 7 (5) | 2 (1) | 10 (10) | 2 | 21 | 2 | 0 | 2 |
| Избушка в лесу: Белград и Орашац, 1923 | `hotoe-book-3-en` | 205–238 | 21 | 22 (5) | 4 (3) | 1 (1) | 4 | 23 | 3 | 0 | 2 |
| Тёмный крестоносец | `hotoe-book-3-en` | 51–73 | 23 | 24 (5) | 3 (2) | 2 (2) | 13 | 25 | 5 | 0 | 2 |
| Хлеб и камень | `hotoe-book-3-en` | 135–163 | 18 | 27 (4) | 2 (1) | 8 (8) | 8 | 30 | 4 | 0 | 1 |
| Sanguis Omnia Vincet: Константинополь, 330 год | `hotoe-book-3-en` | 167–196 | 23 | 25 (5) | 8 (4) | 2 (2) | 1 | 38 | 4 | 0 | 0 |

## Находки по сценариям

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

### Хлеб и камень (`hotoe-book-3-en/scenario/bread-and-stone`) — 1

- [low] `scenes.no_people` `hotoe-book-3-en/scene/vinkovci-crusaders-tomb` Гробница крестоносца — сцена без участников

