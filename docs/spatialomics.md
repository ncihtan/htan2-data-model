# SpatialOmics

HTAN Spatial Omics Data Model Schema for Phase 2 - All Levels

<div class="grid cards" markdown>

-   **[CoreFileAttributes](#corefileattributes)**
    ---
    Universal attributes that apply to all file-based data in HTAN

-   **[SpatialLevel1](#spatiallevel1)**
    ---
    _Level 1_ &nbsp; Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files

-   **[SpatialLevel3](#spatiallevel3)**
    ---
    _Level 3_ &nbsp; Level 3 processed spatial assay output bundle - Contains platform-specific output files, segmentation, matrices, and ...

-   **[SpatialLevel4](#spatiallevel4)**
    ---
    _Level 4_ &nbsp; Level 4 interoperable spatial omics file (optional) - Harmonized h5ad, RDS, or Zarr file for downstream analysis

-   **[SpatialPanel](#spatialpanel)**
    ---
    Spatial omics panel information for targeted sequencing or protein panels

</div>

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## SpatialLevel1

**Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | [FileFormatLevel1](enums.md#fileformatlevel1) | Yes | High-level package format of the bundle |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.tar for tar; .tar.gz for tar.gz; .zip for zip) |
| `PLATFORM` | [Platform](enums.md#platform) | Yes | Name of the platform used to generate the data |
| `ASSAY_TYPE` | [AssayType](enums.md#assaytype) | Yes | Broad assay class (drives downstream conditionals) |
| `BUNDLE_CONTENTS` | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `HAS_SEQUENCING` | boolean | No | If raw/aligned sequencing data is included |
| `SEQUENCING_FILE_TYPE` | [SequencingFileType](enums.md#sequencingfiletype) | Conditional: SEQUENCING_FILE_TYPE is required when HAS_SEQUENCING is true | Sequencing file type |
| `HAS_IMAGES` | boolean | Yes | Whether any image files (e.g., TIFFs) are included |
| `IMAGE_TYPES` | [ImageType](enums.md#imagetype) | Conditional: IMAGE_TYPES is required when HAS_IMAGES is true | Types of images provided |
| `HAS_PROBE_SET` | boolean | Conditional: HAS_PROBE_SET is required when ASSAY_TYPE is molecular barcoding | Whether a targeted probe/gene panel is included |
| `HAS_REGISTRATION_FILES` | boolean | Yes | Whether any spatial registration transform files are included |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## SpatialLevel3

**Level 3 processed spatial assay output bundle - Contains platform-specific output files, segmentation, matrices, and QC metrics**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `PLATFORM` | [PlatformLevel3](enums.md#platformlevel3) | Yes | Name of the platform used to generate the data |
| `SPATIAL_ASSAY_TYPE` | [SpatialAssayType](enums.md#spatialassaytype) | No | Type of spatial assay (in situ or capture-based) |
| `ASSAY_CHEMISTRY_VERSION` | string | Yes | Assay chemistry version (e.g., v1, v2) |
| `SOFTWARE_AND_VERSION` | string | No | Software/tools used for processing |
| `PROTOCOL_LINK` | string | No | URL to protocol documentation |
| `RNA_MEASURED` | boolean | Yes | Whether RNA was measured |
| `PROTEIN_MEASURED` | boolean | Yes | Whether protein was measured |
| `TRANSCRIPTOME_TYPE` | [TranscriptomeType](enums.md#transcriptometype) | Conditional: TRANSCRIPTOME_TYPE is required when RNA_MEASURED is true | Molecular targets measured using panels |
| `PANEL_SIZE_TOTAL_TARGETS` | integer | Yes | Total number of targets in the panel |
| `PANEL_NAME` | string | Conditional: PANEL_NAME is required when TRANSCRIPTOME_TYPE is Targeted OR PROTEIN_MEASURED is true | Number of genes/proteins in panel |
| `PANEL_SYNAPSE_ID` | string | Conditional: PANEL_SYNAPSE_ID is required when TRANSCRIPTOME_TYPE is Targeted OR PROTEIN_MEASURED is true | Synapse ID of the completed spatial_omics_panel template |
| `SAME_SECTION_IMAGING_ID` | string | No | HTAN ID of data file that represents same section imaging |
| `SAME_SECTION_IMAGING_MODALITY` | [SameSectionImagingModality](enums.md#samesectionimagingmodality) | No | Was same section imaging performed |
| `SAME_SECTION_IMAGING_CHANNELS` | string | Conditional: SAME_SECTION_IMAGING_CHANNELS is required when SAME_SECTION_IMAGING_MODALITY is fluorescence | Antigens targeted in same section fluorescence imaging |
| `REGION_AREA` | float | Yes | Capture area in µm² |
| `BUNDLE_CONTENTS` | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `PORTAL_PREVIEW_FILE` | string | No | Relative path of HTML preview in bundle if present |
| `HAS_CELL_SEGMENTATION` | boolean | Yes | Indicates presence of cell segmentation data |
| `CELL_SEGMENTATION_METHOD` | string | Conditional: CELL_SEGMENTATION_METHOD is required when HAS_CELL_SEGMENTATION is true | Description of segmentation method |
| `CELL_SEGMENTED_OBJECT_TYPE` | [CellSegmentedObjectType](enums.md#cellsegmentedobjecttype) | Conditional: CELL_SEGMENTED_OBJECT_TYPE is required when HAS_CELL_SEGMENTATION is true | Level of segmentation |
| `NUMBER_OF_SEGMENTED_CELLS` | integer | Conditional: NUMBER_OF_SEGMENTED_CELLS is required when HAS_CELL_SEGMENTATION is true | Total number of segmented cells |
| `HAS_DIMENSIONALITY_REDUCTION` | boolean | No | Indicates presence of dimensionally reduced data |
| `DIMENSIONALITY_REDUCTION_METHOD` | [DimensionalityReductionMethod](enums.md#dimensionalityreductionmethod) | Conditional: DIMENSIONALITY_REDUCTION_METHOD is required when HAS_DIMENSIONALITY_REDUCTION is true | Method used for dimensionality reduction |
| `HAS_CLUSTERING` | boolean | Yes | Indicates if clustering was performed |
| `CLUSTERING_METHOD` | string | Conditional: CLUSTERING_METHOD is required when HAS_CLUSTERING is true | Method used to define clusters |
| `NUMBER_OF_CLUSTERS` | integer | Conditional: NUMBER_OF_CLUSTERS is required when HAS_CLUSTERING is true | Number of clusters identified |
| `SLIDE_SERIAL_NUMBER` | string | Conditional: SLIDE_SERIAL_NUMBER is required when PLATFORM is Visium or Visium HD or Xenium | Slide serial number |
| `CAPTURE_AREA` | [CaptureArea](enums.md#capturearea) | Conditional: CAPTURE_AREA is required when PLATFORM is Visium or Visium HD | Area (or Capture Area) - One of the either four or two active regions where tissue can be placed on a Visium slide |
| `RUN_ID` | string | No | A unique identifier for this individual run (typically associated with a single slide) of the spatial transcriptomic processing workflow |
| `CYTASSIST_USED` | boolean | Conditional: CYTASSIST_USED is required when PLATFORM is Visium or Visium HD | Whether CytAssist was used |
| `GENOMIC_REFERENCE` | string | Conditional: GENOMIC_REFERENCE is required when PLATFORM is Visium or Visium HD | Reference genome used |
| `SEQUENCING_INSTRUMENT` | string | Conditional: SEQUENCING_INSTRUMENT is required when SPATIAL_ASSAY_TYPE is capture-based | Sequencer used |
| `SEQUENCING_CONFIGURATION` | string | Conditional: SEQUENCING_CONFIGURATION is required when SPATIAL_ASSAY_TYPE is capture-based | Read and index setup |
| `SEQUENCING_DEPTH` | string | Conditional: SEQUENCING_DEPTH is required when SPATIAL_ASSAY_TYPE is capture-based | Sequencing depth |
| `QC_SPATIAL_UNIT` | [QCSpatialUnit](enums.md#qcspatialunit) | Yes | Type of spatial unit |
| `QC_FEATURE_NUMBER` | integer | Yes | Features (e.g. spots or bins) under tissue |
| `QC_MEAN_READS_PER_FEATURE` | float | Yes | Mean reads per feature |
| `QC_TOTAL_GENES_DETECTED` | integer | Yes | Total genes detected |
| `QC_TOTAL_NUMBER_OF_READS` | integer | Yes | Total number of reads |
| `FILENAME` | string | Yes | Name of the bundle file. Must end with .tar.gz or .gz |
| `FILE_FORMAT` | string | Yes | Format of the bundle file (tar.gz or gz) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## SpatialLevel4

**Level 4 interoperable spatial omics file (optional) - Harmonized h5ad, RDS, or Zarr file for downstream analysis**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | [FileFormatLevel4](enums.md#fileformatlevel4) | Yes | File format of the data file |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.h5ad for h5ad; .rds for rds; .zarr for zarr) |
| `TOOL_COMPATIBILITY` | [ToolCompatibility](enums.md#toolcompatibility) | No | Tools or libraries compatible with this file |
| `NUMBER_OF_FEATURES` | integer | Yes | Number of features (e.g. transcripts) |
| `NUMBER_OF_OBJECTS` | integer | Yes | Number of objects (e.g. cells) |
| `HAS_DIMENSIONALITY_REDUCTION` | boolean | Yes | Indicates presence of dimensionally reduced data |
| `DIMENSIONALITY_REDUCTION_METHOD` | [DimensionalityReductionMethodLevel4](enums.md#dimensionalityreductionmethodlevel4) | Conditional: DIMENSIONALITY_REDUCTION_METHOD is required when HAS_DIMENSIONALITY_REDUCTION is true | Method used for dimensionality reduction |
| `HAS_CLUSTERING` | boolean | Yes | Indicates if clustering was performed |
| `CLUSTERING_METHOD` | string | Conditional: CLUSTERING_METHOD is required when HAS_CLUSTERING is true | Method used to define clusters |
| `NUMBER_OF_CLUSTERS` | integer | Conditional: NUMBER_OF_CLUSTERS is required when HAS_CLUSTERING is true | Number of clusters identified |
| `HAS_CELL_TYPE_CALLING` | boolean | Yes | Indicates presence of cell type annotations |
| `CELL_TYPE_CALLING_METHOD` | string | Conditional: CELL_TYPE_CALLING_METHOD is required when HAS_CELL_TYPE_CALLING is true | Method used for cell type annotation |
| `CELL_TYPES` | string | Conditional: CELL_TYPES is required when HAS_CELL_TYPE_CALLING is true | List of cell types present in the data |
| `HAS_NORMALISED_ARRAY` | boolean | Yes | Indicates presence of normalized array |
| `NORMALISATION_METHOD` | [NormalisationMethod](enums.md#normalisationmethod) | Conditional: NORMALISATION_METHOD is required when HAS_NORMALISED_ARRAY is true | Method used for normalizing the array data |
| `HAS_RAW_ARRAY` | boolean | Yes | Indicates presence of raw expression array |
| `HAS_IMAGE` | boolean | Yes | Indicates presence of associated image data |
| `IMAGE_TYPE` | [ImageTypeLevel4](enums.md#imagetypelevel4) | Conditional: IMAGE_TYPE is required when HAS_IMAGE is true | Type of image associated with the data file |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## SpatialPanel

**Spatial omics panel information for targeted sequencing or protein panels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `HTAN_PANEL_ID` | string | Yes | Unique identifier for the panel |
| `GENE_SYMBOL` | string | Yes | HGNC-approved Gene symbol (e.g., MYC, PIK3C) |
| `HGNC_VERSION` | string | Yes | Version of the HGNC used, indicated with the date of the HGNC reference (e.g., 2025-08-01) |
| `GENE_ID` | string | Yes | Stable Ensembl gene identifier (e.g., ENSG00000214114, ENSG00000121879). String matching ENSG\\d+ or digits |
| `USER_GENE_NAME` | string | No | Optional user-defined name for the Gene |

## Enums

### AssayType

| Value | Description |
|-------|-------------|
| in situ sequencing | In situ sequencing assay type |
| molecular barcoding | Molecular barcoding assay type |
| multi-omic sequencing | Multi-omic sequencing assay type |
| spot-based sequencing | Spot-based sequencing assay type |

### CaptureArea

| Value | Description |
|-------|-------------|
| A | Capture area A (CytAssist slides with 11 mm Capture Area) |
| A1 | Capture area A1 (Visium slides v1 with 6.5 mm Capture Area, or CytAssist/Gateway slides with 6.5 mm Capture Area) |
| B | Capture area B (CytAssist slides with 11 mm Capture Area) |
| B1 | Capture area B1 (Visium slides v1 with 6.5 mm Capture Area) |
| C1 | Capture area C1 (Visium slides v1 with 6.5 mm Capture Area) |
| D1 | Capture area D1 (Visium slides v1 with 6.5 mm Capture Area, or CytAssist/Gateway slides with 6.5 mm Capture Area) |

### CellSegmentedObjectType

| Value | Description |
|-------|-------------|
| cytoplasm | Cytoplasm segmentation object type |
| nucleus | Nucleus segmentation object type |
| Whole cell | Whole cell segmentation object type |

### DimensionalityReductionMethod

| Value | Description |
|-------|-------------|
| PCA | Principal Component Analysis |
| t-SNE | t-Distributed Stochastic Neighbor Embedding |
| UMAP | Uniform Manifold Approximation and Projection |
| other | Other dimensionality reduction method |

### DimensionalityReductionMethodLevel4

| Value | Description |
|-------|-------------|
| PCA | Principal Component Analysis |
| t-SNE | t-Distributed Stochastic Neighbor Embedding |
| UMAP | Uniform Manifold Approximation and Projection |
| other | Other dimensionality reduction method |

### FileFormatLevel1

| Value | Description |
|-------|-------------|
| tar | TAR archive format |
| tar.gz | TAR GZIP compressed archive format |
| zip | ZIP compressed archive format |

### FileFormatLevel4

| Value | Description |
|-------|-------------|
| h5ad | AnnData HDF5 format (Python) |
| rds | RDS format (R) |
| zarr | Zarr format |

### ImageType

| Value | Description |
|-------|-------------|
| DAPI | DAPI (4',6-diamidino-2-phenylindole) image type |
| H&E | Hematoxylin and Eosin image type |
| MIF | Multiplex Immunofluorescence image type |
| Other | Other image type |

### ImageTypeLevel4

| Value | Description |
|-------|-------------|
| jpeg | JPEG image format |
| other | Other image format |
| png | PNG image format |
| tiff | TIFF image format |

### NormalisationMethod

| Value | Description |
|-------|-------------|
| CPM | Counts Per Million normalization |
| log normalization | Log normalization |
| SCTransform | SCTransform normalization |
| TPM | Transcripts Per Million normalization |
| other | Other normalization method |

### Platform

| Value | Description |
|-------|-------------|
| 10x Genomics Visium | 10x Genomics Visium platform |
| 10x Genomics Visium HD | 10x Genomics Visium HD platform |
| 10x Genomics Xenium | 10x Genomics Xenium platform |
| Nanostring CosMX | Nanostring CosMX platform |
| STOmics Stereo-CITE | STOmics Stereo-CITE platform |
| STOmics Stereo-seq | STOmics Stereo-seq platform |

### PlatformLevel3

| Value | Description |
|-------|-------------|
| 10x Genomics Visium | 10x Genomics Visium platform |
| 10x Genomics Visium HD | 10x Genomics Visium HD platform |
| 10x Genomics Xenium | 10x Genomics Xenium platform |
| DBiT-seq | DBiT-seq platform |
| Nanostring CosMX | Nanostring CosMX platform |
| SeqFISH | SeqFISH platform |
| STOmics Stereo-CITE | STOmics Stereo-CITE platform |
| STOmics Stereo-seq | STOmics Stereo-seq platform |

### QCSpatialUnit

| Value | Description |
|-------|-------------|
| 100um area | 100 micrometer area spatial unit |
| 8um bin | 8 micrometer bin spatial unit |
| cell | Cell spatial unit |
| spot | Spot spatial unit |

### SameSectionImagingModality

| Value | Description |
|-------|-------------|
| fluorescence | Fluorescence imaging modality |
| H&E | Hematoxylin and Eosin imaging modality |

### SequencingFileType

| Value | Description |
|-------|-------------|
| BAM | BAM alignment file format |
| FASTQ | FASTQ sequencing file format |

### SpatialAssayType

| Value | Description |
|-------|-------------|
| capture-based | Capture-based spatial assay type |
| In situ | In situ spatial assay type |

### ToolCompatibility

| Value | Description |
|-------|-------------|
| anndata | AnnData library compatibility |
| seurat | Seurat library compatibility |
| spatialdata | SpatialData library compatibility |

### TranscriptomeType

| Value | Description |
|-------|-------------|
| Protein coding | Protein coding transcriptome type |
| Targeted | Targeted transcriptome type |
| Whole transcriptome | Whole transcriptome type |
