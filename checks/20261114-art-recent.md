# Картинки последних книг (2026-11-14, Р-165)

Портреты персонажей и иллюстрации, которые части переноса последних книг не взяли (разделы «Не взято» отчётов
`checks/20261113-fungi`, `-tatters`, `-reign`, `-ru-rest`, `checks/20261114-ru-more`). Вырезка — из рендера страницы
(300 dpi; «Грибы с Юггота» — 200 dpi, скан «Наедине с тьмой» — 72 dpi), рамки — `20261114-art-recent/<имя>-boxes.json`
(доли страницы, физические страницы); области картинок найдены по `pdftohtml -xml`, каждая проверена глазами на сводном
листе. Копии — `pipeline/art/add_images.py` с новым необязательным полем `name` (имя файла с префиксом книги или части;
существующий файл с таким именем не перезаписывается), предложения применены `pipeline/integrate/apply.py`;
`python -B tools/check.py --changed` — ошибок 0.

## Итог: 139 картинок

| Книга | Картинок |
|---|---|
| `griby-s-yuggota-ru` | 7 |
| `lokhmotya-korolya-ru` | 48 |
| `tsarstvo-terrora-ru` | 39 (в т. ч. 7 раздаток, у которых картинок не было) |
| `reign-of-terror-women-en` | 0 |
| `sny-o-yaponii-ru` | 3 |
| `tri-koshmarnykh-vechera-ru` | 6 |
| `mify-hastura-ru` | 0 (иллюстрации сгенерированы ИИ — не брать) |
| `naedine-s-hellouinom-ru` | 0 (см. ниже) |
| `naedine-s-pomekhami-ru` | 7 |
| `temnye-veka-tri-stsenariya-ru` | 20 (15 — к общим записям `coc:creature:*` бестиария) |
| `naedine-s-prilivom-ru` | 6 |
| `naedine-s-plamenem-ru` | 0 (в простой версии иллюстраций нет, только карта) |
| `naedine-s-tmoy-ru` | 3 |

## Не взято и почему

- `naedine-s-hellouinom-ru`: по предисловию переводчика (с. 5) все иллюстрации книги «преображены с помощью нейросетей» —
  как и у «Мифов Хастура», не брались. Портреты Кори Адамс и Криса Гранта на листах персонажей
  (`naedine-s-hellouinom-pregens-ru`, `-pregens-2-ru`) не достать: это формы XFA, Poppler показывает только заглушку
  «Please wait…».
- `naedine-s-pomekhami-ru`: взяты иллюстрации мест и предметов, у которых есть записи. Иллюстрации книги по виду похожи на
  сгенерированные ИИ (в книге об этом не сказано; портреты Алекса и Чарли часть уже брала) — вопрос владельцу: оставить
  или убрать. Без записи-адресата: «Вещи», «Раненый олень», «Душ», «Помехи внутри», «Лес под луной», «Погоня»,
  «Видеозапись», «Итог», «Идеальная пара», «Беспорядок в хижине», «Сумка», «Жест приглашения», «Кольца».
- `reign-of-terror-women-en`: портрет дамы (с. 11) — тот же арт, что Селин Бессет в «Царстве Террора», к записи
  Шарлотты Корде не привязан (угадывать не стал); шествие женщин (с. 8), пентаграмма (с. 9) — записей нет.
- `tsarstvo-terrora-ru`: портреты шести сыщиков на с. 11 и повторы портретов на с. 91–92, 96 — взяты портреты с их листов
  (с. 120–125) и из «Действующих лиц» (с. 13–15); исторические картины без записи (с. 9, 25, 39, 52, 55, 56, 59, 63, 71,
  79, 85, 94, 98, 99, 106); тумбриль на с. 16 (полностраничный арт, сцены у него нет).
- `lokhmotya-korolya-ru`: обложка, фронтиспис, титулы книг I–III, силуэт города (с. 35), созвездие Тельца (с. 8),
  повторы раздаток и фото Анзалоне/Скиппоне в тексте (с. 211; в раздатке № 26 уже есть), вторая картинка шантака (с. 291,
  почти повтор с. 290), карты.
- `griby-s-yuggota-ru`: украшения английского скана (физ. 2–5, 77), повторы эмблемы NWI (взята одна — к
  `organization/new-world-incorporated`).
- `sny-o-yaponii-ru`: иллюстрации предисловия и введения (физ. 3, 4), гравюра Хиросигэ (физ. 22), пистолет Намбу
  (физ. 25; оружие — общая запись), сцена с призраками (физ. 27 — неясно, к какой сцене).
- `tri-koshmarnykh-vechera-ru`: иллюстрации введения, повтор портрета Джейкоба (с. 86), рисунок револьвера (с. 87),
  отдельные рисунки Мисси (в раздатке «Рисунки Мисси» уже есть).
- `naedine-s-prilivom-ru`: «Показ антиквариата», «Стрельба в существо Иба», «Высвобождение», «Тварь за окном»,
  «Затопленный город», «Пробираясь через болото», «Путь к спасению?», «Затопленные руины Сарната» — записи-адресата нет
  (сцен в книге-игре нет, Сарната в базе нет); портреты Элеоноры и Эллери Вудс — у записей уже есть.
- `naedine-s-tmoy-ru`: люди на палубе (абз. 69), караван (абз. 242), мумия (с. 66), лодка (абз. 456), бросок динамита,
  полностраничная картина (с. 87) — адресат неясен; портреты сыщиков в тексте — у прегенов уже есть.
- `temnye-veka-tri-stsenariya-ru`: иллюстрации глав сеттинга и системы (миниатюры, гобелен, сцены) — без записей.

## Список

### `griby-s-yuggota-ru` — 7

Сопоставление `fungi.json`, рамки `fungi-boxes.json`, предложения `fungi-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `griby-s-yuggota-ru/organization/new-world-incorporated` | `app/art/organizations/fungi-new-world-incorporated.webp` | art | Эмблема корпорации «Новый Мир» (NWI) | «Грибы с Юггота», с. 7 (физ. 8) |
| `griby-s-yuggota-ru/character/abd-katif` | `app/art/characters/fungi-abd-katif.webp` | illustration | Абд Катиф и его приспешники на верблюдах | «Грибы с Юггота», с. 38 (физ. 39) |
| `griby-s-yuggota-ru/character/chan-kvok` | `app/art/characters/fungi-chan-kvok.webp` | portrait | Жрец храма с жабьим лицом | «Грибы с Юггота», с. 55 (физ. 56) |
| `griby-s-yuggota-ru/scene/bay-pearl-beach-ritual` | `app/art/scenes/fungi-bay-pearl-beach-ritual.webp` | illustration | Гидра и Лэнг-Фу на Жемчужном пляже | «Грибы с Юггота», с. 58 (физ. 59) |
| `griby-s-yuggota-ru/creature/bay-thing-from-between-planes` | `app/art/creatures/fungi-bay-thing-from-between-planes.webp` | art | Нечто из межмирья в номере отеля | «Грибы с Юггота», с. 64 (физ. 65) |
| `griby-s-yuggota-ru/creature/beast-the-beast` | `app/art/creatures/fungi-beast-the-beast.webp` | art | Сфинкс с пустотой вместо лица | «Грибы с Юггота», с. 69 (физ. 70) |
| `griby-s-yuggota-ru/location/celaeno-great-library` | `app/art/locations/fungi-celaeno-great-library.webp` | illustration | Великая библиотека Целаено | «Грибы с Юггота», с. 73 (физ. 74) |

### `lokhmotya-korolya-ru` — 48

Сопоставление `tatters.json`, рамки `tatters-boxes.json`, предложения `tatters-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `lokhmotya-korolya-ru/scene/prologue-presenting-the-play` | `app/art/scenes/prologue-presenting-the-play.webp` | illustration | Кассильда и Незнакомец | «Лохмотья Короля», с. 23 |
| `lokhmotya-korolya-ru/character/talbot-estus` | `app/art/characters/tatters-talbot-estus.webp` | portrait | Талбот Эстус | «Лохмотья Короля», с. 29 |
| `lokhmotya-korolya-ru/character/charles-highsmith` | `app/art/characters/tatters-charles-highsmith.webp` | portrait | Доктор Хайсмит | «Лохмотья Короля», с. 39 |
| `lokhmotya-korolya-ru/character/montague-edwards` | `app/art/characters/tatters-montague-edwards.webp` | portrait | Мистер Эдвардс | «Лохмотья Короля», с. 46 |
| `lokhmotya-korolya-ru/character/alexander-roby` | `app/art/characters/tatters-alexander-roby.webp` | portrait | Александр Роби | «Лохмотья Короля», с. 48 |
| `lokhmotya-korolya-ru/character/lucius-harriwell` | `app/art/characters/tatters-lucius-harriwell.webp` | portrait | Луциус Харривелл | «Лохмотья Короля», с. 56 |
| `lokhmotya-korolya-ru/character/dick-blair` | `app/art/characters/tatters-dick-blair.webp` | portrait | Дик Блэр | «Лохмотья Короля», с. 86 |
| `lokhmotya-korolya-ru/scene/springer-the-killing` | `app/art/scenes/springer-the-killing.webp` | illustration | Бьякхи над Дженнингсом | «Лохмотья Короля», с. 91 |
| `lokhmotya-korolya-ru/character/harold-jennings` | `app/art/characters/tatters-harold-jennings.webp` | portrait | Гарольд Дженнингс | «Лохмотья Короля», с. 93 |
| `lokhmotya-korolya-ru/scene/springer-regents-canal` | `app/art/scenes/springer-regents-canal.webp` | illustration | Бэкон находит жертву | «Лохмотья Короля», с. 99 |
| `lokhmotya-korolya-ru/creature/springer-unspeakable-possessor-bacon` | `app/art/creatures/springer-unspeakable-possessor-bacon.webp` | art | Невыразимый Одержимый («Mr. Bacon?») | «Лохмотья Короля», с. 100 |
| `lokhmotya-korolya-ru/character/lawrence-bacon` | `app/art/characters/tatters-lawrence-bacon.webp` | portrait | Лоуренс Бэкон | «Лохмотья Короля», с. 101 |
| `lokhmotya-korolya-ru/creature/springer-five-urban-ghouls` | `app/art/creatures/springer-five-urban-ghouls.webp` | art | Упырь | «Лохмотья Короля», с. 104 |
| `lokhmotya-korolya-ru/character/aleister-crowley` | `app/art/characters/tatters-aleister-crowley.webp` | portrait | Алистер Кроули | «Лохмотья Короля», с. 114 |
| `lokhmotya-korolya-ru/character/henry-lister` | `app/art/characters/tatters-henry-lister.webp` | portrait | Генри Листер | «Лохмотья Короля», с. 120 |
| `lokhmotya-korolya-ru/scene/talk-gresty-arrest` | `app/art/scenes/talk-gresty-arrest.webp` | illustration | Грести перед церковью Христа | «Лохмотья Короля», с. 162 |
| `lokhmotya-korolya-ru/character/wilfred-gresty` | `app/art/characters/tatters-wilfred-gresty.webp` | portrait | Уилфред Грести | «Лохмотья Короля», с. 163 |
| `lokhmotya-korolya-ru/creature/nug-blessed-of-shub-niggurath` | `app/art/creatures/nug-blessed-of-shub-niggurath.webp` | art | Благословенный Шуб-Ниггурат | «Лохмотья Короля», с. 191 |
| `lokhmotya-korolya-ru/creature/nug-blessed-of-shub-niggurath` | `app/art/creatures/nug-blessed-of-shub-niggurath-2.webp` | illustration | Благословенный в лесу Гоатсвуда | «Лохмотья Короля», с. 175 |
| `lokhmotya-korolya-ru/character/hillary-quarrie` | `app/art/characters/tatters-hillary-quarrie.webp` | portrait | Хилари Кверри | «Лохмотья Короля», с. 176 |
| `lokhmotya-korolya-ru/creature/nug-hillary-mastiffs` | `app/art/creatures/nug-hillary-mastiffs.webp` | art | Пиг и Уолтер, мастифы Хилари | «Лохмотья Короля», с. 176 |
| `lokhmotya-korolya-ru/scene/nug-meeting-hillary` | `app/art/scenes/nug-meeting-hillary.webp` | illustration | Хилари и собаки | «Лохмотья Короля», с. 178 |
| `lokhmotya-korolya-ru/character/will` | `app/art/characters/tatters-will.webp` | portrait | Уилл | «Лохмотья Короля», с. 178 |
| `lokhmotya-korolya-ru/creature/nug-dark-young-summoned-by-atkinson` | `app/art/creatures/nug-dark-young-summoned-by-atkinson.webp` | illustration | Тёмный молодняк, вызванный Аткинсоном | «Лохмотья Короля», с. 187 |
| `lokhmotya-korolya-ru/character/atkinson` | `app/art/characters/tatters-atkinson.webp` | portrait | Аткинсон | «Лохмотья Короля», с. 190 |
| `lokhmotya-korolya-ru/character/paulo-tuminardo` | `app/art/characters/tatters-paulo-tuminardo.webp` | portrait | Пауло Туминардо | «Лохмотья Короля», с. 201 |
| `lokhmotya-korolya-ru/character/thomas-villiers` | `app/art/characters/tatters-thomas-villiers.webp` | portrait | Томас Вильерс | «Лохмотья Короля», с. 202 |
| `lokhmotya-korolya-ru/character/giuseppe-colombo` | `app/art/characters/tatters-giuseppe-colombo.webp` | portrait | Джузеппе Коломбо | «Лохмотья Короля», с. 203 |
| `lokhmotya-korolya-ru/scene/milan-the-angel-attacks` | `app/art/scenes/milan-the-angel-attacks.webp` | illustration | Вильерс выпускает Ангела | «Лохмотья Короля», с. 207 |
| `lokhmotya-korolya-ru/character/ian-gore` | `app/art/characters/tatters-ian-gore.webp` | portrait | Преподобный Ян Гор | «Лохмотья Короля», с. 214 |
| `lokhmotya-korolya-ru/character/stephen-thomas` | `app/art/characters/tatters-stephen-thomas.webp` | portrait | Стивен Томас | «Лохмотья Короля», с. 215 |
| `lokhmotya-korolya-ru/character/julian-knight` | `app/art/characters/tatters-julian-knight.webp` | portrait | Джулиан Найт | «Лохмотья Короля», с. 216 |
| `lokhmotya-korolya-ru/character/henrietta-tullis` | `app/art/characters/tatters-henrietta-tullis.webp` | portrait | Генриетта Туллис | «Лохмотья Короля», с. 217 |
| `lokhmotya-korolya-ru/character/francesca-nicholson` | `app/art/characters/tatters-francesca-nicholson.webp` | portrait | Франческа Николсон | «Лохмотья Короля», с. 220 |
| `lokhmotya-korolya-ru/character/patricia-berry` | `app/art/characters/tatters-patricia-berry.webp` | portrait | Патриция Берри | «Лохмотья Короля», с. 221 |
| `lokhmotya-korolya-ru/scene/ship-drama-on-the-bombay-dock` | `app/art/scenes/ship-drama-on-the-bombay-dock.webp` | illustration | Патрицию вытаскивают из гавани | «Лохмотья Короля», с. 224 |
| `lokhmotya-korolya-ru/character/sivakumar-patel` | `app/art/characters/tatters-sivakumar-patel.webp` | portrait | Сивакумар Патель | «Лохмотья Короля», с. 228 |
| `lokhmotya-korolya-ru/scene/india-entering-nepal` | `app/art/scenes/india-entering-nepal.webp` | illustration | Переход границы Непала | «Лохмотья Короля», с. 239 |
| `lokhmotya-korolya-ru/character/jigme-rinzing` | `app/art/characters/tatters-jigme-rinzing.webp` | portrait | Джигме Ринзинг | «Лохмотья Короля», с. 243 |
| `lokhmotya-korolya-ru/character/tsewan-pemba` | `app/art/characters/tatters-tsewan-pemba.webp` | portrait | Тсеван Пемба | «Лохмотья Короля», с. 257 |
| `lokhmotya-korolya-ru/character/carlo-schippone` | `app/art/characters/tatters-carlo-schippone.webp` | portrait | Карло Скиппоне | «Лохмотья Короля», с. 266 |
| `lokhmotya-korolya-ru/scene/drakmar-firefight` | `app/art/scenes/drakmar-firefight.webp` | illustration | Скиппоне тщательно целится | «Лохмотья Короля», с. 268 |
| `lokhmotya-korolya-ru/character/house-tcho-tcho` | `app/art/characters/house-tcho-tcho.webp` | portrait | Чо-чо | «Лохмотья Короля», с. 280 |
| `lokhmotya-korolya-ru/character/roberto-anzalone` | `app/art/characters/tatters-roberto-anzalone.webp` | portrait | Профессор Анзалоне | «Лохмотья Короля», с. 283 |
| `lokhmotya-korolya-ru/scene/house-the-gate` | `app/art/scenes/house-the-gate.webp` | illustration | В пещере Чагнара Фаугна | «Лохмотья Короля», с. 285 |
| `lokhmotya-korolya-ru/character/malcolm-quarrie` | `app/art/characters/tatters-malcolm-quarrie.webp` | portrait | Малкольм Кверри | «Лохмотья Короля», с. 287 |
| `lokhmotya-korolya-ru/scene/house-shantak-encounter` | `app/art/scenes/house-shantak-encounter.webp` | illustration | Шантак над чо-чо | «Лохмотья Короля», с. 290 |
| `lokhmotya-korolya-ru/creature/house-king-in-yellow` | `app/art/creatures/house-king-in-yellow.webp` | art | Король в Жёлтом | «Лохмотья Короля», с. 299 |

### `tsarstvo-terrora-ru` — 39

Сопоставление `reign.json`, рамки `reign-boxes.json`, предложения `reign-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `tsarstvo-terrora-ru/character/louis-malon` | `app/art/characters/reign-louis-malon.webp` | portrait | Капитан Луи Малон | «Царство Террора», с. 13 |
| `tsarstvo-terrora-ru/character/lucien-rigault` | `app/art/characters/reign-lucien-rigault.webp` | portrait | Доктор Люсьен Риго | «Царство Террора», с. 13 |
| `tsarstvo-terrora-ru/character/guillaume-ghoul` | `app/art/characters/reign-guillaume-ghoul.webp` | portrait | Гуль, что был Гийомом | «Царство Террора», с. 14 |
| `tsarstvo-terrora-ru/character/fenalik` | `app/art/characters/reign-fenalik.webp` | portrait | Граф Феналик | «Царство Террора», с. 14 |
| `tsarstvo-terrora-ru/character/fenalik` | `app/art/characters/reign-fenalik-2.webp` | illustration | Граф Феналик | «Царство Террора», с. 30 |
| `tsarstvo-terrora-ru/character/comte-benoit` | `app/art/characters/reign-comte-benoit.webp` | portrait | Граф Бенуа | «Царство Террора», с. 14 |
| `tsarstvo-terrora-ru/character/1789-melodie-benoit` | `app/art/characters/1789-melodie-benoit.webp` | portrait | Мелоди Бенуа | «Царство Террора», с. 15 |
| `tsarstvo-terrora-ru/character/celine-bessette` | `app/art/characters/reign-celine-bessette.webp` | portrait | Селин Бессет | «Царство Террора», с. 15 |
| `tsarstvo-terrora-ru/character/dietrich-zann` | `app/art/characters/reign-dietrich-zann.webp` | portrait | Дитрих Цанн | «Царство Террора», с. 15 |
| `tsarstvo-terrora-ru/character/thierry-renault` | `app/art/characters/reign-thierry-renault.webp` | portrait | Сержант Тьерри Рено | «Царство Террора», с. 120 |
| `tsarstvo-terrora-ru/character/michel-beaumains` | `app/art/characters/reign-michel-beaumains.webp` | portrait | Мишель Бомэн | «Царство Террора», с. 121 |
| `tsarstvo-terrora-ru/character/jean-dupois` | `app/art/characters/reign-jean-dupois.webp` | portrait | Жан Дюпуа | «Царство Террора», с. 122 |
| `tsarstvo-terrora-ru/character/christophe-pressi` | `app/art/characters/reign-christophe-pressi.webp` | portrait | Кристоф Пресси | «Царство Террора», с. 123 |
| `tsarstvo-terrora-ru/character/etienne-babin` | `app/art/characters/reign-etienne-babin.webp` | portrait | Этьен Бабен | «Царство Террора», с. 124 |
| `tsarstvo-terrora-ru/character/joseph-hugel` | `app/art/characters/reign-joseph-hugel.webp` | portrait | Жозеф Хюгель | «Царство Террора», с. 125 |
| `tsarstvo-terrora-ru/scene/1789-into-the-catacombs` | `app/art/scenes/1789-into-the-catacombs.webp` | illustration | Рабочие в катакомбах | «Царство Террора», с. 21 |
| `tsarstvo-terrora-ru/location/1789-versailles` | `app/art/locations/1789-versailles.webp` | illustration | Вид Версаля | «Царство Террора», с. 28 |
| `tsarstvo-terrora-ru/scene/1789-aristo-gossip` | `app/art/scenes/1789-aristo-gossip.webp` | illustration | Бал аристократов | «Царство Террора», с. 29 |
| `tsarstvo-terrora-ru/item/1789-skinless-pope` | `app/art/items/1789-skinless-pope.webp` | illustration | Гость целует кольцо Безкожего Папы | «Царство Террора», с. 35 |
| `tsarstvo-terrora-ru/scene/1789-dinner-party` | `app/art/scenes/1789-dinner-party.webp` | illustration | Званый ужин у Феналика | «Царство Террора», с. 36 |
| `tsarstvo-terrora-ru/scene/1789-guests-arrive` | `app/art/scenes/1789-guests-arrive.webp` | illustration | Гости в звериных масках | «Царство Террора», с. 41 |
| `tsarstvo-terrora-ru/scene/1789-the-assault` | `app/art/scenes/1789-the-assault.webp` | illustration | Феналик атакует! | «Царство Террора», с. 44 |
| `tsarstvo-terrora-ru/scene/1789-tennis-court-oath` | `app/art/scenes/1789-tennis-court-oath.webp` | illustration | Клятва в зале для игры в мяч | «Царство Террора», с. 46 |
| `tsarstvo-terrora-ru/scene/1789-bastille` | `app/art/scenes/1789-bastille.webp` | illustration | Штурм Бастилии | «Царство Террора», с. 47 |
| `tsarstvo-terrora-ru/scene/1789-declaration` | `app/art/scenes/1789-declaration.webp` | illustration | Декларация прав человека и гражданина | «Царство Террора», с. 49 |
| `tsarstvo-terrora-ru/creature/guillotined-dead` | `app/art/creatures/reign-guillotined-dead.webp` | art | Гильотинированные мертвецы | «Царство Террора», с. 65 |
| `tsarstvo-terrora-ru/scene/1794-interview-with-the-ghoul` | `app/art/scenes/1794-interview-with-the-ghoul.webp` | illustration | Разговор с гулем | «Царство Террора», с. 67 |
| `tsarstvo-terrora-ru/scene/1794-the-black-book` | `app/art/scenes/1794-the-black-book.webp` | illustration | Чёрная книга | «Царство Террора», с. 73 |
| `tsarstvo-terrora-ru/scene/1794-music-from-beyond` | `app/art/scenes/1794-music-from-beyond.webp` | illustration | Музыка Иного | «Царство Террора», с. 82 |
| `tsarstvo-terrora-ru/scene/1794-the-guillotine` | `app/art/scenes/1794-the-guillotine.webp` | illustration | Гильотина | «Царство Террора», с. 83 |
| `tsarstvo-terrora-ru/scene/1794-denouement` | `app/art/scenes/1794-denouement.webp` | illustration | Праздник Верховного Существа | «Царство Террора», с. 86 |
| `tsarstvo-terrora-ru/location/paris-bastille` | `app/art/locations/paris-bastille.webp` | illustration | Бастилия | «Царство Террора», с. 109 |
| `tsarstvo-terrora-ru/handout/reign-handout-1` | `app/art/handouts/reign-handout-1.webp` | handout | Царство № 1: отчёт капитана Луи Малона | «Царство Террора», с. 114 |
| `tsarstvo-terrora-ru/handout/reign-handout-2` | `app/art/handouts/reign-handout-2.webp` | handout | Царство № 2: дневник безымянного солдата | «Царство Террора», с. 115 |
| `tsarstvo-terrora-ru/handout/1789-handout-3` | `app/art/handouts/1789-handout-3.webp` | handout | Царство № 3: «Что такое третье сословие?» | «Царство Террора», с. 116 |
| `tsarstvo-terrora-ru/handout/1789-handout-4` | `app/art/handouts/1789-handout-4.webp` | handout | Царство № 4: «Знай своё место» | «Царство Террора», с. 116 |
| `tsarstvo-terrora-ru/handout/1794-handout-5` | `app/art/handouts/1794-handout-5.webp` | handout | Царство № 5: отрывок из «Верховной Пустоты» | «Царство Террора», с. 117 |
| `tsarstvo-terrora-ru/handout/reign-players-map-1789` | `app/art/handouts/reign-players-map-1789.webp` | handout | Карта Парижа 1789 года для игроков | «Царство Террора», с. 118 |
| `tsarstvo-terrora-ru/handout/reign-players-map-1794` | `app/art/handouts/reign-players-map-1794.webp` | handout | Карта Парижа 1794 года для игроков | «Царство Террора», с. 119 |

### `sny-o-yaponii-ru` — 3

Сопоставление `japan.json`, рамки `japan-boxes.json`, предложения `japan-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `sny-o-yaponii-ru/character/edgar-lee-chadwick` | `app/art/characters/japan-edgar-lee-chadwick.webp` | portrait | Эдгар Ли-Чедвик в инвалидном кресле | «Сны о Японии», с. 8 (физ. 9) |
| `sny-o-yaponii-ru/character/alfred-noble` | `app/art/characters/japan-alfred-noble.webp` | portrait | Альфред Нобл в своём офисе | «Сны о Японии», с. 12 (физ. 13) |
| `sny-o-yaponii-ru/scene/hundred-candles` | `app/art/scenes/japan-hundred-candles.webp` | illustration | Сто свечей | «Сны о Японии», с. 18 (физ. 19) |

### `tri-koshmarnykh-vechera-ru` — 6

Сопоставление `nightmare-evenings.json`, рамки `nightmare-evenings-boxes.json`, предложения `nightmare-evenings-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `tri-koshmarnykh-vechera-ru/scene/glow-pobeg` | `app/art/scenes/glow-pobeg.webp` | illustration | Побег от монстра | «Три кошмарных вечера», с. 62 (физ. 63) |
| `tri-koshmarnykh-vechera-ru/scene/glow-nachalo-nalet` | `app/art/scenes/glow-nachalo-nalet.webp` | illustration | Авария | «Три кошмарных вечера», с. 68 (физ. 69) |
| `tri-koshmarnykh-vechera-ru/scene/glow-otschet-vremeni` | `app/art/scenes/glow-otschet-vremeni.webp` | illustration | Сияние в горах | «Три кошмарных вечера», с. 74 (физ. 75) |
| `tri-koshmarnykh-vechera-ru/location/glow-khizhina-7-komnata-missi` | `app/art/locations/glow-khizhina-7-komnata-missi.webp` | illustration | Комната Мисси | «Три кошмарных вечера», с. 77 (физ. 78) |
| `tri-koshmarnykh-vechera-ru/location/glow-khizhina-9-samodelnye-kletki` | `app/art/locations/glow-khizhina-9-samodelnye-kletki.webp` | illustration | Клетки | «Три кошмарных вечера», с. 78 (физ. 79) |
| `tri-koshmarnykh-vechera-ru/scene/glow-stolknovenie-s-tsvetom` | `app/art/scenes/glow-stolknovenie-s-tsvetom.webp` | illustration | Уничтожение сарая | «Три кошмарных вечера», с. 83 (физ. 84) |

### `naedine-s-pomekhami-ru` — 7

Сопоставление `pomekhi.json`, рамки `pomekhi-boxes.json`, предложения `pomekhi-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `naedine-s-pomekhami-ru/item/videokamera` | `app/art/items/pomekhi-videokamera.webp` | illustration | Разбитая камера | «Наедине с помехами», с. 8 |
| `naedine-s-pomekhami-ru/location/black-hills` | `app/art/locations/pomekhi-black-hills.webp` | illustration | Блэк-Хиллз | «Наедине с помехами», с. 17 |
| `naedine-s-pomekhami-ru/location/khizhina-marka` | `app/art/locations/pomekhi-khizhina-marka.webp` | illustration | Хижина | «Наедине с помехами», с. 21 |
| `naedine-s-pomekhami-ru/item/televizor-i-videomagnitofon` | `app/art/items/pomekhi-televizor-i-videomagnitofon.webp` | illustration | Телевизор | «Наедине с помехами», с. 27 |
| `naedine-s-pomekhami-ru/location/peshekhodnaya-tropa` | `app/art/locations/pomekhi-peshekhodnaya-tropa.webp` | illustration | Лесная прогулка | «Наедине с помехами», с. 35 |
| `naedine-s-pomekhami-ru/location/zabroshennyy-saray` | `app/art/locations/pomekhi-zabroshennyy-saray.webp` | illustration | Сарай | «Наедине с помехами», с. 52 |
| `naedine-s-pomekhami-ru/character/neznakomets` | `app/art/characters/pomekhi-neznakomets.webp` | illustration | Незнакомец | «Наедине с помехами», с. 68 |

### `temnye-veka-tri-stsenariya-ru` — 20

Сопоставление `dark-ages.json`, рамки `dark-ages-boxes.json`, предложения `dark-ages-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `coc:creature:dverg` | `app/art/creatures/ages-dverg.webp` | art | Дверг | «Ктулху: Тёмные века» (фанатский перевод), с. 169 (физ. 170) |
| `coc:creature:demon-of-bula-shess` | `app/art/creatures/ages-demon-of-bula-shess.webp` | art | Демон Була-Шесс | «Ктулху: Тёмные века» (фанатский перевод), с. 170 (физ. 171) |
| `temnye-veka-tri-stsenariya-ru/creature/mythos-goblin` | `app/art/creatures/mythos-goblin.webp` | art | Гофф’н Хупадг (гоблин) | «Ктулху: Тёмные века» (фанатский перевод), с. 171 (физ. 172) |
| `coc:creature:gotii` | `app/art/creatures/ages-gotii.webp` | art | Готии | «Ктулху: Тёмные века» (фанатский перевод), с. 171 (физ. 172) |
| `coc:creature:children-of-the-green-god` | `app/art/creatures/ages-children-of-the-green-god.webp` | art | Дитя Зелёного Бога | «Ктулху: Тёмные века» (фанатский перевод), с. 172 (физ. 173) |
| `coc:creature:horig` | `app/art/creatures/ages-horig.webp` | art | Хориг | «Ктулху: Тёмные века» (фанатский перевод), с. 173 (физ. 174) |
| `coc:creature:nameless-mist` | `app/art/creatures/ages-nameless-mist.webp` | art | Безымянный Туман | «Ктулху: Тёмные века» (фанатский перевод), с. 173 (физ. 174) |
| `coc:creature:pucel` | `app/art/creatures/ages-pucel.webp` | art | Пуцел | «Ктулху: Тёмные века» (фанатский перевод), с. 175 (физ. 176) |
| `coc:creature:skraeling` | `app/art/creatures/ages-skraeling.webp` | art | Скрелинг | «Ктулху: Тёмные века» (фанатский перевод), с. 176 (физ. 177) |
| `coc:creature:spawn-of-the-abyss` | `app/art/creatures/ages-spawn-of-the-abyss.webp` | art | Порождение Бездны | «Ктулху: Тёмные века» (фанатский перевод), с. 176 (физ. 177) |
| `coc:creature:teutates` | `app/art/creatures/ages-teutates.webp` | art | Тевтат | «Ктулху: Тёмные века» (фанатский перевод), с. 177 (физ. 178) |
| `temnye-veka-tri-stsenariya-ru/creature/mythos-worms-of-the-earth` | `app/art/creatures/mythos-worms-of-the-earth.webp` | art | Земляной червь | «Ктулху: Тёмные века» (фанатский перевод), с. 178 (физ. 179) |
| `coc:creature:basilisk` | `app/art/creatures/ages-basilisk.webp` | art | Василиск | «Ктулху: Тёмные века» (фанатский перевод), с. 179 (физ. 180) |
| `coc:creature:dragon` | `app/art/creatures/ages-dragon.webp` | art | Дракон | «Ктулху: Тёмные века» (фанатский перевод), с. 179 (физ. 180) |
| `coc:creature:scucca` | `app/art/creatures/ages-scucca.webp` | art | Скукка | «Ктулху: Тёмные века» (фанатский перевод), с. 180 (физ. 181) |
| `coc:creature:thyrs` | `app/art/creatures/ages-thyrs.webp` | art | Тирс | «Ктулху: Тёмные века» (фанатский перевод), с. 181 (физ. 182) |
| `temnye-veka-tri-stsenariya-ru/creature/mythos-vampire` | `app/art/creatures/mythos-vampire.webp` | art | Вампир | «Ктулху: Тёмные века» (фанатский перевод), с. 182 (физ. 183) |
| `temnye-veka-tri-stsenariya-ru/creature/mythos-pontius-pilate` | `app/art/creatures/mythos-pontius-pilate.webp` | art | Понтий Пилат | «Ктулху: Тёмные века» (фанатский перевод), с. 182 (физ. 183) |
| `temnye-veka-tri-stsenariya-ru/creature/mythos-werewolf` | `app/art/creatures/mythos-werewolf.webp` | art | Оборотень | «Ктулху: Тёмные века» (фанатский перевод), с. 183 (физ. 184) |
| `coc:creature:wight` | `app/art/creatures/ages-wight.webp` | art | Сущность | «Ктулху: Тёмные века» (фанатский перевод), с. 184 (физ. 185) |

### `naedine-s-prilivom-ru` — 6

Сопоставление `tide.json`, рамки `tide-boxes.json`, предложения `tide-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `naedine-s-prilivom-ru/character/banyu` | `app/art/characters/tide-banyu.webp` | portrait | Банью | «Наедине с приливом», с. 12 (физ. 13) |
| `naedine-s-prilivom-ru/character/mister-uorren` | `app/art/characters/tide-mister-uorren.webp` | portrait | М-р Уоррен | «Наедине с приливом», с. 19 (физ. 20) |
| `naedine-s-prilivom-ru/character/ofitser-pauell` | `app/art/characters/tide-ofitser-pauell.webp` | illustration | Драка с офицером Пауэллом | «Наедине с приливом», с. 27 (физ. 28) |
| `naedine-s-prilivom-ru/location/ozero` | `app/art/locations/tide-ozero.webp` | illustration | Озеро | «Наедине с приливом», с. 40 (физ. 41) |
| `naedine-s-prilivom-ru/creature/bokrug` | `app/art/creatures/tide-bokrug-2.webp` | art | Бокруг | «Наедине с приливом», с. 57 (физ. 58) |
| `naedine-s-prilivom-ru/location/tserkov` | `app/art/locations/tide-tserkov.webp` | illustration | Внутри церкви | «Наедине с приливом», с. 68 (физ. 69) |

### `naedine-s-tmoy-ru` — 3

Сопоставление `dark.json`, рамки `dark-boxes.json`, предложения `dark-proposals.json`.

| Запись | Файл | Вид | Подпись | Источник |
|---|---|---|---|---|
| `naedine-s-tmoy-ru/location/nyu-york-redaktsiya-nyu-york-san` | `app/art/locations/dark-nyu-york-redaktsiya-nyu-york-san.webp` | illustration | Параграф 86. «Нью-Йорк Сан» | «Наедине с тьмой», с. 23 (физ. 24) |
| `naedine-s-tmoy-ru/location/kair-bazar-fudzhayra` | `app/art/locations/dark-kair-bazar-fudzhayra.webp` | illustration | Параграф 134. Базар Фуджайра | «Наедине с тьмой», с. 29 (физ. 30) |
| `naedine-s-tmoy-ru/location/afiny-port-pirey` | `app/art/locations/dark-afiny-port-pirey.webp` | illustration | Параграф 173. Пирей с высоты птичьего полёта | «Наедине с тьмой», с. 34 (физ. 35) |
