# «Вирусный» / Viral (`viral-en`) — сверка переноса (часть viral)

Источник — английский оригинал `[EN 7e] Call_of_Cthulhu_Viral.pdf` («Viral Unredacted», Alex Guillotte, Buds RPG Review,
© 2022, Miskatonic Repository), 124 страницы PDF с текстовым слоем; карты (с. 104–110), раздатки-картинки и листы готовых
сыщиков (с. 111–122) прочитаны по изображениям страниц (150–200 dpi). Машинный перевод `[RU-ИИ 7e] Viral_RU.pdf` не
использовался (Р-147). Русский текст — наш перевод, флаг `translated`. Правила — 7-я редакция, ядро (`ruleset` core);
эпоха — наши дни (24–25 августа 2019 года), `axes.era` = `modern`.

## Страницы

Печатная = физическая на с. 5–104 (номера видны на страницах; `pagemap` — физ. 6–104 + 0). Обложка (1), выходные данные (2),
письмо (3), предупреждение (4) без номеров; карты с. 105–110, листы сыщиков 111–122, реклама мерча 123 и задняя обложка 124
без номеров — у них `printed_page` = `null`.

## Термины

По реестру терминов владельца: Зрение (The Sight), Порча (Taint), Реликвы (The Reliquae), Чумной монах (The Plague Monk),
Пожиратель (The Devourer), Яма костей (Charnel Pit), команда «Спектрал» (Spektral Krew). Великий Древний — общая запись
`coc:creature:hastalyk` («Хасталык», Malleus Monstrorum); форма реестра «Хасталик» предложена псевдонимом. У термина
Isola di Malamente в реестре нет русской формы — дана транслитерация «Изола-ди-Маламенте» (вопрос владельцу).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| Обложка «Viral Unredacted. A Modern Call of Cthulhu Scenario» | — (физ. 1) | сценарий `viral-en/scenario/viral` (summary, псевдоним) |
| Credits, © 2022, OBS Community Content | — (физ. 2) | сценарий: summary, sources; см. «Не взято» |
| Письмо Марко (вступление) | — (физ. 3) | раздатки `…/handout/handout-4-marco-email-1`, `…-5-marco-email-2` |
| Warning | — (физ. 4) | сценарий: advice |
| Contents | 5 | сценарий: sources |
| Introduction, Summary, Overview | 6 | сценарий: summary, keeper_info |
| The Spektral Krew; Marco ‘Proudfoot’ Maglioni | 7–8 | организация `…/organization/spektral-krew`; персонаж `…/character/marco-maglioni` |
| Corrina Trench | 8 | `…/character/corrina-trench` |
| Enoch Jeremiah Eakins | 9 | `…/character/enoch-eakins` |
| Peter Wharton | 9–10 | `…/character/peter-wharton` |
| Ku Hyeon | 10 | `…/character/ku-hyeon` |
| Maya Adeduwon (NPC), Maya’s Secrets | 10–11 | `…/character/maya-adeduwon` |
| Emily ‘Em’ Lavigne (NPC): Super Fan Option, Another Ghost Hunter Option, Keeper’s Notes | 11–12 | `…/character/emily-lavigne`; `…/organization/phantom-posse` |
| Creating New Investigators; Other Investigator Options (Mythos Investigators, Documentary Film Crew, Tourists, Pesky Teenagers) | 12–13 | организация `spektral-krew` (description); `…/character/nuncio-vendra` (legend) |
| Spektral Krew Gear: Carried (Satchel, Handheld NV Cameras, EMF Meter, Spirit Box, EVP SCD1, FLIR) | 14 | `…/item/krew-gear` |
| Static (Base Station, Wi-Fi Repeaters, UPS Batteries, Night Vision Cameras, Drone) | 14 | `…/item/krew-gear` |
| Timeline | 15 | сценарий: таблица «Хронология» |
| History; Keeper’s Notes (1954, книга 1958) | 15–16 | `…/location/isola-di-malamente` (history); `…/organization/plague-cult`, `…/organization/dss`; `…/item/il-culto-della-peste`; `…/character/giovanni-pellegrino` |
| One Night in Perla; The Purging of Morbus; видео 2002 года | 17 | город `coc:location:perla`; сцена `…/scene/welcome-to-perla` |
| Welcome to Perla; The Hotel Sunset | 18–19 | сцена `welcome-to-perla`; `…/location/hotel-sunset`, `…/location/perla-piazza`; `…/character/paolo` |
| Perla: The Shops, The Homes, The Docks, Nuncio Vendra | 19 | `coc:location:perla`; `…/location/perla-docks`, `…/location/cappella-di-santanna`; `…/character/nuncio-vendra` |
| Local Teens; Communication | 20 | `…/character/local-teens`; `coc:location:perla` |
| Exploring in Perla; Rumors (1–10) | 20–21 | сцена `…/scene/exploring-perla`; таблица «Слухи об Изола-ди-Маламенте» у `coc:location:perla` |
| Signs and Portents (1–10) | 21–22 | таблица «Знамения и предзнаменования» у `coc:location:perla`; `…/location/misteri-del-passato`, `…/item/morbus-coin`; `…/character/luca`, `…/character/signore-marino`, `…/character/angelo-russo` |
| The Burning of the Disease | 23–24 | сцена `…/scene/burning-of-the-disease` |
| The Next Day (записка Нунцио) | 24 | сцена `…/scene/the-next-day`; раздатка `…/handout/nuncios-note` |
| Perla NPCs: Santina Maria Salvatore, Padre Angelo | 25 | `…/character/santina-salvatore`, `…/character/padre-angelo`, `…/character/alonzo-salvatore` |
| Isola di Malamente (титул части) | — (26) | `…/location/isola-di-malamente` |
| Keeper’s Secrets; Running the Investigation; Night of the Plague; The Live Stream; Managing the Investigators | 27 | сценарий: keeper_info |
| Stream Schedule (1–8); Maya; Commenters; Hastalÿk; The Ghost Hunting Aesthetic | 28 | сценарий: таблица «План стрима», keeper_info, advice |
| The Environment, The Evidence, The ‘Psychics’, Getting into the Mindset (рекомендуемый просмотр) | 29–30 | сценарий: advice; раздатка `…/handout/handout-3-ghost-hunter` |
| Number of Sessions (One, Two, Full Scenario) | 30 | сценарий: advice |
| Plots and Schemes: The Plague Monk, Hastalÿk, Nuncio Vendra, The Italian Government | 30–31 | `…/creature/plague-monk`; сценарий: keeper_info; `…/character/nuncio-vendra`; `…/organization/dss` |
| Prologue | 32 | сцена `…/scene/prologue`; раздатка `…/handout/handout-11-enochs-vision` |
| Isola di Malamente: Locations; General Description: The Main Island | 33 | `…/location/isola-di-malamente` |
| 1. Lighthouse/Radio Station (Exterior, Interior, Lighthouse Base, Stairs, Lantern Deck) | 33–34 | `…/location/lighthouse`; сцена `…/scene/lighthouse-setup` |
| 2. Beggar’s Cove (таблица гребли) | 34 | `…/location/beggars-cove` (таблица «Гребля на лодке из Бухты Нищих»); `…/item/rowboat` |
| 3. The Weeping Bridge (Elder Sign, видение) | 34–35 | `…/location/weeping-bridge`; `…/item/elder-sign-mosaic`; сцена `…/scene/opening-monologue` |
| 4. Lemon Grove (таблица лимонов 1–10, видение) | 35–37 | `…/location/lemon-grove` (таблица «Мутировавшие лимоны»); сцена `…/scene/lemon-grove` |
| 5. Saint Roche’s Hospital (Exterior, Interior, Other Descriptions, Limiting Exploration, Optional Discoveries) | 37–38 | `…/location/saint-roches-hospital`; сцены `…/scene/outside-the-hospital`, `…/scene/inside-the-hospital` |
| Audio Recording (итальянский и английский), видение | 38–39 | `…/item/emi-tape-recorder`; `…/character/colonel-rossi` |
| VHS Recorder | 39 | `…/item/vhs-recorder` |
| Hospital Locations; Hospital, Cellar: Morgue, Old Files, Storage | 39–40 | `…/location/hospital-cellar`, `…/location/hospital-morgue`, `…/location/hospital-old-files`, `…/location/hospital-cellar-storage` |
| Hospital, Ground Floor: 1A–1H | 40–42 | `…/location/hospital-ground-floor`; `…/location/1a-administrators-office` … `…/location/1h-main-dining-hall`; `…/character/enzo-bianco` |
| Ground Floor, West Wing: 1I–1M | 42 | `…/location/1i-west-corridor` … `…/location/1m-terminal-ward` |
| Ground Floor, East Wing: 1N–1R (молельня, вращающееся распятие) | 42–43 | `…/location/1n-east-corridor` … `…/location/1r-staff-dormitory` |
| Ground Floor, Secret Rooms: 1S–1V | 43–44 | `…/location/1s-shrine-of-bones` … `…/location/1v-cast-offs`; `…/tome/iuramentum-corruptionis`; `…/item/bodeo-revolver` |
| Administrator’s House (наркоман, этажи, чердак) | 44 | `…/location/administrators-house`; `…/character/angelo-russo`; сцена `…/scene/administrators-house` |
| Hospital, Second Floor: 2A–2D; West Wing 2E–2H; East Wing 2I–2J | 45 | `…/location/hospital-second-floor`; `…/location/2a-head-nurses-office` … `…/location/2j-recent-ward` |
| Hospital, Third Floor | 45 | `…/location/hospital-attic` |
| 6. Mass Graves | 45–46 | `…/location/mass-graves`; сцена `…/scene/mass-graves` |
| 7. Cremation Pit | 46 | `…/location/cremation-pit`; сцена `…/scene/cremation-pit` |
| 8. Isola di Malamente Dock | 46 | `…/location/malamente-dock` |
| 9. Overlook Point (катер «Ведетта») | 46–47 | `…/location/overlook-point`; `…/item/vedetta` |
| 10. Chapel & Crypt (Cemetery, Chapel, Crypt, The Witch Board) | 47–48 | `…/location/chapel-ruins`, `…/location/crypt`; `…/item/witch-board`, `…/item/crypt-iron-box`; сцены `…/scene/the-chapel`, `…/scene/witch-board-seance` |
| 11. Catacomb Entrance; Live Stream | 48 | `…/location/catacomb-entrance`; раздатка `…/handout/handout-35-book-fragment` |
| 12. Catacombs | 48–49 | `…/location/catacombs`; сцена `…/scene/catacombs` |
| 13. Temple of Morbus; The Birthing Pit | 49 | `…/location/temple-of-morbus`, `…/location/charnel-pit` |
| Hastalÿk Awakens; Hastalÿk Rises | 49–50 | сцена `…/scene/hastalyk-awakens`; `…/creature/devourer` |
| Escape! Going Back; Split in the Wall; Diseased Lemon Tree; Why Not Use the Climb Skill? | 50–51 | сцена `…/scene/escape`; `…/location/smugglers-tunnel` |
| Hastalÿk Unleashed | 51 | сцена `…/scene/hastalyk-unleashed` |
| The Desolation of Isola di Malamente | 52 | сцена `…/scene/desolation` |
| Epilogue; Rewards | 52 | сцена `…/scene/epilogue`; сценарий: conclusion |
| Иллюстрация (истребители) | — (53) | см. «Не взято» |
| Cinematic Ending; DSS Incendiary Grenades; таблица броска; Escaping the Island | 54–55 | сцена `…/scene/cinematic-ending`; `…/item/dss-incendiary-grenades`; сценарий: таблица «Бросок гранаты» |
| Expanded Ending; New Epilogue | 56–57 | сцена `…/scene/expanded-ending`; `…/organization/dss` |
| Appendix: Encounters; Outdoor Encounters (1–12) | 58–59 | сценарий: таблица «Встречи на открытом воздухе» |
| Hospital Encounters (1–12) | 59 | сценарий: таблица «Встречи в больнице» |
| Catacomb Encounters (1–6) | 60 | сценарий: таблица «Встречи в катакомбах» |
| New Rules: The Sight; Using the Sight (Simple, Mechanical, Open/Close the Sight, Sensing a Presence, Echoes of the Past, Precognition, Calm the Mind) | 60–61 | раздатка `…/handout/handout-2-the-sight` (полный текст); сценарий: keeper_info; `…/character/enoch-eakins` (abilities) |
| The Taint; Taint Levels | 62 | сценарий: таблица «Уровни Порчи», keeper_info |
| Insanity and Bouts of Madness (1–10) | 63 | сценарий: таблица «Приступы безумия на острове» |
| Appropriate Phobias | 64 | сценарий: таблица «Подходящие фобии» |
| Paranormal Phenomena (1–10) | 64 | сценарий: таблица «Паранормальные явления» |
| New Mythos Horrors: Hastalÿk; The Devourer (Aspect of Hastalÿk) | 65 | `…/creature/devourer`; общая `coc:creature:hastalyk` — через предложения |
| The Plague Monk | 66 | `…/creature/plague-monk` |
| The Reliquae (статблок, Infected Flesh, таблицы болезней) | 66–67 | `…/creature/reliquae`; сценарий: таблицы «Заражение Реликв: серьёзное / смертельное» |
| New Mythos Tome: Iuramentum Corruptionis | 67 | `…/tome/iuramentum-corruptionis` |
| New Spell: Control Reliquae | 68 | сценарий: keeper_info (пересказ); черновик общей записи — в отчёте (kb/spells общий) |
| A Few Pointers on Running Viral from Bud | 68 | сценарий: advice; персонажи (description) |
| Player Handouts: #1 Original Google Map | 69 | `…/handout/handout-1-google-map` |
| #2a–2b The Sight: Player Reference Sheet | 70–71 | `…/handout/handout-2-the-sight` |
| #3a–3b How to Be a Ghost Hunter | 72–73 | `…/handout/handout-3-ghost-hunter` |
| #4–5 Marco’s Emails | 74 | `…/handout/handout-4-marco-email-1`, `…-5-marco-email-2` |
| #6–8 Maya’s Emails | 75–76 | `…/handout/handout-6-maya-email-1`, `…-7-maya-email-2`, `…-8-maya-email-3` |
| #9 Printout of Island Map with Notes | 77 | `…/handout/handout-9-island-map` |
| #10 Saint Roche’s Hospital – Photocopy from Maya | 78 | `…/handout/handout-10-hospital-map` |
| #11 Enoch’s Vision | 78 | `…/handout/handout-11-enochs-vision` |
| #12 Corrina’s Research | 79 | `…/handout/handout-12-corrinas-research` |
| #13 Marco’s Intro Script | 80 | `…/handout/handout-13-intro-script` |
| #14 Isola di Malamente Lighthouse | 81 | `…/handout/handout-14-lighthouse` |
| Hyeon’s iPads / The Stream Begins (пояснение) | 82 | `…/character/ku-hyeon` (description); описание раздаток 15–25 |
| #15–25 iPad-раздатки (мост, роща, яма, могилы, у больницы, дом администратора, больница 1–3, часовня, склеп) | 83–93 | `…/handout/handout-15-stream-begins` … `…/handout/handout-25-witch-board-ritual` |
| #26 The Crypt: Following the Collapse; #27 The Catacombs and Beyond | 93 | `…/handout/handout-26-crypt-collapse`, `…/handout/handout-27-catacombs-and-beyond` |
| #28–39 картинки (мост, Знак, окно ×2, роща, яма, доска, фрагмент книги, катакомбы, рыцарь, Хасталык ×2) | 94–103 | `…/handout/handout-28-weeping-bridge` … `…/handout/handout-39-hastalyk-destroyed`; `…/handout/handout-35-book-fragment` |
| Keeper Maps: карта побережья с примечанием | 104 | карта `…/map/sicily-coast` (`app/maps/viral-sicily-coast.jpg`) |
| Карта острова (легенда 1–9) | — (105) | карта `…/map/isola-di-malamente` (12 меток) |
| Ground Floor & Basement (A–V) | — (106–107) | карта `…/map/hospital-ground-floor` (разворот, 37 меток) |
| Second & Third Floors (A–J), Heroin Addict | — (108–109) | карта `…/map/hospital-upper-floors` (разворот, 16 меток) |
| Secret Underground | — (110) | карта `…/map/secret-underground` (9 меток) |
| Pre-Gens: листы Марко, Коррины, Инока, Питера, Хёна | — (111–120) | пять готовых сыщиков (статблоки, предыстория, снаряжение, деньги, обязанности) |
| Пустой лист сыщика Spektral Krew | — (121–122) | см. «Не взято» |
| Реклама мерча Spektral Krew (Zazzle) | — (123) | `…/organization/spektral-krew` (description) |
| Задняя обложка | — (124) | сценарий: summary |

Итого записей книги: сценарий 1; сцен 23; мест 63 (5 в Перле, окрестности Перлы, остров и 56 мест острова; + общий город `coc:location:perla`); карт 5; персонажей 19 (5 готовых
сыщиков); существ 3; книга Мифов 1; предметов 12; раздаток 40; организаций 4.

## Опечатки и расхождения книги (в `errata` записей)

- Карта острова (с. 105): номера 1 и 2 в легенде перепутаны с текстом (на самой карте «1» у маяка, «2» у бухты); больница
  названа «Ospedale Sant’Esposito / Saint Esposito Hospital» — `lighthouse`, `beggars-cove`, `saint-roches-hospital`.
- Лист Марко: «Marco Prooudfoot», место рождения NYC (в тексте — Палермо); лист Инока: Ланкастер, Пенсильвания (в тексте — Огайо).
- Лист Питера: не заполнены Первая помощь, История, язык и урон выкидного ножа.
- Раздатка 9: «стрим в 21:00, забор в 6:00» против 20:00 (хронология) и 5:30 (записка Нунцио).
- Пролог: праздник назван «La Notte della Malattia», в остальной книге вторая ночь — Notte della Peste; раздатки «1–7» вместо 1–8.
- Письмо Майи: «Notta della Peste».
- Видео/нож: история с туристом 2002 года (с. 17) и с репортёром (с. 27) расходятся.
- Хронология: прилёт 24 августа (с. 15) против нового пролога с 23 августа (с. 18).
- Катакомбы: III век н. э. (текст) против III века до н. э. (карта).
- Анджело Руссо: «десять лет» на острове против «несколько лет назад» в Перле.
- Знак Старших богов: древний (с. 35) против печатей DSS (с. 55).
- Пожиратель: бонус к урону «3D6» без «+».
- 1P «десять коек вдоль северной и южной стен, всего десять» — в записи `1p-recent-ward` — без числа, в `errata`.

## Не взято

- Список авторов, редакторов и тестеров, благодарность Сету Скорковски, правовая плашка (с. 2) — не игровые данные; © и
  издательство — в summary сценария.
- Иллюстрации без подписи и текста (с. 26 — коридор, с. 53 — истребители) и картинки раздаток: в базу не добавлены — это
  `app/art/` вне моих файлов; раздатки-картинки описаны пересказом (Р-130). Портреты на листах сыщиков — тоже не добавлены
  (кандидаты для `pipeline/art/add_images.py`).
- Раздатки 9 и 10 (карта острова и план больницы для игроков) не заведены как карты с метками: их картинки — раздатки,
  подписи переписаны в текст раздаток.
- Пустой лист сыщика (с. 121–122) — бланк без данных.
- «Быстрые правила» на листах сыщиков (уровни успеха, раны и лечение) — повтор правил ядра.
- Реальные города на карте побережья (Виттория, Рагуза, Шикли, Модика и др.) — меток нет: записей этих мест в базе нет, в
  сценарии они не участвуют.
- Слепой антиквар, зеленщик, офицер полиции, старуха в окне, солдат из «Кинематографичного финала», сержант Бьянки, Катена
  Ла Роза, Феликс Блю, муж Сантины Паулу — без своих записей: эпизодические фигуры, описаны в текстах мест, таблиц, сцен,
  раздаток и персонажей.


