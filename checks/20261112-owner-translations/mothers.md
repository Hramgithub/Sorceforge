# «Любовь матери» (Mothers Love) — сверка заголовков (часть «mothers», Р-223)

Источник — перевод владельца `2_Обработка\1920 Mothers Love` (книга `mothers-love-ru`, надёжный перевод): текст —
`Mothers_Love_Full_RU_v1.html`, страницы — `Pdf\Mothers_Love_Full_RU_v1.pdf` (15 с., печатная = физической; с. 1 — обложка,
с. 2 — оглавление). Дополнительно: `Раздатка.pdf` (4 с., английский оригинал раздаток, с. 178–181 оригинала),
`Прегены персонажей.pdf` (36 с., английские листы шести готовых сыщиков, с. 201–236 оригинала), `Газета.pdf` (6 с.,
английский реквизит «Arkham Advertiser»). Оригинал сценария не найден: числа перевода не сверены (Р-223); раздатки и
готовые сыщики сверены по английским страницам.

Записи: `kb/books/mothers-love-ru/` — 60 (сценарий 1, сцен 19, персонажей 20 — из них 6 готовых сыщиков, существ 2,
организаций 2, мест 4, предметов 6, раздаток 5, карта 1); картинка карты — `app/maps/mothers-innsmouth.jpg`.
Правки общих записей — `proposals-mothers.json` (52 предложения, пробный прогон `apply.py --dry-run` проходит).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Оглавление | 2 | `scenario/lyubov-materi` (источник) |
| Любовь матери (вступление) | 3 | `scenario/lyubov-materi` — `summary` |
| Информация для Хранителя | 3 | `scenario/lyubov-materi` — `keeper_info`; `character/tobias-sisk`, `organization/banda-lyagushka`, `item/sedan-dodge`, `item/dobycha-banka-ipsvicha` |
| Информация для сыщиков | 3 | `scenario/lyubov-materi` — `hook` |
| Блок-схема расследования | 3 | `scenario/lyubov-materi` — `advice` (пересказ схемы владельца) |
| Предыстория | 3–4 | `scenario/lyubov-materi` — `keeper_info`; `character/meri-sisk`, `character/tobias-sisk`, `location/piratskoe-ubezhishche`, `item/bronzovyy-kolokol`, `item/braslet-meri-sisk` |
| Создание атмосферы | 4–5 | `scenario/lyubov-materi` — `advice`; `creature/politseyskaya-ishcheyka`; друзья Сиска — `scene/konstebli-innsmuta` |
| Банда «Лягушка» | 5 | `organization/banda-lyagushka`; `map/karta-innsmuta` (иллюстрация «Карта Иннсмута» на этой странице) |
| Бюро расследований | 5 | `scenario/lyubov-materi` — `hook`; `character/dzhek-maloun`; `organization/politsiya-shtata-massachusets`; Бюро — предложения к `lightless-beacon-ru/organization/beacon-bureau-of-investigation` |
| Кооперативный банк Ипсвича | 5 | `scene/ograblenie-v-ipsviche`, `location/kooperativnyy-bank-ipsvicha`, `character/dzheffri-kinsella`; предложение к `coc:location:ipswich` |
| Поиск брошенного автомобиля и Дункана | 5–6 | `scene/broshennyy-avtomobil`, `item/sedan-dodge`, `character/eyb-dunkan`, `creature/khishchnyy-rakoobraznyy` |
| Документы «Материнская любовь» № 1 (раздатка H01) | 5–6 | `handout/h01-dokumenty-byuro` (+ английский оригинал, «Раздатка.pdf», с. 178) |
| Констебли Иннсмута | 6 | `scene/konstebli-innsmuta`; предложение к `pobeg-iz-innsmuta-ru/organization/gorodskaya-vlast-innsmuta` |
| Главный констебль Эндрю Мартин | 6 | `scene/konstebli-innsmuta`; предложения к `pobeg-iz-innsmuta-ru/character/endryu-martin` (абзац, вариант статблока) |
| Констебль Натан Бёрч | 7 | `scene/konstebli-innsmuta`; предложения к `pobeg-iz-innsmuta-ru/character/natan-berch` |
| Констебль Эллиот Роупс | 7 | `scene/konstebli-innsmuta`; предложения к `pobeg-iz-innsmuta-ru/character/elliot-roups` |
| Сведения полиции Иннсмута о Тобиасе Сиске | 7 | `scene/konstebli-innsmuta` (список дословно), `item/svidetelstva-o-smerti-siskov`, `character/iezekiil-sisk` |
| Доктор Роули Марш | 7 | `scene/doktor-rouli-marsh`; предложения к `pobeg-iz-innsmuta-ru/character/doktor-rouli-marsh` |
| Эзотерический Орден Дагона | 7 | `scene/orden-dagona`; профиль младших жрецов — `character/tipichnyy-zhitel-gibrid`; предложения к `coc:organization:esoteric-order-of-dagon` |
| Компания Marsh по очистке | 7 | `scene/affinazhnyy-zavod`; предложения к `coc:location:innsmouth-501-…` (псевдонимы) и `pobeg-iz-innsmuta-ru/character/dzheykob-marsh` |
| Банк East India Marine Merchants | 7 | `scene/bank-morskikh-torgovtsev`; предложение к `coc:location:innsmouth-210-…` (псевдонимы) |
| Гавань | 7 | `scene/gavan` |
| Отель Gilman House | 7–8 | `scene/otel-dom-gilmana`; предложения к `coc:location:innsmouth-703-…`, `pobeg-iz-innsmuta-ru/character/dzhordzh-khebbit`, `…/charlz-gilman` |
| Пользование телефоном | 8 | `scene/polzovanie-telefonom`; предложение к `pobeg-iz-innsmuta-ru/character/moyra-pirs` |
| События в городе | 8 | `scenario/lyubov-materi` — шаг «События в городе» |
| Местные дети | 8 | `scene/mestnye-deti` (песенка дословно) |
| Песнь шогготов | 8 | `scene/pesn-shoggotov` |
| Пропавший полицейский | 8 | `scene/propavshiy-politseyskiy` |
| Появление Уинна | 8–9 | `scene/poyavlenie-uinna`, `character/teddi-uinn` |
| Дом Сиска | 9 | `scene/dom-siska`, `location/dom-siska`; на карте — вычисленная метка |
| Раздатка H02: детский рисунок Тобиаса | 9 | `handout/h02-detskiy-risunok` (+ «Раздатка.pdf», с. 179) |
| Раздатка H03: карта «Пиратское убежище» | 9 | `handout/h03-karta-piratskoe-ubezhishche` (+ «Раздатка.pdf», с. 180) |
| Грейс Декерт | 10 | `scene/greys-dekert`, `character/greys-dekert` |
| Убежище | 10–11 | `scene/ubezhishche`, `scene/grot-i-kolokol`, `location/sklad-ueytov`, `location/piratskoe-ubezhishche`, `item/bronzovyy-kolokol`, `item/meshok-piratskikh-sokrovishch` |
| Раздатка H04: розыскной плакат Тобиаса Сиска | 11 | `handout/h04-rozysknoy-plakat` (текст — по «Раздатка.pdf», с. 181, наш перевод) |
| Оставшаяся банда «Лягушка» | 11 | `organization/banda-lyagushka`, `scene/ubezhishche` |
| Тобиас Сиск | 11 | `character/tobias-sisk` |
| Пёрл Каммайр | 11 | `character/perl-kammayr` |
| Роберто Сото | 11 | `character/roberto-soto` |
| Когда дым рассеется | 12 | `scene/kogda-dym-rasseetsya` |
| Браслет Мэри Сиск | 12 | `item/braslet-meri-sisk` |
| Награды и последствия | 12 | `scenario/lyubov-materi` — `conclusion` |
| Приложения / Статблоки | 12 | заголовки разделов; статблоки — ниже |
| Джек Мэлоун, старший агент BOI | 12 | `character/dzhek-maloun` |
| Типичный сотрудник полиции штата / агент BOI | 12 | `character/tipichnyy-politseyskiy-shtata` |
| Типичная полицейская ищейка | 12 | `creature/politseyskaya-ishcheyka` (instance_of `coc:creature:dog`) |
| Хищный ракообразный | 13 | `creature/khishchnyy-rakoobraznyy` (instance_of `pobeg-iz-innsmuta-ru/creature/plotoyadnye-rakoobraznye`) |
| Эндрю Мартин, главный констебль | 13 | предложение: вариант статблока в `pobeg-iz-innsmuta-ru/character/endryu-martin` |
| Натан Бёрч, хитрый старый констебль | 13 | предложение: вариант в `…/natan-berch` |
| Эллиот Роупс, грубый констебль | 13 | предложение: вариант в `…/elliot-roups` |
| Доктор Роули Марш, удручённый врач | 13 | предложение: вариант в `…/doktor-rouli-marsh` |
| Роберт Марш, преданный верховный жрец Дагона | 13 | предложение: вариант в `…/robert-marsh` |
| Джейкоб Марш, дружелюбный управляющий заводом | 14 | предложение: вариант в `…/dzheykob-marsh` |
| Типичный житель-человек | 14 | `character/tipichnyy-zhitel-chelovek` |
| Типичный житель-гибрид (и гибриды-жрецы) | 14 | `character/tipichnyy-zhitel-gibrid` |
| Тедди Уинн, отчаянно пытается покинуть город | 14 | `character/teddi-uinn` |
| Грейс Декерт, отвергнутая возлюбленная | 14 | `character/greys-dekert` |
| Мэри Сиск, встревоженная мать, глубоководная | 15 | `character/meri-sisk` (instance_of `coc:creature:deep-one`) |
| Тобиас Сиск, гибрид глубоководного | 15 | `character/tobias-sisk` |
| Пёрл Каммайр, испуганная будущая мать | 15 | `character/perl-kammayr` |
| Роберто Сото, не желает сдаваться | 15 | `character/roberto-soto` |
| Иллюстрация «Карта Иннсмута» | 5 | `map/karta-innsmuta`, `app/maps/mothers-innsmouth.jpg` (2400×1855) |
| «Раздатка.pdf» (с. 178–181 оригинала) | — | `handout/h01…h04` (английский текст и сверка) |
| «Прегены персонажей.pdf»: Angela May Bastable | 201–206 | `character/anzhela-beystebl` |
| — Carl Etheridge | 207–212 | `character/karl-eteridzh` |
| — Conrad T. Franklin | 213–218 | `character/konrad-franklin` |
| — Fr. Michael Calhoun | 219–224 | `character/otets-maykl-kalkhun` |
| — Johnny Logan | 225–230 | `character/dzhonni-logan` |
| — Rhoda Goldstein | 231–236 | `character/roda-goldsteyn` |
| «Газета.pdf»: Arkham Advertiser, 11 сентября 1928 | 1–6 файла | `handout/arkham-advertiser-1928` (пересказ полос) |

## Не взято

- Картинки (обложка IMG_01, церковь IMG_02, Мэри с ребёнком IMG_04, «Убежище: подземная угроза» IMG_05, улица IMG_06,
  раздатки H01–H04, портрет Грейс `Images\NPC\NPC01_…`): поле `images` требует копий в `app/art/`, которые этой части
  не принадлежат. Пути к оригиналам — в `quality.notes` раздаток; добавить через `pipeline/art/add_images.py` при сведении.
  Папок `Images\NPC` и `Images\Diagrams` (портрет Грейс, блок-схема SVG) в папке владельца нет — HTML ссылается на них.
- Текст «Газета.pdf» дословно: шесть полос английского реквизита, со сценарием (апрель 1927 года) не связан
  (номер от 11 сентября 1928 года); взят пересказ заголовков. Вопрос владельцу — нужна ли газета в базе дословно.
- Страницы «Strange Symbols & Diagrams Found» и «Notes & Frantic Scribblings» листов готовых сыщиков — пустые бланки.
- Безымянные мелочи без механики: рабочий на лестнице в банке, свидетели ограбления, гостиница Ипсвича (командный пункт
  Малоуна), бостонский офис Бюро, Историческое общество Ньюберипорта (записи нет), трое продвинутых гибридов третьего
  этажа «Дома Гилмана» — остаются текстом сцен.
- Псевдоним «Assembly Hall» для Ратуши Иннсмута (213) не предложен: отождествление — вывод из текста; в сцене и
  предмете указано как вывод (Р-41).

## Сомнения и опечатки

- Раздатка H01 в переводе расходится с английским оригиналом: Сото «26» (оригинал и статблок — 28), Уинн сбил
  «15-летнего» мальчика (оригинал — 13-летнего). Записано в `errata` раздатки, Сото и Уинна.
- Половины и пятые исправлены (Р-35): полиция штата 55% (22/9 → 27/11; 22/9 подходит к 45%, Р-77), Уинн дробовик
  40% (20/5 → 20/8), Сото пистолет 60% (30/10 → 30/12); у готовых сыщиков — Этеридж язык 80 (40/14 → 40/16),
  Голдстейн пистолет 45 (27/09 → 22/9) и Скрытность 60 (39/12 → 30/12).
- У Бэйстебл и Голдстейн драка в таблице оружия (40%) не совпадает с навыком (50% и 37%).
- Типичный житель-гибрид: Скорость 8 при СИЛ и ЛВК больше ТЕЛ (по правилам 9) — как напечатано.
- Полицейская ищейка: потеря Рассудка 1/1d6 — вероятно, ошибка вёрстки; как напечатано.
- Фамилия агента: «Малоун» (текст) / «Мэлоун» (статблок).
- Мэри Сиск: возраст «9,529» — как напечатан.
- Перевод называет золотоаффинажный завод «Нефтеперерабатывающим заводом Марша» (refinery) — псевдоним предложен с пометкой.
- `parse_uncertain` по заданию нужен на всех записях с числами, но `tools/check.py` требует его ровно у записей с
  `errata` (Р-141); флаг стоит только там, а «оригинал не найден, числа не сверены (Р-223)» — в `quality.notes`.
