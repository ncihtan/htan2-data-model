#!/usr/bin/env python3
"""
Generate table-formatted documentation from LinkML schemas.
For Clinical: Show each class separately with attributes
For WES: Show each level separately with attributes
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
    """Format enum values - link to enum section (cleaner representation)."""
    if not enum_def.permissible_values:
        return ""
    
    # Always link to enum section for cleaner representation
    enum_anchor = enum_def.name.lower().replace('_', '-').replace('enum', '')
    return f"[{enum_def.name}](#{enum_anchor})"

def get_conditional_requirements(class_def, attr_name):
    """Extract conditional requirements from slot_usage and rules."""
    conditions = []
    
    # Check slot_usage first (simpler, more direct)
    if class_def.slot_usage and attr_name in class_def.slot_usage:
        slot_usage = class_def.slot_usage[attr_name]
        if slot_usage.description:
            desc = slot_usage.description
            if "Required when" in desc:
                # Extract the condition part
                condition = desc.replace("Required when ", "").strip()
                conditions.append(condition)
            elif "required when" in desc.lower():
                condition = desc.split("required when", 1)[1].strip()
                conditions.append(condition)
    
    # Check rules as fallback
    if not conditions and class_def.rules:
        for rule in class_def.rules:
            if rule.postconditions and rule.postconditions.slot_conditions:
                if attr_name in rule.postconditions.slot_conditions:
                    postcond = rule.postconditions.slot_conditions[attr_name]
                    if hasattr(postcond, 'required') and postcond.required:
                        # Extract precondition
                        if rule.preconditions and rule.preconditions.slot_conditions:
                            precond_desc = []
                            for precond_attr, precond_val in rule.preconditions.slot_conditions.items():
                                if hasattr(precond_val, 'equals_string'):
                                    precond_desc.append(f"{precond_attr} = '{precond_val.equals_string}'")
                                elif hasattr(precond_val, 'any_of'):
                                    # Extract patterns
                                    patterns = []
                                    for pattern_obj in precond_val.any_of:
                                        if hasattr(pattern_obj, 'pattern'):
                                            # Clean up pattern
                                            pattern = pattern_obj.pattern.replace('.*', '').replace('^', '').replace('$', '')
                                            if pattern:
                                                patterns.append(pattern)
                                    if patterns:
                                        precond_desc.append(f"{precond_attr} matches '{' or '.join(patterns)}'")
                                elif hasattr(precond_val, 'required') and precond_val.required:
                                    precond_desc.append(f"{precond_attr} is present")
                            if precond_desc:
                                conditions.append("when " + " and ".join(precond_desc))
    
    return conditions

def generate_class_table(class_name, class_def, all_enums, f):
    """Generate attributes table for a class."""
    if class_def.description:
        f.write(f"**{class_def.description}**\n\n")
    
    if class_def.attributes:
        f.write("| Attribute | Type | Required | Description |\n")
        f.write("|-----------|------|----------|-------------|\n")
        
        for attr_name, attr_def in sorted(class_def.attributes.items()):
            # Get base required status
            required = "Yes" if attr_def.required else "No"
            
            # Get conditional requirements
            conditions = get_conditional_requirements(class_def, attr_name)
            if conditions:
                required = f"No<br/>*Required {', '.join(conditions)}*"
            
            range_str = attr_def.range if attr_def.range else "string"
            
            # Check if range is an enum
            enum_def = None
            if all_enums and range_str in all_enums:
                enum_def = all_enums[range_str]
            
            if enum_def:
                enum_values = format_enum_values(enum_def)
                range_str = enum_values
            
            description = attr_def.description or ""
            description = description.replace("|", "\\|")
            
            f.write(f"| `{attr_name}` | {range_str} | {required} | {description} |\n")
        f.write("\n")

def generate_module_doc(schema_path: str, output_path: str):
    """Generate markdown with attributes in tables."""
    # Load the main schema
    schema = yaml_loader.load(str(schema_path), SchemaDefinition)
    base_dir = Path(schema_path).parent
    
    all_enums = {}
    all_classes = {}
    
    # Start with enums and classes from main schema
    if schema.enums:
        for enum_name, enum_def in schema.enums.items():
            all_enums[enum_name] = enum_def
    
    if schema.classes:
        for class_name, class_def in schema.classes.items():
            all_classes[class_name] = class_def
    
    # Load enums and classes from imported files
    if schema.imports:
        for imp in schema.imports:
            if isinstance(imp, str) and not imp.startswith('linkml:'):
                # Try to find the file
                import_file = base_dir / f"{imp}.yaml"
                if import_file.exists():
                    try:
                        import_schema = yaml_loader.load(str(import_file), SchemaDefinition)
                        if import_schema.enums:
                            for enum_name, enum_def in import_schema.enums.items():
                                all_enums[enum_name] = enum_def
                        if import_schema.classes:
                            for class_name, class_def in import_schema.classes.items():
                                all_classes[class_name] = class_def
                    except Exception as e:
                        # Skip if can't load
                        pass
    
    with open(output_path, 'w') as f:
        f.write(f"# {schema.name}\n\n")
        if schema.description:
            f.write(f"{schema.description}\n\n")
        
        # Special handling for Clinical - show each class separately
        if schema.name == "Clinical":
            f.write("## Classes\n\n")
            # Show main ClinicalData class first, but rename to "Manifests"
            if "ClinicalData" in all_classes:
                f.write("### Manifests\n\n")
                generate_class_table("ClinicalData", all_classes["ClinicalData"], all_enums, f)
            
            # Then show all other classes
            for class_name, class_def in sorted(all_classes.items()):
                if class_name != "ClinicalData":
                    f.write(f"### {class_name}\n\n")
                    generate_class_table(class_name, class_def, all_enums, f)
        
        # Enums section for Clinical - show all enums in tables
        if schema.name == "Clinical" and all_enums:
            f.write("## Enums\n\n")
            for enum_name, enum_def in sorted(all_enums.items()):
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
        
        # Special handling for WES - show each level separately
        elif schema.name == "WES":
            f.write("## Levels\n\n")
            # Load level schemas
            level_files = {
                "Level 1": base_dir / "level_1.yaml",
                "Level 2": base_dir / "level_2.yaml",
                "Level 3": base_dir / "level_3.yaml",
            }
            
            for level_name, level_file in level_files.items():
                if level_file.exists():
                    try:
                        level_schema = yaml_loader.load(str(level_file), SchemaDefinition)
                        level_enums = {}
                        if level_schema.enums:
                            level_enums.update(level_schema.enums)
                        
                        # Load enums from level file imports too
                        if level_schema.imports:
                            for imp in level_schema.imports:
                                if isinstance(imp, str) and not imp.startswith('linkml:'):
                                    enum_file = level_file.parent / f"{imp}.yaml"
                                    if enum_file.exists():
                                        try:
                                            enum_schema = yaml_loader.load(str(enum_file), SchemaDefinition)
                                            if enum_schema.enums:
                                                level_enums.update(enum_schema.enums)
                                        except:
                                            pass
                        
                        # Find the level class (BulkWESLevel1, BulkWESLevel2, etc.)
                        level_class_name = None
                        for class_name in level_schema.classes.keys():
                            if "Level" in class_name:
                                level_class_name = class_name
                                break
                        
                        if level_class_name:
                            f.write(f"### {level_name} ({level_class_name})\n\n")
                            if level_schema.description:
                                f.write(f"{level_schema.description}\n\n")
                            
                            class_def = level_schema.classes[level_class_name]
                            generate_class_table(level_class_name, class_def, level_enums, f)
                    except Exception as e:
                        print(f"Warning: Could not load {level_file}: {e}")
        
        # Default: show all classes
        else:
            if all_classes:
                f.write("## Classes\n\n")
                for class_name, class_def in sorted(all_classes.items()):
                    f.write(f"### {class_name}\n\n")
                    generate_class_table(class_name, class_def, all_enums, f)
        
        # Enums section (show all enums with many values)
        if all_enums:
            long_enums = []
            for enum_name, enum_def in sorted(all_enums.items()):
                if enum_def.permissible_values and len(enum_def.permissible_values) > 5:
                    long_enums.append((enum_name, enum_def))
            
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
