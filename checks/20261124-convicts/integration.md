# Convicts & Cthulhu — сведение линейки (2026-11-25)

Книги: `convicts-cthulhu-en` (+ `convicts-cthulhu-players-en` — только источники), `convicts-tol-01-en` … `convicts-tol-12-en`,
`convicts-tol-15-en`. Отчёты частей о покрытии — `convicts-{core,tol-a,tol-b,tol-c,tol-d}.md` (строки о перенесённом при
сведении поправлены в `convicts-tol-c.md`, `convicts-tol-d.md`). Скрипты сведения — во временной папке, в базу не входят.

## 1. Общие записи из черновиков

**Профессии — 43 записи `kb/occupations/convicts-*.json`:**

- 14 профессий основной книги, которые ToL #5 перепечатывает в расширенной редакции (одна запись на id):
  `convicts-career-criminal`, `-clever-man-or-woman`, `-doctor`, `-domestic-servant`, `-down-on-luck-craftsman`,
  `-fallen-clergyman`, `-farmer-settler`, `-hunter-gatherer`, `-labourer`, `-lawyer`, `-merchant`, `-nsw-corps-officer`,
  `-political-agitator`, `-publican`. Первый источник — основная книга (с. 21–23) и Players Version, затем ToL #5. Пункты
  навыков, Средства и список навыков — по основной книге (Р-125). Описание и «связи» (`contacts`) — из ToL #5 (в основной
  книге их нет); первой фразой описания оставлен класс профессии из основной книги («Каторжная профессия.» и т. п.).
  Псевдонимы — обеих книг. Расхождения ToL #5 — в `quality.notes` (у профессии нет поля `source_variants`):
  Doctor — Чтение и письмо (английский) + один навык вместо двух любых; Fallen Clergyman — Чтение и письмо вместо Слуха;
  Lawyer — Чтение и письмо вместо Родного языка; Merchant — «Ловкость рук или Чтение и письмо»; Clever-Man, Hunter-Gatherer —
  Средства в европейской колонии 0–5. Сверено по страницам (Doctor: ToL #5 с. 12, основная книга с. 22).
- 27 профессий только из ToL #5: `convicts-botanist-naturalist`, `-explorer-surveyor`, `-fallen-aristocrat`, `-ferry-pilot`,
  `-forger`, `-gambler-confidence-trickster`, `-government-clerk-bureaucrat`, `-indigenous-bush-constable-tracker`,
  `-indigenous-guide-explorer`, `-indigenous-voyager`, `-mapmaker`, `-marine`, `-merchant-sailor`, `-mineralogist`,
  `-missionary`, `-naval-officer`, `-naval-rating`, `-nsw-corps-soldier`, `-parson-chaplain`, `-poacher`, `-sealer-whaler`,
  `-ships-purser`, `-shopkeeper`, `-smuggler`, `-spy`, `-supercargo`, `-undertaker`.
- 2 профессии ToL #2: `convicts-french-naturalist`, `convicts-french-occult-explorer`.
- Во всех: «Актёрское мастерство» → «Актёрская игра» (форма `kb/occupations`), термины шага 2, служебные фразы
  «черновик… ведущий переносит» убраны из `quality.notes`.

**Навык:** `coc:skill:gambling` («Азартные игры», ToL #5; дублей нет — `gamble-recklessly` из «Масок» — другой навык).
Ссылка на него проставлена у Элайзы Петти (`convicts-tol-10-en/character/eliza-petty`, раньше не связана).

**Заклинания — 6 записей `kb/spells/`** (дублей по `name.en` нет): `ritual-of-the-yellow-zombie` (ToL #3),
`resurrection-according-to-lucifers-pelt` (ToL #6), `summon-thing-from-the-bone-pit` (ToL #8), `call-dismiss-zstylzhemgni`,
`enchant-wound` (ToL #10), `enchant-ritual-bell` (ToL #15). У `enchant-ritual-bell` добавлена ссылка `refs` на
`coc:creature:zu-che-quon` и пометка о похожем заклинании Grand Grimoire «Зачаровать колокола ужаса» (`variant_of` не
ставил — книга их не связывает).

## 2. Термины одной формой (формы основной книги)

93 файла (скрипт по всем строкам, кроме `aliases`, `corrections`, `source_variants`, английских полей):

| Термин | Было | Стало | Мест |
|---|---|---|---|
| Ticket of Leave | «билет на поселение» (tol-b), в т. ч. название выпуска «Билет на поселение» № N | «отпускной билет» (с согласованием падежа) | 38 |
| Government House | «Дом губернатора» (tol-b, #6–#7) | «Дом правительства» | 22 |
| The Rocks | «Скалы» (#8, и 5 мест в основной книге), несклоняемое «в Рокс» (#5, #6, #15), испорченное «Роксуи» (основная книга) | «Рокс», склоняется как в основной книге (в Роксе, Рокса, к Роксу) | 68 |
| assigned convict | «приписанный каторжник» (все ToL) | «распределённый каторжник»; «приписан к кому-то» (глагол) оставлен | 36 |

Переименованы (старое имя — в `aliases`, `corrections` с Р-184): `convicts-tol-06-en/location/hole-in-the-rocks` и
`scene/the-hole-in-the-rocks` («Дыра в Роксе»), `location/rocks-convict-burial-grounds`, `location/double-death-site-iv`,
`location/stitch-office` («Кабинет Стича в Доме правительства»), `convicts-tol-15-en/location/charles-warehouse`.

## 3. Предложения

Все шесть файлов легли целиком, без ручных правок (применены до замены терминов, чтобы куски `old` совпали; новые тексты
потом прошли замену): `proposals-core.json` — 9 правок 5 записей (`coc:weapon:flintlock`, `brown-bess-musket`,
`war-boomerang`, `spear-thrown`, `coc:location:sydney`); `proposals-tol-a.json` — 4 (`convicts-cthulhu-en/location/georges-river`);
`proposals-tol-b.json` — 6 (`coc:skill:read-and-write-language`, `explosives`, `charm`); `proposals-tol-c.json` — 4
(`convicts-cthulhu-en/character/john-harris`); `proposals-tol-d.json` — 3 (`convicts-tol-01-en/character/john-styles`);
`proposals-after-shared-tol-b.json` — 11 (`occupation_ref` у 10 персонажей ToL #5, ссылка на заклинание у Стича).
После них `normalize_dice` исправил «1D8»/«1D6» в цитатах `source_variants` и `corrections` оружия (4 файла).

## 4. Дубли между частями

- **Джозеф Бэнкс** — есть и в основной книге (набросок «Огни Ботани-Бей»), и в ToL #12: записи оставлены обе, связаны
  `same_as` в обе стороны (у основной книги — роль в наброске, у #12 — биография и портрет).
- **Томас Джеймисон** — биография ToL #11 (с. 5–6) перенесена абзацем «В „Отпускном билете“ № 11…» в `legend`
  `convicts-cthulhu-en/character/thomas-jamison` (Р-125) вместе с его ролью в сценарии (с. 10), источники добавлены; в
  `organization/colonial-medical-service` вместо биографии — ссылка.
- **Уильям Патерсон** — врезка ToL #12 (с. 9) перенесена в `convicts-cthulhu-en/character/william-paterson` (биография,
  роль в «Падших звёздах»), туда же портрет (файл переехал в `app/art/characters/convicts-tol-d-william-paterson.webp`);
  имя дополнено до «Уильям Патерсон» / «William Paterson» (Р-41, прежнее — в `aliases`); в `rule/the-scientific-elite` — ссылка.
- **Джон Харрис** — врезка ToL #10 (с. 4) перенесена так же в `convicts-cthulhu-en/character/john-harris`; в сценарии
  #10 — ссылка. Возраст «~50 (born 1754)» из заголовка статблока (с. 14) записан в `age` — Скорость 6 сходится с
  возрастной поправкой (снято предупреждение `check.py`).
- **«First People(s) of the Blue Mountains»** — #12 (с. 12) перепечатывает врезку #7 в сокращении: запись #12 слита в
  `convicts-tol-07-en/rule/first-peoples-of-the-blue-mountains` (источник #12, название перепечатки в `aliases`, ссылка на
  стоянку гандангарра); файл #12 удалён, ссылка в `convicts-tol-12-en/rule/exploring-the-blue-mountains` переписана.
- **Карты** «Principal Regions of His Majesty’s Colony at New South Wales» (#10) и «План колонии Новый Южный Уэльс, 1802»
  (основная книга) — сверено по изображениям: разные карты (другой рисунок и охват — крупный план Порт-Джексона с
  Файв-Доком); не слиты, карта #10 получила `shows: convicts-cthulhu-en/location/new-south-wales`.
- Попутно: **Тварь из Ямы** (#15) книга называет «Zu-chequon» (с. 23) — `same_as: coc:creature:zu-che-quon`, псевдоним
  «Зу-че-куон» (выпуск «unstatted» — для игры годится статблок справочника).

## 5–6. Атмосфера и проверки

- `merge_atmosphere.py` для пяти частей: добавлено 105 страниц (core 54, tol-a 10, tol-b 13, tol-c 14, tol-d 14).
- `tools/check.py` по всем книгам линейки, `kb/occupations`, `kb/skills`, `kb/spells`, `kb/weapons`, Сиднею — 0 ошибок и
  0 предупреждений в наших файлах (30 ошибок — висячие ссылки чужих книг `wwc-*`, которые сейчас переносят).
- `scenario_check` → `scenario/`: 10 находок — 6 «нет сцен» у набросков основной книги (так задумано, у книги там нет
  сцен) и 4 сцены без участников (низкий уровень).
- `completeness` → `completeness/`: `text.gap` 2 (выходные данные с. 1–4 основной книги и Players Version — не взято по
  отчёту core); `art.uncovered` 18 и `art.record_without` 50 — по отчётам частей это рамки врезок (536×1492 и т. п.) и
  гравюры без подписи; `context.incomplete` 11 — #15 «unstatted» и книги без чисел чтения.

## Остаток находок

- Ещё расходятся формы (в задание не входили): Commissariat — «интендантство» (основная книга, 17 мест) против
  «комиссариат» (ToL #1, #3, #5, #15, ~35 мест); free settler — «свободный поселенец» (основная книга, #1–#7) против
  «вольный поселенец» (#8–#15, около 20 мест); Charm/Bootlick — «Обаяние/Подхалимство» (#5, #6, принято псевдонимом
  `coc:skill:charm`) против «Обаяние/Угодничество» (#3, #4, #10) и «Обаяние (в том числе подхалимство)» (основная книга).
- Картинки: 68 находок `completeness` (см. выше) — разобрать, нет ли среди них портретов (например, #5 с. 6, 8, 9, 18 —
  страницы биографий Нанбарри, Фултона, Кэтчпол, Джонса; по отчёту tol-b это рамки врезок).
- `checks/20261124-convicts/art-tol-d.json` по-прежнему называет целью портрета Патерсона правило #12 — при повторном
  прогоне `add_images.py` поправить цель на `convicts-cthulhu-en/character/william-paterson`.
- ToL #11, с. 2: «In February 1808 … (with Governor King's approval) … three years later (under Governor Bligh)» —
  хронология книги не сходится (Кинг уехал в 1806 году); в записи как напечатано, без `errata` (не механика).

## Вопросы владельцу

1. Свести ещё три формы (выше): Commissariat → «интендантство», free settler → «свободный поселенец», Charm/Bootlick →
   одна форма? Рекомендую формы основной книги.
2. Внести термины линейки (Ticket of Leave, Government House, The Rocks, assigned convict и др.) в глоссарий `kb/terms`?
3. ToL #15 в библиотеке — «unstatted»: зарегистрировать «statted» версию (статблоки, стоимость заклинания, награды)?
4. Вопросы частей остаются открытыми: tol-a — общая запись Австралии вместо `convicts-tol-02-en/location/new-holland`;
   склад Лорда (#1) — Сидней или Парраматта; tol-c — портрет пожилой женщины #9 с. 9 (Элизабет Патерсон?); навыки
   существ «Know Fears» и т. п. без записей; core — Alcheringa Dream Lore / Dream Song ждут «Secrets of Australia».
