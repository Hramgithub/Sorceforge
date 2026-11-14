# F8 существа (mm1, лор) — исправления по сверке контента (2026-11-15)

Пункт, не сделанный в F1 (`fix-F1.md`, строка «Описания по Keeper Deck вместо статей»; `mm1.md`, строка «Лор основных
статей»): у 45 записей существ, заведённых первыми по Malleus Keeper Deck, было лишь описание в 1–2 фразы. Добавлен лор
статей Malleus Monstrorum, т. I (облик, история, повадки, места, культы) в `legend` — наш перевод своими словами, полный
по фактам, без дословного воспроизведения длинных абзацев; числа профилей не трогались (их сверил F1). Скрипты и тексты
легенд — `scratchpad\fix-F8\` (`legends*.py`, `apply.py`).

| Пункт | Итог | Файлы |
|---|---|---|
| Лор статей Malleus в `legend` (≈11,5 тыс. слов) | сделано у всех 45 записей: `legend.ru` (флаг `translated`; добавлен там, где его не было, — тёмная молодь, югг); описание по колоде сохранено; страницы статьи Malleus в `sources` с `note` (что взято) и `entry_page`, Malleus переставлен первым источником (Р-22), существовавшие пометки источников сохранены; элемент `corrections` `legend.ru` (Р-247) с книгой и страницами. Врезки статей переведены в легенде: «Shambling Questions» (бродяга между измерениями), «Chant of Dismissal» (спектральный охотник), «A Better Formula» (реанимированный), «“Wendigoism”» (ходящий по ветру), «Lightning Gun: Model C» — облик (Великая Раса, конусовидная форма); вступительные курсивные зарисовки — их факты (облик, запах, повадки) вошли в легенды | `kb/creatures/`: `byakhee`, `carnivorous-plant`, `chakota`, `child-of-the-sphinx`, `cold-one`, `courtier-of-the-king-in-yellow`, `crawling-one`, `dark-young-of-shub-niggurath`, `daughter-of-atlach-nacha`, `death-vines-of-xiclotl`, `deep-one-hybrid`, `devil-s-weed-devil-plant`, `dimensional-shambler`, `dweller-in-the-depths`, `elder-thing`, `fire-vampire`, `fisher-from-outside`, `goatswood-gnome`, `great-race-of-yith-beetle-swarm-form`, `great-race-of-yith-cone-body-form`, `horror-from-the-depths`, `larvae-of-the-great-old-ones`, `martense-kin`, `mr-shiny`, `nightgaunt`, `nioth-korghai`, `reanimated`, `sand-dweller`, `scarecrow`, `servant-of-y-golonac`, `shoggoth-twsha`, `shoggoth`, `spawn-of-abhoth`, `spawn-of-hastur`, `spawn-of-ubbo-sathla`, `spectral-hunter`, `star-spawn-of-cthulhu`, `star-vampire`, `thrall-of-cthulhu`, `voormis`, `werewolf`, `wind-walker`, `worm-that-walks`, `yugg`, `zombie` |
| Описание, противоречащее статье | сделано: у «Червя, который ходит» описание («бывший колдун, чьё тело поглотили черви») не из книги — на карточке колоды (с. 54) описательного текста нет, а Malleus (с. 150–151) описывает иномирного червя с иллюзорными личинами; описание исправлено, прежнее — в `corrections` (Р-22). Остальные описания по колоде статье не противоречат и оставлены | `worm-that-walks.json` |
| Противоречие текста и профиля (найдено при переводе) | чакота: текст статьи — «DEX is always 1», профиль на той же странице — ЛВК 15 (Уклонение 7% подходит к 15); в записи 15 по профилю (Р-38), противоречие — в `errata` (`fixed: false`), флаг поставлен `errata_flag.py` | `chakota.json` |

## Не взято

- Механика разделов Powers (Spin Web, Feast, Dream Sending, Life Drain, Corrupting Influence, Hive Mind, Grab и т. п.) и
  способы упокоения зомби — уже есть в `abilities` записей; в легенде лишь упомянуты без чисел.
- Врезки статей, у которых есть свои записи или которые взял F1: «The Five Watchers» (`the-five-watchers`), «Dho-Spawn»
  (`dho-spawn`), «Beloved of Cthulhu» и таблица «Monstrous Deep One Hybrids» (`beloved-of-cthulhu`, `dolphin-hybrid`,
  `shark-hybrid`; в легенде гибрида — только лор), «The Three Oaths of Dagon», дневники Поплана (F1), «Scarlet Circles»
  (F1), «Body Parts Table» (уже в `abilities` реанимированного), правила стрельбы молниемёта модели C (в `abilities`).

## Вопросы владельцу

- `spawn-of-abhoth`: `name.ru` «Порождение Абота», а божество — «Абхот» (`coc:creature:abhoth`); в легенде написано
  «Абхот», «Порождение Абхота» уже есть в `aliases`. Переименовать запись в «Порождение Абхота»?

## Проверка

`python -B tools/check.py` по 45 файлам — ошибок 0, предупреждений 0. Предложений по чужим записям нет.
