# «МТС Харьков-37» (mts-kharkov-37-ru) — сверка покрытия

Книга: «Машинно-тракторная станция Харьков-37» (Machine Tractor Station Kharkov-37, Miskatonic University Monograph
#0310), русское издание «[RU 7e]», 93 страницы PDF с текстовым слоем (все числа, таблицы и карты сверены по изображениям
страниц; распознавание tesseract не понадобилось). Оригинал — английский сценарий под 6-ю редакцию (паспорт владельца:
EN 6e, RU 7e): русское издание переведено на проценты 7-й редакции, но часть чисел Цвета и магнитов осталась в масштабе
6-й (запись `creature/tsvet-bolota`, errata). Система — «Зов Ктулху» 7e, `ruleset: "core"`, эпоха — март 1933 года
(`era: ["1930s"]`).

Страницы: номеров на страницах нет — печатная = физическая (offset 0). Физ. 1 — обложка, 93 — плакат без текста.

Префикс записей: `mts-kharkov-37-ru/`. Общий город — `coc:location:kharkov` (новый, `kb/locations/kharkov.json`);
места сценария — в «Окрестностях Харькова» (Р-209). Карты — `app/maps/kharkov-*.jpg` (7 штук).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка (Machine Tractor Station Kharkov-37, A Cthulhu scenario set in Stalin's USSR) | 1 | `scenario/mts-kharkov-37` (name.en, summary, sources) |
| Машинно-тракторная станция Харьков-37 (титул) | 2 | `scenario/mts-kharkov-37` |
| О МТС Харьков-37 | 2 | `scenario/mts-kharkov-37` (advice) |
| Философия сценария и вдохновение | 2–3 | `scenario/mts-kharkov-37` (summary, advice) |
| Предисловие | 3 | `scenario/mts-kharkov-37` (keeper_info); `organization/gruppa-ogpu-shilova`, `organization/gru-osobyy-otdel-8` |
| Примечание от автора (прочитать «Цвет из иных миров») | 3 | `scenario/mts-kharkov-37` (advice) |
| До начала | 3–4 | `scene/do-nachala` |
| Депо Красной Армии 945 | 4–5 | `scene/depo-945`; `location/depo-krasnoy-armii-945`; `character/mayor-presnenskiy`; `organization/garnizon-depo-945`; `item/gruzoviki-gaz-aa` |
| Вариант для Хранителя (дизентерия) | 4–5 | `scene/depo-945` (description, mechanics) |
| Примечание о советских воинских званиях | 6 | `scenario/mts-kharkov-37` (advice; таблица «Советские воинские звания») |
| Дорога до станции | 6–7 | `scene/doroga-do-stantsii`; `location/doroga-na-stantsiyu`, `location/bogorodsk`, `location/ulovka`, `location/degmatorsk` |
| Кролик | 7–8 | `scene/krolik`; `creature/krolik-mutant` |
| Машинно-тракторная станция Харьков 37 | 9 | `scene/pribytie-na-stantsiyu`; `location/mts-kharkov-37` |
| Карта станции (Machine Tractor Station Karkhov 37) | 10 | `map/karta-stantsii` (24 метки) |
| 1. Бараки | 10 | `location/mts-1-baraki`; `location/mts-sortiry` (флигель/сортир, знак «L») |
| 1А. Административное жилье | 11 | `location/mts-1a-administrativnoe-zhile` |
| 1Б. Телеграфная (сгорел) | 11 | `location/mts-1b-telegrafnaya`; `item/telegrafnyy-klyuch` |
| 1С. Лазарет (сгорел) | 11 | `location/mts-1c-lazaret` |
| 1D и 1Е. Корпус | 12 | `location/mts-1d-1e-korpusa` |
| 1F. Временная столовая | 12 | `location/mts-1f-vremennaya-stolovaya` |
| 1G. Тюрьма | 12 | `location/mts-1g-tyurma` |
| 2А. Сарай | 13 | `location/mts-2a-saray` |
| 2Б. Костер | 13 | `location/mts-2b-koster` |
| 3. Молочный завод | 14 | `location/mts-3-molochnyy-zavod` |
| 4. Гаражи | 14 | `location/mts-4-garazhi` |
| Garage Map (план гаража) | 15 | `map/plan-garazha` (5 меток) |
| 4А. Гараж А | 15 | `location/mts-4a-garazh-a`; `item/traktory-stantsii` |
| 4Б. Гараж Б | 15 | `location/mts-4b-garazh-b` |
| 4Б-1. Комната сержантов | 15–16 | `location/mts-4b-1-komnata-serzhantov`; `item/snaryazhenie-bukovicha`; `character/serzhant-bukovich` |
| 4Б-2. Квартиры лейтенантов | 16 | `location/mts-4b-2-kvartiry-leytenantov`; `item/metallicheskiy-yashchik-s-pasportami`, `item/otchet-mts-po-selskomu-khozyaystvu` |
| 4Б-3. Кварталы ученых | 16 | `location/mts-4b-3-kvartiry-uchenykh`; `item/tekst-po-khimii-s-zametkami` |
| 4Б-4. Сожженная лаборатория | 16–17 | `location/mts-4b-4-sozhzhennaya-laboratoriya`; `item/obryvki-laboratornykh-zapisey` |
| 4Б-5. Комната Шилова | 17 | `location/mts-4b-5-komnata-shilova` |
| 4С. Гараж С | 17 | `location/mts-4c-garazh-c`; `item/ruchnoy-nasos`, `item/gruzovik-ogpu` |
| 5. Зернохранилища | 18 | `location/mts-5-zernokhranilishcha` |
| 5А. Зернохранилище («Ленин») | 18 | `location/mts-5a-lenin`; `item/mutirovannoe-zerno`, `item/mutirovavshiy-kuznechik` |
| 5Б. Зернохранилище («Сталин») | 18–19 | `location/mts-5b-stalin`; `character/leytenant-gudzin` |
| 5С. Недостроенное зернохранилище | 19 | `location/mts-5c-nedostroennoe-zernokhranilishche` |
| 5Д. Сельский грузовик с электростанцией | 19 | `location/mts-5d-gruzovik-elektrostantsiya`; `item/elektrifikatsionnyy-gruzovik`, `item/sumka-chirikova`, `item/albom-chirikova`; `character/pavel-chirikov` |
| Колхозы (условные знаки r, b, штриховка; время в пути) | 20 | `scene/kolkhozy` |
| Карта окрестностей (Colour's Lair, The Crater…) | 20 | `map/karta-okrestnostey` (7 меток); `location/okrestnosti-kharkova` |
| Байленхов (время в пути 15 минут), карта | 21 | `location/baylenkhov`; `map/karta-baylenkhova` (10 меток) |
| 1. Православная Церковь | 22 | `location/baylenkhov-1-tserkov` |
| 1А. Кладбище | 22 | `location/baylenkhov-1a-kladbishche` |
| 2. «Община» | 22 | `location/baylenkhov-2-obshchina` |
| 2А. Деревенский Колодец | 22–23 | `location/baylenkhov-2a-kolodets` |
| 3. Цистерна | 23 | `location/baylenkhov-3-tsisterna` |
| 4. Амбары | 23 | `location/baylenkhov-4-ambary` |
| 4А. Пустая цистерна | 23 | `location/baylenkhov-4a-pustaya-tsisterna` |
| 4Б. Курятники и небольшой костер | 23 | `location/baylenkhov-4b-kuryatniki` |
| 5. Кузница | 23 | `location/baylenkhov-5-kuznitsa` |
| 6. Руины поместья | 23 | `location/baylenkhov-6-ruiny-pomestya` |
| Юренково (время в пути 30 минут), карта | 24 | `location/yurenkovo`; `map/karta-yurenkovo` (5 меток) |
| 1. Зал Павших Героев Революции | 25 | `location/yurenkovo-1-zal-pavshikh-geroev` |
| 2. Ветряная мельница и резервуар для воды | 25 | `location/yurenkovo-2-vetryanaya-melnitsa` |
| 3. Амбары | 25 | `location/yurenkovo-3-ambary` |
| 3А. Место бойни | 25 | `location/yurenkovo-3a-mesto-boyni` |
| 4. Братская могила | 25 | `location/yurenkovo-4-bratskaya-mogila` |
| Чеченка (время в пути 40 минут), карта | 26 | `location/chechenka`; `map/karta-chechenki` (7 меток) |
| 1. Восточная Православная Церковь | 27 | `location/chechenka-1-tserkov` |
| 2. Кладбище | 27 | `location/chechenka-2-kladbishche` |
| 3. Конюшня | 27 | `location/chechenka-3-konyushnya`; `creature/issokhshiy-poni` |
| 4. «Община» | 27 | `location/chechenka-4-obshchina` |
| 5. Колодец | 28 | `location/chechenka-5-kolodets` |
| 6. Кузница | 28 | `location/chechenka-6-kuznitsa` |
| 7. Беспокойный дом | 28 | `location/chechenka-7-bespokoynyy-dom`; `character/semya-vizhedikh` |
| Кратер | 29–30 | `scene/krater`; `location/krater` |
| Логово Цвета | 30–31 | `scene/poisk-logova-tsveta`; `location/logovo-tsveta` |
| Действия партии (вступление) | 31 | `scene/razbivka-lagerya` |
| Разбивка лагеря | 31 | `scene/razbivka-lagerya` |
| Вскрытие (правила; Кролик, Лейтенант Чириков, Пони, Сгоревшая туша, Сожженные трупы, Останки из логова, Останки животных, Другие останки) | 31–34 | `scene/vskrytiya` |
| Эксперименты (Мутировавшие насекомые, Мутированное зерно, Логово или кратерная вода, Логово) | 34–35 | `scene/eksperimenty`; `item/mutirovavshiy-kuznechik`, `item/mutirovannoe-zerno`, `item/veshchestvo-logova` |
| Чтение документов | 35 | `scene/chtenie-dokumentov` |
| Секретный журнал лейтенанта Чирикова; Вариант для Хранителя | 36 | `item/albom-chirikova` (mechanics) |
| Текст по химии с заметками; Вариант для жестоких Хранителей | 36–37 | `item/tekst-po-khimii-s-zametkami` |
| Отчет МТС-Х37 по сельскому хозяйству | 37 | `item/otchet-mts-po-selskomu-khozyaystvu` |
| Научные отчеты | 37 | `item/obryvki-laboratornykh-zapisey` |
| Другие занятия; Конструкция электромагнита | 37–38 | `scene/elektromagnit` |
| Починка телеграфных линий | 38–39 | `scene/pochinka-telegrafa` |
| Работа с войсками | 39–40 | `scene/rabota-s-voyskami`; `character/krasnoarmeytsy-depo-945`, `character/serzhant-blochintsev`, `character/serzhant-kovalevskiy` |
| Действия Цвета; День первый … День седьмой и далее | 40–43 | `scene/deystviya-tsveta` |
| Необязательная встреча: Обнаружена семья Вижедих | 41 | `scene/semya-vizhedikh`; `location/mesto-gibeli-semi-vizhedikh`; `character/semya-vizhedikh` |
| Атаки цвета | 43 | `scene/ataki-tsveta` |
| Взаимодействие с Цветом; Побег; Атака; Пленение; Защита | 44–46 | `scene/vzaimodeystvie-s-tsvetom` |
| Заключение | 46 | `scenario/mts-kharkov-37` (conclusion) |
| Заметки хранителя (Настроение, Игрок против игрока, Изменение сценария) | 46–47 | `scenario/mts-kharkov-37` (advice) |
| Цитата из «Цвета из иных миров» | 47 | не взято — см. ниже |
| О Цвете | 47–48 | `creature/tsvet-bolota` (legend) |
| Особые умения; Цвет из иных миров (таблица характеристик, атаки) | 48–49 | `creature/tsvet-bolota` (statblock, abilities) |
| Но что насчет… | 49 | `creature/tsvet-bolota` (legend) |
| Статистика: снаряжение (Пистолеты, Винтовки, Пулемёт) | 49–50 | `scenario/mts-kharkov-37` (advice); атаки персонажей; предложения `source_variants` |
| Гранаты | 50 | `item/butylochnye-granaty` |
| Транспортные средства: Грузовики Станции; Тракторы станции; Сельский электрификационный грузовик | 50–51 | `item/gruzoviki-gaz-aa`, `item/traktory-stantsii`, `item/elektrifikatsionnyy-gruzovik` |
| Красноармейцы: Отряд А, Отряд Б; Навыки сержантов, Навыки рядовых; Атаки | 52–53 | `character/krasnoarmeytsy-depo-945` (17 вариантов), `character/serzhant-blochintsev`, `character/serzhant-kovalevskiy` |
| Новый навык: Репутация в партии | 53–54 | `scenario/mts-kharkov-37` (advice); навык не заведён — см. ниже |
| Информация для Хранителя: что произошло на МТС-Х37 | 54–57 | `scenario/mts-kharkov-37` (keeper_info); персонажи группы ОГПУ |
| Допустимая дезинформация: Тунгусский метеорит | 57–58 | `scene/tungusskiy-meteorit`; `handout/tungusskiy-meteorit-1`, `handout/tungusskiy-meteorit-2` |
| Недопустимая дезинформация: Радиация | 58 | `scene/radiatsiya` |
| Раздаточные материалы (разделитель) | 59 | — (только заголовок) |
| Карта окрестностей МТС-Х37 для игроков | 60 | `map/karta-okrestnostey-dlya-igrokov` (5 меток) |
| Досье ГРУ на МТС-Х37 | 60–61 | `handout/dose-gru-na-mts-kh37` |
| Тунгусский метеорит. Сообщение первое / второе | 61–62 | `handout/tungusskiy-meteorit-1`, `handout/tungusskiy-meteorit-2` |
| Воспоминания о метеоре | 62 | `handout/vospominaniya-o-meteore` |
| Фрагменты лабораторных заметок | 62–63 | `handout/fragmenty-laboratornykh-zametok` |
| Производственные отчеты МТС-Х37 1929-32 гг. | 63 | `handout/proizvodstvennye-otchety-mts` |
| Альбом для рисования лейтенанта Чирикова (последняя запись) | 63–64 | `item/albom-chirikova`; `handout/poslednyaya-zapis-chirikova` |
| Дневник Чирикова, 8 ноября 1932 — 4 февраля 1933 | 65–75 | `handout/dnevnik-chirikova` |
| Листы персонажей | 75–76 | `scenario/mts-kharkov-37` (hook, sources) |
| Старший лейтенант Григорий Федоров, Красная Армия | 77–78 | `character/grigoriy-fedorov` |
| Старший сержант — доктор Виссарион (Бесо) Иванович Любимов | 79–80 | `character/vissarion-lyubimov` |
| Комиссар Петр Петрович Юшкевич | 81–82 | `character/petr-yushkevich` |
| Администратор — Майор Юрий Кополев, ТАСС | 83–84 | `character/yuriy-kopolev` |
| Лейтенант-Электрик Николай Дугов, ТАСС | 85–86 | `character/nikolay-dugov` |
| Капитан-Техник Александр Тропинов, ТАСС | 87–88 | `character/aleksandr-tropinov` |
| Дополнительная информация для Юрия Кополева | 89–90 | `character/yuriy-kopolev` (background.secret, legend, possessions «Тайно»); `organization/gru-osobyy-otdel-8` |
| Дополнительная информация для Николая Дугова | 91 | `character/nikolay-dugov` (background.secret, legend, possessions) |
| Дополнительная информация для Александра Тропинова | 92 | `character/aleksandr-tropinov` (background.secret, legend, possessions) |
| Плакат «Тов. Ленин очищает землю от нечисти» | 93 | не взято — см. ниже |

Персонажи, упомянутые в тексте и дневнике, — тоже записи: `character/nikolay-shilov`, `pavel-chirikov`,
`leytenant-gudzin`, `serzhant-bukovich`, `doktor-zelentsov`, `doktor-mezhlauk`, `valentin-pechenkin`, `dmitriy-limonov`,
`ostrogorskiy`, `mariytsev`, `burat-polden`, `semya-vizhedikh`.

## Не взято

- Иллюстрации и советские плакаты (с. 1, 2, 7, 9, 11, 13, 14, 20, 24, 27, 29–31, 36, 38, 40, 42, 44, 45, 47, 49–51, 54,
  55, 57, 59, 75, 93) — оформление без текста для игры; картинки в `images` не добавлялись.
- Цитата из «Цвета из иных миров» Лавкрафта (с. 47) — эпиграф к разделу о Цвете, без механики.
- «Официальные приказы» группы и статья Британской энциклопедии «Радиация» (1930) — книга их упоминает, но не печатает.
- Навык «Репутация в партии» (с. 53–54) — отдельной записи навыка не заведено (`kb/skills` — общий справочник): правило
  — в advice сценария, в листах — как «Средства (партийная репутация)» со ссылкой на `coc:skill:credit-rating`;
  черновик записи — в отчёте.
- Пулемёт «Туламаш-Максим М-1890» — записи в справочнике оружия нет; атаки без ссылки `weapon`, числа — в тексте.

## Опечатки и сомнения книги (в errata записей)

- Ершов: ПЗ 25 (ожидалось 15); Блочинцев: ПЗ 11 (ожидалось 10); Дзюбенко: Рассудок 47 (ожидалось 57); Кополев:
  Уклонение 35 ниже половины ЛВК 80.
- Цвет: стартовая МОЩ 75, но в первую ночь «текущий POW, равный 15»; пороги 20/25/40 и МОЩ магнитов 30–45 — в масштабе
  6-й редакции; абзац первой ночи напечатан дважды с разными правилами.
- «29 января 1993 г.» в дневнике; разное написание фамилий (Печенкин/Паченкин/Пенкин, Лимонов/Лиминов,
  Чириков/Чирков, Блочинцев/Блохинцев, Тропинов/Триепинов, «Любимова»), «доктор Елецкий» вместо Зеленцова;
  «Пямбироских»/«Симбирских»; время основания Байленхова; Шилов «и ещё трое» против «двое»; расход топлива генератора;
  потеря Рассудка за текст по химии (1/1d3 и 1/2); могилы 1931 года со следами Цвета; хронология урожая 1931 года;
  дата отправки группы ОГПУ; проверка ТЕЛ против дизентерии; примеры распределённого магнита.
- Карта станции штрихует гараж С, а по тексту горел гараж Б; знак «7» у бункера «Сталин» в ключе не объяснён.
