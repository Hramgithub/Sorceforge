# «Туманы острова Сан-Кристобаль» (`tumany-san-kristobal-ru`) — сверка переноса (часть fogs)

Источник — русский оригинал авторов (Ярослав Федосов, Кристиана Денисенко; конкурс «НРИ-Кашевар», лето 2024), PDF
24 страницы с текстовым слоем; раздатки (физ. с. 16–18) и листы сыщиков (физ. с. 19–24, без текстового слоя) прочитаны
по изображениям страниц (`pages.py image`, 100–200 dpi). Правила — 7-я редакция («Книга хранителя» пер. «Мира Хобби»),
`ruleset` core; действие — ноябрь 1912 года, `axes.era` — `other`.

## Страницы

Смещение `tumany-san-kristobal-ru`: **печатная = физическая − 1** (номер внизу страницы: физ. 4 = с. 3 … физ. 15 = с. 14).
Обложка (физ. 1), выходные данные (физ. 2), содержание (физ. 3), раздатки (физ. 16–18) и листы сыщиков (физ. 19–24) без
номеров — у них в `sources` `printed_page: null`. Ниже — печатные страницы, для страниц без номера — «физ.».

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Туманы острова Сан-Кристобаль», «НРИ-Кашевар, лето 2024 г.» | физ. 1 | сценарий `tumany-san-kristobal-ru/scenario/tumany-ostrova-san-kristobal` (summary, sources) |
| Выходные данные, аннотация, «От авторов», тема и ключевые слова конкурса | физ. 2 | сценарий: summary, advice («От авторов»); `…/location/ostrov-san-kristobal` |
| Содержание | физ. 3 | сценарий: sources (только список разделов) |
| Посвящение Роберту Б. Уайди; эпиграф (Джек Лондон, «Страшные Соломоновы острова») | 3 | сценарий: summary (упоминание; текст эпиграфа — см. «Не взято») |
| Введение | 3 | сценарий: summary, hook; сцена `…/scene/dikiy-plyazh` |
| Предыстория (с правилами на столпах) | 4 | сценарий: keeper_info; `…/location/ostrov-san-kristobal` (history); раздатка `…/handout/svod-zakonov-ostrova`; `…/creature/ngorieru`, `…/creature/adaro` (legend) |
| Персонажи | 5 | сценарий: keeper_info; персонажи `…/character/adam-terner`, `endi-terner`, `yudzhin-khopkins`, `khyu-marlou`, `nomoa`, `uilyam-bleyk`; существа `…/creature/kakamora`, `adaro`, `ngorieru` |
| Хранителю на заметку: опасности адаро (врезка) | 5 | `…/creature/adaro` (description, abilities); сценарий: keeper_info |
| Ход событий: 15 ноября 1912 года; Первая ночь | 5 | сценарий: tables «Ход событий»; сцены `…/scene/dikiy-plyazh`, `…/scene/pervaya-noch` |
| Ход событий: Вторая, Третья, Четвёртая ночь; Судная ночь; события по ночам | 6 | сценарий: tables «Ход событий»; сцены `…/scene/vtoraya-noch`, `…/scene/tretya-noch`, `…/scene/chetvertaya-noch` |
| Мотивы: первый, второй мотив | 6 | сценарий: hook; сцена `…/scene/dom-dzhina` |
| Мотивы: третий мотив | 7 | сценарий: hook; `…/character/yudzhin-khopkins` |
| Локации (не больше двух за день) | 7 | `…/location/ostrov-san-kristobal`; сцена `…/scene/dom-dzhina` (исход) |
| Дикий пляж | 7 | `…/location/dikiy-plyazh`; сцена `…/scene/dikiy-plyazh` |
| Британское поселение | 7 | `…/location/britanskoe-poselenie`, `…/location/dom-adama`, `…/location/tserkov`; сцена `…/scene/britanskoe-poselenie`; предмет `…/item/ritualnyy-kinzhal` |
| Деревня аборигенов | 8 | `…/location/derevnya-aborigenov`; организация `…/organization/plemya-aborigenov`; сцена `…/scene/derevnya-aborigenov` |
| Дом Джина | 8 | `…/location/dom-dzhina`; сцена `…/scene/dom-dzhina` |
| Дом художника | 9–10 | `…/location/dom-khudozhnika`; сцены `…/scene/dom-khudozhnika`, `…/scene/uilyam-ishchet-zhertvu`; предметы `…/item/nezakonchennoe-polotno`, `…/item/bolshaya-rakushka`; книга `…/tome/dnevnik-uilyama-bleyka` |
| Пещера какамора | 10 | `…/location/peshchera-kakamora`; сцена `…/scene/peshchera-kakamora`; `…/creature/kakamora`; предмет `…/item/naskalnaya-karta` |
| Береговая батарея | 11 | `…/location/beregovaya-batareya`; сцена `…/scene/beregovaya-batareya`; предмет `…/item/polosatyy-platok-dzhina` |
| Дом Номоа | 11 | `…/location/dom-nomoa`; сцена `…/scene/dom-nomoa`; предметы `ritualnyy-kinzhal`, `…/item/oberegi` |
| Дом Адама | 11–12 | `…/location/dom-adama`; сцена `…/scene/sovet-v-dome-adama` |
| Хранителю на заметку: Пророчество (врезка) | 12 | раздатка `…/handout/prorochestvo`; сцена `dom-nomoa` |
| Финал; Условия победы сыщиков | 12 | сцена `…/scene/final`; сценарий: conclusion |
| Условия победы Нгориеру | 12 | сцена `…/scene/chetvertaya-noch`; сценарий: conclusion; предмет `…/item/lodka-dzhina` |
| Награды | 12 | сценарий: conclusion; сцена `final` (mechanics) |
| Чудовища: Адаро | 13 | существо `…/creature/adaro` (статблок) |
| Чудовища: Нгориеру | 13 | существо `…/creature/ngorieru` (статблок, errata) |
| Материалы: Карта острова Сан-Кристобаль | 14 | карта `…/map/ostrov-san-kristobal` (`app/maps/fogs-ostrov-san-kristobal.jpg`, 7 меток на 7 подписях) |
| Страница дневника: 28 октября, 1912 год | физ. 16 | раздатка `…/handout/dnevnik-uilyama`; книга `…/tome/dnevnik-uilyama-bleyka` |
| Страница дневника: «Ктулху фхтагн»; 14 ноября, 1912 год | физ. 17 | раздатка `…/handout/dnevnik-uilyama` |
| Молния (заклинание) | физ. 18 | раздатка `…/handout/zaklinanie-molniya`; книга `dnevnik-uilyama-bleyka` (spells); проект записи заклинания — в отчёте |
| Личное дело № 48 — Микки Валентайн (лист и биография) | физ. 19–20 | готовый сыщик `…/character/mikki-valentayn` |
| Личное дело № 1516 — Томас Грин (лист и биография) | физ. 21–22 | готовый сыщик `…/character/tomas-grin` |
| Личное дело № 2342 — Мэри Стоун (лист и биография) | физ. 23–24 | готовый сыщик `…/character/meri-stoun` |

## Записи (54)

- сценарий 1: `tumany-ostrova-san-kristobal`;
- сцены 15: `dikiy-plyazh`, `britanskoe-poselenie`, `derevnya-aborigenov`, `pervaya-noch`, `dom-dzhina`, `dom-khudozhnika`,
  `peshchera-kakamora`, `beregovaya-batareya`, `vtoraya-noch`, `dom-nomoa`, `uilyam-ishchet-zhertvu`, `tretya-noch`,
  `sovet-v-dome-adama`, `chetvertaya-noch`, `final`;
- места 12: `ostrov-san-kristobal` (город сценария), `britanskoe-poselenie`, `derevnya-aborigenov` (районы), `dom-adama`,
  `tserkov`, `dom-dzhina`, `dom-nomoa`, `dom-khudozhnika` (здания), `dikiy-plyazh`, `peshchera-kakamora`,
  `beregovaya-batareya`, `kholm-varivari` (места);
- карта 1: `ostrov-san-kristobal`;
- персонажи 9: 6 персонажей Хранителя (без статблоков — в книге их нет) и 3 готовых сыщика;
- существа 3: `adaro`, `ngorieru`, `kakamora` (без статблока);
- предметы 7: `ritualnyy-kinzhal`, `oberegi`, `bolshaya-rakushka`, `nezakonchennoe-polotno`, `polosatyy-platok-dzhina`,
  `naskalnaya-karta`, `lodka-dzhina`;
- раздатки 4: `dnevnik-uilyama`, `zaklinanie-molniya`, `prorochestvo`, `svod-zakonov-ostrova`;
- книга Мифов 1: `dnevnik-uilyama-bleyka`; организация 1: `plemya-aborigenov`.

## Опечатки и сомнения

- Нгориеру: СИЛ 160 + ТЕЛ 184 = 344 → БкУ +4d6, Комплекция 5; напечатано +3d6 и 4 (согласны между собой) — большинства
  нет, оставлено как напечатано, `errata` (Р-36), вопрос владельцу.
- Нгориеру: ПЗ «25 днём / 45 четвёртой ночью» при расчётных 43 — задумано книгой (Р-76), `errata` без исправления.
- Кинжал / нож: книга зовёт один предмет то кинжалом (с. 7, 11, 12), то ножом (с. 8, 12) — одна запись, пометка.
- Текстовый слой физ. с. 16–17 местами набран прописными («Сегодня», «НА ОСТРОВЕ», «Господину»); раздатка — по изображению
  (строчные, как написано от руки).
- Микки Валентайн: Скорость 6 (возраст 40 и хромота −1, как сказано на листе) — сходится.

## Не взято

- Иллюстрации: кинжал (с. 7), ракушка (с. 10), адаро на карте, рисунки на полях дневника (оккультные круги, птичья лапа,
  обезьяна — описаны в раздатке), портреты на листах сыщиков — картинки в `app/art/` не входят в файлы части; портреты
  можно добавить позже через `pipeline/art/add_images.py`.
- Текст эпиграфа Джека Лондона (с. 3) — художественная цитата без игровых данных; источник и тема упомянуты в summary.
- Выходные данные (редактор, дизайн, Canva Pro) и содержание (физ. 2–3) — без игровых данных; авторы и конкурс — в summary.
- Склад поселения, сундук художника, морские ежи, «сокровище из темницы», «большая обезьяна», вожди четырёх племён и
  Старейший Шаман, «местные мальчишки», люди из биографий сыщиков (Демьен Кармоди, Анабель, Джон, тётя Руби) — упомянуты
  мимоходом, без описаний: остаются текстом в описаниях мест, существ и персонажей, отдельных записей нет.
- Пустые строки навыков на листах сыщиков (без значений, в том числе «Мифы Ктулху») — не переносились; поля биографии
  с «н/д» перенесены как напечатаны.
