# «Маленький клуб ужасов» (malenkiy-klub-uzhasov-ru) — сверка покрытия

Книга: сценарий «Маленький клуб ужасов» Ли Карра (Trepan Interactive, 2017), русский перевод SNOKYAN; 20 страниц PDF
с текстовым слоем (метка владельца «[RU 7e]»). В текстовом слое нет заголовков, названий навыков (выделены жирным) и
имён на листах персонажей — всё это и все числа сверены по изображениям страниц (110 dpi). Система — «Зов Ктулху»
7-й редакции, ядро (проценты с половиной и пятой, Комплекция, БкУ, трудные/чрезвычайные проверки): `ruleset: "core"`.
Эпоха — «Современная эпоха или 1920-е годы» (с. 3; действие 28 октября 2017 года, врезка о переносе в 1920-е на с. 13)
— `era: ["modern", "1920s"]`.

Страницы: печатная = физической (смещение 0): номера стоят со с. 2 (на с. 3 — «3»), с. 1 и 20 — обложки без номера.

Префикс записей: `malenkiy-klub-uzhasov-ru/`. Общий город — `coc:location:lincoln` (новый, `kb/locations/lincoln.json`):
других записей Линкольна в базе нет, другие части этого плана в Линкольне не происходят. Места вне города — в области
`location/okrestnosti-linkolna` (Р-209). Карт в книге нет (хотя в выходных данных указан автор «Карт»).

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Маленький клуб ужасов» | 1 | `scenario/malenkiy-klub-uzhasov` (sources) |
| Титул | 2 | `scenario/malenkiy-klub-uzhasov` (name) |
| Выходные данные (сценарий, редактура, иллюстрации, тестировщики, перевод) | 3 | `scenario/malenkiy-klub-uzhasov` (summary) |
| Описание Сценария (система, время, игроки, эпоха, локация; завязка) | 3 | `scenario/malenkiy-klub-uzhasov` (summary, keeper_info); `coc:location:lincoln` |
| Информация для Хранителя | 3 | `scenario/malenkiy-klub-uzhasov` (advice); `character/tayler-bruks`, `character/evan-ross`; `scene/drugie-ischeznoveniya` |
| Город Линкольн (текст для чтения вслух) | 4 | `scene/drug-v-bede`; `coc:location:lincoln` |
| Друг в беде | 4 | `scene/drug-v-bede`; `character/devid-laynkhem`, `character/gregori-miller` |
| Дело о пропавшем Смозерсе (слухи, шериф, отец) | 4 | `scene/delo-o-propavshem-smozerse`; таблица «Слухи о пропаже Смозерса» в `scenario/…`; `character/uolter-martin`, `character/alan-smozers`; `location/politseyskiy-uchastok-linkolna`, `location/treyler-smozersov`, `location/odinokoe-ozero` |
| Другие исчезновения близ Линкольна | 5 | `scene/drugie-ischeznoveniya`; таблица «Другие исчезновения близ Линкольна» в `scenario/…`; `location/biblioteka-linkolna`, `location/okrestnosti-linkolna` |
| Тропа к Клубу через особняк Мэдисон | 5–6 | `scene/tropa-cherez-osobnyak-medisona`; `location/osobnyak-medisona`, `location/tonnel-pod-osobnyakom`; `item/mashina-medisona`, `item/bumagi-medisona`; `character/dzheyms-medison` |
| Вырезка «Вестник Линкольна» (22 мая 1907 года) | 5 | `handout/vestnik-linkolna-1907` |
| Поляна Клуба | 6 | `scene/polyana-kluba`; `location/polyana-kluba`, `location/nora-pod-kornyami`; `handout/pismo-miss-kheyz`; `item/oblomki-kostey`, `item/izurodovannyy-krolik`; `character/miss-kheyz` |
| Врезка об альбоме Смозерса | 6 | `item/albom-smozersa` |
| Клуб | 6–7 | `scene/klub`; `location/klub`; `item/zapisnaya-knizhka-smozersa`; `handout/nadpisi-na-stenakh-kluba` |
| Смозерс атакует | 7 | `scene/smozers-atakuet`; `character/stiven-smozers` (способность «Особые силы») |
| Физические атаки: Психокинез, Падающие деревья | 8 | `character/stiven-smozers` (способности); таблица «Атаки Смозерса» в `scenario/…` |
| Атака стаи красных белок | 8 | `creature/krasnye-belki`; `character/stiven-smozers` (способность) |
| Контроль над сыщиком | 8 | `character/stiven-smozers` (способность) |
| Нападение лося | 8–9 | `creature/los` (instance_of `coc:creature:moose`); `character/stiven-smozers` (способность) |
| Нападение чёрного медведя | 9 | `coc:creature:bear` (профиль совпадает; источник — предложением); `character/stiven-smozers` (способность с числами книги) |
| Психологические атаки: Марш насекомых, Лагерный костёр, Наблюдающие глаза, Биение гниющего сердца, Видение Ахм’хлти | 9 | `character/stiven-smozers` (способности); таблица «Атаки Смозерса» |
| Бежать или звать на помощь | 10 | `scene/bezhat-ili-zvat-na-pomoshch`; `character/ofitsery-sherifa`, `character/okhotniki` |
| Смерть туристов | 10 | `scene/smert-turistov`; `character/rouen-kritchli`, `character/dzhordan-kritchli`, `character/neytan-myuller` |
| Смозерс и его путешествие домой | 10–11 | `scene/puteshestvie-domoy`; `character/stiven-smozers` (способность «Возвращение по частям») |
| Родовой канал Ахм’хлти | 11 | `scene/rodovoy-kanal`; `location/rodovoy-kanal-akhmkhlti` |
| Чрево Ахм’хлти | 11 | `scene/chrevo-akhmkhlti`; `location/chrevo-akhmkhlti`; `creature/akhmkhlti` |
| Стивен Смозерс (статблок, описание) | 12 | `character/stiven-smozers` |
| Смерть Смозерса | 12 | `scene/smert-smozersa`; `scenario/…` (conclusion) |
| Поглощённый Ахм’хлти | 12 | `scene/pogloshchyonnyy-akhmkhlti`; `creature/akhmkhlti` (encounters) |
| Финал: Покинуть поляну и никогда не возвращаться | 12 | `scene/pokinut-polyanu` |
| Сжечь здание Клуба и поляну | 12 | `scene/szhech-klub` |
| Побег из Клуба | 12 | `scene/pobeg-iz-kluba` |
| Возвращение Смозерса | 12–13 | `scene/vozvrashchenie-smozersa`; `character/stiven-smozers` (способность «Вернувшийся на Землю») |
| Преобразование в эпоху 1920-х годов (Город Линкольн, Школа Линкольна, Особняк Мэдисона, Родители Лайнхэма, Мобильные телефоны / смартфоны, Интерьер Клуба, Умения готового сыщика, Биография готового сыщика) | 13 | таблица «Преобразование в эпоху 1920-х годов» в `scenario/…`; те же сведения — в `coc:location:lincoln`, `location/srednyaya-shkola-linkolna`, `location/osobnyak-medisona`, `location/klub`, `item/mashina-medisona`, родителях Лайнхэма и прегенах |
| Персонажи: Дэвид Лайнхэм | 14 | `character/devid-laynkhem`; `character/geyl-laynkhem`, `character/semyuel-laynkhem` |
| Персонажи: Грегори Миллер | 15 | `character/gregori-miller`; `character/pol-miller`, `character/syu-miller` |
| Персонажи: Уолтер Мартин | 16 | `character/uolter-martin` |
| Готовые сыщики: Студент театрального факультета и Президент Школьного Совета | 17 | `character/tayler-bruks` (имя придумано, Р-150) |
| Готовые сыщики: Атлет | 17 | `character/rayan-kallakhan` (имя придумано) |
| Готовые сыщики: Тусовщик | 18 | `character/kodi-bennet` (имя придумано) |
| Готовые сыщики: Отличник | 18 | `character/evan-ross` (имя придумано) |
| Авторские права, благодарности | 19 | `scenario/…` (summary: автор, издатель, год) |
| Задняя обложка (аннотация) | 20 | `scenario/…` (summary) |

## Опечатки и сомнения книги

- Уолтер Мартин (с. 16): «Ближний бой (Драка) 65% (30/12)» — доли от 60%; «Уклонение 35% (21/8)» — доли от 42%;
  в списке навыков «Уклонение 40%». Доли исправлены (Р-35, Р-77), проценты — как напечатаны; `errata`.
- Красные белки (с. 8): «Укус 35% (12/5)» — доли от 25%; исправлены на 17/7 (Р-77).
- Президент Школьного Совета (с. 17): «Уклонение 20% (8/4)» → 10/4.
- Тусовщик (с. 18): «Электрика 205» — знак % набран как 5; в записи 20%.
- Лось (с. 8): БкУ +3d6 и Комплекция 4 при СИЛ 140 + ТЕЛ 165 = 305 (полагается +4d6 и 5); как напечатано (Р-36).
- С. 13: «Победа над Смозерсом вознаградит сыщиков потерей 1D10 Рассудка» — противоречие; вероятно, награда +1d10
  (как за убийство в Чреве, с. 12). Как напечатано, `errata` в сценарии и сцене «Возвращение Смозерса».
- «Наука Психология 60%» у Президента — в 7e Психология не специализация Науки; ссылка на навык Психология.
- «Юриспунденция» (Мартин), «Юриспуденция» (Отличник) — названия навыков как напечатаны.
- Возраст Смозерса «7 лет» (с. 12) при «бывшем друге» восьмилетнего Лайнхэма — как напечатано.
- Медведь «Нападения чёрного медведя» (с. 9) совпадает с медведем «Книги хранителя» (без брони, с МОЩ 50) — своя запись
  не заведена (Р-79).

## Не взято

- Иллюстрации: обложка (с. 1), лось у Клуба (с. 7), рука, растущая из трупа (с. 10), Ахм’хлти (с. 11), портреты
  Лайнхэма, Миллера и Мартина (с. 14–16), фон задней обложки (с. 20) — помощник не владеет `app/art/`; можно добавить
  позже `pipeline/art/add_images.py`.
- Список тестировщиков и благодарности (с. 3, 19) — не игровой материал; автор, издатель, переводчик и год — в summary.
- Безымянные лица только из предыстории — текстом, без записей: турист-врач, нашедший кости; подростки — любители
  хэви-метала у особняка; мать Смозерса (умерла при родах); собака Лайнхэма Капитан Гав; универсальный магазин Миллеров;
  криминалистическая лаборатория в Конкорде; Национальный лес Большой Белой горы.
- Вещи тайника (спички, карандаши, мел, охотничий ножик, фляжка виски), фонарик, комиксы, 23 доллара и игровое
  устройство Лайнхэма — текстом в местах и сценах, без отдельных записей (механики нет).
