# Imaging

HTAN Base Imaging Data Model - Common attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)

## Classes in This Module

| Class | Level | Description |
|-------|-------|-------------|
| [BaseImagingAttributes](#baseimagingattributes) | — | Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.) |
| [CoreFileAttributes](#corefileattributes) | — | Universal attributes that apply to all file-based data in HTAN |

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseImagingAttributes

**Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | [ExperimentalStrategyAndDataSubtypes](enums.md#experimentalstrategyanddatasubtypes) | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `DE_IDENTIFICATION_METHOD_TYPE` | [DeIdentificationMethodType](enums.md#deidentificationmethodtype) | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | Conditional: Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' | Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | [License](enums.md#license) | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `IMAGE_MODALITY` | [ImageModality](enums.md#imagemodality) | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `STAINING_METHOD` | [StainingMethod](enums.md#stainingmethod) | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `IMMERSION` | [ImmersionMedium](enums.md#immersionmedium) | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | [Species](enums.md#species) | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | Conditional: Required when HAS_SLIDE_LABEL is true | Required when HAS_SLIDE_LABEL is true |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## Enums

### DeIdentificationMethodType

| Value | Description |
|-------|-------------|
| Automatic | Automatic de-identification method |
| Manual | Manual de-identification method |
| Not Applicable | De-identification not applicable |
| Semiautomatic | Semi-automatic de-identification method |

### ExperimentalStrategyAndDataSubtypes

| Value | Description |
|-------|-------------|
| Pathological | Pathological experimental strategy and data subtype |

### ImageModality

| Value | Description |
|-------|-------------|
| SM | Slide Microscopy |

### ImmersionMedium

| Value | Description |
|-------|-------------|
| Air | Air immersion medium |
| Glycerol | Glycerol immersion medium |
| Oil | Oil immersion medium |
| Other | Other immersion medium |
| Water | Water immersion medium |

### License

| Value | Description |
|-------|-------------|
| CC BY 4.0 | Creative Commons Attribution 4.0 International License |

### Species

| Value | Description |
|-------|-------------|
| 9606 (Homo sapiens) | NCBI Taxonomy ID for Homo sapiens |

### StainingMethod

| Value | Description |
|-------|-------------|
| CODEX | CODEX staining method |
| CyCIF | Cyclic Immunofluorescence staining method |
| ExSeq | Expansion Sequencing staining method |
| GeoMX-DSP | GeoMX Digital Spatial Profiling staining method |
| H&E | Hematoxylin and Eosin staining method |
| IHC | Immunohistochemistry staining method |
| IMC | Imaging Mass Cytometry staining method |
| MERFISH | Multiplexed Error-Robust Fluorescence In Situ Hybridization staining method |
| MIBI | Multiplexed Ion Beam Imaging staining method |
| MxIF | Multiplexed Immunofluorescence staining method |
| Not Applicable | Staining not applicable |
| SABER | Signal Amplification By Exchange Reaction staining method |
| mIHC | Multiplexed Immunohistochemistry staining method |
| t-CyCIF | Tissue Cyclic Immunofluorescence staining method |
