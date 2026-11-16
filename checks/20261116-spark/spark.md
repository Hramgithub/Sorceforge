# Spark of Life (`spark-of-life-en`) — перенос в базу (Р-251)

Jon Hook, 2019, Miskatonic Repository; приключение для одиночного сыщика, сентябрь 1926 года, Аркхэм, Мискатоникский университет.
Русского перевода сценария в базе нет (проверено по ключевым именам: Вестингауз, Ксейруу’к, Каппа Дельта Пси, Честерфилд и др.).

Страницы: PDF 24 страницы; печатная страница = физическая − 2 (смещение для `books.json`: **−2**: «с. 2» на физ. 4).
Без номеров: обложка (физ. 1), выходные данные (физ. 2), оглавление (физ. 3), листы сыщиков (физ. 14–19), реклама (физ. 24).

## Записи (65)

- сценарий 1: `scenarios/spark-of-life`
- сцены 11: `walking-home`, `strange-observations`, `hoyt-administration`, `campus-crier-archives`, `restricted-collection`, `faculty-ally`, `frat-house-before-party`, `toga-party`, `avoiding-the-party`, `resurrection-ritual`, `confronting-xeiruuk`
- персонажи 17: прегены `david-miller`, `ruth-peasley`, `victoria-chang`; `thomas-forte`, `kevin-chesterfield`, `kdp-brothers` (групповой профиль), `billy-brown`, `cornelius-westinghaus`, `connie-landers`, `richard-cook`, `agatha-fielding`, `howard-freeman`, `john-cawley`, `edward-greene`, `janet-rhodes`, `edgar-hathaway` (имя придумано, Р-150), `ifc-clerks` (группа, Р-151)
- существо 1: `creatures/xeiruuk` (Великий Древний сценария; общей записи нет)
- организации 3: `kappa-delta-psi`, `cult-of-xeiruuk`, `inter-fraternity-council`
- книга Мифов 1: `tomes/spark-of-life`
- предметы 11: `kdp-pledge-pin`, `astronomy-books`, `surveillance-photos`, `shoebox-revolver`, `cult-robes-and-handcuffs`, `framed-pages`, `building-permits`, `restricted-collection`, `cykranoshian-drink`, `lightning-rod`, `faculty-photograph`
- раздатка 8: `spark-papers-1-pledge-pin` … `spark-papers-7-nameless-cults`, `thomas-note`
- места 11: `kdp-frat-house` (Кампус), `kdp-parlor`, `kdp-presidents-quarters`, `westinghaus-perch`, `kdp-great-room`, `kdp-star-chamber`, `pickman-street-boarding-house` (Кампус), `hoyt-archives-room` (корпус Хойта, 629), `armitage-office` (библиотека Орна), `faculty-fishing-cabin` (окрестности Аркхэма), `xeiruuk-lair` (Цикранош)
- карта 1: `maps/kdp-frat-house-plan` (`app/maps/spark-kdp-frat-house-plan.png`, 40 меток — на каждой напечатанной подписи плана)

Картинки (12, применены): раздатка 1–7, значок кандидата (с. 3), дом братства (с. 7), портреты трёх прегенов (листы сыщиков) — `app/art/*/spark-*.webp`.
Атмосфера → `atmosphere.json`: обложка; копия раздатки 7 в тексте (с. 6); реклама подкаста (физ. 24).

Предложения к общим записям — `proposals-spark.json` (24 правки, 6 записей, пробный прогон проходит): Генри Армитедж (абзац «В „Искре жизни“»), библиотека Орна, корпус Хойта (629), Цикранош, «Мискатоникский глашатай» (псевдоним «The Campus Crier»), экземпляр «Невыразимых культов» (`copies`).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, Credits | физ. 1–2 | сценарий (`sources`), атмосфера (обложка); Ксейруу’к — пометка о придуманном божестве |
| Table of Contents | физ. 3 | сценарий (`sources`) |
| Introduction | 2 | сценарий (`summary`, `advice`, `keeper_info`: особая примета); прегены |
| Background | 2 | сценарий (`keeper_info`); Вестингауз; Ксейруу’к; культ; книга «Искра жизни» |
| Opening Scene – Walking Home | 2–3 | сцена `walking-home` |
| Chasing the Shadow (врезка) | 2 | сцена `walking-home`; Билли Браун |
| Daily Routine (врезка) | 3 | сцена `walking-home`; таблица сценария «Распорядок дня аспиранта» |
| Strange Observations (+ Keeper’s Note) | 3–4 | сцена `strange-observations`; таблица «Как культ следит за аспирантом» |
| Researching Kappa Delta Psi | 4 | сцена `hoyt-administration` |
| Thomas’ Research Assistance (врезка, статблок) | 4 | Томас Форте; сцена `hoyt-administration` |
| Inter-Fraternity Council | 4 | организация Совет братств; клерки; сцена `hoyt-administration` |
| Hoyt Administration Building (+ Keeper’s Note) | 4 | место `hoyt-archives-room`; Конни Ландерс; предмет `building-permits`; сцена `hoyt-administration` |
| Orne Library (+ Keeper’s Note) | 4–5 | сцена `campus-crier-archives`; раздатка 2–6 |
| Campus Crier articles 1–6 | 5 | сцена `campus-crier-archives`; раздатка 2–6; Кук, Филдинг, Фримен, Коули, Грин, Роудс |
| The Restricted Collection (+ Keeper’s Note) | 5–6 | сцена `restricted-collection`; предмет `restricted-collection`; место `armitage-office`; раздатка 7 |
| Keeper’s Note — senior faculty member | 6 | сцена `faculty-ally`; Эдгар Хэтэуэй; рыбацкая хижина; фотография |
| The Toga Party / Before the Party | 6 | сцена `frat-house-before-party` |
| Daytime Activities in the KDP Frat House (врезка) | 6 | сцена `frat-house-before-party`; дом братства |
| Kappa Delta Psi Frat House: Ground / Second / Cellar Floor Rooms | 7–9 | дом братства и комнаты (`kdp-parlor`, `kdp-presidents-quarters`, `westinghaus-perch`, `kdp-great-room`, `kdp-star-chamber`); предметы комнат |
| Kappa Delta Psi Star Symbol (врезка) | 7 | организация Каппа Дельта Пси; Ксейруу’к |
| The Spark of Life (врезка) | 8 | книга `tomes/spark-of-life` |
| Kappa Delta Psi frat house plan | 8 | карта `kdp-frat-house-plan` |
| The Toga Party (Idea; Keeper’s Note о погоде) | 9 | сцена `toga-party`; таблица «Время на вечеринке в тогах» |
| Kevin Chesterfield III (статблок) | 9 | Кевин Дж. Честерфилд III |
| KDP Frat Boy (статблок) | 9 | `kdp-brothers` |
| What if the Graduate Student does not want to go to the Toga Party? | 9 | сцена `avoiding-the-party`; раздатка `thomas-note` |
| Entering the Party; Alcohol | 9 | сцена `toga-party` |
| Snooping Through the House (President’s Quarters, The Fight, Drugging the Drinks, The Ritual) | 10 | сцена `toga-party`; `cykranoshian-drink` |
| How to Run the Finale (врезка) | 10 | сцена `toga-party`; сценарий (`advice`) |
| The Resurrection Ritual (1–3) | 10 | сцена `resurrection-ritual` |
| Stopping the Ritual Before it Starts; The Lightning Rod | 10 | сцена `resurrection-ritual`; предмет `lightning-rod` |
| Confronting Xeiruu’k | 10–11 | сцена `confronting-xeiruuk` |
| Xeiruu’k (врезка, Cult, статблок) | 11 | существо `xeiruuk`; культ; логово |
| Rewards | 11 | сценарий (`conclusion`); суммы — также в записях Кевина, площадки, Звёздной палаты, книги |
| Graduate Student | 11 | сценарий (`advice`); прегены (`description`, `player_chooses`) |
| Листы сыщиков (Characteristics, Skills, Weapons, Backstory, Gear, Cash) | физ. 14–19 | прегены Дэвид Миллер, Рут Пизли, Виктория Чанг |
| Handouts: The Spark of Life Papers #1–#7 | 18–21 | раздатка 1–7 (текст как напечатан + наш перевод, картинки) |

## Не взято

- Реклама подкаста «MU Podcast» (физ. 24) — не материал сценария (в `atmosphere.json` как просмотренная).
- Копия раздатки 7 в тексте главы (с. 6) — дубль картинки из приложения.
- Фоновые рамки страниц и «Quick Reference Rules», «Fellow Investigators» на обороте листов сыщиков — оформление бланка, правил книги нет.
- Фото Вестингауза, Филдинг, Фримена и Роудс, о которых говорит текст (с. 5), в книге не напечатаны — пометки в раздатке.
- Clavis Alchemae, Le Gran Albert, Der Hexenhammer, Liber Investigationis, Magnalia Christi Americana, Манускрипт Войнича, New England Canaan — записей в справочнике нет, оставлены текстом в предмете «Закрытое собрание Армитеджа» (кандидаты в записи — владельцу).
- Ассоциация выпускников Мискатоникского университета, студенческий сенат, Дисциплинарная комиссия, полиция кампуса — упомянуты один раз, без записи (текст в сценах).

## Опечатки и сомнения

- Врезка «What if…?» (с. 9): записку подсовывают под дверь «on-campus apartment», хотя на с. 2–3 аспирант и Томас живут в пансионе на 585 W. Pickman St. — `errata` сцены `avoiding-the-party` и сценария, как напечатано.
- Ксейруу’к: БкУ 0 при Комплекции 20 и СИЛ «--» — как напечатано, пометка в `quality.notes` (вывести нельзя).
- «Le Gran Albert» (вероятно, «Le Grand Albert») — как напечатано в тексте.
- «Nameless Cults (flawed edition)» — издание не названо: ссылка на общую запись книги, в предложении `copies` — «издание не уточнено».
- «New England Canaan» — то ли реальная книга Мортона, то ли «Thaumaturgical Prodigies in the New-England Canaan»; без ссылки.
- Цвет родимого пятна Виктории: «red» в тексте (с. 2), «wine» на листе — в пометке прегена.
- Буква «S» у стены Большого зала на плане не объяснена (возможно, сейф) — метка с пометкой.
- Билли Браун = нападающая «тень» — вывод из врезки; револьвер в коробке = револьвер Кевина — вывод.
- Дом братства и пансион отнесены к Кампусу — вывод (Уэст-Пикман-стрит и «братство на кампусе»).
- Вызов «Call / Dismiss Xeiruu’k» ссылается на `coc:spell:call-deity` (одна ссылка на пункт; пара — `dismiss-deity`).

## Термины книги (English → Russian)

| English | Русский |
|---|---|
| Spark of Life (сценарий) | Искра жизни |
| The Spark of Life (книга Вестингауза) | «Искра жизни» (запись «Искра жизни (книга Вестингауза)») |
| The Spark of Life (эпитет божества) | Искра Жизни |
| Isolated Investigator Adventure | приключение для одиночного сыщика |
| graduate student | аспирант (аспирантка) |
| Xeiruu’k | Ксейруу’к |
| Cykranosh | Цикранош (как в базе) |
| Ydheems | идхеемцы (как в базе) |
| Kappa Delta Psi (KDP) | Каппа Дельта Пси (КДП) |
| fraternity / frat house | братство / дом братства |
| frat boy / fraternity brothers | братья КДП |
| pledge / pledge pin | кандидат / значок кандидата |
| Greek Rush Week | неделя набора в братства |
| toga party | вечеринка в тогах |
| star symbol | звезда братства (звезда КДП) |
| Inter-Fraternity Council | Совет братств |
| Archives Room | Архив (корпуса Хойта) |
| student senate / Disciplinary Review Board | студенческий сенат / Дисциплинарная комиссия |
| The Campus Crier / The Crier | «Глашатай» (= «Мискатоникский глашатай») |
| Restricted Collection / Restricted Section | Закрытое собрание / закрытый отдел |
| Comparative Ecclesial Studies; ecclesiology | сравнительная экклезиология; экклезиология |
| Dean of Humanities | декан гуманитарного факультета |
| Alumni Association | Ассоциация выпускников |
| Hyperborean pagan cult | гиперборейский языческий культ |
| President’s Quarters | Покои президента |
| Westinghaus’ Perch | Площадка Вестингауза |
| Parlor / Sitting Room | Гостиная / малая гостиная |
| Great Room | Большой зал |
| Star Chamber | Звёздная палата |
| Bedroom Chambers | спальни |
| Resurrection Ritual | обряд воскрешения |
| vessel | сосуд |
| distinct physical feature | особая примета |
| Crimson Lightning | Багровая молния |
| Crimson Storm | Багровая буря |
| Feed the Spark of Life | «Накормить Искру Жизни» |
| Commune with the Crimson Storm | «Беседа с Багровой бурей» |
| The Deathless Breath | «Бессмертное дыхание» |
| Xeiruu’k’s Caress | «Ласка Ксейруу’ка» |
| The Cloak of Another’s Flesh | «Плащ чужой плоти» |
| Rite of Salts | «Обряд солей» |
| Cykranoshian drink (alien chemical agent) | цикраношский напиток |
| The Spark of Life Papers #N | Раздатка «Искра жизни» N |
| Per Positivum Mutatio Magicae / Positive Change Through Magic | «Позитивные перемены через магию» |
| mad creator; blood-red star; stormlord | безумный творец; кроваво-красная звезда; повелитель бурь |
| Hard Success / Hard roll | трудный успех / трудная проверка |
| Cornelius Westinghaus | Корнелиус Вестингауз |
| Kevin J Chesterfield III | Кевин Дж. Честерфилд III |
| Thomas Forte | Томас Форте |
| Billy Brown | Билли Браун |
| Connie Landers | Конни Ландерс |
| Dr. Richard Cook | доктор Ричард Кук |
| Agatha Fielding | Агата Филдинг |
| Howard Freeman | Говард Фримен |
| John J. Cawley | Джон Дж. Коули |
| Edward Greene | Эдвард Грин |
| Janet Rhodes | Джанет Роудс |
| Ruth Peasley / William “Grandpa Bean” Peasley | Рут Пизли / Уильям Пизли, «дедушка Бин» |
| David Miller | Дэвид Миллер |
| Victoria Chang | Виктория Чанг |
| Mr. Mittens | Мистер Митенс |
| Pickman Street / West Street / W. Pickman St. | Пикман-стрит / Уэст-стрит / Уэст-Пикман-стрит |
| Arkham’s River District | Речной район Аркхэма |
