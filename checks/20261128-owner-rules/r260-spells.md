# Р-260 — заклинания, названные без текста, 2026-11-28

Решение владельца Р-260: если в справочнике очевидно то же заклинание под другим именем — ссылка `spell` на него и имя книги
в `aliases`; иначе имя остаётся текстом, заглушки не заводятся. Скрипты — `.cache/lead-tools/apply-r258/spells_null.py`
(опись `spell: null` в WWC, Goat, New Tales, HOTOE, CoF — 59 мест) и `r260.py` (ссылки и псевдонимы).

## Связано (24 ссылки)

| Имя в книге | Где | Запись справочника |
|---|---|---|
| Call Daoloth; Summon the Render (Call Daoloth) | Айгюль Дегирменджи; том «The Heavens Beyond the Veils» (Cold War) | `coc:spell:call-dismiss-daoloth` |
| Contact Daoloth; Commune with the Render (Contact Daoloth) | Дегирменджи, Катырджи, Коч (Cold War), Марквардт (Covert Actions); том «Heavens…» | `coc:spell:contact-deity` |
| Contact Tawil at'Umr; Call the Most Ancient One (Contact Tawil at'Umr) | Экмекчи, Демирджи; том «Hidden Keys to the Locked Dimensions» (Cold War) | `coc:spell:contact-deity` |
| Contact Fthaggua; Invocation of Flame (Contact Fthaggua) | Аврора Уильямс; «Book of All Forbidden Arts» (London) | `coc:spell:contact-deity` |
| Call/Dismiss Fthaggua; Summon Herald of the True Flame (Call/Dismiss Fthaggua) | Аврора Уильямс; «Book of All Forbidden Arts» (London) | `coc:spell:call-deity` |
| Divination (Daoloth / Yog-Sothoth Variant); Behold the Future; Look Beyond Tomorrow | Дегирменджи, Катырджи, Коч, Экмекчи, Демирджи; оба тома Cold War | `coc:spell:divination` |
| Create Limbo Gate; Door to Nowhere (Create Limbo Gate) | Экмекчи, Демирджи; «Hidden Keys…» | `coc:spell:limbo-gate` |

Псевдонимы добавлены: `call-dismiss-daoloth` (Summon the Render), `contact-deity` (Contact Daoloth, Commune with the Render,
Contact Tawil at'Umr, Call the Most Ancient One, Contact Fthaggua, Invocation of Flame), `call-deity` (Call/Dismiss Fthaggua,
Summon Herald of the True Flame, Call/Dismiss Y’golonac, Вызов/изгнание И’голонака — ссылка New Tales была, имени не было),
`divination` (Divination (Daoloth Variant), Divination (Yog-Sothoth Variant), Behold the Future, Look Beyond Tomorrow),
`limbo-gate` (Create Limbo Gate, Door to Nowhere), `contact-spirits-of-the-dead` (Contact Dead — ссылка HOTOE была).
Уже были связаны при сведении: Bless (Калидасджи, CoF → `bless-folk`), Contact Dead (Мадам Аркана → `contact-spirits-of-the-dead`),
Call/Dismiss Y’golonac (Ронни Пайн → `call-deity`).

## Оставлено текстом (очевидного соответствия нет)

- Goat: «Call the Brood» (Лилит Рен), «Drain Essence» (Мать-Коза Топей), «Blessing of Boundless Fertility», «Summon Woodland
  creatures» (ДикаяМудраяЖенщина), «Hymn for the great nuptial union» (`tome/book-of-standing-stones`); «Dominate (mythos power)»
  — сила, не заклинание.
- New Tales: «Summon/Bind Leng Spider» — ни заклинания, ни общего семейства «Призыв/укрощение» в справочнике нет.
- HOTOE: «Animate Skin» (герцог дез Эссент и запись с «*»), «Command Flock*» (Бабушка), «Fez rituals».
- Cold War — заклинания с текстом в правилах `rule/spells-of-*`, справочник их не знает: Beseech Daoloth / Rend Ignorance,
  Temporal Cloak (Daoloth/Yog-Sothoth Variant) / Shroud of Veils / Hide Between the Seconds, Pentacle of the Planes / Star of
  Protection, Enchant Silver Key / Crafting the Key, Enchant Orb, Synchronicity / Ride on Time's Wave, Wrath of Yog-Sothoth /
  Touch of the Sphere. Это не случай Р-260 (текст в книге есть): заводить ли записи `coc:spell:*` — открытый вопрос 5 сведения WWC.
