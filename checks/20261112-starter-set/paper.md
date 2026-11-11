# «Бумажный след» (Стартовый набор, `starter-paper-chase-ru`) — сверка переноса (часть paper)

Источник — официальное русское издание Стартового набора, «Бумажный след» (скан без текстового слоя, 12 страниц):
страницы распознаны `pdftoppm -r 200` + `tesseract -l rus`, каждое число сверено по изображению страницы (статблоки —
по вырезке при 200 dpi). Официальная раздатка — папка владельца `Стартовый набор (Starter Set)\Бумажный след\бумажный_1.jpg`
(на деле TIFF) и «официальная базовая раздатка», с. 11.

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Заставка (иллюстрация без номера) | 6 | 1 |
| Сценарий первый «Бумажный след» | 7–16 | 2–11 |
| «Бумажный след: персонажи и монстры» | 17 | 12 |

Смещение `starter-paper-chase-ru`: **печатная = физическая + 5** на всех страницах (2→7, 3→8, 7→12, 9→14, 12→17;
номера напечатаны внизу каждой страницы, кроме заставки). В `pipeline/source/books.json` смещение для этой книги не записано —
его стоит добавить (`"offset": 5`), файл мне не принадлежит. Колонтитул нечётных страниц — «Бумажный след», чётных — «Книга третья».

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (заставка: Дуглас Кимбол читает на кладбище) | 6 | сценарий `…/scenario/paper-chase` (sources) |
| Сценарий первый: Бумажный след (эпиграф Лавкрафта, «Для 1–2 сыщиков…», вступление) | 7 | сценарий: summary |
| Информация для Хранителя: предыстория | 7 | сценарий: keeper_info; `…/character/douglas-kimball` (legend); `coc:location:arnoldsburg`; `…/location/kimball-house`, `cemetery`, `favorite-gravestone`, `ghoul-tunnels-entrance` |
| Информация для игрока (с текстом для чтения вслух) | 7 | сценарий: hook; сцена `…/scene/start`; `…/character/thomas-kimball`; `…/organization/society-for-the-exploration-of-the-unexplained` |
| Начало (список шести вариантов) | 8 | сцена `…/scene/start`; сценарий: шаги «Поручение…», «Начало: варианты расследования» |
| Двое сыщиков (врезка) | 8 | сценарий: advice |
| Опросить соседей (с заметкой Хранителю) | 8 | сцена `…/scene/ask-neighbors`; `…/character/lila-odell` |
| Осмотреть кладбище | 8–10 | сцена `…/scene/cemetery`; `…/character/melodias-jefferson`; `…/location/cemetery` |
| (заметки Хранителю: повторная проверка, последствия провала; Запугивание и трудное Убеждение; сухой закон) | 9–10 | сцена `cemetery` (description, mechanics) |
| Поискать информацию в библиотеке (с заметкой Хранителю) | 10 | сцена `…/scene/library`; `…/location/library`; `…/item/advertiser-article`; `…/character/horace-whitmore` |
| Поговорить с полицией | 10 | сцена `…/scene/police`; `…/location/police-station`; `…/character/frank-murphy` |
| О кражах со взломом | 11 | сцена `police`; `…/character/jake-thompson` |
| О кладбище | 11 | сцена `police`; `…/location/cemetery` (описание) |
| О пропавшем дяде Томаса Кимбола, Дугласе | 11 | сцена `police`; `douglas-kimball` (legend) |
| «Арнольдсберг эдвертайзер» | 11 | сцена `…/scene/newspaper`; `…/organization/arnoldsburg-advertiser`; `…/location/advertiser-office`; `…/character/artie-malloy` |
| Информация из газеты (с заметкой Хранителю) | 11 | сцена `newspaper`; `…/item/reporter-notebook`; `…/character/hilda-ward` |
| Дом Кимболов (с заметкой Хранителю) | 11 | сцена `…/scene/kimball-house`; `…/location/kimball-house`, `douglas-study`; `…/item/douglas-diary`, `stolen-books` |
| Дальнейшие шаги (три варианта, заметка Хранителю об открытом финале) | 12 | сценарий: advice, шаг «Дальнейшие шаги» |
| Любимое надгробие Дугласа Кимбола | 12 | сцена `…/scene/favorite-gravestone`; `…/location/favorite-gravestone`, `ghoul-tunnels-entrance` |
| Карта «Владения Дугласа» (подпись «Карта дома Кимболов и кладбища», ключ 1–4) | 12 | карта `…/map/douglas-estate` (`app/maps/starter-paper-douglas-estate.jpg`, 4 метки 1–4); места 1–4: `kimball-house`, `douglas-study`, `favorite-gravestone`, `ghoul-tunnels-entrance` |
| Сыщик потерял сознание | 13 | сцена `favorite-gravestone` |
| Сыщик исследует тоннели | 13 | сцена `…/scene/tunnels`; `…/location/ghoul-tunnels` |
| Сыщик не спускается в тоннели | 13 | сцена `tunnels` |
| Встреча с Дугласом-упырём (с заметкой Хранителю) | 13 | сцена `tunnels` (description, mechanics) |
| Упыри (врезка с цитатой из «Модели Пикмана») | 13 | сценарий: keeper_info; `coc:creature:ghoul` (ссылки) |
| Наблюдение за домом или кладбищем (с заметкой Хранителю) | 14 | сцена `…/scene/watch` |
| Если сыщик хочет напасть на незнакомца (с двумя заметками Хранителю) | 14–15 | сцена `…/scene/attack` |
| Если сыщик смог убить или нокаутировать незнакомца (первая и вторая проверки, заметка о временном безумии, при провале / при успехе проверки Рассудка) | 15–16 | сцена `…/scene/kill-or-knockout`; `…/location/hospital` |
| Если сыщик хочет поговорить с незнакомцем | 16 | сцена `…/scene/talk` |
| Финал (три награды, улучшение навыков) | 16 | сценарий: conclusion, шаг «Финал» |
| Бумажный след: персонажи и монстры (вступление) | 17 | статблоки персонажей ниже |
| Мелодиас Джефферсон, 58 лет, смотритель | 17 | `…/character/melodias-jefferson` (статблок, описание, черты, роль) |
| Дуглас Кимбол, упырь (со сноской про 3 атаки) | 17 | `…/character/douglas-kimball` (статблок, броня, потеря Рассудка; `instance_of` `coc:creature:ghoul`) |
| Официальная раздатка «Владения Дугласа» (ключ 1–2) | — | раздатка `…/handout/douglas-estate-map`; карта `…/map/douglas-estate-players` (`app/maps/starter-paper-douglas-estate-players.jpg`, 2 метки) |

`…/` = `starter-paper-chase-ru/`. Город — новая общая запись `kb/locations/arnoldsburg.json` (Р-190); места сценария —
записи книги с `part_of` на город (все места в черте города, «Окрестности» не понадобились).

## Записи (43)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `paper-chase` |
| scene | 13 | `start`, `ask-neighbors`, `cemetery`, `library`, `police`, `newspaper`, `kimball-house`, `favorite-gravestone`, `tunnels`, `watch`, `attack`, `kill-or-knockout`, `talk` |
| location | 11 | общий город `coc:location:arnoldsburg`; книги: `kimball-house` (1), `douglas-study` (2), `cemetery`, `favorite-gravestone` (3), `ghoul-tunnels-entrance` (4), `ghoul-tunnels`, `library`, `police-station`, `advertiser-office`, `hospital` |
| map | 2 | `douglas-estate` (книга, 1–4), `douglas-estate-players` (раздатка, 1–2) |
| character | 9 | `douglas-kimball` (статблок), `melodias-jefferson` (статблок), `thomas-kimball`, `lila-odell`, `artie-malloy`, `hilda-ward`, `jake-thompson`, `frank-murphy`*, `horace-whitmore`* |
| item | 4 | `stolen-books`, `douglas-diary`, `advertiser-article`, `reporter-notebook` |
| handout | 1 | `douglas-estate-map` |
| organization | 2 | `society-for-the-exploration-of-the-unexplained`, `arnoldsburg-advertiser` |
| creature | 0 | упыри — общий вид `coc:creature:ghoul` (своих профилей стаи в книге нет); Дуглас — персонаж (Р-94) с `instance_of` |

\* имя придумано (Р-150), флаг `editorial_text`: в книге — «дежурный» и «библиотекарь».

Готовые сыщики Стартового набора (`startovyy-nabor-ru/character/*`, пять записей) — в ссылках сценария; сам текст
сценария их не называет (так и сказано в advice).

## Опечатки и сомнения

- Мелодиас Джефферсон: Скорость 8 (с. 17), по правилам — 7, с поправкой на 58 лет — 5. `errata` как напечатано (Р-161).
- Дуглас Кимбол: Скорость 5, по правилам — 7; возраст не указан («средних лет») — возможно, поправка на возраст. `errata`.
- «Потеряв все пункты здоровья (например, от двух попаданий из пистолета), Дуглас погибает» (с. 15) — но по статблоку
  он получает от огнестрельного оружия половину урона: два попадания 1d10 дают не больше 10 при 12 ПЗ. `errata` в сцене `attack`.
- Потеря Рассудка от Дугласа: статблок — 0/1d6 «за то, чтобы увидеть упыря»; сцены дают свои проверки (0/1d6 + 1/1d4 при
  осмотре тела; 0/1d4 и затем 1d4 при беседе); потеря при успехе проверки на стаю не указана. Пометки в записях, не опечатка.
- Ссылки на «Книгу вторую» Стартового набора (правила боя с. 18, «Приступы безумия» с. 17, «Награды» с. 22): книги нет в
  базе, ссылки ведут на правила «Книги хранителя» (`coc:rule:combat-round`, `bout-of-madness`, `investigator-development-phase`).
- Английские названия: «Paper Chase» (Р-217); Douglas Kimball, Thomas Kimball, Melodias Jefferson, Arnoldsburg, Society
  for the Exploration of the Unexplained — по памяти об оригинале, с английским изданием не сверялись (пометки в quality).
  Остальные имена — без `name.en`.

## Не взято

- Иллюстрации (с. 6 — заставка; с. 7 — портрет Дугласа; с. 9 — «Расследование на кладбище»; с. 13 — «Упырь»;
  с. 14 — «Дуглас Кимбол крадёт собственные книги»; с. 17 — портрет Джефферсона): картинки в записи не добавлялись
  (`app/art/` мне не принадлежит; можно добавить позже `pipeline/art/add_images.py`). Подписи иллюстраций — без данных.
- Картинка раздатки «Владения Дугласа» хранится как карта `douglas-estate-players` (`images` раздатки требует `app/art/`).
- Безымянные констебль из старой статьи, репортёр (автор блокнота), «общий знакомый» Томаса и соседи — упомянуты мимоходом,
  остались текстом в сценах и предметах; записей нет.
- Детройт (куда переехала миссис Уорд) и тюрьма Джейка Томпсона — только текст (`residence`), записей мест нет.
- Выпивка для подкупа ($2 за пол-литра) и бутылка Джефферсона — механика в сцене `cemetery`, отдельного предмета нет.

## Предложения

`proposals-paper.json` — 0 предложений: общие записи правок не требуют (город Арнольдсберг — новый, мой). Пробный прогон
`pipeline/integrate/apply.py --dry-run`: «правок: 0». Вне формата предложений: в `pipeline/source/books.json` добавить
`"offset": 5` для `starter-paper-chase-ru`.
