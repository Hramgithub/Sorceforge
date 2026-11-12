# «Подземка» (podzemka-ru) — сверка покрытия

Книга: сценарий «Подземка», 12 страниц PDF с текстовым слоем (метка владельца «[RU 7e]»; автор в PDF не назван). Все
числа и карта сверены по изображениям страниц. Система — «Зов Ктулху» 7-й редакции, ядро (проценты с половиной и пятой,
Комплекция, БкУ, ПМ): `ruleset: "core"`. Эпоха — «современность» (с. 2: «Монреаль, Канада, современность»; гоу-про,
видеоблог; станция законсервирована в 1992 году) — `era: ["modern"]`; год «1990» в каталоге владельца книгой не
подтверждается. Фраза «В оригинале место действия — Монреаль» может значить, что текст — пересказ чужого сценария;
оригинал не найден.

Страницы: номеров на страницах нет, печатная = физическая (смещение 0). Физ. 1 — титул с двумя картинками,
физ. 12 — карта.

Префикс записей: `podzemka-ru/`. Общий город — `coc:location:montreal` (новый, `kb/locations/montreal.json`): других
записей Монреаля в базе нет, другие части этого плана в Монреале не происходят.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул «Подземка» | 1 | `scenario/podzemka` (name, sources) |
| О сценарии | 2 | `scenario/podzemka` (summary, hook, advice); `coc:location:montreal` |
| Особенности метро Монреаля | 2 | `location/metro-monrealya`; `coc:location:montreal`; `scenario/podzemka` (advice) |
| Блогер-диггер Ляо Хан… (задержание, КСРБ, записи с камеры) | 2–3 | `scene/zaderzhanie-krota`; `handout/videozapis-krota`; `character/lyao-khan`, `character/zhaklin-bodri`; `location/stantsiya-anno` (history) |
| Что видно на записи (пункты «*») | 2–3 | `handout/videozapis-krota` |
| Ляо Хан в полиции; может войти в отряд | 3 | `scene/zaderzhanie-krota`; `character/lyao-khan` |
| Что вспомнит Ляо Хан (пункты «=») | 3 | `scene/chto-pomnit-lyao-khan` |
| Для Хранителя | 3–4 | `scenario/podzemka` (keeper_info); `creature/mi-go-stalker`; `creature/gast-mi-go`; `character/manfred` |
| Путь до законсервированной станции | 4 | `scene/put-do-stantsii`; `location/otvorot-k-stantsii` |
| Кострище; Манфред (пункты «*», «**») | 4 | `scene/vstrecha-s-manfredom`; `location/kostrishche-u-stantsii`; `character/manfred` (background.secret) |
| «***» Если Манфреда нет на месте | 5 | `scene/vstrecha-s-manfredom`; `character/manfred` |
| Законсервированная станция | 5 | `scene/logovo-gasta`; `location/stantsiya-anno`; `creature/gast-mi-go` (encounters) |
| Обратный путь | 5 | `scene/obratnyy-put` |
| Технический подуровень | 5 | `scene/spusk-na-podurovne`; `location/tekhnicheskiy-uroven` |
| 1 | 6 | `location/t-01-shchitovaya`; `item/zhurnal-neispravnostey`; `creature/mi-go-stalker` (способность «Чутьё электросети») |
| 2 | 6–7 | `location/t-02-komnata-personala`; `scene/pomekhi-v-komnate-personala`; `item/televizor-s-pomekhami` |
| Одержимый техник (28 лет) — статблок и вещи | 7 | `character/mark-ganon`; `item/klyuchi-tekhnika` |
| 3 | 7 | `location/t-03-ventilyatsionnaya-1` |
| А | 7 | `location/t-a-koridor-s-tarakanami` |
| 4 (СКО -1) | 7 | `location/t-04-komnata-s-trubami` |
| 5 (СКО -1) | 7 | `location/t-05-nasosnaya-2` |
| 6 (СКО -1) | 7–8 | `location/t-06-sklad-zapchastey` |
| 7 (СКО -1) | 8 | `location/t-07-sklad-oborudovaniya` |
| С | 8 | `location/t-c-zatoplennyy-tupik` |
| 8 (СКО-1) | 8 | `location/t-08-pustoe-pomeshchenie` |
| 9 | 8 | `location/t-09-nasosnaya-1` |
| 10 (СКО -1) | 8 | `location/t-10-ventilyatsionnaya-2`; `scene/zasada-gasta` |
| 11 | 8–9 | `location/t-11-kholl`; `item/braslet-zhaklin`; `item/instrumenty-obkhodchikov` |
| 12 | 9 | `location/t-12-laboratoriya`; `scene/laboratoriya-mi-go`; `item/mozgovye-tsilindry`, `item/biopautinnaya-bronya`, `item/khirurgicheskie-instrumenty`, `item/paryashchiy-svetilnik` |
| 13 | 9 | `location/t-13-kamera`; `scene/lobotomit`; `character/zhil-tramble` |
| 14 (СКО -1) | 9 | `location/t-14-nasosnaya-3` |
| 15 | 9–10 | `location/t-15-zapertoe-pomeshchenie`; `item/bloknot-manfreda`; `character/manfred` |
| 16 (СКО -1, тьма?) | 10 | `location/t-16-preddverie`; `scene/tma-pered-laboratoriey` |
| Награды сценария | 10 | `scenario/podzemka` (conclusion); исходы сцен |
| Тактика Ми-го | 10 | `scene/taktika-mi-go`; `creature/mi-go-stalker` (encounters) |
| Сопровождающий вооружённый товарищ; Лютер Харден (32 года) | 10 | `character/lyuter-harden` (roles npc, pregen); `scenario/podzemka` (advice, шаг «Сопровождающий») |
| «Если ваши сыщики кажутся вам плохо вооружёнными…» | 10 | `scenario/podzemka` (advice); `item/biopautinnaya-bronya` |
| Список персонажей: Ми-го Сталкер | 11 | `creature/mi-go-stalker` (instance_of `coc:creature:mi-go`); `item/elektropushka-mi-go` |
| Список персонажей: Гаст | 11 | `creature/gast-mi-go` (instance_of `coc:creature:gast`) |
| Список персонажей: Манфред (54 года) | 11 | `character/manfred` |
| Список персонажей: Одержимый техник | 11 | `character/mark-ganon` |
| Список персонажей: Лоботомит | 11 | `character/zhil-tramble` |
| Карта технического уровня (с легендой) | 12 | `map/tekhnicheskiy-uroven` (`app/maps/subway-tekhnicheskiy-uroven.jpg`, 20 меток: 1–16, «a», «c», «Вверх», «Вниз») |

Записи (59): сценарий 1; сцены 13; места 23 в книге + 1 общий город (`kb/locations/montreal.json`); карта 1;
персонажи 6; существа 2; предметы 11; раздатка 1. Предложений правок общих записей нет
(`proposals-subway.json` — пустой список).

## Опечатки и сомнения (в `errata` записей)

- `location/t-14-nasosnaya-3`: «Дверь в помещение №14 в восточной стене» в описании самого помещения 14 — по карте и
  описанию помещения 15 это дверь в 15; в записи исправлено (`fixed: true`).
- `location/t-01-shchitovaya`: на щитке насос 3 назван работающим (с. 6), в помещении 14 он выключен ми-го (с. 9) —
  как напечатано.
- `location/t-06-sklad-zapchastey`: помещения 6 и 7 оба названы «Склад №2» — как напечатано; названия записей даны по
  назначению, надпись — в псевдонимах.
- `creature/gast-mi-go`: Уклонение «35% (17/5)» — пятая часть исправлена на 7 (Р-35); урон «3к6» без БкУ (вероятно,
  1d6 + БкУ 2d6 уже сложены) — как напечатано.
- `character/zhil-tramble` (лоботомит): Скорость 8 при СИЛ 65 и ЛВК 55 меньше ТЕЛ 70 — по правилам 7; возраст не указан —
  как напечатано (Р-161).
- Без `errata` (не ошибки): радиус гипноза ми-го 13 м (в общем профиле 12 м) — свой профиль сценария; у одержимого
  техника БкУ не напечатан; ловушка на двери в лабораторию (помещение 16) книгой не описана — пометка в сцене.

## Не взято

- Картинки: две иллюстрации титула (туннель с диггером, разгромленный вагон), фото технического коридора (с. 6),
  картинка телевизора с силуэтом (с. 7) — оформление без игровых сведений; при желании их можно добавить в `images`
  станции, уровня и телевизора.
- Отдельные записи для служб и толпы: служба транспортной безопасности, полиция, КСРБ, диспетчер, плановые обходчики —
  упомянуты одной фразой, без сведений; остаются текстом в сцене «Задержание Крота» и в местах.
- Двое других пропавших знакомых Манфреда и личности в мозговых цилиндрах — книга не даёт ни имён, ни подробностей;
  остаются текстом в `character/manfred`, `item/mozgovye-tsilindry`.
- Крысы и тараканы (помещения 4, 5, 8, 9, А) — без статблоков, их механика (проверка Уклонения, 1 ПЗ; 0/1 Рассудка)
  записана в местах.
- «Проверка на видеомонтаж» — навыка нет в правилах, механики сверх одной фразы нет (Р-126): текстом в сцене.
- «По усмотрению Хранителя, один из мозгов может знать 1d4 заклинания» — заклинания не названы; новых заклинаний в
  книге нет.

## Кандидаты и вопросы

- Монреаль упомянут в других записях: `mertvennyy-svet-ru/character/lili-berzheron` (место рождения),
  `investigator-handbook-ru/character/pierre-leblanc` (родился и вырос), `kb/creatures/chaugnar-faugn.json` (культ
  «Кровь» в XVIII веке), `pulp-cthulhu-en/organizations/ambrosia-foundation` (контора фонда). Ссылки на общий город из
  них можно добавить при сведении (сейчас город знает только «Подземку»; его эпоха — `modern`).
- Карточка владельца (`3_КБ\Ваншоты\1990 Подземка\_паспорт.md`) указывает место «Россия, крупный город» и год 1990;
  книга — Монреаль, современность.
