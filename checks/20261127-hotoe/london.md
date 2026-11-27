# Horror on the Orient Express — часть london (кн. II, с. 1–44, 233–241)

Книга `hotoe-book-2-en` (Chaosium 2014, 7e; «Dancers in an Evening Fog» — Джефф Гиллан при участии Л. Н. Изинуилла и Майка
Лэя; «The Doom Train» — Джефф Гиллан при участии Марка Моррисона). Смещение −2 подтверждено по изображениям (с. 30 = физ.
32, с. 233 = физ. 235). Дополнительно: `hotoe-book-6-handouts-en` с. 9–20, 55, 57 (раздатка и копии планов),
`hotoe-keeper-maps-en` 1 и `hotoe-player-maps-en` 1 (карты Лондона 1923 года). Русского издания нет: весь русский текст —
наш перевод (`translated`, Р-251). Решения: Р-254, Р-251, Р-202, Р-206, Р-209, Р-154.

## Файлы части

- Записи: 89 — этапы 2 (`scenarios/dancers-in-an-evening-fog`, `scenarios/the-doom-train`), сцены 22, места 30 (6 районов,
  13 зданий и мест Лондона, включая комнату Стэнли и дом Баттера, 7 комнат лавки Макрьята, Поезд рока и 3 его части), персонажи 12,
  раздатка 11, предметы 5, организации 2, карты 4 — в `kb/books/hotoe-book-2-en/`; общее заклинание 1 —
  `kb/spells/doom-gate.json` («Врата рока», нового в базе не было).
- Карты: `app/maps/hotoe-london-city-1923.jpg` (Keeper Maps 1), `hotoe-london-city-1923-players.jpg` (Player Maps 1),
  `hotoe-london-the-shop.jpg` (с. 235), `hotoe-london-british-museum.jpg` (с. 241).
- Картинки: `art-london.json` → `art-london-proposals.json` (25: 6 портретов, 8 иллюстраций, 11 раздаток; копии
  `app/art/**/hotoe-london-*.webp`) — применены к своим записям. План Лондона с. 44 («The Pictorial Plan of London») —
  картинка общего города: копия `app/art/locations/hotoe-london-pictorial-plan.webp`, предложение — в
  `proposals-london.json`.
- `proposals-london.json` — 27 предложений к 6 чужим записям (пробный прогон `apply.py --dry-run` проходит):
  `coc:organization:brothers-of-the-skin` (абзац HOTOE, эпоха 1920s, ссылки, источники), `coc:spell:control-skin`
  (версия кн. II, с. 31), `coc:location:london` (абзац 1923 года, ссылки, источники, картинка с. 44),
  `coc:location:british-museum` (абзац 1923 года, читальный зал, собрание Модсли, карта), `hotoe-book-2-en/location/fez-oriental-club`
  (сведения 1923 года — запись части fez; своей записи клуба часть london не заводит),
  `fears-sharp-little-needles-en/character/spilsbury-randolph-alexis` (`same_as`).
- `new-shared-locations-london.json` — черновик `coc:location:dover` (Дувр) и дополнение к черновику Кале части express.
- `atmosphere-london.json` — 15 страниц оформления и атмосферы.
- `completeness-london/`, `scenario-london/` — отчёты проверок (находки других частей ожидаемы).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| (форзац: фрагмент карты Франции и Швейцарии) | 1 | не взято — оформление (`atmosphere-london.json`) |
| Dedication; выходные данные | 2 | не взято — посвящение и выходные данные |
| Титульная страница | 3 | не взято |
| Table of Contents | 4–6 | не взято — оглавление; фото «Rue du Grenier-sur-l'Eau, Paris, 1923» (с. 6) — атмосфера |
| Book 2 — London 1923 — Dancers in an Evening Fog (вступление) | 7 | `scenario/dancers-in-an-evening-fog` — `summary`, `hook`, `advice` |
| London Handout #1 (What You Know About Your Friend, Prof. Smith) | 8 | `handout/london-handout-1-what-you-know-about-smith` |
| The Maudslay Collection | 8 | `scene/london-maudslay-collection`; `location/london-maudslay-collection` |
| The Challenger Lecture | 8–12 | `scene/london-challenger-lecture`; `organization/london-challenger-trust`; `location/london-imperial-institute` |
| (подпись) The Imperial Institute in Kensington; Beddows, the faithful… | 9 | картинка `london-imperial-institute`; второй портрет Беддоуза — атмосфера |
| Scenario Timeline | 10 | этап 1 — таблица «Лондон, январь 1923: хронология сценария» |
| Events in London in 1923 | 11 | этап 1 — таблица «Лондон, январь 1923: события»; абзац — предложение к `coc:location:london` |
| London 1923 Map | 12 | `map/london-city-1923` (источник) |
| After The Lecture | 12–13 | `scene/london-challenger-lecture` |
| The Plot Thickens | 13 | этап 1 — `keeper_info`; `character/mehmet-makryat`, `character/julius-smith` |
| The Newspapers | 13 | `scene/london-newspapers` |
| London Handout #2 (Man Dies Three Times in One Night) | 14 | `handout/london-handout-2-man-dies-three-times` |
| The Message | 14 | `scene/london-newspapers` |
| The Burned Man | 14–16 | `scene/london-burned-man`; `location/london-cheapside-bed-sit` |
| London Handout #3 (Professor's Home Burns) | 15 | `handout/london-handout-3-professors-home-burns` |
| London Handout #4 | 15 | `handout/london-handout-4-smiths-card` |
| What Professor Smith Says; Here Is What He Remembers of His Researches | 16 | `scene/london-burned-man` (списки «•») |
| What Beddows Knows | 16–17 | `scene/london-burned-man`; `item/london-beddows-valise` |
| London Handout #5 (Beddows' Notes) | 17 | `handout/london-handout-5-beddows-notes` |
| An Option for Keepers | 18 | `scene/london-burned-man`; этап 1 — `keeper_info`, `advice` |
| After The Meeting; Makryat Uncovered | 18 | `scene/london-burned-man` |
| Investigating the Professor: St. John's Wood; University of London; The Oriental Club | 18 | `scene/london-investigating-the-professor`; `location/london-smiths-house`, `london-university-of-london`; клуб — `location/fez-oriental-club` (часть fez) + предложение |
| The 1893 Diary | 19 | `scene/london-investigating-the-professor` (ссылки на раздатку дневника части fez) |
| The Multiple Murders: The Chelsea Arms; Scotland Yard; Makryat's Life; Embassy of Turkey | 19–20 | `scene/london-multiple-murders`; `location/london-chelsea-arms-hotel`, `london-turkish-embassy`; `character/inspector-fleming`, `mustapha-koprulu` |
| Makryat's Shop (подпись «Crescent Treasury») | 20–21 | `scene/london-makryats-shop`; `location/london-makryats-shop` и 7 комнат |
| The Shop Map | 21 | `map/london-the-shop` |
| A Curious Account Book Entry | 21 | `item/london-makryat-account-books`; `scene/london-makryats-shop` |
| A Final Visit | 21–22 | `scene/london-final-visit` |
| London Researches | 22 | `scene/london-researches`; `location/london-british-museum-reading-room` |
| A Portent | 22 | `scene/london-portent`; `item/london-wentworth-skin-note` |
| Richard Wentworth | 23 | `character/richard-wentworth`; `scene/london-portent` |
| Leaving England | 23 | `scene/london-leaving-england`; `location/london-croydon-aerodrome`; Дувр — `new-shared-locations-london.json` |
| A Word for the Keeper | 23 | этап 1 — `advice` |
| British Museum Map | 24 | `map/london-british-museum` (источник) |
| What Mehmet Does Next; Mehmet's Interventions; Mehmet's Telegrams | 25 | `scene/london-what-mehmet-does-next`; `character/mehmet-makryat` |
| Telegram Handout #1–#4 (тексты и пояснения) | 25–26 | `handout/london-telegram-1` … `london-telegram-4` |
| What Mehmet Does Next (Continued); Telegrams — Extra Information | 26 | `scene/london-what-mehmet-does-next` (три примера «•»); телеграммы 2–4 |
| Telegram Handout #1–#4 (бланки) | 27–28 | `handout/london-telegram-1` … `-4` (источники) |
| Blank Telegram Handout ×2 | 29 | `handout/london-telegram-blank` |
| Statistics: Dr. Julius Smith; James Beddows; Mehmet Makryat | 30–31 | `character/julius-smith`, `james-beddows`, `mehmet-makryat` |
| Fire Vampire | 31 | статблок совпадает с видом `coc:creature:fire-vampire` (Р-79) — числа в `mechanics` сцены `london-burned-man` |
| Spell: Control Skin | 31 | предложение к `coc:spell:control-skin` |
| London and Beyond 1923 — The Doom Train (вступление) | 32 | `scenario/the-doom-train` — `summary` |
| Another Fine Mess; Keeper's Background | 32–33 | `scene/doom-another-fine-mess`; этап 2 — `keeper_info` |
| This 1923 Scenario is Optional | 32 | этап 2 — `advice`; `scene/doom-another-fine-mess` |
| London Handout #6 (Man Disappears In Cloud Of Smoke) | 33 | `handout/london-handout-6-man-disappears` |
| The Alexis Family | 33–34 | `scene/doom-alexis-family`; `character/randolph-alexis`, `albert-alexis` |
| The Bed-Sitting Room | 34 | `scene/doom-bed-sitting-room`; `location/doom-stanley-bed-sit`; `character/constance-atkins` |
| The Local Police | 34–35 | `scene/doom-bed-sitting-room` |
| London Train-Spotters | 35 | `scene/doom-train-spotters`; `location/doom-butter-house`; `organization/doom-london-train-spotters-association`; `character/arthur-butter` |
| The Association Dinner | 36 | `scene/doom-train-spotters` (список «•») |
| A Curious Remembrance | 36 | `scene/doom-train-spotters` |
| The Train Set | 36–37 | `scene/doom-train-set`; `item/doom-train-set` |
| Researching The Original | 37 | `scene/doom-researching-the-original` |
| The Doom Train | 37–38 | `scene/doom-the-doom-train`; `location/doom-the-doom-train` (корабль), `doom-locomotive` |
| The First Carriage | 38–39 | `scene/doom-first-carriage`; `location/doom-first-carriage` |
| On Board | 39 | `scene/doom-first-carriage` |
| The Second Carriage | 40 | `scene/doom-second-carriage`; `location/doom-second-carriage` |
| The Plan | 40–41 | `scene/doom-second-carriage`; `item/doom-meat-pattern` |
| Back to Earth | 41 | `scene/doom-back-to-earth` |
| Conclusion; Resources | 42 | `scene/doom-back-to-earth`; этап 2 — `conclusion` |
| Statistics: Arthur Butter; Henry Stanley; Randolph Alexis | 42 | `character/arthur-butter`, `henry-stanley`, `randolph-alexis` |
| Ten Dead Passengers, Aboard the Doom Train | 43 | `character/dead-passengers` (групповой профиль, 10 вариантов) |
| Doom Gate | 43 | `coc:spell:doom-gate` (новое общее заклинание) |
| (The Pictorial Plan of London) | 44 | предложение картинки к `coc:location:london` (Р-249) |
| London Keeper's Map | 233 | `map/london-city-1923` |
| London Players' Map | 234 | `map/london-city-1923-players` |
| The Shop | 235 | `map/london-the-shop` |
| Telegram Handout #1–#4 | 236–237 | телеграммы 1–4 (источники) |
| Blank Telegram Handout | 238–239 | `handout/london-telegram-blank` |
| British Museum — Plan of the Ground Floor | 241 | `map/london-british-museum` |
| Keeper Maps 1 «London 1923» | — | `map/london-city-1923` (картинка) |
| Player Maps 1 «London 1923» | — | `map/london-city-1923-players` (картинка) |
| Book VI: Dancers in an Evening Fog — London Handouts #1–#5, Telegrams #1–#4, Blank Telegram, The Doom Train — London Handout #6 | VI: 9–20 | картинки раздаток (11); пустые обороты (с. 10, 12, 14, 16, 18, 20) — не взяты |
| Book VI: The Shop; British Museum (копии для игроков) | VI: 55, 57 | источники `map/london-the-shop`, `map/london-british-museum` (совпадают с планами Хранителя) |

## Не взято

- Передние страницы книги II (с. 1–6: форзац с картой, посвящение Линну Уиллису, выходные данные, титул, оглавление) и
  физ. 1–2 (обложка, реклама Chaosium) — не материал сценария; картинки — в `atmosphere-london.json`.
- Повторные портреты Смита (с. 10, 13) и Беддоуза (с. 9), рисунок парома (с. 23), рисунок паровоза (с. 39), газетная тумба
  на полях — атмосфера/оформление (`atmosphere-london.json`); у записей — портреты с подписями со с. 30.
- Карта Лондона: значки вокзалов без подписей и рамка «Reference» отдельными метками не размечены; подписи районов и
  зданий без своих записей (Camden, Primrose Hill, Battersea, Battersea Park, Claridge's, The Ritz, Old Bailey,
  Fenchurch St., London Bridge Sta., Victoria Station, Shoreditch, Bethnal Green, Whitechapel, Victoria Park, Rotherhithe,
  Bermondsey, Bloomsbury, Regents Park, Marylebone station) ведут на город или район с пояснением в `text` — своих записей
  не заведено: текста о них в книге нет (кандидаты для части companion).
- План Британского музея: 84 зала из ключа — метки на `coc:location:british-museum` с названием в `text` (Р-120), а не
  отдельные записи: о залах в книге нет ничего, кроме названия; номера 32 и 47 на плане не найдены (32 нет и в ключе).
- Упомянутые без записи: детектив-сержант Ригби (раздатка Лондон 3), доктор Альфред П. Модсли, жена Смита Маргарет,
  миссис Алексис, сержант участка Сток-Ньюингтона, Дж. Темпл Терстон,
  Иоганн Винкельман и доктор Милован Тодорович (персонажи глав trieste и belgrade — только в тексте раздатки), граф
  Коллоредо, Эдвард Келли, Вилем Рожмберк, Хуан Вальверде де Амуско, Кюри, Маркони, фон Цеппелин, Эдисон, доктор Кейвор —
  остаются текстом сцен и раздатки.
- Места без записи: больница Университетского колледжа, госпиталь для ветеранов, поместье Смита под Кембриджем, банк
  «Сосьете Женераль» в Константинополе (текст сцены; место — у части constantinople), постоялый двор у места крушения,
  река крушения 1897 года, место столкновения (≈ 96 км к северо-западу) — текстом сцен.
- Кожаный дьявол (Skin Devil), ползучая плоть, «чужая кожа» — существа без статблока в этих главах (кн. IV); в тексте.
- Огненный вампир (с. 31) — своей записи не получил: числа совпадают с видом (Р-79); в HOTOE нет объединённой атаки и
  заклинаний вида.

## Опечатки и сомнения

- Комплекция 1 при БкУ +0 у Артура Баттера (СИЛ+ТЕЛ 120), Генри Стэнли (105) и Рэндольфа Алексиса (95) — должна быть 0;
  `errata` записей (как напечатано).
- Мёртвые пассажиры: общие БкУ +1d4 и Комплекция 1, но у Пятого и Восьмого СИЛ+ТЕЛ 120 (БкУ 0, Комплекция 0); общая
  Скорость 6 при правилах 7–8 (возможно, медлительность мёртвых); ПЗ Второго 14 (округление вверх, Р-161) — `errata`.
- Карта Лондона: нумерация ключа в Keeper Maps 1 и в книге (с. 12, 233) разная (в пометке карты — обе); на с. 233 у № 3
  лишняя цифра «7» без кружка; «Prof. Smith's Hideout» стоит у Бетнал-Грина, а текст (с. 14, 16) — Чипсайд (`errata` места
  и `note` метки).
- Раздатка Лондон 4: подпись Book VI — «BOOK II, PAGE 14», в книге — с. 15.
- Задание называет телеграммы 1–3; в книге их четыре (№ 4 — «Goods in Société Générale») — взяты все.
- «Makyrat» (с. 18, 26, 33), «St John's Woods» (раздатка 3), «Persuade 31 %», «Science (Linguistics 60%)» — мелкое
  оформление (Р-39), не записано.
- «Болгарская война 1875 года» (раздатка 5) — как напечатано.
- Возраст Рэндольфа Алексиса 59 при «почти не постарел за четверть века» — как напечатано.
- Заклинания Мехмета «Contact Skinless One» и «Turn To Skin» в справочнике нет — их статьи в кн. IV, с. 62–64 (часть
  constantinople); в статблоке — как напечатано без ссылки.
- Рэндольф Алексис — тот же оккультист, что в «Спилсбери № 9485» («Fears Sharp Little Needles»): `same_as` с обеих
  сторон (предложение); кандидат в общую запись по Р-154 — решение ведущего.
- Восточный клуб уже заведён частью fez (`fez-oriental-club`, все эпохи) — часть london ссылается на него; сведения 1923
  года — предложением (оно опирается на кусок текста её описания: если fez его изменит, предложение не ляжет).
- Аэродром Кройдон (`london-croydon-aerodrome`) — если часть express заведёт свой, записи нужно свести.

## Ссылки на записи других частей (пока не существуют)

`hotoe-book-4-en/character/selim-makryat` (constantinople), `hotoe-book-2-en/scenario/the-blood-red-fez` (fez),
`hotoe-book-4-en/scenario/the-fog-lifts`, `…/by-the-skin-of-the-teeth` (return, constantinople), `coc:location:belgrade`,
`coc:location:sofia` (belgrade, sofia).

## Термины (английский → русский)

| English | Русский |
|---|---|
| Dancers in an Evening Fog | Танцоры в вечернем тумане (как в записи кампании) |
| The Doom Train; Doom Gate; Dead Passengers; Doom Kiss | Поезд рока; Врата рока; мёртвые пассажиры; поцелуй рока |
| Sedefkar Simulacrum; Sedefkar Scrolls | Симулякр Седефкара; Свитки Седефкара |
| Shunned Mosque | Отверженная мечеть |
| Brothers of the Skin; Skinless One | Братья кожи; Бескожий |
| Skin Devil | кожаный дьявол |
| Control Skin; Flesh Creeper; Skin Walker; Curse of the Putrid Husk | Управлять кожей; ползучая плоть; «чужая кожа»; Проклятие гниющей оболочки (по справочнику) |
| Challenger Lecture; Challenger Trust (trustees) | Челленджеровская лекция; попечители Челленджеровских лекций |
| Imperial Institute; Oriental Club; University of London | Имперский институт; Восточный клуб; Лондонский университет |
| Maudslay Collection | собрание Модсли |
| Reading Room (British Museum Library) | читальный зал Британского музея |
| Chelsea Arms Hotel; Turkish Embassy; Scotland Yard | отель «Челси Армс»; посольство Турции; Скотленд-Ярд |
| Crescent Treasury; Brophy Lane | «Сокровищница полумесяца»; Брофи-лейн |
| St. John's Wood; Cheapside; Islington; Stoke Newington; Camberwell; Kensington; Marylebone | Сент-Джонс-Вуд; Чипсайд; Излингтон; Сток-Ньюингтон; Камберуэлл; Кенсингтон; Мэрилебон |
| Croydon Aerodrome; Dover; Calais; Calais coaches; Boat-Train | аэродром Кройдон; Дувр; Кале; вагоны Кале; поезд к парому |
| Thomas Cook & Son; Compagnie Internationale des Wagons-Lits | «Томас Кук и сын»; Международная компания спальных вагонов |
| Telegraph Restant (poste restante) | до востребования |
| Société Générale | «Сосьете Женераль» |
| Deutschen Order (Teutonic Knights) | Тевтонский орден |
| The Devil's Simulare | «Дьявольский симуляр» |
| London Train Spotters' Association; train-spotter | Лондонская ассоциация любителей поездов; любитель поездов |
| Wrightson special-commission train set | игрушечная железная дорога «Райтсон» (особый заказ) |
| meat-pattern | петля из внутренностей (мясной узор) |
| bed-sitting room (bed-sit) | меблированная комната |
| haunting / haunter; curtains of perception; paraphysicality | призрак; занавес восприятия; парафизика |
| capsule universe | «капсульная» вселенная |
| Paraphysical Researcher | исследователь паранормального |
| Bon Mot; Detect Fraud; Maneuver For Knighthood; Parapsychology | Острое словцо; Распознать обман; Хлопоты о посвящении в рыцари; Парапсихология (навыки без механики) |
| Clean Shoes; Etiquette; Fashion; Remain Imperturbable | Чистка обуви; Этикет; Мода; Невозмутимость |
| Train Lore; Whimper; Linguist; Art (Skin Human) | Знание поездов; Хныканье; Лингвист; Искусство (свежевание людей) |
| Cult Skinning Knife; Quoit (thrown); Rusty Knife | культовый нож для свежевания; кольцо-кистень (метательное); ржавый нож |
| Mehmet Makryat; Selim Makryat; Julius Arthur Smith; James Beddows | Мехмет Макрьят; Селим Макрьят; Джулиус Артур Смит; Джеймс Беддоуз |
| Randolph Alexis; Albert Alexis; Henry Stanley; Arthur Butter; Constance Atkins | Рэндольф Алексис; Альберт Алексис; Генри Стэнли; Артур Баттер; Констанс Аткинс |
| Inspector Fleming; Mustapha Köprülü; Richard Wentworth; Walter Partridge | инспектор Флеминг; Мустафа Кёпрюлю; Ричард Уэнтворт; Уолтер Партридж |
| Extreme Intelligence roll | чрезвычайная проверка ИНТ |
| Les Fleurs du Mal; The Blood Red Fez; The Dreamlands Express; The Fog Lifts; By the Skin of the Teeth | «Цветы зла»; «Кроваво-красная феска»; «Экспресс Страны грёз»; «Туман рассеивается»; «На волосок» (как в записи кампании) |
