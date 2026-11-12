# «Bless the Beast and Children» («Благослови детей его») — сверка заголовков (часть bless)

Книга `bless-the-beast-and-children-ru` — перевод владельца (Р-223, `trusted`), единственный источник; оригинал не найден.
Читалось: `Bless_the_Beast_and_Children_Full_RU_v1.html` (порядок текста) и `Pdf/Bless_the_Beast_and_Children_Full_RU_v1.pdf`
(15 страниц, номеров не печатает: печатная страница = странице PDF; числа и статблоки сверены по изображениям страниц).
`pages.py text` для этой книги не работает: в `books.json` поле `pdf` указывает на HTML, а `pdftotext` его не читает.
По колонтитулу карты Фалькон-Пойнта («48 Adventures In Arkham Country») оригинал — сборник Chaosium «Adventures in Arkham Country» (вывод).

Записи: `kb/books/bless-the-beast-and-children-ru/` — сценарий 1, сцен 21, персонажей 31, мест 19, предметов 7,
раздаток 5, карт 4, существ 1 (всего 89). Картинки карт: `app/maps/bless-arkham.jpg`, `bless-kidnappers-hideout.jpg`,
`bless-falcon-point.jpg`, `bless-beach-house.jpg`. Предложения: `proposals-bless.json` (25 правок, 6 записей; пробный прогон проходит).

Пометки Р-223: у всех записей флаг `translated`; у записей с числами (статблоки, потери Рассудка, проверки, суммы) — элемент
`errata` «Оригинал не найден, числа не сверены (Р-223)» и, значит, `parse_uncertain` (Р-141 требует флаг ровно при `errata`);
`sources[].verified: false`. Официальные названия «Побега из Иннсмута» важнее написания перевода: «Фалькон-Пойнт»
(в переводе — «Фалкон-Пойнт», «Фэлкон-Пойнт»; в псевдонимы — предложением). Меры переведены в метрические (Р-64).

Префикс id ниже: `B/` = `bless-the-beast-and-children-ru/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) Bless the Beast and Children / Благослови детей его | 1 | `B/scenario/bless-the-beast-and-children` (name, sources) |
| Содержание | 2 | сверка этой таблицы |
| Благословите зверей и детей | 3 | сценарий: `hook`; псевдоним сценария |
| Сведения для сыщиков | 3 | `B/scene/nachalo-pokhishcheniya`; `B/character/charlz-anderson`, `dzhun-anderson`, `robert-bekvort`; `B/location/tauer-bilding`, `klub-miskatonik` |
| ДЕТСКИЕ БУМАГИ #1 | 3 | `B/handout/detskie-bumagi-1` |
| Сведения для Хранителя | 3 | сценарий: `keeper_info`; `B/character/garold-snouden` (legend) |
| ДЕТСКИЕ БУМАГИ #2 | 3–4 | `B/handout/detskie-bumagi-2` |
| Варианты Иннсмута | 4 | сценарий: `keeper_info`, `advice`; `garold-snouden`, `denni-eyms` (legend); `B/item/zapisi-snoudena`; `B/creature/glubokovodnye-plyazhnogo-domika` (legend) |
| Ключ к карте Аркхэма | 5 | `B/map/karta-arkhema` (метки 1–14); места 1–12: `B/location/politseyskiy-uchastok-arkhema`, `otel-miskatonik`, `innsmouth-terror-en/location/arkham-advertiser` (3), `redaktsiya-arkham-gazett`, `coc:location:orne-library` (5), `tauer-bilding`, `pervaya-presviterianskaya-tserkov`, `molochnaya-ferma-arkham-farms`, `upravlenie-arkhemskogo-tramvaya`, `arkham-keb`, `klub-miskatonik`, `mesto-obnaruzheniya-trupa` |
| Карта Аркхэма | 5 | `B/map/karta-arkhema`; номера 13 и 14 без ключа — `B/location/dom-segreto`, `B/location/dom-pokhititeley` (догадки, см. вопросы) |
| Похищение | 5 | сценарий: `keeper_info`; `B/character/emili-langford`; `B/location/mesto-obnaruzheniya-trupa`; `B/item/detskaya-kolyaska` |
| Второе похищение (для Хранителя) | 5 | сценарий: `keeper_info`; `B/scene/vtoroe-pokhishchenie` |
| Аркхэм | 5 | `B/scene/nachalo-pokhishcheniya`; сценарий: `advice` |
| Аркхэмская полиция | 5–6 | `B/scene/arkhamskaya-politsiya`; `B/character/eysa-nikols`, `lyuter-harden`; `B/location/politseyskiy-uchastok-arkhema` |
| Список источников | 5–6 | `B/scene/spisok-istochnikov`; `B/character/gregori-dalberg`, `donni-o-shi`; места 8, 9, 10 |
| Жуткая находка | 6–7 | `B/scene/zhutkaya-nakhodka`; `B/item/zolotaya-serga`, `goluboy-chepchik` |
| След остывает? | 7 | `B/scene/istoriya-denni-eymsa` (начало); сценарий: `advice` |
| История Дэнни Эймса | 7 | `B/scene/istoriya-denni-eymsa`; `B/character/denni-eyms` |
| Старьевщик Хайрам | 7 | `B/scene/starevshchik-khayram`; `B/character/khayram`; `B/item/detskaya-kolyaska` |
| Второе похищение | 7 | `B/scene/vtoroe-pokhishchenie`; `B/character/donna-segreto`, `dzhozef-segreto`, `mariya-segreto`, `art-smit`; `B/location/dom-segreto`; `B/item/furgon-ford` |
| Похитители залегают на дно | 7 | `B/scene/dom-pokhititeley` (первый абзац) |
| Дом похитителей | 7 | `B/scene/dom-pokhititeley`; `B/location/dom-pokhititeley` |
| Убежище похитителей | 8 | `B/scene/dom-pokhititeley`; `B/location/dom-pokhititeley` (`history`) |
| Обстановка | 8 | `B/scene/dom-pokhititeley` |
| Дом (Living Room, Kitchen, The Bedroom, Ванная, Подвал, Задний двор, Гараж) | 8–9 | `B/location/dom-pokhititeley` (описание по комнатам); `B/item/slonoboynoe-ruzhe`, `furgon-ford` |
| ДЕТСКИЕ БУМАГИ #3 | 8 | `B/handout/detskie-bumagi-3` |
| План «The Kidnapers’ Hideout» | 8 | `B/map/dom-pokhititeley` (8 подписей) |
| Нагнать мошенников | 9 | `B/scene/nagnat-moshennikov` |
| Завершение в Аркхэме | 9 | `B/scene/zavershenie-v-arkheme`; сценарий: `conclusion` |
| Государственная больница | 9–10 | `B/scene/gosudarstvennaya-bolnitsa`; `B/character/enson-best`; место — `dveri-vo-tmu-ru/location/genius-danvers-asylum` (предложения) |
| ДЕТСКИЕ БУМАГИ #4 | 10 | `B/handout/detskie-bumagi-4` |
| Посещение Дэнни Эймса | 10–11 | `B/scene/poseshchenie-denni-eymsa`; `B/character/denni-eyms` |
| Газетные истории | 11 | `B/scene/gazetnye-istorii` |
| ДЕТСКИЕ БУМАГИ #5 | 11 | `B/handout/detskie-bumagi-5` |
| Первая баптистская церковь | 11 | `B/scene/pervaya-baptistskaya-tserkov`; `B/location/pervaya-baptistskaya-tserkov`; `B/character/charlz-noyes` |
| Фалкон-Пойнт | 11 | `B/scene/falkon-poynt`; сценарий: `advice`; место — `coc:location:innsmouth-1010-falkon-poynt` (предложения) |
| Деревня | 11 | `B/scene/falkon-poynt`; `B/location/dom-ebigeyl-harding`; предложение к описанию Фалькон-Пойнта |
| Магазин наживки и снастей | 11–12 | `B/scene/falkon-poynt`; `B/location/magazin-van-de-forda`; `B/character/delmar-van-de-ford`; `B/item/zolotaya-moneta` |
| Карта Фалкон-Пойнта | 12 | `B/map/falkon-poynt` (9 подписей) |
| Джек Уилсон | 12 | `B/scene/falkon-poynt`; `B/character/dzhek-uilson`; `B/location/dom-dzheka-uilsona` |
| Эбигейл Хардинг | 12 | `B/scene/ebigeyl-harding`; `B/character/ebigeyl-harding` |
| Ферма Келсо | 12 | `B/location/ferma-kelso` |
| Майк Келсо | 12–13 | `B/scene/ferma-kelso`; `B/character/maykl-kelso`, `sara-kelso` |
| Расследование дела Келсо | 13 | `B/scene/rassledovanie-dela-kelso` |
| Следующий ход | 13 | `B/scene/rassledovanie-dela-kelso` |
| Пляжный домик | 13 | `B/location/plyazhnyy-domik`; `B/scene/plyazhnyy-domik` (расстановка днём) |
| План пляжного домика и пещеры | 13 | `B/map/plyazhnyy-domik` (7 подписей) |
| Снаружи дома | 13–14 | `B/scene/plyazhnyy-domik`; `B/location/plyazhnyy-domik` (ручей, лодки) |
| Пещера | 14 | `B/location/peshchera-pod-plyazhnym-domikom`; `B/scene/spasenie-detey` |
| Спасение детей | 14 | `B/scene/spasenie-detey`; `B/item/zapisi-snoudena` |
| Для кровожадного Хранителя | 14 | `B/scene/spasenie-detey` (последний абзац); `coc:creature:shoggoth` |
| Спасенные дети | 14 | `B/scene/spasennye-deti`; `B/character/piter`, `rut`, `salli`, `billi` |
| Награды и штрафы | 14 | сценарий: `conclusion` |
| Статблоки | 15 | статблоки персонажей ниже |
| Чало Таламентес, 29, похититель | 15 | `B/character/chalo-talamentes` |
| Ник Касл, 24, похититель | 15 | `B/character/nik-kasl` |
| Преподобный Гарольд Сноуден, 48, лишенный сана человек божий | 15 | `B/character/garold-snouden` |
| Оскар Венторф, 26, гибрид глубоководного | 15 | `B/character/oskar-ventorf` |
| Дэнни Эймс, 18, безумный эксперимент | 15 | `B/character/denni-eyms` (основной блок + вариант «Во время припадков») |
| Майкл Келсо, 42, фермер | 15 | `B/character/maykl-kelso` |
| Сара Келсо, 33, жена фермера | 15 | `B/character/sara-kelso` |
| Мелисса и Шэрон, 28 и 29, гибридные няньки | 15 | `B/character/nyanki-melissa-i-sheron` (один профиль на двоих) |

## Не взято

- Картинки-иллюстрации — в `app/art/` писать не моя часть (только `app/maps/bless-*`). Для ведущего — разметка
  для `pipeline/art/add_images.py` (папка `C:\_Hobby\Yandex.Disk\НРИ\1_Зов Ктулху\2_Обработка\1920 Bless the Beast and Children\Images\`):
  ```json
  [
    {"target": "bless-the-beast-and-children-ru/character/denni-eyms", "src": "<папка>/Source_Images/bless-page-011-source-illustration-render.png",
     "kind": "portrait", "caption": "Дэнни Эймс", "source": "«Благослови детей его», перевод владельца, с. 11 (иллюстрация оригинала, подпись «Danny Ames»)"},
    {"target": "bless-the-beast-and-children-ru/scene/nachalo-pokhishcheniya", "src": "<папка>/Source_Images/bless-page-006-source-illustration-render.png",
     "kind": "illustration", "caption": "Двое мужчин над чертежами у окна с видом на город", "source": "«Благослови детей его», перевод владельца, с. 6 (иллюстрация оригинала без подписи)"},
    {"target": "bless-the-beast-and-children-ru/scenario/bless-the-beast-and-children", "src": "<папка>/Landing/bless_landing_no_caption.png",
     "kind": "art", "caption": "Обложка перевода (глубоководный и ребёнок)", "source": "папка владельца, Images/Landing — раздатка владельца"}
  ]
  ```
  Кто изображён на с. 6, книга не говорит (по смыслу — Андерсон и Бекворт над планами завода; не утверждаю).
- Люди, упомянутые только текстом (без записей, остались в описаниях): Маргарет Андерсон (4 года, осталась дома с насморком),
  судмедэксперт Эфраим Спраг, таксисты Брайан Кэнфилд, Пол Уайатт, Леон Отт, родители Дэнни Питер и Синтия Эймс, дядя Дэнни
  (истинный растлитель), утонувший ребёнок, юный глубоководный, спасший Сноудена (в `legend` существа), Кеннет Росс (в `history` дома),
  двое мальчишек с мячом.
- Дом Сноудена в Иннсмуте — места книга не даёт (выбирает Хранитель); записи нет, сказано в сценарии и в записях Сноудена.
- «Здание суда в Иннсмуте» (записи о собственности) — общей записи суда нет, с Ратушей не отождествлял; оставлено текстом в сцене
  (`where` — сам Иннсмут).
- Глостер (машина Сноудена, почтовый грузовик) — записи города нет; текстом.
- Подпись «Atlantic Ocean» на карте Фалькон-Пойнта — записи нет, метки нет. Дом Джедедайи Харпера и подписи дорог/ручья — метки ведут на
  Фалькон-Пойнт и «Дороги из Иннсмута» с `text`.
- «Награды Рассудка за убийство глубоководных описаны в правилах» — без ссылки (числа в книге нет).

## Опечатки и сомнения книги (в `errata` записей)

- Чарльз Андерсон в «Детских бумагах #1» — «бостонский» промышленник, везде — нью-йоркский (`charlz-anderson`, `detskie-bumagi-1`).
- Возраст Донны Сегрето: «трех лет» (с. 5) / «тринадцати месяцев» (с. 7) (`donna-segreto`, `vtoroe-pokhishchenie`).
- Дэнни пропал «более десяти лет назад» (с. 7) / «десять лет назад» (с. 10) / «более семи лет назад» (с. 11) (`denni-eyms`, `gazetnye-istorii`).
- Дэнни прожил дома до смерти матери «год» (с. 7) / «шесть месяцев» (с. 9) (`denni-eyms`, `gosudarstvennaya-bolnitsa`).
- Майк Келсо в сцене — 12-калиберный дробовик с солью, 75%, 1d6 (с. 13); в статблоке — 20-калиберный, 65% (`maykl-kelso`, `rassledovanie-dela-kelso`).
- План пляжного домика: спальни «Men’s / Nannies’ / Kid’s», текст: мужчины спят в жилой комнате, спальни — нянек, младенцев, средних детей (заметка метки и `quality.notes` места).
- Метка 12 карты стоит у Баундари между Солтонстолл и Вашингтон, текст — между Вашингтон и Мискатоник (заметка метки).
- «Ford Model A» в статье десятилетней давности — анахронизм (модель с конца 1927 г.; пометка в `detskie-bumagi-5`).
- Написание в переводе: Харден/Хардин, Эйса/Аса Николс, Венторф/Вентоф, Mellisa/Melissa — в псевдонимах.

## Вопросы владельцу

1. Номера 13 и 14 на карте Аркхэма не расшифрованы в ключе. Метка 14 стоит у Хилл-стрит между Хай и Солтонстолл — поставил на дом
   похитителей (вывод); метку 13 (Френч-Хилл, у Сентинел-стрит) — на дом Сегрето (догадка: фургон уехал от него на запад по Хай-стрит).
   Верно ли?
2. Р-223 просит `parse_uncertain` у записей с числами, а Р-141 разрешает флаг только при непустом `errata` — поставил в `errata` элемент
   «Оригинал не найден, числа не сверены (Р-223)». Так и оставить?
3. Р-154: Данверская психбольница (`dveri-vo-tmu-ru/location/genius-danvers-asylum`) и редакция «Аркхэм эдвертайзер»
   (`innsmouth-terror-en/location/arkham-advertiser`) теперь встречаются во второй/третьей книге — перенос в общие записи
   (`coc:location:…`) с переписью ссылок за ведущим; я только сослался на них и предложил псевдонимы/абзац для больницы.

## Технический долг

- `pipeline/source/books.json`: `pdf` книги указывает на HTML — `pages.py text/show/grep/image` не работают; стоит указать
  `Pdf\Bless_the_Beast_and_Children_Full_RU_v1.pdf` (не моя часть).
