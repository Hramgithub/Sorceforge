---
name: kb-integrate
description: Сведение работы помощников после переноса (Р-139) — нормализация изменённых файлов, применение предложений правок общих записей, проверка, разбор отчётов. Use after extraction agents of kb-import have finished.
---

# Сведение (Р-139)

1. Прочитать отчёты помощников: файлы, предложения, опечатки, сомнения, «Не взято».
2. Нормализация только изменённого:
   `python pipeline/fix/normalize_dice.py --changed`
   `python pipeline/fix/normalize_terms.py --changed`
   `python pipeline/fix/attribute_words.py --changed`
   `python pipeline/fix/errata_flag.py --changed`
   Никогда без границ: `--all` — только по решению владельца.
3. Предложения: `python pipeline/integrate/apply.py <check_dir>/proposals-*.json --dry-run`, затем без
   `--dry-run`. Не легло — поправить предложение (чаще всего кусок `old` не совпал), не править запись руками.
   Предложение, которое меняет смысл или противоречит решению, — сначала владельцу.
4. `python tools/check.py --changed`, затем `python tools/check.py` (ссылки по всей базе). Ошибок — 0.
5. Покрытие: в `<check_dir>/<часть>.md` у каждого заголовка книги есть «где в базе»; «Не взято» — с причиной.
6. Дальше — навык `kb-release`.
