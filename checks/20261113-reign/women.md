# «Женщины Французской революции» — часть women: покрытие

Книга `reign-of-terror-women-en` (Women of the French Revolution, Kelly Grant, Chaosium 2023; английский оригинал,
печатная страница = физической). Русского издания нет: весь текст — наш перевод (флаг `translated`, Р-21); названия
навыков и профессий — по глоссарию (`tools/terms.py`, официальные формы). В PDF 11 страниц, а не 12: страницы 12 нет.
Предложения правок общих и чужих записей — `proposals-women.json` (15 правок; пробный прогон
`apply.py proposals-cast.json proposals-women.json --dry-run` проходит: якорь у `coc:occupation:shpion` — конец абзаца
части cast, поэтому файл применяется после `proposals-cast.json`).

Сокращения путей: `ch/` = `kb/books/reign-of-terror-women-en/characters/`, `occ/` = `kb/occupations/`, `r/` = `kb/rules/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Women of the French Revolution» | 1 | не взято — см. ниже |
| Credits | 2 | не взято — см. ниже |
| Dedication: Kelly Grant (1964–2023) | 3 | не взято — см. ниже |
| Бланк листа сыщика «Reign of Terror» | 4 | `r/reign-women-investigators.json`, таблица «Лист сыщика «Царства Террора»: базовые значения навыков» |
| Women of the Revolution | 5 | `r/reign-women-of-the-revolution.json` |
| The Rights of Women: Before, During, & After Revolution | 5 | `r/reign-women-of-the-revolution.json` (`text`) |
| Врезка «Newspapers» | 5 | `r/reign-women-of-the-revolution.json` (абзац «Газеты») |
| Investigator Occupations | 6 | `r/reign-women-investigators.json` |
| Working Class | 6 | `r/reign-women-investigators.json` (текст, таблица «Роды занятий сыщиц по классам») |
| Абзацы о парикмахерском деле (мадам Мартен, Легро де Рюминьи, Леонар) | 6 | `occ/parikmakher.json` (`description`) |
| Врезка «Jeanne Baret» | 6 | `ch/jeanne-baret.json` |
| Explorer | 7 | предложение к `coc:occupation:puteshestvennik` (абзац + источник); строка таблицы `r/reign-women-investigators.json` |
| Hairdresser | 7 | `occ/parikmakher.json` |
| Sans-culotte (commoner) | 7 | предложение к `coc:occupation:sankyulot` (часть cast); строка таблицы |
| Spy | 7 | предложение к `coc:occupation:shpion`; строка таблицы |
| Врезка «Claire Lacombe» | 7 | `ch/claire-lacombe.json` |
| Bourgeoisie | 7 | `r/reign-women-investigators.json` (текст, таблица по классам) |
| Абзац о женщинах в ополчении и армии | 8 | `r/reign-women-investigators.json` (абзац «Женщины в армии») |
| Врезка «Théroigne de Méricourt» | 8 | `ch/theroigne-de-mericourt.json` |
| Врезка «The Salons» | 9 | `r/reign-women-salons.json` |
| Artist Entrepreneur | 9 | `occ/khudozhnik-predprinimatel.json` |
| Courtesan | 9 | `occ/kurtizanka.json`; предложение `occupation_ref` для `tsarstvo-terrora-ru/character/celine-bessette` |
| Midwife | 9 | `occ/povitukha.json` |
| Political Activist | 9 | `occ/politicheskiy-aktivist.json` |
| Врезка «Marie Tussaud» | 9 | `ch/marie-tussaud.json`; предложение к `tsarstvo-terrora-ru/location/reign-palais-royal` (выставка Кюртиуса) |
| Врезка «Angélique du Coudray, Doctor, & Midwife» | 10 | `ch/angelique-du-coudray.json` |
| Врезка «Etta Palm d’Aelders» | 10 | `ch/etta-palm-daelders.json` |
| Noblewomen | 10–11 | `r/reign-women-investigators.json` (абзацы «Знатные дамы») |
| Noble (Aristocrat) | 11 | предложение к `coc:occupation:dvoryanin` (часть cast); строка таблицы |
| Врезка «Charlotte Corday» | 11 | `ch/charlotte-corday.json` |
| Врезка «The September Massacres, 1792» | 11 | `r/reign-women-of-the-revolution.json` (абзац «Сентябрьские убийства 1792 года») |

Ещё предложения: штурм Тюильри 10 августа 1792 года с участием Лакомб и Мерикур — абзац и `refs` у
`tsarstvo-terrora-ru/location/paris-tuileries`; `refs` правила `coc:rule:reign-social-class` →
`coc:rule:reign-women-investigators`.

## Не взято

- Обложка (с. 1), выходные данные (с. 2) и посвящение памяти Kelly Grant (с. 3: её проекты для Chaosium, текст был
  написан для второго тома «Love Eterne») — не игровой материал.
- Иллюстрации: шествие вооружённых женщин (с. 8), пентаграмма (с. 9), портрет дамы (с. 11), декоративная рамка
  бланка (с. 4) — картинки, для kb-art позже.
- Упомянутые без своей врезки люди (мадам Мартен, Легро де Рюминьи, Леонар, Филипп Кюртиус, Альфонс Леруа, Жан-Поль
  Марат, Жозеф Фуше, Робеспьер, Бугенвиль, Коммерсон, маркиза де Кондорсе, Олимпия де Гуж) — текстом в записях, своих
  записей нет. Кандидат в запись — Жан-Поль Марат (встречается в четырёх врезках и в «Царстве Террора», с. 99, 112). — частично: запись Робеспьера есть («Царство Террора»), ссылка из правила «Роды занятий сыщиц» — уборка 2026-11-14, `checks/20261114-tidy.md`.
- Роды занятий только из списков, без профиля (перчаточница, автор газетных статей, швея, владелица лавки, хозяйка
  салона, философ, переводчица) — в таблице «Роды занятий сыщиц по классам», своих записей нет.

## Опечатки и сомнения

- Теруань де Мерикур: «в октябре 1794 года… провела 20 лет и умерла в 1804 году» — даты не сходятся (`errata`).
- Художник-предприниматель: Убеждение и в списке, и среди навыков общения на выбор (`errata`).
- «В 1792 году Национальное собрание» — по хронологии «Царства Террора» (с. 98) в 1792 году было Законодательное
  собрание, затем Конвент; оставлено как в книге, пометка в `quality.notes`.
- Шпион: «Language (French)» — для француженки это родной язык; передано как напечатано («Язык (Французский)»).
- Санкюлот дополнения отличается от «Царства Террора»: Вождение и Пилотирование даны оба, дополнительный навык один.
- Дворянин дополнения: Средства 5–70 (в «Царстве Террора» 50–99) — так задумано книгой (конфискации), не опечатка.
- Ссылки персонажей на роды занятий (`occupation_ref`) — вывод из текста (Р-41): в книге биографии — примеры к
  разделам, профессий у них нет.
