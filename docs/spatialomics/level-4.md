# SpatialOmics - Level 4

HTAN Spatial Omics Level 4 - Interoperable h5ad or RDS file (optional)

**Level 4 interoperable spatial omics file (optional) - Harmonized h5ad, RDS, or Zarr file for downstream analysis**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CELL_TYPES` | string | Required IF HAS_CELL_TYPE_CALLING = 'None' | List of cell types present in the data |
| `CELL_TYPE_CALLING_METHOD` | string | Required IF HAS_CELL_TYPE_CALLING = 'None' | Method used for cell type annotation |
| `CLUSTERING_METHOD` | string | Required IF HAS_CLUSTERING = 'None' | Method used to define clusters |
| `DIMENSIONALITY_REDUCTION_METHOD` | [DimensionalityReductionMethodLevel4](#dimensionalityreductionmethodlevel4) | Required IF HAS_DIMENSIONALITY_REDUCTION = 'None' | Method used for dimensionality reduction |
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

