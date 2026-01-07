# MultiplexMicroscopy - Level 4

HTAN Multiplex Microscopy Level 4 - Cell-by-feature tables

**Multiplex Microscopy Level 4 - Cell-by-feature table (typically cell-by-marker) generated from the segmentation mask and image. No changes from prior definitions (RFC Imaging Level 3 & 4 - v1)**

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

