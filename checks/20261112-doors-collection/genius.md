# «Гений места» («Двери во тьму», `dveri-vo-tmu-ru`) — сверка переноса (часть genius)

Источник — официальное русское издание «Двери во тьму» (скан без текстового слоя): страницы распознаны
`pdftoppm -r 200` + `tesseract -l rus`, каждое число сверено по изображению страницы; рукописные раздатки («Гений 1»,
«Гений 5») прочитаны по изображению. Английский оригинал `doors-to-darkness-en` — для сверки чисел и английских
названий (Р-213, Р-216).

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 3 «Гений места» (Брайан Куртманш) | 35–55 | 34–54 |
| «Материалы для игроков»: «Гений 1» … «Гений 6» | 113–118 | 112–117 |
| «Готовые персонажи» (десять сыщиков сборника) | 126–135 | 125–134 |

Смещение: печатная = физическая + 1 (проверено по колонтитулам с. 37–55; раздатки с. 113–118 — по порядку страниц и смещению).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 3. Гений места (Брайан Куртманш; эпиграф Ширли Джексон) | 35 | сценарий `dveri-vo-tmu-ru/scenario/genius-loci` (summary) |
| Введение | 35 | сценарий: summary; город `coc:location:danvers` |
| Информация для Хранителя | 35 | сценарий: keeper_info; `…/location/genius-hathorne-hill`, `…/location/genius-danvers-asylum`; `…/creature/genius-lloigor`; `…/character/genius-john-hathorne`, `genius-william-shine`, `genius-james-berger`; `…/item/genius-elder-sign-disk`; `…/organization/genius-lloigor-thralls` |
| Хранителю на заметку: как вовлечь сыщиков (врезка) | 36 | сценарий: advice; `genius-larry-croswell` (legend) |
| Вовлечение сыщиков | 36 | сцена `…/scene/genius-letters`; сценарий: hook; `…/character/genius-larry-croswell` |
| Истинная история Данверской психбольницы (врезка) | 36 | `…/location/genius-danvers-asylum` (history); сценарий: advice (фильм) |
| Материал «Гений 1» (в главе) | 37 | `…/handout/genius-1-croswell-letter` |
| Материал «Гений 2» (в главе) | 38 | `…/handout/genius-2-asylum-letter` |
| Визит в Данверскую психбольницу (эпиграф Э. По) | 39–41 | сцена `…/scene/genius-visiting-asylum`; места `genius-danvers-asylum`, `genius-asylum-main-building`, `genius-ward-10`, `genius-reservoir`, `genius-amphitheater`; персонажи `genius-james-berger`, `genius-staff-nurses`, `genius-orderlies`, `genius-patients` |
| Хранителю на заметку: это место сводит меня с ума (врезка) | 40 | сценарий: advice |
| Карта 1. Окрестности Данверской больницы | 40 | карта `…/map/genius-map-1-environs` (`app/maps/dveri-genius-map-1.jpg`, 13 меток на подписи); область `…/location/genius-danvers-environs` |
| Хранителю на заметку: за вами следят! (врезка) | 41 | сценарий: advice; сцена `genius-lloigor-takes-notice`; `genius-lloigor` (legend) |
| Ллойгор обращает внимание | 41–42 | сцена `…/scene/genius-lloigor-takes-notice`; таблица сценария «Ллойгор обращает внимание» (6 строк) |
| Сбор и изучение сведений | 42 | сцены `genius-research-asylum` … `genius-research-hathorne` |
| О Данверской психбольнице | 42–43 | сцена `…/scene/genius-research-asylum`; таблица сценария «Зацепки о Данверской психбольнице» (5 строк); места `genius-peabody-institute-library`, `genius-phillips-library`, `genius-danvers-historical-society`, `genius-danvers-town-hall`, `genius-danvers-herald`, `genius-salem-news`; `…/character/genius-warren-herrick`; город `coc:location:salem` |
| Материал «Гений 3» (в главе) | 43 | `…/handout/genius-3-amphitheater-article`; `genius-elder-sign-disk` |
| О докторе Шайне | 43 | сцена `…/scene/genius-research-shine`; `genius-william-shine` |
| Материал «Гений 4» (в главе) | 44 | `…/handout/genius-4-shine-retires` |
| Документы Шайна в Салемской больнице | 44 | сцена `genius-research-shine`; `…/location/genius-salem-hospital`; `…/item/genius-shine-papers` |
| О докторе Бергере | 44 | сцена `…/scene/genius-research-berger`; `genius-james-berger` (legend) |
| О судье Джоне Хаторне | 44–45 | сцена `…/scene/genius-research-hathorne`; `genius-john-hathorne`; `genius-hathorne-hill` |
| Нежелательное внимание (эпиграф Ницше) | 45, 48 | сцена `…/scene/genius-unwanted-attention`; таблицы сценария «Нежелательное внимание: запугивание» (2 строки) и «Покушения ллойгора издали» (5 строк); `genius-orderlies` |
| Хранителю на заметку: выходы из тупика (врезка) | 45 | сценарий: advice |
| Материал «Гений 5» (в главе) | 46–47 | `…/handout/genius-5-shine-diary` |
| Визит Эндрю Макбрайда | 48 | сцена `…/scene/genius-macbride-visit`; `…/character/genius-andrew-macbride` |
| Вытащить Ларри Крозвелла | 48–49 | сцена `…/scene/genius-busting-out`; `genius-danvers-asylum` (забор, двери) |
| Ночь новолуния (эпиграф «Девятая сессия») | 49–52 | сцена `…/scene/genius-dark-of-the-moon`; `genius-amphitheater`, `genius-reservoir`; `genius-lloigor`; `genius-lloigor-thralls` |
| Материал «Гений 6» (в главе) | 49 | `…/handout/genius-6-macbride-death` |
| Карта 2. Амфитеатр на холме Хаторна | 50 | карта `…/map/genius-map-2-amphitheater` (`app/maps/dveri-genius-map-2.jpg`, 16 меток на подписи); места `genius-ward-8`, `genius-ward-9`, `genius-ward-10`, `genius-asylum-main-building`, `genius-amphitheater`, `genius-reservoir` |
| Итоги | 52 | сценарий: conclusion; шаг «Итоги и награды» |
| Награды | 52 | сценарий: conclusion (шесть наград Рассудка) |
| Приложение А. Персонажи Хранителя и чудовища | 52 | — |
| Лоуренс «Ларри» Крозвелл, 52 года, писатель, узник психбольницы | 52 | `…/character/genius-larry-croswell` (статблок) |
| Доктор Джеймс Бергер, 39 лет, одержимый главврач больницы | 53 | `…/character/genius-james-berger` (статблок) |
| Эндрю Макбрайд, 56 лет, пациент психбольницы | 53 | `…/character/genius-andrew-macbride` (статблок) |
| Медсестра больницы, рабыня ллойгора | 53 | `…/character/genius-staff-nurses` (групповой профиль, имена) |
| Врач больницы, раб ллойгора | 53 | `…/character/genius-staff-physicians` (групповой профиль, имена) |
| Санитар больницы, раб ллойгора | 53 | `…/character/genius-orderlies` (групповой профиль, имена) |
| Пациент больницы | 53 | `…/character/genius-patients` (групповой профиль, имена) |
| Ллойгор, пирующий под водой (особые умения, броня, заклинания, потеря рассудка) | 55 | `…/creature/genius-lloigor` (`instance_of` `coc:creature:lloigor`; 4 способности; «Зародить страх», «Усыхание конечности») |
| Материалы для игроков: «Гений 1» | 113 | `genius-1-croswell-letter` (источник) |
| «Гений 2» | 114 | `genius-2-asylum-letter` (источник) |
| «Гений 3», «Гений 4» | 115 | `genius-3-amphitheater-article`, `genius-4-shine-retires` (источник) |
| «Гений 5» | 116–117 | `genius-5-shine-diary` (источник) |
| «Гений 6» | 118 | `genius-6-macbride-death` (источник) |
| Готовые персонажи (десять сыщиков) | 126–135 | существующие записи `dveri-vo-tmu-ru/character/<slug>` — в ссылках сценария (не дублировались) |

`…/` = `dveri-vo-tmu-ru/`.

## Записи (53 + 2 города)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `genius-loci` (4 таблицы, 12 шагов) |
| scene | 11 | `genius-letters`, `-visiting-asylum`, `-lloigor-takes-notice`, `-research-asylum`, `-research-shine`, `-research-berger`, `-research-hathorne`, `-unwanted-attention`, `-macbride-visit`, `-busting-out`, `-dark-of-the-moon` |
| location | 19 | общие города `coc:location:danvers`, `coc:location:salem` (новые, Р-190); книги: `genius-danvers-environs`, `-hathorne-hill`, `-danvers-asylum`, `-asylum-main-building`, `-ward-8`, `-ward-9`, `-ward-10`, `-amphitheater`, `-reservoir`, `-asylum-cemetery`, `-peabody-institute-library`, `-danvers-historical-society`, `-danvers-town-hall`, `-danvers-herald`, `-phillips-library`, `-salem-hospital`, `-salem-news` |
| map | 2 | `genius-map-1-environs`, `genius-map-2-amphitheater` |
| character | 10 | со статблоком: `genius-larry-croswell`, `-james-berger`, `-andrew-macbride`; групповые профили: `-staff-nurses`, `-staff-physicians`, `-orderlies`, `-patients`; без статблока: `-william-shine`, `-john-hathorne`, `-warren-herrick` |
| creature | 1 | `genius-lloigor` |
| item | 2 | `genius-elder-sign-disk`, `genius-shine-papers` |
| handout | 6 | `genius-1-croswell-letter` … `genius-6-macbride-death` |
| organization | 1 | `genius-lloigor-thralls` (название наше, `editorial_text`) |

Картинки карт: `app/maps/dveri-genius-map-1.jpg` (1183×806), `app/maps/dveri-genius-map-2.jpg` (1154×864) — вырезки
из страниц 40 и 50 (200 dpi); метки проверены глазами по вырезкам с нанесёнными кружками.

## Расхождения изданий и опечатки

- Год постройки больницы: 1878 (врезка, с. 36) и 1876 (зацепка, с. 42); так и в оригинале. `errata` у
  `genius-danvers-asylum`.
- Зона вихря ллойгора: «в радиусе 10 метров» / «в пределах 10 метров» (с. 50, 52) и «участок диаметром 10 метров»
  (с. 55); так и в оригинале (ten-meter radius / within ten yards / 10 yards (10 meters) in diameter). `errata` у сцены
  `genius-dark-of-the-moon`.
- Производные значения (Р-161), как в оригинале: Крозвелл — Скорость 8 (по характеристикам 7, с возрастом 5);
  Бергер — Уклонение 30% при ЛВК 70; санитары — ПМ 9 при МОЩ 35. `errata` в записях, значения как напечатано.
- Ллойгор: БкУ +5d6 и Комплекция 6 при СИЛ + ТЕЛ 450 (по таблице — +4d6 и 5) — так и в Malleus Monstrorum
  (общая запись); оставлено, пометка в `quality.notes`. Профиль сценария отличается от общего вида: ЛВК 50,
  Ближний бой 40%, Уклонение 20%, ПМ 200*, навыков нет.
- Корпуса русского издания 8, 9, 10 и камера 10-12 — H Ward, I Ward, J Ward и J-12 оригинала.
- Масштабы карт: русское издание — 0–0,5–1–1,5 км и 0–30–60–90 метров; оригинал — 0–½–1 миля и 0–100–200–300 футов.
- Расстояние до Бостона: «примерно 30 километров» (оригинал — eighteen miles).
- Хаторн: в оригинале «approximately two dozen» (с. 42) и «nearly twenty» (с. 44) осуждённых; в русском издании оба
  раза «два десятка».
- Словесная опечатка русского издания «лечиться от вздумал» (с. 52, вместо «он») — не записывалась (Р-39).

## Не взято

- Иллюстрации: с. 39 — фото Данверской больницы («из Библиотеки конгресса»); с. 42 — «Рисунок жабы» (худ. Пэт
  Лобойко); с. 51 — «Зверская вакханалия» (на всю страницу); с. 54 — «Появление ллойгора» (на всю страницу) — картинки
  в записи не добавлялись (поле `images` необязательно; можно добавить позже `pipeline/art/add_images.py`).
- Эпиграфы (Ширли Джексон, Э. По, Ницше, «Девятая сессия») — оформление глав, не перенесены.
- Подписи карты 1 без своих записей (станции Хоу, Больница, Бивер-Брук; ж/д линия Салем — Лоуренс; холмы Путнем и
  Випл; Путнемвилль; речки Ипсвич, Фрост-фиш-брук, Бивер-Брук) — метки ведут на `genius-danvers-environs`, названия
  перечислены в её описании. Подписи карты 2 «Лужайка», «Дорога», «Дороги», «Дорога по периметру», «Насыпь», «Лес»,
  «Каталка с Крозвеллом», «Ллойгор», «Путь процессии» — метки с `text` на запись больницы, холма, озера или амфитеатра.
- Данверская полиция, Государственная психиатрическая лечебница Остина (Техас) — упомянуты мимоходом, текстом в сценах
  и у персонажей, записей нет.
- Безымянные эпизодические фигуры (дежурная сестра без пол-уха, здоровенный пациент, шпион-сотрудник, болтливый
  библиотекарь/служащий/журналист, простоватый незнакомец) — текстом в сценах и групповых профилях.
- Картина «Святой Георгий и дракон» и фото Шайна с Бергером в кабинете — текстом в описании главного здания и сцене
  визита, отдельных предметов нет. Факелы с солями меди и каталка — текстом в сцене «Ночь новолуния».
- Алфавитный указатель книги — служебный.

## Кандидаты и вопросы

- `coc:location:salem` заведён как общий город (по Р-190), хотя в сценарии в Салеме только три места исследования;
  если владелец предпочитает держать такие места в «Окрестностях Данверса» — перенести.
- Атака дубинкой санитаров (1d4 + 1d4) не связана с оружием: у «Дубинки полицейской» таблицы урон 1d6; можно
  предложить `source_variants` для `coc:weapon:club-small`.

## Предложения

`proposals-genius.json` — 2 предложения: `coc:location:arkham` — ссылки на новые города `coc:location:danvers` и
`coc:location:salem` (без `corrections`). Пробный прогон `pipeline/integrate/apply.py --dry-run`: 2 правки ложатся.
