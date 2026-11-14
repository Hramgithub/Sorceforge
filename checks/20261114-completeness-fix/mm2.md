# Malleus Monstrorum, т. II — правила божеств, таблица, заклинание, лор (часть «mm2», Р-242)

Книга `malleus-monstrorum-2-en`. В задании и в verify-malleus.md страницы физические (10–24, 28, 33, 141, 167);
ниже «Страница» — печатный номер книги (физическая = печатная + 1; у `pages.py` для этой книги смещения нет, «с. N»
в его выводе — физическая страница). Тексты — наш перевод с английского (`translated`), числа сверены по изображениям
страниц (с. 13, 19, 20–21, 27, 166).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 1 «Unknowable: About the Gods of the Mythos» (вступление главы) | 9 | `coc:rule:malleus-deity-classifications` (`text`, первые абзацы) |
| Classifications (с перечнем шести групп) | 9 | `coc:rule:malleus-deity-classifications` |
| Great and Lesser Old Ones | 9–10 | `coc:rule:malleus-deity-classifications` |
| Outer Gods (с примечанием об Other Gods) | 10 | `coc:rule:malleus-deity-classifications` |
| Avatars | 10 | `coc:rule:malleus-deity-classifications` |
| Elder Gods (с примечанием о Дерлете) | 10–11 | `coc:rule:malleus-deity-classifications` |
| Unique Beings | 11 | `coc:rule:malleus-deity-classifications` |
| Other—Great Ones | 11 | `coc:rule:malleus-deity-classifications` |
| Human Perceptions of the Mythos (с эпиграфом из «Зова Ктулху») | 11 | `coc:rule:malleus-human-perceptions-of-the-mythos` |
| The Mind Opened to the Mythos | 11–12 | `coc:rule:malleus-human-perceptions-of-the-mythos` |
| Earthly Forms | 12 | `coc:rule:malleus-human-perceptions-of-the-mythos` |
| Using Mythos Gods in Games | 12 | `coc:rule:malleus-using-mythos-gods-in-games` |
| At the Human Level | 12–13 | `coc:rule:malleus-using-mythos-gods-in-games` |
| We Attack! | 13 | `coc:rule:malleus-using-mythos-gods-in-games` |
| Deity Spells and Powers | 13 | `coc:rule:malleus-using-mythos-gods-in-games` |
| The Gifts of Gods (стандартные дары: заклинание; пункты Мифов Ктулху по 5–10) | 13 | `coc:rule:malleus-using-mythos-gods-in-games` (`text`, `steps`) |
| Designing Mythos Gods (13 вопросов-подсказок, броня, размер, МОЩ, заклинания, атаки) | 16–17 | `coc:rule:malleus-designing-mythos-gods` |
| The Entries (без ИНТ у богов) | 17 | `coc:rule:malleus-deity-entries` |
| Physical Manifestation | 17 | `coc:rule:malleus-deity-entries` |
| Entry Format: Quoted Description, Other Names, Main Entry, Cult, Possible Blessings, Encounters, Aura, Main Profile, Sanity Loss, Magic/Spells, Powers, Typical Physical Manifestation (без Уклонения — половина ЛВК; без численного превосходства) | 17–18 | `coc:rule:malleus-deity-entries` (`text`, `steps`) |
| Hit Points (при 0 ПЗ — рассеивается) | 19 | `coc:rule:malleus-deity-entries` |
| Armor; Immunities; Vulnerabilities | 19–20 | `coc:rule:malleus-deity-entries` |
| Hit Point Losses by Damage Type (таблица со сносками) | 19 | `coc:rule:malleus-deity-entries` (`tables[0]`) — таблица без броска (Р-171); та же таблица т. I — у части mm1 |
| Deities by Type: Great Old Ones, Lesser Old Ones, Outer Gods | 20 | `coc:rule:malleus-deities-by-type` (`tables[0–2]`) |
| Deities by Type: Avatars, Elder Gods, Unique Entities | 21 | `coc:rule:malleus-deities-by-type` (`tables[3–5]`); все 120 строк (113 сущностей) связаны с записями базы (`refs`) |
| Chapter 2 «Deities of the Mythos»; Abhoth (Great Old One) | 23 | уже было: `coc:creature:abhoth`; тип в базе «Внешний бог» ≠ Malleus — предложение в `proposals-mm2.json` |
| Aphoom Zhah: Ice Touch → «Hit Location Table» | 26 | `coc:table:malleus-aphoom-zhah-hit-location` (`description`) |
| Table: Hit Location (1d20) | 27 | `coc:table:malleus-aphoom-zhah-hit-location` |
| Arwassa (начало статьи) | 27 | уже было: `coc:creature:arwassa` |
| Atlach-Nacha: основной текст, Other names | 29–30 | `coc:creature:atlach-nacha` (`legend`, `aliases`, связь `related_to` Йог-Сотот) |
| Spiders in Myth and Legend (врезка) | 32 | `coc:creature:atlach-nacha` (`legend`, последний абзац) |
| Azathoth (начало статьи) | 32 | уже было: `coc:creature:azathoth` |
| Bast: цитата-описание, основной текст, Other names | 40–41 | `coc:creature:bast` (`legend`, `aliases`) |
| Chaugnar Faugn: цитата-описание, основной текст, Other names | 47 | `coc:creature:chaugnar-faugn` (`legend`, `aliases`, связь `related_to` Ньярлатхотеп) |
| Cthulhu: цитата-описание, основной текст, Other names | 51, 54 | `coc:creature:great-cthulhu` (`legend`, `aliases`) |
| Daoloth: цитата-описание, основной текст (Азатот, Тиндал / Мх’итрха, Ядрем), Other names | 73–74 | `coc:creature:daoloth` (`legend`, `aliases`, связи `related_to` Мх’итрха и Азатот) |
| From the Journal of Sir Hansen Poplan: Elder Gods (врезка) | 140 | `coc:rule:malleus-deity-classifications` (`text`, после «Старших богов») |
| Nodens (аура, силы), Nug & Yeb (начало) | 140 | уже было: `coc:creature:nodens`, `coc:creature:nug-and-yeb` |
| Vach-Viraj Incantation (Spell) (врезка) и абзац о «Некрономиконе» | 166 | `coc:spell:vach-viraj-incantation` (название — «Песнопение Вак-Вирадж» по русской «Книге хранителя», с. 303) |
| Nyogtha: Cult, Possible Blessings | 166 | уже было: `coc:creature:nyogtha` |
| Yibb-Tstll (Great Old One/Outer God/Unique Entity): цитата-описание, основной текст, Other names | 222–223 | `coc:creature:yibb-tstll` (`legend`, `aliases`, `subcategory`, связи `related_to` Йог-Сотот, Бугг-Шаш, Шуб-Ниггурат) |
| Yog-Sothoth: цитата-описание, основной текст, цитата «Некрономикона», Other names | 232–233 | `coc:creature:yog-sothoth` (`legend`, `aliases`, связи `related_to` Сайтулос, Хастур) |

У всех семи существ добавлены источники Malleus для страниц начала статьи и элементы `corrections` (`legend.ru`,
`aliases`, `sources`, `relations`; у Йибб-Тистла ещё `subcategory`, Р-22). Прежние поля не менялись.

## Предложения

`proposals-mm2.json` — 4 предложения (пробный прогон `apply.py --dry-run` проходит):
- `coc:creature:abhoth` — `subcategory` «Внешний бог» → «Великий Древний» (Malleus, с. 23 и указатель, Р-22);
- `coc:creature:aphoom-zhah` — ссылка способности «Ледяное касание» на `coc:table:malleus-aphoom-zhah-hit-location`;
- `coc:creature:nyogtha` — ссылка способности «Изгнание» на `coc:spell:vach-viraj-incantation` и официальное
  название «Песнопение Вак-Вирадж» вместо «Vach-Viraj» в её тексте.

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Полностраничные иллюстрации и подписи к ним («Opposite: Learning the sigils», «Opposite: Forbidden Knowledge», «Image over page…») | 14, 15, 22, 9, 23, 51 | атмосферные иллюстрации не импортируются (Р-241) |
| Мелкие детали «covered»-строк verify-malleus.md по т. II (опера «Massa di Requiem per Shuggay», цитата МакРуда, экспедиция Мортимера–Паркса, теория Джакоби Тинда, «Wild Forests», Фоли и Нуэлл’да, Якш, Акен/Меджед/Эрешкигаль) | 39–219 | вне задания части mm2 (не «partly» и не в `target`); остаются в verify-malleus.md |
| Отдельная запись таблицы «Hit Point Losses by Damage Type» | 19 | таблица без броска — в `tables` правила (Р-171); её копию из т. I (с. 29 PDF) переносит часть mm1 — сведение может оставить одну |

## Опечатки и сомнения

- Указатель «Божества по типам» расходится с заголовками статей: Фарол (с. 174) и Себек (с. 186) в указателе —
  Великие Древние, в статьях — «Lesser Old One/Unique Entity»; Мать гноя (с. 134) в указателе — Внешний бог, в статье —
  «Lesser Outer God». В записи правила — `errata` (как напечатано); записи существ следуют заголовкам статей.
- Абхот: в базе «Внешний бог», в Malleus — Великий Древний (заголовок статьи и указатель) → предложение.
- Йибб-Тистл: в базе был «Внешний бог»; в Malleus — «Great Old One/Outer God/Unique Entity»; исправлено в записи (Р-22).
- «Table: Hit Location» напечатана на странице статьи «Арвасса» (с. 27), но по тексту относится к ледяному касанию
  Афум-Жа (с. 26); в записи `aphoom-zhah` «Ледяное касание» в таблице атак названо Flame Touch (уже в её `errata`).
- Vach-Viraj: «magic/hit points/» — лишняя косая черта; «500 yards/meters» → 500 метров. Механика заклинания есть только
  в Malleus; «Книга хранителя» (с. 303) называет его лишь среди уязвимостей хтонийцев.

## Кандидаты в новые записи

- Кошки с Сатурна и Урана (упомянуты в статье «Баст» как неподвластные ей) — записи существа нет.
- Книги «Of Stars and Blood» (Уиппл, 1768; статья «Йибб-Тистл») и «Voids of Darkness» (дневник Ядрема; статья
  «Даолот») — записей книг Мифов нет; у существ нет поля `refs`, поэтому `coc:tome:cthaat-aquadingen` из легенды
  Йибб-Тистла не связан.
- Эликсир Тиккун и «петлистый крест» — пока только в описании `coc:spell:vach-viraj-incantation`.
