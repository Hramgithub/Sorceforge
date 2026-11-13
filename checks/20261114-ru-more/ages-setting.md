# Тёмные века — часть ages-setting (Введение, Предисловие, гл. 1 «Англо-саксонская Англия», гл. 2 «От А до Я про Тёмные века»)

Книга `temnye-veka-tri-stsenariya-ru`, физические страницы 7–57 (печатные 6–56). Сверка — с `cthulhu-dark-ages-en`
(предварительная английская версия: ссылки «@@», вёрстка другая; гл. 1 там на с. 70–99, гл. 2 — на с. 34–45).
Текст — по русскому переводу с правкой опечаток и явных ошибок перевода; таблицы и числа сверены по изображениям
страниц. Меры переведены в метрические (Р-64): мили → км, футы/дюймы → м/см, акры → га.

Все записи: `axes.era` ["dark-ages"], `ruleset` "core". Правила — `coc:rule:dark-ages-setting-*` (59), вложенность —
полем `parent` (корни — `anglo-saxon-england`, `a-z`, отдельно `introduction`). Таблиц с броском в этих главах нет,
поэтому записей `coc:table:*` нет: все таблицы без броска — в `tables` правил. Города путеводителя — общие записи мест
`coc:location:*` (18); Лондон уже был в базе — описание Тёмных веков предложено в `proposals-ages-setting.json`.

## Заголовки книги

| Заголовок книги | Страница (печ.) | Где в базе |
|---|---|---|
| Введение | 6 | `coc:rule:dark-ages-setting-introduction` |
| Предисловие | 7 | `coc:rule:dark-ages-setting-introduction` |
| Глава 1. Англо-саксонская Англия (вступление) | 9 | `coc:rule:dark-ages-setting-anglo-saxon-england` |
| Англия | 9 | `coc:rule:dark-ages-setting-anglo-saxon-england` |
| Земля | 9 | `coc:rule:dark-ages-setting-anglo-saxon-england` |
| Погода | 9 | `coc:rule:dark-ages-setting-anglo-saxon-england` |
| Типы поселений: Бург, Крепость на холме, Монастырь, Вик, Деревня | 9–12 | `coc:rule:dark-ages-setting-settlement-types` |
| Врезка «Короли англо-саксонской Англии» | 10 | `coc:rule:dark-ages-setting-kings-and-kingdoms` (tables) |
| Врезка «Бурги англо-саксонского Уэссекса» (32 бурга) | 10 | `coc:rule:dark-ages-setting-settlement-types` (tables) |
| Карта англо-саксонской Англии | 11 | `app/maps/ages-setting-anglo-saxon-england.jpg`; черновик записи карты — см. «Ведущему»; описание — `coc:rule:dark-ages-setting-geography` |
| Врезка «Королевства англо-саксонской Англии и Денло» | 12 | `coc:rule:dark-ages-setting-kings-and-kingdoms` |
| Социальная структура | 12–13 | `coc:rule:dark-ages-setting-social-structure` |
| Врезка «Тени прошлого» | 12 | `coc:rule:dark-ages-setting-social-structure` |
| Имена | 13 | `coc:rule:dark-ages-setting-names` |
| Врезка «Прозвища» | 13 | `coc:rule:dark-ages-setting-names` (tables) |
| Люди; Семья; Брак | 16 | `coc:rule:dark-ages-setting-people` |
| Женщины; Дети | 17 | `coc:rule:dark-ages-setting-people` |
| Детские игры | 18 | `coc:rule:dark-ages-setting-people` |
| Врезка «Беот» | 18 | `coc:rule:dark-ages-setting-beot` (механика Статуса) |
| Постройки | 18 | `coc:rule:dark-ages-setting-buildings` |
| Врезка «Вопрос о грамотности и алфавите» | 18 | `coc:rule:dark-ages-setting-literacy-and-alphabet` |
| Руины; Личное жильё; Жильё тэна; Грубенхауз | 19 | `coc:rule:dark-ages-setting-buildings` |
| Врезка «Старые английские фразы» | 19 | `coc:rule:dark-ages-setting-old-english` (tables) |
| Валюта и налоги; Налоги (таблицы монет и цен животных) | 20 | `coc:rule:dark-ages-setting-currency-and-taxes` |
| Врезка «Рассмотрение судебных дел» | 20 | `coc:rule:dark-ages-setting-court-cases` |
| Преступление и наказание | 21–22 | `coc:rule:dark-ages-setting-crime-and-punishment` |
| Врезка «Преступление и возмещение» | 21 | `coc:rule:dark-ages-setting-crime-and-punishment` (tables) |
| Вергельд (таблица); Наказание; Нанесение увечий и казнь | 22 | `coc:rule:dark-ages-setting-crime-and-punishment` |
| Вне закона; Вражда | 23 | `coc:rule:dark-ages-setting-crime-and-punishment` |
| Внешний вид; Одежда; Причёска | 23 | `coc:rule:dark-ages-setting-appearance` |
| Еда, охота и фермерство; Еда | 23–24 | `coc:rule:dark-ages-setting-food-and-farming` |
| Приготовление и питание; Голод; Фермерство | 24 | `coc:rule:dark-ages-setting-food-and-farming` |
| Рыбалка и охота | 25 | `coc:rule:dark-ages-setting-food-and-farming` |
| Путешествия | 25 | `coc:rule:dark-ages-setting-travel` |
| Развлечения; Стихи и загадки | 25 | `coc:rule:dark-ages-setting-entertainment` |
| Врезка «Примеры загадок» | 25 | `coc:rule:dark-ages-setting-entertainment` |
| Военное дело; Фирд; Хартверу; Военное снаряжение | 26–27 | `coc:rule:dark-ages-setting-warfare` |
| Врезка «Вторжения викингов» | 27 | `coc:rule:dark-ages-setting-warfare` |
| Сборы; Стена щитов | 28 | `coc:rule:dark-ages-setting-warfare` |
| Вера; Христианство | 28 | `coc:rule:dark-ages-setting-faith` |
| Врезка «Общая десятина» | 28 | `coc:rule:dark-ages-setting-faith` (tables) |
| Типы церквей; Заговоры; Обереги | 29 | `coc:rule:dark-ages-setting-faith` |
| Врезка «Архиепископы Кентерберийские» | 29 | `coc:rule:dark-ages-setting-faith` (tables) |
| Старые обычаи | 29–30 | `coc:rule:dark-ages-setting-old-ways` |
| Врезка «Кто есть кто?» | 30 | `coc:rule:dark-ages-setting-old-ways` |
| Англо-саксонские языческие боги; Язычество на практике | 30–31 | `coc:rule:dark-ages-setting-old-ways` |
| Ходящие в ночи; Вирд | 31 | `coc:rule:dark-ages-setting-old-ways` |
| Норвежское язычество; Боги | 31–33 | `coc:rule:dark-ages-setting-norse-paganism` |
| Таблица «Англосаксонские месяцы и их значение» | 32 | `coc:rule:dark-ages-setting-time-and-year` (tables) |
| Время и год | 33 | `coc:rule:dark-ages-setting-time-and-year` |
| Здоровье, исцеление и смерть | 33 | `coc:rule:dark-ages-setting-health-and-healing` |
| Врезка «Медицина» | 33 | `coc:rule:dark-ages-setting-medicine` (механика) |
| Санитария; Болезни и травмы; Уход | 34 | `coc:rule:dark-ages-setting-health-and-healing` |
| Врезка «Инструментарий врача» | 34 | `coc:rule:dark-ages-setting-health-and-healing` (tables) |
| Врезка «Примеры лечения» | 35 | `coc:rule:dark-ages-setting-health-and-healing` |
| «Лечебник Бальда», «Лакнунга», святые места, калеки | 35–36 | `coc:rule:dark-ages-setting-health-and-healing` |
| Смерть и похороны | 36 | `coc:rule:dark-ages-setting-death-and-burial` |
| География англо-саксонской Англии | 36 | `coc:rule:dark-ages-setting-geography` |
| Аберфрау (Миф) | 36 | `coc:location:aberffraw` |
| Альтклуд (Миф) | 36 | `coc:location:altclud` |
| Кентербери (Миф) | 36–37 | `coc:location:canterbury` |
| Врезка «Руководство по произношению» | 37 | `coc:rule:dark-ages-setting-old-english` |
| Карлайл (Миф) | 37 | `coc:location:carlisle` |
| Честер (Миф) | 37–38 | `coc:location:chester` |
| Динефор (Мифы) | 38 | `coc:location:dinefwr` |
| Дарем (Миф) | 38 | `coc:location:durham` |
| Эксетер (Миф) | 38 | `coc:location:exeter` |
| Ипсвич (Миф) | 38–39 | `coc:location:ipswich-england` |
| Лестер (Миф) | 39 | `coc:location:leicester` |
| Линкольн (Миф) | 39 | `coc:location:lincoln-england` |
| Лондон (Миф) | 39 | `coc:location:london` — через предложения (`proposals-ages-setting.json`) |
| Норидж (Миф) | 39–40 | `coc:location:norwich` |
| Оксфорд (Миф) | 40 | `coc:location:oxford` |
| Пенгверн (Миф) | 40 | `coc:location:pengwern` |
| Тетфорд (Миф) | 40 | `coc:location:thetford` |
| Вэрхэм | 40–41 | `coc:location:wareham` |
| Винчестер (Миф) | 41 | `coc:location:winchester` |
| Йорк | 41 | `coc:location:york` |
| Глава 2. От А до Я про Тёмные века (вступление) | 43 | `coc:rule:dark-ages-setting-a-z` |
| Сражения | 43 | `coc:rule:dark-ages-setting-a-z-battles` |
| Замки | 43 | `coc:rule:dark-ages-setting-a-z-castles` |
| Коммуникации | 43 | `coc:rule:dark-ages-setting-a-z-communication` |
| Сообщество | 43–44 | `coc:rule:dark-ages-setting-a-z-community` |
| Тьма | 44 | `coc:rule:dark-ages-setting-a-z-darkness` |
| Дьявол | 44–45 | `coc:rule:dark-ages-setting-a-z-devil` |
| Ересь; врезка «Орлеанская ересь» | 45 | `coc:rule:dark-ages-setting-a-z-heresy` |
| Иерархия | 45 | `coc:rule:dark-ages-setting-a-z-hierarchy` |
| Взятие заложника | 46 | `coc:rule:dark-ages-setting-a-z-hostage-taking` |
| Юмор | 46 | `coc:rule:dark-ages-setting-a-z-humor` |
| Рыцари | 46 | `coc:rule:dark-ages-setting-a-z-knights` |
| Грамотность; врезка «Грамотность в игре» | 46 | `coc:rule:dark-ages-setting-a-z-literacy` |
| Верность | 46–47 | `coc:rule:dark-ages-setting-a-z-loyalty` |
| Магия; Виды магии | 47 | `coc:rule:dark-ages-setting-a-z-magic` |
| Простые чары; Гримуары | 48 | `coc:rule:dark-ages-setting-a-z-magic` |
| Наказание (за магию) | 49 | `coc:rule:dark-ages-setting-a-z-magic` |
| Устная традиция | 49 | `coc:rule:dark-ages-setting-a-z-oral-tradition` |
| Письменные доказательства | 49 | `coc:rule:dark-ages-setting-a-z-written-evidence` |
| Божий суд (виды испытаний) | 49–50 | `coc:rule:dark-ages-setting-a-z-ordeal` |
| Религия | 50–51 | `coc:rule:dark-ages-setting-a-z-religion` |
| Коррупция в Церкви | 51 | `coc:rule:dark-ages-setting-a-z-religion` |
| Монашеская жизнь; Вступление в орден | 51 | `coc:rule:dark-ages-setting-a-z-monastic-life` |
| Монастырские офисы; Другие обязанности; Монастырская иерархия | 52 | `coc:rule:dark-ages-setting-a-z-monastic-life` |
| Святые | 53 | `coc:rule:dark-ages-setting-a-z-saints` |
| Сельская местность | 53 | `coc:rule:dark-ages-setting-a-z-rural` |
| Секретность | 53 | `coc:rule:dark-ages-setting-a-z-secrecy` |
| Крепостное право | 53 | `coc:rule:dark-ages-setting-a-z-serfdom` |
| Рабство | 53 | `coc:rule:dark-ages-setting-a-z-slavery` |
| Сверхъестественное | 53 | `coc:rule:dark-ages-setting-a-z-supernatural` |
| Подозрительность | 54 | `coc:rule:dark-ages-setting-a-z-suspicion` |
| Теория ограниченного блага | 54 | `coc:rule:dark-ages-setting-a-z-theory-of-limited-good` |
| Время | 54 | `coc:rule:dark-ages-setting-a-z-time` |
| Путешествия | 54 | `coc:rule:dark-ages-setting-a-z-travel` |
| Дикая местность | 54 | `coc:rule:dark-ages-setting-a-z-wilderness` |
| (оригинал) врезка «Dark Age Doctrine», EN с. 42 — в русском переводе нет | — | `coc:rule:dark-ages-setting-a-z-dark-age-doctrine` (наш перевод, `translated`) |

## Не взято

- Иллюстрации и подписи к ним (физ. 9, 15, 16, 43, 56, 57 — полностраничные иллюстрации без текста; подписи «Христос на троне», «Керл, крестьянин…», «Лидеры викингов…», «Бандиты ждут в лесах…», «Стена щитов…», «Испытание огнём…», «Сатана», «Копия Ктаат Аквадинген», «Крещение Христа» и т. п.) — оформление без данных.
- Врезка оригинала с выдержкой из письма Фульберта Шартрского и записью соглашения Гуго Лузиньянского с Вильгельмом V Аквитанским (EN с. 37) — в русский перевод не вошла; суть письма Фульберта есть в тексте «Верности», историческая выдержка без механики не переводилась.
- Заговор «For flying venom» (EN с. 39) — в русском переводе на его месте другие обереги (против Дьявола, от боли в конечностях); взят русский набор.
- Ссылки книги на страницы («стр. 191», «стр. 261», «стр. 260», «стр. 48», «стр. 50») оставлены как в переводе; это печатные номера русской вёрстки/оригинала, в базе им соответствуют записи других частей (Тотбург, библиография, святые — ages-totburg, ages-appendices).

## Опечатки и ошибки перевода (в записях)

- «Преступление и возмещение»: «Убийство свободного человека — золото, равное весу человека» (в оригинале — вергельд человека) — `errata`, оставлено как напечатано; «Помещение керла в сточную канаву» (stocks — колодки) — `errata`, исправлено в записи.
- «Общая десятина»: «Сочельник» (Easter Eve — канун Пасхи), «День Святой Троицы» (Pentecost) — `errata`, как напечатано; «Душа шотландца» (Soul Scot — сбор за погребение) — пометка.
- «Инструментарий врача»: правая половина таблицы сдвинута, у Bydene нет назначения, «Комплект» вместо перевода — выровнено по оригиналу (`corrections`).
- «Магия»: Бурхард Вормсский предлагает «снисходительное» наказание — слово пропущено в переводе (`errata`, исправлено).
- Кентербери, «Миф»: «врата неопределённости… дверг» (gates of limbo, the dark ones) — `errata`, исправлено по оригиналу.
- Прочие словесные ошибки перевода (названия монастырских должностей, «Хеофонлик Бога», «пуцелы», «Синдилан», «Катбет», «Ательстан», «хинды», «грабить» вместо «рыхлить граблями», «расквартировать», цитата из «Саги о Ньяле») исправлены молча или с пометкой в `quality.notes` записи (Р-39).
- Карта: «Пиренейское море» — так в переводе (на месте Ирландского моря); оставлено, пометка в черновике карты.

## Ведущему

- Черновик записи карты: `.cache/ages-setting/draft-map-ages-setting-anglo-saxon-england.json` (`coc:map:ages-setting-anglo-saxon-england`, 20 меток городов, `location` — `coc:location:totburg`, которую заводит ages-totburg; картинка уже в `app/maps/ages-setting-anglo-saxon-england.jpg`). Папка `kb/maps/` не входит в файлы этой части.
- Запись области «Англия» не заведена: место без `part_of` может быть только городом (Р-189).
- Когда части ages-investigators и ages-system заведут навыки «Статус», «Чтение и Письмо» и правила устной традиции, стоит добавить ссылки на них в `dark-ages-setting-beot`, `-court-cases`, `-literacy-and-alphabet`, `-a-z-literacy`, `-a-z-written-evidence`, `-a-z-oral-tradition`.
- Кандидаты в записи (сейчас только текст): Собака Одина (Ипсвич), доккальфары (Оксфорд), василиск (Винчестер), Зелёный бог Варренни, семья Валентов (Линкольн).
