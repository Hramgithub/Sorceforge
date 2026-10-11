import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import YAML from "yaml";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const projectRoot = path.resolve(__dirname, "../..");
const repoRoot = path.resolve(projectRoot, "..");

const args = process.argv.slice(2);
const quiet = args.includes("--quiet");
const fileArgIndex = args.findIndex((arg) => arg === "--file");
const requestedFile =
  fileArgIndex >= 0 && args[fileArgIndex + 1]
    ? args[fileArgIndex + 1]
    : "docs/roadmap/roadmap.yaml";

const roadmapPath = resolveSourcefoldPath(requestedFile);
const errors = [];

function resolveSourcefoldPath(value) {
  if (!value) return null;
  if (path.isAbsolute(value)) return value;
  if (value.startsWith("Sourcefold/") || value.startsWith("Sourcefold\\")) {
    return path.resolve(repoRoot, value);
  }
  return path.resolve(projectRoot, value);
}

function requireArray(root, key) {
  if (!Array.isArray(root[key])) {
    errors.push(`Top-level key '${key}' must be an array.`);
    return [];
  }
  return root[key];
}

function requireObjectArray(root, key) {
  return requireArray(root, key).filter((item, index) => {
    if (!item || typeof item !== "object" || Array.isArray(item)) {
      errors.push(`${key}[${index}] must be an object.`);
      return false;
    }
    return true;
  });
}

function requirePath(label, value) {
  const resolved = resolveSourcefoldPath(value);
  if (!resolved || !fs.existsSync(resolved)) {
    errors.push(`${label} path is missing: ${value}`);
  }
}

function uniqueById(label, items) {
  const ids = new Map();
  for (const [index, item] of items.entries()) {
    if (!item.id) {
      errors.push(`${label}[${index}] is missing id.`);
      continue;
    }
    if (ids.has(item.id)) {
      errors.push(
        `Duplicate ${label} id '${item.id}' at indexes ${ids.get(item.id)} and ${index}.`,
      );
      continue;
    }
    ids.set(item.id, index);
  }
  return ids;
}

function requireFields(label, item, fields) {
  for (const field of fields) {
    if (item[field] === undefined || item[field] === null || item[field] === "") {
      errors.push(`${label} '${item.id ?? "(missing id)"}' is missing ${field}.`);
    }
  }
}

if (!fs.existsSync(roadmapPath)) {
  console.error(`Roadmap file not found: ${roadmapPath}`);
  process.exit(1);
}

const source = fs.readFileSync(roadmapPath, "utf8");
const doc = YAML.parseDocument(source, {
  prettyErrors: true,
  strict: true,
  uniqueKeys: true,
});

for (const parseError of doc.errors) {
  errors.push(`YAML parse error: ${parseError.message}`);
}

const data = doc.toJS();
if (!data || typeof data !== "object" || Array.isArray(data)) {
  errors.push("Roadmap root must be a mapping/object.");
}

const root = data && typeof data === "object" && !Array.isArray(data) ? data : {};
const requiredTopLevel = [
  "schema_version",
  "roadmap_id",
  "title",
  "updated_at",
  "source_policy",
  "status_values",
  "lanes",
  "nodes",
  "edges",
];

for (const key of requiredTopLevel) {
  if (!(key in root)) errors.push(`Missing top-level key: ${key}`);
}

const statuses = requireArray(root, "status_values");
const statusSet = new Set(statuses);
const lanes = requireObjectArray(root, "lanes");
const nodes = requireObjectArray(root, "nodes");
const edges = requireObjectArray(root, "edges");
const checkpoints = Array.isArray(root.documentation_checkpoints)
  ? requireObjectArray(root, "documentation_checkpoints")
  : [];

const laneIds = uniqueById("lane", lanes);
const nodeIds = uniqueById("node", nodes);
uniqueById("edge", edges);
uniqueById("documentation checkpoint", checkpoints);

if (root.source_policy && typeof root.source_policy === "object") {
  requirePath("source_policy.canonical", root.source_policy.canonical);
  requirePath("source_policy.viewer", root.source_policy.viewer);
  const refs = Array.isArray(root.source_policy.reference_documents)
    ? root.source_policy.reference_documents
    : [];
  for (const [index, ref] of refs.entries()) {
    requirePath(`source_policy.reference_documents[${index}]`, ref?.path);
  }
}

for (const node of nodes) {
  requireFields("node", node, ["title", "lane", "status", "linked_plan"]);
  if (node.lane && !laneIds.has(node.lane)) {
    errors.push(`Node '${node.id}' uses unknown lane '${node.lane}'.`);
  }
  if (node.status && !statusSet.has(node.status)) {
    errors.push(`Node '${node.id}' uses unknown status '${node.status}'.`);
  }
  if (node.linked_plan) {
    requirePath(`node '${node.id}' linked_plan`, node.linked_plan);
  }
}

for (const edge of edges) {
  requireFields("edge", edge, ["from", "to", "type", "status", "reason"]);
  if (edge.from && !nodeIds.has(edge.from)) {
    errors.push(`Edge '${edge.id}' references unknown from node '${edge.from}'.`);
  }
  if (edge.to && !nodeIds.has(edge.to)) {
    errors.push(`Edge '${edge.id}' references unknown to node '${edge.to}'.`);
  }
  if (edge.status && !statusSet.has(edge.status)) {
    errors.push(`Edge '${edge.id}' uses unknown status '${edge.status}'.`);
  }
}

for (const checkpoint of checkpoints) {
  requireFields("documentation checkpoint", checkpoint, [
    "created_at",
    "type",
    "goal",
    "summary",
  ]);
  if (checkpoint.goal) {
    requirePath(
      `documentation checkpoint '${checkpoint.id}' goal`,
      `docs/plans/${checkpoint.goal}/plan.md`,
    );
  }
}

if (!quiet) {
  console.log("Sourcefold roadmap validation");
  console.log(`Roadmap: ${roadmapPath}`);
  console.log(`Statuses: ${statuses.length}`);
  console.log(`Lanes: ${lanes.length}`);
  console.log(`Nodes: ${nodes.length}`);
  console.log(`Edges: ${edges.length}`);
  console.log(`Documentation checkpoints: ${checkpoints.length}`);
}

if (errors.length > 0) {
  if (!quiet) {
    console.log("");
    console.log("Errors:");
    for (const error of errors) console.log(`- ${error}`);
  }
  process.exit(1);
}

if (!quiet) {
  console.log("");
  console.log("Roadmap validation passed.");
}
