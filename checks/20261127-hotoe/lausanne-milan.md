# «Ужас в Восточном экспрессе», книга II: «Ноктюрн» и «Нота в ноту» — часть lausanne-milan

Источник: `hotoe-book-2-en`, с. 181–232, 256–264 (печатная = физическая − 2); раздатка — `hotoe-book-6-handouts-en`, с. 45–52, 83–89;
карты — `hotoe-keeper-maps-en` (листы 5, 6), `hotoe-player-maps-en` (листы 3, 4); реквизит `hotoe-scroll-of-the-head-en`.
Решения: Р-254, Р-251, Р-202, Р-190, Р-206, Р-209, Р-154, Р-208. Русский текст — наш перевод (флаг `translated`).
Скрипты — `.cache/lead-tools/gen-hotoe-lausanne-milan/` (`gen_*.py`; карты — `gen_maps.py --render`, картинки — `art_crops.py`).

Сокращения: `B2/` = `kb/books/hotoe-book-2-en/`; S = scene, L = location, C = character, H = handout, I = item, M = map, O = organization.

## Заголовки книги

### «Nocturne: Lausanne 1923» (с. 181–207)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Nocturne (вступление, автор Nick Hagger) | 181 | `B2/scenario/nocturne` (summary, hook) |
| Arrival | 181–182 | S `lausanne-arrival`; L `lausanne-railway-station`; C `jean-claude` |
| Lausanne (врезка) | 182 | `coc:location:lausanne` (описание) |
| Events in Lausanne in 1923 (врезка) | 182 | `coc:location:lausanne`, таблица «Лозанна в 1923 году» (сценарий — `from`) |
| Rue St. Etienne | 182 | S `lausanne-rue-st-etienne`; L `lausanne-wellington-fils` |
| The Taxidermist Shop: Ground Floor (Shop Front, Store Room, Study, Work Room), Upper Floor (Kitchen / Dining Room, William's Bedroom, Edgar's Bedroom) | 183 | L `lausanne-wellington-shop-front`, `-store-room`, `-study`, `-work-room`, `-kitchen`, `-williams-bedroom`, `-edgars-bedroom` |
| Breaking In | 183 | S `lausanne-rue-st-etienne` |
| 50, rue St. Etienne (план) | 184, 256 | M `lausanne-50-rue-st-etienne`; игроки (книга VI, с. 83) — M `lausanne-50-rue-st-etienne-players` |
| Visiting the Shop | 184 | S `lausanne-visiting-the-shop` |
| Edgar Wellington; Edgar Wellington's Hobby | 184–185 | C `edgar-wellington` (description, legend) |
| William Wellington | 185 | C `william-wellington` |
| Taking Tea | 185 | S `lausanne-visiting-the-shop`; tome `coc:tome:scroll-of-the-head`; C `raoul-malon` |
| The Duke Arrives | 186 | S `lausanne-visiting-the-shop` |
| Карта Лозанны | 186, 257, 258 | M `lausanne-city` (Keeper Maps 5), M `lausanne-city-players` (Player Maps 3; книга VI, с. 85) |
| The 7:30 Club (что это) | 187 | O `lausanne-730-club` |
| Duc Jean Floressas des Esseintes | 187–188 | C `jean-floressas-des-esseintes` (legend) |
| A Tour of Lausanne: The Cathedral, Cantonal Museum and Library, Le Signal, Le Chat Noir | 188–189 | S `lausanne-tour`; L `lausanne-cathedral`, `lausanne-cantonal-museum`, `lausanne-palais-de-rumine`, `lausanne-le-signal`, `lausanne-le-chat-noir` |
| The Rest of the Afternoon: The Duke's House, The Taxidermy Shop, Looking in the Library | 189 | S `lausanne-afternoon`; L `lausanne-dukes-house`; I `lausanne-door-of-souls`; копия `coc:tome:unaussprechlichen-kulten` (предложение) |
| The 7:30 club; My Life, According to Max; Max's True Story | 190 | S `lausanne-730-club`; C `maximillian-von-wurtheim` |
| Behind the Scenes | 190–191 | S `lausanne-behind-the-scenes` |
| The Murders in Rue St. Etienne; Inside the Shop; Alerting the Police | 191–192 | S `lausanne-murders` |
| Investigating the Clues: The Receipt, The Scroll, The Green Bottle, The Diary, A Logical Conclusion | 192 | S `lausanne-investigating-the-clues`; I `lausanne-fake-scroll`, `lausanne-dream-drug` |
| Lausanne Handout #1 | 193 (VI, 45) | H `lausanne-handout-1-edgar-wellington-diary` |
| Taking the Drug; Dream Drug Logistics | 193–194 | S `lausanne-taking-the-drug` |
| Dream Lausanne | 194 | S `lausanne-dream-wasteland`; L `lausanne-dream-lausanne` |
| The Wasteland; The Dream Shop | 195–196 | S `lausanne-dream-wasteland`; L `lausanne-dream-wasteland`, `lausanne-dream-taxidermy-shop` |
| Lausanne Handout #2 (Summarizing the Scroll) | 195 (VI, 45) | H `lausanne-handout-2-summarizing-the-scroll` |
| The Streets of Dream Lausanne; First … Seventh Event | 196–198 | S `lausanne-dream-streets`; таблица «Лозанна снов: видения» в `nocturne` |
| For Whom the Bell Tolls; A Short Interview | 198–199 | S `lausanne-dream-for-whom-the-bell-tolls`; L `lausanne-dream-place-de-la-palud` |
| The Trial; The First / Second / Third Charge | 199–200 | S `lausanne-dream-trial` |
| Scoring for the Trial; Trial Results (врезка) | 200 | таблица «Суд в Лозанне снов: подсчёт» в `nocturne`; S `lausanne-dream-trial` |
| The Prince and the Prosecutor (полностраничная иллюстрация) | 201 | `atmosphere-lausanne-milan.json` |
| Lausanne Handout #3 (A Sample Passage From the Scroll) | 202 (VI, 47) | H `lausanne-handout-3-sample-passage` |
| Bargaining With the Prince | 202 | S `lausanne-dream-trial` |
| The Verdict; The Escape; The Dream Fades | 202–203 | S `lausanne-dream-verdict` |
| Sample Mob in Dream Lausanne (статблок, шесть горожан) | 203 | C `mob-in-dream-lausanne` (variants) |
| The Waking World; About the Scroll | 203–204 | S `lausanne-waking-world` |
| The Scroll of the Head; The Typescript (характеристики) | 204 | `coc:tome:scroll-of-the-head`; `B2/tome/lausanne-scroll-of-the-head-typescript` (edition_of) |
| The Perilous Lunch; Foiling the Duke | 204–205 | S `lausanne-perilous-lunch` |
| Conclusion | 205 | `nocturne`: conclusion, таблица «Ноктюрн: награды» |
| Spells: Brew Dream Drug, Enchant Flesh, Graft Flesh | 206 | общие `coc:spell:brew-dream-drug`, `enchant-flesh`, `graft-flesh` — источник и расхождения с Grand Grimoire предложены (proposals) |
| Statistics: Edgar Wellington, William Wellington, Maximillian von Wurtheim, Duc Jean Floressas des Esseintes | 207 | C `edgar-wellington`, `william-wellington`, `maximillian-von-wurtheim`, `jean-floressas-des-esseintes` |
| Реквизит «The Scroll of the Head» (пересказ, «How to use these scrolls», факсимиле) | — | H `lausanne-scroll-of-the-head-facsimile`; картинка — у него и у `coc:tome:scroll-of-the-head` |

### «Note For Note: Milano 1923» (с. 208–230)

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Note For Note (вступление, автор Bernard Caleo) | 208 | `B2/scenario/note-for-note` (summary, hook) |
| Brothers of the Skin | 208 | `note-for-note` advice; O `milan-brothers-of-the-skin`; абзац для `coc:organization:brothers-of-the-skin` (предложение) |
| Italy in the 1920s: Passports, Customs, Police, Money, Government | 209 | таблица «Италия в 1920-е» — предложена `coc:location:milan`, в сценарии — `from` |
| Keeper Information | 209–210 | `note-for-note` keeper_info; C `arturo-faccia`; O `milan-brothers-of-the-skin` |
| Arriving in Milan; Symptoms of the City; Caterina Cavollaro; The Shell of the City | 211–213 | S `milan-arriving`; L `milan-stazione-centrale` |
| Events in Milan 1923 (врезка) | 211 | таблица «Милан в 1923 году» — предложена `coc:location:milan` |
| Milan Handout #1 | 212 (VI, 49) | H `milan-handout-1-opera-star-missing` |
| Milan (врезка: история, город в 1923) | 213 | предложения `coc:location:milan` (history, абзац 1923 года); L `milan-santa-maria-delle-grazie`; `lokhmotya-korolya-ru/location/milan-university` (предложение) |
| Scenario Timeline (врезка) | 214 | таблица «Нота в ноту: хронология» в `note-for-note` |
| The Cause | 214 | S `milan-arriving` |
| Searching for Caterina: Station Porters, Cavarollo's Apartment, The Police, Patrons, La Scala | 214–216 | S `milan-searching-for-caterina`; L `milan-cavollaro-townhouse`, `milan-police-station`; C `ysabel` |
| Milan Handout #2 | 216 (VI, 49) | H `milan-handout-2-automobile-worker-murdered` |
| Centro di Milano: La Galleria Vitorrio Emanuele, Their Hotel Rooms, Il Duomo | 216–217 | S `milan-centro`; L `milan-galleria-vittorio-emanuele`, `milan-caffe-biffi`, `milan-duomo`, `milan-piazza-del-duomo`; I `milan-la-scala-guidebook` |
| Milan Handout #3 | 217 (VI, 49) | H `milan-handout-3-a-welcome-return` |
| In the Cathedral; The Three Crones; A Crazy Old Man | 217–218 | S `milan-in-the-cathedral`; C `father-angelico`, `three-crones` |
| A Midnight Episode | 218 | S `milan-midnight-episode` |
| Death of a Unionist; Involving the Investigators; The Body; The Murder Scene | 218–219 | S `milan-death-of-a-unionist`; C `ennio-spinola`; L `milan-portello`, `milan-portello-warehouse` |
| Conti's Apartment | 219–221 | S `milan-contis-apartment`; L `milan-conti-apartment`; C `flavio-conti` |
| Teatro alla Scala, Milan (план) | 220, 261 | M `milan-teatro-alla-scala`; игроки (книга VI, с. 89) — M `milan-teatro-alla-scala-players`; ключ — таблица «Ла Скала: ключ плана» у L `milan-teatro-alla-scala` |
| Faccia's Mansion | 221 | S `milan-contis-apartment`; L `milan-faccia-mansion`, `milan-faccia-warehouse` |
| La Scala; Entry | 221 | S `milan-la-scala`; L `milan-teatro-alla-scala`, `milan-piazza-della-scala`, `milan-scala-stage-door` |
| Spells: Transfer Organ, Control Skin | 222 | общие `coc:spell:transfer-organ`, `control-skin` — источник и расхождения предложены |
| Backstage; The Music Director; Paolo Rischonti | 222–224 | S `milan-la-scala`; C `arturo-toscanini`, `paolo-rischonti` |
| The Costumery; Further Searches; Benito's Orders | 224–225 | S `milan-la-scala`; L `milan-scala-costumery`; C `luisa-visconti`, `benito-andriani` |
| Milan Handout #4 | 225 (VI, 51) | H `milan-handout-4-cavollaros-disappearance` |
| The Performance; The Newspapers; Return To La Scala | 226 | S `milan-the-performance` |
| Milan Handout #5 | 226 (VI, 51) | H `milan-handout-5-milanese-man-murdered` |
| Opening Night; The Best Seats in the House | 226–228 | S `milan-opening-night`; L `milan-scala-stalls`, `milan-scala-stage` |
| Six Brothers of the Skin, Milan Chapter (статблок, таблица) | 228 | C `brothers-of-the-skin-milan-chapter` (variants) |
| Finale | 228–229 | S `milan-finale` |
| Conclusion; Caterina Cavollaro; Postscriptum | 229 | `note-for-note` conclusion, таблица «Нота в ноту: награды»; S `milan-finale`; судьба Каволларо — предложение к `B2/character/caterina-cavollaro` |
| Statistics: Father Angelico, Marco Baldo, Flavio Conti, Benito Andriani, Arturo Faccia | 229–230 | C `father-angelico`, `marco-baldo`, `flavio-conti`, `benito-andriani`, `arturo-faccia` |
| Statistics: Caterina Cavollaro, Age 27 (Looks 87*), ex-Opera Star | 230 | вариант статблока — предложение к `B2/character/caterina-cavollaro` (запись части paris, Р-125) |
| Карта Милана | 215, 259, 260 | M `milan-city` (Keeper Maps 6), M `milan-city-players` (Player Maps 4; книга VI, с. 87); ключ — таблица «Милан: места на карте (1923)» (предложение городу) |

### Страницы 231–232, 256–264

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Keeper's Entries: Additional Characters, Special Items and Information, Important Events | 231 | не взято — пустые бланки |
| Keeper's Subplots, Notes, Baleful Influence (бланк: часть статуи — владелец) | 232 | не взято — пустые бланки |
| 50, rue St. Etienne | 256 | M `lausanne-50-rue-st-etienne` |
| Lausanne Keeper's Map / Players' Map | 257 / 258 | M `lausanne-city` / `lausanne-city-players` |
| Milan Keeper's Map / Players' Map | 259 / 260 | M `milan-city` / `milan-city-players` |
| Teatro alla Scala, Milan | 261 | M `milan-teatro-alla-scala` |
| Index of Significant & Useful Entries | 262–264 | не взято — указатель книги |

## Записи части (134 файла)

- Этапы: 2 (`nocturne`, order 6; `note-for-note`, order 7; `part_of` — кампания).
- Сцены: 28 (Лозанна 17, Милан 11).
- Места: 60 — общий город `coc:location:lausanne` (новый); Лозанна 24 (ключ карты 1–15, вокзал, окрестности, 7 комнат мастерской); Лозанна снов 4 (город сна, пустошь, мастерская сна, площадь Палю); Милан 31 (ключ карты 1–16 кроме университета «Лохмотьев Короля», Пьяцца дель Дуомо, Пьяцца делла Скала, «Биффи», Портелло и склад, окрестности и склад Фаччи, полиция; «Ла Скала»: 4 уровня плана, сцена, партер, служебный вход, костюмерная).
- Персонажи: 19 (со статблоками — 11, из них 2 групповых профиля; без статблоков — 8).
- Организации: 2 (клуб «7:30», миланская ячейка Братьев кожи).
- Предметы: 4 (поддельный свиток, наркотик снов, Дверь самоубийц, книга о «Ла Скала»).
- Книги Мифов: 2 (`coc:tome:scroll-of-the-head` — общая, новая; машинописный перевод — запись книги, `edition_of`).
- Раздаточные материалы: 9 (Лозанна 1–3, Милан 1–5, реквизит «Свиток Головы»).
- Карты: 8 (по две — Хранителя и игроков — для Лозанны, улицы Сент-Этьен, 50, Милана и «Ла Скала»); картинки `app/maps/hotoe-lausanne-milan-*.jpg`.
- Картинки: 13 (`app/art/**/hotoe-lausanne-milan-*.webp`: 3 портрета, 9 раздаток, 1 факсимиле свитка у книги Мифов) — сопоставление `art-lausanne-milan.json`, предложения картинок применены к записям части.
- Атмосферные иллюстрации — `atmosphere-lausanne-milan.json` (9 страниц) — сводит ведущий.
- Предложения чужим записям — `proposals-lausanne-milan.json` (59; пробный прогон `apply.py --dry-run` — все ложатся).
- `new-shared-locations-lausanne-milan.json` не нужен: Лозанну заводит сама часть, Милан есть.

## Не взято

- Keeper's Entries (с. 231–232): пустые бланки для записей Хранителя (персонажи, предметы, события, подсюжеты, заметки, владельцы частей статуи).
- Index of Significant & Useful Entries (с. 262–264): указатель книги.
- Колонтитулы и подписи страниц; атмосферные иллюстрации (с. 181, 187, 194, 196, 201, 205, 210, 216 «Alfa Romeo, 1922», 224) — в `atmosphere-lausanne-milan.json` (Р-241).
- Упомянутые мимоходом без записей (текстом в записях): Ж.-К. Гюисманс, Оттон де Грансон (статуя), папа Григорий X, г-н де Шантье, Джузеппе Менгони, лорд Керзон, Муссолини, Виктор Эммануил III, Роуз Уайлдер Лейн, дублёрша Мария Диматтина, тенор-Радамес, покровители из Милан 3 (Нунцио Точчи, чета Сорренти, Анджела Суско, Серена Спаньоло, Розарио Сорбелло), импресарио Каволларо, носильщики вокзала Милана, следователь по делу Спинолы, хамелеон Фаччи (немагический питомец — способность у Фаччи), семья Лорьен (записи части paris — текстом).
- Строки ключа карты без текста в главе (гостиницы Лозанны 4–6, отели и кафе Милана 6, 8–10, площадь Рипонн, Арена, вокзал Дора, Шильон): записи заведены с описанием «есть только на карте» — описания добавит часть companion («Спутник путешественника»).
- План «Ла Скала»: номера 2 (уборные) и 10 (лестница наверх) подвала на скане не различимы — меток нет (есть в таблице ключа).

## Опечатки и сомнения книги

- Эдгар: «Brawl 50% (25/12)» — пятая 10; исправлено в записи (`errata`, fixed).
- Герцог: Скорость 6 при ЛВК 65, СИЛ 60 < ТЕЛ 75 (по правилам 7, с поправкой за 90 лет — 2) — как напечатано; с. 194 ссылается на запись «Dream Drug» при статистике герцога — её нет.
- Бенито Андриани: ЛВК 14 при Скорости 8 и Уклонении 44% — вероятная опечатка (как напечатано).
- Каволларо (Милан): «Dodge 30% (12/5)» — должно быть (15/6); предложено исправить в варианте.
- Толпа Лозанны снов: Уклонение 35% ниже половины ЛВК 75/70 у части горожан; Братья кожи: общая Скорость 8 при правиле 7 у части — как напечатано.
- Третий Брат: ПЗ 14 при (ВЫН 70 + ТЕЛ 65)/10 = 13,5 — округление вверх (приём книги, Р-161).
- с. 219: «Transform Organ» вместо «Transfer Organ».
- с. 182: «seek out Worthington» вместо Wellington; с. 185: «he has not been unable to uncover much» (лишнее отрицание); с. 204: «Sedekfar Scrolls»; с. 208: «This aventure»; с. 214: «Cavarollo's Apartment»; с. 216: «Vitorrio»; с. 209: «Carbinieri», «Partitio Nazionale Fascista»; с. 213: «Avonti!-Giornole Sociolisto» (Avanti!) и «столица Священной Римской империи» в IV веке (Западной Римской) — словесные, исправлены в переводе молча (Р-39).
- с. 221: на Пьяцца делла Скала — «статуя Микеланджело» (на деле памятник Леонардо) — как напечатано, пометка в записи площади.
- Реквизит «Scroll of the Head»: «Scroll of the Right Arm / Left Arm» против «Right Hand / Left Hand» книги (с. 195) — `errata` у книги Мифов и у факсимиле.
- Хронология (с. 214): сыщики выходят в Лозанне «в 7 утра» (с. 181 — 6:45); отъезд из Милана «в 13:00» (с. 229 — 13:20); Милан 1: Каволларо сошла с поезда «в 1pm» (экспресс — 12:20).
- Указатель (с. 263): «Otto of Grandson» (в тексте — Otho).
- Нож Фаччи: «Cult Skinning Knife 60%» без половины и пятой — вычислены.

## Вопросы и кандидаты

- Ссылки на записи, которые ещё пишут другие части (check.py ждёт их): `hotoe-book-4-en/character/selim-makryat` (constantinople), `hotoe-book-4-en/scenario/blue-train-black-night` (return).
- Заклинание «Animate Skin» (герцог) — без ссылки: книга относит его к «New Spells» книги IV (часть constantinople); кандидат `coc:spell:animate-skin`.
- Запись Каволларо (часть paris) называет главу «Нота за нотой» и Галерею «Виктора Эммануила» — предложена замена на «Нота в ноту» и «Галерея Витторио Эмануэле» (у этапа «Нота за нотой» оставлено псевдонимом).
- Лозанна снов — запись книги `город` без `part_of`, со ссылкой на Лозанну (как Город колоколов, Р-190); индекс книги относит её к Стране грёз, текст — нет.
- План «Ла Скала»: 44 номера на четырёх уровнях сведены в записи уровней (ключ — таблица у театра, метки — с пояснением `text`); свои записи — только помещениям, важным для игры. Если владелец хочет запись на каждый номер — добавить.
- Склад, куда увезли Каволларо (с. 210 «склад на окраине»), книга не уточняет — ни к складу Фаччи, ни к складу в Портелло не привязан.

## Термины (английский → русский)

| English | Русский |
|---|---|
| Nocturne | Ноктюрн (этап «Ноктюрн: Лозанна, 1923») |
| Note for Note | Нота в ноту (этап «Нота в ноту: Милан, 1923») |
| Dream Lausanne | Лозанна снов |
| Waking World | мир яви (глоссарий) |
| Jigsaw Prince | Лоскутный принц |
| the Duke / the Prince | Герцог / Принц |
| Duc Jean Floressas des Esseintes | Жан Флоресса дез Эссент (герцог дез Эссент) |
| dream drug | наркотик снов (как у «Сварить наркотик снов») |
| Scroll of the Head / the Typescript | Свиток Головы / машинописный перевод |
| Scroll of the Belly, of the Legs, of the Right Hand, of the Left Hand | Свиток Чрева, Свиток Ног, Свиток Правой руки, Свиток Левой руки |
| Sedefkar the Osmanli | Седефкар Османлы |
| Baleful Influence | пагубное влияние |
| The 7:30 Club | клуб «7:30» |
| Wellington Fils, Taxidermie | мастерская «Веллингтон и сын» |
| Edgar / William Wellington | Эдгар / Уильям Веллингтон |
| Maximillian von Wurtheim (Brüllig) | Максимилиан фон Вуртхайм (Брюллиг) |
| Raoul Malon | Рауль Малон |
| Rue St. Etienne; Rue du Pré | улица Сент-Этьен; улица дю Пре |
| Le Chat Noir; Le Signal; Musée Arlaud; Cantonal Museum; Palais de Rumine | кафе «Ле Ша Нуар»; Ле Синьяль; музей Арло; Кантональный музей; дворец Рюмин |
| Place de la Palud; Place de la Riponne | площадь Палю; площадь Рипонн |
| Beau-Rivage Palace; Lausanne-Palace-Beau-Site; Hotel Cecil; Hôtel Central | «Бо-Риваж Палас»; «Лозанна-Палас-Бо-Сит»; «Сесиль»; «Сантраль» |
| Chateau de Chillon | Шильонский замок |
| Conference of Lausanne | Лозаннская конференция |
| The Wasteland; The Dream Shop | Пустошь; мастерская Веллингтонов в Лозанне снов |
| door of the Duke's house | Дверь самоубийц |
| Sample Mob in Dream Lausanne | Толпа Лозанны снов |
| Otho of Grandson | Оттон де Грансон |
| Arturo Faccia; Flavio Conti; Benito Andriani; Ennio Spinola | Артуро Фачча; Флавио Конти; Бенито Андриани; Эннио Спинола |
| Father Angelico; Marco Baldo; Ysabel; Paolo Rischonti; Luisa Visconti | отец Анджелико; Марко Бальдо; Изабель; Паоло Рисконти; Луиза Висконти |
| the three crones | три старухи-костюмерши |
| Brothers of the Skin, Milan chapter | миланская ячейка Братьев кожи |
| Teatro alla Scala; Piazza del Scala | театр «Ла Скала»; Пьяцца делла Скала |
| Il Duomo; Piazza del Duomo | Миланский собор (Дуомо); Пьяцца дель Дуомо |
| La Galleria Vittorio Emanuele; Biffi's | Галерея Витторио Эмануэле; кафе «Биффи» |
| Stazione Centrale; Stazione Dora | Центральный вокзал; вокзал Дора |
| Castello Sforzesco; Santa Maria delle Grazie | замок Сфорца; монастырь Санта-Мария-делле-Грацие |
| Caffè Cova; Hotel de la Ville; Grand Hotel Marino et National; Hotel Cavour | кафе «Кова»; «Де ла Виль»; Гранд-отель «Марино э Насьональ»; «Кавур» |
| Portello; Conti Machine Parts | Портелло; «Конти: детали машин» |
| costumiers' curse | проклятие костюмеров |
| Collapse of Milan | упадок Милана |
| Costumery; Stage Doors; Stalls | костюмерная; служебный вход (двери); партер |
| Blackshirts; Vigili; Carabinieri; Militi | чернорубашечники; вигили; карабинеры; милиция |
| Stare Unnervingly; Taxidermy; Scrawl Note; Understand English | Смущающий взгляд; Таксидермия; Писать записки; Понимать английский |
| Concoct Assassinations; Enjoy Life; Protect Property; Refuse Entry | Подстроить убийство; Наслаждаться жизнью; Охранять имущество; Не пускать |
| Church Doctrine; Church Law; Oratory; Hide; Sneak | Церковная доктрина; Каноническое право; Ораторское искусство; Прятаться; Подкрадывание |
| Sword Cane; Cult Skinning Knife; Broken Chair | трость-шпага; культовый свежевальный нож; сломанный стул |
| Mythos Rating | Значение Мифов (глоссарий) |
