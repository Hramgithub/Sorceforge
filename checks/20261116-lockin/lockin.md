# Lock-in: Five in a Bunker (`lock-in-five-en`) — сверка переноса

Р-251, Р-134. Книга: Alison Cybe, Miskatonic Repository, 2020; 30 страниц PDF.
Страницы: печатная = физическая − 1 (обложка и выходные данные без номера; «3» на физ. 4) → `offset: -1`.
Записи — `kb/books/lock-in-five-en/` (59): сценарий 1, сцены 8, персонажи 8 (5 прегенов), существо 1,
раздатки 28, предметы 7, места 4, организации 2. Карт и планов в книге нет.

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, выходные данные | физ. 1–2 | `scenario/lock-in-five-in-a-bunker` (sources); обложка — `atmosphere.json` |
| Contents | 2 | `scenario/lock-in-five-in-a-bunker` (sources) |
| A quick word on piracy | 2 | не взято — обращение автора к читателю о пиратстве и ссылки на Ko-fi/Patreon, не игровой материал |
| Introduction | 3 | `scenario/…` → `advice` (вступление автора, согласие, изоляция); `scene/involving-the-players` |
| Lock-in: Five in a bunker / Keeper Information | 4 | `scenario/…` → `summary`, `keeper_info`; `character/sandford`, `organization/sandford-task-force`, `organization/sandford-benefactors`, `item/xb-742`, `item/chalmers-journal-fragments`, `character/halpin-chalmers`, `location/arizona-military-base`, `location/base-tunnels` |
| Involving the Players | 5 | `scene/involving-the-players` |
| Act 1 (текст для чтения, свободный акт, удостоверения) | 5 | `scene/act-1-awakening`; `item/identification-cards`; `location/bunker-chamber` |
| Камера, дверь, тело, обыск | 6 | `scene/act-1-awakening`; `location/bunker-chamber`; `item/sandford-revolver`, `item/sandford-id-badge` |
| Врезка «Why shoot the Hound when we can shoot each other?» | 6 | `item/sandford-revolver` → `mechanics`; `scenario/…` → `advice`; `creature/bunker-hound-of-tindalos` (способность) |
| Раздатка № 2, две раздатки Акта 1, оружие | 7 | `scene/act-1-awakening` |
| Конец Акта 1 (солдат у двери) | 7 | `scene/act-1-soldier-at-the-door`; `character/billy-carson` |
| Act 2 | 7–9 | `scene/act-2-the-soldiers-body`; `location/bunker-hallway`; `item/first-aid-kit`, `item/walkie-talkie` |
| Врезка «My Sanity is zero!» | 9 | `scene/act-2-the-soldiers-body`; `scenario/…` → `advice` |
| Аптечка, рация, голос Сэндфорда, конец Акта 2 | 9 | `scene/act-2-walkie-talkie` |
| Итоги Акта 2 | 9–10 | `scene/act-2-the-soldiers-body` |
| Act 3 (раздатки № 4, A/B, путь по туннелю, двойники) | 10–11 | `scene/act-3-through-the-fragments`; `location/base-tunnels` |
| Ритуал (раздатки № 5, текст для чтения, раздатка C) | 11–12 | `scene/act-3-the-ritual` |
| Врезка «Cut it out!» | 12 | `scene/act-3-the-ritual`; `handout/handout-b` |
| The Hound of Tindalos (статблок в Акте 3) | 12–13 | `creature/bunker-hound-of-tindalos` |
| Гончая до 0 ПЗ, бегство, три концовки | 13 | `scene/act-3-hound-and-escape` |
| Concluding the nightmare | 14 | `scenario/…` → `conclusion` |
| Antagonists: The Hound of Tindalos | 15 | `creature/bunker-hound-of-tindalos` (тот же статблок) |
| Antagonists: Lieutenant Sandford | 15 | `character/sandford` |
| Investigators — Harvey Walsh + Handouts #1–5 | 16–17 | `character/harvey-walsh`; `handout/walsh-handout-1…5` |
| Investigators — Corbin Richardson + Handouts #1–5 | 18–19 | `character/corbin-richardson`; `handout/richardson-handout-1…5` |
| Investigators — Samantha Rockford + Handouts #1–5 | 20–21 | `character/samantha-rockford`; `handout/rockford-handout-1…5` |
| Investigators — Rachel King + Handouts #1–5 | 22–23 | `character/rachel-king`; `handout/king-handout-1…5` |
| Investigators — Daniel Langsdale + Handouts #1–5 | 24–25 | `character/daniel-langsdale`; `handout/langsdale-handout-1…5` |
| Handouts: Handout A, B, C | 26 | `handout/handout-a`, `handout/handout-b`, `handout/handout-c` |
| About the Author | 27 | не взято — биография автора и контакты, не игровой материал |
| Пустые страницы | физ. 30 | — |

## Картинки

- Взята: Гончая Тиндала (физ. 14) → `creature/bunker-hound-of-tindalos` (`app/art/creatures/lockin-hound-of-tindalos.webp`; `art.json`, предложения применены).
- Атмосфера (`atmosphere.json`, сводит ведущий): обложка, задняя обложка, силуэт у вступления, черепа, военный с пистолетом без подписи (физ. 9),
  тараканы, рука с сердцем, череп, рука из могилы. Портретов прегенов, раздаток-картинок и карт в книге нет.
- `tools/completeness.py`: находки `art.record_without` / `art.uncovered` — это украшения из списка атмосферы; `text.gap` — «About the Author» (не взято).

## Не взято

- «A quick word on piracy» (с. 2) — обращение автора о пиратстве, ссылки на Ko-fi и Patreon.
- «About the Author» (с. 27) — биография автора, контакты.
- Декоративные картинки — в `atmosphere.json`.

## Опечатки и сомнения (в `errata` записей)

| Запись | Напечатано | Ожидалось | Исправлено |
|---|---|---|---|
| Харви Уолш, с. 16 | Magic 11 | ПМ 8 (МОЩ 40) | нет |
| Харви Уолш, с. 16 | Fighting (Handguns 60%) | Стрельба (пистолет) | да |
| Корбин Ричардсон, с. 18 | Magic 9 | ПМ 12 (МОЩ 60) | нет |
| Корбин Ричардсон, с. 18 | Fighting (Handguns 50%) | Стрельба (пистолет) | да |
| Саманта Рокфорд, с. 20 | Hit Points 11 | 14 ((70+70)/10) | нет |
| Дэниел Лэнгсдейл, с. 24 | Hit Points 9 | 12 ((55+70)/10) | нет |
| Лейтенант Сэндфорд, с. 15 | HP 13 | 11 ((65+45)/10) | нет |
| Лейтенант Сэндфорд, с. 15 | Move 12 | 9 (человек) | нет |

Без errata (в `quality.notes`): урон Сэндфорда «Punch 1d4 + 2», «Pistol 2d6 + 4» — как напечатан; Гончая — ТЕЛ 85, Скорость 6, без полёта, брони и потери
Рассудка; сценарий разрешает ранить её револьвером (1d12), хотя по Malleus она неуязвима для обычного оружия; Рассудок при виде Гончей в Акте 3 не
напечатан (в сцене дана подсказка вида 1d3/1d20 как вывод); раздатка Саманты Рокфорд № 2 повторяет конец раздатки Харви Уолша № 2 («he’s») —
по с. 7 двое добиваются оружия, текст как напечатан; «Rescued Sandford: +1d6» — Сэндфорд в настоящем мёртв, спасти можно только его прошлое «я»
(по тексту не уточнено). Мелочи исправлены молча (Р-39): «first aid kid», «One way our remains», «Anthropology (34)» без %, разрыв «Your inv … 0estigator».

## Термины (English → русский)

| English | Русский |
|---|---|
| Lock-in: Five in a Bunker | Взаперти: пятеро в бункере |
| Lieutenant Sandford | лейтенант Сэндфорд |
| Harvey Walsh | Харви Уолш |
| Corbin Richardson | Корбин Ричардсон |
| Samantha Rockford | Саманта Рокфорд |
| Rachel King | Рейчел Кинг |
| Daniel Langsdale | Дэниел Лэнгсдейл |
| Halpin Chalmers | Хэлпин Чалмерс |
| the soldier (unnamed) | рядовой Билли Карсон (имя придумано, Р-150) |
| Hound of Tindalos / the Hound | Гончая Тиндала / Гончая |
| XB-742 | XB-742 (препарат) |
| the bunker / the chamber | бункер / камера |
| hallway | коридор |
| tunnels beneath the base | туннели под базой |
| US military base in Arizona | военная база в Аризоне |
| fragments (of time); time fragments | осколки времени; время дробится на осколки |
| the ritual / reversing the ritual | ритуал / обратный ритуал (обратить ритуал вспять) |
| incantation; chant | напев |
| task force | оперативная группа (Сэндфорда) |
| shadowy benefactors; backers | тёмные покровители; покровители |
| covert group within the US military complex | тайная группа внутри военно-промышленного комплекса США |
| Viet Cong | Вьетконг |
| revolver; the gun | револьвер; оружие |
| ID badge; identification card | удостоверение |
| first aid kit | аптечка |
| walkie-talkie | рация |
| Handout #1…#5 (of an investigator) | раздатка № 1…5 (сыщика) |
| Handout A / B / C | раздатка A / B / C |
| You remember the following | Вы вспоминаете |
| Mental State | Душевное состояние |
| Roleplay Objective | Ролевая цель |
| amnesiac | без памяти; потеря памяти |
| Keeper Information | Информация для Хранителя |
| Involving the Players | Вовлечение игроков |
| Act 1 / 2 / 3 | Акт 1 / 2 / 3 |
| Antagonists | Противники |
| Concluding the nightmare | Конец кошмара |
| “Why shoot the Hound when we can shoot each other?” | «Зачем стрелять в Гончую, если можно друг в друга?» |
| “My Sanity is zero!” | «У меня ноль Рассудка!» |
| “Cut it out!” | «Вырежи его!» |
| ichor | ихор |
| PvP (inter-character conflict) | PvP (конфликт между персонажами) |
| emotional bleed | эмоциональный перенос |
| Idea roll | проверка Идеи |
| Hard / Extreme Dexterity roll | трудная / чрезвычайная проверка ЛВК |
| difficult Jump roll | трудная проверка Прыжков |
| Strength roll | проверка СИЛ |
| bonus (extra ‘tens’ die) | бонусная кость |
| wounding / lethal attack | ранящий / смертельный выстрел |
