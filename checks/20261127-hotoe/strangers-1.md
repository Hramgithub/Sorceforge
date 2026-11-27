# HOTOE, книга V — часть strangers-1: «Strangers on the Train», с. 1–34

Источник — английский оригинал (`hotoe-book-5-en`, печатная = физическая − 2). Русский текст — наш перевод
(`translated`, Р-251, Р-21). Записи — в `kb/books/hotoe-book-5-en/` (Р-254).

Записей: 41 — персонажи 39 (15 статей пассажиров: 16 пассажиров, «Тайные агенты» — двое; 21 спутник из «Свиты»;
2 кошки), правила 2 (`rule/strangers-famous-faces`, `rule/strangers-passengers`). Картинки: 18 портретов
(`app/art/characters/hotoe-strangers-1-*.webp`; фото Херрингов — у обоих супругов, фото кошек — у обеих кошек;
рамки вырезки — `art-strangers-1-boxes.json`), предложения картинок применены к своим записям
(`art-strangers-1-proposals.json`). Атмосфера — `atmosphere-strangers-1.json` (6). Предложения к чужим записям —
`proposals-strangers-1.json` (2, навигационные ссылки без `corrections`).

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, рекламная страница Chaosium | физ. 1–2 | не взято (см. ниже); картинки — `atmosphere-strangers-1.json` |
| Титульный лист, выходные данные | 1–2 | не взято (см. ниже) |
| Famous Faces Aboard: 1890–1900, After 1900, After 1920 | 3–4 | `rule/strangers-famous-faces` (таблица «Знаменитости на борту», 15 строк) |
| Strangers on the Train: Divers Personages Available For The Keeper’s Purposes, Or As New Investigators | 5 | `rule/strangers-passengers` (text, aliases) |
| Passengers | 5 | `rule/strangers-passengers` (text) |
| Key (строка боя) | 5 | `rule/strangers-passengers` (text) |
| List of Passengers | 6 | `rule/strangers-passengers` (таблица «Список пассажиров»; ссылки на записи с. 7–34) |
| Simon Johns | 7 | `character/simon-johns` |
| Entourage: Mrs. Amanda Johns, Miss Mary Baxter | 8 | `character/amanda-johns`, `character/mary-baxter` |
| Colonel and Mrs. Herring: Col. Andrew Herring (Ret.), Mrs. Agnes Herring | 9 | `character/andrew-herring`, `character/agnes-herring` |
| Entourage: Mr. Albert Rumsford, Miss Annabelle Hawkins | 10 | `character/albert-rumsford`, `character/annabelle-hawkins` |
| Kerim Mahtuk | 11 | `character/kerim-mahtuk` |
| Entourage: Çürügü Yaryı, Yolculuk Tutuyor | 12 | `character/curugu-yaryi`, `character/yolculuk-tutuyor` |
| Lorna Cambell-Barnes | 13 | `character/lorna-cambell-barnes` |
| Entourage: Roger Dipcott, Gertrude Wentworth | 14 | `character/roger-dipcott`, `character/gertrude-wentworth` |
| Roger Whipsnade, Lord Palfrey | 15 | `character/roger-whipsnade` |
| Entourage: Armand Applegate, Miss Karen Lindon | 16 | `character/armand-applegate`, `character/karen-lindon` |
| Andre / Andrea Stefani | 17 | `character/andre-andrea-stefani` |
| Entourage: Tomas Infuego, Miss Carmina Ferrara | 18 | `character/tomas-infuego`, `character/carmina-ferrara` |
| Biff Baxter | 19 | `character/biff-baxter` (конь Молния — в тексте) |
| Entourage: Mr. J. B. Bramwell, Miss Penelope Barnes | 20 | `character/j-b-bramwell`, `character/penelope-barnes` |
| Humphrey Enderly | 21 | `character/humphrey-enderly` |
| Entourage: Mr. Albert Swanson | 22 | `character/albert-swanson` |
| Seregena Androkovna Rankenberg | 23 | `character/seregena-androkovna-rankenberg` |
| Entourage: Vladimir Veslenka, Marie Rimbaud | 24 | `character/vladimir-veslenka`, `character/marie-rimbaud` |
| The Secret Agents: Roman Petrov, Nikolai Vasiliev | 25 | `character/roman-petrov` (связь `rival_of`), `character/nikolai-vasiliev` |
| Entourage (пустые формы) | 26 | не взято (см. ниже) |
| Yves Rostande | 27 | `character/yves-rostande` (связь `knows` → `character/paul-deguerre`, часть strangers-2) |
| Entourage: Jacques Pouret, Luc Gesparde | 28 | `character/jacques-pouret`, `character/luc-gesparde` |
| Ronald Lakeby | 29 | `character/ronald-lakeby` |
| Entourage (пустые формы) | 30 | не взято (см. ниже) |
| Dr. Vincenzo Gaspari | 31 | `character/vincenzo-gaspari` |
| Entourage: Dr. Antonio Visconti | 32 | `character/antonio-visconti` |
| Lady Margaret Bramwell; Charlotte, Siamese Cat; Emily, Siamese Cat | 33 | `character/margaret-bramwell`, `character/charlotte-siamese-cat`, `character/emily-siamese-cat` (`instance_of` → `coc:creature:ordinary-cats`) |
| Entourage: Gertrude Rosewater | 34 | `character/gertrude-rosewater` |
| Keeper Entries (на каждой чётной странице 8–34) | 8–34 | не взято (см. ниже) |

## Не взято

- Обложка, рекламная страница Chaosium (физ. 1–2), титульный лист и выходные данные (с. 1–2) — не содержание книги;
  картинки записаны в `atmosphere-strangers-1.json`.
- Формы «Keeper Entries» на страницах «Свиты» (с. 8–34) и страницы 26 и 30 целиком («Entourage» без статблоков) —
  пустые бланки для заметок Хранителя, текста нет.
- Без статблоков и без записей (остались текстом в описаниях): отец Саймона — дипломат в Венеции (с. 7); покойный
  муж Лорны Джон Барнс и её «нынешний спутник» (с. 13); мать лорда Палфри (с. 15); конь Биффа Бакстера Молния
  (Lightning) и его возможный агент среди пассажиров (с. 19); богатый клиент Эндерли в Константинополе (с. 21); две
  горничные, лакей и две борзые княжны Ранкенберг (с. 23).
- Реальные знаменитости «Famous Faces Aboard» (с. 3–4) — строки таблицы правила, отдельных записей нет.

## Опечатки и сомнения книги (в `errata`)

- Бифф Бакстер, драка «65% (12/5)» — доли от 25%; доли исправлены на 32/13 (Р-77), возможна опечатка в проценте.
- Дж. Б. Брэмвелл, револьвер .38 «58% (28/11)» — доли от 56%; половина исправлена на 29 (Р-77).
- Андре / Андреа Стефани: строка языков спутана («English, 60% (own) Italian 65%»), английский дважды (45% и 60%).
- Лорд Палфри: родной английский дважды (55% в навыках, 25% в языках); Скорость 7 при расчётной 8.
- Леди Маргарет Брэмвелл: «English (own) 65%, English 55%».
- Доктор Антонио Висконти: родной язык итальянского врача напечатан «English (own) 93%».
- Кошка Эмили: Скорость 10 (кошачья, расчёт по человеческому правилу — 9) и Уклонение 45% при половине ЛВК 47%.
- Без `errata` (пометки в `quality.notes`): карабин .30 Биффа 2d6+3 (в справочнике 2d6); «22 Automatic» Кармины
  (пропущена точка); у Гертруды Уэнтворт нет строки языков; у Серегены, Васильева и Ростанда родной язык без «own»;
  сноска «*Charlotte and Emily will also defend…» без звёздочки в статблоке леди Брэмвелл; в списке пассажиров —
  «Seregane» и «Paul DeGeurre» (в статьях «Seregena», «DeGuerre»); ПЗ Мэри Бакстер 13 при расчётных 12 (округление
  вверх — приём книги, Р-161).

## Связи с другими частями

- `character/yves-rostande` → `hotoe-book-5-en/character/paul-deguerre` (запись части strangers-2, уже есть).
- `rule/strangers-passengers` ссылается на поезд `hotoe-book-1-en/location/express-simplon-orient-express` и правила
  `express-…`; предложено обратные навигационные ссылки добавить в поезд и в «Общество Симплон-Ориент-экспресса».

## Термины (английский → русский)

| English | Русский |
|---|---|
| Strangers on the Train | Незнакомцы в поезде |
| Famous Faces Aboard | Знаменитости на борту |
| Passengers | Пассажиры |
| List of Passengers | Список пассажиров |
| Entourage | Свита |
| Keeper Entries | Записи Хранителя |
| Key | Ключ |
| Orient Express / Simplon-Orient Express | Восточный экспресс / Симплон-Ориент-экспресс |
| Staff | служащие (персонал) поезда |
| The Secret Agents | Тайные агенты |
| Cheka / NKVD / KGB | ЧК / НКВД / КГБ |
| Cheka Agent / Czarist Agent | агент ЧК / царский агент |
| White Russian | белый русский (белоэмигрант) |
| Romanov Princess | княжна из дома Романовых |
| Borzois | борзые |
| Cat Burglar | вор-домушник |
| gigolo | жиголо |
| Peer of the Realm | пэр королевства |
| Duchy of Derbyshire | герцогство Дербишир |
| stateroom | купе |
| Second Class / First Class | второй класс / первый класс |
| dining car | вагон-ресторан |
| Chef de Cuisine | шеф-повар |
| Guide Michelin | гид «Мишлен» |
| Marvel Cinema Corp. | «Марвел синема корпорейшн» |
| Lightning (horse) | Молния |
| Ice Pick | шило для льда |
| Chef’s Knife | поварской нож |
| Heavy Epee (sharpened) | тяжёлая шпага (заточенная) |
| Fencing Foil | фехтовальная рапира |
| Slingshot | рогатка |
| Hickory Switch | ореховый прут |
| Claws | когти |
| Gastronomy / Taste / Wine Lore | Гастрономия / Вкус / Знание вин |
| Linguist | Полиглот |
| Intrigue / Politics | Интриги / Политика |
| Gossip | Сплетничать |
| Lariat | Лассо |
| Siamese Cat | сиамская кошка |
| Legion of Honor | орден Почётного легиона |
| Ismaili | исмаилиты |

Имена (`name.ru`): Саймон Джонс, Аманда Джонс, Мэри Бакстер, Эндрю Херринг, Агнес Херринг, Альберт Рамсфорд,
Аннабелла Хокинс, Керим Махтук, Чюрюгю Ярый, Йолджулук Тутуйор, Лорна Кэмбелл-Барнс, Роджер Дипкотт, Гертруда
Уэнтворт, Роджер Уипснейд, лорд Палфри, Арманд Эпплгейт, Карен Линдон, Андре / Андреа Стефани, Томас Инфуэго, Кармина
Феррара, Бифф Бакстер, Дж. Б. Брэмвелл, Пенелопа Барнс, Хамфри Эндерли, Альберт Суонсон, Серегена Андроковна
Ранкенберг, Владимир Весленка, Мари Рембо, Роман Петров, Николай Васильев, Ив Ростанд, Жак Пуре, Люк Геспард, Рональд
Лейкби, Винченцо Гаспари, Антонио Висконти, Маргарет Брэмвелл, Шарлотта, Эмили, Гертруда Роузуотер; Поль Дегерр — по
записи strangers-2.

Шуточные навыки свиты («Catch Simon», «Please Lorna», «Hiss At Intruder» и т. п.) переведены в статблоках с английским
оригиналом в скобках; механики у них нет (Р-126).
