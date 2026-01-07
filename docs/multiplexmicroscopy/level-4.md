# MultiplexMicroscopy - Level 4

If submitting Level 4 files for MultiplexMicroscopy, here are the list of attributes you need to fill out:

**Multiplex Microscopy Level 4 - Cell-by-feature table (typically cell-by-marker) generated from the segmentation mask and image. No changes from prior definitions (RFC Imaging Level 3 & 4 - v1)**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### Base Imaging Attributes

These attributes are inherited from BaseImagingAttributes.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CITATION_OR_DOI` | string, pattern: <code>^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10\|127)(?:\.\d{1,3}){3})(?!(?:169\.254\|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]\|2\d\|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?\|1\d\d\|2[01]\d\|22[0-3])(?:\.(?:1?\d{1,2}\|2[0-4]\d\|25[0-5])){2}(?:\.(?:[1-9]\d?\|1\d\d\|2[0-4]\d\|25[0-4]))\|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$</code> | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Description of the process of removing potentially identifying data or data elements to render data into a form that does not identify individuals and where identification is not likely to take place. |
| `DE_IDENTIFICATION_METHOD_TYPE` | [DeIdentificationMethodType](#deidentificationmethodtype) | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | [ExperimentalStrategyAndDataSubtypes](#experimentalstrategyanddatasubtypes) | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `IMAGE_MODALITY` | [ImageModality](#imagemodality) | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_PROTOCOL` | string, pattern: <code>^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10\|127)(?:\.\d{1,3}){3})(?!(?:169\.254\|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]\|2\d\|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?\|1\d\d\|2[01]\d\|22[0-3])(?:\.(?:1?\d{1,2}\|2[0-4]\d\|25[0-5])){2}(?:\.(?:[1-9]\d?\|1\d\d\|2[0-4]\d\|25[0-4]))\|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$</code> | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `IMMERSION` | [ImmersionMedium](#immersionmedium) | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `LICENSE` | [License](#license) | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SLIDE_LABEL_REDACTED` | boolean | No | Have identifiers including dates been masked in the label image |
| `SPECIES` | [Species](#species) | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `STAINING_METHOD` | [StainingMethod](#stainingmethod) | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |

### Module-Specific Attributes

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

