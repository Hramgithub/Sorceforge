# «Одно небольшое дельце…» (`odno-nebolshoe-deltse-ru`) — сверка переноса (часть affair)

Источник — русский сценарий Кирилла Семакова, написанный для конкурса коротких приключений Hobby Games (PDF с
текстовым слоем, 12 страниц); редакция — 7-я, ядро (не Pulp). Эпоха в книге прямо не названа: 1920-е — по умолчанию
(Р-04) и по каталогу владельца (на это же указывают «относительно недавняя» Испано-американская война и ссылки на
«Книгу хранителя» для транспорта). Город — Бостон (общая запись `coc:location:boston` уже есть; дополнения —
предложениями). Числа статблоков, карта и открытка сверены по изображениям страниц (150–300 dpi).
Записи — `kb/books/odno-nebolshoe-deltse-ru/` (Р-222), без пометки «перевод».

## Страницы

Смещение: **печатная = физическая − 1** (номера внизу страниц: физ. 2 → «1», физ. 7 → «6», физ. 12 → «11»).
Физ. с. 1 (обложка) номера не несёт. В `pipeline/source/books.json` смещение пока не записано — его ставит ведущий.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка (3–5 игроков, конкурс Hobby Games, автор) | физ. 1 | сценарий `…/scenario/odno-nebolshoe-deltse` (summary, sources) |
| Описание | физ. 1 | сценарий: summary |
| Содержание | 1 | не взято (оглавление) |
| Вступление | 2 | сценарий: keeper_info, advice (создание персонажей, желательные навыки); `…/character/michael-green` (legend); `…/organization/kachaho-servants`; `…/creature/kachaho` (legend) |
| Предложение | 2 | сцена `…/scene/offer`; `…/character/thomas-harris`; место `…/location/hinkle-lake-road-bar`; `…/item/delivery-address-card`; `…/item/obsidian-sarcophagus`; сценарий: hook |
| Подготовка — Автомобиль | 2–3 | сцена `…/scene/vehicle` (со ссылкой на `coc:rule:vehicle-reference-charts`, «Книга хранителя», с. 414) |
| Библиотека и городской архив | 3 | сцена `…/scene/library-archive`; место `…/location/city-library-archive`; `…/item/museum-blueprints`, `…/item/conquistador-chronicle`; `…/character/rafael-araya`; место `…/location/museum-basement-tunnel` |
| Музей | 3 | сцена `…/scene/museum-visit`; места `…/location/boston-museum`, `museum-back-yard`, `museum-war-hall`, `museum-exhibition-hall`; `…/item/araya-saber`; `…/character/diego-araya` |
| Устройство на работу | 3–4 | сцена `…/scene/job-interview`; `…/character/brian-paterson`; место `…/location/museum-manager-office`; `…/item/employment-contract` |
| Аптека | 4 | сцена `…/scene/pharmacy`; место `…/location/miller-pharmacy`; `…/character/leonard-miller` |
| Ночь ограбления — Вход через подвал | 4 | сцена `…/scene/basement-entry`; места `miller-pharmacy`, `museum-basement-tunnel` |
| Вход через задний двор | 4 | сцена `…/scene/backyard-entry`; место `museum-back-yard`; `…/character/museum-guards` |
| Работа в охране | 4–5 | сцена `…/scene/guard-shift`; `…/character/douglas-parker`, `…/character/andrew`, `museum-guards`; место `…/location/museum-guard-room` |
| Внутри музея | 5 | сцена `…/scene/inside-museum`; `…/creature/soldier-mannequins`; `araya-saber`; `museum-manager-office` |
| Выставочный зал (и бой) | 5–6 | сцена `…/scene/exhibition-hall`; место `museum-exhibition-hall`; `kachaho`, `michael-green`, `…/character/green-assistants`, `thomas-harris`; `…/item/obsidian-knives`, `obsidian-sarcophagus`; `kachaho-servants` |
| Финал (и награды Рассудка) | 6 | сцена `…/scene/finale`; сценарий: conclusion (награды — пункты «•»); `…/character/boston-police` |
| Персонажи хранителя: Брайан Патерсон | 7 | `…/character/brian-paterson` (statblock) |
| Дуглас Паркер | 7 | `…/character/douglas-parker` (statblock) |
| Майкл Грин | 7 | `…/character/michael-green` (statblock) |
| Леонард Миллер | 7 | `…/character/leonard-miller` (statblock) |
| Охранник | 8 | `…/character/museum-guards` (групповой профиль, придуманные имена) |
| Ассистент | 8 | `…/character/green-assistants` (групповой профиль; Томас Харрис — `instance_of`) |
| Полицейский | 8 | `…/character/boston-police` (групповой профиль) |
| Существа: Манекен | 8 | `…/creature/soldier-mannequins` |
| Качахо | 8–9 | `…/creature/kachaho` (`instance_of` `coc:creature:mummy`; взор, переселение, щупальце теней — способности) |
| Предметы: Сабля Арайи | 9 | `…/item/araya-saber` |
| Раздаточные материалы: Материал 1. Открытка с приглашением | 10 | `…/handout/affair-1-postcard` (рукописный текст переписан с изображения) |
| Материал 2. Карта музея | 11 | карта `…/map/boston-museum` (`app/maps/affair-museum.jpg`, 6 меток); `…/handout/affair-2-museum-map` |

## Записи (47)

- сценарий 1: `odno-nebolshoe-deltse`;
- сцены 12: `offer`, `vehicle`, `library-archive`, `museum-visit`, `job-interview`, `pharmacy`, `basement-entry`,
  `backyard-entry`, `guard-shift`, `inside-museum`, `exhibition-hall`, `finale`;
- персонажи 11: 4 с параметрами (Патерсон, Паркер, Грин, Миллер), 3 групповых профиля (охранники, ассистенты,
  полицейские), 4 без параметров (Томас Харрис, Эндрю, Рафаэль Арайя, Диего Арайя);
- существа 2: `kachaho`, `soldier-mannequins`;
- места 10 (в Бостоне): музей и 6 его частей (выставочный зал, зал Испано-американской войны, кабинет управляющего,
  помещение охраны, задний двор, тайный тоннель), аптека Миллера, библиотека и городской архив, бар на Хинкл Лэйк Роад;
- предметы 7, раздатки 2, организация 1, карта 1.

## Предложения

`proposals-affair.json` — 9 (пробный прогон `apply.py --dry-run` проходит): Бостон — источник, абзац описания и
5 ссылок; `source_variants` у `coc:weapon:bayonet` (штык манекена 1d8 + 1 + БкУ) и `coc:weapon:sword-heavy`
(сабля Арайи 1d8 + 2 + БкУ).

## Опечатки и сомнения

- ПЗ не сходятся с (ВЫН + ТЕЛ) / 10 у Патерсона (16 вместо 13), Грина (14 вместо 11), Миллера (7 вместо 9),
  охранников (10 вместо 8), полицейских (14 вместо 8), манекена (12 вместо 10), Качахо (20 вместо 14); ПМ Качахо 15
  вместо 17 — как напечатано, в `errata`.
- Скорость: Патерсон 6 (по правилам 7, с возрастом 5), Миллер 6 (8 / 5), охранники 8 (9) — как напечатано, в `errata`;
  манекены 6 (у человека с такими числами — 8) — пометка в записи.
- Охрана ночью: Паркер говорит, что сам сидит в помещении охраны, а «ещё один человек» — в комнате отдыха; текст после
  речи — «двое находятся в комнате охраны» (с. 4–5): `errata` у сцены `guard-shift`.
- Оружие без модели: револьвер Паркера и полицейских (1d10 + 2) привязан к «Револьвер .45», кинжал из обсидиана
  (1d4) — к «Нож маленький», штык манекена — к «Штык (примкнутый)» (урон другой) — вывод из текста (Р-41).
- Адрес бара на рукописной открытке читается как «Хинкл Лэйк Роад, 235»; «Хинкл» — неуверенно.
- У Качахо не напечатаны бонус к урону, НАР, ОБР и проценты атак (атаки идут проверками МОЩ, Рассудка, ВЫН).
- Связи, которые книга подразумевает, но прямо не называет (вывод из текста, Р-41): аптекарь сцен = Леонард Миллер
  и живёт над аптекой; «Крадущийся во мраке» = Качахо; сабля в музее = благословлённая сабля Рафаэля Арайи.

## Не взято

- Содержание (с. 1) — оглавление, не данные для игры.
- Фирменный текст обложки (ссылка на hobbygames.ru, Fan Material Policy Chaosium) — не данные для игры.
- Картинка открытки (материал 1): изображения раздаток идут в `app/art/` через `pipeline/art/add_images.py` — эта
  папка не входит в мою часть; кандидат для владельца — физ. с. 11 (вся страница — открытка с видом улицы).
- Безымянные люди без статблоков и сюжетных линий (бармен, охранник у двери днём, случайный свидетель угона,
  переводчик с испанского) — текстом сцен, без своих записей.
- Захоронение инков, где Грин нашёл саркофаг, и адрес доставки на карточке — в книге не названы, остаются текстом.
