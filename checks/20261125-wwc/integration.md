# World War Cthulhu — сведение линейки (Р-139)

Пять книг: `wwc-cold-war-en`, `wwc-covert-actions-en`, `wwc-our-american-cousins-en`, `wwc-section-46-en`,
`wwc-london-en`; восемь частей (cw-a, cw-b, covert-a, covert-b, s46, cousins, london-a, london-b). Скрипты сведения —
`.cache/lead-tools/integrate-wwc/` (пути от `__file__`).

## Общие записи (перенесены из черновиков; дублей в `kb/` нет — проверено по id, `name.en`, псевдонимам)

- Навыки (8): `coc:skill:tradecraft`, `organisation-knowledge`, `signals` (+ псевдоним «Радиосвязь»), `military-science`
  (+ источник London, расхождение баз 00%/01% — в `quality.notes`), `civil-defence`, `command`, `make-do-and-mend`,
  `operate-radio`. Готовых записей Operate Radio / Command / Signals в базе не было.
- Профессии (13): `coc:occupation:wwc-intelligence-officer` и 12 лондонских `coc:occupation:wwc-*`.
- Заклинания (16): `pnakotus-quills`, `enslavement-to-the-icterus`, `drop-guise`, `speak-the-shining-word`,
  `call-dismiss-ti-taki-ti`, `ubytsa-mertvykh` (variant_of «Изгнание Йде Итад»), `corruption-of-chort` (variant_of
  «Иссушение»), `summon-dismiss-child-of-magna-mater` (название редакционное, `needs_review`), `anchor-of-dreams`,
  `gifts-of-the-deep`, `echo-of-the-past`, `enchant-sacrificial-blade` (не объединено с `enchant-sacrificial-dagger`
  «Царства Террора» — другое заклинание), `summoning-circle`, `create-fire-vampire`, `fire-walk`, `pyromancy`.

## Предложения

Применены все: proposals-london-a (39), -cousins (10), -cw-a (8), -cw-b (18), -covert-a (1), -london-b (15), -s46 (9),
-drafts-london-a (3), art2-cousins (1). Остальные art-*/art2-*/art3-* были применены частями (пробный прогон — «уже было»).
Поправлены сами предложения: drafts-london-a — у схемы навыка нет `errata`, расхождение баз Военного дела записано в
`quality.notes` (вместо errata + `parse_uncertain`); cousins — связь Гувера с ФБР: `note` «служба» (было «директор» в обе
стороны); covert-a — экземпляр «Откровений Хали» сразу со ссылкой на `coc:spell:enslavement-to-the-icterus`; cw-b, s46 —
кубы строчной `d` в `source_variants` (Р-27; записи поправил `normalize_dice.py`). Пропущенных нет.
**Повторно `apply.py` на эти файлы не запускать**: операции `replace` вставят абзацы второй раз.

## Ссылки

- Статблоки: 81 навык связан со справочником (Шпионское ремесло, Военное дело, Командование, Связь, Знание организаций
  со специализацией, Криптография → Наука, Гражданская оборона, Смекалка и починка); «Доверие (…)» — механика, без ссылки.
- Заклинания: 31 ссылка `spell` (новые записи; «Summon Deep One» → `coc:spell:summon-bind-deep-one`; Кощей и
  «Бессмертный»/«О порче» → варианты вместо «Иссушения»/«Изгнания Йде Итад»).
- `occupation_ref` → `coc:occupation:wwc-intelligence-officer`: Файза Канаан и 4 прегена S46.
- `refs`: правила cw-a и london-a о новых навыках/профессиях; плёнка «Уриан» и сцена «Плёнка» → заклинание Магна Матер;
  правила S46 → правила Cold War, на которые книга ссылается страницей; 64 ссылки на навыки из текстов правил/сцен/предметов.
- `instance_of` (covert-b → профили cw-b): солдаты Тимора и АБРИ → «Солдат», ФРЕТИЛИН → «Террорист/партизан», КГБ и
  милиция МВД, Костин → «Сотрудник тайной полиции» (книга: «KGB and MVD officers… page 131»).
- Перси Гуджон — член `wwc-cold-war-en/organization/brothers-of-the-yellow-sign`.
- Убраны устаревшие пометки «черновик… ссылку добавить после переноса» (47 мест); дубль связи `knows` Ефимов/Мамыкин.

## Термины (одна форма на все пять книг)

| English | Принято | Было иначе |
|---|---|---|
| Signals (навык) | Связь | «Радиосвязь» (cw-b, covert-a) — заменено, псевдоним навыка |
| Organisation Knowledge | Знание организаций | «Знание организации» (cw-b) |
| Organisation Knowledge (Soviet Union) | специализация «Советский Союз» | «СССР» (s46) |
| Safe house | конспиративная квартира; не квартира — «конспиративная ферма», «конспиративное убежище» | «убежище» (covert-a, s46: «Поиск убежища» → «Поиск конспиративной квартиры», Стратфорд → «Конспиративное убежище SIS…») |
| Bonus / penalty die | бонусная / штрафная кость (офиц.) | «кубик» (covert-a) |
| Hard / Extreme | трудная / чрезвычайная (офиц. «Трудный/Чрезвычайный успех») | — |
| SIS | SIS (латиница, большинство записей) | «СИС» (cw-b, cousins) |
| Our Other Enemy | Наш Другой Враг | «Наш другой враг», «нашим Другим Врагом» |
| Bruiser (тип личности) | Громила (cw-a, cw-b) | «Боец» (london-a, s46) |
| Building Trust | Укрепление Доверия | «Завоевание Доверия» (s46) |
| Exfiltration | вывод (эксфильтрация) | «Эвакуация» (cousins, сцена) |
| Trust (агентство) | Доверие (КГБ / ЦРУ / АНБ / ФБР / РУМО / Штази / Секция 46 / Фольксполицай / SIS …) | латиница KGB, CIA, NSA, FBI, DIA, Stasi, Section 46… |
| Tradecraft, Military Science, Command, Operate Radio, Trust, dead drop, walk-in, handler, Tcho-Tcho, ghoul | Шпионское ремесло, Военное дело, Командование, Радиодело, Доверие, тайник, инициативник, куратор, чо-чо, упырь | совпадали |

## Смещения страниц

`pipeline/source/books.json`: `offset: 0` у всех пяти книг (все части сообщили 0).

## Проверки

Нормализация `--changed`: normalize_dice — 31 строка в 16 файлах, остальные — 0. `tools/check.py --changed`: 1640 записей,
0 ошибок, 0 предупреждений. `tools/check.py`: 23 271 запись, 0 ошибок, 2 предупреждения (howl-of-the-chimeras-en, не WWC).
`tools/audit.py`: 135 находок по WWC из 1134 (см. «Вопросы»).

## Кандидаты в справочник оружия (не заведены)

Cold War (cw-b), таблицы правил: `rule/revolvers` (с. 148–149): Colt Detective Special (возможно `model_of` .38 Revolver),
Colt Python, S&W Model 60, Manurhin MR73. `rule/semi-automatic-pistols` (с. 149–151): Star B, Star P, Walther PPK
(возможно .32 Automatic), FN/Browning GP35, PSM, Colt Defender, Astra Falcon, MBA Gyrojet, S&W Model 39, Auto Mag, CZ 75.
`rule/shotguns` (с. 151–153): Mossberg 500, Winchester Defender, Remington M870, Ithaca 37, Ithaca 37 Stakeout, Browning
Auto 5, Atchisson Assault Shotgun, KS-23. `rule/light-automatic-weapons` (с. 153–155): Vigneron, Sterling, CZ Model 25,
MAT-49, Erma MP58, Beretta M12, Stechkin, H&K VP70, Star Z70B, Ingram M10. `rule/rifles-assault-rifles-and-light-support-weapons`
(с. 156–158): M14, M14A1, M21, H&K G3, AR-15/M16, M16A1 (возможно `model_of` M16A2), M40, Mauser SP66, H&K PSG1,
H&K HK21/HK13, Stoner Weapon System. `rule/other-equipment` (с. 158–160): Glove Pistol. Итого 45; уже в справочнике
(получили `source_variants`): Makarov, Thompson, PPSh-41, Uzi, Skorpion, MP5, AK-47, AK-74, FN FAL, СВД.
Section 46 (с. 106–111, правила `special-weapons-*`): Welrod, H&K P11, СПП-1, De Lisle, АПС, РПК, FN MAG 58/L7, MG 3,
РПД/Тип 56/Тип 62, ПКМ, Carl Gustav M2, H&K 69A1, M203, светошумовая, дымовая, зажигательная гранаты, Federal Riot Gun,
ARWEN, Schermuly; без статистики — M28/M29 Davy Crockett, S&W Model 23 «Hush Puppy». London (с. 78, `rule/firearms`):
пика Внутренней гвардии.

## Вопросы владельцу

1. Кладбище Боу — в трёх книгах: `wwc-covert-actions-en/location/bow-cemetery` (London дополнил источником) и
   `wwc-section-46-en/location/tower-hamlets-cemetery-park`; перенести в общую запись (Р-154) и слить?
2. Никсон, Джим Джонс, Пол Пот (`wwc-cold-war-en/character/*`; Никсон — и в Our American Cousins) — в общие персонажи?
3. Грин-парк `masks-of-nyarlathotep-en/location/england-green-park` дополнен London — перенести в общие места?
4. Завести общие записи оружия по списку выше?
5. 14 новых заклинаний Cold War (Daoloth, Tawil at’Umr, Yog-Sothoth) лежат только в правилах `rule/spells-of-*`; в
   статблоках и книгах `spell: null` — завести `coc:spell:*`? Вызов/изгнание и Связь с Фтаггуа (London) книга только называет.
6. «Призыв/изгнание дитяти Магна Матер» — название редакционное (`needs_review`): принять?
7. «Убийца мёртвых» и «Порча Чёрта» — записи-варианты (`variant_of`); или псевдонимы «Изгнания Йде Итад» / «Иссушения»?
8. Военное дело: база 00% (Cold War) или 01% (London)? Запись — по Cold War.
9. Термины на подтверждение: SIS латиницей (а не «СИС»), Bruiser — «Громила» (голоса частей поровну).
10. Таблицы с броском (cw-a, london-a) — внутри правил; заводить `coc:table:wwc-*`?
11. Раненый шоггот (london-b, с. 94): БкУ/Комплекция без большинства (Р-36).
12. 6 карт-планов не видны в просмотрщике (audit `map.location_not_top`: numbers-station, raf-akrotiri, hanover-terrace,
    piccadilly-hotel-plans, st-jamess-hall-plans, williams-shipping-warehouse).
13. Audit по WWC: 70 мест прямо под городом с районами (Лондон, Москва, Стамбул), 19 подписей с возможными спойлерами,
    17 «мёртвых жителей» — разбирать?
14. Метка библиотеки [EN 6e] у книг линейки неверна (это 7-я редакция) — поправить имена файлов?
15. Эксхэмский приорат и Лагерь X — заводить места (нет места-родителя)?
