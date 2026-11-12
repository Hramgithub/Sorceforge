# «Ничего, кроме ветра» (nichego-krome-vetra-ru) — сверка покрытия

Книга: официальный русский перевод сценария Miskatonic Repository (автор — Пи Джей Стивенс, 2020), 17 страниц PDF
с текстовым слоем; листы готовых персонажей (с. 6–13) напечатаны по-английски. Эпоха — Тёмные века (`dark-ages`),
правила — ядро 7-й редакции. Страницы: печатная = физическая − 4 (физ. 1–4 — обложка, иллюстрация, выходные данные «iii»,
содержание «iv»; физ. 5 = с. 1, физ. 17 = с. 13).

Префикс записей: `nichego-krome-vetra-ru/`.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка («Ничего, кроме ветра», Джей Пи Стивенс) | i (физ. 1) | `scenario/nichego-krome-vetra` (summary, sources, quality.notes) |
| Иллюстрация (заснеженный лес) | ii (физ. 2) | не взято — см. ниже |
| Выходные данные (автор, тестеры, ©) | iii (физ. 3) | `scenario/nichego-krome-vetra` (summary: автор, 2020; quality.notes) |
| Содержание | iv (физ. 4) | не взято — см. ниже |
| Введение | 1 | `scenario/nichego-krome-vetra` (summary) |
| Ведение игры | 1 | `scenario/nichego-krome-vetra` (advice) |
| История | 1 | `scenario/nichego-krome-vetra` (keeper_info «История», hook) |
| Секрет Хранителя | 1 | `scenario/nichego-krome-vetra` (keeper_info «Секрет Хранителя»); `creature/osedlavshiy-veter`, `creature/vendigo` |
| Структура сценария | 1 | `scenario/nichego-krome-vetra` (advice, steps); ссылка на `coc:rule:spending-luck` |
| Навыки Мифической Исландии | 1 | `scenario/nichego-krome-vetra` (таблица «Навыки Мифической Исландии») |
| Начало: день первый | 2 | `scene/pribytie`; `location/bereg`, `location/voyushchaya-skala` |
| Местные предания (в книге «Местные придания») | 2 | `scene/mestnye-predaniya` |
| Деревня Воющих Скал (в содержании «Деревня Воющей Скалы») | 2 | `scene/derevnya`; `location/voyushchaya-skala`, `location/zabroshennye-vigvamy`, `location/zhiloy-vigvam`; `item/risunki-chudovishcha` |
| Охота | 2 | `scene/okhota`; `location/les` |
| Леса | 2 | `scene/lesa`; `location/les`, `location/zamerzshiy-prud`, `location/okrestnosti-voyushchey-skaly` |
| Ужин | 2 | `scene/uzhin` (errata: «Заражение» → «Инфекция») |
| Карта Воющих Скал | 3 | `map/voyushchaya-skala` (картинка `app/maps/wind-voyushchaya-skala.jpg`, 11 вычисленных меток: 8 хижин, кострище, лес ×2) |
| Жители деревни | 4 | `scene/zhiteli-derevni`; `location/zhiloy-vigvam` |
| Акна, мать | 4 | `character/akna` |
| Кумаглак, взрослый сын | 4 | `character/kumaglak` |
| Тигуаак, отец | 4 | `character/tiguaak` |
| Приход ночи | 4 | `scene/prikhod-nochi` |
| День второй | 4 | `scene/den-vtoroy` |
| День третий | 4 | `scene/den-tretiy` |
| Эпилог | 4 | `scene/epilog`; `scenario/nichego-krome-vetra` (conclusion) |
| Награды | 4 | `scene/epilog`; `scenario/nichego-krome-vetra` (conclusion) |
| Противники | 5 | `creature/vendigo`, `creature/osedlavshiy-veter` |
| Вендиго (эпиграф Дерлета, описание, культ) | 5 | `creature/vendigo` (legend, cult) |
| Итакуа, Оседлавший Ветер, он же Вендиго (статблок) | 5 | `creature/vendigo` (statblock, abilities) → `avatar_of` `coc:creature:ithaqua` |
| Оседлавший Ветер | 5 | `creature/osedlavshiy-veter` (description) |
| Оседлавший Ветер, Хищный Каннибал (статблок) | 5 | `creature/osedlavshiy-veter` (statblock, abilities) → `instance_of` `coc:creature:wind-walker` |
| Готовые персонажи | 5 | `scenario/nichego-krome-vetra` (advice, steps «Подготовка»); персонажи ниже |
| Лист: Bjorn the Large (лицо и оборот) | 6–7 | `character/bjorn` |
| Лист: Hrappur the Deep Minded | 8–9 | `character/hrappur` |
| Лист: Egill the Vicious | 10–11 | `character/egill` |
| Лист: Ulfhildur the Brave | 12–13 | `character/ulfhildur` |

## Не взято

- Иллюстрация на физ. с. 2 (заснеженный лес) и обложка как картинка — оформление без игровых сведений.
- Содержание (с. iv) — служебная страница; все её заголовки — в таблице выше.
- Список тестеров (с. iii) — не игровые сведения.
- «Краткие правила» и «Ранения и лечение» на обороте листов персонажей (Quick Reference Rules) — типовой текст бланка
  «Мифической Исландии», повторяет «Книгу хранителя»; силуэты-заглушки вместо портретов на листах.
- Пустые поля бланков (игрок, возраст, место жительства, Удача, деньги и имущество) — в книге не заполнены
  (о возрасте и Удаче сказано в quality.notes персонажей).

## Сомнения и опечатки (в записях — как напечатано)

- Деревня: в тексте девять вигвамов кольцом, на карте восемь хижин — errata `location/voyushchaya-skala`.
- «Ужин» отсылает к способности «Заражение», в статблоке она «Инфекция» — errata `scene/uzhin` (исправлено в записи).
- Эгиль: «Знания о регионе» 20 при базе «половина ИНТ» = 25 — errata `character/egill`.
- Имена: «Кумаглак»/«Кумуглак», «Тигуаак»/«Тигуак» (с. 4) — в aliases.
- Автор: на обложке «Джей Пи Стивенс», в выходных данных «Пи Джей Стивенс».
- Деревянный щит: у Бьёрна урон 2d4, у Храппура 1d4 — как напечатано.
- Нож Ульфхильдур: урон «1d6 + половина БкУ» (обычно у рукопашного ножа полный БкУ) — как напечатано.
- Статблок Вендиго дословно из «Книги хранителя» (с. 317), общая запись Итакуа — по Malleus (урон ближнего боя 4d6 против 8d6
  здесь) — поэтому профиль сценария отдельной записью.

## Кандидаты в новые общие записи (только в отчёте)

- Навыки «Мифической Исландии» (`kb/skills/`): Озарение (Insight), Пророчество (Prophecy), Второе зрение (Second Sight),
  Знания о регионе (Regional Knowledge), Катание на лыжах (Skiing), Статус (Status), Грамотность (Literacy).
- Оружие «Мифической Исландии» (`kb/weapons/`): боевой молот, большой топор, ручной топор (метательный), копьё (ближний бой),
  нож; деревянный щит.
- Профессии: вождь (Chieftain), мудрец (Sage), берсерк (Berserker), разведчик (Scout).
