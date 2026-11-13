# «Лохмотья Короля» — часть madman: сверка покрытия

Книга `lokhmotya-korolya-ru` (RU 7e, официальный перевод; печатная страница = физической). Страницы части: 35–59, 332–335
(раздаточный материал № 5 начинается на с. 332 под окончанием № 4). Глава 1 «Безумец», этап `L/scenario/madman` (order 2).
Префикс `L/` ниже = `lokhmotya-korolya-ru/`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Картинка (силуэт города) | 35 | не взято (см. ниже) |
| «Книга I. Безумец» (титул книги, картинка) | 36 | `L/scenario/madman`: `name`, `quality.notes`; Книга I — `L/scenario/tatters-of-the-king` (часть intro) |
| «Глава 1. Безумец» (заголовок-картинка), эпиграфы Чемберса и Майкла Ши | 37 | `L/scenario/madman`: `name`; эпиграфы — `advice` |
| Вступление: письмо Хайсмита 19 октября 1928, «симпатическая мания», примечание хранителя о поле адресата | 37 | `madman`: `hook`, `keeper_info`; `L/scene/madman-interview-with-dr-highsmith` |
| Беседа с доктором Хайсмитом | 37–38 | `L/scene/madman-interview-with-dr-highsmith`; `L/location/madman-great-western-hotel` |
| Доктор Чарльз Хайсмит (внешность, Известно, Инсайдерские знания, Сюжет, статблок) | 39–40 | `L/character/charles-highsmith` |
| Дополнительная информация от доктора Хайсмита (5 тем; Медицина; Психология −20%) | 40–41 | `L/scene/madman-interview-with-dr-highsmith`: `mechanics`; `L/item/madman-roby-case-file` |
| Освещение убийств Роби в новостях | 42 | `L/scene/madman-news-coverage-of-roby-murders`; `L/handout/madman-handout-5-newspaper-stories` |
| Факты об убийствах Роби (англиканская церковь, похоронное бюро) | 42 | та же сцена; `L/location/madman-st-peters-church`, `L/location/madman-ames-funeral-home`, `L/location/madman-roby-house` |
| Картинки газетных вырезок (копии № 5) | 41–42 | `L/handout/madman-handout-5-newspaper-stories` (картинки — по с. 332–333) |
| Лечебница Святой Агнессы (поездка, Уобли) | 43 | `L/scene/madman-journey-to-st-agnes`; `coc:location:hereford` (новый общий город); `L/location/madman-hereford-environs`; `L/location/madman-weobley` |
| Карта Уобли и приюта | 43 | `L/map/madman-weobley` (`app/maps/tatters-madman-weobley.jpg`, 6 меток) |
| Британские приюты (врезка) | 43–44 | `L/location/madman-st-agnes-asylum`: `description` (последний абзац) |
| Подготовка к интервью с Роби | 44–46 | `L/scene/madman-preparing-for-roby-interview`; `L/location/madman-st-agnes-asylum` (здания, персонал), `madman-asylum-main-building`, `madman-asylum-administration-building`, `madman-highsmith-office` |
| План и фасад приюта Святой Агнессы | 45 | `L/map/madman-st-agnes-asylum` (`app/maps/tatters-madman-st-agnes-asylum.jpg`, 7 меток) |
| Монтегю Эдвардс (сцена в коридоре; внешность, мания, исцеление, Известно, Инсайдерские знания, Описание, статблок) | 46–47 | `L/scene/madman-montague-edwards`; `L/character/montague-edwards` (способность «Исцеление ран») |
| Александр Роби (внешность, Известно, Инсайдерские знания, Описание, статблок) | 47–49 | `L/character/alexander-roby` |
| Состояние души Александра Роби | 49 | `L/character/alexander-roby`: `legend`; `L/scene/madman-interview-with-alexander-roby` |
| Сотворение Каркозы, новое заклинание (врезка) | 49–50 | `coc:spell:build-carcosa` (новая общая запись) |
| Призыв Хастура (врезка; Free Hastur) | 50 | `coc:spell:free-hastur` (новая общая запись; `name.ru` «Освобождение Хастура», напечатанное — псевдоним) |
| Допрос Александра Роби (камера, книги, три речи, песня Кассильды) | 51–53 | `L/scene/madman-interview-with-alexander-roby`; `L/location/madman-roby-cell`; `L/item/madman-graves-book`; `L/handout/madman-handout-6-roby-transcript` |
| Оценка интервью Роби (улики ■) | 53 | `L/scene/madman-interview-with-alexander-roby` (пункты «•») |
| Стенограмма (картинка, копия № 6) | 54 | `L/handout/madman-handout-6-roby-transcript` (картинка — по с. 334) |
| Допрос Эванса | 54–55 | `L/scene/madman-interview-with-evans` |
| Тайна приюта | 55 | `L/scene/madman-asylum-secret`; `L/location/madman-harriwell-cell` |
| Допрос Люциуса Харривелла | 55–56 | `L/scene/madman-interviewing-lucius-harriwell` |
| Люциус Харривелл (внешность, Известно, Инсайдерские знания, Описание, статблок) | 56–57 | `L/character/lucius-harriwell` |
| Полиция Херефорда | 57 | `L/scene/madman-hereford-police`; `L/location/madman-hereford-police-station` |
| Расследование нового убийства | 57–58 | `L/scene/madman-investigating-new-murder` |
| Действия Эдвардса в ту ночь | 58 | `L/scene/madman-edwards-actions-that-night` |
| Видение во сне (врезка) | 58–59 | `L/handout/madman-handout-7-dream-vision` |
| Краткое содержание главы | 59 | `L/scenario/madman`: `summary`, `conclusion` |
| Раздаточный материал № 5 (две вырезки «The Daily E…») | 332–333 | `L/handout/madman-handout-5-newspaper-stories` (текст с картинок, 2 картинки `app/art/handouts/`) |
| Раздаточный материал № 6 (машинописная стенограмма) | 334 | `L/handout/madman-handout-6-roby-transcript` (текст с картинки, картинка `app/art/handouts/`) |
| Раздаточный материал № 7 «Видение во сне» | 335 | `L/handout/madman-handout-7-dream-vision` |

Новые записи: этап 1, персонажи 4, места 14 (общий город `coc:location:hereford` + 13 книжных), карты 2, раздаточные материалы 3,
предметы 2, сцены 12, заклинания 2 (общие). Картинки: `app/maps/tatters-madman-weobley.jpg`,
`app/maps/tatters-madman-st-agnes-asylum.jpg`, `app/art/handouts/madman-handout-5-newspaper-stories.webp`,
`…-5-newspaper-stories-2.webp`, `…-6-roby-transcript.webp`.

## Не взято

- Картинка с. 35 (силуэт города) и титул «Книга I. Безумец» с. 36 — оформление без текста; название главы взято в запись этапа.
- Портреты доктора Хайсмита (с. 39), мистера Эдвардса (с. 46), мистера Роби (с. 48), мистера Харривелла (с. 56) — `app/art/characters/` не входит в файлы части, часть intro портреты тоже не брала; можно добавить потом `pipeline/art/add_images.py`. — сделано (коммит `207f20a`).
- Повторы раздаточных материалов в тексте главы (№ 5 — с. 41–42, № 6 — с. 54) — те же картинки, взяты по приложению H.
- Третий столбец газетных вырезок № 5 и обрывки английского текста на карте с. 43 — неразборчивый английский текст макета оригинала.
- Второстепенные люди без статблоков — медбрат/санитар Прайс, секретарь мистер Ривз, Катберт Йейтс, Фредерик Лонг, суперинтендант Уоллес Рис, Персиваль Хьюм, преподобный Джеймс Брайант, Герберт и Джорджина Роби, Делия Хартстон — остались текстом в сценах и местах (кандидаты в записи персонажей; персонажи без префикса — не файлы этой части). Прайс, Рис, Лонг и Герберт Роби появляются и в главах 2–4. — сделано для Делии Хартстон (запись `character/delia-morrison` части park; ссылка из раздатки № 6 — уборка 2026-11-14, `checks/20261114-tidy.md`).

## Опечатки и сомнения

- Псевдоним Эдвардса: «Марк Эванс» (с. 47, 54, 83), «Майкл Эванс» (с. 9, 59, 110, 123), «Моррис Эванс» (с. 16) — `errata` у `montague-edwards`.
- Роби: ОБР 70 при EDU 15 оригинала (ожидается 75) — `errata`.
- Харривелл: СИЛ 65 (оригинал STR 15 → 75), ЛВК 35 (DEX 06 → 30) — `errata`; «наручники» (с. 55, 56) вместо смирительной рубашки (оригинал straightjacketed; с. 109 — «смирительную рубашку»).
- История болезни: «двухмесячный рецепт» (с. 40) вместо двух трёхмесячных (оригинал) — `errata` у `madman-roby-case-file`.
- Стихи Кассильды «в первой сцене второго акта» (с. 53) — в оригинале Act 1 Scene 2 — `errata` у сцены допроса Роби.
- «Сотворение Каркозы»: проверка «против ВОЛ 70 по таблице сопротивляемости» — правило 6-й редакции; «Призыв Хастура» (Free Hastur): числа 350/180 участников и 50 МОЩ — не пересчитаны под 7-ю редакцию — `errata` в заклинаниях.
- Русское «Нашествие снов» переводит и Send Dreams (Эдвардс), и Dream Vision (Роби, с. 57) — ссылки поставлены по английскому списку; «Призыв Хастура» в списке Эдвардса — Free Hastur, а не Call Hastur.
- «Делия Хартстон» (с. 53, так и в оригинале) — в остальной книге Делия Моррисон; связь поставлена на `delia-morrison`.
- Расстояния: в тексте Уобли в 20 милях (32 км) от Херефорда и границы, на карте «19 miles».

## Ссылки на записи других частей (пока не существуют)

`L/character/malcolm-quarrie` (house), `L/scenario/springer-mound` (springer-flight), `L/scenario/carcosa` (carcosa). — сделано (сведение, коммит `c326b15`).

## Предложения

`checks/20261113-tatters/proposals-madman.json` — 7 псевдонимов общих записей (заклинания send-dream, dream-vision,
bespeak-the-end-of-the-day, call-dismiss-hastur, hands-of-colubra; существа spawn-of-hastur, adherent-of-the-unspeakable-oath).
