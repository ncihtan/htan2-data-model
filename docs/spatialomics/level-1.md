# SpatialOmics - Level 1

If submitting Level 1 files for SpatialOmics, here are the list of attributes you need to fill out:

**Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
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

