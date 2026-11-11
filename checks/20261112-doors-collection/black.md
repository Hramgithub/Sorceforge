# «Чернее чёрного» («Двери во тьму», `dveri-vo-tmu-ru`) — сверка переноса (часть black)

Источник — официальное русское издание «Двери во тьму» (скан без текстового слоя): страницы распознаны
`pdftoppm -r 200` + `tesseract -l rus`, распознавание на двухколоночных страницах с фоном неполное, поэтому весь текст
прочитан и каждое число сверено по изображению страницы; английский оригинал `doors-to-darkness-en` — для сверки чисел и
английских названий (Р-213).

## Страницы

| Что | Печатные страницы | Физические страницы PDF |
|---|---|---|
| Гл. 6 «Чернее чёрного» (с. 106 — иллюстрация во всю страницу) | 96–110 | 95–109 |
| «Материалы для игроков»: материал «Чернота 1» | 125 (и картинка на с. 100) | 124 (99) |
| «Готовые персонажи» (десять сыщиков сборника) | 126–135 | 125–134 |

Смещение `dveri-vo-tmu-ru`: печатная = физическая + 1 на всех страницах части (95→96 … 109→110, 124→125).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Глава 6. Чернее чёрного (Брайан М. Сэммонс) | 96 | сценарий `dveri-vo-tmu-ru/scenario/none-more-black` (summary) |
| Введение | 96 | сценарий: summary; город сценария `…/location/black-college-town` |
| Информация для Хранителя | 96 | сценарий: keeper_info; `…/character/black-jonathan-dover`, `black-margaret-dover`, `black-jacob-dover`; `coc:creature:yibb-tstll`; организации `…/organization/black-black-trade`, `black-irish-mob` |
| Смерть Уолтера Резника | 96–98 | сцена `…/scene/black-death-of-walter-resnick`; `…/character/black-walter-resnick`, `black-thomas-swanson`; места `…/location/black-resnick-room`, `black-morgue`; предметы `…/item/black-glass-bottles`, `black-resnick-autopsy-report` |
| Вовлечение сыщиков | 98 | сценарий: hook |
| Направления расследования | 98 | сценарий: шаг «Направления расследования» |
| Странное поведение | 98 | сцена `…/scene/black-odd-behavior`; `…/location/black-college` |
| Чёрный язык | 98 | сцена `…/scene/black-black-tongue`; `…/character/black-mary-clawson`, `black-franklin-stewart` |
| Стеклянные бутылки | 98–99 | сцена `black-odd-behavior`; `…/item/black-glass-bottles` |
| Чернота | 99 | сцена `…/scene/black-examining-the-black`; `…/item/black-the-black` |
| Поиски Пола Роджерса | 99 | сцена `…/scene/black-finding-paul-rodgers`; `…/location/black-town-hall`; `…/item/black-rodgers-tax-receipts` |
| Дом Пола Роджерса | 99–100 | сцена `…/scene/black-rodgers-house`; `…/location/black-rodgers-house`; `…/item/black-galoshes`, `black-rodgers-stash`; `…/character/black-leslie` |
| Хранителю на заметку: мафия (врезка) + статблок «Шеймус О’Ши, 33 года, бандит» | 100 | сценарий: advice; `…/character/black-seamus-oshea` (статблок); `…/organization/black-irish-mob` |
| Материал «Чернота 1» (в главе) | 100 | раздатка `…/handout/black-1-rodgers-calculations` |
| Если отведать Черноты | 100–101 | сцена `…/scene/black-trying-the-black`; `…/item/black-the-black` (mechanics) |
| Таблица 1. Действие Черноты (с «Зависимость», «Борьба с зависимостью») | 101 | сценарий: таблица «Таблица 1. Действие Черноты» (8 строк) |
| Вариант: смерть с небес | 101–102 | сцена `…/scene/black-death-from-above` |
| Заклинание: Вызов Черноты (врезка) | 102 | сценарий: таблица «Заклинание: Вызов Черноты» (6 строк); записи в `kb/spells` нет — черновик ниже |
| Бойня | 102–103 | сцена `…/scene/black-the-slaughterhouse`; места `…/location/black-slaughterhouse`, `black-blood-creek`; `…/item/black-slaughterhouse-deed`, `black-black-vat` |
| Бойня или Дувр? | 103 | сцена `…/scene/black-slaughterhouse-or-dover`; сценарий: advice |
| Хранителю на заметку: используйте ночных призраков (врезка) | 103 | сценарий: advice; существо `…/creature/black-nightgaunts` (описание, способность «Сбросить с высоты») |
| Досье на Джейкоба Дувра | 104 | сцена `…/scene/black-researching-dover`; места `…/location/black-county-hospital`, `black-old-dover-house`; `…/item/black-jonathan-death-certificate` |
| Комната Джейкоба Дувра | 104 | сцена `black-researching-dover`; место `…/location/black-dover-room` |
| Дневник Джонатана Дувра (врезка) | 104 | книга `…/tome/black-jonathan-dover-journal` (reading, spells) |
| Кто такой Йибб-Тистл (врезка) | 104 | книга `black-jonathan-dover-journal` (description); `coc:creature:yibb-tstll` |
| Вовлечение полиции | 105 | сцена `black-slaughterhouse-or-dover` (последний абзац); сценарий: advice; `…/organization/black-black-trade` |
| Финальная схватка | 105, 107 | сцена `…/scene/black-showdown`; места `black-slaughterhouse-main-floor`, `black-slaughterhouse-small-stock` |
| Хранителю на заметку: вызов Черноты (врезка) | 105 | книга `black-jonathan-dover-journal`; сцена `black-researching-dover`; сценарий: advice |
| Карта «Бойня» | 105 | карта `…/map/black-map-1-slaughterhouse` (`app/maps/dveri-black-map-1.jpg`, 1235×815, 19 меток на все подписи) |
| Хранителю на заметку: Сырая Голова да Чёрные Кости (врезка) | 107 | сцена `…/scene/black-raw-head`; существо `…/creature/black-raw-head-and-black-bones` (legend) |
| Итоги | 108 | сценарий: conclusion; шаг «Итоги и награды» |
| Награды | 108 | сценарий: conclusion (четыре награды Рассудка) |
| Приложение А. Персонажи Хранителя и чудовища | 108 | — |
| Чернушники, бандиты-наркоманы | 108 | `…/character/black-blackheads` (групповой профиль, придуманные имена) |
| Пол Роджерс, 20 лет, наркоторговец | 108–109 | `…/character/black-paul-rodgers` (статблок) |
| Уиллис Картер, 20 лет, телохранитель-наркоман | 109 | `…/character/black-willis-carter` (статблок) |
| Джейкоб Дувр, 27 лет, чародей-наркоторговец | 109 | `…/character/black-jacob-dover` (статблок, заклинания) |
| Ночные призраки, два приспешника | 109 | `…/creature/black-nightgaunts` (`instance_of` `coc:creature:nightgaunt`) |
| Сырая Голова да Чёрные Кости | 110 | `…/creature/black-raw-head-and-black-bones` (статблок, способности; `spawn_of` `coc:creature:physical-manifestation-the-black`) |
| Материалы для игроков: материал «Чернота 1» | 125 | `…/handout/black-1-rodgers-calculations` (источник текста) |
| Готовые персонажи (десять сыщиков) | 126–135 | существующие записи `dveri-vo-tmu-ru/character/<slug>` — в ссылках сценария (источник книги им предложен частью darkness) |

`…/` = `dveri-vo-tmu-ru/`.

## Записи (55)

| Вид | Число | Записи |
|---|---|---|
| scenario | 1 | `none-more-black` (order 5; две таблицы) |
| scene | 13 | `black-death-of-walter-resnick`, `-odd-behavior`, `-black-tongue`, `-examining-the-black`, `-finding-paul-rodgers`, `-rodgers-house`, `-trying-the-black`, `-death-from-above`, `-the-slaughterhouse`, `-slaughterhouse-or-dover`, `-researching-dover`, `-showdown`, `-raw-head` |
| location | 13 | `black-college-town` (город сценария, Р-190), `-college`, `-resnick-room`, `-morgue`, `-town-hall`, `-county-hospital`, `-rodgers-house`, `-old-dover-house`, `-dover-room`, `-slaughterhouse` (адрес «Ривер-стрит, 143»), `-slaughterhouse-main-floor`, `-slaughterhouse-small-stock`, `-blood-creek` |
| map | 1 | `black-map-1-slaughterhouse` |
| character | 12 | статблоки: `black-jacob-dover`, `-paul-rodgers`, `-willis-carter`, `-seamus-oshea`, `-blackheads` (группа); без статблока: `-walter-resnick`, `-thomas-swanson`, `-mary-clawson`, `-franklin-stewart`, `-leslie`, `-jonathan-dover`, `-margaret-dover` |
| creature | 2 | `black-nightgaunts`, `black-raw-head-and-black-bones` |
| item | 9 | `black-the-black`, `-glass-bottles`, `-resnick-autopsy-report`, `-rodgers-tax-receipts`, `-galoshes`, `-rodgers-stash`, `-slaughterhouse-deed`, `-jonathan-death-certificate`, `-black-vat` |
| handout | 1 | `black-1-rodgers-calculations` |
| tome | 1 | `black-jonathan-dover-journal` |
| organization | 2 | `black-black-trade` («Торговля Чернотой»), `black-irish-mob` |

Город: книга не называет город («любой городок, где есть колледж», с. 96; предлагает Аркхэм) — как «Ящик Пандоры», это
запись книги «Город сценария «Чернее чёрного»» (`location_type` «город сценария», Р-190), со ссылкой на `coc:location:arkham`.
Все места — внутри города (бойня — на окраине), области «Окрестности» не понадобилось.

## Опечатки книги и расхождения изданий

- **Джейкоб Дувр** (с. 109): ПЗ 13 при ВЫН 75 и ТЕЛ 70 (по правилам 14); ПМ 8 при МОЩ 85 (по правилам 17). Так и в оригинале.
  `errata` как напечатано (Р-161).
- **Материал «Чернота 1»**: оригинал — «63 B × $12 = $819» (63 × 12 = 756), русское издание — «63 × $13 = $819» (сходится).
  Взято по русскому изданию, пометка в раздатке.
- **Ночные призраки в финале** (с. 107): русское издание — «спрыгнув с шестиметрового потолка и нанеся 2d6 урона»; оригинал —
  уносят сыщика под потолок 20 футов и роняют (2D6). Взято по русскому, пометки в существе и сцене.
- **Врезка «Вызов Черноты»** (с. 105): русское — «+1% к Мифам Ктулху», с. 174 и 175–176 «Книги Хранителя»; оригинал —
  «+1 Cthulhu Mythos», с. 176 и 177–178 Rulebook.
- Дувр: в статблоке «Наука (фармакология)», в тексте сценария «Наука (фармацевтика)», в оригинале Science (Pharmacy).
- Маргарет: «несчастный случай на реке» (с. 104), в оригинале boating accident; имя в оригинале Margaret / Margret.
- Мелочи формулировок: масштаб карты 0–5 метров (оригинал 0–15 футов); «метров шестьдесят» (200 feet); «метр семьдесят,
  под семьдесят кило» (five-eight, 160 pounds); «не больше ста грамм» (a few ounces); подписи карты «Распил» (Dispatch),
  «Свежевальня» (Cradle), «Офис» (Records Office); «довольно осторожно» о Сырой Голове (quite stealthy).
- Ночные призраки: в строке «Захват (манёвр)» шанс не напечатан (и в оригинале) — записано «—».

## Не взято

- **Раздатка `[RU 7e] Раздатка «Развеять Мрак» / «None more black».pdf`** (18 с.) — не взята как источник: её содержимое не
  совпадает с книгой и с официальной раздаткой сборника. В ней названия фанатского перевода «Развеять мрак» («Довер», «Мрак»),
  документы, которых в книге нет (страницы дневника 1899–1918 гг., отчёт коронера и полиции Аркхэма от 13 апреля 1921 г. с
  именами Вилсон Хиггинс, Дерек Питерс, Вернон Гилмор; налоговая декларация 1040, договоры залога и купли-продажи, газетная
  колонка, свидетельство о смерти Джона Довера 1919 г.), и другой адрес бойни («Мясозаготовки Кэмпбелла, 11 Халей-стрит»).
  Это самодельный набор к фанатскому переводу, несмотря на метку `[RU 7e]` в имени файла. Вопрос владельцу: оставить
  метку или переименовать файл в `[RU-фан 7e]`.
- Официальная раздатка сборника `[RU 7e] Раздатка «Двери во тьму».pdf` сверена: с. 16 — тот же материал «Чернота 1»,
  с. 22 — карта «Бойня» для игроков (повёрнута). Новых данных нет; картинка карты взята из книги (с. 105).
- Иллюстрации: с. 97 «Вскрытие Уолтера Резника», с. 106 «Сырая Голова да Чёрные Кости» (обе — Уэйн М. Миллер). В записи
  картинки не добавлялись (`images` необязательно, можно позже через `pipeline/art/add_images.py`).
- Без записей, текстом в сценах: безымянный старик-свидетель («Смерть с небес»), «дурная компания» студентов, охрана
  колледжа, хозяин доходного дома, банк, конфисковавший дом Дувров, архивы газеты и библиотеки, племя гвари’кую, джунгли
  Кледа и Мир грёз (места Страны снов в этой части не заводились), дедушкин «Кольт Писмейкер» и машина Дувра (в `possessions`),
  лепёшка с «Шестой Сатлаттой» (в тексте заклинания).
- Оружие: атака «Ближний бой (лом)» у чернушников не связана с записью оружия (отдельной позиции для лома нет).
- Числа листов готовых сыщиков (с. 126–135) с записями не сверялись (как и в части darkness).

## Кандидат в справочник: заклинание «Вызов Черноты»

Справочник заклинаний общий (`kb/spells`), часть его не пишет. Полный текст — в таблице «Заклинание: Вызов Черноты»
сценария; ссылки `spell` у Дувра и в дневнике пока `null`. После заведения записи стоит проставить ссылку в
`character/black-jacob-dover` (`statblock.spells.items[0]`) и `tome/black-jonathan-dover-journal` (`spells[0]`). Черновик:

```json
{
  "schema": "sourcefold.spell.v0",
  "id": "coc:spell:call-the-black",
  "kind": "spell",
  "name": {"ru": "Вызов Черноты", "en": "Call the Black"},
  "aliases": ["Call The Black"],
  "category": "Атака",
  "mechanic": "ритуал",
  "cost": {"raw": "8 пунктов магии; 1 МОЩ; 2d6 пунктов рассудка", "magic_points": "8", "sanity": "2d6", "pow": "1", "other": null},
  "casting_time": {"raw": "3 часа"},
  "description": {"ru": "Заклинание обрушивает живую кровь Йибб-Тистла, так называемую Черноту, на одну цель: мягкие тёмные хлопья прилипают к телу и накапливаются огромной массой, удушая жертву; когда жертва умрёт, Чернота возвращается к Йибб-Тистлу, утаскивая её душу. Первый раунд — проверка ВЫН (успех — 1d2 здоровья, провал — 1d4); второй — трудная проверка ВЫН (1d4/1d6); третий и далее — чрезвычайная (1d6/1d8), пока жертва не умрёт или Черноту не рассеют. Рассеять её могут только смерть колдуна, добровольное снятие чар или большие объёмы (проточной) воды — и, вероятно, обратить против заклинателя. Если вычертить символ «Шестая Сатлатта» на лепёшке из воды и муки и заставить цель её съесть, атака автоматически успешна (без проверок ВЫН, наибольший урон). Призванная без цели, Чернота исчезает, но пара-тройка хлопьев остаётся — Дувры смешивали их со спиртом и делали наркотик.", "en": null},
  "variant_of": null,
  "axes": {"era": ["any"], "ruleset": "core"},
  "sources": [{"book_id": "dveri-vo-tmu-ru", "physical_page": 101, "printed_page": 102, "method": "book_text", "verified": true, "note": "«Двери во тьму», гл. 6 «Чернее чёрного»: врезка «Заклинание: Вызов Черноты»"}],
  "quality": {"needs_review": false, "flags": [], "notes": "Новое заклинание сценария «Чернее чёрного»; его знают Джейкоб Дувр и чернушники, оно в дневнике Джонатана Дувра. Тип и механика — по Р-66/Р-69: связь с божеством и сотворение 3 часа — ритуал."}
}
```

## Предложения

`proposals-black.json` — 6 предложений: `coc:location:arkham` — ссылки на сценарий и город сценария (книга предлагает
Аркхэм, `correction: false`); `coc:spell:contact-yibb-tstll` — псевдонимы «Разговор с Йибб-Тистлом», «Speak With Yibb-Tstll»;
`coc:spell:summon-bind-nightgaunt` — псевдонимы «Вызвать безликого», «Call Down The Faceless Ones» (названия из списка
дневника Джонатана Дувра, с. 104). Пробный прогон `pipeline/integrate/apply.py --dry-run`: 6 правок ложатся, 3 записи.
