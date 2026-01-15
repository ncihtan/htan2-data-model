#!/usr/bin/env python3
"""
Generate simple attribute lists from LinkML schemas - no fancy formatting
"""
import yaml
from pathlib import Path
from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml_runtime.loaders import yaml_loader

MODULES = {
    "Clinical": "modules/Clinical/domains/clinical.yaml",
    "Biospecimen": "modules/Biospecimen/domains/biospecimen.yaml",
    "CoreFile": "modules/CoreFile/domains/core.yaml",
    "Sequencing": "modules/Sequencing/domains/sequencing.yaml",
    "WES": "modules/WES/domains/wes.yaml",
    "scRNA-seq": "modules/scRNA-seq/domains/scrna_seq.yaml",
    "Imaging": "modules/Imaging/domains/imaging.yaml",
    "DigitalPathology": "modules/DigitalPathology/domains/digital_pathology.yaml",
    "MultiplexMicroscopy": "modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml",
    "SpatialOmics": "modules/SpatialOmics/domains/spatial.yaml",
}

def generate_module_doc(schema_path: str, output_path: str):
    """Generate simple markdown with just attributes."""
    schema = yaml_loader.load(str(schema_path), SchemaDefinition)
    
    with open(output_path, 'w') as f:
        f.write(f"# {schema.name}\n\n")
        f.write(f"{schema.description or ''}\n\n")
        
        # List all classes
        if schema.classes:
            f.write("## Classes\n\n")
            for class_name, class_def in schema.classes.items():
                f.write(f"### {class_name}\n\n")
                if class_def.description:
                    f.write(f"{class_def.description}\n\n")
                
                # List attributes
                if class_def.attributes:
                    f.write("**Attributes:**\n\n")
                    for attr_name, attr_def in class_def.attributes.items():
                        required = "**Required**" if attr_def.required else "Optional"
                        range_str = attr_def.range if attr_def.range else "string"
                        f.write(f"- `{attr_name}` ({range_str}) - {required}\n")
                        if attr_def.description:
                            f.write(f"  - {attr_def.description}\n")
                    f.write("\n")
        
        # List all slots
        if schema.slots:
            f.write("## Slots\n\n")
            for slot_name, slot_def in sorted(schema.slots.items()):
                required = "**Required**" if slot_def.required else "Optional"
                range_str = slot_def.range if slot_def.range else "string"
                f.write(f"- `{slot_name}` ({range_str}) - {required}\n")
                if slot_def.description:
                    f.write(f"  - {slot_def.description}\n")
            f.write("\n")
        
        # List enums
        if schema.enums:
            f.write("## Enums\n\n")
            for enum_name, enum_def in sorted(schema.enums.items()):
                f.write(f"### {enum_name}\n\n")
                if enum_def.description:
                    f.write(f"{enum_def.description}\n\n")
                if enum_def.permissible_values:
                    f.write("**Values:**\n\n")
                    for pv_name, pv_def in sorted(enum_def.permissible_values.items()):
                        f.write(f"- `{pv_name}`")
                        if pv_def.description:
                            f.write(f" - {pv_def.description}")
                        f.write("\n")
                    f.write("\n")

def main():
    base_dir = Path(__file__).parent.parent
    os.chdir(base_dir)
    
    for module_name, schema_path in MODULES.items():
        full_path = base_dir / schema_path
        if not full_path.exists():
            print(f"Warning: {full_path} not found")
            continue
        
        output_path = base_dir / "docs" / f"{module_name.lower()}.md"
        print(f"Generating {output_path}...")
        try:
            generate_module_doc(str(full_path), str(output_path))
        except Exception as e:
            print(f"Error generating {module_name}: {e}")

if __name__ == "__main__":
    import os
    main()

