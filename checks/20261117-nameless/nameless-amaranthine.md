# «Nameless Horrors» (nameless-horrors-en), часть amaranthine — сверка заголовков (Р-134, Р-251)

Страницы: печатные 1–42 (выходные данные, оглавление, введение сборника, «An Amaranthine Desire» с приложениями) и
физ. 1–2 (обложка, страница Chaosium). Печатная страница = физическая − 2 (проверено по картинкам с. 12, 23, 31 —
смещение верное). Записи — `kb/books/nameless-horrors-en/` (105: сценарий 1, сцены 15, персонажи 24 (из них готовых
сыщиков 6, групповых профилей 2), существа 3, организация 1, предметы 5, раздатки 7, места 46, карты 2, правило 1).
Картинки: 29 (13 портретов, 7 раздаток, 9 иллюстраций/схем) — `art-amaranthine.json`, рамки — `boxes-amaranthine.json`;
карты — `app/maps/nameless-amaranthine-dunwich-1287.jpg`, `app/maps/nameless-amaranthine-dunwich-through-the-ages.jpg`.
Русского перевода сценария в базе нет (проверено по именам и местам в `kb/books/*-ru/`).

Пути ниже — id без префикса `nameless-horrors-en/`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) «Call of Cthulhu. Nameless Horrors. Six Reasons to Fear the Unknown» | физ. 1 | `rule/nameless-horrors-introduction` (sources, quality); картинка — атмосфера |
| (страница Chaosium Inc.) | физ. 2 | `rule/nameless-horrors-introduction` (sources); картинка — атмосфера |
| (титул, логотип) | с. 1 | `rule/nameless-horrors-introduction` (sources); картинка — атмосфера |
| Authors / Editing / … / Thanks to our Playtesters (выходные данные) | с. 2 | `rule/nameless-horrors-introduction` (quality: авторы, редакторы, художники); список плейтестеров и бэкеров — не взят (см. ниже) |
| Table of Contents | с. 3 | `rule/nameless-horrors-introduction`, `scenario/an-amaranthine-desire` (sources) |
| Introduction (сборника) | с. 4 | `rule/nameless-horrors-introduction` (summary, text) |
| The Scenarios | с. 5 | `rule/nameless-horrors-introduction` (text: шесть сценариев) |
| An Amaranthine Desire (титульная иллюстрация) | с. 6 | `scenario/an-amaranthine-desire` (sources); картинка — `location/witches-pyre` |
| An Amaranthine Desire / By Matthew Sanderson (эпиграф Стейнбека) | с. 7 | `scenario/an-amaranthine-desire` (summary, quality — эпиграф) |
| Introduction (сценария) | с. 7 | `scenario/an-amaranthine-desire` (summary, keeper_info), `location/dunwich-suffolk` |
| Keeper Considerations | с. 7 | `scenario/an-amaranthine-desire` (advice), `scene/amaranthine-time-loop` |
| Pre-generated Investigators (врезка) | с. 7 | `scenario/an-amaranthine-desire` (hook), `scene/amaranthine-dunwich-1895` |
| Background | с. 8 | `scenario/an-amaranthine-desire` (keeper_info) |
| The Three Crowns | с. 8 | `item/dunwich-crown`, `scenario/an-amaranthine-desire` (keeper_info) |
| The Tale of Sarah Browne | с. 8–10 | `character/sarah-browne` (legend), `character/thomas-browne`, `character/william-levett`, `character/joseph-fynche`, `character/ralph-hawkins`, `organization/servants-of-the-old-gods` |
| The Three Crowns: Other Legends (врезка) | с. 10 | `item/dunwich-crown` (quality: все толкования) |
| The Old Gods (врезка) | с. 10 | `creature/he-that-is-the-dark-behind-the-night` (legend), `scenario/an-amaranthine-desire` (keeper_info) |
| The Storms and the Fate of Dunwich | с. 10 | `location/dunwich-suffolk` (history), `location/st-bartholomews-church` |
| Dramatis Personae | с. 11 | персонажи ниже |
| New Spell: Wrath of Ages (врезка) | с. 11 | общая `coc:spell:wrath-of-ages` (уже есть по Grand Grimoire) — предложение: источник и пометка (`proposals-amaranthine.json`) |
| Sarah Browne | с. 11 | `character/sarah-browne` |
| Servants of the Old Gods | с. 11 | `organization/servants-of-the-old-gods` |
| Katherine Downing | с. 11, 13 | `character/katherine-downing` |
| Relationship Map | с. 12 | картинка `scenario/an-amaranthine-desire` (plan); связи — `relations` персонажей |
| Dramatis Personae (иллюстрация) | с. 13 | портреты 7 персонажей |
| Clare Boone | с. 13 | `character/clare-boone` |
| Nathaniel Hall | с. 13 | `character/nathaniel-hall` |
| Tarquin | с. 13 | `creature/tarquin` |
| William Levett | с. 13–14 | `character/william-levett` |
| Ralph Hawkins | с. 14 | `character/ralph-hawkins` |
| Father Joseph Fynche | с. 14 | `character/joseph-fynche`, `creature/ghost-of-father-fynche` |
| Walter Lucas | с. 14–15 | `character/walter-lucas` |
| Henry Scott | с. 15 | `character/henry-scott` |
| Priests of St. Bartholomew’s | с. 15 | `character/priests-of-st-bartholomews` (групповой профиль) |
| Dunwich City Guard | с. 15 | `character/dunwich-city-guard` (групповой профиль), `scene/amaranthine-city-streets` |
| Events Unfold | с. 16 | `scene/amaranthine-dunwich-1895`, `scene/amaranthine-time-loop` |
| Handout: Amaranthine 1 — Setting the Scene | с. 16, 34 | `handout/amaranthine-1-setting-the-scene` |
| Contextual Information | с. 16 | `scene/amaranthine-dunwich-1895` |
| Dunwich, 1895 | с. 16–17 | `scene/amaranthine-dunwich-1895`, `location/dunwich-beach`, `location/wave-rider`, `character/louis-gerd` |
| Father Fynche observes the Investigators (иллюстрация) | с. 17 | картинка `scene/amaranthine-dunwich-1895` |
| Dunwich: 1287 | с. 17 | `scene/amaranthine-time-loop` |
| Timeline of Events | с. 17 | `scene/amaranthine-time-loop` (нумерованный список 1–6) |
| Effects of Note | с. 17 | `scene/amaranthine-time-loop` |
| Language Barrier | с. 18 | `scene/amaranthine-time-loop` |
| Damage and Dying | с. 18 | `scene/amaranthine-time-loop` (mechanics) |
| The Night Begins Again | с. 18 | `scene/amaranthine-time-loop` (описание, старение), `location/st-bartholomews-church` |
| Ending the Cycle | с. 18 | `scene/amaranthine-time-loop` (mechanics) |
| Denying Reality | с. 18 | `scene/amaranthine-time-loop` (mechanics) |
| What is the Void? (врезка) | с. 19 | `creature/he-that-is-the-dark-behind-the-night`, `scene/amaranthine-time-loop` |
| In the Woods | с. 19–20 | `scene/amaranthine-in-the-woods`, `location/greyfriars-wood` |
| Tarquin, Clare, Nathaniel, and Katherine (иллюстрация) | с. 19 | картинка `organization/servants-of-the-old-gods` |
| The Crown Revealed (врезка) | с. 20 | `scene/amaranthine-in-the-woods` (mechanics), `item/dunwich-crown`, раздатки 2–7 |
| 1287: Historical Context (врезка) | с. 20 | `scene/amaranthine-in-the-woods`, `location/dunwich-suffolk` |
| The Windmill | с. 21–22 | `scene/amaranthine-the-windmill`, `location/burning-windmill`, `item/sigils-on-fynches-body`, `item/fynches-silver-cross`; иллюстрация — картинка `location/burning-windmill` |
| Approaching the City | с. 22–23 | `scene/amaranthine-approaching-the-city`, `location/gilden-gate`, `location/palesdyke`, `location/covent-garden-dunwich`, `location/cock-hill-beacon` |
| Ancestors (врезка) | с. 22 | `scene/amaranthine-approaching-the-city`, `character/tobias-levett`, `character/elizabeth-devereux`, `location/levetts-house` |
| The City Streets | с. 23–24 | `scene/amaranthine-city-streets`, `location/dunwich-suffolk` (описание 1287 г.), `location/blackfriars`, `location/bridge-gate`, `location/king-johns-highway`, `location/maison-dieu`, `location/st-james-chapel` |
| (карта) Dunwich in the year of our lord 1287 | с. 23 | `map/dunwich-1287` (39 меток: легенда 1–17, мельницы, подписи) |
| Traveling Beyond the City | с. 24 | `scene/amaranthine-city-streets`, `location/walberswick`, `location/edge-of-the-world` |
| The City Jail | с. 24 | `scene/amaranthine-city-jail`, `location/city-jail`, `location/market-place`, `location/st-johns-church` |
| The Harbor Inn | с. 24–25 | `scene/amaranthine-harbor-inn`, `location/harbor-inn`, `character/george-hayman`, `character/samuel-harding`, `character/henry-scott` |
| Sarah’s House | с. 25–26 | `scene/amaranthine-sarahs-house`, `location/sarahs-house`, `item/elder-sign-under-floorboards` |
| The Elder Sign (иллюстрация) | с. 25 | картинка `item/elder-sign-under-floorboards` |
| Levett’s House | с. 26 | `scene/amaranthine-levetts-house`, `location/levetts-house`, `character/miles-holt` |
| Sarah’s Documents (врезка и сноска о «Gather the Abundance of the Sea») | с. 26 | `item/sarahs-documents`; общая `coc:spell:attract-fish` — предложение (источник, расхождение 2d100+100 / 1d100) |
| St. Bartholomew’s Church | с. 26–27 | `scene/amaranthine-st-bartholomews-church`, `location/st-bartholomews-church`, `location/st-bartholomews-crypt` |
| The Ghost Attacks! | с. 27 | `scene/amaranthine-st-bartholomews-church`, `creature/ghost-of-father-fynche` (иллюстрация — картинка), `item/dunwich-crown` |
| Burning Sarah | с. 27–28 | `scene/amaranthine-burning-sarah`, `location/witches-pyre` |
| The Wrath of Ages is cast (иллюстрация) | с. 28 | картинка `scene/amaranthine-burning-sarah` |
| Sarah’s Prayer (врезка) | с. 28 | `scene/amaranthine-burning-sarah` (текст молитвы по-русски и по-английски) |
| Edge of the World | с. 28–29 | `scene/amaranthine-edge-of-the-world`, `location/edge-of-the-world`, `location/king-johns-highway` |
| Point of Return | с. 29–30 | `scene/amaranthine-point-of-return` (список бурь 1916–2013) |
| Unaided Escape (врезка) | с. 30 | `scene/amaranthine-edge-of-the-world` (mechanics) |
| Coda: Future Shores | с. 30–32 | `scene/amaranthine-coda-future-shores`, `location/ship-inn`, `location/all-saints-church`, `location/st-james-church` |
| (карта) Dunwich Through The Ages | с. 31 | `map/dunwich-through-the-ages` (13 меток) |
| Conclusion | с. 32 | `scenario/an-amaranthine-desire` (conclusion: награды Рассудка), `item/dunwich-crown` (mechanics) |
| Appendix A: Characters | с. 32–33 | статблоки ниже |
| SARAH BROWN, 29, Priestess of the Old Gods | с. 32 | `character/sarah-browne` (statblock) |
| KATHERINE DOWNING, 32, Servant of the Old Gods | с. 32 | `character/katherine-downing` |
| CLARE BOONE, 22, Servant of the Old Gods | с. 32 | `character/clare-boone` |
| NATHANIEL HALL, 26, Servant of the Old Gods | с. 32–33 | `character/nathaniel-hall` |
| TARQUIN, Shape-shifting familiar | с. 33 | `creature/tarquin` |
| WILLIAM LEVETT, 31, Merchant driven by greed | с. 33 | `character/william-levett` |
| RALPH HAWKINS, 25 | с. 33 | `character/ralph-hawkins` |
| JOSEPH FYNCHE, 42, Guardian of the Dunwich Crown | с. 33 | `character/joseph-fynche` |
| Fynche as THE GHOST | с. 33 | `creature/ghost-of-father-fynche` (`instance_of` `coc:creature:ghost`) |
| PRIESTS OF ST. BARTHOLOMEW’S, Servants of the Lord | с. 33 | `character/priests-of-st-bartholomews` |
| DUNWICH CITY GUARD, Servants of the People | с. 33 | `character/dunwich-city-guard` |
| Appendix B: Handouts | с. 34–35 | раздатки ниже (текст как напечатан + перевод + картинка) |
| Handout: Amaranthine 1 — Setting the Scene | с. 34 | `handout/amaranthine-1-setting-the-scene` |
| Handout: Amaranthine 2 — Legends of the Three Crowns for Tobias Levett | с. 34 | `handout/amaranthine-2-legends-tobias-levett` |
| Handout: Amaranthine 3 — … for Elizabeth Devereux | с. 34 | `handout/amaranthine-3-legends-elizabeth-devereux` |
| Handout: Amaranthine 4 — … for Marie Martindale | с. 35 | `handout/amaranthine-4-legends-marie-martindale` |
| Handout: Amaranthine 5 — … for Theodore Maynard | с. 35 | `handout/amaranthine-5-legends-theodore-maynard` |
| Handout: Amaranthine 6 — … for Emmanuel Beaulieu | с. 35 | `handout/amaranthine-6-legends-emmanuelle-beaulieu` |
| Handout: Amaranthine 7 — … for Richard Garrett | с. 35 | `handout/amaranthine-7-legends-richard-garrett` |
| Appendix C: Pre-Generated Player Investigators / Overview of the Investigators | с. 36 | `description` готовых сыщиков |
| Tobias Levett, customs official, age 35 | с. 37 | `character/tobias-levett` |
| Elizabeth Devereux, lady of leisure, age 20 | с. 38 | `character/elizabeth-devereux` |
| Marie Martindale, farmer’s wife, age 25 | с. 39 | `character/marie-martindale` |
| Theodore Maynard, criminal, age 27 | с. 40 | `character/theodore-maynard` |
| Emmanuelle Beaulieu, smuggler, age 33 | с. 41 | `character/emmanuelle-beaulieu` |
| Richard Garrett, gamekeeper, age 35 | с. 42 | `character/richard-garrett` |

Упомянутые без своих записей (текст — в записях): Агнес Браун (мать Сары) и жена трактирщика — в `character/sarah-browne`,
`character/george-hayman`; Алан (муж Эммануэль) и Джеймс Тёрнер (браконьер) — в легендах `character/emmanuelle-beaulieu`,
`character/richard-garrett`; шестеро моряков Портового трактира — в `character/samuel-harding`; около десяти местных на
берегу и около тридцати тушащих мельницу — в сценах; «Та, что ходит нехожеными тропами» — в `creature/tarquin`;
исторические лица (Эдуард I, короли Редвальд, Анна, Сигеберт, Эдмунд, Белин и др.) — в `location/dunwich-suffolk` и
`item/dunwich-crown`; Олдборо, Блитбург, Брамфилд, Рендлшем, Бери-Сент-Эдмундс, Саксмандем, Норидж, Ипсвич, Старый
Уинчелси, Гастингс — текстом.

## Не взято

| Что | Страница | Причина |
|---|---|---|
| Список плейтестеров и благодарность бэкерам Kickstarter | с. 2 | имена без игрового содержания; авторы и художники записаны в `rule/nameless-horrors-introduction` (quality) |
| Бледные белые подписи улиц на карте 1287 года (у церкви Святого Леонарда, у рынка «St J…’s street», в центре, на западе за стеной) | с. 23 | в PDF не читаются; метки не поставлены (кроме «king street» — с сомнением) |
| Картинки обложки (физ. 1), страницы Chaosium (физ. 2), логотип (с. 1), украшения с. 30 и 32 | — | атмосфера: `atmosphere-amaranthine.json` |
| Средневековые «Бумаги Сары» как книга Мифов | с. 26 | у книги нет чисел (Мифы, Рассудок); оформлены предметом `item/sarahs-documents` |

## Опечатки и сомнения книги

| Где | Напечатано | Ожидалось | Что сделано |
|---|---|---|---|
| с. 5 (введение сборника) и карта с. 31 | «It is 1753…», береговая линия «1753» | 1895 (во всём сценарии) | `scenario/an-amaranthine-desire` errata; эпоха записей — gaslight |
| с. 32, заголовок статблока | SARAH BROWN | Sarah Browne | псевдоним (Р-39) |
| с. 9, 10, 28 | Levitt | Levett | псевдоним `character/william-levett` |
| с. 17, хронология п. 5 | Water Lucas | Walter Lucas | псевдоним `character/walter-lucas` |
| с. 27 | Servants of the Old Ones | Servants of the Old Gods | молча (Р-39) |
| с. 35, раздатка 6 | for Emmanuel Beaulieu | Emmanuelle | quality раздатки, псевдоним персонажа |
| с. 12, схема связей | Richard Garett | Garrett | псевдоним |
| с. 34, раздатка 1 | JJanuary | January | молча (quality раздатки) |
| с. 32–33, Скорость | Кэтрин 6, Клэр 7, Натаниэль 7, Левет 6, Хокинс 8, священники 6, стража 7 | 7, 8, 8, 7, 9, 7, 8 | errata, как напечатано (Р-161); у групп — возраст не указан |
| с. 42, Скорость Ричарда Гаррета | 9 | 8 | errata, как напечатано (Р-161) |
| с. 33, Натаниэль | «Гнев веков» в статблоке не назван | (Слуги творят его вместе) | quality |
| с. 26 и Grand Grimoire | 2d100+100 рыб | GG: 1d100 | предложение в `coc:spell:attract-fish` (quality.notes) |

## Термины (English → русский), выбранные в этой части

| English | Русский |
|---|---|
| Nameless Horrors | «Безымянные ужасы» |
| An Amaranthine Desire | «Неувядающее желание» |
| amaranthine desire / unfading wish / undying desire | неувядающее желание / неумирающая жажда |
| Old Gods | Древние боги |
| Servants of the Old Gods | Слуги Древних богов |
| Priestess of the Old Gods | жрица Древних богов |
| He that is the dark behind the night | Тот, кто есть тьма за ночью |
| He that resides beyond our reach | Тот, кто пребывает вне нашей досягаемости |
| She who walks the untrodden paths | Та, что ходит нехожеными тропами |
| the void | пустота |
| Edge of the World | Край мира |
| time loop / loop resets | петля времени / перезапуск петли |
| Ending the Cycle | конец круга |
| Denying Reality | отрицание реальности |
| Point of Return | точка возвращения |
| Coda: Future Shores | Кода: берега будущего |
| familiar | фамильяр |
| Shape-shift | смена облика |
| Ghost Attack | атака призрака |
| Fynche as the Ghost | Призрак отца Финча |
| the Crown / Three Crowns / Wuffingas | Данвичская корона / три короны / Вуффинги |
| Elder Sign | Знак Старших богов (официальная форма) |
| Wrath of Ages | «Гнев веков» (как в общей записи) |
| Gather the Abundance of the Sea | «Собрать изобилие моря» (псевдоним «Привлечь рыбу») |
| Contact Deep One | «Связь с Глубоководными» (как в общей записи `coc:spell:contact-deep-one`) |
| Middle English | среднеанглийский |
| Dunwich (Suffolk) | Данвич (Саффолк) |
| St. Bartholomew’s Church | церковь Святого Варфоломея |
| the Palesdyke / palisade | Палесдайк / частокол |
| the Daine | Дейн |
| Gilden Gate / Bridge Gate | Гилденские ворота / Мостовые ворота |
| Cock Hill Beacon | сигнальный огонь на Кок-Хилле |
| Greyfriar’s Wood | Лес Грейфрайерс |
| King John’s Highway | Большая дорога короля Иоанна |
| Maison Dieu | Мезон-Дьё |
| Blackfriars / Grey Friars | Блэкфрайерс (доминиканцы) / Серые братья (францисканцы) |
| the Temple | Темпл |
| Harbor Inn | Портовый трактир |
| Ship Inn | трактир «Шип-инн» |
| Walberswick | Уолберзуик |
| Wave Rider | пароход «Уэйв Райдер» |
| Relationship Map | схема связей |
| Hard / Extreme / Regular roll | трудная / чрезвычайная / обычная проверка |
| group Luck roll | групповая проверка Удачи |
| bonus die / penalty die | бонусная кость / штрафная кость |
| push | повторная проверка |
| Know roll | проверка Знания |

Имена: Сара Браун, Кэтрин Даунинг, Клэр Бун, Натаниэль Холл, Тарквин, Уильям Левет, Ральф Хокинс, отец Джозеф Финч,
Уолтер Лукас, Генри Скотт, Джордж Хейман, Сэмюэл Хардинг, Майлз Холт, капитан Луис Герд, Томас Браун, Джеймс
Мартиндейл, Джонатан Левет; готовые сыщики — Тобайас Левет, Элизабет Деверо, Мари Мартиндейл, Теодор Мейнард,
Эммануэль Больё, Ричард Гаррет.
