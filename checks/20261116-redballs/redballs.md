# Hudson & Brand: Eyes Like Red Balls of Flame — перенос в базу (Р-251)

Книга `eyes-like-red-balls-en` (Stygian Fox, 2019, Glynn Owen Barrass, «Cthulhu by Gaslight»), 16 страниц PDF.
Печатная страница = физической (offset 0): «3» на физ. 3, «5» на физ. 5, «14» на физ. 14 — сверено по изображениям;
без номеров — физ. 1 (обложка), 2 (выходные данные), 15 (задняя обложка), 16 (пустая).

Записи: `kb/books/eyes-like-red-balls-en/` — 47 записей (сценарий 1, сцены 6, персонажи 19, организации 2,
предметы 2, раздатки 5, места 11, карта 1). Карта — `app/maps/redballs-hampstead-heath.jpg`; картинки —
`app/art/{handouts,characters}/redballs-*.webp` (12, сопоставление `art.json`, применено).
Правки общей записи `coc:location:london` — `proposals.json` (7 предложений). Атмосфера — `atmosphere.json`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Eyes Like Red Balls of Flame» | 1 (без номера) | сценарий `eyes-like-red-balls-of-flame` (sources); картинка — `atmosphere.json` |
| Выходные данные (©2019 Stygian Fox) | 2 (без номера) | сценарий (sources); гравюра — `atmosphere.json` |
| Авторы (Written by … Cartography by …) | 3 | сценарий (summary, sources) |
| Introduction and Background (боковой заголовок) | 4 | сценарий |
| Introduction | 4 | сценарий, `keeper_info` («Введение») |
| Scenario Background | 4 | сценарий, `keeper_info` («Предыстория», «Тайна»); `organization/phantom-club`; `character/spring-heeled-jack` |
| The Meeting at the Phantom Club | 4, 6 | сцена `scene/phantom-club-meeting`; место `location/manwaring-house` |
| Eyes Like Red Balls of Flame Papers #1 | 5 | раздатка `handout/papers-1-manwaring-letter` |
| Research and the Hunt (боковой заголовок) | 6 | сцены `research`, `the-hunt` |
| Research | 6 | сцена `scene/research`; место `location/hudson-and-brand-office` (Газетная справочная) |
| The Hunt | 6 | сцена `scene/the-hunt`; места `location/willoughby-road`, `location/hampstead`; персонажи `peterson`, `decoys`, `patrol-constable`, `ronald-hooker`, `william-parlow` |
| Eyes Like Red Balls of Flame Papers #3 | 6 | раздатка `handout/papers-3-mysterious-disappearance` |
| Eyes Like Red Balls of Flame Papers #2a | 7 | раздатка `handout/papers-2-jack-case` (лист 2a) |
| The Trap and Hampstead Heath (боковой заголовок) | 8 | сцены `the-trap`, `hampstead-heath-pursuit` |
| Eyes Like Red Balls of Flame Papers #2b | 8 | раздатка `handout/papers-2-jack-case` (лист 2b) |
| Eyes Like Red Balls of Flame Papers #4 | 9 | раздатка `handout/papers-4-dreadful-coach-crash` |
| The Trap (с «Keeper’s Note») | 9 | сцена `scene/the-trap`; место `location/willow-road-pilgrims-lane`; персонаж `maisy` |
| Hampstead Heath (с «Keeper’s Note») | 9 | сцена `scene/hampstead-heath-pursuit`; места `location/hampstead-heath`, `location/wooded-copse`, `location/jacks-trail` |
| The Abandoned Boathouse and Conclusion (боковой заголовок) | 10 | сцена `abandoned-boathouse`, сценарий `conclusion` |
| The Abandoned Boathouse | 10 | сцена `scene/abandoned-boathouse`; место `location/abandoned-boathouse`; предмет `item/jacob-pocket-watch` |
| Eyes Like Red Balls of Flame Papers #5 | 10 | раздатка `handout/papers-5-murder-of-two-persons` |
| Conclusion | 10 | сценарий, `conclusion`; предмет `item/phantom-club-files` |
| Карта «Hampstead Heath & Parliament Hill» (метки The Trap, Wooded Copse, Jack’s Trail, The Boathouse, Hampstead Heath Station; легенда) | 11 | карта `map/hampstead-heath` (7 меток); легенда — в `location/hampstead-heath` |
| Sanity Awards, Scenario Seeds and NPCs (боковой заголовок) | 12 | сценарий |
| Sanity Rewards | 12 | сценарий, `conclusion` («Награды Рассудка») |
| Scenario Seeds | 12 | сценарий, `conclusion` («Что дальше») и таблица «Зацепки для новых сценариев» |
| The Ravenscar Terror | 12 | таблица «Зацепки для новых сценариев», строка «Ужас Рейвенскара» |
| The Witches of Pendle Hill | 12 | там же, «Ведьмы Пендл-Хилла» |
| Ghouls of the Necropolis | 12 | там же, «Упыри Некрополя» |
| The Highgate Mystery | 12 | там же, «Тайна Хайгейта» |
| The River Witch | 12 | там же, «Речная ведьма» |
| The Croglin Vampire | 12 | там же, «Кроглинский вампир» |
| Dramatis Personae | 13 | персонажи ниже |
| Donald Manwaring - Dilettante | 13 | `character/donald-manwaring` (статблок, портрет) |
| Raghubir - Butler | 13 | `character/raghubir` (статблок, портрет) |
| Charles Godfrey - Doctor | 13 | `character/charles-godfrey` (статблок, портрет) |
| William Hodges - Accountant (Phobias: Haemaphobia) | 13 | `character/william-hodges` (статблок, портрет, способность «Гемофобия») |
| NPCs (боковой заголовок) | 14 | персонажи ниже |
| Peterson - Thug | 14 | `character/peterson` (статблок, портрет) |
| Spring-Heeled Jack - Monster | 14 | `character/spring-heeled-jack` (статблок, способности, картинка) |
| Задняя обложка (аннотация) | 15 (без номера) | `atmosphere.json`; аннотация — не взято |
| Пустая страница | 16 | — |

Упомянутые в тексте персонажи без статблоков — тоже записи: `mary-manwaring`, `sophia-manwaring`, `edwin-manwaring`,
`robert-manwaring`, `bernard-waters`, `hunter-dunn`, `finnegan`, `gargery`. Организации: `phantom-club`, `hudson-and-brand`.
Места: `harrow-on-the-hill`, `hampstead`, `hampstead-heath-station` (только метка карты), все `part_of` общий `coc:location:london`.

## Не взято

- Аннотация задней обложки (с. 15) — рекламный текст, пересказывает завязку; картинка — `atmosphere.json`.
- Обрывки соседних колонок газет в раздатках 3, 4, 5 (конец письма «A Detester of Barbarianism», «Egypt», «Irish Affairs — the Land League
  Convention», «This Day’s Police — Serious Charge of Fraud», заметка о царе и императоре Австрии, объявления) — декорация раздаток, к сценарию
  не относятся; видны на картинках раздаток.
- Таблица «Sinister Portents» — в книге её нет, только ссылка на «The Spirits of London», с. 12 (книги в базе нет); ссылка оставлена текстом в сцене «Охота».
- Исторические лица из раздаток 2a–2b и 3 (Мэри Стивенс, сэр Джон Коуэн, Джейн Олсоп, инспекторы Пенни и Дженкинс), преподобный Кэннон и Пег
  Паулер из зацепок, Холлоуэйская лечебница, контора Хаттон-Гарден — только текстом (упомянуты мимоходом, Р-42).
- Надписи исторической основы карты (Parliament Hill, Ken Wood, Highgate, North End, South End, Vale of Health и др.) — в тексте сценария не
  встречаются, меток и записей нет; метки есть у пяти надписей сценария и у «HAMPSTEAD HEATH», «HAMPSTEAD».
- Оформление страниц (газетные фоны, рамки заголовков, логотипы, силуэт Джека на с. 14) — `atmosphere.json`.
- Оружие эпохи «Газового света» (.450 Webley MP, .380 Webley No.2, .455 Webley WG Revolver) — записей в справочнике оружия нет; атаки
  без ссылки `weapon` (кандидаты в справочник, помощник справочник не правит).
- Навык «Journalism» (сцена «Изыскания») и «Unnerving Giggle 100%» (Джек) — записей навыков нет, оставлены текстом (Р-126).

## Опечатки и сомнения

| Где | Напечатано | Что в базе |
|---|---|---|
| Дональд Мэнуоринг, с. 13 | «Fighting (Brawl) 25% (12/54)» | исправлено на 25% (12/5), `errata.fixed: true` |
| Дональд Мэнуоринг, с. 4 / 13 | волосы рыжие (с. 4) / тёмные (с. 13) | оба варианта в описании, `errata` |
| Уильям Ходжес, с. 13 | HP 13 (по ВЫН 45 и ТЕЛ 70 — 11) | как напечатано, `errata` |
| Уильям Ходжес, с. 4 / 13 | высокий (с. 4) / среднего роста (с. 13) | оба варианта, `errata` |
| Петерсон, с. 14 | Move 6 (база 7, с возрастом 54 — 5) | как напечатано, `errata` |
| Петерсон, с. 14 | «Dodge 20 (10/4)» без % | как напечатано (`raw`), мелочь |
| Джек-Прыгун, с. 14 | Magic Points 120 (МОЩ/5 = 24) | как напечатано, `errata` (возможно, задумано: прыжок стоит 5 ПМ) |
| Джек-Прыгун, с. 14 | HP 23 (по ВЫН 80 и ТЕЛ 100 — 18) | как напечатано, `errata` |
| Джек-Прыгун, с. 14 | «Sanity Loss: 1D6» — одно значение | `sanity_loss`: успех «—», провал 1d6 |
| Сцена «Заседание», с. 4 | «Psychology role» | опечатка в слове, при переводе исчезла (Р-39) |
| Раздатка 2a, с. 7 | «brouhht», забитые машинописью буквы «XXXX» | как напечатано в `text.en`, в переводе опущено |
| Боковой заголовок, с. 12 | «Sanity Awards», а раздел — «Sanity Rewards» | мелочь |

## Термины (English → Russian)

| English | Русский |
|---|---|
| Hudson & Brand: Eyes Like Red Balls of Flame | Хадсон и Брэнд: Глаза как красные огненные шары |
| Hudson & Brand (agency) | «Хадсон и Брэнд» |
| Hudson & Brand: Inquiry Agents of the Obscure | (название книги не переводится) |
| Cthulhu by Gaslight / Gaslight | «Газовый свет» |
| The Phantom Club | Призрачный клуб |
| Spring-Heeled Jack | Джек-Прыгун |
| Jacob Freely Manwaring | Джейкоб Фрили Мэнуоринг |
| Donald Manwaring | Дональд Мэнуоринг |
| Mary Manwaring | Мэри Мэнуоринг |
| Sophia Manwaring | София Мэнуоринг |
| Edwin / Robert Manwaring | Эдвин / Роберт Мэнуоринг |
| Raghubir | Рагхубир |
| Charles Godfrey | Чарльз Годфри |
| William Hodges | Уильям Ходжес |
| Peterson | Петерсон |
| Bernard Waters | Бернард Уотерс |
| Hunter Dunn | Хантер Данн |
| Finnegan / Gargery | Финнеган / Гарджери |
| Maisy | Мейзи |
| decoys | приманки (запись «Приманки клуба») |
| policeman on patrol | патрульный полицейский (имя придумано: констебль Альберт Джадд) |
| Superintendent Ronald Hooker | суперинтендант Рональд Хукер |
| Sergeant William Parlow | сержант Уильям Парлоу |
| Mary Stevens / Jane Alsop / Sir John Cowan | Мэри Стивенс / Джейн Олсоп / сэр Джон Коуэн |
| Inspector Penny / Inspector Jenkins | инспектор Пенни / инспектор Дженкинс |
| Harrow on the Hill | Харроу-он-те-Хилл |
| High Street / Waldron Road | Хай-стрит / Уолдрон-роуд |
| Hampstead / Hampstead Heath | Хэмпстед / Хэмпстед-Хит |
| Willoughby Road | Уиллоуби-роуд |
| Willow Road / Pilgrim’s Lane | Уиллоу-роуд / Пилгримс-лейн |
| The Trap | Ловушка |
| Wooded Copse | Лесистая роща |
| Jack’s Trail | След Джека |
| The (Abandoned) Boathouse | (Заброшенный) лодочный сарай |
| Hampstead Heath Station | станция «Хэмпстед-Хит» |
| Parliament Hill / Ken Wood Estate | Парламент-Хилл / поместье Кенвуд |
| 33 Golden Square | Голден-сквер, 33 |
| Newspaper Reference | Газетная справочная |
| Holloway Asylum | Холлоуэйская лечебница |
| Hatton Garden Office | контора Хаттон-Гарден |
| High Green Ghost | Призрак Хай-Грин |
| The Jack Case | «Дело Джека» |
| Eyes Like Red Balls of Flame Papers #N | Раздатка N |
| Mysterious Disappearance of a Gentleman | «Таинственное исчезновение джентльмена» |
| Dreadful Coach Crash / Two Children Dead | «Ужасное крушение кареты» / «Двое детей погибли» |
| Murder of Two Persons | «Убийство двух человек» |
| Sinister Portents (The Spirits of London) | «Зловещие предзнаменования» |
| Populating London | (название раздела не переводится) |
| Scenario Seeds | Зацепки для новых сценариев |
| The Ravenscar Terror | «Ужас Рейвенскара» |
| The Witches of Pendle Hill | «Ведьмы Пендл-Хилла» |
| Ghouls of the Necropolis | «Упыри Некрополя» |
| Gorbals Vampire | Горбалсский вампир |
| The Highgate Mystery | «Тайна Хайгейта» |
| The River Witch / Peg Powler | «Речная ведьма» / Пег Паулер |
| Peg Powler’s suds / cream | «мыльная пена Пег Паулер» / «сливки Пег Паулер» |
| The Croglin Vampire / Croglin Grange | «Кроглинский вампир» / Кроглин-Грейндж |
| Reverend Cannon | преподобный Кэннон |
| Roman Signal Station | римская сигнальная станция |
| Dilettante / Doctor / Accountant / Butler / Thug / Monster | дилетант / врач / бухгалтер / дворецкий / головорез / чудовище |
| Art/Craft (Butlering) | Искусство/ремесло (служба дворецкого) |
| Journalism (skill) | Журналистика |
| Unnerving Giggle | Жуткое хихиканье |
| Haemaphobia | гемофобия |
| Kukri | кукри |
| .450 Webley MP Revolver | револьвер «Вебли» MP .450 |
| .380 Webley No.2 Revolver | револьвер «Вебли» No. 2 .380 |
| .455 Webley WG Revolver | револьвер «Вебли» WG .455 |
| hardy flesh | крепкая плоть |
| oilskin | промасленная ткань |
| skullcap | металлическая шапочка |
| hibernate | впадать в спячку |

## Проверки

- `python -B tools/check.py kb/books/eyes-like-red-balls-en` — ошибок 0, предупреждений 0.
- `tools/completeness.py` (`completeness/`): `text.gap` 0; 6 находок картинок — оформление и обложки (с. 1, 2, 3, 4, 12, 15), все в `atmosphere.json`.
- `tools/scenario_check.py` (`scenario/`): 1 находка low — у сцены «Изыскания» нет участников: в книге там только сыщики (библиотеки и редакции газет).
