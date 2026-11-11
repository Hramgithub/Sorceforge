# «Секретный код» («Особняки безумия. За закрытыми дверями», `osobnyaki-bezumiya-ru`) — сверка переноса (часть code)

Источник — официальное русское издание (Hobby World), скан без текстового слоя: распознанный текст
`.cache/ocr/osobnyaki-bezumiya-ru/NNN.txt` (tesseract -l rus, 200 dpi); каждое число, имя и статблок сверены по изображению
страницы (`pages.py image`). Рукописные раздатки («Код 1», «Код 3»–«Код 5») распознаванием не читаются — переписаны по
изображениям страниц 196–206. Английского текста 7e нет (книга `[EN 6e] Mansions of Madness` в папке — 6e, этого сценария
в ней нет), поэтому `name.en` заполнено только у города Хэмптон (реальный городок Hampton, округ Вашингтон, штат Нью-Йорк).

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 3 «Секретный код» | 69–102 (иллюстрация «Костюм времени» — с. 68) | 70–103 |
| Раздатки в главе: «Код 1», «Код 2» | 75 | 76 |
| Раздатки в главе: «Код 3» (2 с.), «Код 4» (4 с.), «Код 5» (4 с.) | 84–93 | 85–94 |
| «Материалы для игроков»: «Код 1»–«Код 5», карты поместья и дома | 196–208 | 197–209 |

Смещение: **печатная = физическая − 1** на всех проверенных страницах (69, 72, 74, 76, 98–100, 196–208).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 3. Секретный код («В которой сыщиков приглашают на очень необычную вечеринку»), вступление | 69 | сценарий `…/scenario/code-secret-code` (summary, aliases) |
| Информация для Хранителя | 69–70 | сценарий: keeper_info; `…/character/code-eva-pierce`, `code-clint-davis`, `code-kenneth-connolly` (legend) |
| Вовлечение сыщиков | 70 | сценарий: hook; сцена `…/scene/code-meeting-connolly`; `code-seamus-quinn`, `code-diana-carlson` (как сыщики) |
| Хранителю на заметку: знакомство с Коннолли | 70 | сцена `…/scene/code-meeting-connolly`; сценарий: advice |
| Действующие лица | 70–71 | сценарий: advice |
| • Ева Пирс, 33 года, мошенница и чародейка | 71 | `…/character/code-eva-pierce` |
| • Клинт Дэвис, 36 лет, мошенник | 71–72 | `…/character/code-clint-davis` |
| • Доктор Шеймас Куинн, 57 лет, профессор физики | 72 | `…/character/code-seamus-quinn` |
| • Диана Карлсон, 28 лет, учительница физики | 72 | `…/character/code-diana-carlson` |
| • Доктор Кеннет Коннолли, 54 года, начинающий путешественник во времени | 73 | `…/character/code-kenneth-connolly` |
| Завязка: письмо | 73–74 | сцена `…/scene/code-letter`; раздатки `code-1-connolly-letter`, `code-2-telegram` |
| Хэмптон (с «Хранителю на заметку») | 74 | сцена `…/scene/code-hampton`; город `coc:location:hampton` (новый общий); `…/location/code-saunders-store`; `…/character/code-clem-saunders` |
| Хранителю на заметку: самый обычный день | 74 | сцена `…/scene/code-ordinary-day` |
| Материал «Код 1», материал «Код 2» (в главе) | 75 | `…/handout/code-1-connolly-letter`, `…/handout/code-2-telegram` |
| Поместье Веллингтон (с «Хранителю на заметку»: план мошенников) | 76–77 | сцена `…/scene/code-wellington-estate`; места `code-wellington-estate`, `code-1-house`, `code-house-4-parlor` |
| Карта «Поместье Веллингтон: дом и его окрестности» (ключ 1–5) | 76 | карта `…/map/code-map-estate` (`app/maps/mansions-code-estate.jpg`, 10 меток); места `code-1-house`, `code-2-truck`, `code-3-cars`, `code-4-old-stable`, `code-5-fire-pit` |
| Лжец, лжец (врезка) | 77 | сцена `code-wellington-estate` (полный текст); сценарий: advice; `code-eva-pierce` |
| В библиотеку; Рабочий стол | 77–78 | сцена `…/scene/code-to-the-library`; место `code-house-11-library`; предметы `code-time-suit`, `code-workbench-notes`, `code-code-keypad` |
| Костюм времени (врезка) | 78 | предмет `…/item/code-time-suit` (описание и механика) |
| Осмотр особняка (с «Хранителю на заметку») | 78–79 | сцена `…/scene/code-searching-mansion`; предмет `code-light-sources` |
| Хроноаномалии | 79 | сцена `…/scene/code-chrono-anomalies`; таблица сценария «Хроноаномалии» |
| • Движущийся силуэт | 79 | сцена `…/scene/code-moving-silhouette` |
| • То же место, другое время | 79 | сцена `…/scene/code-same-place-other-time` |
| • Стая волков (с «Хранителю на заметку») | 79, 81 | сцена `…/scene/code-wolf-pack`; существо `…/creature/code-wolves` |
| • Кто здесь? | 81 | сцена `…/scene/code-who-is-there` |
| • Безумец | 81 | сцена `…/scene/code-madman`; `code-clint-davis` |
| • Гости | 81 | сцена `…/scene/code-visitors`; существо `…/creature/code-tchalliks` |
| • Помощь из прошлого (с двумя «Хранителю на заметку») | 81–82 | сцена `…/scene/code-help-from-the-past`; места `code-house-13-master-bedroom`, `code-house-14-blue-bedroom`; раздатки `code-3/4/5-connolly-diary` |
| Путешествия во времени (врезка) | 79 | сцена `code-chrono-anomalies` (полный текст); сценарий: advice |
| Карта «Поместье Веллингтон: план дома» (ключ 1–16, чердак) | 80 | карта `…/map/code-map-house` (`app/maps/mansions-code-house.jpg`, 33 метки); места `code-house-1-…` … `code-house-16-lounge`, `code-house-attic` |
| Дом и его окрестности | 82 | место `code-1-house` (описание); шаг сценария «Дом и его окрестности» |
| Первый этаж: Вестибюль (1), Гардеробная (2), Комната слуг (3), Гостиная (4), Комната слуг (5), Прачечная (6), Лестница для слуг (7), Столовая (8), Комната для завтрака (9) | 82 | места `code-house-1-vestibule`, `-2-cloakroom`, `-3-servants-room-william`, `-4-parlor`, `-5-servants-room`, `-6-laundry`, `-7-servants-stairs`, `-8-dining-room`, `-9-breakfast-room` |
| Кухня (10), Библиотека (11) | 83 | места `code-house-10-kitchen`, `code-house-11-library`; предмет `code-library-painting` |
| Второй и третий этажи: Остальные спальни (12, 14) | 83, 94 | места `code-house-12-bedrooms`, `code-house-14-blue-bedroom` |
| Дневник Коннолли (врезка) | 83 | книга `…/tome/code-connolly-diary` |
| Материал «Код 3», стр. 1–2 (в главе) | 84–85 | `…/handout/code-3-connolly-diary` |
| Материал «Код 4», стр. 1–4 (в главе) | 86–89 | `…/handout/code-4-connolly-diary` |
| Материал «Код 5», стр. 1–4 (в главе) | 90–93 | `…/handout/code-5-connolly-diary` |
| Хозяйская спальня (13) | 94 | место `code-house-13-master-bedroom` |
| Ванные (15) | 94 | место `code-house-15-bathrooms`; предмет `code-hair-dye-drops` |
| Чердак | 94 | место `code-house-attic`; предмет `code-code-keypad`; существо `code-fractal-chrono-entities` (житель) |
| Вокруг дома: Старая конюшня (4) | 94 | место `code-4-old-stable`; предметы `code-eva-suitcase`, `code-light-sources` |
| Костровище (5) | 94 | место `code-5-fire-pit`; предмет `code-burnt-clothes` |
| Тело Коннолли (не отмечено) | 94 | место `…/location/code-connolly-grave` (в «Окрестностях Хэмптона») |
| Отъезд из поместья | 94, 96 | сцена `…/scene/code-leaving-estate`; предмет `code-car-parts`; места `code-2-truck`, `code-3-cars` |
| Книга заклинаний Евы (врезка): «Отражение урона», «Призыв/укрощение фрактальной хроносущности» | 95 | книга `…/tome/code-eva-spellbook` (оба заклинания полным текстом в описании); `coc:spell:deflect-harm` — предложение псевдонима; новое заклинание — черновик в отчёте |
| Зачистка | 96 | сцена `…/scene/code-cleanup` |
| Завершение (варианты аномалий, два «Хранителю на заметку») | 96–97 | сцена `…/scene/code-ending`; таблица сценария «Ещё варианты аномалий в финале»; сценарий: conclusion |
| Награды | 97 | сценарий: conclusion (восемь наград и штрафов Рассудка) |
| Как продлить этот ужас | 97–98 | сценарий: conclusion; ссылки `coc:creature:hound-of-tindalos`, `coc:creature:yog-sothoth-tawil-atumr`, `coc:location:miskatonic-university` |
| Персонажи и чудовища; Персонажи Хранителя | 98–99 | статблоки `code-eva-pierce`, `code-clint-davis`, `code-seamus-quinn`, `code-diana-carlson`, `code-kenneth-connolly` |
| Существа и чудовища: Волки | 99 | `…/creature/code-wolves` (`instance_of` `coc:creature:wolf`) |
| Тчалликсы, будущие обитатели Земли; Пример тчалликса | 99 | `…/creature/code-tchalliks` (новый вид, только в этой книге) |
| Фрактальные хроносущности, разумы вне пространства и времени; Пример фрактальной хроносущности | 99–100 | `…/creature/code-fractal-chrono-entities` (новый вид, только в этой книге) |
| Материалы для игроков: «Код 1», «Код 2» | 196 | раздатки `code-1-connolly-letter`, `code-2-telegram` (источник текста) |
| «Код 3», стр. 1–2 | 197–198 | `code-3-connolly-diary` |
| «Код 4», стр. 1–4 | 199–202 | `code-4-connolly-diary` |
| «Код 5», стр. 1–4 | 203–206 | `code-5-connolly-diary` |
| Поместье Веллингтон — материал для игроков (карта окрестностей) | 207 | карта `code-map-estate` (картинка — с этой страницы, повёрнута) |
| План дома (материал для игроков) | 208 | карта `code-map-house` (картинка — с этой страницы) |

`…/` = `osobnyaki-bezumiya-ru/`. Город — общая запись `kb/locations/hampton.json` (новая, Р-190, Р-218); места сценария —
записи книги с `part_of` на город (магазин) и на область «Окрестности Хэмптона» (`code-hampton-environs`, Р-209):
поместье → дом → комнаты.

## Записи (73)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `code-secret-code` (13 шагов, 2 таблицы, награды) |
| scene | 18 | `code-meeting-connolly`, `-letter`, `-ordinary-day`, `-hampton`, `-wellington-estate`, `-to-the-library`, `-searching-mansion`, `-chrono-anomalies`, `-moving-silhouette`, `-same-place-other-time`, `-wolf-pack`, `-who-is-there`, `-madman`, `-visitors`, `-help-from-the-past`, `-leaving-estate`, `-cleanup`, `-ending` |
| location | 27 | общий город `coc:location:hampton`; книги: `code-hampton-environs`, `-saunders-store`, `-wellington-estate`, `-1-house`, `-2-truck`, `-3-cars`, `-4-old-stable`, `-5-fire-pit`, `-connolly-grave`, `-house-1-vestibule` … `-house-16-lounge`, `-house-attic` |
| map | 2 | `code-map-estate`, `code-map-house` |
| character | 6 | `code-eva-pierce`, `-clint-davis`, `-seamus-quinn`, `-diana-carlson`, `-kenneth-connolly` (все со статблоками), `-clem-saunders` |
| creature | 3 | `code-wolves`, `code-tchalliks`, `code-fractal-chrono-entities` |
| item | 9 | `code-time-suit`, `-code-keypad`, `-workbench-notes`, `-eva-suitcase`, `-burnt-clothes`, `-hair-dye-drops`, `-car-parts`, `-library-painting`, `-light-sources` |
| handout | 5 | `code-1-connolly-letter`, `-2-telegram`, `-3-connolly-diary`, `-4-connolly-diary`, `-5-connolly-diary` |
| tome | 2 | `code-connolly-diary`, `code-eva-spellbook` |
| organization | 0 | организаций нет (секта, в которой состояла Пирс, — без имени, текстом в её биографии) |

Готовые сыщики сборника — существующие записи `za-zakrytymi-dveryami-ru/character/*` (6), в ссылках сценария.

## Опечатки и расхождения

- С. 76, «Хранителю на заметку»: «а **Прайс** — за Клэр Уайтли» вместо «Пирс» — `errata` у `code-eva-pierce`.
- Диана Карлсон: ПМ 13 при МОЩ 70 (по правилам 14) — `errata`, как напечатано. Возраст — 28 (с. 72 и 98; распознавание давало «25»).
- Тчалликс: ПЗ 17 при ВЫН 65 и ТЕЛ 85 (по правилам 15), «среднее здоровье 16–17» не сходится со средними — `errata`.
- Могила Коннолли: «в паре километров от дома» (с. 70) и «примерно в полутора километрах от поместья» (с. 94) — `errata` у места.
- Дневник: в «Коде 5» важный прорыв датирован 25 июля, в «Коде 4» — 29 июля; Дэвид — «кузен» (так задумано: изменённое прошлое) — пометка у раздатки.
- Нож Евы Пирс — урон 1d6 (в таблице оружия ножа с таким уроном нет) — ссылка на оружие не ставилась, пометка у атаки.
- «Материал «Код 5» на стр. 93» (с. 81) — материал в главе занимает с. 90–93; не опечатка, указана последняя страница.

## Не взято

- Иллюстрации: с. 68 (костюм времени, «На предыдущей странице: костюм времени»), портреты на с. 71–73 (Ева Пирс, Клинт Дэвис,
  Шеймас Куинн, Диана Карлсон, Кеннет Коннолли), с. 83 («Спрятанный дневник»), с. 100–101 («Фрактальная красота»), с. 102
  (полностраничная иллюстрация без подписи: фокусник на сцене — по сюжету, вероятно, относится к следующей главе «Дом Мемфиса»):
  картинки в записи не добавлялись (поле `images` необязательно; можно добавить позже `pipeline/art/add_images.py`).
- Почтовое отделение Хэмптона, Чикагский университет, Гарвардский университет, школа для девочек в Массачусетсе, жених Карлсон
  Роберт Льюис, отец Дэвиса, лидер секты, декан Мискатоника, «Пирс из будущего», динозавр — упомянуты мимоходом: остались текстом
  в описаниях города, персонажей и сцен, отдельных записей нет.
- «Более опасная гончая» со с. 178 этого сборника (глава «Девятнадцатая лунка», часть hole) — текстом в «Как продлить этот ужас»,
  ссылка не ставилась (запись — в чужой части).
- Подписи этажей и «Вверх»/«Вниз» у главной лестницы на плане дома — без меток (не места).
- Заклинание «Призыв/укрощение фрактальной хроносущности» — в справочнике нет; полный текст сохранён в книге заклинаний Евы,
  черновик записи `kb/spells` — в отчёте части (справочник общий).

## Предложения

`proposals-code.json` — 5 предложений: `coc:spell:deflect-harm` — псевдоним «Отражение урона» и источник книги (с. 95);
`coc:spell:contact-yog-sothoth` — псевдонимы «Связь с Повелителем Времени», «Связь с Йог-Сототом»;
`coc:location:miskatonic-university` и `coc:location:arkham` — ссылка на сценарий. Пробный прогон
`pipeline/integrate/apply.py --dry-run`: 5 правок ложатся.
