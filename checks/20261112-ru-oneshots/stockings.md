# «Чулки возле печки» (`chulki-vozle-pechki-ru`) — сверка переноса (часть stockings)

Источник — фанатский перевод (Hort, vk.com/call_of_cthulhu_rpg) рождественского сценария Марка Харта «Hung by the Chimney
with Care» (блог Petersen Games, по лицензии Chaosium); метка владельца `[RU-фан 7e]`, издание `trusted` (Р-227).
PDF 17 страниц с хорошим текстовым слоем; статблоки (с. 13–14) и заклинания (с. 15) сверены по изображениям страниц.
Английского оригинала в библиотеке нет — числа по переводу. Правила — 7-я редакция (проценты с долями, ПЗ/ПМ, Комплекция),
`ruleset` core; эпоха — «под Рождество любого из 1920-х годов» (с. 1) → `1920s`.
Все записи — с флагом `translated` (по заданию партии 4, см. вопрос ниже).

## Страницы

Смещение `chulki-vozle-pechki-ru`: **печатная = физическая** — номера внизу страниц 1–17 совпадают с PDF (проверено по изображениям).

## Заголовки книги

| Заголовок книги | Страница | Где в базе |
|---|---|---|
| «Чулки возле печки развешены в ряд», Марк Харт (+ сведения об оригинале и переводчике) | 1 | сценарий `chulki-vozle-pechki-ru/scenario/chulki-vozle-pechki` (name, summary, sources) |
| Вступление | 1 | сценарий: summary; `…/location/gorod-stsenariya` |
| Информация для Хранителя | 1 | сценарий: keeper_info; `…/character/uinston-speys`, `…/character/nataniel-pemont`, `…/character/edmund-lyuis`; `…/organization/obshchestvo-toro`; `…/tome/otkroveniya-glaaki-tom-12`; `…/creature/igolonak-v-tele-edmunda-lyuisa` |
| И'Голонак (врезка) | 2 | `…/creature/igolonak-v-tele-edmunda-lyuisa` (description, способность «Призыв по имени»); сценарий: keeper_info |
| Мольба о помощи (+ бланк телеграммы Western Union) | 2 | сценарий: hook, шаг 1; раздатка `…/handout/telegramma-pemonta` |
| Хмурый сочельник | 3 | сцена `…/scene/khmuryy-sochelnik`; места `…/location/glavnaya-ulitsa`, `…/location/univermag` |
| Встреча в отеле | 3 | сцена `…/scene/vstrecha-v-otele`; место `…/location/otel-dankhem`; `…/character/uolter-griffin` (портье); `…/item/portfel-pemonta`, `…/handout/zapiska-pemonta`, `…/item/klyuch-ot-abonentskogo-yashchika` |
| Начало расследования | 3–4 | сценарий: advice (список направлений, по пунктам как в книге) |
| Почта | 4 | сцена `…/scene/pochta`; место `…/location/pochta`; `…/character/meybl`; `…/item/vypiski-pemonta`, `…/item/plakaty-propal-chelovek`; пропавшие `…/character/entoni-klark`, `…/character/mira-klark`, `…/character/klayd-khuper`, `…/character/bayron-kharmon` |
| Редакция газеты | 4–5 | сцена `…/scene/redaktsiya-gazety`; место `…/location/redaktsiya-gazety`; `…/character/uinifred-obri`, `…/character/karlton-benks`; `…/item/foto-obshchestva-toro`, `…/item/foto-lyuisa-santy`, `…/item/foto-iz-morga`; убитые `…/character/sara-skott`, `…/character/darvin-telbot`, `…/character/deyvis-griggs`, `…/character/robert-latem`; `…/location/gorodskaya-bolnitsa` |
| Места преступлений | 5–6 | сцена `…/scene/mesta-prestupleniy`; место `…/location/dom-latemov`; `…/character/meri-latem`, `…/character/billi-latem` |
| Лучше один раз увидеть... | 6 | сцена `…/scene/luchshe-odin-raz-uvidet`; `…/item/risunok-billi` |
| Полиция | 6–7 | сцена `…/scene/politsiya`; место `…/location/politseyskiy-uchastok`; `…/character/khenk-erikson`; сценарий: advice |
| Прогулка по городу | 7 | сцена `…/scene/progulka-po-gorodu` (слухи по пунктам как в книге); `…/character/peysli-lyuis` |
| Засада | 8 | сцена `…/scene/zasada`; `…/character/bandity-speysa` |
| Сохраняем темп расследования | 8 | сценарий: advice |
| Дальнейшие шаги | 8–9 | сценарий: advice, шаг «Дальнейшие шаги» |
| «Реликвии былого» | 9 | сцена `…/scene/relikvii-bylogo`; места `…/location/relikvii-bylogo`, `…/location/tserkov-svyatogo-marka` |
| Дом Хэглунда | 9–10 | сцена `…/scene/dom-kheglunda`; место `…/location/dom-kheglunda`; `…/character/dzhordzh-kheglund`, `…/character/margaret-kheglund` |
| Слежка за домом Хэглунда | 10 | сцена `…/scene/slezhka-za-domom-kheglunda` |
| Посещение Санты | 10–11 | сцена `…/scene/poseshchenie-santy`; место `…/location/gorodskoe-kladbishche` |
| Кульминация | 11–12 | сцена `…/scene/kulminatsiya`; место `…/location/podval-relikviy-bylogo`; `…/item/altar-speysa`; `…/tome/otkroveniya-glaaki-tom-12` (copies: сейф) |
| Итоги | 12 | сценарий: conclusion |
| Награды | 12 | сценарий: conclusion (по пунктам); награды и в карточках Пьемонта, Хэглунда, Спэйса, сцене слежки |
| Характеристики персонажей: Хэнк Эриксон, 36 | 13 | `…/character/khenk-erikson` (statblock) |
| Киган Дюкесне, 29 | 13 | `…/character/kigan-dyukesne` (statblock, заклинания) |
| Натаниэль Пьемонт, 56 | 13 | `…/character/nataniel-pemont` (statblock) |
| Бандиты | 14 | `…/character/bandity-speysa` (групповой профиль, `names`) |
| Уинтон Спэйс | 14 | `…/character/uinston-speys` (statblock, заклинания) |
| И'Голонак (характеристики) | 14–15 | `…/creature/igolonak-v-tele-edmunda-lyuisa` (statblock, `instance_of` → `coc:creature:ygolonac`) |
| Заклинания: Изгнание Совратителя (Banishment of the Defiler) | 15 | механика — `…/item/vypiski-pemonta`; в `…/tome/otkroveniya-glaaki-tom-12` (spell: null); новое заклинание — черновик в отчёте |
| Затуманивание памяти (Cloud Memory) | 15 | `coc:spell:cloud-memory` (у Дюкесне) |
| Воззвание к мёртвым (Contact Spirits of the Dead) | 15 | у Дюкесне (spell: null); новое заклинание — черновик в отчёте |
| Дурной глаз (Evil eye) | 16 | `coc:spell:evil-eye` (у Дюкесне) |
| Господство (Dominate) | 16 | `coc:spell:dominate` (у Спэйса) |
| Порабощение жертвы (Enthrall victim) | 16 | `coc:spell:enthrall-victim` (у Спэйса; псевдоним — в предложениях) |
| Мысленное внушение (Mental suggestion) | 16 | `coc:spell:mental-suggestion` (у Спэйса) |
| Разрушение (Wrack) | 16–17 | `coc:spell:wrack` (у Спэйса) |
| (город действия — не назван, «Средний Запад») | 1 | `…/location/gorod-stsenariya` (Р-190) |

## Опечатки книги (errata)

- Киган Дюкесне: ПМ 19 при МОЩ 70 (должно 14) — как напечатано.
- Бандиты: ПМ 9 при МОЩ 35 (должно 7) — как напечатано.
- И’голонак сценария: драка 25%, урон 1d3 без БкУ +2d6, уклонение 25%, шанс укуса не напечатан — похоже на перенесённый профиль человека (в «Книге хранителя» 100%, 2d6, укус 80%, уклонение 40%); как напечатано.
- «Уинтон Спэйс» в заголовке статблока (в тексте «Уинстон»), «Хаглунд»/«Хэглунд», «Натан»/«Натаниэль» — в псевдонимах и `quality.notes`.
- Заклинание Contact Spirits of the Dead названо в статблоке «Связь с духами мёртвых», в разделе «Заклинания» — «Воззвание к мёртвым» (пометка у Дюкесне).

## Выведено (Р-41), с пометкой в записях

- Сара Скотт и Мира Кларк — члены «Общества Торо» (книга называет членами только тех, кто на фото; И’голонак охотится на членов общества).
- Жалующийся владелец магазина, чей адвокат «прячется дома», — речь о Хэглунде (сцена «Прогулка по городу»).
- Универмаг — на главной улице.
- Придуманы имена (Р-150, Р-151, `editorial_text`): портье — Уолтер Гриффин; миссис Хэглунд — Маргарет Хэглунд; пять имён для группы бандитов.

## Не взято

| Что | Страница | Причина |
|---|---|---|
| Иллюстрация И’голонака | 2 | картинки в `app/art/` — не в части; кандидат на `pipeline/art/add_images.py` для владельца |
| Оформление бланка Western Union (шапка, служебные надписи) | 2 | оформление; текст телеграммы — в раздатке |
| Тексты заклинаний Затуманивание памяти, Дурной глаз, Господство, Порабощение жертвы, Мысленное внушение, Разрушение | 15–17 | пересказ «Книги хранителя»; стоимости и время совпадают с общими записями — ссылки на них, правки не нужны |
| Сын Хэглунда, сестра Мэри Латэм, полицейский за рулём, соседи Хэглунда, друг Обри в морге, житель, доставлявший товар в «Реликвии», раздражённый владелец магазина | 3–10 | безымянные статисты без характеристик и своей роли — остаются в тексте сцен и мест |
| Дома остальных жертв (Скотт, Тэлбот, Григгс) | 5–6 | адресов и описаний в книге нет — общий текст в сцене «Места преступлений» и в городе |
| Сейф Спэйса, машина бандитов, грузовик | 9, 11 | без своей записи — в описании места и сцен |

## Карты

Карт и планов в книге нет — записей `map` и картинок `app/maps/stockings-*` нет.

## Новые заклинания (черновики для `kb/spells`, справочник не в части)

- «Изгнание Совратителя» (Banishment of the Defiler) — с. 15; «Воззвание к мёртвым» (Contact Spirits of the Dead, в статблоке — «Связь с духами мёртвых») — с. 15. Черновики — в отчёте части ведущему.

## Предложения

`proposals-stockings.json` — 7: псевдонимы `coc:creature:ygolonac` («И'Голонак», «Совратитель», «Длань Питающая»), `coc:spell:enthrall-victim` («Порабощение жертвы»), `coc:spell:contact-ygolonac`; ссылки из `coc:tome:revelations-of-glaaki` на том XII и из `coc:location:chicago` на Пьемонта. Пробный прогон `apply.py --dry-run` проходит.
