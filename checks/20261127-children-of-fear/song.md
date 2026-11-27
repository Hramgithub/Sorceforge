# «The Children of Fear», часть song — глава 3 «Song of the Lost and Forgotten» (с. 97–152, 349–350, 369–373, 388–391)

Этап `children-of-fear-en/scenario/song-of-the-lost-and-forgotten` (order 3). Русский текст — наш перевод (Р-251, флаг `translated`).
Генератор — `.cache/lead-tools/gen-cof-song/gen.py` (люди и существа — `gen_people.py`, места и карты — `gen_places.py`,
сюжет, предметы, раздатка, правила — `gen_story.py`; тексты раздатки — `handout_texts.py`; вырезки — `crops.py`).

Записи: 154 файла — сценарий 1, сцены 17, персонажи 18, существа 7, предметы 5, раздатка 8, правила 8, карты 8,
места книги 78, общие города 4 (`peshawar`, `chakdara`, `khotan`, `turfan`). Картинки — 17 (`art-song.json`, применены),
карты — `app/maps/cof-song-*.jpg` (8).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 3: Song of the Lost and Forgotten (вступление) | 97 | сценарий `song-of-the-lost-and-forgotten`: summary, keeper_info |
| Tackling the Unknown | 97 | сценарий: keeper_info |
| Towing the (Red) Line | 97 | сценарий: advice |
| The Taklamakan's Weather | 98 | место `song-tarim-basin` (абзац «Погода Такла-Макан») |
| Part One: The Land of Death | 98–99 | `song-tarim-basin`, `song-taklamakan-desert`; arc.part сцен 1–5 |
| North or South? | 99–100 | сцена `song-north-or-south`; места `song-northern-silk-road`, `song-southern-silk-road` |
| Missing the Plot | 100 | сценарий: advice |
| Signs and Portents | 100 | сцена `song-north-or-south` |
| With Curious Eyes 1: The Silk Road | 101 | сцена `song-north-or-south` |
| The Black Storm (Optional) | 101 | сцена `song-the-black-storm` |
| The Northern Route | 102 | `song-northern-silk-road`; Нефритовые ворота — запись части gates `gates-jade-gate` (факты — предложением); Хами — черновик |
| The Painted Ruins (Optional) | 102–104 | сцена `song-the-painted-ruins`; места `song-karakhoja`, `song-turfan-environs`; персонаж `song-karakhoja-archaeologist` |
| High and Dry | 102 | `song-tarim-basin` (абзац «Высоко и сухо») |
| Self-Improvement: The Tarim Basin | 102 | правило `song-self-improvement` |
| Turfan (врезка) | 104 | общий город `coc:location:turfan`; `song-bezeklik-caves`, `song-flaming-mountains` |
| The Southern Route | 104 | `song-southern-silk-road` |
| A Thorn in Their Side | 104 | сцена `song-the-painted-ruins`; персонаж `song-karakhoja-archaeologist` |
| The People You Meet | 105 | сцена `song-the-people-you-meet`; аксакалы — `song-tarim-basin` |
| The Rat King (Optional) | 105–109 | сцена `song-the-rat-king`; места `song-rat-king-colony`, `song-khotan-guest-house`, `song-khotan-environs`, `song-dandan-uilik`; персонажи `celia-roberts`, `moira-abernathy` |
| Khotan (врезка) | 106 | общий город `coc:location:khotan` |
| The Fate of Miss Abernathy | 108–109 | сцена `song-the-rat-king`; `moira-abernathy` |
| Peaks and Troughs | 110 | место `song-mountain-passes` |
| Part Two: Through the Mountains | 110–111 | `song-mountain-passes`; сцена `song-through-the-mountains` |
| From Kashgar (Northern Route) | 111 | сцена `song-through-the-mountains`; `song-kilik-pass`, `song-khunjerab-pass`; Кашгар, Гилгит — черновики |
| With Curious Eyes 2: The Mountain Passes | 111 | сцена `song-through-the-mountains` |
| The Giantess Reborn (Optional) | 111–112 | сцена `song-the-giantess-reborn-the-bear`; `song-hasinas-cave`; существо `song-asiatic-black-bear` |
| The Village | 112–113 | сцена `song-the-giantess-reborn-the-village`; `song-shina-village`; `atif-baig`, `song-the-danyal` |
| The Graveyard | 113 | та же сцена; `song-shina-village-graveyard` |
| The Missing Girl | 115 | та же сцена; `ziab-ali`, `hasina-moiz` |
| The Night Watch | 115 | сцена `song-the-giantess-reborn-night-watch` |
| The Cave | 116 | та же сцена |
| From Khotan/Yarkand (Southern Route) | 116–117 | сцена `song-through-the-mountains`; `song-karakorum-pass`, `song-mustagh-pass`, `song-malakand-pass`; Яркенд, Лех, Сринагар, Равалпинди — черновики |
| Self-Improvement: The High Passes | 117 | правило `song-self-improvement` |
| The Runner (Optional) | 117–118 | сцена `song-the-runner`; `harit-peshin`, `james-strudwick`, предмет `song-runners-wallet` |
| Many Voices: Hindustani | 117 | правило `song-many-voices-hindustani` |
| Part Three: Still Waters; Chakdara | 119 | общий город `coc:location:chakdara`; `song-chakdara-environs`, `song-lake-danakosha` |
| Set Up: Smoke and Mirrors | 120 | сценарий: hook |
| Dramatis Personae (Moorcroft, Dhar, Singh, Pisachas) | 120–123 | таблица «Песнь: действующие лица» сценария; `robert-moorcroft`, `suraj-dhar`, `isminder-veer-singh`, `song-pisachas` |
| Chain of Command | 121 | правило `song-chain-of-command` |
| The Caste System | 122 | правило `song-the-caste-system` |
| Guru Singh's Warriors | 123 | правило `song-guru-singhs-warriors` |
| Racism in Colonial India | 123 | правило `song-racism-in-colonial-india` |
| Start: Reflections; The Stupa | 124–125 | сцена `song-reflections`; `song-andan-dheri-stupa`, `song-damkot-hill-fort`; предмет `song-rfm-handkerchief` |
| Line of Sight; Side Effects; In Absentia 1 | 126 | правило `song-line-of-sight` |
| Houses of Wonder (Peshawar) | 126–127 | общий город `coc:location:peshawar`; районы `song-peshawar-old-city`, `song-peshawar-cantonment`; сцена `song-houses-of-wonder` |
| Peshawar Museum | 127 | место `song-peshawar-museum` и 25 помещений по карте |
| Peshawar's Weather | 128 | таблица «Пешавар: погода» у `coc:location:peshawar` |
| On Display | 128–130 | сцена `song-houses-of-wonder`; предмет `song-ritual-bowls` |
| Coin of the Realm: India | 130 | правило `song-coin-of-the-realm-india` |
| The Curator's Office | 130–131 | сцена `song-houses-of-wonder`; `song-peshawar-museum-a-office`; `harold-hargreaves` |
| The Man from the Ministry; At Work; At the Royal Ancillary Club; At Home | 132–133 | сцена `song-the-man-from-the-ministry`; `song-moorcroft-house`, `song-royal-ancillary-club` |
| Members Only | 132 | место `song-royal-ancillary-club` |
| Something for the Ladies | 132 | сцена `song-the-man-from-the-ministry` |
| Recovery; Sale or Return?; On Loan; Breaking and Entering | 133–135 | сцена `song-recovery`; `song-ander-shahar` |
| Doing Time | 135 | сцена `song-recovery` |
| Not the Real Deal | 136 | сцена `song-recovery` |
| Unwanted Attention; Bedside Manner | 136–137 | сцена `song-unwanted-attention`; `song-peshawar-9-lady-reading-hospital` |
| Museum Mayhem | 137–138 | та же сцена; `neha` |
| Unwelcome Guests; At a Hidden Location; Up Close and Personal; Brief Encounters | 138–140 | сцена `song-unwelcome-guests`; `song-british-cemetery`, `song-southern-charnel-grounds` |
| Mark of a God | 139 | предмет `song-mark-of-sisirama`; способность пишачей |
| A Quiet Word | 140 | сцена `song-unwelcome-guests` |
| Moving On; To the Cool Grove (Sitavana); To the Parkhang (Derge) | 140–141 | сцена `song-moving-on`; последний шаг сценария |
| The River of Life | 140 | место `song-grand-trunk-road` |
| Missing Pieces? | 141 | сцена `song-moving-on`; предмет `song-ritual-bowls` (mechanics) |
| The End of the Road: Gandhara | 141 | сцена `song-moving-on` |
| Wellcome's Man in India (с профилем Dr. Paira Mall) | 142 | персонаж `paira-mall` |
| Rewards | 143 | таблица «Песнь: награды» сценария; conclusion |
| Characters and Monsters; Non-Player Characters | 144 | `hasina-moiz`, `robert-moorcroft`, `suraj-dhar`, `isminder-veer-singh` |
| Generic Villagers/Townsfolk | 145 | групповой профиль `song-generic-villagers` (6 вариантов, имена придуманы, Р-151) |
| Creatures and Monsters: Rat King; Diadem of the Rat King | 146 | существо `song-rat-king`; предмет `song-diadem-of-the-rat-king` |
| Rat-Things, lieutenants of the Rat King | 147 | существо `song-rat-things` (6 вариантов, instance_of `coc:creature:rat-thing`) |
| Rat Pack | 147 | существо `song-rat-pack` (6 вариантов, instance_of `coc:creature:rat-swarm`) |
| Pisachas, ghoul subspecies; Six Sample Pisachas | 148 | существо `song-pisachas` (средние + 6 вариантов, instance_of `coc:creature:ghoul`) |
| Walking Portraits, animated art | 149 | существо `song-walking-portraits` (5 вариантов) |
| Asiatic Black Bear, opportunistic scavenger | 150 | существо `song-asiatic-black-bear` (instance_of `coc:creature:bear`) |
| Yak, beast of burden | 151 | существо `song-yak` |
| Handout: Song 1–6 | 98, 114, 128, 130, 133, 136; 369–372 | раздатка `song-handout-1-kara-buran` … `song-handout-6-moorcroft-note` (текст англ. + перевод, картинки) |
| What Your Investigator Knows 3: The Tarim Basin | 349 | `song-knows-3-the-tarim-basin` |
| What Your Investigator Knows 4: The Northwest Frontier | 350 | `song-knows-4-the-northwest-frontier` |
| Карта «The Northern and Southern Silk Roads … 1924» | 99 / 388 | карты `song-northern-and-southern-silk-roads-1924` (+`-players`) |
| Карта «Mountain Passes» | 110 / 389 | карты `song-mountain-passes` (+`-players`) |
| Карта «The City of Peshawar» (ключ 1–18) | 127 / 390 | карты `song-city-of-peshawar` (+`-players`); места `song-peshawar-1…17`, `song-peshawar-museum` (3), `song-peshawar-old-city` (18) |
| Карта «Peshawar Museum c. 1924» (1–18, A–G) | 129 / 391 | карты `song-peshawar-museum-1924` (+`-players`); 25 мест `song-peshawar-museum-*` |

## Не взято

- с. 152 — иллюстрация во всю страницу без текста (атмосфера, `atmosphere-song.json`).
- с. 373 — «Handout: Bones 1» и «Bones 2» на той же странице приложения F принадлежат части bones; с. 369 — «Handout: Gates 5» — части gates.
- Атмосферные иллюстрации (12, включая «Opposite: Investigating Peshawar Museum», «The nighttime procession», «Padmasambhava by
  Nicholas Roerich» и второй Крысиный король на с. 108) — `atmosphere-song.json` (сводит ведущий).
- Мелкие безымянные лица без механики (молодой субалтерн форта Дамкот, клерк, уборщик, чайвала, секретари музея, медсестра,
  имам Караходжи, певцы Хотана) — текстом в сценах; записей не заводилось.
- Подписи карт без записей мест (Kucha, Korla, Aksu, Tumchuq, Cherchen, Abdal, Simla, Kabul, Mingora, Rawalpindi, Lahore, Multan,
  Rutok, Gartok, названия стран) — без меток, перечислены в `quality.notes` карт.
- Своей записи «Нефритовые ворота» нет — есть `gates-jade-gate` (части gates); факты главы 3 — в `proposals-song.json`.

## Опечатки и сомнения

- Сурадж Дхар: урон драки «1D3+D4» (с. 144) — исправлено на 1d3+1d4 (errata, fixed).
- Крысиный король: ПЗ 18 при ВЫН 95, ТЕЛ 70 (ожидалось 16) — оставлено как напечатано; Уклонение 45% в бою и 50% в навыках (с. 146).
- Крысиные твари 1, 2, 6: ПЗ 4 при (ВЫН+ТЕЛ)/10 = 1–2 — как напечатано (с. 147); стая крыс 3: ПЗ 9 при ожидаемых 7.
- Таблица стай крыс: звёздочка «5*» без сноски (перенесена из таблицы крысиных тварей).
- Пишачи: средняя СИЛ 80 при броске (3d6+6)×5 — как в «Книге хранителя».
- Текст: крепость «Balar Hisar» (с. 127), на карте — «Bala Hisar Fort»; витрина с чашами «в углу задней галереи (F)» (с. 128), а на
  карте F — витрина, задняя галерея — 5; подпись «Investigating Peshawar Muesum» (с. 97); «$5 dollars US» (с. 130).
- Перевал Килик в тексте есть, на карте «Mountain Passes» не подписан.
- Знак Сисирамы: часть spirits завела тот же предмет (`spirits-sisirama-token`, гл. 7), часть song — `song-mark-of-sisirama`
  (впервые напечатан в гл. 3, id ждёт часть liberation); объединить — вопрос ведущему.

## Термины (English → русский)

kara-buran — кара-буран; pisacha — пишача (мн. пишачи); ghoul — упырь; rat-thing — крысиная тварь; aksakal — аксакал;
melong — мелонг; rten (place of power) — тен (место силы); khatvanga — кхатванга; terma — терма; stupa — ступа; kapala — капала;
lama — лама; mala beads — чётки; thumo — туммо; bleed-through — просачивание; Danyal — даньял; Danyalism — даньялизм;
khoi — шапка-кхои; Turki — тюрки; Uighurs — уйгуры; Shina — шина; Pashto — пушту; Pathans — патаны; Hindustani — хиндустани;
naswar — насвай; tonga — тонга; haveli — хавели; cantonment — кантонмент; sahib — сахиб; Babu — бабу; Brahmin — брахман;
Kshatriya — кшатрий; Vaishya — вайшья; Shudra — шудра; Dalit — далит; Khalsa — кхалса; dastar — дастар; kesh, kangha, kaccha,
kirpan, kara — кеш, кангха, каччха, кирпан, кара; rupee / anna — рупия / анна; chai wallah — чайвала; subaltern — субалтерн;
ICS — Индийская гражданская служба (ИГС); IPS — Индийская политическая служба (ИПС); ASI — Археологическая служба Индии;
Survey of India — Топографическая служба Индии; Grand Trunk Road — Великий колёсный путь; Khyber Pass — Хайберский проход;
Tarim Basin — Таримская впадина; Taklamakan — Такла-Макан; Silk Road — Шёлковый путь; Gandhara — Гандхара; Oddiyana — Уддияна;
Swat — Сват; Andan Dheri — Андан-Дхери; Lake Danakosha — озеро Данакоша; Damkot Hill — холм Дамкот; Karakhoja — Караходжа;
Bezeklik — Безеклик; Flaming Mountains — Пылающие горы; Dandan-uilik — Дандан-Уйлик; Kilik / Khunjerab / Karakorum / Mustagh /
Malakand Pass — перевал Килик / Хунджераб / Каракорумский / Мустаг / Малаканд; Peshawar Museum — Пешаварский музей;
Royal Ancillary Club — клуб «Ройял Энсиллари»; Lady Reading Hospital — больница леди Рединг; Ander Shahar — Андер-Шахар (Ювелирный
базар); Chowk Yadgar — Чоук-Ядгар; Street of Storytellers — Улица сказителей; Hiuen-Tsiang — Сюаньцзан; Fa Hsien — Фа Сянь;
Padmasambhava / Guru Rinpoche — Падмасамбхава / Гуру Ринпоче; Yeshe Tsogyal — Еше Цогьял; Sisirama — Сисирама; Mordiggian —
Мордиггиан; Tokabhaya — Токабхая; King of Fear — Царь Страха; Hard / Extreme roll — трудная / чрезвычайная проверка; pushed roll —
повторная проверка; bonus / penalty die — бонусная / штрафная кость; Know roll — проверка Знаний (ОБР).
Имена: Robert Frederick Moorcroft — Роберт Фредерик Муркрофт; Suraj Dhar — Сурадж Дхар; Isminder Veer Singh — Исминдер Вир
Сингх; Hasina Moiz — Хасина Моиз; Dr. Paira Mall — Пайра Малл; Celia Roberts — Селия Робертс; Moira Abernathy — Мойра Абернети;
Atif Baig — Атиф Байг; Ziab Ali — Зияб Али; Harit Peshin — Харит Пешин; James Strudwick — Джеймс Страдвик; Harold Hargreaves —
Гарольд Харгривз; Neha — Неха; Shri Badat — Шри Бадат; Yathini — Ятхини; Miyokhay — Миёхай; Azu Jamsher — Азу Джамшер;
Nur Bakht — Нур Бахт; Soglio — Солио.
