# WES - Level 3

If submitting Level 3 files for WES, here are the list of attributes you need to fill out:

**Bulk Whole Exome Sequencing Level 3 - Called variants and MSI analysis**

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
| `GERMLINE_VARIANTS_WORKFLOW_TYPE` | string | No | Type of germline variants workflow |
| `GERMLINE_VARIANTS_WORKFLOW_URL` | string | No | URL to the germline variants workflow |
| `MSI_SCORE` | float | No | MSI score |
| `MSI_STATUS` | [MSIStatusEnum](#msistatusenum) | No | MSI status |
| `MSI_WORKFLOW_LINK` | string | No | Link to MSI workflow |
| `SOMATIC_VARIANTS_SAMPLE_TYPE` | [SomaticVariantsSampleTypeEnum](#somaticvariantssampletypeenum) | No | Type of sample for somatic variants |
| `SOMATIC_VARIANTS_WORKFLOW_TYPE` | string | No | Type of somatic variants workflow |
| `SOMATIC_VARIANTS_WORKFLOW_URL` | string | No | URL to the somatic variants workflow |
| `STRUCTURAL_VARIANT_WORKFLOW_TYPE` | string | No | Type of structural variant workflow |
| `STRUCTURAL_VARIANT_WORKFLOW_URL` | string | No | URL to the structural variant workflow |

## Enums

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| `Paired-end` | Paired-end sequencing |
| `Single-end` | Single-end sequencing |

### MSIStatusEnum

| Value | Description |
|-------|-------------|
| `MSI-H` | High microsatellite instability |
| `MSI-L` | Low microsatellite instability |
| `MSS` | Microsatellite stable |
| `Unknown` | Unknown MSI status |

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

### SomaticVariantsSampleTypeEnum

| Value | Description |
|-------|-------------|
| `Metastatic` | Metastatic tumor sample |
| `Normal` | Normal tissue sample |
| `Other` | Other sample type |
| `Primary` | Primary tumor sample |
| `Recurrent` | Recurrent tumor sample |

