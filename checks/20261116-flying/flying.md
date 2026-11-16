# «We Dream of Flying» (we-dream-of-flying-en) — сверка заголовков (Р-134, Р-251)

Книга: Jim Phillips, «We Dream of Flying», SoC Press / Miskatonic Repository, 2023; 30 страниц PDF. Печатная
страница = физической (сдвиг 0): номера напечатаны на с. 2–9, на обложке и с. 10–30 номеров нет. Записи —
`kb/books/we-dream-of-flying-en/` (50: сценарий 1, сцены 12, персонажи 16, существа 1, места 10, предметы 3,
раздатки 4, карты 3). Русское название — «Мы грезим о полёте» (наш перевод).

Проверка, что сценария нет в базе под русским переводом: поиск «Накано», «Наоко», «Лунные коты», «Рейс 19»,
«Moon Cats», «Crystallizer» по `kb/` — русской версии нет; Кристаллизатор снов есть только как правило
`coc:rule:crystallizer-of-dream` и вид существа `coc:creature:guardian-of-crystallizers-of-dreams`.

Пути ниже — id без префикса `we-dream-of-flying-en/`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) «We Dream of Flying», Jim Phillips | физ. 1 | `scenario/we-dream-of-flying` (sources); картинка — у `creature/guardian-flight-19` (Страж несёт самолёт) |
| Credits | с. 2 | `scenario/we-dream-of-flying` (sources); логотип — атмосфера (`atmosphere.json`) |
| Introduction | с. 3 | `scenario/we-dream-of-flying` (summary, advice) |
| Keeper’s Background | с. 3 | `scenario/we-dream-of-flying` (keeper_info), `character/yuu-nakano`, `item/crystallizer-of-dreams`, `item/moon-cats-book`, `character/other-dreamers` |
| Call for Boarding | с. 3–4 | `scene/call-for-boarding`, `scenario/we-dream-of-flying` (hook), `location/lax-departure-gate` |
| Settling In | с. 4–5 | `scene/settling-in`, `location/upper-deck` |
| Trapped Between Worlds | с. 5–6 | `scene/trapped-between-worlds`, `location/aft-lavatory`, `creature/guardian-flight-19` |
| Meanwhile in the Waking World | с. 6–7 | `scene/meanwhile-in-the-waking-world`, `location/forward-crew-rest`, `location/cockpit`, `character/flight-19-crew` |
| The Empty Plane (и таблица потерь Рассудка) | с. 7 | `scene/the-empty-plane`; таблица «Потеря Рассудка оставшихся в мире яви» — `scenario/we-dream-of-flying` (tables); `character/flight-19-passengers` |
| Another Point of View | с. 7 | `scene/another-point-of-view`, спутники `character/*` |
| Finding Yuu | с. 7–8 | `scene/finding-yuu`, `item/yuu-backpack`, `item/moon-cats-book`, `location/coach-seats` |
| Yuu Nakano (статблок) | с. 8 | `character/yuu-nakano` |
| The Guardian | с. 8 | `creature/guardian-flight-19` (instance_of `coc:creature:guardian-of-crystallizers-of-dreams`), `scenario/we-dream-of-flying` (keeper_info) |
| Conclusion | с. 8 | `scenario/we-dream-of-flying` (conclusion) |
| Do Nothing | с. 8 | `scene/do-nothing` |
| Take the Crystalizer | с. 9 | `scene/take-the-crystallizer` |
| Leave the Plane Without Yuu | с. 9 | `scene/leave-the-plane-without-yuu` |
| Leave the Plane With Yuu | с. 9 | `scene/leave-the-plane-with-yuu` |
| Personal Sacrifice | с. 9 | `scene/personal-sacrifice` |
| Sanity Rewards | с. 9 | `scenario/we-dream-of-flying` (tables «Награды Рассудка», conclusion) |
| Handout 1 - Flight 19 | физ. 10 | `handout/handout-1-flight-19`, карта `map/flight-19-cutaway` (метки Upper Deck Access, Galleys / Lavatories, Coach Seats, Boeing 747 → `location/upper-deck-access`, `location/galleys-lavatories`, `location/coach-seats`, `location/flight-19`) |
| Handout 2 - First Class | физ. 11 | `handout/handout-2-first-class`, карта `map/first-class-upper-deck` (метка «747 - Upper Deck» → `location/upper-deck`) |
| Handout 3 - The Elder Sign | физ. 12 | `handout/handout-3-elder-sign`, карта `map/elder-sign-seating` |
| Handout 4 - The Moon Cats | физ. 13 | `handout/handout-4-moon-cats` (текст полностью + перевод) |
| Rajeev Pelagia (They / Them) | физ. 14, лист физ. 21 | `character/rajeev-pelagia` |
| Leonie Kaj (They / Them) | физ. 14, лист физ. 18 | `character/leonie-kaj` |
| Sylviane Radomil (She / Her) | физ. 15, лист физ. 22 | `character/sylviane-radomil` |
| Moriko Isamu (She / Her) | физ. 15, лист физ. 20 | `character/moriko-isamu` |
| Michal Pravin (He / Him) | физ. 16, лист физ. 19 | `character/michal-pravin` |
| Dario Madhavi (He / Him) | физ. 16, лист физ. 17 | `character/dario-madhavi` |
| Companions | физ. 23 | `character/juliette-uliana` (лист физ. 27), `character/marceli-neda` (28), `character/horymir-vavrinec` (26), `character/cho-emi` (25), `character/marshall-ilean` (29), `character/albina-fernande` (24) |
| (задняя обложка) SoC Press | физ. 30 | `scenario/we-dream-of-flying` (sources); картинка — атмосфера |

Листы сыщиков (физ. 17–22, 24–29) — заполненные листы наших дней без текста меток: значения сняты из
текстового слоя по координатам и сверены по изображению страниц; Удача на листе только обведена на шкале —
снята по изображению (Дарио 30, Леони 50, Михал 80, Морико 50, Раджив 60, Сильвиана 50, все спутники 50).
Половины и пятые доли всех значений на листах сходятся.

## Опечатки и расхождения книги

- Фамилия девочки: «Yuu Naoko» (с. 3) и «Yuu Nakano» (с. 5, 8, 9) — в записи Nakano, напечатанное — в `errata`
  и `aliases` (`character/yuu-nakano`).
- Статблок Юу: «Natural World 20$» — оформление, исправлено молча (Р-39); половины и пятые навыков не
  напечатаны — посчитаны.
- Раджив Пелагия: заголовок биографии — «Software Manager at a Mid-Size Tech Company», текст и лист — Chief
  Engineer (в описании записи).
- Написание артефакта: «Crystallizer of Dreams» (с. 3) и «Crystalizer» / «Crystializer» дальше — в `aliases`.
- Обложка книжки на рисунке (с. 4) — «Jane Randolph Carter», в тексте — «Jane R. Carter» (в описании предмета).
- С. 5: Страж несёт самолёт «with Neko and everyone else on board» — вероятно, имелась в виду Юу; в переводе
  — «со всеми, кто на борту» (сомнение, вопрос владельцу).
- Мелкие словесные опечатки без значения для игры («The fight is completely full», «Investors») не записаны (Р-39).
- Потеря Рассудка за Стража в сценарии (1d4/1d6 сквозь облака, 1d8/1d20 увидеть прямо) отличается от вида
  (1/1d6) — замысел книги (исполинский размер), отмечено в `quality.notes` существа, не опечатка.
- На листах спутников Ближний бой (драка) у Альбины, Джульетты и Маршалла и у всех шести сыщиков не
  заполнен (строка «Unarmed» без процентов) — в атаке шанс «—» с пометкой.

## Не взято

- Луна как место: тип «область» без `part_of` проверка не пускает, а места на Луне в книге не играются —
  Луна описана в сценах «Развязка: бездействие», «Покинуть самолёт с Юу» и в сценарии.
- Токио (пункт назначения), Мумбаи, Прага, Нью-Дели, Тбилиси — только текстом: общих записей городов нет,
  создавать их часть не вправе. Кандидат в общую запись — `coc:location:tokyo`.
- Кот Нэко, родители и бабушка Юу, автор книжки Джейн Р. Картер — без своих записей (упомянуты, в игре не
  участвуют): текстом в `character/yuu-nakano`, `item/moon-cats-book`.
- Номера мест (2A … 6C) на раздатках не напечатаны — меток на картах нет, список мест — в текстах.
- Иллюстрации с. 5 и 6 (безымянные пассажир у иллюминатора и парящее тело сновидца), логотипы с. 2 и 30 —
  атмосфера (`atmosphere.json`).

## Термины (English → русский)

| English | Русский |
|---|---|
| We Dream of Flying | Мы грезим о полёте |
| Flight 19 | рейс 19 |
| Crystallizer of Dreams / Crystalizer | Кристаллизатор снов (предмет — «Кристаллизатор снов Юу») |
| The Guardian | Страж (запись — «Страж Кристаллизатора («Мы грезим о полёте»)») |
| Waking World / waking world | мир яви |
| Dreamlands | Страна грёз |
| Dreaming world / Dream world | мир сновидений |
| Dreaming (skill) | Сновидение |
| Dream Lore | Тайные знания (сновидения) |
| Dreamer | сновидец |
| Elder Sign | Знак Старших богов |
| half-way state / in-between state | промежуточное состояние |
| The Moon Cats | «Лунные коты» |
| Cat Lore / Cat Care | Тайные знания (кошки) / Уход за кошками |
| upper deck / main passenger deck | верхняя палуба / главная пассажирская палуба |
| first class / coach | первый класс / эконом-класс |
| aft-most lavatory | кормовой туалет главной палубы |
| forward crew rest | носовой отсек отдыха экипажа |
| Upper Deck Access | лестница на верхнюю палубу |
| Galleys / Lavatories | кухни и туалеты |
| cockpit | кабина пилотов |
| gate attendant | сотрудник у выхода на посадку |
| traveling companion / Companions | спутник / спутники |
| Normal / Hard / Extreme roll | обычная / трудная / чрезвычайная проверка |
| opposed STR roll | встречная проверка СИЛ |
| Sanity Rewards | Награды Рассудка |
| Do Nothing / Take the Crystalizer / Leave the Plane Without (With) Yuu / Personal Sacrifice | Развязка: бездействие / отнять Кристаллизатор / покинуть самолёт без Юу (с Юу) / самопожертвование |
| Another Point of View | С другой стороны |
| Trapped Between Worlds | Между мирами |
| Meanwhile in the Waking World | Тем временем в мире яви |
| The Empty Plane / Finding Yuu / Settling In / Call for Boarding | Пустой самолёт / Поиски Юу / Обустройство на борту / Посадка на рейс 19 |

Имена: Yuu Nakano — Юу Накано; Neko — Нэко; Rajeev Pelagia — Раджив Пелагия; Leonie Kaj — Леони Кай;
Sylviane Radomil — Сильвиана Радомил; Moriko Isamu — Морико Исаму; Michal Pravin — Михал Правин; Dario
Madhavi — Дарио Мадхави; Juliette Uliana — Джульетта Ульяна; Marceli Neda — Марцели Неда; Horymír Vavřinec —
Горимир Вавржинец; Cho Emi — Тё Эми (по Поливанову; «Чо Эми» — псевдоним); Marshall Ilean — Маршалл Илеан;
Albína Fernande — Альбина Фернанде; Jane R. Carter — Джейн Р. Картер.
Заклинания сыщиков — общие записи: Песнь Тота, Околдовать жертву, Метаморфозы Горгорота, Мысленное внушение,
Затуманить память, Слова власти.
