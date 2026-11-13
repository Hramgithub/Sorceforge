# Ревизия базы знаний 2026-11-14

Скрипт `python tools/audit.py` (только чтение `kb/`); записей прочитано: 15742 (мест 3766, карт 350, персонажей 3241, сцен 2434). Все находки — в `findings.json` (класс, проверка, файл, id, суть, уверенность); здесь — первые 150 по каждой проверке, по книгам.

Уверенность: **high** — нарушение правила видно из данных; **medium** — вероятная ошибка, нужен взгляд; **low** — кандидат на просмотр, много законных случаев.

<!-- manual:start -->
## Главное (вывод ревизии 2026-11-14)

Снимок сделан, пока параллельно правились ссылки в `kb/`; числа могут немного сдвинуться — повторный прогон `python tools/audit.py` займёт около 5 секунд (этот блок он сохранит).

**Чисто (0 находок):** у меток нет несуществующих целей и координат вне 0–100; у каждой карты есть картинка в `app/maps/`; карт без меток и без пометки «меток нет» нет; у каждого места, кроме города, корабля и города сценария, есть `part_of`, циклов нет; нет городов с двумя «Окрестностями»; в Аркхэме и Иннсмуте ни одно место с номером не висит прямо под городом и не стоит в чужом районе (диапазоны районов выведены по сотням: Аркхэм 100–999, Иннсмут 100–1099; самопроверка с подставленными ошибками их ловит); домов, названных именем жителя, и псевдонимов «Семья …» не осталось (Р-82, Р-143); полных сирот (ни входящих, ни исходящих ссылок) нет. Разборы Р-82, Р-114, Р-163, Р-209 держатся.

**Что исправить в первую очередь (высокая уверенность, мало работы):**
- 3 симметричные связи записаны дважды (Р-114): Марла Слокам ↔ Даррелл Слокам (`arkham-en`), Эдвард Чандлер ↔ барон Гауптман (`griby-s-yuggota-ru`), Вероника Чедвик ↔ Тильда Смит-Чедвик (`sny-o-yaponii-ru`). Скриптом: оставить одну, `note_back` взять из второй.
- 2 повтора в списках: `refs` предмета `chernaya-kasseta-ru/item/chernaya-kasseta`, `where` сцены `keeper-rulebook-ru/scene/crimson-unconsidered-trifles`. Скриптом.
- 4 случая «два места одной книги под одним номером на одной карте»: Пикпюс и «Чердак Цанна» (№ 15, `tsarstvo-terrora-ru`; та же пара всплывает в `map.label_number` — метка «17» ведёт на Пикпюс, у которого № 15) и три трюма парохода «Президент Кулидж» (у трюмов и кают своя нумерация на одной карте — скорее законно, нужен взгляд).
- `pulp-cthulhu-en/character/the-goop`: персонаж с `form_of` → «Шоггот» (Р-82: `instance_of`).
- Джереми Кроуфорд в жителях Дома Кроуфордов с заметкой «умер в 1925 году» (Р-82, Р-101: в `refs`).

**Карты, по чтению (средняя уверенность):** 20 меток с номером, не совпадающим с `number` цели (сильнее всего — `lightless-beacon-ru/map/beacon-lighthouse`: 7 меток, «21» → дом смотрителя № 3, «22» → лестница № 9; `starter-dead-mans-stomp-ru` Гарлем; `autofagiya-ru` план 1 — метка «3» ведёт на каюты 103/113/121/124); ещё 21 такая же (низкая уверенность) — у карт сценариев, ведущих на общие места Аркхэма со своей нумерацией (`bless-the-beast-and-children-ru`, `sny-o-yaponii-ru`) — законно, но стоит проверить, что метка ведёт на то место. Карта `masks-of-nyarlathotep-en/map/australia-canning-basin` показывает Большую Песчаную пустыню (по `part_of` — Кункуджери), а её `location` — Порт-Хедленд. Метки карт Перу и Австралии ведут на места другого города (Пуно, Кункуджери) — карты страны; решить, в каком городе показывать такие карты. 8 мест района без метки на карте района: «Топливная лавка Иннсмута» (712) на карте Новой городской площади, 5 темниц Кремля, 2 места Гарлема (`starter-dead-mans-stomp-ru`, карта для игроков). 9 районов без мест (Найроби ×4, Бомбей ×2, Момбаса, Чжабэй, Чайнатаун Сан-Франциско).

**На чтение, только человеком:** 92 подписи `keeper_hint` с признаками спойлера (Р-209) — больше всего в Иннсмуте (21: камеры Й’ха-нтлеи и пещеры рифа с кубами, процентами и потерей Рассудка в подписи) и в Аркхэме (15: скидки и бонусы «+1d10» в подписях магазинов), дальше `osobnyaki-bezumiya-ru` (10). Слово «тайн» (38) часто законно («потайная лестница»), находки с кубами, процентами и Рассудком (27 medium) — почти всегда механика, которую надо унести в описание. 92 жителя-«умерших» (24 средней уверенности) — в основном ложные (умер муж, погибла мать); настоящие — нежить и призраки Янкылмы и Бобылёвых (законные жители) и Джереми Кроуфорд. 16 `form_of` у существ книг — почти все формы одного существа (законно по Р-79), кроме `the-goop`.

**Двойники (Р-154):** 34 кандидата из разных книг. Явные: 4 места Кампуса Аркхэма в `sny-o-yaponii-ru` (Юго-Западная подстанция, Западное и Восточное общежития, Дом президента) повторяют общие записи Аркхэма; «Первая пресвитерианская церковь» `bless-the-beast-and-children-ru` = `coc:location:arkham-817-…`; Eagle Lake (`fears-sharp-little-needles-en` и общая); персонажи «Побега из Иннсмута», которые есть в путеводителе Аркхэма (Микки Харриган, Люси Джеймс, Иезекиль Уоллес), Анна Тилтон (`lightless-beacon-ru` и «Побег»), Стивен Херст (общая и «Побег»), Мартин Фен (`arkham-en` и `naedine-s-tmoy-ru`), Эдмунд Хейл (`lightless-beacon-ru` и `pax-cthuliana-ru`), «Незримый конь» (`mify-hastura-ru` и общий). Остальное — совпадение имён (Р-99) или профили сценария (Р-75). Внутри книг — 17, из них заслуживают взгляда 8 (повторы сцен в `fears-sharp-little-needles-en`, «Пергамент призвать/отпустить зверя» ×2 в `griby-s-yuggota-ru`, две сцены «Scene 1: Travel» в `cursed-idol-of-manco-capac-en`).

**Номера в тексте без ссылки:** 91, из них 77 средней уверенности; почти всё можно добавить в `refs` скриптом по номеру после беглого просмотра: палубы «Президента Кулиджа» (28), Тотбург (№ 16, 17, 25 — дома людей), комнаты Лечебницы «Карнавала безумия» (10), храм «Проклятия Ганеши» (11), «Особняки безумия» (9).

**Сироты:** полных нет; 24 документа, предмета и организации, на которые никто не ссылается (13 — `arkham-en`: страницы «Advertiser 1922», таблица расстояний; это справочный материал гайда, а не сюжетная раздатка) — сцену, где их дают, ищет человек.

**Что можно исправлять автоматически:** `relations.sym_both`, `relations.list_dup`, `relations.self` (2 строки таблиц Масок), `grouping.under_city_in_range` / `grouping.wrong_district` (если появятся — диапазон района однозначен), большая часть `text_refs.number` (с номерами из 3+ цифр и при единственной цели на карте самого места). **Только чтением:** подписи, умершие жители, двойники, несовпадения номеров меток, места вне города карты, места без метки, пустые районы, сироты. `map.dup_label` (69, низкая) и `map.dup_target` (27, в основном планы зданий с подписями комнат) — почти все законны: тот же номер напечатан несколько раз (ванные, спальни, станции); достаточно `note`, если владелец хочет тишины в отчёте.

**Ограничения скрипта:** диапазоны районов выводятся только там, где номера мест идут по сотням (Аркхэм, Иннсмут); в городах «Масок» номера — ключи карт, и проверка «номер в чужом районе» там невозможна. Метки и номера сравниваются как строки после разбора («425-A» = «425», «OS115» = «115», «1–3» = 1, 2, 3). Спойлеры и умершие ищутся по словам — это список на просмотр, а не список ошибок.
<!-- manual:end -->

## Сводка

| Класс | Проверка | Находок | high / medium / low | Исправление |
|---|---|---:|---|---|
| **Карты** | | **146** | | |
| | Метка ведёт на несуществующую запись (`map.target_missing`) | 0 | 0 / 0 / 0 | авто: нет — нужна верная цель; но список короткий |
| | Координаты метки вне 0–100 (`map.coords`) | 0 | 0 / 0 / 0 | авто: нет — положение правится в редакторе меток (Р-160) |
| | Поле `location`/`shows` карты ведёт на несуществующую запись или не на место (`map.location_missing`) | 0 | 0 / 0 / 0 | авто: нет |
| | `location` карты — не город верхнего уровня: просмотрщик показывает карту только в разделе «Карта» города (`map.location_not_top`) | 0 | 0 / 0 / 0 | авто: да — `location` = город по цепочке `part_of`, изображаемое место — в `shows` |
| | Место, которое показывает карта (`shows`), не лежит в городе карты (`location`) (`map.location_shows`) | 0 | 0 / 0 / 0 | чтение: поправить `location` карты или `part_of` места; метки такой карты в «вне города» не повторяются |
| | Нет файла картинки карты в `app/maps/` (`map.image_missing`) | 0 | 0 / 0 / 0 | авто: нет — картинку надо вырезать из книги |
| | Карта без меток (и без пометки «меток нет» в `quality.notes`) (`map.no_spots`) | 0 | 0 / 0 / 0 | авто: нет — метки ставятся по распознаванию и глазами |
| | Разные метки одной карты ведут на одно место (не пара A/B, без `text`) (`map.dup_target`) | 27 | 0 / 3 / 24 | авто: нет — одна из меток ведёт не туда, нужна сверка по картинке |
| | Один и тот же номер дважды на карте, обе метки — на одно место, без `note` (`map.dup_label`) | 69 | 0 / 0 / 69 | авто: частично — если второй кружок на карте есть, достаточно `note` |
| | Метка карты указывает на место вне города карты (цепочка `part_of` не доходит до `location` карты) (`map.outside_city`) | 10 | 0 / 4 / 6 | авто: нет — либо `part_of` места, либо `location` карты |
| | Номер метки не совпадает с `number` записи, на которую она ведёт (`map.label_number`) | 25 | 0 / 4 / 21 | авто: нет — ошибка либо в цели, либо в `number` |
| | Место района с `number` без метки на карте района (`map.district_missing`) | 8 | 0 / 8 / 0 | авто: нет — метку надо найти на картинке; иногда место стоит не в том районе |
| | Метка карты района ведёт на место другого района (`map.other_district`) | 7 | 0 / 0 / 7 | чтение: соседние места на краю карты района законны; проверить, не стоит ли место не в том районе |
| **Группировка мест** | | **10** | | |
| | Место без `part_of`, а тип не город / корабль / город сценария (`grouping.no_part_of`) | 0 | 0 / 0 / 0 | авто: нет — родителя выбирает человек |
| | `part_of` на несуществующую запись, не на место или цикл (`grouping.bad_part_of`) | 0 | 0 / 0 / 0 | авто: нет |
| | У города больше одной области «Окрестности …» (`grouping.many_environs`) | 0 | 0 / 0 / 0 | полуавто: слить области в одну, места перевесить скриптом |
| | Место с номером прямо под городом, а номер в диапазоне района (`grouping.under_city_in_range`) | 0 | 0 / 0 / 0 | авто: да — `part_of` → район по номеру (диапазон района однозначен) |
| | Место с номером в районе, а номер — из диапазона другого района (`grouping.wrong_district`) | 0 | 0 / 0 / 0 | авто: да при однозначном диапазоне, иначе чтение |
| | Места одной книги с одинаковым `number` под одним городом (`grouping.same_number`) | 1 | 1 / 0 / 0 | чтение: двойник или опечатка номера |
| | Район без мест (`grouping.empty_district`) | 9 | 0 / 9 / 0 | чтение: удалить район или разнести в него места |
| **Подписи мест (keeper_hint)** | | **5** | | |
| | Подпись места похожа на спойлер (тайна, улика, проверка, культ, проценты, кубы) (`hint.spoiler`) | 5 | 0 / 1 / 4 | чтение: подпись переписывается в нейтральное «что это за место», остальное — в описание |
| **Связи** | | **104** | | |
| | Симметричная связь записана в обеих карточках (`relations.sym_both`) | 0 | 0 / 0 / 0 | авто: да — оставить одну, `note_back` взять из второй |
| | Ссылка или связь записи на саму себя (`relations.self`) | 0 | 0 / 0 / 0 | авто: да — убрать |
| | В `residents` — умерший или похороненный (по словам в заметке или в описании человека) (`relations.dead_resident`) | 91 | 0 / 23 / 68 | чтение: перенос из `residents` в `refs` после проверки текста |
| | `form_of` у именованной особи (персонаж или особь сценария) — должно быть `instance_of` (`relations.form_of_instance`) | 13 | 0 / 0 / 13 | полуавто: у персонажей — замена типа; у существ книг — чтение |
| | Здание названо именем человека или с псевдонимом «Семья …» (`relations.house_named`) | 0 | 0 / 0 / 0 | чтение: новое название «Дом …», старое — в `corrections` |
| | Повтор одного id в списке записи (`refs`, `residents`, `members` и т. п.) (`relations.list_dup`) | 0 | 0 / 0 / 0 | авто: да — убрать повтор (при разных `note` — объединить) |
| **Двойники (Р-154)** | | **41** | | |
| | Записи одного вида с одинаковым названием в разных книгах (или книга + общая), без `same_as` (`twins.cross_book`) | 24 | 0 / 9 / 15 | чтение: общая запись или законное совпадение имён (Р-99) |
| | Записи одного вида с одинаковым названием внутри одной книги (`twins.same_book`) | 17 | 0 / 8 / 9 | чтение: слить или переименовать |
| **Сироты** | | **0** | | |
| | Сюжетная запись книги, на которую никто не ссылается и которая сама никуда не ссылается (`orphans.isolated`) | 0 | 0 / 0 / 0 | чтение: привязать к сцене/месту или убрать |
| | Документ, предмет или организация книги, на которые никто не ссылается (сами ссылаются только на место или людей) (`orphans.unused`) | 0 | 0 / 0 / 0 | чтение: найти сцену или шаг сценария, где его дают, и сослаться оттуда |
| **Номера мест в тексте без ссылки** | | **15** | | |
| | В описании места или сцены назван номер места того же города, а ссылки на это место нет (`text_refs.number`) | 15 | 0 / 2 / 13 | полуавто: добавить id в `refs` по номеру (числа из 3+ цифр почти всегда верны) |

## Карты

### Метка ведёт на несуществующую запись — 0

Проверка `map.target_missing`; решения: Р-120. Исправление: авто: нет — нужна верная цель; но список короткий.

Находок нет.

### Координаты метки вне 0–100 — 0

Проверка `map.coords`; решения: Р-120. Исправление: авто: нет — положение правится в редакторе меток (Р-160).

Находок нет.

### Поле `location`/`shows` карты ведёт на несуществующую запись или не на место — 0

Проверка `map.location_missing`; решения: Р-120. Исправление: авто: нет.

Находок нет.

### `location` карты — не город верхнего уровня: просмотрщик показывает карту только в разделе «Карта» города — 0

Проверка `map.location_not_top`; решения: Р-120. Исправление: авто: да — `location` = город по цепочке `part_of`, изображаемое место — в `shows`.

Находок нет.

### Место, которое показывает карта (`shows`), не лежит в городе карты (`location`) — 0

Проверка `map.location_shows`; решения: Р-120. Исправление: чтение: поправить `location` карты или `part_of` места; метки такой карты в «вне города» не повторяются.

Находок нет.

### Нет файла картинки карты в `app/maps/` — 0

Проверка `map.image_missing`; решения: Р-120. Исправление: авто: нет — картинку надо вырезать из книги.

Находок нет.

### Карта без меток (и без пометки «меток нет» в `quality.notes`) — 0

Проверка `map.no_spots`; решения: Р-120, Р-206. Исправление: авто: нет — метки ставятся по распознаванию и глазами.

Находок нет.

### Разные метки одной карты ведут на одно место (не пара A/B, без `text`) — 27

Проверка `map.dup_target`; решения: Р-120, Р-155, Р-209. Исправление: авто: нет — одна из меток ведёт не туда, нужна сверка по картинке.

По книгам: _общие — 1, chernovodnyy-ruchey-ru — 4, dveri-vo-tmu-ru — 1, idol-tota-ru — 1, kholodnyy-urozhay-ru — 1, lager-sanni-ru — 1, masks-of-nyarlathotep-en — 1, mts-kharkov-37-ru — 1, osobnyaki-bezumiya-ru — 2, ostrov-luchezarnoy-nadezhdy-ru — 6, otel-skaylayn-ru — 1, starter-edge-of-darkness-ru — 2, tsarstvo-terrora-ru — 5

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/maps/innsmouth-smugglers-tunnels.json` | метки «D2», «D1» → одно место «Завалы с засадой» | low |
| chernovodnyy-ruchey-ru | `kb/books/chernovodnyy-ruchey-ru/maps/blackwater-karta-ferma-dzharvi.json` | метки «Пастбище для свиней», «Загон для свиней», «Выгребная яма», «Свинарник», «Хлев для коров» → одно место «Скотный двор Джарви» | low |
| chernovodnyy-ruchey-ru | `kb/books/chernovodnyy-ruchey-ru/maps/blackwater-karta-ferma-dzharvi.json` | метки «Сарай с утварью», «Бойня» → одно место «Прочие постройки фермы Джарви» | low |
| chernovodnyy-ruchey-ru | `kb/books/chernovodnyy-ruchey-ru/maps/blackwater-karta-ferma-karmodi.json` | метки «Туалет», «Фермерский дом» → одно место «Фермерский дом Кармоди» | low |
| chernovodnyy-ruchey-ru | `kb/books/chernovodnyy-ruchey-ru/maps/blackwater-karta-ferma-karmodi.json` | метки «Конюшня», «Загон для лошадей» → одно место «Конюшня Кармоди» | low |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/maps/darkness-map-3-lair.json` | метки «Горячий источник», «Шкуры и подушки» → одно место «Жилые комнаты» | low |
| idol-tota-ru | `kb/books/idol-tota-ru/maps/plan-lechebnitsy-arkhema.json` | метки «Палата», «Палата Артура Ормонда» → одно место «Палата Артура Ормонда» | low |
| kholodnyy-urozhay-ru | `kb/books/kholodnyy-urozhay-ru/maps/karta-regiona.json` | метки «РЕКА САМАРА», «SAMARA RIVER» → одно место «Река Самара» | medium |
| lager-sanni-ru | `kb/books/lager-sanni-ru/maps/lager-sanni.json` | метки «CLIFFS», «Обрыв», «CLIFFS» → одно место «Обрывы» | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/australia-commonwealth-of-australia.json` | метки «To Hong Kong and Shanghai», «To Hong Kong» → одно место «Гонконг» | medium |
| mts-kharkov-37-ru | `kb/books/mts-kharkov-37-ru/maps/karta-stantsii.json` | метки «5Б», «7» → одно место «Зернохранилище «Сталин»» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/memphis-map-house.json` | метки «20», «Подвал» → одно место «Подвал» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/memphis-map-house.json` | метки «21», «Чердак» → одно место «Библиотека» | low |
| ostrov-luchezarnoy-nadezhdy-ru | `kb/books/ostrov-luchezarnoy-nadezhdy-ru/maps/plan-stsilly.json` | метки «1», «1», «1. Шлюпки» → одно место «Шлюпки» | low |
| ostrov-luchezarnoy-nadezhdy-ru | `kb/books/ostrov-luchezarnoy-nadezhdy-ru/maps/plan-stsilly.json` | метки «2», «2», «2», «2. Пушки» → одно место «Пушки» | low |
| ostrov-luchezarnoy-nadezhdy-ru | `kb/books/ostrov-luchezarnoy-nadezhdy-ru/maps/plan-stsilly.json` | метки «3», «3», «3. Склад оружия» → одно место «Склад оружия» | low |
| ostrov-luchezarnoy-nadezhdy-ru | `kb/books/ostrov-luchezarnoy-nadezhdy-ru/maps/plan-stsilly.json` | метки «4», «4», «4. Склад провизии» → одно место «Склад провизии» | low |
| ostrov-luchezarnoy-nadezhdy-ru | `kb/books/ostrov-luchezarnoy-nadezhdy-ru/maps/plan-stsilly.json` | метки «5», «5», «5», «5», «5. Кают компания» → одно место «Кают-компания» | low |
| ostrov-luchezarnoy-nadezhdy-ru | `kb/books/ostrov-luchezarnoy-nadezhdy-ru/maps/plan-stsilly.json` | метки «6», «6. Каюта капитана» → одно место «Каюта капитана» | low |
| otel-skaylayn-ru | `kb/books/otel-skaylayn-ru/maps/plan-podvala.json` | метки «Резервуар для выращивания», «Больничные кровати», «Инвентарь» → одно место «Помещение с резервуаром» | low |
| starter-edge-of-darkness-ru | `kb/books/starter-edge-of-darkness-ru/maps/farm-players.json` | метки «Ферма: первый этаж», «Старая ферма» → одно место «Фермерский дом» | low |
| starter-edge-of-darkness-ru | `kb/books/starter-edge-of-darkness-ru/maps/farm.json` | метки «Ферма: первый этаж», «Старая ферма» → одно место «Фермерский дом» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1789-fenalik-cellar.json` | метки «Логово Феналика», «Зал со статуей» → одно место «Зал со статуей» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1789-fenalik-estate.json` | метки «16», «16», «16», «16», «16», «16», «16», «16», «16», «Комната для прислуги» → одно место «Комнаты прислуги» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1789-fenalik-estate.json` | метки «Гардероб», «Обувная» → одно место «Гардеробные» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1794-rigault-rooms.json` | метки «Операционный стол», «Операционная» → одно место «Операционная Риго» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1794-zann-attic.json` | метки «Чердак Цанна», «5 этаж (чердак)» → одно место «Комната на чердаке» | low |

### Один и тот же номер дважды на карте, обе метки — на одно место, без `note` — 69

Проверка `map.dup_label`; решения: Р-120. Исправление: авто: частично — если второй кружок на карте есть, достаточно `note`.

По книгам: _общие — 10, dveri-vo-tmu-ru — 1, fears-sharp-little-needles-en — 6, karnaval-bezumiya-ru — 2, lechebnitsa-ru — 1, masks-of-nyarlathotep-en — 25, ograblenie-po-arkhemski-ru — 1, osobnyaki-bezumiya-ru — 6, pogonya-v-poezde-ru — 1, pulp-cthulhu-en — 4, secrets-of-the-kremlin-en — 4, shadows-of-leningrad-en — 1, ten-nad-providensom-ru — 4, tsarstvo-terrora-ru — 3

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/maps/innsmouth-outskirts.json` | «1002» ×10 → «Удалённые фермерские дома» | low |
| _общие | `kb/maps/innsmouth-outskirts.json` | «1003» ×7 → «Фермерские дома» | low |
| _общие | `kb/maps/innsmouth-plan.json` | «106» ×4 → «Разные руины» | low |
| _общие | `kb/maps/innsmouth-plan.json` | «505» ×9 → «Заброшенные склады» | low |
| _общие | `kb/maps/innsmouth-plan.json` | «507» ×3 → «Рыбоупаковочные цеха» | low |
| _общие | `kb/maps/innsmouth-plan.json` | «802» ×22 → «Кирпичные и каменные склады» | low |
| _общие | `kb/maps/innsmouth-plan.json` | «901» ×6 → «Старые причалы» | low |
| _общие | `kb/maps/innsmouth-plan.json` | «903» ×4 → «Рыбацкие хижины» | low |
| _общие | `kb/maps/innsmouth-reef.json` | «C» ×2 → «Пещеры с барельефами» | low |
| _общие | `kb/maps/innsmouth-reef.json` | «B» ×2 → «Пещеры с глифами Р’льеха» | low |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/maps/darkness-map-2-catacombs.json` | «5» ×3 → «Пристанища выродков» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/maps/phlebotomy-ferguson-clinic.json` | «12» ×2 → «Задняя терраса/крыльцо» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/maps/phlebotomy-ferguson-clinic.json` | «27» ×2 → «Открытые пространства над нижним этажом» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/maps/waiting-new-life-clinic.json` | «1» ×8 → «Палаты пациентов» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/maps/walter-whispering-willow.json` | «L» ×2 → «Прачечная» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/maps/walter-whispering-willow.json` | «V» ×2 → «Комната ожидания для посетителей» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/maps/walter-whispering-willow.json` | «A» ×2 → «Архив» | low |
| karnaval-bezumiya-ru | `kb/books/karnaval-bezumiya-ru/maps/karta-igrokov.json` | «29» ×3 → «Портативные туалеты» | low |
| karnaval-bezumiya-ru | `kb/books/karnaval-bezumiya-ru/maps/karta-khranitelya.json` | «29» ×3 → «Портативные туалеты» | low |
| lechebnitsa-ru | `kb/books/lechebnitsa-ru/maps/plan-lechebnitsy.json` | «Комнаты пациентов» ×2 → «Больничное крыло» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/china-ho-fang-mansion.json` | «8» ×3 → «Гостевые комнаты особняка Хо Фана» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/china-ho-fang-mansion.json` | «13» ×13 → «Спальни особняка Хо Фана» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/china-ho-fang-mansion.json` | «14» ×5 → «Кладовые особняка Хо Фана» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/china-ho-fang-warehouse.json` | «4» ×2 → «Туалет склада Хо Фана» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/china-ho-fang-warehouse.json` | «1» ×4 → «Кабинеты склада Хо Фана» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/egypt-tunnels-below.json` | «B» ×2 → «Вход «B»» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/egypt-tunnels-below.json` | «C» ×2 → «Вход «C»» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/egypt-tunnels-below.json` | «D» ×2 → «Вход «D»» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-blue-pyramid-club.json` | «1» ×2 → «Лифт» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-blue-pyramid-club.json` | «5» ×2 → «Лестница» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-limehouse.json` | «S» ×14 → «Железнодорожные станции у Лаймхауса» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-misr-house.json` | «2» ×8 → «Спальни» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-misr-house.json` | «1» ×8 → «Ванные» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-misr-house.json` | «3» ×3 → «Кладовые» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-misr-house.json` | «7» ×6 → «Уборные» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-misr-house.json` | «17» ×9 → «Комнаты слуг» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-misr-house.json` | «16» ×10 → «Темница Миср-хауса» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-penhew-foundation.json` | «4» ×2 → «Библиотека Фонда» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-penhew-foundation.json` | «7» ×3 → «Кабинеты служащих» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-penhew-foundation.json` | «11» ×2 → «Комнаты приезжих учёных» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-penhew-foundation.json` | «15» ×4 → «Картотеки» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-penhew-foundation.json` | «17» ×2 → «Смотровые» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-plum-castle.json` | «23» ×8 → «Камеры темницы» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/england-shipley-house.json` | «2» ×3 → «Спальни дома Шипли» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/peru-ruins.json` | «8» ×2 → «Трупная яма» | low |
| ograblenie-po-arkhemski-ru | `kb/books/ograblenie-po-arkhemski-ru/maps/osobnyak-martinesa-2-etazh.json` | «Гостевая спальня» ×2 → «Гостевые спальни» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/code-map-estate.json` | «3» ×2 → «Автомобили» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/code-map-house.json` | «7» ×3 → «Лестница для слуг» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/code-map-house.json` | «16» ×2 → «Место отдыха» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/code-map-house.json` | «15» ×2 → «Ванные» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/code-map-house.json` | «12» ×8 → «Спальни» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/maps/corbitt-house.json` | «10» ×3 → «Пустые спальни» | low |
| pogonya-v-poezde-ru | `kb/books/pogonya-v-poezde-ru/maps/vagon-1-klassa-restoran-bagazhnyy-kabuz.json` | «Купол» ×2 → «Кабуз» | low |
| pulp-cthulhu-en | `kb/books/pulp-cthulhu-en/maps/slow-boat-lower-decks.json` | «7» ×5 → «Гостиная» | low |
| pulp-cthulhu-en | `kb/books/pulp-cthulhu-en/maps/slow-boat-upper-decks.json` | «5» ×2 → «Бассейн» | low |
| pulp-cthulhu-en | `kb/books/pulp-cthulhu-en/maps/slow-boat-upper-decks.json` | «7» ×3 → «Гостиная» | low |
| pulp-cthulhu-en | `kb/books/pulp-cthulhu-en/maps/slow-boat-upper-decks.json` | «13» ×2 → «Библиотека первого класса» | low |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «22» ×4 → «Кремлёвские стены» | low |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «34» ×2 → «Арсенал» | low |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «41» ×2 → «Старые пушки» | low |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «42» ×2 → «Пушки, захваченные у французской Великой армии в 1812 году» | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/maps/revolution-hospital.json` | «2-5» ×7 → «Палаты безумцев» | low |
| ten-nad-providensom-ru | `kb/books/ten-nad-providensom-ru/maps/milton-hotel-brochure.json` | «1» ×3 → «Конференц-зал» | low |
| ten-nad-providensom-ru | `kb/books/ten-nad-providensom-ru/maps/milton-hotel-brochure.json` | «3» ×2 → «Свадебный зал» | low |
| ten-nad-providensom-ru | `kb/books/ten-nad-providensom-ru/maps/milton-hotel.json` | «1» ×3 → «Конференц-зал» | low |
| ten-nad-providensom-ru | `kb/books/ten-nad-providensom-ru/maps/milton-hotel.json` | «3» ×2 → «Свадебный зал» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1789-fenalik-estate.json` | «13» ×3 → «Полости и отверстия в стене» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1789-fenalik-estate.json` | «15» ×2 → «Башни» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/1789-versailles.json` | «2» ×2 → «Парадный двор» | low |

### Метка карты указывает на место вне города карты (цепочка `part_of` не доходит до `location` карты) — 10

Проверка `map.outside_city`; решения: Р-120, Р-209. Исправление: авто: нет — либо `part_of` места, либо `location` карты.

По книгам: griby-s-yuggota-ru — 1, lokhmotya-korolya-ru — 6, masks-of-nyarlathotep-en — 3

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/maps/moon-peru.json` | метка «Lake Titicaca» → «Озеро Титикака» (masks-of-nyarlathotep-en/location/peru-lake-titicaca); город записи — Пуно, город карты — Лима | medium |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/maps/india-india-and-nepal.json` | метка «Тибет» → «Западный Непал и долина Кали-Гандаки» (lokhmotya-korolya-ru/location/india-western-nepal); город записи — Бенарес, город карты — Бомбей | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/maps/india-india-and-nepal.json` | метка «Гималаи» → «Западный Непал и долина Кали-Гандаки» (lokhmotya-korolya-ru/location/india-western-nepal); город записи — Бенарес, город карты — Бомбей | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/maps/india-india-and-nepal.json` | метка «Непал» → «Западный Непал и долина Кали-Гандаки» (lokhmotya-korolya-ru/location/india-western-nepal); город записи — Бенарес, город карты — Бомбей | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/maps/india-india-and-nepal.json` | метка «Pokhara» → «Покхара» (lokhmotya-korolya-ru/location/drakmar-pokhara); город записи — Бенарес, город карты — Бомбей | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/maps/india-india-and-nepal.json` | метка «Nautanwa» → «Наутанва» (lokhmotya-korolya-ru/location/india-nautanwa); город записи — Бенарес, город карты — Бомбей | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/maps/ship-voyage-to-bombay.json` | метка «Бомбей» → «Причал P&O в гавани Бомбея» (lokhmotya-korolya-ru/location/ship-bombay-dock); город записи — Бомбей, город карты — «Наместник Индии» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/australia-commonwealth-of-australia.json` | метка «City of the Great Race» → «Город Великой Расы» (masks-of-nyarlathotep-en/location/australia-city-of-the-great-race); город записи — Кункуджери, город карты — Перт | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/peru-lima.json` | метка «RUINS» → «Руины» (masks-of-nyarlathotep-en/location/peru-ruins); город записи — Пуно, город карты — Лима | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/maps/peru-lima.json` | метка «Lake Titicaca» → «Озеро Титикака» (masks-of-nyarlathotep-en/location/peru-lake-titicaca); город записи — Пуно, город карты — Лима | medium |

### Номер метки не совпадает с `number` записи, на которую она ведёт — 25

Проверка `map.label_number`; решения: Р-206, Р-209. Исправление: авто: нет — ошибка либо в цели, либо в `number`.

По книгам: bless-the-beast-and-children-ru — 9, sny-o-yaponii-ru — 5, starter-dead-mans-stomp-ru — 9, tsarstvo-terrora-ru — 2

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «4» → «Редакция «Аркхэм газетт»» с number «110» | medium |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «1» → «Полицейский участок Аркхэма» с number «228» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «2» → «Отель «Мискатоник»» с number «634» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «3» → «Редакция «Аркхэм Адвертайзер»» с number «131» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «6» → «Тауэр-билдинг» с number «119» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «7» → «Первая пресвитерианская церковь» с number «817» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «9» → «Управление аркхэмского трамвая» с number «224» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «10» → «Таксомоторная компания «Аркхэм кэб»» с number «236» (место другой книги: у карты может быть своя нумерация) | low |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/maps/karta-arkhema.json` | метка «11» → «Клуб «Мискатоник»» с number «804» (место другой книги: у карты может быть своя нумерация) | low |
| sny-o-yaponii-ru | `kb/books/sny-o-yaponii-ru/maps/miskatonic-campus.json` | метка «2» → «Юго-западная трансформаторная подстанция» с number «602» (место другой книги: у карты может быть своя нумерация) | low |
| sny-o-yaponii-ru | `kb/books/sny-o-yaponii-ru/maps/miskatonic-campus.json` | метка «18» → «Западное общежитие» с number «617» (место другой книги: у карты может быть своя нумерация) | low |
| sny-o-yaponii-ru | `kb/books/sny-o-yaponii-ru/maps/miskatonic-campus.json` | метка «19» → «Восточное общежитие» с number «620» (место другой книги: у карты может быть своя нумерация) | low |
| sny-o-yaponii-ru | `kb/books/sny-o-yaponii-ru/maps/miskatonic-campus.json` | метка «22» → «Дом президента университета» с number «622» (место другой книги: у карты может быть своя нумерация) | low |
| sny-o-yaponii-ru | `kb/books/sny-o-yaponii-ru/maps/miskatonic-campus.json` | метка «23» → «Библиотека Орна» с number «623» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | метка «4» → ««Смоллс Парадайз»» с number «5» | medium |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | метка «5» → «Гарлемская больница» с number «28» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | метка «6» → «Нью-Йоркская публичная библиотека (гарлемский филиал на 135-й улице)» с number «13» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | метка «7» → «Колумбийский университет» с number «20» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | метка «8» → «Собор Святого Иоанна Богослова» с number «26» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem.json` | метка «6» → «Гарлемская больница» с number «28» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem.json` | метка «8» → «Нью-Йоркская публичная библиотека (гарлемский филиал на 135-й улице)» с number «13» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem.json` | метка «9» → «Колумбийский университет» с number «20» (место другой книги: у карты может быть своя нумерация) | low |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem.json` | метка «10» → «Собор Святого Иоанна Богослова» с number «26» (место другой книги: у карты может быть своя нумерация) | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/paris-1789-1794.json` | метка «17» → «Кладбище Пикпюс» с number «15» | medium |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/maps/paris-1794.json` | метка «17» → «Кладбище Пикпюс» с number «15» | medium |

### Место района с `number` без метки на карте района — 8

Проверка `map.district_missing`; решения: Р-209. Исправление: авто: нет — метку надо найти на картинке; иногда место стоит не в том районе.

По книгам: _общие — 1, secrets-of-the-kremlin-en — 5, starter-dead-mans-stomp-ru — 2

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/maps/innsmouth-new-town-square.json` | «Топливная лавка Иннсмута» (712) — в районе «Современный торговый район», метки на карте района нет | medium |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «Темница 1» (1) — в районе «Кремль», метки на карте района нет | medium |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «Темница 2» (2) — в районе «Кремль», метки на карте района нет | medium |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «Темница 3» (3) — в районе «Кремль», метки на карте района нет | medium |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «Темница 4» (4) — в районе «Кремль», метки на карте района нет | medium |
| secrets-of-the-kremlin-en | `kb/books/secrets-of-the-kremlin-en/maps/kremlin-plan.json` | «Темница 5 — Библиотека Ивана Грозного» (5) — в районе «Кремль», метки на карте района нет | medium |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | «Старый гараж» (4) — в районе «Гарлем», метки на карте района нет | medium |
| starter-dead-mans-stomp-ru | `kb/books/starter-dead-mans-stomp-ru/maps/harlem-players.json` | «Комната Лироя Тёрнера» (7) — в районе «Гарлем», метки на карте района нет | medium |

### Метка карты района ведёт на место другого района — 7

Проверка `map.other_district`; решения: Р-209. Исправление: чтение: соседние места на краю карты района законны; проверить, не стоит ли место не в том районе.

По книгам: _общие — 7

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/maps/innsmouth-new-church-green.json` | метка «105» → «Руины с тоннелем» из района «Трущобы Северного побережья» | low |
| _общие | `kb/maps/innsmouth-new-church-green.json` | метка «103» → «Старая методистская епископальная церковь Эсбери» из района «Трущобы Северного побережья» | low |
| _общие | `kb/maps/innsmouth-new-church-green.json` | метка «501» → «Аффинажная компания Марша» из района «Прибрежная промышленная зона и торговые районы» | low |
| _общие | `kb/maps/innsmouth-new-town-square.json` | метка «503» → «Пожарная часть» из района «Прибрежная промышленная зона и торговые районы» | low |
| _общие | `kb/maps/innsmouth-new-town-square.json` | метка «605» → ««Сад» (бар и гриль)» из района «Южный жилой район» | low |
| _общие | `kb/maps/innsmouth-new-town-square.json` | метка «К 506» → «Опасный мост» из района «Прибрежная промышленная зона и торговые районы» | low |
| _общие | `kb/maps/innsmouth-new-town-square.json` | метка «К 604» → «Сквер на Элиот-стрит» из района «Южный жилой район» | low |

## Группировка мест

### Место без `part_of`, а тип не город / корабль / город сценария — 0

Проверка `grouping.no_part_of`; решения: Р-163, Р-189, Р-197. Исправление: авто: нет — родителя выбирает человек.

Находок нет.

### `part_of` на несуществующую запись, не на место или цикл — 0

Проверка `grouping.bad_part_of`; решения: Р-78. Исправление: авто: нет.

Находок нет.

### У города больше одной области «Окрестности …» — 0

Проверка `grouping.many_environs`; решения: Р-209. Исправление: полуавто: слить области в одну, места перевесить скриптом.

Находок нет.

### Место с номером прямо под городом, а номер в диапазоне района — 0

Проверка `grouping.under_city_in_range`; решения: Р-209, Р-80. Исправление: авто: да — `part_of` → район по номеру (диапазон района однозначен).

Находок нет.

### Место с номером в районе, а номер — из диапазона другого района — 0

Проверка `grouping.wrong_district`; решения: Р-209. Исправление: авто: да при однозначном диапазоне, иначе чтение.

Находок нет.

### Места одной книги с одинаковым `number` под одним городом — 1

Проверка `grouping.same_number`; решения: Р-206, Р-209. Исправление: чтение: двойник или опечатка номера.

По книгам: tsarstvo-terrora-ru — 1

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/locations/paris-picpus-cemetery.json` | № 15 в книге tsarstvo-terrora-ru, город «Париж»: «Кладбище Пикпюс» (kb/books/tsarstvo-terrora-ru/locations/paris-picpus-cemetery.json); «Чердак Цанна» (kb/books/tsarstvo-terrora-ru/locations/paris-zann-house.json); на одной карте: tsarstvo-terrora-ru/map/paris-1789-1794, tsarstvo-terrora-ru/map/paris-1794 | high |

### Район без мест — 9

Проверка `grouping.empty_district`; решения: Р-80, Р-209. Исправление: чтение: удалить район или разнести в него места.

По книгам: griby-s-yuggota-ru — 1, lokhmotya-korolya-ru — 2, masks-of-nyarlathotep-en — 6

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/locations/bay-chinatown.json` | район в «Сан-Франциско» без мест | medium |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/locations/india-bombay-colaba.json` | район в «Бомбей» без мест | medium |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/locations/india-bombay-fort.json` | район в «Бомбей» без мест | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/china-zhabei.json` | район в «Шанхай» без мест | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/kenya-indian-quarter.json` | район в «Найроби» без мест | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/kenya-industrial-area.json` | район в «Найроби» без мест | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/kenya-mombasa-old-town.json` | район в «Момбаса» без мест | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/kenya-private-estates.json` | район в «Найроби» без мест | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/kenya-somali-town.json` | район в «Найроби» без мест | medium |

## Подписи мест (keeper_hint)

### Подпись места похожа на спойлер (тайна, улика, проверка, культ, проценты, кубы) — 5

Проверка `hint.spoiler`; решения: Р-209. Исправление: чтение: подпись переписывается в нейтральное «что это за место», остальное — в описание.

По книгам: _общие — 2, fears-sharp-little-needles-en — 1, masks-of-nyarlathotep-en — 1, osobnyaki-bezumiya-ru — 1

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/locations/arkham-215-b-federal-bond-agency.json` | [процент] поручительство под залог: 10% наличными, 20% годовых | medium |
| _общие | `kb/locations/innsmouth-213-ratusha-innsmuta.json` | [секрет] Место городских собраний и архив; Юстис Элиот, сварливый муниципальный секретарь; список выборных должностных лиц округа Иннсмут | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/locations/phlebotomy-clinic-04-admin-office.json` | [секрет] кабинет секретаря | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/egypt-nyarlathotep-sanctum.json` | [тайн] потайной покой внутри Ломаной пирамиды | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/locations/crooked-house-19-secret-room.json` | [тайн] потайная комната | low |

## Связи

### Симметричная связь записана в обеих карточках — 0

Проверка `relations.sym_both`; решения: Р-114, Р-118. Исправление: авто: да — оставить одну, `note_back` взять из второй.

Находок нет.

### Ссылка или связь записи на саму себя — 0

Проверка `relations.self`; решения: Р-30. Исправление: авто: да — убрать.

Находок нет.

### В `residents` — умерший или похороненный (по словам в заметке или в описании человека) — 91

Проверка `relations.dead_resident`; решения: Р-82, Р-101. Исправление: чтение: перенос из `residents` в `refs` после проверки текста.

По книгам: _общие — 19, auktsion-ru — 1, autofagiya-ru — 1, bezymyannyy-tuman-ru — 2, chernovodnyy-ruchey-ru — 1, dveri-vo-tmu-ru — 4, fears-sharp-little-needles-en — 5, griby-s-yuggota-ru — 5, karnaval-bezumiya-ru — 3, kholodnyy-urozhay-ru — 1, kogda-zazhigayutsya-kostry-ru — 1, lechebnitsa-ru — 2, lokhmotya-korolya-ru — 3, malenkiy-klub-uzhasov-ru — 1, masks-of-nyarlathotep-en — 5, naedine-s-hellouinom-ru — 3, naedine-s-plamenem-ru — 2, novaya-zhizn-ru — 1, ograblenie-po-arkhemski-ru — 1, omerzitelnaya-pyaterka-ru — 1, osobnyaki-bezumiya-ru — 5, park-razvlecheniy-ru — 1, pod-zemlyoy-i-nad-zemlyoy-ru — 3, popalis-ru — 1, poselok-berezovyy-ru — 1, pustye-stranitsy-ru — 5, shadows-of-leningrad-en — 2, tri-koshmarnykh-vechera-ru — 3, tsarstvo-terrora-ru — 1, tumany-san-kristobal-ru — 3, vedomo-li-lyubvi-ru — 2, viral-en — 1, zabyvayushchiysya-ru — 1

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/locations/arkham-710-lewiston-house-hotel.json` | житель «Марша Льюистон»: «…Владелица отеля «Льюистон-хаус» (710). Как и покойный муж, очень набожна и слишком уж тревожится о «безбожной мол…» | medium |
| _общие | `kb/locations/arkham-905-szymanskis-boarding-house.json` | житель «Магдалена Шиманская»: «…Хозяйка пансиона Шиманской (905), вдова: её муж Якуб умер всего три года назад. Говорит с сильным польским акцентом и…» | medium |
| _общие | `kb/locations/innsmouth-1004-enni-pernell.json` | житель «Энни Пернелл»: «…овиком. Живёт одна на ферме с тех пор, как десять лет назад умер её муж Лестер. О гибридах Иннсмута знает немало, но видит т…» | medium |
| _общие | `kb/locations/innsmouth-podvodnaya-lodka-s-19.json` | житель «Рой Акер»: «…Нервный: его лучший друг погиб в декабре позапрошлого года, когда у Род-Айленда затонула п…» | medium |
| _общие | `kb/locations/totburg-forest.json` | житель «Бегильда»: «…вущих в лесу в двух часах ходьбы от Тотбурга (№ 29). Её муж погиб: дерево, которое они рубили, сломало ему ногу, и через пару…» | medium |
| _общие | `kb/locations/totburg-roman-ruins.json` | житель «Атильда»: «…Бывшая жена тэна Освина. По общему мнению, умерла в прошлом году, упав с лошади. Вместе с призраком Гая Монса…» | medium |
| _общие | `kb/locations/totburg-sigerics-house.json` | житель «Сигерик»: «…лафа, родом из Веоргоран-Честера (Вустера) выше по Северну, умерла прошлой зимой при родах. Сигерик отказался вернуть «утренни…» | medium |
| _общие | `kb/locations/yankylma.json` | житель «Матвей Бобылёв»: заметка «мертвец» | medium |
| _общие | `kb/locations/yankylma.json` | житель «Глафира Бобылёва»: заметка «мертвец» | medium |
| _общие | `kb/locations/yankylma.json` | житель «Жители Янкылмы»: заметка «остальные старики, живые и мёртвые» | medium |
| _общие | `kb/locations/arkham-305-thorne-house.json` | житель «Мелисса Торн»: «…т дневник с секретами Аркхэма. Муж проиграл их сбережения и умер, оставив ей только дом; займы постепенно превратились в под…» | low |
| _общие | `kb/locations/arkham-820-hartwell-home.json` | житель «Мортон Хартвелл»: «…адьбы Мортон и Джанин не провели врозь ни дня, и, когда она умерла, он не смог с ней расстаться. Несмотря на пышные похороны,…» | low |
| _общие | `kb/locations/clare-melford.json` | житель «Дик Блэр»: «…с Бэкона. Эдвардс узнаёт о смерти Дженнингса от Блэра; если погиб сам Блэр, об этом пишут газеты.…» | low |
| _общие | `kb/locations/clare-melford.json` | житель «Гарольд Дженнингс»: «…поги, тяжёлую куртку и плоскую кепку. Вдовец, с тех пор как умерла жена, сторонится людей; в деревне его считают чудаком («ско…» | low |
| _общие | `kb/locations/innsmouth-207-ezotericheskiy-orden-dagona.json` | житель «Роберт Марш»: «…ровее карает болтливых горожан — последним его гнев испытал покойный Зэдок Аллен. Виновных обычно арестовывают или поручают убит…» | low |
| _общие | `kb/locations/innsmouth-401-sintiya-dzhenks-gilman.json` | житель «Синтия Дженкс Гилман»: «…женщина, которую насильно выдали за гибрида. Её первый муж умер почти пятнадцать лет назад, вскоре после свадьбы; скорбящей…» | low |
| _общие | `kb/locations/innsmouth-orden-dagona-vnutri.json` | житель «Роберт Марш»: «…ровее карает болтливых горожан — последним его гнев испытал покойный Зэдок Аллен. Виновных обычно арестовывают или поручают убит…» | low |
| _общие | `kb/locations/perla.json` | житель «Сантина Мария Сальваторе»: «…сю жизнь прожила в Перле, вдова с тех пор, как 20 лет назад умер муж Паулу; в юности потеряла сыновей-близнецов от пневмонии…» | low |
| _общие | `kb/locations/totburg-unfurths-house.json` | житель «Унфурт»: «…е (№ 18), когда поселение ещё называлось Тотилл. Жена давно умерла, двое детей захвачены викингами и проданы в рабство в Конст…» | low |
| auktsion-ru | `kb/books/auktsion-ru/locations/dom-na-pervoy-folshtrasse.json` | житель «Клаус Хундерпрест»: «…ко лет назад (три года назад, по сведениям сыщиков) от рака умерла его любимая жена Ида; он ищет способ вернуть её к жизни и в…» | low |
| autofagiya-ru | `kb/books/autofagiya-ru/locations/kayuta-113.json` | житель «Глория Рейнбек»: «…аничной поездки — побывала в Лондоне, Париже и Кале. Её сын погиб на войне; у неё есть племянница, которую она не прочь сосва…» | low |
| bezymyannyy-tuman-ru | `kb/books/bezymyannyy-tuman-ru/locations/osobnyak-genri-pirsa.json` | житель «Генри Пирс»: «…Эннис Гибсон во время вечерней прогулки 14 августа; мать её умерла при родах, а «проходимец отец» отказался от неё и уехал в А…» | low |
| bezymyannyy-tuman-ru | `kb/books/bezymyannyy-tuman-ru/locations/zabroshennyy-dom-u-kladbishcha.json` | житель «Рене Пирс»: «…её увеличился, и вскоре она родила здоровую девочку, а сама умерла. Новорождённую забрали влиятельные культисты Пирсы и назвал…» | low |
| chernovodnyy-ruchey-ru | `kb/books/chernovodnyy-ruchey-ru/locations/blackwater-dom-geriga.json` | житель «Уолт Гериг»: «…у, чтобы ухаживать за «больной матерью». На самом деле мать умерла, когда он был маленьким, и похоронена на местном кладбище:…» | low |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/locations/lake-motel.json` | житель «Роберт Брофи»: «…ода. Из-за дурных слухов Брофи эмигрировали в США; Элизабет погибла в пути от «Зелёного гниения». В Кингспорте Уильям повёз отц…» | low |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/locations/lake-motel.json` | житель «Уильям Брофи»: «…ле долгого отсутствия и тоже покорился воле Гла’аки. Уильям умер в 25 лет — Гла’аки забрал его 58 лет назад, так что этому т…» | low |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/locations/lake-robert-bedroom.json` | житель «Роберт Брофи»: «…ода. Из-за дурных слухов Брофи эмигрировали в США; Элизабет погибла в пути от «Зелёного гниения». В Кингспорте Уильям повёз отц…» | low |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/locations/lake-william-bedroom.json` | житель «Уильям Брофи»: «…ле долгого отсутствия и тоже покорился воле Гла’аки. Уильям умер в 25 лет — Гла’аки забрал его 58 лет назад, так что этому т…» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/locations/hit-and-run-gareth-cabin.json` | житель «Джебедайя Гарет»: «…тей Миллерсберга. Был набожным человеком, пока его семья не погибла в автомобильной аварии; выжил только десятилетний внук Уиль…» | medium |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/locations/awto-ashton-law-office.json` | житель «Александр Эштон»: «…илось», и всячески вмешивается в расследование; если Хармон погиб, украдкой плюёт на тело. На визитке, найденной у Хармона: «…» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/locations/hit-and-run-methodist-church.json` | житель «Дональд Халости»: «…едайю: тот был добрым набожным человеком, пока его семья не погибла в аварии; с тех пор замкнулся и живёт за городом в хижине с…» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/locations/lights-out-university-library.json` | житель «Профессор Ормунд»: «…культе, ни о книге до того, как три недели назад весь культ погиб в огне. • Едва увидев книгу, он понял, что в ней заключена…» | low |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/locations/phlebotomy-ferguson-clinic.json` | житель «Лондон Синклер»: «…омочь скрыться (сцены «Изменение уравнения», «Ещё не совсем мертва!»). Если она сбежит, а сыщики причастны к вреду ей, они наж…» | low |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/locations/castle-gypsy-camp.json` | житель «Сарена»: «…Старая цыганка, много повидавшая за свои 85 лет. Муж давно умер; с тех пор она живёт только со слабоумным сыном Вехом в ярк…» | medium |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/locations/dreamer-irene-lemond-house.json` | житель «Ирен ЛеМонд»: «…Пола одна на небольшие средства, оставленные мужем, который умер очень молодым. Через две недели после исчезновения сына под…» | low |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/locations/dreamer-woods-estate-sanatorium.json` | житель «Пол ЛеМонд»: «…ным ребёнком в сельской местности недалеко от Буффало; отец умер очень молодым, и Пола растила мать, Ирен, на небольшие сред…» | low |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/locations/well-cornwallis-mansion.json` | житель «Джереми Корнуоллис»: «…дца перед особняком. По некрологу 4 июля 1891 года младенец умер при рождении; его гроб в фамильном склепе заполнен камнями.…» | low |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/locations/well-mansion-well.json` | житель «Джереми Корнуоллис»: «…дца перед особняком. По некрологу 4 июля 1891 года младенец умер при рождении; его гроб в фамильном склепе заполнен камнями.…» | low |
| karnaval-bezumiya-ru | `kb/books/karnaval-bezumiya-ru/locations/16-gadalka.json` | житель «Мадам Фортуна»: «…адшая сестра Симоны (Леди Сари), родилась в 1822 году; мать умерла через несколько минут после её рождения. В двенадцать лет (…» | low |
| karnaval-bezumiya-ru | `kb/books/karnaval-bezumiya-ru/locations/28-myortvaya-petlya.json` | житель «Джеральд Адамс»: «…д нужными звёздами, и провела над ней ужасные ритуалы; мать умерла, но родила; ребёнка воспитал член внутреннего круга. Приёмн…» | low |
| karnaval-bezumiya-ru | `kb/books/karnaval-bezumiya-ru/locations/40-vagonchik-ledi-sari.json` | житель «Леди Сари»: «…й Левеск, бежавшей в 1810 году с Корсики от культа Маззери; умерла в 1822 году при родах Авроры). Симона увлекалась театром, п…» | low |
| kholodnyy-urozhay-ru | `kb/books/kholodnyy-urozhay-ru/locations/ko3-15-dom-abramova.json` | житель «Дмитрий Петрович Абрамов»: «…пинает грязь и немелодично насвистывает. Знает, что Галина мертва, и думает, что это сделал Василий. Если спросить, как он се…» | low |
| kogda-zazhigayutsya-kostry-ru | `kb/books/kogda-zazhigayutsya-kostry-ru/locations/dom-eremina.json` | житель «Егор Димитриевич Еремин»: «…• Когда-то был женат на женщине, которую очень любил; жена скончалась от болезни несколько лет назад. О покойной жене отзывается…» | low |
| lechebnitsa-ru | `kb/books/lechebnitsa-ru/locations/komnata-1.json` | житель «Бланш Годдард Ричмонд»: «…ла; первый сеанс лишь убедит её, что персонал действительно мёртв; дальнейшие раскроют правду о гибели её детей и могут убеди…» | low |
| lechebnitsa-ru | `kb/books/lechebnitsa-ru/locations/komnata-4.json` | житель «Генри Адам Барбер III»: «…онности. Психоанализ: позволит ему осознать, что сотрудники мертвы; может вывести его из суицидального состояния. Физическое с…» | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/locations/house-chaugnar-faugn-cavern.json` | житель «Роберто Анзалоне»: «…): он становится новым спутником-проводником. Если Анзалоне умер, кровь для Врат берут у сыщика или с человеческого трупа. С…» | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/locations/springer-jennings-farm.json` | житель «Гарольд Дженнингс»: «…поги, тяжёлую куртку и плоскую кепку. Вдовец, с тех пор как умерла жена, сторонится людей; в деревне его считают чудаком («ско…» | low |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/locations/springer-railway-pub.json` | житель «Дик Блэр»: «…с Бэкона. Эдвардс узнаёт о смерти Дженнингса от Блэра; если погиб сам Блэр, об этом пишут газеты.…» | low |
| malenkiy-klub-uzhasov-ru | `kb/books/malenkiy-klub-uzhasov-ru/locations/chrevo-akhmkhlti.json` | житель «Стивен Смозерс»: «…— зловонное, гнилое, склизкое и почерневшее. Мать Смозерса умерла при его родах; отец, Алан, пьёт. Никто в школе, кроме Лайнх…» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/china-ho-fang-mansion.json` | житель «Хо Цзуси»: «…ка после того, как на одном из обрядов отца у неё на глазах погибла мать. Не выходит из своей комнаты в особняке, целыми днями…» | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/china-ho-tzu-hsi-room.json` | житель «Хо Цзуси»: «…ка после того, как на одном из обрядов отца у неё на глазах погибла мать. Не выходит из своей комнаты в особняке, целыми днями…» | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/australia-mackenzie-house.json` | житель «Роберт Б. Ф. Маккензи»: «…); в 1921 году они собирались обследовать место, но Макуирр умер от гриппа. Два-три года назад некий «мистер Хаустон» (Хасто…» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/kenya-neville-jermyn-house.json` | житель «Невилл Джермин»: «…сошедшего с ума в 1765 году; сын покойного Артура Джермина (умер в 1913 году в 43 года) из рассказа Лавкрафта «Факты, касающ…» | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/peru-hotel-espana.json` | житель «Петронила Купитина»: «…чёрную шаль и головной платок и ходит с тростью. Муж Анхель умер три года назад, и она одна держит отель, несмотря на годы:…» | low |
| naedine-s-hellouinom-ru | `kb/books/naedine-s-hellouinom-ru/locations/osobnyak-fon-raysht.json` | житель «Барон Бирлад Текучи фон Райшт»: «…дготовил к его приезду собственность и замок — и вскоре сам погиб (469); в 1943 году к нему в Салем собиралась «сестра» Дремл…» | low |
| naedine-s-hellouinom-ru | `kb/books/naedine-s-hellouinom-ru/locations/osobnyak-fon-raysht.json` | житель «Доктор Карри»: «…Балуется» тайнами разума и сотворения жизни — его раб Питер погиб в автокатастрофе за территорией замка и создан заново. Прик…» | low |
| naedine-s-hellouinom-ru | `kb/books/naedine-s-hellouinom-ru/locations/osobnyak-fon-raysht.json` | житель «Питер»: «…ый голем доктора Карри: полностью покорен своему создателю. Погиб в трагической автокатастрофе прямо за территорией замка на…» | low |
| naedine-s-plamenem-ru | `kb/books/naedine-s-plamenem-ru/locations/emberhead.json` | житель «Уиллард Арбогаст»: «…спускается с утёса (абз. 112, 141, 191). Безумен: «Эмберхед умер сорок лет назад… уничтоженный самими звёздами»; жители «воз…» | low |
| naedine-s-plamenem-ru | `kb/books/naedine-s-plamenem-ru/locations/peshchera-arbogasta.json` | житель «Уиллард Арбогаст»: «…спускается с утёса (абз. 112, 141, 191). Безумен: «Эмберхед умер сорок лет назад… уничтоженный самими звёздами»; жители «воз…» | low |
| novaya-zhizn-ru | `kb/books/novaya-zhizn-ru/locations/dom-charli.json` | житель «Норман Эдингтон»: «…двое детей — сын Бернард и дочь Шарлотта. Однажды Элизабет погибла в автокатастрофе; понимая, что нужно прокармливать троих де…» | low |
| ograblenie-po-arkhemski-ru | `kb/books/ograblenie-po-arkhemski-ru/locations/osobnyak-martinesa.json` | житель «Артур Мартинес»: «…ра и его прислуги. Слух, будто он отравил жену, — ложь: она умерла от инсульта.…» | low |
| omerzitelnaya-pyaterka-ru | `kb/books/omerzitelnaya-pyaterka-ru/locations/galantereya-gudmena.json` | житель «Ричард Гудмен»: «…езвозвратно утерян. Дома помог обратить своих дочерей; жена погибла, а дочери умерли от холода (см. Эшли Гудмен). Когда прибыли…» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/locations/code-house-3-servants-room-william.json` | житель «Клинт Дэвис»: «…ы хватало на себя и на папу. Когда Клинту было 13, его отец умер от болезни печени, и мальчик остался один. В Чикаго он неск…» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/locations/code-wellington-estate.json` | житель «Клинт Дэвис»: «…ы хватало на себя и на папу. Когда Клинту было 13, его отец умер от болезни печени, и мальчик остался один. В Чикаго он неск…» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/locations/corbitt-3-house.json` | житель «Бернард Корбитт»: «…стил мать в дом престарелых в Нью-Йорке (через три года она умерла) и с тех пор единолично владеет компанией. С тех пор он неи…» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/locations/corbitt-hart-house.json` | житель «Ребекка Уоллас»: «…ньонка мисс Харт (врезка «Рука помощи»). Муж Ребекки Уолтер умер от гриппа-испанки во время Мировой войны. Все её дети вырос…» | low |
| osobnyaki-bezumiya-ru | `kb/books/osobnyaki-bezumiya-ru/locations/memphis-house.json` | житель «Великий Мемфис»: «…лание — медленную и неуклюжую передачу психических образов. Покойный чародей постепенно возвращается, шаг за шагом порабощая тер…» | low |
| park-razvlecheniy-ru | `kb/books/park-razvlecheniy-ru/locations/domiki-rabotnikov.json` | житель «Джереми Бигль»: «…енных девушек. Работал в Риверсайд-парке 5 лет назад, когда погибла Мери Гувер. Ранее был осуждён за нападение в Бостоне: это б…» | low |
| pod-zemlyoy-i-nad-zemlyoy-ru | `kb/books/pod-zemlyoy-i-nad-zemlyoy-ru/locations/dom-bobylevykh.json` | житель «Матвей Бобылёв»: «…Один из старейших жителей деревни, давно мёртв; просыпается ближе к вечеру. Очень любит поболтать и покури…» | medium |
| pod-zemlyoy-i-nad-zemlyoy-ru | `kb/books/pod-zemlyoy-i-nad-zemlyoy-ru/locations/dom-bobylevykh.json` | житель «Глафира Бобылёва»: «…Одна из старейших жителей деревни, давно мертва; просыпается ближе к вечеру. Необщительна, но полна сил: ча…» | medium |
| pod-zemlyoy-i-nad-zemlyoy-ru | `kb/books/pod-zemlyoy-i-nad-zemlyoy-ru/locations/okhotnichya-izba.json` | житель «Бахтияр»: «…Шаман манси и самый старый житель деревни, мёртв уже три века. Единственный, кто знает о заточённом Куль-Оты…» | medium |
| popalis-ru | `kb/books/popalis-ru/locations/osobnyak-kenninga.json` | житель «Томас Кеннинг»: «…привлечёт знакомых преступников, чтобы те нашли книгу; если мёртв — полиция нашла тело и разыскивает убийц.…» | low |
| poselok-berezovyy-ru | `kb/books/poselok-berezovyy-ru/locations/dom-volynskogo.json` | житель «Григорий Артемьевич Волынский»: «…али условный срок. За два года до начала приключения у него умерла жена. В конце весны заказывал у продавщицы сельпо странные…» | low |
| pustye-stranitsy-ru | `kb/books/pustye-stranitsy-ru/locations/bernvud-kholl.json` | житель «Джеймс Мейнард»: «…Гриффита; опознан среди останков на пепелище Бернвуд-Холла. Погиб в пожаре Бернвуд-Холла в 1874 году вместе с Гриффитом и ост…» | medium |
| pustye-stranitsy-ru | `kb/books/pustye-stranitsy-ru/locations/bernvud-kholl.json` | житель «Зебедайя Уэстклифф»: «…ся торговца рыбой и морепродуктами, последователя Гриффита. Погиб в пожаре Бернвуд-Холла в 1874 году; его тело — одно из трёх…» | medium |
| pustye-stranitsy-ru | `kb/books/pustye-stranitsy-ru/locations/bernvud-kholl.json` | житель «Эдвард Торренс»: «…Призрак студента-математика, последователя Гриффита. Погиб в пожаре Бернвуд-Холла в 1874 году; его тело — одно из трёх…» | medium |
| pustye-stranitsy-ru | `kb/books/pustye-stranitsy-ru/locations/bernvud-kholl.json` | житель «Хаким Рухани»: «…теля Гриффита. Глубинной магией «Дурного глаза» не владеет. Погиб в пожаре Бернвуд-Холла в 1874 году; его тело — одно из трёх…» | medium |
| pustye-stranitsy-ru | `kb/books/pustye-stranitsy-ru/locations/bernvud-kholl.json` | житель «Карл Гриффит»: «…отказали ей, газеты отозвались иронически, в 1873 году она умерла от острой сердечной недостаточности. С шестью последователя…» | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/locations/orkonov-1-7-servants-quarters.json` | житель «Джона»: «…м, откуда он, Джона не помнит. Ответы Джоны: где был, когда умерла Шарлотта, — смешивал краски в башне, услышал крики на кухне…» | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/locations/orkonov-estate.json` | житель «Джона»: «…м, откуда он, Джона не помнит. Ответы Джоны: где был, когда умерла Шарлотта, — смешивал краски в башне, услышал крики на кухне…» | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/locations/glow-ferma-1-khizhina-bikerov.json` | житель «Джейкоб Бикер»: «…вету; в ссоре запер в спальне жену Эдди и забыл о ней — она умерла от голода. По телеграмме Бюро, у него есть записи об ареста…» | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/locations/glow-ferma-bikerov.json` | житель «Джейкоб Бикер»: «…вету; в ссоре запер в спальне жену Эдди и забыл о ней — она умерла от голода. По телеграмме Бюро, у него есть записи об ареста…» | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/locations/glow-khizhina-8-komnata-dzheykoba-i-eddi.json` | житель «Джейкоб Бикер»: «…вету; в ссоре запер в спальне жену Эдди и забыл о ней — она умерла от голода. По телеграмме Бюро, у него есть записи об ареста…» | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/locations/paris-rigault-rooms.json` | житель «Люсьен Риго»: «…луночи до рассвета режет мандалы в Катакомбах. После гибели похоронен на кладбище Пикпюс (с. 62, 68, 86).…» | low |
| tumany-san-kristobal-ru | `kb/books/tumany-san-kristobal-ru/locations/britanskoe-poselenie.json` | житель «Адам Тёрнер»: «…счезновением сына и винит в этом рыболюдей. Если Хью Марлоу мёртв, план ударить по холму из батареи предложит Адам, ссылаясь…» | low |
| tumany-san-kristobal-ru | `kb/books/tumany-san-kristobal-ru/locations/dom-adama.json` | житель «Адам Тёрнер»: «…счезновением сына и винит в этом рыболюдей. Если Хью Марлоу мёртв, план ударить по холму из батареи предложит Адам, ссылаясь…» | low |
| tumany-san-kristobal-ru | `kb/books/tumany-san-kristobal-ru/locations/dom-khudozhnika.json` | житель «Уильям Блейк»: «…ачинается кровавая охота. Если к этому времени художник уже мёртв, вместо него это делает Хью Марлоу. Адам Тёрнер подозревает…» | low |
| vedomo-li-lyubvi-ru | `kb/books/vedomo-li-lyubvi-ru/locations/kvartira-khetti.json` | житель «Хэтти Мэй»: заметка «живёт с Хайболом; покойный муж — Джон Мэй» | medium |
| vedomo-li-lyubvi-ru | `kb/books/vedomo-li-lyubvi-ru/locations/dom-na-uest-belmont-avenyu.json` | житель «Хэтти Мэй»: «…ошейник Хайбола, кинжал носит в сумочке. 14 февраля её муж погиб в Бойне в День святого Валентина, Хайбола забрала полиция.…» | low |
| viral-en | `kb/books/viral-en/locations/administrators-house.json` | житель «Анджело Руссо»: «…урной компанией, подсел на героин и вернулся в Перлу, когда умерла мать; совершил несколько краж, и его исчезновение особо не…» | low |
| zabyvayushchiysya-ru | `kb/books/zabyvayushchiysya-ru/locations/ferma-arturov.json` | житель «Оуэн Артур»: «…а и Итана; вдовец (на семейном фото в доме — он, оба сына и покойная жена, снимку всего пара лет). Около 5–6 вечера Артуры видят…» | medium |

### `form_of` у именованной особи (персонаж или особь сценария) — должно быть `instance_of` — 13

Проверка `relations.form_of_instance`; решения: Р-82, Р-79. Исправление: полуавто: у персонажей — замена типа; у существ книг — чтение.

По книгам: lokhmotya-korolya-ru — 1, masks-of-nyarlathotep-en — 3, park-razvlecheniy-ru — 1, ten-nad-providensom-ru — 2, tri-koshmarnykh-vechera-ru — 5, tsarstvo-terrora-ru — 1

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/creatures/carcosa-montague-edwards-unspeakable-possessor.json` | существо книги: `form_of` → «Монтегю Эдвардс» — особь или разновидность? | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/creatures/dream-dingoes.json` | существо книги: `form_of` → «Динго Грогана» — особь или разновидность? | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/creatures/million-favored-ones-leeches.json` | существо книги: `form_of` → «Миллион избранных» — особь или разновидность? | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/creatures/spawn-of-nyarlathotep-mother-aspect.json` | существо книги: `form_of` → «Отродье Ньярлатхотепа: облик отца» — особь или разновидность? | low |
| park-razvlecheniy-ru | `kb/books/park-razvlecheniy-ru/creatures/dukh-abrakhama.json` | существо книги: `form_of` → «Абрахам Перрис» — особь или разновидность? | low |
| ten-nad-providensom-ru | `kb/books/ten-nad-providensom-ru/creatures/ibnhotep-human-form.json` | существо книги: `form_of` → «Ибнхотеп» — особь или разновидность? | low |
| ten-nad-providensom-ru | `kb/books/ten-nad-providensom-ru/creatures/ibnhotep-protoshoggoths.json` | существо книги: `form_of` → «Ибнхотеп» — особь или разновидность? | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/creatures/pieces-golova.json` | существо книги: `form_of` → «Куски и Фрагменты, ожившие части тела» — особь или разновидность? | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/creatures/pieces-nogi.json` | существо книги: `form_of` → «Куски и Фрагменты, ожившие части тела» — особь или разновидность? | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/creatures/pieces-ruki.json` | существо книги: `form_of` → «Куски и Фрагменты, ожившие части тела» — особь или разновидность? | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/creatures/pieces-tulovishche.json` | существо книги: `form_of` → «Куски и Фрагменты, ожившие части тела» — особь или разновидность? | low |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/creatures/pieces-vnutrennosti.json` | существо книги: `form_of` → «Куски и Фрагменты, ожившие части тела» — особь или разновидность? | low |
| tsarstvo-terrora-ru | `kb/books/tsarstvo-terrora-ru/creatures/seed-bastille-thing.json` | существо книги: `form_of` → «Итакуа» — особь или разновидность? | low |

### Здание названо именем человека или с псевдонимом «Семья …» — 0

Проверка `relations.house_named`; решения: Р-82, Р-143. Исправление: чтение: новое название «Дом …», старое — в `corrections`.

Находок нет.

### Повтор одного id в списке записи (`refs`, `residents`, `members` и т. п.) — 0

Проверка `relations.list_dup`; решения: Р-30. Исправление: авто: да — убрать повтор (при разных `note` — объединить).

Находок нет.

## Двойники (Р-154)

### Записи одного вида с одинаковым названием в разных книгах (или книга + общая), без `same_as` — 24

Проверка `twins.cross_book`; решения: Р-154, Р-80, Р-99. Исправление: чтение: общая запись или законное совпадение имён (Р-99).

По книгам: _общие — 5, arkham-en — 1, bless-the-beast-and-children-ru — 1, dead-light-en — 1, dveri-vo-tmu-ru — 2, griby-s-yuggota-ru — 1, hellouin-v-danviche-ru — 1, kanikuly-v-innsmute-ru — 1, kogda-zazhigayutsya-kostry-ru — 1, lightless-beacon-ru — 1, lokhmotya-korolya-ru — 1, odno-nebolshoe-deltse-ru — 1, shadows-of-leningrad-en — 7

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/characters/stephen-hurst.json` | character «стивен херст» (ru) в 2 книгах: coc:character:stephen-hurst (_общие); pobeg-iz-innsmuta-ru/character/stiven-kherst (pobeg-iz-innsmuta-ru) | medium |
| _общие | `kb/creatures/horse-of-the-invisible.json` | creature «незримый конь» (ru) в 2 книгах: coc:creature:horse-of-the-invisible (_общие); mify-hastura-ru/creature/unseen-horse (mify-hastura-ru) | medium |
| _общие | `kb/locations/eagle-lake.json` | location «eagle lake» (en) в 2 книгах: coc:location:eagle-lake (_общие); fears-sharp-little-needles-en/location/pulvis-eagle-lake-lake (fears-sharp-little-needles-en) | medium |
| _общие | `kb/creatures/horig.json` | creature «horig» (en) в 2 книгах: coc:creature:horig (_общие); temnye-veka-tri-stsenariya-ru/creature/esewald-horig (temnye-veka-tri-stsenariya-ru); уже связаны: relations.target | low |
| _общие | `kb/creatures/pucel.json` | creature «pucel» (en) в 2 книгах: coc:creature:pucel (_общие); temnye-veka-tri-stsenariya-ru/creature/esewald-pucel (temnye-veka-tri-stsenariya-ru); уже связаны: relations.target | low |
| arkham-en | `kb/books/arkham-en/characters/northside-lucy-james.json` | character «люси джеймс» (ru) в 2 книгах: arkham-en/character/northside-lucy-james (arkham-en); pobeg-iz-innsmuta-ru/character/lyusi-dzheyms (pobeg-iz-innsmuta-ru) | medium |
| bless-the-beast-and-children-ru | `kb/books/bless-the-beast-and-children-ru/characters/salli.json` | character «салли» (ru) в 2 книгах: bless-the-beast-and-children-ru/character/salli (bless-the-beast-and-children-ru); kanikuly-v-innsmute-ru/character/salli (kanikuly-v-innsmute-ru) | low |
| dead-light-en | `kb/books/dead-light-en/locations/chalice-well.json` | location «колодец» (ru) в 2 книгах: dead-light-en/location/chalice-well (dead-light-en); starter-edge-of-darkness-ru/location/well (starter-edge-of-darkness-ru) | medium |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/characters/darkness-john-brown.json` | character «джон браун» (ru) в 2 книгах: dveri-vo-tmu-ru/character/darkness-john-brown (dveri-vo-tmu-ru); za-zakrytymi-dveryami-ru/character/john-brown (za-zakrytymi-dveryami-ru) | medium |
| dveri-vo-tmu-ru | `kb/books/dveri-vo-tmu-ru/locations/lake-clearing.json` | location «clearing» (en) в 2 книгах: dveri-vo-tmu-ru/location/lake-clearing (dveri-vo-tmu-ru); keepers-companion-en/location/little-miracles-clearing (keepers-companion-en) | medium |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/creatures/sands-byakhee.json` | creature «byakhee» (en) в 2 книгах: griby-s-yuggota-ru/creature/sands-byakhee (griby-s-yuggota-ru); lokhmotya-korolya-ru/creature/milan-byakhee (lokhmotya-korolya-ru) | medium |
| hellouin-v-danviche-ru | `kb/books/hellouin-v-danviche-ru/characters/edit.json` | character «эдит» (ru) в 2 книгах: hellouin-v-danviche-ru/character/edit (hellouin-v-danviche-ru); osobnyaki-bezumiya-ru/character/memphis-edith (osobnyaki-bezumiya-ru) | low |
| kanikuly-v-innsmute-ru | `kb/books/kanikuly-v-innsmute-ru/characters/uilyam.json` | character «уильям» (ru) в 2 книгах: kanikuly-v-innsmute-ru/character/uilyam (kanikuly-v-innsmute-ru); lechebnitsa-ru/character/uilyam (lechebnitsa-ru) | low |
| kogda-zazhigayutsya-kostry-ru | `kb/books/kogda-zazhigayutsya-kostry-ru/handouts/vvodnaya-dlya-igrokov.json` | handout «вводная для игроков» (ru) в 2 книгах: kogda-zazhigayutsya-kostry-ru/handout/vvodnaya-dlya-igrokov (kogda-zazhigayutsya-kostry-ru); pod-zemlyoy-i-nad-zemlyoy-ru/handout/vvodnaya-dlya-igrokov (pod-zemlyoy-i-nad-zemlyoy-ru) | low |
| lightless-beacon-ru | `kb/books/lightless-beacon-ru/characters/artist.json` | character «эдмунд хейл» (ru) в 2 книгах: lightless-beacon-ru/character/artist (lightless-beacon-ru); pax-cthuliana-ru/character/edmund-kheyl (pax-cthuliana-ru) | medium |
| lokhmotya-korolya-ru | `kb/books/lokhmotya-korolya-ru/characters/drakmar-porters.json` | character «носильщики» (ru) в 2 книгах: lokhmotya-korolya-ru/character/drakmar-porters (lokhmotya-korolya-ru); pogonya-v-poezde-ru/character/nosilshchiki (pogonya-v-poezde-ru) | low |
| odno-nebolshoe-deltse-ru | `kb/books/odno-nebolshoe-deltse-ru/characters/boston-police.json` | character «полицейские» (ru) в 2 книгах: odno-nebolshoe-deltse-ru/character/boston-police (odno-nebolshoe-deltse-ru); zabyvayushchiysya-ru/character/politseyskie (zabyvayushchiysya-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-a-arkham-advertiser.json` | handout «player handout a» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-a-arkham-advertiser (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-a-invitation (sny-o-yaponii-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-b-kamzanov-telegram.json` | handout «player handout b» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-b-kamzanov-telegram (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-b-library (sny-o-yaponii-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-c-police-notes.json` | handout «player handout c» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-c-police-notes (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-c-veronica-room (sny-o-yaponii-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-d-one-happy-family.json` | handout «player handout d» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-d-one-happy-family (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-d-fuji (sny-o-yaponii-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-e-they-live.json` | handout «player handout e» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-e-they-live (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-e-naushua (sny-o-yaponii-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-f-temple-map.json` | handout «player handout f» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-f-temple-map (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-f-forest-sign (sny-o-yaponii-ru) | low |
| shadows-of-leningrad-en | `kb/books/shadows-of-leningrad-en/handouts/handout-g-mikhail-note.json` | handout «player handout g» (en) в 2 книгах: shadows-of-leningrad-en/handout/handout-g-mikhail-note (shadows-of-leningrad-en); sny-o-yaponii-ru/handout/japan-handout-g-dead-investigators (sny-o-yaponii-ru) | low |

### Записи одного вида с одинаковым названием внутри одной книги — 17

Проверка `twins.same_book`; решения: Р-154. Исправление: чтение: слить или переименовать.

По книгам: _общие — 3, cursed-idol-of-manco-capac-en — 1, fears-sharp-little-needles-en — 5, griby-s-yuggota-ru — 1, mts-kharkov-37-ru — 4, pulp-cthulhu-en — 1, tri-koshmarnykh-vechera-ru — 1, viral-en — 1

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/locations/arkham-137-newsstand.json` | location «newsstand» (en) ×2: coc:location:arkham-137-newsstand; coc:location:arkham-437-a-newsstand | low |
| _общие | `kb/rules/dark-ages-setting-a-z-oral-tradition.json` | rule «oral tradition» (en) ×2: coc:rule:dark-ages-setting-a-z-oral-tradition; coc:rule:dark-ages-system-oral-tradition | low |
| _общие | `kb/rules/dark-ages-system-optional-combat-rules.json` | rule «optional rules» (en) ×2: coc:rule:dark-ages-system-optional-combat-rules; coc:rule:dark-ages-system-optional-sanity-rules | low |
| cursed-idol-of-manco-capac-en | `kb/books/cursed-idol-of-manco-capac-en/scenes/race-travel.json` | scene «scene 1: travel» (en) ×2: cursed-idol-of-manco-capac-en/scene/race-travel; cursed-idol-of-manco-capac-en/scene/travel | medium |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/items/bone-deep-security-footage.json` | item «security camera footage» (en) ×2: fears-sharp-little-needles-en/item/bone-deep-security-footage; fears-sharp-little-needles-en/item/phlebotomy-qwiklab-camera-footage | medium |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/scenes/dissociation-interlude-one.json` | scene «dreamscape interlude» (en) ×2: fears-sharp-little-needles-en/scene/dissociation-interlude-one; fears-sharp-little-needles-en/scene/dissociation-interlude-two | medium |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/scenes/dissociation-investigation-one.json` | scene «investigation» (en) ×2: fears-sharp-little-needles-en/scene/dissociation-investigation-one; fears-sharp-little-needles-en/scene/dissociation-investigation-three | medium |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/scenes/phlebotomy-jess-bell-clinic.json` | scene «interview, jess bell» (en) ×2: fears-sharp-little-needles-en/scene/phlebotomy-jess-bell-clinic; fears-sharp-little-needles-en/scene/phlebotomy-jess-bell-interview | medium |
| fears-sharp-little-needles-en | `kb/books/fears-sharp-little-needles-en/scenes/poetry-night-return.json` | scene «returning to earth» (en) ×2: fears-sharp-little-needles-en/scene/poetry-night-return; fears-sharp-little-needles-en/scene/poetry-night-returning-to-earth-steps | medium |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/items/bay-call-beast-parchment.json` | item «пергамент с заклинанием призвать/отпустить зверя» (ru) ×2: griby-s-yuggota-ru/item/bay-call-beast-parchment; griby-s-yuggota-ru/item/castle-beast-vellum | medium |
| mts-kharkov-37-ru | `kb/books/mts-kharkov-37-ru/locations/baylenkhov-1a-kladbishche.json` | location «кладбище» (ru) ×2: mts-kharkov-37-ru/location/baylenkhov-1a-kladbishche; mts-kharkov-37-ru/location/chechenka-2-kladbishche | low |
| mts-kharkov-37-ru | `kb/books/mts-kharkov-37-ru/locations/baylenkhov-2-obshchina.json` | location «община» (ru) ×2: mts-kharkov-37-ru/location/baylenkhov-2-obshchina; mts-kharkov-37-ru/location/chechenka-4-obshchina | low |
| mts-kharkov-37-ru | `kb/books/mts-kharkov-37-ru/locations/baylenkhov-4-ambary.json` | location «амбары» (ru) ×2: mts-kharkov-37-ru/location/baylenkhov-4-ambary; mts-kharkov-37-ru/location/yurenkovo-3-ambary | low |
| mts-kharkov-37-ru | `kb/books/mts-kharkov-37-ru/locations/baylenkhov-5-kuznitsa.json` | location «кузница» (ru) ×2: mts-kharkov-37-ru/location/baylenkhov-5-kuznitsa; mts-kharkov-37-ru/location/chechenka-6-kuznitsa | low |
| pulp-cthulhu-en | `kb/books/pulp-cthulhu-en/scenes/hurricane-aftermath.json` | scene «aftermath» (en) ×2: pulp-cthulhu-en/scene/hurricane-aftermath; pulp-cthulhu-en/scene/hurricane-hotel-aftermath | medium |
| tri-koshmarnykh-vechera-ru | `kb/books/tri-koshmarnykh-vechera-ru/locations/pieces-apartamenty-2-ofis.json` | location «офис» (ru) ×2: tri-koshmarnykh-vechera-ru/location/pieces-apartamenty-2-ofis; tri-koshmarnykh-vechera-ru/location/pieces-morg-4-ofis | low |
| viral-en | `kb/books/viral-en/locations/1e-operating-room.json` | location «operating room» (en) ×2: viral-en/location/1e-operating-room; viral-en/location/1u-operating-room | low |

## Сироты

### Сюжетная запись книги, на которую никто не ссылается и которая сама никуда не ссылается — 0

Проверка `orphans.isolated`; решения: Р-128, Р-132. Исправление: чтение: привязать к сцене/месту или убрать.

Находок нет.

### Документ, предмет или организация книги, на которые никто не ссылается (сами ссылаются только на место или людей) — 0

Проверка `orphans.unused`; решения: Р-128, Р-133. Исправление: чтение: найти сцену или шаг сценария, где его дают, и сослаться оттуда.

Находок нет.

## Номера мест в тексте без ссылки

### В описании места или сцены назван номер места того же города, а ссылки на это место нет — 15

Проверка `text_refs.number`; решения: Р-30, Р-78. Исправление: полуавто: добавить id в `refs` по номеру (числа из 3+ цифр почти всегда верны).

По книгам: _общие — 1, griby-s-yuggota-ru — 1, masks-of-nyarlathotep-en — 13

| Книга | Файл | Суть | Ув. |
|---|---|---|---|
| _общие | `kb/locations/arkham-104-renforth-residence.json` | «…оме (498, прежде 493, Уэст-Кёрвен-стрит; у Hort — место 103) живёт не Джудит Ренфорт, а з…» → «Дом Эппли» (coc:location:arkham-103-appley-residence) | medium |
| griby-s-yuggota-ru | `kb/books/griby-s-yuggota-ru/scenes/bay-night-trap.json` | «…копическими руками-клешнями и излучателем; Клешни (4) 25%, 1d6 (схватив, наносит ур…» → «Модель небосвода» (griby-s-yuggota-ru/location/bay-nw-4-heavens-model) | medium |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/america-prospero-house.json` | «…секретаря Кенсингтона — письмо Элиаса из Найроби (№ 11), его найробийские заметки (№…» → «Отель «Таймс-сквер»» (masks-of-nyarlathotep-en/location/america-times-square-hotel) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/america-prospero-house.json` | «…лиаса из Найроби (№ 11), его найробийские заметки (№ 12) и последние заметки (№ 13).…» → «Нью-Йоркская публичная библиотека» (coc:location:new-york-public-library) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/locations/america-prospero-house.json` | «…о найробийские заметки (№ 12) и последние заметки (№ 13).…» → «Отель «Мюррей-Хилл»» (masks-of-nyarlathotep-en/location/america-murray-hill-hotel) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…убийц): письмо Роджеру Карлайлу от Варена Безара (№ 1); визитная карточка Эдварда Га…» → «Нью-Йоркский университет (кампус Юниверсити-Хайтс)» (masks-of-nyarlathotep-en/location/america-nyu-university-heights) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…Безара (№ 1); визитная карточка Эдварда Гавигана (№ 2); пустой коробок спичек из бар…» → «Бронксский зоопарк» (masks-of-nyarlathotep-en/location/america-bronx-zoo) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…устой коробок спичек из бара «Спотыкающийся тигр» (№ 3); размытая фотография яхты (№…» → «Стадион «Янки»» (masks-of-nyarlathotep-en/location/america-yankee-stadium) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…отыкающийся тигр» (№ 3); размытая фотография яхты (№ 4); визитная карточка «Эмерсон-и…» → «Центральный парк» (coc:location:central-park) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…сон-импортс» с именем «Сайлас Н’Кване» на обороте (№ 5); письмо Мириам Атрайт, библио…» → «Медицинский совет штата Нью-Йорк» (masks-of-nyarlathotep-en/location/america-medical-affairs-board) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…№ 5); письмо Мириам Атрайт, библиотекаря Гарварда (№ 6); афиша лекции профессора Каул…» → «Редакция La Prensa» (masks-of-nyarlathotep-en/location/america-la-prensa) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…еологией в христианском мире» Эндрю Диксона Уайта (№ 7). Последняя улика — знак, выре…» → «Отель «Плаза»» (masks-of-nyarlathotep-en/location/america-plaza-hotel) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-information-in-room-410.json` | «…Последняя улика — знак, вырезанный на лбу Элиаса (№ 8), — доступна, только если сыщи…» → «Редакция New York Times» (masks-of-nyarlathotep-en/location/america-new-york-times) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-prospero-house-visit.json` | «…Кении. Вскоре Кенсингтон получил обещанные записи (№ 12). Потом Элиас телеграфировал и…» → «Нью-Йоркская публичная библиотека» (coc:location:new-york-public-library) | low |
| masks-of-nyarlathotep-en | `kb/books/masks-of-nyarlathotep-en/scenes/america-prospero-house-visit.json` | «…дней назад, Элиас оставил Кенсингтону ещё записи (№ 13). Они так путаны и отрывочны,…» → «Отель «Мюррей-Хилл»» (masks-of-nyarlathotep-en/location/america-murray-hill-hotel) | low |
