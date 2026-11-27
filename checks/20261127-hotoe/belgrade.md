# HOTOE, книга III — часть belgrade: «Little Cottage in the Wood: Beograd | Orašac 1923»

Страницы: книга III, с. 203–239, 261–263, 268–271 (физ. +2); книга VI, с. 125, 163, 165; Keeper Maps 9, 12; Player Maps 7.
Этап: `hotoe-book-3-en/scenario/little-cottage-in-the-wood` (order 14, `part_of` — кампания). Русское название главы — «Избушка в лесу» (как в записи кампании).

## Записи (85 файлов `kb/` + 3 карты-картинки + 8 картинок)

- Общие города (новые): `kb/locations/belgrade.json`, `kb/locations/orasac.json`.
- Места книги (31): `hotoe-book-3-en/location/belgrade-*` — вокзал, 12 мест ключа карты (отели «Европа», «Москва», «Петроград», Национальный музей, Большая рыночная площадь, Новый Конак, собор Святого Михаила, ратуша, больница, почтамт, Национальный банк, Бюро национальных сокровищ), «Турецкий город» (Дорчол, район), Базар, крепость и парк Калемегдан, две библиотеки, «Окрестности Белграда», аэродром Панчево; в Орашаце — церковь, дом Недичей, дом Филоповичей; «Окрестности Орашаца» (Шумадия), Младеновац, станция Копляре, Аранджеловац, старый лес, избушка в лесу, табор цыган.
- Карты (3): `belgrade-city`, `belgrade-city-players`, `belgrade-orasac` (копия для игроков в книге VI, с. 165, совпадает с картой Хранителя — отдельной записи нет).
- Сцены (21): `belgrade-arriving` … `belgrade-on-to-sofia` (порядок — `arc.order`).
- Персонажи (19): petar-riticht, statue-vendor, statue-thief, serbian-brawlers, turkish-brawlers, milovan-todorovic, vleja-radi, todor-nedic, ilija-nedic, marja-nedic, kristijan-filopovic, marko-markovic, luminitsa-venclovic, tsura-ljubisa, cigani-hunters, kcerca, ana-filopovic, grandmother, fortune-teller (без статблока: ilija-nedic, marko-markovic, luminitsa-venclovic, tsura-ljubisa, fortune-teller).
- Существа (3): `belgrade-walker-in-the-woods` (аватар, `avatar_of` Шуб-Ниггурат), `belgrade-dark-young` (`instance_of`, 3 варианта), `belgrade-baba-yagas-flock`.
- Организации (2): `belgrade-baba-yaga` (культ), `belgrade-cigani` (клан). Предметы (2): `belgrade-bone-pipe-whistle`, `belgrade-export-permit`. Раздатка (1): `belgrade-handout-1-nikephoros`.
- Правая рука симулякра — запись части campaign (`hotoe-book-1-en/item/campaign-simulacrum-right-arm`): ссылки из этапа и сцен, точное место — предложение.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Beograd \| Oraszac 1923: Little Cottage in the Wood (титул, подзаголовок, авторы) | 203 | этап: `summary` |
| Keeper Information | 203 | этап: `keeper_info`, `hook` |
| Belgrade (прибытие, Петар Ритихт) | 203–205 | сцена `belgrade-arriving`; `belgrade-station`; `petar-riticht` |
| Beograd (Belgrade) — врезка: History, People, Transport, Language, Money | 204 | `coc:location:belgrade` (`description`, `history`); `belgrade-turkish-town`; `belgrade-pancevo-airfield` |
| The Hotel | 205 | `belgrade-arriving`; `belgrade-hotel-moskva`, `belgrade-hotel-europa` |
| People To See, Things To Do; Meeting Dr. Todorovic | 205 | `belgrade-arriving` |
| Guidebooks and Maps; Dreaming in the Park | 205 | `belgrade-arriving`; `coc:location:belgrade`; `belgrade-kalemegdan-park` (Склон Грёз) |
| The Bazaar; Traveling Without a Guide; Five-Fingered Discount | 205–207 | сцена `belgrade-the-bazaar`; `belgrade-bazaar` |
| Карта Белграда (Reference 1–12) | 206, 262 | `belgrade-city`; таблица «Белград: места на карте» у города |
| Events in Belgrade in 1923 (врезка) | 207 | таблица «Белград: события 1923 года» у города (`from` в этапе) |
| The Fortune Teller | 207–208 | `belgrade-the-bazaar`; `fortune-teller` |
| The Arm; Chasing the Statue Thief (врезка); Brawl! | 208–209 | сцена `belgrade-the-arm`; `statue-vendor`, `statue-thief`, `serbian-brawlers`, `turkish-brawlers` |
| Narodni Muzej (The National Museum of Serbia); Dr. Milovan Todorovic, the Curator | 209–210 | сцена `belgrade-national-museum`; `belgrade-national-museum`; `milovan-todorovic` |
| The Supplier; Permits; Researching the Sedefkar Simulacrum | 210 | `belgrade-national-museum` |
| Bureau Of National Treasures | 210–211 | сцена `belgrade-bureau-of-national-treasures`; место; `vleja-radi`; `belgrade-export-permit` |
| About Orašac (врезка, Keeper's Note) | 211 | `coc:location:orasac`; этап `keeper_info` |
| Credentials, And A New Destination; Researching Orašac | 211–212 | сцена `belgrade-credentials-and-a-new-destination`; `belgrade-national-library`, `belgrade-university-library`; история — `coc:location:orasac` |
| Another Day, Another Train | 212 | сцена `belgrade-another-day-another-train` |
| Belgrade Handout #1 | 213 (книга VI, с. 125) | `belgrade-handout-1-nikephoros` (с картинкой) |
| A Stubborn Passenger; All Change; Nice Day for a Walk | 213 | `belgrade-another-day-another-train`; `belgrade-mladenovac`, `belgrade-kopljare-station` |
| Orašac: Keeper Information | 213–215 | сцена `belgrade-village-life`; этап `keeper_info` |
| Карта «Orašac and its place in Šumadija» | 214, 261 (книга VI, с. 165) | `belgrade-orasac`; таблица «Орашац: подписи на карте Шумадии» |
| Village Life | 215 | `belgrade-village-life`; `coc:location:orasac` |
| The Village Priest; Attitudes to the Village; Attitudes to the Cigani; Meeting the Antiquities Collector | 215–216 | `belgrade-village-life`; `kristijan-filopovic`, `ana-filopovic` |
| The Picture in the House | 216 | `belgrade-village-life`; `belgrade-filopovic-house` |
| The Village Mayor; An Invitation to Dinner, and Other Things | 216 | `belgrade-village-life`; `todor-nedic`; `belgrade-nedic-house` |
| The Pottery Objects | 217 | `belgrade-village-life`; `belgrade-bone-pipe-whistle` |
| Asking About the Antiquities Collector; Asking About the Forest | 217 | `belgrade-village-life`; `belgrade-forest` |
| The Cigani; Elder; Wise Woman; The Lonely Twin | 217–218 | `belgrade-cigani`; `marko-markovic`, `luminitsa-venclovic`, `tsura-ljubisa`; `belgrade-cigani-camp` |
| An Ancient Ritual | 218–219 | сцена `belgrade-an-ancient-ritual` |
| Whispers in the Night; Overnight Accommodation; The Nedic House; The Filopovic House | 219–220 | сцена `belgrade-overnight-accommodation` |
| The Little Cottage: Keeper Information; Into the Woods | 220–222 | сцена `belgrade-into-the-woods`; `belgrade-baba-yaga`; `belgrade-little-cottage` |
| About Baba Yaga (врезка) | 221 | `belgrade-baba-yaga` (`description`) |
| Whistle Blower; The Bone Pipe-Whistle (врезка) | 222 | `belgrade-bone-pipe-whistle` (`mechanics`); `belgrade-into-the-woods`; `belgrade-blow-the-house-down` |
| Kcerca; About the Singing; Items of Interest | 222–223 | сцена `belgrade-kcerca`; `kcerca` |
| Grandmother Returns; Grandmother's Story; Looking for the Arm | 223–224 | сцена `belgrade-grandmother-returns`; `grandmother` |
| Who's For Dinner?; Staying Free | 224–226 | сцена `belgrade-whos-for-dinner` |
| Blow The House Down; Outside the Cottage, Before; Inside the Cottage; Outside the Cottage, After | 226–228 | сцена `belgrade-blow-the-house-down` |
| Fresh Air; Escape; Baba Reborn; Fleeing the Forest; Armless | 226–229 | сцена `belgrade-escape` |
| Where Next?; Cigani and Safety; Back From the Dead?; Revenge (Hunting the Walker, Declining the Invitation); Loyalty Rewards | 229–230 | сцена `belgrade-where-next`; `cigani-hunters` |
| Orašac (возвращение) | 230–231 | сцена `belgrade-orasac-again`; `belgrade-orasac-church` |
| Making a Connection | 231 | сцена `belgrade-making-a-connection` |
| Attack; The Baba Yaga's Flock; A Minor Plague; The Observing Presence | 231–232 | сцена `belgrade-attack`; `belgrade-baba-yagas-flock` |
| On to Sofia; Conclusion | 232–233 | сцена `belgrade-on-to-sofia`; этап `conclusion`, таблица «Избушка в лесу: Рассудок» |
| Statistics: Petar Riticht, Statue Vendor, Statue Thief, Six Serbian/Turkish Brawlers, Dr. Milovan Todorovic, Vleja Radi, Todor Nedic, Marja Nedic, Father Filopovic, Six Cigani Hunters | 234–235 | персонажи (статблоки как напечатаны) |
| The Baba Yaga: Kcerca, Ana Filipovic, Grandmother, Special Abilities (Power of Three) | 236 | `kcerca`, `ana-filopovic`, `grandmother` (способность «Сила Троицы») |
| Baba Yaga's Flock | 236 | `belgrade-baba-yagas-flock` |
| Walker in the Woods, Avatar of Shub-Niggurath (Cult, Special Powers, Attacks) | 237–238 | `belgrade-walker-in-the-woods` |
| Dark Young of Shub-Niggurath | 238 | `belgrade-dark-young` |
| The Cottage (иллюстрация) | 239 | картинка `belgrade-little-cottage` |
| Orašac; Belgrade Keeper's Map; Belgrade Players' Map | 261–263 | карты `belgrade-orasac`, `belgrade-city`, `belgrade-city-players` (картинки — Keeper Maps 9, 12, Player Maps 7) |
| Index of Significant & Useful Entries | 268–271 | не взято (см. ниже) |

## Не взято

- Указатель книги III, с. 268–271 — навигация по страницам книги, не материал; его данные есть в записях (опечатка «Nephoros» отмечена у раздатки).
- Подписи рек на картах (River Danube, River Save, Sava River, Great Morava River, Major River, Tributary) и заголовки карт — меток нет, записей рек нет; дороги и железные дороги карты Шумадии — строкой таблицы у Орашаца.
- Отдельная карта для игроков «Орашац» — копия (книга VI, с. 165) не отличается от карты Хранителя; источник добавлен к `belgrade-orasac`.
- Заклинание «Command Flock*» у Бабушки — описания в книге нет (звёздочка отсылает к профилю стаи): в статблоке без ссылки, записи заклинания не заведено (кандидат, вопрос владельцу).
- Атмосферные картинки (10 страниц) — `atmosphere-belgrade.json`. «Картинки» на с. 204, 207, 210, 222 по `pdfimages` (completeness `art.record_without`) — фоновые текстуры врезок, не рисунки. Виньетки-силуэты с. 224–228 — оформление.
- Ниш — Црвени-Крст — общего города нет: черновик в `new-shared-locations-belgrade.json`; пока — текстом и меткой на «Окрестности Орашаца».

## Опечатки и расхождения книги

- Титул главы и таблица книги I: «ORASZAC/Oraszac»; в тексте и указателе — «Orašac» (alias у города).
- Тодорович: 57 лет в статблоке (с. 234), 48 в тексте (с. 209); Скорость 6 соответствует 40–49 годам — `errata`.
- Ана: заголовок статблока «ANA FILIPOVIC» (и в указателе), в тексте «Filopovic»; БкУ напечатан дважды («0» и «+1D4») — в записи 0 (`errata`, `corrections`).
- Кчерка: Уклонение «60% (30/10)» → 30/12 (исправлено, Р-35); Комплекция 0 при БкУ +1d4; «Age 19 (apparent)», в тексте «на вид около 16» (с. 220).
- Бабушка: ПЗ «13/39» (по характеристикам 9; сумма трёх жриц — 38), Комплекция «0/2» при БкУ +2d6 (должно 3) — как напечатано.
- Цыгане-охотники: Драка «50% (30/12)» → 25/10 (исправлено); ПЗ третьего и четвёртого 11 (по правилам 12; столбец ПЗ, видимо, из таблицы турецких драчунов); у дробовика «+1D4 (burn)» — строка факела (исправлено).
- Стая: «Pecks and Rips 50% (15/6)» → 25/10 (исправлено); БкУ 0 и Комплекция 1 при ТЕЛ 250 — задумано книгой (Р-76), как напечатано.
- Турецкие драчуны: Скорость 8 общей строкой, у четверых по правилам 7. Тодор Недич — Уклонение не напечатано. Влея Ради — Уклонение 25% ниже базы 27%.
- С. 219: «Investigators staying in the Todorovic household» — должно быть дом Филоповичей (Тодорович в Белграде); в сцене — дом Филоповичей.
- С. 232: «1/ID3» — исправлено молча на 1/1d3 (Р-39).
- Карта Белграда для Хранителя: номер 9 («Hospital») напечатан дважды; на карте для игроков — один.
- Расстояния: Орашац «fifty miles» (текст) и «47 Miles» (карта); Панчево «12½ miles» и «13 Miles»; Рудник «nears 4000 feet» и «3,714 ft» на карте.
- Сестра Цуры по слухам погибла от медведя (с. 218) или волков (с. 230).
- Отец Филопович «единственный свободно говорит по-английски», в статблоке английский 30%.

## Термины (англ. → рус.; новые формы главы)

| English | Русский |
|---|---|
| Little Cottage in the Wood | Избушка в лесу |
| Baba Yaga (priestesses) | Баба-яга; Баба-яги (жрицы) |
| Grandmother / Baba | Бабушка / Баба |
| Crone-Judge / Mother-Nurturer / Daughter-Bearer Aspect | облик старухи-судьи / матери-кормилицы / дочери-носительницы |
| Power of Three | Сила Троицы |
| Walker in the Woods | Бродящий в лесу |
| Song of Delusion | Песнь морока |
| Filament Network | Сеть волокон |
| Black Goat of the Woods (with a Thousand Young) | Чёрная Коза Чащоб (с Легионом Младых) — по глоссарию |
| Thousand Young | Тысяча Младых |
| Dark Young of Shub-Niggurath | Тёмная молодь Шуб-Ниггурат — по глоссарию |
| Baba Yaga's Flock | Стая Бабы-яги |
| cigani / gypsies | цыгане (цигани) |
| bone pipe-whistle | костяная дудка-свисток |
| Bureau of National Treasures | Бюро национальных сокровищ |
| permit of export | разрешение на вывоз (древностей) |
| Narodni Muzej (National Museum of Serbia) | Национальный музей Сербии (Народный музей) |
| Slope of Dreaming | Склон Грёз |
| Kalemegdan Fortress / Park | крепость / парк Калемегдан |
| ‘Turkish Town’ (Dorcol) | «Турецкий город» (Дорчол) |
| Great Market Place | Большая рыночная площадь |
| The New Konak (Palace) | Новый Конак (дворец) |
| Great War Island | остров Великой войны |
| Pancevo Airfield | аэродром Панчево |
| Orašac / Arandjelovac / Mladenovac / Kopljare / Topola / Kragujevac | Орашац / Аранджеловац / Младеновац / Копляре / Топола / Крагуевац |
| Nis-Crveni Krst | Ниш — Црвени-Крст |
| Šumadija | Шумадия |
| Kosmaj / Bukulja / Venčac / Rudnik / Avala / Presexa Hill | Космай / Букуля / Венчац / Рудник / Авала / холм Пресекса |
| Moesia (Superior) | (Верхняя) Мёзия |
| Cybele | Кибела — по глоссарию |
| Nikephoros I; Droungarios | Никифор I; друнгарий |
| Dahias; knezes; Janissaries | дахии; кнезы; янычары |
| Karađorđe Petrović | Карагеоргий Петрович |
| Hadži-Mustafa | Хаджи-Мустафа |
| Serbo-Croatian; Romani; Archaic Dialect | сербохорватский; цыганский (романи); архаичный диалект |
| Folk History; Gossip; Political In-Fighting; Smuggle; Theology | Народная история; Сплетни; Политические интриги; Контрабанда; Богословие (навыки без механики, Р-126) |
| Disapproval; Cackle Gleefully; Shovel into Oven; Cluck Menacingly | Неодобрение; Злорадный хохот; Сунуть в печь; Угрожающее кудахтанье |
| Art (Tapestry) / Art (Sing) | Искусство (гобелен) / Искусство (пение) |
| Hotel Moskva / Europa / Petrograd | отель «Москва» / «Европа» / «Петроград» |
| Svetozar Markovic University Library | Университетская библиотека «Светозар Маркович» |

Имена: Петар Ритихт, Милован Тодорович, Влея Ради, Кристиян и Ана Филопович, Тодор, Илия и Марья Недич, Марко Маркович, Луминица Венцлович, Цура Любиша, Кчерка. Придуманы (Р-150/151): торговец статуями — Драган Илич, вор — Мехмед Хасанович, имена драчунов и охотников (`names`). гадалка — Стана Петрович.
