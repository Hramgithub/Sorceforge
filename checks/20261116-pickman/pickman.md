# «Pickman’s Legacy» (`pickmans-legacy-en`) — сверка полноты (Р-134, Р-251)

Часть `pickman`, вся книга. В PDF 11 страниц (кэш текста даёт 12-ю пустую — `pdftoppm` её не знает). Печатные номера
совпадают с физическими (на с. 2, 4–11 напечатаны 2, 4–11; на обложке с. 1 и в оглавлении с. 3 номеров нет) —
`offset: 0` (в `pipeline/source/books.json` не правилось). Источник — английский оригинал (Keegan Sullivan,
Miskatonic Repository, 2018); русский текст — наш перевод (флаг `translated`). Эпоха — наше время (`modern`).

Записи — `kb/books/pickmans-legacy-en/` (55): сценарий 1, сцены 17, персонажи 16, существо 1 (групповой профиль,
`instance_of` `coc:creature:ghoul`), организации 2, книга Мифов 1, предметы 5, раздатки 4, места 8. Карт в книге нет.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Pickman’s Legacy», логотип Miskatonic Repository | 1 | `scenario/pickmans-legacy` (sources); рисунок — `atmosphere.json` |
| Credits Page (автор, редактор, благодарности, художник, © 20018) | 2 | `scenario.summary` (автор, год), `scenario.sources`; юридическое — «Не взято» |
| Table of Contents | 3 | `scenario.sources` (оглавление) |
| Introduction | 4 | `scenario.summary`, `scenario.advice`, `scenario.hook` |
| Keeper Information | 4 | `scenario.keeper_info`; `character/joseph-pickman`, `sara-pickman`, `wendy-harper`; `organization/order-of-the-dark-moon`; `tome/cannibals-memoirs` |
| Meeting with Joseph Pickman | 4 | `scene/meeting-joseph-pickman`; `location/joseph-pickman-apartment`; `handout/police-report` |
| Conducting Research | 4 | `scene/saras-room` (ключ, Артур); `character/arthur-pickman` |
| Sara’s Room | 4–5 | `scene/saras-room`; `location/sara-room`; `handout/sara-diary` |
| NYU | 5 | `scene/nyu-professors`; `location/new-york-university` |
| • Cynthia Todd | 5 | `character/cynthia-todd` |
| • Shelley Roberts | 5 | `character/shelley-roberts` |
| • Garland Pomerleau | 5 | `character/garland-pomerleau`; `organization/boston-art-club` |
| • Darrell Borgman | 5 | `character/darrell-borgman` |
| • Stephen Welch | 5 | `character/stephen-welch` |
| Kim Madrigal | 5–6 | `scene/kim-madrigal`; `character/kim-madrigal` |
| David McDermott | 6 | `scene/david-mcdermott`; `character/david-mcdermott`; `location/mcdermott-apartment` |
| Fergus Gurule | 6 | `scene/fergus-gurule`; `character/fergus-gurule`; `item/pickman-gallery-painting` |
| The Gallery | 6 | `scene/the-gallery`; `location/harvard-art-museum` |
| Richard Upton Pickman | 6 | `scene/richard-upton-pickman`; `item/pickman-family-photographs`; `handout/the-missing-artist`; `character/christopher-thurber`; общий персонаж `sudba-bratev-vashington-ru/character/richard-apton-pikman` (связи и предложения) |
| Arkham, Massachusetts | 6–7 | `scene/arkham-arrival`; `creature/harper-ghouls`; `location/arkham-old-tunnels` |
| Miskatonic University | 7 | `scene/miskatonic-university`; `item/harper-dna-paper`; общее место `coc:location:miskatonic-university` |
| • Alfred Davis | 7 | `character/alfred-davis` |
| • Denise Mosher | 7 | `character/denise-mosher` |
| • Janice McGann | 7 | `character/janice-mcgann` |
| Wendy Harper | 7 | `scene/breaking-in` (адрес); `location/wendy-harper-apartment` |
| Breaking In | 7 | `scene/breaking-in`; `handout/wendy-harper-journal` |
| Calling Ahead | 7 | `scene/calling-ahead` |
| Stopping In | 7–8 | `scene/stopping-in` |
| Ambush | 8 | `scene/ambush`; `location/wendy-harper-lab`; `item/sara-cage` |
| Stalking in the Night | 8 | `scene/stalking-in-the-night`; `item/dried-human-flesh` |
| Desperation | 8 | `scene/desperation` |
| Conclusion | 8 | `scenario.conclusion` (награды Рассудка); `scene/conclusion` |
| Characters and Monsters | 9 | статблоки ниже |
| Wendy Harper, crazed cult scientist | 9 | `character/wendy-harper` (statblock) |
| Grave Eater’s Master (врезка) | 9 | `character/wendy-harper` (`abilities`, `statblock.spells`); черновик общей записи — `spell-draft-grave-eaters-master.json` |
| Ghouls (таблица One/Two/Three, Damage Bonus, атаки) | 9 | `creature/harper-ghouls` (`variants`) |
| The Pseudo-Ghoul That Was Sara Pickman | 9 | `character/sara-pickman` (statblock, `aliases`) |
| Handouts | 10–11 | раздатки ниже (текст en как напечатан + наш перевод, картинка-вырезка) |
| Police Report (Summary of the Boston Police) | 10 | `handout/police-report` |
| Diary (Excerpts from Sara’s Diary) | 10 | `handout/sara-diary` |
| The Missing Artist (Local Artist Missing!) | 11 | `handout/the-missing-artist` |
| Journal of Wendy Harper | 11 | `handout/wendy-harper-journal` |

## Опечатки и расхождения книги

- Год в выходных данных: «© 20018» (с. 2) — должно быть 2018 (в `scenario.quality.notes`; в `summary` — 2018).
- Оглавление (с. 3): раздел «Miskatonic Repository», в тексте (с. 7) — «Miskatonic University» (`scene/miskatonic-university` notes).
- Урон револьвера Харпер «1D8+1D4» (с. 9): БкУ к огнестрельному оружию не прибавляется, у Харпер БкУ 0 (`character/wendy-harper.errata`).
- Проверка Психологии против «Acting» Харпер (с. 8), а в статблоке (с. 9) такого навыка нет (`character/wendy-harper.errata`).
- Даты поездки в бостонскую галерею: выходные Дня труда (Боргман, с. 5), конец августа — начало сентября (Мадригал, с. 5), между 12 и 18 сентября (дневник, с. 10) (`scene/the-gallery.errata`).
- Как Сара увидела картину Пикмана: показала Харпер («Keeper Information», с. 4) или увидела на выставке с Гуруле (с. 6, 10) (`scenario.errata`).
- Мелочи без записи в `errata` (Р-39): «Pomerlau» (с. 5) вместо Pomerleau, «Sarah» (с. 5) вместо Sara (в `aliases` Сары), «grizzly figure» (с. 4) вместо grisly.
- Сомнения: «close until about four months ago» (Артур, с. 5) — вероятно, считая от исчезновения (пометка в записях); в «Stalking in the Night» Харпер тратит первый раунд боя на призыв двух упырей, хотя заклинание сотворяется 10 минут (вероятно, она зовёт уже укрощённых — не исправлялось); у упырей нет Скорости, Комплекции, ПМ и шанса «Укуса и хватки», у Харпер и Сары нет Уклонения (как напечатано).

## Термины (English → Russian)

| English | Русский |
|---|---|
| Pickman’s Legacy | Наследие Пикмана |
| Joseph Pickman | Джозеф Пикман |
| Sara Pickman | Сара Пикман |
| Arthur Pickman | Артур Пикман |
| Richard Upton Pickman | Ричард Аптон Пикман (как в базе) |
| Wendy Harper | Венди Харпер |
| Kim Madrigal | Ким Мадригал |
| David McDermott | Дэвид Макдермотт |
| Fergus Gurule | Фергус Гуруле |
| Cynthia Todd | Синтия Тодд |
| Shelley Roberts | Шелли Робертс |
| Garland Pomerleau | Гарланд Померло |
| Darrell Borgman | Даррелл Боргман |
| Stephen Welch (Coach Welch) | Стивен Уэлч (тренер Уэлч) |
| Alfred Davis | Альфред Дэвис |
| Denise Mosher | Дениз Мошер |
| Janice McGann | Дженис Макганн |
| Christopher Thurber | Кристофер Тёрбер |
| Peters (alias of Pickman) | Питерс |
| Keegan Sullivan / Faith Wilson / Marco Monte | Киган Салливан / Фейт Уилсон / Марко Монте |
| ghoul / ghouls | упырь / упыри (как в базе) |
| pseudo-ghoul | псевдоупырь |
| The Pseudo-Ghoul That Was Sara Pickman | Псевдоупырь, что была Сарой Пикман |
| full ghoul | полноценный упырь |
| ghoul guard | упырь-страж |
| Ghouls (Harper’s) | Упыри Венди Харпер |
| Grave Eater’s Master | Повелитель пожирателей могил |
| Order of the Dark Moon | Орден Тёмной Луны |
| Cannibal’s Memoirs | «Мемуары каннибала» |
| metamorphosis / transformation / the change | метаморфоза / превращение / изменение |
| crazed cult scientist | безумная учёная-культистка |
| venture capitalist | венчурный инвестор |
| Boston Art Club | Бостонский художественный клуб |
| Harvard Art Museum | Художественный музей Гарварда |
| traveling art gallery | передвижная (художественная) выставка |
| New York University (NYU) | Нью-Йоркский университет |
| Miskatonic University | Мискатоникский университет (как в базе) |
| Mott Haven | Мотт-Хейвен |
| 1 Huntington Avenue | Хантингтон-авеню, 1 |
| 157 Parker Way Apt 37 | Паркер-уэй, 157, кв. 37 |
| old North End of Boston | старый Норт-Энд Бостона |
| old sewers of Arkham / old man-made tunnels | старая канализация Аркхэма / старые рукотворные туннели (запись «Старые туннели под Аркхэмом») |
| storm drain | ливнёвка |
| Harper’s lab | Лаборатория Венди Харпер |
| Sara’s Room | Комната Сары Пикман (сцена — «Обыск комнаты Сары») |
| Police Report / Summary of the Boston Police | Полицейский отчёт / Сводка бостонской полиции |
| Diary / Excerpts from Sara’s Diary | Дневник Сары / Отрывки из дневника Сары |
| The Missing Artist / Local Artist Missing! | Пропавший художник / Пропал местный художник! |
| Journal of Wendy Harper | Журнал Венди Харпер |
| DNA Analysis of Human Beings and Anomalies in Evolution | «Анализ ДНК человека и аномалии эволюции» (выпускная работа Венди Харпер) |
| junk DNA | «мусорная ДНК» |
| Film and New Media / Art and Art History | «Кино и новые медиа» / «Искусство и история искусства» |
| Sound, Image, and Story; History of Film; Art History; Language of Film | «Звук, образ и история»; «История кино»; «История искусства»; «Язык кино» |
| Organic Chemistry II; Human Evolution; American Arts of the 1920s; Winter Ecology | «Органическая химия II»; «Эволюция человека»; «Американское искусство 1920-х»; «Зимняя экология» |
| wrestling team / Physical Education | команда борцов / физкультура |
| Labor Day weekend | выходные Дня труда |
| Meeting with Joseph Pickman | Встреча с Джозефом Пикманом |
| Conducting Research | Расследование |
| The Gallery | Галерея |
| Arkham, Massachusetts | Аркхэм, Массачусетс (сцена — «Аркхэм: тварь в ливнёвке») |
| Breaking In / Calling Ahead / Stopping In | Взлом квартиры Венди Харпер / Звонок Венди Харпер / Визит к Венди Харпер |
| Ambush / Stalking in the Night / Desperation / Conclusion | Засада / Слежка в ночи / Отчаяние / Развязка (сцена — «Развязка: судьба Сары») |
| Pickman’s Model (H. P. Lovecraft) | «Модель Пикмана» |
| Extreme (success) / Hard (roll) | чрезвычайный успех / сложная проверка |
| advantage | преимущество (вероятно, бонусный кубик — пометка в записях) |
| Strength roll | проверка СИЛ |
| Idea roll | проверка Идеи |
| Acting | Актёрское мастерство |
| Keeper | Хранитель |

## Не взято

- Физ. с. 2: юридическая оговорка (товарный знак Chaosium, программа OBS Community Content, логотип Miskatonic Repository) и
  «Special Thanks» (Kevin Dixon, Tanya Stere, Thomas DiModica, Tyler MacMillan) — не игровой материал (автор, год — в `summary`, остальное — в `sources.note`).
- Персонал дома Джозефа, бостонская полиция, соседи Харпер, дед Джозефа (брат Пикмана, без имени) — без имён и чисел; текстом в сценах и персонажах.
- Местное кафе (встреча с Харпер), газетные архивы Бостона, Гарвард (где учится Артур), ливнёвка в центре Аркхэма, работа Харпер — только упоминания; текстом в сценах.
- Ключ от комнаты Сары, киноафиши и неоконченные сценарии Сары — текстом в сцене и месте.
- Револьвер Харпер — атака в статблоке без ссылки на оружие (модель не названа, урон не сходится с таблицей).
- Пустая 12-я страница кэша текста — в PDF её нет.

## Картинки

- Раздатки (с. 10–11): 4 вырезки с серыми плашками — `app/art/handouts/pickman-*.webp`; рамки — `handout-boxes.json`, сопоставление — `art.json`, применено (`art-proposals.json`).
- Обложка (физ. с. 1, рисунок Marco Monte: бледная девушка у стены, пальцы будто с когтями) — `atmosphere.json`. Вопрос владельцу:
  отдать ли её Саре Пикман как портрет — книга рисунок не подписывает. Логотип Miskatonic Repository не берётся.

## Предложения правок общих записей

`proposals-pickman.json` — 19 предложений (пробный прогон `apply.py` проходит): абзацы «В „Наследии Пикмана“…» с источником и ссылками у
`coc:location:boston`, `coc:location:new-york`, `coc:location:arkham`, `coc:location:arkham-sewers`; у
`sudba-bratev-vashington-ru/character/richard-apton-pikman` — `name.en`, абзац описания и три источника. Вопрос ведущему:
Ричард Аптон Пикман теперь встречается во второй книге — по Р-154 его можно перенести в общую запись `coc:character:richard-upton-pickman`.

## Проверки

- `python tools/check.py kb/books/pickmans-legacy-en` — ошибок 0, предупреждений 0.
- `tools/completeness.py` (`completeness/`) — 2 находки: картинка обложки (физ. с. 1) → `atmosphere.json`; `tome/cannibals-memoirs` с флагом `incomplete` (книга не даёт характеристик).
- `tools/scenario_check.py` (`scenario/`) — 0 находок.
