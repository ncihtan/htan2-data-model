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
2. Run `make gen-project` to regenerate schema classes
3. Run tests to verify changes
4. Commit only source files, not generated files
