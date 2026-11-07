set -euo pipefail
W=/home/foundry/foundrydata/Data/worlds/zov-glubin-ktulhu/data
T=$(mktemp -d /tmp/nri_ro_dump_XXXXXX)
for c in tables journal folders settings; do cp -a "$W/$c" "$T/$c"; rm -f "$T/$c/LOCK"; done
cd "$T"
node - "$T" > "$T/dump.json" <<'NODE'
(async () => {
const { ClassicLevel } = require('/opt/foundry/resources/app/node_modules/classic-level');
const root = process.argv[2];
const out = { world: 'zov-glubin-ktulhu', dumpedAt: new Date().toISOString(), collections: {} };
for (const c of ['tables', 'journal', 'folders', 'settings']) {
  const db = new ClassicLevel(root + '/' + c, { valueEncoding: 'utf8', keyEncoding: 'utf8' });
  await db.open();
  const entries = [];
  for await (const [k, v] of db.iterator()) {
    let val; try { val = JSON.parse(v); } catch { val = v; }
    entries.push([k, val]);
  }
  await db.close();
  out.collections[c] = entries;
}
process.stdout.write(JSON.stringify(out));
})().catch(e => { console.error(e); process.exit(1); });
NODE
gzip -c "$T/dump.json" | base64 -w0
rm -rf "$T"
