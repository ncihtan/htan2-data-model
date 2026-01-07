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
                all_attrs.update(parent_attrs)
                inheritance_chain.extend(parent_chain)
                parent_class_defs.update(parent_defs)
            else:
                # Try to load from imported schemas
                # Common parent classes: CoreFileAttributes, BaseSequencingAttributes, BaseImagingAttributes
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
                            all_attrs.update(parent_attrs)
                            inheritance_chain.extend(parent_chain)
                            parent_class_defs.update(parent_defs)
                    except Exception as e:
                        pass
    
    return all_attrs, inheritance_chain, parent_class_defs

def get_conditional_requirements(class_def, attr_name):
    """Extract conditional requirements from slot_usage and rules."""
    conditions = []
    
    # Check slot_usage first (simpler, more direct) - this is the most reliable
    if class_def.slot_usage and attr_name in class_def.slot_usage:
        slot_usage = class_def.slot_usage[attr_name]
        if slot_usage.description:
            desc = slot_usage.description
            # Extract the condition part - handle various formats
            if "Required when" in desc:
                condition = desc.replace("Required when ", "").strip()
                # Make it clearer - use "=" consistently and improve readability
                condition = condition.replace(" is ", " = ")
                # Handle common phrases to make them clearer
                condition = condition.replace(" = any stage value", " has any stage value")
                condition = condition.replace(" = Stage IV or any of its substages", " = Stage IV or any substage")
                condition = condition.replace(" is a surgical or radiation therapy", " contains 'Surgical' or 'Radiation'")
                condition = condition.replace(" = present", " is provided")
                condition = condition.replace(" is present", " is provided")
                # Make "= present" clearer
                if " = present" in condition:
                    condition = condition.replace(" = present", " is provided")
                conditions.append(condition)
            elif "required when" in desc.lower():
                condition = desc.split("required when", 1)[1].strip()
                condition = condition.replace(" is ", " = ")
                condition = condition.replace(" = any stage value", " has any stage value")
                condition = condition.replace(" = Stage IV or any of its substages", " = Stage IV or any substage")
                condition = condition.replace(" is a surgical or radiation therapy", " contains 'Surgical' or 'Radiation'")
                condition = condition.replace(" = present", " is provided")
                condition = condition.replace(" is present", " is provided")
                # Make "= present" clearer
                if " = present" in condition:
                    condition = condition.replace(" = present", " is provided")
                conditions.append(condition)
    
    # Check rules as fallback - but prefer slot_usage if available
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
                                    # Extract patterns and make them readable
                                    patterns = []
                                    for pattern_obj in precond_val.any_of:
                                        if hasattr(pattern_obj, 'pattern'):
                                            pattern = pattern_obj.pattern
                                            # Clean up regex patterns to be more readable
                                            pattern = pattern.replace('.*', '').replace('^', '').replace('$', '')
                                            if pattern and pattern not in patterns:
                                                patterns.append(pattern)
                                    if patterns:
                                        if len(patterns) == 1:
                                            precond_desc.append(f"{precond_attr} matches '{patterns[0]}'")
                                        else:
                                            precond_desc.append(f"{precond_attr} matches one of: {', '.join(patterns)}")
                                elif hasattr(precond_val, 'required') and precond_val.required:
                                    precond_desc.append(f"{precond_attr} is present")
                            if precond_desc:
                                conditions.append(" and ".join(precond_desc))
    
    return conditions

def write_attribute_row(attr_name, attr_def, class_def, all_enums, f):
    """Helper function to write a single attribute row."""
    required = "Yes" if attr_def.required else "No"
    
    # Get conditional requirements
    conditions = get_conditional_requirements(class_def, attr_name)
    if conditions:
        required = f"Required IF {', '.join(conditions)}"
    
    range_str = attr_def.range if attr_def.range else "string"
    
    # Check if range is an enum
    enum_def = None
    if all_enums and range_str in all_enums:
        enum_def = all_enums[range_str]
    
    if enum_def:
        enum_values = format_enum_values(enum_def)
        range_str = enum_values
    
    # Get pattern if exists and add to Type column
    try:
        if hasattr(attr_def, 'pattern') and attr_def.pattern:
            pattern_val = attr_def.pattern
            if pattern_val:
                pattern_val_escaped = pattern_val.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                range_str = f"{range_str}, pattern: <code>{pattern_val_escaped}</code>"
        elif hasattr(attr_def, 'structured_pattern') and attr_def.structured_pattern:
            pattern_val = None
            if hasattr(attr_def.structured_pattern, 'syntax'):
                pattern_val = attr_def.structured_pattern.syntax
            elif isinstance(attr_def.structured_pattern, str):
                pattern_val = attr_def.structured_pattern
            if pattern_val:
                pattern_val_escaped = pattern_val.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                range_str = f"{range_str}, pattern: <code>{pattern_val_escaped}</code>"
    except:
        pass
    
    description = attr_def.description or ""
    description = description.replace("|", "\\|")
    
    f.write(f"| `{attr_name}` | {range_str} | {required} | {description} |\n")

def generate_class_table_with_inheritance(class_name, class_def, all_enums, f, all_classes, base_dir):
    """Generate attributes table for a class with inherited attributes organized by source."""
    if class_def.description:
        f.write(f"**{class_def.description}**\n\n")
    
    # Resolve inheritance chain
    all_attrs, inheritance_chain, parent_class_defs = resolve_inheritance_chain(class_def, all_classes, base_dir)
    
    if not all_attrs:
        return
    
    # Organize attributes by source
    core_attrs = {}
    base_attrs = {}
    module_attrs = {}
    
    # Get current class attributes (module-specific)
    if class_def.attributes:
        module_attrs = class_def.attributes.copy()
    
    # Get parent class attributes
    for parent_name in inheritance_chain:
        if parent_name in parent_class_defs:
            parent_class = parent_class_defs[parent_name]
            if parent_class.attributes:
                if parent_name == 'CoreFileAttributes':
                    core_attrs = parent_class.attributes.copy()
                elif parent_name in ['BaseSequencingAttributes', 'BaseImagingAttributes']:
                    base_attrs = parent_class.attributes.copy()
    
    # Write sections in order: Core File, Base (Sequencing/Imaging), Module-specific
    if core_attrs:
        f.write("### Core File Attributes\n\n")
        f.write("These attributes are inherited from CoreFileAttributes and apply to all file-based data.\n\n")
        f.write("| Attribute | Type | Required | Description |\n")
        f.write("|-----------|------|----------|-------------|\n")
        for attr_name in sorted(core_attrs.keys()):
            write_attribute_row(attr_name, core_attrs[attr_name], parent_class_defs.get('CoreFileAttributes', class_def), all_enums, f)
        f.write("\n")
    
    if base_attrs:
        base_name = 'Base Sequencing Attributes' if 'Sequencing' in str(inheritance_chain) else 'Base Imaging Attributes'
        base_class_name = None
        for parent_name in inheritance_chain:
            if parent_name in ['BaseSequencingAttributes', 'BaseImagingAttributes']:
                base_class_name = parent_name
                break
        if not base_class_name and inheritance_chain:
            base_class_name = inheritance_chain[0] if 'Sequencing' in str(inheritance_chain) or 'Imaging' in str(inheritance_chain) else inheritance_chain[-1]
        f.write(f"### {base_name}\n\n")
        if base_class_name:
            f.write(f"These attributes are inherited from {base_class_name}.\n\n")
        else:
            f.write(f"These attributes are inherited from base classes.\n\n")
        f.write("| Attribute | Type | Required | Description |\n")
        f.write("|-----------|------|----------|-------------|\n")
        for attr_name in sorted(base_attrs.keys()):
            if attr_name not in core_attrs:  # Don't duplicate core attributes
                parent_class = parent_class_defs.get(inheritance_chain[1] if len(inheritance_chain) > 1 else inheritance_chain[0], class_def)
                write_attribute_row(attr_name, base_attrs[attr_name], parent_class, all_enums, f)
        f.write("\n")
    
    if module_attrs:
        f.write("### Module-Specific Attributes\n\n")
        f.write("| Attribute | Type | Required | Description |\n")
        f.write("|-----------|------|----------|-------------|\n")
        for attr_name in sorted(module_attrs.keys()):
            write_attribute_row(attr_name, module_attrs[attr_name], class_def, all_enums, f)
        f.write("\n")

def generate_class_table(class_name, class_def, all_enums, f, is_manifest=False, all_classes=None):
    """Generate attributes table for a class."""
    if class_def.description:
        f.write(f"**{class_def.description}**\n\n")
    
    if class_def.attributes:
        # For manifests, separate identifier/common attributes from class references
        common_attrs = {}
        class_attrs = {}
        
        if is_manifest:
            # Separate identifier/common attributes (like HTAN_PARTICIPANT_ID) from class references
            for attr_name, attr_def in class_def.attributes.items():
                # Check if it's an identifier or a simple type (not a class reference)
                if hasattr(attr_def, 'identifier') and attr_def.identifier:
                    common_attrs[attr_name] = attr_def
                elif attr_def.range and attr_def.range not in all_classes and attr_def.range not in ['Demographics', 'Diagnosis', 'Exposure', 'FamilyHistory', 'FollowUp', 'MolecularTest', 'Therapy', 'VitalStatus']:
                    # It's a simple type, not a class reference
                    common_attrs[attr_name] = attr_def
                else:
                    # It's a class reference
                    class_attrs[attr_name] = attr_def
        else:
            # For other classes, all attributes are class-specific
            class_attrs = class_def.attributes
        
        # Show common attributes section if any
        if common_attrs:
            f.write("### Common Attributes\n\n")
            f.write("| Attribute | Type | Required | Description |\n")
            f.write("|-----------|------|----------|-------------|\n")
            
            for attr_name, attr_def in sorted(common_attrs.items()):
                required = "Yes" if attr_def.required else "No"
                
                # Get conditional requirements
                conditions = get_conditional_requirements(class_def, attr_name)
                if conditions:
                    required = f"Required IF {', '.join(conditions)}"
                
                range_str = attr_def.range if attr_def.range else "string"
                
                # Check if range is an enum
                enum_def = None
                if all_enums and range_str in all_enums:
                    enum_def = all_enums[range_str]
                
                if enum_def:
                    enum_values = format_enum_values(enum_def)
                    range_str = enum_values
                
                # Get pattern if exists and add to Type column
                try:
                    if hasattr(attr_def, 'pattern') and attr_def.pattern:
                        pattern_val = attr_def.pattern
                        if pattern_val:  # Make sure it's not empty
                            # Escape special markdown characters for markdown tables
                            # Use HTML code tags instead of backticks for better table compatibility
                            pattern_val_escaped = pattern_val.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                            range_str = f"{range_str}, pattern: <code>{pattern_val_escaped}</code>"
                    elif hasattr(attr_def, 'structured_pattern') and attr_def.structured_pattern:
                        # Handle structured patterns
                        pattern_val = None
                        if hasattr(attr_def.structured_pattern, 'syntax'):
                            pattern_val = attr_def.structured_pattern.syntax
                        elif isinstance(attr_def.structured_pattern, str):
                            pattern_val = attr_def.structured_pattern
                        if pattern_val:
                            # Escape special markdown characters for markdown tables
                            # Use HTML code tags instead of backticks for better table compatibility
                            pattern_val_escaped = pattern_val.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                            range_str = f"{range_str}, pattern: <code>{pattern_val_escaped}</code>"
                except:
                    pass  # If pattern access fails, just leave it empty
                
                description = attr_def.description or ""
                description = description.replace("|", "\\|")
                
                f.write(f"| `{attr_name}` | {range_str} | {required} | {description} |\n")
            f.write("\n")
        
        # Show class-specific attributes
        if class_attrs:
            if common_attrs:
                f.write("### Class References\n\n")
            
            f.write("| Attribute | Type | Required | Description |\n")
            f.write("|-----------|------|----------|-------------|\n")
            
            for attr_name, attr_def in sorted(class_attrs.items()):
                # Get base required status
                required = "Yes" if attr_def.required else "No"
                
                # Get conditional requirements
                conditions = get_conditional_requirements(class_def, attr_name)
                if conditions:
                    required = f"Required IF {', '.join(conditions)}"
                
                range_str = attr_def.range if attr_def.range else "string"
                
                # Check if range is an enum
                enum_def = None
                if all_enums and range_str in all_enums:
                    enum_def = all_enums[range_str]
                
                if enum_def:
                    enum_values = format_enum_values(enum_def)
                    range_str = enum_values
                
                # Get pattern if exists and add to Type column
                try:
                    if hasattr(attr_def, 'pattern') and attr_def.pattern:
                        pattern_val = attr_def.pattern
                        if pattern_val:  # Make sure it's not empty
                            # Escape special markdown characters for markdown tables
                            # Use HTML code tags instead of backticks for better table compatibility
                            pattern_val_escaped = pattern_val.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                            range_str = f"{range_str}, pattern: <code>{pattern_val_escaped}</code>"
                    elif hasattr(attr_def, 'structured_pattern') and attr_def.structured_pattern:
                        # Handle structured patterns
                        pattern_val = None
                        if hasattr(attr_def.structured_pattern, 'syntax'):
                            pattern_val = attr_def.structured_pattern.syntax
                        elif isinstance(attr_def.structured_pattern, str):
                            pattern_val = attr_def.structured_pattern
                        if pattern_val:
                            # Escape special markdown characters for markdown tables
                            # Use HTML code tags instead of backticks for better table compatibility
                            pattern_val_escaped = pattern_val.replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
                            range_str = f"{range_str}, pattern: <code>{pattern_val_escaped}</code>"
                except:
                    pass  # If pattern access fails, just leave it empty
                
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
    
    # Store all_classes in a way that generate_class_table can access it
    # We'll pass it as a parameter
    
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
                generate_class_table("ClinicalData", all_classes["ClinicalData"], all_enums, f, is_manifest=True, all_classes=all_classes)
            
            # Then show all other classes
            for class_name, class_def in sorted(all_classes.items()):
                if class_name != "ClinicalData":
                    f.write(f"### {class_name}\n\n")
                    generate_class_table(class_name, class_def, all_enums, f, is_manifest=False, all_classes=all_classes)
        
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
                            # Merge level_enums with all_enums for complete enum lookup
                            combined_enums = {**all_enums, **level_enums}
                            # Merge level classes with all_classes for inheritance resolution
                            combined_classes = {**all_classes}
                            if level_schema.classes:
                                combined_classes.update(level_schema.classes)
                            generate_class_table_with_inheritance(level_class_name, class_def, combined_enums, f, combined_classes, base_dir)
                    except Exception as e:
                        print(f"Warning: Could not load {level_file}: {e}")
        
        # Default: show all classes (for file-based modules, use inheritance)
        else:
            if all_classes:
                f.write("## Classes\n\n")
                for class_name, class_def in sorted(all_classes.items()):
                    f.write(f"### {class_name}\n\n")
                    # Use inheritance for file-based modules (not Clinical or Biospecimen)
                    if schema.name not in ["Clinical", "Biospecimen"]:
                        generate_class_table_with_inheritance(class_name, class_def, all_enums, f, all_classes, base_dir)
                    else:
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
