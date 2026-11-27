# Целостность сценариев — 2026-11-27

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 26 |
| `scenes.none` | У сценария нет сцен | 1 |
| `scenes.no_place` | Сцена без места | 0 |
| `scenes.no_people` | Сцена без участников | 0 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 0 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ужас в Восточном экспрессе | `hotoe-book-1-en` | 60–60 | 0 | 3 (1) | 7 (5) | 6 (6) | 9 | 9 | 0 | 0 | 27 |

## Находки по сценариям

### Ужас в Восточном экспрессе (`hotoe-book-1-en/scenario/horror-on-the-orient-express`) — 27

- [high] `plot.bad_ref` шаг «Глава 3. «Кроваво-красная феска» (Лондон, 1893)» → hotoe-book-2-en/scenario/the-blood-red-fez
- [high] `plot.bad_ref` шаг «Глава 3. «Кроваво-красная феска» (Лондон, 1893)» → hotoe-book-4-en/character/selim-makryat
- [high] `plot.bad_ref` шаг «Глава 4. «Цветы зла» (Париж и Пуасси, 1923)» → hotoe-book-2-en/scenario/les-fleurs-du-mal
- [high] `plot.bad_ref` шаг «Глава 5. «Экспресс Страны грёз» (Страна грёз, 1923)» → hotoe-book-2-en/scenario/the-dreamlands-express
- [high] `plot.bad_ref` шаг «Глава 6. «Ноктюрн» (Лозанна, 1923)» → hotoe-book-2-en/scenario/nocturne
- [high] `plot.bad_ref` шаг «Глава 6. «Ноктюрн» (Лозанна, 1923)» → coc:location:lausanne
- [high] `plot.bad_ref` шаг «Глава 6. «Ноктюрн» (Лозанна, 1923)» → coc:tome:scroll-of-the-head
- [high] `plot.bad_ref` шаг «Глава 7. «Нота в ноту» (Милан, 1923)» → hotoe-book-2-en/scenario/note-for-note
- [high] `plot.bad_ref` шаг «Глава 8. «Смерть (и любовь) в гондоле» (Венеция, 1923)» → hotoe-book-3-en/scenario/death-and-love-in-a-gondola
- [high] `plot.bad_ref` шаг «Глава 9. «Тёмный крестоносец» (Константинополь, 1204)» → hotoe-book-3-en/scenario/the-dark-crusader
- [high] `plot.bad_ref` шаг «Глава 9. «Тёмный крестоносец» (Константинополь, 1204)» → hotoe-book-3-en/character/sedefkar
- [high] `plot.bad_ref` шаг «Глава 10. «Дует холодный ветер» (Триест, 1923)» → hotoe-book-3-en/scenario/cold-wind-blowing
- [high] `plot.bad_ref` шаг «Глава 10. «Дует холодный ветер» (Триест, 1923)» → coc:location:trieste
- [high] `plot.bad_ref` шаг «Глава 12. «Хлеб и камень» (Винковци, 1923)» → hotoe-book-3-en/scenario/bread-and-stone
- [high] `plot.bad_ref` шаг «Глава 12. «Хлеб и камень» (Винковци, 1923)» → coc:location:vinkovci
- [high] `plot.bad_ref` шаг «Глава 13. «Sanguis Omnia Vincet» (Константинополь, 330)» → hotoe-book-3-en/scenario/sanguis-omnia-vincet
- [high] `plot.bad_ref` шаг «Глава 14. «Избушка в лесу» (Белград и Орашац, 1923)» → hotoe-book-3-en/scenario/little-cottage-in-the-wood
- [high] `plot.bad_ref` шаг «Глава 14. «Избушка в лесу» (Белград и Орашац, 1923)» → coc:location:belgrade
- [high] `plot.bad_ref` шаг «Глава 14. «Избушка в лесу» (Белград и Орашац, 1923)» → coc:location:orasac
- [high] `plot.bad_ref` шаг «Глава 15. «Изъятие» (София, 1923)» → hotoe-book-4-en/scenario/repossession
- [high] `plot.bad_ref` шаг «Глава 15. «Изъятие» (София, 1923)» → coc:location:sofia
- [high] `plot.bad_ref` шаг «Глава 16. «На волосок» (Константинополь, 1923)» → hotoe-book-4-en/scenario/by-the-skin-of-the-teeth
- [high] `plot.bad_ref` шаг «Глава 16. «На волосок» (Константинополь, 1923)» → hotoe-book-4-en/character/selim-makryat
- [high] `plot.bad_ref` шаг «Глава 17. «Синий поезд, чёрная ночь» (через Европу, 1923)» → hotoe-book-4-en/scenario/blue-train-black-night
- [high] `plot.bad_ref` шаг «Глава 18. «Туман рассеивается» (снова Лондон, 1923)» → hotoe-book-4-en/scenario/the-fog-lifts
- [high] `plot.bad_ref` шаг «Глава 19. «Освобождённый Симулякр» (Стамбул, 2013)» → hotoe-book-4-en/scenario/the-simulacrum-unbound
- [high] `scenes.none` у сценария нет сцен (arc.scenario)

