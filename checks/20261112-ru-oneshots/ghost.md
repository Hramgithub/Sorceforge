# «Призрак» (prizrak-ru) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] Призрак.pdf`, 17 страниц; номеров страниц нет — печатная страница = физической (смещение 0).
Текстовый слой надёжен (PDF с текстом, картинок нет); статблоки и числа сверены по изображениям страниц 1, 5–8, 13–17.
Карт, иллюстраций и раздаток-картинок в книге нет. Действие — Бостон, октябрь 1920 года (эпоха 1920-е).

**Редакция правил.** Книга помечена «7e», но механика — прежних редакций: характеристики 3–18, Идея и Знание, броски
«ЛВК ×4» / «ЛВК ×7», Таблица сопротивления, ранги ЛВК, старые названия навыков («Болтовня», «Кредит», «Заметка»,
«Использование библиотеки», «Ремонт электроники») и сокращения (ТЛЗ = ВЫН, РЗМ = ТЕЛ, ВЛВ = МОЩ, ВПД = НАР, РСД, ОЗ).
По Р-221 статблоков нет: характеристики Корбитта и Межпространственного бродяги даны текстом в `description`
(«Характеристики (старая редакция, как напечатаны): …»), механика — в `abilities`; у существ сохранён `instance_of`
(для игры по 7e — статблок вида). `ruleset` — `core`; в тексте записей навыки названы по-новому с книжным названием в скобках.

**Связь с «The Haunting».** По сюжету это старая версия сценария Chaosium «The Haunting» (книга оригинал не называет).
В русской «Книге хранителя» его нет (заменён «Среди древних деревьев»), в английской 7e он — только пример в правилах;
записей «Дома с привидениями» / The Haunting в базе нет, связывать `same_as`/`related_to` не с чем. Связаны три правила,
где английское издание упоминает The Haunting: `coc:rule:anatomy-of-a-linear-scenario`, `coc:rule:ending-a-story`,
`coc:rule:new-keepers` — `refs` сценария и предложения обратных `refs`.

Префикс записей книги: `prizrak-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| «Зов Ктулху. Призрак» (заголовок) | 1 | `scenario/prizrak` |
| Вступление (воскресенье, 17 октября 1920 года) | 1 | `scene/priglashenie`; `scenario/prizrak` (hook) |
| Резиденция Уилларда и Марджори Браун-Росс | 1–2 | `scene/vstrecha-s-braunom`; `location/dom-brauna-rossa`; `character/uillard-braun`, `character/mardzhori-ross-braun`; `item/konvert-brauna`; `character/vittorio-makarios`, `gabriella-makarios`, `pedro-makarios`, `alessandro-makarios`, `rozalina` |
| Гостиница «Копли-сквер» | 2 | `location/gostinitsa-kopli-skver`; `scene/vstrecha-s-braunom` |
| Роксберийский санаторий | 2–3 | `scene/roksberiyskiy-sanatoriy`; `location/roksberiyskiy-sanatoriy`; `character/kharriet-menning`, `uolles-robertson`, `vittorio-makarios`, `gabriella-makarios` |
| Boston Globe (Морг, вырезки) | 3–4 | `scene/boston-globe`; `location/redaktsiya-boston-globe`; `character/administrator-boston-globe`, `elizabet-kheys`; `handout/vyrezki-boston-globe` |
| Бостонская публичная библиотека | 4 | `scene/publichnaya-biblioteka`; `location/bostonskaya-publichnaya-biblioteka`; `character/bibliotekar`, `genri-uebber`; `handout/stati-iz-biblioteki` |
| Архив | 5 | `scene/arkhiv`; `location/arkhiv`; `character/klerk-arkhiva`, `maykl-tomas`; `organization/tserkov-gospoda-daruyushchego-tayny` |
| Высшие суды; Центральный полицейский участок (рейд 7 мая 1912 года) | 5 | `scene/sudy-i-politsiya`; `location/vysshie-sudy`, `location/tsentralnyy-politseyskiy-uchastok`; `organization/tserkov-gospoda-daruyushchego-tayny` |
| Часовня созерцания и церковь Господа нашего, Дарующего тайны | 6 | `scene/ruiny-chasovni`, `scene/podval-chasovni`; `location/ruiny-chasovni-sozertsaniya`, `location/podval-chasovni`; `tome/latinskiy-foliant`; `item/trapetsoedr`, `item/rzhavyy-klyuch` |
| В дневнике Майкла Томаса написано | 7–8 | `handout/dnevnik-maykla-tomasa`; `character/maykl-tomas`, `deniel-ellsvort` |
| Клетка с детскими скелетами (без заголовка) | 8 | `scene/podval-chasovni`; `location/podval-chasovni` |
| Дом на ул. Шиф, 20 (снаружи, сарай) | 8 | `scene/dom-snaruzhi`; `location/dom-shif-20`, `location/dom-shif-20-saray`; `item/instrumenty-iz-saraya` |
| Первый этаж | 8 | `location/dom-shif-20-pervyy-etazh`; `scene/pervyy-etazh` |
| Первый этаж: Комната 1 | 8 | `location/dom-shif-20-kladovaya`; `item/pyat-klyuchey` |
| Первый этаж: Комната 2 | 8 | `location/dom-shif-20-kladovaya-produktov` |
| Первый этаж: Комната 3 | 9 | `location/dom-shif-20-prikhozhaya` |
| Первый этаж: Комната 4 (события) | 9 | `location/dom-shif-20-gostinaya` (таблица «События в гостиной») |
| Первый этаж: Комната 5 | 9 | `location/dom-shif-20-stolovaya` |
| Первый этаж: Комната 6 | 9 | `location/dom-shif-20-kukhnya` |
| Верхний этаж | 9 | `location/dom-shif-20-verkhniy-etazh`; `scene/verkhniy-etazh` |
| Верхний этаж: Комната 1 | 9 | `location/dom-shif-20-glavnaya-spalnya` |
| Верхний этаж: Комната 2 | 9 | `location/dom-shif-20-detskaya` |
| Верхний этаж: Комната 3 (события) | 10 | `location/dom-shif-20-zapertaya-komnata` (таблица «События в запертой комнате») |
| Верхний этаж: Комната 4 | 10 | `location/dom-shif-20-vannaya` |
| Чердак (события) | 10 | `location/dom-shif-20-cherdak` (таблица «События на чердаке»); `scene/cherdak`; `tome/dnevniki-korbitta` |
| Дневники Корбитта гласят: Первый дневник | 10–12 | `handout/dnevniki-korbitta`; `character/uolter-korbitt` (legend), `ameli-khuper`, `bendzhamin-khuper` |
| Второй дневник | 12 | `handout/dnevniki-korbitta`; `character/genri-uebber`, `deniel-ellsvort`, `piter-ellsvort` |
| Третий дневник | 12–13 | `handout/dnevniki-korbitta`; `character/maykl-tomas` |
| Заклинание «Призыв слуги из Пустоты» (без заголовка) | 13 | `tome/dnevniki-korbitta` (description, spells); `scene/cherdak` |
| Подвал | 13 | `location/dom-shif-20-podval`; `scene/podval-sklad` |
| Подвал: Комната 1 (кинжал) | 13–14 | `location/dom-shif-20-sklad`; `item/serebryanyy-kinzhal`; `character/uolter-korbitt` (способность «Парящий кинжал») |
| Подвал: Комната 2 | 14 | `location/dom-shif-20-ugolnyy-otsek` |
| Подвал: Комната 3 | 14 | `location/dom-shif-20-podpol`; `scene/podpol` |
| Стая крыс, Rattus Norvegicus | 14 | `creature/krysinye-stai` (instance_of `coc:creature:rat-swarm`) |
| Подвал: Комната 4 | 15 | `location/dom-shif-20-taynaya-komnata`; `scene/taynaya-komnata`; `item/chernyy-kamen`, `item/goroskop` |
| Характеристики Шамблера Измерений | 15 | `creature/mezhprostranstvennyy-brodyaga` (description — текстом как напечатаны, Р-221; instance_of `coc:creature:dimensional-shambler`) |
| Заклинания Корбитта («Господство», «Плотяная защита», движение) | 16 | `character/uolter-korbitt` (abilities, spells) |
| Характеристики Корбитта | 16 | `character/uolter-korbitt` (description — текстом как напечатаны, Р-221; abilities) |
| Сыщики победили! | 17 | `scene/pobeda`; `scenario/prizrak` (conclusion, таблица наград) |
| Мистическое ожерелье | 17 | `item/chernyy-kamen`; `scene/pobeda` |
| Заключение | 17 | `scene/zaklyuchenie`; `scenario/prizrak` (conclusion); `character/piter-ellsvort` |

Город: общий `coc:location:boston` (уже есть) — дополнение предложениями; все места сценария — записи книги с `part_of`
на Бостон. Районы (Бэк-Бэй, Роксбери, Уэст-Роксбери) своих записей не имеют — названы в `address`.

## Не взято

- Картинок, карт и раздаток-картинок в книге нет; `app/maps/ghost-*` не создавались.
- Безымянные люди без своей роли в игре — текстом в записях: семьи-жильцы 1868, 1880 (французские иммигранты), 1909/1914,
  1917 годов (в `history` дома); сын Майкла Томаса (род. 17 марта 1879 года, в дневнике и записи Томаса); очевидцы 1919 года;
  коронер; «влиятельный местный чиновник» 1912 года; 54 арестованных и 17 погибших культистов, 3 погибших полицейских
  (в организации); студенты Бостонского университета в библиотеке; «коллеги»-члены общества 1819 года; скелет-охранник
  в мантии (в месте и сцене подвала часовни).
- Вещи без механики — текстом в сценах: серебряный портсигар Брауна, заржавевший дробовик у скелета («бесполезный»),
  молоток, гвозди, скотч и клей в кладовой, предметы обстановки комнат.
- Статблоки 7e не составлялись (Р-221): характеристики, навыки (в т. ч. «Спрятать», «Лежать неподвижно», «Вводить
  в заблуждение»), Идея и Знание — текстом в описаниях Корбитта и бродяги.

## Опечатки и сомнения (errata в записях)

- Дата встречи: назначена на воскресенье, 24 октября, 13:00 (с. 1), раздел датирован «Четверг, 21 октября 1920 года»
  (`scene/vstrecha-s-braunom`, `scenario/prizrak`).
- «€24 в неделю» в гостинице 1920 года (вероятно, $24) (`location/gostinitsa-kopli-skver`).
- Доктор Робертсон: семья «въехала в 1914 году», по вырезкам — въехала в 1909-м, трагедия в 1914-м
  (`character/uolles-robertson`, `scenario/prizrak`).
- Бродяга: «Идея 45» при ИНТ 07 (по правилам — 35) (`creature/mezhprostranstvennyy-brodyaga`).
- Дневники Корбитта: «ВЛВ» на месте «могущества» и «министр» на месте «священника» — следы перевода (`handout/dnevniki-korbitta`).
- Без errata, пометками: «Часовня ТЛЗ» в записях о рейде (с. 5) — сбой перевода; фамилия «Браун-Росс» / «Росс-Браун»;
  «Макариос» / «Макарио»; расстояния «от здания суда» (неясно, какого).

## Выводы из текста (Р-41)

- «Господь Дарующий тайны» / «Тёмный человек», призванный через Трапецоэдр, — Скиталец тьмы (латинский том: Обитатель
  Тьмы, пробуждаемый взглядом в Сияющий Трапецоэдр): связь `servitor_of` у Корбитта и `refs` у культа помечены как вывод.
- Проявления в доме вызывает Корбитт; латинский фолиант, возможно, — том, найденный Корбиттом в 1818 году; смена почерка
  в дневнике Томаса с 1900 года — возможно, сын; обведённая дата 15 июня 1912 года — срок второй части ритуала.
- Придуманы имена (Р-150): администратор «Boston Globe» — Джозеф Салливан, библиотекарь — Агнес Доэрти, клерк Архива —
  Фрэнсис Дойл (`editorial_text`).

## Предложения

`proposals-ghost.json` — 17 правок, пробный прогон `apply.py --dry-run` — все ложатся: Бостон (абзац описания, 3 ссылки,
источник); `refs` на сценарий в трёх правилах, упоминающих The Haunting; псевдонимы «Межпространственный бродяга», «Шамблер Измерений» (`coc:creature:dimensional-shambler`),
«Обитатель Тьмы» (`coc:creature:haunter-of-the-dark`), «Господство», «Повинуйся воле хозяина», «Повиноваться воле
господина» (`coc:spell:dominate`), «Плотяная защита», «Rigor Vitae» (`coc:spell:flesh-ward`), «Призыв слуги из Пустоты»
(`coc:spell:summon-bind-dimensional-shambler`).

## Вопросы владельцу

- Книга с меткой «[RU 7e]» написана по правилам прежних редакций: характеристики — текстом (Р-221), `ruleset: core`;
  нужны ли пересчитанные в 7e статблоки Корбитта и бродяги?
