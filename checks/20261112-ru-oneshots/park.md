# «Парк развлечений» → база (часть park, Р-222)

Книга `park-razvlecheniy-ru` — «[RU 7e] Для печати. Парк развлечений (Кулькин Владимир).pdf», 32 страницы; автор Владимир
Кулькин, «НРИ Зов Ктулху, 7я ред» (обложка). Текст написан по-русски, английского оригинала нет.

- Редакция: 7-я, ядро (характеристики в процентах, Рассудок, Удача, бонусные/штрафные кубики); не Pulp. Эпоха — 1920-е (май 1921).
- Страницы: печатный номер «~ N ~» внизу каждой страницы совпадает с физическим (offset 0); с. 1 — обложка (номер «~ 1 ~»
  напечатан). С. 20–32 — картинки без текстового слоя (раздатки и портреты); текст раздаток прочитан с изображений.
- Записи: `kb/books/park-razvlecheniy-ru/` — сценарий, 17 сцен, 29 персонажей, 4 существа, 11 предметов, 11 раздаток,
  2 книги, 28 мест, 1 карта; общий город `kb/locations/agawam.json` (новый, Р-190: Агуэма в базе не было, других частей
  плана в нём нет).
- Карта: `app/maps/park-riverside-park.jpg` — **из цветной версии книги** («[RU 7e] Цветной. Парк развлечений (Кулькин
  Владимир).pdf», 31 с., с. 19, вложенная картинка 1600×1600 без пересжатия). В зарегистрированной версии для печати карты
  нет — только строка «Карта парка» в списке раздатки (с. 19). Метки — на все русские подписи (15) и три значка, которые текст
  однозначно называет (якорь — причал, шары — лавка шариков, вывеска «Restaurant» — ресторан); наложение проверено глазами.
- Предложения общих записей: `proposals-park.json` (1).

Префикс id ниже: `B/` = `park-razvlecheniy-ru/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка: «Парк развлечений», автор Кулькин Владимир | 1 | `B/scenario/park-razvlecheniy` (summary) |
| Парк развлечений (вступление, курсив) | 2 | сценарий (summary) |
| «Май 1921 г. штат Массачусетс, г. Агуэм…» | 2 | сценарий (summary); `coc:location:agawam`; `B/location/riverside-park` |
| История парка | 2 | `B/location/riverside-park` (history); `B/character/genri-perkins` |
| Хронология событий (1–3) | 2–3 | сценарий (keeper_info, hook) |
| Локации: 1. Пароход | 3 | `B/scene/parokhod-silviya`; `B/location/parokhod-silviya` |
| 2. Парк развлечений: Причал | 3–4 | `B/scene/prichal`; `B/location/prichal` |
| Центр парка | 4 | `B/location/tsentralnaya-ploshchad`; `B/scene/otkrytie-molnii` |
| Начало | 4–5 | `B/scene/otkrytie-molnii`; `B/scene/rassledovanie` (13:00) |
| Администрация парка | 5 | `B/location/administratsiya`; `B/scene/administratsiya`; `B/item/seyf-bukhgalterii` |
| Домики-вагончики работников | 5 | `B/location/domiki-rabotnikov`; `B/location/stolovaya` |
| Домик Сью Гранта | 5–6 | `B/location/domik-zavkhoza`; `B/scene/domik-syu-granta`; `B/item/kostyum-psa-khoui`, `dokumenty-rabotnikov`, `zapasnye-klyuchi` |
| Чулан в доме Сью | 6 | `B/location/domik-zavkhoza`; `B/item/drobovik-luk-i-strely` |
| Остальные домики | 6 | `B/scene/domiki-rabotnikov`; `B/item/cherep-materi-klouna`, `gazetnye-vyrezki-biglya`, `vintovka-slonoboy`; `B/tome/grimuar-vudu` |
| Окрестности вокруг парка | 6 | `B/location/mogily-salazarov`; `B/scene/domiki-rabotnikov` |
| Танцевальная площадка | 6 | `B/location/tantsevalnaya-ploshchadka`; `B/character/muzykanty-orkestra` |
| Ресторан парка | 6 | `B/location/restoran` |
| Аттракционы: тир | 6 | `B/location/tir`; `B/item/vintovka-tira`, `sled-botinka` |
| колесо обозрения (место финальной битвы) | 6–7 | `B/location/koleso-obozreniya`; `B/scene/koleso-obozreniya-prizrak` |
| лавка продавца шариков | 7 | `B/location/lavka-sharikov`; `B/character/rufus-uembe` |
| лавка продавца сладостей | 7 | `B/location/lavka-sladostey`; `B/character/bonni-lopes` |
| замок ужасов | 7–8 | `B/location/zamok-uzhasov`; `B/scene/zamok-uzhasov`; `B/creature/prizrak-meri-guver` |
| детская зона Киддиленд | 8 | `B/location/kiddilend`; `B/scene/kiddilend` |
| Павильон смеха «кривые зеркала» | 8 | `B/location/pavilon-smekha` |
| старые американские горки «Гончая» | 8 | `B/location/gonchaya` |
| новые большие американские горки «Молния» | 8 | `B/location/molniya` |
| Расследование: Полиция, судмедэксперты | 8–9 | `B/scene/rassledovanie` |
| Свидетели | 9 | `B/scene/rassledovanie`; `B/character/mett-donakhyu`, `rob-donalds`, `tom-kid`; `B/item/sled-botinka` |
| 3. Город Агуэм (Библиотека, Гостиница, Полицейский участок, Городской архив, Бар, Местный рынок) | 9 | `coc:location:agawam`; `B/scene/gorod-aguem`; `B/location/biblioteka`, `gostinitsa`, `politseyskiy-uchastok`, `gorodskoy-arkhiv`, `bar`, `rynok`; `B/item/ingredienty-rituala` |
| Транспорт | 9 | сценарий, таблица «Транспорт» |
| 4. Загородный дом | 9 | `B/location/dom-forte`; `B/scene/zagorodnyy-dom` |
| Возможные события: Нападение призрака в костюме пса Хоуи | 9–10 | `B/scene/napadenie-v-kostyume-khoui`; `B/creature/prizrak-v-kostyume-khoui` |
| Ритуал по призыву духа | 10 | `B/scene/ritual-prizyva-dukha`; `B/tome/grimuar-vudu`, `istoriya-afriki` |
| Обещание мальчику | 10 | `B/scene/zagorodnyy-dom` |
| Финал; Возможные действия: Пытаться остановить убийцу | 10 | `B/scene/final-pozhar` |
| Убежать из парка | 10–11 | `B/scene/ubezhat-iz-parka` |
| Арестовать Джереми Бигля | 11 | `B/scene/arestovat-biglya` |
| Призрак Абрахама будет являться знакомому сыщику, если погибнет | 11 | `B/creature/dukh-abrakhama`; `B/scene/arestovat-biglya` |
| Награды | 11 | сценарий (conclusion) |
| NPC (список) | 11 | сценарий (advice); персонажи и существа ниже; «Полицейские (5 человек)» и «Посетители (от 100 до 1500)» — текстом в сценарии и у парка |
| На корабле «Сильвия»: Уэйн Ховард, Дэнни Флорес, Паула Гриффин | 12 | `B/character/uein-khovard`, `denni-flores`, `paula-griffin` |
| Персонал парка: Генри Дж. Перкинс | 13 | `B/character/genri-perkins` |
| Джон Август Миллер | 13 | `B/character/dzhon-avgust-miller` |
| Сью Грант | 13 | `B/character/syu-grant` |
| Руфус Уэмбе | 14 | `B/character/rufus-uembe` |
| Джереми Бигль | 14 | `B/character/dzheremi-bigl` |
| Джонни Финн (мистер Хохотун) | 15 | `B/character/dzhonni-finn` |
| Лиззи Уолтер | 15 | `B/character/lizzi-uolter` |
| Пит Дастон | 15 | `B/character/pit-daston` |
| Алонзо Джованни | 16 | `B/character/alonzo-dzhovanni` |
| Пенни Прайс | 16 | `B/character/penni-prays` |
| Бонни Лопес | 16 | `B/character/bonni-lopes` |
| Посетители/свидетели: Кэсси Фортье | 17 | `B/character/kessi-forte` |
| Абрахам Перрис | 17 | `B/character/abrakham-perris` |
| Музыкант оркестра джазовой музыки (5) | 17 | `B/character/muzykanty-orkestra` |
| Случайный работник парка (10) | 17 | `B/character/rabotniki-parka` |
| Девушки-танцовщицы (5) | 18 | `B/character/devushki-tantsovshchitsy` |
| Прегены: Дэвин Джонс, Том Даккер, (альтернатива) Тэмми Даккер | 18 | `B/character/devin-dzhons`, `tom-dakker`, `temmi-dakker` |
| Раздатка (список) | 19 | сценарий (advice); строки — ниже |
| Карта парка | 19 | `B/map/riverside-park` (картинка из цветной версии) |
| Старые фото парка (открытка «Steamer Sylvia», горки, горки после пожара) | 20, 22, 23 | `B/handout/starye-foto-parka` |
| Фотографии персонажей | 20–23, 28, 30–32 | портреты указаны в `quality.notes` персонажей (см. ниже) |
| Карта батальной сцены на колесе обозрения | 29 | `B/handout/koleso-obozreniya-foto` |
| Гримуар-вуду (на французском) | 24 | `B/handout/grimuar-vudu-list`; `B/tome/grimuar-vudu` |
| Книга. История Африки и её обычаев | 24 | `B/handout/oblozhka-istoriya-kultov-afriki`; `B/tome/istoriya-afriki` |
| Результат осмотра места преступления. Убийство Софии Кид | 25 | `B/handout/svidetelstvo-o-smerti` |
| Убийство Мери Гувер 5 лет назад | 27 | `B/handout/gazeta-gigantskiy-proval` |
| Убийство Патрика и Линды Салазар | 26 | `B/handout/protokol-sherifa-1902` |
| Данные об убийствах в парках Массачусетса | — | `B/handout/ubiystva-v-parkakh` (листа в книге нет — пересказ, `incomplete`) |
| Данные о задержании Джереми Бигля | 27 | `B/handout/zaderzhanie-biglya` |
| Данные о лечении от наркомании Пита Дастона | 28 | `B/handout/lechenie-pita-dastona` |
| Данные о связях Лиззи Уолтер и итальянской мафии | 28 | `B/handout/svyazi-lizzi-uolter` |

## Портреты (картинки не перенесены)

Портреты и фото не подписаны; кто на них — по описаниям персонажей. Перенос картинок (`pipeline/art/add_images.py`,
`app/art/…`) — не в правах части, оставлен ведущему.

| Страница | Что на картинке | Запись |
|---|---|---|
| 20 | открытка «Steamer Sylvia» | `B/handout/starye-foto-parka` |
| 20 | клоун в колпаке; костюм пса | `B/character/dzhonni-finn`; `B/item/kostyum-psa-khoui` |
| 21 | блондинка; мальчик в коляске; колдун с сигарой; женщина в розовом парике | `kessi-forte`, `abrakham-perris`, `rufus-uembe`, `lizzi-uolter` |
| 22 | деревянные горки; старик в кепке; книга с застёжкой | `starye-foto-parka`; `dzheremi-bigl`; `B/tome/grimuar-vudu` |
| 23 | горки после пожара; толстяк в шляпе; худой мужчина в клетчатой рубашке | `starye-foto-parka`; `syu-grant`; `pit-daston` |
| 29 | колесо обозрения | `B/handout/koleso-obozreniya-foto` |
| 30 | мужчина в очках; девушка с мороженым; повар; официантка | `dzhon-avgust-miller`, `bonni-lopes`, `alonzo-dzhovanni`, `penni-prays` |
| 31 | капитан; дама с собачкой | `uein-khovard`, `paula-griffin` |
| 32 | мужчина с усами в синем костюме; двое мальчиков | возможно `genri-perkins` (не уверен); `mett-donakhyu` и `rob-donalds` |

## Не взято

- Цветные звёзды, молнии и неподписанные значки карты (клоун, тележка, качели, детские горки, «Riverside park» в
  углу, картинки-заставки) — не объяснены ни на карте, ни в тексте; меток нет.
- «Касса» и «Туалет» на карте — мест в тексте нет; метки ведут на запись парка с пояснением, отдельных записей нет.
- Бухгалтер администрации («староватая раздражительная женщина»), дирижёр оркестра, криминалисты и детективы, «Полицейские
  (5 человек)», «Посетители (от 100 до 1500)» — без имён и характеристик; остались текстом в местах, сценах и сценарии
  (записи с придуманными именами не заводились: механики у них нет).
- «Миллер и Бейкер» (бизнес Миллера), «Спрингфилд», «Олд-Сейбрук», река Коннектикут, лечебница Святого Павла, итальянская
  мафия / наркокартель Детройта — упомянуты без описания; остались текстом (кандидаты в записи — в отчёте).
- Портреты (с. 20–23, 28, 30–32) — см. таблицу выше; картинки в `images` не добавлены.

## Опечатки и сомнения

- Производные значения не по правилам (оставлены как напечатано, `errata`): Скорость Флореса, Перкинса, Миллера, Бигля,
  Финна, Кэсси, танцовщиц; ПЗ Руфуса, Бигля, Финна, танцовщиц; ПМ Финна; БкУ Абрахама (0 при Комплекции −2). Скорость 1
  у Абрахама — задумано (коляска).
- Финн: пятая метательных ножей «70(35/18)» → 14 (исправлено, Р-35); Маскировка напечатана дважды (60% и 20%).
- «СКР 9» (с. 10) понято как Скорость 9; «Биболиотека» (с. 9) — опечатка заголовка.
- Кэсси во вступлении названа вдовой (с. 2), на с. 17 — брошенной мужем.
- Имена: «Кэсси/Кесси Фортье», «Абрахам Перрис/Пэррис», «Пенни/Пэнни Прайс», «Мери/Мэри Гувер», «Генри Перкинс/Перкинсон»
  (раздатки) — варианты в `aliases`.
- Чей призрак нападает на колесе обозрения (ИНТ 45/МОЩ 50), книга не говорит; цифры те же, что у призрака Салазаров.
- Обложка книги из библиотеки: «История культов Афьики» — так напечатано.
