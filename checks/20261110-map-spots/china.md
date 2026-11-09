# Метки карт «Китай» (2026-11-10, Р-206)

Часть «china» конвейера Р-139. Книга `masks-of-nyarlathotep-en`, страницы 519–618; карты — с. 521 (Шанхай), 548, 554,
559, 575, 585. Распознавание `tesseract … tsv` на текстуре карт номеров почти не дало, поэтому кружки найдены
сопоставлением с шаблоном кружка (светлый диск с тёмным ободом) около глазной оценки, каждая метка проверена глазами
по вырезке с нарисованным перекрестьем; подписи (районы, «Secret Door», «UP» и т. п.) — по вырезкам. Названия комнат —
по легендам планов официального русского т. II (скан `masks-of-nyarlathotep-ru-2`, физ. с. 163, 169, 174, 189, 199),
Шанхая — по таблице ключа у города.

## Карты

| Карта | Меток | Номеров в ключе | Новых мест | Не поставлено |
|---|---|---|---|---|
| `china-shanghai` (с. 521) | 38: 1–32; «HONGKEW DISTRICT», «SHANGHAI INTERNATIONAL SETTLEMENT», «FRENCH CONCESSION», «OLD CITY», во врезке «Дальний Восток» — «Gray Dragon Island» (на карту острова), «Hong Kong» | 32 | 18: 1, 3, 4, 6, 9, 12, 13, 15–21, 25, 26, 30, 32 | районы без записей — «ZHABEI DISTRICT», «NANSHI DISTRICT», «POOTUNG DISTRICT»; «THE BUND» (Набережная — псевдоним Международного сеттльмента, своей записи нет); «Whangpoo River»; подписи врезок — «SHANGHAI» (сам город), «Soochow», «Chung Ming», «Keijo», «Taihoku»; масштабы, легенда «Railroad» |
| `china-mr-lung-apartment` (с. 548) | 8: 1–8 | 8 | 8: 1–8 | «Neighboring Building», «Stairwell to other apartments», «Arrows point up Stairs» — ориентиры |
| `china-ho-fang-warehouse` (с. 554) | 14: 1 (четыре раза), 2, 3, 4 (дважды), 5–8, A, B | 8 + точки A, B | 7: 1–7 (8 — существующее «Особое хранилище») | «Top Floor», «Ground Floor», «Dock», пояснения к точкам A и B — ориентиры (точки A и B — метки особого хранилища с `text`) |
| `china-ho-fang-mansion` (с. 559) | 41: 1–20 (8 — трижды, 13 — тринадцать раз, 14 — пять раз), три «X» | 20 | 19: всё, кроме 3 (существующее «Святилище Опухшей дамы») | «Areas marked “X” are open to the air» — пояснение легенды (знаки «X» — метки с `text`: внутренний двор, внешний двор, безымянный дворик среди спален → особняк) |
| `china-mu-hsien-house` (с. 575) | 10: 1–7, «Secret Door» (→ 7), «12-foot Wall» (→ дом), «Pool» (→ 3) | 7 | 7: 1–7 | «Neighboring Building» — ориентир |
| `china-gray-dragon-island` (с. 585) | 20: 1–17, «UP» и «Plan of the Chamber of the Bloated Woman» (→ покой Опухшей дамы), «Gray Dragon Lagoon Details» (→ остров) | 5 + 12 | 11: 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17 | масштабы — ориентиры |

Всего: 131 метка, 70 новых мест. Номера, у которых записи уже были: Шанхай 2, 5, 7, 8, 10, 11, 14, 22, 23, 24, 27, 28,
29, 31; склад 8; особняк 3; остров 1, 2, 10, 12, 14, 16 — `number` у них уже стоял. Размер кружков (`spot_shape`)
пересчитан для каждой картинки (диаметр кружка в пикселях к ширине и высоте).

## Новые места

| Метка | Запись (`masks-of-nyarlathotep-en/location/…`) | Страницы |
|---|---|---|
| Шанхай 1 | `china-hongkew-park` — «Парк Хункоу» | 521 |
| Шанхай 3 | `china-north-railway-station` — «Северный вокзал» | 521 |
| Шанхай 4 | `china-yo-fu-monastery` — «Монастырь Ёфу» | 521 |
| Шанхай 6 | `china-court-house` — «Суд» | 521 |
| Шанхай 9 | `china-general-hospital` — «Центральная больница» | 521 |
| Шанхай 12 | `china-american-consulate` — «Американское консульство» | 521 |
| Шанхай 13 | `china-british-consulate` — «Британское консульство» | 521, 538 |
| Шанхай 15 | `china-sassoon-building` — «Офис «Сассун»» | 521 |
| Шанхай 16 | `china-shanghai-library` — «Шанхайская библиотека» | 521, 540 |
| Шанхай 17 | `china-ching-an-monastery` — «Монастырь Цинань» | 521 |
| Шанхай 18 | `china-post-office` — «Почта» | 521, 565, 574 |
| Шанхай 19 | `china-palace-hotel` — «Отель «Палас»» | 521 |
| Шанхай 20 | `china-royal-asiatic-society` — «Королевское азиатское общество» | 521 |
| Шанхай 21 | `china-recreation-ground` — «Развлекательный центр» | 521 |
| Шанхай 25 | `china-french-consulate` — «Французское консульство» | 521 |
| Шанхай 26 | `china-heng-shen-hotel` — «Отель «Хэншэн»» | 521 |
| Шанхай 30 | `china-confucius-temple` — «Конфуцианский храм» | 521 |
| Шанхай 32 | `china-south-railway-station` — «Южный железнодорожный вокзал» | 521 |
| Квартира Луна 1–8 | `china-lung-kitchen`, `-bedroom`, `-wc`, `-back-room`, `-brazier`, `-office`, `-living-area`, `-entrance-hall` | 546–550 |
| Склад 1–7 | `china-ho-fang-warehouse-offices`, `china-ho-fang-office`, `china-ho-fang-secretary-office`, `china-ho-fang-warehouse-bathroom`, `china-ho-fang-main-warehouse`, `china-ho-fang-assistant-office`, `china-ho-fang-reception` | 553–556 |
| Особняк 1, 2, 4–20 | `china-ho-fang-potion-room`, `-pavilion`, `-gun-room`, `-inner-court`, `china-ho-tzu-hsi-room`, `china-ho-fang-room`, `-guestrooms`, `china-stanford-room`, `china-ho-fang-library`, `-dining-hall`, `-sitting-room`, `-bedrooms`, `-storerooms`, `-kitchen`, `-servants-dining`, `-garage`, `-outer-court`, `-doorman-room`, `-repair-shop` | 558–560 |
| Дом Му Сяня 1–7 | `china-mu-hsien-study`, `-living-room`, `-courtyard`, `-bedroom`, `-kitchen`, `-servant-room`, `china-jack-brady-room` | 573–577 |
| Остров 3, 4, 5 | `china-gray-dragon-underwater-entry`, `china-gray-dragon-dock`, `china-gray-dragon-land-entry` | 585–589 |
| Покой 6, 7, 8, 9, 11, 13 | `china-parts-and-storage`, `china-magma-pool`, `china-bubbling-pool`, `china-quiet-pool`, `china-the-rocket`, `china-the-statue` | 587–590 |
| Покой 15 | `china-marine-chronometer` — «Морской хронометр (мастерская сэра Обри)», `part_of` — мастерская | 591, 594, 595 |
| Покой 17 | `china-burial-chamber` — «Погребальная камера сэра Обри», `part_of` — египетская комната | 590 |

Изменены записи части: карты (6) — `spots`, `spot_shape`, `quality.notes`, `corrections`; `kb/locations/shanghai.json` —
ссылки 18 строк таблицы «Шанхай: условные обозначения карты» на новые места, пометка о местах без записей убрана,
`corrections`. `kb/locations/hong-kong.json` не менялся (на него только ведёт метка «Hong Kong»).

## Предложения

`proposals-china.json` — 12 предложений (пробный прогон `pipeline/integrate/apply.py --dry-run` ложится целиком):
`found_at` предметов на новые комнаты — навигационная карта острова и бумаги о поставках → кабинет Хо Фана,
шкатулка врат → комната Стэнфорда, «Эссенция добровольной отставки» → кладовые особняка, саркофаг → погребальная
камера, статуя → «Статуя», ракета → «Ракета», сварочный аппарат → склад с деталями, шкатулка демонов → подсобка
Луна; `where` сцен — «Подсобка…» → подсобка, «Встреча с Хо Фаном» → кабинет Хо Фана, «Ложный след: Рангун» →
британское консульство.

## Сомнения и выводы из текста

- Указатель 5 на карте острова («Land Entry») упирается в край кратера конуса, а по тексту наземный вход — пещера
  примерно в 46 м вверх по склону (с. 587); записано в пометках карты и места.
- «Potion Room» (1) и «Gun Room» (4) особняка отнесены к двум нишам тайного коридора за статуей Будды (мастерская
  ядов и тайник с оружием, с. 560); кабинет секретарши (3 склада) — кабинет Сунь Чуньхуа; «Почта» (18) — возможно,
  центральный почтамт (с. 565, 574); «Шанхайская библиотека» (16) — возможно, публичная библиотека сеттльмента
  (с. 540) — всё помечено «вывод из текста (Р-41)».
- Чьи спальни 13 особняка, книга не говорит — в записи так и сказано.
- Морской хронометр (15) по тексту висит на стене мастерской (с. 591), на плане указатель 15 ведёт к её стене;
  `part_of` — мастерская сэра Обри.
- Мелочи оформления (Р-39, не записаны): «EXPLANTION» и «Seaman’s Club» на карте Шанхая.
- Имя Линь в ключе карты (т. II, «Дом Линь Яньюй») и в записи персонажа («Линь Енью») расходится — это записи
  других частей, правка не предлагалась; в тексте новых записей — «Линь Енью» по записи персонажа.

## Заголовки книги

Полная сверка заголовков с. 519–618 сделана при переносе главы: `checks/20261109-masks/china-1.md`, `china-2.md`.
Здесь — заголовки, которые получили новые записи места.

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Ключ карты «The Pearl of the Orient: Shanghai» (1–32) | 521 | `coc:location:shanghai` (таблица) + 18 новых мест |
| Getting Sidetracked (британский консул) | 538 | `china-british-consulate` (и сцена) |
| Newspaper Archives (публичная библиотека) | 540 | `china-shanghai-library` («возможно») |
| The House of Mr. Lung (шесть комнат) | 546 | комнаты квартиры Луна |
| Amulets; Feng Shui; Tiger Scrolls; Brazier of Burning Slippers | 547–548 | `china-lung-entrance-hall`, `china-lung-living-area`, `china-lung-brazier` |
| Mr. Lung’s Apartment (план, легенда 1–8) | 548 | 8 записей комнат |
| The Back Room; Coin Sword | 549 | `china-lung-back-room` |
| The Main Warehouse | 553 | `china-ho-fang-main-warehouse` |
| Ho Fang’s Office | 554 | `china-ho-fang-office` |
| Ho Fang’s Warehouse (план, легенда 1–8, точки A, B) | 554 | 7 записей + `china-ho-fang-special-storeroom` |
| Meeting with Ho Fang (секретарша) | 556 | `china-ho-fang-secretary-office` |
| Rooms Around the Outer Court; The Doorman’s Room; Luxurious Sitting Room; The Dining Room; The Library; Ho’s Bedroom; Carl Stanford’s Room | 558 | комнаты особняка 7, 9–12, 14–20 |
| Ho Fang’s Mansion (план, легенда 1–20) | 559 | 19 записей + святилище |
| The Room of Ho Tzu-Hsi; The Inner Court; The Pavilion | 560 | `china-ho-tzu-hsi-room`, `china-ho-fang-inner-court`, `china-ho-fang-pavilion`, `-potion-room`, `-gun-room` |
| Mu Hsien’s House (план, легенда 1–7) | 575 | 7 записей комнат |
| Gray Dragon Island (карта 1–5, план покоя 6–17) | 585 | 11 новых мест |
| Into the Lagoon (пристань) | 586 | `china-gray-dragon-dock` |
| Deep One Colony; The Trail to the Volcano; To the Heart of the Volcano | 587 | `china-gray-dragon-underwater-entry`, `china-gray-dragon-land-entry` |
| Parts and Storage; The Pools | 589 | `china-parts-and-storage`, `china-bubbling-pool`, `china-quiet-pool` |
| The Statue; The Egyptian Room (погребальная камера) | 590 | `china-the-statue`, `china-burial-chamber` |
| The Chronometer | 594 | `china-marine-chronometer` |

## Не взято

- Районы «ZHABEI DISTRICT», «NANSHI DISTRICT», «POOTUNG DISTRICT» на карте Шанхая: в главе о них только упоминание
  (описание города, с. 526–527), записей нет — меток нет; кандидаты в записи районов, если владелец захочет.
- «THE BUND», «Whangpoo River»: Набережная — псевдоним записи Международного сеттльмента, река записи не имеет;
  метки на подписи не ставились (ориентиры).
- Подписи врезок «Environs of Shanghai» и «Far East» (Shanghai, Soochow, Chung Ming, Keijo, Taihoku), масштабы,
  легенда «Railroad», заголовки карт — ориентиры.
- Подписи-ориентиры планов: «Neighboring Building» (квартира Луна, дом Му), «Stairwell to other apartments»,
  «Arrows point up Stairs», «Top Floor», «Ground Floor», «Dock», пояснения к точкам A и B — без меток.
