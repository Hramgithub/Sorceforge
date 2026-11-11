# «Некрополис» (The Necropolis), с. 12–33

Книга `necropolis-en` (PDF — 22 страницы; печатная страница = физическая + 11: физ. 1 = с. 12, физ. 22 = с. 33; страницы 23 в PDF нет). Книга — отрывок сборника «Gateways to Terror» (колонтитулы), ссылки на его вводную главу («Using Luck, page 6», «Sanity section in the Introduction, page 11») ведут за пределы файла.
Решения: Р-214, Р-190, Р-206, Р-209, Р-134, Р-150. Русский текст — наш перевод (`translated`, Р-21); русский файл в папке книги — машинный перевод, не источник (не читался).
Записи — `kb/books/necropolis-en/*/necropolis-*`, сценарий — `necropolis-en/scenario/necropolis`; общий город — `coc:location:luxor` (новый, `kb/locations/luxor.json`); карты — `app/maps/necropolis-*.jpg`.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Иллюстрация «The Abomination wakes!» | 12 | не взято (см. ниже); описание Мерзости — `creature/necropolis-abomination` |
| The Necropolis (вступление: 26 ноября 1924 года, Долина царей, Говард Картер, Тутанхамон) | 13 | сценарий `necropolis`: `summary`; `location/necropolis-valley-of-the-kings` |
| Introduction | 13 | сценарий: `summary`, `keeper_info` |
| Scenario Structure (Set Up, Ready to Play, Discoveries in the Darkness, The Abomination Awakes, Conclusion, Epilogue — с минутами) | 13 | сценарий: `advice`; таблица сценария «Ход сценария по времени» |
| About the Investigators | 14 | сценарий: `hook`, `advice`; готовые сыщики (`description`) |
| The Archaeologist | 14 | `character/necropolis-archaeologist` (`description`) |
| The Professor of Languages | 14 | `character/necropolis-professor-of-languages` (`description`) |
| The Dilettante | 14–15 | `character/necropolis-dilettante` (`description`; лорд Карнарвон — текстом) |
| The Ex-Soldier | 15 | `character/necropolis-ex-soldier` (`description`) |
| Fewer Than Four Players | 15 | сценарий: `advice`; способность «Если игрок один» у Профессора языков; `legend` готовых сыщиков |
| Additional/Alternate Investigators (Crew Chief, Plucky Kid; свои сыщики; полезные навыки) | 15 | сценарий: `advice`, `hook` |
| Setting Up (текст для чтения) | 16 | `scene/necropolis-setting-up`; сценарий: `hook`; `location/necropolis-steps` |
| Start: Imprisoned in the Valley of the Kings (текст для чтения, Рассудок, Слух, повторная проверка) | 16–17 | `scene/necropolis-start`; `character/necropolis-laborers`; `location/necropolis-entry-chamber` |
| Discoveries in the Darkness (свет, Keeper note о тьме, факел, улики входной камеры) | 17 | `scene/necropolis-discoveries-in-the-darkness`; `item/necropolis-archaeologist-candles`; `location/necropolis-entry-chamber` |
| Areas of Interest | 18 | `scene/necropolis-discoveries-in-the-darkness`; `location/necropolis-tomb` |
| The Passageway (фрески, ниши с собаками, иероглифы, лаз, золотой сундук, два Keeper note об обвале) | 18, 20 | `scene/necropolis-the-passageway`; `location/necropolis-passageway`; `item/necropolis-gold-chest` |
| Opposite: The Necropolis map (карта Хранителя) | 19 | `map/necropolis-keeper-map` (`app/maps/necropolis-keeper-map.jpg`): 19 меток на подписях — Steps → ступени; Stone Slab → входная камера; Passageway, Hieroglyphs & Frescoes, Gold Chest & Table, Sealed Archway → коридор; Antechamber, Animal-Headed Statues, Sealed Door → передняя камера; Annex, Mural, Shrine & Skeleton, Archway (Broken Through) → боковая камера; Burial Chamber, Abomination’s Sarcophagus → погребальная камера; Treasury, Open Archway, Chest Containing Canopic Jars → сокровищница; The Necropolis → гробница |
| The Antechamber (обыск, Keeper note о Скрытности, стражи, оружие, плита) | 20 | `scene/necropolis-the-antechamber`; `location/necropolis-antechamber`; `item/necropolis-guardian-weapons` |
| The Annex (святилище, анх, скелет, сумка, дневник, две росписи) | 21 | `scene/necropolis-the-annex`; `location/necropolis-annex`; `character/necropolis-sascha-karner`, `-gerald-sutton`; `item/necropolis-karner-satchel`, `-karner-dynamite`, `-jewelry-sack` |
| Handout: Necropolis 1 | 22 | `handout/necropolis-1-karner-journal` |
| The Abomination Awakes! (и Keeper notes о бое) | 23–24 | `scene/necropolis-the-abomination-awakes`; сценарий: `advice` |
| Insane Investigators (врезка) | 23 | таблица сценария «Безумные сыщики»; способность «Безумие (врезка …)» у каждого готового сыщика |
| The Burial Chamber (и Keeper note о вёслах) | 24 | `scene/necropolis-the-burial-chamber`; `location/necropolis-burial-chamber`; `item/necropolis-oars` |
| The Treasury (сундук, канопы, проверки Археологии, сердце) | 24–25 | `scene/necropolis-the-treasury`; `location/necropolis-treasury`; `item/necropolis-canopic-jars`, `-abomination-heart` |
| Conclusion | 25 | `scene/necropolis-conclusion`; сценарий: `conclusion` |
| Eaten by the Abomination | 25 | `scene/necropolis-conclusion` |
| Explosion | 25 | `scene/necropolis-conclusion`; `item/necropolis-karner-dynamite` |
| Cave-in | 25 | `scene/necropolis-conclusion` |
| Slay the Abomination | 25 | `scene/necropolis-conclusion` |
| Escape | 25 | `scene/necropolis-conclusion`; `item/necropolis-karner-dynamite` |
| A Creative Escape | 25 | `scene/necropolis-conclusion` |
| Abomination Escapes | 26 | `scene/necropolis-conclusion`; `location/necropolis-luxor-environs`; `coc:location:luxor` |
| Rewards | 26 | сценарий: `conclusion`; `scene/necropolis-conclusion` |
| Epilogue | 26 | сценарий: `conclusion`; `scene/necropolis-conclusion` |
| The Monster: The Abomination, creature of the Necropolis (описание, статблок, Special Powers, Fighting, потеря Рассудка) | 26 | `creature/necropolis-abomination` |
| Archaeologist, age 36 (лист сыщика: статблок, Backstory, Roleplaying hooks, Possessions) | 27 | `character/necropolis-archaeologist` |
| Professor of Languages, age 40 | 28 | `character/necropolis-professor-of-languages` |
| Dilettante, age 44 | 29 | `character/necropolis-dilettante` |
| Ex-Soldier, age 29 | 30 | `character/necropolis-ex-soldier` |
| Collected Player Handouts: Handout: Necropolis 1 | 31 | `handout/necropolis-1-karner-journal` (второй источник) |
| Player map for the Necropolis—1 | 32 | `map/necropolis-player-map-1` (`app/maps/necropolis-player-map-1.jpg`): название → гробница; ступени, коридор, передняя и боковая камеры — вычисленные метки |
| Player map for the Necropolis—2 | 33 | `map/necropolis-player-map-2` (`app/maps/necropolis-player-map-2.jpg`): то же + погребальная камера и сокровищница |

Места (дерево гайда, Р-209): `coc:location:luxor` (город) → `necropolis-luxor-environs` (область «Окрестности Луксора») → `necropolis-valley-of-the-kings` → `necropolis-tomb` («Некрополь») → `necropolis-steps`, `-entry-chamber`, `-passageway`, `-antechamber`, `-annex`, `-burial-chamber`, `-treasury`. Через Каир завязка не идёт — `coc:location:cairo` не связан.

## Записи (43)

сценарий 1; сцены 10; места 10 (в том числе общий город Луксор); персонажи 7 (4 готовых сыщика, Карнер, Саттон, рабочие); существо 1; предметы 9; раздатка 1; карты 3; картинки карт 3.

## Опечатки и сомнения книги

- Мерзость: СИЛ 200 + ТЕЛ 90 = 290 → по таблице БкУ +4d6 и Комплекция 5; напечатаны +3D6 и 4 (согласованы между собой, но не с СИЛ и ТЕЛ; ПЗ 17 подтверждает ТЕЛ 90). Большинства нет — как напечатано, `errata`; **вопрос владельцу** (Р-36).
- Мерзость: хопеш «1D6+3D6», а в передней камере хопеш стража — 1D6+1+DB (с. 20): `errata`, как напечатано.
- Мерзость: урон Ближнего боя «3D6» — только БкУ, без урона кулака; как напечатано, пометка в `quality.notes`.
- «Start»: врезка «Insane Investigators» названа «on page 22», а напечатана на с. 23: `errata` сцены «Начало».
- Дилетант: «Navigate 10 (5/2)» без знака % — исправлено молча (Р-39); Археолог: «Fighitng (Brawl)» — молча.
- Профессор языков: Скорость 8 при 40 годах — без возрастной поправки (приём книги, Р-161); Уклонение 25% при ЛВК 45 — как напечатано.
- Бывший солдат: навыка «Firearms (Handgun)» в списке нет, шанс 60% — строкой «.32 revolver».

## Выводы из текста (Р-41) и придуманное

- Имена готовых сыщиков придуманы (Р-150): Сидни Хейл (Археолог), Эвелин Эшдаун (Профессор языков), Хилари Фэрфакс (Дилетант), Альберт Бриггс (Бывший солдат); книга оставляет «Name:» пустым, игроки выбирают имена сами (`player_chooses`). Имена рабочих (`names`) — тоже придуманы (Р-151).
- Луксор как ближайший город и область «Окрестности Луксора» — решение Р-214; в книге Луксора нет («nearest settlement»), положение города и Долины — справочно (`editorial_text`).
- Скелет в боковой камере — Карнер (паспорт и дневник рядом); мешок драгоценностей — собранный Карнером; Дилетант финансирует раскопки Археолога; вторую карту для игроков дают после пробуждения Мерзости — выводы, помечены в записях.

## Не взято

- Иллюстрации и фото без данных: «The Abomination wakes!» (с. 12), «Examples of potential investigators» (с. 14), «Locals can serve as great alternate investigators» (с. 15), «The Valley of the Kings» (с. 16), «The tomb corridor» (с. 17), «The passageway» (с. 18), «The treasury» (с. 24) — картинки в `app/art/` не входят в часть; кандидаты в `images` (Мерзость, места) — на усмотрение ведущего.
- Строки «Player Notes:» и «Luck:» листов сыщиков — пустые поля для игрока (Удача — `player_chooses`).
- Колонтитулы «Gateways to Terror» / «The Necropolis» и боковая надпись «Berlin» по краю страниц — оформление вёрстки.
- Ссылки на вводную главу сборника (с. 6, 11) — главы в файле нет; в сценах вместо них — ссылки на записи правил.

## Кандидаты в новые записи

- Говард Картер, лорд Карнарвон (Джордж), Тутанхамон, Маргарет Мюррей — упомянуты текстом, записей в базе нет.
- «Старший над рабочими» (Crew Chief) и «Бойкий подросток» (Plucky Kid) — идеи дополнительных сыщиков без листов; сейчас в `advice` сценария.

## Предложения правок общих записей

`proposals-necropolis.json` — предложений нет (0): Каир в завязке не участвует, общие существа (Чёрный фараон, Дитя Сфинкса, Ньярлатхотеп) связаны со стороны записей книги.
