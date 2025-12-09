# HTAN Spatial Omics

Spatial Omics module for HTAN Phase 2 data model, implementing standards for sequencing-based and sequence-hybridization spatial omics assays including Visium, Xenium, CosMx, STOmics, and other spatial transcriptomics technologies.

## Purpose

This module implements the Spatial Omics RFC for HTAN Phase 2, which supports:

1. **Sequencing-Based Spatial Assays**: Spot-based capture (Visium, Visium HD), in situ sequencing (seqFISH), molecular barcoding (Xenium, CosMx), and other spatial transcriptomics platforms
2. **Multi-Level Data Structure**: Level 1 (raw data, optional), Level 3 (processed bundles), Level 4 (interoperable files, optional), and Panel information
3. **Platform Flexibility**: Supports current and emerging spatial omics technologies
4. **Bundle-Level Metadata**: Eliminates per-file metadata requirements, focusing on bundle-level structure
5. **Panel Information**: Structured metadata for targeted sequencing or protein panels

## Structure

### **Domain Files**
- `domains/spatial.yaml` - Main schema file (imports all levels)
- `domains/level_1.yaml` - Level 1 schema (raw spatial data bundle, optional)
- `domains/level_3.yaml` - Level 3 schema (processed spatial assay output bundle)
- `domains/level_4.yaml` - Level 4 schema (interoperable h5ad or RDS file, optional)
- `domains/spatial_panel.yaml` - Spatial panel information schema

### **Key Attributes**

#### **Level 1: Raw Spatial Data Bundle (Optional)**
- **HTAN Identifiers**: Data file ID, parent biospecimen ID, parent data file ID
- **Bundle Format**: tar.gz or zip archive format
- **Platform**: 10x Genomics (Visium, Visium HD, Xenium), Nanostring CosMX, STOmics (Stereo-seq, Stereo-CITE)
- **Assay Type**: spot-based sequencing, in situ sequencing, molecular barcoding, multi-omic sequencing
- **Bundle Contents**: List of expected files or folders in the bundle
- **Sequencing Data**: Whether raw/aligned sequencing data is included (FASTQ, BAM)
- **Images**: Whether image files are included (H&E, DAPI, MIF, Other)
- **Probe Set**: Whether a targeted probe/gene panel is included
- **Registration Files**: Whether spatial registration transform files are included

#### **Level 3: Processed Spatial Assay Output Bundle (Required)**
- **HTAN Identifiers**: Data file ID, parent biospecimen ID, parent data file ID (optional)
- **Platform**: 10x Genomics (Visium, Visium HD, Xenium), Nanostring CosMX, STOmics (Stereo-seq, Stereo-CITE), SeqFISH, DBiT-seq
- **Assay Details**: Spatial assay type (in situ, capture-based), assay chemistry version, software and version, protocol link
- **Molecular Targets**: RNA measured, protein measured, transcriptome type (whole transcriptome, protein coding, targeted), panel size/total targets
- **Panel Information**: Panel name, panel Synapse ID (for targeted panels or protein measurements)
- **Same Section Imaging**: Imaging ID, modality (H&E, fluorescence), channels
- **Region Area**: Capture area in µm²
- **Bundle Contents**: List of expected files or folders in the bundle
- **Portal Preview**: Relative path of HTML preview if present
- **Cell Segmentation**: Presence, method, object type (whole cell, nucleus, cytoplasm), number of segmented cells
- **Dimensionality Reduction**: Presence, method (PCA, UMAP, t-SNE, other)
- **Clustering**: Presence, method, number of clusters
- **Platform-Specific Attributes**:
  - **Visium/Visium HD**: Slide serial number, capture area (A1, B1, C1, D1, A, B), CytAssist used, genomic reference
  - **Xenium**: Slide serial number
  - **Capture-Based Assays**: Sequencing instrument, sequencing configuration, sequencing depth
- **Quality Control Metrics**:
  - QC spatial unit (8um bin, spot, 100um area, cell)
  - QC feature number (features under tissue)
  - QC mean reads per feature
  - QC total genes detected
  - QC total number of reads

#### **Level 4: Interoperable File (Optional)**
- **HTAN Identifiers**: Data file ID, parent data file ID (optional)
- **File Format**: h5ad, rds, or zarr
- **Tool Compatibility**: anndata, spatialdata, seurat
- **Data Dimensions**: Number of features (e.g., transcripts), number of objects (e.g., cells)
- **Dimensionality Reduction**: Presence, method (PCA, UMAP, t-SNE, other)
- **Clustering**: Presence, method, number of clusters
- **Cell Type Calling**: Presence, method, list of cell types
- **Normalization**: Presence, method (CPM, TPM, log normalization, SCTransform, other)
- **Arrays**: Raw array presence, normalized array presence
- **Image**: Presence, image type (tiff, jpeg, png, other)

#### **Spatial Panel Information**
- **HTAN Panel ID**: Unique identifier for the panel
- **Gene Symbol**: HGNC-approved gene symbol (e.g., MYC, PIK3C)
- **HGNC Version**: Version of the HGNC used (date format: YYYY-MM-DD)
- **Gene ID**: Stable Ensembl gene identifier (ENSG\d+ or digits)
- **User Gene Name**: Optional user-defined name for the gene

### **Data Levels**

#### **Level 1: Raw Spatial Data Bundle (Optional)**
- **Purpose**: Minimal bundle-level metadata for raw sequencing data submissions
- **Contents**: FASTQs/BAMs, original images, registration files
- **Format**: tar.gz or zip archive
- **Note**: Not required for standard submissions; only if raw data is being submitted

#### **Level 3: Processed Spatial Assay Output Bundle (Required)**
- **Purpose**: Bundle-level metadata for processed spatial assay submissions
- **Contents**: Platform-specific output files (matrices, segmentation, images, vendor JSONs)
- **Format**: tar.gz or zip archive
- **Structure**: Must follow expected directory and file structure defined in HTAN platform guidance
- **Prohibited**: Controlled-access data (fastqs, bams, bai files)

#### **Level 4: Interoperable File (Optional)**
- **Purpose**: Harmonized output file for downstream analysis
- **Contents**: Expression matrices, spatial coordinates, feature metadata in reusable format
- **Format**: h5ad (AnnData), rds (Seurat), or zarr
- **Compatibility**: Compatible with Squidpy, Seurat, and other downstream tools

#### **Spatial Panel Information**
- **Purpose**: Structured metadata for targeted sequencing or protein panels
- **Contents**: Panel identifier, gene/protein targets with stable identifiers
- **Format**: Separate table or filtered by Target_Type
- **Usage**: Required for assays using targeted panels (Xenium, CosMx, Stereo-CITE)

## Supported Platforms

### **Spot-Based Capture Assays**
- 10x Genomics Visium
- 10x Genomics Visium HD
- Slide-seq and related variants

### **In Situ Sequencing (ISS) and Hybridization-Based Assays**
- seqFISH and seqFISH+
- MERFISH
- Academic ISS methods

### **Barcoded Capture with Molecular Decoding**
- 10x Genomics Xenium
- Nanostring CosMx SMI
- BGI/MGI STOmics platforms:
  - Stereo-seq (RNA)
  - Stereo-CITE (RNA + protein)
  - Stereo-seq OMNI (multiome)

### **Other Sequencing-Based Spatial Molecular Profiling**
- DBiT-seq
- Custom or academic assays combining spatial barcoding with NGS

## Usage

### Level 3: Processed Spatial Assay Output Bundle

```yaml
# Example Spatial Level 3 data
SpatialLevel3:
  COMPONENT: "Spatial Omics"
  FILENAME: "visium_sample.tar.gz"
  FILE_FORMAT: "tar.gz"
  HTAN_DATA_FILE_ID: "HTA200_2_12347"
  HTAN_PARENT_ID: "HTA200_2_B7002"
  
  # Platform and assay details
  PLATFORM: "10x Genomics Visium"
  SPATIAL_ASSAY_TYPE: "capture-based"
  ASSAY_CHEMISTRY_VERSION: "v1"
  SOFTWARE_AND_VERSION: "Space Ranger 2.0.0"
  PROTOCOL_LINK: "https://protocols.io/example"
  
  # Molecular targets
  RNA_MEASURED: true
  PROTEIN_MEASURED: false
  TRANSCRIPTOME_TYPE: "Whole transcriptome"
  PANEL_SIZE_TOTAL_TARGETS: 18000
  
  # Same section imaging
  SAME_SECTION_IMAGING_MODALITY: "H&E"
  
  # Region and bundle
  REGION_AREA: 6.5
  BUNDLE_CONTENTS:
    - "filtered_feature_bc_matrix.h5"
    - "spatial/tissue_positions_list.csv"
    - "spatial/scalefactors_json.json"
    - "spatial/tissue_lowres_image.png"
  
  # Segmentation
  HAS_CELL_SEGMENTATION: true
  CELL_SEGMENTATION_METHOD: "Cellpose"
  CELL_SEGMENTED_OBJECT_TYPE: "Whole cell"
  NUMBER_OF_SEGMENTED_CELLS: 5000
  
  # Analysis
  HAS_DIMENSIONALITY_REDUCTION: true
  DIMENSIONALITY_REDUCTION_METHOD: "UMAP"
  HAS_CLUSTERING: true
  CLUSTERING_METHOD: "Leiden"
  NUMBER_OF_CLUSTERS: 10
  
  # Platform-specific (Visium)
  SLIDE_SERIAL_NUMBER: "V19J01-123"
  CAPTURE_AREA: "A1"
  CYTASSIST_USED: false
  GENOMIC_REFERENCE: "GRCh38"
  
  # Sequencing (capture-based)
  SEQUENCING_INSTRUMENT: "NovaSeq 6000"
  SEQUENCING_CONFIGURATION: "28x91"
  SEQUENCING_DEPTH: "50M reads"
  
  # Quality control
  QC_SPATIAL_UNIT: "spot"
  QC_FEATURE_NUMBER: 4992
  QC_MEAN_READS_PER_FEATURE: 5000.5
  QC_TOTAL_GENES_DETECTED: 12000
  QC_TOTAL_NUMBER_OF_READS: 25000000
```

### Level 4: Interoperable File

```yaml
# Example Spatial Level 4 data
SpatialLevel4:
  COMPONENT: "Spatial Omics"
  FILENAME: "spatial_data.h5ad"
  FILE_FORMAT: "h5ad"
  HTAN_DATA_FILE_ID: "HTA200_2_12348"
  HTAN_PARENT_ID: "HTA200_2_12347"
  
  TOOL_COMPATIBILITY:
    - "anndata"
    - "spatialdata"
  
  NUMBER_OF_FEATURES: 18000
  NUMBER_OF_OBJECTS: 5000
  
  HAS_DIMENSIONALITY_REDUCTION: true
  DIMENSIONALITY_REDUCTION_METHOD: "UMAP"
  
  HAS_CLUSTERING: true
  CLUSTERING_METHOD: "Leiden"
  NUMBER_OF_CLUSTERS: 10
  
  HAS_CELL_TYPE_CALLING: true
  CELL_TYPE_CALLING_METHOD: "SingleR"
  CELL_TYPES:
    - "T cell"
    - "B cell"
    - "Macrophage"
    - "Epithelial cell"
  
  HAS_NORMALISED_ARRAY: true
  NORMALISATION_METHOD: "log normalization"
  HAS_RAW_ARRAY: true
  
  HAS_IMAGE: true
  IMAGE_TYPE: "tiff"
```

### Spatial Panel Information

```yaml
# Example Spatial Panel data
SpatialPanel:
  HTAN_PANEL_ID: "HTA200_2_P0001"
  GENE_SYMBOL: "MYC"
  HGNC_VERSION: "2025-08-01"
  GENE_ID: "ENSG00000136997"
  USER_GENE_NAME: "c-Myc"
```

## Conditional Requirements

The Spatial module implements several conditional requirements using LinkML rules:

### **Level 1**
- `SEQUENCING_FILE_TYPE` is required when `HAS_SEQUENCING` is true
- `IMAGE_TYPES` is required when `HAS_IMAGES` is true
- `HAS_PROBE_SET` is required when `ASSAY_TYPE` is "molecular barcoding"

### **Level 3**
- `TRANSCRIPTOME_TYPE` is required when `RNA_MEASURED` is true
- `PANEL_NAME` and `PANEL_SYNAPSE_ID` are required when `TRANSCRIPTOME_TYPE` is "targeted" OR `PROTEIN_MEASURED` is true
- `SAME_SECTION_IMAGING_CHANNELS` is required when `SAME_SECTION_IMAGING_MODALITY` is "fluoresence"
- Segmentation attributes are required when `HAS_CELL_SEGMENTATION` is true
- Dimensionality reduction method is required when `HAS_DIMENSIONALITY_REDUCTION` is true
- Clustering attributes are required when `HAS_CLUSTERING` is true
- Platform-specific attributes are required based on platform type

### **Level 4**
- `DIMENSIONALITY_REDUCTION_METHOD` is required when `HAS_DIMENSIONALITY_REDUCTION` is true
- `CLUSTERING_METHOD` and `NUMBER_OF_CLUSTERS` are required when `HAS_CLUSTERING` is true
- `CELL_TYPE_CALLING_METHOD` and `CELL_TYPES` are required when `HAS_CELL_TYPE_CALLING` is true
- `NORMALISATION_METHOD` is required when `HAS_NORMALISED_ARRAY` is true
- `IMAGE_TYPE` is required when `HAS_IMAGE` is true

## Validation

### **Pattern Validation**
- **HTAN IDs**: Must match HTAN ID regex pattern
- **Synapse IDs**: `^syn\d+$` for panel Synapse IDs
- **Gene IDs**: `^(ENSG\d+|\d+)$` for Ensembl gene identifiers
- **HGNC Version**: `^\d{4}-\d{2}-\d{2}$` for date format
- **URLs**: Standard HTTP/HTTPS URL pattern for protocol links

### **Minimum Value Constraints**
- `PANEL_SIZE_TOTAL_TARGETS`: ≥ 1
- `REGION_AREA`: ≥ 0.0
- `NUMBER_OF_FEATURES`: ≥ 1
- `NUMBER_OF_OBJECTS`: ≥ 1
- `NUMBER_OF_CLUSTERS`: ≥ 1
- QC metrics: ≥ 0

## Testing

Run module tests:
```bash
cd modules/SpatialOmics
make test
```

## Schema Generation

Generate Python classes and JSON schema:
```bash
cd modules/SpatialOmics
make gen-schema
```

Generate Synapse-compatible flat JSON schema:
```bash
cd modules/SpatialOmics
make gen-synapse-schema
```

