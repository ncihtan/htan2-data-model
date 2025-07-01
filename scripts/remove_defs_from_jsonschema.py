import json
import sys
from pathlib import Path

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python remove_defs_from_jsonschema.py [file]")
        sys.exit(1)
    remove_unsupported_fields(sys.argv[1]) 