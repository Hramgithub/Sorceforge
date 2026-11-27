# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 4 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 6 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Тёмный крестоносец | `hotoe-book-3-en` | 51–73 | 23 | 23 (1) | 3 (0) | 2 (0) | 12 | 24 | 5 | 0 | 4 |
| Дует холодный ветер: Триест, 1923 | `hotoe-book-3-en` | 86–115 | 22 | 17 (1) | 4 (2) | 5 (0) | 5 | 18 | 4 | 0 | 3 |
| В городе колоколов и башен | `hotoe-book-3-en` | 119–128 | 7 | 7 (1) | 2 (1) | 10 (0) | 2 | 21 | 2 | 0 | 3 |

## Находки по сценариям

### Тёмный крестоносец (`hotoe-book-3-en/scenario/the-dark-crusader`) — 4

- [high] `plot.bad_ref` шаг «Раздатки «Симуларе дьявола» (1923)» → hotoe-book-3-en/scenario/death-and-love-in-a-gondola
- [high] `plot.bad_ref` шаг «Уход из башни и награда» → hotoe-book-3-en/scenario/bread-and-stone
- [low] `scenes.no_people` `hotoe-book-3-en/scene/crusader-drunken-rabble` Пьяный сброд — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/crusader-crypt-and-tunnel` Крипта и туннель — сцена без участников

### Дует холодный ветер: Триест, 1923 (`hotoe-book-3-en/scenario/cold-wind-blowing`) — 3

- [high] `plot.bad_ref` шаг «Заключение» → hotoe-book-3-en/scenario/little-cottage-in-the-wood
- [low] `scenes.no_people` `hotoe-book-3-en/scene/trieste-arriving` Прибытие в Триест — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/trieste-looking-up-winckelmann` Поиски Винкельмана — сцена без участников

### В городе колоколов и башен (`hotoe-book-3-en/scenario/in-a-city-of-bells-and-towers`) — 3

- [high] `plot.bad_ref` шаг «Дальше: Винковци» → hotoe-book-3-en/scenario/bread-and-stone
- [low] `scenes.no_people` `hotoe-book-3-en/scene/zagreb-a-gift` Подарок — сцена без участников
- [low] `scenes.no_people` `hotoe-book-3-en/scene/zagreb-what-they-meet` Что они встречают — сцена без участников

