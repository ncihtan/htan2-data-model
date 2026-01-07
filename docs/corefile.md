# Core

HTAN Core Data Model - Universal attributes shared across all file-based modules

## Classes

### CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Pattern | Description |
|-----------|------|----------|---------|-------------|
| `FILENAME` | string | Yes | `^.+[\\/]\S*$` | Name of the file |
| `FILE_FORMAT` | string | Yes |  | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$` | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_([BD][0-9]{1,20})$` | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

