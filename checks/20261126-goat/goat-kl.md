# The Year of the Goat — часть kl (с. 187–228)

Сценарии «Dead Letters from the Orchard» (Perry Clark, с. 187–206) и «Mother of a Thousand Young» (Poul Holmelund,
с. 207–227); задняя обложка (с. 228). Смещение страниц 0 (печатная = физической; сверено по изображениям с. 200, 201,
202, 203, 209, 219–225). Русский текст — наш перевод (Р-251, Р-21). Префикс id: `year-of-the-goat-en/`.

Проверка до этого: сценариев нет в базе в русском переводе (поиск по Harper’s Orchard, Whistler, Tooms, Groan Peak,
Appleby — совпадения только с чужим Appleby из WWC Covert Actions).

## Dead Letters from the Orchard (с. 187–206) → `scenario/dead-letters-from-the-orchard`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Dead Letters from the Orchard (титул; Investigators 2-5, Game Time 6-8 hours) | 187 | `scenario/dead-letters-from-the-orchard` — summary |
| Introduction | 187 | scenario — summary |
| Scenario Structure | 187 | scenario — summary, hook |
| Background | 188 | scenario — keeper_info; `character/john-harper`, `character/miles-harper-sr`, `character/miles-harper-jr` |
| Historical Context (врезка) | 188 | scenario — advice; `location/harpers-orchard`, `location/north-harpers-orchard` |
| About the Investigators | 189 | scenario — advice |
| Tilda Whistler, 24, The Reporter | 189, 204 | `character/tilda-whistler` (pregen) |
| Quin Tooms, 25, The Police Officer | 189, 204 | `character/quin-tooms` (pregen) |
| Coral Bags, 24, The Researcher/Student | 189, 205 | `character/coral-bags` (pregen) |
| Bouts of Madness (врезка) | 189 | scenario — advice; `background.phobias_manias` каждого сыщика |
| Additional Optional Investigators: Dr. Vera Sanchez, 35 | 190, 205 | `character/vera-sanchez` (pregen) |
| Lonny Miles, 40, Handyman/Firefighter | 190, 206 | `character/lonny-miles` (pregen) |
| Dramatis Personae — Independents & Potential Allies | 190 | персонажи ниже |
| John Harper, 58, The Abolitionist | 190 | `character/john-harper` |
| Elias Hughes, 43, Post Office Employee | 190 | `character/elias-hughes` |
| Wila Lawrence, 52, Housekeeper | 190 | `character/wila-lawrence` |
| Antagonists: John Harper, 58, The Believer | 191 | `character/john-harper` (одна запись на обе личности) |
| Albert Whistler, 25, Police Officer | 191 | `character/albert-whistler` |
| Setting Up | 191 | `scene/orchard-setting-up`; `location/mayweather-boarding-house`, `character/elle-mayweather`, `character/ezra-coleman` |
| Act I: Lay of the Land | 192 | `scene/orchard-newspaper-office` |
| At the Newspaper Office | 192 | `scene/orchard-newspaper-office`; `location/harpers-orchard-newspaper-office` |
| Around West Harper’s Orchard | 192 | `location/west-harpers-orchard` |
| Jessup Boarding House | 192 | `scene/orchard-jessup-boarding-house`; `location/jessup-boarding-house`; `character/mae-jessup`, `character/patrick-goza` |
| Harper Manor | 193 | `scene/orchard-harper-manor`; `location/harper-manor` |
| Chronike von Nath/Chronicle of Nath (врезка) | 193 | `tome/chronicle-of-nath` |
| Orchard Processing Center | 193 | `scene/orchard-processing-center`; `location/orchard-processing-center`; `item/orchard-strange-fruit` |
| The Thicket | 193–194 | `scene/orchard-thicket`; `location/harpers-orchard-thicket` |
| Post Office | 194 | `scene/orchard-post-office`; `location/west-harpers-orchard-post-office` |
| Act II: Rising Tempers | 195 | `scene/orchard-taking-stock` |
| Taking Stock | 195 | `scene/orchard-taking-stock` |
| Compel Nature (врезка) | 195 | черновик общего заклинания `coc:spell:compel-nature` — `new-shared-spells-kl.json`; текст — в сценах |
| Herbert House | 195–196 | `scene/orchard-herbert-house`; `location/herbert-house`; `character/polly-herbert`, `character/william-herbert`, `character/mary-herbert`, `character/lloyd-herbert` |
| Blake’s Repair & Smith | 196 | `scene/orchard-blakes-repair`; `location/blakes-repair-and-smith`; `character/marguerite-blake` |
| Act III: Revelation | 197 | `scene/orchard-greenhouse` |
| The Greenhouse | 197 | `scene/orchard-greenhouse`; `location/orchard-workshop`, `location/orchard-greenhouse` |
| Keeper’s Note (как ест Харпер) | 197 | `scene/orchard-greenhouse` |
| The Black Cherry Tree | 197 | `scene/orchard-black-cherry-tree`; `creature/black-cherry-tree` |
| Battling the Dark Young | 197–198 | `scene/orchard-black-cherry-tree` |
| Conclusion | 198 | scenario — conclusion |
| Epilogue | 198 | scenario — conclusion |
| Rewards | 198 | scenario — conclusion |
| Characters & Monsters: The Black Cherry Tree, Dark Young of Shub-Niggurath | 199 | `creature/black-cherry-tree` (instance_of `coc:creature:dark-young-of-shub-niggurath`) |
| Hybrid, Transformed Servant of Shub-Niggurath | 199 | `creature/orchard-hybrids` |
| Player Handouts | 200 | раздатки ниже |
| Handout #1: Harper’s Letter | 200 | `handout/orchard-handout-1-harpers-letter` |
| Handout #2: Town Map | 201 | `map/orchard-town-map` (метки на каждую подпись: здания → места, улицы → район) |
| Handout #3: Envelope | 201 | `handout/orchard-handout-3-envelope` |
| Handout #4: Post Office Log | 202 | `handout/orchard-handout-4-post-office-log` |
| Handout #5: Bark; Keeper’s Note | 203 | `handout/orchard-handout-5-bark`; `item/cursed-bark-letters` |
| Investigators (листы сыщиков) | 204–206 | пять pregen-записей |

Места карты без своего раздела в тексте: `location/harpers-orchard-clinic`, `harpers-orchard-firehouse`, `carter-market`,
`harpers-orchard-library`, `harpers-orchard-bank`, `harper-orchard-groves`; группа `character/north-harpers-orchard-vigilantes`
(вооружённые белые, без статблока); улика `item/harper-land-papers`.

## Mother of a Thousand Young (с. 207–227) → `scenario/mother-of-a-thousand-young`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Mother of a Thousand Young (титул; 1953; Investigators 4, 3-4 hours) | 207 | `scenario/mother-of-a-thousand-young` — summary |
| Introduction | 207 | scenario — summary |
| Scenario Structure | 207 | scenario — summary |
| Background | 208 | scenario — keeper_info; `character/gladys-appleby` — legend |
| Groan Peak | 208 | `location/groan-peak`; scenario — keeper_info |
| About the Investigators | 209 | scenario — advice |
| Rose Thompson, 39, The Mediator | 209, 226 | `character/rose-thompson` (pregen) |
| Samuel Brooks, 29, The Ambitious | 209, 226 | `character/samuel-brooks` (pregen) |
| Walter Grey, 45, The Bureaucrat | 209, 227 | `character/walter-grey` (pregen) |
| Tommy Baker, 24, The Circumspect | 209, 227 | `character/tommy-baker` (pregen) |
| Dramatis Personae | 209 | scenario — advice; `character/abel-carter`, `richard-johnson`, `beatrice-johnson`, `lesley-johnson`, `johnny-wilson`, `dan-gore`, `anabell-skoge`, `gladys-appleby` (Judy Label — псевдоним), `margaret-connerly` |
| Antagonist: Gladys Appleby, 65, Demi-Ghoul Witch of Shub-Niggurath | 210 | `character/gladys-appleby` |
| Act I: The Missing Teens | 210 | `scene/thousand-missing-teens`; `organization/groan-peak-police-department` |
| Meeting the Johnsons | 210–211 | `scene/thousand-meeting-the-johnsons`; `location/johnson-home`, `location/blue-hill`; `item/johnnys-convertible`; `character/johnson-party-guests` |
| The Parking Lot at the Lookout | 211 | `scene/thousand-lookout`; `location/lookout-parking-lot` |
| Stumbling In The Woods | 211–212 | `scene/thousand-stumbling-in-the-woods`; `location/groan-peak-outskirts`, `location/groan-peak-fox-den` |
| Interlude | 212 | `scene/thousand-interlude` |
| Act II: The Search | 212 | `scene/thousand-station-briefing` |
| Station Briefing | 212 | `scene/thousand-station-briefing`; `character/hal-brennan` (коронер) |
| Principal Gore | 212–213 | `scene/thousand-principal-gore`; `location/groan-peak-high-school` |
| Judy´s Home? | 213–214 | `scene/thousand-judys-home`; `location/gladys-appleby-house`, `location/groan-peak-abandoned-house`, `location/groan-peak-poor-quarter`; `item/judys-ford-pickup`, `item/judys-yellow-dress`, `item/gladys-jars`, `item/mothers-lashing-tongue`; `character/carla-baker` |
| The Orphanage | 214 | `scene/thousand-orphanage`; `location/groan-peak-orphanage`; `character/timmy` |
| Final Act: The Confrontation | 215 | `scene/thousand-spelunking` |
| Spelunking | 215 | `scene/thousand-spelunking`; `location/ghoul-tunnels` |
| Confrontation with Gladys | 215 | `scene/thousand-confrontation-with-gladys`; `location/ghoul-central-cave` |
| Conclusion | 216 | scenario — conclusion |
| Keeper’s Notes (Карла) | 216 | scenario — conclusion; `character/carla-baker`, `character/tommy-baker` |
| Rewards | 216 | scenario — conclusion |
| Characters & Monsters: Adult Ghouls, The Trench Children | 217 | `creature/thousand-adult-ghouls` (instance_of `coc:creature:ghoul`) |
| Child Ghouls, Adoptees from the Orphanage | 217 | `creature/thousand-child-ghouls` |
| Adolescent Ghouls, Spawn of Gladys | 217 | `creature/thousand-adolescent-ghouls` |
| Gladys Apleby, 65 (статблок), Possessions | 218 | `character/gladys-appleby`; `item/mothers-lashing-tongue`, `item/mothers-pearls`, `tome/mothers-hungry-children` |
| Player Handouts; Handout #1: Groan Peak Map | 219 | `map/groan-peak-map` (метки 1–6, заголовок, ключ) |
| Handout #2: Rose´s Knowledge of Gladys | 220 | `handout/thousand-handout-2-roses-knowledge` |
| Handout #3: Samuel´s Knowledge of Gladys | 221 | `handout/thousand-handout-3-samuels-knowledge` |
| Handout #4: Walter´s Knowledge of Gladys | 222 | `handout/thousand-handout-4-walters-knowledge` |
| Handout #5: Tommy´s Knowledge of Gladys | 223 | `handout/thousand-handout-5-tommys-knowledge` |
| Handout #6: The Mother´s Hungry Children | 224 | `handout/thousand-handout-6-mothers-hungry-children`; `tome/mothers-hungry-children` |
| Handout #7: Children’s Drawing | 225 | `handout/thousand-handout-7-childrens-drawing` |
| Investigators (листы сыщиков) | 226–227 | четыре pregen-записи |
| Задняя обложка (эпиграф из «Шепчущего во тьме», аннотация сборника) | 228 | источник `scenario/mother-of-a-thousand-young`; картинка — `atmosphere-kl.json` |

## Не взято

- Строки «PLAYER NOTES» на листах сыщиков (с. 204–206, 226–227) — пустые поля для записей игрока.
- Декоративные картинки без привязки к записи (с. 189 портрет женщины без подписи, с. 196 кричащее лицо, маски заголовков,
  рамки раздаток, фон задней обложки) — в `atmosphere-kl.json`.
- Текст задней обложки (с. 228): эпиграф Лавкрафта и аннотация всего сборника — не данные сценария; отмечен источником
  сценария «Мать тысячи младых» (последний в книге).
- Безымянные эпизодические фигуры без роли в игре: главный аптекарь (убит Гозой — в легендах Веры и Гозы), шериф Северного
  Харперс-Орчарда, жена директора Гора, ночная смена полиции, бродячая кошка, кошка Гозы, родители сыщиков (Сол и Салли,
  Сэмюел и Эбигейл Майлз — в `background.significant_people`), Анна Бейкер (в легенде Томми) — текстом в записях.

## Опечатки и сомнения книги

- Возраст сыщиков «Dead Letters»: Куин 25/24, Корал 24/22, Вера 35/29, Лонни 40/30 (описание / лист) — errata, в записи по листу.
- «Lonnie» (с. 189) / «Lonny»; «Willa Lawrence» (раздатка 1) / «Wila»; «Walther Grey» (с. 211); «Gladys Apleby» (с. 218);
  «Leslie»/«Lesley»; отец Лесли — «Richard» (с. 209) и «Clyde» (с. 210).
- Неверные половина/пятая исправлены (Р-35): Куин Средства 18% (9/1→9/3); Лонни Обаяние 50% (25/20→25/10); Уолтер
  Револьвер 25% (12/7→12/5), Винтовка 60% (30/6→30/12), Вождение 25% (12/7→12/5), Внимание 40% (20/9→20/8); упыри-подростки
  35% (17/6→17/7); упыри-дети 30% (15/5→15/6) ×3.
- Чёрная вишня: ПЗ 40 (по ВЫН+ТЕЛ — 34), Комплекция 7 (ожид. 6), потеря Рассудка 1d3+1/1d10 (у вида 1d3/1d10).
- Гибриды: ПЗ 20 (ожид. 14), БкУ 1d6 и Комплекция 2 (ожид. +1d4 и 1).
- Глэдис: ПЗ 12 (ожид. 13), Скорость 9 (ожид. 8, с возрастом 5). Роуз: ПМ 12 (13), Скорость 8 (7). Уолтер: Скорость 8 (7).
- Упыри-подростки: ПЗ 11 (12), ПМ 12 (13), «Attacks per round: 2 (Bite, Claw, Kick)». Упыри-дети: ПМ 9 (11), БкУ −1d4
  (по таблице −1), укус с захватом 1d4 в атаке и 1d2 в способности.
- Почтовый журнал: четыре письма без исправленного адреса, а текст говорит о двух недоставленных.
- Раздатка 6: цитата «Harvsted young men’s lifegiving seed and organs» против «Harvested the life-giving substance from young
  men» в тексте (с. 214); «Receipts» вместо «recipes». Раздатка 7: «TO MOMMY» против «To Mum» в тексте.
- Майлз Харпер-младший: на с. 190 отпущен со службы, на с. 206 «succumbed to injuries».
- В обзоре «Mother» (с. 207) — «ночные молнии», в актах их нет.

## Эпохи

- «Dead Letters from the Orchard» — 1910 год, оси `gaslight` (ближайшая эпоха до 1920-х; вопрос ведущему, если для
  1900–1910-х принято иное).
- «Mother of a Thousand Young» — 1953 год, оси `1940s-1980s` (Р-252).

## Термины (English → Russian)

| English | Русский |
|---|---|
| Dead Letters from the Orchard | Невостребованные письма из сада |
| dead letter; Dead Letters Department | невостребованное письмо; отдел невостребованных писем |
| Harper’s Orchard / West Harper’s Orchard / North Harper’s Orchard | Харперс-Орчард / Западный Харперс-Орчард / Северный Харперс-Орчард |
| the Orchard | сад Харперов (сад) |
| Orchard Processing Center / Processing Plant | центр переработки урожая / перерабатывающий цех |
| Workshop / Greenhouse | мастерская / теплица |
| The Thicket | Чаща |
| Harper Manor | особняк Харперов |
| Jessup Boarding House / Mayweather Boarding House | пансион Джессап / пансион Мэйуэзер |
| Herbert House | дом Хербертов |
| Blake’s Repair & Smith | «Ремонт и кузница Блейка» |
| Newspaper Office / Post Office / Clinic / Firehouse / Carter Market | редакция газеты / почта / клиника / пожарная часть / рынок Картера |
| Sunset town | закатный город |
| Jim Crow laws; Red Summer | законы Джима Кроу; «Красное лето» |
| John the Abolitionist / John the Believer | Джон-аболиционист / Джон-верующий |
| Black Goat of the Woods | Чёрная Коза Лесов |
| The Black Cherry Tree | Чёрная вишня |
| Dark Young (of Shub-Niggurath) | Тёмная молодь (Шуб-Ниггурат) — официальная форма |
| Hybrid; Transformed Servant of Shub-Niggurath | гибрид; превращённый слуга Шуб-Ниггурат |
| cursed bark; bark-like parchment | проклятая кора; похожий на кору пергамент |
| infection burrs | наплывы-«капы» |
| Chronike von Nath / Chronicle of Nath | «Хроника Ната» |
| Rudolf Yergler; Ka-Nefer; Hermes Trismegistus | Рудольф Йерглер; Ка-Нефер; Гермес Трисмегист |
| Compel Nature | Повеление природе |
| letter spike | наколка для бумаг |
| Bouts of Madness | приступы безумия |
| Anthophobia / Dipsomania | антофобия / дипсомания |
| Scotophobia / Demonomania | скотофобия / демономания |
| Autophobia / Thanatomania | аутофобия / танатомания |
| Rhabdophobia / Algomania | рабдофобия / алгомания |
| Haemophobia / Enosimania | гемофобия / эносимания |
| Tilda Whistler, Quin Tooms, Coral Bags, Vera Sanchez, Lonny Miles | Тильда Уислер, Куин Тумс, Корал Бэгс, Вера Санчес, Лонни Майлз |
| John Harper, Elias Hughes, Wila Lawrence, Albert Whistler, Patrick Goza | Джон Харпер, Элайас Хьюз, Уила Лоренс, Альберт Уислер, Патрик Гоза |
| Elle Mayweather, Mae Jessup, Polly / William / Mary / Lloyd Herbert, Marguerite Blake | Элл Мэйуэзер, Мэй Джессап, Полли / Уильям / Мэри / Ллойд Херберт, Маргерит Блейк |
| Miles Harper, Sr. / Jr. | Майлз Харпер-старший / -младший |
| The Reporter / The Police Officer, The Deputy / The Student / The Doctor / The Soldier | репортёр / помощник шерифа / студент / врач / солдат |
| Mother of a Thousand Young | Мать тысячи младых |
| Groan Peak | Гроун-Пик |
| Groan Peak Police Department | полиция Гроун-Пика |
| Blue Hill neighborhood | район Блю-Хилл |
| the lookout; The Parking Lot at the Lookout | смотровая площадка; стоянка у смотровой площадки |
| Groan Peak High School / Groan Peak Orphanage | средняя школа Гроун-Пика / сиротский приют Гроун-Пика |
| Poor Part of Town | бедная часть Гроун-Пика |
| Ghoul Tunnels; central cave | туннели упырей; логово в центральной пещере |
| Spelunking | под землёй (спелеология) |
| ghoul | упырь — официальная форма |
| Demi-Ghoul Witch of Shub-Niggurath | ведьма-полуупырь Шуб-Ниггурат |
| Adult Ghouls, The Trench Children | взрослые упыри, «Дети окопов» |
| Adolescent Ghouls, Spawn of Gladys | упыри-подростки, порождение Глэдис |
| Child Ghouls, Adoptees from the Orphanage | упыри-дети, «усыновлённые» из приюта |
| Bite and Hold | укус с захватом |
| Mother’s Lashing Tongue | «Хлёсткий язык Матери» |
| Mother’s Pearls | «Жемчуга Матери» |
| The Mother’s Hungry Children | «Голодные дети Матери» |
| Listen to Mother (Enthrall Victim) | «Слушай маму» (Околдовать жертву) |
| Come see me | «Приди ко мне» (народное «Come and See Me») |
| Control Skin (Deeper magic) | Управлять кожей (усиленная версия) |
| Mistress Appleby | госпожа Эпплби |
| Rose Thompson (The Mediator), Samuel Brooks (The Ambitious), Walter Grey (The Bureaucrat), Tommy Baker (The Circumspect) | Роуз Томпсон (Посредница), Сэмюел Брукс (Честолюбец), Уолтер Грей (Бюрократ), Томми Бейкер (Осмотрительный) |
| Gladys Appleby; Judy Label | Глэдис Эпплби; Джуди Лейбл |
| Abel Carter, Richard (Clyde) / Beatrice / Lesley Johnson, Johnny Wilson | Эйбел Картер, Ричард (Клайд) / Беатрис / Лесли Джонсон, Джонни Уилсон |
| Dan Gore, Anabell Skoge, Margaret Connerly, Timmy, Carla Baker | Дэн Гор, Анабелл Скоуг, Маргарет Коннерли, Тимми, Карла Бейкер |
| coroner | коронер (придуманное имя — Хэл Бреннан, Р-150) |
| Handout | раздатка (как в записях базы; официальная форма — «наглядные материалы») |
| Keeper’s Note | Хранителю на заметку |
