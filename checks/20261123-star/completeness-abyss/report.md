# Полнота перенесённых книг — 2026-11-23

Создано `python tools/completeness.py`; база не менялась. Пороги: страница с текстом — от 120 слов; картинка — от 250×250, повторённые на 3+ страницах не считаются.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `text.gap` | Страницы с текстом, которые не цитирует ни одна запись | 6 |
| `art.uncovered` | Картинки книги на странице, где ни одна запись не несёт картинку | 0 |
| `art.record_without` | Страница с картинкой, которую не несёт ни одна запись, а персонаж, существо, раздатка, предмет или книга этой страницы — без `images` | 0 |
| `links.character_unused` | Персонаж без связей: ни сцена, ни сценарий, ни другая запись на него не ссылаются, своих связей нет | 0 |
| `links.scene_no_place` | Сцена без места (`where`) | 0 |
| `links.unused` | Раздатка или предмет, которые не использует ни сцена, ни сценарий | 0 |
| `context.no_description` | Запись без описания | 0 |
| `context.handout_empty` | Раздатка без текста и без картинки | 0 |
| `context.scenario_thin` | Сценарий без краткого содержания (`summary`) или сведений для хранителя (`keeper_info`/`steps`) | 0 |
| `context.incomplete` | Запись помечена `incomplete` | 1 |

## Книги

| Книга | Язык | Текст | Стр. | Записей | Цитир. стр. | Стр. без записей (слов) | Стр. с картинками | без записи | Находок |
|---|---|---|---|---|---|---|---|---|---|
| The Star on the Shore (`star-on-the-shore-en`) | en | текст | 99 | 20 | 12 | 60 (19941) | 0 | 0 | 7 |

## Находки по книгам

### The Star on the Shore (`star-on-the-shore-en`) — 7

**Тексты** (6)

- [high] с. 8 — с. 16: 8 стр., 2855 слов не цитирует ни одна запись; headings: PRS; Introduction; Prologue; Keeper's Secret
- [high] с. 19 — с. 37: 19 стр., 6861 слов не цитирует ни одна запись; headings: Location 1; Rockport Police Department; Police Station; Front Door; near: Ядро — разломная бомба
- [high] с. 40 — с. 67: 24 стр., 8198 слов не цитирует ни одна запись; headings: American War, and was instrumental in changing; Congregational Church down to the police station,; Location 24; Rockport Library; near: Вооружение и оккультизм; Дубовая копия ядра; Ключ к Бездне
- [high] с. 88 — с. 96: 7 стр., 1052 слов не цитирует ни одна запись; headings: Cy, 4; Rr, |; ALEXANDER HAWKEY, Private Eye, age 32; Combat
- [low] с. 79: 1 стр., 473 слов не цитирует ни одна запись; headings: British Attack was All Wet; September 8, 1814, the British frigate Nymph; Firing the shot, the carronade went through; Their captain effected an exchange of
- [low] с. 82: 1 стр., 502 слов не цитирует ни одна запись; headings: Local News Bsa essive; Weather; The high today was 79; Almanac predicts the

**Контекст** (1)

- [low] `star-on-the-shore-en/tome/armaments-and-the-occult` Вооружение и оккультизм — Русский текст — наш перевод с английского оригинала (Р-251, Р-21); книга — скан без текстового слоя, текст и числа сверены по изображениям страниц; печатная страница = физическая − 3. Свойств книги (п

