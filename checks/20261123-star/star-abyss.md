# «The Star on the Shore» — часть abyss: «Key to the Abyss» (с. 65–73)

Книга `star-on-the-shore-en`, скан без текстового слоя: каждая страница прочитана по изображению.
Страницы: печатная = физическая − 3 (с. 62 на физ. 65, с. 65 на физ. 68, с. 73 на физ. 76); физ. 73 — раздатка
без номера (по порядку — с. 70). Для `books.json`: смещение +3 (physical = printed + 3); правит ведущий.

## Заголовки книги → записи базы

Префикс id: `star-on-the-shore-en/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Key to the Abyss (заставка главы) | 65 | `scenario/key-to-the-abyss` (part_of `scenario/the-star-on-the-shore`, order 2); картинка — атмосфера (`atmosphere-abyss.json`) |
| Introduction | 65 | `scenario/key-to-the-abyss` — `keeper_info` «Предыстория», `hook`, `advice`; `item/rift-bomb-cannonball` |
| Keeper's Secret | 65–66 | `scenario/key-to-the-abyss` — `keeper_info` «Тайна Хранителя»; `scene/abyss-preparation` (синий очиток, помост) |
| (рисунок: ядро с первой руной) | 66 | картинка `item/rift-bomb-cannonball` |
| The Cannonball | 66–67 | `scene/abyss-the-cannonball`; `item/rift-bomb-cannonball` |
| \*\*Provide Players with Handout Key 2\*\* | 66, 67 | `handout/handout-key-2-second-rune` |
| Research | 67 | `scene/abyss-research`; `tome/armaments-and-the-occult` |
| \*\*Provide the Players handout Key 1\*\* | 67 | `handout/handout-key-1-armaments-and-the-occult` |
| Preparation | 67 | `scene/abyss-preparation`; `item/oak-replica-cannonball`; `item/blue-stonecrop` |
| Sealing the Rift (шаги 1–11) | 67–68 | `scene/abyss-sealing-the-rift` (шаги — абзацы «• 1.» … «• 11.»); шаг сценария «Запечатывание разлома» |
| Конец мини-сценария (part of the Star on the Shore / stand-alone) | 68 | `scenario/key-to-the-abyss` — `conclusion` |
| (иллюстрация: церковь ночью) | 68 | атмосфера (`atmosphere-abyss.json`) |
| Spell for Key to the Abyss — ‘Sigillum Tempus’ aka ‘Barrier Shield’ | 69 | таблица сценария «Заклинание Щит-барьер (Sigillum Tempus)»; `item/sigillum-tempus-incense`; кандидат в общую запись `coc:spell:sigillum-tempus` — `checks/20261123-star/spell-sigillum-tempus-abyss.json` (kb/spells не мой) |
| Abyss Rift Random Encounter Chart (1d100) | 69 | таблица сценария «Случайные встречи у разлома в Бездну» (строки → записи тварей и `coc:creature:azathoth`) |
| 2nd Ruin / Handout Key 2 (рисунок) | 69 | `handout/handout-key-2-second-rune` (текст — подпись, картинка) |
| Handout Key 1 pt 1 — Armaments and the Occult, By Dr. Henry Armitage | 70 (без номера, физ. 73) | `handout/handout-key-1-armaments-and-the-occult` (текст целиком + перевод, картинка 1); `tome/armaments-and-the-occult` |
| Handout Key 1 pt 2 | 71 | та же раздатка (продолжение текста, картинка 2) |
| Creatures From the Abyss | 72 | таблица сценария «Твари из Бездны: как они себя ведут» и записи тварей (ниже) |
| • Tentacle of a Chthonian | 72 | `creature/abyss-chthonian-tentacle` (instance_of `coc:creature:chthonian-adult`) |
| • Byakhee | 72 | `creature/abyss-byakhee` (instance_of `coc:creature:byakhee`) |
| • Colours out of Space | 72 | `creature/abyss-colour-out-of-space` (instance_of `coc:creature:colour-out-of-space`) |
| • Formless Spawn | 72 | `creature/abyss-formless-spawn` (instance_of `coc:creature:formless-spawn`) |
| • Hunting Horror | 72 | `creature/abyss-hunting-horror` (instance_of `coc:creature:hunting-horror`) |
| • Star Vampire | 72 | `creature/abyss-star-vampire` (instance_of `coc:creature:star-vampire`) |
| • Dark Young | 72 | `creature/abyss-dark-young` (instance_of `coc:creature:dark-young-of-shub-niggurath`) |
| • Shoggoth | 72 | `creature/abyss-shoggoth` (instance_of `coc:creature:shoggoth`) |
| • Eye of Azathoth | 73 | строка 98–100 таблицы встреч (текст целиком), ссылка `coc:creature:azathoth` — отдельной записи нет (событие, не тварь со статблоком) |
| Общие правила разрыва (Keeper Rulebook ch. 14; хотя бы один чтец; живое / обезвреженное ядро; копия без знаков; тварь по эту сторону) | 73 | `scene/abyss-sealing-the-rift`; `scenario/key-to-the-abyss` — `conclusion`, `advice` |
| (иллюстрация: щупальца) | 73 | атмосфера (`atmosphere-abyss.json`) |

## Записи части (20)

- scenario 1: `key-to-the-abyss`
- scene 4: `abyss-the-cannonball`, `abyss-research`, `abyss-preparation`, `abyss-sealing-the-rift`
- creature 8: `abyss-chthonian-tentacle`, `abyss-byakhee`, `abyss-colour-out-of-space`, `abyss-formless-spawn`,
  `abyss-hunting-horror`, `abyss-star-vampire`, `abyss-dark-young`, `abyss-shoggoth`
- item 4: `rift-bomb-cannonball`, `oak-replica-cannonball`, `blue-stonecrop`, `sigillum-tempus-incense`
- handout 2: `handout-key-1-armaments-and-the-occult`, `handout-key-2-second-rune`
- tome 1: `armaments-and-the-occult`

Картинки (`art-abyss.json` → `art-abyss-proposals.json`, применены): `app/art/items/star-abyss-rift-bomb-cannonball.webp`,
`app/art/handouts/star-abyss-handout-key-2-second-rune.webp`, `app/art/handouts/star-abyss-handout-key-1.webp`,
`app/art/handouts/star-abyss-handout-key-1-2.webp`. Атмосфера — `atmosphere-abyss.json` (3 страницы).

## Ссылки на записи других частей (пока не созданы)

Персонажи (статблоки на страницах части town): `character/ronald-lynn` (преподобный Рональд Линн, место 21),
`character/alan-douglas` (место 17), `character/christina-smith` (место 3). Места (часть town):
`location/loc-21-…` (Олд-Слуп), `loc-16-…` (Дом ведьмы), `loc-17-…` (дом старика Дугласа), `loc-3-…` (скобяная лавка
Смита), `loc-11-…` (аптека «Гранит»), `loc-31-…` (пекарня «Сэнди-Бэй»). Основной сценарий (часть core):
`scenario/the-star-on-the-shore`. Окончательные id подставляются при сведении.

## Опечатки и сомнения

| Где | Напечатано | Что в базе |
|---|---|---|
| с. 68, шаг 5 | «Abyss Rift Random Encounter chart on page 71» | таблица — с. 69; исправлено (errata `fixed: true`, corrections) |
| с. 69, компоненты | «pharmacy or bakery (Locations 11 or 13 in Rockport)» | место 13 — парикмахерская Бейли, пекарня — место 31; исправлено на 11 и 31 |
| с. 69, стоимость | «1d3 Sanity and Magic points per caster to start» | неясно, 1d3 ли и ПМ; оставлено как напечатано, errata |
| с. 65 / с. 67 | «Miskatonic University Library» / «Arkham University Library» | одна библиотека — `coc:location:orne-library`; errata без правки |
| с. 66 / с. 69, 72 | щупальце при преждевременном вынимании ядра: 0/1d3, 1/1d6, отпускает после 30 урона за раунд; «Tentacle of a Chthonian»: 0/1d6, отпускает после 15 урона | оба значения на своих местах; errata в сцене «Ядро в колокольне» |
| с. 67 / раздатка | «Armament and the Occult» / «Armaments and the Occult» | название по раздатке, первое — в aliases |
| с. 69 | «2nd Ruin» (подпись к раздатке) | опечатка вместо «2nd Rune»; в text раздатки — как напечатано, в переводе «Вторая руна» |
| с. 66 / раздатка с. 71 | ядро взорвётся «через несколько минут» / «probably within 10 to 15 minutes» | оба в записи ядра и сцене |
| раздатка «Ключ» 1 | «ordinance» вместо «ordnance» | английский текст как напечатан |

## Не взято

- Ничего из текста с. 65–73 не отброшено. Отдельной записи «Око Азатота» нет: это строка таблицы встреч (текст
  целиком), ссылка на общую запись Азатота.
- Заклинание Щит-барьер (Sigillum Tempus) не заведено в `kb/spells/` (справочник общий, части не принадлежит; у
  предложений нет операции создания записи): полностью — в таблице сценария и в готовом кандидате
  `spell-sigillum-tempus-abyss.json` (схема проверена). После его заведения — поставить `spell` в
  `tome/armaments-and-the-occult` (`spells[0]`).
- Помост у шпиля, питомник в Бостоне, контора агентства «Тёмное крыло» — без своих записей (мелочи без механики; в
  текстах сцен; бостонские места по-прежнему без схемы id — открытый вопрос conventions).
- Размер награды Рассудка («receive a sanity bonus») книга не называет.

## Термины (English → русский)

| English | Русский |
|---|---|
| Key to the Abyss | Ключ к Бездне |
| The Star on the Shore | Звезда на берегу |
| the Abyss | Бездна |
| rift | разлом |
| tear | разрыв |
| Rift Bomb | разломная бомба |
| the Old Sloop | Олд-Слуп (церковь Олд-Слуп) |
| HMS Nymphe | HMS «Нимфа» |
| Rev. (Ronald) Lynn | преподобный (Рональд) Линн |
| Alan Douglas | Алан Дуглас |
| Christina Smith | Кристина Смит |
| Smith Hardware | скобяная лавка Смита |
| Witch House | Дом ведьмы |
| Dark Wing Detectives | детективное агентство «Тёмное крыло» |
| Armaments and the Occult | «Вооружение и оккультизм» |
| Sigillum Tempus / Barrier Shield | Щит-барьер (Sigillum Tempus) |
| chant / chanters | песнопение / чтецы |
| blue stonecrop (Sedum reflexum) | синий очиток |
| holly / rue / star anise | падуб / рута / бадьян |
| incense | благовоние |
| wooden (oak) replica | дубовая копия ядра |
| live dud | «живой» неразорвавшийся снаряд |
| Abyss Rift Random Encounter Chart | Случайные встречи у разлома в Бездну |
| Creatures From the Abyss | Твари из Бездны |
| Eye of Azathoth | Око Азатота |
| Tentacle of a Chthonian | щупальце хтонийца |
| power resistance check | проверка сопротивления (МОЩ твари против общей МОЩ заклинателей) |
| demolition check | проверка Взрывчатки (официальный навык) |
| Spot Hidden / Library Use / Art/Craft / Idea | Внимание / Работа в библиотеке / Искусство/ремесло / проверка Идеи (официальные) |
