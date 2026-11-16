# Stage Fright at the Playhouse (`stage-fright-en`) — сверка переноса

Сценарий John Hedge with The Playhouse Staff, Miskatonic Repository, v2 (2024-12-01). Часть `stagefright` — вся книга.
Записи — `kb/books/stage-fright-en/` (69): сценарий 1, сцены 20, персонажи 18 (из них готовые сыщики 5), места 17,
предметы 7, раздатки 6, книга Мифов 1, карта 1. Русский текст — наш перевод (Р-251, Р-21).

Страницы: PDF — 39 физических страниц; печатная = физическая − 4 (с. 1 = физ. 5, с. 33 = физ. 37); обложка (физ. 1),
аннотация (физ. 2), выходные данные (физ. 3), оглавление (физ. 4), реклама подкаста (физ. 38) и афиши (физ. 39) без
номеров. Смещение для `books.json`: **offset = −4**.

## Заголовки книги → записи базы

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (аннотация, выходные данные) | физ. 2–3 | `scenario/stage-fright` (summary, sources) |
| Table of Contents; Content Warnings | физ. 4 | `scenario/stage-fright` (summary: предупреждения; advice: инструменты безопасности) |
| Introduction | 1 | `scene/introduction`; `scenario/stage-fright` (summary) |
| Keeper note: SEU | 1 | `scene/introduction`, `scenario` hook; ОИН — общая запись (предложение) |
| Preparing for Play | 1 | `scene/introduction`, `scenario` hook |
| Keeper Information | 2 | `scenario` keeper_info |
| Table Stage-01: timeline of events | 2 | `scenario` tables «Хронология событий» |
| Involving the Investigators | 3 | `scene/introduction` |
| Alternative Hook: An Academic Request | 3 | `scene/academic-request`; `character/julius-van-der-hoff`; Уоррен Райс — общая запись (предложение) |
| Dramatis Personae: Edward Kleverstein | 4 | `character/edward-kleverstein` |
| Genevieve ‘Ginny’ Dubois | 4 | `character/ginny-dubois` |
| Franc Turner | 5 | `character/franc-turner` |
| Hannah Carter | 5 | `character/hannah-carter` |
| Iain Smith | 6 | `character/iain-smith` |
| Xander Turner | 6 | `character/xander-turner` |
| Minor NPCs: Diane Loring, Henry Armitage, Karen Jeffries | 6 | `character/diane-loring`, `character/karen-jeffries`; Армитедж — общая запись (вариант статблока — предложение) |
| START: Avenues of Research | 7 | `scenario` steps 2–3 |
| Orne Library (Miskatonic University) | 7 | `scene/orne-library`; `scenario` tables «Поиски в библиотеке Орна»; место — `coc:location:orne-library` |
| Keeper note (импровизация) | 7 | `scene/orne-library`, `scenario` advice |
| Handout Stage-1 / Stage-2 (копии в главе) | 8 | `handout/stage-1-playhouse-photograph`, `handout/stage-2-newspaper-article` |
| The Arkham Advertiser | 9 | `scene/arkham-advertiser`; место — `coc:location:arkham-advertiser` |
| The Archives | 9 | `scene/arkham-advertiser`; `scenario` tables «Поиски в архиве «Адвертайзера»»; `item/advertiser-1813`, `item/day-labour-advert` |
| The Playhouse | 10 | `scene/outside-playhouse`; театр — `innsmouth-terror-en/location/miskatonic-playhouse` (адрес, история — предложения) |
| Outside the Playhouse | 10 | `scene/outside-playhouse`, `location/playhouse-entrance`, `handout/stage-3-carvings` |
| Keeper note (символы вырезаны неправильно) | 10 | `location/playhouse-entrance`, `scene/outside-playhouse`, `scenario` keeper_info |
| The Alley | 11 | `scene/alley`, `location/playhouse-alley`, `item/xander-effects` |
| The Lobby | 11 | `scene/lobby`, `location/playhouse-lobby` |
| Kleverstein’s office (+ Keeper note о западной двери) | 12 | `scene/kleverstein-office`, `location/kleverstein-office`, `item/kleverstein-notepad`, `handout/stage-4-notepad` |
| Backstage (+ список слухов) | 13 | `scene/backstage`, `location/backstage` (таблица «Слухи за кулисами»), `location/hannah-office`, `character/production-crew`, `item/spare-keys` |
| False Walls | 13 | `scene/backstage`, `location/backstage-staircase` |
| Dressing Rooms (+ Keeper note об «иннсмутской внешности») | 14–15 | `scene/dressing-rooms`, `location/dressing-rooms`, `location/ginny-dressing-room`, `item/insurance-policies`, `item/ginny-photographs`, `handout/stage-5-map` |
| Following Iain Smith; Good Cop; Bad Cop | 15 | `scene/following-iain-smith`, `location/iain-smith-office` |
| Evening in the Playhouse (+ Keeper note о драматичном моменте) | 16 | `scene/evening-in-the-playhouse`, `scenario` advice |
| Searching with Franc | 16 | `scene/searching-with-franc` |
| Repairing the Elevator | 16 | `scene/repairing-the-elevator`, `location/goods-elevator` |
| Breaking In | 16 | `scene/evening-in-the-playhouse` |
| Map Stage-1: the prop room | 17 | `map/prop-room` (`app/maps/stagefright-prop-room.jpg`; метки на все 8 подписей + 2 вычисленные) |
| Prop Room | 17 | `scene/prop-room`, `location/prop-room` и его части: `goods-elevator`, `backstage-staircase`, `secret-staircase`, `hidden-room`, `electronics-storage`, `cleaning-cupboard`, `pyrotechnics-storage` |
| The Pickering Diary (сцена) | 18 | `scene/pickering-diary-room`, `location/hidden-room` |
| The Pickering Diary (врезка книги) | 18 | `tome/pickering-diary` |
| Handout Stage-6 (спираль в главе) | 18 | `handout/stage-6-pickering-diary` |
| The Climax | 19 | `scene/climax-xander` (вступление), `scenario` advice |
| Xander the Servitor | 19 | `scene/climax-xander`, `character/xander-turner` |
| Ginny Dubois (кульминация) + Keeper note о заклинаниях | 19 | `scene/climax-ginny` |
| Edward Kleverstein (кульминация) | 19 | `scene/climax-kleverstein` |
| Conclusion | 20 | `scene/conclusion`, `scenario` conclusion |
| The Fate of the Playhouse | 20 | `scene/conclusion`, `scenario` conclusion |
| Rewards | 20 | `scenario` conclusion (награды Рассудка, ссылки на правила) |
| Continuing the Campaign | 20 | `scenario` conclusion |
| Characters and Monsters: Arkham Residents | 21 | `character/diane-loring`, `character/karen-jeffries`; Армитедж — предложение (вариант) |
| Playhouse Staff | 21–22 | `character/edward-kleverstein`, `ginny-dubois`, `franc-turner`, `hannah-carter`, `iain-smith` |
| Monster: Xander Turner | 22 | `character/xander-turner` (instance_of `coc:creature:zombie`) |
| Pre-generated Investigators: Clara Windu | 23 | `character/clara-windu` |
| Hugo ‘Shrimpy’ Hargreaves | 24 | `character/hugo-hargreaves` |
| Patty Gillian | 25 | `character/patty-gillian` |
| Luis Carlos Andriani | 26 | `character/luis-carlos-andriani` |
| Margaret ‘Maggie’ Myers | 27 | `character/margaret-myers` |
| Handouts: Stage-1…Stage-6 | 28–33 | `handout/stage-1-…` … `handout/stage-6-…` (картинки — из приложения) |
| Miskatonic Playhouse (реклама подкаста) | физ. 38 | не взято — реклама |

## Не взято

- Реклама подкаста Miskatonic Playhouse (физ. 38) и афиши других сценариев (физ. 39) — не материал сценария; записаны в `atmosphere.json`.
- Логотипы выходных данных, украшения страниц, атмосферные фото (зрительный зал, гримёрная Джинни, закулисье, сцена, египетская шкатулка, «древний мёртвый язык») — `atmosphere.json`; портрет Армитеджа (с. 7) — у общей записи свой портрет.
- Продолжение статьи о кражах в текстовом слое PDF под обрезом полосы (с. 29) — на странице не видно, в текст раздатки не взято; пересказ — в `quality.notes` раздатки.
- Версия «print-friendly», названная в аннотации, — в этом PDF её нет.
- Две сотрудницы «Адвертайзера» — отдельной записи нет, описаны в сцене `scene/arkham-advertiser`.
- Египетская шкатулка из «Грани тьмы» — отдельной записи в базе нет (кандидат в предмет «Стартового набора»); упоминается текстом.

## Опечатки и противоречия книги

| Где | Напечатано | Что в базе |
|---|---|---|
| Срок пропажи Ксандера | «three weeks ago» (с. 2) против «about two months ago» (с. 5) и «2 months ago» (хронология) | два месяца; `errata` у Франка |
| Возраст Иэна Смита | 30 (с. 6), 25 (с. 22), «mid-to-late 40s» (с. 14) | 30; `errata` у Иэна и сцены |
| Статья раздатки Stage-2 | «Autumn of 1927» при действии осенью 1923 | как напечатано; `errata` раздатки |
| Клеверштейн: Скорость | 6 (ожид. 8) | как напечатано, `errata` |
| Джинни: ПЗ / БкУ / Скорость | 9 / 0 / 7 (ожид. 10 / +1d4, Комплекция 1 / 9) | как напечатано, `errata` |
| Ханна: ПЗ / Скорость | 11 / 7 (ожид. 12 / 9) | как напечатано, `errata` |
| Иэн: БкУ / ПМ | 0 / 12 (ожид. +1d4 / 18) | как напечатано, `errata` |
| Карен Джеффрис: БкУ | 0, урон драки «1D3+1D4» (ожид. +1d4, Комплекция 1) | как напечатано, `errata` |
| Диана Лоринг: Скорость | 7 (с поправкой за 50 лет — 6) | как напечатано, `errata` |
| Армитедж: Скорость | 6 (с поправкой за 70 лет — 3) | в предложении варианта (reason) |
| Луис Андриани: БкУ | 0 (ожид. +1d4, Комплекция 1) | как напечатано, `errata` |
| Пэтти: английский | 67% (32/13) | 67% (33/13), `errata` fixed (Р-35, Р-77) |
| Мэгги: Работа в библиотеке | 75% (35/14) | 75% (37/15), `errata` fixed; возможна опечатка 70% (Р-77) |
| ВЫН «6o» (Джинни, Франк, Иэн, Ксандер, Карен) | буква «o» вместо нуля | 60, молча (Р-39) |
| «janiter» (с. 5–6), «brian» (с. 4), «Arkaham» (с. 13), «Massachucetts» (с. 2) | словесные опечатки | исчезают в переводе (Р-39) |
| Раздатка 4 | «notepad» в тексте, «notebook» в подписи | название — «блокнот», оба в `aliases`/заметках |

## Термины книги (English → Russian)

| English | Русский |
|---|---|
| Stage Fright at the Playhouse | Испуг на сцене (как уже в базе) |
| Miskatonic Playhouse | Мискатоникский театр (как уже в базе) |
| playhouse | театр |
| Prop Room / props room | склад реквизита |
| Backstage | закулисье |
| Lobby | фойе |
| Dressing Rooms / dressing room | гримёрные / гримёрная |
| Goods elevator / Goods Lift | грузовой лифт |
| False Walls | фальшивые стены |
| Secret Entrance / secret staircase | тайная лестница |
| the hidden room | тайная комната |
| Old Cleaning Supplies / cleaning cupboard | старая кладовая уборщика |
| Pyrotechnics (room) | кладовая пиротехники |
| Electronics (room) | кладовая электрооборудования |
| Scenery / Large Props / Small Props | декорации / крупный реквизит / мелкий реквизит |
| Orchestra pit; producers box | оркестровая яма; ложа продюсера |
| Producer / Executive Producer | продюсер / исполнительный продюсер |
| Stage Manager | заведующая постановочной частью |
| Production Crew | постановочная бригада |
| janitor / cleaner | уборщик |
| day labour(ers) | подёнщики |
| starlet / leading lady | старлетка / ведущая актриса |
| The Pickering Diary | дневник Пикеринга |
| Lord Alexander Pickering-Carter | лорд Александр Пикеринг-Картер |
| Edward Kleverstein | Эдвард Клеверштейн |
| Genevieve ‘Ginny’ Dubois | Женевьева «Джинни» Дюбуа (как уже в базе) |
| Franc / Xander Turner | Франк / Ксандер Тёрнер |
| Hannah Carter | Ханна Картер |
| Iain Smith | Иэн Смит |
| Diane Loring; Karen Jeffries | Диана Лоринг; Карен Джеффрис (как уже в базе) |
| Julius Van der Hoff | Джулиус ван дер Хофф |
| Clara Windu; Luis Carlos Andriani | Клара Винду; Луис Карлос Андриани |
| Hugo ‘Shrimpy’ Hargreaves; Patty Gillian; Margaret ‘Maggie’ Myers | Хьюго «Шримпи» Харгривз; Пэтти Гиллиан; Маргарет «Мэгги» Майерс (как уже в базе) |
| Xander the Servitor | Ксандер-служитель |
| Servitors of Azathoth | служители Азатота |
| Song of the Servitors | Песнь служителей |
| Claw-like nails / Clawed feet | когтистые ногти / когтистые лапы |
| the Innsmouth look | иннсмутская внешность |
| Good Cop / Bad Cop | добрый полицейский / злой полицейский |
| Society for the Exploration of the Unexplained (SEU) | Общество исследователей необъяснимого (ОИН) — как уже в базе |
| Women in Bronze | «Женщины в бронзе» |
| Survival (Library) | Выживание (библиотека) |
| Art/Craft (Dewey Decimal System) | Искусство/ремесло (десятичная классификация Дьюи) |
| Language (Mu) | Иностранный язык (язык Му) |
| Handout Stage-N | раздатка «Сцена-N» |
| Map Stage-1: the prop room | план склада реквизита |

Официальные формы из глоссария: Dominate — «Покорение», Shrivelling — «Иссушение», Breath of the Deep — «Дыхание глубин»,
Warding — «Оберег», Words of Power — «Слова власти», Summon/Bind Servitor of the Outer Gods — «Призыв/укрощение служителя
Внешних богов», Deep One hybrid — «гибрид глубоководного», Hard/Extreme success — «трудный/чрезвычайный успех»,
Self Help — «Самолечение», Mythos Rating — «Значение Мифов», Law — «Юриспруденция», Track — «Чтение следов».

## Связи с другими книгами (Р-154 — кандидаты в общие записи)

- `same_as` на записи «Ужаса в Иннсмуте» (`innsmouth-terror-en`): Франк Тёрнер, Джинни Дюбуа, Диана Лоринг, Карен Джеффрис,
  Хьюго Харгривз, Пэтти Гиллиан, Маргарет Майерс — по Р-154 их стоит вынести в общие `coc:character:*`.
- Мискатоникский театр — запись `innsmouth-terror-en/location/miskatonic-playhouse`; места этой книги стоят `part_of` неё;
  по Р-154 — кандидат в общую `coc:location:arkham-miskatonic-playhouse` (адрес Марш-стрит, 552 — вероятно, район Даунтаун).
- Предложения (`proposals-stagefright.json`, 22): Армитедж — вариант статблока и источник; Уоррен Райс — источник и абзац
  описания; ОИН — 5 членов, источник, ссылка на сценарий; театр — адрес, история, источник, 8 ссылок.
