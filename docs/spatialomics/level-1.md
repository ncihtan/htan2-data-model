# SpatialOmics - Level 1

📥 [Download attributes as CSV](csv/spatialomics-level-1.csv)

If submitting Level 1 files for SpatialOmics, here are the list of attributes you need to fill out:

**Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ASSAY_TYPE` | [AssayType](#assaytype) | Yes | Broad assay class (drives downstream conditionals) |
| `BUNDLE_CONTENTS` | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `FILE_FORMAT` | [FileFormatLevel1](#fileformatlevel1) | Yes | High-level package format of the bundle |
| `HAS_IMAGES` | boolean | Yes | Whether any image files (e.g., TIFFs) are included |
| `HAS_PROBE_SET` | boolean | Required IF ASSAY_TYPE = 'molecular barcoding' | Whether a targeted probe/gene panel is included |
| `HAS_REGISTRATION_FILES` | boolean | Yes | Whether any spatial registration transform files are included |
| `HAS_SEQUENCING` | boolean | No | If raw/aligned sequencing data is included |
| `IMAGE_TYPES` | [ImageType](#imagetype) | Required IF HAS_IMAGES = 'None' | Types of images provided |
| `PLATFORM` | [Platform](#platform) | Yes | Name of the platform used to generate the data |
| `SEQUENCING_FILE_TYPE` | [SequencingFileType](#sequencingfiletype) | Required IF HAS_SEQUENCING = 'None' | Sequencing file type |

## Enums

### AssayType

| Value | Description |
|-------|-------------|
| `in situ sequencing` | In situ sequencing assay type |
| `molecular barcoding` | Molecular barcoding assay type |
| `multi-omic sequencing` | Multi-omic sequencing assay type |
| `spot-based sequencing` | Spot-based sequencing assay type |

### FileFormatLevel1

| Value | Description |
|-------|-------------|
| `tar` | TAR archive format |
| `tar.gz` | TAR GZIP compressed archive format |
| `zip` | ZIP compressed archive format |

### ImageType

| Value | Description |
|-------|-------------|
| `DAPI` | DAPI (4',6-diamidino-2-phenylindole) image type |
| `H&E` | Hematoxylin and Eosin image type |
| `MIF` | Multiplex Immunofluorescence image type |
| `Other` | Other image type |

### Platform

| Value | Description |
|-------|-------------|
| `10x Genomics Visium` | 10x Genomics Visium platform |
| `10x Genomics Visium HD` | 10x Genomics Visium HD platform |
| `10x Genomics Xenium` | 10x Genomics Xenium platform |
| `Nanostring CosMX` | Nanostring CosMX platform |
| `STOmics Stereo-CITE` | STOmics Stereo-CITE platform |
| `STOmics Stereo-seq` | STOmics Stereo-seq platform |

### SequencingFileType

| Value | Description |
|-------|-------------|
| `BAM` | BAM alignment file format |
| `FASTQ` | FASTQ sequencing file format |

