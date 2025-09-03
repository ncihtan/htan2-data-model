# HTAN WES Module

This module contains the Whole Exome Sequencing (WES) data model and related components for the HTAN project.

## Directory Structure

- `domains/` - Contains domain-specific YAML schema definitions for WES data
  - `level_1.yaml` - Level 1 WES data (raw files)
  - `level_2.yaml` - Level 2 WES data (aligned files and QC)
  - `level_3.yaml` - Level 3 WES data (called variants)
  - `wes.yaml` - Main schema that combines all levels

- `src/htan_wes/` - Contains the Python implementation of the WES data model
  - `datamodel/` - Contains the generated Python classes for the data model
  - `schema/` - Contains the main schema definition that combines all domains

- `tests/` - Contains unit tests for the WES module
  - Tests are organized by level and functionality
  - Includes test data and validation tests

## Testing

The WES module includes comprehensive tests to ensure schema integrity and data model correctness:

### Schema Loading Tests
- **`test_schema_loading`**: Validates that the main WES schema (`wes.yaml`) can be loaded without errors
- Ensures the schema is syntactically correct and all imports resolve properly

### Level-Specific Schema Tests
- **`test_level_1_schema`**: Validates Level 1 schema structure
  - Confirms `BulkWESLevel1` class exists and inherits from `BaseSequencingAttributes`
  - Verifies WES-specific required attributes: `LIBRARY_SELECTION_METHOD`, `READ_LENGTH`
  - Gets core file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes` via inheritance
  - Gets base sequencing attributes (LIBRARY_LAYOUT, SEQUENCING_PLATFORM, etc.) from `BaseSequencingAttributes`

- **`test_level_2_schema`**: Validates Level 2 schema structure
  - Confirms `BulkWESLevel2` class exists and inherits from `BaseSequencingAttributes`
  - Verifies WES-specific required attributes: `ALIGNMENT_WORKFLOW_TYPE`, `MEAN_COVERAGE`
  - Gets core file attributes and base sequencing attributes from inheritance chain

- **`test_level_3_schema`**: Validates Level 3 schema structure
  - Confirms `BulkWESLevel3` class exists and inherits from `BaseSequencingAttributes`
  - Verifies WES-specific required attributes: `SOMATIC_VARIANTS_WORKFLOW_TYPE`
  - Gets core file attributes and base sequencing attributes from inheritance chain

### Enum Validation Tests
- **`test_enums`**: Validates that all enums are properly defined in their respective level files
  - **Level 1 enums**: `LibrarySelectionMethodEnum` (base enums come from BaseSequencingAttributes)
  - **Level 2 enums**: None (base enums come from BaseSequencingAttributes)
  - **Level 3 enums**: `SomaticVariantsSampleTypeEnum`, `MSIStatusEnum`

### Test Coverage
These tests ensure:
- Schema files are valid LinkML YAML
- All required attributes are present in each level
- Enums are correctly defined and accessible
- Import relationships work correctly
- Generated Python classes will have the expected structure

## Architecture

The WES module uses a clean inheritance chain:

```
WES classes → BaseSequencingAttributes → BiospecimenAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: All WES classes get universal file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes`
- **Biospecimen Attributes**: All WES classes get required `HTAN_BIOSPECIMEN_ID` from `BiospecimenAttributes`
- **Base Sequencing Attributes**: All WES classes get common sequencing attributes (LIBRARY_LAYOUT, SEQUENCING_PLATFORM, etc.) from `BaseSequencingAttributes`
- **WES-Specific Attributes**: Each level adds its own WES-specific attributes
- **No Duplication**: Common attributes are defined once in the base modules

## Schema Organization

The WES module follows the HTAN data model structure with three levels:

### Level 1 - Raw Files
Contains metadata for raw sequencing files including:
- Library preparation information
- Sequencing platform details
- File format and naming conventions
- Quality control parameters

### Level 2 - Aligned Files and QC
Contains metadata for aligned files and quality control metrics including:
- Alignment workflow information
- Coverage statistics
- Quality metrics (GC content, duplication rates, etc.)
- MSI (Microsatellite Instability) analysis

### Level 3 - Called Variants
Contains metadata for variant calling results including:
- Genomic reference information
- Workflow details for germline, somatic, and structural variants
- Sample type classification

## Development

1. Update domain YAML files in `domains/`
2. Run `make gen-schema` to regenerate schema classes
3. Run `make test` to verify changes
4. Commit only source files, not generated files
