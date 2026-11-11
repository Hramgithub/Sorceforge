# «Компаньон хранителя» — часть system (с. 43–84)

Глава 2 «Game System»: раздел 1 «Core Rules», раздел 2 «Combat», раздел 3 «Chases». Русский текст — наш перевод
(`translated`, Р-21), `axes.ruleset: core`, эпоха `any` (Р-212). Записей: 47 правил `coc:rule:kc-*` и 2 таблицы с броском
`coc:table:kc-*`. Пересмотр правила «Книги хранителя» — первая ссылка `refs` и «Пересмотр правила …» в `summary` (Р-185);
вложенность — `parent` по заголовкам книги (Р-187). Правок общих записей нет: `proposals-system.json` пуст (отмена навыка
Стрельба (пистолет-пулемёт) — в предложениях части investigators, с. 17). `python -B tools/check.py <49 файлов>` — 0 ошибок,
0 предупреждений.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 2: Game System (вступление) | 43 | `coc:rule:kc-game-system` |
| Section 1: Core Rules | 43 | `coc:rule:kc-game-system` (заголовок раздела без своего текста) |
| When to Roll Dice; Have a Goal | 43 | `coc:rule:kc-when-to-roll-dice` |
| When to Call for a Roll | 44 | `coc:rule:kc-when-to-roll-dice` |
| Success & Failure | 44 | `coc:rule:kc-when-to-roll-dice` |
| Building on Failed Rolls; Example (Хейли и окно) | 44 | `coc:rule:kc-when-to-roll-dice` (текст, пример) |
| Learning from Experience | 44–45 | `coc:rule:kc-when-to-roll-dice` |
| Individual & Group Rolls | 45 | `coc:rule:kc-individual-and-group-rolls` |
| Group Rolls; Examples (библиотека, балка) | 45–46 | `coc:rule:kc-individual-and-group-rolls` (текст, примеры) |
| Group Roll Disadvantage | 46 | `coc:rule:kc-individual-and-group-rolls` |
| Leads: Obvious & Obscure Clues; врезка Leads | 46 | `coc:rule:kc-leads-obvious-and-obscure-clues` |
| Obvious Clues; Missing Obvious Clues; Drop Hints & Prompts | 46–47 | `coc:rule:kc-leads-obvious-and-obscure-clues` |
| Move the Clue; Rework the Clue | 47 | `coc:rule:kc-leads-obvious-and-obscure-clues` |
| Obscure Clues | 47 | `coc:rule:kc-leads-obvious-and-obscure-clues` |
| One-Shot vs. Campaign Mode; The Two Styles Have Differences | 47–48 | `coc:rule:kc-one-shot-vs-campaign-mode` |
| Lethality; Increase or Decrease; Total Party Kill | 48–49 | `coc:rule:kc-lethality` |
| Investigator Development | 49 | `coc:rule:kc-investigator-development` |
| Downtime; Recovery & Downtime; Sanity Recovery—Summary | 49–50 | `coc:rule:kc-downtime` |
| Training & Downtime; Training Skills; Improvement Roll; Training Characteristics | 50 | `coc:rule:kc-downtime` |
| Investigator Development & Downtime | 51 | `coc:rule:kc-downtime` |
| Reading Tomes | 51 | `coc:rule:kc-reading-tomes` |
| New Options | 51 | `coc:rule:kc-new-options` |
| Option: Take Five | 51 | `coc:rule:kc-option-take-five` |
| Option: Add Backstory Element During Play; примеры (дом с привидениями, человек, место, предмет) | 51–52 | `coc:rule:kc-option-add-backstory-element-during-play` |
| Making a Backstory Addition in Play | 52 | `coc:rule:kc-option-add-backstory-element-during-play` |
| Option: Temperature Effects; Effects of Cold; Effects of Heat | 52 | `coc:rule:kc-option-temperature-effects` |
| Cold & Heat Damage Effects; Cold Damage Recovery | 53, 55 | `coc:rule:kc-option-temperature-effects` |
| Cold Weather Clothing (врезка: Gaslight to Twenties, Modern Era) | 53 | `coc:rule:kc-option-temperature-effects` |
| Frostbite; Hypothermia; Heat Stroke (врезки) | 54 | `coc:rule:kc-option-temperature-effects` |
| Heat Damage Recovery | 55 | `coc:rule:kc-option-temperature-effects` |
| Option: Reputation | 55 | `coc:rule:kc-option-reputation` |
| Three Aspects to a Reputation; Area; Niche Reputations | 56 | `coc:rule:kc-option-reputation` |
| Table 3: Reputations | 56 | `coc:rule:kc-option-reputation` (`tables`, без броска) |
| Status & Description; Starting Reputations | 57 | `coc:rule:kc-option-reputation` |
| Reputations in Play: Modifiers; Reputations in Play: Status Check | 57 | `coc:rule:kc-option-reputation` |
| Gaining New Reputations; Recognition; Example (Майкл); Contacts | 58 | `coc:rule:kc-option-reputation` (текст, пример) |
| Section 2: Combat (вступление) | 59 | `coc:rule:kc-combat` |
| Rounds & Terminology (врезка) | 59 | `coc:rule:kc-combat` |
| Round-Table Initiative; Who Goes First?; Who Goes Next? | 59 | `coc:rule:kc-round-table-initiative` |
| Round-Table Online; Handling NPCs | 60 | `coc:rule:kc-round-table-initiative` |
| Order of Play: Combat Initiated by NPC (Diagram A) | 60 | `coc:rule:kc-round-table-initiative` (пример: подпись и порядок ходов) |
| Order of Play: Combat Initiated by an Investigator (Diagram B) | 61 | `coc:rule:kc-round-table-initiative` (пример: подпись и порядок ходов) |
| Movement in Combat (Revised); Actions in Combat; Example | 60–61 | `coc:rule:kc-movement-in-combat-revised` |
| Handguns in Melee Combat (три вопроса «What Are My Options?») | 61, 64 | `coc:rule:kc-handguns-in-melee-combat` |
| Using Miniatures & Maps (врезка): The Map; Character Size; Movement; Using Yards/Meters; Using Squares; Diagonal Movement | 62 | `coc:rule:kc-using-miniatures-and-maps` |
| Difficult Terrain; Switching Movement Modes; Breaking Up Movement; Moving Through an Occupied Space; Narrow Spaces; Grid Combat; Reach; Range | 63 | `coc:rule:kc-using-miniatures-and-maps` |
| Option: Shooting Back in Melee | 64 | `coc:rule:kc-option-shooting-back-in-melee` |
| Automatic Fire Revisited | 64–65 | `coc:rule:kc-automatic-fire-revisited` |
| Three-Round Burst; Full Auto; Concentrated Fire; Armor & Concentrated Fire | 65 | `coc:rule:kc-automatic-fire-revisited` |
| Range: Firearm Difficulty Level (врезка) | 65 | `coc:rule:kc-automatic-fire-revisited` |
| Firearms Flowchart | 66 | `coc:rule:kc-firearms-flowchart` |
| Example (Брайан, сосредоточенный огонь); Spray & Pray | 67 | `coc:rule:kc-automatic-fire-revisited` (пример, текст) |
| Forcing Targets to Dive for Cover (врезка) | 67 | `coc:rule:kc-automatic-fire-revisited` |
| Optional: Auto-Success When Diving for Cover | 67 | `coc:rule:kc-optional-auto-success-when-diving-for-cover` |
| Firearm Maneuvers; Cause Panic; Order at Gunpoint | 67–69 | `coc:rule:kc-firearm-maneuvers` |
| Explosions; Example (динамитная шашка); Explosions: Attack Rolls; Explosions: Missed Attacks; Example (граната) | 69 | `coc:rule:kc-explosions` |
| Fighting a Horde; Playing a Horde | 69–70 | `coc:rule:kc-fighting-a-horde` |
| Horde Maneuvers; Herd; Seize | 70, 72 | `coc:rule:kc-fighting-a-horde` |
| Example Hordes: Deep One Horde; Human Horde; Zombie Horde (врезка) | 71 | `coc:rule:kc-fighting-a-horde` (`tables` «Примеры орд», числа сверены по изображению) |
| Horde Combat; Creating a Horde | 72 | `coc:rule:kc-fighting-a-horde` |
| Wounds & Healing Revisited; Dying; Dying & First Aid; Dying & Medicine | 72, 74 | `coc:rule:kc-wounds-and-healing-revisited` |
| Damage & Healing Flowchart; Suffering Damage | 73 | `coc:rule:kc-damage-and-healing-flowchart` |
| Example (Хейли при смерти); Regular Damage Recovery; Major Wound Recovery; Modifiers | 74 | `coc:rule:kc-wounds-and-healing-revisited` |
| Option: Speedier Major Wound Recovery; Choose One; Luck Loss; Disfigurement; Distressed | 74 | `coc:rule:kc-option-speedier-major-wound-recovery` |
| Section 3: Chases (вступление); Updated Chase Rules; Is There a Chase? | 75 | `coc:rule:kc-chases` |
| Chase Terminology (врезка) | 76 | `coc:rule:kc-chases` |
| Locations | 76 | `coc:rule:kc-chase-locations` |
| Round Order; Those Not in the Chase | 76 | `coc:rule:kc-chase-round-order` |
| Actions in a Chase Round | 76 | `coc:rule:kc-actions-in-a-chase-round` |
| Starting a Chase; Starting Location; Example | 76 | `coc:rule:kc-starting-a-chase` |
| Location Challenges | 76–77 | `coc:rule:kc-location-challenges` |
| Cinematic Chase Locations (врезка) | 77 | `coc:rule:kc-chase-locations` |
| Skills & Characteristics for Location Challenges; Example: Graveyard Chase (начало) | 77 | `coc:rule:kc-location-challenges` (текст, пример) |
| Making the Skill Roll; Roll Outcomes | 77 | `coc:rule:kc-location-challenges` |
| Movement Points (MvP) | 77 | `coc:rule:kc-movement-points-mvp` |
| Zero MvP; Recovering MvP; Major Wounds & MvP | 78 | `coc:rule:kc-movement-points-mvp` |
| Example: Back to the Graveyard Chase (Round One … Round Five (What If…)) | 78–80 | `coc:rule:kc-movement-points-mvp` (пример целиком) |
| Ending the Chase | 80 | `coc:rule:kc-ending-the-chase` |
| Sample Challenges | 80 | `coc:rule:kc-sample-challenges` |
| On Foot: City Challenges (1d6) | 80–81 | `coc:table:kc-on-foot-city-challenges` |
| On Foot: Indoor Challenges (1d6) | 81 | `coc:table:kc-on-foot-indoor-challenges` |
| Optional Chase Rules | 81 | `coc:rule:kc-optional-chase-rules` |
| Summary: Running a Chase (врезка) | 81 | `coc:rule:kc-chases` (текст по пунктам, `steps`) |
| Attacks; Example | 81–82 | `coc:rule:kc-chase-attacks` |
| Create or Change a Challenge; Example | 82–83 | `coc:rule:kc-create-or-change-a-challenge` |
| Help; Example | 83 | `coc:rule:kc-chase-help` |
| Hide | 83 | `coc:rule:kc-chase-hide` |
| Monster & NPC Skills; Example | 83 | `coc:rule:kc-monster-and-npc-skills` |
| Splitting Up | 83 | `coc:rule:kc-chase-splitting-up` |
| Strong Lead; Example | 83 | `coc:rule:kc-strong-lead` |
| Switching Movement Modes | 83 | `coc:rule:kc-chase-switching-movement-modes` |

## Опечатки и сомнения (в `errata` записей)

| Запись | Что | Как в записи |
|---|---|---|
| `coc:rule:kc-using-miniatures-and-maps` | с. 62: «Build 13 to 2: occupies 9 squares» — пропущена цифра (промежуток между 12 и 28) | «от 13 до 27», `fixed: true`, `corrections` с «вывод из текста (Р-41)» |
| `coc:rule:kc-fighting-a-horde` | с. 71: у орды глубоководных «Build: 6», а по правилу «Создание орды» СИЛ + ТЕЛ = 140 + 400 = 540 → Комплекция 7 (у людской орды и орды зомби сходится) | как напечатано (6), `fixed: false` |
| `coc:rule:kc-fighting-a-horde` | с. 72 текст: одна атака при ПЗ «меньше пятой части»; с. 71 примеры: уже при пятой части (13 из 65, 12 из 60) | как напечатано в каждом месте, `fixed: false` |

Не опечатки, но отмечено в `quality.notes`: ПЗ орды зомби 72,5 → 73 (округление вверх, Р-161); стрельба в упор «одна пятая ЛВК
в футах» → 1/15 ЛВК в метрах, как в русской «Книге хранителя» (Р-64); на с. 51–52 ссылки «Significant Person & Place (page 93)» и
«Notable Item (page 93)» ведут в главу «Рассудок», где на с. 93 — примеры этих граф; сами графы — с. 25–27 (обе записи в `refs`).
Обновлённые правила погони не упоминают проверку скорости и действия перемещения по разнице Скоростей — это отмечено как вывод
из текста.

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Подписи иллюстраций: «Opposite: Escaping the Heat», «A Desperate Act», «Fetching a Clue», «Lost in the Desert», «Fighting the Cold», «Now Hide!», «Trouble at the Bar», «Take Cover!», «Get off my land!», «Oh, Rats!», «Never Mind the Scenery!», «Get Back Here!», «Hide and Seek» | 43–83 | подписи к рисункам, без механики |
| Иллюстрация на всю страницу (газетный киоск, паук на доме) | 84 | рисунок без текста |
| Рисунки схем А и Б (портреты вокруг стола) | 60–61 | картинки; их подписи и порядок ходов — в примерах `kc-round-table-initiative` |
| Изображения страниц «Firearms Flowchart» и «Damage & Healing Flowchart» | 66, 73 | текст схем перенесён в записи; картинки не добавлены (`app/art/` вне этой части) |
| Колонтитулы «CHAPTER 2», «GAME SYSTEM», номера страниц | все | оформление |

## Кандидаты в новые записи (вопрос владельцу)

- Орды как существа: «Орда глубоководных», «Людская орда», «Орда зомби» (с. 71) — сейчас статблоки таблицей в
  `coc:rule:kc-fighting-a-horde`; при желании — записи `creature` со связью к `coc:creature:deep-one` / `coc:creature:zombie`
  (не `instance_of`: числа другие, это группа).
- Картинки схем стрельбы и урона (с. 66, 73) в `images` записей `kc-firearms-flowchart` и `kc-damage-and-healing-flowchart`.
