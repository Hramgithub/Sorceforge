# «A Time to Harvest», Month 1 — часть ep1 (эпизод 1): покрытие

Книга `time-to-harvest-1-en`, физ. 36–71 (печ. 34–69; печатная = физическая − 2, проверено по изображениям физ. 39, 43, 57, 61, 62, 67, 70).
В PDF 71 страница: физ. 72 (печ. 70) из задания не существует. Первая страница эпизода (печ. 34, физ. 36) входит в диапазон
части world, но записей world не касается — взята в источники сценария эпизода.

Записи части: 58 файлов в `kb/books/time-to-harvest-1-en/` (сценарий 1, сцены 23, персонажи 11, существа 4, места 10, карты 2,
раздатки 4, предметы 3); картинки `app/art/characters/harvest-ep1-robert-blaine.webp`, `app/art/handouts/harvest-ep1-harvest-papers-4…7.webp`,
`app/maps/harvest-ep1-maclearan-farm-map.jpg`, `app/maps/harvest-ep1-shack-map.jpg`. Предложения — `proposals-ep1.json` (37),
картинки — `art-ep1.json` (применено), рамки вырезки раздаток — `handout-boxes-ep1.json`.

Сокращения: `ep` = `time-to-harvest-1-en/scenario/episode-1`; `sc/…` = `time-to-harvest-1-en/scene/…`; `ch/…`, `loc/…`, `cr/…`,
`ho/…`, `it/…`, `map/…` — записи книги `time-to-harvest-1-en`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Episode 1 (эпиграф — Лавкрафт, «The Colour Out of Space») | 34 | `ep` (эпиграф — «Не взято») |
| Field Research | 34 | `ep` → `hook` |
| Running Episode One (четыре цели) | 34–35 | `ep` → `keeper_info` |
| Start: The Trip To Cobb’s Corners | 35 | `sc/ep1-trip-to-cobbs-corners` |
| Joe Harlow, age 58, truck driver | 35 | `ch/joe-harlow` |
| Prior Knowledge | 36 | `sc/ep1-trip-to-cobbs-corners` |
| Professor Roger Harrold, age 44, anthropologist | 36 | `ch/roger-harrold` |
| Getting To Know You | 36 | `sc/ep1-trip-to-cobbs-corners` |
| Robert Blaine, age 24, expedition leader (+ портрет) | 36–37 | `ch/robert-blaine` (портрет — `images`) |
| Clarissa Thurber, age 21, chemistry major | 37 | `ch/clarissa-thurber` |
| Jason Trent, age 20, history major | 37–38 | `ch/jason-trent` |
| Roderick “Little Rod” Block, age 21, geography major | 38 | `ch/roderick-block` |
| Louis Gibbons, age 22, botany major | 38 | `ch/louis-gibbons` |
| Harold Higgins, age 20, geology major | 38 | `ch/harold-higgins` |
| William Noakes, age 20, anthropology major | 39 | `ch/william-noakes` |
| Terrence Laslow, age 22, history and psychology majors | 39 | `ch/terrence-laslow` |
| The Romance | 39 | `sc/ep1-trip-to-cobbs-corners` |
| Day One: Arrival | 39 | `sc/ep1-maclearan-farmhouse` |
| The Maclearan Farmhouse | 39–40 | `sc/ep1-maclearan-farmhouse`, `loc/maclearan-farmhouse`, `loc/maclearan-flowerbed`, `loc/maclearan-outhouse` |
| A Trip To Jim’s Grill | 40 | `sc/ep1-jims-grill` (место — `loc/jims-grill`, часть world) |
| Jim and Ann Haggerty, age 42 and 39 | 40 | `ch/jim-haggerty`, `ch/ann-haggerty` (world) — участники `sc/ep1-jims-grill`; источник — предложение |
| Jason Haggerty, age 14 | 40 | `ch/jason-haggerty` (world) — участник `sc/ep1-jims-grill`; источник — предложение |
| Richard Wendell, age 35, nosey small-town reporter | 40, 42 | `ch/richard-wendell` (world) — участник `sc/ep1-jims-grill`; статблок — предложение |
| The Maclearan Farm Map | 41 | `map/maclearan-farm-map` (13 меток) |
| Enter The Sheriff | 42 | `sc/ep1-jims-grill` |
| The Sheriff’s Speech (врезка) | 42 | `sc/ep1-jims-grill` (речь целиком) |
| The Lawmen | 42 | `sc/ep1-jims-grill` |
| Sheriff Dan Spenser, age 40, puritanical lawman | 42–43 | `ch/dan-spenser` (world); статблок — предложение |
| Deputy John Cutter, age 20, baby faced cult leader | 43 | `ch/john-cutter` (world); статблок — предложение |
| The Full Treatment | 43 | `sc/ep1-full-treatment` |
| Red Herrings Galore | 43–44 | `sc/ep1-red-herrings`, `it/witch-cult-in-western-europe`, `it/mandrake-root` |
| The Dream Gate | 44 | `sc/ep1-perchance-to-dream-1`, `it/dream-gate`, `ch/john-jeffrey`, `ep` → `keeper_info` |
| Cobb’s Corners Player Map | 45 | `map/cobbs-corners-player` (world); ссылка из `sc/ep1-wild-hunt` |
| Perchance to Dream: Part One | 46 | `sc/ep1-perchance-to-dream-1` |
| Day Two: Research Begins | 46 | `sc/ep1-wild-hunt` |
| The Wild Hunt | 46 | `sc/ep1-wild-hunt` |
| Folklore Interviews (10 рассказов) | 46–48 | `sc/ep1-folklore-interviews`; рассказы — таблица «Рассказы местных жителей» в `ep` |
| Handout: Harvest Papers 4 | 47, 66 | `ho/harvest-papers-4` (текст + перевод + картинка) |
| Handout: Harvest Papers 5 | 48, 67 | `ho/harvest-papers-5` |
| Slim Pickings For Diggers | 48 | `sc/ep1-slim-pickings` |
| At The End Of The Day | 48 | `sc/ep1-slim-pickings` |
| Perchance to Dream: Part Two | 48 | `sc/ep1-perchance-to-dream-2` |
| Day Three: The Accident | 48–49 | `sc/ep1-the-accident`, `loc/gismend-river-bridge` |
| Harry Higgins’ Rant | 49–50 | `sc/ep1-harry-higgins-rant` (речь целиком) |
| Handout: Harvest Papers 6 | 50, 68 | `ho/harvest-papers-6` |
| Perchance to Dream: Part Three | 50 | `sc/ep1-perchance-to-dream-3` |
| Day Four: The Gathering | 50–51 | `sc/ep1-the-gathering`, `loc/broken-hill-mound` (часть `loc/broken-hill` world) |
| The Folklorists Meet Agnus | 51 | `sc/ep1-folklorists-meet-agnus`, `loc/bellweather-house` |
| Agnus Bellweather, age 88, knowledgeable local | 51–52 | `ch/agnus-bellweather` (world) — участник сцены; источник — предложение |
| Handout: Harvest Papers 7 — Mrs. Bellweather’s Tale | 51, 68 | `ho/harvest-papers-7` |
| What Happens Next? | 52 | `sc/ep1-dealing-with-the-dream-gate` |
| Dealing With The Dream Gate | 52 | `sc/ep1-dealing-with-the-dream-gate` |
| The Enchanted Woods | 52 | `sc/ep1-dealing-with-the-dream-gate`, `loc/sugar-maple-forest`, `cr/zoog` |
| The Clearing | 52–53 | `sc/ep1-the-clearing`, `loc/jeffrey-clearing`, `cr/moon-beast` |
| John Jeffrey | 53–54 | `sc/ep1-john-jeffrey` |
| John Jeffrey, age 25, failed experiment | 53 | `ch/john-jeffrey` |
| Optional (врезка о проходе сквозь Врата) | 54 | `sc/ep1-john-jeffrey`, `it/dream-gate` → `mechanics` |
| The Cabin In The Woods | 54–55 | `sc/ep1-cabin-in-the-woods`, `loc/the-shack`, `loc/shack-root-cellar`, `cr/men-of-leng` |
| The Shack Map | 55 | `map/shack-map` (11 меток) |
| Emily Braithwaite, age 18, simple-minded girl | 55 | `ch/emily-braithwaite` (world) — участник `sc/ep1-cabin-in-the-woods`; статблок — предложение |
| Optional Ending: Dream Gate Resolution | 55–56 | `sc/ep1-dream-gate-resolution` |
| Back At The Farm: One Way For Things To Go Down | 56 | `sc/ep1-back-at-the-farm` |
| Back At The Mound: Another Way For Things To Happen | 56 | `sc/ep1-back-at-the-mound` |
| Captured By The Mi-Go? | 57 | `sc/ep1-day-five-conclusion`, `ep` → `advice` |
| Rewards For Episode One | 57 | `ep` → `conclusion` |
| Day Five: Conclusion | 57 | `sc/ep1-day-five-conclusion` |
| Appendix A: Personalities and Monsters (указатель по ролям) | 58 | `ep` → `sources` |
| University People: Harrold, Blaine, Block, Gibbons, Higgins, Laslow, Noakes, Thurber, Trent | 58–59 | статблоки в `ch/…` этих персонажей |
| Locals of Cobb’s Corner: Sheriff Dan Spenser, Deputy John Cutter | 59–60 | предложения `statblock` к `ch/dan-spenser`, `ch/john-cutter` (world) |
| Joe Harlow, Cobb’s Corners local and truck driver | 60 | `ch/joe-harlow` |
| Richard Wendell, nosey small-town reporter | 60 | предложение `statblock` к `ch/richard-wendell` (world) |
| Monsters: Mi-Go, standard form | 60 | `cr/mi-go-standard-form` (`instance_of` `coc:creature:mi-go`) |
| Dream Gate Characters: John Jeffrey | 60 | `ch/john-jeffrey` |
| Dream Gate Characters: Emily Braithwaite | 60–61 | предложение `statblock` к `ch/emily-braithwaite` (world) |
| Men of Leng, sadistic servants | 61 | `cr/men-of-leng` |
| Moon-beast, loathsome and cruel | 61 | `cr/moon-beast` |
| Zoogs, pesky and cunning | 61 | `cr/zoog` |
| Spell Appendix: Alter Weather (+ таблица Weather Components) | 62 | `coc:spell:alter-weather` (таблица уже в описании); предложение-источник |
| Augury | 62–63 | `coc:spell:augury-folk`; предложение-источник |
| Blight/Bless Crop | 63 | `coc:spell:blight-bless-crop`; предложение-источник |
| Cause Disease | 63 | `coc:spell:cause-disease`; предложение-источник (расхождение цены) |
| Command Animal (Folk) | 63 | `coc:spell:command-animal-folk`; предложение-источник (расхождение цены) |
| Contact Shub-Niggurath | 63 | `coc:spell:contact-shub-niggurath`; предложение-источник |
| Grasp Of Cthulhu | 63–64 | `coc:spell:grasp-of-cthulhu`; предложение-источник |
| Lame/Heal Animal | 64 | `coc:spell:lame-heal-animal-folk`; предложение-источник |
| Raise Night Fog | 64 | `coc:spell:raise-night-fog`; предложение-источник |
| Red Sign, The | 64 | `coc:spell:red-sign-of-shudde-mell`; предложение-источник и псевдоним «Red Sign, The» |
| Player Handouts: Harvest Papers 1, 2 | 65 | `ho/harvest-papers-1`, `ho/harvest-papers-2` (world; уже цитируют физ. 67) |
| Harvest Papers 3a, 3b | 66, 67 | `ho/harvest-papers-3a`, `ho/harvest-papers-3b` (world; уже цитируют физ. 68, 69) |
| Harvest Papers 4, 5, 6, 7 (сборные) | 66–68 | `ho/harvest-papers-4…7` (картинки — из сборных) |
| Cobb’s Corners Player Map (повтор) | 69 | `map/cobbs-corners-player` (world); предложение — источник физ. 71 |

## Не взято (и почему)

- Эпиграф эпизода (цитата из «The Colour Out of Space», с. 34) — литературная цитата без игрового содержания; упомянута здесь.
- Безымянный фермер с ружьём (день третий, с. 48) — эпизодическая роль без статблока; его реплика — в `sc/ep1-the-accident`, записи нет.
- Обрушившийся амбар, старый колодец у лачуги, индейский наконечник стрелы, фотоаппарат с магниевой вспышкой, фонограф, «Шевроле» модели K,
  бутылка виски Блейна — мелочи без механики; текстом в сценах и местах (амбар — метка карты дома на лес).
- Рекламный текст «Wilmington Realty» на плане дома — дословно в `quality.notes` карты.
- Ресторан «Регата» (Аркхэм) и рассказ «Серебряный ключ», народ К’н-йана, дополнение «H.P. Lovecraft’s Dreamlands» — упоминания, текстом.
- Сара Маклиран, Джимми Маклиран, Хаггерти, Мейбл Каррутерс, Оуэн Перри, Бойд Паттерсон — записи части world; в сценах — ссылками.
  Дафна Девайн (`time-to-harvest-1-en/character/daphne-devine`) — ещё не заведена частью world; ссылки на неё (сцены, Блейн, Джеффри)
  добавит повторный прогон `links.py` (или ведущий), сейчас — текстом. Культ Младых уже связан.
- Отдельной атмосферы на страницах части нет (`atmosphere-ep1.json` не создан): все картинки физ. 36–71 — портрет, карты и раздатки записей.
- Картинки раздаток «Жатва» 1–3б на физ. 67–69 и повтор карты игроков на физ. 71 — для записей части world (не мои файлы).

## Опечатки и расхождения книги

| Где | Напечатано | Ожидалось | В базе |
|---|---|---|---|
| Clarissa Thurber, статблок (с. 59) | Brawl «1D3 + 1D4» при «DB: 0» | 1d3 | как напечатано, `errata` |
| Clarissa Thurber (с. 59) | Dodge 30% | не ниже 35% (½ ЛВК 70) | как напечатано, `errata` |
| Joe Harlow (с. 60) | Move 6 | 5 (58 лет) или 7 | как напечатано, `errata` |
| Richard Wendell (с. 60) | MP 10 | 8 (МОЩ 40) | предложение `errata` в запись world |
| John Jeffrey (с. 60) | HP n/a, Move n/a | — | задумано книгой (Р-76), `errata` с пояснением |
| Clarissa Thurber (с. 59) | HP 12 при (75+40)/10 = 11,5 | — | округление вверх, приём книги (Р-161), заметка |
| с. 38 | «Lewis Gibbons» | Louis Gibbons | псевдоним, заметка |
| с. 49–50 | «Harry Higgins» | Harold Higgins | псевдоним, заметка |
| с. 42–43 | «Sheriff Spencer» | Spenser | заметка в сцене |
| с. 47 | «Sara Maclearan» | Sarah | цитата в таблице как напечатано |
| с. 54 | «Jeffery» | Jeffrey | псевдоним, заметка |
| с. 46 | «Broken Hills region» | Broken Hill | заметка в сцене |
| с. 60, заклинания Каттера | «Call Shub-Niggurath Cause Disease» (без запятой) | два заклинания | разобрано на два в предложении |
| с. 68 (сборная раздатка 7) | «I wonder what’s why we was granted» | «I wonder why…» (с. 51) | текст по с. 51, заметка |
| с. 36, 34 | профессор Лирмонт — «Geology Dept.» | в «Аркхэме» (`arkham-en/character/campus-ashley-learmonth`) — металлург | заметка в сцене поездки |
| Spell Appendix, Command Animal (Folk) (с. 63) | 5 ПМ; 1d4 Рассудка | справочник (Grand Grimoire): 1 ПМ; 1d3 | предложение-источник с пометкой |
| Spell Appendix, Cause Disease (с. 63) | 8+ ПМ, без потери Рассудка | справочник: 8+ ПМ, 1d4 Рассудка | предложение-источник с пометкой |
| Задание (эпоха) | «modern day» | книга: 1930 год (с. 34; гл. 1, с. 9) | эпоха `1920s` (как у ep3) |

## Термины (English → русский)

| English | Русский |
|---|---|
| A Time to Harvest | «Время жатвы» |
| Episode One / Episode 1 | эпизод 1 |
| Field Research | Полевые исследования |
| Harvest Papers N | раздатка «Жатва» N |
| Dream Gate | Врата сна |
| Waking World | мир яви |
| Dreamlands | Страна грёз |
| Enchanted Wood(s) | Зачарованный лес |
| Dylath-Leen | Дийлат-Лин |
| black galley | чёрная галера |
| moon-beast | лунный зверь |
| men of Leng / Lengites | люди Ленга / ленгиты |
| zoog(s) | зуг(и) |
| Mi-Go, standard form | ми-го, обычный облик |
| Fungi (mi-go) | Грибы |
| Sugar Maple forest | лес сахарных клёнов |
| The Clearing | поляна Джеффри |
| The Shack / The Cabin In The Woods | заброшенная лачуга / «Хижина в лесу» (сцена) |
| Root Cellar | погреб |
| The Old Maclearan Farmhouse | Старый дом Маклиранов |
| Outhouse | уборная |
| Charming Feature Flowerbed | клумба |
| Gismend River Bridge | мост через Гисменд |
| Broken Hill / Round Hill | Брокен-Хилл / Раунд-Хилл |
| Landin Mountain | гора Лэндин |
| Sarah’s Shade | Тень Сары |
| The Young (cult) / Mother | Младые (форма части world) / Мать |
| Jim’s Grill | закусочная Джима (форма world) |
| Brattleboro | Браттлборо (форма world) |
| Wilmington Realty | «Уилмингтон Риэлти» |
| spore gun | споровое ружьё (форма world) |
| Seize (mnvr) | Захват (манёвр) |
| Sacrificial dagger | жертвенный кинжал |
| Know roll / Know (EDU) roll | проверка Знаний / проверка Знаний (ОБР) |
| Hard Swim roll | трудная проверка Плавания |
| push (a roll) | повторная проверка |
| bonus die | бонусная кость |
| Dream Lore (skill) | Знание Страны грёз |
| Send Dream | Насылать сны |
| Make Cutting Remark | Язвительное замечание |
| Shy | Застенчивость |
| Quote Scripture | Цитирование Писания |
| Read Mi-Go | Чтение на языке ми-го |
| Art/Craft (Comedian / Singing / Dancing / Piano) | Искусство/ремесло (комик / пение / танцы / фортепиано) |
| Art/Craft (Photography / Uncover Dirty Secrets) | Искусство/ремесло (фотография / раскапывать грязные тайны) |
| Art/Craft (Brew Moonshine / Carpentry) | Искусство/ремесло (самогоноварение / плотницкое дело) |
| Lore (Witchery) | Тайные знания (колдовство) |
| Occult (Local Legends) | Оккультизм (местные легенды) |
| The Witch-Cult in Western Europe | «Культ ведьм в Западной Европе» |
| Mandragora Officinarum / Mandrake Root | мандрагора лекарственная / корень мандрагоры |

Имена: Robert Blaine — Роберт Блейн; Roger Harrold — Роджер Харролд; Clarissa Thurber — Кларисса Тёрбер; Jason Trent — Джейсон Трент;
Roderick “Little Rod” Block — Родерик «Малыш Род» Блок; Louis Gibbons — Луис Гиббонс; Harold (Harry) Higgins — Гарольд (Гарри) Хиггинс;
William Noakes — Уильям Ноукс; Terrence Laslow — Терренс Ласлоу; Joe Harlow — Джо Харлоу; John Jeffrey — Джон Джеффри;
Daphne Devine — Дафна Девайн; Agnus Bellweather — Агнус Беллуэзер; Beltane (кот) — Белтейн; Franklin Cobb — Франклин Кобб.

## Ссылки на записи других частей

- `time-to-harvest-1-en/scenario/a-time-to-harvest` (`part_of` эпизода) — запись части world по схеме (к концу работы уже есть).
- На записи world, которые уже есть, сцены и места ссылаются напрямую (`links.py`): шериф, помощник, Уэнделл, Хаггерти, Маклираны,
  Агнус Беллуэзер, Эмили Брейтуэйт, Каррутерс, Перри, Бойд Паттерсон; закусочная Джима, контора шерифа, памятник, пристани, Брокен-Хилл,
  Браттлборо, редакция газеты; карта игроков; споровое ружьё, мозговой цилиндр, врата ми-го; раздатка 2.
