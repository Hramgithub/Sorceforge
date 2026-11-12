# «Лагерь Санни» (`lager-sanni-ru`) — сверка заголовков (Р-134, Р-222)

Книга: `[RU 7e] Лагерь Санни.pdf`, 28 страниц. Это не русский авторский ваншот, а перевод Green Goblin Gang сценария
Chaosium «Camp Sunny» (© 2017; Based on an Original Idea by Keary Birch, Written by Paul Fricker with Mike Mason) для
7-й редакции. Английского оригинала в библиотеке нет — перевод служит полным источником, в том числе для чисел (Р-147).
Текстовый слой надёжен (вёрстка в две колонки, порядок сверен по изображениям); статблоки (с. 13), листы сыщиков
(с. 16, 18, 20, 22, 24, 26 — текстовый слой листов перемешан) и карта (с. 28) сняты с изображений страниц (150–200 dpi).

**Правила и эпоха:** 7-я редакция, `ruleset` = `core`; «современный сценарий» (с. 4): интернет, навигатор, отсутствие
сотовой связи, лагерь основан шестьдесят лет назад, в 1960-х — `axes.era` = `modern`. Год 1980 в каталоге владельца —
не эпоха сценария.

**Страницы:** номер напечатан на каждой странице с 4-й по 28-ю и совпадает с физическим — печатная = физическая
(`offset` 0); с. 1–3 (обложка, выходные данные, заставка переводчиков) без номеров — `printed_page: null`.

**Место действия:** туристический лагерь у Великих озёр (США), город и штат не названы — запись «город сценария»
`location/glush-u-velikikh-ozer` внутри книги (Р-190); новых общих городов нет.

Префикс записей книги: `lager-sanni-ru/<kind>/…` (ниже — без префикса).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Лагерь Санни», логотипы Call of Cthulhu 7th Edition и Chaosium | 1 | `scenario/lager-sanni` (sources) |
| Выходные данные (авторы, перевод Green Goblin Gang, © 2017 Chaosium, оговорки) | 2 | `scenario/lager-sanni` (summary, sources) |
| Заставка переводчиков «Пишем. Переводим. Публикуем» | 3 | `scenario/lager-sanni` (sources) |
| «Лагерь Санни»: «Что вообще может пойти не так во время отдыха в пустующем летнем лагере?» | 4 | `scenario/lager-sanni` (summary) |
| Введение | 4 | `scenario/lager-sanni` (summary, advice); `location/glush-u-velikikh-ozer`, `location/lager-sanni` |
| Что на самом деле происходит? | 4 | `scenario/lager-sanni` (keeper_info); `character/uilyam-fishbern`, `garold-fishbern`, `dzhenis-fishbern`, `frenk-maddoks`; `creature/billi`; `item/zashchitnoe-koltso`, `item/otrublennaya-ruka`, `item/dnevnik-chastnogo-detektiva` |
| Проведение сценария | 4–5 | `scenario/lager-sanni` (advice) |
| Сыщики | 5 | `scenario/lager-sanni` (advice); персонажи-прегены (ниже) |
| Действующие лица: Гарольд и Дженис Фишберн, гибриды глубоководных | 5 | `character/garold-fishbern`, `character/dzhenis-fishbern` (legend, abilities «Притяжение противоположного пола») |
| Первое впечатление о Гарольде Фишберне; Первое впечатление о Дженис Фишберн (описания для мужчин и женщин) | 5 | `handout/pervoe-vpechatlenie-dlya-muzhchin`, `handout/pervoe-vpechatlenie-dlya-zhenshchin`; `character/…fishbern` (background.description) |
| Оспаривание первого впечатления (МОЩ), зов Билли и шерифа | 6 | `scene/otkryvayushchaya-stsena` (mechanics); `character/…fishbern` (abilities) |
| Замыслы Гарольда и Дженис | 6 | `scenario/lager-sanni` (keeper_info); `character/…fishbern` (background.secret) |
| Зацепки для отыгрыша | 6 | `character/…fishbern` (background.traits) |
| Билли, домашний шоггот (текст) | 6 | `creature/billi` (description, legend, abilities «„Вечеринка“»); `item/bloknot-uilyama-fishberna`; `location/klubnaya-komnata` |
| «См. также „Прочие персонажи“» | 6 | `character/postoyalets-lagerya` и др. (ниже) |
| Вводная для игроков | 6–7 | `scene/vvodnaya-dlya-igrokov`; `scenario/lager-sanni` (hook); `item/vnedorozhnik-studentov` |
| Открывающая сцена | 7 | `scene/otkryvayushchaya-stsena`; `location/resepshn` |
| Первая ночь (совет: прогулки в темноте, «песочница») | 7 | `scene/pervaya-noch` |
| Локации (общее состояние лагеря, фонари, туманы) | 7 | `location/lager-sanni` |
| Ресепшн | 7 | `location/resepshn` |
| Служебный кабинет | 7–8 | `location/sluzhebnyy-kabinet`; `item/dokumenty-lagerya`, `item/gazetnye-vyrezki`, `item/fotografiya-1986-goda`; `character/piter-reynolds`, `character/smitkhi` |
| Домики сыщиков (с примечанием об английском варианте — счётчик на жетонах) | 8 | `location/domiki-syshchikov` |
| Событие: утки у порога | 8 | `location/domiki-syshchikov`; `scene/pervaya-noch` |
| Бассейн | 8 | `location/basseyn`; `creature/billi` |
| Клубная комната (вестибюль, бар, подвал, решётки-стоки) | 8 | `location/klubnaya-komnata`, `location/podval-klubnoy-komnaty` |
| Пляж | 8–9 | `location/plyazh`; `item/otrublennaya-ruka`, `item/zashchitnoe-koltso` |
| Сарай для лодок | 9 | `location/saray-dlya-lodok` |
| Домик Фишбернов | 9 | `location/dom-fishbernov`; `item/dnevnik-chastnogo-detektiva` |
| Домики-трейлеры | 9 | `location/domiki-treylery`; `item/ballony-s-propanom` |
| Детская площадка | 9 | `location/detskaya-ploshchadka` |
| Прочие персонажи (вступление: один усреднённый профиль) | 10 | `character/postoyalets-lagerya` (description, legend) |
| Коринн Хаттон, 56 лет, уборщица лагеря | 10 | `character/korinn-khatton` |
| Дерек Уэрс, 45 лет, постоялец | 10 | `character/derek-uers`; `character/dorin` |
| Семья Симондсов | 10 | `character/bob-simonds`, `shina-simonds`, `radzh-simonds`, `nerissa-simonds`; `scene/pribytie-simondsov` |
| Шериф Смитхи, 58 лет, местный законник | 10–11 | `character/smitkhi` (background, abilities «Под чарами Дженис») |
| Ход игры | 11 | `scenario/lager-sanni` (advice, steps); `scene/pribytie-simondsov` |
| Возможные события | 11 | `scenario/lager-sanni` (steps) |
| Клубная комната вечером | 11 | `scene/klubnaya-komnata-vecherom` |
| Первая ночь (порча внедорожника, проверка ВЫН, механик) | 11–12 | `scene/pervaya-noch`; `item/vnedorozhnik-studentov`; `character/rey-douson` |
| День на пляже | 12 | `scene/den-na-plyazhe` |
| Жалоба Фишбернам | 12 | `scene/zhaloba-fishbernam` |
| Мы вызываем полицию! | 12 | `scene/my-vyzyvaem-politsiyu`; `character/smitkhi` |
| Побег из Лагеря Санни | 12 | `scene/pobeg-iz-lagerya-sanni`; `location/glush-u-velikikh-ozer` |
| Заключение: финальная схватка (итоги, 5 пунктов) | 12–13 | `scene/finalnaya-skhvatka`; `scenario/lager-sanni` (conclusion) |
| Персонажи и монстры: Постоялец лагеря (Изменяйте при нужде) | 13 | `character/postoyalets-lagerya` (statblock, names) |
| Персонажи и монстры: Шериф Смитхи, законник | 13 | `character/smitkhi` (statblock) |
| Персонажи и монстры: Гарольд и Дженис, гибриды глубоководных | 13 | `character/garold-fishbern`, `character/dzhenis-fishbern` (statblock; `instance_of` → `coc:creature:deep-one-hybrid`) |
| Персонажи и монстры: Билли, домашний шоггот | 13 | `creature/billi` (statblock, abilities; `instance_of` → `coc:creature:shoggoth`) |
| Готовые сыщики (Удача 3d6×5, «Трата Удачи»; меньше шести игроков) | 14 | `scenario/lager-sanni` (advice); прегены (`player_chooses: luck`); `coc:rule:spending-luck` |
| Студенты (мужчины); Студентки (женщины) — список с отношениями | 14 | прегены (description, relations) |
| Для сыщиков-мужчин (карточки ×3) | 14–15 | `handout/pervoe-vpechatlenie-dlya-muzhchin` |
| Для сыщиков-женщин (карточки ×3) | 15 | `handout/pervoe-vpechatlenie-dlya-zhenshchin` |
| Лист сыщика: Фил Пэйнтер | 16 | `character/fil-peynter` |
| Фил Пэйнтер — предыстория | 17 | `handout/predystoriya-fila-peyntera`; `character/fil-peynter` (legend, background, relations) |
| Лист сыщика: Джо-Джо Джонсон | 18 | `character/dzho-dzho-dzhonson` |
| Джо-Анна (Джо-Джо) Джонсон — предыстория | 19 | `handout/predystoriya-dzho-dzho-dzhonson`; `character/dzho-dzho-dzhonson` |
| Лист сыщика: Элли Бехель | 20 | `character/elli-bekhel` |
| Элли Бехель — предыстория | 21 | `handout/predystoriya-elli-bekhel`; `character/elli-bekhel` |
| Лист сыщика: Рейдел Грей | 22 | `character/reydel-grey` |
| Рейдел Грей — предыстория | 23 | `handout/predystoriya-reydela-greya`; `character/reydel-grey` |
| Лист сыщика: Нейт Аптон | 24 | `character/neyt-apton` |
| Нейт Аптон — предыстория | 25 | `handout/predystoriya-neyta-aptona`; `character/neyt-apton` |
| Лист сыщика: Чарли Харриган | 26 | `character/charli-kharrigan` |
| Чарли Харриган — предыстория | 27 | `handout/predystoriya-charli-kharrigan`; `character/charli-kharrigan` |
| Карта лагеря | 28 | `map/lager-sanni` (картинка `app/maps/sunny-lager-sanni.jpg`, 16 меток на всех подписях: ОЗЕРО, Красное ведро, CLIFFS ×2, Обрыв, Пляж, Сарай для лодок, PATH, Площадка, Кабинки, Клубная комната, CAMP SUNNY, Ресепшн, Дом Фишбернов, CAR PARK, Трейлеры); места `location/ozero`, `location/obryvy`, `location/parkovka` |

Отношения шести прегенов — 15 пар, каждая хранится один раз (`knows` / `rival_of` с `note` и `note_back` по их
предысториям).

## Записи (67)

- сценарий 1: `scenario/lager-sanni`;
- сцены 10: `vvodnaya-dlya-igrokov`, `otkryvayushchaya-stsena`, `pervaya-noch`, `klubnaya-komnata-vecherom`,
  `den-na-plyazhe`, `zhaloba-fishbernam`, `my-vyzyvaem-politsiyu`, `pribytie-simondsov`, `pobeg-iz-lagerya-sanni`,
  `finalnaya-skhvatka`;
- места 16: `glush-u-velikikh-ozer` (город сценария), `lager-sanni`, `resepshn`, `sluzhebnyy-kabinet`,
  `domiki-syshchikov`, `basseyn`, `klubnaya-komnata`, `podval-klubnoy-komnaty`, `plyazh`, `saray-dlya-lodok`,
  `dom-fishbernov`, `domiki-treylery`, `detskaya-ploshchadka`, `ozero`, `obryvy`, `parkovka`;
- карта 1: `map/lager-sanni`;
- персонажи 21: прегены `fil-peynter`, `dzho-dzho-dzhonson`, `elli-bekhel`, `reydel-grey`, `neyt-apton`,
  `charli-kharrigan`; `garold-fishbern`, `dzhenis-fishbern`, `uilyam-fishbern`, `smitkhi`, `korinn-khatton`,
  `derek-uers`, `dorin`, `bob-simonds`, `shina-simonds`, `radzh-simonds`, `nerissa-simonds`, `piter-reynolds`,
  `frenk-maddoks` (имя придумано, Р-150), `rey-douson` (имя придумано), `postoyalets-lagerya` (групповой профиль, Р-151);
- существо 1: `creature/billi` (`instance_of` → `coc:creature:shoggoth`);
- предметы 9: `vnedorozhnik-studentov`, `otrublennaya-ruka`, `zashchitnoe-koltso`, `dnevnik-chastnogo-detektiva`,
  `gazetnye-vyrezki`, `dokumenty-lagerya`, `fotografiya-1986-goda`, `bloknot-uilyama-fishberna`, `ballony-s-propanom`;
- раздатки 8: `pervoe-vpechatlenie-dlya-muzhchin`, `pervoe-vpechatlenie-dlya-zhenshchin`, шесть предысторий
  `predystoriya-*`.

## Опечатки и сомнения

- Билли (с. 13): ЛВК 420 — повтор ТЕЛ; Уклонение 10% соответствует ЛВК около 20 (у вида — 15). `errata`, как напечатано.
- Шериф Смитхи (с. 13): «БкУ 0, Компл. 0» при СИЛ 70 + ТЕЛ 75 = 145 (по правилам +1d4 и 1; урон драки напечатан
  «1d3+1d4»); ПМ 9 при МОЩ 50 (по правилам 10); винтовка «.38-06» — опечатка .30-06 (урон 2d6+4). `errata`, как
  напечатано; оружие связано с `coc:weapon:30-06-semi-automatic-rifle`.
- Постоялец лагеря (с. 13): урон драки «1d3+1d4» при БкУ 0. `errata`.
- Гарольд и Дженис (с. 13): НАР «35/85*» при сноске «Удвойте НАР» (удвоение — 70). `errata`.
- Листы сыщиков, исправлено в записях (Р-35, `fixed: true`): Фил — Ис-во/ремесло (Живопись) 70 (70/70) → (35/14);
  Джо-Джо — Средства 48 (24/3) → (24/9); Рейдел — ОБР 75 (37/12) → (37/15); Нейт — ТЕЛ 55 (27/10) → (27/11),
  Уклонение 55 (22/11) → (27/11).
- Элли: у Науки вписаны «Биология» и «Фармацевтика», но поля значений пусты — в записи без значений, `errata`.
- Чарли: список на с. 14 — «свободна, но испытывает симпатию к Элли», а в её предыстории (с. 27) она терпеть не может
  Элли; возможно, ошибка перевода. `errata` в `character/charli-kharrigan`, запись — по предыстории.
- Семья Симондсов (с. 10): «братья могут расправиться с родителями» — по смыслу Фишберны (брат и сестра); пометка в
  `scene/pribytie-simondsov`.
- Мелкие словесные опечатки исправлены молча (Р-39): «Механие 40%» → Механика, «(Измение при нужде)» → «Изменяйте при
  нужде» (в `raw` способностей Билли текст оставлен как напечатан, с «Будучи шогготов»).
- Мужчина на фотографии 1986 года и владелец блокнота — Уильям Фишберн: вывод из текста (Р-41).
- Мили (сто миль, 40 миль в час, двадцать миль) — в текстах километрами (Р-64), исходное — в `quality.notes`.
- **Вид издания:** в `books.json` книга записана `official` (метка `[RU 7e]` в имени файла), но это перевод группы
  Green Goblin Gang, а не издание Chaosium/«Мира Хобби» — владельцу стоит решить, не `trusted` ли это (на числа не
  влияет: оригинала в библиотеке нет).

## Предложения правок общих записей

`proposals-sunny.json` — 2 (псевдонимы, Р-96): «Поглощение облика» у `coc:spell:consume-likeness` и «Знак Древних» у
`coc:spell:elder-sign`. Пробный прогон `apply.py --dry-run` — ложатся оба.

## Не взято

- Картинки: обложка с логотипами (с. 1), заставка переводчиков (с. 3), фото-портреты на листах сыщиков (с. 16–26) —
  картинки в `app/art` вне файлов части; владелец может добавить портреты через `pipeline/art/add_images.py`.
- Юридический текст выходных данных (с. 2) — только упоминание в `sources` сценария.
- Пустые поля листов сыщиков (Игрок, Местожительство, Место рождения, отметки навыков, шкалы ПЗ/Рассудка/Удачи/ПМ);
  базовые значения навыков на листах — в статблоках только навыки, отличные от базовых (пометка в `quality.notes`).
- Без своих записей (текстом в местах и сценах): дядя сыщиков, бабушка детектива, патрульные на участке шерифа,
  жертвы Билли (дальнобойщик, коммивояжёр, пропавшие юнцы), газета South Lakes Tribune (организации не заводил),
  ключ от сарая и железные ключи Фишбернов, телефоны лагеря, аквариум с золотыми рыбками, счётчик на жетонах.
- Бассейн на карте не отмечен — метки нет (в `location/basseyn` пометка).
- Новых заклинаний нет («Поглощение облика» = `coc:spell:consume-likeness`); новых общих городов нет.
