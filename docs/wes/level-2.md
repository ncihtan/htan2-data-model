# WES - Level 2

Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC

**Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC**

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

