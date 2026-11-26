# World War Cthulhu: Cold War — сторона игроков (часть «cw-a»)

Книга `wwc-cold-war-en` (Cubicle 7, 2016; 7-я редакция, хотя метка библиотеки — [EN 6e]). Часть cw-a — с. 1–62:
вступление, история холодной войны, разведывательные службы, Секция 46, создание сыщика, Доверие, шпионское ремесло.
Часть Хранителя (с. 63 и дальше, включая титул «Part Three» на физ. 63) — часть cw-b.

Страницы: печатная = физической (смещение **0**; «5» на физ. 5, «26» на физ. 26, «62» на физ. 62); без номера — физ. 1
(обложка), 4 и 24 (титулы частей). Русского перевода в базе и библиотеке нет (поиск «Section 46», «Секция 46»,
«World War Cthulhu», имён — пусто); русский текст — наш перевод (`translated`). Эпоха — `1940s-1980s`, свод — `core`.

## Записи (100 в `kb/books/wwc-cold-war-en/`)

- `rule` — 47: «Введение»; «Холодная война: краткая история» + 4 периода; «Разведывательные службы» → «Разведка и холодная
  война» и «Разведслужбы мира» → 4 региона; «Работа на Секцию 46»; глава создания сыщика «Офицеры, агенты и прочие шпионы»
  → 17 разделов (шаги 1–10, лист, быстрый способ, пример, перенос сыщиков, новые навыки, «Доверие» → 5 подразделов,
  «Влияние H» под шагом 7); «Шпионское ремесло» → 8 разделов.
- `organization` — 41: Секция 46, Сеть N, SOE, OSS, «Пять глаз» (UKUSA/ECHELON) и 36 разведок и служб безопасности
  (mi6, mi5, gchq, cia, dia, nsa, nro, fbi, asis, nzsis, rcmpss, dsd, cse, gcsb, bnd, sdece, kgb, gru, stasi, hva, sb,
  securitate, savak, mossad, aman, shin-bet, bfss, raw, intelligence-bureau, isi, central-investigation-department,
  ministry-for-public-security, psia, secretaria-de-inteligencia, sni, dina).
- `character` — 6: N, H, Ким Филби, Джеймс Джизес Энглтон, Маркус Вольф, Файза Сукайна Канаан (сыщик из примера, `pregen`, статблок).
- `location` — 2: Сенчури-хаус, Клуб Грина (оба `part_of` `coc:location:london`).
- `handout` — 4: записка об аугсбургском инциденте с ответом N; коды срочных сообщений Секции 46; сводка «Most Secret»;
  оперативный отчёт о проникновении в усадьбу.
- Картинки — 9 (`art-cw-a.json` → `art-cw-a-proposals.json`, применены): 4 раздатки, лист сыщика (2 стороны) у
  `rule/character-sheet-summary`, эмблемы ЦРУ, КГБ, Моссада; рамки вырезки — `boxes-cw-a.json`. Атмосфера — 18 страниц в
  `atmosphere-cw-a.json`.
- Черновики общих записей (не в `kb/`, проверены схемой — `new-shared/`): навыки `coc:skill:tradecraft`,
  `coc:skill:organisation-knowledge` (12 специализаций-регионов), `coc:skill:signals`, `coc:skill:military-science`;
  профессия `coc:occupation:wwc-intelligence-officer`. После переноса добавить ссылки: навыки в статблоке Файзы
  (`skills[].skill`), `occupation_ref` Файзы, `refs` правил «Новые навыки…», шагов 5–6, «Шпионское ремесло».
- Предложения — `proposals-cw-a.json` (8): абзацы и источники World War Cthulhu: Cold War у `coc:skill:art-craft`
  (Подделка), `coc:skill:explosives` и `coc:skill:science` (Криптография — основные навыки, на листе 00%),
  `coc:character:j-edgar-hoover` (Первая красная угроза). Пробный прогон `apply.py` — 8 правок ложатся.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) | 1 | не взято — обложка; `atmosphere-cw-a.json` |
| Contents | 2–3 | не взято — оглавление (использовано для плана частей) |
| Credits; Disclaimer | 3 | не взято — выходные данные |
| Part One: Introduction (титул) | 4 | не взято — оформление; `atmosphere-cw-a.json` |
| Introduction: What is World War Cthulhu?; World War Cthulhu: Cold War; Cthulhu Mythos | 5 | `rule/introduction` |
| Real Horrors; Mood | 6 | `rule/introduction` |
| The Cold War: A Brief History | 7 | `rule/the-cold-war-a-brief-history` |
| The Origins of the Cold War (1917–1950); World War Two; The Aftermath of Victory | 7–8 | `rule/the-origins-of-the-cold-war` |
| Post-War Germany | 8 | `rule/the-origins-of-the-cold-war` |
| From Korea to Cuba (1950–1962); Korea, China and the Developing World | 8–9 | `rule/from-korea-to-cuba` |
| Proxy Wars (врезка) | 9 | `rule/from-korea-to-cuba` |
| Nuclear Escalation | 9–10 | `rule/from-korea-to-cuba` |
| The Cambridge Spy Ring (врезка) | 10 | `rule/from-korea-to-cuba`, `character/kim-philby` |
| The Cuban Missile Crisis; сноска 1 | 10–11 | `rule/from-korea-to-cuba` |
| The Spectre of Nuclear Annihilation (врезка) | 11 | `rule/hotline-to-detente` |
| Hotline to Détente (1963–1972); The Vietnam War | 11–12 | `rule/hotline-to-detente` |
| The Vietnamese at Versailles; The Vietnam War in World War Cthulhu: Cold War (врезки) | 12 | `rule/hotline-to-detente` |
| Revolution, Repression and Rapprochement | 12 | `rule/hotline-to-detente` |
| The Second Cold War (1973–1980); The Oil Crisis; сноска 2 | 13 | `rule/the-second-cold-war` |
| Afghanistan and Iran | 13–14 | `rule/the-second-cold-war` |
| International Terrorism; The End of the Cold War (1981–1991) | 14 | `rule/the-second-cold-war` |
| Dealing with Terrorism (врезка) | 14 | `rule/the-second-cold-war` |
| Intelligence Agencies; Intelligence and the Cold War | 15 | `rule/intelligence-agencies`, `rule/intelligence-and-the-cold-war` |
| Forms of Intelligence (HUMINT, SIGINT, COMINT, ELINT, IMINT, TECHINT, OSINT) | 15–16 | `rule/intelligence-and-the-cold-war` |
| Intelligence and Security Agencies Around the World | 16 | `rule/intelligence-and-security-agencies-around-the-world` |
| The Western Allies | 16–18 | `rule/the-western-allies`; организации cia, dia, nsa, nro, mi6, mi5, gchq, asis, nzsis, rcmpss, dsd, cse, gcsb, bnd, sdece, fbi |
| James Jesus Angleton (врезка) | 17 | `rule/the-western-allies`, `character/james-jesus-angleton` |
| Black Propaganda (врезка) | 18 | `rule/the-western-allies`, `organization/cia`, `organization/kgb` |
| The Eastern Bloc | 18–19 | `rule/the-eastern-bloc`; организации kgb, gru, stasi, hva, sb, securitate |
| The Man Without a Face (врезка) | 19 | `rule/the-eastern-bloc`, `character/markus-wolf` |
| Honey Traps (врезка) | 19 | `rule/the-eastern-bloc`, `organization/hva` |
| Africa and the Middle East | 19–20 | `rule/africa-and-the-middle-east`; организации savak, mossad, aman, shin-bet, bfss |
| ECHELON (врезка) | 20 | `rule/africa-and-the-middle-east`, `organization/five-eyes` |
| Elsewhere in the World | 21 | `rule/elsewhere-in-the-world`; организации raw, intelligence-bureau, isi, central-investigation-department, ministry-for-public-security, psia, secretaria-de-inteligencia, sni, dina |
| Assassinations (врезка) | 21 | `rule/elsewhere-in-the-world` |
| Section 46: The Wartime Network N | 22 | `organization/n` |
| Section 46 | 22 | `organization/section-46`, `location/century-house` |
| Tentacles Across the World | 22 | `organization/section-46`, `organization/oss`, `organization/soe` |
| N, The Ghost of St James’s | 22–23 | `character/n`, `location/greene-club` |
| H, The Ghost of Dreams | 23 | `character/h` |
| Working for Section 46 | 23 | `rule/working-for-section-46` |
| Part Two: Investigator’s Resources (титул) | 24 | не взято — оформление; `atmosphere-cw-a.json` |
| Officers, Agents and Other Spies; Creating your Investigator; десять шагов | 25 | `rule/officers-agents-and-other-spies` |
| Character Sheet Summary (1–11, лист с номерами) | 26–27 | `rule/character-sheet-summary` (+ 2 картинки) |
| Step One: Generate Characteristics | 28 | `rule/step-one-generate-characteristics` |
| Step Two: Investigator’s Age | 28 | `rule/step-two-investigators-age` |
| Step Three: Other Attributes | 28–29 | `rule/step-three-other-attributes` |
| Step Four: Identity and Name | 29 | `rule/step-four-identity-and-name` |
| Step Five: Occupation, Skills and Trust; Prior Career; Direct Recruits; Intelligence Officer; Trust | 29–30 | `rule/step-five-occupation-skills-and-trust`; черновик `coc:occupation:wwc-intelligence-officer` |
| Step Six: Specialised Intelligence Agency Training; Intelligence Analyst; Field Officer; Surveillance Officer; Technical Specialist; Covert Actions Operative | 30–31 | `rule/step-six-specialised-intelligence-agency-training` |
| Agents: An Alternative to Playing an Intelligence Officer (врезка) | 31 | `rule/step-six-specialised-intelligence-agency-training` |
| Step Seven: Create a Backstory; Using Random Tables for Inspiration; Personal Description; Why are you a Spy? (1d10) | 32 | `rule/step-seven-create-a-backstory` (таблица) |
| Becoming a Double Agent; Significant People (1d10); Treasured Possessions (1d10); Personality Trait | 33 | `rule/step-seven-create-a-backstory` (таблицы) |
| Personality (1d4); Meaningful Locations (1d10); руководитель задания | 34 | `rule/step-seven-create-a-backstory` (таблицы) |
| Regaining Sanity; Key Background Connection | 35 | `rule/step-seven-create-a-backstory` |
| Option: The Influence of H (врезка) | 35 | `rule/option-the-influence-of-h` |
| Step Eight: Brush with the Mythos (1d10) | 35–36 | `rule/step-eight-brush-with-the-mythos` (таблица) |
| Step Nine: Recruitment; Indoctrination | 36–38 | `rule/step-nine-recruitment` |
| Quick-Fire Method of Investigator Creation (врезка) | 37 | `rule/quick-fire-method-of-investigator-creation` |
| Step Ten: Equipping your Investigator; Living Standards; Cash and Assets (таблица); Equipment | 38–39 | `rule/step-ten-equipping-your-investigator` |
| Example of Investigator Creation | 40–41 | `rule/example-of-investigator-creation` (примеры), `character/faizah-sukaynah-kanaan` |
| Adapting Call of Cthulhu Investigators | 41 | `rule/adapting-call-of-cthulhu-investigators` |
| Adapting Investigators from The Darkest Hour; Convert…; Age…; Convert Specialist Skills (таблица); Retraining; Roll for H’s Influence; Assign Trust | 41–42 | `rule/adapting-investigators-from-the-darkest-hour` |
| New Skills and New Uses for Existing Skills; Cryptography and Demolitions (врезка) | 42 | `rule/new-skills-and-new-uses-for-existing-skills`; предложения к `coc:skill:explosives`, `coc:skill:science` |
| Art/Craft (Forgery) (05%) | 42–43 | `rule/new-skills-and-new-uses-for-existing-skills`; предложение к `coc:skill:art-craft` |
| Military Science (00%) | 43 | то же правило; черновик `coc:skill:military-science` |
| Organisation Knowledge (01%) | 43–44 | то же правило; черновик `coc:skill:organisation-knowledge` |
| Signals (01%) | 44 | то же правило; черновик `coc:skill:signals` |
| Tradecraft (01%) | 44–45 | то же правило; черновик `coc:skill:tradecraft` |
| Trust; Levels of Trust | 45–46 | `rule/trust` |
| Using Trust; Pushing Trust | 46–47 | `rule/using-trust` |
| Trust Tests | 47 | `rule/trust-tests` |
| Eroding Trust; Magnitude of the Offence; Source of Information (таблица) | 47–48 | `rule/eroding-trust` |
| Building Trust; Increasing Current Trust Points | 48–49 | `rule/building-trust` |
| Establishing Trust | 49 | `rule/establishing-trust` |
| Tradecraft; General Considerations | 50 | `rule/tradecraft` |
| The Moscow Rules (врезка) | 51 | `rule/the-moscow-rules` |
| Disguises and Cover Identities; Open and Covert Operations | 51 | `rule/disguises-and-cover-identities` |
| Disguises; Cover Identities | 52 | `rule/disguises-and-cover-identities` |
| (записка «Personal note… Augsburg incident» с ответом N) | 52 | `handout/n-note-augsburg-incident` |
| Good Cover Identities (врезка); Threats to Cover Identities | 53 | `rule/disguises-and-cover-identities` |
| Surveillance and Counter-surveillance; Covert Surveillance; Vehicular Surveillance; Being Followed | 54–55 | `rule/surveillance-and-counter-surveillance` |
| Meeting Contacts | 55 | `rule/surveillance-and-counter-surveillance` |
| Finding and Running Assets; Recruitment; Communicating with Assets | 55–56 | `rule/finding-and-running-assets` |
| Communications and Cryptography; Microdots | 56–57 | `rule/communications-and-cryptography` |
| Encryption, Codes and Ciphers; Flash Messages | 57 | `rule/communications-and-cryptography` |
| (документ «Section 46 Confidential — New Flash Codes») | 57 | `handout/section-46-flash-codes` |
| One-Use Pads; Electronic Transmissions and Bugs | 58 | `rule/communications-and-cryptography` |
| Counterintelligence; Killing Assets | 58–59 | `rule/counterintelligence` |
| Subtler Means; Denial of Information | 59 | `rule/counterintelligence` |
| Deception and Misinformation; Passive and Active Camouflage | 59–60 | `rule/deception-and-misinformation` |
| Discredited and False Information; Deception and Cover Stories | 60–61 | `rule/deception-and-misinformation` |
| (документ «Most Secret») | 60 | `handout/most-secret-shifting-sands` |
| Disinformation and Misinformation | 61 | `rule/deception-and-misinformation` |
| Black Bag Operations | 61–62 | `rule/black-bag-operations` |
| (бланк «Operational Report — Most Secret») | 62 | `handout/operational-report-stately-home` |

## Не взято

- Обложка, оглавление, выходные данные и дисклеймер (с. 1–3), титулы частей (с. 4, 24) — не правила и не сюжет;
  картинки — в `atmosphere-cw-a.json`.
- Иллюстрации без подписи (с. 6, 9, 13, 15, 30, 35, 38, 40, 44, 47, 51, 55, 59) — атмосфера (проверены глазами: ни одна не
  портрет персонажа записи). Картинки 456×… на с. 9–21, 31, 35, 37, 53 — фоны врезок (бумага), не иллюстрации.
- Скрытый текст бланка на с. 62 (под чёрными полосами: «Stately home imcursion», «Smithson H A», «26/7/74 to 31/7/74») — на
  печати не виден; упомянут только в `quality.notes` раздатки.
- Реальные лица и группы, упомянутые мимоходом (Андропов, Гелен, Пеньковский, Гордиевский, Беленко, Георгий Марков,
  Сталин, Трумэн, Кеннеди, Хрущёв, Никсон и др.; «Фракция Красной армии», «Красные бригады», FALN, НФОП, ООП, ИРА, НАТО,
  ОПЕК, CND, SANE) — остаются текстом правил. Никсон, «Чёрный сентябрь», Баадер и др. — персонажи/организации части cw-b.
- Кодовые обозначения раздаток (BANQUO’S GHOST, SHIFTING SANDS, RED GLADIOLUS), Кин, сэр Реджинальд, Фабриция Падовано —
  только текст раздаток: книга их не раскрывает.
- Лагерь X (Camp X, озеро Онтарио), Кавершем-парк, Норманненштрассе — текстом (нет общих записей Канады/Беркшира; Берлин —
  театр части cw-b).
- Таблицы с броском (1d10 ×5, 1d4) — внутри правил (`tables`): записи `table` книги в базе не заводятся; кандидаты в
  `coc:table:wwc-*` — вопрос владельцу.

## Опечатки и сомнения

| Где | Напечатано | Ожидалось | В записи |
|---|---|---|---|
| с. 25 | «presented in eight steps» | десять шагов (список на той же странице) | исправлено, errata `rule/officers-agents-and-other-spies` |
| с. 28 | «Roll twice to generate a Luck score (see Luck, above)» | Удача описана ниже, в шаге 3 (с. 29) | исправлено, errata `rule/step-two-investigators-age` |
| с. 30 | «Regardless of what occupation you chose in Step Four» | Step Five | исправлено, errata `rule/step-six-…` |
| с. 39 | «CR x 2 (£2 - $18)» | £18 | исправлено, errata `rule/step-ten-…` |
| с. 40 | проверка Интеллекта «60» при ИНТ 80 | 80 | как напечатано, errata `rule/example-of-investigator-creation`, `character/faizah-sukaynah-kanaan` |
| с. 40 | 160 пунктов личных интересов, распределено 145 | 160 | как напечатано, errata там же |
| с. 2 | «Step Five: Occupation and Skills», «Example of Investigator Creatrion», «Step Ten: Equiping», «General Considerarions», «Diguises» | — | оглавление; в `aliases` |
| с. 42 | старение 25–39 лет, переподготовка «25–40 лет» | — | как напечатано, `quality.notes` |
| с. 26 | базы на листе: Бухгалтерское дело 10%, История 20%, Криптография 00%, Взрывчатка 00% | «Книга хранителя»: 05%, 05%, 01%, 01% | как напечатано, `quality.notes` `rule/character-sheet-summary` |
| с. 57 | «SPACIAL BREACH» | SPATIAL | словесная, как напечатано (Р-39) |
| с. 17 | «New Zealand Secret Intelligence Service», «Defence Signals Division» | настоящие названия — Security Intelligence Service, Directorate | как в книге, `quality.notes` |

## Термины (English → русский, наш выбор; переводчик книги берёт эти формы)

| English | Русский |
|---|---|
| Section 46 | Секция 46 |
| Network N | Сеть N |
| N, The Ghost of St James’s | N, призрак Сент-Джеймса |
| Lord Brichester | лорд Бричестер |
| H, The Ghost of Dreams | H, призрак снов |
| Greene Club | Клуб Грина |
| Century House | Сенчури-хаус |
| Trust | Доверие |
| Trust roll | проверка Доверия |
| Trust test | тест Доверия |
| Pushing Trust | повторная проверка Доверия |
| Eroding Trust / Building Trust / Establishing Trust | подрыв / укрепление / установление Доверия |
| Enemy Agent / Unknown / Partially Trusted / One of Us / Beyond Reproach | вражеский агент / неизвестный / частичное доверие / свой / вне подозрений |
| Weak / Standard / Strong Source | слабый / обычный / сильный источник |
| Minor / Moderate / Major Offence | мелкий / средний / крупный проступок |
| Tradecraft (skill and chapter) | Шпионское ремесло |
| Organisation Knowledge | Знание организаций |
| Signals | Связь |
| Military Science | Военное дело |
| Art/Craft (Forgery) | Искусство/ремесло (подделка) |
| Cryptography / Demolitions | Криптография (специализация Науки) / Взрывчатка |
| Command / Gunnery / Radio Operations (The Darkest Hour) | Командование / Артиллерийское дело / Радиодело |
| Intelligence Officer | офицер разведки |
| Intelligence Analyst / Field Officer / Surveillance Officer / Technical Specialist / Covert Actions Operative | аналитик разведки / оперативный офицер / офицер наблюдения / технический специалист / оперативник тайных операций |
| Agent | агент |
| Prior Career / Direct Recruits | прежняя карьера / прямой набор |
| Specialised Intelligence Agency Training | подготовка в разведке |
| Brush with the Mythos | соприкосновение с Мифами |
| Recruitment / Indoctrination | вербовка / психологическая обработка |
| distant / general / immediate threat | далёкая / общая / непосредственная угроза |
| Why are you a Spy? | Почему вы шпион? |
| Personality Trait: Bruiser / Practical / Thinker / Leader | тип личности: Громила / Практик / Мыслитель / Лидер |
| Key Background Connection | ключевая связь |
| Quick-Fire Method | быстрый способ |
| Living Standards; Penniless / Poor / Average / Wealthy / Rich / Super Rich | уровень жизни; без гроша / бедный / средний / состоятельный / богатый / сверхбогатый |
| Spending Level | уровень трат |
| Moscow Rules | Московские правила |
| cover identity / disguise | легенда / маскировка |
| grey man | «серый человек» |
| dry cleaning | «химчистка» |
| asset / case officer / walk-in | источник (агент) / куратор / инициативник |
| dead drop | тайник |
| honey trap | «медовая ловушка» |
| microdot / one-use pad / flash message | микроточка / одноразовый блокнот / срочное сообщение |
| bug | «жучок» |
| Maskirovka | маскировка (Maskirovka) |
| disinformation / misinformation | дезинформация / «информационный шум» |
| black bag operation / wet work | операция «чёрного мешка» / «мокрое дело» |
| HUMINT, SIGINT (COMINT, ELINT), IMINT, TECHINT, OSINT | агентурная, радиоэлектронная (перехват связи, электронных излучений), видовая, техническая разведка, разведка по открытым источникам |
| SIS (MI6) / Security Service (MI5) / GCHQ | Секретная разведывательная служба (МИ-6) / Служба безопасности (МИ-5) / Центр правительственной связи (GCHQ) |
| Stasi (MfS) / HVA | Штази / Главное управление разведки ГДР (HVA) |

## Ссылки на записи линейки

- Ссылок на несуществующие записи в файлах части нет (проверено `tools/check.py --limit 1000` по 100 файлам).
- Добавлены ссылки на записи части cw-b, уже созданные: `organization/black-brotherhood` (раздатка с. 52),
  `organization/black-september-organization` (`rule/the-second-cold-war`).
- Для других частей: `organization/section-46`, `organization/n`, `character/n`, `character/h`, разведки
  (`organization/<slug>` по списку выше) — существуют.
