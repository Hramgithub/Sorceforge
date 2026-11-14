# Часть `gg`: Grand Grimoire of Cthulhu Mythos Magic — заклинания, правила глав 1–3, таблицы, врезки, колдуны

Книга `grand-grimoire-en` (физическая страница = печатная + 1; ниже страницы печатные). Описи покрытия прошлых переносов:
`checks/20261114-completeness-fix/gg-rules.md`, `gg-spells.md` (Р-242); все записи, названные в них, есть в `kb/`.

Как проверялось:

- Статьи гл. 4 извлечены прямо из PDF по шрифту заголовка (ACaslonPro-Bold 11 pt) в порядке набора — 522 заголовка;
  они совпали с описью `gg-spells.md` (523 строки: «Contact Deity — see page 72» и «Contact Elder Thing» в PDF — один
  заголовок). У каждой статьи разобраны поля Cost, Casting time, описание, Deeper magic, Alternative names.
- Каждая статья сопоставлена с записью `kb/spells/` (по `name.en`, id, затем `aliases`) — найдены все 522.
- Скриптом для **всех** статей: числа цены и времени книги против `cost.raw` / `casting_time.raw`; все кубы и проценты
  описания и глубинной магии против текста записи; числа с единицами (ПМ, МОЩ, Рассудок, ПЗ, раунды, часы, дни,
  характеристики) против записи; каждое альтернативное название против `aliases`; наличие глубинной магии в книге против
  поля `deeper_magic`; печатная страница GG в `sources`. Все расхождения разобраны вручную по тексту страниц: большая часть —
  перетекание соседних статей и врезок в вёрстке, остальное ниже.
- Вручную целиком (цена, время, все числа описания, глубинная магия, названия): Accursed Eye, Activation, Alter Weather,
  Bestow Karma, Animate Flesh Thing, Contact Zoth-Ommog, Free Hastur, Stupefying Blast, Summon Baka, Summon Greater Desh,
  Summon Shoggoth, общие статьи семейств (вызов, связь, изгнание, призыв, зачарование).
- Главы 1–3 прочитаны полностью (физ. 8–26) и сверены с записями `coc:rule:gg-*`; таблица 1 — построчно выборочно;
  списки категорий гл. 3 — скриптом в обе стороны (книга ↔ строки записи).
- Скрипты — `scratchpad\gg\` (`extract.py`, `compare.py`, `summ.py`, `altwhere.py`, `ctx.py`, `grepent.py`, `units.py`,
  `cats2.py`, `cats3.py`, `statblocks.py`).

## Introduction (с. 5)

не нужно — служебное вступление редакции (`gg-rules.md`, «Не взято»).

## Гл. 1 «Concerning Magic» (с. 7–10)

цел — `coc:rule:gg-state-of-mind`, `gg-the-nature-of-sacrifice`, `gg-are-the-stars-right`. Сверены все четыре таблицы
записи построчно: «Дни недели» (7), «Фазы луны» (4, опечатка 180–255 — в `errata`), «Колесо года» (8 дат), «Прочие
астрономические факторы» (7: 29,5 дня, 44 голубые луны, 1833, 1 000 метеоров, 2 392 года, 1531/75 лет/2061,
1881/1889/2004/2117); правило бонуса/штрафа за время сотворения; врезки-воззвания цитатой.

## Гл. 2 «Concerning Spells» (с. 11–21)

| что | стр. | вид | где должно быть / что не так | важность |
|---|---|---|---|---|
| Пример к «Spellcasting in the Dreamlands»: уроженец Страны грёз за Unspeakable Promise (2D8) теряет только 2 Рассудка, за Devolution — полные 1D10 | 14 | rule | `coc:rule:gg-dreamlands-magic` — правило есть, пример опущен | низкая |

Остальное цело: Spell Names, Deeper Magic (источник GG в `coc:rule:deeper-magic`, 1D100 против Мифов Ктулху), Adjusting
Spells, Difficulties in Spellcasting, Folk Magic, Flawed Spells (60/40 %, 1D8+1 и 2D8+1 часа, Мифы 40 %, трудные
проверки, 7 проявлений), Spirit Attacks and Possession (1D10 ПМ, 1/1D4, 2D10, 1D10 часов, каждые 8 часов), Spell
Components (7 видов), Magical Tools (таблица), Amulets/Talismans, Magical Residue (МОЩ 70, Мифы 50 %/49 %, 1D6+1 раунд,
+2D6 ПМ), Residual Magical Effects (8 существ, 1/1D6, +1D10 Мифов/−1D10 Рассудка, −5 МОЩ), Ley Lines (+20 %, 1D10+1
раунд, +1D10 ПМ, −1D10+1 ПМ, 96 км), врезка о предложениях главы, Fictional Magic.

## Таблица 1 «Spell Components» (с. 16–17)

цел — `coc:table:spell-components`, 1D100, 100 строк; сверены строки 1–3, 16–19, 67–70, 98–100 («Grave dirt» дважды — как
напечатано).

## Гл. 3 «Spell Categories» (с. 22–25)

| что | стр. | вид | где должно быть / что не так | важность |
|---|---|---|---|---|
| Списки категорий: 6 названий сопоставлены не с той записью через псевдоним-однофамилец (та же ошибка сопоставления, что ловится на «Evil Eye» → `curse-folk`). Enchantments: нет Enchant Spear (37 вместо 38). Combat: Vanish стоит как «Шкатулки врат» (`gate-boxes`). Harmful: Evil Eye → «Проклятье (народное)», Melt Flesh → «Жидкая смерть», нет Lift Veil (40 вместо 41). Influencing Others: Evil Eye → «Проклятье (народное)». Protection: нет Seal of Nephren-Ka (32 вместо 33). Travel: нет Vanish (21 вместо 22) | 22–25 | rule (таблица) | `coc:rule:gg-spell-categories`: строки таблицы и `refs` — заменить на `evil-eye`, `melt-flesh`, `lift-veil`, `vanish`, добавить `enchant-spear`, `seal-of-nephren-ka`; счётчики 37/40/32/21 → 38/41/33/22 | средняя |

Остальные 11 категорий совпали с книгой поимённо (46, 112, 8, 57, 15, 16, 23, 38, 40, 12, 31). Опечатки списков
(Shub-Niggurtah, Posses Corpse) — в `errata`.

## Entry Format; Call, Contact, and Summon Disambiguation (с. 25)

цел — `coc:rule:gg-spell-entry-format`, источник GG в `coc:rule:call-contact-and-summon-disambiguation` и
`coc:rule:casting-time-and-spells-in-combat` (DEX+50, ход по ЛВК).

## Гл. 4 — статьи заклинаний (с. 26–193)

Записи есть у всех 522 заголовков; страница GG в `sources` верна у всех. Цена и время совпадают у всех статей, кроме
расхождений, уже записанных в `quality.notes`/`errata` (Call The Black 20 ПМ/10 МОЩ против 8/1 «Дверей во тьму»; Enchant
Dagger of Nyarlathotep +2D10 Рассудка; Gate Boxes 5 МОЩ против 1 МОЩ КХ; Brew Space-Mead «7+ дней»; Dust of Suleiman
«24+ часа»; Time Gate «1 час на 5 МОЩ»; опечатки Bestow Karma и Fire Dance). Кубы и проценты описаний и глубинной магии
найдены в записях у всех статей (недостающие — только перетекание вёрстки). Неверных чисел не найдено.

| что | стр. | вид | где должно быть / что не так | важность |
|---|---|---|---|---|
| Глубинная магия GG не перенесена у 6 записей: Cloud Memory (+10 ПМ — бонусная кость во встречной МОЩ), Dread Curse of Azathoth (колдун поглощает отнятую МОЩ, повышая свою МОЩ и ПМ), Dowsing (поиск вещей Мифов с проверкой Мифов Ктулху), Ill Luck (при проигрыше встречной МОЩ невезение 24 часа на самом колдуне), Nyhargo Dirge (до 8 нежитей за раз; 20 ПМ, 1D10 Рассудка, 5 МОЩ навсегда — сейчас только в `note` источника), Spirit Summoning (вместо нужного духа может явиться другой дух или нечто извне и вселиться) | 66, 98, 98, 128, 146, 172 | spell, поле `deeper_magic` | `coc:spell:cloud-memory`, `dread-curse-of-azathoth`, `dowsing-folk`, `ill-luck-folk`, `nyhargo-dirge`, `spirit-summoning` — поле пусто | средняя |
| Balk Brood: версия GG не записана — успех встречным броском 1D100 (ПМ×5 против дней заражения×5 у Хранителя), цель теряет 1D4 Рассудка и 1 ПЗ за день, Эйхорт — 10 % и +10 % за каждое следующее сотворение; `note` источника GG ошибочно пишет «альтернативных названий нет» | 34 | spell | `coc:spell:balk-brood` (числа по «Не забывай меня»: ПМ сравниваются с днями, 1d3 Рассудка) — версию GG в `quality.notes` (Р-51), названия в `aliases` | средняя |
| Альтернативные названия GG не внесены у 10 записей, получивших источник GG только предложением (30 названий): Balk Brood — Dispel Children of the Labyrinth, Crack the Eggs of White Death; Become Spectral — Hide Unseen, Cast Off Thy Flesh And Be As Spirit, Enter the Shadow Realm; Disembodiment — Cast Off Thy Flesh, Spirit Sight, Limbo Journeying; Dowsing — Water Witching, Create Diving Rod, Locate Treasures, Find Substance; Free Hastur — Unbound the Unspeakable One, Invocation of Hali, Rite in Yellow; Ill Luck — Hex, Malediction, Jinx, Execration; Nyhargo Dirge — Destroy Zombie, Chant of Eradication; Poison Blood — Poison Touch, The Dread, Blight; Spirit Summoning — Séance, Commune with the Dead, Spiritualism, Channeling; Winds of Desolation — Call Tempest, Breath of Judgment | 34–190 | spell, `aliases` | `coc:spell:balk-brood`, `become-spectral`, `disembodiment`, `dowsing-folk`, `free-hastur`, `ill-luck-folk`, `nyhargo-dirge`, `poison-blood-folk`, `spirit-summoning`, `winds-of-desolation-folk` | низкая |
| Spirit Summoning: числа версии GG (переменные ПМ, ×5 — процентный шанс; 1D4 Рассудка; 1D4 раунда; личный предмет умершего) записаны только в `note` источника, в `quality.notes` расхождения с «Грибами с Юггота» нет | 172 | spell | `coc:spell:spirit-summoning` → `quality.notes` (Р-51) | низкая |
| Become Spectral Hunter: подробности GG — охотник не дальше мили от фигурки, повреждённая фигурка — 1D8 урона охотнику, уничтоженная — охотник развеян, но вернётся через 7 дней | 37 | spell | `coc:spell:become-spectral-hunter` (текст по «Царству террора»/КХ: «за неделю изготовит новую фигурку») | низкая |

Не потери: «Armor of the Will», «Snake Skin Cloak», «Rite of Dissolution» в GG — в записях стоят написания КХ «Armour…»,
«The Snake Skin Cloak», «Rite of the Dissolution»; «Maggots» в выгрузке PDF получил названия соседнего Living Clothes —
у `living-clothes` они есть.

## Общие правила семейств заклинаний (с. 41–42, 53–54, 72, 77, 96–97, 106, 174–177)

цел — `coc:spell:summon-bind` (с «Form of the Command»), `call-deity` (1+ ПМ, 1D10, 1–100 минут), `contact-deity`
(5 МОЩ, 1D6, 1D6+4 раунда), `contact-spells` (1D3, 1D6+4 раунда), `dismiss-deity` (1 ПМ на 25 МОЩ, +5 %, максимум 99 %,
пример Ктугхи 8+19 = 27 ПМ), `enchant-item`, сводки призыва/укрощения (Summon Baka, Greater Desh, Shoggoth — новые записи;
остальные — `summon-bind-*`), сверены цена, время, глубинная магия и названия.

## Врезки и таблицы гл. 4

| что | стр. | вид | где должно быть / что не так | важность |
|---|---|---|---|---|
| Table 2: Time Gate Creation and Travel Costs — 14 строк (5 МОЩ/1 ПМ — 1 час, 10/2 — 1 день, 15/3 — неделя, 20/4 — месяц, 25/5 — год, 30/6 — 10 лет … 70/14 — 100 000 000 000 лет) | 180 | spell (таблица) или table | `coc:spell:time-gate` — по КХ («16 км = 10 лет»), `quality.notes` лишь упоминает, что у GG своя таблица; значений таблицы в базе нет | средняя |
| Профили GG Spectral Hunter (СИЛ 100, ТЕЛ 95, ЛВК 55, МОЩ 90, ПМ 18, Бой 40 % 3D6+БкУ, Рассудок 1/1D6+2) и Human Hybrid Tindalosian (СИЛ 130, ВЫН 130, ТЕЛ 85, ЛВК 95, ИНТ 85, МОЩ 120, ПЗ 22, БкУ +2D6, ПМ 24) отличаются от Malleus Monstrorum | 37, 48 | creature | `coc:creature:spectral-hunter`, `coc:creature:tindalosian-hybrids` — числа по MM (первоисточник), но нет ни источника GG, ни заметки о расхождении | низкая |
| Профиль Fog Spawn из врезки GG | 155 | creature | не взят (`gg-spells.md`, вопрос владельцу открыт); в базе только `masks-of-nyarlathotep-en/creature/fog-spawn` | низкая |

Цело: Weather Components (Alter Weather — все 5 составляющих), таблица 1D8 Activation, Flesh Thing (СИЛ 75, ВЫН 100,
ТЕЛ 90…, 90/45/30 %), Flesh Creeper, Star-Seeds, Circle Spell Variations, Avatars of Nyarlathotep, Shamballah, Effigy of
Hate (текстом), Conjuration of The Turua (4 части: цены и время, профиль туруа — все числа), Table 1: Gate Creation (=
таблица XII КХ: 5 МОЩ — 100 миль … ), Nightmare Effect (1D10), Winds of Desolation Strength (5 ступеней 4–64 ПМ), Fungus
Timeline.

## Персонажи-колдуны (с. 85, 133, 185)

| что | стр. | вид | где должно быть / что не так | важность |
|---|---|---|---|---|
| Портрет Томаса Дэвенпорта (вклейка физ. 133, подпись «Opposite: Thomas Davenport by Jonathan Wyke» на с. 133) — сейчас в `pipeline/art/atmosphere.json` как «человек у накрытого тела, сцена» | 132 | картинка (Р-241, Р-245) | `grand-grimoire-en/character/thomas-davenport` — `images` пусто | низкая |

Статблоки целы у всех трёх: характеристики, ПЗ, ПМ (с талисманом/тростью), Рассудок (0, 0, 48), БкУ, Комплекция,
Скорость, атаки и Уклонение, навыки, заклинания (у Дэвенпорта — 16 названий со ссылками). Портреты Хестии Локсби и
Нильса-Вигго Шоу — в записях.

## Прочее

| что | стр. | вид | где должно быть / что не так | важность |
|---|---|---|---|---|
| Одинаковое русское название «Наслать мор» у двух записей: Bring Pestilence и Summon Plague | 51, 177 | spell, `name.ru` | `coc:spell:bring-pestilence`, `coc:spell:summon-plague` — развести названия | низкая |

Не нужно: указатель (с. 195–200; названия сверены в `gg-spells.md`), эпиграфы, колонтитулы, подписи; вклейки-«страницы
гримуара», знаки и круги — 36 страниц в `atmosphere.json`. Арт туруа (физ. 71) и гомункула Цатоггуа (физ. 160) — тоже
там: записей этих существ нет (туруа — кандидат, `gg-rules.md`); у Короля в Жёлтом (физ. 58) картинки уже есть.

## Итого

Частей — 12: **цел** — 4 (гл. 1, таблица 1, Entry Format и Disambiguation, общие правила семейств); **частично** — 5
(гл. 2 — мелочь; гл. 3 — 6 неверных сопоставлений в списках категорий; статьи гл. 4 — глубинная магия, версия Balk Brood,
названия; врезки гл. 4 — таблица Time Gate, профили; колдуны — портрет); **нет** — 0; **не нужно** — 3 (Introduction,
указатель, эпиграфы и оформление).

Потери — 12 строк:

- высокая — 0;
- средняя — 4: глубинная магия GG у 6 записей; версия GG «Balk Brood»; таблица 2 «Time Gate Creation and Travel Costs»;
  списки категорий гл. 3 (6 названий в 6 категориях);
- низкая — 8: 30 альтернативных названий у 10 записей; числа GG «Spirit Summoning» только в `note`; подробности «Become
  Spectral Hunter»; профили GG Spectral Hunter и Human Hybrid Tindalosian без заметки; профиль Fog Spawn; портрет
  Дэвенпорта; пример магии Страны грёз; одинаковое `name.ru` «Наслать мор».

Неверных чисел не найдено: цена, время, кубы и проценты всех 522 статей совпадают с книгой или расходятся по записанной
причине (другая книга — первоисточник, опечатка в `errata`). Почти все потери — у записей, заведённых по другим книгам,
которым источник GG добавили только предложением (`proposals-gg-spells.json` внёс `sources`, но не названия и глубинную
магию).
