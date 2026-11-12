# «Погоня в поезде» (`pogonya-v-poezde-ru`) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] Погоня в поезде.pdf`, 22 страницы; русский фанатский сценарий Александра Ядрихинского («Уголок
Хранителя», 2021, Fan Material Policy Chaosium), английское название «Railroad Chase» — на странице копирайта.
Редакция 7-я, `ruleset` = `core`, `axes.era` = `1920s`. Скан без текстового слоя: все страницы распознаны
`tesseract -l rus` (200 dpi), каждое число и таблица сверены по изображению страницы.

**Страницы:** физ. 1 — обложка, физ. 2 — копирайт (без номеров); печатные 1–18 = физические 3–20; физ. 21 — пустая
задняя обложка; физ. 22 — раздаточный материал «Будка» (без номера). Печатная = физическая − 2, `offset` = −2.

Город и маршрут книга не называет — «город сценария» `location/zheleznaya-doroga` внутри книги (Р-190); общих
городов не заведено и не изменено.

Префикс записей книги: `pogonya-v-poezde-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Погоня в поезде. Игровой сценарий» | физ. 1 | `scenario/pogonya-v-poezde` (name) |
| Копирайт «Railroad Chase» © 2021 Yadrikhinsky Alexander | физ. 2 | `scenario/pogonya-v-poezde` (name.en, summary, sources) |
| Вступление (1–3 сыщика, 1 встреча, 1920-е годы, завязка) | 1 | `scenario/…` (summary, hook); `location/zheleznaya-doroga` |
| От автора | 1 | `scenario/…` (advice) |
| Звуковое сопровождение (аудиолист VK, QR-код), авторы, благодарности | 1 | `scenario/…` (advice, summary) |
| Описание поезда: Возможный состав поезда | 2 | `location/poezd` (таблица «Возможный состав поезда»; в сценарии — ссылкой) |
| Краткие факты | 2 | `location/poezd`; `item/shvabra`; `location/vokzal` (телеграф на станциях) |
| Локомотив | 2 | `location/parovoz`, `location/budka-mashinista`; `item/shchup-dlya-masla`, `item/lopata`, `item/gazovye-lampy` |
| Тендер или тендерный вагон | 2 | `location/tender` |
| Багажные вагоны | 2 | `location/bagazhnyy-vagon` |
| Спальные вагоны (типы А и Б) | 2 | `location/spalnyy-vagon` |
| Вагон-ресторан | 3 | `location/vagon-restoran` |
| Сидячий вагон (типы А и Б) | 3 | `location/sidyachiy-vagon` |
| Первый класс | 3 | `location/vagon-pervogo-klassa` |
| Кабуз (тормозной вагон), Хранителю на заметку | 3 | `location/kabuz`; `scene/ekstrennaya-ostanovka` |
| Соединение вагонов | 3 | `location/poezd` (description) |
| Схемы «Спальные вагоны», «Сидячие вагоны» | 4 | `map/spalnye-i-sidyachie-vagony` (24 метки) → `app/maps/train-spalnye-i-sidyachie-vagony.jpg` |
| Схемы «Вагон 1 класса», «Вагон-ресторан», «Багажный вагон», «Кабуз (тормозной вагон)» | 5 | `map/vagon-1-klassa-restoran-bagazhnyy-kabuz` (26 меток) → `app/maps/train-vagon-1-klassa-restoran-bagazhnyy-kabuz.jpg` |
| Схема «Локомотив» | 6 | `map/lokomotiv` (7 меток) → `app/maps/train-lokomotiv.jpg` |
| Персонал поезда (где спит экипаж) | 6 | `location/poezd` (description, residents) |
| Начальник поезда | 6 | `character/nachalnik-poezda` |
| Носильщики | 6 | `character/nosilshchiki` |
| Проводники | 6 | `character/provodniki` |
| Доставщики | 6 | `character/dostavshchiki` |
| Уборщики и горничные | 7 | `character/uborshchiki-i-gornichnye` |
| Метродотель | 7 | `character/metrdotel` |
| Официанты | 7 | `character/ofitsianty` |
| Повара и посудомойки (напечатано дважды) | 7 | `character/povara-i-posudomoyki` |
| Машинист | 7 | `character/mashinist` |
| Кочегар | 7 | `character/kochegar` |
| Прочие (тормозной охранник, ремонтная бригада) | 7 | `character/tormoznoy-okhrannik` |
| Вокзал | 7 | `location/vokzal`; `scene/vokzal` |
| Расписание | 7 | `location/vokzal`; `scene/vokzal` |
| Кассы и справочная будка (проездные) | 7 | `location/vokzal`; `item/bilety` |
| Врезка «Цены на билеты» | 7 | `location/vokzal` (таблица «Цены на билеты», мили → км) |
| Случайные события (2d4) | 8 | `location/vokzal` (таблица «Случайные события»); `scene/vokzal` |
| Посадка: Погрузка багажа | 8 | `scene/posadka`; `character/nosilshchiki`; `item/bilety` |
| Посадка | 8 | `scene/posadka` |
| Проверка документов | 8 | `scene/posadka`; `item/bilety` |
| Хранителю на заметку (нет билетов) | 8 | `scene/posadka`; `item/bilety` |
| Ручная кладь | 8 | `scene/posadka`; `location/sidyachiy-vagon`, `location/spalnyy-vagon` |
| Пассажиры: Сидячие вагоны (список 1d10) | 8 | `location/sidyachiy-vagon` (таблица «Попутчики в сидячем вагоне») |
| Спальные вагоны (список 1d6) | 9 | `location/spalnyy-vagon` (таблица «Попутчики в спальном вагоне») |
| Вагоны первого класса (список 1d10) | 9 | `location/vagon-pervogo-klassa` (таблица «Пассажиры первого класса») |
| Поездка | 9 | `scene/poezdka` |
| Пассажиры сидячего вагона: Общительная бабуля-экономка | 9 | `character/obshchitelnaya-babulya-ekonomka` |
| Застенчивая девушка-гувернантка | 10 | `character/zastenchivaya-guvernantka` |
| Угрюмый строитель или грузчик | 10 | `character/ugryumyy-stroitel` |
| Пугливый лаборант | 10 | `character/puglivyy-laborant` |
| Сонный клерк | 10 | `character/sonnyy-klerk` |
| Мать с двумя беспокойными детьми | 10 | `character/mat-s-dvumya-docheryami` |
| Шумные студенты | 10 | `character/shumnye-studenty` |
| Почтенный профессор с газетой | 10 | `character/pochtennyy-professor` |
| Нервный мафиози | 10 | `character/nervnyy-mafiozi` |
| Потный жующий фермер | 10–11 | `character/potnyy-fermer` |
| Пассажиры спального вагона: Энергичный коммивояжёр | 11 | `character/kommivoyazher` |
| Сосредоточенный биржевой клерк | 11 | `character/birzhevoy-klerk`; `item/insayderskaya-informatsiya` |
| Молодая семейная пара | 11 | `character/molodaya-semeynaya-para` |
| Манерная пожилая женщина; Хранителю на заметку (огонь, дым) | 11 | `character/manernaya-pozhilaya-zhenshchina`; `scene/poezdka` |
| Женщина с маленьким ребёнком | 11 | `character/zhenshchina-s-rebenkom` |
| Секретарь пассажира первого класса | 12 | `character/sekretar` |
| Пассажиры вагона первого класса: Богатый бизнесмен (примеры промышленников) | 12 | `character/bogatyy-biznesmen` |
| Жена богатого бизнесмена/военного | 12 | `character/zhena-biznesmena` |
| Дочери богатого бизнесмена | 12 | `character/docheri-biznesmena` |
| Известный врач | 12 | `character/izvestnyy-vrach` |
| Успешный дизайнер | 12 | `character/uspeshnyy-dizayner` |
| Русская графиня | 12 | `character/russkaya-grafinya` |
| Известный актёр/актриса | 13 | `character/izvestnyy-akter` |
| Руководитель отдела в крупной фирме | 13 | `character/rukovoditel-otdela` |
| Обеспеченный иностранный учёный | 13 | `character/inostrannyy-uchenyy` |
| Преступный воротила | 13 | `character/prestupnyy-vorotila` |
| Преследователи: Тип преследователей | 13 | `scenario/…` (таблица «Тип преследователей», keeper_info); `scene/nachalo-pogoni` |
| Полиция или Бюро расследований | 13 | таблица «Тип преследователей» (→ `coc:organization:bureau-of-investigation`) |
| Преступники | 13 | таблица «Тип преследователей» |
| Культисты | 13 | таблица «Тип преследователей»; `character/kultist` |
| Монстры | 13 | таблица «Тип преследователей»; `creature/okhotyashchiysya-uzhas` (abilities) |
| Заклятье для преследователя: «Помутнение» | 14 | `character/kultist` (abilities, текст полностью); черновик общей записи — в отчёте |
| Примеры преследователей: Крупный преследователь | 14 | `character/krupnyy-presledovatel` |
| Ловкий преследователь | 14 | `character/lovkiy-presledovatel` |
| Вооружённый преследователь | 14 | `character/vooruzhennyy-presledovatel` |
| Культист | 14 | `character/kultist` |
| Охотящийся ужас | 14 | `creature/okhotyashchiysya-uzhas` (instance_of `coc:creature:hunting-horror`) |
| Погоня: Начало | 15 | `scene/nachalo-pogoni`; таблица сценария «Как сыщики узнают о преследователях» |
| Преследование (препятствия, двери, столпотворение) | 15 | `scene/presledovanie`; таблица сценария «Препятствия в проходе» |
| Отстыковка вагона | 15 | `scene/otstykovka-vagona`; `item/lom` |
| Экстренная остановка поезда | 15 | `scene/ekstrennaya-ostanovka`; `item/avariynyy-shnur` |
| Иллюстрация «Охотящийся Ужас» | 15 | `creature/okhotyashchiysya-uzhas` (sources) |
| Погоня по крыше | 16 | `scene/pogonya-po-kryshe` |
| Прыжок из поезда | 16 | `scene/pryzhok-iz-poezda` |
| Убитые монстром или в крушении (в оглавлении — «Человеческие жертвы») | 16 | `scene/zhertvy`; `scenario/…` (conclusion) |
| Управление поездом (рычаги и приборы) | 17 | `scene/upravlenie-poezdom`; `location/budka-mashinista` |
| Схема приборов будки | 17 | `map/budka-mashinista-skhema` (10 меток) → `app/maps/train-budka-mashinista-skhema.jpg` |
| Оглавление | 18 | сверка заголовков (эта таблица) |
| Материал «Будка» | физ. 22 | `handout/budka` |

## Записи (79)

- сценарий 1: `scenario/pogonya-v-poezde`;
- сцены 11: `vokzal`, `posadka`, `poezdka`, `nachalo-pogoni`, `presledovanie`, `otstykovka-vagona`, `ekstrennaya-ostanovka`,
  `pogonya-po-kryshe`, `pryzhok-iz-poezda`, `zhertvy`, `upravlenie-poezdom`;
- места 12: `zheleznaya-doroga` (город сценария), `vokzal`, `poezd`, `parovoz`, `budka-mashinista`, `tender`,
  `bagazhnyy-vagon`, `spalnyy-vagon`, `vagon-restoran`, `sidyachiy-vagon`, `vagon-pervogo-klassa`, `kabuz`;
- карты 4 (67 меток), картинки `app/maps/train-*.jpg`;
- персонажи 41: персонал 11, попутчики 26, преследователи 4 — все типажи с `names` (Р-151, имена придуманы, `editorial_text`);
- существо 1: `creature/okhotyashchiysya-uzhas`;
- предметы 8: `shchup-dlya-masla`, `lopata`, `shvabra`, `gazovye-lampy`, `avariynyy-shnur`, `lom`, `insayderskaya-informatsiya`, `bilety`;
- раздатка 1: `handout/budka`.

## Опечатки и сомнения

- Охотящийся ужас: Уклонение «60% (16/6)» — доли исправлены на 30/12 (Р-35), 16/6 подходят к 33% (Р-77, `errata`);
  БкУ «1D6» при СИЛ+ТЕЛ 220 и Комплекции 3 — исправлен на +2d6 по большинству (Р-36). Потеря Рассудка 1d3/3d6, броня 2,
  Скорость 3/17 — свои числа сценария (у общей записи 0/1d10 и др.), отдельный профиль (Р-75).
- Культист: «ПМ 24» при МОЩ 75 (ожидается 15) — `errata`, как напечатано. Обозначения «ВОЛ» (= МОЩ), «Сборка» (= Комплекция),
  «Древние Мифы» (= Мифы Ктулху) — в пометках.
- «Повара и посудомойки» напечатаны дважды подряд (с. 7) — ошибка вёрстки, в записи один раз.
- Таблица «Случайные события (2d4)»: строка 1 — прочерк (при 2d4 не выпадает); оставлена как напечатана.
- «Преследование»: книга просит расставить препятствия «используя представленную нумерацию», но список без номеров.
- «Убитые монстром или в крушении»: проверка Рассудка «5/2d10+3» (потеря 5 даже при успехе) — как напечатано.
- «Почтенный профессор»: «обращает внимания на окружающих» — восстановлено как «не обращает» (вывод из текста).
- Проценты атак дубинкой, трубой и стилетом в книге не даны отдельно — взяты по строке «Ближний бой»/«Драка» (Р-41);
  пистолет вооружённого преследователя связан с «Пистолетом автоматическим .32» по урону 1d8 (наш вывод).
- Меры: мили таблицы цен → км (80/160/800), ярды у охотящегося ужаса → метры 1 к 1 (Р-64).

## Не взято

- Иллюстрации (кондуктор на с. 1, фото спального вагона с. 2, фото посадки с. 7, билеты «Бостон — Аркхэм» компании
  Пульмана с. 8, бабуля с. 9, Охотящийся ужас над поездом с. 15, фото крушения с. 16) — оформление без текста и механики;
  папка `app/art/` вне этой части. Маршрут «Бостон — Аркхэм» с билета в тексте не упоминается — ссылок на города нет.
- Картинка раздатки «Будка» (физ. 22) — запись `handout/budka` есть, изображение не добавлено (`app/art/` вне части).
- QR-код и ссылка VK «Уголок Хранителя», благодарности спонсорам — служебная информация издания (упомянуты в `advice`/`summary`).
- Реальные промышленники из примеров к «Богатому бизнесмену» — отдельных записей нет, список в описании типажа.
- Мальчишки-чистильщики, полицейский, продавцы чёрного рынка и карманники на вокзале — без описания и механики, текстом в `location/vokzal`.
- Заклятье «Помутнение» — общая запись `kb/spells` вне части; полный текст у `character/kultist`, черновик — в отчёте.
