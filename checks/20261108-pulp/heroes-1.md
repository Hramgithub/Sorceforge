# Pulp Cthulhu (en), часть heroes-1: с. 7–8, 15–23

Введение (Пульп-о-метр, Pulp Cthulhu в обычном «Зове Ктулху») и глава 2, шаги 1–2: создание пульп-героев,
все 22 архетипа, определение характеристик. Книга `pulp-cthulhu-en`, печатная страница = физическая − 1.

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Introduction (By Mike Mason) | 7 | `coc:rule:pulp-introduction` |
| Pulp-O-Meter: How Much Pulp? | 7–8 | `coc:rule:pulp-o-meter` (текст, шаги, таблица «Уровни пульпа») |
| Low pulp / Mid pulp / High pulp (список) | 8 | `coc:rule:pulp-o-meter` |
| Using Pulp Cthulhu with Call of Cthulhu | 8 | `coc:rule:pulp-using-pulp-with-call-of-cthulhu` |
| Chapter 2: Creating Pulp Heroes (вступление) | 15 | `coc:rule:pulp-creating-pulp-heroes` |
| Creating Pulp Heroes (семь шагов) | 15 | `coc:rule:pulp-creating-pulp-heroes` (`steps`) |
| Option (врезка) | 15 | `coc:rule:pulp-creating-pulp-heroes` (абзац «Вариант», последний шаг) |
| Step One: Choose a Pulp Archetype | 15 | `coc:rule:pulp-choose-a-pulp-archetype` |
| Guidance notes (врезка) | 15 | `coc:rule:pulp-choose-a-pulp-archetype` («Пояснения») |
| Pulp Archetypes (врезка-список) | 16 | `coc:rule:pulp-choose-a-pulp-archetype` (таблица «Пульп-архетипы», `refs` на 22 архетипа) |
| Adventurer | 15–16 | `coc:archetype:adventurer` |
| Beefcake | 16 | `coc:archetype:beefcake` |
| Bon Vivant | 16 | `coc:archetype:bon-vivant` |
| Cold Blooded | 16–17 | `coc:archetype:cold-blooded` |
| Dreamer | 17 | `coc:archetype:dreamer` |
| Egghead | 17–18 | `coc:archetype:egghead` |
| Explorer | 18 | `coc:archetype:explorer` |
| Femme Fatale | 18–19 | `coc:archetype:femme-fatale` |
| Grease Monkey | 19 | `coc:archetype:grease-monkey` |
| Hard Boiled | 19 | `coc:archetype:hard-boiled` |
| Harlequin | 19 | `coc:archetype:harlequin` |
| Hunter | 19–20 | `coc:archetype:hunter` |
| Mystic | 20 | `coc:archetype:mystic` |
| Outsider | 20 | `coc:archetype:outsider` |
| Rogue | 20 | `coc:archetype:rogue` |
| Scholar | 20–21 | `coc:archetype:scholar` (особое правило — `notes`) |
| Seeker | 21 | `coc:archetype:seeker` |
| Sidekick | 21 | `coc:archetype:sidekick` |
| Steadfast | 22 | `coc:archetype:steadfast` |
| Swashbuckler | 22 | `coc:archetype:swashbuckler` |
| Thrill Seeker | 22 | `coc:archetype:thrill-seeker` |
| Two-Fisted | 22 | `coc:archetype:two-fisted` |
| Adjustments (у каждого архетипа) | 15–22 | поля архетипа: `core_characteristic`, `bonus_points`, `bonus_skills`, `suggested_occupations`, `talents`, `suggested_traits`, `notes` |
| Step Two: Generate Characteristics | 23 | `coc:rule:pulp-generate-characteristics` |
| Age | 23 | `coc:rule:pulp-generate-characteristics` |
| Determine Other Attributes | 23 | `coc:rule:pulp-generate-characteristics` |
| Table 1: Damage Bonus and Build | 23 | `coc:rule:pulp-generate-characteristics` (`tables[0]`) |
| Table 2: Movement Rates | 23 | `coc:rule:pulp-generate-characteristics` (`tables[1]`) |
| Step Three: Determine Pulp Talents | 23 | часть heroes-2 (`coc:rule:pulp-determine-pulp-talents`) |

## Опечатки и сомнения книги (в `errata` записей)

- Hunter (с. 19–20): рекомендуемые профессии слово в слово повторяют список Hard Boiled — `coc:archetype:hunter`.
- Mystic (с. 20): черты слово в слово повторяют черты Harlequin; талант Psychic в описании «обязателен», в поправках «рекомендуется», а в таблице талантов он называется Psychic Power — `coc:archetype:mystic`.
- Scholar (с. 21): ссылка «Chapter 9: Sanity» — правило «Вера в Мифы» стоит в главе 9 «Магия» «Книги хранителя» — `coc:archetype:scholar`.
- Таблица 1 (с. 23): у строки 85–124 пуст столбец Build (по ядру 0); таблица 2: заголовок столбца «STR+SIZ» вместо сравнения ЛВК, СИЛ и ТЕЛ — `coc:rule:pulp-generate-characteristics`.
- Мелочи без записи в errata (Р-39): Outsider — Navigation вместо Navigate; Steadfast и Swashbuckler — Private Detective вместо Private Investigator; Swashbuckler — «life&quot;.» (мусор вёрстки); Scholar — лишняя закрывающая кавычка; Computer Use у Egghead при эпохе 1930-х (оставлено как напечатано, пометка в `quality.notes`).

## Не взято

- Иллюстрации: фронтиспис главы 2 «The Monday Night Heroes» (Victor Manuel Leza Moreno, с. 15) и рисунки архетипов (Chris Lackey, с. 17, 18, 21) с подписями-названиями архетипов — картинки без правил; переносятся отдельно через `pipeline/art/add_images.py`, если владелец решит.
- Декоративная вертикальная надпись по краю страниц (с. 8, 16, 18, 20, 22) и колонтитулы — оформление.
- Глава 1 (с. 9–14) в эту часть не входит.
