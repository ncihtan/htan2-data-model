# DigitalPathology

HTAN Digital Pathology Data Model Schema for Phase 2

## Classes

### BaseImagingAttributes

**Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)**

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

### DigitalPathologyData

**Container for digital pathology imaging data**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ANNOTATION_TYPE` | AnnotationType<br/>`Artifact`, `Cell`, `Nucleus`, `ROI`, `Tissue` | No | What types of annotation are contained in the image |
| `FILE_FORMAT` | string | Yes | Format of the imaging file. Must be compatible with Bio-Formats or OpenSlide Python. |
| `HAS_ANNOTATIONS` | boolean | Yes | Does the image contain annotations |

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

