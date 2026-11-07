set -euo pipefail
M=/home/foundry/foundrydata/Data/modules
T=$(mktemp -d /tmp/nri_ro_packs_XXXXXX)
cp -a "$M/nri-coc-library/packs/library-journals" "$T/lj"; rm -f "$T/lj/LOCK"
cp -a "$M/nri-coc-library/packs/library-rolltables" "$T/lr"; rm -f "$T/lr/LOCK"
cp -a "$M/coc-Amygdal-chest/packs/tablicy-hranitelya" "$T/am"; rm -f "$T/am/LOCK"
V=$(python3 -c "import json;print(json.load(open('$M/nri-coc-library/module.json'))['version'])")
cd "$T"
node - "$T" "$V" > "$T/dump.json" <<'NODE'
(async () => {
const { ClassicLevel } = require('/opt/foundry/resources/app/node_modules/classic-level');
const root = process.argv[2];
const out = { nriLibraryVersion: process.argv[3], dumpedAt: new Date().toISOString(), packs: {} };
for (const c of ['lj', 'lr', 'am']) {
  const db = new ClassicLevel(root + '/' + c, { valueEncoding: 'utf8', keyEncoding: 'utf8' });
  try { await db.open(); } catch (e) { out.packs[c] = String(e); continue; }
  const entries = [];
  for await (const [k, v] of db.iterator()) { let val; try { val = JSON.parse(v); } catch { val = v; } entries.push([k, val]); }
  await db.close();
  out.packs[c] = entries;
}
process.stdout.write(JSON.stringify(out));
})().catch(e => { console.error(e); process.exit(1); });
NODE
gzip -c "$T/dump.json" | base64 -w0
rm -rf "$T"
