# Исправление связей по проверке полноты (2026-11-14)

Основа — `checks/20261114-completeness/verify-scenarios.md` (часть Б и список «Что нет или нужно исправить», пункты 3–6).
Каждая правка существующих записей сделана через `pipeline/integrate/apply.py` из файлов
`links-edits.json` (59 правок, 33 записи) и `links-edits-2.json` (4 правки): изменения значений записаны в
`corrections` записей (`where`, `found_at`, `refs`, `sources`, `tables.N.rows.M.refs`); правки `quality.notes`
(устаревшие пометки «записи места нет») — без `corrections`. Страницы ниже — печатные («с. N»), физические — в
`sources` записей. Проверка: `python -B tools/check.py` по всем 47 файлам — ошибок 0, предупреждений 0;
`tools/completeness.py` по затронутым книгам — у этих сцен и персонажей находок больше нет.

## 1. Сцены, у которых место уже было (6)

| Сцена | `where` | Страница книги |
|---|---|---|
| `masks-of-nyarlathotep-en/scene/america-meeting-professor-cowles` | `coc:location:miskatonic-university` (кабинет в здании гуманитарных факультетов), `coc:location:arkham-139-grafton-diner` | Masks, с. 136 |
| `mts-kharkov-37-ru/scene/rabota-s-voyskami` | `mts-kharkov-37-ru/location/mts-kharkov-37` | «на Станции», с. 39 |
| `pobeg-iz-innsmuta-ru/scene/doktor-iezekil-uolles` | `coc:location:arkham-208-asbury-methodist-episcopal-church` | с. 79–80: пастор церкви, доказательства в подвале |
| `pobeg-iz-innsmuta-ru/scene/politsiya-arkhema` | `coc:location:arkham-228-police-station` | с. 79 |
| `pobeg-iz-innsmuta-ru/scene/efraim-v-oblike-derbi` | `coc:location:arkham-os114-crowninshield-manor` с пометкой: сюда Эфраим просит принести рукопись, где он впервые обращается к сыщикам, книга не говорит | с. 81 |
| `pulp-cthulhu-en/scene/disintegrator-vstrecha-s-finchem` | `coc:location:miskatonic-university` (отдельный кабинет) | Pulp, с. 139: «private office at the Miskatonic University» |

## 2. Новые места (Р-243) и сцены (13)

Новые записи (10):

| Запись | Что это | `part_of` | Источники |
|---|---|---|---|
| `kb/locations/cambridge.json` — `coc:location:cambridge` | **новый общий город** Кембридж (Массачусетс) | — | Masks с. 124 («Miss Atwright, of Cambridge, Massachusetts»); русская раздатка США 6 (бланк «Гарвардский университет, Кембридж, Массачусетс») |
| `kb/books/masks-of-nyarlathotep-en/locations/america-widener-library.json` | Библиотека Уайднера (Гарвард) | Кембридж | Masks с. 109, 136, 641; раздатка США 6 |
| `kb/locations/boston-doki.json` — `coc:location:boston-doki` | Бостонские доки, **общее место**: их называют две книги (Р-154) | Бостон | Побег, с. 104, 141; «Черноводный ручей», с. 38 (склад Макбрайда) |
| `kb/books/pobeg-iz-innsmuta-ru/locations/federalnoe-zdanie-v-bostone.json` | Федеральное здание в Бостоне: кабинет 402, комната для совещаний, камеры в подвале | Бостон | Побег, с. 99–101, 104 |
| `kb/books/pobeg-iz-innsmuta-ru/locations/dom-greggov.json` | Дом Греггов (комната Брайана) | Ипсвич | Побег, с. 80–81 |
| `kb/books/pobeg-iz-innsmuta-ru/locations/dom-bernkhemov.json` | Дом Бёрнхэмов, Саут-Паудермилл-стрит, 325 | Французский холм (Аркхэм) | Побег, с. 79 |
| `kb/books/fears-sharp-little-needles-en/locations/separation-case-western-school-of-medicine.json` | Медицинская школа Университета Кейс Вестерн | Кливленд | Fears, с. 8, 9, 152 |
| `kb/books/fears-sharp-little-needles-en/locations/dissociation-night-flight.json` | Ночной рейс Сан-Диего — Сиэтл; тип «корабль» (воздушное судно, вершина гайда, Р-189); название дано нами (`editorial_text`) | — | Fears, с. 113 |
| `kb/books/podzemka-ru/locations/politsiya-monrealya.json` | Полиция Монреаля (книга говорит только «содержится в полиции»; название наше, `editorial_text`) | Монреаль | Подземка, с. 2–3 |
| `kb/books/poselok-berezovyy-ru/locations/koloniya-45.json` | Колония строгого режима № 45 | посёлок Берёзовый (где колония, книга не говорит; как подлодка S-19 в Иннсмуте, Р-163) | Посёлок, с. 3, 9, 11 |

У «Побега из Иннсмута» раньше не было папки мест: места этой книги — общие места Иннсмута. Места в Бостоне, Ипсвиче и
Аркхэме, нужные только этому сценарию, положены в папку книги с `part_of` на общий город (Р-190).

`where` сцен:

| Сцена | Место |
|---|---|
| `masks-of-nyarlathotep-en/scene/america-meeting-miriam-atwright` | библиотека Уайднера («или по телефону») |
| `pobeg-iz-innsmuta-ru/scene/komnata-brayana-u-greggov` | дом Греггов |
| `pobeg-iz-innsmuta-ru/scene/roditeli-brayana` | дом Бёрнхэмов |
| `pobeg-iz-innsmuta-ru/scene/po-zovu-dolga`, `reyd-instruktazh`, `reyd-vremya-prishlo` | Федеральное здание в Бостоне |
| `pobeg-iz-innsmuta-ru/scene/tsel-4-sbor-v-bostonskikh-dokakh` | бостонские доки |
| `podzemka-ru/scene/chto-pomnit-lyao-khan` | полиция Монреаля |
| `poselok-berezovyy-ru/scene/poezdka-v-tyurmu` | колония № 45 |
| `fears-sharp-little-needles-en/scene/separation-missing`, `separation-work-computer` | медицинская школа Кейс Вестерн |
| `fears-sharp-little-needles-en/scene/separation-friends-and-coworkers` | медицинская школа Кейс Вестерн — **вывод из текста (Р-41)**: коллеги и научный руководитель — по месту работы Би-Би; мать и друзья — где угодно |
| `fears-sharp-little-needles-en/scene/dissociation-abduction` | ночной рейс Сан-Диего — Сиэтл |

Дополнительно: предмет `fears-sharp-little-needles-en/item/separation-bb-work-computer` получил `found_at` → медицинская
школа Кейс Вестерн. В сценах, где в `quality.notes` было «записи места нет», пометка убрана или переписана.

## 3. Три исторических персонажа «Побега из Иннсмута»

У персонажа нет поля `refs`, а `relations` — связи между персонажами и существами, поэтому ссылки поставлены со стороны
мест (бывшие и упомянутые люди — в `refs` места, Р-82) и строк хронологии Иннсмута:

| Персонаж | Ссылки |
|---|---|
| `pobeg-iz-innsmuta-ru/character/dzhebedayya-gilman` | `coc:location:innsmouth-703-otel-dom-gilmana` → `refs`; `coc:location:innsmouth`, хронология, строка 1834 → `refs` (с. 7, 47) |
| `pobeg-iz-innsmuta-ru/character/dzhon-smit` | `coc:location:innsmouth-1011-rif-dyavola` → `refs`; хронология, строка 1616 (с. 7, 57) |
| `pobeg-iz-innsmuta-ru/character/tomas-martin` | хронология, строка 1678 «Верфь Мартина» (с. 3: «В 1678 году Томас Мартин открыл верфь»; с. 7). К Старой верфи Мартина (906) не привязан: книга не говорит, его ли это верфь |

## 4. Ссылки на страницы

| Запись | Добавлено в `sources` |
|---|---|
| `coc:location:arkham` | arkham-guide-hort-ru, с. 8 (физ. 8) — «Предисловие» |
| `coc:location:arkham-uptown` | arkham-guide-hort-ru, с. 90 (физ. 90) — «Аптаун» |
| `karnaval-bezumiya-ru/scenario/karnaval-bezumiya` | karnaval-bezumiya-ru, с. 80 (физ. 80) — «Таблица Нереальности 1», пункты 5–8; в `tables[0].source.note` — «пункты 5–8 — с. 80» |
| `sny-o-yaponii-ru/scenario/sny-o-yaponii` | sny-o-yaponii-ru, с. 45 (физ. 46) — истории 7–8; с. 46 (физ. 47) — «Возможные реакции японцев…»; в `source.note` таблицы историй — «истории 7–8 — с. 45». Таблица реакций уже ссылалась на с. 46, но проверка смотрит только `sources` записи |
| шесть готовых сыщиков «Масок»: `madelyn-brown` (с. 86), `archibald-washington` (88), `winston-greene` (90), `jennifer-smallwood` (92), `johan-braun` (93), `francoise-pelletier` (95) | masks-of-nyarlathotep-ru-players, печатная = физическая |
| ещё четыре готовых сыщика: `arthur-dibden` (87), `eleanor-butler` (89), `perry-astor` (91), `pranit-singh-dhillon` (94) | то же; после первых шести правок проверка показала их страницы отдельными пропусками (раньше они входили в общий пропуск с. 86–95) |

У всех десяти сыщиков характеристики, ПЗ, Рассудок и возраст на русском листе совпадают с записями (по английской книге);
навыки не сверялись — это сказано в `note` источника.

## Предложения правок вне задания (не применены)

`proposals-links.json` (проверено `apply.py --dry-run`):
`chernovodnyy-ruchey-ru/location/blackwater-sklad-makbrayda` — `part_of` → `coc:location:boston-doki`;
`pobeg-iz-innsmuta-ru/organization/proekt-zavet` — штаб в `based_at` → Федеральное здание (пометка «отдельной записи нет»
устарела); `refs` городов Бостон, Ипсвич, Кливленд, Монреаль, Берёзовый — на новые места (навигация, без `corrections`).

## Не сделано и почему

- Бунгало Каулеса на Пикман-стрит (Masks, с. 136) — записи нет, в `where` сцены не ставилось: в задании его нет, а
  «Pickman between West and Garrison» — граница районов Кампус и Аптаун, район неочевиден. Кандидат в новую запись
  (`masks-of-nyarlathotep-en/location/…`, вероятно Аптаун — там описаны старые дома Уэст-Пикман-стрит).
- 60 сцен «без места» из verify-scenarios.md (письма, звонки, сны, итоги) — по Р-243 остаются без `where`.
- Описания общих городов (Бостон, Ипсвич, Кливленд, Монреаль) новыми абзацами не дополнялись: места видны в гайде
  через `part_of`; ссылки — в предложениях.
- Описания исторических персонажей не менялись: связи поставлены со стороны мест и хронологии.

## Сомнения

- Кейс Вестерн, «Беседа с друзьями и коллегами»: место — вывод из текста (Р-41), помечено в `note`.
- Сцена «Уэйт и Дерби»: в `where` — особняк Кроуниншилд как место передачи рукописи; где Эфраим приходит к сыщикам,
  книга не говорит (пометка в `note` и `quality.notes`).
- Персонал Федерального здания (агент Дрю, мисс Джеймсон) — в `residents`, как сотрудники «Бостон Глоуб» в
  `coc:location:boston-globe`; доктор Бигсби — в `refs`: что она работает в медицинской школе, книга прямо не говорит.
- Самолёт оформлен типом «корабль» (Р-189 «пароход, дирижабль и т. п.»), чтобы быть вершиной гайда без города.
