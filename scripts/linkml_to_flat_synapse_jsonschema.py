#!/usr/bin/env python3
"""Convert LinkML YAML to Synapse-compatible flat JSON Schema.

This script converts LinkML YAML files to JSON Schema format that is compatible
with Synapse's JSON Schema service. It handles flattening, version conversion,
and Synapse-specific formatting requirements.

Key transformations:
- Flattens JSON schemas (removes $ref and $defs)
- Converts schema version to Draft-07 (Synapse requirement)
- Fixes additionalProperties (converts boolean to {})
- Cleans union types (removes null from type arrays)
- Fixes boolean pattern checks (converts pattern: "^true$" to const: true for boolean fields)
- Removes unsupported fields ($defs, metamodel_version, version)

Note on boolean pattern fixes:
LinkML rules with pattern: "^true$" or "^false$" for boolean fields are converted
to const: true or const: false because JSON Schema's pattern keyword only applies
to strings, not booleans. This ensures conditional requirements work correctly
for boolean fields in the generated JSON Schema.
"""
from pathlib import Path
from typing import Any, Union
import argparse
import json
import subprocess
import sys

import jsonref
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml_runtime.utils.schemaview import SchemaView


def run_gen_json_schema(linkml_yaml: str, class_name: str, tmp_json: str) -> None:
    """Generate JSON Schema from LinkML YAML using Python library.

    Converts a LinkML YAML file to JSON Schema format using the LinkML
    JsonSchemaGenerator. The generated schema is written to a temporary file
    for further processing (flattening, version conversion, etc.).

    Args:
        linkml_yaml (str): Path to the input LinkML YAML file
        class_name (str): Name of the top-level class to generate schema for.
                         If empty string, uses the default class from the schema.
        tmp_json (str): Path to the temporary JSON file where the generated
                       schema will be written

    Raises:
        FileNotFoundError: If the LinkML YAML file cannot be found
        ValueError: If there's an error in the LinkML schema or generation process
        OSError: If there's an error writing the output file

    Returns:
        None: The function writes the generated schema to the specified file
    """
    print(f"Generating JSON Schema from {linkml_yaml}")

    # Use the Python library instead of shell command
    generator = JsonSchemaGenerator(linkml_yaml)
    if class_name:
        generator.top_class = class_name

    # Generate the schema
    schema_str = generator.serialize()

    # Write to temporary file
    with open(tmp_json, "w") as f:
        f.write(schema_str)

    print(f"Generated JSON Schema written to {tmp_json}")


def _convert_to_plain_dict(obj, visited=None) -> Union[dict, list, Any]:
    """Convert jsonref objects to plain Python dictionaries and lists.

    Recursively converts jsonref.JsonRef objects to plain Python data structures
    that can be serialized to JSON. This is needed because jsonref sometimes
    leaves special objects that aren't directly JSON serializable.

    Args:
        obj: The object to convert (dict, list, or other)
        visited: Set of already visited objects to prevent infinite recursion

    Returns:
        Union[dict, list, Any]: Plain Python data structure
    """
    if visited is None:
        visited = set()

    # Prevent infinite recursion by tracking visited objects
    obj_id = id(obj)
    if obj_id in visited:
        return obj  # Return the object as-is to break recursion

    visited.add(obj_id)

    try:
        if isinstance(obj, dict):
            return {k: _convert_to_plain_dict(v, visited) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [_convert_to_plain_dict(item, visited) for item in obj]
        else:
            return obj
    finally:
        visited.discard(obj_id)  # Clean up visited set


def flatten_json_schema(schema_data: dict) -> dict:
    """Flatten/dereference $ref in a JSON Schema data using Python (jsonref)."""
    # Dereference $ref
    deref_schema = jsonref.JsonRef.replace_refs(schema_data)

    # Convert to plain dict to ensure JSON serializable
    deref_schema = _convert_to_plain_dict(deref_schema)
    print("Flattened schema in memory")
    return deref_schema


def _fix_schema_version_logic(data: dict) -> tuple[dict, str]:
    """Update the $schema field to use Draft-07 for Synapse compatibility.

    Args:
        data: JSON Schema data as dictionary

    Returns:
        tuple[dict, str]: Updated data and status message
    """
    if "$schema" in data:
        current_schema = data["$schema"]
        if "draft-07" not in current_schema:
            data["$schema"] = "https://json-schema.org/draft-07/schema"
            message = f"Updated $schema from '{current_schema}' to 'https://json-schema.org/draft-07/schema'"
        else:
            message = f"$schema already uses Draft-07: {current_schema}"
    else:
        # Add $schema if it doesn't exist
        data["$schema"] = "https://json-schema.org/draft-07/schema"
        message = "Added $schema field with Draft-07"

    return data, message


def fix_schema_version(schema_data: dict) -> dict:
    """Update the $schema field to use Draft-07 for Synapse compatibility."""
    # Update $schema to Draft-07
    schema_data, message = _fix_schema_version_logic(schema_data)
    print(message)
    return schema_data


def remove_unsupported_fields(schema_data: dict) -> dict:
    """Remove fields that are not supported by Synapse JSON Schema service."""

    def recursive_clean(obj, visited=None):
        if visited is None:
            visited = set()

        # Prevent infinite recursion by tracking visited objects
        obj_id = id(obj)
        if obj_id in visited:
            return
        visited.add(obj_id)

        try:
            if isinstance(obj, dict):
                # Remove unsupported fields (don't process them recursively)
                unsupported_fields = ["$defs", "metamodel_version", "version"]
                for field in unsupported_fields:
                    obj.pop(field, None)  # Safely remove if exists

                # Recursively process remaining values
                for value in obj.values():
                    recursive_clean(value, visited)
            elif isinstance(obj, list):
                for item in obj:
                    recursive_clean(item, visited)
        except (RecursionError, TypeError, AttributeError) as e:
            # Skip problematic objects
            print(f"Warning: Skipping object due to error: {e}")
            pass

    recursive_clean(schema_data)
    print("Cleaned unsupported fields from schema")
    return schema_data


def fix_additional_properties(schema_data: dict) -> dict:
    """Recursively replace boolean additionalProperties with {} in a JSON Schema data."""

    def recursive_fix(obj, visited=None):
        if visited is None:
            visited = set()

        # Prevent infinite recursion by tracking visited objects
        obj_id = id(obj)
        if obj_id in visited:
            return
        visited.add(obj_id)

        try:
            if isinstance(obj, dict):
                if "additionalProperties" in obj and isinstance(
                    obj["additionalProperties"], bool
                ):
                    obj["additionalProperties"] = {}
                for value in obj.values():
                    recursive_fix(value, visited)
            elif isinstance(obj, list):
                for item in obj:
                    recursive_fix(item, visited)
        except (RecursionError, TypeError, AttributeError) as e:
            # Skip problematic objects
            print(f"Warning: Skipping object due to error: {e}")
            pass

    recursive_fix(schema_data)
    print("Fixed additionalProperties in schema")
    return schema_data


def clean_union_types(schema_data: dict) -> dict:
    """Recursively clean union types like ["string", "null"] to just "string"."""

    def recursive_clean_union(obj, visited=None):
        if visited is None:
            visited = set()

        # Prevent infinite recursion by tracking visited objects
        obj_id = id(obj)
        if obj_id in visited:
            return
        visited.add(obj_id)

        try:
            if isinstance(obj, dict):
                # Clean union types in type fields
                if "type" in obj and isinstance(obj["type"], list):
                    # Keep only the first non-null type
                    types = [t for t in obj["type"] if t != "null"]
                    if types:
                        obj["type"] = types[0]  # Use first non-null type
                    else:
                        obj["type"] = "string"  # Default to string if only null

                # Recursively process remaining values
                for value in obj.values():
                    recursive_clean_union(value, visited)
            elif isinstance(obj, list):
                for item in obj:
                    recursive_clean_union(item, visited)
        except (RecursionError, TypeError, AttributeError) as e:
            # Skip problematic objects
            print(f"Warning: Skipping object due to error: {e}")
            pass

    recursive_clean_union(schema_data)
    print("Cleaned union types from schema")
    return schema_data


def fix_boolean_patterns(schema_data: dict) -> dict:
    """Convert pattern checks for boolean fields to const checks.

    LinkML rules with pattern: "^true$" or "^false$" for boolean fields
    need to be converted to const: true or const: false in JSON Schema,
    since pattern only applies to strings, not booleans.

    This is necessary because:
    - JSON Schema's `pattern` keyword only validates strings
    - Boolean fields use `const` for exact value matching
    - LinkML generates `pattern: "^true$"` for boolean checks in rules
    - The conversion ensures conditional requirements work correctly

    Example transformation:
    - Before: {"HAS_SLIDE_LABEL": {"pattern": "^true$"}}
    - After:  {"HAS_SLIDE_LABEL": {"const": true}}

    Only affects properties with type: "boolean" in the schema.
    String fields with patterns are left unchanged.
    """
    # Get property types from the schema
    properties = schema_data.get("properties", {})

    def fix_boolean_patterns_in_obj(obj, visited=None):
        if visited is None:
            visited = set()

        obj_id = id(obj)
        if obj_id in visited:
            return
        visited.add(obj_id)

        try:
            if isinstance(obj, dict):
                # Check if this is an "if" clause with properties
                if "if" in obj and isinstance(obj["if"], dict):
                    if_clause = obj["if"]
                    if "properties" in if_clause:
                        for prop_name, prop_schema in if_clause["properties"].items():
                            # Check if this property is a boolean type
                            prop_def = properties.get(prop_name, {})
                            if prop_def.get("type") == "boolean":
                                # Convert pattern to const for boolean fields
                                if "pattern" in prop_schema:
                                    pattern = prop_schema["pattern"]
                                    if pattern == "^true$":
                                        prop_schema["const"] = True
                                        del prop_schema["pattern"]
                                    elif pattern == "^false$":
                                        prop_schema["const"] = False
                                        del prop_schema["pattern"]

                # Recursively process allOf arrays (where rules are typically stored)
                if "allOf" in obj and isinstance(obj["allOf"], list):
                    for item in obj["allOf"]:
                        fix_boolean_patterns_in_obj(item, visited)

                # Recursively process nested objects
                for value in obj.values():
                    fix_boolean_patterns_in_obj(value, visited)
            elif isinstance(obj, list):
                for item in obj:
                    fix_boolean_patterns_in_obj(item, visited)
        except (RecursionError, TypeError, AttributeError) as e:
            print(f"Warning: Skipping object due to error: {e}")
            pass

    fix_boolean_patterns_in_obj(schema_data)
    print("Fixed boolean pattern checks to use const")
    return schema_data


def _build_contains_from_anon_slot(anon_slot) -> Union[dict, None]:
    """Translate a LinkML AnonymousSlotExpression into a JSON Schema fragment
    expressing "the multivalued slot contains a member matching this constraint."

    Handles two shapes that appear in HTAN rule preconditions:
    - Direct: ``has_member: { equals_string: "X" }`` -> ``{contains: {const: "X"}}``
    - any_of of branches, each carrying a ``has_member`` block
      -> ``{anyOf: [{contains: ...}, ...]}``

    Returns None when the slot expression has no translatable member constraint
    so the caller can leave the existing JSON fragment untouched.
    """
    if anon_slot is None:
        return None

    any_of = getattr(anon_slot, "any_of", None)
    if any_of:
        branches = []
        for sub in any_of:
            sub_fragment = _build_contains_from_anon_slot(sub)
            if sub_fragment:
                branches.append(sub_fragment)
        if branches:
            return {"anyOf": branches}
        return None

    has_member = getattr(anon_slot, "has_member", None)
    if not has_member:
        return None

    contains: dict = {}
    if getattr(has_member, "equals_string", None):
        contains["const"] = has_member.equals_string
    elif getattr(has_member, "equals_string_in", None):
        contains["enum"] = list(has_member.equals_string_in)
    elif getattr(has_member, "pattern", None):
        contains["pattern"] = has_member.pattern
    else:
        return None
    return {"contains": contains}


def fix_multivalued_member_constraints(
    schema_data: dict, linkml_yaml: str, class_name: str
) -> dict:
    """Rewrite rule preconditions on multivalued slots to use JSON Schema ``contains``.

    LinkML's ``JsonSchemaGenerator`` processes rule preconditions with
    ``omit_type=True``, which short-circuits the array-aware code path that
    translates ``has_member`` into ``contains``. The result is an empty ``{}``
    constraint on the multivalued slot inside the ``if`` clause, which means the
    ``if`` is vacuously satisfied for every record and the ``then`` requirements
    fire unconditionally (HTAN-859).

    This function walks the source LinkML schema to recover the original
    ``has_member`` expressions for each rule's precondition slots and replaces
    the empty fragments in the generated JSON with proper ``contains`` clauses.
    Matching is positional: rules from the class and its ancestors are zipped
    against the JSON output's ``allOf`` (or top-level ``if``), mirroring how
    ``JsonSchemaGenerator`` emits them.

    Only runs when ``class_name`` is set so the SchemaView can resolve which
    slots are multivalued in the context of the target class.
    """
    if not class_name:
        return schema_data

    sv = SchemaView(linkml_yaml)
    try:
        ancestor_names = sv.class_ancestors(class_name)
    except Exception:
        return schema_data

    rules = []
    for ancestor_name in ancestor_names:
        cls = sv.get_class(ancestor_name)
        if cls and getattr(cls, "rules", None):
            rules.extend(cls.rules)

    if not rules:
        return schema_data

    if_then_blocks: list[dict] = []
    if isinstance(schema_data.get("allOf"), list):
        if_then_blocks = [item for item in schema_data["allOf"] if isinstance(item, dict) and "if" in item]
    elif "if" in schema_data:
        if_then_blocks = [schema_data]

    if len(rules) != len(if_then_blocks):
        print(
            f"Warning: rule count ({len(rules)}) does not match if/then block count "
            f"({len(if_then_blocks)}); skipping multivalued precondition fix"
        )
        return schema_data

    fixed = 0
    for rule, block in zip(rules, if_then_blocks):
        preconditions = getattr(rule, "preconditions", None)
        if not preconditions:
            continue
        slot_conditions = getattr(preconditions, "slot_conditions", None) or {}
        if_props = block.get("if", {}).get("properties", {})
        for slot_name, anon_slot in slot_conditions.items():
            if slot_name not in if_props:
                continue
            try:
                induced = sv.induced_slot(slot_name, class_name)
            except Exception:
                continue
            if not getattr(induced, "multivalued", False):
                continue
            replacement = _build_contains_from_anon_slot(anon_slot)
            if not replacement:
                continue
            if_props[slot_name].clear()
            if_props[slot_name].update(replacement)
            fixed += 1

    if fixed:
        print(f"Fixed {fixed} multivalued precondition constraint(s) using `contains`")
    return schema_data


def backfill_descriptions_from_linkml(
    schema_data: dict, linkml_yaml: str, class_name: str
) -> dict:
    """Set description on any top-level property that is missing it, using the LinkML schema.

    LinkML's JsonSchemaGenerator can omit descriptions for some properties (e.g. inherited).
    Uses induced_slot() when class_name is set so slot_usage overrides from the class
    are applied; falls back to get_slot() on resolution failure or when class_name is empty.
    """
    sv = SchemaView(linkml_yaml)
    props = schema_data.get("properties", {})
    filled = 0
    for prop_name, prop_val in props.items():
        if not isinstance(prop_val, dict) or prop_val.get("description"):
            continue
        try:
            slot = (
                sv.induced_slot(prop_name, class_name)
                if class_name
                else sv.get_slot(prop_name)
            )
        except Exception:
            slot = sv.get_slot(prop_name)
        if slot and getattr(slot, "description", None):
            prop_val["description"] = slot.description
            filled += 1
    if filled:
        print(f"Backfilled {filled} missing description(s) from LinkML schema")
    return schema_data


def get_args():
    """Set up command-line interface and get arguments."""
    parser = argparse.ArgumentParser(
        description="Convert LinkML YAML to Synapse-compatible flat JSON Schema"
    )
    parser.add_argument(
        "linkml_yaml",
        type=str,
        help="Path to the input LinkML YAML file",
    )
    parser.add_argument(
        "--class-name",
        "-c",
        type=str,
        default="",
        help="Name of the top-level class to generate schema for (optional)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        help="Output filename (optional, defaults to <input>.flat.schema.json)",
    )
    parser.add_argument(
        "--output-dir",
        "-d",
        type=str,
        default="JSON_Schemas",
        help="Output directory (default: JSON_Schemas)",
    )
    return parser.parse_args()


def main():
    args = get_args()

    # Determine output filename
    if args.output:
        output_filename = args.output
    else:
        base = Path(args.linkml_yaml).stem
        output_filename = f"{base}.flat.schema.json"

    if args.output:
        # If output is specified, use it directly
        output_file = Path(args.output)
        output_file.parent.mkdir(parents=True, exist_ok=True)
    else:
        # If no output specified, use output_dir
        output_dir = Path(args.output_dir)
        output_dir.mkdir(exist_ok=True)
        output_file = output_dir / output_filename
    tmp_json = output_file.with_suffix(output_file.suffix + ".tmp.json")

    # 1. Generate JSON Schema using Python library
    run_gen_json_schema(args.linkml_yaml, args.class_name, tmp_json)

    # 2. Read the generated schema into memory
    with open(tmp_json, "r") as f:
        schema_data = json.load(f)

    # 3. Process schema in memory (no file I/O between steps)
    schema_data = flatten_json_schema(schema_data)
    schema_data = fix_schema_version(schema_data)
    schema_data = backfill_descriptions_from_linkml(
        schema_data, args.linkml_yaml, args.class_name
    )
    schema_data = fix_additional_properties(schema_data)
    schema_data = clean_union_types(schema_data)
    schema_data = fix_boolean_patterns(schema_data)
    schema_data = fix_multivalued_member_constraints(
        schema_data, args.linkml_yaml, args.class_name
    )
    schema_data = remove_unsupported_fields(schema_data)

    # 4. Write final result to output file
    with open(output_file, "w") as f:
        json.dump(schema_data, f, indent=2)

    # 5. Cleanup
    Path(tmp_json).unlink(missing_ok=True)
    print(f"✅ Synapse-compatible flat schema written to {output_file}")


if __name__ == "__main__":
    main()
