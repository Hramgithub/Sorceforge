# Little Torches (`little-torches-en`) — перенос в базу (Р-251)

Heinrich D. Moore, 2020, Miskatonic Repository; современность (май 1994 года), Калифорния — Санта-Роза и окрестности.
Русского перевода сценария в базе нет (проверено по ключевым именам и местам: Эйнсли Харпер, Камелия, Дедал, Киносура,
Кэти Белл, Бану Нор, Харлем Бэнкс).

Страницы: PDF 60 страниц; печатная страница = физической (смещение для `books.json`: **0**). Без номера: обложка
(физ. 1) и листы готовых сыщиков (физ. 55–60); с. 2 и 3 (выходные данные, оглавление) пронумерованы.

## Записи (123)

- сценарий 1: `scenarios/little-torches` (summary, keeper_info, hook, advice, 13 шагов, conclusion с наградами Рассудка;
  таблицы «Хронология важных событий», «Шкала „Отмеченного Ктугхой“», «Как открыть Путь, Лестницу и Конец», «Дальнейшие изыскания»)
- сцены 21: часть I — `kathy-bell-burning`, `fire-aftermath`, `sky-meadows-talk`, `bell-family`, `professor-nor`,
  `inheritors-lecture`, `harper-first-meeting`, `further-research`; часть II — `midnight-visit`, `daedalus-exploration`,
  `beneath-the-institute`, `camellia-house-visit`; часть III — `lighthouse-dreams`, `the-outside`, `the-groundfloor`,
  `police-car-door`, `graffiti-door`, `wood-cabin-door`, `ordinary-door`, `the-tower`, `lantern-room`
- персонажи 33: со статблоками — `ainslee-harper`, `banu-nor`, `florence-sanders`, `simon-chance`, `dana-crawford`,
  `harlem-banks`, `alberto` (instance_of «Гибрид глубоководного»); групповые профили — `daedalus-nurses`,
  `daedalus-orderlies`; персонал (instance_of профиля) — `jessica-engel`, `denise-engel`, `cade-fall`, `joel-studer`,
  `coel-apsar`, `anita-gonzales`, `jason-dwyer`; без статблока — `kathy-bell`, `mark-bell`, `elanor-bell`, `sky-meadows`,
  `nathan`, `hanna-caulfield`, `alex-wu`, `heather-prinn`, `winston-larimee`, `shireen-harper`, `brandon-harper`;
  готовые сыщики (pregen) — `rhonda-persopoulos`, `cicero-washington`, `ian-walsh`, `morgan-starbuck`, `neda-rashbar`, `arthur-hansen`
- существа 3: `fire-vampires` (instance_of «Огненный вампир»), `cthugha-living-flame` (instance_of «Ктугха»),
  `ghoul-family` (instance_of «Упырь»)
- организации 4: `school-of-dream` (культ), `little-torches` («Маленькие факелы» доктора Харпер), `daedalus-staff`, `camellia-artist-colony`
- предметы 12: `cynosure` (артефакт; правила Киносуры и отметины Ктугхи), `lighthouse-puzzle-replica`, `festival-flyer`,
  `daedalus-clothes`, `kathy-prescriptions`, `elanor-watercolors`, `nor-office-artifacts`, `nor-travel-photographs`,
  `harper-tome-cabinet`, `maze-sketches`, `maze-paintings`, `walsh-sacred-scrolls`
- раздатка 14: `handout-01-lit` … `handout-14-camellia-reopening` (текст как напечатан + наш перевод, картинка приложения B)
- места 34: `santa-rosa` (город; общей записи нет), `santa-rosa-environs`, `crowley-college`, `price-building`,
  `crowley-display-hall`, `nor-office`, `bell-house`, `kathy-bell-room`, `elanor-bell-studio`, `daedalus-institute`,
  13 комнат по ключу плана (`daedalus-lobby` … `daedalus-harper-office`, `number` 1–13), `daedalus-caverns`, `daedalus-grounds`,
  `camellia-house`, `camellia-lighthouse`, `camellia-tunnels`, `gathering-of-leaves`; сновидение — `dream-lighthouse`
  (`город сценария`), `dream-outside`, `dream-groundfloor`, `dream-tower`, `dream-lantern-room`
- карта 1: `maps/daedalus-institute-layout` (`app/maps/torches-daedalus-institute-layout.jpg`, 1400×754; 18 меток —
  на каждой напечатанной цифре, «3» ×5, «8» ×2)

Картинки (28, применены `pipeline/integrate/apply.py`): портреты 6 (Кэти Белл, Харпер, Фло Сандерс, Бэнкс, Чанс, Кроуфорд),
фото Киносуры, фото усадьбы «Камелия», раздатка 1–14 (вырезки страниц 39–52, рамки — `torches-boxes.json`), листы шести
готовых сыщиков (`card`; портретов нет — силуэт). Атмосфера → `atmosphere.json` (9: обложка, с. 6, 9, 18, 23, 24, 26, 31, 32).

Предложения к общим записям — `proposals-torches.json` (3, пробный прогон проходит): экземпляры «Золотой ветви»,
«Разоблачённой Изиды» и «Текста Р’льеха» в шкафу Харпер (`copies`).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка | физ. 1 | сценарий (`sources`); атмосфера (обложка) |
| Credits: Author Information, Photo Credits, Thanks to the Playtesters, Special Thanks, Disclaimer | 2 | сценарий (`sources`, `summary` — предупреждение); подписи картинок — по Photo Credits; остальное — «Не взято» |
| Table of Contents | 3 | сценарий (`sources`) |
| Introduction (эпиграф Глазби) | 4 | сценарий; эпиграф — «Не взято» |
| Overview | 4 | сценарий (`summary`, `advice`) |
| A Note on Skill Checks | 4 | сценарий (`advice`) |
| Cthugha, Great Old One | 4 | сценарий (`keeper_info`); `cthugha-living-flame` (legend); `fire-vampires` |
| Who is Dr. Ainslee Harper? | 4–5 | сценарий (`keeper_info`); `ainslee-harper` (legend, secret) |
| The Cynosure | 5 | `item/cynosure` (description, mechanics: уничтожение) |
| The Spark of Cthugha | 5–6 | `item/cynosure` (mechanics: заворожённость, ПМ, вампиры) |
| Touched by Cthugha | 6 | `item/cynosure` (mechanics); раздатки 1–4; сцена `lighthouse-dreams` |
| Investigator’s Introduction | 6 | сценарий (`hook`); сцена `fire-aftermath` |
| Keeper’s Introduction | 6, 8 | сценарий (`keeper_info`) |
| Touched by Cthugha Progression (Player Handouts #1–4) | 7 | раздатки 1–4 (description — эффект); таблица сценария «Шкала „Отмеченного Ктугхой“» |
| Timeline of Important Events: Historical Events | 8 | таблица сценария «Хронология важных событий» |
| Current Events; Possible Future Events | 9 | та же таблица; сцены (`when`) |
| Part I: The Burning of Kathy Bell (эпиграф Дикинсон) | 10 | сцена `kathy-bell-burning`; эпиграф — «Не взято» |
| Crowley College | 10 | места `crowley-college`, `price-building`; сцена `kathy-bell-burning` |
| School Fire (и список эпизодов) | 10–11 | сцена `kathy-bell-burning` (все 7 эпизодов) |
| Aftermath | 11 | сцена `fire-aftermath` |
| Sky Meadows | 11 | сцена `sky-meadows-talk`; персонаж `sky-meadows` |
| The Bell Family | 12 | сцена `bell-family`; `mark-bell`; место `bell-house` |
| Kathy Bell's Kidnapping and the School of Dream | 12 | сцена `bell-family`; организация `school-of-dream`; `elanor-bell` |
| The Daedalus Institute (у Беллов) | 12 | сцена `bell-family`; `kathy-bell` |
| Kathy Bell's Last Morning | 12 | сцена `bell-family` |
| Elanor Bell's Studio | 12 | место `elanor-bell-studio`; предмет `elanor-watercolors` |
| Kathy Bell’s Room (Desk, Closet, Bedside dresser, Bed) | 12–13 | место `kathy-bell-room`; предметы `cynosure`, `daedalus-clothes`, `kathy-prescriptions`; раздатка 11 |
| Player Handout #11 (в главе) | 13 | раздатка 11 (отличия копий — в `quality.notes`) |
| Professor Banu Nor (The Cynosure, Kathy Bell's last words, lecture, Dr. Ainslee Harper) | 13–14 | сцена `professor-nor`; `banu-nor`; место `nor-office`; предметы `nor-office-artifacts`, `nor-travel-photographs` |
| Цитата Бану Нор | 14 | `banu-nor` (legend); сцена `professor-nor` |
| Inheritors of the Light | 14 | сцена `inheritors-lecture`; место `crowley-display-hall` |
| Doctor Ainslee Harper | 14 | сцена `harper-first-meeting`; место `daedalus-institute` (history) |
| First impressions (и темы разговора) | 15 | сцена `harper-first-meeting`; место `daedalus-harper-office` |
| Encounters in the Institute | 15 | сцена `harper-first-meeting` |
| Further Research (Kathy Bell, Camellia House, Dr. Ainslee Harper, Daedalus Institute, Cthugha) | 16–17 | сцена `further-research`; таблица сценария «Дальнейшие изыскания» |
| Player Handouts #12, #13, #14 (в главе) | 16–17 | раздатки 12–14 |
| Part II: Counterstrike (эпиграф Фроста) | 18 | сцена `midnight-visit`; эпиграф — «Не взято» |
| A Midnight Visit; цитата Фло | 18 | сцена `midnight-visit`; `florence-sanders` |
| Florence “Flo” Sanders (история) | 19 | `florence-sanders` (legend); сцена `midnight-visit` |
| The Daedalus Institute; Layout | 19 | сцена `daedalus-exploration`; место `daedalus-institute` |
| West Wing & Lobby (1)–(6) | 19–20 | места `daedalus-lobby` … `daedalus-kathy-room`; карта |
| East Wing (7)–(13) | 20 | места `daedalus-recreational-space` … `daedalus-harper-office`; предмет `harper-tome-cabinet`; карта |
| Grounds | 20 | место `daedalus-grounds` |
| Daedalus Institute Layout (план) | 21 | карта `daedalus-institute-layout` |
| Beneath the Institute (First–Fourth Chamber) | 21 | место `daedalus-caverns`; сцена `beneath-the-institute`; `alberto`, `nathan`, `ghoul-family` |
| Staff (Day shift, Night shift) | 21–22 | организация `daedalus-staff`; персонал; сцена `daedalus-exploration` |
| Patients | 22 | сцена `daedalus-exploration`; место `daedalus-institute`; организация `little-torches` |
| Цитата Харпер («Я назвала его „Дедал“…») | 22 | `ainslee-harper` (legend); сцена `daedalus-exploration` |
| Camellia House | 22–23 | место `camellia-house`, `camellia-lighthouse`, `camellia-tunnels`; сцена `camellia-house-visit` |
| Daytime visits, Nighttime visits | 22–23 | сцена `camellia-house-visit`; организация `camellia-artist-colony` |
| Part III: Dreams in the Lighthouse (эпиграф Донна) | 24 | сцена `lighthouse-dreams`; место `dream-lighthouse`; эпиграф — «Не взято» |
| Discovering the Path, the Stairs, and the End | 25 | раздатки 5–7; таблица сценария «Как открыть Путь, Лестницу и Конец» |
| The Outside; Player Handout #8 | 26 | сцена `the-outside`; раздатка 8; место `dream-outside` |
| Following the shoreline; Going to the Light; Enter the darkness | 26–27 | сцена `the-outside` |
| The Groundfloor; Player Handout #9 | 27 | сцена `the-groundfloor`; раздатка 9; место `dream-groundfloor` |
| The Metal Trapdoor | 27 | сцена `the-groundfloor` |
| The Police Car Door—Officer Harlem Banks | 28 | сцена `police-car-door`; `harlem-banks` |
| The Graffiti Door—Simon Chance; цитата Чанса | 28–29 | сцена `graffiti-door`; `simon-chance` |
| The Wood Cabin Door—Dana Crawford | 30 | сцена `wood-cabin-door`; `dana-crawford`; место `gathering-of-leaves`; предмет `festival-flyer` |
| The Ordinary Door—Florence “Flo” Sanders | 30–31 | сцена `ordinary-door` |
| Solve the Puzzle | 31 | сцена `the-groundfloor`; предмет `lighthouse-puzzle-replica` |
| The Tower; Player Handout #10; The Sea; The Flame; Keep Running | 32 | сцена `the-tower`; раздатка 10; место `dream-tower` |
| The Lantern Room | 32–33 | сцена `lantern-room`; место `dream-lantern-room`; `cthugha-living-flame` |
| Цитата Харпер («Знаете, я вас люблю…») | 34 | `ainslee-harper` (legend); сцена `lantern-room` |
| Conclusion | 34 | сценарий (`conclusion`: награды Рассудка) |
| Future Threads | 34 | сценарий (`conclusion`, «Нити на будущее») |
| Appendix A: Biographies & Bestiary — Daedalus Institute; Staff, Nurses and Orderlies | 35 | `daedalus-nurses`, `daedalus-orderlies`, `daedalus-staff` |
| Jessica and Denise Engel; Joel Studer and Coel Apsar; Anita Gonzales; Cade Fall; Jason Dwyer | 35 | одноимённые персонажи |
| Daedalus Institute Nurses / Orderlies (статблоки) | 35 | `daedalus-nurses`, `daedalus-orderlies` |
| Dr. Ainslee Harper, Psychiatrist and Head of the Daedalus Institute | 36 | `ainslee-harper` (statblock) |
| Daedalus Residents: “Alberto,” Deep One Hybrid | 36 | `alberto` |
| “The Family,” Ghoul pack | 36 | `ghoul-family` |
| Little Torches: Florence “Flo” Sanders, Old Before Her Time | 36–37 | `florence-sanders` |
| Simon Chance, Burnt-out Ballerina | 37 | `simon-chance` |
| Dana Crawford, Tired Park Ranger | 37 | `dana-crawford` |
| Officer Harlem Banks, Fanatical Police Officer | 37 | `harlem-banks` |
| Other Cast: Professor Banu Nor, Gentlewoman Adventurer | 37 | `banu-nor` |
| Creatures of the Mythos: Fire Vampires, Children of Fomalhaut | 37–38 | `fire-vampires` |
| Cthugha, The Living Flame | 38 | `cthugha-living-flame` |
| Appendix B: Player Handouts #1–#14 | 39–52 | раздатки 1–14 (тексты и картинки) |
| Appendix C: Pre-Generated Characters (Rhonda Persopoulos, Cicero Washington, Ian Walsh, Sister Morgan Starbuck, Neda Rashbar, Arthur Hansen) | 53–54 | одноимённые готовые сыщики (background, legend) |
| Листы готовых сыщиков «Modern Era Investigator» | физ. 55–60 | статблоки готовых сыщиков; картинки листов (`card`) |

## Опечатки и противоречия книги

| Где | Напечатано | Что сделано |
|---|---|---|
| с. 25, таблица «Discovering…» | Player Handout #6 The Path, #7 The Stairs, #8 The End | номера по приложению B (#5–#7); `errata` у раздаток 5–7 и сценария |
| с. 25 | модель головоломки «in Kathy Bell's room at the Daedalus Institute» | по описанию комнат (с. 19–20, 31) — у Фло Сандерс и Саймона Чанса; `errata` предмета `lighthouse-puzzle-replica` |
| с. 25 | «Simon Chase» | Simon Chance; написание — в псевдонимах Чанса, пометка в раздатке 7 |
| с. 42, карта раздатки 4 | «Y'ah nafl mguh'e, Y'an fm'latghor» | текст карты как напечатан; `errata` раздатки 4 (везде «Y'ah») |
| с. 37, Харлем Бэнкс | Dodge 25% (13/5) | половина исправлена на 12 (Р-35), `errata` + `corrections` |
| с. 35, санитары | Dodge 35% (16/7) | половина исправлена на 17 (Р-35), `errata` + `corrections` |
| с. 35, медсёстры | Move: 0 | как напечатано, `errata` (по характеристикам 8) |
| с. 36, Альберто | HP 11; Move 8/8; Dodge 30% | как напечатано, `errata` (12; 9; не ниже 32%) |
| с. 37, Дана Кроуфорд | Move: 8 | как напечатано, `errata` (по характеристикам 7) |
| с. 36, Фло Сандерс | Move: 4 при возрасте 21 | задумано книгой (тело постарело, Р-76), `errata` с пометкой |
| физ. 55, Ронда Персопулос | Handgun 70/35/14 в графе оружия при навыке Стрельбы (пистолет) 50; Language (Own) Greek 50 при ОБР 60 | как напечатано, `errata` |
| с. 13 / с. 49 | копии дневника Кэти различаются («college»/«school» и др.) | текст — по приложению B; отличия в `quality.notes` раздатки 11 |
| с. 16 / с. 50 | «within the building» / «within the compound» | текст — по приложению B; пометка в раздатке 12 |
| с. 36, упыри | «it hands on» (вместо «hangs on») | raw как напечатано; пометка в `quality.notes` |
| физ. 59 | «Mashdad, Iran» | место рождения — Мешхед; пометка у Неды Рашбар |
| с. 19 / с. 36 | Фло «late 70s» / «early 70s» | пометка у Фло Сандерс |
| с. 16, с. 28 | «Hard of Extreme success» | словесная опечатка («or»), исчезает в переводе — не записана (Р-39) |

## Термины книги (английский → русский)

| English | Русский |
|---|---|
| Little Torches (сценарий) | «Маленькие факелы» |
| Little Torches (пациенты Харпер) | «маленькие факелы» (организация — «„Маленькие факелы“ доктора Харпер») |
| Touched by Cthugha | отмеченный Ктугхой (стать отмеченным Ктугхой) |
| Lit / Ignited / Burned / Immolation | «Зажжён» / «Воспламенён» / «Обожжён» / «Самосожжение» |
| the Cynosure | Киносура |
| The Spark of Cthugha | искра Ктугхи |
| the Lighthouse (dream) | Маяк; Маяк-сновидение |
| dreamscape | сновидческий мир (Киносуры) |
| The Outside | «Снаружи» (место — «берег и пещеры») |
| The Groundfloor | первый этаж |
| The Tower | Башня |
| The Lantern Room | Фонарный зал |
| The Path / The Stairs / The End | «Путь» / «Лестница» / «Конец» |
| the Light (в пещерах) | Свет |
| The Sea / The Flame / Keep running | Море / Пламя / Бежать дальше |
| fugue state | состояние фуги, фуга |
| Daedalus Institute for Psychiatric Research and Treatment | Институт психиатрических исследований и лечения «Дедал» (институт «Дедал») |
| Permanent Residents | «постоянные жильцы» |
| Reflection room | комната размышлений |
| Utilities Room | техническое помещение |
| Camellia House | усадьба «Камелия» |
| rum runner tunnels | туннели бутлегеров |
| School of Dream | Школа Сна |
| artist colony | колония художников |
| Crowley College; Crawlies | колледж Кроули; «Ползуны» |
| Price Building | корпус Прайса |
| Inheritors of the Light | «Наследники света» |
| A Gathering of Leaves | «Собрание листьев» |
| Ateshgah (Fire Temple, Baku) | Атешгях (храм огня, Баку) |
| Agape Lodge | «Ложа Агапе» |
| Sonoma Mountain Range | горы Сонома |
| The Family (ghoul pack) | Упыри «Семья» |
| Cthugha, The Living Flame | Ктугха, Живое пламя |
| Fire Vampires, Children of Fomalhaut | огненные вампиры, Дети Фомальгаута |
| Flame Burst | Сполох пламени |
| Advantage (на проверках) | бонусная кость |
| Hard / Extreme / Regular success | трудный / чрезвычайный / обычный успех |

Имена: Ainslee Harper — Эйнсли Харпер; Banu Nor — Бану Нор; Kathy / Mark / Elanor Bell — Кэти / Марк / Эленор Белл;
Sky Meadows — Скай Медоус; Florence “Flo” Sanders — Флоренс «Фло» Сандерс; Simon Chance — Саймон Чанс; Dana Crawford —
Дана Кроуфорд; Harlem Banks — Харлем Бэнкс; Jessica / Denise Engel — Джессика / Дениз Энгел; Joel Studer — Джоэл Стьюдер;
Coel Apsar — Коул Апсар; Anita Gonzales — Анита Гонсалес; Cade Fall — Кейд Фолл; Jason Dwyer — Джейсон Дуайер; Alberto —
Альберто; Nathan — Нейтан; Hanna Caulfield — Ханна Колфилд; Alex Wu — Алекс Ву; Heather Prinn — Хизер Принн; Winston
Larimee — Уинстон Ларими; Shireen / Brandon Harper — Ширин / Брэндон Харпер; Rhonda Persopoulos — Ронда Персопулос;
Cicero Washington — Сисеро Вашингтон; Ian Walsh — Иэн Уолш; Sister Morgan Starbuck — сестра Морган Старбак; Neda Rashbar —
Неда Рашбар; Arthur Hansen — Артур Хансен; Andrea Hollander — Андреа Холландер.

## Не взято

- Эпиграфы частей (Джон Глазби «The Dark Mirror», Эмили Дикинсон, Роберт Фрост «Fire and Ice», Джон Донн «A Burnt Ship»,
  с. 4, 10, 18, 24) — цитаты чужих литературных произведений, без игрового содержания.
- Выходные данные (с. 2): контакты автора (почта, Twitter), список игроков-тестеров, благодарности, строка о товарных
  знаках — не игровой материал; фото-кредиты использованы в подписях картинок.
- Атмосферные иллюстрации (9) — в `atmosphere.json`, не в записях.
- Комната без номера на плане института (рядом с комнатами 3) — в ключе не описана; метки нет, догадка (комната персонала)
  — в `quality.notes` карты.
- Отдельные записи для упомянутых только в предысториях готовых сыщиков (напарница Андреа Холландер, бывший капитан
  пожарной части, сестра Морган, брат Ронды) — без роли в сценарии; остаются текстом в `background`.
- Отдельные записи мест, упомянутых мимоходом (Атешгях в Баку, Иран, церковь моряков под Бостоном, дом Ларими, участок
  Бэнкса, ночной клуб Чанса, хижина Кроуфорд, Фомальгаут) — остаются текстом в сценах и описаниях.
- Алистер Кроули и Джек Парсонс — упомянуты текстом; общих записей нет (есть записи книг в «Лохмотьях Короля» и
  «Pax Cthuliana»), связи не ставились.

## Вопросы и долги

- `dream-lighthouse` («Маяк-сновидение») — вершина гайда с типом `город сценария`: сновидческий мир Киносуры не входит в
  реальный город, а `check.py` разрешает место без `part_of` только городу, кораблю или городу сценария. Книга не называет
  его Страной грёз. Если нужна другая вершина (например, общая «Страна грёз»), — решение владельца.
- Санта-Роза — запись книги (`location_type` `город`), общей записи нет; кандидат в общий город `coc:location:santa-rosa`.
- `names` групповых профилей персонала — имена из книги, а не придуманные (книга называет всех сотрудников).
- Кандидаты в общие записи: Санта-Роза; Алистер Кроули, Джек Парсонс; «Ложа Агапе» / орден Восточных тамплиеров;
  термин «Touched by Cthugha».
