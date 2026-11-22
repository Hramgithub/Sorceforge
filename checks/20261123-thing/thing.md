# Thing Torments Poet, Daimyo Calls on Greatest Help, Will the Players Fail? — сверка переноса (2026-11-23)

Книга `thing-torments-poet-en` (Steven Goodison, фанатский сценарий, ©2020; эпоха Эдо, Ямагути, 1679). PDF без текстового
слоя: текст — распознавание (`.cache/ocr/thing-torments-poet-en`), каждая страница прочитана и по изображению; числа и имена —
с изображений. Русского перевода в базе и в библиотеке нет (поиск по `kb/books/*-ru/`: Yamaguchi/Ямагути, Idaina, Kekkan — пусто).

**Страницы.** 32 физические страницы. Печатные номера есть на физ. 4–32 («1»…«29»): **печатная = физическая − 3**
(смещение для `books.json`: −3; физ. 1–3 — обложка, внутренняя обложка, выходные данные — без номеров, в `sources` `printed_page: null`).

Все id ниже — `thing-torments-poet-en/<kind>/<slug>`; сокращённо `<kind>/<slug>`.

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Thing Tormens Poet Daimyo Calls on Greatest Help Will the Players Fail?» | физ. 1 | `scenario/thing-torments-poet` (источник, errata названия); картинка — atmosphere.json |
| Внутренняя обложка «The first chapter in a five part Edo Japan campign…» | физ. 2 | `scenario/thing-torments-poet` (summary); atmosphere.json |
| Special thanks and copyright | физ. 3 | `scenario/thing-torments-poet` (источник; автор, ©2020, «The King in Yellow» Чемберса) |
| Thing Torments Poet Daimyo Calls for Greatest Help Will the Players Fail? (титул, эпиграф Масаоки Сики) | 1 | `scenario/thing-torments-poet` (summary) |
| Keeper information | 1 | `scenario/thing-torments-poet` (keeper_info); `character/idaina-shinjin`; `item/countdown-rash` |
| Investigator information | 1 | `scenario/thing-torments-poet` (hook); `handout/daimyo-letter` |
| The elder things in Japan and the defective elder thing (+ врезка кандзи цифр) | 1 | `creature/yamaguchi-elder-things`, `creature/sis-or-ec-a-kan`, `creature/kekkan-noaru-tan-bo`; кандзи — keeper_info и `item/countdown-rash` |
| Idaina Shinjin’s encounter with the defective Elder Thing and the conflict with the Yamaguchi Elder Things | 2 | `scenario` (keeper_info); `character/idaina-shinjin`; `creature/kekkan-noaru-tan-bo` |
| Yamaguchi city | 2 | `location/yamaguchi` |
| Врезка об оружии (только самураи) | 2 | `scenario` (advice) |
| Rurikoji Temple and meeting with the Daimyo | 2–3 | `scene/rurikoji-meeting`; `location/rurikoji-temple`; `character/yamaguchi-hogo`, `kuroi-rohu`, `yubi-hira`; `item/letter-of-entry`, `item/kuroi-dagger` |
| The Black Duck Kabuki house | 3 | `scene/black-duck-arrival`; `location/black-duck-kabuki-house`, `location/entertainment-district`; `organization/black-duck-troupe`; `item/the-play` |
| Backstage of the Kabuki house and the basement (+ врезка о мужчинах в кабуки) | 4 | `scene/backstage-basement`; `location/black-duck-backstage`, `location/black-duck-basement`; `item/benzaiten-statue`; врезка — `scenario` (advice), `character/kabuki-actors` |
| Idaina Shijin and his room | 4 | `scene/idaina-room`; `location/idaina-room`; `item/idaina-flowers`, `item/countdown-rash` |
| The boss and his office | 5 | `scene/boss-office`; `location/geijutsu-office`; `character/geijutsu-teki`; `handout/insurance-scam-note` |
| The mysterious play | 5 | `scene/mysterious-play`; `item/the-play` |
| The Betorozu betting house and stag beetle wrestling | 6 | `scene/betting-house`; `location/betorozu-betting-house`; `creature/stag-beetles` |
| Confronting Kandaina Te and his office | 6 | `scene/kandaina-office`; `character/kandaina-te` |
| Yamaguchi library | 6 | `scene/library`; `location/tenjin-shrine-library`; `character/monks` |
| Yamaguchi cemetery and the ‘Mononoke’ | 6 | `scene/cemetery`; `location/yamaguchi-cemetery`; `character/donyokuna-te` |
| The Butcher shop | 7 | `scene/butcher-shop`; `location/butcher-shop`, `location/cow-pen`; `character/butcher` |
| The Shikigami visit (+ врезка о сикигами) | 7 | `scene/shikigami-visit`; `creature/shikigami`; `handout/shikigami`; врезка — `scenario` (advice) |
| Assault on Kuroi’s house (During) | 8 | `scene/kuroi-assault-during`; `location/kuroi-house`; `creature/pseudo-thing` |
| Assault of Kuroi’s house (After) | 8 | `scene/kuroi-assault-after` |
| Kuroi’s House and if Kuroi lives | 8 | `scene/kuroi-house-lives`; `handout/kuroi-research-notes` |
| Mount Shojidake and the shrine | 9 | `scene/shojidake-shrine`; `location/mount-shojidake`, `location/shojidake-shrine` |
| The butcher shop day 2 | 9 | `scene/butcher-day-2`; `location/butcher-storage` |
| Otodoiyama forest | 9 | `scene/otodoiyama-forest`; `location/otodoiyama-forest`, `location/forest-shrine` |
| Mount Otodoiyama and the defective Elder Things lair | 9 | `scene/monastery-lair`; `location/mount-otodoiyama`, `abandoned-village`, `ruined-monastery`, `monastery-fountain`, `zen-garden` |
| Confronting the Defective Elder Thing | 10 | `scene/confronting-kekkan` |
| The defective Elder Thing is violently killed | 10 | `scene/ending-killed` |
| The defective Elder Thing Sacrifices himself | 11 | `scene/ending-sacrifice` |
| The defective Elder Thing is not killed and Idaina Shinjin’s death | 11 | `scene/ending-idaina-death`; `location/fushino-river` |
| Idaina Shinjin is cured by the Onmyojis spell | 11 | `scene/ending-cured` |
| Conclusion | 11 | `scenario` (conclusion) |
| Rewards | 11 | `scenario` (conclusion, награды); сцены исходов (mechanics) |
| Appendix A: Charatcers, NPC’s and Montsers — Yamaguchi Hogo; Kuroi Rohu; Yubi Hira | 12 | `character/yamaguchi-hogo`, `kuroi-rohu`, `yubi-hira` |
| — Idaina Shinjin; Gaijutsu Teki; Butcher; Kandaina Te | 13 | `character/idaina-shinjin`, `geijutsu-teki`, `butcher`, `kandaina-te` |
| — Donyakuna Te; Samurai guard; Kabuki actor; Black Duck Kabuki house worker; Resident of Yamaguchi city | 14 | `character/donyokuna-te`, `samurai-guards`, `kabuki-actors`, `black-duck-workers`, `yamaguchi-residents` |
| — Monk; Elder Thing; Defective Elder Thing, Kekkan’noaru Tan Bo; Psuedo-Thing | 15 | `character/monks`; `creature/yamaguchi-elder-things`, `kekkan-noaru-tan-bo`, `pseudo-thing` |
| Рисунок Бракованного Старца (без подписи) | 16 | картинка `creature/kekkan-noaru-tan-bo` |
| Appendix B: Stag Beetles (Rodrigez, BooBoo, Tsuyoi, Yakunitatanai) | 17 | `creature/stag-beetles` (варианты) |
| Appendix C: Spells — Bind shikigami; Sever psychic hold; Contact/Dispel spirit | 17 | таблица «Приложение C: заклинания» в `scenario`; черновики общих записей — `checks/20261123-thing/spells/` |
| Appendix D: Maps — Yamaguchi city; Butchers shop day 1; Butchers shop day 2 | 18 | `map/yamaguchi-city`, `map/butcher-day-1`, `map/butcher-day-2` |
| Black duck kabuki house- Floor 1; Black duck basement | 19 | `map/black-duck-floor-1`, `map/black-duck-basement` (+ `location/black-duck-foyer`, `black-duck-stage`) |
| Black duck kabuki house- floor 2; Kuroi Rohus house | 20 | `map/black-duck-floor-2` (+ `location/black-duck-lobby`), `map/kuroi-house` |
| Otodoiyama forest; The monastery | 21 | `map/otodoiyama-forest`, `map/monastery` |
| Appendix D: Handouts — Daimyo letter | 22 | `handout/daimyo-letter` |
| Newspaper poet day 1; Newspaper stolen cows day 1 | 23 | `handout/newspaper-poet-day-1`, `handout/newspaper-stolen-cows-day-1` |
| Insurance scam note; Flying bear story | 24 | `handout/insurance-scam-note`, `handout/flying-bear-story` (+ `character/yamaguchi-hogokuchi`) |
| Dispel spirit spell; Obituary; Kurois research notes | 25 | `handout/dispel-spirit-spell`, `handout/obituary-donyokuna-te`, `handout/kuroi-research-notes` |
| Shikigami; Shikigam- Japanese | 26 | `handout/shikigami` (две картинки) |
| Newspaper dead onmyoji day 2; Newsppaer dead butcher day 2 | 27 | `handout/newspaper-dead-onmyoji-day-2`, `handout/newspaper-dead-butcher-day-2` |
| Newspaper Idaina Shinjin changed forever / is cured / is killed | 28 | `handout/newspaper-idaina-changed-forever`, `newspaper-idaina-cured`, `newspaper-idaina-killed` |
| The adventure continues on Tanegashima island — The Kofun closes to the west — Coming soon… | 29 | `scenario` (summary, conclusion); картинка — atmosphere.json |

Сводные записи без своего заголовка: `organization/daimyo-court`, `location/elder-things-base`.

## Не взято

- Иллюстрации-атмосфера (гравюры и фотографии без подписей, физ. 1, 2, 5–14, 32) — в `atmosphere.json` (ведущий сливает).
- Гора Камэяма (упомянута один раз в «Yamaguchi city», без сюжета) и город Хофу — только текстом в `location/yamaguchi`.
- «Записка» в столе Гэйдзюцу (с. 5: «a successful library use roll will get the Investigator a note») — книга не говорит, что в ней; осталась текстом в сцене и месте.
- Комната драматурга после пьесы (пуста, окно открыто) — без записи, текстом в `scene/mysterious-play`.
- Три новых заклинания — не в `kb/spells` (общий справочник), а черновиками `checks/20261123-thing/spells/*.json` (схема проверена `tools/validate.py`); после их добавления ведущему стоит поставить ссылки `spell` в `character/kuroi-rohu` (statblock.spells.items: «Bind Shikigami», «Contact spirit», «Sever psychic hold*»).

## Опечатки и сомнения книги

- Имена: «Idaina Shijin / Sinjin / Shinin / Taina» при «Shinjin»; «Kuroi Robu», «Kurioi» при «Rohu»; «Gaijutsu» при «Geijutsu»; «Donyakuna» при «Donyokuna»; «Kekkan’Noaru Ten Bo» при «Tan Bo»; «Betoruzu / Betoruzo» при «Betorozu»; «Otodoyama», «Ototloiyama», «Onijkuma», «Mount Gtodainna» (последние — ошибки распознавания/печати, в записях не повторены); «Psuedo-Thing», «Sepuku», «Japanse», «Natural word», «Masaoaka Shiki», «Sorage area», «Abanonded village», «Monastary», «Dead bucther», «Newsppaer»; «Charatcers… Montsers»; «Tormens» / «Calls on» / «Calls for» в названии.
- Страховой полис: 10 000 иен в тексте (с. 5), 3000 иен на раздатке (с. 24) — `handout/insurance-scam-note` errata.
- Раздатка «Newspaper Idaina Shinjin is cured» повторяет текст «changed forever» (об обездвиженном поэте) — errata.
- Бракованный Старец: потеря Рассудка 1d6 в тексте (с. 9) и 1d6+2 в профиле (с. 15); Скорость 9/8 (на земле быстрее, чем в полёте); БкУ +1d6 при СИЛ 179 + ТЕЛ 150; «Fighting 30% (10/4)», «Dodge 20% (25/11)» — доли исправлены по Р-35/Р-77 (`percent_parts.py`).
- Псевдостарец: «Spin attack 40% (20/100)» — доли исправлены (Р-35).
- Жуки-олени: доли процентов не сходятся (Бубу, Цуёи, Родригес) — исправлены (Р-35).
- Производные значения почти всех профилей (ПЗ, ПМ, БкУ, Комплекция, Скорость, Уклонение ниже ЛВК/2) не по правилам 7e — errata, как напечатано (Р-161).
- Идайна: «Jump 60» без %, «Natural world» без значения; Хого: «Drink Sake» без значения; Донёкуна: атака «Brawl 55%» при «Cannot physically attack».
- Донёкуна: увидеть его можно, только «провалив» проверку МОЩ — как напечатано.
- Проекция Старца «will have idea where to find the defective Elder Thing» — вероятно, пропущено «no»; как напечатано.
- Кабинет Гэйдзюцу — «единственная комната третьего этажа» в тексте, но нарисован на плане второго этажа.
- Иены в 1679 году не было (анахронизм книги).
- Святилище Тэндзина = «Yamaguchi library monastery / central library and monastery» — вывод из текста; какие «три раздатки библиотеки» — вывод (летающий медведь, заклинание изгнания духа, некролог).

## Термины (English → русский), выбранные для книги

| English | Русский |
|---|---|
| Elder Thing / Elder Things | Старец / Старцы (по общей записи `coc:creature:elder-thing`) |
| Yamaguchi Elder Things | Старцы Ямагути |
| Defective Elder Thing | Бракованный Старец |
| Kekkan’noaru Tan Bo | Кэккан-ноару Тан Бо |
| Sis-or-ec-a-kan | Сис-ор-эк-а-кан |
| Pseudo-Thing (Psuedo-Thing) | псевдостарец |
| Daimyo | даймё |
| Onmyoji | онмёдзи |
| Shikigami | сикигами |
| Yokai | ёкай |
| Mononoke | мононокэ |
| Onikuma | оникума |
| Kami | ками |
| Kabuki / Kabuki house | кабуки / театр кабуки |
| Haiku | хайку |
| Kanji | кандзи |
| Gaijin | гайдзин («Странное представление гайдзинов») |
| Samurai | самурай |
| Sepuku (Seppuku) | сэппуку |
| Sake | сакэ |
| Yen | иена |
| Edo period | эпоха Эдо |
| Zen garden | сад камней |
| Benzaiten | Бэндзайтэн |
| Tenjin | Тэндзин |
| countdown rash | сыпь обратного отсчёта |
| letter of entry | пропускное письмо даймё |
| Black Duck Kabuki house | театр кабуки «Чёрная утка» |
| Betorozu betting house | игорный дом «Беторозу» |
| stag beetle wrestling | бои жуков-оленей |
| Yamaguchi / Yamaguchi Hogo / Hogokuchi | Ямагути / Ямагути Хого / Ямагути Хогокути |
| Idaina Shinjin | Идайна Синдзин |
| Kuroi Rohu | Курои Роху |
| Yubi Hira | Юби Хира |
| Geijutsu Teki | Гэйдзюцу Тэки |
| Kandaina Te / Donyokuna Te | Кандайна Тэ / Донёкуна Тэ |
| Rurikoji temple | храм Рурикодзи |
| Mount Shojidake / Mount Otodoiyama / Otodoiyama forest | гора Сёдзидакэ / гора Отодоияма / лес Отодоияма |
| Mount Kameyama, Hofu, Fushino river, Tanegashima | гора Камэяма, Хофу, река Фусино, Танэгасима |
| Bind shikigami | Связать сикигами |
| Sever psychic hold | Разорвать психическую хватку |
| Contact/Dispel spirit | Призвать/изгнать духа |
| Himawari ni mi o tsutsunda yōroppa no jōgi | «Химавари ни ми о цуцунда ёроппа но дзёги» (название пьесы не переводится) |
| The Kofun closes to the west | (название второй главы; не переводилось) |

Японские слова — по системе Поливанова; романдзи книги — в `name.en`.
