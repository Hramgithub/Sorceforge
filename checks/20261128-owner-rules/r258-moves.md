# Р-258 — перенос в общие записи (Р-154), 2026-11-28

Решение владельца Р-258: что точно встречается в двух книгах и есть тот же объект — в общую запись без вопроса. Скрипты —
`.cache/lead-tools/apply-r258/` (пути от `__file__`): `scan.py`, `scan2.py` (кандидаты с доказательством: источник другой
книги, структурная ссылка — `participants`, `where`, `part_of`, `members`, `residents`, `spots`, `relations`, `same_as` — или
`refs` из записи, чей текст называет объект), `dups.py` (дубли по имени), `apply.py` + `plan.txt`/`plan2.txt` (перенос и
слияние, перепись ссылок по всей базе и `ref` в `checks/*/new-terms.json`), `fix_corr_to.py` (`corrections[].to` следует за
новым id; `from` хранит историю).

Итог: 175 операций — 169 переносов, 6 слияний (Мордехай О’Лири, Салемская больница, кладбище Боу, Алистер Кроули,
Роджер Харролд, Майкл Томас). Старый id — в `corrections` записи (field `id`, ref Р-258). Слитые записи: тексты второй книги —
абзацем с названием книги, имена — в `aliases`, статблок второй книги — вариантом, расхождения скаляров — в `quality.notes`.
Ссылки переписаны в 1 400+ файлах; `pipeline/art/atmosphere.json` — 2 упоминания Пера Паласа.

Семьи одной работы считались одной книгой (не переносились): тома HOTOE, Convicts, A Time to Harvest; `mothers-love-ru` +
New Tales; `arkham-en` + `arkham-guide-hort-ru`; Petersen's Abominations + The Derelict + «Кошмары цифровой эпохи»;
Dead Light + «Мертвенный свет»; «Особняки безумия» + «За закрытыми дверями»; стартовые наборы; «Набор хранителя» +
«Черноводный ручей». Групповые профили (`stock_type`: солдат, сотрудник тайной полиции, террорист WWC) — не объекты, остались.

| Действие | Запись | Было | Стало | Книги-источники |
|---|---|---|---|---|
| перенос | Золотая заря | `london-3-mythos-london-en/organization/golden-dawn` | `coc:organization:golden-dawn` | london-3-mythos-london-en |
| перенос | Роджер Харролд | `time-to-harvest-1-en/character/roger-harrold` | `coc:character:roger-harrold` | arkham-en, time-to-harvest-1-en, time-to-harvest-2-en |
| слияние | Роджер Харролд | `arkham-en/character/campus-roger-harrold` | `coc:character:roger-harrold` | arkham-en, time-to-harvest-1-en, time-to-harvest-2-en |
| перенос | Майкл Томас | `prizrak-ru/character/maykl-tomas` | `coc:character:michael-thomas` | prizrak-ru, star-on-the-shore-en |
| слияние | Майкл Томас | `star-on-the-shore-en/character/michael-thomas` | `coc:character:michael-thomas` | prizrak-ru, star-on-the-shore-en |
| перенос | Руины Часовни созерцания | `prizrak-ru/location/ruiny-chasovni-sozertsaniya` | `coc:location:boston-chapel-of-contemplation-ruins` | prizrak-ru |
| перенос | Церковь Господа нашего, Дарующего тайны | `prizrak-ru/organization/tserkov-gospoda-daruyushchego-tayny` | `coc:organization:church-of-our-lord-granter-of-secrets` | prizrak-ru |
| перенос | Альберт Н. Уилмарт | `arkham-en/character/campus-albert-wilmarth` | `coc:character:albert-wilmarth` | arkham-en, arkham-guide-hort-ru, time-to-harvest-2-en |
| перенос | Эшли Лирмонт | `arkham-en/character/campus-ashley-learmonth` | `coc:character:ashley-learmonth` | arkham-en, time-to-harvest-2-en |
| перенос | Маринус Брикнелл | `arkham-en/character/campus-marinus-bricknell` | `coc:character:marinus-bricknell` | arkham-en, time-to-harvest-2-en |
| перенос | Надин Лонг | `arkham-en/character/campus-nadine-long` | `coc:character:nadine-long` | arkham-en, time-to-harvest-2-en |
| перенос | Брэдли Харкорт | `arkham-en/character/downtown-bradley-harcourt` | `coc:character:bradley-harcourt` | arkham-en, arkham-maps-en, new-tales-miskatonic-valley-2e-en |
| перенос | Чарльз Харт | `arkham-en/character/downtown-charles-hart` | `coc:character:charles-hart` | arkham-en, new-tales-miskatonic-valley-2e-en |
| перенос | Джанет Ларкин | `arkham-en/character/downtown-janet-larkin` | `coc:character:janet-larkin` | arkham-en, new-tales-miskatonic-valley-2e-en |
| перенос | Андреас вер Ховен | `arkham-en/character/merchant-andreas-ver-hoven` | `coc:character:andreas-ver-hoven` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Эдвард Паррингтон | `arkham-en/character/merchant-edward-parrington` | `coc:character:edward-parrington` | arkham-en, time-to-harvest-2-en |
| перенос | Гуди Фаулер | `arkham-en/character/merchant-goody-fowler` | `coc:character:goody-fowler` | arkham-en, arkham-guide-hort-ru |
| перенос | Бартоломью Эппли IV | `arkham-en/character/northside-bartholomew-appley` | `coc:character:bartholomew-appley` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Эдвард Тиллингаст | `arkham-en/character/northside-edward-tillinghast` | `coc:character:edward-tillinghast` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Эфраим Спрег | `arkham-en/character/northside-ephraim-sprague` | `coc:character:ephraim-sprague` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Харви Гедни | `arkham-en/character/northside-harvey-gedney` | `coc:character:harvey-gedney` | arkham-en |
| перенос | Роберта Генри | `arkham-en/character/northside-roberta-henry` | `coc:character:roberta-henry` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Райдер Адамс | `arkham-en/character/rivertown-rider-adams` | `coc:character:rider-adams` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Хортон Уилсон | `arkham-en/character/uptown-horton-wilson` | `coc:character:horton-wilson` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Стюарт Портман | `arkham-en/character/uptown-stewart-portman` | `coc:character:stewart-portman` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | «Мискатоникский глашатай» | `arkham-en/organization/campus-miskatonic-crier` | `coc:organization:miskatonic-university-crier` | arkham-en, arkham-guide-hort-ru, spark-of-life-en |
| перенос | «Камни» | `arkham-en/organization/frenchhill-the-rocks` | `coc:organization:the-rocks` | arkham-en, arkham-guide-hort-ru, new-tales-miskatonic-valley-2e-en |
| перенос | Мордехай О’Лири | `arkham-en/character/frenchhill-mordecai-oleary` | `coc:character:mordecai-oleary` | arkham-en, chernovodnyy-ruchey-ru |
| слияние | Мордехай О’Лири | `chernovodnyy-ruchey-ru/character/dues-mordekhay-oliri` | `coc:character:mordecai-oleary` | arkham-en, chernovodnyy-ruchey-ru |
| перенос | Салемская больница | `dveri-vo-tmu-ru/location/genius-salem-hospital` | `coc:location:salem-hospital` | dveri-vo-tmu-ru, eliksir-zhizni-ru |
| слияние | Салемская больница | `eliksir-zhizni-ru/location/bolnitsa-salema` | `coc:location:salem-hospital` | dveri-vo-tmu-ru, eliksir-zhizni-ru |
| перенос | Окрестности Салема | `fears-sharp-little-needles-en/location/do-not-call-salem-environs` | `coc:location:salem-environs` | fears-sharp-little-needles-en |
| перенос | Мартинс-Бич | `fears-sharp-little-needles-en/location/do-not-call-martins-beach` | `coc:location:martins-beach` | fears-sharp-little-needles-en |
| перенос | Росс-Корнерс | `starter-edge-of-darkness-ru/location/ross-corners` | `coc:location:ross-corners` | starter-edge-of-darkness-ru |
| перенос | Кладбище Боу | `wwc-covert-actions-en/location/bow-cemetery` | `coc:location:bow-cemetery` | wwc-covert-actions-en, wwc-london-en, wwc-section-46-en |
| слияние | Кладбище Боу | `wwc-section-46-en/location/tower-hamlets-cemetery-park` | `coc:location:bow-cemetery` | wwc-covert-actions-en, wwc-london-en, wwc-section-46-en |
| перенос | Хэмпстед | `eyes-like-red-balls-en/location/hampstead` | `coc:location:hampstead` | eyes-like-red-balls-en |
| перенос | Паддингтон | `fears-sharp-little-needles-en/location/fuel-paddington` | `coc:location:paddington` | fears-sharp-little-needles-en |
| перенос | Вокзал Паддингтон | `fears-sharp-little-needles-en/location/fuel-paddington-station` | `coc:location:paddington-station` | fears-sharp-little-needles-en |
| перенос | Ист-Энд | `lark-in-a-cage-en/location/east-end` | `coc:location:east-end` | lark-in-a-cage-en |
| перенос | Гринвич | `lark-in-a-cage-en/location/greenwich` | `coc:location:greenwich` | lark-in-a-cage-en |
| перенос | Темза | `lark-in-a-cage-en/location/river-thames` | `coc:location:river-thames` | lark-in-a-cage-en, london-3-mythos-london-en |
| перенос | Риджентс-канал | `lokhmotya-korolya-ru/location/springer-regents-canal` | `coc:location:regents-canal` | lokhmotya-korolya-ru |
| перенос | Спиталфилдс | `lokhmotya-korolya-ru/location/talk-spitalfields` | `coc:location:spitalfields` | lokhmotya-korolya-ru |
| перенос | Финсбери | `london-3-mythos-london-en/location/finsbury` | `coc:location:finsbury` | london-3-mythos-london-en |
| перенос | Клеркенуэлл | `london-3-mythos-london-en/location/clerkenwell` | `coc:location:clerkenwell` | london-3-mythos-london-en |
| перенос | Форт Коулхаус | `london-3-mythos-london-en/location/coalhouse-fort` | `coc:location:coalhouse-fort` | london-3-mythos-london-en |
| перенос | Гринвичский пирс | `london-3-mythos-london-en/location/greenwich-pier` | `coc:location:greenwich-pier` | london-3-mythos-london-en |
| перенос | Медуэй | `london-3-mythos-london-en/location/river-medway` | `coc:location:river-medway` | london-3-mythos-london-en |
| перенос | Вестминстер | `masks-of-nyarlathotep-en/location/england-westminster` | `coc:location:westminster` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Сити | `masks-of-nyarlathotep-en/location/england-city-of-london` | `coc:location:city-of-london` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Саутуарк | `masks-of-nyarlathotep-en/location/england-southwark` | `coc:location:southwark` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Сент-Панкрас | `masks-of-nyarlathotep-en/location/england-st-pancras` | `coc:location:st-pancras` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Челси | `masks-of-nyarlathotep-en/location/england-chelsea` | `coc:location:chelsea` | masks-of-nyarlathotep-en |
| перенос | Ковент-Гарден | `masks-of-nyarlathotep-en/location/england-covent-garden` | `coc:location:covent-garden` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Мэйфэр | `masks-of-nyarlathotep-en/location/england-mayfair` | `coc:location:mayfair` | masks-of-nyarlathotep-en |
| перенос | Сохо | `masks-of-nyarlathotep-en/location/england-soho` | `coc:location:soho` | gothic-by-gaslight-en, masks-of-nyarlathotep-en |
| перенос | Окрестности Лондона | `masks-of-nyarlathotep-en/location/england-london-environs` | `coc:location:london-environs` | masks-of-nyarlathotep-en |
| перенос | Адмиралтейство | `masks-of-nyarlathotep-en/location/england-admiralty` | `coc:location:admiralty` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Военное министерство | `masks-of-nyarlathotep-en/location/england-war-office` | `coc:location:war-office` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Новый Скотланд-Ярд | `masks-of-nyarlathotep-en/location/england-new-scotland-yard` | `coc:location:new-scotland-yard` | masks-of-nyarlathotep-en |
| перенос | Парк Грин | `masks-of-nyarlathotep-en/location/england-green-park` | `coc:location:green-park` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players, wwc-london-en |
| перенос | Парк Сент-Джеймс | `masks-of-nyarlathotep-en/location/england-st-jamess-park` | `coc:location:st-jamess-park` | lokhmotya-korolya-ru, masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Станция «Элефант-энд-Касл» | `masks-of-nyarlathotep-en/location/england-elephant-and-castle-station` | `coc:location:elephant-and-castle-station` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Станция «Юстон» | `masks-of-nyarlathotep-en/location/england-euston-station` | `coc:location:euston-station` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Станция «Кингс-Кросс» | `masks-of-nyarlathotep-en/location/england-kings-cross-station` | `coc:location:kings-cross-station` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Станция «Сент-Панкрас» | `masks-of-nyarlathotep-en/location/england-st-pancras-station` | `coc:location:st-pancras-station` | hotoe-travelers-companion-en, masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Больница Святого Варфоломея | `masks-of-nyarlathotep-en/location/england-st-bartholomews-hospital` | `coc:location:st-bartholomews-hospital` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Редакция «Таймс» | `masks-of-nyarlathotep-en/location/england-times-office` | `coc:location:times-office` | masks-of-nyarlathotep-en, masks-of-nyarlathotep-ru-players |
| перенос | Столичная полиция (Скотланд-Ярд) | `masks-of-nyarlathotep-en/organization/england-metropolitan-police` | `coc:organization:metropolitan-police` | masks-of-nyarlathotep-en |
| перенос | Сенчури-хаус | `wwc-cold-war-en/location/century-house` | `coc:location:century-house` | wwc-cold-war-en |
| перенос | Клуб Грина | `wwc-cold-war-en/location/greene-club` | `coc:location:greene-club` | wwc-cold-war-en, wwc-section-46-en |
| перенос | Джексон Элиас | `masks-of-nyarlathotep-en/character/jackson-elias` | `coc:character:jackson-elias` | masks-of-nyarlathotep-en |
| перенос | Порождение тумана (Тварь в тумане) | `masks-of-nyarlathotep-en/creature/fog-spawn` | `coc:creature:fog-spawn` | grand-grimoire-en, masks-of-nyarlathotep-en |
| перенос | Морнингсайд-парк | `masks-of-nyarlathotep-en/location/america-morningside-park` | `coc:location:morningside-park` | masks-of-nyarlathotep-en |
| перенос | Парк Маунт-Моррис | `masks-of-nyarlathotep-en/location/america-mount-morris-park` | `coc:location:mount-morris-park` | masks-of-nyarlathotep-en |
| перенос | Стадион «Поло-Граундс» | `masks-of-nyarlathotep-en/location/america-polo-grounds` | `coc:location:polo-grounds` | masks-of-nyarlathotep-en |
| перенос | Риверсайд-парк | `masks-of-nyarlathotep-en/location/america-riverside-park` | `coc:location:riverside-park` | masks-of-nyarlathotep-en |
| перенос | Парк Сент-Николас | `masks-of-nyarlathotep-en/location/america-st-nicholas-park` | `coc:location:st-nicholas-park` | masks-of-nyarlathotep-en |
| перенос | Старый город | `masks-of-nyarlathotep-en/location/egypt-old-city` | `coc:location:cairo-old-city` | masks-of-nyarlathotep-en |
| перенос | Озеро Титикака | `masks-of-nyarlathotep-en/location/peru-lake-titicaca` | `coc:location:lake-titicaca` | masks-of-nyarlathotep-en |
| перенос | Окрестности Парижа | `tsarstvo-terrora-ru/location/paris-environs` | `coc:location:paris-environs` | hotoe-book-2-en, tsarstvo-terrora-ru |
| перенос | Пуасси | `tsarstvo-terrora-ru/location/1789-poissy` | `coc:location:poissy` | hotoe-book-2-en, tsarstvo-terrora-ru |
| перенос | Версаль | `tsarstvo-terrora-ru/location/1789-versailles` | `coc:location:versailles` | tsarstvo-terrora-ru |
| перенос | Катакомбы | `tsarstvo-terrora-ru/location/paris-catacombs` | `coc:location:paris-catacombs` | hotoe-book-2-en, hotoe-travelers-companion-en, tsarstvo-terrora-ru |
| перенос | Шарантонская психиатрическая больница | `tsarstvo-terrora-ru/location/paris-charenton-asylum` | `coc:location:paris-charenton-asylum` | hotoe-book-2-en, tsarstvo-terrora-ru |
| перенос | Люксембургский сад | `tsarstvo-terrora-ru/location/paris-luxembourg-garden` | `coc:location:paris-luxembourg-garden` | tsarstvo-terrora-ru |
| перенос | Собор Нотр-Дам | `tsarstvo-terrora-ru/location/paris-notre-dame` | `coc:location:paris-notre-dame` | hotoe-travelers-companion-en, tsarstvo-terrora-ru |
| перенос | Королевская библиотека | `tsarstvo-terrora-ru/location/paris-royal-library` | `coc:location:paris-royal-library` | hotoe-book-2-en, hotoe-travelers-companion-en, tsarstvo-terrora-ru |
| перенос | Дворец Тюильри | `tsarstvo-terrora-ru/location/paris-tuileries` | `coc:location:paris-tuileries` | tsarstvo-terrora-ru |
| перенос | Дом Инвалидов | `tsarstvo-terrora-ru/location/reign-invalides` | `coc:location:paris-invalides` | tsarstvo-terrora-ru |
| перенос | Пале-Рояль | `tsarstvo-terrora-ru/location/reign-palais-royal` | `coc:location:paris-palais-royal` | tsarstvo-terrora-ru |
| перенос | Оноре Фрагонар | `tsarstvo-terrora-ru/character/1789-honore-fragonard` | `coc:character:honore-fragonard` | tsarstvo-terrora-ru |
| перенос | Мадам де Бриенн | `tsarstvo-terrora-ru/character/1789-madame-de-brienne` | `coc:character:madame-de-brienne` | tsarstvo-terrora-ru |
| перенос | Луи Малон | `tsarstvo-terrora-ru/character/louis-malon` | `coc:character:louis-malon` | tsarstvo-terrora-ru |
| перенос | Люсьен Риго | `tsarstvo-terrora-ru/character/lucien-rigault` | `coc:character:lucien-rigault` | tsarstvo-terrora-ru |
| перенос | Клер Лакомб | `reign-of-terror-women-en/character/claire-lacombe` | `coc:character:claire-lacombe` | reign-of-terror-women-en |
| перенос | Мари Тюссо | `reign-of-terror-women-en/character/marie-tussaud` | `coc:character:marie-tussaud` | reign-of-terror-women-en |
| перенос | Теруань де Мерикур | `reign-of-terror-women-en/character/theroigne-de-mericourt` | `coc:character:theroigne-de-mericourt` | reign-of-terror-women-en |
| перенос | Центр Милана | `lokhmotya-korolya-ru/location/milan-city-centre` | `coc:location:milan-city-centre` | lokhmotya-korolya-ru |
| перенос | Миланский университет | `lokhmotya-korolya-ru/location/milan-university` | `coc:location:milan-university` | hotoe-book-2-en, lokhmotya-korolya-ru |
| перенос | Кремль | `secrets-of-the-kremlin-en/location/kremlin` | `coc:location:kremlin` | secrets-of-the-kremlin-en |
| перенос | Александровский сад | `secrets-of-the-kremlin-en/location/alexandrovsky-garden` | `coc:location:alexandrovsky-garden` | secrets-of-the-kremlin-en |
| перенос | Москва-река | `secrets-of-the-kremlin-en/location/moscow-river` | `coc:location:moscow-river` | secrets-of-the-kremlin-en |
| перенос | Большой Стамбул | `wwc-cold-war-en/location/greater-istanbul` | `coc:location:greater-istanbul` | wwc-cold-war-en |
| перенос | Бейоглу | `wwc-cold-war-en/location/beyoglu` | `coc:location:beyoglu` | hotoe-book-2-en, hotoe-book-3-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Фатих | `wwc-cold-war-en/location/fatih` | `coc:location:fatih` | hotoe-book-2-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Эюп | `wwc-cold-war-en/location/eyup` | `coc:location:eyup` | wwc-cold-war-en |
| перенос | Ускюдар | `wwc-cold-war-en/location/uskudar` | `coc:location:uskudar` | hotoe-book-2-en, hotoe-book-3-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Кадыкёй | `wwc-cold-war-en/location/kadikoy` | `coc:location:kadikoy` | hotoe-book-3-en, wwc-cold-war-en |
| перенос | Босфор | `wwc-cold-war-en/location/bosphorus` | `coc:location:bosphorus` | hotoe-book-3-en, hotoe-book-4-en, wwc-cold-war-en |
| перенос | Золотой Рог | `wwc-cold-war-en/location/golden-horn` | `coc:location:golden-horn` | hotoe-book-3-en, wwc-cold-war-en |
| перенос | Золотые ворота | `wwc-cold-war-en/location/golden-gate` | `coc:location:constantinople-golden-gate` | hotoe-book-3-en, wwc-cold-war-en |
| перенос | Святая София | `wwc-cold-war-en/location/haghia-sophia` | `coc:location:haghia-sophia` | hotoe-book-2-en, hotoe-book-3-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Голубая мечеть | `wwc-cold-war-en/location/blue-mosque` | `coc:location:blue-mosque` | hotoe-book-2-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Гранд-базар | `wwc-cold-war-en/location/grand-bazaar` | `coc:location:grand-bazaar` | hotoe-book-2-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Дворец Топкапы | `wwc-cold-war-en/location/topkapi-palace` | `coc:location:topkapi-palace` | hotoe-book-2-en, wwc-cold-war-en |
| перенос | Галатский мост | `wwc-cold-war-en/location/galata-bridge` | `coc:location:galata-bridge` | hotoe-book-2-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Галатская башня | `wwc-cold-war-en/location/galata-tower` | `coc:location:galata-tower` | wwc-cold-war-en |
| перенос | Отель «Пера Палас» | `wwc-cold-war-en/location/pera-palas-hotel` | `coc:location:pera-palas-hotel` | hotoe-book-2-en, hotoe-book-4-en, hotoe-travelers-companion-en, wwc-cold-war-en |
| перенос | Площадь Беязит и Стамбульский университет | `wwc-cold-war-en/location/beyazit-square-and-istanbul-university` | `coc:location:beyazit-square-and-istanbul-university` | wwc-cold-war-en |
| перенос | Аэропорт Ататюрка | `wwc-cold-war-en/location/ataturk-airport` | `coc:location:ataturk-airport` | wwc-cold-war-en |
| перенос | N | `wwc-cold-war-en/character/n` | `coc:character:n` | wwc-cold-war-en, wwc-london-en |
| перенос | H | `wwc-cold-war-en/character/h` | `coc:character:h` | wwc-cold-war-en |
| перенос | Гарольд Вильсон | `wwc-cold-war-en/character/harold-wilson` | `coc:character:harold-wilson` | wwc-cold-war-en |
| перенос | Джеймс Джизес Энглтон | `wwc-cold-war-en/character/james-jesus-angleton` | `coc:character:james-jesus-angleton` | wwc-cold-war-en |
| перенос | Джим Джонс | `wwc-cold-war-en/character/jim-jones` | `coc:character:jim-jones` | wwc-cold-war-en |
| перенос | Ким Филби | `wwc-cold-war-en/character/kim-philby` | `coc:character:kim-philby` | wwc-cold-war-en |
| перенос | Патриция «Патти» Херст | `wwc-cold-war-en/character/patty-hearst` | `coc:character:patty-hearst` | wwc-cold-war-en |
| перенос | Пол Пот | `wwc-cold-war-en/character/pol-pot` | `coc:character:pol-pot` | wwc-cold-war-en |
| перенос | Ричард Никсон | `wwc-cold-war-en/character/richard-nixon` | `coc:character:richard-nixon` | wwc-cold-war-en, wwc-our-american-cousins-en |
| перенос | Сеть N | `wwc-cold-war-en/organization/n` | `coc:organization:network-n` | wwc-cold-war-en, wwc-london-en |
| перенос | Секция 46 | `wwc-cold-war-en/organization/section-46` | `coc:organization:section-46` | wwc-cold-war-en |
| перенос | Австралийская секретная разведывательная служба (ASIS) | `wwc-cold-war-en/organization/asis` | `coc:organization:asis` | wwc-cold-war-en |
| перенос | Бюро государственной безопасности ЮАР (BfSS) | `wwc-cold-war-en/organization/bfss` | `coc:organization:bfss` | wwc-cold-war-en |
| перенос | Чёрное братство | `wwc-cold-war-en/organization/black-brotherhood` | `coc:organization:black-brotherhood` | wwc-cold-war-en |
| перенос | Братья Жёлтого знака (1970-е) | `wwc-cold-war-en/organization/brothers-of-the-yellow-sign` | `coc:organization:brothers-of-the-yellow-sign` | wwc-cold-war-en |
| перенос | Центральный следственный отдел КНР (CID) | `wwc-cold-war-en/organization/central-investigation-department` | `coc:organization:central-investigation-department` | wwc-cold-war-en |
| перенос | Центральное разведывательное управление (ЦРУ) | `wwc-cold-war-en/organization/cia` | `coc:organization:cia` | wwc-cold-war-en |
| перенос | Разведывательное управление Министерства обороны (РУМО) | `wwc-cold-war-en/organization/dia` | `coc:organization:dia` | wwc-cold-war-en |
| перенос | Национальное разведывательное управление Чили (DINA) | `wwc-cold-war-en/organization/dina` | `coc:organization:dina` | wwc-cold-war-en |
| перенос | Австралийское управление оборонной связи (DSD) | `wwc-cold-war-en/organization/dsd` | `coc:organization:dsd` | wwc-cold-war-en |
| перенос | Федеральное бюро расследований (ФБР) | `wwc-cold-war-en/organization/fbi` | `coc:organization:fbi` | wwc-cold-war-en |
| перенос | «Пять глаз» (соглашение UKUSA) | `wwc-cold-war-en/organization/five-eyes` | `coc:organization:five-eyes` | wwc-cold-war-en |
| перенос | Центр правительственной связи (GCHQ) | `wwc-cold-war-en/organization/gchq` | `coc:organization:gchq` | wwc-cold-war-en |
| перенос | Главное разведывательное управление (ГРУ) | `wwc-cold-war-en/organization/gru` | `coc:organization:gru` | wwc-cold-war-en |
| перенос | Межведомственная разведка Пакистана (ISI) | `wwc-cold-war-en/organization/isi` | `coc:organization:isi` | wwc-cold-war-en |
| перенос | Комитет государственной безопасности (КГБ) | `wwc-cold-war-en/organization/kgb` | `coc:organization:kgb` | wwc-cold-war-en |
| перенос | Служба безопасности (МИ-5) | `wwc-cold-war-en/organization/mi5` | `coc:organization:mi5` | wwc-cold-war-en |
| перенос | Секретная разведывательная служба (МИ-6) | `wwc-cold-war-en/organization/mi6` | `coc:organization:mi6` | wwc-cold-war-en |
| перенос | Моссад | `wwc-cold-war-en/organization/mossad` | `coc:organization:mossad` | wwc-cold-war-en |
| перенос | Национальное управление военно-космической разведки (НУВКР) | `wwc-cold-war-en/organization/nro` | `coc:organization:nro` | wwc-cold-war-en |
| перенос | Агентство национальной безопасности (АНБ) | `wwc-cold-war-en/organization/nsa` | `coc:organization:nsa` | wwc-cold-war-en |
| перенос | Управление стратегических служб (УСС) | `wwc-cold-war-en/organization/oss` | `coc:organization:oss` | wwc-cold-war-en |
| перенос | Служба безопасности Королевской канадской конной полиции (RCMPSS) | `wwc-cold-war-en/organization/rcmpss` | `coc:organization:rcmpss` | wwc-cold-war-en |
| перенос | Организация разведки и национальной безопасности Ирана (САВАК) | `wwc-cold-war-en/organization/savak` | `coc:organization:savak` | wwc-cold-war-en |
| перенос | Служба внешней документации и контрразведки (SDECE) | `wwc-cold-war-en/organization/sdece` | `coc:organization:sdece` | wwc-cold-war-en |
| перенос | Департамент государственной безопасности Румынии (Секуритате) | `wwc-cold-war-en/organization/securitate` | `coc:organization:securitate` | wwc-cold-war-en |
| перенос | Управление специальных операций (SOE) | `wwc-cold-war-en/organization/soe` | `coc:organization:soe` | wwc-cold-war-en |
| перенос | Министерство государственной безопасности ГДР (Штази) | `wwc-cold-war-en/organization/stasi` | `coc:organization:stasi` | wwc-cold-war-en |
| перенос | Алистер Кроули | `lokhmotya-korolya-ru/character/aleister-crowley` | `coc:character:aleister-crowley` | lokhmotya-korolya-ru, pax-cthuliana-ru |
| слияние | Алистер Кроули | `pax-cthuliana-ru/character/alister-krouli` | `coc:character:aleister-crowley` | lokhmotya-korolya-ru, pax-cthuliana-ru |
| перенос | Элеанор Вудс | `koshmarnyy-priliv-ru/character/eleanor-woods` | `coc:character:eleanor-woods` | koshmarnyy-priliv-pregens-ru, naedine-s-prilivom-ru |
| перенос | Эллери Вудс | `koshmarnyy-priliv-ru/character/ellery-woods` | `coc:character:ellery-woods` | koshmarnyy-priliv-pregens-ru, naedine-s-prilivom-ru |
| перенос | Существа Иба | `naedine-s-prilivom-ru/creature/sushchestva-iba` | `coc:creature:beings-of-ib` | naedine-s-prilivom-ru |
| перенос | Плотоядные ракообразные | `pobeg-iz-innsmuta-ru/creature/plotoyadnye-rakoobraznye` | `coc:creature:carnivorous-crustaceans` | pobeg-iz-innsmuta-ru |
| перенос | Первая национальная бакалея | `pobeg-iz-innsmuta-ru/organization/pervaya-natsionalnaya-bakaleya` | `coc:organization:first-national-grocery` | pobeg-iz-innsmuta-ru |
| перенос | Юрей | `sny-o-yaponii-ru/creature/yurei` | `coc:creature:yurei` | sny-o-yaponii-ru |
| перенос | Сесил Джонс | `starter-edge-of-darkness-ru/character/cecil-jones` | `coc:character:cecil-jones` | starter-edge-of-darkness-ru |
| перенос | Кроуфорд Харрис | `starter-edge-of-darkness-ru/character/crawford-harris` | `coc:character:crawford-harris` | starter-edge-of-darkness-ru |
| перенос | Гарольд Копли | `starter-edge-of-darkness-ru/character/harold-copley` | `coc:character:harold-copley` | starter-edge-of-darkness-ru |
| перенос | Роберт Менкин | `starter-edge-of-darkness-ru/character/robert-menkin` | `coc:character:robert-menkin` | starter-edge-of-darkness-ru |
| перенос | Таящийся на чердаке | `starter-edge-of-darkness-ru/creature/lurker-in-the-attic` | `coc:creature:lurker-in-the-attic` | starter-edge-of-darkness-ru |
| перенос | Порошок Ибн-Гази | `starter-edge-of-darkness-ru/item/ibn-ghazi-powder` | `coc:item:ibn-ghazi-powder` | starter-edge-of-darkness-ru |
| перенос | Тёмное братство | `starter-edge-of-darkness-ru/organization/dark-brotherhood` | `coc:organization:dark-brotherhood` | starter-edge-of-darkness-ru |

## Оставлено (не тот же объект или второй книги нет)

- Стаки: Кэлвин (`arkham-en/character/downtown-calvin-stuckey`) и Рэй (`new-tales…/character/ray-stuckey`) — разные имена,
  текст не доказывает одно лицо; две записи.
- Тиллингаст: Edwin/Edward — одна запись (псевдоним Edwin), теперь общая `coc:character:edward-tillinghast`.
- Уилбур Уэйтли — записи нет ни в одной книге (упоминание в рассказе «Духа предприятия»), текст.
- Король Куранес — запись только в HOTOE; другие книги называют его в тексте (`coc:location:celephais`), записью не стал.
- Существа Иба: вид `naedine-s-prilivom-ru/creature/sushchestva-iba` → `coc:creature:beings-of-ib`; делегация HOTOE
  (`hotoe-book-2-en/creature/dream-beings-of-ib`, 6 вариантов) — запись книги со `same_as` на общую.
- Районы Кингспорта (`new-tales…/location/kingsport-*`) — других книг нет, остались.
- Финляндия, Кент, Южный Техас, Бангей (Goat), станции пути HOTOE, Танкар/Пасигхат/Бодх-Гая (CoF) — одна книга, текст/записи книги.
- Медальон Итакуа HOTOE и общий (Дерлет); чернорубашечники Венеции и Триеста — разные, не слиты.
- Флойд Тоби, Мистер Блэк, упыри кладбища Боу, вспомогательные агенты Сети N, Персиваль Сент-Джон, Перси Гуджон, «Пестис»,
  музей Топкапы, отель «Мидленд Гранд», Дельплас/Леру/Гимар, Дом Лорьенов — «вторая книга» лишь в абзаце, перенесённом из их же
  книги; не переносились.
- Помещения особняка Феналика 1789 года и Дом Лорьенов 1923 года (камеры, зал статуи) — у HOTOE свои записи, тождество не очевидно.
- Хищный ракообразный «Любви матери» — экземпляр сцены со связью на общий вид `coc:creature:carnivorous-crustaceans`.
- ГПУ (`secrets-of-the-kremlin-en`) и общий ОГПУ — разные периоды, не слиты; британское генконсульство в Стамбуле (WWC) и
  консульство 1893 года HOTOE — у HOTOE своя запись.
- Братья Жёлтого знака: WWC (1970-е) — общая `coc:organization:brothers-of-the-yellow-sign`; миланская ячейка «Лохмотьев короля»
  — своя запись.
- «Алхимические сочинения Эдварда Келли» (`arkham-en` и London 3) — книга Мифов с разными характеристиками изданий (Р-56):
  не сливалась, нужна запись издания — на усмотрение ведущего.
- Профили WWC (`soldier`, `secret-police`, `terrorist-guerrilla-fighter`) — шаблоны, `instance_of` из Covert Actions оставлен.