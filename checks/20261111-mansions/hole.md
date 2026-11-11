# «Девятнадцатая лунка» («Особняки безумия. За закрытыми дверями», `osobnyaki-bezumiya-ru`) — сверка переноса (часть hole)

Источник — официальное русское издание (Hobby World), скан без текстового слоя: текст — распознавание
`.cache/ocr/osobnyaki-bezumiya-ru/NNN.txt` (tesseract, 200 dpi), каждое число, кость и статблок сверены по изображению
страницы (`pages.py image`, 110–200 dpi; Р-213). Английский текст 7e в библиотеке отсутствует (английская книга — 6e),
поэтому `name.en` поставлен только там, где он напечатан или общеизвестен (Thistledown — сноска на с. 143; Алистер Маккензи,
герцог Монтроз, Данди; виды существ).

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 5 «Девятнадцатая лунка» (Стюарт Бун) | 143–179 | 144–180 |
| «Материалы для игроков»: «Девятнадцатая 1–3», карта окрестностей, план подвала | 214–218 | 215–219 |

Смещение на всех проверенных страницах — **печатная = физическая − 1** (143→144, 152→153, 162→163, 172→173, 176→177,
179→180, 214→215, 218→219). Печатные с. 180–181 (физ. 181–182) — уже раздатки «Мистера Корбитта», не этой части.

## Заголовки книги

`…/` = `osobnyaki-bezumiya-ru/`; все записи части — с префиксом `hole-`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 5. Девятнадцатая лунка (вступление) | 143 | сценарий `…/scenario/hole-nineteenth-hole` (summary) |
| Информация для Хранителя | 143–144 | сценарий: keeper_info; `…/character/hole-arthur-macmillan`, `-crystal-macmillan`, `-alister-mackenzie`; `…/location/hole-thistledown`, `-crow-wood-hall` |
| Сноска «Англ. Thistledown — пух чертополоха» | 143 | `…/location/hole-thistledown` (`name.en`) |
| Как всё было на самом деле | 144–145 | сценарий: keeper_info; `…/character/hole-donald-gilmore`, `-james-lackey`, `-duke-of-montrose`; `…/item/hole-lackey-device` |
| Как сейчас обстоят дела | 145 | сценарий: keeper_info; `…/creature/hole-dimensional-shambler`; `hole-thistledown` |
| Вовлечение сыщиков | 145–146 | сценарий: hook; сыновья `…/character/hole-albert-macmillan`, `-charles-macmillan`, `-gordon-macmillan` |
| Материал «Девятнадцатая 1» (в главе) | 146 | `…/handout/hole-1-scotsman` |
| Навыки для новых сыщиков | 146 | сценарий: advice |
| Действующие лица | 146 | сценарий: advice |
| Артур Эдвард Макмиллан, 64 года | 146–147 | `hole-arthur-macmillan` (background, legend) |
| Кристал Лорен Макмиллан, 58 лет | 147 | `hole-crystal-macmillan` |
| Дональд Харрисон Гилмор, 49 лет | 147–148 | `hole-donald-gilmore` (возраст — errata) |
| Джеймс Роберт Лэки, 46 лет | 148 | `hole-james-lackey` |
| Кэмерон Нэрн, 52 года | 148 | `…/character/hole-cameron-nairn` |
| Джеральд Китинг, 55 лет | 148–149 | `…/character/hole-gerald-keating` |
| Одри Грант, 48 лет | 149 | `…/character/hole-audrey-grant` |
| Тереза Далкит и Кэти Макдональд, 16 и 17 лет | 149 | `…/character/hole-teresa-dalkeith`, `hole-katie-macdonald` |
| Питер Крейг, 37 лет | 149 | `…/character/hole-peter-craig` |
| Гордон Килбёрн, 45 лет | 150 | `…/character/hole-gordon-kilburn` |
| Завязка: первый удар | 150 | сцена `…/scene/hole-journey` |
| Дорога в Данди и Кроу-Вуд-Холл | 150 | сцена `hole-journey` |
| Из Америки или Европы | 150–151 | сцена `hole-journey`; город `coc:location:dundee` |
| Хранителю на заметку: валюта | 151 | сцена `hole-journey` |
| Из других частей Великобритании | 151 | сцена `hole-journey`; ссылка `coc:location:london` |
| Из Данди в Кроу-Вуд-Холл | 151 | город `coc:location:dundee` (описание); `…/location/hole-dundee-motorcars`; сцена `hole-journey` (errata направления) |
| Прибытие в Кроу-Вуд-Холл | 151–152 | сцена `…/scene/hole-arrival`; `…/location/hole-crow-wood-hall`, `hole-crow-wood-hall-garage` |
| Смена места действия (врезка) | 152 | сценарий: advice; `…/location/hole-dundee-environs` |
| Карта «Гольф-клуб «Тислдаун». Окрестности гольф-клуба» (ключ 1–5) | 152 | карта `…/map/hole-map-environs` (`app/maps/mansions-hole-environs.jpg`, 8 меток: 1–5, два леса, «В Данди»); места `hole-thistledown`, `-queens-head`, `-bell-farm`, `-mackintosh-farm`, `-crow-wood-hall`, `-crow-wood`, `-black-wood` |
| Разговор с Кристал Макмиллан (и три заметки для Хранителя) | 152–153 | сцена `hole-arrival`; `…/item/hole-humber`; `…/character/hole-milton` |
| Прислуга Кроу-Вуд-Холла | 154 | сцена `…/scene/hole-servants` |
| Джеральд Китинг (дворецкий) | 154–155 | сцена `hole-servants`; `hole-gerald-keating` |
| Одри Грант (экономка и кухарка) | 155 | сцена `hole-servants` |
| Тереза Далкит и Кэти Макдональд (горничные) | 155 | сцена `hole-servants`; `…/item/hole-crumpled-notes` |
| Питер Крейг (садовник) | 155 | сцена `hole-servants`; `…/item/hole-crossley`; леса `hole-crow-wood`, `hole-black-wood` (Чёрный Джейми) |
| Гордон Килбёрн (лакей) | 155–156 | сцена `hole-servants` |
| Дальнейшее расследование | 156 | `hole-dundee-environs`; шаги сценария |
| Паб «Голова королевы» | 156 | `…/location/hole-queens-head`; `…/character/hole-henry-adams`, `-margery-adams`, `-gregor-adams` |
| Разговор с Кэмероном Нэрном | 156–157 | сцена `…/scene/hole-talk-nairn`; `…/item/hole-nairn-keys` |
| Разговор с рабочими | 157–158 | сцена `…/scene/hole-talk-workers`; `…/character/hole-jones`, `-macdonald-mason`, `-abernethy`, `-gemmel` |
| Прогулка в Вороньем или Чёрном лесу (с заметкой для Хранителя) | 158 | сцена `…/scene/hole-woods`; `hole-crow-wood`, `hole-black-wood` |
| Посещение фермы Макинтошей или Беллов | 158 | сцена `…/scene/hole-farms`; `hole-mackintosh-farm`, `hole-bell-farm`; `…/character/hole-dugal-mackintosh` |
| Поездка в Данди | 158 | `coc:location:dundee` (описание); сцена `hole-talk-police` (псевдоним) |
| Разговор с полицейскими | 158–159 | сцена `…/scene/hole-talk-police`; `…/location/hole-dundee-police`; `…/character/hole-william-black`, `-michael-mcandrew` |
| Университетский колледж или библиотека Данди | 159–160 | сцена `…/scene/hole-library-research`; `…/location/hole-university-college`, `hole-dundee-library` |
| Осмотр «Тислдауна» | 160–161 | сцена `…/scene/hole-approach`; `hole-thistledown`; `hole-crossley` |
| Ложные следы (врезка; ложные следы 1–3) | 160 | сценарий: таблица «Ложные следы» (+ errata даты); `…/character/hole-mary-conlon`, `-john-campbell`, `-james-netherwell`, `-david-netherwell` |
| Поле для гольфа | 161 | `…/location/hole-golf-course`; `hole-thistledown` (history) |
| Хижина садовника и генератор (с заметкой для Хранителя) | 161 | `…/location/hole-gardeners-hut`; `…/item/hole-starter-relay`; сцена `hole-field-anomalies` |
| Сцены на поле | 161 | сцена `…/scene/hole-field-anomalies` |
| Возможные эфирные и межпространственные аномалии: Межпространственные помехи, Искры света, Газовый вихрь, Пространственный барьер, Вспышка в эфире | 161–163 | сценарий: таблица «Возможные эфирные и межпространственные аномалии»; сцена `hole-field-anomalies` |
| Поле «Тислдаун» в цифрах; Названия и характеристики лунок (таблица) | 162 | `hole-golf-course`: таблица «Названия и характеристики лунок» (сценарий — ссылкой `from`) |
| Игра в гольф в «Тислдауне» | 162 | `hole-golf-course` (описание) |
| Здание клуба «Тислдаун» | 163 | `…/location/hole-clubhouse` |
| Первый этаж клуба | 163 | `hole-clubhouse` (описание); комнаты первого этажа |
| Вход и вестибюль | 163–164 | `…/location/hole-entrance-hall`; сцена `…/scene/hole-entrance-hall`; `…/item/hole-toolbox` |
| Холл | 164 | `…/location/hole-hall` |
| Гольф-лавка | 164 | `…/location/hole-golf-shop`; сцена `…/scene/hole-golf-shop` |
| Главный холл | 164 | `…/location/hole-main-hall` |
| Женская раздевалка (с заметкой о шёпоте) | 164–165 | `…/location/hole-ladies-changing-room`; сцена `…/scene/hole-ladies-changing-room` |
| Женская душевая | 165 | `…/location/hole-ladies-showers` |
| Мужская раздевалка (с заметкой о бродящих) | 165–166 | `…/location/hole-mens-changing-room`; сцена `…/scene/hole-mens-changing-room` |
| Послания из эфира (врезка) | 165 | сцена `…/scene/hole-messages-from-aether` |
| Мужская душевая | 166 | `…/location/hole-mens-showers`; сцена `hole-mens-changing-room` |
| Спуск в подвал | 166 | `…/location/hole-basement-stairs`; сцена `…/scene/hole-basement-stairs` |
| Второй этаж клуба | 166 | `hole-clubhouse` (описание) |
| Библиотека/переговорная (с заметкой о гравитации) | 166–167 | `…/location/hole-library` (errata 6 м / 4,3 м); сцена `…/scene/hole-library` |
| Ресторан/бальный зал (с заметкой о пузыре) | 167 | `…/location/hole-ballroom`; сцена `…/scene/hole-ballroom` |
| Гостиная | 168 | `…/location/hole-lounge`; сцена `…/scene/hole-lounge` |
| Кабинет и склад (с заметкой о планах) | 168 | `…/location/hole-office`; сцена `…/scene/hole-office`; `…/item/hole-solicitors-letters`; `…/character/hole-harold-clemens` |
| Бар | 168 | `…/location/hole-bar` |
| Служебное помещение | 168 | `…/location/hole-staff-room`; сцена `…/scene/hole-staff-room` |
| Вестибюль | 169 | `…/location/hole-upper-vestibule` |
| Кухня | 169 | `…/location/hole-kitchen`; сцена `…/scene/hole-kitchen` |
| Кладовая | 169 | `…/location/hole-pantry`; сцена `…/scene/hole-pantry` |
| Подвал клуба | 169 | `…/location/hole-basement` |
| Склад (1) (с заметкой о морозе) | 169, 172 | `…/location/hole-1-storeroom`; сцена `…/scene/hole-storeroom` |
| Материал «Девятнадцатая 2» (в главе) | 170 | `…/handout/hole-2-reconstruction-plan`; карта `…/map/hole-map-plan-1928` (`app/maps/mansions-hole-plan-1928.jpg`, 29 меток на подписи помещений, лестниц и этажей) |
| Материал «Девятнадцатая 3» (в главе) | 171 | `…/handout/hole-3-plan-1903`; карта `…/map/hole-map-plan-1903` (`app/maps/mansions-hole-plan-1903.jpg`, 31 метка) |
| План «Подвал гольф-клуба «Тислдаун»» (ключ 1–9) | 172 | карта `…/map/hole-map-basement` (`app/maps/mansions-hole-basement.jpg`, 9 меток); места `hole-1-storeroom` … `hole-9-boiler-room` (8 — прибор в лаборатории) |
| Вход в подвал (2) | 172 | `…/location/hole-2-basement-entrance`; сцена `hole-storeroom` |
| Щитовая (3) (с заметкой об ударе током) | 172–173 | `…/location/hole-3-electrical-room`; сцена `…/scene/hole-electrical-room` |
| Винный погреб (4) | 173 | `…/location/hole-4-wine-cellar`; сцена `…/scene/hole-wine-cellar` |
| Тайный ход (5) | 173 | `…/location/hole-5-secret-passage`; сцена `…/scene/hole-secret-quarters` |
| Жилище Гилмора и Лэки (6) | 173 | `…/location/hole-6-living-quarters`; сцена `hole-secret-quarters`; `…/item/hole-gilmore-books` |
| Лаборатория Гилмора и Лэки (7, 8) (с заметкой) | 173–174 | `…/location/hole-7-laboratory`; сцена `…/scene/hole-laboratory`; `hole-lackey-device`; `…/item/hole-ram-head-cane` |
| Котельная и топка (9) | 174 | `…/location/hole-9-boiler-room`; сцена `…/scene/hole-boiler-room` |
| Откровения и решения | 174 | сцена `…/scene/hole-revelations` |
| Путешествия в эфир и за его пределы | 174–175 | сцена `…/scene/hole-into-the-aether` |
| Столкновения с тварями Мифов | 175 | сцена `…/scene/hole-mythos-encounters`; ссылка `coc:creature:ghost` |
| Завершение | 175 | сценарий: conclusion; шаг «Завершение и награды» |
| Награды | 175 | сценарий: conclusion (пять наград и штрафов Рассудка) |
| Персонажи и чудовища; Персонажи Хранителя | 176 | — |
| Кристал Лорен Макмиллан, 58 лет (статблок) | 176 | `hole-crystal-macmillan` (errata Уклонения) |
| Джеральд Китинг, 55 лет (статблок) | 176 | `hole-gerald-keating` |
| Одри Грант, 48 лет (статблок) | 176–177 | `hole-audrey-grant` |
| Тереза Далкит и Кэти Макдональд (статблок) | 177 | `hole-teresa-dalkeith`, `hole-katie-macdonald` (одна копия статблока у каждой; errata Уклонения) |
| Питер Крейг, 37 лет (статблок) | 177 | `hole-peter-craig` |
| Гордон Килбёрн, 45 лет (статблок) | 177 | `hole-gordon-kilburn` (Уклонение 0% → 30%, errata + corrections, вопрос владельцу) |
| Кэмерон Нэрн, 52 года (статблок) | 177 | `hole-cameron-nairn` |
| Артур Эдвард Макмиллан, 64 года (статблок) | 177 | `hole-arthur-macmillan` |
| Дональд Харрисон Гилмор, 48 лет (статблок) | 177 | `hole-donald-gilmore` (errata ПМ и возраста) |
| Джеймс Роберт Лэки, 46 лет (статблок) | 178 | `hole-james-lackey` |
| Существа и чудовища | 178 | — |
| Бродящий меж миров, космический скиталец | 178 | `…/creature/hole-dimensional-shambler` (`instance_of` `coc:creature:dimensional-shambler`) |
| Гончая Тиндала, санитар времени | 178–179 | `…/creature/hole-hound-of-tindalos` (`instance_of` `coc:creature:hound-of-tindalos`) |
| Материалы для игроков: материал «Девятнадцатая 1» | 214 | `hole-1-scotsman` (источник текста) |
| Материал «Девятнадцатая 2» | 215 | `hole-2-reconstruction-plan`; `hole-map-plan-1928` (источник) |
| Материал «Девятнадцатая 3» | 216 | `hole-3-plan-1903`; `hole-map-plan-1903` (источник) |
| Окрестности гольф-клуба «Тислдаун» — материал для игроков | 217 | `…/handout/hole-player-map-environs`; `hole-map-environs` (источник) |
| Подвал гольф-клуба «Тислдаун» — материал для игроков | 218 | `…/handout/hole-player-map-basement`; `hole-map-basement` (источник) |

Город — общая запись `kb/locations/dundee.json` (`coc:location:dundee`, новая, Р-190); места сценария — записи книги с
`part_of` на город (полиция, колледж, библиотека, прокат машин) и область «Окрестности Данди» `hole-dundee-environs` (Р-209).

## Записи (131)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `hole-nineteenth-hole` |
| scene | 33 | `hole-journey`, `-arrival`, `-servants`, `-talk-nairn`, `-talk-workers`, `-woods`, `-farms`, `-talk-police`, `-library-research`, `-approach`, `-field-anomalies`, `-entrance-hall`, `-golf-shop`, `-ladies-changing-room`, `-messages-from-aether`, `-mens-changing-room`, `-basement-stairs`, `-library`, `-ballroom`, `-lounge`, `-office`, `-staff-room`, `-kitchen`, `-pantry`, `-storeroom`, `-electrical-room`, `-wine-cellar`, `-secret-quarters`, `-laboratory`, `-boiler-room`, `-revelations`, `-into-the-aether`, `-mythos-encounters` |
| location | 44 | общий город `coc:location:dundee`; книги: `hole-dundee-environs`, `-dundee-police`, `-university-college`, `-dundee-library`, `-dundee-motorcars`, `-crow-wood-hall`, `-crow-wood-hall-garage`, `-queens-head`, `-bell-farm`, `-mackintosh-farm`, `-crow-wood`, `-black-wood`, `-thistledown`, `-golf-course`, `-gardeners-hut`, `-clubhouse`, 8 комнат первого этажа и спуск в подвал (`-entrance-hall`, `-hall`, `-golf-shop`, `-main-hall`, `-ladies-changing-room`, `-ladies-showers`, `-mens-changing-room`, `-mens-showers`, `-basement-stairs`), 9 помещений второго этажа (`-library`, `-ballroom`, `-lounge`, `-office`, `-bar`, `-staff-room`, `-upper-vestibule`, `-kitchen`, `-pantry`), `-basement`, `-1-storeroom` … `-7-laboratory`, `-9-boiler-room` |
| map | 4 | `hole-map-environs`, `hole-map-plan-1928`, `hole-map-plan-1903`, `hole-map-basement` |
| character | 32 | 11 со статблоками (`hole-arthur-macmillan`, `-crystal-macmillan`, `-donald-gilmore`, `-james-lackey`, `-cameron-nairn`, `-gerald-keating`, `-audrey-grant`, `-teresa-dalkeith`, `-katie-macdonald`, `-peter-craig`, `-gordon-kilburn`); 21 без статблока (`-william-black`, `-michael-mcandrew`, `-henry-adams`, `-margery-adams`, `-gregor-adams`, `-dugal-mackintosh`, `-jones`, `-macdonald-mason`, `-abernethy`, `-gemmel`, `-harold-clemens`, `-alister-mackenzie`, `-duke-of-montrose`, `-albert-macmillan`, `-charles-macmillan`, `-gordon-macmillan`, `-milton`, `-mary-conlon`, `-john-campbell`, `-james-netherwell`, `-david-netherwell`) |
| creature | 2 | `hole-dimensional-shambler`, `hole-hound-of-tindalos` |
| item | 10 | `hole-lackey-device`, `-starter-relay`, `-nairn-keys`, `-ram-head-cane`, `-crossley`, `-humber`, `-crumpled-notes`, `-solicitors-letters`, `-gilmore-books`, `-toolbox` |
| handout | 5 | `hole-1-scotsman`, `-2-reconstruction-plan`, `-3-plan-1903`, `-player-map-environs`, `-player-map-basement` |
| organization, tome, spell | 0 | организаций, книг Мифов и новых заклинаний в сценарии нет (книги Гилмора — научные, предмет) |

Картинки карт: `app/maps/mansions-hole-environs.jpg`, `mansions-hole-plan-1928.jpg`, `mansions-hole-plan-1903.jpg`,
`mansions-hole-basement.jpg` (вырезки 200 dpi; каждая метка проверена глазами по вырезке с нанесёнными точками).

## Опечатки и противоречия книги (в `errata`)

- Килбёрн: «Уклонение 0% (15/6)» (с. 177) — выпала цифра; в записи 30% (15/6), `fixed: true`, `corrections` с `ref: null` —
  **вопрос владельцу** (процент по Р-35/Р-77 меняет только владелец; можно вернуть 0%).
- Гилмор: возраст 49 («Действующие лица», с. 147) и 48 (статблок, с. 177); ПМ 13 при МОЩ 70 (ожидается 14).
- Кристал: Уклонение 25% при ЛВК 70 (по правилам 35%); горничные: 30% при ЛВК 65 (32%) — как напечатано (Р-161).
- Дорога из Данди: «поезд на северо-восток до Купар-Ангуса», «к северо-востоку от Данди … Фоулис» (с. 151), хотя
  Кроу-Вуд-Холл и клуб — к северо-западу от Данди (с. 143, 146) — в сцене `hole-journey`.
- Ложный след 2: «после открытия «Тислдауна» в 1909 году» (с. 160), а поле построено в 1901–1903, клуб закрыт в 1909
  (с. 143, 161) — в сценарии.
- Библиотека клуба: падение «с высоты 6 метров» (с. 167) при размере комнаты 4,3×4,3 м на обоих планах — в месте `hole-library`.
- Призрак полицейских: «в мужской раздевалке» (с. 159) и «именно здесь» в описании мужской душевой (с. 166) — в сцене `hole-talk-police`.

Мелкие словесные опечатки (например, «Слева от Гилмора и Люки», с. 173) не записывались (Р-39).

## Не взято

- Иллюстрации и подписи к ним (заставка главы с. 143; портреты персонажей и подписи «Кэмерон Нэрн», «Тереза Далкит и Кэти
  Макдональд», «Питер Крейг», «Гордон Килбёрн» на с. 147–151; «Кошмары Кристал Макмиллан» на с. 154; «Бродящие меж миров»
  на с. 166; «Гончая Тиндала в засаде» на с. 176): картинки в записи не добавлялись (`images` необязательно; `app/art/` —
  не в owns этой части).
- Старая ратуша, Епископальный собор святого Павла, Кэрд-Холл, институт Альберта, почтамт, неофициальный рынок в порту,
  вокзал Данди; Глазго, Эдинбург, залив Форт и мост, Лондонская и Северо-восточная железная дорога; посёлки Абернети и
  Фоулис; Купар-Ангус (стрелка на карте без метки); Эдинбургский университет; газеты «Скотсмен», «Таймс», «Геральд»;
  Индия — только упоминания: остались текстом в описаниях города, области, сцен и персонажей, записей нет.
- Безымянные: электрик из Данди, трое рабочих, видевших призрак в бальном зале, четверо констеблей, глава семейства Беллов,
  жена Нэрна, «другой слуга» — текстом в сценах; отдельных профилей в книге нет.
- Чёрный Джейми (легендарный чёрный пёс) и «женщина в белом» — текстом в описании лесов и в таблице ложных следов:
  в сценарии это слухи, не существа; связь с `coc:creature:spectral-black-dog` не ставилась (книга её не делает).
- Брошюра лорда Кельвина, книга Маккензи «Архитектура для гольфа», банка растворителя в мужской душевой, верёвки у груды
  досок, фотографии Макмиллана, три набора клюшек — текстом в предметах, местах и сценах.
- Внутренние помещения Кроу-Вуд-Холла (гостиная, библиотека, столовая, кухня, кабинет хозяина, спальни) — текстом в
  описании дома: плана дома в книге нет.
- Размеры на планах (длины стен) — в тексте раздаток «Девятнадцатая 2/3», меток на картах не получили.
- Алфавитный указатель книги (с. 220–224) — служебный.

## Предложения

`proposals-hole.json` — 1 предложение: `coc:creature:dimensional-shambler` — псевдоним «Бродящий меж миров» (официальный
перевод этой книги, Р-96). Пробный прогон `pipeline/integrate/apply.py --dry-run`: 1 правка ложится.

## Вопросы владельцу

1. Килбёрн, Уклонение: оставить исправление 0% → 30% (по напечатанным долям 15/6) или вернуть напечатанные 0%?
2. Английское название сценария («The Nineteenth Hole»?) и английские имена персонажей в русской книге не напечатаны —
   `name.en` у них пуст.
