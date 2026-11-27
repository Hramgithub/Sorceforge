# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 3 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 3 |
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
| Туман рассеивается: снова Лондон, 1923 | `hotoe-book-4-en` | 87–87 | 9 | 12 (2) | 3 (0) | 3 (0) | 4 | 9 | 1 | 0 | 4 |
| Симулякр на свободе: Стамбул, 2013 | `hotoe-book-4-en` | 129–165 | 21 | 20 (2) | 4 (1) | 6 (0) | 14 | 21 | 0 | 0 | 4 |
| На волосок: Константинополь, 1923 | `hotoe-book-4-en` | 41–85 | 27 | 26 (3) | 5 (0) | 4 (1) | 11 | 28 | 4 | 0 | 2 |
| Изъятие: София, 1923 | `hotoe-book-4-en` | 10–40 | 19 | 27 (5) | 2 (1) | 1 (1) | 9 | 25 | 7 | 0 | 1 |
| Синий поезд, чёрная ночь: через Европу, 1923 | `hotoe-book-4-en` | 88–114 | 13 | 21 (4) | 4 (1) | 2 (0) | 10 | 14 | 2 | 0 | 0 |

## Находки по сценариям

### Туман рассеивается: снова Лондон, 1923 (`hotoe-book-4-en/scenario/the-fog-lifts`) — 4

- [low] `scenes.no_people` `hotoe-book-4-en/scene/foglifts-scroll-of-the-left-hand` Свиток Левой руки — сцена без участников
- [low] `scenes.no_people` `hotoe-book-4-en/scene/foglifts-conclusion` Заключение кампании — сцена без участников
- [low] `scenes.no_place` `hotoe-book-4-en/scene/foglifts-what-if-mehmet-escapes` Что, если Мехмет уйдёт? — сцена без места
- [low] `scenes.no_place` `hotoe-book-4-en/scene/foglifts-conclusion` Заключение кампании — сцена без места

### Симулякр на свободе: Стамбул, 2013 (`hotoe-book-4-en/scenario/the-simulacrum-unbound`) — 4

- [high] `plot.bad_ref` шаг «Поезд 2013 года» → hotoe-book-4-en/map/modern-sleeper-cars
- [high] `plot.bad_ref` шаг «Развязка в Отверженной мечети» → hotoe-book-4-en/map/modern-shunned-mosque
- [high] `plot.bad_ref` шаг «Развязка в Отверженной мечети» → hotoe-book-4-en/map/modern-istanbul-today
- [low] `scenes.no_place` `hotoe-book-4-en/scene/modern-a-request-for-help` Просьба о помощи — сцена без места

### На волосок: Константинополь, 1923 (`hotoe-book-4-en/scenario/by-the-skin-of-the-teeth`) — 2

- [low] `scenes.no_people` `hotoe-book-4-en/scene/constantinople-arrival` Прибытие в Константинополь — сцена без участников
- [low] `scenes.no_people` `hotoe-book-4-en/scene/constantinople-police` Полиция — сцена без участников

### Изъятие: София, 1923 (`hotoe-book-4-en/scenario/repossession`) — 1

- [low] `scenes.no_people` `hotoe-book-4-en/scene/sofia-library-research` Работа в библиотеке — сцена без участников

