# «Маски Ньярлатхотепа», часть england-2: глава 3 «Англия», с. 227–294

Этап `masks-of-nyarlathotep-en/scenario/england` (england-1) — шаги, заключение и таблица наград этой половины предложены в
`proposals-england-2.json`. Побочный сценарий «Ужас Дербишира» — `scenario/england-derbyshire-horror` (part_of — этап, order 2).
Префиксы id ниже: `S:` = `masks-of-nyarlathotep-en/scene/england-`, `L:` = `…/location/england-`, `I:` = `…/item/england-`,
`H:` = `…/handout/england-carlyle-papers-`, `O:` = `…/organization/england-`, `M:` = `…/map/england-`, `C:` = `…/character/`.
Сцены «Ужаса Дербишира» — `S:derbyshire-…` (arc.scenario — побочный сценарий), остальные — arc.scenario = этап, order 22–45.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Sidetrack Scenario: The Derbyshire Horror (ссылки, вступление) | 227 | `scenario/england-derbyshire-horror`: summary, hook |
| Mad Dogs | 228 | сценарий: keeper_info |
| Keeper Considerations | 228 | сценарий: advice |
| Dramatis Personae: Derbyshire Horror (Tumwell, Stratton) | 228–229 | персонажи уже в базе (`C:hubert-tumwell`, `C:jeremy-stratton`); `O:order-of-the-golden-druid` |
| The Vane Family (Lord Arthur, Lawrence, Eloise) | 229–230 | персонажи уже в базе (`C:arthur-vane`, `C:lawrence-vane`, `C:eloise-vane`); сценарий: keeper_info (распорядок полнолуния) |
| Other Villagers | 229 | сценарий: таблица «Ужас Дербишира: другие селяне»; `C:edith-osgood`, `C:john-parkins`, `C:ernest-wallop`, `C:maddy-albright`, `C:alice-pitchlock`, `C:john-pitchlock` |
| What’s in a Vane? (врезка) | 229 | сценарий: keeper_info |
| Getting to Lesser Edale | 231 | сценарий: hook; `L:lesser-edale` |
| Lesser Edale (+ план) | 231 | `L:lesser-edale`; `M:lesser-edale` |
| Initial Research | 232 | `S:derbyshire-laughing-horse` |
| Laughing Horse Inn (+ сплетни) | 232 | `L:laughing-horse-inn`, таблица «„Смеющаяся лошадь“: слухи»; `C:bill-tatlock` |
| Pitchlock General Store | 233 | `L:pitchlock-general-store` |
| Meeting Constable Tumwell | 233 | `S:derbyshire-meeting-tumwell`; `L:tumwell-house` |
| Interviewing the Victims’ Families; Osgood Farm; Parkins’ House | 233–234 | `S:derbyshire-victims-families`; `L:osgood-farm`, `L:parkins-house` |
| Asking About Harold Short | 234 | `S:derbyshire-victims-families`; `C:harold-short` |
| Further Inquiries | 234 | arc.part «Дальнейшие расспросы» |
| The Vicar of Lesser Edale; Exploring the Church Grounds; Meeting Reverend Stratton | 235–236 | `S:derbyshire-vicar`; `L:lesser-edale-church`; `C:sarah-bright`, `C:jed-wainwright` |
| Carlyle Papers England #9 | 235 | `H:9` (официальный русский текст) |
| The Journal (врезка) | 236 | `I:old-vicar-journal` |
| Tracking the Beast | 236 | `S:derbyshire-tracking-the-beast`; `I:torn-lace-scrap` |
| Asking About the Vanes | 236 | `L:lesser-edale`, таблица «Малый Эдейл: что известно о Вейнах» |
| Further Research on the Vanes, History, and Folklore | 236–237 | `L:lesser-edale`, таблица «Малый Эдейл: история и фольклор» |
| Keeper note: старые свинцовые рудники | 237 | `L:lesser-edale`: description |
| Truth Stranger than Fiction? (врезка) | 237 | `S:derbyshire-tracking-the-beast` |
| Local Sites of Interest: Mam Tor; Blue John Cavern | 238 | `L:mam-tor`, `L:blue-john-cavern` |
| The Curse of the Vanes | 239 | сценарий: keeper_info |
| A Visit to Plum Castle | 239 | `S:derbyshire-plum-castle-visit`; `L:plum-castle` |
| The Servants | 240 | `L:plum-castle`: description; `S:derbyshire-plum-castle-visit` |
| In Conversation with the Vanes; Dinner at Plum Castle (врезка) | 240 | `S:derbyshire-plum-castle-visit` |
| Lawrence Asks for Help | 241 | `S:derbyshire-lawrence-asks-for-help` |
| Meeting Eloise Vane | 241 | `S:derbyshire-meeting-eloise` |
| Key Locations in Plum Castle; Great Hall | 241 | `L:plum-castle` |
| The Library | 241, 243 | `L:plum-castle-library`; `I:edgar-vane-journal` |
| Map of Plum Castle | 242 | `M:plum-castle`; ключ 1–25 — quality.notes `L:plum-castle` |
| Vane Mausoleum | 243 | `L:vane-mausoleum` |
| The Dungeon | 243 | `L:plum-castle-dungeon` |
| Investigator Options; Using Stealth; Confronting the Vanes | 243–244 | `S:derbyshire-investigator-options` |
| Eloise Escapes; Eloise at Large | 244 | `S:derbyshire-eloise-escapes` |
| Pulp Option (стая упырей); Possible Outcomes; We Need Silver Bullets! | 245 | `S:derbyshire-eloise-escapes` |
| Conclusion | 245 | сценарий: conclusion |
| Rewards; Pulp Rewards | 246 | сценарий: conclusion, таблица «Ужас Дербишира: награды» |
| Characters and Monsters: The Derbyshire Monster (Tumwell, Stratton, Average Townsfolk, Vanes, Eloise in Ghoul Form, Pulp Combat/Talents) | 246–249 | уже в базе: `C:hubert-tumwell`, `C:jeremy-stratton`, `C:lesser-edale-townsfolk`, `C:arthur-vane`, `C:lawrence-vane`, `C:eloise-vane` (ничего нового) |
| Pulp Option: Ghoul Pack (профиль) | 249 | уже в базе: `…/creature/ghoul-masks`; ссылка из `S:derbyshire-eloise-escapes` |
| Slaughter in Soho; Murder! | 250 | `S:inspector-barrington` (arc.part «Резня в Сохо») |
| Inspector Barrington of the Yard | 250 | `S:inspector-barrington`; `L:new-scotland-yard` |
| London Police (врезка) | 250 | `O:metropolitan-police` |
| Leads Possessed by Inspector Barrington; What Barrington says about Jackson Elias / about the murders; Clues Barrington is prepared to share | 251 | `S:inspector-barrington` |
| The Truth Behind the Murders; Following Up Barrington’s Leads | 251 | `S:inspector-barrington`; `C:gregory-munden`, `C:badru` |
| Map of the Blue Pyramid Club (with Soho inset) | 252 | `M:blue-pyramid-club`; ключ — quality.notes `L:blue-pyramid-club` |
| The Blue Pyramid Club | 253 | `L:blue-pyramid-club` (пункт 18 карты Лондона) |
| Visiting the Blue Pyramid Club | 253 | `S:blue-pyramid-visit` |
| Asking Questions | 254 | `S:blue-pyramid-visit` |
| Meeting Yalesha Essam; Pulp: Direct Action | 255 | `S:meeting-yalesha` |
| Stakeout: Blue Pyramid Club | 255 | `S:blue-pyramid-stakeout` |
| Empire Spices (+ план) | 256 | `L:empire-spices`; `M:empire-spices` |
| Talking to Zahra Shafik; What Shafik Says | 257 | `S:talking-to-shafik` |
| Empire Spices: Key Locations; Ground Floor Rooms | 257 | `L:empire-spices` |
| Zahra Shafik’s Apartment | 257 | `L:empire-spices-apartment` |
| Shafik’s Artifacts: Mirror of Gal; Sandstone Vials; Robe, Skullcap, and Metal Ankh; Scroll; Two Scepters | 258 | уже в базе `…/item/campaign-mirror-of-gal` (с флаконами) и `…/item/campaign-two-scepters`; `I:shafik-regalia`, `I:mirror-of-gal-scroll` (флаконы — в mechanics) |
| The Cellar | 258 | `L:empire-spices-cellar`; `I:shafik-black-pharaoh-idol`, `I:ceremonial-clubs` |
| Nitocris in London (врезка) | 258 | `S:empire-spices-search` |
| The Schemes of Zahra Shafik | 259 | `S:shafik-schemes` |
| An Important Meeting; Conversation topics; Pulp: Exhibition | 260 | `S:important-meeting`; `L:british-empire-exhibition` |
| Captured by Shafik | 260 | `S:captured-by-shafik` |
| British Empire Exhibition; Exhibition Overview; Campaign Foreshadowing | 261 | `L:british-empire-exhibition`, таблица «Британская имперская выставка: видения во „Дворце красоты Пирс“» |
| Machinations of the Brotherhood | 262 | `S:finding-henson` (arc.part «Происки Братства») |
| Henson Manufacturing (Derby) | 262 | `O:henson-manufacturing`; `L:henson-manufacturing` |
| Finding the Workshop; If Following Gavigan | 262–264 | `S:finding-henson` |
| Map of Henson Manufacturing (with Derby inset) | 263 | `M:henson-manufacturing`; ключ 1–16 — quality.notes `L:henson-manufacturing` |
| If Researching the Company from Paperwork; Asking the Locals | 264 | `S:finding-henson` |
| About Derby | 264 | `L:derby` |
| Inside Henson Manufacturing; Main Workshop | 264 | `L:henson-manufacturing`, `L:henson-workshop`; `S:henson-break-in` |
| The Components (врезка) | 265 | `I:rocket-components` |
| Сейф, наклейка Randolph Shipping | 266 | `L:henson-workshop`; `I:rocket-components` |
| Pulp: Weird Science; Pulp: Weird Science II | 266, 268 | `I:rocket-components`: mechanics; `S:last-shipment` |
| The Big Shed and Furnace; Wooden Shed | 266 | `L:henson-manufacturing` |
| Carlyle Papers England #10 | 266 | `H:10` (официальный русский текст) |
| The Engineers and their Guards | 266 | `L:henson-manufacturing`; `O:henson-manufacturing` |
| Cult Guards and Foreman; Frank Marshall; The Workers; Henson Manufacturing Workers | 267 | `S:henson-altercations`; персонажи уже в базе (`C:frank-marshall`, `C:henson-manufacturing-employees`) |
| Altercations and Events | 267–268 | `S:henson-altercations` |
| The Last Shipment; Concluding Henson Manufacturing | 268–269 | `S:last-shipment`; `I:rocket-components` |
| Misr House (ссылки, вступление) | 269 | `L:misr-house`; `S:researching-misr-house` |
| Researching Misr House | 269 | `S:researching-misr-house`; `C:neville-lloyd-price` |
| Map of Walton-on-the-Naze with Misr House inset | 270 | `M:misr-house`; ключ — quality.notes `L:misr-house` |
| About Walton-on-the-Naze; Getting to Misr House | 271 | `L:the-naze`; `S:getting-to-misr-house` |
| If Following the Cultists from London | 271 | `S:getting-to-misr-house` |
| The Naze Tower (врезка) | 271 | `L:naze-tower` |
| Entrances to the Estate; The Island Estate | 272 | `L:misr-house`; `S:getting-to-misr-house` |
| The Manor House; Inside the Manor House | 272 | `L:misr-house` |
| Great Hall | 272–273 | `L:misr-house-great-hall` |
| Gavigan’s Servants (врезка) | 273 | `L:misr-house`; `I:high-priest-robes` |
| Master Bedroom; Headdress of eyes; Painting of the Black Pharaoh; Wall clock; Letter | 273 | `L:misr-house-master-bedroom`; уже в базе `…/item/campaign-headdress-of-eyes`, `…/item/campaign-marine-chronometers`; `I:black-pharaoh-painting` |
| Carlyle Papers England #11 | 274 | `H:11` (официальный русский текст) |
| High priest robes | 275 | `I:high-priest-robes` |
| Secret Workroom and Dungeon; Secret Workroom (Torture devices, Wall hook, Desk) | 275 | `L:misr-house-secret-workroom`; `I:gavigan-ledger` |
| Carlyle Papers England #12, #13 | 275–276 | `H:12`, `H:13` (официальный русский текст) |
| Statuary; Two scepters; Books and scrolls (Song of the Djinn, Quicken Fog-Spawn); Spell Components | 276–277 | `I:misr-house-statuary`, `…/item/campaign-two-scepters`, `I:misr-house-occult-library`, `I:spell-components`; копия «Песни джина» — предложение для `coc:tome:song-of-the-djinn` |
| Shelves (растения, личинки) | 277 | `I:strange-plants`, `I:fog-spawn-larvae` |
| Pulp: Fog-spawn Larvae and Strange Plants | 277 | `I:fog-spawn-larvae`, `I:strange-plants` |
| The Dungeon (Misr House) | 277 | `L:misr-house-dungeon`; `I:munden-warrant-card` |
| Rites of the Brotherhood; стела | 278 | `L:misr-house-ritual-clearing`; `S:lesser-rite` |
| Torture (врезка) | 278 | `S:torture` |
| Lesser Rites | 278–279 | `S:lesser-rite` |
| Grand Rites (6 частей); Pulp: Rites | 279 | `S:grand-rite` |
| Constructing a Climax; Pulp: Epic Climax | 280 | `S:infiltrating-the-rites`; предложение для advice этапа |
| Infiltrating the Rites | 280 | `S:infiltrating-the-rites` |
| All-Out Assault | 282 | `S:all-out-assault` |
| Going to the Authorities | 282 | `S:going-to-the-authorities` |
| Zahra Shafik at the Rite | 282–283 | `S:shafik-at-the-rite` |
| Anything Else? | 283 | `S:all-out-assault` |
| Aftermath | 283 | `S:aftermath` |
| Conclusion | 283 | предложение: conclusion этапа |
| Rewards; Pulp: Rewards | 284 | предложение: таблица этапа «Англия: награды» |
| Characters and Monsters: England (Mahoney, Barrington, Steadfast Constables, Jasmine Pink, Pulp: John Craig, Bigger/Average Cultists, Gavigan, Kinnery, Shafik, Edjo, Nawisha, Bouncers, Yalesha, Chaudhary, Lascars, Torvak, Sailors, Marshall, Henson Employees) | 284–291 | уже в базе (записи персонажей england; ничего нового) |
| Monsters: Fog-spawn; Hunting Horror; Million Favored Ones: The Dead; Shantak | 291–293 | уже в базе: `…/creature/fog-spawn`, `coc:creature:hunting-horror` (профиль = средний; предложение — источник «Масок»), `…/creature/million-favored-ones-the-dead-masks`, `…/creature/shantak-masks` |

## Строки аудита `checks/20261025-masks/not_in_kb.md` на с. 227–294

| Строка аудита | Стр. (физ./печ.) | Где теперь |
|---|---|---|
| Hunting Horror — профиль вида в книге | 295/292 | профиль совпадает со средними значениями `coc:creature:hunting-horror` — предложение добавить источник «Масок» (отдельная запись не нужна) |
| Rewards: награды по главам (249/246, 287/284) | 249/246, 287/284 | `scenario/england-derbyshire-horror`: таблица наград; этап «Англия» — предложение conclusion и таблицы «Англия: награды» |
| Слухи в Лессер-Эдейле (Laughing Horse Inn) | 235–236/232–233 | `L:laughing-horse-inn`, таблица «„Смеющаяся лошадь“: слухи» |
| Sandstone Vials (obra’an, gabeshgal) | 261/258 | уже в `…/item/campaign-mirror-of-gal` (псевдоним, mechanics); здесь — `I:mirror-of-gal-scroll` (mechanics) |
| Marine Chronometers (Misr House) | 276/273 | `…/item/campaign-marine-chronometers` — предложение found_at = `L:misr-house-master-bedroom`; описан в `L:misr-house-master-bedroom` |
| Детали ракеты на Henson Manufacturing | 268/265, 271/268 | `I:rocket-components` (записи ракеты сэра Обри пока нет — часть china) |
| England #9–#13 | 238–279/235–276 | `H:9` … `H:13` (официальный русский текст) |
| Карты: Lesser Edale, Plum Castle, Blue Pyramid Club, Empire Spices, Henson Manufacturing, Misr House | 234, 245, 255, 259, 266, 273 (физ.) | `M:lesser-edale`, `M:plum-castle`, `M:blue-pyramid-club`, `M:empire-spices`, `M:henson-manufacturing`, `M:misr-house` |
| Lesser Edale (Laughing Horse Inn, Pitchlock General Store, дом викария) | 234–238/231–235 | `L:lesser-edale` (область) + `L:laughing-horse-inn`, `L:pitchlock-general-store`, `L:lesser-edale-church`, `L:tumwell-house`, `L:osgood-farm`, `L:parkins-house` |
| Mam Tor, Blue John Cavern | 241/238 | `L:mam-tor`, `L:blue-john-cavern` |
| Plum Castle (Key Locations) | 242–247/239–244 | `L:plum-castle` + `L:plum-castle-library`, `L:vane-mausoleum`, `L:plum-castle-dungeon` |
| Soho / Blue Pyramid Club | 256/253 | `L:blue-pyramid-club` (part_of `L:soho`) |
| Empire Spices | 259/256 | `L:empire-spices` + `L:empire-spices-apartment`, `L:empire-spices-cellar` (part_of `L:soho`) |
| Henson Manufacturing (Derby) | 265–271/262–268 | `L:derby` (область), `L:henson-manufacturing`, `L:henson-workshop`; организация `O:henson-manufacturing` |
| Misr House, Naze Tower, Walton-on-the-Naze | 272–280/269–277 | `L:the-naze` (область, с Уолтоном), `L:naze-tower`, `L:misr-house` + `L:misr-house-great-hall`, `-master-bedroom`, `-secret-workroom`, `-dungeon`, `-ritual-clearing` |
| Scotland Yard / London Police | 253/250 | `L:new-scotland-yard`; `O:metropolitan-police` |
| British Empire Exhibition | 264/261 | `L:british-empire-exhibition` (место, с таблицей видений) |
| Организации: Henson Manufacturing, Empire Spices, Blue Pyramid Club | 265, 259, 256 | `O:henson-manufacturing`; лавка и клуб — места (`L:empire-spices`, `L:blue-pyramid-club`), не организации: оба — прикрытие Братства (`O:brotherhood-of-the-black-pharaoh`, предложение based_at) |
| Полиция: London Police / Scotland Yard | 253/250 | `O:metropolitan-police` |
| Bakewell Witches | 239/236, 244/241 | текст: сценарий (keeper_info), таблица «Малый Эдейл: история и фольклор», `I:old-vicar-journal`; отдельной записи нет (историческая группа без механики) |
| Inspector Gregory Munden | 253/250, 280/277 | `C:gregory-munden`; `I:munden-warrant-card` |
| Badru | 190/187, 258/255 | `C:badru` |
| Neville Lloyd-Price | 272/269 | `C:neville-lloyd-price` |
| Жители Лессер-Эдейла: Bill Tatlock, Harold Short, Lydia и John Parkins, George и Edith Osgood, Sarah Bright, Jed Wainwright, Maddy Albright, Tom Corty | 232–238/229–235 | `C:bill-tatlock`, `C:harold-short`, `C:john-parkins`, `C:edith-osgood`, `C:sarah-bright`, `C:jed-wainwright`, `C:maddy-albright` (+ `C:ernest-wallop`, `C:alice-pitchlock`, `C:john-pitchlock`); убитые Лидия и Джордж, Том Корти — текст |
| Mrs. Joyce Bullrush | 269/266 | текст в `O:henson-manufacturing` (одна фраза) |
| Пульп-врезки Weird Science (I, II) | 269/266, 271/268 | `I:rocket-components`: mechanics; `S:henson-break-in`, `S:last-shipment` |
| Нитокрис в Лондоне | 261/258 | `S:empire-spices-search` (ссылка на `C:sharifa-rawash`) |
| Rites of the Brotherhood: Torture, Lesser Rites, Grand Rites | 281–282/278–279 | `S:torture`, `S:lesser-rite`, `S:grand-rite`; `L:misr-house-ritual-clearing` |
| Sidetrack: The Derbyshire Horror | 230–249/227–246 | `scenario/england-derbyshire-horror` + 10 сцен, 13 мест, 3 предмета, `H:9`, 10 персонажей, организация |
| Conclusion разделы глав (Aftermath) | 286/283 | `S:aftermath`; conclusion этапа — предложение |
| Constructing a Climax (England) | 283/280 | `S:infiltrating-the-rites` (+ `S:all-out-assault`, `S:going-to-the-authorities`, `S:shafik-at-the-rite`); абзац в advice этапа — предложение |

## Не взято

| Что | Стр. | Почему |
|---|---|---|
| Иллюстрации: Элоиза в пещере Синего Джона, вывеска «Смеющейся лошади», церковь, холмы Дербишира, Мам-Тор, жила синего Джона, клуб «Синяя пирамида», артефакты Шафик, детали «Хэнсона», головной убор из глаз, обряд у стелы, охотящийся ужас, шантак; полностраничный арт с. 294 | разные | Арт без данных; картинки не переносились (Р-165 — по решению владельца) |
| Изображения раздаток Англия 9–13 | 235, 266, 274–276 | Текст перенесён; картинки в `images` не добавлялись (как в england-1) |
| Персонажи без записей: Нед Лоутон и его жена Марджи, Том Корти, Томас Шорт (брат Гарольда), слуга Джайлс, дочери Осгудов Мэгги и Рейчел, убитые Джордж Осгуд и Лидия Перкинс, леди Эванджелина Вейн, Энни Стаффорд и Дженни Грин, Эдгар Вейн, Веллингтон Вейн, Джеффри Лайонс, лорд Джошуа Вейн и Эбнер Вейн Карел, Лестер Иллингворт, лорд Малгрейв, призрак Мэйбл, Артур Хэнсон, миссис Джойс Буллраш, три пленника-лондонца в темнице Миср-хауса | разные | Упомянуты одной-двумя фразами, без профиля и роли в игре; оставлены текстом в сценах, местах и предметах — кандидаты в записи персонажей |
| Места без записей: дом Гарольда Шорта (2), ветеринарная клиника (7), Арбор-Лоу и «Девять дев», Скегнесс, Бейкуэлл, Эдейл, гостиницы «Старый колокол» и «Джорджиан-Хаус», Регистрационная палата компаний, архив совета Челмсфорда, Колчестер, «Марин-отель», Данвич, Харвич, дом охранников «Хэнсона», «Мавританское кафе» и «Алжирец» | разные | Одна фраза в книге, без сцены; текст в записях мест и сцен |
| Ракета сэра Обри, Город Великой Расы, система наведения | 262, 265, 268 | Описаны в главах «Китай» и «Австралия» (части china-2, australia); здесь — текст и `I:rocket-components` |
| Опечатка плана Миср-хауса «Second Floor Floor», «Gavigan’s Bedrom» | 270 | Мелкое оформление (Р-39) |

## Сомнения и опечатки книги (в errata)

1. Фамилия второй жертвы: «Lydia Perkins» (с. 232, 233, 235) против «Lydia Parkins»/«John Parkins» (с. 229, 233); официальная раздатка Англия 2 — «Лидия Перкинс» — errata у `L:parkins-house`.
2. План Малого Эдейла (с. 231): дом Паркинсов дважды — 4 «Parkins’ House» и 8 «John Parkin’s House» (на русском плане пункта 8 нет) — errata у `L:parkins-house`.
3. «Хэнсон»: дорога «Uttoxeter Road» (текст, с. 264) против «Albany Road» (английский план, с. 263); русский план — «Уттокстерская дорога» — errata у `L:henson-manufacturing`, пометка на `M:henson-manufacturing`.
4. Миср-хаус: «построен в XVI веке при Елизавете I» (с. 269) против «фундамент особняка XVII века» (с. 272) — errata у `L:misr-house`.
5. Потеря Рассудка за Миллион избранных: 0/1d8 в Большом обряде (с. 279) против 0/1d6 в профиле (с. 292) — errata у `S:grand-rite`.
6. Раздатка Англия 12: в русской версии нет «(6 feet)» у статуи, «Astronomical charts» → «Астрологические таблицы», «Huston» → «Хастон» — пометка в quality.notes `H:12` (официальный текст оставлен как есть).
7. Раздатка Англия 11: скан официального текста размыт («бюсти» → «бюста» по английскому «the bust»); Англия 13 — «поимку» по смыслу (в рукописи неразборчиво) — пометки в quality.notes.

## Ссылки на записи других частей

Все ссылки этой части указывают на существующие записи (`python -B tools/check.py` по 109 файлам — 0 ошибок в своих файлах).
Ссылок на будущие записи других частей нет: ракета сэра Обри, «Перевозки Рэндольфа», дом аль-Шакти оставлены текстом.

## Вопросы ведущему

1. Места вне общего города — Малый Эдейл, Дерби, Нейз — сделаны вершинами вида `область` с `part_of` = Лондон (как в Перу); деревню можно было бы оформить и как `место`.
2. Официальные названия: «Миср-хаус» (план «Материалов для игроков») против «Миср-Хаус» в записях england-1; «Малый Эдейл», «Синяя пирамида», «Имперские специи», «Хэнсон» против «Лессер-Эйдейл», «Голубая пирамида», «Эмпайр Спайсиз», «Хенсон Мэньюфекчуринг» в записях персонажей — предложены только residence и псевдонимы; тексты персонажей не правились.
3. Новые персонажи (13) созданы без префикса главы по указанию ведущего, хотя задание отдаёт части только файлы `*/england-*`.
