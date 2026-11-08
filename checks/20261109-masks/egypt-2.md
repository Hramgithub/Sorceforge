# «Маски Ньярлатхотепа»: глава 4 «Египет», вторая половина (с. 340–384) — сверка заголовков

Часть `egypt-2` переноса «Масок» (Р-202). Книга `masks-of-nyarlathotep-en`, печатная страница = физическая − 3.
Этап — `masks-of-nyarlathotep-en/scenario/egypt` (запись egypt-1); сцены этой части продолжают `arc.order` с 22 по 43,
шаги, `conclusion`, таблица наград и уточнение `keeper_info` этапа — в файле предложений `proposals-egypt-2.json`.
Префикс записей книги — `M/` = `masks-of-nyarlathotep-en/`.

## Записи

| Вид | Записи |
|---|---|
| места (14) | `M/location/egypt-ibn-tulun-mosque` (№ 18 карты Каира), `egypt-ibn-tulun-cellar`, `egypt-al-shakti-plantation`, `egypt-al-shakti-home`, `egypt-giza`, `egypt-great-sphinx`, `egypt-mycerinus-pyramid`, `egypt-giza-tunnels` (таблица «Туннели внизу: ключ карты»), `egypt-great-chamber`, `egypt-meidum-collapsed-pyramid`, `egypt-dahshur`, `egypt-red-pyramid`, `egypt-bent-pyramid`, `egypt-nyarlathotep-sanctum` |
| сцены (22, `arc.order` 22–43) | `M/scene/egypt-…`: ibn-tulun-mosque, girdle-options, tragedy-strikes, police-investigation, al-shakti-plantation, al-shakti-home, investigating-al-shakti, giza-plateau, mycerinus-pyramid, descent-into-horror, beneath-the-pyramids, great-chamber, cult-rituals, resurrection-of-nitocris, foiling-the-resurrection, nitocris-in-cairo, collapsed-pyramid, dahshur, nyarlathotep-sanctum, nyarlathotep-arrives, doorway-to-the-past, escape |
| раздатки (2) | `M/handout/egypt-carlyle-papers-4`, `-5` (тексты — официальные «Материалы для игроков», с. 28) |
| предметы (5) | `M/item/egypt-al-shakti-logbook`, `egypt-hunting-horror-tissue`, `egypt-nodens-dagger`, `egypt-nitocris-mummy`, `egypt-hemispheric-map` |
| карты (1) | `M/map/egypt-tunnels-below` (картинка `app/maps/masks-egypt-tunnels-below.jpg`, 1104 × 714, без меток; `location` — Каир, `shows` — `egypt-giza-tunnels`, `order` 2) |
| таблицы с броском (2) | `coc:table:masks-egypt-events-beneath-the-sphinx` (1d10), `coc:table:masks-egypt-pits-and-chasms` (1d4) |
| организации, персонажи | новых нет: Братство — `M/organization/england-brotherhood-of-the-black-pharaoh`; все персонажи и существа с. 373–383 уже в базе |

Предложения (`proposals-egypt-2.json`, 62 правки, пробный прогон `apply.py --dry-run` проходит): 9 шагов этапа, `conclusion`,
таблица «Египет: награды», замена в `keeper_info` (подробности «Экспедиции Карлайла и пирамид», имя «Гипатия Мастерс» как
в записи персонажа), 20 ссылок и 3 источника этапа; ссылка из строки 18 таблицы «Каир: места на карте» на мечеть; ссылки из
сцен egypt-1 (najjars-tale, talking-to-besart, nuri-of-el-wasta, talking-to-kafour, talking-to-clive-expedition,
cairo-bulletin) и места `egypt-el-wasta` на новые места; `found_at` Пояса (подвал мечети), Короны и Ожерелья (Великий
чертог); `held_by` Двух скипетров (аль-Шакти); ссылка хронометров на дом аль-Шакти; Братство — 3 `based_at`, 1 `members`;
`where` сцены `conclusion-egypt` → туннели под Гизой; `residence` у Омара аль-Шакти, Нессима Эфти, Шарифы Раваш;
псевдонимы Ахмеда аль-Захаби («Ахмед аль-Дахаби» — официальная раздатка); псевдоним «Call the Black Pharaoh» у
`coc:spell:contact-nyarlathotep`.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| An Audacious Theft (вступление, Link) | 340 | сцена `egypt-ibn-tulun-mosque`; шаг этапа «Дерзкая кража» (предложение) |
| The Mosque of Ibn Tulun | 340 | место `egypt-ibn-tulun-mosque` (№ 18); сцена `egypt-ibn-tulun-mosque` |
| The Nazir | 340–341 | сцена `egypt-ibn-tulun-mosque`; существующие `ahmed-al-dhahabi`, `nessim-efti` |
| Locating the Girdle of Nitocris | 341–342 | место `egypt-ibn-tulun-cellar`; сцена `egypt-ibn-tulun-mosque`; существующие `guardian-ulama`, `campaign-girdle-of-nitocris`, `coc:weapon:sword-of-akmallah` |
| Keeper note (Пояс — прил. D; уничтожение — с. 361) | 342 | сцена `egypt-ibn-tulun-mosque` |
| Options; Guarding the Girdle; Stealing the Girdle; Leaving Cairo with the Girdle; Other Options | 342 | сцена `egypt-girdle-options` |
| Tragedy Strikes | 342–343 | сцена `egypt-tragedy-strikes` |
| Pulp: Mean and Nasty | 343 | сцена `egypt-tragedy-strikes` (`mechanics`) |
| Carlyle Papers Egypt #4 | 343 | `handout/egypt-carlyle-papers-4` |
| The Police Investigation; Keeper note | 343 | сцена `egypt-police-investigation`; предмет `egypt-hunting-horror-tissue` |
| A Dangerous Man (вступление, 8 связей) | 344 | сцена `egypt-al-shakti-plantation` |
| The Plantation | 344–345 | место `egypt-al-shakti-plantation`; сцена `egypt-al-shakti-plantation` |
| Omar al-Shakti’s Home | 345 | место `egypt-al-shakti-home`; сцена `egypt-al-shakti-home` |
| Talking to al-Shakti; The Carlyle Expedition; Jackson Elias | 345 | сцена `egypt-al-shakti-home` |
| Keeper note (аль-Шакти уже знает сыщиков) | 346 | сцена `egypt-al-shakti-home` |
| Other Lines of Inquiry | 346 | сцена `egypt-al-shakti-home` («Другие расспросы») |
| Investigating al-Shakti | 346 | сцена `egypt-investigating-al-shakti` |
| The Safe | 347 | сцена `egypt-investigating-al-shakti`; место `egypt-al-shakti-home`; предмет `egypt-al-shakti-logbook` |
| Carlyle Papers Egypt #5 | 347 | `handout/egypt-carlyle-papers-5` |
| The Horrors Below (эпиграф, вступление, связи) | 348 | сцена `egypt-giza-plateau` |
| The Riddle of the Great Sphinx | 348 | место `egypt-great-sphinx` и `egypt-giza` (`history`); сцена `egypt-giza-plateau` |
| Giza | 348 | место `egypt-giza`; сцена `egypt-giza-plateau` |
| Following Up Leads | 349 | сцена `egypt-giza-plateau` |
| Mycerinus’ Pyramid; Searching the Pyramid | 349 | место `egypt-mycerinus-pyramid`; сцена `egypt-mycerinus-pyramid` |
| Descent into Horror | 349–350 | сцена `egypt-descent-into-horror` |
| Entrance A | 350–351 | место `egypt-great-sphinx`; место `egypt-giza-tunnels`; сцена `egypt-descent-into-horror` |
| Map: The Tunnels Below (ключ 1–7, A–D, врезка «Other entrances to the Tunnels») | 350 | `map/egypt-tunnels-below`; таблица «Туннели внизу: ключ карты» у `egypt-giza-tunnels` |
| Entrance B; Entrance C; Entrance D | 351 | место `egypt-giza-tunnels`; сцена `egypt-descent-into-horror` |
| Beneath the Pyramids; The Main Tunnel | 351 | место `egypt-giza-tunnels`; сцена `egypt-beneath-the-pyramids` |
| Table: Events Beneath the Sphinx | 352 | `coc:table:masks-egypt-events-beneath-the-sphinx` |
| The Side Tunnels | 352 | место `egypt-giza-tunnels`; сцена `egypt-beneath-the-pyramids` |
| Finding the Path; Random Events | 353 | сцена `egypt-beneath-the-pyramids`; описание таблицы событий |
| Pulp: Additional Hazards; Table: Pits and Chasms | 354 | `coc:table:masks-egypt-pits-and-chasms` (врезка — в `description`) |
| The Great Chamber of Nyarlathotep | 355 | место `egypt-great-chamber`; сцена `egypt-great-chamber` |
| The Pillars; Stair to the Underworld; The Leech Pit | 355–356 | место `egypt-great-chamber`; сцена `egypt-great-chamber` (`mechanics`) |
| Missing Persons (врезка) | 355 | сцена `egypt-cult-rituals`; место `egypt-giza-tunnels` (камеры) |
| The Altar; The Throne; The Processional Bridge; The Stele | 356 | место `egypt-great-chamber`; сцена `egypt-great-chamber` |
| The Enormous Hole | 357 | место `egypt-great-chamber`; сцена `egypt-great-chamber` |
| The Black Sphinx (врезка) | 357 | сцена `egypt-great-chamber`; существующее `creature/black-sphinx` |
| The Cult’s Rituals | 358 | сцена `egypt-cult-rituals` |
| Special Rites for Queen Nitocris; The Order of Ceremonies | 358, 360 | сцена `egypt-resurrection-of-nitocris` |
| Foiling the Resurrection of Nitocris; The Mummy | 360 | сцена `egypt-foiling-the-resurrection`; предмет `egypt-nitocris-mummy` |
| Deus Ex | 360 | сцена `egypt-foiling-the-resurrection`; предмет `egypt-nodens-dagger` |
| Death and the Maiden? | 360–361 | сцена `egypt-foiling-the-resurrection` |
| Pulp: Smash and Grab | 361 | сцена `egypt-foiling-the-resurrection` |
| The Items of Power; Destroying the Crown / Necklace / Girdle of Nitocris | 361–363 | сцена `egypt-foiling-the-resurrection` (`description`, `mechanics`) |
| An Unfamiliar Face; Nitocris in Cairo | 363 | сцена `egypt-nitocris-in-cairo`; предложение `residence` Шарифы Раваш |
| Into the Sanctum (вступление, связи) | 364 | сцена `egypt-collapsed-pyramid` |
| Meidum: The Collapsed Pyramid | 364 | место `egypt-meidum-collapsed-pyramid`; сцена `egypt-collapsed-pyramid` |
| Dahshur; The Red Pyramid; The Bent Pyramid | 364 | места `egypt-dahshur`, `egypt-red-pyramid`, `egypt-bent-pyramid`; сцена `egypt-dahshur` |
| The North Entrance; The West Entrance | 365 | место `egypt-bent-pyramid`; сцена `egypt-dahshur` |
| Nyarlathotep’s Sanctum; The Throne; The Bas-Reliefs; Keeper note | 365–366 | место `egypt-nyarlathotep-sanctum`; сцена `egypt-nyarlathotep-sanctum` |
| The Astronomy Wall | 366 | место `egypt-nyarlathotep-sanctum`; сцена `egypt-nyarlathotep-sanctum` |
| The Hemispheric Map; Keeper note | 366–367 | предмет `egypt-hemispheric-map`; сцена `egypt-nyarlathotep-sanctum` |
| Nyarlathotep Arrives; Keeper note | 366–367 | сцена `egypt-nyarlathotep-arrives` |
| Nyarlathotep’s Offer; Keeper note | 367–368 | сцена `egypt-nyarlathotep-arrives` |
| Nyarlathotep’s Rebuke; Truth or Fiction?; Interview’s End | 368–369 | сцена `egypt-nyarlathotep-arrives` |
| Small Victories (врезка) | 368 | сцена `egypt-nyarlathotep-arrives` |
| Taking on a God | 369–370 | сцена `egypt-nyarlathotep-arrives` |
| Pulp: Doorway to the Past (Escape!, Magic, Further Adventure, Keeper note) | 369 | сцена `egypt-doorway-to-the-past` |
| Conclusion; Escape | 370 | сцена `egypt-escape`; `conclusion` этапа (предложение) |
| The Carlyle Expedition and the Pyramids (врезка) | 370 | сцена `egypt-nyarlathotep-sanctum`; место `egypt-nyarlathotep-sanctum`; замена в `keeper_info` этапа (предложение) |
| Nitocris’ Plans; At Cross-Purposes? | 370–372 | сцена `egypt-nitocris-in-cairo` |
| Rewards; Bringing Down a God: Egypt; Pulp: Rewards | 372 | `conclusion` этапа и таблица «Египет: награды» (предложения) |
| Characters and Monsters: Egypt (вступление) | 372 | существующие записи персонажей и существ |
| Guides and Robbers: Ibi Moussa; Robbers, various troublemakers; Hakim; Saleem Naziz; Mahmoud | 373 | существующие `ibi-moussa`, `robbers-various-troublemakers`, `hakim`, `saleem-naziz`, `mahmoud` |
| Allies or Independents: Faraz Najjar; Warren Besart; Nigel Wassif; Dr. Ali Kafour | 374 | существующие `faraz-najjar`, `warren-besart`, `nigel-wassif`, `ali-kafour` |
| Dr. Emile Vabreaux; Egyptian Policeman/Guard | 375 | существующие `emile-vabreaux`, `egyptian-policeman-guard` |
| Ibn Tulun Mosque: Ahmed al-Dhahabi; Nessim Efti; Guardian Ulama | 375 | существующие `ahmed-al-dhahabi`, `nessim-efti`, `guardian-ulama`; места мечети (`residents`) |
| Members of the Clive Expedition: Henry Clive; Martin Winfield; James Gardner; Johanna Specht; Agatha Broadmoor | 376–377 | существующие `henry-clive`, `martin-winfield`, `james-gardner`, `johanna-specht`, `agatha-broadmoor` |
| Adversaries: Omar al-Shakti; Hetep, cat-demon; Sharifa Rawash | 377–378 | существующие `omar-al-shakti`, `creature/hetep`, `sharifa-rawash` |
| Average Brotherhood Cultists (Egypt), Assorted Thugs | 379 | существующий `average-brotherhood-cultists-egypt` |
| Additional Cultists of the Brotherhood (Resurrection Ceremony) | 380 | существующий `additional-cultists-of-the-brotherhood-resurrection-ceremony` (опечатка «Dodge 50% (20/8)» уже в его `errata`) |
| Monsters: Million Favored Ones: Leeches; Children of the Sphinx | 381 | существующие `creature/million-favored-ones-leeches`, `creature/child-of-the-sphinx-masks` |
| Sample Children of the Sphinx | 382 | существующий `creature/sample-children-of-the-sphinx` |
| Sand-dwellers, Stalkers of the Wastes | 382 | `coc:creature:sand-dweller` (ссылки); расхождение профиля — см. «Не взято» |
| The Black Pharaoh, avatar of Nyarlathotep; The Black Sphinx, spawn of Nyarlathotep | 383 | существующие `creature/black-pharaoh-masks`, `creature/black-sphinx` |

Статблоки с. 373–383 не менялись и заново не сверялись (персонажи и существа заведены раньше).

## Строки аудита `checks/20261025-masks/not_in_kb.md` (с. 340–384)

| Строка аудита | Что взяло |
|---|---|
| 38: Sand-dwellers, Stalkers of the Wastes (385/382) | не перенесено: профиль «Масок» отличается от `coc:creature:sand-dweller` Скоростью (8 против 7) и строкой заклинаний (30% знать 1d6 заклинаний) — вопрос владельцу (отдельная запись «Обитатель песков («Маски»)» по Р-75 или пометка); запись чужая |
| 49: Table: Events Beneath the Sphinx (355/352) | `coc:table:masks-egypt-events-beneath-the-sphinx` |
| 50: Table: Pits and Chasms (357/354) | `coc:table:masks-egypt-pits-and-chasms` |
| 62: Rewards — Египет (375/372) | `conclusion` этапа и таблица «Египет: награды» (предложения) |
| 112: Hemispheric Map (369–370/366–367) | предмет `egypt-hemispheric-map` |
| 165: Egypt #4 (346/343) | `handout/egypt-carlyle-papers-4` |
| 166: Egypt #5 (350/347) | `handout/egypt-carlyle-papers-5`; визитка Гэвигана — существующая `america-carlyle-papers-2`; журнал — `egypt-al-shakti-logbook` |
| 198: The Tunnels Below (353/350) | `map/egypt-tunnels-below`, место `egypt-giza-tunnels` |
| 266: Mosque of Ibn Tulun (343/340) | места `egypt-ibn-tulun-mosque`, `egypt-ibn-tulun-cellar` |
| 267: Плантация и дом Омара аль-Шакти (347–348/344–345) | места `egypt-al-shakti-plantation`, `egypt-al-shakti-home` |
| 268: Giza: Sphinx, Mycerinus’ Pyramid, Beneath the Pyramids, Great Chamber, Enormous Hole (351–361/348–358) | места `egypt-giza`, `egypt-great-sphinx`, `egypt-mycerinus-pyramid`, `egypt-giza-tunnels`, `egypt-great-chamber` |
| 269: Dahshur: Red, Collapsed, Bent Pyramid, Nyarlathotep’s Sanctum (367–372/364–369) | места `egypt-dahshur`, `egypt-red-pyramid`, `egypt-meidum-collapsed-pyramid`, `egypt-bent-pyramid`, `egypt-nyarlathotep-sanctum` |
| 347: египетская полиция (346/343) | сцены `egypt-police-investigation`, `egypt-giza-plateau`; существующий `egyptian-policeman-guard` |
| 398: Call the Black Pharaoh (381/378) | предложение: псевдоним у `coc:spell:contact-nyarlathotep` |
| 447: …and the Pyramids; Nitocris’ Plans (373/370) | сцены `egypt-nyarlathotep-sanctum`, `egypt-nitocris-in-cairo`; замена в `keeper_info` этапа |
| 449: Нитокрис — Cairo (366/363) | сцена `egypt-nitocris-in-cairo` |
| 452: The Cult’s Rituals; Special Rites for Queen Nitocris (361/358) | сцены `egypt-cult-rituals`, `egypt-resurrection-of-nitocris` |
| 462: Conclusion главы (373/370) | сцена `egypt-escape`; `conclusion` этапа |

## Опечатки и расхождения книги

| Где | Напечатано | Ожидалось | Запись |
|---|---|---|---|
| с. 348 | связь «(The Plantation and The Cult’s Rituals, pages 358 and 344 respectively)» | с. 344 и 358 | `errata` сцены `egypt-giza-plateau` (`fixed: true`) |
| с. 356 | «peep cautiously around the sides of the obelisk» | стела | пометка в `egypt-great-chamber` |
| с. 342, 367 | профиль охотящегося ужаса — «Characters and Monsters: England, page 284» | профиль на с. 292 (284 — начало раздела, как «Characters and Monsters: Egypt, page 372») | пометки в сценах `egypt-tragedy-strikes`, `egypt-nyarlathotep-arrives`; не опечатка |
| с. 343 / «Материалы для игроков» | Egypt #4: «al-Dhahabi»; официальный перевод: «аль-Дахаби» | в базе — «аль-Захаби» | текст раздатки — как напечатан; предложение псевдонима |
| с. 347 / «Материалы для игроков» | Egypt #5: подпись «A. P.»; официальный перевод: «О. П.» | — | пометка в раздатке |
| с. 364 | «Just over 20 miles (35 km)» | 20 миль ≈ 32 км («just over») | метрическое значение книги, без `errata` |
| с. 365, 380 | «Charm role»; «It’s width» | — | словесные, не записаны (Р-39) |

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Иллюстрации: «A hunting horror attacks the Ibn Tulun Mosque», «Having tea with Omar al-Shakti and his cat, Hetep», «The Children of the Sphinx», «The Resurrection of Nitocris» (с. 359 целиком), «The Items of Power», «The Circlet of Nata Haje», «The Hemispheric Map», «Reign of the Black Pharaoh», фронтиспис главы «Кения» (с. 384 целиком) | 341–384 | картинки добавляются отдельно (`pipeline/art/add_images.py`, Р-165) |
| Отдельные записи мест: больница Каср-эль-Айни (остров Рода), лаборатория доктора Вабро, отель «Мена-Хаус», контора экскурсий, раскопки Венской академии и Гарварда | 343, 348 | только упомянуты; описаны текстом в сценах и в записи `egypt-giza` |
| Записи персонажей: безымянный врач приюта, двое мальчиков с едой, местный проводник в пирамиде, Эмиль Бараз (исторический инженер), Снофру, сын Саладина, Тутмос IV | 340–349, 364 | без статблока и без самостоятельных действий (или исторические лица); оставлены текстом |
| Организация «стражи Пояса» (улемы мечети) | 341 | книга не описывает их как организацию; групповой профиль `guardian-ulama` и место `egypt-ibn-tulun-cellar` покрывают их |
| Предмет «белые балахоны культистов с перевёрнутыми анхами» | 345, 357 | мелочь без механики; текстом в сценах |
| Вариант профиля обитателя песков из «Масок» (Скорость 8, шанс заклинаний) | 382 | запись `coc:creature:sand-dweller` чужая; вопрос владельцу (см. аудит, строка 38) |
| Поле `chase` (погони) | 358, 370 | в схеме персонажа нет; бегство и погоня — текстом в `mechanics` сцен |
| Метки на карте (`spots`) | 350 | по Р-202 карты без меток; ключ — таблица у `egypt-giza-tunnels` |
| Ссылки на раздатки и места других глав, которых ещё нет в базе (Англия 11–12, Австралия 4–5, Китай 8, «Хо Фан: импорт и экспорт», «Рэндольф Шиппинг Ко.», мастерская сэра Обри, Миср-Хаус, «Эмпайр Спайсес», Гора Чёрного ветра) | 344–369 | только текстом, чтобы не ломать проверку ссылок; после сведения других частей можно добавить `refs` |
