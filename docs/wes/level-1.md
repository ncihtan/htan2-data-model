# WES - Level 1

If submitting Level 1 files for WES, here are the list of attributes you need to fill out:

**Bulk Whole Exome Sequencing Level 1 - Raw files**

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
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayout) | Yes | Library layout (paired-end or single-end) |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatform) | Yes | Sequencing platform used |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
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
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `LIBRARY_PREPARATION_KIT_NAME` | string | No | Name of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VENDOR` | string | No | Vendor of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VERSION` | string | No | Version of the library preparation kit |
| `LIBRARY_SELECTION_METHOD` | [LibrarySelectionMethodEnum](#libraryselectionmethod) | Yes | Method used for library selection |
| `MULTIPLEX_BARCODE` | string | No | Multiplex barcode |
| `READ_INDICATOR` | string | No | Read indicator |
| `READ_LENGTH` | integer | Yes | Read length in base pairs |
| `SIZE_SELECTION_RANGE` | string | No | Size selection range |
| `TARGET_CAPTURE_KIT` | string | No | Target capture kit used |
| `TARGET_DEPTH` | integer | No | Target sequencing depth |
| `TO_TRIM_ADAPTER_SEQUENCE` | boolean | No | Whether to trim adapter sequence |

