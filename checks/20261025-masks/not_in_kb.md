# Masks of Nyarlathotep 7e (EN): что ещё не перенесено в kb

Аудит от 2026-10-25, только чтение. Источник — текстовый слой книги `masks7.txt`.
Страницы даны как **физ./печ.**: физическая страница PDF и печатный номер (печ. = физ. − 3).
Если номер взят из оглавления или указателя книги, физическая страница посчитана как печатная + 3.

## Что уже есть в kb из этой книги

| Вид | Записей | Где лежат |
|---|---|---|
| персонажи | 168 | `kb/books/masks-of-nyarlathotep-en/characters` |
| существа | 49 | `kb/books/masks-of-nyarlathotep-en/creatures`, плюс источник Masks в `kb/creatures/lion-big-cat.json`, `shoggoth-twsha.json`, `father-of-maggots.json` |
| тома | 23 (все 23 тома Приложения C) | `kb/tomes` |
| заклинания | 39 (всё Приложение B) | `kb/spells` |
| оружие | 12 | `kb/weapons` |
| навыки | 34 | `kb/skills` |
| локации | **0** | — |

Все 227 строк инвентаря `masks_inventory.jsonl` перенесены. Альтернативные профили (Larkin, одержимый Ньярлатхотепом; Ssathasaa в облике Bertha Shipley; Eloise в облике упыря; Neris в облике пантеры; синий огненный вампир; пульп-стая упырей) вошли в существующие записи.
Ниже перечислено то, что в kb пока не попало.

Как предлагается хранить: **существующие виды** — character, creature, tome, spell, weapon, location (схема Р-78 с `residents` и `tables`); **новые виды** — «артефакт», «таблица», «раздаточный материал», «организация», «сюжет», «правило»; карты и схемы улик — ссылкой из записи локации или главы.

---

## 1. Статблоки: не перенесены или перенесены не полностью (10)

| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Chase Sequence Quick Reference: Iregi Kipkemboi, Colm Doyle, Jimmy Jepleting | 122/119 | Для погони: ВЫН, ЛВК, СИЛ, ТЕЛ, ДВИ и навыки (Лазание, Прыжки, Слух, Скрытность, Выслеживание и др.) трёх убийц Элайеса; рядом препятствия погони (пожарная лестница, переулок, тротуар, дорога) | существующие персонажи: блок `chase`; препятствия — «таблица» или раздел главы |
| Chase QR: Ibi Moussa and his Accomplices | 314/311 | ВЫН 50, ЛВК 50, СИЛ 45, базовое ДВИ 7, навыки для погони | `ibi-moussa` (блок `chase`) |
| Chase QR: Warren Besart | 322/319 | ВЫН 40, ЛВК 35, СИЛ 20, ДВИ 7, навыки для погони | `warren-besart` (блок `chase`) |
| Chase QR: Neris (облик человека и облик пантеры) | 333/330 | Две колонки параметров (ДВИ 9 и 12) и навыки; рядом пульп-врезка о погоне по крышам | `neris` (блок `chase`) |
| Chase QR: Avtar Singh | 399/396 | ВЫН 70, ЛВК 85, СИЛ 60, ДВИ 9, навыки для погони | `avtar-singh` (блок `chase`) |
| Chase QR: Cultists (люди Хо Фана) и Lin Yenyu’s Hirelings | 559/556 | Два набора параметров для погони; врезка «Chasing the Watchers» | `average-cultist-of-the-bloated-woman-china`, `nefarious-hirelings-of-lin-yenyu` (блок `chase`) |
| Chase QR: Chu Min и Average Firm Action Members | 580/577 | Параметры для погони (ДВИ 9 и 8) и навыки | `chu-min`, `fighters-for-the-new-china-to-come` (блок `chase`) |
| Hunting Horror — профиль вида в книге | 295/292 | Полный профиль (СИЛ 145, ТЕЛ 205…) в разделе «Монстры: Англия» | `kb/creatures/hunting-horror.json`: добавить источник Masks и сверить отличия; при расхождении — вариант в `books/.../creatures` |
| Sand-dwellers, Stalkers of the Wastes | 385/382 | Профиль песчаных жителей (СИЛ 50, ТЕЛ 80…) в разделе «Монстры: Египет» | `kb/creatures/sand-dweller.json`: источник Masks плюс сверка |
| Titan Horror (Buddai?) | 501/498 | Гигантское неподвижное существо под Городом Великой Расы; профиля нет, только потеря Рассудка 1/1d10 | существо без профиля или заметка в локации «Город Великой Расы» |

## 2. Таблицы и справочные списки (31)

| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Timeline of Key Events, 1916–1926 | 21–22/18–19 | Хронология кампании по датам | «сюжет» (хронология) или «таблица» |
| Location of Carlyle Expedition Principals, January 1925 | 16/13 | Где на январь 1925 г. находятся Carlyle, Brady, Penhew, Huston, Masters | «сюжет»; ссылки на персонажей |
| Peruvian Vampire Names | 51/48 | Местные названия харисири (pishtaco, ñakaq) | заметка в `kharisiri` (aliases) |
| Table: Plutonian Visions (1d6) | 223/220 | Видения от «плутонианского наркотика» и потеря Рассудка по каждому | «таблица» или `tables` в локации «дом Шипли» |
| Table: Events Beneath the Sphinx (1d10) | 355/352 | Случайные события в туннелях под Сфинксом | `tables` локации «Туннели под Гизой» |
| Table: Pits and Chasms (1d4) | 357/354 | Ширина провала, глубина ямы и урон от падения | `tables` той же локации |
| Table: Desert Encounters (1d6) с описаниями | 481–482/478–479 | Встречи в Большой Песчаной пустыне (змеи, старатель, аборигены, беглец, поломка, песчаная буря) | `tables` локации «Большая Песчаная пустыня» |
| Golden Mirror — список видений | 652/649 | Шесть видений-предзнаменований по главам кампании | в запись артефакта (п. 3) |
| Table: Mask of Hayama Visions (1d4) | 653/650 | Бог, явившийся в видении, и потеря Рассудка при успехе и провале | в запись артефакта (п. 3) |
| Table: Oceanic Travel Times in Days | 628/625 | Матрица дней пути между шестью портами | «таблица» (путешествия) |
| Стоимость поездок: море, воздух, поезд, дирижабль | 627–630/624–627 | Цена за день пути по классам, время в пути | «таблица» или «правило» (путешествия) |
| Learning a New Skill: списки по видам транспорта | 631/628 | Каким навыкам можно научиться на лайнере и на трамп-пароходе; пульп-вариант | «правило» (путешествия) |
| Travel Events | 632/629 | Шесть заготовок для дорожных эпизодов (преследование культистами, слежка, крушение, убийство на борту, проклятый груз…) | «таблица» |
| Handy Ship Names | 628/625 | Laurentides, Snohomish, Ineluctable, Amra, Chukawan, Ivory Wind | «таблица» или локации-корабли |
| Madam Lin’s Poisons | 608/605 | Яд крайта и сонное зелье Fragile Silver: сила яда и эффект | «правило» (яды) или заметка в `lin-yenyu` |
| The Events of January 14, 1926 by Chapter | 622–623/619–620 | Что происходит в каждой стране в день затмения | «сюжет» |
| The Ultimate Outcome: подсчёт очков и итоги | 623–625/620–622 | Очки по главам, модификаторы (хронометр, Око Света и Тьмы) и три исхода (Full Horror…) | «таблица» плюс «сюжет» |
| Rewards: награды по главам | 86/83, 165/162, 228/225, 249/246, 287/284, 336/333, 375/372, 422/419, 440/437, 478/475, 509/506, 555/552, 604/601, 625/622 | Награды Рассудком (и пульп-бонусы) за итоги главы и побочного сценария | «сюжет» (у главы) или «таблица» |
| What Mahoney Knows about Jackson Elias | 194/191 | Что знает редактор The Scoop | `tables` или `keeper_hint` локации «The Scoop» |
| Asking Around about Jackson Elias | 197/194 | Сведения о визите Элайеса в Лондон | «таблица» (слухи), Лондон |
| Research Locations (Лондон) | 198/195 | British Museum, London Library, Central News Agency, Press Association: часы работы и доступ | локации-здания в «Лондоне» |
| Слухи в Лессер-Эдейле (Laughing Horse Inn, сплетни) | 235–236/232–233 | Что рассказывают местные о нападениях | `tables` локации «Лессер-Эдейл» |
| Notable Locations in Mombasa | 399/396 | Fort Jesus, Treasury Square, рыбный рынок, доки, Castle Hotel, Manor Hotel | локации-места в «Момбасе» |
| Notable Nairobi Locations, Other Nairobi Contacts | 405–407/402–404 | Места и контакты Найроби | локации «Найроби» |
| Local Gossip: Ndovu | 430/427 | Слухи деревни Ндову о Горе Чёрного Ветра | `tables` локации «Ндову» |
| Слухи в баре Bertram’s (Дарвин) | 465/462 | Список слухов за выпивку или броски общения | `tables` локации «Дарвин» |
| Cuncudgerie Gossip, Other Gossip | 470–472/467–469 | Слухи (каждый стоит выпивки) о Бакли, Слэттери, Безумном Рыжем Малдуне | `tables` локации «Канкаджери» |
| Grogan’s Answers | 486/483 | Ответы Грогана на вопросы о Лагере смерти и городе | заметка в `jeremy-grogan` или `tables` |
| What the Scholar Says (Shanghai Museum) | 570/567 | Что сообщает каждый учёный о Семи загадочных книгах и Ордене | `tables` локации «Шанхайский музей» |
| Хронология Австралии (1920–1925) | 452/449 | Huston, MacWhirr, раскопки по годам | «сюжет» |
| What the Carlyle Expedition Did in Kenya | 389/386 | Хронология экспедиции в Кении и резня | «сюжет» |

## 3. Артефакты и особые предметы (31)

### Приложение D

| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| The Golden Mirror | 652/649 | Золотая маска-зеркало: видения при броске МОЩ, при экстремальном успехе действует как Contact Nyarlathotep | «артефакт»; связь с `luis-de-mendoza`, отель España |
| The Ward of the Pyramid (Golden Ward) | 652–653/649–650 | Золотая полоса вокруг пирамиды, действует как Знак Древних; вынесенный кусок наносит харисири урон 1d3 за раунд | «артефакт» |
| Mask of Hayama | 653/650 | Маска с четырьмя ликами: видение бога (таблица 1d4), +1d10 к Мифам Ктулху, бонусный куб к Contact/Call | «артефакт» |
| Mirror of Gal | 653–654/650–651 | Зеркало для ясновидения и атаки: стоимость в ПМ и Рассудке, встречная проверка МОЩ, урон за ПМ; пульп-вариант | «артефакт» |
| Sandstone Vials (obra’an, gabeshgal) | 653/650, 261/258 | Вещества, без которых Зеркало Гал не работает | «артефакт» или часть Зеркала Гал |
| Two Scepters | 654/651 | +2d10 ПМ раз в день, поглощают 1d10 магического урона | «артефакт»; `edward-gavigan`, `zahra-shafik` |
| Headdress of Eyes | 654–655/651–652 | Хранилище ПМ (20, по 5 за раз), проклятие голоса Чёрного фараона; пульп-вариант | «артефакт» |
| Crown of Nitocris | 655/652 | Корона из циркония и железа — один из трёх предметов силы Нитокрис | «артефакт» |
| Girdle of Nitocris | 655/652 | Золотой пояс со звёздчатым рубином (мечеть Ибн Тулуна) | «артефакт» |
| Necklace of Nitocris | 655/652 | Серебряная цепь с изумрудами (изображение Чёрного сфинкса) | «артефакт» |
| Amulet of the Night Beasts | 655/652 | Защищает владельца от охотничьих ужасов (встречная проверка МОЩ) | «артефакт»; `faraz-najjar` |
| Circlet of Nata Haje | 655/652 | Создаёт египетских кобр за ПМ (яд Mild или Strong) | «артефакт»; `sharifa-rawash` |
| Token of Bast’s Regard | 656/653 | Защита от котов-демонов; проклятие за вред кошке (2d6) | «артефакт» |
| Taan’s Ring | 656/653 | Хранит 30 ПМ, забирает ПМ умирающих, даёт иммунитет к огню | «артефакт»; `taan-kaur` |
| Bundari’s Fly Whisk | 656–657/653–654 | Бонусный куб против магии и при поиске скрытого зла | «артефакт»; `old-bundari` |
| The Device of Rods, Wheels, and Mirrors | 657/654 | Обмен разумом с йитом на 1d4 недели (Рассудок, +1d8+2 к Мифам Ктулху); пульп-вариант | «артефакт» |

### Вне Приложения D

| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| The Mind Controller | 503/500 | Шлем йитов для стирания памяти: проверка ИНТ, −1d6 Рассудка | «артефакт»; локация «Штаб Хьюстона» |
| Marine Chronometers (часы культов) | 276/273, 503/500, 598/595, 624/621 | Синхронизация Великого обряда; уничтожение даёт −1 очко в итоговом подсчёте | «артефакт» (один, со ссылками на места) |
| Sir Aubrey’s Rocket (плюс Guidance System, Warhead, пусковой механизм) | 591–595/588–592 | Ракета на острове Серого Дракона, детали, способы сорвать запуск | «артефакт» и «сюжет» |
| Детали ракеты на Henson Manufacturing | 268/265, 271/268 | Компоненты, их опознание и саботаж (с пульп-врезками Weird Science) | в запись ракеты |
| Gate Box (Carl Stanford) | 563/560, 613/610 | Парные врата для бегства Стэнфорда | «артефакт»; `carl-stanford` |
| Statue of the Bloated Woman | 565/562 | Резерв ПМ (до 40, +2 в день), Рассудок 0/1d2 | «артефакт»; святилище в особняке Хо Фана |
| The Crawling Ceiling | 565/562 | Узор-ловушка, затягивающий разум (Трудная проверка МОЩ) | «артефакт» или «правило» (ловушка) |
| Plutonian Drug | 223/220 | Зелёный наркотик Ssathasaa, вызывает видения | «артефакт» (вещество); навык Lore (Brew Plutonian Drug) |
| Hemispheric Map | 369–370/366–367 | Карта с точками Великого обряда | «артефакт» или раздаточный материал |
| M’Weru’s Pendant (кровь Ньярлатхотепа) | 396/393, 650/647 | Три капли крови бога — пульп-ингредиент для Brew Space Mead | «артефакт»; `mweru` |
| Статуи-хранилища и великая статуя Ньярлатхотепа (Храм Пурпурного купола) | 497/494, 624/621 | Используются в обряде (+2 очка, если целы) | «артефакт» или локация |
| Медная чаша «copper from above» | 503/500 | Помогает при заклинании Send Dream | заметка в `send-dream` или «артефакт» |
| Камень Нури (половина Ока Света и Тьмы) и обломок печати Красной пирамиды | 323/320 | Символ для ритуала Ока Света и Тьмы | «артефакт»; `eye-of-light-and-darkness` |
| Pulp: Weird Science Workshop — Tabula Rasa Device, Temporal Communicator | 505/502 | Отсылка к предметам Книги хранителя | ссылка на существующие записи КХ, если они будут |
| Pendant and Golden Cup (Перу) | 65/62 | Находки Ларкина, связанные с пирамидой | «артефакт» (мелкий) |

## 4. Раздаточные материалы: Carlyle Papers (69)

Номера — по указателю «Handouts» (с. 668/665). Сами раздаточные материалы в PDF — изображения, текстового слоя у них нет; описания восстановлены по ссылкам в тексте. Куда в kb: новый вид «раздаточный материал» (`chapter`, `number`, `found_at` → локация, `mentions` → персонажи и тома).

| Элемент | Стр. | Что содержит |
|---|---|---|
| Peru #1 | 53/50 | Статья в международной прессе о наборе в экспедицию Ларкина |
| Peru #2 | 54/51 | Письмо или телеграмма Ларкина: сбор в Лиме, Bar Cordano |
| Peru #3 | 74/71 | Выдержки из «Последней исповеди Гаспара Фигероа» (→ `final-confessions-of-gaspar-figueroa`) |
| The Expedition #1 | 95/92 | Радиограмма Элайеса с корабля, январь 1925 |
| The Expedition #2 | 96/93 | Что сыщики знают об Элайесе, если пролог сыгран |
| The Expedition #3 | 97/94 | То же, если пролог не сыгран |
| The Expedition #4–#11 (8 шт.) | 98–100/95–97 | Газетные статьи о создании, успехах и гибели экспедиции Карлайла |
| America #1 | 125/122 | Письмо Besart → Roger Carlyle (март 1919) о продаже артефактов; из номера Элайеса |
| America #2 | 125/122 | Визитка Эдварда Гэвигана (Фонд Пенхью) из номера Элайеса |
| America #3 | 125/122 | Пустой коробок спичек из бара Stumbling Tiger (Шанхай) |
| America #4 | 126/123 | Бумага из номера Элайеса — зацепка на Шанхай |
| America #5 | 126/123 | Визитка Emerson Imports |
| America #6 | 126/123 | Письмо Мириам Этрайт Элайесу о пропавшей книге |
| America #7 | 127/124 | Объявление о лекции проф. Коулза в Нью-Йоркском университете |
| America #8 | 127/124 | Символ, вырезанный на лбу Элайеса |
| America #9 | 128/125 | Статьи New York Times об убийстве Элайеса и деле Хилтона Адамса |
| America #10 | 132/129 | Записка Элайеса «прочесть в случае моей смерти» |
| America #11 | 133/130 | Письмо Элайеса Кенсингтону (часть участников экспедиции жива) |
| America #12 | 134/131 | Заметки Элайеса (Nelson, Kenyatta, Mariga, Starret) |
| America #13 | 133/130 | Последние заметки Элайеса (тетрадь на 40 листов) |
| America #14 | 138/135 | Цитата из Life as a God о тронном зале Чёрного фараона |
| America #15 | 140/137 | Слайды Коулза: монолиты в австралийской пустыне |
| America #16 | 144/141 | Выдержки из досье «Carlyle, Roger V.W.» (лечение у Хьюстона) |
| England #1 | 194/191 | Заметка в The Scoop о «Челсийском змее» (выставка Шипли) |
| England #2 | 197/194 | Заметка в The Scoop о Дербиширском чудовище |
| England #3 | 198/195 | Статья в The Scoop с упоминанием инспектора Баррингтона |
| England #4 | 201/198 | Статья в книге из Фонда Пенхью об экспедиции в Египте |
| England #5 | 203/200 | Телеграмма д-ра Клайва Гэвигану о раскопках в Гизе |
| England #6 | 205/202 | Квитанции: Henson Manufacturing, Ferris & Sons |
| England #7 | 206/203 | Визитная карточка под квитанциями (линия «Айвори Винд» — Шанхай) |
| England #8 | 210/207 | Старая заметка в The Scoop о встрече с туманным отродьем |
| England #9 | 238/235 | Документ из Лессер-Эдейла (линия викария Страттона) |
| England #10 | 269/266 | Старые транспортные этикетки на Henson Manufacturing |
| England #11 | 277/274 | Письмо Омара аль-Шакти Гэвигану (Misr House) |
| England #12 | 278/275 | Записи в гроссбухе Гэвигана: адресаты поставок |
| England #13 | 279/276 | Неоконченное письмо Гэвигана |
| Egypt #1 | 321/318 | Показания Уоррена Бесарта |
| Egypt #2 | 323/320 | Символ на камне Нури (Око Света и Тьмы) |
| Egypt #3 | 325/322 | Заметка Cairo Bulletin о пожаре в лавке на улице Шакалов |
| Egypt #4 | 346/343 | Документ к эпизоду «An Audacious Theft» (мечеть Ибн Тулуна) |
| Egypt #5 | 350/347 | Находки из сейфа аль-Шакти: визитка Гэвигана, расписка |
| Kenya #1 | 410/407 | Пульп-вариант: письмо Лин Йеню и карты Города Белой гориллы |
| Kenya #2 | 411/408 | Показания сержанта Бампшена о гибели экспедиции |
| Kenya #3 | 415/412 | Пометка в «Чёрной книге» (подвал Таан Каур) |
| Kenya #4 | 427/424 | Сводка сведений Старого Бундари |
| Australia #1 | 466/463 | Дневник Артура Макуирра (координаты города) |
| Australia #2 | 488/485 | Рассказ Джереми Грогана |
| Australia #3 | 496/493 | Машинописные приказы Хьюстона |
| Australia #4 | 504/501 | Письмо Гэвигана Хьюстону |
| Australia #5 | 506/503 | Запись из рукописи Хьюстона Gods of Reality (→ `gods-of-reality`) |
| China #1, #2 | 544/541 | Статьи Shanghai Courier о покушениях на Брэди |
| China #3 | 545/542 | Материал к гибели людей в доме цветочных девушек на Lantern Street |
| China #4 | 545/542 | Объявление астролога Лунга в Shanghai Courier |
| China #5 | 566/563 | Свитки Ордена из тикового шкафа (бедствия с 1556 г.) |
| China #6 | 574/571 | Свиток, который Мадам Лин читает вслух |
| China #7 | 580/577 | Записка на английском в штабе «Новой Китая» |
| China #8 | 584ff/581ff | Отчёт Джека Брэди (Каир, Дахшур, Красная пирамида) |
| China #9 | 587/584 | Обломок печати Красной пирамиды (символ) |
| China #10 | 596/593 | Письмо Гэвигана сэру Обри о Henson Manufacturing |
| China #11 | 597/594 | Телеграмма Хьюстона сэру Обри |
| China #12 | 598/595 | Выдержки из дневников сэра Обри (1921–1925) |

## 5. Карты и схемы улик (45)

Хранить как ссылку `map_page` в записи локации или главы; изображения в kb не переносятся.

| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| World Map | 195–196/192–193, 531–532/528–529 | Карта мира кампании | глава / сюжет |
| Peru, Route Map, The Ruins | 56/53, 76/73, 81/78 | Перу, маршрут, руины пирамиды | локации Перу |
| Greater New York, Harlem, The Ju Ju House | 104/101, 147/144, 160/157 | Нью-Йорк | локации Америки |
| London, Penhew Foundation, Limehouse, Shipley’s House, Lesser Edale, Plum Castle, Blue Pyramid Club, Empire Spices, Henson Manufacturing, Misr House | 192, 200, 211, 222, 234, 245, 255, 259, 266, 273 (физ.) | 10 планов Англии | локации Англии |
| Cairo, The Tunnels Below | 299/296, 353/350 | Каир, туннели под Гизой | локации Египта |
| Kenya, Route Map, Nairobi, Taan Kaur’s Shop, The Game Lodge, M’Weru’s Cavern, The Great Temple | 390, 402, 403, 413, 419, 432, 434 (физ.) | 7 карт Кении | локации Кении |
| Australia, Randolph Shipping Co., Canning Basin, Close Environs, Huston’s Main Entrance, Portions of the City, Huston’s HQ | 454, 468, 473, 482, 490, 493, 502 (физ.) | 7 карт Австралии | локации Австралии |
| Shanghai, Mr. Lung’s Apartment, Ho Fang’s Warehouse, Ho Fang’s Mansion, Mu Hsien’s House, Gray Dragon Island | 524, 551, 557, 562, 578, 588 (физ.) | 6 планов Китая | локации Китая |
| Clue Diagrams: America, England, Egypt, Kenya, Australia, China | 105/102, 181/178, 301/298, 392/389, 457/454, 525/522 | Схемы связей улик по главам | «сюжет» (у главы) |

Итого 45: 39 карт (вместе с картой мира) и 6 схем улик. Номера взяты из «Map Index», с. 667/664.

## 6. Локации: города, здания, корабли (79)

Схема `location` (Р-78) уже есть; записей из Masks нет. Ниже дерево «город → место»; тип указан по схеме.

### Перу
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Lima | 55–57/52–54, 64/61 | Справка о Перу и Лиме 1921 г. | location: город |
| Bar Cordano | 64/61 | Место сбора экспедиции | location: здание |
| Hotel España, Hotel Maury | 67/64, 57/54 | Гостиница Ларкина (Золотое зеркало), вторая гостиница | location: здание |
| Museo de Arqueología y Antropología, The Storeroom | 68/65 | Архив университета, кусок золотой печати, исповедь Фигероа | location: здание |
| Puno, Lake Titicaca | 73–79/70–76 | Город на высокогорье, встреча с Найрой, горная болезнь | location: город |
| The Ruins: пирамида, туннели, Chimneys, Charnel Pit, Pool of Filth | 80–85/77–82 | Руины с Отцом личинок | location: место (с подместами) |

### Америка
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| New York City (география, Манхэттен) | 103–108/100–105 | Справка о городе 1925 г. | location: город |
| Hotel Chelsea | 121/118 | Убийство Элайеса, сцена погони | location: здание |
| Prospero House | 131/128 | Издательство Кенсингтона, оглашение завещания | location: здание |
| Carlyle Estate, Carlyle Mansion Library | 135–137/132–134 | Поместье Эрики Карлайл, библиотека с томами | location: здание |
| Emerson Imports | 141/138 | Импортёр, связь с Ахджей Сингхом | location: здание |
| Harlem | 146–147/143–144 | Район 1920-х, оргпреступность | location: район |
| Ju-Ju House | 157–162/154–159 | Логово Кровавого Языка, комнаты, обряды | location: здание |
| Sing Sing («Old Sparky’s House») | 153/150 | Визит к Хилтону Адамсу | location: здание |
| Fat Maybelle’s, Cypress Hills Cemetery | 155/152, 123/120 | Клуб в Гарлеме; кладбище, похороны Элайеса | location: здание / место |
| NY Public Library, Widener Library, газетные архивы (morgues) | 108/105, 130/127 | Места для исследований | location: здание |

### Англия
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| London (Getting About, London Fog) | 182–185/179–182 | Справка о Лондоне, туман, транспорт | location: город |
| The Scoop | 193/190 | Редакция Махони | location: здание |
| Penhew Foundation (Key Rooms, Secret Room) | 199–210/196–207 | Фонд: комнаты, тайный подвал | location: здание (с комнатами) |
| Квартира Гэвигана в Мэйфэре | 207/204 | Адрес Гэвигана | location: здание |
| Limehouse Docks, склад Puneet Chaudhary | 211/208 | Доки, склад | location: район |
| Holbein Mews (Chelsea), дом Шипли | 220–226/217–223 | Дом художника, видения | location: здание |
| Lesser Edale (Laughing Horse Inn, Pitchlock General Store, дом викария) | 234–238/231–235 | Деревня в Дербишире | location: город (деревня) + здания |
| Mam Tor, Blue John Cavern | 241/238 | Местные достопримечательности | location: место |
| Plum Castle (Key Locations) | 242–247/239–244 | Замок Вейнов | location: здание |
| Soho / Blue Pyramid Club | 256/253 | Клуб Абдула Нависхи | location: здание |
| Empire Spices | 259/256 | Лавка Захры Шафик | location: здание |
| Henson Manufacturing (Derby) | 265–271/262–268 | Мастерская деталей ракеты | location: здание |
| Misr House, Naze Tower, Walton-on-the-Naze | 272–280/269–277 | Усадьба Гэвигана, тайная мастерская и темница | location: здание |
| British Museum, London Library, Central News Agency, Press Association | 198/195 | Места для исследований | location: здание |
| Scotland Yard / London Police | 253/250 | Расследование Баррингтона | location: здание |
| British Empire Exhibition | 264/261 | Выставка (пульп-сцена) | location: место |
| Govan District Asylum | 211/208 | Шотландский побочный сюжет (Alan McGann) | location: здание |

### Египет
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Port Said (прибытие), Cairo (Egypt in 1925) | 302–306/299–303 | Справка о стране и городе | location: город |
| Hotel du Sud | 314–315/311–312 | Мадам Патено и Иби Мусса | location: здание |
| Street of Potters (лавки Фараза Наджара), Street of Jackals | 316–319/313–316 | Лавки и пожар | location: место |
| The Red Alley (комната Бесарта, лавка Абу Удхре) | 320/317 | Логово Бесарта | location: место |
| Cairo Bulletin | 324/321 | Редакция, архив | location: здание |
| Egyptian Museum, The Vaults | 325–328/322–325 | Музей, хранилища | location: здание |
| The Black Cat (дом ван Хёвелена), Temple of Bast | 329–336/326–333 | Побочный сценарий | location: здание |
| Лагерь экспедиции Клайва | 339–342/336–339 | Раскопки в Гизе | location: место |
| Mosque of Ibn Tulun | 343/340 | Пояс Нитокрис, Нессим Эфти | location: здание |
| Плантация и дом Омара аль-Шакти | 347–348/344–345 | Логово главы Братства | location: здание |
| Giza: Sphinx, Mycerinus’ Pyramid, Beneath the Pyramids, Great Chamber of Nyarlathotep, The Enormous Hole | 351–361/348–358 | Подземный комплекс | location: место (с подместами) |
| Dahshur: Red, Collapsed, Bent Pyramid, Nyarlathotep’s Sanctum | 367–372/364–369 | Пирамиды и святилище | location: место |
| El Wasta, Meidum, Sakkara | 323/320 | Нури; упоминаемые места | location: место |

### Кения
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Mombasa | 399/396 | Порт, известные места | location: город |
| Uganda Railway | 400–402/397–399 | Поезд до Найроби, первое нападение | location: место |
| Nairobi (Swahili Town, Loyal Defender, Victoria Bar, Fort Smith) | 403–407/400–404 | Город, колониальная власть | location: город |
| Nairobi Star | 406/403 | Редакция, пожары | location: здание |
| Taan Kaur’s Shop | 413–415/410–412 | Чайная лавка и подвал | location: здание |
| The Game Lodge | 416–423/413–420 | Охотничий домик Эндикотта, платформа | location: здание |
| Old Bundari’s Hut | 424/421 | Хижина колдуна | location: здание |
| Ndovu Village, Aberdare Forest | 430/427, 429/426 | Деревня у горы, экология леса | location: город / область |
| Mountain of the Black Wind, Cavern of M’Weru, Great Temple | 431–439/428–436 | Гора, пещеры, храм обряда | location: место |

### Австралия
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Perth и Fremantle | 464/461 | Город, университет | location: город |
| Sydney (Australia Museum, National Art Gallery, University of Sydney, дом Коулзов) | 464–465/461–462 | Город и места для исследований | location: город |
| Darwin, Randolph Shipping Company | 465–468/462–465 | Порт, контора Тодди Рэндольфа | location: город + здание |
| Port Hedland | 469/466 | Порт в Пилбаре | location: город |
| Cuncudgerie | 470–473/467–470 | Шахтёрский городок | location: город |
| Dingo Falls, Slattery’s Hovel, The Caves | 476–478/473–475 | Места побочного сюжета «Призрак Бакли» | location: место / здание |
| Great Sandy Desert, Canning Stock Route | 480–488/477–485 | Пустыня, выживание | location: область |
| The Death Camp | 485/482 | Лагерь погибшей экспедиции | location: место |
| City of the Great Race: Huston’s Main Entrance, Second Entrance, Bunkhouse, Great Plazas, Purple Dome Temple, Nursery, Titan Horror, Huston’s HQ, Current Excavations, Kakakatak’s Chamber | 489–508/486–505 | Подземный город и его зоны | location: город (+ места) |

### Китай
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Hong Kong (лечебница Роджера Карлайла) | 527/524 | Город и лечебница | location: город |
| Shanghai (Lantern Street, Chin-Ling Road) | 524–533/521–530 | Справка о городе, Зелёная банда, компрадоры | location: город |
| Stumbling Tiger Bar, Flower Girl Houses | 540–542/537–539 | Бар Фергюса Чама, дома цветочных девушек | location: здание |
| Shanghai Courier | 543/540 | Редакция Чана | location: здание |
| Квартира Mr. Lung | 548–555/545–552 | Побочный сценарий «Демонический шкаф» | location: здание |
| Ho Fang Import/Export, склад | 556–559/553–556 | Контора и склад | location: здание |
| Особняк Хо Фана (Seven Gates to Heaven, Crawling Ceiling, святилище Раздутой женщины) | 561–567/558–564 | Особняк культа | location: здание |
| Shanghai Museum | 570/567 | Учёные-консультанты | location: здание |
| Дом Madam Lin Yenyu (Madam Swallow), коллекция | 571–575/568–572 | Дом и коллекция томов | location: здание |
| Дом Mu Hsien | 576–578/573–575 | Дом учёного | location: здание |
| Штаб New China / Firm Action, чайная Autumn Morning | 579–580/576–577 | Штаб Брэди, чайная | location: здание |
| Gray Dragon Island (Pale Viper’s Lair, тропа к вулкану, сердце вулкана) | 588–603/585–600 | Остров, ракетная шахта | location: место (остров) |

### Корабли
| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Ivory Wind | 213/210 | Торговое судно Лондон — Шанхай, экипаж-ласкары | location: здание (судно) |
| Dark Mistress | 568/565 | Судно-призрак, обезумевший экипаж | location: здание (судно) |
| Luxuriant Goddess | 541/538, 558/555 | Яхта Хо Фана | location: здание (судно) |

## 7. Организации и культы (28)

Куда в kb: новый вид «организация» (тип, глава, лидер → character, места → location, члены → characters).

| Элемент | Стр. | Что содержит |
|---|---|---|
| Brotherhood of the Black Pharaoh (UK) | 185/182 | Культ в Лондоне: структура, лидеры, места |
| Brotherhood of the Black Pharaoh (Egypt) | 307/304 | Культ в Каире |
| Cult of the Bloody Tongue (NYC) | 109/106 | Культ в Гарлеме |
| Cult of the Bloody Tongue (Kenya) | 393/390 | Культ на Горе Чёрного Ветра |
| Cult of the Sand Bat (+ Sign of the Sand Bat) | 459–460/456–457 | Культ в Австралии |
| Order of the Bloated Woman | 534/531 | Культ в Шанхае |
| Культ Отца личинок и харисири (Peru: Cult in Residence) | 58/55 | Культ в Перу |
| Carlyle Expedition | 142–145/139–142 | Участники, досье, судьба |
| Penhew Foundation | 199/196 | Фонд как организация |
| Clive Expedition | 310/307, 339/336 | Археологи в Гизе |
| Green Gang | 530/527 | Шанхайская банда |
| Firm Action / New China | 579/576, 610/607 | Отряд Брэди |
| Randolph Shipping Company | 465/462 | Судоходная контора-посредник |
| Emerson Imports | 141/138 | Импортная фирма |
| Ho Fang Import/Export | 556/553 | Фирма Хо Фана |
| Henson Manufacturing | 265/262 | Мастерская культа |
| Empire Spices | 259/256 | Лавка-прикрытие Шафик |
| Blue Pyramid Club | 256/253 | Клуб-прикрытие |
| Prospero House | 131/128 | Издательство Элайеса |
| Газеты: The Scoop, Cairo Bulletin, Nairobi Star, Shanghai Courier, New York Times | 193/190, 324/321, 406/403, 543/540, 148/145 | Редакции и их архивы как источники улик |
| Полиция: NYPD; London Police / Scotland Yard; египетская полиция; колониальная администрация Кении | 128/125, 253/250, 346/343, 404/401 | Как работают власти в каждой главе |
| Compradors | 533/530 | Посредники Шанхая |
| Dragomen | 318/315 | Проводники Каира |
| The Friends of Hilton Adams, Military Men | 116/113, 118/115 | Круг союзников в Гарлеме |
| Imperial Japanese Navy | 535/532 | Поддержка Исоге Таро |
| University of Sydney, Miskatonic University, Harvard (Widener Library) | 465/462, 34/31, 112/109 | Академические контакты |
| Bakewell Witches | 239/236, 244/241 | Исторический ковен рода Вейнов |
| Ferris & Sons | 205/202 | Перевозчик грузов культа |

## 8. Именные NPC без профиля, важные для сюжета (27)

Куда в kb: `character` с пустыми характеристиками (только описание, связи, `keeper_hint`) или жители (`residents`) локации.

| Элемент | Стр. | Что содержит |
|---|---|---|
| Roger Carlyle | 16/13, 33/30, 142/139 | Глава экспедиции, безумен, в лечебнице Гонконга; знает Великий план |
| Hypatia Masters (как человек) | 145/142 | Досье участницы; в kb есть только аспект Порождения |
| Reggie Baines | 33/30 | Хозяин лучшей гостиницы Найроби, Hampton House |
| Adrian Ferris | 34/31 | Секретарь Медицинского совета штата Нью-Йорк (досье Карлайла) |
| George Brunton | 120/117, 154/151 | Заместитель начальника тюрьмы Синг-Синг |
| Sgt. Leonard Bumption | 406/403, 411/408 | Свидетель с места резни (Kenya #2) |
| Captain Montgomery | 410–412/407–409 | Капитан полиции в Найроби, Форт-Смит |
| Roger Corydon | 410/407 | Заместитель колониального секретаря Кении |
| Lt. Mark Selkirk (погиб) | 388–390/385–387 | Командир отряда, «нашедшего» убийц экспедиции |
| Nuri of El Wasta и сын Ubaid | 313/310, 323/320 | Хранительница половины Ока Света и Тьмы («No profiles are provided») |
| Mme. Patenaude | 315/312 | Хозяйка Hotel du Sud |
| Abou Udhreh | 320/317 | Лавочник, приютивший Бесарта |
| Inspector Gregory Munden | 253/250, 280/277 | Пропавший полицейский; его удостоверение в Misr House |
| Badru | 190/187, 258/255 | Друг Ялеши Эссам |
| Neville Lloyd-Price | 272/269 | Прежний владелец Misr House |
| Alan McGann | 210–211/207–208 | Жертва в шотландском побочном сюжете |
| Жители Лессер-Эдейла: Bill Tatlock, Harold Short, Lydia и John Parkins, George и Edith Osgood, Sarah Bright, Jed Wainwright, Maddy Albright, Tom Corty | 232–238/229–235 | Трактирщик, выжившие, родственники жертв, прислуга, сплетница |
| Imelda Bosch (умерла) | 143/140 | Самоубийство; связь с Карлайлом |
| Arthur MacWhirr (умер) | 452/449, 465/462 | Открыл Город Великой Расы, автор дневника |
| Johnny Bigbush | 467/464 | Абориген из Дарвина, источник легенды |
| Derby Dave | 471/468, 481/478 | Валлиец-старатель в пустыне |
| Mad Ginger Muldoon | 471/468 | Источник историй о чудовищах |
| Auntie Gee | 535/532, 547/544 | Хозяйка дома цветочных девушек |
| Li Chou | 548/545 | Астролог-соперник, наславший кота-демона |
| Quivering Jade, Magenta Joy | 546–547/543–544 | Цветочные девушки, свидетельницы |
| Narcisa Quispe, Fortunato Cupitina | 80/77, 60/57 | Перу: женщина из Пуно; сын Петронилы |
| Mr. Schwentafsky, Mrs. Joyce Bullrush | 399/396, 269/266 | Хозяин Castle Hotel в Момбасе; домовладелица охраны Henson |

## 9. Заклинания и тома: несвязанные варианты и упоминания (11)

| Элемент | Стр. | Что содержит | Куда в kb |
|---|---|---|---|
| Speak to the Father of Maggots / Contact Father of Maggots | 642/639, 89/86 | Вариант Contact Nyarlathotep | alias в `contact-nyarlathotep`; связь с `father-of-maggots` |
| Contact Small Crawler | 445/442 | Вариант Contact Nyarlathotep (Кровавый Язык) | alias в `contact-nyarlathotep` |
| Contact Nyarlathotep (Sand Bat) | 514/511 | Вариант для культа Песчаной летучей мыши | alias в `contact-nyarlathotep` |
| Mistress of the Fan (Contact Nyarlathotep / Bloated Woman) | 649/646 | Вариант в Goddess of the Black Fan | alias в `contact-nyarlathotep` |
| Call the Black Pharaoh | 381/378 | Заклинание Шарифы и Black Rites | alias в соответствующей записи Call/Contact |
| «Talking to the Dead»: вариант Command Ghost у Му Сяня | 609/606 | Работает через личную вещь: 2 ПМ за вопрос, 30 минут | заметка в `command-ghost-folk` |
| Pulp: Alternative Ingredients (Brew Space Mead) | 650/647 | Кровь Ньярлатхотепа как ингредиент | заметка в `brew-space-mead` |
| Заклинание Хо Фана, связанное со статуей Раздутой женщины | 565/562 | Черпает ПМ статуи | заметка в `ho-fang` и в артефакте |
| Deciphering the Seven Cryptical Books | 582/579 | Расшифровка и ритуал Ока Света и Тьмы | заметка в `seven-cryptical-books-of-hsan`, `eye-of-light-and-darkness` |
| Ponape Scriptures | 141/138 | Коулз читал; копия Сиднейского университета не возвращена (John Scott) | `kb/tomes/ponape-scripture.json`: добавить источник Masks |
| People of the Monolith | 644/641 | Стихи Джастина Джеффри (связь с Amongst the Stones) | `kb/tomes/people-of-the-monolith.json`: источник Masks, связь |

## 10. Правила и врезки-механики (22)

Куда в kb: новый вид «правило» (короткая механика со ссылкой на главу) или `keeper_hint` у локации.

| Элемент | Стр. | Что содержит |
|---|---|---|
| Running This Campaign: Pulp or Classic, Lethality, Avoiding Certain Death, Luck Spending | 24–26/21–23 | Настройка смертоносности и траты Удачи |
| Spelling Conventions; Racism, Sexism | 25/22 | Соглашения и тон кампании |
| Creating Investigators, Useful Skills, Replacements, What If They All Die or Go Mad? | 29–30/26–27 | Создание и замена сыщиков |
| Money, Expenses | 25/22 | Деньги и расходы |
| Altitude Sickness | 75/72 | Горная болезнь в Андах |
| Firearms in the United Kingdom; Pulp: Customs Waiver | 182–183/179–180 | Оружие и таможня в Англии |
| London Fog; Getting About in London | 184–185/181–182 | Туман и транспорт |
| Legal Tender; Papers, Please! | 303/300 | Деньги и документы в Египте |
| Too Hot to Handle (жара, обезвоживание, тепловой удар) | 306/303 | Урон от жары и восстановление |
| Dragomen | 318/315 | Наём проводников |
| Languages (Кения) | 392/389 | Языки Кении |
| Tropical Diseases | 404/401 | Тропические болезни |
| Ecology of the Mountain; Dangerous Days | 429/426, 431/428 | Среда и угрозы у Горы Чёрного Ветра |
| Desert Survival | 481/478 | Вода, соль, движение по пустыне |
| Line Walkers (электролинии города) | 497/494 | Шум, проверки Удачи, привлечение культистов |
| Customs and Licenses (Китай) | 527/524 | Таможня и разрешения |
| Radiation (с пульп-врезкой) | 591/588 | Облучение у магмовой шахты |
| The Crawling Ceiling | 565/562 | Ловушка-узор (см. п. 3) |
| Travel: Recovery and Skills | 630–631/627–628 | Фаза развития, +1d3 Рассудка за спокойное плавание, обучение навыкам |
| Pulp: Airships | 630/627 | Цена и время перелёта на дирижабле |
| Пульп-врезки Weird Science (I, II, More, Workshop) | 269/266, 271/268, 595/592, 505/502 | Сниженная сложность для таланта Weird Science |
| Пульп-врезки по главам (около 75 шт. вместе с пульп-наградами: Evening Attack, Exploding Trucks!, Kaboom! и др.) | по всей книге | Альтернативные сцены для пульп-игры |

## 11. Сюжет: предыстория, ритуалы, развязка (25)

Куда в kb: новый вид «сюжет» (глава, события, ссылки на персонажей, локации и раздаточные материалы).

| Элемент | Стр. | Что содержит |
|---|---|---|
| Campaign Backstory: The Public Version / The Secret Version | 13/10 | Две версии событий экспедиции |
| The Great Plan: Now; The Great Plan Enacted | 15–16/12–13 | Замысел Ньярлатхотепа и 14 января 1926 г. |
| The Involvement of Jackson Elias | 17/14 | Как Элайес вышел на след |
| Nyarlathotep: Role in the Campaign, An Alternative Explanation, The Cults of… | 17–20/14–17 | Аватары и культы |
| Peru: Background, The Avatar in the Pyramid, The Fate of Larkin | 50/47, 85/82 | Предыстория и итоги пролога |
| The Carlyle Expedition Principals, The Carlyle Records | 142–145/139–142 | Исследование участников экспедиции |
| The Carlyle Expedition in Cairo; …and the Pyramids; Nitocris’ Plans | 300/297, 373/370 | Что экспедиция делала в Египте |
| What the Carlyle Expedition Did in Kenya | 389/386 | Хронология в Кении (см. п. 2) |
| Нитокрис по главам: London, Cairo, Kenya, Australia, Shanghai | 261/258, 366/363, 398/395, 499/496, 538/535 | Сквозная линия Нитокрис |
| Rites of the Bloody Tongue at Ju-Ju House | 162/159 | Обряды Нью-Йорка |
| Rites of the Brotherhood: Torture, Lesser Rites, Grand Rites | 281–282/278–279 | Обряды Лондона |
| The Cult’s Rituals; Special Rites for Queen Nitocris | 361/358 | Обряды Каира |
| Ordinary Rites; The Ritual of the Birth; Running the Ritual; Pulping Up the Ritual | 436–439/433–436 | Обряды Кении |
| Cult Rituals (Australia) | 500/497 | Обряды культа Песчаной летучей мыши |
| Rituals of the Order; The Special Ritual on the Day of Opening | 599/596 | Обряды Шанхая |
| Sidetrack: The Chelsea Serpent | 218–229/215–226 | Побочный сценарий |
| Sidetrack: The Derbyshire Horror | 230–249/227–246 | Побочный сценарий |
| Optional Sidetrack: The Scottish Horror; The Thing in the Fog | 209–210/206–207 | Набросок сценария и встреча с туманным отродьем |
| Sidetrack: The Black Cat | 329–336/326–333 | Побочный сценарий |
| Sidetrack: Buckley’s Ghost | 474–478/471–475 | Побочный сценарий |
| Sidetrack: The Demon Cabinet of Mister Lung | 548–555/545–552 | Побочный сценарий |
| Conclusion разделы глав (Possible Outcomes, Partial Victories, Aftermath) | 86/83, 163/160, 286/283, 373/370, 440/437, 509/506, 604/601 | Итоги глав |
| Constructing a Climax (England) | 283/280 | Как собрать кульминацию главы |
| Grand Conclusion: Finishing / Extending the Campaign | 625/622 | Финал и продолжение |
| Selected Passages from The Shadow Out of Time | 492/489 | Выдержки из Лавкрафта как подсказка игрокам |

---

## Сводка

| Категория | Позиций |
|---|---|
| 1. Статблоки (не перенесены или неполные) | 10 |
| 2. Таблицы и справочные списки | 31 |
| 3. Артефакты и предметы | 31 |
| 4. Раздаточные материалы | 69 документов (61 строка) |
| 5. Карты и схемы улик | 45 |
| 6. Локации | 79 |
| 7. Организации и культы | 28 |
| 8. Именные NPC без профиля | 27 строк (около 40 человек) |
| 9. Заклинания и тома (связи) | 11 |
| 10. Правила и врезки | 22 |
| 11. Сюжет | 25 |
| **Всего** | **378 позиций** |

Позиция — строка таблицы. Исключения: раздаточные материалы считаются по документам; карты — по картам и схемам. Строка про локацию может включать несколько мест (например, зоны Города Великой Расы).

## 10 самых ценных

1. **Локации Masks (в kb 0, в списке 79)**: города и ключевые здания по схеме Р-78. Это каркас кампании, к нему привязываются жители, раздаточные материалы и таблицы.
2. **69 раздаточных материалов Carlyle Papers** — основная цепочка улик кампании; нужен вид «раздаточный материал» со ссылками «где найдено» и «на кого указывает».
3. **Артефакты Приложения D (16 предметов, считая флаконы)** с механикой: Mask of Hayama, Mirror of Gal, Headdress of Eyes, предметы силы Нитокрис, Device of Rods…
4. **Ultimate Outcome и события 14 января 1926 г.** — подсчёт очков финала и последствия по главам.
5. **Timeline of Key Events 1916–1926** вместе с «Location of Carlyle Expedition Principals, January 1925».
6. **Организации и культы**: шесть культов Ньярлатхотепа и фирмы-прикрытия (Penhew Foundation, Randolph Shipping, Ho Fang Import/Export, Henson…).
7. **Случайные таблицы мест**: Events Beneath the Sphinx, Pits and Chasms, Desert Encounters, Plutonian Visions — сразу ложатся в `tables` локаций.
8. **Путешествия (Приложение A)**: матрица дней пути, цены, восстановление и обучение в пути, дорожные события, названия кораблей.
9. **Блоки погони (7 врезок Chase Quick Reference)** для существующих персонажей.
10. **Roger Carlyle и другие ключевые NPC без профиля** (Nuri, Montgomery, Bumption, Corydon, Brunton, Baines) плюс слухи и сплетни (Ndovu, Cuncudgerie, Darwin, Lesser Edale) для таблиц локаций.
