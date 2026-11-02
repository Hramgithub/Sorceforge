---
name: kb-check
description: Проверка базы знаний — схемы, ссылки, правила записи, формат файлов — и разбор найденного. Use before every commit of kb data, after any edit of kb records, or when the owner asks whether the base is consistent.
---

# Проверка базы

- Всё: `python tools/check.py`; изменённое: `python tools/check.py --changed`; файлы: `python tools/check.py <пути>`.
  Ссылки и повторы id проверяются по всей базе всегда.
- Ошибки чинить по сообщению: в каждом названо правило и номер решения; формат файла —
  `python pipeline/fix/normalize_terms.py <файл>`; флаг опечатки — `python pipeline/fix/errata_flag.py <файл>`.
- Изменение значения существующей записи — с `corrections` (field, from, to, reason, ref «Р-NN» или null).
- Новое правило, которое скрипт может проверить, добавляется в `tools/check.py` вместе с решением и
  строкой в `docs/conventions.md`; сначала прогнать на всей базе, найденное — владельцу.
