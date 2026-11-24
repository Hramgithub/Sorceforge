# Полнота перенесённых книг — 2026-11-24

Создано `python tools/completeness.py`; база не менялась. Пороги: страница с текстом — от 120 слов; картинка — от 250×250, повторённые на 3+ страницах не считаются.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `text.gap` | Страницы с текстом, которые не цитирует ни одна запись | 0 |
| `art.uncovered` | Картинки книги на странице, где ни одна запись не несёт картинку | 1 |
| `art.record_without` | Страница с картинкой, которую не несёт ни одна запись, а персонаж, существо, раздатка, предмет или книга этой страницы — без `images` | 3 |
| `links.character_unused` | Персонаж без связей: ни сцена, ни сценарий, ни другая запись на него не ссылаются, своих связей нет | 0 |
| `links.scene_no_place` | Сцена без места (`where`) | 0 |
| `links.unused` | Раздатка или предмет, которые не использует ни сцена, ни сценарий | 0 |
| `context.no_description` | Запись без описания | 0 |
| `context.handout_empty` | Раздатка без текста и без картинки | 0 |
| `context.scenario_thin` | Сценарий без краткого содержания (`summary`) или сведений для хранителя (`keeper_info`/`steps`) | 0 |
| `context.incomplete` | Запись помечена `incomplete` | 0 |

## Книги

| Книга | Язык | Текст | Стр. | Записей | Цитир. стр. | Стр. без записей (слов) | Стр. с картинками | без записи | Находок |
|---|---|---|---|---|---|---|---|---|---|
| Convicts & Cthulhu — Ticket of Leave #1 - Night Terrors (`convicts-tol-01-en`) | en | текст | 5 | 20 | 4 | 0 (0) | 2 | 0 | 0 |
| Convicts & Cthulhu — Ticket of Leave #2 - Tricolour Terror (`convicts-tol-02-en`) | en | текст | 7 | 27 | 6 | 0 (0) | 3 | 0 | 0 |
| Convicts & Cthulhu — Ticket of Leave #3 - Criminal Enterprise (`convicts-tol-03-en`) | en | текст | 9 | 29 | 8 | 0 (0) | 3 | 1 | 1 |
| Convicts & Cthulhu — Ticket of Leave #4 - The Vanishing Ensign (`convicts-tol-04-en`) | en | текст | 15 | 36 | 14 | 0 (0) | 7 | 3 | 3 |

## Находки по книгам

### Convicts & Cthulhu — Ticket of Leave #4 - The Vanishing Ensign (`convicts-tol-04-en`) — 3

**Картинки** (3)

- [high] с. 3: 1 карт. (1130×999); без картинки: Чарльз Роджерс (character), Ричард Фитч (character)
- [high] с. 9: 1 карт. (548×982); без картинки: Джоб Трэшер (character)
- [low] с. 5: 1 карт. (539×582); на странице: Посещение мест близ Парраматты (scene), Посещение мест близ Сиднея (scene)

### Convicts & Cthulhu — Ticket of Leave #3 - Criminal Enterprise (`convicts-tol-03-en`) — 1

**Картинки** (1)

- [high] с. 6: 1 карт. (536×741); без картинки: Добровольцы Бэнкс-Тауна (character), Джонатан Дженкс (character), Мистер и миссис Смейлз (character), Сара Смейлз (character), Перегонный куб Смейлзов (item)

