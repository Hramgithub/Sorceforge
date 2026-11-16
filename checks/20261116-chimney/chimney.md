# «Hung by the Chimney with Care» (`hung-by-the-chimney-en`) — сверка с переводом (часть chimney)

Оригинал Марка Харта (Petersen Games 2021, по лицензии Chaosium), PDF 12 страниц, хороший текстовый слой; статблоки
(с. 11–12) сверены по изображениям страниц. Сценарий уже есть в базе в фанатском переводе Hort — «Чулки возле печки»
(`kb/books/chulki-vozle-pechki-ru/`, сверка `checks/20261112-ru-oneshots/stockings.md`). По Р-147 второй набор записей
не заводится: перевод хранит текст, оригинал даёт числа. Всё из оригинала — предложениями к записям перевода:
`proposals-chimney.json` (345 правок в 67 записях: 66 записей перевода + `coc:spell:banishment-of-the-defiler`).
Записей `kb/books/hung-by-the-chimney-en/` нет.

## Страницы

Смещение `hung-by-the-chimney-en`: **печатная = физическая** (номера на с. 2–12 совпадают с PDF; с. 1 — титульный лист
без номера, по счёту 1). `pagemap` это подтверждает («физ. 2–12: печ. = физ. + 0»).

## Проверка

Предложения применены в песочнице (полная копия `kb/`, `schemas/`, `tools/`): `apply.py` — 345 правок, 67 записей;
`tools/check.py` по изменённым записям — ошибок 0, предупреждений 0; то же для `art-proposals.json`. В самой базе
ничего не применено — записи перевода не в части.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Hung by the Chimney with Care (титульный лист, аннотация, выходные данные) | 1 | сценарий `chulki-vozle-pechki-ru/scenario/chulki-vozle-pechki` (sources) |
| Introduction | 2 | сценарий: summary |
| Keeper Information | 2 | сценарий: keeper_info; Пьемонт, Спэйс, Льюис, «Общество Торо», том XII |
| Y’golonac (врезка) | 2 | `…/creature/igolonak-v-tele-edmunda-lyuisa`; сценарий: keeper_info |
| A Plea for Help (+ Western Union Telegram) | 3 | сценарий: hook; раздатка `…/handout/telegramma-pemonta` (+ `text.en`) |
| A Somber Season | 3 | сцена `…/scene/khmuryy-sochelnik` |
| Meeting at the Hotel | 3 | сцена `…/scene/vstrecha-v-otele`; записка `…/handout/zapiska-pemonta` (+ `text.en`), портфель, ключ |
| The Investigation Begins | 3 | сценарий: advice |
| At the Post Office | 4 | сцена `…/scene/pochta` |
| At the Gazette | 4–5 | сцена `…/scene/redaktsiya-gazety`; место `…/location/redaktsiya-gazety` (псевдоним «Редакция «Газетт»») |
| Murder Scenes | 5 | сцена `…/scene/mesta-prestupleniy` |
| One Picture Is Worth a Thousand Scares | 5–6 | сцена `…/scene/luchshe-odin-raz-uvidet`; `…/item/risunok-billi` |
| The Police | 6 | сцена `…/scene/politsiya`; `…/character/khenk-erikson` |
| Wandering the Town | 6–7 | сцена `…/scene/progulka-po-gorodu` |
| Ambush | 7 | сцена `…/scene/zasada`; `…/character/bandity-speysa` |
| Keeping the Investigation Going | 7 | сценарий: advice |
| Next Steps | 7 | сценарий: advice, шаг «Дальнейшие шаги» |
| The Relic Retrospective | 7–8 | сцена `…/scene/relikvii-bylogo`; место `…/location/relikvii-bylogo` |
| Haglund’s Home | 8 | сцена `…/scene/dom-kheglunda`; место `…/location/dom-kheglunda` |
| Stakeout of the Haglund Home | 8–9 | сцена `…/scene/slezhka-za-domom-kheglunda` |
| A Santa Sighting | 9 | сцена `…/scene/poseshchenie-santy` |
| Confrontation | 9 | сцена `…/scene/kulminatsiya` |
| Conclusion | 10 | сценарий: conclusion |
| Rewards | 10 | сценарий: conclusion (награды Рассудка — совпадают с переводом) |
| NPCs & Monsters: Hank Erickson, 36 | 11 | `…/character/khenk-erikson` |
| Keegan Duquesne, 29 | 11 | `…/character/kigan-dyukesne` |
| Nathaniel Piedmont, 56 | 11 | `…/character/nataniel-pemont` |
| Thugs | 11 | `…/character/bandity-speysa` |
| Winston Spaes | 11 | `…/character/uinston-speys` |
| Y’golonac (статблок) | 12 | `…/creature/igolonak-v-tele-edmunda-lyuisa` |
| Banishment of the Defiler | 12 | `coc:spell:banishment-of-the-defiler`; `…/item/vypiski-pemonta` |

## Что предложено (proposals-chimney.json)

- Каждой из 66 записей перевода — источники оригинала (`sources`, печатная = физическая), `name.en` (кроме записей с
  придуманными именами — Маргарет Хэглунд и Уолтер Гриффин: им английские обозначения книги в псевдонимы, «Mrs. Haglund»,
  «desk clerk»), английские формы имён в `aliases`; в `quality.notes` «английского оригинала в библиотеке нет — числа
  по переводу» заменено на «числа сверены с английским оригиналом…».
- Раздатка: английский текст телеграммы и записки как напечатан (`text.en`).
- Числа (в `corrections`, ошибки перевода — в `errata`, `fixed: true`):
  - Хэнк Эриксон: Уклонение 50% (25/10) → **40% (20/8)** (ошибка перевода);
  - Киган Дюкесне: навыка «Прыжки 45%» в оригинале нет (перевод взял его из статблока Эриксона) — убран;
  - Бандиты: «Blackjack» — оружие `coc:weapon:blackjack` вместо `club-large` (урон тот же 1d8), `name.en`;
  - Уинстон Спэйс: в списке заклинаний пропущен **Voorish Sign** → добавлен `coc:spell:voorish-sign`;
  - И’голонак сценария: вместо «Ближний бой (драка) 25% (12/5), 1d3» перевода — **Fighting 100% (50/20), урон БкУ**;
    укус — **100% (50/20)** (в переводе шанс не напечатан); уклонения в оригинале нет — 25% перевода заменены на 40% (20/8)
    из общей записи `coc:creature:ygolonac` (вывод из текста, Р-41); прежняя errata о «похожем на человеческий профиле»
    заменена объяснением;
  - сцена «Посещение Санты»: «сложная проверка Вождения» → **трудная** (Hard Drive Auto), «обычная проверка
    Выслеживания» → **лёгкая** (Easy Track).
- Текст (только `corrections`): похищение Пьемонта «примерно час назад» → **полчаса** (about half an hour ago; сцена,
  портье, бандиты, Пьемонт, keeper_info); Билли у тёти «на пару недель» → **несколько дней** (a few nights; Билли, Мэри,
  сцена «Места преступлений»); у Хэглунда **сын и дочь** (дочь в переводе пропущена; сцена, миссис Хэглунд, пометка места);
  И’голонак «заточён в подземных руинах под древней каменной стеной» → «обычно заточён за древней космической кирпичной
  стеной» (behind an ancient cosmic brick wall; существо, сцена «Дом Хэглунда»); итог «Если Спэйс устранён, но И’голонак
  не изгнан» → «Если сыщики не завершат ритуал изгнания» (в оригинале условия о Спэйсе нет).
- `quality.notes` сценария: раздел «Заклинания» перевода (с. 15–17: Затуманивание памяти, Воззвание к мёртвым, Дурной
  глаз, Господство, Порабощение жертвы, Мысленное внушение, Разрушение) — добавлен переводчиком, в оригинале только
  «Banishment of the Defiler».
- `coc:spell:banishment-of-the-defiler`: источники оригинала (с. 12, 9), errata о противоречии (см. ниже), флаг.

## Опечатки и противоречия оригинала

- Дюкесне: «MP: 19» при POW 70 (должно 14) — так же в переводе; пометка errata дополнена.
- Бандиты: «MP: 9» при POW 35 (должно 7) — так же в переводе; пометка дополнена.
- Спэйс: «Move: 3» — при СИЛ 55, ЛВК 50 < ТЕЛ 60 Скорость 7 (3 — только с 80 лет); в переводе 7 — в записи 7, errata.
- И’голонак: укус «1D4+2» в абзаце «Attacks» и «1D4 non-healing damage» в таблице — взят текст (Р-38), как в переводе и
  Malleus Monstrorum; errata.
- «Banishment of the Defiler»: «each additional magic point … by 5 percent» и сразу «Sacrificing 10 additional magic points
  adds 25 percent» (10 × 5% = 50%) — в переводе второй фразы нет; в записи +5% за ПМ, errata `fixed: false` — вопрос владельцу.
- «Nathan»/«Nathaniel» Piedmont, «Win» Aubrey — формы имени, в псевдонимах.
- «paternal secret order» (с. 4), видимо, вместо «fraternal» — словесная, не записана (Р-39).

## Мелкие расхождения перевода, не предложенные (без значения для игры)

- Отель «located off Main Street» (рядом с главной улицей) — в переводе «на главной улице».
- «metal lockbox» у алтаря — в переводе «сейф»; «the newspaper morgue» — «газетный морг».
- «Come soonest possible…» в телеграмме и т. п. — вольности перевода; английский текст — в `text.en`.
- «одного … размахивал значком, а у другого шрам» — в оригинале «one of them … one of them» (может быть один и тот же).

## Картинки

- `art.json` → `art-proposals.json` (2, не применено — записи перевода): красная книга (с. 5) → том XII
  (`app/art/tomes/chimney-otkroveniya-glaaki-tom-12.webp`); портрет полицейского в разделе «The Police» (с. 6) → Хэнк
  Эриксон (`app/art/characters/chimney-khenk-erikson.webp`) — подписи нет, сопоставление по месту на странице.
- И’голонак в истинном облике (с. 4) у перевода уже есть — не повторён.
- `atmosphere.json` — 6: логотип, чудовище с глазами на стебельках (с. 2, похоже на Гла’аки), две раскрытые книги
  (с. 3, 10), портрет без подписи (с. 9 — Льюис или Спэйс? вопрос владельцу), повтор И’голонака (с. 4).

## Не взято

| Что | Страница | Причина |
|---|---|---|
| Выходные данные (художники, вёрстка, редактура, копирайты Chaosium и Рэмси Кэмпбелла) | 1 | не игровые данные; автор и издатель — в источнике сценария |
| Карты | — | в книге карт нет |
| Новые записи книги `hung-by-the-chimney-en` | — | всё ложится в записи перевода (Р-147) |

## Термины (English → русский)

Взяты формы перевода и базы; новые — только «Газетт» и «лёгкая проверка».

| English | Русский |
|---|---|
| Hung by the Chimney with Care | Чулки возле печки развешены в ряд |
| Y’golonac; The Defiler; the Hand that Feeds | И’голонак; Совратитель; Длань Питающая |
| The Revelations of Gla’aki (volume twelve) | «Откровения Гла’аки», том XII |
| Banishment of the Defiler | Изгнание Совратителя |
| Dismiss (ritual) | ритуал изгнания |
| Thoreau Society | Общество Торо |
| The Relic Retrospective | «Реликвии былого» |
| the Gazette | «Газетт» (новый) |
| Dunham Hotel | отель «Данхэм» |
| St. Mark’s Church | церковь Св. Марка |
| Thugs | Бандиты Спэйса |
| Nathaniel (Nathan G.) Piedmont | Натаниэль (Натан Дж.) Пьемонт |
| Winston Spaes | Уинстон Спэйс |
| Keegan Duquesne | Киган Дюкесне |
| Hank Erickson | Хэнк Эриксон |
| George Haglund | Джордж Хэглунд |
| Edmund Lewis; Paisley Lewis | Эдмунд Льюис; Пэйсли Льюис |
| Winifred “Win” Aubrey | Уинифред (Уин) Обри |
| Robert, Mary, Billy Latham | Роберт, Мэри, Билли Латэм |
| Sarah Scott; Darwin Talbot; Davis Griggs | Сара Скотт; Дарвин Тэлбот; Дэйвис Григгс |
| Anthony Clark; Myra Clark | Энтони Кларк; Мира Кларк |
| Clyde Hooper; Byron Harmon; Carlton Banks; Mabel | Клайд Хупер; Байрон Хармон; Карлтон Бэнкс; Мэйбл |
| Hard roll; Easy roll | трудная проверка; лёгкая проверка (новый) |
| Blackjack | дубинка скрытого ношения (`coc:weapon:blackjack`) |
| Voorish Sign | Вурский знак |
