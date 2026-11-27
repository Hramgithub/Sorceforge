# Часть fez — «The Blood Red Fez: London 1893» (кн. II, с. 45–100, 240, 243–247)

Этап `hotoe-book-2-en/scenario/the-blood-red-fez` (order 3, необязательный, эпоха `gaslight`). Русский текст — наш перевод (Р-251, Р-21).
Генераторы и вырезки — `.cache/lead-tools/gen-hotoe-fez/` (g_chars, g_world, g_story, g_stage, g_props, g_newloc, g_art, maps_*,
handout_crop, art_crop). После перегенерации записей нужно снова применить `art-fez-proposals.json` (картинки).

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Blood Red Fez (заглавие), This Historical Scenario is Optional, Introduction | 45 | этап: `summary`, `advice` |
| Using this Scenario with the 1923 Campaign; Handouts for 1920s Investigators; As a Prequel | 46 | этап: `hook`, `advice` |
| About the Investigators | 46 | этап: `advice`; прегены (ниже) |
| London: Keeper's Information | 46–49 | этап: `keeper_info`; `organization/fez-children-of-the-blood-red-fez`; `character/hieronymus-menkaph`, `nisra` |
| The 1893 Diary: Introductory Handout | 47 | `handout/fez-handout-diary-introductory` |
| The 1893 Diary: Summary Handout | 47 | `handout/fez-handout-diary-summary` |
| About Fezzes (врезка) | 48 | этап: `advice` («О фесках») |
| The Young Professor Smith | 48 | этап: `advice`; предложение к `character/julius-smith` |
| Further Reading; Bibliographical Notes; Additional Thanks | 49 | этап: `advice`; прегены: `quality.notes` (создатели-тестеры) |
| Gaslight Handout #1 | 50 | `handout/fez-handout-1-message-from-professor-smith` |
| Investigators' Introduction | 50 | `scene/fez-investigators-introduction` |
| The Whitechapel Terror: To Durward Street, Outside Number 5, Inside Number 5, Smith's Story, What Smith Needs, The Man in the Fez | 50–53 | `scene/fez-whitechapel-terror`; `location/fez-durward-street`, `fez-lodging-house-durward-street`, `fez-room-of-the-withered-man`; `character/mrs-grim`, `niels-hobbs`, `matthew-pook` |
| The Blood Red Fez (врезка: Description, Writings, Touching, Wearing, Spells, Destroying) | 53 | `item/fez-blood-red-fez` (`description`, `mechanics`) |
| The Thing That Was Matthew Pook; Handling the Fez; After the Attack | 54–55 | `scene/fez-thing-that-was-matthew-pook`; `creature/fez-undead-servitor-of-the-blood-red-fez` |
| New Spell: Arrest Fez Decline | 54 | `coc:spell:arrest-fez-decline` (новая общая) |
| Fez Degeneration (Day One–Four) | 55 | `item/fez-blood-red-fez` (`mechanics`, «Деградация носителя фески») |
| The Oriental Club: Arriving at the Club, Smith's Request, Journey Proposal | 55–57 | `scene/fez-oriental-club-meeting` |
| About the Oriental Club (врезка; 1920s; Modern Era) | 56 | `location/fez-oriental-club` (`description`, `history`) |
| Gaslight Handout #2, #3 | 56–57 | `handout/fez-handout-2-demirs-first-telegram`, `fez-handout-3-demirs-recent-telegram` |
| London Investigations; Telegraphing Demir; Researching the Fez; The Whispering Fez | 57–58 | `scene/fez-london-investigations` |
| New Mythos Tome: Apocrypha of the Fez | 57 | `tome/fez-apocrypha-of-the-fez` |
| Gaslight Handout #4 | 58 | `handout/fez-handout-4-apocrypha-extracts` |
| The Whitechapel Garret | 58 | `scene/fez-whitechapel-garret`; `item/fez-translation-notes`, `fez-notepad-impression`, `fez-ferry-ticket-stubs` |
| The Fez Collector's Murder; Searching the House | 58–59 | `scene/fez-fez-collectors-murder`; `location/fez-devores-house`; `item/fez-devores-ledger`, `fez-leeds-letter`; `character/joshua-devore` |
| Gaslight Handout #5 | 59 | `handout/fez-handout-5-rotherhithe-fez-murder` |
| Bentley Burnham (врезка) | 59 | `character/bentley-burnham` |
| The Student's Lodgings; Monday Visit; Tuesday Visit; Searching the Lodgings | 60 | `scene/fez-students-lodgings`; `location/fez-pooks-flat`; `character/josiah-griggs` |
| Gaslight Handout #6 | 60 | `handout/fez-handout-6-pook-journal` |
| Researching the Allies: Professor Demir, Baron von Hofler | 60–62 | `scene/fez-researching-the-allies`; `character/professor-demir`, `leopold-von-hofler` |
| Children of the Blood Red Fez (врезка): The Cultist's Timetable, What the Cultists Want | 61 | этап: таблица «расписание культистов»; организация: `goals` |
| The Shoreditch Address | 62 | `scene/fez-shoreditch-address`; `location/fez-burnhams-rooms` |
| Preparing for the Trip; What if the Investigators Take a Later Train? | 62 | `scene/fez-preparing-for-the-trip` |
| The Journey: London to Chalons-sur-Marne; Burnham on Board; Châlons-sur-Marne | 62–63 | `scene/fez-london-to-chalons` |
| On Board the Orient Express | 63 | `scene/fez-day-one` (вступление) |
| Sleeping Car One: Paris to Constantinople | 63 | `location/fez-sleeping-car-one` |
| Henri Peeters, Conducteur; Henri in the Dreamlands | 63–64 | ссылка на `character/henri-peeters` (dreamlands) + предложение; этап: `advice` |
| (1)–(10) купе и пассажиры: Aileen Macgregor, Karla Minkoff, Egorov, Kapok, Scott Myers, Elizabeth Myers, Hieronymus Menkaph, Count Rudolph Razumosky, Countess Irina Razumosky, Pytor Trubosky | 64–66 | `location/fez-sleeping-car-one-compartments-1-3`, `…-compartment-4` … `-10`; персонажи (ниже) |
| Gaslight Handout #7 | 66 | `handout/fez-handout-7-letter-in-english` |
| Menkaph on the Train | 66–68 | `character/hieronymus-menkaph` (`legend`) |
| New Spells: Drain the Fez, Control Servant of the Blood Red Fez, Spawn Fez, Favorite of Yog-Sothoth, Control the Fez | 67 | `coc:spell:drain-the-fez`, `control-servant-of-the-blood-red-fez`, `spawn-fez`, `favorite-of-yog-sothoth`, `control-the-fez` (новые общие) |
| Gaslight Handout #8 | 68 | `handout/fez-handout-8-whispering-fez-extracts` |
| New Mythos Tome: The Whispering Fez | 68 | `tome/fez-the-whispering-fez` |
| Day One (Wednesday): Timetable, Boarding, Midnight Shadows | 69 | `scene/fez-day-one` |
| Day Two (Thursday): Timetable, Morning, Breakfast, Lunch, Afternoon, Vienna, Baron von Hofler, Before Belgrade: The Baron's Daughter, 11:00 P.M. Budapest, More Midnight Shadows | 69–72 | `scene/fez-day-two`; `character/ilsa-von-hofler`, `leopold-von-hofler` |
| Карта Константинополя в тексте главы | 71 | `map/fez-gaslight-constantinople` (источник) |
| Day Three (Friday): Timetable, Belgrade, Breakfast, Final Midnight Shadows; What if the Investigators Get Everything? | 72–73 | `scene/fez-day-three` |
| Day Four (Saturday): Final Morning; Constantinople: Arriving in Constantinople | 73 | `scene/fez-day-four-arrival` |
| Ottoman Constantinople (врезка: история, Accommodation, Currency, Guns and Goods, Dogs, Getting Around) | 74–75 | этап: таблица «Константинополь 1893: жильё, деньги, транспорт»; предложения к `coc:location:constantinople` (абзац эпохи и история) и к местам WWC |
| The Professor's Children | 75 | `scene/fez-day-four-arrival`; `character/toprak-demir`, `rana-demir` |
| Professor Demir's House; The Kidnap; The Book; Children of the Blood Red Fez; Nisra, Daughter of Fate; The Blood Red Fez; Selim Makryat | 75–76 | `scene/fez-professor-demirs-house`; `location/fez-demirs-house`; `item/fez-kidnap-note`; `character/selin-demir` |
| Research; The Imperial Treasury; The Imperial Museum of Antiquities; Museum of Ancient Costume; Possible Information | 76–77 | `scene/fez-research-in-constantinople`; `location/fez-imperial-treasury`, `fez-imperial-museum-of-antiquities`, `fez-museum-of-ancient-costume` |
| The Final Section of the Whispering Fez | 77 | `scene/fez-professor-demirs-house`; `tome/fez-the-whispering-fez` |
| Visiting the Frenchman | 77–78 | `scene/fez-visiting-the-frenchman`; `location/fez-frenchmans-residence`; ссылка на `character/jean-floressas-des-esseintes` + предложение |
| The Brothers of the Skin; Selim Makryat | 78–79 | `scene/fez-brothers-of-the-skin`; `location/fez-selim-makryats-fort`; предложения к `coc:organization:brothers-of-the-skin`, `character/mehmet-makryat` |
| The Sultan; The Palace | 79 | `scene/fez-the-sultan`; `location/fez-sultans-palace` |
| The British Consul | 79 | `scene/fez-british-consul`; `location/fez-british-consulate` |
| The Kidnap Exchange: The Arrangements, The Kidnappers' Trip from the Island, Meeting at the Shipping Yard | 79–80 | `scene/fez-kidnap-exchange`; `location/fez-kasim-pasha-shipyards`; `character/nine-fingered-abdullah` |
| Карта острова Нисры в тексте главы | 80 | `map/fez-nisras-island` (источник) |
| The Island of Doomed Princes: Princes' Islands, Getting to the Island, On the Island, The Cultists' Tower, Nisra, the Daughter of Fate, The Doomed Prince | 80–81 | `scene/fez-island-of-doomed-princes`; `location/fez-princes-islands`, `fez-island-of-doomed-princes`, `fez-cultists-tower`, `fez-tower-ground-floor`, `fez-tower-top-floor` |
| The Final Ritual; Destroying the Fez | 81–82 | `scene/fez-final-ritual` |
| Conclusion (награды Рассудком); Forward to 1923 | 82 | этап: `conclusion`, таблица «награды Рассудком» |
| New Spell: Destroy the Fez | 83 | `coc:spell:destroy-the-fez` (новая общая) |
| Gaslight on the Orient Express: The Orient Express in Victorian Times | 83, 85 | `location/fez-orient-express-1893` (`history`); `rule/fez-gaslight-on-the-orient-express` |
| Gaslight Era Timeline (врезка) | 84 | `rule/fez-gaslight-on-the-orient-express` — таблица «Хронология эпохи газового света» |
| The Pera Palace (иллюстрация) | 84 | `atmosphere-fez.json`; предложение к `wwc-cold-war-en/location/pera-palas-hotel` |
| Boarding the Express: Preparation and Booking, Advice on Travel | 85 | правило `text`; поезд `description` (цены) |
| On Board the Express: Train Configuration, The Order of Cars, Carriage Construction, Compartments and Fittings, Interior Design, Train Times, Departure Point | 85–86 | `location/fez-orient-express-1893` (`description`); вагоны `fez-sleeping-car-one`, `fez-sleeping-car-two`, `fez-restaurant-car`, `fez-salon-car`, `fez-fourgons` |
| Timetable (Paris–Constantinople, Constantinople–Paris) | 86–87 | поезд: две таблицы расписаний; этап: ссылка `from` |
| Towns and Stations En Route: Paris, Châlons-sur-Marne, Strasbourg, Stuttgart, Ulm, Münich, Salzburg, Vienna, Budapest, Belgrade, Nisch, Sofia, Constantinople | 87–90 | поезд: таблица «города и станции по пути»; предложения к `coc:location:paris`, `vienna`; черновики городов — `new-shared-locations-fez.json` (+ абзацы для Белграда, Софии, Кале) |
| Other Considerations: Telegraph — the Victorian Email; Further Reading | 90 | `rule/fez-gaslight-on-the-orient-express` |
| Statistics: Paris-Constantinople Train Passengers | 91–92 | `character/rudolph-razumosky`, `irina-razumosky`, `karla-minkoff`, `egorov`, `pytor-trubosky`, `aileen-macgregor`, `scott-myers`, `elizabeth-myers` |
| Villains and Thugs En Route | 92–93 | `character/hieronymus-menkaph`, `kapok`, `menkaphs-thugs`, `menkaphs-fez-servants`, `bentley-burnham` |
| The Yatagan (врезка) | 93 | ятаган = `coc:weapon:sword-light` (1d6, Ближний бой (меч)) в атаках; текст врезки — `quality`/описания культистов не нужен, см. «Не взято» |
| Second Sleeping Car Passengers | 93 | `character/ilsa-von-hofler`, `leopold-von-hofler` |
| Monsters and Other Entities: Shadow Spawn, Undead Servitors | 93–94 | `creature/fez-shadow-spawn-of-the-blood-red-fez`, `fez-undead-servitor-of-the-blood-red-fez` |
| New Spells: Shadow Void | 94 | `coc:spell:shadow-void` (есть, Grand Grimoire) — предложение: источник и расхождение |
| Ottoman Constantinople (статистика) | 95–97 | `character/professor-demir`, `barlas-demir`, `toprak-demir`, `rana-demir`, `turkish-policeman-1893`, `blood-red-fez-cultists`, `fez-servant-cultists`, `turkish-sailors-1893`, `nisra`, `prince-ramazan`, `ulug` |
| New Spells: Dance of the Gelin; Golden Cage of Desire | 96 | `coc:spell:dance-of-the-gelin` (новая); `coc:spell:golden-cage-of-desire` (есть) — предложение |
| Investigators: Harold Worth, Roderick Barrington, George Banks, Amelia Meadowcroft, Kasim Polat, Jean-Louis Saroch | 97–100 | `character/harold-worth`, `roderick-barrington`, `george-banks`, `amelia-meadowcroft`, `kasim-polat`, `jean-louis-saroch` (роль `pregen`) |
| Durward Street (план) | 50, 240; VI 59 | `map/fez-durward-street` |
| Gaslight London Keeper's Map / Players' Map | 51, 243–244; KM 2; VI 61 | `map/fez-gaslight-london`, `fez-gaslight-london-players` |
| Gaslight Constantinople Keeper's Map / Players' Map | 71, 245–246; KM 17; PM 12; VI 63 | `map/fez-gaslight-constantinople`, `fez-gaslight-constantinople-players` |
| Nisra's Island | 80, 247; VI 65 | `map/fez-nisras-island` |
| Раздатка Книги VI | VI 21–27 | картинки раздаток (`images`, вырезки — `.cache/lead-tools/gen-hotoe-fez/handout-boxes.json`) |

Места 1893 года без ключа карты: `fez-hotel-meurice` (Париж), `fez-sleeping-car-*`. Ключи карт Константинополя 2, 4, 5 и подписи районов ведут на места WWC
(Гранд-базар, Святая София, Голубая мечеть, Фатих, Бейоглу, Ускюдар, Эюп, Золотой Рог, Босфор), Лондона 1, 2, 7, 10 — на места части london
(`london-imperial-institute`, `london-victoria-and-albert-museum`, `london-university-of-london`, `london-smiths-house`), 3, 4, 5 — на
`coc:location:houses-of-parliament`, `coc:location:british-museum`, `masks-of-nyarlathotep-en/location/england-new-scotland-yard`.

## Не взято

- Иллюстрации-атмосфера (вокзал Константинополя с. 72, «Пера Палас» с. 84, пивоварня «Лёвенброй» с. 88, Лионский вокзал с. 100) и оформление
  (врезки с рельсами/паровозом, газетная заставка «Man Dies Three Times» на полях) — `atmosphere-fez.json`.
- Серые фоны врезок (completeness `art.uncovered` на с. 48, 55, 57–63, 67–68, 72, 74–75, 93, 96, 100) — подложки врезок, не картинки.
- «Additional Thanks» (с. 49): благодарности Даррену Уотсону и бэкерам Kickstarter — не взяты; создатели прегенов — в `quality.notes` прегенов.
- Врезка «The Yatagan» (с. 93): описание оружия (тонкий турецкий меч, «уши» на навершии, без гарды, ножны из дерева и бархата, носят за поясом;
  1d6, Ближний бой (меч)) — в справочник оружия не внесено (там есть «Меч лёгкий», те же числа); кандидат в `source_variants`/новую позицию — вопрос владельцу.
- Портрет Смита 1893 года (с. 49) — запись не моя: картинка сделана (`app/art/characters/hotoe-fez-julius-smith-1893-2.webp`), добавление — в `proposals-fez.json`.

## Опечатки и сомнения

- Капок: возраст 42 (с. 65) и 50 (статблок, с. 92) — `errata`.
- Комплекция: «рабы фески» Менкафа и культисты-рабы фески — 1 при СИЛ+ТЕЛ 190–195 (по правилам 2); проф. Уорт — 1 при 95 (по правилам 0) — `errata`.
- Скорость: громилы Менкафа 9 (по правилам 8), принц Рамазан 7 (по правилам 8) — `errata`. Топрак: ПЗ 11 (по правилам 12) — `errata`.
- Половины процентов: граф Разумоский «40% (22/8)» ×3, Рамазан «Dodge 27% (14/5)» — исправлено по Р-35, `errata`.
- Егоров: Уклонение 34% в навыках и 35% в бою. Культисты-рабы фески: Рассудок 50 (у рабов Менкафа 0).
- Урон выше табличного: Бернем «.22 Revolver 1D8», Амелия «41 Revolver 1D10+4», Улуг «Scimitar 1D4+1D6» — `errata`, как напечатано.
- Касым Полат: шрам «от автомобильной аварии» в 1893 году — анахронизм, `errata`.
- Обратное расписание: «Ulm 7:41am» между 17:23 и 21:14 — вероятно 19:41; Будапешт «образован в 1872 году объединением четырёх городов» — `errata` поезда.
- Заклинание: «Favorite of Yog-Sothoth» (статья) и «Favored of Yog-Sothoth» (список книги, Нисра) — второе в `aliases`.
- «Destroy the Fez» нет в списке заклинаний «Шепчущей фески», но по тексту учится только из её иероглифической части — добавлено (Р-41).
- Keeper Maps 2 (London 1893): ключ и номера не сходятся с текстом и с картой книги (с. 243) — картинка и метки по с. 243.
- Keeper Maps 17: «13. Professor Ahmed's House», «12. Thomas Cook & Sons» (в книге — Demir's House, Thomas Cook & Son).
- Отель «Де Бизанс»: текст — в Пере (с. 74), на карте № 3 — в Стамбуле у Сиркеджи.
- Француз отсылает слуг «на юг, к Мраморному морю… на запад, к Скутари» — Скутари к востоку; как напечатано.
- Взятие Константинополя османами — «1452» (с. 74), исторически 1453; в предложении к городу — «(в книге — 1452 год)».
- Дневник Пука: Демир назван «K.H Demir» только в подписи раздатки (с. 47).

## Ожидаемые ссылки на записи других частей (ошибки check.py до их сведения)

- `hotoe-book-4-en/character/selim-makryat` (constantinople) — 10 ссылок; абзац о Селиме 1893 года для его записи: «В 1893 году
  („Кроваво-красная феска“, кн. II, с. 76–79): глава Братьев кожи в древнем форте в Скутари (там около половины времени); ставит опыты со
  сдиранием кожи с людей; насторожен, держит Братьев наготове, на всякий случай под заклинанием „Кожа Седефкара“ (броня 10); не любит Нисру
  (не терпит женщин с оккультной властью) и помогает только её противникам — рассказывает об Острове обречённых принцев и о культе Нисры
  (около пятидесяти); бывший союзник Менкафа по культу Бескожего; Смит выступил против него в Турции и не может вернуться на Восток». Источник — кн. II, с. 78.
- `hotoe-book-4-en/location/constantinople-sirkeci-station` (constantinople) — 3 ссылки (метка 1 обеих карт, сцена прибытия). Описание 1893
  года (с. 73): новый величественный вокзал (1890), нечто среднее между мечетью и викторианским вокзалом, творение прусского архитектора,
  классика европейского ориентализма; багаж идёт в железнодорожную таможню и персоналу «Вагон-Ли».
- `coc:location:belgrade`, `coc:location:sofia` — строки таблицы городов поезда; абзацы 1893 года — `new-shared-locations-fez.json` → `additions`.

## Термины (английский → русский)

| English | Русский |
|---|---|
| The Blood Red Fez | Кроваво-красная феска (артефакт; «Феска» с заглавной) |
| Fez / fezzes | феска / фески |
| Fez wearer / Fez Controller / Control Fez | носитель фески / управитель фески / управляющая феска |
| Master of the Fez | повелитель фески |
| Fez Degeneration | деградация носителя фески |
| Servant of the Blood Red Fez / Fez Servants | раб Кроваво-красной фески / рабы фески |
| Shadow Spawn of the Blood Red Fez | теневое отродье Кроваво-красной фески |
| Undead Servitors of the Blood Red Fez / Fez Zombie | неупокоенный слуга Кроваво-красной фески / зомби фески |
| Lesser Servitor Race | младшая раса слуг |
| Children of the Blood Red Fez | Дети Кроваво-красной фески |
| Apocrypha of the Fez / The Whispering Fez | «Апокрифы фески» / «Шепчущая феска» |
| Arrest Fez Decline / Spawn Fez / Drain the Fez | Остановить угасание фески / Породить феску / Осушить феску |
| Control Servant of the Blood Red Fez / Control the Fez / Destroy the Fez | Подчинить раба Кроваво-красной фески / Власть над феской / Уничтожить феску |
| Favorite (Favored) of Yog-Sothoth / Dance of the Gelin | Любимец Йог-Сотота / Танец гелин |
| Shadow Void / Golden Cage of Desire | Пустота тени / Золотая клетка желания (есть в базе) |
| Father of Sorcerers | Отец чародеев |
| Nisra the Daughter of Fate | Нисра, Дочь Судьбы |
| The Frenchman / The Jigsaw Prince | Француз / Принц-Головоломка |
| The Island of Doomed Princes / Princes' Islands (Kizil Adalar) | Остров обречённых принцев / Принцевы острова (Кызыл Адалар) |
| Gaslight Handout #N | «Газовый свет» № N |
| Cthulhu by Gaslight / Gaslight era | «Cthulhu by Gaslight» / эпоха газового света |
| conducteur / Chef de Train / Wagons-Lits (CIWL) | кондуктор / начальник поезда / «Вагон-Ли» (Международная компания спальных вагонов, CIWL) |
| sleeping car / restaurant car / salon car / fourgon | спальный вагон / вагон-ресторан / вагон-салон / фургон (багажный вагон) |
| Stamboul / Pera / Galata / Scutari / Golden Horn / Bosporus | Стамбул (старый город) / Пера / Галата / Скутари / Золотой Рог / Босфор |
| Sirkeci Station / Kasim Pasha / Sea of Marmara | вокзал Сиркеджи / Касымпаша / Мраморное море |
| Old Seraglio / Imperial Treasury / Imperial Museum of Antiquities / Museum of Ancient Costume | Старый сераль / Императорская сокровищница / Императорский музей древностей / Музей старинного костюма |
| Imperial Warrant / travel permit | императорский фирман / путевой билет |
| dragoman / caïque / yatagan / piastre (gurush) / lira | драгоман / каик / ятаган / пиастр (куруш) / лира |
| Black Eunuch / harem girl | чёрный евнух / девушка из гарема |
| Dashnaks / Armenian Question | дашнаки / «армянский вопрос» |
| Oriental Club / Board School | Восточный клуб / бесплатная школа для бедных |
| Durward Street (Bucks Row) / Whitechapel / Shoreditch / Rotherhithe / Lambeth / St John's Wood / Blithering Lane / Hanover Square | Дарвард-стрит (Бакс-роу) / Уайтчепел / Шордич / Ротерхит / Ламбет / Сент-Джонс-Вуд / Блитеринг-лейн / Ганновер-сквер |
| Châlons-sur-Marne / Strasbourg / Münich / Vienna Westbahnhof / Staatsbahnhof / Nisch | Шалон-сюр-Марн / Страсбург / Мюнхен / Вена, Западный вокзал (Вестбанхоф) / Государственный вокзал (Штатсбанхоф) / Ниш |
| Hotel Meurice / Hotel de Byzance / Hotel Belle Vue / Hotel d'Angleterre (Misseri's) / Thomas Cook & Son | отель «Мёрис» / «Де Бизанс» / «Бельвю» / «Д’Англетер» (Миссери) / «Томас Кук и сын» |
| Hieronymus Menkaph (Mortimer Leeds) / Kapok / Bentley Burnham | Иеронимус Менкаф (Мортимер Лидс) / Капок / Бентли Бернем |
| Count Rudolph / Countess Irina Razumosky / Pytor Trubosky / Karla Minkoff / Egorov | граф Рудольф Разумоский / графиня Ирина Разумоская / Пётр Трубоский / Карла Минкофф / Егоров |
| Aileen Macgregor / Scott Myers / Elizabeth ‘Ellie’ Myers | Эйлин Макгрегор / Скотт Майерс / Элизабет «Элли» Майерс |
| Baron Leopold / Ilsa von Hofler | барон Леопольд / Ильза фон Хофлер |
| Professor K. H. Demir / Selin / Toprak / Rana / Barlas | профессор К. Х. Демир / Селин / Топрак / Рана / Барлас |
| Nine-Fingered Abdullah / Prince Ramazan / Ulug / Sehdi Bey | Девятипалый Абдулла / принц Рамазан / Улуг / Сехди-бей |
| Matthew Pook / Mrs. Grim / Dr. Niels Hobbs / Joshua Devore / Josiah Griggs / Inspector Kendall | Мэтью Пук / миссис Грим / доктор Нильс Хоббс / Джошуа Девор / Джосайя Григгс / инспектор Кендалл |
| Harold ‘Harry’ Worth / Roderick Barrington, Bart. / George Banks / Amelia Meadowcroft / Kasim Polat / Jean-Louis Saroch | Гарольд «Гарри» Уорт / Родерик Баррингтон, баронет / Джордж Бэнкс / Амелия Медоукрофт / Касым Полат / Жан-Луи Сарош |
| Selim / Mehmet Makryat | Селим / Мехмет Макрьят |
| Henri Peeters | Анри Петерс |
| Thrash Serf / Disdain Inferiors / Blackmail / Politics | Порка крепостных / Презрение к низшим / Шантаж / Политика (навыки без механики, Р-126) |

Расхождение форм: запись `henri-peeters` (часть dreamlands) называет главу «Кровавая феска»; здесь — «Кроваво-красная феска» (вопрос сведения).
Фамилию Makryat другие части могут писать иначе (здесь — «Макрьят»).
