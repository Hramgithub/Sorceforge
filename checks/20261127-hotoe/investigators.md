# HOTOE, кн. V «Strangers on the Train» — часть «investigators» (с. 65–92)

Источник: `hotoe-book-5-en`, печатные с. 65–92 (физ. 67–94; печатная = физическая − 2). Русский текст — наш перевод
(флаг `translated`, Р-251, Р-21); числа сверены с текстовым слоем и изображениями страниц (с. 67, 82, 83 — при 60–110 dpi).
Все записи — `kb/books/hotoe-book-5-en/`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Investigators (вступление: шесть сыщиков «Брэдфорд Плейерс» и шесть от спонсоров Kickstarter) | 65 | `quality.notes` и `legend` каждого из 12 прегенов (источник с. 65 у каждого) |
| (пустая страница) | 66 | не взято — пустой фон |
| Colonel Neville “Never” Goodenough — статблок, Notes | 67 | `character/neville-goodenough` |
| Goodenough — Entourage (пусто), Player Entries (бланк), Backstory | 68 | `character/neville-goodenough` (`background`) |
| Mrs. Elisabeth “Betty” Sunderland — статблок, Notes | 69 | `character/elisabeth-sunderland` |
| Sunderland — Backstory | 70 | `character/elisabeth-sunderland` (`background`) |
| Grace Murphy — статблок, Notes | 71 | `character/grace-murphy` (связь `works_for` → Сандерленд) |
| Murphy — Backstory | 72 | `character/grace-murphy` (`background`) |
| Margrave Milos Valinchek — статблок, Notes | 73 | `character/milos-valinchek` |
| Valinchek — Backstory | 74 | `character/milos-valinchek` (`background`) |
| Violet Davenport — статблок, Notes | 75 | `character/violet-davenport` |
| Davenport — Backstory | 76 | `character/violet-davenport` (`background`, `errata`) |
| Professor Alphonse Moretti — статблок, Notes | 77 | `character/alphonse-moretti` |
| Moretti — Backstory | 78 | `character/alphonse-moretti` (`background`) |
| Jarrod Holst — статблок, Notes (дубинка нгарлума) | 79 | `character/jarrod-holst`; `item/investigators-ngarluma-cudgel` |
| Holst — Backstory | 80 | `character/jarrod-holst` (`background`); `item/investigators-ngarluma-cudgel` |
| Christopher Macias — статблок, Notes | 81 | `character/christopher-macias` |
| Macias — Entourage: Winston, Age 3, Loyal Pug (статблок, фото); Backstory | 82 | `character/winston` (связь `works_for` → Масиас); `character/christopher-macias` (`background`) |
| Bryan Thao Worra — статблок, Notes | 83 | `character/bryan-thao-worra` |
| Thao Worra — Backstory | 84 | `character/bryan-thao-worra` (`background`) |
| Colonel Nathaniel R. Miller — статблок, Notes | 85 | `character/nathaniel-r-miller` |
| Miller — Backstory | 86 | `character/nathaniel-r-miller` (`background`) |
| Brett Bozeman — статблок, Notes | 87 | `character/brett-bozeman` |
| Bozeman — Backstory | 88 | `character/brett-bozeman` (`background`) |
| Lord Martin Alan-Brown — статблок, Notes | 89 | `character/martin-alan-brown` |
| Alan-Brown — Backstory | 90 | `character/martin-alan-brown` (`background`) |
| (логотип Chaosium) | 91 | не взято — служебная страница |
| (задняя обложка: герб Восточного экспресса, список городов) | 92 | не взято — обложка |

Портреты всех 12 прегенов и фото Уинстона — `images` записей (`checks/20261127-hotoe/art-investigators.json`, файлы
`app/art/characters/hotoe-investigators-*.webp`; вырезка — рамки в `.cache/lead-tools/gen-hotoe-investigators/boxes.json`).

## Не взято

- Графы «Entourage» (кроме Уинстона) и «Player Entries» (Special Knowledge, Special Skills, Special Items, Others) на
  чётных страницах 68–90 — пустые бланки для записей игрока.
- С. 66 — пустая страница; с. 91 — логотип Chaosium; с. 92 — задняя обложка. Атмосферных иллюстраций в разделе нет
  (файл `atmosphere-investigators.json` не нужен).
- Упомянутые без статблока люди — без отдельных записей, остаются текстом: Лили Гудинаф (покойная жена), Уолтер
  Дэвенпорт («Великолепный Уолтер Дэвенпорт», муж Вайолет), Милош Валинчек-старший (отец), Огюст-Эдуар Шове
  (пригласил Тхао Ворру), жена, двое детей, камердинер Томпсон и камеристка Милн лорда Алан-Брауна, шантажист Миллера.
  Кандидаты в записи, если глава их использует (особенно «жена» лорда Алан-Брауна — сюжетная зацепка без разгадки).
- Статуя «Ньяр» из лаосской пещеры и «культ Ньяр» — только в рассказе Тхао Ворры, без описания и механики; текстом в
  `legend`.

## Опечатки и сомнения

- Вайолет Дэвенпорт: графа «Injuries & Scars» (с. 76) дословно повторяет строку полковника Гудинафа («Walks with a
  limp, the result of an old war wound») — вероятно, ошибка вёрстки; Скорость 8 при СИЛ 65 и ЛВК 80 > ТЕЛ 50 (по
  правилам 9). Обе — `errata`, как напечатано.
- Брайан Тхао Ворра: Рассудок 23 совпадает с Мифами Ктулху 23% при МОЩ 80 — возможная ошибка набора (ожидалось бы 57);
  `errata`, как напечатано.
- Альфонс Моретти: в статблоке 66 лет, в заметках — «in his early sixties»; `errata`.
- Бетти Сандерленд: «English (own) 93)» — скобка вместо %, исправлено молча (Р-39). Кристофер Масиас: «Spot Hidden 30%,»
  — запятая в конце списка, молча.
- Лорд Алан-Браун: Рассудок 53 < МОЩ 65 — не опечатка (он «медленно сходит с ума»), пометка в `quality.notes`.
- Остальные производные (ПЗ, БкУ, Комплекция, Скорость с возрастной поправкой, половины/пятые) сходятся с правилами
  (проверено `tools/check.py`).
- Чужие страницы: оглавление пассажиров кн. V (с. 6) даёт страницы сыщиков на 2 больше напечатанных (физические:
  «Colonel Neville Goodenough … 69», «Lord Martin Alan-Brown … 91») — для части strangers-1.
- Колонтитул с. 83 «ASSENGERS» вместо «PASSENGERS» — мелочь вёрстки, не записана.

## Термины (English → русский)

| English | Русский |
|---|---|
| Investigators (ready investigators) | готовые сыщики |
| Bradford Players | «Брэдфорд Плейерс» (группа игроков записи на Yog-Sothoth.com) |
| Entourage | свита / спутники |
| Player Entries | записи игрока (бланк) |
| Backstory | предыстория |
| Royal Engineers | Королевские инженерные войска |
| Zulu Wars / the Great War | Зулусские войны / Великая война |
| Art/Craft (Technical Survey) | Искусство/ремесло (техническая съёмка) |
| Art/Craft (Shorthand) / (Typing) | Искусство/ремесло (стенография) / (машинопись) |
| Art/Craft (Dressmaking) / (Stage Magic) | Искусство/ремесло (шитьё) / (сценические фокусы) |
| Art/Craft (Writing) / (Poetry) / (Sculpture) | Искусство/ремесло (писательство) / (поэзия) / (скульптура) |
| Science (Biology / Chemistry / Pharmacy / Geology) | Наука (биология / химия / фармацевтика / геология) |
| Firearms (Handgun) / (Rifle/Shotgun) | Стрельба (пистолет) / (винтовка/дробовик) |
| .45 SMG | Пистолет-пулемёт .45 (атака «Стрельба (пистолет-пулемёт)», модель — «Томпсон») |
| Walking Stick | Трость |
| Cudgel | Дубинка |
| Machete | Мачете |
| Bite | Укус |
| Bark Noisily | Громко лаять |
| Fetch | Апорт |
| Scent | Нюх (`coc:skill:scent`) |
| Afrikaans | африкаанс |
| Egyptian Hieroglyphs | египетские иероглифы |
| Lao | лаосский |
| Tcho-Tcho (language) | чо-чо (как существо `coc:creature:cho-cho`) |
| The Silver Fox | Серебряная Лиса |
| God’s Country (Yorkshire) | «Божий край» (Йоркшир) |
| Valinchek Zbrani Firma | «Валинчек збрани фирма» |
| De Forest Phonofilm Corporation | корпорация «Де Форест Фонофильм» |
| Ngarluma | нгарлума (народ северо-запада Австралии) |
| Ngarluma cudgel | дубинка нгарлума |
| Roebourne | Робурн |
| The Father of All Bats | «Отец всех летучих мышей» (Ньярлатхотеп) |
| On the Other Side of the Eye | «По ту сторону глаза» |
| skinless snakeman | «бесшкурый человек-змей» |
| Nyar / Nyar Cult | «Ньяр» / «культ Ньяр» |
| Theosophist lodges | теософские ложи |
| Naga / Lan Xang | наги / Лансанг |
| Batrachophobia | батрахофобия (боязнь лягушек) |
| Salon Car | салон-вагон (как `hotoe-book-1-en/location/express-salon-car`) |
| Lady in Waiting / valet | камеристка / камердинер |
| Oil Baron | нефтяной барон |
| Military Attaché | военный атташе |
| Magician’s Assistant | ассистентка фокусника |
| Shady Historian | историк с тёмным прошлым |
| Dilettante and Landed Gentry | дилетант, землевладелец-аристократ |

Имена: Невилл «Невер» Гудинаф; Элизабет «Бетти» Сандерленд; Грейс Мёрфи; маркграф Милош Валинчек; Вайолет Дэвенпорт;
Альфонс Моретти; Джаррод Холст; Кристофер Масиас; Уинстон; Брайан Тхао Ворра; Натаниэль Р. Миллер; Бретт Боузман;
лорд Мартин Алан-Браун; Уолтер Дэвенпорт; Огюст-Эдуар Шове; Томпсон; Милн; Лили.

## Связи и профессии

- Профессии: Гудинаф и Миллер — «Военный (офицер)»; Сандерленд — «Археолог»; Мёрфи — «Секретарь»; Валинчек —
  «Торговец»; Дэвенпорт — «Фокусник»; Моретти — «Профессор»; Холст — «Психиатр»; Масиас и Тхао Ворра — «Писатель»;
  Алан-Браун — «Дилетант»; Боузман — без ссылки (профессии «нефтяной барон» нет).
- Оружие атак: «Трость» и «Дубинка» → «Дубинка полицейская» (по урону 1d6, вывод), «Мачете» → «Нож большой (мачете и
  т. п.)», «.45 SMG» → «Томпсон», остальное — по таблице.

## Предложения

Нет: все записи части — свои; ссылки из записи кампании на прегенов ставит ведущий.
