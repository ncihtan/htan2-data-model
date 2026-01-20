#!/usr/bin/env python3
"""
Generate identifier documentation page listing all HTAN identifiers and their patterns.
"""
import os
from pathlib import Path
from linkml_runtime.linkml_model.meta import SchemaDefinition
from linkml_runtime.loaders import yaml_loader

def find_identifiers():
    """Find all identifier fields and their patterns across all modules."""
    base_dir = Path(__file__).parent.parent
    
    identifiers = []
    
    # Clinical - HTAN_PARTICIPANT_ID
    clinical_file = base_dir / "modules" / "Clinical" / "domains" / "clinical.yaml"
    if clinical_file.exists():
        schema = yaml_loader.load(str(clinical_file), SchemaDefinition)
        if "ClinicalData" in schema.classes:
            class_def = schema.classes["ClinicalData"]
            if class_def.attributes and "HTAN_PARTICIPANT_ID" in class_def.attributes:
                attr = class_def.attributes["HTAN_PARTICIPANT_ID"]
                if hasattr(attr, 'pattern') and attr.pattern:
                    identifiers.append({
                        'name': 'HTAN_PARTICIPANT_ID',
                        'module': 'Clinical',
                        'pattern': attr.pattern,
                        'description': attr.description or 'HTAN Participant ID (Primary Key)',
                        'required': attr.required
                    })
    
    # Biospecimen - HTAN_BIOSPECIMEN_ID
    biospecimen_file = base_dir / "modules" / "Biospecimen" / "domains" / "biospecimen.yaml"
    if biospecimen_file.exists():
        schema = yaml_loader.load(str(biospecimen_file), SchemaDefinition)
        if "BiospecimenData" in schema.classes:
            class_def = schema.classes["BiospecimenData"]
            if class_def.attributes and "HTAN_BIOSPECIMEN_ID" in class_def.attributes:
                attr = class_def.attributes["HTAN_BIOSPECIMEN_ID"]
                if hasattr(attr, 'pattern') and attr.pattern:
                    identifiers.append({
                        'name': 'HTAN_BIOSPECIMEN_ID',
                        'module': 'Biospecimen',
                        'pattern': attr.pattern,
                        'description': attr.description or 'HTAN Biospecimen ID (Primary Key)',
                        'required': attr.required
                    })
            if class_def.attributes and "HTAN_PARENT_ID" in class_def.attributes:
                attr = class_def.attributes["HTAN_PARENT_ID"]
                if hasattr(attr, 'pattern') and attr.pattern:
                    identifiers.append({
                        'name': 'HTAN_PARENT_ID (Biospecimen)',
                        'module': 'Biospecimen',
                        'pattern': attr.pattern,
                        'description': attr.description or 'HTAN Parent ID',
                        'required': attr.required
                    })
    
    # CoreFile - HTAN_DATA_FILE_ID, HTAN_PARENT_ID
    core_file = base_dir / "modules" / "CoreFile" / "domains" / "core.yaml"
    if core_file.exists():
        schema = yaml_loader.load(str(core_file), SchemaDefinition)
        if "CoreFileAttributes" in schema.classes:
            class_def = schema.classes["CoreFileAttributes"]
            if class_def.attributes:
                for attr_name in ["HTAN_DATA_FILE_ID", "HTAN_PARENT_ID"]:
                    if attr_name in class_def.attributes:
                        attr = class_def.attributes[attr_name]
                        if hasattr(attr, 'pattern') and attr.pattern:
                            identifiers.append({
                                'name': attr_name,
                                'module': 'CoreFile (all file-based modules)',
                                'pattern': attr.pattern,
                                'description': attr.description or f'{attr_name}',
                                'required': attr.required
                            })
    
    # SpatialOmics - HTAN_PANEL_ID
    spatial_panel_file = base_dir / "modules" / "SpatialOmics" / "domains" / "spatial_panel.yaml"
    if spatial_panel_file.exists():
        schema = yaml_loader.load(str(spatial_panel_file), SchemaDefinition)
        if "SpatialPanel" in schema.classes:
            class_def = schema.classes["SpatialPanel"]
            if class_def.attributes and "HTAN_PANEL_ID" in class_def.attributes:
                attr = class_def.attributes["HTAN_PANEL_ID"]
                if hasattr(attr, 'pattern') and attr.pattern:
                    identifiers.append({
                        'name': 'HTAN_PANEL_ID',
                        'module': 'SpatialOmics',
                        'pattern': attr.pattern,
                        'description': attr.description or 'HTAN Panel ID',
                        'required': attr.required
                    })
    
    return identifiers

def generate_identifier_doc():
    """Generate the identifier documentation page."""
    base_dir = Path(__file__).parent.parent
    identifiers = find_identifiers()
    
    output_path = base_dir / "docs" / "identifiers.md"
    
    with open(output_path, 'w') as f:
        f.write("# HTAN Identifiers\n\n")
        f.write("This page lists all HTAN identifier fields and their validation patterns.\n\n")
        f.write("## Identifier Patterns\n\n")
        f.write("| Identifier | Module | Pattern | Required | Description |\n")
        f.write("|------------|--------|---------|----------|-------------|\n")
        
        for ident in identifiers:
            # Escape pipe characters in pattern
            pattern_escaped = ident['pattern'].replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
            required = "Yes" if ident['required'] else "No"
            description = ident['description'].replace("|", "\\|")
            
            f.write(f"| `{ident['name']}` | {ident['module']} | <code>{pattern_escaped}</code> | {required} | {description} |\n")
        
        f.write("\n")
        f.write("## Notes\n\n")
        f.write("- All HTAN identifiers support Phase 2 center IDs (HTA200-229)\n")
        f.write("- Total identifier length is limited to 50 characters\n")
        f.write("- Patterns use regular expression syntax\n")
        f.write("- File-based modules inherit `HTAN_DATA_FILE_ID` and `HTAN_PARENT_ID` from CoreFileAttributes\n")

if __name__ == "__main__":
    generate_identifier_doc()
    print("Generated docs/identifiers.md")

