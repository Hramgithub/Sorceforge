# HOTOE, часть venice — книга III, с. 1–42, 240–245

«Death (and Love) in a Gondola: Venezia 1923» → этап `hotoe-book-3-en/scenario/death-and-love-in-a-gondola`
(«Смерть (и любовь) в гондоле: Венеция, 1923», order 8). Русский текст — наш перевод (Р-251, флаг `translated`).

## Записи

| Вид | Число | Где |
|---|---|---|
| scenario | 1 | `kb/books/hotoe-book-3-en/scenarios/death-and-love-in-a-gondola.json` |
| location (общий город) | 1 | `kb/locations/venice.json` (`coc:location:venice`) |
| location (места) | 40 | `kb/books/hotoe-book-3-en/locations/venice-*.json` |
| scene | 25 | `kb/books/hotoe-book-3-en/scenes/venice-*.json` |
| character | 20 | `kb/books/hotoe-book-3-en/characters/` (13 со статблоком, 7 без) |
| handout | 4 | `kb/books/hotoe-book-3-en/handouts/venice-handout-1…4-*.json` |
| item | 2 | `venice-gremanci-ledgers`, `venice-devils-simulare` |
| creature | 1 | `venice-automatons` |
| organization | 1 | `venice-blackshirts` |
| map | 6 | `venice-venice-1923`, `-players`, `venice-marias-house`, `venice-gremanci-doll-works`, `venice-palazzo-rezzoniani`, `venice-clock-tower` |

Картинки: карты `app/maps/hotoe-venice-*.jpg` (6); портреты, арт и раздатка — `checks/20261127-hotoe/art-venice.json`
(9 картинок, предложения применены к своим записям); атмосфера — `atmosphere-venice.json` (12). Предложения к чужим
записям — `proposals-venice.json` (6: Феналик, Левая нога Симулякра). Новых общих городов не нужно (файла
`new-shared-locations-venice.json` нет).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, посвящение (Lynn W. Willis), выходные данные, «Book 3», содержание | 1–6 | не взято (см. ниже) |
| Death (and Love) in a Gondola: Venezia 1923 (титул, вступление) | 7 | этап `death-and-love-in-a-gondola`: summary, hook; сцена `venice-trip-from-milan` |
| Scenario Considerations | 7 | этап: summary, advice |
| Love in Venice Timeline | 7 | этап: таблица «Любовь в Венеции: хронология» |
| Venetian Glossary | 8 | город: таблица «Венецианский словарик» |
| Keeper Information | 8 | этап: keeper_info; город (нет отделения Братьев Кожи) |
| Venice; The Character of Venice | 9 | город `coc:location:venice`: description |
| подсюжеты «Death in Venice» / «Love in Venice» (Keeper Information, окончание) | 9–10 | этап: keeper_info |
| Love in Venice | 10 | этап: advice (линию можно пропустить) |
| Venice 1923 Map | 10 | карты `venice-venice-1923`, `venice-venice-1923-players`; город: таблица «Венеция: места на карте» |
| The Trip From Milan | 10 | сцена `venice-trip-from-milan` |
| At St. Lucia Station, Venice | 10–12 | сцена `venice-at-st-lucia-station`; место `venice-santa-lucia-station` |
| The Suitors: Alberto Rossini | 12 | персонаж `alberto-rossini` |
| The Blackshirts | 12–13 | организация `venice-blackshirts`; персонаж `blackshirt-thugs` |
| подпись: Carnivale, mid-February 1923 | 12, 19 | город: description; картинки — атмосфера |
| Georgio Gasparetti | 13 | персонаж `georgio-gasparetti` |
| Events in Venice in 1923 (врезка) | 13 | город: description, history |
| Events in Venice | 13 | этап: advice; сцены дней |
| Day One: News from Milan; Oil on the Water; Georgio Calls; A Cry in the Dark | 13–14 | сцена `venice-day-one` |
| Day Two: A Murder Discovered; A Note From Maria; Foul Waters Rising; Tears of Blood | 14–15 | сцена `venice-day-two` |
| Afternoon: Investigating the Murder | 15 | сцена `venice-investigating-the-murder`; персонаж `anselma-moretti` |
| Day Three: Another Murder; News of Plague; Strange Fish | 15, 17 | сцена `venice-day-three` |
| Late Morning: The Funeral | 15–16 | сцена `venice-the-funeral`; места `venice-san-michele`, `venice-stagliani-house` |
| Early Afternoon: An Incident | 16–17 | сцена `venice-the-incident` |
| Day Four: News of Unrest; The Black Canals; Another Note From Maria; Panic in the Streets | 17–19 | сцена `venice-day-four` |
| Night: Maria's Rescue | 18–19 | сцена `venice-marias-rescue`; места `venice-stagliani-house-morning-room`, `-kitchen` |
| Day Five: Venice in Fear; A Honeymoon; The Scorned Suitor; Venice in Lockdown | 20–21 | сцена `venice-day-five` |
| Venice Handout #1 | 20 | раздатка `venice-handout-1-official-report-summary` |
| Death in Venice | 21 | этап: шаг «Смерть в Венеции», keeper_info |
| Searching for the Simulacrum | 21 | сцена `venice-bonapartes-footprint`; этап: шаг |
| Maria's House (план) | 21 | карта `venice-marias-house` |
| Bonaparte's Footprint | 22–23 | сцена `venice-bonapartes-footprint`; город: history |
| Venice Handout #2 | 22 | раздатка `venice-handout-2-diary-of-capitaine-dubois` |
| The Latin Manuscript; The Fate of San Maria Celeste | 23 | сцена `venice-the-latin-manuscript`; место `venice-naval-mechanics-school`; предмет `venice-devils-simulare` |
| Discovery at the Biblioteca Marciana | 24 | сцена `venice-the-latin-manuscript`; место `venice-biblioteca-marciana` |
| San Marco Basilica | 24 | место `venice-san-marco-basilica`; сцена `venice-chapel-of-saint-isidoro` |
| The Chapel Of Saint Isidoro; The Paving Stone; Lifting the Paving Stone | 24–25 | сцена `venice-chapel-of-saint-isidoro`; место `venice-chapel-of-saint-isidoro` |
| Breaking In And Out Of San Marco | 25–26 | сцена `venice-breaking-into-san-marco` |
| Beneath The Paving Stone; The Wax Seal | 26 | сцена `venice-beneath-the-paving-stone` |
| Venice Handout #3 (Handwritten Note Found in San Marco) | 26 | раздатка `venice-handout-3-thiefs-confession` |
| Researching the Gremancis | 27 | сцена `venice-researching-the-gremancis` |
| The Doll Makers | 27 | место `venice-gremanci-doll-works`; этап: шаг «Кукольники» |
| The Campo Della Bambino | 27–28 | место `venice-campo-della-bambino` |
| Gremanci Doll Works (план) | 28 | карта `venice-gremanci-doll-works` |
| The Doll Works; The Foyer | 28–29 | сцена `venice-visiting-the-doll-works`; место `venice-gremanci-foyer` |
| Antonio's Office; Antonio Gremanci | 29 | место `venice-gremanci-antonios-office`; персонаж `antonio-gremanci` |
| Sebastiano Gremanci; Sebastiano's Story | 30 | персонаж `sebastiano-gremanci` |
| What the Gremancis Know; The Gremanci Records | 30–31 | сцена `venice-gremanci-records`; предмет `venice-gremanci-ledgers` |
| Venice Handout #4 (The Ledgers of Marco Gremanci) | 31 | раздатка `venice-handout-4-ledgers-of-marco-gremanci` |
| The Work Rooms; The Store Room | 31–32 | места `venice-gremanci-finishing-room`, `-shaping-room`, `-store-room` |
| The Footprint Revealed | 32 | сцена `venice-gremanci-records` |
| Palazzo Rezzoniani | 32 | место `venice-palazzo-rezzoniani` |
| The Caretaker | 32–33 | сцена `venice-the-caretaker`; персонаж `nonno-fidele`; место `venice-campo-rezzoniani` |
| Palazzo Rezzoniani (план) | 33 | карта `venice-palazzo-rezzoniani` |
| Inside The Palazzo; The Ground Floor; The Second Floor; The Third Floor | 33–34 | сцена `venice-inside-the-palazzo`; места `venice-palazzo-rezzoniani`, `-courtyard`, `-private-apartment` |
| The Clock Tower; The Door; The Stairs | 34–35 | сцена `venice-climbing-the-clock-tower`; место `venice-clock-tower` (таблица «Часовая башня: выходы автоматов») |
| Outside the Clock | 35 | сцена `venice-climbing-the-clock-tower` |
| Inside the Clock; The Automatons; Searching the Statues | 35–36 | сцена `venice-inside-the-clock`; место `venice-clock-tower-clockwork` (таблица «Часовая башня: где стоят автоматы») |
| The Clock Strikes | 36 | сцена `venice-inside-the-clock` |
| The Automatons Attack | 36–37 | сцена `venice-the-automatons-attack` |
| Clock Tower (план) | 37 | карта `venice-clock-tower` |
| Conclusion; Fenalik | 38 | сцена `venice-conclusion`; этап: conclusion, таблица «… Рассудок»; предложение к `coc:character:fenalik` |
| Statistics: Antonio Gremanci, Sebastiano Gremanci, Gasparo, Maria Stagliani, Georgio Gasparetti, Alberto Rossini, Nonno Fidele | 39–40 | персонажи `antonio-gremanci`, `sebastiano-gremanci`, `gasparo`, `maria-stagliani`, `georgio-gasparetti`, `alberto-rossini`, `nonno-fidele` |
| The Mob; Carlo Casciano; Sample Mob Member | 40 | персонажи `carlo-casciano`, `sample-mob-member`; этап: advice |
| Six Blackshirt Thugs; Two Blackshirt Elite; Six Police (Vigili) | 40–41 | персонажи `blackshirt-thugs`, `blackshirt-elite`, `police-vigili` |
| Sebastiano's Friends | 41 | персонаж `sebastianos-friends` |
| The Automatons | 41 | существо `venice-automatons` |
| (плакат Simplon-Orient-Express, полная страница) | 42 | атмосфера |
| Complete Maps: Venice Keeper's Map; Venice Player's Map | 240–241 | карты `venice-venice-1923`, `venice-venice-1923-players` (источники) |
| Complete Maps: Maria's House; Gremanci Doll Works; Palazzo Rezzoniani; Clock Tower | 242–245 | карты (картинки — с этих страниц) |
| Keeper Maps, лист 7; Player Maps, лист 5 | — | картинки карт `venice-venice-1923`, `-players` |
| Book VI, с. 91–95 (раздатки), 127 (карта игроков), 129–135 (планы) | — | источники и картинки раздаток; источники карт |

## Не взято

- С. 1–6: обложка, посвящение Линну Уиллису, выходные данные Chaosium (адрес, ISBN), титул «Book 3», содержание —
  игрового содержания нет.
- С. 42: полностраничный плакат «Simplon-Orient-Express — Vers la Corne d'Or» — атмосфера (`atmosphere-venice.json`),
  как и фото и рисунки глав (Венеция сверху, акварель лагуны, маски «Moretta» и «Bauta», Большой канал, «стоячие
  каналы», одержимый с распятиями, палаццо на канале, мастерская кукол, странные рыбы, церковь с колокольней).
- Отдельных записей не получили (упомянуты текстом в сценах и персонажах): жертвы Феналика Марио Росси и гондольер
  Пауло Ризо, дочь Дюбуа Шери, майор Отмон, Альвизе де Гременчи (1630), внук Марко Гременчи (погиб у Монте-Граппа),
  священник, управляющий отелем, официант и его шурин, виновный гондольер, левые студенты Джорджо, Артуро Фачча
  (персонаж Милана, часть lausanne-milan). Места без записей: Арсенал, Местре, Маргера, Пеана, Монте-Граппа, канал
  Джудекка (метка карты ведёт на город), казармы Сан-Марко 1797 года, «запущенное кампо» засады.
- Карта игроков для четырёх планов (Book VI, с. 129–135) отдельными записями не заведена: копии для игроков
  совпадают с планами Хранителя (с. 242–245), их страницы — в `sources` карт. Отдельная карта игроков — только у
  Венеции (Player Maps, лист 5: другой ключ 1–9).
- На планах не получили меток масштабы («5 meters», «1 2 meters», «3 mts»), роза ветров, заголовок «Venice — Queen of
  the Adriatic», рамка ключа и подписи-оформление «senso di casa nel marco morte» (план фабрики) и «m. morte
  watch-house» (план башни).

## Опечатки и сомнения

- Мария Стальяни: Скорость 4 (ожидается 8) — `errata`.
- Карло Кашано: Скорость 5 (ожидается 8) — `errata`.
- Альберто Россини: Дерринджер «36% (18/6)» → 7 (Р-35, исправлено); ПЗ 17 при 16,5 — округление вверх (Р-161).
- Джорджо Гаспаретти: Уклонение «53% (26/11)» → 10 (Р-35, исправлено).
- Элита чернорубашечников: Драка «70% (30/12)» — доли от 60%; доли исправлены (Р-77), возможна опечатка в проценте.
- Член толпы (образец): БкУ 0, но урон драки и дубинки «+1d4» — `errata`.
- Друзья Себастьяно: Уклонение 30% ниже половины ЛВК 65 у двоих — `errata`.
- Смерть деда Марко Гременчи: «в июле 1918» (с. 30) против «9 апреля 1918» (Венеция 4, с. 31) — `errata` у
  персонажа, сцены и раздатки.
- Тело синьора Реццониани нашли «через несколько месяцев» (Фиделе, с. 32) против «несколько дней» (Венеция 4,
  с. 31) — `errata`.
- Ключ карты (Keeper Maps и с. 10, 240): «Pelazzo Rezzoniani»; подпись «Giul Canale Della Giudecca» — как напечатано.
- Нумерация мест у карты Keeper Maps (лист 7) не совпадает с картой книги (с. 10, 240) и игроков — обе в таблице
  «Венеция: места на карте».
- «San Michelle» (с. 15) — остров Сан-Микеле; «Miestre» (с. 30) — Местре; «Antiono» (с. 30), «Soon offer sunset»
  (с. 7), «Italian (0wn)» — словесные, исправлены молча (Р-39).
- Нонно Фиделе: в тексте «только средних лет», в статблоке — 66 лет (оставлено, пометка).
- План фабрики Гременчи: каналы Сан-Кассиан и Мадоннетта (район Сан-Поло), в тексте — Каннареджо (пометка).
- Хронология (с. 7): вторая записка Марии «вскоре после заката» четвёртого дня, в «Событиях» (с. 17) — «конец дня».
- «Six Blackshirts loiter down-stairs» + двое наверху = восемь при шестерых в статблоке — как в книге.
- Book VI, с. 129: поверх плана «Maria's House» напечатана посторонняя подпись «BOOK III, PAGE 213» (к другой главе —
  для части belgrade).

## Термины (английский → русский)

| English | Русский |
|---|---|
| Death (and Love) in a Gondola | Смерть (и любовь) в гондоле |
| Love in Venice / Death in Venice / Events in Venice | Любовь в Венеции / Смерть в Венеции / События в Венеции |
| Venice; Venezia | Венеция |
| Queen of the Adriatic | Королева Адриатики |
| Grand Canal; Canal Grande | Большой канал |
| Rialto; The Rialto Bridge | Риальто; мост Риальто |
| Piazza San Marco | площадь Сан-Марко |
| San Marco Basilica | собор Святого Марка |
| Chapel of Saint Isidoro | капелла Святого Исидора |
| Ducal Palace; Doges' Palace | Дворец дожей |
| Biblioteca Marciana | Библиотека Марчиана |
| I Frari (Friary) | Фрари (монастырь) |
| Accademia | Академия |
| Ca' Foscari University | университет Ка' Фоскари |
| St. Lucia Station | вокзал Санта-Лючия |
| Gritti Palace Hotel | отель «Гритти Палас» |
| Hotel Royal Danieli | отель «Ройял Даниели» |
| Rest. Baur-Grunwald; Restaurant Pilsen | ресторан «Бауэр-Грюнвальд»; ресторан «Пильзен» |
| San Marco / Cannaregio / Castello (districts) | Сан-Марко / Каннареджо / Кастелло (районы) |
| San Michele (San Michelle) | остров-кладбище Сан-Микеле |
| Campo S. Angelo; Campo della Bambino; Campo Rezzoniani | кампо Сан-Анджело; кампо делла Бамбино; кампо Реццониани |
| Rio di S. Salvatore; Rio di San Cassian; Rio della Madonnetta | рио ди Сан-Сальваторе; рио ди Сан-Кассиан; рио делла Мадоннетта |
| San Maria Celeste | Сан-Мария-Челесте |
| school for navy mechanics | школа морских механиков |
| Arsenal; Arsenal Fire of 1569 | Арсенал; пожар Арсенала 1569 года |
| Mestre; Marghera; Peana; Monte Grappa | Местре; Маргера; Пеана; Монте-Граппа |
| campanile / campo / canal / doge / fondamenta / gondola / gondolier / palazzo / pensione / piazza / rio / vaporetto | кампанила / кампо / канал / дож / фондамента / гондола / гондольер / палаццо / пансионе / пьяцца / рио / вапоретто |
| Sempre dritto | «Sempre dritto» («всё прямо») |
| Carnivale | карнавал |
| Council of Ten; Bocca di Leone | Совет десяти; «Львиная пасть» |
| Blackshirts; Fascist; Communist | чернорубашечники; фашист; коммунист |
| Arditi | ардити |
| Vigili; Militi | виджили; милити |
| Palazzo Rezzoniani | палаццо Реццониани |
| Clock Tower; Fifth Floor (Inside the Clock) | часовая башня; часовой механизм (пятый этаж) |
| Automatons | автоматы (глоссарий: Automaton → Автомат) |
| Death / Angel / Turk / Winged Lion / Condottiere (Soldier) / Assassin / Rustic Lass / Rustic Lad | Смерть / Ангел / Турок / Крылатый лев / Кондотьер (Солдат) / Наёмный убийца / Сельская девушка / Сельский парень |
| Gremanci Doll Works (Dollworks) | кукольная фабрика Гременчи |
| Foyer (Waiting Room); Antonio's Office; Finishing Room; Shaping Room; Store Room (Warehouse, Old Storage) | приёмная; кабинет Антонио; отделочная мастерская; формовочная мастерская; склад |
| The Gremanci Records; The Ledgers of Marco Gremanci | конторские книги Гременчи; конторские книги Марко Гременчи |
| Thief's Confession; Handwritten Note Found in San Marco | признание вора; записка, найденная в соборе Святого Марка |
| Official Report Summary; The Diary of Capitaine Dubois | краткий официальный рапорт; дневник капитана Дюбуа |
| The Devil's Simulare | «Дьявольское подобие» (совпадает с частью crusader) |
| Left Leg of the Sedefkar Simulacrum | Левая нога Симулякра Седефкара |
| Baleful Influence | Пагубное влияние (как у части campaign) |
| Maria's House; Gasparetti's House; Sebastian's House | дом Марии Стальяни; дом Гаспаретти; дом Себастьяно Гременчи |
| Morning Room; Kitchen | утренняя комната; кухня |
| Maria Stagliani; Bice; Giovanni Stagliani | Мария Стальяни; Биче; Джованни Стальяни |
| Georgio Gasparetti | Джорджо Гаспаретти |
| Alberto Rossini | Альберто Россини |
| Antonio / Sebastiano / Marco / Alvise de Gremanci | Антонио / Себастьяно / Марко / Альвизе де Гременчи |
| Gasparo | Гаспаро |
| Nonno Fidele | Нонно Фиделе («Дедушка» Фиделе) |
| Signor Rezzoniani | синьор Реццониани |
| Capitaine Guillaume Dubois; Jean Boucher; Major Hautemont; Cherie | капитан Гийом Дюбуа; Жан Буше; майор Отмон; Шери |
| Anselma Moretti; Mario Rossi; Paulo Rizo | Ансельма Моретти; Марио Росси; Пауло Ризо |
| Carlo Casciano | Карло Кашано |
| Sample Mob Member; The Mob | член толпы (образец); толпа |
| Six Blackshirt Thugs; Two Blackshirt Elite | чернорубашечники-громилы; элита чернорубашечников |
| Six Police (Vigili) | полицейские-виджили |
| Sebastiano's Friends | друзья Себастьяно |
| Catch Rat; Spot Tourist; Belittle; Growl Ominously; Wave Torches (шуточные навыки) | ловить крыс; замечать туристов; унижать; грозно рычать; размахивать факелами |
