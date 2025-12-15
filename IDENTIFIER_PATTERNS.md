# HTAN Data Model - Identifier Regex Patterns

This document lists all identifier and validation regex patterns used across the HTAN data model.

## HTAN Identifiers

### HTAN Data File ID
**Location**: `modules/CoreFile/domains/core.yaml` (inherited by all file-based modules)
- **Attribute**: `HTAN_DATA_FILE_ID`
- **Pattern**: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$`
- **Description**: Primary key for all data files. Supports HTA200-229 for phase 2. Total length max 50 characters.
- **Examples**: 
  - `HTA200_2_D36667`
  - `HTA200_EXT001_D123`
  - `HTA229_0000_D1`

### HTAN Biospecimen ID
**Location**: `modules/Biospecimen/domains/biospecimen.yaml`
- **Attribute**: `HTAN_BIOSPECIMEN_ID`
- **Pattern**: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(B[0-9]{1,20})$`
- **Description**: Primary key for biospecimen records. Supports HTA200-229 for phase 2. Total length max 50 characters.
- **Examples**: 
  - `HTA200_2_B7001`
  - `HTA200_EXT001_B123`
  - `HTA229_0000_B1`

### HTAN Participant ID
**Location**: `modules/Clinical/domains/clinical.yaml`
- **Attribute**: `HTAN_PARTICIPANT_ID`
- **Pattern**: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})$`
- **Description**: Primary key for participant/patient records. Supports HTA200-229 for phase 2. Total length max 50 characters.
- **Examples**: 
  - `HTA200_2`
  - `HTA200_EXT001`
  - `HTA229_0000`

### HTAN Panel ID
**Location**: `modules/SpatialOmics/domains/spatial_panel.yaml`
- **Attribute**: `HTAN_PANEL_ID`
- **Pattern**: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$`
- **Description**: Unique identifier for spatial omics panels
- **Examples**: 
  - `HTA200_2_P0001`
  - `HTA200_EXT001_P0001`

### HTAN Parent ID (File-based modules)
**Location**: `modules/CoreFile/domains/core.yaml` (inherited by all file-based modules)
- **Attribute**: `HTAN_PARENT_ID`
- **Pattern**: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_([BD][0-9]{1,20})$`
- **Description**: Foreign key to parent entity (B for Biospecimen, D for data file). Supports HTA200-229 for phase 2. Total length max 50 characters.
- **Examples**: 
  - `HTA200_2_B7001` (biospecimen with B suffix)
  - `HTA200_2_D36667` (data file with D suffix)
  - `HTA229_0000_B1`
  - `HTA200_EXT001_D123`

### HTAN Parent ID (Biospecimen module)
**Location**: `modules/Biospecimen/domains/biospecimen.yaml`
- **Attribute**: `HTAN_PARENT_ID`
- **Pattern**: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})(?:_(B[0-9]{1,20}))?$`
- **Description**: Foreign key to parent entity (Participant ID or Biospecimen ID with B suffix). Supports HTA200-229 for phase 2. Total length max 50 characters.
- **Examples**: 
  - `HTA200_2` (participant ID)
  - `HTA200_2_B7001` (biospecimen ID with B suffix)
  - `HTA229_EXT001_B123`

## External Identifiers

### Synapse ID
**Location**: 
- `modules/SpatialOmics/domains/level_3.yaml` (PANEL_SYNAPSE_ID)
- `modules/MultiplexMicroscopy/domains/level_2.yaml` (CHANNEL_METADATA_ID)
- **Pattern**: `^syn\d+$`
- **Description**: Synapse platform identifier
- **Examples**: 
  - `syn123456`
  - `syn9876543`

### Ensembl Gene ID
**Location**: `modules/SpatialOmics/domains/spatial_panel.yaml`
- **Attribute**: `GENE_ID`
- **Pattern**: `^(ENSG\d+|\d+)$`
- **Description**: Stable Ensembl gene identifier or numeric ID
- **Examples**: 
  - `ENSG00000214114`
  - `ENSG00000121879`
  - `12345` (numeric ID)

### HGNC Version
**Location**: `modules/SpatialOmics/domains/spatial_panel.yaml`
- **Attribute**: `HGNC_VERSION`
- **Pattern**: `^\d{4}-\d{2}-\d{2}$`
- **Description**: Version of the HGNC used, indicated with the date (YYYY-MM-DD format)
- **Examples**: 
  - `2025-08-01`
  - `2024-12-15`

### RRID (Research Resource Identifier) - Antibody
**Location**: `modules/MultiplexMicroscopy/domains/multiplex_microscopy_channel_metadata.yaml`
- **Attribute**: `ANTIBODY_RRID`
- **Pattern**: `^RRID:AB_\d+$`
- **Description**: Research Resource Identifier for antibodies
- **Examples**: 
  - `RRID:AB_123456`
  - `RRID:AB_987654`

## URL Patterns

### HTTP/HTTPS URL (General)
**Location**: 
- `modules/SpatialOmics/domains/level_3.yaml` (PROTOCOL_URL)
- `modules/Imaging/domains/imaging.yaml` (CITATION_OR_DOI, IMAGING_PROTOCOL)
- **Pattern**: `^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$`
- **Description**: Validates HTTP/HTTPS URLs, excluding private IP ranges (10.x.x.x, 127.x.x.x, 169.254.x.x, 192.168.x.x, 172.16-31.x.x)
- **Examples**: 
  - `https://protocols.io/view/my-protocol`
  - `http://example.com/path?query=value`
  - `https://doi.org/10.1234/example`

## File Format Patterns

### Filename
**Location**: `modules/CoreFile/domains/core.yaml` (inherited by all file-based modules)
- **Attribute**: `FILENAME`
- **Pattern**: `^.+[\\/]\S*$`
- **Description**: File path with directory separator
- **Examples**: 
  - `data/file.txt`
  - `path/to/file.fastq.gz`

### File Format Patterns (Module-specific)
These are typically enforced via enums rather than regex, but some modules use patterns:

#### Level 4 File Format (MultiplexMicroscopy)
**Location**: `modules/MultiplexMicroscopy/domains/level_4.yaml`
- **Attribute**: `FILE_FORMAT`
- **Pattern**: `^(csv|h5ad)$`

#### Level 3 File Format (MultiplexMicroscopy)
**Location**: `modules/MultiplexMicroscopy/domains/level_3.yaml`
- **Attribute**: `FILE_FORMAT`
- **Pattern**: `^(ome-tiff|ome\.tiff|tiff|tif)$`

#### Level 2 File Format (MultiplexMicroscopy)
**Location**: `modules/MultiplexMicroscopy/domains/level_2.yaml`
- **Attribute**: `FILE_FORMAT`
- **Pattern**: `^(ome-tiff|tiff|qptiff|svs)$`

#### Digital Pathology File Format
**Location**: `modules/DigitalPathology/domains/digital_pathology.yaml`
- **Attribute**: `FILE_FORMAT`
- **Pattern**: `^(ome-tiff|tiff|qptiff|svs)$`

#### scRNA-seq File Format
**Location**: `modules/scRNA-seq/domains/level_3_4.yaml`
- **Attribute**: `FILE_FORMAT`
- **Pattern**: `^h5ad$`

#### scRNA-seq AnnData Schema Version
**Location**: `modules/scRNA-seq/domains/level_3_4.yaml`
- **Attribute**: `ANNDATA_SCHEMA_VERSION`
- **Pattern**: `^0\.1$`

## Summary by Module

### CoreFile Module
- `HTAN_DATA_FILE_ID`: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$`
- `HTAN_PARENT_ID`: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_([BD][0-9]{1,20})$`
- `FILENAME`: `^.+[\\/]\S*$`

### Biospecimen Module
- `HTAN_BIOSPECIMEN_ID`: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(B[0-9]{1,20})$`
- `HTAN_PARENT_ID`: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})(?:_(B[0-9]{1,20}))?$`

### Clinical Module
- `HTAN_PARTICIPANT_ID`: `^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})$`

### SpatialOmics Module
- `HTAN_PANEL_ID`: `^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$`
- `PANEL_SYNAPSE_ID`: `^syn\d+$`
- `GENE_ID`: `^(ENSG\d+|\d+)$`
- `HGNC_VERSION`: `^\d{4}-\d{2}-\d{2}$`
- `PROTOCOL_URL`: HTTP/HTTPS URL pattern

### MultiplexMicroscopy Module
- `CHANNEL_METADATA_ID`: `^syn\d+$`
- `ANTIBODY_RRID`: `^RRID:AB_\d+$`
- `FILE_FORMAT` (Level 2): `^(ome-tiff|tiff|qptiff|svs)$`
- `FILE_FORMAT` (Level 3): `^(ome-tiff|ome\.tiff|tiff|tif)$`
- `FILE_FORMAT` (Level 4): `^(csv|h5ad)$`

### Imaging Module
- `CITATION_OR_DOI`: HTTP/HTTPS URL pattern
- `IMAGING_PROTOCOL`: HTTP/HTTPS URL pattern

### DigitalPathology Module
- `FILE_FORMAT`: `^(ome-tiff|tiff|qptiff|svs)$`

### scRNA-seq Module
- `FILE_FORMAT`: `^h5ad$`
- `ANNDATA_SCHEMA_VERSION`: `^0\.1$`

## Notes

1. **HTAN ID Format**: HTAN identifiers follow the pattern `HTA{center_id}_{participant_id}_{entity_id?}` where:
   - Center ID: `2[0-2][0-9]` for Phase 2 (HTA200-229)
   - Participant ID: `0000`, `EXT[0-9]{1,18}`, or `[0-9]{1,21}` (max 21 characters)
   - Entity ID: Optional `[BD][0-9]{1,20}` (max 21 characters: B/D + up to 20 digits)
   - Total length: Maximum 50 characters (enforced by lookahead)

2. **Phase 2 Support**: All HTAN identifier patterns support Phase 2 center IDs (HTA200-229) with explicit length constraints to ensure total IDs never exceed 50 characters.

3. **URL Validation**: The URL pattern excludes private IP ranges to ensure only publicly accessible URLs are accepted.

4. **File Format Validation**: Most file formats are validated via enums, but some modules use regex patterns for stricter validation.



