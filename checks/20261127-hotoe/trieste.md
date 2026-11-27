# HOTOE, книга III — часть trieste: «Cold Wind Blowing: Trieste 1923» (с. 81–116, 252–255)

Этап `hotoe-book-3-en/scenario/cold-wind-blowing` («Дует холодный ветер: Триест, 1923», order 10). Источник — английский
оригинал (`hotoe-book-3-en`, печатная = физическая − 2), копии раздатки и карт — `hotoe-book-6-handouts-en`, карты —
`hotoe-keeper-maps-en` (8, 11), `hotoe-player-maps-en` (6). Русский текст — наш перевод (`translated`, Р-251, Р-21).

Записей: 82 — места 28 (в т. ч. общий город `coc:location:trieste`), сцены 22, персонажи 14, раздатка 5, карты 4,
предметы 3, существа 2, организации 2, книга Мифов 1, этап 1. Картинки: 7 (5 раздаток, портрет Винкельмана, арт ллойгора)
+ 4 карты в `app/maps/hotoe-trieste-*.jpg`. Предложения: `proposals-trieste.json` (24 правки, 6 записей).

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Trieste 1923 / Cold Wind Blowing (by Russell Waters), вступление | 81 | `scenario/cold-wind-blowing` (summary, advice) |
| Keeper Information | 81–82 | `scenario/cold-wind-blowing` (keeper_info); `character/johann-winckelmann`, `character/francesco-arcangeli` |
| The Lloigor | 82 | keeper_info этапа; `creature/trieste-lloigor`; `organization/trieste-lloigor-cult`; `location/trieste-postumia` |
| Mehmet Makryat | 82–84 | keeper_info этапа; предложение к `hotoe-book-2-en/character/mehmet-makryat` |
| (карта Триеста в главе) | 82 | `map/trieste-city` |
| Врезка «Trieste» | 83 | `coc:location:trieste` (description, history); `location/trieste-grotta-gigante` |
| Brothers of the Skin | 84 | keeper_info этапа; предложение к `coc:organization:brothers-of-the-skin` |
| The Ghost of Winckelmann | 84 | keeper_info этапа; `character/johann-winckelmann` |
| Fenalik | 84 | keeper_info этапа; `scene/trieste-blackshirts-and-hustlers`; предложение к `coc:character:fenalik` |
| Arriving in Trieste | 84–85 | `scene/trieste-arriving`; `location/trieste-station` |
| Asleep in Trieste | 85–86 | `scene/trieste-arriving` (mechanics); `creature/trieste-lloigor` (способность) |
| Врезка «Scenario Timeline» | 85 | таблица этапа «Триест: хронология сценария» |
| Looking up Winckelmann | 86 | `scene/trieste-looking-up-winckelmann` |
| The Museum | 86 | `location/trieste-museo-di-storia-e-darte`; сцена выше |
| Giardino Lapidario | 86–88 | `location/trieste-giardino-lapidario`; сцена выше |
| Trieste Handout #1 | 87 (кн. VI, 99) | `handout/trieste-handout-1-johann-joachim-winckelmann` |
| Врезка «Events in Trieste in 1923» | 87 | `coc:location:trieste` (history) |
| Research; Johann Winckelmann | 88 | `scene/trieste-research`; `location/trieste-city-library` |
| Winckelmann’s Medallions | 88 | `item/trieste-winckelmann-medallions`; `character/ernesto-pabeno` |
| Locanda Grande | 88–89 | `location/trieste-hotel-vanoli`; `location/trieste-piazza-unita-ditalia` |
| Napoleon’s Army | 89 | `scene/trieste-research` |
| Trieste Handout #2 | 89 (кн. VI, 101) | `handout/trieste-handout-2-court-martial` |
| Karst Caverns | 89–90 | `scene/trieste-research`; `location/trieste-environs`, `trieste-grotta-gigante`, `trieste-postumia` |
| Adelsberg, Postumia, Postojna | 90 | `location/trieste-postumia` |
| The Silent Reader | 90 | `scene/trieste-research`; `character/helmut-grossinger` |
| The Termonas; The Family Secret | 90 | `scene/trieste-visiting-antonio`; `character/antoni-termona` |
| Visiting Antonio | 90–92 | `scene/trieste-visiting-antonio`; `location/trieste-termona-house`; `character/marco` |
| Врезка «The Bora» | 90 | таблица города «Триест: бора» (`coc:location:trieste`), ссылка из этапа |
| Trieste Handout #3 | 91 (кн. VI, 103) | `handout/trieste-handout-3-winckelmann-diary` |
| After the Meeting | 92 | `scene/trieste-visiting-antonio` |
| The Translator | 92–93 | `scene/trieste-the-translator`; `character/marcius-montanelli`; `location/trieste-montanelli-house` |
| Winckelmann’s Diary | 93 | `tome/trieste-winckelmann-diary`; `scene/trieste-the-translator` |
| In Their Footsteps (список) | 93 | таблица этапа «Триест: кто идёт по следу сыщиков» |
| Cesare Druni | 93–94 | `scene/trieste-cesare-druni`; `character/cesare-druni` |
| Helmut Grossinger; Helmut’s Hovel | 94–95 | `scene/trieste-helmut-grossinger`; `location/trieste-grossinger-hovel` |
| Trieste Handout #4 | 95 (кн. VI, 105) | `handout/trieste-handout-4-grossinger-journal` |
| The Turkish Businessmen; The Brothers’ Hideout | 95–96 | `scene/trieste-turkish-businessmen`; `location/trieste-salleh-pensione`; `character/fahim-salleh` |
| The Blackshirts | 96 | `scene/trieste-blackshirts-and-hustlers`; `organization/trieste-blackshirts` |
| The Pale Stranger | 96 | `scene/trieste-the-pale-stranger` |
| Hustlers and Thieves; Fenalik | 97 | `scene/trieste-blackshirts-and-hustlers` |
| A Memorable Dinner | 97–98 | `scene/trieste-memorable-dinner` |
| The Haunted Hotel; The Rooms | 98–99 | `scene/trieste-haunted-hotel` |
| Trieste Handout #5 | 99 (кн. VI, 105) | `handout/trieste-handout-5-letter-to-salleh` |
| The Room with the Diary; A Séance; The Next Night | 99–100 | `scene/trieste-haunted-hotel` |
| Searching for Bacchus; Bacchus; Bacchus in Trieste | 100–101 | `scene/trieste-searching-for-bacchus`; `item/trieste-burnett-sketchbook` |
| Walking the Streets | 102 | `scene/trieste-searching-for-bacchus` |
| The Villa of Bacchus; Inside the Villa; Upstairs; The Cellar | 102–103 | `scene/trieste-villa-of-bacchus`; `location/trieste-villa-of-bacchus`; `character/signora-mordelli` |
| Winckelmann Appears | 103–104 | `scene/trieste-villa-of-bacchus` |
| The Medallion of Ithaqua | 104 | `item/trieste-medallion-of-ithaqua` |
| Return to Termona; Shadowing Termona | 104–105 | `scene/trieste-return-to-termona` |
| The Caverns at Postumia | 105–106 | `scene/trieste-to-postumia` |
| Врезка «New Spell: Contact Lloigor» | 106 | предложение к `coc:spell:contact-lloigor` (источник, расхождение цены); `tome/trieste-winckelmann-diary` |
| Into the Depths; Breaking In | 106–107 | `scene/trieste-to-postumia`; `location/trieste-grotte-di-postumia` |
| (карта пещер в главе) | 107 | `map/trieste-postumia` |
| The Tour; “Human Fish”; Lights Out | 107–108 | `scene/trieste-the-tour`; `character/carlo` |
| The Cultist Battle | 109 | `scene/trieste-cultist-battle` |
| Lair of the Lloigor; The Lloigor; Occult Treasure; Surrendering the Medallion; Rage of the Lloigor; Escape | 109–111 | `scene/trieste-lair-of-the-lloigor`; `location/trieste-lloigor-lair`; предложение к `hotoe-book-1-en/item/campaign-simulacrum-right-leg` |
| The Race for the Train; The Vortex | 111–112 | `scene/trieste-race-for-the-train` |
| Hiding in Trieste | 112 | `scene/trieste-hiding-in-trieste` |
| Conclusion (и награды) | 112–113 | `scene/trieste-conclusion`; этап (conclusion, таблица «Триест: награды») |
| Иллюстрация «Attack by the Lloigor» | 112 | картинка `creature/trieste-lloigor` |
| Statistics: Antoni Termona, Marcius Montanelli, Marco, Cesare Druni | 113 | `character/antoni-termona`, `marcius-montanelli`, `marco`, `cesare-druni` |
| Sample Lloigor Cultists | 114 | `character/lloigor-cultists-trieste` (группа, 6 вариантов) |
| Helmut Grossinger; Fahim Salleh | 114 | `character/helmut-grossinger`, `character/fahim-salleh` |
| Sample Brothers of the Skin | 114 | `character/brothers-of-the-skin-trieste` (группа, 6 вариантов) |
| Johann Winckelmann, Ghost | 114 | `character/johann-winckelmann` (ИНТ, МОЩ; портрет со с. 92) |
| Six Blackshirt Thugs | 114–115 | `character/blackshirt-thugs-trieste` (группа, 6 вариантов) |
| Sample Lloigor | 115 | `creature/trieste-lloigor` (instance_of `coc:creature:lloigor`) |
| Giant Olm | 115 | `creature/trieste-giant-olm` |
| Trieste Keeper's Map | 252 (Keeper Maps 8) | `map/trieste-city` |
| Trieste Player’s Map | 253 (Player Maps 6; кн. VI, 145) | `map/trieste-city-players` |
| Grotte di Postumia Keeper's Map | 254 (Keeper Maps 11) | `map/trieste-postumia` |
| Grotte di Postumia Players' Map | 255 (кн. VI, 147) | `map/trieste-postumia-players` |
| Книга VI: Trieste Handouts #1–#5 | 99, 101, 103, 105 | раздатки (текст и картинка) |

Места на карте Триеста (16 номеров + вокзал, почтамт, Арсенал) — все с записями под `coc:location:trieste`; ключ —
таблица города «Триест: места на карте». Районов карты не подписывают — места стоят прямо под городом.

## Не взято (с причиной)

- Атмосферные иллюстрации (фото вокзала, мавзолея, сада, книги, пещер, ужина, спящей женщины, призрака на лестнице,
  мужчины в очках, плакат «Chemins de fer orientaux» на с. 116, фон врезки «Scenario Timeline») — в `atmosphere-trieste.json`
  (Р-241, Р-245). Фото мужчины в очках на с. 106 без подписи — возможно, портрет Термоны (вопрос владельцу).
- Оформление страниц (рисунок дракона в углу колонтитула, рельсы) — не материал книги.
- Пустые оборотные страницы книги VI (с. 100, 102, 104, 106) — пусты.
- Персонажи, упомянутые без роли в игре, — текстом в записях, без своих записей: Джованни и Маркус Термона (предки
  Антони), Николас Бёрнетт (автор альбома), Кавачеппи, граф фон Бюнау, Антон Рафаэль Менгс, участники трибунала 1797 г.
  (Легран, Ласньер, Эрон, Кошфер, Маркетти, Гастон Фёзиль — только в раздатке «Триест 2»), экономка Монтанелли,
  городской служащий, официант, повар, невестка синьоры Морделли.
- Места без сюжета — текстом: Морской музей (Museo del Mare), таверны 1797 года «Иль Капро Убриако» и «Каверна деи
  Реттили» (только в раздатке), тоннель Монтуцца, площадь Карло Гольдони, Большой канал, Монте-Джусто, Виа Марко Поло
  (в записи виллы), Лонгатико, Регенсбург, Любляна, Аквилея. Новых общих городов часть не требует
  (`new-shared-locations-trieste.json` не заведён).
- Список литературы «Making Trieste Italian: 1918–1954» — упомянут в истории города.

## Опечатки и сомнения

- Ключ карты: «Seleh’s Pensione» — в тексте Fahim Salleh (`errata` у `location/trieste-salleh-pensione`).
- Имя Термоны: «Antoni» (с. 82, 85, 93, 109, 113) и «Antonio» (с. 88, 90, 108) — в записи «Antoni» по статблоку.
- Монтанелли: БкУ 0 и Комплекция 0 при СИЛ + ТЕЛ = 90 (ожидается −1); Скорость не напечатана; Уклонения нет.
- Друни: Скорость не напечатана (ожидается 7); Уклонения нет; ПЗ 13 при (45 + 80)/10 = 12,5 (округление вверх — приём книги).
- «Sample Brothers of the Skin»: столбец HP 65–80 вместо 12–15; одно Уклонение 25% ниже половины ЛВК (всё — `errata`, как напечатано).
- «Six Blackshirt Thugs»: одно Уклонение 30% на всю группу, у «One» по правилам 32% (`errata`).
- «Sample Lloigor»: HP 48 при (150 + 300)/10 = 45 — исправлено по большинству (Р-36, `errata` fixed, `corrections`).
- «Giant Olm»: Fighting (Slam) 60% (30/6) — исправлено на (30/12) (Р-35); шанс захвата не напечатан.
- Раздатка «Триест 2»: «Cochefer» и «Cachefer» — как напечатано.
- «Grotto Gigante» (с. 83) и «Grotta Gigante» (с. 89); «Ospitale Civile» на карте (итал. Ospedale) — как напечатано.
- Подпись фото на с. 101: «investagators».
- Карта пещер для игроков — масштаб в ярдах, для Хранителя — в метрах.
- Обязательность главы: задание называет её необязательной, а таблица книги I (с. 43) — «Core»; в записи — основная
  (как и в записи кампании). Хронология «Scenario Timeline» допускает поездку в Постумию без медальона.
- Общая запись `coc:item:medallion-of-ithaqua` (энциклопедия «Миры Лавкрафта», по Дерлету) — другой предмет; книга их не
  связывает. Медальон HOTOE — своя запись `item/trieste-medallion-of-ithaqua` со ссылкой (вопрос владельцу о слиянии).
- Заклинание «Связь с ллойгором»: в HOTOE 3 ПМ и 3 Рассудка, в Grand Grimoire — 3+ ПМ и 1d3 Рассудка (предложение в `quality.notes`).
- Чернорубашечники есть и у части venice (`organization/venice-blackshirts`, профиль `character/blackshirt-thugs` — другие
  числа) — кандидат в общую запись `coc:organization:blackshirts` (решение ведущего).

## Ссылки на записи других частей (ждут их)

- `hotoe-book-4-en/character/selim-makryat` (constantinople): `character/fahim-salleh`, `handout/trieste-handout-5-letter-to-salleh`,
  этап, `scene/trieste-turkish-businessmen`, `scene/trieste-hiding-in-trieste`.
- `hotoe-book-3-en/scenario/little-cottage-in-the-wood` (belgrade): этап (шаг «Заключение»), `scene/trieste-conclusion`.
- Остальные ссылки на чужие записи (кампания, правая нога, Смит, Мехмет, этап Венеции) уже разрешаются.

## Термины (английский → русский)

| English | Русский |
|---|---|
| Cold Wind Blowing | Дует холодный ветер (как в записи кампании) |
| Trieste / Tergeste | Триест / Тергесте |
| Postumia / Postojna / Adelsberg | Постумия / Постойна / Адельсберг |
| Grotte di Postumia | пещеры Постумии |
| The Lloigor Grotto / Lair of the Lloigor | Грот ллойгоров / логово ллойгоров |
| Grotta Gigante | Гротта-Гиганте |
| Karst | Карст |
| bora | бора |
| lloigor | ллойгор (глоссарий) |
| Ithaqua, the Wind Walker | Итакуа, Идущий с ветром |
| Wendigo | Вендиго |
| Medallion of Ithaqua | медальон Итакуа |
| Winckelmann’s Diary | дневник Винкельмана |
| Contact Lloigor | Связь с ллойгором (как в справочнике) |
| Ritual of Cleansing | Очистительный ритуал (как в справочнике) |
| Sedefkar Scrolls | Свитки Седефкара |
| Baleful Influence | Пагубное влияние |
| Right Leg (of the Simulacrum) | правая нога Симулякра |
| Sedefkar Simulacrum | Симулякр Седефкара |
| Brothers of the Skin | Братья кожи |
| The Skinless One | Бескожий |
| dead men’s eyes | глаза мертвецов |
| Turkish businessmen | турецкие дельцы |
| Cult Skinning Knife | культовый нож для свежевания |
| Flesh Creeper / Create Flesh Creeper | ползучая плоть / Создать ползучую плоть |
| Control Skin; Transfer Body Part | Управлять кожей; Пересадка части тела |
| Blackshirts | чернорубашечники |
| Hustlers and Thieves | ловкачи и воры |
| The Pale Stranger | бледный незнакомец |
| A Memorable Dinner | незабываемый ужин |
| The Haunted Hotel | гостиница с привидением |
| Searching for Bacchus | в поисках Вакха |
| Bacchus / Dionysus; maenads; satyrs | Вакх / Дионис; менады; сатиры |
| The Villa of Bacchus | Вилла Вакха |
| olm / “human fish” (pesce umano) | протей / «человеческая рыбка» |
| Giant Olm | гигантский протей |
| implosion vortex | вихрь-имплозия |
| Museo di Storia e d'Arte | Музей истории и искусства |
| Giardino Lapidario | сад Лапидарий |
| Cattedrale San Giusto / Castello di San Giusto | собор Сан-Джусто / замок Сан-Джусто (Кастелло) |
| Piazza Unità d'Italia | площадь Единства Италии |
| Locanda Grande / Hotel Vanoli | «Локанда Гранде» / отель «Ваноли» |
| Municipio | Ратуша |
| Arsenal de Lloyd | Арсенал Ллойда |
| Antoni (Antonio) Termona; Marcius Montanelli; Marco; Cesare Druni | Антони (Антонио) Термона; Марций Монтанелли; Марко; Чезаре Друни |
| Helmut Grossinger; Fahim Salleh; Carlo | Хельмут Гроссингер; Фахим Салле; Карло |
| Johann Joachim Winckelmann; Francesco Arcangeli | Иоганн Иоахим Винкельман; Франческо Арканджели |
| Ernesto Pabeno; Signora Mordelli; Nicholas Burnett | Эрнесто Пабено; синьора Морделли; Николас Бёрнетт |
| Mehmet / Selim Makryat | Мехмет / Селим Макрьят (как в записях частей london, campaign) |
| Feign Death; Show Contempt; Lurk; Debate; Wheel-Chair | Притворная смерть; Презрение; Затаиться (глоссарий); Спор; Инвалидное кресло (навыки без механики, Р-126) |
| Art (Skin Human) | Искусство (свежевание людей) |
