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
  - Confirms `BulkWESLevel1` class exists
  - Verifies all required attributes are present: `COMPONENT`, `FILENAME`, `FILE_FORMAT`, `HTAN_PARENT_BIOSPECIMEN_ID`, `HTAN_DATA_FILE_ID`, `LIBRARY_LAYOUT`, `LIBRARY_SELECTION_METHOD`, `READ_LENGTH`, `SEQUENCING_PLATFORM`

- **`test_level_2_schema`**: Validates Level 2 schema structure
  - Confirms `BulkWESLevel2` class exists
  - Verifies all required attributes are present: `COMPONENT`, `FILENAME`, `FILE_FORMAT`, `HTAN_PARENT_DATA_FILE_ID`, `HTAN_DATA_FILE_ID`, `ALIGNMENT_WORKFLOW_TYPE`, `GENOMIC_REFERENCE`, `MEAN_COVERAGE`, `TOTAL_READS`, `TOTAL_UNIQUELY_MAPPED`, `TOTAL_UNMAPPED_READS`, `PROPORTION_READS_MAPPED`

- **`test_level_3_schema`**: Validates Level 3 schema structure
  - Confirms `BulkWESLevel3` class exists
  - Verifies all required attributes are present: `COMPONENT`, `FILENAME`, `FILE_FORMAT`, `HTAN_PARENT_DATA_FILE_ID`, `HTAN_DATA_FILE_ID`, `GENOMIC_REFERENCE`

### Enum Validation Tests
- **`test_enums`**: Validates that all enums are properly defined in their respective level files
  - **Level 1 enums**: `LibraryLayoutEnum`, `LibrarySelectionMethodEnum`, `SequencingPlatformEnum`
  - **Level 2 enums**: `MSIStatusEnum`
  - **Level 3 enums**: `SomaticVariantsSampleTypeEnum`

### Test Coverage
These tests ensure:
- Schema files are valid LinkML YAML
- All required attributes are present in each level
- Enums are correctly defined and accessible
- Import relationships work correctly
- Generated Python classes will have the expected structure

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
