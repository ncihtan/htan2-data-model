#!/usr/bin/env python3
"""
Generate CSV files from LinkML schemas for each module and level.
Each CSV contains all attributes with their types, requirements, patterns, and descriptions.
"""
import csv
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

def resolve_inheritance_chain(class_def, all_classes, base_dir, visited=None):
    """Resolve inheritance chain and collect all attributes from parent classes.
    Returns: (all_attributes_dict, inheritance_chain_list, parent_class_defs_dict)
    """
    if visited is None:
        visited = set()
    
    all_attrs = {}
    inheritance_chain = []
    parent_class_defs = {}
    
    # Get attributes from current class
    if class_def.attributes:
        all_attrs.update(class_def.attributes)
    
    # Follow inheritance chain
    if hasattr(class_def, 'is_a') and class_def.is_a:
        parent_name = class_def.is_a
        if parent_name not in visited:
            visited.add(parent_name)
            
            # Try to find parent in all_classes
            if parent_name in all_classes:
                parent_class = all_classes[parent_name]
                inheritance_chain.append(parent_name)
                parent_class_defs[parent_name] = parent_class
                # Recursively get parent attributes
                parent_attrs, parent_chain, parent_defs = resolve_inheritance_chain(parent_class, all_classes, base_dir, visited)
                # Only add parent attributes that don't exist in child (child attributes take precedence)
                for attr_name, attr_def in parent_attrs.items():
                    if attr_name not in all_attrs:
                        all_attrs[attr_name] = attr_def
                inheritance_chain.extend(parent_chain)
                parent_class_defs.update(parent_defs)
            else:
                # Try to load from imported schemas
                parent_schemas = {
                    'CoreFileAttributes': base_dir.parent.parent / 'CoreFile' / 'domains' / 'core.yaml',
                    'BaseSequencingAttributes': base_dir.parent.parent / 'Sequencing' / 'domains' / 'sequencing.yaml',
                    'BaseImagingAttributes': base_dir.parent.parent / 'Imaging' / 'domains' / 'imaging.yaml',
                }
                
                if parent_name in parent_schemas and parent_schemas[parent_name].exists():
                    try:
                        parent_schema = yaml_loader.load(str(parent_schemas[parent_name]), SchemaDefinition)
                        if parent_name in parent_schema.classes:
                            parent_class = parent_schema.classes[parent_name]
                            inheritance_chain.append(parent_name)
                            parent_class_defs[parent_name] = parent_class
                            parent_attrs, parent_chain, parent_defs = resolve_inheritance_chain(parent_class, parent_schema.classes, base_dir, visited)
                            # Only add parent attributes that don't exist in child (child attributes take precedence)
                            for attr_name, attr_def in parent_attrs.items():
                                if attr_name not in all_attrs:
                                    all_attrs[attr_name] = attr_def
                            inheritance_chain.extend(parent_chain)
                            parent_class_defs.update(parent_defs)
                    except Exception as e:
                        pass
    
    return all_attrs, inheritance_chain, parent_class_defs

def get_conditional_requirements(class_def, attr_name):
    """Extract conditional requirements from slot_usage and rules."""
    conditions = []
    
    if class_def.slot_usage and attr_name in class_def.slot_usage:
        slot_usage = class_def.slot_usage[attr_name]
        if slot_usage.description:
            desc = slot_usage.description
            if "required if" in desc.lower() or "required when" in desc.lower():
                conditions.append(desc)
    
    if class_def.rules:
        for rule in class_def.rules:
            if hasattr(rule, 'preconditions') and rule.preconditions:
                for precond in rule.preconditions:
                    if hasattr(precond, 'slot_conditions'):
                        for slot_name, slot_cond in precond.slot_conditions.items():
                            if slot_name == attr_name:
                                if hasattr(slot_cond, 'equals_string'):
                                    conditions.append(f"Required IF {slot_name} = {slot_cond.equals_string}")
                                elif hasattr(slot_cond, 'equals_expression'):
                                    conditions.append(f"Required IF {slot_name} = {slot_cond.equals_expression}")
    
    return "; ".join(conditions) if conditions else ""

def get_attribute_info(attr_name, attr_def, class_def, all_enums):
    """Extract attribute information for CSV row."""
    # Get type/range
    range_str = "string"
    if attr_def.range:
        if attr_def.range in all_enums:
            range_str = all_enums[attr_def.range].name
        else:
            range_str = attr_def.range
    
    # Get pattern
    pattern = ""
    try:
        if hasattr(attr_def, 'pattern') and attr_def.pattern:
            pattern = attr_def.pattern
        elif hasattr(attr_def, 'structured_pattern') and attr_def.structured_pattern:
            if hasattr(attr_def.structured_pattern, 'syntax'):
                pattern = attr_def.structured_pattern.syntax
            elif isinstance(attr_def.structured_pattern, str):
                pattern = attr_def.structured_pattern
    except:
        pass
    
    # Get required status
    required = "No"
    if hasattr(attr_def, 'required') and attr_def.required:
        required = "Yes"
    elif hasattr(attr_def, 'minimum_cardinality') and attr_def.minimum_cardinality and attr_def.minimum_cardinality > 0:
        required = "Yes"
    
    # Get conditional requirements
    conditional = get_conditional_requirements(class_def, attr_name)
    if conditional:
        required = f"Conditional: {conditional}"
    
    # Get description
    description = attr_def.description or ""
    
    return {
        'Attribute': attr_name,
        'Type': range_str,
        'Pattern': pattern,
        'Required': required,
        'Description': description
    }

def generate_csv_for_class(class_name, class_def, all_enums, all_classes, base_dir, output_path):
    """Generate CSV file for a class with all attributes (including inherited)."""
    # Resolve inheritance chain
    all_attrs, inheritance_chain, parent_class_defs = resolve_inheritance_chain(class_def, all_classes, base_dir)
    
    if not all_attrs:
        return
    
    # Write CSV
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Attribute', 'Type', 'Pattern', 'Required', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Write attributes sorted by name
        for attr_name in sorted(all_attrs.keys()):
            attr_def = all_attrs[attr_name]
            # Use the class_def that actually defines this attribute (could be parent)
            attr_class_def = class_def
            for parent_name in inheritance_chain:
                if parent_name in parent_class_defs:
                    parent_class = parent_class_defs[parent_name]
                    if parent_class.attributes and attr_name in parent_class.attributes:
                        attr_class_def = parent_class
                        break
            
            row = get_attribute_info(attr_name, attr_def, attr_class_def, all_enums)
            writer.writerow(row)
    
    print(f"Generated CSV: {output_path}")

def generate_level_csv(level_file, level_name, module_name, module_output_name, all_enums, all_classes, base_dir):
    """Generate CSV for a specific level."""
    csv_dir = base_dir / "docs" / "csv"
    csv_dir.mkdir(exist_ok=True)
    
    # Create filename from level name
    level_filename = level_name.lower().replace(" ", "-").replace("/", "-")
    output_path = csv_dir / f"{module_output_name}-{level_filename}.csv"
    
    try:
        level_schema = yaml_loader.load(str(level_file), SchemaDefinition)
        level_enums = {}
        if level_schema.enums:
            level_enums.update(level_schema.enums)
        
        # Load classes and enums from imported schemas
        combined_classes = {**all_classes}
        if level_schema.classes:
            combined_classes.update(level_schema.classes)
        
        # Load imported schemas recursively
        schemas_to_load = []
        if level_schema.imports:
            for imp in level_schema.imports:
                if isinstance(imp, str) and not imp.startswith('linkml:'):
                    import_file = level_file.parent / f"{imp}.yaml"
                    if import_file.exists():
                        schemas_to_load.append(import_file)
        
        loaded_schemas = set()
        while schemas_to_load:
            schema_file = schemas_to_load.pop(0)
            if str(schema_file) in loaded_schemas:
                continue
            loaded_schemas.add(str(schema_file))
            
            try:
                import_schema = yaml_loader.load(str(schema_file), SchemaDefinition)
                if import_schema.enums:
                    level_enums.update(import_schema.enums)
                if import_schema.classes:
                    combined_classes.update(import_schema.classes)
                
                if import_schema.imports:
                    for sub_imp in import_schema.imports:
                        if isinstance(sub_imp, str) and not sub_imp.startswith('linkml:'):
                            sub_import_file = schema_file.parent / f"{sub_imp}.yaml"
                            if sub_import_file.exists() and str(sub_import_file) not in loaded_schemas:
                                schemas_to_load.append(sub_import_file)
            except Exception as e:
                pass
        
        # Find the level class
        level_class_name = None
        for class_name in level_schema.classes.keys():
            if "Level" in class_name or "Panel" in class_name:
                level_class_name = class_name
                break
        
        if level_class_name:
            class_def = level_schema.classes[level_class_name]
            combined_enums = {**all_enums, **level_enums}
            generate_csv_for_class(level_class_name, class_def, combined_enums, combined_classes, base_dir, output_path)
    except Exception as e:
        print(f"Warning: Could not generate CSV for level {level_file}: {e}")

def generate_module_csv(schema_path: str, module_name: str, output_map: dict, base_dir: Path):
    """Generate CSV files for a module."""
    schema = yaml_loader.load(str(schema_path), SchemaDefinition)
    
    all_enums = {}
    all_classes = {}
    
    if schema.enums:
        all_enums.update(schema.enums)
    if schema.classes:
        all_classes.update(schema.classes)
    
    # Load imported schemas
    if schema.imports:
        for imp in schema.imports:
            if isinstance(imp, str) and not imp.startswith('linkml:'):
                import_file = Path(schema_path).parent / f"{imp}.yaml"
                if import_file.exists():
                    try:
                        import_schema = yaml_loader.load(str(import_file), SchemaDefinition)
                        if import_schema.enums:
                            all_enums.update(import_schema.enums)
                        if import_schema.classes:
                            all_classes.update(import_schema.classes)
                    except Exception as e:
                        pass
    
    csv_dir = base_dir / "docs" / "csv"
    csv_dir.mkdir(exist_ok=True)
    
    # For record-based modules (Clinical, Biospecimen), generate CSV with all attributes
    if module_name == "Clinical":
        # For Clinical, include all attributes from all classes (not just ClinicalData manifest)
        output_path = csv_dir / f"{output_map[module_name]}.csv"
        with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Attribute', 'Type', 'Pattern', 'Required', 'Description', 'Class']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Write attributes from all classes
            for class_name in sorted(all_classes.keys()):
                class_def = all_classes[class_name]
                if class_def.attributes:
                    for attr_name in sorted(class_def.attributes.keys()):
                        attr_def = class_def.attributes[attr_name]
                        row = get_attribute_info(attr_name, attr_def, class_def, all_enums)
                        row['Class'] = class_name
                        writer.writerow(row)
        
        print(f"Generated CSV: {output_path}")
    
    elif module_name == "Biospecimen":
        # For Biospecimen, include all attributes from BiospecimenData
        if "BiospecimenData" in all_classes:
            output_path = csv_dir / f"{output_map[module_name]}.csv"
            generate_csv_for_class("BiospecimenData", all_classes["BiospecimenData"], all_enums, all_classes, Path(schema_path).parent, output_path)
    
    # For file-based modules with levels, generate CSV for each level
    elif module_name == "WES":
        level_files = {
            "Level 1": Path(schema_path).parent / "level_1.yaml",
            "Level 2": Path(schema_path).parent / "level_2.yaml",
            "Level 3": Path(schema_path).parent / "level_3.yaml",
        }
        for level_name, level_file in level_files.items():
            if level_file.exists():
                generate_level_csv(level_file, level_name, module_name, output_map[module_name], all_enums, all_classes, base_dir)
    
    elif module_name == "scRNA-seq":
        level_files = {
            "Level 1": Path(schema_path).parent / "level_1.yaml",
            "Level 2": Path(schema_path).parent / "level_2.yaml",
            "Level 3/4": Path(schema_path).parent / "level_3_4.yaml",
        }
        for level_name, level_file in level_files.items():
            if level_file.exists():
                generate_level_csv(level_file, level_name, module_name, output_map[module_name], all_enums, all_classes, base_dir)
    
    elif module_name == "MultiplexMicroscopy":
        level_files = {
            "Level 2": Path(schema_path).parent / "level_2.yaml",
            "Level 3": Path(schema_path).parent / "level_3.yaml",
            "Level 4": Path(schema_path).parent / "level_4.yaml",
        }
        for level_name, level_file in level_files.items():
            if level_file.exists():
                generate_level_csv(level_file, level_name, module_name, output_map[module_name], all_enums, all_classes, base_dir)
    
    elif module_name == "SpatialOmics":
        level_files = {
            "Level 1": Path(schema_path).parent / "level_1.yaml",
            "Level 3": Path(schema_path).parent / "level_3.yaml",
            "Level 4": Path(schema_path).parent / "level_4.yaml",
            "Panel": Path(schema_path).parent / "spatial_panel.yaml",
        }
        for level_name, level_file in level_files.items():
            if level_file.exists():
                generate_level_csv(level_file, level_name, module_name, output_map[module_name], all_enums, all_classes, base_dir)
    
    # For DigitalPathology (single level, but file-based)
    elif module_name == "DigitalPathology":
        if "DigitalPathologyData" in all_classes:
            output_path = csv_dir / f"{output_map[module_name]}.csv"
            generate_csv_for_class("DigitalPathologyData", all_classes["DigitalPathologyData"], all_enums, all_classes, Path(schema_path).parent, output_path)

def main():
    base_dir = Path(__file__).parent.parent
    os.chdir(base_dir)
    
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
    
    for module_name, schema_path in MODULES.items():
        full_path = base_dir / schema_path
        if not full_path.exists():
            print(f"Warning: {full_path} not found")
            continue
        
        print(f"Processing {module_name}...")
        try:
            generate_module_csv(str(full_path), module_name, output_map, base_dir)
        except Exception as e:
            print(f"Error processing {module_name}: {e}")
    
    print("\nCSV generation complete!")

if __name__ == "__main__":
    main()

