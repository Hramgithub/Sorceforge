# New Tales of the Miskatonic Valley (2E) — часть malice: «Malice Everlasting» («Вечная злоба»), с. 101–120

Сборник «New Tales of the Miskatonic Valley», 2-е изд. (Stygian Fox, 2019). Печатная страница = физической
(смещение 0; сверено по изображениям с. 101, 119, 171). Русского перевода сценария в базе нет (поиск по Чандлеру,
Ронни Пайну, Норме Фарр, Дому Фантов, Амулету Дамиетты в `kb/books/*-ru/` — пусто) — записи по английскому
оригиналу, русский текст — наш перевод (`translated`, Р-251, Р-21). Эпоха — `1920s` (год не назван; по тексту и
раздатке 4 — около 1928, вывод Р-41).

Записи: `kb/books/new-tales-miskatonic-valley-2e-en/` — 87 файлов: сценарий 1, сцены 16, персонажи 28, существа 3,
места 29, карты 2, раздатки 6, предметы 6, книга Мифов 1. Картинки: 7 (`art-malice.json`, применены: 6 раздаток из
приложения, иллюстрация газетчика у Ронни Пайна); карты — `app/maps/newtales-malice-kingsport-neighbourhoods.jpg`,
`app/maps/newtales-malice-funt-house.jpg`. Атмосфера и копии раздаток в тексте — `atmosphere-malice.json`.
Предложения к общим записям — `proposals-malice.json` (8: Кингспорт, Аркхэмская психбольница, «Откровения Гла’аки»).
Генератор и вспомогательные скрипты — `.cache/lead-tools/gen-newtales/malice/`.

## Заголовки книги

Префикс id: `new-tales-miskatonic-valley-2e-en/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Malice Everlasting (титул, вступление) | 101 | `scenario/malice-everlasting` (summary); `scene/malice-introduction` |
| Keeper Information | 101–102 | `scenario/malice-everlasting` (keeper_info); `character/matthew-chandler`, `character/ronnie-pine`, `location/funt-house` (history) |
| Investigator Information | 102 | `scenario/malice-everlasting` (hook); `scene/malice-introduction` |
| Kingsport (семь районов) | 102 | `scene/malice-introduction`; районы `location/kingsport-*` (7); `map/kingsport-neighbourhoods` |
| Part One: Elusive Links | 102 | `scene/malice-the-victims` |
| Simon McDonald | 103 | `character/simon-mcdonald`, `character/miriam-mcdonald` |
| Bernard White | 103 | `character/bernard-white` |
| John Placard | 103 | `character/john-placard`, `character/virginia-placard`, `character/abigail-waite` |
| Scott Forrester | 103 | `character/scott-forrester`, `character/martha-forrester`, `location/first-marine-bank` |
| Information Gained | 103 | `scene/malice-the-victims` |
| The Paperboy | 103–104 | `scene/malice-the-paperboy`; `character/ronnie-pine`; `location/kingsport-chronicle-offices` |
| The Paperboy’s Red Herring | 104 | `scene/malice-the-paperboy`; `item/paperboy-camera-film` |
| Иллюстрация: газетчик у больницы | 104 | картинка `character/ronnie-pine` |
| Police and Doctors | 106 | `scene/malice-police-and-doctors`; `character/tristram-crane`, `character/matthew-harris`; `location/kingsport-police-department`, `location/congregational-hospital` |
| Part Two: A Window into the Past | 106 | `scene/malice-public-library` |
| Monstrous Minions | 106 | `scene/malice-public-library`; `item/the-sack`, `creature/children-of-ygolonac`, `creature/malice-fire-vampire` |
| Researching the Victims | 106 | `scene/malice-public-library` |
| Kingsport Public Library | 106 | `location/kingsport-public-library`; `character/letitia-comstock`; `handout/malice-papers-3-century-by-the-sea` |
| A Possible Attack at the Library | 106 | `scene/malice-public-library`; `character/letitia-comstock` |
| Talbot Hall | 106–107 | `location/talbot-hall`; `character/wanda-drake`; `scene/malice-talbot-hall` |
| Victims’ Bloodlines | 107 | таблица «Поиски в Толбот-холле» (`location/talbot-hall`, ссылка из сценария) |
| The Appleton Bloodline | 107 | там же; `character/wallace-appleton` |
| The Warlock’s Home | 107 | там же; `handout/malice-papers-4-abstract-of-title`; `location/funt-house` |
| The Funt House, The Real Story | 108 | таблица «Дом Фантов: правдивая история» (`location/talbot-hall`); `location/funt-house` (history) |
| A Certain Attack at Talbot Hall | 108 | `scene/malice-talbot-hall`; `creature/children-of-ygolonac` (вариант 4) |
| Kingsport Historical Society Museum | 108 | `location/kingsport-historical-society-museum`; `character/aaron-hart`; `scene/malice-historical-society` |
| The Attic | 108 | `scene/malice-historical-society`; `handout/malice-papers-5-trial-record` |
| A Fatal Fire | 108, 110 | `scene/malice-fatal-fire` (иллюстрация с. 110 — атмосфера) |
| The Attic Window Option | 110 | `scene/malice-fatal-fire` |
| The Second Floor Option | 110 | `scene/malice-fatal-fire` |
| Defeating the Fire Vampire | 111 | `scene/malice-fatal-fire`; `creature/malice-fire-vampire` |
| The Fire’s Aftermath | 111 | `scene/malice-fatal-fire`; `character/nolan-paxson` |
| Part Three: The Final Threads | 111 | `scene/malice-further-red-herrings` |
| Further Red Herrings | 111 | `scene/malice-further-red-herrings` |
| The Paperboy’s Camera | 111 | `scene/malice-further-red-herrings`; `item/paperboy-camera-film` |
| Dockside Hunt | 112 | `scene/malice-dockside-hunt`; `location/derby-warehouse`; `character/derby-hoboes` |
| Melvin Wade, Red Herring | 112 | `character/melvin-wade`; `scene/malice-dockside-hunt` |
| Silencing the Red Herring | 112 | `scene/malice-dockside-hunt`; `creature/children-of-ygolonac` (вариант 16) |
| Wallace Appleton | 112–113 | `character/wallace-appleton`, `character/charles-appleton-butler`; `location/appleton-residence`; `scene/malice-wallace-appleton` |
| The Family Heirlooms | 113 | `scene/malice-wallace-appleton`; `location/appleton-residence` |
| The Amulet of Damietta | 113 | `item/amulet-of-damietta` |
| The Bible of David Appleton | 113 | `tome/appleton-bible`; `character/david-appleton` |
| The Appleton Bible – Journal Notes (врезка) | 113 | `tome/appleton-bible` (reading) |
| Part Four: The Hand of Vengeance | 113 | `scene/malice-funt-house`; `location/kingsport-hilltown` |
| The Dark Story | 113–114 | `scene/malice-funt-house`; `character/matthew-chandler`, `character/julia-pine` |
| Enter Norma Farr | 114–115 | `character/norma-farr`; `character/sanitarium-catatonic-patients` |
| The Funt House | 115 | `location/funt-house`; `scene/malice-funt-house` |
| Talking to Ronnie Pine | 115 | `scene/malice-funt-house`; `character/ronnie-pine` |
| Inside the Funt House: The Living Room | 115 | `location/funt-house-living-room`; `item/silver-seahorse-invoice` |
| The Dining Room | 115 | `location/funt-house-dining-room` |
| The Kitchen | 115 | `location/funt-house-kitchen`; `item/funt-house-kitchen-box` |
| The Bathroom | 116 | `location/funt-house-bathroom` |
| The Master Bedroom | 116 | `location/funt-house-master-bedroom` |
| The Guest Room | 116 | `location/funt-house-guest-room` |
| The Basement | 116 | `location/funt-house-basement` |
| План Дома Фантов (копия в тексте) | 116 | `map/funt-house` (картинка — из приложения, с. 193) |
| The Temple of Y’golonac | 116–117 | `location/temple-of-ygolonac`; `scene/malice-temple-of-ygolonac` |
| The Sack and The Children of Y’golonac | 117 | `item/the-sack`; `creature/children-of-ygolonac`; `scene/malice-temple-of-ygolonac` |
| The Warlock Reborn | 117 | `scene/malice-temple-of-ygolonac`; `character/ronnie-pine` |
| Kill Ronnie Pine | 117 | `scene/malice-temple-of-ygolonac` |
| Use the Amulet of Damietta | 117 | `scene/malice-temple-of-ygolonac`; `item/amulet-of-damietta` |
| Part Five: Hell Hath No Fury | 117 | `scene/malice-the-plan` |
| The Plan | 117 | `scene/malice-the-plan`; `item/chandler-severed-hand` |
| Terror on Cabot Wharf | 118 | `scene/malice-cabot-wharf`; `location/cabot-wharf`, `location/silver-seahorse` |
| Defeating Y’golonac | 118 | `scene/malice-cabot-wharf`; `creature/malice-ygolonac` |
| Destroying the Hand | 118 | `scene/malice-destroying-the-hand`; `item/chandler-severed-hand` |
| The Fate of Ronnie and Julia Pine | 118 | `scene/malice-destroying-the-hand`; `character/julia-pine` |
| Rewards and Repercussions | 118 | `scenario/malice-everlasting` (conclusion) |
| NPCs and Monsters | 119 | статблоки ниже |
| Ronnie Pine, Possessed Teen | 119 | `character/ronnie-pine` |
| The Children of Y’golonac (4) / (16) / (unlimited) | 119 | `creature/children-of-ygolonac` (варианты) |
| Fire Vampire | 119 | `creature/malice-fire-vampire` |
| Norma Farr, Loyal Accomplice | 119 | `character/norma-farr` |
| Y’golonac, Great Old One | 119 | `creature/malice-ygolonac` |
| The Neighbourhoods of Kingsport (карта) | 120 | `map/kingsport-neighbourhoods` |
| Malice Everlasting Papers #1 | 102, 171 | `handout/malice-papers-1-student-struck-blind` |
| Malice Everlasting Papers #2 | 103, 171 | `handout/malice-papers-2-another-man-suffers-blindness` |
| Malice Everlasting Papers #3 | 105, 172 | `handout/malice-papers-3-century-by-the-sea` |
| Malice Everlasting Papers #4 | 107, 173 | `handout/malice-papers-4-abstract-of-title` |
| Malice Everlasting Papers #5 (протокол суда) | 109, 174 | `handout/malice-papers-5-trial-record` |
| Malice Everlasting Papers #5 (Библия Эпплтона) | 114, 175 | `handout/malice-papers-5-appleton-journal` |
| The Funt House (план приложения) | 193 | `map/funt-house` (23 метки) |

Карты с. 179–192 приложения к «Вечной злобе» не относятся (Mother’s Love, Wasted Youth, Reeling Midnight, Spirit of
Industry, Proof of Life); единственная карта части в приложении — с. 193.

## Не взято

- Исторические владельцы Дома Фантов (Харрисон Чандлер, Томас Колдерсон, Кеннет Обер, Брайан, Эмма и Сандра Фант,
  Уилсон Винтон), рыбаки 1692 года (Сэмюэл Форрестер, Джейкоб Макдональд, Гудвайн Уайт, Джеймс Плакард), журналист
  Стэнли Картер, приёмщик фотоателье — отдельных записей нет: только имена в истории; текст — в `location/funt-house`
  (history), таблице Толбот-холла, раздатках и записях потомков.
- Лодка «Мелани Роуз», верфь «Ф. У. Иллсли и сыновья», пожарная команда Кингспорта, ливнёвый сток — упоминания без
  описания; остаются текстом в записях.
- Обрывки чужих газетных заметок вокруг раздаток 1–2 (оформление), обрывки слов по краям разрывов раздатки 5,
  карандашная пометка на раздатке «5» (с. 175) — не транскрибированы (пометки в `quality.notes`).
- Отметки масштаба «3ft Wide», «5ft Wide» на плане Дома Фантов — без меток.
- Атмосфера и копии раздаток в тексте главы — `atmosphere-malice.json`.

## Опечатки и расхождения книги

- Раздатка «#5» напечатана дважды: протокол суда (с. 109, 174) и дневник Эпплтона (с. 114, 175) — errata в
  `handout/malice-papers-5-appleton-journal`.
- «Ollie Matlock» (с. 115) вместо «Ollie Mattock» — errata в `character/ronnie-pine`.
- «Mathew Chandler» (с. 108, 111, 115, 117) вместо «Matthew» — errata в `character/matthew-chandler`.
- Уоллес Эпплтон: 37 лет (с. 107) и 29 лет (с. 112) — errata, в записи 29.
- Скотт Форрестер: текст — ослеп в обед 5 ноября, «день назад»; раздатка 2 — «позавчера вечером, дома за газетой».
- Раздатка 4 против текста: покупка дома Пайнами 1912 (текст — въезд 1913), наследство Джулии 1920 (по тексту отец
  погиб, когда Ронни было 10, т. е. около 1925); Колдерсон: регистрация 1747/1750 и продажа 1774, по тексту съехал в 1752.
- Анахронизм: «полный комплект „Откровений Гла’аки“» в храме, заложенном в 1692 году (книга издана с 1842) — errata в
  `location/temple-of-ygolonac`.
- Статблок Ронни: урон оружия против таблицы «Книги хранителя» (.38 — 1d8 вместо 1d10, нож 1d6, дубинка 1d3).
- Дети И’голонака: «DB: N/A» при Комплекции −2; вариант (4) с Уклонением 20% против 25% у других.
- Огненный вампир: «85% 42/17)» — скобка восстановлена молча (Р-39).
- И’голонак: БкУ +2d6 / Комплекция 3 при СИЛ + ТЕЛ 250 — как в Malleus, не правлено.
- «Dockside» (с. 111–112) — не один из семи районов; по тексту — Харборсайд (псевдоним района).
- David Appleton: в тексте — «пятый член команды» рыбаков, в раздатке 3 — преподобный, организатор отряда.
- Раздатка 1 называет Макдональда пациентом больницы, по тексту он дома.

## Термины (English → русский)

| English | Русский |
|---|---|
| Malice Everlasting | Вечная злоба |
| Two Tales of Kingsport (колонтитул) | Две истории Кингспорта |
| Malice Everlasting Papers #N | Раздатка «Вечная злоба» N |
| Elusive Links | Неуловимая связь |
| A Window into the Past | Окно в прошлое |
| The Final Threads | Последние нити |
| The Hand of Vengeance / the hand of vengeance | Рука мщения |
| Hell Hath No Fury | Нет ярости страшнее |
| warlock | колдун |
| witch hysteria | охота на ведьм |
| Kingsport — A Century by the Sea | «Кингспорт: столетие у моря» |
| Kingsport Chronicle | «Кингспорт кроникл» (редакция «Кингспорт кроникл») |
| Harborside / Dockside | Харборсайд / доки |
| The Hollow | Холлоу |
| Central Hill | Централ-Хилл (как в общей записи Кингспорта) |
| Southshore / South Shore | Саутшор |
| Downtown (Kingsport) | Даунтаун (запись — «Даунтаун Кингспорта») |
| West Side | Уэст-Сайд |
| Hilltown / Hill Town | Хиллтаун |
| Prospect Hill | Проспект-Хилл |
| The Neighbourhoods of Kingsport | Районы Кингспорта |
| Congregational Hospital | Конгрегационалистская больница |
| Kingsport Police Department | Полицейское управление Кингспорта |
| Kingsport Public Library | Публичная библиотека Кингспорта |
| Talbot Hall | Толбот-холл |
| City Clerk | городской секретарь |
| Kingsport Historical Society Museum | Музей Исторического общества Кингспорта |
| First Marine Bank of Kingsport | Первый морской банк Кингспорта |
| F.W. Illsley & Sons | верфь «Ф. У. Иллсли и сыновья» |
| Kingsport Fire Department | пожарная команда Кингспорта |
| Derby warehouse | склад Дерби |
| Cabot Wharf | пристань Кабота |
| Silver Seahorse | «Серебряный морской конёк» |
| Melanie Rose (boat) | «Мелани Роуз» |
| The Funt House | Дом Фантов |
| The Temple of Y’golonac | Храм И’голонака |
| Restraint Area / Summoning Area / Temple (план) | место для пленников / место призыва / храм |
| Arkham Sanitarium | Аркхэмская психбольница (общая запись) |
| dementia ward | отделение для слабоумных |
| Children of Y’golonac | Дети И’голонака |
| Y’golonac / Igollonack (раздатка) | И’голонак / Иголлонак |
| Great Old One | Великий Древний |
| Fire Vampire | огненный вампир |
| Shan | шаны |
| Tulzscha / Oorn | Тульцща / Оорн |
| the Sack | Мешок |
| Amulet of Damietta / Damietta / Templars | Амулет Дамиетты / Дамиетта / тамплиеры |
| The Bible of David Appleton | Библия Дэвида Эпплтона |
| mummified (severed) hand | мумифицированная (отрубленная) рука |
| Abstract of Title | выписка о праве собственности |
| Kodak Brownie | «Кодак Брауни» |
| Dodge Model DC truck | грузовичок «Додж» модели DC |
| Victrola | виктрола |
| Greek fishermen’s hat | греческая рыбацкая кепка |
| the mysterious sailor | таинственный моряк |
| red herring | ложный след |
| paperboy | газетчик (мальчишка-газетчик) |
| Possessed Teen / Loyal Accomplice | одержимый подросток / верная сообщница |
| Matthew Chandler | Мэттью Чандлер |
| Ronnie (Ronald) Pine / Pinéro | Ронни (Рональд) Пайн / Пинеро |
| Ollie Mattock | Олли Мэтток |
| Norma Farr | Норма Фарр |
| Julia Pine / Gabriel Pine | Джулия Пайн / Габриэль Пайн |
| Simon McDonald / Miriam | Саймон Макдональд / Мириам |
| Bernard White | Бернард Уайт |
| John Placard / Virginia Placard / Abigail Waite | Джон Плакард / Вирджиния Плакард / Эбигейл Уэйт |
| Scott Forrester / Martha | Скотт Форрестер / Марта |
| Wallace Appleton / David Appleton / Charles (butler) | Уоллес Эпплтон / Дэвид Эпплтон / дворецкий Чарльз |
| Tristram Crane | Тристрам Крейн |
| Dr. Matthew Harris | доктор Мэттью Харрис |
| Letitia Comstock | Летиция Комсток |
| Wanda Drake | Уонда Дрейк |
| Aaron Hart | Аарон Харт |
| Nolan “Smoke” Paxson | Нолан «Дымок» Паксон |
| Melvin Wade | Мелвин Уэйд |
| Stanley Carter | Стэнли Картер |
| Harrison Chandler; Thomas Caulderson; Kenneth Ober; Brian, Emma, Sandra Funt; Wilson Vinton | Харрисон Чандлер; Томас Колдерсон; Кеннет Обер; Брайан, Эмма, Сандра Фант; Уилсон Винтон |
| Samuel Forrester; Jacob McDonald; Goodwine White; James Placard | Сэмюэл Форрестер; Джейкоб Макдональд; Гудвайн Уайт; Джеймс Плакард |
| James & James Corp | «Джеймс энд Джеймс корп.» |
| Улицы: Ship, Barrel, Silver, High, Carter, Brush, Holt, Green, Hall, Caldecott, Turner, Summit, Howard, Harper, Parson | Шип-, Баррел-, Силвер-, Хай-, Картер-, Браш-, Холт-, Грин-, Холл-, Колдекотт-, Тёрнер-, Саммит-, Хауард-, Харпер-, Парсон-стрит |

Правила и навыки — по глоссарию: Know roll — проверка Знаний; Library Use — Работа в библиотеке; Spot Hidden —
Внимание; Track — Чтение следов; Jump — Прыжки; Luck roll — проверка Удачи; bonus / penalty die — бонусная / штрафная
кость; Hard — трудная проверка; Scent — Нюх; Pilot (Boat) — Пилотирование (лодка); Science (Pharmacy) — Наука
(фармакология); Cause Blindness — Наслать слепоту (запись «Наслать/исцелить слепоту»); Stop Heart — Остановка сердца;
Enthrall Victim — Околдовать жертву; Cloud Memory — Затуманить память; Nightmare — Кошмар; Summon/Bind Fire Vampire —
Призыв/укрощение огненного вампира; Call/Dismiss Y’golonac — Вызов/изгнание И’голонака (ссылка на «Вызов божества»).
