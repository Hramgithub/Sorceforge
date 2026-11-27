# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 1 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 3 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 6 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 1 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Изъятие: София, 1923 | `hotoe-book-4-en` | 10–40 | 19 | 27 (4) | 2 (0) | 1 (1) | 9 | 25 | 7 | 1 | 11 |

## Находки по сценариям

### Изъятие: София, 1923 (`hotoe-book-4-en/scenario/repossession`) — 11

- [high] `plot.bad_ref` шаг «Дальше — Константинополь» → hotoe-book-4-en/scenario/by-the-skin-of-the-teeth
- [low] `pages.gap` страницы без записей: физ. 37
- [low] `scenes.no_outcome` `hotoe-book-4-en/scene/sofia-last-night-on-the-orient-express` Последняя ночь в «Восточном экспрессе» — сцена без итога
- [low] `scenes.no_outcome` `hotoe-book-4-en/scene/sofia-fenalik-strikes` Массовое убийство в «Восточном экспрессе» — сцена без итога
- [low] `scenes.no_outcome` `hotoe-book-4-en/scene/sofia-vampire-at-bay` Вампир загнан — сцена без итога
- [low] `scenes.no_outcome` `hotoe-book-4-en/scene/sofia-hotel-ambush` Засада в гостинице — сцена без итога
- [low] `scenes.no_outcome` `hotoe-book-4-en/scene/sofia-other-train-ambush` Засада в другом поезде — сцена без итога
- [low] `scenes.no_outcome` `hotoe-book-4-en/scene/sofia-roadside-ambush` Засада на дороге — сцена без итога
- [low] `scenes.no_people` `hotoe-book-4-en/scene/sofia-library-research` Работа в библиотеке — сцена без участников
- [low] `scenes.no_people` `hotoe-book-4-en/scene/sofia-last-night-on-the-orient-express` Последняя ночь в «Восточном экспрессе» — сцена без участников
- [low] `scenes.no_people` `hotoe-book-4-en/scene/sofia-conclusion` Заключение — сцена без участников

