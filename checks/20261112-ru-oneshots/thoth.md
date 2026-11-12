# «Идол Тота» (`idol-tota-ru`) — сверка переноса (часть thoth)

Источник — официальный русский перевод (`[RU 7e]`; в титрах: перевод Miskatonic Librarians, версия 1.1) сценария Джо Триера
(Stygian Fox) для «Зова Ктулху» 7-й редакции. PDF 24 страницы, скан без текстового слоя: каждая страница распознана
tesseract (`-l rus`, 200 dpi), все числа, статблоки, хронология и карты сверены по изображениям страниц. Правила — 7-я
редакция, `ruleset` core. Действие — вторник, 10 февраля 1925 года (Бостон и Аркхэм); на обложках — «возвращается в
1920 году»; `axes.era` — `1920s`.

## Страницы

Смещение: **печатная = физическая − 1** (номер внизу страницы: физ. 2 = с. 1, физ. 7 = с. 6, физ. 19 = с. 18, физ. 22 = с. 21).
Без номера: обложка (физ. 1), титульный лист (физ. 3), пустая страница (физ. 23), задняя обложка (физ. 24).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка, титульный лист «Идол Тота» | физ. 1, 3 | сценарий `idol-tota-ru/scenario/idol-tota` (summary, sources) |
| Титры | 1 | сценарий (summary: автор, издатель, перевод) |
| Карта транспортной системы Бостона (версия Хранителя с цветными метками) | 3 | карта `…/map/karta-transportnoy-sistemy-bostona` (`app/maps/thoth-karta-bostona.jpg`, 52 метки: 3 цветных квадрата, 3 строки легенды, 25 станций, 21 подпись районов, рек, улиц и направлений) |
| Содержание | 4 | навигация — не взято (см. ниже) |
| Идол Тота; Описание сценария | 5 | сценарий: summary, hook |
| Информация для Хранителя | 5–6 | сценарий: keeper_info; существо `…/creature/idol-tota` (legend); `…/character/artur-ormond`, `…/character/klerens-batterfild`, `…/character/etel-brauning`, `…/character/uorren-hollister`, `…/character/rodstvenniki-ormonda` |
| Хронология конца 1924 – начала 1925 года (таблица) | 6 | сценарий: `tables` «Хронология конца 1924 – начала 1925 года» (6 строк) |
| Расследование начинается; Музей изобразительных искусств | 6 | сцена `…/scene/muzey-pribytie`; место `…/location/muzey-izobrazitelnykh-iskusstv` |
| Прибытие сыщиков | 7 | сцена `muzey-pribytie` |
| Мистер Уоррен Холлистер, владелец музея | 7 | `…/character/uorren-hollister`; сцена `muzey-pribytie` |
| Мисс Этель Браунинг | 7–8 | `…/character/etel-brauning`; сцена `…/scene/muzey-etel-brauning`; предмет `…/item/vizitnaya-kartochka-greya` |
| Выставка | 8–9 | сцена `…/scene/muzey-vystavka`; место `…/location/muzey-atrium` |
| Саркофаг | 9 | предмет `…/item/sarkofag-idola-tota`; сцена `muzey-vystavka` |
| Стол Клэренса Баттерфилда | 9–10 | раздатка `…/handout/zapisi-klerensa-batterfilda`; предмет `…/item/egipetskiy-ieroglificheskiy-slovar` |
| Постамент | 10 | предмет `…/item/statuya-isidy` |
| Расследование продолжается | 10 | сцена `…/scene/rassledovanie-prodolzhaetsya` |
| Лечебница Аркхэма | 10 | сцена `…/scene/lechebnitsa-doktor-merrik`; общее место `coc:location:arkham-sanitarium` (предложения) |
| Доктор Меррик | 10 | `…/character/uilyam-merrik`, `…/character/chester-merrik`; сцена `lechebnitsa-doktor-merrik` |
| Снаружи лечебницы | 10–12 | `…/character/dzheyms`; сцена `lechebnitsa-doktor-merrik` |
| План лечебницы (первый этаж, подвал, второй, третий этаж) | 11 | карта `…/map/plan-lechebnitsy-arkhema` (`app/maps/thoth-lechebnitsa-arkhema.jpg`, 60 меток на все подписи); места `…/location/lechebnitsa-pervyy-etazh`, `…-podval`, `…-vtoroy-etazh`, `…-tretiy-etazh`, `…/location/lechebnitsa-palata-artura-ormonda` |
| Мистер Артур Ормонд | 12 | сцена `…/scene/lechebnitsa-artur-ormond`; `…/character/artur-ormond` |
| Мискатоникский университет в Аркхэме; Библиотека | 12 | сцена `…/scene/miskatonik-biblioteka`; общие места `coc:location:miskatonic-university`, `coc:location:orne-library` (предложения) |
| Книга Мертвых: аналитика 20-го века (1921) доктора Томаса Уильямса | 12 | предмет `…/item/kniga-mertvykh-analitika` (миф целиком) |
| Идол Тота / Фараон самой черной ночи | 12 | сцена `miskatonik-biblioteka`; существо `idol-tota` (legend) |
| Фрагменты Эхнатона (18-я династия) | 12 | книга `…/tome/fragmenty-ekhnatona`; сцена `miskatonik-biblioteka` |
| Кабинет 366 | 13–14 | сцена `…/scene/kabinet-366`; место `…/location/kabinet-366`; предметы `…/item/staryy-schet-za-gaz`, `…/item/kalendar-greya`; раздатка `…/handout/nedopisannoe-pismo-greya`; `…/character/goratsiy-finni` |
| План «Кабинет профессора Винсента Грея в Мискатоникском университете» | 13 | карта `…/map/kabinet-366` (`app/maps/thoth-kabinet-366.jpg`, 7 меток) |
| Бостон Глоуб | 14 | сцена `…/scene/boston-globe`; место `prizrak-ru/location/redaktsiya-boston-globe` (чужая запись, предложения) |
| Статья «Эксцентричный авантюрист болен» | 14 | раздатка `…/handout/statya-ekstsentrichnyy-avantyurist-bolen`; `…/character/genri-rods` |
| Дом Клэренса Баттерфилда | 14 | сцена `…/scene/dom-klerensa`; место `…/location/dom-klerensa-batterfilda`; `…/character/bridzhit-omelli` |
| Дом профессора Винсента Грея | 14–15 | `…/character/vinsent-grey`; место `…/location/osobnyak-greya` (в «Окрестностях Аркхэма», Р-209) |
| Поездка в особняк Грея; Прибытие к дому | 15 | сцена `…/scene/poezdka-v-osobnyak-greya`; `…/character/ebenezer-kholbruk` |
| Профессор Винсент Грей | 15–16 | сцена `…/scene/professor-grey` |
| Нападение Клэренса Баттерфилда | 16 | сцена `…/scene/napadenie-klerensa`; ссылка `coc:rule:chases` |
| Возвращение в музей изобразительных искусств; Прибытие; До 5 часов вечера | 16 | сцена `…/scene/vozvrashchenie-v-muzey` |
| После 5 часов вечера | 16 | сцена `…/scene/posle-5-chasov`; `…/character/prisluzhniki-tota` |
| Уничтожение идола | 16–17 | сцена `…/scene/unichtozhenie-idola`; существо `idol-tota` (способность «Хрупкость») |
| Эпилог (награды) | 17 | сцена `…/scene/epilog`; сценарий: conclusion |
| Приложение: Фрагменты Эхнатона | 17 | книга `…/tome/fragmenty-ekhnatona` (чтение, 8 заклинаний — все есть в `kb/spells`) |
| Приложение: Идол Тота (описание, статблок) | 17–18 | существо `…/creature/idol-tota` |
| Мисс Этель Браунинг (статблок) | 18 | `…/character/etel-brauning` |
| Мистер Клэренс Баттерфилд (статблок) | 18 | `…/character/klerens-batterfild` |
| Прислужники Тота (статблок) | 18 | `…/character/prisluzhniki-tota` (групповой профиль, имена придуманы, Р-151) |
| Заметки для Хранителя: Отыгрывание ролей | 19 | сценарий: advice |
| Заметки для Хранителя: Мисс Этель Браунинг | 19 | `etel-brauning` (legend); сценарий: advice |
| Заметки для Хранителя: Клэренс Баттерфилд | 19 | `klerens-batterfild` (legend); сцена `napadenie-klerensa` |
| Заметки для Хранителя: Место преступления в музее | 19 | сцена `muzey-vystavka` |
| Заметки для Хранителя: Расследование | 19 | сцена `rassledovanie-prodolzhaetsya` |
| Заметки для Хранителя: Артур Ормонд (захватывающая или напряжённая игра) | 20 | сцена `lechebnitsa-artur-ormond` |
| Заметки для Хранителя: Профессор Грей | 20 | `vinsent-grey` (legend); сцена `rassledovanie-prodolzhaetsya` |
| Листовка «Египетская феерия» | 20 | раздатка `…/handout/listovka-egipetskaya-feeriya` |
| Карта транспортной системы Бостона (без меток, для игроков) | 21 | карта `karta-transportnoy-sistemy-bostona` (второй источник; картинка — версия с. 3) |
| Задняя обложка | физ. 24 | сценарий (sources) |

## Записи (58) и картинки (3)

- сценарий 1: `idol-tota`;
- сцены 17: `muzey-pribytie`, `muzey-etel-brauning`, `muzey-vystavka`, `rassledovanie-prodolzhaetsya`, `lechebnitsa-doktor-merrik`,
  `lechebnitsa-artur-ormond`, `miskatonik-biblioteka`, `kabinet-366`, `boston-globe`, `dom-klerensa`, `poezdka-v-osobnyak-greya`,
  `professor-grey`, `napadenie-klerensa`, `vozvrashchenie-v-muzey`, `posle-5-chasov`, `unichtozhenie-idola`, `epilog`;
- места 10: `muzey-izobrazitelnykh-iskusstv`, `muzey-atrium`, `dom-klerensa-batterfilda` (Бостон); `lechebnitsa-pervyy-etazh`,
  `lechebnitsa-podval`, `lechebnitsa-vtoroy-etazh`, `lechebnitsa-tretiy-etazh`, `lechebnitsa-palata-artura-ormonda`
  (в `coc:location:arkham-sanitarium`); `kabinet-366` (в `coc:location:miskatonic-university`); `osobnyak-greya`
  (в `keepers-companion-en/location/arkham-environs`);
- карты 3: `karta-transportnoy-sistemy-bostona`, `plan-lechebnitsy-arkhema`, `kabinet-366`
  (`app/maps/thoth-karta-bostona.jpg`, `thoth-lechebnitsa-arkhema.jpg`, `thoth-kabinet-366.jpg`);
- персонажи 14: со статблоком `etel-brauning`, `klerens-batterfild`, `prisluzhniki-tota` (группа); без статблока
  `uorren-hollister`, `artur-ormond`, `vinsent-grey`, `uilyam-merrik`, `chester-merrik`, `dzheyms`, `genri-rods`;
  с придуманным именем (Р-150, `editorial_text`) `ebenezer-kholbruk` (дворецкий Грея), `bridzhit-omelli` (домовладелица
  Клэренса), `goratsiy-finni` (сотрудник университета с ключом); группа `rodstvenniki-ormonda` (имена придуманы, Р-151);
- существо 1: `idol-tota` (уникальная сущность, свой статблок);
- книга Мифов 1: `fragmenty-ekhnatona`;
- предметы 7: `sarkofag-idola-tota`, `egipetskiy-ieroglificheskiy-slovar`, `kniga-mertvykh-analitika`, `vizitnaya-kartochka-greya`,
  `staryy-schet-za-gaz`, `kalendar-greya`, `statuya-isidy`;
- раздатки 4: `zapisi-klerensa-batterfilda`, `statya-ekstsentrichnyy-avantyurist-bolen`, `nedopisannoe-pismo-greya`,
  `listovka-egipetskaya-feeriya`.

## Опечатки и сомнения

- Сцена «Лечебница Аркхэма» (с. 10): «В понедельник, 9 января (уже не полнолуние)» — по хронологии (с. 6) 9 января —
  пятница, полнолуние, а понедельник с убывающей луной — 12 января (errata, как напечатано).
- «Фрагменты Эхнатона»: в библиотеке и у Грея — «18-я династия» (с. 12, 14), в приложении — «17-я династия, 1340 г. до н.э.?»
  (с. 17) (errata).
- Прислужники Тота: ПМ 8 при МОЩ 50 (должно быть 10) — errata, как напечатано.
- Идол Тота, «Доминирование»: «Встречной проверке СИЛ», а у идола СИЛ — прочерк (МОЩ 150); вероятно, имелась в виду МОЩ
  (errata, вывод из текста).
- Мисс Браунинг: «БкУ: -» (по СИЛ + ТЕЛ = 95 — 0); в `value` 0, пометка в записи.
- Размер саркофага «18 дюймов (46 см)» — в записях только метрическая мера (Р-64).
- Листовка (с. 20) напечатана прописными; в `handout.text` набрана обычным регистром: `tools/check.py` принимает слово «раз»
  прописными («…ВЫПАДАЕТ РАЗ В ЖИЗНИ!») за запрещённое обозначение размера (ложное срабатывание правила «РАЗ/ВЕЛ»).
- На плане лечебницы «Т» не расшифровано — в пояснениях меток «туалет (вывод из обозначения)».

## Не взято

- Содержание (с. 4) — навигация по книге, в базе её заменяют ссылки.
- Иллюстрации: портреты Холлистера, Браунинг, Меррика, Ормонда, Грея, Клэренса, фото музея и «Дома Грея», рисунки саркофага
  и идола, пример египетских артефактов (с. 5) — папка `app/art/` вне моей части; кандидаты для `images`
  (`pipeline/art/add_images.py`). В папке владельца `3_КБ\Ваншоты\1925 Идол Тота\раздат Идол Тота` есть те же портреты,
  листовка, саркофаг, идол и «Карта Бостонского музея» (988×702) — плана музея в книге нет, поэтому эта картинка не взята.
- Легенда условных обозначений карты Бостона (линии надземного метро, трамвайные пути, станции) и роза ветров на плане
  лечебницы — метки не ставились; псевдоиероглифы под заголовком листовки.
- Безымянные «несколько крупных санитаров» лечебницы — фон сцены без роли и параметров, остаются текстом в сцене
  «Мистер Артур Ормонд».
- Логотипы и выходные данные (Chaosium, Stygian Fox, How We Roll, Miskatonic Repository, адреса сайтов, задняя обложка) —
  не данные сценария (автор и перевод названы в summary).
- Сценарий «Dead Light» (Chaosium), упомянутый как похожая ситуация с преследованием, — записи в базе нет, упоминание
  оставлено текстом в сцене «Поездка в особняк Грея».

## Кандидаты в новые записи (вне моей части)

- Редакция «Бостон Глоуб» — запись книги `prizrak-ru/location/redaktsiya-boston-globe`, теперь встречается во второй книге:
  по Р-154 её стоит перенести в общие (`coc:location:boston-globe`); пока — ссылки и абзац предложением.
- Затерянный город Ньярлат близ Каира и «Фараон самой чёрной ночи» — остаются текстом (книга не связывает их с
  Ньярлатхотепом или Чёрным фараоном прямо; только заклинание «Связь с божеством: Ньярлатхотеп» во «Фрагментах»).
- Районы и пригороды Бостона с карты (Кембридж, Челси, Южный Бостон, Дорчестер и др.) — записей нет, метки ведут на
  Бостон с пояснением.

## Предложения

`proposals-thoth.json` — 45 правок в 7 записях (пробный прогон `apply.py --dry-run` проходит): абзацы, источники и ссылки
для `coc:location:boston`, `coc:location:arkham`, `coc:location:arkham-sanitarium` (+4 жителя: Ормонд, оба Меррика,
Джеймс), `coc:location:miskatonic-university`, `coc:location:orne-library`, `keepers-companion-en/location/arkham-environs`
(особняк Грея) и `prizrak-ru/location/redaktsiya-boston-globe`.
