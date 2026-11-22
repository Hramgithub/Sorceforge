# The Star on the Shore — часть town (печ. с. 14–50)

Книга `star-on-the-shore-en` — скан без текстового слоя; всё сверено по изображениям страниц.
Смещение страниц: **печатная = физическая − 3** (физ. 15 = с. 12, физ. 17 = с. 14, физ. 52 = с. 49; физ. 53 — полностраничная
иллюстрация без номера, по счёту с. 50). Префикс id мест — `star-on-the-shore-en/location/loc-<N>-<slug>`.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Keeper's Map (Rockport, MA), врезки Rockport / Straitsmouth Island / Thacher Island | 14–15 | `map/keeper-map-rockport` (39 меток; разворот склеен и повёрнут) |
| City of Rockport (окончание: NPC, туннели, туман, пешком/машиной, трамвай) | 16 | сцена core `scene/star-city-of-rockport`; трамвай — в `map/keeper-map-rockport` (quality.notes); туннели и Холл — `character/scott-hall` |
| Location 1 — Rockport Police Department | 16–17 | `location/loc-1-rockport-police-department`; план — `map/police-station-plan` |
| Officer Michael Wild (+статблок) | 16 | `character/michael-wild` |
| Chief Corey Studdard (+статблок) | 17 | `character/corey-studdard` |
| Police Station (ключ 1–6, план) | 17 | `location/loc-1-…` (описание), `map/police-station-plan` |
| Location 2 — Griffon Butcher Shop (таблица мяса по времени суток) | 18 | `location/loc-2-griffon-butcher-shop` (tables) |
| Harry Wensor | 18 | `character/harry-wensor` |
| Location 3 — Smith Hardware | 18–19 | `location/loc-3-smith-hardware` |
| Christina Smith (+статблок) | 18–19 | `character/christina-smith` |
| Location 4 — Train Depot (расписание) | 19 | `location/loc-4-train-depot` (tables) |
| Rebecca Wood (+статблок) | 19 | `character/rebecca-wood` |
| Location 5 — The Woods House (объявление, дело 1877 года) | 19–22 | `location/loc-5-the-woods-house` |
| Sarah Hikey; Ethan “Big E” Denham; Tommy; Phyllis | 21–22 | `character/sarah-hikey`, `ethan-denham`, `tommy`, `phyllis` |
| Location 6 — Thacher Island Lighthouses (сарай, доска, табличка) | 22 | `location/loc-6-thacher-island-lighthouses`, `item/thacher-bronze-plaque` |
| Tanner Bivens; 6 assistants | 22–23 | `character/tanner-bivens`, `character/lighthouse-assistants` |
| Location 7 — Rockport Granite Company | 23–24 | `location/loc-7-rockport-granite-company`, `character/granite-workers` |
| Justice Gordan (+статблок «Justice Gordon») | 24 | `character/justice-gordan` |
| Ryan Grimsley (+статблок) | 24 | `character/ryan-grimsley` |
| Location 8 — Quarry #1 | 24–25 | `location/loc-8-quarry-1` |
| Locations 9 & 10 — Quarries #2 & #3 | 25 | `location/loc-9-quarry-2`, `location/loc-10-quarry-3` |
| Foremen; Neil McCarth (+статблок); J. Pekka Myllyluoma (+статблок); Ray Ingrahm | 25 | `character/neil-mccarth`, `j-pekka-myllyluoma`, `ray-ingrahm` |
| Location 11 — Granite Pharmacy; Stephen Drake | 26 | `location/loc-11-granite-pharmacy`, `character/stephen-drake`, `item/knockout-gas` |
| Location 12 — David Babson Co.; Lisa Turner; Olias ‘Ollie’ Cheatham | 26 | `location/loc-12-david-babson-co`, `character/david-babson`, `lisa-turner`, `olias-cheatham`, `item/babson-notes` |
| Location 13 — Bailey's Barber; Michel Foisy (+статблок «Michael Foisy») | 26–27 | `location/loc-13-baileys-barber`, `character/michel-foisy` |
| Location 14 — Pigeon Cove Chapel | 27–28 | `location/loc-14-pigeon-cove-chapel` |
| Rev. Jack Sardonicus (+статблок) | 27 | `character/jack-sardonicus` |
| Gabriel Rahn (+статблок, дневник) | 27–28 | `character/gabriel-rahn`, `item/gabriel-journal`, `item/gabriel-enchanted-blade` |
| Raven “Shadowz” Alexis (+статблок) | 28 | `character/raven-alexis` |
| Location 15 — Cape Ann Tool Company; Jeffrey Graves | 29 | `location/loc-15-cape-ann-tool-company`, `character/jeffrey-graves` |
| Location 16 — The Witch House | 29–30 | `location/loc-16-the-witch-house`, `item/yde-etad-scroll` |
| Cindy Alvarez (+статблок) | 30 | `character/cindy-alvarez` |
| The Ghost of Danny Williams (статблок) | 30 | `creature/ghost-of-danny-williams` (`instance_of` `coc:creature:ghost`) |
| Banishment of Yde Etad (стоимость) | 30 | `item/yde-etad-scroll` (mechanics) → `coc:spell:banishment-of-yde-etad` |
| Location 17 — Old Man Douglas's House; Alan Douglas (+статблок) | 31 | `location/loc-17-old-man-douglass-house`, `character/alan-douglas` |
| Location 18 — Post and Telegraph Office; Marjorie “Wolf” Osteen (+статблок «Majorie»); Jim Reese | 32 | `location/loc-18-post-and-telegraph-office`, `character/marjorie-osteen`, `jim-reese` |
| Location 19 — Town Hall; Nash Philburton (+статблок); бланк «Request for City Records» | 32–33 | `location/loc-19-town-hall`, `character/nash-philburton`; бланк = раздатка 6 (core) |
| Location 20 — Universalist Church; Bernard Leong | 33–34 | `location/loc-20-universalist-church`, `character/bernard-leong` |
| Location 21 — Congregational Church / The Old Sloop (план, ядро 1814 года) | 34–36 | `location/loc-21-the-old-sloop`, `map/congregational-church-plan`; ядро — `item/rift-bomb-cannonball` (abyss) |
| Reverend Ronald Lynn | 35–36 | `character/ronald-lynn` |
| Location 22 — John Tarr Store; Samuel Cox | 36 | `location/loc-22-john-tarr-store`, `character/samuel-cox` |
| Location 23 — Rockport Memorial Hall; Col. Scott Hall (+статблок) | 36–37 | `location/loc-23-rockport-memorial-hall` (таблица расписания Холла), `character/scott-hall` |
| Location 24 — Rockport Library (список статей → раздатки 7–13); Stephen White | 37–38 | `location/loc-24-rockport-library` (tables), `character/stephen-white` |
| Location 25 — Sandy Bay Cafe; Evelyn McGillicutty-Jones; Ron Lynn | 38–39 | `location/loc-25-sandy-bay-cafe`, `character/evelyn-mcgillicutty-jones`, `ron-lynn` |
| Location 26 — Rockport Art Association; Craig O’Casey | 39 | `location/loc-26-rockport-art-association`, `character/craig-ocasey` |
| Location 27 — Bearskin Neck; Howard Smith; Stephanie Thompson; Andrew Green | 40 | `location/loc-27-bearskin-neck`, `character/bearskin-neck-painters`, `howard-smith`, `stephanie-thompson`, `andrew-green` |
| Location 28 — Bradley Brothers Ships and Fishing; Adam Alexander; Eddie Guy (история о ведьме) | 41–43 | `location/loc-28-bradley-brothers-ships-and-fishing`, `character/adam-alexander`, `eddie-guy` |
| Location 29 — The Red Barn—Motif #1 (бронзовая табличка) | 43–44 | `location/loc-29-red-barn`, `item/red-barn-bronze-plate` |
| Location 30 — Interstate Fish Corporation; Kindle Cimmerian (распылители) | 44 | `location/loc-30-interstate-fish-corporation`, `character/kindle-cimmerian`, `item/freezing-spray` |
| Location 31 — Sandy Bay Bakery; Zach Glazer | 45 | `location/loc-31-sandy-bay-bakery`, `character/zach-glazer` |
| Location 32 — Rockport Theatre; Kevin Wright; Deandre Wright | 45–46 | `location/loc-32-rockport-theatre`, `character/kevin-wright`, `deandre-wright` |
| Location 33 — Tuck Upholstery; Maurine Daugherty | 46 | `location/loc-33-tuck-upholstery`, `character/maurine-daugherty` |
| Location 34 — 224 School Street, Home of Nash Philburton (список культистов, заметки, план) | 46–47 | `location/loc-34-224-school-street`, `scene/star-nash-philburton-murder`, `item/nash-cultist-list`, `item/nash-research-notes`, `map/224-school-street-plan` |
| Location 35 — Parrish Cemetery; Brent “Lump” Collins (+статблок) | 48 | `location/loc-35-parrish-cemetery`, `character/brent-collins` |
| Location 36 — Sandy Bay Rock Island | 48 | `location/loc-36-sandy-bay-rock-island` |
| Location 37 — Fisherman’s Wharf; Captain Chase Street (+статблок); Daniel Klaminder (+статблок) | 48–49 | `location/loc-37-fishermans-wharf`, `character/chase-street`, `daniel-klaminder`, `item/street-harpoons` |
| Location 38 — Straitsmouth Island; Rolf Halverson | 49 | `location/loc-38-straitsmouth-island`, `character/rolf-halverson` |
| Location 39 — Rockport Report; Sean Taylor | 49 | `location/loc-39-rockport-report`, `character/sean-taylor` |
| Полностраничная иллюстрация (щупальца и маяки) | 50 | `atmosphere-town.json` |

Портреты (9): Сара Хайки, Таннер Бивенс, Алан Дуглас, Скотт Холл, Стивен Уайт, Крейг О’Кейси, Адам Александер, Зак Глейзер,
Чейз Стрит — `art-town.json`, применены (`art-town-proposals.json`), файлы `app/art/characters/star-town-*.webp`.
Карты (4): `app/maps/star-town-keeper-map-rockport.jpg`, `star-town-police-station.jpg`, `star-town-congregational-church.jpg`,
`star-town-224-school-street.jpg`; рамки — `map-boxes-town.json`.

## Не взято

- Копии раздаток в тексте глав: бронзовая табличка острова Тэтчер (с. 22, = раздатка 17), таблички Красного сарая (с. 43 и 44,
  = раздатки 15 и 16) — раздатка берётся из «Player Aids» (часть core); предметы-находки заведены (`item/thacher-bronze-plaque`,
  `item/red-barn-bronze-plate`).
- Семь атмосферных иллюстраций — в `atmosphere-town.json` (сводит ведущий).
- Подписи улиц, врезка «Rockport» и маршрут трамвая на карте Хранителя — без меток (нет записей), упомянуты в `quality.notes` карты.
- «NPC random chart» (место 13, с. 27): в книге такой таблицы нет — бросок оставлен текстом, без ссылки.
- Существа Мифов на резных фигурах Алана Дугласа (Король в Жёлтом, Ньярлатхотеп, Йиг, Атлак-Нака, глубоководный, ми-го, Древний,
  йитианец) — только текст, без ссылок.
- Упомянутые без записи (только текст): Джо Смит (отец Кристины), Анри Вудс, Альберт Джой, Чарльз Х. Гилман, Мэри Проктор,
  доктор Таппер, Джордж Перкинс, Джон и Джим Брэдли, Джон Брэдли-младший, Томас Прэнг (мавзолей).

## Опечатки и сомнения книги (в `errata` записей)

- Gordan / Gordon (заголовок статблока, с. 24) — `justice-gordan`.
- Michel / Michael Foisy (статблок и одна фраза, с. 27) — `michel-foisy`.
- Marjorie / Majorie (статблок, с. 32; так же в сводке культистов, с. 62) — псевдоним `marjorie-osteen`.
- Nash / Nathan (с. 33) — `nash-philburton`; адрес в записке «246 School Street» вместо 224 (с. 33) — `loc-19-town-hall`.
- Bernard / Christopher Leong (с. 36) — `bernard-leong`.
- Zach / Richard Glazer (с. 45) — `zach-glazer`.
- Harry / Brian (мясник, с. 18) — `harry-wensor`.
- Доли процентов исправлены (Р-35): Стаддард, Винтовка 60% (30/6) → (30/12); Маккарт, Драка 50% (25/5) → (25/10).
- Производные (Р-161, как напечатано): Синди Альварес — БкУ «нет»/Комплекция 0 при СИЛ+ТЕЛ 80 (−1/−1); Скотт Холл — Скорость 7 (по правилам 8).
- Не в errata, в заметках: «Sport Hidden» у Габриэля; «Mass Charm» в дневнике vs «Mass Suggestion» в справочном разделе;
  7 августа (Леонг) и 9 августа (заметки Нэша); встреча у Нэша в 19:30, но «в 19:20 или позже» Нэш мёртв; доктор Таппер купил
  дом в 1870 году и умер «чуть больше года назад» (возраст неправдоподобен — не опечатка, просто заметка в отчёте);
  «pistons» вместо «pistols», «bread and breakfast» — исправлено в переводе молча (Р-39).

## Термины (English → русский)

| English | Русский |
|---|---|
| Star Spawn | звёздное отродье |
| Deep Ones | глубоководные |
| Keeper's Map | карта Хранителя |
| The Old Sloop / Congregational Church | церковь Олд-Слуп / конгрегационалистская церковь |
| The Witch House | Дом ведьмы |
| The Woods House | Дом Вудса |
| Red Barn — Motif #1 | Красный сарай («Мотив № 1») |
| Bearskin Neck | Бэрскин-Нек |
| Pigeon Cove (Chapel) | (часовня) Пиджен-Коув |
| Sandy Bay (Cafe/Bakery) | Сэнди-Бэй |
| Sandy Bay Rock Island | остров Сэнди-Бэй-Рок |
| Thacher Island | остров Тэтчер |
| Straitsmouth Island | остров Стрейтсмут |
| Rockport Granite Company | Гранитная компания Рокпорта |
| Granite Pharmacy | аптека «Гранит» |
| Smith Hardware | скобяная лавка Смита |
| Griffon Butcher Shop | мясная лавка «Гриффон» |
| Bailey's Barber | парикмахерская Бейли |
| Cape Ann Tool Company | Инструментальная компания Кейп-Энн |
| Bradley Brothers Ships and Fishing / Bradley Wharf | «Суда и рыбалка братьев Брэдли» / пристань Брэдли |
| Interstate Fish Corporation | Межштатная рыбная корпорация |
| Rockport Memorial Hall | Мемориальный зал Рокпорта |
| Rockport Art Association | Художественная ассоциация Рокпорта |
| Rockport Report | «Рокпорт рипорт» |
| Tuck Upholstery | обивочная мастерская Така |
| Parrish Cemetery | кладбище Пэрриш |
| Fisherman’s Wharf | Рыбацкая пристань |
| Universalist Church | церковь универсалистов |
| Enchanted Blade (MB) | зачарованный клинок (МБ — магический бонус) |
| Summon Spirit Animal | Призыв духа-зверя |
| Shadow Protection | Защита тенями |
| Obscuring Shadows | Скрывающие тени |
| Control Birds | Власть над птицами |
| Mass Charm | Массовое обаяние |
| Contact Star Spawn | Связь со звёздным отродьем (общая запись «Связь со звёздным отродьем Ктулху») |
| Banishment of Yde Etad | Изгнание Йде Итад (общая запись) |
| deacon (of Gabriel) | дьякон Габриэля |
| Shadowz / Wolf / Lump / Big E (прозвища) | Шэдоуз / Вулф / Ламп / Биг И (транслитерация) |
| Envelope Attack | Обволакивание |
