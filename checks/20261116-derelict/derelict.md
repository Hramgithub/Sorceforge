# «The Derelict» (`the-derelict-en`) — сверка полноты (Р-134, Р-251)

Часть `derelict`, вся книга. Сэнди Петерсен при участии Майка Мейсона, Chaosium, 2016 (Free RPG Day, Item #23150).
Источник — английский оригинал; русский текст — наш перевод (флаг `translated`). Эпоха — `modern` (февраль 2016).
Русского перевода сценария в базе нет (проверены имена и названия: Groenland/Гренланд, Delilah/Делайла, sciapod/скиапод,
Engström, Löfgren, McQuinlan и др.).

**Страницы.** В PDF 50 страниц. Физ. 1 — обложка-разворот (передняя и задняя), физ. 2 — титул, физ. 3 — выходные данные,
физ. 4 — оглавление (без номеров); с физ. 5 напечатаны номера 4, 5, … — **печатная = физическая − 1, offset −1** (в
`pipeline/source/books.json` у книги `offset` не задан — ставит ведущий). Готовые сыщики — физ. 25–48 = **с. 24–47**
(в задании сказано «25–48» печатных — на деле это физические). Физ. 49 (с. 48) — реклама, физ. 50 — тот же разворот, что
обложка.

**Записи** — `kb/books/the-derelict-en/` (100): сценарий 1, сцены 11, персонажи 12 (6 готовых сыщиков `pregen`, 2 NPC
яхты с придуманными именами, капитан, старший механик и радист рефрижератора, групповой профиль экипажа), существо 1
(скиапод), организация 1, предметы 14, раздатка 1, места 56 (Северная Атлантика, айсберг, 2 корабля, палубы, уровни и
помещения), карты 3. Картинки: 6 портретов, арт скиапода, иллюстрация к луку, иллюстрация столовой экипажа, 2 листа
раздатки (`app/art/*/derelict-*.webp`); карты — `app/maps/derelict-*.jpg` (3).

Прегены: листы и предыстории — картинки страниц книги (с. 24–47); тексты предысторий и «The Derelict» Agenda сверены с
полями формы отдельных PDF владельца (`[EN 7e] <имя>.CoC7e…background.pdf`; поля «Background», «Background2»; в листах
полей нет).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «The Derelict. A Tale of Terror for Call of Cthulhu», текст задней обложки | физ. 1, 50 | `scenario/the-derelict` (summary, sources); картинка — `atmosphere.json` |
| Титул | физ. 2 | `scenario/the-derelict` (sources) |
| Credits (Sandy Petersen, Mike Mason, M. Wayne Miller, Stephanie McAlea, Ron McClug…) | физ. 3 | `scenario/the-derelict` (summary, sources) |
| Table of Contents | физ. 4 | `scenario/the-derelict` (sources) |
| Getting Ready to Play | с. 4 | `scene/investigators` (подготовка), `scenario.advice` |
| Foreword (Sandy Petersen, 2016) | с. 4 | `scenario.keeper_info` («Предисловие»), `creature/sciapod` (legend) |
| The Derelict (вступление) | с. 5 | `scenario.summary`, `keeper_info` |
| The Investigators (Option One / Option Two, профессии) | с. 5 | `scene/investigators`; `scenario.hook` |
| Important note (серебро) | с. 5–6 | `scene/investigators`; `creature/sciapod` (способность «Невидимость»); `scenario.keeper_info` |
| Delilah, Luxury Yacht (врезка, характеристики) | с. 6 | `location/delilah` (+ палубы, рубка, каюты, машинное отделение) |
| Geneva Convention on the High Seas (врезка, Article 98) | с. 6 | `scene/start` (полный текст врезки) |
| Start | с. 6 | `scene/start`; `scenario.hook` |
| Sequence of Events (пункты) | с. 6, 8 | `scenario.steps`; `scene/start`, `using-the-radio`, `exploring-the-reefer`, `hold-1`, `the-hunt` |
| Deck Plan of The Delilah | с. 7 | `map/delilah-deck-plan` (43 метки) |
| Salvage Rights (Law of Salvage, Law of Finds) | с. 8–9 | `item/maritime-law-books` (полный текст); `scenario.advice` |
| Using the Radio | с. 9 | `scene/using-the-radio`; `location/delilah-wheelhouse` |
| Groenland Tropisch, Reefer Ship (характеристики) | с. 9 | `location/groenland-tropisch`; `organization/simmons-and-calvert` |
| Exploring the Reefer | с. 9, 12 | `scene/exploring-the-reefer`; `location/groenland-tropisch` (history) |
| Deck Plan of Groenland Tropisch (разрез, палуба, грузовые уровни, паспорт судна) | с. 10 | `map/groenland-tropisch-deck-plan` (51 метка); паспорт — `location/groenland-tropisch` |
| Deck Plan of Groenland Tropisch (надстройка, ключ 1–28, карта маршрута) | с. 11 | `map/groenland-tropisch-superstructure` (67 меток); места 1–28 — `location/gt-*` |
| Main Deck; Cranes; Possible discoveries | с. 12 | `location/gt-main-deck` (таблица находок), `gt-cranes`, `gt-lifeboat` |
| Superstructure: Level One, Kitchen | с. 12 | `location/gt-level-1` |
| Food stores | с. 12 | `location/gt-food-stores` |
| CO2 room | с. 12–13 | `location/gt-co2-room`; `item/co2-bottles` |
| Cargo office | с. 13 | `location/gt-cargo-office`; `item/cargo-manifest` |
| Captain’s office | с. 13 | `location/gt-captain-office`; `item/captains-log`, `maritime-law-books` |
| Chief engineer’s office | с. 13 | `location/gt-chief-engineer-office`; `item/chief-engineer-papers` |
| Officers’ dining room | с. 13 | `location/gt-officers-dining-room` |
| Galley kitchen | с. 13 | `location/gt-galley` |
| Crew’s dining room; Possible discoveries | с. 13 | `location/gt-crew-dining-room` (таблица находок) |
| The Crew’s Dining Room (иллюстрация) | с. 14 | картинка `location/gt-crew-dining-room` |
| Superstructure: Level Two, Crew Quarters; Possible discoveries | с. 13–14 | `location/gt-level-2` (таблица находок) |
| Crew cabins | с. 13 | `location/gt-crew-cabins` |
| Crew lounge | с. 13 | `location/gt-crew-lounge` |
| Medical room | с. 13–14 | `location/gt-hospital` |
| Superstructure: Level Three, Officers’ Quarters; Possible discoveries | с. 14 | `location/gt-level-3` (таблица находок), `gt-officer-cabins`, `gt-officers-laundry`, `gt-officers-lounge`; `item/crystal-harpoon` |
| Keeper note (каюта с книгами) | с. 15 | `scene/saga-cabin`; `item/norse-sagas-volume`, `silver-fountain-pen` |
| Erik the Red’s Saga (врезка) | с. 15 | `scene/saga-cabin`, `item/norse-sagas-volume` (полный текст врезки) |
| Superstructure: Level Four, Senior Officers’ Quarters | с. 15 | `location/gt-level-4`, `gt-recreation-room`, `gt-lifeboat` |
| Radio operator’s cabin | с. 15 | `location/gt-radio-operator-cabin`; `character/thorolf-lofgren`; `item/silver-razor` |
| Captain’s cabin | с. 15 | `location/gt-captain-cabin`; `item/silver-letter-opener`, `rum-decanter`, `captains-log` |
| Chief engineer’s cabin | с. 15 | `location/gt-chief-engineer-cabin`; `item/chief-engineer-papers` |
| Handout: Derelict 1 - Pages from Erik the Red’s Saga | с. 16–17 | `handout/derelict-1-erik-the-reds-saga` (текст обеих страниц + перевод, 2 картинки) |
| Possible discoveries (уровень 4) | с. 18 | `location/gt-level-4` (таблица находок); `character/helmar-engstrom` |
| Superstructure: Level Five, Wheelhouse; Keeper note; Possible discoveries | с. 18 | `location/gt-level-5` (таблица находок), `gt-wheelhouse`, `gt-radio-room` |
| Cargo Holds (Hold 1–3); Keeper note; Possible discoveries | с. 18–19 | `location/gt-cargo-holds` (таблица находок), `gt-hold-1`, `gt-hold-2`, `gt-hold-3`; `scene/hold-1`; `item/bulldozer`, `forklift` |
| A grisly discovery | с. 19 | `scene/hold-1`; `location/gt-hold-1`; `character/groenland-crew` |
| Engine Room; Keeper note; Possible discoveries | с. 19 | `location/gt-engine-room` (таблица находок); `scene/engine-room-lights` |
| Searching the Iceberg | с. 19, 21 | `scene/searching-the-iceberg`; `location/iceberg` |
| The Sciapod, The Horror from Ancient Norse “History” (иллюстрация) | с. 20 | картинка `creature/sciapod` |
| Combating the Sciapod (Using flour or ice, a trap, the bulldozer/forklift, the reefer’s cranes, CO2) | с. 21 | `scene/combating-the-sciapod`; `item/co2-bottles`, `bulldozer`, `forklift`; `location/gt-cranes` |
| Injured? | с. 22 | `scene/combating-the-sciapod`; `creature/sciapod` (encounters) |
| Conclusion (текст для чтения вслух) | с. 22 | `scene/epilogue`; `scenario.conclusion` |
| Appendix: Non-Player Characters — Yacht Captain | с. 22 | `character/glenn-harding` (имя придумано, Р-150) |
| Appendix: Non-Player Characters — Captain’s Mate | с. 22 | `character/kevin-riordan` (имя придумано, Р-150) |
| The Sciapod (описание, «SCIAPOD, great footed and hungering thing», Combat, Clutch and Crush, Crystalline bow, Invisibility, Armor, Spells, Sanity Loss) | с. 22–23 | `creature/sciapod`; `item/crystal-bow`; иллюстрация с луком (с. 22) — картинка `item/crystal-bow` |
| Pre-Generated Character Sheets: Ashley May Bethell | с. 24–27 | `character/ashley-may-bethell` |
| Charles “Mac” McQuinlan | с. 28–31 | `character/charles-mcquinlan` |
| Daniel von Hollisander | с. 32–35 | `character/daniel-von-hollisander` |
| Dennis McCrane | с. 36–39 | `character/dennis-mccrane` |
| Elisabeth “Liz” Hill | с. 40–43 | `character/elisabeth-hill` |
| Mathew “Dodge” Grantham | с. 44–47 | `character/mathew-grantham` |
| Реклама «Call of Cthulhu» | с. 48 | `atmosphere.json` |

## Опечатки и противоречия книги

| Где | Напечатано | Ожидалось | В записи |
|---|---|---|---|
| «Groenland Tropisch, Reefer Ship», с. 9 | Length: 331 feet (117 meters) | 117 м ≈ 384 фута | 117 м (как в паспорте на плане), `errata` у `location/groenland-tropisch` |
| «Superstructure: Level Four», с. 15 | «level three contains the captain’s cabin…» | level four | исправлено, `errata` (fixed) + `corrections` у `location/gt-level-4` |
| «Main Deck», с. 12 | шлюпка на наружной палубе третьего уровня | четвёртый уровень (с. 15 и план с. 11) | `errata` у `location/gt-lifeboat` |
| «Searching the Iceberg», с. 21 | hyperthermia | hypothermia (переохлаждение) | исправлено, `errata` (fixed) у `scene/searching-the-iceberg` |
| «The Sciapod», с. 23 | Clutch & Crush: damage 5D6 (строка атаки) | 4D6 (описание манёвра) | как напечатано, `errata` у `creature/sciapod` — **вопрос владельцу** |
| «Captain’s Mate», с. 22 | DB: 0, но урон «1D3 + 1D4», нож «1D4 + 1D4» | +БкУ 0 | как напечатано, `errata` у `character/kevin-riordan` |
| «Superstructure: Level Three», с. 14 | «(see The Sciapod, page 21)» | page 22 | `errata` у `location/gt-level-3` |
| Лист Чарльза, с. 28 | ПМ 15, на шкале обведено 09 | 15 | `errata` у `character/charles-mcquinlan` |
| Лист Дэниела, с. 32 | Language (Own) — пусто | 70 (= ОБР) | исправлено по Р-41, `errata` (fixed) + `corrections` |
| Лист Лиз, с. 40–41 | у ножа нет процентов; Выживание пусто; снаряжение и деньги пусты | — | нож — 25% (Ближний бой (драка), вывод Р-41), остальное — в `quality.notes` |
| Лист Денниса, с. 36 | крикетная бита без чисел | — | 65%, 1d8+БкУ по таблице (вывод Р-41) |
| Предыстория Денниса, с. 39 | в «Relations» о Маке — текст Дэнни («that Danny respects»); отец Дэнни погиб «из-за мафии» | у Дэнни — автокатастрофа | как напечатано, в `quality.notes` |

Молча (Р-39): «Compliment» (complement), «Entrepenuer», «Accomodations», «Galway Irland», «karmna», «Ashely May», «remains’»,
«more series injuries», «vocal chords», «Using the Rad io».

Прочие наблюдения (не опечатки): судовой журнал капитана книга кладёт и в кабинет (с. 13), и в дневную каюту (с. 15) — оба
места в `found_at`; «up to thirteen» тел в трюме + радист + офицер в шлюпке + моряк в прачечной + двое на айсберге могут
превысить экипаж в 16 человек; сейф в каюте капитана из цели Мака в тексте сценария не описан; наград Рассудка книга не
даёт; «Gross Tonnage 6,600» (текст) и «Displacement 6,600 tonnes» (план) переданы как напечатаны.

## Термины книги (English → русский)

| English | Русский |
|---|---|
| The Derelict | Брошенное судно |
| sciapod (uniped, one-footer, einfætingr) | скиапод (однонога) |
| great footed and hungering thing | великоногая алчущая тварь |
| reefer, refrigerated cargo ship / liner | рефрижератор, рефрижераторное грузовое судно / лайнер |
| Groenland Tropisch (MV Grøenland Tropisch) | «Гренланд Тропиш» |
| Delilah | «Делайла» |
| Simmons and Calvert (Shipping) | «Симмонс и Калверт» |
| Harland and Wolff, Belfast | «Харланд энд Вулф», Белфаст |
| salvage; salvage reward / fee; salvor | спасание (судна); вознаграждение за спасание; спасатель |
| Law of Salvage; Law of Finds | право морского спасания; закон о находке |
| Geneva Convention on the High Seas | Женевская конвенция об открытом море |
| ghost ship | корабль-призрак |
| superstructure | надстройка |
| wheelhouse; navigation bridge; radio room | рулевая рубка; ходовой мостик; радиорубка |
| main deck; the deck level | главная палуба; палубный уровень |
| sun deck, fly (open top) bridge | солнечная палуба (флайбридж) |
| berth deck, lower deck | нижняя палуба |
| cargo hold (Hold 1 Lvl 1) | (грузовой) трюм (трюм 1, уровень 1) |
| cargo level one / two | первый / второй грузовой уровень |
| engine room; motor room & engineering controls | машинное отделение; моторное отделение и пульт управления механизмами |
| motor casing | шахта машинного отделения |
| emergency capsize escape tunnel | аварийный туннель на случай опрокидывания |
| galley, galley kitchen, kitchen | камбуз |
| officers’ / crew’s dining room | столовая офицеров / экипажа |
| crew lounge; officers’ lounge | кают-компания экипажа; кают-компания офицеров |
| crew / officer staterooms, cabins; contractors | каюты экипажа / офицеров; каюты подрядчиков |
| dayroom | дневная каюта |
| medical room, hospital | лазарет |
| recreation room, hobby room | комната отдыха |
| off duty mess | комната отдыха вахты |
| hold climate ops | пост климат-контроля трюмов |
| ship’s store; crew cargo; changing room; wet room | судовая кладовая; склад экипажа; раздевалка; мойка |
| CO2 (bottle) room; CO2 bottles | помещение баллонов CO2; баллоны с CO2 |
| cargo office; cargo manifest | грузовая контора; грузовой манифест |
| captain’s logbook | судовой журнал |
| deck awning | навес над палубой |
| pilot’s rooms | каюты лоцмана |
| comms array; funnel; gangway; winches; ballast; iceberg breach | антенны связи; дымовая труба; сходня; лебёдки; балласт; пробоина от айсберга |
| lifeboat; dinghy | спасательная шлюпка; шлюпка (динги) |
| chief engineer; radio operator / officer; bosun; cook | старший механик; радист; боцман; кок |
| crystal(line) bow; harpoon-like arrow, crystal harpoon | кристаллический лук; стрела-гарпун, кристаллический гарпун |
| Clutch and Crush (mnvr) | Захват и сдавливание (манёвр) |
| Possible discoveries | Возможные находки |
| A grisly discovery | Жуткая находка |
| Erik the Red’s Saga; Thorfinn Karlsefni; Gudrid; Thorvald; Hóp; Straumfjord | «Сага об Эйрике Рыжем»; Торфинн Карлсефни; Гудрид; Торвальд; Хоп; Страумфьорд |
| hyperthermia (sic) / hypothermia | переохлаждение |
| “The Derelict” Agenda; Relations | цель в плавании; отношения |
| Sukkertoppen (Maniitsoq); Bergen | Суккертоппен (Маниитсок); Берген |
| Helmar Engström; Gunnar Ulfsson; Thorolf Löfgren | Хельмар Энгстрём; Гуннар Ульфссон; Торольф Лёфгрен |
| Ashley May Bethell; Charles “Mac” McQuinlan; Daniel von Hollisander; Dennis McCrane; Elisabeth “Liz” Hill; Mathew “Dodge” Grantham | Эшли Мэй Бетелл; Чарльз «Мак» Маккуинлан; Дэниел фон Холлисандер; Деннис Маккрейн; Элизабет «Лиз» Хилл; Мэтью «Додж» Грэнтем |
| Yacht Captain; Captain’s Mate (придуманные имена) | капитан яхты (Гленн Хардинг); помощник капитана (Кевин Риордан) |
| Know roll; Hard / Extreme / Regular | проверка Знаний; трудная / чрезвычайная / обычная проверка |
| Pilot (Boat); Science (Engineering); Survival (Sea); Operate Heavy Machinery | Пилотирование (лодка); Наука (инженерия); Выживание (море); Управление тяжёлыми машинами |

## Не взято

- Пустой лист сыщика «at the back of this book» (с. 4) — в этом PDF его нет.
- Блоки листов сыщиков «Quick Reference Rules» и «Fellow Investigators» (общие правила ядра и пустые поля), силуэты на
  обороте листа; базовые значения навыков в скобках на листе — навыки взяты только отличные от базовых (`quality.notes`).
- Изображения страниц листов сыщиков (оборот, предыстория, цель) — данные перенесены в записи прегенов, портреты — картинками;
  страницы перечислены в `atmosphere.json`.
- Цветовые условные обозначения плана надстройки (с. 11) и шкала «Metres 0–10» (с. 10) — не метки мест; кратко — в описании
  судна.
- Логотипы Free RPG Day, Call of Cthulhu, Chaosium; реклама на с. 48 — `atmosphere.json`.

## Предложения

`proposals-derelict.json` — 1: `coc:weapon:flare-gun` → `source_variants` (урон заряженной ракетницы «1d10+3+burn», с. 14, Р-124).
Картинки — `art.json` → `art-proposals.json` (11, применены). Атмосфера — `atmosphere.json` (21 строка, сливает ведущий).

## Проверки

`python tools/check.py kb/books/the-derelict-en` — 0 ошибок, 0 предупреждений. `tools/completeness.py` — `text.gap` 0,
`art.record_without` 0, `art.uncovered` 21 (все — в `atmosphere.json`). `tools/scenario_check.py` — 0 находок.
