# scRNA-seq

HTAN scRNA-seq Data Model - Single-cell RNA sequencing data

<div class="grid cards" markdown>

-   **[BaseSequencingAttributes](#basesequencingattributes)**
    ---
    Minimal base attributes shared across all sequencing types

-   **[BaseSequencingLevel1Attributes](#basesequencinglevel1attributes)**
    ---
    _Level 1_ &nbsp; Level 1 attributes - sequencing run and library (raw data)

-   **[BaseSequencingLevel2Attributes](#basesequencinglevel2attributes)**
    ---
    _Level 2_ &nbsp; Level 2 attributes - alignment and alignment workflow

-   **[BaseSequencingLevel3Attributes](#basesequencinglevel3attributes)**
    ---
    _Level 3_ &nbsp; Level 3+ attributes - inherits alignment and workflow; used for processed/analysis levels

-   **[CoreFileAttributes](#corefileattributes)**
    ---
    Universal attributes that apply to all file-based data in HTAN

-   **[scRNALevel1](#scrnalevel1)**
    ---
    _Level 1_ &nbsp; scRNA-seq Level 1 data - Raw sequencing files and metadata

-   **[scRNALevel2](#scrnalevel2)**
    ---
    _Level 2_ &nbsp; scRNA-seq Level 2 data - Workflow and processing metadata

-   **[scRNALevel3and4](#scrnalevel3and4)**
    ---
    _Level 3_ &nbsp; Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships

</div>

## BaseSequencingAttributes

**Minimal base attributes shared across all sequencing types**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseSequencingLevel1Attributes

**Level 1 attributes - sequencing run and library (raw data)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseSequencingLevel2Attributes

**Level 2 attributes - alignment and alignment workflow**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](enums.md#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseSequencingLevel3Attributes

**Level 3+ attributes - inherits alignment and workflow; used for processed/analysis levels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](enums.md#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## scRNALevel1

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the raw sequencing file (fastq or fastq.gz) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.fastq for fastq; .fastq.gz or .fq.gz for fastq.gz) |
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](enums.md#singlecellisolationmethodenum) | Yes | Method used to isolate single cells |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](enums.md#dissociationmethodenum) | Yes | Method used to dissociate tissue into single cells |
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](enums.md#nucleicacidsourceenum) | Yes | Type of nucleic acid used for sequencing |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](enums.md#libraryconstructionmethodenum) | Yes | Method used to construct the sequencing library |
| `REVERSE_TRANSCRIPTION_PRIMER` | [ReverseTranscriptionPrimerEnum](enums.md#reversetranscriptionprimerenum) | Yes | Primer used for reverse transcription |
| `SPIKE_IN` | [SpikeInEnum](enums.md#spikeinenum) | Yes | Type of spike-in used, if any |
| `READ_INDICATOR` | [ReadIndicatorEnum](enums.md#readindicatorenum) | Yes | Type of read (forward, reverse, index) |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## scRNALevel2

**scRNA-seq Level 2 data - Workflow and processing metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the aligned file (bam or cram) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.bam for bam; .cram for cram) |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel2](enums.md#scrnaseqworkflowtypeenumlevel2) | Yes | Generic name for the workflow used to analyze the dataset |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | string | No | Link to whitelist cell barcode file |
| `CELL_BARCODE_TAG` | string | No | Tag used for cell barcodes |
| `UMI_TAG` | string | No | Tag used for UMIs |
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](enums.md#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## scRNALevel3and4

**Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the file (only h5ad files accepted for Level 3/4) |
| `FILENAME` | string | Yes | Name of the file. Must end with .h5ad extension |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel3and4](enums.md#scrnaseqworkflowtypeenumlevel3and4) | Yes | Generic name for the workflow used to analyze a data set |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation, ran empty drops or doublet detection, used filter on # genes/cell, etc. scRNA-seq Level 4: dimensionality reduction with PCA and 50 components, nearest-neighbor graph with k = 20 and Leiden clustering with resolution = 1, UMAP visualization using 50 PCA components, marker genes used to annotate cell types, information about droplet matrix (all barcodes) to cell matrix (only informative barcodes representing real cells) conversion |
| `DATA_CATEGORY` | [DataCategoryEnum](enums.md#datacategoryenum) | Yes | Specific content type of the data file |
| `MATRIX_TYPE` | [MatrixTypeEnum](enums.md#matrixtypeenum) | Yes | Type of data stored in matrix |
| `LINKED_MATRICES` | string | No | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of filenames |
| `CELL_MEDIAN_NUMBER_READS` | integer | Yes | Median number of reads per cell |
| `CELL_MEDIAN_NUMBER_GENES` | integer | Yes | Median number of genes detected per cell |
| `CELL_TOTAL` | integer | Yes | Number of sequenced cells. Applies to raw counts matrix only |
| `ANNDATA_SCHEMA_VERSION` | string | Yes | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | boolean | Yes | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](enums.md#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

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

### GenomicReferenceEnum

Genomic or transcriptomic reference assembly used for alignment

| Value | Description |
|-------|-------------|
| GRCh37 | Genome Reference Consortium human build 37 |
| GRCh37.p13 | GRCh37 patch release 13 |
| GRCh38 | Genome Reference Consortium human build 38 |
| GRCh38.p13 | GRCh38 patch release 13 |
| GRCh38.p14 | GRCh38 patch release 14 |
| hg19 | UCSC human genome reference hg19 |
| hg38 | UCSC human genome reference hg38 |

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
