# Convicts & Cthulhu — основная книга (часть core)

Книга `convicts-cthulhu-en` (Cthulhu Reborn, 2016; 98 с.) и `convicts-cthulhu-players-en` (Players Version, 57 с. —
постраничная копия с. 1–56 основной книги без частей IV–VI; сравнение текстового слоя по страницам — совпадает слово в
слово, кроме оглавления). Записей в `kb/books/convicts-cthulhu-en/`: 245 — правил 50, персонажей 83, мест 67, сценариев 7
(вводный сценарий и 6 набросков), сцен 11, предметов 9, организаций 7, карт 4, раздаток 4, существ 3. Записей только из
Players Version нет: всё в ней есть в основной книге, её страницы стоят в `sources` записей основной книги (для всех
записей с физ. с. 5–57 — проверено скриптом).

## Страницы (для `pipeline/source/books.json`, ставит ведущий)

- `convicts-cthulhu-en`: физическая = печатная + 1 (печатная «3» на физ. 4, «13» на физ. 14) — **offset −1**; физ. 1 —
  обложка, физ. 98 — задняя обложка (без номера).
- `convicts-cthulhu-players-en`: то же — **offset −1** (страницы совпадают с основной книгой физ. 1–57).
- Пока смещение не записано, `tools/completeness.py` читает «с. N» в `images[].source` как физическую страницу и считает
  часть картинок непокрытыми (портрет Блая и т. п.) — после записи смещения находки уйдут.

## Заголовок книги → запись

Страницы — печатные. Префикс id `convicts-cthulhu-en/` опущен.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Ballad of Jim Jones at Botany Bay | 1 | не взято (см. ниже) |
| Clear Credit; Table of Contents; Authors' Notes | 2–4 | не взято (см. ниже) |
| Introduction | 5–6 | `rule/introduction` (+ карта Австралии 1803 — картинка) |
| Part I: The Historical Setting | 7 | `rule/part-i-the-historical-setting` |
| Early Days of Settlement | 8 | `rule/early-days-of-settlement` |
| Darker Days | 8–9 | `rule/darker-days` |
| Impact on Indigenous Australians | 9 | `rule/impact-on-indigenous-australians` |
| The Rum Economy | 9, 11 | `rule/the-rum-economy` |
| Timeline of Early Colonial New South Wales | 10 | `rule/timeline-of-early-colonial-new-south-wales` (таблица) |
| Врезки-биографии губернаторов и офицеров (Phillip, Grose, Paterson, Hunter, King, Bligh, Macquarie, Johnston, Macarthur) | 9–13 | `character/arthur-phillip`, `francis-grose`, `william-paterson`, `john-hunter`, `philip-gidley-king`, `william-bligh`, `lachlan-macquarie`, `george-johnston`, `john-macarthur` |
| Being Bligh | 12 | `character/william-bligh` (советы Хранителю) |
| The Rum Rebellion | 11 | `rule/the-rum-rebellion` |
| Sub-eras of Convicts & Cthulhu | 11 | `rule/sub-eras-of-convicts-and-cthulhu` |
| Life During the Rum Trade / Life Under Bligh / The Time of Military Rule | 11–14 | `rule/life-during-the-rum-trade`, `rule/life-under-bligh`, `rule/the-time-of-military-rule` |
| Principal Settlements | 14 | `rule/principal-settlements` |
| Communication with the 'Civilised World' | 14 | `rule/communication-with-the-civilised-world`; `character/isaac-nichols` |
| Part II: Investigations in the Colony; Creating Investigators | 15 | `rule/creating-investigators` |
| Indigenous Investigators | 15–16 | `rule/indigenous-investigators` |
| Convict Classes | 16, 18 | `rule/convict-classes` |
| Map of New South Wales | 17 | `map/new-south-wales-1802` (картинка `app/maps/convicts-core-new-south-wales-1802.jpg`); места карты — `location/*` с `part_of` `location/new-south-wales` |
| Freemen Social Classes & Outlooks | 18 | `rule/freemen-social-classes-and-outlooks` |
| Investigator Backgrounds | 18–19, 21 | `rule/investigator-backgrounds` (+ карта «Aboriginal Clans of the Sydney Region» — картинка) |
| Government Officials (врезка) | 19 | `rule/government-officials` |
| Skills | 19–20 | `rule/skills` (список навыков и базы — таблица) |
| The Importance of Credit Rating | 21 | `rule/the-importance-of-credit-rating` |
| Literacy | 21 | `rule/literacy` |
| Effects of Drunkenness (из Pulp Cthulhu) | 21 | `rule/effects-of-drunkenness` (таблица) |
| Character Templates: Indigenous / Convict / Freeman Occupations | 21–23 | `rule/character-templates`; 14 профессий — черновики `checks/20261124-convicts/new-shared/occupations/convicts-*.json` (см. ниже) |
| Life As A Convict | 23 | `rule/life-as-a-convict` |
| A Day in the Life | 23 | `rule/a-day-in-the-life` |
| Convict Punishments | 23–24 | `rule/convict-punishments` |
| Gear & Equipment | 24–26 | `rule/gear-and-equipment` |
| The Flash Language: Convict Slang | 25 | `rule/the-flash-language` (словарь — таблица) |
| Pay and Victuals | 26 | `rule/pay-and-victuals` |
| An English Diet | 26–27 | `rule/an-english-diet` (цены — таблица) |
| A Note About Currency and Trade | 27–28 | `rule/a-note-about-currency-and-trade` |
| A Variety of Coins | 27 | `rule/a-variety-of-coins` |
| Local Industries | 28 | `rule/local-industries` |
| Personal Possessions | 28–29 | `rule/personal-possessions` |
| Entertainments | 29 | `rule/entertainments` |
| Requisitioning From the Commissariat | 29–30 | `rule/requisitioning-from-the-commissariat` |
| Better Living Through Stealing | 30 | `rule/better-living-through-stealing` |
| Common Weapons: Colonial Firearms; Aboriginal Weapons (из Secrets of Australia) | 30–32 | `rule/common-weapons` (обе таблицы); предложения к `coc:weapon:*` — `proposals-core.json` |
| Investigating in the Colony | 32, 90 | `rule/investigating-in-the-colony` (+ репродукция «Sydney Gazette», 1807 — картинка) |
| Part III: Desperate People, Desolate Places; A Brief Tour of Hell | 33, 35 | `rule/a-brief-tour-of-hell` |
| Scurrilous Events & Curiosities | 34 | `rule/scurrilous-events-and-curiosities` (таблица) |
| How many people are in the Colony? | 35 | `rule/how-many-people-are-in-the-colony` |
| Places in Sydney | 35 | `coc:location:sydney` — источник и ссылка на карту через `proposals-core.json`; `location/new-south-wales` |
| 1. Government House | 35–36 | `location/government-house` (+ картинка) |
| 2. Sydney Gaol | 36–37 | `location/sydney-gaol` |
| Map of Sydney Township | 37 | `map/sydney-township-1807` |
| 3. Government Commissariat | 37–38 | `location/government-commissariat`; `character/john-palmer` |
| 4. Chaplains' Office | 38 | `location/chaplains-office`; `character/samuel-marsden` |
| 5. Magistrates' Office | 38–39 | `location/magistrates-office`; `character/richard-atkins`, `george-crossley`, `andrew-thompson` |
| Depicting the Colony (врезка) | 39 | `rule/depicting-the-colony` |
| 6. NSW Corps Barracks & Parade | 39–40 | `location/nsw-corps-barracks-and-parade`; `organization/nsw-corps` |
| 7. St Phillip's Church | 40 | `location/st-phillips-church` (+ гравюра) |
| 8. Female Orphan School | 40 | `location/female-orphan-school` (+ картинка из ToL #9); `character/elizabeth-more-hume` |
| 9. Paymaster's General Store | 41 | `location/paymasters-general-store`; `character/anthony-fenn-kemp` |
| 10. The Tanks and the Tank Stream | 41 | `location/the-tanks-and-the-tank-stream`; `location/simeon-lords-home-and-warehouse`; `character/simeon-lord` |
| 11. Sydney Cove Wharfs & Warehouses | 41–42 | `location/sydney-cove-wharfs-and-warehouses`, `location/government-wharf`; `character/james-underwood`, `henry-kable` |
| 12. The Rocks | 42 | `location/the-rocks`; `character/mary-wade`, `thomas-moore` |
| 13. Dawes Point (Fort Phillip, Sydney Hospital, Observatory, Battery & Powder Magazine, Campbell's Wharf) | 42–43 | `location/dawes-point`, `fort-phillip`, `sydney-hospital`, `sydney-observatory`, `dawes-battery-and-powder-magazine`, `robert-campbells-warehouse-and-wharf` (+ гравюра); `character/thomas-jamison`, `john-harris` (+ портрет из ToL #10), `robert-campbell` |
| 14. An Example Warehouse: Jeremiah Stone's | 43 | `location/jeremiah-stones-warehouse`; `character/jeremiah-stone` |
| 15. An Example Public House: The Black Swan | 43–44 | `location/the-black-swan`; `character/james-squire` |
| 16. Aboriginal Settlements in and around Sydney Town | 44 | `location/aboriginal-settlements-around-sydney`; `character/bungaree`, `bennelong` |
| Places in Parramatta; Parramatta Township | 44–46 | `location/parramatta`; `character/darcy-wentworth` |
| Map of Parramatta Township | 46 | `map/parramatta-township-1804` |
| Parramatta: Hospital; Barracks; Church; Wharf & Commissariat; Rowland Hassall's Store | 45–47 | `location/parramatta-hospital`, `parramatta-barracks`, `parramatta-church`, `parramatta-commissariat`, `rowland-hassalls-store`; `character/rowland-hassall`, `george-mealmaker` |
| Prison at Hanging Green | 46–47 | `location/prison-at-hanging-green`; `character/francis-oakes`, `sgt-dogwood` |
| Freemason's Arms, Public House | 46–47 | `location/freemasons-arms`; `character/james-larra`, `molly-rowson`, `phillip-cunningham` |
| Elizabeth Farm (Macarthur's Landholding) | 48 | `location/elizabeth-farm`; `character/elizabeth-macarthur` |
| Vinegar Hill (aka Castle Hill) | 48–49 | `location/vinegar-hill`; `character/baron-verincourt-de-clambe` |
| 6. A Sample Small Farmstead: The Cushing Farm | 49 | `location/cushing-farm`; `character/julius-cushing`, `caroline-cushing`, `jenny-milgrim`, `dunkle`, `smogg` |
| 7. A Sample Larger Farmstead: The Verrier Farm | 49–50 | `location/verrier-farm`; `character/william-verrier` |
| Aboriginal Settlements near Parramatta | 50 | `location/aboriginal-settlements-near-parramatta`; `character/pemulwuy`, `tedbury` |
| The Coal River Settlement | 51 | `location/coal-river` |
| Coal River: Wharves and Beach; Convict Camp; Barracks | 51–52 | `location/coal-river-wharves-and-beach`, `coal-river-convict-camp`, `coal-river-barracks`; `character/charles-throsby`, `owen-mcdermot`, `edward-nail` |
| Aboriginal Settlements near Coal River | 53 | `location/aboriginal-settlements-near-coal-river` |
| Other Settled Places: East of Sydney / South of Sydney / North of the Harbour / West of Parramatta / Broken Bay / Hawkesbury | 53–54 | `location/new-south-wales` (вводный текст); `woolloomooloo`, `south-head`, `botany-bay`, `point-solander`, `cooks-river`, `cape-banks`, `georges-river`, `lane-cove`, `hunters-hill`, `field-of-mars`, `kissing-point`, `broken-bay`, `toongabbie`, `prospect-hill`, `hawkesbury-river`, `richmond-hill`, `blue-mountains` |
| Further Afield | 54–55 | `rule/further-afield` |
| Van Diemen's Land | 54–55 | `location/van-diemens-land`, `location/hobart-town`, `location/port-dalrymple` |
| Norfolk Island; Map of Norfolk Island, 1788 | 55–56 | `location/norfolk-island` (карта 1788 — картинка записи: на ней нет номеров и меток мест) |
| Other Places Explored | 55 | `rule/further-afield` |
| Part IV: Dark Southern Land; Cults in the Colony | 57–58 | `rule/part-iv-dark-southern-land` |
| Культы: The Effigy of Scars and Suffering; The Industrious Brothers of the New World; The Outcast Dreamers; The Sharks-Tooth Cult; The Bacchanal Club | 58–59 | `organization/effigy-of-scars-and-suffering`, `industrious-brothers-of-the-new-world`, `outcast-dreamers`, `sharks-tooth-cult`, `bacchanal-club`; `item/effigy-of-scars`, `item/sharks-tooth`; `character/chandler-meriwether`, `ella-carmody`, `thomas-nightmonger`, `charles-morrison`, `old-barney` |
| Indigenous Horrors | 60–61 | `rule/indigenous-horrors`; `creature/yowie`; `item/pituri` |
| New Nightmares | 61–62 | `rule/new-nightmares` |
| Part V: Mythos Tales; Introductory Scenario: Un-Fresh Off The Boat; Keeper's Background | 63–64 | `scenario/un-fresh-off-the-boat`; `organization/heralds-of-the-silver-dawn`; `location/emily`, `location/lulworth-cove` |
| Involving the Investigators; Handouts 1–2 | 65–66 | `scene/involving-the-investigators`; `handout/handout-1-the-voyage-out-convict`, `handout-2-the-voyage-out-free-settler` |
| The Rumour Mill | 67 | `scene/the-rumour-mill` |
| The Colonial Secretary | 67–68 | `scene/the-colonial-secretary`; `character/edmund-griffin`, `corporal-waterstone`, `nancy-pike` |
| On the Trail of a Blind Man; Word on the Street | 68–69 | `scene/word-on-the-street`; `character/jack-tapper` |
| The Cruel Hand of Mercy | 69–70 | `scene/the-cruel-hand-of-mercy`; `character/melford`, `sergeant-freeley` |
| What the Parson Knows | 70 | `scene/what-the-parson-knows`; `handout/letter-to-reverend-fredericks` |
| Soldiers of Low Repute | 70–71 | `scene/soldiers-of-low-repute`; `character/rupert-rowsthorn` |
| The Powder Magazine; Map of Dawes Point Battery | 71–72 | `scene/the-powder-magazine`; `map/gun-battery-on-dawes-point`; `location/powder-magazine-hidden-room`; `handout/heralds-membership-certificate`; `item/heralds-ring` |
| Death of a Chaplain; Rise of the Watcher Spawn | 72–73 | `scene/death-of-a-chaplain`, `scene/rise-of-the-watcher-spawn`; `character/elijah-fredericks`; `creature/watcher-spawn` |
| Scorched Earth | 73–74 | `scene/scorched-earth` |
| Rewards and Loose Ends | 74 | `scenario/un-fresh-off-the-boat` (`conclusion`) |
| Statistics | 74–75 | `creature/watcher-spawn` (стадии — `variants`); статблоки персонажей сценария |
| Story Seeds; Seed 1: The Ghosts of Vinegar Hill | 76–78 | `scenario/seed-1-the-ghosts-of-vinegar-hill`; `item/cunninghams-silver-coins` |
| Seed 2: The Lights of Botany Bay | 78–82 | `scenario/seed-2-the-lights-of-botany-bay`; `character/solander`, `joseph-banks`, `lt-paulson`, `john-montagu`; `item/banks-botany-bay-notes`, `paulson-sandwich-papers` |
| Seed 3: Ghosts of the North | 82–84 | `scenario/seed-3-ghosts-of-the-north`; `character/rudi-gorelov`, `solonik`, `sarah-molloy` |
| Seed 4: The Baleful Flood | 84–86 | `scenario/seed-4-the-baleful-flood`; `location/hawkesbury-caves`; `character/uriah-waterford`; `item/essential-saltes` |
| Seed 5: The Hinterland Monster | 86–87 | `scenario/seed-5-the-hinterland-monster`; `creature/yowie` (+ иллюстрация с. 87) |
| Seed 6: Dream Sequence | 86–89 | `scenario/seed-6-dream-sequence`; `character/edward-sloane`; `creature/dream-shambler`; `item/yithian-weapon` |
| Part VI: Resources; A Short Bibliography (TV and Film, Convict Fiction, Historical Books, Websites) | 90–92 | `rule/a-short-bibliography` |
| Representative Statistics | 92–94 | `character/typical-convict`, `typical-convict-overseer`, `typical-free-settler`, `typical-nsw-corps-officer`, `typical-nsw-corps-soldier`, `typical-aboriginal-man`, `typical-government-officer`, `typical-surgeon`, `typical-merchant` |
| Character Sheet | 95–96 | не взято (бланк) |

Сценарии-наброски (Story Seeds) — короткие идеи без сцен и статблоков: каждая — запись `scenario` с ходом
расследования в `steps` и тремя вариантами разгадки в `keeper_info`; `tools/scenario_check.py` отмечает у них «нет
сцен» (6 находок) — сознательно, у книги сцен там нет.

## Профессии (черновики общих записей)

`checks/20261124-convicts/new-shared/occupations/` — 14 черновиков `coc:occupation:convicts-<slug>` по с. 21–23:
hunter-gatherer, clever-man-or-woman, career-criminal, domestic-servant, down-on-luck-craftsman, fallen-clergyman,
political-agitator, labourer, doctor, farmer-settler, lawyer, merchant, nsw-corps-officer, publican. Все 14 id совпадают
с черновиками части tol-b (`new-shared-tol-b.json`, Ticket of Leave #5 — расширенная редакция тех же профессий);
названия приведены к форме tol-b, специализации — с прописной, как в `kb/occupations`. Проверка схемой и правилами
записи — 0 замечаний. При переносе ведущему (одна запись на id, не две):

- первый источник — основная книга (с. 21–23) и Players Version, затем ToL #5 (источники tol-b);
- описание — из черновика tol-b (в основной книге описаний нет);
- списки навыков ToL #5 расходятся с основной книгой: Doctor — + Чтение и письмо (английский); Fallen Clergyman —
  Слух → Чтение и письмо (английский); Lawyer — Родной язык → Чтение и письмо (английский); Merchant — у tol-b без
  ссылки на Ловкость рук; Clever-Man / Hunter-Gatherer — у ToL #5 Средства «в европейской колонии 0–5». Это поздняя
  редакция книги-источника: в `quality.notes`/`source_variants`, основной список — по основной книге (решение ведущего);
- tol-b пишет «Актёрское мастерство», `kb/occupations` — «Актёрская игра» (так в core).

Навыки: «Религия» — `coc:skill:kc-religion` (база в книге 20%). Alcheringa Dream Lore и Dream Song книга только называет
(«см. Secrets of Australia»), механики нет — записей не заводили (Р-126), в профессиях они текстом; кандидаты в общий
справочник, когда в базе будет Secrets of Australia.

## Картинки

- `art-core.json` (прежний помощник, применено): Блай, Макартур, Фредерикс, Отродья Стража, раздатки 1–2, Дом правительства,
  карта Норфолка, карта Австралии, карта кланов.
- `art2-core.json` → `art2-core-proposals.json` (применено): Йови (с. 87), церковь Святого Филиппа (с. 40), склад
  Кэмпбелла (с. 43), «Sydney Gazette» 1807 к правилу «Расследования в колонии» (с. 90); по просьбе части tol-c
  (`art-core-targets-tol-c.json`) — портрет Джона Харриса (ToL #10, с. 4) и здание Школы для девочек-сирот (ToL #9,
  с. 5), файлы `convicts-core-john-harris`, `convicts-core-female-orphan-school`.
- Карты — 4 записи `map` с картинками `app/maps/convicts-core-*.jpg`.
- `atmosphere-core.json` (сливает ведущий): 31 страница основной книги (обложки, заставки частей, гравюры без подписи,
  рамки врезок, лист сыщика) и 23 страницы Players Version (уменьшенные копии тех же картинок). После картинок записей
  непокрытых картинок основной книги нет (подсчёт по `images.list` с тем же фильтром, что у `completeness.py`, при
  смещении −1).

## Не взято

- с. 1 «The Ballad of Jim Jones at Botany Bay» — народная песня-эпиграф (около 1830 г.), художественный текст без
  данных для игры.
- с. 2 «Clear Credit», с. 3 оглавление, с. 4 «Authors' Notes» — выходные данные, авторы, история книги (сказано в покрытии;
  по правилу книги правил вступление и история книги не переносятся).
- с. 95–96 «Character Sheet» — бланк листа сыщика (список навыков с базами есть в `rule/skills`).
- Задняя обложка (физ. 98) — аннотация книги.
- Гравюры без подписи и заставки — в `atmosphere-core.json`, не в записях.

## Опечатки и сомнения книги (в `errata` записей)

- `rule/a-note-about-currency-and-trade`: «each pound being worth 12 shillings or 240 pence» (с. 27) — в фунте 20 шиллингов;
  исправлено в записи (`fixed: true`).
- Доли процентов в статблоках «Representative Statistics» (с. 93–94): «45% (22/7)» у Уклонения/Драки нескольких типажей,
  «75% (15/6)» у Кнута надсмотрщика — доли исправлены (Р-35, Р-77); у Отродья Стража «Dodge 40% (22/7)» → (20/8).
- `typical-government-officer`: ПМ 11 при МОЩ 50; `typical-merchant`, `typical-surgeon`: Скорость 9 при СИЛ/ЛВК не выше
  ТЕЛ — как напечатано.
- `watcher-spawn`: Paralyse 55/50/45% убывает с ростом стадии — как напечатано.
- `rule/darker-days`: Филлип уезжает в 1795 году (с. 9), в хронике — 1792 (с. 10).
- `rule/timeline-of-early-colonial-new-south-wales`: даты основания Коул-Ривер (1801/1803/1804) и Земли Ван-Димена (1803/1804)
  расходятся по книге.
- `location/coal-river`: 40 миль на карте (с. 17) и 160 км в тексте (с. 51).
- `location/botany-bay`: вождём кемейгал назван Беннелонг (с. 53), хотя на с. 45 он из вангал.
- `character/baron-verincourt-de-clambe`: Verincourt / Verrincourt.
- `rule/scurrilous-events-and-curiosities`: две записи 1799 года не по порядку.
- Без `errata` (историческая неточность, не механика, Р-39): «Lt Governor Arthur» на Земле Ван-Димена в 1806 году
  (с. 54; исторически Коллинз, Артур — с 1824 года); «Arthur Philips» (с. 9) — опечатка имени.

## Предложения к общим записям

`checks/20261124-convicts/proposals-core.json` — 9 правок 5 записей: `coc:weapon:flintlock` (источник, псевдоним, эпоха),
`coc:weapon:brown-bess-musket`, `coc:weapon:war-boomerang`, `coc:weapon:spear-thrown` (`source_variants` таблиц с. 30–31),
`coc:location:sydney` (источник «Places in Sydney», эпоха, ссылка на карту 1807 года). Пробный прогон `apply.py` — 9 правок,
ошибок нет.

## Ссылки частей ToL на основную книгу

Все ссылки `convicts-cthulhu-en/*` в записях ToL #1–#15 существуют (`tools/check.py` по всем книгам серии — висячих
ссылок на основную книгу нет; 15 ошибок — общие заклинания части tol-c `coc:spell:*`, не основной книги). Схемный id
`convicts-cthulhu-en/location/sydney-town` из задания не нужен: Сидней — общий `coc:location:sydney`, места книги
`part_of` его. Карта Нового Южного Уэльса — `convicts-cthulhu-en/map/new-south-wales-1802`.

## Термины (English → русский)

Выбрано и проверено по записям основной книги; переводчик и части ToL берут эти формы.

| English | Русский |
|---|---|
| Convicts & Cthulhu | «Каторжники и Ктулху» |
| Ticket of Leave / ticket-of-leave (man) | **отпускной билет** (каторжник с отпускным билетом); псевдоним — «билет на поселение» |
| Conditional Pardon / Full (Absolute) Pardon | условное помилование / полное помилование |
| serving sentence | отбывает срок |
| convict / assigned convict / emancipist | каторжник / распределённый каторжник (каторжник-работник) / эмансипист (бывший каторжник) |
| free settler | свободный поселенец |
| New South Wales | Новый Южный Уэльс |
| NSW Corps (New South Wales Corps), «Rum Corps» | Корпус Нового Южного Уэльса |
| Rum Rebellion / Rum Economy | Ромовый бунт / ромовая экономика |
| Government House | Дом правительства |
| The Rocks | Рокс (псевдоним «Скалы») |
| Sydney Cove / Port Jackson | Сиднейская бухта / Порт-Джексон |
| Government Wharf | Казённая пристань |
| Commissariat / Commissary | интендантство / комиссар снабжения |
| Paymaster's General Store | Лавка казначея |
| Sydney Gaol | Сиднейская тюрьма |
| Female Orphan School | Школа для девочек-сирот |
| Judge-Advocate / Provost-Marshal / Surveyor-General | судья-адвокат / провост-маршал / генеральный землемер |
| Magistrate / Magistrates' Office | магистрат / Контора магистратов |
| Chaplain | капеллан |
| Van Diemen's Land / Hobart Town | Земля Ван-Димена / Хобарт-Таун |
| Coal River (Newcastle) | Коул-Ривер (Ньюкасл) |
| Vinegar Hill (Castle Hill) | Винегар-Хилл (Касл-Хилл) |
| Botany Bay | Ботани-Бей |
| Hawkesbury River | река Хоксбери |
| Blue Mountains | Голубые горы |
| bushranger | бушрейнджер |
| clever-man / clever woman | знахарь / знахарка |
| The Flash Language | «флэш» (жаргон каторжников) |
| Credit Rating | Средства |
| Charm (incl. bootlicking) | Обаяние (в том числе подхалимство) |
| Insight | Проницательность |
| Religion | Религия |
| Alcheringa Dream Lore / Dream Song | Знание Алчеринги / Песнь сновидений |
| Lore (Aboriginal) | Тайные знания (аборигенов) |
| Survival (Bush) | Выживание (буш) |
| Language (Own) / Read/Write English | Родной язык / Чтение и письмо (английский) |
| Literate / Semi-Literate / Illiterate | грамотный / полуграмотный / неграмотный |
| Story Seed | набросок (сценария) |
| Keeper | Хранитель |
| Watcher Spawn | Отродье Стража |
| The Heralds of the Silver Dawn | Глашатаи Серебряной Зари |
| The Industrious Brothers of the New World | Трудолюбивые братья Нового Света |
| The Outcast Dreamers / The Sharks-Tooth Cult / The Bacchanal Club | Отверженные сновидцы / Культ Акульего Зуба / Вакхический клуб |
| The Effigy of Scars and Suffering | Идол шрамов и страданий |
| Yowie / Pituri | Йови / питури |
| Dream Shambler | Сновидческий бродяга |

Расхождения с частями ToL (их записи не правил — ведущему при сведении): «билет на поселение» — у tol-b (ToL #5–#7,
39 мест, включая 14 черновиков профессий) → «отпускной билет»; «Скалы» — у tol-c/tol-d (ToL #8, #9, #11, #15) и «Рокс» —
у tol-b → «Рокс» (в основной книге «Скалы» заменены на «Рокс», 15 записей, прежняя форма — псевдоним `location/the-rocks`);
«Дом губернатора» — у tol-b (ToL #6, #7) → «Дом правительства»; «приписанный каторжник» (assigned convict) — в списке
терминов tol-a → «распределённый каторжник».
