# gg-rules — Grand Grimoire, главы 1–3 и врезки (Р-242)

Книга `grand-grimoire-en`; страницы: физ. 6–26, 72, 86, 134, 186 (печатные — на 1 меньше). Русский текст — наш пересказ
(флаг `translated`). Работа закончена; `python tools/check.py` по 24 файлам — 0 ошибок.

| Заголовок книги | Страница (печ.) | Где в базе |
|---|---|---|
| Introduction (Mike Mason) | 5 | не взято — служебное вступление без игрового содержания |
| Гл. 1 Concerning Magic (вступление) | 7 | `coc:rule:gg-state-of-mind` |
| State of Mind; Working Space; Watch the Heavens | 7 | `coc:rule:gg-state-of-mind` |
| The Nature of Sacrifice | 7–8 | `coc:rule:gg-the-nature-of-sacrifice` |
| Are the Stars Right? | 8 | `coc:rule:gg-are-the-stars-right` |
| Days of the Week (таблица) | 9 | `coc:rule:gg-are-the-stars-right`, tables «Дни недели» |
| Phases of the Moon (таблица) | 9 | `coc:rule:gg-are-the-stars-right`, tables «Фазы луны» (errata 180–255) |
| Wheel of the Year; Fire Festivals; Solar Festivals | 10 | `coc:rule:gg-are-the-stars-right`, tables «Колесо года» |
| Other Astronomical Factors | 10 | `coc:rule:gg-are-the-stars-right`, tables «Прочие астрономические факторы» |
| Врезки-воззвания (Rural invocation, Appeal to the Outer Ones) | 8, 10 | `coc:rule:gg-are-the-stars-right` (упомянуты, начало формул цитатой) |
| Гл. 2 Concerning Spells (вступление) | 11 | `coc:rule:gg-concerning-spells` |
| Spell Names | 11 | `coc:rule:gg-spell-names` |
| Deeper Magic; Deeper Magic in Play | 11–12 | предложение (proposals-gg-rules.json): источник GG к `coc:rule:deeper-magic` |
| Adjusting Spells | 12 | `coc:rule:gg-adjusting-spells` |
| Difficulties in Spellcasting | 12 | `coc:rule:gg-difficulties-in-spellcasting` |
| Folk Magic | 13 | `coc:rule:gg-folk-magic` |
| Flawed Spells | 13 | `coc:rule:gg-flawed-spells` |
| Dreamlands Magic; Spellcasting in the Dreamlands | 14 | `coc:rule:gg-dreamlands-magic` |
| Spirit Attacks and Possession | 14 | `coc:rule:gg-spirit-attacks-and-possession` |
| Spell Components | 15, 18 | `coc:rule:gg-spell-components` |
| Magical Tools (врезка) | 15 | `coc:rule:gg-magical-tools` |
| Table 1: Spell Components | 16–17 | `coc:table:spell-components` |
| Amulets; Talismans (врезки) | 18 | `coc:rule:gg-amulets-and-talismans` |
| Magical Residue | 18–19 | `coc:rule:gg-magical-residue` |
| Residual Magical Effects | 19 | `coc:rule:gg-residual-magical-effects` |
| Ley Lines; Tracks Around the World; Ley Lines and Magic | 19–21 | `coc:rule:gg-ley-lines` |
| Врезка о предложениях главы (без заголовка) | 21 | `coc:rule:gg-concerning-spells` |
| Fictional Magic | 21 | `coc:rule:gg-fictional-magic` |
| Гл. 3 Spell Categories; Categories (17 списков) | 22–25 | не взято — фильтр (повтор); категории GG — справочный список названий заклинаний |
| Entry Format | 25 | `coc:rule:gg-spell-entry-format` |
| Call, Contact, and Summon Disambiguation | 25 | предложение (proposals-gg-rules.json): источник GG к `coc:rule:call-contact-and-summon-disambiguation` |
| Conjuration of the Turua (врезка) | 71 | `coc:rule:gg-conjuration-of-the-turua` (профиль туруа — в tables) |
| NPC: Hestia Locksby | 85 | `grand-grimoire-en/character/hestia-locksby` |
| NPC: Thomas Davenport | 133 | `grand-grimoire-en/character/thomas-davenport` |
| NPC: Niels-Viggo Schou | 185 | `grand-grimoire-en/character/niels-viggo-schou` |

## Не взято

- Introduction (с. 5) — служебное вступление редакции без игрового содержания.
- Гл. 3 Spell Categories (с. 22–25): 17 списков названий заклинаний по категориям GG — запись трижды останавливалась на фильтре
  содержимого; не взято. У заклинаний базы своя классификация из 14 типов (Р-66). Перенести можно позже, таблицей
  «Категория | заклинания» без пересказа.
- Эпиграфы глав (Кроули, Гейл З. Мартин, Нил Гейман, «Зловещие мертвецы», «Макбет») — цитаты из художественных и
  оккультных книг, без механики.
- Подписи к иллюстрациям («Opposite: …»), колонтитулы, иконки категорий.

## Предложения

`proposals-gg-rules.json` — 3 правки: источник Grand Grimoire к `coc:rule:deeper-magic`,
`coc:rule:call-contact-and-summon-disambiguation`, `coc:rule:casting-time-and-spells-in-combat` (пробный прогон `apply.py` — ложатся).

## Кандидаты в записи и вопросы

- Туруа — профиль лежит таблицей в `coc:rule:gg-conjuration-of-the-turua`; кандидат в запись существа. В категориях GG
  ритуал значится заклинанием «Conjuration of The Turua»: если часть gg-spells заведёт `coc:spell:conjuration-of-the-turua`,
  запись правила стоит слить с ним.
- Заклинания без записей (ссылки не поставлены): Opaque Wall, Devolution (упомянуты в «Магии Страны грёз»); у Дэвенпорта —
  Reanimation, Remortification, Soul-Trap.
- Книга «The Severance Aphopsis» (Хестия Локсби), Оборванец Ник (Ragged Nick) — упомянуты текстом, записей нет.
- Опечатки: фазы луны — полнолуние «180–255» перекрывается с убывающей луной (errata, как напечатано); у Дэвенпорта в
  биографии один раз назван «Lawrence» (errata, исправлено); «Grave dirt» дважды в таблице 1 (строки 17 и 69, как напечатано).