# MultiplexMicroscopy

HTAN Multiplex Microscopy Data Model Schema for Phase 2 - All Levels

## Classes

### CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### MultiplexMicroscopyData

**Container for all Multiplex Microscopy data levels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `LEVEL_2_DATA` | MultiplexMicroscopyLevel2 | No | Level 2 Multiplex Microscopy data (imaging data with channel metadata) |
| `LEVEL_3_DATA` | MultiplexMicroscopyLevel3 | No | Level 3 Multiplex Microscopy data (segmentation masks) |
| `LEVEL_4_DATA` | MultiplexMicroscopyLevel4 | No | Level 4 Multiplex Microscopy data (cell-by-feature tables) |

### MultiplexMicroscopyLevel2

**Multiplex Microscopy Level 2 - Imaging data compiled into a single file format (preferably tiled and pyramidal OME-TIFF), accompanied by a CSV file containing channel metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHANNEL_METADATA_ID` | string, pattern: <code>^syn\d+$</code> | Yes | Unique identifier specifying the location of the required channel metadata (Synapse ID) |
| `FILE_FORMAT` | string, pattern: <code>^(ome-tiff\|tiff\|qptiff\|svs)$</code> | Yes | Format of the imaging file. Must be compatible with Bio-Formats or OpenSlide Python. |
| `IMAGING_ASSAY_TYPE` | [ImagingAssayType](#imagingassaytype) | Yes | Type of imaging assay |
| `PHYSICAL_SIZE_X` | float | Yes | Physical size of a single pixel in the x dimension. In microns. |
| `PHYSICAL_SIZE_Y` | float | Yes | Physical size of a single pixel in the y dimension. In microns. |
| `PHYSICAL_SIZE_Z` | float | Yes | Physical size of a single pixel in the z dimension. In microns. |
| `PYRAMID` | boolean | No | The data file contains an image pyramid |
| `SIZE_C` | integer | Yes | Number of channels. Integer >= 1 |
| `SIZE_T` | integer | Yes | Number of timepoints. Integer >= 1 |
| `SIZE_X` | integer | Yes | The number of pixels in the x dimension at the highest resolution available |
| `SIZE_Y` | integer | Yes | The number of pixels in the y dimension at the highest resolution available |
| `SIZE_Z` | integer | Yes | The number of pixels in the z dimension at the highest resolution available |
| `WORKING_DISTANCE` | string | No | The working distance of the lens, expressed as a floating point number. Floating point > 0. Size needs to be specified in microns (um) |

### MultiplexMicroscopyLevel3

**Multiplex Microscopy Level 3 - Segmentation mask. Structured mask data following existing HTAN segmentation templates (RFC Imaging Level 3 & 4 - v1)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string, pattern: <code>^(ome-tiff\|ome\.tiff\|tiff\|tif)$</code> | Yes | Format of the segmentation mask file (should be ome-tiff for Level 3) |
| `SEGMENTATION_ANNOTATION_TYPE` | string | No | Type of objects segmented (e.g., Cell, Nucleus, Tissue, ROI) |
| `SEGMENTATION_METHOD` | string | Yes | Method used for segmentation (e.g., CellPose, StarDist, Ilastik, manual annotation) |
| `SEGMENTATION_PARAMETERS` | string | No | Parameters used for segmentation (e.g., model name, threshold values, preprocessing steps) |
| `SEGMENTATION_WORKFLOW_TYPE` | string | Yes | Type of segmentation workflow used to generate the mask |
| `SEGMENTATION_WORKFLOW_URL` | string | No | URL or link to the segmentation workflow used |
| `SEGMENTATION_WORKFLOW_VERSION` | string | No | Version of the segmentation workflow |

### MultiplexMicroscopyLevel4

**Multiplex Microscopy Level 4 - Cell-by-feature table (typically cell-by-marker) generated from the segmentation mask and image. No changes from prior definitions (RFC Imaging Level 3 & 4 - v1)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FEATURE_EXTRACTION_METHOD` | string | Yes | Method used for feature extraction (e.g., mean intensity, median intensity, total intensity, texture features) |
| `FEATURE_EXTRACTION_PARAMETERS` | string | No | Parameters used for feature extraction (e.g., channel names, measurement types, normalization methods) |
| `FEATURE_EXTRACTION_WORKFLOW_TYPE` | string | Yes | Type of workflow used to extract features from segmented objects |
| `FEATURE_EXTRACTION_WORKFLOW_URL` | string | No | URL or link to the feature extraction workflow used |
| `FEATURE_EXTRACTION_WORKFLOW_VERSION` | string | No | Version of the feature extraction workflow |
| `FILE_FORMAT` | string, pattern: <code>^(csv\|h5ad)$</code> | Yes | Format of the feature table file (csv or h5ad for Level 4) |
| `MATRIX_TYPE` | [MatrixTypeEnum](#matrixtype) | Yes | Type of feature matrix (raw counts, normalized, etc.) |
| `NUMBER_OF_FEATURES` | integer | No | Number of features (markers/channels) in the feature matrix |
| `NUMBER_OF_OBJECTS` | integer | No | Number of segmented objects (cells, nuclei, etc.) in the feature matrix |

## Enums

### ImagingAssayType {#imagingassaytype}

| Value | Description |
|-------|-------------|
| `CODEX` | CODEX imaging assay type |
| `CyCIF` | Cyclic Immunofluorescence imaging assay type |
| `ExSeq` | Expansion Sequencing imaging assay type |
| `GeoMX-DSP` | GeoMX Digital Spatial Profiling imaging assay type |
| `H&E` | Hematoxylin and Eosin imaging assay type |
| `IHC` | Immunohistochemistry imaging assay type |
| `IMC` | Imaging Mass Cytometry imaging assay type |
| `MERFISH` | Multiplexed Error-Robust Fluorescence In Situ Hybridization imaging assay type |
| `MIBI` | Multiplexed Ion Beam Imaging imaging assay type |
| `MxIF` | Multiplexed Immunofluorescence imaging assay type |
| `Not Applicable` | Imaging assay not applicable |
| `SABER` | Signal Amplification By Exchange Reaction imaging assay type |
| `mIHC` | Multiplexed Immunohistochemistry imaging assay type |
| `t-CyCIF` | Tissue Cyclic Immunofluorescence imaging assay type |

### MatrixTypeEnum {#matrixtype}

| Value | Description |
|-------|-------------|
| `Log Normalized` | Log normalized counts |
| `Normalized Counts` | Normalized count matrix |
| `Other` | Other normalization method |
| `Raw Counts` | Raw count matrix |
| `Scaled Counts` | Scaled count matrix |
| `Z-Score Normalized` | Z-score normalized values |

