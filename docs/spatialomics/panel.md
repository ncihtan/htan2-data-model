# SpatialOmics - Panel

📥 [Download attributes as CSV](csv/spatialomics-panel.csv)

If submitting Panel files for SpatialOmics, here are the list of attributes you need to fill out:

**Spatial omics panel information for targeted sequencing or protein panels**

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `GENE_ID` | string, pattern: <code>^(ENSG\d+\|\d+)$</code> | Yes | Stable Ensembl gene identifier (e.g., ENSG00000214114, ENSG00000121879). String matching ENSG\\d+ or digits |
| `GENE_SYMBOL` | string, pattern: <code>^[A-Za-z0-9_\-]+(@)?$</code> | Yes | HGNC-approved Gene symbol (e.g., MYC, PIK3C) |
| `HGNC_VERSION` | string, pattern: <code>^\d{4}-\d{2}-\d{2}$</code> | Yes | Version of the HGNC used, indicated with the date of the HGNC reference (e.g., 2025-08-01) |
| `HTAN_PANEL_ID` | string, pattern: <code>^(HTA([1-9]\|1[0-6]))_((EXT)?([0-9]\d*\|0000))_([0-9]\d*\|0000)$</code> | Yes | Unique identifier for the panel |
| `USER_GENE_NAME` | string | No | Optional user-defined name for the Gene |

