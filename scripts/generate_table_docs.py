#!/usr/bin/env python3
"""
Simplified doc generator using LinkML SchemaView.
~120 lines vs the original 800-line script.
"""
from pathlib import Path
from linkml_runtime import SchemaView

# All modules with their schema paths
MODULES = {
    "Clinical": "modules/Clinical/domains/clinical.yaml",
    "Biospecimen": "modules/Biospecimen/domains/biospecimen.yaml",
    "WES": "modules/WES/domains/wes.yaml",
    "scRNA-seq": "modules/scRNA-seq/domains/scrna_seq.yaml",
    "SpatialOmics": "modules/SpatialOmics/domains/spatial.yaml",
    "MultiplexMicroscopy": "modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml",
    "DigitalPathology": "modules/DigitalPathology/domains/digitalpathology.yaml",
    "Imaging": "modules/Imaging/domains/imaging.yaml",
}

# LinkML built-in classes to exclude from documentation
EXCLUDED_CLASSES = {"AnyValue", "extension", "Extension", "Extensible", "Annotatable"}

def get_conditional_requirements(cls) -> dict:
    """Extract conditional requirements from class rules and slot_usage.
    Returns a dict mapping slot_name -> condition description.
    """
    conditional = {}
    
    # Extract from formal rules
    if hasattr(cls, 'rules') and cls.rules:
        for rule in cls.rules:
            if not rule:
                continue
            # Get the rule description
            rule_desc = getattr(rule, 'description', None) or ""
            
            # Extract which slots are conditionally required from postconditions
            postconditions = getattr(rule, 'postconditions', None)
            if postconditions:
                slot_conditions = getattr(postconditions, 'slot_conditions', None)
                if slot_conditions:
                    for slot_name, slot_cond in slot_conditions.items():
                        if hasattr(slot_cond, 'required') and slot_cond.required:
                            conditional[slot_name] = rule_desc
    
    # Also extract from slot_usage descriptions that contain "Required when"
    if hasattr(cls, 'slot_usage') and cls.slot_usage:
        for slot_name, slot_usage in cls.slot_usage.items():
            if slot_usage and hasattr(slot_usage, 'description') and slot_usage.description:
                desc = slot_usage.description
                # Check if description contains conditional requirement info
                if 'required when' in desc.lower() or 'required if' in desc.lower():
                    conditional[slot_name] = desc
    
    return conditional

def generate_class_table(sv: SchemaView, class_name: str, enum_names: set) -> str:
    """Generate markdown table for a class."""
    # Skip LinkML built-in classes
    if class_name in EXCLUDED_CLASSES:
        return ""
    
    cls = sv.get_class(class_name)
    if not cls or cls.mixin or cls.abstract:
        return ""
    
    # Get conditional requirements from rules
    conditional_reqs = get_conditional_requirements(cls)
    
    lines = [f"## {class_name}\n"]
    if cls.description:
        lines.append(f"**{cls.description}**\n")
    
    lines.append("| Attribute | Type | Required | Description |")
    lines.append("|-----------|------|----------|-------------|")
    
    # Get slot_usage overrides for this class
    slot_usage = {}
    if hasattr(cls, 'slot_usage') and cls.slot_usage:
        slot_usage = cls.slot_usage
    
    for slot_name in sv.class_slots(class_name):
        slot = sv.get_slot(slot_name)
        if slot:
            slot_range = slot.range or "string"
            # Link to enum if the type is an enum
            if slot_range in enum_names:
                type_display = f"[{slot_range}](#{slot_range.lower()})"
            else:
                type_display = slot_range
            
            # Determine required status
            if slot.required:
                required = "Yes"
            elif slot_name in conditional_reqs:
                cond_desc = conditional_reqs[slot_name].replace("|", "\\|")
                required = f"Conditional: {cond_desc}"
            else:
                required = "No"
            
            # Get description - prefer slot_usage override if present
            desc = slot.description or ""
            if slot_name in slot_usage and slot_usage[slot_name]:
                usage = slot_usage[slot_name]
                if hasattr(usage, 'description') and usage.description:
                    desc = usage.description
            desc = desc.replace("\n", " ").replace("|", "\\|")
            
            lines.append(f"| `{slot_name}` | {type_display} | {required} | {desc} |")
    
    return "\n".join(lines) + "\n"

def generate_enum_table(sv: SchemaView, enum_name: str) -> str:
    """Generate markdown table for an enum."""
    enum = sv.get_enum(enum_name)
    if not enum or not enum.permissible_values:
        return ""
    
    lines = [f"### {enum_name}\n"]
    if enum.description:
        lines.append(f"{enum.description}\n")
    
    lines.append("| Value | Description |")
    lines.append("|-------|-------------|")
    
    for pv_name, pv in enum.permissible_values.items():
        desc = (pv.description or "").replace("\n", " ").replace("|", "\\|")
        lines.append(f"| {pv_name} | {desc} |")
    
    return "\n".join(lines) + "\n"

def generate_module_docs(name: str, schema_path: str, output_path: str):
    """Generate docs for a module."""
    sv = SchemaView(schema_path)
    
    # Output filename for CSV link
    csv_name = Path(output_path).stem
    
    lines = [f"# {name}\n"]
    if sv.schema.description:
        lines.append(f"{sv.schema.description}\n")
    
    # CSV download link (only for record-based modules)
    if name in ["Clinical", "Biospecimen", "DigitalPathology"]:
        lines.append(f"📥 [Download attributes as CSV](csv/{csv_name}.csv)\n")
    
    # Get all enum names for linking
    enum_names = set(sv.all_enums())
    
    # Classes
    for class_name in sv.all_classes():
        table = generate_class_table(sv, class_name, enum_names)
        if table:
            lines.append(table)
    
    # Enums
    enums = list(sv.all_enums())
    if enums:
        lines.append("## Enums\n")
        for enum_name in sorted(enums):
            table = generate_enum_table(sv, enum_name)
            if table:
                lines.append(table)
    
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines))
    print(f"✓ {output_path}")

def main():
    base_dir = Path(__file__).parent.parent
    
    # Output filename mapping
    output_names = {
        "Clinical": "clinical",
        "Biospecimen": "biospecimen", 
        "WES": "wes",
        "scRNA-seq": "scrna-seq",
        "SpatialOmics": "spatialomics",
        "MultiplexMicroscopy": "multiplexmicroscopy",
        "DigitalPathology": "digitalpathology",
        "Imaging": "imaging",
    }
    
    print("Generating documentation from LinkML schemas...\n")
    
    for name, schema_path in MODULES.items():
        full_path = base_dir / schema_path
        if full_path.exists():
            output_path = base_dir / "docs" / f"{output_names[name]}.md"
            generate_module_docs(name, str(full_path), str(output_path))
        else:
            print(f"⚠ {name}: schema not found")
    
    print("\nDone!")

if __name__ == "__main__":
    main()
