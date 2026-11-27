# HOTOE, часть dreamlands — книга II, с. 131–180, 254–255 (2026-11-27)

«The Dreamlands Express: Dreamlands 1923» (Пенелопа Лав), этап `hotoe-book-2-en/scenario/the-dreamlands-express`
(`part_of` кампании, `order` 5, необязательный). Источники: `hotoe-book-2-en` (печатная = физическая − 2),
`hotoe-keeper-maps-en` лист 13 (карта Хранителя), `hotoe-book-6-handouts-en` с. 39–44, 79, 81 (копии для игроков).
Русский текст — наш перевод (флаг `translated`, Р-251). Решения: Р-254, Р-251, Р-190, Р-189, Р-206, Р-150, Р-125.

## Записи (104)

| Вид | Записи |
|---|---|
| scenario (1) | `the-dreamlands-express` (таблицы «Список пассажиров», «Расписание для Хранителя») |
| scene (24) | `dream-boarding-the-dreamlands-express`, `dream-waking-world-investigations`, `dream-settling-in-at-ulthar`, `dream-dylath-leen-new-passengers`, `dream-the-diplomacy-game-begins`, `dream-zar-the-madman`, `dream-murder-on-the-dreamlands-express`, `dream-there-has-been-a-murder`, `dream-the-second-murder`, `dream-the-confession`, `dream-aphorat-the-second-banquet`, `dream-after-dinner-diplomacy`, `dream-an-undiscovered-murder`, `dream-thalarion-meeting-the-sorcerer`, `dream-xura-the-ghoul-that-was-guillaume`, `dream-a-break-in-diplomacy`, `dream-aira-remembrance`, `dream-sona-nyl-the-royal-passenger`, `dream-king-kuranes-judgment`, `dream-serannian`, `dream-the-attack-on-the-express`, `dream-the-vengeful-dead`, `dream-the-sorcerer-and-the-crone`, `dream-journeys-end` |
| character (14) | `henri-peeters`, `mac-mackenzie`, `karakov`, `madame-bruja` (2 облика — `variants`), `zsusza`, `the-madman` (имя придумано, Р-150), `mironim-mer` (2 облика), `blackjack`, `sophie`, `sarnathian-delegation` (групповой профиль, 6 вариантов), `haragrim`, `nadamens`, `the-sorcerer` (имя придумано, Р-150), `king-kuranes` (без статблока) |
| creature (8) | `dream-beings-of-ib` (6 вариантов, `same_as` naedine-s-prilivom-ru), `dream-squeaker`, `dream-nightgaunt-stokers` (`instance_of` ночного призрака, 6 вариантов), `dream-shantaks` (`instance_of` шантака, 6), `dream-trench-rats` (`instance_of` стаи крыс), `dream-alien-dream-train-beasts`, `dream-vengeful-dead`, `dream-eidolon-lathi` |
| location (35) | поезд `dream-dreamlands-express` (корабль) и вагоны `dream-express-engine` (1), `-fuel-tender` (2), `-baggage-van` (3), `-padded-compartment` (3, часть багажного), `-bath-house` (4), `-sleeping-compartments` (5–6), `-mens-saloon` (7), `-banqueting-hall` (8), `-kitchen` (8, часть зала), `-ladies-parlor` (9), `-cat-compartment` (10); `dream-ulthar-station` (под `coc:location:ulthar`); города и земли маршрута `dream-zar`, `dream-aphorat`, `dream-thalarion`, `dream-xura`, `dream-aira`, `dream-sona-nyl` (+ `dream-crystal-headlands`), `dream-serannian`, `dream-gulf-of-nodens`; подписи карты, упомянутые в тексте: `dream-nir`, `dream-hatheg`, `dream-river-skai` (под Ултаром), `dream-river-zuro`, `dream-forest-of-parg`, `dream-the-south`, `dream-zak`, `dream-cuppar-nombo`, `dream-karthian-hills`, `dream-hills-of-implan`, `dream-sydathria`, `dream-mnar`, `dream-ib` |
| map (4) | `dream-dreamlands-map` (Keeper Maps 13, 30 меток), `dream-dreamlands-map-players` (кн. VI с. 81), `dream-dreamlands-trains` (с. 255, 20 меток), `dream-dreamlands-trains-players` (кн. VI с. 79) |
| item (7) | `dream-lovers-heart`, `dream-karakovs-trunk`, `dream-macs-briefcase`, `dream-zsuszas-dancer-statuette`, `dream-madmans-soapstone-head`, `dream-karakovs-cutlass`, `dream-madame-brujas-valise` |
| handout (7) | `dream-handout-1-dreamlands-express-ticket`, `dream-handout-2-the-lovers-heart`, `dream-handout-3-in-memory-of-aira`, `dream-handout-4-death-of-an-arms-dealer`, `dream-menu-welcoming-banquet`, `dream-menu-second-banquet`, `dream-menu-royal-feast` |
| rule (4) | `dream-technology-in-the-dreamlands`, `dream-death-and-injury-in-the-dreamlands`, `dream-dreamlands-skills`, `dream-dream-artifacts` |

Картинки: карты `app/maps/hotoe-dreamlands-*.jpg` (4); портреты и раздатка — `app/art/{characters,handouts}/hotoe-dreamlands-*.webp`
(12, сопоставление `art-dreamlands.json`, предложения `art-dreamlands-proposals.json` применены к своим записям).
Атмосферные иллюстрации — `atmosphere-dreamlands.json` (7 страниц). Предложения к общим записям — `proposals-dreamlands.json` (37).
Скрипты — `.cache/lead-tools/gen-hotoe-dreamlands/` (`gen_*.py`, `maps.py`, `crop.py`).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| The Dreamlands Express (титул, подзаголовок, автор) | 131 | этап `the-dreamlands-express`: `name`, `summary` |
| An Option for Keepers | 131 | этап: `hook`, `summary` |
| A Dream Option (врезка) | 131 | этап: `advice` |
| Keeper’s Information | 131–132 | этап: `keeper_info`; поезд `dream-dreamlands-express`; Анри |
| Technology in the Dreamlands | 132 | правило `dream-technology-in-the-dreamlands` |
| Death and Injury in the Dreamlands | 132–133 | правило `dream-death-and-injury-in-the-dreamlands` |
| Dreamlands Skills (врезка): Dreaming (1/5 Power), Dream Lore (1/2 Cthulhu Mythos) | 133 | правило `dream-dreamlands-skills`; предложения к `coc:skill:dreaming`, `coc:skill:lore` |
| Investigator Information | 133 | сцена `dream-boarding-the-dreamlands-express` |
| Boarding the Dreamlands Express; Ulthar Station; The Dream Conducteur; The Passengers | 134 | та же сцена; место `dream-ulthar-station`; Анри |
| The Train Arrives | 134–135 | та же сцена; существо `dream-alien-dream-train-beasts` |
| A Ticket to Dream; Dreamlands Handout #1 | 135 | та же сцена; раздатка `dream-handout-1-dreamlands-express-ticket` |
| The Train Departs; Waking From the Dream | 135–136 | та же сцена |
| The Express of All Times | 136 | поезд `description`; этап `keeper_info` |
| The Dreamlands Express: Henri Peeters; Story | 136 | персонаж `henri-peeters` |
| Dream Artifact (Анри) | 137 | `henri-peeters` `legend` |
| The Alien Dream-Train Beasts | 137 | существо `dream-alien-dream-train-beasts` |
| Menials of the Dreamlands Express | 137 | поезд `description` («Прислуга»); существо зверей (щупальца-слуги) |
| Strange Companions; Dream Artifacts | 137 | правило `dream-dream-artifacts`; этап, таблица «Список пассажиров» |
| The Carriages (врезка, с. 138–140): The Engine, The Fuel Tender, The Baggage Van, The Padded Compartment, The Bath House, The Sleeping Compartments, The Men’s Saloon, The Banqueting Hall, The Kitchen, The Ladies Parlor, The Cat Compartment | 138–140 | вагоны `dream-express-*` (11 мест) |
| Passenger List (врезка) | 141 | этап, таблица «Список пассажиров» |
| Sarrubians and Sarnathians | 141 | этап `advice`; `mironim-mer`, `sarnathian-delegation` |
| “Mac” Mackenzie; Story; Dream Artifact | 141–142 | `mac-mackenzie`; предмет `dream-macs-briefcase` |
| Monsieur Karakov; Story; Dream Artifact: Karakov’s Trunk | 142–143 | `karakov`; предмет `dream-karakovs-trunk`; существо `dream-trench-rats` |
| Madame Bruja; Story; Dream Artifact | 143–144 | `madame-bruja`; предметы `dream-madame-brujas-valise`, `dream-lovers-heart` |
| Dreamlands Handout #2: The Lovers’ Heart | 144 | раздатка `dream-handout-2-the-lovers-heart` |
| Mironim-Mer; Story; Dream Artifact | 144–145 | `mironim-mer` |
| The Beings of Ib; Story; Dream Artifact | 145 | существа `dream-beings-of-ib`, `dream-squeaker` |
| The Sarnath Delegation; Story; Dream Artifact | 145–146 | `sarnathian-delegation` |
| Zsusza; Story; Dream Artifact | 146 | `zsusza`; предмет `dream-zsuszas-dancer-statuette` |
| The Madman; Story; Dream Artifact | 146 | `the-madman`; предмет `dream-madmans-soapstone-head` |
| The Ghoul that was Guillaume; Story; Dream Artifact | 147 | предложения к `coc:character:guillaume-ghoul` (легенда, источники, эпоха); сцена `dream-xura-the-ghoul-that-was-guillaume` |
| The Sorcerer; Story; Dream Artifact | 147 | `the-sorcerer` |
| Waking World Investigations: Henri Peeters, “Mac” Mackenzie, Karakov, Zsusza, Madame Bruja, The Sorcerer, The Madman, Guillaume, The Lovers’ Heart | 147–149 | сцена `dream-waking-world-investigations` |
| (карта на с. 148) | 148 | карта `dream-dreamlands-map` (источник) |
| The Journey; Keeper’s Timetable | 149–150 | поезд `description`; этап, таблица «Расписание для Хранителя»; `advice` |
| Welcoming Banquet Menu | 150 | раздатка `dream-menu-welcoming-banquet` |
| Ulthar; Events; Departure; The Journey to Dylath-Leen | 150–151 | сцена `dream-settling-in-at-ulthar`; предложение к `coc:location:ulthar` |
| Settling In; Dream Artifact Creation; Meeting Blackjack; The First Banquet; Blackjack and Henri | 151 | та же сцена; правило `dream-dream-artifacts`; `blackjack`, `sophie` |
| Dylath-Leen; Events; Arrival; Departure; The Journey to Zar | 151–153 | сцена `dream-dylath-leen-new-passengers`; предложение к `coc:location:dylath-leen` |
| The Doomed Cities of Sarnath and Ib (врезка) | 153 | сцена `dream-the-diplomacy-game-begins`; `dream-beings-of-ib`; `dream-ib`; предложение к `coc:location:sarnath` |
| New Passengers; The Golden-Eyed Man; The Sarnath Delegation; The Beings of Ib; Zsusza’s Arrival | 153–154 | сцена `dream-dylath-leen-new-passengers` |
| The Diplomacy Game Begins; Beings of Ib; The Sarnath Delegation; Sarnathian Pranks; Waking | 154–155 | сцена `dream-the-diplomacy-game-begins` |
| Zar; Events; Arrival; Departure; The Journey to Aphorat; New Passenger | 155 | место `dream-zar`; сцена `dream-zar-the-madman` |
| Murder on the Dreamlands Express; Events After Lunchtime; The First Murder; Finding the Body; The Body | 156 | сцена `dream-murder-on-the-dreamlands-express` |
| Events When the Body Is Found; There Has Been a Murder...; The Dreamers’, Karakov’s, Madame Bruja’s, Mironim-Mer’s, Mac’s, Zsusza’s Compartment; The Padded Compartment; The Sarnathian Compartment; The Cat Compartment (и «Questioning …») | 157–159 | сцена `dream-there-has-been-a-murder`; предмет `dream-karakovs-cutlass` |
| The Second Murder; Mironim-Mer Captured; Mironim-Mer Victorious | 159–160 | сцена `dream-the-second-murder` |
| The Confession; Conclusion; Waking | 160 | сцена `dream-the-confession` |
| Aphorat; Events; Arrival; Departure; The Journey to Thalarion | 160–161 | место `dream-aphorat`; сцена `dream-aphorat-the-second-banquet` |
| Second Banquet Menu | 161 | раздатка `dream-menu-second-banquet` |
| The Second Banquet | 161 | сцена `dream-aphorat-the-second-banquet` |
| After-Dinner Diplomacy; The Beings of Ib; The Sarnathians; Karakov and the Diplomacy Game | 161–162 | сцена `dream-after-dinner-diplomacy` |
| An Undiscovered Murder? | 162 | сцена `dream-an-undiscovered-murder` |
| Thalarion; Events; Arrival; Departure; The Journey to Xura; Meeting the Sorcerer; The Eidolon Lathi | 162–164 | место `dream-thalarion`; сцена `dream-thalarion-meeting-the-sorcerer`; существо `dream-eidolon-lathi` |
| The Land of Xura; Events; Arrival and Departure; The Journey to Aira; New Passenger | 164–165 | место `dream-xura`; сцена `dream-xura-the-ghoul-that-was-guillaume` |
| A Break in Diplomacy; Henri Intervenes | 165 | сцена `dream-a-break-in-diplomacy` |
| Aira; Events; Arrival; Departure; The Journey to Sona-Nyl; Remembrance; The Burial of Blackjack | 165–166 | место `dream-aira`; сцена `dream-aira-remembrance` |
| Dreamlands Handout #3: In Memory of Aira | 166 | раздатка `dream-handout-3-in-memory-of-aira` |
| Sona-Nyl; Events; Arrival; Departure; The Journey to Serannian | 166–168 | места `dream-sona-nyl`, `dream-crystal-headlands`; сцена `dream-sona-nyl-the-royal-passenger` |
| Royal Feast Menu | 168 | раздатка `dream-menu-royal-feast` |
| The Royal Passenger; The Third Banquet (Royal Feast) | 168 | сцена `dream-sona-nyl-the-royal-passenger`; `king-kuranes` |
| King Kuranes’ Judgment; The Murder Charge; Conclusion | 168–169 | сцена `dream-king-kuranes-judgment` |
| Serannian; Arrival; Departure; Events | 169–170 | место `dream-serannian`; сцена `dream-serannian`; предложение к `coc:location:celephais` |
| The Gulf of Nodens; Arrival and Departure; The Attack on the Express; Timeline of the Attack (врезка) | 170–171 | место `dream-gulf-of-nodens`; сцена `dream-the-attack-on-the-express` |
| Allies: The Beings of Ib, The Cats of Ulthar, Guillaume, The Nightgaunts, Mac Mackenzie, The Madman, Mironim-Mer, Zsusza | 171–172 | сцена `dream-the-attack-on-the-express` |
| The Vengeful Dead; The First Wave: Cavalry; The Second Wave: The Cannon; The Third Wave: The Submarine; How to Stop the Dead; Is Henri Killed? | 172–173 | сцена `dream-the-vengeful-dead`; существо `dream-vengeful-dead` |
| The Sorcerer and the Crone; Madame Bruja; The Lovers’ Heart (текст и врезка) | 173–174 | сцена `dream-the-sorcerer-and-the-crone`; предмет `dream-lovers-heart` |
| Journey’s End; What of the Others? | 174–175 | сцена `dream-journeys-end`; этап `conclusion` |
| Dreamlands Handout #4: Death of an Arms Dealer | 175 | раздатка `dream-handout-4-death-of-an-arms-dealer` |
| Statistics: Passengers — Mr. “Mac” Mackenzie, Karakov, Madame Bruja (Human Dream Form, Crone Form), Zsusza | 176 | статблоки соответствующих персонажей |
| The Ghoul That Was Guillaume (статблок) | 176–177 | предложение к `coc:character:guillaume-ghoul` (статблок совпадает, Р-125) |
| The Madman; Mironim-Mer (Human Dream Form, True Alien Form) | 177 | `the-madman`, `mironim-mer` |
| Cats: Blackjack; Sophie | 177–178 | `blackjack`, `sophie` |
| Diplomats: Sarnathians; Beings of Ib; Squeaker | 178 | `sarnathian-delegation`, `dream-beings-of-ib`, `dream-squeaker` |
| King Kurane’s Guardians: Haragrim; Nadamens | 178–179 | `haragrim`, `nadamens` |
| Staff: Henri Peeters; Nightgaunts | 179 | `henri-peeters`, `dream-nightgaunt-stokers` |
| Enemies: Trench Rats; The Sorcerer; Shantaks | 180 | `dream-trench-rats`, `the-sorcerer`, `dream-shantaks` |
| Credits | 180 | `mironim-mer`, `haragrim` (`legend`/`sources`); этап `sources` |
| Dreamlands Map | 254 (+ с. 148; Keeper Maps 13; кн. VI с. 81) | карты `dream-dreamlands-map`, `dream-dreamlands-map-players` |
| Dreamlands Trains | 255 (+ с. 138; кн. VI с. 79) | карты `dream-dreamlands-trains`, `dream-dreamlands-trains-players` |

## Не взято

- Подписи карты Страны грёз без текста в главе (метки не поставлены, записей нет): Oorotha(?), Kirin, Drinen, Golthoth, Mt. Hatheg-Kla,
  Oukranos, Iranian Desert, The Stony Desert, Mt. Sidrak, Oonai, Sinara, Teloth, Ilarnek, Akurion, Fantastic Realm, роза ветров
  (Lengward, Mnarward, Mhorward, Zakward) — география Страны грёз, о которой глава ничего не говорит (перечислено в `quality.notes` карт).
- Упомянутые без записи (только в тексте записей): патриарх Атал, кот Фортуна (спутник Миронима-Мера), Захарофф, принц Дийлат-Лина,
  Очи Дийлат-Лина и Чёрные галеры (в тексте сцены и в предложении к Дийлат-Лину), гора Лерион, Панг, Бахарна, Сарруб и Безымянное озеро,
  Мтал, статуя Бокруга (у «Наедине с приливом» есть `naedine-s-prilivom-ru/item/idol-bokruga` — связь не ставилась), дочь спасённой
  Анри дамы — без механики, по одной фразе.
- Атмосферные иллюстрации (с. 131, 132, 152, 154, 167, 169, 175) — `atmosphere-dreamlands.json`.

## Опечатки и сомнения книги

- Мадам Бруха, человеческий облик: ПЗ 20 при (ВЫН 100 + ТЕЛ 70)/10 = 17; облик Старухи: Комплекция 1 при СИЛ+ТЕЛ 200 (ожидается 2);
  Уклонение в обоих обликах «25% (25/10)» → доли исправлены на 12/5 (Р-35, Р-77).
- Жужа: «Dancer Statuette 50% (22/9)» → доли исправлены на 25/10; ПЗ 11 при 10,5 — округление вверх (приём книги).
- Безумец: после «Move:» пусто (по правилам 9).
- Мироним-Мер: строка «ED 99+» вместо «EDU»; возраст «9,280»/«9280».
- Сарнатцы: одна Скорость 8 на всех; у Дульсе и Бесвит по правилам 9.
- Надаменс: нет строки «Damage Bonus» (по СИЛ 85 + ТЕЛ 80 — +1d6), а урон булавы «1D10 + 1D4».
- Колдун: ПМ 90 при МОЩ 90 (обычно 18); нет Комплекции и Скорости.
- «Squeaker, Speaker for the Beings if Ib» (if → of); «King Kurane’s Guardians» (Kuranes’).
- Серанниан (с. 170): страница легенды о Сердце названа «Dreamlands Handout #1» — должно быть #2 (исправлено в сцене).
- Кн. VI: копия Раздатки 2 подписана «Book II, page 1044» (с. 144).
- Расписание: отправление из Аиры 13:00 (с. 149), в тексте 14:00 (с. 166); врезка названа «Keeper’s Timestable» (с. 150).
- «Sydathria» на карте, «Sydarthian groves» в тексте.
- Блэкджек: Скорость 10 (кошачья) — проверка производных значений выдаёт предупреждение по человеческому правилу (9); оставлено, пометка в `quality.notes`.

## Термины (англ. → рус.)

Глоссарий (`tools/terms.py`) и записи базы: Dreamlands → Страна грёз (реестр владельца; в старых записях — «Страна снов»);
Dreaming → Сновидение; Dream Lore → Тайные знания (сновидения) (официальная форма «Книги хранителя»; в глоссарии — «Знание Страны грёз», наш вариант,
review); Waking World → Мир яви; Black Galley → Чёрная галера; Zoog → зуг; Nightgaunt → ночной призрак; Shantak → шантак; Ghoul → упырь;
The Ghoul That Was Guillaume → Упырь, что был Гийомом; Ulthar → Ултар; Dylath-Leen → Дийлат-Лин; Celephaïs → Селефаис; Sarnath → Сарнат;
Oriab, Ngranek → Ориаб, Нгранек; Nodens → Ноденс; Haunter of the Dark → Скиталец тьмы; Orient Express → Восточный экспресс;
Dread Curse of Azathoth → Зловещее проклятье Азатота; Melt Flesh → Плавление плоти; Mindblast → Взрыв мозга; Wrack → Разрушение;
Contact Bokrug → Связь с божеством: Бокруг; Summon Shantak → ссылка на «Заклинания призыва» (`coc:spell:summon-bind`).

Новые формы этой части (одна на термин): The Dreamlands Express → Экспресс Страны грёз; Henri’s Unusual Train of Dreams → Необычный поезд
снов Анри; Dream Conducteur → кондуктор снов; dream artifact → артефакт сна; Henri Peeters → Анри Петерс; “Mac” Mackenzie → «Мак» Маккензи;
Monsieur Karakov → месье Караков; Madame Bruja → мадам Бруха; the Crone → Старуха; the Sorcerer → Колдун; The Lovers’ Heart → Сердце
влюблённых; Zsusza → Жужа; The Madman → Безумец; Mironim-Mer → Мироним-Мер; the Golden-Eyed Man → Золотоглазый человек; Sarrub, Sarrubian →
Сарруб, саррубиец; Sarnathian → сарнатец; Sarnath Delegation → делегация Сарната; Theophed, Amor, Caromel, Ibex, Dulce, Besweet → Теофед,
Амор, Каромель, Ибекс, Дульсе, Бесвит; Beings of Ib → существа Иба; Ib → Иб; Squeaker → Пищалка; Bokrug → Бокруг; DOOM → РОК; Blackjack →
Блэкджек; Sophie → Софи; Fortune → Фортуна; King Kuranes → король Куранес; Haragrim → Харагрим; Nadamens → Надаменс;
Atal → Атал; Eidolon Lathi → эйдолон Лати; Akariel → Акариэль; Trench Rats → окопные крысы; Vengeful Dead → мстительные мёртвые;
the Alien Dream-Train Beasts → звери поезда снов; Engine → Локомотив; Fuel Tender → Тендер; Baggage Van → Багажный вагон;
Padded Compartment → мягкий отсек; Bath House → Баня; Sleeping Compartments → спальные вагоны; Men’s Saloon → Мужской салон;
Banqueting Hall → Банкетный зал; Ladies Parlor → Дамская гостиная; Cat Compartment → Кошачий вагон; Ulthar Station → станция Ултар;
Zar → Зар (Abode of Unformed Dreams → Обитель Невоплощённых Грёз); Aphorat → Афорат; Thalarion → Таларион (City of a Thousand Wonders →
Город Тысячи Чудес); Xura → Ксура (Land of Pleasures Unattained → Страна Недостижимых Наслаждений); Aira → Аира; Iranon → Иранон;
Sona-Nyl → Сона-Нил (Land of Fancy → Страна Фантазии); Crystal Headlands → Хрустальные мысы; Serannian → Серанниан; Gulf of Nodens →
Бездна Ноденса; Skai → Скай; Zuro → Зуро; Nithra → Нитра; Kra → Кра; Nir → Нир; Hatheg → Хатег; Pang → Панг; Baharna → Бахарна;
Forest of Parg → лес Парг; The South / South Land → Южная страна; Zak → Зак; Mount Lerion → гора Лерион; Cuppar-Nombo → Куппар-Номбо;
Karthian hills → Картианские холмы; Implan → Имплан; Mount Aran → гора Аран; Mtal → Мтал; Sydathria / Sydarthian → Сидатрия /
сидартианский; Bnazic desert → пустыня Бназ; Mnar → Мнар; magah birds → птицы магах; yath-trees → деревья ят; thagweed → тагвид;
quagga → квагга; Cats from Saturn → кошки с Сатурна; Eyes of Dylath-Leen → Очи Дийлат-Лина; Zoog moon-tree wine → лунное вино зугов;
Eastern Fungus Forest → Восточный Грибной лес; Ziegfeld Follies → «Безумства Зигфелда»; Zaharoff → Захарофф.

## Ссылки на записи, которых ещё нет

Нет: все ссылки моих записей существуют (часть-кампания `hotoe-book-1-en/scenario/horror-on-the-orient-express` и
`hotoe-book-1-en/location/express-simplon-orient-express` уже в базе).

## Вопросы и кандидаты

- Общая запись «Страна грёз» (`coc:location:dreamlands`) как верхнего уровня для Ултара, Дийлат-Лина, Селефаиса, Сарната и земель
  этой главы — сейчас земли верхнего уровня заведены типом «город сценария», как Ориаб и Кадат.
- Кандидаты в общие записи: король Куранес (персонаж Лавкрафта), существа Иба (есть ещё в «Наедине с приливом»), Серанниан (владение
  Селефаиса).
- Анри Петерс 1893 года («Кровавая феска», с. 63) — без статблока; запись заведена здесь, часть fez добавит своё предложением.
- Предложение `coc:skill:dreaming` `base` = «1/5 МОЩ» (`formula: varies`) меняет справочник — на решение ведущего.
