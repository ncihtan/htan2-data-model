# scRNA-seq - Level 3/4

Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships

**Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ANNDATA_SCHEMA_VERSION` | string, pattern: <code>^0\.1$</code> | Yes | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | boolean | Yes | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `CELL_MEDIAN_NUMBER_GENES` | integer | Yes | Median number of genes detected per cell |
| `CELL_MEDIAN_NUMBER_READS` | integer | Yes | Median number of reads per cell |
| `CELL_TOTAL` | integer | Yes | Number of sequenced cells. Applies to raw counts matrix only |
| `DATA_CATEGORY` | [DataCategoryEnum](#datacategory) | Yes | Specific content type of the data file |
| `FILE_FORMAT` | string, pattern: <code>^h5ad$</code> | Yes | Format of the file (only h5ad files accepted for Level 3/4) |
| `LINKED_MATRICES` | string | No | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of filenames |
| `MATRIX_TYPE` | [MatrixTypeEnum](#matrixtype) | Yes | Type of data stored in matrix |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation, ran empty drops or doublet detection, used filter on # genes/cell, etc. scRNA-seq Level 4: dimensionality reduction with PCA and 50 components, nearest-neighbor graph with k = 20 and Leiden clustering with resolution = 1, UMAP visualization using 50 PCA components, marker genes used to annotate cell types, information about droplet matrix (all barcodes) to cell matrix (only informative barcodes representing real cells) conversion |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel3_4](#scrnaseqworkflowtypelevel3-4) | Yes | Generic name for the workflow used to analyze a data set |

