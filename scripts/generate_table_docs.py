#!/usr/bin/env python3
"""
Generate table-formatted documentation from LinkML schemas.
Attributes are shown in tables, enums are linked or shown inline if short.
"""
import os
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

def format_enum_values(enum_def, max_inline=5):
    """Format enum values - inline if short, link if long."""
    if not enum_def.permissible_values:
        return ""
    
    values = sorted(enum_def.permissible_values.items())
    if len(values) <= max_inline:
        # Show inline - just the value names
        value_list = ", ".join([f"`{pv_name}`" for pv_name, _ in values])
        return value_list
    else:
        # Link to enum section
        enum_anchor = enum_def.name.lower().replace('_', '-').replace('enum', '')
        return f"See [{enum_def.name}](#{enum_anchor}) enum below"

def generate_module_doc(schema_path: str, output_path: str):
    """Generate markdown with attributes in tables."""
    # Load the main schema
    schema = yaml_loader.load(str(schema_path), SchemaDefinition)
    
    # Load enums from imported files
    base_dir = Path(schema_path).parent
    all_enums = {}
    
    # Start with enums from main schema
    if schema.enums:
        for enum_name, enum_def in schema.enums.items():
            all_enums[enum_name] = enum_def
    
    # Load enums from imported files
    if schema.imports:
        for imp in schema.imports:
            if isinstance(imp, str) and not imp.startswith('linkml:'):
                # Try to find the enum file
                enum_file = base_dir / f"{imp}.yaml"
                if enum_file.exists():
                    try:
                        enum_schema = yaml_loader.load(str(enum_file), SchemaDefinition)
                        if enum_schema.enums:
                            for enum_name, enum_def in enum_schema.enums.items():
                                all_enums[enum_name] = enum_def
                    except Exception as e:
                        # Skip if can't load
                        pass
    
    # Replace schema.enums with our merged dict
    schema.enums = all_enums
    
    with open(output_path, 'w') as f:
        f.write(f"# {schema.name}\n\n")
        if schema.description:
            f.write(f"{schema.description}\n\n")
        
        # List all classes with attributes in tables
        if schema.classes:
            f.write("## Classes\n\n")
            for class_name, class_def in schema.classes.items():
                f.write(f"### {class_name}\n\n")
                if class_def.description:
                    f.write(f"{class_def.description}\n\n")
                
                # Attributes table
                if class_def.attributes:
                    f.write("**Attributes:**\n\n")
                    f.write("| Attribute | Type | Required | Description |\n")
                    f.write("|-----------|------|----------|-------------|\n")
                    
                    for attr_name, attr_def in sorted(class_def.attributes.items()):
                        required = "Yes" if attr_def.required else "No"
                        range_str = attr_def.range if attr_def.range else "string"
                        
                        # Check if range is an enum
                        enum_def = None
                        if schema.enums and range_str in schema.enums:
                            enum_def = schema.enums[range_str]
                        
                        if enum_def:
                            enum_values = format_enum_values(enum_def)
                            if enum_values and not enum_values.startswith("See"):
                                range_str = f"{range_str}<br/>{enum_values}"
                            elif enum_values:
                                range_str = enum_values
                        
                        description = attr_def.description or ""
                        # Escape pipe characters in description
                        description = description.replace("|", "\\|")
                        
                        f.write(f"| `{attr_name}` | {range_str} | {required} | {description} |\n")
                    f.write("\n")
        
        # Slots table
        if schema.slots:
            f.write("## Slots\n\n")
            f.write("| Slot | Type | Required | Description |\n")
            f.write("|------|------|----------|-------------|\n")
            
            for slot_name, slot_def in sorted(schema.slots.items()):
                required = "Yes" if slot_def.required else "No"
                range_str = slot_def.range if slot_def.range else "string"
                
                # Check if range is an enum
                enum_def = None
                if schema.enums and range_str in schema.enums:
                    enum_def = schema.enums[range_str]
                
                if enum_def:
                    enum_values = format_enum_values(enum_def)
                    if enum_values and not enum_values.startswith("See"):
                        range_str = f"{range_str}<br/>{enum_values}"
                    elif enum_values:
                        range_str = enum_values
                
                description = slot_def.description or ""
                description = description.replace("|", "\\|")
                
                f.write(f"| `{slot_name}` | {range_str} | {required} | {description} |\n")
            f.write("\n")
        
        # Enums section (show all enums, but prioritize those with many values)
        if schema.enums:
            # Separate enums by length
            short_enums = []
            long_enums = []
            for enum_name, enum_def in sorted(schema.enums.items()):
                if enum_def.permissible_values:
                    if len(enum_def.permissible_values) > 5:
                        long_enums.append((enum_name, enum_def))
                    else:
                        short_enums.append((enum_name, enum_def))
            
            # Show long enums first (they were linked from tables)
            if long_enums:
                f.write("## Enums\n\n")
                for enum_name, enum_def in long_enums:
                    enum_anchor = enum_name.lower().replace('_', '-').replace('enum', '')
                    f.write(f"### {enum_name} {{#{enum_anchor}}}\n\n")
                    if enum_def.description:
                        f.write(f"{enum_def.description}\n\n")
                    
                    f.write("| Value | Description |\n")
                    f.write("|-------|-------------|\n")
                    for pv_name, pv_def in sorted(enum_def.permissible_values.items()):
                        description = pv_def.description or ""
                        description = description.replace("|", "\\|")
                        f.write(f"| `{pv_name}` | {description} |\n")
                    f.write("\n")
            
            # Show short enums if any (for reference)
            if short_enums and not long_enums:
                f.write("## Enums\n\n")
                for enum_name, enum_def in short_enums:
                    f.write(f"### {enum_name}\n\n")
                    if enum_def.description:
                        f.write(f"{enum_def.description}\n\n")
                    
                    f.write("| Value | Description |\n")
                    f.write("|-------|-------------|\n")
                    for pv_name, pv_def in sorted(enum_def.permissible_values.items()):
                        description = pv_def.description or ""
                        description = description.replace("|", "\\|")
                        f.write(f"| `{pv_name}` | {description} |\n")
                    f.write("\n")

def main():
    base_dir = Path(__file__).parent.parent
    os.chdir(base_dir)
    
    for module_name, schema_path in MODULES.items():
        full_path = base_dir / schema_path
        if not full_path.exists():
            print(f"Warning: {full_path} not found")
            continue
        
        # Map module names to output filenames
        output_map = {
            "Clinical": "clinical",
            "Biospecimen": "biospecimen",
            "CoreFile": "corefile",
            "Sequencing": "sequencing",
            "WES": "wes",
            "scRNA-seq": "scrna-seq",
            "Imaging": "imaging",
            "DigitalPathology": "digitalpathology",
            "MultiplexMicroscopy": "multiplexmicroscopy",
            "SpatialOmics": "spatialomics",
        }
        
        output_path = base_dir / "docs" / f"{output_map[module_name]}.md"
        print(f"Generating {output_path}...")
        try:
            generate_module_doc(str(full_path), str(output_path))
        except Exception as e:
            print(f"Error generating {module_name}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()

