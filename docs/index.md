# HTAN Phase 2 Data Model

Welcome to the HTAN Phase 2 Data Model documentation. This documentation provides comprehensive guides and references for working with the Human Tumor Atlas Network (HTAN) data model.

## Overview

The HTAN Phase 2 Data Model is a comprehensive, modular data model built using **LinkML** for standardizing cancer research data. It supports multiple data types including clinical records, biospecimens, sequencing data, and imaging data.

```mermaid
graph TD
    A[HTAN2 Data Model] --> B[Record-Based Modules]
    A --> C[File-Based Modules]
    B --> D[Clinical]
    B --> E[Biospecimen]
    C --> F[Sequencing]
    C --> G[Imaging]
    F --> H[WES]
    F --> I[scRNA-seq]
    F --> J[SpatialOmics]
    G --> K[DigitalPathology]
    G --> L[MultiplexMicroscopy]
```

## Quick Links

- **[Getting Started](getting-started.md)** - New to HTAN2? Start here
- **[Module Overview](modules/overview.md)** - Understand the module architecture
- **[API Reference](reference/index.md)** - Complete schema reference
- **[Contributing](contributing.md)** - How to contribute to the data model

## Module Categories

### Record-Based Modules
Modules that represent clinical and biospecimen records:

- **[Clinical](modules/clinical.md)** - Clinical and demographic data
- **[Biospecimen](modules/biospecimen.md)** - Biospecimen metadata and classification

### File-Based Modules
Modules that represent data files with hierarchical levels:

#### Sequencing Modules
- **[WES](modules/wes.md)** - Whole Exome Sequencing (3 levels)
- **[Sequencing Base](modules/sequencing.md)** - Base sequencing attributes

#### Imaging Modules
- **[Digital Pathology](modules/digital-pathology.md)** - Whole-slide imaging data
- **[Multiplex Microscopy](modules/multiplex-microscopy.md)** - Multiplexed tissue imaging
- **[Imaging Base](modules/imaging.md)** - Base imaging attributes

#### Single-Cell & Spatial
- **[scRNA-seq](modules/scrna-seq.md)** - Single-cell RNA sequencing
- **[Spatial Omics](modules/spatial-omics.md)** - Spatial omics assays

### Core Modules
- **[Core File](modules/core-file.md)** - Universal file attributes

## Key Concepts

### Data Hierarchy

```
Participant (HTAN_PARTICIPANT_ID)
├── Biospecimen (HTAN_BIOSPECIMEN_ID)
│   └── Level 1 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _B####
│       └── Level 2 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
│           └── Level 3 Data (HTAN_DATA_FILE_ID) → HTAN_PARENT_ID: _D####
```

### Primary Identifiers

- **`HTAN_DATA_FILE_ID`**: Unique identifier for all data files
- **`HTAN_BIOSPECIMEN_ID`**: Unique identifier for biospecimens
- **`HTAN_PARTICIPANT_ID`**: Unique identifier for participants

### Foreign Keys

- **`HTAN_PARENT_ID`**: References parent entity
  - `_B####` - References a biospecimen
  - `_D####` - References a data file

## Resources

- [HTAN Website](https://humantumoratlas.org)
- [LinkML Documentation](https://linkml.io)
- [GitHub Repository](https://github.com/ncihtan/htan2-data-model)
- [Contributing Guide](../CONTRIBUTING.md)
