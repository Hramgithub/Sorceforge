# Arkham (arkham-en) — часть «northside»: Нортсайд, места 100–199 (с. 70–94, физ. 71–95)

Решение: Р-234. Источник — `arkham-en` (оригинал), русский текст — наш перевод (`translated`); машинный перевод не использовался.
Карты — `arkham-maps-en` (с. 4 — карта района, с. 17 — схема канализации). Предложения правок общих записей —
`proposals-northside.json` (25 правок, пробный прогон `pipeline/integrate/apply.py --dry-run` проходит).

Сокращения в таблице: `L:` = `coc:location:`, `C:` = `arkham-en/character/northside-`, `O:` = `arkham-en/organization/northside-`,
`I:` = `arkham-en/item/northside-`, `H:` = `arkham-en/handout/northside-`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Neighborhood 1: Northside 100–199 (вступление) | 70 | `L:arkham-northside` (запись части overview, текст уже там) |
| Карта «Arkham Neighborhood Northside», Points of Interest | 71 | `arkham-en/map/northside-map` (метки 101–140 + заголовок района), картинка `app/maps/arkham-northside-map.jpg` |
| 101 Pump House & Water Tower (Notable Folk, Historical, Strangeness) | 70 | `L:arkham-101-pump-house-water-tower`; `C:arthur-bowen`, `C:richard-tobey` |
| 102 Potter’s Field (Notable Folk, Historical, Strangeness) | 70 | `L:arkham-102-potters-field`; профили `C:patrick-ohare`, `C:jeremiah-williams` (с. 74) |
| Arkham’s Sewers (врезка: Access Points, Layout, Notable Folk, Strangeness) | 72 | `L:arkham-sewers`; `C:bill-kent`, `C:ted-rogers`, `C:edna-rogers` |
| Схема «Arkham Sewers Record Plan» | 73 | `arkham-en/map/northside-sewers`, картинка `app/maps/arkham-northside-sewers.jpg` |
| Patrick O’Hare, Jeremiah Williams (профили) | 74 | `C:patrick-ohare`, `C:jeremiah-williams` |
| 103 Bartholomew Appley IV, Home of (Historical, Strangeness) + профиль | 74–75 | `L:arkham-103-appley-residence`; `C:bartholomew-appley` |
| 104 Judith Renforth, Home of (Important Things, Strangeness) + профиль, Pulp | 75 | `L:arkham-104-renforth-residence`; `C:judith-renforth`; `I:renforth-rlyeh-translation`; экземпляр в `coc:tome:rlyeh-text` — предложение |
| 105 Folger’s Boarding House (Notable Folk, Historical, Strangeness) | 76 | `L:arkham-105-folgers-boarding-house`; `C:isaac-hoffman`, `C:sarah-hoffman`, `C:david-folger` |
| 106 Manley Theater (Notable Folk) | 76 | `L:arkham-106-manley-theater`; `C:nelly-samson`, `C:jed-smith` |
| Arkham Amateur Theatre Company (врезка, Benefits) | 76 | `O:arkham-amateur-theatre-company`; `C:andrew-lamont`, `C:elizabeth-peabody` |
| 107 Jenkin Public School (Notable Folk) | 76 | `L:arkham-107-jenkin-public-school`; `C:alfred-mcguiness` |
| 108 Masonic Lodge (Women’s Associate Group, Lodge Offices, Benefits, Strangeness) | 76–77 | `L:arkham-108-masonic-lodge`; `O:arkham-masonic-lodge`; `C:caleb-carson`; `I:innsmouth-lodge-papers` |
| 109 Guardian Apartments (Notable Folk, Strangeness) | 77 | `L:arkham-109-guardian-apartments`; `C:jimmy-fassbender`, `C:miriam-fassbender` |
| 110 Arkham Gazette (Notable Folk, Historical, Strangeness) | 77 | `L:arkham-gazette` (общая запись) — предложения: номер, район, адрес, текст статьи, жители, источники; `I:gazette-duplicate-issues` |
| Michael Crane, Willard Peck (профили) | 78 | `C:michael-crane`, `C:willard-peck` |
| 111 Jedediah Marsh & Assoc. (Notable Folk, Strangeness) | 78 | `L:arkham-111-jedediah-marsh-associates`; `C:jedediah-marsh`, `C:zachary-winesap`, `C:janet-mccrimmon` |
| 112 Terrace Building Apartments (Notable Folk, Strangeness) | 78–79 | `L:arkham-112-terrace-building-apartments`; `C:santiago-silva` |
| Minerva «Minnie» Coleman (профиль, Psychic Powers, Pulp) | 79 | `C:minnie-coleman` |
| 113 The Speakeasy (Notable Folk) | 80 | `L:arkham-113-the-speakeasy` |
| Speakeasy People: Sam Flinn, Mikey Catchpole, Ruby Simmons, «Saint Looey» Larry Freen | 80–81 | `C:sam-flinn`, `C:mikey-catchpole`, `C:ruby-simmons`, `C:larry-freen` |
| 114 Arkham Loan Agency (Getting a Loan, Notable Folk, Historical) | 82 | `L:arkham-114-arkham-loan-agency`; `C:aidan-fitzgerald`, `C:maeve-maloney` |
| 115 Arkham Fuel & Coal Co. (Notable Folk, Strangeness) | 82 | `L:arkham-115-arkham-fuel-coal`; `C:dwight-molzan`, `C:norma-king`, водители `C:albin-pawlak`, `C:oles-symanski`, `C:abraham-scurlock`, `C:clarence-shattuck`, `C:percy-cutch`; `I:erratic-rod` |
| Реклама «Gleason’s Dress Sale» | 82 | `H:gleasons-dress-sale-ad` |
| 116 Construction Site (Strangeness) | 83 | `L:arkham-116-construction-site`; `I:beacher-marvels` |
| 117 Harding Boarding House (Notable Folk) | 83 | `L:arkham-117-harding-boarding-house`; `C:william-harding`, `C:grace-harding` |
| Jin Lillibridge (профиль) | 83 | `C:jin-lillibridge` |
| 118 Taranowski’s Bakery (Notable Folk, Strangeness) | 83 | `L:arkham-118-taranowskis-bakery`; `C:georgie-taranowski`, `C:wilma-taranowski` |
| 119 Tower Professional Building (Notable Folk; Suites 1A, 1B, 2A, 2C, 3A, 4A, 5A; Look to the Future; Strangeness) | 84–85 | `L:arkham-119-tower-professional-building`; `C:sawyer-lyman`, `C:brett-cox`, `C:ephraim-sprague`, `C:gilroy-feldman`, `C:veronica-lee`, `C:james-gedney`, `C:gordon-brown`, `C:cedrick-manton`, `C:august-manton`, `C:elliot-stigleitz`, `C:michael-stigleitz`, `C:allen-turner`, `C:duncan-wright`, `C:adam-crane` |
| Edwin Cassidy (профиль) | 84 | `C:edwin-cassidy` |
| 120 Miss Christian’s School for Modern Women (Benefits) | 85 | `L:arkham-120-miss-christians-school`; `C:regina-christian` |
| 121 Hardwicke’s Stamps & Coins (Notable Folk, Strangeness) | 85 | `L:arkham-121-hardwickes-stamps-coins`; `C:chester-hardwicke`, `C:francis-jenks` |
| 122 J. J. Abbott Taxidermist (Strangeness) + профиль Jerome J. Abbot | 85–86 | `L:arkham-122-jj-abbott-taxidermist`; `C:jerome-abbott`; `I:mer-man` |
| 123 Worldwide Clipping Service (Notable Folk, Strangeness) | 87 | `L:arkham-123-worldwide-clipping-service`; `C:elliot-snow`, `C:alice-cutler`, `C:ruth-windsor`, `C:lillian-lane`, `C:ralph-bartoll` |
| 124 Uptown Laundry (Notable Folk) | 87 | `L:arkham-124-uptown-laundry`; `C:mildred-briry` |
| 125 E. E. Saltonstall & Associates, Legal Practice (Notable Folk) + профиль Ellis E. Saltonstall, Sr. | 87 | `L:arkham-125-saltonstall-associates`; `C:ellis-saltonstall`, `C:ammon-wyman`, `C:marston-leach`, `C:james-allen-white` |
| 126 Rare Books & Maps (Notable Folk, Possibilities, Strangeness) + профили Edward Tillinghast, Alice Ballard, Pulp | 87–89 | `L:arkham-126-rare-books-maps`; `C:edward-tillinghast`, `C:alice-ballard` |
| 127 Arkham Chamber of Commerce (Benefits) | 89 | `L:arkham-127-chamber-of-commerce`; `O:arkham-chamber-of-commerce` |
| 128 Arkham Baler Company (Notable Folk, Look to the Future) | 89 | `L:arkham-128-arkham-baler-company`; `C:jackson-dodge`, `C:lyn-spencer` |
| 129 Arkham Bus Line (маршруты) | 89 | `L:arkham-129-arkham-bus-line` — таблица «Автобусные маршруты» |
| 130 Borden Arms Hotel (Notable Folk, Strangeness) + профиль Alex Hearne | 89–91 | `L:arkham-130-borden-arms-hotel`; `C:harold-oconnor`, `C:alex-hearne` |
| 131 Arkham Advertiser (Useful, Notable Folk) + профиль Roberta Henry | 90–91 | `L:arkham-advertiser` (общая запись) — предложения; `C:harvey-gedney`, `C:roberta-henry` |
| 132 Desolate Highway Café (Notable Folk, Historical, Look to the Future) | 91 | `L:arkham-132-desolate-highway-cafe`; `C:reid-vandervelden`, `C:josh-visser`, `C:cecilia-atkins` |
| 133 Commercial House (Notable Folk) | 91 | `L:arkham-133-commercial-house`; `C:jacob-newcomb`, `C:danny-read`, `C:phoebe-may` |
| 134 B&M Train Station (Useful, Notable Folk, Strangeness) | 91–92 | `L:arkham-134-bm-train-station` — таблица «Поезда»; `C:wilson-horton`, `C:bobby-ashbourne` |
| 135 Aunt Lucy’s Diner (Notable Folk, Useful) | 92 | `L:arkham-135-aunt-lucys-diner`; `C:lucy-james`, `C:earl-james` |
| 136 Tilden Arms Hotel (Notable Folk, Not So Useful, Look to the Future) + профиль Marvin Dunlap, Pulp | 92–93 | `L:arkham-136-tilden-arms-hotel`; `C:simeon-tufts`, `C:margaret-rea`, `C:marvin-dunlap` |
| 137 Newsstand (Notable Folk) | 93 | `L:arkham-137-newsstand`; `C:ernie-casado` |
| 138 Sander’s Wax Museum (Notable Folk, Look to the Future, Strangeness) | 93 | `L:arkham-138-sanders-wax-museum`; `C:pete-sander` |
| 139 Grafton Diner (Notable Folk) | 93 | `L:arkham-139-grafton-diner`; `C:victor-grafton`, `C:bernice-whaley`, `C:judy-allaband` |
| 140 Railroad Properties (Notable Folk, Strangeness) | 93–94 | `L:arkham-140-railroad-properties`; группы `C:rail-crew`, `C:hoboes`; `C:greasy-spoon` |
| The Imperfect Resurrected Thing (профиль) | 94 | `arkham-en/creature/northside-imperfect-resurrected-thing` (`instance_of` `coc:creature:reanimated`) |
| «Greasy Spoon» (профиль) | 94 | `C:greasy-spoon` |
| Реклама «Stigleitz & Son Insurance» | 94 | `H:stigleitz-ad` |

## Не взято

- Иллюстрации и портреты (портреты персонажей; «The Speakeasy», с. 81; «Taxidermist’s Workroom», с. 86; металлическое существо, с. 83; стопка книг, с. 75; картинки реклам на с. 82 и 94) — папка `app/art/` не входит в мою часть; тексты реклам перенесены в раздаточные материалы. Перенести картинки можно через `pipeline/art/add_images.py`.
- Исторические и упомянутые лица без записей (текстом в описаниях мест): Хеспер Пейн (105), Аарон Крейн (110), Дэвид и Бенджамин Палмеры (112), Боб Бичер (116), Уилфред Ричардсон (119), Ричард Гедни (131), Герберт Уэст (102, 140), Генри Уэнтворт Эйкли (136), охранник, искусанный тварью (140), безымянные посыльные (134).
- «Аркхэм свингтайм бэнд» (133) — студенческий оркестр без описания; упомянут текстом.
- Подписи улиц на карте района и технические подписи схемы канализации — записей улиц нет; подписи схемы сведены в текст единственной метки.
- Ключевые навыки малых персонажей (Лайман, Хардвик, Ньюкомб, Рид, Мэй, Эшборн) — в описании, полного статблока в книге нет.

## Ссылки на места и людей других частей (текстом; связать при сведении)

Ратуша (217), Суд и тюрьма (212) и судья Кизар Рэндалл, Психиатрическая больница Пикеринга (201; Тоби — предложение к `coc:location:arkham-sanitarium`), «Лаки Клевер» (412) и Дэнни О’Баннион, «Редкости и древности» (419) и Джордж Тиллингаст, вторая пекарня Тарановского (442), универмаг Глисона (427), кирпичный завод Данэма (517), «Тоннели Аркхэма» (с. 144), Клиническая больница св. Марии (626; ссылка на `coc:location:st-marys-hospital` уже стоит), библиотека Орна (623), кафедры 614-A/614-D, Альберт Н. Уилмарт (с. 169), доктор Джабир Шарик (с. 170), «Университетские актёры» (с. 163), Эдвард Пикман Дерби и Дом семьи Дерби (818), Аркхэмское историческое общество (901), Симпсон-апартментс (911) и Гарольд Бимис, кладбище Крайстчерч (921), «Ривер-Таун файв» (врезка с. 222), Испепелённая пустошь (OS112), поместье Кроуниншилд (OS114) и Асенат Уэйт (с. 240), Аркхэмский ковен (с. 51: члены — Джеймс Аллен-Уайт, возможно Элис Баллард).

## Пересечения с обзором (overview)

Обзор «Arkham Societies» (с. 32–33) называет труппу (106), торговую палату (127) и масонскую ложу (108). Полные записи с выгодами заведены здесь: `O:arkham-amateur-theatre-company`, `O:arkham-chamber-of-commerce`, `O:arkham-masonic-lodge` — если часть overview завела свои, их надо слить. Таблица слухов обзора ссылается на места 102–140 — id мест см. выше.

## Кандидаты на слияние (Р-154)

| Запись другой книги | Общая запись | Примечание |
|---|---|---|
| `chernovodnyy-ruchey-ru/location/dues-zabegalovka` | `coc:location:arkham-113-the-speakeasy` | «Забегаловка» на Норт-Гаррисон-стрит («Вышел срок»); там вышибала — Фрэнк, не Сэм Флинн |
| `chernovodnyy-ruchey-ru/character/dues-mayki-ketpol` | `arkham-en/character/northside-mikey-catchpole` | тот же бармен |
| `chernovodnyy-ruchey-ru/character/dues-salnyy-spun` | `arkham-en/character/northside-greasy-spoon` | тот же бродяга-карманник |
| `dveri-vo-tmu-ru/location/ties-borden-arms-hotel` | `coc:location:arkham-130-borden-arms-hotel` | тот же адрес; владелица в «Узах крови» — Пэнси Осборн, в путеводителе владелец — Гарольд О’Коннор |
| `bless-the-beast-and-children-ru/location/tauer-bilding` | `coc:location:arkham-119-tower-professional-building` | то же здание (№ 6 карты «Bless the Beast and Children») |
| `tri-koshmarnykh-vechera-ru/location/pieces-apartamenty-uorvika` | часть `coc:location:arkham-119-tower-professional-building` | апартаменты доктора Уорвика в этом здании — `part_of` можно перевести на 119 |

## Опечатки и сомнения

- Джудит Ренфорт: Скорость напечатана 4, по правилам 6 (`errata`).
- Эдвард Тиллингаст: урон Драки «1D4» при БкУ 0 (`errata`).
- Джером Дж. Эбботт: в заголовке профиля «Abbot», в названии места «Abbott» (`errata`).
- Элис Баллард: блок Pulp вверху с. 89 без имени — отнесён к Баллард по вёрстке (вывод); фраза таланта «Strong Willed» оборвана (`errata`).
- Несовершенное воскрешённое существо: в строке Уклонения напечатан урон «1D10» (`errata`).
- «Аркхэм газетт» в записи из «Вышел срок» названа «Еженедельная газета. Основана в 1869 г.» — путеводитель: основана в 1806 году, ежедневная с 1894 года. Оба текста остаются (разные книги).
- Тауэр-билдинг: обзор района (overview) пишет английское название, здесь русское — «Тауэр-билдинг» по записи «Bless the Beast and Children»; улицы — по записи района (Уэст-…, Кёрвен-стрит).
- Канализация Аркхэма (`coc:location:arkham-sewers`) — ненумерованная врезка из моих страниц, заведена как общее место города (`part_of` `coc:location:arkham`).
