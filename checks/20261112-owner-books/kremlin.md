# «Secrets of the Kremlin, 1931» (secrets-of-the-kremlin-en) — сверка заголовков (Р-134, Р-221)

Часть «kremlin»: сценарий целиком, 21 физическая страница. **Книга не для 7-й редакции**: T.O.M.E., 1984 (переиздание
TOC, 2002), характеристики без процентов, ХАР (CHR) вместо НАР, бонус к урону «+1D6 Damage», потеря Рассудка «1D20 SAN»
без дроби. Поэтому статблоков 7e нет: характеристики Потапова, Ивана и Николая — текстом в описании персонажа как
напечатаны, Тёмная молодь и Шоггот — `instance_of` общих видов. Печатные страницы = физическим («page N/21», offset 0).
Русский текст — по переводу владельца (`2_Обработка\тайны кремля 1931\document.html`), сверен с оригиналом; числа — по
английской странице, меры — метрические (Р-64). Имена сверены со сборником 1984 года («Glozel est Authentique & Secrets
of the Kremlin», [EN 6e], OCR): совпадают. Эпоха — `1930s`. Префикс записей: `secrets-of-the-kremlin-en/<вид>/<slug>`
(ниже — без префикса).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул «Secrets of the Kremlin» by E.S. Erkes | 1 | `scenario/secrets-of-the-kremlin` (summary) |
| Introduction | 2 | `scenario/secrets-of-the-kremlin` (summary, advice: раздавать копии страниц); юридический абзац — «Не взято» |
| Background (Самсонов в Берлине) | 2 | `scenario/secrets-of-the-kremlin` (keeper_info), `character/alexei-samsonov` |
| The Tunnels | 2 | `scenario/secrets-of-the-kremlin` (keeper_info), `location/underground-kremlin`, `location/dungeon-5`, `location/lenin-mausoleum`, `tome/russian-necronomicon`; греческий «Некрономикон» — предложение `copies` для `coc:tome:necronomicon-greek` |
| Plan of the Kremlin (ключ 1–42, план) | 3 | `map/kremlin-plan` (`app/maps/kremlin-plan.jpg`, 55 меток: 42 номера, повторы 22×4, 34×2, 41×2, 42×2, 7 французских подписей); места `location/kremlin-01-borovitsky-tower` … `location/kremlin-42-captured-cannons`; подписи — `location/alexandrovsky-garden`, `red-square`, `lenin-mausoleum`, `st-basils-cathedral`, `moskvoretsky-bridge`, `moscow-river` |
| Aleksandrov | 4–5 | `character/vladimir-aleksandrov`, `creature/kremlin-dark-young` (legend) |
| The Dark Young | 5 | `scenario/secrets-of-the-kremlin` (keeper_info), `creature/kremlin-dark-young`, `character/josef-stalin`, `character/genrikh-yagoda`, `character/blind-guards`, `character/asylum-inmates`, `character/expedition-survivors`, `character/kremlin-chemists`, `location/laboratory` |
| Potapov (похищение в Берлине) | 5, 7 | `character/evgeny-potapov` (legend), `location/potapov-apartment` |
| Scene One: February 21, 1931 | 7–8 | `scene/scene-one-london`, `handout/anonymous-note`, `character/walter`, `location/london-flat`, `scenario/secrets-of-the-kremlin` (hook) |
| A Note on Role-Playing the Character of Walter | 8 | `scene/scene-one-london` (mechanics), `character/walter`, `scenario/secrets-of-the-kremlin` (advice) |
| Accreditation | 8 | `scene/scene-one-london` (mechanics) |
| Library Use (Лондон/Берлин) | 8 | `scene/scene-one-london` (mechanics) |
| Scene Two: Berlin | 8–9 | `scene/scene-two-berlin`, `location/berlin`, `location/berliner-stadtbank`, `location/stadthof-hotel`, `item/safe-deposit-box` |
| Содержимое ячейки: The Times (Oct 20, 1930); Pravda (Oct 3, 1930); Deutsches Reichswehr; The New York Times (July 8, 1928); The International Herald Tribune (Dec 8, 1930) | 9 | `handout/times-blind-veterans`, `handout/pravda-aleksandrov`, `handout/reichswehr-letter`, `handout/nyt-construction`, `handout/herald-tribune-mental-illness` |
| Additional Investigation | 9–10 | `scene/scene-two-berlin`, `location/potapov-apartment`, `handout/reichswehr-letter` (подделка по словам рейхсвера) |
| The Train from Berlin to Moscow | 10 | `scene/train-to-moscow`, `item/stilt-shoes`, `character/ivan` |
| Scene Three: Moscow (Катков, Саша, Арбатова, «Nodens») | 10 | `scene/scene-three-moscow`, `location/hotel-rossiya`, `location/moscow-central-station`, `character/yuri-katkov`, `character/sasha`, `character/tatiana-arbatova`, `item/forged-passports`, `organization/gpu` |
| Two Cults | 10–11 | `organization/nodens-brotherhood`, `organization/shub-niggurath-cult`, `scenario/secrets-of-the-kremlin` (keeper_info) |
| Ivan | 11 | `character/ivan`, `scene/scene-three-moscow` |
| The Conference | 11 | `scene/conference`, `location/kremlin-12-spasskaya-tower`, `location/kremlin-37-kremlin-grand-palace`, `location/kremlin-29-ivan-the-great-bell-tower`, `location/tunnel-c` |
| Returning to the Hotel Rossiya | 11 | `scene/nikolai`, `character/nikolai` |
| The Situation | 11 | `scene/nikolai`, `organization/shub-niggurath-cult` |
| Nikolai | 11 | `scene/nikolai`, `character/nikolai`, `location/lenin-purchasing-building-trapdoor` |
| Иван следует за сыщиками (без заголовка) | 12 | `scene/ivan-in-the-tunnels`, `character/ivan` |
| Врезка «The Kremlin in the early twentieth century» | 12 | `location/kremlin` (description, history), `location/kremlin-22-kremlin-walls`, `location/kremlin-12-spasskaya-tower`, `coc:location:moscow` |
| The Bell Tower of Ivan the Great | 12 | `location/kremlin-29-ivan-the-great-bell-tower`, `location/kremlin-23-sobornaya-square` |
| Inhabitants of the Lower Tunnels: Dungeon 1–5 | 13 | `scene/dungeons`, `location/dungeon-1` … `dungeon-5`, `item/third-rome-reliefs`, `location/tunnel-h` |
| A Note on Stalin | 13 | `scene/stalins-study`, `location/stalins-study`, `character/josef-stalin`, `character/nadezhda-stalina`, `character/vassily-stalin`, `character/svetlana-stalina`, `character/kremlin-guards` |
| The Lowest Room | 13–14 | `scene/lowest-room`, `location/lowest-room`, `location/blind-barracks`, `location/dark-young-pit`, `location/yagoda-office`, `location/laboratory`, `creature/kremlin-dark-young` |
| The Final Secret | 14 | `scene/final-secret`, `creature/kremlin-shoggoth`, `character/ivan-the-terrible`, `scenario/secrets-of-the-kremlin` (keeper_info, таблица «Хронология событий») |
| Escaping | 14 | `scene/escaping`, `scenario/secrets-of-the-kremlin` (conclusion) |
| The Underground Kremlin: Tunnels, Chambers, and Waterways — Level One | 15 | `location/underground-kremlin`, `location/neglinnaya-underground`, `location/level-1-tower-tunnels`, `location/secret-tower-guard-post`, `location/kremlin-04-taynitskaya-tower` |
| Level Two | 15 | `location/level-2-junction`, `location/level-2-northeast-tunnel`, `location/level-2-east-tunnel`, `location/tunnel-a`, `location/tunnel-b` |
| Level Three | 15 | `location/tunnel-c`, `location/tunnel-d`, `location/tunnel-e`, `location/tunnel-f`, `location/tunnel-g`, `location/stalins-study` |
| Level Four: Dungeons; Note: Guards | 16 | `location/dungeon-1` … `dungeon-5`, `location/underground-kremlin`, `character/kremlin-guards`, `scene/underground-descent` |
| Level Five: The Lowest Room | 16 | `location/lowest-room`, `location/dark-young-pit`, `location/tunnel-h` |
| Статблоки: Evgeny Potapov; Ivan; Nikolai | 16 | `character/evgeny-potapov`, `character/ivan`, `character/nikolai` (характеристики текстом, заклинания — `abilities` со ссылкой на `coc:spell:contact-nodens` / `contact-shub-niggurath`) |
| Карта «Niveau Un» | 17 | `map/kremlin-level-1` (3 метки) |
| Карта «Niveau Deux» | 18 | `map/kremlin-level-2` (5 меток) |
| Карта «Niveau Trois» | 19 | `map/kremlin-level-3` (6 меток) |
| Карта «Niveau Quatre» (легенда Cachot 1–5) | 20 | `map/kremlin-level-4` (11 меток: строки легенды и номера 1–5, туннель H) |
| Карта «Niveau Cinq» | 21 | `map/kremlin-level-5` (8 меток) |

Сквозное: `scene/underground-descent` — путь вниз по приложению (с. 11, 15–16); `coc:location:moscow` — новый общий город;
таблица «Хронология событий» — в сценарии. Награды Рассудка книга не печатает — это сказано в conclusion сценария.

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Иллюстрации: титульный рисунок, сцена похищения (©1984), Спасская башня, фото Кремля | 1, 6, 10, 12 | `app/art/` не входит в owns части; кандидаты для `pipeline/art/add_images.py` при сведении |
| Юридический абзац Introduction («by permission of Arkham House», «similarity … coincidental») | 2 | не игровой материал |
| Пустая рамка «NOTES» и колонтитулы «© T.O.M.E. / © 2002 TOC» | 16, все | оформление |
| Гора Мурад (Памир) отдельной записью | 4, 5, 9 | место вне города не проходит проверку (место без part_of — только город, Р-189); факты — в `character/vladimir-aleksandrov`, `creature/kremlin-dark-young`, `handout/pravda-aleksandrov` |
| Упомянутые без записи: Эрнст и Франц (письмо), адъютант и атташе Самсонова, офицеры рейхсвера, берлинские дети, хозяин и соседи Потапова, высланный корреспондент «Таймс», глава министерства печати, расстрелянные археологи и специалисты, строители мавзолея, «обычный русский», сказавший пароль | 2, 5, 7, 9, 11, 14 | только упоминания — текстом в сценах, персонажах и раздатках |
| Упомянутые места без записи: Лубянка, Московский университет, Варшава, Александерплац, пивной зал в Берлине, лагеря за Полярным кругом, советская граница | 2, 7, 10 | только упоминания — текстом (`coc:location:moscow`, `organization/gpu`, сцены) |
| Кружок «o» на Красной площади и стрелки севера на картах | 3, 17 | не подпись и не номер ключа |
| Перевод владельца: картинки в `assets` — те же кропы страниц оригинала без перевода подписей | — | взяты свои кропы страниц 200 dpi; подписи карт переведены в `spots[].text` |

## Опечатки и сомнения

- Даты конференции: с. 7 — открытие в 11:00 в понедельник 15 апреля; с. 11 — автобус в 7:30 и речь в 8:00; с. 14 —
  «пятница, 17 апреля» (если 15-е понедельник, 17-е — среда; в 1931 году 15-е — среда). `errata` в сценарии и сценах
  «Конференция и колокольня», «Последняя тайна».
- Карта второго уровня: подпись «TUNNEL "A"» стоит вдоль длинного туннеля на северо-восток, а по тексту туннель A —
  короткий проход от него к туннелю C (подпись «Tunnel conduisant au tunnel C») — `note` у метки.
- Легенда карты четвёртого уровня: «Potatov» вместо «Potapov» — `note` у метки; титул карты 1: «Le Krelim souterrain».
- Ключ плана: «Nikol'kaya», «Tsarkaya» (в издании 1984 года — «Nikol'skaya»); в `name.en` — как напечатано, верное — в aliases.
- В тексте с. 15 башни названы по-английски: Secret Tower, Water Tower, Forest Tower, Beklemishev Tower; Тайная = № 4
  Тайницкая (как у владельца), Водовзводная и Боровицкая — вывод из текста, Беклемишевская = № 8 Москворецкая — вывод
  (в книге не сказано), помечено в описаниях.
- Исторические вольности сценария (гостиница «Россия» в 1931 году, Василию Сталину «шесть лет», «Надежда Сталина»)
  оставлены как напечатаны и не помечены — не числа правил (Р-39).

## Технический долг и вопросы

- **Берлин**: общей записи нет, а `kb/locations/` этой части не принадлежит (кроме Москвы). Заведён город книги
  `location/berlin` (с ним `berliner-stadtbank`, `stadthof-hotel`, `potapov-apartment`); по Р-190 его нужно перенести в
  общую `coc:location:berlin` при сведении (переноса в `apply.py` нет).
- Сталин и Ягода — исторические персонажи; если они есть в «Тенях Ленинграда», по Р-154 нужны общие записи.
- ГПУ (`organization/gpu`) — кандидат в общую организацию советской тайной полиции вместе с НКВД «Теней Ленинграда».
- Предложения (`proposals-kremlin.json`, 18 правок): экземпляр греческого «Некрономикона» (`copies` + источник),
  ссылка Лондона на квартиру, ссылки 15 терминов владельца на записи сценария; пробный прогон `apply.py` проходит.
