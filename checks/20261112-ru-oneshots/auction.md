# «Аукцион» (`auktsion-ru`) — сверка переноса (часть auction)

Источник — фанатский перевод (`[RU-фан 7e]`, издание `trusted`, Р-227) сценария Рэнди МакКолла «The Auction» (сборник
«The Asylum & Other Tales», Chaosium, 1983) с «мелкими доработками и адаптацией для 7-й редакции» (Hort). PDF 48 страниц с
текстовым слоем; статблоки, таблица ставок и оба плана сверены по изображениям страниц. Статблоки — в формате 7-й редакции
(проценты с долями), `ruleset` core. Действие — Вена после Первой мировой, до введения шиллинга (1920-е); `axes.era` —
`1920s`. Русский текст — источник; флаг `translated` не ставился (перевод не наш; так же у `pobeg-iz-innsmuta-ru`).

## Страницы

Номеров страниц в книге нет: **печатная = физическая** (смещение 0). Без текста: с. 48 (план дома Аспергов для игроков
и герб Аспергов).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Аукцион (титул: автор, оригинал, перевод) | 1 | сценарий `auktsion-ru/scenario/auktsion` (summary) |
| От переводчика | 1 | сценарий: advice |
| Вступление | 1–2 | сценарий: hook, keeper_info; сцена `…/scene/podgotovka`; `…/character/ser-martin-myurrey`, `…/character/dzhordzh-uolker` |
| Историческая справка | 2 | город `coc:location:vienna` (history) |
| Информация для сыщиков; Каталог | 2 | сцена `podgotovka`; раздатка `…/handout/katalog-aukciona` |
| Дом Аспергов | 3 | организация `…/organization/dom-aspergov`; сцена `podgotovka` |
| Путешествие и размещение | 3–4 | сцена `podgotovka`; таблица «Жильё в Вене» у `coc:location:vienna` (в сценарии — ссылка `from`); сцена `…/scene/vizit-v-aspergkhaus` |
| Финансовый кризис | 4 | сцена `podgotovka`; `coc:location:vienna` |
| Фредерик Альберт Асперг | 4 | `…/character/frederik-albert-asperg`, `…/character/leopold-gruber`, `…/character/otto-felber`; сцена `vizit-v-aspergkhaus` |
| Аукционные лоты (вводный абзац, Венская библиотека) | 5 | сцена `vizit-v-aspergkhaus`; сценарий: таблица «Аукционные лоты» (16 строк) |
| Лот №1 — Анкх, египетский | 5 | `…/item/lot-1-krovavyy-ankh` |
| Лот №2 — Манускрипт Бет Элохим | 5–6 | книга `…/tome/manuskript-bet-elokhim` |
| Лот №3 — Разное | 6 | `…/item/lot-3-ritualnye-predmety` |
| Лот №4 — Рука славы | 6 | `…/item/lot-4-ruka-slavy` |
| Лот №5 — Разное | 7 | `…/item/lot-5-fetish-i-baraban` |
| Лот №6 — «Волхв» | 7 | книга `…/tome/volkhv` |
| Лот №7 — Меч | 7–8 | `…/item/lot-7-mech-paratselsa` |
| Лот №8 — Череп, человеческий | 8 | `…/item/lot-8-cherep-chasha` |
| Лот №9 — Бронзовая голова | 8–9 | `…/item/lot-9-bronzovaya-golova` |
| Служитель Головы (статблок, особые свойства, броня, потеря рассудка) | 9–10 | существо `…/creature/sluzhitel-golovy` (`instance_of` `coc:creature:servitor-of-outer-gods`) |
| Лот №10 — Палочки и-цзинь | 10 | `…/item/lot-10-palochki-i-tszin` |
| Лот №11 — «Книга закона» | 10 | книга `…/tome/kniga-zakona` |
| Лот №12 — «Чудеса в новоанглийском Канаане» | 10 | общая книга `coc:tome:thaumaturgical-prodigies-in-the-new-england-canaan` — экземпляр в `copies` и псевдоним (предложения); строка таблицы лотов сценария |
| Лот №13 — Разное | 11 | `…/item/lot-13-medalony` |
| Лот №14 — «Dictionaiire Infernal» | 11 | книга `…/tome/adskiy-slovar` |
| Лот №15 — Лекарский мешочек шамана | 11 | `…/item/lot-15-lekarskiy-meshochek` |
| Лот №16 — Кольцо, золотое | 11–12 | `…/item/lot-16-koltso-solomona` |
| Аукцион (банкет, этикет) | 12 | сцена `…/scene/banket-i-gosti`; место `…/location/aspergkhaus-zelenaya-komnata` |
| Гости аукциона | 12 | сцена `banket-i-gosti` |
| Леди Маргарет Джеймсон (статблок) | 12–13 | `…/character/ledi-margaret-dzheymson` |
| Мишель де Борсавен (статблок) | 13 | `…/character/mishel-de-borsaven` (способность «Спиритический сеанс») |
| Сэр Мартин Мюррей | 13 | `…/character/ser-martin-myurrey` |
| Граф Николай Тычевский | 14 | `…/character/nikolay-tychevskiy`; `…/character/naemnye-golovorezy` (группа) |
| Лешек Чернин | 14 | `…/character/leshek-chernin` |
| Джордж Уолкер | 14 | `…/character/dzhordzh-uolker` |
| Клаус Хундерпрест (среди гостей) | 14 | `…/character/klaus-khunderprest` |
| Дарнел Колсон | 14 | `…/character/darnel-kolson` |
| Таблица ставок (символы, сетка 8 гостей × 16 лотов) | 15 | сценарий: таблица «Таблица ставок» (8 строк, символы в intro); сцена `…/scene/khod-torgov` |
| Ход аукциона и убийство | 15–17 | сцены `khod-torgov`, `…/scene/ubiystvo`; места `…/location/aspergkhaus-sluzhebnaya-komnata`, `…/location/aspergkhaus-khranilishche-s-prolomom`; `…/character/frants-mayrkhofer`, `…/character/anton-khuber`, `…/character/paul-vinkler`; предмет `…/item/domkraty` |
| Осмотр Аспергхауса | 17–18 | места `…/location/aspergkhaus`, `…-podval`, `…-pervyy-etazh`, `…-kabinet-asperga`, `…-vtoroy-etazh` |
| План дома Аспергов (подвал, первый и второй этажи) | 18, 48 | карта `…/map/plan-doma-aspergov` (`app/maps/auction-plan-doma-aspergov.jpg`, 40 меток на все подписи) |
| Полиция (три сведения, свидетель) | 18–19 | сцена `…/scene/politsiya`; таблица «Разговоры полицейских» сценария; `…/character/venskaya-politsiya` (группа); место `…/location/kladbishche-das-tor` |
| Расследование | 19–20 | сцена `…/scene/rassledovanie-uliki` |
| Улики на месте преступления | 20 | сцена `rassledovanie-uliki`; предмет `…/item/obrazets-tkani-iz-pod-nogtey`; место `…/location/venskiy-universitet` |
| Подземный ход | 20 | сцена `…/scene/podzemnyy-khod`; место `…/location/tonneli-pod-venoy` |
| Подозреваемые | 20–21 | сцена `…/scene/podozrevaemye`; `…/character/karl-prust` |
| Клаус Хундерпрест (описание, статблок, мотив, «Liber Tenebrea», сведения 1–4, ювелиры, допрос, похищение) | 21–23 | `klaus-khunderprest`; организация `…/organization/kult-germesa-khtoniusa`; книга `…/tome/liber-tenebrea`; сцены `…/scene/svedeniya-o-khunderpreste`, `…/scene/pokhishchenie`; таблица «Сведения о Хундерпресте» сценария; раздатка `…/handout/anonimnoe-poslanie`; предмет `…/item/grob-dlya-plennikov`; `…/character/ida-khunderprest` |
| Жилище Хундерпреста (Либерман, Хорст, Дорнхайм, ночные прогулки, полиция) | 23–25 | сцены `…/scene/dom-na-folshtrasse`, `…/scene/nochnaya-progulka`; место `…/location/dom-na-pervoy-folshtrasse`; `…/character/adolf-liberman`, `…/character/rudolf-khorst`, `…/character/volfgang-dornkhaym` |
| Окрестности | 25 | сцена `…/scene/foltassebar` |
| Фольтассебар; Пьяный задира (статблок) | 25–27 | сцена `foltassebar`; место `…/location/foltassebar`; `…/character/pyanyy-zadira` (типаж), `…/character/yozef-pikhler` |
| Лекарь | 27 | сцена `…/scene/lekar`; `…/character/vilgelm-ferkhamm` |
| Квартира Хундерпреста | 27–29 | сцена `…/scene/kvartira-khunderpresta`; место `…/location/kvartira-khunderpresta`; предмет `…/item/koltso-s-palcem` |
| План «Квартира Хундерпреста и тайное подземелье» | 28 | карта `…/map/kvartira-khunderpresta` (`app/maps/auction-kvartira-khunderpresta.jpg`, 13 меток) |
| Подземелье | 29–30 | сцены `…/scene/podzemele`, `…/scene/labirint-tunneley`; места `…/location/grobnitsa-khunderpresta`, `…/location/sklep-idy`, `…/location/peshchera-upyrey`; предметы `…/item/sunduchok-mogilnykh-dragotsennostey`, `…/item/chernye-plashchi` |
| Упырь 1–4 (статблоки, бой, особые способности, навыки, броня) | 30–31 | существо `…/creature/upyri-khunderpresta` (4 варианта, `instance_of` `coc:creature:ghoul`) |
| Итоги сценария | 31 | сцена `…/scene/itogi`; сценарий: conclusion; предмет `…/item/koltsa-aspergov` |
| Карточки лотов №1–16 (приложение) | 32–47 | раздатка `katalog-aukciona` (текст всех 16 карточек); записи лотов (sources) |
| План дома Аспергов (для игроков), герб Аспергов | 48 | карта `plan-doma-aspergov` (картинка отсюда) |

## Записи (93: 92 в книге + город) и картинки (2)

- сценарий 1: `auktsion`;
- сцены 19: `podgotovka`, `vizit-v-aspergkhaus`, `banket-i-gosti`, `khod-torgov`, `ubiystvo`, `politsiya`, `rassledovanie-uliki`,
  `podzemnyy-khod`, `podozrevaemye`, `svedeniya-o-khunderpreste`, `dom-na-folshtrasse`, `nochnaya-progulka`, `foltassebar`, `lekar`,
  `pokhishchenie`, `kvartira-khunderpresta`, `podzemele`, `labirint-tunneley`, `itogi`;
- город 1 (общий, новый): `kb/locations/vienna.json` (`coc:location:vienna`, таблица «Жильё в Вене»);
- места 17: `aspergkhaus`, `aspergkhaus-podval`, `aspergkhaus-khranilishche-s-prolomom`, `aspergkhaus-pervyy-etazh`,
  `aspergkhaus-kabinet-asperga`, `aspergkhaus-vtoroy-etazh`, `aspergkhaus-zelenaya-komnata`, `aspergkhaus-sluzhebnaya-komnata`,
  `dom-na-pervoy-folshtrasse`, `kvartira-khunderpresta`, `grobnitsa-khunderpresta`, `sklep-idy`, `peshchera-upyrey`,
  `kladbishche-das-tor`, `foltassebar`, `venskiy-universitet`, `tonneli-pod-venoy`;
- карты 2: `plan-doma-aspergov`, `kvartira-khunderpresta` (`app/maps/auction-plan-doma-aspergov.jpg`, `auction-kvartira-khunderpresta.jpg`);
- персонажи 24: со статблоком `ledi-margaret-dzheymson`, `mishel-de-borsaven`, `klaus-khunderprest`, `pyanyy-zadira` (типаж);
  без статблока `frederik-albert-asperg`, `ser-martin-myurrey`, `nikolay-tychevskiy`, `leshek-chernin`, `dzhordzh-uolker`,
  `darnel-kolson`, `karl-prust`, `ida-khunderprest`, `adolf-liberman`, `rudolf-khorst`, `volfgang-dornkhaym`, `vilgelm-ferkhamm`;
  с придуманным именем (Р-150, `editorial_text`) `leopold-gruber` (мажордом), `otto-felber` (секретарь), `frants-mayrkhofer`
  (убитый ассистент), `anton-khuber` (второй ассистент), `paul-vinkler` (ассистент при сыщиках), `yozef-pikhler` (завсегдатай
  «Кружки»); группы с `names` (Р-151) `venskaya-politsiya`, `naemnye-golovorezy`;
- существа 2: `sluzhitel-golovy`, `upyri-khunderpresta`;
- организации 2: `dom-aspergov`, `kult-germesa-khtoniusa`;
- книги 5: `manuskript-bet-elokhim`, `volkhv`, `kniga-zakona`, `adskiy-slovar` (оккультные), `liber-tenebrea` (Мифы);
- предметы 18: лоты №1, 3, 4, 5, 7, 8, 9, 10, 13, 15, 16; `obrazets-tkani-iz-pod-nogtey`, `domkraty`, `koltso-s-palcem`,
  `sunduchok-mogilnykh-dragotsennostey`, `chernye-plashchi`, `grob-dlya-plennikov`, `koltsa-aspergov`;
- раздатки 2: `katalog-aukciona`, `anonimnoe-poslanie` (пересказ, Р-130).

## Опечатки и сомнения

- Таблица ставок (с. 15): текст обещает для каждого гостя общую сумму и «потолок» за лот, но в таблице их нет — только
  пример леди Маргарет (£1600 / £500). Errata в сценарии; Хранитель задаёт суммы сам.
- Джордж Уолкер: во вступлении (с. 1) ему нужны лоты №6, 7, 12 и 15, а в таблице ставок против лота №6 у него «-» (errata).
- Служитель Головы: БкУ 0 при СИЛ 70 + ТЕЛ 65 = 135 и Комплекции 1 — исправлено на +1d4 по большинству (Р-36, `corrections`);
  ПЗ 15 при (ВЫН 75 + ТЕЛ 65)/10 = 14 — как напечатано (errata). Урон щупальца 2d6 — без БкУ, как напечатано.
- Пьяный задира: Скорость 9 (по правилам 8) и ПМ 19 при МОЩ 45 (должно быть 9; видимо, перенесено из статблока Хундерпреста) —
  errata, как напечатано. Кастет 1d3+1d4+2 против 1d3+1+БкУ таблицы оружия — `source_variants` оружия (предложение, Р-124).
- Лот №10: «шесть палочек» (с. 10) против «пятнадцати» на карточке (с. 41) — errata.
- Лот №14: «Dictionaiire Infernal» (опечатка во французском, с. 11 и 45) — как напечатано; «Адский словарь» (с. 11) / «Словарь ада» (с. 45) — псевдонимы.
- Асперг один раз «Аусперг» (с. 16), на гербе — «AUSPERG» (с. 48); Мишель де Борсавен на с. 21 — «Майкл» (errata, псевдонимы).
- Лот №12 (общая книга): сценарий даёт свои числа экземпляра (+5% Мифов, 1d6 Рассудка, без заклинаний; «начало XVIII века»)
  против «Книги хранителя» (+1/+3%, 1788(?)) — только в `copies`, справочник не меняется.
- ПЗ леди Маргарет и Мишеля (8,5 → 9) и упыря 3 (10,5 → 11) округлены вверх, Скорость Хундерпреста без возрастной поправки — приёмы книги (Р-161).
- Меры: 600 миль Гамбург — Вена → «около 960 км»; «кварта крови» → «не меньше литра» (Р-64, пометки в записях); дюймы
  размеров лотов не взяты.
- «WC» на плане квартиры стоит там, где текст описывает ванную («напротив кухни»); метка ведёт на квартиру с пояснением.

## Не взято

- Иллюстрации: голова (с. 8), Служитель (с. 9), картинки шестнадцати карточек лотов (с. 32–47), герб Аспергов (с. 48) —
  папка `app/art/` вне моей части; кандидаты для `images` (`pipeline/art/add_images.py`). Папка владельца
  `3_КБ\Ваншоты\1920 Аукцион` — только `_паспорт.md` и `_карточка.md`, картинок нет.
- Условные обозначения планов (лестницы, шахты лифтов, двери), розы ветров и масштаб «3 м» — без меток.
- Упомянутые исторические лица без роли в сюжете — Теософ Великий, донья Мария Спендоса, Уинстон Рис-Смит, Фрэнсис Баррет,
  Парацельс, Роджер Бэкон, Алистер Кроули, Айвасс, Коттон Мэтер, преп. Уорд Филиппс, Жак Коллен, Распутин, царь Соломон —
  остаются текстом в записях лотов и персонажей.
- Фоновые безымянные без роли и параметров: струнный квартет, французский шеф-повар и австрийский кондитер, остальные слуги,
  нанятый химик (£3 в день), венские ювелиры, брат завсегдатая (пропавший грабитель), бездомные в канализации — текстом в сценах.
- Места без своего материала: Венская библиотека, городской архив, Гофбург, Гамбург, прежняя квартира Хундерпреста, четыре
  других осквернённых кладбища — текстом в сценах и у города.
- Заклинание освобождения Служителя («призыв могущественного существа из пустоты») — книга не называет его и не даёт механики;
  новой записи заклинания не заводилось, текст — у бронзовой головы и Служителя.

## Кандидаты в новые записи (вне моей части)

- Божество «Гермес Хтониус» — книга не связывает его с известным божеством Мифов; пока имя в организации `kult-germesa-khtoniusa`.
- Алистер Кроули — реальное лицо, упоминается и в других книгах базы; общей записи персонажа нет.

## Предложения

`proposals-auction.json` — 8 правок в 7 записях (пробный прогон `apply.py --dry-run` проходит): фанатские формы в псевдонимы
`coc:spell:contact-ghoul` («Связь с упырями»), `coc:spell:contact-nyogtha` («Связь с Ньогтой»), `coc:spell:contact-ygolonac`
(«Связь с Й`Голонаком»), `coc:spell:voorish-sign` («Знамение Вуриш»), `coc:creature:hound-of-tindalos` («Гончая Тиндалоса»);
экземпляр лота №12 и псевдоним «Чудеса в новоанглийском Канаане» у `coc:tome:thaumaturgical-prodigies-in-the-new-england-canaan`;
вариант урона кастета у `coc:weapon:brass-knuckles`. «Знак Древних» у `coc:spell:elder-sign` уже есть.
