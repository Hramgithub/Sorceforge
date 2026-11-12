# «Эликсир жизни» (`eliksir-zhizni-ru`) — сверка переноса (часть elixir)

Источник — официальное русское издание (`[RU 7e]`): игровой сценарий Никиты Борисова, сообщества «Заметки Упыря» и
«Уголок Хранителя» («Elixir of Life» © 2020 Borisov Nikita; дизайн © 2021 Yadrikhinsky Alexander). PDF 12 страниц,
растровый (Microsoft Print to PDF, 300 dpi), без текстового слоя: каждая страница распознана `tesseract -l rus` (200 dpi),
все числа, кубы, адреса и статблоки сверены по вырезкам изображений. Правила — 7-я редакция, `ruleset` core.
Действие — **1930 год**, Салем, Массачусетс (с. 1) — `axes.era` `1930s`; в каталоге владельца сценарий значится как «1920».
Заметки владельца (`3_КБ\Ваншоты\1920 Эликсир жизни\_карточка.md`) описывают другой сюжет (учёный-алхимик, конец XIX
века) — с книгой не совпадают, записи сделаны по книге.

## Страницы

Смещение: **печатная = физическая − 1** (номер внизу страницы: физ. 2 = с. 1 … физ. 11 = с. 10; на физ. 7 номер закрыт
картинкой). Обложки (физ. 1 и 12) без номера — в `sources` `printed_page: null`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Эликсир жизни. Игровой сценарий» | физ. 1 | сценарий `eliksir-zhizni-ru/scenario/eliksir-zhizni` (summary, sources) |
| Вводная: число игроков, время игры, 1930 г., Салем; требования к сыщикам; 1 пистолет и 1 автомобиль; авторы | 1 | сценарий: summary, hook, advice; `…/item/tabelnyy-pistolet-rayta` |
| Предыстория (врезка) | 2 | сценарий: summary; задняя обложка — та же аннотация |
| Зловещая истина | 2–3 | сценарий: keeper_info; `…/character/sivilia`, `…/character/dzhon-foks`, `…/character/nil-foks`, `…/character/odri-rayt`, `…/character/kordeliya-khamfri`; `…/item/eliksir-zhizni`; `…/tome/kniga-zaklinaniy-kulta-salema`, `…/tome/kniga-svyashchennika`; `…/location/muzey-vedm-salema` |
| Газета «The Salem Observer» (иллюстрация) | 2 | раздатка `…/handout/gazeta-salem-observer`; `…/character/breydli-khartsfild` |
| Отчёт Полицейского управления Салема (иллюстрация) | 3 | раздатка `…/handout/otchet-politseyskogo-upravleniya` («Досье»); жертвы `…/character/kassandra-duglas`, `misti-krayton`, `lora-martin`; `…/location/otel-saylent`; `…/organization/politseyskoe-upravlenie-salema` |
| Хронология | 3 | сцены `…/scene/khronologiya-kordeliya`, `khronologiya-napadenie-gonchey`, `khronologiya-begstvo-sivilii`; сценарий: keeper_info, steps; `…/location/dom-mera-khamfri` |
| Кафе «Джулия» (Соут-Салем, Нью-Дерби Стрит, 17) | 3–4 | `…/location/kafe-dzhuliya`; сцена `…/scene/kafe-dzhuliya`; `…/character/devid-rayt`, `nil-uilkins`, `donald-tayler` |
| Больница Салема (Хайленд-Авеню, 81) | 4 | `…/location/bolnitsa-salema`; сцена `…/scene/bolnitsa-salema`; `…/character/teylor-dayson`, `tommi-bennet`; `…/item/rostki-edema` |
| Отдел кадров больницы Салема | 4 | сцена `…/scene/otdel-kadrov` (место — больница) |
| Криминальная лаборатория (Централ-Авеню, 17) | 4 | `…/location/kriminalisticheskaya-laboratoriya`; `…/character/donald-tayler` |
| Проникновение в морг лаборатории | 5 | сцена `…/scene/proniknovenie-v-morg`; `…/character/dzhozef-konnelli` |
| Осмотр тел | 5–6 | сцена `…/scene/osmotr-tel`; раздатка `…/handout/foto-zhertv`; `…/organization/vedmovskoy-kult-salema` (тройная луна) |
| Лес Салема (западнее Соут-Салема) | 6 | `…/location/les-salema`; сцена `…/scene/les-salema`; `…/item/medalon-sobaki`; раздатка `…/handout/foto-medalona` |
| Заброшенный дом (Стейшен-Роуд, 11) | 6 | `…/location/zabroshennyy-dom-lesnichego`; сцена `…/scene/zabroshennyy-dom` |
| Свидетели: Дом Кассандры Дуглас (Грин-Плейс, 2) | 6 | `…/location/dom-kassandry-duglas`; сцена `…/scene/dom-kassandry-duglas`; `…/character/kristofer-duglas` |
| Фрагмент карты города внизу страницы | 6 | карта `…/map/karta-goroda-salem` |
| Бордель «Алые ведьмы» (Дерби Авеню, 23) | 7 | `…/location/bordel-alye-vedmy`; сцена `…/scene/bordel-alye-vedmy`; `…/character/miki`, `rubi-kheys` |
| Дом Мисти Крайтон (Вашингтон-Сквер, 4) | 7 | `…/location/dom-misti-krayton`; сцена `…/scene/dom-misti-krayton`; `…/character/metyu-krayton` |
| Дом Джона Фокса (Эймс-Стрит, 39); 1 этаж | 7 | `…/location/dom-dzhona-foksa`; сцена `…/scene/dom-dzhona-foksa`; `…/item/ruzhyo-dzhona`, `poserebryonnye-kinzhaly`, `banki-s-sushchestvami` |
| Подвал | 8 | сцена `…/scene/podval`; `…/tome/kniga-svyashchennika` |
| Паб «Green Heel» (Лафайет, 139) | 8–9 | `…/location/pab-green-heel`; сцена `…/scene/pab-green-heel`; `…/character/patrik-donovan`; `…/item/kartina-s-kartoy-salema` |
| Картина с картой Салема (иллюстрация) | 8 | карта `…/map/kartina-salema` (`app/maps/elixir-kartina-salema.jpg`, 5 меток) |
| Дом знахарки Сивилии (Уиллсон-Стрит, 6) | 9 | `…/location/dom-znakharki-sivilii`; сцена `…/scene/dom-znakharki-sivilii`; `…/item/dnevnik-sivilii` |
| Перевод ключа, разгадка шифра | 9 | сцена `…/scene/razgadka-shifra`; раздатка `…/handout/klyuch` |
| Ключ (иллюстрация, латынь) | 9 | раздатка `…/handout/klyuch` (текст как напечатан) |
| Кладбище (Чартер-стрит, 51) | 9 | `…/location/kladbishche-na-charter-strit`; сцена `…/scene/kladbishche`; `…/item/eliksir-zhizni` |
| Финал (награды Рассудка) | 9 | сценарий: conclusion |
| Персонажи хранителя: Сивилия | 10 | `…/character/sivilia` (статблок) |
| Персонажи хранителя: Джон Фокс | 10 | `…/character/dzhon-foks` (статблок) |
| Гончая Шаб-Ниггурат | 10 | существо `…/creature/gonchaya-shab-niggurat` (`spawn_of` `coc:creature:shub-niggurath`) |
| Заклинания: Глаз тьмы | 10 | черновик ниже (справочник `kb/spells` общий); механика — в сцене `dom-znakharki-sivilii`, у Сивилии в `statblock.spells` без ссылки |
| Задняя обложка: аннотация, «Специальное издание» | физ. 12 | сценарий: sources |

Записи без своего заголовка: район `…/location/sout-salem` (все адреса книги — «Соут-Салем, …»), `…/character/breydli-khartsfild`
(газета), карта `…/map/karta-goroda-salem` (фрагмент с. 6, полный лист — в комплекте раздаточных материалов).

## Записи (77)

- сценарий 1: `eliksir-zhizni`;
- сцены 19: `kafe-dzhuliya`, `bolnitsa-salema`, `otdel-kadrov`, `proniknovenie-v-morg`, `osmotr-tel`, `les-salema`,
  `zabroshennyy-dom`, `dom-kassandry-duglas`, `bordel-alye-vedmy`, `dom-misti-krayton`, `dom-dzhona-foksa`, `podval`,
  `pab-green-heel`, `dom-znakharki-sivilii`, `razgadka-shifra`, `kladbishche`, `khronologiya-kordeliya`,
  `khronologiya-napadenie-gonchey`, `khronologiya-begstvo-sivilii`;
- места 16: `sout-salem` (район, часть общего `coc:location:salem`), `kafe-dzhuliya`, `bolnitsa-salema`,
  `kriminalisticheskaya-laboratoriya`, `les-salema`, `zabroshennyy-dom-lesnichego`, `dom-kassandry-duglas`,
  `bordel-alye-vedmy`, `otel-saylent`, `dom-misti-krayton`, `dom-dzhona-foksa`, `pab-green-heel`, `dom-znakharki-sivilii`,
  `kladbishche-na-charter-strit`, `muzey-vedm-salema`, `dom-mera-khamfri`;
- карты 2: `kartina-salema` (5 меток), `karta-goroda-salem` (10 меток, одна вычисленная) — картинки
  `app/maps/elixir-kartina-salema.jpg`, `app/maps/elixir-karta-goroda-salem.jpg`;
- персонажи 20: со статблоком `sivilia`, `dzhon-foks`; без статблока `nil-foks`, `devid-rayt`, `odri-rayt`, `nil-uilkins`,
  `donald-tayler`, `teylor-dayson`, `kordeliya-khamfri`, `kassandra-duglas`, `kristofer-duglas`, `misti-krayton`,
  `metyu-krayton`, `lora-martin`, `miki`, `breydli-khartsfild`; с придуманными именами (Р-150) `patrik-donovan` (хозяин
  паба), `dzhozef-konnelli` (дежурный полицейский), `tommi-bennet` (больной подросток), `rubi-kheys` (проститутка);
- существо 1: `gonchaya-shab-niggurat`;
- предметы 9: `eliksir-zhizni`, `rostki-edema`, `poserebryonnye-kinzhaly`, `ruzhyo-dzhona`, `tabelnyy-pistolet-rayta`,
  `medalon-sobaki`, `kartina-s-kartoy-salema`, `dnevnik-sivilii`, `banki-s-sushchestvami`;
- раздатки 5: `gazeta-salem-observer`, `otchet-politseyskogo-upravleniya`, `foto-zhertv`, `foto-medalona`, `klyuch`;
- книги 2: `kniga-zaklinaniy-kulta-salema`, `kniga-svyashchennika`;
- организации 2: `vedmovskoy-kult-salema`, `politseyskoe-upravlenie-salema`.

## Карты

- **Картина с картой Салема** (с. 8): картинка — с листа «Картина» комплекта раздаточных материалов (чище, без
  перспективы), повёрнута. Метки: «Charter St» (рядом нарисовано кладбище), картуш «The Port of SALEM», три ленты со
  слогами шифра. Подписи улиц, «North River», «South River», сетка рамки — не размечены (мест сценария нет).
- **Карта города Салем**: в книге (с. 6) — только декоративный фрагмент; картинка — полный лист из комплекта раздаточных
  материалов (старинная карта атласа с русскими подписями). Номеров мест на ней нет; метки стоят на подписях улиц из
  адресов книги (Нью-Дерби, Централ, Стейшен-роуд, Грин-Плейс, Федерал-стрит, Дерби, Вашингтон-сквер, Лафайет-стрит,
  «Кладб.» у Чартер-стрит) и вычисленная метка леса. Хайленд-авеню, Эймс-стрит, Уиллсон-стрит не найдены. Каждая метка
  проверена по вырезке.

## Опечатки и выводы

- Адрес Кассандры Дуглас: «Грин-Плейс, 2» (с. 6) и «Федерал-стрит, д. 3» (отчёт полиции, с. 3) — errata у места и
  отчёта; в записи — адрес заголовка.
- Адрес Мисти Крайтон: «Вашингтон-Сквер, 4» (с. 7) и «напротив её дома 6 по Вотер-стрит» (отчёт, с. 3) — errata.
- Инспектор «Нил Уилкинс» (текст, с. 3) и «Нил Уилкис» (подпись отчёта) — errata у персонажа и отчёта.
- Статблоки Сивилии и Джона Фокса печатают характеристику «ВОЛ 55», которой нет в 7-й редакции; у Джона нет МОЩ и ПМ
  (флаг `incomplete`). «ВОЛ» в запись не взята — errata.
- Джон Фокс: Скорость 8, по ЛВК 60 и СИЛ 60 > ТЕЛ 55 — 9, возраст не указан — errata, как напечатано.
- Гончая Шаб-Ниггурат: навыки слово в слово повторяют навыки Джона Фокса (Убеждение 50%, Психология 40% у чудовища) —
  вероятно, перенесены по ошибке; errata, как напечатано. Скорости и Уклонения у гончей нет.
- Шанс атаки ножом у Сивилии и Джона не напечатан — «—», в пометке: по навыку Ближний бой (вывод из текста).
- Кубы книги «1D3», «1D4+1», «2/2D6+1» и т. п. записаны строчной d (Р-27).
- Тэйлор / Тейлор Дайсон — два написания имени (с. 4), второе в псевдонимах; «криминальная» и «криминалистическая»
  лаборатория — второе название в псевдонимах.
- Выводы из текста (Р-41): неизвестный труп из леса — Нил Фокс (книга отсылает к нему из отдела кадров); Корделия —
  клиентка Сивилии; Брейдли Хартсфилд из газеты — тот «человек, ограбивший музей», у которого куплены обе книги; банки
  с существами — детёныши тёмной молоди; дежурный полицейский — тот, чей «Слух 40»; Дональд Тайлер — сотрудник полиции;
  разгадка шифра по слогам картины (CAE, MET, ERI, UM).

## Не взято

- Раздаточные картинки как изображения записей (`images`): папка `app/art/` не входит в мою часть — газету, досье,
  фото жертв, фото медальона, ключ и картину можно добавить `pipeline/art/add_images.py` при сведении (оригиналы — книга
  и `1_Библиотека\Сценарии\Эликсир жизни\Раздатка\[RU 7e] Раздатка .pdf`).
- Иллюстрации книги: обложки (физ. 1, 12), морг (с. 5 — использован как «Фото жертв»), табличка «DANGER — Safety first»
  (с. 4), щупальца (с. 7), гончая (с. 10) — без данных или уже описаны.
- Благодарности, ссылки сообществ, патроны, уведомление Chaosium (с. 1) — не данные сценария.
- Мэр Салема Хамфри (отец Корделии) — без имени, только упомянут; остаётся текстом у Корделии.
- Газетные персонажи без роли в сюжете (доктор Уоллес Чайлс, отец Этан Эйдриан, А. Л. Дуглас, Дж. У. Вальтер и др.) —
  только в тексте раздатки; 2-й полицейский участок, местная библиотека, заброшенный причал на Вотер-стрит — упомянуты,
  записей не заведено.
- Три высушенных тела в заброшенном доме — безымянные жертвы гончей, текстом в сцене.

## Вопросы и долг

- **Комплект раздаточных материалов** (`…\Эликсир жизни\Раздатка\[RU 7e] Раздатка .pdf`, 6 листов: досье, фото жертв,
  фото медальона, ключ, газета дважды, картина, карта города) не записан в `pipeline/source/books.json`. По нему взяты
  полный текст газеты и картинки обеих карт; в `sources` стоит книга, в `quality.notes` — пометка. Предлагаю записать его
  (`pages.py register`, например `eliksir-zhizni-razdatka-ru`) и добавить источник.
- **Больница Салема**: `…/location/bolnitsa-salema` и `dveri-vo-tmu-ru/location/genius-salem-hospital` («Салемская
  больница», «Гений места»), возможно, одно здание; книги этого не утверждают. Если владелец решит, что это одно место, —
  перенос в общую запись по Р-154.
- **Район «Соут-Салем»** заведён в папке книги; если другие книги опишут его, его можно сделать общим.
- В газете цены «за фунт» и «80 акров» оставлены как напечатаны в раздатке (Р-138); если Р-64 требует пересчёта и в
  тексте раздаток — поправить.

## Кандидат в новые записи (вне моей части): заклинание «Глаз тьмы»

Черновик для `kb/spells/` (в справочнике нет; источник — с. 10, физ. 11):

- `name`: «Глаз тьмы» (en — нет, русский сценарий); `category`: «Атака» (книга: «эти атакующие чары»); `mechanic`:
  «мгновенное».
- `cost.raw`: «1 рассудка, 4 ПМ» (+ 1 пункт здоровья за порез; + дополнительные пункты Рассудка — длительность).
- Время чтения: 1 раунд.
- Описание: для срабатывания нужна противостоящая проверка МОЩ. Чары ослепляют цель, заполняя её глаза густой чёрной
  жидкостью. После проверки наложения маг делает продольный порез на ладони (трата 1 пункта здоровья) и произносит
  слова заклинания; на месте пореза появляется тёмное око. Все цели, посмотревшие в око, проходят проверку Рассудка;
  при провале слепнут на число раундов, равное числу дополнительно вложенных заклинателем пунктов Рассудка (не более 5).
- Знает: `eliksir-zhizni-ru/character/sivilia`.

## Предложения

`proposals-elixir.json` — 8 предложений к `coc:location:salem`: абзац «Эликсира жизни» в описании, эпоха `1930s`,
4 ссылки для навигации (сценарий, район Соут-Салем, Лес Салема, Музей ведьм), 2 источника. Пробный прогон
`pipeline/integrate/apply.py --dry-run` — ложится.
