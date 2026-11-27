# HOTOE — часть «campaign»: книга I (с. 1–9, 11–14, 41–58, 73–74), книга IV (с. 169–179), реквизит

Источники: `hotoe-book-1-en`, `hotoe-book-4-en` (с. 169–179), `hotoe-sticker-pack-en` (10 с.), `hotoe-us-passport-en` (2 с.),
`hotoe-calendar-1923-en` (4 с.), `hotoe-book-6-handouts-en` (с. 1–4). Русский текст — наш перевод (флаг `translated`, Р-251).
Генераторы — `.cache/lead-tools/gen-hotoe-campaign/` (`gen_campaign.py`, `gen_items.py`, `gen_rules.py`, `gen_handouts.py`,
`gen_art.py`, `gen_proposals.py`, `cutout.py`).

## Записи (24)

- Кампания: `hotoe-book-1-en/scenario/horror-on-the-orient-express` — summary, keeper_info, hook, advice, 20 шагов (19 глав + «Тайная глава»
  «Царство Террора»), conclusion, 4 таблицы.
- Предметы (8): шесть частей симулякра `hotoe-book-1-en/item/campaign-simulacrum-{head,torso,left-arm,right-arm,left-leg,right-leg}`;
  `campaign-sedefkar-scrolls` (все пять Свитков Седефкара); `campaign-mims-sahis` (нож впервые и полно описан в книге I, с. 52–53).
- Раздатка (6): `hotoe-book-1-en/handout/campaign-handout-{calendar-1923,us-passport,luggage-stickers,postcards,matchbox,simulacrum-sheet}`.
- Правила (9): `hotoe-book-1-en/rule/campaign-the-orient-express` (введение книги I); `hotoe-book-4-en/rule/campaign-{conversion-notes,
  conversion-statistics,conversion-skills,conversion-rule-differences,recommended-7th-edition-rules,spending-luck-points,pushing-the-roll,
  full-half-fifth-values-table}`.
- Картинки (19, `art-campaign.json`, применены): 4 листа календаря, 2 стороны паспорта, 3 наклейки, 5 сторон открыток, коробок,
  лист-вырезка; вырезки головы и торса симулякра и ножа Мимс Сахис (из листа-вырезки). Руки и ноги не вырезаны: на листе они не
  подписаны, левую и правую по рисунку не определить.
- Атмосфера: `atmosphere-campaign.json` (29 страниц).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка книги I | I, с. 1 | не взято (обложка; картинка — атмосфера) |
| Dedication; выходные данные | I, с. 2 | кампания: summary (посвящение Линну Уиллису), sources |
| Титульный лист | I, с. 3 | не взято (титул; атмосфера) |
| Credits | I, с. 4 | кампания: summary (авторы, первоначальный план, редакторы); остальные титры — не взято |
| Introduction (Марк Моррисон) | I, с. 5–6 | кампания: summary (издание 1991 года, премии Origins, второе издание, «Спутник путешественника»); обзор участников — не взято |
| About Call Of Cthulhu 7th Edition | I, с. 6 | кампания: advice «О 7-й редакции»; правила — книга IV (ниже) |
| What Is In This Box? | I, с. 7 | кампания: summary и таблица «Состав коробки» |
| Chaosium Thanks | I, с. 8 | не взято (благодарности) |
| Table of Contents | I, с. 9 | не взято (оглавление) |
| Book 1 Introduction: The Orient Express (Джефф Гиллан) | I, с. 11–15 | правило `campaign-the-orient-express` (конец введения на с. 15 — тоже здесь) |
| Orientation: The Campaign | I, с. 41 | кампания: summary, advice «Ожидаемые выборы» |
| Scenario Options (врезка, значки) | I, с. 41 | кампания: advice «Значки сценариев»; шаги `optional` |
| The Calendar | I, с. 41–42 | кампания: advice «Календарь»; раздатка `campaign-handout-calendar-1923` |
| Scenario Timelines | I, с. 42 | кампания: advice «Хронологии сценариев» |
| The Scenarios | I, с. 42 | кампания: advice «Порядок чтения» |
| Таблица «Scenario Summary» | I, с. 43 | кампания: таблица «Сценарии кампании» |
| London, 1923 (Dancers; Doom Train) | I, с. 42–43 | кампания: hook; шаги 1–2 |
| London, 1893 | I, с. 43 | кампания: шаг 3 |
| Paris, 1923 | I, с. 43–44 | кампания: шаг 4, advice «Изображения частей», «Спокойные поездки»; предмет «левая рука» |
| The Dreamlands | I, с. 44 | кампания: шаг 5 |
| Lausanne, 1923 | I, с. 44 | кампания: шаг 6; «Свитки Седефкара» |
| Milan, 1923 | I, с. 44 | кампания: шаг 7; предмет «торс» |
| Venice, 1923 | I, с. 44–45 | кампания: шаг 8; предмет «левая нога» |
| Constantinople, 1204 | I, с. 45 | кампания: шаг 9 |
| Trieste, 1923 | I, с. 45 | кампания: шаг 10; предмет «правая нога» |
| Dream Zagreb, 1923 | I, с. 45 | кампания: шаг 11 |
| Vinkovci, 1923 | I, с. 45 | кампания: шаг 12; предмет «Мимс Сахис» |
| Constantinople, 330 | I, с. 45 | кампания: шаг 13 |
| Belgrade, 1923 | I, с. 46 | кампания: шаг 14; предмет «правая рука» |
| Sofia, 1923 | I, с. 46 | кампания: шаг 15; предмет «голова» |
| Constantinople, 1923 | I, с. 46 | кампания: шаг 16, conclusion |
| Across Europe, 1923 | I, с. 46–47 | кампания: шаг 17 |
| London Again, 1923 | I, с. 47 | кампания: шаг 18, conclusion |
| Istanbul, 2013 | I, с. 47 | кампания: шаг 19 |
| The Sedefkar Simulacrum | I, с. 47 | кампания: keeper_info; предложение к `coc:item:sedefkar-simulacrum` |
| The Sedefkar Scrolls | I, с. 47–48 | кампания: keeper_info; предмет `campaign-sedefkar-scrolls` |
| Fenalik | I, с. 48 | кампания: keeper_info; предложение к `coc:character:fenalik` |
| The Fate Of The Scrolls | I, с. 49 | кампания: keeper_info; `campaign-sedefkar-scrolls` |
| Selim Makryat | I, с. 49–50 | кампания: keeper_info; предложения к `coc:organization:brothers-of-the-skin`, `…/selim-makryat` (источник); текст — ниже |
| Mehmet Makryat | I, с. 50–51 | кампания: keeper_info; предложение к `hotoe-book-2-en/character/mehmet-makryat` (источник); текст — ниже |
| Fenalik Again | I, с. 51 | кампания: keeper_info; предложение к `coc:character:fenalik` |
| The Investigators (сюжет) | I, с. 51 | кампания: keeper_info |
| Sedefkar's Legacies: The Sedefkar Simulacrum | I, с. 51–52 | шесть предметов-частей (описание, механика); кампания: keeper_info; предложение к симулякру |
| Sedefkar's Legacies: The Sedefkar Scrolls | I, с. 52 | `campaign-sedefkar-scrolls` |
| Sedefkar's Legacies: The Mims Sahis | I, с. 52–53 | `campaign-mims-sahis` |
| Таблица «Locations of the Sedefkar Scrolls» | I, с. 53 | кампания: таблица «Где хранятся Свитки Седефкара» |
| Таблица «Locations of Simulacrum Segments» | I, с. 53 | кампания: таблица «Где спрятаны части симулякра»; found_at частей |
| Running the Campaign | I, с. 53 | кампания: advice «Проведение кампании» |
| Historicity | I, с. 53–54 | кампания: advice «Историчность» |
| The Investigators (развитие, части в пути) | I, с. 54–55 | кампания: hook (Лондон), advice «Развитие сыщиков», «Части симулякра в пути», «Спокойные поездки» |
| The Brothers Of The Skin | I, с. 55 | кампания: advice «Братья кожи»; предложение к `coc:organization:brothers-of-the-skin` |
| Incidents Aboard The Orient Express | I, с. 55–56 | кампания: advice «Происшествия в Восточном экспрессе» |
| The Train Cars | I, с. 56 | кампания: advice «Вагоны» |
| The Investigator Survival Guide (вступление и список) | I, с. 56 | кампания: advice «Руководство по выживанию сыщиков» |
| Create New Characters | I, с. 56 | там же, пункт |
| Improve the Investigators | I, с. 56–57 | там же, пункт; правила книги IV |
| Modify Difficulty | I, с. 57 | там же, пункт |
| Reward Ingenuity | I, с. 57–58 | там же, пункт |
| Plan for Succession | I, с. 58 | там же, пункт |
| Deus ex Fenalik | I, с. 58 | там же, пункт; предложение к Феналику; `campaign-mims-sahis` (механика) |
| None of the Above | I, с. 58 | там же, пункт |
| Подписи к иллюстрациям (с. 12, 13, 14, 50, 51, 52, 55) | I | правило `campaign-the-orient-express` (подпись с. 12 — в тексте и errata); остальные — `atmosphere-campaign.json` |
| Index of Significant & Useful Entries | I, с. 73–74 | не взято (указатель) |
| Call of Cthulhu Conversion: Conversion Notes for Earlier Editions; Quick Conversion (врезка) | IV, с. 169 | `campaign-conversion-notes` |
| Statistics: Characteristics, Education, Hit Points, Damage Bonus, Build, Movement Rate (+ таблицы) | IV, с. 169–170 | `campaign-conversion-statistics` |
| Skills (+ таблица), Fighting, Attack Values | IV, с. 170–171 | `campaign-conversion-skills` |
| Rule Differences: Opposed Rolls And The Resistance Table, Characteristic Rolls (+ таблица), Difficulty, Idea Rolls And Know Rolls, Bonuses And Penalties, Chase Rules, Poison Damage (+ таблица) | IV, с. 171–172, 174 | `campaign-conversion-rule-differences` |
| Recommended 7th edition rules (врезка) | IV, с. 173 | `campaign-recommended-7th-edition-rules` |
| Spending Luck Points (Optional Rule); Recovering Luck Points | IV, с. 173 | `campaign-spending-luck-points` |
| Pushing The Roll; Foreshadowing Failure; Pushed Roll: Success; Pushed Roll: Failure | IV, с. 173–174 | `campaign-pushing-the-roll` |
| Full / Half / Fifth Values Table | IV, с. 175 | `campaign-full-half-fifth-values-table` (100 строк, все сверены) |
| Kickstarter Backers | IV, с. 176–179 | не взято (список спонсоров) |
| Реквизит: Calendar 1923 | 4 листа | `campaign-handout-calendar-1923` (+ 4 картинки) |
| Реквизит: US Passport | 2 с. | `campaign-handout-us-passport` (+ 2 картинки) |
| Реквизит: Sticker Pack — наклейки (с. 1, 2, 9) | | `campaign-handout-luggage-stickers` (+ 3 картинки) |
| Реквизит: Sticker Pack — открытки (с. 3–7) | | `campaign-handout-postcards` (+ 5 картинок) |
| Реквизит: Sticker Pack — коробок (с. 8) | | `campaign-handout-matchbox` (+ картинка) |
| Реквизит: Sticker Pack — «Sedefkar Simulacrum & Mims Sahis» (с. 10) | | `campaign-handout-simulacrum-sheet` (+ картинка); вырезки — у головы, торса и Мимс Сахиса |
| Книга VI: обложка, выходные данные | VI, с. 1–2 | не взято (обложка, выходные данные) |
| Книга VI: Table of Contents; About the Handouts | VI, с. 3 | не взято (оглавление; пояснение, что номера страниц на раздатке — книга и страница источника) |
| Книга VI: с. 4 | VI, с. 4 | не взято (пустая страница) |

## Не взято

- Обложка и титул книги I (с. 1, 3), выходные данные, полные титры (с. 2, 4 — авторы взяты в summary), благодарности
  «Chaosium Thanks» (с. 8), оглавление (с. 9), указатель (с. 73–74) — служебные страницы без игрового материала. В указателе номера
  страниц сдвинуты на +4 относительно напечатанных (например, «Calendar for 1923 … 45» при печатной с. 41).
- Из «Introduction» (с. 5–6) не взяты перечни участников переиздания (кто какую главу дополнил, эссе, тестеры) — это история издания;
  взяты год и премии первого издания, состав второго, посвящение.
- Список спонсоров Kickstarter (книга IV, с. 176–179).
- Книга VI, с. 1–4: обложка, выходные данные, оглавление, «About the Handouts», пустая страница.
- Подписи-инструкции реквизита («Matchbox. To use, print image…») — взяты пересказом в описании коробка.

## Опечатки и сомнения

- Книга I, с. 12: текст — первый рейс в 1882 году, подпись к фото — «October 4, 1883» (errata в `campaign-the-orient-express`).
- Книга I, с. 43 и 44–46: названия глав «Love (and Death) in a Gondola», «Bread or Stone», «Little Cottage in the Woods»; в книге III —
  «Death (and Love) in a Gondola», «Bread and Stone» (оглавление; на с. 131 — «Bread or Stone»), «Little Cottage in the Wood»; на с. 53 —
  «Death in a Gondola» (errata кампании).
- «Cold Wind Blowing»: таблица на с. 43 — «Core» (там правая нога), указатель (с. 73) — «optional scenario»; план импорта считает главу
  необязательной. В записи кампании — основной. **Вопрос владельцу / сведению:** `optional` у этапа `cold-wind-blowing`.
- Книга I, с. 53: «Oraszac» вместо «Orašac» (errata кампании и правой руки, исправлено).
- Книга I, с. 43 и 53: место правой ноги — «Trieste» и «Postumia» (errata правой ноги; по сути одно и то же).
- Календарь 1923: в апреле напечатан 31 день (errata раздатки).
- Паспорт: «in the year 1919 … the one hundred and forty seventh» (147-й год независимости — 1923) и подпись Ч. Э. Хьюза, госсекретаря
  с 1921 года (errata раздатки).
- Книга I, с. 4: «Sedekfar Simulacrum (2013)» в титрах — опечатка в «Sedefkar» (титры не взяты).
- Симулякр: потеря Рассудка 1/1d8 («Царство Террора», с. 42) и 1/1d6 (книга I, с. 52) — разные сцены; в предложении к
  `coc:item:sedefkar-simulacrum` — оба с пометкой.
- Книга IV, с. 175: таблица полных/половинных/пятых значений сверена с округлением вниз — расхождений нет.
- Вырезки рук и ног симулякра: какая левая, какая правая — по рисунку не определить; картинки не даны.

## Предложения (`proposals-campaign.json`, 61)

- `coc:item:sedefkar-simulacrum` — история и вид по книге I (description), силы, 1/1d6, Пагубное влияние (mechanics), заметка о
  Бескожем и двух значениях потери Рассудка, refs (кампания, шесть частей, свитки, Мимс Сахис, Бескожий, Братья кожи, Седефкар,
  Мехмет, Селим), 5 источников, эпохи `1920s`, `dark-ages`, флаг `translated`.
- `coc:character:fenalik` — абзацы книги I в legend (Тиллий Корв, 1204, Венеция, Париж, Шарантон, «Феналик снова», Deus ex Fenalik),
  заметка, 4 источника, эпохи, флаг `translated`.
- `coc:organization:brothers-of-the-skin` — абзац 1923 года (description), цели 1923 года, based_at (Красная/Отверженная мечеть),
  members (Селим, Мехмет), refs, эпоха `1920s`, 4 источника, заметка.
- `coc:creature:skinless-one` — абзац книги I в legend, 3 источника (refs у существа схемой не предусмотрены).
- `coc:spell:cleansing-ritual` — «Седефкарского симулякра» → «Симулякра Седефкара».
- `hotoe-book-2-en/character/mehmet-makryat`, `hotoe-book-4-en/character/selim-makryat` — источники книги I (4 и 2). Запись Селима
  заводит часть constantinople: до неё файл предложений целиком не применится (`apply.py` — всё или ничего).

Пробный прогон без двух предложений Селима: «правок: 59, уже было: 0, записей: 6».

### Тексты для записей Мехмета и Селима (вставить в legend при сведении; наш перевод, книга I)

- **Селим Макрьят (с. 49–50).** В начале XIX века молодой учёный Селим Макрьят прочёл Свитки Седефкара. Он считал себя
  рационалистом, но чтил свитки как реликвии, связанные с рождением османской мощи, а лично его они соблазняли как орудия его
  жестокого садизма. Когда обряды сработали, у Бескожего появился новый поклонник. Вообразив себя новым Османом, Макрьят собрал
  последователей, научил их части магии свитков и основал культ — Братьев кожи; среди прочего они захватили Красную мечеть на месте
  Красной башни Седефкара, прозванную Отверженной мечетью. Магия Свитка Чрева позволила ему заменить все части тела, кроме сердца
  (сердца нет у самого Бескожего), и он стоял перед неизбежной смертью. Свитки намекали, что владелец симулякра будет бессмертен
  (точнее, сможет заменять отказывающие части тела, но всё ещё может погибнуть от ран); силы Селима иссякли, и он послал сына
  Мехмета найти симулякр и принести его в Отверженную мечеть, где Братья могли бы греться в его славе и в поклонении Бескожему
  жить вечно.
- **Мехмет Макрьят (с. 50–51).** Мехмет слушался отца, но он еретик: симулякр, по его мнению, должен дать Братьям великую власть в
  мире, а Бескожий — орудие, а не предмет поклонения. Он учился в Европе и Англии и изучил Мифы глубже Селима. В поиски он взял трёх
  Братьев и каждому дал свою внешность, личность и имя; вместе они объездили мир, и он понял, где могут лежать все части. Не веря
  верности двойников и под надзором отца, он вернулся в Константинополь, сделал доклад, обещал скорый успех и уехал, похитив Свиток
  Левой руки с Ритуалом очищения; двойников-Мехметов он собрал в Лондоне и убил. Сам искать части он не может (агенты отца знают его,
  их магия делает маскировку бесполезной), Братьев использовать нельзя (они верны Селиму) — поэтому он выбирает людей, о которых отец
  не знает и которые пойдут на труды ради старого друга в беде: сыщиков. О Феналике он не знает.

## Ссылки на записи других частей (ждут их; `check.py` до сведения даёт «ссылка на несуществующую запись»)

Этапы: `hotoe-book-2-en/scenario/{les-fleurs-du-mal,the-dreamlands-express,nocturne,note-for-note,the-blood-red-fez}` (на момент
проверки «Танцоры» и «Поезд рока» уже были), `hotoe-book-3-en/scenario/{death-and-love-in-a-gondola,the-dark-crusader,cold-wind-blowing,
in-a-city-of-bells-and-towers,bread-and-stone,sanguis-omnia-vincet,little-cottage-in-the-wood}`, `hotoe-book-4-en/scenario/{repossession,
by-the-skin-of-the-teeth,blue-train-black-night,the-fog-lifts,the-simulacrum-unbound}`; персонажи `hotoe-book-3-en/character/sedefkar`,
`hotoe-book-4-en/character/selim-makryat`; общие города `coc:location:{lausanne,trieste,vinkovci,belgrade,orasac,sofia}` (и `venice`,
если его ещё нет); книга `coc:tome:scroll-of-the-head`. Других висячих ссылок в моих файлах нет.

## Кандидаты в записи (для частей глав)

- Сердце влюблённых (Lovers' Heart) — предмет «Экспресса Страны грёз»; Врата рока (Doom Gate) — «Поезд рока»; «Дьявольский симуляр»
  (The Devil's Simulare) — рукопись из Венеции; «Рассказ Тиллия Корва» (The Account of Tillius Corvus) — документ из Винковцев;
  медальон Итаквы (Trieste).
- Персонажи без записей, упомянутые в книге I: Эдгар Веллингтон и его брат (Лозанна), герцог дез Эссент / Принц-мозаика
  (Лозанна; в базе уже ссылаются на `hotoe-book-2-en/character/jean-floressas-des-esseintes`), Анри (проводник 1893 года и шеф поезда
  Страны грёз), Баба-яга, Язмина Морич, граф Балдуин, брат Меровак (= Феналик), Унвен, Иоганн Винкельман (призрак), Луи Малон
  (есть в «Царстве Террора»), Мария и Джорджо, Фачча.
- Ритуал очищения (Ritual of Cleansing) и Ритуал свершения (Ritual of Enactment), Пагубное влияние (Baleful Influence) — заклинания
  глав (указатель книги I называет их «spell»); общий `coc:spell:cleansing-ritual` — другой ритуал (Grand Grimoire).
- Красная (Отверженная) мечеть, музей Топкапы — места Константинополя (часть constantinople).
- Мимс Сахис заведён здесь (`hotoe-book-1-en/item/campaign-mims-sahis`): часть zagreb-vinkovci должна ссылаться на него и дополнять
  предложениями, а не заводить свой.

## Термины (английский → русский; одна форма везде)

| English | Русский |
|---|---|
| Horror on the Orient Express | «Ужас в Восточном экспрессе» |
| Campaign Book / Through the Alps / Italy and Beyond / Constantinople & Consequences / Strangers on the Train | «Книга кампании» / «Через Альпы» / «Италия и дальше» / «Константинополь и последствия» / «Незнакомцы в поезде» |
| The Traveler's Companion | «Спутник путешественника» |
| Orient Express | Восточный экспресс |
| Simplon-Orient Express | Симплон-Ориент-экспресс (как у части express) |
| Simplon Express | Симплонский экспресс |
| Venice Simplon-Orient-Express | Венеция-Симплон-Ориент-экспресс |
| Compagnie Internationale des Wagons-Lits (CIWL) | Международная компания спальных вагонов (CIWL) |
| Taurus Express | экспресс «Таурус» |
| Sedefkar Simulacrum | Симулякр Седефкара (в тексте и «симулякр») |
| Head / Torso / Left Arm / Right Arm / Left Leg / Right Leg (of the simulacrum) | голова / торс / левая рука / правая рука / левая нога / правая нога |
| Sedefkar Scrolls | Свитки Седефкара |
| Scroll of the Head / Belly / Legs / Right Hand / Left Hand | Свиток Головы / Чрева / Ног / Правой руки / Левой руки |
| Ritual of Enactment | Ритуал свершения |
| Ritual of Cleansing | Ритуал очищения |
| Baleful Influence | Пагубное влияние |
| Mims Sahis | Мимс Сахис |
| Voorish knife / Voor | вурский нож / вуры |
| Lovers' Heart | Сердце влюблённых |
| Doom Gate / Doom Train | Врата рока / Поезд рока |
| The Devil's Simulare | «Дьявольский симуляр» |
| The Account of Tillius Corvus | «Рассказ Тиллия Корва» |
| The Skinless One | Бескожий |
| Brothers of the Skin; Brother (of the Skin) | Братья кожи; Брат кожи |
| The Unburdened Flesh | «Необременённая плоть» |
| Red Tower / Red Mosque / Shunned Mosque | Красная башня / Красная мечеть / Отверженная мечеть |
| Topkapi Museum | музей Топкапы |
| Sedefkar | Седефкар |
| Fenalik; Comte Fenalik | Феналик; граф Феналик |
| Tillius Corvus | Тиллий Корв |
| Brother Merovac | брат Меровак |
| Count Baldwin | граф Балдуин |
| Unwen | Унвен |
| Selim Makryat / Mehmet Makryat | Селим Макрьят / Мехмет Макрьят (как у части london) |
| Professor (Julius) Smith | профессор Смит |
| Heironymous Menkaph | Иеронимус Менкаф (как у части london) |
| Henri | Анри |
| Edgar Wellington | Эдгар Веллингтон |
| Duc des Esseintes; Jigsaw Prince | герцог дез Эссент; Принц-мозаика |
| Baba Yaga | Баба-яга |
| Jazmina Moric | Язмина Морич |
| Johann Winckelmann | Иоганн Винкельман |
| Louis Malon | Луи Малон (как в «Царстве Террора») |
| Maria and Georgio | Мария и Джорджо |
| Faccia | Фачча |
| Georges Nagelmackers / George Pullman | Жорж Нагельмакерс / Джордж Пульман |
| Challenger Foundation / Challenger Trust Banquet Lecture | Фонд Челленджера / лекция-банкет Фонда Челленджера |
| Gulf of Nodens | Бездна Ноденса |
| Dream Zagreb / Dream Lausanne | Загреб из сна / Лозанна из сна |
| Blackshirts | чернорубашечники |
| Perfect Skin (рассказ) | «Идеальная кожа» |
| Dancers in an Evening Fog | «Танцоры в вечернем тумане» |
| The Blood Red Fez | «Кроваво-красная феска» |
| Les Fleurs du Mal | «Цветы зла» |
| The Dreamlands Express | «Экспресс Страны грёз» |
| Nocturne | «Ноктюрн» |
| Note for Note | «Нота в ноту» |
| Death (and Love) in a Gondola | «Смерть (и любовь) в гондоле» |
| The Dark Crusader | «Тёмный крестоносец» |
| Cold Wind Blowing | «Дует холодный ветер» |
| In a City of Bells and Towers | «В городе колоколов и башен» |
| Bread and Stone / Bread or Stone | «Хлеб и камень» |
| Sanguis Omnia Vincet | «Sanguis Omnia Vincet» |
| Little Cottage in the Wood(s) | «Избушка в лесу» |
| Repossession | «Изъятие» |
| By the Skin of the Teeth | «На волосок» |
| Blue Train, Black Night | «Синий поезд, чёрная ночь» |
| The Fog Lifts | «Туман рассеивается» |
| The Simulacrum Unbound | «Освобождённый Симулякр» |
| Scenario Options; core / optional scenario | значки сценариев; основной / необязательный сценарий |
| Investigator Survival Guide | Руководство по выживанию сыщиков |
| Create New Characters / Improve the Investigators / Modify Difficulty / Reward Ingenuity / Plan for Succession / None of the Above | Создать новых персонажей / Усилить сыщиков / Изменить сложность / Поощрять изобретательность / Запастись преемниками / Ничего из перечисленного |
| Consider yes | «Подумай о „да“» |
| Conversion Notes for Earlier Editions | Перевод на ранние редакции |
| Regular / Hard / Extreme difficulty | обычная / трудная / чрезвычайная сложность |
| Hard / Extreme success | Трудный / Чрезвычайный успех (глоссарий) |
| Resistance Table | таблица сопротивления |
| bonus die / penalty die | бонусная кость / штрафная кость |
| opposed roll | встречная проверка |
| Idea roll / Know roll | проверка Идеи / проверка Знаний |
| Spending Luck Points / Recovering Luck Points | трата пунктов Удачи / восстановление пунктов Удачи |
| improvement check (Luck, skill) | проверка развития; галочка (check) |
| Pushing the Roll / Foreshadowing Failure | повторная проверка / предчувствие провала |
| fumble / critical / malfunction | крах / критический успех / осечка |
| impale | проникающая рана |
| Poison potency (POT) | сила яда (POT) |
| Full / Half / Fifth Values Table | Таблица полных, половинных и пятых значений |
| Luggage stickers / Postcards / Matchbox / Puzzle-Cut Simulacrum Sheet / American Passports | багажные наклейки / почтовые открытки / спичечный коробок / лист-вырезка / американские паспорта |
