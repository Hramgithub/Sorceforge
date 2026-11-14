# F4 Grand Grimoire — исправления по сверке контента

Строка «F4 Grand Grimoire» из `summary.md`, подробности — `gg.md`. Книга `grand-grimoire-en` (физ. = печ. + 1). Скрипты —
`scratchpad\fix-F4\` (`apply_spells.py`, `apply_rules.py`, `cats.py`, `verify_cats.py`). Каждое изменение — в `corrections`
записи; наш перевод с английского — флаг `translated` и пометка в `quality.notes`.

| Пункт | Итог | Файлы |
|---|---|---|
| Глубинная магия GG у 6 заклинаний | сделано: поле `deeper_magic` по с. 68, 102, 98, 129, 146, 173; где глубинная магия на следующей странице — добавлен источник GG с этой страницей | `kb/spells/cloud-memory.json`, `dread-curse-of-azathoth.json`, `dowsing-folk.json`, `ill-luck-folk.json`, `nyhargo-dirge.json`, `spirit-summoning.json` |
| Версия GG у Balk Brood | сделано: механика GG (ПМ×5 против дней×5 у Хранителя, 1d4 Рассудка и 1 ПЗ за день, Эйхорт 10% и +10%) — в `quality.notes` (Р-51), числа записи — по «Не забывай меня»; ошибочная пометка источника GG («(Chthonian)», «альтернативных названий нет») исправлена; добавлен источник с. 35 | `kb/spells/balk-brood.json` |
| 30 альтернативных названий | сделано: все 30 в `aliases` 10 записей (по одной поправке на название, Р-96) | `balk-brood`, `become-spectral`, `disembodiment`, `dowsing-folk`, `free-hastur`, `ill-luck-folk`, `nyhargo-dirge`, `poison-blood-folk`, `spirit-summoning`, `winds-of-desolation-folk` |
| Spirit Summoning | сделано: числа и механика GG (ПМ×5 — шанс, круг добавляет ПМ, 1d4 Рассудка, 1d4 раунда, уход духа по встречной МОЩ) и расхождение с «Грибами с Юггота» — в `quality.notes`; источник с. 173 | `kb/spells/spirit-summoning.json` |
| Become Spectral Hunter | сделано: подробности врезки (не дальше 1,6 км от фигурки, 1d8 урона за повреждение, возврат через 7 дней, уничтожение — фигурка + «Песнопение изгнания») — абзацем в описании | `kb/spells/become-spectral-hunter.json` |
| Таблица 2 «Time Gate Creation and Travel Costs» | сделано: новая запись правила с таблицей (14 строк, сверено по изображению с. 180); у «Врат времени» — ссылка и пометка. Скачок 10 000 → 10 000 000 лет оставлен как напечатан (в пометке таблицы); лишняя запятая «10,000,000,years» убрана (Р-39) | `kb/rules/gg-time-gate-creation-and-travel-costs.json` (новая), `kb/spells/time-gate.json` |
| Категории гл. 3 (6 неверных сопоставлений) | сделано: Combat — «Исчезновение» вместо «Шкатулок врат»; Harmful — «Сглаз», «Плавление плоти», + «Приподнять завесу» (41); Influencing Others — «Сглаз»; Enchantments + «Зачаровать копьё» (38); Protection + «Печать Нефрен-Ка» (33); Travel + «Исчезновение» (22); в `refs` добавлены 6 заклинаний; `curse-folk`, `liquid-death`, `gate-boxes` остались — они есть в своих списках (Folk, Combat, Travel). Найдено попутно: в Dreamlands было 56 названий при счётчике 57 — Bring Pestilence (II) и Summon Plague слились из-за общего «Наслать мор»; добавлено «Призвать чуму». Проверено скриптом: число названий в каждой из 17 строк равно счётчику книги, каждое название однозначно ведёт на запись из `refs`, лишних ссылок нет | `kb/rules/gg-spell-categories.json` |
| Пример магии Страны грёз | пример уже был в `examples`; сделано: ссылки на `devolution` и `opaque-wall` (записи теперь есть), устаревшая пометка «заклинаний нет в базе» убрана, название в примере — по записи («Деградация») | `kb/rules/gg-dreamlands-magic.json` |
| Дубль «Наслать мор» | сделано: Bring Pestilence остаётся «Наслать мор», Summon Plague — «Призвать чуму» (наш перевод, как и прежнее); старое название в `aliases` не оставлено — оно совпадает с названием другой записи (Р-95), только в `corrections` | `kb/spells/summon-plague.json` |
| Профили GG Spectral Hunter, Human Hybrid Tindalosian | предложения: источник GG и пометка о расхождении с Malleus (числа по MM, Р-22); гибриду — псевдоним «Human Hybrid Tindalosian» | `proposals-F4.json` |
| Профиль Fog Spawn из врезки GG | предложение: числа совпадают с «Масками» — источник GG к `masks-of-nyarlathotep-en/creature/fog-spawn` и пометка о единственном расхождении (переход под солнцем 10 минут против «минуты-другой») | `proposals-F4.json` |

`python -B tools/check.py` по всем изменённым файлам — ошибок 0, предупреждений 0; `apply.py proposals-F4.json --dry-run` —
7 правок ложатся.

## Не сделано / вне задания

- Портрет Томаса Дэвенпорта (`gg.md`, раздел «Персонажи-колдуны») — в строке F4 `summary.md` его нет, в задание не входил.
- Запись туруа (кандидат в существо) и Fog Spawn как общая запись — не заводились (вопрос владельцу из `gg-spells.md` открыт).

## Замечено попутно (не правилось)

- `coc:spell:free-hastur`: в `cost.raw` — «очко ВОЛ» (из фанатского перевода «Тёмных веков»); в остальном тексте базы — МОЩ.
- `coc:spell:dowsing-folk`, `ill-luck-folk`, `nyhargo-dirge`, `become-spectral` и др. стоят с эпохой только `dark-ages`, хотя
  Grand Grimoire (ядро 7e) печатает их без привязки к эпохе.
