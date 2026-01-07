# WES

HTAN Whole Exome Sequencing Data Model Schema

## Levels

### Level 1 (BulkWESLevel1)

Bulk Whole Exome Sequencing Level 1 - Raw files

**Bulk Whole Exome Sequencing Level 1 - Raw files**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `ADAPTER_NAME` | string | No |  | Name of the adapter used |
| `ADAPTER_SEQUENCE` | string | No |  | Adapter sequence |
| `BASE_CALLER_NAME` | string | No |  | Name of the base caller |
| `BASE_CALLER_VERSION` | string | No |  | Version of the base caller |
| `FLOW_CELL_BARCODE` | string | No |  | Flow cell barcode |
| `FRAGMENT_MAXIMUM_LENGTH` | integer | No |  | Maximum fragment length |
| `FRAGMENT_MEAN_LENGTH` | integer | No |  | Mean fragment length |
| `FRAGMENT_MINIMUM_LENGTH` | integer | No |  | Minimum fragment length |
| `FRAGMENT_STANDARD_DEVIATION_LENGTH` | integer | No |  | Standard deviation of fragment length |
| `LANE_NUMBER` | integer | No |  | Lane number |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No |  | Days from index for library preparation |
| `LIBRARY_PREPARATION_KIT_NAME` | string | No |  | Name of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VENDOR` | string | No |  | Vendor of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VERSION` | string | No |  | Version of the library preparation kit |
| `LIBRARY_SELECTION_METHOD` | [LibrarySelectionMethodEnum](#libraryselectionmethod) | Yes |  | Method used for library selection |
| `MULTIPLEX_BARCODE` | string | No |  | Multiplex barcode |
| `READ_INDICATOR` | string | No |  | Read indicator |
| `READ_LENGTH` | integer | Yes |  | Read length in base pairs |
| `SIZE_SELECTION_RANGE` | string | No |  | Size selection range |
| `TARGET_CAPTURE_KIT` | string | No |  | Target capture kit used |
| `TARGET_DEPTH` | integer | No |  | Target sequencing depth |
| `TO_TRIM_ADAPTER_SEQUENCE` | boolean | No |  | Whether to trim adapter sequence |

### Level 2 (BulkWESLevel2)

Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC

**Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `ADAPTER_CONTENT` | string | No |  | Adapter content information |
| `ALIGNMENT_WORKFLOW_TYPE` | string | Yes |  | Type of alignment workflow used |
| `AVERAGE_BASE_QUALITY` | float | No |  | Average base quality |
| `AVERAGE_INSERT_SIZE` | integer | No |  | Average insert size |
| `AVERAGE_READ_LENGTH` | integer | No |  | Average read length |
| `BASIC_STATISTICS` | string | No |  | Basic statistics from QC |
| `CONTAMINATION` | float | No |  | Contamination estimate |
| `CONTAMINATION_ERROR` | float | No |  | Contamination error estimate |
| `ENCODING` | string | No |  | Encoding information |
| `INDEX_FILE_NAME` | string | No |  | Name of the index file |
| `IS_LOWEST_LEVEL` | boolean | No |  | Whether this is the lowest level |
| `MEAN_COVERAGE` | float | Yes |  | Mean coverage depth |
| `OVERREPRESENTED_SEQUENCES` | string | No |  | Overrepresented sequences |
| `PAIRS_ON_DIFF_CHR` | integer | No |  | Number of read pairs on different chromosomes |
| `PERCENT_GC_CONTENT` | float | No |  | Percent GC content |
| `PER_BASE_N_CONTENT` | string | No |  | Per base N content |
| `PER_BASE_SEQUENCE_CONTENT` | string | No |  | Per base sequence content |
| `PER_BASE_SEQUENCE_QUALITY` | string | No |  | Per base sequence quality |
| `PER_SEQUENCE_GC_CONTENT` | string | No |  | Per sequence GC content |
| `PER_SEQUENCE_QUALITY_SCORE` | string | No |  | Per sequence quality score |
| `PER_TILE_SEQUENCE_QUALITY` | string | No |  | Per tile sequence quality |
| `PROPORTION_BASE_MISMATCH` | float | No |  | Proportion of base mismatches |
| `PROPORTION_COVERAGE_10X` | float | No |  | Proportion of coverage at 10x |
| `PROPORTION_COVERAGE_30X` | float | No |  | Proportion of coverage at 30x |
| `PROPORTION_READS_DUPLICATED` | float | No |  | Proportion of duplicated reads |
| `PROPORTION_READS_MAPPED` | float | Yes |  | Proportion of mapped reads |
| `PROPORTION_TARGETS_NO_COVERAGE` | float | No |  | Proportion of targets with no coverage |
| `QC_WORKFLOW_LINK` | string | No |  | Link to QC workflow |
| `QC_WORKFLOW_TYPE` | string | No |  | QC workflow type |
| `QC_WORKFLOW_VERSION` | string | No |  | QC workflow version |
| `SEQUENCE_DUPLICATION_LEVELS` | string | No |  | Sequence duplication levels |
| `SEQUENCE_LENGTH_DISTRIBUTION` | string | No |  | Sequence length distribution |
| `SHORT_READS` | integer | No |  | Number of short reads |
| `TOTAL_READS` | integer | Yes |  | Total number of reads |
| `TOTAL_UNIQUELY_MAPPED` | integer | Yes |  | Total number of uniquely mapped reads |
| `TOTAL_UNMAPPED_READS` | integer | Yes |  | Total number of unmapped reads |

### Level 3 (BulkWESLevel3)

Bulk Whole Exome Sequencing Level 3 - Called variants and MSI analysis

**Bulk Whole Exome Sequencing Level 3 - Called variants and MSI analysis**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `GERMLINE_VARIANTS_WORKFLOW_TYPE` | string | No |  | Type of germline variants workflow |
| `GERMLINE_VARIANTS_WORKFLOW_URL` | string | No |  | URL to the germline variants workflow |
| `MSI_SCORE` | float | No |  | MSI score |
| `MSI_STATUS` | [MSIStatusEnum](#msistatus) | No |  | MSI status |
| `MSI_WORKFLOW_LINK` | string | No |  | Link to MSI workflow |
| `SOMATIC_VARIANTS_SAMPLE_TYPE` | [SomaticVariantsSampleTypeEnum](#somaticvariantssampletype) | No |  | Type of sample for somatic variants |
| `SOMATIC_VARIANTS_WORKFLOW_TYPE` | string | No |  | Type of somatic variants workflow |
| `SOMATIC_VARIANTS_WORKFLOW_URL` | string | No |  | URL to the somatic variants workflow |
| `STRUCTURAL_VARIANT_WORKFLOW_TYPE` | string | No |  | Type of structural variant workflow |
| `STRUCTURAL_VARIANT_WORKFLOW_URL` | string | No |  | URL to the structural variant workflow |

