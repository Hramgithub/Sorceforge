"""Export Foundry world tables and rule journals to readable JSON and Markdown.

usage: python -I export.py world_dump.json packs_dump.json OUT_DIR
"""
import collections, difflib, html, json, re, sys
from html.parser import HTMLParser
from pathlib import Path

world = json.load(open(sys.argv[1], encoding='utf8'))
packs = json.load(open(sys.argv[2], encoding='utf8'))
OUT = Path(sys.argv[3])
W = world['collections']

TR = dict(zip('абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
              ['a','b','v','g','d','e','e','zh','z','i','y','k','l','m','n','o','p','r','s','t','u','f','kh','ts','ch','sh','shch','','y','','e','yu','ya']))
def slug(s):
    s = ''.join(TR.get(c, c) for c in s.lower())
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

# ---------- HTML -> Markdown ----------
class MD(HTMLParser):
    BLOCK = {'p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'ul', 'ol', 'table', 'hr', 'blockquote'}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.buf = []; self.lists = []; self.table = None; self.cell = None; self.heading = None
    def flush(self, prefix=''):
        t = re.sub(r'[ \t]+', ' ', ''.join(self.buf)).strip()
        self.buf = []
        if t:
            self.out.append(prefix + t)
    def handle_starttag(self, tag, attrs):
        if self.cell is not None:
            if tag in ('p', 'li', 'br') and self.cell:
                self.cell.append(' ')
            if tag in ('strong', 'b'): self.cell.append('**')
            if tag == 'code': self.cell.append('`')
            return
        if tag in ('strong', 'b'): self.buf.append('**')
        elif tag in ('em', 'i'): self.buf.append('*')
        elif tag == 'code': self.buf.append('`')
        elif tag == 'br': self.buf.append('  \n')
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            self.flush(); self.heading = '#' * (int(tag[1]) + 1) + ' '
        elif tag in ('ul', 'ol'):
            self.flush(); self.lists.append([tag, 0])
        elif tag == 'li':
            self.flush()
            kind = self.lists[-1] if self.lists else ['ul', 0]
            kind[1] += 1
            self.li_prefix = '  ' * (len(self.lists) - 1) + ('- ' if kind[0] == 'ul' else f'{kind[1]}. ')
        elif tag == 'table':
            self.flush(); self.table = []
        elif tag == 'tr' and self.table is not None:
            self.table.append([])
        elif tag in ('td', 'th') and self.table is not None:
            self.cell = []
        elif tag == 'hr':
            self.flush(); self.out.append('---')
        elif tag in self.BLOCK:
            self.flush(self.cur_prefix())
    def cur_prefix(self):
        return getattr(self, 'li_prefix', '') if self.lists else ''
    def handle_endtag(self, tag):
        if self.cell is not None:
            if tag in ('strong', 'b'): self.cell.append('**')
            elif tag == 'code': self.cell.append('`')
            elif tag in ('td', 'th'):
                txt = re.sub(r'\s+', ' ', ''.join(self.cell)).strip().replace('|', '\\|')
                self.table[-1].append(txt); self.cell = None
            return
        if tag in ('strong', 'b'): self.buf.append('**')
        elif tag in ('em', 'i'): self.buf.append('*')
        elif tag == 'code': self.buf.append('`')
        elif tag in ('h1', 'h2', 'h3', 'h4'):
            t = re.sub(r'\s+', ' ', ''.join(self.buf)).strip(); self.buf = []
            if t: self.out.append(self.heading + t)
            self.heading = None
        elif tag == 'li':
            self.flush(self.cur_prefix())
        elif tag in ('ul', 'ol'):
            self.flush(self.cur_prefix())
            if self.lists: self.lists.pop()
            if not self.lists: self.out.append('')
        elif tag == 'table' and self.table is not None:
            rows = [r for r in self.table if r]
            if rows:
                n = max(len(r) for r in rows)
                rows = [r + [''] * (n - len(r)) for r in rows]
                self.out.append('')
                self.out.append('| ' + ' | '.join(rows[0]) + ' |')
                self.out.append('|' + ' --- |' * n)
                for r in rows[1:]:
                    self.out.append('| ' + ' | '.join(r) + ' |')
                self.out.append('')
            self.table = None
        elif tag in ('p', 'div', 'section', 'blockquote'):
            if self.lists:
                # paragraph inside a list item: keep in the item
                self.buf.append(' ')
            else:
                self.flush(); self.out.append('')
    def handle_data(self, data):
        if self.cell is not None: self.cell.append(data)
        else: self.buf.append(data)
    def result(self):
        self.flush()
        text = '\n'.join(self.out)
        text = re.sub(r'\*\*\s*\*\*', '', text)
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip() + '\n'

def h2md(h):
    if not h: return ''
    p = MD(); p.feed(h); p.close(); return p.result()

# ---------- index ----------
def index(entries, coll):
    docs = {v['_id']: v for k, v in entries if k.startswith(f'!{coll}!')}
    emb = collections.defaultdict(list)
    for k, v in entries:
        if k.startswith(f'!{coll}.'):
            emb[k.split('!')[2].split('.')[0]].append(v)
    return docs, emb

folders = {v['_id']: v for k, v in W['folders']}
def fpath(fid):
    parts = []
    while fid and fid in folders:
        parts.append(folders[fid]['name']); fid = folders[fid].get('folder')
    return ' / '.join(reversed(parts))

tables, results = index(W['tables'], 'tables')
journals, pages = index(W['journal'], 'journal')
ptables, presults = index(packs['packs']['am'], 'tables')
pjournals, ppages = index(packs['packs']['lj'], 'journal')

TABLE_ORDER = ['Безумие в реальном времени', 'Безумие в прошедшем времени', 'Примеры фобий', 'Примеры маний', 'Зоны попаданий']
JOURNAL_ORDER = ['Журнал Рассудка', 'Правила: Алкоголь, яды и т.д.', 'Правила: Бой — кратко', 'Правила: Быстро за столом',
                 'Правила: Магия и книги', 'Правила: Навыки и развитие', 'Правила: Необязательные правила', 'Правила: Погони — кратко',
                 'Правила: Подготовка сценария', 'Правила: Проверки и кости', 'Правила: Расследование', 'Правила: Рассудок и здоровье',
                 'Правила: Советы Хранителю', 'Правила: Характеристики и ресурсы']
sel_tables = sorted(tables.values(), key=lambda t: (TABLE_ORDER.index(t['name']), t['_stats']['createdTime']))
sel_journals = sorted([j for j in journals.values() if j['name'] in JOURNAL_ORDER], key=lambda j: JOURNAL_ORDER.index(j['name']))
assert len(sel_tables) == 7 and len(sel_journals) == 14, (len(sel_tables), len(sel_journals))

def origin(doc):
    src = doc['_stats'].get('compendiumSource')
    if not src: return 'создано в мире (не из компендиума)'
    return src

def iso(ms):
    import datetime
    return datetime.datetime.fromtimestamp(ms / 1000, datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC') if ms else ''

# ---------- raw JSON (one file per document, embedded docs inline, like `fvtt package unpack`) ----------
raw_t = OUT / 'raw' / 'tables'; raw_j = OUT / 'raw' / 'journals'
raw_t.mkdir(parents=True, exist_ok=True); raw_j.mkdir(parents=True, exist_ok=True)
def dump(path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf8', newline='\n')

table_files = {}
for t in sel_tables:
    doc = dict(t); doc['results'] = sorted(results[t['_id']], key=lambda r: r['range'][0])
    doc['_folderPath'] = fpath(t.get('folder'))
    name = f"{slug(t['name'])}.{t['_id']}.json"; table_files[t['_id']] = name
    dump(raw_t / name, doc)
journal_files = {}
for j in sel_journals:
    doc = dict(j); doc['pages'] = sorted(pages[j['_id']], key=lambda p: p.get('sort', 0))
    doc['_folderPath'] = fpath(j.get('folder'))
    name = f"{slug(j['name'])}.{j['_id']}.json"; journal_files[j['_id']] = name
    dump(raw_j / name, doc)
used = {t.get('folder') for t in sel_tables} | {j.get('folder') for j in sel_journals}
dump(OUT / 'raw' / 'folders.json', [{'_id': f['_id'], 'type': f['type'], 'name': f['name'], 'path': fpath(f['_id']), 'parent': f.get('folder')}
                                    for f in sorted(folders.values(), key=lambda f: (f['type'], fpath(f['_id']))) if f['type'] in ('RollTable', 'JournalEntry')])

# ---------- tables.md ----------
L = ['# Таблицы мира «Зов Глубин Ктулху» (Foundry)', '',
     f"Выгрузка {world['dumpedAt'][:10]} из базы мира `zov-glubin-ktulhu` (LevelDB `data/tables`). Сырые документы — `raw/tables/`.", '']
for t in sel_tables:
    rs = sorted(results[t['_id']], key=lambda r: r['range'][0])
    L += [f"## {t['name']}", '',
          f"- Папка: {fpath(t.get('folder'))}",
          f"- Формула: `{t.get('formula')}`, строк: {len(rs)}",
          f"- Происхождение: {origin(t)}",
          f"- Создана: {iso(t['_stats'].get('createdTime'))}; изменена: {iso(t['_stats'].get('modifiedTime'))}",
          f"- Файл: `raw/tables/{table_files[t['_id']]}`", '']
    if t.get('description'):
        L += ['**Описание таблицы:**', '', h2md(t['description']).strip(), '']
    L += ['| Бросок | Результат | Описание |', '| --- | --- | --- |']
    for r in rs:
        a, b = r['range']; rng = str(a) if a == b else f'{a}–{b}'
        name = (r.get('name') or '').replace('|', '\\|').strip()
        desc = re.sub(r'\s*\n\s*', ' ', h2md(r.get('description') or '')).strip().replace('|', '\\|')
        L.append(f'| {rng} | {name} | {desc} |')
    L.append('')
(OUT / 'tables.md').write_text('\n'.join(L), encoding='utf8', newline='\n')

# ---------- journals/*.md ----------
jdir = OUT / 'journals'; jdir.mkdir(exist_ok=True)
jindex = []
for n, j in enumerate(sel_journals, 1):
    ps = sorted(pages[j['_id']], key=lambda p: p.get('sort', 0))
    fname = f"{n:02d}-{slug(j['name'])}.md"
    jindex.append((j, fname, len(ps)))
    L = [f"# {j['name']}", '',
         f"- Папка мира: {fpath(j.get('folder'))}",
         f"- Происхождение: {origin(j)}",
         f"- Создан: {iso(j['_stats'].get('createdTime'))}; изменён: {iso(j['_stats'].get('modifiedTime'))}",
         f"- Страниц: {len(ps)}; сырой документ: `raw/journals/{journal_files[j['_id']]}`", '']
    for p in ps:
        L += [f"## {p['name']}", '']
        if p['type'] != 'text':
            L += [f"*(страница типа `{p['type']}`, src: `{p.get('src')}`)*", '']
        L += [h2md((p.get('text') or {}).get('content')).strip(), '']
    (jdir / fname).write_text('\n'.join(L).rstrip() + '\n', encoding='utf8', newline='\n')

# ---------- world vs module ----------
def norm_md(h):
    md = h2md(h)
    md = re.sub(r'^\*\*ID:\*\* `[\w-]+`\s*$', '', md, flags=re.M)
    md = re.sub(r'^- `id`: .*$', '', md, flags=re.M)
    return [l for l in md.splitlines() if l.strip()]
def plain(h):
    t = re.sub(r'<[^>]+>', ' ', h or ''); t = re.sub(r'\s*ID:\s+[\w-]+', '', html.unescape(t))
    return re.sub(r'\s+', ' ', t).strip()

D = ['# Что изменено в мире по сравнению с модулем', '',
     f"Сравнение журналов «Правила: …» мира `zov-glubin-ktulhu` с паком `nri-coc-library.library-journals` "
     f"(развёрнутая на сервере версия модуля `{packs['nriLibraryVersion']}`; данные карточек в git не менялись с 2026-08-04, "
     "то есть с момента импорта в мир). Различия только в оформлении (строка `ID:` перенесена, пробелы) не показаны.", '']
summary = []
for j in sel_journals:
    src = pjournals.get(j['_id'])
    if not src: continue
    sp_by_id = {p['_id']: p for p in ppages[j['_id']]}; sp_by_name = {p['name']: p for p in ppages[j['_id']]}
    block = []
    for p in sorted(pages[j['_id']], key=lambda p: p.get('sort', 0)):
        s = sp_by_id.get(p['_id']) or sp_by_name.get(p['name'])
        wh = (p.get('text') or {}).get('content');
        if not s:
            block += [f"### + Новая страница: {p['name']}", '', 'Есть только в мире. Текст — в `journals/`.', '']
            summary.append((j['name'], p['name'], 'новая'))
            continue
        sh = (s.get('text') or {}).get('content')
        if plain(wh) == plain(sh) and p['name'] == s['name']:
            continue
        title = p['name'] if p['name'] == s['name'] else f"{p['name']} (в модуле: «{s['name']}»)"
        diff = list(difflib.unified_diff(norm_md(sh), norm_md(wh), 'модуль', 'мир', lineterm='', n=1))
        block += [f"### ~ Изменена: {title}", '', '```diff'] + diff[2:] + ['```', '']
        summary.append((j['name'], p['name'], 'изменена'))
    wn = {p['name'] for p in pages[j['_id']]}; wi = {p['_id'] for p in pages[j['_id']]}
    for s in ppages[j['_id']]:
        if s['_id'] not in wi and s['name'] not in wn:
            block += [f"### − Удалена в мире: {s['name']}", '']
            summary.append((j['name'], s['name'], 'удалена'))
    head = f"## {j['name']}" + ('' if j['name'] == src['name'] else f" (в модуле: «{src['name']}»)")
    if j['name'] != src['name']:
        summary.append((j['name'], '—', f"журнал переименован (в модуле «{src['name']}»)"))
    D += [head, ''] + (block or ['Без изменений по содержанию.', ''])
S = ['## Сводка', '', '| Журнал | Страница | Что |', '| --- | --- | --- |'] + [f'| {a} | {b} | {c} |' for a, b, c in summary] + ['']
D[4:4] = S
(OUT / 'world-vs-module.md').write_text('\n'.join(D), encoding='utf8', newline='\n')

# duplicates check for README
def sig(tid):
    return [(tuple(r['range']), (r.get('name') or '').strip(), (r.get('description') or '').strip()) for r in sorted(results[tid], key=lambda r: r['range'][0])]
dups = collections.defaultdict(list)
for t in sel_tables: dups[t['name']].append(t)
dupinfo = {}
for name, ts in dups.items():
    if len(ts) == 2:
        dupinfo[name] = sig(ts[0]['_id']) == sig(ts[1]['_id'])
pack_same = {}
for t in sel_tables:
    if t['_id'] in ptables:
        pack_same[t['name'] + ' ' + t['_id']] = sig(t['_id']) == [(tuple(r['range']), (r.get('name') or '').strip(), (r.get('description') or '').strip()) for r in sorted(presults[t['_id']], key=lambda r: r['range'][0])]
json.dump({'tables': [(t['name'], t['_id'], origin(t), len(results[t['_id']]), table_files[t['_id']]) for t in sel_tables],
           'journals': [(j['name'], j['_id'], origin(j), c, f) for j, f, c in jindex],
           'duplicates_identical': dupinfo, 'same_as_amygdal_pack': pack_same, 'summary': summary},
          open(sys.argv[4], 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('ok')
