# Исправления F3 — «Книга хранителя» (RU)

Строка F3 `summary.md`; подробности — `kr-lists.md` (гл. 4, 12, 14) и `kr-rules.md` (гл. 4). Все тексты и числа — по
изображениям страниц `keeper-rulebook-ru`; изменённые значения — в `corrections` (Р-247, Р-22). Скрипты —
`scratchpad\fix-F3\` (`cols.py`, `clean.py` — колонки текстового слоя; `final_*.txt` — вычитанный текст статей;
`build_skills.py`, `build_rules.py`, `build_table.py`, `swarm.py`, `proposals.py`). `tools/check.py` по всем файлам — ошибок 0,
предупреждений 0.

| Пункт строки F3 | Итог | Файлы |
|---|---|---|
| Полные тексты статей навыков (с. 55–77): описание, «Противоположный навык и уровни сложности» с обычной и трудной задачей, примеры повторной проверки, последствия её провала, «если провалит безумный сыщик», примечания и списки специализаций | сделано: у всех 54 навыков «Книги хранителя» `description.ru` — текст статьи книги (вычитан по изображениям физ. 52–73); прежний краткий пересказ — в `corrections.from`; абзацы других книг («Компаньон хранителя», Hort и др.) сохранены после текста статьи; у статей на двух страницах — источник на каждую страницу (`entry_page`) | `kb/skills/` — accounting, animal-handling, anthropology, appraise, archaeology, art-craft, artillery, charm, climb, computer-use, credit-rating, cthulhu-mythos, disguise, diving, dodge, drive-auto, electrical-repair, electronics, explosives, fast-talk, fighting, firearms, first-aid, heavy-machinery, history, hypnosis, intimidate, jump, language-other, language-own, law, library-use, listen, locksmith, lore, mechanical-repair, medicine, natural-world, navigate, occult, persuade, pilot, psychoanalysis, psychology, read-lips, ride, science, sleight-of-hand, spot-hidden, stealth, survival, swim, throw, track |
| Частные правила внутри статей: падение с лошади (не менее 1d6 ПЗ, Прыжки отменяют урон, дамское седло), Прыжки (урон вдвое, расстояния), Ловкость рук (сложность по Вниманию <50% / 50–89%), Медицина (лечение позже — трудный успех, бонусная кость к еженедельной проверке), Лазание (1d6/1d10 за 3 м) | сделано — входят в тексты статей | `kb/skills/ride.json`, `jump.json`, `sleight-of-hand.json`, `medicine.json`, `climb.json` |
| Шкала владения иностранным языком и опознание языка (с. 76) | сделано: текст в статье навыка и отдельная запись правила с двумя таблицами (5/10/30/50/75%; Знания / Археология или История / Мифы Ктулху или Оккультизм) | `kb/skills/language-other.json`, `kb/rules/other-language-skill-suggestions.json` (новая) |
| Необязательное правило «Специализации: перенос бонусов» и «Языки» с примерами Матвея и Бориса (с. 76–77) | сделано: `optional: true`, шаги, оба примера; расхождение примера с английским изданием (топор 30% в EN, 25% в RU) — в `quality.notes` | `kb/rules/specializations-transferable-skill-benefit.json` (новая) |
| Вступление «Раздел 2. Божества Мифов» и врезка «Встреча с божеством» (с. 308) | сделано | `kb/rules/section-two-deities-of-the-mythos.json` (новая) |
| Вступления «Раздел 3. Традиционные монстры» (с. 330) и «Раздел 4. Животные» (с. 334) | сделано, по образцу `section-one-mythos-monsters` | `kb/rules/section-three-traditional-horrors.json`, `kb/rules/section-four-beasts.json` (новые) |
| Таблица XIII «Врата: места и расстояния» (с. 248) | сделано: все 27 строк; в английском издании это таблица XIV — в `aliases` и `quality.notes`; другие расстояния русского издания (звёзды, облако Оорта) — в `quality.notes`; «105 (23)» у Азатота и дальнего квазара (по правилу 105 МОЩ = 21 ПМ, так же в EN) — `errata` как напечатано, флаг `parse_uncertain` | `kb/tables/gate-locations-and-distances.json` (новая) |
| Осиный или пчелиный рой: «до 3d6 минут», источник «Книги хранителя» | сделано: «до 3d6 минут» по «Книге хранителя» (RU с. 337, EN с. 340); «3D6 rounds» Malleus противоречит его же «each minute of such an attack» — `errata` (`fixed: true`) и `corrections`; источники KR RU и EN добавлены (Malleus остаётся первым); название и формулировки «Преследования» и «Африканизированных пчёл» — по русской «Книге хранителя» (Р-22), прежнее название «Рои ос и пчёл» — в `aliases` | `kb/creatures/wasp-and-bee-swarm.json` |
| Опечатка ЛВК насекомого с Шаггая ((2d6+24)×5 при среднем 80, с. 295; так же в EN с. 305) | предложение: запись `coc:creature:shan` — часть F1 (Malleus); `errata` + флаг `parse_uncertain`. Если F1 тоже заводит `errata` у этой записи, предложение `set errata` надо применить после F1 как `append` | `checks/20261115-content/proposals-F3.json` |

Сверх строки (тот же раздел книги, записи не было): врезка «Социальные навыки: в чём разница?» и «Как применять к
персонажам игроков» (с. 59) — `kb/rules/interpersonal-skills-disambiguation.json` (новая).

Предложения (`proposals-F3.json`, пробный прогон `apply.py` проходит): `coc:rule:skill-specializations` — заменить пометку
«правило … здесь не записано» ссылкой на новую запись и добавить её в `refs`; `coc:creature:shan` — опечатка ЛВК (см. выше).

## Не взято

- Эпиграфы разделов 2 и 3 гл. 14 (Лавкрафт, «Ужас Данвича», «Брошенный дом») — как у раздела 1; упомянуты в `quality.notes`.
- Подписи к иллюстрациям гл. 4 («Эти иероглифы мне незнакомы», «Роясь в библиотеке, можно узнать удивительные вещи!»,
  «На перевод уйдёт несколько недель!») — атмосфера, без правил.
- Заголовки статей навыков («Антропология (01%)», «[необычный]», «[современный]») в текст не повторены: база и пометки уже в
  полях `base`, `uncommon`.

## Для ведущего

- Поле `examples` у части навыков (например, «Найти регулярные выплаты культу в книгах фирмы») — не из книги (наследие
  веб-помощника), флага нет. Не трогал: убирать или помечать — вопрос владельцу.
- Таблица XII «Стоимость создания и использования врат» по-прежнему только строками в `coc:spell:create-gate` (вне строки F3).
