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



---

## Schema Documentation

# Imaging

HTAN Base Imaging Data Model - Common attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)

## Classes

### BaseImagingAttributes

Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Description of the process of removing potentially identifying data or data elements to render data into a form that does not identify individuals and where identification is not likely to take place. |
| `DE_IDENTIFICATION_METHOD_TYPE` | DeIdentificationMethodType<br/>`Automatic`, `Manual`, `Not Applicable`, `Semiautomatic` | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | ExperimentalStrategyAndDataSubtypes<br/>`Pathological` | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `IMAGE_MODALITY` | ImageModality<br/>`SM` | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `IMMERSION` | ImmersionMedium<br/>`Air`, `Glycerol`, `Oil`, `Other`, `Water` | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `LICENSE` | License<br/>`CC BY 4.0` | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SLIDE_LABEL_REDACTED` | boolean | No | Have identifiers including dates been masked in the label image |
| `SPECIES` | Species<br/>`9606 (Homo sapiens)` | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `STAINING_METHOD` | See [StainingMethod](#stainingmethod) enum below | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |

## Enums

### StainingMethod {#stainingmethod}

| Value | Description |
|-------|-------------|
| `CODEX` | CODEX staining method |
| `CyCIF` | Cyclic Immunofluorescence staining method |
| `ExSeq` | Expansion Sequencing staining method |
| `GeoMX-DSP` | GeoMX Digital Spatial Profiling staining method |
| `H&E` | Hematoxylin and Eosin staining method |
| `IHC` | Immunohistochemistry staining method |
| `IMC` | Imaging Mass Cytometry staining method |
| `MERFISH` | Multiplexed Error-Robust Fluorescence In Situ Hybridization staining method |
| `MIBI` | Multiplexed Ion Beam Imaging staining method |
| `MxIF` | Multiplexed Immunofluorescence staining method |
| `Not Applicable` | Staining not applicable |
| `SABER` | Signal Amplification By Exchange Reaction staining method |
| `mIHC` | Multiplexed Immunohistochemistry staining method |
| `t-CyCIF` | Tissue Cyclic Immunofluorescence staining method |

