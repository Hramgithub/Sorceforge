# «Грибы с Юггота» (RU 7e), глава V «Горы Луны» — сверка покрытия (часть moon)

Страницы — печатные 40–50 (физ. 41–51; содержание ошибочно даёт началом главы с. 39) и раздатки главы V: с. 83 (физ. 84,
РМ 7), с. 94 (физ. 95, Доп. 6 и 7), с. 95 (физ. 96, РМ 7 оформленный), с. 96 (физ. 97, Доп. 8). Этап —
`griby-s-yuggota-ru/scenario/mountains-of-the-moon` (Р-228). Текст — официальное русское издание (флага `translated` нет);
английский оригинал 1984 г. — только для `name.en` и сверки опечаток.

Сокращения: `…/` = `griby-s-yuggota-ru/`; сцены — `…/scene/moon-*`, места — `…/location/moon-*`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Колонтитул «Перу», титул «Глава V. "Горы луны"» с подзаголовком | 40 | этап `…/scenario/mountains-of-the-moon` (`name`, `summary`) |
| Информация для сыщиков (Доп. раздаточный материал 6) | 40 | этап: `hook`; сцена `…/scene/moon-vision-and-research`; раздатка `…/handout/moon-extra-handout-6` |
| Информация для хранителя | 40 | этап: `keeper_info`; `…/item/moon-blue-john`; организация `…/organization/moon-goyo-rebels`; персонажи `…/character/jonathan-harris`, `…/character/melvin-peale`, `…/character/goyo` |
| Историческая справка (пророчество о «Призраке, который ходит») | 40 | этап: `keeper_info`; организация `…/organization/moon-huari` |
| Основная информация (Доп. раздаточный материал 7; Знания, Геология) | 40–41 | этап: `hook`; сцена `moon-vision-and-research`; раздатка `…/handout/moon-extra-handout-7` |
| Начало игры (Легуя, корабль, дорога в Хуанкучо, язык, высокогорье) | 41 | этап: `hook`, `advice`; сцена `moon-journey-to-huancucho`; общая область `coc:location:lima-environs`; факты о Лиме — предложение в `proposals-moon.json` |
| СЦЕНЫ | 41 | этап: `steps` |
| Хуанкучо и магазин | 41 | сцена `moon-trading-post`; места `…/location/moon-huancucho`, `…/location/moon-trading-post` |
| Хранителю на заметку («дядя Виктор») | 41 | этап: `advice`; сцена `moon-trading-post`; персонаж `…/character/victor-montain` |
| Перестрелка | 41 | сцена `moon-gunfight` |
| Виктор Монтэйн (описание, статблок; «карта сокровищ») | 41–42 | персонаж `…/character/victor-montain`; предмет `…/item/moon-treasure-map` |
| Карта Перу и Боливии (Rand McNally, без подписи) | 42 | карта `…/map/moon-peru` (картинка `app/maps/fungi-moon-peru.jpg`, метки LIMA, Puno, Lake Titicaca) |
| Жена Виктора (статблок) | 42 | персонаж `…/character/victor-montain-wife` (имя придумано, Р-150) |
| Перуанская армия | 43 | сцена `moon-army-patrol`; организация `…/organization/moon-peruvian-army-patrol` |
| Путь к шахте (стычки, большая гадюка) | 43 | сцена `moon-trail-to-mine`; место `…/location/moon-mine-trail` |
| Санчо (статблок) | 43 | персонаж `…/character/sancho` |
| Шахтёрский лагерь (встреча с Харрисом, экскурсия) | 43 | сцена `moon-mine-camp-arrival`; места `…/location/moon-mine-camp`, `…/location/moon-nwi-mine` |
| Джонатан Харрис (статблок) | 44 | персонаж `…/character/jonathan-harris` |
| Административное здание, офис Харриса, комната охраны, офис доктора (без заголовков) | 44 | сцена `moon-administration-search`; места `…/location/moon-administration-building`, `moon-harris-office`, `moon-security-office`, `moon-doctor-office`; предметы `moon-geological-maps`, `moon-shipping-bills`; раздатка `…/handout/moon-extra-handout-8` |
| Раздаточный материал 7: Глава V (письмо Харриса Чандлеру) | 44 (и 83, 95) | раздатка `…/handout/moon-handout-7` (картинка — с. 95) |
| Шахтёры (слухи, могилы, эксгумация) | 45 | сцена `moon-camp-rumors`; персонажи `…/character/moon-miners`, `…/character/moon-missing-miner` |
| Трупы индейцев (табличка Хуари) | 45 | сцена `moon-dead-indians`; предмет `…/item/moon-wooden-tablet` |
| Мелвин Пил (статблок) | 45 | персонаж `…/character/melvin-peale` |
| Охранники (статблок) | 45 | групповой профиль `…/character/moon-mine-guards` |
| Доктор Лоуренс Ричардс (статблок) | 45–46 | персонаж `…/character/lawrence-richards` |
| Враждебные индейцы | 46 | организация `…/organization/moon-huari`; этап: `advice` |
| Сектор А-48 | 46 | сцена `moon-sector-a-48`; место `…/location/moon-sector-a-48` |
| Грибы | 46 | сцена `moon-mi-go-hunt`; `coc:creature:mi-go` (ссылки) |
| Пещера Ми-Го | 46 | сцена `moon-cave-gate`; место `…/location/moon-mi-go-cave` |
| Колония на луне (камера врат, коридоры) | 46–47 | сцена `moon-lunar-arrival`; место `…/location/moon-lunar-colony` |
| Иллюстрация: ми-го в горах | 47 | картинка сцены `moon-sector-a-48` |
| Хирургия (без заголовка; цилиндры, мозг шахтёра) | 47–48 | сцена `moon-surgery`; место `…/location/moon-mi-go-surgery`; предмет `…/item/moon-brain-cylinders` |
| Оружие Ми-Го (врезка) | 47 | предмет `…/item/moon-mi-go-weapon` |
| Кратер (без заголовка; церемония, Шуб-Ниггурат) | 48 | сцена `moon-crater-rite`; место `…/location/moon-lunar-crater` |
| Укрытие повстанцев | 48 | сцена `moon-rebel-hideout-visit`; место `…/location/moon-rebel-hideout`; предмет `…/item/moon-rebel-papers` |
| Гойо (статблок) | 48 | персонаж `…/character/goyo` |
| Повстанцы (статблок) | 48 | групповой профиль `…/character/moon-rebels`; организация `…/organization/moon-goyo-rebels` |
| Призыв Дитя Йига; Подчинение Дитя Йига (врезка) | 49 | сцена `moon-altar-visit` (`mechanics`); таблица этапа «Горы Луны: потеря Рассудка»; новое заклинание — проект в отчёте (`kb/spells` — общий справочник) |
| Алтарь Йига | 49 | сцена `moon-altar-visit`; место `…/location/moon-altar-of-yig` (с иллюстрацией) |
| Йиг | 49 | сцена `moon-altar-visit`; `coc:creature:yig`, `coc:spell:contact-yig` (ссылки) |
| «Призрак, который ходит» (Нганса, статблок, броня, заклинания) | 49–50 | персонаж `…/character/ngansa`; сцена `moon-ngansa-appears`; предмет `…/item/moon-ngansa-paste` |
| Хранителю на заметку (прибытие Нгансы) | 50 | этап: `advice`; сцена `moon-ngansa-appears` |
| ФИНАЛ | 50 | этап: `conclusion`, таблица «Горы Луны: улики финала»; предмет `…/item/moon-nwi-gate-sign` |
| Посох Нганса (врезка) | 50 | предмет `…/item/moon-ngansa-staff` |
| Логотип NWI (рисунок) | 50 | картинка предмета `moon-nwi-gate-sign` |
| Раздаточный материал 7 (набор раздаток) | 83 | раздатка `moon-handout-7` (источник) |
| Доп. раздаточный материал 6: стенограмма видения Пола ЛеМонда | 94 | раздатка `…/handout/moon-extra-handout-6` (текст снят с картинки) |
| Доп. раздаточный материал 7: газетная статья о землетрясениях в Перу | 94 | раздатка `…/handout/moon-extra-handout-7` (текст снят с картинки) |
| Раздаточный материал 7 (оформленный, бланк NWI) | 95 | картинка раздатки `moon-handout-7` |
| Доп. раздаточный материал 8: клочок бумаги | 96 | раздатка `…/handout/moon-extra-handout-8` |

Общая область (новая): `coc:location:lima-environs` — Хуанкучо, тропа, лагерь и шахта НМ, сектор А-48, пещера ми-го,
укрытие повстанцев, алтарь Йига (`part_of`). Колония ми-го на Луне — `location_type: город сценария`, `part_of: null`.

## Не взято

- Колонтитул «Перу» — оформление.
- Обрывки соседних газетных колонок на картинке Доп. раздаточного материала 7 («Как мн здесь в…», «В НА ПО Все могл…») —
  декоративный фон, текста нет.
- Остальные подписи атласной карты Перу и Боливии (страны, Тихий океан, Callao, Cuzco, Arequipa, Iquitos, La Paz и др.) —
  записей в базе нет; метки поставлены на LIMA, Puno, Lake Titicaca.
- Рисунок Раздаточного материала 8 главы VI на с. 96 — часть bay.
- Большая гадюка, ламы, собаки — без статблоков и механики, остаются текстом сцен.
- Заклинания «Призыв/Подчинение Дитя Йига» и «Вызвать/Связать Дхоула» — записей нет; первое — проект в отчёте части,
  механика — в сцене `moon-altar-visit`; второе — упоминание (Голубой Джон — ингредиент фимиама).

## Опечатки и сомнения (errata)

- Содержание: глава V на с. 39, на деле — с. 40 (этап).
- «В пятидесяти милях севернее Перу» (с. 40; в оригинале «northwest of Peru») — так в книге, по газете — недалеко от Лимы
  (этап, сцена `moon-vision-and-research`).
- Ключ от картотеки Харриса на связке в комнате охраны: в русском издании есть, в оригинале — единственное исключение
  (сцена `moon-administration-search`).
- Направления в колонии (гул слева/справа) противоречат друг другу и в оригинале (сцена `moon-lunar-arrival`).
- Хирургия «площадью сорок квадратных футов» — в оригинале квадрат 40 × 40 футов (сцена `moon-surgery`).
- Доктор Ричардс: выпал навык Treat Disease 95% (персонаж `lawrence-richards`).
- Нганса: ПЗ 15 при ВЫН 80 и ТЕЛ 60 (по правилам 14) — перенесено из старой редакции (персонаж `ngansa`).
- Доп. раздаточный материал 8: заголовок называет стол офиса Харриса, текст главы — комнату охраны (раздатка `moon-extra-handout-8`).
