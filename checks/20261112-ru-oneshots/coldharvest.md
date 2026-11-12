# «Холодный урожай» (kholodnyy-urozhay-ru) — сверка покрытия

Книга: «Холодный урожай» (Cold Harvest: Roleplaying During the Great Purges, Chad J. Bowser, Chaosium #23143),
официальное русское издание «[RU 7e]», 63 страницы PDF с текстовым слоем (числа, статблоки и обе карты сверены по
изображениям страниц; распознавание не понадобилось). Система — «Зов Ктулху» 7e, `ruleset: "core"`, эпоха — октябрь
1937 года (`era: ["1930s"]`).

Страницы: номеров на страницах нет — печатная = физическая (offset 0). Физ. 1 — обложка, 63 — плакат без текста.

Префикс записей: `kholodnyy-urozhay-ru/`. Новый общий город — `coc:location:kuybyshev` (`kb/locations/kuybyshev.json`);
места сценария — в «Окрестностях Куйбышева» (Р-209). Карты — `app/maps/coldharvest-*.jpg` (2 штуки). Готовые сыщики уже
были в базе (книга `kholodnyy-urozhay-pregens-ru`) — на них только ссылки; очерки сценария (с. 50–60) — предложениями.

Записей: 102 (сценарий 1, сцен 19, мест 30 + общий город, карт 2, персонажей 34, существо 1, организация 1, предметов 9,
раздаток 4).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка (Cold Harvest, Roleplaying During the Great Purges, by Chad J. Bowser) | 1 | `scenario/kholodnyy-urozhay` (name.en, aliases, summary) |
| Холодный урожай. Расследование антисоветской деятельности в Средней Азии | 2 | `scenario/kholodnyy-urozhay` (summary, advice) |
| Предыстория для Хранителя (Октябрь 1937 года; зацепки; триггерные события) | 3–4 | `scenario/kholodnyy-urozhay` (keeper_info, hook); `creature/lloigor` (legend) |
| Приказ НКВД № 00447 (врезка) | 4 | `item/prikaz-00447`; `character/nikolay-ezhov` |
| Ключевые неигровые персонажи | 4 | `scenario/kholodnyy-urozhay` (advice) |
| Совет хранителю (эскизы NPC как раздатка) | 4–5 | `scenario/kholodnyy-urozhay` (advice); картинки — не взято |
| Григорий Павлович Аганин (очерк) | 5 | `character/grigoriy-aganin` |
| Пётр Михайлович Абрамов (очерк) | 5 | `character/petr-abramov` |
| Дмитрий Петрович Абрамов (очерк) | 6 | `character/dmitriy-abramov` |
| Екатерина Боровна Абрамова (очерк) | 6–7 | `character/ekaterina-abramova` |
| Борис Александрович Гапон (очерк) | 7 | `character/boris-gapon` |
| Василий Викторович Смольский (очерк) | 8 | `character/vasiliy-smolskiy` |
| Мария Андроновна Елизарова (очерк) | 8 | `character/mariya-elizarova` |
| Андрей Галинович Елизаров (очерк) | 9 | `character/andrey-elizarov` |
| Раиса Андреевна Елизарова (очерк) | 9 | `character/raisa-elizarova` |
| Пересмотр кредитного рейтинга (средств) сыщиков (врезка) | 10 | `scenario/kholodnyy-urozhay` (advice) |
| Расследование | 10 | `scenario/kholodnyy-urozhay` (hook) |
| Введение в расследование (зацепка 1) | 10 | `scene/vvedenie-zatsepka-1`; `location/upravlenie-nkvd-kuybyshev` |
| Введение в расследование (зацепка 2) | 11 | `scene/vvedenie-zatsepka-2` |
| Большой брат следит за тобой | 11 | `scene/vvedenie-zatsepka-1` (description); `character/beriya` |
| Раздаточный материал 1 (Факты по делу) | 11 | `handout/fakty-po-delu` |
| Раздаточный материал 2 (Донос) | 12 | `handout/donos-smolskoy`; `character/galina-smolskaya` |
| Раздаточный материал 3 (Расчётная запись совхоза) | 12–13 | `handout/raschetnaya-zapis-sovkhoza`; персонажи-жители |
| С участием ГРУ | 13 | `scenario/kholodnyy-urozhay` (advice); `organization/nkvd`; предложение к `mts-kharkov-37-ru/organization/gru-osobyy-otdel-8` |
| Что может агент НКВД? | 13–15 | `organization/nkvd` (description); `scenario/kholodnyy-urozhay` (advice) |
| Паранойя (врезка) | 15 | `scenario/kholodnyy-urozhay` (advice) |
| Преступления и проступки; Преступления; Не считается преступлением | 15–16 | таблица «Преступления и проступки» сценария |
| Обмундирование (врезка; Каждый сыщик имеет; У некоторых исследователей; На грузовике есть; Грузовик ГАЗ АА) | 16–17 | `item/snaryazhenie-agentov`, `item/gruzovik-gaz-aa`, `item/ranets-radio-6-pkd` |
| Путешествие (варианты в дороге) | 17–18 | `scene/puteshestvie`; `location/okrestnosti-kuybysheva` |
| Первый совхоз | 18 | `scene/pervyy-sovkhoz`; `location/sovkhoz-leninskiy-2` |
| Погода (врезка) | 18–19 | `scenario/kholodnyy-urozhay` (advice); `location/okrestnosti-kuybysheva` |
| О Красивом Октябре-3 | 19 | `location/krasivyy-oktyabr-3`; `location/sovkhoz-krasivyy-oktyabr` |
| Почему они не уходят? (врезка) | 20 | `location/krasivyy-oktyabr-3` (description); `location/sovkhoz-krasivyy-oktyabr` |
| Прибытие | 20 | `scene/pribytie` |
| Карта 1, регион Красивого Октября-3 | 21 | `map/karta-regiona` (9 меток) |
| Психология? (врезка) | 22 | `scenario/kholodnyy-urozhay` (advice) |
| Неожиданный визит (Антисоветская деятельность; Абрамовы; Убийца; Совхоз) | 22–23 | `scene/neozhidannyy-vizit` |
| В расследовании на Красивом Октябре-3 | 23 | `scenario/kholodnyy-urozhay` (keeper_info) |
| Необходимые факты: Галина; Ллойгор; Задание | 23–24 | `scenario/kholodnyy-urozhay` (keeper_info); `character/galina-smolskaya`; `creature/lloigor` (legend) |
| Сон | 24 | `scene/son-i-koshmary` |
| Путешествие (поезд «Транспорт 4023», депо) | 24–25 | `scene/poezd`; `location/depo` |
| Кошмары (врезка) | 25 | `scene/son-i-koshmary`; таблица «Кошмары» сценария |
| Пути расследования | 25 | `scenario/kholodnyy-urozhay` (steps) |
| Абрамовы (Пётр; Екатерина; Дмитрий) | 26–27 | `scene/abramovy` |
| Тело | 27 | `scene/telo-galiny`; `item/ikona-vasiliya`, `item/revolver-vasiliya` |
| Взаимодействие с другими совхозами | 27–28 | `scene/drugie-poseleniya`; `location/krasivyy-oktyabr-1`, `location/krasivyy-oktyabr-2`; `character/viktor-demidov` |
| Состояние совхоза | 28–30 | `scene/sostoyanie-sovkhoza` |
| Карта 2 (Krasivyi Oktabyr-3) | 29 | `map/karta-krasivogo-oktyabrya-3` (22 метки) |
| 1. Льняные поля | 30 | `location/ko3-1-lnyanye-polya` |
| 2. Дом Никитиных | 30 | `location/ko3-2-dom-nikitinykh`; `character/andrey-nikitin`, `character/olga-nikitina` |
| 3. Пустой дом | 30 | `location/ko3-3-pustoy-dom` |
| 4. Дом Баршая | 30 | `location/ko3-4-dom-barshay`; `character/aleksandr-barshay`, `character/liviya-barshay` |
| Опиум (врезка) | 30–31 | `item/opium-barshaev` (mechanics) |
| 5. Амбар №1 | 31 | `location/ko3-5-ambar-1`; `item/trotil` |
| 6. Амбар №2 | 31 | `location/ko3-6-ambar-2` |
| 7. Дом Чмилы | 31 | `location/ko3-7-dom-chmily`; `character/svetlana-chmila` |
| 8. Дом Десни | 31 | `location/ko3-8-dom-desni`; `character/filipp-desni`, `magda-desnaya`, `olga-desnaya` |
| 9. Дом Смольских | 31 | `location/ko3-9-dom-smolskikh` |
| 10. Дом Сидорова | 31–32 | `location/ko3-10-dom-sidorova`; `character/simeon-sidorov`, `rada-sidorova`, `anton-sidorov`, `bogdan-sidorov` |
| 11. Дом Жукова | 32 | `location/ko3-11-dom-zhukova`; `character/pavel-zhukov`; `item/broshyura-chego-ozhidat-v-amerike` |
| 12. Дом Кесин | 32 | `location/ko3-12-dom-kesin`; `character/tatyana-kesina`, `character/veniamin-kesin` |
| 13. Дом Лазуткина | 32–33 | `location/ko3-13-dom-lazutkina`; `character/boris-lazutkin`, `character/sofya-lazutkina` |
| 14. Дом Молодина | 33 | `location/ko3-14-dom-molodina`; `character/nikita-molodin`, `character/lyusya-molodina` |
| 15. Дом Абрамова | 33 | `location/ko3-15-dom-abramova` |
| 16. Дом Елизарова | 33 | `location/ko3-16-dom-elizarova` |
| 17. Пруд | 33 | `location/ko3-17-prud` |
| 18. Центр посёлка | 33 | `location/ko3-18-tsentr-poselka` |
| 19. Дом Гапона | 34 | `location/ko3-19-dom-gapona` |
| Телекинез ллойгора и временная линия (Ночь прибытия … День третий) | 34–35 | `scene/telekinez-lloygora`; таблица «Телекинез ллойгора: временная линия» сценария |
| Река | 35–36 | `scene/reka`; `location/reka-samara`, `location/kamennyy-krug` |
| Гипертермия (врезка) | 36 | `scene/reka` (mechanics, errata) |
| Кравчуки | 36–37 | `scene/kravchuki`; `character/kravchuki-i-vitrukiny`, `character/dmitriy-kravchuk`; `location/lager-kravchukov` |
| Уровень работы в совхозе | 37–38 | `scene/uroven-raboty` |
| Пример из тестовой игры (врезка) | 38 | `scenario/kholodnyy-urozhay` (advice) |
| Елизаровы (Андрей; Мария; Раиса) | 38–40 | `scene/elizarovy`; `handout/risunok-raisy` (рисунок с. 39) |
| Демонстрация ллойгора | 40–41 | `scene/demonstratsiya-lloygora` |
| Поезд | 41 | `scene/poezd` |
| Развязка (Ничего не делать; Завершить миссию по депортации; Депортировать всех; Помогите некоторым или всем жителям сбежать; Убить их всех; Объявление совхоза безумным; Вызов подкрепления; Победить ллойгора) | 41–44 | `scenario/kholodnyy-urozhay` (conclusion, награды Рассудка) |
| Отчёт | 44 | `scene/otchet` |
| Действующие личности: Аганин, Абрамовы, Гапон, Смольский, Елизаровы (статблоки) | 44–48 | статблоки соответствующих `character/*` |
| Кравчуки и Витрукины (статблок) | 48 | `character/kravchuki-i-vitrukiny` |
| Ллойгор, Великая внеземная раса; Специальные силы; Ллойгор, мастер телекинеза | 48–50 | `creature/lloigor` (instance_of `coc:creature:lloigor`) |
| Восемь готовых сыщиков (Яров, Мачинко, Шемкова, Буре, Замятин, Ахмеров, Гуков, Кравчук) | 50–60 | существующие `character/*` книги `kholodnyy-urozhay-pregens-ru`: ссылки; источники, биографии (legend), варианты имён и расхождения — в `proposals-coldharvest.json` |
| Глоссарий | 60–61 | таблица «Глоссарий» сценария |
| Интеграция Холодного урожая с другими советскими приключениями (МТС Харьков-37; Тайны Кремля; Тени Ленинграда; Террор) | 61–62 | `scenario/kholodnyy-urozhay` (advice, refs); таблица «Предлагаемая хронология советской кампании» |
| Соединяя даты | 62 | `scenario/kholodnyy-urozhay` (advice); таблица «Соединяя даты: увечья после Лубянки» |
| Плакат «Женщина — вступайте в кооперацию» | 63 | не взято — см. ниже |

## Не взято

- Иллюстрации (обложка с. 1; портреты NPC с. 5–9 — книга советует раздавать их игрокам; «Кошмар в сарае» с. 25;
  «Ллойгор переворачивает ГАЗ АА» и «Стоящие камни» с. 35; «Кравчуки и Витрукины» с. 37; «Разрушенный совхоз» с. 38;
  «Ллойгор нападает на следователей» с. 41; портреты готовых сыщиков с. 51–59; плакат с. 63) — `images` не добавлялись:
  `app/art/` не входит в задание части. Рисунок Раисы (с. 39) — раздатка `handout/risunok-raisy` с пересказом.
- Статблоки готовых сыщиков (с. 51–60) — сыщики уже в базе по листам готовых персонажей; сравнены только
  характеристики и ПМ (расхождения — errata в предложениях), навыки построчно не сверялись.
- Эпиграф из «Возвращения ллойгора» Колина Уилсона (с. 48–49) — пересказан в legend существа, цитатой не взят.

## Опечатки и сомнения книги (в errata записей)

- Магические очки NPC почти у всех не следуют из МОЩ (Аганин, Абрамовы, Гапон, Василий, Андрей, Раиса); Раиса: драка
  25% (15/5) — половина исправлена на 12; Кравчуки: ПЗ 14 (ожидалось 12), уклонение напечатано как «Ловкость».
- Ллойгор: «ОБР 135» при «МОЩ —» и «обладает только ОБР, ИНТ и ЛВК» (вероятно, МОЩ); БкУ +5d6 и Комплекция 6 при
  СИЛ+ТЕЛ 500; потеря «0/1d4 МАГИИ» при мысленном контакте.
- «Гипертермия» вместо переохлаждения; бодрствование проверяется «ТЕЛ»; вытаскивание грузовика — «против РАЗМЕРА».
- Кабина ГАЗ АА: двое (с. 16) / трое (с. 17); бензина (80 л) не хватает на 200 км без заправки в «Ленинском-2».
- Блок характеристик Максима Кравчука в сценарии — копия блока Гукова; у остальных сыщиков ОБР/ИНТ/МОЩ расходятся с
  листами готовых персонажей.
- Возрасты и отчества жителей в расчётной записи и в тексте расходятся (Пётр 32/39, Раиса 8/10, Антон 13/15, Богдан
  11/13, Вениамин 1/3, Жуков 59/61, Чмила 46/48, Симеон 34/«за 40», Галина 51/«под сорок»; Мария Андроновна/Андровна/
  Мариновна); время бегства Кравчуков — два/четыре/шесть месяцев; давность последнего отчёта — два/четыре месяца;
  «Харьков-47» в хронологии; «Холодная жатва» и «Красный Октябрь» наряду с основными названиями.
