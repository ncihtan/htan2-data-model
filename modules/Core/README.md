# HTAN Core Module

Universal attributes shared across all file-based modules in the HTAN project.

## Purpose

Defines common attributes that every file-based data type in HTAN must have, eliminating duplication and ensuring consistency.

## Universal Attributes

### Required Attributes
- **COMPONENT**: Category of metadata (e.g., "Bulk WES Level 1", "scRNA-seq Level 2")
- **FILENAME**: Name of the file (pattern: `^.+[\\\\/]\\S*$`)
- **FILE_FORMAT**: Format of the file (e.g., fastq, bam, vcf, h5ad)
- **HTAN_PARTICIPANT_ID**: HTAN ID associated with a patient
- **HTAN_DATA_FILE_ID**: HTAN Data File ID (Primary Key)
- **HTAN_PARENT_ID**: HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
- **HTAN_BIOSPECIMEN_ID**: HTAN Biospecimen ID of the parent biospecimen

### Optional Attributes
- None currently defined

## Primary and Foreign Keys

### Primary Keys (marked with `identifier: true`)
- **HTAN_DATA_FILE_ID**: Unique identifier for data files across all levels

### Required Fields (not primary keys in this context)
- **HTAN_PARTICIPANT_ID**: HTAN ID associated with a patient
- **HTAN_BIOSPECIMEN_ID**: HTAN Biospecimen ID of the parent biospecimen

### Foreign Key
- **HTAN_PARENT_ID**: References parent entity using suffix convention:
  - `_B####` - References a biospecimen (e.g., `HTA200_2_B7001`)
  - `_D####` - References a data file (e.g., `HTA200_2_D36667`)

### Data Hierarchy
```
Participant (HTAN_PARTICIPANT_ID)
├── Biospecimen (HTAN_BIOSPECIMEN_ID)
│   └── Level 1 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _B####
│       └── Level 2 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
│           └── Level 3 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
```

## Validation Patterns

### HTAN_PARTICIPANT_ID
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))$`
- **Examples**: `HTA200_2`, `HTA200_EXT001`, `HTA200_0000`

### HTAN_DATA_FILE_ID
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$`
- **Examples**: `HTA200_2_36667`, `HTA200_EXT001_36667`

### HTAN_PARENT_ID
- **Pattern**: `^(HTA20[0-9])(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$`
- **Examples**: `HTA200_2_B7001` (biospecimen), `HTA200_2_D36667` (data file)

### HTAN_BIOSPECIMEN_ID
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$`
- **Examples**: `HTA200_2_7001`, `HTA200_EXT001_7001`

## Usage

Other modules inherit from Core:

```yaml
imports:
  - ../../Core/domains/core

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

- **Base schema** for inheritance, not a full module
- No Python implementation generated (schema inheritance only)
- All validation patterns enforced in JSON Schema generation
- Provides foundation for all file-based data types
