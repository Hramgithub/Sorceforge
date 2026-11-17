# «Mohole» (petersens-abominations-en, с. 107–148) — сверка заголовков, часть mohole (Р-134, Р-251)

Книга: «Petersen’s Abominations» (Sandy Petersen, Mike Mason; Chaosium, 2018), глава 4 «Mohole». Печатная страница =
физическая − 1 (проверено по изображениям с. 109, 111, 121, 122: номер на странице на единицу меньше физического;
`offset: -1` в `pipeline/source/books.json` верен). Отдельные PDF: готовые сыщики «Mohole» —
`petersens-abominations-pregens-en`, с. 20–25 (печатная = физической); раздатка и карты
(`petersens-abominations-handouts-en`, 9 страниц) — материалов «Mohole» нет (только Hotel, Derelict, Panacea, Voice),
в разделе Player Handouts книги (с. 186–193) их тоже нет.

Русский перевод: в базе есть только готовые сыщики «Мохола» из официального русского издания прегенов
(«Кошмары цифровой эпохи», `digital-nightmares-pregens-ru`, с. 23–29, записи `digital-nightmares-ru/character/*`).
Текста сценария на русском в базе и в библиотеке нет (в папке «Цифровая эпоха» — только прегены и материалы игроков).
Поэтому сценарий — наш перевод (`translated`); готовые сыщики не дублируются: по Р-147 к ним — предложения
(английские источники, `name.en`, `occupation.en`, сверка чисел — совпадают). Официальные формы из русских прегенов:
«Мохол» (глава 4), проект «Нергал», «ролотный газ» / «ролот», платформа «Дыра дьявола», Саймон Ройлотт, Пирс Голдман,
Джеральд Уайнстеп, «министр по вопросам бизнеса, энергетики и промышленной стратегии», «проверяющие».

Записи — `kb/books/petersens-abominations-en/` (95): сценарий 1, сцены 19, персонажи 24 (17 человек и 7 групповых
профилей), существа 2, места 34, карты 2, предметы 8, организации 4, раздатка 1. Пути ниже — id без префикса
`petersens-abominations-en/`. Картинки — 10 (`art-mohole.json`, применены к своим записям); атмосфера —
`atmosphere-mohole.json` (7); предложения к чужим и общим записям — `proposals-mohole.json` (33; пробный прогон
`apply.py --dry-run` — всё ложится). Карты — `app/maps/abom-mohole-devils-hole-rig.jpg`,
`app/maps/abom-mohole-accommodation-block-plan.jpg`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 4: Mohole (титул, подзаголовок, вступление) | с. 107 | `scenario/mohole` (summary, sources) |
| Foreword (Sandy Petersen, 2017; эпиграф — Екклесиаст 1:9) | с. 107 | `scenario/mohole` (keeper_info, «Предисловие автора») |
| Background | с. 108 | `scenario/mohole` (keeper_info), `character/piers-goldman`, `character/gerald-winestep`, `character/simon-roylott`, `organization/fortudo`, `character/david-stahl` |
| Project Nergal | с. 108 | `organization/mohole-project-nergal`, `scenario/mohole` (keeper_info) |
| Deep Down | с. 108 | `scenario/mohole` (keeper_info), `item/mohole-green-slime`, `creature/primordial`, `creature/formless-spawn-mohole` |
| The Investigators | с. 108–109 | `scenario/mohole` (hook), `scene/mohole-arrival`, `organization/mohole-infrastructure-and-projects-authority`; готовые сыщики — `digital-nightmares-ru/character/*` |
| Project Nergal and the Mohorovicic Discontinuity (карта) | с. 109 | картинка `location/devils-hole` (карта без номеров — Р-249) |
| North Sea Energy (врезка) | с. 109 | `scenario/mohole` (keeper_info), `location/devils-hole`, `organization/mohole-beis` |
| Project Mohole; The Moho; The Earth’s Mantle (врезка) | с. 110 | `scenario/mohole` (keeper_info, «Проект „Мохол“») |
| Dramatis Personae | с. 110 | `scenario/mohole` (keeper_info), `handout/mohole-organisational-chart` |
| Devil’s Hole Organisational Chart | с. 111 | `handout/mohole-organisational-chart` (текст подписей + перевод, картинка) |
| Gerald Winestep, 54, Secretary of State | с. 112 | `character/gerald-winestep`, `scene/mohole-winestep-call` |
| Platform Crew | с. 112 | `organization/mohole-project-nergal` (members) |
| Piers Goldman, 48, Company Man | с. 112 | `character/piers-goldman` (+ портрет) |
| Dr. Simon Roylott, 53, Project Lead (и Keeper note) | с. 112–113 | `character/simon-roylott` (+ портрет), `item/mohole-roylott-computer` |
| Jerry Scrivens, 49, Offshore Operations Engineer (OOE) | с. 113–114 | `character/jerry-scrivens` (+ портрет) |
| Dr. Rachel Kent, 49, Nuclear Operations Engineer (NOE) | с. 114 | `character/rachel-kent` (+ портрет), `item/mohole-kent-notes` |
| Angie Yousef, 53, Operations Team Leader (OTL) | с. 114 | `character/angie-yousef` (+ портрет) |
| Michel “Mich” Tennyson, 42, Operations Coordinator | с. 115 | `character/michel-tennyson` |
| Other Platform Crew | с. 115 | групповые профили ниже |
| Finbar Drummond, Jeff Smalls, Lucille Sharkey, Fiona McCraig — Control Room and Power Control Systems Operators | с. 115 | `character/control-room-operators` |
| Gabe Macready, 31, radio operator | с. 115 | `character/gabe-macready` |
| Lewis Duffy, Bill Greer, Mitch Logan, Steve Cressey — Processing Technicians | с. 115–116 | `character/processing-technicians` |
| Denise Latch, Cerys Jones, Mea MacDougal — Reactor Control | с. 116 | `character/reactor-and-coolant-technicians`, `item/mohole-reactor-logs` |
| Vijay Reza, Tom Martin — Coolant Technicians | с. 116 | `character/reactor-and-coolant-technicians` |
| Harry Dawson, 35, automation systems specialist | с. 116 | `character/harry-dawson` |
| Harry Slocum, 43, and Billy Waters, 24, Maintenance Crew | с. 116–117 | `character/harry-slocum`, `character/billy-waters` |
| Tony Pearson, 36, paramedic | с. 117 | `character/tony-pearson` |
| Tegan Fielding, 36, stores keeper | с. 117 | `character/tegan-fielding` |
| Richard Copper, 42, crane operator | с. 117 | `character/richard-copper` |
| Boris “the bird” Cooke, 38, helicopter pilot | с. 117 | `character/boris-cooke` |
| Patrick Murphy, Seamus O’Clare — Catering Crew | с. 117 | `character/catering-crew` |
| Drill Crew | с. 117 | `character/drill-crew` |
| Security Team | с. 118 | `character/stahls-men`, `organization/fortudo` |
| David Stahl, 38, Head of Security | с. 118 | `character/david-stahl` (+ портрет) |
| Stahl’s Guns and Cell Phone Jammer (врезка, таблица оружия) | с. 118 | `location/mohole-stahl-office` (таблица «Оружие из шкафа Шталя»), `item/mohole-stahl-gun-cabinet`, `item/mohole-cell-phone-jammer`; предложение к `coc:weapon:glock-17` (source_variants) |
| Stahl’s Men | с. 119 | `character/stahls-men`, `character/nigel-gordon` |
| Devil’s Hole Rig | с. 119 | `location/devils-hole-platform` |
| Locations on the Rig | с. 119 | `location/devils-hole-platform`, `map/mohole-devils-hole-rig` |
| Accommodation Block | с. 119 | `location/mohole-accommodation-block` |
| Sickbay (Level 1) | с. 119 | `location/mohole-sickbay` |
| Offices (Level 2) | с. 120 | `location/mohole-offices` и шесть кабинетов (`mohole-goldman-office`, `mohole-roylott-office`, `mohole-kent-office`, `mohole-yousef-office`, `mohole-stahl-office`, `mohole-investigators-office`) |
| Kitchen and Restaurant (Level 3) | с. 120 | `location/mohole-kitchen-and-restaurant` |
| Stores and Shop (Level 3) | с. 120 | `location/mohole-stores-and-shop` |
| Gym (Level 3) | с. 120 | `location/mohole-gym` |
| Living Quarters (Levels 4–6) | с. 120 | `location/mohole-living-quarters` |
| Control Room | с. 120 | `location/mohole-control-room` |
| Power Control Systems | с. 120 | `location/mohole-power-control-systems` |
| Generators and Diesel Engines | с. 120 | `location/mohole-generators-and-diesel-engines` |
| Devil’s Hole Rig — Exploded View (план, 24 подписи) | с. 121 | `map/mohole-devils-hole-rig` (метки на всех подписях; без раздела в тексте — небольшие записи `mohole-upper-decks`, `mohole-lower-decks`, `mohole-derrick`, `mohole-crane`, `mohole-gas-tower`, `mohole-gas-flare`, `mohole-helipad`, `mohole-desalination-units`, `mohole-engineering`, `mohole-docking-facility`) |
| Devil’s Hole Accommodation Block Plan (этажи 1–6, ключи) | с. 122 | `map/mohole-accommodation-block-plan` (23 метки); записка Голдмана и объявление — `location/mohole-accommodation-block` |
| Processing Systems | с. 123 | `location/mohole-processing-systems` |
| Drilling Floor | с. 123 | `location/mohole-drilling-floor` |
| Coolant Plant | с. 123 | `location/mohole-coolant-plant` |
| Nuclear Reactor | с. 123 | `location/mohole-nuclear-reactor` |
| Reactor Control Systems | с. 123 | `location/mohole-reactor-control-systems` |
| Lifeboats and ROV | с. 123 | `location/mohole-lifeboats-and-rov` |
| Helicopter | с. 123 | `item/mohole-helicopter`, `character/boris-cooke` |
| Starting the Scenario | с. 124 | `scene/mohole-arrival` |
| Running the Scenario; Part One; Part Two; Park Three [sic] | с. 124–125 | `scenario/mohole` (advice, steps) |
| Technical Jargon (врезка) | с. 125 | `scene/mohole-tour` (список терминов), `scenario/mohole` (advice — ссылка) |
| Part One: Events | с. 125 | `scenario/mohole` (steps), сцены части 1 |
| Tour of the Platform | с. 125 | `scene/mohole-tour` |
| Interview with Piers Goldman | с. 126 | `scene/mohole-goldman-interview` |
| Interview with Dr. Roylott | с. 126–127 | `scene/mohole-roylott-interview` |
| Brain Wipe (врезка) | с. 127 | `character/simon-roylott` (abilities), `scene/mohole-roylotts-madness` |
| Dr. Roylott’s Madness | с. 127 | `scene/mohole-roylotts-madness` |
| Interviews with Other Personnel | с. 127–128 | `scene/mohole-other-interviews` |
| Malfunctions | с. 128 | `scene/mohole-malfunctions` |
| Part Two: Events | с. 128 | `scenario/mohole` (steps) |
| Where’s Harry Slocum? | с. 128 | `scene/mohole-wheres-harry-slocum` |
| A Medical Emergency | с. 128–129 | `scene/mohole-medical-emergency` |
| Macready’s Sabotage | с. 129, 132–133 | `scene/mohole-macreadys-sabotage` |
| The Green Slime (врезка) | с. 131 | `item/mohole-green-slime` (механика, анализ списком «•») |
| Hot, Hot, Hot! (врезка) | с. 132 | `scenario/mohole` (таблица «Температура тела», advice — гипертермия) |
| Tsathoggua’s Influence (врезка) | с. 132 | `scene/mohole-tsathogguas-influence` |
| The Primordials (врезка) | с. 133 | `creature/primordial` (abilities, legend), `item/mohole-co2-extinguishers` |
| Drilling for Slime | с. 133 | `scene/mohole-drilling-for-slime` |
| Part Three: Events | с. 134 | `scenario/mohole` (steps) |
| The Primordials Attack | с. 134 | `scene/mohole-primordials-attack` |
| Dr. Kent’s Assistance | с. 134 | `scene/mohole-dr-kents-assistance` |
| The Madness of Stahl; The Firing Squad | с. 134 | `scene/mohole-madness-of-stahl` |
| Lava Danger | с. 136 | `scene/mohole-lava-danger` |
| Elastic Horror | с. 136 | `scene/mohole-elastic-horror` (+ картинка «The Formless Spawn» у `creature/formless-spawn-mohole`) |
| Ending the Scenario; Escape; Stopping the drill | с. 136–137 | `scene/mohole-ending` |
| Conclusion; Rewards | с. 137 | `scenario/mohole` (conclusion), `scene/mohole-ending` (outcome) |
| Appendix: Mohole — Non-Player Characters and Monsters | с. 137 | статблоки записей ниже |
| Dr. Simon Roylott, project lead (статблок) | с. 137 | `character/simon-roylott` |
| Angie Yousef; Dr. Rachel Kent; Piers Goldman; Michel “Mich” Tennyson; Jerry Scrivens; Tony Pearson; Tegan Fielding (статблоки) | с. 138–139 | записи персонажей |
| Control Room/Power Control Systems Operators, and Radio Operator | с. 139 | `character/control-room-operators` |
| Processing Technicians | с. 139 | `character/processing-technicians` |
| Reactor Control and Coolant Technicians | с. 139 | `character/reactor-and-coolant-technicians` |
| Automation Systems Specialist, Maintenance Workers, and Crane Operator | с. 139 | `character/maintenance-crew` |
| Catering Crew | с. 139–140 | `character/catering-crew` |
| Drill Crew | с. 140 | `character/drill-crew` |
| Security Team: David Stahl; Stahl’s Men | с. 140 | `character/david-stahl`, `character/stahls-men` |
| Primordial (иллюстрация) | с. 140 | картинка `creature/primordial` |
| Monsters: Primordials, shambling jelly monsters | с. 141 | `creature/primordial` |
| Formless Spawn | с. 141 | `creature/formless-spawn-mohole` (instance_of `coc:creature:formless-spawn`) |
| Jessica Anderson | с. 142 | `digital-nightmares-ru/character/jessica-anderson` (предложения: name.en, источники) |
| Phillip Swann | с. 143 | `digital-nightmares-ru/character/philip-swann` (предложения) |
| Terry Douglas | с. 144 | `digital-nightmares-ru/character/terry-douglas` (предложения) |
| Trisha Hickey | с. 145 | `digital-nightmares-ru/character/trisha-hickey` (предложения) |
| Victor Mann | с. 146 | `digital-nightmares-ru/character/victor-mann` (предложения) |
| Clarice Williams | с. 147 | `digital-nightmares-ru/character/clarice-williams` (предложения) |
| Полностраничная иллюстрация (головы в банках) | с. 148 | не «Мохол» — относится к «Voice over the Phone»; в `atmosphere-mohole.json` с пометкой для части voice |

## Не взято

- Атмосферные иллюстрации (Р-241): титул главы «Tsathoggua and The Rig» (с. 107), «Devil’s Hole Rig» (с. 126),
  «The Medical Emergency» (с. 129), «Drilling for Slime» (с. 130), «The Primordials Attack» (с. 135) — в
  `atmosphere-mohole.json`.
- Портреты готовых сыщиков на с. 142–147: у записей `digital-nightmares-ru` уже есть портреты из русского издания
  (одна картинка на запись).
- Отдельные записи для членов групп без своей роли в сюжете (Драммонд, Смоллс, Шарки, Маккрейг; Даффи, Грир, Логан,
  Кресси; Лэтч, Джонс, Макдугал, Реза, Мартин; Мёрфи, О’Клэр; 11 буровиков; 9 охранников кроме Гордона): описаны в
  групповых профилях, имена — в `aliases` профиля. Алистер Эдвардс (только подпись на схеме) — в тексте раздатки и
  организации.
- Навыки первородного «Shamble» и «Relentless Pursuit» — без записи справочника (нет механики, Р-126).
- Винтовка HK416 — записи в `kb/weapons/` нет; у атак Шталя и его людей нет ссылки `weapon` (кандидат в общую запись:
  2d8, 80 ярдов, 1 (2) или авто, магазин 30, осечка 99, с. 118).

## Опечатки и сомнения книги

- Ройлотт: ПМ 9 при МОЩ 35 (ожидалось 7; оставлено — иначе нельзя стереть 36 часов за 10 ПМ); Убеждение 55% в статблоке
  (с. 137) и 70% в тексте (с. 127).
- Скривенс: «Brawl 60% (30/13)» → 30/12 (исправлено, Р-35); ПМ 9 при МОЩ 60 (ожидалось 12).
- Шталь: ПЗ 15 при (60 + 80) / 10 = 14. Группа диспетчерской: ПЗ 13 при 11. Техники переработки: Скорость 7 при 8.
  Тиган Филдинг: ПЗ 12 (11,5 округлено вверх — приём книги).
- Пирсон и ремонтники: драка «1D3» без БкУ при БкУ +1d4.
- Первородный: броня напечатана дважды («bullets… minimum damage…» и «Armor: none»); «The Primordials Attack» отсылает
  к профилям «on page 133» (на деле с. 141).
- «Refer to Goldman’s write up… (page 110)» — описание на с. 112.
- Жилой блок: «divided over five levels» (с. 119), а уровни 4–6 и план — шесть этажей.
- «Technical Jargon»: «32,000 kg per square cm (2,250 psi)» и «14,000 kg per square cm (1,000 psi)» — неверный перевод
  единиц (≈ 158 и 70 кг/см²).
- «Project Mohole»: «12,301 feet (3,783 meters)» — 12 301 фут ≈ 3 749 м.
- Организационная схема (с. 111) расходится с текстом: «Nigel Gorden», «Gay Hunt», «Yan Anderson», «Fiona MacCraig»,
  «Mich Logan», «Production Technicians»; Голдман — «Project Manager»; на плане — «Dr. Pearson’s Office» (Пирсон —
  парамедик).
- Голдман называет Скривенса «Jerry Scriven» (с. 126); подзаголовок «Park Three» (с. 125); подпись «Accomodation»
  (с. 122) — словесные, в записях не отмечены (Р-39), кроме псевдонима.
- Готовые сыщики (в оригинале; русское издание верно): Андерсон «Brawl 25% (12/15)», «Credit Rating 44% (22/9)»;
  Суонн «Brawl 25% (12/15)», «Charm 45 (22/9)»; Дуглас «Brawl 25% (12/15)», «Library Use 30% (16/6)» — в предложениях
  (quality.notes).
- Глок 17 в таблице Шталя: осечка 99 (в справочнике 98) — предложение source_variants (Р-124).

## Термины (английский → русский)

| English | Русский |
|---|---|
| Mohole | Мохол (офиц., русские прегены) |
| Devil’s Hole Platform / Rig | платформа «Дыра дьявола» (офиц.) |
| Devil’s Hole (trenches) | Дыра дьявола (впадины Северного моря) |
| Project Nergal | проект «Нергал» (офиц.) |
| Rolot gas / Rolot | ролотный газ / ролот (офиц.) |
| external auditors / audit | проверяющие / проверка, инспекция (офиц. «проверяющие») |
| Secretary of State for Business, Energy, and Industrial Strategy | министр по вопросам бизнеса, энергетики и промышленной стратегии (офиц.) |
| Department for Business, Energy, and Industrial Strategy (BEIS) | Министерство бизнеса, энергетики и промышленной стратегии |
| Infrastructure and Projects Authority | Управление инфраструктуры и проектов |
| Fortudo | «Фортудо» |
| Company Man / Executive Manager / Project Manager | представитель заказчика / исполнительный директор (офиц.) / менеджер проекта |
| Project Lead | руководитель проекта |
| Offshore Operations Engineer (OOE) | инженер морских операций |
| Nuclear Operations Engineer (NOE) | инженер ядерной установки |
| Operations Team Leader (OTL) | руководитель операционной группы |
| Operations Coordinator | координатор операций |
| Head of Security / Section Leaders | начальник охраны / старшие смены |
| Control Room / Radio Room | диспетчерская / радиорубка |
| Power Control Systems | система управления энергоснабжением |
| Processing Systems / Processing Technicians | система переработки газа / техники переработки |
| Reactor Control Systems (Room) / Reactor Control team | пульт управления реактором / группа управления реактором |
| Coolant Plant / Coolant Technicians | установка охлаждения / техники системы охлаждения |
| Drilling Floor / Drill Crew | буровая площадка / буровая бригада |
| Driller / Mud engineer / Derrickhands / Roughnecks | бурильщик / инженер по буровым растворам / верховые / помбуры |
| Accommodation Block / Living Quarters | жилой блок / жилые этажи |
| Sickbay | медпункт |
| Stores keeper | кладовщица |
| Lifeboats (free-fall) / ROV | спасательные капсулы (свободного падения) / телеуправляемый подводный аппарат (ТНПА) |
| tension-leg platform (TLP) | платформа на натяжных опорах |
| Derrick / Gas Tower / Gas Flare / Helipad / Docking Facility / Desalination Units / Engineering | буровая вышка / газовая башня / газовый факел / вертолётная площадка / причал / опреснители / мастерские |
| Upper Decks / Lower Decks | верхние палубы / нижние палубы |
| green slime | зелёная слизь |
| primordials | первородные (ед. «первородный») |
| shambling jelly monsters | ковыляющие студенистые чудовища |
| formless spawn (of Tsathoggua) | бесформенное отродье (глоссарий) |
| Brain Wipe | стирание памяти |
| Greater Mind | Высший разум |
| Tsathoggua / N’Kai / the Sleeper / Zhothaqqua / Sadagowah | Цатхоггуа / Н’кай / Спящий / Жотаккуа / Садагова |
| Mohorovičić discontinuity / the Moho | граница Мохоровичича / Мохо |
| martial law | военное положение |
| firing squad | расстрел (расстрельная команда) |
| cell phone jammer | глушилка сотовой связи |
| Shamble / Relentless Pursuit (навыки) | ковылять / неотступная погоня |
| Technical Jargon: steam turbine, coolant system, wellhead, blowout preventer, production separator, gas compressors, gas export metering system | паровая турбина, система охлаждения, устье скважины, противовыбросовый превентор, сепаратор, газовые компрессоры, система учёта экспорта газа |
