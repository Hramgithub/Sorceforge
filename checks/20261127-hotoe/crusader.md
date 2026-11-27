# HOTOE — часть crusader: «The Dark Crusader: Constantinople 1204» («Тёмный крестоносец»)

Книга `hotoe-book-3-en` (Book III: Italy & Beyond), печатные страницы 43–80 и 246–250 (печатная = физическая − 2);
копии для игроков — `hotoe-book-6-handouts-en` с. 97 (раздатки), 137, 139, 141, 143 (карты); Keeper Maps, лист 16;
Player Maps, лист 11. Русского издания нет — русский текст наш перевод (флаг `translated`, Р-251). Эпоха — `dark-ages`.
Префикс id ниже опущен: `hotoe-book-3-en/`. Скрипты — `.cache/lead-tools/gen-hotoe-crusader/` (`gen_all.py` — записи,
`gen_props.py` — предложения; после применения картинок `gen_all.py` повторно не запускать — он перезапишет `images`).

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Dark Crusader (титул: «In which Frankish knights…», by Geoff Gillan) | 43 | `scenario/the-dark-crusader` (summary) |
| Keeper's Information | 43 | `scenario/the-dark-crusader` (keeper_info) |
| It Is Written | 43 | `scenario/the-dark-crusader` (keeper_info «Так написано») |
| This Historical Scenario is Optional (врезка) | 43 | `scenario/the-dark-crusader` (advice) |
| About the Investigators; A Note on Terms | 43–44 | `scenario/the-dark-crusader` (hook) |
| Карта Constantinople at the Time of the Fourth Crusade | 44 | `map/crusader-constantinople-1204` |
| The Fourth Crusade and the Sack of Constantinople | 44–46 | `scenario/the-dark-crusader` (advice «Исторический фон») |
| Using This Scenario with the 1923 Campaign | 45 | `scenario/the-dark-crusader` (hook) |
| Handouts for 1920s Investigators | 45 | `scenario/the-dark-crusader` (hook, steps[0]) |
| The Devil's Simulare: Introductory Handout | 45 | `handout/crusader-handout-devils-simulare-introductory` (+ Book VI с. 97) |
| The Devil's Simulare: Summary Handout | 46 | `handout/crusader-handout-devils-simulare-summary` (+ Book VI с. 97) |
| Constantinople 1204: Core Groups (The Venetians; The Franks (Boniface); The Franks (Baldwin); European Residents; Byzantines; Off Stage: Pope Innocent III) | 47–48 | `scenario/the-dark-crusader` (таблица «Константинополь 1204: основные силы»); `character/enrico-dandolo`, `character/boniface-of-montferrat`, `character/baldwin-of-flanders`, `character/henry-of-flanders`; предложение абзаца 1204 года `coc:location:constantinople` |
| Timeline of the Fourth Crusade (врезка) | 47 | `scenario/the-dark-crusader` (таблица «Хронология Четвёртого крестового похода») |
| Key City Locations: Hagia Sophia; Boukeleon Palace or Great Palace Complex; The Hippodrome; Golden Gate | 48 | Святая София и Золотые ворота — `wwc-cold-war-en/location/haghia-sophia`, `…/golden-gate` (абзацы 1204 года — предложениями); `location/crusader-boukeleon-palace`, `location/crusader-hippodrome` |
| Keeper's Background | 49 | `scenario/the-dark-crusader` (keeper_info «Предыстория») |
| Prologue: Storming the Walls; Tactics of Battle; Placing Investigators (Towers, Lower Wall, Horse Transports) | 49–51 | `scene/crusader-prologue-storming-the-walls`; `location/crusader-city-walls` |
| Further Reading (врезка) | 50 | `scenario/the-dark-crusader` (advice «Что почитать») |
| Additional Thanks (врезка) | 50 | авторы прегенов — в `quality.notes` прегенов; в остальном «Не взято» |
| Investigator's Introduction; A Summons | 51 | `scene/crusader-summons` |
| Blachernae Palace (врезка с портретом графа Балдуина) | 51 | `location/crusader-blachernae-palace`; `character/baldwin-of-flanders` (портрет) |
| A Note on Combat (врезка: Morale, Limit Enemies) | 52 | `scenario/the-dark-crusader` (advice «О бое»); `scene/crusader-varangian-attack`, `scene/crusader-ruined-church` (mechanics) |
| Count Baldwin's Mission; Seeking the Priest; A Final Request | 52 | `scene/crusader-summons` |
| Crossing the City; Checkpoints; Experiencing the Sack (типичные встречи) | 53 | `scene/crusader-crossing-the-city`; таблица этапа «Через город: типичные встречи» |
| Varangian Attack; After the Cistern | 53–54 | `scene/crusader-varangian-attack`; `location/crusader-cistern-of-aetius`, `location/crusader-cistern-of-aspar`; `character/typical-varangian-guard` |
| The Forum of Theodosius: Forum and Basilica; Four Guardian Knights | 54 | `scene/crusader-one-eyed-priest`; `location/crusader-forum-of-theodosius`, `location/crusader-northern-basilica` |
| The One-Eyed Priest (портрет) | 54 | `character/padre-agostino` (портрет) |
| The Cursed Eye (врезка) | 55 | `scene/crusader-one-eyed-priest` (mechanics); предложение к `coc:spell:accursed-eye` (quality.notes) |
| The Priest's Tale | 55–56 | `scene/crusader-one-eyed-priest`; `character/padre-agostino` |
| Plans and Reinforcements | 56 | `scene/crusader-plans-and-reinforcements` |
| Seeking Ramardi: Church of Christ Pantocrator (Christ the Almighty); Meeting Ramardi | 56–57 | `scene/crusader-seeking-ramardi`; `location/crusader-church-of-christ-pantocrator`; `character/ramardi` |
| The Leper Ship: About Leprosy; The Ship | 57–58 | `location/crusader-leper-ship-pestis` (корабль, `part_of: null`); `scene/crusader-leper-ship` |
| Relics of Constantinople (врезка) | 58 | `scenario/the-dark-crusader` (таблица «Реликвии Константинополя») |
| The Monk; The Unburdened Flesh; Sedefkar; The Skinless One; The Simulare; The Ritual; Further Assistance; Merovac's True Nature | 58–59 | `scene/crusader-leper-ship`; `organization/crusader-unburdened-flesh`; `coc:character:fenalik` (предложение: абзац 1204 года, псевдонимы «Брат Меровак») |
| The Church of St. Mokius: The Hill of the Dragon; A Drunken Rabble | 59–60 | `scene/crusader-drunken-rabble`; `location/crusader-seventh-hill` |
| The Frightened Family | 60 | `scene/crusader-frightened-family` |
| Карта Church of St. Mokius | 60 | `map/crusader-st-mokius-church` |
| The Ruined Church; Inside the Church; Ramardi Arrives | 60–62 | `scene/crusader-ruined-church`; `location/crusader-church-of-st-mokius`; `character/zorzi` |
| The Hidden Package | 62–63 | `item/crusader-hidden-package`, `item/crusader-ritual-of-detect-skinless-one`, `item/crusader-skin-of-the-skinless-one` |
| Карта Cistern of St. Mokius | 62 | `map/crusader-st-mokius-cistern` |
| Sedefkar's Plan (врезка) | 63 | `scenario/the-dark-crusader` (keeper_info «План Седефкара»); `character/sedefkar` (legend) |
| Escape from the Church (Negotiation, Fighting it out, Escape through the crypt) | 63 | `scene/crusader-escape-from-the-church` |
| The Crypt and the Tunnel | 63–64 | `scene/crusader-crypt-and-tunnel`; `location/crusader-st-mokius-crypt` |
| The Dragon in the Cistern: The Cistern; The Anatolian Dragon; Engaging the Dragon | 64–65 | `scene/crusader-dragon-in-the-cistern`; `location/crusader-st-mokius-cistern`; `creature/crusader-anatolian-dragon` |
| The Way Back | 65 | `scene/crusader-the-way-back` |
| The Ritual of The Skinless One: Casting the Ritual (Critical, Success, Failure, Fumble) | 65–66 | `scene/crusader-ritual-of-the-skinless-one`; `coc:spell:detect-skinless-one` (новая общая запись) |
| What if the Investigators Do Not Deliver the Simulacrum? (врезка) | 66 | `scenario/the-dark-crusader` (keeper_info); `character/miho-of-dubrovnik` |
| What if the Investigators Fail? (врезка) | 66 | `scenario/the-dark-crusader` (conclusion) |
| Locating the Red Tower | 66–67 | `scene/crusader-ritual-of-the-skinless-one`; `location/crusader-red-tower` |
| Attack of the Skin Devils | 67 | `scene/crusader-attack-of-the-skin-devils`; `creature/crusader-skin-devil` (рисунок) |
| The Blood Red Tower: Boniface's Men | 67 | `scene/crusader-bonifaces-men` |
| Sir Gautmaris; The Simulare; Sedefkar Attacks | 67–68 | `scene/crusader-sir-gautmaris`; `character/sir-gautmaris` |
| Карта The Red Tower | 68 | `map/crusader-red-tower` |
| Within the Tower; Floor One … Floor Seven | 68–69 | `scene/crusader-within-the-tower`; `location/crusader-red-tower`, `location/crusader-red-tower-floor-1` … `-7` |
| Sedefkar's Altar (рисунок) | 69 | `location/crusader-red-tower-floor-7` (картинка) |
| Fight with Sedefkar; Location Chart | 69–70 | `scene/crusader-fight-with-sedefkar`; таблица этапа «Попадание по частям тела» (строки ведут на шесть частей симулякра части campaign) |
| The Skinless One Comes; Sedefkar Defeated | 70 | `scene/crusader-fight-with-sedefkar` |
| Leaving the Tower | 70 | `scene/crusader-leaving-the-tower` |
| Aftermath: The Count's Reward | 70–71 | `scene/crusader-counts-reward`; `scenario/the-dark-crusader` (conclusion: 1d10 Рассудка) |
| The Fate of the Mims Sahis; The Fate of the Sedefkar Simulacrum; The Fate of the Investigators | 71 | `scene/crusader-counts-reward`; предложения к `hotoe-book-1-en/item/campaign-mims-sahis` и `organization/vinkovci-order-of-the-noble-shield` |
| Historical Aftermath | 71 | `scenario/the-dark-crusader` (conclusion «Исторические последствия») |
| Statistics: Typical Frankish Man-at-Arms; Typical Frankish Knight | 72 | `character/typical-frankish-man-at-arms`, `character/typical-frankish-knight` |
| Bledic, Frankish Minstrel and Guide | 72 | `character/bledic` |
| Typical Greek Citizen (с рисунком) | 72–73 | `character/typical-greek-citizen` (рисунок) |
| Typical Venetian Sailor-Warrior; Typical Varangian Guard | 73 | `character/typical-venetian-sailor-warrior`, `character/typical-varangian-guard` |
| Cultist of the Unburdened Flesh | 73–74 | `character/cultist-of-the-unburdened-flesh` |
| New Spells: Skinless Stigmata; Accursed Eye | 73 | `coc:spell:skinless-stigmata` (новая общая запись); «Проклятое око» уже есть (`coc:spell:accursed-eye`, Grand Grimoire) — источник и расхождения предложением |
| Zorzi, High Priest of the Unburdened Flesh | 74 | `character/zorzi` |
| Captain Ramardi, Leader of the Cult of the Unburdened Flesh | 74 | `character/ramardi` |
| Sedefkar, Ageless sorcerer and owner of the simulacrum (Mims Sahis, Screaming Cut, Armor) | 74–75 | `character/sedefkar` (фиксированный id) |
| New Spells: Burden of The Skinless One; Create Skin Devil; Skin of The Skinless One | 75 | «Бремя Бескожего» уже есть (`coc:spell:burden-of-the-skinless-one`, GG; источник — предложением); `coc:spell:create-skin-devil`, `coc:spell:skin-of-the-skinless-one` (новые общие записи) |
| Creatures and Monsters: Skin Devils, Noisome Protégés of Sedefkar | 75–76 | `creature/crusader-skin-devil` |
| The Anatolian Dragon, Unique Magical Creature | 76 | `creature/crusader-anatolian-dragon` (рисунок со с. 64) |
| Investigators: Gilles de la Grave | 76–77 | `character/gilles-de-la-grave` (pregen) |
| Brother David | 77 | `character/brother-david` (pregen) |
| Andre of Troyes | 77–78 | `character/andre-of-troyes` (pregen) |
| Renaud of Flanders | 78–79 | `character/renaud-of-flanders` (pregen) |
| Martinus de l'Isles | 79 | `character/martinus-de-lisles` (pregen) |
| Eloise of Flanders | 79–80 | `character/eloise-of-flanders` (pregen); `character/marie-de-champagne` |
| Constantinople Dark Ages Keeper's Map | 246 | `map/crusader-constantinople-1204` (картинка — Keeper Maps, лист 16) |
| Constantinople Dark Ages Keeper's Map [так в книге; на деле карта игроков] | 247 | `map/crusader-constantinople-1204-players` (картинка — Player Maps, лист 11) |
| Church of St. Mokius | 248 | `map/crusader-st-mokius-church` |
| Cistern of St. Mokius | 249 | `map/crusader-st-mokius-cistern` |
| The Red Tower | 250 | `map/crusader-red-tower` |

Места с номерами карты Константинополя 1204 (Reference 1–13): 1 `location/crusader-boukeleon-palace`, 2 `…/crusader-blachernae-palace`,
3 `…/crusader-church-of-christ-pantocrator`, 4 `wwc-cold-war-en/location/haghia-sophia`, 5 `wwc-cold-war-en/location/golden-gate`,
6 `…/crusader-hippodrome`, 7 `…/crusader-cistern-of-aetius`, 8 `…/crusader-cistern-of-aspar`, 9 `…/crusader-basilica-cistern`,
10 `…/crusader-forum-of-theodosius`, 11 `…/crusader-church-of-st-mokius`, 12 `…/crusader-red-tower`, 13 `…/crusader-leper-ship-pestis`.
Подписи карты: Golden Horn, Bosphorus, Straight of St. George, Pera, Chrysopolis, Chalcedon — общие места Стамбула WWC
(Р-254: одна запись на все эпохи; старые имена — предложениями в `aliases`); стены — `location/crusader-city-walls`.

## Записи (88 файлов)

- Сценарий: `scenario/the-dark-crusader` (этап 9, `part_of` кампании, 14 шагов, 5 таблиц).
- Сцены (23): `scene/crusader-…` — prologue-storming-the-walls, summons, crossing-the-city, varangian-attack, one-eyed-priest,
  plans-and-reinforcements, seeking-ramardi, leper-ship, drunken-rabble, frightened-family, ruined-church,
  escape-from-the-church, crypt-and-tunnel, dragon-in-the-cistern, the-way-back, ritual-of-the-skinless-one,
  attack-of-the-skin-devils, bonifaces-men, sir-gautmaris, within-the-tower, fight-with-sedefkar, leaving-the-tower, counts-reward.
- Персонажи (24): Седефкар, Дзордзи, Рамарди, Бледик; типажи — франкский латник, франкский рыцарь, горожанин-грек,
  венецианский моряк-воин, варяг-гвардеец, культист Освобождённой плоти (имена придуманы, Р-151); без статблоков — граф
  Балдуин, Генрих Фландрский, Бонифаций Монферратский, Энрико Дандоло, падре Агостино, сэр Готмарис, Мария Шампанская,
  сэр Михо Дубровницкий; прегены — Жиль де ла Грав, брат Давид, Андре из Труа, Рено Фландрский, Мартинус де Лиль, Элоиза Фландрская.
- Места (23): 15 мест Константинополя 1204 + 7 этажей Красной башни + корабль «Пестис» (`корабль`).
- Карты (5), существа (2: кожаный дьявол, Анатолийский дракон), предметы (3), организация (1: Освобождённая плоть),
  раздатки (2), новые общие заклинания (4): `coc:spell:skinless-stigmata`, `create-skin-devil`, `skin-of-the-skinless-one`,
  `detect-skinless-one`.
- Картинки (10, `art-crusader.json` → `art-crusader-proposals.json`, применены к своим записям): портреты Балдуина,
  Агостино, Рамарди, горожан-греков; рисунки дракона и кожаного дьявола; корабль прокажённых; алтарь Седефкара; две раздатки
  (Book VI, с. 97). Атмосферные иллюстрации — `atmosphere-crusader.json`.

## Предложения — `proposals-crusader.json` (63)

`coc:location:constantinople` (абзац 1204 года в `history`, источники, ссылки на этап и карты); `wwc-cold-war-en/location/`
`haghia-sophia`, `golden-gate`, `golden-horn` (абзацы 1204 года в `history`, источники); `beyoglu` (Пера), `uskudar`
(Хрисополь), `kadikoy` (Халкидон), `bosphorus` (пролив Святого Георгия) — старые имена; `coc:character:fenalik` (псевдонимы
«Брат Меровак», абзац 1204 года в `legend`, источники); `coc:spell:accursed-eye` (источник HOTOE и расхождения с GG в
`quality.notes`); `coc:spell:burden-of-the-skinless-one` (источник HOTOE, числа совпадают); `coc:creature:skinless-one`,
`coc:item:sedefkar-simulacrum` (источники 1204); `coc:organization:brothers-of-the-skin` (ссылка на Красную башню);
`hotoe-book-1-en/item/campaign-mims-sahis` (псевдоним «Коготь змея», правила 1204 года в `mechanics`, источники);
`organization/vinkovci-order-of-the-noble-shield` (источник с. 71, ссылки на Михо, Балдуина, этап). Пробный прогон
`apply.py --dry-run`: ложится целиком (одна правка — «уже было»).

## Опечатки и сомнения

- Хронология (с. 47): «DECEMBER 1204: Envoys arrive from Prince Alexius» — по порядку и тексту с. 45 декабрь 1202 (в `errata` этапа, как напечатано).
- Бонифаций — «Marquis Boniface of Montserrat» (с. 47; в хронологии — Montferrat): в `quality.notes` персонажа.
- Карта с. 44/246: «Basilico Cistern» (Basilica), «Straight of St. George» (Strait) — в пометках меток/мест.
- С. 247 подписана «Constantinople Dark Ages Keeper's Map», но это карта игроков (без мест 11–13; в Book VI, с. 137 — «Players' Map»).
- Венецианский моряк-воин: ПЗ 11 при (70+50)/10 = 12 — `errata`.
- Культист Освобождённой плоти: БкУ 0 и Комплекция 0 при СИЛ+ТЕЛ = 130 (+1d4, 1) — `errata`.
- Анатолийский дракон: БкУ +3d6 и Комплекция 4 при СИЛ+ТЕЛ = 350 (+4d6, 5) — `errata`, как напечатано, вопрос владельцу (Р-36).
- Рено Фландрский: Уклонение 48% (24/10) → пятая 9 — исправлено (`errata`, `fixed: true`).
- Жиль де ла Грав: у щита «75% (blocks attacks, 25 hp)» без половины и пятой — посчитаны (37/15), пометка.
- Татуировка культа: «left bicep» (с. 55) и «upper arm» (статблоки) — пометка у организации.
- Сценарий Винковци в тексте главы назван «Bread or Stone» (в оглавлении и id — «Bread and Stone»).
- «Ритуал обнаружения Бескожего» не входит в «New Spells», затраты ПМ и время не названы — общая запись заклинания с пометкой.
- «Проклятое око» (Accursed Eye): вариант HOTOE отличается от Grand Grimoire (глаз убивает жертву) — расхождения предложением в `quality.notes` заклинания.

## Не взято

- Additional Thanks (с. 50): имена тестеров — только как авторы прегенов в `quality.notes` прегенов (кредиты, без игрового содержания).
- Further Reading: ссылки на книги и сайты пересказаны в `advice`, отдельных записей нет (библиография без механики).
- Исторические лица, упомянутые мимоходом (Алексей III, IV, V/Мурзуфл, Тибо Шампанский, Филипп Швабский, папа Иннокентий III,
  Андре/Эндрю д'Юребуаз, Алеом из Клари, Пьер Амьенский, епископ Мартин, Гунтер Пэрисский, Никита Хониат, Виллардуэн,
  Бернадус, Юбер де ла Грав) — без записей: текст в сценарии, сценах и легендах (Р-30, Р-42).
- Безымянные греческий колдун, франкские священники и пьяная проститутка (с. 59–60) — без записей, только в сцене.
- Форум Аркадия, Меса, монастырь Пантепопта, ворота Петрион, Европейские кварталы — упоминаются текстом в местах и сценах, своих записей нет.
- Отдельные карты игроков для церкви, цистерны и Красной башни не заведены: копии в Book VI (с. 139, 141, 143) — те же карты
  (церковь даже с подписью «Hidden package»); Book VI указана источником карт.
- Фоновые текстуры врезок (с. 47, 50, 75 и др.) и бледный рисунок дракона в колонтитулах — оформление, не картинки.
- Атмосферные иллюстрации (с. 43, 49, 51, 52, 55, 61, 71, 78, 80) — в `atmosphere-crusader.json`.

## Ссылки на записи других частей

- `hotoe-book-4-en/scenario/the-fog-lifts` (часть return; фиксированный id) — пока не существует: 2 ошибки ссылки в сценах
  `crusader-fight-with-sedefkar`, `crusader-ritual-of-the-skinless-one` ожидаемы до сведения.
- Используются уже созданные записи других частей: `hotoe-book-1-en/scenario/horror-on-the-orient-express`, шесть частей
  симулякра `hotoe-book-1-en/item/campaign-simulacrum-*`, `campaign-mims-sahis`, `campaign-sedefkar-scrolls`;
  `item/venice-devils-simulare`, `location/venice-biblioteca-marciana`, `scenario/death-and-love-in-a-gondola` (venice);
  `organization/vinkovci-order-of-the-noble-shield`, `scenario/bread-and-stone` (zagreb-vinkovci); `scenario/sanguis-omnia-vincet`.
- Заклинания «Contact Skinless One» и «Turn To Skin» (список Седефкара) описаны в Book IV, с. 64 (часть constantinople): в
  `statblock.spells.items` Седефкара без ссылки — поставить при сведении.
- «Отверженная мечеть» 1923 года (часть constantinople) — упомянута текстом у Красной башни; связь — при сведении.

## Термины (английский → русский)

| English | Русский |
|---|---|
| The Dark Crusader | Тёмный крестоносец |
| The Devil's Simulare | «Дьявольское подобие» (форма части venice) |
| Simulare (доспех) | Подобие |
| Sedefkar Simulacrum / simulacrum | симулякр Седефкара / симулякр (глоссарий) |
| Mims Sahis / Serpent's Claw | Мимс Сахис / «Коготь змея» |
| Sedefkar Scrolls | Свитки Седефкара |
| The Skinless One | Бескожий (глоссарий) |
| The Unburdened Flesh | Освобождённая плоть |
| Skin Devil | кожаный дьявол |
| The Anatolian Dragon | Анатолийский дракон |
| Skinless Stigmata | Стигматы Бескожего |
| Detect Skinless One / Ritual of Detect Skinless One | Обнаружение Бескожего / Ритуал обнаружения Бескожего |
| Skin of The Skinless One | Кожа Бескожего |
| Create Skin Devil | Создание кожаного дьявола |
| Accursed Eye | Проклятое око (существующая запись) |
| Burden of The Skinless One | Бремя Бескожего (существующая запись) |
| Screaming Cut | Кричащий порез |
| Baleful Influence | Зловещее влияние |
| The (Blood) Red Tower | Красная (Кроваво-красная) башня |
| Shunned Mosque | Отверженная мечеть |
| The Leper Ship (Pestis) / leper monk | корабль прокажённых «Пестис» / прокажённый монах |
| Brother Merovac | брат Меровак |
| Fourth Crusade / Sack of Constantinople / Latin Empire | Четвёртый крестовый поход / разграбление Константинополя / Латинская империя |
| Franks / Venetians / Varangians / Byzantines (Greeks) | франки / венецианцы / варяги / византийцы (греки) |
| man-at-arms / knight / sailor-warrior / Varangian guard | латник / рыцарь / моряк-воин / варяг-гвардеец |
| Doge | дож |
| Blachernae Palace | Влахернский дворец |
| Boukeleon Palace (Great Palace) | дворец Буколеон (Большой дворец) |
| Church of Christ Pantocrator | церковь Христа Пантократора |
| Hagia Sophia | Святая София (существующая запись) |
| Hippodrome | Ипподром |
| Golden Gate / Golden Horn / Bosphorus | Золотые ворота / Золотой Рог / Босфор (существующие записи) |
| Straight of St. George | пролив Святого Георгия |
| Pera / Chrysopolis / Chalcedon | Пера / Хрисополь / Халкидон |
| Cistern of Aetius / of Aspar / Basilica Cistern | цистерна Аэция / цистерна Аспара / Цистерна Базилика |
| Forum of Theodosius (Forum of the Bull) | форум Феодосия (форум Быка) |
| Forum of Arcadius / Mese / Petrion Gate | форум Аркадия / Меса / ворота Петрион |
| Church of St. Mokius / Seventh Hill / Hill of the Dragon | церковь Святого Мокия / Седьмой холм / Холм дракона |
| Order of the Noble Shield | Орден Благородного Щита (форма части zagreb-vinkovci) |
| Count Baldwin of Flanders / Henry of Flanders | граф Балдуин Фландрский / Генрих Фландрский |
| Marquis Boniface of Montferrat | маркиз Бонифаций Монферратский |
| Enrico Dandolo | Энрико Дандоло |
| Marie de Champagne | Мария Шампанская |
| Bledic / Padre Agostino / Ramardi / Zorzi / Sir Gautmaris / Sir Miho of Dubrovnik | Бледик / падре Агостино / Рамарди / Дзордзи / сэр Готмарис / сэр Михо Дубровницкий |
| Gilles de la Grave / Brother David / Andre of Troyes / Renaud of Flanders / Martinus de l'Isles / Eloise of Flanders | Жиль де ла Грав / брат Давид / Андре из Труа / Рено Фландрский / Мартинус де Лиль / Элоиза Фландрская |
| Other Kingdoms | Другие королевства (навык, глоссарий) |
| Forage / Stand Watch / Skin Human / Cult teachings | Добыча пропитания / Нести дозор / Свежевание людей / Учение культа (навыки без записей) |
| Potions / Astrology / Natural History / Folklore / Linguist / Pick Pocket / Treat Poison | Зелья / Астрология / Естественная история / Фольклор / Лингвист / Карманная кража / Лечение ядов |
| Suck / Bowel Flail / Terrify | Сосание / Удар кишкой / Устрашение |
| Invisible Flight / Fire Breath | Невидимый полёт / Огненное дыхание |
| Location Chart | Попадание по частям тела |
| Core Groups | основные силы |
| Mass of Separation | Месса отлучения |
