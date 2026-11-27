# HOTOE, часть modern — книга IV, с. 127–168, 187–192 (2026-11-27)

«The Simulacrum Unbound: Istanbul 2013» (Майк Мейсон при участии Пенелопы Лав), этап
`hotoe-book-4-en/scenario/the-simulacrum-unbound` (`part_of` кампании, `order` 19, необязательный, эпоха `modern`).
Источники: `hotoe-book-4-en` (печатная = физическая − 2), `hotoe-book-6-handouts-en` с. 173–179, 189 (копии для игроков).
Русский текст — наш перевод (флаг `translated`, Р-251). Решения: Р-254, Р-251, Р-252, Р-190, Р-189, Р-206, Р-125, Р-126, Р-161.

## Записи (76)

| Вид | Записи |
|---|---|
| scenario (1) | `the-simulacrum-unbound` (таблицы «Жертвы и части тела», «Таймлайн событий», «Награды») |
| scene (21) | `modern-all-aboard`, `modern-who-cooked-this`, `modern-budapest-hilton`, `modern-guided-tour`, `modern-a-request-for-help`, `modern-the-murderer-prepares`, `modern-the-ritual-goes-wrong`, `modern-echoes-of-the-past`, `modern-sample-echoes`, `modern-the-first-murders`, `modern-the-missing-train`, `modern-discovering-the-murders`, `modern-murders-3-4-5`, `modern-a-vital-clue`, `modern-wilson-confronts-antin`, `modern-investigating-the-murderer`, `modern-milton-captured`, `modern-victim-6`, `modern-milton-creates-the-gate`, `modern-showdown-at-the-shunned-mosque`, `modern-possibilities` |
| character (17) | со статблоком (15): `john-milton`, `giuseppe-roti`, `john-walters`, `enzo-banuelos`, `oscar-griffin`, `faustino-gonzaga`, `antonio-abella` (он же Анджело Минотти), `chantel-antin`, `henri-guillemette`, `merissa-ocana`, `wanda-zeigler`, `lars-farber`, `mark-wilson`, `fabian-wyss`, `rene-violet`; без статблока (2): `jacques-cote`, `didier-lagoy` |
| creature (2) | `modern-faceless-soldiers`, `modern-meat-simulacrum` |
| location (16) | поезд `modern-orient-express` (корабль; таблицы «Состав поезда», «Аварийное снаряжение») и вагоны `modern-salon-bar-car-e`, `modern-restaurant-car-la-saveur-dasie`, `modern-restaurant-car-la-cote`, `modern-sleeping-car-f`, `modern-sleeping-car-g`, `modern-fourgon-luggage`; `modern-the-other-place` (область под поездом) с `modern-other-place-forest`, `modern-other-place-train-tunnel`; Стамбул 2013 (под `coc:location:constantinople`): `modern-sirkeci-station` (1), `modern-park-hyatt-hotel` (2), `modern-basilica-cistern` (5), `modern-sultan-ahmet-park` (7), `modern-shunned-mosque` (11) и `modern-shunned-mosque-main-hall` |
| item (7) | `modern-the-diary`, `modern-miltons-journal`, `modern-miltons-spell-components`, `modern-chalk-drawings`, `modern-stolen-shirts`, `modern-suitcase-of-body-parts`, `modern-wilsons-stalker-kit` |
| handout (6) | `modern-handout-1-profile-john-milton`, `-2-sample-menu`, `-3-orient-express-itinerary`, `-4-lovely-chantel`, `-5-dearest-chantel`, `-6-miltons-journal` (картинки — кн. VI) |
| organization (1) | `modern-lux-vista` |
| rule (1) | `modern-miltons-spells-quick-reference` (таблица девяти заклинаний) |
| map (4) | `modern-istanbul-today` (с. 140/188, 19 меток), `modern-istanbul-today-players` (с. 189, кн. VI с. 189, 18 меток), `modern-shunned-mosque` (с. 160, 10 меток), `modern-sleeper-cars` (с. 142 и 187, 16 меток) |

Картинки: карты `app/maps/hotoe-modern-*.jpg` (4); раздатка `app/art/handouts/hotoe-modern-handout-1…6.webp` (сопоставление
`art-modern.json`, предложения `art-modern-proposals.json` применены). Портретов в главе нет (большие картинки на с. 129, 130,
135, 141, 150, 157, 168 — фоны врезок и рамка раздатки). Атмосферные иллюстрации — `atmosphere-modern.json` (4 страницы).
Предложения к чужим и общим записям — `proposals-modern.json` (10, пробный прогон ложится). Черновик общего города —
`new-shared-locations-modern.json` (Будапешт). Скрипты — `.cache/lead-tools/gen-hotoe-modern/` (`gen_*.py`, `maps.py`, `art_crops.py`).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Simulacrum Unbound (титул, подзаголовок, авторы) | 127 | этап `the-simulacrum-unbound`: `name`, `summary` |
| An Optional Sequel (врезка) | 127 | этап: `advice`; сцена `modern-echoes-of-the-past` |
| Keeper Information | 127–128 | этап: `keeper_info`; `john-milton` |
| Investigator Information | 128 | этап: `hook`; `modern-lux-vista` |
| Keeper's Information About John Milton | 128–130 | `john-milton` `legend`; этап `keeper_info`; копия «Некрономикона» — предложение к `coc:tome:necronomicon-english` |
| Modern Handout #1 (Profile—John Milton) | 129 | раздатка `modern-handout-1-profile-john-milton` |
| The Diary (врезка) | 130 | предмет `modern-the-diary`; этап `keeper_info` |
| Using The Express Diaries (врезка) | 130 | `modern-the-diary`; этап `advice` |
| Unexpected Consequences | 130 | этап `keeper_info`; сцена `modern-the-ritual-goes-wrong` |
| Player Characters | 131 | этап `hook` |
| The Modern Train | 131–132 | поезд `modern-orient-express` |
| The Journey | 132 | поезд `description` |
| Configuration | 132 | поезд, таблица «Состав поезда»; вагоны `modern-*` |
| Dining; What To Wear? | 132–134 | поезд `description`; вагоны-рестораны |
| Modern Handout #2 (Sample Menu); Sample Menus | 133–134 | раздатка `modern-handout-2-sample-menu`; поезд |
| Washing facilities; Luggage; Languages; Currency | 134 | поезд `description` |
| Emergency Equipment | 134 | поезд, таблица «Аварийное снаряжение» |
| Communications On The Train | 134–135 | поезд `description` («Связь») |
| John Milton (статблок, Backstory, Notes) | 135 | `john-milton` |
| Passengers From London | 135 | поезд `description`; этап, шаг «Пролог» |
| Customs And Immigration | 136 | поезд `description` |
| The Six Body Parts; Victims and body parts | 136 | этап, таблица «Жертвы и части тела»; `keeper_info` |
| Competition Winners: Giuseppe Roti, John Walters, Enzo Banuelos, Oscar Griffin, Faustino Gonzaga | 136–137 | персонажи |
| Replacement Player Characters (врезка) | 137 | этап `advice` |
| Antonio Abella (AKA Angelo Minotti) | 138 | `antonio-abella` |
| Additional Characters: Chantel Antin, Henri Guillemette, Merissa Ocana, Wanda Zeigler, Lars Färber, Mark Wilson, Fabian Wyss | 138–141 | персонажи; этап `advice` |
| Istanbul Today (карта) | 140 | карта `modern-istanbul-today` (источник) |
| Train Staff; Rene Violet | 141 | `rene-violet`; поезд |
| Modern Handout #3 (Orient Express Itinerary) | 141 | раздатка `modern-handout-3-orient-express-itinerary` |
| Sleeper F / Sleeper G (схемы вагонов) | 142 | карта `modern-sleeper-cars`; вагоны F и G (`residents`) |
| 2013 Train Itinerary | 142 | раздатка 3 (`description`) |
| Timeline Of Events; Day 1–Day 5 (таймлайн) | 142–143 | этап, таблица «Таймлайн событий» |
| Day 1 - Friday 30 August; All Aboard!; Welcome To The Orient Express; Dinner | 144–145 | сцена `modern-all-aboard` |
| Day 2 – Saturday 31 August; Who Cooked This? | 145 | сцена `modern-who-cooked-this`; вагон `modern-restaurant-car-la-cote` |
| Budapest | 145–146 | сцена `modern-budapest-hilton`; черновик `coc:location:budapest` |
| Day 3 – Sunday 1 September; The Guided Tour | 146–147 | сцена `modern-guided-tour`; черновик Будапешта |
| A Request For Help; Modern Handout #4 | 147–148 | сцена `modern-a-request-for-help`; раздатка `modern-handout-4-lovely-chantel` |
| The Murderer Prepares; Who's Been In My Cabin? | 148–149 | сцена `modern-the-murderer-prepares`; предметы `modern-chalk-drawings`, `modern-stolen-shirts` |
| Machinations of Nyarlathotep? (врезка) | 149 | место `modern-the-other-place`; сцена `modern-the-ritual-goes-wrong`; этап `keeper_info` |
| The Ritual Goes Wrong | 149–150 | сцена `modern-the-ritual-goes-wrong` |
| The Other Place | 150–151 | место `modern-the-other-place`; сцена `modern-echoes-of-the-past` |
| Echoes of the Historical Past (врезка) | 150 | сцена `modern-echoes-of-the-past` (пять исторических событий) |
| (отголоски 1923 года, Мифы Ктулху и Оккультизм) | 151 | сцена `modern-echoes-of-the-past`; место `modern-the-other-place` |
| Sample Echoes Of The Other Place: Looking Out Of The Window; Leaving The Train – Via The Embankment; Faceless Soldiers (статблок); The Forest's Edge | 152 | сцена `modern-sample-echoes`; существо `modern-faceless-soldiers`; место `modern-other-place-forest` |
| Leaving The Train – Following The Train Track; Turning On The Taps; Checking The Luggage; The Crying Child; Realizing They Are Trapped | 153 | сцена `modern-sample-echoes`; место `modern-other-place-train-tunnel` |
| The First Murders | 153 | сцена `modern-the-first-murders`; предмет `modern-suitcase-of-body-parts` |
| Running Events To The Conclusion | 153–154 | сцена `modern-murders-3-4-5`; этап `advice` |
| Day 4 – Monday 2 September; The Missing Train | 154–155 | сцена `modern-the-missing-train` |
| Discovering The Murders; Bloody Clothing | 155–156 | сцена `modern-discovering-the-murders`; `fabian-wyss`; `modern-stolen-shirts` |
| Modern Handout #5 | 156 | раздатка `modern-handout-5-dearest-chantel` |
| Murders 3, 4 and 5 | 156 | сцена `modern-murders-3-4-5` |
| A Vital Clue | 156 | сцена `modern-a-vital-clue`; `modern-the-diary` |
| Wilson Confronts Antin | 156, 158 | сцена `modern-wilson-confronts-antin` |
| Modern Handout #6 (Excerpts One–Three) | 157 | раздатка `modern-handout-6-miltons-journal`; таблица «Жертвы и части тела» (ниши) |
| Investigating The Murderer; Milton's Journal; Stolen Shirts; Spell Components | 158–159 | сцена `modern-investigating-the-murderer`; предметы `modern-miltons-journal`, `modern-stolen-shirts`, `modern-miltons-spell-components` |
| Using the Create Gate Spell (врезка) | 159 | `modern-miltons-journal` `mechanics`; сцена `modern-investigating-the-murderer` |
| Milton Captured? | 159–160 | сцена `modern-milton-captured` |
| The Shunned Mosque (план) | 160 | карта `modern-shunned-mosque`; места мечети |
| Day 5 – Tuesday 3 September; Victim 6 | 160 | сцена `modern-victim-6` |
| Milton Creates The Gate | 160–161 | сцена `modern-milton-creates-the-gate` |
| Showdown At The Shunned Mosque; The Shunned Mosque | 161–162 | сцена `modern-showdown-at-the-shunned-mosque`; места `modern-shunned-mosque` (`history`), `modern-shunned-mosque-main-hall`; абзац 2013 года — предложение к `coc:location:constantinople` |
| The Ritual of Enactment; The Meat Simulacrum; Meat Simulacrum (статблок) | 162–163 | сцена `modern-showdown-at-the-shunned-mosque`; существо `modern-meat-simulacrum` |
| Possibilities; Conclusion | 163 | сцена `modern-possibilities`; этап `conclusion` |
| Rewards | 163 | этап, таблица «Награды», `conclusion` |
| Statistics; Non-Player Characters; NPC Key; Lux-Vista Competition Winners; Other Passengers; Train Staff; The Murderer | 164–167 | статблоки персонажей (источник «статблок»); «NPC Key» — общая подсказка формата, не взята отдельно |
| Milton's Spells - Quick reference | 168 | правило `modern-miltons-spells-quick-reference` |
| Sleeper F / Sleeper G (схемы вагонов в «Complete Maps», повёрнуты; по указанию ведущего) | 187 | карта `modern-sleeper-cars` (второй источник; картинка — с. 142, та же схема) |
| Istanbul Today Keeper's Map | 188 | карта `modern-istanbul-today` (картинка) |
| Istanbul Today Players' Map | 189 | карта `modern-istanbul-today-players` |
| Index of Significant & Useful Entries | 190–192 | не взято |

## Не взято

- Указатель книги IV (с. 190–192, «Index of Significant & Useful Entries») — указатель по страницам, данных нет.
- «NPC Key» (с. 164) — пояснение формата строки атаки (общий формат статблоков 7e), отдельной записи нет.
- Ссылка на сайт компании (www.orient-express.com/…, с. 132) и сайт лабиринта (www.labirintus.com, с. 147) — внешние адреса.
- Книга Ширли Шервуд «Venice Simplon Orient-Express: the return of the world's most celebrated train» (1983) — упоминание в истории поезда (текст в `modern-orient-express`), без записи.
- Подписи карты «Стамбул сегодня» Eminönü, Ortaköy, Beşiktaş, Sea of Marmara, To Greece, значки станций и порты — без меток: записей нет, текст их не описывает.
- Вагоны состава, не участвующие в сюжете (локомотив, фургон персонала, «Этуаль дю Нор», спальные A–D) — строки таблицы «Состав поезда» без своих записей.
- Безымянный «очень услужливый библиотекарь» и «Ричмонд» (раздатка 6) — упомянуты в тексте, без записей (книга сама оставляет их Хранителю).
- Синая, Бухарест, Варна — только строки расписания (раздатка 3); черновиков городов нет.
- Атмосферные иллюстрации (с. 131, 145, 147, 161) — в `atmosphere-modern.json`.

## Опечатки и расхождения книги (в `errata` записей)

- Отель в Будапеште: таймлайн (с. 143) — «Sofitel», текст дня (с. 145–146) и раздатка 3 — «Hilton» (этап, сцена, черновик Будапешта).
- Вагоны-рестораны: «Etoile du Nord / La Côte / La Saveur d’Asie» (состав), «La Navigation / La Côte / La Saveur d’Asie» (Dining), «L’Oriental» (с. 144) (поезд, сцена `modern-all-aboard`); там же ужин «19.00–21.00» против «19.00–22.00».
- Профиль Милтона (раздатка 1): «Born in 1995» при возрасте 32 года в 2013 году (с. 128, 135).
- Милтон: ПМ 15 при МОЩ 90 (ожидается 18); повтор статблока на с. 167 обрезан (нет Психологии, Ловкости рук, Скрытности, языков) — запись по с. 135.
- Мясной симулякр: ПМ «5 (15)» при МОЩ 40.
- Ларс Фербер: «Brawl 50% (15/6)» — доли исправлены на 25/10 (Р-77), возможна опечатка процента (30%).
- Оскар Гриффин: «Dodge 45% (22/8)» — пятая исправлена на 9 (Р-35).
- Имена: «Morissa» (схема с. 142) / «MeRISSA» (с. 166) / Merissa; «Jacque Cote» (с. 144) / «Jacques Côte» (с. 150); «Giuseppi Roti» (схема); «Sultan Ahment Park» (легенда карты).
- Дневник: Британская библиотека (с. 128) против Британского музея (с. 130, 156).
- Справка заклинаний (с. 168) описывает «Flesh Ward», которой нет в списке Милтона, и не описывает «Contact Nyarlathotep».
- Таймлайн: день 5 — «Antonio Abella murdered», хотя в «Victim 6» Абелла лишь возможная замена.
- Ссылки «page 109 / 77 / 114 of the 1923 campaign» — страницы книги IV (сцена `modern-echoes-of-the-past`).
- Английский текст раздатки 6: «Nylarathotep», «descendent», «whisperer», «breath deeply» — как напечатано.

## Ссылки и вопросы

- Ссылки на записи других частей (существуют на 2026-11-27): Мехмет Макрьят `hotoe-book-2-en/character/mehmet-makryat`, Принц-мозаика
  `hotoe-book-2-en/character/jean-floressas-des-esseintes`, части симулякра `hotoe-book-1-en/item/campaign-simulacrum-*`, места 1923 года
  части constantinople (`constantinople-sirkeci-station`, `-basilica-cistern`, `-shunned-mosque` и его комнаты — метки плана мечети),
  места WWC (`wwc-cold-war-en/location/*`) для меток карты.
- Ritual of Cleansing и Ritual of Enactment (и изменённые версии Милтона) — заклинаний в справочнике нет; в статблоках Милтона и
  Мясного симулякра они без ссылки, изменённые версии описаны в правиле `modern-miltons-spells-quick-reference`. Когда общие записи
  ритуалов появятся (campaign/return/constantinople), нужно проставить `spell` и `variant_of`.
- Сцена `modern-a-request-for-help` без `where` (Будайский лабиринт) — до создания `coc:location:budapest`.
- «Иное место» — область под поездом (`part_of` = поезд): у области без `part_of` нет места в дереве гайда (Р-189, Р-197).
- Стамбульские места 2013 года заведены отдельно от записей 1923 года (с эпохой в названии), со ссылками на них; если владелец
  решит, что здания одной эпохи без различий — одна запись, их можно слить.

## Термины (английский → русский; одна форма везде)

| English | Русский |
|---|---|
| The Simulacrum Unbound | «Симулякр на свободе» |
| Istanbul 2013 / Istanbul Today | Стамбул, 2013 / Стамбул сегодня |
| Modern Handout #N | Современная раздатка N |
| Lux-Vista | «Люкс-Виста» |
| “Anyone Can Go” | «Поехать может каждый» |
| Meat Simulacrum | Мясной симулякр |
| The Other Place | Иное место |
| Echoes of the Past / Historical Echoes | отголоски прошлого / отголоски исторического прошлого |
| Faceless Soldiers | безликие солдаты |
| Shunned Mosque / Red Mosque | Отверженная мечеть / Красная мечеть (как у части campaign) |
| Ritual of Cleansing / Ritual of Enactment | Ритуал очищения / Ритуал свершения (как у части campaign) |
| Create Gate; Gate | «Создание врат»; Врата |
| Cloud Memory, Control Skin, Dominate, Flesh Ward, Melt Flesh, Send Dreams, Contact Nyarlathotep, Call The Skinless One | «Затуманить память», «Управлять кожей», «Покорение», «Защита плоти», «Плавление плоти», «Послание сна», «Связь с божеством: Ньярлатхотеп», «Вызов Бескожего» (по справочнику) |
| The Diary / Milton’s Journal | дневник 1923 года / журнал Милтона |
| The Modern Train; Venice Simplon-Orient-Express | Восточный экспресс (2013); Венеция-Симплон-Ориент-экспресс |
| Salon Bar Car E | салон-бар (вагон E) |
| Restaurant Car—La Côte / La Saveur d’Asie / Etoile du Nord / La Navigation / L’Oriental | вагон-ресторан «Ла Кот» / «Ла Савёр д’Ази» / «Этуаль дю Нор» / «Ла Навигасьон» / «Л’Ориенталь» |
| Sleeping Car (Sleeper) F, G | спальный вагон F, G |
| Fourgon—luggage | багажный фургон |
| steward; maître d’ | стюард; метрдотель |
| Gare de l’Est | Восточный вокзал (Парижа) |
| Sirkeci Station; Park Hyatt Hotel; Basilica Cistern; Sultan Ahmet Park; Istanbul University; Grand Bazaar; Galata Tower | вокзал Сиркеджи; отель «Парк Хаятт»; Цистерна Базилика; парк Султанахмет; Стамбульский университет; Гранд-базар; Галатская башня |
| Main Hall; Great Dome; Stone Column; niches | главный зал; большой купол; каменная колонна; ниши |
| Hilton Hotel; Icon Restaurant | отель «Хилтон»; ресторан «Айкон» |
| Buda Castle Labyrinth; Crowned Head; Trinity Square; Matthias Church; Fisherman's Bastion; Hungarian House of Wines | Лабиринт Будайской крепости; «Коронованная голова»; площадь Святой Троицы; церковь Матьяша; Рыбацкий бастион; Венгерский дом вин |
| Nyugati Pályaudvar (West Station) | Западный вокзал (Ньюгати) |
| John Milton; Giuseppe Roti; John Walters; Enzo Banuelos; Oscar Griffin; Faustino Gonzaga | Джон Милтон; Джузеппе Роти; Джон Уолтерс; Энцо Бануэлос; Оскар Гриффин; Фаустино Гонзага |
| Antonio Abella (Angelo Minotti); Chantel Antin; Henri Guillemette; Merissa Ocana; Wanda Zeigler; Lars Färber; Mark Wilson; Fabian Wyss | Антонио Абелла (Анджело Минотти); Шантель Антен; Анри Гийеметт; Мерисса Окана; Ванда Зейглер; Ларс Фербер; Марк Уилсон; Фабиан Висс |
| Rene Violet; Jacques Côte; Didier Lagoy | Рене Виолет; Жак Кот; Дидье Лагуа |
| The Love of YOUR Life | «Любовь всей ТВОЕЙ жизни» |
| Act Likeable; Write Offensive Letters/Emails | Казаться милым; Писать оскорбительные письма и e-mail (навыки сценария без механики, Р-126) |
| Jigsaw Prince; Locomotive Beast; flesh creeper | Принц-мозаика; Зверь-локомотив; ползучая плоть |
| Extreme / Hard roll; pushed roll | чрезвычайная / трудная проверка; повторная проверка |
| Fajr call to prayer | азан фаджр (призыв к утренней молитве) |
