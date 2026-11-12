# «Не забывай меня» (ne-zabyvay-menya-ru) — сверка покрытия

Книга: сценарий «Не забывай меня», 28 страниц PDF с текстовым слоем (метка владельца «[RU 7e]»). На титуле — «Forget Me
Not, by Brian M. Sammons»: это русский перевод сценария Брайана М. Сэммонса; оригинала в библиотеке нет. Система —
«Зов Ктулху» 7-й редакции, ядро (`ruleset: "core"`), но местами книга пользуется механикой прежних редакций (проверка
Идеи и половины Идеи, «ЛОВ×3», «INT×2/×3», «Телосложения ×3», «МР 9%») — в записях как напечатано. Эпоха — современность
(телефоны, GPS, ноутбуки) — `era: ["modern"]`; год не назван (вероятно, 2011–2013: в апреле 2011 года Ванесса уже
отвечает за дом, раздатка №4, а унаследовала его «два года назад»). Год «2020» в каталоге владельца книгой не
подтверждается.

Страницы: номеров на страницах нет, печатная = физическая (смещение 0). Физ. 19 и 22 — карты, физ. 23 — почти пустая,
физ. 24 — врезка, закрывающая начало абзаца о втором этаже (оно есть только в текстовом слое).

Числа, раздатки-вырезки (с. 8–11) и обе карты сверены по изображениям страниц. Префикс записей: `ne-zabyvay-menya-ru/`.
Общий город — `coc:location:clio` (новый, `kb/locations/clio.json`): записи Клайо в базе не было, другие части плана здесь
не происходят.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Титул «Forget Me Not» | 1 | `scenario/ne-zabyvay-menya` (name.en, summary, sources) |
| Введение | 1 | `scenario/ne-zabyvay-menya` (summary, advice); `organization/supernatural-files` |
| Пробуждение | 1–2 | `scene/probuzhdenie`; `item/furgon`, `item/klyuch-karty`; `location/doroga-makkamsi`; `coc:location:clio` |
| Информация для Хранителя | 3 | `scenario/ne-zabyvay-menya` (keeper_info); `character/lin-kartrayt`; `creature/potomstvo-eykhorta` |
| Врезка «Лабиринт Эйхорта» | 3 | `location/labirint-eykhorta`; `scenario` (advice) |
| Врезка «Опытные сыщики и возгласы “Мой персонаж так бы не поступил!”» | 3 | `scenario` (advice) |
| Сразу на грани безумия (арахнофобия, клаустрофобия, ситофобия, мизофобия) | 4–5 | `scenario` (advice, таблица «Безумия на выбор»; потери за воспоминания — вступление таблицы «Воспоминания») |
| Спутанные воспоминания | 5 | `scenario` (таблица «Воспоминания») |
| Врезка «Роли в шоу» | 5 | `scenario` (таблица «Роли в шоу»); `organization/supernatural-files` |
| После аварии; воспоминание о доме Куперов | 5–6 | `scene/posle-avarii`; `location/ferma-beykerov`; `character/mister-beyker`, `character/deyv` |
| Обращение за медицинской помощью; воспоминание об удушье | 6–7 | `scene/meditsinskaya-pomoshch`; `location/tsentr-neotlozhnoy-pomoshchi`, `location/gospital-svyatoy-marii`; `character/endryu-koui` |
| Обращение в полицию | 7 | `scene/politsiya`; `organization/politsiya-klayo`; `location/politsiya-klayo` |
| В мотеле (воспоминание, сведения Сойеров) | 7–8 | `scene/v-motele`; `location/motel-kouch-i-lantern`; `character/bob-soyer`, `enn-soyer`, `tomas-soyer`, `liza-soyer` |
| Номера сыщиков (футболка, папка, кассеты, ноутбуки; аудиальное воспоминание) | 8 | `scene/v-motele`; `item/futbolka-tsf`, `item/papka-s-vyrezkami`, `item/audiokassety`, `item/noutbuk-operatora`, `item/noutbuk-vedushchego` |
| Раздаточный материал №1 (Saginaw News, 19.06.1990) | 8 | `handout/razdatka-1-saginaw-news` |
| В комнате Лин | 9 | `scene/v-komnate-lin`; `location/komnata-lin`; `item/noutbuk-lin` |
| Врезка «История любви?» | 9 | `scene/v-komnate-lin`; таблица «Воспоминания» |
| Раздаточный материал №2 (Флинт Джорнэл, 5.11.1979) | 9 | `handout/razdatka-2-flint-journal` |
| Раздаточный материал 3 (Детройт Фри Пресс, 13.03.1965) | 9–10 | `handout/razdatka-3-detroit-free-press` |
| Сон как ключ к Безумию (сны Мифов) | 10–11 | `scene/sny`; `scenario` (таблица «Сны Мифов») |
| Раздаточный материал 4 (Вестник Клио, 20.04.2011) | 11 | `handout/razdatka-4-clio-messenger`; `organization/7-gate-films` |
| Человеческие кошмары | 11–13 | `scene/sny`; `scenario` (таблица «Человеческие кошмары») |
| Транскрипт звукового файла (раздатка #5) | 12–13 | `handout/razdatka-5-transkript`; `character/dzheyms-byork`, `character/aleksis-romanov` |
| Список опрошенных (раздатка #6, записка в комнате Лин) | 13 | `handout/razdatka-6-spisok-intervyu` |
| Я чувствую себя ужасно… | 13–14 | `scene/ya-chuvstvuyu-sebya-uzhasno`; `scenario` (таблица «Мерзкие события») |
| Врезка «Эксперименты с отпрысками» | 14 | `scene/ya-chuvstvuyu-sebya-uzhasno`; `creature/potomstvo-eykhorta` (description) |
| Исследования (Miller/Frost, 7 Gate Films, полиция Ванкувера) | 14 | `scene/issledovaniya`; `organization/miller-frost-studios`, `organization/7-gate-films` |
| Библиотека и интернет-розыск (Тиффани, тело 1979, дело Куперов 1965) | 14–15 | `scene/biblioteka-i-internet`; `character/tiffani-yensen`, `character/dzhon-kuper` |
| Дом Куперов (архивы, библиотека и интернет) | 15–16 | `location/dom-kuperov` (history); `scene/biblioteka-i-internet`; `character/edmund-makkamsi`, `debora-makkamsi`, `dzheykob-makkamsi`, `rebekka-makkamsi` |
| Врезка «До Дедала: Лабиринты в истории и легенде» | 15 | `tome/do-dedala`; `scene/biblioteka-i-internet` |
| Связь МакКамси | 16 | `scenario` (keeper_info); `character/edmund-makkamsi` |
| Раздаточный материал сыщика №7 «История Джозефа Кеннеди» | 16 | `handout/razdatka-7-istoriya-kennedi`; `character/dzhozef-kennedi` |
| Повторные интервью | 16 | `scene/povtornye-intervyu` |
| Интервьюируемые (мэр, шеф, Бейкеры, Гроверы, подростки, Кеннеди, Остин, Фолкер) | 16–17 | `scene/povtornye-intervyu`; `character/sharlotta-koulman`, `donald-metyuz`, `mister-beyker`, `mark-grover`, `penelopa-grover`, `itan-grover`, `greys-grover`, `dzheyms-byork`, `aleksis-romanov`, `dzhozef-kennedi`, `lilli-ostin`, `vanessa-folker`; `location/muzey-istoricheskogo-obshchestva`, `location/ferma-groverov` |
| А вот кто враг | 17–20 | `character/vanessa-folker` (legend, background.secret); `scenario` (keeper_info) |
| Карта «Vanessa Volker's Properties» | 19 | `map/vladeniya-folker` (`app/maps/forgetmenot-vladeniya-folker.jpg`, 25 меток); `location/ofis-folker`, `location/dom-folker`, `location/politsiya-klayo` |
| Врезка «Примечание для Хранителя: Сколько времени осталось сыщикам?» | 20 | `scenario` (advice); `creature/potomstvo-eykhorta` |
| Возвращение последнего воспоминания | 20–21 | `scene/poslednee-vospominanie` |
| Возвращение в дом Куперов | 21–26 | `scene/vozvrashchenie-v-dom-kuperov`; `location/dom-kuperov`, `dom-kuperov-gostinaya`, `dom-kuperov-kukhnya`, `dom-kuperov-kabinet`, `dom-kuperov-vtoroy-etazh`, `dom-kuperov-podval`, `taynaya-komnata`, `razrushennyy-saray`; `item/broshennoe-oborudovanie`, `item/rabochaya-kamera` |
| Карта «The Cooper House» | 22 | `map/dom-kuperov` (`app/maps/forgetmenot-dom-kuperov.jpg`, 30 меток) |
| Врезка «Примечание для Хранителя: Кровавое предвестие» | 24 | `scene/krovavoe-predvestie`; `character/brodyaga` |
| Врезка «Откровения Глааки, том IV» | 25 | `tome/otkroveniya-glaaki-tom-4` |
| Врезка «Отгоняющий Потомство» | 25 | `coc:spell:balk-brood` (новое общее заклинание, `kb/spells/balk-brood.json`); `scene/final` (mechanics) |
| Как выжить исследователям? | 26 | `scene/kak-vyzhit`; `tome/otkroveniya-glaaki-tom-4` (copies) |
| Финал: Основные цели исследователей | 26 | `scene/final`; `scenario` (conclusion) |
| Эйхот и дальнейшие события | 26–27 | `scene/final` |
| Книга «Откровения Глааки, том IV» и «Заклинание Отгоняющий Потомство» (повтор) | 27 | `tome/otkroveniya-glaaki-tom-4`; `coc:spell:balk-brood`; `scene/final` |
| Возможные концовки | 27 | `scene/final`; `scenario` (conclusion); `location/labirint-eykhorta` |
| Награды | 27 | `scenario` (conclusion) |
| Ванесса Фолькер, Избранная Эйхорта (статблок, особые способности, потеря рассудка) | 27–28 | `character/vanessa-folker` (statblock, abilities); `creature/potomstvo-eykhorta` (рой) |

Записи (91): сценарий 1; сцены 16; места 21 в книге + 1 общий город (`kb/locations/clio.json`); карты 2; персонажи 26;
существо 1; организации 4; предметы 10; раздатки 7; книги 2; плюс общее заклинание `coc:spell:balk-brood`
(`kb/spells/balk-brood.json`, заведено по поручению ведущего). Картинки карт: `app/maps/forgetmenot-dom-kuperov.jpg`,
`app/maps/forgetmenot-vladeniya-folker.jpg`. Предложения правок общих записей — `proposals-forgetmenot.json`
(10 правок в 7 записях: псевдонимы Эйхорта и пяти заклинаний в переводе книги, ссылка с общей записи «Откровений
Гла’аки» на том IV); пробный прогон `apply.py --dry-run` проходит.

## Опечатки и сомнения (в `errata` записей)

- `handout/razdatka-1-saginaw-news`: «где в 1976 году убили жену и ребёнка Энди Купера» — по раздатке №3 и тексту убийство
  12 марта 1965 года, убийца Джон Купер. Как напечатано.
- `character/vanessa-folker`: «Постройка: 0» — при СИЛ 100 и ТЕЛ 45 Комплекция 1 (БкУ +1d4 напечатан верно); «Воля: 21» —
  МОЩ не кратна 5 и не вяжется со «сверхъестественной духовной мощью» (возможно, 210), ПМ не напечатаны. Как напечатано.
  Названия характеристик в статблоке словами: «Телосложение 110» разобрано как ВЫН (ТЕЛ — «Размер 45»).
- `character/mister-beyker`: «(подробнее на стр. 36)» — ссылка из другого издания; причина — на с. 5–6.
- `tome/otkroveniya-glaaki-tom-4`: потеря Рассудка напечатана одним числом «1D6» (без потери за успех).
- Без `errata` (пометки в `quality.notes`): «ТЕЛ (Телосложение)» в тайных бросках (с. 1) — по смыслу, возможно, ВЫН;
  механика прежних редакций (Идея, «ЛОВ×3», «INT×2/×3», «Телосложения ×3»); три написания фамилии Ванессы (Фолкер,
  Волкер, Фолькер; на карте — Volker); «Тиффани Дженсен» в раздатке №1 и «Йенсен» в тексте; «Мэтиус»/«Мэтьюз»;
  «Клайо»/«Клио»; «Клайда» в раздатке №3; мэр «сорока с небольшим» «ребёнком была свидетелем» убийства 1965 года — при
  действии в 2010-х это невозможно буквально (оставлено как есть, не механика).

## Новое заклинание

`coc:spell:balk-brood` — «Отгоняющий Потомство» (name.en «Balk Brood»; псевдоним «Остановить Бруда», с. 18), заведено в
`kb/spells/balk-brood.json`: категория «Исцеление», механика «мгновенное» (обе — вывод из текста, Р-41, Р-69), 3 раунда,
1d3 Рассудка с участника и ПМ участников против дней заражения; исход — 1d3 Рассудка и 1 ПЗ за день заражения; 10%
накопительно — явление Эйхорта (с. 25, 27). Ссылка `spell` проставлена в `tome/otkroveniya-glaaki-tom-4` (spells,
copies[0].spells) и `character/vanessa-folker` (statblock.spells «Balk Brood»); заклинание — в refs сцен `final`,
`kak-vyzhit`, `ya-chuvstvuyu-sebya-uzhasno`, сценария и способности «Заражение» у Потомства. Книга ссылается на него как
на заклинание «из правил» (с. 13), но в «Книге хранителя» его нет.

## Не взято

- Картинки: обложка (фургон в кукурузе), портрет Ванессы (с. 17), иллюстрация дома (с. 21) — оформление; `app/art/` не
  входит в эту часть. При желании портрет — в `images` записи `character/vanessa-folker`.
- Отдельные записи для упомянутых мимоходом: Скотти (друг подростков), Дейл Лалёр (приятель Кеннеди), Дэвид Ким и
  Энджи Уокер (7 Gate Films), Тревор Каннингем (продюсер), Сьюзан Марш и Марк Нейманн (журналисты), шериф Снайдер и шеф
  Уоллман, миссис Купер и её сын, Джеймс Стили, Томас и Джон Дрейк, миссис Бейкер, прежний риелтор, «Mr. Blackk», автовор
  из Флинта — без сведений сверх одной фразы; остаются текстом в записях (дом Куперов, Кеннеди, 7 Gate Films, раздатки,
  Ванесса, ноутбук Лин).
- Места без своих записей: мастерская Дэйва, местные бары, цветочный магазин Blooms & Things, парковка Advantage Auto
  Parts, улицы W. Vienna Street и Sunset Drive (метки карты ведут на город), библиотеки Сагино и Флинта, библиотека
  Мичиганского университета в Энн-Арборе (в `copies` тома), полиция Ванкувера — одна фраза.
- Метки карт не поставлены на заголовки, розу ветров, масштаб, стрелки лестниц и тексты легенд (это не подписи мест).
- Готовых сыщиков книга не даёт — только роли в шоу с навыками (таблица сценария).

## Кандидаты и вопросы

- Сагино, Флинт, Детройт, Энн-Арбор — отдельных городов в базе нет; госпиталь Святой Марии (Сагино) отнесён к
  «Окрестностям Клайо» с пометкой.
- Эйхорт в базе — «Айхорт»; в этой книге — «Эйхорт» (предложен псевдоним). Общая запись «Откровений Гла’аки» не имеет
  поля `aliases` — вариант «Откровения Глааки» стоит в псевдонимах тома IV.
- Карточка владельца (`3_КБ\Ваншоты\2020 Не забывай меня\_паспорт.md`) — год 2020; книга года не называет.
