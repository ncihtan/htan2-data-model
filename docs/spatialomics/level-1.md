# SpatialOmics - Level 1

HTAN Spatial Omics Level 1 - Raw spatial data bundle (optional)

**Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files**

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

