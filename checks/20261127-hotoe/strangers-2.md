# HOTOE, книга V «Strangers on the Train», с. 35–64 — часть strangers-2

Источник: `hotoe-book-5-en` (печатная страница = физическая − 2). Пятнадцать пассажиров и служащих поезда со свитами:
30 персонажей `hotoe-book-5-en/character/*` (все `npc`, эпоха `1920s`, флаг `translated`), 15 портретов
(`app/art/characters/hotoe-strangers-2-*.webp`, сопоставление `art-strangers-2.json`, применено к своим записям).
Атмосферных иллюстраций на с. 35–64 нет (только фотопортреты), поэтому `atmosphere-strangers-2.json` не заводился.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Homer Banner (Age 33, American Journalist and Writer) | 35 | `character/homer-banner` (+ портрет) |
| Entourage: Mrs. Margaret Banner, Faithful Wife | 36 | `character/margaret-banner` |
| Walter Partridge (Age 40, English Train Buff) | 37 | `character/walter-partridge` (+ портрет) |
| Entourage: Allen Carmichael, Temporary Manservant | 38 | `character/allen-carmichael` |
| Kay Montague (Age 29, Social Climber) | 39 | `character/kay-montague` (+ портрет) |
| Entourage: Amy Van Patton, Fellow Social Climber | 40 | `character/amy-van-patton` |
| Daisy Cannon (Age 22, American Heiress) | 41 | `character/daisy-cannon` (+ портрет) |
| Entourage: Matilda Simpson, Matronly Maid; Sam Miller P. I., Secret Bodyguard | 42 | `character/matilda-simpson`, `character/sam-miller` |
| Madam Arcana (Age 53, Medium from Marseille) | 43 | `character/madam-arcana` (+ портрет) |
| Entourage: Cybelle Francis, Assistant Medium; Margorie Endicott, Maid and Confidant | 44 | `character/cybelle-francis`, `character/margorie-endicott` |
| Doreen O'Bannon (Age 33, Irish Invalid) | 45 | `character/doreen-obannon` (+ портрет) |
| Entourage: Alice O'Malley, Doting Nurse; Jim Allen, Devoted Servant | 46 | `character/alice-omalley`, `character/jim-allen` |
| François LaVerge (Age 26, Broken-Hearted Lover) | 47 | `character/francois-laverge` (+ портрет) |
| Entourage / Keeper Entries (пусто) | 48 | не взято (пустые бланки) |
| Jean Pourvois (Age 55, French Manufacturer) | 49 | `character/jean-pourvois` (+ портрет) |
| Entourage: Fi Fi Dulouvre, Bored Prostitute; Jacques Artuad, Bored Manservant | 50 | `character/fi-fi-dulouvre`, `character/jacques-artuad` |
| Franklin Myers (Age 37, American Antiquarian) | 51 | `character/franklin-myers` (+ портрет); экземпляр «Unaussprechlichen Kulten» — предложение в `copies` общей книги |
| Entourage / Keeper Entries (пусто) | 52 | не взято (пустые бланки) |
| Patrick Jensen (Age 42, Travel Writer) | 53 | `character/patrick-jensen` (+ портрет) |
| Entourage / Keeper Entries (пусто) | 54 | не взято (пустые бланки) |
| Rene Clement (Staff) (Age 50, Senior Conductor) | 55 | `character/rene-clement` (+ портрет) |
| Entourage: Armand Chavelle, Assistant; Ricarde Allou, Another Assistant | 56 | `character/armand-chavelle`, `character/ricarde-allou` |
| Pierre Marchand (Staff) (Age 37, Conductor) | 57 | `character/pierre-marchand` (+ портрет) |
| Entourage / Keeper Entries (пусто) | 58 | не взято (пустые бланки) |
| Lorenzo Berce (Staff) (Age 22, Ambitious Waiter) | 59 | `character/lorenzo-berce` (+ портрет) |
| Entourage / Keeper Entries (пусто) | 60 | не взято (пустые бланки) |
| Paul DeGuerre (Staff) (Age 49, Chef de Cuisine) | 61 | `character/paul-deguerre` (+ портрет) |
| Entourage: Richard Montalou, Assistant Chef; Jean Renour, Pastry Chef | 62 | `character/richard-montalou`, `character/jean-renour` |
| Emile Duchamps (Staff) (Age 33, Conductor) | 63 | `character/emile-duchamps` (+ портрет) |
| Entourage / Keeper Entries (пусто) | 64 | не взято (пустые бланки) |

Все id — `hotoe-book-5-en/character/<slug>`.

## Не взято

- Бланки «Keeper Entries» на каждой чётной странице (Special Knowledge, Special Skills, Others, Special Items) и пустые
  бланки «Entourage» на с. 48, 52, 54, 58, 60, 64 — пустые формы для записей Хранителя, текста нет.
- Колонтитулы «Passengers» / «Entourage», рамки и фоновые картинки страниц — оформление.

## Связи и предложения

- Свиты: `relative_of` (Маргарет Баннер — Гомер Баннер), `knows` (Эми Ван Паттон — Кей Монтегю), остальные спутники и
  помощники — `works_for` своему пассажиру.
- `proposals-strangers-2.json` (10): экземпляр Майерса в `coc:tome:unaussprechlichen-kulten.copies`; служащие поезда
  в `refs` вагона-ресторана (`hotoe-book-1-en/location/express-dining-car`: Дегерр, Монталу, Ренур, Берсе) и спального
  вагона (`express-sleeping-car`: Клеман, Шавель, Аллу, Маршан, Дюшан). Пробный прогон `apply.py` — ложится целиком.
- Ссылки только текстом, без записи: Бифф Бакстер (с. 19, часть strangers-1, у Дюшана), «Спутник путешественника»
  (`hotoe-travelers-companion-en`, у Дженсена; запись — после части companion), Чёрный камень фон Юнцта (у Майерса),
  капитан Эдуар Гуляр, Майкл О’Бэннон.

## Опечатки и сомнения

- Эмиль Дюшан (с. 63): статблок в шкале прежних редакций (СИЛ 12 … ОБР 15, «SAN 85», «Weapons: none») — не переведён
  в 7-ю; оставлен как напечатан, `errata` с ×5-значениями (60…85); Комплекция, Скорость, Уклонение не напечатаны.
- Скорость не по правилам (Р-161, `errata`, как напечатано): Эми Ван Паттон 8 (по правилам 7), Мадам Аркана 6 (5 с
  поправкой за 53 года), Ришар Монталу 9 (8), Жан Ренур 9 (8), Матильда Симпсон 8 (9; возраст не указан —
  возможно, поправка за возраст).
- Эми Ван Паттон: Рассудок 70 при МОЩ 45 — так в книге (в заметке записи).
- Список пассажиров (с. 6): «Paul DeGeurre», «Jean Porvois» — в псевдонимах записей; в статьях — DeGuerre, Pourvois.
- Заголовки «RENE CLEMENT», «LORENZO BERCE» без диакритики, в тексте — «Bercé»; `name.en` — Rene Clement (как в
  заголовке, «René Clement» — псевдоним), Lorenzo Bercé (как в тексте).
- Майерс: в книге «Unausprechlichen Kulten» (пропущена «s»).
- «Contact Dead» (Мадам Аркана) сопоставлено с `coc:spell:contact-spirits-of-the-dead` по названию (вывод, Р-41);
  у Сибель Франсис «Contact Dead 12%» стоит среди навыков — оставлен навыком без ссылки.
- Мелкое оформление (не в `errata`): «Sanity80», «71 %», «English (own) 93» без %, «+0», «+1 D4», «APP 50E DU 45»
  (текстовый слой; на изображении APP 50, EDU 45), «45%.Dreaming».

## Термины (English → русский)

| English | Русский |
|---|---|
| Entourage | свита |
| Keeper Entries | записи Хранителя (бланк, не взят) |
| Staff | персонал поезда |
| Senior Conductor | старший проводник |
| Conductor | проводник |
| Chef de Cuisine | шеф-повар |
| Assistant Chef | помощник шеф-повара |
| Pastry Chef | кондитер |
| Ambitious Waiter | честолюбивый официант |
| Train Buff | любитель поездов |
| Train Lore | Знание поездов (как в книге II) |
| Social Climber | карьеристка, рвущаяся в высший свет |
| Heiress | наследница |
| Medium | медиум |
| spirit guide | дух-проводник |
| séance | спиритический сеанс |
| Invalid | больная |
| Broken-Hearted Lover | влюблённый с разбитым сердцем |
| Manufacturer | фабрикант |
| Antiquarian | антиквар |
| Travel Writer | автор путеводителей |
| Traveler's Companion | «Спутник путешественника» |
| Black Stone | Чёрный камень |
| Contact Dead | Связь с мёртвыми (навык Сибель); заклинание — «Связь с духами мёртвых» |
| Credit Rating (Apparent) | Средства (напоказ) |
| Evaluate (Social) Class | Определять положение в обществе |
| Courtesy | Учтивость |
| Be Discreet | Не привлекать внимания |
| Report to Daisy's Mother | Докладывать матери Дейзи |
| Hide | Прятаться |
| Ski | Лыжи |
| Oratory | Ораторское искусство |
| Bon Mot | Острое словцо |
| Work Unobtrusively | Работать незаметно |
| Time Food | Подавать блюда вовремя |
| Homer Banner | Гомер Баннер |
| Margaret Banner | Маргарет Баннер |
| Walter Partridge | Уолтер Партридж |
| Allen Carmichael | Аллен Кармайкл |
| Kay Montague | Кей Монтегю |
| Amy Van Patton | Эми Ван Паттон |
| Daisy Cannon | Дейзи Кэннон |
| Matilda Simpson | Матильда Симпсон |
| Sam Miller | Сэм Миллер |
| Madam Arcana (Blanche Goulart) | Мадам Аркана (Бланш Гуляр) |
| Cybelle Francis | Сибель Франсис |
| Margorie Endicott | Марджори Эндикотт |
| Doreen O'Bannon | Дорин О’Бэннон |
| Alice O'Malley | Элис О’Мэлли |
| Jim Allen | Джим Аллен |
| François LaVerge | Франсуа Лаверж |
| Jean Pourvois | Жан Пурвуа |
| Fi Fi Dulouvre | Фифи Дюлувр |
| Jacques Artuad | Жак Артюад |
| Franklin Myers | Франклин Майерс |
| Patrick Jensen | Патрик Дженсен |
| Rene Clement | Рене Клеман |
| Armand Chavelle | Арман Шавель |
| Ricarde Allou | Рикар Аллу |
| Pierre Marchand | Пьер Маршан |
| Lorenzo Bercé (Harold Smith) | Лоренцо Берсе (Гарольд Смит) |
| Paul DeGuerre | Поль Дегерр |
| Richard Montalou | Ришар Монталу |
| Jean Renour | Жан Ренур |
| Emile Duchamps | Эмиль Дюшан |
