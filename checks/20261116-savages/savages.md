# «We Are All Savages» (we-are-all-savages-en) — сверка заголовков (Р-134, Р-251)

Книга: William Adcock, «We Are All Savages: A Colonial Scenario for Call of Cthulhu 7th Edition», Miskatonic
Repository, © 2019; рисунки Jonathan Myers, вёрстка и карты Danial Carroll; 37 страниц PDF. Январь 1760 года, форт
Ниагара (колония Нью-Йорк), Франко-индейская война. Русское название — «Мы все дикари» (наш перевод).

Номера страниц: печатный номер стоит на физ. 4–19 (с. 2–17): **физическая = печатная + 2, offset −2**
(в `pipeline/source/books.json` не правлено — ставит ведущий). Обложка, выходные данные, оглавление (физ. 1–3), листы
сыщиков (физ. 20–31; по оглавлению с. 18–29) и бонусные рисунки (физ. 32–37; по оглавлению с. 30) — без номеров, в
`sources` у них `printed_page: null`.

Проверка, что сценария нет в базе под русским переводом: поиск «Coulon», «Кулон», «Niagara», «Ниагар», «Savages»,
«Дикар» по `kb/` — совпадений по сюжету нет (только кулоны-украшения и профессия «Дикарь»).

Записи — `kb/books/we-are-all-savages-en/` (69): сценарий 1, сцены 17, персонажи 14 (6 готовых сыщиков, 6 персонажей
Хранителя, 2 групповых профиля), места 27, предметы 5, организации 3, раздатка 1, карта 1. Существ книги нет: вендиго
Робер Кулон — персонаж со статблоком книги и связью `instance_of` на общий вид `coc:creature:wind-walker`
(«Ходящий по ветру»; Malleus называет обращённых Итакуа людей «вендиго», правило `coc:rule:malleus-wendigoism`) и
`servitor_of` на `coc:creature:ithaqua`. Пути ниже — id без префикса `we-are-all-savages-en/`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) «We Are All Savages», William Adcock | физ. 1 | `scenario/we-are-all-savages` (sources); картинка — атмосфера |
| Credits | физ. 2 | `scenario/we-are-all-savages` (sources) |
| Table of Contents | физ. 3 | `scenario/we-are-all-savages` (sources) |
| Introduction | с. 2 | `scenario/we-are-all-savages` (keeper_info), `location/fort-niagara` (history), `location/fort-niagara-environs` |
| Keeper’s Information | с. 2 | `scenario/we-are-all-savages` (keeper_info), `character/robert-coulon` (legend) |
| Timeline of Events | с. 2 | `scenario/we-are-all-savages` (таблица «Хронология событий») |
| A Note on Historical Fidelity | с. 2 | `scenario/we-are-all-savages` (advice) |
| Fort Niagra Map | с. 3 | картинка записи `location/fort-niagara` (`kind: plan`): подписей и номеров на плане нет (как Р-249) |
| New Weapon: Musket | с. 3 | `item/brown-bess-musket`; `scenario/we-are-all-savages` (таблица «Новое оружие: мушкет», advice) |
| Beginning the Investigation | с. 4 | `scene/eyres-briefing`, `character/william-eyre`, `scenario/we-are-all-savages` (hook) |
| Running Deer’s Tale | с. 4 | `scene/running-deers-tale`, `character/running-deer` |
| Setting Out | с. 4–5 | `scene/setting-out`, `location/fort-niagara-environs` |
| Winter Weather | с. 5 | `scene/setting-out` (description, mechanics), `scenario/we-are-all-savages` (advice) |
| The Remains of the Caravan | с. 5–6 | `scene/remains-of-the-caravan`, `location/ambush-site`, `item/caravan-supplies` |
| Tracking the Marauders | с. 6–7 | `scene/tracking-the-marauders` (с тремя пунктами ночёвки) |
| The Trappers’ Abbatoir | с. 7 | `scene/trappers-abattoir`, `location/trappers-camp`, `organization/french-trappers` |
| Inside the Longhouse | с. 7 | `scene/inside-the-longhouse`, `location/trappers-longhouse`, `item/trappers-diary` |
| Handout: Trapper’s Diary (в тексте) | с. 7–8 | `handout/trappers-diary` (текст полностью + перевод) |
| Cold Storage | с. 8–9 | `scene/cold-storage` |
| The Seneca War Party | с. 9 | `scene/seneca-war-party`, `character/two-foxes`, `character/red-hawk`, `character/seneca-warriors`, `item/wendigo-heart` |
| Returning to the Fort | с. 9 | `scene/returning-to-the-fort` |
| Meeting Anderson | с. 9–10 | `scene/meeting-anderson`, `character/robert-coulon`, `location/fort-hospital` |
| The Storm | с. 10 | `scene/the-storm`, `item/andersons-belongings` |
| After the Storm | с. 10–11 | `scene/after-the-storm`, `location/fort-barracks` |
| Following Anderson | с. 11 | `scene/following-anderson` |
| Anderson’s Plan | с. 11 | `scene/andersons-plan` |
| Inside the French Castle (A–R) | с. 12 | `scene/inside-the-french-castle`, `location/french-castle`; комнаты: A `location/vestibule`, B `trade-room`, C `guards-room`, D `powder-room`, E `store-room`, F `johnson-room`, G `bakery`, H `first-story-vestibule`, I `upper-guards-room`, J `chapel`, K `cabinet`, L `commanders-apartment`, M `officers-mess`, N `sentry-point`, O/P/Q `officers-quarters-o/-p/-q`, R `attic` |
| French Castle Floorplan (First Floor, Ground Floor) | с. 13 | `map/french-castle-floorplan` (картинка `app/maps/savages-french-castle-floorplan.jpg`, 18 меток A–Q, F дважды с `note`) |
| Seeking Outside Help | с. 12, 14 | `scene/seeking-outside-help`, `character/white-owl`, `location/turtle-clan-land`, `organization/turtle-clan` |
| Concluding the Scenario | с. 14 | `scenario/we-are-all-savages` (conclusion, шаг «Развязка») |
| Rewards | с. 14 | `scenario/we-are-all-savages` (conclusion, таблица «Награды Рассудка») |
| Statistics: Average British Soldier | с. 14 | `character/british-soldiers` (групповой профиль, придуманные `names`) |
| Statistics: Average Seneca Warrior | с. 14 | `character/seneca-warriors` (групповой профиль, придуманные `names`) |
| Statistics: Robert Coulon, wendigo | с. 14 | `character/robert-coulon` (статблок, способности) |
| Handout – Trapper’s Diary | с. 15–17 | `handout/trappers-diary` (3 картинки листов) |
| Pre-Generated Characters | физ. 20–31 | `character/john-ambrose` (20–21), `character/james-shaddock` (22–23), `character/arnold-howard` (24–25), `character/jonathan-wellington` (26–27), `character/running-fox` (28–29), `character/wandering-bear` (30–31); портреты — вырезки с листов |
| Bonus Artwork | физ. 32–37 | атмосфера (`atmosphere.json`): шесть рисунков во весь рост без подписей |

Листы сыщиков (физ. 20–31) — картинки без текстового слоя: все числа сняты по изображению страниц (150 dpi),
Удача — по отметке на шкале (Эмброуз 50, Шаддок 40, Говард 50, Веллингтон 60, Бегущий Лис 35, Бродячий Медведь 60).
Половины и пятые доли всех значений на листах сходятся; ПЗ, ПМ, БкУ, Комплекция и Скорость листов сходятся с
характеристиками (у Веллингтона Скорость 6 — с поправкой на возраст 41). Раздел «Gear & Possessions» и «Cash & Assets»
на всех листах пуст.

## Опечатки и расхождения книги

- Таблица «New Weapon: Musket» (с. 3): навык мушкета — «Fighting (Rifle)»; листы сыщиков считают мушкет по Firearms
  (Rifle/Shotgun). В `item/brown-bess-musket` исправлено на Стрельбу (винтовка/дробовик) — `errata` (`fixed: true`) и
  `corrections`.
- «Average Seneca Warrior» (с. 14): Уклонение в «Combat» 35% (17/7), в навыках «Dodge 40%» — в записи 35%, `errata`.
- Хронология (с. 2): дрова в казармах кончаются 18 января, во Французском замке — 19-го; в тексте «After the Storm»
  (с. 11) к рассвету 19-го у казарм дров нет «уже два дня» — небольшое расхождение, отмечено в `quality.notes` сцены.
- Подпись карты «Fort Niagra Map» и заголовок «The Trappers’ Abbatoir» — словесные опечатки (Р-39, не в `errata`).
- Статблок «Robert Coulon, wendigo»: шансы когтей и укуса и навыки без половины и пятой доли — посчитаны. ПЗ солдат 14
  и воинов 15 — округление вверх (приём книги, Р-161).
- Лист Шаддока: Роберт Роджерс назван «Lieutenant-Colonel» — как напечатано (историческая неточность не правится).
- Лист Говарда: «priests no little more about God» (know) — словесная опечатка, исчезает в переводе.

## Предложения правок общих записей

`checks/20261116-savages/proposals-savages.json` — 7 правок в 4 записях (пробный прогон проходит, не применено):
`coc:location:albany` (абзац о 1760 годе, ссылка на сценарий, источник), `coc:weapon:bayonet` и
`coc:weapon:hatchet-sickle` (`source_variants`: урон 1d6+БкУ), `coc:spell:melt-flesh` (псевдонимы «The Charm for
Unmaking a Wendigo» / «Чары развоплощения вендиго»).

Кандидат в новую общую запись оружия (создать предложением нельзя): мушкет «Браун Бесс» (Long Land Pattern) —
Firearms (Rifle/Shotgun), 1d8+4, 40 yards, 1/4, 1, 97; сейчас — предмет книги `item/brown-bess-musket`, атаки
статблоков без поля `weapon`.

## Не взято

- Рисунки физ. 8 и 10 (сани с телами и воронами; повешенные в длинном доме), обложка и шесть бонусных рисунков —
  атмосфера (`atmosphere.json`, Р-241): бонусные рисунки без подписей, по позе и одежде совпадают с героями листов лишь
  предположительно, а портреты листов — другие рисунки.
- Физ. 16: картинки 1808×2088 — полупрозрачные подложки под статблоки (оформление), не иллюстрация.
- Без своих записей (упомянуты, в игре не участвуют): полковник Уильям Джонсон (портрет в зале Джонсона, взятие форта
  1759 года), лорд Джеффри Амхерст и Роберт Роджерс (листы сыщиков), Абигейл — жена Говарда, брат Кулона, трое
  спутников Кулона по шалашу, безымянный автор дневника, второй отряд рейнджеров, люди обоза. Общих записей мест для
  Освего, форта Питт, Питтсбурга, Скенектади, Брентвуда, озера Онтарио, реки Святого Лаврентия, Новой Франции нет —
  только текстом; создавать общие записи часть не вправе (Олбани — предложение выше).
- «Cold Storage» — сцена, а не место: два тела в сугробе за длинным домом описаны в лагере трапперов.
- Подписи этажей плана «First Floor» / «Ground Floor» — заголовки, не метки.

## Термины этой книги (English → Russian)

| English | Русский |
|---|---|
| We Are All Savages | Мы все дикари |
| Fort Niagara | форт Ниагара |
| French Castle | Французский замок |
| Ground Floor / First Floor (плана) | первый этаж / второй этаж |
| Robert Coulon | Робер Кулон |
| Joseph Anderson | Джозеф Андерсон |
| Lieutenant-Colonel William Eyre | подполковник Уильям Эйр |
| Colonel William Johnson | полковник Уильям Джонсон |
| Lord Jeffrey Amherst | лорд Джеффри Амхерст |
| Robert Rogers | Роберт Роджерс |
| Running Deer | Бегущий Олень |
| Two Foxes | Две Лисы |
| Red Hawk | Красный Ястреб |
| White Owl | Белая Сова |
| Running Fox | Бегущий Лис |
| James Bear / Wandering Bear | Джеймс Бэр / Бродячий Медведь |
| John Ambrose / James Shaddock / Arnold Howard / Jonathan Wellington | Джон Эмброуз / Джеймс Шаддок / Арнольд Говард / Джонатан Веллингтон |
| Abigail | Абигейл |
| wendigo | вендиго |
| wendigoism | вендигоизм |
| Itakwa / Ithaqua | Итакуа |
| the Wind-Walker; Him Who Walks Upon the Winds | Ходящий по ветру; Тот, Кто Ходит по Ветрам |
| Great Spirit | Великий Дух |
| Seneca; Mohawk; Iroquois (Confederacy); Algonquin; Wendat | сенека; мохок; ирокезы (Конфедерация ирокезов); алгонкины; вендаты |
| Turtle Clan | клан Черепахи |
| medicine man | знахарь |
| sub-chief | младший вождь |
| war party | военный отряд |
| French trappers / marauders | французские трапперы / налётчики |
| trappers’ camp; The Trappers’ Abbatoir | лагерь трапперов; «Бойня трапперов» |
| longhouse | длинный дом |
| Cold Storage | «Ледник» |
| caravan; supply train | обоз |
| sledges | сани |
| lean-to | шалаш, навес |
| Trapper’s Diary | дневник траппера |
| “Brown Bess” Long Land Pattern Musket | мушкет «Браун Бесс» длинного сухопутного образца |
| bayonet; hatchet; war club; bow | штык; топорик; боевая палица; лук |
| 18-pounder | 18-фунтовая пушка |
| British Grenadier | британский гренадер |
| British Regular Infantryman | британский пехотинец регулярной армии |
| Colonial Militiaman | колониальный ополченец |
| Seneca Warrior | воин-сенека |
| scouts, rangers and woodsmen | разведчики, рейнджеры и лесные следопыты |
| 55th Regiment of Foot | 55-й пехотный полк |
| garrison | гарнизон |
| deserter | дезертир |
| scurvy | цинга |
| spruce beer | еловое пиво |
| salt pork; hardtack | солонина; галеты |
| snowshoes | снегоступы |
| lake effect snow | снег озёрного эффекта |
| cabin fever | «хижинная лихорадка» |
| New France; Saint Lawrence River; Ohio River Valley | Новая Франция; река Святого Лаврентия; долина реки Огайо |
| Oswego; Fort Pitt; Pittsburgh; Albany; Schenectady; Brentwood | Освего; форт Питт; Питтсбург; Олбани; Скенектади; Брентвуд |
| Lake Ontario; Lake Erie; Niagara River | озеро Онтарио; озеро Эри; река Ниагара |
| Drive Wagon (навык листа) | Управление повозкой |
| Fighting (Spear) / (Axe) | Ближний бой (копьё) / (топор) |
| Survival (Woodlands) / (North American Woodlands) | Выживание (леса) / (леса Северной Америки) |
| Language (Other) Iroquois; Language (Own) Seneca | Иностранный язык (ирокезский); Родной язык (сенека) |
| Art/Craft (Carpentry / Farming / Masonry) | Искусство/ремесло (плотницкое дело / земледелие / каменная кладка) |
| Science (Meteorology) | Наука (метеорология) |
| The Charm for Unmaking a Wendigo (Melt Flesh) | Чары развоплощения вендиго («Плавление плоти») |
| Contact Ithaqua | Связь с Итакуа (справочник «Связь с божеством») |
| Rooms A–R | Вестибюль; Торговая комната; Караульная первого этажа; Пороховой погреб; Кладовая; Зал Джонсона; Пекарня; Вестибюль второго этажа; Караульная второго этажа; Часовня; Кабинет; Покои коменданта; Офицерская столовая; Пост часового; Офицерская комната O/P/Q; Чердак Французского замка |

Формы из глоссария: Hard / Extreme — трудный / чрезвычайный успех (проверка); bonus die — бонусная кость (penalty die —
штрафная кость, наша форма по образцу); fumble — крах; Idea / Luck / Sanity roll — проверка Идеи / Удачи / Рассудка; Track — Чтение следов;
Navigate — Ориентирование; Spot Hidden — Внимание; Natural World — Естествознание.
