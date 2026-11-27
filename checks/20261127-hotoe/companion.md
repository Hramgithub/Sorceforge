# HOTOE, часть companion — «Спутник путешественника» (Travelers’ Companion), с. 1–52 (2026-11-27)

Источник — `hotoe-travelers-companion-en` (П. Э. Йенсен; печатных номеров нет, печатная = физическая). Русский текст — наш
перевод (флаг `translated`, Р-251, Р-21). Решения: Р-254 (общие города, каждая эпоха — свой абзац), Р-190, Р-209, Р-154, Р-64.
Путеводитель — реквизит для игроков: описания городов, отели, достопримечательности уходят предложениями в общие города и
готовые места глав; советы, таможня, валюта и путь — правила по странам; места, которых в базе не было, — записи `companion-*`.

## Записи (20) — `kb/books/hotoe-travelers-companion-en/`

| Вид | Записи |
|---|---|
| rule (8) | `companion-welcome-aboard-the-orient-express` (верхний раздел: предисловие, приветствие, вагон-ресторан, общие советы, персонал, газеты; таблицы «Меню вагона-ресторана», «Наш персонал», «Валюта по пути», «Пограничные проверки по пути»); по странам (`parent` — первая): `companion-great-britain`, `companion-france`, `companion-switzerland`, `companion-italy`, `companion-kingdom-of-serbs-croats-and-slovenes`, `companion-bulgaria`, `companion-thrace-and-turkey` |
| location (12) | Лондон: `companion-london-ritz-hotel`, `companion-london-claridges` (Мэйфэр), `companion-london-carlton-hotel` (Вестминстер), `companion-london-midland-grand-hotel` (Сент-Панкрас); Лозанна: `companion-lausanne-le-lausannois`, `companion-lausanne-hotel-beau-sejour`, `companion-lausanne-lake-geneva`, `companion-lausanne-montreux` (оба — в `lausanne-environs`); Венеция: `companion-venice-hotel-cipriani`, `companion-venice-caffe-florian` (район Сан-Марко); Триест: `companion-trieste-corso`, `companion-trieste-commercial-and-nautical-academy` |

Картинки: `app/art/locations/hotoe-companion-*.webp` (10), сопоставление `art-companion.json`, предложения
`art-companion-proposals.json` (не применены — применяет ведущий). Атмосфера — `atmosphere-companion.json` (5 страниц).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Le Guide du Voyageur. The Traveler’s Companion» (фото холла «Пера Паласа») | 1 | правило `companion-welcome-…` (текст); фото — картинка `wwc-cold-war-en/location/pera-palas-hotel`; остальное — атмосфера |
| The Travelers’ Companion; Welcome Aboard the Orient Express (титул) | 3 | правило `companion-welcome-…` |
| Выходные данные | 4 | не взято (см. ниже) |
| Preface; приветствие Wagons-Lits, вагон-ресторан | 5 | правило `companion-welcome-…` |
| Menu (Entrees, Dessert, Wine list) | 6 | правило `companion-welcome-…`, таблица «Меню вагона-ресторана» (18 строк) |
| Advice to Travelers (общие); Our Staff; Chef de Brigade; Chef de Cuisine; Chef de Train; Newspapers | 7 | правило `companion-welcome-…`, текст и таблица «Наш персонал» |
| Conductor (Conducteur); Head Waiter (Serveur-Receveur); Maitre D’Hôtel; Waiter (Serveur) | 8 | то же, таблица «Наш персонал» |
| London: Location; Description | 8 | предложение `coc:location:london` (абзац 1923 года) |
| London: Advice to Travelers (и таможня) | 8–9 | правило `companion-great-britain` |
| Карта Лондона (для игроков) | 9 | источник карты `hotoe-book-2-en/map/london-city-1923-players` (предложение) |
| Hotels (Ritz, Claridges, Carlton, Midland Grand) | 9–10 | записи `companion-london-*`; абзац города |
| Currency (Британия) | 10 | правило `companion-great-britain`; таблица «Валюта по пути» |
| Places of Interest: The British Museum and Library – the Reading Room | 10 | предложение `hotoe-book-2-en/location/london-british-museum-reading-room` |
| The Victoria and Albert Museum | 10 | предложение `hotoe-book-2-en/location/london-victoria-and-albert-museum` |
| St Paul’s Cathedral (и фото) | 10–11 | предложение `coc:location:st-pauls-cathedral`; картинка |
| The Tower of London | 10–11 | предложение `coc:location:tower-of-london` |
| London to Calais | 11 | правило `companion-great-britain`; предложение `masks-…/england-st-pancras-station`; дополнение черновика `coc:location:dover` |
| Calais: Location; Description; Places of Interest; Calais to Paris | 12 | правило `companion-france`; дополнение черновика `coc:location:calais` |
| Paris: Location; Description | 12 | предложение `coc:location:paris` |
| Paris: Advice to Travelers (вокзал, этикет, транспорт) | 13, 15 | правило `companion-france` |
| Карта Парижа (для игроков) | 13 | источник карты `hotoe-book-2-en/map/paris-city-1923-players` |
| Eiffel Tower (фото) | 14 | картинка `hotoe-book-2-en/location/paris-eiffel-tower` |
| Hotels (Bristol, du Rhin, Balmoral) | 15 | предложения `paris-bristol-hotel`, `paris-hotel-du-rhin`, `paris-balmoral-hotel` (текст + адрес); абзац города |
| Currency (франк) | 15 | правило `companion-france` |
| The Eiffel Tower (Tour Eiffel…) | 15 | предложение `hotoe-book-2-en/location/paris-eiffel-tower` |
| The Bibliothèque Nationale | 16 | предложение `tsarstvo-terrora-ru/location/paris-royal-library` |
| The Louvre (Musée du Louvre) | 16 | предложение `hotoe-book-2-en/location/paris-louvre` |
| Cathedrale de Notre-Dame | 16 | предложение `tsarstvo-terrora-ru/location/paris-notre-dame` (+ эпоха 1920s) |
| Les Catacombes (Place Denfert-Rochereau) | 16–17 | предложение `tsarstvo-terrora-ru/location/paris-catacombs` |
| From Paris to Lausanne; Frasne; Vallorbe | 17 | правила `companion-france`, `companion-switzerland`; таблица проверок |
| Lausanne: Location; Description | 17–18 | предложение `coc:location:lausanne` |
| Карта Лозанны (для игроков) | 18 | источник карты `hotoe-book-2-en/map/lausanne-city-players` |
| Lausanne: Advice to Travelers (Lausannois, Hôtel Central, Le Chat Noir, транспорт) | 19 | запись `companion-lausanne-le-lausannois`; предложения `lausanne-hotel-central`, `lausanne-le-chat-noir`; правило `companion-switzerland` |
| Hotels (Beau-Rivage, Lausanne-Palace-Beau-Site, Cecil, Beau-Séjour) | 19 | предложения трёх отелей (текст + адрес); запись `companion-lausanne-hotel-beau-sejour` |
| Currency (франки) | 19 | правило `companion-switzerland` |
| Cantonal Museum and Library (Musée de Beaux-Arts) | 19 | предложение `hotoe-book-2-en/location/lausanne-cantonal-museum` |
| Lausanne Cathedral (Notre-Dame) (и фото) | 19–20 | предложение `hotoe-book-2-en/location/lausanne-cathedral`; картинка |
| The Arlaud Museum | 20 | предложение `hotoe-book-2-en/location/lausanne-musee-arlaud` |
| Palais de Rumine (Place de la Riponne) | 20 | предложение `hotoe-book-2-en/location/lausanne-palais-de-rumine` |
| Lake Geneva | 20–21 | запись `companion-lausanne-lake-geneva` |
| Montreux: Location; Description; Advice to Travelers; Currency | 21 | запись `companion-lausanne-montreux`; валюта — правило `companion-switzerland` |
| Place of Interest – Chateau de Chillon | 21 | предложение `hotoe-book-2-en/location/lausanne-chateau-de-chillon` |
| From Lausanne to Brigue; Brigue (Description, Advice to Travelers) | 21–22 | правило `companion-switzerland` |
| The Simplon Tunnel | 22 | правило `companion-switzerland` |
| Italy: Advice to Travelers; Passports and visas; Customs levies; Currency | 22–23 | правило `companion-italy` |
| Iselle; Domodossola (Description); From Domodossola to Milan | 23 | правило `companion-italy` |
| Milan (прибытие на Stazione Centrale) | 23 | предложение `hotoe-book-2-en/location/milan-stazione-centrale`; правило `companion-italy` |
| Milan: Location; Description | 24 | предложение `coc:location:milan` |
| Milan: Advice to Travelers (Cova, Biffi) | 24 | предложения `milan-caffe-cova`, `milan-caffe-biffi` |
| Hotels (de la Ville, Cavour, Marino et National) | 24 | предложения трёх отелей (текст + адрес) |
| Places of Interest: La Galleria Vittorio Emanuele | 24–25 | предложение `hotoe-book-2-en/location/milan-galleria-vittorio-emanuele` |
| Карта Милана (для игроков) | 25 | источник карты `hotoe-book-2-en/map/milan-city-players` |
| Il Duomo (и фото) | 26 | предложение `hotoe-book-2-en/location/milan-duomo`; картинка |
| The Piazza del Duomo | 26 | предложение `hotoe-book-2-en/location/milan-piazza-del-duomo` |
| The Piazza della Scala | 26 | предложение `hotoe-book-2-en/location/milan-piazza-della-scala` |
| Teatro alla Scala | 27 | предложение `hotoe-book-2-en/location/milan-teatro-alla-scala` |
| Convent of Santa Maria delle Grazie | 27 | предложение `hotoe-book-2-en/location/milan-santa-maria-delle-grazie` |
| From Milan to Venice | 27 | правило `companion-italy` |
| Venice: Location; Description (и история) | 27–28 | предложение `coc:location:venice` (+ замена пометки «дополнит позже» в `quality.notes`) |
| Venice: Advice to Travelers (лодки, гондолы) | 28 | правило `companion-italy` |
| Hotels (Gritti Palace, Daniel, Cipriani; pensione; Pilsen, Bauer-Grünwald) | 28 | предложения `venice-gritti-palace-hotel`, `venice-hotel-royal-danieli`, `venice-restaurant-pilsen`, `venice-restaurant-baur-grunwald`; запись `companion-venice-hotel-cipriani` |
| Places of Interest: The Grand Canal | 28 | предложение `hotoe-book-3-en/location/venice-grand-canal` |
| Piazza San Marco (кафе, музыка; фото) | 28–30 | предложение `hotoe-book-3-en/location/venice-piazza-san-marco`; запись `companion-venice-caffe-florian`; картинка |
| Карта Венеции (для игроков) | 29 | источник карты `hotoe-book-3-en/map/venice-venice-1923-players` |
| St Mark’s Basilica (Basilica di San Marco) | 30 | предложение `hotoe-book-3-en/location/venice-san-marco-basilica` |
| The Biblioteca Marciana | 30 | предложение `hotoe-book-3-en/location/venice-biblioteca-marciana` |
| The Doge’s Palace | 31 | предложение `hotoe-book-3-en/location/venice-doges-palace` |
| Venice to Trieste | 31 | правило `companion-italy` |
| Trieste: Location; Description | 31 | предложение `coc:location:trieste` |
| Trieste: Advice to Travelers (вокзал, кухня, вина, купания, бора) | 31–32 | правило `companion-italy`; предложение `trieste-station` |
| Hotels (Savoia Excelsior, de la Ville, Metropole, Moncenisio, Central) | 32 | предложения трёх отелей (текст + адрес); «Метрополь» и «Монченизио» — только в абзаце города (книга даёт лишь имена) |
| Places of Interest: The Corso | 32 | запись `companion-trieste-corso` |
| The Piazza Unità d’Italia | 32 | предложение `hotoe-book-3-en/location/trieste-piazza-unita-ditalia` |
| The Giardino Lapidario | 32 | предложение `hotoe-book-3-en/location/trieste-giardino-lapidario` |
| Карта Триеста (для игроков) | 33 | источник карты `hotoe-book-3-en/map/trieste-city-players` |
| Cattedrale San Giusto (и фото) | 33–34 | предложение `hotoe-book-3-en/location/trieste-cattedrale-san-giusto`; картинка |
| The Castello | 34 | предложение `hotoe-book-3-en/location/trieste-castello-di-san-giusto` |
| The Commercial and Nautical Academy (the Piazza Lipsia) | 34 | запись `companion-trieste-commercial-and-nautical-academy`; предложение `trieste-city-library` |
| Grotta Gigante | 34 | предложение `hotoe-book-3-en/location/trieste-grotta-gigante` |
| Postumia; Place of Interest – Grotte di Postumia | 35 | предложения `trieste-postumia`, `trieste-grotte-di-postumia`; правило `companion-italy` |
| Rakek; From Trieste to Ljubljana; Ljubljana; Ljubljana to Zagreb | 35 | правило `companion-kingdom-of-serbs-croats-and-slovenes` |
| Zagreb (Agram): Location; Description | 36 | правило (проверка); дополнение черновика `coc:location:zagreb` |
| Vinkovci: Description | 36 | предложения `coc:location:vinkovci`, `vinkovci-hotel-lehrner`, `vinkovci-train-station` |
| Zagreb to Belgrade (Beograd) | 36 | правило `companion-kingdom-…` |
| Belgrade: Location; Description; Hotels | 37 | предложения `coc:location:belgrade`, `belgrade-hotel-europa`, `-moskva`, `-petrograd` (текст + адрес) |
| Belgrade: Advice to Travelers; Currency | 37 | правило `companion-kingdom-…`; предложение `belgrade-station` |
| Places of Interest: Kalemegdan Park | 38 | предложение `hotoe-book-3-en/location/belgrade-kalemegdan-park` |
| Карта Белграда (для игроков) | 38 | источник карты `hotoe-book-3-en/map/belgrade-city-players` |
| The Kalemegdan fortress (и фото) | 39 | предложение `hotoe-book-3-en/location/belgrade-kalemegdan-fortress`; картинка |
| The Market Place | 39 | предложение `hotoe-book-3-en/location/belgrade-great-market-place` (+ адрес Кралев трг) |
| The Belgrade Museum | 39 | предложение `hotoe-book-3-en/location/belgrade-national-museum` |
| The New Konak, or Royal Palace (Milan street) | 40 | предложение `hotoe-book-3-en/location/belgrade-new-konak` |
| The Turkish Quarter and Bazaar | 40 | предложения `belgrade-turkish-town`, `belgrade-bazaar` |
| Belgrade to Nïs/Pirot; Nïs/Pirot; Tzaribrod (Dimitervgrad) | 40 | правило `companion-kingdom-…`; Ниш — дополнение черновика `coc:location:nis` |
| Dragoman | 41 | правило `companion-bulgaria` |
| Sofia: Location; Description | 41–42 | предложения `coc:location:sofia`, `sofia-rail-station`, `sofia-house-of-parliament` |
| Карта Софии (для игроков) | 42 | источник карты `hotoe-book-4-en/map/sofia-city-1923-players` |
| Sofia: Advice to Travelers (языки) | 42 | правило `companion-bulgaria` |
| Hotels (de la Bulgarie); Currency (лев) | 43 | предложение `sofia-hotel-de-la-bulgarie`; правило `companion-bulgaria` |
| Places of Interest: Alexander Nevsky cathedral | 43 | предложение `hotoe-book-4-en/location/sofia-alexander-nevsky-cathedral` |
| The Royal Palace (фото, статья) | 43–44 | предложение `hotoe-book-4-en/location/sofia-royal-palace`; картинка |
| The Archeological Museum | 44 | предложение `hotoe-book-4-en/location/sofia-archaeology-museum` |
| The University of Sofia | 44 | предложение `hotoe-book-4-en/location/sofia-university` |
| The Central Mineral Baths | 44 | предложение `hotoe-book-4-en/location/sofia-central-mineral-baths` |
| National Theatre | 44 | предложение `hotoe-book-4-en/location/sofia-national-theatre` |
| Dimitrovgrad; Svilengrad | 44 | правило `companion-bulgaria` |
| Adrianople (Edirne); Tcherkesseui; Sinakli; Sinakli to Constantinople | 45 | правило `companion-thrace-and-turkey`; дополнение черновика `coc:location:adrianople` |
| Constantinople (Istanbul): прибытие; Location | 45 | правило `companion-thrace-and-turkey`; предложения `constantinople-sirkeci-station`, `coc:location:constantinople` |
| Description (Stamboul, Pera-Galata, Iskudar) | 46 | предложения `coc:location:constantinople`, `wwc-cold-war-en/location/fatih`, `beyoglu`, `uskudar` |
| Advice to Travelers (Галатский мост, консульство, бани, чайные, грязь) | 46–47 | правило `companion-thrace-and-turkey`; предложения `wwc-…/galata-bridge`, `constantinople-british-consulate` |
| Карта Константинополя 1923 (для игроков; ключ 1–10) | 47 | источник карты `hotoe-book-4-en/map/constantinople-1923-players` |
| Hotels (Pera Palace) | 47–48 | предложение `wwc-cold-war-en/location/pera-palas-hotel` |
| Currency (турецкий фунт) | 48 | правило `companion-thrace-and-turkey` |
| Places of Interest: The Sultan Ahmet I Cammi (the Blue Mosque) | 48 | предложение `wwc-cold-war-en/location/blue-mosque` |
| The Aya Sofia (и фото) | 48–49 | предложение `wwc-cold-war-en/location/haghia-sophia`; картинка |
| The Hippodrome | 48–49 | предложение `hotoe-book-4-en/location/constantinople-hippodrome` (+ ссылка на колонну Константина 330 года) |
| The Basilica Cistern | 49 | предложение `hotoe-book-4-en/location/constantinople-basilica-cistern` |
| The Grand Bazaar | 49–50 | предложение `wwc-cold-war-en/location/grand-bazaar` |
| The Topkapi Museum | 50 | предложение `hotoe-book-4-en/location/constantinople-topkapi-museum` |

## Не взято

- с. 2, 51 — синие внутренние стороны обложек без текста; с. 52 — задняя обложка с эмблемой; с. 5 — герб Wagons-Lits; обложка
  (кроме фото холла) — атмосфера, `atmosphere-companion.json`.
- с. 4 — выходные данные (copyright, адрес Chaosium, ISBN) — не материал игры.
- Колонтитулы с названиями городов — оформление.
- Отдельные записи станций пути (Фрасн, Валлорб, Бриг, Симплонский туннель, Изелле, Домодоссола, Постумия-граница, Ракек, Любляна,
  Брод, Пирот, Цариброд, Драгоман, Свиленград, Димитровград, Черкесекей, Синакли) не заводились: их текст — в правилах по странам
  и в таблице «Пограничные проверки по пути»; кандидаты в общие города — на усмотрение ведущего.
- Площади и улицы, упомянутые только в советах (площадь Сен-Франсуа, Палю, Гран-Пон в Лозанне; Пьяцца-дель-Меркато в Домодоссоле;
  Bagno Foniania и Военная купальня в Триесте; рыбный рынок Триеста; Театр-плац и улица Милана в Белграде) — текстом в правилах и
  абзацах, без записей.
- Отели «Метрополь» и «Монченизио» (Триест) — только имена, текстом в абзаце города.

## Предложения и черновики

- `proposals-companion.json` — 319 предложений к 110 записям: 101 абзац 1923 года в `description.ru` (replace в конце текста),
  142 источника, 44 ссылки, 22 адреса (`set address`, где адреса не было), 9 эпох `1920s`, 1 замена пометки в `quality.notes`
  Венеции; 9 источников карт игроков (та же карта напечатана в путеводителе, сверено по изображениям страниц).
- **Порядок применения:** после предложений глав (`proposals-london/paris/lausanne-milan/venice/…/constantinople.json`): у
  Лондона, Парижа, Милана, Константинополя, районов Стамбула и некоторых мест якорь `old` — конец абзаца, который добавляют главы.
  Пробный прогон в памяти (все предложения глав, затем companion) — 0 несостыковок, записи проходят схемы
  (`.cache/lead-tools/gen-hotoe-companion/dryrun.py`). Общий `apply.py … --dry-run` по всем файлам сейчас останавливается на чужом
  `proposals-lausanne-milan.json #33` (`caterina-cavollaro`, кусок «(глава «Нота за нотой»).» не найден) — не наша часть.
- `new-shared-locations-companion.json` — новых городов нет; дополнения по путеводителю к черновикам других частей: Кале, Адрианополь
  (express), Дувр (london), Загреб (zagreb-vinkovci), Ниш (fez) — абзац в конец `description.ru`, источники, ссылки на правила.
- `art-companion.json` → `art-companion-proposals.json` (10 картинок, не применены): фото холла «Пера Паласа», собор Святого Павла,
  Эйфелева башня, Лозаннский собор, Дуомо, площадь Сан-Марко, собор Сан-Джусто, крепость Калемегдан, Королевский дворец в Софии,
  Айя-София.

## Опечатки, расхождения и сомнения

- с. 17: Восточный экспресс отходит «from the Gare de L’Est»; книга II (с. 125, 128) — Лионский вокзал: `errata` правила `companion-france`.
- с. 11: «поезд к пароходу» — со Сент-Панкраса (как напечатано).
- с. 15: «12 Rue du Faubourg Saint-Honor» — без «é» (адрес в предложении — Сент-Оноре).
- с. 26: на Пьяцца делла Скала — памятник Леонардо да Винчи; у записи главы (кн. II, с. 221) — «статуя Микеланджело». Обе версии остаются.
- с. 19–20: Лозаннский собор — «XI век», «164 ступени», вход 1 франк, «Otto III of Castle Grandson»; книга II — 1235–1275, 160
  ступеней, 35 сантимов, Оттон де Грансон. Библиотека в 120 000 томов — у Кантонального музея (книга II — во дворце Рюмин). Абзацы
  помечены как сведения «Спутника».
- с. 20: «Calane, Diday» — художники Калам и Диде (в тексте — пометка «в книге»).
- с. 28: «the Daniel» = «Даниели»; «Bauer-Grünwald» (на карте — «Baur-Grunwald»).
- с. 31: Триест «in northwestern Italy» (на деле — северо-восток), как напечатано с пометкой.
- с. 32: «Bagno Foniania», «Polo San Tersa» — как напечатано.
- с. 34: «Kart region» (Карст), «Aqulia» (Аквилея); Гротта-Гиганте «nine miles» (14,4 км) против «около 5 км» у записи главы.
- с. 36: «Panonnian».
- с. 37: «Sremsk 1» (Сремска, 1). Белград: турецкое владычество «кончилось в 1866 году», а крепость занята турками «до 1867 года» (с. 39).
- с. 39: «Usun-Mirkova»; с. 40: «Theatre-Plazt».
- с. 40: «Tzaribrod (Dimitervgrad)»; с. 44 — болгарский Димитровград описан как существующий город (сомнение: возможный анахронизм).
- с. 43: «Tsar Alexander Nevsky»; с. 44: «Kliment Ohdirski» (Охридски).
- с. 45: «Sea of Marmosa» (Мраморное море); Адрианополь и Черкесекей — «Greek customs» (сомнение отмечено и частью express).
- с. 46: Ататюрк «banned veils and fezzes» в 1922 году — как напечатано (сомнение: запрет фесок — 1925).
- с. 49: Цистерна Базилика «now mostly empty» — у главы (кн. IV) она затоплена; как напечатано, пометка «так в путеводителе».
- с. 7: газета Die Welt в 1923 году — как напечатано (сомнение). с. 28: отель «Чиприани» — как напечатано (сомнение по времени).
- Меры переведены в метрические (Р-64): футы, мили, акры (50 акров → 20 га), высоты и длины.

## Термины (английский → русский)

| English | Русский |
|---|---|
| The Travelers’ Companion / Le Guide du Voyageur | «Спутник путешественника» |
| Advice to Travelers; Places of Interest | советы путешественникам; достопримечательности |
| Boat-Train | «поезд к пароходу» |
| Calais coaches | вагоны Кале |
| customs check-point | таможенный пункт |
| Interallied police | межсоюзническая полиция |
| funiculaire | фуникулёр |
| vaporetti; gondola; gondolier (pl. gondoliere); pensione | вапоретто; гондола; гондольер (мн. «гондольери»); пансион |
| bora | бора |
| pound, shilling, pence, florin, half-crown | фунт, шиллинг, пенс, флорин, полкроны |
| franc, centime | франк, сантим |
| lira (pl. lire) | лира (мн. «лире») |
| dinar, para | динар, пара |
| leva | лев (в книге — «leva») |
| Turkish pound | турецкий фунт |
| Salle de Travail des Imprimés | Salle de Travail des Imprimés (без перевода) |
| Burghers of Calais | «Граждане Кале» |
| Tower of Skulls | Башня черепов |
| Old Seraglio | Старый Сераль |
| Stamboul; Pera-Galata; Iskudar | Стамбул; Пера-Галата; Ускюдар |
| Aya Sofia; Blue Mosque (Sultan Ahmet I Cammi) | Айя-София (запись — «Святая София»); Голубая мечеть (мечеть султана Ахмеда I) |
| Burnt Column of Constantine; Serpent Column; Obelisk of Thutmosis | Обгорелая колонна Константина; Змеиная колонна; обелиск Тутмоса |
| Lake Geneva (Lac Léman); Montreux; Chateau de Chillon | Женевское озеро (Леман); Монтрё; Шильонский замок |
| Brigue; Simplon Tunnel; Iselle; Domodossola | Бриг; Симплонский туннель; Изелле; Домодоссола |
| Rakek; Ljubljana; Zagreb (Agram); Brod; Nïs/Pirot | Ракек; Любляна; Загреб (Аграм); Брод; Ниш / Пирот |
| Tzaribrod; Dragoman; Dimitrovgrad; Svilengrad | Цариброд; Драгоман; Димитровград; Свиленград |
| Adrianople (Edirne); Tcherkesseui; Sinakli (Sinekli) | Адрианополь (Эдирне); Черкесекей; Синакли (Синекли) |
| The Ritz; Claridges; The Carlton; The Midland Grand | «Ритц»; «Кларидж»; «Карлтон»; «Мидленд Гранд» |
| The Lausannois; Hotel Beau-Séjour | ресторан «Лозаннуа»; отель «Бо-Сежур» |
| The Cipriani; Florian’s (Aurora, Quadri, Ortes Rosa) | «Чиприани»; кафе «Флориан» («Аврора», «Квадри», «Ортес Роза») |
| The Corso; Commercial and Nautical Academy; Museo del Mare; Municipal Museum of Antiquities | Корсо; Торговая и мореходная академия; Морской музей; Городской музей древностей |
| Pala d’Oro; balas rubies | Пала д’Оро; баласы (шпинели) |
| Fikir-Baïr (“slope of dreaming”) | Фикир-Баир («склон грёз») |

## Проверки

- `python -I -B tools/check.py kb/books/hotoe-travelers-companion-en` — в 20 своих файлах ошибок 0 (6 ошибок — ссылки в
  `children-of-fear-en`, чужая работа в процессе). Ссылки записей и предложений — все на существующие записи.
- `completeness-companion/` — 5 «пробелов» (с. 16, 26, 30, 39, 49–50) и 23 страницы с картинками: текст этих страниц уходит
  предложениями в чужие записи, картинки — `art-companion*.json` и атмосфера; после применения пробелы закроются.
- `scenario-companion/` — находок 0 (сценариев в части нет).
