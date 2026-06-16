#!/usr/bin/env python3
"""Generate constraint test suites from a JSON schema file.

Produces:
  valid.json                              — one record satisfying all constraints
  invalid_missing_required_<FIELD>.json  — missing required field
  invalid_bad_enum_<FIELD>.json          — enum field set to invalid value
  invalid_pattern_<FIELD>.json           — pattern field set to non-matching value
  invalid_wrong_type_<FIELD>.json        — string field set to integer
  invalid_conditional_<FIELD>_missing.json — if/then conditional violated

Usage:
    python scripts/generate_constraint_tests.py <schema.json> --output-dir <dir>
"""
from __future__ import annotations

import argparse
import copy
import json
import random
import re
import sys
from pathlib import Path

try:
    import exrex
    HAS_EXREX = True
except ImportError:
    HAS_EXREX = False

try:
    from faker import Faker
    _faker = Faker()
    _faker.seed_instance(42)
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False

# Fixed seed for reproducibility
random.seed(42)

def _valid_value_for_pattern(pattern: str) -> str:
    """Return a string that matches the given pattern.

    Strips lookahead/lookbehind assertions before passing to exrex, since
    exrex cannot generate strings for patterns containing them. The generated
    string is then verified against the original pattern, retrying if needed.
    """
    if HAS_EXREX:
        # Strip lookahead (?=...) / negative lookahead (?!...) and
        # lookbehind (?<=...) / negative lookbehind (?<!...) assertions.
        simplified = re.sub(r"\(\?<?[=!][^)]*\)", "", pattern)
        for _ in range(10):
            try:
                val = exrex.getone(simplified, limit=10)
                if val and re.match(pattern, val):
                    return val
            except Exception:
                break

    # Fallback: try a handful of simple candidates, including a URL for URL patterns
    for candidate in ["https://example.com", "valid_string", "sample", "test", "data", "abc123"]:
        try:
            if re.match(pattern, candidate):
                return candidate
        except re.error:
            pass

    return "valid_string"


def _valid_value_for_field(field_name: str, field_schema: dict) -> object:
    """Return a valid value for a field given its schema definition."""
    field_type = field_schema.get("type", "string")

    # Array type (e.g. HTAN_PARENT_ID, TREATMENT_TYPE)
    if field_type == "array":
        items = field_schema.get("items", {})
        if "enum" in items:
            return [items["enum"][0]]
        item_pattern = items.get("pattern")
        if item_pattern:
            return [_valid_value_for_pattern(item_pattern)]
        item_type = items.get("type", "string")
        if item_type == "integer":
            return [1]
        if item_type == "number":
            return [1.0]
        return [_random_string()]

    # Enum
    if "enum" in field_schema:
        return field_schema["enum"][0]

    # Pattern string
    if "pattern" in field_schema:
        return _valid_value_for_pattern(field_schema["pattern"])

    # Type-based
    if field_type == "integer":
        return 1
    if field_type == "number":
        return 1.0
    if field_type == "boolean":
        return True
    if field_type == "string":
        return _random_string()

    return _random_string()


def _random_string() -> str:
    if HAS_FAKER:
        return _faker.word()
    return "sample"


def _collect_conditional_triggering_values(schema: dict) -> dict[str, set]:
    """Return a map of field_name -> set of const values that trigger conditionals."""
    triggers: dict[str, set] = {}
    for block in schema.get("allOf", []):
        if_clause = block.get("if", {})
        if_props = if_clause.get("properties", {})
        for field, constraint in if_props.items():
            if "const" in constraint:
                triggers.setdefault(field, set()).add(constraint["const"])
    return triggers


def build_valid_record(schema: dict) -> dict:
    """Build a valid record satisfying all schema constraints."""
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    triggering = _collect_conditional_triggering_values(schema)

    record: dict = {}

    # Populate all required fields
    for field in required:
        field_schema = properties.get(field, {})
        value = _valid_value_for_field(field, field_schema)

        # If this field triggers conditionals, pick a non-triggering enum value
        if field in triggering and "enum" in field_schema:
            for enum_val in field_schema["enum"]:
                if enum_val not in triggering[field]:
                    value = enum_val
                    break

        record[field] = value

    # Process allOf if/then blocks: if we happen to have set a triggering value,
    # ensure the then-required fields are present
    for block in schema.get("allOf", []):
        if_clause = block.get("if", {})
        then_clause = block.get("then", {})
        if_props = if_clause.get("properties", {})
        if_required = if_clause.get("required", [])
        then_required = then_clause.get("required", [])
        then_props = then_clause.get("properties", {})

        # Check if the if condition is currently satisfied
        condition_met = True
        for field in if_required:
            if field not in record:
                condition_met = False
                break
            const_val = if_props.get(field, {}).get("const")
            if const_val is not None and record.get(field) != const_val:
                condition_met = False
                break

        if condition_met:
            for then_field in then_required:
                if then_field not in record:
                    then_field_schema = then_props.get(then_field, {})
                    # Try to get the schema from top-level properties if not in then
                    if not then_field_schema:
                        then_field_schema = properties.get(then_field, {})
                    record[then_field] = _valid_value_for_field(then_field, then_field_schema)

    return record


def generate_invalid_files(schema: dict, valid_record: dict) -> list[tuple[str, dict]]:
    """Generate (filename, record) pairs for all constraint violations."""
    properties = schema.get("properties", {})
    required = schema.get("required", [])
    results = []

    # 1. Missing required fields
    for field in required:
        record = copy.deepcopy(valid_record)
        del record[field]
        results.append((f"invalid_missing_required_{field}.json", record))

    # 2. Bad enum values
    for field in required:
        field_schema = properties.get(field, {})
        if "enum" in field_schema:
            record = copy.deepcopy(valid_record)
            record[field] = "INVALID_VALUE"
            results.append((f"invalid_bad_enum_{field}.json", record))

    # 3. Bad pattern values
    for field in required:
        field_schema = properties.get(field, {})
        if "pattern" in field_schema and "enum" not in field_schema:
            record = copy.deepcopy(valid_record)
            record[field] = "DOES NOT MATCH"  # space ensures failure for any alphanumeric/URL/HTAN pattern
            results.append((f"invalid_pattern_{field}.json", record))

    # 4. Wrong type (string field set to integer)
    for field in required:
        field_schema = properties.get(field, {})
        if field_schema.get("type") == "string" and "enum" not in field_schema:
            record = copy.deepcopy(valid_record)
            record[field] = 999
            results.append((f"invalid_wrong_type_{field}.json", record))

    # 5. Conditional violations: satisfy if condition, remove then-required field
    for block in schema.get("allOf", []):
        if_clause = block.get("if", {})
        then_clause = block.get("then", {})
        if_props = if_clause.get("properties", {})
        if_required = if_clause.get("required", [])
        then_required = then_clause.get("required", [])

        if not if_required or not then_required:
            continue

        # Build a record that satisfies the if condition
        for then_field in then_required:
            record = copy.deepcopy(valid_record)

            # Satisfy the if condition for all if_required fields
            for if_field in if_required:
                const_val = if_props.get(if_field, {}).get("const")
                if const_val is not None:
                    record[if_field] = const_val
                elif if_field not in record:
                    field_schema = properties.get(if_field, {})
                    record[if_field] = _valid_value_for_field(if_field, field_schema)

            # Ensure then-required fields are present EXCEPT the one we're violating
            then_props = then_clause.get("properties", {})
            for other_then_field in then_required:
                if other_then_field != then_field and other_then_field not in record:
                    field_schema = then_props.get(other_then_field, {}) or properties.get(other_then_field, {})
                    record[other_then_field] = _valid_value_for_field(other_then_field, field_schema)

            # Remove the then-required field to create the violation
            record.pop(then_field, None)

            results.append((f"invalid_conditional_{then_field}_missing.json", record))

    return results


def run(schema_path: Path, output_dir: Path) -> None:
    """Generate constraint tests for a single schema."""
    with open(schema_path) as f:
        schema = json.load(f)

    output_dir.mkdir(parents=True, exist_ok=True)

    # Build and write valid record
    valid_record = build_valid_record(schema)
    valid_path = output_dir / "valid.json"
    with open(valid_path, "w") as f:
        json.dump(valid_record, f, indent=2)
    print(f"  wrote {valid_path}")

    # Generate and write invalid records
    invalid_files = generate_invalid_files(schema, valid_record)
    for filename, record in invalid_files:
        out_path = output_dir / filename
        with open(out_path, "w") as f:
            json.dump(record, f, indent=2)
        print(f"  wrote {out_path}")

    print(f"Generated {1 + len(invalid_files)} files in {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schema", type=Path, help="Path to JSON schema file")
    parser.add_argument("--output-dir", type=Path, required=True, help="Output directory")
    args = parser.parse_args()

    if not args.schema.exists():
        print(f"Error: schema file not found: {args.schema}", file=sys.stderr)
        sys.exit(1)

    run(args.schema, args.output_dir)


if __name__ == "__main__":
    main()
