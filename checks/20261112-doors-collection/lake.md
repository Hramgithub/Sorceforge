# «Служители озера» («Двери во тьму», `dveri-vo-tmu-ru`) — сверка переноса (часть lake)

Источник — официальное русское издание «Двери во тьму» (скан без текстового слоя): страницы распознаны
`pdftoppm -r 200` + `tesseract -l rus`, каждое число и каждый плохо распознанный кусок сверены по изображению страницы
(вырезки), рукописная раздатка «Служители 2» прочитана по изображению. Английский оригинал `doors-to-darkness-en` — для
сверки чисел и `name.en`. Раздатка из папки владельца `Раздатка\[RU 7e] Служители озера раздатка.docx` (пять картинок:
фото Джеймса, «Служители 1», «Служители 2», страница учётной книги, врезка о томе VI) — другой перевод тех же материалов;
источником текста не взята, различия — в `quality.notes` раздаток.

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 4 «Служители озера» (заставка — с. 56) | 57–75 | 56–74 (заставка — 55) |
| «Материалы для игроков»: «Служители 3», «Служители 1», «Служители 2» | 118, 119, 120 | 117, 118, 119 |

Смещение `dveri-vo-tmu-ru`: печатная = физическая + 1 на всех страницах главы и раздаток. Номера печатных страниц
совпадают с оригиналом (`doors-to-darkness-en`: печатная = физическая − 1).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 4. Служители озера (Глинн Оуэн Баррасс) | 57 | сценарий `dveri-vo-tmu-ru/scenario/servants-of-the-lake` (summary) |
| Введение | 57 | сценарий: summary, advice (современность); `…/location/lake-squatters-lake` |
| Информация для Хранителя | 57 | сценарий: keeper_info; `…/character/lake-robert-brophy`, `-william-brophy`, `-elizabeth-brophy`, `-gemma-brophy`; `…/organization/lake-brophy-family`; `…/item/lake-glaaki-jars` |
| Гла’аки и его аватары | 57–58 | сценарий: keeper_info; `…/creature/lake-avatar-of-glaaki` (legend) |
| Вовлечение сыщиков (с врезкой — сведения Джеральда и фото) | 58 | сцена `…/scene/lake-involving`; сценарий: hook; `…/character/lake-gerald-frazer`, `lake-james-frazer`; предмет `…/item/lake-james-photo` |
| Сбор сведений | 58 | сцена `…/scene/lake-research`; `…/character/lake-travis-bryce`, `lake-emily-livingstone` |
| Прибытие в мотель | 58, 60 | сцена `…/scene/lake-arriving`; места `lake-squatters-lake`, `lake-road`, `lake-motel` |
| Материал «Служители 1» (в главе) | 59 | раздатка `…/handout/lake-1-local-history` |
| Карта 1 | 60 | карта `…/map/lake-map-1-squatters-lake` (`app/maps/dveri-lake-map-1-squatters-lake.jpg`, 8 меток: 5 подписей + 3 значка) |
| Приёмная | 60 | место `…/location/lake-reception`; сцена `lake-arriving` |
| Хранителю на заметку (номера машин) | 60 | `lake-reception`; предмет `…/item/lake-license-plates`; сцена `lake-arriving` |
| «Братья» Брофи (с ответами на вопросы) | 61 | сцена `…/scene/lake-brophy-brothers`; предмет `…/item/lake-guest-book`; `lake-crawlspace` |
| Номера | 61–62 | сцена `…/scene/lake-rooms`; места `…/location/lake-room-1` … `lake-room-8` |
| Хранителю на заметку (люки) | 62 | сцена `lake-rooms`; место `…/location/lake-crawlspace`; номера |
| Неприятный инцидент | 62 | сцена `…/scene/lake-ugly-incident`; `…/character/lake-jacob-trent` |
| Карта 2. Мотель «Сквоттерс-Лейк» | 62 | карта `…/map/lake-map-2-motel` (`app/maps/dveri-lake-map-2-motel.jpg`, 34 метки на все подписи) |
| Материал «Служители 2» (в главе) | 63 | раздатка `…/handout/lake-2-james-notebook` |
| Обыск мотеля | 64 | сцена `…/scene/lake-searching-motel` |
| Номера сыщиков | 64 | сцена `lake-searching-motel`; предмет `…/item/lake-fingernail`; `lake-room-4` |
| Другие постояльцы | 64 | сцена `…/scene/lake-other-tenants` |
| Джейкоб Трент (с «Хранителю на заметку») | 64 | `…/character/lake-jacob-trent` (legend, background.secret); `…/character/lake-tori-hickey` |
| Билл Данстон | 64 | `…/character/lake-bill-dunston`; `lake-room-6` |
| Сара Боннер | 64–65 | `…/character/lake-sarah-bonner`; `lake-room-7` |
| Материал «Служители 3» (в главе) | 65 | раздатка `…/handout/lake-3-guest-list` |
| Приёмная (обыск) | 65 | `lake-reception`; `lake-license-plates`; сцена `lake-searching-motel` |
| Гостиная братьев Брофи | 65 | место `…/location/lake-living-room`; `lake-3-guest-list`; `…/item/lake-shotgun` (патроны) |
| Спальня Уильяма | 65 | место `…/location/lake-william-bedroom`; предмет `…/item/lake-lockbox` |
| Спальня Роберта | 65 | место `…/location/lake-robert-bedroom`; книга `…/tome/lake-revelations-of-glaaki-volume-6` |
| Откровения Гла’аки. Том VI (врезка) | 66 | книга `…/tome/lake-revelations-of-glaaki-volume-6` (`edition_of` `coc:tome:revelations-of-glaaki`, `copies`) |
| Мастерская (с «Хранителю на заметку») | 66 | место `…/location/lake-workshop`; сцена `…/scene/lake-workshop-search`; предметы `lake-victims-belongings`, `lake-glaaki-jars`; `lake-mr-smith`, `lake-mrs-smith` |
| Осмотр округи | 66–67 | сцена `…/scene/lake-exploring`; места `lake-pier`, `lake-tire-tracks`, `lake-clearing`, `lake-old-settlement` (с колодцем), `lake-woods` |
| Хранителю на заметку: связь с властями | 67 | сценарий: advice (полностью); `lake-william-brophy` (legend) |
| Развитие событий | 67 | сцена `…/scene/lake-sequence-of-events` |
| Хранителю на заметку: позвольте сыщикам поработать самим | 69 | сцена `lake-sequence-of-events`; сценарий: advice |
| Сонный зов | 69 | сцена `…/scene/lake-dream-pull`; аватар: способность «Сонный зов» |
| Финальная схватка | 69 | сцена `…/scene/lake-final-confrontation` |
| Сон о затонувшем городе (врезка) | 69 | сцена `lake-dream-pull` |
| Хранителю на заметку (похищение Сары) | 69 | сцена `lake-final-confrontation`; `lake-sarah-bonner`, `lake-james-frazer` |
| Сопротивление | 69–70 | сцена `lake-final-confrontation` |
| У озера в лунном свете | 70 | сцена `…/scene/lake-by-the-lake`; место `lake-clearing` |
| Хранителю на заметку: чудовищная нежить | 70 | существо `…/creature/lake-zombies` (legend); сцена `lake-by-the-lake`; сценарий: advice |
| Итоги | 70, 72 | сценарий: conclusion; шаг «Итоги и награды»; `lake-gerald-frazer` |
| Награды | 72 | сценарий: conclusion (четыре награды Рассудка) |
| Приложение А. Персонажи Хранителя и чудовища | 73 | — |
| Постояльцы мотеля: Джейкоб Трент, нервный юноша | 73 | `…/character/lake-jacob-trent` (статблок) |
| Билл Данстон, замкнутый постоялец | 73 | `…/character/lake-bill-dunston` (статблок) |
| Сара Боннер, дама в беде | 73 | `…/character/lake-sarah-bonner` (статблок) |
| Чудовища мотеля: Мистер и миссис Смит, служители Гла’аки | 73 | `…/character/lake-mr-smith`, `lake-mrs-smith` (статблоки; `instance_of` `coc:creature:servant-of-glaaki`) |
| Джеймс Фрейзер, служитель Гла’аки | 74 | `…/character/lake-james-frazer` (статблок) |
| Роберт Брофи, служитель Гла’аки | 74 | `…/character/lake-robert-brophy` (статблок) |
| Уильям Брофи, служитель Гла’аки | 74 | `…/character/lake-william-brophy` (статблок) |
| Зомби, четверо неудавшихся служителей | 74 | `…/creature/lake-zombies` (`instance_of` `coc:creature:zombie`) |
| Аватар Гла’аки; Особые умения: Сонный зов | 75 | `…/creature/lake-avatar-of-glaaki` (`avatar_of` `coc:creature:glaaki`; способности «Сонный зов», «Шип и заражение») |
| Материалы для игроков: материал «Служители 3» | 118 | `…/handout/lake-3-guest-list` (источник текста) |
| Материал «Служители 1» | 119 | `…/handout/lake-1-local-history` (источник текста) |
| Материал «Служители 2» | 120 | `…/handout/lake-2-james-notebook` (источник текста) |
| Готовые персонажи (десять сыщиков) | 126–135 | существующие записи `dveri-vo-tmu-ru/character/<slug>` — в ссылках сценария (источник книги и `name.en` уже предложены частью darkness) |

`…/` = `dveri-vo-tmu-ru/`. Город для гайда — общий Аркхэм: озеро Сквоттерс — область `part_of`
`keepers-companion-en/location/arkham-environs` («Окрестности Аркхэма», Р-209; книга ставит озеро к северу от Кингспорта
и к юго-западу от Аркхэма); места сценария — записи книги в этой области, мотель и его комнаты — `part_of` мотеля.
Карты привязаны к `coc:location:arkham`.

## Записи (68)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `servants-of-the-lake` (order 3) |
| scene | 14 | `lake-involving`, `-research`, `-arriving`, `-brophy-brothers`, `-rooms`, `-ugly-incident`, `-searching-motel`, `-other-tenants`, `-workshop-search`, `-exploring`, `-sequence-of-events`, `-dream-pull`, `-final-confrontation`, `-by-the-lake` |
| location | 22 | `lake-squatters-lake` (область), `-road`, `-motel`, `-reception`, `-living-room`, `-william-bedroom`, `-robert-bedroom`, `-workshop`, `-crawlspace`, `-room-1` … `-room-8` (number 1–8), `-pier`, `-tire-tracks`, `-clearing`, `-old-settlement`, `-woods` |
| map | 2 | `lake-map-1-squatters-lake`, `lake-map-2-motel` |
| character | 14 | статблоки: `lake-jacob-trent`, `-bill-dunston`, `-sarah-bonner`, `-mr-smith`, `-mrs-smith`, `-james-frazer`, `-robert-brophy`, `-william-brophy`; без статблока: `-gerald-frazer`, `-emily-livingstone`, `-travis-bryce`, `-tori-hickey`, `-elizabeth-brophy`, `-gemma-brophy` |
| creature | 2 | `lake-avatar-of-glaaki`, `lake-zombies` |
| item | 8 | `lake-james-photo`, `-guest-book`, `-license-plates`, `-shotgun`, `-lockbox`, `-glaaki-jars`, `-victims-belongings`, `-fingernail` |
| handout | 3 | `lake-1-local-history`, `lake-2-james-notebook`, `lake-3-guest-list` |
| tome | 1 | `lake-revelations-of-glaaki-volume-6` |
| organization | 1 | `lake-brophy-family` («„Семья“ Брофи») |

Служители Гла’аки из человеческой семьи и постояльцы со своей историей (Брофи, Джеймс, Смиты) — персонажи со связью
`instance_of` `coc:creature:servant-of-glaaki` (Р-94); безымянные зомби — существо с профилем сценария.

## Опечатки книги (`errata`, значения — как напечатано)

- Страница учётной книги (материал «Служители 3», с. 65 и 118): Джейкоб Трент — «№ 3», а по тексту (с. 64) он снимает номер 8;
  в оригинале в раздатке — Room 8. `errata` у раздатки и у Джейкоба.
- ПЗ 19 у Джейкоба (по правилам 12), Билла Данстона (15), Сары Боннер (12) и зомби (14); так и в оригинале.
- Уклонение Сары 35% при ЛВК 75 (не ниже 37%); так и в оригинале.
- Джеймс Фрейзер: БкУ +1d6, а урон атак — «1d3 + 1d4» и «1d6 + 1d4» (строки Смитов); так и в оригинале.
- Скорость Роберта 2 и Уильяма 5 (по правилам 7; у Роберта с возрастом — 0, у Уильяма — 2); так и в оригинале. Для дряхлой нежити, вероятно, задумано.

## Расхождения изданий и сомнения (`quality.notes`)

- Русское издание переименовало друга Джейкоба: «Тори Хикки» (оригинал — Abraham/Abe Hickey, «Abe Hickie»; в docx владельца — «Эйб Хикли»).
- Сара Боннер: оригинал — едет в Салем из Ньюберипорта (с. 64; в приложении — в Кингспорт); русское издание — в Кингспорт из Ньюпорта.
- Стороны света в мотеле русское издание сверило с Картой 2 (север — вправо): дверь в жилые комнаты — в северо-восточном углу
  (оригинал — northwest), номера соединены с северным и южным соседом (оригинал — восточным и западным), окна спален — в северной
  стене (оригинал — западной) и т. д. В записях — как в русском издании.
- Гостиная Брофи: русское издание — «несколько меньше номеров (6 на 3 метра)»; оригинал — «slightly larger» (20 × 10 футов).
- Потеря Рассудка «1/1d8, если выглядит как оживший труп» у Смитов и Джеймса — только в русском издании.
- Сонный зов: оригинал в «Развитии событий» отправляет пленников к аватару «at the lake’s southeast corner»; русское издание — юго-западный берег (как везде).
- Правило сонного зова в статблоке называет «пункты магии Гла’аки», в сцене (с. 69) — «пункты магии аватара».
- Строка потери Рассудка «если он умер от „Зелёного гниения“» стоит и у Уильяма (нежить 58 лет, гниение — после шестидесяти).
- Ногти у двери номера 4: русское издание — «вырванные человеческие ногти», оригинал — один ноготь; следы в руинах: русское — «одна [нога] босая», оригинал — «one missing shoe».
- Меры: озеро 290 на почти 100 м (950 × 325 футов), колодец 6 м (20 футов), следы шин в 15 м от пристани (50 футов), сонный зов +1 за 800 м (half-mile), рост Джеймса 189 см (6’2’’).
- Связь Тори Хикки с профилем зомби — вывод из текста (Р-41): книга говорит, что Тори не стал служителем и бродит по лесу нежитью, а четверо зомби — бывшие постояльцы, сброшенные в озеро.
- Значки без подписи на Карте 1 (пристань, три лодки, следы шин) получили метки по тексту главы; пометка `note` у каждой.

## Не взято

- Иллюстрации (с. 56 — заставка «Братья Брофи» у мотеля; с. 58 — фото Джеймса в тексте, взято описанием в предмет; с. 68 — «Затонувший город»;
  с. 71 — «У озера в лунном свете»; с. 72 — портреты «Мистер и миссис Смит», «Джейкоб Трент», «Роберт Брофи», «Уильям Брофи» и «Служитель
  Гла’аки»; с. 75 — «Гла’аки»): картинки в записи не добавлялись (поле `images` необязательно; добавить можно `pipeline/art/add_images.py`,
  папка `app/art` вне этой части). Картинки docx владельца — тоже.
- Кларкс-Корнерс, Бричестер, долина реки Северн, Бостон, Салем/Ньюпорт, бакалея за лесом, плотник, прежний владелец мотеля, полиция,
  «милая Пейдж» и владелец часов «Дж. С.» — упомянуты мимоходом: текстом в описаниях и сценах, записей нет (кандидаты не нужны для игры).
- Ключи Уильяма, которые стягивает Джейкоб, коробка патронов, рукавицы, бочки масла, стол с ремнями — текстом в сценах и местах (без
  отдельных записей предметов).
- Материал «Гений 6» на той же с. 118 — часть genius.
- Готовые сыщики (с. 126–135) с листами книги не сверялись — это сделала часть darkness предложениями.

## Предложения

`proposals-lake.json` — 10 предложений (все `correction: false`): «Окрестности Аркхэма» — фраза об озере Сквоттерс в описании,
источник и ссылки на озеро и сценарий; Аркхэм — ссылки на сценарий, Тревиса Брайса и Джейкоба Трента; Кингспорт — ссылки на
сценарий и Эмили Ливингстон; `coc:tome:revelations-of-glaaki` — ссылка на том VI. Пробный прогон
`pipeline/integrate/apply.py --dry-run`: 10 правок ложатся (4 записи).
