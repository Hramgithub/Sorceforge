# «Грань тьмы» («Стартовый набор», `starter-edge-of-darkness-ru`) — сверка переноса (часть edge)

Источник — официальное русское издание «Стартового набора» (книга третья, сценарий второй), скан без текстового слоя:
страницы распознаны `pdftoppm -r 200` + `tesseract -l rus`, каждое число и кубы сверены по изображению страницы
(вырезки строк с числами). Тексты раздаточных материалов «Грань 1»–«Грань 7» сверены с официальными «Наглядными
материалами» Стартового набора (папка владельца `Раздатка\[RU 7e] Зов Ктулху. НРИ. Наглядные материалы (2021).pdf`,
текстовый слой) и с изображениями страниц книги; текст газетной вырезки (часть 5 «Грани 2») — только с изображения с. 27.
Записи — `kb/books/starter-edge-of-darkness-ru/` (Р-217), без пометки «перевод».

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| «Сценарий второй: Грань тьмы» (весь сценарий с раздатками и картой) | 19–47 | 1–29 |
| «Грань тьмы: персонажи и монстры» | 48–49 | 30–31 |

Смещение `starter-edge-of-darkness-ru`: **печатная = физическая + 18** на всех проверенных страницах
(1→19, 2→20, 3→21, 8→26, 15→33, 16→34, 17→35, 18→36, 19→37, 23→41, 30→48, 31→49 — номер на изображении страницы).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Сценарий второй: Грань тьмы (эпиграф — Лавкрафт, «Цвет из иных миров»; 2–5 сыщиков, 1–3 встречи) | 19 | сценарий `starter-edge-of-darkness-ru/scenario/edge-of-darkness` (summary) |
| Подготовка к игре (связь с Мерривезером, вариант с ОИН) | 19 | сценарий: hook; предложение к `starter-paper-chase-ru/organization/society-for-the-exploration-of-the-unexplained` |
| Информация для Хранителя: предыстория | 19 | сценарий: keeper_info; `…/character/rupert-merriweather` |
| Информация для игроков (текст для чтения вслух) | 20 | сцена `…/scene/start`; сценарий: hook |
| Начало | 20 | сцена `…/scene/start`; место `…/location/st-marys-hospital`; `…/character/agnes-merriweather`, `bertrand-merriweather` |
| Страшная тайна | 20 | сцена `…/scene/terrible-secret`; предмет `…/item/metal-box` |
| Хранителю на заметку: почему Мерривезер не исправил содеянное | 21 | сценарий: advice; `rupert-merriweather` (legend) |
| Содержимое ящичка | 21 | сцена `…/scene/box-contents` |
| • Документы и ключ | 21 | предмет `…/item/farm-deed-and-key` |
| • Письмо | 21 | раздатка `…/handout/1-merriweather-letter` |
| • Шкатулка саркофаг | 21 | предмет `…/item/golden-sarcophagus` |
| Материал «Грань 1» | 22 | раздатка `…/handout/1-merriweather-letter` (текст) |
| Хранителю на заметку: символы внутри крышки — ложный след | 23 | `golden-sarcophagus` (mechanics); сценарий: advice |
| Тонкая тетрадь | 23 | предмет `…/item/merriweather-diary`; сцена `box-contents`; организация `…/organization/dark-brotherhood` |
| Материал «Грань 2» (части 1–5, с вырезкой «Жестокое убийство в доках» и списком имён) | 23–27 | раздатка `…/handout/2-merriweather-diary`; персонажи `marion-allen`, `robert-menkin`, `harold-copley`, `crawford-harris`, `cecil-jones` |
| Последняя запись | 26 | `merriweather-diary` (description); `2-merriweather-diary` |
| Дальнейшие шаги (и заметка Хранителю «сразу на ферму») | 26 | сцена `…/scene/next-steps`; сценарий: advice |
| Варианты действий | 26 | сцена `next-steps` |
| Дополнительная мотивация | 28 | сцена `…/scene/additional-motivation`; `agnes-merriweather`, `bertrand-merriweather` |
| Смерть Мариона Аллена (и заметка о личных вещах) | 28 | сцена `…/scene/death-of-marion-allen`; `marion-allen` |
| Иероглифы на золотой шкатулке (напоминание о бонусной кости) | 28 | сцена `…/scene/hieroglyphs`; `…/character/warren-rice` |
| Материал «Грань 3» (часть 1) — показания Кормана и Уоррена | 29 | раздатка `…/handout/3-new-orleans-reports`; `howard-corman`, `harold-warren`, `officer-wood` |
| Материал «Грань 3» (часть 2) — заключение доктора Лоуренса | 30 | `3-new-orleans-reports`; `wilbur-lawrence` |
| Материал «Грань 4» — перевод | 30 | раздатка `…/handout/4-hieroglyph-translation` |
| Визит в библиотеку Орна | 30 | сцена `…/scene/orne-library`; предметы `…/item/reference-book`, `…/item/mu-book`; `…/character/nofru-ka`; место `dveri-vo-tmu-ru/location/ties-orne-library` (предложение) |
| De Vermiis Mysteriis (и заметка об Армитедже) | 31 | сцена `orne-library`; `coc:tome:de-vermiis-mysteriis` (предложение: экземпляр); `pobeg-iz-innsmuta-ru/character/genri-armitedzh` (предложение) |
| Что дальше? | 31 | сцена `…/scene/what-next` |
| Росс-Корнерс | 31 | сцена `…/scene/ross-corners`; места `…/location/ross-corners`, `ross-corners-store`, `boone-road`; `…/character/ma-peters`, `maggie-mcferter` |
| Старая ферма | 32 | сцена `…/scene/old-farm`; места `…/location/farm`, `farmhouse` |
| Вокруг дома | 32 | сцена `old-farm`; места `garden`, `outhouse`, `barn`, `woodshed`, `well`; предмет `…/item/dead-raccoon` |
| Ближайшие окрестности | 32 | сцена `…/scene/maggie-body`; место `…/location/nearby-woods` |
| Амбар | 32 | место `barn`; сцена `old-farm` |
| Карта фермы: «Ферма: первый этаж» (1–7), «погреб» (1–11), «чердак» (1–2), «окрестности» (9 подписей и крест тела) | 33 | карты `…/map/farm` (`app/maps/starter-edge-farm.jpg`, 35 меток: 21 на номерах ключа (на чердаке «1» напечатана дважды), 4 заголовка планов, 9 подписей окрестностей, крест тела) и `…/map/farm-players` (`app/maps/starter-edge-farm-players.jpg`, 34 метки, без креста); раздатка `…/handout/farm-plan`; места `first-floor-1-back-door` … `first-floor-7-stove`, `cellar-1-chairs` … `cellar-11-tarp`, `attic-1-junk`, `attic-2-hatch`; комнаты `living-room`, `back-room`, `cellar`, `attic`; `boone-road`, `dead-tree`, `outhouse`, `woodshed`, `barn`, `farmhouse`, `well`, `swing`, `garden`, `nearby-woods` |
| Информация для Хранителя: история фермы | 34 | `farm` (history); `…/character/bradley-washington`, `sarah-washington` |
| Дом вблизи | 34 | `farmhouse`; `swing`; предмет `…/item/protective-wards`; сцена `old-farm` |
| Гостиная | 35 | место `living-room`; сцена `…/scene/farmhouse-rooms` |
| Задняя комната | 35 | место `back-room`; сцена `farmhouse-rooms`; предмет `…/item/jake-bundle` |
| Рыжий Джейк | 35 | сцена `…/scene/red-jake`; `…/character/red-jake` |
| Если не беспокоить Рыжего Джейка (погоня) | 35–36 | сцена `red-jake` |
| Бой (врезка) | 36 | сцена `…/scene/cellar-ambush` |
| Если сыщики спустились в погреб | 36 | сцена `cellar-ambush`; место `cellar-7-table-leg` |
| Допрос Рыжего Джейка | 36 | сцена `…/scene/jake-interrogation` |
| Что будет с Рыжим Джейком? | 37 | сцена `jake-interrogation`; `…/character/pa-peters` |
| Погреб | 37–38 | место `cellar`; сцена `…/scene/cellar` |
| Сундук | 38 | предметы `…/item/trunk`, `black-robes`; раздатка `…/handout/5-allen-note`; место `cellar-10-trunk` |
| Сигарная коробка | 38 | предметы `…/item/cigar-box`, `brown-powder` |
| Порошок Ибн-Гази (врезка) | 38 | предмет `…/item/ibn-ghazi-powder` (→ `coc:spell:powder-of-ibn-ghazi`) |
| Стопка пожелтевших бумаг (и заметка Хранителю) | 39 | предмет `…/item/allen-papers`; сцена `cellar` |
| Информация для Хранителя: Таящийся на чердаке | 39, 43 | сцена `…/scene/attic-hatch`; существо `…/creature/lurker-in-the-attic`; место `attic-2-hatch` |
| Материал «Грань 5» | 40 | раздатка `…/handout/5-allen-note` |
| Материал «Грань 6» | 41 | раздатка `…/handout/6-latin-chant` |
| Материал «Грань 7» | 41 | раздатка `…/handout/7-chant-translation` |
| Материал «Грань 8» | 42 | раздатка `…/handout/8-pentagram` |
| Хранителю на заметку: разные потери рассудка, гибель сыщика, полиция | 43 | сцена `attic-hatch`; сценарий: advice |
| О Таящемся | 43 | `lurker-in-the-attic` (description, legend); сценарий: keeper_info |
| Особые способности Таящегося | 43 | `lurker-in-the-attic` (abilities) |
| Как изгнать Таящегося (и врезка о пунктах магии) | 44 | сцена `…/scene/ritual`; `allen-papers` (mechanics) |
| Перед началом ритуала | 44 | сцена `…/scene/before-ritual` |
| Ритуал (и заметка о регулировке угрозы) | 44 | сцена `ritual`; сценарий: advice |
| Проведение ритуала | 45–46 | сцена `ritual`; существа `zombie-maggie-mcferter`, `zombie-red-jake`, `zombie-raccoon`, `zombie-bear` |
| Хранителю на заметку: жестокий приём; почему Таящийся не проходит сквозь стену; Вариант (проверки) | 46 | сцена `ritual` (description, mechanics); `protective-wards` |
| Появление Таящегося | 46–47 | сцена `…/scene/lurker-appears` |
| Финал (награды Рассудка) | 47 | сценарий: conclusion |
| Незавершённые дела | 47 | сценарий: conclusion; `…/organization/church-of-contemplation`; `marion-allen`; `golden-sarcophagus` |
| Грань тьмы: персонажи и монстры — Персонажи | 48 | статблоки `rupert-merriweather`, `bertrand-merriweather`, `red-jake` |
| Монстры: Таящийся на чердаке | 48–49 | статблок `lurker-in-the-attic` |
| Ожившие мертвецы: Зомби Мэгги Макфертер, Зомби Рыжий Джейк, Зомби-енот, Зомби-медведь | 49 | существа `…/creature/zombie-maggie-mcferter`, `zombie-red-jake`, `zombie-raccoon`, `zombie-bear` (`instance_of` `coc:creature:zombie`, `spawn_of` Таящегося) |

Готовые сыщики — `startovyy-nabor-ru/character/*` (пять листов набора) в ссылках сценария; сам текст сценария их не называет.

## Предложения правок чужих записей

`checks/20261112-starter-set/proposals-edge.json` — 27 правок в 7 записях (пробный прогон `pipeline/integrate/apply.py --dry-run` проходит):
`coc:location:arkham` (источник, абзац описания, ссылки), `keepers-companion-en/location/arkham-environs` (источник, фраза о
Росс-Корнерс и ферме, ссылки), `dveri-vo-tmu-ru/location/ties-miskatonic-university` (источник, ссылки),
`dveri-vo-tmu-ru/location/ties-orne-library` (источник, абзац о часах работы и закрытом отделе, ссылки),
`pobeg-iz-innsmuta-ru/character/genri-armitedzh` (источник, абзац «В „Грани тьмы“» по Р-125), `coc:tome:de-vermiis-mysteriis`
(экземпляр в `copies`, Р-65), `starter-paper-chase-ru/organization/society-for-the-exploration-of-the-unexplained` (источник,
вариант завязки, ссылки).

## Не взято

- Иллюстрации: «Шкатулка в форме саркофага» (с. 21), «Фермерский дом» (с. 34), «Сыщик сталкивается с Рыжим Джейком» (с. 37),
  «Мэгги Макфертер хочет…» (с. 45) и картинки раздаток (`Грань Тьмы\грань_1.jpg` … `грань_8.jpg`, `грань дом.jpg`,
  `грань шкатулка.jpg`) — поле `images` заполняется через `pipeline/art/add_images.py` в `app/art/`, это вне файлов части;
  кандидаты для ведущего.
- Новый Орлеан (доки Компании Мексиканского залива и Панамы, полиция, «посвящённые из Нового Орлеана») и Бостон (дядя Аллена,
  Церковь Созерцания, лечение Сары Вашингтон) — общих записей городов нет; заводить их ради упоминаний в предыстории и раздатке
  не стали (риск столкнуться с другими частями) — текст в записях, кандидаты в общие города.
- Дядя Мариона Аллена (без имени), род Паркинби-Андерсонов, Компания Мексиканского залива и Панамы, автобусный рейс
  Аркхэм — Вустер, небольшая публичная библиотека Аркхэма — только текст в записях.
- Ритуал изгнания (песнопение, пентаграмма, бурый порошок, 8 пунктов магии) — механика в предмете `allen-papers` и сцене
  `ritual`; общей записи заклинания нет (справочник заклинаний — не файлы части) — кандидат.
- Навыки без механики «Давление на свидетелей», «Мерзкий характер» (Бертран), «Атака кислотой» (Таящийся), «Язык (му)» —
  без записей справочника (Р-126).
- Ссылки на «Книгу вторую» Стартового набора (с. 8, 14, 18, 19, 20) — в тексте как напечатано, ссылки ведут на правила
  «Книги хранителя».

## Сомнения и пометки

- Опечаток с числами не найдено: производные значения всех статблоков сходятся (ПЗ, БкУ, Комплекция, Скорость с возрастом,
  ПМ Таящегося = МОЩ/5).
- Записка Аллена («Грань 5») датирована 23 марта 1877 года, а дневник 26 марта пишет, что Аллен «сегодня утром» вернулся на
  ферму оставить ритуальные принадлежности — так напечатано, отмечено в `5-allen-note`.
- Латынь «Грани 6» — как напечатана («Pontentiam», «Virtum»).
- Зомби Рыжего Джейка (СИЛ 75, ТЕЛ 75) крупнее живого Джейка (СИЛ 50, ТЕЛ 60) — как напечатано, отмечено в записи.
- Мили в тексте сценария («в нескольких милях», «две мили (3,2 км)», «пару миль») переданы километрами (Р-64), пометки — в
  `quality.notes` сцен.
- Церемония 1877 года, вероятно, прошла в задней комнате (камин и кресло в углу) — вывод из текста, помечен в `back-room`.
- Генри Армитедж, Мискатоникский университет и библиотека Орна — записи других книг (`pobeg-iz-innsmuta-ru`, `dveri-vo-tmu-ru`);
  по Р-154 их стоит вынести в общие записи — долг ведущему. ОИН теперь встречается в двух сценариях Стартового набора — тоже
  кандидат в общую организацию.
