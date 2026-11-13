# «Грибы с Юггота»: главы II «Нечто в колодце» и III «Замок Тёмный» — сверка заголовков

Часть `castle` переноса кампании (Р-228). Книга `griby-s-yuggota-ru`, печатная страница = физическая − 1.
Страницы: физ. 16–32 (с. 15–31) и раздатки глав II–III: физ. 82, 83, 88, 89, 90–93. Префикс записей книги —
`G/` = `griby-s-yuggota-ru/`.

## Записи

| Вид | Записи |
|---|---|
| этапы (scenario) | `G/scenario/thing-in-the-well` (order 2), `G/scenario/castle-dark` (order 3) |
| города (общие, новые) | `coc:location:klausenburg`, `coc:location:klausenburg-environs`; Бостон — существующий `coc:location:boston` (предложения) |
| места: Бостон | `G/location/well-cornwallis-mansion`, `well-mansion-well`, `well-carriage-house`, `well-tower-laboratory`, `well-all-hearts-cemetery`, `well-cornwallis-crypt`, `well-boston-police-station` (7) |
| места: Клаусенбург | `G/location/castle-munte-mare`, `castle-drovosna`, `castle-drovosna-inn`, `castle-drovosna-church`, `castle-church-catacombs`, `castle-gypsy-camp`, `castle-hauptmann`, `castle-residence`, `castle-entry-hall`, `castle-parlor`, `castle-dining-room`, `castle-kitchen`, `castle-vacant-rooms`, `castle-guest-rooms`, `castle-storage`, `castle-study`, `castle-bedroom`, `castle-catacombs`, `castle-family-crypt`, `castle-workshop`, `castle-torture-chamber`, `castle-lair-of-nyogtha`, `castle-alchemical-laboratory`, `castle-soldiers-chamber`, `castle-escape-tunnel`, `castle-stable`, `castle-tower`, `castle-tower-room` (28) |
| сцены гл. II | `G/scene/well-…` (10): newspaper-archive, police-station, boston-globe, additional-clippings, mansion-grounds, mansion-interior, tower-laboratory, spectacles, all-hearts-cemetery, jeremy |
| сцены гл. III | `G/scene/castle-…` (22): research, drovosna, inn, henchmen, village-church, church-catacombs, gypsy-camp, vech-death, approach, residence-ground, study, bedroom, catacombs, lair-of-nyogtha, alchemical-laboratory, soldiers-chamber, escape-tunnel, stable, tower, baron-reacts, dinner, sergei |
| персонажи | `G/character/baron-hauptmann`, `ambrose-cornwallis`, `emily-cornwallis`, `sarah-cornwallis`, `jeremy-cornwallis`, `ted-ryder`, `larry-holmes`, `boston-detective` (имя придумано), `lazlo`, `jerzy`, `jurek`, `sergei-rosalovich`, `drobne`, `drovosna-priest` (имя придумано), `sarena`, `vech`, `jan-savechik`, `lionel-newman`, `count-spanglais` (19) |
| существа | `G/creature/well-dimensional-being` (уникальное), `G/creature/castle-star-vampire` (`instance_of` `coc:creature:star-vampire`); Ниогта — `coc:creature:nyogtha` |
| книги (сценарные) | `G/tome/castle-hauptmann-journals`, `castle-brotherhood-book`, `castle-rasputin-diary`; экземпляры общих книг (De Vermiis Mysteriis, «Аль-Азиф», «Текст Р’льеха», греческий «Некрономикон») — предложения `copies` |
| предметы | `G/item/well-hauptmann-spectacles`, `well-cornwallis-journal`, `castle-nofru-ka-tomb-map`, `castle-beast-vellum`, `castle-key-ring`, `castle-puzzle-box`, `castle-space-mead`, `castle-elder-sign-stone`, `castle-rlyeh-scroll`, `castle-sleeping-drug`, `castle-space-mead-recipe`, `castle-grenades` (12) |
| раздатки | `G/handout/well-handout-2` (РМ 2, картинки 2-а и 2-б), `well-extra-handout-4`, `well-extra-handout-5`, `castle-handout-3`, `castle-handout-4`, `castle-handout-5`; картинки — `app/art/handouts/well-*.webp`, `castle-*.webp` |
| карты | `G/map/castle-romania`, `castle-residence-main-floor`, `castle-residence-second-floor`, `castle-basement-and-catacombs`, `castle-tower-room` (картинки `app/maps/fungi-castle-romania.jpg`, `-main-floor`, `-second-floor`, `-catacombs`, `-tower-room`; 2 + 8 + 8 + 11 + 4 меток) |
| иллюстрации | Джереми (с. 16) → `jeremy-cornwallis`; окуляры (с. 18) → `well-hauptmann-spectacles`; замок (с. 26) → `castle-hauptmann`; скелеты (с. 30) → `castle-soldiers-chamber` (`app/art/…`) |
| таблицы | этап II: «Газетные вырезки о Корнуоллисах», «Журнал доктора Корнуоллиса»; у мест (Р-136, в этапе III — `from`): «Замок Гауптмана: сведения из библиотеки» (`castle-hauptmann`), «Записи прихода Дровосны» (`castle-church-catacombs`). Таблиц с броском нет |

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Бостон. Глава II «Нечто в колодце» (подзаголовок) | 15 | `thing-in-the-well` (name, summary) |
| Информация для сыщиков | 15 | `thing-in-the-well`.hook; `well-extra-handout-4` |
| Информация для хранителя | 15 | `thing-in-the-well`.keeper_info |
| Историческая справка | 15 | `thing-in-the-well`.keeper_info; `ambrose-cornwallis`, `emily-cornwallis`, `sarah-cornwallis` (legend) |
| Основная информация: Газетный архив | 15 | `well-newspaper-archive`; `well-extra-handout-5` |
| Полицейский участок Бостона | 15 | `well-police-station`; `well-boston-police-station`; `boston-detective` |
| Редакция Бостон Глоуб | 15–16 | `well-boston-globe`; `larry-holmes`; `coc:location:boston-globe` (предложение) |
| Дополнительная информация (вырезки 1–3) | 16 | `well-additional-clippings`; таблица «Газетные вырезки о Корнуоллисах» |
| СЦЕНЫ: Особняк Корнуоллисов | 16–17 | `well-mansion-grounds`; `well-cornwallis-mansion`, `well-mansion-well`, `well-carriage-house`; `ted-ryder` |
| Особняк Корнуоллисов внутри | 17 | `well-mansion-interior`; `well-cornwallis-mansion` |
| Сара Корнуоллис (статблок) | 17 | `sarah-cornwallis` |
| Лаборатория в башне, журнал на латыни 1–7 | 17–18 | `well-tower-laboratory` (сцена и место); `well-cornwallis-journal`; таблица «Журнал доктора Корнуоллиса» |
| Кладбище Олл Хартс | 18 | `well-all-hearts-cemetery` (сцена и место); `well-cornwallis-crypt` |
| ФИНАЛ (гл. II) | 18 | `thing-in-the-well`.conclusion; `well-jeremy` |
| Раздаточный материал 2: Глава II | 18, 81, 89–90 | `well-handout-2` |
| Окуляры Гауптмана (врезка) | 19 | `well-hauptmann-spectacles`; `well-spectacles` |
| Джереми Корнуоллис (врезка, статблок) | 19 | `jeremy-cornwallis` |
| Существо из другого измерения (врезка, статблок) | 19 | `well-dimensional-being`; `well-spectacles` |
| Главное, что должны узнать сыщики… | 19 | `thing-in-the-well`.advice |
| Трансильвания, Румыния. Глава III «Замок Тёмный» (подзаголовок) | 20 | `castle-dark` (name, hook) |
| Информация для сыщиков | 20 | `castle-dark`.hook; `castle-research` |
| Информация для хранителя | 20 | `castle-dark`.keeper_info |
| Историческая справка | 20 | `castle-dark`.keeper_info; `castle-hauptmann`.history; `baron-hauptmann` |
| Начало игры | 20 | `castle-dark`.hook; `coc:location:klausenburg-environs` |
| Хранителю на заметку (Бела Лугоши, Клуж) | 20 | `castle-dark`.advice; `coc:location:klausenburg` |
| Основная информация 1–4 | 20 | таблица «Замок Гауптмана: сведения из библиотеки» (`castle-hauptmann`); `castle-research` |
| СЦЕНЫ: Село Дровосна | 20–21 | `castle-drovosna` (сцена и место); `castle-munte-mare` |
| Трактир | 21 | `castle-inn`; `castle-drovosna-inn`; `drobne` |
| Джон Копич (статблок) | 21 | `sergei-rosalovich` |
| Приспешники Гауптмана | 21 | `castle-henchmen` |
| Лазло (статблок) | 21 | `lazlo` |
| Подручные Лазло: Джерзи, Юрек (статблоки) | 21 | `jerzy`, `jurek` |
| Сельская церковь | 21–23 | `castle-village-church`; `castle-drovosna-church`; `drovosna-priest` |
| Карта «Roumania and Bulgaria» | 22 | `castle-romania` |
| Раздаточный материал 3: Глава III | 23, 82, 91 | `castle-handout-3`; `jan-savechik` |
| Зацепки 1–6 | 23–24 | таблица «Записи прихода Дровосны» (`castle-church-catacombs`); `castle-church-catacombs` (сцена); `count-spanglais` |
| Цыганский лагерь | 24 | `castle-gypsy-camp` (сцена и место) |
| Сарена (статблок) | 24 | `sarena` |
| Вех (статблок); гибель Веха | 24 | `vech`; `castle-vech-death`; `castle-star-vampire` |
| Замок Гауптмана | 24 | `castle-approach`; `castle-hauptmann` |
| Резиденция Гауптмана: Первый этаж (Прихожая, Гостиная, Столовая, Кухня, Пустые комнаты) | 24–25 | `castle-residence-ground`; `castle-residence`, `castle-entry-hall`, `castle-parlor`, `castle-dining-room`, `castle-kitchen`, `castle-vacant-rooms` |
| План «Castle Hauptman MAIN FLOOR» | 25 | `castle-residence-main-floor` |
| Резиденция Гауптмана: Второй этаж (Гостевые комнаты, Кладовая, Кабинет Гауптмана) | 25–26 | `castle-study` (сцена); `castle-guest-rooms`, `castle-storage`, `castle-study`; `castle-hauptmann-journals`, `castle-brotherhood-book`, `castle-nofru-ka-tomb-map`, `castle-beast-vellum`, `castle-key-ring`, `castle-puzzle-box` |
| План «Castle Hauptman SECOND FLOOR» | 25 | `castle-residence-second-floor` |
| Спальня Гауптмана | 26–27 | `castle-bedroom` (сцена и место) |
| План «Castle Hauptman BASEMENT AND CATACOMBS» | 27 | `castle-basement-and-catacombs` |
| Раздаточный материал 4: Глава III | 27, 82, 92 | `castle-handout-4` |
| Подвал и катакомбы: Фамильный склеп, Мастерская, Камера пыток | 27 | `castle-catacombs` (сцена и место); `castle-family-crypt`, `castle-workshop`, `castle-torture-chamber` |
| Логово Ньогта | 27–28 | `castle-lair-of-nyogtha` (сцена и место); `coc:creature:nyogtha` |
| Алхимическая лаборатория | 28 | `castle-alchemical-laboratory` (сцена и место); `castle-sleeping-drug`, `castle-space-mead-recipe` |
| Камера | 28 | `castle-soldiers-chamber` (сцена и место); `castle-rasputin-diary`, `castle-grenades` |
| Туннель | 28 | `castle-escape-tunnel` (сцена и место) |
| Стойло | 28 | `castle-stable` (сцена и место) |
| Башня; Вход в верхнюю часть башни; Область обсерватории; Стальные ступени; Подиум | 28–29 | `castle-tower` (сцена); `castle-tower`, `castle-tower-room`; `castle-space-mead`, `castle-elder-sign-stone`, `castle-rlyeh-scroll`; De Vermiis Mysteriis — предложение `copies` |
| План «Castle Hauptman TOWER ROOM» | 29 | `castle-tower-room` (карта) |
| Раздаточный материал 5: Глава III | 29, 82, 92 | `castle-handout-5` |
| Барон Гауптман (описание, статблок) | 29–30 | `baron-hauptmann`; `lionel-newman` |
| Перемещение сознания (врезка) | 29 | `baron-hauptmann`.abilities; `coc:spell:mind-transfer` (предложение: псевдоним и пометка) |
| Взрыв мозга (врезка) | 29 | `baron-hauptmann`.abilities; `coc:spell:mindblast` (предложение: пометка) |
| ФИНАЛ (гл. III) | 30–31 | `castle-dark`.conclusion; `castle-baron-reacts`, `castle-dinner`, `castle-sergei` |
| Доп. раздаточный материал 4. Глава II | 87 | `well-extra-handout-4` |
| Доп. раздаточный материал 5. Глава II | 88 | `well-extra-handout-5` |
| Раздаточный материал 2-а, 2-б (оформленные письма) | 89–90 | `well-handout-2`.images |
| Раздаточный материал 3 (оформленный) | 91 | `castle-handout-3`.images |
| Раздаточный материал 4, 5 (оформленные) | 92 | `castle-handout-4`.images, `castle-handout-5`.images |

## Не взято

- Эмблема-лев «NWI» (с. 19 и 31) — декоративная заставка корпорации «Новый Мир», текста и сведений нет; при желании — картинка записи `G/organization/new-world-incorporated` (часть final).
- Подписи масштаба на планах (20 ft, 40 ft, 10 ft) и сетка долгот/широт карты Румынии — не метки; масштабы пересчитаны в пометках карт.
- Города и селения карты «Roumania and Bulgaria», кроме Клаусенбурга, — записей нет, меток нет.
- Раздаточный материал 1 и Доп. 2–3 на с. 81, 87 — глава I (часть intro).
- Заметка о гробокопателе (вырезка 3) отдельной раздаткой не напечатана: книга ошибочно ссылается на Доп. 5 (опечатка в записях).
- Бакалейная лавка Теда, газетный архив и «публичная библиотека» без адреса — мест не заведено: книга их не описывает, они упомянуты в текстах сцен.
- Исторические лица (Распутин, Джон Ди, Эдвард Келли, Людвиг Принн, Герман фон Сальца, Людовик Великий) — только текстом (в базе записей нет; кандидатов не предлагаю).

## Опечатки и сомнения книги (в `errata` записей)

- Вырезка 3 «(Доп. Раздаточный материал 5)» — на с. 88 другая статья (о третьем убитом ребёнке); в оригинале 1984 года заметка о гробокопателе от 16 ноября 1891 года (`well-additional-clippings`, `well-extra-handout-5`, этап II).
- Репортаж о двойном убийстве датирован 30 августа 1891 года, а статья конца сентября говорит «ранее в том же месяце» (оригинал — 15 сентября) (`well-additional-clippings`, этап II).
- Склеп Корнуоллисов: 12 ниш, в оригинале 20 гробов (`well-cornwallis-crypt`).
- Джереми: ПЗ 11 при ВЫН 60 и ТЕЛ 80 (так и в оригинале); Скорость 6 вместо 7 (`jeremy-cornwallis`).
- «Пророчество Нофру-Ка (см. Приложение 4)» — это Раздаточный материал 4 (`castle-dark`, исправлено в записи).
- Раздаточный материал 5: «во втором зале слева», в оригинале — справа (second gallery right) (`castle-handout-5`) — сверить с «Залами Целаено».
- Дневник Распутина: взрыв в Сибири «в 1907 году» (так и в оригинале; Тунгусский взрыв — 1908) (`castle-rasputin-diary`, `castle-soldiers-chamber`).
- Барон Гауптман: МОЩ 80 и ОБР 155 не соответствуют пересчёту оригинала (32 и 35 по шкале 3–18) — как напечатано, пометка в `quality.notes`.
- «Описание Р’льеха» — перевод названия книги R’lyeh Text (предложение псевдонима `coc:tome:rlyeh-text`).
- Сила снотворного «12 пунктов» — правила ядов старых редакций; оставлено как напечатано.
- Доктор Корнуоллис — «доктор физики» (в оригинале physician, врач); как напечатано, пометка.
