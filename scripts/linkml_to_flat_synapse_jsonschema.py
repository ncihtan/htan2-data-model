import subprocess
import sys
import json
from pathlib import Path

def run_gen_json_schema(linkml_yaml, class_name, tmp_json):
    cmd = f"gen-json-schema {linkml_yaml}"
    if class_name:
        cmd += f" --top-class {class_name}"
    cmd += f" > {tmp_json}"
    print(f"Running: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def run_flatten_jschema(input_json, flat_json):
    cmd = ["node", "scripts/flatten.js", str(input_json), str(flat_json)]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def remove_unsupported_fields(filepath):
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
    # 1. Generate JSON Schema
    run_gen_json_schema(linkml_yaml, class_name, tmp_json)
    # 2. Flatten JSON Schema
    run_flatten_jschema(tmp_json, output_file)
    # 2.5. Fix additionalProperties
    fix_additional_properties(output_file)
    # 3. Remove unsupported fields
    remove_unsupported_fields(output_file)
    # 4. Cleanup
    Path(tmp_json).unlink(missing_ok=True)
    print(f"✅ Synapse-compatible flat schema written to {output_file}")

if __name__ == "__main__":
    main() 