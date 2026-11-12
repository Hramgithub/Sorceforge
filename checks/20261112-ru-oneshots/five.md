# «Омерзительная пятёрка» (`omerzitelnaya-pyaterka-ru`) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] Омерзительная 5ятерка.pdf`, 11 страниц; неофициальный русский сценарий для 7-й редакции (Алексей Старк,
вёрстка — Валерий Титков; NiceTableGame, Dungeons and bartender). Текстовый слой надёжен; числа статблоков и
исторической справки сверены по изображениям страниц 6–8 (150 dpi). Текст на картинках, которого нет в текстовом слое,
переписан по изображениям: «Заметка для мастера!» (физ. с. 3) и открытка «Маленький секрет Харриса» (физ. с. 5, 250 dpi).
Карт в книге нет. Действие — поздняя зима 1867 года, Вайоминг: `axes.era` = `wild-west` (первое употребление в базе),
`ruleset` = `core`.

**Страницы:** печатная = физическая − 2 (номер «~ 1 ~» внизу физ. с. 3 … «~ 9 ~» на физ. с. 11; обложка физ. с. 1 и
титул физ. с. 2 без номера). В записях `printed_page` стоит по этому правилу, у физ. с. 1–2 — `null`; `offset` в
`books.json` не записан — ставит ведущий.

Префикс записей книги: `omerzitelnaya-pyaterka-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница (печ. / физ.) | Где в базе |
|---|---|---|
| Обложка «Ом5рзительная пятерка» | — / 1 | `scenario/omerzitelnaya-pyaterka` (sources, aliases) |
| Титул: «Неофициальный сценарий…», для 2–4 сыщиков, 1–2 сессии, аннотация, авторы | — / 2 | `scenario/omerzitelnaya-pyaterka` (summary) |
| От автора | — / 2 | `scenario/omerzitelnaya-pyaterka` (advice) |
| Как же работает это приключение? | — / 2 | `scenario/omerzitelnaya-pyaterka` (advice); порядок исключения — `character/charlz-keyn`, `character/ronni-khill` (legend) |
| Предыстория | 1 / 3 | `scenario/omerzitelnaya-pyaterka` (keeper_info); `creature/parazit`, `character/richard-gudmen`, `character/eshli-gudmen`, `character/dzho-danston`; `location/oblomki-korablya` |
| Персонажи игроков: Гарри Янг (Имущество, Характер/Особенности, Отношения) | 1 / 3 | `character/garri-yang` (pregen); связи с `ronni-khill`, `rubi-danston`; `character/tomas-duglas` |
| Заметка для мастера! (Стрельба (револьвер) не ниже 65; перестрелка вероятна) | 1 / 3 | `scenario/omerzitelnaya-pyaterka` (advice); прегены (quality.notes — лист) |
| Ронни Хилл (Майор Ронни Хилл): Имущество, Характер, Отношения, врезки, настоящая история | 2 / 4 | `character/ronni-khill` (background, secret, legend); `item/dokument-o-medali-za-otvagu`; `character/dzhonatan-kharris` |
| Дополнительная информация (Ронни: Гудмены, Эри) | 2 / 4 | `character/ronni-khill` (legend); `character/richard-gudmen`, `character/eshli-gudmen`, `character/erik-uotson`; `location/galantereya-gudmena` (табличка) |
| Начало сценария для Ронни Хилла | 2 / 4 | `character/ronni-khill` (legend, possessions — три трупа); `scene/dilizhans` |
| Фред Харрис (шериф): Имущество, врезка о дроби, Характер | 3 / 5 | `character/fred-kharris`; `item/dokumenty-o-naznachenii-sherifa` |
| Маленький секрет Харриса (открытка) | 3 / 5 | `handout/malenkiy-sekret-kharrisa`; `organization/danstonskie-ublyudki`; `character/fred-kharris` (background.secret) |
| Отношения (Фред: Гарри, Ронни, Чарльз, Руби, Джо и остальные) | 3 / 5 | `character/fred-kharris` (legend, relations); `character/dzho-danston`, `character/rubi-danston` |
| Дополнительная информация (Фред), врезка о суде на месте | 3 / 5 | `character/fred-kharris` (legend); `character/dzhonatan-kharris` |
| Начало сценария для Фреда Хариса | 3 / 5 | `character/fred-kharris` (legend); `scene/galantereya-gudmena` |
| Чарльз Кейн (палач): Имущество, Характер, Отношения, Дополнительная информация | 4 / 6 | `character/charlz-keyn`; `item/pismo-o-naznachenii-palacha`; `coc:location:red-rock` |
| Начало сценария для Чарльза Кейна | 4 / 6 | `character/charlz-keyn` (legend); `location/tualet` |
| Историческая справка: битва при Чаттануге | 4 / 6 | `scenario/omerzitelnaya-pyaterka` (advice, числа целиком) |
| Персонажи мастера: Паразит (и три тезиса о паразитах) | 5 / 7 | `creature/parazit` (abilities, legend); `location/podpol-saraya`; `item/kapsuly-s-parazitami` |
| Врезка «Подконтрольные паразитам люди…» | 5 / 7 | `scene/galantereya-gudmena`; `character/pancho-vilya`, `character/mark-gilmor`, `character/erik-uotson` |
| Панчо Вилья, представившийся Карлосом Веларде (статблок, имущество, навыки, врезка «амиго») | 5 / 7 | `character/pancho-vilya`; `scenario/…` (advice) |
| Марк Гилмор, который представился как Джонас Брукс | 5 / 7 | `character/mark-gilmor` |
| Ричард Гудмен (под управлением паразита) | 5 / 7 | `character/richard-gudmen` |
| Томас Дуглас (врезка о камине) | 6 / 8 | `character/tomas-duglas` |
| Руби Данстон («Знает, что её спасут») | 6 / 8 | `character/rubi-danston` |
| Трупы: Эшли Гудмен и дочери Эмма и Бриджит | 6 / 8 | `character/eshli-gudmen`, `character/emma-gudmen`, `character/bridzhit-gudmen`; `location/saray` |
| Трупы: Джо Данстон | 6 / 8 | `character/dzho-danston`; `location/podval-galanterei` |
| Глава I: «Дилижанс» | 6 / 8 | `scene/dilizhans`; `location/okrestnosti-red-roka` |
| Глава II: «Галантерея Гудмена» | 7 / 9 | `scene/galantereya-gudmena` |
| Локация: Галантерея | 7 / 9 | `location/galantereya-gudmena` |
| Подвал Галантереи | 7 / 9 | `location/podval-galanterei` |
| Конюшни (сценка с Карлосом) | 7 / 9 | `location/konyushni`; `character/pancho-vilya` |
| Туалет | 7 / 9 | `location/tualet` |
| Сарай (тела, подпол, капсулы) | 8 / 10 | `location/saray`, `location/podpol-saraya`; `item/kapsuly-s-parazitami` |
| Глава III «У Гудмена есть секрет» (подталкивания) | 8 / 10 | `scene/u-gudmena-est-sekret` |
| Вставка «что же было в галантерее сегодня утром» | 8 / 10 | `scene/utro-v-galanteree` |
| Оглушение Карлосом, «кратко расскажите» игроку, «Вербовка» | 8 / 10 | `scene/oglushenie-v-sarae`; `handout/zapiska-oglushennomu-igroku`; `creature/parazit` (abilities) |
| Врезка «Как только произошёл момент раскрытия…» | 9 / 11 | `scene/u-gudmena-est-sekret` |
| Глава IV: «Кукловоды» (паразиты, Руби, Томас) | 9 / 11 | `scene/kuklovody`; `creature/parazit`, `character/rubi-danston`, `character/tomas-duglas` |
| Финалы: 1. Паразиты погибли; 2. Паразиты выжили (эпилог о корабле, Зона 51) | 9 / 11 | `scene/kuklovody`; `scenario/omerzitelnaya-pyaterka` (conclusion); `location/oblomki-korablya`; `organization/danstonskie-ublyudki` |
| Заключительное слово автора («тарантиновская атмосфера…») | 9 / 11 | `scenario/omerzitelnaya-pyaterka` (summary, conclusion) |

Город: Рэд-Рок — новая общая запись `coc:location:red-rock` (Р-190; в базе его не было, другие части плана там не
играют); действие — в его окрестностях: область `location/okrestnosti-red-roka` (Р-209, привязка к Рэд-Року — вывод
из текста, Р-41) → `location/galantereya-gudmena` → подвал, конюшни, туалет, сарай → подпол; `location/oblomki-korablya`.

## Опечатки и противоречия книги (в `errata`)

- `character/pancho-vilya`: СИЛ 50 + ТЕЛ 40 = 90 → БкУ −1, Комплекция −1; напечатаны 0 и 0 (обе согласованы, оставлены как напечатано).
- `character/dzhonatan-kharris`: отец Фреда — «командующий кавалерийского полка» (с. 3) и «один из командующих южного артиллерийского полка» (с. 4).
- `location/saray`: ссылка «см. Персонажи мастера, стр. 5» — раздел «Трупы» на с. 6.

Без `errata` (не важно ведущему или не опечатка): «Мистер Гаррия Янг» (с. 1), «Начало сценария для Фреда Хариса» (с. 3) —
словесные опечатки имён; урон дробью у револьвера Ле Ма напечатан «1d8/d10» — оставлен как напечатано. «Предыстория»
говорит, что Джо и его люди приехали «дилижансом», а в конюшнях стоят 3 лошади бандитов — книга, по-видимому, называет
так приезд; оставлено как есть.

## Не взято

- Иллюстрации (обложка, горы Вайоминга с подписью «Прекрасные заснеженные горы Вайоминга скоро станут красными от
  пролитой крови», дилижансы, битва, паразит, дом, комната с телами, рисунок существа) — картинки без игровых данных;
  `app/art/` не входит в файлы этой части. Подпись к картинке гор — атмосферная фраза без данных.
- Логотипы NiceTableGame и Dungeons and bartender и уведомление о Политике Chaosium для фанатских материалов (с. 2) —
  выходные данные; названия команд — в `summary` сценария.
- Три трупа разыскиваемых у Ронни Хилла (Ричард Долл, Виллис Браун, Энди Уоллес; 3, 5 и 5 тыс.), предыдущий шериф
  Рэд-Рока, лагерь банды, Ричмонд, Зона 51 — упоминания без описания: оставлены текстом в записях
  (`ronni-khill`, `danstonskie-ublyudki`, `okrestnosti-red-roka`, `oblomki-korablya`), отдельных записей нет.
- Оружие персонажей (винтовка Спенсер на 7 патронов, револьвер Ремингтон на 6 патронов, револьвер Ле Ма на 9 патронов +
  заряд дроби, Кольт Арми с 6-зарядным барабаном, охотничий нож) — в справочнике оружия нет моделей 1860-х; оружие
  записано в `possessions` как напечатано, атаки револьвером у НПС собраны из навыка и урона «Имущества» без ссылки
  `weapon`. Кандидаты в новые записи справочника — в отчёте.
- Потери Рассудка и награды: в книге их нет (у НПС Рассудок «-/-»).
