# «Судьба братьев Вашингтон» (`sudba-bratev-vashington-ru`) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] Судьба Братьев Вашингтон.pdf`, 9 страниц; сценарий Мэта Райана в переводе Сергея Черкасова
(метка `[RU 7e]` — официальный; английское название книга не печатает). Правила — 7-я редакция (листы сыщиков 7e,
погоня по правилам 7e). Текстовый слой надёжен; листы сыщиков (с. 4, 7) и карта (с. 3) сверены по изображениям
страниц. Действие — февраль 1922 года: `axes.era` = `1920s`, `ruleset` = `core`.

**Страницы:** номеров на страницах нет — печатная = физическая (offset 0).

Префикс записей книги: `sudba-bratev-vashington-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| «Судьба братьев Вашингтон», авторы (Мэт Райан, перевод — Черкасов Сергей) | 1 | `scenario/sudba-bratev-vashington` (summary, quality.notes) |
| Информация для Хранителя | 1 | `scenario/sudba-bratev-vashington` (keeper_info); `organization/tserkov-zvezdnoy-mudrosti`; `character/j-s`; `coc:creature:nyarlathotep`, `coc:creature:great-cthulhu` (refs) |
| Информация для игроков | 1 | `scenario/…` (hook); `character/roland-vashington`, `character/sesil-vashington` (legend); `character/gaspar-messina`; `organization/banda-messiny`, `organization/otets-i-synovya-desalvo` |
| Подготовка | 1 | `scenario/…` (hook); `item/gruzovik-mak-ab`; `location/doroga-boston-buffalo` |
| Склад | 1 | `scene/sklad`; `location/sklad-v-bostone`; `character/j-s`, `character/litovskie-bandity`, `character/gangstery-messiny`; `item/zaponki-i-braslet`, `item/yashchik-grob`, `item/kartiny-pikmana`; `location/parokhod-tolosa` |
| Покидая Бостон | 1 | `scene/pokidaya-boston`; `character/gangstery-messiny`; `coc:rule:chases` и др. (refs) |
| Недалеко от Олбани | 1–2 | `scene/nedaleko-ot-olbani`; `location/zapravka-v-olbani`; `character/frenk-kallakhan`; новый город `coc:location:albany` |
| Давайте заглянем внутрь | 2 | `scene/davayte-zaglyanem-vnutr`; `item/kartiny-pikmana`, `item/yashchik-grob`; `creature/upyr-strazh`; `character/richard-apton-pikman` |
| Рассадник социальных волнений | 2 | `scene/rassadnik-sotsialnykh-volneniy`; `location/nochnaya-zapravka-v-sirakuzakh`; `character/tomas-origan`, `character/tagd-origan`; `organization/kompartiya-sirakuz`; `item/vintovki-voennogo-obraztsa`; новый город `coc:location:syracuse` |
| Этот город когда-нибудь спит? | 2 | `scene/etot-gorod-kogda-nibud-spit`; `location/doki-buffalo`, `location/parokhod-tolosa`; `character/ogast-veber`, `character/avtomatchiki`; `scenario/…` (conclusion); новый город `coc:location:buffalo` |
| Дополнительные материалы: Карта («Mand McRally … Northeast Mileage Chart of the United States») | 3 | `map/northeast-mileage-chart` (картинка `app/maps/washington-northeast-mileage-chart.jpg`, 9 меток: 6 городов и 3 расстояния маршрута) |
| Лист сыщика: Роланд Вашингтон (характеристики, навыки, бой) | 4 | `character/roland-vashington` (statblock) |
| Лист сыщика, оборот: «Моя история» — «грубая сила» | 5 | `character/roland-vashington` (description) |
| Лист сыщика: Сесил Вашингтон (характеристики, навыки, бой) | 7 | `character/sesil-vashington` (statblock; Уклонение — errata) |
| Лист сыщика, оборот: «Моя история» — «мозговой центр» | 8 | `character/sesil-vashington` (description) |

Город: Бостон — существующая общая запись `coc:location:boston` (дополнение — предложениями). Олбани, Сиракузы,
Буффало — новые общие записи `kb/locations/albany.json`, `syracuse.json`, `buffalo.json` (Р-190; в базе их не было,
другие части плана там не играют). Маршрут связан записью-зоной `location/doroga-boston-buffalo` (Р-135,
`part_of` — Бостон, откуда начинается путь).

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Пустые графы листов сыщика: место рождения, Удача, «Биография» (описание, идеалы, значимые люди, важные места, ценное имущество, черты, травмы, фобии, книги, встречи), имущество, благосостояние, знакомые сыщики | 4–5, 7–8 | на листах не заполнены |
| «Памятка по правилам» на обороте листа (уровни успеха, раны и лечение) | 5, 8 | типовой текст бланка; правила есть в `kb/rules/` |
| Разлинованные пустые страницы для заметок | 6, 9 | без текста |
| Подписи карты вне маршрута (Toronto, Rochester, Ithaca, Binghamton, Watertown, Plattsburgh, Burlington, Springfield, Hartford, New Haven, Lake Ontario) и расстояния вне маршрута | 3 | записей этих мест нет, в сценарии они не участвуют (как на «Путевой карте Южного Перу») — перечислены в `quality.notes` карты |
| «Кадиллак Тайп 51» клиента, два «Форда Модель Т» гангстеров, трое грузчиков у «Толосы» | 1–2 | без механики; остаются текстом в сценах |

## Сомнения и опечатки

- «Полдюжины картин» («Информация для Хранителя», с. 1) против пяти картин в ящике (с. 2) — `errata` сценария, как напечатано.
- Сесил: Уклонение на листе пусто — поставлено 40 (½ ЛВК 80), `errata` (fixed) и `corrections`, вывод из текста (Р-41).
- «Бульвар Жуткий» (Сиракузы) — как напечатано; вероятно, перевод названия Erie Boulevard (в `quality.notes`).
- «Пилларед Ирем», «Слитмур», «Призрак» — названия сюжетов картин как напечатаны.
- Потеря Рассудка при виде упыря — 1/1d8 (у вида в справочнике — 0/1d6); записана в сцене и упыре-страже.
- Сумма расстояний маршрута по карте — 463 мили (≈ 745 км), текст — «примерно 700 км»; не опечатка, отмечено в карте.
- Что крупный мужчина на складе — сам «J.S.», и что автоматчики — люди культа, книга прямо не говорит (вывод из текста).

## Придуманные имена (Р-150, Р-151)

- Полицейский штата Нью-Йорк — Фрэнк Каллахан; бригадир в доках Буффало — Огаст Вебер.
- Групповые профили с `names`: литовские бандиты, гангстеры Мессина, автоматчики в доках.

## Предложения

`checks/20261112-ru-oneshots/proposals-washington.json` — 7 правок: Бостон (источник, абзац описания, 4 ссылки),
Каир (ссылка на сценарий). Пробный прогон `apply.py --dry-run` — все ложатся.
