# Ктулху: Тёмные века — три сценария (часть ages-scenarios)

Книга `temnye-veka-tri-stsenariya-ru` (фанатский перевод Cthulhu Dark Ages 7e, надёжный), физ. 222–251 = с. 221–250.
Числа сверены с английским оригиналом `cthulhu-dark-ages-en` (с. 176–201 по слою pages.py). Записи — в
`kb/books/temnye-veka-tri-stsenariya-ru/<вид>/{hunt,wessex,esewald}-*.json`; карты — `app/maps/hunt-*.jpg`, картинки —
`app/art/{handouts,scenes,locations}/…`. Префикс id ниже — `temnye-veka-tri-stsenariya-ru/`; общие записи — `coc:…`.
Люди и места Тотбурга — записи части ages-totburg (`…/character/totburg-*`, `coc:location:totburg-*`), здесь только ссылки.

## Глава 9. «Охота» (с. 221–231)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Охота (вступление) | 221 | `scenario/hunt-the-hunt` (summary) |
| Информация для Хранителя | 221 | `scenario/hunt-the-hunt` (keeper_info) |
| Вовлечение сыщиков | 221 | `scenario/hunt-the-hunt` (hook) |
| Ферма | 221–222 | `scene/hunt-the-farm`, `location/hunt-eorhelm-farm` |
| Где ферма? (врезка) | 222 | `scenario/hunt-the-hunt` (advice), `location/hunt-eorhelm-farm` |
| Карта фермы Йорхельма | 222 | `map/hunt-eorhelm-farm` (`app/maps/hunt-eorhelm-farm.jpg`) |
| Эльхаф | 222–223 | `scene/hunt-ealhaf`, `character/hunt-ealhaf` |
| Восстание мертвецов (врезка) | 223 | `scene/hunt-dead-rise`, `character/hunt-angifu`, `creature/hunt-undead-hound` |
| Беот | 223–224 | `scene/hunt-beot` |
| Эдда (Эадда) | 224 | `scene/hunt-beot`; `character/totburg-eadda` |
| Унферт | 224 | `scene/hunt-beot`; `character/totburg-unfurth` |
| Минуя Тотбург (врезка) | 224 | `scenario/hunt-the-hunt` (advice) |
| Дополнительная информация в Тотбурге | 224–225 | `scene/hunt-totburg-information` |
| Судьба Свейна и хартверу (врезка) | 224 | `scenario/hunt-the-hunt` (advice) |
| Раздаточный материал: Охота 1 (врезка) | 225 | `handout/hunt-handout-1` |
| Следы | 225 | `scene/hunt-tracks`, `location/hunt-wolf-den`, `item/hunt-ichor-knife`, `item/hunt-milk-waterskin` |
| Getting Ahead of the Game (врезка оригинала, с. 180; в переводе её нет) | — | `scene/hunt-getting-ahead` (наш перевод, `translated`) |
| Собирая информацию | 226 | `scene/hunt-begilda` (вступление) |
| Бегильда | 226 | `scene/hunt-begilda`; `character/totburg-begilda` |
| Эдрик Кровавая Рука | 226 | `scene/hunt-edric`; `character/totburg-edric`, `character/totburg-hlodere` |
| Дополнительная встреча: Зачарованное дерево | 226–227 | `scene/hunt-enchanted-tree`, `location/hunt-enchanted-tree`, `creature/hunt-ent` |
| Деревня Готии | 227–228 | `scene/hunt-gotii-village`; место `coc:location:totburg-gotii-village` (+ предложение); `item/hunt-moon-lens` |
| Карта деревни Готии | 227 | `map/hunt-gotii-village` (`app/maps/hunt-gotii-village.jpg`) |
| Успех | 228 | `scene/hunt-success` |
| Награда | 228 | `scenario/hunt-the-hunt` (conclusion) |
| Приложение А: персонажи — Ангифу | 229 | `character/hunt-angifu` |
| Гончая-нежить, Несчастная Йорхельма | 229 | `creature/hunt-undead-hound` |
| Бегильда, 42 года | 229 | `character/totburg-begilda` (числа совпадают, своей записи нет) |
| Эдрик, 24 года | 229 | `character/totburg-edric` (числа совпадают) |
| Хлодер, члены банды Эдрика | 230 | `character/totburg-hlodere` (числа совпадают) |
| Готии, ярые культисты | 230 | `creature/hunt-gotii` (instance_of `coc:creature:gotii`) |
| Вель-вульф; ВЕЛЬ-ВУЛЬФ, проявления тёмной матери | 230 | `creature/hunt-wael-wulf` |
| Приложение Б: раздаточный материал | 231 | `handout/hunt-handout-1` (картинка `app/art/handouts/hunt-handout-1.webp`) |

Прочие люди: `character/hunt-eorhelm`, `character/hunt-inric`, `character/hunt-gaius-aquilius-collatinus`.

## Глава 10. «Гибель, пришедшая в Уэссекс» (с. 233–241)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Гибель, пришедшая в Уэссекс (вступление) | 233 | `scenario/wessex-doom-that-came-to-wessex` (summary) |
| Информация для Хранителя | 233 | `scenario/wessex-doom-that-came-to-wessex` (keeper_info) |
| Вовлечение сыщиков | 233 | `scenario/wessex-doom-that-came-to-wessex` (hook) |
| Морские волки | 233–234 | `scene/wessex-sea-wolves`, `character/wessex-vikings` |
| Ужас Хотера | 234 | `scene/wessex-horror-of-hothere` |
| В монастырь | 234–235 | `scene/wessex-to-the-monastery`; место `coc:location:totburg-st-swithuns-monastery` |
| Монахи (семь смертных грехов) | 235 | `scene/wessex-monks` (картинка `app/art/scenes/wessex-monks.webp`) |
| Что Фет может сделать с вами? (врезка) | 236 | `scene/wessex-monastery-clues`, `creature/wessex-pheth` (abilities) |
| События и улики в монастыре | 236–237 | `scene/wessex-monastery-clues`, `item/wessex-pheth-cask` |
| Обратно в Тотбург | 237 | `scene/wessex-back-in-totburg` |
| Бред Хигерда | 237–238 | `scene/wessex-hygerd-ravings`, `handout/wessex-hygerd-clue` |
| Назад в монастырь | 238 | `scene/wessex-back-to-monastery`, `item/wessex-unmixed-wine` |
| Экзорцизм | 238 | `scene/wessex-exorcism` |
| Сделка с демоном (врезка) | 238 | `scene/wessex-exorcism` |
| Итоги и награды | 240 | `scenario/wessex-doom-that-came-to-wessex` (conclusion) |
| Приложение А: Викинг, типичный налётчик | 240 | `character/wessex-vikings` |
| Хартверу, типичный солдат | 240 | `character/totburg-hearthweru` + предложение варианта (МОЩ 60, Рассудок 60, ПМ 12) |
| Мусулиос, 34 года | 240 | `character/wessex-mousoulios` |
| Монахи — см. главу о Тотбурге | 241 | `character/totburg-monks` (числа совпадают) |
| Фет (уникальное существо — или Ллойгор, или аватар); ФЕТ, демон греха | 241 | `creature/wessex-pheth` |

## Глава 11. «Эсевальд» (с. 243–250)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Эсевальд (вступление) | 243 | `scenario/esewald-eseweald` (summary) |
| Информация для Хранителя | 243 | `scenario/esewald-eseweald` (keeper_info) |
| Вовлечение сыщиков | 243–244 | `scenario/esewald-eseweald` (hook), `scene/esewald-involvement` |
| Информация в Тотбурге: Хартверу; Иса; Эдд; Хафден; Вифрун; Хигерд; Эрнвульф; Витгар; Гутлаф; Другие жители Тотбурга | 244–245 | `scene/esewald-totburg-information`; `character/esewald-ingar`, `-osred`, `-cenric`, `-alfgar`, `-edwulf` |
| Слухи о Лесе | 245 | `location/esewald-forest-of-dean` (таблица «Слухи о Лесе») |
| Выдвигаться | 246 | `scene/esewald-heading-out` |
| Лагерь | 246 | `scene/esewald-camp`, `location/esewald-camp`, `item/esewald-cloak-clasp`, `item/esewald-wifrun-charm`, `item/esewald-omagh-cloak-shred`, `character/esewald-wadu` |
| Кордуон | 246 | `scene/esewald-corduon`, `location/esewald-corduon`, `character/esewald-anwar`, `character/esewald-eiddol` |
| Отшельница | 247 | `scene/esewald-hermit`, `location/esewald-eurwen-shelter`, `character/esewald-eurwen`, `handout/esewald-eurwen-riddle` |
| Пуцел | 247 | `scene/esewald-pucel`, `creature/esewald-pucel` |
| Угольщики | 247 | `scene/esewald-charcoal-burners`, `location/esewald-omagh-hut`, `item/esewald-arm-rings`, `item/esewald-wadu-head` |
| Эсевальд | 247 | `scene/esewald-eseweald`; место `coc:location:totburg-eseweald` (+ предложение) |
| Роща Хорига | 248 | `scene/esewald-horig-grove`, `location/esewald-horig-grove` (part_of `coc:location:totburg-eseweald`, картинка) |
| Итоги | 249 | `scenario/esewald-eseweald` (conclusion) |
| Приложение А: Викинги или кимрийские воины | 249 | `character/esewald-warriors` |
| Волк | 249 | `creature/esewald-wolf` (instance_of `coc:creature:wolf`) |
| Ома, угольщик | 249 | `character/esewald-omagh` |
| Телери, жена угольщика | 249 | `character/esewald-teleri` |
| Пуцел | 250 | `creature/esewald-pucel` (instance_of `coc:creature:pucel`) |
| Медведь, нежить-хранитель | 250 | `creature/esewald-undead-bear` (instance_of `coc:creature:bear`) |
| Хориг | 250 | `creature/esewald-horig` (instance_of `coc:creature:horig`) |

Прочее: `item/esewald-osred-cross`.

## Расхождения перевода с оригиналом и опечатки

| Запись | Что | Как в базе |
|---|---|---|
| `scenario/hunt-the-hunt` | «Награда»: перевод «принимали участие в бою», оригинал «took part in the beot» | по оригиналу, `corrections` (Р-147) |
| `scene/hunt-beot` | перевод «Освин первым… хвастается», оригинал — Свейн; Эадда в переводе «Эдда» в женском роде | по оригиналу, `corrections` |
| `character/hunt-angifu` | оригинал БкУ 0 / Комплекция 0 при СИЛ 65 + ТЕЛ 65 | как в переводе (+1d4 / 1), пометка |
| `creature/hunt-undead-hound`, `creature/esewald-wolf`, `character/esewald-teleri` | ПЗ перевода и оригинала расходятся на 1 (округление) | как в переводе, пометка |
| `creature/hunt-gotii` | средние ИНТ, МОЩ, НАР, ПЗ в оригинале не сходятся с бросками | как в переводе (сходятся), пометка |
| `character/esewald-teleri` | ПМ 9 в переводе, 13 в оригинале (= МОЩ 65 / 5) | 13, `corrections` (Р-147) |
| `character/esewald-teleri` | Скорость 8 (по правилам 9), Уклонение 32% (по правилам 37%) — так и в оригинале | как напечатано, `errata` |
| `character/esewald-omagh` | Уклонение 30% (по правилам 35%); «Создание угля 85%» — числа нет в оригинале | как напечатано, `errata`, пометка |
| `creature/esewald-pucel` | радиус взрыва «10 шагов» / «10 метров», в оригинале 10 футов | 3 м, `corrections` (Р-147) |
| `creature/esewald-horig` | БкУ –2 в переводе, 0 в оригинале | как в переводе, пометка |
| `handout/hunt-handout-1` | «decimated» → «уничтожил», «found crushed» → «найдена» | текст как напечатан, пометка |
| `handout/wessex-hygerd-clue`, `handout/esewald-eurwen-riddle`, `scene/esewald-totburg-information` | вольный перевод цитат (27-й «день», загадка, «Приготовь пир огня») | как напечатано, английский текст рядом |

## Предложения

`checks/20261114-ru-more/proposals-ages-scenarios.json` — 57 правок (пробный прогон `apply.py --dry-run` проходит):
ссылки (`refs`) мест Тотбурга на записи сценариев (гайд города, Р-132); жители деревни готиев и Эзевельда; абзацы
«В „Охоте“…», «В „Эсевальде“…», «В „Гибели…“…» в описаниях деревни готиев, Эзевельда и монастыря (Р-125); вариант
профиля хартверу из «Гибели» (МОЩ 60, Рассудок 60, ПМ 12) в `character/totburg-hearthweru`.

## Не взято

- Полностраничные и вводные иллюстрации глав (физ. 221, 233, 240, 243: «страница из Бестиария Эшмола», «воры врываются в
  усыпальницу Святого Эдмунда», «Портрет Матфея», «влияние Хорига») — арт без данных; взяты три иллюстрации к сценам
  (деревня готиев, монахи под властью Фета, роща Хорига), раздатка и две карты.
- Колонтитулы, номера страниц, подписи «Напротив: …» — оформление.
- Физ. 252 (глоссарий) — часть ages-appendices.
- Ссылки на оружие Тёмных веков (`attacks[].weapon` у копья, меча, топора, лука) не поставлены: записей оружия Тёмных
  веков в базе на момент переноса нет; «Драка» связана с `coc:weapon:unarmed`, факел пуцела — с `coc:weapon:burning-torch`.
- Река Северн — без записи (места-реки в базе нет), упоминается текстом.
