# Petersen's Abominations — часть «Панацея» (гл. 3, с. 69–106 + раздатка)

Книга `petersens-abominations-en` (печатная = физическая − 1, сверено по с. 69, 79, 80, 87, 88);
отдельные PDF `petersens-abominations-pregens-en` (с. 14–19) и `petersens-abominations-handouts-en` (с. 7–8) — печатная = физической
(на с. 7 раздатки номера нет). Записи — `kb/books/petersens-abominations-en/*` (120 файлов), русский текст — наш перевод (`translated`),
официальные русские формы — по листам прегенов «Кошмаров цифровой эпохи» и официальной раздатке (Р-184).
Готовые сыщики «Панацеи» уже есть в базе по официальному русскому листу (`digital-nightmares-ru/character/*`, Р-147) — вторых записей нет,
английские данные — в `proposals-panacea.json` (38 предложений).

## Заголовки книги → записи

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Chapter 3 «Panacea», эпиграф | 69 | `scenario/panacea` (summary) |
| вступление (место действия, Северный Даллас, прегены) | 69 | `scenario/panacea` (advice), `location/panacea-city` |
| Foreword (Sandy Petersen, 2017) | 69 | `scenario/panacea` (advice) |
| Background | 70 | `scenario/panacea` (keeper_info), `organization/zymedbio`, `organization/anak-cult` |
| The Truth About Zylactis | 70 | `item/zylactis`, `creature/amoebozoans` |
| врезка «The Milk of Shub-Niggurath» (биоциты) | 70 | `item/milk-of-shub-niggurath`, keeper_info |
| The Anak Brothers (и два варианта) | 70–71 | `character/ulysses-anak`, `character/jefferson-anak` |
| Ulysses Anak; Jefferson Anak | 71 | те же записи |
| врезка «Concerning Tcho-Tcho» | 71 | `scenario/panacea` (keeper_info); связь `related_to` с `coc:creature:cho-cho` |
| The Investigators (варианты A/B, шесть прегенов, зацепки варианта B) | 71–72 | `scenario/panacea` (hook); прегены — `digital-nightmares-ru/character/*` |
| Dramatis Personae | 72–73 | `scenario/panacea` (advice) |
| Chuck Ogle, 46, party host | 73 | `character/chuck-ogle` |
| Ted Dawson, 57, police chief | 73–74 | `character/ted-dawson` |
| Anthony Callison, 48, editor | 74 | `character/anthony-callison`, `organization/morning-news` |
| врезка «The Dark Young, Child of Shub-Niggurath» | 74 | `creature/zymedbio-dark-young` |
| Sissy Richards, 37 | 75 | `character/sissy-richards` |
| Andrew Lucio, 24 | 75 | `character/andrew-lucio` |
| Jim Conaty, 51 | 75–76 | `character/jim-conaty` |
| Blanche Yurka, 44 | 76 | `character/blanche-yurka` |
| Other ZyMedBio Employees | 76 | `character/brad-mestler`, `beatrice-april`, `esme-richards`, `tiana-freeman`, `zymedbio-it-team`, `ethan-brock`, `wesley-rice`, `anne-jones`, `lewis-pitts`, `alyssa-dean`, `elina-goul` |
| Part One; The Party | 76–78 | `scene/panacea-the-party` |
| врезка «The Satyrs, Human-Animal Mutants» | 77 | `creature/panacea-lesser-satyr`, `creature/panacea-greater-satyr` (legend) |
| The Investigators save their friend from Chuck Ogle | 78 | `scene/panacea-saving-the-woman`, `character/ogles-victim` |
| Next Steps | 78, 81 | `scene/panacea-saving-the-woman`, `scenario/panacea` (steps, advice) |
| иллюстрация (Огл нападает) | 79 | атмосфера (`atmosphere-panacea.json`) |
| Chuck Ogle's House (план) | 80 | `map/chuck-ogles-house`, `location/chuck-ogles-house`, `location/ogles-bedroom` |
| Part Two | 81 | `scene/panacea-researching-zymedbio` |
| Searching Ogle's House | 81 | `scene/panacea-searching-ogles-house`, `item/ogles-zymedbio-letters` |
| врезка «New Drug Applications» | 81 | `scene/panacea-researching-zymedbio`, `organization/zymedbio` |
| Expansion Option: Ogle Escapes | 81 | `scene/panacea-searching-ogles-house` |
| Handout: Panacea 1 | 82, 191 | `handout/panacea-1-welcome-to-zymedbio` (картинка — PDF раздатки, с. 7) |
| Researching ZyMedBio; Initial research; Deeper research | 83 | `scene/panacea-researching-zymedbio` |
| Expansion Option: FDA Involvement | 83 | `scene/panacea-researching-zymedbio`, `character/ted-dean` |
| Hacking ZyMedBio; Information possibly obtained | 83–84 | `scene/panacea-hacking-zymedbio`, `item/zymedbio-server-data` |
| Contacting People on the Zylactis Trial | 84 | `scene/panacea-contacting-trial-people` |
| Visiting ZyMedBio During Working Hours; Getting an Appointment | 84–85 | `scene/panacea-visiting-zymedbio`, `location/zymedbio-building` |
| Expansion Option: Something in the Water | 85 | `scene/panacea-something-in-the-water` |
| Applying for the Zylactis Trial | 86 | `scene/panacea-applying-for-the-trial` |
| Consequences of Treatment | 86 | `item/zylactis` (mechanics), `scene/panacea-applying-for-the-trial` |
| ZyMedBio Offices (план, ключ 1–60) | 87 | `map/zymedbio-offices`; места `location/zymedbio-*` (крылья, парковка, приёмный блок и 50 записей по номерам 1–60, диапазоны — одной записью) |
| Part Three; Breaking into ZyMedBio; Gaining Entrance | 88 | `scene/panacea-breaking-in` |
| Entrance Lobby; Building Layout | 88–89 | `scene/panacea-entrance-lobby`, места 1–5 |
| Administration Wing (West Wing) | 89–91 | `scene/panacea-administration-wing` |
| Cold Words (врезка, все реплики) | 90 | `scene/panacea-cold-words` |
| Jim Conaty's Office | 91 | `scene/panacea-conatys-office`, `item/conatys-keys` |
| Handout: Panacea 2 | 91, 192 | `handout/panacea-2-experimental-schedule` (картинка — PDF раздатки, с. 8) |
| Where Next?; Possible encounters and clues | 92 | `scene/panacea-where-next`, `item/boteler-surveillance-report` |
| Research Wing (East Wing); Front Corridor | 92–93 | `scene/panacea-research-wing` |
| Rear Corridor; Staff Lounge; Jefferson Anak's Office; Laboratories; Electrical Closet and Flammable Storage; Cold Store | 93 | `scene/panacea-rear-corridor`, `item/jefferson-anaks-whiteboard`, `item/flammable-chemicals`, места 47–54 |
| Lab Animals: The Dogs | 93–94 | `scene/panacea-lab-dogs`, `creature/mutated-dogs` |
| Tertiary Biocyte Storage | 94 | `scene/panacea-tertiary-biocyte-storage`, `location/zymedbio-53-tertiary-biocyte-storage` |
| Delivery Area | 94–95 | `scene/panacea-delivery-area` |
| иллюстрация «The Mutated Canines» | 94 | картинка `creature/mutated-dogs` |
| врезка «Cattle Prods» | 95 | `item/cattle-prods` |
| Milking Room | 95 | `scene/panacea-milking-room`, `location/zymedbio-59-primary-biocyte-collection` |
| East Wing Basement; Confrontation with the Dark Young | 95, 97 | `scene/panacea-east-wing-basement` |
| иллюстрация «The Milking Room» | 96 | картинка `location/zymedbio-59-primary-biocyte-collection` |
| Conclusion; Rewards | 97 | `scenario/panacea` (conclusion) |
| Appendix: Panacea — Non-Player Characters and Monsters | 97–99 | статблоки: `sissy-richards`, `andrew-lucio`, `chuck-ogle`, `ted-dawson`, `anthony-callison`, `panacea-lesser-satyr`, `panacea-greater-satyr`, `mutated-dogs`, `zymedbio-dark-young` |
| иллюстрация «The Satyr» | 98 | картинка `creature/panacea-lesser-satyr` |
| Wade Boteler … Gus Phillips (листы прегенов) | 100–105 | `digital-nightmares-ru/character/{wade-boteler, mary-fuller, elliot-closon, belinda-norwich, marina-kolga, gus-philips}` + предложения; страницы в `sources` сценария |
| с. 106 — иллюстрация к главе «Mohole» | 106 | атмосфера (относится к части mohole) |
| Appendix 1 «Player Handouts»: Panacea 1–2 | 191–192 | раздатки выше |
| иллюстрация к «Панацее» на с. 68 (Конати-сатир у «Tertiary Biocyte Storage», подпись на с. 69) | 68 | картинка `location/zymedbio-53-tertiary-biocyte-storage` (страница в диапазоне части hotel — её не брать) |

## Не взято

- Портреты прегенов (с. 100–105, PDF прегенов с. 14–19): у русских записей уже есть портреты с официальных листов — не дублируются.
- Копии раздаток в тексте главы (с. 82, 91) и в приложении (с. 191–192): картинки взяты из отдельного PDF раздатки (лучше копия).
- Декоративная картинка на с. 88 (бактерии) и иллюстрация с. 79 — атмосфера.
- Упомянутые без своих записей: FDA, полиция Доусона, больница Фуллер и Норвич, дом Доусона, цветочный магазин Сисси, участок лёгкой промышленности; тётя Огла, напарник Филипса, мать Ботелера, отец Клосона, бабушка Колги, пациент Норвич, охранники «ЗиМедБио» (ночью отсутствуют), «врач» на процедурах, хакер-наёмник и охранный подрядчик — без текста и механики, остаются текстом в записях.
- Безымянные сатиры западного крыла (со шприцем, свинья, паук) — встречи в `scene/panacea-where-next` с профилем меньшего сатира, отдельных записей нет.
- Навык «Interface with Computer 90%» тёмной молоди — без записи навыка (механики нет, Р-126). Электропогонялка — предмет, а не позиция справочника оружия (справочник общий; кандидат в `kb/weapons` — решать владельцу).

## Опечатки и противоречия книги (в `errata`)

- Возраст братьев Анак: 65 и 70 лет (с. 71) против «mid-50s» на портретах (с. 89).
- Тед Доусон: Психология 80% (с. 73) против 55% в статблоке (с. 98); Скорость 7 без возрастной поправки.
- Энтони Каллисон: «Master's conditioning» (с. 74) и «Master's mutations» (с. 98) — остаток шаблона, исправлено на Каллисона; ПМ 9 при МОЩ 60 (ожидается 12).
- Чак Огл: Уклонение 20% (ЛВК/2 = 22); Скорость 5 (по правилам 6; возможно, из-за ампутации).
- Меньший сатир: СИЛ 60 и ИНТ 60 при бросках 3d6×5; больший сатир: ИНТ 40 при (3d6)×5 — как напечатано (Р-37).
- Тёмная молодь: во врезке о взломе (с. 84) заклинания Implant Fear и Mindblast, которых нет в списке статблока (с. 99).
- Доильня: «the sixth greater satyrs» — шестеро (исправлено).
- Число сотрудников «ЗиМедБио»: около 80 и почти 100 (с. 83), более 100 (лист Клосона).
- План (с. 87): «Jeffersen Anak»; листок дома Огла: «Bedrooms: 4», а на плане подписано пять спален.
- Листы прегенов (англ.): Ботелер — винтовка «50% (35/14)», Филипс — .38 «50% (30/12)» (в русском листе верно 25/10) — предложено в `errata` русских записей. Ботелер (с. 100): Колга названа кузиной Огла (она его соседка) — в русском переводе исправлено, в errata не записано (Р-39). «Elliot»/«Elliott» Clawson — псевдоним (предложение).

## Термины (English → русский)

| English | Русский |
|---|---|
| ZyMedBio (Corp) | «ЗиМедБио» (офиц.) |
| Zylactis | «Зилактис» (офиц.) |
| Primary / Secondary / Tertiary Biocyte | первичный / вторичный / третичный биоцит (офиц.) |
| Experimental Schedule ZMB17B; Formula B138 | график эксперимента ЗМБ17Б; формула Б138 (офиц.) |
| primary collection units; milk harvesting | первичные агрегаты забора; забор молока (офиц.) |
| SUPPORTING (в раздатке 2) | Поддержание (офиц.) |
| amoebozoans | амебозои |
| the milk of Shub-Niggurath | молоко Шуб-Ниггурат |
| Milking Room | Доильня |
| Primary Biocyte Collection | Забор первичного биоцита |
| lesser / greater satyr | меньший / больший сатир (база) |
| dark young | тёмная молодь (база) |
| tcho-tcho | чо-чо (база) |
| mutated description | мутировавший облик |
| Cold Words | «Холодные слова» |
| cattle prod | электропогонялка |
| Interface with Computer | Связь с компьютером |
| New Drug Application (NDA) | заявка на новый препарат |
| Morning News | «Морнинг ньюс» |
| Vice President (Conaty) | вице-председатель (офиц.) |
| Hard / Extreme roll; Know roll | трудная / чрезвычайная проверка; проверка Знаний |
| имена листов | Уэйд Ботелер, Мэри Фуллер, Эллиот Клосон, Белинда Норвич, Марина Колга, Гас Филипс, Чак Огл, Джим Конати, Бланш Юрка, Сисси Ричардс, начальник полиции Доусон, Энтони Каллисон, Эндрю Лучо, Уэсли Райс (офиц.) |
| наши имена | Улисс и Джефферсон Анак, Тед Доусон, Брэд Местлер, Беатрис Эйприл, Эсме Ричардс, Тиана Фримен, Итан Брок, Энн Джонс, Льюис Питтс, Алисса Дин, Элина Гоул, Алан Госс, Санджит Пингл, Аниш Рама, Джесс Уайт, Тед Дин |

## Для ведущего

- Официальные русские раздатки зарегистрированы ведущим (`digital-nightmares-handouts-ru`): `text.ru` обеих раздаток «Панацеи» заменён официальным текстом (с. 7–8), источник добавлен, прежний перевод — в `corrections`; описание раздаток — наш перевод (флаг `translated` остаётся).
- Смещение страниц основной книги (−1) подтверждено; у PDF прегенов и раздатки смещения нет.
