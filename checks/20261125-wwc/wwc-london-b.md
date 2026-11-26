# World War Cthulhu: London — сторона Хранителя (часть «london-b»)

Книга `wwc-london-en` (Cubicle 7, 2016; 7-я редакция, хотя метка библиотеки — [EN 6e]). Часть london-b — с. 79–192: глава
«Mythos Horrors», «Battles on the Home Front», три сценария («Midnight Sunrise», «Captive Audience», «The Meat Trade»),
«Fortean Events in Wartime London» и указатель. Работа начата одним помощником (прерван лимитом 2026-11-25: «Ужасы Мифов»,
«Полуночный восход», фортеанские события, первая половина «Пленённой публики») и закончена вторым (2026-11-26).

Страницы: печатная = физической (смещение **0**, как у части london-a; сверено по изображениям с. 156, 157 и по номерам в
текстовом слое на всех страницах 79–189). Русского перевода книги в базе и библиотеке нет (поиск имён и мест сценариев —
Грейвс, Франклин, Даггет, Шепард, Фтаггуа, «Пикадилли» — в `kb/books/*-ru/` пуст); русский текст — наш перевод
(`translated`). Эпоха — `1940s-1980s` (Лондон 1940–1941, по общей схеме линейки; сказано в `quality.notes`), свод — `core`.

## Записи

303 записи в `kb/books/wwc-london-en/` (`python tools/check.py` по ним — 0 ошибок, 0 предупреждений): `character` 91,
`location` 68, `scene` 64, `item` 25, `handout` 19, `creature` 11, `organization` 8, `rule` 8, `map` 4, `scenario` 3, `tome` 2.
Из них 210 записал первый помощник (списки `written-mh-*`, `written-ms-*`, `written-ca-part1`), 93 — второй (`written-ca-part2`,
`written-mt`, `written-maps`); второй помощник ещё дописал ссылки на карты (11 записей), исходы и участников 5 сцен
«Полуночного восхода», «Пленённой публики» и «Мясной торговли» по `scenario_check`.

- «Ужасы Мифов» (с. 79–104): 7 правил (`mythos-in-wartime-london`, `rise-of-the-ghouls`, `renewed-call-of-cthulhu`,
  `buried-temples-and-forgotten-horrors`, `artefacts-and-tomes`, `deep-ones-in-the-thames`, `battles-on-the-home-front`),
  организации Крысоловы, Жнецы, Храм восставшего Р’льеха, Море разумов, Змеелюди Балхэма; персонажи, существа, предметы, места
  разделов (таблица ниже).
- «Полуночный восход» (с. 105–134): сценарий + 23 сцены, 6 раздаток, книга Мифов, карта склада «Уильямс шиппинг».
- «Пленённая публика» (с. 135–169): сценарий + 26 сцен, 12 раздаток, 23 персонажа, Призрак истины, 3 карты (Сент-Джеймс-холл,
  отель «Пикадилли», Ганновер-террас).
- «Мясная торговля» (с. 170–185): сценарий + 15 сцен, 27 персонажей (в том числе 5 упырей в чужом облике — `instance_of`
  `coc:creature:ghoul`), 2 существа, банда Шепарда и упыри кладбища Боу, 12 мест, 7 предметов, книга «Записи Даггет», раздатка.
- «Фортеанские события» (с. 186–189): правило `fortean-events-in-wartime-london`, места `st-james-garlickhythe`,
  `cleopatras-needle`, `clarence-house`, `pond-square`, `hall-place`, рассказчик Джим Такер.
- Сверки: `checks/20261125-wwc/completeness-london-b/`, `checks/20261125-wwc/scenario-london-b/` — остались только находки
  [low]: сцены-поиски в библиотеке без места и участников (по книге их нет) и картинки-фоны (см. «Не взято»).

Черновики и предложения:

- `checks/20261125-wwc/new-shared-spells-london-b.json` — 8 черновиков общих заклинаний (`tools/validate.py` — 0 ошибок):
  `coc:spell:anchor-of-dreams` (Якорь снов, с. 87), `gifts-of-the-deep` (Дары глубин, с. 88), `echo-of-the-past` (Эхо прошлого,
  с. 142), `enchant-sacrificial-blade` (Зачаровать жертвенный клинок, с. 142–143), `summoning-circle` (Круг призыва, с. 143),
  `create-fire-vampire` (Создание огненного вампира, с. 109–110), `fire-walk` (Огненный путь, с. 110), `pyromancy`
  (Пиромантия, с. 110). После переноса — поставить ссылки `spell` у Джойс Мерчант, Лайонела Дауни, Тейлора Грейвса, Авроры
  Уильямс, слуг Уильямс и в списке «Книги всех запретных искусств» (сейчас `spell: null`). «Call/Dismiss Fthaggua» и «Contact
  Fthaggua» книга только называет — черновиков нет.
- `checks/20261125-wwc/proposals-london-b.json` — 15 правок (пробный прогон `apply.py` — ложатся все):
  `wwc-covert-actions-en/location/bow-cemetery` — кладбище Боу встретилось во второй книге линейки: псевдонимы «Tower Hamlets
  Cemetery», история 1941 года, источники с. 171, 182, ссылки на логово, племя, мистера Блэка и сцену; по Р-154 запись стоит
  перенести в общие места (решение ведущего); экземпляры книг (Р-65): `coc:tome:true-magick` (кабинет Грейвса),
  `coc:tome:cultes-des-goules` (кабинет Грейвса; стол Даггет), `coc:tome:de-vermiis-mysteriis`, `coc:tome:nameless-cults`
  (кабинет Грейвса), `coc:tome:king-in-yellow` (экземпляр Британской библиотеки на «Олдвиче»).
- Навыки «Гражданская оборона» и «Смекалка и починка» в статблоках и сценах — черновики части london-a
  (`coc:skill:civil-defence`, `coc:skill:make-do-and-mend`); ссылок нет до их переноса.

Картинки и карты:

- 4 карты `map` (картинки `app/maps/wwc-london-b-*.jpg`, 1400 px, метки на каждой напечатанной подписи, Р-206):
  `map/williams-shipping-warehouse` (с. 133), `map/st-jamess-hall-plans` (с. 156, раздатка 10),
  `map/piccadilly-hotel-plans` (с. 157, раздатка 11; номера — на 8 помещений-записей), `map/hanover-terrace`
  (с. 160). Координаты — по сетке 5% на глаз (±1%); владельцу стоит проверить в просмотрщике.
- 45 картинок записей — `checks/20261125-wwc/art-london-b.json` → `art-london-b-proposals.json`, копии `app/art/*/wwc-london-b-*.webp`;
  предложения применены к своим записям (`apply.py` — 45 правок, 0 ошибок): 32 портрета, 6 артов существ и предметов (Каррагаш,
  Спот, Призрак истины, зонд змеелюдей, «Акулья вырезка», «Король в жёлтом»), 2 раздатки-плана, 5 иллюстраций с узнаваемым
  героем или местом (Тереза Хьюз, дворецкий Браун, Мартер на платформе, воронка «Нечто в яме», фургон «Уилсона»).
  Сомнение: у Марка Лонга на портрете усы, а текст — «clean-shaven»; у Эллиотта нет очков («clean spectacles»): портреты стоят
  под их именами (с. 140, 144), взяты.
- Атмосфера и оформление — `checks/20261125-wwc/atmosphere-london-b.json` (54 картинки: заставки глав, сцены без своей записи,
  фоны врезок, раздаток и статблоков, эмблема).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Mythos Horrors; The Mythos in Wartime London | 79 | `rule/mythos-in-wartime-london` |
| The Rise of the Ghouls: The Aftermath of the 1920s; The Rat Catchers in the 1940s | 79–80 | `rule/rise-of-the-ghouls`, `organization/rat-catchers` |
| Joining the Rat Catchers | 80 | `rule/rise-of-the-ghouls`, `organization/rat-catchers` |
| The Ointment of True Seeing (врезка) | 81 | `item/ointment-of-true-seeing`, `character/ernest-glover` |
| Kenneth Hodge; Nancy Wain (статблоки) | 81–83 | `character/kenneth-hodge`, `character/nancy-wain` |
| Karragash, Ghoul Sorcerer | 83 | `creature/karragash` |
| Modern Turf Wars; Underground Stations and Bomb Shelters as Hunting Grounds | 84 | `rule/rise-of-the-ghouls`, `creature/karragash` |
| The Renewed Call of Cthulhu | 84 | `rule/renewed-call-of-cthulhu` |
| The Harvesters; Joyce Merchant; New Spell: Anchor of Dreams | 85–87 | `organization/harvesters`, `character/joyce-merchant`; черновик `coc:spell:anchor-of-dreams` |
| The Temple of R’lyeh Risen; Lionel Downey; New Spell: Gifts of the Deep | 86–88 | `organization/temple-of-rlyeh-risen`, `character/lionel-downey`, `character/maria-francis`, `location/forest-hill-pools`, `location/st-james-boys-orphanage`; черновик `coc:spell:gifts-of-the-deep` |
| Transformed Cthulhu Cultist; Transformations (таблица) | 88–89 | `character/transformed-cthulhu-cultists` |
| The Sea of Minds; Lydia Gardner | 89–91 | `organization/sea-of-minds`, `character/lydia-gardner`, `character/annie-noonan`, `character/janice-mullings`, `character/samuel-wildman`, `character/reverend-foreman`, `location/gardner-flat`, `location/stepney-green-station`, `location/mile-end-spiritualist-church` |
| Buried Temples and Forgotten Horrors; The Lost Temple of Magna Mater | 91–92 | `rule/buried-temples-and-forgotten-horrors`, `location/temple-of-magna-mater`, `location/chislehurst-caves`, `item/magna-mater-flesh`, `character/barry-matthews` |
| The Serpent People of Balham; Malfunction (таблица) | 92–93 | `organization/serpent-people-of-balham`, `item/serpent-people-probe`, `location/serpent-people-enclave`, `location/the-george-balham` |
| The Forgotten Shoggoth; Strays and Vermin | 93–95 | `creature/small-shoggoth-fragment`, `creature/large-shoggoth-fragment`, `location/isle-of-dogs` |
| The Thing in the Pit | 94 | `creature/injured-shoggoth`, `location/thing-in-the-pit-crater`, `character/des-merrill` |
| The Unwitting Host | 95–96 | `character/edna-goddard` |
| A Boy and his Shoggoth; James Fursey; Spot | 96–97 | `character/james-fursey`, `creature/spot` |
| Artefacts and Tomes; The British Museum Restricted Collection; Alec Harper | 97–98 | `rule/artefacts-and-tomes`, `location/british-museum-aldwych-store`, `character/alec-harper`, `character/gladys-wise`, `location/harper-tenement` |
| Shards of Darkness; Basil Forbes | 98–100 | `item/shards-of-darkness`, `character/basil-forbes`, `location/forbes-antiques` |
| Camden Town Deep-level Construction Works; The Porous Tunnel; The Dancing Shadows; The Gateway that Walks; Charlie Keene | 99–102 | `location/camden-town-deep-level-shelter`, `character/charlie-keene`, `character/deirdre-shepard`, `character/paul-jakeway`, `location/the-bell-camden`, `rule/artefacts-and-tomes` |
| Deep Ones in the Thames; Shark Steaks | 102 | `rule/deep-ones-in-the-thames`, `item/shark-steaks`, `character/simon-graves` |
| Battles on the Home Front; Assembling a World War Cthulhu: London Scenario; Setting; Tone; Content | 103–104 | `rule/battles-on-the-home-front` |
| London Voices: Albert Penny (врезка) | 104 | `character/albert-penny` |
| Midnight Sunrise: Introduction; Background | 105–107 | `scenario/midnight-sunrise` (summary, keeper_info) |
| Non-player Characters: Aurora Williams; Williams’ Staff (Named Staff, Example Staff Statistics) | 107–108 | `character/aurora-williams`, `character/williams-staff`, `character/miles-browne`, `character/martha-roberts`, `character/anthony-morris`, `character/ian-baker`, `character/harold-norton`, `character/everett-johnson`, `organization/williams-household` |
| New Spells: Candle Communication; Cloak of Fire; Create Fire Vampire; Fire Walk; Pyromancy | 109–110 | общие `coc:spell:candle-communication`, `coc:spell:cloak-of-fire`; черновики `create-fire-vampire`, `fire-walk`, `pyromancy` |
| Joseph Dunbar; Thomas Whitaker; Dr Paul Chamberlain; Reginald Fotheringay | 110–112 | `character/joseph-dunbar`, `character/thomas-whitaker`, `character/paul-chamberlain`, `character/reginald-fotheringay` |
| Fire Vampires; Proto-Fire Vampires; Fthaggua | 112–113 | `creature/fire-vampire-london`, `creature/proto-fire-vampire`, `creature/fthaggua-london` |
| Involving the Investigators; What do the Investigators Know about Teresa? (врезка) | 113–114 | `scene/ms-involving`, `character/teresa-hughes`, `character/lewis-hughes`, `character/rachael-hughes` |
| Keeper’s Timeline of Events | 114–115 | `scenario/midnight-sunrise` (keeper_info) |
| Teresa Hughes: Meeting Teresa; Avenues of Enquiry | 115–117 | `scene/ms-meeting-teresa`, `location/teresa-hughes-house`, `item/marble-triangle-slab` |
| Dunbar Visits; Visiting Lewis and Rachael | 117–118 | `scene/ms-dunbar-visits`, `scene/ms-visiting-lewis-and-rachael`, `location/rachael-hughes-flat` |
| Wednesday Night; Further Assistance from Teresa (врезка) | 118–120 | `scene/ms-wednesday-night` |
| Joseph Dunbar: Dunbar & Associates; Meeting Dunbar; Alternative Resolution (врезка) | 120–122 | `scene/ms-dunbar-and-associates`, `scene/ms-meeting-dunbar`, `location/dunbar-and-associates`, `character/miss-davies`, `item/dunbar-client-folder` |
| Dr Chamberlain: Royal Herbert Hospital (Handout 1); Dr Chamberlain’s Office (Handout 2) | 122–123 | `scene/ms-royal-herbert-hospital`, `scene/ms-chamberlain-office`, `handout/ms-handout-1-evening-standard`, `handout/ms-handout-2-handwritten-note`, `location/royal-herbert-hospital`, `location/chamberlain-office`, `location/chamberlain-home`, `character/mrs-young`, `item/chamberlain-williams-file` |
| Thomas Whitaker: Meeting Whitaker; Convincing Whitaker to Leave; Joyce Dobbs and Whitaker’s Abduction; Alternatives to Whitakers Abduction | 123–125 | `scene/ms-meeting-whitaker`, `scene/ms-joyce-dobbs-and-whitakers-abduction`, `scene/ms-alternatives-to-whitakers-abduction`, `location/riverside-hotel`, `location/joyce-dobbs-flat`, `character/joyce-dobbs` |
| The Williams Shipping Warehouse; Where to go from Here? | 125–126 | `scene/ms-williams-shipping-warehouse`, `location/williams-shipping-warehouse`, `character/williams-warehouse-guards` |
| Aurora Williams: Researching Williams (Handout 3); The Williams Residence | 126–127 | `scene/ms-researching-williams`, `scene/ms-williams-residence`, `handout/ms-handout-3-times`, `location/williams-residence` |
| Investigating Booksellers; An Optional Encounter | 127 | `scene/ms-investigating-booksellers`, `scene/ms-optional-encounter`, `location/charing-cross-road`, `character/charing-cross-bookseller` |
| Returning to the Williams Residence; The Assassination Tactic (врезка) | 127–128 | `scene/ms-returning-to-williams-residence`, `item/fake-police-identification` |
| Williams’ Study (Handouts 4–6); Das Puch Aller Verpoten Kunst | 128–130 | `scene/ms-williams-study`, `location/williams-study`, `handout/ms-handout-4-williams-journal`, `handout/ms-handout-5-fomalhaut`, `handout/ms-handout-6-journal-entry`, `tome/book-of-all-forbidden-arts`, `item/williams-candles` |
| The First Night of the Blitz: Meeting Fotheringay at Teresa’s House | 130–131 | `scene/ms-meeting-fotheringay-at-teresas-house` |
| Getting to the Warehouse; The Docklands Fire; Bombing Near the Warehouse (врезки) | 131–132 | `scene/ms-getting-to-the-warehouse`, `location/blackwall-tunnel`, `location/union-wharf`, `item/fireboat` |
| Arrival at the Warehouse | 132–134 | `scene/ms-arrival-at-the-warehouse`, `location/williams-warehouse-basement` |
| Aftermath | 134 | `scene/ms-aftermath`, `scenario/midnight-sunrise` (conclusion) |
| Captive Audience: Introduction; Keeper Considerations & The King in Yellow (врезка) | 135 | `scenario/captive-audience` (summary, advice) |
| Background: Act One: Preparation & Performance; Act Two: Aftermath & Planning | 135–138 | `scenario/captive-audience` (keeper_info); `character/simon-fairfax`, `seth-page`, `martin-jacobs`, `dean-henderson`, `constance-parker`, `ronald-brooks` |
| Keeper’s Timeline of Events | 138–139 | `scenario/captive-audience` (keeper_info) |
| Non-player Characters: Taylor Graves; Thomas Franklin; Stephen Nash; Mark Long; Adrienne Jacobs; The Acting Troupe | 139–141 | `character/taylor-graves`, `thomas-franklin`, `stephen-nash`, `mark-long`, `adrienne-jacobs`, `acting-troupe` (+ `joseph-marter`, `mary-beckett`) |
| New Spells: Echo of the Past; Enchant Sacrificial Blade; Summoning Circle | 142–143 | способности `character/taylor-graves`; черновики `echo-of-the-past`, `enchant-sacrificial-blade`, `summoning-circle`; `item/sacrificial-blade` |
| Charles Hubbard; Penny Beck; Vincent Elliott; Shelly Greene; Detective Robin Armstrong | 143–146 | `character/charles-hubbard`, `penny-beck`, `vincent-elliott`, `shelly-greene`, `robin-armstrong`; `character/hubbards-workers` |
| The Phantom of Truth (статблок, Join the Dance) | 146 | `creature/phantom-of-truth` |
| Involving the Investigators; Invitations – New Investigators (Handout 1, Handout 2) | 146–148 | `scene/ca-invitations`, `handout/ca-handout-1-invitation`, `handout/ca-handout-2-invitation`, `location/camden-street-house` |
| The Yellow Sign (врезка) | 148 | `scene/ca-invitations`, `scenario/captive-audience` (advice) |
| King’s Cross – Existing Investigators; Optional Scene (врезка) | 148–149 | `scene/ca-kings-cross`, `location/kings-cross-station`, `character/edward-bridges` |
| Network N Auxiliaries | 149–150 | `scene/ca-network-n` |
| Investigation & Encounters; Air Raids & Shelters: Conditions, Events | 150 | `scene/ca-air-raids-and-shelters` |
| Newspaper Articles (Handouts 3–4); Historical Events (Handouts 5–6) | 151 | `scene/ca-newspaper-articles`, `handout/ca-handout-3…6`, `character/mildred-davies` |
| Bridges’ Apartment | 152 | `scene/ca-bridges-apartment`, `location/bridges-apartment` |
| Researching Henderson, Brooks & Franklin (Handout 7) | 152 | `scene/ca-researching-henderson-brooks-franklin`, `handout/ca-handout-7-obituary` |
| Camden Street | 152–153 | `scene/ca-camden-street`, `item/franklin-photo`, `item/parker-belongings` |
| Meeting Franklin | 153 | `scene/ca-meeting-franklin`, `location/franklin-house` |
| The King in Yellow: Background; Obtaining a Copy (Handout 8); Reading the Play; The Last Page (врезка) | 153–155 | `scene/ca-king-in-yellow`, `handout/ca-handout-8-the-king-in-yellow`, `item/british-library-king-in-yellow`, `item/british-library-ledger`, `item/typed-copies-of-the-play`; предложение к `coc:tome:king-in-yellow` |
| St James’s Hall (Handout 9, Handout 10) | 155–156 | `scene/ca-st-jamess-hall-research`, `handout/ca-handout-9-st-jamess-hall`, `handout/ca-handout-10-plans-st-jamess-hall`, `map/st-jamess-hall-plans`, `location/st-jamess-hall` |
| Handout 11: Plans of the Piccadilly Hotel; The Piccadilly Hotel | 157–158 | `handout/ca-handout-11-plans-piccadilly-hotel`, `map/piccadilly-hotel-plans`, `scene/ca-piccadilly-hotel`, `location/piccadilly-hotel`, `location/piccadilly-hotel-air-raid-shelter` и 8 помещений по меткам плана |
| Charles Hubbard | 158 | `scene/ca-charles-hubbard` |
| Nash Attacks | 158–159 | `scene/ca-nash-attacks` |
| Nash’s Home (Handout 12) | 159 | `scene/ca-nashs-home`, `location/nash-home`, `handout/ca-handout-12-graves-business-card`, `item/nash-family-photo`, `item/piccadilly-hotel-uniforms` |
| Researching Graves | 159–160 | `scene/ca-researching-graves` |
| Hanover Terrace: Gaining Entry; The Summoning Circle; Police Involvement (врезка) | 160–162 | `scene/ca-hanover-terrace`, `location/hanover-terrace`, `location/graves-basement` |
| The Study and the Gateway to Carcosa | 161–162 | `scene/ca-study-and-gateway`, `location/graves-study`; предложения к `coc:tome:true-magick`, `cultes-des-goules`, `de-vermiis-mysteriis`, `nameless-cults` |
| The Night of the Performance; Set-up; Initial Investigation | 162–163 | `scene/ca-set-up` |
| The Troupe Acts | 163–164 | `scene/ca-troupe-acts`, `character/molly-locke` |
| The Communist Protest; The Captive Audience; Investigator Intervention (врезка) | 164–165 | `scene/ca-communist-protest` |
| St James’s Hall (эхо) | 165 | `scene/ca-st-jamess-hall-echo`, `location/st-jamess-hall-understage` |
| Stopping the Performance | 165–166 | `scene/ca-stopping-the-performance`, `location/st-jamess-hall-great-hall` |
| The Phantom of Truth (сцена) | 166–167 | `scene/ca-phantom-of-truth-on-stage` |
| Contingencies (врезка): Killing Graves; Refusing to Intervene; Sabotaging the Air-raid Shelter; Bombing the Hotel | 167–168 | `scene/ca-contingencies` |
| Conclusion | 168–169 | `scene/ca-conclusion`, `scenario/captive-audience` (conclusion) |
| The Meat Trade: Introduction | 170 | `scenario/the-meat-trade` (summary, advice) |
| Background: The Shepard Gang; Shepard’s Business Interests; The Bow Cemetery Ghouls; The Rat Catchers | 170–172 | `scenario/the-meat-trade` (keeper_info), `organization/shepard-gang`, `organization/bow-cemetery-ghouls`, `item/tainted-bacon`, `character/ronnie-shepard`, `character/desmond-welch`, `character/alf-welch`, `character/john-regan`, `creature/ghouls-in-human-guise` |
| Involving the Investigators: Random Strangers; Network N Auxiliaries; The Rat Catchers; Unaffiliated Investigators | 172 | `scene/mt-involving` |
| Opening Scene | 172–174 | `scene/mt-opening-scene`, `location/welch-shelter-whitechapel`, `character/barry-connell` |
| Grace Daggett (статблок); Daggett’s List | 173–174 | `character/grace-daggett`, `handout/mt-handout-1-daggetts-list`, `character/william-stubbings`, `edna-stubbings`, `billy-stubbings` |
| Davey Reed | 174–175 | `character/davey-reed` |
| The Shelter; The Raid Continues | 175–176 | `scene/mt-shelter-and-raid` |
| The Tunnels Beneath | 176 | `scene/mt-tunnels-beneath`, `location/ghoul-tunnels-east-end` |
| Grace Daggett’s Flat; Daggett’s Notes (врезка) | 177 | `scene/mt-grace-daggetts-flat`, `location/grace-daggett-flat`, `tome/daggetts-notes`, `item/rat-catchers-address-book`, `item/rat-catchers-photo-album`, `item/pickman-ghoul-painting`, `item/daggett-weapons-cabinet` |
| Welch & Sons | 177–178 | `scene/mt-welch-and-sons`, `location/welch-and-sons-yard` |
| Thompson Builders | 178 | `scene/mt-thompson-builders`, `location/thompson-builders`, `character/mick-thompson` |
| Fellick Printing; Meyer Fellick | 178–179 | `scene/mt-fellick-printing`, `location/fellick-printing`, `character/meyer-fellick`, `creature/fellick-guard-ghoul`, `item/forged-identity-documents` |
| The London Hospital; Dr Constance Morris | 179–180 | `scene/mt-london-hospital`, `location/london-hospital`, `character/constance-morris`, `character/martha-graves`, `character/kevin-graves` |
| Eddie Graves, Butcher and Widower; Jenny Graves, Ghoulish Daughter | 180–181 | `scene/mt-eddie-graves`, `character/eddie-graves`, `character/jenny-graves`, `location/graves-butchers-shop` |
| Bow Cemetery | 182 | `scene/mt-bow-cemetery`, `location/bow-cemetery-warrens`, `character/mr-black`; предложение к `wwc-covert-actions-en/location/bow-cemetery` |
| The Shoulder of Mutton; Frankie Shepard; Shepard’s Men; Ronnie Shepard | 182–184 | `scene/mt-shoulder-of-mutton`, `location/shoulder-of-mutton`, `character/frankie-shepard`, `character/shepards-men`, `character/ronnie-shepard` |
| Wilson’s Meat Supplies | 184 | `scene/mt-wilsons-meat-supplies`, `location/wilsons-meat-supplies`, `character/eric-wilson` |
| Wrapping Things Up | 184 | `scene/mt-wrapping-things-up` |
| Aftermath; Nancy Vallance | 184–185 | `scene/mt-aftermath`, `character/nancy-vallance`, `scenario/the-meat-trade` (conclusion) |
| Handout 1: Daggett’s List | 185 | `handout/mt-handout-1-daggetts-list` |
| The Strange and the Unexplained: Fortean Events in Wartime London | 186 | `rule/fortean-events-in-wartime-london` |
| Miraculous Escapes; The Clairvoyant Bookseller; The Enigma Disappearance | 186–187 | `rule/fortean-events-in-wartime-london` |
| Awoken by the Bomb | 187 | то же; `location/st-james-garlickhythe` |
| Suicide Point | 187–188 | то же; `location/cleopatras-needle` |
| The Ghost of Clarence House | 188 | то же; `location/clarence-house` |
| The Beast of Pond Square | 188 | то же; `location/pond-square` |
| Herald of Ill Fortune | 188 | то же; `location/hall-place` |
| Phantoms in the Skies (в оглавлении «Phantoms on the Skies») | 188–189 | `rule/fortean-events-in-wartime-london` |
| London Voices: Jim Tucker, 54, Office Clerk (врезка) | 189 | `character/jim-tucker`, `rule/fortean-events-in-wartime-london` |
| Index | 190–192 | не взято — указатель книги (использован для сверки заголовков) |

## Не взято

- Указатель (с. 190–192) — не данные; использован для сверки заголовков.
- Фоны врезок, раздаток и статблоков (бумага, узор), заставки глав и иллюстрации сцен без своей записи — атмосфера/оформление,
  `atmosphere-london-b.json`. Отчёт полноты помечает на этих страницах персонажей и раздатки «без картинки» — у них в книге
  портретов нет (Гловер, Чемберлен, Хендерсон, Паркер, Бриджес и др.); текстовые раздатки (газеты, записки, приглашения,
  список Даггет) напечатаны набором на фоне бумаги — текст в записях, картинок нет.
- Заклинания «Call/Dismiss Fthaggua» и «Contact Fthaggua» (с. 108, 130) — в книге только названия; в списках заклинаний с
  `spell: null`.
- Упомянутые мимоходом реальные места и лица — текстом в сценах и местах: Гросвенорская часовня, больница Уиттингтон, станции
  «Хайгейт», «Арчуэй», «Майл-Энд», «Боу-роуд», церковь Святого Михаила в Камдене, Королевский институт британских архитекторов,
  Министерство продовольствия, Профсоюз транспортных и разнорабочих, «Ягуар SS100» Грейвса; Хильда Бриджес, сестра Эдди Грейвса
  из Брайтона, гости отеля (примерные типы); в фортеанских событиях — Артур Баттеруорт, «Ричард Левински», Алан Тьюринг,
  Альфред Нокс, Сигрейв Чемберлен («Джимми Гарлик»), Соня Марш, герцог Коннаутский, Фрэнсис Бэкон, Теренс Лонг, Чёрный принц,
  леди Констанс Эт-Холл, пилот Грейсон, Манфред фон Рихтгофен, Уильям Хеншоу, аэродром Биггин-Хилл.
- Безымянные персонажи без механики (второй портье, констебли, 15 статистов 1905 года — по профилю труппы, восемь пленников в
  клетках у упырей, трое упырей на складе «Уилсона») — текстом в сценах и групповых записях; своих записей нет.
- Масштабные линейки и стрелка севера на картах — без меток (не подписи).

## Опечатки и сомнения

| Где | Напечатано | Ожидалось | В записи |
|---|---|---|---|
| с. 139 (хронология) | квартира Бриджеса «in Piccadilly» | Генриетта-стрит, Ковент-Гарден (с. 151, 152) | исправлено, errata `scenario/captive-audience` |
| с. 148 / с. 151 | Бриджес «early 40s» / «Edward Bridges (35)» | одно значение | по раздатке (35), errata `character/edward-bridges` |
| с. 153 | «see Handout 11 on the following page» (сведения Франклина о пьесе) | раздатка 8 (с. 154) | исправлено, errata `handout/ca-handout-8-the-king-in-yellow` |
| с. 141 | статблок Адрианны Джейкобс: навыки, языки и пистолет дословно как у Авроры Уильямс (с. 108) | — | как напечатано, errata `character/adrienne-jacobs` (сомнение) |
| с. 141 | труппа, вариант №2: Скорость 8 при СИЛ 70, ЛВК 65 > ТЕЛ 60 | 9 | как напечатано, errata `character/acting-troupe` (Р-161) |
| с. 175 | Дейви Рид: Скорость 6 | 8 по правилам (вероятно, учтена хромота) | как напечатано, errata `character/davey-reed` |
| с. 179 | Мейер Феллик: ПЗ 9 при ВЫН 45 + ТЕЛ 55 | 10 | как напечатано, errata (Р-161) |
| с. 181 | Дженни Грейвс: Скорость 9 при СИЛ 25, ЛВК 62 и ТЕЛ 30 | 8 | как напечатано, errata (Р-161) |
| с. 183 | Фрэнки Шепард: Скорость 8 при СИЛ 55, ЛВК 67 < ТЕЛ 70 | 7 | как напечатано, errata (Р-161) |
| с. 185 | Нэнси Валланс: Скорость 7 при СИЛ 55, ЛВК 62 > ТЕЛ 50 | 9 | как напечатано, errata (Р-161) |
| с. 180 | Констанс Моррис: Spot Hidden 50% (25/12) | (25/10) | исправлено, errata (Р-35) |
| с. 185 | Нэнси Валланс: Charm 40% (20/6); Cthulhu Mythos 2% (1/1) | (20/8); (1/0) | исправлено, errata (Р-35) |
| с. 3 / с. 188 | оглавление «Phantoms on the Skies» / заголовок «Phantoms in the Skies» | — | словесное (Р-39), не в errata |
| с. 3, 160 | «Hannover Terrace» (оглавление, указатель) / «Hanover Terrace» (текст) | — | словесное, по тексту |
| с. 142, 157 | «Picadilly Hotel» (врезка, план) / «Piccadilly» | — | словесное (Р-39); на плане — в `text` раздатки как напечатано |
| с. 171 | «tamper with the meat its way into London» | — | словесное (Р-39) |
| с. 82 | Кеннет Ходж: «Spot Hidden (Botany) 70%» | Внимание 70% или Наука (ботаника) 70% | как напечатано, errata `character/kenneth-hodge` |
| с. 83 | Нэнси Уэйн: Скорость 0, Уклонение 05% | 7; не ниже 16% | как напечатано, errata `character/nancy-wain` (Р-161) |
| с. 89 | преображённый культист: DB +1D6, Build +2 при СИЛ 90 + ТЕЛ 75 | +1d4, +1 (так и в атаке) | как напечатано, errata `character/transformed-cthulhu-cultists` |
| с. 94 | раненый шоггот: DB +2D6, Build +3 при СИЛ 120 + ТЕЛ 100 | +1d6, +2 | как напечатано, errata `creature/injured-shoggoth` — большинства нет (Р-36), **вопрос владельцу** |
| с. 97 | Джеймс Фёрси: Sleight of Hand «(40/16)» без процента | 80% | исправлено (вывод из текста, Р-41), errata `character/james-fursey` |
| с. 81–98, 141 | неверные половина/пятая у Ходжа, Мерчант, Дауни, Гарднер, Харпера, Фёрси, Лонга | по правилу 7-й редакции | исправлено (Р-35, Р-77 — где доли подходят к другому проценту, сказано в errata) |
| с. 99–145 | производные (ПЗ, ПМ, Скорость, Уклонение) у Форбса, Кина, Дауни, Гарднер, Ходжа, Эллиотта, Джейкобс | по правилам | как напечатано (Р-161) |
| с. 113 | Фтаггуа: жар в броне — «a fifth of their DEX in feet», в атаке — ВЫН в ярдах | одно правило | как напечатано, errata `creature/fthaggua-london` |
| с. 91 | «Chiselhurst Caves» | Chislehurst | errata `location/chislehurst-caves` |
| с. 128 | «Cloak of Fire (see pg 124)» | с. 109 | исправлено, errata `scene/ms-returning-to-williams-residence` |
| с. 129 | «(see 6: Journal Entry)» | Handout 6 | исправлено, errata `handout/ms-handout-6-journal-entry` |

## Термины (English → русский, наш выбор; переводчик книги берёт эти формы)

| English | Русский |
|---|---|
| Mythos Horrors | Ужасы Мифов |
| ghoul / ghoul changeling / warrens | упырь / упырь-подменыш / норы (логово) |
| The Rat Catchers | Крысоловы |
| Ointment of True Seeing | Мазь истинного зрения |
| Consume Likeness | Поглощение образа (по базе) |
| The Harvesters / The Temple of R’lyeh Risen / The Sea of Minds | Жнецы / Храм восставшего Р’льеха / Море разумов |
| The Serpent People of Balham | Змеелюди Балхэма |
| Shards of Darkness / Shark Steaks | Осколки тьмы / «Акулья вырезка» |
| Battles on the Home Front | Битвы в тылу |
| Midnight Sunrise / Captive Audience / The Meat Trade | Полуночный восход / Пленённая публика / Мясная торговля |
| Fthaggua, Herald of Cthugha / fire vampire / proto-fire vampire | Фтаггуа, Вестник Ктугхи / огненный вампир / прото-огненный вампир |
| The Book of All Forbidden Arts (Das Puch Aller Verpoten Kunst) | Книга всех запретных искусств |
| Anchor of Dreams / Gifts of the Deep | Якорь снов / Дары глубин |
| Create Fire Vampire (Ignite the Flame Within) / Fire Walk / Pyromancy | Создание огненного вампира (Зажечь пламя внутри) / Огненный путь / Пиромантия |
| Echo of the Past / Enchant Sacrificial Blade / Summoning Circle | Эхо прошлого / Зачаровать жертвенный клинок / Круг призыва |
| Sacrificial Blade | жертвенный клинок |
| The King in Yellow / the Yellow Sign / the Pallid Mask | «Король в жёлтом» / Жёлтый знак / Бледная маска (по базе) |
| The Phantom of Truth, Herald of the King in Yellow / the Stranger | Призрак истины, вестник Короля в жёлтом / Чужак |
| Join the Dance | Присоединиться к танцу |
| Yhtill / Queen Cassilda / Lake of Hali / Carcosa | Йхтилл / королева Кассильда / озеро Хали / Каркоза |
| Servitor of the Outer Gods / Court of Azathoth | служитель Внешних богов / Двор Азатота |
| True Magick | «Истинная магия» (по базе) |
| St James’s Hall / The Piccadilly Hotel | Сент-Джеймс-холл / отель «Пикадилли» |
| Hanover Terrace | Ганновер-террас |
| Special Branch | «Особый отдел» |
| The Shepard Gang / Shepard’s Men | банда Шепарда / люди Шепарда |
| The Bow Cemetery Ghouls / Bow Cemetery (Tower Hamlets Cemetery) | упыри кладбища Боу / кладбище Боу (кладбище Тауэр-Хамлетс) |
| The Shoulder of Mutton | паб «Баранья лопатка» |
| Welch & Sons / Thompson Builders / Fellick Printing / Wilson’s Meat Supplies | «Уэлч и сыновья» / строительная фирма «Томпсон» / типография Феллика / «Мясные поставки Уилсона» |
| Daggett’s Notes / Daggett’s List | «Записи Даггет» / список Даггет |
| ghouls in human guise | упыри в человеческом облике |
| Fortean Events / Story Hook | фортеанские события / зацепка |
| Ministry of Food / War Office | Министерство продовольствия / Военное министерство |

## Висящие ссылки

Нет: все ссылки записей части ведут на существующие записи (в том числе `wwc-cold-war-en/character/n`, записи части
london-a и `wwc-covert-actions-en/location/bow-cemetery`). Ссылки на черновики (заклинания, навыки) не поставлены — см. выше.
