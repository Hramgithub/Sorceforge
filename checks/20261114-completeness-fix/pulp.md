# Pulp Cthulhu — цены и оружие 1930-х (часть «pulp», Р-242)

Книга `pulp-cthulhu-en`, гл. 15 «References», печатные с. 254–262 (физ. 255–263). В verify-rules.md те же
страницы названы 255–256 и 261–262 (физические номера); строки «missing» (цены 1930-х) и «partly» (списки оружия)
закрыты ниже. Все числа сверены по изображениям страниц.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 15 «References» (заголовок главы) | 254 | записи ниже (у главы нет своего текста) |
| Equipment (вступление о ценах) | 254 | `description` каждой из таблиц `coc:table:equipment-1930s-*` |
| For Your Pocket | 254 | `coc:table:equipment-1930s-pocket` |
| Clothing for Men | 254 | `coc:table:equipment-1930s-clothing` (раздел «Мужская одежда») |
| Clothing for Women | 254 | `coc:table:equipment-1930s-clothing` (раздел «Женская одежда») |
| Out and About | 254 | `coc:table:equipment-1930s-out-and-about` |
| Investigation | 254 | `coc:table:equipment-1930s-investigation` |
| For Your Home | 255 | `coc:table:equipment-1930s-home` |
| Transport | 255 | `coc:table:equipment-1930s-transport` |
| Something to Eat | 255 | `coc:table:equipment-1930s-food` (раздел «Продукты») |
| At the Restaurant (New York Prices) | 255 | `coc:table:equipment-1930s-food` (раздел «В ресторане») |
| Travel | 255 | `coc:table:equipment-1930s-travel` |
| Homes | 255 | `coc:table:equipment-1930s-homes` |
| Weapon Lists — Weapon (ближний бой и метательное, 23 строки) | 256–257 | `coc:rule:pulp-weapon-lists` (`tables[0]`); цена 1930-х — `cost.1930s` записей оружия |
| Handguns (i) (12 строк) | 258 | `coc:rule:pulp-weapon-lists` (`tables[1]`); новая запись `coc:weapon:44-revolver` |
| Rifles (i) (9 строк) | 258–259 | `coc:rule:pulp-weapon-lists` (`tables[2]`) |
| Shotguns* (7 строк) | 259 | `coc:rule:pulp-weapon-lists` (`tables[3]`) |
| Submachine guns* (4 строки) | 260 | `coc:rule:pulp-weapon-lists` (`tables[4]`); новая запись `coc:weapon:beretta-1938a`; MP18 и MP-28/II — `coc:weapon:bergmann-mp18-mp28` (`source_variants`) |
| Machine guns* (5 строк) | 260 | `coc:rule:pulp-weapon-lists` (`tables[5]`); новая запись `coc:weapon:lewis-gun-mk-vi` |
| Explosives, Heavy Weapons, misc. (9 строк) | 260–261 | `coc:rule:pulp-weapon-lists` (`tables[6]`) |
| Key: Acronyms, Skill, Damage, (i), Base Range, Uses per Round, Bullets in Gun, 1930s Cost, +DB, Burn, Burst/Full Auto, 1B/2B, 1/2–1/3, 1 or 2, NA | 261 | `coc:rule:pulp-weapon-lists` (`text`) |
| Malfunction (Mal); 2 yards, 3 yards, etc. | 262 | `coc:rule:pulp-weapon-lists` (`text`) |
| * See note below: Chainsaw, Col. Moran’s Air Rifle, Dynamite stick and Hand grenade, Garrote, Handguns, Rifles, Shotguns, Shotgun solid slugs | 262 | `coc:rule:pulp-weapon-lists` (`text`) |
| References and Sources of Inspiration (The 1930s, The Pulps, Popular Culture) | 262–263 | не взято (см. ниже) |

## Оружие: строка таблицы → запись

69 строк таблиц Pulp → 68 записей оружия (MP18 и MP-28/II — одна запись «Бергман» MP18/MP28).

- Новые записи (3): `coc:weapon:44-revolver` (.44 Revolver), `coc:weapon:beretta-1938a` (Beretta 1938A),
  `coc:weapon:lewis-gun-mk-vi` (Lewis Gun MK VI).
- Существующие записи (65): добавлены `cost.1930s` (как напечатано; «N/A» → «Нет», у камня «—» → `null`),
  источник `pulp-cthulhu-en` с номером страницы и элемент `corrections` (`cost.1930s`, Р-242).
- Числа Pulp, которые расходятся с записью справочника, — в `source_variants` (Р-124), 13 строк в 12 записях:
  `hatchet-sickle` (навык Fighting (Axe)), `spear-thrown` (урон 1d8+1+½ БкУ), `38-automatic` (6 патронов),
  `mauser-c96-broomhandle` (6 патронов, осечка 99), `41-revolver` (6 патронов), `30-06-bolt-action-rifle` (10 патронов),
  `shotgun-12-gauge-2b` (атак 1), `shotgun-12-gauge-pump` (осечка «0»), `shotgun-12-gauge-semi-auto` (атак 2),
  `shotgun-10-gauge-2b` (дальний урон 1d6), `bergmann-mp18-mp28` (две строки MP18 и MP-28/II),
  `lewis-gun-mark-i` (27/97 патронов).

## Предложения

`proposals-pulp.json` — 65 предложений: `append` «1930s» в `axes.era` каждой существующей записи оружия, получившей
цену 1930-х (пробный прогон `apply.py --dry-run` проходит).

## Не взято

| Что | Страница | Почему |
|---|---|---|
| «References and Sources of Inspiration»: книги о 1930-х, сайты, пульп-литература, фильмы | 262–263 | библиография не переносится (Р-242); не входит в задание части |
| Иллюстрация — газетная реклама (пишущая машинка Underwood, «Get Strong») | 255 | атмосферная иллюстрация, не импортируется (Р-241) |
| Отдельная запись бензопилы для 1930-х | 262 | в таблицах Pulp строки бензопилы нет, есть только примечание; оно — в тексте `coc:rule:pulp-weapon-lists`, запись `coc:weapon:chainsaw` не менялась |

## Опечатки и сомнения

- Дробовик помповый 12-го калибра: осечка напечатана «0» (с. 259), у остальных дробовиков и в «Книге хранителя» — 100.
  В таблице правила — как напечатано (`errata`), в записи оружия — `source_variants`.
- Пулемёт «Льюис» Mk I: «27/97» патронов (с. 260), в «Книге хранителя» 47/97 — вероятная опечатка, так же.
- Калибр «Льюиса» Mk VI в книге не указан и не поставлен (вопрос владельцу); у записи каталога
  `bsa-lewis-mk-iii-savage-lewis-m1917` псевдоним «Savage-Lewis M1917 (MK VI)» — записи не объединены.
- Пронзающие пистолеты-пулемёты и пулемёты: в Pulp у заголовков «*», а не «(i)»; `impaling: true` у новых записей —
  по таблице XVII «Книги хранителя» (вывод, Р-41, в `corrections`).
