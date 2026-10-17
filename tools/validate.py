"""Minimal JSON Schema validator for the subset used in schemas/ (stdlib only).

Supports: type (incl. lists), required, properties, additionalProperties: false,
items, enum, const, minItems, pattern, and $ref to "#/$defs/..." or
"<file>.json#/$defs/..." relative to the schema directory. Temporary until a
locked jsonschema dependency is added (decision T2).

Usage: python tools/validate.py <schema.json> <instance.json> [...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

TYPES = {"object": dict, "array": list, "string": str, "boolean": bool, "null": type(None)}


def type_ok(value, name: str) -> bool:
    if name == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if name == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    return isinstance(value, TYPES[name])


class Validator:
    def __init__(self, schema_path: Path):
        self.dir = schema_path.parent
        self.cache: dict[str, dict] = {}
        self.root_name = schema_path.name

    def load(self, name: str) -> dict:
        if name not in self.cache:
            self.cache[name] = json.loads((self.dir / name).read_text(encoding="utf-8"))
        return self.cache[name]

    def resolve(self, ref: str, current: str) -> tuple[dict, str]:
        file, _, pointer = ref.partition("#")
        doc_name = file or current
        node = self.load(doc_name)
        for part in [p for p in pointer.split("/") if p]:
            node = node[part]
        return node, doc_name

    def check(self, schema: dict, value, path: str, doc: str, errors: list[str]) -> None:
        if "$ref" in schema:
            target, target_doc = self.resolve(schema["$ref"], doc)
            self.check(target, value, path, target_doc, errors)
            return
        if "const" in schema and value != schema["const"]:
            errors.append(f"{path}: expected const {schema['const']!r}, got {value!r}")
        if "enum" in schema and value not in schema["enum"]:
            errors.append(f"{path}: {value!r} not in {schema['enum']}")
        if "type" in schema:
            names = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
            if not any(type_ok(value, n) for n in names):
                errors.append(f"{path}: type {type(value).__name__} not in {names}")
                return
        if isinstance(value, str) and "pattern" in schema and not re.search(schema["pattern"], value):
            errors.append(f"{path}: {value!r} does not match {schema['pattern']}")
        if isinstance(value, dict):
            for key in schema.get("required", []):
                if key not in value:
                    errors.append(f"{path}: missing required '{key}'")
            props = schema.get("properties", {})
            for key, sub in value.items():
                if key in props:
                    self.check(props[key], sub, f"{path}.{key}", doc, errors)
                elif schema.get("additionalProperties") is False:
                    errors.append(f"{path}: unexpected property '{key}'")
        if isinstance(value, list):
            if len(value) < schema.get("minItems", 0):
                errors.append(f"{path}: fewer than {schema['minItems']} items")
            if "items" in schema:
                for i, item in enumerate(value):
                    self.check(schema["items"], item, f"{path}[{i}]", doc, errors)

    def validate(self, instance) -> list[str]:
        errors: list[str] = []
        self.check(self.load(self.root_name), instance, "$", self.root_name, errors)
        return errors


def main() -> int:
    schema = Path(sys.argv[1])
    v = Validator(schema)
    bad = 0
    for p in sys.argv[2:]:
        errs = v.validate(json.loads(Path(p).read_text(encoding="utf-8")))
        print(f"{'OK ' if not errs else 'FAIL'} {p}")
        for e in errs:
            print("   ", e)
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
