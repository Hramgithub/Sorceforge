# Целостность сценариев — 2026-11-17

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 0 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 1 |
| `scenes.no_place` | Сцена без места | 9 |
| `scenes.no_people` | Сцена без участников | 5 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 7 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 0 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 0 |
| `clues.empty` | Раздатка без текста и без картинки | 0 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 0 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Голос в трубке | `petersens-abominations-en` | 154–179 | 19 | 42 (6) | 9 (7) | 2 (0) | 9 | 16 | 5 | 0 | 14 |
| Адский отель | `petersens-abominations-en` | 11–35 | 16 | 13 (7) | 4 (3) | 5 (5) | 10 | 35 | 5 | 0 | 7 |
| Кошмары цифровой эпохи | `petersens-abominations-en` | 1–7 | 0 | 0 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 1 |
| Мохол | `petersens-abominations-en` | 109–138 | 19 | 30 (12) | 3 (3) | 1 (1) | 8 | 34 | 2 | 0 | 0 |
| Панацея | `petersens-abominations-en` | 74–98 | 22 | 28 (12) | 7 (4) | 2 (2) | 9 | 42 | 2 | 0 | 0 |

## Находки по сценариям

### Голос в трубке (`petersens-abominations-en/scenario/voice-over-the-phone`) — 14

- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-analyzing-green-fluid` Анализ зелёной жидкости — сцена без итога
- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-researching-viper` Расспросы о Вайпере и ЮВ14 — сцена без итога
- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-pet-theft` Кражи питомцев — сцена без итога
- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-missing-fingers` Недостающие пальцы — сцена без итога
- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-body-count` Счёт трупам — сцена без итога
- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-police-crack-down` Полиция закручивает гайки — сцена без итога
- [low] `scenes.no_outcome` `petersens-abominations-en/scene/voice-your-enemy-is-my-friend` Враг твой — мой друг — сцена без итога
- [low] `scenes.no_people` `petersens-abominations-en/scene/voice-analyzing-green-fluid` Анализ зелёной жидкости — сцена без участников
- [low] `scenes.no_people` `petersens-abominations-en/scene/voice-vehicular-revelations` Что рассказали машины — сцена без участников
- [low] `scenes.no_place` `petersens-abominations-en/scene/voice-analyzing-green-fluid` Анализ зелёной жидкости — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/voice-the-voice-on-the-phone` Голос в трубке: звонки Вайпера — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/voice-missing-fingers` Недостающие пальцы — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/voice-body-count` Счёт трупам — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/voice-your-enemy-is-my-friend` Враг твой — мой друг — сцена без места

### Адский отель (`petersens-abominations-en/scenario/hotel-hell`) — 7

- [low] `scenes.no_people` `petersens-abominations-en/scene/hotel-ground-floor` Отель: первый этаж — сцена без участников
- [low] `scenes.no_people` `petersens-abominations-en/scene/hotel-hoodoo-mountain` Поход к горе Худу — сцена без участников
- [low] `scenes.no_people` `petersens-abominations-en/scene/hotel-prospector-cabins` Старательские хижины — сцена без участников
- [low] `scenes.no_place` `petersens-abominations-en/scene/hotel-investigators` Сыщики, снаряжение и связь — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/hotel-research` Поиски о наследстве — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/hotel-possession` Одержимость — сцена без места
- [low] `scenes.no_place` `petersens-abominations-en/scene/hotel-breaking-news` Срочные новости — сцена без места

### Кошмары цифровой эпохи (`petersens-abominations-en/scenario/petersens-abominations`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

