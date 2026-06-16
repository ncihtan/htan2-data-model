#!/usr/bin/env python3
"""Validate synthetic constraint test data against JSON schemas.

For each schema found in --schema-dir, locates the matching constraint_tests
subdirectory under --data-dir, then:
  - Asserts valid.json passes jsonschema.validate()
  - Asserts every invalid_*.json raises jsonschema.ValidationError

Exits non-zero with a summary of failures.

Usage:
    python scripts/validate_synthetic_data.py \\
        --schema-dir JSON_Schemas/v1.3.0 \\
        --data-dir synthetic_data/v1.3.0/constraint_tests
"""

import argparse
import json
import sys
from pathlib import Path

import jsonschema


def _schema_name_from_path(schema_path: Path) -> str:
    """Extract schema name from filename like HTAN.Demographics-v1.3.0-schema.json."""
    stem = schema_path.stem  # e.g. HTAN.Demographics-v1.3.0-schema
    # Remove HTAN. prefix and -vX.Y.Z-schema suffix
    name = stem
    if name.startswith("HTAN."):
        name = name[5:]
    # Remove version suffix: -v1.3.0-schema
    import re
    name = re.sub(r"-v[\d.]+(-schema)?$", "", name)
    name = re.sub(r"-schema$", "", name)
    return name


def validate_schema_dir(schema_path: Path, data_dir: Path) -> list[str]:
    """Validate one schema's constraint tests. Returns list of failure messages."""
    failures = []

    schema_name = _schema_name_from_path(schema_path)
    test_dir = data_dir / schema_name

    if not test_dir.exists():
        failures.append(f"[{schema_name}] No constraint test directory found at {test_dir}")
        return failures

    with open(schema_path) as f:
        schema = json.load(f)

    # Validate valid.json — should PASS
    valid_path = test_dir / "valid.json"
    if not valid_path.exists():
        failures.append(f"[{schema_name}] valid.json not found")
    else:
        with open(valid_path) as f:
            valid_data = json.load(f)
        try:
            jsonschema.validate(instance=valid_data, schema=schema)
            print(f"  [PASS] {schema_name}/valid.json")
        except jsonschema.ValidationError as e:
            failures.append(f"[{schema_name}] valid.json FAILED validation: {e.message}")
        except jsonschema.SchemaError as e:
            failures.append(f"[{schema_name}] Schema error: {e.message}")

    # Validate invalid_*.json — each should FAIL
    invalid_files = sorted(test_dir.glob("invalid_*.json"))
    if not invalid_files:
        failures.append(f"[{schema_name}] No invalid_*.json files found")
    else:
        for invalid_path in invalid_files:
            with open(invalid_path) as f:
                invalid_data = json.load(f)
            try:
                jsonschema.validate(instance=invalid_data, schema=schema)
                failures.append(
                    f"[{schema_name}] {invalid_path.name} PASSED validation (expected failure)"
                )
            except jsonschema.ValidationError:
                print(f"  [PASS] {schema_name}/{invalid_path.name} (correctly rejected)")
            except jsonschema.SchemaError as e:
                failures.append(f"[{schema_name}] Schema error on {invalid_path.name}: {e.message}")

    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema-dir", type=Path, required=True, help="Directory with JSON schemas")
    parser.add_argument("--data-dir", type=Path, required=True, help="Directory with constraint_tests subdirs")
    args = parser.parse_args()

    if not args.schema_dir.exists():
        print(f"Error: schema directory not found: {args.schema_dir}", file=sys.stderr)
        sys.exit(1)
    if not args.data_dir.exists():
        print(f"Error: data directory not found: {args.data_dir}", file=sys.stderr)
        sys.exit(1)

    schema_files = sorted(args.schema_dir.glob("*.json"))
    if not schema_files:
        print(f"No JSON schemas found in {args.schema_dir}", file=sys.stderr)
        sys.exit(1)

    all_failures: list[str] = []

    for schema_path in schema_files:
        schema_name = _schema_name_from_path(schema_path)
        print(f"\nValidating {schema_name}...")
        failures = validate_schema_dir(schema_path, args.data_dir)
        all_failures.extend(failures)

    print(f"\n{'=' * 60}")
    if all_failures:
        print(f"FAILED: {len(all_failures)} issue(s) found:")
        for msg in all_failures:
            print(f"  {msg}")
        sys.exit(1)
    else:
        print(f"All constraint tests passed for {len(schema_files)} schema(s).")


if __name__ == "__main__":
    main()
