# WES - Level 1

Bulk Whole Exome Sequencing Level 1 - Raw files

**Bulk Whole Exome Sequencing Level 1 - Raw files**

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

