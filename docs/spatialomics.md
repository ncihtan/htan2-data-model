# Spatial

HTAN Spatial Omics Data Model Schema for Phase 2 - All Levels

## Classes

### CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### SpatialData

**Container for all Spatial Omics data levels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `LEVEL_1_DATA` | SpatialLevel1 | No | Level 1 Spatial Omics data (raw spatial data bundle, optional) |
| `LEVEL_3_DATA` | SpatialLevel3 | Yes | Level 3 Spatial Omics data (processed spatial assay output bundle, required) |
| `LEVEL_4_DATA` | SpatialLevel4 | No | Level 4 Spatial Omics data (interoperable h5ad or RDS file, optional) |
| `PANEL_DATA` | SpatialPanel | No | Spatial panel information for targeted sequencing or protein panels |

### SpatialLevel1

**Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ASSAY_TYPE` | AssayType<br/>`in situ sequencing`, `molecular barcoding`, `multi-omic sequencing`, `spot-based sequencing` | Yes | Broad assay class (drives downstream conditionals) |
| `BUNDLE_CONTENTS` | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `FILE_FORMAT` | FileFormatLevel1<br/>`tar`, `tar.gz`, `zip` | Yes | High-level package format of the bundle |
| `HAS_IMAGES` | boolean | Yes | Whether any image files (e.g., TIFFs) are included |
| `HAS_PROBE_SET` | boolean | No | Whether a targeted probe/gene panel is included |
| `HAS_REGISTRATION_FILES` | boolean | Yes | Whether any spatial registration transform files are included |
| `HAS_SEQUENCING` | boolean | No | If raw/aligned sequencing data is included |
| `IMAGE_TYPES` | ImageType<br/>`DAPI`, `H&E`, `MIF`, `Other` | No | Types of images provided |
| `PLATFORM` | See [Platform](#platform) enum below | Yes | Name of the platform used to generate the data |
| `SEQUENCING_FILE_TYPE` | SequencingFileType<br/>`BAM`, `FASTQ` | No | Sequencing file type |

### SpatialLevel3

**Level 3 processed spatial assay output bundle - Contains platform-specific output files, segmentation, matrices, and QC metrics**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ASSAY_CHEMISTRY_VERSION` | string | Yes | Assay chemistry version (e.g., v1, v2) |
| `BUNDLE_CONTENTS` | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `CAPTURE_AREA` | See [CaptureArea](#capturearea) enum below | No | Area (or Capture Area) - One of the either four or two active regions where tissue can be placed on a Visium slide |
| `CELL_SEGMENTATION_METHOD` | string | No | Description of segmentation method |
| `CELL_SEGMENTED_OBJECT_TYPE` | CellSegmentedObjectType<br/>`Whole cell`, `cytoplasm`, `nucleus` | No | Level of segmentation |
| `CLUSTERING_METHOD` | string | No | Method used to define clusters |
| `CYTASSIST_USED` | boolean | No | Whether CytAssist was used |
| `DIMENSIONALITY_REDUCTION_METHOD` | DimensionalityReductionMethod<br/>`PCA`, `UMAP`, `other`, `t-SNE` | No | Method used for dimensionality reduction |
| `GENOMIC_REFERENCE` | string | No | Reference genome used |
| `HAS_CELL_SEGMENTATION` | boolean | Yes | Indicates presence of cell segmentation data |
| `HAS_CLUSTERING` | boolean | Yes | Indicates if clustering was performed |
| `HAS_DIMENSIONALITY_REDUCTION` | boolean | No | Indicates presence of dimensionally reduced data |
| `NUMBER_OF_CLUSTERS` | integer | No | Number of clusters identified |
| `NUMBER_OF_SEGMENTED_CELLS` | integer | No | Total number of segmented cells |
| `PANEL_NAME` | string | No | Number of genes/proteins in panel |
| `PANEL_SIZE_TOTAL_TARGETS` | integer | Yes | Total number of targets in the panel |
| `PANEL_SYNAPSE_ID` | string | No | Synapse ID of the completed spatial_omics_panel template |
| `PLATFORM` | See [PlatformLevel3](#platformlevel3) enum below | Yes | Name of the platform used to generate the data |
| `PORTAL_PREVIEW_FILE` | string | No | Relative path of HTML preview in bundle if present |
| `PROTEIN_MEASURED` | boolean | Yes | Whether protein was measured |
| `PROTOCOL_LINK` | string | No | URL to protocol documentation |
| `QC_FEATURE_NUMBER` | integer | Yes | Features (e.g. spots or bins) under tissue |
| `QC_MEAN_READS_PER_FEATURE` | float | Yes | Mean reads per feature |
| `QC_SPATIAL_UNIT` | QCSpatialUnit<br/>`100um area`, `8um bin`, `cell`, `spot` | Yes | Type of spatial unit |
| `QC_TOTAL_GENES_DETECTED` | integer | Yes | Total genes detected |
| `QC_TOTAL_NUMBER_OF_READS` | integer | Yes | Total number of reads |
| `REGION_AREA` | float | Yes | Capture area in µm² |
| `RNA_MEASURED` | boolean | Yes | Whether RNA was measured |
| `RUN_ID` | string | No | A unique identifier for this individual run (typically associated with a single slide) of the spatial transcriptomic processing workflow |
| `SAME_SECTION_IMAGING_CHANNELS` | string | No | Antigens targeted in same section fluorescence imaging |
| `SAME_SECTION_IMAGING_ID` | string | No | HTAN ID of data file that represents same section imaging |
| `SAME_SECTION_IMAGING_MODALITY` | SameSectionImagingModality<br/>`H&E`, `fluorescence` | No | Was same section imaging performed |
| `SEQUENCING_CONFIGURATION` | string | No | Read and index setup |
| `SEQUENCING_DEPTH` | string | No | Sequencing depth |
| `SEQUENCING_INSTRUMENT` | string | No | Sequencer used |
| `SLIDE_SERIAL_NUMBER` | string | No | Slide serial number |
| `SOFTWARE_AND_VERSION` | string | No | Software/tools used for processing |
| `SPATIAL_ASSAY_TYPE` | SpatialAssayType<br/>`In situ`, `capture-based` | No | Type of spatial assay (in situ or capture-based) |
| `TRANSCRIPTOME_TYPE` | TranscriptomeType<br/>`Protein coding`, `Targeted`, `Whole transcriptome` | No | Molecular targets measured using panels |

### SpatialLevel4

**Level 4 interoperable spatial omics file (optional) - Harmonized h5ad, RDS, or Zarr file for downstream analysis**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CELL_TYPES` | string | No | List of cell types present in the data |
| `CELL_TYPE_CALLING_METHOD` | string | No | Method used for cell type annotation |
| `CLUSTERING_METHOD` | string | No | Method used to define clusters |
| `DIMENSIONALITY_REDUCTION_METHOD` | DimensionalityReductionMethodLevel4<br/>`PCA`, `UMAP`, `other`, `t-SNE` | No | Method used for dimensionality reduction |
| `FILE_FORMAT` | FileFormatLevel4<br/>`h5ad`, `rds`, `zarr` | Yes | File format of the data file |
| `HAS_CELL_TYPE_CALLING` | boolean | Yes | Indicates presence of cell type annotations |
| `HAS_CLUSTERING` | boolean | Yes | Indicates if clustering was performed |
| `HAS_DIMENSIONALITY_REDUCTION` | boolean | Yes | Indicates presence of dimensionally reduced data |
| `HAS_IMAGE` | boolean | Yes | Indicates presence of associated image data |
| `HAS_NORMALISED_ARRAY` | boolean | Yes | Indicates presence of normalized array |
| `HAS_RAW_ARRAY` | boolean | Yes | Indicates presence of raw expression array |
| `IMAGE_TYPE` | ImageTypeLevel4<br/>`jpeg`, `other`, `png`, `tiff` | No | Type of image associated with the data file |
| `NORMALISATION_METHOD` | NormalisationMethod<br/>`CPM`, `SCTransform`, `TPM`, `log normalization`, `other` | No | Method used for normalizing the array data |
| `NUMBER_OF_CLUSTERS` | integer | No | Number of clusters identified |
| `NUMBER_OF_FEATURES` | integer | Yes | Number of features (e.g. transcripts) |
| `NUMBER_OF_OBJECTS` | integer | Yes | Number of objects (e.g. cells) |
| `TOOL_COMPATIBILITY` | ToolCompatibility<br/>`anndata`, `seurat`, `spatialdata` | No | Tools or libraries compatible with this file |

### SpatialPanel

**Spatial omics panel information for targeted sequencing or protein panels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `GENE_ID` | string | Yes | Stable Ensembl gene identifier (e.g., ENSG00000214114, ENSG00000121879). String matching ENSG\\d+ or digits |
| `GENE_SYMBOL` | string | Yes | HGNC-approved Gene symbol (e.g., MYC, PIK3C) |
| `HGNC_VERSION` | string | Yes | Version of the HGNC used, indicated with the date of the HGNC reference (e.g., 2025-08-01) |
| `HTAN_PANEL_ID` | string | Yes | Unique identifier for the panel |
| `USER_GENE_NAME` | string | No | Optional user-defined name for the Gene |

## Enums

### CaptureArea {#capturearea}

| Value | Description |
|-------|-------------|
| `A` | Capture area A (CytAssist slides with 11 mm Capture Area) |
| `A1` | Capture area A1 (Visium slides v1 with 6.5 mm Capture Area, or CytAssist/Gateway slides with 6.5 mm Capture Area) |
| `B` | Capture area B (CytAssist slides with 11 mm Capture Area) |
| `B1` | Capture area B1 (Visium slides v1 with 6.5 mm Capture Area) |
| `C1` | Capture area C1 (Visium slides v1 with 6.5 mm Capture Area) |
| `D1` | Capture area D1 (Visium slides v1 with 6.5 mm Capture Area, or CytAssist/Gateway slides with 6.5 mm Capture Area) |

### Platform {#platform}

| Value | Description |
|-------|-------------|
| `10x Genomics Visium` | 10x Genomics Visium platform |
| `10x Genomics Visium HD` | 10x Genomics Visium HD platform |
| `10x Genomics Xenium` | 10x Genomics Xenium platform |
| `Nanostring CosMX` | Nanostring CosMX platform |
| `STOmics Stereo-CITE` | STOmics Stereo-CITE platform |
| `STOmics Stereo-seq` | STOmics Stereo-seq platform |

### PlatformLevel3 {#platformlevel3}

| Value | Description |
|-------|-------------|
| `10x Genomics Visium` | 10x Genomics Visium platform |
| `10x Genomics Visium HD` | 10x Genomics Visium HD platform |
| `10x Genomics Xenium` | 10x Genomics Xenium platform |
| `DBiT-seq` | DBiT-seq platform |
| `Nanostring CosMX` | Nanostring CosMX platform |
| `STOmics Stereo-CITE` | STOmics Stereo-CITE platform |
| `STOmics Stereo-seq` | STOmics Stereo-seq platform |
| `SeqFISH` | SeqFISH platform |

