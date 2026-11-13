# «Аркхэм» (arkham-en): кандидаты на слияние с записями других книг (Р-154)

Единый список из разделов «Кандидаты на слияние (Р-154)» отчётов частей (`overview`, `downtown`, `east-merchant`, `northside`,
`rivertown-uptown`, `southside`, `campus`, `frenchhill`, `outskirts`, `appendices`), сверенный с базой после сведения частей.
Слияние **не выполнено** — это список для отдельной работы (Р-234: «места Аркхэма из других книг сливаются позже»).

Как сливать (Р-154, Р-80): у мест общая запись — запись путеводителя `coc:location:arkham-…`, книжная запись переезжает в неё
(текст сценария — абзацем со своим источником, старый id — в `corrections`, ссылки переписываются); у людей и организаций —
общая запись `coc:<вид>:<slug>`, в которую сводятся обе книжные. Русское название при слиянии — по официальному изданию (Р-184):
если у книжной записи официальное название, а у записи путеводителя наш перевод, основным становится официальное, наше — в `aliases`.

Уверенность: **высокая** — тот же объект по названию, адресу и роли; **средняя** — тот же по смыслу, но расходятся детали;
**низкая** — возможное совпадение, решает владелец. «Связь» — что уже стоит в базе между записями.

## Места

| Запись другой книги (издание) | Общая запись путеводителя | Уверенность | Связь | Расхождения |
|---|---|---|---|---|
| `naedine-s-tmoy-ru/location/arkham-zakusochnaya-pchela` «Закусочная „Пчела“» (официальное) | `coc:location:arkham-210-bees-diner` «Закусочная Би» | высокая | нет | официальное название «Закусочная „Пчела“» — основным при слиянии |
| `naedine-s-tmoy-ru/location/arkham-pervyy-natsionalnyy-bank` «Первый национальный банк Аркхэма» (официальное) | `coc:location:arkham-214-arkham-first-bank` «Первый банк Аркхэма» | низкая | нет | в путеводителе «Arkham First Bank», в «Наедине с тьмой» — «Arkham First National Bank»; может быть другой банк |
| `bless-the-beast-and-children-ru/location/arkham-keb` (надёжный перевод) | `coc:location:arkham-236-arkham-cab-co` | высокая | нет | — |
| `bless-the-beast-and-children-ru/location/upravlenie-arkhemskogo-tramvaya` | `coc:location:arkham-224-arkham-trolleys` | высокая | нет | адрес: «южная сторона Коммона» — путеводитель: Ист-Армитедж-стрит, 405 |
| `bless-the-beast-and-children-ru/location/politseyskiy-uchastok-arkhema` | `coc:location:arkham-228-police-station` | высокая | нет | — |
| `keeper-rulebook-ru/location/crimson-crawfords` «„Кроуфордс“» (официальное) | `coc:location:arkham-219-crawfords-restaurant` | высокая | нет | — |
| `keeper-rulebook-ru/location/crimson-unconsidered-trifles` «„Мелкие безделицы“» (официальное) | `coc:location:arkham-431-unconsidered-trifles` | высокая | `refs` | название уже официальное |
| `keeper-rulebook-ru/location/crimson-trifles-cellar` «Подвал „Мелких безделиц“» | `coc:location:arkham-431-unconsidered-trifles` (подвал, план 11–16) | высокая | нет | в путеводителе подвал — часть записи 431, не отдельное место |
| `keeper-rulebook-ru/location/crimson-trifles-underground` «Подпол под „Мелкими безделицами“» (официальное) | `coc:location:arkham-431-unconsidered-trifles-subbasement` «Подподвал „Мелких безделиц“» | высокая | `refs` | официальное «Подпол» — основным при слиянии |
| `chernovodnyy-ruchey-ru/location/dues-zabegalovka` «„Забегаловка“» (официальное) | `coc:location:arkham-113-the-speakeasy` | высокая | нет | в «Вышел срок» вышибала — Фрэнк, в путеводителе — Сэм Флинн |
| `dveri-vo-tmu-ru/location/ties-borden-arms-hotel` (официальное) | `coc:location:arkham-130-borden-arms-hotel` | высокая | нет | владелица в «Узах крови» — Пэнси Осборн, в путеводителе владелец — Гарольд О’Коннор |
| `bless-the-beast-and-children-ru/location/tauer-bilding` | `coc:location:arkham-119-tower-professional-building` | высокая | нет | № 6 карты «Bless the Beast and Children» |
| `tri-koshmarnykh-vechera-ru/location/pieces-apartamenty-uorvika` «Апартаменты Уорвика» (официальное) | часть `coc:location:arkham-119-tower-professional-building` | средняя | нет | не слияние: `part_of` апартаментов перевести на 119 |
| `bless-the-beast-and-children-ru/location/klub-miskatonik` | `coc:location:arkham-804-miskatonic-club` (+ организация `arkham-en/organization/uptown-miskatonic-club`) | высокая | нет | № 11 карты «Bless the Beast and Children» |
| `chernovodnyy-ruchey-ru/location/dues-dom-22-po-kerzon-strit` «Дом 22 по Кёрзон-стрит» (официальное) | `coc:location:arkham-906-walnut-street-apartments` «Многоквартирный дом „Уолнат-стрит“» | высокая | нет | адрес совпадает (Кёрзон-стрит, 22); официальное название — основным или в `aliases` (решить при слиянии: в путеводителе дом назван по Уолнат-стрит) |
| `chernovodnyy-ruchey-ru/location/dues-tserkov-presvyatogo-serdtsa` «Церковь Пресвятого Сердца» (официальное) | `coc:location:arkham-908-our-lady-of-the-sacred-heart` «Церковь Богоматери Пресвятого Сердца» | высокая | нет | адрес совпадает; официальное название — основным |
| `chernovodnyy-ruchey-ru/location/dues-u-platana` «„У платана“» (официальное) | `coc:location:arkham-920-sycamores` | высокая | нет | — |
| `keepers-companion-en/location/hammer-salts-diner` («Будь у меня молоток») | `coc:location:arkham-917-salts-diner` | высокая | нет | — |
| `keepers-companion-en/location/hammer-christchurch-cemetery` | `coc:location:arkham-921-christchurch-cemetery` | высокая | нет | — |
| `dveri-vo-tmu-ru/location/ties-dorothy-upman-hall` (официальное) | `coc:location:arkham-619-dorothy-upman-hall` | высокая | `refs` | — |
| `chernovodnyy-ruchey-ru/location/dues-muzey-miskatonikskogo-universiteta` «Музей Мискатоникского университета» (официальное) | `coc:location:arkham-627-university-exhibit-museum` «Выставочный музей университета» | высокая | `refs` | адрес совпадает; официальное название — основным |
| `bless-the-beast-and-children-ru/location/otel-miskatonik` | `coc:location:arkham-634-hotel-miskatonic` | высокая | `refs` | — |
| `keeper-rulebook-ru/location/crimson-medical-school-morgue` «Морг медицинского факультета» (официальное) | `coc:location:arkham-624-college-of-medicine` | средняя | `refs` | морг — часть здания 624; не слияние, а `part_of` на 624 |
| `tri-koshmarnykh-vechera-ru/location/pieces-morg` «Морг Учебного госпиталя Святой Марии» (официальное) | `coc:location:st-marys-hospital` | средняя | `refs` | морг — часть больницы 626; `part_of` на больницу |
| `keeper-rulebook-ru/location/crimson-leiter-office` «Кабинет Лейтера в университете» | возможно `coc:location:arkham-614-robert-carter-memorial-hall` (кафедра истории, 614-I) | низкая | `refs` | вывод из текста; кабинет — часть здания, не слияние |
| `idol-tota-ru/location/kabinet-366` | неясно (отдельное здание в западной части кампуса) | низкая | `refs` на `coc:location:miskatonic-university` | номера здания в путеводителе не найдено |
| `chernovodnyy-ruchey-ru/location/dues-pekarnya-khogana` (официальное) | `coc:location:arkham-716-hogans-bakery` | высокая | `refs` | — |
| `chernovodnyy-ruchey-ru/location/dues-osobnyak-khrama-nadezhdy` (+ этажи `dues-khram-*-etazh`, план `chernovodnyy-ruchey-ru/map/dues-plan-khrama-nadezhdy`) | `coc:location:arkham-719-temple-of-hope` | высокая | `refs` | адрес: «Ист-Колледж-стрит, 114» — путеводитель: 142 E College Street |
| `bless-the-beast-and-children-ru/location/pervaya-baptistskaya-tserkov` | `coc:location:arkham-711-first-baptist-church` | высокая | нет | — |
| `keepers-companion-en/location/little-miracles-ordnams-woods` (+ карта `keepers-companion-en/map/little-miracles-ordnams-woods`) | `coc:location:arkham-os101-ordnams-woods` | высокая | нет | — |
| `keepers-companion-en/location/puzzler-dooley-house` «Дом Дули» (Ист-Пикман-стрит, 411) | пары нет | — | — | в путеводителе места нет; `part_of` можно сменить на `coc:location:arkham-french-hill` |
| «Макгуайр: искусство и дизайн» (сценарий «Вот так головоломка!», `keepers-companion-en`) | пары нет | — | — | в путеводителе упомянут Торговый район без номера — место остаётся в записи сценария |
| Кларкс-Корнерс в описании `coc:location:arkham-environs` (по «Дверям во тьму» — живой посёлок) | `coc:location:arkham-os113-clarks-corners` | высокая | нет | в 2023 году (путеводитель) — руины; абзац «Дверей во тьму» перенести в OS113 |

## Люди

| Запись другой книги (издание) | Запись путеводителя | Уверенность | Связь | Расхождения |
|---|---|---|---|---|
| `bless-the-beast-and-children-ru/character/eysa-nikols` | `arkham-en/character/downtown-asa-nichols` | высокая | `same_as` | — (в членах Аркхэмского оружейного клуба теперь запись путеводителя) |
| `bless-the-beast-and-children-ru/character/lyuter-harden` | `arkham-en/character/downtown-luther-harden` | высокая | `same_as` | Харден из «Подземки» — другой человек (Р-99) |
| `bless-the-beast-and-children-ru/character/gregori-dalberg` | `arkham-en/character/downtown-gregory-dahlberg` | высокая | `same_as` | — |
| `bless-the-beast-and-children-ru/character/robert-bekvort` | `arkham-en/character/campus-robert-beckworth` | высокая | нет | член клуба «Мискатоник» в обеих книгах; дубля внутри путеводителя нет (одна запись, часть campus) |
| `bless-the-beast-and-children-ru/character/charlz-noyes` | `arkham-en/character/frenchhill-charles-noyes` | высокая | `same_as` | — |
| `pobeg-iz-innsmuta-ru/character/artur-anderson` | `arkham-en/character/downtown-arthur-anderson` | высокая | `same_as` | — |
| `pobeg-iz-innsmuta-ru/character/dzho-sardzhent` | `arkham-en/character/downtown-joe-sargent` | высокая | `same_as` | возраст: 33 года («Побег из Иннсмута») — 42 (путеводитель) |
| `pobeg-iz-innsmuta-ru/character/asenat` | `arkham-en/character/outskirts-asenath-waite` | высокая | `same_as` | кандидат в общую `coc:character:asenath-waite` |
| `pobeg-iz-innsmuta-ru/character/edvard-derbi`, `hellouin-v-danviche-ru/character/edvard-derbi` (официальное) | `arkham-en/character/uptown-edward-pickman-derby` | высокая | нет | кандидат в общую запись; официальная форма «Эдвард Дерби» — в `aliases` |
| `pobeg-iz-innsmuta-ru/character/efraim-ueyt` | пары нет | — | — | Эфраим Уэйт в путеводителе — только в тексте записи Асенат |
| `keeper-rulebook-ru/character/crimson-keziah-mason` «Кеция Мейсон» (официальное) | `arkham-en/character/frenchhill-keziah-mason` | высокая | `same_as` | кандидат в общую `coc:character:keziah-mason`; форма «Кеция» принята во всех текстах путеводителя |
| `keeper-rulebook-ru/character/crimson-abner-wick` (официальное) | `arkham-en/character/merchant-abner-wick` | высокая | `same_as` | — |
| `keeper-rulebook-ru/character/crimson-bryce-fallon` | пары нет | — | — | упомянут как прежний заведующий кафедрой истории (614-I) — текстом |
| `chernovodnyy-ruchey-ru/character/dues-denni-obannion` (официальное) | `arkham-en/character/merchant-danny-obannion` | высокая | `same_as` | — |
| `popalis-ru/character/denni-obennion` «Дэнни О’Бэннион» (официальное) | `arkham-en/character/merchant-danny-obannion` | высокая | нет | два официальных перевода расходятся: «О’Баннион» («Вышел срок») и «О’Бэннион» («Попались»); в путеводителе принято «О’Баннион» |
| `chernovodnyy-ruchey-ru/character/dues-mordekhay-oliri` (официальное) | `arkham-en/character/frenchhill-mordecai-oleary` | средняя | `same_as` | статблоки различаются (дробовик 12-го / 20-го калибра) |
| `chernovodnyy-ruchey-ru/character/dues-gvozd-okifi` «Гвоздь О’Кифи» (официальное) | `arkham-en/character/frenchhill-niall-okeeffe` «Найл „Гвоздь“ О’Кифи» | высокая | `same_as` | основное имя путеводителя приведено к официальной форме (Р-184) |
| `chernovodnyy-ruchey-ru/character/dues-dzheykob-smit` (официальное) | `arkham-en/character/frenchhill-jacob-smith` | высокая | `same_as` | — |
| `chernovodnyy-ruchey-ru/character/dues-dzho-portello` «Джо Портелло» (официальное) | `arkham-en/character/southside-joe-potrello` «Джузеппе „Джо“ Портелло» | высокая | `same_as` | в английском путеводителе «Potrello»; основное имя — официальное (Р-184), «Потрелло» — в `aliases` |
| `chernovodnyy-ruchey-ru/character/dues-mayki-ketpol` (официальное) | `arkham-en/character/northside-mikey-catchpole` | высокая | нет | — |
| `chernovodnyy-ruchey-ru/character/dues-salnyy-spun` (официальное) | `arkham-en/character/northside-greasy-spoon` | высокая | нет | — |
| `chernovodnyy-ruchey-ru/character/dues-mardzh-khokler` (официальное) | `arkham-en/character/southside-marge-hockler` | высокая | `same_as` | — |
| `chernovodnyy-ruchey-ru/character/dues-lipkiy-dzhek-fulton` (официальное) | `arkham-en/character/southside-jack-fulton` | высокая | `same_as` | — |
| `chernovodnyy-ruchey-ru/character/dues-entoni-morensi` (официальное) | `arkham-en/character/southside-anthony-morency` | высокая | `same_as` | — |
| `chernovodnyy-ruchey-ru/character/dues-leksi` «Лекси» (официальное) | `arkham-en/character/southside-lexy-romano` | высокая | `same_as` | в «Вышел срок» без фамилии |
| `chernovodnyy-ruchey-ru/character/dues-lyusi-kolaski` (официальное) | `arkham-en/character/campus-lucy-kolasky` | высокая | нет | — |
| `chernovodnyy-ruchey-ru/character/dues-khilda-boungreyder` (официальное) | `arkham-en/character/campus-hilda-bonegrader` | высокая | нет | — |
| `pulp-cthulhu-en/character/chester-armwright` | `arkham-en/character/campus-chester-armwright` | высокая | нет | пульп-профиль — вариант статблока (Р-125) |
| `pulp-cthulhu-en/character/francis-morgan` | `arkham-en/character/campus-francis-morgan` | высокая | нет | то же; возраст в путеводителе 31 (текст) / 37 (статблок) |
| `pulp-cthulhu-en/character/william-dyer` | `arkham-en/character/campus-william-dyer` | высокая | нет | то же |
| `keepers-companion-en/character/hammer-arkham-police` | `arkham-en/character/generic-police-patrol-officer` | — | нет | не дубль: числа другие, только сходство типажа |

## Организации, книги, карты

| Запись другой книги (издание) | Запись путеводителя | Уверенность | Связь | Расхождения |
|---|---|---|---|---|
| `chernovodnyy-ruchey-ru/organization/dues-mafiya-obanniona` «Мафия О’Банниона» (официальное) | `arkham-en/organization/merchant-obannion-organization` «Организация Дэнни О’Банниона» | высокая | `refs` | официальное название «Мафия О’Банниона» — основным при слиянии |
| `chernovodnyy-ruchey-ru/organization/dues-khram-nadezhdy` (официальное) | `arkham-en/organization/frenchhill-temple-of-hope` | высокая | `refs` | — |
| `dead-light-en/tome/chalice-lesser-key-of-solomon` «Малый ключ царя Соломона» | `arkham-en/tome/southside-lesser-key-of-solomon` «Малый ключ Соломона» | высокая | нет | то же издание 1904 года; кандидат в общую запись справочника `coc:tome:*` (Р-56) |
| `sny-o-yaponii-ru/map/miskatonic-campus` | `arkham-en/map/campus-neighborhood` | — | нет | не дубль: другая карта кампуса; обе остаются |
| Другие номера «Arkham Advertiser» (`pobeg-iz-innsmuta-ru/handout/arkham-advertiser-spetsvypusk`, `mothers-love-ru/handout/arkham-advertiser-1928`, `shadows-of-leningrad-en/handout/handout-a-arkham-advertiser`) | `arkham-en/handout/advertiser-1922-page-*` | — | — | не дубли: разные выпуски газеты |

## Кандидаты в общие записи внутри путеводителя

- Персонажи, которые встречаются в нескольких книгах и годятся в общие `coc:character:*`: Кеция Мейсон, Асенат Уэйт, Эдвард Пикман Дерби,
  Дэнни О’Баннион (три книги), Абнер Уик.
- Рэндольф Картер и Герберт Уэст упоминаются в нескольких частях путеводителя, записей нет — кандидаты в общие записи персонажей.
