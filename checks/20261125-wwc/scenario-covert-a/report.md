# Целостность сценариев — 2026-11-25

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 6 |
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
| Операция «Хедер» | `wwc-covert-actions-en` | 122–147 | 15 | 35 (13) | 4 (4) | 3 (0) | 7 | 18 | 1 | 0 | 4 |
| Каденция | `wwc-covert-actions-en` | 63–92 | 24 | 20 (8) | 4 (2) | 4 (4) | 8 | 19 | 3 | 0 | 1 |
| Нечистая сила | `wwc-covert-actions-en` | 150–172 | 16 | 18 (7) | 2 (2) | 4 (4) | 12 | 16 | 0 | 0 | 1 |
| Стражи леса | `wwc-covert-actions-en` | 94–120 | 18 | 25 (16) | 3 (3) | 1 (0) | 9 | 13 | 0 | 0 | 0 |
| Лужи становятся озёрами | `wwc-covert-actions-en` | 7–26 | 16 | 15 (6) | 4 (3) | 10 (10) | 9 | 19 | 0 | 0 | 0 |
| Форсирующий ход | `wwc-covert-actions-en` | 35–60 | 13 | 20 (11) | 1 (1) | 1 (1) | 2 | 16 | 0 | 0 | 0 |

## Находки по сценариям

### Операция «Хедер» (`wwc-covert-actions-en/scenario/operation-header`) — 4

- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-official-briefing` Официальный брифинг в Лэнгли — сцена без места
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-n-mission` Миссия N: курьер «Хедер» — сцена без места
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-h-mission` Миссия H — сцена без места
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-debriefing` Отчёт — сцена без места

### Каденция (`wwc-covert-actions-en/scenario/cadenza`) — 1

- [low] `scenes.no_place` `wwc-covert-actions-en/scene/cadenza-court-of-azathoth` Двор Азатота — сцена без места

### Нечистая сила (`wwc-covert-actions-en/scenario/the-unclean`) — 1

- [low] `scenes.no_place` `wwc-covert-actions-en/scene/unclean-meeting-arkhiv` Встреча с Архивом — сцена без места

