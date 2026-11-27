# «The Children of Fear» — часть peking (глава 1 «The City of Decaying Splendor», с. 29–50, 347, 363–365, 383)

Записи: `kb/books/children-of-fear-en/*/peking-*`, этап `scenarios/the-city-of-decaying-splendor.json`, персонажи
`wang-enlai`, `hsu-te-chuan`, `wu-pei-fu`, общий город `kb/locations/peking.json`; карты `app/maps/cof-peking-*.jpg`;
картинки `app/art/**/cof-peking-*.webp`. Генератор и вырезки — `.cache/lead-tools/gen-cof-peking/` (после применения
картинок `run_all.py` не перезапускать: он перезапишет записи без `images`).

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 1: The City of Decaying Splendor — Peking, China (вступление: Пекин 1920-х, Уорнер, телеграмма) | 29 | этап `the-city-of-decaying-splendor` (summary, keeper_info); город `coc:location:peking` |
| China: The Middle Kingdom | 29–31 | rule `peking-china-the-middle-kingdom` |
| Taking Liberties (врезка) | 29 | rule `peking-taking-liberties` |
| Opposite: Peking, the decaying city of splendor (подпись) | 29 | атмосфера (`atmosphere-peking.json`, физ. 29) |
| Coin of the Realm: China (врезка) | 30 | rule `peking-coin-of-the-realm-china` (таблица курсов) |
| About Money (врезка) | 30 | rule `peking-about-money` |
| The Jade Marshal (врезка) | 31 | персонаж `wu-pei-fu` (legend) |
| Peking: The Northern Capital | 31–34 | город `coc:location:peking` (description, history); районы `peking-legation-quarter`, `peking-tartar-city` и др. |
| No Entry (врезка) | 31 | место `peking-forbidden-city` |
| Avenues and Alleyways (врезка) | 32 | город (абзац «Проспекты и переулки»); `peking-pata-hutung` |
| The Imperial Gate of Peking (подпись) | 32 | атмосфера |
| Opposite: The City of Peking map / карта «The City of Peking» | 32–33 | map `peking-city-of-peking` (30 меток); таблица «Пекин: места на карте» у города; 41 запись мест |
| Pagodas in the Peking countryside (подпись) | 34 | атмосфера; `peking-environs` |
| Peking’s Weather (врезка) | 34 | город (абзац «Погода») |
| Peking Timeline (Early 20th Century) (врезка) | 34 | город, таблица «Пекин: хронология начала XX века» |
| Set Up: An Educational Invitation | 35 | этап (hook); scene `peking-an-educational-invitation` |
| Handout: Decaying Splendor 1, 2 (копии на странице главы) | 35 | handouts `peking-handout-1-lecture-invitation`, `peking-handout-2-note-from-wang-enlai` (картинки — с приложения F) |
| Dramatis Personae: Wang Enlai | 36 | персонаж `wang-enlai` (background, legend); портрет |
| Dramatis Personae: Sofian Bazaz-Wain | 36–37 | этап (keeper_info «Действующие лица»); предложение к `sofian-bazaz-wain` (часть appendix) |
| Getting There | 37 | scene `peking-an-educational-invitation` |
| Where to Stay | 37–38 | scene `peking-an-educational-invitation`; город; отели `peking-hotel-des-wagons-lits`, `peking-hotel-du-nord`, `peking-grand-hotel-de-pekin` |
| The American School of Archaeology (врезка) | 37 | место `peking-american-school-of-archaeology`; `peking-yenching-university` |
| Start: The Lecture | 38 | scene `peking-on-the-way`; место `peking-university` |
| On the Way | 38–39 | scene `peking-on-the-way` |
| The Chinese Quarter of Peking (подпись) | 38 | атмосфера; `peking-chinese-city` (alias) |
| Keeper note (наблюдатели, проверка МОЩ, Внимание) | 39 | scene `peking-on-the-way` (mechanics); этап (advice) |
| Late Arrivals | 39 | scene `peking-late-arrivals`; место `peking-examination-hall-5` |
| Many Voices: Chinese Dialects (врезка) | 39 | rule `peking-many-voices-chinese-dialects` |
| Visions in the Dark (список видений, Keeper note о «Send Vision») | 40–41 | scene `peking-visions-in-the-dark`; таблица «Видения во тьме» этапа |
| Mr. Bazaz-Wain’s lecture (подпись) | 40 | атмосфера |
| Keeper note (несчастливое число четыре) | 41 | scene `peking-visions-in-the-dark`; место `peking-examination-hall-5` |
| Keeper Note: Crib Notes (врезка) | 41 | scene `peking-late-arrivals`; этап (advice) |
| Rising Tensions (врезка) | 41 | rule `peking-rising-tensions` |
| (студенты освистывают лектора, Рассудок 0/1) | 41, 43 | scene `peking-the-students-protest` |
| Handout: Decaying Splendor 3 | 42 | handout `peking-handout-3-silk-road-lecture-notes` |
| A Conversation over Canapes | 43–44 | scene `peking-a-conversation-over-canapes` |
| Handout: Decaying Splendor 4 | 43 | handout `peking-handout-4-warners-telegram` |
| Making Plans | 44 | scene `peking-making-plans` |
| An Unseasonable Storm | 44–45 | scene `peking-an-unseasonable-storm`; место `peking-hsi-chi-men-gate` |
| Prof. Wang’s Office | 45–46 | scene `peking-prof-wangs-office`; место `peking-prof-wangs-office`; предметы `peking-travel-permit`, `peking-purse-of-silver-dollars`, `peking-chest-of-flags`, `peking-expedition-cars` |
| Some Sights of Peking: The Lama Temple, The Temple of Heaven, The Observatory | 45 | места `peking-lama-temple`, `peking-temple-of-heaven`, `peking-observatory`; scene `peking-making-plans` |
| Expedition Logistics (врезка) | 46 | rule `peking-expedition-logistics` |
| On the Road | 47 | scene `peking-on-the-road`; этап (последний шаг → `to-the-gates-of-the-sun`) |
| Travel by Map (врезка) | 47 | rule `peking-travel-by-map` (ссылка на `coc:rule:pulp-red-lining`) |
| A Dodge Model 30-35 and the Peking Countryside (подпись) | 47 | картинка у `peking-expedition-cars` |
| Non-Player Characters (вступление: Базаз-Уэйн — с. 405) | 48 | этап (keeper_info) |
| Wang Enlai (статблок) | 48 | `wang-enlai` statblock |
| Chinese Soldier (статблок), сержант Hsu Te-Chu’an | 48 | `peking-chinese-soldiers` (групповой, 6 имён), `hsu-te-chuan`; организация `peking-chihli-clique` |
| The shrines and temples of Peking (подпись) | 48 | атмосфера |
| Driver (статблок, военные водители) | 49 | `peking-drivers` (вариант «Военный водитель») |
| Soldiers of the Beiyang Army (подпись) | 49 | картинка у `peking-chinese-soldiers` |
| (с. 50 — полностраничный арт, опенинг главы 2) | 50 | атмосфера |
| Appendix C: What Your Investigator Knows (вступление) + 1: China and Peking | 347 | handout `peking-knows-1-china-and-peking` (вступление приложения — в описании) |
| Appendix F: Player Handouts and Maps (вступление), Decaying Splendor 1–4 | 363–365 | handouts 1–4 (картинки и текст — отсюда) |
| Player Maps: The City of Peking | 383 | map `peking-city-of-peking-players` |

## Не взято

- Колонтитулы, номера страниц, декоративная вертикальная надпись «agartha» на полях — оформление.
- Подпись «Overleaf: Central Asia map» (с. 383) — карта части campaign.
- Атмосферные иллюстрации (с. 28/29, 32, 34, 38, 40, 48, 50) — не картинки записей, список в `atmosphere-peking.json`.
- Портрет Софиана Базаз-Уэйна (с. 36): запись `sofian-bazaz-wain` (часть appendix) ещё не создана — вырезка лежит в
  `.cache/lead-tools/gen-cof-peking/img/bazaz-wain.png`, ведущему решить (лист прегена на с. 405 — вероятно, крупнее).
- Тяньцзинь не заведён записью (нет хозяина) — черновик общего города в `new-shared-locations-peking.json`.
- Отдельные записи для «Цюаньцзюйдэ», аэродрома Наньюань, Старого Летнего дворца, Китайской лекторской ассоциации,
  Геологической службы Китая, Джона Лейтона Стюарта, Адема (брата Базаз-Уэйна) не заведены: упомянуты мимоходом, без
  описания — остаются текстом в городе, сценах и записях людей.

## Опечатки и сомнения

- Винтовка M1888 у китайских солдат — урон «1D6+1» (с. 48), как у винтовки .22 таблицы; у армейской винтовки ждали бы
  2d6+4. В записи — как напечатано, `errata` у `peking-chinese-soldiers`.
- Ключ карты: «Moham Medam Mosque» (= Mohammedan Mosque), «Tung-Chin-Men» (в тексте других источников Tung-Chih-Men),
  «Hsi-Chi-Men» (в тексте с. 44 — Hsi-chih-men), «Hotel des Wagon-Lits» (верно Wagons-Lits) — печатные формы в
  `name.en`/`aliases`, пометки в `quality.notes`.
- «Jade Marshall» (с. 31, текст) при заголовке «The Jade Marshal» — словесная, не записана (Р-39).
- Шанс пистолета сержанта Сюй Дэцюаня (55%) и навыки военных водителей — вывод из текста (Р-41), в `corrections`.
- Штемпель телеграммы (Decaying Splendor 4) — «PEKING 3 UU 30 35 C.T.O.», передан как виден.
- Русские названия ворот 21–30 — передача подписей карты, отождествление с современными только там, где его даёт книга
  (Сичжимэнь, Гуаньаньмэнь, Цяньмэнь); Дунчжимэнь и др. — наш вывод.

## Термины (английский → русский)

| English | Русский |
|---|---|
| Peking (Beijing, Dadu, Beiping/Peiping) | Пекин (Бэйцзин, Даду, Бэйпин/Пэйпин) |
| Tartar (Inner) City | Татарский (Внутренний) город |
| Outer (Chinese) City | Китайский (Внешний) город |
| Imperial City / Forbidden City | Императорский город / Запретный город |
| (Foreign) Legation Quarter | Посольский квартал |
| Tiananmen Square | площадь Тяньаньмэнь |
| Lama (Yonghe) Temple | Ламаистский храм Юнхэгун |
| Temple of Heaven | храм Неба |
| Yenching University | Яньцзинский университет |
| American School of Archaeology | Американская школа археологии |
| Peking University | Пекинский университет |
| China Lecture Association | Китайская лекторская ассоциация |
| szuho-yuan (siheyuan) / hu-t’ung (hutong) | сыхэюань / хутун |
| Pata (Bada) Hu-t’ung | Бада-хутун |
| Tashihlan (Dashilan) | улица Дашилань |
| Hotel des Wagons-Lits / Hotel du Nord / Grand Hotel de Pekin | отель «Вагон-Ли» / отель «Дю Нор» / Гранд-отель де Пекин |
| Magic Lantern | волшебный фонарь |
| Tokabhaya / Children of Fear | Токабхая / Дети страха |
| Send Vision | «Наслать видение» (заклинание; русское имя — за частью appendix) |
| Wang Enlai | Ван Эньлай |
| Wu Pei-fu (the Jade Marshal) | У Пэйфу (Нефритовый маршал) |
| Hsu Te-Chu’an | Сюй Дэцюань |
| Sofian Bazaz-Wain | Софиан Базаз-Уэйн |
| Langdon Warner | Лэнгдон Уорнер |
| Mi Han | Ми Хань |
| Chihli Clique / Fengtien Clique / Beiyang | Чжилийская клика / Фэнтяньская клика / Бэйян |
| Kuomintang (KMT) / National Revolutionary Army | Гоминьдан / Национально-революционная армия |
| warlord | милитарист |
| Sian (Xi’an, Chang’an) | Сиань (Чанъань) |
| Tun-huang | Дуньхуан |
| Kansu (Corridor), Souchou | Ганьсу (коридор Ганьсу), Сучжоу |
| Caves of the Thousand Buddhas | пещеры Тысячи Будд |
| Tarim Basin / Taklamakan / Silk Road(s) | Таримская впадина / Такла-Макан / Шёлковый путь (пути) |
| Fogg Museum | Музей Фогга |
| Tientsin (Tianjin) | Тяньцзинь |
| Ch’ien-men / Chang-y-men (Guang’anmen) / Hsi-chih-men | ворота Цяньмэнь / Чжанъимэнь (Гуаньаньмэнь) / Сичжимэнь |
| Marco Polo Bridge | мост Марко Поло |
| silver dollar, fen, wen, tael | серебряный доллар, фэнь, вэнь, лян |
| Ma-tao saber | сабля ма-дао |
| Mauser Broomhandle M1912 | пистолет «Маузер» M1912 «Ручка от метлы» |
| Language (Chinese) / Chinese (Own) | Иностранный язык (китайский) / Родной язык (китайский) |
| POW roll / Hard POW roll / Know roll | проверка МОЩ / трудная проверка МОЩ / проверка Знаний |
| red lining | «красная линия» |
| Tsongkhapa, Gelug (Yellow Hat), Maitreya | Цзонхава, Гелуг («жёлтые шапки»), Майтрейя |
