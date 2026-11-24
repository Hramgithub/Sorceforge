# In Strange Seas: Horror in the Royal Navy for Regency Cthulhu — покрытие (часть «seas»)

Книга `in-strange-seas-en` (Evan Perlman, Chaosium Community Content, 2023; 31 с.). Это не сценарий, а дополнение
правил и сеттинга к Regency Cthulhu (навык `kb-rules-book`): записи вида `rule` книги, раздатка, место-корабль,
организация, персонаж. Сценарий «Wonders in the Deep» — отдельный файл набора, в библиотеке его нет.

Страницы: печатная = физической (смещение 0) на всех страницах с номером (2–31, номер стоит и на с. 14 и 27–31);
обложка (физ. 1) без номера. Русского перевода в базе и в библиотеке нет. Ось эпохи — `other` (Регентство, 1811–1820),
свод — `core`.

## Записи (44 в `kb/books/in-strange-seas-en/`)

- `rule` — 34 (дерево по `parent`: «Жизнь на флоте Его Величества» → 11 подразделов; «Сыщик на флоте» → 6 шагов;
  «Морской бой» → памятка; «Советы Хранителю» → 4 (+1 под «Репутацией»); приложения и «Зацепки Мифов» — верхнего уровня).
- `location` — 6: фрегат «Калибан» (`корабль`) и 5 палуб/частей под ним.
- `organization` — 1: клуб «Кракен» (в Лондоне, `coc:location:london`).
- `character` — 1: адмирал Плимптон.
- `handout` — 2: вербовочный плакат; «Кулинария для Королевского флота» (5 рецептов).
- Картинки: 5 (`app/art/handouts/seas-*`, `app/art/organizations/seas-kraken-club.webp`), применены
  (`art.json` → `art-proposals.json`); атмосфера — 12 страниц в `atmosphere.json`.
- Черновики общих записей (не в `kb/`): 11 профессий `coc:occupation:regency-navy-*` и навык `coc:skill:sail` —
  `new-shared/` (проверены схемой и ссылками). По `docs/conventions.md` §1 профессии и навыки — только общий справочник,
  поэтому помощник их в `kb/` не кладёт; данные профессий целиком есть и в таблице правила «Шаг 2. Флотские профессии».

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) | 1 | не взято — обложка; `atmosphere.json` |
| Credits | 2 | не взято — выходные данные; упоминание «Gazette» — в `rule/expand-the-world`, логотип — `atmosphere.json` |
| Contents | 3 | источник `rule/what-is-this` |
| What Is This? | 4 | `rule/what-is-this` |
| The Wooden World | 4 | `rule/what-is-this` (абзац «Деревянный мир») |
| Life in His Majesty’s Navy | 4 | `rule/life-in-his-majestys-navy` |
| Types and Ranks of Sailors; Commissioned Officers | 4–5 | `rule/types-and-ranks-of-sailors` |
| Warrant Officers; Common Sailors | 5 | `rule/types-and-ranks-of-sailors` (+ таблица «Чины и должности корабля») |
| Sexism and Homophobia in the Navy (врезка) | 5 | `rule/types-and-ranks-of-sailors` |
| Mythos Hook: The Unknown Passenger | 5 | `rule/mythos-hooks` |
| Joining the Navy | 5–6 | `rule/joining-the-navy` |
| Influence and Promotion | 6 | `rule/influence-and-promotion` |
| Mythos Hook: The Kraken Club | 6 | `rule/mythos-hooks`, `organization/kraken-club`, `character/admiral-plimpton` |
| Society and Relationships; Work & Social Groups: Watches and Divisions | 6–7 | `rule/society-and-relationships` |
| Pride and Prejudice | 7 | `rule/society-and-relationships` |
| Etiquette and Tradition | 7–8 | `rule/society-and-relationships` |
| A Note on Honor, Insults and Duels (врезка) | 7 | `rule/a-note-on-honor-insults-and-duels` |
| Daily Life at Sea | 8 | `rule/daily-life-at-sea` |
| Clothing | 8 | `rule/daily-life-at-sea` |
| Meals | 8, 10 | `rule/daily-life-at-sea` |
| (иллюстрация: пост-капитан, около 1807) | 9 | `rule/daily-life-at-sea` (источник, подпись); картинка — `atmosphere.json` |
| Combat | 10–11 | `rule/daily-life-at-sea` (абзац «Бой») |
| Firing the Long Guns (врезка) | 10 | `rule/firing-the-long-guns` (шаги команд) |
| Death, Pox, Drunkenness and other Hazards | 11 | `rule/death-pox-drunkenness-and-other-hazards` |
| Mythos Hook: An Outbreak of Plague | 11 | `rule/mythos-hooks` |
| Sailors’ Superstitions | 11 | `rule/sailors-superstitions` |
| Discipline, Punishment and Mutiny | 11 | `rule/discipline-punishment-and-mutiny` |
| Mythos Hook: Mutiny on the Argent | 12 | `rule/mythos-hooks` |
| The Admiralty | 12 | `rule/the-admiralty` |
| (подпись: «Спиди» берёт «Эль Гамо», 1801) | 12 | источник `rule/the-admiralty`; картинка — `atmosphere.json` |
| Types of Ships and Their Purposes; Ships of the Line; Frigates; Smaller Warships | 13 | `rule/types-of-ships-and-their-purposes` |
| (эмблема клуба «Кракен» с подписью) | 13 | картинка `organization/kraken-club` |
| (гравюра «A View of the Royal Navy of Great Britain», 1804) | 14 | источник `rule/types-of-ships-and-their-purposes`; картинка — `atmosphere.json` |
| Your Investigator At Sea; Age and Seniority (врезка) | 15 | `rule/your-investigator-at-sea` |
| Step 1: Generate Characteristics | 15 | `rule/step-1-generate-characteristics` |
| Step 2: Determine Occupation; Commissioned Officer | 15–16 | `rule/step-2-determine-occupation` (таблица «Флотские профессии»); черновик `new-shared/occupations/regency-navy-commissioned-officer.json` |
| Bosun; Carpenter; Chaplain; Gunner; Marine | 16–17 | то же, черновики `regency-navy-bosun`, `-carpenter`, `-chaplain`, `-gunner`, `-marine` |
| (иллюстрации «A Bosun, circa 1807», «A Private of Marines, ca. 1815») | 5, 16 | `atmosphere.json` (к профессиям, когда появятся) |
| Master; Purser; Surgeon; Forecastle Sailor or Topman; Afterguard/Waister | 17 | то же, черновики `regency-navy-master`, `-purser`, `-surgeon`, `-forecastle-sailor-or-topman`, `-afterguard-waister` |
| Step 3: Decide Skills and Allocate Skill Points; Astronomy; Credit Ratings and Prizes; Etiquette | 18 | `rule/step-3-decide-skills-and-allocate-skill-points` |
| The Sail Skill | 18 | `rule/step-3-decide-skills-and-allocate-skill-points`; черновик `new-shared/skills/sail.json` |
| Step 4: Create a Backstory; Appearance and Ideology/Beliefs; Significant People; Meaningful Locations; Treasured Possessions; Scars & Strange Encounters | 18 | `rule/step-4-create-a-backstory` |
| Additional Details; Birthplace (таблица 1d100); Officers vs. Seamen: Nationality; Gender; Name; Picture | 19 | `rule/additional-details` (таблица в правиле) |
| Step 5: Equip the Investigator | 19 | `rule/step-5-equip-the-investigator` |
| Naval Combat in Call of Cthulhu; Quick Tips on Managing a Battle | 19 | `rule/naval-combat-in-call-of-cthulhu` (шаги — советы) |
| Naval Combat Cheat Sheet for Keepers & Investigators; What Do I Do?; What Skill Do I Use? | 20 | `rule/naval-combat-cheat-sheet` (2 таблицы) |
| Keeper Advice | 21 | `rule/keeper-advice` |
| Reputation in the Navy; Keeper’s Note; таблица Reputation / Ship’s Opinion / Effect | 21 | `rule/reputation-in-the-navy` |
| The Meaning of Reputation at Sea; Losing and Gaining Reputation | 21–22 | `rule/reputation-in-the-navy` (2 таблицы и список +10) |
| The Alternative Reputation Score (примеры Шафтсбери и Уиллис) | 21–22 | `rule/the-alternative-reputation-score` (`optional`, `examples`) |
| Social Groups in Your Party | 22 | `rule/social-groups-in-your-party` |
| Expand the world | 22–23 | `rule/expand-the-world` |
| (подписи: смерть Нельсона; «Виктори» при Трафальгаре) | 22, 23 | источник `rule/the-navy-vs-the-mythos`; картинки — `atmosphere.json` |
| The Navy vs. the Mythos | 23 | `rule/the-navy-vs-the-mythos` |
| Appendix: Ships, Guns and Crew (параметры) | 23–24 | `rule/appendix-ships-guns-and-crew` |
| First-Rate Ships; Frigate; Sloop-of-War; Typical … Statistics | 24 | `rule/appendix-ships-guns-and-crew` (таблица «Типичные корабли») |
| Appendix: A Tour of a Frigate; Directions on a ship | 25 | `rule/appendix-a-tour-of-a-frigate`; `location/hms-caliban` |
| Masts and Rigging; Upper Deck; Gundeck; Mess Deck; Orlop and Hold | 25 | `location/caliban-masts-and-rigging`, `caliban-upper-deck`, `caliban-gundeck`, `caliban-mess-deck`, `caliban-orlop-and-hold` |
| Deck arrangements in other kinds of ships | 25 | `rule/appendix-a-tour-of-a-frigate` |
| (подпись: «Блэк Джоук» берёт «Эль Альмиранте», 1829) | 25 | источник `rule/appendix-ships-guns-and-crew`; картинка — `atmosphere.json` |
| Appendix: Some Convenient Phrases | 26 | `rule/appendix-some-convenient-phrases` (таблица фраз + словарик жаргона) |
| Learn More About the Navy | 26 | `rule/learn-more-about-the-navy` |
| Handouts | 26 | описания `handout/recruitment-poster`, `handout/cookery-for-the-royal-navy` |
| Handout 1: VOLUNTEERS / Royal Tars of Old England | 27 | `handout/recruitment-poster` (текст + перевод + картинка) |
| Handout 2: Cookery for the Royal Navy (титул) | 28 | `handout/cookery-for-the-royal-navy` |
| Plum Pudding, or Duff; Ship’s Biscuit | 29 | `handout/cookery-for-the-royal-navy` |
| Burgoo; Pease Porridge; Grog | 30 | `handout/cookery-for-the-royal-navy` |
| (задняя обложка, аннотация) | 31 | не взято — аннотация; `atmosphere.json` |

## Не взято

- Обложка (с. 1), выходные данные (с. 2), задняя обложка с аннотацией (с. 31) — оформление и реклама; картинки — в `atmosphere.json`.
- Оружие: книга не даёт ни одной характеристики оружия (пушки, мушкеты, пистолеты, сабли только названы) — записей и `source_variants` нет.
- Корабли «Призрак» (HMS Wraith) и «Арджент» (HMS Argent), адмирал Форрестер — только в зацепках, остаются текстом `rule/mythos-hooks`.
- Лейтенант Томас Шафтсбери и помощник боцмана Лайза Уиллис — персонажи примера, остаются в `examples` правила.
- Исторические люди и корабли из подписей и текста (лорд Нельсон, лорд Кокрейн, «Виктори», «Спиди», «Шеннон», «Чесапик» и т. п.) — текстом.
- Профессии и навык «Парусное дело» — не в `kb/` (правило §1), а черновиками в `new-shared/` и таблицей в правиле.
- Таблица мест рождения (1d100) и потери Репутации — таблицами внутри правил, не записями `table` (общий `kb/tables/` не наш).
- Документ «Gazette» и сценарий «Wonders in the Deep» — внешние, в библиотеке нет.

## Опечатки и расхождения книги

| Где | Напечатано | Что не так | В записи |
|---|---|---|---|
| с. 18, Etiquette | «See Reputations At Sea» | раздела с таким названием нет; это «Reputation in the Navy» (с. 21) | `rule/step-3-…` errata, исправлено в записи |
| с. 24, параметры кораблей | «Speed: Measured in knots and km/h» | ни у одного из трёх кораблей скорость не дана | `rule/appendix-ships-guns-and-crew` errata |
| с. 6 и с. 27 | премия добровольца «a pound or two» / на плакате 5 фунтов, 2 фунта 10 шиллингов, 30 шиллингов | два разных значения | `rule/joining-the-navy` errata |
| с. 13, 24, 25 | фрегат: 28 пушек на одной палубе, «gun deck» — жильё / типичный — 38 пушек (28 на верхней палубе) / «Калибан» — 16 пушек с борта на крытой орудийной палубе | разные описания; книга оговаривает разнообразие | `quality.notes` правил и корабля |
| с. 21 | таблица Репутации кончается на 96–99 | значения 100 нет | `quality.notes`, как напечатано |
| с. 29 | сухарь: «four cups flour … two pounds of fat» | жира как в пудинге на 4 фунта муки — похоже на перенос строки рецепта | `quality.notes` раздатки, как напечатано |
| с. 4, 29 | «In Strage Seas», «coffee..» | словесные опечатки (Р-39) | не записаны; в `text.en` раздатки — как напечатано |

## Термины книги (English → русская форма в записях)

| English | Русский |
|---|---|
| In Strange Seas | «В странных морях» |
| Regency Cthulhu | Regency Cthulhu (без перевода); эпоха — Регентство |
| Royal Navy; His Majesty’s Navy; King’s ship | Королевский (военно-морской) флот; флот Его Величества; корабль короля |
| HMS … | корабль Его Величества «…» |
| The Wooden World | Деревянный мир |
| Mythos Hook | Зацепка Мифов |
| Sail (skill) | Парусное дело |
| Etiquette (skill) | Этикет |
| Reputation | Репутация |
| Natural Philosophy (Anatomy / Mathematics) | Натурфилософия (анатомия / математика) |
| Astronomy | Астрономия |
| Dancing; Gaming | Танцы; Азартные игры |
| Occupation(al) Band | полоса дохода |
| Fighting (Sword) / (Brawl) / (Melee weapons) | Ближний бой (меч) / (драка) / (холодное оружие) |
| Firearms (Cannon) / (Musket) / (Pistol) | Стрельба (пушка) / (мушкет) / (пистолет) |
| Art/Craft (Carpentry) / (Knots) | Искусство/ремесло (плотницкое дело) / (узлы) |
| interpersonal skill | социальный навык |
| any one other skill as personal or era specialty | один любой другой навык в зависимости от специальности и эпохи |
| Commissioned Officer | офицер с патентом |
| Warrant Officer | уорент-офицер |
| standing officers | постоянные офицеры |
| petty officers; mates | унтер-офицеры; помощники |
| captain; post captain; made post | капитан; пост-капитан; получить пост |
| commander; master and commander | коммандер; мастер-коммандер |
| lieutenant; midshipman; young gentlemen; youngsters | лейтенант; мичман; юные джентльмены; молодняк |
| Navy list | Список флота |
| master (sailing master); master’s mate; quartermaster | штурман; помощник штурмана; квартирмейстер |
| gunner; gunner’s mate; armorer | канонир; помощник канонира; оружейник |
| bosun (boatswain); bosun’s mate; sailmaker | боцман; помощник боцмана; парусный мастер |
| carpenter; carpenter’s mate; caulker | корабельный плотник; помощник плотника; конопатчик |
| purser | казначей |
| surgeon; surgeon’s mate; loblolly boy | корабельный хирург; помощник хирурга; лоблолли-бой |
| chaplain; parson | капеллан; священник |
| Marine; Marine captain; Royal Marine | морской пехотинец; капитан морской пехоты; Королевская морская пехота |
| Forecastle Sailor; Topman | баковый матрос; марсовый |
| Afterguard; Waister | ютовый; шкафутный |
| able seaman / rated able; ordinary seaman; landsman / landman | матрос первой статьи / записан в первую статью; матрос второй статьи; сухопутный |
| idlers | «бездельники» |
| watch; go below; division(s) | вахта; уйти вниз; дивизион(ы), смотр по дивизионам |
| mess; messmates; mess cook; wardroom | бачок; товарищи по бачку; кок бачка; кают-компания |
| Impress Service; pressed; bounty | Служба вербовки; завербован силой; вербовочная премия |
| come in through the hawse-hole | прийти через клюз |
| half pay; thrown on shore | половинное жалованье; списан на берег |
| prize money | призовые деньги |
| sea daddy; tie-mate; pigtail | морской батя; напарник по косице; косица |
| slops | слопс |
| ship’s biscuit; hard tack; salt horse | корабельный сухарь; галета; солёная конина |
| grog; burgoo; pease porridge; plum duff | грог; бергу; гороховая каша; плам-дафф (сливовый пудинг) |
| bargemen (weevils) | баржевики |
| Articles of War; court martial | Военные статьи; военный суд |
| flogging; disrated; in irons; sent to the masthead; cashiered | порка; разжалован; в кандалы; отправлен на мачту; уволен со службы |
| crossing the line | пересечение экватора |
| jonah | Иона |
| right man-o-war’s man; shipmate; A second Lord Nelson | настоящий военный моряк; товарищ по экипажу; второй лорд Нельсон |
| the Ton | высший свет |
| Admiralty; First Lord of the Admiralty; Admiralty Board; Naval Board | Адмиралтейство; Первый лорд Адмиралтейства; Совет Адмиралтейства; Морской совет |
| Victualling Board | Провиантский совет |
| rear-admiral; vice admiral; Admiral of the Fleet; yellow admiral | контр-адмирал; вице-адмирал; адмирал флота; жёлтый адмирал |
| squadron (red, white, blue) | эскадра (красная, белая, синяя) |
| ship of the line; first-rate … sixth-rate | линейный корабль; корабль первого … шестого ранга |
| frigate; sloop (of war); brig; Baltimore clipper | фрегат; (военный) шлюп; бриг; балтиморский клипер |
| gunboat; bomb ship | канонерская лодка; бомбардирский корабль |
| beat to quarters | бить боевую тревогу |
| long guns; great guns; carronade; swivel gun; chase guns | корабельные орудия; большие пушки; карронада; фальконет; погонные орудия |
| broadside; round-shot; chain-shot / bar-shot; grapeshot | бортовой залп; ядра; книппели; картечь |
| 32-pounder (и т. п.) | 32-фунтовое орудие |
| cutting-out expedition | вылазка за призом |
| weather-gage | наветренное положение |
| Silence! / Cast loose your guns! / Sponge your guns! / Load cartridge! / Load round! / Run out your gun! / Fire! | Тишина! / Отдать орудия! / Банить орудия! / Заряжай картуз! / Заряжай ядро! / Выкатить орудие! / Огонь! |
| fore/forward; aft; starboard; port/larboard; aloft; below; windward; leeward | нос; корма; штирборт; бакборт; наверху; внизу; наветренная; подветренная сторона |
| mainmast; foremast; mizzenmast; tops; bowsprit; figurehead | грот-мачта; фок-мачта; бизань-мачта; марсы; бушприт; носовая фигура |
| stays, braces, halyards, shrouds, ratlines; rigging | штаги, брасы, фалы, ванты, выбленки; такелаж |
| upper deck; quarterdeck; forecastle; gundeck; mess deck; orlop; hold | верхняя палуба; шканцы; бак; орудийная палуба; жилая палуба; орлоп; трюм |
| helm; capstan; heads; galley; manger | штурвал; кабестан; гальюн; камбуз; загон для скота |
| cockpit; sick berth; powder magazine; spirit room | кокпит; лазарет; крюйт-камера; винная кладовая |
| Tons Burthen; gundeck length; beam; draught; sail plan; ship-rigged; square-rigged | тонны бертен; длина орудийной палубы; ширина; осадка; парусное вооружение; корабельное; прямые паруса |
| hand, reef and steer | работать со снастями, брать рифы и стоять на руле |
| The Kraken Club | клуб «Кракен» |
| Admiral Plimpton; Admiral Forrester | адмирал Плимптон; адмирал Форрестер |
| HMS Caliban; HMS Wraith; HMS Argent | «Калибан»; «Призрак»; «Арджент» |
| Wonders in the Deep | «Чудеса в глубине» |
| Gazette (living world document); London Gazette | «Gazette» («живой» документ мира); «Лондонская газета» |
| Spithead; the Nore | Спитхед; Нор |
| Royal Naval Academy / College | Королевская военно-морская академия / колледж |
| Volunteers; Royal Tars of Old England | Добровольцы; Королевские матросы Старой Англии |
| Cookery for the Royal Navy | «Кулинария для Королевского флота» |

## Вопросы ведущему

- Профессии и навык «Парусное дело»: задание говорило «новые флотские профессии — записями книги», а
  `docs/conventions.md` §1 — профессии и навыки только в общем справочнике. Сделано по правилам: черновики общих записей
  в `new-shared/` (11 профессий `coc:occupation:regency-navy-*`, навык `coc:skill:sail`), данные — в таблице правила.
  Перенести черновики в `kb/occupations/`, `kb/skills/` — решение ведущего (тогда в таблице правила и записях можно
  поставить ссылки).
- Глава книги в `chapters` (`pipeline/source/books.json`) для вкладки «Правила» не задана — нужна, если правила книги
  должны встать в свою главу (по образцу Pulp/эпох).
- Глоссарий `kb/terms/` не пересобирался (не мой файл); список терминов — выше.
