# WES

HTAN Whole Exome Sequencing Data Model Schema

## Classes in This Module

| Class | Level | Description |
|-------|-------|-------------|
| [BaseSequencingAttributes](#basesequencingattributes) | — | Minimal base attributes shared across all sequencing types |
| [BaseSequencingLevel1Attributes](#basesequencinglevel1attributes) | Level 1 | Level 1 attributes - sequencing run and library (raw data) |
| [BaseSequencingLevel2Attributes](#basesequencinglevel2attributes) | Level 2 | Level 2 attributes - alignment and alignment workflow |
| [BaseSequencingLevel3Attributes](#basesequencinglevel3attributes) | Level 3 | Level 3+ attributes - inherits alignment and workflow; used for processed/analysis levels |
| [BulkWESLevel1](#bulkweslevel1) | Level 1 | Bulk Whole Exome Sequencing Level 1 - Raw files |
| [BulkWESLevel2](#bulkweslevel2) | Level 2 | Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC |
| [BulkWESLevel3](#bulkweslevel3) | Level 3 | Bulk Whole Exome Sequencing Level 3 - Called variants and MSI analysis |
| [CoreFileAttributes](#corefileattributes) | — | Universal attributes that apply to all file-based data in HTAN |

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

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

## BulkWESLevel1

**Bulk Whole Exome Sequencing Level 1 - Raw files**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the raw sequencing file (fastq or fastq.gz) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.fastq for fastq; .fastq.gz or .fq.gz for fastq.gz) |
| `READ_INDICATOR` | string | No | Read indicator |
| `LIBRARY_SELECTION_METHOD` | [LibrarySelectionMethodEnum](enums.md#libraryselectionmethodenum) | Yes | Method used for library selection |
| `READ_LENGTH` | integer | Yes | Read length in base pairs |
| `TARGET_CAPTURE_KIT` | string | No | Target capture kit used |
| `LIBRARY_PREPARATION_KIT_NAME` | string | No | Name of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VENDOR` | string | No | Vendor of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VERSION` | string | No | Version of the library preparation kit |
| `ADAPTER_NAME` | string | No | Name of the adapter used |
| `ADAPTER_SEQUENCE` | string | No | Adapter sequence |
| `BASE_CALLER_NAME` | string | No | Name of the base caller |
| `BASE_CALLER_VERSION` | string | No | Version of the base caller |
| `FLOW_CELL_BARCODE` | string | No | Flow cell barcode |
| `FRAGMENT_MAXIMUM_LENGTH` | integer | No | Maximum fragment length |
| `FRAGMENT_MEAN_LENGTH` | integer | No | Mean fragment length |
| `FRAGMENT_MINIMUM_LENGTH` | integer | No | Minimum fragment length |
| `FRAGMENT_STANDARD_DEVIATION_LENGTH` | integer | No | Standard deviation of fragment length |
| `LANE_NUMBER` | integer | No | Lane number |
| `MULTIPLEX_BARCODE` | string | No | Multiplex barcode |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `SIZE_SELECTION_RANGE` | string | No | Size selection range |
| `TARGET_DEPTH` | integer | No | Target sequencing depth |
| `TO_TRIM_ADAPTER_SEQUENCE` | boolean | No | Whether to trim adapter sequence |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](enums.md#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](enums.md#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BulkWESLevel2

**Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the aligned file (bam or cram) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.bam for bam; .cram for cram) |
| `ALIGNMENT_WORKFLOW_TYPE` | string | Yes | Type of alignment workflow used |
| `INDEX_FILE_NAME` | string | No | Name of the index file |
| `AVERAGE_BASE_QUALITY` | float | No | Average base quality |
| `AVERAGE_INSERT_SIZE` | integer | No | Average insert size |
| `AVERAGE_READ_LENGTH` | integer | No | Average read length |
| `CONTAMINATION` | float | No | Contamination estimate |
| `CONTAMINATION_ERROR` | float | No | Contamination error estimate |
| `MEAN_COVERAGE` | float | Yes | Mean coverage depth |
| `ADAPTER_CONTENT` | string | No | Adapter content information |
| `BASIC_STATISTICS` | string | No | Basic statistics from QC |
| `ENCODING` | string | No | Encoding information |
| `OVERREPRESENTED_SEQUENCES` | string | No | Overrepresented sequences |
| `PER_BASE_N_CONTENT` | string | No | Per base N content |
| `PER_BASE_SEQUENCE_CONTENT` | string | No | Per base sequence content |
| `PER_BASE_SEQUENCE_QUALITY` | string | No | Per base sequence quality |
| `PER_SEQUENCE_GC_CONTENT` | string | No | Per sequence GC content |
| `PER_SEQUENCE_QUALITY_SCORE` | string | No | Per sequence quality score |
| `PER_TILE_SEQUENCE_QUALITY` | string | No | Per tile sequence quality |
| `PERCENT_GC_CONTENT` | float | No | Percent GC content |
| `SEQUENCE_DUPLICATION_LEVELS` | string | No | Sequence duplication levels |
| `SEQUENCE_LENGTH_DISTRIBUTION` | string | No | Sequence length distribution |
| `QC_WORKFLOW_TYPE` | string | No | QC workflow type |
| `QC_WORKFLOW_VERSION` | string | No | QC workflow version |
| `QC_WORKFLOW_LINK` | string | No | Link to QC workflow |
| `PAIRS_ON_DIFF_CHR` | integer | No | Number of read pairs on different chromosomes |
| `TOTAL_READS` | integer | Yes | Total number of reads |
| `TOTAL_UNIQUELY_MAPPED` | integer | Yes | Total number of uniquely mapped reads |
| `TOTAL_UNMAPPED_READS` | integer | Yes | Total number of unmapped reads |
| `PROPORTION_READS_DUPLICATED` | float | No | Proportion of duplicated reads |
| `PROPORTION_READS_MAPPED` | float | Yes | Proportion of mapped reads |
| `PROPORTION_TARGETS_NO_COVERAGE` | float | No | Proportion of targets with no coverage |
| `PROPORTION_BASE_MISMATCH` | float | No | Proportion of base mismatches |
| `SHORT_READS` | integer | No | Number of short reads |
| `PROPORTION_COVERAGE_10X` | float | No | Proportion of coverage at 10x |
| `PROPORTION_COVERAGE_30X` | float | No | Proportion of coverage at 30x |
| `IS_LOWEST_LEVEL` | boolean | No | Whether this is the lowest level |
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

## BulkWESLevel3

**Bulk Whole Exome Sequencing Level 3 - Called variants and MSI analysis**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the variant file (vcf or vcf.gz) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.vcf for vcf; .vcf.gz for vcf.gz) |
| `GERMLINE_VARIANTS_WORKFLOW_URL` | string | No | URL to the germline variants workflow |
| `GERMLINE_VARIANTS_WORKFLOW_TYPE` | string | No | Type of germline variants workflow |
| `SOMATIC_VARIANTS_WORKFLOW_URL` | string | No | URL to the somatic variants workflow |
| `SOMATIC_VARIANTS_WORKFLOW_TYPE` | string | No | Type of somatic variants workflow |
| `SOMATIC_VARIANTS_SAMPLE_TYPE` | [SomaticVariantsSampleTypeEnum](enums.md#somaticvariantssampletypeenum) | No | Type of sample for somatic variants |
| `STRUCTURAL_VARIANT_WORKFLOW_URL` | string | No | URL to the structural variant workflow |
| `STRUCTURAL_VARIANT_WORKFLOW_TYPE` | string | No | Type of structural variant workflow |
| `MSI_WORKFLOW_LINK` | string | No | Link to MSI workflow |
| `MSI_SCORE` | float | No | MSI score |
| `MSI_STATUS` | [MSIStatusEnum](enums.md#msistatusenum) | No | MSI status |
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

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| Paired-end | Paired-end sequencing |
| Single-end | Single-end sequencing |

### LibrarySelectionMethodEnum

| Value | Description |
|-------|-------------|
| Hybrid Selection | Hybrid selection method |
| PCR | PCR-based selection |
| RANDOM | Random selection |
| other | Other selection method |

### MSIStatusEnum

| Value | Description |
|-------|-------------|
| MSI-H | High microsatellite instability |
| MSI-L | Low microsatellite instability |
| MSS | Microsatellite stable |
| Unknown | Unknown MSI status |

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

### SomaticVariantsSampleTypeEnum

| Value | Description |
|-------|-------------|
| Metastatic | Metastatic tumor sample |
| Normal | Normal tissue sample |
| Other | Other sample type |
| Primary | Primary tumor sample |
| Recurrent | Recurrent tumor sample |
