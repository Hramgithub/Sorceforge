# «Скрюченный домище» («Особняки безумия. За закрытыми дверями», `osobnyaki-bezumiya-ru`) — сверка переноса (часть crooked)

Источник — официальное русское издание (Hobby World, скан без текстового слоя): текст `.cache/ocr/osobnyaki-bezumiya-ru/`
(tesseract) лишь подспорье; все страницы главы прочитаны по изображениям (`pages.py image`, 120–200 dpi), статблоки — по
вырезкам 200 dpi. Английское издание 6e («The Crack'd and Crook'd Manse», Mansions of Madness, 1990, с. 54–60) — только для
`name.en` и сверки смысла; числа из него не брались (Р-218).

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 2 «Скрюченный домище» | 41–67 (иллюстрация-разворот «Отродье Шуб-Ниггурат» — с. 40; с. 68 — полностраничная иллюстрация перед гл. 3) | 42–68 |
| «Материалы для игроков»: «Домище 1»–«Домище 6», план поместья, план дома | 191–195 | 192–196 |

Смещение: **печатная = физическая − 1** на всех проверенных страницах (41, 52, 59, 65, 191, 195).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 2. Скрюченный домище (вступление, история публикации, сноски) | 41 | сценарий `…/scenario/crooked-manse` (summary) |
| Информация для Хранителя: «Дом Фицджеральдов 60 лет назад», «30 лет назад», «месяц назад», «сегодня» | 41–42 | сценарий: keeper_info (пролог); `…/character/crooked-john-fitzgerald`, `-william-fitzgerald`, `-arthur-curwen`, `-arthur-cornthwaite`; предмет `…/item/crooked-shotgun-shells` |
| Время и место действия (врезка) | 42 | сценарий: keeper_info; город `coc:location:gamwell` |
| Тайна Корнтуэйта | 42 | сценарий: keeper_info |
| Что известно местным жителям | 42 | сценарий: keeper_info; сцена `crooked-at-the-boarding-house`; `…/location/crooked-fitzgerald-estate` (history); персонажи `crooked-henry-franklin`, `-martha-franklin`, `-arthur-curwen`, `-john-fitzgerald` |
| Хранителю на заметку (Карвен в потайной комнате) | 42 | keeper_info; `crooked-arthur-curwen`; место `crooked-house-19-secret-room` |
| О чём местные не знают: гибель экспедиции | 42–43 | keeper_info; `crooked-arthur-cornthwaite` |
| Тайна исчезнувшего племени | 43 | keeper_info; существо `…/creature/crooked-spawn-of-shub-niggurath` (legend); `coc:creature:shub-niggurath` |
| Судьба Корнтуэйта | 43 | keeper_info; `crooked-arthur-cornthwaite`; `crooked-spawn-of-shub-niggurath` |
| Вовлечение сыщиков | 43–44 | сценарий: hook, advice (навыки); сцена `crooked-unexpected-letter` |
| Действующие лица | 44 | персонажи (ниже) |
| Реджинальд, Уолтер и Херберт Доджи, 57, 59 и 60 лет, юристы | 45 | `…/character/crooked-dodge-brothers` |
| Хэнк и Эдит Хаггарти, 56 и 46 лет, владельцы пансиона | 45 | `crooked-hank-haggarty`, `crooked-edith-haggarty` |
| Стэн Артемис, 47 лет, редактор газеты | 45 | `crooked-stan-artemis` |
| Джо Вирелли, 28 лет, репортёр | 46 | `crooked-joe-virelli` |
| Уильям Уитфорд, 61 год, шериф округа | 46 | `crooked-william-whitford` |
| Сьюзен Арвелл, 32 года, библиотекарь | 46–47 | `crooked-susan-arwell` |
| Отродье Тёмной Матери, уродливая тварь | 47 | `crooked-spawn-of-shub-niggurath` (aliases, sources) |
| Завязка: неожиданное письмо (+ «Хранителю на заметку») | 47 | сцена `…/scene/crooked-unexpected-letter`; раздатки `crooked-1-dodge-letter`, `crooked-2-millionaire-missing` |
| Предварительное расследование | 47 | сцена `crooked-preliminary-research` |
| Гэмвелл | 47 | `coc:location:gamwell` (новая общая запись, Р-190) |
| Пансион Хаггарти | 47 | место `…/location/crooked-haggarty-boarding-house`; сцена `crooked-at-the-boarding-house` |
| Контора братьев Додж (+ «Хранителю на заметку» о соли) | 47, 49 | место `crooked-dodge-office`; сцена `crooked-at-the-dodge-office`; предметы `crooked-cornthwaite-ledgers`, `crooked-salt` |
| Материал «Домище 1» (в главе) | 48 | `…/handout/crooked-1-dodge-letter` |
| Материал «Домище 2» (в главе) | 49 | `…/handout/crooked-2-millionaire-missing` |
| «Гэмвелл газетт» | 49–50 | организация `…/organization/crooked-gamwell-gazette`; место `crooked-gazette-office`; сцена `crooked-at-the-gazette` |
| Кладбище | 50 | место `crooked-cemetery`; сцена `crooked-at-the-cemetery`; `crooked-arthur-grimstock`, `crooked-gloria-curwen` |
| Кабинет шерифа (+ «Хранителю на заметку» о кобыле) | 50 | место `crooked-sheriff-office`; сцена `crooked-at-the-sheriff`; `crooked-seb-watkins` |
| Материал «Домище 3» (в главе) | 50 | `…/handout/crooked-3-family-slain` |
| Мэрия | 50 | место `crooked-town-hall`; сцена `crooked-at-the-town-hall`; `crooked-nigel-tellings`; предмет `crooked-title-deed` |
| Городская библиотека | 51 | место `crooked-library`; сцена `crooked-at-the-library`; предмет `crooked-lost-people-book`; `crooked-thomas-pratt` |
| Поместье Фицджеральдов | 51 | место `crooked-fitzgerald-estate`; область `crooked-gamwell-environs`; сцена `crooked-around-the-house` |
| Соседние поместья (+ «Хранителю на заметку» о костях) | 51–52 | места `crooked-neighboring-estates`, `crooked-watkins-farm`; сцена `crooked-neighbors`; предмет `crooked-horse-bones` |
| Материал «Домище 4» (в главе) | 51 | `…/handout/crooked-4-fitzgerald-tragedy` |
| Вокруг дома | 52 | сцена `crooked-around-the-house`; места `crooked-estate-1-gate`, `-2-wall`, `-3-driveway` |
| План «Поместье Фицджеральдов» (для Хранителя) | 52 | карта `…/map/crooked-estate` (`app/maps/mansions-crooked-estate.jpg`, 9 меток: 1–6, «Деревья» ×2, «Дорога в Гэмвелл») |
| Декоративный сад (5) | 52 | место `crooked-estate-5-garden` |
| Поиски в саду | 52–53 | сценарий: таблица «Поиски в саду»; сцена `crooked-around-the-house`; предмет `crooked-tropical-plants` |
| Зловещий сарай (6) | 53 | место `crooked-estate-6-shed` |
| Дом снаружи (4) | 53 | место `crooked-fitzgerald-house` (description) |
| Дом Фицджеральдов (+ «Хранителю на заметку» о полах) | 53–54 | `crooked-fitzgerald-house`; сцена `crooked-inside-the-house` |
| Что за шум? (+ «Хранителю на заметку») | 54 | сцена `crooked-inside-the-house` |
| Посетители: Шериф Уитфорд, Джо Вирелли, Призрак (+ две заметки Хранителю) | 54–55 | сцена `crooked-visitors`; `crooked-william-whitford`, `crooked-joe-virelli`, `crooked-john-fitzgerald` |
| Поездка в Южную Америку (врезка) | 55 | сценарий: advice; сцена `crooked-at-the-dodge-office` |
| Дом | 55–56 | сцены `crooked-ground-floor`, `crooked-second-floor`; `crooked-fitzgerald-house` |
| Первый этаж: Библиотека (1) (+ две заметки Хранителю) | 56, 58 | место `crooked-house-1-library`; предмет `crooked-curwen-note` |
| Отродье (врезка): Следы и наблюдения, Тактика отродья, заметка Хранителю | 57 | сцена `crooked-spawn-stalks`; `crooked-spawn-of-shub-niggurath` (legend) |
| Кабинет (2) | 58 | `crooked-house-2-study`; `crooked-lost-people-book` |
| Чулан (3) | 58 | `crooked-house-3-closet` |
| Материал «Домище 5» (в главе) | 58 | `…/handout/crooked-5-lost-people` |
| Холл (4), Гардеробная (5), Пустая комната (6), Кухня (7), Столовая (8), Кладовая (9), Прачечная (10) | 58 | места `crooked-house-4-hall` … `crooked-house-10-laundry`; предмет `crooked-missing-salt` |
| План «Дом Фицджеральдов» (для Хранителя, легенда 1–23) | 59 | карта `…/map/crooked-house` (`app/maps/mansions-crooked-house.jpg`, 29 меток: 1–23, 4 подписи этажей, 2 люка); место `crooked-house-20-landing` (только на плане) |
| Гостиная (11) | 60 | `crooked-house-11-parlor` |
| Второй этаж: Балкон | 60 | `crooked-house-balcony`; сцена `crooked-second-floor` |
| Рабочий кабинет (12) | 60 | `crooked-house-12-office`; `crooked-double-barrel-shotgun` |
| Хозяйская спальня (13) | 60 | `crooked-house-13-master-bedroom`; `crooked-shotgun-shells`, `crooked-valuables`, `crooked-missing-salt` |
| Материал «Домище 6» (в главе) | 60 | `…/handout/crooked-6-cornthwaite-note` |
| Зал трофеев (14) (+ заметка Хранителю) | 60 | `crooked-house-14-trophy-room`; `crooked-trophies` |
| Комната отдыха (15) | 60 | `crooked-house-15-lounge` |
| Спальня (16) | 60–61 | `crooked-house-16-bedroom`; существо `crooked-raccoon` |
| Гостевая спальня (17) | 61 | `crooked-house-17-guest-bedroom` |
| Ванная (18) (+ заметка Хранителю) | 61 | `crooked-house-18-bathroom`; `crooked-nacl-mirror` |
| Тайная комната (19) | 61 | `crooked-house-19-secret-room`; `crooked-curwen-axe`; `crooked-arthur-curwen` |
| Соль? (врезка) | 61 | предмет `crooked-salt` |
| Чердак (+ заметка Хранителю) | 61–62 | место `crooked-house-attic`; сцена `crooked-attic`; `crooked-expedition-trunk` |
| Подвалы: Дровяной погреб (21), Центральный подвал (22), Угольный погреб (23) | 62 | места `crooked-house-21-woodshed`, `-22-central-cellar`, `-23-coal-cellar`; сцена `crooked-cellars` |
| Завершение | 62–64 | сцена `crooked-finale`; таблица «Урон от соли» (ссылка) |
| Награды | 64 | сценарий: conclusion (четыре награды/штрафа Рассудка) |
| Как продлить этот ужас | 64 | сценарий: conclusion |
| Персонажи и чудовища / Персонажи Хранителя (семь статблоков) | 64–65 | статблоки `crooked-dodge-brothers`, `-hank-haggarty`, `-edith-haggarty`, `-stan-artemis`, `-joe-virelli`, `-william-whitford`, `-susan-arwell` |
| Существа и чудовища: Отродье Шуб-Ниггурат; Образ жизни и повадки | 65–66 | `crooked-spawn-of-shub-niggurath` (description, legend, abilities) |
| Ложноножка, мерзкое щупальце чудовища | 66–67 | вариант «Ложноножка» в `crooked-spawn-of-shub-niggurath` |
| Основная туша, зыбкая неземная субстанция | 67 | основной статблок и вариант «Основная туша» |
| Урон от соли (врезка) | 67 | сценарий: таблица «Урон от соли»; `crooked-salt` (mechanics); способность «Соль» у существа |
| Материалы для игроков: «Домище 1» | 191 | `crooked-1-dodge-letter` (источник текста) |
| «Домище 2», «Домище 3», «Домище 4», «Домище 5» | 192 | `crooked-2-millionaire-missing`, `-3-family-slain`, `-4-fitzgerald-tragedy`, `-5-lost-people` |
| «Домище 6» | 193 | `crooked-6-cornthwaite-note` |
| Поместье Фицджеральдов — материал для игроков | 194 | раздатка `crooked-player-map-estate` (легенда; картинка — карта `crooked-estate`) |
| Дом Фицджеральдов — материал для игроков | 195 | раздатка `crooked-player-map-house` (легенда; картинка — карта `crooked-house`) |
| Готовые сыщики сборника | — (отдельный PDF) | существующие `za-zakrytymi-dveryami-ru/character/*` (6) в ссылках сценария |

`…/` = `osobnyaki-bezumiya-ru/`. Город — новая общая запись `kb/locations/gamwell.json` (Р-190); места в городе — `part_of`
Гэмвелл, поместье и ферма — в области «Окрестности Гэмвелла» (Р-209).

## Записи (109)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `crooked-manse` |
| scene | 19 | `crooked-unexpected-letter`, `-preliminary-research`, `-at-the-boarding-house`, `-at-the-dodge-office`, `-at-the-gazette`, `-at-the-cemetery`, `-at-the-sheriff`, `-at-the-town-hall`, `-at-the-library`, `-neighbors`, `-around-the-house`, `-inside-the-house`, `-visitors`, `-ground-floor`, `-second-floor`, `-attic`, `-cellars`, `-spawn-stalks`, `-finale` |
| location | 43 | общий город `coc:location:gamwell`; книги: `crooked-gamwell-environs`, 7 мест города, `-neighboring-estates`, `-watkins-farm`, `-fitzgerald-estate`, `-estate-1-gate` … `-estate-6-shed` (5), `-fitzgerald-house` (4), 23 комнаты `-house-1-library` … `-house-23-coal-cellar`, `-house-balcony`, `-house-attic` |
| map | 2 | `crooked-estate`, `crooked-house` |
| character | 18 | 7 со статблоками (Доджи — один групповой статблок на троих, как в книге), 11 без статблоков: `crooked-arthur-cornthwaite`, `-arthur-curwen`, `-gloria-curwen`, `-john-fitzgerald`, `-william-fitzgerald`, `-henry-franklin`, `-martha-franklin`, `-seb-watkins`, `-arthur-grimstock`, `-nigel-tellings`, `-thomas-pratt` |
| creature | 2 | `crooked-spawn-of-shub-niggurath` (уникальное, `spawn_of` Шуб-Ниггурат; основная туша + ложноножка), `crooked-raccoon` (животное без статблока) |
| item | 15 | `crooked-cornthwaite-ledgers`, `-salt`, `-missing-salt`, `-nacl-mirror`, `-title-deed`, `-horse-bones`, `-curwen-note`, `-lost-people-book`, `-double-barrel-shotgun`, `-shotgun-shells`, `-valuables`, `-trophies`, `-expedition-trunk`, `-curwen-axe`, `-tropical-plants` |
| handout | 8 | `crooked-1-dodge-letter` … `crooked-6-cornthwaite-note`, `crooked-player-map-estate`, `crooked-player-map-house` |
| organization | 1 | `crooked-gamwell-gazette` |

Новых заклинаний и книг Мифов в сценарии нет. Картинки карт: `app/maps/mansions-crooked-estate.jpg` (1263×850),
`app/maps/mansions-crooked-house.jpg` (1332×1905); метки проверены глазами по вырезкам с нарисованными кружками (Р-206).

## Опечатки и расхождения

- С. 51, «Городская библиотека»: «Миссис **Карвен** много знает о Гэмвелле…» — по смыслу Арвелл. `errata` (исправлено в записи)
  у `crooked-susan-arwell` и сцены `crooked-at-the-library`.
- С. 58, «Кухня (7)»: «перекрыты трубы (Спальня, стр. 60)» — о трубах сказано в «Ванной (18)», с. 61. `errata` у `crooked-house-7-kitchen`.
- С. 49: газета «Основана в 1847 году!»; в английском 6e — «Established 1887». Оставлено как в русском издании, пометка в `errata`
  организации `crooked-gamwell-gazette` (не исправлено: 6e не источник чисел).
- С. 43: «С тех пор прошло немало лет», хотя Корнтуэйт исчез в январе 1925 года (письмо Доджа — 30 января), — смысловая
  нестыковка перевода (в 6e — «All has been still for some time now»); в записях не цитируется, не правилось.
- Все производные статблоков сходятся с правилами (ПЗ, ПМ, БкУ, Комплекция, Скорость с возрастной поправкой); `tools/check.py`
  возраст Доджей берёт по младшему (57).
- Подзаголовок с. 47 «…уродливая тварь» напечатан бледно (первые буквы не читаются уверенно).
- Англ. 6e: смотритель кладбища и служащий мэрии без имён; в русском издании — Артур Гримсток и Найджел Теллингс (взято по-русски).

## Не взято

- Иллюстрации: с. 40 (разворот «Отродье Шуб-Ниггурат»), с. 44 «Братья Додж», «Хэнк и Эдит Хаггарти», с. 45 Стэн Артемис,
  «Джо Вирелли», с. 46 «Уильям Уитфорд», «Сьюзен Арвелл», с. 54 «Джо Вирелли входит в дом», с. 56 «Отродье Шуб-Ниггурат»,
  с. 63 (тварь разваливает дом) — картинки в записи не добавлялись (поле `images` необязательно; можно позже `pipeline/art/add_images.py`).
- С. 68 — полностраничная иллюстрация перед гл. 3 «Секретный код»: не этой части.
- Эйнсфилды (владельцы 1866–1894, без имён), Альберт, Эльма, Саймон и Грейс Фицджеральд, дети Карвенов (Харольд, Сара, Сьюзен),
  садовник и слуги Корнтуэйта, участники экспедиции, туземцы-потомки племени, культ Шуб-Ниггурат (упомянут как возможное
  продолжение) — текстом в записях персонажей, сценария и существа; отдельных записей нет (без статблоков и своей роли).
- Храм исчезнувшего племени в Южной Америке — текстом (keeper_info, легенда существа); записи места нет: сыщики туда не попадают
  в рамках сценария.
- Ключи от дома, ржавый топор Джо Вирелли (книга: «не имеет значения»), мачете и револьвер .45 из чемодана, серебряный сервиз,
  патроны — текстом в сценах и предметах (без отдельных записей).
- Значки легенды плана дома (потайная дверь, камины, лестницы) меток не получили (это обозначения, не места).
- Сноски с. 41 (детская песенка «There was a crooked man» / «Скрюченная песня» Чуковского; «When Johnny comes marching home») —
  справочные примечания переводчика, не игровые; упомянуты здесь.
- Алфавитный указатель (с. 220–224) — служебный (использован для проверки страниц раздаток).

## Предложения

`proposals-crooked.json` — 3 предложения: `coc:creature:shub-niggurath` — псевдоним «Тёмная Мать» (с. 43, 47);
`coc:location:boston` — ссылки на Гэмвелл и на сценарий (без `corrections`). Пробный прогон `pipeline/integrate/apply.py --dry-run`:
3 правки ложатся.
