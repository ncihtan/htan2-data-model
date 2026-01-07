# scRNA-seq

HTAN scRNA-seq Data Model - Single-cell RNA sequencing data

## Classes

### scRNALevel1

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No |  | Whether cells were cryopreserved in the sample |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](#dissociationmethod) | Yes |  | Method used to dissociate tissue into single cells |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](#libraryconstructionmethod) | Yes |  | Method used to construct the sequencing library |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](#nucleicacidsource) | Yes |  | Type of nucleic acid used for sequencing |
| `READ_INDICATOR` | [ReadIndicatorEnum](#readindicator) | Yes |  | Type of read (forward, reverse, index) |
| `REVERSE_TRANSCRIPTION_PRIMER` | [ReverseTranscriptionPrimerEnum](#reversetranscriptionprimer) | Yes |  | Primer used for reverse transcription |
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](#singlecellisolationmethod) | Yes |  | Method used to isolate single cells |
| `SPIKE_IN` | [SpikeInEnum](#spikein) | Yes |  | Type of spike-in used, if any |

### scRNALevel2

**scRNA-seq Level 2 data - Workflow and processing metadata**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `CELL_BARCODE_TAG` | string | No |  | Tag used for cell barcodes |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel2](#scrnaseqworkflowtypelevel2) | Yes |  | Generic name for the workflow used to analyze the dataset |
| `UMI_TAG` | string | No |  | Tag used for UMIs |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | string | No |  | Link to whitelist cell barcode file |

### scRNALevel3_4

**Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `ANNDATA_SCHEMA_VERSION` | string | Yes | `^0\.1$` | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | boolean | Yes |  | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `CELL_MEDIAN_NUMBER_GENES` | integer | Yes |  | Median number of genes detected per cell |
| `CELL_MEDIAN_NUMBER_READS` | integer | Yes |  | Median number of reads per cell |
| `CELL_TOTAL` | integer | Yes |  | Number of sequenced cells. Applies to raw counts matrix only |
| `DATA_CATEGORY` | [DataCategoryEnum](#datacategory) | Yes |  | Specific content type of the data file |
| `FILE_FORMAT` | string | Yes | `^h5ad$` | Format of the file (only h5ad files accepted for Level 3/4) |
| `LINKED_MATRICES` | string | No |  | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of filenames |
| `MATRIX_TYPE` | [MatrixTypeEnum](#matrixtype) | Yes |  | Type of data stored in matrix |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes |  | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation, ran empty drops or doublet detection, used filter on # genes/cell, etc. scRNA-seq Level 4: dimensionality reduction with PCA and 50 components, nearest-neighbor graph with k = 20 and Leiden clustering with resolution = 1, UMAP visualization using 50 PCA components, marker genes used to annotate cell types, information about droplet matrix (all barcodes) to cell matrix (only informative barcodes representing real cells) conversion |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel3_4](#scrnaseqworkflowtypelevel3-4) | Yes |  | Generic name for the workflow used to analyze a data set |

### scRNAseqData

**Root class for scRNA-seq data**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `level1_data` | scRNALevel1 | No |  | Level 1 scRNA-seq data |
| `level2_data` | scRNALevel2 | No |  | Level 2 scRNA-seq data |
| `level3_4_data` | scRNALevel3_4 | No |  | Level 3/4 scRNA-seq data |

## Enums

### DataCategoryEnum {#datacategory}

| Value | Description |
|-------|-------------|
| `Exon Expression Quantification` | Exon expression quantification |
| `Gene Expression` | Gene expression data |
| `Gene Expression Quantification` | Gene expression quantification |
| `Isoform Expression Quantification` | Isoform expression quantification |
| `Other` | Other data category |
| `Splice Junction Quantification` | Splice junction quantification |
| `Transcript Expression` | Transcript expression data |

### LibraryConstructionMethodEnum {#libraryconstructionmethod}

| Value | Description |
|-------|-------------|
| `10X Genomics` | 10X Genomics library construction method |
| `Drop-seq` | Drop-seq library construction method |
| `Fluidigm C1` | Fluidigm C1 library construction method |
| `InDrop` | InDrop library construction method |
| `Other` | Other library construction method |
| `Smart-seq` | Smart-seq library construction method |
| `Unknown` | Unknown library construction method |

### SingleCellIsolationMethodEnum {#singlecellisolationmethod}

| Value | Description |
|-------|-------------|
| `Cell Sorting` | Cell sorting isolation method |
| `Droplet-based` | Droplet-based isolation method |
| `Manual Picking` | Manual picking isolation method |
| `Microfluidics` | Microfluidics isolation method |
| `Other` | Other isolation method |
| `Unknown` | Unknown isolation method |

### scRNAseqWorkflowTypeEnumLevel2 {#scrnaseqworkflowtypelevel2}

| Value | Description |
|-------|-------------|
| `CellRanger` | CellRanger workflow |
| `HCA Optimus` | HCA Optimus workflow |
| `Other` | Other workflow |
| `SEQC` | SEQC workflow |
| `STARsolo` | STARsolo workflow |
| `Unknown` | Unknown workflow |
| `dropEST` | dropEST workflow |

### scRNAseqWorkflowTypeEnumLevel3_4 {#scrnaseqworkflowtypelevel3-4}

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

