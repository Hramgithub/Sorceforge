# Целостность сценариев — 2026-11-23

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 16 |
| `scenes.none` | У сценария нет сцен | 0 |
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
| Ключ к Бездне | `star-on-the-shore-en` | 68–76 | 4 | 1 (1) | 9 (1) | 2 (2) | 4 | 3 | 0 | 0 | 17 |

## Находки по сценариям

### Ключ к Бездне (`star-on-the-shore-en/scenario/key-to-the-abyss`) — 17

- [high] `plot.bad_ref` шаг «Просьба преподобного» → star-on-the-shore-en/character/ronald-lynn
- [high] `plot.bad_ref` шаг «Просьба преподобного» → star-on-the-shore-en/location/loc-21-the-old-sloop
- [high] `plot.bad_ref` шаг «Просьба преподобного» → star-on-the-shore-en/scenario/the-star-on-the-shore
- [high] `plot.bad_ref` шаг «Ядро в колокольне» → star-on-the-shore-en/location/loc-21-the-old-sloop
- [high] `plot.bad_ref` шаг «Ядро в колокольне» → star-on-the-shore-en/character/ronald-lynn
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/character/alan-douglas
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/character/christina-smith
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/location/loc-17-old-man-douglass-house
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/location/loc-16-the-witch-house
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/location/loc-3-smith-hardware
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/location/loc-11-granite-pharmacy
- [high] `plot.bad_ref` шаг «Подготовка» → star-on-the-shore-en/location/loc-31-sandy-bay-bakery
- [high] `plot.bad_ref` шаг «Запечатывание разлома» → star-on-the-shore-en/character/alan-douglas
- [high] `plot.bad_ref` шаг «Запечатывание разлома» → star-on-the-shore-en/character/christina-smith
- [high] `plot.bad_ref` шаг «Развязка» → star-on-the-shore-en/character/ronald-lynn
- [high] `plot.bad_ref` шаг «Развязка» → star-on-the-shore-en/scenario/the-star-on-the-shore
- [low] `scenes.no_people` `star-on-the-shore-en/scene/abyss-research` Поиски в оккультной библиотеке — сцена без участников

