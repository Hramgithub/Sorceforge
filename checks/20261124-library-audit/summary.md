# Сверка каталога библиотеки — итог (2026-11-24)

Проверено: 666 карточек `_описание.md` и 1019 PDF в `1_Библиотека` (только чтение; файлы библиотеки не менялись).
Подробно по разделам — `desc-scen1.md`, `desc-scen2.md`, `desc-coll.md`, `desc-sett.md`, `desc-mags.md`, `desc-misc.md`;
автоматический разбор редакций по текстовому слою — `editions.md` / `editions.json`; все строки про редакцию одним списком — `_edition-lines.txt`.

| Часть | Папок | С находками | Строк-находок |
|---|---|---|---|
| Сценарии 1 | 83 | 40 | 53 |
| Сценарии 2 | 82 | 38 | 38 |
| Сборники и кампании | 132 | 31 | 36 |
| Сеттинги | 136 | 67 | 37 |
| Журналы и монографии | 110 | 97 | 97 |
| Правила, атмосфера, прочее | 123 | 38 | 46 |
| **Всего** | **666** | **311** | **307** |

Карточек, описывающих совсем другое произведение, нет; есть карточки, описывающие лишь часть папки (раздатку вместо книги, один том из нескольких).

## 1. Редакция: метка «7e» на старой книге

Эти файлы ошибочно считались 7-й редакцией (часть из них уже ловили вручную):
Adventures in Arkham Country (1993), Curse of the Cthonians (updated, 2011, статы 6e), Masks of Nyarlathotep Companion (Bloody Tongue, фан под 6e),
Arkham Now — Sample Scenario (2010), Canis Mysterium (2013), Now Adv — Dockside Dogs (2012), Now Adv — Flesh for Eihort,
Finger Biter / The Drooler in the Dark / Brunholt Head / I Want You To Kill The Ice Cream Man (LaBossiere, один md5 под 6e и 7e),
Cthulhu Now — Secrets of Japan (2005), Punktown, Parapsychologist's Handbook (2003), Atomic Age Character Sheet,
«Призрак» `[RU 7e]` (перевод версии The Haunting 6e), «Посёлок Берёзовый» `[RU 7e]` (система СЫЩИК).
Не по системе «Зов Ктулху» при метке 7e: Matakishi's Tea House — Flame from Space и Threads (The Cthulhu Hack), Absinthe in Carcosa (The Yellow King RPG), Pulp Egypt (системно-нейтральная линейка), Fate, Stormbringer, Pokethulhu, «Миры ГФЛ», Cthulhu Wars.

## 2. Редакция: метка «6e» или «[EN]» на книге 7-й редакции — новые кандидаты для переноса (Р-251)

Ни одна из них не зарегистрирована в базе:
- **Convicts & Cthulhu** (Cthulhu Reborn, 2016–2018): основная книга, версия для игроков, выпуски Ticket of Leave (13 папок; #15 — версия без статов).
- **World War Cthulhu: Cold War** (2016) и дополнения Covert Actions, Our American Cousins, Section 46 Operations Manual; **World War Cthulhu: London** (2016).
- **Tails of Valor** (Cathulhu, Golden Goblin Press), **The Stars Are Right — Upgrade Pack** (2017), **Cthulhu Invictus — The Assignment** (Miskatonic Repository, 2020).
- **Hypergraphia Magazine 2** (2019), **Treasure for the Watcher**, **Vermis**, **In Strange Seas**, **Occam's Razor**, **The Last Valley (The Posse)**, **Dissociation** (`[EN]` → 7e).
- Также 7e, но с неверной карточкой: **Berlin — The Wicked City** (2019, 3 сценария; карточка описывает только раздатку).

## 3. Последствия для базы знаний

- **«Слабо» (сборник «Монстры Эдны», `[RU 7e]`, © 2020) — русский перевод The Dare** (Кевин Росс). The Dare перенесена в базу как английское произведение без перевода (`the-dare-en`, Р-251) и переведена в HTML. По Р-147 при существующем переводе текст должен идти из перевода, а оригинал давать числа. Нужно решение владельца: перевести `the-dare-en` на русский текст «Слабо» (официальные формы имён) или считать «Слабо» отдельной переработкой (у неё правила «Зова Ктулхёнка» для детей — сверить, совпадают ли они с «Зовом Кид-тулху» The Dare).
- **«Призрак»** (`prizrak-ru`) — перевод версии 6e; в базе уже отмечен как старое издание со статами текстом — подтверждено.
- **«Посёлок Берёзовый»** — в базе уже с другим набором правил (Trail of Cthulhu) — подтверждено.
- **Adventures in Arkham Country** — отложена, «Bless the Beasts and Children» есть в базе по переводу владельца (Р-223).
- Остальные перенесённые книги серии Р-251 проверены: их редакция 7e подтверждена (Petersen's Abominations, Nameless Horrors, London 3, Gothic by Gaslight, A Time to Harvest, The Star on the Shore и др.).

## 4. Что поправить в библиотеке (на решение владельца; ничего не сделано)

- **Метки** (`_edition-lines.txt`, 162 строки): старые книги под «7e» и 7e-книги под «6e» — см. разделы 1–2; 74 журнала и монографии до 2014 года под «[EN]» без редакции → «[EN 6e]»; фан-переводы под «[RU 7e]» → «[RU-фан 7e]» («Прочти и играй», подборка `Call_Of_Cthulhu_Материалы`, Pax Cthuliana); книги не по системе → `_Другие системы` (GURPS CthulhuPunk, Call of Catthulhu, Cthulhu Live ×2, All the World's Monsters 1–3, Deities & Demigods, d20-сценарии A Bridge Too Far и The Shadow in the Tree, Protodimension без материалов CoC).
- **Дубли:** одинаковые файлы под разными метками (Cthulhu-Fu, FBI Cthulhu Report, Cthulhu Weaponry 1–2, Business Cards / Monster Master Sheet, Тайны Кремля); одно произведение в двух папках (Лагерь Санни / Camp Sunny; Curse of Cthulhu / Грибы с Юггота; Secrets of Japan ×2; Цифровая эпоха → Petersen's Abominations; Dead Boarder и What's in the Cellar → Gateways to Terror; Dark Island, Ice Cream Man, War Buddy → 40 Adventures; Music of the Spheres → The Stars Are Right; Death in Luxor; woc1–5 → Worlds of Cthulhu); раздатка и прегены отдельными папками (A Time for Harvest, Stage Fright, The Derelict, Antarctic Expedition Kit → Beyond the Mountains of Madness).
- **Карточки** (описана часть папки): Особняки безумия (описан модуль Foundry), A Time for Harvest (эпизод 3 вместо кампании из 6; верное название A Time to Harvest), Horror on the Orient Express (только том III), Tournament of Shadows (только India), Монстры Эдны (одно из трёх), Стартовый набор, Маски (только машинный перевод), Berlin, Pulp Egypt, Книга хранителя / Компаньон / Малеус / Ширма (одно издание из нескольких), Тайник бутлегеров и Эликсир жизни (только раздатка), Dark Designs и Final Flight («скан без текста» — текст читается), Protodimension #21 (содержание из шаблона #18), White Dwarf Omnibus (3 сценария из 15+), «Ведомо ли любви прощение» (несуществующий третий сценарий).
- **Чужие файлы в папках:** The Howl of the Chimeras (газета Arkham Advertiser 2025 и бланки паспортов), Cults of Cthulhu (эссе 1987 г. вместо книги Chaosium), Miskatonic University (две разные книги), The Unspeakable Oath 23 (тексты выпусков #1–4), Багровые письмена (чужая иллюстрация), Монстры Эдны (пустая подпапка «1938 Тени Ленинграда»).
- **Издатель:** ~30 карточек называют Chaosium по строке о товарном знаке, хотя издатель другой.
- **3_КБ:** у 7 записей в имени неверный год (напр. «1990 Жертвы северных ветров» → 1926).

## Вопросы владельцу (по одному)

1. Править метки и карточки в библиотеке по этому списку (скриптом, с показом списка перед применением)?
2. Различать ли старые редакции (1-я–5-я) или всё до 7e метить «6e»?
3. «Слабо» = The Dare: перевести записи `the-dare-en` на русский текст «Слабо» по Р-147?
