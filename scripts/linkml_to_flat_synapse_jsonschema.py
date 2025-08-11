#!/usr/bin/env python3
"""Convert LinkML YAML to Synapse-compatible flat JSON Schema.

This script converts LinkML YAML files to JSON Schema format that is compatible
with Synapse's JSON Schema service. It handles flattening, version conversion,
and Synapse-specific formatting requirements.
"""
from pathlib import Path
from typing import Any, Union
import argparse
import json
import subprocess
import sys

import jsonref
from linkml.generators.jsonschemagen import JsonSchemaGenerator


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


def _convert_to_plain_dict(obj) -> Union[dict, list, Any]:
    """Convert jsonref objects to plain Python dictionaries and lists.

    Recursively converts jsonref.JsonRef objects to plain Python data structures
    that can be serialized to JSON. This is needed because jsonref sometimes
    leaves special objects that aren't directly JSON serializable.

    Args:
        obj: The object to convert (dict, list, or other)

    Returns:
        Union[dict, list, Any]: Plain Python data structure
    """
    if isinstance(obj, dict):
        return {k: _convert_to_plain_dict(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_convert_to_plain_dict(item) for item in obj]
    else:
        return obj


def flatten_json_schema(input_path: str, output_path: str) -> Union[dict, list]:
    """Flatten/dereference $ref in a JSON Schema file using Python (jsonref)."""
    with open(input_path, "r") as f:
        schema = json.load(f)
    # Dereference $ref
    deref_schema = jsonref.JsonRef.replace_refs(schema)

    # Convert to plain dict to ensure JSON serializable
    deref_schema = _convert_to_plain_dict(deref_schema)
    with open(output_path, "w") as f:
        json.dump(deref_schema, f, indent=2)
    print(f"Flattened schema written to {output_path}")
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


def fix_schema_version(filepath: str) -> None:
    """Update the $schema field to use Draft-07 for Synapse compatibility."""
    with open(filepath, "r") as f:
        data = json.load(f)

    # Update $schema to Draft-07
    data, message = _fix_schema_version_logic(data)
    print(message)

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Fixed schema version in {filepath}")


def remove_unsupported_fields(filepath: str) -> None:
    """Remove fields that are not supported by Synapse JSON Schema service."""
    with open(filepath, "r") as f:
        data = json.load(f)

    def recursive_clean(obj):
        if isinstance(obj, dict):
            # Remove unsupported fields (don't process them recursively)
            unsupported_fields = ["$defs", "metamodel_version", "version"]
            for field in unsupported_fields:
                obj.pop(field, None)  # Safely remove if exists

            # Recursively process remaining values
            for value in obj.values():
                recursive_clean(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive_clean(item)

    recursive_clean(data)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Cleaned unsupported fields from {filepath}")


def fix_additional_properties(filepath: str) -> None:
    """Recursively replace boolean additionalProperties with {} in a JSON Schema file."""
    with open(filepath, "r") as f:
        data = json.load(f)

    def recursive_fix(obj):
        if isinstance(obj, dict):
            if "additionalProperties" in obj and isinstance(
                obj["additionalProperties"], bool
            ):
                obj["additionalProperties"] = {}
            for value in obj.values():
                recursive_fix(value)
        elif isinstance(obj, list):
            for item in obj:
                recursive_fix(item)

    recursive_fix(data)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Fixed additionalProperties in {filepath}")


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

    output_dir = Path(args.output_dir)
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / output_filename
    tmp_json = output_file.with_suffix(output_file.suffix + ".tmp.json")

    # 1. Generate JSON Schema using Python library
    run_gen_json_schema(args.linkml_yaml, args.class_name, tmp_json)

    # 2. Flatten JSON Schema using Python
    flatten_json_schema(tmp_json, output_file)

    # 3. Fix schema version to Draft-07
    fix_schema_version(output_file)

    # 4. Fix additionalProperties
    fix_additional_properties(output_file)

    # 5. Remove unsupported fields
    remove_unsupported_fields(output_file)

    # 6. Cleanup
    Path(tmp_json).unlink(missing_ok=True)
    print(f"✅ Synapse-compatible flat schema written to {output_file}")


if __name__ == "__main__":
    main()
