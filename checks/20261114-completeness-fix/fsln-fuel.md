# Fear's Sharp Little Needles — часть fsln-fuel: «Whose Fuel is Men and Stones»

Сценарий «Чьё топливо — люди и камни», пропущенный при первом переносе со ссылкой на Р-217 (`checks/20261111-fsln/u2.md`),
найден проверкой полноты (`checks/20261114-completeness/verify-scenarios.md`, строка 12). Решения: Р-220, Р-219, Р-213,
Р-190, Р-206, Р-209, Р-230.

**Формат.** Это обычный сценарий для Хранителя и одного игрока («designed for a Keeper and one investigator»), а не
книга-игра с нумерованными абзацами: запись `scenario` без `solo`, сцены, места, персонажи — как у остальных сценариев
сборника. Р-217 к нему не относится.

**Страницы.** В PDF печатная = физическая − 1 (`pipeline/source/books.json`: offset −1; на физ. 33 напечатано «32»,
на физ. 181 — «180»). «с. N» ниже — печатные. Сценарий занимает с. 28–33 = физ. 29–34 (титул с иллюстрацией — с. 28,
физ. 29). Карта напечатана дважды: в тексте сценария на с. 30 (физ. 31) и в разделе «Maps and Handouts» на с. 180
(**физ. 181**). Задание называло «физ. 30–34 и карту на физ. 180»: физ. 180 — это с. 179, карта «Walter's Final Wish»;
карта этого сценария — физ. 181 (по маркеру `pdf-page-181` в переводе владельца — тоже).

**Источники.** Числа — английский оригинал (текстовый слой; все статблоки сверены по изображениям с. 32–33). Русские
формулировки — рабочий перевод владельца `2_Обработка/fears-sharp-little-needles/document.html` (pdf-page-030–034, 181),
флаг `translated`; отдельного перевода этого сценария в папках владельца нет. Официальные формы: «Ктугха», «Вызов/изгнание
Ктугхи», «Сглаз», «Плавление плоти» (записи базы; у владельца «Ктхугха», «Призыв Ктхугхи»); «Живое Пламя Глубочайшей
Тьмы», «ифрит», «Чьё топливо — люди и камни» — по реестру терминов.

Все записи — в `kb/books/fears-sharp-little-needles-en/` с id `fears-sharp-little-needles-en/<kind>/fuel-<slug>`; ниже —
`<kind>/fuel-<slug>`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул «Whose Fuel is Men and Stones» (автор Jason Williams; метки Psychological Thriller, For One Player, Paranoia, Mysticism) | 28 | `scenario/fuel-whose-fuel-is-men-and-stones` (summary); иллюстрация не перенесена (Р-241) |
| Эпиграф (Коран, 2:24) | 29 | `scenario/…` (keeper_info) |
| Introduction | 29 | `scenario/…` (keeper_info); `organization/fuel-jaleel-cell`; `character/fuel-jaleel`, `-haytham`, `-isis-recruiter` |
| Involving the Investigator | 29 | `scenario/…` (hook, keeper_info); `location/fuel-investigator-hotel` |
| Track Marks (врезка) | 29 | `scenario/…` (advice), refs `scenario/spilsbury`, `scenario/lights-out`, `creature/lights-out-ifrit`; `scene/fuel-week-in-london`; `creature/fuel-living-flame-of-deepest-black` (legend) |
| Information for the Keeper | 29 | `scenario/…` (advice, keeper_info); `scene/fuel-week-in-london` |
| Description of Area Surrounding Paddington Station | 29, 31 | `location/fuel-paddington` (район), `location/fuel-paddington-station`, `-paddington-underground`, `-st-marys-hospital` (495 коек), `-paddington-basin`, `-little-venice` |
| Карта «Paddington, the basin, & little venice» (в тексте) | 30 | `map/fuel-paddington` (та же карта, что на с. 180) |
| Strange Occurrences — are they imagined, dreams, or twisted realitys? (врезка, 7 пунктов) | 31 | `scenario/…` → `tables` «Странные происшествия» (7 строк с потерей Рассудка); `scene/fuel-week-in-london` (mechanics) |
| Setting Up the Investigator | 31–32 | `scene/fuel-arrival`, `scene/fuel-recruiter-suspicions`, `scene/fuel-capture`; `item/fuel-recruiter-phone-laptop`; `character/fuel-isis-recruiter` |
| Способы захвата (три пункта) | 32 | `scene/fuel-capture` |
| The Summoning | 32 | `scene/fuel-summoning`; `location/fuel-raghad`; `item/fuel-sacrificial-dagger`, `item/fuel-iron-nail`; `coc:spell:call-dismiss-cthugha` |
| Rewards and Repercussions | 32 | `scenario/…` (conclusion, шаг «Развязка»), `scene/fuel-summoning` (outcome) |
| JALEEL, Mystic/Wizard and Cult Leader | 32–33 | `character/fuel-jaleel`; `tome/fuel-jaleel-scrolls`; `location/fuel-camden-market`, `location/fuel-raghad` (Raghad) |
| HAYTHAM, Apprentice Cultist | 33 | `character/fuel-haytham` |
| NAZIM (Male) or KHAWLAH (Female) Abdelaziz, ISIS Recruiter | 33 | `character/fuel-isis-recruiter` (основной статблок + `variants` Назим / Хаула) |
| LIVING FLAME OF DEEPEST BLACK, Avatar of Cthugha | 33 | `creature/fuel-living-flame-of-deepest-black` (avatar_of `coc:creature:cthugha`) |
| Карта «Whose Fuel is Man and Stones Map» | 180 | `map/fuel-paddington` (37 меток; картинка `app/maps/fsln-fuel-paddington.jpg`, снята с с. 180) |

Метки карты: каждая надпись получила метку. Свои записи: Little Venice, Paddington Basin, St. Mary's Hospital, Paddington
Station, Paddington Underground, Paddington Green Police Station, план узкой лодки (11 подписей: Bow, Lounge, Galley, Master
Bedroom, Bathroom, Study, Closet, 2nd Bedroom, Cockpit, Stern, Tiller → `location/fuel-raghad` с пояснением). Остальные
подписи (заголовок карты, Novotel Paddington, Microsoft, Vodafone, VISA, Sheldon Square, Kingfisher, The Prince of Wales Pub,
Hilton Paddington, Hotel Mercure Paddington, Hilton Metropole, City of Westminster College Paddington, Cet Primary School,
Merchant Square, Imperial College London St. Mary's, Tesco, Hope Montessori Primary School, Westway, Edgware Road ×2) —
метки с пояснением на `location/fuel-paddington`: в тексте сценария они не участвуют. Метки проверены по наложению на
картинку.

Итого 26 записей: сценарий 1, сцены 5, персонажи 3, существо 1, организация 1, предметы 3, книга 1, места 10, карта 1.

## Не взято

- Иллюстрация титула (с. 28) — атмосферная, не переносится (Р-241).
- Легенда цветов карты (8 категорий) и масштабные линейки (0–250 и 0–5 футов) — меток не получили (не места); перечислены
  в `quality.notes` карты.
- Сам сыщик и покойный благодетель — без записей: книга не даёт ни имени, ни статблока (сыщик — персонаж игрока).
- Сообщник вербовщика и нанятые «местные» с фургоном (способы захвата) — только текстом в сцене «Захват»: безымянные,
  без статблока.
- ИГИЛ как организация — без записи: реальная организация, в сценарии только фон (вербовщик, надежды Джалила); текстом в
  записях персонажей и ячейки.
- Видеокамера вербовщика — текстом в сцене «Призыв» и у лодки (её выбрасывают за борт), без записи предмета.
- Музей, собор/церковное кладбище, историческая табличка о Великом пожаре из «Странных происшествий» — книга их не называет;
  остаются текстом строк таблицы (сцена — на общем месте Лондон).
- Заголовки «Separation» / «Anxiety» в текстовом слое с. 29 — мусор колонтитула соседнего сценария, не заголовки.

## Опечатки и сомнения

- `character/fuel-isis-recruiter`: у Назима СИЛ 65 + ТЕЛ 60 = 125 → бонус к урону +1d4, Комплекция 1; напечатано «none»
  и 0 (у Хаулы верно) — в `errata`, как напечатано. «Skills: Skills:» — повтор в книге.
- `creature/fuel-living-flame-of-deepest-black`: СИЛ 225 + ТЕЛ 225 = 450 → +6d6 и Комплекция 7; напечатано +5D6 и 6
  (согласованы между собой, подходят к 365–444) — большинства нет (Р-36), в `errata`, как напечатано.
- `character/fuel-jaleel`: Скорость 3 при расчётной 4 (7 − 3 за возраст 72) — книга поясняет «полуинвалид»; намеренно
  (Р-76), в `errata`.
- Книга пишет, что вокзал Паддингтон — «in the City of London» (на деле — Вестминстер); оставлено как в книге, пометка в
  `quality.notes` вокзала.
- В колонтитуле с. 33 и в подписи карты название — «Whose Fuel is **Man** and Stones» — псевдоним сценария.
- Что ритуальная лодка за больницей — это «Рагхад» Джалила, книга прямо не говорит (вербовщик называет её лодкой
  родственника); запись лодки одна, вывод помечен (Р-41).
- Полицейский участок Паддингтон-Грин есть только на карте; связь с полицией сцен — «возможно, отсюда» (Р-41, Р-156).
- Тесак Хайтама (1d8+БкУ) сослан на «Нож большой» по урону, хотя в справочнике тесак назван у «Ножа среднего» (1d4+2).
- Свитки Джалила — запись книги Мифов без чисел чтения (`incomplete`): книга их не даёт.
- Записи других частей называют сценарий «соло-приключением» и «не переносится (Р-217)» (`scenario/spilsbury`,
  `scenario/lights-out`, `creature/lights-out-ifrit`, `scenario/awto`, `scenario/focus-group`) — исправления в
  предложениях. В `checks/20261111-fsln/u2.md` (и u3, u9) та же пометка — не запись, не правлю.

## Предложения (`proposals-fsln-fuel.json`, 11 правок, пробный прогон проходит)

- `scenario/spilsbury`: текст связи «Track Marks» — «сценарий для одного игрока «Чьё топливо — люди и камни»», убрать
  «(Соло-приключение в базу не переносится, Р-217.)», ссылка на новый сценарий.
- `scenario/lights-out`, `creature/lights-out-ifrit`: «соло-приключение» → «сценарий для одного игрока «Чьё топливо — люди
  и камни»»; ссылка на сценарий у «Свет погас».
- `scenario/awto`, `scenario/focus-group`: в `quality.notes` «считая соло «Whose Fuel…»» → «считая «Чьё топливо — люди и
  камни»».
- `coc:spell:call-dismiss-cthugha`: псевдонимы «Summon Ifrit», «Призвать ифрита» (с. 32).
- `coc:location:london`: ссылка на сценарий.

Новых заклинаний нет: «Summon Ifrit (Call Cthugha)», «Evil Eye», «Melt Flesh» — записи справочника.
