#!/usr/bin/env python3
"""
Simplified doc generator using LinkML SchemaView.
~120 lines vs the original 800-line script.
"""
import re
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
    "DigitalPathology": "modules/DigitalPathology/domains/digital_pathology.yaml",
    "Imaging": "modules/Imaging/domains/imaging.yaml",
}

# LinkML built-in classes and container classes to exclude from documentation
EXCLUDED_CLASSES = {
    "AnyValue",
    "extension",
    "Extension",
    "Extensible",
    "Annotatable",
    "ClinicalData",
    "WESData",
    "scRNAseqData",
    "SpatialData",
}


def get_conditional_requirements(cls) -> dict:
    """Extract conditional requirements from class rules and slot_usage.
    Returns a dict mapping slot_name -> condition description.
    """
    conditional = {}

    # Extract from formal rules
    if hasattr(cls, "rules") and cls.rules:
        for rule in cls.rules:
            if not rule:
                continue
            # Get the rule description
            rule_desc = getattr(rule, "description", None) or ""

            # Extract which slots are conditionally required from postconditions
            postconditions = getattr(rule, "postconditions", None)
            if postconditions:
                slot_conditions = getattr(postconditions, "slot_conditions", None)
                if slot_conditions:
                    for slot_name, slot_cond in slot_conditions.items():
                        if hasattr(slot_cond, "required") and slot_cond.required:
                            conditional[slot_name] = rule_desc

    # Also extract from slot_usage descriptions that contain "Required when"
    if hasattr(cls, "slot_usage") and cls.slot_usage:
        for slot_name, slot_usage in cls.slot_usage.items():
            if (
                slot_usage
                and hasattr(slot_usage, "description")
                and slot_usage.description
            ):
                desc = slot_usage.description
                # Check if description contains conditional requirement info
                if "required when" in desc.lower() or "required if" in desc.lower():
                    conditional[slot_name] = desc

    return conditional


def generate_class_table(sv: SchemaView, class_name: str, enum_names: set) -> str:
    """Generate markdown table for a class."""
    if class_name in EXCLUDED_CLASSES:
        return ""

    cls = sv.get_class(class_name)
    if not cls or cls.mixin or cls.abstract:
        return ""

    conditional_reqs = get_conditional_requirements(cls)

    lines = [f"## {class_name}\n"]
    if cls.description:
        lines.append(f"**{cls.description}**\n")

    lines.append("| Attribute | Type | Required | Description |")
    lines.append("|-----------|------|----------|-------------|")

    for slot_name in sv.class_slots(class_name):
        # Use induced_slot to get the slot with all class-specific overrides applied
        slot = sv.induced_slot(slot_name, class_name)
        if slot:
            slot_range = slot.range or "string"
            # Link to enum if the type is an enum.
            # Match Python-Markdown toc slugify: lowercase, keep word chars/spaces/-,
            # replace spaces with -.  Underscores are preserved (word chars).
            if slot_range in enum_names:
                slug = re.sub(r"[^\w\s-]", "", slot_range.lower()).strip().replace(
                    " ", "-"
                )
                type_display = f"[{slot_range}](enums.md#{slug})"
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

            desc = (slot.description or "").replace("\n", " ").replace("|", "\\|")
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


def _inheritance_level(sv: SchemaView, class_name: str) -> str | None:
    """Return a short level label (e.g. 'Level 1') from the class name or is_a chain."""
    m = re.search(r"[Ll]evel\s*(\d)", class_name)
    if m:
        return f"Level {m.group(1)}"
    cls = sv.get_class(class_name)
    if cls and cls.is_a:
        return _inheritance_level(sv, cls.is_a)
    return None


def generate_class_overview_table(sv: SchemaView) -> str:
    """Generate a class overview table for all concrete classes in the schema."""
    rows = []
    for class_name in sorted(sv.all_classes()):
        if class_name in EXCLUDED_CLASSES:
            continue
        cls = sv.get_class(class_name)
        if not cls or cls.mixin or cls.abstract:
            continue

        desc = (cls.description or "").replace("\n", " ")
        if len(desc) > 120:
            desc = desc[:117] + "..."

        level = _inheritance_level(sv, class_name)
        level_str = level if level else "—"
        anchor = class_name.lower()
        rows.append(f"| [{class_name}](#{anchor}) | {level_str} | {desc} |")

    if not rows:
        return ""

    lines = [
        "## Classes in This Module\n",
        "| Class | Level | Description |",
        "|-------|-------|-------------|",
    ] + rows
    return "\n".join(lines) + "\n"


def generate_module_docs(name: str, schema_path: str, output_path: str):
    """Generate docs for a module."""
    sv = SchemaView(schema_path)

    lines = [f"# {name}\n"]
    if sv.schema.description:
        lines.append(f"{sv.schema.description}\n")

    # Class overview table
    overview = generate_class_overview_table(sv)
    if overview:
        lines.append(overview)

    enum_names = set(sv.all_enums())

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


def generate_enums_page(base_dir: Path, output_path: str):
    """Generate a combined vocabulary/enums page across all modules."""
    lines = [
        "# Vocabulary (Enums)\n",
        "All controlled vocabulary terms used across HTAN modules. "
        "Use your browser's search (`Ctrl+F` / `⌘F`) or the site search "
        "to find a specific value.\n",
    ]

    for name, schema_path in MODULES.items():
        full_path = base_dir / schema_path
        if not full_path.exists():
            continue
        sv = SchemaView(str(full_path))
        enums = sorted(sv.all_enums())
        if not enums:
            continue

        lines.append(f"## {name}\n")
        for enum_name in enums:
            table = generate_enum_table(sv, enum_name)
            if table:
                lines.append(table)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines))
    print(f"✓ {output_path}")


def generate_slots_index(base_dir: Path, output_path: str):
    """Generate a cross-module slot index page."""
    # slot_name -> {"range", "description", "modules": set, "required": bool}
    slot_data: dict[str, dict] = {}

    for module_name, schema_path in MODULES.items():
        full_path = base_dir / schema_path
        if not full_path.exists():
            continue
        sv = SchemaView(str(full_path))
        for slot_name, slot in sv.all_slots().items():
            if slot_name not in slot_data:
                slot_data[slot_name] = {
                    "range": slot.range or "string",
                    "description": (slot.description or "")
                    .replace("\n", " ")
                    .replace("|", "\\|"),
                    "modules": set(),
                    "required": bool(slot.required),
                }
            slot_data[slot_name]["modules"].add(module_name)

    lines = [
        "# Slot Index\n",
        "Every metadata field defined across all HTAN modules, sorted alphabetically. "
        "Fields shared between modules are listed once with all modules noted.\n",
        "| Slot | Module(s) | Type | Required | Description |",
        "|------|-----------|------|----------|-------------|",
    ]

    for slot_name in sorted(slot_data.keys()):
        d = slot_data[slot_name]
        modules_str = ", ".join(sorted(d["modules"]))
        required = "Yes" if d["required"] else "No"
        desc = d["description"]
        if len(desc) > 150:
            desc = desc[:147] + "..."
        lines.append(
            f"| `{slot_name}` | {modules_str} | {d['range']} | {required} | {desc} |"
        )

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text("\n".join(lines) + "\n")
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

    generate_enums_page(base_dir, str(base_dir / "docs" / "enums.md"))
    generate_slots_index(base_dir, str(base_dir / "docs" / "slots.md"))

    print("\nDone!")


if __name__ == "__main__":
    main()
