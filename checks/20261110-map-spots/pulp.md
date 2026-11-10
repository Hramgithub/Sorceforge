# Метки карт Pulp Cthulhu (2026-11-10, Р-206)

Часть «pulp» конвейера Р-139. Книга `pulp-cthulhu-en` (печатная страница = физическая − 1), карты сценариев
«The Disintegrator» (с. 142–143), «Waiting for the Hurricane» (с. 160–161, 167–168), «Pandora’s Box» (с. 188, 191)
и «A Slow Boat to China» (с. 210–211, 219); картинки большей части карт — копии для игроков из гл. 14 (с. 237–252).
Подписи найдены `tesseract … tsv` (масштаб ×2); номера в кружках tesseract не читает — кружки найдены по глазной
оценке и уточнены поиском лучшего кружка рядом (тёмный диск со светлой цифрой — планы «Уайт-Пойнта» и храма; светлый
диск с тёмным ободом — карты парохода), каждая метка проверена глазами по увеличенной вырезке с нанесёнными метками
(сомнительные уточнения поиска заменены координатами по вырезке). Карты сценариев Pulp без номеров (большая часть) —
это подписи помещений: если у подписи есть запись, метка ведёт на неё, иначе — на здание с пояснением в `text`
(Р-155); подписи-ориентиры и подписи без записей (улицы, болота, пляжи, лес) — без меток.

## Карты

| Карта | Меток | Номеров в ключе | Новых мест | Не поставлено |
|---|---|---|---|---|
| `white-point-hotel-environs` (с. 142) | 6: «Hotel», «Barn», «Boat House», «Walled Gardens» (на сад отеля, с пометкой), «White Point Cove» (на Уайт-Пойнт), «To Kingsport» | — (номеров нет) | 0 | «The Hinterland», «Rocky Headlands», «Slipway», «Golf Course», «Beach» — подписи без записей (описаны текстом в записи «Уайт-Пойнт»); роза ветров |
| `white-point-hotel-floorplan` (с. 143 = 237) | 16: 1–11; «To the Barn», «Stone Angel», «Open to Below» (на вестибюль), «Stores» ×2 (подвал, на отель) | 11 | 8: 3–10 (1, 2, 11 были, `number` у них стоял) | заголовки этажей «First/Second/Third Floor», «Basement», пояснения «not to scale», «Area of the Hotel Above», легенда |
| `grand-hotel-and-environs` (с. 160 = 240) | 4: «The Grand Hotel», «Garden Area & Pool», «Parking Lot», «Rented Apartments» (все на Гранд-отель) | — | 0 | «The Beach», «Smather’s Beach», «Bertha Street», «Atlantic Boulevard», «Swamp» ×3, «The Straits of Florida» — без записей; роза ветров |
| `grand-hotel-floorplan` (с. 161 = 241) | 26: подписи помещений двух этажей (кухня, кладовые, лифты, прачечная, консьерж, персонал, раздевалки, кабинеты, ресторан, вестибюль, гостиная, пожарные лестницы ×4, номера и люксы) — все на Гранд-отель с `text` | — | 0 | «First Floor», «Second Floor», легенда («Dumb Waiter», «Staircase», «Elevator», «Private/Public Areas»), уменьшенная схема окрестностей |
| `wisteria-island` (с. 167 = 238) | 4: «Temple Dome» (на карту храма), «Path Through Woods» (на тропу — № 5 плана храма), «Beached Yacht» (на остров), «Key West» | — | 0 (тропа заведена по плану храма) | «Woodland» ×2, «Tank Island (Sunset Key)» — записи нет; масштаб, роза ветров |
| `wisteria-temple` (с. 168 = 239) | 16: 1–7; «Ramp Going Down», «Entrance» (на вход 1), «Open Pool» (на тоннель 6), «Dome Perimeter», «Dressing Rooms», «Living Room», «Whiting’s Room», «Store» ×2 (на храм) | 7 | 7: 1–7 | «Bedrock», «Woodland» ×2, масштаб, роза ветров |
| `pandoras-palace` (с. 188) | 36: все подписи и сокращения помещений (W.C. ×5, ST. ×3, BAR ×3, D.R. ×2, V.I.P. ×2, F. ×2 и др.); «Bailey’s Office», «Safe», «Forced Skylight» — на кабинет Бейли, остальные на клуб с `text` | — | 0 | легенда сокращений, заголовок |
| `seekers-lodge` (с. 191) | 5: «Fence», «Front Gate», «Magical Experimentation Room», «The Ritual Room», «Robing Room» (на Ложу с `text`) | — | 0 | «Basement», «Boundary of the House Above», «5ft», легенда; **первый и второй этажи в картинку не попали** (см. ниже) |
| `slow-boat-upper-decks` (с. 210 = 251) | 27: 20 кружков (7 ×3, 5 ×2, 13 ×2 и по одному 4, 6, 8–12, 14, 16–20); «Sun Deck», «Boat Deck», «Promenade Deck», «Deck A»; на врезке «Shanghai», «Hong Kong», «New York» | 20 | 18 ключевых + 4 палубы | номера 1, 2, 3, 15 есть только на карте нижних палуб; города врезки без записей (Peking, Vladivostok, Tokyo, San Francisco, Chicago, Boston, Mexico City, Hawai’i, Bangkok, Singapore, «…utta»); ключ, легенда, плакат |
| `slow-boat-lower-decks` (с. 211 = 252) | 24: 11 кружков (7 ×5; 1, 2, 3, 10, 15, 18); «Cargo Hold 1–7»; «Boiler Room», «Engine Room» (на машинное отделение); «Deck B–E» | ключ — тот же | 4 палубы | рекламная врезка «Dollar Line» (её фильмы и оркестры — в записях «Континентальная гостиная» и «Большой салон») |
| `slow-boat-first-third-class-lodging` (с. 219) | 4: «Promenade», «First Class» (на первый класс), «Third Class», «Shared Bathrooms» (на третий класс) | — | 0 | заголовок плана |

Всего: 168 меток, 41 новое место. Номера ключа парохода 1 и 9 — существующие записи «Обеденный зал первого класса» и
«Музыкальный салон» (им добавлен `number`); номера 1, 2, 11 плана «Уайт-Пойнта» — существующие записи с `number`.
`spot_shape` пересчитан для каждой картинки (кружки — диаметр кружка; карты с подписями — `label` по размеру подписи).

## Новые места (`pulp-cthulhu-en/location/…`)

| Метка | Запись | Страницы |
|---|---|---|
| «Уайт-Пойнт» 3–10 | `white-point-hotel-store`, `-mud-room`, `-basement-stairs`, `-lobby`, `-lounge`, `-check-in`, `-office`, `-reception-room` | 143, 237 (+151, 156) |
| Храм 1–4, 6, 7 | `wisteria-temple-entrance`, `-altar-one`, `-altar-two`, `-cthulhu-statue`, `-underwater-tunnel`, `-guard` | 168–170, 239 |
| Храм 5 / «Path Through Woods» | `wisteria-trail-to-shore` (`part_of` — остров) | 167–169 |
| Пароход 2–8, 10–20 | `slow-boat-special-class-dining-room`, `-other-dining`, `-bridge`, `-pool`, `-soda-shop`, `-lounge`, `-first-class-saloon`, `-smoking-room`, `-grand-salon`, `-continental-lounge`, `-library`, `-print-room`, `-gymnasium`, `-barber-shop`, `-dark-room`, `-beauty-salon`, `-tailor`, `-ships-doctor` | 206–211, 218, 222, 251–252 |
| Палубы | `slow-boat-sun-deck`, `-boat-deck`, `-promenade-deck`, `-deck-a`, `-deck-b`, `-deck-c`, `-deck-d`, `-deck-e` | 206, 208, 210–211, 218, 220–221 |

Изменены записи части: 11 карт (`spots`, `spot_shape`, `quality.notes` — убрано устаревшее «картинки пока нет»,
`corrections`); `slow-boat-ss-president-coolidge` — `refs` строк 1–20 таблицы «Ключ к картам «Президента Кулиджа»»,
`corrections`; `slow-boat-first-class-dining-room` (`number` 1), `slow-boat-music-room` (`number` 9) — `corrections`,
`refs` на карту. `kb/locations/kingsport.json` и `key-west.json` не менялись (на них только ведут метки).

## Предложения

`proposals-pulp.json` — 14 предложений (пробный прогон `pipeline/integrate/apply.py --dry-run` ложится целиком, 7 записей):
`found_at` статуи Ктулху → место статуи; `where` сцены «Обряд» += два алтаря, место статуи, подводный тоннель; сцены
«Остров Вистерия» += тропа, пост стража, вход; «Доктор Сун просит о помощи» += курительная, библиотека; «Украденная
книга» += шлюпочная и прогулочная палубы; «Пустой костюм» += палуба A; «Соседи по каюте» += прогулочная палуба.

## Сомнения и выводы из текста

- **Картинка `app/maps/pulp-seekers-lodge.jpg` (623×699) — вырезка только левой части плана со с. 191**: участок и
  подвал. Первый и второй этажи Ложи (бар, гостиная, курительная, кабинеты, зал для собраний, столовая, кухня,
  приёмная, вестибюль, комнаты ожидания; библиотека со звёздочкой «reserved books», читальня, зал совета, галерея,
  веранда) в неё не попали. Нужна новая вырезка всего плана (с. 191 или повтор на с. 250) — тогда добавить метки
  этих подписей. Картинки — не файлы части, правка за ведущим.
- «Walled Gardens» карты окрестностей ведёт на задний сад плана отеля; что это одно место, книга прямо не говорит —
  в `note` метки (вывод, Р-41).
- «Другие столовые» (3) — вероятно, обеденный зал третьего класса (у кормы палубы C, с. 206) — вывод из текста, Р-41.
- Палубы на карте против текста (в `note` меток и в записях): музыкальный салон (9) — в тексте на палубе B, на карте на
  прогулочной; «Континентальная гостиная» (12) — в тексте на палубе A, на карте на прогулочной (отмечено ещё в
  `slowboat.md` для салона).
- Кабинет управляющего Гранд-отеля (с. 159) — возможно, одна из комнат «Offices» плана; номер 202 (с. 160) на плане
  не обозначен — сказано в `text` меток.
- Кладовая с дробовиком смотрителя «below stairs» (с. 156) — в подвале ли, книга не уточняет; сказано в записи
  лестницы в подвал.
- Мелочи оформления карт (Р-39, не записаны): «Smather’s Beach» (в тексте — Smathers Beach), «Seeker’s Lodge» (в
  тексте — Seekers).

## Заголовки книги

Полная сверка заголовков с. 135–234 сделана при переносе сценариев: `checks/20261108-pulp/disintegrator.md`,
`hurricane.md`, `pandora.md`, `slowboat.md`. Здесь — заголовки и подписи карт, получившие метки и новые записи.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The White Point Hotel and Environs (карта) | 142 | `map/white-point-hotel-environs` — 6 меток |
| The White Point Hotel Internal Floorplan (план, легенда 1–11) | 143, 237 | `map/white-point-hotel-floorplan`; 8 новых комнат + кухня, оранжерея, столовая |
| The Grand Hotel and Environs (карта) | 160, 240 | `map/grand-hotel-and-environs` — 4 метки |
| The Grand Hotel Internal Floorplan (план) | 161, 241 | `map/grand-hotel-floorplan` — 26 меток |
| Wisteria Island — Where Dark Rites Are Performed (карта) | 167, 238 | `map/wisteria-island`; `wisteria-trail-to-shore` |
| The Temple on Wisteria Island (план, легенда 1–7) | 168, 239 | `map/wisteria-temple`; 7 новых мест |
| Wisteria Island; The Ritual; Stopping the Cult (вход, страж, алтари, статуя, тоннель) | 169–170 | `wisteria-temple-*`, `wisteria-trail-to-shore` |
| Pandora’s Palace — a place of heavenly delights (план) | 188 | `map/pandoras-palace` — 36 меток |
| The Seeker’s Lodge (план) | 191, 250 | `map/seekers-lodge` — 5 меток (картинка неполная) |
| Across the Pacific in Style; Entertainment; Smoking and Drinking (залы и палубы) | 206–208 | `slow-boat-*` — 18 мест ключа и 8 палуб |
| S.S. Coolidge and Its Journey — The Upper Decks (ключ 1–20) | 210, 251 | `map/slow-boat-upper-decks`; таблица ключа у парохода со ссылками |
| S.S. Coolidge and Its Journey — The Lower Decks | 211, 252 | `map/slow-boat-lower-decks` |
| S.S. Coolidge — First & Third Class (план) | 219 | `map/slow-boat-first-third-class-lodging` — 4 метки |

## Не взято

- Подписи без записей: окрестности «Уайт-Пойнта» — «The Hinterland», «Rocky Headlands», «Slipway», «Golf Course»,
  «Beach» (описаны в записи «Уайт-Пойнт»); окрестности Гранд-отеля — «The Beach», «Smather’s Beach», «Bertha Street»,
  «Atlantic Boulevard», три «Swamp», «The Straits of Florida»; остров Вистерия — два «Woodland», «Tank Island (Sunset
  Key)»; план храма — «Bedrock», два «Woodland»; города врезки маршрута парохода, кроме Шанхая, Гонконга и Нью-Йорка.
  Кандидаты в записи, если владелец захочет: остров Танк, пляж Смазерс.
- Заголовки этажей и подвалов («First/Second/Third Floor», «Basement»), пояснения масштаба, «Area of the Hotel Above»,
  «Boundary of the House Above», «5ft», легенды цветов и значков, ключи (сам ключ парохода — таблица у парохода),
  розы ветров, масштабы, заголовки карт, рекламные врезки («Dollar Line», плакат «The S.S. Coolidge — First Class
  Luxury»).
- Первый и второй этажи Ложи Искателей — не на картинке (см. «Сомнения»).
