# HTAN Core Module

This module contains the universal attributes that are shared across all file-based modules in the HTAN project.

## Purpose

The Core module defines the common attributes that every file-based data type in HTAN must have. This eliminates duplication across modules and ensures consistency in how file metadata is structured.

## Universal Attributes

The `CoreFileAttributes` class defines these universal attributes:

### Required Attributes
- **COMPONENT**: Category of metadata (e.g., "Bulk WES Level 1", "scRNA-seq Level 2")
- **FILENAME**: Name of the file
- **FILE_FORMAT**: Format of the file (e.g., fastq, bam, vcf, h5ad)
- **HTAN_PARTICIPANT_ID**: HTAN ID associated with a patient
- **HTAN_DATA_FILE_ID**: HTAN Data File ID
- **HTAN_PARENT_ID**: HTAN Parent ID (Underscore B for Biospecimen and D for data file)

### Optional Attributes
- **HTAN_BIOSPECIMEN_ID**: HTAN Biospecimen ID of the parent biospecimen

## Validation Rules

All Core attributes include validation patterns to ensure data quality and consistency:

### FILENAME
- **Pattern**: `^.+\\/\\S*$`
- **Description**: Must contain a path with at least one character followed by a forward slash and non-whitespace characters

### FILE_FORMAT
- **Valid Values**: Extensive list of supported formats including:
  - **Sequencing**: fastq, fasta, bam, sam, vcf, bcf, maf
  - **Images**: tif, tiff, OME-TIFF, png, jpg, svg
  - **Documents**: pdf, doc, excel, powerpoint, txt, csv, tsv
  - **Compressed**: zip, gzip, bgzip, 7z, tar
  - **Data**: json, xml, sqlite, hdf5, RData, mtx
  - **And many more**: See full list in schema

### HTAN_PARTICIPANT_ID
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))$`
- **Examples**: 
  - `HTA200_2` (standard format)
  - `HTA200_EXT001` (external control)
  - `HTA200_0000` (special case)

### HTAN_DATA_FILE_ID
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$`
- **Examples**: 
  - `HTA200_2_36667` (standard format)
  - `HTA200_EXT001_36667` (external control)
  - `HTA200_0000_36667` (special case)

### HTAN_PARENT_ID
- **Pattern**: `^(HTA20[0-9])(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$`
- **Examples**:
  - **Biospecimen derivatives**: `HTA200_2_B7001` (participant_id_Binteger)
  - **Data file derivatives**: `HTA200_2_D36667` (participant_id_Dinteger)
  - **Control/Blank samples**: `HTA200_2_EXT001_B7002` (includes EXT code)

### HTAN_BIOSPECIMEN_ID
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$`
- **Examples**:
  - `HTA200_2_7001` (standard biospecimen)
  - `HTA200_EXT001_7001` (external control biospecimen)

## HTAN Identifier Validation

The HTAN identifiers follow specific patterns for different entity types:

### Pattern Breakdown:
- `HTA20[0-9]` - HTAN participant identifier (HTA200-HTA209)
- `(?:_0000)?` - Optional 0000 suffix
- `(?:_\d+)?` - Optional numeric suffix
- `(?:_EXT\d+)?` - Optional external control code
- `_(B|D)` - B for biospecimen derivatives, D for data files
- `\d{1,50}` - 1-50 digit integer

## Directory Structure

- `domains/` - Contains the core YAML schema definition
  - `core.yaml` - Universal attributes schema

## Usage

Other modules (WES, scRNA-seq, etc.) will import and inherit from the Core module:

```yaml
imports:
  - core

classes:
  BulkWESLevel1:
    is_a: CoreFileAttributes  # Inherit universal attributes
    attributes:
      # WES-specific attributes only
      LIBRARY_LAYOUT:
        range: LibraryLayoutEnum
        required: true
```

## Design Notes

- This is a **base schema** for inheritance, not a full module
- No Python implementation is generated since it's only used for schema inheritance
- The `CoreFileAttributes` class provides the foundation for all file-based data types
- Each module can extend these attributes with their specific requirements
- All validation patterns are enforced in JSON Schema generation
