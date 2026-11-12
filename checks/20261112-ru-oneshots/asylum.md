# «Лечебница» (`lechebnitsa-ru`) — сверка переноса (часть asylum)

Источник — любительский перевод сценария Кита Хербера «The Sanatorium» (сборник «Mansions of Madness», Chaosium,
1990, 2007) с доработками и адаптацией для 7-й редакции (Hort), PDF 31 страница с текстовым слоем; издание `trusted`.
Правила — 7-я редакция (`ruleset` core), действие — 1920-е (убийства Бланш в канун Рождества 1922 года, Брюэр
встретил Хардинга в 1923-м, гробница Тутанхамона), `axes.era` — `1920s`. Статблоки и карты сверены по изображениям
страниц (200 dpi).

Флаг `translated` не ставился: по правилам записи (`docs/conventions.md` §3, Р-21, Р-147) он означает только *наш*
перевод с английского, а здесь русский текст — надёжный перевод из библиотеки владельца. Если ведущий хочет помечать
фанатские переводы этим флагом (как сказано в задании), его можно поставить пакетно на все 112 записей.

## Страницы

Номеров страниц в PDF нет: **печатная = физическая** (смещение 0).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Заголовок: «Лечебница», Кит Хербер, «The Sanatorium», выходные данные | 1 | сценарий `lechebnitsa-ru/scenario/lechebnitsa` (summary, sources) |
| Вступление | 1 | сценарий: advice (поводы для приглашения, навыки, Тиллер); `…/character/oldos-bryuer`; `…/character/genri-tiller` |
| Информация для сыщиков | 1–2 | сценарий: hook |
| Материал 1 — Письмо доктора Брюэра | 2 | раздатка `…/handout/material-1-pismo-bryuera` |
| Материал 2 — Фрагмент статьи доктора Брюэра | 3 | раздатка `…/handout/material-2-fragment-stati` |
| Информация для Хранителя | 3 | сценарий: keeper_info |
| Что произошло | 3–4 | сценарий: keeper_info; легенды персонажей; существо `…/creature/sushchestvo-iz-inogo-mira` (legend) |
| Что произойдёт | 4–5 | сценарий: keeper_info, advice (темп); сцены `zhertvoprinoshenie`, `okhota-na-dzhonsona` |
| Обитатели лечебницы | 5 | сценарий: keeper_info; сцена `…/scene/psikhoanaliz-khardinga` («Сеансы с пациентами»); организация `…/organization/personal-lechebnitsy` |
| Обычные пациенты | 5–6 | сценарий: keeper_info; персонажи ниже |
| Бланш Годдард Ричмонд, детоубийца | 6 | `…/character/blansh-richmond` |
| Генри Адам Барбер III, богатый наследник и социопат | 6–7 | `…/character/genri-barber` |
| Полковник Крэндалл Биллингс, старый вояка | 7 | `…/character/krendall-billings` |
| Миссис Сесиль (Карла) Рэндольф, светская львица | 7 | `…/character/sesil-rendolf` |
| Особые пациенты | 8 | сценарий: keeper_info; персонажи ниже |
| Аллен Хардинг, одержимый поэт (подсказки 1–4) | 8 | `…/character/allen-kharding`; таблица «Бред Хардинга» в сценарии; сцена `psikhoanaliz-khardinga` |
| Дарлин, женщина с множественным прошлым; «От переводчика» | 9 | `…/character/darlin`; таблица «Личности Дарлин» в сценарии |
| Леонард Хокинс, провозвестник рока | 9 | `…/character/leonard-khokins` |
| Врезка «Гипноз» | 10 | сценарий: advice (правила врезки по пунктам); сцена `kontakt-s-anefis` |
| Путь на остров | 10–11 | сцена `…/scene/put-na-ostrov`; `…/character/ebenezer-ueyt`; предмет `…/item/medalon-ebenezera` |
| Высадка | 11 | сцена `…/scene/vysadka`; место `…/location/prichal` |
| Лечебница: Парадный вход | 11 | сцена `…/scene/paradnyy-vkhod` |
| Первый этаж: Фойе, Столовая, Кладовая, Библиотека, Гостиная | 11–13 | места `foye`, `stolovaya`, `kladovaya`, `biblioteka`, `gostinaya` (часть `lechebnitsa-pervyy-etazh`); сцена `telo-v-gostinoy`; `…/character/ketrin-ems` |
| План «Лечебница Норт-Айленд» (первый этаж, подвал, второй этаж) | 12 | карта `…/map/plan-lechebnitsy` (`app/maps/asylum-plan-lechebnitsy.jpg`, 49 меток) |
| Первый этаж: больничное крыло — Склад, Стол и стул, Санузел, Палаты пациентов 1–5, Прачечная | 13–14 | `…/location/lechebnitsa-bolnichnoe-krylo` (стол и стул — в описании), `sklad`, `sanuzel`, `komnata-1` … `komnata-5`, `prachechnaya`; сцена `bolnichnoe-krylo`; `…/character/bobbi-byorch`, `…/character/melba`; предметы `smiritelnye-rubashki` |
| Подвал: Палаты пациентов 1–4, Спальня Чарльза Джонсона | 14 | `…/location/lechebnitsa-podval`, `podval-palata-1` … `podval-palata-4`, `spalnya-dzhonsona`; сцена `podval`; предмет `vrata-v-palate-khardinga` |
| Второй этаж: Гостевые комнаты, Спальни Эмс, Бёрч и Брюэра, Кабинет доктора Брюэра | 14–16 | `…/location/lechebnitsa-vtoroy-etazh`, `gostevye-komnaty`, `spalnya-ketrin-ems`, `spalnya-bobbi-byorch`, `spalnya-bryuera`, `kabinet-bryuera`; сцена `vtoroy-etazh`; предметы `bumazhka-s-kodom-seyfa`, `seyf-bryuera`, `revolver-i-klyuchi-bryuera`, `kartoteka-bryuera`; книги `…/tome/manuskript-kastro`, `…/tome/stikhi-allena-khardinga` |
| Материал 3 — Неоконченное письмо | 15 | раздатка `…/handout/material-3-neokonchennoe-pismo` |
| Материал 4 — Из дневника доктора Брюэра | 16 | раздатка `…/handout/material-4-iz-dnevnika-bryuera`; `…/character/dzheymson` |
| Кладовая медикаментов, Смотровая, Комната электрошоковой терапии | 16 | `kladovaya-medikamentov`, `smotrovaya`, `komnata-elektroshokovoy-terapii`; предмет `uspokoitelnye-preparaty` |
| Материал 5а — Из личного дела Дарлин | 17 | раздатка `…/handout/material-5a-delo-darlin` |
| Материал 5b — Из личного дела Аллена Хардинга | 18 | раздатка `…/handout/material-5b-delo-khardinga` |
| Материал 5c — Из личного дела Леонарда Хокинса | 18 | раздатка `…/handout/material-5v-delo-khokinsa` |
| Материал 6 — Из личного дела Чарльза Джонсона | 19 | раздатка `…/handout/material-6-delo-dzhonsona` |
| Материал 7 — Заложенная страница «Манускрипта Кастро» | 19 | раздатка `…/handout/material-7-stranitsa-manuskripta` |
| Материал 8 — Газетная вырезка | 19 | раздатка `…/handout/material-8-gazetnaya-vyrezka` |
| Территория лечебницы (рисунок): Мёртвый кот, Домик Мельбы, Лачуга Эбенезера, Хозблок, Генераторная, Деревья, Скалы, Причал | 20–21 | `…/location/territoriya-lechebnitsy` (кот, деревья, скалы — в описании), `dom-melby`, `khizhina-ebenezera`, `khozblok`, `generatornaya`, `prichal`; карта `…/map/territoriya-lechebnitsy` (`app/maps/asylum-territoriya-lechebnitsy.jpg`, 8 меток); сцены `territoriya-lechebnitsy`, `ubiystvo-na-prichale`; предмет `kanistry-benzina` |
| Материал 9 — Письмо из хижины Эбенезера Уэйта | 21 | раздатка `…/handout/material-9-pismo-ebenezeru`; `…/character/uilyam` |
| Оставшаяся часть острова | 21 | город сценария `…/location/nort-aylend` (Р-190) |
| Лагерь студента | 21–22 | `…/location/lager-shelli`; сцена `lager-shelli`; `…/character/dzheyms-shelli`; предметы `pistolet-shelli`, `dnevnik-shelli` |
| Карта «Норт-Айленд» | 22 | карта `…/map/nort-aylend` (`app/maps/asylum-nort-aylend.jpg`, 10 меток) |
| Кораблекрушение | 22–23 | `…/location/korablekrushenie`; сцена `korablekrushenie`; предмет `svintsovaya-plastina` |
| Жертвенный камень | 23 | `…/location/zhertvennyy-kamen`; сцены `lager-shelli`, `zhertvoprinoshenie` |
| Убежище Джонсона | 23 | `…/location/ubezhishche-dzhonsona`; `…/character/charlz-dzhonson`; сцена `okhota-na-dzhonsona` |
| Маяк (облик и уязвимости существа) | 23 | `…/location/mayak`; сцена `mayak`; существо (description, abilities) |
| Вероятная последовательность событий | 23–24 | сцены `zhertvoprinoshenie`, `okhota-na-dzhonsona`, `mayak`, `chudovishche-u-lechebnitsy`; сценарий: steps, conclusion |
| Существо из иного мира (статблок) | 24–25 | `…/creature/sushchestvo-iz-inogo-mira` |
| Уничтожение чудовища | 25 | сцена `…/scene/unichtozhenie-chudovishcha`; существо: abilities |
| Контакт с царевной Анефис | 25–26 | сцена `…/scene/kontakt-s-anefis`; `…/character/anefis`; предмет `retsept-dlya-darlin` |
| Врезка «Благословление Баст»; «От переводчика» | 26 | сцена `kontakt-s-anefis` (mechanics); общее заклинание `coc:spell:blessing-of-bast` (источник — предложение) |
| Если чудовище не удастся уничтожить | 26–27 | сцена `…/scene/preobrazhenie` |
| Награды за успех | 27 | сценарий: conclusion; сцены `unichtozhenie-chudovishcha`, `preobrazhenie` |
| Характеристики персонажей: Бланш, Генри, Биллингс, Рэндольф, Хардинг, Дарлин | 27–28 | статблоки персонажей |
| Царевна Анефис, Леонард Хокинс, Чарльз Джонсон, Джеймс Шелли, Доктор Генри Тиллер | 28 | статблоки `anefis`, `leonard-khokins`, `charlz-dzhonson`, `dzheyms-shelli`, `genri-tiller` |
| Приложение 1. Заклинания царевны Анефис: Благословление Баст, Знак Древних, Ужасное проклятье Азатота, Увядание, Призыв/подчинение ночного призрака | 29–30 | ссылки `statblock.spells` Анефис на общие записи (`blessing-of-bast`, `elder-sign`, `dread-curse-of-azathoth`, `shrivelling`, `summon-bind-nightgaunt`); фанатские названия и альтернативные имена — в `proposals-asylum.json` |
| Приложение 2. Множественные умы Дарлин Доу (1d8) | 31 | таблица «Личности Дарлин» в сценарии; `coc:creature:dark-young-of-shub-niggurath` (Энья) |

## Записи (112)

- сценарий 1: `lechebnitsa`;
- сцены 19: `put-na-ostrov`, `vysadka`, `paradnyy-vkhod`, `telo-v-gostinoy`, `bolnichnoe-krylo`, `podval`, `vtoroy-etazh`,
  `territoriya-lechebnitsy`, `ubiystvo-na-prichale`, `zhertvoprinoshenie`, `lager-shelli`, `korablekrushenie`,
  `psikhoanaliz-khardinga`, `kontakt-s-anefis`, `okhota-na-dzhonsona`, `mayak`, `chudovishche-u-lechebnitsy`,
  `unichtozhenie-chudovishcha`, `preobrazhenie`;
- места 43: город сценария `nort-aylend`; здание `lechebnitsa-nort-aylend` с этажами (`lechebnitsa-pervyy-etazh`,
  `lechebnitsa-bolnichnoe-krylo`, `lechebnitsa-podval`, `lechebnitsa-vtoroy-etazh`) и 25 помещениями (5 комнат и 4 палаты
  с номерами плана); `territoriya-lechebnitsy` и 5 строений/мест; 5 мест острова (`mayak`, `lager-shelli`,
  `korablekrushenie`, `zhertvennyy-kamen`, `ubezhishche-dzhonsona`);
- карты 3: `plan-lechebnitsy` (49 меток), `territoriya-lechebnitsy` (8), `nort-aylend` (10);
- персонажи 18: со статблоком — `blansh-richmond`, `genri-barber`, `krendall-billings`, `sesil-rendolf`, `allen-kharding`,
  `darlin`, `anefis`, `leonard-khokins`, `charlz-dzhonson`, `dzheyms-shelli`, `genri-tiller`; без статблока — `oldos-bryuer`,
  `ketrin-ems`, `bobbi-byorch`, `melba`, `ebenezer-ueyt`, `dzheymson`, `uilyam`;
- существо 1: `sushchestvo-iz-inogo-mira` (уникальное, вида в справочнике нет);
- книги 2: `manuskript-kastro`, `stikhi-allena-khardinga`;
- предметы 13, раздатки 11, организация 1 (`personal-lechebnitsy`).

Город: сценарий не называет города — остров «Норт-Айленд» у берегов Новой Англии заведён «городом сценария» внутри
книги (Р-190), общая запись в `kb/locations/` не создавалась. Упомянутые Бостон, Иннсмут, Каир, Лондон — ссылками
на существующие общие записи.

## Опечатки и выводы

- Хардинг (с. 27): БкУ 0 и Комплекция 0 при СИЛ + ТЕЛ = 125 (ожидается +1d4 и 1) — errata.
- Анефис (с. 28): ПМ 11 при МОЩ 90 (ожидается 18; переписано у Дарлин) — errata; три датировки её жизни (ок. 1000,
  ок. 1400 до н. э., «около 3000 лет назад») — errata.
- Хокинс (с. 28): ПЗ 14 (по ВЫН 65 + ТЕЛ 60 — 12) и ПМ 14 (по МОЩ 50 — 10) — errata.
- Шелли (с. 28): ПЗ 14 (по ВЫН 60 + ТЕЛ 65 — 12) — errata.
- Бланш, Биллингс, Рэндольф: БкУ «-1d4» при СИЛ + ТЕЛ 65–84 — в 7-й редакции −1 — errata.
- Джонсон: Уклонение 25% при ЛВК 60 (по правилам не ниже 30%) — errata; МОЩ 9 и ПМ 1 — как напечатано (сходятся).
- Существо (с. 24): БкУ +1d6 при СИЛ + ТЕЛ = 360 (ожидается +3d6; Комплекция 4 напечатана верно) — errata; урон огнём
  «2d6 на пять литров» (с. 23) против «канистра в пять галлонов — 2d6» (с. 25) — errata.
- Комната 2 (с. 13): «полковника Крэндалла Бриггса» вместо Биллингса — errata в месте и у персонажа.
- Бобби Бёрч: «медсестёр Бобби Бёрч и Кэтрин Эмс» (с. 4) против «санитар Бобби… его тело» (с. 13) — errata, пол не указан.
- Причал (с. 20): «обнаружат там мёртвого Джонсона» — должно быть Эбенезера — errata в сцене `ubiystvo-na-prichale`.
- Рэндольф: «Сесиль (Карла)» (с. 7) и «Сесиль (Барбара)» (с. 27) — errata, оба в псевдонимах. ОБР 14 — как напечатано
  (подозрительно мало для светской дамы, но доказательств опечатки нет).
- Длина острова: «немногим больше мили» (с. 21) против «1.5 мили с севера на юг» (карта) — пометка в записи острова.
- Меры (Р-64): рост Бланш «около пяти футов» → 1,5 м; канистры «5 галлонов» → 19 л (и в цитате способности существа);
  остров 1,6 × 0,8 км; в раздатке 8 «в двадцати милях» → 32 км (пометка в `quality.notes`).
- Официальные формы (Р-227): «Знак Древних» в наших текстах — «Знак Старших богов» (книжная форма — в `raw`, текстах
  раздаток и псевдонимах названий предметов).
- Выводы из текста (Р-41): «Кладовая» у комнаты 1 на плане = «Склад» текста; значок у комнаты 4 = санузел; медальон
  остаётся на теле Эбенезера; смирительные рубашки — для Джонсона; «Х.», «Д.», «Хк.» дневника = Хардинг, Дарлин, Хокинс.

## Не взято

- Портреты пациентов, Джонсона и других (с. 6–9, 23): папка `app/art/` не входит в мою часть — можно добавить
  `pipeline/art/add_images.py` при сведении.
- Доктора Хаген и Аллен (критики в материалах 3–4), жена Хокинса, муж миссис Рэндольф, внуки Биллингса, судья Эдмунд
  Годфри (личность 5 Дарлин), экспедиция Хантсфорда — упомянуты мимоходом, остаются текстом в раздатках, легендах и таблице.
- Личности Дарлин 2–8 — строки таблицы «Личности Дарлин», отдельных записей нет (нет статблоков).
- Тексты заклинаний приложения 1 (с. 29–30) как отдельные записи: все пять заклинаний есть в общем справочнике; фанатский
  текст не меняет их механику (у «Знака Старших богов» стоимость здесь «10 МОЩ, 1 час») — только источники и псевдонимы через
  предложения. Ссылки «здесь» на внешние страницы (о Баст, о Годфри, о правилах призыва) — гиперссылки PDF, без текста.
- Оформление (рамки страниц, заставка заголовка) — без данных.

## Кандидаты и вопросы

- Навык существа «Спрятаться в темноте 90%» — возможно, это `coc:skill:skulk-in-darkness` («Скрываться во тьме»);
  не связано без подтверждения. «Видеть в темноте 85%» у Джонсона — навык без механики, без записи (Р-126).
- Шуточные навыки пациентов («Смятение», «Кляузничество», «Громкие вопли», «Декламация (Йейтс)» и др.) — без записей
  справочника (Р-126).

## Предложения

`proposals-asylum.json` — 17 правок пяти общих заклинаний (`dread-curse-of-azathoth`, `shrivelling`,
`summon-bind-nightgaunt`, `elder-sign`, `blessing-of-bast`): 12 фанатских названий и альтернативных имён в `aliases`
и 5 источников `lechebnitsa-ru` в `sources` (без `corrections`). Пробный прогон `apply.py --dry-run` проходит.
