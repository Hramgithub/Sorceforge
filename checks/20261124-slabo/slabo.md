# «Слабо» (`slabo-ru`) → записи The Dare (`the-dare-en`) (Р-253, Р-147)

Книги: «Слабо» — официальный русский перевод The Dare (Кевин Росс; редакция Брета Крамера; «Хватай Мачете» Брайана М. Сэммонса; правила «Зова Ктулхненка» Брета Крамера), «Монстры Эдны», © 2020 Sentinel Hill Press / Chaosium; PDF 76 стр. (в выводе `show` — 77, последняя пустая). Оригинал — `the-dare-en` (71 стр.).

Записи остались в `kb/books/the-dare-en/` с прежними id. Русский текст и имена — из «Слабо», числа — по оригиналу; источник `slabo-ru` стоит в `sources` каждой записи первым.

## Смещение страниц «Слабо»

**Печатная = физическая − 7 (`offset: -7`), как у оригинала.** Проверено по номерам на страницах: физ. 8 — «1», физ. 16 — «9», физ. 36 — «29», физ. 47 — «40», физ. 56 — «49». Без номеров: физ. 1–7 (обложка, титул «Слабо», эпиграф «Г.Ф. Лавкрафт», выходные данные, благодарность, оглавление, посвящение), листы прегенов физ. 59–68 (по оглавлению — с. 52–61), раздатка в приложении физ. 75, задняя обложка физ. 76 («i»). Русский текст длиннее: тело сценария в «Слабо» — с. 4–40 (в оригинале 3–35), правила — 41–46 (36–41), «Хватай Мачете» — 47–49 (42–43), «Фото из школьного альбома» — 50–51 (44–45), прегены — 52–61 (46–55), карты — 62–67 (56–61). В `books.json` смещение не правилось.

## Сопоставление книг

«Слабо» — полный перевод того же издания 2020 года: те же главы в том же порядке, те же врезки, те же правила «Зова Ктулхненка» (= The Call of Kid-thulhu), те же 10 прегенов, те же 6 карт (подписи переведены) и раздатка. Сверх оригинала — только сноски переводчика:

- PG и R — американские возрастные рейтинги, «в России обозначаются как 12+» и «16+» (с. 4) — в `scenario/the-dare`;
- названия заклинаний Grand Grimoire: «Гипноз» (Mesmerize, ныне «Мысленное Внушение» — Mental Suggestion), «Общение через Свечи» (Candle Communication), «Вытягивание Сил» (Power Drain), «Утопание Разума» (Drown Mind), «Внедрение Страха» (Implant Fear), «Стать Спектром» (Become Spectral), «Укрощение Животного» (Bind Animal), «Сотворить Грозу» (Create Storm) — в заметках сцен, Эвелин, Растиса, свечей;
- «рояль в кустах» (deus ex machina), «Картина в доме» (The Picture in the House) — в сцене «Гроза»; «Dem Bones» («Их Кости») — в сцене «Кухня»; «Witchcraft and Black Magic» — «Колдовство и Черная Магия» — в альбоме вырезок; «Выставление Штрафа за Просрочку» — «шуточный навык»; «Псевдо-Крысы» вместо «Крысиных Тварей» «Книги хранителя» — «дабы отличить их происхождения» — в записи псевдо-крыс;
- ключ карты туннелей: «Возможно автор ошибся… точки Е… Х… F» — в `map/tunnels-map`, `location/cistern-brickwork`;
- транскрипция раздатки в трех видах (английский оригинал, адаптация на петровское правописание, перевод на современный русский; с. 33) — `text.ru` раздатки = перевод на современный русский, петровская версия — в `description.ru`.

Новых правил, сыщиков или врезок нет, поэтому новых записей не заведено. Всё, что есть в оригинале, есть и в «Слабо»; пометок «нет в «Слабо»» не понадобилось.

## Расхождения чисел и ошибки перевода

Сверка: листы прегенов — по всем числам (скрипт по текстовому слою + изображения физ. 59, 60, 68), статблоки — построчно, кубы, потери Рассудка и проценты всего тела книги — сравнением наборов (`numcmp.py` в рабочей папке). В записях — числа оригинала.

| Где | «Слабо» | Оригинал (The Dare) | В записи |
|---|---|---|---|
| Даррен/Дарлин Пикетт, МОЩ (с. 53) | 60 | POW 65 (с. 47; Рассудок 65 и ПМ 13 на обоих листах) | 65; errata «ошибка перевода» |
| Гарри/Гарриет Энслин, возраст (с. 61) | «11 через неделю» | «10 until next week» (с. 55) | 10; errata «ошибка перевода» |
| Растис, атак в раунд (с. 38) | 1 | 2 (с. 33) | 2; errata |
| Растис, навыки (с. 38) | Прятки 40%, Наблюдательность 50% (строка псевдо-летучих мышей) | Be Sneaky 90%, Gym Class 75%, Notice Stuff 80% (с. 33) | по оригиналу; errata |
| «Разрушая дом»: участок обвала (с. 32) | 5 х 5 и 10 х 10 **дюймов** | 5’ x 5’, 10’ x 10’ (с. 28) | 1,5 × 1,5 и 3 × 3 м; errata «ошибка перевода» |
| «Снаряжение» (с. 45): что нельзя | «не допускается … тупого оружия (клюшка, бита, трость) крупнее перочинного ножа» | «no non-blunt weapons (golf club, baseball bat, walking stick, etc. are ok) bigger than a pocket knife» (с. 40) | текст исправлен по оригиналу; errata «ошибка перевода» |
| Растис, Укус (с. 38) | 35% (17/7) | (17/6) — опечатка оригинала | 17/7 уже было исправлено (Р-35); «Слабо» печатает верно |
| Крысиные стаи, ссылка на «Книгу хранителя» (с. 37) | с. 336 | с. 338 (у мышей — 336) | заметка в `creature/rat-packs` |
| Опечатки оригинала, повторенные в «Слабо» | ЛВК 480 у псевдо-летучей мыши #10; ПЗ 3 у #3; «смесь человека и крысы»; два Уклонения библиотекаря; 1/1d6 у библиотекаря; два урона ножа Роджера; «пять дней» / «две недели»; три значения оглушения Эвелин; «замедляются на X»; «записная книжка … (см. стр. 20)»; ×6 у НАР и ВЫН; метки X/E/F на карте туннелей | — | errata оригинала остаются |

Прочие числа (статблоки Роджера, Эвелин, псевдо-крыс, псевдо-летучих мышей, ужасной псевдо-летучей мыши, библиотекаря; все кубы и потери Рассудка сцен; базы навыков; остальные 9 прегенов) совпадают.

**Ссылки на страницы в тексте «Слабо».** Часть ссылок переводчик пересчитал (стр. 13, 16, 23, 24, 32, 38, 50–51), часть оставил по оригиналу: «стр. 30» (заключительные сцены, в «Слабо» — с. 35), «странице 5» (оружие, с. 6), «стр. 20» (записная книжка, на деле альбом на с. 22–23; ошибка и в оригинале), «стр. 31» (Роджер, с. 36), «стр. 42» (эссе Сэммонса, с. 47). В текстах записей — как напечатано, в `quality.notes` — пометка.

## Записи: что изменено

Во всех 148 записях: источник `slabo-ru` первым, флаг `translated` снят, в `quality.notes` — «Русский текст и имена — по официальному русскому изданию «Слабо»…, числа — по оригиналу» и перечень того, что осталось нашим; в `corrections` — смена `name.ru` (прежнее имя — в `aliases`, у карт — только в `corrections`, схема карт `aliases` не допускает) и замена текстовых полей (`ref` Р-253). Длинные тексты (описания, легенды, механика, правила, раздатка, сценарий) — дословно «Слабо»; правки только: кубы `1d6`, «×», кавычки «…», меры в метрах (Р-64), явные опечатки набора («Бонус у урону», «Коплекция», «Повтороной», «пукнтов», «расcвет» и т. п.), сноски-цифры убраны; вступления, набранные в книге прописными, — обычным регистром.

**Осталось нашим (по терминам «Слабо», не перевод с английского, поэтому флаг `translated` снят):** короткие подписи — `when`, `arc.part`, роли участников, `outcome`, `where`/`found_at`/`held_by`, заметки связей, `residence`, `subcategory`, `habitat`, `keeper_hint`, пояснения меток карт; `summary` и `steps` записей правил и шаги сценария; вводная фраза `legend` прегенов; `mechanics` сцен «Использование Растиса», «Гроза», «Проведение сценария», «Завершение сценария»; `encounters` роев летучих мышей; описание гардероба выжженной спальни (в книге — только на карте); вывод о Эллен Роуз = Эвелин (Р-41); `background.secret` (вывод о прежнем имени) и `possessions` Эвелин. Каждая запись перечисляет свое в `quality.notes` («Наш текст (не из «Слабо»): …»).

| Запись | Название | Заменено текстом «Слабо» | Стр. «Слабо» | Ошибки перевода |
|---|---|---|---|---|
| `characters/ace-simmons` | Эйс Симмонс | description.ru, legend.ru | 5, 25, 32, 54 |  |
| `characters/charles-bruckner` | Чарльз/Шарлотта Брукнер → **Чарльз/Шарлотта Бракнер** | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 60 |  |
| `characters/darren-pickett` | Даррен/Дарлин Пикетт | background.description, description.ru, legend.ru, occupation.ru, названия навыков, атак и способностей в statblock | 53 | errata: 1 |
| `characters/donna-briggs` | Донна Бриггс | description.ru, legend.ru | 7, 8, 17, 22 |  |
| `characters/eliza-fowler` | Элайза Фаулер → **Элиза Фаулер** | description.ru | 23 |  |
| `characters/ellen-rawes` | Эллен (Линн) Роуз | description.ru | 23 |  |
| `characters/erastus-bishop` | Эрастус Бишоп | description.ru | 23 |  |
| `characters/evelyn-barnaker` | Эвелин Барнакер | description.ru, legend.ru, названия навыков, атак и способностей в statblock | 40, 39, 7, 8, 17, 28, 29, 30, 32 |  |
| `characters/harry-enslin` | Гарри/Гарриет Энслин | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 61 | errata: 1 |
| `characters/jay-thurston` | Джулиус (Джей)/Джулия Тёрстон → **Джулиус (Джей)/Джулия Терстон** | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 57 |  |
| `characters/joe-bachman` | Джо/Джолин Бакман → **Джо/Джолин Бахман** | background.description, description.ru, legend.ru, occupation.ru, названия навыков, атак и способностей в statblock | 58 |  |
| `characters/joey-delafano` | Джоуи (Джозеф/Джозефина) Делафано | background.description, description.ru, legend.ru, occupation.ru, названия навыков, атак и способностей в statblock | 54 |  |
| `characters/john-rawes` | Джон Роуз | description.ru | 23 |  |
| `characters/kyle-robards` | Кайл/Кайли Робардс | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 52 |  |
| `characters/mr-briggs` | Мистер Бриггс | description.ru, legend.ru | 7, 8, 16, 22 |  |
| `characters/mrs-ward` | Миссис Уорд | description.ru | 12 |  |
| `characters/old-danny` | Старый Дэнни → **Старик Дэнни** | description.ru, legend.ru | 15, 22, 30, 32 |  |
| `characters/paul-laughlin` | Пол/Полин Логлин → **Пол/Полин Лафлин** | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 56 |  |
| `characters/rich-davis` | Рич/Рейчел Дэвис → **Рич/Рэйчел Дэвис** | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 55 |  |
| `characters/roger-simmons` | Роджер Симмонс | description.ru, legend.ru, background.secret, названия навыков, атак и способностей в statblock | 36, 8, 6, 32, 51 |  |
| `characters/sherwood-kent` | Шервуд/Ширли Кент | background.description, description.ru, legend.ru, occupation.ru, possessions, названия навыков, атак и способностей в statblock | 59 |  |
| `creatures/bat-swarms` | Стаи летучих мышей («На спор») → **Рои летучих мышей («Слабо»)** | description.ru, abilities[0].summary, abilities[1].summary | 37, 17, 23 |  |
| `creatures/bat-things` | Нетопыриные твари → **Псевдо-летучие мыши** | description.ru, encounters.ru, названия навыков, атак и способностей в statblock | 38, 23 |  |
| `creatures/corpse-lights` | Трупные огни → **Трупные огоньки** | description.ru, encounters.ru | 21, 20 |  |
| `creatures/evelyn-rat-things` | Крысиные твари Эвелин → **Псевдо-крысы** | description.ru, encounters.ru, названия навыков, атак и способностей в statblock | 37, 38, 7, 24, 28, 33 |  |
| `creatures/rastis` | Растис | description.ru, legend.ru, encounters.ru, названия навыков, атак и способностей в statblock | 38, 39, 19, 16, 11, 8, 32, 35 | errata: 2 |
| `creatures/rat-packs` | Стаи крыс («На спор») → **Крысиные стаи («Слабо»)** | description.ru, abilities[0].summary, encounters.ru | 37, 33, 12 |  |
| `creatures/rat-thing-librarian` | Крысиная тварь-библиотекарь → **Псевдо-крыса-библиотекарь** | description.ru, encounters.ru, названия навыков, атак и способностей в statblock | 24, 25, 26 |  |
| `creatures/skin-servitor` | Кожаный слуга | description.ru, abilities[0].summary, abilities[1].summary, abilities[2].summary, encounters.ru | 39, 36, 32 |  |
| `creatures/terrible-bat-thing` | Ужасная нетопыриная тварь → **Ужасная псевдо-летучая мышь** | description.ru, encounters.ru, названия навыков, атак и способностей в statblock | 20, 23 |  |
| `handouts/handout-1-grimoire-page` | Раздатка 1: страница гримуара Эвелин → **Раздаточный материал №1: страница гримуара Эвелин** | text.ru, description.ru | 33, 34, физ. 75, 26, 27 |  |
| `items/ace-revolver` | Револьвер Эйса | description.ru, mechanics.ru | 25 |  |
| `items/briggs-photo` | Фотография семьи Бриггс | description.ru | 16 |  |
| `items/briggs-scrapbook` | Альбом вырезок мистера Бриггса | description.ru, mechanics.ru | 22, 23, 7, 28 |  |
| `items/cloth-doll` | Тряпичная кукла-двойник | description.ru, mechanics.ru | 19 |  |
| `items/evelyn-portrait` | Портрет Эвелин Барнакер | description.ru, mechanics.ru | 28, 29 |  |
| `items/fat-candles` | Свечи из человеческого жира | description.ru, mechanics.ru | 13, 24 |  |
| `items/fireplace-poker` | Каминная кочерга | description.ru, mechanics.ru | 16, 28 |  |
| `items/front-door-key` | Ключ от парадной двери | description.ru, mechanics.ru | 13, 25 |  |
| `items/hand-of-glory` | Рука славы Старого Дэнни → **Рука славы Старика Дэнни** | description.ru, mechanics.ru | 30, 31, 22, 39 |  |
| `items/house-mirrors` | Зеркала дома Барнакеров | description.ru, mechanics.ru | 15, 16, 17, 21, 24, 28, 39 |  |
| `items/jar-of-eyes` | Банка с глазами | description.ru, mechanics.ru | 25 |  |
| `items/kerosene-can` | Ржавая канистра керосина | description.ru, mechanics.ru | 9 |  |
| `items/kitchen-knives` | Кухонные ножи | description.ru, mechanics.ru | 15, 21 |  |
| `items/old-danny-effects` | Вещи на теле Старого Дэнни → **Вещи на теле Старика Дэнни** | description.ru, mechanics.ru | 22 |  |
| `items/old-danny-knapsack` | Рюкзак Старого Дэнни → **Рюкзак Старика Дэнни** | description.ru | 15 |  |
| `items/shed-tools` | Инструменты из сарая Барнакеров | description.ru, mechanics.ru | 9, 6, 12 |  |
| `items/silver-coin-collection` | Коллекция старых монет → **Коллекция старинных монет** | description.ru, mechanics.ru | 21, 28 |  |
| `items/telescope` | Маленький телескоп | description.ru, mechanics.ru | 21 |  |
| `locations/barnaker-attic` | Чердак дома Барнакеров | description.ru | 23, 26, 65 |  |
| `locations/barnaker-back-entryway` | Задняя прихожая дома Барнакеров | description.ru | 13, 14, 63 |  |
| `locations/barnaker-basement-bedroom-closet` | Чулан подвальной спальни → **Гардероб спальни в подвале** | description.ru | 28, 27, 66 |  |
| `locations/barnaker-basement-bedroom` | Спальня в подвале | description.ru | 27, 28, 27, 66 |  |
| `locations/barnaker-basement` | Подвал дома Барнакеров | description.ru | 24, 27, 66 |  |
| `locations/barnaker-bathroom` | Ванная дома Барнакеров → **Ванная комната дома Барнакеров** | description.ru | 16, 18, 64 |  |
| `locations/barnaker-boys-bedroom-closet` | Чулан спальни мальчика → **Гардероб спальни мальчика** | description.ru | 21, 18, 64 |  |
| `locations/barnaker-boys-bedroom` | Спальня мальчика | description.ru | 21, 18, 64 |  |
| `locations/barnaker-cistern` | Цистерна за домом Барнакеров | description.ru | 11, 12, 10, 62 |  |
| `locations/barnaker-coal-room` | Угольная дома Барнакеров → **Угольное помещение дома Барнакеров** | description.ru | 25, 27, 66 |  |
| `locations/barnaker-cupola` | Купол дома Барнакеров | description.ru | 20, 21, 26, 65 |  |
| `locations/barnaker-dining-room` | Столовая дома Барнакеров → **Обеденная комната дома Барнакеров** | description.ru | 15, 14, 63 |  |
| `locations/barnaker-entry-hall` | Прихожая дома Барнакеров | description.ru | 13, 14, 63 |  |
| `locations/barnaker-fence` | Ограда дома Барнакеров → **Забор дома Барнакеров** | description.ru | 9 |  |
| `locations/barnaker-fish-pond` | Пруд за домом Барнакеров → **Пруд с рыбой за домом Барнакеров** | description.ru | 9, 11, 10, 62 |  |
| `locations/barnaker-front-porch` | Парадное крыльцо дома Барнакеров | description.ru | 12, 10, 62, 14, 63 |  |
| `locations/barnaker-girls-bedroom` | Спальня девочки | description.ru | 17, 18, 64 |  |
| `locations/barnaker-girls-room-closet` | Чулан спальни девочки → **Гардероб спальни девочки** | description.ru | 17, 18, 64 |  |
| `locations/barnaker-house` | Дом Барнакеров | description.ru, history.ru | 7, 8, 12, 10, 62 |  |
| `locations/barnaker-kitchen` | Кухня дома Барнакеров | description.ru | 13, 25, 14, 63 |  |
| `locations/barnaker-large-attic-space` | Большое чердачное помещение | description.ru | 22, 23, 26, 65 |  |
| `locations/barnaker-living-room` | Общая комната дома Барнакеров → **Гостиная дома Барнакеров** | description.ru | 16, 14, 63 |  |
| `locations/barnaker-master-bedroom-closet` | Большой чулан хозяйской спальни → **Большой гардероб главной спальни** | description.ru | 22, 18, 64 |  |
| `locations/barnaker-master-bedroom` | Хозяйская спальня дома Барнакеров → **Главная спальня дома Барнакеров** | description.ru | 21, 22, 18, 64 |  |
| `locations/barnaker-neighborhood` | Округа дома Барнакеров → **Окрестности дома Барнакеров** | description.ru | 8, 12 |  |
| `locations/barnaker-pantry` | Кладовая в подвале | description.ru | 25, 27, 66 |  |
| `locations/barnaker-parlor` | Гостиная для приёмов дома Барнакеров → **Зал дома Барнакеров** | description.ru | 15, 14, 63 |  |
| `locations/barnaker-scorched-bedroom-closet` | Чулан обожжённой спальни → **Гардероб выжженной спальни** | description.ru | 18, 64 |  |
| `locations/barnaker-scorched-bedroom` | Обожжённая спальня → **Выжженная спальня** | description.ru | 21, 18, 64 |  |
| `locations/barnaker-sewing-room-closet` | Чулан швейной комнаты | description.ru | 19, 18, 64 |  |
| `locations/barnaker-sewing-room` | Швейная комната | description.ru | 19, 20, 18, 64 |  |
| `locations/barnaker-shed` | Сарай во дворе Барнакеров | description.ru | 9, 10, 62 |  |
| `locations/barnaker-small-attic-space` | Малое чердачное помещение → **Небольшое чердачное помещение** | description.ru | 17, 26, 65 |  |
| `locations/barnaker-study` | Кабинет в подвале | description.ru | 25, 26, 27, 66 |  |
| `locations/barnaker-upper-hall` | Верхний коридор дома Барнакеров | description.ru | 16, 17, 18, 64 |  |
| `locations/barnaker-workroom` | Мастерская в подвале | description.ru | 24, 27, 66 |  |
| `locations/barnaker-yard` | Двор дома Барнакеров | description.ru | 9 |  |
| `locations/beneath-the-basement` | Под подвалом: нора Эвелин → **Под подвалом** | description.ru | 29, 31, 67 |  |
| `locations/bone-heap` | Груда костей в норе | description.ru | 31, 29, 67 |  |
| `locations/cistern-brickwork` | Кирпичная кладка цистерны | description.ru | 31, 32, 67 |  |
| `locations/evelyn-alcove` | Ниша Эвелин | description.ru | 29, 30, 31 |  |
| `locations/hometown` | Родной город юных сыщиков → **Родной город детей-сыщиков** | description.ru | 5, 7, 6 |  |
| `locations/porch-tunnel` | Туннель к люку под крыльцом | description.ru | 29, 31, 39, 67 |  |
| `locations/tunnel-entry-chamber` | Малая земляная комната под решёткой → **Небольшое помещение под решеткой** | description.ru | 29, 31, 67 |  |
| `locations/under-porch` | Подполье под крыльцом → **Под крыльцом** | description.ru | 12, 27, 66 |  |
| `maps/attic-map` | План чердака дома Барнакеров → **Карта чердака дома Барнакеров** | названия навыков, атак и способностей в statblock | 26, 65 |  |
| `maps/basement-map` | План подвала дома Барнакеров → **Карта подвала дома Барнакеров** | названия навыков, атак и способностей в statblock | 27, 66 |  |
| `maps/exterior-map` | Карта участка дома Барнакеров → **Карта окрестностей дома Барнакеров** | названия навыков, атак и способностей в statblock | 10, 62 |  |
| `maps/ground-floor-map` | План первого этажа дома Барнакеров → **Карта первого этажа дома Барнакеров** | названия навыков, атак и способностей в statblock | 14, 63 |  |
| `maps/tunnels-map` | План туннелей под домом Барнакеров → **Карта туннелей под домом Барнакеров** | названия навыков, атак и способностей в statblock | 31, 67 |  |
| `maps/upper-floor-map` | План второго этажа дома Барнакеров → **Карта второго этажа дома Барнакеров** | названия навыков, атак и способностей в statblock | 18, 64 |  |
| `rules/call-of-kid-thulhu` | Зов Кид-тулху: упрощённые правила для «На спор» → **Зов Ктулхненка: упрощенные НРИ правила для «Слабо»** | text.ru, summary.ru | 41, 42 |  |
| `rules/grab-the-machete` | Хватай мачете: уроки фильмов ужасов 1980-х → **Хватай мачете, или Как я научился не сходить с ума и полюбил фильмы ужасов 80-х** | text.ru, summary.ru, названия навыков, атак и способностей в statblock | 47, 48, 49 |  |
| `rules/kid-combat` | Зов Кид-тулху: бой → **Зов Ктулхненка: бой** | text.ru, summary.ru | 44 |  |
| `rules/kid-creating-investigator` | Зов Кид-тулху: создание юного сыщика → **Зов Ктулхненка: создание собственного ребенка-сыщика** | text.ru, summary.ru | 46 |  |
| `rules/kid-equipment` | Зов Кид-тулху: снаряжение → **Зов Ктулхненка: снаряжение** | text.ru, summary.ru | 45 | errata: 1 |
| `rules/kid-injury` | Зов Кид-тулху: ранения → **Зов Ктулхненка: повреждения** | text.ru, summary.ru | 44 |  |
| `rules/kid-pushing-rolls` | Зов Кид-тулху: повторная проверка → **Зов Ктулхненка: повторные проверки** | text.ru, summary.ru, examples[0] | 44, 45 |  |
| `rules/kid-roleplaying-80s` | Зов Кид-тулху: играем ребёнка 80-х → **Зов Ктулхненка: отыгрыш ребенка 80-х** | text.ru, summary.ru | 45, 46 |  |
| `rules/kid-sanity` | Зов Кид-тулху: Рассудок → **Зов Ктулхненка: Рассудок** | text.ru, summary.ru, examples[0] | 44 |  |
| `rules/kid-skill-rolls` | Зов Кид-тулху: как работают проверки навыков → **Зов Ктулхненка: как работают проверки навыком** | text.ru, summary.ru | 43, 44 |  |
| `rules/kid-skills` | Зов Кид-тулху: навыки → **Зов Ктулхненка: навыки** | text.ru, summary.ru, examples[0], названия навыков, атак и способностей в statblock | 42, 43 |  |
| `rules/kid-statistics` | Зов Кид-тулху: характеристики → **Зов Ктулхненка: характеристики** | text.ru, summary.ru | 42 |  |
| `scenarios/the-dare` | На спор → **Слабо** | summary.ru, keeper_info.ru, hook.ru, advice.ru, conclusion.ru, названия навыков, атак и способностей в statblock | физ. 1, физ. 4, физ. 5, физ. 6, физ. 7, 1, 2, 4, 5, 6, 7, 8, 35, физ. 76 |  |
| `scenes/ace-arrives` | Появляется Эйс | description.ru, mechanics.ru | 25 |  |
| `scenes/attic` | Чердак и крыша → **Чердак** | description.ru, mechanics.ru | 23 |  |
| `scenes/basement-bedroom` | Подвальная спальня: портрет → **Спальня (подвал)** | description.ru, mechanics.ru | 27, 28 |  |
| `scenes/basement` | Подвал и мастерская → **Подвал** | description.ru, mechanics.ru | 24 |  |
| `scenes/battle-against-evelyn` | Битва с Эвелин → **Битва против Эвелин** | description.ru, mechanics.ru, arc.part | 31, 32, 33 | errata: 1 |
| `scenes/beneath-the-basement` | Под подвалом: логово Эвелин → **Под подвалом** | description.ru, mechanics.ru, arc.part | 29, 30, 31 |  |
| `scenes/boys-bedroom` | Спальня мальчика | description.ru, mechanics.ru, arc.part | 21 |  |
| `scenes/cistern` | Цистерна | description.ru, mechanics.ru, arc.part | 11, 12 |  |
| `scenes/closing-scenes` | Финал: заключительные сцены → **Завершение сценария: заключительные сцены** | description.ru, mechanics.ru, arc.part | 35 |  |
| `scenes/coal-room-pantry` | Угольная и кладовая → **Угольное помещение и кладовая** | description.ru, mechanics.ru | 25 |  |
| `scenes/cupola` | Купол: трупные огни → **Купол** | description.ru, mechanics.ru, arc.part | 20, 21, 16 |  |
| `scenes/dining-room` | Столовая → **Обеденная комната** | description.ru, mechanics.ru, arc.part | 15 |  |
| `scenes/entry-hall` | Прихожая и задняя прихожая → **Прихожая** | description.ru, mechanics.ru, arc.part, outcome.ru | 13 |  |
| `scenes/exterior` | Осмотр дома снаружи → **Внешний вид дома Барнакеров** | description.ru, mechanics.ru, arc.part, outcome.ru | 8, 9 |  |
| `scenes/fighting-evelyn` | Как сражаться с Эвелин → **Сражение с Эвелин** | description.ru, mechanics.ru, arc.part | 28 |  |
| `scenes/fish-pond` | Пруд → **Пруд с рыбой** | description.ru, mechanics.ru, arc.part | 9, 11 |  |
| `scenes/front-porch` | Парадное крыльцо и подполье → **Парадное крыльцо** | description.ru, mechanics.ru, arc.part | 12, 39 |  |
| `scenes/girls-bedroom` | Спальня девочки и малый чердак → **Спальня девочки** | description.ru, mechanics.ru, arc.part | 17 |  |
| `scenes/interior` | Внутри дома: общее → **Интерьер: общие сведения** | description.ru, mechanics.ru, arc.part, outcome.ru | 5, 6, 12, 13 |  |
| `scenes/kitchen` | Кухня: кости и телефон → **Кухня** | description.ru, mechanics.ru, arc.part | 13, 15 |  |
| `scenes/large-attic-space` | Большое чердачное помещение: альбом Бриггса → **Большое чердачное помещение** | description.ru, mechanics.ru | 22, 23 |  |
| `scenes/living-room` | Общая комната: Растис → **Гостиная** | description.ru, mechanics.ru, arc.part | 16 |  |
| `scenes/master-bedroom` | Хозяйская спальня: тело Старого Дэнни → **Главная спальня** | description.ru, mechanics.ru, arc.part | 21, 22 |  |
| `scenes/meeting-at-the-house` | У дома Барнакеров: спор → **Проведение сценария** | description.ru, mechanics.ru, arc.part, outcome.ru | 5, 7, 8 |  |
| `scenes/parlor` | Гостиная для приёмов → **Зал** | description.ru, mechanics.ru, arc.part | 15, 16 |  |
| `scenes/scorched-bedroom` | Обожжённая спальня → **Выжженная спальня** | description.ru, mechanics.ru, arc.part | 21 |  |
| `scenes/sewing-room` | Швейная комната | description.ru, mechanics.ru, arc.part | 19, 20 |  |
| `scenes/shed` | Сарай | description.ru, mechanics.ru, arc.part, outcome.ru | 9, 11 |  |
| `scenes/storm` | Колдовская буря → **Гроза** | description.ru, arc.part | 6 |  |
| `scenes/study` | Кабинет: крыса-библиотекарь → **Кабинет** | description.ru, mechanics.ru | 25, 26, 27 |  |
| `scenes/sympathy-for-the-devil-spawn` | Сочувствие к дьявольскому отродью | description.ru, mechanics.ru | 24, 33 |  |
| `scenes/upper-floor` | Второй этаж: ванная и верхний коридор → **Второй этаж: общие сведения** | description.ru, mechanics.ru, arc.part | 7, 16, 17 |  |
| `scenes/using-rastis` | Проделки Растиса → **Использование Растиса** | description.ru, mechanics.ru, arc.part | 19, 6, 7 |  |
| `tomes/evelyn-grimoire` | Гримуар Эвелин | description.ru | 25, 26, 27, 24 |  |
| `tomes/evelyn-spellbook` | Книга заклинаний Эвелин | description.ru | 39, 40, 30 |  |

## Глоссарий: официальные формы «Слабо» (English → Russian)

Прежние формы нашего перевода (`checks/20261116-dare/dare.md`) — в `aliases` записей. Для базы терминов (`kb/terms/`, Р-184) — кандидаты, сами записи `term` не заводились.

| English | «Слабо» | Прежде (наш перевод) |
|---|---|---|
| The Dare | Слабо | На спор |
| I Double-Dog Dare Ya | А спорим тебе слабо? | — |
| kid investigator | ребенок-сыщик, дети-сыщики (также «юные сыщики») | юный сыщик |
| The Call of Kid-thulhu | Зов Ктулхненка | Зов Кид-тулху |
| Simplified RPG Rules for The Dare | упрощенные НРИ правила для «Слабо» | упрощённые правила для «На спор» |
| Be a Pal | Дружба | Быть другом |
| Be Bossy | Лидерство | Командовать |
| Be Sneaky | Прятки | Красться |
| Dodge | Уклонение | Уклонение |
| Fighting (Brawl) | Драка; в статблоках — Ближний бой (Драка) | Драка |
| First Aid | Первая помощь | Первая помощь |
| Fix Stuff | Очумелые Ручки | Чинить вещи |
| Gym Class | Уроки Физкультуры (на листе — «Уроки Физ-ры») | Физкультура |
| Nature | Окружающий Мир | Природа |
| Notice Stuff | Наблюдательность | Замечать всякое |
| Play with Matches | Игра со Спичками | Играть со спичками |
| Reading, Writing, and Arithmetic | Чтение, Письмо и Арифметика | Чтение, письмо и счёт |
| Science Class | Уроки Науки | Школьные науки |
| Spooky Stuff | Ужастики | Жуткие штуки |
| Taunt | Задира | Дразнить |
| Spawn Vermin | Породить Вредителя | Порождать паразитов |
| Issue Late Fees | Выставление Штрафа за Просрочку | Выписывать штрафы за просрочку |
| BB Gun | Пневматический пистолет («пневм. пистолет») | Пневматическая винтовка |
| Freak Out | Офигивать, Офигивание | Психануть |
| Totally Lose It | Окончательно Едет Крыша | Совсем слететь с катушек |
| Major Wound | Серьезная Рана | серьёзная рана |
| Push (a roll) | Повторная Проверка, Повторить | повторная проверка |
| Kid (profession) | Ребенок | Ребёнок |
| Kid Investigator (1980s) (лист) | Ребенок-Сыщик (1980-е) | — |
| Nickname / Who Are You? / What Do Others Know About You? | Прозвище / Кто ты? / Что Другие Знают о Тебе? | — |
| fraidy-cat(s) | трусишка, «как кучка трусишек» | трусишка |
| Rat-thing | псевдо-крыса (сноска: в «Книге хранителя» — крысиная тварь) | крысиная тварь |
| Bat-thing | псевдо-летучая мышь | нетопыриная тварь |
| ‘thing’ | «псевдо-тварь», «тварь» | тварь |
| The Terrible Bat-Thing | Ужасная Псевдо-Летучая Мышь | Ужасная нетопыриная тварь |
| The Rat-Thing Librarian | Псевдо-крыса Библиотекарь | Крысиная тварь-библиотекарь |
| Rat Packs / Bat Swarms | Крысиные Стаи / Рои Летучих Мышей | стаи крыс / стаи летучих мышей |
| Skin Servitor | Кожаный Слуга | кожаный слуга |
| corpse lights / will-o’-the-wisps | трупные огоньки / Блуждающие Огоньки | трупные огни / блуждающие огоньки |
| familiar | фамильяр | фамильяр |
| Grandmother Illusion | Иллюзия бабушки | Бабушкин морок |
| Devour (mnvr) | Пожирание (маневр) | Пожирание (манёвр) |
| Carry off (mnvr) | Похищение (маневр) | Унести (манёвр) |
| Shriek | Визг | Визг |
| Rake | Раздирание | Задние когти |
| Human Speech / Psychic Link | Человеческая Речь / Психическая Связь | Человеческая речь / Мысленная связь |
| Hand of Glory | Рука Славы | Рука славы |
| Black Man | Черный Человек | Чёрный человек |
| Create Skin Servitor | Создать Кожаного Слугу | Создание кожаного слуги |
| Dampen Flame | Погасить Пламя | Притушить пламя |
| See Through Mirrors | Видеть Сквозь Зеркала | Взгляд сквозь зеркала |
| Seal House | Запечатать Дом | Запечатать дом |
| Mesmerize | Гипноз | Заворожить |
| Power Drain | Вытягивание Сил | Истощение сил |
| Wrack | Разрушение | Разрушение |
| Evil Eye | Сглаз | Сглаз |
| Cloud Memory | Затуманить Память | Затуманить память |
| Drown Mind | Утопание Разума | Утопить разум |
| Implant Fear | Внедрение Страха | Зародить страх |
| Become Spectral | Стать Спектральным (сноска — «Стать Спектром») | — |
| Bind Animal | Укрощение Животного | — |
| Call the Black Man | Вызов Черного Человека | — |
| Candle Communication | Общение через Свечи | Свечная связь |
| Create Storm | Сотворить Грозу | — |
| The Storm | Гроза | Колдовская буря |
| Running The Dare | Проведение Сценария | — |
| Controlling the Pace | Контроль Темпа | — |
| Setting Note | Примечание об Обстановке | — |
| PG / R | PG / R (12+ / 16+) | версия «PG» / «R» |
| Roger’s Actions | Поведение Роджера | Действия Роджера |
| Barnaker House | дом Барнакеров | дом Барнакеров |
| The Neighborhood | Окрестности | округа |
| Exterior / The Exterior of the Barnaker House | Снаружи / Внешний вид дома Барнакеров | — |
| Fence / The Yard / The Shed / The Fish Pond / The Cistern / The Front Porch | Забор / Двор / Сарай / Пруд с Рыбой / Цистерна / Парадное Крыльцо | ограда / двор / сарай / пруд / цистерна / парадное крыльцо |
| Under Porch / Back Porch | Под Крыльцом / Заднее Крыльцо | подполье под крыльцом / заднее крыльцо |
| The Interior / Smell / Noises / Lighting | Интерьер / Запах / Шумы / Освещение | — |
| Entry Hall / Back Entryway | Прихожая / Задняя Прихожая | прихожая / задняя прихожая |
| Kitchen / Dining Room / Parlor / Living Room (Family Room) | Кухня / Обеденная Комната / Зал / Гостиная (на карте «Гостинная») | кухня / столовая / гостиная для приёмов / общая комната |
| Upper Floor / Landing / Bathroom / Top of the Stairs / Upper Hall | Второй Этаж / Лестничная площадка / Ванная Комната / Наверху Лестницы / Верхний Коридор | второй этаж / площадка / ванная / верх лестницы / верхний коридор |
| Through a Mirror, Dark Magically | Сквозь Зеркало, Темное Магически | Через тёмное зеркало |
| Foreshadowing, Literally | Предзнаменование, Буквально | Предвестие, в буквальном смысле |
| Girl’s Bedroom / Girl’s Room Closet | Спальня Девочки / Гардероб Спальни Девочки | спальня девочки / чулан спальни девочки |
| Small / Large Attic Space | Небольшое / Большое Чердачное Помещение | малое / большое чердачное помещение |
| Sewing Room / Sewing Room Closet | Швейная Комната / Чулан Швейной Комнаты | швейная комната / чулан |
| Using Rastis | Использование Растиса | Проделки Растиса |
| Tricks and Traps / Theft / Voice in the Dark / Cat Scare and Ambush | Уловки и Ловушки / Кража / Голос во Тьме / Кошачий Испуг и Засада | — |
| Cupola / An Alternative Encounter | Купол / Альтернативное Столкновение | купол / другой вариант встречи |
| Scorched Bedroom | Выжженная Спальня (на карте «Выжженая») | обожжённая спальня |
| Boy’s Bedroom / Master Bedroom / Large Closet | Спальня Мальчика / Главная Спальня / Большой Гардероб | спальня мальчика / хозяйская спальня / большой чулан |
| closet | гардероб (у швейной комнаты — чулан) | чулан |
| Sympathy for the Devil-Spawn | Сочувствие к Дьявольскому Отродью | Сочувствие к дьявольскому отродью |
| Rescue / Guide / Advisor | Спасение / Проводник / Советник | Спасение / Проводник / Советчик |
| The Attic | Чердак | чердак |
| The Basement / Workroom / Furnace / Metal Grate | Подвал / Мастерская / Печь / Металлическая Решетка | подвал / мастерская / печь / решётка |
| Optional Encounter: Ace Arrives | Опциональное столкновение: Появляется Эйс | Появляется Эйс |
| Coal Room / Pantry / The “Study” / Bedroom | Угольное Помещение / Кладовая / «Кабинет» / Спальня | угольная / кладовая / кабинет / подвальная спальня |
| Fighting Evelyn | Сражение с Эвелин | Как сражаться с Эвелин |
| Silver and Iron / Fire / Connection to Rastis / Reflection | Серебро и Железо / Огонь / Связь с Растисом / Отражение | — |
| Beneath the Basement | Под Подвалом | под подвалом |
| Tunnels Map Key | Ключ к Карте Туннелей | — |
| The Battle Against Evelyn | Битва Против Эвелин | Битва с Эвелин |
| Roger (and other reanimated corpses) / Rats and Bats | Роджер (и другие ожившие трупы) / Крысы и Летучие Мыши | — |
| Bringing Down the House | Разрушая Дом | Обрушить дом |
| Ending the Scenario: Closing Scenes (Loss, Draw, Win) | Завершение Сценария: Заключительные Сцены (Поражение, Ничья, Победа) | Финал: заключительные сцены |
| Creature and Character Statistics | Характеристики Существ и Персонажей | — |
| Handout #1 | Раздаточный Материал №1 | раздатка 1 |
| Exterior / Ground Floor / Upper Floor / Attic / Basement / Tunnels Map | Карта Окрестностей / Первого Этажа / Второго Этажа / Чердака / Подвала / Туннелей | карта участка / план … |
| Grab the Machete | Хватай Мачете | Хватай мачете |
| Yearbook Photos | Фото из Школьного Альбома | Фото из школьного альбома |
| Pre-Generated Kid Investigators | Готовые Листы Детей Сыщиков | — |
| Roger Simmons, vindictive bully and undead thing | Роджер Симмонс, мстительный хулиган и нежить | мстительный задира и нежить |
| Evelyn Barnaker, deathless, child-eating witch and living nightmare | бессмертная ведьма, пожирающая детей, и кошмар во плоти | бессмертная ведьма-людоедка |
| Rastis, Evelyn’s feline familiar | Растис, кошачий фамильяр Эвелин | — |
| Ace | Эйс | Эйс |
| Old Danny | Старик Дэнни | Старый Дэнни |
| Eliza Fowler / Erastus Bishop | Элиза Фаулер / Эрастус Бишоп | Элайза Фаулер / Эрастус Бишоп |
| John Rawes / Ellen (Lynn) Rawes | Джон Роуз / Эллен (Линн) Роуз | — |
| Governor Phips / Rex / Mrs. Ward | губернатор Фиппс / Рекс / миссис Уорд | губернатор Фипс / Рекс / миссис Уорд |
| Kyle/Kylie Robards — The Bookworm | Кайл/Кайли Робардс — Книжный червь | — |
| Darren/Darlene Pickett — The Athlete | Даррен/Дарлин Пикетт — Спортсмен(ка) | Спортсмен |
| Joey (Joseph/Josephine) Delafano — The Tough | Джоуи (Джозеф/Джозефина) Делафано — Крутой/Крутая | Крутой |
| Rich/Rachel Davis — The Side Kick | Рич (Ричард, Ричи)/Рэйчел Дэвис — Приятель | Рич/Рейчел Дэвис — Напарник |
| Paul/Pauline Laughlin — The Prankster | Пол/Полин Лафлин — Приколист(ка) | Пол/Полин Логлин — Шутник |
| Julius (Jay)/Julia Thurston — The Snob | Джулиус (Джей)/Джулия Терстон — Зазнайка | Тёрстон — Сноб |
| Joe/Joelene Bachman — The Poor Kid | Джо/Джолин Бахман — Бедняк | Бакман |
| Sherwood/Shirley Kent — The Boy/Girl Scout | Шервуд/Ширли Кент — Бойскаут/Герлскаут | Скаут |
| Charles/Charlotte Bruckner — The Weirdo | Чарльз/Шарлотта Бракнер — Чудик | Брукнер |
| Harry/Harriette Enslin — The Know It All | Гарри/Гарриет Энслин — Всезнайка | — |
| Halloween Costumes / Roleplaying as an 80s Kid | Костюмы на Хэллоуин / Отыгрыш Ребенка 80-х | — |
| Creating Your Own Kid Investigator / Creating Skills | Создание Собственного Ребенка-Сыщика / Создание Навыков | — |
| Statistics / Skills / How Skill Rolls Work / Bonus and Penalty Dice / Combat / Injury / Sanity / Pushing Rolls / Equipment | Характеристики / Навыки / Как Работают Проверки Навыком / Бонусные и Штрафные Кости / Бой / Повреждения / Рассудок / Повторные Проверки / Снаряжение | — / — / — / — / бой / ранения / Рассудок / повторная проверка / снаряжение |
| films (Grab the Machete) | «Хэллоуин», «Путешествие в Ад» (Tourist Trap), «Зловещие Мертвецы», «Безумец», «Полтергейст», «Ночь Страха», «Муха», «Пятница 13 Часть 6: Джейсон жив!», «Пропащие ребята», «Безумная» (I, Madman) | «Ловушка для туристов», «Я, безумец» |

## Не взято

- Физ. 2 (титульная картинка «Слабо»), физ. 3 (эпиграф «Г.Ф. Лавкрафт»), физ. 10 (окончание предисловия Кевина Росса: «почему такое отзывается у взрослых», подпись «Из района, где жила Эвелин Барнейкер, Сентябрь 2017 года») — без игрового материала; как и в оригинале, из предисловия взяты только эпохи и восстановленная сцена (`scenario/the-dare`, `keeper_info`).
- Физ. 57 и 58 «Фото из школьного альбома» — портреты с шуточными подписями (на английском, как в оригинале); как и прежде, к записям не привязаны (физ. 58 — источник фото «roger simmons» у Роджера). Вопрос владельцу о них — тот же, что в `checks/20261116-dare/dare.md`.
- Благодарность и выходные данные (физ. 5), посвящение (физ. 7) — только источниками сценария; шуточные отзывы задней обложки — нет.
- Английский текст раздатки и ее адаптация на петровское правописание в `text.ru` не взяты: `text.ru` — перевод «Слабо» на современный русский, петровская версия — в `description.ru`.

## Не сделано / вопросы ведущему

1. Смещение `slabo-ru` в `pipeline/source/books.json` — `offset: -7` (не правилось по заданию).
2. Флаг `translated` снят у всех 148 записей: весь переведенный с английского текст заменен текстом «Слабо»; оставшиеся наши подписи и выжимки — не перевод, а пересказ по «Слабо», они перечислены в `quality.notes` каждой записи. Если «наше» тоже должно нести флаг — вернуть его у записей, где в `quality.notes` есть «Наш текст (не из «Слабо»)» с полями крупнее подписей (правила: `summary`, `steps`; сценарий: `steps`; сцены «Использование Растиса», «Гроза»; Эллен Роуз; гардероб выжженной спальни).
3. Названия заклинаний в `statblock.spells.items` Эвелин и Растиса оставлены по оригиналу (по ним ссылки на справочник); русские формы «Слабо» — в заметках. Справочник заклинаний (`kb/spells/`) не трогался: «Гипноз», «Вытягивание Сил» и др. — кандидаты в `aliases` общих записей заклинаний (предложений не делал: это формы одного перевода сценария, а не «Книги хранителя»).
4. Наш HTML-перевод The Dare в библиотеке пометкой о русском издании не снабжен (вне задания, Р-253 поручает это отдельно).
5. Термины из глоссария выше не заведены записями `term` (Р-184) — кандидаты.
