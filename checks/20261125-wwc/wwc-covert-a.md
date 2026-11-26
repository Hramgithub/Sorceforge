# World War Cthulhu: Cold War — Covert Actions: часть covert-a (миссии 1–3)

Книга `wwc-covert-actions-en` (оригинал, Cubicle 7, 2017; издание 7e — Hard/Extreme, бонусные и штрафные кубики, статблоки 7e).
Страницы части: с. 1–92 (обложка, оглавление, выходные данные, введение сборника и миссии «Puddles Become Lakes»,
«The Forcing Move», «Cadenza»). **Печатная страница = физической (offset 0)**: «2» на физ. 2, «27» на физ. 27,
«92» на физ. 92; без номера — обложка (1) и титулы глав (5, 33, 62).

Записи — `kb/books/wwc-covert-actions-en/` (215 файлов): 3 сценария, 53 сцены, 50 персонажей, 2 существа, 68 мест,
3 карты, 15 раздаток, 19 предметов, 2 организации. Карты — `app/maps/wwc-covert-a-{limassol,raf-akrotiri,numbers-station}.jpg`;
картинки — 46 записей (`checks/20261125-wwc/art-covert-a.json`, применено). Черновики общих заклинаний —
`checks/20261125-wwc/new-shared-covert-a/spells/` (4). Предложения — `proposals-covert-a.json` (1). Эпоха — `1940s-1980s`.

## Заголовки книги → записи базы

`…/` = `wwc-covert-actions-en/`.

### Начало книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка | 1 | источник сценария `…/scenario/puddles-become-lakes`; картинка — атмосфера |
| Contents | 2–3 | источник всех трёх сценариев |
| Credits | 3 | авторы — в `summary` сценариев; источник сценариев |
| Introduction (сборника) | 4 | `summary` каждого сценария (год, автор, завязка); источник сценариев |

### Puddles Become Lakes (Мэттью Докинз) — `…/scenario/puddles-become-lakes`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул главы 1 | 5 | источник сценария (картинка — атмосфера) |
| Puddles become Lakes: Date, Location | 6 | `summary` сценария |
| Introduction | 6 | `summary` |
| Background | 6–7 | `keeper_info`; персонажи Сенцова, Фанмур, Ховенхэм, Гуджон, Эпплби |
| Briefings | 7–9 | сцены `puddles-briefing`, `puddles-bow-cemetery`, `puddles-operation-lake`; места `billingsgate-flophouse`, `bow-cemetery`, `stepney-east-station` |
| врезка SIS and Domestic Operations | 8 | сцена `puddles-briefing` (mechanics), `advice` сценария |
| Dan Vassidine, SIS Handler, Age 64 | 9 | `…/character/dan-vassidine` |
| The Journalist’s House | 9–10 | сцена `puddles-fanmoore-house`, место `fanmoore-house` |
| The Garden | 10 | место `fanmoore-house`, существо `…/creature/clement` |
| The Upstairs | 10 | место `fanmoore-house`, `…/character/leonard-fanmoore`, раздатка 1 |
| The Downstairs | 10–11 | место `fanmoore-house`, раздатка 2 |
| The Cellar | 11 | сцена `puddles-fanmoore-cellar`, место `fanmoore-cellar` |
| The Evidence | 11–12 | предмет `fanmoore-dictaphone-tape` (полный текст обеих сторон кассеты) |
| Billie Fanmoore, Freelance Journalist, Age 22 | 12–13 | `…/character/billie-fanmoore` |
| Researching the Peers | 13 | сцена `puddles-researching-the-peers` |
| Public Record / Private Secrets | 13–14 | таблица сценария «Изыскания о пэрах»; `legend` Ховенхэма и Гуджона |
| врезка Another Road to the Pub | 14 | сцена `puddles-researching-the-peers` |
| The Cask and Glass | 14–15 | сцена `puddles-cask-and-glass`, место `cask-and-glass` |
| Seyton Hovenham, Baron of Harlow and Soviet Mole, Age 55 | 15 | `…/character/seyton-hovenham` |
| Percy Goodjohn, Viscount Longforgan and Brother of the Yellow Sign, Age 53 | 15–16 | `…/character/percy-goodjohn` |
| Hovenham Manor | 16–17 | сцена `puddles-hovenham-manor`; места `hemel-hempstead`, `hovenham-manor`, `hovenham-summerhouse`; `lynette-agard`; предмет `hovenham-radio` |
| Goodjohn’s Journey | 17 | сцена `puddles-goodjohn-train` |
| The Train | 17 | сцена `puddles-goodjohn-train`, предмет `goodjohn-briefcase`, раздатки 3, 4 |
| The Estate | 17–18 | сцена `puddles-dandelion-house`; места `longforgan`, `dandelion-house`; `dandelion-house-staff` |
| The Labyrinth | 18 | место `dandelion-house`, сцена `puddles-dandelion-house` |
| The Attic | 18–19 | место `dandelion-house-attic`; предметы `goodjohn-radio`, `enslavement-to-the-icterus-copy`; экземпляр «Откровений Хали» — предложение |
| The Safe House | 19–20 | сцена `puddles-safe-house`, место `stratford-safe-house` |
| The Return of Vassidine | 20 | сцена `puddles-safe-house` |
| Appleby’s Trail | 20–21 | сцена `puddles-appleby-trail`; места `kirkcaldy`, `la-petite-maison`; `maggie-swivney`; предмет `appleby-cash-clip`; раздатка 7 |
| Appleby’s Remains | 21 | сцена `puddles-appleby-trail`, предмет `appleby-needles`, `godfrey-appleby` |
| The Beach Hut | 21 | сцена `puddles-beach-hut`, место `kirkcaldy-beach-hut-c3`, раздатка 8 |
| Emily Macarthur? | 21–22 | сцена `puddles-macarthur-flat`, место `macarthur-flat`, `emily-macarthur`, `gus-campbell`, раздатки 9, 10 |
| The Open | 22 | сцена `puddles-the-open`, места `st-andrews`, `open-royal-pavilion` |
| Dress Appropriately | 22 | место `open-royal-pavilion`, сцена `puddles-the-open` |
| The Movers and Shakers (Hovenham, Goodjohn, Fanmoore, Sentsova) | 22–24 | сцена `puddles-the-open`; `valerie-brown`; предметы `tartan-golf-bag`, `neural-seed` |
| Sentsova’s Plan | 24–25 | `…/character/alexia-sentsova` (`legend`), сцена `puddles-the-open` |
| Alexia Sentsova, Yithian disguised as a Scottish Barmaid disguised as a Ukrainian Agent, Age 25 | 25 | `…/character/alexia-sentsova` |
| Return to Dandelion House | 25–26 | сцена `puddles-return-to-dandelion-house` |
| Conclusion | 26–27 | `conclusion` сценария (все концовки) |
| Relationship Map | 26 | таблица сценария «Карта связей» + картинка сценария (`kind: plan`) |
| Sanity/Trust Rewards | 27 | `conclusion` сценария |
| Spells: Pnakotus Quills | 27 | черновик `coc:spell:pnakotus-quills`; атака у `alexia-sentsova` |
| Spells: Enslavement to the Icterus | 27–28 | черновик `coc:spell:enslavement-to-the-icterus` |
| Handouts #1–#10 | 28–32 | `…/handout/puddles-handout-1-letter-from-alex` … `puddles-handout-10-open-ticket-envelope` (текст + картинка) |

### The Forcing Move (Скотт Доруорд) — `…/scenario/the-forcing-move`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул главы 2 | 33 | источник сценария (картинка — атмосфера) |
| The Forcing Move: Date, Location, Introduction | 34 | `summary` сценария |
| врезка A Note on Historical Accuracy | 35 | сцена `forcing-laugardalsholl`, `advice` |
| Background | 35 | `keeper_info` |
| Erik Leonidovich Yefimov, the Central Chess Club, and N | 35–36 | `keeper_info`; `erik-yefimov`, `ratimir-zakharin`, `stanimir-timoshkin`, `iosif-mamykin`; организация `central-chess-club`; предмет `yefimov-dossier` |
| врезка Timeline of Events | 36 | таблица сценария «Хронология событий» |
| Bobby Fischer and the Shining Word | 36 | `keeper_info`; организация `shining-word-publications`; `bobby-fischer`, `virgil-marquardt` |
| Briefings / Official Briefing | 36–38 | сцена `forcing-official-briefing` (место — `wwc-cold-war-en/location/greene-club`) |
| Sir Clive Grenfell, Head of the Soviet Section, Age 62 | 38 | `…/character/clive-grenfell` |
| врезка British/Icelandic Relations | 39 | `history` места `reykjavik` |
| N’s Briefing | 39–40 | сцена `forcing-n-briefing`; `lauren-weeks` |
| врезка Involving H | 41 | сцена `forcing-n-briefing` (mechanics) |
| Reykjavik | 41 | место `reykjavik` |
| врезка Icelandic Currency and Exchange Rates | 41 | место `reykjavik` |
| Possible Meeting Places in Reykjavik | 42 | места `austurvollur-square`, `holavallagardur-cemetery`, `reykjavik-botanical-gardens` |
| The Icelandic Authorities; Average Icelandic Police Officer | 42 | место `reykjavik`; `…/character/icelandic-police-officer` |
| врезка Additional NPC Names | 42 | таблица сценария «Дополнительные имена персонажей»; `names` полицейского и горожанина |
| врезки A Note on Russian Names / A Note on Icelandic Names | 43 | вступление таблицы «Дополнительные имена персонажей» |
| British Embassy | 43–44 | сцена `forcing-british-embassy`, место `british-embassy-reykjavik` |
| Bernard Morton, SIS Number Two in Reykjavik, Age 31 | 44–45 | `…/character/bernard-morton` |
| врезка Access to Firearms | 45 | сцена `forcing-british-embassy` (mechanics) |
| Terence Soames, Reykjavik Head of Station, Age 44 | 45–46 | `…/character/terence-soames` |
| The Safe House | 46 | сцена `forcing-safe-house`, место `reykjavik-safe-house-farm` |
| Erik Leonidovich Yefimov, Would-be Defector, Age 39 | 46–47 | `…/character/erik-yefimov` |
| Dealing with Yefimov | 47 | сцена `forcing-dealing-with-yefimov` |
| Ratimir Rodionovich Zakharin, Russian Correspondent of N, Age 56 | 47–48 | `…/character/ratimir-zakharin` |
| Zakharin’s Actions | 48 | сцена `forcing-zakharin` |
| The Hotel Esja | 48–49 | сцена `forcing-hotel-esja`, место `hotel-esja`, `miloslav-agapov` |
| врезка The Presence of Intelligence Services in Reykjavik | 49 | сцена `forcing-hotel-esja` (mechanics) |
| Bobby Fischer, Damaged Genius, Age 29; врезки Bobby Fischer and Mental Illness, Fischer after 1972 | 49–50 | `…/character/bobby-fischer`, сцена `forcing-bobby-fischer` |
| Other Notable Characters | 50–51 | `william-lombardy`, `boris-spassky`, `gudmundur-thorarinsson`, `lothar-schmid` |
| Generic Civilian | 52 | `…/character/generic-civilian` |
| The Hotel Loftleidir | 52 | место `hotel-loftleidir`, сцена `forcing-bobby-fischer` |
| Bobby Fischer’s Suite; врезка Shining Word Publications in Fischer’s Suite | 52 | место `fischer-suite`, предмет `dangerous-truths` |
| Laugardalsholl | 52–54 | место `laugardalsholl`, сцена `forcing-laugardalsholl` |
| врезка Key Events of the 1972 World Chess Championship | 53 | таблица сценария «Главные события чемпионата мира по шахматам 1972 года» |
| Virgil Marquardt; Virgil Marquardt, Disciple of Daoloth, Age 36 | 54–55 | `…/character/virgil-marquardt` |
| врезки Spell: Speak the Shining Word / Spell: Drop Guise | 55 | черновики `coc:spell:speak-the-shining-word`, `coc:spell:drop-guise` |
| Marquardt’s Hideout | 55–56 | сцена `forcing-marquardt-hideout`, место `marquardt-guest-house` |
| врезка Rending the Veil | 56 | сцена `forcing-marquardt-hideout` |
| Exposure to Shining Word Transmissions | 57–58 | предмет `dangerous-truths` (mechanics) + таблица сценария «Воздействие Сияющего слова» (1d12) |
| врезка Building Paranoia | 57 | сцена `forcing-keeping-things-moving` |
| Tracking Down Marquardt | 58 | сцена `forcing-tracking-down-marquardt`, место `keflavik-airport` |
| врезка The Rest of the Shining Word | 58 | организация `shining-word-publications` |
| Keeping Things Moving | 58–59 | сцена `forcing-keeping-things-moving` (все события), `jonathan-cairns`; финальное событие — сцена `forcing-marquardt-ascension` |
| Conclusion | 59–60 | `conclusion` сценария |
| Sanity and Trust Awards | 60 | `conclusion` сценария |
| Handout #1: Summary of STOAT’s SIS File | 61 | `…/handout/forcing-handout-1-stoat-file` |

### Cadenza (Мэттью Сандерсон) — `…/scenario/cadenza`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул главы 3 | 62 | источник сценария (картинка — атмосфера) |
| Cadenza: эпиграф, Date, Location, Introduction | 63 | `summary` сценария |
| Briefing & Preparation; врезка CIA Agents; Keeper’s Note | 63–64 | сцена `cadenza-briefing` |
| Background / The Musician | 64–65 | `keeper_info`; `bryce-fredericks` |
| врезка Numbers Stations | 66 | место `numbers-station` |
| The Blackmailed Officer | 66 | `keeper_info`; `thomas-musgrave`, `burcin-uzun`, `aydin-dikmen`; предмет `musgrave-blackmail-photos` |
| врезка Mr Snow’s Goal | 67 | `…/character/mr-snow` (`legend`) |
| врезка Timeline of Events | 67 | таблица сценария «Хронология событий» |
| Journey & Arrival; N’s Note; врезка Listening to the Broadcasts | 68–69 | сцена `cadenza-journey-arrival`; раздатка `cadenza-handout-n-note`; предмет `numbers-station-a-tapes`; `victoria-fanshaw` |
| Reception | 69 | сцена `cadenza-reception`; предмет `kartal-polaroid` |
| Wing Commander Thomas Musgrave, Second in Command, Age 42 | 70 | `…/character/thomas-musgrave` |
| Group Captain George Knight, Base Commander, Age 50 | 70–71 | `…/character/george-knight` |
| LAC Louis Palmer, the Go-to Man, Age 35 | 71 | `…/character/louis-palmer` |
| врезка The Turkish Invasion of Cyprus | 71–72 | `history` места `limassol` |
| врезка Keeper Guidance | 72 | сцена `cadenza-reception`, `advice` |
| Limassol; Travel & Complications | 72 | сцена `cadenza-limassol-travel`, место `limassol` |
| Marina Bar-Café | 72–74 | сцена `cadenza-marina-bar-cafe`, место `marina-bar-cafe`, `ilias-marinos` |
| врезка The Conflict in Limassol | 73 | место `limassol` |
| Карта Лимасола | 73 | `…/map/limassol` |
| врезка Currency | 74 | место `limassol` |
| The Dikmen Gallery; Ground/First/Second Floor; Keepers Note | 74–75 | сцена `cadenza-dikmen-gallery`, место `dikmen-gallery`; предметы `uzun-charter-papers`, `dikmen-van-rijn-letters` |
| врезка Historical Note | 76 | `aydin-dikmen` (`legend`), предмет `saint-euphemianos-fresco` |
| Confronting Uzun | 76 | сцена `cadenza-confronting-uzun` |
| Burçin Uzun, Art Thief, Age 38 | 76–77 | `…/character/burcin-uzun` |
| RAF Akrotiri, The Airbase & Surrounding Area | 77–78 | место `raf-akrotiri`, `akrotiri-village`, `limassol-salt-lake` |
| Карта RAF Akrotiri (ключ 1–28) | 77 | `…/map/raf-akrotiri`; места ключа: `akrotiri-personnel-quarters` (1) … `fredericks-barracks` (28) |
| врезка Base Personnel & Procedures | 78 | место `raf-akrotiri` |
| SHQ | 78–79 | место `akrotiri-shq`, сцена `cadenza-shq` |
| Frederick’s Report | 79 | раздатка `cadenza-handout-fredericks-report` |
| Armoury | 80 | место `akrotiri-armoury`, сцена `cadenza-armoury` |
| Sergeants’ Mess | 80 | место `akrotiri-sergeants-mess`, сцена `cadenza-sergeants-mess`, `henry-carter` |
| Infirmary | 80–81 | место `akrotiri-infirmary`, сцена `cadenza-infirmary`; `lisa-sullivan`, `terrence-monahan`, `victoria-fanshaw`, `kenneth-hamilton` |
| The Numbers Station (журнал КПП) | 81–82 | место `numbers-station`, сцена `cadenza-numbers-station`, предмет `numbers-station-logbook` |
| План станции (ключ 1–10) | 81 | `…/map/numbers-station`; места `numbers-station-stores`, `numbers-station-generator-room`, `numbers-station-control-room` |
| Store Rooms, Kitchenette & Toilets / Generator Room / Main Control Room | 82 | места станции (выше) |
| Removing the “A” Tapes / Listening to the “A” Tapes | 82 | предмет `numbers-station-a-tapes` |
| Fredericks’ Barracks | 82–83 | место `fredericks-barracks`, сцена `cadenza-fredericks-barracks`; `crispin-ford`, `merritt-ellison`, `ronny-ibbott`; предмет `fredericks-theremin`; раздатки `cadenza-handout-alien-aria`, `cadenza-handout-lyra` |
| Questioning Sandford | 83 | сцена `cadenza-fredericks-barracks` |
| Corporal Reginald Sandford, RAF Communications Specialist, Age 29 | 83–84 | `…/character/reginald-sandford` |
| Questioning Howland | 84 | сцена `cadenza-questioning-howland` |
| Sergeant Emma Howland, RAF Intelligence Officer, Age 30 | 84–85 | `…/character/emma-howland` |
| Questioning Fredericks | 85 | сцена `cadenza-questioning-fredericks` |
| Corporal Bryce Fredericks, the Musician, Age 28 | 85–86 | `…/character/bryce-fredericks` |
| Refugees & Escalating Technical Problems | 86 | сцена `cadenza-refugees-technical-problems`; место `princess-marys-hospital` |
| Reporting to Knight | 86–87 | сцена `cadenza-reporting-to-knight` |
| Meeting Zann; врезка Recommended Reading | 87 | сцена `cadenza-meeting-zann` |
| Erich Zann, Musician of Azathoth, Apparent Age 60 | 88 | `…/character/erich-zann` |
| Tru’nembra, the Angel of Music (Other Characteristics, Banishment, Attacks, Abduction) | 88–90 | `…/creature/trunembra-cadenza` (`instance_of` `coc:creature:trunembra`) |
| врезка Optional Encounter: Servitors of the Outer Gods | 89 | сцена `cadenza-servitor` |
| Conclusions / Abductions Commence | 90 | сцена `cadenza-abductions-commence` |
| Sacrificing Fredericks / Converting the Mast | 90 | сцена `cadenza-sacrificing-fredericks`; место `numbers-station-generator-room` |
| Taking Fredericks’ Place | 91 | сцена `cadenza-taking-fredericks-place` |
| Banishing Tru’nembra | 91 | сцена `cadenza-banishing-trunembra` |
| The Court of Azathoth | 91–92 | сцена `cadenza-court-of-azathoth` (без места: записи места у Двора нет — см. ниже) |
| Cover Stories | 92 | `conclusion` сценария |
| Sanity & Trust Rewards | 92 | `conclusion` сценария |

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Картинки-атмосфера (обложка, титулы глав, паб, рука с деньгами, рот с иглами, папки «Top Secret», стопка брошюр) | 1, 4, 5, 7, 22, 27, 33, 38, 52, 62 | не привязаны к записи (Р-241) — `atmosphere-covert-a.json`; рисунок «Пнакотских игл» (с. 27) можно отдать заклинанию, но у вида `spell` нет `images` |
| Фоны врезок и колонтитулы (911×…, 1899×…, 2571×1145 и т. п.) | все | оформление; проверка полноты считает их «картинками без записи» — это ложные находки |
| Семья Ховенхэма (леди Миранда, Бруно, Элис, Бернадетт, Пол, Херман), жена и дочери Ефимова, жена и дети Масгрейва, отец Фредерикса, Янна и Афанасия Маринос, Мишель ван Рейн, агенты Хоровиц и Гриффин, мистер Хартман, соседка Фанмуров, старик из конторы проката, клерк проката машин, бельгийская пара и хозяева гостевого дома | 7–92 | упомянуты мимоходом без действий; сохранены текстом в записях родственников, мест и сцен |
| Достопримечательности у Акротири (монастырь Святого Николая Кошачьего, пляжи Черепаший и Леди-Майл, клуб ARABS), церковь в Лиси, стадион в Лимасоле, бар «Новар», ярмарка Линкс-Маркет, Беверидж-парк, тайник у тоннеля Ротерхит, абонентский ящик 93 | 9, 21, 73, 75, 77 | места без сцен и без пункта на карте — текстом в описаниях `raf-akrotiri`, `limassol`, `kirkcaldy`, сцен |
| Отдельная запись места «Двор Азатота» | 91–92 | место вне Земли нельзя поставить в дерево гайда (место без `part_of` — только город); описание — в сцене `cadenza-court-of-azathoth` |
| Названия на врезке карты Кипра (Никосия, Гирне, Ларнака, Пафос и др.) | 73 | в сценарии не участвуют; одна метка на врезку |

## Опечатки и сомнения книги (errata в записях)

- Уклонения и атаки с половиной, округлённой вверх (Вассидайн, Ховенхэм, Гуджон; нож Фанмур «50% (50/10)») — исправлены `pipeline/fix/percent_parts.py` (Р-35, `fixed: true`).
- Гуджон: ПМ 30 при МОЩ 10 («depleted») — как напечатано.
- Ховенхэм: Скорость 4 «(impaired)» — намеренно (протез), Р-76.
- Сенцова: атака «Pnatokus Quill» против заклинания «Pnakotus Quills».
- Раздатка 10 «Луж»: даты чемпионата «12th–19th July 1970», а в тексте финал — 12 июля.
- Ефимов: в статблоке 39 лет, в досье (раздатка) дата рождения 18.07.1942 и вербовка КГБ в 1954 году.
- «Хронология событий» (с. 36): поездка Ефимова с клубом дважды — 3 и 5 июля; «Главные события» (с. 53): 11-я партия дважды (6 и 8 августа; 8 августа — 12-я).
- Мортон: Скорость 9 при СИЛ = ТЕЛ (по правилам 8). Исландский полицейский: Скорость 8 (по правилам 7). Обычный горожанин: ПЗ 11 (12), Скорость 8 (7), Уклонение 27% ниже половины ЛВК 58.
- Хауленд: ПЗ 15 при ВЫН 65 и ТЕЛ 55 (по правилам 12).
- Бумаги о фрахте: «1,300 miles (2,902km)» — мили и км не сходятся.
- Станция чисел: в тексте одна кабинка туалета, на плане — три «1».
- Награды «Каденции»: две почти одинаковые строки «Providing an adequate report» с разными наградами (вероятно, во второй пропущено «inadequate»).
- Мелочи без errata (в `quality.notes`): «Ratmir»/«Ratimir» Захарин, «Terrence»/«Terence» Сомс, «Timoskin», «Losif» (Иосиф) Мамыкин, «b» вместо «Other Languages:» у Фредерикса (исправлено молча, Р-39), «Dikman Gallery», «RAF Akratori», «Frederik’s barrracks» на картах; номер 27 на карте Акротири отсутствует, а 28 стоит дважды.

## Термины (English → русский), выбранные в этой части

| English | Русский |
|---|---|
| Covert Actions (сборник) | «Тайные операции» |
| Puddles Become Lakes | «Лужи становятся озёрами» |
| Operation Puddle / Operation Lake | операция «Лужа» / операция «Озеро» |
| The Forcing Move | «Форсирующий ход» |
| Cadenza | «Каденция» |
| SIS | SIS (как у части cw-a; запись — «Секретная разведывательная служба (МИ-6)») |
| Section 46 | Секция 46 |
| Trust | Доверие |
| Tradecraft | Шпионское ремесло |
| Signals | Радиосвязь |
| Military Science | Военное дело |
| Command | Командование |
| Organisation Knowledge | Знание организаций |
| handler | куратор |
| safe house | убежище (ферма — «конспиративная ферма») |
| dead drop | тайник |
| honey trap / honeypot | «медовая ловушка» |
| numbers station | станция чисел |
| Lincolnshire Poacher | «Линкольнширский браконьер» |
| STOAT | ГОРНОСТАЙ |
| Brothers of the Yellow Sign | Братья Жёлтого знака (как в «Лохмотьях короля») |
| the Unspeakable One | Неизречённый |
| Great Race of Yith / Yithian | Великая Раса Йит / йитианин, йитианка |
| neural seed | нейронное семя |
| Enslavement to the Icterus | Желтушное рабство |
| Pnakotus Quills | Пнакотские иглы |
| Shining Word Publications / the Shining Word | издательство «Сияющее слово» / Сияющее слово |
| Dangerous Truths | «Опасные истины» |
| Drop Guise | Сбросить личину |
| Speak the Shining Word | Изречь Сияющее слово |
| Rending the Veil | срывая завесу |
| Tru’nembra, the Angel of Music | Тру'нембра, Ангел музыки |
| Court of Azathoth / Demon Sultan | Двор Азатота / Султан демонов |
| Servitor of the Outer Gods | служитель Внешних богов (как в общей записи) |
| RAF Police | военная полиция ВВС |
| SHQ (Station Headquarters) | штаб базы (SHQ) |
| Sergeants’ Mess | сержантская столовая |
| Group Captain / Wing Commander / LAC | групп-кэптен / винг-коммандер / ведущий авиатор |
| theremin | терменвокс |
| D-Notice | «Д-нотис» |
| Cod War | тресковая война |
| Lögreglan | Лёгреглан (исландская полиция) |
| Hard / Extreme roll | трудная / чрезвычайная проверка |
| penalty / bonus die | штрафной / бонусный кубик |
| bout of madness / delusion | приступ безумия / галлюцинация |

## Ссылки на записи других частей (общая схема линейки)

`wwc-cold-war-en/organization/{section-46,mi6,mi5,kgb,cia,fbi,nsa}`, `wwc-cold-war-en/character/{n,h}`,
`wwc-cold-war-en/location/{century-house,greene-club}` — уже существуют (часть cw-a).
Кандидаты без записи (текстом): организация «Братья Жёлтого знака» (основная книга, с. 115, 197 — часть cw-b),
заклинание «Contact Daoloth» (основная книга, с. 192 — часть cw-b), навыки линейки (Tradecraft, Signals,
Military Science, Command, Organisation Knowledge, Trust — часть cw-a): в статблоках они без `skill`.
