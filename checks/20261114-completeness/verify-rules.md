# Сверка пробелов текста: книги правил (2026-11-14)

Проверены все находки `text.gap` из `findings.json` по книгам grand-grimoire-en, pulp-cthulhu-en, keeper-rulebook-ru,
keeper-rulebook-en, cthulhu-dark-ages-en (54 находки, все уровни уверенности). Страницы — физические. Находки, где на
страницах смешано разное, разбиты на несколько строк (64 строки).

Принято: английская «Книга хранителя» покрыта, если то же есть в базе по русской (keeper-rulebook-ru); английская
Cthulhu Dark Ages покрыта, если то же есть по фанатскому переводу `temnye-veka-tri-stsenariya-ru`.

**Итог по строкам:** покрыто (covered) — 22, частично (partly) — 3, нет в базе (missing) — 25, служебное (service) — 14.

| книга | стр. | что там | вердикт | записи / чего нет |
|---|---|---|---|---|
| pulp-cthulhu-en | 1, 3, 4, 6 | обложка, выходные данные (Credits), оглавление | service | — |
| pulp-cthulhu-en | 10–14 | глава 1 «The Pulps»: история пульп-журналов (Манси, Weird Tales, «геройские» пульпы, weird menace) — эссе без игровых чисел | missing | rule «Пульп-журналы» (гл. 1, с. 9–13), справочная статья; низкий приоритет. Прецедент — очерки гл. 8 (`coc:rule:pulp-culture`, `coc:rule:pulp-the-great-depression`) |
| pulp-cthulhu-en | 255–256 | гл. 15 «References»: цены 1930-х — «For your pocket», одежда мужская и женская, «Out and about», расследование, дом, транспорт (марки авто), еда, ресторан, путешествия, жильё | missing | table «Снаряжение и цены 1930-х» (с. 254–255); аналог для 1920-х есть — `coc:table:equipment-1920s-*` |
| pulp-cthulhu-en | 261–262 | гл. 15, списки оружия: пистолеты-пулемёты, пулемёты, взрывчатка и тяжёлое оружие; ключ к таблице | partly | оружие в базе по «Книге хранителя»: `coc:weapon:thompson-smg`, `coc:weapon:bergmann-mp18-mp28`, `coc:weapon:gatling-gun-1882`, `coc:weapon:browning-m1918-bar`, `coc:weapon:browning-m1917a1-30`, `coc:weapon:lewis-gun-mark-i`, `coc:weapon:molotov-cocktail`, `coc:weapon:flare-gun`, `coc:weapon:blasting-cap`, `coc:weapon:field-gun-75mm` и др.; ключ повторяет примечания таблицы XVII. Нет: цен 1930-х (`cost` знает только 1920s/modern), Beretta 1938A, Lewis Gun Mk VI |
| pulp-cthulhu-en | 263–264 | «References and Sources of Inspiration»: книги о 1930-х, пульп-литература, фильмы | missing | rule «Библиография Pulp Cthulhu»; низкий приоритет. Прецедент — `coc:rule:dark-ages-bibliography`, `coc:rule:arkham-bibliography`, `coc:rule:reign-bibliography` |
| pulp-cthulhu-en | 265–270 | алфавитный указатель (гл. 16) | service | — |
| pulp-cthulhu-en | 274 | задняя обложка | service | — |
| keeper-rulebook-ru | 2 | оглавление | service | — |
| keeper-rulebook-ru | 5–9 | алфавитный указатель | service | — |
| keeper-rulebook-ru | 11–17 | глава 1 «Введение»: что такое ролевая игра, Хранитель и игроки, пример игры, «Чему посвящена эта игра», рассказы Лавкрафта для начала, новое издание, что нужно для игры, игральные кости, как пользоваться d100, варианты бросков (2d6, 1d6+1, БкУ), лист сыщика, миниатюры и реквизит | missing | rule(s) «Введение в игру» / «Игральные кости и их обозначения» (с. 8–14 печ.). Есть лишь термины глоссария `coc:term:1d100`, `coc:term:1d4-1d6-1d8-1d10-etc` |
| keeper-rulebook-ru | 18–24 | глава 2 «Говард Лавкрафт»: биография, Мифы Ктулху (Дерлет, Хастур), Великие Древние, Внешние и Старшие боги, расы, фильмы | missing | rule «Говард Лавкрафт и Мифы Ктулху», справочная статья без игровых чисел; низкий приоритет |
| keeper-rulebook-ru | 51 | сводный «Список навыков» с базовыми значениями (с. 54 печ.) | covered | базовые значения — в записях `coc:skill:*` (54 записи по этой книге), `coc:rule:skill-definitions` |
| keeper-rulebook-ru | 255–259 | вступление к главе 14: «Параметры существ», таблица XV «Сравнение Комплекции», «Чудовища и сыщики: сравнение», «Краткие правила сравнения Комплекции», «Как лучше играть» чудовищ, бой, «Чудовища и манёвры», «Чудовища и контратаки», «Как убить чудовище», «Заклинания чудовищ», вступление «Чудовища Мифов» | missing | rule(s) «Чудовища: параметры, Комплекция и бой» + table «Таблица XV. Сравнение Комплекции» (с. 276–280 печ.); в базе только `coc:rule:monsters-in-a-chase` (о погоне) |
| keeper-rulebook-ru | 300 | продолжение Ктугхи (характеристики, бой, автоматическое сожжение) и Ниогты (культ) | covered | `coc:creature:cthugha`, `coc:creature:nyogtha` (цитируют только соседние страницы) |
| keeper-rulebook-ru | 318–319 | врезка «Вариант структуры Мифов Ктулху»: Внешние, Старшие и Иные боги, Великие Древние, народы служителей, независимые народы | missing | rule «Вариант структуры Мифов Ктулху» (с. 340–342 печ.) |
| keeper-rulebook-ru | 381–384, 386–389 | гл. 16 «Кратко о правилах»: проверки навыков, бонусные кости, бой, дистанционное оружие, схема боя, схема урона, погоня, таблица VI | service | краткий пересказ правил, которые есть: `coc:rule:bonus-and-penalty-dice`, правила боя и погони, `coc:rule:other-forms-of-damage` и др. |
| keeper-rulebook-ru | 391–393 | «Кратко о правилах»: рассудок, приступы (таблица VII), магия | service | пересказ правил рассудка и магии (`coc:rule:casting-spells` и др.) |
| keeper-rulebook-ru | 395 | «Мистические слова»: список «лавкрафтовских» прилагательных (шутка: прочитавший теряет 1d3 рассудка) | missing | rule/table «Мистические слова» (с. 419 печ.); низкий приоритет |
| keeper-rulebook-en | 5, 6, 8, 9 | благодарности, копирайт, предисловие, оглавление | service | — |
| keeper-rulebook-en | 13–20 | Chapter 1 «Introduction» (= RU 11–17) | missing | как RU 11–17: в базе нет ни по одному изданию |
| keeper-rulebook-en | 23–28 | Chapter 2 «H. P. Lovecraft and the Cthulhu Mythos» (= RU 18–24) | missing | как RU 18–24 |
| keeper-rulebook-en | 36 | лист сыщика, шаги 8–11, таблица БкУ и Комплекции | covered | `coc:rule:creating-your-investigator` («Памятка по созданию сыщика»), `coc:rule:other-attributes` |
| keeper-rulebook-en | 57–80 | Chapter 4: Skill List и описания навыков | covered | по RU: `coc:skill:*` (54), `coc:rule:skill-definitions`, `coc:rule:skill-specializations` |
| keeper-rulebook-en | 279–283 | вступление гл. 14: About the Entries, Monster Sizes, Table XV, Playing Monsters Effectively, Chaosium Pronunciations of Mythos Names, Monsters and Maneuvers, Fighting Back, Killing Monsters, Monster Spells | missing | как RU 255–259; таблица произношения имён Мифов в базе тоже отсутствует |
| keeper-rulebook-en | 284–328 | чудовища Мифов и божества (Byakhee … Tulzscha) | covered | по RU: `coc:creature:byakhee`, `coc:creature:chthonian-adult`, `coc:creature:colour-out-of-space`, … `coc:creature:shudde-mell`, `coc:creature:tsathoggua`, `coc:creature:tulzscha` |
| keeper-rulebook-en | 330–336 | Spawn of Ubbo-Sathla, Y'golonac, Yibb-Tstll, Yig, Yog-Sothoth, Zoth-Ommog; традиционные ужасы | covered | `coc:creature:spawn-of-ubbo-sathla`, `…ygolonac`, `…yibb-tstll`, `…yig`, `…yog-sothoth`, `…zoth-ommog`, `…ghost`, `…mummy`, `…skeleton`, `…vampire`, `…werewolf`, `…zombie` |
| keeper-rulebook-en | 339 | Horse, Rat Pack, Lion, Shark | covered | `coc:creature:horse`, `coc:creature:rat-swarm`, `coc:creature:lion-big-cat`, `coc:creature:shark` |
| keeper-rulebook-en | 341–343 | Wolf; Wasp and Bee Swarms; врезка «An Optional Structure for the Cthulhu Mythos» | missing | звери есть (`coc:creature:wolf`, `coc:creature:wasp-and-bee-swarm` по Malleus Monstrorum); нет врезки — как RU 318–319 |
| keeper-rulebook-en | 347–364 | сценарий «Amidst the Ancient Trees» | covered | `keeper-rulebook-ru/scenario/trees-amidst-the-ancient-trees` и его записи |
| keeper-rulebook-en | 387–390 | Appendix I: Glossary; начало Appendix II | covered | термины глоссария `coc:term:*` по RU (с. 384–387 печ.), `coc:rule:converting-investigators`, `coc:rule:converting-material-from-previous-editions` |
| keeper-rulebook-en | 407–421 | Summary of Game System Rules: примечания к таблице оружия, бонусные кости, ближний бой, огнестрел, схемы боя и урона, погоня, таблицы V–VII, рассудок, магия, таблица половин и пятых | service | краткий пересказ правил, которые есть в базе по RU |
| keeper-rulebook-en | 422 | Lovecraftian words | missing | как RU 395 |
| keeper-rulebook-en | 427–437 | плейтестеры, спонсоры Kickstarter | service | — |
| grand-grimoire-en | 3 | Credits | service | — |
| grand-grimoire-en | 6 | Introduction (Mike Mason, 2016) | service | — |
| grand-grimoire-en | 8–11 | гл. 1 «Concerning Magic»: настрой заклинателя, природа жертвоприношения, рабочее пространство, «Are the Stars Right?», дни недели и планеты, фазы луны, колесо года (праздники огня, солнцестояния), прочие астрономические факторы | missing | rule «О магии» + tables «Дни недели», «Фазы луны», «Колесо года» |
| grand-grimoire-en | 12–16 | гл. 2 «Concerning Spells» (начало): Deeper Magic, Spell Names, Difficulties in Spellcasting, Adjusting Spells, Folk Magic, Flawed Spells, Dreamlands Magic, Spirit Attacks and Possession, Spell Components, Magical Tools | partly | есть по «Книге хранителя»: `coc:rule:deeper-magic`, `coc:rule:spell-variations`; аналог одержимости — `coc:rule:dark-ages-system-spirit-attacks-and-possession`. Нет: имена заклинаний, трудности сотворения, народная магия, ущербные заклинания, магия Страны грёз, компоненты и магические инструменты, а также таблица 1 «Spell Components» (с. 17–18) |
| grand-grimoire-en | 19–22 | гл. 2 (окончание): Amulets, Talismans, Residual Magical Effects, Ley Lines, Fictional Magic | missing | rule(s) «Амулеты и талисманы», «Остаточные магические эффекты», «Лей-линии», «Вымышленная магия» |
| grand-grimoire-en | 23–26 | гл. 3 «Spell Categories»: списки заклинаний по 20 категориям, формат статьи, Call/Contact/Summon Disambiguation | partly | различие вызова, связи и призыва — `coc:rule:call-contact-and-summon-disambiguation`; формат статьи — служебное. Нет: категорий GG (у заклинаний своя классификация из 14 категорий `category`) |
| grand-grimoire-en | 44 | Bind Child of the Sphinx (окончание), Bind Shoggoth, Bind Were-Creature | missing | spells «Укрощение дитя Сфинкса» (с. 42–43 печ.), «Укрощение шоггота», «Укрощение оборотня» (с. 43) |
| grand-grimoire-en | 49 | врезка Human-Hybrid Tindalosian (профиль) | covered | `coc:creature:tindalosian-hybrids` (по Malleus Monstrorum); материнское заклинание Brew Elixir of Life (с. 47–48) в базе отсутствует |
| grand-grimoire-en | 55 | Call Aku-Shin Kage, Call Ahtu, Call Arwassa, Call Avatar of The Skinless One | missing | 4 spells (с. 54 печ.); упомянуты лишь в заметке `coc:spell:call-dismiss-nyarlathotep`; существа есть (`coc:creature:ahtu`, `coc:creature:arwassa`, `coc:creature:aku-shin-kage`, `coc:creature:skinless-one`) |
| grand-grimoire-en | 72 | врезка «Conjuration of the Turua»: пример сложного ритуала из четырёх заклинаний | missing | rule или spell «Призыв туруа» (с. 71 печ.) |
| grand-grimoire-en | 86 | врезка-пример: Хестия Локсби, ведьма из Данвича (профиль) | missing | character (с. 85 печ.) |
| grand-grimoire-en | 117 | Eyes of a Stranger, Fang of Yig, Feast of the Owl (Folk) | missing | 3 spells (с. 116 печ.) |
| grand-grimoire-en | 134 | врезка-пример: Томас Дэвенпорт, историк и некромант (профиль) | missing | character (с. 133 печ.) |
| grand-grimoire-en | 158 | окончание таблицы кошмаров Ravening Madness; Reach; Reanimation | missing | таблица есть в `coc:spell:ravening-madness`; нет spells «Reach» и «Reanimation» (с. 157 печ.) |
| grand-grimoire-en | 163 | Sacred Molting of the Serpent, Saaamaaa Ritual | missing | 2 spells (с. 162 печ.) |
| grand-grimoire-en | 186 | врезка-пример: Нильс-Вигго Шоу, архивист (профиль) | missing | character (с. 185 печ.) |
| grand-grimoire-en | 194 | «Fungus Timeline» — окончание заклинания Zymoticism (начало на с. 193) | missing | spell «Zymoticism» (с. 192–193 печ.) |
| grand-grimoire-en | 195–202 | указатель, биографии авторов, выходные данные | service | — |
| cthulhu-dark-ages-en | 4 | Credits | service | — |
| cthulhu-dark-ages-en | 7–31 | введение ко 2-му изданию; создание сыщика (шаги, жизненные события, занятия, предыстория, имена, бартер и имущество, половины и пятые), навыки, снаряжение и цены | covered | `coc:rule:dark-ages-setting-introduction`, `coc:rule:dark-ages-investigators-*` (23 записи), занятия `coc:occupation:*` (20), навыки (17), таблицы предыстории (6) — по RU |
| cthulhu-dark-ages-en | 35–41 | Where are the Magical Weapons?, Shields; Players Guide A–Z: Battle … Literacy, Magic (charms, grimoires) | covered | `coc:rule:dark-ages-investigators-magical-weapons`, `…-shields-and-armor`, `coc:rule:dark-ages-setting-a-z-*` (battles, castles, communication, community, darkness, devil, heresy, hierarchy, hostage-taking, humor, knights, literacy, loyalty, magic) |
| cthulhu-dark-ages-en | 43 | Religion (в т. ч. Corruption in the Church) | covered | `coc:rule:dark-ages-setting-a-z-religion` |
| cthulhu-dark-ages-en | 45–47 | Monastic Life (вступление в орден, должности), Saints, Rural … Wilderness, Time | covered | `coc:rule:dark-ages-setting-a-z-monastic-life`, `…-saints`, `…-rural`, `…-secrecy`, `…-serfdom`, `…-slavery`, `…-supernatural`, `…-suspicion`, `…-travel`, `…-theory-of-limited-good`, `…-wilderness`, `…-time` |
| cthulhu-dark-ages-en | 73–82 | Anglo-Saxon England: земля, погода, короли, бурги Уэссекса, королевства, социальная структура, произношение, имена и прозвища, люди и семья, фразы, грамотность, постройки, валюта и налоги, суды, преступления | covered | `coc:rule:dark-ages-setting-anglo-saxon-england`, `…-settlement-types`, `…-kings-and-kingdoms`, `…-social-structure`, `…-names`, `…-people`, `…-buildings`, `…-currency-and-taxes`, `…-court-cases`, `…-crime-and-punishment` и др. |
| cthulhu-dark-ages-en | 84–88 | увечья и казни, объявление вне закона, кровная месть; внешность; еда и земледелие; развлечения, загадки; путешествия; военное дело (фирд, стена щитов) | covered | `coc:rule:dark-ages-setting-crime-and-punishment`, `…-appearance`, `…-food-and-farming`, `…-entertainment`, `…-travel`, `…-warfare` |
| cthulhu-dark-ages-en | 90–93 | архиепископы, Old Ways (языческие боги, вирд), время и год, здоровье и лечение | covered | `coc:rule:dark-ages-setting-faith`, `…-old-ways`, `…-time-and-year`, `…-health-and-healing`, `coc:table:dark-ages-whos-who` |
| cthulhu-dark-ages-en | 95–99 | Gazetteer of Anglo-Saxon England (Кентербери … Йорк) | covered | `coc:rule:dark-ages-setting-geography` |
| cthulhu-dark-ages-en | 108–119 | The Cthulhu Mythos in the Dark Ages, Here Be Mythos (места), Here Be Trouble (культы), Here Be Dragons (божества), Books of the Mythos | covered | `coc:rule:dark-ages-mythos-cthulhu-mythos-in-the-dark-ages`, `…-here-be-mythos`, `…-here-be-trouble`, `…-here-be-dragons`, `…-mythos-tomes` |
| cthulhu-dark-ages-en | 122–153 | книги Мифов и оккультные книги; Dark Ages Grimoire (народная и ритуальная магия, заклинания); Bestiary (чудовища Мифов, фольклора, животные) | covered | 29 записей `tome`, 34 `spell`, `coc:rule:dark-ages-mythos-magic-of-the-dark-ages`, `…-ritual-magic`, `…-grimoire`, `…-bestiary`, существа по RU (Cold One … Wolf) |
| cthulhu-dark-ages-en | 178–181 | сценарий «The Hunt» (завязка, предыстория, ферма, Тотбург) | covered | `temnye-veka-tri-stsenariya-ru/scenario/hunt-the-hunt` и его записи |
| cthulhu-dark-ages-en | 183–203 | «The Hunt» (окончание), «The Doom that Came to Wessex», «Eseweald» с приложениями | covered | `…/scenario/hunt-the-hunt`, `…/scenario/wessex-doom-that-came-to-wessex`, `…/scenario/esewald-eseweald` |

## Нет в базе (missing)

1. **Pulp Cthulhu, с. 10–14** — глава 1 «The Pulps» (очерк истории пульп-журналов): rule; низкий приоритет.
2. **Pulp Cthulhu, с. 255–256** — цены 1930-х (одежда, снаряжение, дом, транспорт, еда, путешествия, жильё): table.
3. **Pulp Cthulhu, с. 263–264** — «References and Sources of Inspiration»: rule-библиография; низкий приоритет.
4. **«Книга хранителя», RU 11–17 / EN 13–20** — глава 1 «Введение» (обзор, пример игры, что нужно, кости и чтение d100, варианты бросков, лист сыщика).
5. **«Книга хранителя», RU 18–24 / EN 23–28** — глава 2 «Говард Лавкрафт и Мифы Ктулху»: справочная статья; низкий приоритет.
6. **«Книга хранителя», RU 255–259 / EN 279–283** — вступление к главе 14: параметры существ, таблица XV «Сравнение Комплекции», чудовища в бою, манёвры, контратаки, как убить чудовище, заклинания чудовищ, произношение имён Мифов (EN 281).
7. **«Книга хранителя», RU 318–319 / EN 341–343** — врезка «Вариант структуры Мифов Ктулху».
8. **«Книга хранителя», RU 395 / EN 422** — «Мистические слова»; низкий приоритет.
9. **Grand Grimoire, с. 8–11** — глава 1 «Concerning Magic» с таблицами дней недели, фаз луны, колеса года.
10. **Grand Grimoire, с. 19–22** — амулеты, талисманы, остаточные магические эффекты, лей-линии, вымышленная магия.
11. **Grand Grimoire, заклинания (15)**: Bind Child of the Sphinx, Bind Shoggoth, Bind Were-Creature (с. 43–44); Call Aku-Shin Kage, Call Ahtu, Call Arwassa, Call Avatar of The Skinless One (с. 54–55); Eyes of a Stranger, Fang of Yig, Feast of the Owl (Folk) (с. 117); Reach, Reanimation (с. 158); Sacred Molting of the Serpent, Saaamaaa Ritual (с. 163); Zymoticism (с. 193–194).
12. **Grand Grimoire, с. 72** — врезка «Conjuration of the Turua» (пример ритуала из четырёх заклинаний).
13. **Grand Grimoire, с. 86, 134, 186** — врезки-примеры колдунов: Хестия Локсби, Томас Дэвенпорт, Нильс-Вигго Шоу (character).

## Частично (partly)

1. **Pulp Cthulhu, с. 261–262** (и списки с. 257–260 той же главы) — оружие есть по «Книге хранителя», но нет цен 1930-х и отдельных образцов (Beretta 1938A, Lewis Gun Mk VI).
2. **Grand Grimoire, с. 12–16** — есть только усиленная магия и вариации заклинаний по «Книге хранителя»; нет имён заклинаний, трудностей сотворения, народной магии, ущербных заклинаний, магии Страны грёз, нападений духов и одержимости (в версии GG), компонентов, магических инструментов и таблицы 1 «Spell Components» (с. 17–18).
3. **Grand Grimoire, с. 23–26** — различие вызова, связи и призыва есть по «Книге хранителя»; категорий GG нет (у заклинаний своя классификация).

## Замечание вне задания

По решению Р-51 Grand Grimoire переносился не целиком: брались заклинания веб-помощника, заклинания из карт существ и персонажей, остальное — по необходимости. Поэтому находки `text.gap` показывают только страницы, где не процитировано ни одного заклинания. Беглая сверка названий по соседним, уже процитированным страницам тоже не находит в `kb/spells/` ряд заклинаний. Это Brew Elixir of Life, Brew Liao Drug, Black Box, Koshchey's Death, Raise Night Fog, Removal of Favor, Reincarnate, Create Fetch Stick, Final Feast, Fire Dance, Lambent Flame, Reversed Angles of Tagh-Clatur, Return Servitor, Seal Pit, Voice Thoughts, Vortex of Far Journeying, The Waking Slumber и др. Сверка шла по английским названиям, поэтому часть из них может быть заведена под другим именем. Полноту Grand Grimoire стоит проверить отдельно, по списку заклинаний из указателя (с. 195–200).
