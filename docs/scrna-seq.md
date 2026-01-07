# scRNA-seq

HTAN scRNA-seq Data Model - Single-cell RNA sequencing data

## Classes

### scRNALevel1

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
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
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](#dissociationmethod) | Yes | Method used to dissociate tissue into single cells |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](#libraryconstructionmethod) | Yes | Method used to construct the sequencing library |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](#nucleicacidsource) | Yes | Type of nucleic acid used for sequencing |
| `READ_INDICATOR` | [ReadIndicatorEnum](#readindicator) | Yes | Type of read (forward, reverse, index) |
| `REVERSE_TRANSCRIPTION_PRIMER` | [ReverseTranscriptionPrimerEnum](#reversetranscriptionprimer) | Yes | Primer used for reverse transcription |
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](#singlecellisolationmethod) | Yes | Method used to isolate single cells |
| `SPIKE_IN` | [SpikeInEnum](#spikein) | Yes | Type of spike-in used, if any |

### scRNALevel2

**scRNA-seq Level 2 data - Workflow and processing metadata**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
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
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CELL_BARCODE_TAG` | string | No | Tag used for cell barcodes |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel2](#scrnaseqworkflowtypelevel2) | Yes | Generic name for the workflow used to analyze the dataset |
| `UMI_TAG` | string | No | Tag used for UMIs |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | string | No | Link to whitelist cell barcode file |

### scRNALevel3_4

**Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
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
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
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
| `DATA_CATEGORY` | [DataCategoryEnum](#datacategory) | Yes | Specific content type of the data file |
| `FILE_FORMAT` | string, pattern: <code>^h5ad$</code> | Yes | Format of the file (only h5ad files accepted for Level 3/4) |
| `LINKED_MATRICES` | string | No | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of filenames |
| `MATRIX_TYPE` | [MatrixTypeEnum](#matrixtype) | Yes | Type of data stored in matrix |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation, ran empty drops or doublet detection, used filter on # genes/cell, etc. scRNA-seq Level 4: dimensionality reduction with PCA and 50 components, nearest-neighbor graph with k = 20 and Leiden clustering with resolution = 1, UMAP visualization using 50 PCA components, marker genes used to annotate cell types, information about droplet matrix (all barcodes) to cell matrix (only informative barcodes representing real cells) conversion |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel3_4](#scrnaseqworkflowtypelevel3-4) | Yes | Generic name for the workflow used to analyze a data set |

### scRNAseqData

**Root class for scRNA-seq data**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `level1_data` | scRNALevel1 | No | Level 1 scRNA-seq data |
| `level2_data` | scRNALevel2 | No | Level 2 scRNA-seq data |
| `level3_4_data` | scRNALevel3_4 | No | Level 3/4 scRNA-seq data |

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

