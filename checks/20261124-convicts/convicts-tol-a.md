# Convicts & Cthulhu — Ticket of Leave #1–#4 (часть tol-a)

Книги: `convicts-tol-01-en` (4 с.), `convicts-tol-02-en` (6 с.), `convicts-tol-03-en` (8 с.), `convicts-tol-04-en` (14 с.).
Во всех четырёх PDF печатная страница = физической (номер «1» на физ. 1): **offset 0** (в `books.json` не записан — ставит ведущий).
Метки библиотеки «[EN 6e]» неверны: статблоки — 7-я редакция (проценты, «Build», «Move», доли «(25/10)»).
Русского перевода нет; русский текст — наш перевод (`translated`). Эпоха — `other`.

## Заголовок книги → где в базе

### #1 Night Terrors (`convicts-tol-01-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Night Terrors (титул, врезка о Tickets-of-Leave) | 1 | `convicts-tol-01-en/scenario/night-terrors` (summary) |
| Introduction | 1 | `…/scenario/night-terrors` (keeper_info: «Сеттинг») |
| The Night Watch | 1 | `…/scenario/night-terrors` (hook; псевдоним «Ночной дозор») |
| General Orders (газетная вырезка) | 1 | `…/handout/general-orders` (текст как напечатан + перевод, картинка) |
| Backstory | 2 | `…/scenario/night-terrors` (keeper_info), `…/organization/warehouse-cult` |
| Investigator Roles & Other Patrollers | 2 | `…/scenario/night-terrors` (hook) |
| Potential Patrol Members (Styles, Goode, Marriot, Tully, Selkirk, Mavery) | 2 | `…/character/john-styles`, `victor-goode`, `freddy-marriot`, `benjamin-tully`, `henry-selkirk`, `jenny-mavery` (instance_of типажей основной книги) |
| The Patrol’s Route & Encounters | 2 | `…/scenario/night-terrors` (advice, шаг «Маршрут патруля») |
| таблица случайных встреч (1D3 × 1D8) | 3 | `…/scenario/night-terrors` → `tables` «Случайные встречи патруля» (24 строки) |
| The Unfolding Adventure | 3 | `…/scenario/night-terrors` (steps) |
| First Night | 3 | `…/scene/first-night`, `…/character/charlie-cookman`, `…/character/hezekiah-barnes` |
| Second Night | 3 | `…/scene/second-night`, `…/item/foremans-face`; Бродяга — `coc:creature:dimensional-shambler` |
| Third Night | 4 | `…/scene/third-night` |
| Resolution | 4 | `…/scene/resolution`, `…/scenario/night-terrors` (conclusion) |
| The Warehouse (план) | 4 | `…/map/warehouse` (24 метки), `…/location/lord-warehouse`, `…/location/warehouse-lower-croft`, `…/location/warehouse-upper-croft` |
| Footnotes | 4 | `…/handout/general-orders` (description) |

### #2 Tricolour Terror (`convicts-tol-02-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Tricolour Terror (титул), Introduction | 1 | `convicts-tol-02-en/rule/french-in-the-colonies` |
| French and English Encounters + карта «French Exploration in Australia» | 1 | `…/map/french-exploration-in-australia` (10 меток), `…/location/new-holland`, `geographe-bay`, `terre-napoleon`, `encounter-bay`, `king-island`, `recherche-bay`, `port-phillip` |
| вступление (страх французского вторжения) | 2 | `…/rule/french-in-the-colonies` (text) |
| Timeline | 2 | `…/rule/french-in-the-colonies` → таблица «Хронология» (24 строки) |
| Letter from Gov. King to Nicholas Baudin | 3 | `…/handout/king-letter-to-baudin` (текст переписан с рукописи + перевод, картинка) |
| Les Nouveaux Mystères: French Occult Exploration in the South Pacific | 3 | `…/organization/les-nouveaux-mysteres` |
| New Occupations; French Naturalist | 3 | черновик `coc:occupation:convicts-french-naturalist` → `checks/20261124-convicts/occupation-convicts-french-naturalist-tol-a.json` |
| French Occult Explorer | 4 | черновик `coc:occupation:convicts-french-occult-explorer` → `…/occupation-convicts-french-occult-explorer-tol-a.json` |
| French Explorers of Australia | 4 | `…/rule/french-in-the-colonies` (refs) и записи ниже |
| Jean-Francois de Galaup La Perouse (1741-1788) | 4 | `…/character/la-perouse` |
| Joseph-Antoine Raymond Bruny d'Entrecasteaux (1739-1793) | 4 | `…/character/bruny-dentrecasteaux` (статблок) |
| Nicolas Thomas Baudin (1754-1803) | 4 | `…/character/nicolas-baudin` (статблок) |
| Francois Péron (1754-1803) | 5 | `…/character/francois-peron` (статблок, портрет) |
| Adventure Seed: Tricolour Terror | 5 | `…/scenario/tricolour-terror` |
| Beginning the Adventure | 5 | `…/scene/beginning-the-adventure`, `…/character/french-castaways`, `…/location/remarquable`, `…/item/bell-shaped-things` |
| The Mission | 5 | `…/scene/the-mission` |
| Complications | 6 | `…/scene/complications`, `…/character/walter-hale`, `…/item/french-notebook` |
| The Solution: Option 1 / 2 / 3 | 6 | `…/scene/option-antipodean-shoggoths`, `option-gulf-between-oceans`, `option-floating-fungi` (существа — общие записи шоггота, Звёздного отродья, ми-го) |
| Further Reading | 6 | `…/scenario/tricolour-terror` (advice, ссылки как напечатаны) |

### #3 Criminal Enterprise (`convicts-tol-03-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Criminal Enterprise (титул), Introduction | 1 | `convicts-tol-03-en/rule/nature-of-crime` (text) |
| карта Дженкса (без подписи) | 1 | `…/map/jenks-map` (12 меток), `…/handout/jenks-map` (подписи как напечатаны + перевод, картинка) |
| The Nature of Crime in the Colony of New South Wales | 2 | `…/rule/nature-of-crime` |
| Joining a Gang – By Hook or By Crook | 2–3 | `…/rule/joining-a-gang` |
| The Jenks Gang | 3 | `…/organization/jenks-gang` |
| Sgt Jonathan Jenks, Gang Leader | 3 | `…/character/jonathan-jenks` |
| George Leather, Smuggler | 3 | `…/character/george-leather` |
| Mary Franklin, Assigned Convict and Thief | 3 | `…/character/mary-franklin` |
| Felix Biggs, Burglar | 4 | `…/character/felix-biggs` |
| Samuel Seeler, Sailor and Merchant | 4 | `…/character/samuel-seeler`, `…/character/graham-potts` |
| Robert Morton, Ticket-of-Leave Man and Gambler | 4 | `…/character/robert-morton` |
| Typical Schemes of the Jenks Gang | 4–5 | `…/organization/jenks-gang` (goals, 5 пунктов) |
| Scenario Sketch: Shyneth As The Gold | 5 | `…/scenario/shyneth-as-the-gold` |
| A Simple Plan | 5 | `…/scene/a-simple-plan`, `…/item/goblet-of-the-king` |
| About the Smales | 5–6 | `…/scenario/shyneth-as-the-gold` (keeper_info), `…/character/mr-and-mrs-smales`, `…/character/sarah-smales` |
| Smuggling on the Georges River (Navy Patrols, Banks’ Town Volunteers, Weird Things) | 6 | `…/scene/smuggling-on-the-georges-river`, `…/character/banks-town-volunteers`, `…/item/distillation-equipment`; река — `convicts-cthulhu-en/location/georges-river` (дополнение — предложение) |
| Location: Banks' Town | 6 | `…/location/banks-town` |
| The Smales Family Farm | 7 | `…/scene/smales-family-farm`, `…/location/smales-farm` |
| The Smales Farmstead (план) | 7 | `…/map/smales-farmstead` (12 меток), `…/location/smales-farmhouse`, `smales-large-barn`, `smales-small-barn` |
| Returning to Rob the Smales | 7 | `…/scene/returning-to-rob-the-smales` |
| Mr and Mrs Smales, Weirdly Similar Weirdos | 8 | `…/character/mr-and-mrs-smales` (один статблок на пару) |
| Ritual of the Yellow Zombie (в статблоке) | 8 | черновик `coc:spell:ritual-of-the-yellow-zombie` → `checks/20261124-convicts/spell-ritual-of-the-yellow-zombie-tol-a.json` |
| Yellow Zombies (текст и статблок) | 8 | `…/creature/yellow-zombie` |
| Further Reading | 8 | `…/scenario/shyneth-as-the-gold` (advice), сайт Бэнкстауна — там же |

### #4 The Vanishing Ensign (`convicts-tol-04-en`)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Vanishing Ensign (титул), Introduction | 1 | `convicts-tol-04-en/rule/blighs-muster-of-1807` (text), `…/scenario/grand-muster` |
| Returns from the Governor's Muster … January 1807 (изображение) | 1 | `…/handout/muster-returns-january-1807` (таблица переписана + перевод, картинка) |
| Historical Context: Bligh’s Muster of 1807 | 2 | `…/rule/blighs-muster-of-1807` |
| The Grand Muster Campaign Frame | 2 | `…/scenario/grand-muster` |
| Called to the Muster | 2 | `…/scene/called-to-the-muster` |
| (Optional) NPC Leaders for the Muster Party | 3 | `…/character/richard-fitch`, `…/character/charles-rogers` |
| Undertaking the Survey | 3 | `…/scene/undertaking-the-survey` |
| Searching Correspondence and Records | 4 | `…/scene/searching-correspondence-and-records` |
| Five ways… research and letter writing (врезка) | 4 | `…/scenario/grand-muster` → `tables` «Сценарии из записей и переписки» |
| Visiting Sites Near Sydney | 5 | `…/scene/visiting-sites-near-sydney` |
| The Perils of Damp Gunpowder | 5 | `…/rule/perils-of-damp-gunpowder` |
| Visiting Sites Near Parramatta | 5 | `…/scene/visiting-sites-near-parramatta` |
| Five ways… visits to sites around Sydney or Parramatta (врезка) | 6 | `…/scenario/grand-muster` → `tables` «Сценарии из посещений Сиднея и Парраматты» |
| Enclosure to the Governor's Correspondence: Return of Ordnance (изображение) | 6 | `…/handout/return-of-ordnance` |
| Absent Officers / Officers in Command / Officers Present (изображение) | 7 | `…/handout/officers-ledger` |
| Visiting Outlying Places: Coal River and Hawkesbury | 7 | `…/scene/visiting-outlying-places`, `…/location/guinevere`, `…/character/captain-spillman` |
| Five examples… outlying or remote parts (врезка) | 8 | `…/scenario/grand-muster` → `tables` «Сценарии из поездок в дальние края» |
| Wrapping Up the Muster | 8 | `…/scene/wrapping-up-the-muster` |
| Scenario Outline: The Vanishing Ensign | 8 | `…/scenario/vanishing-ensign` (part_of grand-muster) |
| Keeper's Introduction | 8–9 | `…/scenario/vanishing-ensign` (keeper_info) |
| Who is “Job Thrasher”? (врезка) | 9 | `…/scene/who-is-job-thrasher`, `…/character/job-thrasher`, `…/location/thrashers-grave` |
| The Investigations; At the First Location | 9–10 | `…/scene/at-the-first-location` |
| At the Second Location; Subsequent Locations | 10 | `…/scene/at-the-second-location` |
| The Final Location | 10 | `…/scene/at-the-final-location` |
| Three Possible Mythos Solutions | 10 | `…/scenario/vanishing-ensign` (steps) |
| Option One: Dobley is a Deep One Hybrid (Dobley’s Secret, Unique Clues, Job Thrasher, Denouement) | 10–11 | `…/scene/option-one-deep-one-hybrid`, `…/item/thrashers-notebook`, `…/character/isaac-pell` |
| Ensign Ernest Dobley as a Deep One Hybrid (статблок, Special Powers) | 11 | `…/character/ernest-dobley` (статблок, способности, картинка) |
| Melt Into Background (врезка) | 11 | `…/character/ernest-dobley` (abilities) |
| Mother Hydra's Fetish (врезка) | 11 | `…/item/mother-hydras-fetish` |
| Option Two: Dobley is a Ghost | 12 | `…/scene/option-two-ghost`, `…/item/forged-service-records` |
| Job Thrasher & The Ghostly Ensign | 12 | `…/character/job-thrasher` (legend; instance_of «Типичный каторжник»), `…/character/ernest-dobley` (вариант «Призрак») |
| The Cursed Gold | 12 | `…/item/cursed-gold` |
| Option Three: Dobley is the Victim of Foul Sorcery | 13–14 | `…/scene/option-three-foul-sorcery` (картинка), `…/item/dobley-dummy`, `…/location/thrashers-farmstead`, `…/character/ned-crowe` |
| Job Thrasher, Mythos Sorcerer (статблок) | 14 | `…/character/job-thrasher` |
| Thrasher's Wizardry | 14 | `…/character/job-thrasher` (abilities: варианты «Околдовать жертву» и «Вызова Йог-Сотота») |
| References | 14 | `…/rule/blighs-muster-of-1807` (text, «Источники») |

## Не взято

- Врезка «Tickets-of-Leave are small self-contained additions…» и «Credits» на с. 1 каждого выпуска, лицензия CC, реклама основной книги внизу последней страницы — выходные данные, без игрового содержания (имена авторов и годы — в summary сценариев).
- Ссылки «For more info, see: http://adb.anu.edu.au/…» у исследователей (#2) — оставлены текстом в legend; отдельных записей нет.
- Призыв поддержать Internet Archive в «References» (#4) — не игровой текст.
- Декоративные рамки врезок и гравюра «колонна каторжников» (#3 с. 4, #4 с. 4), логотипы — в `atmosphere-tol-a.json`.
- Исторические офицеры из книги смотра (#4 с. 7: Гроуз, Фово, Кемп, Мур, Пайпер, Эббот, Брабин, Патерсон, Джонстон, Минчин, Лейкок и др.) — только текстом раздатки; ссылки — на записи основной книги, где они есть (Гроуз, Кемп, Харрис, Патерсон, Джонстон).
- Персонажи, упомянутые мимоходом без роли в игре (секретарь Э. Гриффин и майор Джонстон в приказе — ссылки на записи основной книги; капитан Эббот; бывший ювелир в Парраматте; американский корабль; контрабандисты Трэшера; старый каторжник-свидетель в разгадке 2; Флиндерс, Басс, Дампир, Ламарк, де Фрейсине, д’Орибо, Хассалл) — текстом в записях.
- Отдельная запись Матери Гидры не заводилась: ссылка на общую `coc:creature:dagon-i-gidra` (в книге — статистика по «Книге хранителя», с. 286–287).
- «Yellow Decay» (вариант «Green Decay») — без своей записи: в статблоке Смейлзов ссылка на `coc:spell:green-decay`, отличие — в `spells.raw`.

## Опечатки и сомнения (в `errata` записей)

- #1: обещаны «наброски семи патрульных», дано шесть (сценарий); «Bidigal» вместо «Bidjigal» (таблица, исправлено в переводе); «local goal» вместо «gaol» (молча); дата шапки вырезки 13 августа 180… против даты приказа 13 мая 1806 (раздатка).
- #2: годы Перона «(1754-1803)» повторяют годы Бодена (исторически 1775–1810); Скорость д’Антркасто 6, Бодена 7, Перона 7 не по правилам (возрастные поправки частично объясняют; как напечатано).
- #3: Дженкс — Уклонение «45% (22/7)» → (22/9) исправлено (Р-35); Смейлзы — Скорость 10, ИНТ 110 (как напечатано); жёлтые зомби — средние 80 у СИЛ/ВЫН/МОЩ при бросках 3d6×5 (со средними сходятся ПЗ, БкУ, ПМ — вероятна опечатка в броске; как напечатано).
- #4: «Rogers» / «Rodgers» (Роджерс); Трэшер — «Brawl 80% (20/8)», «Axe 80% (20/8)» → доли исправлены на (40/16) по Р-77, возможна опечатка процента (40%); у «Art/Craft (Wood Carving)» нет значения; Скорость Добли 8 и Трэшера 6 — с возрастной поправкой; «Mother Dagon» вместо «Mother Hydra» (фетиш); в итогах смотра сумма барабанщиков 16 при «Итого» 18; «investors» вместо «investigators», «appraiseapprise» (молча).

## Термины этого выпуска (английский → русский)

Ticket of Leave → отпускной билет; ticket-of-leave man → каторжник с отпускным билетом; convict → каторжник; assigned convict → приписанный каторжник; ex-convict / freed convict → бывший каторжник; NSW Corps → Корпус Нового Южного Уэльса; Volunteer Association → Добровольческая ассоциация; Night Watch / patrol → ночной дозор / патруль; gaol → тюрьма; Chief Constable → главный констебль; Commissariat → Комиссариат; General Orders → «Общие приказы»; Government Gazette → «Правительственная газета»; taptoo → тапту; supercargo → суперкарго; factor → фактор; centinel → часовой; Clever Man → знахарь; the Dreaming → Время сновидений; Alcheringa → Алчеринга; Cadigal → кадигал; Bidjigal → бидьигал (как в основной книге); Les Nouveaux Mystères → «Новые Мистерии»; French Naturalist → Французский натуралист; French Occult Explorer → Французский оккультист-исследователь; Charm/Bootlick → Обаяние/Угодничество; Jenks Gang → банда Дженкса; Yellow Zombie → жёлтый зомби; Yellow Taint → жёлтая порча; Goblet of the King → Кубок Короля (золотой кубок); Ritual of the Yellow Zombie → Ритуал жёлтого зомби; Yellow Decay → Жёлтое гниение; Fowling Piece → охотничье ружьё; Musket → мушкет; Carbine → карабин; Flintlock Pistol → кремнёвый пистолет; Bligh’s Muster → смотр Блая; Grand Muster → Великий смотр; Campaign Frame → рамка кампании; muster party → группа смотра; Ensign → прапорщик; damp gunpowder → отсыревший порох; Melt Into Background → «Слиться с фоном»; Deep Lungs → «Глубокие лёгкие»; Mother Hydra's Fetish → Фетиш Матери Гидры; Cursed Gold → Проклятое золото; cutter Guinevere → куттер «Гвиневра»; Banks' Town → Бэнкс-Таун; New Holland → Новая Голландия; Terre Napoleon → Земля Наполеона; Encounter Bay → залив Встречи; Geographe Bay → залив Географ; Recherche Bay → бухта Решерш; King Island → остров Кинг; Port Phillip → Порт-Филлип.
Формы основной книги, взятые без изменений: Саймон Лорд, Ботани-Бей, мыс Доуз, Кейп-Бэнкс, Кукс-Ривер, мыс Соландер, река Джорджес, река Хоксбери, Коул-Ривер, Порт-Далримпл, Земля Ван-Димена, Хобарт-Таун, остров Норфолк, Дом правительства, Сиднейская тюрьма, Сиднейская больница, форт Филлип (Виндмилл-Хилл), Уильям Блай, Филип Гидли Кинг.
Имена: Лаперуз; Брюни д’Антркасто; Николя Боден; Франсуа Перон; Джонатан Дженкс; Смейлз; Эрнест Добли; Джоб Трэшер; Ричард Фитч; Чарльз Роджерс; Спиллман.

## Вопросы владельцу

1. Карта континента (#2) требует вершины гайда: заведена `convicts-tol-02-en/location/new-holland` с видом «город сценария» (общей записи Австралии нет). Оставить так или завести общую запись?
2. Склад Саймона Лорда (#1) привязан к «Дому и складу Саймона Лорда» основной книги, хотя выпуск допускает и Парраматту.
