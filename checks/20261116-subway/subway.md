# «Shadows of the Old Subway» (J.C. Connors, соло) — перенос в базу

Книга `shadows-old-subway-en` (v1.1, 31 с.; 1shotadventures.com, фанатский материал по Fan Material Policy Chaosium; год на
страницах не напечатан, в метаданных PDF — январь 2024). Печатная страница = физической (смещение 0) на с. 1–27; листы
готовых сыщиков (физ. 28–31) без номера. Русской версии в базе нет (проверено по именам Gittings, Donmai, Algernon, Clark Street).
Эпоха — `other` (1918 год). Всё в `kb/books/shadows-old-subway-en/`: 1 сценарий (соло, Р-230), 16 персонажей, 2 существа,
13 предметов, 1 книга Мифов, 2 раздатки, 2 организации, 15 мест, 3 карты (картинки `app/maps/subway-*.jpg`), раздатка —
`app/art/handouts/subway-*.webp`.

## Заголовок книги | Страница | Где в базе

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Shadows of the Old Subway (обложка, by J.C. Connors) | 1 | сценарий `scenario/shadows-of-the-old-subway`: `summary`, `sources` |
| вступление «In 1918, the expansion…» | 1 | сценарий: таблица «Абзацы», строка «Введение» |
| About the Adventure | 1 | сценарий: `advice`; «Абзацы» — «Введение» |
| Special Rules (жирные вещи и имена, фонарик 95%, Удача 2d6×5+10) | 1 | сценарий: `advice`; «Абзацы» — «Введение»; предмет `item/winchester-flashlight` |
| Undearneath the City | 2 | сценарий: `hook`; «Абзацы» — «Введение»; места `location/clark-street-tunnel`; `organization/irt`; `character/commissioner-whitney`, `character/frank-mercer` |
| #1–#73 | 2–23 | сценарий: таблицы «Абзацы» (перевод) и «Абзацы (оригинал)» — все 73 абзаца; `steps` — 12 веток и финалы |
| Cultist of the Foul Union (статблок) | 3 | `character/cultists-of-azathoth` (вариант «с. 3») |
| The Considerable Rat-Thing (статблок) | 10 | `creature/considerable-rat-thing` (instance_of `coc:creature:rat-thing`) |
| записка «Dear Algernon…» (картинка в абз. 32) | 11 | `handout/gladys-note` (текст + картинка); абз. 32 |
| The Deranged Sculptor (статблок) | 14 | `character/algernon-carson` |
| The Harbinger of Azathoth (статблок) | 17 | `creature/harbinger-of-azathoth` |
| Rewards | 23 | сценарий: `conclusion`; «Абзацы» — строка «Награды» |
| Special Thanks | 23 | сценарий: `sources`, `quality.notes` (Dungeondraft, нейросети — Р-240) |
| Disclaimer | 23 | сценарий: `sources` (Fan Material Policy) |
| Version History | 23 | сценарий: `quality.notes`; `character/algernon-carson` (источник: v1.1 исправила статблок) |
| Mr. Gittings (статблок) | 24 | `character/edward-gittings` |
| Cultist of Azathoth (статблок) | 24 | `character/cultists-of-azathoth` (вариант «с. 24») |
| Giuseppe (статблок) | 24 | `character/giuseppe-affini` |
| On the Sending Out of the Soul / Handout A | 24 | `handout/handout-a-sending-out-of-the-soul` (текст + картинка), `tome/on-the-sending-out-of-the-soul` |
| Tunnel Map | 25 | `map/tunnel-map` (2 метки X) |
| Harbinger Map | 26 | `map/harbinger-map` (PC, X) |
| Terminus Map | 27 | `map/terminus-map` (3 × X, PC; печать — вычисленная метка) |
| лист «1920s Era Investigator»: Eng Fao | физ. 28–29 | `character/eng-fao` (преген) |
| лист «1920s Era Investigator»: Josephine Wilson | физ. 30–31 | `character/josephine-wilson` (преген) |
| KEY WORDS (circle when encountered) | физ. 29, 31 | сценарий: таблица «Ключевые слова» (14 слов: где записываются и где действуют) |

## Не взято

- Иллюстрации и портреты (обложка; картинки с. 5, 8, 10, 21, 22; портреты в статблоках с. 3, 10, 14, 17, 24; портреты прегенов
  с. 28, 30): книга сама пишет (с. 23), что «art and portraits» сделаны с элементами thispersondoesnotexist и Midjourney —
  по Р-240 не берутся; перечислены в `atmosphere.json` (ведущему — слить). Если владелец считает это случаем Р-244, портреты
  можно взять. Значки-фонарики и рамки — оформление (`atmosphere.json`).
- Безымянные эпизодические фигуры без действий, кроме одной реплики: отец Диэри (сравнение в абз. 61), сосед сыщика (абз. 56),
  усатый рабочий и второй рабочий (абз. 73), машинист метро (абз. 29), ослепший рабочий (вступление) — остаются текстом абзацев.
- Места, упомянутые мимоходом, без сцен: Таймс-сквер, станция «42-я улица», Чайнатаун (дом Донмай), ресторан «Люхов», Коламбус-серкл,
  Кони-Айленд, Бродвей, Манхэттен, Ист-Ривер, Салерно, Шэньян, Талса; Ютландское сражение, HMS «Айрон Дьюк», «Росток» — текст
  абзацев и записей.
- Мелочи без механики: карта метро на ящике (абз. 70), джазовая афиша (абз. 56), слепая крыса и рой крыс (абз. 36, 71),
  разумные водоросли (абз. 27, 62, 65; статблока нет) — в описаниях мест; амулет Уилли (абз. 2, 26, 54, 57) — в записи Уилли;
  Серая слизь — в `keeper_info` сценария и тексте абзацев; набор электрика и рабочие ботинки — `possessions` прегенов.
- Заклинание из раздатки A (без названия, 8 ПМ, отрывает головы) — в записях книги Мифов и раздатки; общей записи `coc:spell:*`
  нет — кандидат в справочник (вопрос ведущему).

## Опечатки и сомнения (errata)

- Абз. 70 недостижим: ни один абзац не отсылает к нему (подвеска и У КОНЦА ТОННЕЛЯ иначе не встречаются) — вопрос владельцу.
- Абз. 50: «SIDE DOOR» вместо ключевого слова «SIDE ROOM» (абз. 61, листы).
- Абз. 38, 45: «Electronics Repair» — в русском тексте «Электрика» (исправлено, `corrections`).
- Следы версии GURPS: «Terror» (абз. 28, 50, 55, 70; не объяснён), «1D6 cr damage» (абз. 43), «All-Out Attack» (абз. 50),
  «+2 to hit» (тактика культиста, с. 3), «Easy Climb roll» (абз. 53).
- Имена: «Mr. Giddings» (абз. 5), «Donai» (абз. 4).
- Записка Глэдис: «visiting from and you mother» — пропущено слово.
- Статблоки: крысиная тварь — Уклонение 45% (15/6) → доли исправлены (Р-35, доли подходят к 30% — Р-77), Комплекция 0 при
  СИЛ+ТЕЛ 70; Вестник — ПЗ 19 (по формуле 20), БкУ +1d6 и Комплекция 2 при СИЛ+ТЕЛ 240 (без большинства — как напечатано,
  вопрос владельцу), Уклонение 20% (20/5) → 10/4; Гиттингс — Скорость 7 (по правилам 8); Джузеппе — драка 40% (28/8) → 20/8,
  Скорость 8 (по правилам 9), Уклонение 30% (половина ЛВК 32).
- Прегены: ЛВК 50 с пятой частью 12 (оба листа); Энг Фао — Стрельба (пистолет) 45% (20/8) → 22/9, драка в блоке «Combat»
  25% при навыке 55%, родной язык 30% при ОБР 60; Джозефина — Работа в библиотеке 40% (25/10) → 20/8 (доли подходят к 50%, Р-77),
  Слух 50% (25/12) → 25/10.

## Термины книги (English → русский)

| English | Русский |
|---|---|
| Shadows of the Old Subway | «Тени старой подземки» |
| subway | метро, подземка |
| Interborough Rapid Transit Company (IRT) | компания «Интерборо Рапид Транзит» (IRT) |
| Clark Street Tunnel | тоннель Кларк-стрит |
| Brooklyn Heights station | станция «Бруклин-Хайтс» |
| 42nd Street Station | станция «42-я улица» |
| terminus (of the tunnel) | конец тоннеля |
| Undearneath the City | «Под городом» |
| Harbinger (of Azathoth), harbingers | Вестник (Азатота), вестники |
| Cultist of the Foul Union / of the Union / of Azathoth | культист Мерзкого союза / Союза / Азатота |
| minions of Azathoth | приспешники Азатота |
| The Considerable Rat-Thing | крупная крысиная тварь |
| The Deranged Sculptor | безумный скульптор |
| the mother (the carved face) | мать |
| Gray Ooze, the ooze | Серая слизь, слизь |
| the great seal | великая печать |
| the mark (on the wall) | знак |
| Hydra / Mother Hydra | Гидра / Мать Гидра |
| Cyclopean Hammer | Циклопический молот |
| On the Sending Out of the Soul | «Об отсылании души» |
| strange starred pendant / strange bronze pendant | странная звёздчатая подвеска / странная бронзовая подвеска |
| primitive elder sign | первобытный Знак Старших богов |
| Reliability (of the flashlight) | надёжность |
| check the reliability of your flashlight | проверьте надёжность фонарика |
| Winchester electric flashlight | электрический фонарик «Винчестер» |
| Terror | Ужас |
| penalty die | штрафная кость |
| Sanity Roll | проверка Рассудка |
| Hard Dex roll / Hard Spot Hidden roll | трудная проверка ЛВК / трудная проверка Внимания |
| Easy Climb roll | лёгкая проверка Лазания |
| Con / Str / Pow / Int / Dex roll | проверка ВЫН / СИЛ / МОЩ / ИНТ / ЛВК |
| Luck roll | проверка Удачи |
| Electronics Repair (Elec. Repair) | Электрика |
| All-Out Attack | тотальная атака |
| Tunnel Map / Harbinger Map / Terminus Map | карта тоннеля / карта Вестника / карта конца тоннеля |
| PC (map marker) | PC |
| Handout A | раздатка A |
| Rewards | Награды |
| CHARGE ATTACK | АТАКА С РАЗБЕГА |
| DONMAI IS HERE | ДОНМАЙ ЗДЕСЬ |
| FUMBLING | ВОЗИТСЯ |
| GIUSEPPE IS AN ALLY | ДЖУЗЕППЕ — СОЮЗНИК |
| THE HAMMER IS BLESSED | МОЛОТ БЛАГОСЛОВЛЁН |
| INTIMIDATED | ЗАПУГАН |
| MOSTLY SNEAKY | ПОЧТИ НЕЗАМЕТНО |
| MYTHOS LORE | ЗНАНИЕ МИФОВ |
| NEAR THE TERMINUS | У КОНЦА ТОННЕЛЯ |
| ON THE DEFENSE | В ОБОРОНЕ |
| RATS! | КРЫСЫ! |
| SEEN THE MARK | ВИДЕЛ ЗНАК |
| SIDE ROOM / SIDE DOOR | БОКОВАЯ КОМНАТА / БОКОВАЯ ДВЕРЬ |
| STUNNED | ОШЕЛОМЛЁН |
| Mr. (Edward) Gittings | мистер (Эдвард) Гиттингс |
| Donmai | Донмай |
| Algernon Carson | Элджернон Карсон |
| Giuseppe Affini | Джузеппе Аффини |
| Charlie / Edna / Gladys / Willie | Чарли / Эдна / Глэдис / Уилли |
| Mike Hollinger | Майк Холлингер |
| Acting Commissioner Whitney | исполняющий обязанности комиссара Уитни |
| Eng Fao / Josephine Wilson | Энг Фао / Джозефина Уилсон |
| IRT Engineer | инженер IRT |
| Lüchow’s | «Люхов» |
| Original Dixieland Jazz Band | «Original Dixieland Jazz Band» |
| Columbus Circle / Times Square / Chinatown / Coney Island | Коламбус-серкл / Таймс-сквер / Чайнатаун / Кони-Айленд |
| East River | Ист-Ривер |
| Jutland / Rostock / HMS Iron Duke | Ютланд / «Росток» / «Айрон Дьюк» |
| Father Deary | отец Диэри |

Придуманные имена (Р-150, Р-151): начальник сыщика — Фрэнк Мерсер; бородач у решётки — Хайрам Боулз; ирландский
полицейский — Деннис О’Мэлли; культисты (группа) — Гарет Морган, Томас Ллуэллин, Патрик Доэрти, Сэмюэл Пратт, Луиджи Капелло.

## Файлы проверки

- `art.json`, `art-proposals.json` (применены), `art-boxes.json` (рамки вырезки раздатки и карт), `atmosphere.json` (ведущему —
  `pipeline/art/merge_atmosphere.py`), `proposals-subway.json` (2 предложения: source_variants у `coc:weapon:38-revolver` и
  `coc:weapon:dagger`, не применены), `completeness/`, `scenario/`.
- Полнота: 14 находок `art.record_without` — все про картинки, не взятые по Р-240 (уйдут после слияния `atmosphere.json`).
