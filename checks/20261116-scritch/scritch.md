# Scritch Scratch (`scritch-scratch-en`) — сверка переноса

Lynne Hardy «and Friends», Chaosium, 2018 (Free RPG Day; Chaosium Publication 23157); карты — Matt Ryan; наши дни,
конец лета, север Англии; `axes.era` `modern`. PDF — 42 страницы. **Смещение страниц: −1** (физическая = печатная + 1):
«3» на физ. 4, «6» на физ. 7, «22» на физ. 23, «25» на физ. 26; обложка (физ. 1), титул (физ. 2), выходные данные (физ. 3),
листы сыщиков (физ. 27–40) и задняя обложка (физ. 42) без номера (`printed_page: null`). В `pipeline/source/books.json`
смещение не записано — его ставит ведущий. Русского перевода в базе нет (проверено по `kb/`: Маскоби, Muscoby, Гуртин,
Gurteen, Scritch — совпадений нет).

Записей: 70 — сценарий 1, сцены 9, персонажи 13 (6 прегенов, 7 NPC), существа 2, места 29, карты 2, предметы 9,
раздатка 1, организации 4. Картинки: 15 (`app/art/*/scritch-*.webp`), карты — `app/maps/scritch-muscoby-village.jpg`,
`app/maps/scritch-gurteens-cottage.jpg` (вынуты из PDF, приложение B); рамки вырезки — `scritch-boxes.json`;
атмосфера — `atmosphere.json` (11 строк). Предложений правок общих записей нет (файл `proposals-scritch.json` не нужен).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул | 1–2 (без номера) | сценарий `scenario/scritch-scratch` (sources); картинка обложки — atmosphere.json |
| Credits (выходные данные) | физ. 3 | сценарий: summary, sources (note) |
| Getting Ready to Play | 3 | сценарий: advice («Подготовка») |
| Foreword | 3 | сценарий: advice (последний абзац) |
| Scritch Scratch (вступление), The Investigators | 4–5 | сценарий: summary, hook; прегены (legend) |
| врезка «Alternative Settings» | 4 | сценарий: advice («Другая обстановка») |
| Suggested useful occupations | 5 | сценарий: advice («Полезные профессии») |
| врезка «What’s in a Name?» | 5 | сценарий: advice; организация `martin-cleaning-firm` |
| Introduction | 5–6 | сценарий: keeper_info («Предыстория»); места `muscoby` (history), `muscoby-closed-school`, `muscoby-gift-shop`; `old-gurteen`; организация `council` |
| Handout 1: Scritch Scratch | 6, 23 | раздатка `handout-1-scritch-scratch` (текст + перевод + картинка из приложения B) |
| врезка «Wheels Within Wheels» | 6 | сценарий: keeper_info, advice; организация `council` |
| Alternative Beginnings | 6 | сценарий: hook; предмет `gurteens-keys` |
| What’s Really Going On | 7 | сценарий: keeper_info; существо `green-man` (legend) |
| врезка «The Real Green Man» | 7 | сценарий: advice («Настоящий зелёный человек»); предмет `rodent-scrapbooks` |
| Scenario Structure; How to Approach This Scenario; Keeper note | 7 | сценарий: keeper_info («Структура»), advice («Как вести»); сцены `arrival-in-muscoby`, `end-game` |
| Dramatis Personae (Mrs. Lucy Albright, Mrs. Joyce Deakins, Old George, Young George, Old Gurteen, The Green Man) | 8–9 | персонажи `lucy-albright`, `joyce-deakins` (+ `arthur-deakins`), `old-george`, `young-george`, `old-gurteen`; существо `green-man`; портреты |
| врезка «The Mouseman» | 9 | сценарий: advice («Мышиный человек»); место `muscoby-car-park` (щит) |
| Muscoby | 9 | сцена `arrival-in-muscoby`; места `muscoby`, `muscoby-car-park` |
| Lucy’s Tea Shoppe | 9, 11 | сцена `lucys-tea-shoppe`; место `lucys-tea-shoppe`; `lucy-albright` |
| Handout 2: Muscoby | 10, 24 | карта `map/muscoby-village` (10 меток) |
| врезка «Mobile Phones in Muscoby» | 11 | сцены `arrival-in-muscoby` (mechanics), `lucys-tea-shoppe`; место `muscoby`; `rat-catchers-arms` (будка) |
| Muscoby Village Church; Church Exterior | 11–12 | сцена `muscoby-church`; место `st-gertrudes-church` |
| Church Interior; A Mousey Connection; Stone Watchers | 12–13 | сцена `muscoby-church`; место `st-gertrudes-church`; предмет `green-man-church-carving` (фото «The green man in the church») |
| Old Gurteen’s Cottage; Entering the Cottage | 13 | сцена `gurteens-cottage`; места `gurteens-cottage`, `cottage-hallway`; предмет `gurteens-keys` |
| The Parlor; The Black Book | 13 | место `cottage-parlor`; предмет `gurteen-family-bible` |
| The Dining Room (+ Keeper note о картине) | 13–14 | место `cottage-dining-room`; предметы `rodent-scrapbooks`, `green-man-painting` |
| The Bedrooms | 14 | места `cottage-gurteens-bedroom`, `cottage-parents-bedroom` |
| The Attic | 14 | место `cottage-attic` |
| The Sitting Room (и ванная) | 14 | места `cottage-sitting-room`, `cottage-bathroom` |
| Handout 3: The Cottage | 15, 25 | карта `map/gurteens-cottage` (21 метка: 15 номеров + подписи) |
| The Kitchen (кладовая) | 16 | места `cottage-kitchen`, `cottage-pantry` |
| The Courtyard (+ Keeper note о капканах) | 16 | места `cottage-courtyard`, `cottage-outdoor-toilet`, `cottage-store-room`, `cottage-chemical-storage`, `cottage-potting-shed`, `cottage-workshop`; предметы `gurteens-poisons`, `workshop-traps` |
| The Woods | 16 | сцена `the-woods`; место `muscoby-woods` |
| иллюстрация «The rat bunting» | 17 | место `muscoby-woods` (картинка) |
| Creeping Horror; Entering the Woods; Keeper note | 17 | сцена `the-woods`; место `muscoby-woods` |
| Appleford | 17 | место `appleford` |
| The Golden Ram | 17 | сцена `golden-ram`; место `golden-ram` |
| Speaking with Old George; Speaking with Young George | 18 | сцена `golden-ram`; `old-george`, `young-george`; раздатка `handout-1-scritch-scratch` |
| The Appleford Library and Museum; The Museum | 18–19 | сцена `appleford-library`; место `appleford-library-museum`; предметы `rodent-dioramas`, `church-leaflet`; `reginald-gurteen`; организация `appleford-historical-society` |
| Appleford Community Hospital; Patient Gurteen; Speaking with Gurteen | 19 | сцена `patient-gurteen`; место `appleford-community-hospital`; `old-gurteen` |
| End Game | 19–20 | сцена `end-game`; существа `green-man`, `rat-pack` |
| иллюстрация «The Green Man attacks!» | 20 | atmosphere.json |
| Conclusion | 20–21 | сценарий: conclusion; сцена `end-game`; место `muscoby` (history) |
| Rewards | 21 | сценарий: conclusion, таблица «Награды» |
| Appendix A: Characters and Monsters (Lucy Albright, Joyce Deakins, Young George, Old George, Old Gurteen) | 21–22 | статблоки персонажей |
| The Green Man, avatar of Nyarlathotep | 22 | существо `green-man` (статблок, способности; рисунок) |
| The Rats; Rat Pack | 22–23 | существо `rat-pack` |
| Appendix B: Player Handouts (Handouts 1–3) | 23–25 | раздатка `handout-1-scritch-scratch`; карты `muscoby-village`, `gurteens-cottage` |
| Листы сыщиков (Paul Martin, Shirley Martin, Simon Johnson, Manda Peterson, Tom Chambers, Ellie Stamford) | физ. 27–38 | прегены (статблок, background, possessions, legend; портреты) |
| Чистый лист сыщика | физ. 39–40 | не взято (см. ниже) |
| Реклама; задняя обложка | физ. 41–42 | atmosphere.json; аннотация — сценарий (summary, sources) |

## Не взято

- Чистый лист сыщика «Modern Era Investigator» (физ. 39–40) — бланк без данных.
- Реклама «Call of Cthulhu» (физ. 41) — не материал сценария.
- Мелкие безымянные статисты без статблока (приёмщик и медсестра больницы, врач, туристы в чайной, три велосипедиста,
  викарий, родители Гуртина, пропавший турист альтернативного начала) — описаны текстом в сценах и местах, своих записей нет.
- Упомянутые в предысториях прегенов люди (Чарли, Эдвард «Большой Тед» Робертс, Триша и Аллен Джонсоны), Роберт Томпсон,
  Джулия леди Рэглан — текстом в записях, своих записей нет.
- Места без описания, только упомянутые: полигон отходов за Эпплфордом, окружная психиатрическая лечебница, будущее
  водохранилище, Килберн (Северный Йоркшир), национальные парки — текстом.
- Картинки: копии раздаток в тексте глав (физ. 7, 11, 16), портрет Зелёного человека в «Dramatis Personae» (есть крупнее),
  украшения полей — atmosphere.json с причиной.

## Опечатки и сомнения

- Зелёный человек: ПЗ напечатаны 44*, по ВЫН 345 и ТЕЛ 105 — 45; исправлено по Р-36 (`errata` fixed, `corrections`).
- Схема спален на плане не подписана (оба «Bedroom»): № 9 — спальня Гуртина, № 10 — родителей, по тексту («за столовой» /
  «за гостиной») — вывод из текста (Р-41).
- Элли Стэмфорд: Мифы Ктулху 30% (Рассудок 50, максимум 69) — книга этого не объясняет; Средства на листе не вписаны.
- Число сессий: с. 4 — одна, задняя обложка — одна-две (в `quality.notes` сценария).
- Словесные мелочи без записи (Р-39): «Scrtich Scratch» (с. 8), «Arc of the Covenant» (с. 13), «literary throw» (с. 20);
  нет подзаголовка «Combat» у Молодого Джорджа (с. 21).
- Совет: город, где он заседает, книга не называет — `based_at` Эпплфорд выведен из текста (Р-41).
- Модель дробовика 12-го калибра у Старого и Молодого Джорджа не названа — ссылки на справочник оружия нет.

## Термины (English → русский)

| English | Русский |
|---|---|
| Scritch Scratch (сценарий) | «Цап-царап» |
| Scritch, scratch (в стишке) | цап-царап |
| Rat Catcher’s Rhyme | стишок крысолова |
| rat catcher | крысолов |
| Muscoby | Маскоби |
| Appleford | Эпплфорд |
| Old Gurteen / Gilbert Oswin Gurteen | старый Гуртин / Гилберт Освин Гуртин |
| Reginald Gurteen | Реджинальд Гуртин |
| Lucy Albright; Lucy’s Tea Shoppe | Люси Олбрайт; «Чайная Люси» |
| Joyce Deakins; Arthur Deakins | Джойс Дикинс; Артур Дикинс |
| Old George (George Fletcher, Sr.) | Старый Джордж (Джордж Флетчер-старший) |
| Young George (George Fletcher, Jr.) | Молодой Джордж (Джордж Флетчер-младший) |
| Paul Martin; Shirley Martin; Simon Johnson | Пол Мартин; Ширли Мартин; Саймон Джонсон |
| Manda (Amanda) Peterson; Tom Chambers; Ellie Stamford | Манда (Аманда) Питерсон; Том Чеймберс; Элли Стэмфорд |
| the Council | Совет (местный совет) |
| Appleford Historical Society | Эпплфордское историческое общество |
| The Golden Ram | паб «Золотой баран» |
| Rat Catcher’s Arms | паб «Герб крысолова» |
| St. Gertrude’s (Muscoby Village Church) | церковь Святой Гертруды |
| The Appleford Library and Museum | Эпплфордская библиотека и музей |
| Appleford Community Hospital | Эпплфордская районная больница |
| Old Gurteen’s Cottage | коттедж старого Гуртина |
| The Woods | лес за коттеджем Гуртина |
| rat bunting | крысиные «гирлянды» |
| The Black Book | Чёрная книга (семейная Библия Гуртинов) |
| Green Man (существо) / green man (изображение) | Зелёный человек / зелёный человек |
| foliate heads; uttering / disgorging heads | «лиственные головы»; «изрыгающие» головы |
| Rat Pack | крысиная стая |
| Overwhelm (mnvr) | Натиск (манёвр) |
| Vine Whip | удар лозой |
| Command Plants (mnvr) | Власть над растениями (манёвр) |
| Creeping Horror | ползучий ужас |
| Stone Watchers; A Mousey Connection | каменные стражи; мышиная связь |
| End Game; Conclusion; Rewards | Развязка; Заключение; Награды |
| Dramatis Personae | действующие лица |
| The Mouseman (Robert Thompson) | «Мышиный человек» (Роберт Томпсон) |
| Apollo Smintheus | Аполлон Сминфей |
| kissing gate | узкая калитка (на одного) |
| lych-gate | крытые ворота |
| fly-on-the-wall documentary | документальное реалити-шоу «муха на стене» |
| Cleaner (Scientist) / Cleaner (Former Actress) | уборщик (учёный) / уборщица (бывшая актриса) |
| Director/Producer; Cameraman (Photographer); Sound Engineer | режиссёр и продюсер; оператор (фотограф); звукорежиссёр |
| Art/Craft (Rat Catcher; Blacksmith; Storytelling) | Искусство/ремесло (крысолов; кузнечное дело; рассказывание историй) |
| Art/Craft (Acting; Photography; Photography (Film); Sound Recording; Baking and Cooking) | Искусство/ремесло (актёрское мастерство; фотография; киносъёмка; звукозапись; выпечка и кулинария) |
| Lore (Local Folklore) | Тайные знания (местный фольклор) |
