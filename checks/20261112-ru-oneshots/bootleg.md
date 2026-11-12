# «Тайник Бутлегеров» (`taynik-butlegerov-ru`) — сверка переноса (часть bootleg)

Источник — фанатский сценарий Александра Ядрихинского («Уголок Хранителя», 2020), в библиотеке владельца с меткой
`[RU 7e]`; PDF 20 страниц, скан без текстового слоя: каждая страница распознана tesseract (`-l rus`, 200 dpi), весь текст и
каждое число сверены по изображениям страниц (статблоки, письмо и газетная заметка — по вырезкам). Правила — 7-я редакция,
`ruleset` core (автор советует сценарий и для пульп-стиля). Действие — август 1927 года, Нью-Йорк; `axes.era` — `1920s`.
Заметки владельца (`3_КБ\Ваншоты\1927 Тайник Бутлегеров\_карточка.md`: «небольшой прибрежный город Новой Англии»,
«сверхъестественная сущность») с книгой не совпадают — записи сделаны по книге.

## Страницы

Смещение: **печатная = физическая − 2** (физ. 3 = с. 1, оглавление … физ. 19 = с. 17). Обложка (физ. 1), титул (физ. 2) и
задняя обложка (физ. 20) без номеров — в `sources` `printed_page: null`. На физ. 13 напечатан колонтитул «9» (по оглавлению
это с. 11), на физ. 14 и 16 номера нет — в записях стоят номера по оглавлению (пометка в `errata` сценария).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Тайник Бутлегеров. Игровой сценарий» | физ. 1 | сценарий `taynik-butlegerov-ru/scenario/taynik-butlegerov` |
| Титул: «Для 2–3 сыщиков и Хранителя», вводный текст, «От автора» | физ. 2 | сценарий: summary, hook |
| Оглавление | 1 | сценарий: sources |
| Предыстория | 2 | сценарий: hook; сцена `…/scene/otel-morskoy-parus` |
| Зловещая истина (врезка «Хранителю на заметку») | 2 | сценарий: keeper_info, advice; `…/character/stiven-uelrayt`, `…/character/lyuter-royal`, `…/character/gerbert-lovett`, `…/character/dzhuzeppe-masseriya`, `…/character/dzhordzh-norton`; `…/organization/lozha-serebryanykh-sumerek`; Карл Сэнфорд — запись «Масок» `masks-of-nyarlathotep-en/character/carl-stanford` (предложение) |
| История святилища | 2–3 | сценарий: keeper_info; `…/location/portovyy-sklad` (history); `…/character/kornelius-stardzh`, `…/character/kornelius-vanderbilt`; `…/item/trost-stardzha` |
| Короли Мёртвой Руки | 3 | `…/organization/koroli-myortvoy-ruki`; сценарий: keeper_info |
| Отель «Морской парус» (Вест-Сайд, 11-я Авеню, 599) | 3 | `…/location/otel-morskoy-parus`; сцена `…/scene/otel-morskoy-parus` |
| Персонал отеля | 4 | `…/character/kevin`, `…/character/albert`, `…/character/gregori`, `…/character/bill-merfi` |
| Ресторан; врезка «Хранителю на заметку» | 4 | `…/location/otel-restoran`; сцена `…/scene/restoran`; раздатка `…/handout/instruktsii-salomona` |
| Улица перед отелем | 4 | сцена `…/scene/ulitsa-pered-otelem` |
| Портовые склады (44-я Вест-Стрит, 645) | 4 | `…/location/portovyy-sklad`, `…/location/portovyy-rayon-vest-sayda`; сцена `…/scene/podkhod-k-skladu` |
| Ранний визит | 4 | сцена `…/scene/ranniy-vizit` |
| Дорога к отелю (1) | 4 | `…/location/sklad-1-doroga-k-otelyu` |
| Южный переулок (2) | 4 | `…/location/sklad-2-yuzhnyy-pereulok` |
| Бочка (3) | 5 | `…/location/sklad-3-bochka` |
| Ящики (4) | 5 | `…/location/sklad-4-yashchiki` |
| Лужи (5) | 5 | `…/location/sklad-5-luzhi` |
| Задний двор (6) | 5–6 | `…/location/sklad-6-zadniy-dvor`; сцена `…/scene/zadniy-dvor` |
| Карта склада (номера 1–13) | 5 | карта `…/map/sklad-12` (`app/maps/bootleg-sklad-12.jpg`, 13 меток → 13 мест `…/location/sklad-1-…` … `sklad-13-fasad`) |
| Столкновение | 6 | сцена `…/scene/zadniy-dvor` |
| Смерти противников | 6 | сценарий: advice; сцена `…/scene/zadniy-dvor` (mechanics) |
| Подвал, Тайник Бутлегеров (7) | 6 | `…/location/sklad-7-podval`; сцена `…/scene/podval-i-trup` |
| Разъярённый подросток | 6 | сцена `…/scene/razyaryonnyy-podrostok`; `…/character/vitale-mankuzo` |
| Труп мафиози (8) | 6 | `…/location/sklad-8-trup-mafiozi`; сцена `…/scene/podval-i-trup`; `…/character/fernando-pappeto` |
| Потайная дверь (9) | 6 | `…/location/sklad-9-potaynaya-dver`; сцена `…/scene/potaynaya-dver` |
| Святилище (10) | 6–7 | `…/location/sklad-10-svyatilishche`; сцена `…/scene/svyatilishche` |
| Символы на полу | 7 | `…/location/sklad-10-svyatilishche`; сцена `…/scene/svyatilishche` |
| Алтарь | 7 | `…/location/sklad-10-svyatilishche`; сцена `…/scene/svyatilishche` |
| Трусливый профессор | 7 | сцена `…/scene/truslivyy-professor`; `…/character/gerbert-lovett` |
| Полиция (11) | 7 | `…/location/sklad-11-politsiya`; сцена `…/scene/politsiya-i-pogonya` |
| Останки Герберта | 7 | сцена `…/scene/ostanki-gerberta`; `…/item/bumazhnik-gerberta`; раздатки `…/handout/material-bumazhnik`, `…/handout/material-amulet` |
| Амулет Мёртвой руки | 8 | `…/item/amulet-myortvoy-ruki` |
| Трость с набалдашником в форме волчьей пасти | 8 | `…/item/trost-stardzha` |
| Врезка «Заклятье: Иссушение Мёртвой Руки» | 8 | `…/item/amulet-myortvoy-ruki` (mechanics); черновик заклинания — в отчёте (kb/spells общий) |
| Череп | 8 | `…/location/sklad-10-svyatilishche`; сцена `…/scene/svyatilishche` |
| Блокнот | 8–9 | `…/item/bloknot-stardzha` |
| Бумажник Герберта | 9 | `…/item/bumazhnik-gerberta` |
| Западный Переулок (12) | 9 | `…/location/sklad-12-zapadnyy-pereulok` |
| Западная Улица, фасад склада (13) | 9 | `…/location/sklad-13-fasad` |
| Погоня (см. правила погонь) | 9 | сцена `…/scene/politsiya-i-pogonya` |
| Патрульный автомобиль | 10 | сцена `…/scene/patrulnyy-avtomobil`; `…/character/itan-uolker`, `…/character/salvatore-marantsano` |
| Раненые сыщики | 10 | сцена `…/scene/patrulnyy-avtomobil`; `…/location/klinika-maunt-sinay` |
| Возвращение в отель | 10 | сцена `…/scene/vozvrashchenie-v-otel` |
| Продолжение расследования | 10 | сцена `…/scene/vozvrashchenie-v-portovyy-rayon`; сценарий: steps |
| Возвращение в портовый район | 10 | сцена `…/scene/vozvrashchenie-v-portovyy-rayon` |
| Антикварная лавка Дэвида Блейка | 10–11 | `…/location/antikvarnaya-lavka-bleyka`; сцена `…/scene/antikvarnaya-lavka`; `…/character/devid-bleyk`, `…/character/uilyam-stoun` |
| Символы позади | 11 | сцена `…/scene/antikvarnaya-lavka` |
| Зарисовка в блокноте | 11 | сцена `…/scene/antikvarnaya-lavka`; `…/item/bloknot-stardzha` |
| Трость Страджа | 11 | сцена `…/scene/antikvarnaya-lavka`; `…/item/trost-stardzha` |
| Градостроительное Бюро, городская ратуша (Бродвей, 260) | 11 | `…/location/gradostroitelnoe-byuro`; сцена `…/scene/gradostroitelnoe-byuro` |
| Нью-Йоркская Публичная Библиотека | 11 | общее место `coc:location:new-york-public-library` (абзац — предложение); сцена `…/scene/publichnaya-biblioteka` |
| Упоминания страшных заклятий | 11 | сцена `…/scene/publichnaya-biblioteka` (список как напечатан) |
| Смерть бродяги | 12 | сцена `…/scene/publichnaya-biblioteka`; `…/character/kornelius-stardzh` |
| Фотография с тростью | 12 | сцена `…/scene/publichnaya-biblioteka`; раздатка `…/handout/material-gazeta` |
| Некрологи | 12 | сцена `…/scene/publichnaya-biblioteka`; `…/character/kornelius-stardzh`, `…/character/kornelius-vanderbilt` |
| Происхождение Страджа | 12 | сцена `…/scene/publichnaya-biblioteka`; `…/character/kornelius-stardzh` |
| Полицейский участок (№ 22, Вест-Сайд, 47-я Вест Стрит, 347); врезка «Хранителю на заметку» | 12 | `…/location/politseyskiy-uchastok-22`; сцена `…/scene/politseyskiy-uchastok` |
| Расследование убийства в порту | 12 | сцена `…/scene/politseyskiy-uchastok`; раздатка `…/handout/protokoly` |
| Написание письма и получение награды | 12 | сцена `…/scene/napisanie-pisma-i-final` |
| Похищение амулета | 13 | сцена `…/scene/pokhishchenie-amuleta`; `…/character/dzhordzh-norton` |
| План «Отель, 2 этаж» (номер сыщика, крыша, окно) | 13 | карта `…/map/otel-vtoroy-etazh` (`app/maps/bootleg-otel-2-etazh.jpg`, 3 метки); `…/location/otel-vtoroy-etazh`; раздатка `…/handout/otel-2-etazh` |
| Расследование в отеле | 13 | сцена `…/scene/pokhishchenie-amuleta` |
| Арест: Взятка; Успешная ложь; Суд | 13 | сцена `…/scene/arest` (errata — оборванная фраза) |
| Финал | 14 | сцена `…/scene/napisanie-pisma-i-final`; сценарий: conclusion |
| Ответное письмо (и текст письма) | 14 | сцена `…/scene/napisanie-pisma-i-final`; раздатка `…/handout/otvetnoe-pismo` (текст как напечатан) |
| Позитивные эффекты | 14–15 | сценарий: conclusion (по пунктам, как напечатано) |
| Негативные эффекты | 15 | сценарий: conclusion |
| Газетная заметка «Местные сводки» | 15 | раздатка `…/handout/mestnye-svodki` (текст как напечатан); `…/character/sofi-pappeto`, `…/character/mariya-bellomo` |
| Закрытые отделы библиотек | 15 | сцена `…/scene/zakrytye-otdely-bibliotek`; `…/organization/koroli-myortvoy-ruki` |
| Завязки | 15 | сценарий: conclusion; `…/character/uilyam-stoun` |
| Заклятья: Пепельная печать | 16 | `…/location/sklad-9-potaynaya-dver`; сцены `…/scene/potaynaya-dver`, `…/scene/ranniy-vizit`; черновик заклинания — в отчёте |
| Заклятья: Иссушение Мёртвой Руки («См. Амулет Мёртвой Руки») | 16 | `…/item/amulet-myortvoy-ruki` |
| Персонажи: Эдвард Саломон Рей | 16 | `…/character/stiven-uelrayt` (без статблока) |
| Фернандо Паппето | 16 | `…/character/fernando-pappeto` (без статблока) |
| Майкл Белломо | 16 | `…/character/maykl-bellomo` (статблок) |
| Либорио Манкузо | 16 | `…/character/liborio-mankuzo` (статблок) |
| Витале Манкузо | 16 | `…/character/vitale-mankuzo` (статблок) |
| Герберт Ловетт | 17 | `…/character/gerbert-lovett` (статблок) |
| Итан Уолкер | 17 | `…/character/itan-uolker` (статблок) |
| Джордж Нортон | 17 | `…/character/dzhordzh-norton` (статблок) |
| Задняя обложка | физ. 20 | сценарий: sources |

## Раздаточные материалы, которых нет в книге

Книга упоминает материалы «Инструкции Саломона», «Газета», «Протоколы», «Бумажник», «Амулет», «Отель, 2 этаж», но
печатает только иллюстрации (бумажник, амулет, шапка газеты, план второго этажа). Полные тексты — в отдельном PDF раздаток
автора `1_Библиотека\Сценарии\Тайник Бутлегеров\Раздатка\[RU 7e] РаздаткаТайник Бутлегеров.pdf` (7 страниц: карта для
Хранителя, планы 1-го и 2-го этажа отеля, письмо сыщикам от 3 августа 1927 года, бумажник и амулет, два полицейских рапорта,
полоса «Нью-Йорк таймс» от 16 августа 1873 года). Этот PDF не записан в `pipeline/source/books.json`, поэтому в записях раздаток —
пересказ по тексту сценария (Р-130) с пометкой в `quality.notes`. Из раздаточного PDF взята только картинка карты склада
(ровная и чище, номера совпадают с книгой).

## Не взято

| Что | Страница | Почему |
|---|---|---|
| Благодарности поддержавшим проект, ссылки («Уголок Хранителя», hobbygames), правовая оговорка Chaosium, копирайт | физ. 2 | не игровой материал |
| «Звуковое сопровождение» — QR-код аудиолиста VK | физ. 2 | ссылка на внешний плейлист, текста нет |
| Иллюстрации: фото отеля, меню «Sea Sail Hotel», портрет Герберта Ловетта, фото амулета и бумажника, фото Нью-Йоркской публичной библиотеки, шапка «Нью-Йорк таймс», купюры | 3–14 | картинки в `app/art/` — вне назначенных файлов (Р-165); описаны в записях и раздатках; кандидаты в `images` |
| Тексты материалов «Инструкции Саломона», «Протоколы», «Газета» из отдельного PDF раздаток | — | книга их не печатает, PDF раздаток не записан в списке книг; вопрос ведущему — записать его отдельной книгой |
| План первого этажа отеля (только в PDF раздаток) | — | в книге его нет |
| Компании «Международная торговая морская компания», «Вспомогательная транзитная компания»; «Бюро Запрета»; аукцион городского имущества | 2, 10, 11, 12 | упомянуты без сюжета — текстом в описаниях (Р-30) |
| Мать и сестра Либорио, полицейские без имён | 10, 15 | безымянные упоминания без сюжетной роли |

## Опечатки и сомнения (в `errata`)

- Фамилия колдуна: «Стардж» (с. 2, 11, 12), «Страдж» (с. 3, 11, 12, 14), «Фадже» (с. 11) — запись по первому упоминанию.
- Фамилия антиквара: «Блейк» и «Блэк» (с. 8, 11).
- «10 лет назад» (с. 2–3) — от октября 1909 до августа 1927 года 18 лет.
- Награда: 1000$ на всех в тексте и 500$ в ответном письме (с. 14).
- Ловетт: ПМ 24 при МОЩ 75 (ожидалось 15); навык Убеждение дважды (40% и 50%).
- Белломо: Стрельба 35% и пистолет 50%; Либорио: пистолет 50% и Стрельба 55%.
- «Успешная ложь»: фраза «…Забалтывание, Обаяние или» оборвана (с. 13).
- Колонтитул «9» на физ. 13 (по оглавлению с. 11).

## Предложения

`checks/20261112-ru-oneshots/proposals-bootleg.json` — 17 правок в 6 общих и чужих записях (пробный прогон `apply.py` проходит):
Нью-Йорк (абзац, источник, ссылки), Нью-Йоркская публичная библиотека (абзац, источник, ссылка), Карл Стэнфорд из «Масок»
(псевдоним «Карл Сэнфорд», абзац в legend, источник), ссылки для навигации у библиотеки Орна, Аркхэма и Мискатоникского
университета.
