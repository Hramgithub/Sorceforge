# Keeper's Companion — часть appendices (с. 193–215)

Приложения A «Weapons», B «Vehicle Chases», C «Play Aids», D «Pre-Generated Investigators» и листы сыщика.
Книга `keepers-companion-en` (печатная страница = физическая − 1). Весь русский текст — наш перевод
(`translated`, Р-21). Записи:

- 13 правил `kb/rules/kc-*.json`: `kc-appendix-a-weapons`, `kc-weapons-key`, `kc-weapon-notes`, `kc-vehicle-chases`,
  `kc-vehicular-combat`, `kc-vehicular-and-passenger-damage`, `kc-shooting-tires`, `kc-vehicular-collisions`,
  `kc-vehicle-reference-charts`, `kc-running-a-vehicle-chase`, `kc-content-checklist`, `kc-pre-generated-investigators`,
  `kc-investigator-sheets`;
- 1 таблица с броском: `kb/tables/kc-vehicle-chase-challenges.json`;
- 20 новых записей оружия `kb/weapons/` (строки таблиц 7–14 без позиции в таблице XVII «Книги хранителя»):
  `derringer-41-remington-model-95`, `mauser-c96-broomhandle`, `makarov-pm`, `tt-33-type-54`, `colt-single-action-army`,
  `webley-mk-vi`, `223-semi-automatic-rifle`, `45-70-lever-action-rifle`, `dragunov-rifle`, `m39-enhanced-marksman-rifle`,
  `bolt-action-sniper-rifle`, `410-shotgun-1b`, `winchester-model-1887`, `benelli-m4`, `mp-40-sten-gun`, `ppsh-41`,
  `fn-p90`, `mauser-m712-schnellfeuer`, `m60`, `rpg-7`;
- предложения правок общих записей — `proposals-appendices.json` (217): 88 записей оружия, чьи строки есть в
  пересмотренных таблицах, получают источник «Компаньона», отличия чисел — в `source_variants` (числа справочника
  остаются по «Книге хранителя», Р-124, Р-58) и английское название строки — в `aliases`; 6 записей получают источник и
  `source_variants` по «Примечаниям к оружию» («используйте эти значения для …»): `ak-74`, `beretta-m9`,
  `galil-assault-rifle`, `vickers-303-machine-gun`, `mosin-1891-30`, `45-revolver`; `kc-x-card` — источник с. 208
  и правка пометки. Пробный прогон `apply.py --dry-run`: 217 правок, 95 записей, всё ложится.

Готовых сыщиков (pregen) в книге нет: приложение D печатает только восемь портретов без подписей и чистые листы
сыщика, а листы самих сыщиков даны как скачиваемое приложение на chaosium.com. Поэтому записей персонажей в
`kb/books/keepers-companion-en/characters/` эта часть не завела (ничего не придумано).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Appendices (титул) | 193 | — (заголовок раздела книги) |
| Appendix A: Weapons (вступление, *, (i), NB) | 193 | `coc:rule:kc-appendix-a-weapons` |
| Table 7: Hand-to-Hand Weapons | 193–194 | `coc:rule:kc-appendix-a-weapons` (`tables[0]`); 28 строк → записи `kb/weapons/` (все прежние) |
| Table 8: Handguns | 194–195 | `tables[1]`; 17 строк: 11 прежних записей, 6 новых (дерринджер .41, «Маузер» C96, «Макаров», ТТ-33, «Кольт» SAA, «Вебли» Mk VI) |
| Table 9: Rifles | 195–196 | `tables[2]`; 16 строк: 11 прежних, 5 новых (.223, .45/70, «Драгунов», M39 EMR, снайперская со скользящим затвором) |
| Table 10: Shotguns (дробь, пули, 2B) | 196 | `tables[3]` и текст правила; 8 строк: 5 прежних, 3 новых (.410, «Винчестер» 1887, «Бенелли» M4) |
| Table 11: Assault Rifles | 197 | `tables[4]`; 4 строки — прежние записи |
| Table 12: Submachine Guns | 197 | `tables[5]`; 9 строк: 5 прежних, 4 новых (MP-40/«Стен», ППШ-41, FN P90, «Маузер» M712) |
| Table 13: Machine Guns | 198 | `tables[6]`; 9 строк: 8 прежних, 1 новая (M60) |
| Table 14: Explosives, Heavy Weapons, Misc. | 198–199 | `tables[7]`; 17 строк: 16 прежних, 1 новая (РПГ-7) |
| Weapons Key | 199–201 | `coc:rule:kc-weapons-key` |
| Weapon Notes | 201–203 | `coc:rule:kc-weapon-notes`; замены «используйте эти значения для …» — ещё и в `source_variants` 6 записей (предложения) |
| Appendix B: Vehicle Chases (вступление) | 203 | `coc:rule:kc-vehicle-chases` |
| Locations & Vehicles | 203 | `coc:rule:kc-vehicle-chases` |
| Vehicular Combat | 203 | `coc:rule:kc-vehicular-combat` |
| Crash: T-Bone or Head-On | 203 | `coc:rule:kc-vehicular-combat` |
| Rear-End or Sideswipe | 204 | `coc:rule:kc-vehicular-combat` |
| Example (тёмная молодь) | 204 | `coc:rule:kc-vehicular-combat` (`examples`) |
| Handling Roll | 204 | `coc:rule:kc-vehicular-combat` |
| Example (Хейли и культист) | 205 | `coc:rule:kc-vehicular-combat` (`examples`) |
| Vehicular & Passenger Damage | 205 | `coc:rule:kc-vehicular-and-passenger-damage` |
| Vehicle Suffers Damage Equal to or More Than its Full Build Value in One Incident | 205 | `coc:rule:kc-vehicular-and-passenger-damage` |
| Vehicle Suffers Damage Less Than its Full Build Value | 205 | `coc:rule:kc-vehicular-and-passenger-damage` |
| Cumulative Damage Has Reduced Vehicle's Build to Zero | 205 | `coc:rule:kc-vehicular-and-passenger-damage` |
| Example (машина и мотоцикл) | 205 | `coc:rule:kc-vehicular-and-passenger-damage` (`examples`) |
| Shooting Tires | 205, 207 | `coc:rule:kc-shooting-tires` |
| Table 15: Vehicular Collisions | 205 | `coc:rule:kc-vehicular-collisions` (`tables`; бросок не делается — таблица в правиле, Р-171) |
| Table 16: Vehicle Reference Charts (5 таблиц) и Key | 206 | `coc:rule:kc-vehicle-reference-charts` |
| Summary: Running a Vehicle Chase, Notes | 207 | `coc:rule:kc-running-a-vehicle-chase` |
| Sample Challenges for Vehicle Chases | 207 | `coc:table:kc-vehicle-chase-challenges` (1d6) |
| Appendix C: Play Aids | 208 | `coc:rule:kc-content-checklist` (псевдоним) |
| Content Checklist (Optional) | 208 | `coc:rule:kc-content-checklist` |
| Call of Cthulhu X-Card | 208 | `coc:rule:kc-x-card` (часть sanity-play) — источник с. 208 предложением; упомянута в `kc-content-checklist` |
| Content Checklist (бланк): Your Horror May Vary!, Specific Themes, Horror, Themes | 209 | `coc:rule:kc-content-checklist` |
| Appendix D: Pre-Generated Investigators | 210 | `coc:rule:kc-pre-generated-investigators` |
| 1920s Era Investigator (лист, 2 страницы) | 211–212 | `coc:rule:kc-investigator-sheets` |
| Pulp Hero (лист, 2 страницы) | 213–214 | `coc:rule:kc-investigator-sheets` |
| Appendix E: Author Biographies | 215 | не взято (см. ниже) |

## Не взято

- Подписи к иллюстрациям: «Opposite: A Useful Find» (с. 193), «Kitted Up» (с. 200), «Free Fire» (с. 202),
  «Blow the Doors Off» (с. 204) — подписи к картинкам, без механики.
- Восемь портретов готовых сыщиков (с. 210) — иллюстрации без имён и данных; листов сыщиков в книге нет (скачиваются на
  chaosium.com), поэтому записей `pregen` нет. Если владелец скачает листы, их можно завести отдельно.
- Картинка X-карты (с. 208) — изображение; текст о ней — в `kc-x-card` (предложение) и `kc-content-checklist`.
- Оформление листов сыщика (рамки, пустые графы, рисунки Ктулху и крылатого глаза, копирайт) — в правиле
  `kc-investigator-sheets` описано содержание листов, графика не переносится.
- Appendix E: Author Biographies (с. 215) — биографии авторов (Paul Fricker, Mike Mason, James Coquillat, Adam Gauntlet,
  Al Smith), выходные сведения, не материал игры.

## Опечатки и сомнения

- `kc-weapons-key` (errata, исправлено): ссылка «Full Auto “Spray and Pray” (page 167)» (с. 200) — огонь веером на с. 67.
- `kc-investigator-sheets` (errata, как напечатано): на листе пульп-героя (с. 213) Механика 20%, Верховая езда 20%,
  Плавание 30%; на листе 1920-х, в обновлённом списке навыков «Компаньона» и в «Пульп-Ктулху» (с. 36) — 10%, 05%, 20%.
- `kc-vehicular-collisions`: у «мясорубки» урон «12D20 hit points» — единственные d20 в таблице; оставлено как
  напечатано, в пометке.
- Таблица 14: «All explosives and heavy weapons can impale (i)» — как напечатано (пометка в `kc-appendix-a-weapons`).
- Сопоставление строк «Компаньона» с записями справочника там, где названия разные, — вывод из текста (Р-41):
  «Winchester Model 1894 (.30-30)» → `30-lever-action-carbine`, «M1911 Pistol (.45 ACP)» → `45-automatic`,
  «.22 Semi-Automatic (.22 LR)» → `22-short-automatic`, «Belt-Fed Machine Gun (.30-06)» → `browning-m1917a1-30`,
  «Elephant Gun (.416 Rigby)» → `elephant-gun-2b`, «Gatling Gun (.30-06)» → `gatling-gun-1882`,
  «MP-28» → `bergmann-mp18-mp28`, «Stun Gun» → `taser-*`, «Browning M2 (.50 BMG)» → `browning-50-machine-gun`
  (запись из «Побега из Иннсмута» с навыком Артиллерия и своими числами; числа «Компаньона» — в `source_variants`).

## Вопросы владельцу

1. Новые позиции «Компаньона» рядом с близкими записями из других источников, не объединены:
   `mauser-m712-schnellfeuer` и `mauser-c96-broomhandle` ↔ модель каталога `mauser-c96-m1930-m1932` (M1932 —
   автоматический «Маузер», вероятно, тот же M712); `tt-33-type-54` ↔ `tt-tokarev` (TT-30 из «Холодного урожая»,
   `model_of` = `32-automatic`); `webley-mk-vi` ↔ `webley-revolver` из «Масок» (1d10, как .38). Перевести ли
   `model_of` этих моделей на новые позиции?
2. `browning-50-machine-gun` (Иннсмут, `needs_review`): сделать ли числа таблицы «Компаньона» (Стрельба (пулемёт),
   2d10+1d8+6, 150 м) основными, а иннсмутские — вариантом?
3. Навык Стрельба (пистолет-пулемёт) в «Компаньоне» убран: у пистолетов-пулемётов справочника (`thompson-smg`,
   `uzi-smg`, `heckler-koch-mp5` и др.) новый навык записан только в `source_variants`.
4. Пилотирование в «Компаньоне» разделено на Пилотирование самолёта и Пилотирование лодки; правила приложения B ссылаются
   на общий `coc:skill:pilot`.

## Для сведения и связи с другими частями

- Правила приложения B ссылаются на правила погони части system (`kc-chases`, `kc-chase-round-order`,
  `kc-movement-points-mvp`, `kc-location-challenges`, `kc-sample-challenges`, `kc-ending-the-chase`, `kc-chase-attacks`,
  `kc-round-table-initiative`) и на правила «Книги хранителя» (`vehicular-collisions`, `vehicle-reference-charts`,
  `chase-conflict`, `driver-damage`).
- Правила приложения A ссылаются на `kc-automatic-fire-revisited`, `kc-explosions`, `kc-firearm-maneuvers`, `kc-skills`.
- `kc-content-checklist` ссылается на `kc-pre-game-chat` и `kc-x-card` (часть sanity-play).
