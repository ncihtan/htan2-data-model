# scRNA-seq - Level 2

HTAN scRNA-seq Level 2 Data Model - Workflow and processing metadata

**scRNA-seq Level 2 data - Workflow and processing metadata**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CELL_BARCODE_TAG` | string | No | Tag used for cell barcodes |
| `SCRNASEQ_WORKFLOW_TYPE` | [scRNAseqWorkflowTypeEnumLevel2](#scrnaseqworkflowtypelevel2) | Yes | Generic name for the workflow used to analyze the dataset |
| `UMI_TAG` | string | No | Tag used for UMIs |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | string | No | Link to whitelist cell barcode file |

