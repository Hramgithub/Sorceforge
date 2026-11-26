# Covert Actions, миссии 4–6 (часть covert-b) — сверка покрытия

Книга `wwc-covert-actions-en` (World War Cthulhu: Cold War — Covert Actions, Cubicle 7, 2017), физ. с. 93–175.
Печатная страница = физической (смещение 0): «94» на физ. 94, «131» на физ. 131, «171» на физ. 171; титулы глав
(93, 121, 148) без номера. Записи — `kb/books/wwc-covert-actions-en/`, 228 файлов: сценарии 3, сцены 49, персонажи 77,
существа 5, места 46, предметы 28, раздатки 8, организации 7, правила 2, книги Мифов 2, карта 1. Картинки — 50
(`art-covert-b.json`, `art2-covert-b.json`), карта `app/maps/wwc-covert-b-pin-eb.jpg`.

## Глава 4 «Guardians of the Forest» (с. 93–120) → `scenario/guardians-of-the-forest`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter Four (титул) | 93 | сценарий (источник); картинка — атмосфера |
| Guardians of the Forest / Introduction | 94 | `scenario/guardians-of-the-forest` (summary, keeper_info) |
| Background; East Timor in 1975 | 94 | сценарий keeper_info; `location/forest-suai` |
| The Mason Expedition | 94 | `organization/mason-expedition`; сценарий |
| The Briefing; Operation Glyndwr | 94–96 | `scene/forest-operation-glyndwr`; `location/forest-raf-shek-kong` |
| Questions and Answers | 96 | `scene/forest-operation-glyndwr`; персонажи экспедиции (`character/bertrand-mason` и др.) |
| Equipment for the Mission | 96 | `item/forest-cover-equipment` |
| Optional Encounter: “Tommy” Ng; Tommy Ng, Communist Agent | 96–97 | `scene/forest-tommy-ng`; `character/tommy-ng` |
| Darwin | 97 | `scene/forest-darwin` |
| Pat Tully, ASIS Agent | 97–98 | `character/pat-tully` |
| The Kuru | 98–99 | `location/forest-kuru` |
| Tully’s Briefing | 99 | `scene/forest-darwin`; `item/forest-planted-documents`; `character/bambang` |
| Suai | 99 | `location/forest-suai`; `scene/forest-suai-arrival` |
| Fretilin Offices | 99 | `location/forest-fretilin-offices`; `item/forest-fretilin-membership-list`; `organization/fretilin` |
| Military Headquarters | 99–100 | `location/forest-military-headquarters` |
| Captain Nantes, Garrison Commander | 100 | `character/captain-nantes` |
| East Timorese Soldiers/Militia | 100 | `character/forest-east-timorese-soldiers` |
| Asking about the Mason Expedition | 100–101 | `scene/forest-asking-about-mason` |
| Gil Sarmento; Gil Sarmento, Retired Postal Clerk | 101–102 | `character/gil-sarmento`; `location/forest-gil-sarmento-house` |
| Arrival of the Indonesians | 102 | `scene/forest-arrival-of-indonesians`; `organization/abri` |
| Colonel Yati Caniago | 102–103 | `character/yati-caniago` |
| Captain Susilo | 103–104 | `character/susilo` |
| Indonesian Soldiers | 104 | `character/forest-indonesian-soldiers` |
| Persuading Americo | 104–105 | `scene/forest-persuading-americo` |
| “He Wasn’t Cooperating, So I Shot Him!” (врезка) | 104 | `scene/forest-persuading-americo` (mechanics); `item/forest-americo-journal` |
| Leni Americo | 105 | `character/leni-americo` |
| Americo’s Story | 105–106 | `scene/forest-persuading-americo` |
| Optional Encounter: Ran Ningsheng; Ran Ningsheng | 106–107 | `scene/forest-ran-ningsheng`; `character/ran-ningsheng` |
| Indonesian Pursuit | 107 | `scene/forest-welcome-to-the-jungle`; `character/forest-indonesian-soldiers` |
| Fretilin Guerrillas | 107–108 | `character/forest-fretilin-guerrillas` |
| Welcome to the Jungle | 108 | `scene/forest-welcome-to-the-jungle`; `location/forest-mountain-jungle` |
| Boundary Marker; The Rock Face | 108 | `scene/forest-welcome-to-the-jungle` |
| The Nomads; Nomad, Age 15–30 | 108–109 | `character/forest-nomads` |
| Taga | 109 | `location/forest-taga-lands`; `organization/taga`; `scene/forest-taga-territory` |
| Getting Lost | 109 | `scene/forest-taga-territory`; `location/forest-taga-lands` (keeper_hint) |
| The Hunter; Taga Hunter, Age 22 | 109–110 | `scene/forest-taga-territory`; `character/lo-kan`; `item/forest-henderson-knife` |
| Banzai | 110 | `scene/forest-taga-territory`; `creature/ti-taki-ti` (legend) |
| Sudden Storm | 111 | `scene/forest-taga-territory` |
| Ba Beng | 111–112 | `scene/forest-ba-beng`; `character/ba-beng` |
| Taga Village | 112 | `scene/forest-taga-village`; `location/forest-taga-village` |
| Taga Guards/Hunters | 112–113 | `character/forest-taga-hunters`; `item/forest-mud-helmets` |
| Ta Tok, the Chief | 113–114 | `character/ta-tok`; `item/forest-enchanted-spear` |
| Taga Women and Children | 114 | `character/forest-taga-women-and-children` |
| Ti-Taki-Ti Manifestation; Ti-Taki-Ti Tentacles (4) | 114–115 | `creature/ti-taki-ti` (statblock, abilities); `scene/forest-taga-village` |
| The Box Canyon; Taga Guards | 115–116 | `scene/forest-box-canyon`; `location/forest-box-canyon`; `character/forest-taga-temple-guards` |
| The Temple to Ti-Taki-Ti | 116 | `scene/forest-temple`; `location/forest-temple-of-ti-taki-ti` |
| Return to Suai; Hunter Ambush; Ti-Taki-Ti’s Servants; Rainstorm; Ti-Taki-Ti’s Revenge; Ti-Taki-Ti Manifestation; Indonesian Patrol | 117–118 | `scene/forest-return-to-suai`; `creature/forest-snake`; `coc:creature:byakhee` |
| Death Town | 118 | `scene/forest-death-town`; `location/forest-suai` (history) |
| Extraction | 118 | `scene/forest-extraction` |
| A Twist (or Two) in the Tale; Americo the Traitor; Guardians of the Forest; Not All Are Victims | 118–119 | `scene/forest-twists`; `character/leni-americo` (secret); `organization/taga` (goals) |
| Mason Expedition Traitor, Age 60+ | 119 | `character/mason-expedition-traitor` |
| Ti-Taki-Ti | 119–120 | `creature/ti-taki-ti` |
| The Diary | 120 | `item/forest-mason-diary`; `handout/forest-diary-entry` |
| Call / Dismiss Ti-Taki-Ti | 120 | сценарий keeper_info; черновик `new-shared-spells-covert-b.json` (`coc:spell:call-dismiss-ti-taki-ti`) |
| Sanity & Trust Rewards | 120 | сценарий conclusion |

## Глава 5 «Operation Header» (с. 121–147) → `scenario/operation-header`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter Five (титул) | 121 | сценарий (источник); картинка — атмосфера |
| Operation Header / Introduction | 122 | сценарий summary, keeper_info |
| Official Briefing | 122 | `scene/header-official-briefing`; `character/rickinson` |
| Investigators from Other Agencies (врезка) | 123 | `scene/header-official-briefing` |
| Operation Header Briefing | 123–124 | `scene/header-official-briefing` |
| Crew of PIN-EB | 124–125 | `handout/header-crew-files`; 28 персонажей экипажа |
| The DEW Line | 125 | `location/header-pin-eb` (history) |
| N’s Mission | 125–126 | `scene/header-n-mission`; `item/header-genealogy-envelope` |
| H’s Mission; A Voice from the Realm of Dreams (врезка) | 126 | `scene/header-h-mission`; `handout/header-h-dream` |
| Getting to PIN-EB | 126 | `scene/header-getting-to-pin-eb`; `location/header-summer-queen` |
| Layovers | 126–127 | `scene/header-getting-to-pin-eb`; `character/guy-cote`, `character/abram-hedstrom`, `character/josette-dore` |
| The Helicopter Crew; Nick Boulet; Tony Giacoletto | 127–128 | `character/nick-boulet`, `character/tony-giacoletto` |
| What Happened at PIN-EB | 128–129 | сценарий keeper_info; `creature/adlet` (legend) |
| The Adlets | 129 | `creature/adlet` |
| PIN-EB | 129–130 | `location/header-pin-eb`; `location/header-victoria-island` |
| Outside | 130 | `scene/header-pin-eb-outside`; `location/header-pin-eb` |
| The Main Hub; Offices | 130 | `location/header-main-hub`, `location/header-offices`; `item/header-codebooks-safe`, `item/header-olsen-personnel-file` |
| план «PIN-EB» (ключ 1–15) | 131 | `map/header-pin-eb` (46 меток) |
| Recreation Room; Dinning Room; Kitchen; Exercise Room | 131–133 | `location/header-recreation-room`, `-dining-room`, `-kitchen`, `-exercise-room`; `scene/header-main-hub`; `item/header-adlet-corpse` |
| Setting the Mood (врезка) | 132 | `location/header-pin-eb`; `scene/header-pin-eb-outside`; сценарий advice |
| Medical Bay | 133 | `location/header-medical-bay` |
| The Barracks | 133 | `location/header-barracks`, `location/header-bathroom`; `scene/header-barracks` |
| The Radio Wing | 133 | `location/header-radio-wing`; `scene/header-radio-and-radar-wings` |
| The Polar Bear (врезка) | 134 | `creature/header-polar-bear`; `scene/header-polar-bear` |
| Last Words (врезка) | 134 | `handout/header-last-words` |
| Radar Wing | 134–135 | `location/header-radar-wing`; `item/header-radar-tapes` |
| Maintenance Wing; Storage; Machinery; Motor Pool | 135 | `location/header-maintenance-wing`, `-storage`, `-machinery`, `-motor-pool`; `item/header-gun-cabinet`; `scene/header-maintenance-wing` |
| Following the Adlets’ Trail | 135 | `scene/header-following-trail` |
| John Olsen, Chosen One of Ithaqua | 136–137 | `character/john-olsen`; `scene/header-olsen-returns` |
| Surviving Crew of PIN-EB; How to Use the Survivors (врезка) | 137 | `scene/header-survivors` |
| Irma Barton; Lee-Ann Cooper; Philip Espinoza; Luke Huff; Patrick O’Neil; Edmund Pinafore; Eric Pope; Hugo Salazar; Karl Sanderson; Henry Winkle | 137–144 | `character/irma-barton`, `lee-ann-cooper`, `philip-espinoza`, `luke-huff`, `patrick-oneil`, `edmund-pinafore`, `eric-pope`, `hugo-salazar`, `karl-sanderson`, `henry-winkle`; `item/header-sanderson-codebooks` |
| The Adlet Return | 144 | `scene/header-adlet-return` |
| The Curse of the Wendigo (врезка) | 145 | `rule/curse-of-the-wendigo` |
| Adlet Warrior; Adlet Shaman | 146 | `creature/adlet` (statblock + variants) |
| The Second Raiding Party; Running the Raid; How to Stop Them | 147 | `scene/header-adlet-return`; `scene/header-olsen-returns` |
| The Debriefing | 147 | `scene/header-debriefing` |
| Sanity & Trust Rewards | 147 | сценарий conclusion |

## Глава 6 «The Unclean» (с. 148–172) → `scenario/the-unclean`

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter Six (титул) | 148 | сценарий (источник); картинка — атмосфера |
| The Unclean (эпиграф); Introduction | 149 | сценарий summary, keeper_info |
| Keeper’s Background | 149 | сценарий keeper_info; `organization/unclean-death-cult`; `character/botanist-x`, `character/pyotr-kuznetsov`, `character/anton-kostin` |
| Briefings; Intelligence Briefing | 150 | `scene/unclean-intelligence-briefing` |
| Why You Should Never Use a Non-Secure Line (врезка) | 150 | `scene/unclean-intelligence-briefing` (mechanics) |
| Section 46 Briefing | 150 | `scene/unclean-section-46-briefing` |
| The KGB versus the MVD | 150–151 | сценарий keeper_info |
| Locations; Moscow | 151 | сценарий advice; места `part_of` `coc:location:moscow` |
| Abramov’s Office | 151, 158–160 | `location/unclean-abramov-office`; `scene/unclean-abramov-office` |
| Embassies | 151 | `location/unclean-us-embassy`, `location/unclean-uk-embassy` |
| Lubyanka | 151 | `location/unclean-lubyanka` |
| Rail Yard | 151 | `location/unclean-rail-yard` |
| Samizdat Printing Press | 152 | `location/unclean-samizdat-press` |
| Aganin’s Dacha | 152 | `location/unclean-aganin-dacha` |
| USSR Economic Achievement Exhibit | 152–153 | `location/unclean-vdnkh`, `unclean-vostok-plaza`, `unclean-cosmos-pavilion` |
| Black Flies (врезка) | 152 | сценарий advice; `creature/koschei-chort` (abilities) |
| Leaving the Embassy | 152–153 | `scene/unclean-leaving-the-embassy` |
| The Trap | 153 | `scene/unclean-exhibit-trap` |
| Major Gennady Timurovitch Aganin | 153–154 | `character/gennady-aganin` |
| Searching the Exhibit | 154 | `scene/unclean-exhibit-trap` |
| Kostin Taken; Kostin Saved; Kostin’s Clues | 154–155 | `scene/unclean-exhibit-trap`; `item/unclean-kostin-scratching`, `item/unclean-abramov-address-scrap` |
| Katya Stefanovna Merkulova, KGB assassin | 155–156 | `character/katya-merkulova`; `organization/unclean-cult-of-the-red-tsar` |
| Other Clues | 156, 158 | `scene/unclean-exhibit-trap`; `item/unclean-katya-calling-card` |
| How the KGB Reacts (врезка) | 156 | `scene/unclean-kgb-hunt` |
| Public Transportation (врезка) | 157 | сценарий tables «Общественный транспорт Москвы» |
| Finding Adder | 158 | `scene/unclean-finding-adder`; `location/unclean-novodevichy-cemetery` |
| Michael “Mikhail” Abramov | 158–159 | `character/michael-abramov` |
| Hiding Kostin; Clues | 159–160 | `scene/unclean-abramov-office`; `item/unclean-abramov-warrant`, `unclean-abramov-notebook`, `unclean-aganin-photos` |
| Additional Names (врезка) | 160 | сценарий tables «Дополнительные имена» |
| The Railyard | 160–161 | `scene/unclean-railyard`; `character/unclean-mvd-pavel-and-dmitriy` |
| Under the Tarps; What Magda Knows; Other Clues | 161 | `scene/unclean-railyard`; `character/magda-kuznetsova`, `leon-kuznetsov`, `pyotr-kuznetsov` |
| The Infection (врезка, таблица Jump/POT) | 162 | `rule/unclean-infection` |
| The Kuznetsov Apartment | 162–163 | `location/unclean-kuznetsov-apartment`; `scene/unclean-kuznetsov-apartment`; `item/unclean-pik-pamphlets` |
| Grandfather | 163 | `scene/unclean-kuznetsov-apartment` |
| Koschei/Chort; Special Powers; Koschei/Chort, Legacy of a Time Long Ago | 163–164 | `creature/koschei-chort` |
| Ilya Dmitrovich Kuznetsov, Victim of Corruption | 164 | `character/ilya-kuznetsov` |
| Other Clues | 164 | `item/unclean-burned-bessmertny`, `item/unclean-press-key` |
| Research | 164–165 | `scene/unclean-research`; `location/unclean-historical-library`, `unclean-academy-library` |
| The Unclean (врезка) | 165 | сценарий advice; `creature/koschei-chort` (encounters) |
| Tomb of the Unknown Soldier | 165–166 | `location/unclean-tomb-of-the-unknown-soldier`; `scene/unclean-tomb`; `item/unclean-western-agents-list` |
| The Return of Merkulova | 166 | `scene/unclean-finding-adder` |
| Meeting Fifka; Fifka, Phantom deal broker | 166–167 | `scene/unclean-meeting-fifka`; `character/fifka`; `location/unclean-bolshaya-ordynka-bridge` |
| Meeting Arkhiv | 167 | `scene/unclean-meeting-arkhiv`; `organization/unclean-arkhiv-collective` |
| The Samizdat | 167–168 | `scene/unclean-samizdat`; `item/unclean-bessmertny-sheets` |
| Arkhiv Attacks; Arkhiv; Kniga and Slovo | 168 | `scene/unclean-samizdat`; `character/arkhiv`; `character/kniga-and-slovo` |
| The Dacha | 169 | `scene/unclean-dacha`; `character/unclean-kgb-agents` |
| The Bathhouse | 169 | `scene/unclean-bathhouse`; `location/unclean-koschei-bathhouse`; `item/unclean-koschei-heart` |
| Aftermath | 169 | сценарий conclusion |
| Tomes; Bessmertny (Deathless); On Spoiling | 169–170 | `tome/bessmertny`; `tome/on-spoiling` |
| Spells; Ubytsa Mertvykh (Dead Slayer) | 170 | `scene/unclean-bathhouse`; черновики `coc:spell:ubytsa-mertvykh`, `coc:spell:corruption-of-chort` (`new-shared-spells-covert-b.json`) |
| Handouts #1–#4 | 171–172 | `handout/unclean-handout-1-aganin-dossier`, `-2-kostin-dossier`, `-3-merkulova-dossier`, `-4-fifka-note` |
| Index | 173–175 | не взято — указатель книги (нет содержания) |

## Не взято

- Указатель (с. 173–175) — навигация книги, своего содержания нет.
- Безымянные эпизодические фигуры только внутри сцен, без записей: армейский майор и сержант в Шекконе, «служащий BOAC»,
  второй австралийский агент на «Куру», экипаж «Куру» (8 моряков), почтовые служащие Суаи, отец Жаня Ниншэна,
  индонезийский генерал, агент N на Тиморе, курьер N в фланелевом костюме, шпион адлетов, ночной дежурный центра,
  мальчишка-посыльный Фифки — у них нет ни статблока, ни своих черт (книга называет их одной ролью мимоходом).
- Предки Олсена, упомянутые только в генеалогии (Мари Калверт, Эли и Жиль Коте, Сабина, Патриция, Ив) — текстом в
  записях Ги Коте, Абрама Хедстрома, Жозетты Доре; Юрий Андропов, Феликс Дзержинский — текстом в «Лубянке».
- Павильон химической промышленности, Мичуринский сад, обелиск «Покорителям космоса», телебашня, почта Суаи — текстом
  в записях мест ВДНХ / Суаи (сюжетной роли отдельной нет).
- Оформление: фоны врезок, эмблемы НАТО, титульные силуэты глав, атмосферные полосы — `atmosphere-covert-b.json`.

## Опечатки и противоречия книги (в `errata` записей)

- Аганин: возраст 52 против «Born 1938» в раздатке 1.
- Меркулова: судьба отца (психбольница / похоронен / «уже был мёртв»), смерть родителей 12 или 16 лет назад; «Доверие
  (КГБ) 70% (35/4)» — исправлено (35/14).
- Костин: кодовое имя «Buyan» / «Buyun».
- Пинафор: 46 (статблок) / 45 (текст, список экипажа).
- Эспиноза: «Esperanza» (с. 130), «Ezpinoza» (с. 138), «Phillip» (с. 124). Водри: «Vawlrey» (с. 131).
- Купер: Уклонение 28% и 22% в одном статблоке. Салазар: «Brawl 25% (23/9)» (доли от 45–46%; Р-77).
- Сандерсон: «big, meaty», но ТЕЛ 40. Жань Ниншэн: навык без названия «12%» и «Fist/Punch 30%».
- Проклятие вендиго: «APP −50» дважды. Змея: урон «1D6+1–1D4 + 2D10 poison». Фифка: БкУ в атаках при «DB: None».
- Кощей/Чёрт: Комплекция 3 при СИЛ+ТЕЛ 140. Книга и Слово: ПЗ 13 (по правилам 14); в тексте «Dom and Kniga».
- Ба Бенг ПЗ 16 (по правилам 14); производные значения у Америку, Салазара, Купер, Меркуловой, Уинкла, Аганина, Ильи и др.
  — в `errata` (Р-161); половины и пятые с округлением вверх по всей главе исправлены `percent_parts.py` (55 значений).
- Брифинг «CIA-SIS-CSIS» — CSIS в 1970-е ещё не было (пометка в сценарии). Библиотеки «9:00 AM to 22:00 AM».

## Термины (английский → русский)

| English | Русский |
|---|---|
| Section 46 | Секция 46 (как у cw-a) |
| N’s network | сеть N |
| Trust | Доверие |
| Tradecraft | Шпионское ремесло |
| Organization Knowledge | Знание организаций |
| Military Science | Военное дело |
| Signals | Связь |
| Command | Командование |
| Conceal | Сокрытие |
| Other Enemy | Другой Враг |
| Hide / Sneak / Move Quietly | Прятаться / Красться / Двигаться бесшумно (ссылка на «Скрытность») |
| Adlet (Adlet Warrior / Shaman) | адлет (воин / шаман адлетов) |
| Curse of the Wendigo | Проклятие вендиго |
| Ithaqua, the Wind that Walks | Итакуа, Ходящий по ветрам |
| Ti-Taki-Ti | Ти-Таки-Ти |
| Taga | тага |
| Call / Dismiss Ti-Taki-Ti | Вызов/изгнание Ти-Таки-Ти |
| mud helmet | глиняный шлем |
| Koschei/Chort | Кощей/Чёрт |
| Koschei the Deathless | Кощей Бессмертный |
| Bessmertny (Deathless) | «Бессмертный» |
| On Spoiling | «О порче» |
| Ubytsa Mertvykh (Dead Slayer) | «Убийца мёртвых» |
| Corruption of Chort | Порча Чёрта |
| The Infection | Заражение порчей Кощея |
| unclean dead | нечистый покойник |
| volkhv | волхв |
| The Unclean (сценарий) | Нечистая сила |
| Guardians of the Forest | Стражи леса |
| Operation Header / “Header” | операция «Хедер» / «Хедер» |
| Operation Glyndwr | операция «Глиндур» |
| PIN-EB | PIN-EB |
| DEW Line | линия DEW (дальнего раннего предупреждения) |
| Fretilin / UDT / ABRI | ФРЕТИЛИН / ТДС / АБРИ |
| Adder / Buyan / Chemist / Dread | «Гадюка» / «Буян» / «Химик» / «Ужас» |
| militsiya (MVD) | милиция (МВД) |
| USSR Economic Achievement Exhibit | Выставка достижений народного хозяйства (ВДНХ) |
| samizdat | самиздат |
| Hard / Extreme / Difficult / Average | трудная / чрезвычайная / трудная / обычная проверка |

## Ссылки на записи других частей (по схеме линейки)

`wwc-cold-war-en/organization/section-46`, `/organization/n`, `/character/h`, `/organization/cia`, `/organization/kgb`,
`/organization/mi6`, `/organization/asis`, `/organization/central-investigation-department`, `/organization/five-eyes`,
`/rule/trust`, `/rule/tradecraft`, `/rule/debriefings` — все уже есть. Профили «Soldier (Recruit/Regular)», «Terrorist
Guerrilla Fighters», «KGB/MVD officer» (с. 131 основной книги) — только текстом: id у части cw-b ещё нет.
