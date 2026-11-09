# «Маски Ньярлатхотепа»: глава 7 «Китай», вторая часть (с. 568–618) — сверка заголовков

Часть `china-2` переноса «Масок» (Р-202). Книга `masks-of-nyarlathotep-en`, печатная страница = физическая − 3.
Этап — `masks-of-nyarlathotep-en/scenario/china` (заведён частью china-1); шаги второй части, `conclusion` и таблица
«Китай: награды» — в `proposals-china-2.json`. Префикс записей книги — `M/` = `masks-of-nyarlathotep-en/`.
Русские названия разделов, мест, организаций и предметов — по официальному русскому т. II (скан
`[RU 7e] Masks of Nyarlathotep т2 скан.pdf`; для этих страниц физ. = печ. − 386: печ. 568 = физ. 182, печ. 601 = физ. 215;
сверено по номерам на фото; распознано `tesseract -l rus`); тексты — наш перевод (`translated`); раздатки «Китай 6–12» —
официальные «Материалы для игроков» (`masks-of-nyarlathotep-ru-players`, с. 39–46). Имена персонажей — как в базе
(официально: Линь Енью, Джек Брейди, Хастон, Пэнхью, Исоге, Дуньдунь и Бин).

## Записи

| Вид | Записи |
|---|---|
| места (12) | Шанхай: `M/location/china-house-of-quiet-repose` (Дом тихого отдохновения, 31), `china-mu-hsien-house` (Дом Му Сяня, 27), `china-firm-action-warehouse` (склад «Решительных действий», 24), `china-autumn-morning-teahouse`; остров: `china-gray-dragon-island` (`область`, `part_of` Шанхай), `china-gray-dragon-village`, `china-gray-dragon-lookout-station`, `china-chamber-of-the-bloated-woman`, `china-the-cage`, `china-sacrificial-chamber`, `china-egyptian-room`, `china-sir-aubrey-workshop` |
| сцены (21) | этап, `arc.order` 23–43: `china-madam-swallow`, `recruitment-to-the-ranks`, `house-of-quiet-repose-break-in`, `mr-mu`, `recovering-the-seven-cryptical-books`, `new-china`, `firm-action-break-in`, `meeting-jack-brady`, `talking-to-jack-brady`, `eye-of-light-and-darkness`, `brady-and-choi-mei-ling`, `failing-to-meet-brady`, `pale-vipers-lair`, `new-china-assault-force`, `into-the-lagoon`, `trail-to-the-volcano`, `chamber-of-the-bloated-woman`, `sir-aubrey-workshop`, `rituals-of-the-order`, `special-ritual`, `foiling-the-ritual` |
| раздатки (7) | `M/handout/china-carlyle-papers-6` … `-12` |
| предметы (14) | `M/item/china-lin-yenyu-collection`, `china-lin-yenyu-ledger`, `china-brady-eye-fragment`, `china-firm-action-papers`, `china-sir-aubrey-rocket`, `china-rocket-trigger`, `china-rocket-warhead`, `china-rocket-guidance-system`, `china-rocket-plans`, `china-alien-welding-device`, `china-sir-aubrey-diaries`, `china-sir-aubrey-sarcophagus`, `china-gray-dragon-statue`, `china-mapulos` |
| организации (1) | `M/organization/china-new-china` («Новый Китай» / «Решительные действия») |
| карты (2) | `M/map/china-mu-hsien-house` (картинка `app/maps/masks-china-mu-hsien-house.jpg`, 1102×1500), `china-gray-dragon-island` (`app/maps/masks-china-gray-dragon-island.jpg`, 1089×709); 150 dpi, без меток |
| персонажи и существа | новых нет: все профили с. 602–617 уже в базе (связаны, не переписывались, Р-125) |
| таблицы с броском (`kb/tables/masks-china-*`) | нет: на с. 568–618 таблиц с броском нет; таблица наград — в `tables` этапа (предложение) |

Предложения (`proposals-china-2.json`, 66; пробный прогон `apply.py --dry-run` — все ложатся): этап `china` — 7 шагов,
правка шага «Шанхайский музей», `conclusion`, таблица «Китай: награды», 8 ссылок, правки `keeper_info` и `quality.notes`;
`conclusion-china` — `where` на остров и ссылка на ритуал; `campaign-marine-chronometers` — `found_at` мастерская;
ссылки из `england-rocket-components`, `china-ap-crates`, `egypt-nuri-stone`, `china-gray-dragon-island-chart`,
`china-special-storeroom-artifacts`, мест и сцен первой части, ордена Опухшей дамы (+ `based_at` остров), ключа карты
Шанхая (24, 27, 31); «Юэюань-роад» → официальное «Ююань-роад» (3 правки); официальные псевдонимы (11).

## Заголовок книги → где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Madam Swallow (связки) | 568 | сцена `china-madam-swallow`; `china-house-of-quiet-repose`; шаг этапа «Мадам Ласточка» |
| Lin Yenyu’s Shanghai home (House of Quiet Repose), её наёмники, знак ласточки | 568 | `china-house-of-quiet-repose`; сцена `china-madam-swallow`; существующий `character/nefarious-hirelings-of-lin-yenyu` |
| Pulp: Simian Intervention | 568 | сцена `china-madam-swallow` (`mechanics`); существующие `creature/tun-tun`, `ping` |
| An Interview with Lin Yenyu | 568–569 | сцена `china-madam-swallow` |
| Pulp: Silent Witnesses | 569 | сцена `china-madam-swallow` (`mechanics`) |
| Possession of the Seven Cryptical Books of Hsan; Keeper note | 569–570 | сцена `china-madam-swallow` |
| Madam Lin’s Collection (врезка) | 570 | `item/china-lin-yenyu-collection` |
| Offering to Sell an Artifact | 570 | сцена `china-madam-swallow` |
| Pulp: Rude Investigators | 570 | сцена `china-madam-swallow` (`mechanics`) |
| The Eye of Light and Darkness (у мадам Линь) | 570–571 | сцена `china-madam-swallow`; `item/china-brady-eye-fragment` |
| Recruitment to the Ranks | 571 | сцена `china-recruitment-to-the-ranks` |
| Carlyle Papers China #6 | 571 | `handout/china-carlyle-papers-6` |
| Showered With Gifts | 572 | сцена `china-recruitment-to-the-ranks` |
| Pulp: Kidnapped | 572 | сцена `china-recruitment-to-the-ranks` (`mechanics`); поместье в Гуйлине — текст в `china-house-of-quiet-repose` |
| Talking to Lin Yenyu | 572–573 | сцена `china-madam-swallow` |
| Alternative Means of Entry | 573 | сцена `china-house-of-quiet-repose-break-in`; `item/china-lin-yenyu-ledger` |
| Mr. Mu (связки) | 573 | сцена `china-mr-mu`; `china-mu-hsien-house`; шаг «Господин Му» |
| Talking to Mu Hsien | 573–574 | сцена `china-mr-mu` |
| Recovering the Seven Cryptical Books | 574 | сцена `china-recovering-the-seven-cryptical-books`; ловушки — `china-mu-hsien-house` |
| Mu Hsien’s House map (China Map #5, пояснения 1–7) | 575 | `map/china-mu-hsien-house`; легенда — описание `china-mu-hsien-house` |
| New China | 576 | `organization/china-new-china`; `china-firm-action-warehouse`; сцена `china-new-china` |
| Getting Acquainted; Tailed and Kidnapped | 576 | сцена `china-new-china` |
| Breaking In; Keeper note (Autumn Morning) | 577 | сцена `china-firm-action-break-in`; `item/china-firm-action-papers`; `china-autumn-morning-teahouse` |
| Chase Quick Reference: Chu Min; Average Firm Action Members | 577 | сцена `china-new-china` (`mechanics`) |
| Carlyle Papers China #7 | 577 | `handout/china-carlyle-papers-7` |
| Meeting Jack Brady (связки, убежище) | 577–578 | сцена `china-meeting-jack-brady`; шаг «Встреча с Джеком Брэди» |
| Keeper note (пересказать Китай 8) | 578 | сцена `china-meeting-jack-brady` |
| Talking to Jack Brady; One God, Many Faces; Battle Plans; A Real Eye Opener | 578 | сцена `china-talking-to-jack-brady`; `item/china-brady-eye-fragment` |
| On The Eye of Light and Darkness; Creating the Eye; Breaking the Ward | 578–580 | сцена `china-eye-of-light-and-darkness` |
| Deciphering the Seven Cryptical Books (врезка) | 579 | сцена `china-eye-of-light-and-darkness` (`mechanics`) |
| Brady and Choi Mei-Ling | 580 | сцена `china-brady-and-choi-mei-ling` |
| Failing to Meet Brady | 580 | сцена `china-failing-to-meet-brady` |
| Carlyle Papers China #8 (3 страницы) | 581–583 | `handout/china-carlyle-papers-8` |
| Carlyle Papers China #9 | 584 | `handout/china-carlyle-papers-9` |
| Gray Dragon Island (связки, атолл) | 585 | `china-gray-dragon-island`; сцена `china-pale-vipers-lair` |
| Gray Dragon Island map (пояснения 1–5; план покоя 6–17; Lagoon Details) | 585 | `map/china-gray-dragon-island`; легенда — описание `china-gray-dragon-island`; `number` у мест |
| Destination: The Pale Viper’s Lair | 585–586 | сцена `china-pale-vipers-lair` |
| The New China Assault Force; A Likely Scenario | 586 | сцена `china-new-china-assault-force` |
| Into the Lagoon | 586 | сцена `china-into-the-lagoon`; `china-gray-dragon-island` |
| Pulp: Attack of the Sand Crabs! | 587 | сцена `china-into-the-lagoon` (`mechanics`); существующий `creature/sand-crab-swarm` |
| The Village; The Lookout Station; Deep One Colony | 587 | `china-gray-dragon-village`, `china-gray-dragon-lookout-station`, `china-gray-dragon-island`; сцена `china-into-the-lagoon` |
| The Trail to the Volcano | 587 | сцена `china-trail-to-the-volcano` |
| To the Heart of the Volcano; The Chamber of the Bloated Woman | 587–588 | `china-chamber-of-the-bloated-woman`; сцена `china-chamber-of-the-bloated-woman` |
| Radiation in the Chamber; Pulp: Radiation | 588 | сцена `china-chamber-of-the-bloated-woman` (`mechanics`) |
| Sir Aubrey’s Rocket | 588–589 | `item/china-sir-aubrey-rocket`; сцена `china-chamber-of-the-bloated-woman` |
| Parts and Storage | 589 | `item/china-alien-welding-device` |
| The Pools; Keeper note | 589 | `china-chamber-of-the-bloated-woman`; сцена; существующий `character/twsha-controlled-slave` |
| Pulp: Shoggoth | 590 | сцена `china-chamber-of-the-bloated-woman` (`mechanics`); существующий `creature/the-shoggoth-reassembled-horror` |
| The Cage | 590 | `china-the-cage` |
| The Statue | 590 | `item/china-gray-dragon-statue` |
| The Sacrificial Chamber | 590 | `china-sacrificial-chamber` |
| The Egyptian Room (погребальная камера, саркофаг) | 590 | `china-egyptian-room`; `item/china-sir-aubrey-sarcophagus` |
| Sir Aubrey’s Workshop | 590–591 | `china-sir-aubrey-workshop`; сцена `china-sir-aubrey-workshop` |
| The Shoggoth-Twsha (врезка) | 591 | `item/china-mapulos`; существующие `coc:creature:shoggoth-twsha`, `creature/shoggoth-twsha-masks` |
| The Trigger; Pulp: More Weird Science | 591–592 | `item/china-rocket-trigger` |
| The Warhead | 592 | `item/china-rocket-warhead` |
| The Guidance System | 592 | `item/china-rocket-guidance-system` |
| The Plans (вместе с «Великая Раса», «Хэнсон», военные) | 592, 594 | `item/china-rocket-plans` |
| Carlyle Papers China #10 | 593 | `handout/china-carlyle-papers-10` |
| Carlyle Papers China #11 | 594 | `handout/china-carlyle-papers-11` |
| The Chronometer; Keeper note | 594–595 | `china-sir-aubrey-workshop`; сцена `china-sir-aubrey-workshop`; существующий `item/campaign-marine-chronometers` (предложен `found_at`) |
| The Tools; Keeper note | 595 | `china-sir-aubrey-workshop`; сцена `china-sir-aubrey-workshop` |
| Sir Aubrey’s Diaries; Keeper note | 595 | `item/china-sir-aubrey-diaries` |
| Carlyle Papers China #12 | 595 | `handout/china-carlyle-papers-12` |
| The Divine Wind | 596 | сцена `china-sir-aubrey-workshop` |
| Rituals of the Order; Death Rites; Breeding Rites | 596 | сцена `china-rituals-of-the-order` |
| The Bloated Woman (врезка со строфой «Goddess of the Black Fan») | 597 | сцена `china-rituals-of-the-order`; существующие `creature/bloated-woman-masks`, `coc:creature:bloated-woman` |
| The Special Ritual on the Day of Opening; Keeper note | 596–598 | сцена `china-special-ritual` |
| Foiling the Ritual of Opening; Messing with Time | 598 | сцена `china-foiling-the-ritual` |
| Back to Basics (врезка) | 599 | сцена `china-foiling-the-ritual` |
| Destroying the Trigger / the Guidance System / the Warhead / the Rocket | 599 | `item/china-rocket-trigger`, `-guidance-system`, `-warhead`, `china-sir-aubrey-rocket`; сцена `china-foiling-the-ritual` |
| Pulp: Kaboom!; Destroying the Volcano; Pulp: Escape!; Running the Numbers | 600 | сцена `china-foiling-the-ritual` |
| Partial Victories | 601 | сцена `china-foiling-the-ritual`; этап `conclusion` (предложение) |
| Conclusion | 601 | этап `conclusion` (предложение) |
| Rewards; Bringing Down a God: China; Pulp: Rewards | 601 | этап: таблица «Китай: награды», `conclusion` (предложения) |
| Characters and Monsters: China (вступление, союзники, противники, культисты, чудовища) | 602–617 | существующие записи: `character/li-wen-cheng`, `fergus-chum`, `isoge-taro`, `anthony-chang`, `auntie-gees-goons`, `lin-yenyu`, `nefarious-hirelings-of-lin-yenyu`, `mu-hsien`, `choi-mei-ling`, `jack-brady`, `chu-min`, `firm-action-warehouse-guards`, `fighters-for-the-new-china-to-come`, `green-gang-member`, `ho-fang`, `ho-tzu-hsi`, `carl-stanford`, `jules-savoyard`, `sir-aubrey-penhew`, `average-cultist-of-the-bloated-woman-china`, `twsha-controlled-slave`; существа `tun-tun`, `ping`, `sand-crab-swarm`, `shoggoth-twsha-masks`, `bloated-woman-masks`, `mutant-crab-clawed-deep-one`, `the-shoggoth-reassembled-horror`, `crazed-crew-of-the-dark-mistress`, `villager-hybrids-on-gray-dragon-island`, `dire-deep-ones-of-gray-dragon-island` |
| Madam Lin’s Poisons (врезка) | 605 | существующий `character/nefarious-hirelings-of-lin-yenyu` (умение «Яды мадам Линь»); упомянуты в `china-house-of-quiet-repose`, `item/china-lin-yenyu-ledger` |
| Talking to the Dead (вариант «Повелевать призраком» у Му Сяня) | 606 | существующий `character/mu-hsien` (уже описан) |
| Иллюстрации на всю страницу | 615, 618 | не взято (см. ниже) |

## Строки аудита `checks/20261025-masks/not_in_kb.md` (с. 568–618)

| Строка аудита | Что взяло |
|---|---|
| Chase QR: Chu Min и Average Firm Action Members (580/577) | сцена `china-new-china` (`mechanics`): поля `chase` у персонажа нет |
| Madam Lin’s Poisons (608/605) | уже в `character/nefarious-hirelings-of-lin-yenyu` (умение) |
| Rewards: награды по главам — Китай (604/601) | этап: таблица «Китай: награды» (предложение) |
| Marine Chronometers (598/595) | `item/campaign-marine-chronometers`: предложен `found_at` мастерская; `china-sir-aubrey-workshop` |
| Sir Aubrey’s Rocket (+ Guidance System, Warhead, пусковой механизм) (591–595/588–592) | `item/china-sir-aubrey-rocket`, `china-rocket-trigger`, `china-rocket-warhead`, `china-rocket-guidance-system`, `china-rocket-plans`; сцена `china-foiling-the-ritual` |
| Gate Box (Carl Stanford) (613/610) | `item/china-stanford-gate-box` (часть china-1); профиль Стэнфорда — существующий |
| China #6, #7, #8, #9, #10, #11, #12 | `handout/china-carlyle-papers-6` … `-12` (у #9 в аудите ошибочно «обломок печати Красной пирамиды» — это отрывок «Семи книг» об Оке) |
| Карты: Mu Hsien’s House, Gray Dragon Island (578, 588 физ.) | `map/china-mu-hsien-house`, `map/china-gray-dragon-island` |
| Дом Madam Lin Yenyu, коллекция (571–575/568–572) | `china-house-of-quiet-repose`; `item/china-lin-yenyu-collection` |
| Дом Mu Hsien (576–578/573–575) | `china-mu-hsien-house` |
| Штаб New China / Firm Action, чайная Autumn Morning (579–580/576–577) | `china-firm-action-warehouse`, `china-autumn-morning-teahouse` |
| Gray Dragon Island (588–603/585–600) | `china-gray-dragon-island` и 7 мест на нём |
| Firm Action / New China (579/576, 610/607) | `organization/china-new-china` |
| «Talking to the Dead» (609/606) | уже в `character/mu-hsien` |
| Deciphering the Seven Cryptical Books (582/579) | сцена `china-eye-of-light-and-darkness`; `handout/china-carlyle-papers-9` (в записи книги `coc:tome:seven-cryptical-books-of-hsan` экземпляр у Му уже есть) |
| Radiation (с пульп-врезкой) (591/588) | сцена `china-chamber-of-the-bloated-woman` (`mechanics`) |
| Пульп-врезка More Weird Science (595/592) | `item/china-rocket-trigger`, `china-rocket-plans` (`mechanics`) |
| Rituals of the Order; The Special Ritual on the Day of Opening (599/596) | сцены `china-rituals-of-the-order`, `china-special-ritual` |
| Conclusion: Partial Victories (604/601) | сцена `china-foiling-the-ritual`; этап `conclusion` (предложение) |

## Опечатки и расхождения книги

| Где | Напечатано | Ожидалось | Запись |
|---|---|---|---|
| с. 601, врезка «Pulp: Rewards» | только вступление «In addition, apply the following rewards…», списка нет | пульп-награда | в официальном т. II (физ. 215): «Хранитель может дать героям 10 пунктов Удачи за завершение главы» — взято оттуда с пометкой (предложения этапа) |
| с. 601 | «Chapter 4: Kenya», «Chapter 3: Egypt» | Кения — глава 5, Египет — глава 4 | ссылка не туда; в записях — названия глав без номеров |
| официальные «Материалы», Китай 12 | «8 апреля 1922», «4 октября 1922» | «8th April, 1923», «4th October, 1923» (с. 595) | `errata` в `handout/china-carlyle-papers-12` (текст оставлен как в официальном) |
| официальные «Материалы», Китай 11 | «ЛИЧНАЯ ИНФОРМАЦИЯ» | «P. V.» (Pale Viper) | пометка в `handout/china-carlyle-papers-11` |
| официальный т. II, с. 590 | трудная проверка Внимания (паз египетской комнаты) | обычная («A successful Spot Hidden roll») | взято по оригиналу; пометка в `china-egyptian-room` |
| официальный т. II, с. 599 | незаметная порча механизма — обычная проверка Науки | трудная («Hard success») | взято по оригиналу; пометка в `item/china-rocket-trigger` |
| официальный т. II, с. 592 | «повернуть … на 60 градусов» | «a half-turn to the right» | взято по оригиналу; пометка в `item/china-rocket-warhead` |
| официальный т. II, с. 588 | «десяток культистов» на платформах | «half a dozen» | взято по оригиналу; пометка в сцене |
| с. 572 | «Kweilin», затем «Kwellin» | одно название | мелкое, не записано (Р-39) |
| с. 574 | «”Tulu, Ni-og-tha, Yog-So-thoth, and Aza-thoth” (sic)» | так задумано книгой | оставлено, «(так в книге)» |
| с. 588, 592, 601 | лишняя кавычка «skullcaps.”», «similiarity», «shoggoth-twsha,:» | — | мелкое, не записано (Р-39) |
| база | «Юэюань-роад» в записях первой части | официальное «Ююань-роад» | предложены замены |
| база | «Решительное действие» в записях персонажей | официальное «Решительные действия» | в новых записях — официальное; предложены псевдонимы |

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Иллюстрации: «Meeting Madam Swallow», «The Eye of Light and Darkness», «Talking to Jack Brady and Chu Min», «The Shoggoth Twsha», портреты, разворотные иллюстрации (открытие Великих врат, с. 615; ракета, с. 618) | 569–618 | картинки добавляются отдельно (`pipeline/art/add_images.py`, Р-165); содержание описано текстом |
| Символ Ока, нарисованный в раздатке Китай 8 | 582 | картинка; символ — в раздатке Египет 2 и записи заклинания |
| Запись персонажа Сун Лэ (Sung Lee, спонсор «Нового Китая»), отчисленного курсанта академии Вампу, господина Фэн Убэя (псевдоним Му — уже `aliases` у `mu-hsien`) | 574, 576 | упомянуты мимоходом, без профиля и действий; текст в `organization/china-new-china` (кандидаты — в отчёте) |
| Запись места «поместье Линь Яньюй в Гуйлине» | 572 | только пульп-врезка, без описания; текст в `china-house-of-quiet-repose` и сцене вербовки |
| Записи мест: пристань (4), подводный (3) и наземный (5) входы, склад с деталями (6), озёра (7–9), погребальная камера (17), пещера-вход | 585–590 | части острова и покоя без своих сцен — описаны в `china-gray-dragon-island`, `china-chamber-of-the-bloated-woman`, `china-egyptian-room` (`number` — у мест с собственными записями) |
| Запись оружия «Неземной сварочный аппарат» в `kb/weapons/` | 589 | общий справочник — не моя часть; механика — в `item/china-alien-welding-device` (кандидат) |
| Книга сэра Уэйда Джермина «Обзор некоторых регионов Африки» как запись тома | 570 | в справочнике томов её нет, механики книга не даёт; текст в `item/china-lin-yenyu-collection` |
| Статблоки с. 602–617 | 602–617 | существующие записи (Р-125: не переписывались); сверка профилей не входила в часть |
| Метки на картах (`spots`) | 575, 585 | по Р-202 карты без меток; легенды — в описаниях мест, `number` у мест |
