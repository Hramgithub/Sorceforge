# Nameless Horrors — часть space: «The Space Between» («Пространство между»), с. 178–227

Сборник «Безымянные ужасы» (Nameless Horrors, Chaosium, 2015), сценарий Скотта Дорварда. Печатная страница = физическая − 2
(сверено по изображениям с. 183, 206, 215). Русского перевода в базе и библиотеке нет — запись по английскому оригиналу,
русский текст — наш перевод (`translated`, Р-251, Р-21). Эпоха — `modern`.

Записи: `kb/books/nameless-horrors-en/` — 82 файла (сценарий 1, сцены 16, персонажи 27, существа 4, места 18, карты 2,
раздатка 6, предметы 6, книга Мифов 1, организация 1). Картинки: 22 (`checks/20261117-nameless/art-space.json`, вырезки
раздатки — `art-space-boxes.json`), применены; карты — `app/maps/nameless-space-woodward-penthouse.jpg`,
`app/maps/nameless-space-celebrity-retreat.jpg`. Атмосфера — `atmosphere-space.json`. Предложения к общим записям —
`proposals-space.json` (12: Лос-Анджелес, «Сассекская рукопись», два заклинания).

## Заголовки книги

Префикс id: `nameless-horrors-en/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Space Between (титул) | 178 | `scenario/the-space-between` (картинка — атмосфера) |
| Introduction | 179 | `scenario/the-space-between` (summary) |
| Pre-generated Investigators | 179 | `scenario/the-space-between` (hook); прегены — `character/*` |
| Background for the Keeper | 179 | `scenario/the-space-between` (keeper_info) |
| Origins | 179 | `scenario/the-space-between` (keeper_info); `character/ralph-l-chandler` |
| Creation of the Church of Sunyata | 179–180 | `organization/church-of-sunyata`; `character/ralph-l-chandler`, `character/brian-musgrove` |
| Chandler, hard at work (подпись) | 180 | картинка `character/ralph-l-chandler` |
| Embracing Celebrities | 180 | `organization/church-of-sunyata`; `location/celebrity-retreat`; `character/craig-steele` |
| True Emptiness | 180–181 | `character/craig-steele`; `creature/the-truly-empty`, `creature/the-emptied`; keeper_info |
| The Death of Verity Harrow | 181–182 | `character/verity-harrow`, `character/jared-woodward`; `location/basalt-cliffs-set`; keeper_info |
| Dramatis Personae | 182 | персонажи ниже |
| Tom Bolender, security guard | 182 | `character/tom-bolender` |
| Tekroop Singh, assistant director | 182 | `character/tekroop-singh` |
| Detective Samuel Neumeier, LAPD | 182 | `character/samuel-neumeier` |
| Jared Woodward, film director | 182, 184 | `character/jared-woodward` |
| Relationship Map | 183 | таблица «Схема связей» в `scenario/the-space-between`; картинка сценария (plan); связи `relations` персонажей |
| Mandy Solek, receptionist | 184 | `character/mandy-solek` |
| Verity Harrow, emptied actress, filled with the Void | 184 | `character/verity-harrow` |
| Craig Steele, truly empty actor, filled with the Void | 184–185 | `character/craig-steele` |
| Dramatis Personae (рисунок) | 185 | портреты Сингха, Масгроува, Стила, Харроу, Вудворда |
| Brian Musgrove, truly empty leader of the Church of Sunyata | 185 | `character/brian-musgrove` |
| Rich Vallario, Church member desperate to impress | 186 | `character/rich-vallario` |
| The Emptied | 186 | `creature/the-emptied` |
| The Truly Empty | 186 | `creature/the-truly-empty` |
| The Hungry Void | 186 | `creature/the-hungry-void` |
| Yvette Sommers, film character, and an Avatar of the Void | 186–187 | `creature/yvette-sommers` |
| Handout: Space 2 (копия в тексте) | 186 | `handout/space-2-you-have-been-emptied` |
| Handout: Space 3 (копия в тексте) | 187 | `handout/space-3-you-are-truly-empty` |
| The Production | 187 | `location/schriver-studios-soundstage` |
| The Soundstage | 187 | `location/schriver-studios-soundstage`, `location/basalt-cliffs-set`; `character/milt-schriver` |
| Timeline | 187 | таблица «Хронология» в `scenario/the-space-between` |
| Opening Scene | 188 | `scene/space-opening-scene` |
| Handout: Space 1A, 1B, 1B Continued (копии в тексте) | 188–189 | `handout/space-1a-overview-of-the-script`, `handout/space-1b-church-jargon`, `handout/space-1b-continued-cast-and-crew` |
| Tekroop Singh Becomes Desperate | 188 | `scene/space-singh-becomes-desperate` |
| What does the Production Crew Know about the Film? | 190 | `scene/space-opening-scene`; `item/the-space-between-film` |
| Attempting to Contact Jared Woodward | 190 | `scene/space-contacting-woodward` |
| The Police Investigation | 190–191 | `scene/space-police-investigation`; `character/dwight-greer`, `character/sonia-palermo` |
| Dealing with the Police Investigation (врезка) | 191 | `scenario/the-space-between` (advice); `character/erica-christensen` |
| Verity Harrow’s Apartment | 191–192 | `scene/space-harrow-apartment`, `location/verity-harrow-apartment`; `character/tyrone-goode` |
| Splitting the Party (врезка) | 192 | `scenario/the-space-between` (advice) |
| What does it mean to be Empty? (врезка) | 192 | `scene/space-harrow-apartment`; `creature/the-emptied`, `creature/the-truly-empty` |
| Other Ways of Bringing Harrow into Play | 192 | `scene/space-harrow-apartment` |
| Jared Woodward’s Apartment | 193 | `scene/space-woodward-apartment`, `location/woodward-penthouse`; `character/manny` |
| Woodwards Penthouse — A Domain of Despair (план) | 193 | `map/woodward-penthouse` (20 меток) |
| The Editing Suite | 193–195 | `scene/space-editing-suite`, `location/woodward-editing-suite`; `item/harrow-murder-frames`, `item/space-between-production-notes` |
| The Basalt Cliffs (врезка) | 194 | `location/basalt-cliffs`; `scene/space-editing-suite` |
| Playing One of the Emptied (врезка) | 195 | `scenario/the-space-between` (advice); способности `creature/the-emptied`, `creature/the-truly-empty` |
| Handout: Space 4 (копия в тексте) | 195 | `handout/space-4-the-truth-behind-the-space-between` |
| The Church Headquarters | 195 | `scene/space-church-headquarters`, `location/church-of-sunyata-headquarters` |
| A Free Emptying Session | 195–196 | `scene/space-free-emptying-session` |
| The Security Desk | 196 | `location/church-of-sunyata-headquarters`; `scene/space-church-headquarters`; `character/church-security-guard` |
| The Legal Department | 196 | `location/sunyata-legal-department`; `character/erica-christensen` |
| Brian Musgrove’s Office | 196, 198 | `scene/space-musgrove-office`, `location/musgrove-office`; `character/natalie-collier`; `item/void-bottle` |
| The Retreat — The Gateway to Emptiness (план) | 197 | `map/celebrity-retreat` (60 меток) |
| The Celebrity Retreat | 198 | `scene/space-celebrity-retreat`, `location/celebrity-retreat`, `location/celebrity-retreat-grounds`, `location/retreat-north-wing` |
| Reception | 198 | `location/retreat-reception`; `character/mandy-solek` |
| Security | 198 | `location/celebrity-retreat`, `location/retreat-security-office`; `character/church-security-guard` |
| The Skin of Ralph L. Chandler (подпись) | 198 | `item/skin-of-ralph-l-chandler` (картинка) |
| The Exegesis of Ralph L. Chandler (врезка) | 199 | `tome/exegesis-of-ralph-l-chandler` (картинка) |
| Craig Steele’s Private Office | 199 | `location/steele-private-office`; `scene/space-celebrity-retreat` |
| The Emptying Suites | 199 | `location/retreat-emptying-suites` |
| A Private Session with Steele | 200 | `scene/space-private-session-with-steele` |
| The Operating Theater | 200–201 | `location/retreat-operating-theatre`; `item/sigil-knives`; `scene/space-fast-track-process` |
| The Fast Track Process | 201 | `scene/space-fast-track-process`; `character/retreat-surgeon` |
| Escaping From the Celebrity Retreat; Sneaking Out; Fleeing | 201–202 | `scene/space-escaping-the-retreat` |
| The Screening Room | 202 | `location/retreat-screening-room` |
| The Test Screening | 202–203 | `scene/space-test-screening` |
| Wrapping it Up; Destroying the Film; Helping the Police | 203 | `scene/space-wrapping-it-up` |
| Exposing the Church; Attending the Test Screening; Fleeing; Distribution of the Movie | 204 | `scene/space-wrapping-it-up` |
| Conclusion (награды Рассудка) | 204 | `scenario/the-space-between` (conclusion) |
| Appendix A: Characters | 205–207 | статблоки: `character/lapd-uniformed-officer`, `character/church-security-guard`, `character/tom-bolender`, `character/tekroop-singh`, `character/samuel-neumeier`, `character/jared-woodward`, `character/mandy-solek`, `character/rich-vallario`, `character/verity-harrow`, `character/craig-steele`, `character/brian-musgrove`; `creature/the-emptied`, `creature/the-truly-empty`, `creature/the-hungry-void`, `creature/yvette-sommers` |
| Appendix B: Handouts (Space 1A, 1B, 1B Continued, 2, 3, 4) | 208–210 | `handout/space-*` (тексты как напечатаны + перевод, картинки-вырезки) |
| Appendix C: Pre-Generated Player Investigators | 210 | список — `scenario/the-space-between` (hook) |
| Spencer Shull | 211 | `character/spencer-shull` |
| Julia Cortese | 212 | `character/julia-cortese` |
| Amanda Stennett | 213 | `character/amanda-stennett` |
| Blake Tevis | 214 | `character/blake-tevis` |
| David Otera | 215 | `character/david-otera` |
| Daria Nowland | 216 | `character/daria-nowland` |
| Expanded Contents | 217–219 | не взято (см. ниже) |
| Author Biographies | 220 | не взято (см. ниже) |
| Реклама, логотип, задняя обложка | 221–226 | атмосфера; аннотация «The Space Between» с задней обложки — в summary сценария |

## Не взято

- Expanded Contents (с. 217–219) — оглавление книги, указатель без игрового материала (по общей схеме книги отмечается здесь); использовано для сверки заголовков.
- Author Biographies (с. 220) — биографии авторов (Дорвард, Фрикер, Сандерсон), не игровой материал; ведущему решить, нужен ли текст в записи сборника.
- С. 221–227: реклама Chaosium Fiction и линейки 7e, логотип, пустые страницы — не игровой материал (картинки — в `atmosphere-space.json`).
- Строка-заглушка «Gite libusdaest, niet dus.» в приложении C (с. 210) — опечатка вёрстки, не перенесена (пометка у Дарии Ноуленд).
- Атмосферные иллюстрации без записи: титул (с. 178), ритуал (с. 181), «A Private Session with Steele», «An Emptying Suite» (с. 200), «The Fast Track to becoming Empty» (с. 201), «The Test Screening», знак (с. 203), украшения (с. 204, 207) — `atmosphere-space.json`.
- Упомянутые без записи (текстом): бездомная, нашедшая тело; дежурный врач клиники Ретрита; билетёры показа; зритель, колотящий в дверь; дядя Эл Шалла; персонажи фильма Кларисса Холлоуз и Трент (в раздатке 1A/1B и сценах); места из предысторий прегенов (клуб «Рауль», лодка «Афина», сок-бар в Креншо, кабинет Шалла — в описаниях); ливневый сток у павильона (в описании павильона и сценах); книга «Му: научный подход к просветлению» (не Мифов — в легенде Чандлера).
- Комнаты планов без текста книги (гостиная, бальный зал, кухня, спальни и т. п.) — метки карт ведут на здание с пояснением `text`, отдельных записей нет.

## Опечатки и сомнения

- Внутренние ссылки книги на страницы сдвинуты на +4 по всему сценарию («Relationship Map on page 187» → с. 183; «Verity Harrow, page 188» → 184; «pages 190 and 210» → 186 и 206; «Church Security Guard (page 209)» → 205; «page 204/205» → 200/201; «Appendix C … page 214» → 210). В записях — верные страницы; пометки в `quality.notes`.
- Брайан Масгроув: ПЗ 8 (по правилам 9), БкУ −1 при СИЛ+ТЕЛ 85 (по правилам 0); возраст 63 в статблоке против «mid-fifties» в описании — `errata`, как напечатано.
- Верити Харроу: Комплекция 0 при СИЛ+ТЕЛ 75 (по правилам −1) — `errata`.
- Крейг Стил: Скорость 7 (по правилам 8, с поправкой на 58 лет — 6) — `errata`.
- Блейк Тевис: Уклонение «35% (17/05)» — пятая доля исправлена на 7 (`errata` fixed, `corrections`, Р-35).
- Дэвид Отера: нет строки навыков; Уклонение 22% при ЛВК 70 — `errata`, флаг `incomplete`.
- «Amanda Stenett» в раздатке 1B (с. 189, 209) против «Stennett» на листе сыщика — `errata` раздатки, псевдоним у сыщика.
- Раздатка 4 в приложении: «bring this of Emptiness», «contact from an intelligence» (в копии с. 195 — без опечаток); «examinining» (1A), «hold on you who you are» (2), «boxed test» (с. 194), «sta editing nd out» (с. 195, сбой вёрстки) — словесные, при переводе исчезают.
- Тестовый показ назначен на 20:00, а Солек зовёт гостей в зал в 21:00 — как напечатано (пометка в сцене).
- Сомнения (наш выбор): `category` Голодной Пустоты — `mythos_deity` (книга: «godlike entity», есть аватар); Опустошённые и Истинно Пустые — `supernatural`; «Открыватель Пути» (Opener of the Way) в базе — титул Йог-Сотота, книга прямо не связывает его с Голодной Пустотой; Церковь Шуньяты — `org_type` «культ»; базальтовые утёсы (иная реальность) — `part_of` Лос-Анджелес. В «Аркхэме» (Arricurals of Passing) тоже упомянута «Hungry Void» — связь не установлена.

## Термины (английский → русский)

| English | Русский |
|---|---|
| Nameless Horrors | «Безымянные ужасы» |
| The Space Between (сценарий и фильм) | «Пространство между» |
| Church of Sunyata | Церковь Шуньяты |
| Sunyata | Шуньята |
| Sunyata Central | Шуньята-Центр |
| Woes | Горести |
| Empty | Пустой |
| Emptying | Опустошение |
| Emptying session / Emptying suite | сеанс Опустошения / комната Опустошения |
| Full | Полный |
| Shadows | Тени |
| Infections | Инфекции |
| Cleansing | Очищение |
| the Emptied | Опустошённые |
| the Truly Empty / Truly Empty | Истинно Пустые / Истинно Пустой |
| the Hungry Void | Голодная Пустота |
| Tendrils of the Void | Щупальца Пустоты |
| Emptying Touch | Опустошающее касание |
| Avatar of the Void | аватар Голодной Пустоты |
| The Fast Track Process | «Ускоренный путь» |
| Celebrity Retreat | Ретрит знаменитостей |
| The Basalt Cliffs | базальтовые утёсы |
| The Exegesis of Ralph L. Chandler | «Экзегеза Ральфа Л. Чандлера» |
| Mu: A Scientific Approach to Enlightenment | «Му: научный подход к просветлению» |
| Gateway to the Void | «Врата в Пустоту» (= Вызов/изгнание Йог-Сотота) |
| Commune with the Bringer of Wisdom | «Общение с Приносящим Мудрость» (= Связь с Ньярлатхотепом) |
| Opener of the Way | Открыватель Пути (как в записи Йог-Сотота) |
| Schriver Studios | «Шрайвер Студиос» |
| soundstage | павильон |
| rough cut | черновой монтаж |
| test screening | тестовый показ |
| Steenbeck editing desk | монтажный стол «Стенбек» |
| The Hollywood Tattler | «Голливуд Таттлер» |
| Relationship Map | схема связей |
| Ralph L. Chandler; Brian Musgrove; Craig Steele; Jared Woodward; Verity Harrow | Ральф Л. Чандлер; Брайан Масгроув; Крейг Стил; Джаред Вудворд; Верити Харроу |
| Yvette Sommers; Clarissa Hollows; Trent | Иветт Соммерс; Кларисса Холлоуз; Трент |
| Tom Bolender; Tekroop Singh; Samuel Neumeier; Mandy Solek; Rich Vallario | Том Болендер; Текруп Сингх; Сэмюэл Ноймайер; Мэнди Солек; Рич Валларио |
| Dwight Greer; Sonia Palermo; Tyrone Goode; Erica Christensen; Natalie Collier; Manny; Milt Schriver; Harry Malloy | Дуайт Грир; Соня Палермо; Тайрон Гуд; Эрика Кристенсен; Натали Кольер; Мэнни; Милт Шрайвер; Гарри Маллой |
| Spencer Shull; Julia Cortese; Amanda Stennett; Blake Tevis; David Otera; Daria Nowland | Спенсер Шалл; Джулия Кортезе; Аманда Стеннетт; Блейк Тевис; Дэвид Отера; Дария Ноуленд |
| Havenhurst Drive; Ventura Boulevard; West Hollywood; San Fernando Valley; Hollywood Hills | Хейвенхёрст-драйв; бульвар Вентура; Западный Голливуд; долина Сан-Фернандо; Голливудские холмы |

Придуманные имена (Р-150, Р-151, `editorial_text`): хирург Ретрита — доктор Нил Эрдман; имена групповых профилей патрульных и охранников Церкви.
