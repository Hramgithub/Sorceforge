# «Мертвецкий стомп» (Стартовый набор, `starter-dead-mans-stomp-ru`) — сверка переноса (часть stomp)

Источник — официальное русское издание Стартового набора (Hobby World), отдельный PDF сценария без текстового слоя (скан).
Страницы распознаны `pdftoppm -r 200` + `tesseract -l rus`; каждое число статблоков и проверок сверено по изображению
страницы (вырезки 200 dpi). Официальные раздатки — папка владельца `Стартовый набор (Starter Set)\Мертвецкий Стомп\`
(`стомп_1…7.jpg`) и «официальная базовая раздатка» (с. 10, 11, 13–16).

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Иллюстрация на развороте («Музыка мёртвых», без номера) | 50 | 1 |
| Сценарий третий «Мертвецкий стомп» | 51–72 | 2–23 |
| Карта Гарлема (на всю страницу, без номера) | 61 | 12 |
| «Мертвецкий стомп: персонажи и монстры» | 73–77 | 24–28 |

Смещение: **печатная = физическая + 49** (проверено: 2→51, 3→52, 8→57, 13→62, 24→73, 28→77). В `pipeline/source/books.json`
у `starter-dead-mans-stomp-ru` смещение не записано — предлагается `"offset": 49` (правка общего файла — ведущему).

## Заголовки книги

`…/` = `starter-dead-mans-stomp-ru/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Сценарий третий: Мертвецкий стомп (эпиграф, «Для 2–5 сыщиков…») | 51 | сценарий `…/scenario/dead-mans-stomp` (summary, aliases) |
| Расы и расизм в США 1920-х годов (врезка) | 51 | сценарий: advice (полностью, с пунктами законов Джима Кроу) |
| Подготовка к игре | 51–52 | сценарий: advice («Подготовка к игре», «Музыка») |
| Как вовлечь сыщиков | 52 | сценарий: hook (с тремя ролями профессора); `…/character/cornell-professor` |
| Информация для Хранителя: предыстория | 53 | сценарий: keeper_info; `…/character/leroy-turner`, `…/item/turner-trumpet`, `…/organization/bonato-gang` |
| Ньярлатхотеп (врезка, «Печать Ньярлатхотепа») | 53 | сценарий: keeper_info; ссылка `coc:creature:nyarlathotep` |
| Гарлем (врезка, примечательные места) | 53 | сценарий: keeper_info; предложение абзаца району `masks-of-nyarlathotep-en/location/america-harlem`; `…/location/lenox-avenue-subway` |
| Начало: рай на земле | 54 | сцена `…/scene/smalls-paradise-start`; место `…/location/smalls-paradise` |
| Эд Смоллс и клубная жизнь (врезка) | 54 | `…/character/ed-smalls`; описание `smalls-paradise` |
| Хранителю на заметку (другие клубы Гарлема) | 54 | описание `smalls-paradise`; предложение району Гарлем |
| К делу | 54–55 | сцена `smalls-paradise-start` |
| План «Смоллс Парадайз» (ключ 1–16) | 55 | карта `…/map/smalls-paradise` (`app/maps/starter-stomp-smalls-paradise.jpg`, 16 меток); места `…/location/smalls-paradise-1-bar` … `-16-service-entrance`; раздатка `…/handout/smalls-paradise-plan` |
| Случайная неучтивость | 55–56 | сцена `…/scene/accidental-rudeness` |
| Прибытие гостя | 56–57 | сцена `…/scene/guest-arrives`; `…/item/grey-packard`; `…/character/joey-larson`, `jimmy-foster` |
| Поступь мертвеца | 57 | сцена `…/scene/dead-mans-gait`; `…/character/pete-manusco` |
| Добрые самаритяне | 58 | сцена `…/scene/good-samaritans` |
| Вариант: федеральный агент | 58 | сцена `good-samaritans`; `…/character/roger-daniels` (legend) |
| Материал «Стомп 1» | 58 | `…/handout/stomp-1-business-card` |
| Вечерние расследования; Важная зацепка | 58 | сцена `…/scene/evening-investigations` |
| Оставшись в «Смоллс Парадайз» | 59 | сцена `…/scene/staying-at-smalls` |
| Поиски оркестра и Лироя Тёрнера | 59 | сцена `…/scene/searching-for-orchestra`; `…/character/lucretia-borden`, `buster-bedson` |
| Личность убийцы | 59 | сцена `…/scene/killer-identity` |
| Итоги вечера | 59 | сцена `evening-investigations` |
| Утренние газеты | 60 | сцена `…/scene/morning-papers`; `…/organization/emancipator-and-union-leader`; `…/character/roland-marlowe`, `john-hylan` |
| Дальнейшие шаги (с «Хранителю на заметку» о мотивации) | 60 | сцена `…/scene/next-steps` |
| Что говорят в полиции | 60 | сцена `next-steps`; `…/item/manusco-autopsy-report` |
| Чарли Джонсон | 60 | сцена `next-steps`; `…/character/charlie-johnson`, `miss-walters` |
| Карта Гарлема — 1925 (ключ 1–10) | 61 | карта `…/map/harlem` (10 номеров + 7 подписей парков, стадиона и Бронкса); вариант для игроков — карта `…/map/harlem-players` и раздатка `…/handout/harlem-map-players` |
| Пит Мануско | 62 | сцена `…/scene/manusco-office`; места `…/location/manusco-office`, `manusco-apartment`; предметы `…/item/manusco-files`, `manusco-scrapbook` |
| Материал «Стомп 2» | 62 | `…/handout/stomp-2-note` |
| В редакции газеты | 62 | сцена `…/scene/newspaper-office`; `…/location/emancipator-office`; `…/character/lizzie-fayette` |
| Лирой Тёрнер (в «Дальнейших шагах») | 62 | сцена `next-steps` |
| Поиск информации о Лирое Тёрнере; До похорон Файетта; После похорон Файетта | 62–63 | сцена `…/scene/turner-inquiries`; `…/character/marnie-smeaton` |
| Дома у Тёрнера | 63 | сцена `…/scene/turner-home`; `…/location/turner-room` |
| Похороны Файетта | 63–64 | сцена `…/scene/fayette-funeral`; `…/location/morgan-dupuis-funeral-home`; `…/organization/paradise-orchestra` |
| Материал «Стомп 3» | 63 | `…/handout/stomp-3-marnie-photo` |
| Поступь второго мертвеца | 64–65 | сцена `…/scene/second-dead-mans-gait`; `…/character/freddie-fayette`, `dupuis` |
| Наблюдатель | 65 | сцена `second-dead-mans-gait` |
| Разговор с Лироем Тёрнером; Откуда у него эта труба?; Как выглядит труба; Можно ли купить или одолжить трубу?; Конец беседы | 65–66 | сцена `…/scene/talk-with-turner`; `…/item/turner-trumpet` |
| Разговор с Луи Армстронгом; Луи Армстронг (1901–1971); Что говорит Армстронг | 66–67 | сцена `…/scene/talk-with-armstrong`; `…/character/louis-armstrong`; `…/location/roseland-ballroom` |
| Похищение; Вариант сцены похищения; Если сыщики потеряли «паккард» | 67 | сцена `…/scene/kidnapping`; `…/character/marcus-green` |
| Время для кульминации | 68 | сцена `kidnapping`; сценарий: advice (ссылка) |
| Сюрприз для Джоуи; Начало сцены (диалог); Что дальше? | 68–70 | сцена `…/scene/surprise-for-joey`; `…/location/old-garage`, `old-garage-1-office`; `…/item/bootleg-trucks`; `…/character/lorette`, `mama-chandjel` |
| План «Старый гараж» (ключ 1–8, «А») | 68 | карта `…/map/old-garage` (15 меток: номера 1–8, «4» и «7» дважды, «А» пять раз; 2–5 ведут на персонажей, 7–8 — на предметы); раздатка `…/handout/old-garage-plan` |
| Преследуя Тёрнера; Могила Марни | 70 | сцена `…/scene/marnie-grave`; `…/location/marnie-smeaton-grave`; кладбище — `masks-of-nyarlathotep-en/location/america-trinity-cemetery` (предложения) |
| Карта «Кладбище Троицы» | 71 | карта `…/map/trinity-cemetery` (метка «Могила Марни Смитон»); раздатка `…/handout/trinity-cemetery-plan` |
| Момент истины; Напасть на Тёрнера; Образумить Тёрнера; Убить Тёрнера | 71–72 | сцена `…/scene/moment-of-truth` |
| Финал (награды, судьба трубы) | 72 | сценарий: conclusion (четыре награды Рассудка); шаг «Финал»; `turner-trumpet` (mechanics) |
| Мертвецкий стомп: персонажи и монстры; Персонажи | 73 | — (вступление о двух статблоках — в quality персонажей) |
| Лирой Тёрнер, 28 лет, трубач и пьяница | 73 | `…/character/leroy-turner` (статблок; зомби — вариант) |
| Джоуи Ларсон, 24 года, мелкий гангстер | 73 | `…/character/joey-larson` (статблок; зомби — вариант) |
| Чарли Джонсон, 39 лет, руководитель оркестра | 74 | `…/character/charlie-johnson` |
| Роджер Дэниелс, 31 год, федеральный агент | 74 | `…/character/roger-daniels` |
| Арчи Бонато по прозвищу Босс, 46 лет, главарь банды | 74 | `…/character/archie-bonato` |
| Шестеро гангстеров, гостей на похоронах или жителей (Гангстеры; Гости на похоронах и жители) | 75 | групповые профили `…/character/gangsters` и `…/character/funeral-guests-and-residents` (по 6 вариантов: Мэтт, Фрэггл, Дженнифер, Ферги, Джон, Реджи) |
| Малыш Джимми Фостер, 34 года, гангстер | 75 | `…/character/jimmy-foster` |
| Шестеро полицейских | 76 | групповой профиль `…/character/policemen` (6 вариантов, придуманные имена Р-151) |
| Монстры (правила зомби) | 76 | существо `…/creature/six-zombies` (abilities); `instance_of` `coc:creature:zombie` |
| Зомби Пит Мануско; Зомби Фредди Файетт | 76 | `…/character/pete-manusco`, `…/character/freddie-fayette` (статблок) |
| Шестеро зомби | 77 | `…/creature/six-zombies` (6 вариантов: Спенсер, Ник, Донье, Соломон, Алекс, Джордан) |
| Зомби Джоуи Ларсон; Зомби Лирой Тёрнер | 77 | варианты статблока `joey-larson`, `leroy-turner` |

Город — общая запись `coc:location:new-york`; район — запись «Масок» `masks-of-nyarlathotep-en/location/america-harlem`
(места сценария — книжные записи с `part_of` на неё, Р-190, Р-209). Номера 1, 6, 8, 9, 10 карты Гарлема и подписи
парков, «Поло-Граундс» и Бронкса ведут на уже существующие записи мест «Масок» (кладбище Тринити, больница, библиотека,
Колумбийский университет, собор, парки) — дублей не заводилось.

## Записи (98)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `dead-mans-stomp` |
| scene | 23 | `smalls-paradise-start`, `accidental-rudeness`, `guest-arrives`, `dead-mans-gait`, `good-samaritans`, `evening-investigations`, `staying-at-smalls`, `searching-for-orchestra`, `killer-identity`, `morning-papers`, `next-steps`, `manusco-office`, `newspaper-office`, `turner-inquiries`, `turner-home`, `fayette-funeral`, `second-dead-mans-gait`, `talk-with-turner`, `talk-with-armstrong`, `kidnapping`, `surprise-for-joey`, `marnie-grave`, `moment-of-truth` |
| location | 27 | `smalls-paradise` и 16 мест плана, `morgan-dupuis-funeral-home`, `lenox-avenue-subway`, `old-garage`, `old-garage-1-office`, `turner-room`, `manusco-office`, `manusco-apartment`, `emancipator-office`, `roseland-ballroom`, `marnie-smeaton-grave` |
| map | 5 | `harlem`, `harlem-players`, `smalls-paradise`, `old-garage`, `trinity-cemetery` (картинки `app/maps/starter-stomp-*.jpg`) |
| character | 25 | статблоки: `leroy-turner`, `joey-larson`, `charlie-johnson`, `roger-daniels`, `archie-bonato`, `jimmy-foster`, `pete-manusco`, `freddie-fayette`; групповые: `gangsters`, `funeral-guests-and-residents`, `policemen`; без статблока: `marnie-smeaton`, `lizzie-fayette`, `louis-armstrong`, `ed-smalls`, `roland-marlowe`, `john-hylan`, `lucretia-borden`, `buster-bedson`, `miss-walters`, `marcus-green`, `lorette`, `dupuis`, `mama-chandjel`, `cornell-professor` |
| creature | 1 | `six-zombies` |
| item | 6 | `turner-trumpet`, `manusco-files`, `manusco-scrapbook`, `manusco-autopsy-report`, `grey-packard`, `bootleg-trucks` |
| handout | 7 | `stomp-1-business-card`, `stomp-2-note`, `stomp-3-marnie-photo`, `harlem-map-players`, `smalls-paradise-plan`, `old-garage-plan`, `trinity-cemetery-plan` |
| organization | 3 | `bonato-gang`, `paradise-orchestra`, `emancipator-and-union-leader` |

Готовые сыщики — существующие `startovyy-nabor-ru/character/{jessie-williams,keiko-kane,louisa-russo,nevada-jones,wentworth-avebury}`
(в ссылках сценария; в тексте сценария не названы).

## Опечатки и сомнения

- Шестеро гангстеров, гостей на похоронах или жителей (с. 75): Рассудок «00» у всех шести профилей — вероятная опечатка;
  оставлено как напечатано, `errata` в обоих групповых профилях.
- Арчи Бонато (с. 74): ПЗ 15 при ВЫН 65 и ТЕЛ 75 (по правилам — 14); `errata`.
- Джоуи Ларсон (с. 73): Уклонение 45% при ЛВК 80 (половина — 40); `errata` (возможно, навык поднят).
- Полицейский 3 (с. 76): Уклонение 35% ниже половины ЛВК 75; `errata` (как у той же таблицы в «Масках»).
- Зомби Пит Мануско (с. 76): Скорость 6 (по формуле — 8); у всех зомби сценария Скорость 6; `errata`.
- Дэниелс и Бонато: «50%, (25/10)», «60%, (30/12)» — лишняя запятая; на числа не влияет.
- Зомби Лирой Тёрнер: ИНТ «—», у остальных именных зомби — «00»; оставлено как напечатано.
- Характеристики шестерых полицейских совпадают с профилями 1–6 «Стойкого констебля» «Масок», но шансы атак 40% (в «Масках» — 65%).
- Лиззи Файетт — дочь Чарли Джонсона: вывод из текста (Файетт — зять Джонсона, жена — «Элизабет Джонсон Файетт»), Р-41.
- «Пару миль» (врезка «Гарлем») передано как «около 3 км» (Р-64).
- Офис и квартира Мануско, редакция газеты: адреса в книге не даны, отнесены к Гарлему по умолчанию (пометки в записях).

## Не взято

- Иллюстрации: разворот «Музыка мёртвых» (с. 50; в папке владельца — «Иллюстрация (Дэвид Ардила Диез).jpg»), портреты
  Лироя Тёрнера (с. 52), Чарли Джонсона (с. 73), Роджера Дэниелса (с. 74), «Печать Ньярлатхотепа» (с. 53), «Вечеринка в «Смоллс Парадайз»» (с. 56),
  «Поступь второго мертвеца» (с. 64), «Труба» (с. 66), «Сюрприз для Джоуи» (с. 69). Картинки раздаток «Стомп 1–3» тоже не добавлены:
  поле `images` пишется через `pipeline/art/add_images.py` в `app/art/`, а эта папка не входит в файлы части.
- Маркус Гарви, У. Э. Б. Дю Буа, Национальная ассоциация содействия прогрессу цветного населения, капитан Роберт Смоллс, клубы «Шугар Кейн»,
  «Коннис Инн», Флетчер Хендерсон, отдел сухого закона Министерства финансов, менеджер клуба, падающий в обморок, смотритель
  кладбища, друг Чарли Джонсона, таксист, респектабельная пара — упомянуты мимоходом, остались текстом в сценах и записях.
- Подпольный бар, где Тёрнер беседует с сыщиками, полицейский участок, бордель мамаши Чанджел, артистическое агентство — без адресов
  и описаний; остались текстом в сценах (место сцены — Гарлем).
- Подписи улиц и авеню, рек Гудзон и Гарлем, «Парк Томаса Джефферсона» на карте Гарлема и улиц на карте кладбища — меток нет
  (записей таких мест нет).
- Список джазовых записей 1920-х (с. 52) — взят текстом в advice сценария, отдельных записей нет.

## Предложения

`proposals-stomp.json` — 20 правок 7 записей: Нью-Йорку (`coc:location:new-york`) — абзац о местах «Мертвецкого стомпа», ссылки
на сценарий и две карты Гарлема, источник; району Гарлем «Масок» — абзац по врезке «Гарлем», ссылки, источник; кладбищу Тринити
«Масок» — абзац (открыто в 1838 году, могила Марни, кульминация), псевдонимы «Кладбище церкви Троицы» и «Кладбище Троицы», ссылки,
источник; Гарлемской больнице, гарлемскому филиалу библиотеки, Колумбийскому университету и собору — источник (метки карты 1925 года),
псевдонимы библиотеке и собору. Пробный прогон `pipeline/integrate/apply.py --dry-run`: 20 правок ложатся.

Вопрос ведущему: район Гарлем и кладбище Тринити теперь используют две книги («Маски» и Стартовый набор) — по правилу Р-154
их стоит перенести в общие записи `coc:location:…` (это переименование id — не предложением, а решением ведущего).
