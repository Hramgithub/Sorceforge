# «The Haunted Clubhouse» (haunted-clubhouse-en) — сверка покрытия

Книга: Leigh Carr, «The Haunted Clubhouse» (Trepan Interactive, 2017), английский оригинал, 22 страницы PDF.
Страницы: печатная = физической (смещение 0): номера напечатаны со с. 2 по с. 21; с. 1 (обложка) и с. 22
(задняя обложка) без номера; с. 19–20 — реклама.

## Главное: сценарий уже в базе по официальному переводу

Этот сценарий уже перенесён целиком по официальному русскому переводу «Маленький клуб ужасов»
(`malenkiy-klub-uzhasov-ru`, перевод SNOKYAN, `edition: official`; сверка `checks/20261112-ru-oneshots/club.md`):
64 записи (сценарий, 18 сцен, 20 персонажей, 3 существа, 3 раздатки, 6 предметов, 13 мест) с картинками,
плюс общие `coc:location:lincoln` и `coc:creature:bear`.
Вёрстка перевода повторяет оригинал страница в страницу (с. 1–18; с. 19 перевода = с. 21 оригинала, с. 20 = с. 22).

По Р-147 при надёжном переводе наш перевод с оригинала не делается: числа берутся из оригинала, русские
формулировки — из перевода, расхождения чисел — в `errata`. Поэтому второй набор записей
`kb/books/haunted-clubhouse-en/` не заведён (он повторил бы 64 записи с теми же `name.ru`); вместо этого —
предложения к записям перевода: `checks/20261116-clubhouse/proposals-clubhouse.json` (230 правок, 66 записей — 64 перевода и 2 общие;
пробный прогон `pipeline/integrate/apply.py --dry-run` — ложится целиком):

- `sources` — английский оригинал у каждой страницы каждой записи (и у общих `coc:location:lincoln`, `coc:creature:bear`), без `corrections`;
- `name.en` — английские названия 45 записей; английские обозначения готовых сыщиков, титулы Смозерса, «Madison Home», «Lincoln Forest Natural Reserve», заголовок вырезки — в `aliases`;
- `text.en` раздаток — газетная вырезка и надписи на стенах, как напечатаны;
- числа и правила, где перевод расходится с оригиналом (ниже), — исправлены по оригиналу, напечатанное в переводе — в `errata`.

Если владелец решит иначе (отдельный набор записей английского издания) — это вопрос к нему, см. «Вопросы».

## Расхождения перевода с оригиналом (исправлены предложениями, Р-147)

| Запись | Перевод (с.) | Оригинал (с.) | Правка |
|---|---|---|---|
| `character/devid-laynkhem` (Дэвид Лайнхэм) | навыка Слух нет (14) | «Listen 50%» (14) | добавлен Слух 50% |
| `character/kodi-bennet` (Тусовщик) | РАС 50 (18) | «SAN 40» (18) | Рассудок 40 |
| `character/kodi-bennet` | «Наука Математика» нет (18) | «Science Mathematics 21%» (18) | добавлена Наука (Математика) 21% |
| `character/kodi-bennet` | «Электрика 205» (18) | «Electrical Repair 20%» (18) | 20% уже было исправлено как вывод; пометка ссылается на оригинал |
| `character/rayan-kallakhan` (Атлет) | Плавание 20% (17) | «Swim 60%» (17) | Плавание 60% |
| `character/stiven-smozers`, таблица «Атаки Смозерса» | Психокинез: «Провал проверки Уклонения» — 3 ПЗ (8) | «A fumbled Dodge roll» (8) | крах проверки Уклонения |
| `character/evan-ross`, таблица «Преобразование в эпоху 1920-х годов» | очки Электроники — в Вождение (13) | «moved to the Ride Skill» (13) | Верховая езда |
| `scene/vozvrashchenie-smozersa`, `scenario/malenkiy-klub-uzhasov` | «вознаградит сыщиков потерей 1D10 Рассудка» (13) | «Defeating Smothers will reward investigators with 1D10 Sanity» (13) | награда +1d10 Рассудка; прежняя пометка «как напечатано» закрыта |

Опечатки самого оригинала — те же, что уже записаны в `errata` перевода, оригинал их подтверждает:
Уолтер Мартин — Драка 65% (30/12), Уклонение 35% (21/8) и «Dodge 40%» в списке навыков (с. 16);
Студент театрального факультета — Уклонение 20% (8/4) (с. 17); красные белки — Укус 35% (12/5) (с. 8);
лось — БкУ +3d6 и Комплекция 4 при СИЛ 140 + ТЕЛ 165 (с. 8). Возраст Смозерса «Age 7» при восьмилетнем
Лайнхэме — как напечатано и в оригинале (с. 12, 14). Мелочь без чисел: «Наука Психология 60%» у Студента
театрального факультета — в оригинале просто «Psychology 60%» (с. 17), ссылка записи уже ведёт на Психологию.

Остальные числа сверены и совпадают: характеристики, ПЗ, ПМ, БкУ, Комплекция, Скорость, атаки и навыки всех
статблоков (с. 8–9, 12, 14–18), стоимости атак в ПМ (5, 5, 10, 15, 25, 30, 5, 5, 10, 15, 20), все потери и награды
Рассудка, пороги 40 и 60 ПМ, 75 ПМ Смозерса, ТЕЛ 200/100 деревьев, ТЕЛ 50 для норы, 15%/1d3 частей тела,
44 исчезновения, 1908 год, 22 мая 1907 года, 19 октября 2016 года, население 1 700 / 1 400.

## Заголовок книги → где в базе

Префикс `malenkiy-klub-uzhasov-ru/` опущен.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «The Haunted Clubhouse — The little play house of horrors» | 1 | `scenario/malenkiy-klub-uzhasov` (sources, name.en); картинка — `checks/20261116-clubhouse/atmosphere.json` |
| Титул | 2 | `scenario/malenkiy-klub-uzhasov` (name.en); оформление — не взято |
| Выходные данные (автор, редакторы, художник, тестировщики) | 3 | `scenario/malenkiy-klub-uzhasov` (summary) |
| Scenario Overview | 3 | `scenario/malenkiy-klub-uzhasov` (summary, advice); `coc:location:lincoln` |
| Keeper Information | 3 | `scenario/malenkiy-klub-uzhasov` (advice); `scene/drugie-ischeznoveniya`; `character/evan-ross` |
| The Town of Lincoln | 4 | `scene/drug-v-bede`; `coc:location:lincoln` |
| A Friend In Need | 4 | `scene/drug-v-bede`; `character/devid-laynkhem`, `character/gregori-miller` |
| The Smothers Missing Persons Case | 4 | `scene/delo-o-propavshem-smozerse`; таблица «Слухи о пропаже Смозерса»; `character/uolter-martin`, `character/alan-smozers`, `location/treyler-smozersov`, `location/odinokoe-ozero` |
| Other Disappearances near Lincoln | 5 | `scene/drugie-ischeznoveniya`; таблица «Другие исчезновения близ Линкольна»; `location/biblioteka-linkolna` |
| Hiking past the Madison Mansion to the Clubhouse | 5–6 | `scene/tropa-cherez-osobnyak-medisona`; `location/osobnyak-medisona`, `location/tonnel-pod-osobnyakom`; `item/mashina-medisona`, `item/bumagi-medisona`; `character/dzheyms-medison` |
| The Lincoln Gazette (вырезка) | 5 | `handout/vestnik-linkolna-1907` (text.en — предложение) |
| The Clubhouse Clearing | 6 | `scene/polyana-kluba`; `location/polyana-kluba`, `location/nora-pod-kornyami`; `handout/pismo-miss-kheyz`; `item/oblomki-kostey`, `item/izurodovannyy-krolik`; `character/miss-kheyz` |
| Врезка об альбоме (scrapbook) | 6 | `item/albom-smozersa` |
| The Clubhouse | 6–7 | `scene/klub`; `location/klub`; `item/zapisnaya-knizhka-smozersa`; `handout/nadpisi-na-stenakh-kluba` (text.en — предложение) |
| Smothers Attacks | 7 | `scene/smozers-atakuet`; `character/stiven-smozers` (abilities.0) |
| Physical attacks: Psychokinesis, Falling Trees, Red Squirrel Pack Attack, Possession of an Investigator, Moose Attack | 8 | `character/stiven-smozers` (abilities 1–5); `creature/krasnye-belki`, `creature/los`; таблица «Атаки Смозерса» |
| Black Bear Attack | 9 | `character/stiven-smozers` (abilities.6); `coc:creature:bear` |
| Psychological attacks: The March of the Insects, The Camp Fire, The Watching Eyes, The Beating of the Rotting Heart, The Overlap of Ahm’hlti | 9 | `character/stiven-smozers` (abilities 7–11); таблица «Атаки Смозерса» |
| Run or Call for Help | 10 | `scene/bezhat-ili-zvat-na-pomoshch`; `character/ofitsery-sherifa`, `character/okhotniki` |
| Death of the Hikers | 10 | `scene/smert-turistov`; `character/rouen-kritchli`, `character/dzhordan-kritchli`, `character/neytan-myuller` |
| Smothers and his Journey Home | 10–11 | `scene/puteshestvie-domoy`; `character/stiven-smozers` (abilities.12) |
| The Birth Canal of Ahm’hlti | 11 | `scene/rodovoy-kanal`; `location/rodovoy-kanal-akhmkhlti` |
| The Womb of Ahm’hlti | 11 | `scene/chrevo-akhmkhlti`; `location/chrevo-akhmkhlti`; `creature/akhmkhlti` |
| Steven Smothers (статблок) | 12 | `character/stiven-smozers` |
| Conclusions | 12–13 | `scenario/malenkiy-klub-uzhasov` (conclusion, steps «Финал») |
| Leave the Clearing and Never Return | 12 | `scene/pokinut-polyanu` |
| Burn the Clubhouse and the Clearing | 12 | `scene/szhech-klub` |
| The Death of Smothers | 12 | `scene/smert-smozersa` |
| Consumed by Ahm’hlti | 12 | `scene/pogloshchyonnyy-akhmkhlti` |
| Escape the Clubhouse | 12 | `scene/pobeg-iz-kluba` |
| Smothers Returns | 12–13 | `scene/vozvrashchenie-smozersa`; `character/stiven-smozers` (abilities.13) |
| Converting to a 1920s Era (The Town Lincoln, Lincoln School, Madison Mansion, Lineham’s Parents, Mobile Phones / Smart Phones, Clubhouse Interior, Pre-Generated Investigator Skills, Pre-Generated Investigator Backstories) | 13 | таблица сценария «Преобразование в эпоху 1920-х годов»; абзацы «В 1920-х» в `coc:location:lincoln`, `location/srednyaya-shkola-linkolna`, `location/osobnyak-medisona`, `location/klub`, `character/geyl-laynkhem`, `character/semyuel-laynkhem`, готовых сыщиках |
| Non-Player Characters: David Lineham | 14 | `character/devid-laynkhem` (+ `character/geyl-laynkhem`, `character/semyuel-laynkhem`) |
| Gregory Miller | 15 | `character/gregori-miller` (+ `character/pol-miller`, `character/syu-miller`) |
| Walter Martin | 16 | `character/uolter-martin` |
| Pre-Generated Investigators: Drama Student and Student Council President | 17 | `character/tayler-bruks` |
| Athlete | 17 | `character/rayan-kallakhan` |
| Party Animal | 18 | `character/kodi-bennet` |
| A Grade Student | 18 | `character/evan-ross` |
| Реклама Cryo Chamber | 19 | не взято |
| Реклама Fragged Aeternum | 20 | не взято |
| Copyright, Special Thanks | 21 | `scenario/malenkiy-klub-uzhasov` (sources: авторские права) |
| Задняя обложка: аннотация | 22 | `scenario/malenkiy-klub-uzhasov` (summary); картинка — `checks/20261116-clubhouse/atmosphere.json` |

Картинки оригинала — те же, что в переводе, и уже стоят в записях перевода: Лайнхэм (с. 14), Миллер (с. 15),
Мартин (с. 16), лось (с. 7), Ахм’хлти/Смозерс в коконе (с. 11), вырезка «Вестника» (с. 5); тело на с. 10 и
обложки — в атмосфере. Новых картинок для записей нет, `art.json` не нужен.

## Не взято

- Отдельный набор записей `kb/books/haunted-clubhouse-en/` — повторил бы перевод (Р-147); см. выше.
- С. 2 — титул (оформление). С. 19 — реклама музыкального лейбла Cryo Chamber; с. 20 — реклама игры Fragged Aeternum: не материал сценария.
- С. 21 — благодарности (имена людей без игровой роли).
- Врезка об альбоме на с. 6 оформлена как записка, но это текст для Хранителя, уже в `item/albom-smozersa`; отдельной картинки не нужно.

## Термины (English → русский, по официальному переводу)

Новых терминов нет: все формы берутся из официального перевода и записей `malenkiy-klub-uzhasov-ru`.

| English | Русский |
|---|---|
| The Haunted Clubhouse | «Маленький клуб ужасов» (название перевода) |
| Clubhouse | Клуб |
| The Clubhouse Clearing | Поляна Клуба |
| Ahm’hlti | Ахм’хлти |
| The Womb of Ahm’hlti | Чрево Ахм’хлти |
| The Birth Canal of Ahm’hlti | Родовой канал Ахм’хлти |
| Fetus of Ahm’hlti and Haunter of the Clubhouse | Плод Ахм’хлти и Призрак Клуба |
| Lincoln, New Hampshire | Линкольн, Нью-Гэмпшир |
| Lincoln High School / Lincoln School (1920s) | Средняя школа Линкольна / Школа Линкольна |
| Lincoln town library | Городская библиотека Линкольна |
| Madison Mansion / old Madison Home | Особняк Мэдисона / старый дом Мэдисона |
| The Lincoln Gazette | «Вестник Линкольна» |
| Lonesome Lake | Одинокое озеро |
| Grafton County Sheriff | шериф округа Графтон |
| Concord (forensics laboratory) | Конкорд (криминалистическая лаборатория) |
| White Mountain National Forest | Национальный лес Большой Белой горы |
| Lincoln Forest Natural Reserve | природный заповедник Линкольн-Форест |
| Hadron Collider | Адронный коллайдер |
| black light / black ray | «чёрный свет» / чёрный луч |
| Smothers Attacks | Смозерс атакует |
| Physical attacks / Psychological attacks | Физические атаки / Психологические атаки |
| Psychokinesis | Психокинез |
| Falling Trees | Падающие деревья |
| Red Squirrel Pack Attack | Атака стаи красных белок |
| Possession of an Investigator | Контроль над сыщиком |
| Moose Attack | Нападение лося |
| Black Bear Attack | Нападение чёрного медведя |
| The March of the Insects | Марш насекомых |
| The Camp Fire | Лагерный костёр |
| The Watching Eyes | Наблюдающие глаза |
| The Beating of the Rotting Heart | Биение гниющего сердца |
| The Overlap of Ahm’hlti | Видение Ахм’хлти |
| Buck / Charging Antlers / Biting | Таран / Удар рогами / Укус |
| Scrounge for food / Scent Prey | Выпрашивание еды / Запах добычи |
| hikers / Hunters / officers | туристы / Охотники / офицеры шерифа |
| Run or Call for Help | Бежать или звать на помощь |
| Death of the Hikers | Смерть туристов |
| Smothers and his Journey Home | Смозерс и его путешествие домой |
| Conclusions | Финал |
| Leave the Clearing and Never Return | Покинуть поляну и никогда не возвращаться |
| Burn the Clubhouse and the Clearing | Сжечь здание Клуба и поляну |
| The Death of Smothers | Смерть Смозерса |
| Consumed by Ahm’hlti | Поглощённый Ахм’хлти |
| Escape the Clubhouse | Побег из Клуба |
| Smothers Returns | Возвращение Смозерса |
| Converting to a 1920s Era | Преобразование в эпоху 1920-х годов |
| Non-Player Characters / Pre-Generated Investigators | Персонажи / Готовые сыщики |
| Drama Student and Student Council President | Студент театрального факультета и Президент Школьного Совета |
| Athlete / Party Animal / A Grade Student | Атлет / Тусовщик / Отличник |
| Student Council President | Глава (Президент) Школьного совета |
| Captain Woof | Капитан Гав |
| Art/Craft Crude Fireworks | Искусство/ремесло (Простой фейерверк) |
| Dewey Decimal numbers | номера десятичной классификации Дьюи |
| fumble / Ride | крах / Верховая езда (глоссарий; в переводе здесь ошибки «провал» и «Вождение») |

Имена: Steven Smothers — Стивен Смозерс; David Lineham — Дэвид Лайнхэм; Gregory Miller — Грегори Миллер;
Walter Martin — Уолтер Мартин; Alan Smothers — Алан Смозерс; Miss Hays — мисс Хейз; James Madison — Джеймс Мэдисон;
Gayle, Samuel Lineham — Гейл, Сэмюэл Лайнхэм; Paul, Sue Miller — Пол, Сью Миллер; Rowan, Jordan Critchley —
Роуэн, Джордан Критчли; Nathan Muller — Нэйтан Мюллер. Придуманные имена готовых сыщиков (Р-150) — из записей
перевода: Тайлер Брукс, Райан Каллахан, Коди Беннет, Эван Росс.

## Вопросы

1. Оригинал уже перенесённого официального перевода: правильно ли не заводить второй набор записей, а дописать
   оригинал к записям перевода (предложения `proposals-clubhouse.json`)? Рекомендация — да (Р-147).
2. Картинка с. 11 (существо в коконе с головой, подпись «Smothers stands upright, restrained by a fluid sack cage
   inside of Ahm’hlti») в переводе стоит у `creature/akhmkhlti`; по подписи это скорее Смозерс в коконе
   (`character/stiven-smozers`). Не правил — решение за владельцем.
