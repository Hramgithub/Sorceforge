# «Компаньон хранителя» — часть investigators (с. 5–42)

Введение и глава 1 «Investigators». Русский текст — наш перевод (`translated`, Р-21), `axes.ruleset: core`, эпоха `any`
(Р-212). Правки общих записей (навыки, роды занятий) — в `proposals-investigators.json` (91 предложение, 45 записей;
пробный прогон `pipeline/integrate/apply.py --dry-run` проходит).

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Introduction | 5–6 | `coc:rule:kc-introduction` |
| Who Is This Book For? | 5 | `coc:rule:kc-introduction` (текст, псевдоним) |
| What’s in This Book? | 5–6 | `coc:rule:kc-introduction` (текст, псевдоним) |
| New to Call of Cthulhu? | 7 | `coc:rule:kc-new-to-call-of-cthulhu` |
| What Kind of Horror? / What Does a Player Do? / What Does an Investigator Do? / What Next? | 7 | `coc:rule:kc-new-to-call-of-cthulhu` (текст, псевдонимы) |
| Chapter 1: Investigators (вступление) | 9 | `coc:rule:kc-investigators` |
| Alternative Investigator Creation; Characteristics | 9 | `coc:rule:kc-alternative-investigator-creation` |
| Roll Characteristics | 9 | `coc:rule:kc-alternative-investigator-creation` |
| Table 1: Characteristic Spreads | 10 | `coc:table:kc-characteristic-spreads` |
| Assign Characteristics | 10 | `coc:rule:kc-alternative-investigator-creation` |
| Revised Movement Rate (MOV) | 10 | `coc:rule:kc-revised-movement-rate` |
| Occupations & Skills | 11 | `coc:rule:kc-occupations-and-skills` |
| Option: Personalization | 11 | `coc:rule:kc-option-personalization` |
| Credit Rating (Skill) (врезка) | 12 | `coc:rule:kc-occupations-and-skills` (текст); предложение для `coc:skill:credit-rating` |
| Personal Interest Points | 12 | `coc:rule:kc-personal-interest-points` |
| Sample Revised Occupations (25 родов занятий) | 13–14 | `coc:rule:kc-sample-revised-occupations` (таблица); абзацы и источник в 25 записях `coc:occupation:*` — предложения |
| Creating a New Occupation | 14 | `coc:rule:kc-creating-a-new-occupation` |
| Customizing an Occupation | 15 | `coc:rule:kc-creating-a-new-occupation` (текст, пример) |
| Skills | 15 | `coc:rule:kc-skills` |
| Updated Skill List; Key | 15, 17 | `coc:rule:kc-skills` (таблица из 84 строк) |
| New & Altered Skills (врезка) | 17 | `coc:rule:kc-skills` (текст); абзацы в записях навыков — предложения |
| Skills & Specializations | 18 | `coc:rule:kc-skills-and-specializations` |
| Option: Purchasing Specializations | 18–19 | `coc:rule:kc-option-purchasing-specializations` |
| Option: Fighting Specialization Minimums | 19 | `coc:rule:kc-option-specialization-minimums` |
| Option: Firearms Specialization Minimums | 19 | `coc:rule:kc-option-specialization-minimums` |
| NPCs & Occult Skill (врезка) | 19 | `coc:rule:kc-npcs-and-occult-skill`; предложение для `coc:skill:occult` |
| Revised: Persuade Skill | 19 | `coc:rule:kc-revised-persuade-skill`; предложения для `coc:skill:persuade`, `charm`, `fast-talk`, `intimidate` |
| Persuade & Difficulty Levels; Resolving a Persuade Roll; Set the Difficulty Level | 19–20 | `coc:rule:kc-revised-persuade-skill` (текст, шаги) |
| Award Bonus & Penalty Dice; Investigator Reputation; Supporting Factors | 20 | `coc:rule:kc-revised-persuade-skill` |
| Sensing Deception; Pushing Examples; Sample Consequences of Failing a Pushed Roll; Example (Хейли) | 20–21 | `coc:rule:kc-revised-persuade-skill` (текст, пример) |
| NPCs & Persuade | 22 | `coc:rule:kc-revised-persuade-skill` (текст) |
| Option: Social Bias (врезка) | 22 | `coc:rule:kc-option-social-bias` |
| New Skill: Reassure (one-fifth APP) | 22 | `coc:skill:kc-reassure` |
| New Skill: Religion (10%) | 22–23 | `coc:skill:kc-religion` |
| Revised: Language (Own) | 23 | `coc:rule:kc-revised-language-own`; предложение для `coc:skill:language-own` |
| Option: Skills Derived from Characteristics | 23–24 | `coc:rule:kc-option-skills-derived-from-characteristics` (таблица из 84 строк) |
| Backstory Revised | 25 | `coc:rule:kc-backstory-revised` |
| Fears (врезка) | 25 | `coc:rule:kc-backstory-revised` (текст) |
| Backstory Suggestions; Description | 25 | `coc:rule:kc-backstory-suggestions` |
| Personality (пояснение и пример) | 26 | `coc:rule:kc-backstory-suggestions` |
| Personality Traits | 26 | `coc:table:kc-personality-traits` |
| Personality Flaws | 26 | `coc:table:kc-personality-flaws` |
| Significant Person & Place | 27 | `coc:table:kc-significant-person-and-place` |
| Notable Item | 27 | `coc:table:kc-notable-item` |
| Gear & Possessions; Everyday Items; Uncommon Items; Car Items | 28 | `coc:rule:kc-gear-and-possessions` (три таблицы) |
| Creating Investigator Organizations; Why Create an Organization? (1–3) | 29 | `coc:rule:kc-creating-investigator-organizations` |
| Creating an Investigator Organization; Scale; Small / Medium / Large Organization | 29–31 | `coc:rule:kc-creating-an-investigator-organization` |
| Age; New; Established; Ancient | 31 | `coc:rule:kc-creating-an-investigator-organization` |
| Funding; Limited; Wealthy; Rich | 31–32 | `coc:rule:kc-creating-an-investigator-organization` |
| Public Face (врезка) | 31 | `coc:rule:kc-creating-an-investigator-organization` (текст) |
| Creating the Outline (1–10) | 32–34 | `coc:table:kc-organization-outlines` |
| Mythos Paradigm (1. Aliens … 10. Traditional Horrors) | 34–36 | `coc:table:kc-mythos-paradigms` |
| Paradigm Shift (врезка) | 37 | `coc:table:kc-mythos-paradigms` (notes) |
| Signs & Portents | 37 | `coc:table:kc-signs-and-portents` (описание) |
| Table 2: Signs & Portents | 38 | `coc:table:kc-signs-and-portents` |
| Organization Resources; Base; Contacts | 38 | `coc:rule:kc-organization-resources` |
| Equipment; Tomes & Artifacts | 39 | `coc:rule:kc-organization-resources` |
| Involving the Organization; 1: Someone Seeks Help … 9: Sometimes, It Doesn’t Fit | 39–40 | `coc:rule:kc-involving-the-organization` |
| Organization Worksheet | 40–41 | `coc:rule:kc-organization-worksheet` (графы листа — таблица) |

## Не взято

- Иллюстрации на всю страницу: с. 8, 16, 42 — арт без текста.
- Подписи к иллюстрациям: «Opposite: Siren Songs» (с. 5), «Opposite: Making a Monster» (с. 9), «"Good evening ..."» (с. 11),
  «Hot On Your Heels» (с. 12), «Up and Away» (с. 15), «Opposite: A Deep Dive» (с. 17), «Don't Look Down!» (с. 18),
  «Dealing with Obstinacy» (с. 21), «Too Much View» (с. 24), «Packing Important Items» (с. 28), «Midnight Research» (с. 30),
  «A Good Chat» (с. 37), «Arrival» (с. 33) — названия картинок, не правила.
- Бланк «Organization Worksheet» (с. 41) как картинка — пустая форма; её графы перенесены таблицей в `coc:rule:kc-organization-worksheet`.

## Опечатки книги (errata)

- `kc-sample-revised-occupations`: у лётчика (Pilot) сумма пунктов сверх базовых значений — 340, у частного сыщика
  (Private Investigator) — 290, а правило «Creating a New Occupation» (с. 14) и остальные 23 примера дают ровно 300
  (проверено по базовым значениям «Updated Skill List»); значения оставлены как напечатаны.
- Там же: «For more information on skills, see Chapter 2: Game System» — навыки описаны в главе 1 (с. 15).
- Описка без последствий, в переводе исчезла (Р-39): у «Ancient» — «In scale, established means…».

## Технический долг и вопросы

- Ссылки на правила других частей этой книги пока текстом (записей ещё нет, id неизвестны): Reputation (с. 55, часть system) —
  в `kc-revised-persuade-skill`; Training & Downtime (с. 50) — в `kc-creating-an-investigator-organization`;
  One-shot vs. Campaign Mode (с. 47) — в `kc-involving-the-organization`; Shock (с. 87), Changed (с. 90), проверка на
  реальность гл. 3, Table 5: Sample Phobias, Pre-Game chat (с. 104) — в `coc:skill:kc-reassure` и `kc-backstory-revised`.
  Когда записи появятся, ведущему стоит добавить `refs`. Названия уровней репутации (Distinguished, Celebrated,
  Respectable, Shameful, Notorious) в `kc-revised-persuade-skill` — рабочий перевод с английским рядом; согласовать с частью system.
- IT Worker [modern era only] (с. 13) сведён с записью `coc:occupation:programmist-spetsialist-po-kompyuternoy-tekhnike`
  (те же навыки плюс Юриспруденция; предложен псевдоним «IT Worker»), отдельной записи `coc:occupation:kc-it-worker` нет —
  вопрос владельцу.
- Pilot Aircraft / Pilot Boat — в «Компаньоне» два отдельных навыка; новых записей не заведено, это абзац в `coc:skill:pilot`.
- В справочнике у специализации Науки «Математика» базовое значение 10%, в «Компаньоне» — 01% (абзац в `coc:skill:science`).
- Кандидаты в новые записи: необязательное правило «Specializations: Transferable Skill Benefit» («Книга хранителя», англ.
  изд., с. 78; в `coc:rule:skill-specializations` отмечено как не записанное); пакет «Mythos Experience Package»
  («Книга сыщика», англ. изд., с. 62); места Аркхэм, Бостон, Провиденс, Данвич, Р’льех, Ленг, Каркоза; организация
  Federated Oil and Chemical (A Time to Harvest).
