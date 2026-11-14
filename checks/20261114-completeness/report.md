# Полнота перенесённых книг — 2026-11-14

Создано `python tools/completeness.py`; база не менялась. Пороги: страница с текстом — от 120 слов; картинка — от 250×250, повторённые на 3+ страницах не считаются.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `text.gap` | Страницы с текстом, которые не цитирует ни одна запись | 116 |
| `art.uncovered` | Картинки книги на странице, где ни одна запись не несёт картинку | 135 |
| `art.record_without` | Страница с картинкой, которую не несёт ни одна запись, а персонаж, существо, раздатка, предмет или книга этой страницы — без `images` | 129 |
| `links.character_unused` | Персонаж без связей: ни сцена, ни сценарий, ни другая запись на него не ссылаются, своих связей нет | 0 |
| `links.scene_no_place` | Сцена без места (`where`) | 60 |
| `links.unused` | Раздатка или предмет, которые не использует ни сцена, ни сценарий | 0 |
| `context.no_description` | Запись без описания | 21 |
| `context.handout_empty` | Раздатка без текста и без картинки | 4 |
| `context.scenario_thin` | Сценарий без краткого содержания (`summary`) или сведений для хранителя (`keeper_info`/`steps`) | 0 |
| `context.incomplete` | Запись помечена `incomplete` | 156 |

## Книги

| Книга | Язык | Текст | Стр. | Записей | Цитир. стр. | Стр. без записей (слов) | Стр. с картинками | без записи | Находок |
|---|---|---|---|---|---|---|---|---|---|
| Keeper Rulebook (англ.) (`keeper-rulebook-en`) | en | текст | 439 | 594 | 250 | 133 (74061) | 326 | 0 | 12 |
| Cthulhu Dark Ages (7e, предварительная версия — не изданная книга) (`cthulhu-dark-ages-en`) | en | текст | 215 | 289 | 75 | 125 (64151) | 97 | 0 | 13 |
| Malleus Monstrorum, т. II (`malleus-monstrorum-2-en`) | en | текст | 267 | 156 | 201 | 43 (21154) | 82 | 0 | 46 |
| Книга хранителя (`keeper-rulebook-ru`) | ru | текст | 400 | 1079 | 355 | 25 (9022) | 17 | 0 | 29 |
| Malleus Monstrorum, т. I (`malleus-monstrorum-1-en`) | en | текст | 219 | 276 | 180 | 18 (5971) | 83 | 0 | 17 |
| Pulp Cthulhu (`pulp-cthulhu-en`) | en | текст | 275 | 875 | 241 | 16 (5046) | 113 | 14 | 20 |
| Arkham (Chaosium, 2023) (`arkham-en`) | en | текст | 275 | 1021 | 232 | 12 (4536) | 188 | 0 | 19 |
| Ктулху: Тёмные века (фанатский перевод 2-го издания 7e) (`temnye-veka-tri-stsenariya-ru`) | ru | текст | 275 | 675 | 232 | 12 (2894) | 132 | 12 | 15 |
| Grand Grimoire of Cthulhu Mythos Magic (`grand-grimoire-en`) | en | текст | 203 | 571 | 166 | 10 (2493) | 38 | 0 | 3 |
| Keeper's Companion (англ., 7e) (`keepers-companion-en`) | en | текст | 227 | 520 | 200 | 11 (2462) | 105 | 8 | 13 |
| Маски Ньярлатхотепа (англ., 7e, т. I–II) (`masks-of-nyarlathotep-en`) | en | текст | 670 | 1571 | 629 | 12 (2207) | 330 | 67 | 71 |
| Особняки безумия. За закрытыми дверями (`osobnyaki-bezumiya-ru`) | ru | OCR | 226 | 488 | 211 | 7 (1465) | 0 | 0 | 8 |
| Dead Light and Other Dark Turns (`dead-light-en`) | en | текст | 91 | 142 | 78 | 5 (1068) | 74 | 10 | 12 |
| Миры Говарда Филлипса Лавкрафта: артефакты и легендарные… (`miry-lavkrafta-artefakty-ru`) | ru | текст | 125 | 46 | 90 | 6 (977) | 5 | 5 | 9 |
| Pax Cthuliana (`pax-cthuliana-ru`) | ru | текст | 73 | 86 | 67 | 1 (795) | 71 | 0 | 3 |
| Fear's Sharp Little Needles (`fears-sharp-little-needles-en`) | en | текст | 201 | 957 | 184 | 2 (719) | 119 | 10 | 42 |
| Путеводитель по Аркхэму (Hort, по Arkham Unveiled) (`arkham-guide-hort-ru`) | ru | текст | 112 | 396 | 103 | 5 (704) | 14 | 0 | 1 |
| Beyond the Edge of Darkness (`beyond-the-edge-of-darkness-en`) | en | текст | 38 | 72 | 31 | 2 (617) | 28 | 0 | 6 |
| Три кошмарных вечера (No Time to Scream) (`tri-koshmarnykh-vechera-ru`) | ru | текст | 106 | 159 | 98 | 2 (578) | 88 | 0 | 2 |
| Women of the French Revolution (`reign-of-terror-women-en`) | en | текст | 12 | 24 | 8 | 2 (577) | 8 | 0 | 1 |
| Царство Террора (`tsarstvo-terrora-ru`) | ru | текст | 126 | 290 | 110 | 1 (472) | 75 | 7 | 13 |
| Наедине с приливом: правила (`naedine-s-prilivom-rules-ru`) | ru | текст | 10 | 1 | 7 | 1 (393) | 5 | 5 | 6 |
| Ведомо ли любви прощение Ктулху (`vedomo-li-lyubvi-ru`) | ru | текст | 62 | 90 | 51 | 2 (368) | 35 | 11 | 13 |
| Мифы Хастура. Том 1: Путь в Каркозу (`mify-hastura-ru`) | ru | OCR | 46 | 55 | 39 | 2 (326) | 0 | 0 | 8 |
| Погасший маяк (`lightless-beacon-ru`) | ru | текст | 44 | 78 | 38 | 1 (241) | 37 | 3 | 4 |
| The Cursed Idol of Manco Capác (`cursed-idol-of-manco-capac-en`) | en | текст | 53 | 138 | 43 | 1 (232) | 48 | 2 | 3 |
| Побег из Иннсмута (`pobeg-iz-innsmuta-ru`) | ru | текст | 188 | 562 | 182 | 1 (190) | 56 | 16 | 25 |
| The Innsmouth Terror (`innsmouth-terror-en`) | en | текст | 47 | 83 | 41 | 1 (164) | 36 | 2 | 3 |
| Месяц Ночи (`mesyats-nochi-ru`) | ru | текст | 47 | 93 | 41 | 1 (162) | 29 | 0 | 1 |
| Новая жизнь (`novaya-zhizn-ru`) | ru | текст | 29 | 57 | 25 | 1 (151) | 21 | 1 | 5 |
| Arkham: Arkham Advertiser insert (`arkham-advertiser-en`) | en | скан | 4 | 4 | 4 | 0 (0) | 4 | 0 | 0 |
| Arkham: insert maps (`arkham-insert-maps-en`) | en | скан | 4 | 3 | 3 | 0 (0) | 4 | 1 | 1 |
| Arkham: floorplans (Keeper) (`arkham-maps-en`) | en | текст | 34 | 36 | 27 | 0 (0) | 33 | 0 | 0 |
| Аукцион (`auktsion-ru`) | ru | текст | 49 | 93 | 48 | 0 (0) | 20 | 0 | 1 |
| Аутофагия (`autofagiya-ru`) | ru | текст | 37 | 61 | 33 | 0 (0) | 24 | 0 | 0 |
| Безымянный туман (`bezymyannyy-tuman-ru`) | ru | текст | 8 | 71 | 7 | 0 (0) | 7 | 3 | 8 |
| Bless the Beast and Children (перевод владельца) (`bless-the-beast-and-children-ru`) | ru | скан | 15 | 92 | 15 | 0 (0) | 7 | 0 | 1 |
| Черная кассета (`chernaya-kasseta-ru`) | ru | текст | 17 | 38 | 16 | 0 (0) | 16 | 0 | 1 |
| Черноводный ручей (`chernovodnyy-ruchey-ru`) | ru | скан | 99 | 196 | 94 | 0 (0) | 0 | 0 | 0 |
| Чулки возле печки (`chulki-vozle-pechki-ru`) | ru | текст | 18 | 68 | 16 | 0 (0) | 1 | 0 | 1 |
| Реестр терминов владельца (`coc-terminology`) | ru | скан | 0 | 429 | 0 | 0 (0) | 0 | 0 | 0 |
| Curious Characters Deck (`curious-characters-deck-en`) | en | скан | 30 | 47 | 23 | 0 (0) | 0 | 0 | 0 |
| Кошмары цифровой эпохи: готовые персонажи (`digital-nightmares-pregens-ru`) | ru | скан | 36 | 30 | 30 | 0 (0) | 0 | 0 | 0 |
| Двери во тьму: готовые персонажи (`dveri-vo-tmu-pregens-ru`) | ru | скан | 11 | 10 | 10 | 0 (0) | 1 | 1 | 1 |
| Двери во тьму (`dveri-vo-tmu-ru`) | ru | скан | 142 | 322 | 111 | 0 (0) | 0 | 0 | 1 |
| Джонни бой (`dzhonni-boy-ru`) | ru | текст | 9 | 34 | 8 | 0 (0) | 3 | 0 | 0 |
| Экспонат новая жизнь (`eksponat-novaya-zhizn-ru`) | ru | текст | 21 | 35 | 18 | 0 (0) | 15 | 2 | 2 |
| Эликсир жизни (`eliksir-zhizni-ru`) | ru | скан | 12 | 79 | 12 | 0 (0) | 12 | 4 | 8 |
| Грибы с Юггота (`griby-s-yuggota-ru`) | ru | текст | 101 | 441 | 98 | 0 (0) | 50 | 0 | 19 |
| Хэллоуин в Данвиче (`hellouin-v-danviche-ru`) | ru | текст | 19 | 66 | 17 | 0 (0) | 2 | 0 | 1 |
| Домашние правила (`house-rules`) | ru | скан | 0 | 5 | 0 | 0 (0) | 0 | 0 | 0 |
| Идол Тота (`idol-tota-ru`) | ru | скан | 24 | 65 | 21 | 0 (0) | 0 | 0 | 0 |
| Книга сыщика (`investigator-handbook-ru`) | ru | скан | 269 | 187 | 42 | 0 (0) | 0 | 0 | 0 |
| Каникулы в Иннсмуте (`kanikuly-v-innsmute-ru`) | ru | текст | 9 | 50 | 8 | 0 (0) | 4 | 0 | 1 |
| Карнавал безумия (`karnaval-bezumiya-ru`) | ru | текст | 98 | 212 | 95 | 0 (0) | 44 | 5 | 9 |
| Холодный урожай: готовые персонажи (`kholodnyy-urozhay-pregens-ru`) | ru | скан | 16 | 10 | 16 | 0 (0) | 1 | 0 | 0 |
| Холодный урожай (`kholodnyy-urozhay-ru`) | ru | текст | 64 | 111 | 62 | 0 (0) | 10 | 0 | 0 |
| Когда зажигаются костры (`kogda-zazhigayutsya-kostry-ru`) | ru | текст | 25 | 51 | 24 | 0 (0) | 14 | 0 | 0 |
| Когда зло побеждает (`kogda-zlo-pobezhdaet-ru`) | ru | текст | 15 | 41 | 10 | 0 (0) | 6 | 4 | 6 |
| Кошмарный прилив: готовые персонажи (`koshmarnyy-priliv-pregens-ru`) | ru | скан | 6 | 2 | 4 | 0 (0) | 2 | 0 | 0 |
| Лагерь Санни (`lager-sanni-ru`) | ru | текст | 29 | 67 | 28 | 0 (0) | 2 | 1 | 1 |
| Лечебница (`lechebnitsa-ru`) | ru | текст | 32 | 117 | 31 | 0 (0) | 3 | 0 | 2 |
| Лес Вендиго: готовые персонажи (`les-vendigo-pregens-ru`) | ru | скан | 10 | 5 | 10 | 0 (0) | 4 | 0 | 0 |
| Лохмотья Короля (`lokhmotya-korolya-ru`) | ru | текст | 360 | 455 | 355 | 0 (0) | 83 | 6 | 13 |
| Маленький клуб ужасов (`malenkiy-klub-uzhasov-ru`) | ru | текст | 21 | 66 | 19 | 0 (0) | 15 | 6 | 6 |
| Malleus Keeper Deck (`malleus-keeper-deck-en`) | en | скан | 71 | 65 | 65 | 0 (0) | 0 | 0 | 0 |
| Маски Ньярлатхотепа, т. II (рус.) (`masks-of-nyarlathotep-ru-2`) | 2 | скан | 235 | 4 | 2 | 0 (0) | 0 | 0 | 0 |
| Маски Ньярлатхотепа: материалы для игроков (рус.) (`masks-of-nyarlathotep-ru-players`) | players | текст | 98 | 131 | 60 | 0 (0) | 40 | 1 | 1 |
| Мертвенный свет: готовые персонажи (`mertvennyy-svet-pregens-ru`) | ru | скан | 18 | 6 | 18 | 0 (0) | 0 | 0 | 0 |
| Mothers Love (перевод владельца) (`mothers-love-ru`) | ru | скан | 15 | 73 | 15 | 0 (0) | 8 | 0 | 0 |
| Моя маленькая сестра (`moya-malenkaya-sestra-ru`) | ru | текст | 35 | 70 | 34 | 0 (0) | 17 | 0 | 0 |
| МТС Харьков 37 (`mts-kharkov-37-ru`) | ru | текст | 94 | 144 | 91 | 0 (0) | 16 | 0 | 5 |
| Набор хранителя: готовые персонажи (`nabor-khranitelya-pregens-ru`) | ru | скан | 0 | 12 | 0 | 0 (0) | 0 | 0 | 0 |
| Наедине с Хэллоуином: шкала времени и карта (`naedine-s-hellouinom-map-ru`) | ru | скан | 1 | 1 | 1 | 0 (0) | 1 | 0 | 0 |
| Наедине с Хэллоуином (Alone on Halloween) (`naedine-s-hellouinom-ru`) | ru | текст | 255 | 109 | 253 | 0 (0) | 42 | 0 | 4 |
| Стартовый набор: Наедине с пламенем (простая версия) (`naedine-s-plamenem-ru`) | ru | текст | 72 | 38 | 72 | 0 (0) | 1 | 0 | 2 |
| Наедине с помехами: журнал (`naedine-s-pomekhami-journal-ru`) | ru | текст | 2 | 1 | 1 | 0 (0) | 0 | 0 | 0 |
| Наедине с помехами: Чарли (лист персонажа) (`naedine-s-pomekhami-pregens-2-ru`) | ru | текст | 4 | 1 | 2 | 0 (0) | 2 | 2 | 2 |
| Наедине с помехами: Алекс (лист персонажа) (`naedine-s-pomekhami-pregens-ru`) | ru | текст | 4 | 2 | 2 | 0 (0) | 2 | 0 | 0 |
| Наедине с помехами (`naedine-s-pomekhami-ru`) | ru | текст | 192 | 34 | 192 | 0 (0) | 46 | 10 | 10 |
| Наедине с приливом (Alone Against the Tide) (`naedine-s-prilivom-ru`) | ru | текст | 91 | 37 | 91 | 0 (0) | 37 | 2 | 4 |
| Наедине с тьмой: список адресов (`naedine-s-tmoy-addresses-ru`) | ru | текст | 3 | 49 | 2 | 0 (0) | 2 | 0 | 0 |
| Наедине с тьмой: календарь (`naedine-s-tmoy-calendar-ru`) | ru | скан | 2 | 1 | 2 | 0 (0) | 2 | 2 | 2 |
| Наедине с тьмой: раздатка (`naedine-s-tmoy-handouts-ru`) | ru | скан | 3 | 1 | 2 | 0 (0) | 3 | 3 | 3 |
| Наедине с тьмой: готовые персонажи (`naedine-s-tmoy-pregens-ru`) | ru | скан | 6 | 4 | 4 | 0 (0) | 6 | 2 | 2 |
| Наедине с тьмой (Alone Against the Dark) (`naedine-s-tmoy-ru`) | ru | OCR | 104 | 113 | 102 | 0 (0) | 0 | 0 | 0 |
| Не забывай меня (`ne-zabyvay-menya-ru`) | ru | текст | 29 | 92 | 28 | 0 (0) | 13 | 0 | 2 |
| Necropolis (англ.) (`necropolis-en`) | en | текст | 23 | 43 | 21 | 0 (0) | 13 | 2 | 2 |
| Ничего кроме ветра (`nichego-krome-vetra-ru`) | ru | текст | 18 | 30 | 15 | 0 (0) | 3 | 2 | 2 |
| Number 7 Dream (`number-7-dream-en`) | en | текст | 27 | 100 | 26 | 0 (0) | 15 | 0 | 1 |
| Одно небольшое дельце... (`odno-nebolshoe-deltse-ru`) | ru | текст | 13 | 48 | 11 | 0 (0) | 2 | 0 | 0 |
| Ограбление по-Аркхэмски (`ograblenie-po-arkhemski-ru`) | ru | текст | 15 | 61 | 14 | 0 (0) | 1 | 0 | 2 |
| Омерзительная пятёрка (`omerzitelnaya-pyaterka-ru`) | ru | текст | 12 | 39 | 11 | 0 (0) | 3 | 0 | 1 |
| Остров лучезарной надежды (`ostrov-luchezarnoy-nadezhdy-ru`) | ru | скан | 20 | 38 | 20 | 0 (0) | 2 | 0 | 0 |
| Отель Скайлайн (`otel-skaylayn-ru`) | ru | скан | 31 | 92 | 31 | 0 (0) | 0 | 0 | 0 |
| Парк развлечений (`park-razvlecheniy-ru`) | ru | текст | 33 | 108 | 27 | 0 (0) | 14 | 0 | 7 |
| Под землёй и над землёй (`pod-zemlyoy-i-nad-zemlyoy-ru`) | ru | текст | 23 | 114 | 22 | 0 (0) | 17 | 0 | 0 |
| Подземка (`podzemka-ru`) | ru | текст | 13 | 60 | 12 | 0 (0) | 5 | 0 | 0 |
| Погоня в Поезде (`pogonya-v-poezde-ru`) | ru | скан | 22 | 80 | 20 | 0 (0) | 0 | 0 | 0 |
| Попались (`popalis-ru`) | ru | текст | 3 | 28 | 2 | 0 (0) | 2 | 0 | 2 |
| Поселок Березовый (`poselok-berezovyy-ru`) | ru | текст | 13 | 49 | 12 | 0 (0) | 3 | 0 | 0 |
| Призрак (`prizrak-ru`) | ru | текст | 18 | 87 | 17 | 0 (0) | 0 | 0 | 1 |
| Проклятие Ганеши (`proklyatie-ganeshi-ru`) | ru | текст | 36 | 57 | 35 | 0 (0) | 24 | 0 | 0 |
| Пустые страницы (`pustye-stranitsy-ru`) | ru | текст | 16 | 46 | 15 | 0 (0) | 1 | 0 | 1 |
| Рождественская вечеринка (`rozhdestvenskaya-vecherinka-ru`) | ru | текст | 21 | 81 | 20 | 0 (0) | 15 | 4 | 5 |
| Secrets of the Kremlin, 1931 (`secrets-of-the-kremlin-en`) | en | текст | 22 | 141 | 20 | 0 (0) | 4 | 0 | 1 |
| Shadows of Leningrad (`shadows-of-leningrad-en`) | en | текст | 50 | 138 | 48 | 0 (0) | 14 | 0 | 0 |
| Шанс на чудо (`shans-na-chudo-ru`) | ru | текст | 10 | 24 | 9 | 0 (0) | 6 | 0 | 0 |
| Сны о Японии (Эра Ктулху 6) (`sny-o-yaponii-ru`) | ru | текст | 49 | 137 | 47 | 0 (0) | 18 | 0 | 4 |
| Стартовый набор: Мертвецкий стомп (`starter-dead-mans-stomp-ru`) | ru | скан | 28 | 105 | 27 | 0 (0) | 0 | 0 | 0 |
| Стартовый набор: Грань тьмы (`starter-edge-of-darkness-ru`) | ru | скан | 31 | 119 | 31 | 0 (0) | 0 | 0 | 0 |
| Стартовый набор: Бумажный след (`starter-paper-chase-ru`) | ru | скан | 12 | 43 | 12 | 0 (0) | 0 | 0 | 0 |
| Стартовый набор: готовые персонажи (`startovyy-nabor-pregens-ru`) | ru | скан | 12 | 5 | 10 | 0 (0) | 0 | 0 | 0 |
| Судьба братьев Вашингтон (`sudba-bratev-vashington-ru`) | ru | текст | 10 | 40 | 7 | 0 (0) | 3 | 0 | 0 |
| Тайник Бутлегеров (`taynik-butlegerov-ru`) | ru | скан | 20 | 90 | 19 | 0 (0) | 3 | 0 | 1 |
| Тень над Провиденсом (`ten-nad-providensom-ru`) | ru | текст | 39 | 66 | 37 | 0 (0) | 10 | 5 | 5 |
| Террор (`terror-ru`) | ru | текст | 31 | 81 | 28 | 0 (0) | 16 | 6 | 9 |
| Туманы острова Сан-Кристобаль (`tumany-san-kristobal-ru`) | ru | текст | 25 | 55 | 25 | 0 (0) | 15 | 6 | 7 |
| Viral (`viral-en`) | en | текст | 125 | 174 | 120 | 0 (0) | 85 | 10 | 10 |
| Вне власти времени (`vne-vlasti-vremeni-ru`) | ru | текст | 14 | 38 | 13 | 0 (0) | 8 | 1 | 1 |
| каталог оружия 1920-х (пользовательский, не книга) (`weapons-catalog-1920s`) | ru | скан | 0 | 9 | 0 | 0 (0) | 0 | 0 | 0 |
| веб-помощник (`web-helper-coc`) | ru | скан | 0 | 16 | 0 | 0 (0) | 0 | 0 | 16 |
| За закрытыми дверьми: готовые персонажи (`za-zakrytymi-dveryami-pregens-ru`) | ru | скан | 18 | 6 | 18 | 0 (0) | 6 | 0 | 0 |
| Забывающийся (`zabyvayushchiysya-ru`) | ru | текст | 17 | 42 | 16 | 0 (0) | 6 | 0 | 0 |
| Жертвы северных ветров (`zhertvy-severnykh-vetrov-ru`) | ru | текст | 21 | 73 | 20 | 0 (0) | 6 | 0 | 0 |

## Находки по книгам

### Маски Ньярлатхотепа (англ., 7e, т. I–II) (`masks-of-nyarlathotep-en`) — 71

**Тексты** (2)

- [low] с. -2 (физ. 1) — с. 1 (физ. 4): 3 стр., 768 слов не цитирует ни одна запись; headings: CHA23153- V2; Masks of Nyarlathotep; Masks of; NYARLATHOTEP; near: Поиски древней пирамиды в Перу; Телеграмма Ларкина
- [low] с. 656 (физ. 659) — с. 666 (физ. 669): 9 стр., 1439 слов не цитирует ни одна запись; headings: INDEX; Characters and Monsters; America �����������������������������162; Bloody Tongue ������������������������ 10,

**Картинки** (67)

- [high] с. 223 (физ. 226): 1 карт. (978×483); без картинки: «Алтарь змея» (item)
- [high] с. 243 (физ. 246): 1 карт. (1288×1628); без картинки: Дневник Эдгара Вейна («История Вейнов») (item)
- [high] с. 253 (физ. 256): 1 карт. (1288×1628); без картинки: Вышибала клуба «Синяя пирамида» (character)
- [high] с. 255 (физ. 258): 1 карт. (705×480); без картинки: Бадру (character)
- [high] с. 277 (физ. 280): 1 карт. (754×480); без картинки: инспектор Грегори Манден (character), Флаконы с личинками туманного отродья (item), Удостоверение инспектора Мандена (item), Компоненты заклинаний (item), Странные растения Гавигана (item)
- [high] с. 444 (физ. 447): 1 карт. (786×480); без картинки: М’Веру (character), Подвеска М’Веру с кровью Ньярлатхотепа (item)
- [high] с. 504 (физ. 507): 1 карт. (832×960); без картинки: Пульт йитов (item)
- [high] с. 572 (физ. 575): 1 карт. (850×480); без картинки: Линь Енью (character)
- [high] с. 600 (физ. 603): 2 карт. (765×480, 383×480); без картинки: Боеголовка ракеты (радиевая бомба) (item)
- [high] с. 605 (физ. 608): 1 карт. (687×960); без картинки: Подлые прислужники мадам Линь (character), Бин (creature), Дуньдунь (creature)
- [high] с. 613 (физ. 616): 2 карт. (753×480, 1239×483); без картинки: Мутировавший глубоководный с крабьей клешнёй (creature), Шоггот, собравшийся воедино ужас (creature)
- [high] с. 647 (физ. 650): 1 карт. (709×480); без картинки: Текст Р’льеха (tome)
- [medium] с. 0 (физ. 3): 1 карт. (2592×3376); страницу не цитирует никто
- [medium] с. 2 (физ. 5): 1 карт. (1245×1621); на странице: Поиски древней пирамиды в Перу, Телеграмма Ларкина
- [medium] с. 3 (физ. 6): 1 карт. (1245×1621); на странице: Записи Тринидад Ризо о «Последней исповеди»
- [medium] с. 4 (физ. 7): 1 карт. (1245×1621); страницу не цитирует никто
- [medium] с. 64 (физ. 67): 1 карт. (474×480); без картинки: Педро де Веласко (character)
- [medium] с. 69 (физ. 72): 1 карт. (867×960); на странице: Больница (location), Отель «Эспанья» (location), После нападения: Ларкин в отеле (scene), Схватка с де Мендосой (scene), Кхарисири в Пуно (scene)
- [medium] с. 83 (физ. 86): 1 карт. (250×480); без картинки: Оживлённая мумия (creature), Сокровища кхарисири (item)
- [medium] с. 102 (физ. 105): 2 карт. (1240×804, 1177×762); на странице: Нью-Йорк (location)
- [medium] с. 145 (физ. 148): 1 карт. (1288×1628); на странице: Гарлем (location), Редакция Amsterdam News (location), Редакция New York Times (location), 14-й полицейский участок (location), Редакция New York Times (scene)
- [medium] с. 160 (физ. 163): 1 карт. (471×480); без картинки: Киимба (creature), Запертая шкатулка с вещами жертв (item)
- [medium] с. 178 (физ. 181): 3 карт. (952×669, 1240×804, 1177×762); на странице: Фонд Пэнхью (organization)
- [medium] с. 179 (физ. 182): 1 карт. (1240×804); на странице: Лондон (location), Прибытие в Англию (scene), Встреча с Эдвардом Гавиганом (scene)
- [medium] с. 224 (физ. 227): 1 карт. (1239×960); на странице: Пульп: картина в чулане (scene)
- [medium] с. 271 (физ. 274): 1 карт. (1288×1628); на странице: Станция «Ул. Ливерпуль» (location), Ворота в двухметровой стене (location), Башня Нейза (location), Нейз и Уолтон-на-Нейзе (location), Дорога в Миср-хаус (scene)
- [medium] с. 279 (физ. 282): 1 карт. (328×480); без картинки: Ритуальные дубинки Братства (item)
- [medium] с. 298 (физ. 301): 2 карт. (1240×804, 1177×762); на странице: Редакция «Каирского вестника» (location)
- [medium] с. 299 (физ. 302): 1 карт. (1240×804); на странице: Каир (location), Прибытие в Египет (scene)
- [medium] с. 316 (физ. 319): 1 карт. (441×480); без картинки: Нури из Васты (character), Убайд (character), Артефакты Тёмного фараона, проданные Карлайлу (item)
- [medium] с. 330 (физ. 333): 1 карт. (538×480); без картинки: Йанвиллем ван Хёвелен (character), Нерис (character)
- [medium] с. 369 (физ. 372): 1 карт. (951×960); на странице: Пульп: дверь в прошлое (scene), Явление Ньярлатхотепа (scene)
- [medium] с. 436 (физ. 439): 1 карт. (445×480); без картинки: Отродье Ньярлатхотепа: облик матери (creature)
- [medium] с. 475 (физ. 478): 1 карт. (277×480); без картинки: Фрэнк Слаттери (character), Джако Слаттери (character), Верн Слаттери (character), Ботинки Билла Бакли (item), Губная гармошка Билла Бакли (item)
- [medium] с. 482 (физ. 485): 1 карт. (394×480); без картинки: Дубина культа Песчаной летучей мыши (item)
- [medium] с. 491 (физ. 494): 1 карт. (369×480); без картинки: Летучий полип («Маски») (creature)
- [medium] с. 500 (физ. 503): 1 карт. (393×480); без картинки: Боги реальности (tome), Чаша из «меди сверху» (item), Покоритель разума (item), Статуя Ньярлатхотепа и статуи-хранилища (item)
- [medium] с. 509 (физ. 512): 1 карт. (394×480); без картинки: Обычный культист Песчаной летучей мыши (character), Ложная кобра Гюнтера («Маски») (creature), Смертельная змея («Маски») (creature), Сновидческие динго (creature), Динго Грогана (creature)
- [medium] с. 523 (физ. 526): 1 карт. (1240×804); на странице: Прибытие в Шанхай (scene)
- [medium] с. 539 (физ. 542): 1 карт. (394×480); без картинки: Жуль Савояр (character), сэр Обри Пэнхью (character)
- [medium] с. 552 (физ. 555): 1 карт. (274×480); без картинки: Лун Юнь (character)
- [medium] с. 555 (физ. 558): 1 карт. (284×480); без картинки: Хо Фан (character), Ящики с пометкой «О. П.» (item), Облачение и принадлежности ордена Опухшей дамы (item), Артефакты особого хранилища (item)
- [medium] с. 567 (физ. 570): 1 карт. (309×480); без картинки: Чжан Нин (character), Господин Мао (character)
- [medium] с. 568 (физ. 571): 1 карт. (584×480); без картинки: Линь Енью (character), Безумная команда «Тёмной госпожи» (creature)
- [medium] с. 570 (физ. 573): 1 карт. (296×480); без картинки: Линь Енью (character), Собрание мадам Линь (item)
- [medium] с. 587 (физ. 590): 1 карт. (562×480); без картинки: сэр Обри Пэнхью (character), Ужасные глубоководные с острова Серого дракона (creature), Стая крабов-кротов (creature), Потомки глубоководных из деревни на острове Серого дракона (creature)
- [medium] с. 588 (физ. 591): 1 карт. (418×480); без картинки: сэр Обри Пэнхью (character), Рабы под властью твши (character), Ужасные глубоководные с острова Серого дракона (creature), Мутировавший глубоководный с крабьей клешнёй (creature), Статуя Опухшей дамы (остров Серого дракона) (item)
- [medium] с. 590 (физ. 593): 1 карт. (453×480); без картинки: сэр Обри Пэнхью (character), Ужасные глубоководные с острова Серого дракона (creature), Стая крабов-кротов (creature), Шоггот, собравшийся воедино ужас (creature), Статуя Опухшей дамы (остров Серого дракона) (item)
- [medium] с. 592 (физ. 595): 1 карт. (309×480); без картинки: сэр Обри Пэнхью (character), Система наведения ракеты (item), Чертежи ракеты (item), Спусковой механизм ракеты (item), Боеголовка ракеты (радиевая бомба) (item)
- [medium] с. 651 (физ. 654): 1 карт. (285×480); без картинки: Зеркало Гала (item), Два скипетра (item)
- [medium] с. 652 (физ. 655): 1 карт. (406×480); без картинки: Египетская кобра («Маски») (creature), Амулет ночных тварей (item)
- [medium] с. 654 (физ. 657): 1 карт. (575×480); без картинки: Мухобойка Бундари (item)
- [low] с. 75 (физ. 78): 1 карт. (514×480); на странице: Пуно (location), Озеро Титикака (location), Кхарисири в Пуно (scene), Встреча с Найрой (scene)
- [low] с. 147 (физ. 150): 1 карт. (950×483); на странице: Театр «Лафайет» (location), Редакция New York Times (location), 14-й полицейский участок (location), Салун «У Тедди» (location), Встреча с Милли Адамс (scene)
- [low] с. 180 (физ. 183): 1 карт. (337×480); на странице: Гайд-парк (location), Ламбет (location), Лондон (location), Челси (location), Сити (location)
- [low] с. 245 (физ. 248): 1 карт. (513×480); на странице: Элоиза сбегает (scene)
- [low] с. 260 (физ. 263): 1 карт. (370×480); на странице: Подвал клуба (location), Британская имперская выставка (location), Плен у Шафик (scene), Важная встреча (scene)
- [low] с. 280 (физ. 283): 1 карт. (754×480); на странице: Кульминация: проникновение на обряд (scene)
- [low] с. 333 (физ. 336): 1 карт. (275×480); на странице: Храм Баст (location), Развязка «Чёрной кошки» (scene), Храм Баст (scene)
- [low] с. 361 (физ. 364): 1 карт. (441×480); на странице: Как сорвать воскрешение Нитокрис (scene)
- … ещё 7 (все — в findings.json)

**Связи** (2)

- [low] `masks-of-nyarlathotep-en/scene/campaign-message-from-an-old-friend` Послание от старого друга — сцена без места; сценарий masks-of-nyarlathotep-en/scenario/campaign-beginning
- [low] `masks-of-nyarlathotep-en/scene/conclusion-the-eclipse` Полное солнечное затмение — сцена без места; сценарий masks-of-nyarlathotep-en/scenario/grand-conclusion

### Malleus Monstrorum, т. II (`malleus-monstrorum-2-en`) — 46

**Тексты** (30)

- [high] с. 253 — с. 256: 3 стр., 526 слов не цитирует ни одна запись; headings: PRONUNCIATION; APPENDIX; OF MYTHOS NAMES; Cthulhu Mythos stories and scenarios developed; near: Зу-че-куон
- [medium] с. 26: 1 стр., 645 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; APHOOM ZHAH; Cult; near: Абхот; Афум-Жа; Таблица попаданий (Афум-Жа)
- [medium] с. 34: 1 стр., 671 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Cult; Possible Blessings; Encounters; near: Атлач-Нача
- [medium] с. 40: 1 стр., 684 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; BAOHT Z’UQQA-MOGG; Baoht Z’uqqa-Mogg enjoys consuming dead flesh, which; near: Азатот: Ксада-Хгла; Баот З'укка-Могг; Баст
- [medium] с. 56 — с. 57: 2 стр., 1283 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Finally, anyone (cultist or otherwise) receiving Cthulhu’s; Possible Blessings; Encounters; near: Великий Ктулху; Ктулху: Б'Мот
- [medium] с. 61: 1 стр., 621 слов не цитирует ни одна запись; headings: CHAPTER 2; Chorazin, Cthulhu’s voice; Magic; Powers; near: Ктулху: Левиафан; Ктулху: Хоразин
- [medium] с. 63: 1 стр., 605 слов не цитирует ни одна запись; headings: CHAPTER 2; CTHYLLA; near: Ктилла; Ктулху: Левиафан
- [medium] с. 71: 1 стр., 680 слов не цитирует ни одна запись; headings: CHAPTER 2; Aura; Cult; Possible Blessings; near: Сайтулос
- [medium] с. 79 — с. 80: 2 стр., 1220 слов не цитирует ни одна запись; headings: CHAPTER 2; Possible Blessings; Eihort; DEITIES OF THE MYTHOS; near: Айхорт; Даолот: Священный свет
- [medium] с. 90: 1 стр., 651 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Aura; Ghroth, the harbinger; Magic; near: Гла’аки; Грот
- [medium] с. 102 — с. 103: 2 стр., 1415 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; CHAPTER 2; Encounters; Aura; near: Хасталык
- [medium] с. 109: 1 стр., 717 слов не цитирует ни одна запись; headings: CHAPTER 2; near: Король в жёлтом; Хастур: Ненасытный
- [medium] с. 119 — с. 120: 2 стр., 1285 слов не цитирует ни одна запись; headings: CHAPTER 2; Ithaqua’s purpose remains somewhat unclear, although; Ithaqua; DEITIES OF THE MYTHOS; near: Иод; Итакуа; Итакуа: Ходящий со смертью
- [medium] с. 188: 1 стр., 640 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Possible Blessings; Encounters; Aura; near: Себек
- [low] с. 1 — с. 8: 6 стр., 2312 слов не цитирует ни одна запись; headings: CTHU LHU MYTHOS BESTIARY; VOLUME II; V olume Ii; Printed in Lithuania
- [low] с. 24: 1 стр., 437 слов не цитирует ни одна запись; headings: DEITIES OF; CHAPTER; THE MYTHOS; ABHOTH; near: Абхот
- [low] с. 38: 1 стр., 323 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Xada-Hgla; near: Азатот; Азатот: Ксада-Хгла
- [low] с. 59: 1 стр., 214 слов не цитирует ни одна запись; headings: CHAPTER 2; Chorazin and Leviathan; near: Ктулху: Б'Мот; Ктулху: Хоразин
- [low] с. 68: 1 стр., 524 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; CYMAEGHI; Cymaeghi; near: Саега; Саймеги
- [low] с. 85: 1 стр., 515 слов не цитирует ни одна запись; headings: CHAPTER 2; Encounters; Ghatanothoa; near: Гатанотоа; Фтаггуа
- [low] с. 87: 1 стр., 502 слов не цитирует ни одна запись; headings: CHAPTER 2; GHIZGUTH; Presumably, this entity remains somehow “chained” or; According to Hyperborean scholars, Ghizguth (sometimes; near: Гатанотоа; Гизгут
- [low] с. 132: 1 стр., 526 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; MORDIGGIAN; Mordiggian; near: Мордиггиан; Мх'итрха
- [low] с. 139: 1 стр., 582 слов не цитирует ни одна запись; headings: CHAPTER 2; Nodens; near: Нктоса и Нктолху; Ноденс
- [low] с. 148: 1 стр., 311 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; The Brotherhood also venerate another of Nyarlathotep’s; GREEN MAN, THE; BLOATED WOMAN, THE; near: Аку-Син Кагэ; Ньярлатхотеп: человеческие облики; Отец личинок
- [low] с. 168: 1 стр., 362 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Encounters; Aura; Nyogtha, the thing that should not be; near: Оссадагова; Песнопение Вак-Вирадж
- [low] с. 177: 1 стр., 584 слов не цитирует ни одна запись; headings: CHAPTER 2; Certain lore surrounding Quachil Uttaus associates the; Cult; Quachil Uttaus; near: Квачил Уттаус; Фарол
- [low] с. 194: 1 стр., 555 слов не цитирует ни одна запись; headings: DEITIES OF THE MYTHOS; Shub-Niggurath has been unsuccessfully summoned, or in; The Lady of the Woods; Cult; near: Шуб-Ниггурат; Шуб-Ниггурат: Лесная госпожа
- [low] с. 221: 1 стр., 524 слов не цитирует ни одна запись; headings: CHAPTER 2; Cult; Possible Blessings; Y’golonac; near: И’голонак; Йегг-Ха
- [low] с. 231: 1 стр., 542 слов не цитирует ни одна запись; headings: CHAPTER 2; Cult; Explotaciones de Amaranto (Amaranthine Holdings), based; Possible Blessings; near: Дитя Йига; Йиг; Йидра
- [low] с. 263 — с. 266: 3 стр., 698 слов не цитирует ни одна запись; headings: CONTRIBUTOR BIOGRAPHIES; MIKE MASON; Around the millennium, Mike published The Whisperer,; Robert Bloch, Ramsey Campbell, Thomas Ligotti, TED

**Контекст** (16)

- [low] `coc:creature:aihais` Айхаи — в книге только упоминание, без характеристик.
- [low] `coc:creature:aku-shin-kage` Аку-Син Кагэ — в книге только упоминание: профиля, описания и характеристик нет.
- [low] `coc:creature:black-bull` Чёрный бык / Чёрный лев — в книге только упоминание: профиля, описания и характеристик нет.
- [low] `coc:creature:changelings` Подменыши (дети Пана от людей) — В книге только упоминание, без характеристик.
- [low] `coc:creature:chosen-one-of-chaugnar-faugn` Избранник Шагнера Фана — Блока характеристик в книге нет: в способности «Chosen of Chaugnar Faugn» даны только прибавки к человеческим характеристикам, число заклинаний и потеря Рассудка 0/1d6.
- [low] `coc:creature:crawling-mist` Ползучий туман — В книге только упоминание, без характеристик.
- [low] `coc:creature:crystallized-human` Окаменевший (кристаллизованный) человек — в книге только упоминание, без характеристик. Броня 8 (сила Transform Flesh) и 10 (дар Crystal Form) в книге различаются.
- [low] `coc:creature:cthulhu-leviathan` Ктулху: Левиафан — Собственных характеристик в книге нет: напечатанный блок скопирован из профиля Ктугхи (см. опечатки книги).
- [low] `coc:creature:dark-demon` Тёмный демон — В книге только упоминание, без характеристик.
- [low] `coc:creature:puppet-of-bugg-shash` Марионетка Бугг-Шаша — Блока характеристик в книге нет: даны только изменения к характеристикам человека (см. «Создание марионетки»).
- [low] `coc:creature:shugoran` Сюгоран — в книге только упоминание: профиля, описания и характеристик нет.
- [low] `coc:creature:vaeyen` Ваэйены — в книге только упоминание, без характеристик.
- [low] `coc:creature:worm-folk` Люди-черви Г'харна — В книге только упоминание, без характеристик.
- [low] `coc:creature:yidhra-monstrous-form` Йидра: чудовищная форма — атаки, броню и потерю рассудка в этом облике определяет Хранитель (Malleus т. II, с. 228–229)
- [low] `coc:creature:ythogtha` Итогта — Строка «Spells:» в книге пуста — заклинания не перечислены.
- [low] `coc:creature:zarrians` Заррияне — В книге только упоминание, без характеристик.

### Fear's Sharp Little Needles (`fears-sharp-little-needles-en`) — 42

**Тексты** (2)

- [low] с. 2 (физ. 3): 1 стр., 164 слов не цитирует ни одна запись; headings: Dedications; FEAR’S SHARP LITTLE NEEDLES; Copyright ©2018 by Stygian Fox; Printed on Earth
- [low] с. 6 (физ. 7): 1 стр., 555 слов не цитирует ни одна запись; headings: Introduct io n; near: Tormiss CRD, модель Z-17; И тут явился Жнец; Исследовательский центр Уинока-Пойнт

**Картинки** (10)

- [high] с. 52 (физ. 53): 1 карт. (486×1138); без картинки: Элис Миллер (character), Карл Миллер (character), Казимир Мартен (character), Клэр (character), Клод Дюмонт (character)
- [high] с. 80 (физ. 81): 1 карт. (1013×1214); без картинки: Доктор Мира Сагар (character)
- [high] с. 81 (физ. 82): 1 карт. (1080×616); без картинки: Бернард Дэвис (character), Эдмунд Смит (character), Джозефина Дэвис (character), Ребекка Джонс (character), Тереза Смит (character)
- [high] с. 155 (физ. 156): 2 карт. (491×264, 1008×662); без картинки: Эпифани Фарнсуорт (character), Папка «Проект “Газлайт”» (item), Легенды и фольклор Аппалачей (запрещённый первый черновик) (tome)
- [high] с. 159 (физ. 160): 1 карт. (1018×1371); без картинки: Джеймс Синклер (character), Роуз Уайатт Синклер (character), Вильма Родригес (character)
- [high] с. 162 (физ. 163): 1 карт. (736×1078); без картинки: Доктор Эмили Чанг (character), Джеймс Чанг (character), Доктор Роберт Чанг (character), Лейтенант Том Баркли (character)
- [high] с. 163 (физ. 164): 1 карт. (941×491); без картинки: Бо Джонсон (character), Сью Джонсон (character), Лейтенант Том Баркли (character), Раздатка «Флеботомия» 5: легенды о жизни без головы (handout), Согласие на удочерение Лондон (item)
- [high] с. 164 (физ. 165): 1 карт. (1011×409); без картинки: Джулз Томас (character), Мария Фарнсуорт (character), Роберт Палмер (character), Согласие на удочерение Лондон (item)
- [high] с. 168 (физ. 169): 1 карт. (1000×1154); без картинки: Фанг (character), Вильма Родригес (character)
- [medium] с. 121 (физ. 122): 1 карт. (589×444); без картинки: Анита Симмонс (character), Превращённые люди (character), Дерек Кляйн (character), Эльвира Сондерс (character), Софи Маккендрик (character)

**Связи** (17)

- [low] `fears-sharp-little-needles-en/scene/dissociation-examining-vessels` Осмотр сосудов (сейчас и позже) — сцена без места; сценарий fears-sharp-little-needles-en/scenario/dissociation
- [low] `fears-sharp-little-needles-en/scene/dissociation-survivors` Выжившие — сцена без места; сценарий fears-sharp-little-needles-en/scenario/dissociation
- [low] `fears-sharp-little-needles-en/scene/hatteras-video-of-the-attack` Видео нападения — сцена без места; сценарий fears-sharp-little-needles-en/scenario/hatteras-reef
- [low] `fears-sharp-little-needles-en/scene/reaper-missing-couple` Пропавшая пара — сцена без места; сценарий fears-sharp-little-needles-en/scenario/reaper
- [low] `fears-sharp-little-needles-en/scene/reaper-resolutions` Развязка — сцена без места; сценарий fears-sharp-little-needles-en/scenario/reaper
- [low] `fears-sharp-little-needles-en/scene/separation-missing-persons-research` Поиск похожих пропавших — сцена без места; сценарий fears-sharp-little-needles-en/scenario/separation-anxiety
- [low] `fears-sharp-little-needles-en/scene/separation-mythos-research` Поиск в источниках о Мифах — сцена без места; сценарий fears-sharp-little-needles-en/scenario/separation-anxiety
- [low] `fears-sharp-little-needles-en/scene/sins-confessions` Признания — сцена без места; сценарий fears-sharp-little-needles-en/scenario/sins-of-my-youth
- [low] `fears-sharp-little-needles-en/scene/sores-calling-the-hospital` Звонок в больницу — сцена без места; сценарий fears-sharp-little-needles-en/scenario/sores
- [low] `fears-sharp-little-needles-en/scene/sores-their-turn` Теперь их очередь — сцена без места; сценарий fears-sharp-little-needles-en/scenario/sores
- [low] `fears-sharp-little-needles-en/scene/tormiss-crossing-the-cultists` Столкновение с культистами — сцена без места; сценарий fears-sharp-little-needles-en/scenario/tormiss
- [low] `fears-sharp-little-needles-en/scene/tormiss-doctor-patient` Нарушение врачебной тайны — сцена без места; сценарий fears-sharp-little-needles-en/scenario/tormiss
- [low] `fears-sharp-little-needles-en/scene/tormiss-official-channels` Официальные каналы — сцена без места; сценарий fears-sharp-little-needles-en/scenario/tormiss
- [low] `fears-sharp-little-needles-en/scene/undertow-dog-returns` Собака возвращается — сцена без места; сценарий fears-sharp-little-needles-en/scenario/undertow
- [low] `fears-sharp-little-needles-en/scene/undertow-finding-hayes` Поиски Хейза — сцена без места; сценарий fears-sharp-little-needles-en/scenario/undertow
- [low] `fears-sharp-little-needles-en/scene/undertow-novel` Роман «Подводное течение» — сцена без места; сценарий fears-sharp-little-needles-en/scenario/undertow
- [low] `fears-sharp-little-needles-en/scene/undertow-pale-man` Бледный человек — сцена без места; сценарий fears-sharp-little-needles-en/scenario/undertow

**Контекст** (13)

- [low] `fears-sharp-little-needles-en/character/special-menu-kayla-cooper` Кейла Купер — Статблока нет: книга даёт только ПЗ 12 и Уклонение 25% (с. 139). Русский текст — по рабочему переводу владельца (fears-sharp-little-needles/document.html, «Особое меню»), сверен с английским оригинало
- [low] `fears-sharp-little-needles-en/creature/waiting-regora` Регора — Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа — по английской странице; отдельного перевода владельца для
- [low] `fears-sharp-little-needles-en/location/unland-boat-pond` Пруд для радиоуправляемых лодок — Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа — по английской странице; отдельного перевода владельца для
- [low] `fears-sharp-little-needles-en/location/unland-boating-lake` Озеро для катания на лодках — Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа — по английской странице; отдельного перевода владельца для
- [low] `fears-sharp-little-needles-en/location/unland-office` Контора — Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа — по английской странице; отдельного перевода владельца для
- [low] `fears-sharp-little-needles-en/location/unland-ruined-bridge` Разрушенный мост — Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа — по английской странице; отдельного перевода владельца для
- [low] `fears-sharp-little-needles-en/location/unland-scenic-lake` Живописное озеро — Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа — по английской странице; отдельного перевода владельца для
- [low] `fears-sharp-little-needles-en/tome/fuel-jaleel-scrolls` Древние свитки Джалила — Книга не даёт ни потери Рассудка, ни прибавки к Мифам, ни времени изучения, ни языка — только что свитки ближневосточные и что по ним выучено заклинание; где они хранятся, не сказано. Русский текст — 
- [low] `fears-sharp-little-needles-en/tome/hit-and-run-family-bible` Семейная Библия Гаретов — Заклинание «Retribution of the Wicked» — запись coc:spell:retribution-of-the-wicked («Возмездие нечестивых»). Вид книги «оккультная» — вывод (Библия с вписанным ритуалом, Р-41). Русский текст — по раб
- [low] `fears-sharp-little-needles-en/tome/hit-and-run-family-spell-book` Семейная книга заклинаний Гаретов (сожжена) — «Gate spell» сопоставлено с «Создание врат» (вывод, Р-41). Русский текст — по рабочему переводу владельца (2_Обработка/fears-sharp-little-needles/document.html), сверен с английским оригиналом; числа 
- [low] `coc:spell:ascension-to-immortality` Вознесение к бессмертию — Новое заклинание сценария «Последнее желание Уолтера» (Fear's Sharp Little Needles). Книга называет его вариантом «Вызова Мордиггиана»; такой записи в справочнике нет, поэтому variant_of — семейство «
- [low] `coc:spell:construct-gear-men` Создание Шестерёнщиков — Только название в списке заклинаний «Адских машин» (Fear's Sharp Little Needles, с. 44); описания нет. Связь с семейством «Заклинания связи» — по скобкам книги «(Contact)»; тип и механика выведены из 
- [low] `coc:spell:join-the-worlds-together` Объединение миров — Только название с пояснением в списке заклинаний книги (Fear's Sharp Little Needles, с. 155); стоимости, времени и описания нет. Тип и механика — вывод из пояснения (Р-41). Название — по рабочему пере

### Книга хранителя (`keeper-rulebook-ru`) — 29

**Тексты** (8)

- [high] с. 5 — с. 9: 5 стр., 1216 слов не цитирует ни одна запись; headings: Имя сыщика; Крас 1юречие (навык); Обычный уровень сложности; ЗОВ КТУЛХУ; near: «Мелкие безделицы»
- [high] с. 20 (физ. 19) — с. 24: 6 стр., 3150 слов не цитирует ни одна запись; headings: ЗОВ КТУЛХУ; Говард Филлипс; Лавкрафт; Его жизнь и создание; near: Выносливость; Интеллект; Комплекция
- [high] с. 405 (физ. 381) — с. 408 (физ. 384): 4 стр., 1607 слов не цитирует ни одна запись; headings: Бонусные; Кратко; Проверки навыков; Из характеристики врага по очереди вычитают харак­; near: Автомат «M16A2»; Автомат «M4»; Автомат «АК-47 / АКМ»
- [high] с. 410 (физ. 386) — с. 413 (физ. 389): 4 стр., 1146 слов не цитирует ни одна запись; headings: Определите порядок атак; Внезапная атака; Разыграйте в порядкеЛВК; В бою; near: Автомобиль; Другие виды урона; Задержка дыхания и утопление
- [high] с. 415 (физ. 391) — с. 417 (физ. 393): 3 стр., 1125 слов не цитирует ни одна запись; headings: Кратко; И грокам нужно отслеживать, сколько пунктов рассудка; Провал проверки Рассудка -; Потеря 5 или более пунктов рассудка -; near: Автомобиль
- [low] с. 2: 1 стр., 151 слов не цитирует ни одна запись; near: Коттедж Лейтера
- [low] с. 54 (физ. 51): 1 стр., 186 слов не цитирует ни одна запись; headings: ЗОВ КТУЛХУ; Инженерия (01%) -; Иностранный язык (01%) ~; Искусство/ремесло (05%) ~; near: Антропология; Артиллерия; Археология
- [low] с. 321 (физ. 300): 1 стр., 441 слов не цитирует ни одна запись; headings: Ктугха напоминает постоя нно изменяю ­; Н иогта; Омерзительная вонь начала; Обитает он на звезде Фомальгаут; near: Король в жёлтом; Ктугха; Ниогта

**Контекст** (21)

- [low] `coc:tome:book-of-iod-ancient-tongue` Книга Иода (древнее наречие) — tome без описания
- [low] `coc:tome:book-of-iod-english` Книга Иода (английский) — tome без описания
- [low] `coc:tome:book-of-skelos` Книга Скелоса — tome без описания
- [low] `coc:tome:cabala-of-saboth` Каббала Саваофа — tome без описания
- [low] `coc:tome:chronike-von-nath` Chronike von Nath — tome без описания
- [low] `coc:tome:ilarnek-papyri` Иларнекские папирусы — tome без описания
- [low] `coc:tome:in-pressured-places` Под высоким давлением — tome без описания
- [low] `coc:tome:johansen-narrative` Рассказ Йохансена — tome без описания
- [low] `coc:tome:legends-of-liqualia` Легенды Ликвалии — tome без описания
- [low] `coc:tome:liber-damnatus-damnationum` Liber Damnatus Damnationum — tome без описания
- [low] `coc:tome:life-of-eibon` Жизнь Эйбона — tome без описания
- [low] `coc:tome:occult-foundation` Основы оккультизма — tome без описания
- [low] `coc:tome:of-evil-sorceries-done-in-new-england` О злодеяниях чародеев в Новой Англии — tome без описания
- [low] `coc:tome:parchments-of-pnom` Пергаменты Пнома — tome без описания
- [low] `coc:tome:prehistoric-pacific-in-the-light-of-the-ponape-scripture` Доисторическая Океания в свете Понапского писания — tome без описания
- [low] `coc:tome:revelations-of-hali` Откровения Хали — tome без описания
- [low] `coc:tome:saducismus-triumphatus` Saducismus Triumphatus — tome без описания
- [low] `coc:tome:tunneler-below` Роющие в глубине — tome без описания
- [low] `coc:tome:uralteschrecken` Uralteschrecken — tome без описания
- [low] `coc:tome:we-pass-from-view` Мы уходим из виду — tome без описания
- [low] `coc:tome:yuggya-chants` Песнопения Юггья — tome без описания

### Побег из Иннсмута (`pobeg-iz-innsmuta-ru`) — 25

**Тексты** (1)

- [low] с. 19: 1 стр., 190 слов не цитирует ни одна запись; headings: ПУТЕВОДИТЕЛЬ ПО ИННСМУТУ; И ОКРЕСТНОСТЯМ; УКАЗАТЕЛЬ; ТРУЩОБЫ СЕВЕРНОГО ПОБЕРЕЖЬЯ; near: «Сад» (бар и гриль); Анна Тилтон; Джордж Коул

**Картинки** (16)

- [high] с. 65: 2 карт. (1696×1112, 2285×1582); без картинки: Ралса Марш (character), Рут Гилман (character)
- [high] с. 67: 2 карт. (876×2168, 1087×3163); без картинки: Элизабет Кроуфорд (character), Ричард Мэннинг (character), Дневник Джереми Кроуфорда (handout), Дневник Элизабет Кроуфорд (handout)
- [high] с. 84: 1 карт. (1188×2240); без картинки: Рамона (character), Томас Уэйт (character), Тварь на чердаке (character), Дневник Томаса Уэйта (handout)
- [high] с. 88: 1 карт. (1193×2230); без картинки: Барнабас Марш (character), Джо Сарджент (character), Эскорт гибридов (character)
- [high] с. 120: 1 карт. (2417×1510); без картинки: Барбара Марш (character), Бернард Марш (character)
- [high] с. 136: 1 карт. (1116×3144); без картинки: Отпрыск шоггота (creature)
- [high] с. 137: 1 карт. (1104×3149); без картинки: Чарльз Анзак (character), Норман Волд (character), Витзнеки (character)
- [high] с. 139: 1 карт. (2382×2088); без картинки: Чарльз Анзак (character)
- [high] с. 153: 1 карт. (2161×1070); без картинки: Запечатанные приказы подлодки S-19 (handout)
- [high] с. 165: 1 карт. (2161×2982); без картинки: Джейкоб Марш (character)
- [medium] с. 66: 2 карт. (1696×1144, 2396×1626); на странице: Контора Ралсы Марша (scene), Осмотр дома Кроуфордов (scene)
- [medium] с. 112: 1 карт. (2304×3163); на странице: Храм Ордена Дагона: этажи и подвал (location), Гардеробная и врата в Й’ха-нтлеи (scene), Маленькие комнаты: перевод «Книги Дагона» (scene), Парадный вход и главный зал (scene)
- [medium] с. 123: 1 карт. (2198×3162); на странице: Поместье Маршей: первый этаж (location), Поместье Маршей: подвал (location), Поместье Маршей: третий этаж и купол (location), Поместье Маршей: второй этаж (location), Осмотр особняка Маршей (scene)
- [medium] с. 140: 2 карт. (1364×868, 1917×1215); на странице: Чёрная лагуна (location), Яма для разведения шогготов (location), Типичный квартал северных трущоб (location), Чёрная лагуна (scene), Исход (scene)
- [medium] с. 144: 1 карт. (1193×2250); на странице: Цель 4: первый контакт — обнаружение (scene), Погружение! Погружение! (scene)
- [medium] с. 186: 1 карт. (3119×2315); страницу не цитирует никто

**Связи** (4)

- [low] `pobeg-iz-innsmuta-ru/scene/problema-rozhdeniya` Проблема рождения — сцена без места; сценарий pobeg-iz-innsmuta-ru/scenario/nasledstvo-kroufordov
- [low] `pobeg-iz-innsmuta-ru/scene/reyd-kontakt` Контакт — сцена без места; сценарий pobeg-iz-innsmuta-ru/scenario/reyd-na-innsmut
- [low] `pobeg-iz-innsmuta-ru/scene/reyd-proverka-biografiy` Проект «Завет»: проверка биографий — сцена без места; сценарий pobeg-iz-innsmuta-ru/scenario/reyd-na-innsmut
- [low] `pobeg-iz-innsmuta-ru/scene/vstrevozhennyy-artur-anderson` Встревоженный Артур Андерсон — сцена без места; сценарий pobeg-iz-innsmuta-ru/scenario/pobeg-iz-innsmuta

**Контекст** (4)

- [low] `pobeg-iz-innsmuta-ru/creature/plotoyadnye-rakoobraznye` Плотоядные ракообразные — Блока характеристик в книге нет: числа (СИЛ хватки 45, 1 ПЗ, броня 2, урон 1 за раунд, потери Рассудка) взяты из текста; шанс атаки не указан.
- [low] `coc:spell:command-porpoise` Повелевать морской свиньёй — Только название из списков заклинаний «Побега из Иннсмута»; описания в книге нет. Русское название — наш перевод; тип и механика выведены из названия.
- [low] `coc:spell:command-shark` Повелевать акулой — Только название из списков заклинаний «Побега из Иннсмута»; описания в книге нет. Русское название — наш перевод; тип и механика выведены из названия.
- [low] `coc:tome:abyss-lore` Знание Бездны — Книга из «Побега из Иннсмута»: язык, автор, время изучения и уровень Мифов не указаны; кроме двух заклинаний — ещё 1–4 по выбору Хранителя. Английское название не известно (русское издание).

### Pulp Cthulhu (`pulp-cthulhu-en`) — 20

**Тексты** (4)

- [high] с. 9 (физ. 10) — с. 13 (физ. 14): 5 стр., 2825 слов не цитирует ни одна запись; headings: THE; CHAPTER; PULPS; ENTERTAINMENT FOR; near: Правила пульпа в обычном «Зове Ктулху»; Пульп-о-метр: сколько пульпа?
- [low] с. 0 (физ. 1) — с. 5 (физ. 6): 4 стр., 1023 слов не цитирует ни одна запись; headings: PULP CTHULHU; H U L H; LP C; PU LP CT
- [low] с. 263 (физ. 264) — с. 269 (физ. 270): 6 стр., 898 слов не цитирует ни одна запись; headings: REFERENCES; Popular Culture; INDEX; CHAPTER; near: Револьвер .44; Списки оружия (1930-е)
- [low] с. 273 (физ. 274): 1 стр., 300 слов не цитирует ни одна запись; headings: PULP CTHULHU; H U L H; LP C; PU LP CT

**Картинки** (14)

- [high] с. 182 (физ. 183): 1 карт. (591×1020); без картинки: Раздаточный материал 9: из комментированного издания Liber Ivonis (handout)
- [high] с. 186 (физ. 187): 1 карт. (630×1591); без картинки: Лоуренс Уитлок (character), Мэрион Олден (character), «Тощий» Мэттикс и Эдвин «Дёрганый» Лонерган (character), Минни Уитлок (character), Теодор Каллер (character)
- [high] с. 187 (физ. 188): 3 карт. (956×1452, 1256×2142, 628×1071); без картинки: Мэрион Олден (character), Верн Бейли (character), Гильза .38 под столом Бейли (item)
- [high] с. 190 (физ. 191): 3 карт. (960×868, 1262×1275, 631×638); без картинки: Эллиот Гаскелл (character), Джимми «Ублюдок» Банделло (character), Лестер Конклин (character), Ричардс (character), Сильвия Фейн (character)
- [high] с. 192 (физ. 193): 4 карт. (1492×1304, 746×652, 1492×937, 746×469); без картинки: Эллиот Гаскелл (character), Эфраим Фрош (character), Хаймс (character), Гостевая книга Ложи (item)
- [high] с. 193 (физ. 194): 4 карт. (1489×1304, 745×652, 1489×937, 745×469); без картинки: Арманд Де Сото (character), Харрис Долл (character), Хаймс (character), Хьюго Уиттеринг (character), Ричардс (character)
- [medium] с. 140 (физ. 141): 2 карт. (1352×1296, 950×928); на странице: «Урсус Фаундриз» (organization), Встреча с Финчем (scene)
- [medium] с. 144 (физ. 145): 2 карт. (1352×685, 950×473); на странице: До демонстрации: гости аукциона (scene)
- [medium] с. 179 (физ. 180): 1 карт. (964×1347); на странице: Раздаточный материал 5: значения финикийских знаков
- [medium] с. 180 (физ. 181): 1 карт. (742×1113); на странице: Изыскания о ящике (scene)
- [medium] с. 249 (физ. 250): 2 карт. (1594×937, 797×469); на странице: Раздаточный материал 13: старые дневники Гаскелла (1923)
- [medium] с. 250 (физ. 251): 1 карт. (2550×1688); на странице: План Ложи Искателей (map)
- [medium] с. 253 (физ. 254): 2 карт. (973×687, 1275×1997); на странице: «Медленная лодка» 1: предсмертная записка Чеда
- [low] с. 8 (физ. 9): 1 карт. (650×523); на странице: Пульп-о-метр: сколько пульпа?, Правила пульпа в обычном «Зове Ктулху»

**Связи** (1)

- [low] `pulp-cthulhu-en/scene/disintegrator-izyskaniya` Изыскания перед аукционом — сцена без места; сценарий pulp-cthulhu-en/scenario/the-disintegrator

**Контекст** (1)

- [low] `pulp-cthulhu-en/organization/eight-fortunes-mutual-aid-society` Общество взаимопомощи «Восемь удач» — Упоминается только в этом сценарии; подробностей (устройство, члены, база) книга не даёт; Шанхай — текстом, записи города нет. Эпоха сценария — 1931 год.

### Arkham (Chaosium, 2023) (`arkham-en`) — 19

**Тексты** (4)

- [low] с. 2 (физ. 3) — с. 4 (физ. 5): 2 стр., 1033 слов не цитирует ни одна запись; headings: CREDITS; Authors; Mike Mason, Keith Herber, Bret Kramer; Authors (1990 & 2003 editions)
- [low] с. 251 (физ. 252): 1 стр., 456 слов не цитирует ни одна запись; headings: Game Aids; Celebrated; Weather Generator; Distinguished; near: Лавкрафтовская хронология; Расстояния в окрестностях Мискатоника
- [low] с. 258 (физ. 259) — с. 265 (физ. 266): 8 стр., 2826 слов не цитирует ни одна запись; headings: Biographies; Mike Mason; INDEX; Arkham Advertiser����40, 70, 77, 87, 90, 175; near: Библиография и ресурсы (Аркхэм)
- [low] с. 273 (физ. 274): 1 стр., 221 слов не цитирует ни одна запись; headings: CHA23182-H; For more information about Chaosium; Printed in Poland

**Контекст** (15)

- [low] `arkham-en/character/campus-billings` Биллингс — Имя и возраст в книге не названы; в списке работников отделения его нет. Путеводитель Hort (с. 73): у Hort — доктор Моррис Биллингс, 28 лет, ведущий астроном университета: каждый семестр по два курса 
- [low] `arkham-en/handout/advertiser-1922-page-1` «Аркхэм Адвертайзер», 13 сентября 1922 года, с. 1 — Текстового слоя у вкладки нет — текст набран по изображению страницы (200 dpi). Аркхэмские статьи, объявления и реклама — целиком; реальные новости 1922 года (телеграфные сообщения) — только заголовка
- [low] `arkham-en/handout/advertiser-1922-page-2` «Аркхэм Адвертайзер», 13 сентября 1922 года, с. 2 — Текстового слоя у вкладки нет — текст набран по изображению страницы (200 dpi). Аркхэмские статьи, объявления и реклама — целиком; реальные новости 1922 года (телеграфные сообщения) — только заголовка
- [low] `arkham-en/handout/advertiser-1922-page-3` «Аркхэм Адвертайзер», 13 сентября 1922 года, с. 3 — Текстового слоя у вкладки нет — текст набран по изображению страницы (200 dpi). Аркхэмские статьи, объявления и реклама — целиком; реальные новости 1922 года (телеграфные сообщения) — только заголовка
- [low] `arkham-en/handout/advertiser-1922-page-4` «Аркхэм Адвертайзер», 13 сентября 1922 года, с. 4 — Текстового слоя у вкладки нет — текст набран по изображению страницы (200 dpi). Аркхэмские статьи, объявления и реклама — целиком; реальные новости 1922 года (телеграфные сообщения) — только заголовка
- [low] `arkham-en/tome/southside-alchemical-writings-of-edward-kelly` Алхимические сочинения Эдварда Келли — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `arkham-en/tome/southside-alchemists-through-the-ages` Алхимики сквозь века — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `arkham-en/tome/southside-genuine-thaumaturgy` Подлинная тауматургия — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `arkham-en/tome/southside-history-of-magic` История магии — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `arkham-en/tome/southside-sacred-magic-of-abra-melin` Книга священной магии Абрамелина-мага — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `arkham-en/tome/southside-secret-doctrine` Тайная доктрина — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `arkham-en/tome/southside-the-magus` Маг — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 
- [low] `coc:location:arkham-os120-elm-mountain` Элм-Маунтин — Место путеводителя «Аркхэм» (Chaosium, 2023), глава «Окрестности: за городской чертой» (OS100–OS199); русский текст — наш перевод (Р-234). Номер 120 есть только на карте окрестностей и в её ключе; ста
- [low] `coc:location:arkham-os121-bowen-wood` Лес Боуэна — Место путеводителя «Аркхэм» (Chaosium, 2023), глава «Окрестности: за городской чертой» (OS100–OS199); русский текст — наш перевод (Р-234). Номер 121 есть только на карте окрестностей и в её ключе; ста
- [low] `coc:tome:lesser-key-of-solomon` Малый ключ Соломона — Оккультная книга из списка библиотеки общества «Око Амары» (910); книга даёт только название, автора, язык, год и прибавку к Оккультизму — потери Рассудка и времени изучения нет (incomplete). Русский 

### Грибы с Юггота (`griby-s-yuggota-ru`) — 19

**Связи** (1)

- [low] `griby-s-yuggota-ru/scene/moon-vision-and-research` Видение о землетрясениях в Перу — сцена без места; сценарий griby-s-yuggota-ru/scenario/mountains-of-the-moon

**Контекст** (18)

- [low] `griby-s-yuggota-ru/character/beast-black-robed-arabs` Арабы в чёрных балахонах — Статблока в книге нет. Имена придуманы (Р-151), в книге — «шестеро арабов в чёрных балахонах».
- [low] `griby-s-yuggota-ru/character/goyo` Гойо — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет. «Составление карт» и «Бесшумное передвижение» — навыки старой редакции, 
- [low] `griby-s-yuggota-ru/character/jonathan-harris` Джонатан Харрис — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет. Имя в английском оригинале — Johnathan Harris.
- [low] `griby-s-yuggota-ru/character/lawrence-richards` Лоуренс Ричардс — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет. «Лечение от ядов» и «Поставить диагноз» — навыки старой редакции, ссылок
- [low] `griby-s-yuggota-ru/character/melvin-peale` Мелвин Пил — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет.
- [low] `griby-s-yuggota-ru/character/moon-mine-guards` Охранники шахты НМ — Групповой профиль (Р-74), имена придуманы (Р-151). Навык «Маскировка» — в оригинале Camouflage (не «Маскировка» Disguise 7-й редакции), ссылка не поставлена; «Бесшумное передвижение» — навык старой ре
- [low] `griby-s-yuggota-ru/character/moon-rebels` Повстанцы Гойо — Групповой профиль (Р-74), имена придуманы (Р-151). В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет.
- [low] `griby-s-yuggota-ru/character/ngansa` Нганса — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет. Броня — словесное описание пасты, числового значения нет. «Бесшумное пер
- [low] `griby-s-yuggota-ru/character/ron-paku` Рон-Паку — Статблока в книге нет.
- [low] `griby-s-yuggota-ru/character/sancho` Санчо — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет.
- [low] `griby-s-yuggota-ru/character/victor-montain-wife` Мария Уаман — Имя придумано (Р-150), в книге — «Жена Виктора». В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет.
- [low] `griby-s-yuggota-ru/character/victor-montain` Виктор Монтэйн — В книге у статблока только характеристики, Рассудок, ПЗ и навыки (иногда заклинания): ПМ, БкУ, Комплекции, Скорости и атак нет. Возраст: в сцене — «мужчина 55 лет», в описании — «в свои пятьдесят с по
- [low] `griby-s-yuggota-ru/creature/bay-robot` Робот доктора Дитера — Машина с блоком характеристик — по образцу «Робота-убийцы» Pulp Cthulhu (вид существа, подкатегория «робот»). У робота нет ВЫН, НАР, ИНТ, МОЩ, ОБР; ЛВК — половина ЛВК оператора. «С внутренним уроном» 
- [low] `griby-s-yuggota-ru/creature/bay-thing-from-between-planes` Нечто из межмирья — Уникальное существо сценария (Р-74). В книге нет МОЩ, ПМ, БкУ и Комплекции.
- [low] `griby-s-yuggota-ru/creature/celaeno-sleeper-in-the-lake` Спящий в Озере — Статблока в книге нет.
- [low] `coc:spell:create-yithian-communicator` Создание коммуникатора — Новое заклинание «Грибов с Юггота»: в книге только название и условие. Английское название — по оригиналу «The Fungi from Yuggoth» (Chaosium, 1984; указатель заклинаний, с. 74); оригинал не записан в 
- [low] `coc:spell:dismiss-dhole` Отпустить Дхоула — Новое заклинание «Грибов с Юггота»: в книге только название, цены, времени и механики нет. Английское название — по оригиналу «The Fungi from Yuggoth» (Chaosium, 1984; указатель заклинаний, с. 74); ор
- [low] `coc:spell:enchant-incense` Зачаровать ладан — Новое заклинание «Грибов с Юггота»: в книге только название и назначение. Тип «Зачарование», семейство «Зачаровать предмет» и механика «ритуал» — вывод из текста (Р-41). Английское название — по ориги

### Malleus Monstrorum, т. I (`malleus-monstrorum-1-en`) — 17

**Тексты** (9)

- [medium] с. 204 — с. 206: 2 стр., 279 слов не цитирует ни одна запись; headings: PRONUNCIATION GUIDE; OF MYTHOS NAMES; Entity; Abhoth
- [low] с. 1 — с. 8: 6 стр., 2516 слов не цитирует ни одна запись; headings: CTHU LHU MYTHOS BESTIARY; VOLUME I; V olume I; Printed in Lithuania
- [low] с. 32: 1 стр., 276 слов не цитирует ни одна запись; headings: CHAPTER; MONSTERS OF THE; CTHULHU MYTHOS; ABHOTH, SPAWN OF; near: Порождение Абота; Приверженец Неизречённой клятвы; Чутьё на добычу
- [low] с. 46: 1 стр., 594 слов не цитирует ни одна запись; headings: MONSTERS OF THE CTHULHU MYTHOS; Combat; Drain opposed roll; Dodge; near: Ползучая тварь; Страж Кристаллизаторов снов; Цвет из иных миров
- [low] с. 55: 1 стр., 347 слов не цитирует ни одна запись; headings: CHAPTER 2; DEEP ONE, HYBRID; Deep One Hybrid and Deep One; near: Возлюбленный Ктулху; Гибрид с акулой; Гибрид с дельфином
- [low] с. 163: 1 стр., 480 слов не цитирует ни одна запись; headings: CHAPTER 2; Fighting; Lightning gun 30% (15/6), damage 1D10; Dodge; near: Великая Раса с планеты Йит (форма конусовидного тела); Молниемёт «модель A»
- [low] с. 172: 1 стр., 522 слов не цитирует ни одна запись; headings: MONSTERS; CHAPTER; FROM FOLKLORE; CONSIDERATIONS; near: Блуждающий огонь; Спектральный чёрный пёс
- [low] с. 210 — с. 212: 2 стр., 259 слов не цитирует ни одна запись; headings: INDEX
- [low] с. 215 — с. 218: 3 стр., 698 слов не цитирует ни одна запись; headings: CONTRIBUTOR BIOGRAPHIES; MIKE MASON; Around the millennium, Mike published The Whisperer,; Robert Bloch, Ramsey Campbell, Thomas Ligotti, TED

**Контекст** (8)

- [low] `coc:creature:chthonian-hatchling` Хтониец, детёныш (до первой стадии) — Блока характеристик в книге нет.
- [low] `coc:creature:ghadamon` Гхадамон — В книге только упоминание, без характеристик.
- [low] `coc:creature:piranha-school` Пираньи (стая) — блока характеристик в книге нет: статья даёт только правила стаи (численность, урон, спасение); потеря рассудка не указана.
- [low] `coc:creature:scorpion` Скорпион — блока характеристик в книге нет: статья — правило ужаления и таблица видов (место обитания, действие, урон); урон в способностях — как напечатано. Потеря рассудка не указана.
- [low] `coc:creature:the-five-watchers` Пять Стражей — в книге только упоминание, без характеристик.
- [low] `coc:creature:ubb-lor` Убб-лор — в книге только упоминание, без характеристик.
- [low] `coc:creature:venomous-spider` Ядовитый паук — Блока характеристик в книге нет: для пауков книга прямо называет профиль ненужным. Потеря рассудка не указана.
- [low] `coc:creature:wasp-and-bee-swarm` Рои ос и пчёл — блока характеристик в книге нет: статья даёт только правила роя (длительность, бросок ВЫН, последствия). Потеря рассудка не указана.

### веб-помощник (`web-helper-coc`) — 16

**Контекст** (16)

- [low] `coc:spell:call-dismiss-atlach-nacha` Вызов/изгнание Атлач-Начи — В книгах статьи нет — только название из статблока; механика — по общему заклинанию «Вызов божества» («Книга хранителя», с. 245, 248).
- [low] `coc:spell:call-dismiss-cthulhu` Вызов/изгнание Ктулху — В книгах статьи нет — только название из статблока; механика — по общему заклинанию «Вызов божества» («Книга хранителя», с. 245, 248).
- [low] `coc:spell:call-dismiss-nyarlathotep` Вызов/изгнание Ньярлатхотепа — В книгах статьи нет — по веб-помощнику. «Вызвать рогатого мужа» — название из списка заклинаний книги в КХ (Call Forth the Horned Man).
- [low] `coc:spell:contact-atlach-nacha` Связь с божеством: Атлач-Нача — В книгах статьи нет — только название из статблока; механика — по общему заклинанию «Связь с божеством» («Книга хранителя», с. 254).
- [low] `coc:spell:contact-father-dagon` Связь с Отцом Дагоном — в книгах статьи нет — по веб-помощнику; время сотворения взято из общих правил заклинаний связи.
- [low] `coc:spell:contact-ghatanothoa` Связь с божеством: Гатанотоа — в книгах статьи нет — по веб-помощнику; цена и время — по общим правилам «Связи с божеством» (русская КХ).
- [low] `coc:spell:contact-hastur` Связь с божеством: Хастур — В книгах статьи нет — только название из статблока; механика — по общему заклинанию «Связь с божеством» («Книга хранителя», с. 254).
- [low] `coc:spell:contact-lrogg` Связь с божеством: Лрогг — В книгах статьи нет — только название из статблока; механика — по общему заклинанию «Связь с божеством» («Книга хранителя», с. 254).
- [low] `coc:spell:contact-mother-hydra` Связь с Матерью Гидрой — в книгах статьи нет — по веб-помощнику; время сотворения взято из общих правил заклинаний связи.
- [low] `coc:spell:contact-nyogtha` Связь с божеством: Ниогта — в книгах статьи нет — по веб-помощнику; цена и время — по общим правилам «Связи с божеством» (русская КХ). «Связь с темнейшим» — название в гримуаре по веб-помощнику.
- [low] `coc:spell:contact-shudde-mell` Связь с Шудде-Мьеллом — в книгах статьи нет — по веб-помощнику; цена и время — по общим правилам «Связи с божеством» (русская КХ).
- [low] `coc:spell:contact-yibb-tstll` Связь с божеством: Йибб-Тистл — в книгах статьи нет — по веб-помощнику; цена и время — по общим правилам «Связи с божеством» (русская КХ). «Наваждения Того, Кто Топит» — название в гримуаре по веб-помощнику.
- [low] `coc:spell:contact-yuggya` Связь с божеством: Юггья — в книгах статьи нет — по веб-помощнику; цена и время — по общим правилам «Связи с божеством» (русская КХ). В базе нет существа Юггья — refs пусты.
- [low] `coc:spell:mesmerize` Заворожить — Только название из статблока (Саайтии, Malleus Monstrorum); в книгах статьи нет.
- [low] `coc:spell:summon-bind-chthonian` Призыв/укрощение хтонийца — Только название из статблока (Айхорт, русская «Книга хранителя»); в книгах статьи нет — механика по общему заклинанию «Призыв/укрощение» (Grand Grimoire).
- [low] `coc:spell:summon-bind-ghoul` Призыв/укрощение упыря — Только название из статблока (Айхорт, русская «Книга хранителя»); в книгах статьи нет — механика по общему заклинанию «Призыв/укрощение» (Grand Grimoire).

### Ктулху: Тёмные века (фанатский перевод 2-го издания 7e) (`temnye-veka-tri-stsenariya-ru`) — 15

**Тексты** (3)

- [low] с. 0 (физ. 1) — с. 3 (физ. 4): 3 стр., 1000 слов не цитирует ни одна запись; headings: HORROR ROLEPLAYING DURING THE DARK AGES; England, with nothing but their wits; Dark Ages begins…; Printed in Lithuania
- [low] с. 263 (физ. 264) — с. 270 (физ. 271): 8 стр., 1577 слов не цитирует ни одна запись; headings: THE HUNT; INDEX; Assets ����������������������71, 73, 98, 99; Aberffraw�����������������������������������36; near: Библиография (Тёмные века); Лист сыщика Тёмных веков
- [low] с. 273 (физ. 274): 1 стр., 317 слов не цитирует ни одна запись; headings: HORROR ROLEPLAYING DURING THE DARK AGES; England, with nothing but their wits; Dark Ages begins…; Printed in Lithuania; near: Лист сыщика Тёмных веков

**Картинки** (12)

- [high] с. 192 (физ. 193): 1 карт. (518×767); без картинки: Хартверу (character), Иса (character), Кость пальца святого Мартина (item)
- [high] с. 193 (физ. 194): 1 карт. (491×786); без картинки: Альфред (character), Хартверу (character)
- [high] с. 196 (физ. 197): 1 карт. (475×682); без картинки: Эдд (character), Хафден (character), Свиток «Президии Финиум» и шкура ночного призрака (item)
- [high] с. 197 (физ. 198): 1 карт. (512×736); без картинки: Синред (character), Эрнвульф (character), Годред и Гримволд (character), Хафден (character), Хигит (character)
- [high] с. 198 (физ. 199): 1 карт. (538×719); без картинки: Годред и Гримволд (character), Хигит (character), Вульфрун (character), Продукция варениев (item)
- [high] с. 201 (физ. 202): 1 карт. (502×683); без картинки: Элфгиест (character), Ламбин (character), Унфурт (character), Сыворотка подчинения (item)
- [high] с. 206 (физ. 207): 1 карт. (517×829); без картинки: Ланфранк (character), Окта (character), Ослафа (character), Медовуха Милдойны (item)
- [high] с. 207 (физ. 208): 1 карт. (457×733); без картинки: Гай Монс (character), Окта (character), Мерзкий грибок (item)
- [high] с. 210 (физ. 211): 1 карт. (465×744); без картинки: Гримцител (character), Хотер (character), Джумин (character), Ланфранк (character), Медвин (character)
- [high] с. 212 (физ. 213): 1 карт. (1031×668); без картинки: Медвин (character), Пенда Орлиный Глаз (character)
- [high] с. 214 (физ. 215): 1 карт. (578×815); без картинки: Викинги, люди Ингви (character)
- [medium] с. 209 (физ. 210): 1 карт. (358×498); без картинки: Хлод, члены банды Эдрика (character)

### Cthulhu Dark Ages (7e, предварительная версия — не изданная книга) (`cthulhu-dark-ages-en`) — 13

**Тексты** (13)

- [high] с. 7 — с. 31: 24 стр., 11011 слов не цитирует ни одна запись; headings: Introduction to the; Second Edition; Chad Bowser and Andi Newton; Cthulhu Dark Ages; near: Булава; Копьё длинное; Копьё короткое
- [high] с. 35 — с. 41: 7 стр., 3899 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Where are the; Shields; Equipment and Weapons; near: Баллиста; Катапульта; Требушет гибридный
- [high] с. 45 — с. 47: 3 стр., 1840 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Entering the Order; Peasants may become servants of the monastery,; The Monastic Offices; near: Доктрина Тёмных веков; Игровая система (Тёмные века); Статус и расходы сыщика (Тёмные века)
- [high] с. 73 — с. 82: 9 стр., 4893 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Anglo-Saxon England; Anglo-Saxon life—there’s a Bibliography for Keepers to; He’s responsible for administration, meting out justice,; near: Альтернативная проверка Рассудка (Тёмные века); Встреча с монстром (Тёмные века); Преступление и наказание
- [high] с. 84 — с. 88: 5 стр., 2900 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Mutilation and Execution; Outlawry; Feuds; near: Вера: христианство и народные верования; Преступление и наказание
- [high] с. 90 — с. 93: 4 стр., 2370 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; From; Mar 1051; The Old Ways; near: Вера: христианство и народные верования; Здоровье и исцеление
- [high] с. 95 — с. 99: 5 стр., 3255 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Canterbury (Cantwaraburh); Gazzetteer of; Anglo-Saxon England; near: Здоровье и исцеление; Расследование ужасов в Тёмные века; Соберите группу вместе (Тёмные века)
- [high] с. 108 — с. 119: 12 стр., 7811 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; The Cthulhu Mythos; Playtest Notes; The Mythos In The; near: Вызов Бугг-Шаша; Максимальный ужас (Тёмные века)
- [high] с. 122 — с. 153: 31 стр., 12887 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Ghoul, Contact Sand Dweller, Contact Deity/Nyarlatho-; Song of Yste; Testament of Carnamagos; near: Вызов/изгнание Рлима Шайкорта
- [high] с. 178 — с. 181: 4 стр., 2290 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; The Hunt; Involving the Investigators; Keeper’s Background; near: Озеро Северн; Опередить похитителей; Остров
- [high] с. 183 — с. 203: 19 стр., 10088 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Edric the Bloodhand; Savvy investigators will realize that Edric, despite; The Gotii Village; near: Аббатство; Автомат; Авторы
- [low] с. 4: 1 стр., 350 слов не цитирует ни одна запись; headings: Authors; Clear Credit; Supplementary Rules and Development; Mike Mason
- [low] с. 43: 1 стр., 557 слов не цитирует ни одна запись; headings: Cthulhu Dark Ages; Christianity, Eastern Orthodox Christianity, Judaism,; Religion; Players Guide to the Dark Ages; near: Доктрина Тёмных веков; Устные традиции (Тёмные века)

### Keeper's Companion (англ., 7e) (`keepers-companion-en`) — 13

**Тексты** (2)

- [low] с. 2 (физ. 3) — с. 3 (физ. 4): 2 стр., 708 слов не цитирует ни одна запись; headings: CREDITS; Authors; Gauntlett, and Al Smith; Executive Producer
- [low] с. 215 (физ. 216) — с. 224 (физ. 225): 9 стр., 1754 слов не цитирует ни одна запись; headings: APPENDIX E; INDEX; Chases, Switching Movement Modes��������������������83; Recovery, Major Wound (Speedier)������������������������74; near: Листы сыщика «Компаньона хранителя»

**Картинки** (8)

- [high] с. 155 (физ. 156): 1 карт. (806×739); без картинки: Револьвер Харриса (item), Шкатулка-головоломка (item)
- [medium] с. 5 (физ. 6): 1 карт. (1193×1553); на странице: Введение в «Компаньон хранителя»
- [medium] с. 85 (физ. 86): 1 карт. (1188×1549); на странице: Пункты рассудка, Новый взгляд на Рассудок
- [medium] с. 123 (физ. 124): 1 карт. (1171×805); на странице: Сдвиг фазы, Призыв тумана, Телепатия
- [low] с. 40 (физ. 41): 1 карт. (616×706); на странице: Вовлечение организации, Лист организации
- [low] с. 74 (физ. 75): 1 карт. (737×415); на странице: Ускоренное выздоровление от серьёзной раны, Раны и лечение: новый взгляд
- [low] с. 96 (физ. 97): 1 карт. (1132×284); на странице: Повышение пунктов рассудка, Шок за кадром, Отыгрыш потери рассудка
- [low] с. 159 (физ. 160): 1 карт. (667×723); на странице: Дейзи Гарсия, Эрма Барнс, Хозяин

**Связи** (3)

- [low] `keepers-companion-en/scene/puzzler-lost-in-art` Потерянные в картине — сцена без места; сценарий keepers-companion-en/scenario/what-a-puzzler
- [low] `keepers-companion-en/scene/puzzler-putting-the-pieces-together` Собирая кусочки — сцена без места; сценарий keepers-companion-en/scenario/what-a-puzzler
- [low] `keepers-companion-en/scene/puzzler-the-pale-man` Бледный человек — сцена без места; сценарий keepers-companion-en/scenario/what-a-puzzler

### Лохмотья Короля (`lokhmotya-korolya-ru`) — 13

**Картинки** (6)

- [high] с. 20: 1 карт. (484×663); без картинки: Раздаточный материал «Лохмотья Короля» № 4: письмо доктора Хайсмита (handout)
- [medium] с. 41: 1 карт. (771×940); на странице: Беседа с доктором Хайсмитом (scene)
- [low] с. 42: 1 карт. (652×530); на странице: Похоронное бюро Эймса (location), Дом Роби (location), Церковь Святого Петра (location), Освещение убийств Роби в новостях (scene)
- [low] с. 54: 1 карт. (660×856); на странице: Допрос Эванса (scene)
- [low] с. 211: 1 карт. (456×281); на странице: Университет: упоминание о Дракмаре (scene)
- [low] с. 336: 1 карт. (369×727); на странице: Раздаточный материал «Лохмотья Короля» № 8: «Смертельное ножевое ранение в Св. парк Джеймса»

**Связи** (6)

- [low] `lokhmotya-korolya-ru/scene/flight-bacon-obituary` Некролог Бэкона — сцена без места; сценарий lokhmotya-korolya-ru/scenario/flight-north
- [low] `lokhmotya-korolya-ru/scene/flight-gresty-second-letter` Второе письмо Грести — сцена без места; сценарий lokhmotya-korolya-ru/scenario/flight-north
- [low] `lokhmotya-korolya-ru/scene/flight-roby-note-to-delia` Записка Роби к Делии — сцена без места; сценарий lokhmotya-korolya-ru/scenario/flight-north
- [low] `lokhmotya-korolya-ru/scene/springer-gresty-first-letter` Первое письмо Уилфреда Грести — сцена без места; сценарий lokhmotya-korolya-ru/scenario/springer-mound
- [low] `lokhmotya-korolya-ru/scene/springer-highsmith-letter` Письмо от доктора Хайсмита — сцена без места; сценарий lokhmotya-korolya-ru/scenario/springer-mound
- [low] `lokhmotya-korolya-ru/scene/talk-the-gap-year` Перерыв: год между Шотландией и Грести — сцена без места; сценарий lokhmotya-korolya-ru/scenario/talk-of-goatswood

**Контекст** (1)

- [low] `lokhmotya-korolya-ru/handout/drakmar-handout-29-schippone-diary` Раздаточный материал «Лохмотья Короля» № 29: дневник Карло Скиппоне (итальянский текст) — Текст на картинках не расшифровывается: это рукописный итальянский оригинал, по сюжету — то, что сыщикам ещё нужно перевести (Р-130: в text — пересказ). В русском издании четыре листа (с. 354–355, до 

### Царство Террора (`tsarstvo-terrora-ru`) — 13

**Тексты** (1)

- [low] с. 3: 1 стр., 472 слов не цитирует ни одна запись; headings: CREDITS; Author; Mark Morrison; Additional Writing

**Картинки** (7)

- [high] с. 57: 1 карт. (1193×1530); без картинки: Максимилиан Робеспьер (character)
- [medium] с. 2: 1 карт. (1080×1080); страницу не цитирует никто
- [medium] с. 5: 1 карт. (1147×1481); на странице: Царство Террора
- [medium] с. 17: 1 карт. (1147×1481); на странице: Площадь Революции (location), Нарратив пролога: Человек в повозке (scene)
- [medium] с. 20: 1 карт. (832×1072); на странице: Катакомбы (location), Начало: кладбище (scene), Карета (scene)
- [medium] с. 74: 1 карт. (972×1237); на странице: Зачаровать жертвенный кинжал, Ритуал жертвоприношения, Царство #5: отрывок из «Верховной Пустоты»
- [low] с. 99: 1 карт. (912×591); на странице: Хронология Французской революции («Царство Террора»)

**Контекст** (5)

- [low] `tsarstvo-terrora-ru/character/1794-richebourg` Ришбур — Только характеристики для погони (Скорость 7, ВЫН 60, ЛВК 50, СИЛ 45 и четыре навыка), как в книге и в английском оригинале; половина и пятая навыков посчитаны (в книге их нет). Герцогиня Орлеанская с
- [low] `tsarstvo-terrora-ru/creature/seed-bastille-thing` Нечто в Бастилии — Своего статблока нет: книга велит брать характеристики огненного вампира (coc:creature:fire-vampire) с заменой жара на холод. Название записи — по заголовку задумки.
- [low] `tsarstvo-terrora-ru/creature/seed-gaueko` Гауэко — Своего статблока нет — по профилю бесформенного отродья (instance_of). В переводе — «бесформенное порождение Цатхоггуа».
- [low] `coc:spell:enchant-sacrificial-dagger` Зачаровать жертвенный кинжал — Новое заклинание кампании «Царство Террора»: книга только называет его (с. 73, 96), механика — из сюжета (с. 66, 74, 78), вывод из текста (Р-41). В Grand Grimoire заклинания нет. С «Зачаровать нож» (c
- [low] `coc:spell:ritual-of-sacrifice` Ритуал жертвоприношения — Новое заклинание кампании «Царство Террора» (фанатский перевод 7e — источник русского текста). Цены, времени сотворения и проверок книга не даёт: в `cost` и `casting_time` — то, что сказано во врезке 

### Ведомо ли любви прощение Ктулху (`vedomo-li-lyubvi-ru`) — 13

**Тексты** (2)

- [low] с. 57 (физ. 58): 1 стр., 152 слов не цитирует ни одна запись; headings: БИОГРАФИИ АВТОРОВ; АЙРИС КАМИНСКА; Японовед по образованию, Айрис является координатором; АННА МАРИЯ МАЗУР
- [low] с. 60 (физ. 61): 1 стр., 216 слов не цитирует ни одна запись; headings: ПРОЩЕНИЕ; Люблю тебя до смерти; Маска желания; Рестоном были приглашены на вечеринку в шикарные

**Картинки** (11)

- [high] с. 10 (физ. 11): 2 карт. (892×460, 818×450); без картинки: Эллен О’Салливан (character), Ивонн Лакур (character), Люсиль Моран (character)
- [high] с. 16 (физ. 17): 2 карт. (848×464, 782×453); без картинки: Ханджар (item)
- [high] с. 33 (физ. 34): 2 карт. (612×604, 571×579); без картинки: Сэм Гэррити (character), Миссис Ленокс (character), Деревянная коробка с маской (item)
- [high] с. 36 (физ. 37): 1 карт. (636×726); без картинки: Деревянная коробка с маской (item)
- [medium] с. 8 (физ. 9): 2 карт. (1016×1255, 911×1178); на странице: Материал: Любовь 1 — детство сыщика
- [medium] с. 9 (физ. 10): 2 карт. (1016×1258, 912×1181); на странице: Материал: Любовь 2 — последнее письмо Эллен
- [medium] с. 15 (физ. 16): 2 карт. (1016×1257, 912×1181); на странице: Материал: Любовь 4 — показания Гузенберга
- [medium] с. 18 (физ. 19): 2 карт. (944×1292, 1249×869); на странице: Материал: Любовь 7 — дневник Хэтти
- [medium] с. 27 (физ. 28): 2 карт. (1016×1258, 912×1181); на странице: Материал: Маска 1 — об Анне и Лукасе
- [medium] с. 38 (физ. 39): 1 карт. (380×380); без картинки: Японские телохранители (2) (character), Деревянная коробка с маской (item)
- [low] с. 34 (физ. 35): 4 карт. (584×659, 505×652, 872×496, 793×446); на странице: Неожиданная посылка (scene)

### Dead Light and Other Dark Turns (`dead-light-en`) — 12

**Тексты** (1)

- [low] с. 84 (физ. 85) — с. 89 (физ. 90): 5 стр., 1068 слов не цитирует ни одна запись; headings: INDEX; STORY SEEDS; AUTHOR BIOGRAPHIES; ALAN BLIGH

**Картинки** (10)

- [high] с. 20 (физ. 21): 1 карт. (674×1048); без картинки: Клем Тейлор (character), Годфри Уэбб (character), Бюро доктора Уэбба (item), Ключ от бюро (item), Бумажник Клема (item)
- [high] с. 21 (физ. 22): 1 карт. (674×1049); без картинки: Бюро доктора Уэбба (item), Ароматная восковая мазь (item), Дневник доктора Уэбба (tome)
- [high] с. 22 (физ. 23): 1 карт. (674×1048); без картинки: Карманная Библия доктора (item), Дневник доктора Уэбба (tome)
- [high] с. 51 (физ. 52): 2 карт. (1076×728, 983×637); без картинки: Бесформенный (creature), Жезл Вероники (item)
- [high] с. 52 (физ. 53): 2 карт. (600×720, 504×652); без картинки: Бесформенный (creature), Журнал Вероники (item)
- [high] с. 55 (физ. 56): 2 карт. (660×924, 553×855); без картинки: Малый ключ Соломона (tome), Керосин (item), Жезл Вероники (item)
- [medium] с. 23 (физ. 24): 1 карт. (674×1049); на странице: Подвал Гринэпл-Акра (location), Амбар-гараж Гринэпл-Акра (location), Коттедж Гринэпл-Акр (scene), Охота Мертвенного света (scene)
- [medium] с. 31 (физ. 32): 1 карт. (1229×1589); на странице: Поместье Уэйлендов (location), Дом Уэйлендов (location)
- [medium] с. 50 (физ. 51): 2 карт. (1076×728, 983×637); на странице: Покой (location), Молельня (location)
- [low] с. 24 (физ. 25): 2 карт. (668×880, 591×837); на странице: До рассвета (scene), Охота Мертвенного света (scene)

**Контекст** (1)

- [low] `coc:spell:recall-sin-eater` Призыв пожирателя грехов — Заклинание из дневника доктора Уэбба (сценарий «Dead Light», сборник «Dead Light and Other Dark Turns», 2019). Книга называет его только в профиле дневника и указателе («Recall Sin-Eater Spell», с. 28

### Keeper Rulebook (англ.) (`keeper-rulebook-en`) — 12

**Тексты** (12)

- [high] с. 4 (физ. 5) — с. 8 (физ. 9): 4 стр., 1241 слов не цитирует ни одна запись; headings: Acknowledgements; Matthew Sanderson, Dean Engelhardt, Matt Anderson,; Kramer, Scott David Aniolowski, Brian Courtemache, Brian; Dedications
- [high] с. 22 (физ. 23) — с. 27 (физ. 28): 6 стр., 3851 слов не цитирует ни одна запись; headings: Call of Cthulhu; Howard Philips; Lovecraft; His Life and the Creation of
- [high] с. 56 (физ. 57) — с. 79 (физ. 80): 23 стр., 13660 слов не цитирует ни одна запись; headings: Call of Cthulhu; Skill List; Electrical Repair (10%); Fast Talk (05%); near: Описание навыков; Проверка двух и более навыков
- [high] с. 285 (физ. 286) — с. 327 (физ. 328): 43 стр., 23761 слов не цитирует ни одна запись; headings: Colours Out of Space; Colour out of Space; Though incorporeal, its passing nonetheless feels like; INT; near: Песнопение Вак-Вирадж; Породить отродье
- [high] с. 329 (физ. 330) — с. 335 (физ. 336): 7 стр., 3855 слов не цитирует ни одна запись; headings: SPAWN OF UBBO-SATHLA; STR; CON; SIZ; near: Породить отродье; Чутьё на добычу
- [high] с. 346 (физ. 347) — с. 363 (физ. 364): 18 стр., 10428 слов не цитирует ни одна запись; headings: Call of Cthulhu; Amidst the; Ancient Trees; Introduction; near: Багровые письмена
- [high] с. 406 (физ. 407) — с. 419 (физ. 420): 14 стр., 5350 слов не цитирует ни одна запись; headings: Call of Cthulhu; Summary of; Game System; Rules; near: Бомба трубчатая; Граната ручная; Гранатомёт «M72 LAW»
- [medium] с. 283 (физ. 284): 1 стр., 647 слов не цитирует ни одна запись; headings: SPECIAL POWERS; Chthonians; BYAKHEE, The star-steeds; STR; near: Заклинания чудовищ; Как убить чудовище; Песнопение Вак-Вирадж
- [low] с. 35 (физ. 36): 1 стр., 211 слов не цитирует ни одна запись; headings: STR+SIZ; near: Создаём своего сыщика; Шаг 2. Выбор рода занятий; Шаг 3. Выбор навыков и распределение пунктов навыков
- [low] с. 338 (физ. 339): 1 стр., 433 слов не цитирует ни одна запись; headings: Call of Cthulhu; Horse; RAT PACK; STR; near: Почувствовать жизнь; Учуять что-то интересное
- [low] с. 386 (физ. 387) — с. 389 (физ. 390): 4 стр., 2176 слов не цитирует ни одна запись; headings: Call of Cthulhu; An alphabetical index of the key termi-; Cthulhu Mythos from secondary sourc-; Skill points are immediately deducted as; near: Использование материалов из предыдущих изданий «Зова Ктулху»; Перенос сыщиков
- [low] с. 426 (физ. 427) — с. 436 (физ. 437): 11 стр., 8448 слов не цитирует ни одна запись; headings: Call of Cthulhu; Andrew Nicholson, Matthew Sanderson, Paul David Watts,; Plageman, Chris Padgett, Chad Roberts, Thomas Shavor,; Don Campagna, Rusty Totten-Emerson, Mike Vergamini,

### Наедине с помехами (`naedine-s-pomekhami-ru`) — 10

**Картинки** (10)

- [medium] с. 5: 1 карт. (1245×562); на странице: Наедине с помехами
- [medium] с. 7: 2 карт. (480×465, 1245×562); на странице: Наедине с помехами
- [medium] с. 9: 1 карт. (1245×562); на странице: Журнал, Наедине с помехами
- [medium] с. 110: 1 карт. (608×490); без картинки: Дарси (character)
- [medium] с. 184: 1 карт. (1749×2274); на странице: Чарли
- [medium] с. 185: 1 карт. (1753×2269); страницу не цитирует никто
- [medium] с. 186: 1 карт. (1751×2278); на странице: Алекс
- [medium] с. 187: 1 карт. (1753×2269); страницу не цитирует никто
- [low] с. 82: 1 карт. (669×479); страницу не цитирует никто
- [low] с. 139: 1 карт. (469×372); на странице: Последователи Дитя Леса (organization)

### Viral (`viral-en`) — 10

**Картинки** (10)

- [medium] с. 111: 1 карт. (1228×1588); на странице: Марко Энтони Мальони
- [medium] с. 112: 1 карт. (1228×1588); на странице: Марко Энтони Мальони
- [medium] с. 113: 1 карт. (1228×1588); на странице: Коррина Тренч
- [medium] с. 114: 1 карт. (1228×1588); на странице: Коррина Тренч, Ведьмина доска Коррины
- [medium] с. 115: 1 карт. (1228×1588); на странице: Инок Джеремайя Икинс
- [medium] с. 116: 1 карт. (1228×1588); на странице: Инок Джеремайя Икинс
- [medium] с. 117: 1 карт. (1228×1588); на странице: Питер Уортон
- [medium] с. 118: 1 карт. (1228×1588); на странице: Питер Уортон
- [medium] с. 119: 1 карт. (1228×1588); на странице: Ку Хён
- [medium] с. 120: 1 карт. (1228×1588); на странице: Ку Хён

### Карнавал безумия (`karnaval-bezumiya-ru`) — 9

**Картинки** (5)

- [high] с. 25: 2 карт. (1644×1308, 1656×1324); без картинки: Грег Джонсон (character)
- [high] с. 66: 1 карт. (1756×2242); без картинки: Девять монолитов (item)
- [medium] с. 4: 1 карт. (1824×2362); на странице: Плакат «Пропала»
- [medium] с. 24: 4 карт. (1644×1308, 1509×1174, 1656×1324, 1508×1173); на странице: Буклет Карнавала Пандемониум
- [medium] с. 89: 1 карт. (2346×1824); на странице: Лес вокруг карнавала (location)

**Контекст** (4)

- [low] `karnaval-bezumiya-ru/character/alisa-lankaster` Алиса Ланкастер — Предложенный сыщик зацепки «Исследователи Мифов»; листа персонажа в книге нет.
- [low] `karnaval-bezumiya-ru/character/dzhordzh-uells` Джордж Уэллс — Предложенный сыщик зацепки «Исследователи Мифов»; листа персонажа в книге нет.
- [low] `karnaval-bezumiya-ru/character/lukas-uebb` Лукас Уэбб — Предложенный сыщик зацепки «Исследователи Мифов»; листа персонажа в книге нет.
- [low] `karnaval-bezumiya-ru/character/zoi-satton` Зои Саттон — Предложенный сыщик зацепки «Исследователи Мифов»; листа персонажа в книге нет.

### Миры Говарда Филлипса Лавкрафта: артефакты и легендарные… (`miry-lavkrafta-artefakty-ru`) — 9

**Тексты** (4)

- [high] с. 106 (физ. 108) — с. 108 (физ. 110): 3 стр., 436 слов не цитирует ни одна запись; headings: Первоисточники; Каркоза; Пнакотикские манускрипты; Земля Мнар
- [low] с. 2 (физ. 4): 1 стр., 149 слов не цитирует ни одна запись; headings: ББК 84 (2Рос-Рус)6; М64; Серия «Самая страшная книга (подарочная)»; Оформление обложки Алексея Провоторова
- [low] с. 5 (физ. 7): 1 стр., 178 слов не цитирует ни одна запись; headings: От авторов
- [low] с. 111 (физ. 113): 1 стр., 214 слов не цитирует ни одна запись; headings: Об авторах; Артем Агеев; Алексей Лотерман; Поклонник Мифов Ктулху, писатель и переводчик-любитель, автор

**Картинки** (5)

- [medium] с. -1 (физ. 1): 1 карт. (1654×2206); страницу не цитирует никто
- [medium] с. 0 (физ. 2): 1 карт. (1246×1658); страницу не цитирует никто
- [medium] с. 121 (физ. 123): 1 карт. (1246×1658); страницу не цитирует никто
- [medium] с. 122 (физ. 124): 1 карт. (1654×2206); страницу не цитирует никто
- [low] с. 119 (физ. 121): 1 карт. (525×446); страницу не цитирует никто

### Террор (`terror-ru`) — 9

**Картинки** (6)

- [medium] с. 1 (физ. 2): 1 карт. (1245×1621); на странице: Террор
- [medium] с. 2 (физ. 3): 1 карт. (1245×1621); на странице: Террор
- [medium] с. 3 (физ. 4): 2 карт. (1245×1621, 1229×1589); на странице: Террор
- [medium] с. 8 (физ. 9): 1 карт. (480×465); без картинки: Эдуард Бергер (character), Рубашов (character)
- [medium] с. 20 (физ. 21): 1 карт. (480×465); без картинки: Виктор Семёнович Червяков (character), Аркадий Лунин (character), Метеоритное нечто (creature), Бабуин (метеоритное нечто) (creature), Фотография на болоте (item)
- [low] с. 26 (физ. 27): 3 карт. (588×718, 311×413, 457×787); на странице: Материал № 2: метаморфоза в нечто

**Связи** (2)

- [low] `terror-ru/scene/dopros` Допрос — сцена без места; сценарий terror-ru/scenario/terror
- [low] `terror-ru/scene/poiski-chervyakova` Доктор Червяков: поиски — сцена без места; сценарий terror-ru/scenario/terror

**Контекст** (1)

- [low] `terror-ru/item/papka-tolko-dlya-molotova` Папка «Только для Молотова В.М.» — Содержимое папки книга не описывает. Страницы «с. N» — печатные (печатная = физическая − 1).

### Безымянный туман (`bezymyannyy-tuman-ru`) — 8

**Картинки** (3)

- [high] с. 2: 1 карт. (769×1010); без картинки: Богдан Залевский (character), Дуэйн Шерман (character), Конрад Марш (character), Линда Марш (character), Прислуга Генри Пирса (character)
- [high] с. 7: 1 карт. (773×398); без картинки: Туманное отродье (creature)
- [medium] с. 6: 1 карт. (773×298); без картинки: Дуэйн Шерман (character), Охрана Генри Пирса (character), Полицейский (character), Томас Флэнаган (character), Туманное отродье (creature)

**Контекст** (5)

- [high] `bezymyannyy-tuman-ru/handout/foto-derrika-yorka` Фотография Деррика Йорка — раздатка без текста и картинки
- [high] `bezymyannyy-tuman-ru/handout/foto-rene` Фотография Рене — раздатка без текста и картинки
- [high] `bezymyannyy-tuman-ru/handout/simvol-shchita-akhilla` Символ «Щита Ахилла» — раздатка без текста и картинки
- [low] `bezymyannyy-tuman-ru/creature/bezymyannyy-tuman` Безымянный Туман — Статблока и потери Рассудка за встречу книга не даёт: божество проявляется только туманом Рене. Божество придумано для сценария; с «Безымянной мглой» (Nameless Mist) мифов Лавкрафта — Лумли книга его 
- [low] `bezymyannyy-tuman-ru/tome/kniga-s-simvolom-valknut` Книга культа с символом «Валькнут» — Потеря Рассудка 1/1d6 — за прикосновение (галлюцинация), а не за чтение; прибавки Мифов Ктулху, времени изучения и заклинаний книга не даёт. Название записи — по описанию книги (у неё нет имени).

### Эликсир жизни (`eliksir-zhizni-ru`) — 8

**Картинки** (4)

- [high] с. 1 (физ. 2): 2 карт. (2539×397, 2539×391); без картинки: Дэвид Райт (character), Табельный пистолет инспектора Райта (item)
- [high] с. 2 (физ. 3): 1 карт. (2532×385); без картинки: Брейдли Хартсфилд (character), Дэвид Райт (character), Джон Фокс (character), Корделия Хамфри (character), Нил Фокс (character)
- [high] с. 4 (физ. 5): 2 карт. (2539×397, 2539×391); без картинки: Дэвид Райт (character), Дональд Тайлер (character), Джон Фокс (character), Корделия Хамфри (character), Нил Фокс (character)
- [high] с. 7 (физ. 8): 1 карт. (1476×574); без картинки: Джон Фокс (character), Лора Мартин (character), Мэтью Крайтон (character), Мики (character), Мисти Крайтон (character)

**Контекст** (4)

- [high] `eliksir-zhizni-ru/handout/foto-medalona` Фотография медальона — раздатка без текста и картинки
- [low] `eliksir-zhizni-ru/character/dzhon-foks` Джон Фокс — Статблок — с. 10. МОЩ, ПМ и Удачи книга не даёт. Скорость 8 напечатана; по ЛВК 60 и СИЛ 60 больше ТЕЛ 55 — 9, возраст не указан.
- [low] `eliksir-zhizni-ru/tome/kniga-svyashchennika` Книга священника — Книга не даёт потери Рассудка, прибавки Мифов Ктулху, времени изучения и списка заклинаний.
- [low] `eliksir-zhizni-ru/tome/kniga-zaklinaniy-kulta-salema` Книга заклинаний и ритуалов ведьмовского культа Салема — Книга не даёт потери Рассудка, прибавки Мифов Ктулху, времени изучения и списка заклинаний.

### Мифы Хастура. Том 1: Путь в Каркозу (`mify-hastura-ru`) — 8

**Тексты** (2)

- [low] с. 4 (физ. 6): 1 стр., 205 слов не цитирует ни одна запись; headings: ПРЕДИСЛОВИЕ; ОТ ПЕРЕВОДЧИКА; Перевод материалов из этого сборника - МАРСКОИЕ; Данные статьи позволят проникнуться атмосферой мифов; near: Дорога до Хали; Каркоза
- [low] с. 44 (физ. 46): 1 стр., 121 слов не цитирует ни одна запись; headings: ХАСТУРА; ТОМ 1; ПУТЬ В КАРКОЗУ; near: Король в жёлтом; Король в жёлтом (издание 1895 года)

**Связи** (3)

- [low] `mify-hastura-ru/scene/disappearance` Исчезновение — сцена без места; сценарий mify-hastura-ru/scenario/stage-four-carcosa
- [low] `mify-hastura-ru/scene/search` Поиск — сцена без места; сценарий mify-hastura-ru/scenario/stage-four-carcosa
- [low] `mify-hastura-ru/scene/transport` Транспорт — сцена без места; сценарий mify-hastura-ru/scenario/stage-four-carcosa

**Контекст** (3)

- [low] `mify-hastura-ru/creature/night-flyers` Летящие сквозь ночь — Характеристик в книге нет: «используйте любые характеристики существ, которые вы захотите; они могут стать практически чем угодно эквивалентной массы и размера». Фанатский перевод (издание trusted): р
- [low] `mify-hastura-ru/creature/unseen-horse` Незримый Конь — Явление без характеристик и без атак. Фанатский перевод (издание trusted): русский текст — источник, флаг translated не ставится (Р-230, Р-147). Книга — скан: текст по распознаванию, числа и кубы свер
- [low] `mify-hastura-ru/tome/le-roi-en-jaune-1895` Король в жёлтом (издание 1895 года) — Числа чтения (потеря Рассудка, Мифы Ктулху, время изучения) книга не даёт — см. общую запись. Язык не назван (французское заглавие — только название). Другие датировки в сборнике: «напечатана частным 

### Особняки безумия. За закрытыми дверями (`osobnyaki-bezumiya-ru`) — 8

**Тексты** (2)

- [medium] с. 8 (физ. 9) — с. 9 (физ. 10): 2 стр., 681 слов не цитирует ни одна запись; headings: ПРЕЙИСАОВИЕ; НЕМНОГО ИСТОРИИ; Первое издание «Особняков безумия» было опубликова-; Майкла (Шона) Девульфа, «Плантация» Уэсли Мартина,; near: Материал «Корбитт 4»: дневники Корбитта
- [low] с. 220 (физ. 221) — с. 225 (физ. 226): 5 стр., 784 слов не цитирует ни одна запись; headings: Карты; Владения мистера Корбитта; УВИЕрОкОВ) 15, 189; Дом Корбитта

**Связи** (5)

- [low] `osobnyaki-bezumiya-ru/scene/code-letter` Завязка: письмо — сцена без места; сценарий osobnyaki-bezumiya-ru/scenario/code-secret-code
- [low] `osobnyaki-bezumiya-ru/scene/code-meeting-connolly` Знакомство с Коннолли — сцена без места; сценарий osobnyaki-bezumiya-ru/scenario/code-secret-code
- [low] `osobnyaki-bezumiya-ru/scene/code-ordinary-day` Самый обычный день — сцена без места; сценарий osobnyaki-bezumiya-ru/scenario/code-secret-code
- [low] `osobnyaki-bezumiya-ru/scene/crooked-preliminary-research` Предварительное расследование — сцена без места; сценарий osobnyaki-bezumiya-ru/scenario/crooked-manse
- [low] `osobnyaki-bezumiya-ru/scene/memphis-staying-on-track` Как не сбиться со следа — сцена без места; сценарий osobnyaki-bezumiya-ru/scenario/memphis-house-of-memphis

**Контекст** (1)

- [low] `osobnyaki-bezumiya-ru/character/memphis-edith` Эдит — Полного статблока в книге нет: только пункты здоровья (с. 114).

### Туманы острова Сан-Кристобаль (`tumany-san-kristobal-ru`) — 7

**Картинки** (6)

- [high] с. 5 (физ. 6): 1 карт. (692×686); без картинки: Адам Тёрнер (character), Энди Тёрнер (character), Хью Марлоу (character), Уильям Блейк (character), Юджин Хопкинс (character)
- [high] с. 12 (физ. 13): 1 карт. (692×686); без картинки: Адам Тёрнер (character), Энди Тёрнер (character), Хью Марлоу (character), Юджин Хопкинс (character), Нгориеру (creature)
- [medium] с. 2 (физ. 3): 1 карт. (849×1200); на странице: Туманы острова Сан-Кристобаль
- [medium] с. 19 (физ. 20): 1 карт. (1228×1737); на странице: Микки Валентайн, Туманы острова Сан-Кристобаль
- [medium] с. 21 (физ. 22): 1 карт. (1238×1750); на странице: Томас Грин, Туманы острова Сан-Кристобаль
- [medium] с. 23 (физ. 24): 1 карт. (1238×1750); на странице: Мэри Стоун, Туманы острова Сан-Кристобаль

**Контекст** (1)

- [low] `tumany-san-kristobal-ru/creature/kakamora` Какамора — Статблока в книге нет.

### Парк развлечений (`park-razvlecheniy-ru`) — 7

**Контекст** (7)

- [low] `park-razvlecheniy-ru/character/devin-dzhons` Дэвин Джонс — Характеристик в книге нет (только вводная). Связь с маскотом — по хронологии (с. 2: «студент, рабочий»), вывод из текста (Р-41).
- [low] `park-razvlecheniy-ru/character/temmi-dakker` Тэмми Даккер — Характеристик в книге нет (только вводная).
- [low] `park-razvlecheniy-ru/character/tom-dakker` Том Даккер — Характеристик в книге нет (только вводная).
- [low] `park-razvlecheniy-ru/creature/prizrak-sofii-kid` Призрак Софии Кид — Характеристик призрака книга не даёт.
- [low] `park-razvlecheniy-ru/handout/ubiystva-v-parkakh` Данные об убийствах в парках Массачусетса — Книга не печатает текст этой раздатки — в `text` пересказ того, что сказано о других убийствах во вступлении (Р-130).
- [low] `coc:spell:speak-with-the-dead` Общение с мёртвыми — Новое заклинание сценария «Парк развлечений» (русский оригинал, английского названия нет). Книга даёт только название и цену в статблоке Абрахама Перриса; время сотворения, потеря Рассудка и порядок р
- [low] `coc:spell:stupor` Ступор — Новое заклинание сценария «Парк развлечений» (русский оригинал, английского названия нет). Книга даёт только название, длительность и цену в статблоке Абрахама Перриса. Тип «Контроль и разум» и механи

### Beyond the Edge of Darkness (`beyond-the-edge-of-darkness-en`) — 6

**Тексты** (1)

- [low] с. 32 (физ. 36) — с. 33 (физ. 37): 2 стр., 617 слов не цитирует ни одна запись; headings: Appendix A | Acknowledgments; Katy; Thank you for your unwavering love, and; Craig; near: Виктория Блан; Дети Солнечного Диска; Египетский янтарный камень

**Контекст** (5)

- [low] `beyond-the-edge-of-darkness-en/character/imset-aten` Имсет-Атен — Русский текст — по рабочему переводу владельца (2_Обработка/1924 Beyond the Edge of Darkness, Beyond_the_Edge_of_Darkness_Full_RU_v34.html), сверен с английским оригиналом; числа — по английской стран
- [low] `beyond-the-edge-of-darkness-en/creature/sun-husk` Солнечная оболочка — Русский текст — по рабочему переводу владельца (2_Обработка/1924 Beyond the Edge of Darkness, Beyond_the_Edge_of_Darkness_Full_RU_v34.html), сверен с английским оригиналом; числа — по английской стран
- [low] `beyond-the-edge-of-darkness-en/location/amoun-lounge` «Амун-лаунж» — Русский текст — наш перевод с английского оригинала: у владельца этой части нет. Упомянут только в раздатке; описания в книге нет.
- [low] `beyond-the-edge-of-darkness-en/location/lotus-pavilion` «Лотосовый павильон» — Русский текст — наш перевод с английского оригинала: у владельца этой части нет. Упомянут только в раздатке; описания в книге нет.
- [low] `beyond-the-edge-of-darkness-en/tome/handwritten-grimoire` Рукописный гримуар («Чёрная Коза») — Русский текст — по рабочему переводу владельца (2_Обработка/1924 Beyond the Edge of Darkness, Beyond_the_Edge_of_Darkness_Full_RU_v34.html), сверен с английским оригиналом; числа — по английской стран

### Когда зло побеждает (`kogda-zlo-pobezhdaet-ru`) — 6

**Картинки** (4)

- [high] с. 3: 1 карт. (2000×957); без картинки: Джамал Оливер (character)
- [high] с. 6: 1 карт. (2000×957); без картинки: Кларис Макнотон (character)
- [high] с. 9: 1 карт. (2000×957); без картинки: Алтея Пинто (character)
- [high] с. 12: 1 карт. (2000×957); без картинки: Томас Базилински (character)

**Контекст** (2)

- [low] `kogda-zlo-pobezhdaet-ru/character/kultisty` Культисты — Групповой профиль без статблока: чисел книга не даёт; оружие — кухонные ножи (для игры подойдёт нож из справочника, вывод из текста, Р-41). Имена придуманы (Р-151).
- [low] `kogda-zlo-pobezhdaet-ru/creature/avatar-v-tele-melindy` Аватар Ньярлатхотепа в теле Мелинды — Статблока книга не даёт — только описание способностей; числа Хранитель задаёт сам.

### Маленький клуб ужасов (`malenkiy-klub-uzhasov-ru`) — 6

**Картинки** (6)

- [high] с. 3: 2 карт. (2953×602, 2953×301); без картинки: Эван Росс (character), Стивен Смозерс (character), Тайлер Брукс (character)
- [high] с. 4: 1 карт. (626×1399); без картинки: Алан Смозерс (character), Стивен Смозерс (character), Обломки костей в чёрной слизи (item)
- [high] с. 6: 4 карт. (2444×380, 2444×382, 1158×539, 976×1034); без картинки: Алан Смозерс (character), Джеймс Мэдисон (character), Мисс Хейз (character), Стивен Смозерс (character), Надписи красным мелом на стенах Клуба (handout)
- [high] с. 8: 2 карт. (2444×380, 2444×382); без картинки: Стивен Смозерс (character), Красные белки (creature)
- [high] с. 13: 5 карт. (2132×471, 2132×469, 2105×946, 2105×944…); без картинки: Эван Росс (character), Гейл Лайнхэм (character), Коди Беннет (character), Райан Каллахан (character), Сэмюэл Лайнхэм (character)
- [medium] с. 2: 1 карт. (1476×452); страницу не цитирует никто

### Наедине с приливом: правила (`naedine-s-prilivom-rules-ru`) — 6

**Тексты** (1)

- [low] с. 2: 1 стр., 393 слов не цитирует ни одна запись; headings: Автор; АВТОРЫ; Николас Джонсон; Редактирование и доработка

**Картинки** (5)

- [medium] с. 1: 1 карт. (1660×2156); страницу не цитирует никто
- [medium] с. 3: 1 карт. (1307×950); страницу не цитирует никто
- [medium] с. 5: 2 карт. (716×900, 632×827); на странице: Наедине с приливом
- [medium] с. 7: 1 карт. (1350×950); на странице: Наедине с приливом
- [medium] с. 8: 2 карт. (704×888, 633×827); страницу не цитирует никто

### Новая жизнь (`novaya-zhizn-ru`) — 5

**Тексты** (1)

- [low] с. 26: 1 стр., 151 слов не цитирует ни одна запись; near: Эрик Диггори

**Картинки** (1)

- [high] с. 24: 1 карт. (2481×3300); без картинки: Шарлотта Эдингтон (character)

**Контекст** (3)

- [low] `coc:spell:banishment-of-yde-etad-krampus` Изгнание Йде Итад (ритуал Крампуса) — Вариант «Изгнания Йде Итад» из сценария «Новая жизнь» (русский оригинал): книга прямо называет ритуал Крампуса видоизменённым заклинанием «Книги хранителя», но цены, времени и порядка сотворения не пе
- [low] `coc:spell:stop-time` Остановка времени — Новое заклинание сценария «Новая жизнь» (русский оригинал, английского названия нет). Книга даёт только цену и действие одной фразой в статблоке Крампуса. Тип «Врата и путешествия» (заклинания времени
- [low] `coc:spell:telekinesis` Телекинез — Новое заклинание сценария «Новая жизнь» (русский оригинал, английского названия нет). Книга даёт только цену и действие одной фразой в статблоке Крампуса — остальное не напечатано. Тип «Природа и стих

### Рождественская вечеринка (`rozhdestvenskaya-vecherinka-ru`) — 5

**Картинки** (4)

- [high] с. 3: 3 карт. (1537×1129, 1268×996, 254×571); без картинки: Оливер Баренфельд (character), Пригласительное письмо (handout), Поддельные результаты обследования (item)
- [high] с. 7: 1 карт. (1322×2009); без картинки: Анна Стоун (character), Артур Стоун (character), Джо Ландри (character), Маргарет Питчфорд (character), Мейбл Тибодо (character)
- [high] с. 12: 2 карт. (293×775, 1376×1322); без картинки: Артур Стоун (character), Марк (character), Ральф Хэндж (character), Сара (character), «Генерал Кусака» и другие зомби («Рождественская вечеринка») (creature)
- [high] с. 13: 1 карт. (457×1745); без картинки: Артур Стоун (character), Дональд Бонс (character), Дневник Артура Стоуна (item)

**Контекст** (1)

- [low] `coc:spell:teleportatsiya` Телепортация — Заклинание Нинхурсаг из сценария «Рождественская вечеринка» (официальное русское издание, скан без текстового слоя; сверено по изображению страницы; номеров страниц в книге нет — «с. N» — физическая с

### Тень над Провиденсом (`ten-nad-providensom-ru`) — 5

**Картинки** (5)

- [high] с. 3 (физ. 4): 1 карт. (1280×1655); без картинки: Кейтлин Бронсон (character), Джеймс Маклафлин (character), Ибнхотеп (creature), Табличка к канопе Ибнхотепа (item), Экспонаты выставки «Царство пламени» (item)
- [high] с. 36 (физ. 37): 1 карт. (1275×1650); без картинки: Теодор Джеймсон (character)
- [medium] с. 0 (физ. 1): 1 карт. (1280×1655); на странице: Тень над Провиденсом
- [medium] с. 1 (физ. 2): 1 карт. (1296×1688); страницу не цитирует никто
- [medium] с. 2 (физ. 3): 1 карт. (1296×1688); на странице: Тень над Провиденсом

### МТС Харьков 37 (`mts-kharkov-37-ru`) — 5

**Связи** (5)

- [low] `mts-kharkov-37-ru/scene/chtenie-dokumentov` Чтение документов — сцена без места; сценарий mts-kharkov-37-ru/scenario/mts-kharkov-37
- [low] `mts-kharkov-37-ru/scene/eksperimenty` Эксперименты — сцена без места; сценарий mts-kharkov-37-ru/scenario/mts-kharkov-37
- [low] `mts-kharkov-37-ru/scene/radiatsiya` Недопустимая дезинформация: радиация — сцена без места; сценарий mts-kharkov-37-ru/scenario/mts-kharkov-37
- [low] `mts-kharkov-37-ru/scene/tungusskiy-meteorit` Допустимая дезинформация: Тунгусский метеорит — сцена без места; сценарий mts-kharkov-37-ru/scenario/mts-kharkov-37
- [low] `mts-kharkov-37-ru/scene/vzaimodeystvie-s-tsvetom` Взаимодействие с Цветом — сцена без места; сценарий mts-kharkov-37-ru/scenario/mts-kharkov-37

### Погасший маяк (`lightless-beacon-ru`) — 4

**Тексты** (1)

- [low] с. 2 (физ. 3): 1 стр., 241 слов не цитирует ни одна запись; headings: ТИТРЫ; Текст; Ли Карр и Линн Харди; Редактура; near: Погасший маяк

**Картинки** (3)

- [high] с. 16 (физ. 17): 2 карт. (2039×886, 2039×884); без картинки: Анна Тилтон (character)
- [high] с. 17 (физ. 18): 2 карт. (1956×1064, 1956×528); без картинки: Джордж Кэссиди (character), Майкл Тёрнер (character), Сэмюэль Смит (character), Радиоприёмник маяка (item)
- [high] с. 18 (физ. 19): 1 карт. (2358×408); без картинки: Джордж Кэссиди (character), Майкл Тёрнер (character), Сэмюэль Смит (character), Журнал технических проверок маяка (item), Радиоприёмник маяка (item)

### Наедине с приливом (Alone Against the Tide) (`naedine-s-prilivom-ru`) — 4

**Картинки** (2)

- [high] с. 9: 2 карт. (536×652, 456×596); без картинки: Лэнс Сэнфорд (character), Уильям Харрис (character), Жители и гости Эсбери (character)
- [medium] с. 6: 3 карт. (1245×1621, 548×660, 456×596); на странице: Наедине с приливом

**Контекст** (2)

- [low] `naedine-s-prilivom-ru/creature/bokrug` Бокруг — Статблока в книге нет. Общей записи Бокруга в базе нет — кандидат в общую запись (предложение в proposals-tide.json). Картинка — рисунок с обложки (с. 88).
- [low] `naedine-s-prilivom-ru/creature/sushchestva-iba` Существа Иба — Статблока в книге нет. Общей записи существ Иба в базе нет — кандидат в общую запись (предложение). Название — по тексту цилиндров (абз. 204) и подписи к иллюстрации «Существо Иба» (с. 73).

### Наедине с Хэллоуином (Alone on Halloween) (`naedine-s-hellouinom-ru`) — 4

**Контекст** (4)

- [low] `naedine-s-hellouinom-ru/creature/gorgulya` Ожившая горгулья бильярдной — характеристики даны в тексте абзаца; без английского названия
- [low] `naedine-s-hellouinom-ru/creature/krysolyudy` Крысолюды (туннели особняка) — среднее МОЩ и ЛВК напечатано как «52-53»; ИНТ, БкУ и Комплекция в статблоке не даны
- [low] `naedine-s-hellouinom-ru/creature/rastenie-mukholovka` Растение-мухоловка старой оранжереи — ПЗ и прочие характеристики в книге не даны
- [low] `naedine-s-hellouinom-ru/tome/kniga-iz-pentagrammy` Книга из пентаграммы в башне — название дано по месту, книга безымянная

### Сны о Японии (Эра Ктулху 6) (`sny-o-yaponii-ru`) — 4

**Связи** (3)

- [low] `sny-o-yaponii-ru/scene/dreams` Сны о лесе — сцена без места; сценарий sny-o-yaponii-ru/scenario/sny-o-yaponii
- [low] `sny-o-yaponii-ru/scene/researching-aokigahara` Исследуя Аокигахару — сцена без места; сценарий sny-o-yaponii-ru/scenario/sny-o-yaponii
- [low] `sny-o-yaponii-ru/scene/taint-aftermath` Порча: исчезновения знакомых — сцена без места; сценарий sny-o-yaponii-ru/scenario/sny-o-yaponii

**Контекст** (1)

- [low] `sny-o-yaponii-ru/item/maria-postcard` Открытка Марии Сицилии — Текста открытки в книге нет.

### The Cursed Idol of Manco Capác (`cursed-idol-of-manco-capac-en`) — 3

**Тексты** (1)

- [low] с. 50: 1 стр., 232 слов не цитирует ни одна запись; headings: Once Upon… a highly captivating storybook roleplaying; ONCE UPON…; SENTIENCE; Tale

**Картинки** (2)

- [high] с. 19: 2 карт. (1696×2048, 616×707); без картинки: Нико «Ник» Романо (character)
- [high] с. 31: 1 карт. (1799×2048); без картинки: Амулет защиты (item), Метеоритная оболочка идола (item)

### Grand Grimoire of Cthulhu Mythos Magic (`grand-grimoire-en`) — 3

**Тексты** (3)

- [low] с. 3: 1 стр., 432 слов не цитирует ни одна запись; headings: Developed, Revised, and Written by; CREDITS; Mike Mason with Matthew Sanderson; Cover Art
- [low] с. 6: 1 стр., 456 слов не цитирует ни одна запись; headings: INTRODUCTION; Mike Mason, 2016
- [low] с. 195 — с. 202: 8 стр., 1605 слов не цитирует ни одна запись; headings: INDEX; Bind Deep One����������������������22, 42; Activation ���������������� 24, 26, 30, 149; Awful Doom of Cerrit������������23, 34; near: Зимотизм

### The Innsmouth Terror (`innsmouth-terror-en`) — 3

**Тексты** (1)

- [low] с. -1 (физ. 3): 1 стр., 164 слов не цитирует ни одна запись; headings: Written by; John Hedge, with The Playhouse Staff; Editing; Matt ‘Doc’ Tracey; near: Ужас в Иннсмуте

**Картинки** (2)

- [high] с. 15 (физ. 19): 1 карт. (1379×1268); без картинки: Статья о пожаре в театре (item)
- [medium] с. 10 (физ. 14): 3 карт. (1436×1838, 500×688, 929×257); на странице: Раздатка 1-a: письмо (внутреннее)

### Наедине с тьмой: раздатка (`naedine-s-tmoy-handouts-ru`) — 3

**Картинки** (3)

- [medium] с. 1: 4 карт. (6210×4050, 484×1784, 436×1605, 2550×3300); на странице: Головоломка с пирамидой
- [medium] с. 2: 2 карт. (3129×4022, 2550×3300); страницу не цитирует никто
- [medium] с. 3: 4 карт. (3129×4022, 484×1784, 436×1605, 2550×3300); на странице: Головоломка с пирамидой

### Pax Cthuliana (`pax-cthuliana-ru`) — 3

**Тексты** (1)

- [medium] с. 69: 1 стр., 795 слов не цитирует ни одна запись; headings: Bryce Undy; Rajaat; Eric Dodd; Jonathan Westhaven; near: Pax Cthuliana; Бенедикт Саймон; Виньяр Гронстоэль

**Контекст** (2)

- [low] `coc:spell:proritsanie-pax-cthuliana` Прорицание — Заклинание Меган Шнайдер из системно-нейтрального сценария «Pax Cthuliana» (сверено по изображениям страниц): книга не даёт чисел стоимости и времени сотворения. Тип «Познание» и механика «ритуал» (об
- [low] `coc:spell:vosstanovlenie-sigila` Восстановление Сигила — Ритуал из системно-нейтрального сценария «Pax Cthuliana» (сверено по изображениям страниц): книга не называет заклинание и не даёт чисел стоимости и времени. Название «Восстановление Сигила» придумано

### Экспонат новая жизнь (`eksponat-novaya-zhizn-ru`) — 2

**Картинки** (2)

- [high] с. 14: 2 карт. (2134×1195, 600×953); без картинки: Анастасия Калин (character), Арси Клодермайт (character)
- [medium] с. 20: 1 карт. (2484×3234); страницу не цитирует никто

### Наедине с помехами: Чарли (лист персонажа) (`naedine-s-pomekhami-pregens-2-ru`) — 2

**Картинки** (2)

- [medium] с. 1: 3 карт. (1229×653, 440×441, 454×550); на странице: Чарли
- [low] с. 2: 1 карт. (733×791); на странице: Чарли

### Наедине с тьмой: календарь (`naedine-s-tmoy-calendar-ru`) — 2

**Картинки** (2)

- [medium] с. 1: 2 карт. (6210×4050, 2550×3300); на странице: Календарь 1931 года
- [medium] с. 2: 4 карт. (6210×4050, 484×1784, 436×1605, 2550×3300); на странице: Календарь 1931 года

### Наедине с тьмой: готовые персонажи (`naedine-s-tmoy-pregens-ru`) — 2

**Картинки** (2)

- [medium] с. 5: 1 карт. (2540×3278); страницу не цитирует никто
- [medium] с. 6: 1 карт. (2540×3278); страницу не цитирует никто

### Necropolis (англ.) (`necropolis-en`) — 2

**Картинки** (2)

- [high] с. 22 (физ. 11): 2 карт. (902×1143, 902×1176); без картинки: Доктор Джеральд Саттон (character), Нанятые рабочие (character), Саша Карнер (character), Динамит Карнера (item)
- [medium] с. 13 (физ. 2): 1 карт. (902×1174); на странице: Луксор (location), Окрестности Луксора (location), Долина царей (location)

### Ничего кроме ветра (`nichego-krome-vetra-ru`) — 2

**Картинки** (2)

- [medium] с. -3 (физ. 1): 1 карт. (1429×1883); на странице: Ничего, кроме ветра
- [medium] с. -2 (физ. 2): 1 карт. (1414×2000); страницу не цитирует никто

### Три кошмарных вечера (No Time to Scream) (`tri-koshmarnykh-vechera-ru`) — 2

**Тексты** (1)

- [low] с. 103 (физ. 104) — с. 104 (физ. 105): 2 стр., 578 слов не цитирует ни одна запись; headings: ПРИЛОЖЕНИЕ; Б АВТОРЫ; Брайан Холланд; Бриджетт Джеффрис; near: Рисунки Мисси

**Контекст** (1)

- [low] `tri-koshmarnykh-vechera-ru/location/glow-ferma-3-pristroyka` Пристройка — Есть только строка ключа карты (Р-206).

### Лечебница (`lechebnitsa-ru`) — 2

**Связи** (1)

- [low] `lechebnitsa-ru/scene/put-na-ostrov` Путь на остров — сцена без места; сценарий lechebnitsa-ru/scenario/lechebnitsa

**Контекст** (1)

- [low] `lechebnitsa-ru/tome/manuskript-kastro` Манускрипт Кастро — Потери Рассудка, прибавки к Мифам и заклинаний книга не даёт.

### Стартовый набор: Наедине с пламенем (простая версия) (`naedine-s-plamenem-ru`) — 2

**Контекст** (2)

- [low] `naedine-s-plamenem-ru/creature/vspykhnuvshie-zveri` Вспыхнувшие звери — Статблока нет. Что это за звери (волки? койоты?) и реальны ли они, книга не говорит; потеря Рассудка составлена по двум абзацам (успех — абз. 269, провал — абз. 5).
- [low] `coc:spell:vyzov-nebesnogo-plameni` Вызов Небесного Пламени — Только «Наедине с пламенем» (официальный перевод): цены и шанса успеха книга не даёт, механики сотворения нет — только сюжетный исход (абз. 80). Английское название не сверено: английского издания при

### Не забывай меня (`ne-zabyvay-menya-ru`) — 2

**Связи** (2)

- [low] `ne-zabyvay-menya-ru/scene/issledovaniya` Исследования: студия и 7 Gate Films — сцена без места; сценарий ne-zabyvay-menya-ru/scenario/ne-zabyvay-menya
- [low] `ne-zabyvay-menya-ru/scene/ya-chuvstvuyu-sebya-uzhasno` Я чувствую себя ужасно… — сцена без места; сценарий ne-zabyvay-menya-ru/scenario/ne-zabyvay-menya

### Ограбление по-Аркхэмски (`ograblenie-po-arkhemski-ru`) — 2

**Контекст** (2)

- [low] `ograblenie-po-arkhemski-ru/creature/kharkhan` Кхархан — Характеристик у Кхархана книга не даёт: способности — по тексту сцен, без статблока. Мифы Ктулху книга не упоминает; категория «сверхъестественное» — по описанию духа. «Кхарахан» (с. 8) — опечатка име
- [low] `coc:spell:call-kharkhan` Призвание Кхархана — Новое заклинание сценария «Ограбление по-Аркхемски» (русский оригинал). Собственного названия у заклинания в книге нет: «Призвание Кхархана» составлено по словам книги («призвания демона», с. 9; «чтоб

### Попались (`popalis-ru`) — 2

**Связи** (2)

- [low] `popalis-ru/scene/promedlenie` Промедление — сцена без места; сценарий popalis-ru/scenario/popalis
- [low] `popalis-ru/scene/smylis` Смылись? — сцена без места; сценарий popalis-ru/scenario/popalis

### Путеводитель по Аркхэму (Hort, по Arkham Unveiled) (`arkham-guide-hort-ru`) — 1

**Тексты** (1)

- [low] с. 2 — с. 6: 5 стр., 704 слов не цитирует ни одна запись

### Arkham: insert maps (`arkham-insert-maps-en`) — 1

**Картинки** (1)

- [medium] с. 2: 6 карт. (516×516, 515×516, 442×589, 442×590…); страницу не цитирует никто

### Двери во тьму: готовые персонажи (`dveri-vo-tmu-pregens-ru`) — 1

**Картинки** (1)

- [medium] с. 1: 2 карт. (595×808, 1781×536); страницу не цитирует никто

### Лагерь Санни (`lager-sanni-ru`) — 1

**Картинки** (1)

- [medium] с. 3: 1 карт. (1080×1080); на странице: Лагерь Санни

### Маски Ньярлатхотепа: материалы для игроков (рус.) (`masks-of-nyarlathotep-ru-players`) — 1

**Картинки** (1)

- [medium] с. 95: 1 карт. (1264×1771); на странице: Франсуаза Пелетье

### Месяц Ночи (`mesyats-nochi-ru`) — 1

**Тексты** (1)

- [low] с. 3: 1 стр., 162 слов не цитирует ни одна запись; headings: ТИТРЫ; Текст; Эдна Тайлер; Рогалик; near: Месяц ночи

### Women of the French Revolution (`reign-of-terror-women-en`) — 1

**Тексты** (1)

- [low] с. 2 — с. 3: 2 стр., 577 слов не цитирует ни одна запись; headings: CREDITS; Author; Kelly Grant; Editorial; near: Роды занятий сыщиц («Женщины Французской революции»)

### Вне власти времени (`vne-vlasti-vremeni-ru`) — 1

**Картинки** (1)

- [high] с. 9: 1 карт. (352×3508); без картинки: Культисты Йог-Сотота (character), Тавил (character)

### Аукцион (`auktsion-ru`) — 1

**Контекст** (1)

- [low] `auktsion-ru/tome/liber-tenebrea` Liber Tenebrea — Книга Мифов только этого сценария (Р-131). Прибавка к Мифам одна (+8%), без деления на беглое и полное чтение; язык, автор, значение Мифов и время изучения книга не даёт. Названия заклинаний — фанатск

### Bless the Beast and Children (перевод владельца) (`bless-the-beast-and-children-ru`) — 1

**Связи** (1)

- [low] `bless-the-beast-and-children-ru/scene/istoriya-denni-eymsa` История Дэнни Эймса — сцена без места; сценарий bless-the-beast-and-children-ru/scenario/bless-the-beast-and-children

### Черная кассета (`chernaya-kasseta-ru`) — 1

**Контекст** (1)

- [low] `chernaya-kasseta-ru/character/lilya-chizhova` Лиля Чижова — Книга о ней больше ничего не сообщает; то, что копия у неё, — вывод из текста (Р-41). Страницы «с. N» — печатные (печатная = физическая − 1).

### Чулки возле печки (`chulki-vozle-pechki-ru`) — 1

**Контекст** (1)

- [low] `chulki-vozle-pechki-ru/tome/otkroveniya-glaaki-tom-12` Откровения Гла’аки, том XII — Русский текст — фанатский перевод Hort (vk.com/call_of_cthulhu_rpg) сценария Марка Харта «Hung by the Chimney with Care» (Petersen Games, по лицензии Chaosium), издание trusted (Р-227); английского ор

### Двери во тьму (`dveri-vo-tmu-ru`) — 1

**Связи** (1)

- [low] `dveri-vo-tmu-ru/scene/lake-involving` Вовлечение сыщиков — сцена без места; сценарий dveri-vo-tmu-ru/scenario/servants-of-the-lake

### Хэллоуин в Данвиче (`hellouin-v-danviche-ru`) — 1

**Контекст** (1)

- [low] `hellouin-v-danviche-ru/creature/khobgobliny` Хобгоблины — Статблока в книге нет — только проявления и потеря Рассудка.

### Каникулы в Иннсмуте (`kanikuly-v-innsmute-ru`) — 1

**Контекст** (1)

- [low] `kanikuly-v-innsmute-ru/creature/drevniy-glubokovodnyy` Древний Глубоководный — Статблока нет: книга велит взять характеристики обычного Глубоководного (coc:creature:deep-one) и умножить на 1,5.

### Number 7 Dream (`number-7-dream-en`) — 1

**Контекст** (1)

- [low] `number-7-dream-en/character/vincent-tenny` Винсент Тенни — Готовый сыщик. Удача на листе не напечатана. Пол на листе не указан. Профессия «вышибала» — без записи в справочнике. Русский текст — по переводу владельца (2_Обработка/2021 Number 7 Dream/Number_7_Dr

### Омерзительная пятёрка (`omerzitelnaya-pyaterka-ru`) — 1

**Контекст** (1)

- [low] `omerzitelnaya-pyaterka-ru/creature/parazit` Паразит — Уникальное существо сценария: характеристик, атак и потери Рассудка книга не даёт. Категория «существо Мифов» — по смыслу (инопланетная раса), книга связи с известными видами Мифов не называет.

### Призрак (`prizrak-ru`) — 1

**Связи** (1)

- [low] `prizrak-ru/scene/priglashenie` Приглашение — сцена без места; сценарий prizrak-ru/scenario/prizrak

### Secrets of the Kremlin, 1931 (`secrets-of-the-kremlin-en`) — 1

**Контекст** (1)

- [low] `secrets-of-the-kremlin-en/tome/russian-necronomicon` Русский «Некрономикон» — Русский текст — по рабочему переводу владельца (2_Обработка/тайны кремля 1931/document.html), сверен с английским оригиналом; числа — по английской странице; меры переведены в метрические (Р-64). Хара

### Пустые страницы (`pustye-stranitsy-ru`) — 1

**Контекст** (1)

- [low] `coc:spell:dominate-weakened` Доминация (ослабленная версия) — Вариант «Покорения» из сценария «Пустые страницы» (русский оригинал): книга прямо называет «Доминацию» ослабленной версией одноимённого заклинания. Время сотворения и цена в Рассудке не напечатаны (у 

### Тайник Бутлегеров (`taynik-butlegerov-ru`) — 1

**Контекст** (1)

- [low] `coc:spell:pepelnaya-pechat` Пепельная печать — Новое заклинание сценария «Тайник Бутлегеров» (русский оригинал, английского названия нет; скан без текстового слоя, сверено по изображениям страниц). Книга описывает только действие уже наложенной пе

