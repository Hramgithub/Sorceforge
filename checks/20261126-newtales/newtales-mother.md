# New Tales of the Miskatonic Valley 2E — часть mother («A Mother's Love», с. 147–161, 178–181)

Книга `new-tales-miskatonic-valley-2e-en` (Stygian Fox, 2019), сценарий Сета Скорковски (Seth Skorkowsky), «A Tale of
Innsmouth». Смещение страниц 0 подтверждено по изображениям (с. 147, 150, 178: печатный номер = физическая страница).

Сценарий уже есть в базе по переводу владельца «Любовь матери» (`kb/books/mothers-love-ru/`, Р-223). По Р-147 второй
набор не заводился: текст остаётся у перевода, оригинал даёт источники, английские названия и сверку чисел. Новых записей
в `kb/books/new-tales-miskatonic-valley-2e-en/` эта часть не создаёт — в переводе есть всё, что есть в оригинале.

Файлы части:

- `proposals-mother.json` — 267 предложений к 65 записям (52 записи `mothers-love-ru` и 13 общих): 167 английских
  источников, 46 `name.en`, 35 замен пометки «оригинал не найден, числа не сверены» на «сверены, совпадают», 8 уточнений
  `errata` (опечатки оригинала, а не перевода), исправления раздатки H01 и легенды Уинна по оригиналу, две цитаты с
  английскими словами внутри русского текста, псевдоним «George Habbit». Пробный прогон `apply.py --dry-run` проходит.
- `art-mother.json` → `art-mother-proposals.json` (1 картинка: иллюстрация с. 148 «Мэри Сиск и маленький Тобиас» к
  `mothers-love-ru/character/meri-sisk`; копия `app/art/characters/newtales-mother-meri-sisk.webp`). Предложение не
  применено — запись принадлежит переводу, применяет ведущий.
- `atmosphere-mother.json` — 3 страницы атмосферы (с. 147, 153, 156).
- `completeness-mother/`, `scenario-mother/` — 0 находок (записей книги у этой части нет).

## Сверка чисел

Все статблоки с. 159–161 (17 профилей) сверены построчно с записями перевода и вариантами общих персонажей
(Мартин, Бёрч, Роупс, Роули, Роберт и Джейкоб Марши): характеристики, ПЗ, ПМ, БкУ, Комплекция, Скорость, Рассудок,
атаки, урон, Уклонение, навыки, броня, заклинания, потеря Рассудка, возраст — совпадают. Числа текста (суммы $6,000,
$1,200, $400/$300/$200, $2, $200; даты 5–6 апреля 1927, 20 января 1898, 1917, 1925, 1846; адреса 504 Main Street,
407 Hancock Street; 1d6 жрецов, полдюжины рабочих, 6 полицейских, 5 этажей, 23:30, 2 часа ночи, 58 лет Мойры, 26 лет
Гилмана, 6 раундов, первые 5 раундов, расстояния в метрах по Р-64, награды Рассудка) — совпадают.

Расхождения перевода с оригиналом (исправляются предложениями):

| Где | Перевод | Оригинал | Предложение |
|---|---|---|---|
| Раздатка H01, Сото | «Роберто Сото, 26» | «ROBERTO SOTO, 28» (с. 150, 178) | `text.ru` → 28, `errata.0.fixed: true` |
| Раздатка H01, Уинн | «15-летнего мальчика» | «a 13-year-old boy» (с. 150, 178) | `text.ru` → 13; в легенде Уинна — «13-летнего» |
| Агент Малоун | «Малоун» / «Мэлоун» | везде «Malone» (с. 149, 152, 159) | пометка в `errata.0.note` |
| Цитата Грейс | «Toby доверяет мне» | «Toby trusts me.» (с. 161) | → «Тоби доверяет мне» |
| Цитата Роупса (`coc:character:elliot-ropes`) | «Sisk надо было погибнуть…» | «Sisk shoulda' died…» (с. 160) | → «Сиску надо было…» |

Опечатки самого оригинала (в переводе те же; в `errata` записей уточнено, что это опечатка оригинала):

- Полиция штата/агент BOI: Ближний бой «55% (22/9)» (с. 159) — доли подходят к 45%.
- Роберто Сото: пистолет «60% (30/10)» (с. 161).
- Тедди Уинн: дробовик «40% (20/5)» (с. 161).
- Полицейская ищейка: «Sanity Loss: 1/1D6» у обычной собаки (с. 159).
- Типичный житель-гибрид: «Move: 8/8 swimming» при СИЛ и ЛВК больше ТЕЛ (с. 160).
- Мэри Сиск: возраст «9,529» (с. 161).
- Мелочи оформления (Р-39, не записаны): «Science (Chemistry), 40%» у Роули Марша, «Science (Chemistry 20%)» у
  Джейкоба Марша, «Fighting (Brawling)» у Сото, «Pirate Hideout» (карта, с. 154, 180) / «Pirates Hideout» (с. 157),
  «Thomas Haines» (с. 155) / «Tommy Haines» (надпись карты, с. 180 — уже в пометке раздатки H03), «fiancée» о Сиске.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Table of Contents: «A Mother's Love by Seth Skorkowsky» | 4 | `mothers-love-ru/scenario/lyubov-materi` (источник, автор в `summary`) |
| A Mother's Love (вступление) | 147 | `mothers-love-ru/scenario/lyubov-materi` — `summary` |
| Keeper Information (с Author's Note) | 147 | `scenario/lyubov-materi` — `keeper_info`; `organization/banda-lyagushka`, `item/sedan-dodge`, `item/dobycha-banka-ipsvicha`, `location/sklad-ueytov` |
| Investigator Information | 147 | `scenario/lyubov-materi` — `hook` |
| Background | 147–148 | `scenario/lyubov-materi` — `keeper_info`; `character/meri-sisk`, `character/tobias-sisk`, `location/piratskoe-ubezhishche`, `item/bronzovyy-kolokol`, `item/braslet-meri-sisk` |
| Creating Atmosphere | 148–149 | `scenario/lyubov-materi` — `advice`; `creature/politseyskaya-ishcheyka`; друзья Сиска — `scene/konstebli-innsmuta` |
| Иллюстрация «Мэри Сиск и маленький Тобиас» | 148 | `character/meri-sisk` — картинка (`art-mother-proposals.json`) |
| The Frog Gang | 149 | `organization/banda-lyagushka`, `handout/h01-dokumenty-byuro` |
| The Bureau of Investigation | 149 | `scenario/lyubov-materi` — `hook`; `character/dzhek-maloun`; `coc:organization:bureau-of-investigation`, `coc:organization:massachusetts-state-police` |
| The Cooperative Bank of Ipswich | 149 | `scene/ograblenie-v-ipsviche`, `location/kooperativnyy-bank-ipsvicha`, `character/dzheffri-kinsella` |
| Locating the Abandoned Car and Duncan | 149, 151 | `scene/broshennyy-avtomobil`, `item/sedan-dodge`, `character/eyb-dunkan`, `creature/khishchnyy-rakoobraznyy` |
| A Mother's Love Papers #1 | 150 | `handout/h01-dokumenty-byuro` |
| The Innsmouth Constabulary | 151 | `scene/konstebli-innsmuta`; `coc:organization:innsmouth-town-authority` |
| Chief Constable Andrew Martin | 151 | `scene/konstebli-innsmuta`; `coc:character:andrew-martin` |
| Constable Nathan Birch | 151 | `scene/konstebli-innsmuta`; `coc:character:nathan-birch` |
| Constable Elliot Ropes | 151 | `scene/konstebli-innsmuta`; `coc:character:elliot-ropes` |
| Innsmouth Police Details about Tobias Sisk | 151 | `scene/konstebli-innsmuta`, `item/svidetelstva-o-smerti-siskov`, `character/iezekiil-sisk` |
| Dr. Rowley Marsh | 151 | `scene/doktor-rouli-marsh`; `coc:character:rowley-marsh` |
| The Esoteric Order of Dagon | 152 | `scene/orden-dagona`; `coc:organization:esoteric-order-of-dagon`, `coc:character:robert-marsh` |
| The Marsh Refining Company | 152 | `scene/affinazhnyy-zavod`; `coc:character:jacob-marsh` |
| East India Marine Merchants Bank | 152 | `scene/bank-morskikh-torgovtsev` |
| The Harbor | 152 | `scene/gavan` |
| The Gilman House Hotel | 152 | `scene/otel-dom-gilmana`; `coc:character:george-hubbit`, `coc:character:charles-gilman` |
| Using the Telephone | 153 | `scene/polzovanie-telefonom`; `coc:character:moira-pierce` |
| Occurrences in Town | 153 | `scenario/lyubov-materi` — шаг «События в городе» |
| Local Children | 153 | `scene/mestnye-deti` |
| Shoggoths' Song | 153 | `scene/pesn-shoggotov` |
| Иллюстрация (стрелок над перилами, силуэты) | 153 | атмосфера — `atmosphere-mother.json` |
| Missing Policeman | 154 | `scene/propavshiy-politseyskiy` |
| Wynne's Appearance | 154 | `scene/poyavlenie-uinna`, `character/teddi-uinn` |
| The Sisk House (с рисунком Тобиаса) | 154–155 | `scene/dom-siska`, `location/dom-siska`, `handout/h02-detskiy-risunok`, `handout/h03-karta-piratskoe-ubezhishche` |
| Grace Deckert (с портретом) | 155–156 | `scene/greys-dekert`, `character/greys-dekert` (портрет уже есть из папки владельца) |
| Иллюстрация (ночная улица) | 156 | атмосфера — `atmosphere-mother.json` |
| The Hideout (с плакатом «WANTED») | 156–157 | `scene/ubezhishche`, `scene/grot-i-kolokol`, `location/sklad-ueytov`, `location/piratskoe-ubezhishche`, `item/bronzovyy-kolokol`, `item/meshok-piratskikh-sokrovishch`, `handout/h04-rozysknoy-plakat` |
| The Remaining Frog Gang: Tobias Sisk, Pearl Kammire, Roberto Soto | 158 | `organization/banda-lyagushka`, `character/tobias-sisk`, `character/perl-kammayr`, `character/roberto-soto`, `scene/ubezhishche` |
| After the Smoke Clears | 158 | `scene/kogda-dym-rasseetsya` |
| Mary Sisk's Bracelet | 158 | `item/braslet-meri-sisk` |
| Rewards and Repercussions | 158 | `scenario/lyubov-materi` — `conclusion` |
| NPCs and Monsters | 159 | `scenario/lyubov-materi` (источник) |
| Jack Malone, Senior BOI Agent, Hands-Off Supervisor | 159 | `character/dzhek-maloun` |
| Typical State Police/BOI Agent | 159 | `character/tipichnyy-politseyskiy-shtata` |
| Typical Police Bloodhound | 159 | `creature/politseyskaya-ishcheyka` |
| Carnivorous Crustacean | 159 | `creature/khishchnyy-rakoobraznyy` |
| Andrew Martin, Chief Constable, Deep One Hybrid | 159 | `coc:character:andrew-martin` — вариант «Любовь матери» |
| Nathan Birch, Wily Old Constable, Deep One Hybrid | 159 | `coc:character:nathan-birch` — вариант |
| Elliot Ropes, Brutish Constable, Deep One Hybrid | 160 | `coc:character:elliot-ropes` — вариант |
| Dr. Rowley Marsh, Rueful Physician, Deep One Hybrid | 160 | `coc:character:rowley-marsh` — вариант |
| Robert Marsh, Devoted High Priest of Dagon, Deep One Hybrid | 160 | `coc:character:robert-marsh` — вариант «Любовь матери» |
| Jacob Marsh, Friendly Refinery Manager, Deep One Hybrid | 160 | `coc:character:jacob-marsh` — вариант |
| Typical Human Resident | 160 | `character/tipichnyy-zhitel-chelovek` |
| Typical Hybrid Resident (и гибриды-жрецы) | 160 | `character/tipichnyy-zhitel-gibrid` |
| Teddy Wynne, Desperate to Escape Town | 161 | `character/teddi-uinn` |
| Grace Deckert, Scorned Lover Seeking Revenge, Deep One Hybrid | 161 | `character/greys-dekert` |
| Mary Sisk, Worried Mother, Deep One | 161 | `character/meri-sisk` |
| Tobias Sisk, Deep One Hybrid, Desperately Seeking Redemption | 161 | `character/tobias-sisk` |
| Pearl Kammire, Terrified Mother-To-Be | 161 | `character/perl-kammayr` |
| Roberto Soto, Unwilling to Surrender | 161 | `character/roberto-soto` |
| A Mother's Love Papers #1 (приложение) | 178 | `handout/h01-dokumenty-byuro` |
| Рисунок «DAddy / Me / Mommy» | 179 | `handout/h02-detskiy-risunok` |
| Карта «Pirate Hideout» | 180 | `handout/h03-karta-piratskoe-ubezhishche` |
| Плакат «WANTED» | 181 | `handout/h04-rozysknoy-plakat` |

Все записи без префикса — `mothers-love-ru/…`.

Просмотрены с. 179–193 приложения: этому сценарию принадлежат только с. 179–181 (раздатки H02–H04). Остальные — чужих
частей: с. 182 «The Varga House», с. 183 карты Аркхэма (Varga House; Washburne…), с. 184–185 маршруты по лесу,
с. 186 «Dunwich Mills and Environs», с. 187 «The 1806 Sawmill», с. 188 «The Supervisor's House», с. 189
«The Pickering Mansion», с. 190 «The Pickering Mill», с. 191 «The Old Congregates», с. 192 «The Mi-Go Cavern»,
с. 193 «The Funt House».

## Не взято

- Новых записей в `kb/books/new-tales-miskatonic-valley-2e-en/` нет: всё содержание сценария уже в записях перевода
  (Р-147); правки — предложениями.
- Карты Иннсмута в оригинале нет (ни в главе, ни в приложении): `mothers-love-ru/map/karta-innsmuta` — картинка из папки
  владельца, источника из этой книги не получает. Плана склада Уэйтов в книге тоже нет.
- Копии раздаток внутри главы (с. 150 — H01, с. 154 — H02, с. 155 — H03, с. 157 — H04) и портрет Грейс (с. 155):
  картинки у записей уже есть (из папки владельца, тот же арт); новые не добавлялись — одна картинка на запись.
- Иллюстрации с. 153 и 156 и заставка с. 147 — атмосфера (`atmosphere-mother.json`): изображённый на с. 153 книгой не
  назван (Сото или Тобиас — не угадываем).
- `name.en` не поставлено у записей без напечатанного названия: `scene/grot-i-kolokol` (часть раздела «The Hideout»),
  `location/sklad-ueytov` (книга называет только «abandoned warehouse», фамилия — с таблички), `handout/h02-detskiy-risunok`.
- Готовые сыщики перевода (`character/anzhela-beystebl`, `karl-eteridzh`, `konrad-franklin`, `otets-maykl-kalkhun`,
  `dzhonni-logan`, `roda-goldsteyn` — с. 201–236 этой книги) и газета `handout/arkham-advertiser-1928` (с. 194–199) —
  страницы части reeling; эта часть их не сверяла. Ведущему: части reeling не заводить второй набор, а дать предложения
  к этим записям `mothers-love-ru` (Р-147).

## Вопросы владельцу

- Названия заклинаний в тексте перевода оставлены по-английски («Wrack», «Breath of the Deep»), у общих записей
  заклинаний официальные русские названия — «Разрушение», «Дыхание глубин»; в глоссарии у этих терминов реестр владельца
  пустой (review). Заменить в тексте перевода на официальные формы? Предложений на это не делал — текст перевода
  владельца.
- В статблоках перевода — формы владельца «Внимательность», «Закон», «Выслеживание» (глоссарий: «не писать»; официально
  Внимание, Юриспруденция, Чтение следов). Оставлены как у владельца (решение части mothers, Р-223).

## Термины (English → Russian)

Новых терминов нет: все формы — из записей перевода владельца и общих записей (Р-184). Для переводчика книги:

| English | Русский |
|---|---|
| A Mother's Love | Любовь матери |
| A Tale of Innsmouth | Иннсмутская история (колонтитул; наш перевод) |
| Frog Gang | банда «Лягушка» |
| Tobias "Frog" Sisk / Toby | Тобиас «Лягушка» Сиск / Тоби |
| Mary Sisk | Мэри Сиск |
| Ezekiel Sisk | Иезекииль Сиск |
| Grace Deckert | Грейс Декерт |
| Thomas (Tommy) Haines | Томас (Томми) Хейнс |
| Abe Duncan | Эйб Дункан |
| Pearl Kammire | Пёрл Каммайр |
| Roberto Soto | Роберто Сото |
| Teddy Wynne | Тедди Уинн |
| Jack Malone | Джек Малоун |
| Deputy Geoffrey Kinsella | помощник шерифа Джеффри Кинселла |
| Chief Constable Andrew Martin | главный констебль Эндрю Мартин |
| Constable Nathan Birch | констебль Натан Бёрч |
| Constable Elliot Ropes | констебль Эллиот Роупс |
| Dr. Rowley Marsh / Ralsa Marsh | доктор Роули Марш / Ралса Марш |
| Robert Marsh / Barnabas Marsh / Jacob Marsh | Роберт Марш / Барнабас Марш / Джейкоб Марш |
| George Habbit / Charles Gilman | Джордж Хэббит / Чарльз Гилман |
| Moira Pierce | Мойра Пирс |
| Bureau of Investigation (BOI) | Бюро расследований |
| Massachusetts State Police | полиция штата Массачусетс |
| Innsmouth Constabulary | констебли Иннсмута (полиция Иннсмута) |
| Innsmouth Jail | тюрьма Иннсмута |
| Innsmouth Assembly Hall, Hall of Records | архив Assembly Hall Иннсмута (Ратуша — вывод) |
| Esoteric Order of Dagon | Эзотерический орден Дагона |
| Marsh Refining Company / Marsh Refinery | Аффинажный завод Марша |
| East India Marine Merchants Bank | Банк морских торговцев Ост-Индии |
| Gilman House (Hotel) | отель «Дом Гилмана» |
| Innsmouth Café | кафе «Иннсмут» |
| New Town Square | Новая городская площадь |
| Cooperative Bank of Ipswich | Кооперативный банк Ипсвича |
| Sisk House | Дом Сиска |
| Pirate(s) Hideout | «Пиратское убежище» |
| the hideout (Waite warehouse) | убежище (склад Уэйтов) |
| bronze tube bell | бронзовый трубчатый колокол |
| pirate loot | «пиратские сокровища» |
| Mary Sisk's Bracelet | браслет Мэри Сиск |
| Obed Marsh memorial statue | памятник (мемориал) Обеду Маршу |
| Revolutionary War Memorial | памятник Войне за независимость |
| Innsmouth Look | иннсмутский облик |
| Deep One / Deep One Hybrid | глубоководный / гибрид глубоководного |
| Father Dagon / Mother Hydra | Отец Дагон / Мать Гидра |
| shoggoth; «Tekeli-li!» | шоггот; «Tekeli-li!» |
| Carnivorous Crustacean | плотоядное (хищное) ракообразное |
| Typical Police Bloodhound | полицейская ищейка |
| Buried at Sea | «Похоронен в море» |
| Wrack / Breath of the Deep | Разрушение / Дыхание глубин (в тексте перевода — по-английски, см. вопрос) |
| Contact Cthulhu / Contact Deep Ones / Contact Father Dagon / Contact Mother Hydra | Связь с божеством: Ктулху / Связь с Глубоководными / Связь с Отцом Дагоном / Связь с Матерью Гидрой |
| Curse of the Putrid Husk / Shriveling | Проклятие гниющей оболочки / Иссушение |
| Hard / Regular roll | трудная / обычная проверка |
| Penalty Die / Bonus Die | штрафная кость / бонусная кость |
| Spot Hidden, Track, Law, Animal Handling, Sleight of Hand | Внимание, Чтение следов, Юриспруденция, Обращение с животными, Ловкость рук |
