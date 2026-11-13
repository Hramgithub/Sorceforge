# «Лохмотья Короля» — часть house: сверка покрытия

Книга `lokhmotya-korolya-ru` (RU 7e, официальный перевод; печатная страница = физической). Страницы части: 275–307.
Книга III «Монастырь», глава 12 «Монастырь» (The Upper House), этап `L/scenario/upper-house` (order 13).
Префикс `L/` ниже = `lokhmotya-korolya-ru/`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| «Глава 12. Монастырь» (заголовок-картинка), эпиграфы Лавкрафта, Чемберса, Евреям 10:31 | 275 | `L/scenario/upper-house`: `name`, `advice` (эпиграфы); эпиграф Лавкрафта — также `coc:location:plateau-of-leng`: `history` |
| Дно долины под пещерами (лагерь итальянцев, камень с кровью Дельнегро) | 275 | `L/scene/house-exploring-the-caves`; `L/location/house-drakmar-caves` |
| Исследование пещер | 275–276 | `L/scene/house-exploring-the-caves`; `L/location/house-drakmar-caves` (part_of `L/location/drakmar-drakmar`) |
| Замечания по поводу концовки | 276–277 | `upper-house`: `keeper_info`, `advice` |
| Ночные кошмары (два сна ■) | 277 | `L/scene/house-nightmares`; `L/handout/house-nightmare-butcher`, `L/handout/house-nightmare-thing-in-the-dark` |
| Это ловушка? | 277–278 | `L/scene/house-is-it-a-trap` |
| Ужас с холмов | 278–280 | `L/scene/house-horror-from-the-hills`; `L/location/house-chaugnar-faugn-cavern` |
| План «пещера» (Врата на плато Цанг/Ленг; Чагнар Фан, Роберто Анзалоне, Мири Нигри; путь сыщиков) | 279 | `L/map/house-drakmar-cavern` (`app/maps/tatters-house-drakmar-cavern.jpg`, 4 метки) |
| Чагнар Фан и Мири Нигри | 280 | `L/creature/house-chaugnar-faugn`: `legend`; `L/character/house-tcho-tcho`: `legend` |
| Тчо-Тчо (происхождение, Мустанг, Амепал; внешность и поведение) | 280–281 | `L/character/house-tcho-tcho`: `description`, `legend` |
| Статблок «Жрецы и воины Тчо-Тчо» #1–#6 | 281 | `L/character/house-tcho-tcho` (групповой профиль, варианты #1–#6) |
| Король в желтом и Тчо-Тчо | 282 | `upper-house`: `keeper_info`; `L/character/house-tcho-tcho`: `legend`; `L/creature/house-king-in-yellow`: `legend` |
| Чагнар Фан (врезка; статблок «Чагнар Фагн, Ужас с холмов») | 282–283 | `L/creature/house-chaugnar-faugn` (`instance_of` `coc:creature:chaugnar-faugn`) |
| Роберто Анзалоне (появление, внешность и поведение, Известно, Инсайдерские знания, Сюжет, статблок) | 283–284 | `L/character/roberto-anzalone`; появление и обряд Врат — `L/scene/house-horror-from-the-hills` |
| Врата | 285–286 | `L/scene/house-the-gate`; `L/item/house-drakmar-gate` |
| Плато Ленг | 286 | `L/scene/house-plateau-of-leng`; `coc:location:plateau-of-leng` (новая общая область) |
| Будущие действия Кверри | 286 | `L/character/malcolm-quarrie`: `legend` |
| Малькольм Кверри (внешность, Известно, Инсайдерские знания, Сюжет, статблок, языки) | 287–288 | `L/character/malcolm-quarrie` |
| Беседа с Малькольмом Кверри (три способа ■) | 288–289 | `L/scene/house-conversation-with-malcolm-quarrie` |
| Марш по Ленгу, остановившееся время | 289 | `L/scene/house-plateau-of-leng`; `coc:location:plateau-of-leng` |
| Иллюстрация (шантак над чо-чо) | 290 | не взято (см. ниже) |
| Возможное столкновение: шантаки | 291–292 | `L/scene/house-shantak-encounter` (`coc:creature:shantak`) |
| В дикой местности | 292 | `L/scene/house-in-the-wilderness` |
| Монастырь | 293 | `L/scene/house-the-upper-house`; `L/location/house-upper-house` (здание, part_of `coc:location:plateau-of-leng`) |
| Трубы | 293–294 | `L/scene/house-the-upper-house`; `L/item/house-pipes` |
| Навигация по Монастырю (6 пунктов ■) | 294 | `L/scene/house-navigating-the-upper-house` |
| Коридоры (4 картины ■) | 295 | `L/scene/house-navigating-the-upper-house` |
| Истощение | 295 | `L/scene/house-navigating-the-upper-house` |
| Сердце Монастыря | 295–296 | `L/scene/house-heart-of-the-upper-house`; `L/location/house-heart-of-the-upper-house`; `L/item/house-upper-house-gate` |
| Путь Короля в желтом к Земле | 296 | `L/scene/house-the-king-in-yellow` |
| Король в желтом | 296–297 | `L/scene/house-the-king-in-yellow`; `L/creature/house-king-in-yellow`: `description` |
| Изображение короля в желтом (врезка) | 297–298 | `L/scene/house-the-king-in-yellow`; `L/creature/house-king-in-yellow`: `abilities` |
| Король в желтом (врезка; статблок «Король в желтом, Аватар Хастура») | 298 | `L/creature/house-king-in-yellow` (`instance_of` `coc:creature:king-in-yellow`) |
| Выбор проводника | 298–300 | `L/scene/house-choosing-the-guide` |
| Использование врат | 300 | `L/scene/house-choosing-the-guide`; `L/item/house-upper-house-gate` |
| Шаг на Землю | 300–301 | `L/scene/house-choosing-the-guide` |
| Как остановить Короля в желтом? (вступление) | 301 | `L/scene/house-stopping-the-king-self-sacrifice` |
| Остановить короля: Самопожертвование (стих из «Короля в жёлтом») | 301–302 | `L/scene/house-stopping-the-king-self-sacrifice` |
| Плейтест (врезка) | 302 | `L/scene/house-stopping-the-king-self-sacrifice` (последний абзац); `upper-house`: `advice` (ссылка) |
| Остановить короля: Убийство | 303 | `L/scene/house-stopping-the-king-killing` |
| Остановить короля: Побег | 303–304 | `L/scene/house-stopping-the-king-escape`; `L/item/house-upper-house-gate` |
| Остановить короля: Неповиновение и самоубийство | 304 | `L/scene/house-stopping-the-king-defiance` |
| Послесловие: Следователь в Каркозе | 304–305 | `L/scene/house-investigator-in-carcosa` |
| Последствия: Сыщик в Цанге | 305–306 | `L/scene/house-investigator-in-tsang`; `L/location/house-plateau-of-tsang` |
| Последствия: Король в желтом достигает Земли (4 события ■, литература и театр) | 306–307 | `L/scene/house-king-reaches-earth` |
| Краткое содержание главы | 307 | `upper-house`: `summary` |
| Потери/приобретения рассудка при завершении КНИГИ III | 307 | `upper-house`: `conclusion` и таблица «Потери и приобретения Рассудка за завершение Книги III» |

Новые записи (35): этап 1; персонажи 3 (`malcolm-quarrie`, `roberto-anzalone`, групповой `house-tcho-tcho`); существа 2
(профили книги: Шагнер Фан, Король в жёлтом); места 6 (общая область `coc:location:plateau-of-leng` + `house-drakmar-caves`,
`house-chaugnar-faugn-cavern`, `house-plateau-of-tsang`, `house-upper-house`, `house-heart-of-the-upper-house`); карта 1;
предметы 3 (`house-drakmar-gate`, `house-upper-house-gate`, `house-pipes`); раздаточные 2 (кошмары); сцены 21.
Картинка: `app/maps/tatters-house-drakmar-cavern.jpg` (760×830).

## Не взято

- Иллюстрации и портреты главы: заголовок-картинка (с. 275, название взято), силуэт Шагнер Фана и чо-чо (с. 280), портрет «Professor Anzalone» (с. 282), иллюстрация «In the Cavern With Chaugnar Faugn» (с. 285), портрет Кверри (с. 287), шантак над чо-чо (с. 290), иллюстрация с. 291, Король в жёлтом (с. 299) — картинки без текста; `app/art/` не входит в файлы части. — сделано частично (коммит `207f20a`: чо-чо, Анзалоне, пещера Шагнер Фана, Кверри, шантак, Король в жёлтом).
- Масштабная линейка карты с. 279 («0 15 30 FEET») — меткой не отмечена, пересчёт в `quality.notes` карты.
- Таблиц правил с броском (`kb/tables/tatters-house-*`) на этих страницах нет — не заводились; таблица Рассудка — в этапе.
- Упомянутые без записей: Рэндольф Картер и «Сомнамбулический поиск неведомого Кадата» Лавкрафта (текстом в месте Монастыря), жрец Му Санг, Амепал и сын Агон Сангпо, кочевники Цоцова (текстом у `house-tcho-tcho`), художники и писатели «Последствий» (текстом в сцене), Сара Кверри (текстом). Мири нигри и шантаки — общие записи без своих чисел в книге.

## Опечатки и сомнения

- Шагнер Фан (с. 282–283): бонус к урону +6D6 перенесён из 6-й редакции (по 7-й при СИЛ 325 + ТЕЛ 200 — +9d6); защита от «Загипнотизировать жертву» — «чрезвычайная проверка ВЫН» (в оригинале POW x1, то есть МОЩ); в списке заклинаний нет Create Window, Perfection, Wrack, а вместо Imprison Mind — «Затуманить память»; из брони выпала фраза о 15 минутах до развоплощения — всё `errata`, как напечатано.
- Король в жёлтом (с. 298): в списке заклинаний нет Brew Dream Drug; «все заклинания Призыва/Изгнания» вместо all Summon/Bind — `errata`. Рост: «более восьми футов» (с. 296) и «почти восемь футов» (с. 298). На с. 296 «Покорение» в оригинале — Mesmerize («Зачарование»).
- Карта с. 279: «Мини Нигри» вместо «Мири Нигри» — `note` метки.
- С. 300 «трудным упехом» — характеристика не названа (по оригиналу МОЩ); с. 286 «новым проводников» — по оригиналу новый спутник Шагнер Фана.
- Имена: «Малькольм» (список с. 10) / «Малкольм» / «Кварри» (с. 307) — псевдонимы; «Чагнар Фан» / «Чагнар Фагн» — в базе «Шагнер Фан»; «Тчо-Тчо» — в базе «чо-чо».
- Чо-чо: навыки «Маскировка» (Hide) и «Красться» (Sneak) связаны со Скрытностью; копьё 1d8+1 оружию справочника не сопоставлено.
- Плато Ленг и плато Цанг: в задании Ленг — область с `part_of: null`, но `tools/check.py` не пропускает область без родителя (Р-189, Р-197); родитель обеих — `L/location/drakmar-drakmar-valley` («Дракмар-ин-Тсанг, на пороге плато Ленг», с. 274). **Вопрос владельцу**: какой родитель нужен общей области Ленга (другие книги — Страна снов).
- Даты Кверри: введение (с. 15) — отъезд в Милан в начале 1926 года, приложение A (с. 313) — март 1927 года с Вильерсом; в записи — «в начале 1926 года» по введению.

## Ссылки на записи других частей

На момент проверки все цели существуют (`drakmar-drakmar`, `drakmar-drakmar-valley`, `drakmar-kag`, `drakmar-monastery-te`,
`india-mustang`, `india-riccardo-delnegro`, `organization/india-tcho-tcho-of-drakmar`, `carlo-schippone`, `carcosa-*`, `noss`,
`yolanda`, `scenario/to-drakmar`, `scenario/carcosa`). Связи Кверри с Хиллари, Грести, Аткинсоном, Вильерсом, Кроули, Роби и
Скиппоне и Анзалоне с Вильерсом, Коломбо, Скиппоне и Дельнегро хранятся в их записях и не дублировались.

## Предложения

`checks/20261113-tatters/proposals-house.json` — 18 правок: 16 псевдонимов общих записей (`coc:creature:cho-cho` «Тчо-Тчо»;
`coc:creature:chaugnar-faugn` «Чагнар Фан», «Чагнар Фагн», «Ужас с холмов»; заклинания contact-hastur, bind-enemy, create-gate,
curse-of-chaugnar-faugn, cause-cure-blindness, chime-of-tezchaptl, implant-fear, mesmerize, shrivelling, deflect-harm,
dread-curse-of-azathoth, send-dream — формы русского издания) и 2 навигационные ссылки (`coc:location:carcosa` → сцена
«Сыщик в Каркозе»; `L/location/drakmar-drakmar` → `house-drakmar-caves`). Пробный прогон `apply.py --dry-run`: 18 правок ложатся.
