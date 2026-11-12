# «Dead Light and Other Dark Turns» (`dead-light-en`) — сверка заголовков (Р-134, Р-227)

Книга: `Сборники\Мёртвый свет и другие тёмные повороты (Dead Light and Other Dark Turns)\[EN 7e] dead-light-and-other-dark-turns.pdf`,
90 страниц; сборник Chaosium (2019, CHA23159) для «Зова Ктулху» 7-й редакции: два сценария («Dead Light» — Alan Bligh и Mike Mason,
переработка 2015 года; «Saturnine Chalice» — Matthew Sanderson) и шесть зацепок (дополнительный материал — Lynne Hardy). Редакция 7-я,
`ruleset` = `core`, `axes.era` = `1920s`. Текстовый слой хороший; статблоки, раздатки и карты сверены по изображениям страниц.

**Страницы:** физ. 1 — обложка, 2 — титул, 3 — выходные данные, 4 — оглавление (без номеров); физ. 5 = печатная 4 (пустая) и далее
печатная = физическая − 1 до физ. 89 (печатная 88); физ. 90 — задняя обложка. `offset` = −1 (в `books.json` смещение не записано).

**Перевод.** Русский текст — наш перевод с английского (флаг `translated`). Для «Dead Light» имена и названия взяты из фанатского перевода
«Мёртвый Свет» (Егор, проект «Дело Аркхэм», 2021; `[RU-фан 7e] myortvy_svet_for_call_of_cthulhu_rpg.pdf` — в `books.json` не записан,
поэтому в `sources` не стоит); числа — по оригиналу. Название сценария и существа — «Мертвенный свет», как на официальном русском листе
готовых сыщиков (`mertvennyy-svet-pregens-ru`); «Мёртвый Свет» — в псевдонимах. Расхождения фанатского перевода с оригиналом отмечены в
`quality.notes` записей (дробовик Джейка «20-го калибра» вместо 12-g, Уклонение Мэри 25% вместо 35%, НАР Билли 50 вместо 60, урон
поглощения «МОЩ» вместо ВЫН, гипноз — «ВЫН» вместо МОЩ).

**Города.** «Мертвенный свет» — по умолчанию на дороге из Аркхэма на север, в Ипсвич: область `location/deadlight-orchard-run` в общих
«Окрестностях Аркхэма» (`keepers-companion-en/location/arkham-environs`). «Сатурнова чаша» — место на выбор Хранителя, книга советует к
западу от Аркхэма: `location/chalice-weyland-estate` там же (вывод из текста, Р-41/Р-209). Зацепки мест не получили. Новых общих городов
нет; правки общих записей — `proposals-deadlight.json` (10).

**Готовые сыщики.** Шесть сыщиков сборника (скачиваются отдельно, с. 3) уже есть в базе: `mertvennyy-svet-ru/character/*` — ссылки из обоих
сценариев, не дублировались.

Префикс записей: `dead-light-en/<kind>/…` (ниже — без префикса). Файлы «Мертвенного света» — `deadlight-*`, «Сатурновой чаши» — `chalice-*`,
зацепок — `seed-*`; картинки карт — `app/maps/deadlight-*.jpg`.

## Общие страницы

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, аннотация «two unsettling encounters on the road» | физ. 1, 90 | `scenario/deadlight` (sources); `scenario/chalice` (summary) |
| Титул, Credits (авторы, Clear Credit) | физ. 2–3 | `scenario/deadlight`, `scenario/chalice` (summary, sources) |
| Table of Contents; Investigator Download | физ. 4 | все записи; готовые сыщики — `mertvennyy-svet-ru/character/*` (refs сценариев) |

## Dead Light («Мертвенный свет»)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Dead Light — Surviving One Night Outside of Arkham; Introduction | 5 | `scenario/deadlight` (name, aliases, summary, advice) |
| Keeper’s Information: Events So Far | 5–7 | `scenario/deadlight` (keeper_info); `character/deadlight-godfrey-webb`, `-emilia-webb`, `-mary-laker`, `-clem-tailor`, `-billy-esterhouse`, `-sam-keelham`, `-jake-burns` |
| Врезка Location, Time, and Place | 7 | `location/deadlight-orchard-run`; `scenario/deadlight` (advice, hook) |
| An Alternative Option | 7 | `scenario/deadlight` (hook); `character/deadlight-godfrey-webb` |
| Dramatis Personae: Emilia Webb, Sam Keelham, Jake Burns, Mary Laker, Winifred and Teddy Brewer, Billy Esterhouse, The Dead Light | 8–11 | `character/deadlight-*` (background, legend); `creature/deadlight-dead-light` |
| Start: The Encounter on the Road (текст для чтения вслух, варианты действий) | 12, 14 | `scene/deadlight-encounter-on-the-road`; `location/deadlight-near-miss` |
| Orchard Run Environs Map | 13 (= 64) | `map/deadlight-orchard-run` (10 меток) → `app/maps/deadlight-orchard-run.jpg` |
| Врезка The Antique Chain and Coin-like Medal | 14 | `item/deadlight-antique-chain` |
| What Happens Next? | 14 | `scene/deadlight-traveling-with-emilia` |
| What Emilia Knows | 14 | `character/deadlight-emilia-webb` (legend); `scene/deadlight-traveling-with-emilia` |
| Orchard Run Gas Station and Café Map | 15 (= 65) | `map/deadlight-gas-station` (17 меток) → `app/maps/deadlight-gas-station.jpg` |
| Traveling with Emilia | 16 | `scene/deadlight-traveling-with-emilia` |
| Orchard Run Gas Station and Café | 16 | `location/deadlight-gas-station`, `-gas-station-office`, `-parking-garage`, `-gas-pump`, `-abandoned-truck`; `scene/deadlight-gas-station-arrival`; `character/deadlight-doreen-atler` |
| Inside the Café | 16 | `location/deadlight-cafe`; `scene/deadlight-gas-station-arrival` |
| Orchard Wood | 16 | `location/deadlight-orchard-wood`; `scene/deadlight-orchard-wood` |
| Getting Out by Road or on Foot | 17 | `scene/deadlight-getting-out` |
| Greenapple Acre Cottage | 17–18 | `location/deadlight-greenapple-cottage`, `-cottage-barn`; `scene/deadlight-greenapple-cottage`; `item/deadlight-robbers-gear` (лом) |
| Greenapple Acre Cottage Map | 19 (= 66) | `map/deadlight-greenapple-cottage` (16 меток) → `app/maps/deadlight-greenapple-cottage.jpg` |
| The Reception Room | 18, 20 | `location/deadlight-reception-room`; `item/deadlight-coffer`, `-bureau-key`, `-clems-wallet`, `-robbers-gear`; `character/deadlight-clem-tailor` |
| Emilia Webb’s Bedroom and Study | 20 | `location/deadlight-emilias-room` |
| The Doctor’s Study | 20–21 | `location/deadlight-doctors-study`; `item/deadlight-bureau`, `-wax-ointment` |
| Врезка Dr. Webb’s Journal; профиль книги | 21 | `tome/deadlight-dr-webbs-journal` |
| Dr. Webb’s Bedroom | 22 | `location/deadlight-doctors-bedroom`; `item/deadlight-pocket-bible` |
| The Cellar | 22 | `location/deadlight-cellar`; `item/deadlight-generator` |
| Driving the Action Forward and Maintaining Suspense | 22 | `scene/deadlight-hunt`; `scenario/deadlight` (advice) |
| Slow the Pace for Investigation | 22–23 | `scenario/deadlight` (advice) |
| Foreshadow the Monster; The Grand Entrance; The Weak Fall By The Wayside | 23 | `scene/deadlight-hunt`; `creature/deadlight-dead-light` (encounters) |
| Tear Down The Walls; Present Them With Hope, Then Snatch It Away; Make Them Choose And Make Them Act | 23–24 | `scene/deadlight-hunt` |
| Reaching a Conclusion | 24–25 | `scene/deadlight-dawn`; `scenario/deadlight` (conclusion) |
| Characters & Monsters: Emilia Webb, Sam Keelham, Jake Burns, Mary Laker, Teddy Brewer, Winifred Brewer, Billy Esterhouse | 25–26 | статблоки `character/deadlight-*` |
| The Dead Light, hideous devourer; What It Wants; What It Will Do; How Can It Be Harmed?; How Can It Be Stopped? | 27 | `creature/deadlight-dead-light`; `scene/deadlight-stopping` |
| Containing The Dead Light | 28 | `scene/deadlight-containing`; `creature/deadlight-dead-light` (legend) |
| Характеристики, Combat (Tendril Lash, Consume, Mesmeric Effect), Armor, Vulnerabilities, Other, Sanity Loss | 28–29 | `creature/deadlight-dead-light` (statblock, abilities) |
| Handout: Dead 1a, 1b, 1c, 1d | 20–23 (= 67–70) | `handout/deadlight-dead-1a`, `-1b`, `-1c`, `-1d` (текст с изображений) |
| Handout: Dead 2 | 24 (= 71) | `handout/deadlight-dead-2` |

## Saturnine Chalice («Сатурнова чаша»)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Saturnine Chalice — Where Angels Fear to Tread; Introduction | 31 | `scenario/chalice` (name, aliases, summary) |
| Keeper’s Information: Events So Far | 31–34 | `scenario/chalice` (keeper_info); `character/chalice-augustus-weyland`, `-veronica-weyland` |
| Врезка The Book of Abramelin | 32 | `tome/chalice-book-of-abramelin-mathers` |
| The Operation | 33 | `character/chalice-augustus-weyland`, `-lester-goodman`; `scenario/chalice` |
| Врезка Beacon of Chaos | 33 | `item/chalice-beacon-of-chaos` |
| Veronica Returns | 33–34 | `character/chalice-veronica-weyland`; `creature/chalice-shapeless-one` (legend) |
| Врезка Handling Puzzles | 34 | `scenario/chalice` (advice) |
| Врезка Recommended Reading and Viewing | 34–35 | `scenario/chalice` (advice); `tome/chalice-book-of-abramelin-mathers` |
| Врезка Time and Setting | 34 | `scenario/chalice` (keeper_info); `location/chalice-weyland-estate`; `item/chalice-tear-off-calendar` |
| Dramatis Personae: Augustus, Veronica, Jeremiah, Rosemary, Evangeline, Lester Goodman, The Shapeless One | 35–37 | `character/chalice-*`; `creature/chalice-shapeless-one` |
| Start: Out of Gas; врезка Alternative Beginnings | 38 | `scene/chalice-out-of-gas` |
| Outside the House; Garden | 39 | `location/chalice-garden`, `-ash-pit`, `-driveway` |
| Garage | 39 | `location/chalice-garage`; `item/chalice-gasoline-can` |
| Weyland Estate Map | 39 (= 72) | `map/chalice-weyland-estate` (9 меток) → `app/maps/deadlight-chalice-weyland-estate.jpg` |
| Well; Mausoleum | 40 | `location/chalice-well`, `-mausoleum` |
| Exterior of the House | 40 | `location/chalice-weyland-house` |
| First Floor and Basement: Hall; Lounge | 40–42 | `location/chalice-hall`, `-lounge`; `item/chalice-ward-bust` |
| Library | 42–44 | `location/chalice-library`; `item/chalice-ward-eagle-lectern` |
| Weyland House Map | 43 (= 73) | `map/chalice-weyland-house` (28 меток, одна невычерченная — комната слуг) → `app/maps/deadlight-chalice-weyland-house.jpg` |
| Dining Room | 44 | `location/chalice-dining-room`; `item/chalice-ward-ox` |
| Quick Reference: The Ward Items and Sigils (+ continued: камеа, таблица букв) | 44–45 | `scenario/chalice` (таблицы «Предметы оберега и сигилы», «Камеа Сатурна и шифр букв»); `item/chalice-ward-*` |
| Kitchen, Storeroom, Pantry | 46 | `location/chalice-kitchen`; `item/chalice-kerosene` |
| Store/Access Room | 46 | `location/chalice-store-access-room` |
| Servants’ Room and Bathroom | 46–47 | `location/chalice-servants-room`; `item/chalice-ward-lion` |
| Laundry Room | 47 | `location/chalice-laundry-room` |
| Main Basement | 47 | `location/chalice-basement` |
| Second Floor and Cupola: Landing | 47 | `location/chalice-landing` |
| Bedroom (список дат календаря) | 48 | `location/chalice-bedroom`; `item/chalice-tear-off-calendar`; `scenario/chalice` (таблица «Дата на календаре») |
| Chamber | 49–50 | `location/chalice-chamber` |
| Врезка Books on the Desk (One–Seven) | 49 | `item/chalice-holy-books`, `-augustus-journal`, `-veronica-journal`; `tome/chalice-book-of-abramelin-mathers`, `-das-buch-abramelin` |
| Oratory | 50–51 | `location/chalice-oratory`; `item/chalice-beacon-of-chaos`, `-wand` |
| Bathroom and Cupola | 51 | `location/chalice-bathroom-cupola` |
| Scenes | 51 | `scenario/chalice` (advice, steps) |
| Introductions | 52 | `scene/chalice-introductions` |
| Drinks | 52–53 | `scene/chalice-drinks` |
| Врезка Fallibility | 52 | `creature/chalice-shapeless-one` (legend); `scenario/chalice` (keeper_info) |
| Telephone | 53 | `scene/chalice-telephone` |
| Asking for Gasoline | 53 | `scene/chalice-asking-for-gasoline` |
| Evangeline Outside | 53 | `scene/chalice-evangeline-outside` |
| Conversations | 53 | `scene/chalice-conversations` |
| Exploring Upstairs | 54 | `scene/chalice-exploring-upstairs` |
| Darkness Falls | 54 | `scene/chalice-darkness-falls` |
| Evangeline Inside | 54 | `scene/chalice-evangeline-inside` |
| The Lynwood Bodies | 54 | `scene/chalice-lynwood-bodies` |
| The Dinner Party | 54 | `scene/chalice-dinner-party` |
| Attempting to Leave | 54–55 | `scene/chalice-attempting-to-leave` |
| Questions and Deaths | 55 | `scene/chalice-questions-and-deaths` |
| Realization | 55 | `scene/chalice-realization`; `tome/chalice-lesser-key-of-solomon` |
| Banishing the Demon | 56 | `scene/chalice-banishing-the-demon` |
| Conclusion; Freeing the Trapped Souls | 56 | `scene/chalice-freeing-the-trapped-souls`; `scenario/chalice` (conclusion) |
| Confronting the Shapeless One | 56–57 | `scene/chalice-confronting-the-shapeless-one` |
| Continuation; Rewards | 57 | `scenario/chalice` (conclusion) |
| Characters and Monsters: Character Profiles and Reactions | 57 | `scenario/chalice` (keeper_info); `scene/chalice-questions-and-deaths`; `scene/chalice-conversations` |
| Evangeline Weyland (демоническая форма) | 57 | `character/chalice-evangeline-weyland` (abilities) |
| Shapeless Ones; The Shapeless One’s Tactics; Cover Story; Special Powers | 58–59 | `creature/chalice-shapeless-one` |
| Характеристики Shapeless Ones, Combat, Steal Memories, Inflict Madness, Armor, Spells, Sanity Loss | 59 | `creature/chalice-shapeless-one` (statblock, abilities) |
| Handout: Saturnine 1a/1b, 2a/2b, 3a/3b, 4a/4b | 42–48 (= 74–77) | `handout/chalice-handout-1` … `-4` (описание рисунков и листов-головоломок) |
| Handout: Saturnine 5, 6 | 50–51 (= 78–79) | `handout/chalice-handout-5`, `-6` (текст снят с изображений повёрнутых страниц) |
| Handout: Saturnine 7 | 52 (= 80) | `handout/chalice-handout-7` (Бытие 3:22–24; русский — Синодальный перевод) |
| Handout: Saturnine 8 | 55 (= 81) | `handout/chalice-handout-8` (рисунок — описание) |

## Appendix: Scenario Seeds (зацепки)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Вступление приложения | 60 | `scenario/seed-*` (summary) |
| Neutral Ground (Background, Set Up, What’s Going On?, Mundane Option, Mythos Option) | 60–61 | `scenario/seed-neutral-ground`; `character/seed-tullys-clerk` |
| The Big Blue Buopoth (Background, Set Up, What’s Going On?) | 61 | `scenario/seed-big-blue-buopoth`; `character/seed-professor-malcolm` |
| The Suitcase (Set Up, What’s in the Case?, Returning the Case) | 61–62 | `scenario/seed-suitcase`; `character/seed-old-lady` |
| The Neverending Road (Set Up, What’s Going On?) | 62 | `scenario/seed-neverending-road` |
| The Diversion (Set Up, What’s Going On?) | 63 | `scenario/seed-diversion` |
| The Hitchhikers (Set Up, What’s Going On?) | 63 | `scenario/seed-hitchhikers`; `character/seed-hitchhikers` |

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Collected Maps and Handouts — повторы карт и раздаток | 64–81 | те же карты и раздатки, что в тексте; взяты как источник изображений (`sources` карт и раздаток) |
| Index | 82–84 | указатель; в нём опечатка — «Handout: Dead 1a» трижды вместо 1b–1d (не важно для игры) |
| Author Biographies (Alan Bligh, Matthew Sanderson, Lynne Hardy, Mike Mason) | 85–86 | не игровой материал |
| Реклама «Gateways to Terror» и «Malleus Monstrorum» | 87–88 | реклама |
| Подписи к иллюстрациям («Opposite: The Dead Light», «The generator in the cellar» и т. п.), пустые страницы 4 и 30, иллюстрация экстерьера (41) | разн. | без текста; картинки в `app/art` не заносились (часть `app/art` не моя) |
| Картинки раздаток (рисунки предметов оберега, сигилы, гравюра треугольника) | 74–81 | картинки в `app/art` — не моя часть; в записях раздаток — описание и текст |
| Места зацепок (кемпинг Талли, буопот, свалка) | 60–63 | книга не даёт мест с данными — остаются текстом в записях зацепок |
| Статблоки Уэйлендов и Линвудов | 57 | в книге их нет (видения, используют значения сыщиков) — записано в `quality.notes` |

## Опечатки и сомнения

- `creature/deadlight-dead-light`: БкУ +1d6 и Комплекция 2 при СИЛ+ТЕЛ 160 (+1d4, 1) — как напечатано (`errata`, Р-36: большинства нет).
- `character/deadlight-winifred-brewer`: Уклонение 25% (22/9) — доли исправлены на (12/5) (Р-77, возможно задумано 45%); Скорость 4 при ожидаемой 5 — как напечатано.
- `creature/chalice-shapeless-one`: ПЗ = ПМ = 50 при МОЩ 200 (ожидается 40) — как напечатано; «Насланное безумие» 100% (50/10) — пятая доля исправлена на 20.
- `character/deadlight-mary-laker`: все характеристики и производные совпадают с Эмилией — возможно, повтор вёрстки (`quality.notes`).
- `item/deadlight-robbers-gear`: оружие Клема — «sawn-off shotgun» (с. 7) и «single-barreled 20-gauge shotgun» (с. 20).
- Сводная «Kamea of the (wherein …)» (с. 45) — пропущено слово «Saturn»; не важно для игры.

## Новые записи-кандидаты и вопросы

- Заклинание «Призыв пожирателя грехов» (Recall Sin-Eater) из дневника Уэбба — набросок в отчёте помощника; `kb/spells` общий.
- Бесформенные (Shapeless Ones) — профиль вида только в этой книге (`creature/chalice-shapeless-one`); кандидат в общий `coc:creature:`.
- Буопот и зуги (зацепка «Большой синий буопот») — в справочнике существ нет, остались текстом.
- Болтон (Bolton, Массачусетс) — упоминается (дом и практика Уэбба, власти), но действие там не идёт; записи нет.
- Зарегистрировать фанатский перевод `[RU-фан 7e] myortvy_svet_for_call_of_cthulhu_rpg.pdf` в `books.json` (trusted) и записать `offset` −1 для `dead-light-en`.
