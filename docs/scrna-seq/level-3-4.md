# scRNA-seq - Level 3/4

📥 [Download attributes as CSV](csv/scrna-seq-level-3-4.csv)

If submitting Level 3/4 files for scRNA-seq, here are the list of attributes you need to fill out:

**Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### Base Sequencing Attributes

These attributes are inherited from BaseSequencingAttributes.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `GENOME_ANNOTATION_URL` | string | No | URL to genome annotation |
| `GENOMIC_REFERENCE` | string | Yes | Genomic reference used for alignment |
| `GENOMIC_REFERENCE_URL` | string | No | URL to genomic reference |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ANNDATA_SCHEMA_VERSION` | string, pattern: <code>^0\.1$</code> | Yes | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | boolean | Yes | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `CELL_MEDIAN_NUMBER_GENES` | integer | Yes | Median number of genes detected per cell |
| `CELL_MEDIAN_NUMBER_READS` | integer | Yes | Median number of reads per cell |
| `CELL_TOTAL` | integer | Yes | Number of sequenced cells. Applies to raw counts matrix only |
| `DATA_CATEGORY` | [DataCategoryEnum](#datacategoryenum) | Yes | Specific content type of the data file |
| `FILE_FORMAT` | string, pattern: <code>^h5ad$</code> | Yes | Format of the file (only h5ad files accepted for Level 3/4) |
| `LINKED_MATRICES` | string | No | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of filenames |
| `MATRIX_TYPE` | [MatrixTypeEnum](#matrixtypeenum) | Yes | Type of data stored in matrix |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation, ran empty drops or doublet detection, used filter on # genes/cell, etc. scRNA-seq Level 4: dimensionality reduction with PCA and 50 components, nearest-neighbor graph with k = 20 and Leiden clustering with resolution = 1, UMAP visualization using 50 PCA components, marker genes used to annotate cell types, information about droplet matrix (all barcodes) to cell matrix (only informative barcodes representing real cells) conversion |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel3_4](#scrnaseqworkflowtypeenumlevel3-4) | Yes | Generic name for the workflow used to analyze a data set |

## Enums

### DataCategoryEnum

| Value | Description |
|-------|-------------|
| `Exon Expression Quantification` | Exon expression quantification |
| `Gene Expression` | Gene expression data |
| `Gene Expression Quantification` | Gene expression quantification |
| `Isoform Expression Quantification` | Isoform expression quantification |
| `Other` | Other data category |
| `Splice Junction Quantification` | Splice junction quantification |
| `Transcript Expression` | Transcript expression data |

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| `Paired-end` | Paired-end sequencing |
| `Single-end` | Single-end sequencing |

### MatrixTypeEnum

| Value | Description |
|-------|-------------|
| `Batch Corrected Counts` | Batch corrected count matrix |
| `Normalized Counts` | Normalized count matrix |
| `Raw Counts` | Raw count matrix |
| `Scaled Counts` | Scaled count matrix |

### SequencingPlatformEnum

| Value | Description |
|-------|-------------|
| `ABI_SOLID` | ABI SOLID sequencing platform |
| `BGISEQ` | BGI sequencing platform |
| `CAPILLARY` | Capillary sequencing platform |
| `COMPLETE_GENOMICS` | Complete Genomics sequencing platform |
| `HELICOS` | Helicos sequencing platform |
| `ILLUMINA` | Illumina sequencing platform |
| `ION_TORRENT` | Ion Torrent sequencing platform |
| `LS454` | 454 sequencing platform |
| `OXFORD_NANOPORE` | Oxford Nanopore sequencing platform |
| `PACBIO_SMRT` | PacBio SMRT sequencing platform |

### scRNAseqWorkflowTypeEnumLevel3_4

| Value | Description |
|-------|-------------|
| `Cell annotation` | Cell annotation workflow |
| `CellRanger` | 10x Genomics CellRanger workflow |
| `Cufflinks` | Cufflinks workflow |
| `DEXSeq` | DEXSeq workflow |
| `Differentiation trajectory analysis` | Differentiation trajectory analysis workflow |
| `HCA Optimus` | Human Cell Atlas Optimus workflow |
| `HTSeq - FPKM` | HTSeq FPKM workflow |
| `Other` | Other workflow type |
| `SEQC` | SEQC workflow |
| `STARsolo` | STARsolo alignment workflow |
| `dropEST` | dropEST workflow |

