# HOTOE, книга IV — часть return: «Blue Train, Black Night» и «The Fog Lifts» (с. 85–126, 186–187)

Этапы `hotoe-book-4-en/scenario/blue-train-black-night` («Синий поезд, чёрная ночь: через Европу, 1923», order 17) и
`hotoe-book-4-en/scenario/the-fog-lifts` («Туман рассеивается: снова Лондон, 1923», order 18). Источник — английский
оригинал (`hotoe-book-4-en`, печатная = физическая − 2), копии раздатки — `hotoe-book-6-handouts-en` (с. 169–172).
Русский текст — наш перевод (`translated`, Р-251, Р-21).

Записей: 72 — этапы 2, сцены 22, персонажи 16 (13 со статблоком, 3 без), места 16, существа 4, книги Мифов 4,
раздатка 3, предметы 2, карта 1, общие заклинания 2 (`kb/spells/ritual-of-cleansing.json`, `kb/spells/ritual-of-enactment.json`).
Картинки: 16 у своих записей (12 портретов, арт Бескожего, 3 раздатки) + 2 предложены чужим записям (вагон-собор,
Свитки Седефкара) в `art-return-proposals.json`; карта `app/maps/hotoe-return-calais-coach.jpg`.
Предложения: `proposals-return.json` — 68 правок, 16 записей. Атмосфера: `atmosphere-return.json` (11).

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Across Europe 1923 / Blue Train, Black Night (Geoff Gillan, Nick Hagger), вступление | 85 | `scenario/blue-train-black-night` (summary) |
| Keeper Information | 85–86 | этап (keeper_info); предложение к `hotoe-book-2-en/character/mehmet-makryat` |
| The Simulacrum Empowered | 86 | таблица этапа «Синий поезд: силы Симулякра»; предложение к `coc:item:sedefkar-simulacrum` |
| Investigator Deterioration; Deterioration Effect Table; Body Location Table | 86, 88 | этап (keeper_info), таблицы «Синий поезд: разложение», «Синий поезд: части тела» (ссылки из «Туман рассеивается») |
| Врезка «What If The Investigators Choose to Fly?» (Availability, Hazards and Delays, Trouble in the Air, Rejoining the Express, Mehmet Alone, Arriving at Croydon Aerodrome) | 87 | `scene/bluetrain-flying-to-london` |
| Boarding; On the Platform | 88–89 | `scene/bluetrain-boarding` |
| Fellow Travelers; Compartments and Washrooms | 89 | `scene/bluetrain-boarding`; `location/bluetrain-calais-coach` и 11 мест купе |
| Emile Soucard | 89–90 | `character/emile-soucard`; сцена посадки |
| (1) Luigi Martinelli (статблок) | 90–91 | `character/luigi-martinelli` |
| (3) Jack Gatling (статблок) | 91 | `character/jack-gatling` |
| Врезка «On Skinning Humans» (William A. Workman) | 91 | этап `blue-train-black-night` (advice, полный перевод) |
| (5) Sir Robert Harrow, Bart.; An Unhappy Investigator (статблок) | 92 | `character/robert-harrow` |
| (7) Elena Costanza; An Unhappy Investigatrix (статблок) | 92 | `character/elena-costanza` |
| (9 & 10) The Count And Countess (статблоки Henri, Emmanuelle) | 92–93 | `character/henri-de-bruessy`, `character/emmanuelle-de-bruessy` |
| (11) Kurt Groenig (статблок) | 93–94 | `character/kurt-groenig` |
| (12) Rama Ho-Tet (статблок) | 94–95 | `character/rama-ho-tet` |
| (14) Lord Margrave (статблок) | 95 | `character/michael-margrave` |
| (15) La Doña Del Garda (статблок) | 95–96 | `character/margarita-del-garda` |
| (16) Danton Szorbic (статблок) | 96–97 | `character/danton-szorbic` |
| Investigator Actions; The Fourgons; Passenger Berths; Dining Car, Salon Car; Engine & Tender | 97–98 | `scene/bluetrain-investigator-actions` |
| Врезка «What If the Investigators Catch Makryat early?» | 98 | `scene/bluetrain-investigator-actions` |
| A Little Train of Horrors | 98–99 | таблица этапа «Синий поезд: хронология»; `scene/bluetrain-day-one` |
| Схема вагона Кале (места 1–17) | 99 | `map/bluetrain-calais-coach` (17 меток → 10 купе и место проводника) |
| Day One; London Newspapers | 99–100 | `scene/bluetrain-day-one` |
| Return Handout #1 | 100 (кн. VI, 169) | `handout/bluetrain-handout-1-shopkeeper-murdered` |
| Night One (отравленный графин; 23:25; 00:01; 00:19; 00:40; 03:20; 04:35) | 100–103 | `scene/bluetrain-night-one` |
| Day Two (11:15; 12:48; 14:28; 14:58) | 103 | `scene/bluetrain-day-two` |
| Night Two (18:43; 20:04; полночь) | 103–104 | `scene/bluetrain-night-two-belgrade` |
| Night Two (полночь — Гатлинг; 01:13; 03:17; 03:23; 04:05) | 104–105 | `scene/bluetrain-night-two-flesh-creepers` |
| Day Three; More London Newspapers; 08:30; 09:32; 16:10 | 105–106 | `scene/bluetrain-day-three` |
| Return Handout #2 | 106 (кн. VI, 169) | `handout/bluetrain-handout-2-vagrant-slain` |
| Night Three | 106–107 | `scene/bluetrain-night-three-locomotive-beast` |
| A New Development | 107 | та же сцена; `creature/bluetrain-locomotive-beast` |
| The Cathedral Car; The Meeting; Attacking Makryat | 107, 109–110 | `scene/bluetrain-cathedral-car`; предложение к `hotoe-book-1-en/location/express-cathedral-car` |
| Иллюстрация вагона-собора | 108 | картинка, предложенная `express-cathedral-car` (`art-return-proposals.json`) |
| Врезка «Detransference» | 109 | ссылка на `coc:spell:detransference` + предложение (источник, абзац) |
| If Mehmet Makryat Survives; About the Prince | 110 | `scene/bluetrain-makryat-destroyed` |
| Paris at Dawn | 110–111 | `scene/bluetrain-paris-at-dawn`; `item/bluetrain-duke-of-york-dossier` |
| The Scrolls; The Scroll of the Belly; The Scroll of the Legs; The Scroll of the Right Hand | 111–112 | `tome/bluetrain-scroll-of-the-belly`, `-legs`, `-right-hand`; общее `coc:spell:ritual-of-enactment` |
| Conclusion; Sanity Rewards | 112 | `scene/bluetrain-paris-at-dawn`; этап (conclusion, таблица «Синий поезд: награды») |
| Statistics: Mehmet Makryat (Soucard, et al.) | 113 | предложение: вариант статблока у `hotoe-book-2-en/character/mehmet-makryat` |
| Brothers of the Skin, 12 Madman Cultists (таблица One–Twelve, части мертвецов) | 113 | `character/brothers-of-the-skin-across-europe` (12 вариантов); таблица этапа «Синий поезд: части мертвецов у Братьев» |
| Baba Yaga; Lloigor Cultists (отсылки) | 113 | текст сцен; `hotoe-book-3-en/character/lloigor-cultists-trieste` (ссылка) |
| Flesh Creeper | 114 | `creature/bluetrain-flesh-creeper` |
| The Locomotive Beast, Avatar of The Skinless One | 114 | `creature/bluetrain-locomotive-beast` |
| Duc Jean Floressas des Esseintes (Jigsaw Prince) | 114 | предложение: вариант статблока у `hotoe-book-2-en/character/jean-floressas-des-esseintes` |
| London Again 1923 / The Fog Lifts (Geoff Gillan, Mike Lay), вступление; Keeper Information | 115 | `scenario/the-fog-lifts` (summary, keeper_info) |
| Arrival in London | 115–116 | `scene/foglifts-arrival-in-london`; `location/foglifts-victoria-station`; `character/bill-the-cabbie` |
| План «The Shop» | 116 | тот же план, что `hotoe-book-2-en/map/london-the-shop` — предложение добавить источник |
| Strangeness in Islington; Arthur Bowman | 116 | `scene/foglifts-strangeness-in-islington`; `character/arthur-bowman` |
| Return Handout #3 | 117 (кн. VI, 171) | `handout/foglifts-handout-3-schoolmaster-missing` |
| Robert Osborne | 117 | `location/foglifts-osbornes-outfitters`; сцена |
| The Homeless Man | 117 | `location/foglifts-bookbinders-arms`; сцена |
| Detective Chief Inspector Joseph Phillips | 117 | `character/joseph-phillips` |
| Further Events | 117 | `scene/foglifts-strangeness-in-islington` |
| The Antique Shop; The Lurker On The Ceiling; The Pattern On The Floor; The Captive In The Cupboard; The Scroll On The Desk | 118–119 | `scene/foglifts-the-antique-shop`; `creature/foglifts-skin-devil-beddows`; `item/foglifts-false-ritual-transcript`; предложения к `london-makryats-shop`, `london-makryats-shop-office`, `james-beddows` |
| The False Ritual; Makryat Reborn | 119 | `scene/foglifts-false-ritual` |
| Врезка «What If Mehmet Escapes?» | 119 | `scene/foglifts-what-if-mehmet-escapes` |
| (текст и иллюстрация) None wears the simulacrum; The usurper is unworthy | 120 | `scene/foglifts-the-skinless-one`; картинка `creature/foglifts-skinless-one` |
| Врезка «A Substitute Sacrifice» | 121 | `scene/foglifts-false-ritual` |
| Врезка «What If the Investigators Avoid the False Transcript?» | 121 | `scene/foglifts-scroll-of-the-left-hand` |
| The Gift of Skin is Revoked | 121 | `scene/foglifts-the-skinless-one` |
| Scroll Of The Left Hand; The Scroll of the Left Arm (числа); The End Of The Scrolls | 121–123 | `tome/foglifts-scroll-of-the-left-hand`; `scene/foglifts-scroll-of-the-left-hand` |
| Врезка «Beating Makryat to London» | 122 | `scene/foglifts-beating-makryat-to-london` |
| Врезка «The Ritual of Cleansing» | 122 | новое общее `coc:spell:ritual-of-cleansing` |
| Conclusion (награды); The End For Now; Gratitude | 123 | `scene/foglifts-conclusion`; таблица этапа «Туман рассеивается: награды» |
| Statistics: Skin Devil, Formerly Known as Beddows | 125 | `creature/foglifts-skin-devil-beddows` (instance_of `crusader-skin-devil`) |
| Arthur Bowman (статблок) | 125 | `character/arthur-bowman` |
| Mehmet Makryat, Ageless, Reincarnated Leader of the Brothers | 125–126 | предложение: вариант «Возрождённый» у `mehmet-makryat` |
| The Skinless One (статблок, Cult, Other Characteristics) | 126 | `creature/foglifts-skinless-one` (instance_of `coc:creature:skinless-one`); культ — предложение к `coc:organization:brothers-of-the-skin` |
| The Shop (Complete Maps) | 186 | предложение: источник у `hotoe-book-2-en/map/london-the-shop` (тот же план) |
| с. 187: «Sleeper F», «Sleeper G» | 187 | не взято — см. ниже (схемы вагонов 2013 года главы «The Simulacrum Unbound») |
| Книга VI: Return Handouts #1–#3 | VI: 169, 171 | раздатки (текст и картинка) |

## Не взято (с причиной)

- С. 187 — схемы спальных вагонов «Sleeper F» и «Sleeper G» с именами пассажиров 2013 года (Giuseppe Roti и др.): это
  карта главы «The Simulacrum Unbound» (часть modern; в её записях уже есть `location/modern-sleeping-car-f`,
  `modern-sleeping-car-g`). Карту с метками должна завести часть modern (префикс `modern-`, не мой) — передать ведущему.
- С. 124 — плакат «Orient Express» (атмосфера); с. 108 — иллюстрация вагона-собора (предложена картинкой
  `express-cathedral-car`); прочие атмосферные картинки и фоны врезок — `atmosphere-return.json`.
- Подпись к фото Галатской башни на с. 123 (Хезарфен Ахмед Челеби) — подпись к иллюстрации главы «Константинополь»,
  попавшая на эту страницу; в `atmosphere-return.json`.
- Пустые страницы: с. 124 (только плакат), книга VI с. 170, 172 (оборотные).
- Упомянутые без роли в игре — текстом в записях, без своих записей: начальник бригады и метрдотель (безымянный
  персонал Wagons-Lits; их общие должности — правило `express-simplon-orient-express-operations`), охранники
  фургонов, горничная доньи, ночной носильщик в Загребе, кочегар, паж принца, переводчик в Британском музее,
  мисс Джейн Паркс, Роберт Осборн (в записи магазина), бродяга, поверенный Макрьята, леди Марграв, покойный муж
  доньи, Эд Гейн, Георг V, Эдуард VIII, герцог Йоркский, миссис Симпсон, сэр Дуглас Резерфорд и лейтенант
  Хеннесси (персонажи главы «Константинополь»).
- Места без сюжета — текстом: Арад, Свиленград, Синекли, Цариброд, Ниш-Црвени-Крст, Любляна, Загреб, Симплонский
  туннель, Лозанна, Ломбардия, Кале, Балморал, школа на Ганновер-стрит, пансион на Орлстон-роуд, Британская
  библиотека. Новых общих городов часть не требует (`new-shared-locations-return.json` не заведён).
- Баба-яга, Лесной ходок, чёрные куры, избушка — записи части belgrade (пока не заведены) — текстом, без ссылок.

## Опечатки и сомнения

- Харроу: «as Barrow» (с. 122) — опечатка, в остальном Harrow (`errata` у `character/robert-harrow`).
- Свиток: блок чисел озаглавлен «THE SCROLL OF THE LEFT ARM» (с. 122), в тексте — Scroll of the Left Hand (`errata`).
- Элена Костанца: строка языков напечатана под заголовком «Skills» (с. 92) — исправлено.
- Филлипс: в раздатках — Detective Inspector, в тексте — Detective Chief Inspector (`errata`).
- Принц: потеря Рассудка 2/1D6 (с. 109) и 2/1D6+1 (с. 114) — в предложении `errata` к его записи.
- Зверь-локомотив: БкУ +10D6 и Комплекция 11 при СИЛ + ТЕЛ = 1000 (по правилам +11d6 и 12) — как напечатано, вопрос владельцу.
- Бескожий («Ужас в Восточном экспрессе»): Комплекция 1 при СИЛ + ТЕЛ = 200 и БкУ +1D6 — исправлено на 2 по большинству (Р-36).
- Братья кожи (12): общие Уклонение 25%, ПМ 12, Скорость 8 не сходятся с ЛВК, МОЩ и ТЕЛ отдельных Братьев (`errata`).
- Граф де Брюсси: урон «8mm Lebel Revolver» 1D8-1 (в «Книге хранителя» 1d8) — как напечатано.
- ПЗ с округлением вверх (Костанца, граф, графиня, Марграв, дель Гарда) — приём книги (Р-161).
- Портреты графа и графини (с. 95) отнесены по подписи «de Bruessy» между снимками — вывод, не подпись под каждым.
- Фото женщины на с. 100 без подписи — возможно, кто-то из пассажирок (вопрос владельцу; в атмосфере).
- Обратный поезд — сам «Симплон-Ориент-экспресс» (запись части express): своего «корабля» глава не заводит, вагон
  Кале с купе — места под ним (задание называло «the return train (корабль)»; решение ведущего).
- Свитки Чрева, Ног, Правой и Левой руки — книги Мифов в папке тома (мне не принадлежит `kb/tomes`); по образцу
  `coc:tome:scroll-of-the-head` их стоит перенести в общие записи. Задание называет у части constantinople общий
  `kb/tomes/scroll-of-the-body.json` — такого свитка в книге нет (есть Свиток Чрева, Belly): проверить, не дубль ли.
- «Лоскутный принц» (запись части lausanne-milan) — у частей campaign и fez другие формы («Принц-мозаика»,
  «Принц-Головоломка»); здесь — по записи-владельцу.
- Заклинания «Turn to Skin», «Contact Skinless One», «Create Skin Beast», «Skin of the Sedefkar», «Animate Skin» —
  новые заклинания главы «Константинополь»; в справочнике их нет, в статблоках и свитках — `spell: null`.

## Ссылки на записи других частей

Все ссылки моих записей разрешаются (проверено `tools/check.py`): этапы `by-the-skin-of-the-teeth`, `the-simulacrum-unbound`,
`little-cottage-in-the-wood`, `in-a-city-of-bells-and-towers`, персонаж `selim-makryat` уже в базе.

## Термины (английский → русский)

| English | Русский |
|---|---|
| Blue Train, Black Night; Across Europe 1923 | Синий поезд, чёрная ночь; через Европу, 1923 (как в записи кампании) |
| The Fog Lifts; London Again 1923 | Туман рассеивается; снова Лондон, 1923 |
| Calais coach / through-coach to Calais | вагон Кале |
| conducteur; Chef de Brigade; Maître d’Hôtel | проводник; начальник бригады; метрдотель (как у части express) |
| fourgon; salon car; dining car; engine & tender | фургон; салон-вагон; вагон-ресторан; паровоз и тендер |
| Wagons-Lits | Wagons-Lits (Международная компания спальных вагонов) |
| Interallied Police | межсоюзническая полиция |
| Investigator Deterioration; Deterioration Effect Table; Body Location Table | разложение сыщиков; таблица разложения; таблица частей тела |
| The Simulacrum Empowered | Симулякр, наделённый силой |
| Ritual of Enactment | Ритуал свершения (как в записи кампании) |
| Ritual of Cleansing | Ритуал очищения (не «Очистительный ритуал» Grand Grimoire) |
| Detransference | Обратный перенос (справочник) |
| Turn to Skin; Contact Skinless One; Create Skin Beast; Skin of the Sedefkar; Animate Skin | Обратить в кожу; Связь с Бескожим; Создать кожаного зверя; Кожа Седефкара; Оживить кожу |
| Flesh Creeper | ползучая плоть (как у частей london, trieste) |
| Locomotive Beast | Зверь-локомотив |
| Skin Devil | кожаный дьявол (глоссарий) |
| The Skinless One; Skinning Gaze | Бескожий; Свежующий взгляд |
| Jigsaw Prince | Лоскутный принц (по записи-владельцу) |
| Cathedral Car | вагон-собор (запись части express) |
| Baba Yaga; Walker in the Woods | Баба-яга; Лесной ходок |
| Scroll of the Belly / Legs / Right Hand / Left Hand (Left Arm) | Свиток Чрева / Ног / Правой руки / Левой руки |
| Sedefkar Scrolls | Свитки Седефкара |
| False Ritual / transcript | фальшивый ритуал / фальшивая транскрипция |
| A Substitute Sacrifice | запасная жертва |
| Makryat Reborn | Макрьят возрождённый |
| Cult Skinning Knife; Art (Skin Human); Quoit | культовый нож для свежевания; Искусство (свежевание людей); метательное кольцо |
| Seal Mouth; Asphyxiation | Запечатать рот; удушье |
| Suck; Bowel Flail | Сосание; Удар кишкой |
| Spit Flame; Flesh Tentacle; Crush Under Wheels | Плевок пламенем; Щупальце из плоти; Раздавить колёсами |
| Luigi Martinelli; Jack Gatling; Sir Robert Harrow, Bart. | Луиджи Мартинелли; Джек Гатлинг; сэр Роберт Харроу, баронет |
| Elena Costanza; Henri Matthieu, Count de Bruessy; Emmanuelle | Элена Костанца; Анри Матьё, граф де Брюсси; Эммануэль |
| Kurt Groenig; Rama Ho-Tet; Lord Michael Margrave, Baron of Blackpool | Курт Грёниг; Рама Хо-Тет; лорд Майкл Марграв, барон Блэкпул |
| Doña Margarita del Garda; Danton Szorbic; Emile Soucard | донья Маргарита дель Гарда; Дантон Сорбич; Эмиль Сукар |
| Arthur Bowman; Joseph Phillips (DCI); Bill; Jane Parks; Robert Osborne | Артур Боумен; Джозеф Филлипс (старший инспектор); Билл; Джейн Паркс; Роберт Осборн |
| Groenig Fabrikat | «Грёниг Фабрикат» |
| Victoria Station; Croydon Aerodrome; Gare de Lyon; Sirkeci station | вокзал Виктория; аэродром Кройдон; Лионский вокзал; вокзал Сиркеджи |
| Osborne’s Gentlemen’s Outfitters; Nelson Street | магазин мужской одежды Осборна; Нельсон-стрит |
| Bookbinder’s Arms; Combe Street | паб «Герб переплётчика»; Комб-стрит |
| Hanover Street School; Orleston Road; Brophy Lane | школа на Ганновер-стрит; Орлстон-роуд; Брофи-лейн |
| Svilengrad; Sinekli; Tzaribrod; Nis-Crveni Krst; Ljubljana; Simplon Tunnel | Свиленград; Синекли; Цариброд; Ниш-Црвени-Крст; Любляна; Симплонский туннель |
| Duke of York; Windsor | герцог Йоркский; Виндзоры |
| siderodromophobia | сидеродромофобия |
| Bleriot-Spad 33; Compagnie Franco-Roumaine de Navigation Aérienne | «Блерио-СПАД 33»; «Компани франко-румэн де навигасьон аэрьен» |
