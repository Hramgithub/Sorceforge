# Целостность сценариев — 2026-11-26

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 6 |
| `scenes.no_people` | Сцена без участников | 10 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 3 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Пленённая публика | `wwc-london-en` | 146–169 | 26 | 23 (11) | 4 (4) | 12 (2) | 8 | 20 | 3 | 0 | 8 |
| Полуночный восход | `wwc-london-en` | 107–134 | 23 | 21 (6) | 3 (0) | 6 (0) | 6 | 16 | 1 | 0 | 7 |
| Мясная торговля | `wwc-london-en` | 172–185 | 15 | 27 (10) | 3 (1) | 1 (0) | 7 | 13 | 0 | 0 | 4 |

## Находки по сценариям

### Пленённая публика (`wwc-london-en/scenario/captive-audience`) — 8

- [low] `scenes.no_people` `wwc-london-en/scene/ca-newspaper-articles` Газетные заметки и события прошлого — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/ca-researching-henderson-brooks-franklin` Поиски сведений о Хендерсоне, Бруксе и Франклине — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/ca-st-jamess-hall-research` Сент-Джеймс-холл: поиски сведений — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/ca-nashs-home` Дом Нэша — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/ca-researching-graves` Поиски сведений о Грейвсе — сцена без участников
- [low] `scenes.no_place` `wwc-london-en/scene/ca-newspaper-articles` Газетные заметки и события прошлого — сцена без места
- [low] `scenes.no_place` `wwc-london-en/scene/ca-researching-henderson-brooks-franklin` Поиски сведений о Хендерсоне, Бруксе и Франклине — сцена без места
- [low] `scenes.no_place` `wwc-london-en/scene/ca-researching-graves` Поиски сведений о Грейвсе — сцена без места

### Полуночный восход (`wwc-london-en/scenario/midnight-sunrise`) — 7

- [low] `scenes.no_outcome` `wwc-london-en/scene/ms-investigating-booksellers` Расспросы книготорговцев — сцена без итога
- [low] `scenes.no_outcome` `wwc-london-en/scene/ms-optional-encounter` Необязательная встреча: контора N — сцена без итога
- [low] `scenes.no_outcome` `wwc-london-en/scene/ms-aftermath` Последствия: приглашение к N — сцена без итога
- [low] `scenes.no_people` `wwc-london-en/scene/ms-researching-williams` Сведения об Уильямс — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/ms-williams-study` Кабинет Уильямс — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/ms-getting-to-the-warehouse` Дорога к складу сквозь пожар Доклендса — сцена без участников
- [low] `scenes.no_place` `wwc-london-en/scene/ms-researching-williams` Сведения об Уильямс — сцена без места

### Мясная торговля (`wwc-london-en/scenario/the-meat-trade`) — 4

- [low] `scenes.no_people` `wwc-london-en/scene/mt-shelter-and-raid` Убежище и продолжение налёта — сцена без участников
- [low] `scenes.no_people` `wwc-london-en/scene/mt-grace-daggetts-flat` Квартира Грейс Даггет — сцена без участников
- [low] `scenes.no_place` `wwc-london-en/scene/mt-wrapping-things-up` Подведение итогов — сцена без места
- [low] `scenes.no_place` `wwc-london-en/scene/mt-aftermath` Последствия «Мясной торговли» — сцена без места

