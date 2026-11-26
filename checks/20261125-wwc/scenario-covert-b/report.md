# Целостность сценариев — 2026-11-25

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 0 |
| `scenes.no_place` | Сцена без места | 6 |
| `scenes.no_people` | Сцена без участников | 6 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 18 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Каденция | `wwc-covert-actions-en` | 63–92 | 24 | 20 (0) | 4 (2) | 4 (0) | 8 | 19 | 3 | 0 | 17 |
| Форсирующий ход | `wwc-covert-actions-en` | 35–60 | 13 | 20 (0) | 1 (1) | 1 (0) | 2 | 16 | 0 | 0 | 5 |
| Операция «Хедер» | `wwc-covert-actions-en` | 122–147 | 15 | 35 (13) | 4 (4) | 3 (0) | 7 | 18 | 1 | 0 | 4 |
| Лужи становятся озёрами | `wwc-covert-actions-en` | 7–26 | 16 | 15 (0) | 4 (3) | 10 (0) | 9 | 19 | 0 | 0 | 3 |
| Нечистая сила | `wwc-covert-actions-en` | 150–172 | 16 | 18 (7) | 2 (2) | 4 (4) | 12 | 16 | 0 | 0 | 1 |
| Стражи леса | `wwc-covert-actions-en` | 94–120 | 18 | 25 (16) | 3 (3) | 1 (0) | 9 | 13 | 0 | 0 | 0 |

## Находки по сценариям

### Каденция (`wwc-covert-actions-en/scenario/cadenza`) — 17

- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-limassol-travel` Дорога в Лимасол — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-shq` Штаб базы: архив и кабинет Найта — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-armoury` Арсенал — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-infirmary` Лазарет — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-numbers-station` Станция чисел — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-fredericks-barracks` Казарма Фредерикса и Сэндфорд — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-questioning-howland` Допрос Хауленд — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-questioning-fredericks` Допрос Фредерикса — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-refugees-technical-problems` Беженцы и нарастающие сбои — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-meeting-zann` Встреча с Цанном — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-servitor` Служитель Внешних богов — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-taking-fredericks-place` Занять место Фредерикса — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/cadenza-court-of-azathoth` Двор Азатота — сцена без итога
- [low] `scenes.no_people` `wwc-covert-actions-en/scene/cadenza-briefing` Инструктаж в Сенчури-хаусе — сцена без участников
- [low] `scenes.no_people` `wwc-covert-actions-en/scene/cadenza-dikmen-gallery` Галерея Дикмена — сцена без участников
- [low] `scenes.no_people` `wwc-covert-actions-en/scene/cadenza-refugees-technical-problems` Беженцы и нарастающие сбои — сцена без участников
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/cadenza-court-of-azathoth` Двор Азатота — сцена без места

### Форсирующий ход (`wwc-covert-actions-en/scenario/the-forcing-move`) — 5

- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/forcing-safe-house` Конспиративная ферма — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/forcing-hotel-esja` Гостиница «Эсья» — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/forcing-laugardalsholl` Лаугардальсхёлль: матч века — сцена без итога
- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/forcing-keeping-things-moving` Как держать темп — сцена без итога
- [low] `scenes.no_people` `wwc-covert-actions-en/scene/forcing-safe-house` Конспиративная ферма — сцена без участников

### Операция «Хедер» (`wwc-covert-actions-en/scenario/operation-header`) — 4

- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-official-briefing` Официальный брифинг в Лэнгли — сцена без места
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-n-mission` Миссия N: курьер «Хедер» — сцена без места
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-h-mission` Миссия H — сцена без места
- [low] `scenes.no_place` `wwc-covert-actions-en/scene/header-debriefing` Отчёт — сцена без места

### Лужи становятся озёрами (`wwc-covert-actions-en/scenario/puddles-become-lakes`) — 3

- [low] `scenes.no_outcome` `wwc-covert-actions-en/scene/puddles-researching-the-peers` Изыскания о пэрах — сцена без итога
- [low] `scenes.no_people` `wwc-covert-actions-en/scene/puddles-operation-lake` Операция «Озеро» — сцена без участников
- [low] `scenes.no_people` `wwc-covert-actions-en/scene/puddles-beach-hut` Пляжный домик C3 — сцена без участников

### Нечистая сила (`wwc-covert-actions-en/scenario/the-unclean`) — 1

- [low] `scenes.no_place` `wwc-covert-actions-en/scene/unclean-meeting-arkhiv` Встреча с Архивом — сцена без места

