# The Year of the Goat — сведение книги (Р-139, Р-251)

Книга `year-of-the-goat-en`, 12 сценариев, шесть частей (ab, cd, ef, gh, ij, kl). Скрипты сведения —
`.cache/lead-tools/integrate-goat/` (пути от `__file__`; `integrate.py spells|links|cw|terms`, `build_terms.py`).

## Общие заклинания (новые записи `kb/spells/`)

Поиск по `kb/spells` (названия, псевдонимы, английские имена) совпадений не дал — заведено 6 записей из черновиков:
`coc:spell:mothers-cold-heart` «Холодное сердце Матери», `come-to-mother` «Иди к Матери» (ab, Беатрикс);
`shepherds-call` «Зов пастуха», `panic` «Паника» (ef, Пан); `transitio-umbrae` «Путь теней (Transitio Umbrae)» (gh, Салли
и Сэмюэл Торн); `compel-nature` «Повеление природе» (kl, «Хроника Ната»). Поправлено при переносе: стоимость везде «ПМ»
(было «пунктов магии», «магических очков», английское «2 Magic Points; SAN roll» у Повеления природе), пустое
`deeper_magic: null` убрано (схема), у заклинаний Беатрикс и «Пути теней» в `refs` — заклинатели.

Ссылки `spell`: Беатрикс (2), Пан (2), Салли и Сэмюэл Торн (по 1), `tome/chronicle-of-nath` (1). `refs` на заклинания —
сцены `sorte-final-showdown` (Зов пастуха, Паника), `flesh-meeting-the-thornes` (Путь теней), `orchard-taking-stock` и
`orchard-black-cherry-tree` (Повеление природе).

Без ссылки остались (описания в книге нет): «Call the Brood» (Лилит Рен), «Drain Essence» (Мать-Коза Топей),
«Blessing of Boundless Fertility» и «Summon Woodland creatures» (ДикаяМудраяЖенщина), «Hymn for the great nuptial union»
(`tome/book-of-standing-stones`); «Dominate (mythos power)» Тэда Харта — сила, не заклинание (так и задумано).

## Предложения

Применены все (12 правок в 5 записях): proposals-ef (4: источники и `refs` у `coc:location:tower-of-london`,
`coc:location:inns-of-court-and-chancery`), proposals-gh (7), proposals-kl (1); proposals-ij пуст. Пропущенных нет.
Поправлены сами предложения: составные псевдонимы gh разделены — `coc:spell:enthrall-victim` + «Audi Matrem»,
«Listen to Mother» (kl), «Внемли Матери»; `coc:spell:clutch-of-nyogtha` + «Cardium Frangere», «Shatter the Heart»,
«Разбить сердце»; `coc:creature:shub-niggurath` + «All-Mother», «Всематерь». Русский псевдоним kl «Слушай маму» заменён
общей формой «Внемли Матери» (см. термины). **Повторно `apply.py` не запускать** — `append` пропустит, но смысла нет.

## Предупреждения о содержании

`rule/content-warnings`: в `refs` добавлены остальные 10 сценариев (теперь все 12); названия сценариев в строках таблицы —
«русское (English)», как у первых двух («In Sorte Diaboli» без перевода).

## Атмосфера (Р-241)

Шесть списков `atmosphere-*.json` влиты в `pipeline/art/atmosphere.json` инструментом `pipeline/art/merge_atmosphere.py`:
добавлено 66 страниц книги со статусом `atmosphere`. Записями не заводились.

## Термины (одна форма на всю книгу; правка — 50 файлов книги)

| English | Принято | Было иначе |
|---|---|---|
| Black Goat of the Woods (with a Thousand Young) | Чёрная Коза Чащоб (с Легионом Младых) — офиц. («Особняки безумия», «Тёмные века», «Книга хранителя»; псевдоним Шуб-Ниггурат) | «Чёрный Козёл Лесов с Тысячей Младых» (ab, ij), «Чёрная Коза Лесов с Тысячью Младых» (gh, kl) |
| Black Goat | Чёрная Коза | «Чёрный Козёл» (ab) |
| Listen to Mother / Audi Matrem (= Enthrall Victim) | «Внемли Матери» | «Слушай маму» (kl) |
| Samuel | Сэмюэл (как в базе) | «Сэмюел» (kl: Сэмюел Брукс, родители Лонни) |
| Susan | Сьюзан (как в базе) | «Сьюзен» (ab: Сьюзан Хейнс) |
| Herbert | Герберт (как в базе) | «Херберт» (kl: семья Гербертов) |
| Blackwell | Блэкуэлл (как в базе) | «Блэквелл» (cd: Томас Блэкуэлл) |
| pregen | готовый сыщик | «прегены» (ij, 2 места) |
| magic point | ПМ | «очко магии» (Лади Вен) |
| Shub-Niggurath, Dark Young, ghoul, satyr, handout, bonus/penalty die, Keeper | Шуб-Ниггурат, Тёмная молодь, упырь, сатир, раздатка, бонусная/штрафная кость, Хранитель | совпадали |

`checks/20261126-goat/new-terms.json` — 596 терминов книги (`ru` = `name.ru` записи, если термин её называет; иначе `ref` —
запись, где термин встречается); слиты `new-terms-cd/gh/kl.json` (удалены, чтобы не было дублей) и таблицы терминов
отчётов ab, ef, ij. Отброшено 134: принятые в глоссарии (Dilettante, The Believer, fumble, Extreme success…), имена общих
записей (Tower of London, Green Man…), общие слова (Hard, Kitchen, Garage…), списки имён, заклинания без перевода.

## Проверки

- Нормализация `--changed` (dice, terms, attribute_words, errata_flag): изменений 0.
- `tools/check.py --changed`: 70 записей, 0 ошибок, 0 предупреждений. `tools/check.py`: 23 888 записей, 0 ошибок,
  2 предупреждения (howl-of-the-chimeras-en, не эта книга).
- `tools/completeness.py` → `completeness/`: 3 находки low — оглавление с. 7–8 (ожидаемо); `incomplete` у
  `creature/oaken-guardians` (название записи описательное, статблока нет) и `tome/book-of-standing-stones` (нет
  характеристик книги Мифов и описания гимна).
- `tools/scenario_check.py` → `scenario/`: 12 сценариев, 0 находок.
- `pipeline/source/catalog_sync.py`: 666 работ, в базе 157.

## Вопросы владельцу

1. Эпоха «The Convent of Sancta Maria Lactans» (1526, эпоха Тюдоров): стоит `dark-ages` по подзаголовку книги — оставить?
2. Эпоха «The Witch's Bargain» (1640-е, подзаголовок «Dark Ages»): стоит `other` — оставить или `dark-ages`?
3. Эпоха «Dead Letters from the Orchard» (1910): стоит `gaslight` — принято ли так для 1900–1910-х?
4. Финляндия (`location/salamajarvi-national-park`), графство Кент (`location/kent`), Южный Техас/Хьюстон
   (`location/south-texas`) — вершины «город сценария»; завести общие записи мест?
5. Бангей (`location/bungay`, реальный город) — в общую запись?
6. Заклинания без текста — «Call the Brood», «Drain Essence», «Blessing of Boundless Fertility», «Summon Woodland
   creatures», гимн «Hymn for the great nuptial union»: оставить названием без ссылки или завести записи-заглушки?
7. Р-36 (БкУ/Комплекция/ПЗ существ как напечатано): Мясистая лужа (+7d6/8, ПЗ 57), Пан (+3d6/4), сатир монастыря (0/0),
   Мать-Коза Топей (ПЗ 60, +2d6/4), Чёрный Шак (ПЗ 25, +2d6/3), Мамочка Би (+3d6/4), аватар Сары Торн (+2d6/3, ПЗ 50, ПМ 100),
   Лади Вен (ПЗ 21, +3d6/4, ПМ 25), Хух Ди Гута (ПЗ 28, +2d6 при Комплекции 5), Чёрная вишня (ПЗ 40, Комплекция 7),
   гибриды Харперс-Орчарда (ПЗ 20, 1d6/2) — оставить как напечатано?
8. «Thousand Young» в эпитете — офиц. «Легион Младых»; название сценария «Mother of a Thousand Young» оставлено
   «Мать тысячи младых» — или «Мать Легиона Младых»?
9. «Listen to Mother» — принято «Внемли Матери» для обоих сценариев (вместо «Слушай маму» у Глэдис) — согласны?
10. «Ходячие деревья курорта» (`creature/oaken-guardians`, en «Moving Trees») — название редакционное, `incomplete`: принять?
11. Профессии без записи справочника (`occupation_ref` нет): Гас (учитель), Синди (инвестбанкир), Джойс (мастер на все
    руки), Боб (не названа) — заводить?
12. Кинжал у прегенов и культистов монастыря — 1d4 без БкУ (КХ: 1d4+2): ссылку на справочник оружия ставить?
13. Навык «Theology» («Богословие», «Сделка ведьмы») и навыки листов «Дома плоти»/«Фестиваля» (Соцсети, Финансы, Футбол,
    Мыловарение) — без записей справочника: заводить?
14. Имена, придуманные по Р-150/Р-151 (готовые сыщики «Дева, Мать, Старуха», групповые профили, Хамфри Пимм, Уот Кобб,
    Хэл Бреннан) — принять?
15. Перевод Codex (`checks/20261126-goat/translation/`) шёл параллельно: сверить его с принятыми формами (Чёрная Коза Чащоб,
    «Внемли Матери», Сэмюэл, Сьюзан, Герберт, Блэкуэлл) перед сборкой HTML.
