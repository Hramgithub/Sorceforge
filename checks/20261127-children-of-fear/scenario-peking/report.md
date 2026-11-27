# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 24 |
| `scenes.none` | У сценария нет сцен | 1 |
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
| Дети страха | `children-of-fear-en` | 324–324 | 0 | 4 (0) | 6 (5) | 0 (0) | 0 | 9 | 2 | 0 | 22 |
| Глава 1. Город увядающего великолепия | `children-of-fear-en` | 36–48 | 10 | 7 (0) | 0 (0) | 5 (0) | 4 | 24 | 2 | 0 | 4 |

## Находки по сценариям

### Дети страха (`children-of-fear-en/scenario/the-children-of-fear`) — 22

- [high] `plot.bad_ref` шаг «Глава 2. К Вратам Солнца (Сиань и Дуньхуан)» → children-of-fear-en/scenario/to-the-gates-of-the-sun
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → children-of-fear-en/scenario/song-of-the-lost-and-forgotten
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → children-of-fear-en/location/song-tarim-basin
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → children-of-fear-en/location/song-mountain-passes
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → coc:location:chakdara
- [high] `plot.bad_ref` шаг «Глава 3. Песнь потерянного и забытого (Такла-Макан, Гандхара; главы 3–5 — в любом порядке)» → coc:location:peshawar
- [high] `plot.bad_ref` шаг «Глава 4. Старые кости (Раджгир, Бихар и Орисса; в любом порядке с главами 3 и 5)» → children-of-fear-en/scenario/old-bones
- [high] `plot.bad_ref` шаг «Глава 4. Старые кости (Раджгир, Бихар и Орисса; в любом порядке с главами 3 и 5)» → coc:location:rajgir
- [high] `plot.bad_ref` шаг «Глава 4. Старые кости (Раджгир, Бихар и Орисса; в любом порядке с главами 3 и 5)» → children-of-fear-en/location/bones-rajgir-environs
- [high] `plot.bad_ref` шаг «Глава 5. Пир и голод (Дерге, Кам, Тибет; в любом порядке с главами 3 и 4)» → children-of-fear-en/scenario/feast-and-famine
- [high] `plot.bad_ref` шаг «Глава 5. Пир и голод (Дерге, Кам, Тибет; в любом порядке с главами 3 и 4)» → coc:location:derge
- [high] `plot.bad_ref` шаг «Глава 5. Пир и голод (Дерге, Кам, Тибет; в любом порядке с главами 3 и 4)» → children-of-fear-en/location/feast-kham
- [high] `plot.bad_ref` шаг «Глава 6. Освобождение (Пемакё, Тибет)» → children-of-fear-en/scenario/liberation
- [high] `plot.bad_ref` шаг «Глава 6. Освобождение (Пемакё, Тибет)» → children-of-fear-en/creature/liberation-lords-of-shambhala
- [high] `plot.bad_ref` шаг «Глава 7. Духи земли (Наланда и Патна)» → children-of-fear-en/scenario/spirits-of-the-earth
- [high] `plot.bad_ref` шаг «Глава 7. Духи земли (Наланда и Патна)» → children-of-fear-en/location/spirits-nalanda
- [high] `plot.bad_ref` шаг «Глава 7. Духи земли (Наланда и Патна)» → coc:location:patna
- [high] `plot.bad_ref` шаг «Глава 8. Сердце мира (Ассам)» → children-of-fear-en/scenario/the-heart-of-the-world
- [high] `plot.bad_ref` шаг «Глава 8. Сердце мира (Ассам)» → children-of-fear-en/location/heart-assam
- [high] `plot.bad_ref` шаг «Приложения» → coc:spell:open-the-gates-of-agartha
- [high] `plot.bad_ref` шаг «Приложения» → coc:spell:send-vision
- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Глава 1. Город увядающего великолепия (`children-of-fear-en/scenario/the-city-of-decaying-splendor`) — 4

- [high] `plot.bad_ref` шаг «Опоздавшие» → children-of-fear-en/character/sofian-bazaz-wain
- [high] `plot.bad_ref` шаг «Видения во тьме» → coc:spell:send-vision
- [high] `plot.bad_ref` шаг «В дорогу (дальше — глава 2)» → children-of-fear-en/scenario/to-the-gates-of-the-sun
- [low] `scenes.no_people` `children-of-fear-en/scene/peking-an-unseasonable-storm` Необычный град — сцена без участников

