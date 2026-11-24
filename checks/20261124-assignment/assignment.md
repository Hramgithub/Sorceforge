# Cthulhu Invictus — The Assignment (`invictus-assignment-en`) — сверка переноса

Сценарий Марко Каррера («Miskatonic Repository», 2020; Cthulhu Invictus, Римская империя, Италия; один игрок и
Хранитель). PDF — 10 страниц; печатная страница = физической (смещение 0); без номеров: с. 1 (обложка), с. 3
(оглавление), с. 9 (карты-раздатки). Русский текст — наш перевод (Р-251, Р-21). Русского перевода в базе и в
библиотеке нет (проверено по именам Kaeso, Fenius, Mallius, Brundisium, strix).

Сценарий — не книга-игра с нумерованными абзацами (Р-230): это обычный сценарий для одного игрока. Поэтому
записан как обычный сценарий со сценами и шагами; поля `solo` и таблицы «Абзацы» нет.

## Заголовки книги → записи базы

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) | 1 | атмосфера — `atmosphere.json`; источник сценария `invictus-assignment-en/scenario/the-assignment` |
| Credits | 2 | источник сценария (выходные данные) |
| Table of Contents | 3 | источник сценария (оглавление) |
| Introduction | 4 | сценарий: `keeper_info` («Введение») |
| Keeper Information | 4 | сценарий: `keeper_info`, `summary`; `character/fenius`, `character/kaeso-neratius`, `creature/strix` |
| New Skills | 4 | сценарий: `advice` («Новые навыки») |
| Historical Background about the Investigator’s Occupation | 4 | сценарий: `advice`; `character/fenius` (описание искателя) |
| Carrying Weapons Around | 4 | сценарий: `advice`; `location/brundisium` (запрет на оружие) |
| (карта Италии с Brundisium) | 4 | `map/italy-brundisium` → `location/brundisium` |
| At the villa | 5 | `scene/at-the-villa`; `character/villa-guards`, `character/old-gardener` |
| The parchment (врезка) | 5 | `tome/kaeso-parchment`; `character/egyptian-merchant`; сценарий `keeper_info` |
| The villa (врезка) | 5 | `location/kaeso-villa` |
| The slums | 6 | `scene/the-slums`; `location/slums`; `character/slum-youngster`, `character/thug` |
| The house | 6 | `scene/the-house`; `location/owl-house`, `owl-house-common-room`, `owl-house-bedroom`, `owl-house-dungeon`; `character/prisoner` |
| Where in the forest? | 6–7 | `scene/where-in-the-forest`; `character/augur`, `location/augur-dwelling`, `character/mallius-castus`, `location/market`, `location/house-of-pleasure`, `character/old-man-watcher` |
| The forest | 7 | `scene/the-forest`; `location/forest`, `location/ritual-clearing`; `item/winged-deity-statue`, `item/strix-head`, `character/altar-youth` |
| (возвращение на виллу, внутри «The forest») | 7 | `scene/back-at-the-villa`; сценарий `conclusion` |
| Rewards | 7 | сценарий `conclusion` («Награды»); `scene/back-at-the-villa` |
| NPC Stat Blocks and Skills | 8 | — |
| Strix (The foul-winged woman) | 8 | `creature/strix` (статблок, арт `app/art/creatures/assignment-strix.webp`) |
| Kaeso Neratius | 8 | `character/kaeso-neratius` |
| Average guard | 8 | `character/villa-guards` (групповой профиль, имена придуманы) |
| Thug | 8 | `character/thug` |
| Mallius Castus (Newsreader) | 8 | `character/mallius-castus` |
| Player Handouts: Map 1 | 9 | `map/owl-house-map-1` (`app/maps/assignment-owl-house-map-1.png`) |
| Player Handouts: Map 2 | 9 | `map/owl-house-map-2` (`app/maps/assignment-owl-house-map-2.png`) |
| Torture tools | 10 | `handout/torture-tools` (картинка `app/art/handouts/assignment-torture-tools.webp`) |

Все id — с префиксом `invictus-assignment-en/`.

## Не взято

- Обложка (с. 1) — атмосферная картинка, не связана с записью → `atmosphere.json` (сводит ведущий).
- Безымянные рабы в саду виллы, совы стрикса, пропавшие бедняки, власти — без своих записей: только текст сцен,
  места и существа (книга не даёт им ни имён, ни чисел).
- Метки без подписей на карте 1 (прямоугольник на верхней стене, ромб, пятиугольник) — без меток; описаны в
  `quality.notes` карты.
- Навыки Cthulhu Invictus «Гражданские дела» (Civics) и «Империя» (Empire): правил книга не даёт, записей в
  справочнике нет — текстом в статблоках (Р-126). Кандидаты в справочник навыков эпохи.
- Заклинания стрикса «mind control», «transform into a woman» и пергамента «contact Shantak» — в справочнике нет;
  у стрикса без ссылки, у пергамента — ссылка на семейство «Заклинания связи».

## Опечатки и сомнения книги

- ПЗ всех статблоков не сходятся с (ВЫН + ТЕЛ) / 10 — оставлены как напечатаны, в `errata` (Р-161): стрикс 11
  (по формуле 9), Цезон 9 (12), стражник 10 (12), громила 6 (9), Маллий 10 (8).
- В тексте и на карте 2 — три орудия пыток, на рисунке с. 10 — два (пометка в раздатке).
- «If the Idea roll fails» (с. 7) — не ясно, какая из двух проверок Идеи раздела; оставлено как напечатано
  (пометка в сцене).
- Урон атак людей не указан (только проценты навыков) — навыки перенесены как напечатаны.
- Книга называет Шантака одним существом («the creature Shantak»); ссылка — на общую запись вида.
- Метка библиотеки «[EN 6e]», но статблоки — 7-й редакции; перенесено как 7e.
- Словесные опечатки английского текста («fo 1d6», «She’s is», «robed») при переводе исчезли, не записаны (Р-39).

## Термины (English → Russian)

| English | Русский |
|---|---|
| The Assignment | «Поручение» |
| finder | искатель |
| patron | патрон |
| strix | стрикс |
| Strix (The foul-winged woman) | Мерзкокрылая женщина (стрикс) |
| Kaeso Neratius | Цезон Нераций |
| Fenius | Фений |
| Mallius Castus | Маллий Каст |
| Aelia | Элия |
| newsreader | чтец новостей |
| augur | авгур |
| Brundisium | Брундизий |
| Aegyptus (Egypt) | Египет (Aegyptus) |
| the villa | вилла (Вилла Цезона Нерация) |
| study | кабинет |
| the slums | трущобы (Трущобы Брундизия) |
| her house | Дом с совой |
| common room / bedroom / dungeon | общая комната / спальня / подземелье |
| trapdoor | люк |
| The house of pleasure | «Дом удовольствий» (лупанарий) |
| brothel | лупанарий |
| the forest | лес (Лес у Брундизия) |
| ritual area | место обряда (Поляна с алтарём крылатого божества) |
| statue of a mysterious winged deity | статуя таинственного крылатого божества |
| the parchment | пергамент (Египетский пергамент Цезона) |
| contact Shantak | связь с Шантаком |
| mind control | контроль разума |
| transform into a woman | превращение в женщину |
| torture/sex tools | орудия пыток и утех (Раздатка: орудия пыток) |
| thug | громила |
| Average guard | Обычный стражник (Стражники виллы) |
| Grapple / Rend / Call | Захват / Терзание / Зов |
| Civics | Гражданские дела |
| Empire | Империя |
| Other Kingdoms | Другие королевства (общий навык) |
| Status | Статус (общий навык) |
| Gladius (Sword) | Гладиус (меч) |
| Shield | Щит |
| sestertii | сестерции |
| red herring | ложный след |
| Shantak | Шантак (общая запись) |
| Nyarlathotep | Ньярлатхотеп (общая запись) |

Официальные формы навыков и правил — по глоссарию: Убеждение, Ориентирование, Внимание, Слух, Скрытность,
Проницательность, Запугивание, Медицина, Первая помощь, проверка Идеи, проверка Знаний, проверка Удачи, повторная
проверка, штрафная кость, погоня, Значение Мифов.

## Придуманные имена (Р-150, Р-151)

Стражники виллы — Гай Валерий, Тит Анний, Марк Петроний, Луций Сестий, Публий Вибий; громила — Децим; старый
садовник — Евтих; мальчишка из трущоб — Гней; узник подземелья — Квинт; старик у дома — Порций; авгур — Авл;
юноша на алтаре — Секст; египетский купец — Петосирис.

## Кандидаты в общие записи

- `coc:location:brundisium` — реальный город; общей записи нет, пока запись книги `location/brundisium`.
- Стрикс (вид существа Cthulhu Invictus) — общей записи нет; здесь уникальный вариант сценария.
- Навыки Cthulhu Invictus «Гражданские дела» (Civics), «Империя» (Empire).

## Проверки

- `python -B tools/check.py kb/books/invictus-assignment-en` — ошибок 0, предупреждений 0.
- `completeness`: 1 находка — обложка (атмосфера, `atmosphere.json`).
- `scenario`: 0 находок.
