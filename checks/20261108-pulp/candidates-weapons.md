# Pulp Cthulhu — кандидаты Р-191, часть `weapons` (оружие и «Средний прихвостень») — покрытие

Часть `weapons` (Р-191, Р-183). Записи: `kb/weapons/` (8 новых), `kb/books/pulp-cthulhu-en/characters/` (1 новая).
Ид-ы персонажей, мест и сцен ниже — без префикса `pulp-cthulhu-en/`. Предложения правок чужих записей —
`proposals-candidates-weapons.json` (25 предложений для 11 записей, все с `"correction": false`; пробный прогон
`apply.py --dry-run` проходит).

Источник списка — разделы «Кандидаты…» отчётов `villains.md`, `disintegrator.md`, `slowboat.md`, `hurricane.md`,
`system-sanity.md`, `magic-running.md`. Перед созданием проверены `kb/weapons/` и глоссарий (`tools/terms.py`):
совпадающих позиций нет, кроме дерринджера .25 (см. ниже).

## Кандидаты

| Кандидат (отчёт) | Страница | Итог | Ссылки (предложения) |
|---|---|---|---|
| Дадао (villains) | 123, 124 | запись `coc:weapon:dadao` «Дадао»; `model_of` — `coc:weapon:sword-heavy` (Р-105) | `character/feng-wang`, `character/servant-of-the-jade-emperor` — `attacks[].weapon`, пометки |
| «Кулак дракона» (villains; в книге — «Dragon Fist») | 123 | запись `coc:weapon:dragon-fist` «Кулак дракона» (с манёвром «опутать/обезоружить» в описании) | `character/feng-wang` — атака и манёвр, пометка |
| Кинжал Нефритового императора (villains) | 123 | запись `coc:weapon:dagger` «Кинжал» — книга не называет кинжал уникальным, это обычный «dagger» в профиле, поэтому id общий, числа — из профиля | `character/the-jade-emperor` — `attacks[].weapon`, пометка |
| Луч смерти профессора Кобальта (villains, magic-running) | 88, 124 | запись `coc:weapon:death-ray` «Луч смерти» (устройство гл. 6 и атака Кобальта) | `character/professor-cobalt` — `attacks[].weapon`, пометка; `coc:rule:pulp-death-ray` — `refs`, пометка |
| Дерринджер .45 (disintegrator) | 155 | запись `coc:weapon:45-derringer` «Дерринджер .45»; `model_of` — `coc:weapon:25-derringer` | `character/pietro-morasini` — `attacks[].weapon`, пометка |
| Пистолет автоматический .25 (disintegrator) | 156 | запись `coc:weapon:25-automatic` «Пистолет автоматический .25»; `model_of` — `coc:weapon:22-short-automatic` (тот же урон 1d6) | `character/valery-hind` — `attacks[].weapon`, пометка |
| Духовая трубка (slowboat) | 231 | запись `coc:weapon:blowgun` «Духовая трубка» | `character/wang-ma` — `attacks[].weapon`, пометка (у `character/sheng-tsin` статблока нет — он пользуется профилем Ван Ма) |
| Гарпун (hurricane) | 166 | запись `coc:weapon:harpoon` «Гарпун» | `location/harbor-master-office`, `scene/hurricane-harbor` — `refs`, пометки |
| «Average Mook» (system-sanity) | 63 | групповой профиль `character/average-mook` «Средний прихвостень» (Р-74, Р-151: `stock_type`, 5 придуманных имён, `editorial_text`) | `coc:rule:pulp-mooks` — `refs`, пометка |
| Дерринджер .25 (Скарлет Арахнис, с. 126) | 126 | не кандидат: позиция `coc:weapon:25-derringer` есть, атака уже ссылается на неё | — |

У всех новых записей оружия `axes.ruleset: "pulp"`, `axes.era: ["1930s"]`, флаг `translated`; не напечатанные книгой
колонки (дальность, атаки за раунд, боезапас, осечка, цена) — `null`. Выведенные значения (навык там, где книга его не
называет; БкУ; дальность «Касание» у оружия ближнего боя; «пронзающее» у пистолетов) — в `corrections` с «вывод из
текста (Р-41)».

## Заголовки книги, где стоят кандидаты

Полное покрытие заголовков с. 60–75 и 116–234 — в отчётах частей импорта Р-183 (`system-sanity.md`, `magic-running.md`,
`villains.md`, `disintegrator.md`, `hurricane.md`, `slowboat.md`, `pandora.md`); здесь — только места этой части.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Mooks — врезка «Average Mook» | 63 | `coc:rule:pulp-mooks` (таблицы) и `character/average-mook` |
| Death Ray (Sample Gadgets, гл. 6) | 88 | `coc:rule:pulp-death-ray`; оружие — `coc:weapon:death-ray` |
| The Jade Emperor — статблок (dagger) | 123 | `character/the-jade-emperor`; оружие — `coc:weapon:dagger` |
| Feng Wāng — статблок (Dadao, Dragon Fist) | 123 | `character/feng-wang`; оружие — `coc:weapon:dadao`, `coc:weapon:dragon-fist` |
| Servant of the Jade Emperor — статблок (Dadao) | 124 | `character/servant-of-the-jade-emperor`; оружие — `coc:weapon:dadao` |
| Professor Cobalt — статблок (Death ray) | 124 | `character/professor-cobalt`; оружие — `coc:weapon:death-ray` |
| Pietro Morasini — статблок (.45 Derringer) | 155 | `character/pietro-morasini`; оружие — `coc:weapon:45-derringer` |
| Valarie Hind — статблок (.25 auto) | 156 | `character/valery-hind`; оружие — `coc:weapon:25-automatic` |
| The Harbor (harpoons) | 166 | `scene/hurricane-harbor`, `location/harbor-master-office`; оружие — `coc:weapon:harpoon` |
| Wang Ma/Lo Mai — статблок (Blowgun) | 231 | `character/wang-ma`; оружие — `coc:weapon:blowgun` |

## Не взято

- Ссылка «владелец» из записи оружия (`refs`, как просит задание): в схеме оружия (`schemas/weapon.schema.json`,
  `additionalProperties: false`) поля `refs` нет. Владельцы названы в `description` оружия, связь идёт со стороны
  персонажа (`attacks[].weapon`, Р-59); ссылка на правило «Луч смерти» — со стороны правила (предложение). Нужно ли
  поле `refs` у оружия — вопрос владельцу.
- Цена: книга не даёт цену ни одного из этих видов оружия; у луча смерти есть только стоимость деталей для постройки
  (1 000 долларов) — она в описании, а не в `cost`.
- Псевдоним «Dragon's Fist» (так в задании) не добавлен: книга печатает только «Dragon Fist».

## Найдено попутно (не в списке задания, записи не заведены)

- Револьвер .44 (`character/alex-hubbard`, `character/herman-bukowsky`, 1d10+2): в таблице оружия «Пульп-Ктулху»
  (с. 258) есть позиция «.44 Revolver» (1d10+2, 15 ярдов, 1 (3), 6, $35, 100), в базе — только «Револьвер .44
  Магнум» (1d10+1d4+2); атаки без ссылки на оружие. Кандидат в позицию справочника.
- «.45 rifle 80% (40/16), damage 4D6/2D6/1D6» у Алекса Хаббарда (с. 231): урон дробовика у винтовки — возможная
  опечатка книги; атака без ссылки на оружие.
- Нож 1d4+1 у Пандоры Мулен (`character/pandora-moulin`): урон между «Нож маленький» и «Нож средний», атака без ссылки.
- «Barb caster» ми-го-наблюдателей (с. 157: 60%, 1d8 + застрявший шип 1d3 и кислота 1d10 три раунда, 20 шипов,
  дальность 30 ярдов) — оружие существа, хранится в `creature/mi-go-observers`; отдельной записи оружия нет.
- Дезинтегратор (`character/george-pelfry`, атака без навыка и урона) и «Handgun» Руссо (без чисел) — чисел оружия нет,
  записи не нужны.
- Кинжалы «Масок Ньярлатхотепа» (1d4, 1d4+2, 1d6 у разных персонажей) к `coc:weapon:dagger` не привязаны; при
  привязке их числа идут в `source_variants` (Р-124).

## Опечатки и сомнения

- `character/average-mook`: «Thompson SMG 30% (16/6)» — доли подходят к 32–33%; в записи 30% (15/6) по Р-35/Р-77
  (`errata`, `fixed: true`), как и в таблице `coc:rule:pulp-mooks`. Лишняя скобка «40% (20/8))» убрана молча (Р-39).
- В задании «Death Ray» отнесён к гл. 5; в книге это гл. 6 «Mythos Science and Gadgets», с. 88.
- Специализация «Кулака дракона» не выведена (книга: просто «Dragon Fist 80%»; по устройству ближе к цепу).
- Навык духовой трубки — Метание — вывод из текста, как в записи Ван Ма (у Ван Ма Метание 35%, трубка — 45%).
- `model_of` у «Пистолет автоматический .25» (на .22) и «Дадао» (на «Меч тяжёлый») — по Р-105 (тот же род и навык),
  выбор ближайшей позиции — наш.
