# MultiplexMicroscopy

HTAN Multiplex Microscopy Data Model Schema for Phase 2 - All Levels

## AnyValue

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|

## extension

**a tag/value pair used to add non-model information to an entry**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `extension_tag` | uriorcurie | Yes | a tag associated with an extension |
| `extension_value` | AnyValue | Yes | the actual annotation |
| `extensions` | extension | No | a tag/text tuple attached to an arbitrary element |

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | No |  |
| `FILE_FORMAT` | string | No |  |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## BaseImagingAttributes

**Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | ExperimentalStrategyAndDataSubtypes | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the ... |
| `DE_IDENTIFICATION_METHOD_TYPE` | DeIdentificationMethodType | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Description of the process of removing potentially identifying data or data elements to render da... |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | License | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC... |
| `IMAGE_MODALITY` | ImageModality | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging expe... |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier... |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/op... |
| `STAINING_METHOD` | StainingMethod | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in... |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object be... |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer... |
| `IMMERSION` | ImmersionMedium | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on ... |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | Species | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Have identifiers including dates been masked in the label image |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and th... |
| `FILENAME` | string | No |  |
| `FILE_FORMAT` | string | No |  |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## MultiplexMicroscopyLevel2

**Multiplex Microscopy Level 2 - Imaging data compiled into a single file format (preferably tiled and pyramidal OME-TIFF), accompanied by a CSV file containing channel metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | No |  |
| `FILENAME` | string | No |  |
| `WORKING_DISTANCE` | string | No | The working distance of the lens, expressed as a floating point number. Floating point > 0. Size ... |
| `IMAGING_ASSAY_TYPE` | ImagingAssayType | Yes | Type of imaging assay |
| `PYRAMID` | boolean | No | The data file contains an image pyramid |
| `PHYSICAL_SIZE_X` | float | Yes | Physical size of a single pixel in the x dimension. In microns. |
| `PHYSICAL_SIZE_Y` | float | Yes | Physical size of a single pixel in the y dimension. In microns. |
| `PHYSICAL_SIZE_Z` | float | Yes | Physical size of a single pixel in the z dimension. In microns. |
| `SIZE_C` | integer | Yes | Number of channels. Integer >= 1 |
| `SIZE_T` | integer | Yes | Number of timepoints. Integer >= 1 |
| `SIZE_X` | integer | Yes | The number of pixels in the x dimension at the highest resolution available |
| `SIZE_Y` | integer | Yes | The number of pixels in the y dimension at the highest resolution available |
| `SIZE_Z` | integer | Yes | The number of pixels in the z dimension at the highest resolution available |
| `CHANNEL_METADATA_ID` | string | Yes | Unique identifier specifying the location of the required channel metadata (Synapse ID) |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | ExperimentalStrategyAndDataSubtypes | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the ... |
| `DE_IDENTIFICATION_METHOD_TYPE` | DeIdentificationMethodType | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Description of the process of removing potentially identifying data or data elements to render da... |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | License | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC... |
| `IMAGE_MODALITY` | ImageModality | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging expe... |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier... |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/op... |
| `STAINING_METHOD` | StainingMethod | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in... |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object be... |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer... |
| `IMMERSION` | ImmersionMedium | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on ... |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | Species | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Have identifiers including dates been masked in the label image |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and th... |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## MultiplexMicroscopyLevel3

**Multiplex Microscopy Level 3 - Segmentation mask. Structured mask data following existing HTAN segmentation templates (RFC Imaging Level 3 & 4 - v1)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `SEGMENTATION_WORKFLOW_TYPE` | string | Yes | Type of segmentation workflow used to generate the mask |
| `SEGMENTATION_WORKFLOW_URL` | string | No | URL or link to the segmentation workflow used |
| `SEGMENTATION_WORKFLOW_VERSION` | string | No | Version of the segmentation workflow |
| `SEGMENTATION_METHOD` | string | Yes | Method used for segmentation (e.g., CellPose, StarDist, Ilastik, manual annotation) |
| `SEGMENTATION_PARAMETERS` | string | No | Parameters used for segmentation (e.g., model name, threshold values, preprocessing steps) |
| `SEGMENTATION_ANNOTATION_TYPE` | string | No | Type of objects segmented (e.g., Cell, Nucleus, Tissue, ROI) |
| `FILE_FORMAT` | string | No |  |
| `FILENAME` | string | No |  |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | ExperimentalStrategyAndDataSubtypes | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the ... |
| `DE_IDENTIFICATION_METHOD_TYPE` | DeIdentificationMethodType | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Description of the process of removing potentially identifying data or data elements to render da... |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | License | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC... |
| `IMAGE_MODALITY` | ImageModality | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging expe... |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier... |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/op... |
| `STAINING_METHOD` | StainingMethod | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in... |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object be... |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer... |
| `IMMERSION` | ImmersionMedium | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on ... |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | Species | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Have identifiers including dates been masked in the label image |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and th... |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## MultiplexMicroscopyLevel4

**Multiplex Microscopy Level 4 - Cell-by-feature table (typically cell-by-marker) generated from the segmentation mask and image. No changes from prior definitions (RFC Imaging Level 3 & 4 - v1)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FEATURE_EXTRACTION_WORKFLOW_TYPE` | string | Yes | Type of workflow used to extract features from segmented objects |
| `FEATURE_EXTRACTION_WORKFLOW_URL` | string | No | URL or link to the feature extraction workflow used |
| `FEATURE_EXTRACTION_WORKFLOW_VERSION` | string | No | Version of the feature extraction workflow |
| `MATRIX_TYPE` | MatrixTypeEnum | Yes | Type of feature matrix (raw counts, normalized, etc.) |
| `FEATURE_EXTRACTION_METHOD` | string | Yes | Method used for feature extraction (e.g., mean intensity, median intensity, total intensity, text... |
| `FEATURE_EXTRACTION_PARAMETERS` | string | No | Parameters used for feature extraction (e.g., channel names, measurement types, normalization met... |
| `NUMBER_OF_FEATURES` | integer | No | Number of features (markers/channels) in the feature matrix |
| `NUMBER_OF_OBJECTS` | integer | No | Number of segmented objects (cells, nuclei, etc.) in the feature matrix |
| `FILE_FORMAT` | string | No |  |
| `FILENAME` | string | No |  |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | ExperimentalStrategyAndDataSubtypes | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the ... |
| `DE_IDENTIFICATION_METHOD_TYPE` | DeIdentificationMethodType | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Description of the process of removing potentially identifying data or data elements to render da... |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | License | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC... |
| `IMAGE_MODALITY` | ImageModality | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging expe... |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier... |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/op... |
| `STAINING_METHOD` | StainingMethod | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in... |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object be... |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer... |
| `IMMERSION` | ImmersionMedium | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on ... |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | Species | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Have identifiers including dates been masked in the label image |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and th... |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## MultiplexMicroscopyData

**Container for all Multiplex Microscopy data levels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `LEVEL_2_DATA` | MultiplexMicroscopyLevel2 | No | Level 2 Multiplex Microscopy data (imaging data with channel metadata) |
| `LEVEL_3_DATA` | MultiplexMicroscopyLevel3 | No | Level 3 Multiplex Microscopy data (segmentation masks) |
| `LEVEL_4_DATA` | MultiplexMicroscopyLevel4 | No | Level 4 Multiplex Microscopy data (cell-by-feature tables) |

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

### ImagingAssayType

| Value | Description |
|-------|-------------|
| CODEX | CODEX imaging assay type |
| CyCIF | Cyclic Immunofluorescence imaging assay type |
| ExSeq | Expansion Sequencing imaging assay type |
| GeoMX-DSP | GeoMX Digital Spatial Profiling imaging assay type |
| H&E | Hematoxylin and Eosin imaging assay type |
| IHC | Immunohistochemistry imaging assay type |
| IMC | Imaging Mass Cytometry imaging assay type |
| MIBI | Multiplexed Ion Beam Imaging imaging assay type |
| MERFISH | Multiplexed Error-Robust Fluorescence In Situ Hybridization imaging assay type |
| MxIF | Multiplexed Immunofluorescence imaging assay type |
| mIHC | Multiplexed Immunohistochemistry imaging assay type |
| Not Applicable | Imaging assay not applicable |
| SABER | Signal Amplification By Exchange Reaction imaging assay type |
| t-CyCIF | Tissue Cyclic Immunofluorescence imaging assay type |

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

### MatrixTypeEnum

| Value | Description |
|-------|-------------|
| Raw Counts | Raw count matrix |
| Normalized Counts | Normalized count matrix |
| Scaled Counts | Scaled count matrix |
| Log Normalized | Log normalized counts |
| Z-Score Normalized | Z-score normalized values |
| Other | Other normalization method |

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
