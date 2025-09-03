# HTAN Base Sequencing Module

## Overview

The HTAN Base Sequencing module provides a shared foundation for all sequencing data types in the HTAN project. This module defines common attributes, enums, and base classes that are shared across different sequencing modalities (WES, scRNA-seq, etc.).

## Purpose

The base sequencing module serves as a foundation to:
- **Reduce duplication** across sequencing modules
- **Ensure consistency** in common attributes
- **Simplify maintenance** of shared sequencing metadata
- **Enable modular architecture** for different sequencing types

## Schema Structure

### BaseSequencingAttributes Class

The main class that defines common attributes shared across all sequencing types:

**Required Attributes:**
- `LIBRARY_LAYOUT`: Library layout (paired-end or single-end)
- `SEQUENCING_PLATFORM`: Sequencing platform used
- `WORKFLOW_VERSION`: Major version of the workflow
- `GENOMIC_REFERENCE`: Genomic reference used for alignment

**Optional Attributes:**
- `SEQUENCING_BATCH_ID`: Sequencing batch identifier
- `LIBRARY_PREPARATION_DAYS_FROM_INDEX`: Days from index for library preparation
- `TECHNICAL_REPLICATE_GROUP`: Technical replicate group identifier
- `PROTOCOL_LINK`: Link to sequencing protocol
- `WORKFLOW_LINK`: Link to workflow (DockStore.org recommended)
- `GENOMIC_REFERENCE_URL`: URL to genomic reference
- `GENOME_ANNOTATION_URL`: URL to genome annotation
- `CHECKSUM`: Checksum for data integrity verification

### Enums (Alphabetically Ordered)

**LibraryLayoutEnum:**
- `Paired-end`: Paired-end sequencing
- `Single-end`: Single-end sequencing

**SequencingPlatformEnum:**
- `ABI_SOLID`: ABI SOLID sequencing platform
- `BGISEQ`: BGI sequencing platform
- `CAPILLARY`: Capillary sequencing platform
- `COMPLETE_GENOMICS`: Complete Genomics sequencing platform
- `HELICOS`: Helicos sequencing platform
- `ILLUMINA`: Illumina sequencing platform
- `ION_TORRENT`: Ion Torrent sequencing platform
- `LS454`: 454 sequencing platform
- `OXFORD_NANOPORE`: Oxford Nanopore sequencing platform
- `PACBIO_SMRT`: PacBio SMRT sequencing platform

## Architecture

The `BaseSequencingAttributes` class uses a clean inheritance chain:

```
BaseSequencingAttributes → BiospecimenAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: Gets universal file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes`
- **Biospecimen Attributes**: Gets required `HTAN_BIOSPECIMEN_ID` from `BiospecimenAttributes`
- **Base Sequencing Attributes**: All sequencing modules get common sequencing attributes (LIBRARY_LAYOUT, SEQUENCING_PLATFORM, etc.)
- **No Duplication**: Common attributes are defined once in the base modules

Specific sequencing modules (WES, scRNA-seq) will:
- Inherit from `BaseSequencingAttributes` to get core file, biospecimen, and sequencing attributes
- Add their own specific attributes
- Maintain consistent structure across all sequencing types

## Usage

### Import in Other Modules

```yaml
# In WES module
imports:
  - ../../Sequencing/domains/sequencing

classes:
  BulkWESLevel1:
    is_a: BaseSequencingAttributes
    attributes:
      # WES-specific attributes
      TARGET_CAPTURE_KIT:
        range: string
        required: false
```

```yaml
# In scRNA-seq module
imports:
  - ../../Sequencing/domains/sequencing

classes:
  scRNALevel1:
    is_a: BaseSequencingAttributes
    attributes:
      # scRNA-seq-specific attributes
      SINGLE_CELL_ISOLATION_METHOD:
        range: SingleCellIsolationMethodEnum
        required: true
```

## Build and Testing

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

## Testing

The module includes comprehensive tests for:
- Schema loading and validation
- Enum alphabetical ordering
- Inheritance from CoreFileAttributes
- Common attribute presence and validation
- Optional vs required attribute marking
- Data validation examples

## Dependencies

- **Core Module**: Inherits from `CoreFileAttributes`
- **LinkML**: Uses LinkML for schema definition
- **pytest**: For testing framework

## Architecture Benefits

### Modular Design
- **WES Module**: Extends base with WES-specific attributes
- **scRNA-seq Module**: Extends base with scRNA-seq-specific attributes
- **Future Modules**: Can easily extend base for new sequencing types

### Consistency
- All sequencing modules share the same common attributes
- Consistent enum values across all sequencing types
- Unified validation patterns
