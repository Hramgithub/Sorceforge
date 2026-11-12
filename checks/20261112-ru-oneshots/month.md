# «Месяц ночи» (`mesyats-nochi-ru`) — сверка переноса (часть month)

Источник — русское издание группы «Монстры Эдны» (сборник «Монстры Эдны», текст — Эдна Тайлер; метка владельца
`[RU 7e]`), PDF 46 страниц с текстовым слоем. Без текста — только карты (с. 9, 33), иллюстрации (с. 40 и др.) и
раздатки (с. 44–45): они прочитаны по изображениям страниц (150–300 dpi). Правила — 7-я редакция (статблоки с
половиной и пятой), `ruleset` core. Действие — **1901–1905 годы** (с. 10, год выбирает Хранитель); `axes.era` —
`other` (вопрос владельцу: возможно, `gaslight`). В каталоге — «1900».

## Страницы

Смещение: **печатная = физическая** (номера на страницах 10–45 совпадают с физическими; с. 1–9 и 46 без номеров).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титры, содержание | 1–4 | сценарий `mesyats-nochi-ru/scenario/mesyats-nochi` (summary, sources); см. «Не взято» |
| Холод (вступление) | 5 | сценарий: advice («Холод») |
| Окружение | 5 | сценарий: advice |
| Метель | 5 | сценарий: advice; `…/creature/dukhi-pomoshchniki` (legend) |
| Снег и лёд | 5–6 | сценарий: advice; `…/item/snegostupy` (mechanics) |
| Температура | 6 | сценарий: advice, таблица «Температура» (1d100); `…/item/teplaya-odezhda` |
| Болезнь и гипотермия | 7 | сценарий: advice; `…/location/bolnitsa` |
| Профессии (Этнолог, Геолог, Разводчик ездовых собак, Шахтёр) | 8 | сценарий: таблица «Профессии» (ссылки на навыки и `coc:occupation:shakhter`); advice |
| Карта Сёркла | 9 | карта `…/map/karta-serkla` (`app/maps/month-karta-serkla.jpg`, 9 меток на номерах 1–9) |
| Месяц ночи; Вступление; Краткое содержание сценария; Подготовка к игре | 10–11 | сценарий: summary, keeper_info, hook, steps |
| Сыщики | 11 | сценарий: hook |
| Инуиты | 11 | сценарий: keeper_info; `…/organization/semeystvo-nanardzhuk`; `…/item/kosti-s-risunkami`; существа `…/creature/malenkie-chelovechki`, `…/creature/chelovekoubiytsa`, `…/creature/dukhi-pomoshchniki` |
| Сёркл Сити | 11–12 | новый общий город `coc:location:circle-city` (`kb/locations/circle-city.json`) |
| Знакомство с городом; Гостиница «Лунный песец» (30 октября, вечер) | 12–15 | сцена `…/scene/lunnyy-pesets`; место `…/location/gostinitsa-lunnyy-pesets` (№1); `…/character/stiv-reynolds`, `lyuis-erikson`, `orvil-pays`, `uolter-dyuran` |
| Хранителю на заметку: Пропавшая жена | 14 | сцена `lunnyy-pesets`; `…/character/orvil-pays`, `…/character/fenni` |
| Хранителю на заметку: Сны Силлы | 15 | сцена `…/scene/sny-silly` |
| 31 октября, день; Семейство Нанарджук | 15–17 | сцена `…/scene/semeystvo-nanardzhuk`; место `…/location/dom-nanardzhukov` (№2); `…/character/amakzhuak`, `tiguaak`, `kirima`; `…/organization/semeystvo-nanardzhuk` |
| Хранителю на заметку: Упрямство | 17 | сцена `semeystvo-nanardzhuk`; `…/character/amakzhuak` (legend) |
| Школа Серебряной долины | 17–18 | сцена `…/scene/shkola-serebryanoy-doliny`; место `…/location/shkola-serebryanoy-doliny` (№6); `…/character/dzhennet-sanders`; `…/item/propusk-v-biblioteku` |
| Хранителю на заметку: Влюблённость | 18 | сцена `shkola-serebryanoy-doliny`; `…/character/dzhennet-sanders` |
| Охота на оленя | 18–20 | сцена `…/scene/okhota-na-olenya`; `…/item/bola`, `…/item/snegostupy`; место `…/location/okrestnosti-serkla` |
| Тёплая одежда | 20 | `…/item/teplaya-odezhda` |
| Библиотека | 20–22 | сцена `…/scene/biblioteka`; место `…/location/biblioteka` (№7); `…/character/matyas-buzhond`; `…/item/kartochka-zadolzhavshego-chitatelya` |
| Нерадивый читатель | 22–24 | сцена `…/scene/neradivyy-chitatel`; место `…/location/dom-eddi-alstona` (№12); `…/location/tsentralnaya-ulitsa`; `…/character/eddi-alston`; `…/item/kniga-po-voron`, `…/item/povrezhdennaya-kniga-po`, `…/item/karmannye-chasy-eddi` |
| Хранителю на заметку: Ремонт книги | 24 | сцена `neradivyy-chitatel` (mechanics); `…/item/povrezhdennaya-kniga-po` |
| Полицейский участок | 24 | сцена `…/scene/politseyskiy-uchastok`; место `…/location/politseyskiy-uchastok` (№5); `…/character/otis-brou` |
| Больница | 24–25 | сцена `…/scene/bolnitsa`; место `…/location/bolnitsa` (№9); `…/character/ervin-khill`, `viktor-khill`, `vilma-khill` |
| Хранителю на заметку: Ещё пропажи? | 25 | сцена `bolnitsa`; `…/character/nensi-khill`, `…/character/fenni` |
| Оперный театр | 25 | сцена `…/scene/opernyy-teatr-zakryt`; место `…/location/opernyy-teatr` (№4) |
| 31 октября, ночь | 26 | сцена `…/scene/noch-31-oktyabrya` |
| Погружение во тьму (1 ноября, день); Маленькие человечки | 26–28 | сцена `…/scene/malenkie-chelovechki`; `…/creature/malenkie-chelovechki` |
| Хранителю на заметку: Во что верить? | 26 | сцена `malenkie-chelovechki` (mechanics) |
| 2 ноября, ночь | 28 | сцена `…/scene/noch-2-noyabrya` («Мёртвый дух», название наше) |
| Метка (3 ноября, день) | 28 | сцена `…/scene/metka`; место `…/location/dom-lizy-fletcher` (№8); `…/character/liza-fletcher` |
| 3 ноября, ночь | 28–30 | сцена `…/scene/napadenie-otrodya` |
| Хранителю на заметку: Описание Отродья | 29 | `…/creature/otrodya-ubbo-satly` (description); сцена `napadenie-otrodya` |
| Последствия (4 ноября, день) | 30 | сцена `…/scene/posledstviya`; `…/item/kamushki-izvestnyaka` |
| Шахты (собрание, возвращение шахтёров) | 30–31 | сцена `…/scene/sobranie-v-gostinitse` (название наше); `…/character/albert-kurtis`, `…/character/filippa-vebster` |
| Собачки | 31–32 | сцена `…/scene/sobachki`; место `…/location/dom-donalda-pottsa` (№3); `…/character/donald-potts`; `…/creature/upryazhka-donalda-pottsa` |
| В глубины: 1. Коридор; 2. Жилое помещение; 3. Электрощиток | 32 | сцена `…/scene/v-glubiny`; места `…/location/shakhty`, `shakhty-1-koridor`, `shakhty-2-zhiloe-pomeshchenie`, `shakhty-3-elektroshchitok` |
| План шахт (без подписи) | 33 | карта `…/map/plan-shakht` (`app/maps/month-plan-shakht.jpg`, 7 меток) |
| 4. Рабочая зона; 5, 6 и 7. Шахты | 34 | места `shakhty-4-rabochaya-zona`, `shakhty-5-shakhta-a`, `shakhty-6-shakhta-b`, `shakhty-7-shakhta-c`, `…/location/yama`; `…/item/rukovodstva-po-planam-shakht` |
| Возвращение | 35–36 | сцена `…/scene/vozvrashchenie` |
| Хранителю на заметку: Погода | 35 | сцена `vozvrashchenie` |
| Подношения духам | 36–37 | сцена `…/scene/podnosheniya-dukham`; `…/item/buben-i-kolotushka`, `…/item/trotil` |
| Хранителю на заметку: Легенда | 36 | `…/creature/chelovekoubiytsa` (legend); сцена `podnosheniya-dukham` |
| Представление | 37–38 | сцена `…/scene/predstavlenie` |
| Заключение; Ритуал | 38 | сцена `…/scene/ritual` |
| Тротил | 39 | сцена `…/scene/trotil` |
| Уббо-Сатла | 39 | сцена `…/scene/ubbo-satla`; место `…/location/peshchera-ubbo-satly` |
| Варианты концовок | 39, 41 | сценарий: conclusion |
| Иллюстрация (Уббо-Сатла) | 40 | см. «Не взято» |
| Награды | 41 | сценарий: conclusion |
| Монстры и NPC: Уббо-Сатла; Уббо-Сатла, Извечный источник (статблок) | 42 | существо `…/creature/ubbo-satla` («Уббо-Сатла («Месяц ночи»)», `instance_of` `coc:creature:ubbo-sathla`) |
| Отродья Уббо-Сатла (статблок) | 43 | существо `…/creature/otrodya-ubbo-satly` (`instance_of` `coc:creature:spawn-of-ubbo-sathla`) |
| Отис Броу (статблок) | 43 | `…/character/otis-brou` |
| Раздаточный материал: Книга Э. А. По с пропущенным текстом | 44 | раздатка `…/handout/kniga-po-s-propushchennym-tekstom` (текст по изображению) |
| Дневник шахтёра | 45 | раздатка `…/handout/dnevnik-shakhtera` (рукописный текст по изображению) |
| Задняя обложка «Сценарий в снегах» | 46 | текст повторяет «Вступление» (с. 10) — в summary сценария |

## Не взято

- Титры (с. 3: авторы, редакторы, список благодарностей подписчикам, соцсети) и содержание (с. 4) — служебные страницы.
- Иллюстрации (обложка, с. 8, 21, 40 и др.: Уббо-Сатла, Матьяс, шахтёры, инуиты, собаки) — в `images` не переносились
  (задание картинок не требует; можно добавить `pipeline/art/add_images.py`).
- Рыжий кот Тимоти, щенок хаски Иоланта, трое внуков Амакжуака, школьники (без имён), актриса в театре, пропавший
  шахтёр из дневников, чиновники Сёркла, церковь (только упомянута, на карте не отмечена) — отдельных записей нет,
  всё сказанное книгой — текстом в записях гостиницы, семьи, сцен и города.
- Северный олень (охота) — без статблока, текстом в сцене «Охота на оленя».
- Школьные учебники и бутылка алкоголя для шахтёров — текстом в сценах (предметами не заведены).
- Советы «Чтобы изобразить …» — в `background.traits` персонажей (не потеряны).

## Опечатки и сомнения (errata)

- Уббо-Сатла: «по 1410 за раунд» вместо 1d10 (с. 42).
- Отродья: БкУ +2d6 и Комплекция 3 при СИЛ 110 + ТЕЛ 115 (по таблице +3d6 / 4) — как в «Книге хранителя», оставлено.
- Отис: фамилия «Броуи» (с. 24) / «Броу» (с. 43); «Вождение» дважды (20% и 11%); нет атак и Уклонения; названия
  «Ловость рук», «Юрисприденция» — как напечатаны.
- Дом Эдди №12 — на карте только 1–9.
- «Возвращение» (с. 35): 67 км пешком за 2,5–3,5 часа противоречит с. 31 (пешком почти четыре часа).
- Таблица температуры: значение ровно 50 не описано.
- «Уход за животными» (с. 35), «Внимательность», «тяжёлый успех» — названия как в книге; в механике — Обращение с
  животными / Внимание / трудный успех (пометки в записях).

## Кандидаты в общие записи (не заведены: справочники общие)

- Профессии сценария: Этнолог, Геолог, Разводчик ездовых собак, Шахтёр (вариант сценария; есть `coc:occupation:shakhter`
  «Книги сыщика» с другим набором) — сейчас таблица «Профессии» в сценарии.
- Навыки с механикой сценария: Этнология (проверки на с. 16, 19), Управление ездовыми собаками (с. 8, 35); Выживание
  (снежная местность) — специализация `coc:skill:survival`.
- Сёркл заведён общим городом `coc:location:circle-city` (другой части с этим городом в плане нет).
