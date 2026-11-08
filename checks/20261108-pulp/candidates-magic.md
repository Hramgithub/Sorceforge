# Pulp Cthulhu, кандидаты части magic (Р-191) — покрытие

Часть `magic`. Новые записи: заклинания `kb/spells/` (6), талант `kb/talents/` (1), книга Мифов
`kb/books/pulp-cthulhu-en/tomes/` (1). Предложения правок чужих записей — `proposals-candidates-magic.json`
(29 предложений для 10 записей; `apply.py --dry-run` проходит). `python tools/check.py` по новым файлам — 0 ошибок,
0 предупреждений.

## Кандидаты

| Кандидат (откуда) | Что в книге | Итог |
|---|---|---|
| Cloak of Fire (villains.md) | Pulp Cthulhu, с. 128 — полный текст; Grand Grimoire, с. 66 — полный текст | создана `coc:spell:cloak-of-fire` «Огненный плащ»: значения по Grand Grimoire (Р-51), Pulp Cthulhu — второй источник, расхождения (урон оружия, проверка Удачи на возгорание, усиленная версия 4 ПМ / 1d10+2 у Нефритового императора против 6 ПМ / 1d8) — в `quality.notes` |
| Vanish, Pulp (villains.md) | Pulp Cthulhu, с. 129 — полный текст; Grand Grimoire, с. 183 — «Vanish (Gate Boxes variant)» | создана `coc:spell:vanish` «Исчезновение», `variant_of` — `coc:spell:gate-boxes` (так в Grand Grimoire); отличия Pulp Cthulhu (талисман без врат, несколько шкатулок, осквернение) — в `quality.notes`; у «Шкатулок врат» псевдоним «Vanish» остаётся (из списка Grand Grimoire), различие — предложением в её `deeper_magic` и `quality.notes` |
| Pipes of Madness (slowboat.md) | Pulp Cthulhu, с. 234 — врезка, полный текст; Grand Grimoire, с. 150 | создана `coc:spell:pipes-of-madness` «Трубы безумия»: значения по Grand Grimoire (там ещё абзац о проверке Рассудка самого играющего и дудка от «Create Curse Whistle»), Pulp Cthulhu — второй и третий источник (с. 234, 227) |
| Identify Spirit (magic-running.md) | Pulp Cthulhu, с. 86 — только название; Grand Grimoire, с. 128 — полный текст | создана `coc:spell:identify-spirit` «Опознать духа» по Grand Grimoire: текст есть в книге-источнике заклинаний (Р-51), поэтому правило «только название — не заводить» не применено |
| Contact Servitor of the Outer Gods (organizations.md) | Pulp Cthulhu, с. 58 — только название в списке книги; «Книга хранителя» (рус. с. 253, англ. с. 252) и Grand Grimoire (с. 80) — полный текст | создана `coc:spell:contact-servitor-of-the-outer-gods` «Связь со служителем Внешних богов» по русской КХ (без флага `translated`), `variant_of` — `coc:spell:contact-spells`; запись отсутствовала в справочнике, хотя заклинание есть в КХ |
| Stop Heart (organizations.md) | Pulp Cthulhu, с. 58 — только название; Grand Grimoire, с. 174 — полный текст | создана `coc:spell:stop-heart` «Остановка сердца» по Grand Grimoire |
| The Inheritance of the Kingdom (organizations.md) | Pulp Cthulhu, с. 58 — врезка с числами; с. 57 — упоминание | создана `pulp-cthulhu-en/tome/inheritance-of-the-kingdom` «Наследование Царства» (2d4 Рассудка, Мифы +2/+4, уровень Мифов 18, 32 недели, 7 заклинаний — все со ссылками) |
| Psychic Attack (magic-running.md) | Pulp Cthulhu, с. 86: герой пишет «Psychic Attack» в графу талантов, и тогда не может взять других пульп-талантов | книга даёт её как выбор в графе талантов — создан талант `coc:talent:psychic-attack` «Психическая атака» (раздел «ментальный» — вывод, Р-41; правила атак остаются в `coc:rule:pulp-psychic-attacks-and-possession`) |
| Summon/Bind Star Spawn of Cthulhu (hurricane.md) | только название в статблоке старейшины (с. 175); ни Pulp Cthulhu, ни КХ, ни Grand Grimoire текста не дают | не создано (только название); предложена ссылка у старейшины на семейство `coc:spell:summon-bind` |
| Summon/Bind Flying Polyp (slowboat.md) | только название в списке «Книги Красного нефрита» (с. 223) и в финале (с. 228); текста нигде нет | не создано; предложена ссылка в списке книги на семейство `coc:spell:summon-bind` (у сцены «Последнее испытание» и книги семейство уже в `refs`) |

Оси: шесть заклинаний — `ruleset: core`, `era: any`, как все заклинания справочника из «Книги хранителя» и Grand
Grimoire (по примеру `coc:spell:bind-enemy`, где Pulp Cthulhu — второй источник): эти заклинания есть в книгах ядра,
значит запись ядра (Р-02), а не пульп-запись. Талант и книга Мифов — `pulp`, `1930s` (Р-188).

## Заголовки книги, касающиеся кандидатов

Остальные заголовки страниц 79–90, 116–134, 150–157, 194–234 разнесены раньше и учтены в отчётах `system-sanity.md`
(с. 60–80), `magic-running.md` (с. 81–98), `1930s.md` (с. 99–120), `villains.md` (с. 121–134), `disintegrator.md`
(гл. 10, до с. 157), `pandora.md` (с. 176–204), `slowboat.md` (с. 205–234); эта часть их не меняла.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Mythos Tome: The Inheritance of the Kingdom (врезка) | 58 | `pulp-cthulhu-en/tome/inheritance-of-the-kingdom`; пересказ в описании `organization/inheritors` остаётся |
| Cult Beliefs («suppressed Georgian occult treatise») | 57 | `pulp-cthulhu-en/tome/inheritance-of-the-kingdom` — последний абзац описания |
| Psychic Attacks and Possession («Identify Spirit») | 86 | `coc:rule:pulp-psychic-attacks-and-possession`; заклинание — `coc:spell:identify-spirit` (предложены `refs`) |
| Allowing Heroes to use Psychic Attacks | 86 | `coc:rule:pulp-psychic-attacks-and-possession`; талант — `coc:talent:psychic-attack` |
| The Jade Emperor — Spells: Cloak of Fire** | 123 | `character/the-jade-emperor` — предложена ссылка `statblock.spells.items[0].spell` |
| Scarlet Arachnis — Spells: Vanish* | 126 | `character/scarlet-arachnis` — предложена ссылка `statblock.spells.items[2].spell` |
| Villainous Spells: Cloak Of Fire | 128 | `coc:spell:cloak-of-fire`; полный текст Pulp Cthulhu — `coc:rule:pulp-villainous-spells` |
| Villainous Spells: Vanish | 129 | `coc:spell:vanish`; полный текст Pulp Cthulhu — `coc:rule:pulp-villainous-spells` |
| Deep One Elder — Spells: Summon/Bind Star Spawn of Cthulhu | 175 | `creature/deep-one-elder-rhathylla` — ссылка на семейство `coc:spell:summon-bind` (предложение) |
| The Book of Red Jade — Summon/Bind Flying Polyp | 223 | `tome/book-of-red-jade` — ссылка на семейство (предложение) |
| The Final Test («as per the Pipes of Madness spell») | 227 | `scene/slow-boat-the-final-test` — предложены `refs` на `coc:spell:pipes-of-madness`; `item/slow-boat-pipes-of-leng` — тоже |
| Pipes of Madness (врезка) | 234 | `coc:spell:pipes-of-madness`; текст врезки остаётся в `item/slow-boat-pipes-of-leng` |

## Опечатки и сомнения

- Ошибка перевода в нашей записи `organization/inheritors`: «suppressed Georgian occult treatise» (с. 57) передано как
  «грузинского оккультного трактата»; по врезке (с. 58) книга английская, около XVIII века, — это георгианская эпоха
  Англии. Предложена замена (с `corrections`).
- Pulp Cthulhu против Grand Grimoire: у «Огненного плаща», «Исчезновения» и «Труб безумия» числа цены и времени
  совпадают, различаются подробности (см. таблицу кандидатов); значения записей — по Grand Grimoire (порядок
  источников заклинаний, Р-51), различия — в `quality.notes`, полный текст Pulp Cthulhu — в правиле и предмете.
- «Psychic talent» (с. 86) — так книга называет талант «Psychic Power» (с. 25); вывод (Р-41) — в `corrections` таланта.
- «Necromonicon» (с. 57, 58) — словесная опечатка книги, в переводе исчезла (Р-39).
- В Grand Grimoire заклинание «Связь со служителем Внешних богов» вкладывается «при чрезвычайном успехе Убеждения»,
  в КХ — «не более 1/5 навыка»: одно и то же, отмечено в пометке.
- В `errata` ничего не внесено: числовых опечаток не найдено.

## Не взято

- Иллюстрации на этих страницах — уже перечислены в «Не взято» отчётов `organizations.md`, `magic-running.md`,
  `villains.md`, `slowboat.md` (картинки — отдельный шаг, Р-165).
- Русские варианты названий заклинаний (как у старых записей из веб-помощника) не добавлены: русского источника нет,
  в `aliases` — только «Alternative names» Grand Grimoire.

## Кандидаты в новые записи (не этой части)

- Заклинание «Create Curse Whistle» (Grand Grimoire, с. 86): нужно для «Труб безумия» (и «Soul Singing»); в
  справочнике нет, названо текстом в `coc:spell:pipes-of-madness`.
- Заклинание «Contact Spirits of the Dead» (КХ рус. с. 252–253, англ. с. 252; Grand Grimoire, с. 80) — в справочнике
  нет, хотя есть в «Книге хранителя» (найдено рядом со «Связью со служителем Внешних богов»).
- Существо `pulp-cthulhu-en/creature/malevolent-spirit` и `coc:creature:people-of-kn-yan`: атака «Psychic Attack» —
  можно сослаться на `coc:rule:pulp-psychic-attacks-and-possession` (не предлагалось: это не кандидат части).

## Предложения (`proposals-candidates-magic.json`, 29)

- `character/the-jade-emperor` — ссылка на `coc:spell:cloak-of-fire` в списке заклинаний и в способности «Огненный
  плащ: усиленная версия»; пометка.
- `character/scarlet-arachnis` — ссылка на `coc:spell:vanish`; пометка.
- `coc:rule:pulp-villainous-spells` — `refs` на оба заклинания, `summary`, две ячейки таблицы расхождений, пометка.
- `coc:rule:pulp-psychic-attacks-and-possession` — `refs` на `coc:spell:identify-spirit` и `coc:talent:psychic-attack`;
  пометка (два куска).
- `organization/inheritors` — `refs` на книгу и два заклинания; исправление «грузинского» (с `corrections`); пометка.
- `item/slow-boat-pipes-of-leng`, `scene/slow-boat-the-final-test` — `refs` на `coc:spell:pipes-of-madness`; пометка
  предмета.
- `tome/book-of-red-jade`, `creature/deep-one-elder-rhathylla` — ссылка на семейство `coc:spell:summon-bind`; пометки.
- `coc:spell:gate-boxes` — `deeper_magic` и пометка о том, что «Исчезновение» (Vanish) — отдельная запись-вариант.

Все, кроме исправления перевода у «Наследников», — `"correction": false` (ссылки и устаревшие пометки).
