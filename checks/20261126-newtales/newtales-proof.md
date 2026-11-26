# New Tales of the Miskatonic Valley 2E — часть proof: «Proof of Life» («Доказательство жизни»)

Книга `new-tales-miskatonic-valley-2e-en`, печатные с. 72–100, раздатка с. 165, 170, карты с. 189–192 (смещение 0: печатная = физической,
сверено по изображениям с. 72–100 и 165–192). Все записи — `kb/books/new-tales-miskatonic-valley-2e-en/`; id ниже — без префикса книги.
Русский текст — наш перевод (Р-251, Р-21, флаг `translated`). Сценария в русских переводах базы нет (проверено по «Фоксфилд», «Foxfield»,
«Барнс», «Копли», «Мэдсен», «Уиппл» в `kb/books/*-ru/`).

Записей: 123 — сценарий 1, сцен 21, персонажей 29 (из них 4 групповых профиля), существ 4, мест 43, предметов 13, организаций 4, раздаток 3, карт 5.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Карта «Foxfield» (врезка «The Heart of Foxfield») | 72 | `map/foxfield-map` (44 метки); места `location/foxfield`, фермы и урочища по меткам (см. ниже) |
| Proof of Life (вступление) | 73 | `scenario/proof-of-life` (summary, hook); `organization/crestfield-lumber` |
| Keeper Information | 73–74 | `scenario/proof-of-life` (keeper_info); `character/henry-barnes`, `character/sarah-brock`, `location/mi-go-lair` |
| Investigator Information | 74 | `scenario/proof-of-life` (hook), `scene/proof-arriving-in-foxfield`, `handout/proof-of-life-papers-1` |
| A History of Foxfield | 74 | `location/foxfield` (history), `location/foxfield-road` |
| Supervisor Henry Barnes | 74–75 | `character/henry-barnes`, `character/helen-barnes`, `character/mary-barnes`, `character/robert-barnes` |
| Ike Copley | 75 | `character/ike-copley`, `organization/congregates` |
| Arriving in Foxfield | 75–76 | `scene/proof-arriving-in-foxfield`, `location/foxfield` |
| Places & People | 76 | раздел книги → сцены и места ниже |
| Parker’s General Store | 76 | `location/parkers-general-store`, `scene/proof-parkers-general-store` |
| Louise Madsen | 76 | `character/louise-madsen` |
| What Louise Knows (Foxfield History; Supervisor Barnes; Barnes and Copley Conflict; Town Records; Offices of The Foxfield Courier) | 76–77 | `scene/proof-parkers-general-store`, `character/louise-madsen` (legend) |
| More About Rodney Greene | 77 | `character/rodney-greene` |
| The Mailman (Supervisor Barnes; The Timber Lease; Ike Copley; The Congregates) | 77–78 | `character/sydney-etzler`, `scene/proof-parkers-general-store` |
| Shirley Sutler (Supervisor Barnes; The Timber Lease; Ike Copley; The Congregates) | 78 | `character/shirley-sutler`, `scene/proof-parkers-general-store` |
| Others | 78 | `location/parkers-general-store`, `scene/proof-parkers-general-store` |
| Foxfield Farm Implements & Stable | 78 | `location/foxfield-farm-implements`, `scene/proof-farm-implements`, `character/richard-slate`, `character/dora-slate` |
| The Rodney Greene Home (Supervisor Barnes; The Timber Lease) | 78–79 | `location/greene-home`, `scene/proof-greene-home`, `character/ida-greene` |
| The Old Pickering House | 79 | `location/old-pickering-house`, `scene/proof-town-records`, `item/foxfield-town-records` |
| Offices of the Foxfield Courier (Pickering Mill and Family; The Congregates; Strange Occurrences) | 79 | `location/foxfield-courier-office`, `scene/proof-foxfield-courier`, `item/foxfield-courier-files`, `character/wilson-keyes`, `character/aaron-pickering`, `character/bertrand-pickering`, `character/james-pickering` |
| Follow-ups | 79–80 | `scene/proof-follow-ups`, `character/elias-whipple` |
| The Foxfield Unitarian Church | 80 | `location/foxfield-unitarian-church` (кладбище и мавзолей Пикерингов — в описании) |
| Henry Barnes (Foxfield History; Ike Copley; The Timber Lease; His Family; The Town Meeting) | 80–81 | `scene/proof-unitarian-church`, `character/henry-barnes`, `location/brookdale-school` |
| Church Records (Parishioner Records; Church Accounts) | 81 | `item/church-records`, `scene/proof-unitarian-church`, `organization/quigley-and-sons` |
| The Schoolhouse | 81–82 | `location/foxfield-schoolhouse`, `scene/proof-schoolhouse`, `character/betty-ward`, `character/bobby-kirtland` |
| Schoolmarm Aida Simpson | 82 | `character/aida-simpson` |
| The Southern Farmers | 82 | `location/southern-farms`, `scene/proof-southern-farmers`, `character/typical-southern-farmer` |
| Barnes’ Residence | 83 | `location/pickering-mansion`, `scene/proof-barnes-residence` |
| A Clue or Two | 83 | `item/quigley-letters` |
| A Mysterious Object | 83 | `item/mi-go-stone-key` |
| The Cellar | 83 | `location/pickering-mansion` (описание), `scene/proof-barnes-residence` |
| The Upstairs Bedrooms | 83 | `location/pickering-mansion-locked-bedroom`, `item/barnes-photo-album`, `item/barnes-children-brain-cylinders` |
| Robert’s Canister; Mary’s Canister | 83 | `item/barnes-children-brain-cylinders` (mechanics), `character/robert-barnes`, `character/mary-barnes` |
| The Covered Bridge | 84 | `location/foxfield-covered-bridge`, `scene/proof-mill-town` |
| Mill Town | 84 | `location/mill-town`, `scene/proof-mill-town` |
| The Mill Town Squatters | 84–85 | `location/chylinski-home`, `character/rose-chylinski`, `character/peter-chylinski` |
| The Ruined Mill | 85–86 | `location/pickering-mill`, `scene/proof-ruined-mill` |
| Scuttlers—A Keeper’s Toy (врезка, статблок A Typical Scuttler) | 85 | `creature/scuttler`; совет — `scenario/proof-of-life` (advice) |
| Inside the Mill; Ground Floor; Second Floor; Third Floor | 86–87 | `location/pickering-mill`, `scene/proof-ruined-mill` |
| Scuttlers in the Mill | 87 | `scene/proof-ruined-mill`, `creature/scuttler` (legend) |
| The North Road | 87 | `location/north-road`, `scene/proof-north-road` |
| The Northern Farms | 87 | `location/northern-farms`, `organization/congregates`, `character/typical-northern-farmer` |
| The Ike Copley Farm | 88 | `location/copley-farm`, `scene/proof-north-road` |
| The Fire Tower | 88 | `location/foxfield-fire-tower`, `scene/proof-fire-tower` |
| The Waterfall | 88 | `location/fox-river-falls`, `scene/proof-fire-tower` |
| Events in Foxfield | 89 | `scenario/proof-of-life` (advice), сцены части «События в Фоксфилде» |
| Barnes’ Late-Night Walks | 89–90 | `scene/proof-barnes-late-night-walks` |
| The Town Meeting | 90 | `scene/proof-town-meeting`, `organization/foxfield-township-council` |
| Swing Voter Murdered | 90–91 | `scene/proof-swing-voter-murdered` |
| Follow-up | 91 | `scene/proof-swing-voter-murdered` |
| The Ike Copley-Thing | 91 | `scene/proof-ike-copley-thing`, `character/ike-copley` (вариант «Тварь-Копли») |
| Lair of the Mi-go | 91–92 | `location/mi-go-lair`, `scene/proof-lair-entrance` |
| Schemes of the Fungi | 92 | `scene/proof-lair-entrance` |
| The Sentinel | 92 | `scene/proof-lair-entrance`, `creature/mi-go-sentinel` |
| The Horror in the Hills | 92–93 | `scene/proof-mi-go-chamber` |
| Entering the Chamber | 93 | `scene/proof-mi-go-chamber`, `location/mi-go-lair` |
| The Gate | 93 | `item/mi-go-gate` |
| The Glass Tanks | 94 | `item/mi-go-glass-tanks` |
| The Metal Chest; Two More Chests | 94 | `item/mi-go-metal-chests` |
| The Brain Canister | 94 | `item/watcher-brain-cylinder` |
| The Machine | 94–95 | `item/mi-go-power-plant`, `item/mi-go-bomb` |
| Rewards and Repercussions | 95 | `scenario/proof-of-life` (conclusion, награды Рассудка) |
| NPCs and Monsters: Henry Barnes, Ike Copley, Louise Madsen, Rodney Greene, Sydney Etzler | 95 | `character/henry-barnes`, `character/ike-copley`, `character/louise-madsen`, `character/rodney-greene`, `character/sydney-etzler` |
| Shirley Sutler, Richard Slate, Dora Slate, Betty Ward, Bobby Kirtland, Aida Simpson, Typical Southern Farmer, Typical Southern Farm Wife, Peter Chylinkski | 96 | `character/shirley-sutler`, `character/richard-slate`, `character/dora-slate`, `character/betty-ward`, `character/bobby-kirtland`, `character/aida-simpson`, `character/typical-southern-farmer`, `character/typical-southern-farm-wife`, `character/peter-chylinski` |
| Typical Northern Farmer, Typical Northern Farm Wife, The Ike-Copley Thing, Mi-Go Sentinel, Mi-Go Leader, Mi-Go #2, Mi-Go #3 | 97 | `character/typical-northern-farmer`, `character/typical-northern-farm-wife`, `character/ike-copley` (вариант), `creature/mi-go-sentinel`, `creature/mi-go-leader`, `creature/mi-go-lair-workers` (варианты № 2, № 3) |
| Разворот «Catch some winks in Kingsport» | 98–99 | атмосфера → `atmosphere-proof.json` |
| Карта «Kingsport» | 100 | картинка общей записи `coc:location:kingsport` — предложение в `proposals-proof.json` (Р-249: художественная карта без номеров) |
| Proof of Life Papers #1 | 165 (копия 73) | `handout/proof-of-life-papers-1` (+ картинка) |
| Proof of Life Papers #2 | 170 (копия 77) | `handout/proof-of-life-papers-2` (+ картинка) |
| Proof of Life Papers #3 | 170 (копия 80) | `handout/proof-of-life-papers-3` (+ картинка) |
| The Pickering Mansion (план) | 189 (копия 84) | `map/pickering-mansion-map` (29 меток) |
| The Pickering Mill (план) | 190 (копия 86) | `map/pickering-mill-map` (40 меток) |
| The Old Congregates (карта) | 191 (копия 89) | `map/old-congregates-map` (8 меток) |
| The Mi-Go Cavern — The Hidden Enemy In The Hills (план) | 192 (копия 93) | `map/mi-go-cavern-map` (20 меток) |

Места по меткам карт без описания в тексте (Р-206): `location/allerton`, `location/crystal-quarry`, `location/pearson-farm`, `location/white-farm`
(с. 72, 191); `location/whipple-farm`, `location/brewster-farm`, `location/clegg-farm`, `location/sutler-farm`, `location/taggert-farm`,
`location/abbot-farm`, `location/parker-farm`, `location/poynton-farm`, `location/sawyer-farm`, `location/latham-farm`, `location/mccourt-farm`,
`location/palson-farm`, `location/three-ladies`, `location/herber-hill`, `location/the-heights`, `location/foxfield-road` (с. 72).
Подписи карты с. 72 без своей записи в базе (Мискатоник, Эйлсберийская дорога, «To Lawrence & Andover», «To Tewksbury & Lowell») ведут на
`location/foxfield` с пояснением; «To Arkham & Kingsport» — на `coc:location:arkham`.

Картинки (`art-proof.json`, применено): `item/barnes-children-brain-cylinders` (с. 82), `character/ike-copley` — Тварь-Копли (с. 92), три раздатки (с. 165, 170).
Карты — `app/maps/newtales-proof-{foxfield,pickering-mansion,pickering-mill,old-congregates,mi-go-cavern}.jpg`.

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Разворот-вид Фоксфилда | 70–71 | уже в `atmosphere-industry.json` (указание координатора) |
| Титульная полоса «Proof of Life» с фрагментом карты | 73 | оформление → `atmosphere-proof.json` |
| Иллюстрация: драка Барнса и Копли на улице | 75 | сцена предыстории, атмосфера → `atmosphere-proof.json` |
| Копии раздаток в тексте (Papers #1–3) | 73, 77, 80 | дубли приложения; взяты из приложения (с. 165, 170) |
| Копии карт в тексте (особняк, фабрика, земли конгрегантов, пещера) | 84, 86, 89, 93 | дубли приложения (с. 189–192) |
| Тёмная подложка врезки о шмыгунах | 85 | оформление без изображения существа → `atmosphere-proof.json` |
| Разворот «Catch some winks in Kingsport» | 98–99 | заставка раздела о Кингспорте → `atmosphere-proof.json` |
| Тени-рамки картинок (серые 1552×480, 744×1484 и т. п.) | 73–92 | служебные элементы вёрстки |
| Обрывки соседних колонок и реклама на вырезках раздаток | 165, 170 | к сценарию не относятся; перечислены в `quality.notes` раздаток |
| «Supervisor’s House» | 188 | не этого сценария (Dunwich — часть industry) |
| Отдельные записи Анны и Эммы Пикеринг, Артура Мэдсена, Абрахама и Руфи Уиппл, Войцеха Хылиньского, жены Айка Копли, Роберты Генри | 73–91, 165, 170 | упомянуты мимоходом; остаются текстом в описаниях соседних записей |

## Опечатки и противоречия книги

| Где | Напечатано | Что в записи |
|---|---|---|
| статблок Henry Barnes, с. 95 | Age: 33 | как напечатано; в тексте 35 (с. 74, 80) — `errata` |
| статблок Ike Copley, с. 95 | Age: 36; Move: 9 | как напечатано; в тексте «в начале седьмого десятка» (с. 88), Скорость по характеристикам — 8 — `errata` |
| статблок Ike-Copley Thing, с. 97 | Move: 7; HP 11 | как напечатано; по характеристикам Скорость 8, ПЗ 10,5 (округлено вверх — приём книг) — `errata` |
| статблок Louise Madsen, с. 95 | Age: 33 | как напечатано; в тексте «средних лет», магазин унаследовала около 20 лет назад — `errata` |
| статблок Rodney Greene, с. 95 | MP: 5 | как напечатано; по МОЩ 40 — 8 — `errata` |
| статблок Betty Ward, с. 96 | Move: 6 | как напечатано; по характеристикам 8 — `errata` |
| статблок Peter Chylinski, с. 96 | «PETER CHYLINKSKI» | исправлено на Chylinski (`errata`, fixed) |
| статблоки Typical Southern / Northern Farmer, с. 96–97 | Dodge 30% (15/5) | пятая часть исправлена на 6 (`errata` fixed + `corrections`, Р-35) |
| статблок A Typical Scuttler, с. 85 | DB: none (Build −2) | как напечатано; по сумме 10 БкУ −2 — `errata` |
| Mi-Go Sentinel: текст с. 92 / статблок с. 97 | lightning gun / Electric Gun | по статблоку (электропушка) — `errata` |
| Barnes’ Residence, с. 83 | «Aaron Peabody» | Аарон Пикеринг; «Aaron Peabody» — в `aliases` Аарона и `errata` особняка |
| Follow-ups, с. 80 | «Sydney Etlzer» | Etzler (как на с. 77, 95); отмечено в `quality.notes` |
| Proof of Life Papers #3, с. 170 | «BY WILTON KEYES» | в тексте «Wilson Keyes» (с. 79) — `errata` раздатки и персонажа |
| Proof of Life Papers #2, с. 170 | «I think I it has cobwebs» | словесная опечатка, сохранена в английском тексте |
| карта с. 72 | «Abbot» | в тексте «Abbott» (с. 82); запись «Ферма Эбботтов», `name.en` «Abbot» |

## Термины (English → русский), выбранные для этой книги

| English | Русский |
|---|---|
| Proof of Life | Доказательство жизни (сценарий); «доказательство жизни» (цилиндры) |
| Proof of Life Papers #N | Раздатка «Доказательство жизни» N |
| A Tale of Foxfield | История Фоксфилда |
| Foxfield | Фоксфилд |
| Foxfield Township | тауншип Фоксфилд |
| Township / Town Supervisor | глава тауншипа |
| Township Council | совет тауншипа |
| council member, Councilwoman | член совета |
| Town Clerk | городской секретарь |
| Town Constable | городской констебль |
| Town Coroner | городской коронер |
| county medical examiner | окружной судмедэксперт |
| town meeting | городское собрание |
| timber lease | лесная аренда (аренда) |
| Crestfield Lumber | «Крестфилд Ламбер» |
| Quigley & Sons | «Куигли и сыновья» |
| Congregates | конгреганты |
| Old Believers | староверы |
| The Old Congregates | земли конгрегантов |
| north farmers / Northern Farms | северные фермеры / северные фермы |
| Southern Farmers / Southern Farmlands | южные фермеры / южные фермы (угодья) |
| Fox River | река Фокс |
| Fox River Falls | водопад Фокс-Ривер |
| Foxfield Road | Фоксфилд-роуд |
| Aylesbury Pike | Эйлсберийская дорога (глоссарий) |
| Tewksbury; Lowell; Lawrence; Andover | Тьюксбери; Лоуэлл; Лоуренс; Андовер |
| Bolton; Bolton High School | Болтон; Болтонская старшая школа |
| Brookdale School | школа Брукдейл |
| Parker’s General Store | универсальный магазин Паркера |
| Old Man Parker | Старик Паркер |
| The Old Pickering House | старый дом Пикерингов |
| Pickering Mansion | особняк Пикерингов |
| Pickering Mill / The Old Mill / The Ruined Mill | фабрика Пикерингов / старая фабрика / сгоревшая фабрика |
| Mill Town | Милл-Таун |
| The Mill Town Squatters | дом Хылиньских (самовольные жильцы Милл-Тауна) |
| The Covered Bridge; Pickering Bridge; Foxfield Bridge | крытый мост; мост Пикеринга; Фоксфилдский мост |
| Foxfield Courier | «Фоксфилд курьер» |
| Foxfield Farm Implements & Stable | «Сельхозинвентарь Фоксфилда» и конюшня |
| The Rodney Greene Home / The Green House | дом Гринов |
| The Foxfield Unitarian Church | Фоксфилдская унитарианская церковь |
| Congregational Church | конгрегационалистская церковь |
| Schoolhouse; Schoolmarm | школа; учительница |
| The North Road | северная дорога |
| The Fire Tower; Fire Watch / watchman | пожарная вышка; пожарный смотритель / смотритель |
| Crystal Quarry | Кристальный карьер |
| “The Three Ladies” | «Три дамы» |
| Herber Hill | холм Хербер |
| The Heights | Высоты (Фоксфилда) |
| Lair of the Mi-go; The Mi-Go Cavern | логово ми-го; пещера ми-го |
| The Horror in the Hills; The Hidden Enemy In The Hills | ужас в холмах; тайный враг в холмах |
| Fungi from Yuggoth | Грибы с Юггота (глоссарий) |
| Mi-Go Leader | предводительница ми-го |
| Mi-Go Sentinel | часовой ми-го |
| Scuttler(s) | шмыгун(ы) |
| Jump and Grab | прыжок с захватом |
| Nippers | клешни |
| Seize (mnvr) | Схватить (манёвр) (глоссарий) |
| brain canister | мозговой цилиндр (глоссарий: brain cylinder) |
| Watcher | «Смотритель» (бирка цилиндра) |
| Mi-go key / stone key | каменный ключ ми-го |
| The Gate | Врата (глоссарий) |
| The Glass Tanks | стеклянные баки |
| The Metal Chest | металлический сундук |
| The Machine / The Power Plant | машина ми-го (энергоустановка) |
| bomb | бомба ми-го |
| Electric Gun; lightning gun | электропушка; молниемёт (глоссарий) |
| The Ike Copley-Thing | Тварь-Копли |
| Swing Voter Murdered | убийство Ширли Сатлер (решающий голос) |
| Rewards and Repercussions | итог и награды |
| Know roll | проверка Знаний (глоссарий) |
| Hard / Extreme roll | трудная / чрезвычайная проверка |
| youth at risk | трудный подросток |
| Old Believer (Ike Copley) | старовер |
| Henry Barnes; Helen Barnes (Brock); Mary; Robert | Генри Барнс; Хелен Барнс (Брок); Мэри; Роберт |
| Sarah Brock (Aunt Sarah) | Сара Брок (тётя Сара) |
| Ike Copley; Zeke Copley | Айк Копли; Зик Копли |
| Louise Madsen; Arthur Madsen | Луиза Мэдсен; Артур Мэдсен |
| Rodney Greene; Ida Greene | Родни Грин; Ида Грин |
| Sydney (Syd) Etzler | Сидни (Сид) Этцлер |
| Shirley Sutler | Ширли Сатлер |
| Richard Slate; Dora Slate | Ричард Слейт; Дора Слейт |
| Betty Ward; Bobby Kirtland | Бетти Уорд; Бобби Кертленд |
| Aida Simpson | Аида Симпсон |
| Rose, Peter, Wojciech Chylinski | Роуз Хылиньская, Питер Хылиньский, Войцех Хылиньский |
| Elias Whipple; Abraham and Ruth Whipple | Элайас Уиппл; Абрахам и Руфь Уиппл |
| Wilson (Wilton) Keyes | Уилсон (Уилтон) Киз |
| Aaron, Anne, Bertrand, Emma, James Pickering | Аарон, Анна, Бертран, Эмма, Джеймс Пикеринг |
| Graham Tolliver | Грэм Толливер |
| Roberta Henry | Роберта Генри |
| Bernard Evans, Optometrist (реклама на вырезке) | оптик Бернард Эванс |
| John Muir; Sierra Club | Джон Мьюир; «Сьерра-клуб» |
| Allerton, Brewster, Clegg, Pearson, White, Sutler, Taggert, Abbot(t), Parker, Poynton, Sawyer, Latham, McCourt, Palson | фермы Аллертон, Брюстеров, Клеггов, Пирсонов, Уайтов, Сатлеров, Таггертов, Эбботтов, Паркеров, Пойнтонов, Сойеров, Лэтемов, Маккортов, Палсонов |
