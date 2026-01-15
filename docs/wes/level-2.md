# WES - Level 2

📥 [Download attributes as CSV](csv/wes-level-2.csv)

If submitting Level 2 files for WES, here are the list of attributes you need to fill out:

**Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
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
| `ADAPTER_CONTENT` | string | No | Adapter content information |
| `ALIGNMENT_WORKFLOW_TYPE` | string | Yes | Type of alignment workflow used |
| `AVERAGE_BASE_QUALITY` | float | No | Average base quality |
| `AVERAGE_INSERT_SIZE` | integer | No | Average insert size |
| `AVERAGE_READ_LENGTH` | integer | No | Average read length |
| `BASIC_STATISTICS` | string | No | Basic statistics from QC |
| `CONTAMINATION` | float | No | Contamination estimate |
| `CONTAMINATION_ERROR` | float | No | Contamination error estimate |
| `ENCODING` | string | No | Encoding information |
| `INDEX_FILE_NAME` | string | No | Name of the index file |
| `IS_LOWEST_LEVEL` | boolean | No | Whether this is the lowest level |
| `MEAN_COVERAGE` | float | Yes | Mean coverage depth |
| `OVERREPRESENTED_SEQUENCES` | string | No | Overrepresented sequences |
| `PAIRS_ON_DIFF_CHR` | integer | No | Number of read pairs on different chromosomes |
| `PERCENT_GC_CONTENT` | float | No | Percent GC content |
| `PER_BASE_N_CONTENT` | string | No | Per base N content |
| `PER_BASE_SEQUENCE_CONTENT` | string | No | Per base sequence content |
| `PER_BASE_SEQUENCE_QUALITY` | string | No | Per base sequence quality |
| `PER_SEQUENCE_GC_CONTENT` | string | No | Per sequence GC content |
| `PER_SEQUENCE_QUALITY_SCORE` | string | No | Per sequence quality score |
| `PER_TILE_SEQUENCE_QUALITY` | string | No | Per tile sequence quality |
| `PROPORTION_BASE_MISMATCH` | float | No | Proportion of base mismatches |
| `PROPORTION_COVERAGE_10X` | float | No | Proportion of coverage at 10x |
| `PROPORTION_COVERAGE_30X` | float | No | Proportion of coverage at 30x |
| `PROPORTION_READS_DUPLICATED` | float | No | Proportion of duplicated reads |
| `PROPORTION_READS_MAPPED` | float | Yes | Proportion of mapped reads |
| `PROPORTION_TARGETS_NO_COVERAGE` | float | No | Proportion of targets with no coverage |
| `QC_WORKFLOW_LINK` | string | No | Link to QC workflow |
| `QC_WORKFLOW_TYPE` | string | No | QC workflow type |
| `QC_WORKFLOW_VERSION` | string | No | QC workflow version |
| `SEQUENCE_DUPLICATION_LEVELS` | string | No | Sequence duplication levels |
| `SEQUENCE_LENGTH_DISTRIBUTION` | string | No | Sequence length distribution |
| `SHORT_READS` | integer | No | Number of short reads |
| `TOTAL_READS` | integer | Yes | Total number of reads |
| `TOTAL_UNIQUELY_MAPPED` | integer | Yes | Total number of uniquely mapped reads |
| `TOTAL_UNMAPPED_READS` | integer | Yes | Total number of unmapped reads |

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

