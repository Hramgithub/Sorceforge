# «Shimmering Sea» (`shimmering-sea-en`) — сверка полноты (Р-134, Р-251)

Часть `shimmering`, вся книга. В PDF 11 страниц (кэш текста даёт 12-ю пустую — `pdftoppm` её не знает). На физ. с. 2–11
напечатаны номера 1–10 (печатная = физическая − 1), обложка (физ. 1) без номера: **offset −1** (в
`pipeline/source/books.json` у книги `offset` не задан — ставит ведущий). Источник — английский оригинал (Aser Tolentino,
The Redacted Files, Miskatonic Repository, 2019); русский текст — наш перевод (флаг `translated`). Эпоха — `modern`
(август 2019). Записи — `kb/books/shimmering-sea-en/` (64): сценарий 1, сцены 14, персонажи 26 (6 сыщиков-`pregen` без
статблоков, 15 именных NPC, 3 NPC с придуманными именами, 2 групповых профиля), существа 2, организации 2, предметы 6,
места 13 (3 корабля + 10 помещений эсминца). Раздаточных материалов и карт в книге нет.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Shimmering Sea», Aser Tolentino | физ. 1 | `scenario/shimmering-sea` (sources); картинка — `atmosphere.json` |
| Credits (авторы, иллюстрации US DoD / US Navy и др., © 2019 the Redacted Files) | с. 1 (физ. 2) | `scenario.summary`, `sources`; логотип — `atmosphere.json` |
| Introduction | с. 2 (физ. 3) | `scenario.keeper_info`, `summary`; `item/debye-detector`; `organization/deep-one-colony`, `ncis`; `creature/shoggoth-shimmering`; `character/arthur-duncan`, `phil-claremont`; картинка эсминца — `location/uss-lyndon-johnson` |
| The Scenario / The Briefing | с. 3 (физ. 4) | `scene/briefing`; `scenario.hook`; `character/patricia-oleary`, `seahawk-crew-chief`, `steven-winters`; `location/uss-carl-vinson` |
| Areas of Interest | с. 3 | `location/uss-lyndon-johnson` (перечень помещений) |
| The Bridge | с. 3 | `scene/bridge`, `location/bridge`; `character/jack-picard`, `steven-winters` |
| Ship Mission Center | с. 3 | `scene/ship-mission-center`, `location/ship-mission-center`; `character/aaronson` |
| Sonar Control | с. 3–4 | `scene/sonar-control`, `location/sonar-control` (картинка); `character/dennis-warner`, `ricardo-garza`; `item/debye-detector` |
| Duncan’s Berth | с. 4 (физ. 5) | `scene/duncan-berth`, `location/duncan-berth`; `character/monsour`, `putnaam`, `chavez`; `item/duncan-flash-drive`, `duncan-diary` |
| Claremont’s Berth | с. 4 | `scene/claremont-berth`, `location/claremont-berth`; `character/mendoza`, `butler`; `item/nautical-chart-scraps`, `duncan-laptop` |
| The Armory | с. 4 | `scene/armory`, `location/armory`; `character/todd-fuller` |
| Legal Office | с. 4–5 | `scene/legal-office`, `location/legal-office`; `character/jeffrey-sheridan`; `item/duncan-laptop` |
| The Hangar | с. 5 (физ. 6) | `location/hangar` |
| The Boat Bay | с. 5 | `location/boat-bay` |
| The Chinese Trawler | с. 5 | `scene/chinese-trawler`, `location/chinese-trawler` (картинка); `character/trawler-captain`, `trawler-officer`, `chinese-sailors`; `item/radio-intercept` |
| Avenues of Investigation / The Array | с. 6 (физ. 7) | `scene/the-array`; `item/debye-detector`; `character/jack-picard` |
| The Signal | с. 6 | `scene/the-signal`; `item/duncan-flash-drive`, `duncan-laptop` |
| Examining the Array | с. 6 | `scene/the-array` (второй абзац); `item/debye-detector` |
| The Loss of the Type 091 | с. 6 | `scene/loss-of-type-091`; силуэт шоггота — картинка `creature/shoggoth-shimmering`; фото со стрелком — `atmosphere.json` |
| Someone on the Hull | с. 7 (физ. 8) | `scene/someone-on-the-hull`; `location/upper-deck`; `creature/deep-one-shimmering`; `character/arthur-duncan` |
| The Final Battle (оружие корабля, исходы) | с. 7 | `scene/final-battle` (картинка); таблица «Оружие для обороны корабля» — `location/uss-lyndon-johnson.tables` (в сценарии — ссылка `from`); `scenario.conclusion` |
| Timeline: August 20–23, 24, 25, 28, 30, 31, September 1, 2019 | с. 8 (физ. 9) | `scenario.tables` «Хронология» (14 строк); `scenario.advice`; фото F-35 — `atmosphere.json` |
| Bestiary: American Soldier | с. 9 (физ. 10) | `character/american-soldiers` (варианты «Рядовой и старшина» / «Офицер»; картинка) |
| Bestiary: Chinese Sailor | с. 9 | `character/chinese-sailors` (варианты «Матрос» / «Офицер») |
| Bestiary: Deep One | с. 9 | `creature/deep-one-shimmering` (`instance_of` `coc:creature:deep-one`) |
| Bestiary: Shoggoth | с. 9 | `creature/shoggoth-shimmering` (`instance_of` `coc:creature:shoggoth`) |
| Player Characters: Lieutenant Commander Jillian Morris | с. 10 (физ. 11) | `character/jillian-morris` (`pregen`) |
| Special Agent Alejandro Estrada | с. 10 | `character/alejandro-estrada` (`pregen`) |
| Captain Wesley Forsyth | с. 10 | `character/wesley-forsyth` (`pregen`) |
| Dr. Sheena Brock | с. 10 | `character/sheena-brock` (`pregen`) |
| Special Agent Blaine Dubois | с. 10 | `character/blaine-dubois` (`pregen`) |
| Lieutenant Marilyn “Tweaker” Chan | с. 10 | `character/marilyn-chan` (`pregen`); фото с пулемётом — `atmosphere.json` |

## Картинки

| Страница | Картинка | Куда |
|---|---|---|
| физ. 1 | обложка | `atmosphere.json` |
| физ. 2 | логотип Miskatonic Repository | `atmosphere.json` |
| физ. 3 | эсминец типа «Замволт» | `location/uss-lyndon-johnson` |
| физ. 5 | пост гидроакустиков | `location/sonar-control` |
| физ. 6 | рыболовный траулер | `location/chinese-trawler` |
| физ. 7 | силуэт шоггота | `creature/shoggoth-shimmering` |
| физ. 7 | человек стреляет из пистолета | `atmosphere.json` (с персонажем книга не связывает) |
| физ. 8 | пуск зенитной ракеты | `scene/final-battle` |
| физ. 9 | F-35 над эсминцем | `atmosphere.json` |
| физ. 10 | американские моряки с ракетой | `character/american-soldiers` |
| физ. 11 | моряки у пулемёта | `atmosphere.json` |

Нейросетевых иллюстраций выходные данные не называют (US Department of Defense, aPinkPanthress, Raul Popadineti, US Navy,
Simon Bray, Marco Monte, US 6th Fleet).

## Опечатки и расхождения книги

- Глубоководный: ПЗ 13 при ВЫН 80 и ТЕЛ 70 (должно 15) и БкУ +1D6 при СИЛ + ТЕЛ = 160 и Комплекции 1 (должно +1d4) —
  исправлены по большинству (Р-36, `fixed: true`); ПМ 10 при МОЩ 80 (16) — как напечатано. Похоже, производные значения
  перенесены из профиля «Книги хранителя» без пересчёта (`creature/deep-one-shimmering.errata`).
- Шоггот: ПЗ 80 при ВЫН 250 и ТЕЛ 200 (45) — оставлено как напечатано (Р-76: книга подчёркивает «немыслимый размер»),
  **вопрос владельцу**; ПМ 10 при МОЩ 85 (17); «Attacks per round: 2» против четырёх проверок МОЩ в последнем бою — берётся
  текст боя (Р-38) (`creature/shoggoth-shimmering.errata`, `scene/final-battle.errata`).
- Американский военный: у «Firearms (Rifle/Shotgun) M4 Carbine» нет процента (`errata`); БкУ, Комплекция, Скорость, ПМ не
  напечатаны — посчитаны (Р-41, `corrections`). Китайский моряк — то же (кроме процентов); ПЗ 12 при (65 + 50) / 10 = 11,5 —
  округление вверх (Р-161, не опечатка).
- Оба профиля людей: характеристика «CHA» — принята за НАР (вывод, `errata`).
- Тип подлодки: заголовок «The Loss of the Type 091» (с. 6) — в хронологии «Type 093» (с. 8) (`scene/loss-of-type-091`, `scenario.errata`).
- Исчезновение Дункана: «через три дня после начала патруля, между 0230 и 0730» (с. 2) — «28 августа, после средней вахты в
  0200, хватились в 0730» (с. 8) (`character/arthur-duncan`, `scenario.errata`).
- Хронология, 25 августа: заголовок «2345 Hours», в тексте «at 0148 Hours» (`scenario.errata`).
- Название корабля: «Lynden Johnson» (с. 2) и «Lyndon Johnson» (с. 3, 8) — в `aliases`. Самолёт «C-w Greyhound» (с. 3) —
  опечатка «C-2» (с. 8), исправлено молча (Р-39). «scansion» вместо «stanchion» (с. 7) — словесная, исчезает в переводе.
- Вертолёт: сыщиков везёт SH-60 «Си Хок», в ангаре стоит MH-60R «Си Хок» (`location/hangar.quality`).
- Штрафы «−20%», «−30%», «−40» и «half their skill» — правила прежних редакций, оставлены как в книге.
- Наград Рассудка за исход книга не даёт (`scenario.conclusion`).

## Не взято

- Южно-Китайское море как запись места: `tools/check.py` не допускает место без `part_of`, кроме города, корабля и города
  сценария (Р-189, Р-197); сведения о море, островах Спратли и Тритон, искусственных островах — в `scenario.keeper_info`,
  таблице «Хронология», описаниях кораблей и колонии.
- Аэропорт Манилы, Пёрл-Харбор, авиабаза Розуэлл, остров Тритон, острова Спратли, корабли «Нормандия», «Берри», «О’Кейн»,
  «Боудич», аппарат «Мори», подлодки типа 091/093, вьетнамская лодка, катер контрабандистов — только упоминания, остаются
  текстом в сценарии, хронологии и сценах.
- Безымянные мимолётные роли — вахтенный у кормы, исполняющий обязанности старшины корабельной полиции, контрабандист на
  записи (говорит по-тагальски), вахтенный офицер — без отдельных записей (покрыты групповыми профилями и текстом сцен).
- Бутылка водки — отдельной записи нет: её уже нет (выброшена за борт), это показание Батлера (`character/butler`, `scene/claremont-berth`).
- Пистолет Клермонта — отдельной записи нет: упомянут в `item/duncan-laptop`, `location/legal-office`, `location/armory`.
- Оружие корабля (рельсотрон, 155-мм орудие, ракеты ESSM, «Хеллфайр», 25-мм пушки) и M-240B, «Моссберг» M590A1 —
  записями справочника `kb/weapons/` не заведены (общие записи — не мои): числа в таблице корабля; кандидаты в справочник.
- Контакты и сайт авторов (выходные данные) — не данные игры.

## Предложения (`proposals-shimmering.json`)

- `coc:weapon:m4` — `source_variants`: урон M4 2d6+1 в профиле «American Soldier» (в справочнике 2d6).
- `coc:weapon:tt-33-type-54` — `source_variants`: урон «Тип 54» 1d10 в профиле «Chinese Sailor» (в справочнике 1d10+1).

## Термины (English → Russian)

| English | Русский |
|---|---|
| Shimmering Sea | Мерцающее море |
| South China Sea | Южно-Китайское море |
| South China Sea Incident | «инцидент в Южно-Китайском море» |
| USS Lyndon (Lynden) Johnson, the Johnson | эсминец «Линдон Джонсон», «Джонсон» |
| Zumwalt-class stealth destroyer | эсминец-невидимка типа «Замволт» |
| USS Carl Vinson; Carl Vinson Carrier Strike Group | авианосец «Карл Винсон»; ударная группа «Карла Винсона» |
| USS Normandy / USS Berry / USS O’Cane | крейсер «Нормандия» / эсминец «Берри» / эсминец «О’Кейн» |
| USNS Bowditch; Maury (underwater research vehicle) | «Боудич»; подводный аппарат «Мори» |
| NCIS, Naval Criminal Investigative Service | Служба криминальных расследований ВМС (NCIS) |
| special working group | особая рабочая группа |
| Judge Advocate General’s Corps (JAG) | Корпус военных юристов |
| Chairman of the Joint Chiefs of Staff | председатель Объединённого комитета начальников штабов |
| National Command Authority | Национальное командование |
| Captain (USN, commanding officer) | капитан 1-го ранга, командир |
| Commander; Executive Officer (XO) | капитан 2-го ранга; старший помощник (старпом) |
| Lieutenant Commander | капитан 3-го ранга |
| Lieutenant; Lieutenant Junior Grade | лейтенант; лейтенант (младший) |
| Captain (Marines) | капитан морской пехоты |
| Senior Chief Petty Officer | старший главный старшина |
| Chief (Petty Officer) | главный старшина |
| Chief Master-at-Arms / Master-at-Arms | главный старшина корабельной полиции / старшина корабельной полиции |
| Sonar Technician Third-Class, STG, sonarman | гидроакустик 3-го класса, гидроакустик |
| Gunner’s Mate Second-Class / Third-Class | старшина-оружейник 2-го класса / оружейник 3-го класса |
| Communications and collateral duty Legal Officer | офицер связи и по совместительству юрист корабля |
| Administrative Department / Weapons department | административная боевая часть / оружейная боевая часть |
| crew chief | бортовой техник |
| watch stander / officer of the watch | вахтенный / вахтенный офицер |
| mid watch | средняя вахта |
| General Quarters, battle stations | боевая тревога, места по боевому расписанию |
| communications blackout | запрет на связь |
| visit, board and search (VBS) | досмотровая операция |
| Marine Force Recon | разведка морской пехоты (Force Recon) |
| SEAL complement | отряд «морских котиков» |
| special operations detachment | приданный отряд сил специальных операций |
| Areas of Interest | места на корабле |
| Avenues of Investigation | пути расследования |
| The Bridge | мостик |
| Ship Mission Center / Mission Control Center; auxiliary Ship Mission Center | Центр управления кораблём; запасной Центр управления |
| Common Display Stations | стандартные пульты отображения |
| Sonar Control | гидроакустический пост |
| Duncan’s Berth / Claremont’s Berth | каюта Дункана / каюта Клермонта |
| The Armory | оружейная |
| Legal Office | юридический отдел |
| The Hangar | ангар |
| The Boat Bay | лодочный отсек |
| rigid-hull inflatable boats | жёсткие надувные лодки |
| upper deck, stern, winch | верхняя палуба, корма, лебёдка |
| safety line; stanchion («scansion») | страховочный трос; леерная стойка |
| Debye array / Debye Sensor / Debye detector | детектор Дебая |
| Debye Effect | эффект Дебая |
| towed array (sonar) | буксируемая (гидроакустическая) антенна |
| hull-mounted array | корпусная антенна |
| magnetic anomaly detector | магнитометр |
| resonance imaging | резонансная томография |
| Project Couplet / Project Quire | «Project Couplet» / «Project Quire» (проект «Квайр») — оставлены как напечатаны |
| recovered Roswell AFB | найдено на авиабазе Розуэлл |
| The Signal | Сигнал |
| sound restoration gear | оборудование для восстановления звука |
| flash drive | флешка |
| nautical chart | морская карта |
| evidence bags | пакеты для вещественных доказательств |
| The Chinese Trawler | китайский траулер |
| electronic intelligence gathering platform | корабль радиоэлектронной разведки |
| radio intercept | радиоперехват |
| cigarette boat | катер (контрабандистов) |
| MILF separatists | сепаратисты ИФОМ |
| ASEAN | АСЕАН |
| PLAN, People’s Liberation Army Navy | ВМС НОАК |
| Republic of China | Китайская Республика |
| Triton Island; Spratly Islands | остров Тритон; острова Спратли |
| Type 091 / Type 093 (attack) submarine | подлодка типа 091 / атомная подлодка типа 093 |
| crash ascent | аварийное всплытие |
| pressure hull | прочный корпус |
| coastal steamer | каботажный пароход |
| SH-60 / MH-60R Seahawk | вертолёт SH-60 / MH-60R «Си Хок» |
| C-2 Greyhound carrier onboard delivery (COD) aircraft | самолёт палубной доставки C-2 «Грейхаунд» |
| J10 fighters; SU-30 | истребители J-10; Су-30 |
| V-22 search and rescue aircraft | поисково-спасательный конвертоплан V-22 |
| railgun | рельсотрон |
| 155mm main gun | 155-мм главное орудие |
| Vertical Launch System cells | ячейки установки вертикального пуска |
| Evolved Sea Sparrow Missiles | зенитные ракеты ESSM («Эволвд Си Спарроу») |
| Hellfire missiles | ракеты «Хеллфайр» |
| 25mm cannons | 25-мм пушки |
| M-16 rifles; M-240B medium machine guns; Mossberg M590A1 shotguns | винтовки M-16; единые пулемёты M-240B; дробовики «Моссберг» M590A1 |
| M9 Pistol; M4 Carbine | пистолет M9; карабин M4 |
| Type 54 Pistol; Type 56 Assault Rifle | пистолет «Тип 54»; автомат «Тип 56» |
| American Soldier | Американские военные (групповой профиль) |
| Chinese Sailor | Китайские моряки (групповой профиль) |
| Deep One; Deep One colony | глубоководный; колония глубоководных |
| Shoggoth | шоггот |
| Engulf | Поглощение |
| heavy weapons (skill) | Стрельба (тяжёлое оружие) |
| Engineering / Physics roll | Наука (инженерное дело) / Наука (физика) |
| Piloting | Пилотирование |
| Player Characters | готовые сыщики |
| Bestiary | бестиарий |
| Timeline | Хронология |

Имена: Arthur Duncan — Артур Дункан; Phil Claremont — Фил Клермонт; Jack Picard — Джек Пикар; Steven Winters — Стивен
Уинтерс; Patricia O’Leary — Патриция О’Лири; Aaronson — Ааронсон; Dennis Warner — Деннис Уорнер; Ricardo Garza — Рикардо
Гарса; Todd Fuller — Тодд Фуллер; Monsour — Монсур; Putnaam — Патнаам; Chavez — Чавес; Mendoza — Мендоса; Butler — Батлер;
Jeffrey Sheridan — Джеффри Шеридан; Jillian Morris — Джиллиан Моррис; Alejandro Estrada — Алехандро Эстрада; Wesley
Forsyth — Уэсли Форсайт; Sheena Brock — Шина Брок; Blaine Dubois — Блейн Дюбуа; Marilyn “Tweaker” Chan — Мэрилин «Твикер»
Чан. Придуманы (Р-150, `editorial_text`): бортовой техник «Си Хока» — Кайл Хендерсон; капитан траулера — Лю Цзяньго; офицер
траулера — Чжан Вэй; имена групп (Р-151) — в записях профилей.
