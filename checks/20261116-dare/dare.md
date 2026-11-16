# The Dare (`the-dare-en`) — перенос в базу (Р-251)

Книга: «The Dare», Kevin Ross, ревизия Bret Kramer, «Grab the Machete» — Brian M. Sammons, правила «Call of Kid-thulhu» — Bret Kramer (Sentinel Hill Press / Chaosium, 2020). PDF 71 стр.

**Смещение страниц:** печатная = физическая − 7 (печатная «1» на физ. 8, «8» на физ. 15, «46» на физ. 53, «62» на физ. 69), т. е. `offset: -7`. Физ. 1–7 (обложка, форзац, фото, титул, выходные данные, оглавление, посвящение) и физ. 70–71 (задняя обложка «i», пустая) — без номеров. В `books.json` не правилось — ставит ведущий.

**Записи:** 148 файлов в `kb/books/the-dare-en/`: сценарий 1, сцены 33, персонажи 21 (10 прегенов + 11 NPC), существа 9, места 45, предметы 18, книги Мифов 2, раздатка 1, карты 6, правила 12. Картинки: 22 (`app/art/*/dare-*.webp`), карты 6 (`app/maps/dare-*.jpg`). Предложений к общим записям — 0 (`proposals-dare.json`).

Проверено: сценарий в базе в русском переводе не найден (Grep «Барнакер», «Barnaker», «Растис», «Роджер Симмонс», «Kid-thulhu» по `kb/`).

## Заголовок книги → запись

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка, титул, выходные данные, оглавление) | физ. 1–6 | `scenario/the-dare` (sources); картинки — `atmosphere.json` |
| Dedication | физ. 7 | не взято (посвящение автора без игрового материала) |
| I Double-Dog Dare Ya (Kevin Ross) | 1–2 | `scenario/the-dare` (keeper_info: эпохи, восстановленная сцена; sources) — остальное не взято (история турнира и вдохновения) |
| The Dare: Introduction | 3 | `scenario/the-dare` (summary, keeper_info) |
| PG vs. R: Two Scenario Options | 3–4 | `scenario/the-dare` (keeper_info); варианты PG/R — в сценах |
| Setting Note | 4 | `scenario/the-dare` (keeper_info), `location/hometown` |
| Running The Dare | 4 | `scene/meeting-at-the-house`, `scene/interior`, `scenario/the-dare` (advice) |
| Controlling the Pace | 4–5 | `scenario/the-dare` (advice) |
| The Storm (врезка) | 5 | `scene/storm` |
| A Short History of the Barnaker House | 6 | `location/barnaker-house` (history), `character/evelyn-barnaker` |
| The Barnaker House: The Neighborhood | 6 | `location/barnaker-neighborhood` |
| Exterior: General Notes | 6–7 | `scene/exterior` |
| Roger Simmons (врезка) | 7 | `character/roger-simmons` |
| The Exterior of the Barnaker House | 7 | `scene/exterior`, `location/barnaker-house` |
| Fence | 7 | `location/barnaker-fence`, `scene/exterior` |
| The Yard | 7 | `location/barnaker-yard`, `scene/exterior` |
| Exterior Map | 8, 56 | `map/exterior-map` |
| The Shed; Roger’s Actions (PG/R) | 9 | `scene/shed`, `location/barnaker-shed`, `item/shed-tools`, `item/kerosene-can` |
| The Fish Pond | 9 | `scene/fish-pond`, `location/barnaker-fish-pond` |
| The Cistern | 10 | `scene/cistern`, `location/barnaker-cistern` |
| The Front Porch | 10 | `scene/front-porch`, `location/barnaker-front-porch`, `location/under-porch` |
| The Interior: General Notes; Smell; Noises | 10 | `scene/interior` |
| Ground Floor Map | 11, 57 | `map/ground-floor-map` |
| Lighting | 12 | `scene/interior`, `item/fat-candles` |
| Roger’s Actions (ключ) | 12 | `scene/interior`, `item/front-door-key` |
| The Entry Hall (и Back Entryway) | 12 | `scene/entry-hall`, `location/barnaker-entry-hall`, `location/barnaker-back-entryway` |
| The Kitchen; Roger’s Actions | 12–13 | `scene/kitchen`, `location/barnaker-kitchen`, `item/kitchen-knives` |
| The Dining Room | 12–13 | `scene/dining-room`, `location/barnaker-dining-room` |
| The Parlor | 13 | `scene/parlor`, `location/barnaker-parlor`, `item/old-danny-knapsack`, `item/fireplace-poker` |
| The Living Room; Roger’s Actions | 13–14 | `scene/living-room`, `location/barnaker-living-room`, `creature/rastis`, `item/briggs-photo` |
| Foreshadowing, Literally (врезка) | 14 | `scene/cupola` |
| Upper Floor: General Notes (Landing, Bathroom, Top of the Stairs) | 14 | `scene/upper-floor`, `location/barnaker-bathroom`, `location/barnaker-upper-hall` |
| Through a Mirror, Dark Magically (врезка) | 14 | `scene/upper-floor`, `character/evelyn-barnaker` (abilities), `item/house-mirrors` |
| The Girl’s Bedroom (и Girl’s Room Closet, Small Attic Space) | 14–16 | `scene/girls-bedroom`, `location/barnaker-girls-bedroom`, `location/barnaker-girls-room-closet`, `location/barnaker-small-attic-space` |
| Upper Floor Map | 15, 58 | `map/upper-floor-map` |
| The Sewing Room | 16 | `scene/sewing-room`, `location/barnaker-sewing-room`, `location/barnaker-sewing-room-closet`, `item/cloth-doll` |
| Using Rastis (врезка) | 16 | `scene/using-rastis`, `creature/rastis` (abilities) |
| The Cupola | 17 | `scene/cupola`, `location/barnaker-cupola`, `creature/corpse-lights` |
| An Alternative Encounter (врезка) | 17 | `scene/cupola`, `creature/terrible-bat-thing` |
| The Terrible Bat-Thing (статблок) | 17 | `creature/terrible-bat-thing` |
| The Scorched Bedroom; Roger’s Actions | 17–18 | `scene/scorched-bedroom`, `location/barnaker-scorched-bedroom` |
| The Boy’s Bedroom | 18 | `scene/boys-bedroom`, `location/barnaker-boys-bedroom`, `location/barnaker-boys-bedroom-closet`, `item/silver-coin-collection`, `item/telescope` |
| The Master Bedroom; Roger’s Actions | 18–19 | `scene/master-bedroom`, `location/barnaker-master-bedroom`, `location/barnaker-master-bedroom-closet`, `character/old-danny`, `item/old-danny-effects` |
| (Large Attic Space, вырезки) | 19–20 | `scene/large-attic-space`, `location/barnaker-large-attic-space`, `item/briggs-scrapbook` |
| Sympathy for the Devil-Spawn (врезка) | 20 | `scene/sympathy-for-the-devil-spawn` |
| The Attic | 20 | `scene/attic`, `location/barnaker-attic` |
| The Basement (Workroom) | 20–21 | `scene/basement`, `location/barnaker-basement`, `location/barnaker-workroom` |
| The Rat-Thing Librarian (статблок) | 21 | `creature/rat-thing-librarian` |
| Optional Encounter: Ace Arrives | 21 | `scene/ace-arrives`, `character/ace-simmons`, `item/ace-revolver` |
| Coal Room; Pantry | 21–22 | `scene/coal-room-pantry`, `location/barnaker-coal-room`, `location/barnaker-pantry`, `item/jar-of-eyes` |
| The “Study” | 22–24 | `scene/study`, `location/barnaker-study`, `tome/evelyn-grimoire`, `handout/handout-1-grimoire-page` |
| Attic Map | 22, 59 | `map/attic-map` |
| Basement Map | 23, 60 | `map/basement-map` |
| The Bedroom (подвал) | 24 | `scene/basement-bedroom`, `location/barnaker-basement-bedroom`, `location/barnaker-basement-bedroom-closet`, `item/evelyn-portrait` |
| Fighting Evelyn (Silver and Iron, Fire, Connection to Rastis, Reflection) | 24 | `scene/fighting-evelyn`, `character/evelyn-barnaker` (abilities) |
| Beneath the Basement | 25–27 | `scene/beneath-the-basement`, `location/beneath-the-basement` и места A–F, `item/hand-of-glory` |
| Tunnels Map Key; Tunnels Map | 27, 61 | `map/tunnels-map`, `location/tunnel-entry-chamber`, `location/porch-tunnel`, `location/bone-heap`, `location/evelyn-alcove`, `location/cistern-brickwork` |
| The Battle Against Evelyn (Evelyn, Rastis, Roger, Rat-things and Bat-things, Rats and Bats) | 28 | `scene/battle-against-evelyn` |
| Bringing Down the House (врезка) | 28 | `scene/battle-against-evelyn` (mechanics) |
| (стр. 29 — копия раздатки 1) | 29 | `handout/handout-1-grimoire-page` (sources); картинка — atmosphere |
| Ending the Scenario: Closing Scenes (Loss, Draw, Win) | 30 | `scene/closing-scenes`, `scenario/the-dare` (conclusion) |
| Creature and Character Statistics: Roger Simmons | 31 | `character/roger-simmons` |
| Rat Packs, rattus rattus | 32 | `creature/rat-packs` |
| Bat Swarms, myotis lucifugus | 32 | `creature/bat-swarms` |
| The Rat-Things, unnatural malevolent scuttlers | 32 | `creature/evelyn-rat-things` |
| The Bat-Things / A Dozen Bat-Things | 33 | `creature/bat-things` |
| Rastis (Special Powers) | 33–34 | `creature/rastis` |
| Evelyn’s Spells (Create Skin Servitor, Dampen Flame, See Through Mirrors, Seal House) | 34 | `tome/evelyn-spellbook`, `creature/skin-servitor` |
| Evelyn Barnaker (статблок, Special Powers) | 34–35 | `character/evelyn-barnaker` |
| The Call of Kid-thulhu: Introduction; The Absolute Basics; Understanding Your Character Sheet | 36–37 | `rule/call-of-kid-thulhu` |
| Rules Basics and Skills: Statistics | 37 | `rule/kid-statistics` |
| Skills | 37–38 | `rule/kid-skills` |
| How Skill Rolls Work; Bonus and Penalty Dice | 38 | `rule/kid-skill-rolls` |
| Combat | 38–39 | `rule/kid-combat` |
| Injury | 39 | `rule/kid-injury` |
| Sanity | 39 | `rule/kid-sanity` |
| Pushing Rolls | 39 | `rule/kid-pushing-rolls` |
| Equipment | 39–40 | `rule/kid-equipment` |
| Roleplaying as an 80s Kid; Halloween Costumes | 40–41 | `rule/kid-roleplaying-80s` |
| Creating Your Own Kid Investigator; Creating Skills; Equipment | 40–41 | `rule/kid-creating-investigator` |
| Grab the Machete (10 фильмов) | 42–43 | `rule/grab-the-machete` |
| Yearbook Photos | 44–45 | не взято как записи: портреты на выбор без привязки к персонажам — `atmosphere.json` (вопрос владельцу) |
| Pre-Generated Kid Investigators | 46–55 | `character/kyle-robards`, `darren-pickett`, `joey-delafano`, `rich-davis`, `paul-laughlin`, `jay-thurston`, `joe-bachman`, `sherwood-kent`, `charles-bruckner`, `harry-enslin` |
| Maps and Handout | 56–62 | `map/*` (6), `handout/handout-1-grimoire-page` |
| Задняя обложка | i | `scenario/the-dare` (sources); картинки — atmosphere |

## Не взято

- Посвящение (физ. 7), благодарности и выходные данные (физ. 5) — без игрового материала.
- Предисловие Кевина Росса «I Double-Dog Dare Ya» — взяты только игровые сведения (эпохи, восстановленная сцена); история турнира GenCon и источники вдохновения — не взяты (авторский текст без механики).
- «Yearbook Photos» (с. 44–45): 48 детских портретов с шуточными именами (соавторы и спонсоры) — портреты для своих листов; к записям не привязаны, в `atmosphere.json`. Вопрос владельцу: заводить ли их как картинки (например, у записи правила или прегенов).
- Шуточные отзывы и аннотация задней обложки — atmosphere.
- Мать и старший сын Бриггсов, губернатор Фипс, пёс Рекс — упомянуты в текстах записей, своих записей нет.
- Мелочи без механики (напольные часы, игра в камушки, осиное гнездо, ножницы, труп енота) — в текстах сцен, отдельных записей нет.

## Опечатки и противоречия книги

| Где | Напечатано | Ожидалось | В записи |
|---|---|---|---|
| Rastis, Bite | 35% (17/6) | (17/7) | исправлено (Р-35), `creature/rastis` |
| Bat-Things, описание | «mixture of human and rat» | human and bat | исправлено, `creature/bat-things` |
| Bat-Things #10, DEX | 480 | ≤135 | как напечатано, errata |
| Bat-Things #3, HP | 3 | 4 | как напечатано, errata |
| Rat-Thing Librarian | Dodge 45% и Dodge 85% | одно значение | оба, errata |
| Rat-Thing Librarian, SAN | 1/1D6 | 0/1D6 (как у других тварей) | как напечатано, errata |
| Rat Packs / Bat Swarms | «average slats» | stats | errata (`rat-packs`) |
| Roger, Large Knife | 1D6+1 (с. 31) / 1D4 (с. 28) | одно | errata Роджера и сцены битвы |
| Гибель Роджера | 5 дней назад (с. 7) / две недели назад (с. 18) | одно | errata сцены «Обожжённая спальня» |
| Evelyn, потеря Рассудка | 1D3/2D4+1 и 1D4/2D6 (с. 35) / 1D3/1D10 и 1D2/1D6+1 (с. 25) | одно | errata Эвелин |
| Оглушение Эвелин после гибели Растиса | 1D3 (с. 24, 34) / 1D3+1 (с. 28) | одно | errata Эвелин и сцены битвы |
| Evelyn, Move | 6 | 7 | как напечатано (задумано: почти неподвижна) |
| «See page XX» (огонь) | page XX | номер | errata сцены «Как сражаться с Эвелин» |
| «slowed by X» (затопление) | X | число | errata сцены «Битва с Эвелин» |
| «notebook … in the attic (see page 20)» | блокнот, с. 20 | альбом вырезок, с. 19 | errata `item/briggs-scrapbook` |
| Tunnels Map Key vs карта | ключ TD, A–F; на карте TD, E, C, X, Up, B, A | одна система | метки D, F вычислены; заметки в `map/tunnels-map`, errata `location/cistern-brickwork` |
| Карта 1-го этажа | «Family Room» | «Living Room» (текст) | псевдоним, заметка |
| Joey Delafano | Delafano (имя) / Delfano (текст листа) | одно | errata прегена |
| Kid creation | «2D6+3 x 6 for APP and CON» | ×5? | как напечатано, errata `rule/kid-creating-investigator` |
| Названия навыков в тексте | Playing With Matches, Playing with Fire, Notice Things, Fix Things | Play with Matches, Notice Stuff, Fix Stuff | молча по списку навыков (Р-39), заметка в `rule/kid-skills` |

## Термины этой книги (English → Russian)

| English | Русский |
|---|---|
| The Dare | На спор |
| Kid investigator | юный сыщик |
| The Call of Kid-thulhu | Зов Кид-тулху |
| Barnaker House | дом Барнакеров |
| Be a Pal | Быть другом |
| Be Bossy | Командовать |
| Be Sneaky | Красться |
| Dodge | Уклонение |
| Fighting | Драка |
| First Aid | Первая помощь |
| Fix Stuff | Чинить вещи |
| Gym Class | Физкультура |
| Nature | Природа |
| Notice Stuff | Замечать всякое |
| Play with Matches | Играть со спичками |
| Reading, Writing, and Arithmetic | Чтение, письмо и счёт |
| Science Class | Школьные науки |
| Spooky Stuff | Жуткие штуки |
| Taunt | Дразнить |
| Spawn Vermin (Evelyn) | Порождать паразитов |
| Issue Late Fees (Librarian) | Выписывать штрафы за просрочку |
| BB Gun | Пневматическая винтовка |
| Freak Out | Психануть |
| Totally Lose It | Совсем слететь с катушек |
| Kid (profession) | Ребёнок |
| fraidy-cat | трусишка |
| Skin Servitor | кожаный слуга |
| Rat-thing | крысиная тварь (как в базе) |
| Bat-thing | нетопыриная тварь |
| Terrible Bat-Thing | ужасная нетопыриная тварь |
| Rat-Thing Librarian | крысиная тварь-библиотекарь |
| Rat Pack / Bat Swarm | стая крыс / стая летучих мышей |
| Corpse lights | трупные огни |
| familiar | фамильяр |
| Grandmother Illusion | Бабушкин морок |
| Devour | Пожирание |
| Hand of Glory | Рука славы (как в базе) |
| Black Man | Чёрный человек |
| Create Skin Servitor | Создание кожаного слуги |
| Dampen Flame | Притушить пламя |
| See Through Mirrors | Взгляд сквозь зеркала |
| Seal House | Запечатать дом |
| Parlor / Living Room (Family Room) | гостиная для приёмов / общая комната |
| Cupola | купол |
| Study | кабинет |
| Large / Small Attic Space | большое / малое чердачное помещение |
| Beneath the Basement | под подвалом (нора Эвелин) |
| PG / R | версия «PG» / версия «R» |
| Grab the Machete | Хватай мачете |
| Yearbook Photos | Фото из школьного альбома |
| Handout #1 | раздатка 1 |
| Прозвища прегенов | Книжный червь, Спортсмен, Крутой, Напарник, Шутник, Сноб, Бедняк, Скаут, Чудик, Всезнайка |

## Вопросы ведущему и владельцу

1. Записи правил книги (`the-dare-en/rule/*`) — первые книжные записи вида `rule`; проверить, что просмотрщик их показывает.
2. Детские навыки не заведены как общие навыки (`kb/skills/`): они описаны в `rule/kid-skills`, в статблоках — только `name`. Нужны ли общие записи навыков?
3. Собственные заклинания Эвелин (Create Skin Servitor, Dampen Flame, See Through Mirrors, Seal House) — описаны в `tome/evelyn-spellbook`, в справочнике заклинаний их нет (`spell: null`). Кандидаты в `coc:spell:*`.
4. «Call the Black Man (Nyarlathotep)» связано с `coc:spell:call-dismiss-nyarlathotep`, «Create Storm» — с `coc:spell:create-storm-folk` (другого варианта нет) — наш выбор.
5. «Grab the Machete» в задании назван бонусным сценарием; в книге это эссе с советами — перенесено записью правила `rule/grab-the-machete`.
6. Оставшиеся находки `completeness` по картинкам — пустые рамки врезок (вынесены в `atmosphere.json`).
