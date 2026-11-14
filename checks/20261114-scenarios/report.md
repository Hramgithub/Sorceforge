# Целостность сценариев — 2026-11-14

Создано `python tools/scenario_check.py`; база не менялась. Семья сценария — сам сценарий, его сцены, всё, на что они ссылаются, и записи книги со страниц сценария. В скобках — сколько с картинкой.

## Итог по проверкам

| Проверка | Что ищется | Находок |
|---|---|---|
| `plot.missing` | Нет части сюжета (summary / keeper_info / hook / steps / conclusion) | 15 |
| `plot.bad_ref` | Шаг сюжета ссылается на несуществующую запись | 0 |
| `scenes.none` | У сценария нет сцен | 18 |
| `scenes.no_place` | Сцена без места | 60 |
| `scenes.no_people` | Сцена без участников | 368 |
| `scenes.no_outcome` | Сцена без итога (outcome) | 355 |
| `scenes.unreached` | Сцену не называет ни шаг сюжета, ни другая сцена | 0 |
| `people.lost` | Персонаж страниц сценария, которого не называет ни сценарий, ни его сцены | 2 |
| `clues.unused` | Раздатка или предмет страниц сценария, которых не использует ни сцена, ни шаг | 2 |
| `clues.empty` | Раздатка без текста и без картинки | 4 |
| `pages.gap` | Страница сценария с текстом, которую не цитирует ни одна запись | 2 |

## Сценарии

| Сценарий | Книга | Стр. | Сцен | Персонажи | Существа | Раздатка | Предметы | Места | Карты | Стр. без записей | Находок |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Девятнадцатая лунка | `osobnyaki-bezumiya-ru` | 147–176 | 33 | 38 (6) | 5 (3) | 5 (0) | 10 | 41 | 4 | 0 | 43 |
| Сны о Японии | `sny-o-yaponii-ru` | 7–45 | 30 | 30 (8) | 5 (2) | 10 (8) | 16 | 24 | 5 | 0 | 28 |
| Отель «Скайлайн» | `otel-skaylayn-ru` | 4–11 | 22 | 16 (0) | 5 (2) | 9 (0) | 9 | 18 | 4 | 0 | 26 |
| Проклятый идол Манко Капака | `cursed-idol-of-manco-capac-en` | 15–36 | 27 | 28 (18) | 1 (1) | 15 (15) | 12 | 24 | 7 | 0 | 22 |
| Тайник Бутлегеров | `taynik-butlegerov-ru` | 4–18 | 24 | 23 (1) | 1 (1) | 8 (0) | 4 | 30 | 2 | 0 | 22 |
| Сатурнова чаша | `dead-light-en` | 36–58 | 18 | 12 (12) | 3 (2) | 8 (8) | 12 | 23 | 2 | 0 | 21 |
| Карнавал безумия | `karnaval-bezumiya-ru` | 6–90 | 23 | 61 (5) | 6 (5) | 12 (7) | 15 | 38 | 4 | 0 | 21 |
| Ужас в Иннсмуте | `innsmouth-terror-en` | 5–35 | 25 | 23 (17) | 7 (6) | 3 (3) | 12 | 36 | 0 | 0 | 18 |
| Тьма под холмом | `dveri-vo-tmu-ru` | 14–31 | 17 | 18 (10) | 6 (3) | 2 (0) | 7 | 26 | 3 | 0 | 17 |
| Не забывай меня | `ne-zabyvay-menya-ru` | 1–27 | 16 | 26 (1) | 3 (1) | 7 (5) | 10 | 20 | 2 | 0 | 17 |
| Глава 6. Австралия | `masks-of-nyarlathotep-en` | 452–511 | 34 | 38 (1) | 11 (6) | 6 (6) | 14 | 34 | 7 | 0 | 16 |
| Тени Ленинграда | `shadows-of-leningrad-en` | 6–36 | 26 | 22 (2) | 8 (1) | 8 (8) | 24 | 40 | 6 | 0 | 16 |
| И тут явился Жнец | `fears-sharp-little-needles-en` | 87–91 | 11 | 10 (0) | 2 (1) | 0 (0) | 6 | 10 | 0 | 0 | 15 |
| До самых костей | `fears-sharp-little-needles-en` | 58–62 | 13 | 12 (0) | 2 (2) | 0 (0) | 11 | 14 | 2 | 0 | 14 |
| Лечебница | `lechebnitsa-ru` | 4–27 | 19 | 18 (0) | 3 (2) | 11 (0) | 13 | 39 | 3 | 0 | 14 |
| МТС Харьков-37 | `mts-kharkov-37-ru` | 3–58 | 21 | 22 (0) | 4 (2) | 8 (0) | 17 | 35 | 7 | 0 | 14 |
| Аутофагия | `autofagiya-ru` | 6–30 | 20 | 9 (7) | 3 (3) | 1 (1) | 8 | 13 | 5 | 0 | 13 |
| Преображение рифа Хаттерас | `fears-sharp-little-needles-en` | 75–78 | 10 | 5 (0) | 1 (1) | 0 (0) | 2 | 8 | 0 | 0 | 13 |
| Исследовательский центр Уинока-Пойнт | `fears-sharp-little-needles-en` | 142–146 | 11 | 7 (0) | 2 (0) | 0 (0) | 5 | 10 | 3 | 0 | 13 |
| Любовь матери | `mothers-love-ru` | 3–15 | 19 | 33 (1) | 6 (4) | 5 (4) | 6 | 34 | 1 | 0 | 13 |
| Скрюченный домище | `osobnyaki-bezumiya-ru` | 43–65 | 19 | 24 (6) | 4 (2) | 8 (0) | 15 | 44 | 2 | 0 | 13 |
| Язвы | `fears-sharp-little-needles-en` | 80–85 | 9 | 9 (0) | 0 (0) | 2 (2) | 3 | 7 | 0 | 0 | 12 |
| Секретный код | `osobnyaki-bezumiya-ru` | 71–98 | 18 | 12 (6) | 8 (4) | 5 (0) | 9 | 21 | 2 | 0 | 12 |
| Сбил и скрылся | `fears-sharp-little-needles-en` | 70–73 | 10 | 6 (0) | 1 (1) | 0 (0) | 2 | 10 | 0 | 0 | 11 |
| Глава III. Замок Тёмный | `griby-s-yuggota-ru` | 21–32 | 22 | 15 (0) | 4 (3) | 3 (3) | 10 | 31 | 5 | 0 | 11 |
| Черноводный ручей | `chernovodnyy-ruchey-ru` | 6–38 | 18 | 33 (0) | 8 (4) | 6 (0) | 4 | 35 | 5 | 0 | 10 |
| Tormiss CRD, модель Z-17 | `fears-sharp-little-needles-en` | 125–128 | 8 | 6 (0) | 3 (2) | 1 (0) | 3 | 11 | 0 | 0 | 10 |
| Подводное течение | `fears-sharp-little-needles-en` | 15–18 | 11 | 4 (0) | 3 (2) | 0 (0) | 2 | 11 | 2 | 0 | 10 |
| Призрак | `prizrak-ru` | 1–17 | 18 | 20 (0) | 3 (1) | 4 (0) | 8 | 31 | 0 | 0 | 9 |
| Террор | `terror-ru` | 8–24 | 20 | 21 (2) | 4 (1) | 3 (3) | 15 | 18 | 0 | 0 | 9 |
| Диссоциация | `fears-sharp-little-needles-en` | 114–118 | 15 | 6 (0) | 3 (2) | 1 (0) | 6 | 16 | 1 | 0 | 8 |
| Не вызывай того, чего не сможешь усмирить | `fears-sharp-little-needles-en` | 64–67 | 7 | 5 (0) | 4 (3) | 0 (0) | 0 | 7 | 0 | 0 | 8 |
| Глава 10. От Бомбея до границы Непала | `lokhmotya-korolya-ru` | 227–249 | 11 | 14 (10) | 3 (3) | 1 (1) | 1 | 23 | 2 | 0 | 8 |
| Под землёй и над землёй | `pod-zemlyoy-i-nad-zemlyoy-ru` | 6–22 | 21 | 25 (18) | 7 (2) | 3 (1) | 17 | 28 | 4 | 0 | 8 |
| Грань тьмы | `starter-edge-of-darkness-ru` | 2–29 | 21 | 26 (6) | 8 (3) | 9 (0) | 15 | 34 | 2 | 0 | 8 |
| Безымянный туман | `bezymyannyy-tuman-ru` | 1–7 | 15 | 17 (2) | 2 (0) | 5 (1) | 10 | 18 | 0 | 0 | 7 |
| Страх разлуки | `fears-sharp-little-needles-en` | 9–13 | 12 | 5 (0) | 2 (2) | 0 (0) | 2 | 11 | 1 | 0 | 7 |
| Особое меню | `fears-sharp-little-needles-en` | 136–140 | 7 | 8 (0) | 0 (0) | 0 (0) | 5 | 4 | 0 | 0 | 7 |
| Этап четвёртый: Каркоза | `mify-hastura-ru` | 24–32 | 9 | 4 (0) | 4 (2) | 2 (0) | 4 | 6 | 0 | 0 | 7 |
| Эликсир жизни | `eliksir-zhizni-ru` | 4–11 | 19 | 20 (0) | 3 (3) | 5 (2) | 9 | 17 | 2 | 0 | 6 |
| Призраки Рейвенскара | `fears-sharp-little-needles-en` | 130–134 | 7 | 1 (0) | 2 (1) | 1 (0) | 4 | 8 | 1 | 0 | 6 |
| Глава 3. Англия | `masks-of-nyarlathotep-en` | 182–217 | 45 | 40 (2) | 8 (6) | 12 (12) | 35 | 40 | 7 | 1 | 6 |
| Парк развлечений | `park-razvlecheniy-ru` | 2–24 | 17 | 29 (13) | 5 (1) | 11 (10) | 11 | 29 | 1 | 0 | 6 |
| Погоня в поезде | `pogonya-v-poezde-ru` | 5–19 | 11 | 41 (0) | 3 (2) | 1 (0) | 8 | 12 | 4 | 0 | 6 |
| Аукцион | `auktsion-ru` | 1–31 | 19 | 24 (0) | 5 (4) | 2 (1) | 18 | 20 | 2 | 0 | 5 |
| Вечер поэзии | `fears-sharp-little-needles-en` | 120–123 | 10 | 7 (0) | 3 (2) | 1 (1) | 2 | 8 | 0 | 0 | 5 |
| Воскрешение | `fears-sharp-little-needles-en` | 93–96 | 9 | 9 (0) | 1 (1) | 0 (0) | 4 | 10 | 0 | 0 | 5 |
| В ожидании рождения | `fears-sharp-little-needles-en` | 98–102 | 9 | 8 (0) | 2 (0) | 1 (0) | 5 | 18 | 1 | 0 | 5 |
| Глава VII. В гавани: часть II | `griby-s-yuggota-ru` | 52–67 | 10 | 15 (1) | 2 (1) | 3 (3) | 25 | 21 | 1 | 0 | 5 |
| Среди древних деревьев | `keeper-rulebook-ru` | 324–336 | 19 | 22 (0) | 4 (3) | 9 (4) | 16 | 28 | 2 | 0 | 5 |
| Месяц ночи | `mesyats-nochi-ru` | 7–45 | 25 | 20 (3) | 8 (7) | 2 (2) | 13 | 23 | 2 | 0 | 5 |
| Сон № 7 | `number-7-dream-en` | 7–18 | 19 | 17 (8) | 3 (1) | 10 (0) | 8 | 30 | 3 | 0 | 5 |
| Мистер Корбитт | `osobnyaki-bezumiya-ru` | 14–36 | 17 | 19 (6) | 7 (1) | 4 (0) | 9 | 24 | 2 | 0 | 5 |
| Проклятие Ганеши | `proklyatie-ganeshi-ru` | 4–20 | 15 | 12 (1) | 1 (1) | 3 (0) | 6 | 18 | 1 | 0 | 5 |
| Анленд | `fears-sharp-little-needles-en` | 104–107 | 8 | 3 (0) | 1 (0) | 0 (0) | 3 | 13 | 1 | 0 | 4 |
| Глава VI. В гавани: часть I | `griby-s-yuggota-ru` | 8–15 | 10 | 21 (2) | 4 (4) | 5 (5) | 18 | 14 | 2 | 0 | 4 |
| Глава II. Нечто в колодце | `griby-s-yuggota-ru` | 16–20 | 10 | 11 (2) | 1 (0) | 3 (3) | 2 | 10 | 0 | 0 | 4 |
| Хэллоуин в Данвиче | `hellouin-v-danviche-ru` | 3–11 | 22 | 13 (0) | 5 (1) | 1 (1) | 11 | 15 | 0 | 0 | 4 |
| Идол Тота | `idol-tota-ru` | 7–21 | 17 | 14 (0) | 1 (0) | 4 (0) | 7 | 15 | 3 | 0 | 4 |
| Каникулы в Иннсмуте | `kanikuly-v-innsmute-ru` | 2–8 | 16 | 10 (0) | 4 (3) | 0 (0) | 9 | 17 | 0 | 0 | 4 |
| Когда зажигаются костры | `kogda-zazhigayutsya-kostry-ru` | 6–21 | 15 | 10 (7) | 2 (1) | 3 (1) | 8 | 12 | 1 | 0 | 4 |
| Погасший маяк | `lightless-beacon-ru` | 7–23 | 16 | 8 (0) | 3 (2) | 3 (3) | 16 | 23 | 3 | 0 | 4 |
| Глава 5. Каркоза на Земле | `lokhmotya-korolya-ru` | 117–157 | 15 | 10 (9) | 6 (4) | 3 (3) | 3 | 22 | 0 | 0 | 4 |
| Глава 3. Курган Спрингер Маунд и канал | `lokhmotya-korolya-ru` | 85–107 | 14 | 11 (11) | 7 (7) | 3 (0) | 5 | 11 | 4 | 0 | 4 |
| Дом Мемфиса | `osobnyaki-bezumiya-ru` | 105–140 | 17 | 20 (6) | 3 (3) | 5 (0) | 12 | 25 | 1 | 0 | 4 |
| Остров лучезарной надежды | `ostrov-luchezarnoy-nadezhdy-ru` | 2–8 | 6 | 8 (0) | 5 (2) | 2 (0) | 3 | 7 | 2 | 0 | 4 |
| Попались! | `popalis-ru` | 1–1 | 7 | 7 (1) | 3 (2) | 0 (0) | 2 | 7 | 0 | 0 | 4 |
| Служители озера | `dveri-vo-tmu-ru` | 57–74 | 14 | 24 (10) | 5 (3) | 3 (0) | 8 | 24 | 2 | 0 | 3 |
| Pulvis et Umbra Sumus | `fears-sharp-little-needles-en` | 36–40 | 14 | 5 (0) | 2 (1) | 3 (0) | 1 | 15 | 2 | 0 | 3 |
| Вот так головоломка! | `keepers-companion-en` | 164–192 | 16 | 19 (9) | 4 (3) | 4 (4) | 12 | 22 | 3 | 0 | 3 |
| Глава 4. Полёт на север | `lokhmotya-korolya-ru` | 108–116 | 16 | 16 (13) | 3 (3) | 4 (3) | 2 | 20 | 1 | 0 | 3 |
| Глава 6. Разговоры о Гоатсвуде | `lokhmotya-korolya-ru` | 160–167 | 6 | 5 (5) | 6 (5) | 1 (1) | 1 | 9 | 0 | 0 | 3 |
| Глава 11. Дорога в Дракмар | `lokhmotya-korolya-ru` | 252–274 | 13 | 8 (4) | 4 (3) | 3 (3) | 2 | 19 | 3 | 0 | 3 |
| Пустые страницы | `pustye-stranitsy-ru` | 1–13 | 11 | 16 (0) | 9 (8) | 1 (0) | 6 | 9 | 0 | 0 | 3 |
| Одинокая нить | `tri-koshmarnykh-vechera-ru` | 15–31 | 12 | 6 (5) | 2 (2) | 2 (2) | 5 | 8 | 2 | 0 | 3 |
| Вирусный | `viral-en` | 15–103 | 23 | 19 (10) | 4 (4) | 40 (23) | 12 | 28 | 5 | 0 | 3 |
| Благослови детей его | `bless-the-beast-and-children-ru` | 3–14 | 21 | 31 (3) | 4 (3) | 5 (0) | 7 | 30 | 4 | 0 | 2 |
| Вышел срок | `chernovodnyy-ruchey-ru` | 60–75 | 19 | 32 (7) | 4 (2) | 5 (0) | 4 | 17 | 2 | 0 | 2 |
| Мертвенный свет | `dead-light-en` | 8–35 | 10 | 22 (19) | 2 (1) | 5 (5) | 17 | 15 | 3 | 0 | 2 |
| Большой синий буопот | `dead-light-en` | 61–62 | 0 | 2 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Объезд | `dead-light-en` | 61–64 | 0 | 4 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Попутчицы | `dead-light-en` | 61–64 | 0 | 4 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Нейтральная территория | `dead-light-en` | 61–62 | 0 | 2 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Бесконечная дорога | `dead-light-en` | 61–63 | 0 | 3 (0) | 1 (1) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Чемодан | `dead-light-en` | 61–63 | 0 | 3 (0) | 0 (0) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Чернее чёрного | `dveri-vo-tmu-ru` | 95–109 | 13 | 22 (10) | 5 (2) | 1 (0) | 9 | 14 | 1 | 0 | 2 |
| Джонни Бой | `dzhonni-boy-ru` | 2–7 | 11 | 8 (1) | 2 (1) | 1 (1) | 4 | 8 | 0 | 0 | 2 |
| Экспонат «Новая жизнь» | `eksponat-novaya-zhizn-ru` | 3–16 | 10 | 9 (2) | 2 (2) | 2 (2) | 7 | 5 | 0 | 0 | 2 |
| Дополнительная сцена 1: «Залы Целаено» | `griby-s-yuggota-ru` | 72–75 | 5 | 3 (0) | 3 (2) | 0 (0) | 3 | 8 | 1 | 0 | 2 |
| Глава V. Горы Луны | `griby-s-yuggota-ru` | 41–51 | 19 | 17 (1) | 7 (6) | 4 (4) | 11 | 18 | 1 | 0 | 2 |
| Глава IV. Пески времени | `griby-s-yuggota-ru` | 33–40 | 10 | 16 (1) | 6 (4) | 1 (1) | 5 | 15 | 3 | 0 | 2 |
| Холодный урожай | `kholodnyy-urozhay-ru` | 3–44 | 19 | 43 (9) | 3 (2) | 4 (1) | 9 | 32 | 2 | 0 | 2 |
| Глава 1. Безумец | `lokhmotya-korolya-ru` | 37–59 | 12 | 9 (9) | 4 (4) | 4 (2) | 2 | 15 | 2 | 0 | 2 |
| Глава 7. Ферма Нага | `lokhmotya-korolya-ru` | 168–189 | 9 | 10 (10) | 6 (6) | 4 (1) | 1 | 11 | 2 | 0 | 2 |
| Пролог. Ночная премьера | `lokhmotya-korolya-ru` | 19–20 | 4 | 7 (2) | 2 (2) | 4 (2) | 1 | 4 | 2 | 0 | 2 |
| Глава 12. Монастырь | `lokhmotya-korolya-ru` | 275–307 | 21 | 11 (10) | 8 (6) | 4 (2) | 3 | 15 | 1 | 0 | 2 |
| Глава 9. Наместник Индии | `lokhmotya-korolya-ru` | 212–226 | 5 | 7 (6) | 1 (1) | 0 (0) | 0 | 4 | 1 | 0 | 2 |
| Глава 2. Прогулка в парке | `lokhmotya-korolya-ru` | 60–83 | 11 | 15 (15) | 1 (1) | 4 (1) | 1 | 16 | 1 | 0 | 2 |
| Маленький клуб ужасов | `malenkiy-klub-uzhasov-ru` | 3–13 | 18 | 20 (3) | 4 (3) | 3 (1) | 6 | 14 | 0 | 0 | 2 |
| Глава 7. Китай | `masks-of-nyarlathotep-en` | 526–547 | 43 | 48 (1) | 21 (10) | 21 (21) | 29 | 46 | 6 | 0 | 2 |
| Глава 4. Египет | `masks-of-nyarlathotep-en` | 302–386 | 43 | 46 (3) | 24 (13) | 11 (11) | 19 | 45 | 2 | 0 | 2 |
| Глава 5. Кения | `masks-of-nyarlathotep-en` | 389–406 | 25 | 33 (1) | 21 (13) | 5 (5) | 15 | 29 | 7 | 0 | 2 |
| Моя маленькая сестра | `moya-malenkaya-sestra-ru` | 3–20 | 13 | 11 (8) | 4 (3) | 6 (0) | 13 | 19 | 4 | 0 | 2 |
| Одно небольшое дельце… | `odno-nebolshoe-deltse-ru` | 3–12 | 12 | 11 (0) | 3 (1) | 2 (1) | 7 | 11 | 1 | 0 | 2 |
| Рейд на Иннсмут | `pobeg-iz-innsmuta-ru` | 99–103 | 8 | 15 (9) | 6 (3) | 3 (0) | 1 | 11 | 0 | 0 | 2 |
| Цель 1: Эзотерический орден Дагона | `pobeg-iz-innsmuta-ru` | 108–116 | 14 | 15 (6) | 9 (5) | 1 (0) | 5 | 10 | 0 | 0 | 2 |
| Подземка | `podzemka-ru` | 2–12 | 13 | 6 (0) | 4 (3) | 1 (0) | 11 | 25 | 1 | 0 | 2 |
| Ящик Пандоры | `pulp-cthulhu-en` | 177–195 | 16 | 43 (13) | 9 (2) | 13 (10) | 6 | 10 | 2 | 0 | 2 |
| Дезинтегратор | `pulp-cthulhu-en` | 139–154 | 15 | 27 (9) | 4 (2) | 3 (2) | 3 | 9 | 2 | 1 | 2 |
| Мертвецкий стомп | `starter-dead-mans-stomp-ru` | 4–23 | 23 | 30 (5) | 4 (3) | 7 (0) | 6 | 17 | 5 | 0 | 2 |
| Кровавая страница | `tsarstvo-terrora-ru` | 108–110 | 0 | 12 (0) | 1 (0) | 0 (0) | 0 | 3 | 0 | 0 | 2 |
| Книжные черви | `tsarstvo-terrora-ru` | 108–113 | 0 | 24 (0) | 3 (1) | 0 (0) | 0 | 2 | 0 | 0 | 2 |
| Холодная кровь | `tsarstvo-terrora-ru` | 108–110 | 0 | 13 (1) | 3 (2) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Страх тьмы | `tsarstvo-terrora-ru` | 108–113 | 0 | 24 (0) | 4 (2) | 0 (0) | 0 | 0 | 0 | 0 | 2 |
| Коллекционная редкость | `tsarstvo-terrora-ru` | 108–112 | 0 | 23 (0) | 3 (1) | 0 (0) | 0 | 2 | 0 | 0 | 2 |
| Лаборатория Антуана Лавуазье | `tsarstvo-terrora-ru` | 108–112 | 0 | 23 (0) | 3 (1) | 0 (0) | 0 | 1 | 0 | 0 | 2 |
| Выдуманная болезнь | `tsarstvo-terrora-ru` | 108–111 | 0 | 18 (0) | 2 (1) | 0 (0) | 0 | 1 | 0 | 0 | 2 |
| Игра в напёрстки | `tsarstvo-terrora-ru` | 108–111 | 0 | 18 (0) | 3 (1) | 0 (0) | 0 | 1 | 0 | 0 | 2 |
| Нечто в Бастилии | `tsarstvo-terrora-ru` | 108–108 | 0 | 2 (0) | 3 (2) | 0 (0) | 0 | 3 | 0 | 0 | 2 |
| За гранью тьмы | `beyond-the-edge-of-darkness-en` | 10–33 | 8 | 22 (3) | 4 (2) | 4 (2) | 25 | 11 | 1 | 0 | 1 |
| Гений места | `dveri-vo-tmu-ru` | 35–51 | 11 | 20 (10) | 2 (1) | 6 (0) | 2 | 17 | 2 | 0 | 1 |
| Великий и ужасный Авто | `fears-sharp-little-needles-en` | 42–45 | 6 | 3 (0) | 4 (1) | 0 (0) | 5 | 5 | 0 | 0 | 1 |
| Свет погас | `fears-sharp-little-needles-en` | 52–56 | 10 | 12 (0) | 2 (1) | 2 (2) | 2 | 6 | 0 | 0 | 1 |
| Грехи моей юности | `fears-sharp-little-needles-en` | 20–23 | 5 | 1 (0) | 2 (2) | 0 (0) | 0 | 1 | 0 | 0 | 1 |
| Последнее желание Уолтера | `fears-sharp-little-needles-en` | 27–28 | 6 | 7 (0) | 3 (2) | 0 (0) | 3 | 9 | 1 | 0 | 1 |
| Глава I. Сновидец | `griby-s-yuggota-ru` | 7–7 | 11 | 9 (1) | 2 (2) | 4 (4) | 4 | 11 | 1 | 0 | 1 |
| Грибы с Юггота | `griby-s-yuggota-ru` | 100–100 | 0 | 11 (2) | 6 (6) | 0 (0) | 0 | 8 | 0 | 0 | 1 |
| Будь у меня молоток | `keepers-companion-en` | 143–158 | 15 | 13 (6) | 3 (3) | 0 (0) | 8 | 10 | 2 | 0 | 1 |
| Маленькие чудеса | `keepers-companion-en` | 126–140 | 10 | 3 (2) | 5 (5) | 2 (2) | 1 | 10 | 2 | 0 | 1 |
| Лагерь Санни | `lager-sanni-ru` | 5–13 | 10 | 21 (0) | 3 (2) | 8 (0) | 9 | 14 | 1 | 0 | 1 |
| Глава 1. Начало кампании | `masks-of-nyarlathotep-en` | 94–95 | 2 | 2 (1) | 0 (0) | 11 (11) | 0 | 1 | 0 | 0 | 1 |
| Глава 8. Грандиозный финал | `masks-of-nyarlathotep-en` | 622–625 | 7 | 9 (0) | 14 (10) | 0 (0) | 2 | 8 | 0 | 0 | 1 |
| Маски Ньярлатхотепа | `masks-of-nyarlathotep-en` | 38–38 | 0 | 107 (15) | 17 (10) | 0 (0) | 16 | 12 | 0 | 0 | 1 |
| Пролог: Перу | `masks-of-nyarlathotep-en` | 59–92 | 26 | 13 (2) | 8 (4) | 3 (3) | 4 | 26 | 3 | 0 | 1 |
| Ограбление по-Аркхемски | `ograblenie-po-arkhemski-ru` | 2–14 | 10 | 9 (1) | 3 (1) | 3 (0) | 8 | 26 | 2 | 0 | 1 |
| Pax Cthuliana | `pax-cthuliana-ru` | 13–51 | 13 | 18 (5) | 3 (3) | 23 (22) | 6 | 22 | 2 | 0 | 1 |
| Наследство Кроуфордов | `pobeg-iz-innsmuta-ru` | 64–75 | 11 | 22 (1) | 2 (2) | 5 (1) | 0 | 14 | 0 | 0 | 1 |
| Побег из Иннсмута | `pobeg-iz-innsmuta-ru` | 76–98 | 21 | 42 (9) | 6 (5) | 7 (2) | 4 | 26 | 0 | 0 | 1 |
| Посёлок Берёзовый | `poselok-berezovyy-ru` | 5–12 | 19 | 9 (0) | 4 (3) | 0 (0) | 7 | 12 | 0 | 0 | 1 |
| В ожидании урагана | `pulp-cthulhu-en` | 160–173 | 17 | 14 (5) | 4 (3) | 0 (0) | 5 | 17 | 4 | 0 | 1 |
| Рождественская вечеринка | `rozhdestvenskaya-vecherinka-ru` | 2–13 | 16 | 18 (1) | 3 (1) | 1 (0) | 10 | 21 | 5 | 0 | 1 |
| Тайны Кремля | `secrets-of-the-kremlin-en` | 7–20 | 13 | 20 (0) | 6 (4) | 6 (0) | 4 | 36 | 6 | 0 | 1 |
| Шанс на чудо | `shans-na-chudo-ru` | 4–9 | 7 | 0 (0) | 5 (4) | 0 (0) | 7 | 7 | 0 | 0 | 1 |
| Бумажный след | `starter-paper-chase-ru` | 2–11 | 13 | 14 (5) | 1 (1) | 1 (0) | 4 | 11 | 2 | 0 | 1 |
| Охота | `temnye-veka-tri-stsenariya-ru` | 222–230 | 12 | 16 (4) | 7 (3) | 1 (1) | 3 | 9 | 2 | 0 | 1 |
| Синее сияние | `tri-koshmarnykh-vechera-ru` | 66–86 | 17 | 8 (7) | 4 (4) | 4 (4) | 9 | 20 | 2 | 0 | 1 |
| Царство Террора | `tsarstvo-terrora-ru` | 115–115 | 0 | 20 (14) | 3 (3) | 4 (4) | 1 | 15 | 9 | 0 | 1 |
| Вне власти времени | `vne-vlasti-vremeni-ru` | 3–11 | 9 | 9 (0) | 2 (1) | 5 (1) | 5 | 7 | 1 | 0 | 1 |
| Жертвы северных ветров | `zhertvy-severnykh-vetrov-ru` | 3–20 | 22 | 14 (0) | 2 (1) | 2 (2) | 6 | 20 | 4 | 0 | 1 |
| Чёрная кассета | `chernaya-kasseta-ru` | 4–16 | 9 | 12 (2) | 2 (1) | 2 (1) | 3 | 10 | 0 | 0 | 0 |
| Чулки возле печки развешены в ряд | `chulki-vozle-pechki-ru` | 3–15 | 14 | 23 (0) | 2 (2) | 2 (1) | 9 | 15 | 0 | 0 | 0 |
| Кровные узы | `dveri-vo-tmu-ru` | 76–92 | 16 | 22 (10) | 4 (1) | 6 (0) | 2 | 23 | 2 | 0 | 0 |
| Фокус-группа | `fears-sharp-little-needles-en` | 110–112 | 7 | 5 (0) | 3 (2) | 2 (0) | 4 | 4 | 0 | 0 | 0 |
| Чьё топливо — люди и камни | `fears-sharp-little-needles-en` | 30–34 | 5 | 3 (0) | 3 (1) | 0 (0) | 3 | 11 | 1 | 0 | 0 |
| Флеботомия | `fears-sharp-little-needles-en` | 148–175 | 26 | 31 (2) | 2 (1) | 7 (5) | 12 | 24 | 2 | 0 | 0 |
| Спилсбери № 9485 | `fears-sharp-little-needles-en` | 47–50 | 6 | 2 (0) | 1 (0) | 0 (0) | 5 | 4 | 0 | 0 | 0 |
| Глава VIII: «День Зверя» | `griby-s-yuggota-ru` | 68–71 | 4 | 8 (2) | 3 (3) | 0 (0) | 4 | 11 | 1 | 0 | 0 |
| Дополнительная сцена 2: «Голос из вневремени» | `griby-s-yuggota-ru` | 76–76 | 1 | 4 (1) | 0 (0) | 0 (0) | 1 | 1 | 0 | 0 | 0 |
| Багровые письмена | `keeper-rulebook-ru` | 339–356 | 14 | 15 (11) | 3 (3) | 4 (0) | 8 | 15 | 2 | 0 | 0 |
| Когда зло побеждает | `kogda-zlo-pobezhdaet-ru` | 1–2 | 6 | 9 (1) | 2 (1) | 1 (0) | 6 | 15 | 1 | 0 | 0 |
| Глава 8. Братья Жёлтого знака | `lokhmotya-korolya-ru` | 195–211 | 6 | 10 (9) | 5 (4) | 4 (2) | 2 | 12 | 1 | 0 | 0 |
| Лохмотья Короля | `lokhmotya-korolya-ru` | 21–36 | 1 | 44 (39) | 8 (7) | 4 (2) | 1 | 15 | 0 | 0 | 0 |
| Глава 2. Америка | `masks-of-nyarlathotep-en` | 102–163 | 31 | 49 (4) | 10 (7) | 21 (20) | 13 | 26 | 3 | 0 | 0 |
| Шкатулка демонов господина Луна | `masks-of-nyarlathotep-en` | 548–555 | 4 | 2 (0) | 1 (1) | 1 (1) | 3 | 3 | 1 | 0 | 0 |
| Змей из Челси | `masks-of-nyarlathotep-en` | 218–229 | 6 | 4 (0) | 2 (1) | 1 (1) | 4 | 7 | 1 | 0 | 0 |
| Ужас Дербишира | `masks-of-nyarlathotep-en` | 234–252 | 10 | 19 (0) | 3 (3) | 2 (2) | 3 | 14 | 2 | 0 | 0 |
| Охотничий домик | `masks-of-nyarlathotep-en` | 407–423 | 4 | 12 (0) | 5 (2) | 3 (3) | 7 | 4 | 1 | 0 | 0 |
| Наедине с Хэллоуином (соло) | `naedine-s-hellouinom-ru` | 251–251 | 0 | 23 (0) | 26 (13) | 2 (0) | 13 | 59 | 1 | 0 | 0 |
| Наедине с пламенем (соло) | `naedine-s-plamenem-ru` | 1–5 | 0 | 11 (1) | 4 (2) | 0 (0) | 8 | 18 | 1 | 0 | 0 |
| Наедине с помехами (соло) | `naedine-s-pomekhami-ru` | 191–191 | 0 | 8 (3) | 1 (1) | 2 (1) | 14 | 7 | 0 | 0 | 0 |
| Наедине с приливом (соло) | `naedine-s-prilivom-ru` | 90–90 | 0 | 14 (5) | 2 (2) | 2 (0) | 8 | 12 | 0 | 0 | 0 |
| Наедине с тьмой (соло) | `naedine-s-tmoy-ru` | 104–104 | 0 | 34 (4) | 13 (10) | 9 (8) | 8 | 56 | 6 | 0 | 0 |
| Некрополис | `necropolis-en` | 5–15 | 10 | 7 (0) | 4 (3) | 1 (1) | 9 | 11 | 3 | 0 | 0 |
| Ничего, кроме ветра | `nichego-krome-vetra-ru` | 5–9 | 11 | 7 (0) | 4 (2) | 0 (0) | 1 | 7 | 1 | 0 | 0 |
| Новая жизнь | `novaya-zhizn-ru` | 3–17 | 13 | 10 (7) | 6 (6) | 10 (9) | 4 | 10 | 2 | 0 | 0 |
| Омерзительная пятёрка | `omerzitelnaya-pyaterka-ru` | 3–11 | 6 | 15 (0) | 1 (0) | 2 (1) | 4 | 9 | 0 | 0 | 0 |
| Цель 2: Поместье Маршей | `pobeg-iz-innsmuta-ru` | 118–129 | 11 | 23 (5) | 5 (3) | 1 (0) | 2 | 10 | 0 | 0 | 0 |
| Цель 3: Тоннели контрабандистов | `pobeg-iz-innsmuta-ru` | 61–63 | 13 | 23 (6) | 5 (3) | 0 (0) | 1 | 12 | 0 | 0 | 0 |
| Цель 4: Риф Дьявола | `pobeg-iz-innsmuta-ru` | 141–149 | 13 | 12 (2) | 5 (3) | 0 (0) | 0 | 9 | 0 | 0 | 0 |
| Цель 5: Й’ха-нтлеи | `pobeg-iz-innsmuta-ru` | 150–159 | 11 | 10 (1) | 5 (4) | 1 (0) | 1 | 4 | 0 | 0 | 0 |
| Цель 6: Аффинажный завод Марша | `pobeg-iz-innsmuta-ru` | 104–107 | 10 | 16 (3) | 4 (3) | 0 (0) | 1 | 8 | 0 | 0 | 0 |
| Медленная лодка в Китай | `pulp-cthulhu-en` | 207–235 | 19 | 30 (13) | 4 (2) | 2 (1) | 6 | 26 | 3 | 0 | 0 |
| Судьба братьев Вашингтон | `sudba-bratev-vashington-ru` | 1–2 | 6 | 12 (0) | 4 (3) | 0 (0) | 5 | 11 | 1 | 0 | 0 |
| Эсевальд | `temnye-veka-tri-stsenariya-ru` | 244–249 | 10 | 24 (6) | 6 (2) | 1 (0) | 6 | 10 | 0 | 0 | 0 |
| Гибель, пришедшая в Уэссекс | `temnye-veka-tri-stsenariya-ru` | 234–239 | 9 | 15 (4) | 4 (3) | 1 (0) | 2 | 7 | 0 | 0 | 0 |
| Тень над Провиденсом | `ten-nad-providensom-ru` | 5–18 | 9 | 18 (0) | 5 (2) | 2 (1) | 16 | 10 | 2 | 0 | 0 |
| Куски и фрагменты | `tri-koshmarnykh-vechera-ru` | 38–56 | 13 | 8 (6) | 7 (6) | 4 (4) | 6 | 15 | 2 | 0 | 0 |
| Часть первая: 1789 | `tsarstvo-terrora-ru` | 17–49 | 32 | 29 (14) | 4 (3) | 2 (2) | 8 | 30 | 7 | 0 | 0 |
| Часть вторая: июнь 1794 | `tsarstvo-terrora-ru` | 57–86 | 22 | 28 (14) | 5 (3) | 1 (1) | 8 | 24 | 3 | 0 | 0 |
| Туманы острова Сан-Кристобаль | `tumany-san-kristobal-ru` | 4–18 | 15 | 9 (4) | 3 (0) | 4 (1) | 7 | 12 | 1 | 0 | 0 |
| Люблю тебя до смерти | `vedomo-li-lyubvi-ru` | 12–23 | 8 | 14 (1) | 0 (0) | 7 (7) | 4 | 11 | 0 | 0 | 0 |
| Маска желания | `vedomo-li-lyubvi-ru` | 31–43 | 12 | 11 (0) | 1 (1) | 8 (8) | 3 | 7 | 0 | 0 | 0 |
| Забывающийся | `zabyvayushchiysya-ru` | 4–13 | 8 | 12 (3) | 1 (0) | 0 (0) | 7 | 13 | 0 | 0 | 0 |

## Находки по сценариям

### Девятнадцатая лунка (`osobnyaki-bezumiya-ru/scenario/hole-nineteenth-hole`) — 43

- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-woods` Прогулка в Вороньем или Чёрном лесу — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-farms` Посещение фермы Макинтошей или Беллов — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-library-research` Университетский колледж или библиотека Данди — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-field-anomalies` Сцены на поле — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-entrance-hall` Вход и вестибюль: тёмные витражи — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-golf-shop` Гольф-лавка: царапина «Х» — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-ladies-changing-room` Женская раздевалка: шёпот — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-messages-from-aether` Послания из эфира — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-mens-changing-room` Мужская раздевалка и душевая: бродящие меж миров — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-basement-stairs` Спуск в подвал: обледенелые ступени — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-library` Библиотека/переговорная: смещённая гравитация — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-ballroom` Ресторан/бальный зал: межпространственный пузырь — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-lounge` Гостиная: шкаф-дверь — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-staff-room` Служебное помещение: стрелки вниз — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-kitchen` Кухня: фрактальные следы — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-pantry` Кладовая: «Вниз!» — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-storeroom` Склад и мороз — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-wine-cellar` Винный погреб: гул за стеной — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-secret-quarters` Тайный ход и жилище учёных — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-boiler-room` Котельная: замурованная дверь — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-into-the-aether` Путешествия в эфир и за его пределы — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/hole-mythos-encounters` Столкновения с тварями Мифов — сцена без итога
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-journey` Дорога в Данди и Кроу-Вуд-Холл — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-woods` Прогулка в Вороньем или Чёрном лесу — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-library-research` Университетский колледж или библиотека Данди — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-approach` Осмотр «Тислдауна» — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-field-anomalies` Сцены на поле — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-entrance-hall` Вход и вестибюль: тёмные витражи — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-golf-shop` Гольф-лавка: царапина «Х» — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-ladies-changing-room` Женская раздевалка: шёпот — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-basement-stairs` Спуск в подвал: обледенелые ступени — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-library` Библиотека/переговорная: смещённая гравитация — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-ballroom` Ресторан/бальный зал: межпространственный пузырь — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-lounge` Гостиная: шкаф-дверь — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-office` Кабинет: запертый ящик и два плана — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-staff-room` Служебное помещение: стрелки вниз — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-kitchen` Кухня: фрактальные следы — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-pantry` Кладовая: «Вниз!» — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-storeroom` Склад и мороз — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-electrical-room` Щитовая: удар током — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-wine-cellar` Винный погреб: гул за стеной — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-secret-quarters` Тайный ход и жилище учёных — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/hole-boiler-room` Котельная: замурованная дверь — сцена без участников

### Сны о Японии (`sny-o-yaponii-ru/scenario/sny-o-yaponii`) — 28

- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/dreams` Сны о лесе — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/shipping-office-break-in` Ночной обыск офиса Нобла — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/researching-aokigahara` Исследуя Аокигахару — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/road-to-naushua` Дорога в Наушуа — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/ryokan-axelby` Рёкан Наушуа и Джеймс Аксельби — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/hundred-candles` «100 свечей» — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/luggage-room-clues` Улики в камере хранения — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/ferret-truck` Обыск грузовика Хорька — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/entering-the-forest` Вход в лес Аокигахара — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/event-7-1-ornithologist` Событие 7-1: Орнитолог из Дюссельдорфа — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/event-7-2-time-distortion` Событие 7-2: Искажение времени — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/event-7-3-dream` Событие 7-3: Сон — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/event-7-4-disappearance` Событие 7-4: Исчезновение — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/event-7-6-stalker` Событие 7-6: Сталкер — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/epilogue` Эпилог: возвращение домой — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/taint-aftermath` Порча: исчезновения знакомых — сцена без итога
- [low] `scenes.no_outcome` `sny-o-yaponii-ru/scene/return-to-naushua` Возвращение в деревню Наушуа — сцена без итога
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/veronica-room` Улики в комнате Вероники — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/shipping-office-break-in` Ночной обыск офиса Нобла — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/researching-aokigahara` Исследуя Аокигахару — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/road-to-naushua` Дорога в Наушуа — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/naushua-village` Прибытие в деревню Наушуа — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/luggage-room-clues` Улики в камере хранения — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/ferret-truck` Обыск грузовика Хорька — сцена без участников
- [low] `scenes.no_people` `sny-o-yaponii-ru/scene/event-7-5-dead-investigators` Событие 7-5: Мёртвые сыщики — сцена без участников
- [low] `scenes.no_place` `sny-o-yaponii-ru/scene/dreams` Сны о лесе — сцена без места
- [low] `scenes.no_place` `sny-o-yaponii-ru/scene/researching-aokigahara` Исследуя Аокигахару — сцена без места
- [low] `scenes.no_place` `sny-o-yaponii-ru/scene/taint-aftermath` Порча: исчезновения знакомых — сцена без места

### Отель «Скайлайн» (`otel-skaylayn-ru/scenario/otel-skaylayn`) — 26

- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/kopiya` Копия — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/zhivoy-etazh` Живой этаж — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/voskovoy-etazh` Восковой этаж — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/obychnyy-nomer` Обычный номер — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/komnata-bezdomnogo` Комната бездомного — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/komnata-proshlogo` Комната прошлого — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/razrushennaya-komnata` Разрушенная комната — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/komnata-s-fotografiyami` Комната с фотографиями — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/krasnaya-komnata` Красная комната — сцена без итога
- [low] `scenes.no_outcome` `otel-skaylayn-ru/scene/komnata-uborshchika` Комната уборщика — сцена без итога
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/nachalo-puti` Начало пути — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/probuzhdenie` Пробуждение — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/beskonechnyy-koridor` Бесконечный коридор — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/kopiya` Копия — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/prognivshiy-etazh` Прогнивший этаж — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/zhivoy-etazh` Живой этаж — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/voskovoy-etazh` Восковой этаж — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/obychnyy-nomer` Обычный номер — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/komnata-s-razlomom` Комната с разломом — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/komnata-proshlogo` Комната прошлого — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/razrushennaya-komnata` Разрушенная комната — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/komnata-s-fotografiyami` Комната с фотографиями — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/komnata-s-balkonom` Комната с балконом — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/krasnaya-komnata` Красная комната — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/komnata-s-generatorom` Комната с генератором — сцена без участников
- [low] `scenes.no_people` `otel-skaylayn-ru/scene/komnata-uborshchika` Комната уборщика — сцена без участников

### Проклятый идол Манко Капака (`cursed-idol-of-manco-capac-en/scenario/cursed-idol-of-manco-capac`) — 22

- [medium] `people.lost` `cursed-idol-of-manco-capac-en/character/speedy-durante` Дуранте «Шустрый» — персонаж страниц сценария не назван ни в сценарии, ни в сценах
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/museum-security` Охрана музея — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/security-guards` Охранники — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/museum-curator` Куратор музея — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/empire-of-the-sun-exhibit` Выставка «Империя Солнца» — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/investigating-museum-staff` Проверка сотрудников музея — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/travel` Путь по Нью-Йорку — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/research-and-connections` Исследования и связи — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/abandoned-church` Заброшенная церковь — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/bridgeport-police-station` Полицейский участок Бриджпорта — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/the-detective` Детектив — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/bennet-home` Дом Джозефа Беннета — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/bridgeport-archaeological-society` Бриджпортское археологическое общество — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/curtis-antiquities` Антикварная лавка Кёртиса — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/the-ghost` Призрак — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/race-travel` Дорога в музей — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/consequences` Последствия — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/before-6pm` До 18:00 — сцена без итога
- [low] `scenes.no_outcome` `cursed-idol-of-manco-capac-en/scene/epilogue` Эпилог — сцена без итога
- [low] `scenes.no_people` `cursed-idol-of-manco-capac-en/scene/travel` Путь по Нью-Йорку — сцена без участников
- [low] `scenes.no_people` `cursed-idol-of-manco-capac-en/scene/research-and-connections` Исследования и связи — сцена без участников
- [low] `scenes.no_people` `cursed-idol-of-manco-capac-en/scene/race-travel` Дорога в музей — сцена без участников

### Тайник Бутлегеров (`taynik-butlegerov-ru/scenario/taynik-butlegerov`) — 22

- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/ranniy-vizit` Ранний визит — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/razyaryonnyy-podrostok` Разъярённый подросток — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/potaynaya-dver` Потайная дверь — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/svyatilishche` Святилище — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/ostanki-gerberta` Останки Герберта — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/patrulnyy-avtomobil` Патрульный автомобиль — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/vozvrashchenie-v-portovyy-rayon` Возвращение в портовый район — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/antikvarnaya-lavka` Антикварная лавка Дэвида Блейка — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/publichnaya-biblioteka` Нью-Йоркская публичная библиотека — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/politseyskiy-uchastok` Полицейский участок — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/pokhishchenie-amuleta` Похищение амулета — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/arest` Арест — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/napisanie-pisma-i-final` Написание письма и финал — сцена без итога
- [low] `scenes.no_outcome` `taynik-butlegerov-ru/scene/zakrytye-otdely-bibliotek` Закрытые отделы библиотек — сцена без итога
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/ranniy-vizit` Ранний визит — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/podkhod-k-skladu` Портовые склады: подход к складу — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/svyatilishche` Святилище — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/ostanki-gerberta` Останки Герберта — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/vozvrashchenie-v-portovyy-rayon` Возвращение в портовый район — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/gradostroitelnoe-byuro` Градостроительное бюро, городская ратуша — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/publichnaya-biblioteka` Нью-Йоркская публичная библиотека — сцена без участников
- [low] `scenes.no_people` `taynik-butlegerov-ru/scene/zakrytye-otdely-bibliotek` Закрытые отделы библиотек — сцена без участников

### Сатурнова чаша (`dead-light-en/scenario/chalice`) — 21

- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-introductions` Знакомство — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-drinks` Напитки — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-telephone` Телефон — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-asking-for-gasoline` Просьба о бензине — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-evangeline-outside` Эванджелина снаружи — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-conversations` Разговоры — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-exploring-upstairs` Наверх — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-darkness-falls` Темнеет — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-evangeline-inside` Эванджелина в доме — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-lynwood-bodies` Тела Линвудов — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-dinner-party` Званый ужин — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-questions-and-deaths` Вопросы и смерти — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-realization` Прозрение — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-banishing-the-demon` Изгнание демона — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-freeing-the-trapped-souls` Освобождение душ — сцена без итога
- [low] `scenes.no_outcome` `dead-light-en/scene/chalice-confronting-the-shapeless-one` Встреча с Бесформенным — сцена без итога
- [low] `scenes.no_people` `dead-light-en/scene/chalice-out-of-gas` Кончился бензин — сцена без участников
- [low] `scenes.no_people` `dead-light-en/scene/chalice-telephone` Телефон — сцена без участников
- [low] `scenes.no_people` `dead-light-en/scene/chalice-exploring-upstairs` Наверх — сцена без участников
- [low] `scenes.no_people` `dead-light-en/scene/chalice-darkness-falls` Темнеет — сцена без участников
- [low] `scenes.no_people` `dead-light-en/scene/chalice-attempting-to-leave` Попытка уйти — сцена без участников

### Карнавал безумия (`karnaval-bezumiya-ru/scenario/karnaval-bezumiya`) — 21

- [low] `clues.unused` `karnaval-bezumiya-ru/item/arbalety-attraktsiona` Арбалеты аттракциона — item страниц сценария не использует ни сцена, ни шаг
- [low] `clues.unused` `karnaval-bezumiya-ru/item/sedativ-marvina` Седативное Марвина — item страниц сценария не использует ни сцена, ни шаг
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/glava-1` Глава 1: Найденные и потерянные — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/glava-2` Глава 2: Туда и сюда — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/glava-3` Глава 3: Рифма и разум — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/glava-4` Глава 4: Знаки и предзнаменования — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/glava-5` Глава 5: Прятки и поиски — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/glava-6` Глава 6: Лабиринты и чудовища — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/grazhdanskie-litsa` Неприятности: насилие на карнавале — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/pravookhranitelnye-organy` Неприятности: полиция на карнавале — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/vystupleniya-glavnoy-stseny` Выступления на главной сцене — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/lechebnitsa-progulka` Дом ужасов «Лечебница» — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/vagonchik-ledi-sari` Вагончик Леди Сари — сцена без итога
- [low] `scenes.no_outcome` `karnaval-bezumiya-ru/scene/proyavleniya-nerealnosti` Проявления Нереальности — сцена без итога
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/prolog-stsena-1` Сцена 1. Дорога на карнавал — сцена без участников
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/glava-1` Глава 1: Найденные и потерянные — сцена без участников
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/glava-2` Глава 2: Туда и сюда — сцена без участников
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/glava-3` Глава 3: Рифма и разум — сцена без участников
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/glava-4` Глава 4: Знаки и предзнаменования — сцена без участников
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/glava-5` Глава 5: Прятки и поиски — сцена без участников
- [low] `scenes.no_people` `karnaval-bezumiya-ru/scene/glava-6` Глава 6: Лабиринты и чудовища — сцена без участников

### Ужас в Иннсмуте (`innsmouth-terror-en/scenario/innsmouth-terror`) — 18

- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/arkham-advertiser` «Аркхэм Адвертайзер» — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/miskatonic-playhouse` Мискатоникский театр — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/around-the-train` Вокруг поезда — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/bazzledon-office` Кабинет Баззлдона — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/ginny-trailer` Трейлер Джинни — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/railway-entrance` Вход у железной дороги — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/into-innsmouth` В Иннсмут — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/esoteric-order-of-dagon` Эзотерический орден Дагона — сцена без итога
- [low] `scenes.no_outcome` `innsmouth-terror-en/scene/epilogue` Эпилог — сцена без итога
- [low] `scenes.no_people` `innsmouth-terror-en/scene/arrival` Прибытие в Иннсмут — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/gilman-house` Отель «Дом Гилмана» — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/around-the-train` Вокруг поезда — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/bazzledon-office` Кабинет Баззлдона — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/ginny-trailer` Трейлер Джинни — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/mcguire-lab` Лаборатория Макгвайра — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/railway-entrance` Вход у железной дороги — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/cave-system` Через пещеры — сцена без участников
- [low] `scenes.no_people` `innsmouth-terror-en/scene/into-innsmouth` В Иннсмут — сцена без участников

### Тьма под холмом (`dveri-vo-tmu-ru/scenario/darkness-beneath-the-hill`) — 17

- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-cave-inhabitants` Гнусные обитатели пещер — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-deeper-into-caverns` Глубже в пещеры — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-hall-of-history` Зал Истории — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-pitch` Обрыв — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-music-chamber` Чертоги музыки — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-sinkhole` Провал грунта — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-plantation` Теплица — сцена без итога
- [low] `scenes.no_outcome` `dveri-vo-tmu-ru/scene/darkness-temple` Храм Отца Змей — сцена без итога
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-into-the-depths` В глубины — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-entry-hall` Вестибюль — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-deeper-into-caverns` Глубже в пещеры — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-hall-of-history` Зал Истории — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-pitch` Обрыв — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-music-chamber` Чертоги музыки — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-sinkhole` Провал грунта — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-temple` Храм Отца Змей — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/darkness-suspended-animation` Камера анабиоза — сцена без участников

### Не забывай меня (`ne-zabyvay-menya-ru/scenario/ne-zabyvay-menya`) — 17

- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/meditsinskaya-pomoshch` Обращение за медицинской помощью — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/politsiya` Обращение в полицию — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/v-komnate-lin` В комнате Лин — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/sny` Сон как ключ к Безумию — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/ya-chuvstvuyu-sebya-uzhasno` Я чувствую себя ужасно… — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/issledovaniya` Исследования: студия и 7 Gate Films — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/biblioteka-i-internet` Библиотека, архивы и интернет — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/povtornye-intervyu` Повторные интервью — сцена без итога
- [low] `scenes.no_outcome` `ne-zabyvay-menya-ru/scene/krovavoe-predvestie` Кровавое предвестие — сцена без итога
- [low] `scenes.no_people` `ne-zabyvay-menya-ru/scene/probuzhdenie` Пробуждение — сцена без участников
- [low] `scenes.no_people` `ne-zabyvay-menya-ru/scene/v-komnate-lin` В комнате Лин — сцена без участников
- [low] `scenes.no_people` `ne-zabyvay-menya-ru/scene/sny` Сон как ключ к Безумию — сцена без участников
- [low] `scenes.no_people` `ne-zabyvay-menya-ru/scene/ya-chuvstvuyu-sebya-uzhasno` Я чувствую себя ужасно… — сцена без участников
- [low] `scenes.no_people` `ne-zabyvay-menya-ru/scene/biblioteka-i-internet` Библиотека, архивы и интернет — сцена без участников
- [low] `scenes.no_people` `ne-zabyvay-menya-ru/scene/vozvrashchenie-v-dom-kuperov` Возвращение в дом Куперов — сцена без участников
- [low] `scenes.no_place` `ne-zabyvay-menya-ru/scene/ya-chuvstvuyu-sebya-uzhasno` Я чувствую себя ужасно… — сцена без места
- [low] `scenes.no_place` `ne-zabyvay-menya-ru/scene/issledovaniya` Исследования: студия и 7 Gate Films — сцена без места

### Глава 6. Австралия (`masks-of-nyarlathotep-en/scenario/australia`) — 16

- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-just-rewards` Справедливое воздаяние — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-underground` Подземелья и внутри города — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-bunkhouse` Бараки — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-lines-of-light` Цепочки огней: рабочие — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-cult-rituals` Ритуалы культа — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-nursery` Детская — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-titan-horror` Титанический ужас — сцена без итога
- [low] `scenes.no_outcome` `masks-of-nyarlathotep-en/scene/australia-current-excavations` Текущие раскопки — сцена без итога
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-arriving` Прибытие в Австралию — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-sydney-institutions` Другие места в Сиднее — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-darwin-rumors` Дарвин: слухи — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-cuncudgerie` Кункуджери: дорога и слухи — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-second-entrance` Второй вход — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-underground` Подземелья и внутри города — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-nursery` Детская — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/australia-titan-horror` Титанический ужас — сцена без участников

### Тени Ленинграда (`shadows-of-leningrad-en/scenario/shadows-of-leningrad`) — 16

- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/museum-yezhov-office` Кабинет Владимира Ежова — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/museum-kamzanov-office` Кабинет Юрия Камзанова — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/museum-rossi-wing` Корпус Росси: змеи — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/sanctum-of-learning` Святилище знаний — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/descent-into-darkness` Спуск во тьму: умирающий Владимир — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/chamber-of-enlightenment` Зал просветления — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/dressing-rooms` Гримёрные — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/road-to-temple` Дорога к храму — сцена без итога
- [low] `scenes.no_outcome` `shadows-of-leningrad-en/scene/finale` Заключение — сцена без итога
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/museum-rossi-wing` Корпус Росси: змеи — сцена без участников
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/estate-return` Возвращение в усадьбу — сцена без участников
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/sanctum-of-learning` Святилище знаний — сцена без участников
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/chamber-of-enlightenment` Зал просветления — сцена без участников
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/dressing-rooms` Гримёрные — сцена без участников
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/road-to-temple` Дорога к храму — сцена без участников
- [low] `scenes.no_people` `shadows-of-leningrad-en/scene/finale` Заключение — сцена без участников

### И тут явился Жнец (`fears-sharp-little-needles-en/scenario/reaper`) — 15

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-gadsens-bend` Гадсенс-Бенд — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-st-elijahs-perdition` Погибель святого Илии — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-nikki-prius` «Приус» Никки — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-silas-and-peggy` Сайлас Стэндли и Пегги Дешам — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-southeast-ridge` Юго-восточный гребень — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-the-hollow` Лощина — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-currituck-place` Старая усадьба Карритак — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-pettigrew-house` Лачуга Петтигрю — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/reaper-the-shadowing` Затенение — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/reaper-gadsens-bend` Гадсенс-Бенд — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/reaper-nikki-prius` «Приус» Никки — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/reaper-southeast-ridge` Юго-восточный гребень — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/reaper-the-shadowing` Затенение — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/reaper-missing-couple` Пропавшая пара — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/reaper-resolutions` Развязка — сцена без места

### До самых костей (`fears-sharp-little-needles-en/scenario/bone-deep`) — 14

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-grisly-murder` Жуткое убийство — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-interviewing-jamie` Беседа с Джейми — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-back-yard` Обыск заднего двора — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-autopsy` Вскрытие и лабораторные результаты — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-dr-trask` Беседа с доктором Траск — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-unsolved-cases` Нераскрытые дела — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-doug-watts` Беседа с Дагом Уоттсом — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-vale-visit` Похоронный дом «Вейл» — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-gone-missing` Исчезновения — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-return-to-vale` Возвращение в похоронный дом «Вейл» — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-sepulcher` Склеп — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/bone-deep-blackmail` Шантаж — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/bone-deep-back-yard` Обыск заднего двора — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/bone-deep-return-to-vale` Возвращение в похоронный дом «Вейл» — сцена без участников

### Лечебница (`lechebnitsa-ru/scenario/lechebnitsa`) — 14

- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/put-na-ostrov` Путь на остров — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/paradnyy-vkhod` Парадный вход — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/telo-v-gostinoy` Тело в гостиной — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/podval` Подвал — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/vtoroy-etazh` Второй этаж: кабинет доктора Брюэра — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/territoriya-lechebnitsy` Территория лечебницы — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/zhertvoprinoshenie` Ночное жертвоприношение — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/lager-shelli` Разорённый лагерь студента — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/psikhoanaliz-khardinga` Сеансы с пациентами — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/mayak` Логово на маяке — сцена без итога
- [low] `scenes.no_outcome` `lechebnitsa-ru/scene/chudovishche-u-lechebnitsy` Чудовище у лечебницы — сцена без итога
- [low] `scenes.no_people` `lechebnitsa-ru/scene/territoriya-lechebnitsy` Территория лечебницы — сцена без участников
- [low] `scenes.no_people` `lechebnitsa-ru/scene/korablekrushenie` Раскопки кораблекрушения — сцена без участников
- [low] `scenes.no_place` `lechebnitsa-ru/scene/put-na-ostrov` Путь на остров — сцена без места

### МТС Харьков-37 (`mts-kharkov-37-ru/scenario/mts-kharkov-37`) — 14

- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/vskrytiya` Вскрытия — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/eksperimenty` Эксперименты — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/chtenie-dokumentov` Чтение документов — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/pochinka-telegrafa` Починка телеграфных линий — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/rabota-s-voyskami` Работа с войсками — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/semya-vizhedikh` Обнаружена семья Вижедих — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/ataki-tsveta` Атаки Цвета — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/tungusskiy-meteorit` Допустимая дезинформация: Тунгусский метеорит — сцена без итога
- [low] `scenes.no_outcome` `mts-kharkov-37-ru/scene/radiatsiya` Недопустимая дезинформация: радиация — сцена без итога
- [low] `scenes.no_place` `mts-kharkov-37-ru/scene/eksperimenty` Эксперименты — сцена без места
- [low] `scenes.no_place` `mts-kharkov-37-ru/scene/chtenie-dokumentov` Чтение документов — сцена без места
- [low] `scenes.no_place` `mts-kharkov-37-ru/scene/vzaimodeystvie-s-tsvetom` Взаимодействие с Цветом — сцена без места
- [low] `scenes.no_place` `mts-kharkov-37-ru/scene/tungusskiy-meteorit` Допустимая дезинформация: Тунгусский метеорит — сцена без места
- [low] `scenes.no_place` `mts-kharkov-37-ru/scene/radiatsiya` Недопустимая дезинформация: радиация — сцена без места

### Аутофагия (`autofagiya-ru/scenario/autofagiya`) — 13

- [low] `scenes.no_outcome` `autofagiya-ru/scene/morozilnaya-kamera` Морозильная камера — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/uzhin-v-obedennom-zale` Ужин в обеденном зале — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/razgovor-s-lyudvigom` Разговор с Людвигом — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/gloriya-reynbek` Глория Рейнбек — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/kayuta-121` Каюта 121: Доктор Айзек Уинтроп — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/kayuta-124` Каюта 124: Мистер и миссис Мопен — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/bagazhnoe-otdelenie` Багажное отделение — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/voskhod-zloveshchey-luny` Восход зловещей луны — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/ko-dnu-vmeste-s-korablem` Ко дну вместе с кораблём? — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/vyzhivshiy` Выживший — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/slomannaya-pregrada` Сломанная преграда — сцена без итога
- [low] `scenes.no_outcome` `autofagiya-ru/scene/opportunistka` Оппортунистка — сцена без итога
- [low] `scenes.no_people` `autofagiya-ru/scene/bagazhnoe-otdelenie` Багажное отделение — сцена без участников

### Преображение рифа Хаттерас (`fears-sharp-little-needles-en/scenario/hatteras-reef`) — 13

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-hospital-and-coroner` Больница и коронер — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-obx-rg` Группа восстановления OBX — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-video-of-the-attack` Видео нападения — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-other-sources` Другие источники морских исследований — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-locals` Местные жители — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-it-came-from-the-deep` Оно пришло из глубин! — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hatteras-the-reef` Риф — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hatteras-strange-catch` Странный улов — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hatteras-video-of-the-attack` Видео нападения — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hatteras-other-sources` Другие источники морских исследований — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hatteras-it-came-from-the-deep` Оно пришло из глубин! — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hatteras-the-sapeh` Сапех — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/hatteras-video-of-the-attack` Видео нападения — сцена без места

### Исследовательский центр Уинока-Пойнт (`fears-sharp-little-needles-en/scenario/winoka`) — 13

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-researching` Поиск сведений об Уинока-Пойнт — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-south-newberry` Посещение Саут-Ньюберри — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-getting-there` Как добраться до Уинока-Пойнт — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-welcome` Добро пожаловать на Уинока-Пойнт — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-elevator-shaft` Лифтовая шахта — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-sub-level-1` Первый подземный уровень — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-security-door` Защитная дверь и сообщения из темноты — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-opening-the-door` Открытие защитной двери — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/winoka-sub-level-2` Второй подземный уровень — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/winoka-getting-there` Как добраться до Уинока-Пойнт — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/winoka-welcome` Добро пожаловать на Уинока-Пойнт — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/winoka-sub-level-1` Первый подземный уровень — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/winoka-sub-level-2` Второй подземный уровень — сцена без участников

### Любовь матери (`mothers-love-ru/scenario/lyubov-materi`) — 13

- [low] `scenes.no_outcome` `mothers-love-ru/scene/doktor-rouli-marsh` Доктор Роули Марш — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/orden-dagona` Эзотерический орден Дагона — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/affinazhnyy-zavod` Аффинажный завод Марша — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/bank-morskikh-torgovtsev` Банк морских торговцев Ост-Индии — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/gavan` Гавань — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/otel-dom-gilmana` Отель «Дом Гилмана» — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/polzovanie-telefonom` Пользование телефоном — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/mestnye-deti` Местные дети — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/pesn-shoggotov` Песнь шогготов — сцена без итога
- [low] `scenes.no_outcome` `mothers-love-ru/scene/propavshiy-politseyskiy` Пропавший полицейский — сцена без итога
- [low] `scenes.no_people` `mothers-love-ru/scene/mestnye-deti` Местные дети — сцена без участников
- [low] `scenes.no_people` `mothers-love-ru/scene/pesn-shoggotov` Песнь шогготов — сцена без участников
- [low] `scenes.no_people` `mothers-love-ru/scene/dom-siska` Дом Сиска — сцена без участников

### Скрюченный домище (`osobnyaki-bezumiya-ru/scenario/crooked-manse`) — 13

- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/crooked-preliminary-research` Предварительное расследование — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/crooked-at-the-cemetery` Кладбище — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/crooked-inside-the-house` Что за шум? — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/crooked-ground-floor` Первый этаж — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/crooked-attic` Чердак — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/crooked-cellars` Подвалы — сцена без итога
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/crooked-preliminary-research` Предварительное расследование — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/crooked-around-the-house` Вокруг дома — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/crooked-inside-the-house` Что за шум? — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/crooked-ground-floor` Первый этаж — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/crooked-second-floor` Второй этаж — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/crooked-attic` Чердак — сцена без участников
- [low] `scenes.no_place` `osobnyaki-bezumiya-ru/scene/crooked-preliminary-research` Предварительное расследование — сцена без места

### Язвы (`fears-sharp-little-needles-en/scenario/sores`) — 12

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-acquaintances` Беседы со знакомыми Терезы — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-calling-the-hospital` Звонок в больницу — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-local-history-research` Исследование местной истории — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-speaking-to-the-librarian` Разговор с библиотекаршей — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-theresa-house` Осмотр дома Терезы Смит — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-their-turn` Теперь их очередь — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-involving-the-police` Обращение в полицию — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/sores-breaking-into-the-library` Проникновение в библиотеку — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/sores-local-history-research` Исследование местной истории — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/sores-their-turn` Теперь их очередь — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/sores-calling-the-hospital` Звонок в больницу — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/sores-their-turn` Теперь их очередь — сцена без места

### Секретный код (`osobnyaki-bezumiya-ru/scenario/code-secret-code`) — 12

- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/code-moving-silhouette` Движущийся силуэт — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/code-same-place-other-time` То же место, другое время — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/code-wolf-pack` Стая волков — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/code-who-is-there` Кто здесь? — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/code-madman` Безумец — сцена без итога
- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/code-visitors` Гости — сцена без итога
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/code-ordinary-day` Самый обычный день — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/code-chrono-anomalies` Хроноаномалии — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/code-same-place-other-time` То же место, другое время — сцена без участников
- [low] `scenes.no_place` `osobnyaki-bezumiya-ru/scene/code-meeting-connolly` Знакомство с Коннолли — сцена без места
- [low] `scenes.no_place` `osobnyaki-bezumiya-ru/scene/code-letter` Завязка: письмо — сцена без места
- [low] `scenes.no_place` `osobnyaki-bezumiya-ru/scene/code-ordinary-day` Самый обычный день — сцена без места

### Сбил и скрылся (`fears-sharp-little-needles-en/scenario/hit-and-run`) — 11

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-the-accident` Сбил и скрылся — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-charges` Обвинения — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-phone-call` Телефонный звонок — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-dual-pool-motel` Мотель «Дуал Пул» — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-involving-police` Вовлечение полиции — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-police-and-hospital` Поиски Джебедайи: полиция и больница — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-millersburg` Городок Миллерсберг — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-cabin` Хижина Джебедайи — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/hit-and-run-encounters` Встречи с Воплощением — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hit-and-run-charges` Обвинения — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/hit-and-run-police-and-hospital` Поиски Джебедайи: полиция и больница — сцена без участников

### Глава III. Замок Тёмный (`griby-s-yuggota-ru/scenario/castle-dark`) — 11

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-research` Исследование до отъезда — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-drovosna` Село Дровосна — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-approach` Замок Гауптмана: ворота и двор — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-residence-ground` Резиденция: первый этаж — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-study` Резиденция: второй этаж и кабинет барона — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-bedroom` Спальня барона — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-catacombs` Подвал и катакомбы: склеп, мастерская, камера пыток — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-alchemical-laboratory` Алхимическая лаборатория — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-soldiers-chamber` Камера с погибшими солдатами — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-escape-tunnel` Потайной туннель — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/castle-tower` Башня и обсерватория — сцена без участников

### Черноводный ручей (`chernovodnyy-ruchey-ru/scenario/blackwater-chernovodnyy-ruchey`) — 10

- [low] `scenes.no_outcome` `chernovodnyy-ruchey-ru/scene/blackwater-ruchey` Ручей и плотина — сцена без итога
- [low] `scenes.no_outcome` `chernovodnyy-ruchey-ru/scene/blackwater-les` Лес — сцена без итога
- [low] `scenes.no_outcome` `chernovodnyy-ruchey-ru/scene/blackwater-raskopki` Раскопки — сцена без итога
- [low] `scenes.no_outcome` `chernovodnyy-ruchey-ru/scene/blackwater-vysokhshee-ruslo` Высохшее русло ручья — сцена без итога
- [low] `scenes.no_outcome` `chernovodnyy-ruchey-ru/scene/blackwater-peshchera` Пещера — сцена без итога
- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/blackwater-lager-roudsa` Лагерь Роудса — сцена без участников
- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/blackwater-raskopki` Раскопки — сцена без участников
- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/blackwater-vysokhshee-ruslo` Высохшее русло ручья — сцена без участников
- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/blackwater-peshchera` Пещера — сцена без участников
- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/blackwater-vzryv-peshchery` Взорвать пещеру динамитом — сцена без участников

### Tormiss CRD, модель Z-17 (`fears-sharp-little-needles-en/scenario/tormiss`) — 10

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/tormiss-funeral-home` Похоронный дом «Цайлер-Дэнворт» — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/tormiss-official-channels` Официальные каналы — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/tormiss-doctor-patient` Нарушение врачебной тайны — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/tormiss-second-sublevel` Второй подземный уровень — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/tormiss-crossing-the-cultists` Столкновение с культистами — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/tormiss-success-and-failure` Успех и провал — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/tormiss-official-channels` Официальные каналы — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/tormiss-official-channels` Официальные каналы — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/tormiss-doctor-patient` Нарушение врачебной тайны — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/tormiss-crossing-the-cultists` Столкновение с культистами — сцена без места

### Подводное течение (`fears-sharp-little-needles-en/scenario/undertow`) — 10

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/undertow-neighbors` Соседи — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/undertow-dog-returns` Собака возвращается — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/undertow-beach-at-night` Ночной пляж — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/undertow-novel` Роман «Подводное течение» — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/undertow-beach-at-night` Ночной пляж — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/undertow-pale-man` Бледный человек — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/undertow-novel` Роман «Подводное течение» — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/undertow-finding-hayes` Поиски Хейза — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/undertow-dog-returns` Собака возвращается — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/undertow-pale-man` Бледный человек — сцена без места

### Призрак (`prizrak-ru/scenario/prizrak`) — 9

- [low] `scenes.no_people` `prizrak-ru/scene/sudy-i-politsiya` Высшие суды и Центральный полицейский участок — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/ruiny-chasovni` Часовня созерцания и церковь Господа нашего, Дарующего тайны — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/podval-chasovni` Подвал часовни — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/dom-snaruzhi` Дом на ул. Шиф, 20 — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/pervyy-etazh` Первый этаж — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/verkhniy-etazh` Верхний этаж — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/cherdak` Чердак — сцена без участников
- [low] `scenes.no_people` `prizrak-ru/scene/pobeda` Сыщики победили! — сцена без участников
- [low] `scenes.no_place` `prizrak-ru/scene/priglashenie` Приглашение — сцена без места

### Террор (`terror-ru/scenario/terror`) — 9

- [low] `scenes.no_outcome` `terror-ru/scene/kvartira-babelya` Пропавший экипаж: Исаак Бабель — сцена без итога
- [low] `scenes.no_outcome` `terror-ru/scene/zvonok-vyshinskomu` Пропавший экипаж: звонок Вышинскому — сцена без итога
- [low] `scenes.no_outcome` `terror-ru/scene/skotoboynya` Скотобойня — сцена без итога
- [low] `scenes.no_outcome` `terror-ru/scene/akademiya-nauk` Академия наук СССР — сцена без итога
- [low] `scenes.no_people` `terror-ru/scene/materialy-dela` Материалы дела — сцена без участников
- [low] `scenes.no_people` `terror-ru/scene/kvartira-kalinina` Пропавший экипаж: Михаил Калинин — сцена без участников
- [low] `scenes.no_people` `terror-ru/scene/poiski-chervyakova` Доктор Червяков: поиски — сцена без участников
- [low] `scenes.no_place` `terror-ru/scene/dopros` Допрос — сцена без места
- [low] `scenes.no_place` `terror-ru/scene/poiski-chervyakova` Доктор Червяков: поиски — сцена без места

### Диссоциация (`fears-sharp-little-needles-en/scenario/dissociation`) — 8

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/dissociation-examining-vessels` Осмотр сосудов (сейчас и позже) — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/dissociation-test-subjects` Испытуемые — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/dissociation-scientist` Учёный — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/dissociation-survivors` Выжившие — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/dissociation-dreamscape` Мир грёз — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/dissociation-investigation-one` Расследование (Аниак) — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/dissociation-examining-vessels` Осмотр сосудов (сейчас и позже) — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/dissociation-survivors` Выжившие — сцена без места

### Не вызывай того, чего не сможешь усмирить (`fears-sharp-little-needles-en/scenario/do-not-call`) — 8

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-shark-week` Неделя акул — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-similar-stories` Похожие истории — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-out-to-sea` В открытое море — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-coming-storm` Надвигающаяся буря — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-the-coyote` «Койот» — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-the-monster` Кровавая плата — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/do-not-call-outrun` Попытка уйти от чудовища — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/do-not-call-similar-stories` Похожие истории — сцена без участников

### Глава 10. От Бомбея до границы Непала (`lokhmotya-korolya-ru/scenario/thousand-miles`) — 8

- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/india-coming-of-the-king` Приход Короля; сны — сцена без итога
- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/india-leaving-bombay-by-train` Отъезд из Бомбея на поезде — сцена без итога
- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/india-rail-journey` Железнодорожное путешествие — сцена без итога
- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/india-equipping-for-nepal` Экипировка для путешествия в Непал — сцена без итога
- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/india-italian-expedition` Итальянская экспедиция — сцена без итога
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/india-coming-of-the-king` Приход Короля; сны — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/india-rail-journey` Железнодорожное путешествие — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/india-riot-in-benares` Беспорядки в Бенаресе — сцена без участников

### Под землёй и над землёй (`pod-zemlyoy-i-nad-zemlyoy-ru/scenario/pod-zemlyoy-i-nad-zemlyoy`) — 8

- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/effekt-mertvoy-vody` Эффект мёртвой воды — сцена без итога
- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/vstrecha-s-okhotnikom` Встреча с охотником — сцена без итога
- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/pribytie-rebenka` Прибытие ребёнка в Янкылму — сцена без итога
- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/domovoy` Домовой — сцена без итога
- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/malenkiy-khozyain` Маленький хозяин — сцена без итога
- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/pokhod-na-savynkan` Поход на савынкан — сцена без итога
- [low] `scenes.no_outcome` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/okhota-na-studentov` Охота на студентов — сцена без итога
- [low] `scenes.no_people` `pod-zemlyoy-i-nad-zemlyoy-ru/scene/vremennaya-anomaliya` Временная аномалия — сцена без участников

### Грань тьмы (`starter-edge-of-darkness-ru/scenario/edge-of-darkness`) — 8

- [low] `scenes.no_outcome` `starter-edge-of-darkness-ru/scene/additional-motivation` Дополнительная мотивация — сцена без итога
- [low] `scenes.no_outcome` `starter-edge-of-darkness-ru/scene/maggie-body` Тело в лесу — сцена без итога
- [low] `scenes.no_people` `starter-edge-of-darkness-ru/scene/box-contents` Содержимое ящичка — сцена без участников
- [low] `scenes.no_people` `starter-edge-of-darkness-ru/scene/death-of-marion-allen` Смерть Мариона Аллена — сцена без участников
- [low] `scenes.no_people` `starter-edge-of-darkness-ru/scene/what-next` Что дальше? — сцена без участников
- [low] `scenes.no_people` `starter-edge-of-darkness-ru/scene/old-farm` Старая ферма — сцена без участников
- [low] `scenes.no_people` `starter-edge-of-darkness-ru/scene/farmhouse-rooms` Гостиная и задняя комната — сцена без участников
- [low] `scenes.no_people` `starter-edge-of-darkness-ru/scene/cellar` Погреб и сундук — сцена без участников

### Безымянный туман (`bezymyannyy-tuman-ru/scenario/bezymyannyy-tuman`) — 7

- [high] `clues.empty` `bezymyannyy-tuman-ru/handout/foto-rene` Фотография Рене — раздатка без текста и картинки
- [high] `clues.empty` `bezymyannyy-tuman-ru/handout/simvol-shchita-akhilla` Символ «Щита Ахилла» — раздатка без текста и картинки
- [high] `clues.empty` `bezymyannyy-tuman-ru/handout/foto-derrika-yorka` Фотография Деррика Йорка — раздатка без текста и картинки
- [low] `scenes.no_people` `bezymyannyy-tuman-ru/scene/magazin-derrika-yorka` Магазин Деррика Йорка — сцена без участников
- [low] `scenes.no_people` `bezymyannyy-tuman-ru/scene/publichnaya-biblioteka` Бостонская публичная библиотека — сцена без участников
- [low] `scenes.no_people` `bezymyannyy-tuman-ru/scene/gorodskoy-arkhiv` Городской архив — сцена без участников
- [low] `scenes.no_people` `bezymyannyy-tuman-ru/scene/elektromagnitnaya-anomaliya` Электромагнитная аномалия — сцена без участников

### Страх разлуки (`fears-sharp-little-needles-en/scenario/separation-anxiety`) — 7

- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/separation-work-computer` Рабочий компьютер Би-Би — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/separation-missing-persons-research` Поиск похожих пропавших — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/separation-mythos-research` Поиск в источниках о Мифах — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/separation-farm-connections` Связь с фермой Фарнсуортов — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/separation-approaching-covertly` Скрытное приближение — сцена без участников
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/separation-missing-persons-research` Поиск похожих пропавших — сцена без места
- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/separation-mythos-research` Поиск в источниках о Мифах — сцена без места

### Особое меню (`fears-sharp-little-needles-en/scenario/special-menu`) — 7

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/special-menu-internet` Интернет — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/special-menu-crime-scene` Место преступления — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/special-menu-staff-interviews` Опросы: сотрудники — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/special-menu-customer-interviews` Опросы: посетители — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/special-menu-police-interviews` Опросы: полиция — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/special-menu-crime-scene` Место преступления — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/special-menu-brent-apartment` Встреча с Брентом «Толстозадым» Ходиаком — сцена без участников

### Этап четвёртый: Каркоза (`mify-hastura-ru/scenario/stage-four-carcosa`) — 7

- [low] `scenes.no_people` `mify-hastura-ru/scene/disappearance` Исчезновение — сцена без участников
- [low] `scenes.no_people` `mify-hastura-ru/scene/search` Поиск — сцена без участников
- [low] `scenes.no_people` `mify-hastura-ru/scene/arrival` Прибытие и исследование — сцена без участников
- [low] `scenes.no_people` `mify-hastura-ru/scene/palace-rescue` Дворец: спасение пропавшего — сцена без участников
- [low] `scenes.no_place` `mify-hastura-ru/scene/disappearance` Исчезновение — сцена без места
- [low] `scenes.no_place` `mify-hastura-ru/scene/search` Поиск — сцена без места
- [low] `scenes.no_place` `mify-hastura-ru/scene/transport` Транспорт — сцена без места

### Эликсир жизни (`eliksir-zhizni-ru/scenario/eliksir-zhizni`) — 6

- [high] `clues.empty` `eliksir-zhizni-ru/handout/foto-medalona` Фотография медальона — раздатка без текста и картинки
- [low] `scenes.no_outcome` `eliksir-zhizni-ru/scene/khronologiya-kordeliya` Хронология: смерть Корделии Хамфри — сцена без итога
- [low] `scenes.no_outcome` `eliksir-zhizni-ru/scene/khronologiya-napadenie-gonchey` Хронология: ночное нападение гончей — сцена без итога
- [low] `scenes.no_people` `eliksir-zhizni-ru/scene/les-salema` Лес Салема — сцена без участников
- [low] `scenes.no_people` `eliksir-zhizni-ru/scene/razgadka-shifra` Ключ и шифр — сцена без участников
- [low] `scenes.no_people` `eliksir-zhizni-ru/scene/kladbishche` Кладбище — сцена без участников

### Призраки Рейвенскара (`fears-sharp-little-needles-en/scenario/ravenscar`) — 6

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/ravenscar-internet` Поиск в Интернете — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/ravenscar-calling-authorities` Вызов властей — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/ravenscar-abandoned-houses` Заброшенные дома — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/ravenscar-raven-hall` Рейвен-холл — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/ravenscar-internet` Поиск в Интернете — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/ravenscar-calling-authorities` Вызов властей — сцена без участников

### Глава 3. Англия (`masks-of-nyarlathotep-en/scenario/england`) — 6

- [low] `pages.gap` страницы без записей: физ. 191
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/england-arriving` Прибытие в Англию — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/england-asking-about-elias` Расспросы о Джексоне Элиасе — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/england-researching-penhew-foundation` Сведения о Фонде Пэнхью — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/england-gavigans-flat-break-in` Обыск квартиры Гавигана — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/england-limehouse-locals` Лаймхаус: расспросы местных — сцена без участников

### Парк развлечений (`park-razvlecheniy-ru/scenario/park-razvlecheniy`) — 6

- [low] `scenes.no_outcome` `park-razvlecheniy-ru/scene/administratsiya` Разговор с руководством парка — сцена без итога
- [low] `scenes.no_outcome` `park-razvlecheniy-ru/scene/domiki-rabotnikov` Обыск домиков работников — сцена без итога
- [low] `scenes.no_outcome` `park-razvlecheniy-ru/scene/napadenie-v-kostyume-khoui` Нападение призрака в костюме пса Хоуи — сцена без итога
- [low] `scenes.no_outcome` `park-razvlecheniy-ru/scene/gorod-aguem` Город Агуэм — сцена без итога
- [low] `scenes.no_outcome` `park-razvlecheniy-ru/scene/ubezhat-iz-parka` Убежать из парка — сцена без итога
- [low] `scenes.no_outcome` `park-razvlecheniy-ru/scene/arestovat-biglya` Арестовать Джереми Бигля — сцена без итога

### Погоня в поезде (`pogonya-v-poezde-ru/scenario/pogonya-v-poezde`) — 6

- [low] `scenes.no_outcome` `pogonya-v-poezde-ru/scene/pryzhok-iz-poezda` Прыжок из поезда — сцена без итога
- [low] `scenes.no_outcome` `pogonya-v-poezde-ru/scene/zhertvy` Убитые монстром или в крушении — сцена без итога
- [low] `scenes.no_outcome` `pogonya-v-poezde-ru/scene/upravlenie-poezdom` Управление поездом — сцена без итога
- [low] `scenes.no_people` `pogonya-v-poezde-ru/scene/presledovanie` Преследование — сцена без участников
- [low] `scenes.no_people` `pogonya-v-poezde-ru/scene/pogonya-po-kryshe` Погоня по крыше — сцена без участников
- [low] `scenes.no_people` `pogonya-v-poezde-ru/scene/pryzhok-iz-poezda` Прыжок из поезда — сцена без участников

### Аукцион (`auktsion-ru/scenario/auktsion`) — 5

- [low] `scenes.no_outcome` `auktsion-ru/scene/nochnaya-progulka` Ночная прогулка — сцена без итога
- [low] `scenes.no_outcome` `auktsion-ru/scene/lekar` Лекарь — сцена без итога
- [low] `scenes.no_outcome` `auktsion-ru/scene/labirint-tunneley` Лабиринт туннелей — сцена без итога
- [low] `scenes.no_outcome` `auktsion-ru/scene/itogi` Итоги сценария — сцена без итога
- [low] `scenes.no_people` `auktsion-ru/scene/kvartira-khunderpresta` Квартира Хундерпреста — сцена без участников

### Вечер поэзии (`fears-sharp-little-needles-en/scenario/poetry-night`) — 5

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/poetry-night-becoming-part-of-carcosa` Становление частью Каркозы — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/poetry-night-store-room` Кладовая — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/poetry-night-the-betrayal` Предательство — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/poetry-night-return` Возвращение на Землю — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/poetry-night-return` Возвращение на Землю — сцена без участников

### Воскрешение (`fears-sharp-little-needles-en/scenario/resurrection`) — 5

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/resurrection-internet` Поиски в интернете — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/resurrection-internet` Поиски в интернете — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/resurrection-campus-security` Охрана кампуса — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/resurrection-police` Разговор с полицией — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/resurrection-haverman-house` Дом Хавермана — сцена без участников

### В ожидании рождения (`fears-sharp-little-needles-en/scenario/waiting-to-be-born`) — 5

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/waiting-jake-brinkman` Смерть Джейка Бринкмана — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/waiting-new-life-center` Клиника «Новая жизнь» — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/waiting-underground-facility` Подземный комплекс — сцена без итога
- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/waiting-regora-wrath` Гнев Регоры — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/waiting-facility` Осмотр клиники — сцена без участников

### Глава VII. В гавани: часть II (`griby-s-yuggota-ru/scenario/by-the-bay-2`) — 5

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-morning-newspaper` Утренняя газета — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-research-station-queue` Исследовательский центр — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-restricted-area` Запретная территория — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-dieter-quarters-search` Жилище доктора Дитера и тайная операционная — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-dieter-past` Прошлое доктора Дитера — сцена без участников

### Среди древних деревьев (`keeper-rulebook-ru/scenario/trees-amidst-the-ancient-trees`) — 5

- [low] `scenes.no_people` `keeper-rulebook-ru/scene/trees-shootout-site` Место перестрелки — сцена без участников
- [low] `scenes.no_people` `keeper-rulebook-ru/scene/trees-first-night` День 1. Первая ночь — сцена без участников
- [low] `scenes.no_people` `keeper-rulebook-ru/scene/trees-forest-day-2` День 2. Дорога через лес — сцена без участников
- [low] `scenes.no_people` `keeper-rulebook-ru/scene/trees-forest-day-3` День 3. Дорога через лес — сцена без участников
- [low] `scenes.no_people` `keeper-rulebook-ru/scene/trees-artists-camp` День 3. Лагерь художников — сцена без участников

### Месяц ночи (`mesyats-nochi-ru/scenario/mesyats-nochi`) — 5

- [low] `scenes.no_people` `mesyats-nochi-ru/scene/sny-silly` Сны Силлы — сцена без участников
- [low] `scenes.no_people` `mesyats-nochi-ru/scene/opernyy-teatr-zakryt` Оперный театр — сцена без участников
- [low] `scenes.no_people` `mesyats-nochi-ru/scene/noch-31-oktyabrya` Ночь перед Месяцем ночи — сцена без участников
- [low] `scenes.no_people` `mesyats-nochi-ru/scene/v-glubiny` В глубины — сцена без участников
- [low] `scenes.no_people` `mesyats-nochi-ru/scene/trotil` Тротил — сцена без участников

### Сон № 7 (`number-7-dream-en/scenario/number-7-dream`) — 5

- [low] `scenes.no_outcome` `number-7-dream-en/scene/the-bus` Автобус — сцена без итога
- [low] `scenes.no_people` `number-7-dream-en/scene/enlightened-website` Сайт «Просветлённых» — сцена без участников
- [low] `scenes.no_people` `number-7-dream-en/scene/last-warning` Последнее предупреждение — сцена без участников
- [low] `scenes.no_people` `number-7-dream-en/scene/live-or-let-die` Жить или умереть — сцена без участников
- [low] `scenes.no_people` `number-7-dream-en/scene/the-escape` Побег — сцена без участников

### Мистер Корбитт (`osobnyaki-bezumiya-ru/scenario/corbitt-mr-corbitt`) — 5

- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/corbitt-newspapers` Заметки из газет — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/corbitt-vegetable-garden` Огород — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/corbitt-first-floor` Первый этаж: гостиная — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/corbitt-second-floor` Второй этаж — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/corbitt-laboratory` Подвал: лаборатория — сцена без участников

### Проклятие Ганеши (`proklyatie-ganeshi-ru/scenario/proklyatie-ganeshi`) — 5

- [low] `scenes.no_people` `proklyatie-ganeshi-ru/scene/vkhod-v-khram` Вход в храм — сцена без участников
- [low] `scenes.no_people` `proklyatie-ganeshi-ru/scene/zagadka-statui` Загадка статуи — сцена без участников
- [low] `scenes.no_people` `proklyatie-ganeshi-ru/scene/spusk-v-podzemele` Спуск в подземелье — сцена без участников
- [low] `scenes.no_people` `proklyatie-ganeshi-ru/scene/khranilishche` Хранилище — сцена без участников
- [low] `scenes.no_people` `proklyatie-ganeshi-ru/scene/tonnel-s-lovushkami` Тоннель с ловушками — сцена без участников

### Анленд (`fears-sharp-little-needles-en/scenario/unland`) — 4

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/unland-house-of-hilarity` Дом смеха и Зеркальный зал — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/unland-involving` Вовлечение сыщиков — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/unland-approaching` Приближение к «Анленду» — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/unland-big-twister` Сквозь нити «Большого твистера» — сцена без участников

### Глава VI. В гавани: часть I (`griby-s-yuggota-ru/scenario/by-the-bay-1`) — 4

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-lang-fu-research` Расспросы о Лэнг-Фу — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-pearl-beach-research` Сведения о Жемчужном пляже — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-pearl-beach-scouting` Жемчужный пляж днём — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/bay-pearl-beach-aftermath` Жемчужный пляж после обряда — сцена без участников

### Глава II. Нечто в колодце (`griby-s-yuggota-ru/scenario/thing-in-the-well`) — 4

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/well-newspaper-archive` Газетный архив — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/well-additional-clippings` Газетные вырезки о Корнуоллисах — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/well-tower-laboratory` Лаборатория в башне — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/well-all-hearts-cemetery` Кладбище Олл Хартс — сцена без участников

### Хэллоуин в Данвиче (`hellouin-v-danviche-ru/scenario/khellouin-v-danviche`) — 4

- [low] `scenes.no_people` `hellouin-v-danviche-ru/scene/beg-v-meshkakh` Бег в мешках — сцена без участников
- [low] `scenes.no_people` `hellouin-v-danviche-ru/scene/poisk-pomoshchi` Поиск помощи — сцена без участников
- [low] `scenes.no_people` `hellouin-v-danviche-ru/scene/plan` План — сцена без участников
- [low] `scenes.no_people` `hellouin-v-danviche-ru/scene/sbor-pripasov` Сбор припасов — сцена без участников

### Идол Тота (`idol-tota-ru/scenario/idol-tota`) — 4

- [low] `scenes.no_people` `idol-tota-ru/scene/rassledovanie-prodolzhaetsya` Расследование продолжается — сцена без участников
- [low] `scenes.no_people` `idol-tota-ru/scene/miskatonik-biblioteka` Мискатоникский университет: библиотека — сцена без участников
- [low] `scenes.no_people` `idol-tota-ru/scene/boston-globe` «Бостон Глоуб» — сцена без участников
- [low] `scenes.no_people` `idol-tota-ru/scene/epilog` Эпилог — сцена без участников

### Каникулы в Иннсмуте (`kanikuly-v-innsmute-ru/scenario/kanikuly-v-innsmute`) — 4

- [low] `scenes.no_people` `kanikuly-v-innsmute-ru/scene/tserkov-dnem` Церковь Тайного ордена Дагона днём — сцена без участников
- [low] `scenes.no_people` `kanikuly-v-innsmute-ru/scene/avtobus-propal` Автобус пропал — сцена без участников
- [low] `scenes.no_people` `kanikuly-v-innsmute-ru/scene/zavod-vkhody` Заброшенный золото-плавильный завод: входы — сцена без участников
- [low] `scenes.no_people` `kanikuly-v-innsmute-ru/scene/zavod-liteynaya` Литейная — сцена без участников

### Когда зажигаются костры (`kogda-zazhigayutsya-kostry-ru/scenario/kogda-zazhigayutsya-kostry`) — 4

- [low] `scenes.no_people` `kogda-zazhigayutsya-kostry-ru/scene/mesto-gde-oborvalas-zhizn` Место, где оборвалась жизнь — сцена без участников
- [low] `scenes.no_people` `kogda-zazhigayutsya-kostry-ru/scene/mesto-v-kotorom-nado-sdelat-vybor` Место, в котором надо сделать выбор — сцена без участников
- [low] `scenes.no_people` `kogda-zazhigayutsya-kostry-ru/scene/chistaya-zemlya` «Чистая земля» — сцена без участников
- [low] `scenes.no_people` `kogda-zazhigayutsya-kostry-ru/scene/perezhivshie` Пережившие — сцена без участников

### Погасший маяк (`lightless-beacon-ru/scenario/lightless-beacon`) — 4

- [low] `scenes.no_people` `lightless-beacon-ru/scene/beacon-following-tracks` Если идти по следам — сцена без участников
- [low] `scenes.no_people` `lightless-beacon-ru/scene/beacon-keepers-house` Дом смотрителя маяка — сцена без участников
- [low] `scenes.no_people` `lightless-beacon-ru/scene/beacon-kitchen` Кухня — сцена без участников
- [low] `scenes.no_people` `lightless-beacon-ru/scene/beacon-technical-room` Техническое помещение маяка — сцена без участников

### Глава 5. Каркоза на Земле (`lokhmotya-korolya-ru/scenario/carcosa`) — 4

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/carcosa-arrival` Каркоза на Земле — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/carcosa-city-gate` 1. Городские ворота — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/carcosa-esplanade` 2. Эспланада — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/carcosa-canal-bridge` 3. Мост через канал — сцена без участников

### Глава 3. Курган Спрингер Маунд и канал (`lokhmotya-korolya-ru/scenario/springer-mound`) — 4

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/springer-on-springer-mound` Курган Спрингер Маунд — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/springer-exploring-bacon-house` Исследование дома Бэкона — сцена без участников
- [low] `scenes.no_place` `lokhmotya-korolya-ru/scene/springer-highsmith-letter` Письмо от доктора Хайсмита — сцена без места
- [low] `scenes.no_place` `lokhmotya-korolya-ru/scene/springer-gresty-first-letter` Первое письмо Уилфреда Грести — сцена без места

### Дом Мемфиса (`osobnyaki-bezumiya-ru/scenario/memphis-house-of-memphis`) — 4

- [low] `scenes.no_outcome` `osobnyaki-bezumiya-ru/scene/memphis-staying-on-track` Как не сбиться со следа — сцена без итога
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/memphis-library` Библиотека — сцена без участников
- [low] `scenes.no_people` `osobnyaki-bezumiya-ru/scene/memphis-conclusions` Пора делать выводы — сцена без участников
- [low] `scenes.no_place` `osobnyaki-bezumiya-ru/scene/memphis-staying-on-track` Как не сбиться со следа — сцена без места

### Остров лучезарной надежды (`ostrov-luchezarnoy-nadezhdy-ru/scenario/ostrov-luchezarnoy-nadezhdy`) — 4

- [low] `scenes.no_outcome` `ostrov-luchezarnoy-nadezhdy-ru/scene/stoyanka` Стоянка потерпевших кораблекрушение — сцена без итога
- [low] `scenes.no_outcome` `ostrov-luchezarnoy-nadezhdy-ru/scene/peshchera-s-sokrovishchami` Пещера с сокровищами — сцена без итога
- [low] `scenes.no_people` `ostrov-luchezarnoy-nadezhdy-ru/scene/peshchera-s-sokrovishchami` Пещера с сокровищами — сцена без участников
- [low] `scenes.no_people` `ostrov-luchezarnoy-nadezhdy-ru/scene/kladbishche-korabley` Кладбище кораблей — сцена без участников

### Попались! (`popalis-ru/scenario/popalis`) — 4

- [low] `scenes.no_outcome` `popalis-ru/scene/eshche-odno-deltse` Ещё одно дельце — сцена без итога
- [low] `scenes.no_outcome` `popalis-ru/scene/ozhidanie` Ожидание — сцена без итога
- [low] `scenes.no_place` `popalis-ru/scene/promedlenie` Промедление — сцена без места
- [low] `scenes.no_place` `popalis-ru/scene/smylis` Смылись? — сцена без места

### Служители озера (`dveri-vo-tmu-ru/scenario/servants-of-the-lake`) — 3

- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/lake-arriving` Прибытие в мотель — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/lake-rooms` Номера — сцена без участников
- [low] `scenes.no_place` `dveri-vo-tmu-ru/scene/lake-involving` Вовлечение сыщиков — сцена без места

### Pulvis et Umbra Sumus (`fears-sharp-little-needles-en/scenario/pulvis-et-umbra-sumus`) — 3

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/pulvis-confronting-joseph` Столкновение с Джозефом — сцена без итога
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/pulvis-from-the-airport` Из аэропорта — сцена без участников
- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/pulvis-calling-for-help` Призыв о помощи — сцена без участников

### Вот так головоломка! (`keepers-companion-en/scenario/what-a-puzzler`) — 3

- [low] `scenes.no_place` `keepers-companion-en/scene/puzzler-putting-the-pieces-together` Собирая кусочки — сцена без места
- [low] `scenes.no_place` `keepers-companion-en/scene/puzzler-the-pale-man` Бледный человек — сцена без места
- [low] `scenes.no_place` `keepers-companion-en/scene/puzzler-lost-in-art` Потерянные в картине — сцена без места

### Глава 4. Полёт на север (`lokhmotya-korolya-ru/scenario/flight-north`) — 3

- [low] `scenes.no_place` `lokhmotya-korolya-ru/scene/flight-gresty-second-letter` Второе письмо Грести — сцена без места
- [low] `scenes.no_place` `lokhmotya-korolya-ru/scene/flight-roby-note-to-delia` Записка Роби к Делии — сцена без места
- [low] `scenes.no_place` `lokhmotya-korolya-ru/scene/flight-bacon-obituary` Некролог Бэкона — сцена без места

### Глава 6. Разговоры о Гоатсвуде (`lokhmotya-korolya-ru/scenario/talk-of-goatswood`) — 3

- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/talk-hawksmoor-churches` Церкви Хоксмура — сцена без итога
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/talk-the-gap-year` Перерыв: год между Шотландией и Грести — сцена без участников
- [low] `scenes.no_place` `lokhmotya-korolya-ru/scene/talk-the-gap-year` Перерыв: год между Шотландией и Грести — сцена без места

### Глава 11. Дорога в Дракмар (`lokhmotya-korolya-ru/scenario/to-drakmar`) — 3

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/drakmar-inside-the-monastery` Внутри монастыря — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/drakmar-toward-drakmar` В сторону Дракмара — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/drakmar-arriving-at-drakmar` Прибытие в Дракмар — сцена без участников

### Пустые страницы (`pustye-stranitsy-ru/scenario/pustye-stranitsy`) — 3

- [low] `scenes.no_people` `pustye-stranitsy-ru/scene/kolodets` Колодец — сцена без участников
- [low] `scenes.no_people` `pustye-stranitsy-ru/scene/poiski-v-arkhivakh` Сведения о Бернвуд-Холле — сцена без участников
- [low] `scenes.no_people` `pustye-stranitsy-ru/scene/perenos` Перенос в Бернвуд-Холл — сцена без участников

### Одинокая нить (`tri-koshmarnykh-vechera-ru/scenario/thread-odinokaya-nit`) — 3

- [low] `scenes.no_people` `tri-koshmarnykh-vechera-ru/scene/thread-obysk-khizhiny` Хижина: обыск дома — сцена без участников
- [low] `scenes.no_people` `tri-koshmarnykh-vechera-ru/scene/thread-snaruzhi` Снаружи: сад и автомобили — сцена без участников
- [low] `scenes.no_people` `tri-koshmarnykh-vechera-ru/scene/thread-masterskaya` Мастерская — сцена без участников

### Вирусный (`viral-en/scenario/viral`) — 3

- [medium] `people.lost` `viral-en/character/giovanni-pellegrino` Доктор Джованни Пеллегрино — персонаж страниц сценария не назван ни в сценарии, ни в сценах
- [low] `scenes.no_outcome` `viral-en/scene/epilogue` Эпилог — сцена без итога
- [low] `scenes.no_outcome` `viral-en/scene/expanded-ending` Расширенная концовка и новый эпилог — сцена без итога

### Благослови детей его (`bless-the-beast-and-children-ru/scenario/bless-the-beast-and-children`) — 2

- [low] `scenes.no_people` `bless-the-beast-and-children-ru/scene/gazetnye-istorii` Газетные истории — сцена без участников
- [low] `scenes.no_place` `bless-the-beast-and-children-ru/scene/istoriya-denni-eymsa` История Дэнни Эймса — сцена без места

### Вышел срок (`chernovodnyy-ruchey-ru/scenario/dues-vyshel-srok`) — 2

- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/dues-rassprosy-na-ulitsakh` Что известно сыщикам: расспросы на улицах — сцена без участников
- [low] `scenes.no_people` `chernovodnyy-ruchey-ru/scene/dues-ne-nashli-dom-dzheka` Не нашли дом Джека? — сцена без участников

### Мертвенный свет (`dead-light-en/scenario/deadlight`) — 2

- [low] `scenes.no_people` `dead-light-en/scene/deadlight-getting-out` Уехать или уйти пешком — сцена без участников
- [low] `scenes.no_people` `dead-light-en/scene/deadlight-dawn` До рассвета — сцена без участников

### Большой синий буопот (`dead-light-en/scenario/seed-big-blue-buopoth`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Объезд (`dead-light-en/scenario/seed-diversion`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Попутчицы (`dead-light-en/scenario/seed-hitchhikers`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Нейтральная территория (`dead-light-en/scenario/seed-neutral-ground`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Бесконечная дорога (`dead-light-en/scenario/seed-neverending-road`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Чемодан (`dead-light-en/scenario/seed-suitcase`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Чернее чёрного (`dveri-vo-tmu-ru/scenario/none-more-black`) — 2

- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/black-examining-the-black` Чернота: анализ вещества — сцена без участников
- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/black-trying-the-black` Если отведать Черноты — сцена без участников

### Джонни Бой (`dzhonni-boy-ru/scenario/dzhonni-boy`) — 2

- [low] `scenes.no_people` `dzhonni-boy-ru/scene/vylet-na-obochinu` Вылет на обочину — сцена без участников
- [low] `scenes.no_people` `dzhonni-boy-ru/scene/avariya-evakuatora` Авария эвакуатора — сцена без участников

### Экспонат «Новая жизнь» (`eksponat-novaya-zhizn-ru/scenario/eksponat-novaya-zhizn`) — 2

- [low] `scenes.no_people` `eksponat-novaya-zhizn-ru/scene/muzey` Музей — сцена без участников
- [low] `scenes.no_people` `eksponat-novaya-zhizn-ru/scene/posle-sobytiy` После событий в музее — сцена без участников

### Дополнительная сцена 1: «Залы Целаено» (`griby-s-yuggota-ru/scenario/halls-of-celaeno`) — 2

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/celaeno-library` Библиотека — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/celaeno-galleries` Галереи — сцена без участников

### Глава V. Горы Луны (`griby-s-yuggota-ru/scenario/mountains-of-the-moon`) — 2

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/moon-cave-gate` Пещера ми-го — сцена без участников
- [low] `scenes.no_place` `griby-s-yuggota-ru/scene/moon-vision-and-research` Видение о землетрясениях в Перу — сцена без места

### Глава IV. Пески времени (`griby-s-yuggota-ru/scenario/sands-of-time`) — 2

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/sands-well-of-nofru-ka` Колодец Нофру-Ка — сцена без участников
- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/sands-lost-in-the-dunes` Выход из Колодца — сцена без участников

### Холодный урожай (`kholodnyy-urozhay-ru/scenario/kholodnyy-urozhay`) — 2

- [low] `scenes.no_outcome` `kholodnyy-urozhay-ru/scene/son-i-koshmary` Сон и кошмары — сцена без итога
- [low] `scenes.no_outcome` `kholodnyy-urozhay-ru/scene/telekinez-lloygora` Телекинез ллойгора и временная линия — сцена без итога

### Глава 1. Безумец (`lokhmotya-korolya-ru/scenario/madman`) — 2

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/madman-news-coverage-of-roby-murders` Освещение убийств Роби в новостях — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/madman-hereford-police` Полиция Херефорда — сцена без участников

### Глава 7. Ферма Нага (`lokhmotya-korolya-ru/scenario/nugs-farm`) — 2

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/nug-journey-to-gloucester` Поиски Мерси-Хилл и поездка в Глостер — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/nug-village-of-clotton` Деревня Клоттон — сцена без участников

### Пролог. Ночная премьера (`lokhmotya-korolya-ru/scenario/opening-night`) — 2

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/prologue-at-the-scala` Вечер премьеры у театра «Скала» — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/prologue-the-riot` Беспорядки — сцена без участников

### Глава 12. Монастырь (`lokhmotya-korolya-ru/scenario/upper-house`) — 2

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/house-nightmares` Ночные кошмары — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/house-heart-of-the-upper-house` Сердце Монастыря — сцена без участников

### Глава 9. Наместник Индии (`lokhmotya-korolya-ru/scenario/viceroy-of-india`) — 2

- [low] `scenes.no_outcome` `lokhmotya-korolya-ru/scene/ship-dreams-of-hastur` Сны о Хастуре — сцена без итога
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/ship-joining-at-marseilles` Посадка в Марселе — сцена без участников

### Глава 2. Прогулка в парке (`lokhmotya-korolya-ru/scenario/walk-in-the-park`) — 2

- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/park-roby-staff` Опрос персонала из резиденции Роби — сцена без участников
- [low] `scenes.no_people` `lokhmotya-korolya-ru/scene/park-locating-quarrie` Поиск Малькольма Кверри — сцена без участников

### Маленький клуб ужасов (`malenkiy-klub-uzhasov-ru/scenario/malenkiy-klub-uzhasov`) — 2

- [low] `scenes.no_people` `malenkiy-klub-uzhasov-ru/scene/rodovoy-kanal` Родовой канал Ахм’хлти — сцена без участников
- [low] `scenes.no_people` `malenkiy-klub-uzhasov-ru/scene/szhech-klub` Сжечь здание Клуба и поляну — сцена без участников

### Глава 7. Китай (`masks-of-nyarlathotep-en/scenario/china`) — 2

- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/china-140-lantern-street` Дом 140 на улице Фонарей — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/china-unfortunate-client` Злополучный клиент — сцена без участников

### Глава 4. Египет (`masks-of-nyarlathotep-en/scenario/egypt`) — 2

- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/egypt-arriving` Прибытие в Египет — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/egypt-nyarlathotep-sanctum` Святилище Ньярлатхотепа — сцена без участников

### Глава 5. Кения (`masks-of-nyarlathotep-en/scenario/kenya`) — 2

- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/kenya-uganda-railway` По Угандийской железной дороге в Найроби — сцена без участников
- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/kenya-corrupt-ground` Осквернённая земля — сцена без участников

### Моя маленькая сестра (`moya-malenkaya-sestra-ru/scenario/moya-malenkaya-sestra`) — 2

- [low] `scenes.no_people` `moya-malenkaya-sestra-ru/scene/koridor-s-kokonami` Коридор с коконами — сцена без участников
- [low] `scenes.no_people` `moya-malenkaya-sestra-ru/scene/kladovka` Кладовка — сцена без участников

### Одно небольшое дельце… (`odno-nebolshoe-deltse-ru/scenario/odno-nebolshoe-deltse`) — 2

- [low] `scenes.no_people` `odno-nebolshoe-deltse-ru/scene/vehicle` Автомобиль — сцена без участников
- [low] `scenes.no_people` `odno-nebolshoe-deltse-ru/scene/library-archive` Библиотека и городской архив — сцена без участников

### Рейд на Иннсмут (`pobeg-iz-innsmuta-ru/scenario/reyd-na-innsmut`) — 2

- [low] `scenes.no_place` `pobeg-iz-innsmuta-ru/scene/reyd-proverka-biografiy` Проект «Завет»: проверка биографий — сцена без места
- [low] `scenes.no_place` `pobeg-iz-innsmuta-ru/scene/reyd-kontakt` Контакт — сцена без места

### Цель 1: Эзотерический орден Дагона (`pobeg-iz-innsmuta-ru/scenario/reyd-tsel-1`) — 2

- [low] `scenes.no_people` `pobeg-iz-innsmuta-ru/scene/tsel-1-malenkie-komnaty` Маленькие комнаты: перевод «Книги Дагона» — сцена без участников
- [low] `scenes.no_people` `pobeg-iz-innsmuta-ru/scene/tsel-1-garderobnaya-i-vrata` Гардеробная и врата в Й’ха-нтлеи — сцена без участников

### Подземка (`podzemka-ru/scenario/podzemka`) — 2

- [low] `scenes.no_people` `podzemka-ru/scene/obratnyy-put` Обратный путь — сцена без участников
- [low] `scenes.no_people` `podzemka-ru/scene/spusk-na-podurovne` Технический подуровень — сцена без участников

### Ящик Пандоры (`pulp-cthulhu-en/scenario/pandoras-box`) — 2

- [low] `scenes.no_people` `pulp-cthulhu-en/scene/pandora-researching-the-box` Изыскания о ящике — сцена без участников
- [low] `scenes.no_people` `pulp-cthulhu-en/scene/pandora-destroying-the-box` Уничтожение ящика — сцена без участников

### Дезинтегратор (`pulp-cthulhu-en/scenario/the-disintegrator`) — 2

- [low] `pages.gap` страницы без записей: физ. 149
- [low] `scenes.no_place` `pulp-cthulhu-en/scene/disintegrator-izyskaniya` Изыскания перед аукционом — сцена без места

### Мертвецкий стомп (`starter-dead-mans-stomp-ru/scenario/dead-mans-stomp`) — 2

- [low] `scenes.no_people` `starter-dead-mans-stomp-ru/scene/evening-investigations` Вечерние расследования — сцена без участников
- [low] `scenes.no_people` `starter-dead-mans-stomp-ru/scene/turner-home` Дома у Тёрнера — сцена без участников

### Кровавая страница (`tsarstvo-terrora-ru/scenario/seed-bleeding-page`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: conclusion, steps

### Книжные черви (`tsarstvo-terrora-ru/scenario/seed-bookworms`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Холодная кровь (`tsarstvo-terrora-ru/scenario/seed-cold-blooded`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Страх тьмы (`tsarstvo-terrora-ru/scenario/seed-fear-of-the-dark`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Коллекционная редкость (`tsarstvo-terrora-ru/scenario/seed-highly-collectable`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Лаборатория Антуана Лавуазье (`tsarstvo-terrora-ru/scenario/seed-laboratory-of-antoine-lavoisier`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Выдуманная болезнь (`tsarstvo-terrora-ru/scenario/seed-maladie-imaginaire`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Игра в напёрстки (`tsarstvo-terrora-ru/scenario/seed-shell-game`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### Нечто в Бастилии (`tsarstvo-terrora-ru/scenario/seed-thing-in-the-bastille`) — 2

- [high] `scenes.none` у сценария нет сцен (arc.scenario)
- [medium] `plot.missing` нет: steps

### За гранью тьмы (`beyond-the-edge-of-darkness-en/scenario/beyond-the-edge-of-darkness`) — 1

- [low] `scenes.no_people` `beyond-the-edge-of-darkness-en/scene/traveling-to-cairo` Путешествие в Каир — сцена без участников

### Гений места (`dveri-vo-tmu-ru/scenario/genius-loci`) — 1

- [low] `scenes.no_people` `dveri-vo-tmu-ru/scene/genius-research-asylum` О Данверской психбольнице — сцена без участников

### Великий и ужасный Авто (`fears-sharp-little-needles-en/scenario/awto`) — 1

- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/awto-harmon-apartment` Квартира Хармона — сцена без участников

### Свет погас (`fears-sharp-little-needles-en/scenario/lights-out`) — 1

- [low] `scenes.no_people` `fears-sharp-little-needles-en/scene/lights-out-alice-room` Комната Элис — сцена без участников

### Грехи моей юности (`fears-sharp-little-needles-en/scenario/sins-of-my-youth`) — 1

- [low] `scenes.no_place` `fears-sharp-little-needles-en/scene/sins-confessions` Признания — сцена без места

### Последнее желание Уолтера (`fears-sharp-little-needles-en/scenario/walter-final-wish`) — 1

- [low] `scenes.no_outcome` `fears-sharp-little-needles-en/scene/walter-ending` Конец сценария — сцена без итога

### Глава I. Сновидец (`griby-s-yuggota-ru/scenario/dreamer`) — 1

- [low] `scenes.no_people` `griby-s-yuggota-ru/scene/dreamer-paul-apartment` Квартира Пола — сцена без участников

### Грибы с Юггота (`griby-s-yuggota-ru/scenario/fungi-from-yuggoth`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Будь у меня молоток (`keepers-companion-en/scenario/if-i-had-a-hammer`) — 1

- [low] `scenes.no_people` `keepers-companion-en/scene/hammer-start` Начало — сцена без участников

### Маленькие чудеса (`keepers-companion-en/scenario/little-miracles`) — 1

- [low] `scenes.no_people` `keepers-companion-en/scene/little-miracles-in-ordnams-woods` Лес Орднэма — сцена без участников

### Лагерь Санни (`lager-sanni-ru/scenario/lager-sanni`) — 1

- [low] `scenes.no_people` `lager-sanni-ru/scene/den-na-plyazhe` День на пляже — сцена без участников

### Глава 1. Начало кампании (`masks-of-nyarlathotep-en/scenario/campaign-beginning`) — 1

- [low] `scenes.no_place` `masks-of-nyarlathotep-en/scene/campaign-message-from-an-old-friend` Послание от старого друга — сцена без места

### Глава 8. Грандиозный финал (`masks-of-nyarlathotep-en/scenario/grand-conclusion`) — 1

- [low] `scenes.no_place` `masks-of-nyarlathotep-en/scene/conclusion-the-eclipse` Полное солнечное затмение — сцена без места

### Маски Ньярлатхотепа (`masks-of-nyarlathotep-en/scenario/masks-of-nyarlathotep`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Пролог: Перу (`masks-of-nyarlathotep-en/scenario/peru`) — 1

- [low] `scenes.no_people` `masks-of-nyarlathotep-en/scene/peru-descent-into-tunnels` Спуск в туннели — сцена без участников

### Ограбление по-Аркхемски (`ograblenie-po-arkhemski-ru/scenario/ograblenie-po-arkhemski`) — 1

- [low] `scenes.no_people` `ograblenie-po-arkhemski-ru/scene/cherez-slivnuyu-trubu` Через сливную трубу — сцена без участников

### Pax Cthuliana (`pax-cthuliana-ru/scenario/pax-cthuliana`) — 1

- [low] `scenes.no_people` `pax-cthuliana-ru/scene/kvartira` Вступительная сцена 3 — Квартира — сцена без участников

### Наследство Кроуфордов (`pobeg-iz-innsmuta-ru/scenario/nasledstvo-kroufordov`) — 1

- [low] `scenes.no_place` `pobeg-iz-innsmuta-ru/scene/problema-rozhdeniya` Проблема рождения — сцена без места

### Побег из Иннсмута (`pobeg-iz-innsmuta-ru/scenario/pobeg-iz-innsmuta`) — 1

- [low] `scenes.no_place` `pobeg-iz-innsmuta-ru/scene/vstrevozhennyy-artur-anderson` Встревоженный Артур Андерсон — сцена без места

### Посёлок Берёзовый (`poselok-berezovyy-ru/scenario/poselok-berezovyy`) — 1

- [low] `scenes.no_people` `poselok-berezovyy-ru/scene/nachalo-rassledovaniya` 8 июля. Время начинать своё расследование — сцена без участников

### В ожидании урагана (`pulp-cthulhu-en/scenario/waiting-for-the-hurricane`) — 1

- [low] `scenes.no_outcome` `pulp-cthulhu-en/scene/hurricane-aftermath` Последствия — сцена без итога

### Рождественская вечеринка (`rozhdestvenskaya-vecherinka-ru/scenario/rozhdestvenskaya-vecherinka`) — 1

- [low] `scenes.no_outcome` `rozhdestvenskaya-vecherinka-ru/scene/komnaty-v-dome` Комнаты в доме — сцена без итога

### Тайны Кремля (`secrets-of-the-kremlin-en/scenario/secrets-of-the-kremlin`) — 1

- [low] `scenes.no_people` `secrets-of-the-kremlin-en/scene/scene-two-berlin` Берлин: ячейка Потапова — сцена без участников

### Шанс на чудо (`shans-na-chudo-ru/scenario/shans-na-chudo`) — 1

- [low] `scenes.no_people` `shans-na-chudo-ru/scene/informatsiya-dlya-igrokov` Информация для игроков — сцена без участников

### Бумажный след (`starter-paper-chase-ru/scenario/paper-chase`) — 1

- [low] `scenes.no_people` `starter-paper-chase-ru/scene/favorite-gravestone` Любимое надгробие Дугласа Кимбола — сцена без участников

### Охота (`temnye-veka-tri-stsenariya-ru/scenario/hunt-the-hunt`) — 1

- [low] `scenes.no_people` `temnye-veka-tri-stsenariya-ru/scene/hunt-tracks` Следы — сцена без участников

### Синее сияние (`tri-koshmarnykh-vechera-ru/scenario/glow-sinee-siyanie`) — 1

- [low] `scenes.no_outcome` `tri-koshmarnykh-vechera-ru/scene/glow-zaklyuchenie` Заключение — сцена без итога

### Царство Террора (`tsarstvo-terrora-ru/scenario/reign-of-terror`) — 1

- [high] `scenes.none` у сценария нет сцен (arc.scenario)

### Вне власти времени (`vne-vlasti-vremeni-ru/scenario/vne-vlasti-vremeni`) — 1

- [low] `scenes.no_outcome` `vne-vlasti-vremeni-ru/scene/v-dome-gogolya` Дом Гоголя: сад и прихожая — сцена без итога

### Жертвы северных ветров (`zhertvy-severnykh-vetrov-ru/scenario/zhertvy-severnykh-vetrov`) — 1

- [low] `scenes.no_people` `zhertvy-severnykh-vetrov-ru/scene/okkultnyy-podtekst` Оккультный подтекст — сцена без участников

