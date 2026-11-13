# «Аркхэм» (arkham-en), часть downtown — Даунтаун, места 200–299 (физ. с. 96–114)

Источник — `arkham-en` (печатные с. 95–113), планы и карта — `arkham-maps-en` (с. 5, 18, 19). Перевод наш (флаг `translated`).
Места — `kb/locations/arkham-2NN-*.json` (`part_of` = `coc:location:arkham-downtown`), люди — `kb/books/arkham-en/characters/downtown-*.json`,
карты — `kb/books/arkham-en/maps/downtown-*.json` + `app/maps/arkham-downtown-*.jpg`, правки общих записей — `proposals-downtown.json`.

## Заголовки книги → база

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Neighborhood 2: Downtown, 200–299 (вступление района) | 95 | `coc:location:arkham-downtown` (запись части overview, текст вступления уже там) |
| 201 Pickering Psychopathic Hospital: Historical, Notable Folk, Cure Rate, Look to the Future | 95 | `coc:location:arkham-sanitarium` (тот же адрес, 225 E Derby Street) — предложения: `number` 201, `part_of`, псевдонимы, описание, `history`, источники, жители; люди: `downtown-eric-hardstrom`, `downtown-bradley-harcourt`, `downtown-sophronia-harker`, `downtown-john-ronayne`, `downtown-eric-sykes`, `downtown-michal-symanski` |
| Floorplans of the hospital (pages 98 and 99) | 98–99; maps-en 18–19 | `arkham-en/map/downtown-pickering-1` (первый этаж, подвал), `arkham-en/map/downtown-pickering-2` (второй, третий этажи); картинки `app/maps/arkham-downtown-pickering-1.jpg`, `-2.jpg` |
| 202 Fleetwood Diner: Notable Folk, Strangeness | 95, 97 | `coc:location:arkham-202-fleetwood-diner`; `downtown-ollie-weaver`, `downtown-mei-yang` |
| Карта «Arkham Neighborhood Downtown», Points of Interest | 96; maps-en 5 | `arkham-en/map/downtown-neighborhood` (`app/maps/arkham-downtown-neighborhood.jpg`), метки 201–245 + заголовок района |
| 203 Innsmouth Bus Stop: Notable Folk | 97 | `coc:location:arkham-203-innsmouth-bus-stop` (расписание и цены — пункты описания); `downtown-joe-sargent` |
| 204 Dr. Heinrich T. Muelhig, Psychiatrist: Cure Rate, Strangeness; статблок | 97 | `coc:location:arkham-204-dr-muelhig-psychiatrist`; `downtown-heinrich-muelhig` |
| 205 Kenneth Heath, Private Investigator; The Case; статблок | 97, 100 | `coc:location:arkham-205-heath-private-investigation`; `downtown-kenneth-heath` |
| 206 Rotary Club: Benefits | 100 | `coc:location:arkham-206-rotary-club` (правило членства — в описании) |
| 207 Dr. G. Sinderwald, Reconstructive Surgeon: Shady Business; статблок | 100–101 | `coc:location:arkham-207-dr-sinderwald-surgeon`; `downtown-garrison-sinderwald` |
| 208 Asbury Methodist-Episcopal Church: Notable Folk, Beliefs | 101 | `coc:location:arkham-208-asbury-methodist-episcopal-church`; `downtown-ezekiel-wallace` |
| 209 Diamond Credit Agency: Notable Folk, Strangeness | 101 | `coc:location:arkham-209-diamond-credit-agency`; `downtown-randle-wade` |
| 210 Bee’s Diner: Notable Folk | 101 | `coc:location:arkham-210-bees-diner`; `downtown-helen-bee`, `downtown-pete-bee`, `downtown-agnes-bee` |
| 211 Arkham Public Library: Notable Folk, Useful | 102 | `coc:location:arkham-211-public-library` (ссылка на `coc:tome:azathoth-and-others`); `downtown-adelbert-vine`, `downtown-ellen-whitmarsh`, `downtown-ivie-rea` |
| 212 Courthouse & Jail: Useful, Before the Judge, Notable Folk | 102 | `coc:location:arkham-212-courthouse-and-jail`; `downtown-keezar-randall`, `downtown-lee-craig`, `downtown-edwin-cassidy` |
| 213 Telenews Cinema: Notable Folk, Strangeness | 102–103 | `coc:location:arkham-213-telenews-cinema`; `downtown-reginald-gainor`, `downtown-sally-waite` |
| Врезка «Films of the Twenties» | 103 | таблица «Фильмы двадцатых» в `coc:location:arkham-213-telenews-cinema` (на неё ссылается 225) |
| 214 Arkham First Bank: Notable Folk | 103 | `coc:location:arkham-214-arkham-first-bank`; `downtown-royce-merriam`, `downtown-william-danvers-johnson` |
| 215-A Bertrand Chambers, Attorney-at-Law | 103 | `coc:location:arkham-215-a-bertrand-chambers-attorney`; `downtown-bertrand-chambers` |
| 215-B Federal Bond Agency | 104 | `coc:location:arkham-215-b-federal-bond-agency`; `downtown-leverette-hewes` |
| 216 Massachusetts Guard Armory: Armory, Notable Folk, Look to the Future | 104 | `coc:location:arkham-216-massachusetts-guard-armory` (опись хранилища — пункты); `downtown-william-hathorne`, `downtown-aubrey-bridgeton`, `downtown-charles-hart`, `downtown-stephen-groat` |
| Таблица «Armory Weapons» | 105 | таблица «Оружие арсенала» в записи 216 (строки ссылаются на `coc:weapon:*`); расхождение штыка — предложение `source_variants` для `coc:weapon:bayonet` |
| 217 Town Hall: Mayor’s Office, Public Room, Town Manager’s Office (Secret), Assessor’s Office, Clerk’s Office, Engineer’s Office, School Board, Water Department | 104–105 | `coc:location:arkham-217-town-hall`; `downtown-joseph-peabody`, `downtown-darrell-slocum`, `downtown-marla-slocum`, `downtown-janet-larkin`, `downtown-walt-wednesday`, `downtown-bill-kent` |
| 218 Independence Square (The Common): Events | 105 | `coc:location:arkham-218-independence-square` |
| 219 Crawford’s Restaurant: Notable Folk, Strangeness | 105 | `coc:location:arkham-219-crawfords-restaurant`; `downtown-chesley-shattuck` |
| 220 Art’s Billiards: Notable Folk, Useful | 105–106 | `coc:location:arkham-220-arts-billiards`; `downtown-arthur-smedley`, `downtown-sammy-blithe` |
| 221 Demolition Site: Strangeness | 106 | `coc:location:arkham-221-demolition-site` |
| 222 Arkham Gas Company: Notable Folk | 106 | `coc:location:arkham-222-arkham-gas-company`; `downtown-marvin-wellman` |
| 223 Arkham Bell Telephone: Who’s Listening?, Party Lines, Notable Folk | 106 | `coc:location:arkham-223-arkham-bell-telephone`; `downtown-mildred-heminger`, `downtown-virginia-ozanich` |
| 224 Arkham Trolleys | 106 | `coc:location:arkham-224-arkham-trolleys` (три линии — пункты описания) |
| 225 Amherst Theater: Notable Folk | 106–107 | `coc:location:arkham-225-amherst-theater`; `downtown-sam-whitlocke`, `downtown-george-whitlocke` |
| 226 Dennison’s Ice Cream Emporium: Notable Folk | 107 | `coc:location:arkham-226-dennisons-ice-cream-emporium`; `downtown-bill-pleasant` |
| 227 Northside Market: Notable Folk | 107 | `coc:location:arkham-227-northside-market`; `downtown-robert-czyenck` |
| 228 Arkham Police Station: Notable Folk, Cells, Firearms, Corruption; статблоки Хардена, Харригана, Стаки | 107–108 | `coc:location:arkham-228-police-station`; `downtown-asa-nichols`, `downtown-william-keats`, `downtown-luther-harden`, `downtown-mickey-harrigan`, `downtown-calvin-stuckey` |
| 229 US Post Office: Notable Folk | 108 | `coc:location:arkham-229-post-office`; `downtown-eli-whittaker` |
| 230 Fire Department: Notable Folk | 109 | `coc:location:arkham-230-fire-department`; `downtown-benijah-adams` |
| 231 First National Grocery Store: Notable Folk, Strangeness | 109 | `coc:location:arkham-231-first-national-grocery`; `downtown-arthur-anderson` |
| 232 Ballard’s Auto Lot: Driving Lessons, Notable Folk | 109 | `coc:location:arkham-232-ballards-auto-lot` (правило уроков вождения — абзац описания); `downtown-grainger-ballard`, `downtown-alasdair-crooke`, `downtown-robby-weiss` |
| Врезка «Arkham Auto Prices» | 109 | таблица «Цены на автомобили в Аркхэме» в записи 232 |
| 233 Edison Electric & Gas: Useful, Notable Folk | 109–110 | `coc:location:arkham-233-edison-electric-and-gas`; `downtown-francis-eckhardt` |
| 234 Miskatonic Valley Savings Bank: Notable Folk | 110 | `coc:location:arkham-234-miskatonic-valley-savings-bank`; `downtown-howard-filbert` |
| 235 MassGas Station: Notable Folk | 110 | `coc:location:arkham-235-massgas-station`; `downtown-abel-sykes` |
| 236 Arkham Cab Co.: Notable Folk, Useful | 110–111 | `coc:location:arkham-236-arkham-cab-co`; `downtown-gregory-dahlberg`, `downtown-sheila-crownover`, `downtown-pawl-sawicki` |
| 237 Bunden’s Bindery: Notable Folk, Strangeness | 111 | `coc:location:arkham-237-bundens-bindery`; `downtown-malcolm-bunden` |
| 238 Painless Tattoos: Notable Folk, Secret, Strangeness; статблок Jin-Pin Liou (a.k.a Louis Pinelli) | 111–113 | `coc:location:arkham-238-painless-tattoos`; `downtown-jin-pin-liou` (заклинания — ссылки на `coc:spell:*`) |
| 239 Sheehan Contractor Supply: Notable Folk | 113 | `coc:location:arkham-239-sheehan-contractor-supply`; `downtown-ed-sheehan` |
| 240 Happy Bee Construction Co.: Notable Folk | 113 | `coc:location:arkham-240-happy-bee-construction`; `downtown-lee-kalosh` |
| 241 Penny Arcade: Notable Folk | 113 | `coc:location:arkham-241-penny-arcade`; `downtown-mal-greene` |
| 242 Railroad Properties | 113 | `coc:location:arkham-242-railroad-properties` (отсылка к 140 — текстом) |
| 243 Adams Lumber Yard: Notable Folk | 113 | `coc:location:arkham-243-adams-lumber-yard`; `downtown-steve-monk` |
| 244 Slaughterhouse: Notable Folk, Strangeness | 113 | `coc:location:arkham-244-slaughterhouse`; `downtown-barry-oconnor` |
| 245 Trolley Sidings | 113 | `coc:location:arkham-245-trolley-sidings` |

Итого: мест 44 новых + 1 общее по предложениям (201); персонажей 73 (7 со статблоком); карт 3; предложений 21.

## Не взято

- Портреты (Мюлиг, Хит, Синдервальд, Эллен Уитмарш, судья Рэндалл, мэр Пибоди, начальник Николс, Харден, Харриган, Стаки, Лиу) и иллюстрации «First National Grocery Store» (с. 110), «Special Bindings for Special Books» (с. 112), фасады больницы на планах — картинки кладутся в `app/art/` через `pipeline/art/add_images.py`, это вне файлов части; оставлено ведущему. — сделано (коммит `207f20a`).
- Карта района на с. 96 и планы больницы на с. 98–99 книги — те же листы взяты из `arkham-maps-en` (с. 5, 18, 19), книжные страницы — вторым источником в картах.
- Упомянутые без описания люди — без своих записей, текстом в местах: жена Хита Мадлен, ушедший на покой библиотекарь Джаспар Уиппл, жена Николса Орретт, жена Андерсона Роуз, генерал Шеридан (табличка в «Кроуфордс»), призрак «Рыжая Мэри», безымянные: 12 медсестёр и санитаров больницы, три доставщика газовой компании, три работника лесного склада, переплётчик и помощник Бандена, отвергнутый художник, ежемесячная гостья Пинелли, юноша без памяти (1922, «Праздник»).
- Люди и места других районов, упомянутые здесь (Бобби Силлс с. 129, Дэнни О’Баннион и «Лаки Кловер Картадж» 412, Э. Э. Солтонстолл-старший 125, Бартоломью Эпли IV 103, Tower Professional Building 119, Железнодорожные владения 140, клуб «Мискатоник» 804, Дом семьи Дерби 818, Аркхэмское историческое общество 901, «Скалы» 717, «Финны» 517, театр «Мэнли» 106, масоны 108, Торговая палата 127, рынок Бенсона 448, станция Фрэнка 413, газетный киоск 437-A, госпиталь Св. Марии 626, отель «Мискатоник» 634, кафедра английского языка 614-A, библиотека Орна 623, Аркхэмский оружейный клуб с. 132, Аркхэмский ковен с. 51) — текстом с номером: их записи заводят другие части; ссылки может поставить сведение. — сделано (сведение, коммит `bccc379`; 614-A у переплётной — уборка 2026-11-14, `checks/20261114-tidy.md`).
- Организации: Ротари-клуб, полиция Аркхэма, рота B Национальной гвардии, Аркхэмский ковен — отдельными записями не заведены: клубы и ковен — у части overview, остальное полностью в записях мест.

## Кандидаты на слияние (Р-154)

| Запись другой книги | Общая запись путеводителя |
|---|---|
| `naedine-s-tmoy-ru/location/arkham-zakusochnaya-pchela` (Bees Diner) | `coc:location:arkham-210-bees-diner` |
| `naedine-s-tmoy-ru/location/arkham-pervyy-natsionalnyy-bank` (Arkham First National Bank) | возможно `coc:location:arkham-214-arkham-first-bank` (название другое — сомнение) |
| `bless-the-beast-and-children-ru/location/arkham-keb` | `coc:location:arkham-236-arkham-cab-co` |
| `bless-the-beast-and-children-ru/location/upravlenie-arkhemskogo-tramvaya` (южная сторона Коммона) | `coc:location:arkham-224-arkham-trolleys` |
| `bless-the-beast-and-children-ru/location/politseyskiy-uchastok-arkhema` | `coc:location:arkham-228-police-station` |
| `keeper-rulebook-ru/location/crimson-crawfords` | `coc:location:arkham-219-crawfords-restaurant` |
| `bless-the-beast-and-children-ru/character/eysa-nikols` | `arkham-en/character/downtown-asa-nichols` (`same_as` поставлен) |
| `bless-the-beast-and-children-ru/character/lyuter-harden` | `arkham-en/character/downtown-luther-harden` (`same_as` поставлен; Харден из «Подземки» — другой человек) |
| `bless-the-beast-and-children-ru/character/gregori-dalberg` | `arkham-en/character/downtown-gregory-dahlberg` (`same_as`) |
| `pobeg-iz-innsmuta-ru/character/artur-anderson` | `arkham-en/character/downtown-arthur-anderson` (`same_as`) |
| `pobeg-iz-innsmuta-ru/character/dzho-sardzhent` (33 года) | `arkham-en/character/downtown-joe-sargent` (42 года; `same_as`) |

## Опечатки и сомнения

- Микки/Майки Харриган: в списке участка (с. 107) — «Mikey», в статблоке (с. 108) — «Mickey»; ПЗ 16 при ВЫН 85 и ТЕЛ 85 (должно 17) — `errata`, как напечатано.
- Лютер Харден: ПМ 16 при МОЩ 60 (должно 12) — `errata`, как напечатано.
- Кэлвин Стаки: Уклонение «49% (20/8)» — доли исправлены на 24/9, возможная опечатка процента (40%) — в `errata` (Р-77).
- План больницы: в ключе первого этажа 9 и 10 — обе «Kitchen», 8 — «Waitress Station»; как напечатано, пометки в метках.
- Карта района: номер 215 один, в ключе — 215-A и 215-B (две метки в одной точке).
- Возраст водителя автобуса: Джо Сарджент в «Побеге из Иннсмута» — 33 года, здесь — 42.
- Врезка цен на автомобили: «halve or quarter the cost» против «reduce the price by 20 to 60 percent» в статье 232 — оба сохранены.
- Порядок карт (`order` 22–24) поставлен условно — уточнит сведение вместе с картами других частей.
