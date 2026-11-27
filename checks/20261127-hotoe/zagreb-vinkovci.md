# «Ужас в Восточном экспрессе», книга III: Загреб из сна и Винковци (часть zagreb-vinkovci)

Книга `hotoe-book-3-en` (печатная = физическая − 2), с. 117–164, 251, 256–260; книга VI `hotoe-book-6-handouts-en` с. 107–120,
149–156; Keeper Maps 10, Player Maps 8. Решения: Р-254, Р-251, Р-202, Р-228, Р-190, Р-206, Р-209, Р-154, Р-208.
Генераторы — `.cache/lead-tools/gen-hotoe-zagreb-vinkovci/` (`gen_zagreb.py`, `gen_people.py`, `gen_vinkovci.py`,
`gen_proposals.py`, `maps.py`, `art.py`, `art2.py`). Префиксы `B3 = hotoe-book-3-en`.

## Записи

| Вид | Число | Записи |
|---|---|---|
| scenario | 2 | `B3/scenario/in-a-city-of-bells-and-towers` (order 11), `B3/scenario/bread-and-stone` (order 12) |
| scene | 24 | `zagreb-a-gift`, `-the-consequence`, `-a-search`, `-what-they-meet`, `-a-discovery`, `-a-genuine-peril`, `-an-ending`; `vinkovci-arrival`, `-a-sudden-greeting`, `-oddness-in-the-letter`, `-hovart-brothers`, `-hotel-lehrner`, `-lovacki-dvorac`, `-looking-for-dr-moric`, `-kunjevci`, `-local-authorities`, `-the-cudoviste`, `-crusaders-tomb`, `-missing-reporter`, `-trail-of-clues`, `-lot-187`, `-the-laboratory`, `-mad-scientist`, `-mims-sahis`, `-leaving` |
| location | 49 + общий город | общий `coc:location:vinkovci` (новый, `kb/locations/vinkovci.json`); Город колоколов `zagreb-city-of-bells` (город сна, part_of null) и 18 мест под ним (вокзал, Крепость, Стена, Река, Туман, Бульвар, каналы, места 1–12); Винковци — 12 мест ключа карты, вокзал, читальный зал, сквер с поилкой Валента, улица Звонарска, река Босут, два помещения гробницы; область `vinkovci-environs` с Куньевци, цементным заводом, убежищем ЛПВ, лабораторией Белензады и шестью её частями |
| map | 6 | `zagreb-city-of-bells`, `zagreb-city-of-bells-players`, `vinkovci-town`, `vinkovci-town-players`, `vinkovci-hunting-lodge`, `vinkovci-belenzada-laboratory` (картинки `app/maps/hotoe-zagreb-vinkovci-*.jpg`) |
| handout | 17 | `zagreb-handout-1…10-*`, `vinkovci-handout-1…7-*` (текст как напечатан + перевод, картинка копии из книги VI) |
| character | 24 | со статблоком: `jazmina-moric`, `velemir-karkunica`, `filip-opacic`, `radmilo-boskovic`, `vinkovci-police-officers` (групповой), `belgrade-army-soldiers` (групповой), `goran-belenzada`, `nenad-zupan`, `mihael-loncar`, `branko-jankovic` (вариант «после операции»), Волки: `jakob-turato`, `andro-turato`, `karel-zupan`, `bojun-kasun`, `jovan-kasun`, `tereza-turato`, `neza-zupan`; без статблока: `hooded-stranger`, `dragomir-moric`, `vesna-femic`, `lazar-andric`, `kamila-hanak`, `bisera-odak`, `dieter-koll`, `padovan` |
| creature | 1 | `vinkovci-cudoviste` |
| organization | 3 | `vinkovci-wolves-of-vinkovci`, `vinkovci-peoples-justice-army`, `vinkovci-order-of-the-noble-shield` |
| item | 7 | `zagreb-chateau-guiraud-lafon-sauterne`, `vinkovci-lot-187`, `vinkovci-lot-187-key`, `vinkovci-tyre-tetradrachm`, `vinkovci-barrier-of-st-gabriel`, `vinkovci-tomb-elder-sign-stone`, `vinkovci-noble-shield-archives` |
| tome | 1 | `vinkovci-notebook-of-dr-moric` |

Мимс Сахис — запись кампании `hotoe-book-1-en/item/campaign-mims-sahis` (своей нет); сэр Михо — `B3/character/miho-of-dubrovnik` (часть crusader).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| In a City of Bells and Towers (Dream Zagreb 1923), вступление | 117 | этап `in-a-city-of-bells-and-towers` (summary, keeper_info) |
| An Overnight Journey (врезка) | 117 | этап: advice |
| An Option to Dream (врезка) | 117 | этап: advice, keeper_info |
| A Gift | 117–118 | сцена `zagreb-a-gift`; предмет `zagreb-chateau-guiraud-lafon-sauterne` |
| The Consequence; If They Do Not Disembark | 118–120 | сцена `zagreb-the-consequence`; `hooded-stranger`; `zagreb-station` |
| A Search | 120 | сцена `zagreb-a-search` |
| The Map; The Journals; The Boundaries; Unreliable Senses | 121 | сцена `zagreb-a-search`; места Стена, Река, Туман, Бульвар |
| The Hours (врезка) | 121 | таблица этапа «Город колоколов: часы» |
| The Journal Authors (врезка); The Journal Pages | 122 | таблица этапа «Город колоколов: авторы дневников»; раздатки Загреб 1–10 |
| What They Meet; ONE–TWELVE | 122–123 | сцена `zagreb-what-they-meet`; места `zagreb-1…12-*`; таблица «Город колоколов: что встречают сыщики» |
| Skull of the Hooded Stranger (подпись к рисунку) | 124 | картинка у `hooded-stranger` |
| A Discovery; Accursed Enlightenment; Willful Ignorance | 124–125 | сцена `zagreb-a-discovery`; `zagreb-fortress` |
| A Genuine Peril | 125 | сцена `zagreb-a-genuine-peril` |
| An Ending; The Real Zagreb | 125–126 | сцена `zagreb-an-ending`; город сна (абзац «Настоящий Загреб») |
| Conclusion | 126 | этап: conclusion, таблица «Город колоколов: итоги сна» |
| About Thomas Ligotti (врезка) | 126 | этап: advice |
| Zagreb Handouts #1–#10 | 127–130; кн. VI 107–113 | `zagreb-handout-1…10-*` |
| City of Bells (карта) | 119, 256, 257; кн. VI 149 | `map/zagreb-city-of-bells`, `map/zagreb-city-of-bells-players` |
| Bread or Stone (Vinkovci 1923), вступление | 131 | этап `bread-and-stone` (summary) |
| This 1923 Scenario is Optional (врезка) | 131 | этап: advice |
| Keeper’s Information | 132 | этап: keeper_info; `dragomir-moric`, `goran-belenzada` |
| The Wolves of Vinkovci (врезка и раздел) | 133 | организация `vinkovci-wolves-of-vinkovci`; этап: keeper_info |
| State of Emergency | 133 | этап: keeper_info; город (описание) |
| Arrival in Vinkovci; Slow Train; The Newspaper Story; Arrival; Questions | 133–135 | сцена `vinkovci-arrival`; раздатка Винковци 1 |
| Politics of Post Great War Yugoslavia (врезка) | 134 | `coc:location:vinkovci` (history) |
| Stranded in Vinkovci; Waiting in Vinkovci | 135–136 | сцена `vinkovci-arrival` |
| Sleeping Sickness (врезка) | 136 | сцена `vinkovci-arrival` |
| Events in Vinkovci in 1923 (врезка) | 136 | `coc:location:vinkovci` (описание) |
| A Sudden Greeting; The Wolves Close In | 136–138 | сцена `vinkovci-a-sudden-greeting` |
| About Vinkovci (врезка) | 137 | `coc:location:vinkovci` (описание) |
| Co-operation | 138 | сцена `vinkovci-a-sudden-greeting` |
| Jazmina Moric | 138–139 | `jazmina-moric` |
| A Conversation with Jazmina Moric; Oddness in the Letter; The Wolf’s Tail | 139 | сцена `vinkovci-oddness-in-the-letter`; раздатка Винковци 2 |
| Hovart Brothers Butcher Shop | 140 | сцена `vinkovci-hovart-brothers`; место `vinkovci-hovart-brothers-butcher-shop` |
| The Lovacki Dvorac Hunting Lodge (план) | 140, 260; кн. VI 151 | `map/vinkovci-hunting-lodge` |
| The Hotel Lehrner | 140–141 | сцена `vinkovci-hotel-lehrner`; место; раздатка Винковци 3 |
| Lovacki Dvorac Lodge | 141 | место `vinkovci-lovacki-dvorac-lodge`; сцена `vinkovci-lovacki-dvorac` |
| The People’s Justice Army (LPV) (врезка) | 141 | организация `vinkovci-peoples-justice-army` |
| Investigations | 141–142 | этап: advice, steps |
| Scenario Timeline (врезка) | 142 | таблица этапа «Винковци: хронология» |
| Looking for Dr. Moric; Belenzada’s Home; Opca Bolnica Vinkovci; Visiting the Facility; The Veterans | 142–144 | сцена `vinkovci-looking-for-dr-moric`; места дома, больницы, лаборатории |
| Dr. Belenzada’s Daily Routine (врезка) | 143 | таблица этапа «Винковци: распорядок дня доктора Белензады» |
| Dr. Goran Belenzada; Meeting Dr. Goran Belenzada; After the Meeting | 144–145 | `goran-belenzada`; сцена `vinkovci-looking-for-dr-moric` |
| Kunjevci; Wrongful Death | 145–146 | сцена `vinkovci-kunjevci`; место `vinkovci-kunjevci` |
| Vinkovci Handout #4 | 146 | `vinkovci-handout-4-cudoviste-stalks-vinkovci` |
| The Local Authorities; Police Interrogation; Words of Advice | 146–147 | сцена `vinkovci-local-authorities` |
| The Cudoviste | 147–148 | сцена `vinkovci-the-cudoviste`; существо `vinkovci-cudoviste` |
| The Crusader’s Tomb; Location; Getting Inside; The Entrance; The Guard Room; The Vault | 148–149 | сцена `vinkovci-crusaders-tomb`; места гробницы; `vinkovci-tomb-elder-sign-stone` |
| The Missing Reporter; The Office of Cibalis; Research; Vesna Femic’s Home; Vesna’s Notebook; A Glimpse of Vesna; The Rose Garden; The Rubbish Wagon; Contacting the Police | 149–151 | сцена `vinkovci-missing-reporter`; места; раздатка Винковци 5 |
| The Trail of Clues; The Street; The Book Store; The Warehouse; The Final Riddle | 151–152 | сцена `vinkovci-trail-of-clues`; раздатка Винковци 6; `vinkovci-lot-187-key` |
| Vinkovci Handout #7 | 152 | `vinkovci-handout-7-moric-notebook-summary` |
| Lot 187; The Notebook; The Artifacts (коробка с монетой; коробка с камнем; 32 свитка и 18 книг) | 153 | сцена `vinkovci-lot-187`; предметы; книга `vinkovci-notebook-of-dr-moric` |
| The Accounts of Tillius Corvus; Rasul al-Albarin; Sapientia Maglorum | 154 | `vinkovci-noble-shield-archives`; предложения `copies` в `coc:tome:rasul-al-albarin`, `coc:tome:sapientia-maglorum` |
| The Laboratory; Breaking In; The Restored Guards; The Facility’s Cudoviste | 154 | сцена `vinkovci-the-laboratory`; варианты охранников |
| The Mims Sahis (врезка) | 155 | предложения к `hotoe-book-1-en/item/campaign-mims-sahis` (mechanics, aliases) |
| Unlikely Allies; The Compound; The Wall and Outer Gate; The Guard House; The Office; The Kennels; The Incinerator; The Surgical Lab | 156–158 | сцена `vinkovci-the-laboratory`; места `vinkovci-lab-*` |
| Dr. Belenzada’s Laboratory Compound (план) | 156, 251; кн. VI 153 | `map/vinkovci-belenzada-laboratory` |
| Vinkovci (карта) | 157, 258, 259; Keeper Maps 10; Player Maps 8; кн. VI 155 | `map/vinkovci-town`, `map/vinkovci-town-players`; таблица «Винковци: места на карте» |
| The Mad Scientist; If the Investigators Attack; If the Investigators Talk | 158–159 | сцена `vinkovci-mad-scientist` |
| The Mims Sahis; The Bulatovic Cement Factory; Finding the Rock Crusher; The Wolves Attack; The Mims Sahis is Destroyed; Other Methods; Retaining The Mims Sahis; The Knife and the Simulacrum | 159–160 | сцена `vinkovci-mims-sahis`; место завода; предложения к Мимс Сахису |
| Leaving Vinkovci | 160–161 | сцена `vinkovci-leaving` |
| Conclusion | 161 | этап: conclusion, таблица «Винковци: награды» |
| Statistics: Jazmina Moric, Police Officers, Captain Velemir Karkunica, Major Radmilo Boskovic, Lieutenant Filip Opacic, Soldier | 162 | персонажи (см. выше) |
| The Wolves of Vinkovci: Brothers of the Skin; Names and Roles | 163 | семь персонажей-Волков, организация |
| Dr. Goran Belenzada | 163 | `goran-belenzada` |
| Dr. Belenzada’s Guards | 164 | `nenad-zupan`, `mihael-loncar`, `branko-jankovic` |
| Cudoviste, Lesser Servitor; Cudoviste, Surgical Abominations; Roll 1D4 for Arms; Roll 1D6 for Head | 164 | `vinkovci-cudoviste` (таблицы рук и головы — в способностях) |
| Vinkovci Handouts #1–#7 | 135–152; кн. VI 115–119 | `vinkovci-handout-1…7-*` |

## Не взято

- Настоящий Загреб — общей записи нет: глава прямо не даёт о нём сведений (с. 117, 126). Черновик для ведущего —
  `new-shared-locations-zagreb-vinkovci.json`; Travelers’ Companion (Trieste, with Postumia, Zagreb) — часть companion.
- Звёздочки «Journal Pages» на карте Города колоколов — без меток: книга не связывает звёздочку с раздаткой (места условны, с. 122).
- Помещения охотничьей усадьбы — без отдельных записей: текст их не описывает; метки плана ведут на запись усадьбы.
- Мелкие упомянутые лица без записей (текстом в записях): официант Морис и сомелье, ночной проводник, шеф поезда, чиновник
  Компании спальных вагонов, английский учитель из Загреба, водопроводчик Винко Сервенка, художник Драган Алексич, Ирена Колль,
  семья Лончар (хозяева усадьбы), Бара Тутич, доктор Радко Йорданов (его запись — дело части sofia), Иоланда, Гонорий III, граф Балдуин.
- «Рассказ Тиллия Корва» (The Accounts of Tillius Corvus) — своей записи нет: это раздатка главы «Sanguis Omnia Vincet» (часть sanguis); чисел книги Мифов глава не даёт.
- Иллюстрации «опытов» Белензады (свинья-собака, овца-медведь, с. 158, 154, 161) — атмосфера (`atmosphere-zagreb-vinkovci.json`).
- Фоновые картинки врезок (серые подложки страниц) — не иллюстрации.

## Опечатки и сомнения книги

- Название главы: «Bread or Stone» (с. 131, 71) и «Bread and Stone» (оглавление с. 5) — errata у этапа; русское имя «Хлеб и камень» (как у записи кампании), «Хлеб или камень» — псевдоним.
- Куньевци: 3,25 мили к югу (с. 145) против «Kunjevci 5 miles» на карте (с. 157) — errata у места.
- «Pouzdan Zaiihi Storage» в ключе карты Хранителя (вместо Zalihi) — errata; «Vincovki Train Station» на карте игроков — errata.
- «Kralja Zvonimia» (вместо Kralja Zvonimira) — в раздатке Винковци 3 и на с. 151, как напечатано.
- Чудовиште: Комплекция 0 при СИЛ+ТЕЛ 212 и БкУ +2d6 — исправлено на 3 (Р-36); ЛВК 14 (4d6) без ×5 — как напечатано, errata.
- Полицейские: «8-mm Gaserov M98 revolver» без долей — как напечатано, errata; капитан Каркуница: Ближний бой «70%» без долей — дополнено (35/14).
- Майор Бошкович: .45 — урон 1d10+1 (в «Книге хранителя» 1d10+2) — как напечатано, пометка в атаке.
- Карел Жупан: Скорость 7 при СИЛ = ТЕЛ (8) — возраст не напечатан («Older male»), errata.
- Солдат: ПЗ 14 при 13,5 — округление вверх, приём книги (Р-161); ОБР 10 — как напечатано.
- Масштаб карты Винковци: 200 м в Keeper Maps, 200 ярдов на с. 157.
- Мимс Сахис: «2d4 (see notes)» у Белензады против «2D4+db» во врезке.

## Термины (английский → русский)

| English | Русский |
|---|---|
| In a City of Bells and Towers | В городе колоколов и башен |
| Dream Zagreb | Загреб из сна (псевд. «Загреб во сне») |
| City of Bells | Город колоколов |
| Hooded Stranger / The Cloaked Man | незнакомец в капюшоне / человек в плаще |
| Jigsaw Prince | Принц-мозаика (как в записи кампании) |
| Château Guiraud-Lafon | «Шато Гиро-Лафон» |
| night conductor | ночной проводник |
| Chef de Train | шеф поезда |
| The Fortress / The Wall / The River / The Fog / The Boulevard | Крепость / Стена / Река / Туман / Бульвар |
| Journal Pages | страницы дневника |
| Bread or Stone (Bread and Stone) | Хлеб и камень (псевд. «Хлеб или камень») |
| Vinkovci | Винковци (несклоняемое; псевд. «Винковцы») |
| Colonia Aurelia Cibalae | Колония Аврелия Цибалы |
| Wolves of Vinkovci / Vukovi Vinkovcima | Волки Винковци / Вукови Винковцима |
| Brothers of the Skin | Братья кожи (общая запись) |
| People’s Justice Army (LPV) | Народная армия правосудия (ЛПВ) |
| Order of the Noble Shield | Орден Благородного Щита |
| The Serpent’s Claw | Коготь Змея |
| Mims Sahis | Мимс Сахис |
| Cudoviste | чудовиште |
| Lovacki Dvorac (The Hunter’s Manor) | «Ловачки-Дворац» (Охотничья усадьба) |
| Hotel Lehrner | отель «Лернер» |
| Hovart Brothers | «Братья Ховарт» |
| Opca Bolnica Vinkovci | Общая больница Винковци (Опча болница) |
| Odlika Knjiga | «Одлика книга» |
| Pouzdan Zalihi | склад «Поуздан залихи» |
| Cibalis | «Цибалис» |
| The Rose Garden | «Розовый сад» |
| Kunjevci | Куньевци |
| Bulatovic Cement Factory | цементный завод Булатовича |
| Lot 187 | ячейка 187 |
| Crusader’s Tomb | Гробница крестоносца |
| Notebook of Dr. Moric | Записная книжка доктора Морича |
| Barrier of St. Gabriel (Obex sancti gabrielis) | Преграда святого Гавриила |
| Accounts of Tillius Corvus | «Рассказ Тиллия Корва» (как в записи кампании) |
| Society for War Invalids | Общество инвалидов войны |
| Croatian Common People’s Peasant Party (HSS) | Хорватская народная крестьянская партия (ХСС) |
| Jazmina / Dragomir Moric | Язмина / Драгомир Морич |
| Goran Belenzada | Горан Белензада |
| Velemir Karkunica / Filip Opacic / Radmilo Boskovic | Велемир Каркуница / Филип Опачич / Радмило Бошкович |
| Vesna Femic / Lazar Andric | Весна Фемич / Лазар Андрич |
| Kamila Hanak / Bisera Odak / Dieter Koll / Mr. Padovan | Камила Ханак / Бисера Одак / Дитер Колль / господин Падован |
| Jakob, Andro, Tereza Turato | Якоб, Андро, Тереза Турато |
| Karel, Neza Zupan | Карел, Нежа Жупан |
| Bojun, Jovan Kasun | Боюн, Йован Касун |
| Nenad Zupan / Mihael Loncar / Branko Jankovic | Ненад Жупан / Михаэль Лончар / Бранко Янкович |
| Radko Jordanov | Радко Йорданов |
| Mehmet / Selim Makryat | Мехмет / Селим Макрьят |
| Edgar Wellington / Arturo Faccia / Johann Winckelmann | Эдгар Веллингтон / Артуро Фачча / Иоганн Винкельман |
| Cult Skinning Knife | культовый нож для свежевания |
| Art (Skin Human) | Искусство (свежевание людей) |
| Repetier M95 carbine | карабин «Репетир» M95 |
| 8-mm Gaserov (Gasser) M98 revolver | револьвер 8-мм «Гассер» M98 |
