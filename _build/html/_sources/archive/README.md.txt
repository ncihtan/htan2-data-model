# Archive Directory

This directory contains files that have been moved from the main repository structure but are kept for reference or potential future use.

## Contents

### Files
- **HTAN.jsonld**: Large generated JSON-LD file (legacy)
- **HTAN2Model.yaml**: Legacy schema definition file

### Directories
- **modules/**: Archived LinkML schema modules that are not currently active
  - **Participant/**: Participant data model (moved from `modules/Participant/`)
  - **Sample/**: Sample data model (moved from `modules/Sample/`)
  - **Study/**: Study data model (moved from `modules/Study/`)
  - **Treatment/**: Treatment data model (moved from `modules/Treatment/`)
  - **Tumor/**: Tumor data model (moved from `modules/Tumor/`)
  - **Imaging/**: Imaging data model (moved from `modules/Imaging/`)
  - **Templates/**: Imaging template definitions (moved from `modules/Templates/`)
  - **Worksheets/**: Data collection worksheets (moved from `modules/Worksheets/`)

## Purpose

These files and modules were archived during the project restructuring to:
1. **Reduce repository clutter** in the root directory
2. **Focus development** on the Clinical module as the primary active component
3. **Preserve historical context** and potential future reference
4. **Maintain clean separation** between active and inactive components

## Future Considerations

- These modules may be reactivated as development priorities change
- The archive provides a reference for the broader HTAN data model scope
- When new modules are ready for development, they can be moved back to the main `modules/` directory
