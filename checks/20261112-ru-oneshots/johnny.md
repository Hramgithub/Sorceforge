# «Джонни Бой» (`dzhonni-boy-ru`) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] Джонни Бой (Андрей Смирнов).pdf`, 8 страниц; русский авторский ваншот для 7-й редакции (автор —
Смирнов Андрей Викторович). Текстовый слой надёжен (вёрстка в две колонки, порядок сверен по изображениям); статблоки
«Вампиры» и «Люди», списки потерь и наград Рассудка (с. 6–7) и с. 1, 8 сверены по изображениям страниц (150 dpi).
Карт в книге нет; с. 1 — обложка-фотография (машина на сельской дороге), с. 8 — фото Джонни и радиоприёмника.

**Эпоха:** наши дни — смартфоны, навигатор, 911, блютуз-колонка, вампир обращён в 1956 году; в каталоге владельца
стоит 1930 — это ошибка каталога. `axes.era` = `modern`, `ruleset` = `core`.

**Страницы:** номеров на страницах нет — печатная = физическая (`offset` 0); в записях `printed_page` = `physical_page`.

**Место действия:** город не назван (глухая сельская местность, по 911 и федеральному шоссе — США) — запись
«город сценария» внутри книги `location/selskaya-glush` (Р-190); новых общих городов нет.

Префикс записей книги: `dzhonni-boy-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка (фотография без текста) | 1 | `scenario/dzhonni-boy` (sources) |
| «Джонни Бой»; «О сценарии (для 2-6 сыщиков)» | 2 | `scenario/dzhonni-boy` (summary) |
| Вступление без заголовка: ночная дорога, 0:37, таран эвакуатора, погоня, три исхода | 2 | `scene/taran-na-doroge`; `scenario/…` (hook, advice); `location/obezdnaya-doroga`, `location/selskaya-glush`; `item/evakuator-dzhonni-boya` |
| Вылет на обочину | 2 | `scene/vylet-na-obochinu`; `location/kukuruznye-polya` |
| Победа в погоне | 2 | `scene/pobeda-v-pogone`; `location/povorot-na-fermu` |
| Авария эвакуатора (варианты 1 и 2) | 2 | `scene/avariya-evakuatora`; `item/evakuator-dzhonni-boya` |
| Вечеринка с коктейлями (и сноска о треках Radio Tapok) | 3 | `scene/vecherinka-s-kokteylyami`; `scenario/…` (advice); `coc:weapon:molotov-cocktail` (предложение варианта) |
| Что стоит знать и помнить Хранителю? — Темнота | 3 | `scene/okhota-v-temnote` (description, mechanics); `scenario/…` (advice); `character/dzhonni-dikson` (abilities «Зрение в темноте») |
| О вампире | 3 | `character/dzhonni-dikson` (background, legend); `scenario/…` (keeper_info) |
| Особенности отыгрыша вампира (5 пунктов) | 3–4 | `character/dzhonni-dikson` (background.traits) |
| Вещи Джонни Боя («На момент старта среди вещей…») | 4 | `character/dzhonni-dikson` (possessions, wealth, attacks); `item/radiopriyomnik-regency-tr-1`; `handout/fotokartochka-dzhonni-boya` |
| Что из суеверий о вампирах правда? Дневной свет; кол в сердце; окончательная смерть | 4 | `character/dzhonni-dikson` (abilities); `item/derevyannyy-kol`; `scenario/…` (keeper_info) |
| Деревянный кол (ближний бой, драка) | 4 | `item/derevyannyy-kol` (mechanics) |
| Подмога | 4 | `scene/vyzov-podmogi` |
| Поворот на ферму и ловушка | 4 | `location/povorot-na-fermu`; `scene/ferma-bishopov` |
| Ферма (пёс, машины, сарай, скотный двор, бензоколонка, прихожая, спальня, дверь в подвал) | 4 | `location/ferma-bishopov`, `location/dom-bishopov`, `location/saray-fermy-bishopov`; `scene/ferma-bishopov`; `character/garold-bishop`, `character/linda-bishop` |
| Сара Бишоп в подвале; коробка патронов; ключи; кухня | 5 | `character/sara-bishop`; `scene/sara-v-podvale`; `location/podval-doma-bishopov`; `location/dom-bishopov`; `creature/novoobrashchennyy-vampir` |
| Возможные события на полях (1–6) | 5 | `location/kukuruznye-polya` (tables «Возможные события на полях»; в `scenario/…` — ссылка `from`); `character/dzhozef-bishop`, `character/dzhessika-kuper` |
| Аптечки | 5 | `item/aptechka` |
| Наезд | 5 | `scene/okhota-v-temnote` (mechanics); `scenario/…` (advice) |
| Одержимость | 5 | `character/dzhonni-dikson` (abilities «Взгляд»); `scene/okhota-v-temnote` |
| Полиция и оператор 911 | 5–6 | `scene/vyzov-podmogi`; `character/lyuk-parker` (legend) |
| «Милосердие» вампира (1–3) | 6 | `scene/okhota-v-temnote`; `character/dzhonni-dikson` (background.secret); `creature/novoobrashchennyy-vampir` (legend) |
| Уехать на машине? | 6 | `scene/uekhat-na-mashine` |
| Последнее убийство | 6 | `scene/poslednee-ubiystvo` |
| Возможные потери рассудка (1–7) | 6 | `scenario/…` (tables); `character/dzhonni-dikson` (statblock.sanity_loss) |
| Возможные награды (1–7) | 6 | `scenario/…` (tables, conclusion) |
| Вампиры: Вампир Джонни «Бой» Диксон | 6 | `character/dzhonni-dikson` (statblock, abilities); связь `instance_of` → `coc:creature:vampire` |
| Вампиры: Новообращённый вампир без сил | 6 | `creature/novoobrashchennyy-vampir`; `character/sara-bishop` (`instance_of`) |
| Люди: Люк Паркер (52 года), офицер полиции | 7 | `character/lyuk-parker` |
| Люди: Случайный парень (23 года) | 7 | `character/kayl-merfi` (имя придумано, Р-150) |
| Люди: Случайная девушка (20 лет) | 7 | `character/dzhessika-kuper` (имя придумано, Р-150) |
| Достижения Хранителя (10 отметок) | 7 | `scenario/…` (tables «Достижения Хранителя») |
| Фотокарточка «Джонни Бой, март 1951» | 8 | `handout/fotokartochka-dzhonni-boya` |
| ***Портативный радиоприёмник Regency TR-1 | 8 | `item/radiopriyomnik-regency-tr-1` |
| Автор ваншота: Смирнов Андрей Викторович | 8 | `scenario/…` (summary) |

## Опечатки и сомнения

- Новообращённый вампир (с. 6): «ПЗ 13 (при 0 в дым)» противоречит описанию Сары (с. 5: после смерти не обратится в дым
  и не залечит ран) — `errata` в `creature/novoobrashchennyy-vampir`, как напечатано.
- Джонни Бой: Стрельба напечатана дважды («Стрельба и метание 40%…» и «Стрельба 40% (20/8)…») — одна атака, пометка в
  `notes`. «Ближний бой 50% (+1к4), урон 2к4» и «нож 2к4+1» — по-видимому, урон уже с БкУ 1d4 (вывод из текста, Р-41).
  Скорость 10 — как у вида «Вампир» («как у вида +2»), по характеристикам человека было бы 8 — в `quality.notes`.
- Укус обоих вампиров — потеря цели 2d10 СИЛ (как напечатано); в общей записи «Вампир» по Malleus — ВЫН.
- «Полиция и оператор 911» (с. 6): последняя фраза оборвана («…когда вампир должен вот-вот уничтожить») — оставлено как
  напечатано, пометка в `scene/vyzov-podmogi`.
- В тексте сцены полицейский теряет «дробовик и пистолет», в статблоке у него револьвер .38 — пометка у Люка Паркера.
- «двухмильная пробка» (с. 2) — в текстах метрами (около 3,2 км), исходное — в `quality.notes` (Р-64).

## Предложения правок общих записей

`proposals-johnny.json` — 2: вариант источника у `coc:weapon:knife-small` (выкидной нож 1d4+1) и у
`coc:weapon:molotov-cocktail` (урон 1d6 огнём + горение) (Р-124). Пробный прогон `apply.py --dry-run` — ложатся оба.

## Не взято

- Изображения: обложка (с. 1), фото Джонни и радиоприёмника (с. 8) — картинки в `app/art` вне файлов части; подпись
  фото — в раздатке. Владелец может добавить их через `pipeline/art/add_images.py`.
- Безымянные эпизодические люди без характеристик — семейная пара в случайной машине, мужчина в багажнике, брат и муж
  выжившей девушки, оператор 911 — остаются текстом в сценах и таблице полей (своих записей не заводил).
- Отдельные записи для скотного двора, бензоколонки, трактора, ловушки — описаны текстом в местах и таблице полей.
- Кандидат в справочник оружия: деревянный кол (1d6 + БкУ, ближний бой) — пока механика хранится в `item/derevyannyy-kol`.
