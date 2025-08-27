# HTAN scRNA-seq Module

## Overview

The HTAN scRNA-seq module provides a comprehensive data model for single-cell RNA sequencing data, following the HTAN data model specifications. This module defines schemas for three data levels:

- **Level 1**: Raw sequencing files and metadata
- **Level 2**: Workflow and processing metadata  
- **Level 3/4**: Combined analysis results with h5ad file format validation

## Architecture

The scRNA-seq module uses a clean inheritance chain:

```
scRNA-seq classes → BaseSequencingAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: All scRNA-seq classes get universal file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes`
- **Base Sequencing Attributes**: All scRNA-seq classes get common sequencing attributes (LIBRARY_LAYOUT, SEQUENCING_PLATFORM, etc.) from `BaseSequencingAttributes`
- **scRNA-seq-Specific Attributes**: Each level adds its own scRNA-seq-specific attributes
- **No Duplication**: Common attributes are defined once in the base modules

## Schema Structure

### Level 1 (Raw Data)
Defines attributes for raw sequencing files and sample preparation metadata:

**Required Attributes:**
- `SINGLE_CELL_ISOLATION_METHOD`: Method used to isolate single cells
- `DISSOCIATION_METHOD`: Method used to dissociate tissue
- `NUCLEIC_ACID_SOURCE`: Type of nucleic acid (DNA/RNA)
- `LIBRARY_CONSTRUCTION_METHOD`: Method for library construction
- `REVERSE_TRANSCRIPTION_PRIMER`: Primer used for reverse transcription
- `SPIKE_IN`: Type of spike-in used
- `READ_INDICATOR`: Type of read (forward/reverse/index)
- Base attributes (LIBRARY_LAYOUT, SEQUENCING_PLATFORM, etc.) come from inheritance

**Enums (Alphabetically Ordered):**
- `DissociationMethodEnum`: Enzymatic, Mechanical, Other, Unknown
- `LibraryConstructionMethodEnum`: 10X Genomics, Drop-seq, Fluidigm C1, InDrop, Other, Smart-seq, Unknown
- `NucleicAcidSourceEnum`: DNA, RNA, Unknown
- `ReadIndicatorEnum`: Forward, Index, Reverse, Unknown
- `ReverseTranscriptionPrimerEnum`: Oligo-dT, Random Hexamer, Unknown
- `SingleCellIsolationMethodEnum`: Cell Sorting, Droplet-based, Manual Picking, Microfluidics, Other, Unknown
- `SpikeInEnum`: ERCC, None, Other, Unknown

### Level 2 (Processing Metadata)
Defines workflow and processing metadata:

**Required Attributes:**
- `SCRNASEQ_WORKFLOW_TYPE`: Generic name for the workflow
- Base attributes (WORKFLOW_VERSION, GENOMIC_REFERENCE, etc.) come from inheritance

**Enums (Alphabetically Ordered):**
- `scRNAseqWorkflowTypeEnum`: CellRanger, dropEST, HCA Optimus, Other, SEQC, STARsolo, Unknown

### Level 3/4 (Analysis Results)
Combined schema for analysis results with specific file format requirements:

**File Format Requirements:**
- `FILE_FORMAT`: Must be "h5ad" (pattern: `^h5ad$`)
- `ANNDATA_SCHEMA_VERSION`: Must be "0.1" (pattern: `^0\.1$`)
- `ANNDATA_STRUCTURE_VALIDATED`: Boolean flag for structure validation

**Required Attributes:**
- `SCRNASEQ_WORKFLOW_TYPE`: Workflow type
- `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION`: Detailed workflow parameters
- `DATA_CATEGORY`: Specific content type
- `MATRIX_TYPE`: Type of data stored in matrix
- `CELL_MEDIAN_NUMBER_READS`: Median reads per cell
- `CELL_MEDIAN_NUMBER_GENES`: Median genes per cell
- `CELL_TOTAL`: Total number of sequenced cells
- Base attributes (WORKFLOW_VERSION, WORKFLOW_LINK, etc.) come from inheritance


## Usage

### Schema Validation
```bash
# Validate schema
make validate

# Generate Python classes
make gen-python

# Generate JSON schema
make gen-json-schema

# Run tests
make test
```

## CellxGene Integration

The Level 3/4 schema is designed for integration with CellxGene:

- **h5ad File Format**: Only h5ad files are accepted for Level 3/4 data
- **AnnData 0.1 Schema**: Must conform to AnnData 0.1 schema specification
- **Structure Validation**: Includes boolean flag for structure validation

## Dependencies

- LinkML runtime
- pytest (for testing)
- linkml-validate (for schema validation)

## Testing

The module includes comprehensive tests for:
- Schema loading and validation
- Enum alphabetical ordering
- h5ad file format validation
- AnnData schema compliance
- Inheritance from CoreFileAttributes
- Data validation examples

Run tests with:
```bash
cd modules/scRNA-seq
make test
```
