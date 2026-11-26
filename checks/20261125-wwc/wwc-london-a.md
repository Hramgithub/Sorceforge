# World War Cthulhu: London — сторона сеттинга (часть «london-a»)

Книга `wwc-london-en` (Cubicle 7, 2016; 7-я редакция, хотя метка библиотеки — [EN 6e]). Часть london-a — с. 1–78: от
обложки до конца главы «Shopping and Equipment»; с. 79 («Mythos Horrors») и дальше — часть london-b.

Страницы: печатная = физической (смещение **0**; проверено по изображениям: «5» на физ. 5, «30» на физ. 30, «40» на физ. 40,
«76» на физ. 76); без номера — физ. 1 (обложка). Русского перевода в базе и библиотеке нет (поиск «Network N», «Сеть N»,
«Blitz», «Блиц», имён рассказчиков и мест в `kb/books/*-ru/` — пусто); русский текст — наш перевод (`translated`). Эпоха —
`1940s-1980s` (Лондон 1939–1945, по общей схеме линейки; сказано в `quality.notes`), свод — `core`.

## Записи (80 в `kb/books/wwc-london-en/` + 16 черновиков общих записей)

- `rule` — 41: «Введение в World War Cthulhu: London» → «Лондон в войне: этапы»; «Вспомогательные агенты Сети N: вербовка и
  служба»; «Голоса Лондона» (6 врезок целиком); «Создание вспомогательных агентов Сети N» → 9 шагов, быстрый способ, новые
  навыки, перенос сыщиков «Зова Ктулху», сыщик The Darkest Hour; «Другие организации сыщиков»; «Лондон военного времени» → 9
  разделов («Бомбы и цели», «Угроза изнутри», «Оборона и контрмеры», «Военные в Лондоне», «Воздушные налёты»,
  «Бомбоубежища», «Затемнение», «Гражданская оборона в Блиц», «Последствия налёта»), «Сохраняйте спокойствие и продолжайте»
  → 4 раздела, «Развлечения и пропаганда», «Преступление и наказание» → «Преступный промысел в военное время»; «Покупки и
  снаряжение» → «Как достать товар на чёрном рынке», «Огнестрельное оружие в военном Лондоне», «Противогазы».
- `organization` — 12: Вспомогательные агенты Сети N; Тайная папашина армия; Друзья лондонских кладбищ; Потерянные мальчишки и
  девчонки; Община церкви Искупителя; Банда Брэдли; банды Лондона — семья Сабини, Уайты, Парни из Хокстона, Тяжёлая банда
  Билли Хилла, Банда Хакни, Парни из Элефанта.
- `character` — 16: рассказчики «Голосов Лондона» (Дэвид Рейнольдс, Чарли Хиллиер, Джоан Хёрли, Уильям Криббинс, Том
  Кендал, Патрик Харрисон); Алф Сагден, Томми Брэдли, Микки (банда Брэдли), Билли Хилл, майор Абелар Фолкс; известные люди —
  Уинстон Черчилль, Джордж Формби, лорд Хо-Хо (Уильям Джойс), Грейси Филдс, Вера Линн (5 портретов).
- `location` — 11 (все `part_of` Лондон, его районы из «Масок» или `coc:location:lambeth`): контора N у Трафальгарской
  площади, церковь Искупителя (Баттерси), станция метро «Олдвич», британский ресторан в Балеме, Кабинетские военные комнаты,
  Лондонские доки, Холланд-хаус, Пикадилли-серкус, Трафальгарская площадь, церковь Святого Стефана на Коулман-стрит, Арка
  Веллингтона. Завязки (Plot Hook) — таблицы мест вида «зацепки».
- Черновики общих записей (не в `kb/`, проверены `tools/validate.py` — 0 ошибок) — `checks/20261125-wwc/new-shared-london-a/`:
  - навыки `coc:skill:civil-defence` (Гражданская оборона, 10%), `coc:skill:command` (Командование, 05%),
    `coc:skill:make-do-and-mend` (Смекалка и починка, 15%), `coc:skill:operate-radio` (Радиодело, ИНТ × 2%);
  - 12 профессий `coc:occupation:wwc-*`: university-professor, portrait-artist, ambulance-driver,
    wealthy-london-gentleman-or-lady, big-band-musician, vicar, spiv, london-tramp, market-trader,
    london-newspaper-reporter, london-bobby, london-cabbie.
  После переноса добавить ссылки на них в правила «Новые навыки…», «Шаг пятый», «Шаг шестой», «Гражданская оборона в Блиц»,
  «Преступление и наказание» (лондонский бобби), «Преступный промысел» (спив).
- Предложения — `proposals-london-a.json` (39 правок, пробный прогон `apply.py` — ложатся все): `coc:location:buckingham-palace`,
  `coc:location:hyde-park`, `coc:location:st-pauls-cathedral`, `masks-of-nyarlathotep-en/location/england-green-park`
  (абзац, эпоха, источник, таблица-завязка, ссылки), `coc:location:london` (абзац о Лондоне 1939–1945, эпоха, источник),
  `wwc-cold-war-en/character/n` и `organization/n` (N и сеть в годы войны), `coc:skill:navigate`, `coc:skill:artillery`,
  `coc:skill:art-craft` (лондонские применения). Грин-парк из «Масок» встретился во второй книге — по Р-154 его можно
  перенести в общие места (решение ведущего).
- `proposals-drafts-london-a.json` (4) — к черновикам части cw-a `coc:skill:military-science` (источник London, база 01% против
  00% в Cold War) и `coc:skill:tradecraft` (источник London): применять после переноса черновиков в `kb/skills/`.
- Картинки — 5 портретов (`art-london-a.json` → `art-london-a-proposals.json`, применены): Черчилль, Формби, лорд Хо-Хо,
  Грейси Филдс, Вера Линн. Атмосфера и оформление — `atmosphere-london-a.json` (48 страниц).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (обложка) | 1 | не взято — обложка; `atmosphere-london-a.json` |
| Contents | 2–3 | не взято — оглавление (использовано для плана частей) |
| Credits; Disclaimer | 3 | не взято — выходные данные |
| Introduction: What is World War Cthulhu: London?; London; The Cthulhu Mythos; The Horrors of War | 4–5 | `rule/introduction` |
| London at War | 5 | `rule/introduction` |
| The Phoney War; The Blitz; For the Duration | 5 | `rule/london-at-war` |
| The ‘Baby Blitz’ – V-1 and V-2 Rocket Attacks; Peacetime and Rebuilding | 6 | `rule/london-at-war` |
| Network N; Civilian Auxiliaries | 6–7 | `rule/introduction`, `organization/network-n-auxiliaries` |
| More Information | 7 | `rule/introduction` |
| London Voices: David Reynolds, 28, Builder | 7 | `rule/london-voices`, `character/david-reynolds` |
| Network N Auxiliaries; Recruitment; The Life of an Auxiliary | 8–9 | `rule/network-n-auxiliaries`, `organization/network-n-auxiliaries`, `location/ns-office` |
| Resources; Advancement | 9 | `rule/network-n-auxiliaries` |
| Creating Network N Auxiliaries; Creating your Investigator; девять шагов | 10–11 | `rule/creating-network-n-auxiliaries` |
| London as a Prelude to The Darkest Hour (врезка) | 10 | `rule/creating-network-n-auxiliaries` |
| Step One: Characteristics | 11 | `rule/step-one-characteristics` |
| Step Two: Age | 11 | `rule/step-two-age` |
| Step Three: Other Attributes | 11–12 | `rule/step-three-other-attributes` |
| Step Four: Identity and Name; Investigator Names (таблица); Germans and Austrians; Italians; Poles; Americans | 12–13 | `rule/step-four-identity-and-name` |
| Step Five: Pre-war Occupations and Skills; Professional Skills; Personal Interest Skills | 13–14 | `rule/step-five-pre-war-occupations-and-skills` |
| The London Intelligentsia — University Professor | 14 | то же правило (таблицы); черновик `coc:occupation:wwc-university-professor` |
| The Arts — Portrait Artist | 14–15 | то же; `coc:occupation:wwc-portrait-artist` |
| The Medical Profession — Ambulance Driver | 15 | то же; `coc:occupation:wwc-ambulance-driver` |
| Gentry and Aristocracy — Wealthy London Gentleman or Lady | 15–16 | то же; `coc:occupation:wwc-wealthy-london-gentleman-or-lady` |
| The Entertainment Profession — Big Band Musician | 16 | то же; `coc:occupation:wwc-big-band-musician` |
| Religion — Vicar | 16 | то же; `coc:occupation:wwc-vicar` |
| Criminal — Spiv (Black-marketeer) | 16–17 | то же; `coc:occupation:wwc-spiv` |
| The Homeless — The London Tramp | 17–18 | то же; `coc:occupation:wwc-london-tramp` |
| Tradesmen — Market Trader | 18 | то же; `coc:occupation:wwc-market-trader` |
| The Media — London Newspaper Reporter | 18 | то же; `coc:occupation:wwc-london-newspaper-reporter` |
| Public Order — London Bobby | 18–19 | то же; `coc:occupation:wwc-london-bobby` |
| Jobs about Town and Miscellaneous Professions — London Cabbie | 19 | то же; `coc:occupation:wwc-london-cabbie` |
| Step Six: Wartime Experience; General Experience of Wartime London | 19–20 | `rule/step-six-wartime-experience` (таблица вариантов) |
| Reserved Occupations (врезка) | 20 | `rule/step-six-wartime-experience` |
| Become a Member of the Home Guard | 20 | то же |
| Become one of the Dispossessed; Become an ARP Warden; Become an Auxiliary Firefighter, Ambulance Driver or Medical Staff | 21–22 | то же |
| Military Service; Conscription (врезка); Turn to a Life of Crime | 22–23 | то же |
| Deserters (врезка); The Appliance of Science | 23–24 | то же |
| London Voices: Charlie Hillier, 11, Child | 24 | `rule/london-voices`, `character/charlie-hillier` |
| Conscientious Objectors (врезка) | 24 | `rule/step-six-wartime-experience` |
| Join an Auxiliary Unit; Female Investigators (врезка) | 25 | то же |
| Step Seven: Mythos Encounter | 26 | `rule/step-seven-mythos-encounter` |
| London Voices: Joan Hurley, 29, Housewife and Mother | 26 | `rule/london-voices`, `character/joan-hurley` |
| Step Eight: Create a Backstory; Using Random Tables for Inspiration | 26–27 | `rule/step-eight-create-a-backstory` |
| Personal Description; Someone Who Needs You (1d10); Your Favourite Place in Town (1d10) | 27 | то же (таблицы) |
| Someone You Can Call Upon (1d10); Treasured Possessions (1d10) | 27–28 | то же (таблицы) |
| London Voices: William Cribbins, 52, Local Defence Volunteer | 28 | `rule/london-voices`, `character/william-cribbins` |
| Personality Trait; Personality Style (1d4); Regaining Sanity; Key Background Connection | 29 | `rule/step-eight-create-a-backstory` |
| Step Nine: Equipping your Investigator; Living Standards; Cash and Assets (таблица); Equipment | 30–31 | `rule/step-nine-equipping-your-investigator` |
| Quick-fire Method of Investigator Creation (врезка) | 31 | `rule/quick-fire-method-of-investigator-creation` |
| New Skills and New Uses for Existing Skills; Artillery (01%); Civil Defence (10%) | 31–32 | `rule/new-skills-and-new-uses-for-existing-skills`; черновик `coc:skill:civil-defence`; предложение к `coc:skill:artillery` |
| Command (05%) | 32 | то же правило; черновик `coc:skill:command` |
| Art/Craft (Forgery) (05%) | 32–33 | то же правило; предложение к `coc:skill:art-craft` |
| Make Do and Mend (15%) | 33 | то же правило; черновик `coc:skill:make-do-and-mend` |
| Military Science (01%) | 33 | то же правило; `proposals-drafts-london-a.json` к черновику cw-a |
| Navigate (10%) | 33–34 | то же правило; предложение к `coc:skill:navigate` |
| Operate Radio (INT ×2%) | 34 | то же правило; черновик `coc:skill:operate-radio` |
| Tradecraft (01%) | 34–35 | то же правило; `proposals-drafts-london-a.json` к черновику cw-a |
| Adapting Call of Cthulhu Investigators | 35 | `rule/adapting-call-of-cthulhu-investigators` |
| Playing a World War Cthulhu: The Darkest Hour Investigator | 35 | `rule/playing-a-world-war-cthulhu-the-darkest-hour-investigator` |
| Other Investigator Organisations | 36 | `rule/other-investigator-organisations` |
| Dad’s Secret Army | 36 | `organization/dads-secret-army`, `character/alf-sugden` |
| The Friends of the Cemeteries of London | 36 | `organization/friends-of-the-cemeteries-of-london` |
| The Lost Boys and Girls | 36 | `organization/lost-boys-and-girls` |
| The Church of the Redeemer | 36–37 | `organization/church-of-the-redeemer`, `location/church-of-the-redeemer-battersea` |
| The Bradley Gang | 37 | `organization/bradley-gang`, `character/tommy-bradley`, `character/mickey` |
| London Voices: Thom Kendal, 57, Fire Brigade | 37 | `rule/london-voices`, `character/thom-kendal` |
| Wartime London; London at War | 38–39 | `rule/wartime-london` |
| The Psychological Strain (врезка) | 39 | `rule/bombs-and-targets` |
| Bombs and Targets; Bombs Away; German Bombs (таблица) | 39–40 | `rule/bombs-and-targets` |
| V-1 and V-2 Rocket Attacks; First-hand Account of a V-2 Attack (врезка); Gas Attacks | 40–41 | `rule/bombs-and-targets` |
| The Threat from Within; The Threat of Invasion | 41 | `rule/the-threat-from-within` |
| Internment, Suspicion and Observation (врезка); Other Forms of Subversion | 42 | `rule/the-threat-from-within` |
| Defences and Countermeasures; Down at the Ack-Ack Battery at Midnight (врезка) | 42–43 | `rule/defences-and-countermeasures` |
| The Military in London; The Armed Forces; The Home Guard | 43–44 | `rule/the-military-in-london` |
| Stay-Behind Parties (врезка); Foreign Personnel in London; The Americans are Coming! (врезка) | 44–45 | `rule/the-military-in-london` |
| Air Raids; The Stages of an Air Raid | 45–47 | `rule/air-raids` |
| Getting Caught in the Open (врезка, частное правило) | 46 | `rule/air-raids` (steps) |
| Describing an Air Raid; First-hand Account of an Air Raid (врезки) | 47 | `rule/air-raids` |
| Air-raid Shelters; Surface Shelters | 47–49 | `rule/air-raid-shelters` |
| London Voices: Patrick Harrison, 44, Manager of the Palais de Dance | 49 | `rule/london-voices`, `character/patrick-harrison` |
| Tube Stations | 49–50 | `rule/air-raid-shelters`, `location/aldwych-underground-station` |
| Finding Shelter in Dark Places (врезка) | 50 | `rule/air-raid-shelters` |
| The Blackout; Operating During the Blackout (частное правило) | 50–51 | `rule/the-blackout` |
| Fear the Dark; ARP Wardens and Network N (врезки); ARP Wardens | 51 | `rule/the-blackout` |
| Civil Defence | 51 | `rule/civil-defence` |
| First-hand Account of a Direct Hit; Putting out an Incendiary Bomb (врезки); Fighting Fires | 52 | `rule/civil-defence` (steps) |
| London Ablaze (врезка); Rescuing Survivors | 53 | `rule/civil-defence` |
| Describing the Damage; Getting Used to Death (врезки); Dealing with the Dead | 54 | `rule/civil-defence` |
| Dealing with the Aftermath; Disruption to Investigations; First-hand Account of the Aftermath of an Incendiary Bomb; Becoming Homeless | 55 | `rule/dealing-with-the-aftermath` |
| Things You Might Find in the Rubble (врезка) | 56 | `rule/dealing-with-the-aftermath` |
| Keep Calm and Carry On; Doing Your Bit | 56 | `rule/keep-calm-and-carry-on` |
| Class, Gender and Respectability; Community Spirit and the Working Classes | 57–58 | `rule/keep-calm-and-carry-on` |
| Wartime Privations and Rationing; Rationing and Scarcity (врезка) | 58–59 | `rule/wartime-privations-and-rationing` |
| Children and the Evacuation | 59–60 | `rule/children-and-the-evacuation` |
| Volunteering and Conscription | 60 | `rule/volunteering-and-conscription` |
| Travel; Papers, Please (врезка) | 60–61 | `rule/travel` |
| Entertainment and Propaganda; Sports, Games and Makeshift Fun | 61–62 | `rule/entertainment-and-propaganda` |
| Television and Radio; The Pictures; News, Propaganda and Morale | 62–63 | `rule/entertainment-and-propaganda` |
| Crime and Punishment; The Police; Police Investigators (врезка) | 63–64 | `rule/crime-and-punishment` |
| Criminal Operations in Wartime; The Black Market; Petrol Rationing and Car Chases (врезка) | 64–65 | `rule/criminal-operations-in-wartime` |
| Burglars, Muggers and Looters; Fraudsters, Forgers and Counterfeiters; Prostitution and Other Vices | 65–67 | `rule/criminal-operations-in-wartime` |
| Deserters and Dodgers | 67–68 | `rule/criminal-operations-in-wartime` |
| Criminal Gangs of London (врезка) | 67 | `rule/criminal-operations-in-wartime`; организации sabini-family, whites, hoxton-boys, heavy-mob, hackney-gang, elephant-boys; `character/billy-hill` |
| New and Harsh Penalties | 68 | `rule/criminal-operations-in-wartime` |
| Notable Figures: Winston Churchill, Prime Minister | 68–69 | `character/winston-churchill` (портрет) |
| George Formby, Entertainer | 69 | `character/george-formby` (портрет) |
| Lord Haw Haw, Nazi Propagandist | 70 | `character/lord-haw-haw` (портрет) |
| Gracie Fields, Entertainer | 70 | `character/gracie-fields` (портрет) |
| Vera Lynn, Entertainer | 70–71 | `character/vera-lynn` (портрет) |
| Places of Interest in Wartime London: Aldwych Underground Station (+ Plot Hook) | 71 | `location/aldwych-underground-station` |
| Balham British Restaurant (+ Plot Hook) | 71 | `location/balham-british-restaurant` |
| Buckingham Palace (+ Plot Hook) | 71–72 | предложение к `coc:location:buckingham-palace`; `character/abelard-folkes` |
| Cabinet War Rooms (+ Plot Hook) | 72 | `location/cabinet-war-rooms` |
| The Docklands (+ Plot Hook) | 72 | `location/docklands` |
| Green Park (+ Plot Hook) | 72 | предложение к `masks-of-nyarlathotep-en/location/england-green-park` |
| Holland House (+ Plot Hook) | 73 | `location/holland-house` |
| Hyde Park (+ Plot Hook) | 73 | предложение к `coc:location:hyde-park` |
| Piccadilly Circus (+ Plot Hook) | 73–74 | `location/piccadilly-circus` |
| Trafalgar Square (+ Plot Hook) | 74 | `location/trafalgar-square` |
| St Paul’s Cathedral (+ Plot Hook) | 74 | предложение к `coc:location:st-pauls-cathedral` |
| St Stephen Coleman Street (+ Plot Hook) | 74 | `location/st-stephen-coleman-street` |
| Wellington Arch (+ Plot Hook) | 74 | `location/wellington-arch` |
| Shopping and Equipment; Price Lists (5 таблиц) | 75–77 | `rule/shopping-and-equipment` |
| Sourcing Goods on the Black Market (врезка) | 77 | `rule/sourcing-goods-on-the-black-market` |
| Prices by year | 78 | `rule/shopping-and-equipment` |
| Firearms (пика Внутренней гвардии) | 78 | `rule/firearms` |
| Gasmasks | 78 | `rule/gas-masks` |

## Не взято

- Обложка, оглавление, выходные данные и дисклеймер (с. 1–3) — не правила и не сюжет; обложка — в `atmosphere-london-a.json`.
- Иллюстрации без подписи (с. 4, 7, 9, 10, 14, 17, 22–25, 29, 31, 34, 38–45, 47, 48, 50–59, 61, 64–66, 68, 75, 77, 78) и фоны
  врезок (бумага «Голосов Лондона» на с. 7, 24, 26, 28, 37, 49; фоны с. 20, 67) — атмосфера/оформление, `atmosphere-london-a.json`.
  Отчёт полноты (`completeness-london-a`) помечает рассказчиков «Голосов Лондона», Билли Хилла и Черчилля (с. 68) «без картинки»
  — на этих страницах только фоны врезок и фото без подписи, не портреты.
- Реальные лица и учреждения, упомянутые мимоходом (король Георг VI, Невилл Чемберлен, Эрнест Бевин, Фрэнк Уиттл, Алан Тьюринг,
  Эми Джонсон, Спайк Миллиган, Ноэл Кауард, Децимус Бёртон, Рузвельт, Сталин; Би-би-си, Министерство информации, Crown Film Unit,
  ENSA, ATS, WRNS, WAAF, Женская добровольческая служба, Пожарная охрана, Особый отдел, «Клубный отдел» на Вайн-стрит, MI8),
  второстепенные лица рассказов (Мэвис, Алфи, Деннис, Дэнни, Джекс, Большой Бен, Билли) — остаются текстом правил.
- Места, упомянутые мимоходом (Харли-стрит, больницы Мидлсекса, Грейт-Ормонд-стрит и Бетлем, Национальная портретная галерея,
  Бервик-стрит, «Радужный угол», театр «Критерион», «Лондон Павильон», церковь Сент-Мартин-ин-зе-Филдс, бани Хэмпстеда, болота
  Хакни, пещеры Чизлхерста, танцзал «Пале-де-Данс», остров Мэн, Блетчли-парк, Харпер-Адамс, деревня Ай-Кросс, остров
  Эйлен-Хастейл, Бодлианская библиотека) — текстом в правилах и местах; отдельных записей нет (одна строка без механики).
- Пароход «Марш» (SS Marsh) из Иннсмута — только в завязке «Лондонские доки» (текстом, ссылка на `coc:location:innsmouth`).
- Пика Внутренней гвардии (урон 1d6, 15 ПЗ) — таблица в `rule/firearms`; кандидат в общий справочник оружия `coc:weapon:*`
  (оружие — глобальный справочник, часть его не заводит).
- Таблицы с броском (1d10 ×4, 1d4) — внутри правила шага восьмого (`tables`), записей `table` нет (как у части cw-a).

## Опечатки и сомнения

| Где | Напечатано | Ожидалось | В записи |
|---|---|---|---|
| с. 11 | «Roll twice to generate a Luck score (see Luck, above)» | Удача описана ниже, в шаге третьем (с. 12) | исправлено, errata `rule/step-two-age` |
| с. 21 | «Your Credit Rating score is reduced 10 points or less» | вероятно, «reduced to 10 points or less» | как напечатано, errata `rule/step-six-wartime-experience` |
| с. 21 | Уклонение (Dodge) дважды в списке навыков «Обездоленного» | один раз | errata там же |
| с. 22 / с. 60 | Закон о военной подготовке: «aged 20-22» / «men of 20-21 years» | одно значение | как напечатано, errata `rule/step-six-…`, `rule/volunteering-and-conscription` |
| с. 29 | Мыслитель: «Add +10 to each of these skills» (11 навыков) | у остальных типов — «выберите три» | как напечатано, errata `rule/step-eight-create-a-backstory` |
| с. 40 | «The Blitz came to an end in 1942» | май 1941 (с. 5) | как напечатано, errata `rule/bombs-and-targets` |
| с. 40 | сноска [1] об осколках — у бомбы SC | по тексту осколки — свойство SD | как напечатано, errata там же (сомнение) |
| с. 65 / с. 77 | спекулянту — «14 years in prison» / «a fine of £500 and up to two years in prison» | одно значение | как напечатано, errata `rule/criminal-operations-in-wartime`, `rule/shopping-and-equipment` |
| с. 76 | фотоплёнка «1s/15d – 2s/6d» | пенсов меньше 12 | как напечатано, errata `rule/shopping-and-equipment` |
| с. 71 | «Balham British Restaurant, Lambeth» | исторически Балем — Уондсворт | по книге (`part_of` Ламбет), `quality.notes` |
| с. 33 | Military Science (01%) | в Cold War — 00% | `proposals-drafts-london-a.json` |
| с. 2, 6, 25 | «Dealing witht the Aftermath» (оглавление), «nine9 months», «stress of your roll» | — | словесные (Р-39), не в errata; первое — в `aliases` |

## Термины (English → русский, наш выбор; переводчик книги берёт эти формы)

| English | Русский |
|---|---|
| Network N Auxiliaries / an Auxiliary | вспомогательные агенты Сети N / вспомогательный агент |
| handler | куратор |
| London Voices | Голоса Лондона |
| the Blitz / Baby Blitz / Phoney War | Блиц / «малый Блиц» / Странная война |
| For the Duration | «на время войны» |
| blackout | затемнение |
| Air Raid Precautions (ARP) / ARP warden | ПВО (служба ПВО) / уполномоченный ПВО |
| Home Guard / Local Defence Volunteers (LDV) / Dad’s Army | Внутренняя гвардия / Добровольцы местной обороны / «папашина армия» |
| Auxiliary Unit / Stay-Behind Parties | вспомогательное подразделение / «оставшиеся группы» |
| Auxiliary Fire Service / Fire Guard / Heavy Rescue Squads | Вспомогательная пожарная служба / Пожарная охрана / тяжёлые спасательные отряды |
| air-raid shelter / Anderson / Morrison / surface shelter | бомбоубежище / убежище Андерсона / убежище Моррисона / наземное убежище |
| all clear | отбой |
| high-explosive / incendiary bomb; oil / magnesium bomb | фугасная / зажигательная бомба; масляная / магниевая бомба |
| “Satan” (bomb) | «Сатана» |
| barrage balloon / ack-ack | аэростат заграждения / зенитки |
| doodlebug / buzz bomb (V-1), V-2 | «жужелица» / «жужжащая бомба» («Фау-1»), «Фау-2» |
| rationing / ration book / clothing coupons / off ration / under the counter | нормирование / продовольственная книжка / купоны на одежду / вне нормы / из-под прилавка |
| British Restaurant | британский ресторан |
| black market / black-marketeer / spiv | чёрный рынок / спекулянт / спив («Спекулянт (спив)») |
| identity card | удостоверение личности |
| Reserved Occupations | бронированные профессии |
| conscientious objector | отказник по убеждениям |
| Operation Pied Piper / evacuee / trekkers / dead-end kids | операция «Крысолов» / эвакуированный / «трекеры» / «дети тупика» |
| Doing Your Bit | вносить свою лепту |
| Wartime Experience | военный опыт |
| Pre-war Occupations | довоенные профессии |
| Civil Defence (skill) | Гражданская оборона |
| Command (skill) | Командование |
| Make Do and Mend (skill) | Смекалка и починка |
| Operate Radio (skill) | Радиодело |
| Military Science / Tradecraft / Art/Craft (Forgery) | Военное дело / Шпионское ремесло / Искусство/ремесло (подделка) — как у cw-a |
| Bruiser / Practical / Thinker / Leader (Personality Style) | Боец / Практик / Мыслитель / Лидер (тип личности) |
| Getting Caught in the Open | Под налётом на открытом месте |
| Getting Used to Death | Привыкание к смерти |
| Plot Hook | зацепка (таблица вида «зацепки») |
| Dad’s Secret Army / The Friends of the Cemeteries of London / The Lost Boys and Girls / The Church of the Redeemer / The Bradley Gang | Тайная папашина армия / Друзья лондонских кладбищ / Потерянные мальчишки и девчонки / церковь Искупителя (община церкви Искупителя) / банда Брэдли |
| Lord Haw-Haw | лорд Хо-Хо |
| Cabinet War Rooms / the Slab | Кабинетские военные комнаты / «Плита» |
| Elder Sign | Знак Старших богов (по базе) |
| Emergency Powers (Defence) Bill | Закон о чрезвычайных полномочиях (обороне) |
| Home Guard pike | пика Внутренней гвардии |

## Висящие ссылки на чужие записи

Нет: все ссылки моих записей ведут на существующие записи (в том числе `wwc-cold-war-en/organization/n`, `character/n`,
`organization/soe`, `organization/mi5` части cw-a). Черновики профессий ссылаются на черновики навыков (`coc:skill:civil-defence`)
— появятся после переноса.
