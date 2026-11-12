# «Ведомо ли любви прощение?» (vedomo-li-lyubvi-ru) — сверка покрытия

Книга: сборник Chaosium (2020; польский оригинал — Black Monk Games, 14 февраля 2020 года) из двух сценариев один на один
для «Зова Ктулху» 7-й редакции — «Люблю тебя до смерти» (Чикаго, 15 февраля 1929 года) и «Маска желания» (Нью-Йорк,
сентябрь 1932 года); официальный русский перевод, 61 страница PDF с текстовым слоем (метка владельца «[RU 7e]»). Текстовый
слой на с. 19, 22, 23, 42, 43 перемешан с английским текстом и колонками — эти страницы, все статблоки и все раздатки
сверены по изображениям страниц (рукописные и машинописные раздатки — по изображению с. 44–53, при помощи OCR и увеличения;
дневник с. 48 — по повёрнутому увеличенному фрагменту). Правила — ядро 7-й редакции (`ruleset: "core"`); эпоха: первый
сценарий — `1920s`, второй — `1930s` (книга в советах по созданию сыщика пишет «эпоха 1920-х», действие — 1932 год).
Карт в книге нет. Отдельный PDF «Раздаточный материал» (11 страниц) повторяет раздатки книги; источник — книга.

Страницы: печатная = физическая − 1 (физ. 5 — «4», физ. 23 — «22», физ. 44 — «43»); на обложке, титуле, странице авторов и
оглавлении (физ. 1–4) номеров нет. Ниже «с.» — печатные страницы.

Префикс записей: `vedomo-li-lyubvi-ru/` (ниже — `B/`). Город Чикаго — новый общий `coc:location:chicago` (в базе его не
было, другие части этого плана в Чикаго не играют). Нью-Йорк — общий `coc:location:new-york`: дополнения — в
`proposals-vedomo.json` (9 предложений, `apply.py --dry-run` проходит).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул | физ. 1–2 | `B/scenario/lyublyu-tebya-do-smerti` (sources); картинка — не взято |
| Авторы (английское и польское издание), благодарности, авторство | физ. 3 | `B/scenario/lyublyu-tebya-do-smerti`, `B/scenario/maska-zhelaniya` (summary, sources) |
| Оглавление; указатель оценки сценария (сложность, сессии) | физ. 4 | сложность (1 и 2 звезды) и число сессий — в summary сценариев |
| Введение | 4 | `B/scenario/lyublyu-tebya-do-smerti` (advice), `B/scenario/maska-zhelaniya` (advice) |
| Любовная история? | 4 | то же (advice) |
| Помощь знакомых | 5 | то же (advice) |
| Использование удачи | 5 | то же (advice); `coc:rule:spending-luck` в refs |
| Иллюстрация к «Люблю тебя до смерти» | физ. 7 | не взято — иллюстрация |
| Люблю тебя до смерти (вступление) | 7 | `B/scenario/lyublyu-tebya-do-smerti` (summary) |
| Информация для Хранителя | 7 | `B/scenario/lyublyu-tebya-do-smerti` (keeper_info) |
| Создание сыщика | 7 | `B/scenario/lyublyu-tebya-do-smerti` (advice) |
| Детство сыщика; Хранителю на заметку (×2) | 7 | `B/scenario/lyublyu-tebya-do-smerti` (advice) |
| Материал: Любовь 1 | 8, 45 | `B/handout/lyubov-1` |
| Материал: Любовь 2 | 9, 46 | `B/handout/lyubov-2` |
| Воспоминания (врезка) | 10 | `B/scenario/lyublyu-tebya-do-smerti` (advice) |
| Связи сыщика | 10 | `B/scenario/lyublyu-tebya-do-smerti` (advice); `B/handout/lyubov-3` |
| План Эллен | 10 | `B/scenario/lyublyu-tebya-do-smerti` (keeper_info); `B/character/ellen-osallivan`; `B/character/ivonn-lakur` |
| Материал: Любовь 3 | 10, 44 | `B/handout/lyubov-3` |
| Сеансы прорицания | 11 | `B/scenario/lyublyu-tebya-do-smerti` (keeper_info); `B/character/ellen-osallivan` |
| Подруга в беде | 11 | `B/scenario/lyublyu-tebya-do-smerti` (keeper_info); `B/character/lyusil-moran`; `B/item/serebryanyy-ankh`; `B/item/khandzhar` |
| Действующие лица: Хэтти Мэй, Хайбол | 11 | `B/character/khetti-mey`, `B/character/khaybol` |
| Действующие лица: Барт Чихарски, Билли «Зачесик» Брок, Люсиль Моран, Эллен О'Салливан | 12 | `B/character/bart-chikharski`, `B/character/billi-brok`, `B/character/lyusil-moran`, `B/character/ellen-osallivan`; `B/character/dzhordzh-moran` |
| Начало: Мольба о помощи | 12–13 | `B/scene/nachalo-molba-o-pomoshchi`; `B/item/shelkovyy-sharf-khetti`; `B/item/fotografiya-khetti-s-khaybolom`; `B/character/dzhon-mey` |
| Бойня в День Святого Валентина (Причины, Жертвы, Убийцы, Бойня) | 13 | `coc:location:chicago` (history); `B/location/garazh-na-nort-klark-strit`; `B/organization/banda-nort-sayd` |
| Тайна Хэтти | 13 | `B/scene/nachalo-molba-o-pomoshchi`; `B/character/khetti-mey` (background.secret) |
| Хранителю на заметку; Краткие факты | 14 | `B/scene/nachalo-molba-o-pomoshchi` |
| Полицейский участок; Освобождение Хайбола; Хранителю на заметку | 14 | `B/scene/politseyskiy-uchastok`; `B/location/politseyskiy-uchastok` |
| Материал: Любовь 5 | 14, 49 | `B/handout/lyubov-5` |
| Материал: Любовь 4 | 15, 47 | `B/handout/lyubov-4`; `B/location/bolnitsa-okruga-kuk` |
| Исчезновение Хэтти; Хранителю на заметку (загадки) | 16 | `B/scene/ischeznovenie-khetti`; `B/location/kvartira-khetti`; `B/location/dom-na-uest-belmont-avenyu`; `B/item/khandzhar` |
| Эхо | 16–17 | `B/scene/ischeznovenie-khetti`; `B/handout/lyubov-7` |
| Материал: Любовь 6 | 16, 49 | `B/handout/lyubov-6` |
| Соседи (мистер Броуди, миссис Масслер); Хранителю на заметку (слежка Эллен) | 17 | `B/scene/ischeznovenie-khetti`; `B/character/mister-broudi`; `B/character/missis-massler` |
| Что дальше? | 17 | `B/scene/ischeznovenie-khetti` |
| Закусочная «У Дороти» | 17 | `B/scene/zakusochnaya-u-doroti`; `B/location/zakusochnaya-u-doroti`; `B/location/otel-parkvey` |
| Встреча с Люсиль Моран | 17, 19 | `B/scene/vstrecha-s-lyusil-moran` |
| Материал: Любовь 7 | 18, 48 | `B/handout/lyubov-7` |
| Дополнительные осложнения (врезка) | 19 | `B/scene/dopolnitelnye-oslozhneniya`; `B/character/bernadet-fuks` |
| Амулет (врезка) | 19 | `B/item/serebryanyy-ankh` (mechanics) |
| Последнее колдовское собрание | 19–21 | `B/scene/poslednee-koldovskoe-sobranie`; `B/location/vodonapornaya-bashnya`; `B/location/dom-na-michigan-avenyu`; `B/location/kvartira-ellen`; `B/character/artur-dzhenni`; `B/character/ralf-sallivan` |
| Хэтти и амулет; Разобраться с Эллен | 21 | `B/scene/poslednee-koldovskoe-sobranie` |
| Долго и несчастливо | 21–22 | `B/scene/dolgo-i-neschastlivo` |
| Итоги | 22 | `B/scenario/lyublyu-tebya-do-smerti` (conclusion) |
| Персонажи и чудовища: Хэтти Мэй, Барт Чихарски, Билли Брок, Хайбол | 22–23 | статблоки в `B/character/khetti-mey`, `bart-chikharski`, `billi-brok`, `khaybol` |
| Бернадет «Берни» Фукс, Люсиль Моран, Эллен О'Салливан | 23 | статблоки в `B/character/bernadet-fuks`, `lyusil-moran`, `ellen-osallivan` |
| Прорицание (заклинание) | 23 | общий `coc:spell:augury-folk` (псевдоним «Прорицание» уже есть); источник — в предложениях |
| Мысленное внушение (заклинание) | 23 | общий `coc:spell:mental-suggestion`; источник — в предложениях |
| Иллюстрация к «Маске желания» | физ. 25 | не взято — иллюстрация |
| Маска желания (вступление) | 25 | `B/scenario/maska-zhelaniya` (summary) |
| Информация для Хранителя; Создание сыщика; Хранителю на заметку | 25–26 | `B/scenario/maska-zhelaniya` (keeper_info, advice) |
| Несколько интересных фактов о масках (врезка) | 26 | `B/scenario/maska-zhelaniya` — таблица «Несколько интересных фактов о масках» |
| Маска желания (раздел) | 26, 28 | `B/scenario/maska-zhelaniya` (keeper_info); `B/organization/tokko` |
| Материал: Маска 1 | 27, 50 | `B/handout/maska-1` |
| Как работает Маска Желания | 28 | `B/item/maska-zhelaniya` (mechanics) |
| Действующие лица: Анна Конрад | 28–29 | `B/character/anna-konrad` |
| Лукас Рестон, Мадам Пантея де Тиссон, Профессор Кирилл Ниенарт | 29–30 | `B/character/lukas-reston`, `B/character/panteya-de-tisson`, `B/character/kirill-nienart` |
| Танака Кэндзабуро, Эмили Вебстер | 30 | `B/character/tanaka-kendzaburo`, `B/character/emili-vebster` |
| Маньчжурия и маска (врезка) | 30 | `B/scenario/maska-zhelaniya` (keeper_info); `B/item/maska-zhelaniya`; `B/organization/tokko` |
| Начало: Вечеринка; Хранителю на заметку (×2) | 30–31 | `B/scene/nachalo-vecherinka`; `B/location/otel-ansoniya`; `B/location/apartamenty-de-tisson` |
| Безумец с ножом; Хранителю на заметку (×2) | 31–32 | `B/scene/bezumets-s-nozhom`; `B/character/bezumets-s-nozhom`; `B/item/nozh-bezumtsa` |
| Неожиданная посылка; Хранителю на заметку | 33 | `B/scene/neozhidannaya-posylka`; `B/location/osobnyak-restonov`; `B/character/missis-lenoks`; `B/character/brodyaga-chelovek-tanaki`; `B/item/derevyannaya-korobka` |
| Материал: Маска 2 | 33, 51 | `B/handout/maska-2` |
| Если сыщик преуспел в проверке Удачи; Если сыщик провалил проверку Удачи | 33–34 | `B/scene/neozhidannaya-posylka` |
| Материал: Маска 3, 4, 5 | 34, 51–52 | `B/handout/maska-3`, `maska-4`, `maska-5` |
| Сыщик ждёт, пока Лукас вернётся, чтобы вскрыть посылку | 35 | `B/scene/neozhidannaya-posylka` |
| Возвращение Анны; Хранителю на заметку (×2) | 35 | `B/scene/vozvrashchenie-anny` |
| Разговор с профессором Ниенартом; Хранителю на заметку | 36 | `B/scene/razgovor-s-professorom-nienartom` |
| Разговор с де Тиссон | 36, 38 | `B/scene/razgovor-s-de-tisson` |
| Материал: Маска 6, 7 | 37, 53 | `B/handout/maska-6`, `maska-7` |
| Материал: Маска 8 | 38, 52 | `B/handout/maska-8` |
| Вовлечение Токко (врезка) | 38 | `B/scene/vovlechenie-tokko` |
| Хранителю на заметку (бой у де Тиссон) | 38 | `B/scene/razgovor-s-de-tisson` |
| Убийство; Хранителю на заметку | 38–39 | `B/scene/ubiystvo` |
| Другие варианты: Последний вздох мадам де Тиссон; Противостояние с людьми Танаки | 39 | `B/scene/ubiystvo` |
| Прибытие Лукаса; Возвращение безумца; Полиция | 39–40 | `B/scene/ubiystvo` |
| Итоги: прослушивание | 40 | `B/scene/itogi-proslushivanie`; `B/location/otel-pensilvaniya`; `B/location/manhattanskiy-zal`; `B/character/nensi-terner` |
| Если Лукас наденет маску (перед прослушиванием / после прослушивания); Хранителю на заметку | 40–41 | `B/scene/esli-lukas-nadenet-masku` |
| Если Анна наденет маску; Если Лукас предложит Анне надеть маску; Перехват маски | 41 | `B/scene/esli-anna-nadenet-masku` |
| Прослушивание Анны с надетой маской; без маски | 42 | `B/scene/esli-anna-nadenet-masku` |
| Похищение!; Хранителю на заметку (pulp) | 41–42 | `B/scene/pokhishchenie` |
| Прочие возможности | 42 | `B/scene/pokhishchenie`; `B/scenario/maska-zhelaniya` (conclusion) |
| Персонажи и чудовища: Анна Конрад, Лукас Рестон | 42 | статблоки в `B/character/anna-konrad`, `lukas-reston` |
| Эмили Вебстер, Мадам Пантея де Тиссон, Профессор Кирилл Ниенарт | 43 | статблоки в `B/character/emili-vebster`, `panteya-de-tisson`, `kirill-nienart` |
| Сбитый с толку и растрёпанный человек с ножом | 43 | `B/character/bezumets-s-nozhom` (имя придумано, Р-150) |
| Танака Кэндзабуро; Японские телохранители (2) | 43 | `B/character/tanaka-kendzaburo`; `B/character/yaponskie-telokhraniteli` (групповой профиль, names) |
| Раздаточный материал | 44–53 | 15 записей `B/handout/lyubov-1…7`, `B/handout/maska-1…8` (второй источник каждой) |
| Алфавитный указатель | 54–55 | — (навигация) |
| Биографии авторов | 56–57 | не взято — сведения об авторах, не игровой материал |
| Лист сыщика 1920-х (2 стр.) | физ. 59–60 | не взято — пустой бланк |
| Задняя обложка (аннотация) | физ. 61 | `B/scenario/*` (summary); картинка — не взято |

## Записи (87)

- сценарии 2: `B/scenario/lyublyu-tebya-do-smerti` (order 1), `B/scenario/maska-zhelaniya` (order 2; таблица «Несколько
  интересных фактов о масках»);
- сцены 20: «Люблю тебя до смерти» — `nachalo-molba-o-pomoshchi`, `politseyskiy-uchastok`, `dopolnitelnye-oslozhneniya`,
  `ischeznovenie-khetti`, `zakusochnaya-u-doroti`, `vstrecha-s-lyusil-moran`, `poslednee-koldovskoe-sobranie`,
  `dolgo-i-neschastlivo`; «Маска желания» — `nachalo-vecherinka`, `bezumets-s-nozhom`, `neozhidannaya-posylka`,
  `vozvrashchenie-anny`, `razgovor-s-professorom-nienartom`, `razgovor-s-de-tisson`, `vovlechenie-tokko`, `ubiystvo`,
  `itogi-proslushivanie`, `esli-lukas-nadenet-masku`, `esli-anna-nadenet-masku`, `pokhishchenie`;
- персонажи 25 (16 статблоков: 7 в первом сценарии, включая пса Хайбола, 9 во втором, включая групповой профиль
  телохранителей); готовых сыщиков в книге нет;
- раздатки 15; предметы 7 (анх, ханджар, шарф, фотография; Маска Желания, коробка, нож безумца); места 15;
  организации 2 (банда Норт-Сайд, Токко);
- общий город `kb/locations/chicago.json` (новый).

## Не взято

- Иллюстрации (обложка, физ. 7, физ. 25, задняя обложка) и картинки раздаток (с. 44–53; для «Материала: Любовь 7» —
  рисунок собаки в дневнике): папка `app/art/` вне этой части; при желании ведущий добавит их через
  `pipeline/art/add_images.py` (раздатки — физ. 45–54 книги или отдельный PDF «Раздаточный материал»).
- Биографии авторов, алфавитный указатель, пустой лист сыщика, оглавление — не игровой материал.
- Эпизодические лица без своих записей (описаны в сценах и раздатках): курьер с посылкой; гость, раненный безумцем;
  отец Лукаса (владелец юридической фирмы и особняка); сын Люсиль Джон Джордж Моран; Ирэн из дневника Хэтти; Фрэнк
  Гузенберг (раздатка 4 и история Чикаго); Аль Капоне и прочие жертвы и подозреваемые бойни (история Чикаго, раздатка 5);
  коллега Ниенарта по японскому языку; жена и трое детей Ниенарта; оркестранты Нэнси Тернер; Бенни Гудман (упоминание).
- Мелкие вещи без механики: ритуальный нож Эллен, выцветшая фотография троих детей, пальто и шапка Хэтти, обёрточная
  бумага посылки, записки Анны и Лукаса — текстом в сценах.
- Фолианты Ивонн Лакур («оккультные фолианты») — книга не называет ни одного, записи книги Мифов нет.
- Награды Рассудка за исход — в книге не напечатаны (отмечено в conclusion обоих сценариев).
- Карт в книге нет; новых заклинаний нет (все четыре заклинания Эллен и «Мысленное внушение» де Тиссон — в общем справочнике).

## Сомнения и вопросы

- «Револьвер Кольт .35» у Барта Чихарски (урон 1d10+2, с. 22): такого оружия в таблице нет, урон — как у револьвера .45;
  оставлено как напечатано, `errata`, ссылки на оружие нет.
- Эллен: Уклонение 25% ниже половины ЛВК (27) и Скорость 7 при ЛВК = ТЕЛ (по `tools/derived.py` — 8) — `errata`, как
  напечатано. Хайбол: Скорость 12 — не опечатка (собака), но записана в `errata`, чтобы проверка производных не ругалась;
  если такой приём нежелателен — вопрос владельцу.
- Ссылка внутри текста «Последней колдовской встречи» (стр. 20) — раздел называется «Последнее колдовское собрание», с. 19
  (`errata` сценария).
- Берни Фукс: в статблоке «Телосложение: 1» вместо «Комплекция» — взято как Комплекция (пометка в quality).
- Танто телохранителей (1d4+1+1d4) — в справочнике оружия нет, ссылки нет; «Пистолет Намбу» связан с
  `coc:weapon:8mm-automatic`.
- Родной язык: у Ниенарта принят польский (родился во Львове, 90%) — вывод; у японцев — японский; у остальных — английский.
- Отель «Пенсильвания» поставлен прямо под Нью-Йорк (`part_of: coc:location:new-york`), хотя Седьмая авеню, 401 — Мидтаун;
  книга район не называет. «Ансония» и особняк Рестонов — тоже прямо под городом (записи района Верхний Вест-Сайд нет).
- Место разговора с Ниенартом книга не называет; в сцене стоит `coc:location:columbia-university` с пометкой «вывод из
  текста (Р-41)».
- Придуманные имена (Р-150, Р-151): безумец с ножом — «Уолтер Брэдшоу», человек Танаки в облике бродяги — «Сэм Гэррити»,
  пять имён в `names` японских телохранителей.
- Отдельный PDF «Раздаточный материал» в папке библиотеки не зарегистрирован в `books.json`; он повторяет с. 44–53 книги.
  Папку владельца в `3_КБ\Ваншоты` не смотрел — всё взято из книги.
