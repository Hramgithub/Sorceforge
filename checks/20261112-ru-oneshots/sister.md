# «Моя маленькая сестра» (`moya-malenkaya-sestra-ru`) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] моя маленькая сестра.pdf`, 34 страницы; русское издание (переводчик не назван) сценария Miskatonic
Repository «My Little Sister Wants You to Suffer» (Paul Fricker — на обложке) для 7-й редакции, `ruleset` = `core`.
Действие — «через 20 лет от настоящего времени» (с. 3): ближнее будущее, `axes.era` = `other` (так же, как у
«Посёлка Березовый»). Текстовый слой надёжен (с. 1–23, 25, 27, 29, 31, 33); листы сыщиков (с. 24, 26, 28, 30, 32, 34) —
только изображения, числа прочитаны по изображениям при 200 dpi; статблоки с. 21 сверены по изображению.

**Страницы:** печатная = физическая (номера внизу страниц совпадают с номерами PDF, с. 1–34). `offset` — 0.

Префикс записей книги: `moya-malenkaya-sestra-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «My Little Sister Wants You to Suffer», Paul Fricker, Miskatonic Repository | 1 | `scenario/moya-malenkaya-sestra` (name.en, summary, sources) |
| Оглавление | 2 | сверка заголовков (эта таблица) |
| Введение (особенности сценария, линейная структура, предупреждение о содержании) | 3 | `scenario/moya-malenkaya-sestra` (summary) |
| Информация для Хранителя | 3 | `scenario/…` (keeper_info, hook); `organization/shou-mladshaya-sestra`; `location/gorod-stsenariya` |
| Закрытая или открытая игра | 3 | `scenario/…` (advice) |
| Представление сыщиков (по порядку, 3/4/5 игроков, Удача 2d10 + 40, конверты) | 3 | `scenario/…` (advice); прегены (player_chooses, statblock.luck) |
| Шесть сыщиков | 3 | `scenario/…` (advice) |
| 1. Сэм Уэрн, 25 лет, тюремщица | 4 | `character/sem-uern` |
| 2. Серж Каддик, 33 года, психолог | 4 | `character/serzh-kaddik`; `character/zhared-ladusyor` |
| 3. Миранда Ван Влит, 28 лет, хакер | 4 | `character/miranda-van-vlit` |
| 4. Макс Спаркс, 35 лет, преступник | 4 | `character/maks-sparks` |
| 5. Дженни Фуй, 30 лет, инструктор йоги | 5 | `character/dzhenni-fuy` |
| 6. Филип Монти, 29 лет, сёрфер | 5 | `character/filip-monti` |
| Раздача персонажей | 5 | `scenario/…` (advice) |
| Конверты | 5 | `scenario/…` (advice); раздатки `handout/vospominaniya-*` (description) |
| Ложные воспоминания и безумие | 6 | `scenario/…` (advice); `character/maks-sparks` (legend) |
| Действующие лица | 6 | `character/mutanty`, `character/otets`, `character/kristo` |
| Мутанты — безумные и жаждущие славы (яйцо-почка, описание, черты, мотив) | 6 | `character/mutanty` (abilities, background, legend) |
| «Отец» — бортовой компьютер | 6 | `character/otets` |
| Кристо, 48 лет — режиссёр | 6 | `character/kristo` |
| Обзор «космического корабля» (полы, стены, двери, освещение, камеры, люки, иллюминаторы, аномалии) + карта корабля | 7 | `location/kovcheg`; `location/telestudiya`; `map/karta-korablya` |
| Открывающая сцена: комната стазиса | 8 | `scene/probuzhdenie`; `location/komnata-stazisa` |
| Советы по ведению сцены (закрыть глаза, d10, карточки снаряжения) | 9 | `scene/probuzhdenie` |
| Создание параноидальной атмосферы | 9 | `scene/probuzhdenie`; `location/telestudiya` |
| Содержимое шкафа с снаряжением | 9 | `item/soderzhimoe-shkafa`; `item/pistolet-38`; `item/pnevmaticheskiy-pistolet` (заряды) |
| Верхний уровень (карта, русские подписи) | 10 | `map/verkhniy-uroven`; `location/verkhniy-uroven`; `location/koridor-verkhnego-urovnya` |
| Сады; Сад 1; Сад 2 | 11 | `scene/sady`; `location/sad-1`, `location/sad-2` |
| Садовый робот, мутант в зарослях, татуировка с кодом | 11–12 | `item/sadovyy-robot`; `item/tatuirovka-s-kodom`; `character/mutanty` |
| Советы по ведению сцены (сады) | 12 | `scene/sady`; `item/sadovyy-robot` |
| Комната с мозгами | 13 | `scene/komnata-s-mozgami`; `location/komnata-s-mozgami`; `item/tsilindry-s-mozgami` |
| Советы по ведению сцены (мозги, ми-го) | 14 | `scene/komnata-s-mozgami` |
| Компьютерная комната (верхний уровень); вопросы и ответы «Отца»; серебристое оружие | 14 | `scene/kompyuternaya-verkhniy-uroven`; `location/kompyuternaya-verkhnego-urovnya`; `item/butaforskiy-prishelets`, `item/kompyuter-prishelcev`, `item/pnevmaticheskiy-pistolet`; `character/otets` |
| Рекомендации к проведению сцены (компьютерная) | 15 | `scene/kompyuternaya-verkhniy-uroven` |
| Ангар шаттла | 15 | `scene/polyot-na-shattle`; `location/angar-shattla`; `location/vozdushnyy-shlyuz` |
| Полёт на шаттле: что видят сыщики | 15 | `scene/polyot-na-shattle`; `item/shattl-simulyator` |
| Полёт на шаттле: что происходит на самом деле | 15 | `scene/polyot-na-shattle`; `item/shattl-simulyator` |
| Пошаговая иллюзия: шаг 1 (схема) | 15 | `scene/polyot-na-shattle`; `map/illyuziya-polyota` |
| Шаг 2, шаг 3 (схемы) | 16 | `scene/polyot-na-shattle`; `map/illyuziya-polyota`; `location/angar-shattla` |
| Рекомендации к проведению сцены (шаттл) | 16 | `scene/polyot-na-shattle` |
| Срыв покрова | 16 | `scene/esli-igroki-podozrevayut` |
| Если игроки начинают подозревать | 16 | `scene/esli-igroki-podozrevayut`; `character/kristo` (legend) |
| Нижний уровень (+ карта) | 17 | `location/nizhniy-uroven`; `map/nizhniy-uroven` |
| Компьютерная комната (нижний уровень); «антирадиационный крем» | 17 | `scene/kompyuternaya-nizhniy-uroven`; `location/kompyuternaya-nizhnego-urovnya`; `item/antiradiatsionnyy-krem` |
| Коридор со слизью и коконами; паразит | 17–18 | `scene/koridor-s-kokonami`; `location/koridor-so-slizyu`; `item/kokony-s-parazitami`; `creature/parazit` |
| Атака паразита; Удаление паразита | 18 | `creature/parazit` (abilities); `scene/koridor-s-kokonami` |
| Советы по ведению сцены: испытание ловкости — за игровым столом | 18 | `scene/kompyuternaya-nizhniy-uroven` (по смыслу — к компьютерной комнате, пометка в записи) |
| Удача как популярность у зрителей | 18 | `scene/koridor-s-kokonami`; `creature/parazit` (legend) |
| Энергоустановка (состояние оборудования, панель управления, активация системы, атмосфера и подача) | 18 | `scene/energoustanovka`; `location/energoustanovka`; `item/energeticheskie-tsilindry` |
| Кладовка | 19 | `scene/kladovka`; `location/kladovka`; `item/shkaf-v-kladovke` |
| Центральный пункт управления; рекомендации для Хранителя | 19 | `scene/tsentralnyy-punkt-upravleniya`; `location/tsentralnyy-punkt-upravleniya` |
| Комната с капсулами; как провести эту сцену | 19 | `scene/komnata-s-kapsulami`; `location/komnata-s-kapsulami` |
| Заключение: Вы страдали?; как провести эту сцену | 19–20 | `scene/vy-stradali`; `location/sosednyaya-studiya`; `character/ronni-bleyz` |
| Награды | 20 | `scenario/…` (conclusion) |
| Приложение A: NPC и монстры — Кристо, 48 лет, режиссёр | 21 | `character/kristo` (statblock) |
| Мутанты — кровожадные и жаждущие славы | 21 | `character/mutanty` (statblock) |
| Листы персонажей и воспоминания | 22 | `scenario/…` (advice); раздатки (description) |
| Воспоминания Сэма | 23 | `handout/vospominaniya-sema`; `character/sem-uern` (background) |
| Лист сыщика «Сэм» | 24 | `character/sem-uern` (statblock) |
| Воспоминания Сержа | 25 | `handout/vospominaniya-serzha`; `character/serzh-kaddik` |
| Лист сыщика «Серж» | 26 | `character/serzh-kaddik` (statblock) |
| Воспоминания Миранды | 27 | `handout/vospominaniya-mirandy`; `character/miranda-van-vlit` |
| Лист сыщика «Миранда» | 28 | `character/miranda-van-vlit` (statblock) |
| Макс: Воспоминания | 29 | `handout/vospominaniya-maksa`; `character/maks-sparks` |
| Лист сыщика «Макс» | 30 | `character/maks-sparks` (statblock) |
| Дженни: Воспоминания | 31 | `handout/vospominaniya-dzhenni`; `character/dzhenni-fuy` |
| Лист сыщика «Дженни» | 32 | `character/dzhenni-fuy` (statblock) |
| (без заголовка) воспоминания Филипа | 33 | `handout/vospominaniya-filipa`; `character/filip-monti` |
| Лист сыщика «Филипп» | 34 | `character/filip-monti` (statblock) |

Места: город книга не называет — `location/gorod-stsenariya` («город сценария», Р-190) → `location/telestudiya` →
`location/kovcheg` (декорация) → `location/verkhniy-uroven` / `location/nizhniy-uroven` → комнаты; `location/angar-shattla` —
одна запись на оба «уровня» (по тексту ангар один), часть `kovcheg`; `location/sosednyaya-studiya` — часть студии.
Общих городов не создано и не изменено.

Карты (картинки — `app/maps/sister-*.jpg`, вырезаны из изображений страниц при 200 dpi; метки проверены на наложении):
`map/karta-korablya` (с. 7, 22 метки: все подписи, номера капсул 1–6, условные знаки SLIME и EGG PODS),
`map/verkhniy-uroven` (с. 10, 9 меток), `map/nizhniy-uroven` (с. 17, 15 меток), `map/illyuziya-polyota`
(схемы с. 15–16, сведены в одну картинку, 5 меток).

## Опечатки и противоречия книги (в `errata`)

- `character/dzhenni-fuy`, `handout/vospominaniya-dzhenni`: по вступлению ложное воспоминание Дженни — «борец за свободу; Миранда — культистка» (с. 5), но в пяти её конвертах (с. 31) этого нет; какое воспоминание ложное, книга не говорит.
- `character/dzhenni-fuy`: на листе отмечена Комплекция +1 (с. 32), по правилам при СИЛ 55 + ТЕЛ 45 — 0.
- `character/filip-monti`: Рассудок 50 при МОЩ 55 (с. 34); Метание 10% ниже базовых 20%.
- `character/mutanty`: Скорость 8, по правилам 9 (СИЛ 70, ЛВК 72 > ТЕЛ 65; с. 21).
- `scene/tsentralnyy-punkt-upravleniya`: «активировать все три цилиндра» — а нужно шесть, и падают «все шесть» (с. 18–19).
- `scene/koridor-s-kokonami`, `item/kokony-s-parazitami`: 12 коконов, «некоторые уже лопнули» (с. 17) против «каждое из 12 активных» (с. 18).
- Ссылки не туда: «см. Мутанты, стр. 22» → с. 21 (`scene/sady`); «Компьютерную комнату (см. стр. 13)» → с. 14 (`item/tatuirovka-s-kodom`); «ангара шаттлов (см. стр. 14)» → с. 15–16 (`scene/polyot-na-shattle`); Удача «(см. стр. 4)» → с. 3 (`scenario/moya-malenkaya-sestra`).

Без `errata` (пометки в `quality.notes`): Сэм — женщина во вступлении (с. 4), но в мужском роде в воспоминаниях (с. 23) и в реплике
«Поймай лицо Сэма» (с. 16), и «Она носил форму» в воспоминаниях Миранды (с. 27); «Ладусер» (с. 4) / «Ладусёр» (с. 25);
«Филип» (текст) / «Филипп» (лист); «Father» трижды на с. 18; «французкий», «ремонт элетроники» на листах; название шоу
колеблется («Младшая сестра», «Маленькая сестра», «Младшая сестренка»); на карте с. 10 подпись «Комната стазиса» стоит
над комнатой с мозгами; на листах не отмечены ПМ, у четырёх сыщиков — БкУ и Комплекция (не записаны, правильные
значения — в пометках); у Миранды вписан французский без значения.

## Не взято

- Портреты шести сыщиков (с. 4–5 и на листах), портрет и рисунок Кристо (с. 6, 21), рисунки мутанта (с. 6, 21),
  иллюстрации садов, комнаты с мозгами, капсулы (с. 8, 11–13) и телеведущего (с. 20), обложка (с. 1) — картинки без
  игровых данных; `app/art/` не входит в файлы этой части. Портреты прегенов можно добавить навыком `kb-art`.
- Оформление листов сыщика (кнопки «Сбросить форму/характеристики/навыки», шкалы ПЗ/ПМ/Удачи/Рассудка, базовые
  значения навыков на бланке) — бланк, а не данные сценария; взяты только заполненные значения.

## Кандидаты и вопросы

- Новых заклинаний нет. Новых общих городов нет.
- Предложение (`proposals-sister.json`, 1): псевдоним «Й’голонак» для `coc:creature:ygolonac`.
- Вопрос владельцу: эпоха «через 20 лет от настоящего» записана как `other`; если для ближнего будущего нужна другая
  отметка (например, `modern`), её стоит решить вместе с частью miracle (тоже 2040).
