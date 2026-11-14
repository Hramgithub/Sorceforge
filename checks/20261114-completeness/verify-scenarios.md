# Сверка находок проверки полноты: сценарии и прочие книги (2026-11-14)

Источник: `checks/20261114-completeness/findings.json` (`tools/completeness.py`). Разобраны:

- **А** — все `text.gap`, кроме книг `malleus-monstrorum-1-en`, `malleus-monstrorum-2-en`, `grand-grimoire-en`,
  `pulp-cthulhu-en`, `keeper-rulebook-ru`, `keeper-rulebook-en`, `cthulhu-dark-ages-en` (42 находки);
- **Б** — `context.handout_empty` (14), `links.character_unused` (3), `links.scene_no_place` (79).

Страницы — физические (`pages.py show … --physical`), если не сказано иное. Записи в `kb/` не менялись.

Вердикты А: **покрыто** — содержание страницы есть в записях (иногда без ссылки на эту страницу);
**частично** — запись есть, но чего-то не хватает; **нет** — содержания в базе нет; **служебное** — титры,
оглавление, указатель, биографии, реклама, обложки, вступление без игровых данных.

Итого по А: покрыто — 7, частично — 0, нет — 1, служебное — 34.

## А. text.gap (42)

| # | Книга | Стр. (физ.) | Что на страницах | Вердикт |
|---|---|---|---|---|
| 1 | arkham-en | 3–5 | титры | служебное |
| 2 | arkham-en | 252 | Приложение B «Game Aids»: генератор погоды, гостиницы с ценами, таблица репутации, даты обрядов ковена | покрыто: это сводка того, что уже есть в книге. Погода — `coc:rule:arkham-about` (таблица по месяцам), репутация — `coc:rule:arkham-reputation`, обряды — `arkham-en/organization/overview-arkham-coven`, цены — записи гостиниц `coc:location:arkham-634-hotel-miskatonic`, `-136-tilden-arms-hotel`, `-710-lewiston-house-hotel`, `-130-borden-arms-hotel`, `-724-ymca`, `-728-ywca` |
| 3 | arkham-en | 259–266 | биографии авторов, указатель | служебное |
| 4 | arkham-en | 274 | задняя обложка | служебное |
| 5 | arkham-guide-hort-ru | 2–6, 8 | с. 2–6 — оглавление; с. 8 — предисловие: где Аркхэм (10 км к северу от Салема, у Уэнхема), время действия (октябрь 1928), билет до Бостона $2,20, население | с. 2–6 служебное; с. 8 покрыто в `coc:location:arkham`: абзац «Путеводитель Hort (с. 9–11)» содержит всё это, но в `sources` стоит с. 9, а с. 8 нет |
| 6 | arkham-guide-hort-ru | 90 | вступление к району Аптаун | покрыто: `coc:location:arkham-uptown` (по arkham-en, с. 207), то же содержание; ссылки на Hort с. 90 нет |
| 7 | beyond-the-edge-of-darkness-en | 36–37 | благодарности, биография автора | служебное |
| 8 | cursed-idol-of-manco-capac-en | 50 | реклама других игр издателя | служебное |
| 9 | dead-light-en | 85–88, 90 | указатель (зацепки Story Seeds только перечислены, сами они на с. 60–63), биографии, реклама, задняя обложка | служебное |
| 10 | fears-sharp-little-needles-en | 3 | посвящения, копирайт | служебное |
| 11 | fears-sharp-little-needles-en | 7 | вступление редактора (без игровых данных) | служебное |
| 12 | fears-sharp-little-needles-en | 30, 32–34 | **сценарий «Whose Fuel is Men and Stones»** (с. 29–33 по печатной нумерации): обычный сценарий для Хранителя и одного игрока, Лондон, Паддингтон. Это не книга-игра. Внутри: завязка, «Странные происшествия» (7 видений с потерей Рассудка), описание района Паддингтона, подготовка сыщика, призыв, награды. Статблоки: Джалил (колдун), Хайтам (ученик), Назим/Хавла Абдельазиз (вербовщик), Живое пламя глубочайшей тьмы (аватар Ктугхи) | **нет**. При переносе сценарий пропустили со ссылкой на Р-217 (`checks/20261111-fsln/u2.md`), но Р-217 говорит только о соло-книге-игре «Наедине с пламенем» с нумерованными абзацами. В базе есть лишь термины `kb/terms/whose-fuel-is-men-and-stones.json`, `living-flame-of-deepest-black.json` и карта-термин (карта на с. 180 тоже не взята) |
| 13 | innsmouth-terror-en | 3 | титры | служебное |
| 14 | karnaval-bezumiya-ru | 80 | «Таблица Нереальности 1», пункты 5–8 (Осязание, Время, Дезориентация, Странное поведение) с примерами | покрыто: `karnaval-bezumiya-ru/scenario/karnaval-bezumiya`, `tables` → «Таблица Нереальности 1», строки 5–8. У таблицы в `source` только с. 79 |
| 15 | keepers-companion-en | 3–4 | титры | служебное |
| 16 | keepers-companion-en | 216–225 | Приложение E (биографии авторов), указатель | служебное |
| 17 | lightless-beacon-ru | 3 | титры | служебное |
| 18 | masks-of-nyarlathotep-en | 1, 3, 4 | обложка, титул, титры | служебное |
| 19 | masks-of-nyarlathotep-en | 659–669 | указатель, задняя обложка | служебное |
| 20 | masks-of-nyarlathotep-ru-players | 86–95 | готовые сыщики: Мэдлин Браун, Арчибальд Вашингтон, Уинстон Грин, Дженнифер Смолвуд, Йохан Браун, Франсуаза Пелетье | покрыто: все шесть есть в `masks-of-nyarlathotep-en/character/` (`madelyn-brown`, `archibald-washington`, `winston-greene`, `jennifer-smallwood`, `johan-braun`, `francoise-pelletier`) с `statblock`, по английской книге (физ. 39–48). Ссылки на русский листок игрока нет |
| 21 | mesyats-nochi-ru | 3 | титры | служебное |
| 22 | mify-hastura-ru | 6 | предисловие переводчика | служебное |
| 23 | mify-hastura-ru | 46 | задняя обложка | служебное |
| 24 | miry-lavkrafta-artefakty-ru | 4 | выходные данные | служебное |
| 25 | miry-lavkrafta-artefakty-ru | 7 | «От авторов» (приветствие) | служебное |
| 26 | miry-lavkrafta-artefakty-ru | 108–110 | «Первоисточники»: из какого рассказа взята каждая статья | служебное (библиография). Записи для статей есть: `coc:location:carcosa`, `cykranosh`, `coc:tome:gharne-fragments`, `coc:item:medallion-of-ithaqua` и др. |
| 27 | miry-lavkrafta-artefakty-ru | 113 | об авторах | служебное |
| 28 | naedine-s-prilivom-rules-ru | 2 | титры | служебное |
| 29 | novaya-zhizn-ru | 26 | «Источники»: ссылки на картинки из сети | служебное |
| 30 | osobnyaki-bezumiya-ru | 9–10 | с. 9 — история изданий; с. 10 — врезка «Трата Удачи» (пересказ правила «Книги Хранителя», с. 97) | с. 9 служебное; с. 10 покрыто правилом `coc:rule:spending-luck` |
| 31 | osobnyaki-bezumiya-ru | 221–224, 226 | указатель, задняя обложка | служебное |
| 32 | pax-cthuliana-ru | 69 | список спонсоров | служебное |
| 33 | pobeg-iz-innsmuta-ru | 19 | указатель мест путеводителя (номера 101–214) | служебное. Места есть как записи `coc:location:innsmouth-NNN-…` |
| 34 | reign-of-terror-women-en | 2–3 | титры | служебное |
| 35 | sny-o-yaponii-ru | 46–47 | готовые страшилки 7–8 (Рен и билет; Сяо и картина); «Возможные реакции японцев» (фразы с транскрипцией) | покрыто: `sny-o-yaponii-ru/scenario/sny-o-yaponii`, `tables` (строки 7–8 таблицы историй и таблица «Возможные реакции японцев…») |
| 36 | temnye-veka-tri-stsenariya-ru | 1, 3, 4 | обложка, титры | служебное |
| 37 | temnye-veka-tri-stsenariya-ru | 264–271 | указатель | служебное |
| 38 | temnye-veka-tri-stsenariya-ru | 274 | задняя обложка | служебное |
| 39 | tri-koshmarnykh-vechera-ru | 104–105 | Приложение Б «Авторы» | служебное |
| 40 | tsarstvo-terrora-ru | 3 | титры | служебное |
| 41 | vedomo-li-lyubvi-ru | 58 | биографии авторов | служебное |
| 42 | vedomo-li-lyubvi-ru | 61 | задняя обложка | служебное |

## Б1. context.handout_empty (14)

Все 14 раздаток — только картинка: фото, рисунок, символ или карта. Текста, который надо было бы перенести в `text`,
книга для них не печатает. У каждой нужно вырезать картинку со страницы ниже и записать её в `images` (навык kb-art).

| Раздатка | Что это | Где картинка (книга, физ. стр.) |
|---|---|---|
| `bezymyannyy-tuman-ru/handout/foto-derrika-yorka` | фото мужчины в шляпе | bezymyannyy-tuman-ru, с. 3, справа внизу |
| `bezymyannyy-tuman-ru/handout/foto-rene` | фото девочки с амулетом | bezymyannyy-tuman-ru, с. 1, справа |
| `bezymyannyy-tuman-ru/handout/simvol-shchita-akhilla` | символ «Щита Ахилла» | bezymyannyy-tuman-ru, с. 4, справа вверху |
| `bezymyannyy-tuman-ru/handout/izobrazhenie-amuleta` | янтарный амулет с валькнутом | bezymyannyy-tuman-ru, с. 5, справа вверху |
| `cursed-idol-of-manco-capac-en/handout/06-incan-parchment` | пергамент с пиктограммами (без перевода) | cursed-idol-of-manco-capac-en, с. 41, справа внизу |
| `cursed-idol-of-manco-capac-en/handout/07-amulet-of-protection` | серебряный медальон | cursed-idol-of-manco-capac-en, с. 40, по центру внизу |
| `cursed-idol-of-manco-capac-en/handout/08-burning-hand-amulet` | кулон Пылающей Руки | cursed-idol-of-manco-capac-en, с. 40, справа внизу |
| `cursed-idol-of-manco-capac-en/handout/09-encasing-warm-half` | тёплая половина оболочки | cursed-idol-of-manco-capac-en, с. 40, слева вверху |
| `cursed-idol-of-manco-capac-en/handout/10-encasing-museum-half` | холодная половина оболочки | cursed-idol-of-manco-capac-en, с. 40, справа вверху |
| `cursed-idol-of-manco-capac-en/handout/bridgeport-map` | карта Бриджпорта без подписей | cursed-idol-of-manco-capac-en, с. 41, слева |
| `eliksir-zhizni-ru/handout/foto-medalona` | ошейник с медальоном на ладони | eliksir-zhizni-ru, с. 7, слева |
| `eliksir-zhizni-ru/handout/foto-zhertv` | морг, тела в камерах | eliksir-zhizni-ru, с. 6, вверху. Если есть отдельный лист из комплекта раздаток владельца, взять его |
| `masks-of-nyarlathotep-en/handout/america-carlyle-papers-4` | фото яхты за джонками | masks-of-nyarlathotep-en, с. 126, вверху. Русский вариант — masks-of-nyarlathotep-ru-players, с. 11 |
| `masks-of-nyarlathotep-en/handout/america-carlyle-papers-8` | знак на лбу Элиаса | masks-of-nyarlathotep-en, с. 127, слева внизу. Русский вариант — masks-of-nyarlathotep-ru-players, с. 13 |

## Б2. links.character_unused (3)

| Персонаж | Вердикт |
|---|---|
| `pobeg-iz-innsmuta-ru/character/dzhebedayya-gilman` | Исторический персонаж из хронологии (1834) и описания отеля, в сценах не участвует. Должен ссылаться на место: в `coc:location:innsmouth-703-otel-dom-gilmana` он назван только в тексте, без ссылки на запись. Нужна связь с отелем (и с хронологией `coc:location:innsmouth`) |
| `pobeg-iz-innsmuta-ru/character/dzhon-smit` | Капитан Джон Смит, историческое лицо: по книге он дал название Рифу Дьявола (1616). В сценах не участвует. Нужна связь с `coc:location:innsmouth-1011-rif-dyavola`, где он упомянут только текстом |
| `pobeg-iz-innsmuta-ru/character/tomas-martin` | Основатель первой верфи (1678), из «Официальной истории». В сценах не участвует. Нужна связь с `coc:location:innsmouth` (история и хронология). Его ли это `coc:location:innsmouth-906-staraya-verf-martina`, книга не говорит, поэтому только «см. также» |

Связь со сценой или сценарием книга не даёт ни для одного из трёх: все трое — фон истории города. Чтобы проверка
считала их связанными, достаточно ссылки из записи места или в `refs` персонажа на место.

## Б3. links.scene_no_place (79)

Вердикты: **есть** — запись места есть, её можно поставить в `where`; **нет записи** — книга называет место, но записи для него нет (в скобках — запись города или района, если она есть); **без места** — у сцены нет постоянного места (телефон, письмо, поиск в библиотеке, воспоминание, совет Хранителю, итог).

Итого: есть — 6, нет записи — 13, без места — 60.

| Сценарий/группа | Сцены | Вердикт | Место (id) / примечание |
|---|---|---|---|
| bless-the-beast-and-children-ru | istoriya-denni-eymsa | без места | историю вспоминает полицейский или репортёр, где угодно в Аркхэме |
| dveri-vo-tmu-ru / servants-of-the-lake | lake-involving | без места | Фрейзер звонит по телефону |
| fears / dissociation | dissociation-abduction | нет записи | ночной рейс Сан-Диего — Сиэтл, салон самолёта (физ. 114) |
| fears / dissociation | dissociation-examining-vessels, dissociation-survivors | без места | «в любом окружении»; эпилог |
| fears / hatteras-reef | hatteras-video-of-the-attack | без места | видео показывает OBX-RG (физ. 76), отдельного места нет; на видео — `fears-sharp-little-needles-en/location/hatteras-reef` |
| fears / reaper | reaper-missing-couple, reaper-resolutions | без места | завязка (сведения о пропавших) и обзор развязок; убить Жнеца можно только в `…/location/reaper-shadowing` |
| fears / separation-anxiety | separation-missing, separation-friends-and-coworkers, separation-work-computer | нет записи | медицинская школа Университета Кейс Вестерн, Кливленд (физ. 9–10); записи здания нет, город — `coc:location:cleveland` |
| fears / separation-anxiety | separation-missing-persons-research, separation-mythos-research | без места | поиск в источниках |
| fears / sins-of-my-youth | sins-confessions | без места | там, где побеждён Путешественник |
| fears / sores | sores-calling-the-hospital, sores-their-turn | без места | телефонный звонок; ход болезни |
| fears / tormiss | tormiss-crossing-the-cultists, tormiss-doctor-patient, tormiss-official-channels | без места | нападения где угодно; кабинеты кардиологов (без названия); запросы в FDA и CDC |
| fears / undertow | undertow-novel, undertow-finding-hayes, undertow-dog-returns, undertow-pale-man | без места | завязка и справки; собака встречается на пляже, у дома или в спальне; Бледный человек приходит к сыщику, когда тот один |
| griby-s-yuggota-ru / mountains-of-the-moon | moon-vision-and-research | без места | запись от Ирен и чтение газет |
| keepers-companion-en / what-a-puzzler | puzzler-lost-in-art, puzzler-putting-the-pieces-together, puzzler-the-pale-man | без места | мир внутри картины; головоломку собирают где угодно; Бледный человек — по всему Аркхэму (`coc:location:arkham`) |
| lechebnitsa-ru | put-na-ostrov | без места | в пути, на лодке; прибывают к `lechebnitsa-ru/location/prichal` (`nort-aylend` уже в refs) |
| lokhmotya-korolya-ru (flight-north, springer-mound, talk-of-goatswood) | flight-bacon-obituary, flight-gresty-second-letter, flight-roby-note-to-delia, springer-gresty-first-letter, springer-highsmith-letter, talk-the-gap-year | без места | письма, некролог в журнале, годичный перерыв |
| masks / america | america-meeting-miriam-atwright | нет записи | Библиотека Уайднера Гарвардского университета, Кембридж (физ. 139), или по телефону |
| masks / america | america-meeting-professor-cowles | есть | `coc:location:miskatonic-university` (кабинет), `coc:location:arkham-139-grafton-diner`; бунгало на Пикман-стрит — записи нет |
| masks / campaign-beginning | campaign-message-from-an-old-friend | без места | радиограмма |
| masks / grand-conclusion | conclusion-the-eclipse | без места | исход для всего мира; ракета запускается с `masks-of-nyarlathotep-en/location/china-gray-dragon-island` |
| mify-hastura-ru / stage-four-carcosa | disappearance, search, transport | без места | там, где закончился прошлый сценарий; подсказки; способы попасть в Каркозу |
| mts-kharkov-37-ru | rabota-s-voyskami | есть | `mts-kharkov-37-ru/location/mts-kharkov-37` (всё время на станции) |
| mts-kharkov-37-ru | chtenie-dokumentov, eksperimenty, radiatsiya, tungusskiy-meteorit, vzaimodeystvie-s-tsvetom | без места | чтение и опыты где угодно; ложные версии; группа выбирает, что делать (по смыслу — станция) |
| ne-zabyvay-menya-ru | issledovaniya, ya-chuvstvuyu-sebya-uzhasno | без места | звонки в студии; симптомы болезни |
| osobnyaki-bezumiya-ru (code, crooked, memphis) | code-letter, code-meeting-connolly, code-ordinary-day, crooked-preliminary-research, memphis-staying-on-track | без места | письмо и телеграммы; воспоминания; обычный день; справки в библиотеке; совет Хранителю |
| pobeg / pobeg-iz-innsmuta | doktor-iezekil-uolles | есть | `coc:location:arkham-208-asbury-methodist-episcopal-church` (бумаги Уоллеса лежат в подвале церкви, физ. 80) |
| pobeg / pobeg-iz-innsmuta | politsiya-arkhema | есть | `coc:location:arkham-228-police-station` |
| pobeg / pobeg-iz-innsmuta | efraim-v-oblike-derbi | есть (условно) | Дерби живёт в Кроуниншилде, за пределами Аркхэма (физ. 81) — `coc:location:arkham-os114-crowninshield-manor`; когда и где он появится, решает Хранитель |
| pobeg / pobeg-iz-innsmuta | komnata-brayana-u-greggov | нет записи | дом Греггов в Ипсвиче, комната Брайана (физ. 80–81); город — `coc:location:ipswich` |
| pobeg / pobeg-iz-innsmuta | roditeli-brayana | нет записи | дом Бёрнхэмов, Саут-Паудермилл-стрит, 325 (физ. 79); район — `coc:location:arkham-french-hill` |
| pobeg / pobeg-iz-innsmuta | vstrevozhennyy-artur-anderson | без места | авария на неназванной улице Аркхэма (`coc:location:arkham`) |
| pobeg / reyd-na-innsmut | po-zovu-dolga, reyd-instruktazh, reyd-vremya-prishlo | нет записи | Федеральное здание в Бостоне, кабинет 402 и комната для совещаний (физ. 99–104); город — `coc:location:boston` |
| pobeg / reyd-na-innsmut | reyd-kontakt, reyd-proverka-biografiy | без места | агенты приходят к каждому сыщику домой; справки о биографиях |
| pobeg / reyd-tsel-4 | tsel-4-sbor-v-bostonskikh-dokakh | нет записи | бостонские доки (физ. 141); город — `coc:location:boston`; одно из судов — `coc:location:innsmouth-podvodnaya-lodka-s-19` |
| pobeg / nasledstvo-kroufordov | problema-rozhdeniya | без места | поиск семейных бумаг займёт недели |
| podzemka-ru | chto-pomnit-lyao-khan | нет записи | Ляо Хана держат в полиции (физ. 3); записи полицейского участка нет, город — `coc:location:montreal` |
| popalis-ru | promedlenie, smylis | без места | Брофи является, когда сыщики одни; погоня |
| poselok-berezovyy-ru | poezdka-v-tyurmu | нет записи | колония № 45, где сидит Козяев (физ. 12) |
| prizrak-ru | priglashenie | без места | звонок, телеграмма или визит; встреча назначена в `prizrak-ru/location/dom-brauna-rossa` (это уже следующая сцена) |
| pulp-cthulhu-en / the-disintegrator | disintegrator-vstrecha-s-finchem | есть | `coc:location:miskatonic-university` (отдельный кабинет университета, физ. 140) |
| pulp-cthulhu-en / the-disintegrator | disintegrator-izyskaniya | без места | справки в патентном бюро и газетах |
| sny-o-yaponii-ru | dreams, researching-aokigahara, taint-aftermath | без места | сны; «любая крупная библиотека»; исчезновения знакомых в США |
| terror-ru | dopros, poiski-chervyakova | без места | допрос «в комнате», какое здание — книга не говорит (по смыслу — `terror-ru/location/transportnyy-otdel`); поиски по больницам |

Проверка считает сцену «без места» только по пустому `where`. Многие сцены «без места» уже ссылаются на места в `refs`.
Для 60 сцен без постоянного места стоит пометить в проверке, что пустой `where` для них допустим (например,
отметкой в `quality`), иначе находка будет повторяться.

## Что нет или нужно исправить

1. **Нет сценария «Whose Fuel is Men and Stones»** (fears-sharp-little-needles-en, физ. 30–34, карта на физ. 180).
   Это обычный сценарий для Хранителя и одного игрока, а не книга-игра. Р-217 к нему применили ошибочно.
   Нужно перенести: сценарий, таблицу «Странные происшествия», персонажей Джалила, Хайтама и Назима/Хавлу
   Абдельазиз, существо «Живое пламя глубочайшей тьмы» (аватар Ктугхи), места (район Паддингтона, Паддингтонский
   бассейн и лодка «Рагад»), карту. Перед переносом — вопрос владельцу, раз прежнее решение было «не брать».
2. **Картинки для 14 раздаток** (Б1): вырезать со страниц, указанных в таблице, и записать в `images`.
3. **Связать трёх исторических персонажей** «Побега из Иннсмута» (Б2) с записями мест: отель «Дом Гилмана» (703),
   Риф Дьявола (1011), история Иннсмута.
4. **`where` для 6 сцен**, у которых место уже есть (Б3, вердикт «есть»).
5. **Места без записей**, которые называет книга (13 сцен): салон самолёта (fears, физ. 114); медицинская школа
   Кейс Вестерн (fears, физ. 9–10); Библиотека Уайднера (Маски, физ. 139); дом Греггов, дом Бёрнхэмов,
   Федеральное здание в Бостоне, бостонские доки (Побег из Иннсмута, физ. 79–81, 99–104, 141); полиция Монреаля
   (Подземка, физ. 3); колония № 45 (Посёлок Берёзовый, физ. 12). Можно завести записи или поставить в `where`
   запись города.
6. **Ссылки на страницы** (содержание есть, страница не указана):
   - `coc:location:arkham` — добавить arkham-guide-hort-ru, с. 8;
   - `coc:location:arkham-uptown` — добавить arkham-guide-hort-ru, с. 90;
   - `karnaval-bezumiya-ru/scenario/karnaval-bezumiya`, таблица «Таблица Нереальности 1» — добавить с. 80;
   - шесть готовых сыщиков «Масок» — добавить masks-of-nyarlathotep-ru-players, с. 86–95;
   - `sny-o-yaponii-ru/scenario/sny-o-yaponii` — с. 46–47 у соответствующих таблиц.
