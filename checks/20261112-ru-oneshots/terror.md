# «Террор» (terror-ru) — сверка покрытия

Книга: сценарий «Террор» Троя С. Вильгельмсона (при участии Сэма Джонсона и Джадда Лаки; Chaosium, 2005, монография
Miskatonic University Library Association #0322), перевод и неофициальная вёрстка Madcrowde; 30 страниц PDF с текстовым
слоем (метка владельца «[RU 7e]», в `books.json` — `official`). Все числа, статблоки и раздатки сверены по изображениям
страниц. Оригинал написан для 5-й редакции; переводчик привёл его к 7-й по правилам перехода «Книги хранителя» (с. 3, 5) —
статблоки в формате 7-й редакции, поэтому заведены статблоками; `ruleset: "core"`. Эпоха — февраль 1932 года:
`era: ["1930s"]`. Готовых сыщиков в книге нет. Карт нет (только иллюстрации).

Страницы: печатная = физическая − 1 (физ. 4 — «3», физ. 25 — «24»); на обложках, титуле и содержании номеров нет.
Ниже «с.» — печатные страницы.

Префикс записей: `terror-ru/` (ниже — `B/`). Город — общий `coc:location:moscow` (есть в базе); дополнения к нему и
навигационные ссылки у Кремля и Москвы-реки из «Тайн Кремля» — в `proposals-terror.json` (16 предложений, пробный
прогон `apply.py --dry-run` проходит).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка («Монография #0322», «Приключение для НРИ «Зов Ктулху» в Советском Союзе 1930-х годов») | физ. 1 | `B/scenario/terror` (summary, sources); картинка — не взято |
| Титул (авторы, Copyright 2005 Chaosium, перевод Madcrowde) | физ. 2 | `B/scenario/terror` (summary, quality) |
| Содержание | физ. 3 | — (навигация; все разделы ниже) |
| Предисловие от переводчика | 3 | `B/scenario/terror` (advice «От переводчика», quality); `B/organization/transportnyy-otdel-gugb-nkvd` (quality — историческая неточность) |
| Разворот «Террор» (иллюстрация) | 4 | не взято — иллюстрация |
| Введение | 5 | `B/scenario/terror` (summary, advice) |
| Примечание о персонажах | 5 | `B/scenario/terror` (advice) |
| Новые навыки: Бюрократия (10%), Партийные знания (10%) | 6 | `B/scenario/terror` (advice); текстом в сценах; черновики записей навыков — ниже |
| Информация для Хранителя | 6 | `B/scenario/terror` (keeper_info); `B/creature/tungusskiy-meteorit` (legend); `B/character/iosif-stalin` |
| Хронология событий (13 января — 7 февраля 1932 г.) | 6–7 | `B/scenario/terror` — таблица «Хронология событий» |
| Сноска 1 (Северный вокзал = Ярославский) | 6 | `B/location/severnyy-vokzal` (aliases, sources) |
| Несколько слов про «нечто» | 7 | `B/creature/meteoritnoe-nechto` (description, abilities) |
| Допрос (вопросы, речь Рубашова) | 8 | `B/scene/dopros`; `B/character/rubashov` |
| Сноска 2 (ГУГБ НКВД) | 8 | `B/organization/transportnyy-otdel-gugb-nkvd` |
| Вокзал | 9 | `B/scene/vokzal-chto-znayut-rabochie`; `B/location/severnyy-vokzal` |
| Что знают рабочие? | 9–10 | `B/scene/vokzal-chto-znayut-rabochie`; `B/character/osip-fedorov` |
| Товарный вагон (поиск, трупы, тело и карманы Николая) | 10 | `B/scene/tovarnyy-vagon`; `B/location/tovarnyy-vagon-52861`; `B/character/nikolay-lakoba`; `B/item/dokumenty-nikolaya`; `B/item/ampuly-morfina` |
| Материалы дела | 11 | `B/scene/materialy-dela` |
| Тело | 11 | `B/scene/telo`; `B/location/dom-partrabotnikov` |
| Квартира № 3С: гостиная, спальня, кухня, ванная комната | 11–12 | `B/scene/telo`; `B/location/kvartira-3s`; `B/character/yuriy-potakov`; `B/item/fotografiya-stalina-i-potakova`; `B/item/pistolet-potakova` |
| Квартира Николая (ответы Любови, Материал № 1, седан, тело в реке) | 13 | `B/scene/kvartira-nikolaya`; `B/location/kvartira-nikolaya`; `B/character/lyubov-lakoba`; `B/handout/material-1-rasporyazhenie` |
| Информация о поезде | 14 | `B/scene/transportnyy-otdel` |
| Транспортный отдел ГУГБ НКВД (КПП, Рыков, документы) | 14–15 | `B/scene/transportnyy-otdel`; `B/location/transportnyy-otdel`; `B/organization/transportnyy-otdel-gugb-nkvd`; `B/character/aleksey-rykov`; `B/character/vakhtersha-transportnogo-otdela`; `B/item/dokumenty-o-poezde` |
| Назад на вокзал (раздевалка, шкафчики, Молотов в седане) | 15 | `B/scene/nazad-na-vokzal`; `B/character/vyacheslav-molotov` |
| Сноска 3 (Совнарком) | 15 | `B/character/vyacheslav-molotov` (occupation) |
| Пропавший экипаж: Михаил Иванович Калинин | 15 | `B/scene/kvartira-kalinina`; `B/location/kvartira-kalinina`; `B/character/mikhail-kalinin` |
| Борис Ефимович Ефимов | 15–16 | `B/scene/kvartira-efimova`; `B/location/kvartira-efimova` |
| Статблок «Борис Ефимов (метеоритное нечто)» | 16 | `B/character/boris-efimov` (statblock) |
| Исаак Эммануилович Бабель | 16 | `B/scene/kvartira-babelya`; `B/location/kvartira-babelya`; `B/character/isaak-babel` |
| Михаил Константинович Вышинский (звонок) | 16 | `B/scene/zvonok-vyshinskomu`; `B/character/mikhail-vyshinskiy` |
| Скотобойня | 16–17 | `B/scene/skotoboynya`; `B/location/moskovskaya-skotoboynya`; `B/location/okrestnosti-moskvy`; `B/character/konni-tsilliakus` |
| Доктор Червяков | 17 | `B/scene/poiski-chervyakova`; `B/character/viktor-chervyakov` |
| Академия наук СССР | 17 | `B/scene/akademiya-nauk`; `B/location/akademiya-nauk-sssr`; `B/character/sluzhashchaya-akademii`; `B/item/lichnoe-delo-chervyakova` |
| Архивы НКВД в Кремле | 17–18 | `B/scene/arkhivy-nkvd-v-kremle`; `B/location/arkhivy-nkvd-v-kremle` (часть Кремля «Тайн Кремля»); `B/character/osip-mandelshtam`; `B/item/papka-chervyakova-nkvd` |
| Лаборатория доктора Червякова (ответы доктора, 1d10, бегство) | 18–20 | `B/scene/laboratoriya-chervyakova`; `B/location/laboratoriya-chervyakova`; `B/item/papka-tolko-dlya-molotova`; `B/item/shkaf-ogneopasno`; таблица «Действие нечто-Калинина» в `B/scenario/terror` |
| Статблок «Михаил Калинин (метеоритное нечто)» | 19 | `B/character/mikhail-kalinin` (statblock) |
| Статблок «Бабуин (метеоритное нечто)» | 20 | `B/creature/nechto-babuin` |
| Свинцовый ящик, кусок метеорита, Материал № 2 (в тексте) | 20 | `B/scene/osmotr-laboratorii`; `B/item/kusok-meteorita`; `B/handout/material-2-metamorfoza` |
| Кабинет доктора Червякова (стол, шкаф с документами, металлический шкафчик) | 20–21 | `B/scene/osmotr-laboratorii`; `B/location/kabinet-chervyakova`; `B/item/zapis-na-polyakh`; `B/item/fotografiya-na-bolote`; `B/item/spisok-zaklyuchennykh`; `B/item/kinoplenka-eksperimentov`; `B/character/vtoroy-uchenyy` |
| Материал № 3 (в тексте) | 21 | `B/handout/material-3-zapiska` |
| Возвращение на вокзал (Вышинский, погоня, чемодан) | 21–22 | `B/scene/vozvrashchenie-na-vokzal`; `B/item/chemodan-vyshinskogo` |
| Сноска 4 (ЦК ВКП(б)) | 21 | `B/character/mikhail-vyshinskiy` (occupation) |
| Статблок «Четыре бандита НКВД (головорезы Молотова)» | 22 | `B/character/golovorezy-molotova` (statblock + 4 variants) |
| Финал: отчёт о проделанной работе | 23 | `B/scene/final`; `B/character/nikita-khrushchev`; `B/scenario/terror` (conclusion) |
| Наглядные материалы: Материал № 1 | 24 | `B/handout/material-1-rasporyazhenie` (текст по картинке) |
| Материал № 2 | 25 | `B/handout/material-2-metamorfoza` |
| Материал № 2 (карты: «Метаморфоза в нечто», «Новые способности и цель») | 26 | `B/handout/material-2-metamorfoza` (description, aliases) |
| Материал № 3 | 27 | `B/handout/material-3-zapiska` |
| Иллюстрация, задняя обложка (аннотация) | физ. 29–30 | `B/scenario/terror` (sources); картинки — не взято |

Метеорит — «личинка внешнего бога» (с. 6): `B/creature/tungusskiy-meteorit` с `instance_of` на общую
`coc:creature:larvae-of-the-outer-gods`. Нечто: общий вид `B/creature/meteoritnoe-nechto` (`spawn_of` метеорита);
Борис Ефимов и Михаил Калинин — персонажи со статблоком формы нечто и связью `transforms_into` (Р-94);
бабуин — существо `B/creature/nechto-babuin` (`form_of` общего вида).

## Записи (79)

- сценарий 1: `B/scenario/terror` (2 таблицы: «Хронология событий», «Действие нечто-Калинина» 1d10);
- сцены 20: `dopros`, `vokzal-chto-znayut-rabochie`, `tovarnyy-vagon`, `materialy-dela`, `telo`, `kvartira-nikolaya`,
  `transportnyy-otdel`, `nazad-na-vokzal`, `kvartira-kalinina`, `kvartira-efimova`, `kvartira-babelya`,
  `zvonok-vyshinskomu`, `skotoboynya`, `poiski-chervyakova`, `akademiya-nauk`, `arkhivy-nkvd-v-kremle`,
  `laboratoriya-chervyakova`, `osmotr-laboratorii`, `vozvrashchenie-na-vokzal`, `final`;
- персонажи 21 (статблоки: Борис Ефимов, Михаил Калинин, групповой профиль головорезов с 4 вариантами);
- существа 3; места 15; предметы 15; раздатки 3; организация 1.

## Не взято

- Иллюстрации (обложка, разворот с. 4, Борис-нечто с. 16, Калинин в клетке с. 19, Сталин у метеорита с. 22, иллюстрации
  с. 9, 12, 21, задняя обложка) и картинки раздаток: папка `app/art/` вне этой части; при желании их добавит ведущий
  через `pipeline/art/add_images.py` (Материалы № 1–3 — с. 24, 25, 27 физ. 25, 26, 28).
- Рукописные архивные пометки на бланке Материала № 1 («13 … оп», «05.III-40 г», «130») — оформление шаблона, не текст
  раздатки.
- Текст распоряжения на с. 13 напечатан в битой кодировке (кириллица в cp1252) — взят текст раздатки с с. 24;
  расхождения формулировок — в `quality.notes` раздатки.
- Безымянные эпизодические роли без записи (книга не даёт им ни имени, ни особой роли): секретарь и милиционер у
  телефона, высокопоставленный агент НКВД в архиве Кремля, сторож у ворот вокзала и водитель грузовика (хронология),
  жена и маленькая дочь Бориса, два убитых агента НКВД, трое полицейских у реки, рабочие вокзала, работники трудового
  лагеря, водитель седана. Все они описаны в текстах сцен и таблицы хронологии.
- Награды Рассудка — в книге не напечатаны (отмечено в `conclusion`).
- Тунгусский район (тюрьма и болото) — только предыстория; отдельной записи места нет (место без города не входит в
  дерево гайда, Р-189), сведения — в `B/creature/tungusskiy-meteorit` (legend) и у Червякова.

## Черновики новых навыков (общий справочник `kb/skills/` — вне этой части)

- «Бюрократия» (Bureaucracy?, базовый 10%): «показывает, насколько персонаж игрока знает все тонкости того, как
  преодолеть бюрократическую волокиту советской бюрократии; нужных людей, с которыми можно поговорить, нужное
  учреждение, через которое нужно пройти, и правильные формы для заполнения» (с. 6). Механика в сценарии: проверки при
  проходе КПП, в архивы, в Кремль, по телефону, при опознании ампулы морфина.
- «Партийные знания» (базовый 10%): «отражает знания высокопоставленных чиновников Коммунистической Партии, обладающих
  влиянием и связями в Политбюро» (с. 6). Механика: опознать Потакова на фото, Молотова, Вышинского; трудная проверка —
  имя Джугашвили в списке. Английское название в переводе не дано — `name.en` при заведении проверить по оригиналу.

## Сомнения и вопросы

- Скорость 12 у всех трёх профилей нечто при правиле 9 — оставлено как напечатано, `errata` у Бориса и Калинина (Р-76).
- Сталин — запись книги `B/character/iosif-stalin`; в «Тайнах Кремля» есть `secrets-of-the-kremlin-en/character/josef-stalin`.
  Совпадение имён по Р-99 не связь; если владелец решит считать исторических лиц общими (Р-154), их нужно свести в
  `coc:character:*`.
- ГУГБ НКВД в 1932 году — анахронизм книги (переводчик сам предупреждает, с. 3); в записях — как напечатано.
- Книга — фанатский перевод (Madcrowde, «неофициальная вёрстка»), но в `books.json` записана как `official` по метке
  «[RU 7e]» в имени файла владельца — вопрос владельцу, не стоит ли метка «[RU-фан 7e]».
