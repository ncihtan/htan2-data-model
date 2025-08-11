#!/usr/bin/env python3
"""Convert LinkML YAML to Synapse-compatible flat JSON Schema.

This script converts LinkML YAML files to JSON Schema format that is compatible
with Synapse's JSON Schema service. It handles flattening, version conversion,
and Synapse-specific formatting requirements.
"""
import subprocess
import sys
import json
from pathlib import Path
import jsonref
from linkml.generators.jsonschemagen import JsonSchemaGenerator

def run_gen_json_schema(linkml_yaml, class_name, tmp_json):
    """Generate JSON Schema from LinkML YAML using Python library."""
    print(f"Generating JSON Schema from {linkml_yaml}")
    
    # Use the Python library instead of shell command
    generator = JsonSchemaGenerator(linkml_yaml)
    if class_name:
        generator.top_class = class_name
    
    # Generate the schema
    schema_str = generator.serialize()
    
    # Write to temporary file
    with open(tmp_json, 'w') as f:
        f.write(schema_str)
    
    print(f"Generated JSON Schema written to {tmp_json}")

def flatten_json_schema(input_path, output_path):
    """Flatten/dereference $ref in a JSON Schema file using Python (jsonref)."""
    with open(input_path, 'r') as f:
        schema = json.load(f)
    # Dereference $ref
    deref_schema = jsonref.JsonRef.replace_refs(schema)
    # Convert to plain dict to ensure JSON serializable
    def convert_to_plain_dict(obj):
        if isinstance(obj, dict):
            return {k: convert_to_plain_dict(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert_to_plain_dict(item) for item in obj]
        else:
            return obj
    
    deref_schema = convert_to_plain_dict(deref_schema)
    with open(output_path, 'w') as f:
        json.dump(deref_schema, f, indent=2)
    print(f"Flattened schema written to {output_path}")

def fix_schema_version(filepath):
    """Update the $schema field to use Draft-07 for Synapse compatibility."""
    with open(filepath, "r") as f:
        data = json.load(f)
    
    # Update $schema to Draft-07
    if "$schema" in data:
        current_schema = data["$schema"]
        if "draft-07" not in current_schema:
            data["$schema"] = "https://json-schema.org/draft-07/schema"
            print(f"Updated $schema from '{current_schema}' to 'https://json-schema.org/draft-07/schema'")
        else:
            print(f"$schema already uses Draft-07: {current_schema}")
    else:
        # Add $schema if it doesn't exist
        data["$schema"] = "https://json-schema.org/draft-07/schema"
        print("Added $schema field with Draft-07")
    
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Fixed schema version in {filepath}")

def remove_unsupported_fields(filepath):
    """Remove fields that are not supported by Synapse JSON Schema service."""
    with open(filepath, "r") as f:
        data = json.load(f)
    
    def recursive_clean(obj):
        if isinstance(obj, dict):
            for field in ["$defs", "metamodel_version", "version"]:
                if field in obj:
                    del obj[field]
            for v in obj.values():
                recursive_clean(v)
        elif isinstance(obj, list):
            for item in obj:
                recursive_clean(item)
    
    recursive_clean(data)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Cleaned unsupported fields from {filepath}")

def fix_additional_properties(filepath):
    """Recursively replace boolean additionalProperties with {} in a JSON Schema file."""
    with open(filepath, "r") as f:
        data = json.load(f)
    
    def recursive_fix(obj):
        if isinstance(obj, dict):
            if "additionalProperties" in obj and isinstance(obj["additionalProperties"], bool):
                obj["additionalProperties"] = {}
            for v in obj.values():
                recursive_fix(v)
        elif isinstance(obj, list):
            for item in obj:
                recursive_fix(item)
    
    recursive_fix(data)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Fixed additionalProperties in {filepath}")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 4:
        print("Usage: python linkml_to_flat_synapse_jsonschema.py <linkml_yaml> [class_name] [output_filename]")
        sys.exit(1)
    
    linkml_yaml = sys.argv[1]
    class_name = sys.argv[2] if len(sys.argv) > 2 else ""
    if len(sys.argv) == 4:
        output_filename = sys.argv[3]
    else:
        base = Path(linkml_yaml).stem
        output_filename = f"{base}.flat.schema.json"
    
    output_dir = Path("JSON_Schemas")
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / output_filename
    tmp_json = output_file.with_suffix(output_file.suffix + ".tmp.json")
    
    # 1. Generate JSON Schema using Python library
    run_gen_json_schema(linkml_yaml, class_name, tmp_json)
    
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