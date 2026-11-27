# HOTOE, часть express — книга I, с. 10, 15–40, 59–72 (2026-11-27)

Источник — `hotoe-book-1-en` (печатная страница = физическая − 2), отдельные карты `hotoe-route-map-en`, `hotoe-air-routes-en`,
`hotoe-train-car-plans-en` (5 листов) и копии для игроков в `hotoe-book-6-handouts-en` (с. 5, 7). Русский текст — наш перевод
(флаг `translated`, Р-251). Решения: Р-254 (поезд — место типа «корабль», вагоны — `part_of` него), Р-189, Р-206, Р-64, Р-124.

## Записи (28)

| Вид | Записи |
|---|---|
| location (8) | `express-simplon-orient-express` (корабль, `part_of: null`); вагоны `express-engine-and-tender`, `express-fourgon`, `express-sleeping-car`, `express-dining-car`, `express-salon-car`, `express-cathedral-car`; `express-engine-cab` (`part_of` паровоза) |
| map (9) | `express-route-map`, `express-air-routes-1923`, `express-plan-locomotive-fourgon`, `express-plan-salon-sleeping`, `express-plan-sleeping-cars`, `express-plan-fourgons`, `express-plan-dining-cathedral`, `express-engine-diagram`, `express-engine-cab-diagram` |
| rule (11) | `express-society-on-the-simplon-orient-express`, `express-orient-express-books-and-films`, `express-simplon-orient-express-operations`, `express-other-orient-expresses`, `express-traveling-armed`, `express-air-travel-in-europe-in-the-early-1920s`, `express-practicalities-for-the-european-air-traveler-in-1923` (parent — предыдущая), `express-a-continent-of-horrors`, `express-european-scenarios-outside-the-1920s` (parent — предыдущая), `express-celluloid-train-terrors`, `express-news-aboard-the-orient-express` |

Все — в `kb/books/hotoe-book-1-en/<вид>s/`. Картинки карт — `app/maps/hotoe-express-*.jpg` (9); картинки записей —
`app/art/locations/hotoe-express-{simplon-orient-express,sleeping-car,dining-car,engine-cab}.webp` (сопоставление
`art-express.json`, предложения применены).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Routes of the Orient Express (карта) | 10; Book VI с. 7; `hotoe-route-map-en` | карта `express-route-map` (41 метка) |
| (окончание очерка истории: Вторая мировая, холодная война, 1970–1980-е) | 15 | поезд, `history` (1-й–3-й абзацы); начало очерка (с. 11–14) — часть campaign |
| Society on the Simplon-Orient Express | 15–17 | правило `express-society-on-the-simplon-orient-express` |
| Non-Fiction Books (врезка) | 16 | правило `express-orient-express-books-and-films` |
| Film References (врезка) | 17 | правило `express-orient-express-books-and-films` |
| In The 1890s | 17–18 | поезд, `history` |
| Chaosium Fiction (врезка) | 18 | правило `express-orient-express-books-and-films` |
| The Orient Express Today | 18 | поезд, `history` |
| Resources for the Keeper: Simplon-Orient Express Operations | 19 | правило `express-simplon-orient-express-operations`; поезд, `description` |
| Staff; Brigadier-Postier; Cleaner; Chef de Brigade; Chef de Cuisine; Chef de Train; Conductor (Conducteur) | 20 | правило `express-simplon-orient-express-operations`, таблица «Персонал поезда» |
| Controller (Controleur); Head Waiter (Serveur-Receveur); Maitre d’Hotel; Waiter (Serveur); Consideration | 21–22 | то же правило |
| Other Orient Expresses (текст и таблица) | 22 | правило `express-other-orient-expresses` |
| Components of a Train | 22 | поезд, `description` («Из чего состоит поезд») |
| Security | 23 | поезд, `description` («Безопасность») |
| Sleeping Car | 23–24 | место `express-sleeping-car` |
| Dining Car | 24 | место `express-dining-car` |
| Orient Express Configuration (врезка) | 24 | поезд, таблица «Состав поезда» |
| Fourgon (Baggage Car) | 24–25 | место `express-fourgon` |
| Salon Car | 25 | место `express-salon-car` |
| Engine Cab | 25 | место `express-engine-cab` |
| Communications | 25, 28 | поезд, `description` («Переходы и связь») |
| Планы вагонов: Locomotive & Tender, Fourgon (Baggage Car), Sleeping Car, Salon Car, Dining Car, Cathedral Car | 26–27, 71–72; `hotoe-train-car-plans-en` 1–5 | карты `express-plan-*` (5), места вагонов; `express-cathedral-car` |
| Ticket Prices for the Orient Express (врезка) | 28 | поезд, таблица «Стоимость билетов» |
| Arrangement of the Cars | 28 | поезд, `description` («Расстановка вагонов») |
| Emergency Equipment | 28 | поезд, `description` («Аварийное снаряжение») |
| Stops Along the Way | 29, 32 | поезд, таблица «Остановки в пути» (27 строк); метки карты маршрутов |
| (старая карта: основной путь SOE с 1920 года) | 29 | картинка записи поезда |
| Train diagram: паровоз | 30 | карта `express-engine-diagram` (23 метки), место `express-engine-and-tender` |
| The Engine and Cab (врезка) и рисунок кабины | 31 | место `express-engine-and-tender`; карта `express-engine-cab-diagram` (10 меток), место `express-engine-cab` |
| Traveling Armed | 33–34 | правило `express-traveling-armed` |
| Legal Matters | 34 | то же правило |
| Further Reading | 34 | то же правило |
| Police Officers and Customs Agents (врезка) | 35 | то же правило, таблица «Оружие полиции и таможни (1923)» |
| Air Travel in Europe in the Early 1920s | 36–38 | правило `express-air-travel-in-europe-in-the-early-1920s` |
| Air Routes of Europe in 1923 (карта) | 38, 70; Book VI с. 5; `hotoe-air-routes-en` | карта `express-air-routes-1923`; расстояния — таблица правила `express-practicalities-…` |
| Practicalities For The European Air Traveler In 1923; Airline Travel | 38–39 | правило `express-practicalities-for-the-european-air-traveler-in-1923` |
| Common Commercial Passenger Aircraft (врезка) | 39 | то же правило, таблица самолётов |
| Air Taxis; Aerodromes; Practicalities For The Keeper; Selected Sources | 39–40 | то же правило |
| A Continent of Horrors; A Continent of Call of Cthulhu | 59 | правило `express-a-continent-of-horrors` |
| Albania … Yugoslavia (30 стран) | 59–64 | то же правило, таблица «Европа по странам» |
| European Call of Cthulhu Scenarios outside the 1920s | 64–65 | правило `express-european-scenarios-outside-the-1920s` |
| Celluloid Train Terrors | 66–67 | правило `express-celluloid-train-terrors` (таблица 12 фильмов) |
| News Aboard The Orient Express | 68 | правило `express-news-aboard-the-orient-express` |
| (заголовки газет, январь — май 1923) | 69 | то же правило, таблица «Заголовки 1923 года» (34 строки: как напечатано + перевод) |
| Complete Maps | 70–72 | источники карт `express-air-routes-1923` и `express-plan-*` |
| Book VI: Book 1 Handouts/Maps | Book VI с. 5 (низ), 7 | источники карт `express-air-routes-1923`, `express-route-map` |

## Не взято

- Иллюстрации без записи (фото, рисунки, фоны врезок) — `atmosphere-express.json` (27 страниц) для `pipeline/art/atmosphere.json`;
  среди них подпись «In the Balkans, a blizzard stalls the train… below 50 degrees» (с. 29) — подпись к рисунку, правила нет.
- Колонтитулы «campaign book», «Book 1», «Horror on the Orient Express» — оформление.
- Карта маршрутов: подписи городов без записей (Амстердам, Мадрид, Варшава…), моря, страны, станции чужих линий — метки не ставились
  (перечислено в `quality.notes` карты); Валлорб, Фрасн, Изелле и Пирот на карте не подписаны.
- Карта авиалиний: подписи городов без записей — без меток (перечислены в `quality.notes`); числа расстояний — таблицей правила.
- Book VI с. 5, верх (карта «BOOK IV, PAGE 116», лавка Макрията) — часть return; с. 6, 8 — пустые обороты.
- Начало очерка истории Восточного экспресса (с. 11–14) — часть campaign (может дополнить `history` поезда предложением).
- Отдельные записи для каждого из 12 вагонов состава не заводились: одна запись на вид вагона, состав — таблица поезда.
- Полные адреса сайтов в «Selected Sources» и «Further Reading» — оставлены только названия.

## Опечатки и сомнения

- с. 24 «Train car plans are found on pages 30 and 31» и с. 23 «In the illustrations on pages 30-31» — планы вагонов на с. 26–27
  (и 71–72), на с. 30–31 схемы паровоза: `errata` поезда и спального вагона.
- с. 40 «The route map on page 42» — карта авиалиний на с. 38 и 70: `errata` правила `express-practicalities-…`.
- с. 69 «POPE PAUL XI» — в 1923 году папой был Пий XI: `errata` правила новостей (оставлено как напечатано).
- с. 33 Mauser C96: «Damage 1D8+1, Shots 10» против справочника (1d10+1) — предложение `source_variants` (Р-124).
- с. 32 «TZARIBROD (Dimitrevgrad)»; на карте отдельно «Tsaribrod» и болгарский «Dmitrovgrad».
- с. 22 «Salzberg», «Nuremburg»; с. 66 «Walter Ford» (режиссёр Walter Forde); планы «W.C. (Midieval Style)», схема кабины «Guage» —
  как напечатано, пометки в записях.
- Сомнения без правки (книга — источник): Адрианополь и Черкесекей названы греческой таможней (Восточная Фракия вернулась к
  Турции осенью 1922 года); заголовок 1 мая 1923 года «Putsch In Munich? … Hitler Jailed» неисторичен для мая 1923 года.
- Карта авиалиний: линия «228» от Парижа кончается у Роттердама или Амстердама — неоднозначно (пометка в таблице).
- «Secrets of the Kremlin» T.O.M.E. (с. 63) и запись `secrets-of-the-kremlin-en` («Secrets of the Kremlin, 1931») — связь не проверена,
  ссылки нет.

## Ссылки на записи других частей (пока не существуют)

`coc:location:lausanne`, `coc:location:trieste`, `coc:location:vinkovci`, `coc:location:belgrade`, `coc:location:sofia` (метки
карт, строки таблицы остановок, refs); `hotoe-book-2-en/scenario/the-blood-red-fez`, `hotoe-book-4-en/scenario/blue-train-black-night`,
`hotoe-book-4-en/scenario/the-simulacrum-unbound` (refs поезда и вагона-собора). `coc:location:venice` и кампания уже есть.

## Предложения и черновики

- `proposals-express.json` — 1: `coc:weapon:mauser-c96-broomhandle` + `source_variants` (Р-124); пробный прогон — ложится.
- `new-shared-locations-express.json` — черновики общих городов `coc:location:calais` и `coc:location:adrianople` (их нет в
  `kb/locations`); после создания перевести на них метки «Calais», «Edirne», «Edirne (Adrianople)» карты маршрутов и добавить refs в
  строки таблицы остановок.
- Для других частей: return — вагон-собор и поезд обратного пути (ссылка на `express-cathedral-car`, `express-*` вагоны);
  strangers-2 — служащие Wagons-Lits (проводники, начальник поезда) могут ссылаться на поезд и правило персонала; campaign —
  очерк с. 11–14 в `history` поезда.

## Термины (английский → русский)

| English | Русский |
|---|---|
| Simplon-Orient Express | Симплон-Ориент-экспресс |
| Orient Express | Восточный экспресс |
| Venice Simplon-Orient-Express | «Венеция — Симплон — Восточный экспресс» |
| Simplon Express | «Симплон-экспресс» |
| Compagnie Internationale des Wagons-Lits (CIWL), Wagons-Lits | Международная компания спальных вагонов (CIWL), Wagons-Lits |
| Fourgon (Baggage Car) | фургон (багажный вагон) |
| Sleeping Car | спальный вагон |
| Dining Car | вагон-ресторан |
| Salon Car | салон-вагон |
| Cathedral Car | вагон-собор |
| Locomotive & Tender | паровоз и тендер |
| Engine Cab, Driving Cab | кабина машиниста |
| Brigadier-Postier | бригадир-почтовик |
| Cleaner | уборщик |
| Chef de Brigade | начальник бригады |
| Chef de Cuisine | шеф-повар |
| Chef de Train | начальник поезда |
| Conductor (Conducteur) | проводник |
| Controller (Contrôleur) | контролёр |
| Head Waiter (Serveur-Receveur) | старший официант |
| Maître d’Hôtel | метрдотель |
| Waiter (Serveur) | официант |
| Guard (на плане фургона) | купе кондуктора |
| Regulator Handle | рукоятка регулятора |
| Steam Pressure Gauge | манометр давления пара |
| emergency cord | стоп-кран |
| customs check-point | таможенный пункт |
| Interallied Police | межсоюзническая полиция |
| The Traveler’s Companion | «Спутник путешественника» |
| Stops Along the Way | остановки в пути |
| Traveling Armed | «В путь с оружием» |
| air taxi | воздушное такси |
| Customs Aerodromes | таможенные аэродромы |
| Croydon, Le Bourget | Кройдон, Ле-Бурже |
| Goliath | «Голиаф» |
| Compagnie Franco-Roumaine de Navigation Aérienne | Франко-Румынская компания |
| Little Entente | «Малая Антанта» |
| A Continent of Horrors | «Континент ужасов» |
| vampire belt | «вампирский пояс» |
| Commonplace Book | «Тетрадь для заметок» (Лавкрафта) |
| History of the Necronomicon | «История «Некрономикона»» |
| Celluloid Train Terrors | «Ужасы на киноплёнке: поезда» |
| News Aboard the Orient Express | «Новости в Восточном экспрессе» |
| Calais; Frasne; Vallorbe; Brigue (Brig); Simplon Tunnel; Iselle; Domodossola | Кале; Фрасн; Валлорб; Бриг; Симплонский туннель; Изелле; Домодоссола |
| Postumia; Rakek; Ljubljana; Zagreb (Agram); Nis/Pirot | Постумия; Ракек; Любляна; Загреб (Аграм); Ниш / Пирот |
| Tzaribrod (Tsaribrod); Dragoman; Svilengrad; Adrianople (Edirne); Tcherkesseui (Çerkezköy); Sinakli (Sinekli) | Цариброд; Драгоман; Свиленград; Адрианополь (Эдирне); Черкесекей (Черкезкёй); Синакли (Синекли) |

Названия глав кампании («The Blood Red Fez», «The Simulacrum Unbound», «Blue Train, Black Night») в текстах оставлены
по-английски — русские названия дают части этих глав. Навыки и проверки — по глоссарию: Внимание (Spot Hidden), Средства
(Credit Rating), Красноречие (Fast Talk), проверка Удачи (Luck roll).

## Проверки

- `python -I -B tools/check.py <28 файлов express-*>` — ошибок в своих файлах нет, кроме 21 ссылки на записи других частей (выше).
- `completeness-express/` — по страницам части текстовых пропусков нет; картинки — атмосфера (выше).
- `scenario-express/` — находок по записям части нет (находки — у записи кампании, часть campaign).
