# A Lark in a Cage — перенос в базу (Р-251)

Книга `lark-in-a-cage-en` — Noah Lloyd, «A Lark in a Cage» (Reckoning of the Dead, Miskatonic Repository, ©2019), «Зов Ктулху» 7e, эпоха «Газового света»: Лондон, май 1895 года (`axes.era` `gaslight`). В конце книги — бонус: одностраничный сценарий «Bulwark of the Hudson» (декабрь 1889 года, Нью-Йорк) — отдельная запись `scenario/bulwark-of-the-hudson`.
Записи — `kb/books/lark-in-a-cage-en/` (113 записей), карты — `app/maps/lark-*.jpg` (5), картинки — `app/art/*/lark-*.webp` (13).

Страницы: PDF 58 страниц; «2» напечатана на физ. 4 → **печатная = физическая − 2, `offset: -2`**. Проверено по картинкам и тексту: физ. 4 («2»), физ. 12 («10»), физ. 31 («29»), физ. 51 («49»). Без номеров: обложка, выходные данные, оглавление (физ. 1–3) и бонусные страницы в конце (физ. 52–58). Карты на физ. 16, 45, 46 номера не печатают; по оглавлению («Appendix 3: Maps of the East End — 43») им даны печатные 14, 43, 44.

Русского перевода сценария в базе нет (поиск по `Foxwell`, `Фоксвел`, `Wegg`, `Вегг`, `Greaves`, `Грейвз`, `Flanagan`, `Фланаган`, `Lark in a Cage`, `Жаворон`, `Greathead`, `St. Matthias`, `Blackwall` в `kb/` — пусто или другие люди). Лондон — общая запись `coc:location:london`; Нью-Йорк — `coc:location:new-york`; упыри — `instance_of` `coc:creature:ghoul`.

## Заголовки книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) | — (физ. 1) | сценарий `scenario/a-lark-in-a-cage` (источник); картинка — атмосфера |
| Credits | — (физ. 2) | сценарий (источник: автор, художник, картограф); остальное — «Не взято» |
| Table of Contents | — (физ. 3) | сценарий (источник) |
| эпиграф «…he howl’d fearfully…» (The Duchess of Malfi) | 2 | `handout/handout-7-a-lark-in-a-cage` (источник) |
| вступление (Лондон 1895, 3–6 игроков, X-Card, «The Art of Madness») | 2 | сценарий: `summary`, `advice` |
| Keeper’s Introduction | 2 | сценарий: `keeper_info` («Две стороны») |
| The Story so Far | 2–3 | сценарий: `keeper_info`; `character/wainwright-tamora-greaves`, `character/peter-wegg`, `character/samantha-gregory` |
| The East End in 1895 | 3 | сценарий: `keeper_info`; `location/east-end`, `location/blackwall` |
| Firearms in the 1890s (врезка) | 3 | сценарий: `keeper_info` |
| Oscar Wilde’s Trial | 3–4 | сценарий: `keeper_info` |
| Transportation | 4 | сценарий: `advice` («Переправы»); `location/east-end` |
| British 19th-Century Currency Conversions (врезка) | 4 | сценарий: `advice` |
| The Greenwich Steam Ferry | 4 | `location/greenwich-steam-ferry`; сценарий: `advice` |
| Hiring a Boat / Hiring a Cab / Riding the Tube | 4 | сценарий: `advice` («Переправы») |
| Dramatis Personae | 4 | персонажи ниже |
| Bartholomew Cartwright, Groundskeeper | 4 | `character/bartholomew-cartwright` |
| James Colbert, Isle of Dogs Police Sergeant | 5 | `character/james-colbert` |
| Raymond Flanagan, Shipping merchant and ghoul experiment | 5 | `character/raymond-flanagan` |
| Dr. Nolan Foxwell, Pediatrician… | 5 | `character/nolan-foxwell` |
| Dr. Wainwright Tamora Greaves, Mad scientist | 5–6 | `character/wainwright-tamora-greaves` |
| Amelia and Philip Gregory, Parents | 6 | `character/amelia-gregory`, `character/philip-gregory` |
| John Mackintosh, Reverend at St. Matthias’ Church | 6 | `character/john-mackintosh` |
| Ernest William Moir, Contracting agent for S. Pearson & Sons | 6 | `character/ernest-william-moir`; `organization/s-pearson-and-sons` |
| Peter Wegg, Ghoulish Hybrid | 7 | `character/peter-wegg` |
| The Porter Family, Down-on-their-luck Londoners | 7 | сценарий: `hook`; прегены (приложение 4) |
| The Transformation | 7 | `item/ghoul-serum` (`mechanics`) |
| Wegg’s Cane (врезка) | 7 | `item/weggs-cane` (с картинкой); `character/peter-wegg` (атака, способность) |
| Table 1: Transformation | 8 | сценарий: `tables` «Таблица 1: Превращение» |
| The Cure | 8 | `item/ghoul-serum` («Лекарство»); `location/blackwall-tunnel-airlock`; сценарий: `advice` |
| Involving the Investigators: The Cuckoo | 9–11 | сцена `scene/the-cuckoo` («Завязка: подкидыш»); `creature/cuckoo-child`; `location/gregory-home`; `item/baptism-certificate` |
| Handout 1: Wilde Times (в главе) | 10 | `handout/handout-1-wilde-times` (источник; картинка — из приложения) |
| Hysteria in the 1890s (врезка) | 11 | сцена `scene/the-cuckoo` |
| If they simply refuse . . . (To take the baby? / To go to the cistern? / To go to the lab?) | 11 | сценарий: `advice` |
| The Crash | 12–13 | сцена `scene/the-crash` |
| Locations | 13 | сцены и места ниже |
| The Home of Doctor Nolan Foxwell | 13–15 | сцена `scene/foxwell-home`; `location/foxwell-home` |
| Homosexuality in the 1890s (врезка) | 13 | сцена `scene/foxwell-home` |
| The East End of London: Keeper’s Map | 14 | `map/east-end-keeper-map` (та же карта, что на с. 43) |
| Foxwell’s Examination of Samantha | 15 | сцена `scene/foxwell-home`; `creature/cuckoo-child` |
| Dr. Foxwell’s Library | 16 | сцена `scene/foxwell-library`; `item/harvey-treatise`; раздатки 3, 4 |
| East Greenwich Gas Works | 16–17 | сцена `scene/gas-works`; `location/east-greenwich-gas-works` |
| Isle of Dogs Police Station | 17–18 | сцена `scene/police-station`; `location/isle-of-dogs-police-station` (с фотографией); `item/foxwell-calling-card` |
| The Mortuary | 18–19 | сцена `scene/mortuary` («В морге участка»); `location/police-mortuary`; `item/church-programs`, `item/grave-mold` |
| St. Matthias’ Church | 19 | сцена `scene/st-matthias-church`; `location/st-matthias-church` |
| Interrogating Cartwright | 20 | сцена `scene/interrogating-cartwright` |
| The Catacombs Beneath St. Matthias | 20–21 | сцена `scene/catacombs`; `location/st-matthias-catacombs` |
| Underground London (врезка) | 21 | `location/st-matthias-catacombs` (`history`) |
| The Cistern | 21 | сцена `scene/cistern`; `location/st-matthias-cistern`; `creature/st-matthias-ghouls` |
| Treating with the Ghouls | 21–23 | сцена `scene/treating-with-the-ghouls`; `creature/elder-ghoul`; `organization/st-matthias-warren` |
| Total Party Kill (врезка) | 22 | сцена `scene/treating-with-the-ghouls` |
| Hunting the Ghouls (врезка) | 23 | `location/highgate-cemetery` (`history`); сцена `scene/treating-with-the-ghouls`; сценарий: `advice` |
| The London Sewer | 23–24 | сцена `scene/london-sewer` («Блуждания по канализации»); `location/london-sewer` |
| Wegg’s Home in the Sewers (врезка) | 23 | сцена `scene/wegg-in-the-sewers` |
| Table 2: The Sewers of London (1. Tosher … 6. Branching Tunnel) | 24 | `location/london-sewer`: `tables` «Таблица 2: канализация Лондона» (в сценарии — ссылка `from`, Р-136); `character/flake-no-foot` |
| The Home of Wainwright Tamora Greaves | 24–27 | сцена `scene/greaves-home`; `location/greaves-home` |
| Ground Floor | 25–26 | `location/greaves-home-ground-floor`; `item/pearson-shares`; раздатка 5 |
| (план «The Home of Dr. W. T. Greaves») | 26 | `map/greaves-home-plan` |
| First Floor | 26 | `location/greaves-home-first-floor`; `item/greenwich-railway-tickets` |
| Second Floor | 26 | `location/greaves-home-second-floor`; `item/greaves-wegg-photograph` |
| Discovering Peter with the Porters (врезка) | 26 | сцена `scene/greaves-home`; `item/greaves-wegg-photograph`; `character/henrietta-porter` |
| Basement | 27 | `location/greaves-home-basement`, `location/greaves-tunnels`; сцена `scene/greaves-home` |
| Blackwall Tunnel Construction Site | 27–28 | сцена `scene/tunnel-construction-site`; `location/blackwall-tunnel-site`; `item/greathead-shield` |
| Handout 5: Hudson River Tunnel (в главе) | 27 | `handout/handout-5-hudson-river-tunnel` (источник; картинка — из приложения) |
| The Airlock | 28 | `location/blackwall-tunnel-airlock`; сцена `scene/tunnel-construction-site` |
| Greaves’ Underwater Laboratory / Entering the Laboratory | 28–29 | сцена `scene/underwater-laboratory`; `location/greaves-underwater-laboratory` |
| (разрез «Greaves’ Underwater Laboratory») | 28 | `map/greaves-laboratory-plan` |
| (разрез «Greaves’ Moon Pool & Laboratory») | 29 | `map/greaves-moon-pool` |
| The Lab Itself | 29–31 | сцена `scene/underwater-laboratory`; `location/greaves-submersible` |
| The Duchess of Malfi (врезка) | 30 | сцена `scene/underwater-laboratory`; `handout/handout-7-a-lark-in-a-cage` |
| Mythos Tome: The Diary of Wainwright Tamora Greaves | 31 | `tome/diary-of-wainwright-tamora-greaves` |
| Running the Finale | 31 | сцена `scene/running-the-finale` («Финал: у шлюза») |
| Reaching the airlock | 31–32 | сцена `scene/running-the-finale` |
| Saving Samantha | 32 | сцена `scene/saving-samantha` |
| Failing to Save Samantha | 32 | сцена `scene/failing-to-save-samantha` |
| Investigator Rewards | 33 | сценарий: `conclusion` |
| Appendix 1: Non-Player Characters | 33–37 | статблоки в записях персонажей и существ |
| James Colbert, 37 | 33 | `character/james-colbert` |
| Raymond Flanagan, 46 | 33 | `character/raymond-flanagan` |
| Dr. Nolan Foxwell, 43 | 34 | `character/nolan-foxwell` |
| Elder Ghoul, 250, Leader of the St. Matthias Warren | 34 | `creature/elder-ghoul` |
| Ghouls | 34–35 | `creature/st-matthias-ghouls` |
| Dr. Wainwright Tamora Greaves, 80 | 35 | `character/wainwright-tamora-greaves` |
| Amelia Gregory, 22 | 35 | `character/amelia-gregory` |
| Philip Gregory, 29 | 36 | `character/philip-gregory` |
| Ernest William Moir, 32 | 36 | `character/ernest-william-moir` |
| Flake No-foot, 39, Tosher | 36–37 | `character/flake-no-foot` |
| Peter Wegg, 64, Ghoulish hybrid | 37 | `character/peter-wegg` |
| Appendix 2: Handouts | 38 | раздатки ниже |
| Handout 1: Wilde Times | 38 | `handout/handout-1-wilde-times` (текст и таблица приливов; картинка) |
| Handout 2: Flanagan | 39 | `handout/handout-2-flanagan` (фотография; она же портрет `character/raymond-flanagan`) |
| Handout 3: A Study on the Effects of Degenerative Caisson’s Sickness in Corpses | 39 | `handout/handout-3-caisson-study` |
| Handout 4: Pamphlet on New World Cannibalism | 40 | `handout/handout-4-new-world-cannibalism` |
| Handout 5: Hudson River Tunnel | 40 | `handout/handout-5-hudson-river-tunnel` |
| Handout 6: Mythos Tome: The Diary of Wainwright Tamora Greaves | 41 | `handout/handout-6-greaves-diary`; картинка и у `tome/diary-of-wainwright-tamora-greaves` |
| Handout 7: A Lark in a Cage | 42 | `handout/handout-7-a-lark-in-a-cage` |
| Appendix 3: Maps of the East End — Keeper’s Map | 43 | `map/east-end-keeper-map` (ключ 1–8 → места; подписи районов и виньетки — метки) |
| Player’s Map | 44 | `map/east-end-player-map` (ключ A–H; `location/commercial-docks`, `location/deptford-creek`, `location/west-india-docks`, `location/east-india-docks` заведены по меткам) |
| Appendix 4: Pre-generated Investigators | 45 | сценарий: `hook`, `advice` (важность при неполной группе) |
| Sampson Porter, age 48, Former police sergeant | 45 | `character/sampson-porter` |
| Henrietta Porter, age 53, Mother and wife | 46 | `character/henrietta-porter` |
| Louisa Cahill, age 29, Nurse | 46–47 | `character/louisa-cahill` |
| Saul Cahill, age 35, Shipping accountant | 47–48 | `character/saul-cahill` |
| Regina Porter, age 21, Social activist | 48 | `character/regina-porter` |
| George MacKenzie, age 25, Solicitor | 49 | `character/george-mackenzie` |
| «Bulwark of the Hudson» — вступление автора | — (физ. 52) | `scenario/bulwark-of-the-hudson` (`summary`) |
| Reckoning of the Dead Gazette, December 1889: Bulwark of the Hudson | — (физ. 53) | `scenario/bulwark-of-the-hudson` (`keeper_info`); `location/hudson-river-tunnel` (с рисунком) |
| The Caisson | — (физ. 53) | сцена `scene/bulwark-the-caisson`; `character/thom-mckenzie`, `character/jef-acorn` |
| Something Beneath the River | — (физ. 53) | сцена `scene/bulwark-something-beneath-the-river` |
| The Foulness of Dead Cities (DEX 0, POW 150, HP 150) | — (физ. 53) | `creature/foulness-of-dead-cities` |
| Reckoning of the Dead Character Sheet ×4 | — (физ. 54) | `character/ernest-william-moir` (вариант статблока 1889), `character/james-henry-greathead`, `character/michael-calvert`, `character/philip-barlow` |
| Deck of Emanations (8 карт) | — (физ. 55) | `handout/bulwark-deck-of-emanations` (текст всех карт; картинка) |
| (титульная страница) | — (физ. 56) | атмосфера |
| реклама Into the Darkness | — (физ. 57) | «Не взято»; картинка — атмосфера |
| (задняя обложка, аннотация) | — (физ. 58) | сценарий (источник); картинка — атмосфера |

## Не взято

- Credits (с. физ. 2): список тестировщиков, благодарности спонсорам Patreon, адрес сайта, юридические строки о товарных знаках — не материал для игры. Автор и художники — в `summary` и источниках сценария.
- Реклама подкаста Into the Darkness (физ. 57) — не материал для игры (картинка — в `atmosphere.json`).
- Ссылка на X-Card (tinyurl) — только упомянута в `advice`, без адреса.
- Размерные подписи плана дома Грейвза (25′, 48′6″) и масштабные линейки карт («1 English Statute Mile», «10 Feet») — не метки мест; размеры комнат перенесены в подписи меток (в метрах), исходные — в `quality.notes` карты.
- Персонажи без записей (упомянуты мимоходом, остались текстом): Оскар Уайльд, Альфред Тейлор, судья Уиллс, лорд Дуглас, маркиз Куинсберри; Маргарет Брюс Пеннику (жена Мойра); Майкл Маккензи (отец Джорджа); Аделина Вирджиния Стивен (Вирджиния Вулф); доктор Юфратес Демиболд (шуточная реклама); санитар и дежурный участка; кучер «Виктории»; рабочий-накопитель из «Оплота Гудзона».
- Слово «picture» в тексте «Оплота Гудзона» после «Greathead Tunneling Shield» — остаток вёрстки (Р-39).
- Картинки-атмосфера (обложка, череп, баннер «Dissection Tables», рамки листов сыщиков, титул, задняя обложка, вступление «Оплота», копии раздаток 1 и 5 и карты Хранителя в тексте глав) — `checks/20261116-lark/atmosphere.json`.

## Опечатки и сомнения книги

| Запись | Что напечатано | Как в базе |
|---|---|---|
| `character/peter-wegg` | Dodge 45% (17/7) — доли от 35% (= ЛВК/2) | 45% (22/9), исправлено по Р-77, `errata` |
| `character/peter-wegg` | HP 20 при ВЫН 70 и ТЕЛ 75 (ожидалось 14) | как напечатано, `errata` (возможно, задумано) |
| `character/flake-no-foot` | MP 12 при МОЩ 50; Move 8 при СИЛ и ЛВК > ТЕЛ | как напечатано, `errata` |
| `character/ernest-william-moir` | Move 8 при СИЛ 70 и ЛВК 60 > ТЕЛ 50 (возраст 32) | как напечатано, `errata` |
| `character/louisa-cahill` | «DB:» пусто | 0 по СИЛ и ТЕЛ (Р-41), `errata` + `corrections` |
| `character/raymond-flanagan` | возраст 46 против «in his fifties» на фотографии | 46, `errata` |
| листы «Оплота Гудзона» | половина от 35 везде «18»; Калверт: Spot Hidden 50 (25/25), Library Use 40 (20/40) и ещё раз Library Use 35; Барлоу: Climb 40 (20/40) | доли исправлены (Р-35), `errata`; оба «Library Use» оставлены |
| `scene/treating-with-the-ghouls`, `scene/london-sewer` | «(page XX)» — три незаполненные ссылки на страницы (с. 23) | ссылки на записи, `errata` |
| `location/greaves-home` | «lives on the Isle of Dogs» против карты (2 — Блэкуолл), адреса «55 Blair Street, Poplar» и «his home in Blackwall» | Блэкуолл, `errata` |
| `location/east-end` | Дептфорд «just east of Greenwich» (на деле и на картах книги — западнее) | переведено как напечатано, `errata` |
| `organization/s-pearson-and-sons` | газета: «the American company»; текст: «the British construction firm» | британская, `errata` |
| `scenario/bulwark-of-the-hudson` | «Bulwark of the Hudson» / «Bulwark on the Hudson» | первое — название, второе — в `aliases`, `errata` |
| `handout/handout-6-greaves-diary` | последняя фраза короче, чем в тексте сценария (с. 31) | пометка в `quality.notes` |
| Скорость без возрастной поправки (Фоксвелл 43, Грейвз 80, Вегг 64) | приём книги (Р-161) | как напечатано, пометка |

## Термины книги (English → русский)

| English | Русский |
|---|---|
| A Lark in a Cage | Жаворонок в клетке |
| Bulwark of the Hudson | Оплот Гудзона |
| the Cuckoo / cuckoo child | подкидыш |
| ghoul-child | детёныш упыря |
| ghoul warren / St. Matthias Warren | логово упырей Святого Матфия |
| Elder Ghoul | старейшина упырей |
| ghoulish hybrid | полуупырь |
| Greaves’ serum / ghoul serum | сыворотка Грейвза / сыворотка упырей |
| The Transformation | превращение |
| The Cure | лекарство |
| caisson’s sickness / caisson’s disease / the bends | кессонная болезнь / «бенды» |
| airlock | шлюз |
| moon pool | лунный колодец |
| submersible / diving bell | подводный аппарат / водолазный колокол |
| Greathead Shield | щит Грейтхеда |
| tosher (sewer hunter) | тошер («охотник в канализации») |
| sluice | шлюзовой затвор |
| Victoria (cab) | «виктория» |
| hansom cab | кэб-хэнсом |
| hysteria | истерия |
| Deck of Emanations | колода эманаций |
| The Foulness of Dead Cities | Скверна мёртвых городов |
| the morass | морасс |
| propeller accidents | несчастные случаи с гребными винтами |
| London Daily News | «Лондон дейли ньюс» |
| S. Pearson & Sons | «С. Пирсон и сыновья» |
| Isle of Dogs / Island (River) Police | Собачий остров / островная (речная) полиция |
| Deptford / Greenwich / Greenwich Peninsula | Дептфорд / Гринвич / Гринвичский полуостров |
| Blackwall / Poplar | Блэкуолл / Поплар |
| Canary Wharf | Канэри-Уорф |
| East / West India Docks / Commercial Docks / Deptford Creek | Ост-Индские / Вест-Индские / Коммерческие доки / Дептфорд-Крик |
| East Greenwich Gas Works | Восточно-Гринвичский газовый завод |
| Blackwall Tunnel Construction Site | строительство Блэкуоллского тоннеля |
| Hudson River Tunnel | Гудзонский тоннель |
| St. Matthias’ Church (Poplar Chapel) | церковь Святого Матфия (Попларская часовня) |
| The Cistern / The Catacombs | цистерна / катакомбы |
| Highgate Cemetery | Хайгейтское кладбище |
| Greenwich Steam Ferry | Гринвичский паровой паром |
| Black Ditch | «Блэк-Дитч» |
| Drive Carriage | Управление экипажем |
| Drinking with the Boys | Выпивка с приятелями |
| Architecture (skill) | Архитектура |
| Group Luck roll | групповая проверка Удачи |
| Bonus / Penalty die | бонусная / штрафная кость |
| Hard / Extreme roll | трудная / чрезвычайная проверка |
| Mythos Rating | Значение Мифов |

Имена: Wainwright Tamora Greaves — Уэйнрайт Тамора Грейвз; Peter Wegg — Питер Вегг; Nolan Foxwell — Нолан Фоксвелл; Raymond Flanagan — Рэймонд Фланаган; Amelia / Philip / Samantha Gregory — Амелия / Филип / Саманта Грегори; Bartholomew Cartwright — Бартоломью Картрайт; John Mackintosh — Джон Макинтош; James Colbert — Джеймс Колберт; Elias Cross — Элайас Кросс; Ernest William Moir — Эрнест Уильям Мойр; Flake No-foot — Флейк Ноуфут; Sampson / Henrietta / Regina Porter — Сэмпсон / Генриетта / Реджина Портер; Louisa / Saul Cahill — Луиза / Сол Кэхилл; George MacKenzie — Джордж Маккензи; James Henry Greathead — Джеймс Генри Грейтхед; Michael Calvert — Майкл Калверт; Philip Barlow — Филип Барлоу; Thom McKenzie — Том Маккензи; Jef Acorn — Джеф Эйкорн.

## Кандидаты в общие записи и вопросы

- Навык «Drive Carriage» (эпоха «Газового света») — общей записи нет; у прегенов Сэмпсона и Джорджа он текстом без ссылки. Кандидат в `kb/skills/` (наша форма — «Управление экипажем»).
- Навык «Architecture» (Мойр) — общей записи нет; текстом.
- Предложений правок чужих записей нет (`proposals-lark.json` не создавался).
