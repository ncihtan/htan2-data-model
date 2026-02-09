# scRNA-seq

HTAN scRNA-seq Data Model - Single-cell RNA sequencing data

## BaseSequencingAttributes

**Base attributes shared across all sequencing types**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `GENOMIC_REFERENCE` | string | Yes | Genomic reference used for alignment |
| `GENOMIC_REFERENCE_URL` | string | No | URL to genomic reference |
| `GENOME_ANNOTATION_URL` | string | No | URL to genome annotation |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | No |  |
| `FILE_FORMAT` | string | No |  |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## scRNALevel1

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | No |  |
| `FILENAME` | string | No |  |
| `SINGLE_CELL_ISOLATION_METHOD` | SingleCellIsolationMethodEnum | Yes | Method used to isolate single cells |
| `DISSOCIATION_METHOD` | DissociationMethodEnum | Yes | Method used to dissociate tissue into single cells |
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `NUCLEIC_ACID_SOURCE` | NucleicAcidSourceEnum | Yes | Type of nucleic acid used for sequencing |
| `LIBRARY_CONSTRUCTION_METHOD` | LibraryConstructionMethodEnum | Yes | Method used to construct the sequencing library |
| `REVERSE_TRANSCRIPTION_PRIMER` | ReverseTranscriptionPrimerEnum | Yes | Primer used for reverse transcription |
| `SPIKE_IN` | SpikeInEnum | Yes | Type of spike-in used, if any |
| `READ_INDICATOR` | ReadIndicatorEnum | Yes | Type of read (forward, reverse, index) |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `GENOMIC_REFERENCE` | string | Yes | Genomic reference used for alignment |
| `GENOMIC_REFERENCE_URL` | string | No | URL to genomic reference |
| `GENOME_ANNOTATION_URL` | string | No | URL to genome annotation |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## scRNALevel2

**scRNA-seq Level 2 data - Workflow and processing metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | No |  |
| `FILENAME` | string | No |  |
| `SCRNASEQ_WORKFLOW_TYPE` | string | No |  |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | string | No | Link to whitelist cell barcode file |
| `CELL_BARCODE_TAG` | string | No | Tag used for cell barcodes |
| `UMI_TAG` | string | No | Tag used for UMIs |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `GENOMIC_REFERENCE` | string | Yes | Genomic reference used for alignment |
| `GENOMIC_REFERENCE_URL` | string | No | URL to genomic reference |
| `GENOME_ANNOTATION_URL` | string | No | URL to genome annotation |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | No |  |
| `FILE_FORMAT` | string | No |  |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## scRNALevel3and4

**Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | No |  |
| `FILENAME` | string | No |  |
| `SCRNASEQ_WORKFLOW_TYPE` | string | No |  |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation... |
| `DATA_CATEGORY` | DataCategoryEnum | Yes | Specific content type of the data file |
| `MATRIX_TYPE` | MatrixTypeEnum | Yes | Type of data stored in matrix |
| `LINKED_MATRICES` | string | No | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of... |
| `CELL_MEDIAN_NUMBER_READS` | integer | Yes | Median number of reads per cell |
| `CELL_MEDIAN_NUMBER_GENES` | integer | Yes | Median number of genes detected per cell |
| `CELL_TOTAL` | integer | Yes | Number of sequenced cells. Applies to raw counts matrix only |
| `ANNDATA_SCHEMA_VERSION` | string | Yes | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | boolean | Yes | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_LAYOUT` | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | SequencingPlatformEnum | Yes | Sequencing platform used |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `GENOMIC_REFERENCE` | string | Yes | Genomic reference used for alignment |
| `GENOMIC_REFERENCE_URL` | string | No | URL to genomic reference |
| `GENOME_ANNOTATION_URL` | string | No | URL to genome annotation |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B o... |

## scRNAseqData

**Root class for scRNA-seq data**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `level1_data` | scRNALevel1 | No | Level 1 scRNA-seq data |
| `level2_data` | scRNALevel2 | No | Level 2 scRNA-seq data |
| `level3_4_data` | scRNALevel3and4 | No | Level 3/4 scRNA-seq data |

## Enums

### DataCategoryEnum

| Value | Description |
|-------|-------------|
| Exon Expression Quantification | Exon expression quantification |
| Gene Expression | Gene expression data |
| Gene Expression Quantification | Gene expression quantification |
| Isoform Expression Quantification | Isoform expression quantification |
| Other | Other data category |
| Splice Junction Quantification | Splice junction quantification |
| Transcript Expression | Transcript expression data |

### DissociationMethodEnum

| Value | Description |
|-------|-------------|
| Enzymatic | Enzymatic dissociation method |
| Mechanical | Mechanical dissociation method |
| Other | Other dissociation method |
| Unknown | Unknown dissociation method |

### LibraryConstructionMethodEnum

| Value | Description |
|-------|-------------|
| 10X Genomics | 10X Genomics library construction method |
| Drop-seq | Drop-seq library construction method |
| Fluidigm C1 | Fluidigm C1 library construction method |
| InDrop | InDrop library construction method |
| Other | Other library construction method |
| Smart-seq | Smart-seq library construction method |
| Unknown | Unknown library construction method |

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| Paired-end | Paired-end sequencing |
| Single-end | Single-end sequencing |

### MatrixTypeEnum

| Value | Description |
|-------|-------------|
| Batch Corrected Counts | Batch corrected count matrix |
| Normalized Counts | Normalized count matrix |
| Raw Counts | Raw count matrix |
| Scaled Counts | Scaled count matrix |

### NucleicAcidSourceEnum

| Value | Description |
|-------|-------------|
| DNA | DNA nucleic acid source |
| RNA | RNA nucleic acid source |
| Unknown | Unknown nucleic acid source |

### ReadIndicatorEnum

| Value | Description |
|-------|-------------|
| Forward | Forward read indicator |
| Index | Index read indicator |
| Reverse | Reverse read indicator |
| Unknown | Unknown read indicator |

### ReverseTranscriptionPrimerEnum

| Value | Description |
|-------|-------------|
| Oligo-dT | Oligo-dT reverse transcription primer |
| Random Hexamer | Random hexamer reverse transcription primer |
| Unknown | Unknown reverse transcription primer |

### SequencingPlatformEnum

| Value | Description |
|-------|-------------|
| ABI_SOLID | ABI SOLID sequencing platform |
| BGISEQ | BGI sequencing platform |
| CAPILLARY | Capillary sequencing platform |
| COMPLETE_GENOMICS | Complete Genomics sequencing platform |
| HELICOS | Helicos sequencing platform |
| ILLUMINA | Illumina sequencing platform |
| ION_TORRENT | Ion Torrent sequencing platform |
| LS454 | 454 sequencing platform |
| OXFORD_NANOPORE | Oxford Nanopore sequencing platform |
| PACBIO_SMRT | PacBio SMRT sequencing platform |

### SingleCellIsolationMethodEnum

| Value | Description |
|-------|-------------|
| Cell Sorting | Cell sorting isolation method |
| Droplet-based | Droplet-based isolation method |
| Manual Picking | Manual picking isolation method |
| Microfluidics | Microfluidics isolation method |
| Other | Other isolation method |
| Unknown | Unknown isolation method |

### SpikeInEnum

| Value | Description |
|-------|-------------|
| ERCC | ERCC spike-in |
| None | No spike-in |
| Other | Other spike-in |
| Unknown | Unknown spike-in |

### scRNAseqWorkflowTypeEnumLevel2

| Value | Description |
|-------|-------------|
| CellRanger | CellRanger workflow |
| HCA Optimus | HCA Optimus workflow |
| Other | Other workflow |
| SEQC | SEQC workflow |
| STARsolo | STARsolo workflow |
| Unknown | Unknown workflow |
| dropEST | dropEST workflow |

### scRNAseqWorkflowTypeEnumLevel3and4

| Value | Description |
|-------|-------------|
| Cell annotation | Cell annotation workflow |
| CellRanger | 10x Genomics CellRanger workflow |
| Cufflinks | Cufflinks workflow |
| DEXSeq | DEXSeq workflow |
| Differentiation trajectory analysis | Differentiation trajectory analysis workflow |
| HCA Optimus | Human Cell Atlas Optimus workflow |
| HTSeq - FPKM | HTSeq FPKM workflow |
| Other | Other workflow type |
| SEQC | SEQC workflow |
| STARsolo | STARsolo alignment workflow |
| dropEST | dropEST workflow |
