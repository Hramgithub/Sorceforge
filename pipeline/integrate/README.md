# Предложения правок общих записей (Р-139)

Помощник, который переносит часть книги, пишет только свои файлы. Правки записей, которыми он не владеет
(город, район, место другой части, персонаж из другой книги), он не вносит сам, а кладёт в файл предложений.
Сведение применяет их одной командой; каждое изменение значения само попадает в `corrections` записи.

## Файл

`<папка проверки>/proposals-<часть>.json`, схема — `schemas/proposal.schema.json`:

```json
{
  "schema": "sourcefold.proposals.v0",
  "by": "цель 2 рейда",
  "proposals": [
    {"target": "coc:location:innsmouth-306-uorren-billingem", "op": "append", "path": "residents",
     "value": {"id": "pobeg-iz-innsmuta-ru/character/rut-billingem", "note": "дочь"},
     "reason": "в доме живут жена и дочь Уоррена (с. 86)", "ref": "Р-134"},
    {"target": "coc:location:innsmouth-202-tyurma-innsmuta", "op": "replace", "path": "description.ru",
     "old": "План тюрьмы — в сценарии, с. 88.", "new": "План тюрьмы — в сцене «Тюрьма Иннсмута» (с. 88).",
     "reason": "ссылка на сцену вместо страницы", "ref": "Р-134"},
    {"target": "pobeg-iz-innsmuta-ru/scene/tsel-2-po-zamerzshey-reke", "op": "set", "path": "where.0.location",
     "value": "coc:location:innsmouth-reka-manukset", "reason": "заведена запись реки", "ref": "Р-134"}
  ]
}
```

| Операция | Что делает | Поля |
|---|---|---|
| `set` | ставит значение поля (новое поле верхнего уровня — после `after`) | `value`, `after` |
| `append` | добавляет элемент в список; если такой уже есть — пропуск | `value` |
| `remove` | убирает элементы списка, у которых поля равны `match` | `match` |
| `replace` | заменяет в тексте кусок `old` на `new`; `old` должен встречаться ровно один раз | `old`, `new` |

`path` — поле через точку, номер элемента списка числом: `description.ru`, `tables.3.rows`, `quality.notes`.
`reason` и `ref` (номер решения) идут в `corrections`; `"correction": false` — не записывать (например, ссылка для навигации).

## Применение

```
python pipeline/integrate/apply.py <файлы предложений> --dry-run   # проверить, что всё ложится
python pipeline/integrate/apply.py <файлы предложений>             # применить и проверить tools/check.py
```

Файл применяется целиком или никак: если хоть одно предложение не ложится (нет записи, кусок текста не найден или
найден дважды, удалять нечего), ничего не пишется, и инструмент называет предложение.
