# HTAN Clinical Module

This module contains the clinical data model and related components for the HTAN project.

## Architecture

The Clinical module uses a clean inheritance chain:

```
ClinicalData → ParticipantAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: Gets universal file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes`
- **Participant Attributes**: Gets required `HTAN_PARTICIPANT_ID` from `ParticipantAttributes`
- **Clinical-Specific Attributes**: Adds clinical domain-specific attributes
- **No Duplication**: Common attributes are defined once in the base modules

## Directory Structure

- `domains/` - Contains domain-specific YAML schema definitions for clinical data
  - Each YAML file represents a specific clinical domain (e.g., diagnosis, therapy)
  - These files define the structure and validation rules for each domain

- `src/htan_clinical/` - Contains the Python implementation of the clinical data model
  - `datamodel/` - Contains the generated Python classes for the data model
  - `schema/` - Contains the main schema definition that combines all domains

- `tests/` - Contains unit tests for the clinical module
  - Tests are organized by domain and functionality
  - Includes test data and validation tests

## Schema Organization

- `domains/` contains the source of truth for each clinical domain
- `src/htan_clinical/schema/` contains the combined schema that includes all domains
- Generated files are stored in `project/` and should not be committed to version control

## Testing

Tests are organized by domain and functionality:
- `test_conditional_requirements.py` - Tests for conditional validation rules
- `test_clinical.py` - General clinical data model tests

## Development

1. Update domain YAML files in `domains/`
2. Run `make gen-project` to regenerate schema classes
3. Run tests to verify changes
4. Commit only source files, not generated files 