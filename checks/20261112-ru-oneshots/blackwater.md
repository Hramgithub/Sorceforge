# «Черноводный ручей» (chernovodnyy-ruchey-ru, часть «blackwater») — сверка покрытия

Книга: сборник «Черноводный ручей и Вышел срок» — официальный русский перевод Chaosium (метка «[RU 7e]», на обложке
логотип Chaosium); «Черноводный ручей» — это Blackwater Creek из «Набора хранителя». 99 страниц PDF, скан без текстового
слоя: все страницы распознаны tesseract (`-l rus`, 200 dpi; страницы со сгибом — повторно с выравниванием фона, 300 dpi),
все числа статблоков, наград, стадий Дара Матери и все карты сверены по изображениям страниц. Система — «Зов Ктулху»
7-й редакции, ядро (`ruleset: "core"`), эпоха — 1920-е (сентябрь 1926 года).

Страницы: печатная = физическая + 1 (смещение +1: печатная «27» стоит на физ. 26, «33» — на физ. 32, «34» — на физ. 33).
«Черноводный ручей» — физ. 1–56 (с. 2–57: обложка, оглавление, сценарий, приложение, раздатки, биографии и листы готовых
сыщиков); с физ. 57 (с. 58) — «Вышел срок» (часть «dues»).

Префикс записей: `chernovodnyy-ruchey-ru/<вид>/blackwater-…`. Общий город — `coc:location:blackwater-creek` (новый,
`kb/locations/blackwater-creek.json`): записи посёлка в базе не было, «Вышел срок» происходит в Аркхэме.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Черноводный ручей и Вышел срок» | 2 | `scenario/blackwater-chernovodnyy-ruchey` (summary, sources) |
| Содержание | 3 | `scenario` (sources); пункты — ниже |
| Эпиграф (Лавкрафт, «Картина в доме») | 4 | не взято (см. ниже) |
| Введение; Краткое содержание сценария | 4 | `scenario` (summary, keeper_info) |
| Предыстория: Кейдс-Рест | 5 | `scenario` (keeper_info); `character/blackwater-ezekil-keyd`, `blackwater-deniel-keyd`; `organization/blackwater-sikayuki` |
| Раскопки | 5–6 | `scenario` (keeper_info); `character/blackwater-genri-rouds`, `blackwater-ebigeyl-rouds`; `creature/blackwater-utroba-zemli`; `item/blackwater-voda-rucheya` |
| Хроника событий (1926 год) | 6 | `scenario` (таблица «Хроника событий (1926 год)») |
| Мотивы сыщиков; Вариант 1: сыщики из Мискатоникского университета | 7 | `scenario` (hook); `character/blackwater-ernest-maktavish` |
| Вариант 2: сыщики-бутлегеры | 7 | `scenario` (hook); `character/blackwater-deklan-makbrayd`, `blackwater-maykl-uelan`; `organization/blackwater-banda-makbrayda` |
| Начало игры | 8 | `scenario` (steps); `scene/blackwater-vstrecha-s-maktavishem`, `scene/blackwater-instruktazh-butlegerov` |
| Врезка «Нагнетайте напряжение» | 8 | `scenario` (advice, таблица «Нагнетайте напряжение») |
| Локация 1. Посёлок Блэкуотер-Крик; Приезд в Блэкуотер-Крик | 8 | `scene/blackwater-priezd`; `coc:location:blackwater-creek` |
| Встречи по дороге: Джон Меррит, Гектор Винни | 8, 10 | `scene/blackwater-priezd`; `character/blackwater-dzhon-merrit`, `blackwater-gektor-vinni`; `location/blackwater-khizhina-gektora` |
| Карта «Блэкуотер-Крик. Мгла и порча в Данвичских холмах» | 9 | `map/blackwater-karta-blekuoter-krik` (`app/maps/blackwater-karta-blekuoter-krik.jpg`, 26 меток) |
| Врезка «Влияние Матери» | 10 | `scenario` (advice); `scene/blackwater-priezd`; `creature/blackwater-utroba-zemli` (способность «Дар Матери») |
| Центральная площадь | 10–11 | `location/blackwater-tsentralnaya-ploshchad`; `scene/blackwater-tsentralnaya-ploshchad` |
| Врезка «Как управлять вниманием игроков» | 10 | `scenario` (advice) |
| Местные дети | 11 | `scene/blackwater-tsentralnaya-ploshchad`; `character/blackwater-rebenok-iz-blekuoter-krik`, `blackwater-dzhek-khirn`, `blackwater-gerti-khirn` |
| Врезка «Общение с детьми» | 11 | `scene/blackwater-tsentralnaya-ploshchad` |
| Церковь | 12 | `location/blackwater-tserkov`; `scene/blackwater-tsentralnaya-ploshchad` |
| Дом вдовы Хокинс | 12 | `location/blackwater-dom-vdovy-khokins`; `character/blackwater-vdova-khokins`; `item/blackwater-drobovik-vdovy-khokins` |
| Врезка «Повторные проверки» | 12 | `scene/blackwater-spruston` |
| Дом Спрустона | 12 | `location/blackwater-dom-sprustona`; `scene/blackwater-spruston` |
| Врезка «„Шериф“ Дик Спрустон» | 13 | `scene/blackwater-spruston`; `character/blackwater-dik-spruston`; `organization/blackwater-pastva-sprustona` |
| Лавка Бакстера; Натаниэль Бакстер | 14 | `location/blackwater-lavka-bakstera`; `scene/blackwater-lavka-bakstera`; `character/blackwater-nataniel-bakster` |
| Врезки «Как определить отношение Бакстера к сыщикам», «Бакстер» | 14 | `scene/blackwater-lavka-bakstera` |
| Локация 2. Ферма Джарви | 14–16 | `location/blackwater-ferma-dzharvi`; `scene/blackwater-ferma-dzharvi` |
| Карта «Ферма Джарви» | 15 | `map/blackwater-karta-ferma-dzharvi` (17 меток) |
| Фермерский дом (Джарви) | 16 | `location/blackwater-dom-dzharvi` |
| Материал «Ручей 2» (на странице) | 16 | `handout/blackwater-ruchey-2-neokonchennoe-pismo` |
| Скотный двор | 16 | `location/blackwater-skotnyy-dvor-dzharvi`, `location/blackwater-senoval-dzharvi`; `creature/blackwater-khryak-brut` |
| Врезка «Следите за вещами» | 17 | `scene/blackwater-ferma-dzharvi` |
| Прочие постройки (Старина Пит, бойня, сарай) | 17 | `location/blackwater-postroyki-dzharvi`, `location/blackwater-khizhina-stariny-pita`; `character/blackwater-starina-pit` |
| Малкольм и Эдит Джарви | 17–18 | `character/blackwater-malkolm-dzharvi`, `blackwater-edit-dzharvi`, `blackwater-teodor-dzharvi` |
| Ночное происшествие | 18–19 | `scene/blackwater-nochnoe-proisshestvie` |
| Локация 3. Лагерь Роудса | 19–20 | `location/blackwater-lager-roudsa`; `scene/blackwater-lager-roudsa` |
| Материалы «Ручей 3», «Ручей 4» (на страницах) | 19–20 | `handout/blackwater-ruchey-3-plemena-indeytsev`, `handout/blackwater-ruchey-4-mify-i-legendy` |
| Локация 4. Ручей | 20–21 | `location/blackwater-ruchey`, `location/blackwater-plotina`; `scene/blackwater-ruchey`; `creature/blackwater-besformennaya-massa` |
| Врезка «Нагнетайте напряжение» (у ручья) | 21 | `scene/blackwater-ruchey` |
| Локация 5. Лес | 21–22 | `location/blackwater-les`; `scene/blackwater-les`; `creature/blackwater-zarodysh-temnoy-molodi` |
| Врезка «Зацепки» | 22 | `scene/blackwater-les` |
| Локация 6. Раскопки; врезка «Локации» | 22 | `location/blackwater-raskopki`; `scene/blackwater-raskopki` |
| Локация 7. Высохшее русло ручья | 22 | `location/blackwater-vysokhshee-ruslo`; `scene/blackwater-vysokhshee-ruslo` |
| Локация 8. Ферма Кармоди; Кукурузные поля; Хозяйственные постройки | 23 | `location/blackwater-ferma-karmodi`, `blackwater-kukuruznye-polya-karmodi`, `blackwater-vinokurnya-karmodi`, `blackwater-saray-dlya-viski`, `blackwater-garazh-karmodi`, `blackwater-konyushnya-karmodi`; `scene/blackwater-ferma-karmodi`; `item/blackwater-viski-karmodi` |
| Карта «Ферма Кармоди» (двор) | 24 | `map/blackwater-karta-ferma-karmodi` (13 меток) |
| Демьен Кармоди; врезка «Бой» | 25 | `scene/blackwater-ferma-karmodi`; `character/blackwater-demen-karmodi` |
| Брендан Кармоди; врезка «Цели» | 25, 27 | `scene/blackwater-ferma-karmodi`; `character/blackwater-brendan-karmodi` |
| Карта «Ферма Кармоди» (дом и погреб) | 26 | `map/blackwater-karta-dom-karmodi` (13 меток) |
| Фермерский дом (Кармоди) | 27 | `location/blackwater-dom-karmodi`, `location/blackwater-pogreb-karmodi`; `scene/blackwater-dom-karmodi`; `character/blackwater-dzheyms-karmodi`; `character/blackwater-banda-karmodi` |
| Профессор Генри Роудс | 27–28 | `scene/blackwater-dom-karmodi`; `character/blackwater-genri-rouds` |
| Материал «Ручей 5» (на странице) | 28 | `handout/blackwater-ruchey-5-polevye-zametki` |
| Локация 9. Пещера | 28, 30 | `location/blackwater-peshchera`; `scene/blackwater-peshchera`; `item/blackwater-dinamit` |
| Карта «Утроба Земли» (вид сверху, вид сбоку) | 29 | `map/blackwater-karta-utroba-zemli` (14 меток) |
| Утроба Земли | 30–31 | `location/blackwater-peshchera-utroba`; `scene/blackwater-utroba-zemli` |
| Врезка о безумии и проверке на реальность | 30 | `scene/blackwater-peshchera` |
| Врезка «Эпилог» | 31 | `scene/blackwater-utroba-zemli` |
| Взорвать пещеру динамитом | 31 | `scene/blackwater-vzryv-peshchery` |
| Подведение итогов | 31–32 | `scenario` (conclusion) |
| Врезка о тайных проверках Дара Матери | 32 | `scenario` (advice) |
| Награды | 33 | `scenario` (conclusion) |
| Приложение. Дар Матери; Стадии заражения | 33–34 | `scenario` (advice, таблица «Стадии заражения»); `item/blackwater-voda-rucheya` |
| Персонажи Хранителя и чудовища: Деклан Макбрайд | 34 | `character/blackwater-deklan-makbrayd` |
| Дик Спрустон | 34 | `character/blackwater-dik-spruston` |
| Взрослый из Блэкуотер-Крик, порченый | 34 | `character/blackwater-vzroslyy-iz-blekuoter-krik` |
| Ребёнок из Блэкуотер-Крик, попрошайка | 34 | `character/blackwater-rebenok-iz-blekuoter-krik` |
| Хряк Брут | 34 | `creature/blackwater-khryak-brut` |
| Бесформенная масса, мелкое отродье | 34–35 | `creature/blackwater-besformennaya-massa` |
| Зародыш тёмной молоди Шуб-Ниггурат | 35 | `creature/blackwater-zarodysh-temnoy-molodi` |
| Демьен Кармоди, 34 года, бутлегер | 35 | `character/blackwater-demen-karmodi` |
| Брендан Кармоди, дитя Матери | 35 | `character/blackwater-brendan-karmodi` |
| Банда Кармоди, наёмные головорезы | 36 | `character/blackwater-banda-karmodi` |
| Генри Роудс, 36 лет, пленник | 36 | `character/blackwater-genri-rouds` |
| Утроба Земли, раздающая дары | 36–37 | `creature/blackwater-utroba-zemli` |
| Встреча с профессором Мактавишем | 37–38 | `scene/blackwater-vstrecha-s-maktavishem`; `character/blackwater-ernest-maktavish`, `blackwater-agnes-soums`, `blackwater-klarens-velliver`, `blackwater-uolt-gerig`; `location/blackwater-dom-geriga`; `organization/blackwater-ekspeditsiya-roudsa` |
| Инструктаж бутлегеров (и врезка о сборах) | 38–39 | `scene/blackwater-instruktazh-butlegerov`; `location/blackwater-sklad-makbrayda` |
| Готовые сыщики: биографии | 39 | `scenario` (advice) |
| Благодарности | 39 | не взято (см. ниже) |
| Материалы для игроков (пояснения к «Ручей 1–6») | 39 | `handout/blackwater-ruchey-1…6` (description) |
| Материалы «Ручей 1», «Ручей 2» | 40 | `handout/blackwater-ruchey-1-pismo-roudsa`, `handout/blackwater-ruchey-2-neokonchennoe-pismo` |
| Материалы «Ручей 3», «Ручей 4» | 41 | `handout/blackwater-ruchey-3-plemena-indeytsev`, `handout/blackwater-ruchey-4-mify-i-legendy` |
| Материалы «Ручей 5», «Ручей 6» | 42 | `handout/blackwater-ruchey-5-polevye-zametki`, `handout/blackwater-ruchey-6-ispoved-keyda` |
| Биографии: Ленни Валентайн, Микки Валентайн | 43 | общие записи `nabor-khranitelya-ru/character/lenny-valentine`, `mickey-valentine` (ссылки из `scenario`; источник — предложение) |
| Биографии: Лулу (Луиза) Винни, Стэнли Корриган | 44 | `nabor-khranitelya-ru/character/lulu-winnie`, `stanley-corrigan` |
| Биографии: Джимми Макбрайд, Мэнни Зиглер | 45 | `nabor-khranitelya-ru/character/jimmy-mcbride`, `manny-ziegler` |
| Листы готовых сыщиков (6 × 2 страницы) | 46–57 | те же записи `nabor-khranitelya-ru/character/*` (первые строки листов сверены: характеристики, ПЗ, Рассудок, Скорость совпадают) |

## Не взято

- Эпиграф из Лавкрафта («Картина в доме», с. 4) — художественная цитата, механики и сведений для игры нет.
- «Благодарности» (с. 39) — тестировщики, не игровой материал.
- Иллюстрации и подписи к ним («Дик Спрустон на крыльце своего дома», «Старина Пит зовёт Мать», «На кукурузном поле», «Деклан Макбрайд смывает с рук кровь» и др.) — картинки не переносились (`images` не заводились); сюжет подписей есть в сценах.
- Листы готовых сыщиков (с. 46–57) построчно не переносились: готовые сыщики уже есть общими записями «Набора хранителя» (`nabor-khranitelya-ru`), здесь — только ссылки и предложение добавить источник этой книги. Полная построчная сверка навыков листов не делалась.
- Школа и два безымянных «Дома» на площади, две безымянные «Фермы», «Ограда», «Костёр», «Зернохранилище» Джарви — только подписи карт без текста; отдельных записей нет, метки ведут на площадь, окрестности или ферму с пояснением.

## Опечатки и сомнения книги (в `errata`, значения как напечатано)

- Деклан Макбрайд: Скорость 6 (по правилам 7).
- Генри Роудс: Скорость 7 (по правилам 8; возможно, с учётом ноги).
- Брендан Кармоди: Скорость 8 (по правилам 7).
- Ребёнок из Блэкуотер-Крик: Комплекция −2 при БкУ −1 (по сумме СИЛ+ТЕЛ 65 — −1 и −1); Скорость 8 (по правилам 9).
- Утроба Земли: Комплекция 6 при БкУ +4d6 (по таблице для 450 — Комплекция 5); процент «Захвата» напечатан как «см. выше» (взят 60% атаки — вывод из текста).
- Материал «Ручей 5»: место находки — у Роудса в погребе (с. 27) против «в остатках палатки Роудса» (с. 39); в записи оба.
- Взрослый из Блэкуотер-Крик: «15/06», «12/05» — ведущие нули как напечатано в `raw`.

## Сканы и распознавание

- Сгиб страницы съедает начала строк на левых страницах (с. 11, 13, 17, 19, 21, 23, 25, 27, 33, 35, 37): тексты сверены по изображениям; несколько полуслов восстановлены по смыслу (помечено в `quality.notes` записей Демьена, Мактавиша, винокурни, сцены «Утроба Земли», раздатки «Ручей 6»).
- Раздатка «Ручей 2»: зачёркнутый в книге текст виден игрокам и дан в квадратных скобках с пометкой «зачёркнуто» (часть зачёркнутых слов разобрана по изображению приблизительно).

## Решения, которые стоит подтвердить владельцу

- Город `coc:location:blackwater-creek` создан как общий (Р-190) — посёлок назван в книге, тип «город» как у Данвича.
- Утроба Земли — `avatar` с `avatar_of` Шуб-Ниггурат («частица божества», «воплощение Шуб-Ниггурат»), уникальное существо книги.
- Мактавиш — запись книги с `same_as` на `pulp-cthulhu-en/character/ernest-mctavish`; кандидат в общую запись `coc:character:ernest-mctavish` (Р-154), если владелец решит.
