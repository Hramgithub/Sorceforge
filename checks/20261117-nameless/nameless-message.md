# «Безымянные ужасы» (Nameless Horrors) — часть message: «A Message of Art» (с. 43–79)

Книга `nameless-horrors-en` (печатная = физическая − 2; сверено по с. 44, 48, 69, 71, 72). Сценарий Мэттью Сандерсона,
Париж, 10–12 апреля 1892 года — эпоха `gaslight`. Русского перевода в базе и библиотеке нет (проверено ведущим; поиск
по именам Пеладан, Вирсавия, Ла Раш, Дюран-Рюэль в `kb/books/*-ru/` — пусто). Русский текст — наш перевод (`translated`).

Записи — `kb/books/nameless-horrors-en/`, 75 записей части: сценарий 1, сцены 17, персонажи 20 (7 персонажей Хранителя
со статблоками, 4 без статблока, 3 групповых профиля, 6 готовых сыщиков), существа 6, места 18, карты 2, предметы 4,
книги 2, организации 3, раздатка 2. Картинки — `art-message.json` (21, применены), атмосфера — `atmosphere-message.json`,
предложения к общим записям — `proposals-message.json` (12, не применены).

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| A Message of Art (By Matthew Sanderson), эпиграф (Шоу) | 43 | `scenario/a-message-of-art` (summary, keeper_info) |
| Introduction | 43 | `scenario/a-message-of-art` (keeper_info «Вступление»); `creature/muse-from-beyond` (legend) |
| Keeper Considerations | 43 | `scenario/a-message-of-art` (advice) |
| Background for the Keeper | 43–46 | `scenario/a-message-of-art` (keeper_info), `character/josephin-peladan`, `character/pierre-la-rush`, `creature/bathsheba`, `organization/mystic-order-of-the-rose-croix`, `organization/salon-de-la-rose-croix`, `organization/cabalistic-order-of-the-rosicrucian`, `tome/evocations-du-dieu-interieur` |
| Иллюстрация (Ла Раш перед статуей) | 44 | картинка `creature/bathsheba` (art) |
| Pre-generated Investigators (врезка) | 45 | `scenario/a-message-of-art` (hook) |
| Fiction Shrouded in Truth | 46 | `scenario/a-message-of-art` (keeper_info), `location/durand-ruel-gallery` |
| Seeds of Inspiration | 46 | `scenario/a-message-of-art` (keeper_info), `creature/manifestation-of-inspiration` (способность) |
| Poster for Salon de la Rose + Croix | 46 | картинка `organization/salon-de-la-rose-croix` |
| Manifestations of Inspiration | 47 | `scenario/a-message-of-art` (keeper_info), `creature/manifestation-of-inspiration` |
| Dramatis Personae | 47 | `scenario/a-message-of-art` (keeper_info); персонажи ниже |
| Joséphin Péladan (Host) | 47 | `character/josephin-peladan` |
| Antonin Pinot (Painter) | 47, 49 | `character/antonin-pinot`, `item/the-man-and-the-bull` |
| Relationship Map | 48 | таблица «Карта отношений» и картинка (plan) у `scenario/a-message-of-art`; связи `relations` у персонажей |
| New Spell: Divination; A Note to Keepers | 49 | общая запись `coc:spell:divination` (есть, по Grand Grimoire) — предложения: источник и расхождение цены; `item/divination-font`; совет — в advice сценария |
| Pierre La Rush (Sculptor) | 49 | `character/pierre-la-rush` |
| Bathsheba (Manifestation of Inspiration) | 49–50 | `creature/bathsheba`, `item/bathsheba-ring` |
| Dramatis Personae (групповой портрет) | 50 | портреты 7 персонажей и `creature/bathsheba` (вырезки) |
| Justine Buisson (Choreographer) | 50 | `character/justine-buisson` |
| Dominique Deneriaz (Musician) | 50–51 | `character/dominique-deneriaz` |
| Maximillien Lavagne (Writer) | 51 | `character/maximillien-lavagne` |
| Aimée Prideaux (Poet) | 51 | `character/aimee-prideaux` |
| Act One: The Party; Overview | 51 | `scenario/a-message-of-art` (summary, steps) |
| Scene 1: The Absinthe House | 51–52 | `scene/message-absinthe-house`, `location/absinthe-house` (+ картинка) |
| Handout: Message 1 (Setting the Scene) | 52, 71 | `handout/message-1-setting-the-scene` |
| Карта «IXe Arrondissement — The Operatic Heart of Paris» | 53 | `map/ixe-arrondissement`, `location/ixe-arrondissement` |
| Scene 2: Péladan’s Residence; Arrival and Greeting; NPC Movements; Antonin Pinot; Aimée Prideaux; Justine Buisson; Dominique Deneriaz; Maximillien Lavagne | 53–54 | `scene/message-arrival`, `location/peladan-residence`, `peladan-lobby`, `peladan-lounge`, `peladan-library`; `character/fabian-coffier`, `message-maids`, `message-party-guests`, `item/painting-5000` |
| План «L’Appartement Péladan — Sombres Secrets de la Rue Pinon» | 55 | `map/peladan-apartment`; места `peladan-kitchen`, `peladan-dining-room`, `peladan-servants-quarters`, `peladan-lavatory`, `peladan-guest-bedrooms`, `peladan-offices`, `au-petit-riche` |
| Pierre La Rush and Bathsheba (фразы Вирсавии) | 55–56 | `scene/message-bathsheba-seeds` |
| La Rush and Péladan’s Occult Library | 57 | `scene/message-occult-library`, `location/peladan-occult-library` |
| Getting Upstairs | 57–58 | `scene/message-occult-library`, `character/message-gendarmes` |
| Other Rooms Upstairs | 58 | `scene/message-occult-library`, `location/peladan-guest-bedrooms`, `peladan-offices` |
| Framing Prideaux | 58 | `scene/message-framing-prideaux`, `character/pamela-guillon` |
| Handout: Message 2 (Évocations du Dieu intérieur) | 59, 72 | `handout/message-2-evocations-du-dieu-interieur`, `tome/evocations-du-dieu-interieur` |
| Leaving Péladan’s Residence | 60 | `scene/message-leaving-residence` |
| New Spell: Channeling God | 60 | общая запись `coc:spell:channeling-god` (есть, по Grand Grimoire) — предложения: источник, refs, уточнение текста |
| Scene 3: The Durand-Ruel Gallery; Péladan’s Ritual | 60–61 | `scene/message-durand-ruel-gallery`, `location/durand-ruel-gallery`, `character/jermaine-rivette` |
| The Man and The Bull (иллюстрация) | 61 | картинка `item/the-man-and-the-bull` |
| Scene 4: The End of the Evening; Péladan’s Arrival | 61 | `scene/message-peladan-arrival` |
| Pinot’s Death | 61–62 | `scene/message-pinot-death`, `location/peladan-lavatory` |
| The Gendarmerie | 62–63 | `scene/message-gendarmerie`, `location/gendarmerie-station` |
| Into the Night | 63 | `scene/message-into-the-night` |
| Act Two: The Aftermath; Overview; Artists’ Seeds of Inspiration; Justine Buisson; Maximillien Lavagne; Aimée Prideaux; Dominique Deneriaz | 63–65 | `scene/message-artists-seeds` |
| Potential Point of Conclusion / Divergence (врезка) | 64 | `scene/message-confronting-bathsheba` |
| De Vermiis Mysteriis (врезка) | 64 | `tome/de-vermiis-mysteriis-french` (edition_of общей записи; предложение — экземпляр в copies) |
| Talking to Péladan | 65 | `scene/message-talking-to-peladan` |
| Helping the NPCs; Fallout | 66 | `scene/message-helping-the-npcs` |
| Investigators’ Seeds of Inspiration; Clovis Hérbert; Edwina Alexander and Jane Harnsworth-Wright; René Rochefort and Donatien Benoit; Viviane Hainault | 66–67 | `scene/message-investigators-seeds`, `creature/manifestation-of-inspiration` (способность «Материал») |
| Thoiry | 68 | `scene/message-thoiry`, `location/thoiry`, `location/la-rush-house`, `creature/la-rush-minotaur`, `la-rush-kraken`, `la-rush-unicorn` |
| Conclusion (награды Рассудка) | 68 | `scenario/a-message-of-art` (conclusion) |
| Appendix A: Characters (статблоки) | 69 | статблоки 7 персонажей и `creature/bathsheba` |
| Muse from Beyond | 70 | `creature/muse-from-beyond` |
| Manifestation of Inspiration | 70 | `creature/manifestation-of-inspiration` |
| Appendix B: Handouts | 71–72 | `handout/message-1-setting-the-scene`, `handout/message-2-evocations-du-dieu-interieur` (+ картинки) |
| Appendix C: Pre-Generated Player Investigators | 73 | описание у каждого прегена |
| Edwina Alexander / Jane Harnsworth-Wright / Clovis Hérbert / Donatien Benoit / René Rochefort / Viviane Hainault | 74–79 | `character/edwina-alexander`, `jane-harnsworth-wright`, `clovis-herbert`, `donatien-benoit`, `rene-rochefort`, `viviane-hainault` (+ портреты) |

## Опечатки и расхождения книги

- Ссылки на страницы почти все на одну дальше раздела: Relationship Map (page 49 → 48), Seeds of Inspiration (47 → 46),
  Muse from Beyond / Manifestation (71 → 70), Divination (50 → 49), Framing Prideaux (59 → 58), Channeling God (61 → 60),
  «5,000» (62 → 61), Potential Point of Conclusion (65 → 64), Thoiry (69 → 68); «Channelling God (see page 59)» в статблоке
  Ла Раша — на одну раньше (60). `errata` сценария, Пеладана, Ла Раша.
- Срок жизни прорвавшихся Муз: 1d10 раундов (с. 70) и 1d10 минут (с. 46) — `errata` Музы.
- Скорость: Бюиссон 8 (по правилам 9), Денерьяз 7 (9), Придо 7 (8); Вивиан Эно — ПЗ 9 (10) и Скорость 9 (8) — `errata`,
  как напечатано.
- «Rue George Batellière» (с. 51) против «R. Gge Batellière» на карте (Гранж-Бательер) — `errata` абсентной.
- Без errata (Р-39, оформление): «Channelling/Channeling», «Rue le Peletier» / «Rue Le Pelletier», «Haussmann» / «Hausmann»,
  «Shub-Nigguarath» (с. 43), «Edgar Allen Poe» (с. 51), «Chevelier» в раздатке 2 (оставлено в английском тексте),
  «Hérbert» с акцентом.
- Цена заклинания Гадание: Nameless Horrors — 1d6 ПМ и 1 Рассудка с участника; общая запись (Grand Grimoire) — 1 ПМ и 1d6
  Рассудка. Предложение — пометка в `quality.notes` общей записи; какую цену считать верной — вопрос владельцу.
- Смещение страниц верное: printed = physical − 2.

## Термины (English → русский)

| English | Русский |
|---|---|
| A Message of Art | Послание искусства |
| Nameless Horrors | «Безымянные ужасы» |
| Muse from Beyond | Муза из-за грани (как в `coc:spell:channeling-god`) |
| Manifestation of Inspiration | Проявление вдохновения (так же) |
| Manifestations from Beyond (Conclusion) | Проявления из-за грани |
| Seed(s) of Inspiration; germinate | семя (семена) вдохновения; прорастать |
| astral horrors; art given life | астральный ужас; ожившее произведение искусства |
| Spinning Cut | Вращающийся разрез |
| Mystic Order of the Rose + Croix | Мистический орден Розы и Креста |
| Salon de la Rose + Croix | Салон Розы и Креста |
| Cabalistic Order of the Rosicrucian | Каббалистический орден Розы и Креста |
| Sâr | Сар |
| Martinism; Martinist | мартинизм; мартинистский |
| Beatific Vision | Блаженное видение |
| Inner God | Внутренний Бог |
| Theurgy; henosis | теургия; хенозис |
| Reaux-Croix | Рео-Круа |
| Elus Cohens; Order of Knight-Masons Elect Priests of the Universe | Избранные коэны; Орден рыцарей-масонов избранных коэнов Вселенной |
| Treatise on the Reintegration of Beings | «Трактат о реинтеграции существ» |
| reintegration; illumination | реинтеграция; просветление |
| Évocations du Dieu intérieur (Evocations of the Inner God) | «Évocations du Dieu intérieur» (в переводе «Воззвания к Внутреннему Богу») |
| Divination; Channeling God | Гадание; Проводник бога (общие записи) |
| Relationship Map; Dramatis Personae | Карта отношений; Действующие лица |
| Belle Époque | Прекрасная эпоха |
| Académie des Beaux-Arts | Академия изящных искусств |
| gendarmerie; gendarmes; detectives | жандармерия; жандармы; детективы |
| absinthe house | абсентная |
| IXe Arrondissement — The Operatic Heart of Paris | IX округ — оперное сердце Парижа |
| L’Appartement Péladan — Sombres Secrets de la Rue Pinon | Дом Пеладана: мрачные тайны улицы Пинон |
| Rue Pinon; Boulevard Haussmann; Rue le Peletier; Rue Grange-Batelière; Rue de Provence; Rue Thaitbout; Rue d’Artois; Rue de Richelieu | улица Пинон; бульвар Осман; улица Ле Пелетье; улица Гранж-Бательер; улица Прованс; улица Тетбу; улица д’Артуа; улица Ришельё |
| Comédie Italienne; Au Petit Riche; Tabac; M. DeGrasse, Avocat | Комеди Итальен; ресторан «О Пти Риш»; табачная лавка; контора адвоката М. Деграсса |
| Durand-Ruel Gallery | галерея Дюран-Рюэля |
| Thoiry; Beynes; Versailles | Туари; Бен; Версаль |
| City of the Elder Things | Город Старцев |
| Le Matin | «Ле Матен» |
| The Man and the Bull; “5,000” | «Человек и бык»; «5 000» |
| Joséphin Péladan; Antonin Pinot; Pierre La Rush; Bathsheba | Жозефен Пеладан; Антонен Пино; Пьер Ла Раш; Вирсавия |
| Justine Buisson; Dominique Deneriaz; Maximillien Lavagne; Aimée Prideaux | Жюстин Бюиссон; Доминик Денерьяз; Максимильен Лавань; Эме Придо |
| Fabian Coffier; Paméla Guillon; Jermaine Rivette; Paul Durand-Ruel | Фабиан Коффье; Памела Гийон; Жермен Ривет; Поль Дюран-Рюэль |
| Edwina Alexander; Jane Harnsworth-Wright; Thomas Harnsworth-Wright | Эдвина Александер; Джейн Харнсворт-Райт; Томас Харнсворт-Райт |
| Clovis Hérbert; Donatien Benoit; René Rochefort; Viviane Hainault | Кловис Эрбер; Донасьен Бенуа; Рене Рошфор; Вивиан Эно |
| Martinez de Pasqually | Мартинес де Паскуалли |
| Art/Craft; Know roll; Hard / Extreme | Искусство/ремесло; проверка Знаний; трудная / чрезвычайная проверка |

## Не взято

- Подписи улиц, театра Комеди Итальен и соседей (адвокат, табачная лавка) на картах — своих записей нет: метки ведут на
  запись округа с переводом в `text`; на врезке-карте плана Пеладана подписи улиц без меток (дублируют карту округа).
- Безымянные мелкие лица без записей: врач на месте смерти Пино (внутри профиля `message-gendarmes`), трое членов
  ордена в галерее (у ордена), Томас Харнсворт-Райт (в предыстории Джейн); станция Бен, больница Бюиссон, квартиры
  художников — текстом в сценах.
- Атмосферные картинки (экипаж, «Bathsheba inspires Prideaux», женщина у фортепиано, «The Butler finds Pinot»,
  «Aimée Prideaux in her cell», Старший знак) — `atmosphere-message.json`.
- Колонтитулы страниц.

## Вопросы владельцу

1. Карта отношений (с. 48) взята картинкой сценария (`plan`) и таблицей, а не записью `map` (метки на персонажей схема
   карты не предусматривает). Так ли?
2. Цена Гадания: Nameless Horrors (2015, первая публикация) против Grand Grimoire — какую держать в общей записи?
3. «Évocations du Dieu intérieur» записана как `occult_book` (`incomplete`: книга не даёт потери Рассудка и Мифов), хотя
   содержит рабочее заклинание Мифов.
