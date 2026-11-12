# «Pax Cthuliana» (pax-cthuliana-ru) — сверка заголовков

Книга: Ярле Хакторсон, Эвен В. Россланд, Two Starving Gnolls / NEVR, 2017; русский перевод MADCROWDE (в `books.json` —
`official` по метке файла «[RU 7e]», фактически фанатский перевод). 72 страницы, печатная страница = физической
(смещение 0). Действие — Лондон, 1927 год (с. 5); каталог владельца («2020», «современность») с книгой расходится.
Сценарий системно-нейтральный (с. 7): статблоков и чисел Рассудка нет, `ruleset` — core, эпоха — 1920s.
Страницы без текстового слоя (1–2, 5, 8–9, 12, 14–15, 17, 19–21, 24, 26, 28–32, 34, 36, 38–45, 47–50, 55–67)
распознаны tesseract и сверены по изображениям; раздатки переписаны по изображениям.

Префикс записей: `pax-cthuliana-ru/…`; сценарий — `scenario/pax-cthuliana`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул, выходные данные | 1, 3–4 | `scenario/pax-cthuliana` (summary, sources) |
| Оглавление | 2 | `scenario/pax-cthuliana` (sources) |
| Что такое Pax Cthuliana? | 5 | `scenario/pax-cthuliana` (summary, advice) |
| Эпиграф Лавкрафта | 6 | не взято (см. ниже) |
| Предисловие, часть 1: Практическая информация (использование термина «Персонаж», количество игроков, знание Мифов, игровая система, секретность, Г. Ф. Лавкрафт) | 7 | `scenario/pax-cthuliana` (advice, keeper_info, quality) |
| Предисловие, часть 2: Сценарий — Сюжет вкратце | 8 | `scenario/pax-cthuliana` (summary) |
| Вступление («Прелюдия») | 8 | `scene/prelyudiya` |
| Расширенные сцены | 9 | `scenario/pax-cthuliana` (advice); расширенные сцены — в своих сценах |
| Головоломка/Сигил | 9 | `item/golovolomka-sigil`, `scenario/pax-cthuliana` (keeper_info) |
| Собор Святого Павла | 9–10 | `scenario/pax-cthuliana` (keeper_info), `character/kristofer-ren`, `location/krysha-sobora-svyatogo-pavla`; предложение к `masks…/england-st-pauls-cathedral` |
| Использование музыки | 10–11 | `scenario/pax-cthuliana` (keeper_info, таблица «Музыка») |
| Предисловие, часть 3: Ктулху в Лондоне? | 12–13 | `scenario/pax-cthuliana` (keeper_info, таблица «Как Ктулху оказался в Лондоне») |
| Прелюдия; Несколько заключительных слов о проведении «Прелюдии» | 14–15 | `scene/prelyudiya` |
| Прелюдия: Содержание и Временные рамки | 16 | `scene/prelyudiya` (по отсчётам трека) |
| После «Прелюдии»: музыка, выбор игрока, Джон Доу | 17 | `scene/prelyudiya`, `scene/igra-nachinaetsya`, `character/dzhon-dou` |
| Вступительная сцена 1 — Игра начинается | 18–19 | `scene/igra-nachinaetsya`, `handout/material-1-zapiska-berglou`, `character/alfi-terner` |
| Вступительная сцена 2 — Ханвеллская лечебница | 19–22 | `scene/khanvellskaya-lechebnitsa`, `location/khanvellskaya-lechebnitsa`, `character/sven-berglou`, `character/dzhordzh-uebb`, `character/dzhon-dou`, `handout/zapiska-iz-kurtki-dzhona-dou` |
| Расширенная сцена (адрес Джона Доу) | 22 | `scene/khanvellskaya-lechebnitsa` |
| Вступительная сцена 3 — Квартира | 23–25 | `scene/kvartira`, `location/pab-dva-golodayushchikh-gnolla`, `location/kvartira-dzhona-dou`, таблица сценария «Улики из квартиры Джона Доу», `handout/material-2…10` |
| Расширенная сцена: Трудности с входом | 23 | `scene/kvartira`, `location/pab-dva-golodayushchikh-gnolla` |
| Что произойдет дальше?; Одно исключение: Собор Святого Павла | 25 | `scene/kvartira` |
| Расширенная сцена «Улики» | 25 | `scene/kvartira` |
| Ключевая сцена 1 — Британский музей (Зал Римской Британии, «Некрономикон») | 26–28 | `scene/britanskiy-muzey`, `location/zal-rimskoy-britanii`, `location/otdel-rukopisey`, `location/zapretnaya-sektsiya`, `character/benedikt-saymon`, `character/edmund-kheyl`, `item/kultovyy-predmet-dionisa`, `handout/material-11-simvol-stranitsy-48`; экземпляр — предложение к `coc:tome:necronomicon-english` |
| Расширенная сцена (часть Сигила); Расширенная сцена («Некрономикон») | 28 | `location/zal-rimskoy-britanii`, `location/zapretnaya-sektsiya`, `scene/britanskiy-muzey` |
| План «British Museum — Upper Floor» | 29 | `map/britanskiy-muzey-verkhniy-etazh` (`app/maps/pax-britanskiy-muzey-verkhniy-etazh.jpg`, 39 меток) |
| Ключевая сцена 2 — Лондонский музей науки (+ расширенная сцена) | 30–31 | `scene/muzey-nauki`, `location/muzey-nauki`, `character/per-stalbi`, `item/zvezdnaya-mashina`, `item/zvezdnaya-karta-rena` |
| Ключевая сцена 3 — Витас Варнас | 32–33 | `scene/vitas-varnas`, `location/igla-kleopatry`, `character/vitas-varnas`, `handout/material-12-faksimile-nadpisey` |
| Сцена персонажа 1 — Дж. Р. Р. Толкин (Университет, Музеи, Другие места, Британский музей/Британская библиотека, расширенная сцена) | 34–35 | `scene/tolkin`, `character/dzh-r-r-tolkin`, `character/albert-pirs` |
| Сцена персонажа 2 — Алистер Кроули | 36–37 | `scene/alister-krouli`, `character/alister-krouli`, `character/vinyar-gronstoel`, `location/chernyy-khram`, `location/belyy-khram`, `location/belyy-khram-gostinaya`, `location/belyy-khram-tronnyy-zal` |
| Вариант 1: Дружественный вариант; Вариант 2: Вариант дружественной магики | 37 | `scene/alister-krouli` |
| Вариант 3: Ужасный и враждебный подход без боя | 38 | `scene/alister-krouli`, `location/belyy-khram-komnata-za-tronom`, `character/eda-mortimer` |
| Вариант 4: Ужасный и враждебный подход с боем | 39 | `scene/alister-krouli`, `character/alister-krouli` (errata «Кулак Йига») |
| Улики (Материалы № 13–23) | 39 | `item/bumagi-krouli`, таблица сценария «Улики из дома Кроули», `handout/materialy-13-17…`, `material-18…23` |
| Сцена персонажа 3 — Меган «Ангел» Шнайдер | 40–41 | `scene/megan-shnayder`, `character/megan-shnayder`, `location/dom-megan-shnayder` |
| Сюжетная сцена 1 — Заклинание | 42–43 | `scene/zaklinanie`, `location/ritualnaya-komnata-megan`, `handout/material-25-dva-simvola` |
| Сюжетная сцена 2 — Гробница; Крыша; Гробница Кристофера Рена | 44–47 | `scene/grobnitsa`, `location/krysha-sobora-svyatogo-pavla`, `location/grobnitsa-kristofera-rena`, `character/lars-lund`, `character/frederik-kollinz`, `handout/material-26…`; экземпляр «Аль-Азифа» — предложение к `coc:tome:al-azif` |
| Расширенная сцена — усиленный патруль | 47 | `scene/grobnitsa`, `character/okhrana-sobora` |
| Сюжетная сцена 3 — Конец(цы) (Меган Шнайдер, Музей науки, Снова Меган, Крыша около часа ночи, 1:00) | 48–50 | `scene/kontsy`, `item/pometka-rena` |
| Обычная, Случайная, Неверная концовки, Искажённый финал, Концовка Рена | 51 | таблица сценария «Концовки», `scenario/pax-cthuliana` (conclusion) |
| Заключительный раздел 1 — Факты и вымысел: Собор Святого Павла, Сэр Кристофер Рен, Ханвеллская лечебница, Квартира Джона Доу в пабе, Британский музей | 52 | в описаниях `character/kristofer-ren`, `location/khanvellskaya-lechebnitsa`, `location/pab-dva-golodayushchikh-gnolla`; собор и музей — предложения к записям «Масок» |
| Лондонский музей науки, Игла Клеопатры, Дж. Р. Р. Толкин, Название города Лондон, Алистер Кроули, Материал № 6, Материал № 21, «Что означает название» | 53 | `location/muzey-nauki`, `location/igla-kleopatry`, `character/dzh-r-r-tolkin`, `character/alister-krouli`, `scene/tolkin`, `handout/material-6…`, `handout/material-21…`, `scenario/pax-cthuliana` (aliases «Ктулхуанский мир») |
| Заключительный раздел 2 — Раздаточные материалы № 1–26 | 54–65 | `handout/material-1…26` (22 записи; № 13–17 — одна запись), № 7 — также карта `map/karta-londona-material-7` (`app/maps/pax-karta-londona-material-7.jpg`, 30 меток) |
| Головоломка «Сигил» | 66 | `item/golovolomka-sigil` |
| Заключительный раздел 3 — Список участников, О создателях (TSG) | 68–70 | прообразы персонажей — в легендах (`sven-berglou`, `per-stalbi`, `vinyar-gronstoel`, `benedikt-saymon`, `vitas-varnas`, `lars-lund`, `megan-shnayder`, `golovolomka-sigil`); остальное не взято |

## Не взято

- Эпиграф Лавкрафта (с. 6), иллюстрации без подписей (с. 1, 47, 67 и др.), «Посетите Two Starving Gnolls…» (с. 71), пустая с. 72 — без содержания для игры.
- Список спонсоров Kickstarter (с. 68–69) и «О создателях» (с. 70) — не материал сценария; авторы и переводчик — в `sources`/summary сценария.
- Мимоходом упомянутые без роли в игре: Джон Ди, Карл II, Рамсес II, профессор из Йоркшира (предыстория Меган), профессор-лингвист университета (расширенная сцена Толкина) — текстом в записях, без своих записей.
- «Книга Азатота» (с. 27) — только упоминание в запретной секции («не пригодится»), текстом в `location/zapretnaya-sektsiya`; в общем справочнике такой книги нет.
- Заклинание Меган «Прорицание» и заклинание восстановления Сигила — без механики в книге; черновики — в отчёте помощника, ссылок нет. «Кулак Йига» — без ссылки (errata у Кроули).
- Подписи улиц и мелкие курсивные подписи станций метро на карте-раздатке № 7, масштаб и стрелка на плане музея — без меток (см. `quality.notes` карт).

## Опечатки и расхождения книги

- с. 26: все части головоломки — «во время „Сюжетной Сцены 2“»; на с. 9, 10, 43 — «Сюжетная сцена 3» (`scenario` errata).
- с. 45, 48 — финал «в полночь»; с. 49–50 — «в час ночи» (`scenario`, `scene/kontsy` errata).
- с. 23 — раздать «Материалы № 2-9», а список улик (с. 24) включает № 10 и кусок Сигила (`scene/kvartira` errata).
- с. 24 — Толкин описан в «Сцене персонажа 2»; на деле — «Сцена персонажа 1» (`handout/material-9-tolkin` errata).
- с. 28 — Меган живёт в Найтсбридже; с. 40 — Кенсингтон, Холланд-Парк, 41 (`character/megan-shnayder` errata).
- с. 36 «Гронстоэль» / с. 68 «Гронстол» (`character/vinyar-gronstoel` errata).
- с. 39 «Кулак Йига» (Fist of Yig) — вероятно, «Кулак Йог-Сотота» (`character/alister-krouli` errata).
- с. 53 «В 1877/1888 годах» — вероятно, 1877/1878 (`location/igla-kleopatry` errata).
- с. 68: Пер Сталби назван в «Ключевой сцене 1» (он во 2-й) — список спонсоров не переносился.

## Технический долг

- Британский музей, собор Святого Павла и Гайд-парк — записи книги «Маски Ньярлатхотепа», теперь встретились во второй книге: по Р-154 их стоит перевести в общие `coc:location:*` (решение ведущего). Пока места «Pax Cthuliana» ссылаются на них через `part_of`, дополнения — в `proposals-pax.json`.
