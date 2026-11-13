# Аркхэм: дополнение по путеводителю Hort (`arkham-guide-hort-ru`) — покрытие

Источник: «Путеводитель по Аркхэму» (Hort; по Arkham Unveiled 6e, адаптация к 7e; издание trusted, печатная страница =
физическая, с. 1–111). Решение Р-234: основа Аркхэма — путеводитель Chaosium 2023 года (`arkham-en`); Hort дополняет его тем,
чего в книге 2023 нет, и русскими формами названий и имён. Русский текст Hort — источник для его записей (флаг `translated`
не ставится). Числа Hort, расходящиеся с книгой 2023, в характеристики не переносились — только пометкой в `quality.notes`.

Итог: **6 новых записей**, **734 предложений** к **320 записям** в `proposals-hort.json`
(append aliases: 142, append refs: 6, append sources: 305, replace description: 39, replace history: 1, replace legend: 16, replace text: 1, set aliases: 66, set quality: 158). Пробный прогон `pipeline/integrate/apply.py --dry-run` — без ошибок;
применение на копии базы с `tools/check.py` — 0 ошибок, 0 предупреждений.

Номера Hort (101–139, 201–244, 301–310, 401–458, 501–513, 601–628, 701–723, 801–817, 901–917, 1001–1015) — своя нумерация,
с номерами 2023 не совпадает; соответствие найдено по названию, адресу и описанию.

## Новые записи

| Запись | Что |
|---|---|
| `coc:rule:arkham-hort-loan-calculator` | «Кредитный калькулятор (Hort)» (с. 12–13): модификаторы, бросок 1d100, сроки; таблица базовых вероятностей банков (с. 20, 34, 38) |
| `arkham-guide-hort-ru/character/laban-shrewsbury` | Лабан Шрюсбери (с. 16–17, 79–80), статблок как напечатан; `same_as` Pulp-записи |
| `arkham-guide-hort-ru/character/nathaniel-corey` | Натаниэль Кори, пациент Института Ларкина (с. 96) |
| `coc:location:arkham-hort-billingtons-wood` | Биллингтонский лес (1001, с. 102–103): дом, книги, витраж, призрак Биллингтона, башня |
| `arkham-guide-hort-ru/creature/lurker-at-the-threshold` | Таящийся у порога (с. 103), статблок; `related_to` Йог-Сотот |
| `coc:location:arkham-hort-kingsport-head` | Кингспортский мыс (1014, с. 111): будущая радиостанция, дом на туманном утёсе |

## Покрытие: раздел или место Hort → запись базы

| Раздел/место Hort | Страница | Запись базы | Что сделано |
|---|---|---|---|
| Предисловие | 8 | место Аркхэма (около 10 км к северу от Салема, трасса 1А у Уэнхема и Гамильтона; 35 км до Бостона, билет $2,20), время действия — октябрь 1928 года, население меньше половины салемских 45 000 — пометка у `coc:location:arkham`; рекомендации рассказов Лавкрафта — не взято | — |
| История Аркхэма | 9–11 | `coc:location:arkham` | абзац «По путеводителю Hort», пометка в quality.notes |
| Экономика | 12 | `coc:location:arkham`; `coc:rule:arkham-getting-around` | абзац «По путеводителю Hort»; пометка в quality.notes |
| Кредитный калькулятор | 12–13 | `coc:rule:arkham-hort-loan-calculator` | **новая запись** |
| Репутация и навык Средств | 13 | `coc:rule:arkham-reputation` | абзац «По путеводителю Hort» |
| Законы и полиция | 13–14 | `coc:rule:arkham-law-and-order` | пометка в quality.notes |
| Климат | 14 | `coc:rule:arkham-about` | пометка в quality.notes |
| Лавкрафтовские фамилии | 14 | не взято: тот же список фамилий, что в `coc:table:arkham-names-1/-2`, в иной транслитерации (Беллингхэм, Бэрроуз, Вэйланд, Гэммелл, Дэнфорт, Кэррингтон, Лаймен, Мэтер, Хэторн, Хольт и т. п.); единственная фамилия без пары в таблицах 2023 — «Саллон» | — |
| Путеводитель по Аркхэму (нумерация домов) | 15 | то же, что в `coc:rule:arkham-neighborhoods` («Улицы и переулки»): отсчёт от перекрёстка Мэйн- и Гаррисон-стрит, чётные справа, дробные номера — не взято как повтор | — |
| Нортсайд (вступление) | 15 | `coc:location:arkham-northside` — совпадает с книгой 2023, ничего нового | — |
| 101. Насосная станция и водонапорная башня | 15 | `coc:location:arkham-101-pump-house-water-tower` | пометка в quality.notes |
| 102. Поттерс-филд | 16 | `coc:location:arkham-102-potters-field` | псевдоним |
| 103. Лабан Шрюсбери | 16–17 | `coc:location:arkham-104-renforth-residence`; `arkham-guide-hort-ru/character/laban-shrewsbury` | абзац «По путеводителю Hort»; **новая запись** |
| 104. Спикизи | 17–18 | `coc:location:arkham-113-the-speakeasy`; `arkham-en/character/northside-sam-flinn`; `arkham-en/character/northside-mikey-catchpole`; `arkham-en/character/northside-larry-freen` | пометка в quality.notes; псевдоним, пометка в quality.notes; абзац «По путеводителю Hort», пометка в quality.notes; псевдоним, абзац «По путеводителю Hort», пометка в quality.notes |
| 105. Средняя школа Дженкина | 18 | `coc:location:arkham-107-jenkin-public-school` | псевдоним, пометка в quality.notes |
| 106. Апартаменты «Гардиан» | 18 | `coc:location:arkham-109-guardian-apartments` | псевдоним, абзац «По путеводителю Hort» |
| 107. Масонская ложа | 19 | `arkham-en/organization/northside-arkham-masonic-lodge` | пометка в quality.notes |
| 108. «Аркхэм газетт» | 19 | `coc:location:arkham-gazette`; `arkham-en/character/northside-willard-peck`; `arkham-en/character/northside-michael-crane` | пометка в quality.notes; пометка в quality.notes; совпадает с 2023 |
| 109. Театр «Мэнли» | 20 | `arkham-en/organization/northside-arkham-amateur-theatre-company`; `coc:location:arkham-106-manley-theater`; `arkham-en/character/northside-elizabeth-peabody` | пометка в quality.notes; совпадает с 2023; совпадает с 2023 |
| 110. «Джедидия Марш и партнёры» | 20 | `coc:location:arkham-111-jedediah-marsh-associates` | псевдоним, пометка в quality.notes |
| 111. Апартаменты «Террас» | 20 | `coc:location:arkham-112-terrace-building-apartments`; `arkham-en/character/northside-minnie-coleman` | псевдоним, пометка в quality.notes; абзац «По путеводителю Hort» |
| 112. Аркхэмское кредитное агентство | 20–21 | `coc:location:arkham-114-arkham-loan-agency` | абзац «По путеводителю Hort» |
| 113. Аркхэмская угольно-топливная компания | 21 | `coc:location:arkham-115-arkham-fuel-coal` | псевдоним |
| 114. Стройплощадка | 21 | `coc:location:arkham-116-construction-site` | псевдоним, пометка в quality.notes |
| 115. Апартаменты Хардингов | 21 | `coc:location:arkham-117-harding-boarding-house`; `arkham-en/character/northside-jin-lillibridge`; `arkham-en/character/northside-william-harding`; `arkham-en/character/northside-grace-harding` | псевдоним; абзац «По путеводителю Hort»; совпадает с 2023; совпадает с 2023 |
| 116. Пекарня Тарановски | 21 | `coc:location:arkham-118-taranowskis-bakery`; `arkham-en/character/northside-georgie-taranowski` | псевдоним; совпадает с 2023 |
| 117. Школа для современных женщин мисс Кристиан | 21 | `coc:location:arkham-120-miss-christians-school`; `arkham-en/character/northside-regina-christian` | псевдоним, пометка в quality.notes; совпадает с 2023 |
| 118. Деловой центр «Тауэр» | 22 | `coc:location:arkham-119-tower-professional-building`; `arkham-en/character/northside-ephraim-sprague`; `arkham-en/character/northside-gilroy-feldman`; `arkham-en/character/northside-elliot-stigleitz`; `arkham-en/character/northside-michael-stigleitz`; `arkham-en/character/northside-allen-turner`; `arkham-en/character/northside-sawyer-lyman`; `arkham-en/character/northside-james-gedney`; `arkham-en/character/northside-gordon-brown`; `arkham-en/character/northside-cedrick-manton`; `arkham-en/character/northside-august-manton`; `arkham-en/character/northside-edwin-cassidy` | псевдоним, пометка в quality.notes; псевдоним; псевдоним; псевдоним; псевдоним; совпадает с 2023; совпадает с 2023; совпадает с 2023; совпадает с 2023; совпадает с 2023; совпадает с 2023; совпадает с 2023 |
| 119. Дж.Дж.Эбботт, таксидермист | 22 | `coc:location:arkham-122-jj-abbott-taxidermist`; `arkham-en/character/northside-jerome-abbott` | псевдоним; пометка в quality.notes |
| 120. «Монеты и марки Хардвика» | 23 | `coc:location:arkham-121-hardwickes-stamps-coins`; `arkham-en/character/northside-chester-hardwicke` | псевдоним; совпадает с 2023 |
| 121. Прачечная Аптауна | 23 | `coc:location:arkham-124-uptown-laundry` | псевдоним |
| 122. Служба газетных вырезок | 23 | `coc:location:arkham-123-worldwide-clipping-service` | псевдоним |
| 123. Э.Э.Салтонстолл и партнёры | 23 | `coc:location:arkham-125-saltonstall-associates`; `arkham-en/character/northside-ellis-saltonstall` | псевдоним, пометка в quality.notes; псевдоним |
| 124. «Редкие книги и карты» | 23 | `coc:location:arkham-126-rare-books-maps`; `arkham-en/character/northside-edward-tillinghast` | абзац «По путеводителю Hort»; псевдоним, пометка в quality.notes |
| 125. Торговая палата Аркхэма | 23–24 | `arkham-en/organization/northside-arkham-chamber-of-commerce` | псевдоним, пометка в quality.notes |
| 126. «Аркхэмские сноповязалки» | 24 | `coc:location:arkham-128-arkham-baler-company` | псевдоним |
| 127. Аркхэмская автостанция | 24 | `coc:location:arkham-129-arkham-bus-line` | псевдоним, пометка в quality.notes |
| 128. «Аркхэм Адвертайзер» | 24–25 | `coc:location:arkham-advertiser`; `arkham-en/character/northside-roberta-henry`; `arkham-en/character/northside-harvey-gedney` | псевдоним; абзац «По путеводителю Hort», пометка в quality.notes; совпадает с 2023 |
| 129. Кафе «Безлюдная дорога» | 25 | `coc:location:arkham-132-desolate-highway-cafe`; `arkham-en/character/northside-reid-vandervelden`; `arkham-en/character/northside-josh-visser` | псевдоним, абзац «По путеводителю Hort»; псевдоним; совпадает с 2023 |
| 130. Гостиница «Борден Армс» | 25 | `coc:location:arkham-130-borden-arms-hotel`; `arkham-en/character/northside-alex-hearne` | псевдоним; псевдоним, пометка в quality.notes |
| 131. «Торговый дом» | 26 | `coc:location:arkham-133-commercial-house` | псевдоним, пометка в quality.notes |
| 132. Железнодорожный вокзал | 26 | `coc:location:arkham-134-bm-train-station`; `arkham-en/character/northside-bobby-ashbourne` | псевдоним; совпадает с 2023 |
| 133. «У тетушки Люси» | 26 | `coc:location:arkham-135-aunt-lucys-diner` | псевдоним |
| 134. Отель «Тильден Армс» | 27 | `coc:location:arkham-136-tilden-arms-hotel`; `arkham-en/character/northside-marvin-dunlap` | псевдоним; псевдоним, пометка в quality.notes |
| 135. Газетный киоск | 27 | `arkham-en/character/northside-ernie-casado` | пометка в quality.notes |
| 136. Музей восковых фигур Сандера | 27–28 | `coc:location:arkham-138-sanders-wax-museum`, `arkham-en/character/northside-pete-sander` — совпадает с книгой 2023 | — |
| 137. Столовая «Графтон» | 28 | `coc:location:arkham-139-grafton-diner` | псевдоним, пометка в quality.notes |
| 138. Территория железной дороги | 28 | `coc:location:arkham-140-railroad-properties` | псевдоним, абзац «По путеводителю Hort» |
| 139. Бартоломью Эппли IV | 28 | `coc:location:arkham-103-appley-residence`; `arkham-en/character/northside-bartholomew-appley` | пометка в quality.notes; псевдоним, пометка в quality.notes |
| Даунтаун (вступление) | 29–30 | `coc:location:arkham-sanitarium` | пометка в quality.notes |
| 201. Аркхэмская лечебница для душевнобольных | 30 | `coc:location:arkham-sanitarium`; `arkham-en/character/downtown-eric-hardstrom` | псевдоним, пометка в quality.notes; псевдоним |
| 202. Столовая «Флитфуд» | 30 | `coc:location:arkham-202-fleetwood-diner` | псевдоним |
| 203. Автобус до Иннсмута | 31 | `coc:location:arkham-203-innsmouth-bus-stop`; `arkham-en/character/downtown-joe-sargent` | псевдоним, пометка в quality.notes; совпадает с 2023 |
| 204. Кеннет Хит, частный детектив | 31–32 | `coc:location:arkham-205-heath-private-investigation`; `arkham-en/character/downtown-kenneth-heath` | псевдоним; пометка в quality.notes |
| 205. Ротари-клуб | 32 | `coc:location:arkham-206-rotary-club` | пометка в quality.notes |
| 206. Церковь Эсбери (М.Е.) | 32 | `coc:location:arkham-208-asbury-methodist-episcopal-church`; `arkham-en/character/downtown-ezekiel-wallace` | псевдоним, абзац «По путеводителю Hort», пометка в quality.notes; псевдоним |
| 207. Кредитное агентство «Даймонд» | 32 | `coc:location:arkham-209-diamond-credit-agency`; `arkham-en/character/downtown-randle-wade` | совпадает с 2023; псевдоним |
| 208. Аркхэмская публичная библиотека | 32 | `coc:location:arkham-211-public-library`; `arkham-en/character/downtown-ellen-whitmarsh` | абзац «По путеводителю Hort»; псевдоним |
| 209. Столовая «У пчёлки» | 32 | `coc:location:arkham-210-bees-diner` | псевдоним |
| 210. Суд и тюрьма | 33 | `coc:location:arkham-212-courthouse-and-jail`; `arkham-en/character/downtown-keezar-randall`; `arkham-en/character/downtown-lee-craig` | псевдоним, пометка в quality.notes; совпадает с 2023; псевдоним |
| 211. Площадь Независимости | 33–34 | `coc:location:arkham-218-independence-square` | пометка в quality.notes |
| 212. Кинотеатр «Теленьюс» | 34 | `coc:location:arkham-213-telenews-cinema` | совпадает с 2023 |
| 213. Ресторан «Кроуфорд» | 34 | `coc:location:arkham-219-crawfords-restaurant` | псевдоним |
| 214. Первый банк Аркхэма | 34 | `coc:location:arkham-214-arkham-first-bank` | абзац «По путеводителю Hort» |
| 215. Биллиардная Арта | 34 | `coc:location:arkham-220-arts-billiards` | псевдоним, пометка в quality.notes |
| 216. Бертран Чемберс, адвокат | 34–35 | `coc:location:arkham-215-a-bertrand-chambers-attorney`; `arkham-en/character/downtown-bertrand-chambers` | псевдоним; совпадает с 2023 |
| 217. Федеральное залоговое агентство | 35 | `coc:location:arkham-215-b-federal-bond-agency` | совпадает с 2023 |
| 218. Доктор Синдервальд, пластический хирург | 35 | `coc:location:arkham-207-dr-sinderwald-surgeon`; `arkham-en/character/downtown-garrison-sinderwald` | псевдоним; пометка в quality.notes |
| 219. Доктор Хайнрих Т.Мюльхиг | 35 | `coc:location:arkham-204-dr-muelhig-psychiatrist`; `arkham-en/character/downtown-heinrich-muelhig` | псевдоним; псевдоним, пометка в quality.notes |
| 220. Здание под снос | 35 | `coc:location:arkham-221-demolition-site` | псевдоним |
| 221. Ратуша | 35–36 | `coc:location:arkham-217-town-hall`; `arkham-en/character/downtown-darrell-slocum`; `arkham-en/character/downtown-joseph-peabody`; `arkham-en/character/downtown-janet-larkin` | псевдоним, абзац «По путеводителю Hort», пометка в quality.notes; псевдоним; пометка в quality.notes; совпадает с 2023 |
| 222. Аркхэмская газовая компания | 36 | `coc:location:arkham-222-arkham-gas-company` | совпадает с 2023 |
| 223. Аркхэмская телефонная компания («Белл») | 36 | `coc:location:arkham-223-arkham-bell-telephone` | псевдоним |
| 224. Аркхэмское трамвайное управление | 37 | `coc:location:arkham-224-arkham-trolleys` | псевдоним, абзац «По путеводителю Hort» |
| 225. Театр «Амхерст» | 37 | `coc:location:arkham-225-amherst-theater` | совпадает с 2023 |
| 226. Игровые автоматы «Пенни-аркада» | 37 | `coc:location:arkham-241-penny-arcade` | псевдоним, пометка в quality.notes |
| 227. Лавка мороженого Деннисона | 37 | `coc:location:arkham-226-dennisons-ice-cream-emporium` | псевдоним |
| 228. «Нортсайд-маркет» | 37 | `coc:location:arkham-227-northside-market`; `arkham-en/character/overview-robert-czyenck` | псевдоним; псевдоним |
| 229. Автомобильный двор Балларда | 37–38 | `coc:location:arkham-232-ballards-auto-lot`; `arkham-en/character/downtown-grainger-ballard` | псевдоним, пометка в quality.notes; пометка в quality.notes |
| 230. «Эдисон» | 38 | `coc:location:arkham-233-edison-electric-and-gas` | псевдоним |
| 231. Сберегательный банк долины Мискатоник | 38 | `coc:location:arkham-234-miskatonic-valley-savings-bank` | псевдоним, абзац «По путеводителю Hort» |
| 232. Полицейский участок | 38–39 | `coc:location:arkham-228-police-station`; `arkham-en/character/downtown-luther-harden`; `arkham-en/character/downtown-mickey-harrigan`; `arkham-en/character/downtown-calvin-stuckey`; `arkham-en/character/generic-police-sergeant`; `arkham-en/character/generic-police-patrol-officer`; `arkham-en/character/downtown-asa-nichols`; `arkham-en/character/downtown-william-keats` | псевдоним; пометка в quality.notes; псевдоним, пометка в quality.notes; пометка в quality.notes; пометка в quality.notes; пометка в quality.notes; псевдоним; совпадает с 2023 |
| 233. Почтамт | 41 | `coc:location:arkham-229-post-office`; `arkham-en/character/downtown-eli-whittaker` | псевдоним; совпадает с 2023 |
| 234. Аркхэмское такси | 41 | `coc:location:arkham-236-arkham-cab-co`; `arkham-en/character/downtown-gregory-dahlberg` | псевдоним, пометка в quality.notes; псевдоним |
| 235. Автозаправка «Phillips 66» | 41 | `coc:location:arkham-235-massgas-station`; `arkham-en/character/downtown-abel-sykes` | псевдоним, пометка в quality.notes; псевдоним |
| 236. Пожарная станция | 41 | `coc:location:arkham-230-fire-department`; `arkham-en/character/downtown-benijah-adams` | псевдоним; псевдоним |
| 237. Переплётная мастерская Бандена | 41–42 | `coc:location:arkham-237-bundens-bindery`; `arkham-en/character/downtown-malcolm-bunden` | совпадает с 2023; псевдоним |
| 238. Татуировальный салон | 42 | `coc:location:arkham-238-painless-tattoos`; `arkham-en/character/downtown-jin-pin-liou` | псевдоним; псевдоним, пометка в quality.notes |
| 239. Строительные товары Шихана | 42 | `coc:location:arkham-239-sheehan-contractor-supply`; `arkham-en/character/downtown-ed-sheehan` | совпадает с 2023; совпадает с 2023 |
| 240. Лесопилка Адамса | 42 | `coc:location:arkham-243-adams-lumber-yard` | псевдоним |
| 241. Бойня | 42 | `coc:location:arkham-244-slaughterhouse` | совпадает с 2023 |
| 242. Территория железной дороги | 43 | `coc:location:arkham-242-railroad-properties` | псевдоним |
| 243. Первая национальная бакалея | 43 | `coc:location:arkham-231-first-national-grocery`; `arkham-en/character/downtown-arthur-anderson` | псевдоним; совпадает с 2023 |
| 244. Арсенал Национальной Гвардии Массачусетса | 43 | `coc:location:arkham-216-massachusetts-guard-armory`; `arkham-en/character/downtown-william-hathorne`; `arkham-en/character/downtown-aubrey-bridgeton`; `arkham-en/character/downtown-charles-hart`; `arkham-en/character/downtown-stephen-groat` | пометка в quality.notes; псевдоним; совпадает с 2023; совпадает с 2023; совпадает с 2023 |
| Исттаун (вступление) | 44 | `coc:location:arkham-easttown` — совпадает с книгой 2023 (дороги шириной 40 футов, около 12 м; чёрные семьи, ведущие род с 1788 года) | — |
| 301. Дом Пикерингов | 44–45 | `coc:location:arkham-301-pickering-house` | псевдоним, пометка в quality.notes |
| 302. Первая унитарианская церковь Аркхэма | 45 | `coc:location:arkham-304-first-unitarian-church`; `arkham-en/character/easttown-willet-spencer` | совпадает с 2023; совпадает с 2023 |
| 303. Узница чердака | 45 | `coc:location:arkham-303-crawford-house`; `arkham-en/character/easttown-ellen-crawford` | псевдоним; псевдоним, пометка в quality.notes |
| 304. Трансформаторная подстанция Нортсайда | 45 | `coc:location:arkham-306-northside-transformer-station` | псевдоним |
| 305. Средняя школа Мартина | 46 | `coc:location:arkham-307-martin-public-school` | псевдоним |
| 306. Храм баптистской церкви | 46 | `coc:location:arkham-308-temple-baptist-church` | псевдоним, абзац «По путеводителю Hort» |
| 307. «Химикаты Андерсона» | 46 | `coc:location:arkham-309-andersons-chemical-supply` | совпадает с 2023 |
| 308. Льдохранилище | 46 | `coc:location:arkham-311-ice-house` | псевдоним |
| 309. Аркхэмская камвольная фабрика | 46 | `coc:location:arkham-310-arkham-worsted-mills` | совпадает с 2023 |
| 310. Дом Мелиссы Торн | 46 | `coc:location:arkham-305-thorne-house`; `arkham-en/character/easttown-melissa-thorne` | псевдоним; пометка в quality.notes |
| Торговый район (вступление) | 47 | `coc:location:arkham-merchant-district` | абзац «По путеводителю Hort» |
| 401. Старое заросшее кладбище | 48 | `coc:location:arkham-402-old-wooded-graveyard` | псевдоним |
| 402. Холм Висельника | 48–49 | `coc:location:arkham-403-hangmans-hill`; `arkham-en/character/merchant-goody-fowler` | псевдоним; пометка в quality.notes |
| 403. «Неименуемый» | 49 | `coc:location:arkham-404-old-crossham-house` | псевдоним, пометка в quality.notes |
| 404. «Аркхэмское молоко» | 49 | `coc:location:arkham-405-arkham-dairy` | псевдоним |
| 405. Элайджа, резчик по камню | 50 | `coc:location:arkham-406-elijah-the-stonecutter`; `arkham-en/character/merchant-elijah-potts` | псевдоним; пометка в quality.notes |
| 406. Школьный совет | 50 | `coc:location:arkham-407-public-schools-building`; `arkham-en/character/rivertown-joel-manton` | псевдоним, пометка в quality.notes; пометка в quality.notes |
| 407. Школа Хаббард | 50 | `coc:location:arkham-408-hubbard-grade-school` | псевдоним |
| 408. Западная Церковь | 50 | `coc:location:arkham-409-west-church` | псевдоним |
| 409. Безлюдный остров | 51 | `coc:location:arkham-401-unvisited-island` | псевдоним |
| 410. Доки | 52 | `coc:location:arkham-410-docks` | псевдоним |
| 411. Старые склады | 52 | `coc:location:arkham-411-commercial-warehouses` | псевдоним |
| 412. Грузоперевозки «Счастливый клевер» | 52–53 | `coc:location:arkham-412-lucky-clover-cartage`; `arkham-en/character/merchant-danny-obannion`; `arkham-en/character/merchant-bobby-sills`; `arkham-en/character/merchant-eddie-leery`; `arkham-en/character/merchant-walter-klein`; `arkham-en/character/merchant-tough-muggs` | псевдоним, абзац «По путеводителю Hort»; псевдоним, пометка в quality.notes; пометка в quality.notes; пометка в quality.notes; абзац «По путеводителю Hort», пометка в quality.notes; псевдоним, пометка в quality.notes |
| 413. Автозаправка и сервис «Эссо» | 55 | `coc:location:arkham-413-franks-service-station` | псевдоним, пометка в quality.notes |
| 414. Картинная галерея | 55 | `coc:location:arkham-414-gallery-of-art`; `arkham-en/character/merchant-andreas-ver-hoven` | псевдоним; псевдоним |
| 415. Охранные системы и сейфы Эйса | 55 | `coc:location:arkham-415-a-ace-alarms`; `arkham-en/character/merchant-richard-henry-ace` | псевдоним, абзац «По путеводителю Hort»; совпадает с 2023 |
| 416. Э.Паррингтон, оружейник | 55 | `coc:location:arkham-415-b-parrington-gunsmith`; `arkham-en/organization/merchant-arkham-gun-club`; `arkham-en/character/merchant-edward-parrington` | псевдоним; псевдоним, пометка в quality.notes; совпадает с 2023 |
| 417. Мебель и ковры Андерсона | 56 | `coc:location:arkham-416-andersons-furniture` | псевдоним, пометка в quality.notes |
| 418. Школа танцев Альфреда Мюррея | 56 | `coc:location:arkham-417-toledo-school-of-dance` | псевдоним, пометка в quality.notes |
| 419. Зоомагазин | 56 | `coc:location:arkham-418-a-cunninghams-pet-shop`; `arkham-en/character/merchant-albert-cunningham` | псевдоним; абзац «По путеводителю Hort» |
| 420. Музыкальный магазин Манелли | 56 | `coc:location:arkham-418-b-manellis-music-store`; `arkham-en/character/merchant-alberto-manelli` | абзац «По путеводителю Hort», пометка в quality.notes; совпадает с 2023 |
| 421. Сувениры и антиквариат | 56 | `coc:location:arkham-419-curios-antiques`; `arkham-en/character/merchant-george-tillinghast` | псевдоним; пометка в quality.notes |
| 422. Окулист | 57 | `coc:location:arkham-420-optometrist`; `arkham-en/character/merchant-bernard-evans` | псевдоним; пометка в quality.notes |
| 423. Часы Маллоя | 57 | `coc:location:arkham-421-a-malloys-timepieces`; `arkham-en/character/merchant-john-malloy` | псевдоним; псевдоним |
| 424. Радиотовары | 57 | `coc:location:arkham-421-b-radio-center`; `arkham-en/character/merchant-robert-valencia` | псевдоним; совпадает с 2023 |
| 425. Феннер Эйвери, табачник | 57 | `coc:location:arkham-422-a-tobacconist`; `arkham-en/character/merchant-fenner-avery` | псевдоним; совпадает с 2023 |
| 426. Оптика и необычные игрушки Уолтерса | 57 | `coc:location:arkham-422-b-walters-optics`; `arkham-en/character/merchant-timothy-walters` | псевдоним; абзац «По путеводителю Hort», пометка в quality.notes |
| 427. Элиша Уэйт, золотых дел мастер | 57–58 | `coc:location:arkham-424-waite-goldsmith`; `arkham-en/character/merchant-ewan-waite` | псевдоним; псевдоним, пометка в quality.notes |
| 428. Бутик Хэтти | 58 | `coc:location:arkham-425-a-hatties-boutique`; `arkham-en/character/merchant-hattie-obrian` | пометка в quality.notes; совпадает с 2023 |
| 429. Каселиус, ювелир | 58 | `coc:location:arkham-425-b-caselius-jewelers`; `arkham-en/character/merchant-lazlo-caselius` | псевдоним; пометка в quality.notes |
| 430. Галантерея Пайка | 58 | `coc:location:arkham-426-pikes-haberdashery` | совпадает с 2023 |
| 431. Конторские принадлежности Джилмена | 58 | `coc:location:arkham-428-gilmans-office-supplies` | псевдоним |
| 432. Салон красоты мисс Дженни | 58 | `coc:location:arkham-429-miss-jennys-beauty-parlor`; `arkham-en/character/merchant-jenny-aberstrom` | абзац «По путеводителю Hort»; совпадает с 2023 |
| 433. «Университетская обувь» | 58 | `coc:location:arkham-430-university-shoe-store` | совпадает с 2023 |
| 434. Книжный магазин Джейвил | 58 | `coc:location:arkham-432-a-jaywils-book-store`; `arkham-en/character/merchant-malcomb-jaywil` | псевдоним, пометка в quality.notes; совпадает с 2023 |
| 435. Университетский магазин | 59 | `coc:location:arkham-432-b-university-shop` | псевдоним |
| 436. Кондитерская Марша | 59 | `coc:location:arkham-433-marshs-confectionery` | совпадает с 2023 |
| 437. «Крогерс» | 59 | `coc:location:arkham-423-masse-groceries` | псевдоним, пометка в quality.notes |
| 438. Вулвортс 5&10 | 59 | `coc:location:arkham-435-woolworth` | псевдоним |
| 439. Восточные склады | 59 | `coc:location:arkham-444-easterly-warehouses` | псевдоним |
| 439. Восточные склады | 59 | у Hort одно место объединяет 2023 436 (деревянные склады к северу от Мейн-стрит, перестроенные в дешёвые дома) и 444 (склады на старой пристани, где разгружали хлопок и шерсть) — сведения уже есть в обоих | — |
| 440. Старые склады | 60 | `coc:location:arkham-436-old-warehouses` | совпадает с 2023 |
| 441. Газетный киоск | 60 | `coc:location:arkham-437-a-newsstand` | совпадает с 2023 |
| 442. Кафе «Колокольчик» | 60 | `coc:location:arkham-437-b-bell-cafe` | псевдоним |
| 443. Театральные принадлежности Марквила | 60 | `coc:location:arkham-438-markwils-theatrical-supply`; `arkham-en/character/merchant-ben-woodward` | псевдоним; псевдоним |
| 444. Кафетерий на Чёрч-стрит | 60 | `coc:location:arkham-440-church-street-cafeteria` | псевдоним |
| 445. Аптека Брайанта | 60 | `coc:location:arkham-441-bryants-apothecary`; `arkham-en/character/merchant-mather-bryant` | совпадает с 2023; пометка в quality.notes |
| 446. Пекарня Тарановски | 60 | `coc:location:arkham-442-taranowskis-bakery`; `arkham-en/character/overview-sheila-torsten` | пометка в quality.notes; совпадает с 2023 |
| 447. Подарочный магазин | 60–61 | `coc:location:arkham-443-arkham-gift-shop`; `arkham-en/character/merchant-edith-winkler` | псевдоним; псевдоним |
| 448. Епископальная церковь Христа | 61 | `coc:location:arkham-439-christchurch-episcopal`; `arkham-en/character/merchant-archibald-bishop` | псевдоним; совпадает с 2023 |
| 449. Калеб Маркхэм, слесарь | 61 | `coc:location:arkham-445-markham-locksmith`; `arkham-en/character/merchant-caleb-markham` | псевдоним, пометка в quality.notes; совпадает с 2023 |
| 450. Подержанные книги Хардена | 61 | `coc:location:arkham-446-hardens-used-books`; `arkham-en/character/merchant-herbert-harden` | пометка в quality.notes; совпадает с 2023 |
| 451. Б.Ф.Джонс, хозяйственные товары | 61 | `coc:location:arkham-447-jones-hardware`; `arkham-en/character/merchant-ben-francis-jones` | псевдоним; совпадает с 2023 |
| 452. Продуктовый магазин Бенсона | 61 | `coc:location:arkham-448-bensons-market`; `arkham-en/character/merchant-jasper-benson` | псевдоним; совпадает с 2023 |
| 453. «Одежда со скидкой» | 62 | `coc:location:arkham-449-bargain-house-clothiers` | псевдоним |
| 454. «Караван Стюарта» | 62 | `coc:location:arkham-450-stewarts-caravan`; `arkham-en/character/merchant-gerald-stewart` | совпадает с 2023; совпадает с 2023 |
| 455. «F&M — поезда и другие игрушки» | 62 | `coc:location:arkham-451-fm-trains-toys`; `arkham-en/character/merchant-dean-martelle`; `arkham-en/character/merchant-clell-flint` | псевдоним; псевдоним; совпадает с 2023 |
| 456. Меблированные комнаты «Челси» | 62 | `coc:location:arkham-452-chelsea-house-apartments` | псевдоним, пометка в quality.notes |
| 457. Универмаг Глисона | 62 | `coc:location:arkham-427-gleasons-department-store` | совпадает с 2023 |
| 458. «Сирс и Робак», магазин-каталог | 62 | `coc:location:arkham-434-sears-roebuck`; `arkham-en/character/merchant-henrietta-harrison` | псевдоним, пометка в quality.notes; совпадает с 2023 |
| Ривертаун (вступление) | 63 | `coc:location:arkham-rivertown` — совпадает с книгой 2023 | — |
| 501. Берег реки | 63–64 | `coc:location:arkham-502-the-shore` (псевдоним и источник Hort уже есть); Грег Чудище — `arkham-en/character/rivertown-greg-the-monster` (источник Hort уже есть) | — |
| 501. Берег реки | 63–64 | `arkham-en/character/rivertown-greg-the-monster` | пометка в quality.notes |
| 502. Универсальный магазин | 64 | `coc:location:arkham-504-arkham-general-store` — совпадает с книгой 2023 (указ 1866 года, Элиот Олни) | — |
| 503. Восточная церковь | 64 | `coc:location:arkham-505-east-church` | пометка в quality.notes |
| 504. Благотворительный приют Элинор Пибоди | 64 | `coc:location:arkham-506-eleanor-peabody-charity-home` — совпадает (расхождение адреса уже в пометке) | — |
| 505. «Лодка и наживка» Арли | 64–65 | `coc:location:arkham-501-arleys-boat-and-bait` — совпадает с книгой 2023 | — |
| 506. Грегор Вейлдер, стеклодув | 65 | `coc:location:arkham-509-gregor-weilder-glassblower`, `rivertown-gregor-weilder` — совпадает | — |
| 507. «Аркхэмская печатня» | 65 | `coc:location:arkham-508-arkham-printing` — совпадает | — |
| 508. Восточная средняя школа | 65 | `coc:location:arkham-510-arkham-east-public-high-school` | пометка в quality.notes |
| 509. «Луч надежды» | 65 | `coc:location:arkham-512-beacon-of-hope-settlement-house` — совпадает | — |
| 510. Гюнтер Шмидт, стекольщик | 65 | `arkham-en/character/rivertown-gunther-schmidt` | абзац «По путеводителю Hort» |
| 511. Кузница | 65 | `coc:location:arkham-515-blacksmith`, `rivertown-jacob-asker` — совпадает | — |
| 512. Хайрем, старьёвщик | 66 | `coc:location:arkham-516-junkyard`, `rivertown-hiram-the-junkman` — совпадает | — |
| 513. Кирпичный завод Данхэма | 66 | `arkham-en/organization/rivertown-finns`; `arkham-en/character/rivertown-typical-finn-boy` | абзац «По путеводителю Hort»; пометка в quality.notes |
| Кампус Мискатоникского Университета (вступление) | 67 | `coc:location:arkham-campus` — совпадает с книгой 2023 (Хилл-стрит с тремя колодцами) | — |
| 601. Дом ветеранов долины Мискатоник | 67–68 | `coc:location:arkham-601-miskatonic-valley-veterans-home` | псевдоним |
| 602. Юго-западная трансформаторная подстанция | 68 | `coc:location:arkham-602-southwest-transformer-station` | совпадает с 2023 |
| 603. Аркхэмская государственная средняя школа | 68 | `coc:location:arkham-603-arkham-public-high-school`; `arkham-en/character/campus-anita-pierce` | совпадает с 2023; совпадает с 2023 |
| 604. Морг Уайтчепел | 68 | `coc:location:arkham-608-whitechapel-mortuary` | псевдоним |
| 605. Мискатоникская атлетическая ассоциация | 68 | `coc:location:arkham-605-miskatonic-athletic-association` | пометка в quality.notes |
| 606. Натаниэль Уингейт Пизли | 68 | `coc:location:arkham-607-peaslee-residence` | совпадает с 2023 |
| 607. Корпус им.Джонатана Эдвардса | 68 | `coc:location:arkham-609-jonathan-edwards-hall` | псевдоним, пометка в quality.notes |
| 608. Спортзал Экстона | 69 | `coc:location:arkham-611-axton-field-house`; `arkham-en/character/campus-donald-kanum`; `arkham-en/character/campus-roger-parkinson`; `arkham-en/character/campus-henry-cartwright`; `arkham-en/character/campus-robert-bradbury`; `arkham-en/character/campus-adam-hopkins`; `arkham-en/character/campus-douglas-arthur` | псевдоним, пометка в quality.notes; совпадает с 2023; псевдоним; совпадает с 2023; совпадает с 2023; совпадает с 2023; совпадает с 2023 |
| 609. Медицинский факультет | 69–70 | `coc:location:arkham-624-college-of-medicine`; `arkham-en/character/campus-chester-armwright` | псевдоним; пометка в quality.notes |
| 610. Прачечная и котельная | 70 | `coc:location:arkham-625-university-laundry-and-steam-plant` | псевдоним |
| 611. Учебная больница святой Марии | 70 | `coc:location:st-marys-hospital` | псевдоним |
| 612. Научный корпус | 70–73 | `coc:location:arkham-612-science-hall`; `arkham-en/character/campus-hiram-upham`; `arkham-en/character/campus-w-e-cameron`; `arkham-en/character/campus-donald-atwood`; `arkham-en/character/campus-percy-lake`; `arkham-en/character/campus-roberta-angley`; `arkham-en/character/campus-alex-warden`; `arkham-en/character/campus-wingate-peaslee`; `arkham-en/character/campus-lawrence-abbott`; `arkham-en/character/campus-dewart-ellery`; `arkham-en/character/campus-frank-pabodie`; `arkham-en/character/campus-hinkley-woodbridge`; `arkham-en/character/campus-hamlin-hayes`; `arkham-en/character/campus-william-dyer`; `arkham-en/character/campus-billings`; `arkham-en/character/campus-cecil-waldron`; `arkham-en/character/campus-archibald-greely`; `arkham-en/character/campus-harold-shear`; `arkham-en/character/campus-conrad-miller` | совпадает с 2023; совпадает с 2023; псевдоним; совпадает с 2023; псевдоним, абзац «По путеводителю Hort»; псевдоним, пометка в quality.notes; совпадает с 2023; абзац «По путеводителю Hort», пометка в quality.notes; псевдоним; совпадает с 2023; псевдоним, абзац «По путеводителю Hort»; псевдоним, абзац «По путеводителю Hort»; псевдоним, абзац «По путеводителю Hort»; совпадает с 2023; псевдоним, пометка в quality.notes; псевдоним, абзац «По путеводителю Hort», пометка в quality.notes; совпадает с 2023; совпадает с 2023; совпадает с 2023 |
| 613. Пристройка к Научному корпусу им.Чарльза Тайнера | 73–74 | `coc:location:arkham-613-charles-tyner-science-annex` | псевдоним, пометка в quality.notes |
| 614. Мемориальная колокольня Копли | 74 | `coc:location:arkham-615-copley-memorial-bell-tower` | совпадает с 2023 |
| 615. Корпус гуманитарных наук | 74–77 | `coc:location:arkham-614-robert-carter-memorial-hall`; `arkham-en/character/campus-peter-crownin`; `arkham-en/character/campus-allen-peabody`; `coc:character:warren-rice`; `arkham-en/character/campus-jabir-shariq`; `arkham-en/character/campus-paul-eastman`; `arkham-en/character/campus-stanley-whitman`; `arkham-en/character/campus-albert-wilmarth`; `arkham-en/character/campus-arthur-goddard`; `arkham-en/character/campus-daphne-rosen`; `arkham-en/character/campus-alice-turner`; `arkham-en/character/campus-george-kilbraith`; `arkham-en/character/campus-harvey-wilcox`; `arkham-en/character/campus-martin-fen`; `arkham-en/character/campus-ferdinand-ashley`; `arkham-en/character/campus-abram-bethnell`; `arkham-en/character/campus-tyler-freeborn`; `arkham-en/character/campus-francis-morgan`; `arkham-en/character/campus-anthony-westgate`; `arkham-en/character/campus-nathaniel-wingate-peaslee`; `arkham-en/character/campus-aaron-chase` | псевдоним, пометка в quality.notes; совпадает с 2023; совпадает с 2023; пометка в quality.notes; псевдоним, пометка в quality.notes; псевдоним, пометка в quality.notes; абзац «По путеводителю Hort»; псевдоним, пометка в quality.notes; совпадает с 2023; пометка в quality.notes; псевдоним; псевдоним; абзац «По путеводителю Hort»; совпадает с 2023; совпадает с 2023; совпадает с 2023; совпадает с 2023; пометка в quality.notes; совпадает с 2023; пометка в quality.notes; совпадает с 2023 |
| 616. Памятник декану Хэлси | 77 | `coc:location:arkham-616-statue-lawn` | псевдоним |
| 617. Локсли-холл | 77 | `coc:location:arkham-618-george-locksley-hall` | совпадает с 2023 |
| 618. Западное общежитие | 77 | `coc:location:arkham-617-west-dormitory` | совпадает с 2023 |
| 619. Восточное общежитие | 77 | `coc:location:arkham-620-east-dormitory` | пометка в quality.notes |
| 620. Общежитие Дороти Апмэн | 78 | `coc:location:arkham-619-dorothy-upman-hall` | псевдоним |
| 621. Общежитие для бакалавров и выпускников | 78 | `coc:location:arkham-621-derby-hall` | псевдоним |
| 622. Резиденция президента Университета | 78 | `coc:location:arkham-622-presidents-house` | псевдоним, пометка в quality.notes |
| 623. Университетская библиотека | 78–80 | `coc:location:orne-library`; `coc:character:henry-armitage`; `arkham-en/character/campus-wilfred-llanfer` | псевдоним, абзац «По путеводителю Hort»; пометка в quality.notes; совпадает с 2023 |
| 624. Университетский музей | 80 | `coc:location:arkham-627-university-exhibit-museum` | пометка в quality.notes |
| 625. Административный корпус Хойта | 80–81 | `coc:location:arkham-629-hoyt-administration-building`; `arkham-en/character/campus-harvey-wainscott`; `arkham-en/character/campus-david-edmund`; `arkham-en/character/campus-ruth-ellen-whitby`; `arkham-en/character/campus-howard-prescott`; `arkham-en/organization/campus-miskatonic-crier`; `arkham-en/character/campus-seymour-addleson` | абзац «По путеводителю Hort»; пометка в quality.notes; пометка в quality.notes; совпадает с 2023; абзац «По путеводителю Hort»; псевдоним; псевдоним |
| 626. Отель «Мискатоник» | 81 | `coc:location:arkham-634-hotel-miskatonic` | совпадает с 2023 |
| 627. Аркхэмское общество защиты животных | 81–82 | `coc:location:arkham-635-spca`; `arkham-en/character/campus-wilma-peabody` | псевдоним, абзац «По путеводителю Hort»; псевдоним |
| 628. Гостиница для женщин Харриэт Ботсфорд | 82 | `coc:location:arkham-637-harriet-botsford-hotel-for-women`; `arkham-en/character/campus-abigail-flint` | псевдоним; совпадает с 2023 |
| Френч-Хилл (вступление) | 83 | `coc:location:arkham-french-hill` — абзац Hort уже есть (часть frenchhill) | — |
| 701–723 | 83–89 | все места и люди сопоставлены частью frenchhill (`checks/20261114-arkham/frenchhill.md`): 701→701, 702→702, 703→703-A, 704→703-B, 705→704, 706→708, 707→709, 708→710, 709→720, 710→722, 711→723, 712→705, 713→706, 714→707, 715→711, 716→713, 717→712, 718→714, 719→715, 720→717, 721→724, 722→725, 723→727; псевдонимы, источники и абзацы Hort уже в записях | — |
| Гипноз (опциональный навык) | 87–88 | `coc:skill:hypnosis` | абзац «По путеводителю Hort» |
| 716. Пансионат Смита | 87 | `arkham-en/character/frenchhill-elisha-couzon` | пометка в quality.notes |
| Аптаун (вступление) | 90–91 | `coc:location:arkham-uptown` — совпадает с книгой 2023 | — |
| 801. Пансион Франклинов | 91 | `coc:location:arkham-801-franklin-place`; `arkham-en/character/uptown-gisele-helcimer` | пометка в quality.notes; абзац «По путеводителю Hort», пометка в quality.notes |
| 802. Средняя школа Дэниэла Шея | 91 | `coc:location:arkham-802-daniel-shay-public-school` — совпадает | — |
| 803. Дэниэл Аптон, архитектор-консультант | 92 | `arkham-en/character/uptown-daniel-upton` | абзац «По путеводителю Hort», пометка в quality.notes |
| 804. Дом престарелых Уайтчепел | 92 | `coc:location:arkham-811-whitechapel-nursing-home` — совпадает | — |
| 805. Доктор Хортон Уилсон | 92 | `coc:location:arkham-812-horton-wilson-home`, `uptown-horton-wilson` — совпадает | — |
| 806. Первая пресвитерианская церковь | 92 | `coc:location:arkham-817-first-presbyterian-church`, `uptown-eben-sutton` — совпадает | — |
| 807. Доктор Мортон Хартвелл | 92 | `arkham-en/character/uptown-morton-hartwell` | пометка в quality.notes |
| 808. Доктор и миссис Генри Армитедж | 92 | `coc:location:arkham-807-armitage-home` — совпадает (расхождение адреса уже в пометке) | — |
| 809. Стюарт Портман | 92–93 | `coc:location:arkham-805-stewart-portman-home`; `arkham-en/character/uptown-stewart-portman`; `arkham-en/tome/uptown-zekerboni` | совпадает с 2023; абзац «По путеводителю Hort»; пометка в quality.notes |
| 810. Тимблтон-Армс | 93 | `coc:location:arkham-808-timbleton-arms` | пометка в quality.notes |
| 811. Салон красоты «Мэй лэдис» | 93 | `coc:location:arkham-809-may-ladies-beauty-salon` — совпадает | — |
| 812. Мискатоник-клуб | 93 | `arkham-en/organization/uptown-miskatonic-club` | пометка в quality.notes |
| 813. «Дочери американской революции» | 93 | `coc:location:arkham-813-first-ladies-of-arkham` | псевдоним |
| 814. «Комнаты Кларк» | 94 | `coc:location:arkham-815-clarks-residential-accommodations` | пометка в quality.notes |
| 815. Альбер Н.Уилмарт | 94 | `coc:location:arkham-816-wilmarth-home` — совпадает | — |
| 816. Гарольд Шир | 94 | `coc:location:arkham-819-shear-home`; `arkham-en/character/uptown-jonathan-shear` | совпадает с 2023; пометка в quality.notes |
| 817. Аркхэмская конгрегационная церковь | 94 | `coc:location:arkham-821-arkham-reserved-congregational-church` | пометка в quality.notes |
| Нижний Саутсайд (вступление) | 95 | `coc:location:arkham-lower-southside` | пометка в quality.notes |
| 901. Аркхэмское историческое общество | 95–96 | `coc:location:arkham-901-historical-society`; `arkham-en/character/southside-diane-lapham-peabody` | абзац «По путеводителю Hort»; пометка в quality.notes |
| 902. Институт Ларкина | 96 | `coc:location:arkham-902-gordon-psychiatric-home`; `arkham-en/character/southside-phillip-gordon`; `arkham-guide-hort-ru/character/nathaniel-corey` | псевдоним, абзац «По путеводителю Hort»; пометка в quality.notes; **новая запись** |
| 903. Салон мисс Эндрю | 96 | `coc:location:arkham-903-miss-andrews-social-parlor`; `arkham-en/character/southside-nelly-andrews` | совпадает с 2023; совпадает с 2023 |
| 904. Общество Ока Амары | 96–97 | `arkham-en/organization/southside-eye-of-amara`; `arkham-en/character/southside-jason-gaspard` | пометка в quality.notes; пометка в quality.notes |
| 905. Ветеринар | 97 | `arkham-en/character/southside-william-pinter` | пометка в quality.notes |
| 906. Церковь св.Станислава | 97–98 | `coc:location:arkham-904-st-stanislaus-church`; `arkham-en/character/southside-kazimierz-iwanicki` | совпадает с 2023; пометка в quality.notes |
| 907. Пансионат Шиманской | 98 | `arkham-en/character/southside-magdalena-szymanski`; `arkham-en/character/southside-stanley-malkowski` | абзац «По путеводителю Hort»; пометка в quality.notes |
| 908. Таран-холл | 98 | `coc:location:arkham-907-taran-hall` | совпадает с 2023 |
| 909. Церковь Святого Сердца | 98 | `coc:location:arkham-908-our-lady-of-the-sacred-heart`; `arkham-en/character/southside-anthony-morency` | пометка в quality.notes; совпадает с 2023 |
| 910. Похоронное бюро Элеазара | 98 | `coc:location:arkham-909-eleazars-funeral-home`; `arkham-en/character/southside-jaspar-eleazar` | совпадает с 2023; совпадает с 2023 |
| 911. Меблированные комнаты Симпсона | 98–99 | `coc:location:arkham-911-simpson-apartments`; `arkham-en/character/southside-madame-dulagi` | пометка в quality.notes; пометка в quality.notes |
| 912. «Ресторан Антона» | 99 | `coc:location:arkham-913-antons-restaurant` | совпадает с 2023 |
| 913. «Клуб» | 99–100 | `coc:location:arkham-912-italian-club`; `arkham-en/character/southside-joe-potrello`; `arkham-en/character/southside-virgilio-scavo`; `arkham-en/character/southside-lou-benito` | совпадает с 2023; пометка в quality.notes; совпадает с 2023; совпадает с 2023 |
| 914. Многоквартирный дом | 100 | `coc:location:arkham-914-tenement`; `arkham-en/character/southside-mona-reed`; `arkham-en/character/southside-hagan-wilson` | пометка в quality.notes; псевдоним; пометка в quality.notes |
| 915. Средняя школа Хэлси | 100 | `coc:location:arkham-918-halsey-public-school` | совпадает с 2023 |
| 916. Мужская парикмахерская Петруччи | 100 | `coc:location:arkham-919-petruccis-barbershop`; `arkham-en/character/southside-fabio-petrucci` | совпадает с 2023; пометка в quality.notes |
| 917. Кладбище Крайстчёрч | 101 | `coc:location:arkham-921-christchurch-cemetery` | абзац «По путеводителю Hort» |
| 1001. Биллингтонский лес | 102–103 | `coc:location:arkham-hort-billingtons-wood`; `arkham-guide-hort-ru/creature/lurker-at-the-threshold` | **новая запись**; **новая запись** |
| 1002. Змеиное логово | 103 | `coc:location:arkham-os116-snakes-den-cave` | совпадает с 2023 |
| 1003. Старый особняк Картеров | 103 | `coc:location:arkham-os115-old-carter-mansion` | пометка в quality.notes |
| 1004. Университетский стадион | 105 | `coc:location:arkham-os110-mu-athletic-field` | псевдоним |
| 1005. Городская свалка | 105 | `coc:location:arkham-os102-town-dump` | совпадает с 2023 |
| 1006. Ферма Чепменов | 105 | `coc:location:arkham-os103-chapman-farmhouse` | совпадает с 2023 |
| 1007. Мидоу-хилл | 105–107 | `coc:location:arkham-os105-meadow-hill`; `arkham-en/organization/overview-arkham-coven`; `arkham-en/character/overview-joe-ambrose`; `arkham-en/character/overview-harold-beemis`; `arkham-en/character/overview-robert-czyenck`; `arkham-en/character/overview-william-danvers-johnston`; `arkham-en/character/overview-abigail-larue`; `arkham-en/character/overview-edwin-white-perkins-iii`; `arkham-en/character/overview-marla-slocum`; `arkham-en/character/overview-ellen-whipple-smith`; `arkham-en/character/overview-daniel-swain`; `arkham-en/character/overview-jennifer-tilstrom`; `arkham-en/character/overview-sheila-torsten`; `arkham-en/character/overview-james-allen-white`; `arkham-en/character/frenchhill-keziah-mason` | псевдоним; псевдоним, пометка в quality.notes; псевдоним; абзац «По путеводителю Hort»; абзац «По путеводителю Hort»; псевдоним, абзац «По путеводителю Hort»; пометка в quality.notes; пометка в quality.notes; псевдоним; псевдоним, пометка в quality.notes; псевдоним; псевдоним, абзац «По путеводителю Hort», пометка в quality.notes; совпадает с 2023; псевдоним; псевдоним |
| 1008. Кларкс-Корнерс | 107 | `coc:location:arkham-os113-clarks-corners` | абзац «По путеводителю Hort» |
| 1009. Коттедж Гуди Фаулер | 107 | `coc:location:arkham-os117-goody-fowler-cottage`; `arkham-en/tome/outskirts-goody-fowlers-grimoire` | совпадает с 2023; пометка в quality.notes |
| 1010. Проклятая Пустошь | 107–108 | `coc:location:arkham-os112-blasted-heath`; `arkham-en/creature/outskirts-other-colour-out-of-space` | псевдоним; пометка в quality.notes |
| 1011. Эмми Пирс | 109 | `arkham-en/character/outskirts-ammi-pierce`; `coc:location:arkham-os111-ammi-pierce-farm` | пометка в quality.notes; совпадает с 2023 |
| 1012. Крауниншилд-мэнор | 109–110 | `coc:location:arkham-os114-crowninshield-manor`; `arkham-en/character/uptown-edward-pickman-derby`; `arkham-en/character/outskirts-asenath-waite`; `arkham-en/character/outskirts-eunice-babson`; `arkham-en/character/outskirts-moses-sargent`; `arkham-en/character/outskirts-abigail-sargent` | псевдоним, абзац «По путеводителю Hort»; пометка в quality.notes; псевдоним, пометка в quality.notes; совпадает с 2023; совпадает с 2023; совпадает с 2023 |
| 1013. Аэродром | 110–111 | `coc:location:arkham-os118-arkham-airfield`; `arkham-en/character/outskirts-florence-harrington`; `arkham-en/character/outskirts-bessie-heingrapper` | псевдоним, пометка в quality.notes; абзац «По путеводителю Hort», пометка в quality.notes; пометка в quality.notes |
| 1014. Кингспортский мыс | 111 | `coc:location:arkham-hort-kingsport-head` | **новая запись** |
| 1015. Придорожная закусочная Феннера | 111 | `coc:location:arkham-os108-fenners-roadhouse`; `arkham-en/character/outskirts-reginald-fenner` | пометка в quality.notes; пометка в quality.notes |

Места 701–723 (Френч-Хилл) и псевдонимы мест 501–513 и 801–817 уже взяты частями frenchhill и rivertown-uptown; здесь к ним
добавлены только факты, которых не было (абзацы и пометки), и источник Hort там, где его не было.

## Персонажи Hort, которых книга 2023 заменила своими

Hort и книга 2023 часто дают на одном и том же месте разных людей. Отдельных записей им не заведено: по Р-234 основа — книга
2023, поэтому сведения Hort — абзацем «По путеводителю Hort» или пометкой (со статблоком) у персонажа 2023 на той же роли:
Дэн (бармен, 104) → Майки Кэтпол; Герхардт Уинч (медиум, 111) → Минни Коулман; Джордж Лиллибридж (115) → Джин Лиллибридж;
профессор Муамар Шалад (106, 615) → Джабир Шарик; Эрни Траут (135) → Эрни Касадо; Рэй Стаки (232) → Кэлвин Стаки; Харви
Баллард (229) → Грейнджер Баллард; Майер Голдитц (412, 814) → Уолтер Клейн; Бен Андерсон (417) → Джейн Андерсон; Альфред
Мюррей (418) → место 417; Мальвина Джейвил (434) → место 432-A; Элдон Дженкин (508) → пометка у Джоэла Мэнтона и места 510;
Дэвид Розен (615) → Дафна Розен; Суонсон Эймс (615) → Стэнли Уитмен; Говард Пенобскотт (625) → Говард Прескотт; Данте
Хельцимер (801) → Жизель Хельцимер; Паркер Ларкин (902) → Филлип Гордон и место 902; Альдо Петруччи (916) → Фабио Петруччи;
Стэнли Харрингтон и Баки Хайнграппер (1013) → Флоренс Харрингтон и Бесси Хейнгрэппер; Мэл Феннер (1015) → Реджинальд Феннер;
Э. Лапхэм Пибоди (901) → Дайан Лапхэм-Пибоди (псевдоним уже был). Исключения — Лабан Шрюсбери (на его месте в 2023 Джудит
Ренфорт, но он известный персонаж Мифов и уже есть в Pulp Cthulhu) и Натаниэль Кори (у 2023 места нет) — отдельные записи.

## Главные расхождения Hort и книги 2023

- Время действия: у Hort — октябрь 1928 года (Уилмарт после Вермонта, Армитедж после Данвича, Гилмен в Ведьмином доме, Дерби
  уже женат на Асенат); у книги 2023 — 1922 год с «Взглядами в будущее».
- Президент университета у Hort — Харви Уэйнскотт (баллотируется в мэры), у 2023 — Сеймур Эдлсон; Армитеджу у Hort 73 года
  (у 2023 — 59).
- Эпидемия 1905 года: у Hort — холера, у 2023 — брюшной тиф; у Hort в те же дни — маньяк, похожий на покойного доктора Хэлси.
- Скрытое ношение оружия: у Hort в Аркхэме не запрещено, у 2023 нужно разрешение — взято по 2023, расхождение в пометке
  `coc:rule:arkham-law-and-order`.
- Механики выгод (Масонская ложа, Торговая палата, Ротари-клуб, Мискатоник-клуб, Атлетическая ассоциация, курсы мисс Кристиан,
  стрелковый клуб, Манелли, Маркхэм, Око Амары, гримуар Гуди Фаулер, призрак Гуди Фаулер, второй цвет) — у Hort другие числа;
  везде пометкой.
- Статблоки Hort (адаптация 6e→7e) почти у всех персонажей другие — в пометках у записей 2023, характеристики не менялись.
- Адреса, цены и часы работы у ряда мест иные (101, 105, 107, 110, 117, 129, 203, 218, 234, 801, 814 и др.) — в пометках.
- Хозяин «Тимблтон-Армс» у Hort — сам О’Бэннион; Портман у Hort — насильник, а не убийца (абзац); у Кеции Мейсон в Hort
  по ошибке перепечатаны навыки Шалада, у Гилмена — атака «укус» Бурого Дженкина (опечатки Hort, не переносились).

## Не взято

- Лавкрафтовские фамилии (с. 14): тот же список, что `coc:table:arkham-names-1/-2`, в иной транслитерации; без пары в таблицах 2023
  только «Саллон» (вероятно, опечатка Hort).
- Нумерация домов (с. 15) — повтор «Улиц и переулков» из `coc:rule:arkham-neighborhoods`; ссылки на скачивание карт и
  рекомендации рассказов Лавкрафта в предисловии (с. 8).
- Вступления районов (Нортсайд, Ист-Таун, Ривертаун, Кампус, Аптаун) — совпадают с записями районов 2023.
- Абзацы Hort, которые при сверке оказались уже в записях 2023 (Ротари-клуб, ломбард «Даймонд», «Теленьюс», «Кроуфорд»,
  телефонная станция, полиция, почта, пожарная часть, переплётная, дом Пикеринга, дом Кроуфорд, Старое кладбище, Висельный
  холм, молочная, Западная церковь, Непосещаемый остров, «Челси», лавка Хардена, табачная, газетный киоск, Крайстчерч
  Епископальная, школа 603, спортзал Акстона, больница св. Марии, Научный корпус, музей, салон мисс Эндрюс, церкви 904 и 908,
  Таран-холл, похоронное бюро Элеазара, ресторан Антона, Змеиное логово, свалка, Луговой холм, члены ковена Эмброуз, Суэйн,
  Слокам, Торстен, Аллен-Уайт, «Зекербони») — не дублировались; где числа расходятся — пометкой.
- Список фильмов 1928–1929 годов у театра «Амхерст» (с. 37) — у книги 2023 есть таблица «Фильмы двадцатых» у места 213.
- Список новинок книжного магазина Джейвил (с. 58) — у книги 2023 есть своя таблица у места 432-A.
- Расписания автобусов (с. 24, 31), цены автомобилей (с. 38), опись арсенала (с. 43), прокат самолётов (с. 110–111) — только
  пометками: числа Hort расходятся с 2023 (Р-234).
- Отдельные записи для людей, названных у Hort только по имени (Аарон Крейн, Ричард Гедни, Орретт Николс, Тришем Годдард,
  Амос Пайпер, Элайджа Биллингтон, Пьетро Мора) — упомянуты текстом.

## Кандидаты на слияние (Р-154)

| Запись | Другая запись | Уверенность | Связь |
|---|---|---|---|
| `arkham-guide-hort-ru/character/laban-shrewsbury` | `pulp-cthulhu-en/character/laban-shrewsbury` | высокая | `same_as` |
| Суонсон Эймс (абзац у `arkham-en/character/campus-stanley-whitman`) | `sny-o-yaponii-ru/character/swenson-ames` | средняя | нет — та же фигура кафедры английского МУ |

## Вопросы владельцу

1. Заводить ли отдельные записи для персонажей Hort, которых книга 2023 заменила своими (список выше)? Сейчас — абзац или
   пометка у персонажа 2023.
2. Кингспортский мыс: `part_of` — окрестности Аркхэма (как у Hort) или Кингспорт?
3. Названия на английском у новых записей Hort не заполнены: в источнике их нет (Arkham Unveiled под рукой нет).

## Проверка

- `python -B tools/check.py` по шести новым файлам — 0 ошибок, 0 предупреждений.
- `python -B pipeline/integrate/apply.py checks/20261114-arkham/proposals-hort.json --dry-run` — все правки ложатся.
- Применение на копии базы (`.cache/hort/sim`) с `tools/check.py` по изменённым записям — 0 ошибок, 0 предупреждений.
