# «Мистер Корбитт» — сверка покрытия (Р-134, Р-218)

Книга `osobnyaki-bezumiya-ru` (скан Hobby World, печатная = физическая − 1), гл. 1, с. 11–40, и «Материалы для игроков» с. 180–190.
Текст — распознавание `.cache/ocr` со сверкой каждой страницы по изображению (pdftoppm 150–300 dpi); статблоки — по увеличенным вырезкам.
Префикс записей: `osobnyaki-bezumiya-ru/<kind>/corbitt-…`; ниже — без префикса.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Мистер Корбитт (вступление, подзаголовок, 1–3 встречи) | 11 | scenario `mr-corbitt` (summary) |
| Информация для Хранителя; врезка «Хранителю на заметку» (Бостон или другой город) | 11 | scenario (keeper_info); location `chestnut-street` |
| Вовлечение сыщиков | 11–12 | scenario (hook, advice); location `investigator-house` |
| Навыки, которые пригодятся | 12 | scenario (advice) |
| Связь с Йог-Сототом | 12–13 | scenario (keeper_info); characters `bernard-corbitt`, `theodore-corbitt`, `elaine-corbitt`, `lynn-corbitt`, `mona-dunlap`; creatures `ramasekva`, `thing-child` |
| Действующие лица: Мистер Корбитт | 13 | character `bernard-corbitt` (description, background, legend) |
| Действующие лица: Рэндольф Томашевский | 14 | character `randolph-tomaszewski` |
| Действующие лица: Ман-Багари, Тварь-Дитя | 14 | creature `thing-child` |
| Завязка: странные свёртки; «Хранителю на заметку» | 14 | scene `strange-bundles`; item `canvas-bundles` |
| Расследование; Образ жизни Корбитта | 15 | scene `investigation` |
| Владения мистера Корбитта. План дома и участка (карта, обозначения 1–3) | 15 | map `estate` (app/maps/mansions-corbitt-estate.jpg); locations `estate`, `1-greenhouse`, `2-vegetable-garden`, `3-house` |
| Врезка «Звонок в полицию» | 15 | scene `police-call` |
| «Хранителю на заметку» (поездки по средам, клуб) | 16 | scene `investigation`; organization `businessmen-club` |
| Соседи — персонажи Хранителя (имена) | 16 | character `neighbors` (`names`) |
| Общеизвестная биография Корбитта | 16 | scene `investigation`; character `bernard-corbitt` |
| Работа Корбитта; Роем глубже; «Хранителю на заметку» | 16–17 | scene `company`; organization `importers-of-america`; location `importers-warehouse`; items `company-ledgers`, `statuette` |
| Врезка «Рука помощи»: Харриет Харт, Ребекка Уоллас, Бобби Лински | 17 | characters `harriet-hart`, `rebecca-wallace`, `bobby-linski`; location `hart-house` |
| «Хранителю на заметку» (статуэтка, Оккультизм / Мифы Ктулху) | 18 | item `statuette` |
| Заметки из газет | 18 | scene `newspapers`; location `district-library` |
| Материал «Корбитт 1» | 18, 181 | handout `1-theodore-death` |
| Материал «Корбитт 2» (некрологи, «Сиделка госпитализирована…») | 18, 180 | handout `2-obituary-and-nurse`; characters `edward-myers`, `shirley-myers` |
| Психиатрическая больница | 19 | scene `psychiatric-hospital`; location `central-psychiatric-hospital`; character `dunlap-doctor` |
| Знакомый из больницы | 19 | scene `tomaszewski-trail`; location `central-hospital` |
| Как напасть на след Томашевского | 19–20 | scene `tomaszewski-trail` |
| Материал «Корбитт 3» | 19, 181 | handout `3-animal-slayings` |
| Встреча с Томашевским | 20 | scene `tomaszewski-trail`; location `tomaszewski-apartment`; item `tomaszewski-paraphernalia` |
| Находки среди мусора | 20, 22 | scene `dump`; location `city-dump`; item `canvas-bundles` |
| Врезка «Лицом к лицу с Корбиттом»; Зелья Корбитта; Другие способы | 21 | scene `confrontation`; item `potions` |
| «Хранителю на заметку» (вопросы о свалке, приглашение в теплицу) | 22 | scene `dump` |
| Отъезд Корбитта | 22 | scene `departure`; item `potions` |
| Дом Корбитта | 22 | location `3-house`, `chestnut-street` (полиция при взломе) |
| Вокруг дома: Теплица | 22 | scene `greenhouse`; location `1-greenhouse` |
| Оранжевая лиана | 22–24 | item `orange-vine`; creature `otherworld-thing` |
| План дома мистера Корбитта (обозначения 1–19, лестница, потайная дверь, камин) | 23, 190 | map `house` (app/maps/mansions-corbitt-house.jpg); locations `house-1-porch` … `house-19-thing-room` (19 мест; № 3, 15, 19 — подробные) |
| Пурпурный цветок | 24–25 | creature `purple-flower`; scene `greenhouse` |
| Огород | 25 | scene `vegetable-garden`; location `2-vegetable-garden` |
| Внутри дома; Первые эксперименты Корбитта | 25 | scene `inside-the-house`; creature `running-thing`; location `house-18-workshop` |
| Первый этаж; Гостиная (3) | 25–26 | scene `first-floor`; location `house-3-living-room`; tomes `key-and-gate`, `twelve-occult-experiments`, общая `coc:tome:true-magick`; items `botanical-notes`, `soma`, `dictionaries` |
| Дневники; «Хранителю на заметку I», «…II» | 26 | handout `4-diaries` (description); scene `first-floor` |
| Врезка «Ключ и Врата»; «Заклинание „Вызов Рамасеквы“» | 26 | tome `key-and-gate`; item `soma` |
| Второй этаж: Хозяйская спальня (14), Детская (12), Пустые спальни (10) | 27 | scene `second-floor`; locations `house-14-master-bedroom`, `house-12-nursery`, `house-10-empty-bedrooms` |
| Подвал: Лаборатория (15) | 27 | scene `laboratory`; location `house-15-laboratory` |
| Комната твари (19); Тактика Твари-Дитя | 27, 35 | scene `thing-room`; location `house-19-thing-room`; creature `thing-child` |
| Материал «Корбитт 4», стр. 1–7 (Дневник № 1, 2, 13, 14) | 28–34, 182–188 | handout `4-diaries` (text — полностью, как напечатано) |
| «Хранителю на заметку» (кормление твари) | 35 | scene `thing-room` |
| Завершение | 35 | scenario (conclusion); creature `man-bagari` |
| Награды | 35 | scenario (conclusion, шесть пунктов) |
| Как продлить этот ужас | 36 | scenario (conclusion) |
| Персонажи и чудовища: Персонажи Хранителя — Бернард Корбитт, Рэндольф Томашевский, Харриет Харт, Ребекка Уоллас, Бобби Лински | 37 | characters (statblock) |
| Существа и чудовища: Тварь из иного мира, похожая на паука | 38 | creature `otherworld-thing` |
| Бегающая тварь, плод экспериментов Корбитта | 38 | creature `running-thing` |
| Ман-Багари: Тварь-Дитя, незрелая форма | 38 | creature `thing-child` |
| Ман-Багари, зрелая форма | 39 | creature `man-bagari` |
| Владения мистера Корбитта — материал для игроков | 189 | map `estate` (sources; план тот же) |
| План дома мистера Корбитта — материал для игроков | 190 | map `house` (картинка взята отсюда) |

Готовые сыщики сборника (`za-zakrytymi-dveryami-ru/character/*`, шесть) — в `refs` сценария, не дублировались.

## Записи (88 файлов + 2 картинки)

scenario 1; scene 17; location 32 (улица, участок, дом, 19 комнат плана, теплица, огород, дом сыщика, дом Хартов, склад, библиотека, две больницы, квартира Томашевского, свалка); map 2; character 13; creature 6; item 9; handout 4; tome 2; organization 2.

## Опечатки и сомнения

- Бобби Лински: ПМ 13 при МОЩ 45 (должно быть 9) — `errata`, как напечатано.
- Ман-Багари (зрелая): БкУ +8d6 и Комплекция 9 при СИЛ 250 + ТЕЛ 250 = 500 (по таблице +5d6 и 6) — `errata`, как напечатано.
- Материал «Корбитт 2» против дневников: некролог говорит «вышла замуж … два года назад» и датирован 12 лет назад, а по дневнику № 2 свадьба (9 марта) и роды (21 ноября) — в одном году, 13 лет назад — `errata` у раздатки.
- Три процента Корбитта у корешка размыты (Наука (фармакология) 85%, Нетрадиционная хирургия 87%, Язык (санскрит) 40%) — прочитаны по увеличенной вырезке и совпадают с изданием 6-й редакции.
- Раздатки сценария начинаются в «Материалах для игроков» не с с. 182, как в задании, а с с. 180 («Корбитт 2») и с. 181 («Корбитт 1», «Корбитт 3»); с. 189–190 — карты для игроков.
- Где стоит дом Хартов (на Честнат-стрит или рядом) и где городская свалка, книга не говорит — помечено в записях.

## Не взято

- Иллюстрации (с. 24 «В теплице», с. 36 «Дом Корбитта», с. 40 — полностраничная картина с Тварью-Дитя и Корбиттом): картинки в `app/art` не добавлялись — нет механики; их можно добавить позже через `pipeline/art/add_images.py`.
- Коран (арабское издание) на полке Корбитта — книга без игровых свойств, упомянута в описании гостиной.
- Муж Ребекки Уоллас Уолтер, пёс Бобби Бэзил, сторож склада, двое полицейских, агенты ФБР — упомянуты в текстах записей, отдельных записей нет (нет данных).
- Заклинание «Вызов Рамасеквы» как отдельная запись: вариация «Вызова Йог-Сотота» (стоимость не менее 1 ПМ с человека и 1d10 Рассудка заклинателя, 1–100 минут, вместо каменной башни — зелье «сома») — текст в книге `key-and-gate`, ссылка на `coc:spell:call-dismiss-yog-sothoth`; кандидат в `kb/spells` (решать ведущему).
- «Изготовление незаметных ядов», «Нетрадиционная хирургия», «Чутьё на еду» — навыки без механики (Р-126), остались текстом в статблоках.
