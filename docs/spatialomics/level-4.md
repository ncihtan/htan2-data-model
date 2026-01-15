# SpatialOmics - Level 4

📥 [Download attributes as CSV](csv/spatialomics-level-4.csv)

If submitting Level 4 files for SpatialOmics, here are the list of attributes you need to fill out:

**Level 4 interoperable spatial omics file (optional) - Harmonized h5ad, RDS, or Zarr file for downstream analysis**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CELL_TYPES` | string | Required IF HAS_CELL_TYPE_CALLING = 'None' | List of cell types present in the data |
| `CELL_TYPE_CALLING_METHOD` | string | Required IF HAS_CELL_TYPE_CALLING = 'None' | Method used for cell type annotation |
| `CLUSTERING_METHOD` | string | Required IF HAS_CLUSTERING = 'None' | Method used to define clusters |
| `DIMENSIONALITY_REDUCTION_METHOD` | [DimensionalityReductionMethodLevel4](#dimensionalityreductionmethodlevel4) | Required IF HAS_DIMENSIONALITY_REDUCTION = 'None' | Method used for dimensionality reduction |
| `FILENAME` | string, pattern: <code>^.+\.(h5ad\|rds\|zarr)$</code> | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.h5ad for h5ad; .rds for rds; .zarr for zarr) |
| `FILE_FORMAT` | [FileFormatLevel4](#fileformatlevel4) | Yes | File format of the data file |
| `HAS_CELL_TYPE_CALLING` | boolean | Yes | Indicates presence of cell type annotations |
| `HAS_CLUSTERING` | boolean | Yes | Indicates if clustering was performed |
| `HAS_DIMENSIONALITY_REDUCTION` | boolean | Yes | Indicates presence of dimensionally reduced data |
| `HAS_IMAGE` | boolean | Yes | Indicates presence of associated image data |
| `HAS_NORMALISED_ARRAY` | boolean | Yes | Indicates presence of normalized array |
| `HAS_RAW_ARRAY` | boolean | Yes | Indicates presence of raw expression array |
| `IMAGE_TYPE` | [ImageTypeLevel4](#imagetypelevel4) | Required IF HAS_IMAGE = 'None' | Type of image associated with the data file |
| `NORMALISATION_METHOD` | [NormalisationMethod](#normalisationmethod) | Required IF HAS_NORMALISED_ARRAY = 'None' | Method used for normalizing the array data |
| `NUMBER_OF_CLUSTERS` | integer | Required IF HAS_CLUSTERING = 'None' | Number of clusters identified |
| `NUMBER_OF_FEATURES` | integer | Yes | Number of features (e.g. transcripts) |
| `NUMBER_OF_OBJECTS` | integer | Yes | Number of objects (e.g. cells) |
| `TOOL_COMPATIBILITY` | [ToolCompatibility](#toolcompatibility) | No | Tools or libraries compatible with this file |

## Enums

### DimensionalityReductionMethodLevel4

| Value | Description |
|-------|-------------|
| `PCA` | Principal Component Analysis |
| `UMAP` | Uniform Manifold Approximation and Projection |
| `other` | Other dimensionality reduction method |
| `t-SNE` | t-Distributed Stochastic Neighbor Embedding |

### FileFormatLevel4

| Value | Description |
|-------|-------------|
| `h5ad` | AnnData HDF5 format (Python) |
| `rds` | RDS format (R) |
| `zarr` | Zarr format |

### ImageTypeLevel4

| Value | Description |
|-------|-------------|
| `jpeg` | JPEG image format |
| `other` | Other image format |
| `png` | PNG image format |
| `tiff` | TIFF image format |

### NormalisationMethod

| Value | Description |
|-------|-------------|
| `CPM` | Counts Per Million normalization |
| `SCTransform` | SCTransform normalization |
| `TPM` | Transcripts Per Million normalization |
| `log normalization` | Log normalization |
| `other` | Other normalization method |

### ToolCompatibility

| Value | Description |
|-------|-------------|
| `anndata` | AnnData library compatibility |
| `seurat` | Seurat library compatibility |
| `spatialdata` | SpatialData library compatibility |

