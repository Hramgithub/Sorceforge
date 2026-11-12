# «Рождественская вечеринка» (`rozhdestvenskaya-vecherinka-ru`) — сверка переноса (часть christmas)

Источник — официальное русское издание (`[RU 7e]`, Вадим Первухин, конкурс коротких приключений Hobby Games),
PDF 20 страниц, скан без текстового слоя (вёрстка «в кривых»): распознавание tesseract (`-l rus`, 200 dpi), каждое число
и статблок сверены по изображению страницы (спорные места — 400 dpi). Правила — 7-я редакция, `ruleset` core; действие —
24 декабря 1922 года, Новый Орлеан (`axes.era` 1920s).

Заметка владельца (`3_КБ\Ваншоты\1922 Рождественская вечеринка\_паспорт.md`) называет местом действия «портовый город
восточного побережья (аналог Бостона или Нью-Йорка)» — по книге это Новый Орлеан; записи сделаны по книге.

## Страницы

Номеров страниц в книге нет: **печатная = физическая** (смещение 0), в `sources` `printed_page` = `physical_page`.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Рождественская вечерника 28:28», Вадим Первухин | 1 | сценарий `rozhdestvenskaya-vecherinka-ru/scenario/rozhdestvenskaya-vecherinka` (summary, aliases, errata названия) |
| Введение | 2 | сценарий: summary, advice (болезнь); город `coc:location:new-orleans` |
| Уровень подготовки сыщиков | 2 | сценарий: summary, advice |
| Вовлечение сыщиков; Место действия | 2 | сценарий: hook; сцена `…/scene/v-bolnitse-la-salle`; `…/location/bolnitsa-la-salle` |
| Доктор Оливер Баренфельд (врезка) | 3 | сцена `v-bolnitse-la-salle`; `…/character/oliver-barenfeld`; предмет `…/item/rezultaty-obsledovaniya` |
| Болезни (d8) | 3 | сценарий: таблица «Болезни» |
| «По прошествии игрового часа…», подготовка к вечеру | 3 | сцена `v-bolnitse-la-salle`; сценарий: advice |
| Дом 28 на Бэнкфорд драй | 4 | `…/location/benkford-dray`, `…/location/dom-28-na-benkford-dray`, `…/location/dom-28-banketnyy-zal`; сцена `…/scene/vecherinka-u-stounov`; `…/item/avtobus-s-krasnym-krestom`; дворецкий `…/character/ogyust-dyupre`, охранник `…/character/dzho-landri` |
| Артур Стоун | 4 | `…/character/artur-stoun` |
| Айрис Стоун | 4–5 | существо `…/creature/ninkhursag` (псевдоним «Айрис Стоун»; описание, способность «ИГРА») |
| Маргарет Питчфорд | 5 | `…/character/margaret-pitchford`; сцены `vecherinka-u-stounov`, `rech-artura` |
| Дональд Бонс | 5 | `…/character/donald-bons`; сцена `…/scene/konflikt-s-donaldom`; `…/item/zapiska-s-adresom-priyuta` |
| Пол | 5 | `…/character/pol` |
| Мадам Роза | 5 | `…/character/madam-roza`; `…/location/dom-28-komnata-madam-rozy` |
| Гадание (1. На любовь; 2. На богатство; 3. На будущее) | 6 | сцена `…/scene/gadanie-madam-rozy` (расклады — в описании, errata «только два») |
| Хранителю: (врезка о Нинхурсаг) | 6 | сценарий: keeper_info; существо `ninkhursag`: legend |
| Речь Артура; Артур продолжает | 6–7 | сцена `…/scene/rech-artura` |
| Игра (правила, вопросы из ящиков «2» и «8») | 7 | `…/item/yashchiki-igry` (правила); сценарий: таблицы «Вопросы из ящика «2»», «Вопросы из ящика «8»»; сцена `…/scene/igra` |
| Комнаты в доме (банкетный зал, каминная, кухня, задний двор, второй этаж, кабинет) | 7 | сцена `…/scene/komnaty-v-dome`; места `dom-28-banketnyy-zal`, `dom-28-kaminnaya-komnata`, `dom-28-kukhnya`, `dom-28-zadniy-dvor`, `dom-28-vtoroy-etazh`, `dom-28-kabinet`; `…/item/gruzovik-s-bochkami`, `…/item/dnevnik-artura-stouna`; кухарка `…/character/meybl-tibodo` |
| Нападение на Айрис Стоун | 8 | сцена `…/scene/napadenie-na-ayris`; `…/item/okrovavlennyy-nozh`; `…/location/dom-28-terrasa`, `…/location/politseyskiy-uchastok` |
| Поиск улик (1–3) | 8 | сцена `…/scene/poisk-ulik`; сценарий: таблица «Поиск улик»; `…/location/biblioteka-novogo-orleana`; `…/item/pismo-s-adresom-tsyganskoy-stoyanki`, `…/item/listy-iz-carne-de-aruru` |
| Информация для Хранителя | 8–9 | сценарий: keeper_info; сцена `poisk-ulik` |
| История Артура и Анны Стоун (официальная / неофициальная часть) | 9 | сценарий: keeper_info; `…/character/anna-stoun`; `…/organization/kompaniya-stounov` |
| Свидетели (1–5) | 9 | сценарий: таблица «Свидетели»; администратор `…/character/edgar-leblan` |
| Грегори Чейз; подпись «Обиталище Грегори Чейза» | 9–10 | `…/character/gregori-cheyz`; `…/location/kvartira-gregori-cheyza`; сцена `…/scene/obitalishche-gregori-cheyza` |
| Ветераны инвалиды; Возможные события; подпись «Яма» | 10 | `…/organization/veterany-invalidy`; `…/character/serzhant-tompson`, `…/character/kapral-khartman`; `…/location/trushchoby-v-portu`, `…/location/razrushennyy-portovyy-sklad`; сцена `…/scene/veterany-invalidy` |
| Рассел Доусон; Выйти на него можно | 10–11 | `…/character/rassel-douson`; сцена `…/scene/rassel-douson`; сценарий: таблица «Как выйти на Рассела Доусона» |
| Заброшенный детский приют | 11 | `…/location/zabroshennyy-detskiy-priyut`; сцена `…/scene/zabroshennyy-priyut`; `…/character/mark`, `…/character/sara` |
| Цыгане | 11 | `…/organization/tsyganskaya-obshchina`; `…/location/okrestnosti-novogo-orleana`, `…/location/tsyganskiy-lager`; сцена `…/scene/tsygane` |
| Нинхурсаг, Нинмах, Аруру, Бау, Нинту | 11 | существо `…/creature/ninkhursag` (legend, description) |
| Доктор Ральф Хэндж в «Чистилище» | 11–12 | `…/location/morg-chistilishche`; `…/character/ralf-khendzh`; сцена `…/scene/morg-chistilishche`; `…/item/zapisi-khendzha` |
| Финал | 12 | сцена `…/scene/final`; сценарий: conclusion |
| Победят ли сыщики Нинхурсаг или сбегут? | 12 | сцена `final`; сценарий: conclusion |
| Carne de Aruru, Плоть Аруру (врезка) | 12 | книга `…/tome/carne-de-aruru` |
| Награды | 13 | сценарий: conclusion |
| Персонажи Хранителя и чудовища: Артур Стоун | 13 | статблок `artur-stoun` |
| Дональд Бонс | 13 | статблок `donald-bons` |
| «Генерал Кусака» и другие зомби в сценарии | 14 | существо `…/creature/general-kusaka-i-zombi` (`instance_of` `coc:creature:zombie`, свой профиль Р-75; `spawn_of` Хэндж) |
| Доктор Ральф Хэндж | 14 | статблок `ralf-khendzh` |
| Грегори Чейз | 14 | статблок `gregori-cheyz` |
| Рассел Доусон | 14–15 | статблок `rassel-douson` |
| Нинхурсаг (статблок, «Заклинания»: Зов, Телепортация, Кормление) | 15 | существо `ninkhursag`: statblock, abilities |
| Пригласительное письмо (две стороны) | 16 | раздатка `…/handout/priglasitelnoe-pismo`; карта `…/map/priglashenie-skhema-proezda` (`app/maps/christmas-priglashenie-skhema.jpg`, 10 меток) |
| План первого этажа дома Стоунов | 17 | карта `…/map/plan-pervogo-etazha` (`app/maps/christmas-plan-pervogo-etazha.jpg`, 11 меток на все подписи) |
| План второго этажа дома Стоунов | 18 | карта `…/map/plan-vtorogo-etazha` (`app/maps/christmas-plan-vtorogo-etazha.jpg`; подписей нет — меток нет) |
| Трущобы в порту | 19 | карта `…/map/trushchoby-v-portu` (`app/maps/christmas-trushchoby-v-portu.jpg`; подписей нет, 1 вычисленная метка на складе) |
| Морг | 20 | карта `…/map/morg` (`app/maps/christmas-morg.jpg`; 1 метка «parking») |

## Записи (78 файлов)

- город 1 (общий, новый): `kb/locations/new-orleans.json`;
- сценарий 1: `rozhdestvenskaya-vecherinka`;
- сцены 16: `v-bolnitse-la-salle`, `vecherinka-u-stounov`, `konflikt-s-donaldom`, `gadanie-madam-rozy`, `rech-artura`, `igra`,
  `komnaty-v-dome`, `napadenie-na-ayris`, `poisk-ulik`, `obitalishche-gregori-cheyza`, `veterany-invalidy`, `rassel-douson`,
  `zabroshennyy-priyut`, `tsygane`, `morg-chistilishche`, `final`;
- места 20: `benkford-dray`, `dom-28-na-benkford-dray`, `dom-28-banketnyy-zal`, `dom-28-kaminnaya-komnata`, `dom-28-kukhnya`,
  `dom-28-zadniy-dvor`, `dom-28-terrasa`, `dom-28-vtoroy-etazh`, `dom-28-kabinet`, `dom-28-komnata-madam-rozy`,
  `bolnitsa-la-salle`, `morg-chistilishche`, `biblioteka-novogo-orleana`, `politseyskiy-uchastok`, `kvartira-gregori-cheyza`,
  `trushchoby-v-portu`, `razrushennyy-portovyy-sklad`, `zabroshennyy-detskiy-priyut`, `okrestnosti-novogo-orleana`,
  `tsyganskiy-lager`;
- карты 5 (картинки `app/maps/christmas-*.jpg`);
- персонажи 18: со статблоком `artur-stoun`, `donald-bons`, `gregori-cheyz`, `rassel-douson`, `ralf-khendzh`; без статблока
  `anna-stoun`, `oliver-barenfeld`, `margaret-pitchford`, `pol`, `madam-roza`, `serzhant-tompson`, `kapral-khartman`, `mark`,
  `sara`; безымянные с придуманными именами (Р-150, `editorial_text`) `ogyust-dyupre` (дворецкий), `dzho-landri` (охранник),
  `meybl-tibodo` (слепая кухарка), `edgar-leblan` (администратор детского отделения);
- существа 2: `ninkhursag`, `general-kusaka-i-zombi`;
- предметы 10: `rezultaty-obsledovaniya`, `yashchiki-igry`, `okrovavlennyy-nozh`, `dnevnik-artura-stouna`,
  `pismo-s-adresom-tsyganskoy-stoyanki`, `listy-iz-carne-de-aruru`, `zapiska-s-adresom-priyuta`, `gruzovik-s-bochkami`,
  `avtobus-s-krasnym-krestom`, `zapisi-khendzha`;
- книга Мифов 1: `carne-de-aruru`; раздатка 1: `priglasitelnoe-pismo`; организации 3: `veterany-invalidy`,
  `tsyganskaya-obshchina`, `kompaniya-stounov`.

## Опечатки и выводы

- Название: «Рождественская вечерника» на обложке и во всех колонтитулах; на приглашении — «Вечеринка». Запись —
  «Рождественская вечеринка», напечатанное — в псевдонимах и errata.
- Артур Стоун (с. 13): ПЗ 20 (по ВЫН 70 + ТЕЛ 70 — 14), ПМ 11 (по МОЩ 45 — 9), драка «1d4+1d4» (по правилам 1d3 + БкУ) —
  как напечатано, errata.
- Ральф Хэндж (с. 14): «Ближний бой (драка) 45% (42/9)» — половина 22, исправлено (Р-35). ПЗ 12 — округление вверх (Р-161).
- Грегори Чейз (с. 14): драка «55% (26/11)» — половина 27, исправлено (Р-35); ПМ 11 (по МОЩ 40 — 8) и Скорость 5 (по
  правилам 7; возможно, из-за отсутствия ступни) — как напечатано, errata. Уклонение «22% (1¼)» — дробь 11/4 набрана
  лигатурой, в записи «22% (11/4)».
- Рассел Доусон (с. 14–15): БкУ «+2d4» (по СИЛ 85 + ТЕЛ 70 — +1d4; такого значения в таблице нет), ПЗ «39 (+5 за раунд)»
  (по правилам 16; вероятно, задуманное бессмертие), Скорость 8 (по правилам 9) — как напечатано, errata.
- Нинхурсаг (с. 15): ПЗ 28 (по ВЫН 90 + ТЕЛ 95 — 18); БкУ +1d6 и Комплекция 2 согласны между собой, но по СИЛ 130 + ТЕЛ 95
  = 225 должно быть +2d6 и 3 — большинства нет (Р-36), как напечатано, **вопрос владельцу** (`needs_review: true`).
- «Генерал Кусака» и зомби (с. 14): ПЗ 15 (по правилам 14, округление вверх) — не опечатка.
- Гадание (с. 6): «раскладов может быть только два», а напечатано три — errata в сцене.
- Капрал «Хатрман» и «Хартман» на одной странице (с. 10) — запись «Хартман», errata.
- Мелкие разночтения в псевдонимах: «Бэнкфорд / Бэнкфорт / Бэнкрофт драй», «Ла Салл’е / Ла Салле / Ла Салл»,
  «Питчфорд / Пичфорд»; «Литапедион» → «литопедион» (Р-39).
- Выводы (Р-41): «старший брат» Анны — Грегори Чейз; метка «Зал» плана — банкетный зал; разрушенное здание на карте трущоб —
  склад ветеранов; головы животных — трофеи сафари Артура; пальцы Маргарет — плата за ИГРУ; оружие статблоков — по
  совпадению урона с таблицей (дробовик 16-го калибра, винтовка .22, револьвер .32, маленький нож).
- Противоречие без правки: в тексте Бэнкфорд драй идёт по набережной Миссисипи, а на схеме приглашения улица Bancroft Dr
  стоит у водоёма за бульваром Уиснер.

## Не взято

- Иллюстрации: «Стоуны» (с. 4), «Роза» (с. 6), «Дом Стоунов» (с. 8), «Обиталище Грегори Чейза» (с. 9), «Яма» (с. 10),
  украшения (листья, свиток) — папка `app/art/` не входит в мою часть; картинки можно добавить `pipeline/art/add_images.py`
  при сведении.
- Колонтитул «Приключение написано в рамках конкурса коротких приключений Hobby Games» — только в summary сценария.
- Толстый конверт с деньгами Артура, кольцо с красным камнем Айрис, горючая смесь Грегори, саквояж Маргарет — мелочи без
  механики, остались текстом в сценах и записях персонажей.
- Пропавшая дочь Рассела, отец ветерана, мама Пола, начальник полиции, «командир» ветеранов, официанты, музыканты —
  упомянуты мимоходом, остались текстом (имён и характеристик нет).
- Дом Маргарет Питчфорд и жильё Рассела в трущобах — без описания в книге, остались текстом.
- Река Миссисипи — записи в базе нет, не заведена (только набережная в тексте).
- Обрезанные подписи схемы приглашения («Сейн…», «Рив…», «Гран…», второй ярлык Сейнт-Бернард-авеню) — без меток.

## Кандидаты в новые записи (вне моей части)

- Заклинания (`kb/spells`, черновики — в отчёте): «Разговор с кровавой богиней», «Анафема демону» (аналог «Изгнания Йде
  Итад»), «Зов», «Телепортация», «Кормление» (у Нинхурсаг). Механика есть только у трёх последних (способности Нинхурсаг).
- Новый Орлеан заведён общим городом (`kb/locations/new-orleans.json`); его упоминают и записи «Стартового набора» («На
  краю тьмы», «Танец мертвеца») — им можно добавить ссылку на город при сведении.

## Предложения

`proposals-christmas.json` — пусто: общие записи не меняются.
