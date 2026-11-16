# «The Vernissage» (`vernissage-en`) — сверка переноса (Р-251, Р-134)

Источник: английский оригинал, 31 страница PDF (Miskatonic Repository, серия Zgrozy; сценарий, иллюстрации и оформление — Michal Gralak, перевод на английский — Michał Podłubny). Русского издания в базе нет (проверено по `kb/books/*-ru/`: Артомовский, Зайдлер, Вжодек, Заховский, Чаховский, Янтарное общество — не найдены).

Номера страниц: на страницах книги номеров нет; номера оглавления (с. 4, 5, 6, 16, 19) совпадают с физическими страницами — смещение 0 (physical = printed). В `sources` печатная страница — `null`.

Записи: `kb/books/vernissage-en/` — 77 (сценарий 1, сцены 16, персонажи 16, существо 1, организация 1, места 10, предметы 20, книги 2, раздатки 10). Картинки — 10 (`checks/20261116-vernissage/art.json`, применены); атмосфера — `atmosphere.json` (обложка).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| обложка «Zgrozy: The Vernissage» | 1 | `scenario/vernissage` (sources); картинка — `atmosphere.json` |
| What is The Vernissage? | 2 | `scenario/vernissage` (summary) |
| Table of Contents | 3 | `scenario/vernissage` (advice: устройство книги); ошибки оглавления — errata сценария |
| Background | 4 | `scenario/vernissage` (keeper_info «Предыстория»); `character/zbigniew-artomowski`; `organization/amber-society` |
| Involving the Investigators | 5 | `scenario/vernissage` (hook) |
| Secret motivation | 5 | `character/adept`; `scenario/vernissage` (advice) |
| Adept’s Knowledge | 5 | `scenario/vernissage` — таблица «Знания Адепта»; способность `character/adept` |
| Destroying evidence | 5 | `character/adept` (способность «Уничтожение улик»); advice сценария |
| Investigation | 6 | `scenario/vernissage` (шаги); часть сцен «Расследование» |
| Opening | 6 | `scene/opening`; `location/main-hall` |
| Artomowski’s Music Box | 6 | `scene/music-box-stops`; `item/music-box` |
| The Unveiling | 7 | `scene/unveiling` |
| Beings of New World | 7 | `item/beings-of-new-world`; `item/statue-observer`, `statue-accuser`, `statue-speaker`; `creature/lord-on-amber-throne`; keeper_info |
| The One Who Observes | 8 | `handout/note-the-observer` (текст + картинка страницы) |
| иллюстрация (статуя с глазами) | 9 | `item/statue-observer` (images) |
| The One Who Speaks | 10 | `handout/letter-the-speaker` |
| иллюстрация (статуя со ртом) | 11 | `item/statue-speaker` (images) |
| The One Who Accuses | 12 | `handout/letter-the-accuser` |
| иллюстрация (статуя с указующей рукой) | 13 | `item/statue-accuser` (images) |
| Invocation (Buffet, Cutlery, Amber, Songs of New World, Incense) | 14 | `scene/invocation`; `item/chalk-glyphs`, `marked-cutlery`, `amber-decorations`, `incense`; `character/hired-musicians` |
| Locations | 15 | `location/artomowski-estate` (город сценария) и 9 мест (`main-hall`, `terrace`, `hallway`, `artomowski-study`, `zajdler-office`, `guest-room`, `bathrooms`, `kitchen`, `shed`); `scene/investigation` |
| Evidence and tools | 15 | `scene/investigation`; `item/luminal`, `inkwell`, `solvent`, `perfumes`, `spare-cutlery` |
| Dangers | 16 | сцены части «Опасности» |
| The Observer (Behavior, Conflict: Synergy, Subterfuge, Rhetoric, Evidence; статблок) | 16 | `character/fryderyk-zajdler`; `scene/observer-conflict`; `item/zajdler-notes` |
| The Accuser (Behavior, Conflict: Confrontation, Subterfuge, Diplomacy; статблок) | 17 | `character/zygmunt-wrzodek`; `scene/accuser-conflict`; `character/estate-security` |
| The Speaker (Behavior, Conflict: Duel, Subterfuge, Alliance; статблок) | 18 | `character/antoni-zachowski`; `scene/speaker-conflict` |
| Epitasis | 19 | `scene/apnea` (вступление к эпитасису); шаг «Эпитасис» |
| Apnea | 19 | `scene/apnea`; `character/anna-czerwinska` |
| Fog | 19 | `scene/fog`; `character/jerzy-czaplinski` |
| Moths | 20 | `scene/moths` |
| Ex Machina | 20 | `scene/ex-machina`; `character/czachowski`, `stanislaw-korzeniowski` |
| Epilogue (письмо в конверте без адреса) | 21 | `scene/epilogue`; `handout/final-letter`; conclusion сценария |
| Extras | 21 | заголовок раздела: таблицы и раздатки сценария |
| Subplots | 21 | `scene/stone-gaze` (вступление к побочным линиям); advice |
| Incidents: Stone Gaze | 21 | `scene/stone-gaze`; `character/mieczyslaw-rozycki` |
| Incidents: The Disappearance of Attorney Czachowski | 21 | `scene/czachowski-disappearance` |
| Incidents: Sketch | 21 | `scene/sketch`; `character/tadeusz-kowalczyk` |
| The Overheard | 22 | `scenario/vernissage` — таблица «Подслушанные разговоры»; `character/karol-bartel`, `anna-czerwinska`, `antoni-zachowski`, `kazimierz-karpinski` |
| Psychotic Episodes | 22 | `scenario/vernissage` — таблица «Психотические эпизоды» |
| Motivations | 22 | раздатки «Мотивация 1–4» (description), hook сценария |
| Motivation 1: Family member | 23 | `handout/motivation-1-family-member` |
| Motivation 2: Old friend | 24 | `handout/motivation-2-old-friend` |
| Motivation 3: Sympathizer | 25 | `handout/motivation-3-sympathizer` |
| Motivation 4: Adept | 26 | `handout/motivation-4-adept` |
| Continuing the Adventure | 27 | `scenario/vernissage` (advice «Продолжение приключения»); `creature/lord-on-amber-throne` (relations) |
| Evidence (таблица, 12 строк) | 28–30 | `scenario/vernissage` — таблица «Улики»; `item/artomowski-instructions`, `occult-symbols-sheet`, `invocation-manuscript`, `art-of-reading-symbols`, `the-hidden`; `tome/power-of-ritual`, `power-of-gemstones`; `handout/waiters-instructions`, `note-about-yuggoth`, `note-the-observer`, `letter-the-accuser`, `letter-the-speaker` |
| выходные данные | 31 | `scenario/vernissage` (sources, summary) |

## Не взято

- Гость, зачитывающий записку из шкатулки («a nervous man with an old, exhausted face», с. 6), — одна реплика, книга его не называет; оставлен текстом в `scene/music-box-stops`, своей записи нет.
- Авторы писем-мотиваций 1–3 (кузен, знакомый, приятель) — только подписи писем, оставлены текстом раздаток.
- Хармион (Charmion) — имя из цитаты книги о Монархе в письме об Обвинителе (с. 12), текст раздатки.
- Записка из музыкальной шкатулки — книга не печатает её текст; пересказ — в `item/music-box`.
- Карты, плана усадьбы и готовых сыщиков в книге нет; Адепт — тайная роль (запись `character/adept` без статблока).
- Наград Рассудка за исход книга не даёт (в conclusion сказано прямо).

## Опечатки и сомнения книги

- Оглавление (с. 3): «Epilogue (p. 22)», «Subplots (p. 23)» — на деле с. 21 (errata сценария).
- «Adept’s Knowledge» (с. 5): бросок «3d10» на таблицу из 10 строк — по-видимому, три броска d10 (errata сценария, как напечатано).
- Скорость Зайдлера и Заховского напечатана 8; по характеристикам (СИЛ и ЛВК меньше ТЕЛ) — 7 (errata, как напечатано).
- Урон «2k4» (Вжодек, нож) и «1k3» (Заховский, драка) — польская запись кубов; записано 2d4 и 1d3 (Р-27).
- Фамилия поэта: Zachowski (с. 18, 22) / Żachowski (с. 29); реплика «Do you hear it too?» в «Moths» (с. 20) подписана «Antoni Czachowski» — смешение поэта и адвоката (errata `character/antoni-zachowski`, `scene/moths`).
- Эпилог (с. 21): письмо лежит «in his office» — по описанию мест это кабинет Артомовского (study).
- «Lord on The Amber Throne» (с. 29) — разнобой названия, псевдоним `creature/lord-on-amber-throne`.
- Искатель (The Seeker) — аспект, который упомянут только в таблице «Знания Адепта»; описания нет.
- «ritual effect table (See Extras)» (с. 19) — такой таблицы под этим названием нет; по-видимому, это «Psychotic Episodes» (вывод, Р-41).

## Термины (English → русский)

| English | Русский |
|---|---|
| The Vernissage | «Вернисаж» |
| vernissage | вернисаж |
| Zgrozy (series) | Zgrozy (название серии не переводится) |
| Zbigniew Artomowski | Збигнев Артомовский |
| Fryderyk Zajdler | Фридерик Зайдлер |
| Zygmunt Wrzodek | Зыгмунт Вжодек |
| Antoni Zachowski / Żachowski | Антоний Заховский |
| attorney Czachowski | адвокат Чаховский |
| Anna Czerwinska | Анна Червиньская |
| Jerzy Czaplinski | Ежи Чаплиньский |
| Dr. Stanislaw Korzeniowski | доктор Станислав Коженёвский |
| MP Karol Bartel | депутат Кароль Бартель |
| Kazimierz Karpinski | Казимеж Карпиньский |
| Charmion | Хармион |
| Michal Gralak / Michał Podłubny | Михал Гралак / Михал Подлубный |
| Artomowski’s estate | усадьба Артомовского |
| Amber Society | Янтарное общество |
| Lord on Amber Throne | Владыка на Янтарном троне |
| Amber Throne | Янтарный трон |
| Monarch / Amber Monarch | Монарх / Янтарный Монарх |
| The Servant (of the Monarch) | Слуга (Монарха) |
| Beings of New World | Существа Нового Света |
| New World / Old Continent | Новый Свет / Старый Свет |
| idol / aspect | идол / аспект |
| The Observer / The One Who Observes / The One Who Guards | Наблюдатель / Тот, кто наблюдает / Тот, кто стережёт |
| All-Seeing Eye | Всевидящее Око |
| The Accuser / The One Who Accuses / The One Who Exacts | Обвинитель / Тот, кто обвиняет / Тот, кто взыскивает |
| The Speaker / The One Who Speaks | Глашатай / Тот, кто вещает |
| The Seeker | Искатель |
| The Invocation of the Lord on Amber Throne | «Воззвание к Владыке на Янтарном троне» |
| Invocation | Воззвание |
| energy relays | передатчики энергии |
| conductors | проводники |
| Boundless / Boundless Mystery | Безграничное / Безграничная Тайна |
| Boundless Secrets, Boundless Realms | Безграничные Тайны, Безграничные Царства |
| Great Mystery | Великая Тайна |
| Adept / Secret motivation | Адепт / тайная мотивация |
| Adept’s Knowledge / Destroying evidence | знания Адепта / уничтожение улик |
| Epitasis | эпитасис |
| Apnea / Fog / Moths / Ex Machina | апноэ / туман / мотыльки / Ex machina |
| Dangers / Behavior / Conflict | опасности / поведение / конфликт |
| Synergy / Subterfuge / Rhetoric / Evidence | слаженность / хитрость / риторика / улики |
| Confrontation / Diplomacy / Duel / Alliance | столкновение / дипломатия / поединок / союз |
| Extras / Subplots / Incidents | дополнения / побочные линии / происшествия |
| Stone Gaze / Sketch | «Каменный взгляд» / «Набросок» |
| The Disappearance of Attorney Czachowski | «Исчезновение адвоката Чаховского» |
| The Overheard | подслушанные разговоры |
| Psychotic Episodes | психотические эпизоды |
| Motivation 1–4: Family member / Old friend / Sympathizer / Adept | Мотивация 1–4: родственник / старый друг / сочувствующий / Адепт |
| Evidence (table) | улики |
| homichlophobia / mottephobia | гомихлофобия / моттефобия |
| echopraxia / synaesthesia | эхопраксия / синестезия |
| majordomo / chief of security / security | мажордом / начальник охраны / охрана |
| smorgasbord, buffet | шведский стол |
| music box | музыкальная шкатулка |
| incense | благовония |
| Songs of New World | «Песни Нового Света» |
| luminal | люминал |
| solvent / ornamental inkwell | растворитель / узорная чернильница |
| restricted part of the house | закрытая часть дома |
| The Power of Ritual – Forsaken Magic Practices | «Сила ритуала. Забытые магические практики» |
| The Power of Gemstones. A treaty on preternatural properties of rare minerals | «Сила самоцветов. Трактат о сверхъестественных свойствах редких минералов» |
| The Art of Reading Symbols | «Искусство чтения символов» |
| The Hidden. The history of secret associations in the United States | «Сокрытое. История тайных обществ в Соединённых Штатах» |
| Friedman equation | уравнение Фридмана |

Официальные формы из глоссария: Keeper — Хранитель; Keeper of Arcane Lore — Хранитель тайных знаний; investigator — сыщик; Sanity roll — проверка Рассудка; bonus die — бонусная кость; Cthulhu Mythos — Мифы Ктулху; King in Yellow — Король в жёлтом; Carcosa — Каркоза; Yuggoth — Юггот; Hypnos — Гипнос; phobia — фобия.
