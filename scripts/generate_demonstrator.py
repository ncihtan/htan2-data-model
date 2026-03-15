#!/usr/bin/env python3
"""Generate a semantically coherent synthetic demonstrator dataset using Claude.

Produces a connected dataset across all HTAN schemas: clinical records,
biospecimens, and assay files — all with consistent, joinable IDs.

Usage:
    python scripts/generate_demonstrator.py \\
        --schema-dir JSON_Schemas/v1.3.0 \\
        --output-dir synthetic_data/v1.3.0/demonstrator \\
        --participants 5 --biospecimens-per-participant 3
"""

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import anthropic
import jsonschema

CENTER = "HTA201"

CLINICAL_SCHEMA_NAMES = {
    "Demographics", "Diagnosis", "Therapy", "FollowUp",
    "MolecularTest", "Exposure", "FamilyHistory", "VitalStatus",
}
BIOSPECIMEN_SCHEMA_NAME = "BiospecimenData"


def participant_id(n: int) -> str:
    return f"{CENTER}_{n}"


def biospecimen_id(p: int, b: int) -> str:
    return f"{CENTER}_{p}_B{b}"


def data_file_id(p: int, d: int) -> str:
    return f"{CENTER}_{p}_D{d}"


def generate_ids(num_participants: int, biospecimens_per_participant: int) -> dict:
    participant_ids = [participant_id(i) for i in range(1, num_participants + 1)]
    biospecimen_ids = []
    biospecimen_to_participant = {}
    for p in range(1, num_participants + 1):
        for b in range(1, biospecimens_per_participant + 1):
            bid = biospecimen_id(p, b)
            biospecimen_ids.append(bid)
            biospecimen_to_participant[bid] = participant_id(p)
    return {
        "participant_ids": participant_ids,
        "biospecimen_ids": biospecimen_ids,
        "biospecimen_to_participant": biospecimen_to_participant,
    }


def _schema_name(schema_path: Path) -> str:
    """Extract schema name from e.g. HTAN.Demographics-v1.3.0-schema.json."""
    stem = schema_path.stem
    name = stem
    if name.startswith("HTAN."):
        name = name[5:]
    name = re.sub(r"-v[\d.]+(-schema)?$", "", name)
    name = re.sub(r"-schema$", "", name)
    return name


def load_schema(schema_dir: Path, name: str) -> dict | None:
    for schema_path in schema_dir.glob("*.json"):
        if _schema_name(schema_path) == name:
            with open(schema_path) as f:
                return json.load(f)
    return None


def discover_assay_schemas(schema_dir: Path) -> dict[str, dict]:
    """Return all schemas that are not clinical or biospecimen."""
    skip = CLINICAL_SCHEMA_NAMES | {BIOSPECIMEN_SCHEMA_NAME}
    assay_schemas = {}
    for schema_path in sorted(schema_dir.glob("*.json")):
        name = _schema_name(schema_path)
        if name not in skip:
            with open(schema_path) as f:
                assay_schemas[name] = json.load(f)
    return assay_schemas


def make_client() -> anthropic.Anthropic:
    return anthropic.Anthropic()


def call_claude(
    client: anthropic.Anthropic,
    prompt: str,
    max_tokens: int = 8096,
    model: str = "claude-haiku-4-5",
) -> str:
    with client.messages.stream(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    ) as stream:
        return stream.get_final_message().content[0].text


def extract_json(text: str) -> object:
    fence_match = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
    if fence_match:
        return json.loads(fence_match.group(1))
    return json.loads(text.strip())


def validate_records(records: list[dict], schema: dict) -> list[str]:
    errors = []
    for i, record in enumerate(records):
        try:
            jsonschema.validate(instance=record, schema=schema)
        except jsonschema.ValidationError as e:
            errors.append(f"Record {i}: {e.message}")
    return errors


def generate_and_validate(
    client: anthropic.Anthropic,
    prompt: str,
    schema: dict,
    max_retries: int = 2,
) -> list[dict]:
    """Generate records with Claude, validate against schema, retry once if invalid."""
    for attempt in range(max_retries):
        text = call_claude(client, prompt)
        try:
            data = extract_json(text)
        except (json.JSONDecodeError, ValueError) as e:
            if attempt < max_retries - 1:
                prompt += f"\n\nPrevious attempt failed JSON parsing: {e}. Return ONLY valid JSON."
                continue
            raise RuntimeError(f"Failed to parse JSON from Claude response: {e}") from e

        if not isinstance(data, list):
            data = [data]

        errors = validate_records(data, schema)
        if not errors:
            return data

        if attempt < max_retries - 1:
            error_summary = "\n".join(errors[:5])
            prompt += (
                f"\n\nPrevious attempt failed schema validation:\n{error_summary}\n"
                "Please fix these issues and return corrected JSON."
            )
        else:
            print(f"  WARNING: {len(errors)} validation error(s) in generated records (proceeding anyway)")
            print(f"    First error: {errors[0]}")
            return data

    return []


_LARGE_ENUM_THRESHOLD = 20


def _summarise_schema(schema: dict) -> dict:
    """Return a condensed schema with only required fields and their constraints.

    For enum fields with more than _LARGE_ENUM_THRESHOLD values (e.g. ICD code lists),
    the enum is omitted and only the description is kept — Claude can generate
    plausible values from context without needing thousands of codes in the prompt.
    """
    required = schema.get("required", [])
    properties = schema.get("properties", {})
    summary = {"required": required, "properties": {}}
    for field in required:
        prop = properties.get(field, {})
        entry: dict = {}
        if "description" in prop:
            entry["description"] = prop["description"]
        if "type" in prop:
            entry["type"] = prop["type"]
        enum = prop.get("enum")
        if enum is not None:
            if len(enum) <= _LARGE_ENUM_THRESHOLD:
                entry["enum"] = enum
        elif "items" in prop:
            items_enum = prop["items"].get("enum")
            entry["type"] = "array"
            if items_enum is not None and len(items_enum) <= _LARGE_ENUM_THRESHOLD:
                entry["items"] = {"enum": items_enum}
        if "pattern" in prop:
            entry["pattern"] = prop["pattern"]
        summary["properties"][field] = entry
    # Include conditionals so Claude knows which fields are sometimes required
    if "allOf" in schema:
        summary["allOf"] = schema["allOf"]
    if "if" in schema and "then" in schema:
        summary["if"] = schema["if"]
        summary["then"] = schema["then"]
    return summary


def generate_clinical_records(
    client: anthropic.Anthropic,
    schema_dir: Path,
    participant_ids: list[str],
) -> dict[str, list[dict]]:
    schemas = {
        name: load_schema(schema_dir, name)
        for name in CLINICAL_SCHEMA_NAMES
        if load_schema(schema_dir, name)
    }
    schema_summaries = {name: _summarise_schema(s) for name, s in schemas.items()}

    prompt = f"""Generate synthetic cancer patient data for {len(participant_ids)} participants.

Participant IDs (use exactly these): {json.dumps(participant_ids)}

For each participant, create one record per clinical schema below. Make the data medically
coherent: diagnosis should match therapies and outcomes, exposure history should be plausible
for the cancer type, etc.

Schema summaries (required fields only, with valid enum values):
{json.dumps(schema_summaries, indent=2)}

Return a JSON object with keys matching schema names (Demographics, Diagnosis, Therapy,
FollowUp, MolecularTest, Exposure, FamilyHistory, VitalStatus). Each key maps to an array
of records — one per participant.

Every required field must be present. All enum values must come from the schema's enum list.
All pattern fields must match their regex. Use the provided participant IDs exactly.

Return ONLY the JSON object, no prose."""

    text = call_claude(client, prompt, max_tokens=16000, model="claude-sonnet-4-6")
    try:
        data = extract_json(text)
    except (json.JSONDecodeError, ValueError) as e:
        raise RuntimeError(f"Failed to parse clinical records JSON: {e}") from e

    result = {}
    for schema_name, schema in schemas.items():
        records = data.get(schema_name, [])
        if records:
            errors = validate_records(records, schema)
            if errors:
                print(f"  WARNING: {schema_name} has {len(errors)} validation error(s)")
                print(f"    First: {errors[0]}")
        result[schema_name] = records
    return result


def generate_biospecimen_records(
    client: anthropic.Anthropic,
    schema_dir: Path,
    biospecimen_ids: list[str],
    biospecimen_to_participant: dict[str, str],
    diagnoses: list[dict],
) -> list[dict]:
    schema = load_schema(schema_dir, BIOSPECIMEN_SCHEMA_NAME)
    if schema is None:
        print(f"  WARNING: {BIOSPECIMEN_SCHEMA_NAME} schema not found")
        return []

    diagnosis_summary = {
        r.get("HTAN_PARTICIPANT_ID"): r.get("PRIMARY_DIAGNOSIS", "Unknown cancer")
        for r in diagnoses
    }

    schema_summary = _summarise_schema(schema)

    prompt = f"""Generate synthetic biospecimen records for HTAN data.

Biospecimen IDs (use exactly these as HTAN_BIOSPECIMEN_ID): {json.dumps(biospecimen_ids)}

Parent participant mapping (use participant ID as the single element of HTAN_PARENT_ID array):
{json.dumps(biospecimen_to_participant, indent=2)}

Participant diagnoses (for biological plausibility):
{json.dumps(diagnosis_summary, indent=2)}

Schema (required fields, valid enums, and patterns):
{json.dumps(schema_summary, indent=2)}

Create one record per biospecimen. Required:
- HTAN_BIOSPECIMEN_ID: use the provided biospecimen IDs exactly
- HTAN_PARENT_ID: array with one element — the participant ID for that biospecimen
- All required fields present with valid enum values

Return a JSON array of records. Return ONLY the JSON array, no prose."""

    return generate_and_validate(client, prompt, schema)


def _extract_level(name: str) -> int:
    """Return the first level number in a schema name, or 0 if none found."""
    m = re.search(r"[Ll]evel(\d+)", name)
    return int(m.group(1)) if m else 0


def _assay_group(name: str) -> str:
    """Strip the Level… suffix to get the assay family name (e.g. 'BulkWES')."""
    return re.sub(r"[Ll]evel\w*$", "", name)


def _id_preassignments(
    parent_ids: list[str],
    file_counter: list[int],
    count: int,
) -> list[dict]:
    """Assign deterministic HTAN_DATA_FILE_ID and HTAN_PARENT_ID.

    parent_ids can be biospecimen IDs (for Level 1) or the data file IDs from
    the previous level (for Level 2+). Claude fills everything else.
    """
    assignments = []
    for pid in parent_ids[:count]:
        # Derive participant number from either HTA201_1_B1 or HTA201_1_D1
        parts = pid.split("_")
        p_num = parts[1] if len(parts) > 1 else "1"
        fid = f"{CENTER}_{p_num}_D{file_counter[0]}"
        file_counter[0] += 1
        assignments.append({
            "HTAN_DATA_FILE_ID": fid,
            "HTAN_PARENT_ID": [pid],
        })
    return assignments


def _generate_one_assay_level(
    client: anthropic.Anthropic,
    schema_name: str,
    schema: dict,
    id_assignments: list[dict],
) -> list[dict]:
    count = len(id_assignments)
    schema_summary = _summarise_schema(schema)

    prompt = f"""Generate {count} synthetic {schema_name} records for HTAN data.

Pre-assigned ID fields (use exactly as provided):
{json.dumps(id_assignments, indent=2)}

Schema (required fields, valid enums, and patterns):
{json.dumps(schema_summary, indent=2)}

Fill in all remaining required fields with biologically plausible values. FILENAME and
FILE_FORMAT must match the patterns in the schema.

Return a JSON array of {count} records. Return ONLY the JSON array, no prose."""

    return generate_and_validate(client, prompt, schema)


def generate_assay_records(
    client: anthropic.Anthropic,
    schema_dir: Path,
    biospecimen_ids: list[str],
    file_counter: list[int],
) -> dict[str, list[dict]]:
    assay_schemas = discover_assay_schemas(schema_dir)

    # Group schemas by assay family and sort each group by level so that
    # Level 2 can reference Level 1 file IDs as parents, Level 3 → Level 2, etc.
    groups: dict[str, list[str]] = {}
    for name in assay_schemas:
        groups.setdefault(_assay_group(name), []).append(name)
    for names in groups.values():
        names.sort(key=_extract_level)

    result = {}
    count = min(2, len(biospecimen_ids))

    for group_names in groups.values():
        # Level 1 (or the first level present) parents are biospecimen IDs.
        # Subsequent levels parent off the previous level's data file IDs.
        previous_file_ids = biospecimen_ids[:count]

        for schema_name in group_names:
            schema = assay_schemas[schema_name]
            print(f"  Generating {schema_name} (parents: {previous_file_ids})...")
            id_assignments = _id_preassignments(previous_file_ids, file_counter, count)

            try:
                records = _generate_one_assay_level(client, schema_name, schema, id_assignments)
                result[schema_name] = records
                # The file IDs just generated become parents for the next level
                previous_file_ids = [r["HTAN_DATA_FILE_ID"] for r in records if "HTAN_DATA_FILE_ID" in r]
            except Exception as e:
                print(f"  ERROR generating {schema_name}: {e}")
                result[schema_name] = []
                # Fall back to keeping the same parent IDs so the chain doesn't break
                previous_file_ids = [a["HTAN_DATA_FILE_ID"] for a in id_assignments]

    return result


def _field_hint(field: str, schema: dict) -> dict:
    """Return the full property definition for a specific field, for use in fix prompts."""
    return schema.get("properties", {}).get(field, {})


def _closest_enum(value: str, enum: list[str]) -> str:
    """Return the enum value most similar to the given value."""
    best, best_score = enum[0], 0.0
    value_lower = value.lower()
    for candidate in enum:
        score = SequenceMatcher(None, value_lower, candidate.lower()).ratio()
        if score > best_score:
            best, best_score = candidate, score
    return best


def _postprocess_record(record: dict, schema: dict) -> dict:
    """Deterministic fixes for common LLM errors: enum snapping, type coercion,
    missing conditional fields."""
    properties = schema.get("properties", {})

    # Fix field-level type and enum issues
    for field, value in list(record.items()):
        prop = properties.get(field, {})
        field_type = prop.get("type")

        # String field given as non-string → coerce
        if field_type == "string" and not isinstance(value, str):
            record[field] = str(value)
            value = record[field]

        # Array field given as scalar → wrap
        if field_type == "array" and not isinstance(value, list):
            record[field] = [value]
            value = record[field]

        # Enum snapping for string fields
        enum = prop.get("enum")
        if enum and isinstance(value, str) and value not in enum:
            record[field] = _closest_enum(value, enum)

        # Enum snapping for array-of-enum fields
        items = prop.get("items", {})
        items_enum = items.get("enum")
        if items_enum and isinstance(value, list):
            record[field] = [
                _closest_enum(v, items_enum) if isinstance(v, str) and v not in items_enum else v
                for v in value
            ]

    # Fill missing conditional required fields (allOf if/then + top-level if/then)
    conditional_blocks = list(schema.get("allOf", []))
    if "if" in schema and "then" in schema:
        conditional_blocks.append({"if": schema["if"], "then": schema["then"]})
    for block in conditional_blocks:
        if_clause = block.get("if", {})
        then_clause = block.get("then", {})
        if_props = if_clause.get("properties", {})
        if_required = if_clause.get("required", [])
        then_required = then_clause.get("required", [])

        # Check if the if-condition is satisfied
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
                    then_prop = then_clause.get("properties", {}).get(then_field, {})
                    if not then_prop:
                        then_prop = properties.get(then_field, {})
                    # Fill with first enum value or a placeholder
                    if "enum" in then_prop:
                        record[then_field] = then_prop["enum"][0]
                    elif then_prop.get("type") == "integer":
                        record[then_field] = 1
                    elif then_prop.get("type") == "number":
                        record[then_field] = 1.0
                    elif then_prop.get("type") == "array":
                        record[then_field] = []
                    else:
                        record[then_field] = "Not specified"

    return record


def _postprocess_records(records: list[dict], schema: dict) -> list[dict]:
    """Apply deterministic post-processing to all records."""
    return [_postprocess_record(r, schema) for r in records]


def _llm_fix_records(
    client: anthropic.Anthropic,
    records: list[dict],
    schema: dict,
    schema_name: str,
) -> list[dict]:
    """Single LLM fix pass for errors the deterministic post-processor can't handle."""
    errors_by_index: dict[int, list[str]] = {}
    for i, record in enumerate(records):
        try:
            jsonschema.validate(instance=record, schema=schema)
        except jsonschema.ValidationError as e:
            errors_by_index.setdefault(i, []).append(e.message)

    if not errors_by_index:
        return records

    failing = {i: records[i] for i in errors_by_index}
    failing_fields: set[str] = set()
    for msgs in errors_by_index.values():
        for msg in msgs:
            for m in re.finditer(r"'([A-Z][A-Z0-9_]+)'", msg):
                failing_fields.add(m.group(1))

    field_schemas = {f: _field_hint(f, schema) for f in failing_fields if _field_hint(f, schema)}

    prompt = f"""Fix the following {schema_name} records so they pass JSON schema validation.

Records with errors (keyed by index):
{json.dumps(failing, indent=2)}

Validation errors per record:
{json.dumps(errors_by_index, indent=2)}

Full schema definitions for the affected fields:
{json.dumps(field_schemas, indent=2)}

Return ONLY a JSON object mapping the same integer keys to corrected records.
Do not change any field not mentioned in the errors. Enum values must be copied
EXACTLY from the schema — do not paraphrase or expand them.
For array-type fields, always return a JSON array even if there is only one value."""

    text = call_claude(client, prompt)
    try:
        fixes = extract_json(text)
    except (json.JSONDecodeError, ValueError):
        print(f"  WARNING: could not parse fix response for {schema_name}, keeping originals")
        return records

    fixed = list(records)
    for idx_str, corrected in fixes.items():
        idx = int(idx_str)
        if 0 <= idx < len(fixed):
            fixed[idx] = corrected
    return fixed


def _write_and_fix(
    client: anthropic.Anthropic,
    records: list[dict],
    schema: dict,
    schema_name: str,
    out_path: Path,
) -> None:
    """Post-process deterministically, then one LLM fix pass if needed, then write."""
    # Step 1: deterministic fixes (enum snap, type coercion, conditional fields)
    fixed = _postprocess_records(records, schema)

    pre_errors = validate_records(fixed, schema)
    if pre_errors:
        # Step 2: single LLM pass for remaining issues
        print(f"  {schema_name}: {len(pre_errors)} error(s) after post-process, running LLM fix...")
        fixed = _llm_fix_records(client, fixed, schema, schema_name)
        # Re-apply post-processing to LLM output (it may introduce new type issues)
        fixed = _postprocess_records(fixed, schema)

    remaining = validate_records(fixed, schema)
    if remaining:
        print(f"  WARNING: {schema_name} still has {len(remaining)} error(s)")
        print(f"    {remaining[0]}")

    with open(out_path, "w") as f:
        json.dump(fixed, f, indent=2)
    print(f"  wrote {out_path}")


def run(
    schema_dir: Path,
    output_dir: Path,
    num_participants: int,
    biospecimens_per_participant: int,
) -> None:
    client = make_client()

    print("Generating IDs...")
    ids = generate_ids(num_participants, biospecimens_per_participant)
    participant_ids = ids["participant_ids"]
    biospecimen_ids = ids["biospecimen_ids"]
    biospecimen_to_participant = ids["biospecimen_to_participant"]
    file_counter = [1]

    print(f"\nGenerating clinical records for {num_participants} participants...")
    clinical = generate_clinical_records(client, schema_dir, participant_ids)

    diagnoses = clinical.get("Diagnosis", [])

    print(f"\nGenerating biospecimen records for {len(biospecimen_ids)} biospecimens...")
    biospecimens = generate_biospecimen_records(
        client, schema_dir, biospecimen_ids, biospecimen_to_participant, diagnoses
    )

    print("\nGenerating assay records...")
    assays = generate_assay_records(client, schema_dir, biospecimen_ids, file_counter)

    print("\nValidating and fixing output...")
    clinical_dir = output_dir / "clinical"
    clinical_dir.mkdir(parents=True, exist_ok=True)
    for schema_name, records in clinical.items():
        schema = load_schema(schema_dir, schema_name)
        out_path = clinical_dir / f"{schema_name.lower()}s.json"
        _write_and_fix(client, records, schema, schema_name, out_path)

    output_dir.mkdir(parents=True, exist_ok=True)
    bio_schema = load_schema(schema_dir, BIOSPECIMEN_SCHEMA_NAME)
    _write_and_fix(client, biospecimens, bio_schema, BIOSPECIMEN_SCHEMA_NAME, output_dir / "biospecimens.json")

    assays_dir = output_dir / "assays"
    assays_dir.mkdir(parents=True, exist_ok=True)
    assay_schemas = discover_assay_schemas(schema_dir)
    for schema_name, records in assays.items():
        schema = assay_schemas.get(schema_name)
        out_path = assays_dir / f"{schema_name}.json"
        if schema:
            _write_and_fix(client, records, schema, schema_name, out_path)
        else:
            with open(out_path, "w") as f:
                json.dump(records, f, indent=2)
            print(f"  wrote {out_path}")

    print(f"\nDemonstrator dataset written to {output_dir}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--schema-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--participants", type=int, default=5)
    parser.add_argument("--biospecimens-per-participant", type=int, default=3)
    args = parser.parse_args()

    if not args.schema_dir.exists():
        print(f"Error: schema directory not found: {args.schema_dir}", file=sys.stderr)
        sys.exit(1)

    run(args.schema_dir, args.output_dir, args.participants, args.biospecimens_per_participant)


if __name__ == "__main__":
    main()
