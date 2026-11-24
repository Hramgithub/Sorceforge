# Convicts & Cthulhu — Ticket of Leave #8–#10 (часть tol-c)

Перенос трёх выпусков Cthulhu Reborn для «Convicts & Cthulhu» (7-я редакция; метка библиотеки «[EN 6e]» неверна —
статблоки по 7-й редакции). Русского перевода нет: весь русский текст — наш перевод (флаг `translated`, Р-251, Р-21).
Эпоха `other`, свод `core`.

| Книга | Выпуск | Стр. PDF | Смещение | Записей |
|---|---|---|---|---|
| `convicts-tol-08-en` | #8 «Gentlemen Convicts» (2017) | 20 | 0 (печатная = физическая) | 64 |
| `convicts-tol-09-en` | #9 «Orphan School Horror» (2017) | 23 | 0 | 59 |
| `convicts-tol-10-en` | #10 «The Doom That Came To Five Dock» (2018) | 17 | 0 | 31 |

Смещение проверено по изображениям страниц (номер в пятиугольнике внизу совпадает с физической страницей; обложка — с. 1).

Черновики общих заклинаний (переносит ведущий в `kb/spells/`): `spell-summon-thing-from-the-bone-pit-tol-c.json`,
`spell-call-dismiss-zstylzhemgni-tol-c.json`, `spell-enchant-wound-tol-c.json`. До переноса ссылки на них —
единственные висячие ссылки части (15 мест).

Предложения к записям основной книги — `proposals-tol-c.json` (4 правки `convicts-cthulhu-en/character/john-harris`:
три источника и статблок из ToL #10, с. 14). Картинки для записей основной книги — `art-core-targets-tol-c.json`
(портрет Харриса, рисунок здания Школы для девочек-сирот; исходники рядом: `img-*-tol-c.png`).

## Ticket of Leave #8 — Gentlemen Convicts

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| обложка, Credits | 1 | `convicts-tol-08-en/scenario/the-gentleman-stalker` (sources); обложка — atmosphere |
| Introduction | 1 | `organization/gentlemen-convicts` |
| Gentlemen Convicts (эпиграф Select Committee 1812) | 2 | `organization/gentlemen-convicts` |
| A Note on Gender (врезка) | 2 | `organization/gentlemen-convicts` |
| The Crimes of Nobility | 2 | `organization/gentlemen-convicts` |
| The Scottish Martyrs (врезка) | 3 | `organization/scottish-martyrs` |
| Five Notable Gentlemen Convicts | 3 | `organization/gentlemen-convicts` (members) |
| Thomas Muir (1765-1799) | 3–4 | `character/thomas-muir` (портрет) |
| Thomas Fyshe Palmer (1747-1802) | 4 | `character/thomas-fyshe-palmer` |
| Maurice Margarot (1745-1815) | 4 | `character/maurice-margarot` |
| Sir Henry Browne Hayes (1762-1832) | 5 | `character/henry-browne-hayes` (газетная заметка — картинка) |
| John Grant (1776-?) | 5 | `character/john-grant` |
| Scenario Seed: The Gentleman Stalker | 6 | `scenario/the-gentleman-stalker` (summary, advice) |
| Keeper's Introduction | 6 | scenario keeper_info; `organization/enlightened-brothers` |
| Master and Disciple | 6–7 | scenario keeper_info; `character/sarum-greensleigh`, `character/francis-walton`, `item/proxy-bottles`, `item/ritual-brazier` |
| The Man in the Blue Coat | 7–8 | scenario keeper_info; `creature/man-in-the-blue-coat` |
| Drop Like A Hot Potato | 8 | scenario keeper_info; `character/sarum-greensleigh` |
| Involving the Investigators | 8–9 | `scene/greensleigh-approach` |
| The True Nature of the Threat | 9 | scenario keeper_info |
| Flow of the Adventure (Interviews, Dark Dreams) | 9–10 | `scene/dark-dreams`; scenario steps |
| The 'Man in Blue' Killings (таблица) | 10 | scenario `tables` «Убийства „Человека в синем“» |
| The Murders | 10 | `scene/the-murders` |
| Additional ‘Clues’ From Greensleigh | 10 | `scene/greensleigh-false-clues` |
| Investigating the Secret Society | 11 | `scene/woodhouse` (вступление) |
| Anthony Woodhouse (deceased) | 11 | `scene/woodhouse`, `character/anthony-woodhouse`, `location/woodhouse-house`, `item/blood-bandages` |
| Francis Walton (lunatic) | 11–12 | `scene/walton`, `location/walton-cottage`, `item/walton-cell-scrawls` |
| John McCarty (drunkard), Interviewing McCarty | 12 | `scene/mccarty`, `character/john-mccarty`, `character/mary-marsott`, `character/charles-sarris`, `character/sophia-boyle`, `location/mccarty-farm` |
| William Chaffey (terrified), Interviewing Chaffey | 12–13 | `scene/chaffey`, `character/william-chaffey`, `location/chaffey-house`, `item/chaffey-dream-sketches` |
| Crimes of the Gentlemen (врезка) | 13 | `handout/crimes-of-the-gentlemen`, `scene/government-house-records` |
| Dr Ignatius Lyle (amateur investigator), Interviewing Lyle | 13–14 | `scene/lyle`, `character/ignatius-lyle`, `location/lyle-house` |
| Thomas Hogg (paternal and assured), Interviewing Hogg, Annie’s account | 14 | `scene/hogg`, `character/thomas-hogg`, `character/annie-beddows`, `location/hogg-house` |
| Investigating Greensleigh (liar extraordinaire) | 15 | `scene/investigating-greensleigh`, `location/greensleigh-farm`, `item/promissory-note`, `item/farmhouse-sketch` |
| George Barland (link to the butcher), Interviewing Barland | 16 | `scene/barland`, `character/george-barland`, `location/barland-house` |
| Other Potential Complications | 16 | scenario advice |
| Investigating the Man in the Blue Coat | 16–17 | `scene/hunting-the-man-in-blue`, `item/greensleigh-tome` |
| Key Locations | 17 | места ниже |
| Thomas Muir’s Farm | 17 | `location/muirs-farm`; `scene/final-showdown` |
| The Bone Pit in the Rocks (George Cribb’s slaughter-yard) | 17 | `location/cribbs-bone-pit`, `character/george-cribb` |
| Mythos Options | 17 | сцены вариантов (arc.part «Варианты Мифов») |
| Option A: The Hunter From The Past | 17–18 | `scene/option-a-hunter-from-the-past`, `character/harland-drake`, `item/hogg-diary` |
| Option B: Dreams of Freedom Dying | 18 | `scene/option-b-dreams-of-freedom-dying` |
| Option C: The Bone Book of the Patriarch | 18–19 | `scene/option-c-bone-book-of-the-patriarch`, `tome/bone-book-of-the-patriarch`, `item/patriarch-warning-letter` |
| Statistics; Sarum Greensleigh | 19 | `character/sarum-greensleigh` (статблок, заклинание — черновик `coc:spell:summon-thing-from-the-bone-pit`) |
| The Man in the Blue Coat (aka The Thing from the Bone Pit); Attacks; Special Powers | 19–20 | `creature/man-in-the-blue-coat` (арт со с. 19) |
| Further Source Material, Books, Online Resources | 20 | не взято (см. ниже) |

## Ticket of Leave #9 — Orphan School Horror

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| обложка, Credits | 1 | scenario sources; обложка — atmosphere |
| Introduction | 1 | `convicts-tol-09-en/scenario/the-orphan-school-horror` advice («Вступление выпуска»); `organization/female-orphan-school-committee` |
| The Female Orphan School (эпиграф письма Кинга 1800) | 2 | `organization/female-orphan-school-committee` |
| Establishing the School | 2 | там же |
| Where was the school located? | 2 | там же; здание — `convicts-cthulhu-en/location/female-orphan-school` (based_at, map shows) |
| Captain William Kent (1760-1812) (врезка) | 3 | `character/william-kent` |
| Running the School | 3 | organization (состав комитета, members) |
| Paying for the School | 3–4 | organization |
| Who Went There? | 4 | organization |
| Daily Life at the Female Orphan School | 4 | organization |
| Working for the School | 4–5 | organization |
| Leaving the School | 5 | organization |
| What else was the Schoolhouse used for? | 5 | organization; `location/orphan-school-schoolroom` |
| Matrons and Masters (врезка) | 6 | organization (по годам) + персонажи `mary-robson`, `h-stroud`, `t-p-newsham`, `mr-marchant`, `henry-perfect`, `susannah-perfect`, `john-hoskings`, `ann-hoskings`, `mary-peat`, `mary-cosgrove`, `elizabeth-edwards`, `anne-sandilon`, `mary-gaunterry`, `thomas-mcdermott`; Хьюм — `convicts-cthulhu-en/character/elizabeth-more-hume` |
| Scenario Seed: The Orphan School Horror | 7 | scenario |
| Christmas in the Colony (врезка) | 7 | scenario advice |
| The Orphanage Ghosts | 7 | scenario keeper_info |
| Keeper's Introduction | 7–8 | scenario keeper_info; `creature/orphan-school-horror` |
| Involving the Investigators | 8 | `scene/interview-with-mrs-paterson`; scenario hook |
| Child Investigators (врезка) | 8 | scenario advice |
| The True Nature of the Threat | 9 | scenario keeper_info; сцены вариантов |
| The Interview with Mrs Paterson | 9–10 | `scene/interview-with-mrs-paterson`, `character/elizabeth-paterson`, `item/committee-letter`, `character/mary-asker`, `character/bethany-small`, `character/margaret-boyne`, `character/harriet-torrence` |
| Flow of the Adventure | 10 | scenario advice и steps |
| Early Inquiries | 10–11 | `scene/early-inquiries` |
| About the missing servant women / About the “swooning” and unresponsive girls / About the ghostly sightings | 11 | `scene/early-inquiries`, `character/elizabeth-bean`, `character/caroline-merchant` |
| Other Weirdness | 12 | `scene/other-weirdness` |
| Eerie Encounters in the Night | 12 | `scene/eerie-encounters`; способность «Призрачные проявления» у `creature/orphan-school-horror` |
| Layout of the Sydney Orphan School (карта: Main Building, Basement, Grounds) | 13 | `map/sydney-female-orphan-school` (31 метка); места `location/orphan-school-basement`, `-masters-office`, `-schoolroom`, `-dormitories`, `-grounds`; прочие комнаты — метки с text на здание основной книги |
| Questioning the Girls (missing servant women, unresponsive girls, child ghosts, adult figure ghosts, weird figures at the orphanage gate, gentleman lurker) | 14 | `scene/questioning-the-girls`, `character/lettie-crookes`, `character/jenny-cowley` |
| Wider Investigations around Sydney Cove | 14–15 | `scene/wider-investigations`, `location/government-granary`, `location/underwood-warehouse`, `character/john-biggell` |
| Red Herrings and Other Complications (врезка) | 15 | scenario advice |
| An Encounter with the Lonely Dead | 15 | `scene/encounter-with-the-lonely-dead` |
| Mythos Options | 15 | сцены вариантов |
| Option A: The Crack in Reality (Additional Clues, Eerie Phenomena, Bane & Denouement) | 16–17 | `scene/option-a-crack-in-reality`, `creature/ur-lloigor`, `character/catherine-woakes`, `character/clive-montrose`, `item/montrose-diary` |
| Option B: The Nexus of Need | 17–19 | `scene/option-b-nexus-of-need`, `item/red-bleeding-book`, `item/bethany-drawings` |
| Option C: The Guest of Captain Kent | 19–20 | `scene/option-c-guest-of-captain-kent`, `item/montrose-papers`, `item/montrose-letter`, `item/sigil-stone`, `item/leathery-shell`, `location/peregrine` |
| Rewards & Penalties | 20 | scenario conclusion |
| Statistics; The Orphan School Horror (Harvest the Child, Bring Forth the Child, Vulnerability to the Bane, таблица) | 21–22 | `creature/orphan-school-horror` (арт со с. 21); таблица — также scenario `tables` «Погибель Ужаса: величина действия» |
| Orphan School Ghosts (Harvest Adults) | 22 | `creature/orphan-school-ghosts` (арт со с. 17) |
| Further Source Material | 23 | не взято |

## Ticket of Leave #10 — The Doom That Came To Five Dock

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| обложка, Credits | 1 | scenario sources; обложка — atmosphere |
| Introduction (эпиграф майора Роберта Росса, 1788) | 1 | `convicts-tol-10-en/scenario/the-doom-that-came-to-five-dock` advice («Вступление выпуска») |
| Scenario Seed: The Doom That Came To Five Dock | 2 | scenario; `location/five-dock` |
| Ferries on the Parramatta River (врезка) | 2 | scenario advice |
| Keeper's Introduction | 2 | scenario keeper_info |
| The Insect Horror | 2 | scenario keeper_info; `creature/zstylzhemgni` |
| The Shriek of Doom | 3 | scenario keeper_info; `character/mcgrath` |
| The Owners of Five Dock Farm | 3 | scenario keeper_info; `location/five-dock-farm` |
| Involving the Investigators | 3 | `scene/getting-started`; scenario hook |
| карта Principal Regions of His Majesty’s Colony at New South Wales | 3 | `map/principal-regions-of-new-south-wales` (11 меток) |
| The True Nature of the Threat | 4 | scenario keeper_info; сцены вариантов |
| Dr. John Harris, NSW Corps Surgeon 1754-1838 (врезка) | 4 | `convicts-cthulhu-en/character/john-harris` (биография — абзацем в legend при сведении; в scenario advice — ссылка); `proposals-tol-c.json` |
| Knights of Asclepius (врезка) | 5 | `organization/knights-of-asclepius` |
| Getting Started | 5–6 | `scene/getting-started` |
| Junior Surgeon, Matthew Toomey (врезка) | 6 | `character/matthew-toomey` |
| Asking Around Sydney; Asking about tales of strange flying creatures…; Questioning the Blinded Ferryman | 6 | `scene/asking-around-sydney`, `character/mcgrath` |
| Questioning the Ferry crew…; Asking about a group of “Convict Girls”…; Asking about Eliza Petty | 7 | `scene/asking-around-sydney` |
| Asking about Rev George Fenby; About Dr Matthew Toomey and preparations… | 8 | `scene/asking-around-sydney`, `character/george-fenby`, `location/toomey-house`, `item/rum-jar-eggs`, `item/expedition-rum-jars` |
| Devastation at the Docks | 8 | `scene/devastation-at-the-docks`, `item/petty-mythos-tome` |
| At Five Dock Farm | 8–9 | `scene/at-five-dock-farm`, `character/eliza-petty`, `item/eliza-petty-ring` |
| The Waterhole | 9–10 | `scene/the-waterhole`, `location/five-dock-waterhole` |
| Mother’s Watch | 10 | `scene/the-waterhole`; creature encounters |
| Toomey’s Dream Haul (врезка) | 10 | `scene/the-waterhole` |
| The Wangal Community | 11 | `scene/wangal-community`, `organization/wangal-community` |
| Defeating the Matriarch and her Swarms | 11–12 | `scene/defeating-the-matriarch` |
| Mythos Options | 12 | сцены вариантов |
| Option A: The Long-Suffering Shackle | 12 | `scene/option-a-long-suffering-shackle` |
| Option B: The Blackest Mail | 12–13 | `scene/option-b-blackest-mail`, `item/blackmail-letters`, `item/toomey-journal` |
| Option C: The Egg That Doth Not Hatch | 13–14 | `scene/option-c-egg-that-doth-not-hatch`, `item/zstylzhemgni-eggs` |
| Rewards and Penalties | 14 | scenario conclusion |
| Statistics; Dr. Matthew Toomey | 14 | `character/matthew-toomey` |
| Dr. John Harris (статблок) | 14 | `proposals-tol-c.json` (set statblock у записи основной книги) |
| Eliza Petty | 14–15 | `character/eliza-petty` |
| New Spells; Call/Dismiss Zstylzhemgni; Enchant Wound | 15 | черновики `spell-call-dismiss-zstylzhemgni-tol-c.json`, `spell-enchant-wound-tol-c.json` |
| The Matriarch of Swarms (aka Zstylzhemgni) (Poison Sting, Sonic Screech, таблица, Inject Eggs, Remain in this Reality) | 15–17 | `creature/zstylzhemgni` (арт со с. 16); таблица визга — также scenario `tables` |
| Spawn of the Cicada (Zstylzhemgni’s hatchling offspring) | 17 | `creature/spawn-of-the-cicada` |

## Не взято

- Списки литературы и ссылки: #8 с. 3–5 (ссылки в конце биографий), с. 20 «Further Source Material» (книги Хёрста и Мура,
  отчёт комитета 1812, суд над Палмером, жизнь Джорджа Крибба, путеводитель по Скалам); #9 с. 3 (ссылка о Кенте), с. 7
  (источники врезки о Рождестве), с. 23 «Further Source Material» (диссертации Бубач и Бриджеса, Кливерли, Дэниелс, Данн);
  #10 — нет. Причина: библиография, не игровой материал.
- Реклама основной книги внизу последней страницы каждого выпуска; блоки Credits и лицензия Chaosium (кроме авторов и года —
  они в summary сценариев).
- Мелкие безымянные фигуры без своих записей (остались текстом сцен): констебль и неряшливый капрал Парраматты, ночной сторож,
  охранник Уолтона, жена и дети Барленда, двое каторжников-стражей Барленда, ковен поклонников Йог-Сотота в Англии (#8);
  нынешний привратник, кухарка и экономка, молодой бездельник у стены, писари житницы (#9); капитан парома, четверо
  работников фермы, похмельный солдат-конвоир, мать Элайзы, старейшина вангалов (#10).
- Члены комитета без своих записей (упомянуты в организации): преподобный Джонсон, Уильям Балмейн, Элизабет Кинг, Дэвид Дикенсон
  Манн, Уильям Кокс; жена сержанта Страуда, миссис Ньюшем, миссис Марчант (имена не даны или упомянуты вскользь); Эндрю
  Гамильтон Хьюм (текст организации).
- Рамки врезок и заставки-полосы — оформление; атмосферные иллюстрации — `atmosphere-tol-c.json` (14).

## Опечатки и расхождения книги

- #8, с. 20: Claw «60% (30/15)» — пятая часть 12; исправлено в записи (`errata`, `corrections`, Р-35).
- #8, с. 12: «McCartry» (псевдоним); с. 6: «George Cribbs’» (псевдоним); с. 15: «Greenslieigh» (словесная).
- #8: место гибели Лайла — «фермерский дом, где он прячется» (с. 10) и дом в Киррибилли (с. 13–14); Вудхаус — «ферма» (с. 8)
  и «дом в Парраматте» (с. 11); заклинание названо и «Summon Thing from the Bone Pit» (с. 19), и «Summon Thing in the Pit» (с. 19).
- #9, с. 8 и 10: пропавшие женщины — «две недели и неделю назад» против «за последние четыре дня» (`errata` сценария).
- #9, с. 20: «Melrose» вместо «Montrose» дважды (псевдоним); с. 18: «Female Orphan Horror»; с. 21: «Stealth Know Fears 100%» —
  лишнее «Stealth»; с. 22: у «большого» и «значительного» действия бросок в таблице напечатан одинаково.
- #10, с. 14: Харрис «Credit Rating Accounting 65%» — лишнее «Credit Rating» (в предложении — Бухгалтерское дело 65%).
- #10, с. 15: «cumulative 5% change» — «chance»; размах крыльев Матриарха «at least 10 yards» (с. 2) и «about 35 feet» (с. 15).

## Термины (английский → русский), выбранные в этой части

Согласованы с записями части core (уже созданными): NSW Corps → Корпус Нового Южного Уэльса; Female Orphan School → Школа для
девочек-сирот; Matron / Master → надзирательница / смотритель; The Rocks → Скалы; Lane Cove → Лейн-Ков; Female Factory →
Женская фабрика; Government House → Дом правительства; Sydney Gaol → Сиднейская тюрьма; Sydney Hospital → Сиднейская больница;
The Black Swan → «Чёрный лебедь»; Hawkesbury → Хоксбери; Van Diemen’s Land → Земля Ван-Димена; Coal River → Коул-Ривер.

Новые: Ticket of Leave → отпускной билет (каторжник с отпускным билетом); Gentlemen Convicts → каторжники-джентльмены; Scottish
Martyrs → Шотландские мученики; United Irishmen → «Объединённые ирландцы»; Enlightened Brothers → Просвещённые братья; Hogg’s Hogs →
Хогговы хряки; Staves of Thyrsus → Жезлы Тирса; The Gentleman Stalker → Джентльмен-преследователь; The Man in the Blue Coat →
Человек в синем сюртуке; The Thing from the Bone Pit → Тварь из костяной ямы; Bone Pit / charnel pit → костяная яма; magickal
proxies → магические заместители (бутылки-заместители); brazier → жаровня; Mythos Options → варианты Мифов; The Hunter From The
Past → Охотник из прошлого; Dreams of Freedom Dying → Сны умирающей свободы; The Bone Book of the Patriarch → Костяная книга
Патриарха; Summon Thing from the Bone Pit → Призыв твари из костяной ямы; Track Summoners → Выследить призывателей; Supernatural
Movement → Сверхъестественное перемещение; Songlines → песенные тропы; Aboriginal Lore → Знания аборигенов; Chiv → заточка;
Orphan School Horror → Ужас сиротской школы; Orphan School Ghosts → призраки сиротской школы; Bane → погибель; minor / major /
significant action → малое / большое / значительное действие; Harvest the Child → Жатва ребёнка; Bring Forth the Child → Пробудить
ребёнка; Harvest Adults → Жатва взрослых; Know Fears / Know Childhood Trauma / Know Childhood Fears → Знать страхи / Знать детские
травмы / Знать детские страхи; Ur-Lloigor → Ур-ллойгор; The Crack in Reality → Трещина в реальности; The Nexus of Need →
Средоточие нужды; The Guest of Captain Kent → Гость капитана Кента; Eaters Out Of Space → Пожиратели извне; banishment seal →
печать изгнания; An Encounter with the Lonely Dead → Встреча с Одинокими мёртвыми; Female Orphan School Committee → Комитет Школы
для девочек-сирот; scald head → парша; marriage cow → свадебная корова; Zstylzhemgni → Зстилжемгни; The Matriarch of Swarms →
Матриарх роёв; Insect God → бог-насекомое; Spawn of the Cicada → Отродье цикады; Knights of Asclepius → Рыцари Асклепия; Call/Dismiss
Zstylzhemgni → Вызов/изгнание Зстилжемгни; Enchant Wound → Зачарование раны; Poison Sting → Ядовитое жало; Sonic Screech →
Звуковой визг; Inject Eggs → Ввести яйца; Remain in this Reality → Пребывание в этой реальности; The Long-Suffering Shackle →
Многострадальные оковы; The Blackest Mail → Чернейший шантаж; The Egg That Doth Not Hatch → Яйцо, что не проклюнется; Mother’s
Watch → Дозор матери; Toomey’s Dream Haul → Мечта Туми; Wangal → вангалы; Eora → эора; Cadigal → кадигалы; Cammeraygal →
кэммерайгалы; the Dreaming → Время сновидений; corroboree → корробори; [HARD] → [ТРУДНО]; Charm/Bootlick → Обаяние/угодничество;
Gambling → Азартные игры; Five Dock → Файв-Док; Kirribilli → Киррибилли; Ultimo → Ультимо; Peregrine → «Перегрин».

Имена: Sarum Greensleigh → Сарум Гринсли; Francis Walton → Фрэнсис Уолтон; Anthony Woodhouse → Энтони Вудхаус; George Barland →
Джордж Барленд; William Chaffey → Уильям Чаффи; John McCarty → Джон Маккарти; Thomas Hogg → Томас Хогг; Ignatius Lyle →
Игнейшес Лайл; Annie Beddows → Энни Беддоуз; George Cribb → Джордж Крибб; Harland Drake → Харланд Дрейк; Thomas Muir → Томас
Мьюр; Thomas Fyshe Palmer → Томас Фиш Палмер; Maurice Margarot → Морис Маргаро; Henry Browne Hayes → Генри Браун Хейс; John Grant →
Джон Грант; Elizabeth Paterson → Элизабет Патерсон; William Kent → Уильям Кент; Clive Montrose → Клайв Монтроз; Mary Asker → Мэри
Аскер; Bethany Small → Бетани Смолл; Margaret Boyne → Маргарет Бойн; Harriet Torrence → Гарриет Торренс; Lettie Crookes → Летти
Крукс; Jenny Cowley → Дженни Коули; John Biggell → Джон Биггелл; Catherine Woakes → Кэтрин Воукс; Matthew Toomey → Мэтью Туми;
Eliza Petty → Элайза Петти; George Fenby → Джордж Фенби; McGrath → Макграт.

## Вопросы владельцу

1. Фотопортрет пожилой женщины без подписи (#9, с. 9) рядом с «The Interview with Mrs Paterson» — считать ли портретом
   Элизабет Патерсон? Пока в `atmosphere-tol-c.json`.
2. Карта «Principal Regions…» (#10, с. 3) может совпасть с картой основной книги (у core ожидается
   `convicts-cthulhu-en/map/new-south-wales-1802`) — если так, записи свести.
3. Навыки существ «Know Fears», «Know Childhood Trauma», «Know Childhood Fears» и навыки сеттинга «Gambling», «Aboriginal Lore» —
   без записей справочника (не связаны).
