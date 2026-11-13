# Картинки путеводителя «Аркхэм» (arkham-en), 2026-11-14

Картинки, которые части переноса не взяли (разделы «Не взято» в `checks/20261114-arkham/*.md`), — вырезаны из PDF
книги (`arkham-en`, печатная страница = физическая − 1) и добавлены в `images` записей (Р-165) через
`pipeline/art/add_images.py` (сопоставление `art.json`, предложения `art-proposals.json`, рамки и обрезка — `art-boxes.json`).
Файлы — `app/art/<вид>s/arkham-<slug>[-n].webp`.

Итого: 153 картинки у 147 записей — 90 портретов и 63 других картинок.

Способ вырезки: портреты и часть реклам — область страницы, отрисованной в 150 dpi (с рамкой книги); иллюстрации —
картинка из PDF с её маской прозрачности (`pdfimages`), без текста страницы поверх. Подпись — подпись книги в нашем
переводе (рукописные подписи у иллюстраций, вертикальные подписи у портретов в тексте); у портретов из статблоков
и у картинок без подписи в книге — `null`.

## Портреты (90)

| Файл (`app/…`) | Запись | Вид | Подпись | Страница |
|---|---|---|---|---|
| `art/characters/arkham-overview-william-danvers-johnston.webp` | `arkham-en/character/overview-william-danvers-johnston` (Уильям Данверс Джонстон) | portrait | — | 2023), с. 53 (физ. 54) |
| `art/characters/arkham-overview-joe-ambrose.webp` | `arkham-en/character/overview-joe-ambrose` (Джо Эмброуз) | portrait | — | 2023), с. 53 (физ. 54) |
| `art/characters/arkham-overview-harold-beemis.webp` | `arkham-en/character/overview-harold-beemis` (Гарольд Бимис) | portrait | — | 2023), с. 54 (физ. 55) |
| `art/characters/arkham-overview-robert-czyenck.webp` | `arkham-en/character/overview-robert-czyenck` (Роберт Чиенк) | portrait | — | 2023), с. 54 (физ. 55) |
| `art/characters/arkham-overview-abigail-larue.webp` | `arkham-en/character/overview-abigail-larue` (Абигейл Ларю) | portrait | — | 2023), с. 55 (физ. 56) |
| `art/characters/arkham-overview-edwin-white-perkins-iii.webp` | `arkham-en/character/overview-edwin-white-perkins-iii` (Эдвин Уайт Перкинс III) | portrait | — | 2023), с. 55 (физ. 56) |
| `art/characters/arkham-overview-marla-slocum.webp` | `arkham-en/character/overview-marla-slocum` (Марла Слокам) | portrait | — | 2023), с. 56 (физ. 57) |
| `art/characters/arkham-overview-daniel-swain.webp` | `arkham-en/character/overview-daniel-swain` (Дэниел Суэйн) | portrait | — | 2023), с. 56 (физ. 57) |
| `art/characters/arkham-overview-jennifer-tilstrom.webp` | `arkham-en/character/overview-jennifer-tilstrom` (Дженнифер Тилстром) | portrait | — | 2023), с. 57 (физ. 58) |
| `art/characters/arkham-overview-sheila-torsten.webp` | `arkham-en/character/overview-sheila-torsten` (Шейла Торстен) | portrait | — | 2023), с. 57 (физ. 58) |
| `art/characters/arkham-overview-ellen-whipple-smith.webp` | `arkham-en/character/overview-ellen-whipple-smith` (Эллен Уиппл-Смит) | portrait | — | 2023), с. 58 (физ. 59) |
| `art/characters/arkham-overview-james-allen-white.webp` | `arkham-en/character/overview-james-allen-white` (Джеймс Аллен-Уайт) | portrait | — | 2023), с. 58 (физ. 59) |
| `art/characters/arkham-northside-patrick-ohare.webp` | `arkham-en/character/northside-patrick-ohare` (Патрик О’Хара) | portrait | — | 2023), с. 74 (физ. 75) |
| `art/characters/arkham-northside-jeremiah-williams.webp` | `arkham-en/character/northside-jeremiah-williams` (Джеремайя Уильямс) | portrait | — | 2023), с. 74 (физ. 75) |
| `art/characters/arkham-northside-bartholomew-appley.webp` | `arkham-en/character/northside-bartholomew-appley` (Бартоломью Эппли IV) | portrait | — | 2023), с. 74 (физ. 75) |
| `art/characters/arkham-northside-judith-renforth.webp` | `arkham-en/character/northside-judith-renforth` (Джудит Ренфорт) | portrait | — | 2023), с. 75 (физ. 76) |
| `art/characters/arkham-northside-michael-crane.webp` | `arkham-en/character/northside-michael-crane` (Майкл Крейн) | portrait | — | 2023), с. 78 (физ. 79) |
| `art/characters/arkham-northside-willard-peck.webp` | `arkham-en/character/northside-willard-peck` (Уиллард Пек) | portrait | — | 2023), с. 78 (физ. 79) |
| `art/characters/arkham-northside-minnie-coleman.webp` | `arkham-en/character/northside-minnie-coleman` (Минерва «Минни» Коулман) | portrait | — | 2023), с. 79 (физ. 80) |
| `art/characters/arkham-northside-sam-flinn.webp` | `arkham-en/character/northside-sam-flinn` (Сэм Флинн) | portrait | — | 2023), с. 80 (физ. 81) |
| `art/characters/arkham-mikey-catchpole.webp` | `coc:character:mikey-catchpole` (Майки Кэтпол) | portrait | — | 2023), с. 80 (физ. 81) |
| `art/characters/arkham-northside-ruby-simmons.webp` | `arkham-en/character/northside-ruby-simmons` (Руби Симмонс) | portrait | — | 2023), с. 81 (физ. 82) |
| `art/characters/arkham-northside-larry-freen.webp` | `arkham-en/character/northside-larry-freen` (Ларри «Сент-Луи» Фрин) | portrait | — | 2023), с. 81 (физ. 82) |
| `art/characters/arkham-northside-jin-lillibridge.webp` | `arkham-en/character/northside-jin-lillibridge` (Джин Лиллибридж) | portrait | — | 2023), с. 83 (физ. 84) |
| `art/characters/arkham-northside-edwin-cassidy.webp` | `arkham-en/character/northside-edwin-cassidy` (Эдвин Кэссиди) | portrait | — | 2023), с. 84 (физ. 85) |
| `art/characters/arkham-northside-edward-tillinghast.webp` | `arkham-en/character/northside-edward-tillinghast` (Эдвард Тиллингаст) | portrait | — | 2023), с. 88 (физ. 89) |
| `art/characters/arkham-northside-alice-ballard.webp` | `arkham-en/character/northside-alice-ballard` (Элис Баллард) | portrait | — | 2023), с. 88 (физ. 89) |
| `art/characters/arkham-northside-alex-hearne.webp` | `arkham-en/character/northside-alex-hearne` (Алекс Хёрн) | portrait | — | 2023), с. 90 (физ. 91) |
| `art/characters/arkham-northside-roberta-henry.webp` | `arkham-en/character/northside-roberta-henry` (Роберта Генри) | portrait | — | 2023), с. 91 (физ. 92) |
| `art/characters/arkham-northside-marvin-dunlap.webp` | `arkham-en/character/northside-marvin-dunlap` (Марвин Данлэп) | portrait | — | 2023), с. 92 (физ. 93) |
| `art/characters/arkham-greasy-spoon.webp` | `coc:character:greasy-spoon` (Сальный Спун) | portrait | — | 2023), с. 94 (физ. 95) |
| `art/characters/arkham-downtown-heinrich-muelhig.webp` | `arkham-en/character/downtown-heinrich-muelhig` (Хайнрих Т. Мюлиг) | portrait | — | 2023), с. 97 (физ. 98) |
| `art/characters/arkham-downtown-kenneth-heath.webp` | `arkham-en/character/downtown-kenneth-heath` (Кеннет Хит) | portrait | — | 2023), с. 100 (физ. 101) |
| `art/characters/arkham-downtown-keezar-randall.webp` | `arkham-en/character/downtown-keezar-randall` (Кизар Рэндалл) | portrait | Судья Кизар Рэндалл | 2023), с. 102 (физ. 103) |
| `art/characters/arkham-downtown-ellen-whitmarsh.webp` | `arkham-en/character/downtown-ellen-whitmarsh` (Эллен Уитмарш) | portrait | Эллен Уитмарш | 2023), с. 102 (физ. 103) |
| `art/characters/arkham-downtown-joseph-peabody.webp` | `arkham-en/character/downtown-joseph-peabody` (Джозеф Пибоди) | portrait | Мэр Пибоди | 2023), с. 104 (физ. 105) |
| `art/characters/arkham-asa-nichols.webp` | `coc:character:asa-nichols` (Эйса Николс) | portrait | Начальник полиции Николс | 2023), с. 107 (физ. 108) |
| `art/characters/arkham-luther-harden.webp` | `coc:character:luther-harden` (Лютер Харден) | portrait | — | 2023), с. 108 (физ. 109) |
| `art/characters/arkham-downtown-mickey-harrigan.webp` | `arkham-en/character/downtown-mickey-harrigan` (Микки Харриган) | portrait | — | 2023), с. 108 (физ. 109) |
| `art/characters/arkham-downtown-calvin-stuckey.webp` | `arkham-en/character/downtown-calvin-stuckey` (Кэлвин Стаки) | portrait | — | 2023), с. 108 (физ. 109) |
| `art/characters/arkham-downtown-jin-pin-liou.webp` | `arkham-en/character/downtown-jin-pin-liou` (Джин-Пин Лиу) | portrait | — | 2023), с. 112 (физ. 113) |
| `art/characters/arkham-easttown-ellen-crawford.webp` | `arkham-en/character/easttown-ellen-crawford` (Эллен Кроуфорд) | portrait | — | 2023), с. 116 (физ. 117) |
| `art/characters/arkham-easttown-beatrice-allen.webp` | `arkham-en/character/easttown-beatrice-allen` (Беатрис Аллен) | portrait | — | 2023), с. 116 (физ. 117) |
| `art/characters/arkham-easttown-melissa-thorne.webp` | `arkham-en/character/easttown-melissa-thorne` (Мелисса Торн) | portrait | — | 2023), с. 117 (физ. 118) |
| `art/characters/arkham-merchant-goody-fowler.webp` | `arkham-en/character/merchant-goody-fowler` (Гуди Фаулер) | portrait | — | 2023), с. 123 (физ. 124) |
| `art/characters/arkham-merchant-elijah-potts.webp` | `arkham-en/character/merchant-elijah-potts` (Элайджа Поттс) | portrait | — | 2023), с. 125 (физ. 126) |
| `art/characters/arkham-danny-obannion.webp` | `coc:character:danny-obannion` (Дэнни О’Баннион) | portrait | — | 2023), с. 129 (физ. 130) |
| `art/characters/arkham-merchant-bobby-sills.webp` | `arkham-en/character/merchant-bobby-sills` (Бобби Силлс) | portrait | — | 2023), с. 129 (физ. 130) |
| `art/characters/arkham-merchant-eddie-leery.webp` | `arkham-en/character/merchant-eddie-leery` (Эдди Лири) | portrait | — | 2023), с. 129 (физ. 130) |
| `art/characters/arkham-merchant-timothy-walters.webp` | `arkham-en/character/merchant-timothy-walters` (Тимоти Уолтерс) | portrait | Тимоти Уолтерс | 2023), с. 134 (физ. 135) |
| `art/characters/arkham-merchant-ewan-waite.webp` | `arkham-en/character/merchant-ewan-waite` (Юэн Уэйт) | portrait | Юэн Уэйт | 2023), с. 135 (физ. 136) |
| `art/characters/arkham-merchant-jenny-aberstrom.webp` | `arkham-en/character/merchant-jenny-aberstrom` (Дженни Аберстром) | portrait | Дженни Аберстром | 2023), с. 137 (физ. 138) |
| `art/characters/arkham-merchant-caleb-markham.webp` | `arkham-en/character/merchant-caleb-markham` (Калеб Маркхэм) | portrait | Калеб Маркхэм | 2023), с. 146 (физ. 147) |
| `art/characters/arkham-rivertown-bert-arley.webp` | `arkham-en/character/rivertown-bert-arley` (Берт Арли) | portrait | Берт Арли | 2023), с. 149 (физ. 150) |
| `art/characters/arkham-rivertown-greg-the-monster.webp` | `arkham-en/character/rivertown-greg-the-monster` (Грег Чудище) | portrait | — | 2023), с. 151 (физ. 152) |
| `art/characters/arkham-rivertown-hiram-the-junkman.webp` | `arkham-en/character/rivertown-hiram-the-junkman` (Хайрем) | portrait | Старьёвщик Хайрем | 2023), с. 155 (физ. 156) |
| `art/characters/arkham-campus-nathaniel-wingate-peaslee.webp` | `arkham-en/character/campus-nathaniel-wingate-peaslee` (Натаниэль Уингейт Пизли) | portrait | Натаниэль Уингейт Пизли | 2023), с. 165 (физ. 166) |
| `art/characters/arkham-campus-wingate-peaslee.webp` | `arkham-en/character/campus-wingate-peaslee` (Уингейт Пизли) | portrait | — | 2023), с. 166 (физ. 167) |
| `art/characters/arkham-william-dyer.webp` | `coc:character:william-dyer` (Уильям Дайер) | portrait | Доктор Дайер | 2023), с. 167 (физ. 168) |
| `art/characters/arkham-campus-donald-atwood.webp` | `arkham-en/character/campus-donald-atwood` (Дональд Этвуд) | portrait | Профессор Дональд Этвуд | 2023), с. 168 (физ. 169) |
| `art/characters/arkham-campus-cecil-waldron.webp` | `arkham-en/character/campus-cecil-waldron` (Сесил «Док» Уолдрон) | portrait | Док Уолдрон | 2023), с. 168 (физ. 169) |
| `art/characters/arkham-campus-albert-wilmarth.webp` | `arkham-en/character/campus-albert-wilmarth` (Альберт Н. Уилмарт) | portrait | — | 2023), с. 169 (физ. 170) |
| `art/characters/arkham-campus-jabir-shariq.webp` | `arkham-en/character/campus-jabir-shariq` (Джабир Шарик) | portrait | — | 2023), с. 170 (физ. 171) |
| `art/characters/arkham-francis-morgan.webp` | `coc:character:francis-morgan` (Фрэнсис Морган) | portrait | — | 2023), с. 171 (физ. 172) |
| `art/characters/arkham-henry-armitage.webp` | `coc:character:henry-armitage` (Генри Армитедж) | portrait | — | 2023), с. 176 (физ. 177) |
| `art/characters/arkham-chester-armwright.webp` | `coc:character:chester-armwright` (Честер Армрайт) | portrait | — | 2023), с. 181 (физ. 182) |
| `art/characters/arkham-campus-marinus-bricknell.webp` | `arkham-en/character/campus-marinus-bricknell` (Маринус Брикнелл) | portrait | Маринус Брикнелл | 2023), с. 187 (физ. 188) |
| `art/characters/arkham-campus-ruth-ellen-whitby.webp` | `arkham-en/character/campus-ruth-ellen-whitby` (Рут Эллен Уитби) | portrait | Рут Эллен Уитби | 2023), с. 187 (физ. 188) |
| `art/characters/arkham-campus-sexton-parkin.webp` | `arkham-en/character/campus-sexton-parkin` (Секстон Паркин) | portrait | Секстон Паркин | 2023), с. 190 (физ. 191) |
| `art/characters/arkham-frenchhill-jurgen-mehler.webp` | `arkham-en/character/frenchhill-jurgen-mehler` (Юрген Мелер) | portrait | Юрген Мелер | 2023), с. 194 (физ. 195) |
| `art/characters/arkham-frenchhill-elisha-couzon.webp` | `arkham-en/character/frenchhill-elisha-couzon` (Элиша Кузон) | portrait | — | 2023), с. 196 (физ. 197) |
| `art/characters/arkham-frenchhill-mordecai-oleary.webp` | `arkham-en/character/frenchhill-mordecai-oleary` (Мордехай О’Лири) | portrait | — | 2023), с. 197 (физ. 198) |
| `art/characters/arkham-frenchhill-walter-gilman.webp` | `arkham-en/character/frenchhill-walter-gilman` (Уолтер Гилмен) | portrait | — | 2023), с. 200 (физ. 201) |
| `art/characters/arkham-keziah-mason.webp` | `coc:character:keziah-mason` (Кеция Мейсон) | portrait | — | 2023), с. 202 (физ. 203) |
| `art/characters/arkham-uptown-gisele-helcimer.webp` | `arkham-en/character/uptown-gisele-helcimer` (Жизель Хельцимер) | portrait | — | 2023), с. 206 (физ. 207) |
| `art/characters/arkham-uptown-stewart-portman.webp` | `arkham-en/character/uptown-stewart-portman` (Стюарт Портман) | portrait | — | 2023), с. 209 (физ. 210) |
| `art/characters/arkham-edward-pickman-derby.webp` | `coc:character:edward-pickman-derby` (Эдвард Пикман Дерби) | portrait | — | 2023), с. 212 (физ. 213) |
| `art/characters/arkham-uptown-jonathan-shear.webp` | `arkham-en/character/uptown-jonathan-shear` (Джонатан Шир) | portrait | — | 2023), с. 212 (физ. 213) |
| `art/characters/arkham-southside-diane-lapham-peabody.webp` | `arkham-en/character/southside-diane-lapham-peabody` (Дайан Лапхэм-Пибоди) | portrait | — | 2023), с. 216 (физ. 217) |
| `art/characters/arkham-marge-hockler.webp` | `coc:character:marge-hockler` (Мардж Хоклер) | portrait | Мардж Хоклер | 2023), с. 217 (физ. 218) |
| `art/characters/arkham-southside-jaspar-eleazar.webp` | `arkham-en/character/southside-jaspar-eleazar` (Джаспер Элеазар) | portrait | Джаспер Элеазар | 2023), с. 218 (физ. 219) |
| `art/characters/arkham-southside-jason-gaspard.webp` | `arkham-en/character/southside-jason-gaspard` (Джейсон Гаспард) | portrait | — | 2023), с. 221 (физ. 222) |
| `art/characters/arkham-southside-madame-dulagi.webp` | `arkham-en/character/southside-madame-dulagi` (Мадам Дулаги) | portrait | — | 2023), с. 221 (физ. 222) |
| `art/characters/arkham-joe-potrello.webp` | `coc:character:joe-potrello` (Джузеппе «Джо» Портелло) | portrait | — | 2023), с. 223 (физ. 224) |
| `art/characters/arkham-southside-hagan-wilson.webp` | `arkham-en/character/southside-hagan-wilson` (Хаган Уилсон) | portrait | — | 2023), с. 224 (физ. 225) |
| `art/characters/arkham-lexy-romano.webp` | `coc:character:lexy-romano` (Лекси Романо) | portrait | Лекси Романо | 2023), с. 227 (физ. 228) |
| `art/characters/arkham-outskirts-ammi-pierce.webp` | `arkham-en/character/outskirts-ammi-pierce` (Эмми Пирс) | portrait | — | 2023), с. 235 (физ. 236) |
| `art/characters/arkham-asenath-waite.webp` | `coc:character:asenath-waite` (Асенат Уэйт) | portrait | — | 2023), с. 240 (физ. 241) |
| `art/characters/arkham-outskirts-bessie-heingrapper.webp` | `arkham-en/character/outskirts-bessie-heingrapper` (Бесси Хейнгрэппер) | portrait | Бесси Хейнгреппер | 2023), с. 243 (физ. 244) |
| `art/characters/arkham-outskirts-florence-harrington.webp` | `arkham-en/character/outskirts-florence-harrington` (Флоренс Харрингтон) | portrait | — | 2023), с. 244 (физ. 245) |

## Иллюстрации, реклама, существа, предметы (63)

| Файл (`app/…`) | Запись | Вид | Подпись | Страница |
|---|---|---|---|---|
| `art/locations/arkham-arkham.webp` | `coc:location:arkham` (Аркхэм) | illustration | Народы мискатов до XVII века | 2023), с. 13 (физ. 14) |
| `art/locations/arkham-arkham-2.webp` | `coc:location:arkham` (Аркхэм) | illustration | Салемские процессы над ведьмами | 2023), с. 14 (физ. 15) |
| `art/locations/arkham-arkham-3.webp` | `coc:location:arkham` (Аркхэм) | illustration | Странный метеорит | 2023), с. 15 (физ. 16) |
| `art/rules/arkham-arkham-law-and-order.webp` | `coc:rule:arkham-law-and-order` (Закон и порядок в Аркхэме) | illustration | Бандитская расправа | 2023), с. 19 (физ. 20) |
| `art/rules/arkham-arkham-skills.webp` | `coc:rule:arkham-skills` (Навыки Аркхэма) | illustration | Как пройти?.. | 2023), с. 27 (физ. 28) |
| `art/rules/arkham-arkham-improving-skills.webp` | `coc:rule:arkham-improving-skills` (Развитие навыков сыщика в Аркхэме) | illustration | Развитие навыков | 2023), с. 29 (физ. 30) |
| `art/rules/arkham-arkham-clubs-and-societies.webp` | `coc:rule:arkham-clubs-and-societies` (Клубы, общества и организации сыщиков Аркхэма) | illustration | Встреча умов | 2023), с. 33 (физ. 34) |
| `art/rules/arkham-arkham-experts.webp` | `coc:rule:arkham-experts` (Знатоки и помощь в Аркхэме) | illustration | Помощь может понадобиться в любой час | 2023), с. 41 (физ. 42) |
| `art/rules/arkham-arkham-rumors.webp` | `coc:rule:arkham-rumors` (Слухи и сплетни Аркхэма) | illustration | Слухи и сплетни | 2023), с. 44 (физ. 45) |
| `art/organizations/arkham-overview-arkham-coven.webp` | `arkham-en/organization/overview-arkham-coven` (Аркхэмский ковен) | illustration | Аркхэмский ковен | 2023), с. 50 (физ. 51) |
| `art/locations/arkham-arkham-113-the-speakeasy.webp` | `coc:location:arkham-113-the-speakeasy` («Забегаловка») | illustration | «Забегаловка» | 2023), с. 81 (физ. 82) |
| `art/handouts/arkham-northside-gleasons-dress-sale-ad.webp` | `arkham-en/handout/northside-gleasons-dress-sale-ad` (Реклама распродажи платьев у Глисона) | handout | — | 2023), с. 82 (физ. 83) |
| `art/items/arkham-northside-beacher-marvels.webp` | `arkham-en/item/northside-beacher-marvels` («Чудеса» Боба Бичера) | illustration | — | 2023), с. 83 (физ. 84) |
| `art/locations/arkham-arkham-122-jj-abbott-taxidermist.webp` | `coc:location:arkham-122-jj-abbott-taxidermist` (Таксидермист Дж. Дж. Эбботт) | illustration | Мастерская таксидермиста | 2023), с. 86 (физ. 87) |
| `art/handouts/arkham-northside-stigleitz-ad.webp` | `arkham-en/handout/northside-stigleitz-ad` (Реклама «Штиглайц и сын») | handout | — | 2023), с. 94 (физ. 95) |
| `art/locations/arkham-arkham-231-first-national-grocery.webp` | `coc:location:arkham-231-first-national-grocery` (Магазин «Первая национальная бакалея») | illustration | Магазин «Первая национальная бакалея» | 2023), с. 110 (физ. 111) |
| `art/locations/arkham-arkham-237-bundens-bindery.webp` | `coc:location:arkham-237-bundens-bindery` (Переплётная мастерская Бандена) | illustration | Особые переплёты для особых книг | 2023), с. 112 (физ. 113) |
| `art/locations/arkham-arkham-412-lucky-clover-cartage.webp` | `coc:location:arkham-412-lucky-clover-cartage` (Извозная компания «Лаки Кловер») | handout | Реклама «Лаки Кловер» | 2023), с. 117 (физ. 118) |
| `art/locations/arkham-arkham-412-lucky-clover-cartage-2.webp` | `coc:location:arkham-412-lucky-clover-cartage` (Извозная компания «Лаки Кловер») | illustration | Эмблема «Лаки Кловер» | 2023), с. 128 (физ. 129) |
| `art/locations/arkham-arkham-311-ice-house.webp` | `coc:location:arkham-311-ice-house` (Ледник) | illustration | — | 2023), с. 118 (физ. 119) |
| `art/locations/arkham-arkham-402-old-wooded-graveyard.webp` | `coc:location:arkham-402-old-wooded-graveyard` (Старое лесное кладбище) | illustration | Старое лесное кладбище | 2023), с. 122 (физ. 123) |
| `art/organizations/arkham-obannion-organization.webp` | `coc:organization:obannion-organization` (Организация Дэнни О’Банниона) | illustration | Организация Дэнни О’Банниона | 2023), с. 128 (физ. 129) |
| `art/creatures/arkham-merchant-unnamable-monster.webp` | `arkham-en/creature/merchant-unnamable-monster` (Неименуемое чудовище) | art | — | 2023), с. 124 (физ. 125) |
| `art/creatures/arkham-merchant-arkham-creeper.webp` | `arkham-en/creature/merchant-arkham-creeper` (Аркхэмский ползун) | art | Аркхэмские ползуны | 2023), с. 145 (физ. 146) |
| `art/locations/arkham-arkham-138-sanders-wax-museum.webp` | `coc:location:arkham-138-sanders-wax-museum` (Музей восковых фигур Сандера) | handout | Реклама музея восковых фигур Сандера | 2023), с. 149 (физ. 150) |
| `art/organizations/arkham-merchant-arkham-gun-club.webp` | `arkham-en/organization/merchant-arkham-gun-club` (Аркхэмский оружейный клуб) | handout | Реклама Аркхэмского оружейного клуба | 2023), с. 152 (физ. 153) |
| `art/organizations/arkham-southside-eye-of-amara.webp` | `arkham-en/organization/southside-eye-of-amara` (Общество «Око Амары») | handout | Объявление о лекции общества «Око Амары» | 2023), с. 152 (физ. 153) |
| `art/locations/arkham-arkham-608-whitechapel-mortuary.webp` | `coc:location:arkham-608-whitechapel-mortuary` (Похоронное бюро Уайтчепела) | handout | Реклама похоронного бюро Уайтчепела | 2023), с. 154 (физ. 155) |
| `art/locations/arkham-arkham-514-g-schmidt-glazier.webp` | `coc:location:arkham-514-g-schmidt-glazier` (Стекольная мастерская Г. Шмидта) | illustration | Необычные стеклянные изделия Шмидта | 2023), с. 155 (физ. 156) |
| `art/locations/arkham-miskatonic-university.webp` | `coc:location:miskatonic-university` (Мискатоникский университет) | illustration | Герб Мискатоникского университета | 2023), с. 159 (физ. 160) |
| `art/organizations/arkham-campus-marching-miskies.webp` | `arkham-en/organization/campus-marching-miskies` («Марширующие Миски») | illustration | «Марширующие Миски» | 2023), с. 164 (физ. 165) |
| `art/locations/arkham-arkham-620-east-dormitory.webp` | `coc:location:arkham-620-east-dormitory` (Восточное общежитие) | illustration | Восточное общежитие | 2023), с. 172 (физ. 173) |
| `art/locations/arkham-arkham-616-statue-lawn.webp` | `coc:location:arkham-616-statue-lawn` (Лужайка со статуей) | illustration | Лужайка со статуей | 2023), с. 173 (физ. 174) |
| `art/locations/arkham-orne-library.webp` | `coc:location:orne-library` (Библиотека Орна) | illustration | Библиотека Мискатоника | 2023), с. 175 (физ. 176) |
| `art/locations/arkham-arkham-627-university-exhibit-museum.webp` | `coc:location:arkham-627-university-exhibit-museum` (Музей Мискатоникского университета) | illustration | Музей Мискатоникского университета | 2023), с. 185 (физ. 186) |
| `art/locations/arkham-arkham-707-bayfriars-church.webp` | `coc:location:arkham-707-bayfriars-church` (Церковь Бейфрайарс) | illustration | Церковь Бейфрайарс | 2023), с. 195 (физ. 196) |
| `art/characters/arkham-frenchhill-typical-rock-boy.webp` | `arkham-en/character/frenchhill-typical-rock-boy` (Типичный парень из «Камней») | illustration | — | 2023), с. 198 (физ. 199) |
| `art/organizations/arkham-temple-of-hope.webp` | `coc:organization:temple-of-hope` (Храм надежды) | illustration | Молитвенное собрание в Храме надежды | 2023), с. 199 (физ. 200) |
| `art/creatures/arkham-brown-jenkin.webp` | `coc:creature:brown-jenkin` (Бурый Дженкин) | art | — | 2023), с. 203 (физ. 204) |
| `art/locations/arkham-arkham-122-jj-abbott-taxidermist-2.webp` | `coc:location:arkham-122-jj-abbott-taxidermist` (Таксидермист Дж. Дж. Эбботт) | handout | Реклама таксидермиста Дж. Дж. Эбботта | 2023), с. 204 (физ. 205) |
| `art/locations/arkham-arkham-638-nook-ends.webp` | `coc:location:arkham-638-nook-ends` (Книжная лавка «Нук-Эндс») | handout | Реклама книжной лавки «Нук-Эндс» | 2023), с. 204 (физ. 205) |
| `art/items/arkham-southside-historical-society-newspapers.webp` | `arkham-en/item/southside-historical-society-newspapers` (Забытые подшивки аркхэмских газет) | illustration | — | 2023), с. 214 (физ. 215) |
| `art/organizations/arkham-southside-eye-of-amara-2.webp` | `arkham-en/organization/southside-eye-of-amara` (Общество «Око Амары») | illustration | Общество «Око Амары» | 2023), с. 219 (физ. 220) |
| `art/organizations/arkham-southside-river-town-five.webp` | `arkham-en/organization/southside-river-town-five` («Ривер-Таун Файв») | illustration | «Ривер-Таун Файв» | 2023), с. 222 (физ. 223) |
| `art/locations/arkham-arkham-214-arkham-first-bank.webp` | `coc:location:arkham-214-arkham-first-bank` (Первый банк Аркхэма) | handout | Реклама Первого банка Аркхэма | 2023), с. 223 (физ. 224) |
| `art/locations/arkham-arkham-231-first-national-grocery-2.webp` | `coc:location:arkham-231-first-national-grocery` (Магазин «Первая национальная бакалея») | handout | Реклама магазинов First National | 2023), с. 223 (физ. 224) |
| `art/locations/arkham-arkham-703-b-college-barbershop.webp` | `coc:location:arkham-703-b-college-barbershop` (Парикмахерская «Колледж») | handout | Реклама парикмахерской «Колледж» | 2023), с. 225 (физ. 226) |
| `art/locations/arkham-arkham-720-keenans-laundry.webp` | `coc:location:arkham-720-keenans-laundry` (Прачечная Кинана) | handout | Реклама прачечной Кинана | 2023), с. 225 (физ. 226) |
| `art/locations/arkham-arkham-441-bryants-apothecary.webp` | `coc:location:arkham-441-bryants-apothecary` (Аптека Брайанта) | handout | Реклама аптеки Брайанта | 2023), с. 225 (физ. 226) |
| `art/locations/arkham-arkham-920-sycamores.webp` | `coc:location:arkham-920-sycamores` («У платана») | illustration | «У платана» | 2023), с. 226 (физ. 227) |
| `art/characters/arkham-outskirts-rose-three-dogs.webp` | `arkham-en/character/outskirts-rose-three-dogs` (Роза Три Собаки) | illustration | Роза Три Собаки и Расколотая скала | 2023), с. 232 (физ. 233) |
| `art/locations/arkham-arkham-os112-blasted-heath.webp` | `coc:location:arkham-os112-blasted-heath` (Испепелённая пустошь) | illustration | Испепелённая пустошь | 2023), с. 236 (физ. 237) |
| `art/locations/arkham-arkham-902-gordon-psychiatric-home.webp` | `coc:location:arkham-902-gordon-psychiatric-home` (Психиатрическая лечебница Гордона) | handout | Реклама психиатрической лечебницы Гордона | 2023), с. 241 (физ. 242) |
| `art/locations/arkham-arkham-os117-goody-fowler-cottage.webp` | `coc:location:arkham-os117-goody-fowler-cottage` (Дом Гуди Фаулер) | illustration | Дом Гуди Фаулер | 2023), с. 242 (физ. 243) |
| `art/locations/arkham-arkham-136-tilden-arms-hotel.webp` | `coc:location:arkham-136-tilden-arms-hotel` (Отель «Тилден-Армс») | handout | Реклама отеля «Тилден-Армс» | 2023), с. 243 (физ. 244) |
| `art/locations/arkham-arkham-704-mehlers-funeral-parlor.webp` | `coc:location:arkham-704-mehlers-funeral-parlor` (Похоронное бюро Мелера) | handout | Реклама похоронного бюро Мелера | 2023), с. 243 (физ. 244) |
| `art/locations/arkham-arkham-634-hotel-miskatonic.webp` | `coc:location:arkham-634-hotel-miskatonic` (Отель «Мискатоник») | handout | Реклама отеля «Мискатоник» | 2023), с. 250 (физ. 251) |
| `art/characters/arkham-generic-police-patrol-officer.webp` | `arkham-en/character/generic-police-patrol-officer` (Патрульный полицейский (типовой персонаж Аркхэма)) | illustration | — | 2023), с. 255 (физ. 256) |
| `art/locations/arkham-arkham-913-antons-restaurant.webp` | `coc:location:arkham-913-antons-restaurant` (Ресторан Антона) | handout | Реклама ресторана Антона | 2023), с. 16 (физ. 17) |
| `art/locations/arkham-arkham-447-jones-hardware.webp` | `coc:location:arkham-447-jones-hardware` (Скобяные товары Б. Ф. Джонса) | handout | Реклама скобяной лавки Б. Ф. Джонса | 2023), с. 21 (физ. 22) |
| `art/characters/arkham-rivertown-typical-finn-boy.webp` | `arkham-en/character/rivertown-typical-finn-boy` (Типичный парень из «Финнов») | illustration | — | 2023), с. 156–157 (физ. 157–158) |
| `art/locations/arkham-arkham-410-docks.webp` | `coc:location:arkham-410-docks` (Причалы) | illustration | — | 2023), с. 127 (физ. 128) |
| `art/characters/arkham-abner-wick.webp` | `coc:character:abner-wick` (Абнер Уик) | illustration | Абнер Уик, «Безделицы» | 2023), с. 139 (физ. 140) |

## Не взято

Портреты без записи в базе — нет: каждый портрет книги (92 овальных портрета; Неименуемое чудовище добавлено как арт существа) нашёл свою запись; второй портрет
Кеции Мейсон (с. 52, физ. 53, глава о ковене) — тот же рисунок, что на с. 202 (физ. 203), не дублировался.

Портреты, названные в отчётах частей, но в книге не найденные: Синдервальд (у его статблока на с. 101 — только полоса
с предметами, портрета нет), Лу Бенито (с. 224 — портреты Потрелло и Хагана Уилсона, своего у Бенито нет).

Иллюстрации без подписи и без своей записи (сюжет не привязан к месту, человеку или правилу):
- титульные развороты глав (физ. 11–12, 25–26, 37–38, 61–62, 247–248), задняя обложка и реклама BRP (физ. 272–274);
- разворот кампуса (физ. 69–70), пара с шампанским (физ. 36), поезд на станции (физ. 60), сыщица с фонарём
  (с. 158, физ. 159), рогатое существо во вратах (с. 245, физ. 246), туннели (физ. 145), человек с молниями
  (физ. 147), щупальца над городом (с. 148, физ. 149), лесная сцена с машиной (физ. 214), поезда (физ. 221–222),
  призрак у «Пикеринга» (физ. 49), упавший человек (физ. 53), человек за столом (физ. 31), гуляющие в парке (физ. 32);
- украшения: фигуры-вырезки (полицейский физ. 19, люди кампуса физ. 69, женщина физ. 223), стопка книг (физ. 76),
  книга с очками (физ. 210), чертежи-круги и полосы с предметами (физ. 35, 71, 80, 101–102, 124, 238, 257),
  дипломы МУ (физ. 189), кофейное пятно (физ. 251);
- повторы того, что уже есть: карты и планы (их листы — в `kb/maps`), газета «Arkham Advertiser» (физ. 41, 157–158 —
  у раздаток `advertiser-1922-*` картинки есть), врезки-таблицы (погода, цены, оружие, слухи) — текст в записях;
- фотографии авторов (физ. 259) — не игровой материал.
