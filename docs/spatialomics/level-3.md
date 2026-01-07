# SpatialOmics - Level 3

HTAN Spatial Omics Level 3 - Processed spatial assay output bundle

**Level 3 processed spatial assay output bundle - Contains platform-specific output files, segmentation, matrices, and QC metrics**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ASSAY_CHEMISTRY_VERSION` | string | Yes | Assay chemistry version (e.g., v1, v2) |
| `BUNDLE_CONTENTS` | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `CAPTURE_AREA` | [CaptureArea](#capturearea) | No | Area (or Capture Area) - One of the either four or two active regions where tissue can be placed on a Visium slide |
| `CELL_SEGMENTATION_METHOD` | string | Required IF HAS_CELL_SEGMENTATION = 'None' | Description of segmentation method |
| `CELL_SEGMENTED_OBJECT_TYPE` | [CellSegmentedObjectType](#cellsegmentedobjecttype) | Required IF HAS_CELL_SEGMENTATION = 'None' | Level of segmentation |
| `CLUSTERING_METHOD` | string | Required IF HAS_CLUSTERING = 'None' | Method used to define clusters |
| `CYTASSIST_USED` | boolean | No | Whether CytAssist was used |
| `DIMENSIONALITY_REDUCTION_METHOD` | [DimensionalityReductionMethod](#dimensionalityreductionmethod) | Required IF HAS_DIMENSIONALITY_REDUCTION = 'None' | Method used for dimensionality reduction |
| `GENOMIC_REFERENCE` | string | No | Reference genome used |
| `HAS_CELL_SEGMENTATION` | boolean | Yes | Indicates presence of cell segmentation data |
| `HAS_CLUSTERING` | boolean | Yes | Indicates if clustering was performed |
| `HAS_DIMENSIONALITY_REDUCTION` | boolean | No | Indicates presence of dimensionally reduced data |
| `NUMBER_OF_CLUSTERS` | integer | Required IF HAS_CLUSTERING = 'None' | Number of clusters identified |
| `NUMBER_OF_SEGMENTED_CELLS` | integer | Required IF HAS_CELL_SEGMENTATION = 'None' | Total number of segmented cells |
| `PANEL_NAME` | string | No | Number of genes/proteins in panel |
| `PANEL_SIZE_TOTAL_TARGETS` | integer | Yes | Total number of targets in the panel |
| `PANEL_SYNAPSE_ID` | string, pattern: <code>^syn\d+$</code> | No | Synapse ID of the completed spatial_omics_panel template |
| `PLATFORM` | [PlatformLevel3](#platformlevel3) | Yes | Name of the platform used to generate the data |
| `PORTAL_PREVIEW_FILE` | string | No | Relative path of HTML preview in bundle if present |
| `PROTEIN_MEASURED` | boolean | Yes | Whether protein was measured |
| `PROTOCOL_LINK` | string, pattern: <code>^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10\|127)(?:\.\d{1,3}){3})(?!(?:169\.254\|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]\|2\d\|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?\|1\d\d\|2[01]\d\|22[0-3])(?:\.(?:1?\d{1,2}\|2[0-4]\d\|25[0-5])){2}(?:\.(?:[1-9]\d?\|1\d\d\|2[0-4]\d\|25[0-4]))\|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$</code> | No | URL to protocol documentation |
| `QC_FEATURE_NUMBER` | integer | Yes | Features (e.g. spots or bins) under tissue |
| `QC_MEAN_READS_PER_FEATURE` | float | Yes | Mean reads per feature |
| `QC_SPATIAL_UNIT` | [QCSpatialUnit](#qcspatialunit) | Yes | Type of spatial unit |
| `QC_TOTAL_GENES_DETECTED` | integer | Yes | Total genes detected |
| `QC_TOTAL_NUMBER_OF_READS` | integer | Yes | Total number of reads |
| `REGION_AREA` | float | Yes | Capture area in µm² |
| `RNA_MEASURED` | boolean | Yes | Whether RNA was measured |
| `RUN_ID` | string | No | A unique identifier for this individual run (typically associated with a single slide) of the spatial transcriptomic processing workflow |
| `SAME_SECTION_IMAGING_CHANNELS` | string | Required IF SAME_SECTION_IMAGING_MODALITY = 'fluorescence' | Antigens targeted in same section fluorescence imaging |
| `SAME_SECTION_IMAGING_ID` | string, pattern: <code>^(HTA([1-9]\|1[0-6]))_((EXT)?([0-9]\d*\|0000))_([0-9]\d*\|0000)$</code> | No | HTAN ID of data file that represents same section imaging |
| `SAME_SECTION_IMAGING_MODALITY` | [SameSectionImagingModality](#samesectionimagingmodality) | No | Was same section imaging performed |
| `SEQUENCING_CONFIGURATION` | string | Required IF SPATIAL_ASSAY_TYPE = 'capture-based' | Read and index setup |
| `SEQUENCING_DEPTH` | string | Required IF SPATIAL_ASSAY_TYPE = 'capture-based' | Sequencing depth |
| `SEQUENCING_INSTRUMENT` | string | Required IF SPATIAL_ASSAY_TYPE = 'capture-based' | Sequencer used |
| `SLIDE_SERIAL_NUMBER` | string | No | Slide serial number |
| `SOFTWARE_AND_VERSION` | string | No | Software/tools used for processing |
| `SPATIAL_ASSAY_TYPE` | [SpatialAssayType](#spatialassaytype) | No | Type of spatial assay (in situ or capture-based) |
| `TRANSCRIPTOME_TYPE` | [TranscriptomeType](#transcriptometype) | Required IF RNA_MEASURED = 'None' | Molecular targets measured using panels |

