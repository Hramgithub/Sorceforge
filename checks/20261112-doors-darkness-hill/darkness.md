# «Тьма под холмом» («Двери во тьму», `dveri-vo-tmu-ru`) — сверка переноса (часть darkness)

Источник — официальное русское издание «Двери во тьму» (скан без текстового слоя): страницы распознаны
`pdftoppm -r 200` + `tesseract -l rus`, каждое число сверено по изображению страницы или по английскому
оригиналу `doors-to-darkness-en` (Р-213). Распознанный владельцем текст из `2_Обработка` — только подспорье
для чтения.

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 2 «Тьма под холмом» (с иллюстрацией на развороте) | 14–34 (заставка — с. 13) | 13–33 (заставка — 12) |
| «Материалы для игроков»: «Тьма 1», «Тьма 2» | 111–112 | 110–111 |
| «Готовые персонажи» (десять сыщиков сборника) | 126–135 | 125–134 |

Смещение `dveri-vo-tmu-ru`: **печатная = физическая + 1** на всех проверенных страницах (13→14, 18→19, 22→23,
30→31, 33→34, 110→111, 125→126). Номера печатных страниц русского издания совпадают с английским оригиналом
(`doors-to-darkness-en`: печатная = физическая − 1; сценарий — физ. 15–35, раздатки — физ. 112–113, готовые
персонажи — физ. 127–136).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 2. Тьма под холмом (Кристофер Смит Адейр) | 14 | сценарий `dveri-vo-tmu-ru/scenario/darkness-beneath-the-hill` (summary) |
| Введение | 14 | сценарий: summary |
| Информация для Хранителя | 14 | сценарий: keeper_info; город `coc:location:providence`; персонажи `…/character/darkness-elijah-winscott`, `…/character/darkness-john-brown`; существа `…/creature/darkness-ssyaa-hrisss`, `…/creature/darkness-ghasts` |
| Город Провиденс | 14–15 | `coc:location:providence` (description); `…/location/darkness-college-hill` |
| Встреча с Джошем Винскоттом | 15–16 | сцена `…/scene/darkness-meeting-winscott`; сценарий: hook; `…/character/darkness-josh-winscott`; `…/location/darkness-winscott-house` |
| Хранителю на заметку: пути исследования (врезка) | 16 | сценарий: advice; сцена `darkness-research` (mechanics); раздатка `darkness-1-bishop-letter` |
| Изучение архивов | 16 | сцена `…/scene/darkness-research` |
| • Библиотека им. Джона Хэя | 16 | `…/location/darkness-john-hay-library` |
| • Провиденский Атенеум | 16 | `…/location/darkness-providence-athenaeum` |
| Семейство Винскоттов | 16–17 | сцена `darkness-research`; `…/character/darkness-elijah-winscott`, `darkness-micah-winscott`, `darkness-aunt-florence`; `darkness-winscott-house` |
| Работорговля в Провиденсе | 17 | сцена `darkness-research`; `…/character/darkness-john-brown`; `…/location/darkness-john-brown-house`; `darkness-college-hill` |
| Письмо | 17 | сцена `darkness-research`; `…/handout/darkness-1-bishop-letter`; `darkness-providence-athenaeum` |
| Материал «Тьма 1» (в главе) | 18 | `…/handout/darkness-1-bishop-letter` (текст); `…/character/darkness-jacob-bishop`, `darkness-phillip` |
| Карта 1 | 19 | карта `…/map/darkness-map-1-tunnel` (`app/maps/dveri-darkness-map-1.jpg`, 4 метки на подписи) |
| В глубины | 19 | сцена `…/scene/darkness-into-the-depths`; `…/location/darkness-slave-tunnel`, `darkness-ancient-remains`; предмет `…/item/darkness-turkish-cigarette-stub` |
| Катакомбы змеиного народа | 19 | `…/location/darkness-serpent-catacombs`; сцена `darkness-entry-hall` |
| Вестибюль | 19, 22 | сцена `…/scene/darkness-entry-hall`; место `…/location/darkness-1-entry-hall` |
| Гнусные обитатели пещер | 21 | сцена `…/scene/darkness-cave-inhabitants` |
| Выродки (с примерами: кости, звуки, близкие контакты, драка, засада) | 21 | существо `…/creature/darkness-degenerates`; таблица сценария «Встречи с выродками» |
| Гасты: чудовищные приспешники | 21 | существо `…/creature/darkness-ghasts`; сцена `darkness-cave-inhabitants` |
| Хранителю на заметку: мотивация сыщиков (врезка) | 22 | сценарий: advice |
| Глубже в пещеры | 22 | сцена `…/scene/darkness-deeper-into-caverns`; `darkness-serpent-catacombs` (описание) |
| Зал Истории | 22 | сцена `…/scene/darkness-hall-of-history`; место `darkness-2-hall-of-history` |
| Карта 2 (ключ 1–15) | 23 | карта `…/map/darkness-map-2-catacombs` (`app/maps/dveri-darkness-map-2.jpg`, 18 меток: номера 1–15, три «5», «Назад к цивилизации»); места `darkness-1-entry-hall` … `darkness-15-gate` |
| Обрыв | 25 | сцена `…/scene/darkness-pitch`; место `darkness-3-pitch` |
| Чертоги музыки | 25–26 | сцена `…/scene/darkness-music-chamber`; место `darkness-4-music-chamber`; предмет `…/item/darkness-music-device` |
| Пристанища выродков | 26 | сцена `…/scene/darkness-warrens`; места `darkness-5-warrens`, `darkness-6-testimonial` |
| Провал грунта | 26 | сцена `…/scene/darkness-sinkhole`; место `darkness-7-sinkhole` |
| Теплица | 26 | сцена `…/scene/darkness-plantation`; место `darkness-8-plantation`; предмет `…/item/darkness-poisonous-fungi` |
| Храм Отца Змей | 26 | сцена `…/scene/darkness-temple`; место `darkness-9-temple`; `coc:creature:yig` |
| Материал «Тьма 2» (в главе) | 27 | `…/handout/darkness-2-harper-testimony`; `…/character/darkness-john-harper` |
| Камера анабиоза | 29 | сцена `…/scene/darkness-suspended-animation`; место `darkness-10-suspended-animation-chamber` |
| Хранителю на заметку: шёпот змия (врезка) | 29 | сцена `darkness-temple` (описание); сценарий: advice (ссылка) |
| Схвачены! (врезка) | 30 | сцена `…/scene/darkness-captured`; предмет `…/item/darkness-soporific-poison`; место `darkness-13-alcove-cell` |
| Логово С’сья-Х’риссса | 31–32 | сцена `…/scene/darkness-lair`; места `darkness-11-lair` … `darkness-15-gate`, `darkness-pawtuxet-cave`, `darkness-providence-environs`; предметы `darkness-bronze-gong`, `darkness-laboratory-chemicals`, `darkness-leather-scrolls` |
| Карта 3 | 31 | карта `…/map/darkness-map-3-lair` (`app/maps/dveri-darkness-map-3.jpg`, 9 меток на подписи) |
| Друг в беде | 32 | сцена `…/scene/darkness-friend-in-trouble`; `darkness-josh-winscott` (legend) |
| Итоги | 32 | сценарий: conclusion; шаг «Итоги и награды» |
| Награды | 32 | сценарий: conclusion (шесть наград Рассудка) |
| Приложение А. Персонажи Хранителя и чудовища | 34 | — |
| Джош Винскотт, жертва своего наследия | 34 | `…/character/darkness-josh-winscott` (статблок) |
| Выродки, выродившиеся люди | 34 | `…/creature/darkness-degenerates` (статблок со средними и бросками) |
| Гасты, гнусные надсмотрщики | 34 | `…/creature/darkness-ghasts` (`instance_of` `coc:creature:gast`) |
| С’сья-Х’риссс, змий-учёный | 34 | `…/creature/darkness-ssyaa-hrisss` (`instance_of` `coc:creature:serpent-person`) |
| Материалы для игроков: материал «Тьма 1» | 111 | `…/handout/darkness-1-bishop-letter` (источник текста) |
| Материал «Тьма 2» | 112 | `…/handout/darkness-2-harper-testimony` (источник текста) |
| Готовые персонажи (десять сыщиков) | 126–135 | существующие записи `dveri-vo-tmu-ru/character/<slug>` (из «Двери во тьму: готовые персонажи»); в ссылках сценария; источник книги и `name.en` — предложениями |

`…/` = `dveri-vo-tmu-ru/`. Город — общая запись `kb/locations/providence.json` (новая, Р-190); места
сценария — записи книги с `part_of` на город, район «Колледж-хилл» и область «Окрестности Провиденса» (Р-209).

## Записи (67)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `darkness-beneath-the-hill` |
| scene | 17 | `darkness-meeting-winscott`, `-research`, `-into-the-depths`, `-entry-hall`, `-cave-inhabitants`, `-deeper-into-caverns`, `-hall-of-history`, `-pitch`, `-music-chamber`, `-warrens`, `-sinkhole`, `-plantation`, `-temple`, `-suspended-animation`, `-captured`, `-lair`, `-friend-in-trouble` |
| location | 26 | общий город `coc:location:providence`; книги: `darkness-providence-environs`, `-pawtuxet-cave`, `-college-hill`, `-winscott-house`, `-john-hay-library`, `-providence-athenaeum`, `-john-brown-house`, `-slave-tunnel`, `-ancient-remains`, `-serpent-catacombs`, `-1-entry-hall` … `-15-gate` |
| map | 3 | `darkness-map-1-tunnel`, `darkness-map-2-catacombs`, `darkness-map-3-lair` |
| character | 8 | `darkness-josh-winscott` (статблок), `-elijah-winscott`, `-micah-winscott`, `-aunt-florence`, `-jacob-bishop`, `-phillip`, `-john-harper`, `-john-brown` |
| creature | 3 | `darkness-ssyaa-hrisss`, `darkness-ghasts`, `darkness-degenerates` |
| item | 7 | `darkness-turkish-cigarette-stub`, `-music-device`, `-poisonous-fungi`, `-soporific-poison`, `-leather-scrolls`, `-laboratory-chemicals`, `-bronze-gong` |
| handout | 2 | `darkness-1-bishop-letter`, `darkness-2-harper-testimony` |
| organization | 0 | организаций в сценарии нет (змеиный народ — вид существ) |

## Расхождения изданий и опечатки

- Вестибюль: русское издание — обвалилось 15–20 м **западной** стены (с. 22); английский оригинал — около 50 футов
  **восточной** (с. 22). Взято по русскому изданию; пометки — в сцене и месте 1.
- С’сья-Х’риссс: ПЗ 20 при ВЫН 45 и ТЕЛ 65 (по правилам — 11); так и в оригинале. `errata` как напечатано (Р-161).
- Джон Браун: суд и оправдание — 1797 год (с. 14) и 1796 год (с. 17); так и в оригинале. `errata` у персонажа.
- Ссылки на «Книгу хранителя»: русское издание — «Околдовать жертву» с. 259, «Разрушение» с. 261 (оригинал — с. 258 и 265 англ. издания).
- Мелкие различия формулировок: библиотеки «менее чем в километре от дома Винскотта» (оригинал — полмили к северу);
  атаки С’сья-Х’риссса ножом и укусом — отдельные строки (оригинал — «Fighting 50%, damage 1d3 (or knife, 1d6)»); яд —
  «при провале получает 1d8 урона» (оригинал — «+1d8 damage»). Число голов в Чертогах музыки (два десятка) — только в оригинале.

## Не взято

- Иллюстрации и фото (с. 13 — заставка главы; с. 15 — Библиотека им. Джона Хэя; с. 17 — Провиденский Атенеум; с. 20 — «Выродки»;
  с. 24 — «Зал Истории», «Чертоги музыки»; с. 28 — «Храм Отца Змей и камера анабиоза»; с. 30 — гаст; с. 33 — «Логово С’сья-Х’риссса»):
  картинки в записи не добавлялись (поле `images` необязательно; можно добавить позже `pipeline/art/add_images.py`).
- Роджер Уильямс, Брауновский университет, Род-Айлендская школа дизайна, старейшая баптистская церковь, Канал-стрит,
  «Вестник Провиденса», Ку-клукс-клан — упомянуты только в истории города: остались текстом в описании Провиденса, записей нет.
- Безымянные «итальянские работяги» Винскотта, слуги Элайджи, трое выродков-помощников и детёныши в клетке — текстом в сценах
  и описании выродков (отдельных профилей в книге нет).
- Значок «D» в пещере 4 на Карте 2 — в ключе не объяснён; метка не ставилась, пометка в карте и месте 4.
- Алфавитный указатель книги (с. 136–138) — служебный.
- Числа листов готовых сыщиков в самой книге (с. 126–135) с существующими записями не сверялись: записи заведены по отдельному
  PDF «Двери во тьму: готовые персонажи»; источник книги предложен с `verified: false`.

## Предложения

`proposals-darkness.json` — 21 предложение: десяти готовым сыщикам — `name.en` по оригиналу и источник книги
`dveri-vo-tmu-ru` (с. 126–135); `coc:creature:serpent-person` — псевдоним «Змеиный народ». Пробный прогон
`pipeline/integrate/apply.py --dry-run`: 21 правка ложится.
