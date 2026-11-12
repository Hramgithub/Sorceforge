# «Проклятие Ганеши» (`proklyatie-ganeshi-ru`) — сверка переноса (часть ganesha)

Источник — официальный русский PDF сборника «Монстры Эдны» (`[RU 7e]`), 35 страниц. С. 1–22 и 35 имеют текстовый слой
(прочитан `pages.py show`, числа сверены по изображениям страниц); листы готовых сыщиков (с. 23–34) — изображения без
текста, все числа сняты с изображений 200 dpi по вырезкам. Правила — 7-я редакция, `ruleset` core; книга допускает
адаптацию под Pulp (с. 5), но написана для ядра. Действие — 1920-е годы, юг Индии; `axes.era` — `1920s`.
Заметки владельца (`3_КБ\Ваншоты\1920 Проклятие Ганеши\_паспорт.md`) — пустой паспорт, данных не добавляют.

## Страницы

Смещение **0**: печатная = физической (номера 4–34 стоят внизу страниц). Обложка, титул, содержание (с. 1–3) и задняя
обложка (с. 35) без номеров — в `sources` `printed_page: null`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титул «Монстры Эдны» | 1–2 | сценарий `proklyatie-ganeshi-ru/scenario/proklyatie-ganeshi` (sources) |
| Содержание | 3 | сценарий (sources; «Шагнер Фарн» — в quality.notes) |
| Проклятие Ганеши. Вступление | 4 | сценарий: summary, keeper_info; `coc:location:kandugam` (history) |
| Краткое содержание сценария (1–5) | 4 | сценарий: steps; errata «Х дней» — сцена `…/scene/doroga` |
| Подготовка к игре; Адаптация | 5 | сценарий: advice |
| Сыщики | 5 | сценарий: advice (одно огнестрельное оружие), hook |
| Поселение Кандугам (описание) | 5 | общий город `coc:location:kandugam` (новый, `kb/locations/kandugam.json`) |
| Шагнер Фан | 5–6 | сценарий: keeper_info; общая запись `coc:creature:chaugnar-faugn` (своих чисел нет; источник — предложением) |
| Храм Ганеши (история) | 6 | `…/location/khram-ganeshi` (history); сценарий: keeper_info |
| Университетская библиотека | 6–8 | сцена `…/scene/biblioteka` (место `coc:location:orne-library`) |
| Люциас Пентри | 6 | `…/character/lyutsias-pentri` (background.secret, legend) |
| Чтобы изобразить Стива; Хранителю на заметку: почему он согласился? | 7 | `…/character/stiv-long` (legend, background.secret); сцена `biblioteka` (mechanics) |
| Три книги Стива | 7–8 | предметы `…/item/kniga-puteshestvie-kolumba`, `…/item/kniga-po-petle-vremeni`, `…/item/kniga-dostizhenie-prosvetleniya`; раздатка `…/handout/vypiski-iz-dostizheniya-prosvetleniya` |
| Дорога | 8–10 | сцена `…/scene/doroga`; корабль `…/location/morskoy-ezh`; `…/character/zhan-nyuman` |
| Хранителю на заметку: «Морской ёж»; слухи команды | 9 | `…/location/morskoy-ezh` (description) |
| Хранителю на заметку: что в каюте? | 10 | сцена `doroga` (mechanics); предмет `…/item/statuetka-trekh-khobotov` |
| Поселение Кандугам (глава); Чтобы изобразить Сантосо | 10–11 | сцена `…/scene/pribytie-v-kandugam`; `…/character/santoso-syulan`; `…/location/okrestnosti-kandugama` |
| Хранителю на заметку: великое божество | 11 | сцена `pribytie-v-kandugam` (mechanics); сценарий: advice |
| Встреча с Люциасом; надпись на плитах; Чтобы изобразить Люциаса | 12–13 | сцена `…/scene/vstrecha-s-lyutsiasom`; `…/location/khizhina-lyutsiasa-pentri`; предмет `…/item/reznye-plity`; раздатка `…/handout/nadpis-na-plitakh` |
| Хранителю на заметку: одно существо, два имени | 12 | `coc:location:kandugam` (description); сцена `vstrecha-s-lyutsiasom` |
| Набег аборигенов (итоги 1–3) | 13–14 | сцена `…/scene/nabeg-aborigenov`; `…/character/aborigeny`; `…/character/basappa` (старейшина) |
| Изучение храма; план храма с легендой | 14 | `…/location/khram-ganeshi`; карта `…/map/plan-khrama` (`app/maps/ganesha-plan-khrama.jpg`, 16 меток: 10 номеров + 6 знаков легенды) |
| 1. Вход в храм | 14–15 | `…/location/khram-1-vkhod-v-khram`; сцена `…/scene/vkhod-v-khram` |
| 2. Святилище Ганеши (загадка, надпись) | 15 | `…/location/khram-2-svyatilishche-ganeshi`; сцена `…/scene/zagadka-statui`; раздатка `…/handout/nadpis-na-statue-ganeshi` |
| 3. Спуск в подземелье; Хранителю на заметку: жуткие картинки | 15–16 | `…/location/khram-3-spusk-v-podzemele`; сцена `…/scene/spusk-v-podzemele` |
| 4. Хранилище (свитки, мешки, обереги, предметы; щель) | 16–17 | `…/location/khram-4-khranilishche`; сцена `…/scene/khranilishche` |
| 5. Тоннель с ловушками (дротики, руны, иллюзия); Хранителю на заметку: ограничения | 17–18 | `…/location/khram-5-tonnel-s-lovushkami`; сцена `…/scene/tonnel-s-lovushkami` |
| 6. Алтарная | 18 | `…/location/khram-6-altarnaya`; сцена `…/scene/altarnaya`; предмет `…/item/biven-ganeshi` |
| 7. Спальни | 19 | `…/location/khram-7-spalni`; сцена `…/scene/spalni` |
| 8. Темница | 19 | `…/location/khram-8-temnitsa`; сцена `…/scene/temnitsa` |
| 9. Ритуальная | 19 | `…/location/khram-9-ritualnaya`; сцена `…/scene/ritualnaya` |
| 10. Святилище Шагнер Фана; Развитие событий | 19–20 | `…/location/khram-10-svyatilishche-shagner-fana`; сцена `…/scene/svyatilishche-shagner-fana`; сценарий: conclusion |
| Награды | 20 | сценарий: conclusion (+1d10, +1d6, +1d6, +1d4) |
| Монстры и NPC: Стив Лонг, Люциас Пентри, Сантосо Сюлан | 21 | `…/character/stiv-long`, `…/character/lyutsias-pentri`, `…/character/santoso-syulan` (статблоки) |
| Артефакты: Бивень Ганеши | 22 | `…/item/biven-ganeshi` |
| Лист сыщика Милтон/Мариам Флорес | 23–24 | `…/character/milton-mariam-flores` |
| Лист сыщика Алан/Аллисон Харрис | 25–26 | `…/character/alan-allison-kharris` |
| Лист сыщика Мэттью/Марта Фишер | 27–28 | `…/character/mettyu-marta-fisher` |
| Лист сыщика Рассел/Рози Адамс | 29–30 | `…/character/rassel-rozi-adams` |
| Лист сыщика Шанти/Шакти Маханти | 31–32 | `…/character/shanti-shakti-makhanti` |
| Лист сыщика Коди/Кейра Армстронг | 33–34 | `…/character/kodi-keyra-armstrong` |
| Задняя обложка «Сценарий в Индии» | 35 | сценарий (sources; повтор вступления) |

## Записи (53)

- общий город 1: `coc:location:kandugam` (`kb/locations/kandugam.json`);
- сценарий 1: `proklyatie-ganeshi`;
- сцены 15: `biblioteka`, `doroga`, `pribytie-v-kandugam`, `vstrecha-s-lyutsiasom`, `nabeg-aborigenov`, `vkhod-v-khram`,
  `zagadka-statui`, `spusk-v-podzemele`, `khranilishche`, `tonnel-s-lovushkami`, `altarnaya`, `spalni`, `temnitsa`,
  `ritualnaya`, `svyatilishche-shagner-fana`;
- места 14: `okrestnosti-kandugama`, `khizhina-lyutsiasa-pentri`, `morskoy-ezh` (корабль), `khram-ganeshi`,
  `khram-1-…` … `khram-10-…`;
- карта 1: `plan-khrama`;
- персонажи 12: Хранителя `stiv-long`, `lyutsias-pentri`, `santoso-syulan` (со статблоками), `zhan-nyuman`, `basappa`,
  `aborigeny` (групповой, без статблока); готовые сыщики 6;
- предметы 6: `statuetka-trekh-khobotov`, `biven-ganeshi`, три книги, `reznye-plity`;
- раздатки 3: `vypiski-iz-dostizheniya-prosvetleniya`, `nadpis-na-plitakh`, `nadpis-na-statue-ganeshi`.

Существ своих нет: Шагнер Фан — общая запись `coc:creature:chaugnar-faugn` (книга отсылает к «Книге хранителя»).

## Опечатки и выводы

- «Путь занимает Х дней» (с. 4) — число не проставлено (errata сцены `doroga`).
- Стив Лонг: «двадцати лет» (с. 7) и «21 год» (с. 21); «Внимание» напечатано дважды — 25% и 21% (errata).
- Люциас Пентри: две «Науки (химия,физика,геология и т.п.)» 2% и 1% — шаблонный текст бланка (errata); Скорость 9 без
  возрастной поправки (Р-161).
- Тоннель: проверка Рассудка «2/1к4» — потеря при успехе больше возможной при провале; яду противостоят проверкой ТЕЛ
  (обычно ВЫН) — обе как напечатаны, errata сцены.
- Мэттью/Марта Фишер: урон «Ли-Энфилда» «2d6+БкУ» (в «Книге хранителя» 2d6+4) — errata, предложен `source_variants`.
- Коди/Кейра Армстронг: «Уклонение» и значение родного языка на листе пустые — поставлены 25 (½ ЛВК) и 40 (ОБР),
  вывод из текста (Р-41), `corrections` + errata `fixed: true`.
- Удача не отмечена ни на одном листе — `luck` «—». Проценты атаки «Без оружия» на листах не заполнены — «—».
- Содержание (с. 3): «Шагнер Фарн»; в тексте «Шагнер Фан», в падежах «Шагнер Фану» — пометка в сценарии.
- Футы и ярды → метры (Р-64): тоннель 100 футов → 30 м, 10 футов → 3 м; дальности 110 и 15 ярдов → 110 и 15 м.
- Аборигены: книга отсылает за профилем к «Книге хранителя», не называя его; ближайший — чо-чо (вывод, связь не
  поставлена, пометка в записи). Имя старейшины («Басаппа») и имена аборигенов придуманы (Р-150, Р-151).
- Кандугам заведён общим городом в `kb/locations/` (Р-190): других частей в этом поселении нет.

## Не взято

- Иллюстрации (Сантосо, с. 12; аборигены, с. 19; бивень, с. 22 и др.) и силуэты на листах — `app/art/` не моя часть;
  можно добавить `pipeline/art/add_images.py` при сведении.
- Пустые поля листов (описание, травмы, фобии, книги, встречи, «Знакомые сыщики», «Памятка по правилам») — без данных.
- Пирс, Университетский музей отдельными записями не заведены: пирс — в «Окрестностях Кандугама», музей — ссылка на
  `chernovodnyy-ruchey-ru/location/dues-muzey-miskatonikskogo-universiteta`.
- Выдуманная организация «В недрах», газета Boston American, Храм Чаттешвара и Храм Мул Шанкарешвара (прототипы) —
  текстом, без записей.
- Команда «Морского ежа» — без записи (моряки не названы).
- Двери на плане храма меток не получили.

## Предложения

`proposals-ganesha.json` — 19 правок, пробный прогон `apply.py --dry-run` проходит: «Ли-Энфилд» (`source_variants`,
псевдоним «.303 Ли-Энфилд»); источник для `coc:creature:chaugnar-faugn`; ОИН (описание, источник, ссылка); библиотека
Орна и Мискатоникский университет (абзац описания, источник, ссылки); Аркхэм (ссылка на сценарий).
