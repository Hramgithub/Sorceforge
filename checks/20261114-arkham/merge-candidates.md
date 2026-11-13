# «Аркхэм» (arkham-en): кандидаты на слияние с записями других книг (Р-154)

Единый список из разделов «Кандидаты на слияние (Р-154)» отчётов частей (`overview`, `downtown`, `east-merchant`, `northside`,
`rivertown-uptown`, `southside`, `campus`, `frenchhill`, `outskirts`, `appendices`), сверенный с базой после сведения частей.
**Слияние выполнено 2026-11-14** для кандидатов высокой уверенности (колонка «Сделано»); средние и низкие оставлены владельцу.
Полный список файлов и пар «старый id → общий id» — `merge-done.txt`.

Как сливать (Р-154, Р-80): у мест общая запись — запись путеводителя `coc:location:arkham-…`, книжная запись переезжает в неё
(текст сценария — абзацем со своим источником, старый id — в `corrections`, ссылки переписываются); у людей и организаций —
общая запись `coc:<вид>:<slug>`, в которую сводятся обе книжные. Русское название при слиянии — по официальному изданию (Р-184):
если у книжной записи официальное название, а у записи путеводителя наш перевод, основным становится официальное, наше — в `aliases`.

Уверенность: **высокая** — тот же объект по названию, адресу и роли; **средняя** — тот же по смыслу, но расходятся детали;
**низкая** — возможное совпадение, решает владелец. «Связь» — что уже стоит в базе между записями.

## Места

| Запись другой книги (издание) | Общая запись путеводителя | Уверенность | Связь | Расхождения | Сделано |
|---|---|---|---|---|---|
| `naedine-s-tmoy-ru/location/arkham-zakusochnaya-pchela` «Закусочная „Пчела“» (официальное) | `coc:location:arkham-210-bees-diner` «Закусочная Би» | высокая | нет | официальное название «Закусочная „Пчела“» — основным при слиянии | слито в 210; основное имя «Закусочная „Пчела“», «Закусочная Би» — в `aliases` |
| `naedine-s-tmoy-ru/location/arkham-pervyy-natsionalnyy-bank` «Первый национальный банк Аркхэма» (официальное) | `coc:location:arkham-214-arkham-first-bank` «Первый банк Аркхэма» | низкая | нет | в путеводителе «Arkham First Bank», в «Наедине с тьмой» — «Arkham First National Bank»; может быть другой банк | оставлено: низкая уверенность, название банка другое |
| `bless-the-beast-and-children-ru/location/arkham-keb` (надёжный перевод) | `coc:location:arkham-236-arkham-cab-co` | высокая | нет | — | слито в 236 |
| `bless-the-beast-and-children-ru/location/upravlenie-arkhemskogo-tramvaya` | `coc:location:arkham-224-arkham-trolleys` | высокая | нет | адрес: «южная сторона Коммона» — путеводитель: Ист-Армитедж-стрит, 405 | слито в 224; адрес — по путеводителю, расхождение — в `quality.notes` |
| `bless-the-beast-and-children-ru/location/politseyskiy-uchastok-arkhema` | `coc:location:arkham-228-police-station` | высокая | нет | — | слито в 228 |
| `keeper-rulebook-ru/location/crimson-crawfords` «„Кроуфордс“» (официальное) | `coc:location:arkham-219-crawfords-restaurant` | высокая | нет | — | слито в 219; «Ресторан „Кроуфордс“» — тоже официальная форма (псевдоним записи «Книги хранителя»), осталось основным, «„Кроуфордс“» — в `aliases` |
| `keeper-rulebook-ru/location/crimson-unconsidered-trifles` «„Мелкие безделицы“» (официальное) | `coc:location:arkham-431-unconsidered-trifles` | высокая | `refs` | название уже официальное | слито в 431 |
| `keeper-rulebook-ru/location/crimson-trifles-cellar` «Подвал „Мелких безделиц“» | `coc:location:arkham-431-unconsidered-trifles` (подвал, план 11–16) | высокая | нет | в путеводителе подвал — часть записи 431, не отдельное место | слито в 431 (абзац «подвал лавки») |
| `keeper-rulebook-ru/location/crimson-trifles-underground` «Подпол под „Мелкими безделицами“» (официальное) | `coc:location:arkham-431-unconsidered-trifles-subbasement` «Подподвал „Мелких безделиц“» | высокая | `refs` | официальное «Подпол» — основным при слиянии | слито в 431-subbasement; основное имя «Подпол под „Мелкими безделицами“», «Подподвал…» — в `aliases` |
| `chernovodnyy-ruchey-ru/location/dues-zabegalovka` «„Забегаловка“» (официальное) | `coc:location:arkham-113-the-speakeasy` | высокая | нет | в «Вышел срок» вышибала — Фрэнк, в путеводителе — Сэм Флинн | слито в 113; оба вышибалы — жители с пометкой книги, расхождение — в `quality.notes` |
| `dveri-vo-tmu-ru/location/ties-borden-arms-hotel` (официальное) | `coc:location:arkham-130-borden-arms-hotel` | высокая | нет | владелица в «Узах крови» — Пэнси Осборн, в путеводителе владелец — Гарольд О’Коннор | слито в 130; оба владельца — жители с пометкой книги, расхождение — в `quality.notes` |
| `bless-the-beast-and-children-ru/location/tauer-bilding` | `coc:location:arkham-119-tower-professional-building` | высокая | нет | № 6 карты «Bless the Beast and Children» | слито в 119 |
| `tri-koshmarnykh-vechera-ru/location/pieces-apartamenty-uorvika` «Апартаменты Уорвика» (официальное) | часть `coc:location:arkham-119-tower-professional-building` | средняя | нет | не слияние: `part_of` апартаментов перевести на 119 | оставлено: средняя уверенность (смена `part_of` — решение владельца) |
| `bless-the-beast-and-children-ru/location/klub-miskatonik` | `coc:location:arkham-804-miskatonic-club` (+ организация `arkham-en/organization/uptown-miskatonic-club`) | высокая | нет | № 11 карты «Bless the Beast and Children» | слито в 804; пометка у организации клуба обновлена |
| `chernovodnyy-ruchey-ru/location/dues-dom-22-po-kerzon-strit` «Дом 22 по Кёрзон-стрит» (официальное) | `coc:location:arkham-906-walnut-street-apartments` «Многоквартирный дом „Уолнат-стрит“» | высокая | нет | адрес совпадает (Кёрзон-стрит, 22); официальное название — основным или в `aliases` (решить при слиянии: в путеводителе дом назван по Уолнат-стрит) | слито в 906; основным осталось название путеводителя (в «Вышел срок» у дома нет собственного названия, только адрес), «Дом 22 по Кёрзон-стрит» — в `aliases`; квартиры Джека и хозяйки — `part_of` 906 |
| `chernovodnyy-ruchey-ru/location/dues-tserkov-presvyatogo-serdtsa` «Церковь Пресвятого Сердца» (официальное) | `coc:location:arkham-908-our-lady-of-the-sacred-heart` «Церковь Богоматери Пресвятого Сердца» | высокая | нет | адрес совпадает; официальное название — основным | слито в 908; основное имя «Церковь Пресвятого Сердца» |
| `chernovodnyy-ruchey-ru/location/dues-u-platana` «„У платана“» (официальное) | `coc:location:arkham-920-sycamores` | высокая | нет | — | слито в 920 |
| `keepers-companion-en/location/hammer-salts-diner` («Будь у меня молоток») | `coc:location:arkham-917-salts-diner` | высокая | нет | — | слито в 917 |
| `keepers-companion-en/location/hammer-christchurch-cemetery` | `coc:location:arkham-921-christchurch-cemetery` | высокая | нет | — | слито в 921 |
| `dveri-vo-tmu-ru/location/ties-dorothy-upman-hall` (официальное) | `coc:location:arkham-619-dorothy-upman-hall` | высокая | `refs` | — | слито в 619 |
| `chernovodnyy-ruchey-ru/location/dues-muzey-miskatonikskogo-universiteta` «Музей Мискатоникского университета» (официальное) | `coc:location:arkham-627-university-exhibit-museum` «Выставочный музей университета» | высокая | `refs` | адрес совпадает; официальное название — основным | слито в 627; основное имя «Музей Мискатоникского университета» |
| `bless-the-beast-and-children-ru/location/otel-miskatonik` | `coc:location:arkham-634-hotel-miskatonic` | высокая | `refs` | — | слито в 634; Дэнни О’Баннион (общая запись) переведён из `refs` в жители |
| `keeper-rulebook-ru/location/crimson-medical-school-morgue` «Морг медицинского факультета» (официальное) | `coc:location:arkham-624-college-of-medicine` | средняя | `refs` | морг — часть здания 624; не слияние, а `part_of` на 624 | оставлено: средняя уверенность (смена `part_of` — решение владельца) |
| `tri-koshmarnykh-vechera-ru/location/pieces-morg` «Морг Учебного госпиталя Святой Марии» (официальное) | `coc:location:st-marys-hospital` | средняя | `refs` | морг — часть больницы 626; `part_of` на больницу | оставлено: средняя уверенность (смена `part_of` — решение владельца) |
| `keeper-rulebook-ru/location/crimson-leiter-office` «Кабинет Лейтера в университете» | возможно `coc:location:arkham-614-robert-carter-memorial-hall` (кафедра истории, 614-I) | низкая | `refs` | вывод из текста; кабинет — часть здания, не слияние | оставлено: низкая уверенность |
| `idol-tota-ru/location/kabinet-366` | неясно (отдельное здание в западной части кампуса) | низкая | `refs` на `coc:location:miskatonic-university` | номера здания в путеводителе не найдено | оставлено: низкая уверенность, пары нет |
| `chernovodnyy-ruchey-ru/location/dues-pekarnya-khogana` (официальное) | `coc:location:arkham-716-hogans-bakery` | высокая | `refs` | — | слито в 716 |
| `chernovodnyy-ruchey-ru/location/dues-osobnyak-khrama-nadezhdy` (+ этажи `dues-khram-*-etazh`, план `chernovodnyy-ruchey-ru/map/dues-plan-khrama-nadezhdy`) | `coc:location:arkham-719-temple-of-hope` | высокая | `refs` | адрес: «Ист-Колледж-стрит, 114» — путеводитель: 142 E College Street | слито в 719; этажи — `part_of` 719, метки плана ведут на 719; адрес — по путеводителю, расхождение — в `quality.notes` |
| `bless-the-beast-and-children-ru/location/pervaya-baptistskaya-tserkov` | `coc:location:arkham-711-first-baptist-church` | высокая | нет | — | слито в 711 |
| `keepers-companion-en/location/little-miracles-ordnams-woods` (+ карта `keepers-companion-en/map/little-miracles-ordnams-woods`) | `coc:location:arkham-os101-ordnams-woods` | высокая | нет | — | слито в OS101; места сценария в лесу — `part_of` OS101, карта сценария ведёт на OS101 |
| `keepers-companion-en/location/puzzler-dooley-house` «Дом Дули» (Ист-Пикман-стрит, 411) | пары нет | — | — | в путеводителе места нет; `part_of` можно сменить на `coc:location:arkham-french-hill` | не трогалось: пары нет |
| «Макгуайр: искусство и дизайн» (сценарий «Вот так головоломка!», `keepers-companion-en`) | пары нет | — | — | в путеводителе упомянут Торговый район без номера — место остаётся в записи сценария | не трогалось: пары нет |
| Кларкс-Корнерс в описании `coc:location:arkham-environs` (по «Дверям во тьму» — живой посёлок) | `coc:location:arkham-os113-clarks-corners` | высокая | нет | в 2023 году (путеводитель) — руины; абзац «Дверей во тьму» перенести в OS113 | в OS113 — абзац «Служителей озера» («Двери во тьму», с. 57, 61, 67: посёлок обитаем, полиция, плотник), источники и ссылки; абзац об озере Сквоттерс в «Окрестностях Аркхэма» оставлен (он об озере), у него и у озера — ссылка на OS113 |

## Люди

| Запись другой книги (издание) | Запись путеводителя | Уверенность | Связь | Расхождения | Сделано |
|---|---|---|---|---|---|
| `bless-the-beast-and-children-ru/character/eysa-nikols` | `arkham-en/character/downtown-asa-nichols` | высокая | `same_as` | — (в членах Аркхэмского оружейного клуба теперь запись путеводителя) | общая `coc:character:asa-nichols` |
| `bless-the-beast-and-children-ru/character/lyuter-harden` | `arkham-en/character/downtown-luther-harden` | высокая | `same_as` | Харден из «Подземки» — другой человек (Р-99) | общая `coc:character:luther-harden` (Харден «Подземки» не тронут) |
| `bless-the-beast-and-children-ru/character/gregori-dalberg` | `arkham-en/character/downtown-gregory-dahlberg` | высокая | `same_as` | — | общая `coc:character:gregory-dahlberg` |
| `bless-the-beast-and-children-ru/character/robert-bekvort` | `arkham-en/character/campus-robert-beckworth` | высокая | нет | член клуба «Мискатоник» в обеих книгах; дубля внутри путеводителя нет (одна запись, часть campus) | общая `coc:character:robert-beckworth` |
| `bless-the-beast-and-children-ru/character/charlz-noyes` | `arkham-en/character/frenchhill-charles-noyes` | высокая | `same_as` | — | общая `coc:character:charles-noyes` |
| `pobeg-iz-innsmuta-ru/character/artur-anderson` | `arkham-en/character/downtown-arthur-anderson` | высокая | `same_as` | — | общая `coc:character:arthur-anderson` |
| `pobeg-iz-innsmuta-ru/character/dzho-sardzhent` | `arkham-en/character/downtown-joe-sargent` | высокая | `same_as` | возраст: 33 года («Побег из Иннсмута») — 42 (путеводитель) | общая `coc:character:joe-sargent`; статблок и возраст 33 — «Побега из Иннсмута» (статблок есть только там), 42 — в `quality.notes` |
| `pobeg-iz-innsmuta-ru/character/asenat` | `arkham-en/character/outskirts-asenath-waite` | высокая | `same_as` | кандидат в общую `coc:character:asenath-waite` | общая `coc:character:asenath-waite` |
| `pobeg-iz-innsmuta-ru/character/edvard-derbi`, `hellouin-v-danviche-ru/character/edvard-derbi` (официальное) | `arkham-en/character/uptown-edward-pickman-derby` | высокая | нет | кандидат в общую запись; официальная форма «Эдвард Дерби» — в `aliases` | общая `coc:character:edward-pickman-derby` из записей путеводителя и «Побега из Иннсмута»; **`hellouin-v-danviche-ru/character/edvard-derbi` оставлен**: 12-летний готовый сыщик сценария эпохи 1920-х (в 1920-е Дерби путеводителя за 30), книга не говорит, что это тот же человек, в записи — пометка Р-99 |
| `pobeg-iz-innsmuta-ru/character/efraim-ueyt` | пары нет | — | — | Эфраим Уэйт в путеводителе — только в тексте записи Асенат | не трогалось: пары нет |
| `keeper-rulebook-ru/character/crimson-keziah-mason` «Кеция Мейсон» (официальное) | `arkham-en/character/frenchhill-keziah-mason` | высокая | `same_as` | кандидат в общую `coc:character:keziah-mason`; форма «Кеция» принята во всех текстах путеводителя | общая `coc:character:keziah-mason` |
| `keeper-rulebook-ru/character/crimson-abner-wick` (официальное) | `arkham-en/character/merchant-abner-wick` | высокая | `same_as` | — | общая `coc:character:abner-wick`; основной статблок — «Книги хранителя», статблок путеводителя — вариант «Аркхэм» |
| `keeper-rulebook-ru/character/crimson-bryce-fallon` | пары нет | — | — | упомянут как прежний заведующий кафедрой истории (614-I) — текстом | не трогалось: пары нет |
| `chernovodnyy-ruchey-ru/character/dues-denni-obannion` (официальное) | `arkham-en/character/merchant-danny-obannion` | высокая | `same_as` | — | общая `coc:character:danny-obannion` |
| `popalis-ru/character/denni-obennion` «Дэнни О’Бэннион» (официальное) | `arkham-en/character/merchant-danny-obannion` | высокая | нет | два официальных перевода расходятся: «О’Баннион» («Вышел срок») и «О’Бэннион» («Попались»); в путеводителе принято «О’Баннион» | влит в `coc:character:danny-obannion`; основным — «О’Баннион», «О’Бэннион» — в `aliases` |
| `chernovodnyy-ruchey-ru/character/dues-mordekhay-oliri` (официальное) | `arkham-en/character/frenchhill-mordecai-oleary` | средняя | `same_as` | статблоки различаются (дробовик 12-го / 20-го калибра) | оставлено: средняя уверенность (по сути то же лицо: возраст и числа совпадают, кроме дробовика и навыков путеводителя — слить решением владельца) |
| `chernovodnyy-ruchey-ru/character/dues-gvozd-okifi` «Гвоздь О’Кифи» (официальное) | `arkham-en/character/frenchhill-niall-okeeffe` «Найл „Гвоздь“ О’Кифи» | высокая | `same_as` | основное имя путеводителя приведено к официальной форме (Р-184) | общая `coc:character:niall-okeeffe` |
| `chernovodnyy-ruchey-ru/character/dues-dzheykob-smit` (официальное) | `arkham-en/character/frenchhill-jacob-smith` | высокая | `same_as` | — | общая `coc:character:jacob-smith`; статблок — «Вышел срок» (в путеводителе его нет) |
| `chernovodnyy-ruchey-ru/character/dues-dzho-portello` «Джо Портелло» (официальное) | `arkham-en/character/southside-joe-potrello` «Джузеппе „Джо“ Портелло» | высокая | `same_as` | в английском путеводителе «Potrello»; основное имя — официальное (Р-184), «Потрелло» — в `aliases` | общая `coc:character:joe-potrello`; связь соперничества с О’Баннионом стояла в обеих карточках — оставлена одна (у О’Банниона) |
| `chernovodnyy-ruchey-ru/character/dues-mayki-ketpol` (официальное) | `arkham-en/character/northside-mikey-catchpole` | высокая | нет | — | общая `coc:character:mikey-catchpole` |
| `chernovodnyy-ruchey-ru/character/dues-salnyy-spun` (официальное) | `arkham-en/character/northside-greasy-spoon` | высокая | нет | — | общая `coc:character:greasy-spoon`; основной статблок — «Вышел срок», статблок путеводителя — вариант «Аркхэм» |
| `chernovodnyy-ruchey-ru/character/dues-mardzh-khokler` (официальное) | `arkham-en/character/southside-marge-hockler` | высокая | `same_as` | — | общая `coc:character:marge-hockler`; статблок — «Вышел срок» |
| `chernovodnyy-ruchey-ru/character/dues-lipkiy-dzhek-fulton` (официальное) | `arkham-en/character/southside-jack-fulton` | высокая | `same_as` | — | общая `coc:character:jack-fulton` |
| `chernovodnyy-ruchey-ru/character/dues-entoni-morensi` (официальное) | `arkham-en/character/southside-anthony-morency` | высокая | `same_as` | — | общая `coc:character:anthony-morency` |
| `chernovodnyy-ruchey-ru/character/dues-leksi` «Лекси» (официальное) | `arkham-en/character/southside-lexy-romano` | высокая | `same_as` | в «Вышел срок» без фамилии | общая `coc:character:lexy-romano` |
| `chernovodnyy-ruchey-ru/character/dues-lyusi-kolaski` (официальное) | `arkham-en/character/campus-lucy-kolasky` | высокая | нет | — | общая `coc:character:lucy-kolasky` |
| `chernovodnyy-ruchey-ru/character/dues-khilda-boungreyder` (официальное) | `arkham-en/character/campus-hilda-bonegrader` | высокая | нет | — | общая `coc:character:hilda-bonegrader` |
| `pulp-cthulhu-en/character/chester-armwright` | `arkham-en/character/campus-chester-armwright` | высокая | нет | пульп-профиль — вариант статблока (Р-125) | общая `coc:character:chester-armwright`; статблока в Pulp Cthulhu нет — абзац «В Pulp Cthulhu» |
| `pulp-cthulhu-en/character/francis-morgan` | `arkham-en/character/campus-francis-morgan` | высокая | нет | то же; возраст в путеводителе 31 (текст) / 37 (статблок) | общая `coc:character:francis-morgan`; абзац «В Pulp Cthulhu» |
| `pulp-cthulhu-en/character/william-dyer` | `arkham-en/character/campus-william-dyer` | высокая | нет | то же | общая `coc:character:william-dyer`; абзац «В Pulp Cthulhu» |
| `keepers-companion-en/character/hammer-arkham-police` | `arkham-en/character/generic-police-patrol-officer` | — | нет | не дубль: числа другие, только сходство типажа | не дубль — не трогалось |

## Организации, книги, карты

| Запись другой книги (издание) | Запись путеводителя | Уверенность | Связь | Расхождения | Сделано |
|---|---|---|---|---|---|
| `chernovodnyy-ruchey-ru/organization/dues-mafiya-obanniona` «Мафия О’Банниона» (официальное) | `arkham-en/organization/merchant-obannion-organization` «Организация Дэнни О’Банниона» | высокая | `refs` | официальное название «Мафия О’Банниона» — основным при слиянии | общая `coc:organization:obannion-organization`; основным осталось «Организация Дэнни О’Банниона»: «Мафия О’Банниона» в записи «Вышел срок» — описательное название, данное при переносе (флаг `editorial_text`; в книге — «мафия», «семья», люди О’Банниона), оно в `aliases` |
| `chernovodnyy-ruchey-ru/organization/dues-khram-nadezhdy` (официальное) | `arkham-en/organization/frenchhill-temple-of-hope` | высокая | `refs` | — | общая `coc:organization:temple-of-hope` |
| `dead-light-en/tome/chalice-lesser-key-of-solomon` «Малый ключ царя Соломона» | `arkham-en/tome/southside-lesser-key-of-solomon` «Малый ключ Соломона» | высокая | нет | то же издание 1904 года; кандидат в общую запись справочника `coc:tome:*` (Р-56) | общая `coc:tome:lesser-key-of-solomon`; два экземпляра — в `copies`, автор: Мазерс (перевод), под ред. Кроули |
| `sny-o-yaponii-ru/map/miskatonic-campus` | `arkham-en/map/campus-neighborhood` | — | нет | не дубль: другая карта кампуса; обе остаются | не дубль — не трогалось |
| Другие номера «Arkham Advertiser» (`pobeg-iz-innsmuta-ru/handout/arkham-advertiser-spetsvypusk`, `mothers-love-ru/handout/arkham-advertiser-1928`, `shadows-of-leningrad-en/handout/handout-a-arkham-advertiser`) | `arkham-en/handout/advertiser-1922-page-*` | — | — | не дубли: разные выпуски газеты | не дубли — не трогалось |

## Из отчёта о путеводителе Hort (`hort.md`, «Кандидаты на слияние»)

| Запись | Другая запись | Уверенность | Связь | Сделано |
|---|---|---|---|---|
| `arkham-guide-hort-ru/character/laban-shrewsbury` | `pulp-cthulhu-en/character/laban-shrewsbury` | высокая | `same_as` | общая `coc:character:laban-shrewsbury` (основа и статблок — Hort, абзац «В Pulp Cthulhu»; имя — «Лабан Шрюсбери», «Шрусбери» — в `aliases`) |
| Суонсон Эймс (абзац у `arkham-en/character/campus-stanley-whitman`) | `sny-o-yaponii-ru/character/swenson-ames` | средняя | нет | оставлено: средняя уверенность, отдельной записи в путеводителе нет |

## Кандидаты в общие записи внутри путеводителя

- Персонажи, которые встречаются в нескольких книгах и годятся в общие `coc:character:*`: Кеция Мейсон, Асенат Уэйт, Эдвард Пикман Дерби,
  Дэнни О’Баннион (три книги), Абнер Уик. — **Сделано**: все пять — общие записи (см. «Люди»).
- Рэндольф Картер и Герберт Уэст упоминаются в нескольких частях путеводителя, записей нет — кандидаты в общие записи персонажей.
  — Не сделано: это не слияние, а новые записи.
