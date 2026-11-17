# A Time to Harvest — месяц 2 (часть ep2): сверка покрытия

Книга `time-to-harvest-2-en` (PDF 50 стр., печатная страница = физической; с. 1–3 без номеров, с. 50 пустая).
Записи — `kb/books/time-to-harvest-2-en/` (69 записей), правки чужих записей — `proposals-ep2.json` (общие записи,
книга «Аркхэм», Isis Unveiled) и `proposals-m1-ep2.json` (записи месяца 1 — применять после частей world/ep1).
Картинки раздаток — `art-ep2.json` (применены), карты — `app/maps/harvest-ep2-*.jpg`, рамки вырезок — `map-boxes-ep2.json`.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, Credits, Table of Contents | 1–3 | `time-to-harvest-2-en/scenario/episode-2` (sources) |
| Episode 2 (эпиграф из «Снов в ведьмином доме») | 4 | сценарий `episode-2`; эпиграф — «Не взято» |
| Back To Arkham, Back To School | 4 | `scenario/episode-2` (название, hook) |
| Running Episode Two (цели агентов) | 4 | `scenario/episode-2` keeper_info; `organization/mi-go-agents` goals |
| Start: Losing Face | 4–5 | `scene/ep2-losing-face` |
| Invasion Of The Altered Students | 5 | `scenario/episode-2` keeper_info; `organization/mi-go-agents` |
| A Surprise For Blaine | 5–6 | keeper_info; `character/daphne-devine` |
| The Mi-Go Agents: Who’s Inside Whom? | 6 | keeper_info; таблица «Кто в ком: агенты ми-го» сценария |
| Henry Akeley (as William Noakes) | 6 | `character/henry-akeley` |
| Keith Clark (as Roderick Block) | 6 | `character/keith-clark` |
| Daphne Devine (as Prof. Roger Harrold) | 7 | `character/daphne-devine` |
| Lawrence Jarvis (as Terrence Laslow) | 7 | `character/lawrence-jarvis` |
| Summary of Jarvis’ Psychic Powers: Alter Reality, Go Unseen, Send Nightmare, Telekinesis | 7–8 | `character/lawrence-jarvis` abilities |
| Gustav Ludendorff (as Harold Higgins) | 8 | `character/gustav-ludendorff` |
| Dr. Clayton Osborne (as Louis Gibbons) | 8 | `character/clayton-osborne` |
| Wesley Smith (as Clarissa Thurber) | 8 | `character/wesley-smith` |
| Robert Tunes (as Jason Trent) | 8–9 | `character/robert-tunes` |
| The Mi-Go Plan | 9 | keeper_info; `organization/mi-go-agents`; `item/false-crater-evidence` |
| Glitches In The Plan | 9–10 | keeper_info, advice; Эйкли, Кларк; `character/lou-ann-clark`, `simon-clark`, `samuel-clark` |
| Dr. Henry Armitage (врезка) | 10 | предложение → `coc:character:henry-armitage`; advice сценария |
| Professor Albert N. Wilmarth (врезка) | 10 | предложение → `arkham-en/character/campus-albert-wilmarth`; advice |
| Something Is Not Right | 10, 12 | `scene/ep2-something-is-not-right` |
| Miskatonic University Map | 11 (47) | `map/miskatonic-university` (46 меток) |
| Observation | 13 | `scene/ep2-observation` |
| Professor Ashley Learmonth (врезка) | 13 | предложение → `arkham-en/character/campus-ashley-learmonth` |
| Handout: Harvest Papers 8 | 14 (40) | `handout/harvest-papers-8` |
| Handout: Harvest Papers 9 | 15 (41) | `handout/harvest-papers-9` |
| Handout: Harvest Papers 10 | 16 (42) | `handout/harvest-papers-10` |
| The Search For Blaine | 16, 18 | `scene/ep2-search-for-blaine`; `location/flanaghan-house`, `blaine-attic-apartment`; `item/daphne-devine-journal`; `tome/discoverie-of-witchcraft`, `tome/demonality`, копия `coc:tome:isis-unveiled` (предложение) |
| M.U. Science Building Map | 17 (43) | `map/science-hall` (41 метка) |
| Chief Detective Luther Harden (врезка) | 18 | предложение → `coc:character:luther-harden`; `character/james-harden` |
| Blaine’s Suicide | 18 | `scene/ep2-blaines-suicide` |
| Harvest: Handout Papers 11 | 19 (45) | `handout/harvest-papers-11`; Эмельда — запись ep4 `time-to-harvest-4-en/character/emelda-cratchett` (+ предложение) |
| Harvest: Handout Papers 12 | 20 (44) | `handout/harvest-papers-12` |
| Mind Games | 21 | `scene/ep2-mind-games` |
| Figuring Things Out | 21 | `scene/ep2-figuring-things-out`; `location/harrold-house` |
| Optional: Another Trap? / On Hangman’s Hill | 21–22 | `scene/ep2-another-trap` |
| Chase Sequence: Agent Reference | 23 | таблица сценария «Погоня: справка по агентам»; notes агентов |
| Preparing For The Worst | 23 | `scene/ep2-preparing-for-the-worst` |
| A Good Diversion | 23–24 | `scene/ep2-a-good-diversion`; таблица «Хаос ночи амнезии» |
| The Raid | 24, 27 | `scene/ep2-the-raid`; `location/learmonth-laboratory`, `learmonth-office`, `learmonth-house`, `orne-restricted-collection`; `item/agents-book-lists`; `character/mona-learmonth` |
| Orne Library Map | 25 (48) | `map/orne-library-1` (46 меток) |
| Orne Library Map Upper Level; Orne Library Hours of Operation | 26 (49) | `map/orne-library-2` (41 метка; часы — в quality.notes) |
| A Possible Conclusion? | 27 | `scenario/episode-2` conclusion |
| Optional: The Chase Is On! | 27–28 | `scene/ep2-the-chase-is-on`; `item/harrold-franklin-sedan`, `item/block-buick` |
| Chase Sequence: Reference (машины) | 28 | таблица «Погоня: справка по машинам»; items машин |
| Optional: The Safe House | 28–29 | `scene/ep2-the-safe-house`; `location/safe-house`; `item/mi-go-left-behind` |
| The Safe House Map | 29 (42) | `map/safe-house` (12 меток) |
| Conclusion; Rewards For Episode Two | 30 | `scenario/episode-2` conclusion |
| Appendix A: Personalities and Monsters (Mi-go Agents, Miskatonic University People, Arkham Police) | 31–33 | 8 агентов; статблоки Армитеджа, Лирмонта, Уилмарта, Хардена — предложения (вариант/статблок); `character/typical-police-officer` |
| Appendix B: Arkham And Miskatonic University; About Arkham; Law And Order In Arkham | 34–35 | предложение → `coc:location:arkham` |
| Miskatonic University; A Note About Student Life; Main Campus | 35 | предложение → `coc:location:miskatonic-university` |
| Science Hall | 35 | предложение → `coc:location:arkham-612-science-hall` |
| Charles Tyner Science Annex | 35 | предложение → `…-613-charles-tyner-science-annex`; `location/learmonth-laboratory`, `learmonth-office` |
| George Locksley Hall | 35, 37 | предложение → `…-618-george-locksley-hall` |
| Arkham Map by Joe Rossomanno | 36 (46) | не взято повторно — см. ниже |
| Orne Library | 37 | предложение → `coc:location:orne-library` |
| The Restricted Collection | 37 | `location/orne-restricted-collection` |
| The Quad And Copley Memorial Bell Tower | 38 | `location/university-quad`; предложение → `…-615-copley-memorial-bell-tower` |
| Statue Lawn | 38 | предложение → `…-616-statue-lawn` |
| Robert Carter Memorial Hall | 38 | предложение → `…-614-robert-carter-memorial-hall` |
| West Dormitory / East Dormitory / Dorothy Upman Hall | 38 | предложения → 617, 620, 619 |
| Derby Hall / President’s House | 39 | предложения → 621, 622 |
| Player Handouts (собранные раздатки и карты) | 40–49 | картинки раздаток 8–12; источники карт |

Ключ карты кампуса: номерам без записи в базе заведены места `university-quad` (A), `medical-student-accommodation` (ε),
`garden-cafe` (4), `pauls-steak-house` (6), `delta-phi-house` (9), `sigma-phi-house` (10), `campus-store` (11),
`walgreens-drugs` (13), `book-nook` (14), `newport-creamery` (19); остальные метки — на общие записи Аркхэма.

## Не взято

- Эпиграфы (Лавкрафт, «Сны в ведьмином доме», с. 4; описание Аркхэма из Лавкрафта, с. 34) — литературные цитаты без игрового содержания.
- «Arkham Map by Joe Rossomanno» (с. 36, 46) — та же художественная карта, что в «Книге хранителя»; уже картинка `coc:location:arkham` (Р-249).
- Ресторан «Регата» (Гиббонс играл там на фортепиано, с. 8) и гора Ред-Рок в 8 км к югу от Браттлборо (ложное место находки руды, раздатка 9) — только упоминания, записей нет (кандидаты в записи; Вермонт — область части world).
- Атмосферных картинок в месяце 2 нет (обложка — текст и логотип Chaosium); копии раздаток в тексте глав (с. 14–16, 19–20) не брались — картинки взяты из собранных раздаток (с. 40–45).
- Книги Мифов Закрытого собрания (с. 37) — ссылки на общие записи из `orne-restricted-collection`, копии в `copies` не предлагались (книга даёт только названия «в разное время»).

## Опечатки и противоречия книги (в errata записей)

- Раздатки 11 и 12: в собранных раздатках подписи перепутаны (с. 44–45); в главе (с. 16) письмо из стола названо раздаткой 8, записка в дневнике — раздаткой 9.
- Ссылка «Appendix B: Personalities and Monsters» (с. 6) — статблоки в приложении A.
- Группа у Лирмонта: с. 9 — Блок, Хиггинс, Тёрбер; с. 12–13 — Ноукс, Хиггинс, Тёрбер.
- «Devine»/«Divine» (с. 5–6); «Professor Harold» вместо Harrold (с. 9, 12, 23); «Javis» (с. 7, 18) — словесные.
- Декан «Marinus Bickness» (с. 4, 28) — в путеводителе «Аркхэм» Маринус Брикнелл; президент «Dr. David Addleson» (с. 5) против «President Wainscott» (с. 39).
- Эйкли: Credit Rating 22% и 75% (с. 31); Людендорф: Library Use 60% и 50% (с. 32).
- Джарвис: Dodge 65% (16/6) — доли исправлены на 32/13 (Р-77); MP 12 при POW 110* (текст с. 18 согласуется с 12); Climb 60% против 50% во врезке погони.
- Людендорф: DEX 70 / Climb 70% против DEX 55 / Climb 50% во врезке (с. 23); Тьюнс: Climb 25% против 20%; Осборн: Drive Auto 50%, DEX 65 против 40%, 70 во врезке машин (с. 28).
- Смит: Brawl 1D3 + 1D4 при DB 0. Кларк: HP 16 (по ВЫН и ТЕЛ 15,5).
- Машина Блока: «1926 Buick Model 50» (с. 27) и «Buick Model D-45» (с. 28); водитель машины Харролда — Джарвис, хотя он в команде лаборатории.
- «Appellation Mountains» (с. 13) против Зелёных гор на вырезке; семья Кларков «найдена через три дня» (с. 10) против «убиты больше недели назад» (раздатка 10).
- Врезка Уилмарта (с. 10): «Akeley traveled to Vermont to see his friend Henry Akeley» — по смыслу Уилмарт; возраст Уилмарта 52 против 37 в путеводителе «Аркхэм».
- Старое лесное кладбище «на юго-восточной стороне Аркхэма» (с. 22) против Торгового района (запад) в путеводителе.
- Мемориальный корпус Картера назван в честь «деда» Рэндольфа Картера (в путеводителе — прадеда); штаб «Марширующих Мисков» — в его подвале (в путеводителе — отдельное здание 606).
- «11–12 p.m.» (с. 24) — время пробуждения после амнезии; на карте — «Copely», «Antropology», «Miskatonic Universaity» (с. 47).
- Автор «Demonality» напечатан как «Sinistari».

## Термины (английский → русский)

| English | Русский |
|---|---|
| A Time to Harvest | «Время жатвы» |
| Harvest Papers N | Раздатка «Жатва» N |
| mind swop (agent) | агент ми-го (в теле …) |
| the Fungi | Грибы |
| brain cylinder | мозговой цилиндр |
| Electric Gun | электропушка |
| Mist Projector | распылитель тумана |
| Spore Gun | споровое ружьё |
| Sonic Emitter | звуковой излучатель |
| Amnesia Enzyme | фермент амнезии |
| Pasquallium / Pasqualle Ore | паскуаллий / руда Паскуалле |
| Federated Oil and Chemical (FOC) | «Федерейтед Ойл энд Кемикал» (FOC) |
| Alter Reality | Изменение реальности |
| Go Unseen | Незримость |
| Send Nightmare | Насланный кошмар |
| Telekinesis (Jarvis) | Телекинез |
| Restricted Collection | Закрытое собрание |
| Science Hall / Charles Tyner Science Annex | Научный корпус / Научный флигель Чарльза Тайнера |
| Hangman’s Hill / Old Wooded Graveyard | Висельный холм / Старое лесное кладбище |
| Safe House | дом-убежище агентов |
| Dean of Students | декан по делам студентов |
| Know roll / Hard CON roll | проверка Знаний / трудная проверка ВЫН |
| Chase | погоня |
| Bash Heads (Harden) | «Бить по головам» (без механики, Р-126) |
| Aylesbury Pike | Эйлсберийская дорога |
| Henry Akeley, Keith Clark, Daphne Devine, Lawrence Jarvis, Gustav Ludendorff, Clayton Osborne, Wesley Smith, Robert Tunes | Генри Эйкли, Кит Кларк, Дафна Девайн, Лоуренс Джарвис, Густав Людендорф, Клейтон Осборн, Уэсли Смит, Роберт Тьюнс |
| Sam Flanaghan, Mona Learmonth, Emelda Cratchett, Lou Ann / Simon / Samuel Clark, James Harden, David Addleson | Сэм Флэнаган, Мона Лирмонт, Эмельда Кратчетт, Лу Энн / Саймон / Сэмюэл Кларк, Джеймс Харден, Дэвид Эдлсон |
