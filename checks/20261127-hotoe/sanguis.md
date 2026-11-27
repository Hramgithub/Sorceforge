# HOTOE, Book III — «Sanguis Omnia Vincet: Constantinople 330» (часть sanguis)

Книга `hotoe-book-3-en`, с. 165–202, 264–267; Book VI с. 121–124, 157, 159, 161; Keeper Maps лист 15, Player Maps лист 10.
Этап `hotoe-book-3-en/scenario/sanguis-omnia-vincet` (13, необязательный, 330 год, `axes.era` ["other"]). Генератор — `.cache/lead-tools/gen-hotoe-sanguis/`
(`gen_places.py`, `gen_people.py`, `gen_scenes.py`, `gen_misc.py`, `maps_img.py`, `art_map.py`; вырезки картинок — `art-sanguis-boxes.json`).

## Записи (100)

- Этап: 1 (`scenarios/sanguis-omnia-vincet`).
- Сцены: 23 (`scenes/sanguis-*`).
- Места: 37 — 18 мест «Константинополь 330: …» под `coc:location:constantinople` (Августеон, Курия, Халки, Большой дворец, дворец Дафны, Ипподром, бани Зевксиппа, Милий, Преторий, форумы Константина, Тавра и Вола, колонна Константина, Акрополь, Меса, Северова стена, стена Константина) + баржа «Плетора» (`корабль`); вершина «Лидийская граница (330 год)» и под ней форпост Гилиан, временный лагерь, канава с телами, Сириндже, Алджати, Калекой (ферма, церковь), Вурский храм (проход, плато, шахта, вход, гробница, казарма, кладовая, главный зал, внутреннее святилище).
- Персонажи: 24 — Тиллий Корв (человек + вариант «византийский вампир»), Алексий Гемелл, Курион Лонгин, Абракс, Христанос, Пилатос, Йенци, Незсо, Лиция, Лоренц, Набадиас, Евдокия, Теодорих, Симеон, Рикимар, Адосина, Унвен Га-Валит, профиль «Культист Освежёванных» (имена придуманы, Р-151); 6 прегенов (`pregen`): Азиний Равила, Беласир из Тихамы, Даманаис из Саварии, Эмерик из свевов, Милоний Канми, Галерий Эводис.
- Существа: 5 — филл, гриммита, Мустригг, живые шкуры, Шкура Унвена.
- Организации: 2 — Освежёванные (с Армией кожи и крови), Фортес Фальконес.
- Правила: 2 — «Валерианова чума», «Римские вспомогательные войска начала IV века» (таблица доспехов).
- Раздатка: 2 — Константинополь 330, раздатки 1 и 2.
- Карты: 4 — Константинополь 330 (Хранитель, 20 меток; игроки, 19 меток), Лидийская граница (9), Вурский храм (15); картинки `app/maps/hotoe-sanguis-*.jpg`.
- Картинки: 10 (`art-sanguis.json` → `art-sanguis-proposals.json`, применены к своим записям); атмосфера — 7 страниц (`atmosphere-sanguis.json`).
- Предложения: `proposals-sanguis.json` — 26 (Константинополь: абзацы эпохи 330 в description/history, 5 источников, 3 ссылки, псевдоним; Феналик: абзац происхождения и 3 источника; Братья кожи; Бескожий; вур; Мимс Сахис кампании; архив Ордена Благородного Щита — название рукописи). Пробный прогон `apply.py --dry-run` — все 26 ложатся.
- Черновик общего города: `new-shared-locations-sanguis.json` — Кизик (`coc:location:cyzicus`).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Constantinople 330: Sanguis Omnia Vincet (подзаголовок, автор) | 165 | `scenario/sanguis-omnia-vincet` (summary) |
| 10 March, 330 AD | 165 | сцена `sanguis-investigators-introduction`; `organization/sanguis-fortes-falcones` |
| This Historical Scenario is Optional (врезка) | 165 | этап, advice |
| About the Scenario | 165–166 | этап, summary |
| Magister Militum Alexius Gemellus (подпись к портрету) | 165 | `character/alexius-gemellus` (портрет) |
| It is Written | 166 | этап, keeper_info |
| The Investigators | 166 | этап, advice; прегены |
| Keeper's Information | 166–167 | этап, keeper_info; `organization/sanguis-the-flayed` |
| Further Reading (врезка) | 166 | этап, advice |
| Tribuni Comites Tillius Corvus (подпись к портрету) | 166 | `character/tillius-corvus` (портрет) |
| Constantinople 330 Handout #1 — The Accounts of Tillius Corvus: Introductory Handout | 167 | `handout/sanguis-handout-1-accounts-introductory` (+ Book VI с. 121) |
| Using This Scenario with the 1923 Campaign; Handouts for 1920's Investigators (врезка) | 167 | этап, hook; раздатки 1–2 |
| The Elite of Fortes Falcones | 167 | `organization/sanguis-fortes-falcones` |
| The Accounts of Tillius Corvus: Summary Handout (Constantinople 330 Handout #2) | 168 | `handout/sanguis-handout-2-accounts-summary` (+ Book VI с. 123) |
| Tribuni Comites Tillius Corvus (врезка) | 168–169 | `character/tillius-corvus` |
| Roman Auxiliary Troops of the Early 4th Century (врезка с таблицей) | 169 | `rule/sanguis-roman-auxiliary-troops` |
| Constantinople — Investigators' Introduction | 169 | сцена `sanguis-investigators-introduction` |
| Карта Constantinopolis — Nova Roma (ключ I–XIV) | 170 | `map/sanguis-constantinople-330`, места I–XIV |
| The Curia | 170–171 | сцена `sanguis-the-curia`; место `sanguis-curia` |
| Nova Roma (Constantinople) (врезка) | 171 | предложение абзаца эпохи 330 к `coc:location:constantinople`; этап, advice |
| Welcome to the Byzantine Period (врезка) | 171 | предложение `history` Константинополя; этап, advice |
| A Meeting with the Magister Militum | 171 | сцена `sanguis-meeting-the-magister-militum` |
| Constantinople (врезка-список мест) | 172 | 17 мест «Константинополь 330: …»; таблица этапа «Нова Рома: места города (330 год)» |
| Conversation about the Crisis in Lydia | 172 | сцена `sanguis-meeting-the-magister-militum` (пункты «•») |
| Christianity and Constantine (врезка) | 173 | этап, advice; предложение Константинополю |
| Final Preparations; Setting Out | 173 | сцена `sanguis-final-preparations` |
| The Crisis in Lydia | 173–174 | место `sanguis-lydian-frontier` |
| Cyzicus | 174 | сцена `sanguis-cyzicus`; черновик `coc:location:cyzicus` |
| Карта The Lydian Frontier | 174 | `map/sanguis-lydian-frontier` |
| Running Tribuni Comites Tillius Corvus (врезка) | 175 | этап, advice; `character/tillius-corvus` (legend) |
| Secrecy | 175 | сцена `sanguis-cyzicus` |
| The Road To Ghilian; On the Outskirts | 175 | сцена `sanguis-road-to-ghilian` |
| The Ghilian Outpost | 175 | место `sanguis-ghilian-outpost` |
| The Valerian Plague: Rules, Symptoms, Fatality (врезка) | 176 | `rule/sanguis-valerian-plague` |
| The Garrison; Meeting With Centenarius Longinus; The Garrison Commander's Report | 176–177 | сцена `sanguis-meeting-centenarius-longinus`; `character/curio-longinus` |
| Investigations | 177 | та же сцена |
| The Emergency Camp (подпись к рисунку); The Plague Camp; The Physician | 177–178 | место `sanguis-emergency-camp`; сцена `sanguis-plague-camp`; `character/abrax` (портрет) |
| Talking to the Victims; Rumors of the Valerian Plague | 178 | таблица «Слухи о валериановой чуме» у `sanguis-emergency-camp` |
| Rumors of the Flayed; Rumors of Strange Creatures | 179 | таблицы «Слухи об Освежёванных», «Слухи о странных существах» там же |
| Horror in the Plague Camp | 179 | сцена `sanguis-horror-in-the-plague-camp` |
| The Body Dump; A Closer Look; The Living Skins; The Trail of Blood | 179–180 | сцена и место `sanguis-body-dump` |
| Dozens of Corpses are Piled in the Body Dump (подпись) | 178 | атмосфера |
| The Villager's Dispute (врезка) | 180 | сцена `sanguis-villagers-dispute`; Йенци, Незсо, Лиция |
| Kalekoy | 180 | сцена `sanguis-kalekoy`; место `sanguis-kalekoy` |
| The Origins of The Order of the Flayed; The Ur-Rinna Dauthi; Weaknesses of the Ur-Rinna Dauthi (врезка) | 181 | `organization/sanguis-the-flayed`; `character/unwen-ga-walith`; существа филл, гриммита, Мустригг (способность «Солнечный свет») |
| The Road to Kalekoy; The Farm; The Young Cultists; The Army of Skin and Blood | 182 | сцена `sanguis-kalekoy`; места Сириндже, Алджати, ферма, церковь |
| The Prisoners; The Warning | 182–183 | сцена `sanguis-the-prisoners` |
| The Attack On The Ghillian Outpost; The Battle Within the Battle; Ghilian is Saved; Ghilian is Lost | 183–184 | сцена `sanguis-attack-on-ghilian-outpost`; таблица этапа «Битва за форпост Гилиан: противники каждого сыщика» |
| The Voorish Temple; The Trail | 185 | сцена `sanguis-the-trail-and-the-pass`; место `sanguis-voorish-temple` |
| Карта The Voorish Temple | 185 | `map/sanguis-voorish-temple` |
| The Pass; The Plateau; The Hole; The Barrier | 186–187 | та же сцена; места `sanguis-temple-pass`, `-plateau`, `-shaft` |
| Running the Voorish Temple (врезка) | 186 | этап, advice; сцена `sanguis-the-trail-and-the-pass` |
| Entering The Temple; The Maddening Mists; The Entrance; The Patrol; The Tomb; The Barracks; The Stores | 187–188 | сцена `sanguis-entering-the-temple`; места храма |
| The Temple; The Writing on the Walls; The Central Icon; A School of Skin; The Temple's Secrets (врезка) | 188–189 | сцена `sanguis-the-temple`; место `sanguis-temple-hall` |
| The Concealed Entrance | 189 | та же сцена и место |
| The Inner Sanctum; The Final Battle; A Hero Falls | 189–190 | сцена `sanguis-inner-sanctum`; место `sanguis-temple-inner-sanctum` |
| The Final Battle! (подпись к рисунку) | 190 | картинка у `character/unwen-ga-walith` |
| Constantinople Again | 190–191 | сцена `sanguis-constantinople-again` |
| The Grand Commencement Festival | 191–192 | сцена `sanguis-grand-commencement-festival`; таблица «Награды Рассудком» |
| What if Tillius Corvus Does Not Kill Unwen? (врезка) | 191 | сцена `sanguis-inner-sanctum`; этап, advice |
| The Invitation; Discharged, Rewards and New Assignment | 192 | сцена `sanguis-the-invitation` |
| The Wedding Cruise; The Betrayal | 192–194 | сцена `sanguis-wedding-cruise`; место `sanguis-plethora` |
| Wedding Madness! (подпись к рисунку) | 192 | картинка у `character/tillius-corvus` (облик вампира) |
| A Villain Rises (врезка) | 193 | `character/tillius-corvus` (legend); этап, keeper_info; предложение `coc:character:fenalik` |
| Conclusion; The Byzantine Vampire | 194 | сцена `sanguis-conclusion`; этап, conclusion |
| Additional Thanks (врезка) | 194 | не взято (см. ниже); источник прегенов |
| Statistics: Fill; Grimmitha | 195–196 | `creature/sanguis-fill`, `creature/sanguis-grimmitha` |
| Ricimar and Adosina, Order of the Flayed Acolytes | 196 | `character/ricimar`, `character/adosina` |
| Cultist of the Flayed | 196 | `character/cultist-of-the-flayed` |
| The Living Hides, Unwen's Art Collection (4) | 196 | `creature/sanguis-living-hides` |
| Unwen's Hide; Mustrigg; Unwen Ga-Walith | 197 | `creature/sanguis-unwens-hide`, `creature/sanguis-mustrigg`, `character/unwen-ga-walith` |
| Tillius Corvus, Byzantine Vampire; Tribuni Comites Tillius Corvus | 198 | `character/tillius-corvus` (основной статблок и вариант) |
| Investigators: The Men of Fortes Falcones — Asinius Ravila; Belasir of Tihama; Damanais of Savaria; Emeric of the Suevi; Milonius Kanmi; Galerius Evodis | 198–201 | шесть прегенов |
| с. 202 — плакат «Simplon-Orient-Express» | 202 | атмосфера |
| Constantinople Invictus Keeper's Map | 264 | `map/sanguis-constantinople-330` (источник) |
| Constantinople Invictus Players' Map | 265 | `map/sanguis-constantinople-330-players` |
| Lydian Frontier | 266 | `map/sanguis-lydian-frontier` (картинка) |
| Voorish Temple | 267 | `map/sanguis-voorish-temple` (картинка) |
| Book VI: Constantinople 330 Handout #1; Summary Handout | 121, 123 | раздатки 1–2 (картинки) |
| Book VI: Constantinople Invictus Players' Map; Lydian Frontier; Voorish Temple | 157, 159, 161 | источники карт |
| Keeper Maps, лист 15; Player Maps, лист 10 | — | картинки карт Константинополя 330 |

## Не взято

- «Additional Thanks» (с. 194): список тестировщиков, создавших прегенов (Andrew Fattorruso, Regina Mireau, Matthew Higgins, Joseph Potenza, Joel Jackel, Earl Gachan) — выходные данные, не игровой материал; страница указана в источниках прегенов.
- Book VI с. 122, 124 — пустые обороты.
- Подписи карты Константинополя без записей: Sycae, Chrysopolis, To Western Thrace, Sea of Marmara, значки легенды City gate / Sea port / City cistern; подписи Лидийской границы To Chrysopolis & Chalcedon, Trail, 963 ft, Woodland, Hills — меток нет (отдельных мест книга не описывает).
- Без отдельных записей (упомянуты текстом): судно «Андромеда» (только переход, на борту ничего не происходит), дом госпожи Евдокии, храм Святой Ирины, Стратегион, тюремное крыло с гонцом, хранилище, откуда украден нож, Сарды, Мисия; освежёванный конь Унвена (статблока нет); гонец из Гилиана и посланник Евдокии (безымянные, без действий); Нонна и Кирилл (значимые люди в предыстории Беласира); исторические лица (Константин, Диоклетиан, Лициний, Максимин Даза, Валериан, Шапур I, Констанций II, Марк Аврелий); доктор Радко Йорданов (персонаж главы «Повторное владение», записи пока нет).
- Отдельной записи Армии кожи и крови нет — она описана в организации «Освежёванные» (псевдоним).

## Опечатки и сомнения книги

- с. 183: заголовок «The Attack On The Ghillian Outpost» (Ghillian вместо Ghilian) — отмечено в сцене.
- с. 166: «Sanguius Omnia Vincet» во врезке «Further Reading» — в псевдонимах этапа.
- с. 167, 197: сценарий Винковци назван «Bread or Stone» (глава — «Bread and Stone»).
- с. 167, Book VI с. 121: «the solders face terrors» — в переводе исправлено молча (Р-39).
- с. 189: «a single robbed man» (robed); «the Mim Sahis» — словесные, в переводе исправлены.
- с. 173: «Chi-Ro» (в остальном «Chi-Rho») — в переводе «хи-ро».
- с. 267 (карта): «Voorish Heiroglyphs» — метки с подписью как напечатано.
- Book VI с. 157 называет карту игроков копией с. 170, но на с. 170 — карта Хранителя с ключом XIV (свадебная баржа); копия игроков ключа XIV не имеет.
- errata в записях: филл — СИЛ 80 при броске (3d6+6)×5 (среднее 82); ПЗ «11 - 12»; культист — Скорость 8 (по правилам 9) и Уклонение 30% (не ниже 32%); Тиллий Корв — Уклонение 32% (не ниже 35%); Азиний Равила — Уклонение 39% (20/7) → (19/7), исправлено; Беласир и Даманаис — «6-point Lorica Squamata» (по таблице 1d6); Эмерик — «7-point Lorica Hamata» (по таблице 1d8); Даманаис — Рассудок 70 при МОЩ 65.
- Без errata (как напечатано, не ошибки правил): Драка 1d4 у Равилы, Эмерика и Эводиса; гаста Даманаиса 1d6 (у Корва 1d10); возраст Даманаиса 36 по статблоку и 33 по предыстории.

## Решения и вопросы

- «Лидийская граница» — `location_type: "город сценария"`, `part_of: null`: в задании — «область» с `part_of: null`, но `tools/check.py` такого не пропускает (Р-189, Р-197); по практике (долина Северн, Гиперборея) вершина гайда для области без родителя — «город сценария». Вопрос ведущему.
- Название рукописи: здесь «Записи Тиллия Корва» (раздатки этой главы); часть zagreb-vinkovci написала «Рассказ Тиллия Корва» в `item/vinkovci-noble-shield-archives` — предложение замены в описании.
- «Повторное владение» (Repossession) — рабочий русский перевод названия главы Book IV (часть sofia ещё не записала этап); ссылка `hotoe-book-4-en/scenario/repossession` ждёт её.
- Заклинание «Blight» связано с «Погубить/благословить урожай», «Cause Blindness» — с «Наслать/исцелить слепоту»; навык «Drive» Даманаиса — с «Управление лошадью или волом» (вывод, Р-41). Навыки Cthulhu Invictus «Empire», «Civics», «Tactics», «Potions» — текстом без ссылки (Р-126).
- Метки «Chrysokeras» → Золотой Рог и «Stenon» → Босфор (места WWC под Константинополем) — вывод из названий.
- Рисунок «The Ur-Rinna Dauthi» (с. 181) — летающая кожа, отдан Мустриггу (вывод).
- Ссылки на записи, которых пока нет: `coc:location:sofia` (часть sofia), `hotoe-book-4-en/scenario/repossession` (часть sofia).

## Термины (английский → русский)

| English | Русский |
|---|---|
| Sanguis Omnia Vincet | Sanguis Omnia Vincet (без перевода) |
| Cthulhu Invictus | Cthulhu Invictus |
| Nova Roma; Nova Roma Constantinopolitana | Нова Рома; Nova Roma Constantinopolitana |
| Grand Commencement | Великое открытие |
| Fortes Falcones | Фортес Фальконес |
| Exploratores | эксплораторы |
| Tribuni Comites | трибун-комит |
| Magister Militum | магистр армии |
| Centenarius | центенарий |
| Tillius Corvus | Тиллий Корв |
| Alexius Gemellus | Алексий Гемелл |
| Curio Longinus | Курион Лонгин |
| Lady Eudocia | госпожа Евдокия |
| Abrax; Christanos; Pilatos | Абракс; Христанос; Пилатос |
| Jenci; Nezso; Licia | Йенци; Незсо; Лиция |
| Lorenz; Nabadias («Bear») | Лоренц; Набадиас («Медведь») |
| Theodoric; Symeon | Теодорих; Симеон |
| Ricimar; Adosina | Рикимар; Адосина |
| Unwen Ga-Walith (The Chosen) | Унвен Га-Валит («Избранный») |
| Asinius Ravila; Belasir of Tihama; Damanais of Savaria; Emeric of the Suevi; Milonius Kanmi; Galerius Evodis («Senilis») | Азиний Равила; Беласир из Тихамы; Даманаис из Саварии; Эмерик из свевов; Милоний Канми; Галерий Эводис («Сенилис») |
| The Flayed; Order of the Flayed | Освежёванные; Орден Освежёванных |
| Army of Skin and Blood | Армия кожи и крови |
| ur-rinna dauthi | ур-ринна даути |
| fill | филл |
| grimmitha | гриммита |
| Mustrigg | Мустригг |
| The Living Hides | живые шкуры |
| Unwen's Hide | Шкура Унвена |
| Valerian Plague | валерианова чума |
| Mims Sahis («Skin Knife») | Мимс Сахис («Нож для кожи») |
| Screaming Cut | Вопящий порез |
| Bite and Hold | укус с захватом (по глоссарию) |
| The Accounts of Tillius Corvus | «Записи Тиллия Корва» |
| Voor; Voorish temple; Voorish hieroglyphs | вур; Вурский храм; иероглифы вуров |
| The Maddening Mists | дурманящие туманы |
| The Central Icon; A School of Skin | Центральный идол; «Школа кожи» |
| Ghilian Outpost | форпост Гилиан |
| Emergency Camp; Plague Camp; Body Dump | временный лагерь; чумной лагерь; канава с телами |
| Kalekoy; Sirince; Alcati | Калекой; Сириндже; Алджати |
| Lydia; Lydian Frontier; Sardis; Cyzicus; Mysia | Лидия; Лидийская граница; Сарды; Кизик; Мисия |
| Augustaeum; Curia; The Chalke; Great Palace; Palace of Daphne | Августеон; Курия; Халки; Большой дворец; дворец Дафны |
| Hippodrome; Baths of Zeuxippus; Milion; Mese; Praetorium | Ипподром; бани Зевксиппа; Милий; Меса; Преторий |
| Forum of Constantine; Column of Constantine; Acropolis | форум Константина; колонна Константина; Акрополь |
| Forum Tauri (Forum of the Bull); Forum Bovis (Forum of the Ox) | форум Тавра (форум Быка); форум Вола |
| Severan Wall; Constantine's Wall | Северова стена; стена Константина |
| Chrysokeras; Stenon | Хрисокерас (Золотой Рог); Стенон (Босфор) |
| Haghia Eirene; Strategion | храм Святой Ирины; Стратегион |
| The Plethora; Andromeda | «Плетора»; «Андромеда» |
| Lorica Squamata; Lorica Hamata; Lorica Segmentata | лорика скваммата (чешуйчатый доспех); лорика хамата (кольчуга); лорика сегментата |
| spatha; gladius; pugio; hasta; verrutum; manuballista; composite bow | спата; гладиус; пугио; гаста; верут; манубаллиста; составной лук |
| Chi-Rho | хи-ро |
| Empire; Civics; Tactics; Potions (навыки Invictus) | Империя; Гражданские дела; Тактика; Зелья |
| Byzantine Vampire | византийский вампир |
| Repossession (глава Book IV) | «Повторное владение» (рабочий вариант) |
