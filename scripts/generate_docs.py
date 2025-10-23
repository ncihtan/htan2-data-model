import yaml
import os
import re
from pathlib import Path


def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def generate_basic_type_doc(type_name, output_dir):
    """Generate documentation for basic types (string, integer, decimal)"""
    content = f"# {type_name.capitalize()}\n\n"
    if type_name == "string":
        content += "This field accepts any text value.\n"
    elif type_name == "integer":
        content += "This field accepts whole numbers.\n"
    elif type_name == "decimal":
        content += "This field accepts decimal numbers.\n"

    output_path = os.path.join(output_dir, f"{type_name.capitalize()}.md")
    with open(output_path, "w") as f:
        f.write(content)


def generate_attribute_table(schema):
    """Generate markdown table for attributes without cardinality/range"""
    table = "| Name | Description | Slot URI |\n"
    table += "| --- | --- | --- |\n"

    # Handle files with classes
    if "classes" in schema:
        class_name = next(iter(schema.get("classes", {})))
        class_def = schema["classes"][class_name]

        # For each attribute in the class
        for attr_name, attr_def in class_def.get("attributes", {}).items():
            description = attr_def.get("description", "")
            slot_uri = attr_def.get("slot_uri", "")
            # Get the enum name from the range
            range_type = attr_def.get("range", "")

            # Handle basic types
            if range_type in ["string", "integer", "decimal"]:
                table += f"| {attr_name} | {description} | {slot_uri} |\n"
            else:
                table += (
                    f"| [{attr_name}]({range_type}.md) | {description} | {slot_uri} |\n"
                )

    # Handle files with only enums
    elif "enums" in schema:
        for enum_name, enum_def in schema.get("enums", {}).items():
            description = enum_def.get("description", "")
            slot_uri = enum_def.get("slot_uri", "")
            title = enum_def.get("title", enum_name)
            table += f"| [{title}]({enum_name}.md) | {description} | {slot_uri} |\n"

    return table


def generate_enum_table(enum):
    """Generate markdown table for enum values"""
    table = "| Permissible Value | Description |\n"
    table += "| --- | --- |\n"

    for value, details in enum.get("permissible_values", {}).items():
        description = details.get("description", "")
        table += f"| {value} | {description} |\n"

    return table


def get_module_name(yaml_path):
    """Get the correct module name based on the YAML file name"""
    name_map = {
        "demographics.yaml": "Demographics",
        "diagnosis.yaml": "Diagnosis",
        "exposure.yaml": "Exposure",
        "family_history.yaml": "FamilyHistory",
        "followup.yaml": "FollowUp",
        "molecular.yaml": "MolecularTest",
        "therapy.yaml": "Therapy",
        "vital_status.yaml": "VitalStatus",
    }
    return name_map.get(
        os.path.basename(yaml_path),
        os.path.splitext(os.path.basename(yaml_path))[0].capitalize(),
    )


def generate_module_docs(yaml_path, output_dir):
    """Generate documentation for a single module"""
    schema = load_yaml(yaml_path)
    module_name = get_module_name(yaml_path)

    # Create main module documentation
    main_content = f"# {schema.get('name', module_name)}\n\n"
    main_content += f"{schema.get('description', '')}\n\n"
    main_content += f"URI: {schema.get('id', '')}\n\n"
    main_content += "## Attributes\n\n"
    main_content += generate_attribute_table(schema)

    # Write main module documentation
    main_output_path = os.path.join(output_dir, f"{module_name}.md")
    with open(main_output_path, "w") as f:
        f.write(main_content)

    # Generate documentation for each enum
    for enum_name, enum_def in schema.get("enums", {}).items():
        enum_content = f"# {enum_name}\n\n"
        enum_content += f"URI: {schema.get('id', '')}/{enum_name}\n\n"
        enum_content += "## Permissible Values\n\n"
        enum_content += generate_enum_table(enum_def)

        # Write enum documentation
        enum_output_path = os.path.join(output_dir, f"{enum_name}.md")
        with open(enum_output_path, "w") as f:
            f.write(enum_content)


def main():
    # Set up paths
    modules_dir = "modules/Clinical/domains"
    output_dir = "docs"

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Generate documentation for basic types
    for type_name in ["string", "integer", "decimal"]:
        generate_basic_type_doc(type_name, output_dir)

    # Process each YAML file in the modules directory
    for yaml_file in Path(modules_dir).glob("*.yaml"):
        if yaml_file.name != "clinical.yaml":  # Skip the main clinical schema
            try:
                generate_module_docs(str(yaml_file), output_dir)
                print(f"Generated documentation for {yaml_file.name}")
            except Exception as e:
                print(f"Error processing {yaml_file.name}: {str(e)}")


if __name__ == "__main__":
    main()
