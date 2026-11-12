# «Number 7 Dream» → база (часть number7, Р-221)

Книга `number-7-dream-en` (James Killick, Miskatonic Repository, 2021; EN 7e, Modern Era), 26 страниц. Русский текст и
имена — перевод владельца `2_Обработка\2021 Number 7 Dream\Number_7_Dream_RU.html`; числа — по английским страницам.

- Редакция: 7-я (характеристики в процентах, статблоки 7e) — статблоки перенесены.
- Страницы: печатный номер = физический (offset 0) на с. 4–26; с. 1–3 (обложка, выходные данные, оглавление) без номеров,
  в `sources` у них физический номер.
- Записи: `kb/books/number-7-dream-en/` (сценарий, 19 сцен, 10 раздаток, 8 предметов, 1 организация, 17 персонажей,
  2 существа, 38 мест, 3 карты) и общий город `kb/locations/bristol.json` (новый, Р-190).
- Карты: `app/maps/number7-stanwicks-bookshop.jpg`, `number7-wellness-centre.jpg`, `number7-the-institute.jpg` — метки на
  каждой подписи плана, проверены глазами по наложению.
- Предложения общих записей: `proposals-number7.json` (4).

Префикс id ниже: `B/` = `number-7-dream-en/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «A Call of Cthulhu 7th Edition Modern Era Scenario» | 1 | `B/scenario/number-7-dream` (sources, summary) |
| Credits | 2 | `B/scenario/number-7-dream` (sources: автор, год) |
| Table of Contents | 3 | этот файл |
| Introduction | 4 | `B/scenario/number-7-dream` (summary, advice) |
| Background | 4 | сценарий (keeper_info); `B/organization/the-enlightened` |
| What happened to the investigators? | 4 | сценарий (keeper_info) |
| Construct 7 | 4 | сценарий (keeper_info); `B/item/construct-7` |
| Glitches | 4–5 | сценарий, таблица «Сбои Конструкта» |
| Dreams | 5 | сценарий, таблица «Сны» |
| The Boardroom | 5 | `B/handout/dream-boardroom` |
| The Janitor | 5 | `B/handout/dream-janitor` |
| The Monolith | 5 | `B/handout/dream-monolith` |
| The Monster | 5 | `B/handout/dream-monster` |
| The Canisters | 5 | `B/handout/dream-canisters` |
| The Migo | 6 | сценарий (keeper_info); `B/character/migo-man` |
| Keeper Considerations | 6 | сценарий (keeper_info) |
| The Enlightened | 6 | `B/organization/the-enlightened` |
| Dramatis Personae: Stanwick Webb | 6–7 | `B/character/stanwick-webb` |
| Dramatis Personae: Elsie Webb | 7 | `B/character/elsie-webb` |
| Beginning the Adventure; Handout 1 | 7 | `B/handout/handout-1-stanwick-email` |
| An Email Out of the Blue | 7 | `B/scene/email-out-of-the-blue` |
| Stanwicks Bookshop (план) | 8 | `B/location/stanwicks-bookshop` (+ `bookshop-shop`, `bookshop-office`, `bookshop-bedroom`), `B/map/stanwicks-bookshop`, `B/location/christmas-steps` |
| The Shopper | 8 | `B/scene/bookshop-shopper`; `B/character/the-shopper` |
| Upstairs | 8 | `B/scene/bookshop-upstairs`; `B/item/elsies-charms` |
| What Stanwick Knows | 8–9 | `B/scene/bookshop-upstairs` |
| Handout 2 | 9 | `B/handout/handout-2-elsie-letter` |
| Leaving Stanwicks Bookshop: The Faceless Man; The Shopper | 9 | `B/scene/leaving-bookshop` |
| Elsie’s Flat | 9 | `B/scene/elsies-flat`; `B/location/elsies-flat`, `B/location/launderette`; `B/character/launderette-man` |
| Elsie’s Diary | 9 | `B/item/elsies-diary`; `B/scene/elsies-flat` |
| Handout 3 | 10 | `B/handout/handout-3-enlightened-leaflet` |
| Summary of Elsie’s Journal (Handout 4) | 10 | `B/handout/handout-4-journal-summary` |
| Leaving Elsie’s Flat: The Boyfriend | 10 | `B/scene/the-boyfriend`; `B/character/jonathan`, `B/character/david` |
| Leaving Elsie’s Flat: The Bus | 10 | `B/scene/the-bus` |
| The Enlightened Website | 10 | `B/scene/enlightened-website`; организация (список центров) |
| The Enlightened Wellness Centre (план, расписание) | 10–11 | `B/scene/wellness-centre`; `B/location/wellness-centre` (таблица «Расписание мероприятий») + 11 комнат `wc-*`; `B/map/wellness-centre`; `B/item/enlightened-office-papers`; `B/character/receptionist` |
| Stanwick’s Cottage | 12 | `B/scene/stanwicks-cottage`; `B/location/stanwicks-cottage`; `B/item/stanwicks-weapons` |
| The Cabin in the Woods | 12 | `B/scene/cabin-in-the-woods`; `B/location/cabin-in-the-woods`; `B/location/bristol-environs` |
| Rewind | 12 | `B/scene/rewind` |
| The Last Warning | 12 | `B/scene/last-warning` |
| Live or Let Die | 13 | `B/scene/live-or-let-die` |
| Meeting Elsie | 13 | `B/scene/meeting-elsie` |
| What Happened to Elsie | 13 | `B/scene/meeting-elsie`; `B/character/elsie-webb` (legend) |
| Leaving Elsie | 13–14 | `B/scene/leaving-elsie` |
| Handout 5 | 14 | `B/handout/handout-5-elsie-letter` |
| The Escape | 14 | `B/scene/the-escape` |
| Elder Sign Pendant | 14 | `B/item/elder-sign-pendant` |
| The Institute (план) | 15 | `B/location/institute`, `B/map/the-institute` |
| Keepers Note | 15 | `B/scene/exploring-the-institute` |
| Exploring the Institute | 15 | `B/scene/exploring-the-institute`; `B/location/institute-gatehouse`; `B/character/gatehouse-guard` |
| The Ground Floor: The Entrance; Waiting Rooms; Reading Room | 15 | `B/location/institute-entrance`, `institute-waiting-rooms`, `institute-reading-room` |
| Processing Room | 16 | `B/location/institute-processing-room` |
| Surgery | 16 | `B/location/institute-surgery` |
| Machine Room | 16 | `B/location/institute-machine-room`; `B/item/construct-7`, `B/item/brain-canisters` |
| Gateway Room | 16 | `B/location/institute-gateway-room`; `B/item/gate-to-yuggoth` |
| Hallway | 16 | `B/location/institute-hallway` |
| The First Floor: Bedrooms; Staff Room; Padded Cells; Interrogation Room | 16 | `B/location/institute-bedrooms`, `institute-staff-room`, `institute-padded-cells`, `institute-interrogation-room` (+ `institute-bathroom` с плана) |
| The Final Conference | 17 | `B/scene/final-conference`; `B/location/institute-conference-room` |
| Appendix A – Characters Stats (вступление) | 18 | сценарий (advice) |
| Stanwick Webb | 18 | `B/character/stanwick-webb` (statblock) |
| Elsie Webb | 18 | `B/character/elsie-webb` (statblock) |
| Enlightened (Regular) | 18 | `B/character/enlightened-regular` |
| Enlightened (Heavy) | 18 | `B/character/enlightened-heavy` |
| The Migo Man | 18 | `B/character/migo-man` (statblock) |
| Migo | 18 | `B/creature/mi-go` (instance_of `coc:creature:mi-go`) |
| Hunting Horror | 18 | `B/creature/hunting-horror` (instance_of `coc:creature:hunting-horror`) |
| Appendix B – Handouts (1, 3, 5; 2, 4) | 19–20 | те же записи раздаток (второй источник) |
| Appendix C: Jocelyn Eaves – Author | 21 | `B/character/jocelyn-eaves` |
| Milton Lowe – Computer Programmer | 22 | `B/character/milton-lowe` |
| Augustine Fraser – Private Investigator | 23 | `B/character/augustine-fraser` |
| Captain Ainsley Hammond – Retired Military Officer | 24 | `B/character/ainsley-hammond` |
| Vincent Tenny – Bouncer | 25 | `B/character/vincent-tenny` |
| Camelia Brown – Waitress | 26 | `B/character/camelia-brown` |

## Опечатки книги (в `errata`)

- «Enchanted» вместо «Enlightened» (с. 12, 13, 14) — `B/organization/the-enlightened`; в записях — «Просветлённые», у владельца — «Зачарованные» (псевдоним).
- «anyone who has dreamt The Conference Room» — такого сна нет, это «The Boardroom» — `B/scene/final-conference`.
- Стэнвик: ПЗ 9 (по правилам 13); Драка 55% (17/7) и Дробовик 65% (20/8) — доли исправлены (Р-35/Р-77); Скорость 4 (по правилам 5–7, видимо из-за колена); запас еды — «на две недели» (с. 7) и «на месяц» (с. 12).
- Элси: ПЗ 9 (по правилам 11).
- Просветлённый (обычный): ПМ 17 (по правилам 10 — видимо, перенесено из профиля Элси); Уклонение 10% ниже половины ЛВК.
- Просветлённый (силовик): Уклонение 25% ниже половины ЛВК (27).
- Человек-ми-го: Драка 99% (17/7) — доли исправлены; Скорость 7 (по правилам 9), БкУ 1d4 и Комплекция 1 (по правилам +1d6 и 2), ПМ n/a.
- Ми-го: ПМ 6 (по правилам 8).
- Охотящийся ужас: строки атак, Скорости, брони, Уклонения и потери Рассудка слово в слово повторяют блок ми-го (в Malleus: 65%, броня 9, полёт 11, 0/1d10).
- Винсент Тенни: Комплекция 0 (по правилам 1); «Средства» напечатаны дважды (10% и 35%); Удача не напечатана.
- Камелия Браун: «you and Camelia fell out» вместо «you and Elsie» (исправлено в записи).

## Не взято

- Имена авторов, фотографа и плейтестеров (с. 2) — только в `sources` сценария (автор); плейтестеры не переносятся: не игровой материал.
- Иллюстрации и портреты (с. 1, 4–7, 9, 13–15, 17, 21–26; копии есть в `2_Обработка\2021 Number 7 Dream\assets`) — не добавлены в `images`: картинки — отдельный шаг (Р-165, kb-art).
- Книга, которую Элси украла у «Просветлённых» (с. 13), — без названия и данных; записи `tome` нет, упомянута в записи Элси и сцене «Встреча с Элси».
- Фигура в капюшоне (подсознание сыщиков, с. 12) — без статблока и имени, описана в сценах «Хижина в лесу» и «Последнее предупреждение»; отдельной записи нет.
- Юггот — общей записи места нет; упомянут текстом (врата, ми-го).
- Упомянутые только в предысториях: жена Хэммонда Джанет, его дети, муж Камелии, мальчик, сбитый Фрейзером, мать Элси (это Джоселин — запись есть), «двое крепких санитаров» Института — текстом, без записей.
- Список городов с центрами благополучия (Лондон, Бирмингем, Кардифф, Глазго, Манчестер, Лидс, Ноттингем, Лиссабон, Хьюстон, Нью-Йорк) — текстом в организации и сцене «Сайт»; ссылки только на существующие `coc:location:london`, `coc:location:new-york`, общие города не правились.
- Ущелье Эйвон, театральная школа Бристоль-Олд-Вик — текстом в записи Бристоля.
