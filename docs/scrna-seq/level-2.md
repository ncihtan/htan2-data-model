# scRNA-seq - Level 2

📥 [Download attributes as CSV](csv/scrna-seq-level-2.csv)

If submitting Level 2 files for scRNA-seq, here are the list of attributes you need to fill out:

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
| `CELL_BARCODE_TAG` | string | No | Tag used for cell barcodes |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel2](#scrnaseqworkflowtypeenumlevel2) | Yes | Generic name for the workflow used to analyze the dataset |
| `UMI_TAG` | string | No | Tag used for UMIs |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | string | No | Link to whitelist cell barcode file |

## Enums

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| `Paired-end` | Paired-end sequencing |
| `Single-end` | Single-end sequencing |

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

### scRNAseqWorkflowTypeEnumLevel2

| Value | Description |
|-------|-------------|
| `CellRanger` | CellRanger workflow |
| `HCA Optimus` | HCA Optimus workflow |
| `Other` | Other workflow |
| `SEQC` | SEQC workflow |
| `STARsolo` | STARsolo workflow |
| `Unknown` | Unknown workflow |
| `dropEST` | dropEST workflow |

