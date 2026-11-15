# «What's in the Cellar?» (`whats-in-the-cellar-en`) — сверка полноты (Р-134, Р-251)

Часть `cellar`, вся книга. В PDF 18 страниц (задание называло 1–19; страницы 19 нет — `pdftoppm` отказывает, текстовый
слой пуст). Печатная страница = физической. Источник — английский оригинал; русский текст записей — наш перевод
(флаг `translated`). Записи — `kb/books/whats-in-the-cellar-en/` (40 записей): сценарий 1, сцены 11, персонажи 10
(4 готовых сыщика + 6 NPC), существо 1, предметы 9, раздатка 3, места 3, карты 2.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| What's in the Cellar? A One Hour Demo Scenario for Call of Cthulhu (обложка) | 1 | `scenario/whats-in-the-cellar` (sources); картинки обложки — `atmosphere.json` |
| Credits (выходные данные) | 2 | `scenario/whats-in-the-cellar` — автор и год в `summary`, источник с. 2; остальное — «Не взято» |
| Table of Contents | 3 | не взято — оглавление |
| What's in the Cellar? — «Will your investigators escape from the myserious tomb?» | 4 | `scenario/whats-in-the-cellar` |
| Overview | 4 | `scenario` — `summary`, `advice` («Время»), таблица «Части сценария», `steps` |
| Background | 4 | `scenario.keeper_info` («Предыстория»); `character/arthur-blackwood`, `rose-blackwood`, `joseph-klein`, `john-turner`, `helen-turner`; `location/blackwood-cabin` |
| The Truth | 4–5 | `scenario.keeper_info` («Правда»); `creature/creature-of-darkness` (`legend`); `character/milton-blackwood`; `item/blackwood-ring` |
| The Blackwood Cabin | 5 | `location/blackwood-cabin`, `location/blackwood-cellar`; `scenario.keeper_info` («Домик Блэквудов») |
| Keeper note: логика пола из ракушек | 5 | `scenario.advice`; `location/blackwood-cellar` |
| About the Investigators | 5 | `scenario.advice` («Готовые сыщики»); `character/clarke`, `rumberger`, `dr-pennyworth`, `hughes` |
| Set Up | 5–6 | `scene/set-up` (вступление целиком, обращение Артура, знакомство сыщиков); `scenario.hook`; `item/voice-recorder`, `item/cellar-photograph`; `location/klein-law-office` |
| Cellar Papers 1 (в тексте главы) | 6 | `handout/cellar-papers-1-herald-article` (дата «July 20th, 1928» — только в этой копии) |
| Start | 6 | `scene/start` |
| Keeper note: порядок улик | 6 | `scene/start`; `scenario.advice` |
| The Cellar | 6–7 | `scene/start` (текст для чтения вслух); `location/blackwood-cellar` |
| The Importance of Blood (врезка) | 7 | `scenario.keeper_info` («Важность крови»); `character/clarke`, `dr-pennyworth` |
| Searching the Cellar | 7 | `scene/searching-the-cellar`; `item/cellar-tools-and-weapons`; таблица сценария «Обыск погреба: находки» |
| Clue One: Floor Too Clean | 7 | `scene/clue-1-floor-too-clean` |
| Clue Two: Ladder and Floor | 7 | `scene/clue-2-ladder-and-floor` |
| Keeper's Cellar Map | 8 | `map/keepers-cellar-map` (`app/maps/cellar-keepers-map.jpg`, 12 меток: 1–8, Clue 2, 3, 4, 6) |
| Clue Three: Old Box | 9 | `scene/clue-3-old-box`; `item/milton-blackwood-portrait`, `item/milton-blackwood-journal` |
| Cellar Papers 2 (врезка) | 9 | `handout/cellar-papers-2-milton-journal` |
| Cellar Papers 3 (врезка) | 9 | `handout/cellar-papers-3-scrap-of-paper` |
| Clue Four: Scrapbook | 9 | `scene/clue-4-scrapbook`; `item/scrapbook` (5 заголовков статей) |
| Playing the Creature of Darkness | 9–10 | `scene/playing-the-creature`; `creature/creature-of-darkness` (`encounters`, `aura`, способность «Сила от убийств») |
| Keeper Note: Directing the Players (врезка) | 10 | `scene/playing-the-creature` (целиком); `scenario.advice` (кратко); `creature.encounters`; `character/dr-pennyworth` (`background.secret`) |
| Clue Five: Digging up the Floor | 10 | `scene/clue-5-digging-up-the-floor`; `item/rose-blackwood-skull` |
| Clue Six: Arcane Symbol | 10 | `scene/clue-6-arcane-symbol`; `item/arcane-symbol` |
| Clue Seven: Binding Ring | 10 | `scene/clue-7-binding-ring`; `item/blackwood-ring` |
| The Creature of Darkness, Manifestation of Hate and Malice | 11 | `creature/creature-of-darkness` (статблок, Special Powers → `abilities`, атаки, броня, заклинания, потеря Рассудка) |
| Conclusion and Rewards | 11 | `scenario.conclusion` (три награды Рассудка, благодарность игрокам) |
| Appendix A: Handouts — Cellar Papers 1–3 | 12 | `handout/cellar-papers-1…3` — текст и картинка (вырезка с с. 12) |
| Players' Cellar Map | 13 | `map/players-cellar-map` (`app/maps/cellar-players-map.jpg`, 7 меток-подписей) |
| Appendix B: Investigator Sheets — Clarke, Rumberger, Dr. Pennyworth, Hughes | 14 | `character/clarke`, `rumberger`, `dr-pennyworth`, `hughes` (`legend` — текст карточки и мотивация) |
| Лист сыщика: Rumberger | 15 | `character/rumberger` (статблок, картинка листа) |
| Лист сыщика: Clarke | 16 | `character/clarke` |
| Лист сыщика: Hughes | 17 | `character/hughes` |
| Лист сыщика: Dr. Pennyworth | 18 | `character/dr-pennyworth` |

## Не взято

- С. 2, выходные данные: редактор (Mike Mason), вёрстка (Nicholas Nacario), тестеры, копирайт и юридическая оговорка —
  не игровой материал (автор Jon Hook и год 2017 — в `summary` сценария).
- С. 3, оглавление — дублирует заголовки.
- Полиция штата Нью-Йорк и управление шерифа округа Вашингтон — упомянуты мимоходом (с. 4), записей
  `organization` не заведено; остались текстом в `keeper_info` сценария и в описании хижины.
- Ключ карты «S – Shelves» (с. 8): буквы S на плане нет — метка не ставится (пометка в записи карты).
- Ручей Касл-Крик, река Меттави, тропа Норт-Эш, округ Вашингтон, Уайтхолл — только упоминания; текстом в описании
  хижины и в предложении для `coc:location:new-york-environs`.
- Ключ от домика и письмо Клейна, разрешающее доступ, — без механики; текстом в сцене «Подготовка».
- Книги Мифов (`tome`) в сценарии нет: дневник Милтона Блэквуда без механики чтения — предмет `item/milton-blackwood-journal`.

## Картинки

- Раздатка 1–3 — вырезки с с. 12 (рамки — `handout-boxes.json`), листы сыщиков с. 15–18 — картинки `card` у
  прегенов (портретов в книге нет, только силуэт), карты с. 8 и 13 — `app/maps/cellar-*.jpg`. Предложения картинок
  (`art-proposals.json`) применены.
- Атмосфера (`atmosphere.json`, для `pipeline/art/merge_atmosphere.py`): с. 1 — обложка и логотипы; с. 6 — копия
  раздатки 1 в тексте главы. После слияния исчезнет единственная находка проверки полноты (`art.record_without`, с. 6).

## Проверки

- `python tools/check.py <40 записей>` — ошибок 0, предупреждений 0.
- `tools/completeness.py` (`completeness/`) — 1 находка: картинки с. 6 (копия раздатки 1) → в `atmosphere.json`.
- `tools/scenario_check.py` (`scenario/`) — 0 находок.
