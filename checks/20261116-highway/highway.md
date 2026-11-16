# The Highway of Blood (`highway-of-blood-en`) — перенос в базу (Р-251)

Alex Guillotte (с Ian Christiansen, Davae Breon Jaxon), © 2019; Critical Hit Publishing, Miskatonic Repository. Западный Техас, июль 1975 года — эпоха `1940s-1980s` (Р-252).
Русского перевода в базе нет (проверено по ключевым именам и местам: Abattoir/Абаттуар, Teihiihan, Osteen, dustbilly, Highway of Blood).

Страницы: PDF 131 физ. страница (физ. 131 пустая); печатная = физической (смещение **0**). Номера не напечатаны на физ. 1–4 (обложка, выходные данные, оглавление, эпиграф), 17–18, 42, 69–70 (полностраничные карты и схема хронологии), 80 (стихи Элиота), 98–126 (приложения VI «Handouts» и VII листы прегенов, а также портреты), 129–130 (газета, задняя обложка) — в `sources` у них `printed_page: null`.

## Записи (259)

- сценарий 1 (`scenarios/highway-of-blood`: summary, keeper_info, hook, advice, 10 шагов, conclusion с наградами, таблица «Случайные опасности» + 6 ссылок на таблицы мест)
- сцены 21 (хронология 0–14 + 5a–c, «Ссора в „Последней остановке“», «Ночь в Камере», «Аудиенция у Аль’иссы»)
- персонажи 62: горожане (47), Усадьба (Остин, Сет, Бреннер, Кутер, Кеб, Эйбл), Аль’исса (instance_of «Змеечеловек»), групповые профили «Дастбилли» и «Пленницы Красного дома» (имена придуманы, Р-151), Холгейт, Миллеры (4), готовые сыщики 6 (pregen)
- существа 5: «Тейхиихан» (уникальное), «Стая крыс-мутантов» (instance_of «Стая крыс»), «Порождение Йига («Шоссе крови»)», «Дети Йига («Шоссе крови»)», «Рой металлических жуков» (уникальное)
- организации 4, предметы 23, книги Мифов 2 (издание «De Vermis Mysteriis» Холгейта — edition_of общей записи; «Евангелие Остина»)
- раздатка 20 (раздатки 1, 2, 4–12, 14, 15, 17, 19–24; 3, 13, 16, 18 — карты Хранителя, см. карты)
- места 102 (город, окрестности «Хребет Дьявола», места ключа 1–13, 2a–2c, 3a–3m, улицы с таблицами домов, дороги 13b, Усадьба 14a–14n, посёлок 15a–15e, шахты 1–10, пещеры 1–16 и 15a–15e)
- карты 8 (`app/maps/highway-*.jpg`): Абаттуар, центр, Хребет Дьявола (раздатка 3), Усадьба (с. 42 = раздатка 13), посёлок (раздатка 14), земли компании (раздатка 17), штольни (раздатка 16), Змеиные пещеры (с. 69 = раздатка 18) — метки на каждом номере ключа, номерах домов и подписях
- правила книги 11 (`rules/`): предупреждение о содержании, Охота (4), Правило трёх, опасности окружения, условия пустыни, новые заклинания, радиоактивные материалы, 1970-е

Картинки 57 (применены `pipeline/integrate/apply.py`, `art.json` → `art-proposals.json`): 19 портретов, 4 арта существ, предметы/книга/правило/план арсенала, раздатка, листы 6 прегенов (`card`). Атмосфера — `atmosphere.json` (32 страницы).

Предложения к общим записям — `proposals-highway.json` (1, пробный прогон проходит): экземпляр «De Vermis Mysteriis» в `copies` общей записи.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, Credits, Contents | физ. 1–3 | сценарий (`sources`); атмосфера |
| Эпиграф (Матфей 23:33) | физ. 4 | сценарий (`sources`); атмосфера |
| Warning (Content Warning) | 5 | правило `content-warning` |
| Scenario, Overview | 6 | сценарий: summary |
| Using This Book | 7 | сценарий: advice |
| Plot Hooks | 7–8 | сценарий: hook |
| Preparation | 8 | сценарий: hook; правило `driving-stunts-and-vehicles` |
| Motivations (The Priestess, The Book, The Hunt, The Sacrifices, The Other Victims) | 8–9 | сценарий: keeper_info; `alissya`; организация `dustbillies`; Миллеры |
| Keeper Information: Background (Serpent People, Mescalero Apache, Founding of Midian, Return of the Teihiihan, Rise of the Dustbillies) | 9–11 | сценарий: keeper_info; `abattoir` (history); `teihiihan`; `dustbillies` |
| Running the Scenario | 12 | сценарий: advice |
| Abattoir: The Residents | 13–14 | `abattoir` (ключ жителей); сценарий: advice |
| Setting the Mood | 14 | `abattoir` |
| Starting Trouble | 14 | сцена `trouble-at-last-stop` |
| Prologue | 15 | сцена `opening-credits`; `highway-385`; `coyote-mike` |
| Welcome to Abattoir | 16 | сцена `arrival-in-abattoir`; `abattoir` |
| 1. Esso Gas Station | 16, 19 | `esso-gas-station`; Расс, Нейт, Стив |
| Abattoir Map; Town Center Map | 17–18 | карты `abattoir-map`, `town-center-map` |
| 2. Weyland Estates (таблица 01–100) | 19–24 | `weyland-estates` (таблица полностью); 2a–2c — места по ключу карты; `pete-smith`; `lsd`, `heroin` |
| 3. Abattoir Town Center; 3a–3m | 24–30 | `town-center`; 13 мест 3a–3m; их жители |
| 4. Blood of the Lamb Pentecostal Church | 31–32 | `blood-of-the-lamb-church`; `billy-scott`; `righteous-fury` |
| 5. Weyland School | 32–33 | `weyland-school` |
| 6. Abattoir Water Works | 33 | `water-works`; `vance-kennet` |
| 7. Abattoir Cemetery | 33 | `cemetery`; `malcolm-ferrell` |
| 8. Hackett & Sons Beef Co. | 33 | `hackett-beef-co`; организация `hackett-and-sons` |
| 9. Benson’s Hardware | 34 | `bensons-hardware`; `benson-house`; Бенсоны |
| 10. Highway 6 Diner | 34 | `highway-6-diner` |
| 11. Vincent Bros. Scrap Yard | 34–35 | `vincent-scrap-yard`; братья Винсент |
| 12. Abattoir Landfill | 35 | `landfill`; `gerald-brewster`; `gerald-polaroids` |
| 13. Miscellaneous Houses (Ridge, Hackett, Steel Road) | 36–38 | `misc-houses`; `ridge-road`, `hackett-road`, `steel-road` (таблицы домов); жители |
| 13b. Surrounding Roads (Red, Dirt, Rattler, Serpent’s, Twister, Miner’s, Ridge, Gully Road) | 39 | `surrounding-roads` и 8 дорог (`eastridge-road` — Ridge Road 13b) |
| The Homestead; 14a–14n; The Homestead Map | 40–52 | `homestead` и 14 мест; карта `homestead-keeper-map`; Кеб, Эйбл, Кутер; таблицы арсенала и Камеры; `children-of-yig-armory`, `spawn-of-yig-well`; сцена `cell-night` |
| The Old Mining Camp; 15a–15e; Map | 53–56 | `mining-camp`, 5 мест; `grady`; карта `mining-camp-map` |
| The Weyland Mines: General Description; 1–10; Mineshaft Map / Map Key | 57–61 | `weyland-mines` (ключ карты) и 10 мест; карты `mining-company-land-map`, `mineshaft-keeper-map` |
| The Serpent Caves 1–16, 15a–15e; Serpent Caves Map | 62–69 | `serpent-caves` и 21 место; карта `serpent-caves-map` |
| Timeline of Events 0–14, 5a–5c (с саундтреками) | 70–74 | 18 сцен хронологии (саундтрек — в описании сцены) |
| Final Thoughts | 74 | сценарий: advice |
| Appendix I – The Hunt (Running the Hunt, Chase Rules Overview, Optional Chase Rules, Harpoon Attack, Non-Lethal Attacks, Driving Stunts, Vehicle Options, ’70s Vehicle Examples) | 75–79 | правила `hunt-running`, `hunt-chase-rules`, `hunt-weapons`, `driving-stunts-and-vehicles`; предметы оружия Охоты; `seth-pickup` |
| T. S. Eliot «The Waste Land» | физ. 80 | атмосфера |
| Appendix II – Environs (The Desert, Rule of Three, Environmental Hazards, Definitions, Desert Conditions, Fumblecrit, Desert Hazard: Wasteland) | 81–86 | правила `rule-of-three`, `environmental-hazards`, `desert-conditions` |
| Appendix III – NPCs (Al’issya, Osteen, Brenner, Seth, The Dustbillies) | 87–91 | персонажи `alissya`, `mordechai-osteen`, `robert-brenner`, `seth`, `dustbillies` |
| Appendix IV – Monsters (Teihiihan, Mutant Rat Swarm, Spawn of Yig, Metallic Beetle Swarm) | 92–95 | существа |
| Appendix V – Other: New Spells (Blinding Flesh, Corruption of the Cannibal) | 96 | правило `new-spells` (кандидаты в `kb/spells/`) |
| New Items: Eye of Yig | 96 | предмет `eye-of-yig` |
| De Vermis Mysteriis | 97 | книга `de-vermis-mysteriis`; предложение в `copies` |
| New Rules: Radioactive Material | 97 | правило `radioactive-material` |
| Appendix VI – Handouts #1–#24 | физ. 98–114 | 20 записей раздатки; #3, #13, #16, #18 — карты Хранителя |
| Полностраничная иллюстрация змеи | физ. 115 | атмосфера |
| NPC Portraits | физ. 116–119 | `images` 16 персонажей |
| Appendix VII – Pre-Gens (Option 1: Dead End; Option 2: Two Detectives) и листы | 120–126 | 6 готовых сыщиков (pregen) |
| Appendix VIII – The ’70s (Playing in the 1970s, News & Pop Culture, Slang, Recommended Films, Cash & Assets) | 127–128 | правило `playing-in-the-1970s` |
| The West News; задняя обложка | физ. 129–130 | атмосфера; сценарий (`sources`) |

## Не взято

- Ссылка на магазин Etsy («Idol of Yig», Cryptorium, с. 63) — реклама; упомянута в `quality.notes` идола.
- Пожилой служащий ратуши (без имени, с. 26) — только в описании места, отдельной записи нет (роли в сюжете нет).
- Мелкие рукописные цифры глубин/уклонов на карте штолен и знаки «W» на карте Усадьбы — без отдельных меток (описано в `quality.notes` карт); легенда «Chase Locations» раздатки 3 — без метки.
- Упомянутые мимоходом люди без записей: Уоллес Маккаллен (фото в банке), Хелен Келли, мистер Уэйленд, Уильям Кэлхун, Джон Левинсон, Гарольд Маккиннон (их улики — предметы/строки таблиц), Мэриан Келли (автор дневника во врезке), Т. Скотт-младший, Маргарет и дети Скотта, Эбигейл и Лиза Смит, Барбара Бейнс.
- Иллюстрации-атмосфера (32 страницы) — `atmosphere.json`; рамки-врезки (688 px) — не картинки.

## Опечатки и расхождения книги (в `errata`)

- «Bob’s Barber Shop» в ключе карты (с. 17) — в тексте «Tom’s Barber Shop» (`toms-barber-shop`).
- Peter Sutton (с. 26) / Matthew Sutton (с. 38) — один уполномоченный по зонированию (`matthew-sutton`).
- Обвал в шахте: 1955 (кладбище, с. 33) против 1954 (с. 54–55) (`cemetery`).
- Основание Мидиана 1836 (с. 10) против 1832 (с. 32) (`blood-of-the-lamb-church`).
- «Sally threw him out» — жена пастора Маргарет (`billy-scott`).
- Брайан Уэстбрук записан в двух домах; Гарри Келли — и в квартире над аптекой, и на Ридж-роуд, 8 (`ridge-road`).
- Затопленные туннели: «orange» в тексте места 9 против синих линий ключа (`mines-second-mine-entrance`).
- Длина троса гарпуна 80 / 50 футов (`harpoon-bow`); «morphine» в правилах героина (`heroin`); два разных правила амфетаминов (`amphetamines`).
- «Investigation» в таблице трейлеров (строка 18); нет определения «Incapacitated» (`environmental-hazards`).
- Статблоки: ПЗ Аль’иссы 20 (по формуле 11) и «Curse of the Cannibal»; Скорость Остина 8 (7); Сет — Комплекция 1 при БкУ +1d6, Скорость 9 (7), ТЕЛ 85 при броске (3d6+2)×5; ПМ тейхиихан 0; БкУ крыс 0 при Комплекции −1; Дети Йига — ПЗ 8 (6), БкУ/Комплекция; пленницы — 6 ПЗ (7).
- Ссылки «см. с.» в списке домов сдвинуты на 2 страницы (пометка в `ridge-road`).

## Термины книги (English → русский)

| English | Русский |
|---|---|
| The Highway of Blood / Red Road | «Шоссе крови» / Ред-роуд |
| Abattoir (Midian) | Абаттуар (Мидиан) |
| The Devil’s Backbone | Хребет Дьявола |
| dustbilly / dustbillies | дастбилли (несклоняемое) |
| Teihiihan | тейхиихан (несклоняемое) |
| Al’issya Ss’rissi A’na | Аль’исса Сс’рисси А’на |
| Tylarissh / Rev. Mordechai Osteen | Тиларисш / преподобный Мордехай Остин |
| The Hunt | Охота |
| The Homestead (The Compound) | Усадьба (Компаунд) |
| The Red House / Breeding House / The Cell / Slaughter House / Sacrificial Preparation / Tower of Sacrifice | Красный дом / Дом размножения / Камера / Бойня / Подготовка жертв / Башня жертвоприношений |
| breeding stock | «племенной скот»; пленницы Красного дома |
| Serpent People | змеелюди (змеечеловек) |
| Spawn of Yig / Children of Yig | Порождение Йига / Дети Йига |
| Eye of Yig / Idol of Yig | Око Йига / Идол Йига |
| Elder Sign | Знак Старших богов |
| Sand-Dwellers | обитатели песков |
| Cthonians | хтонийцы |
| Metallic Beetle Swarm / Mutant Rat Swarm | Рой металлических жуков / Стая крыс-мутантов |
| Blinding Flesh / Corruption of the Cannibal | Слепящая плоть / Порча людоеда |
| Forbidden Lands | Запретные земли |
| Weyland Mining Company / Weyland Estates | горнодобывающая компания «Уэйленд» / «Уэйленд-Эстейтс» |
| The Last Stop Bar & Beds | бар и мотель «Последняя остановка» |
| Thunderbird Gifts | сувениры «Громовая птица» |
| Blood of the Lamb Pentecostal Church | пятидесятническая церковь «Кровь Агнца» |
| Best Foot Forward: Shoes & Repairs | обувь и ремонт «Твёрдый шаг» |
| Righteous Fury | «Праведная ярость» |
| mooks | «статисты» |
| Movement Action | действие перемещения |
| Hazard / Sudden Hazard | опасность / случайная опасность |
| Bootlegger Turn / Drifting / Kick-Up Gravel / Slamming the Brakes | полицейский разворот / дрифт / гравийный шлейф / резкое торможение |
| Muscle Car / Dustbilly Car / Luxury Car | маслкар / машина дастбилли / люксовый автомобиль |
| Harpoon Bow / Beanbag Gun / Restraining Pole / Sap / Syringes | гарпунный самострел / ружьё «бинбэг» / шест-петля / кожаная дубинка («сап») / шприцы со снотворным |
| Knock-Out Blows | нокаут (общее правило) |
| Rule of Three | Правило трёх |
| Exhaustion | изнеможение (6 уровней) |
| Even the Odds | «чёт-нечет» |
| Fumblecrit | провалы и криты |
| Flavor / Pressure / If-Then / Changes | атмосфера / давление / если — то / перемены |
| Heat Exhaustion / Heat Stroke / High Sun / Hot Metal | тепловое истощение / тепловой удар / полуденное солнце / раскалённый металл |
| Despair / Hallucinations / Pain (Major, Severe, Extreme, Crippling) | отчаяние / галлюцинации / боль (сильная, тяжёлая, крайняя, невыносимая) |
| Speed / Acid | «спиды» (амфетамины) / «кислота» (ЛСД) |
| Fumble | критический провал |
