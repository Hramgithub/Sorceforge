# Sorceforge

Репозиторий проекта **Sourcefold** (название продукта; `Sorceforge` — только
имя репозитория). Сейчас здесь строится **база знаний по «Зову Ктулху» 7-й
редакции**: данные — JSON в git, книги — источники, веб-помощник
`git_coc/web_helper_coc_gm` — образец и источник русских формулировок.

## Состояние (2026-11-05)

| Что | Где | Сколько |
|---|---|---|
| Существа | `kb/creatures/`, `kb/books/<книга>/creatures/` | 397 |
| Персонажи | `kb/characters/`, `kb/books/<книга>/characters/` | 543 |
| Навыки | `kb/skills/` | 139 |
| Профессии | `kb/occupations/` | 114 |
| Заклинания | `kb/spells/` | 292 |
| Книги Мифов | `kb/tomes/`, `kb/books/<книга>/tomes/` | 127 |
| Оружие | `kb/weapons/` | 133 |
| Места | `kb/locations/` | 144: Иннсмут с районами, домами, комнатами, окраинами, Й'ха-нтлеи |
| Карты | `kb/maps/`, картинки в `app/maps/` | 7 карт «Побега из Иннсмута» с метками |
| Сюжет | `kb/books/<книга>/scenarios`, `scenes`, `items`, `handouts`, `organizations` | «Побег из Иннсмута»: 9 сценариев, 112 сцен, 10 предметов, 16 документов, 5 организаций |

- Источники: «Книга хранителя», «Книга сыщика», Malleus Monstrorum 7e и колода, Grand Grimoire,
  «Маски Ньярлатхотепа» 7e, «Побег из Иннсмута», готовые сыщики сценариев; список книг —
  `pipeline/source/books.json`.
- Правила записи данных — `docs/conventions.md`; цель, решения Р-01…Р-160 и статус —
  `docs/project-goal.md`; контекст для продолжения — `docs/handoff/20261021-kb-state.md`;
  перенос книги — конвейер `pipeline/README.md`.

## Как смотреть и проверять

```bash
python tools/check.py
```

Проверяет всю базу: схемы, ссылки, правила записи, формат файлов (`--changed` — только изменённое).

```bash
python tools/build_viewer.py
```

Собирает `app/kb.html` — просмотрщик (существа, персонажи, навыки, профессии, заклинания и книги,
оружие, гайды по городам с картами и сценариями); открывается в браузере без сервера.

```bash
python tools/kb_server.py
```

Тот же просмотрщик на http://localhost:8765/kb.html с сохранением правки меток карт в базу (Р-160).
## Публикация

Просмотрщик опубликован на `https://kb.kamaztelevizorov.ru`: лендинг `app/index.html` открыт
всем, сама база `kb.html` — под паролем (basic auth). Лендинг собирается тем же
`tools/build_viewer.py` из `tools/landing.template.html`, счётчики подставляются из `kb/`. Тот же
VPS, что и Foundry VTT, но отдельный пользователь `kb` без sudo и без доступа к
данным Foundry; nginx-сайт `/etc/nginx/sites-available/kb`, файлы в `/srv/kb`.

```powershell
.\tools\deploy_kb.ps1 -Build            # пересобрать app/kb.html и выложить
.\tools\deploy_kb.ps1 -Rollback list    # релизы на сервере
.\tools\deploy_kb.ps1 -Rollback <id>    # вернуть предыдущий релиз
```

SSH-ключ пользователя `kb` ищется в `-ServerKey`, `KB_SERVER_KEY_PATH`,
`..\NRI\.ssh\kb_deploy`, `~\.ssh\kb_deploy`; в репозиторий не коммитится.
Пароли сайта — `htpasswd /etc/nginx/kb.htpasswd <имя>` под root.

## Что где

| Каталог | Содержимое |
|---|---|
| `docs/project-goal.md` | рабочий документ: цель, модель предметной области, решения, статус |
| `schemas/` | JSON-схемы и описание полей (`schemas/README.md`), примеры |
| `kb/` | данные базы |
| `app/` | просмотрщик: `kb.html` (собирается `tools/build_viewer.py` из `tools/kb.template.html`), `index.html` открывает его |
| `tools/` | проверка базы (`check.py`), сборка просмотрщика, локальный сервер, валидатор схем, выкладка |
| `pipeline/` | конвейер переноса книг (`README.md`): книги и страницы (`source/`), задания помощникам (`briefs/`), предложения правок (`integrate/`), массовые правки (`fix/`), прежние переносы (`migrate/`) |
| `checks/` | сверки с книгами, планы переносов, файлы предложений |
| `proposals/` | предложения изменений из сценариев и решения по ним |
| `docs/history/` | предыстория: аудит идеи и реализации старого Sourcefold (2026-10-13); прочие старые материалы — в истории репозитория (до коммита этой очистки) и в NRI |

## Где старый код

| Что | Где |
|---|---|
| Sourcefold Phase 0 (скрипты, тесты, фикстуры, evidence, роадмап) | `https://github.com/Hramgithub/NRI`, каталог `Sourcefold/` (коммит `22fafc14`); локально `C:\_Hobby\_work\NRI\Sourcefold` |
| kb_creator | `https://github.com/Hramgithub/NRI`, каталог `kb_creator/`; локально `C:\_Hobby\_work\NRI\kb_creator` |
| Полный снимок до очистки | история этого репозитория, коммит `72ea9be` |

Артефакты MinerU лежат вне репозитория: `C:\_Hobby\_work\NRI\Mineru_tmp`.
Правила работы — `AGENTS.md`.
