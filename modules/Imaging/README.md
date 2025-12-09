# HTAN Base Imaging Module

## Overview

The HTAN Base Imaging module provides a shared foundation for all imaging data types in the HTAN project. This module defines common attributes, enums, and base classes that are shared across different imaging modalities (Digital Pathology, Multiplex Microscopy, etc.).

## Purpose

The base imaging module serves as a foundation to:
- **Reduce duplication** across imaging modules
- **Ensure consistency** in common attributes
- **Simplify maintenance** of shared imaging metadata
- **Enable modular architecture** for different imaging types

## Schema Structure

### BaseImagingAttributes Class

The main class that defines common attributes shared across all imaging types:

**Required Attributes:**
- `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES`: Experimental strategy used for the study
- `DE_IDENTIFICATION_METHOD_TYPE`: De-identification method type (Automatic, Manual, Semiautomatic, Not Applicable)
- `LICENSE`: Official or legal permission to do or own a specified thing
- `IMAGE_MODALITY`: The method in which the images are generated (currently: Slide Microscopy)
- `IMAGING_EQUIPMENT_MANUFACTURER`: Producer of the imaging equipment
- `CITATION_OR_DOI`: Raw Data Protocol or Digital Object Identifier Text
- `STAINING_METHOD`: Staining method used (CODEX, CyCIF, H&E, IHC, IMC, MIBI, MERFISH, etc.)
- `OBJECTIVE`: Manufacturer and/or model number for the optical element
- `NOMINAL_MAGNIFICATION`: Magnification of the lens (floating point value > 1)
- `PASSED_QC`: Confirm that the image has passed internal quality control checks
- `QC_COMMENT`: Comments related to quality control checks
- `SPECIES`: NCBI Taxonomy ID

**Optional Attributes:**
- `DE_IDENTIFICATION_METHOD_DESCRIPTION`: Description of the de-identification process (required when DE_IDENTIFICATION_METHOD_TYPE is not "Not Applicable")
- `DE_IDENTIFICATION_SOFTWARE`: Software used to de-identify the images
- `IMAGING_EQUIPMENT_MODEL`: Specific model of the instrument
- `IMAGING_SOFTWARE`: Software package used to capture, generate, and process the image
- `IMAGING_PROTOCOL`: Protocols.io ID or DOI link to imaging protocol
- `IMMERSION`: Immersion medium (Air, Glycerol, Oil, Other, Water)
- `LENS_NUMERICAL_APERTURE`: Numerical aperture of the lens (floating point value > 0)

**Note:** Organ/Tissue, Tissue Fixative, and Embedding Medium are biospecimen attributes and should be retrieved from the Biospecimen record via `HTAN_PARENT_ID` (which references the biospecimen with B suffix).

### Enums (Alphabetically Ordered)

**DeIdentificationMethodType:**
- `Automatic`: Automatic de-identification method
- `Manual`: Manual de-identification method
- `Not Applicable`: De-identification not applicable
- `Semiautomatic`: Semi-automatic de-identification method

**ImageModality:**
- `SM`: Slide Microscopy

**StainingMethod:**
- `CODEX`: CODEX staining method
- `CyCIF`: Cyclic Immunofluorescence staining method
- `ExSeq`: Expansion Sequencing staining method
- `GeoMX-DSP`: GeoMX Digital Spatial Profiling staining method
- `H&E`: Hematoxylin and Eosin staining method
- `IHC`: Immunohistochemistry staining method
- `IMC`: Imaging Mass Cytometry staining method
- `MIBI`: Multiplexed Ion Beam Imaging staining method
- `MERFISH`: Multiplexed Error-Robust Fluorescence In Situ Hybridization staining method
- `MxIF`: Multiplexed Immunofluorescence staining method
- `mIHC`: Multiplexed Immunohistochemistry staining method
- `Not Applicable`: Staining not applicable
- `SABER`: Signal Amplification By Exchange Reaction staining method
- `t-CyCIF`: Tissue Cyclic Immunofluorescence staining method

**ImmersionMedium:**
- `Air`: Air immersion medium
- `Glycerol`: Glycerol immersion medium
- `Oil`: Oil immersion medium
- `Other`: Other immersion medium
- `Water`: Water immersion medium

## Architecture

The `BaseImagingAttributes` class uses a clean inheritance chain:

```
BaseImagingAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: Gets universal file attributes (FILENAME, HTAN_DATA_FILE_ID, HTAN_PARENT_ID, etc.) from `CoreFileAttributes`
- **Base Imaging Attributes**: All imaging modules get common imaging attributes (EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES, DE_IDENTIFICATION_METHOD_TYPE, etc.)
- **No Duplication**: Common attributes are defined once in the base modules

Specific imaging modules (Digital Pathology, Multiplex Microscopy) will:
- Inherit from `BaseImagingAttributes` to get core file and imaging attributes
- Add their own specific attributes
- Maintain consistent structure across all imaging types

## Usage

### Import in Other Modules

```yaml
# In Digital Pathology module
imports:
  - ../../Imaging/domains/imaging

classes:
  DigitalPathologyData:
    is_a: BaseImagingAttributes
    attributes:
      # Digital Pathology-specific attributes
      HAS_ANNOTATIONS:
        range: boolean
        required: true
```

```yaml
# In Multiplex Microscopy module
imports:
  - ../../Imaging/domains/imaging

classes:
  MultiplexMicroscopyLevel2:
    is_a: BaseImagingAttributes
    attributes:
      # Multiplex Microscopy-specific attributes
      IMAGING_ASSAY_TYPE:
        range: ImagingAssayType
        required: true
```

## Conditional Requirements

The module implements conditional requirements using LinkML rules:

- `DE_IDENTIFICATION_METHOD_DESCRIPTION`: Required when `DE_IDENTIFICATION_METHOD_TYPE` is not "Not Applicable"
  - Implemented as a LinkML rule with preconditions and postconditions
  - Ensures proper validation in generated JSON schemas

## Build and Testing

### Schema Validation
```bash
# Validate schema
make validate

# Generate Python classes
make gen-schema

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
- Conditional requirements validation
- Minimum value constraints

## Dependencies

- **Core Module**: Inherits from `CoreFileAttributes`
- **Biospecimen Module**: Record-based module (does not inherit from CoreFileAttributes)

