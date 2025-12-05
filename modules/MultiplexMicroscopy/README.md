# HTAN Multiplex Microscopy

Multiplex Microscopy module for HTAN Phase 2 data model, implementing standards for multiplexed tissue imaging assays including CODEX, CyCIF, IMC, MIBI, and other multiplex imaging technologies.

## Purpose

This module implements the Multiplex Microscopy RFC for HTAN Phase 2, which supports:

1. **Multiplex Imaging Assays**: CODEX, CyCIF, IMC, MIBI, MERFISH, GeoMX-DSP, and more
2. **Channel Metadata**: Detailed metadata for each channel in multiplex images
3. **Image Dimensions**: Physical size and pixel dimensions (X, Y, Z, C, T)
4. **CRDC Alignment**: HTAN metadata standards align with CRDC Multiplex Microscopy metadata standards
5. **Three Data Levels**: Level 2 (imaging + channel metadata), Level 3 (segmentation masks), Level 4 (cell-by-feature tables)

## Structure

### **Domain Files**
- `domains/multiplex_microscopy.yaml` - Main schema file (imports all levels)
- `domains/level_2.yaml` - Level 2 schema (imaging data with channel metadata)
- `domains/level_3.yaml` - Level 3 schema (segmentation masks)
- `domains/level_4.yaml` - Level 4 schema (cell-by-feature tables)

### **Key Attributes**

#### **Shared with Digital Pathology**
- **Experimental Strategy**: Pathological experimental strategy
- **De-identification**: Method type, description, and software used
- **Imaging Equipment**: Manufacturer, model, and software information
- **Protocols**: Citation/DOI and imaging protocol references
- **Staining**: Method used for tissue staining
- **Microscopy**: Objective, magnification, immersion medium, numerical aperture
- **Quality Control**: QC status and comments
- **Biospecimen**: Species, organ/tissue, fixative, and embedding medium

#### **Multiplex Microscopy Specific**
- **Imaging Assay Type**: Type of multiplex imaging assay (CODEX, CyCIF, IMC, etc.)
- **Working Distance**: Lens working distance
- **Pyramid**: Whether the image contains a pyramid structure
- **Physical Size**: Pixel physical size in X, Y, Z dimensions (microns)
- **Size Dimensions**: Number of pixels/channels/timepoints (X, Y, Z, C, T)
- **Channel Metadata ID**: Reference to channel metadata file
- **Channel Metadata**: Multivalued list of channel-specific information

#### **Channel Metadata Attributes**
- Channel ID and name
- Cycle and sub-cycle numbers
- Target and antibody information
- RRID identifier (with pattern validation)
- Fluorophore and clone information
- Vendor information (lot, catalog number)
- Optical properties (excitation/emission wavelengths and bandwidths)
- Metal isotope information (for IMC)
- Oligo barcode information (for sequencing-based methods)
- Dilution and concentration

### **Data Levels**

#### **Level 2: Imaging Data with Channel Metadata**
- **Images**: Tiled and pyramidal OME-TIFF format (preferred)
- **Channel Metadata**: CSV file containing standardized channel metadata
- **Attributes**: All shared attributes + Multiplex Microscopy specific attributes (imaging assay type, physical sizes, dimensions, etc.)

#### **Level 3: Segmentation Masks**
- **Format**: OME-TIFF segmentation masks
- **Attributes**: 
  - Segmentation workflow type, URL, and version
  - Segmentation method and parameters
  - Segmentation annotation type (Cell, Nucleus, Tissue, ROI)
  - File format validation (must be ome-tiff)

#### **Level 4: Cell-by-Feature Tables**
- **Format**: CSV or h5ad files
- **Attributes**:
  - Feature extraction workflow type, URL, and version
  - Matrix type (Raw Counts, Normalized, Scaled, etc.)
  - Feature extraction method and parameters
  - Number of features and objects
  - File format validation (must be csv or h5ad)

### **Supported Formats**
- `.ome-tiff`, `.qptiff`, `.svs`, `.tif`, `.dcm`, `.ndpi`
- `.vms`, `.vmu`, `.scn`, `.mrxs`, `.tiff`, `.svslide`
- `.bit`, `.czi`

## Usage

### Level 2: Imaging Data with Channel Metadata

```yaml
# Example Multiplex Microscopy Level 2 data
MultiplexMicroscopyLevel2:
  COMPONENT: "Multiplex Microscopy"
  FILENAME: "sample_CODEX.ome.tiff"
  FILE_FORMAT: "ome.tiff"
  HTAN_PARTICIPANT_ID: "HTA200_2"
  HTAN_DATA_FILE_ID: "HTA200_2_12346"
  HTAN_PARENT_ID: "HTA200_2_B7001"
  
  # Required shared attributes
  EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES: "Pathological"
  DE_IDENTIFICATION_METHOD_TYPE: "Automatic"
  LICENSE: "CC BY 4.0"
  IMAGE_MODALITY: "SM"
  IMAGING_EQUIPMENT_MANUFACTURER: "Leica Microsystems"
  CITATION_OR_DOI: "https://doi.org/10.1000/example"
  STAINING_METHOD: "CODEX"
  OBJECTIVE: "Leica HC PL APO 20x/0.75"
  NOMINAL_MAGNIFICATION: 20.0
  PASSED_QC: true
  QC_COMMENT: "Image quality acceptable"
  SPECIES: "9606 (Homo sapiens)"
  ORGAN_OR_TISSUE: "C25.9"
  TISSUE_FIXATIVE: "Formalin"
  EMBEDDING_MEDIUM: "FFPE"
  
  # Multiplex Microscopy specific
  IMAGING_ASSAY_TYPE: "CODEX"
  PHYSICAL_SIZE_X: 0.325
  PHYSICAL_SIZE_Y: 0.325
  SIZE_X: 2048
  SIZE_Y: 2048
  SIZE_C: 50
  SIZE_T: 1
  CHANNEL_METADATA_ID: "syn12345678"
  
  # Channel metadata (multivalued)
  CHANNEL_METADATA:
    - CHANNEL_ID: "ch001"
      CHANNEL_NAME: "CD3"
      TARGET_NAME: "CD3"
      ANTIBODY_NAME: "Anti-CD3"
      RRID_IDENTIFIER: "RRID:AB_123456"
      EXCITATION_WAVELENGTH: 488.0
      EMISSION_WAVELENGTH: 520.0
    - CHANNEL_ID: "ch002"
      CHANNEL_NAME: "CD4"
      TARGET_NAME: "CD4"
      ANTIBODY_NAME: "Anti-CD4"
      RRID_IDENTIFIER: "RRID:AB_123457"
      EXCITATION_WAVELENGTH: 488.0
      EMISSION_WAVELENGTH: 520.0
```

### Level 3: Segmentation Masks

```yaml
# Example Multiplex Microscopy Level 3 data
MultiplexMicroscopyLevel3:
  COMPONENT: "Multiplex Microscopy"
  FILENAME: "sample_CODEX_segmentation.ome.tiff"
  FILE_FORMAT: "ome-tiff"
  HTAN_DATA_FILE_ID: "HTA200_2_12347"
  HTAN_PARENT_ID: "HTA200_2_12346"  # Parent is Level 2 file
  
  SEGMENTATION_WORKFLOW_TYPE: "CellPose"
  SEGMENTATION_WORKFLOW_URL: "https://github.com/MouseLand/cellpose"
  SEGMENTATION_WORKFLOW_VERSION: "2.0"
  SEGMENTATION_METHOD: "CellPose 2.0 with cyto2 model"
  SEGMENTATION_PARAMETERS: "diameter=30, flow_threshold=0.4, cellprob_threshold=0.0"
  SEGMENTATION_ANNOTATION_TYPE: "Cell"
```

### Level 4: Cell-by-Feature Tables

```yaml
# Example Multiplex Microscopy Level 4 data
MultiplexMicroscopyLevel4:
  COMPONENT: "Multiplex Microscopy"
  FILENAME: "sample_CODEX_features.csv"
  FILE_FORMAT: "csv"
  HTAN_DATA_FILE_ID: "HTA200_2_12348"
  HTAN_PARENT_ID: "HTA200_2_12347"  # Parent is Level 3 file
  
  FEATURE_EXTRACTION_WORKFLOW_TYPE: "Custom Python Script"
  FEATURE_EXTRACTION_WORKFLOW_URL: "https://github.com/example/feature_extraction"
  FEATURE_EXTRACTION_WORKFLOW_VERSION: "1.0"
  MATRIX_TYPE: "Raw Counts"
  FEATURE_EXTRACTION_METHOD: "Mean intensity per channel"
  FEATURE_EXTRACTION_PARAMETERS: "channels: CD3, CD4, CD8, CD20, DAPI"
  NUMBER_OF_FEATURES: 50
  NUMBER_OF_OBJECTS: 15234
```

## Testing

Run module tests:
```bash
cd modules/MultiplexMicroscopy
make test
```

## Schema Generation

Generate Python classes and JSON schema:
```bash
cd modules/MultiplexMicroscopy
make gen-schema
```

## Validation Rules

### **Required Fields**
All attributes marked as `required: true` must be provided.

### **Conditional Requirements**
- `DE_IDENTIFICATION_METHOD_DESCRIPTION`: Required if `DE_IDENTIFICATION_METHOD_TYPE` is not "Not Applicable"

### **Pattern Validation**
- `ORGAN_OR_TISSUE`: Must match ICD-O pattern `^[A-Z][0-9]{2}\\.[0-9]{1,2}$`
- `RRID_IDENTIFIER`: Must match pattern `^RRID:AB_\\d+$`

### **Value Constraints**
- `NOMINAL_MAGNIFICATION`: Must be >= 1.0
- `LENS_NUMERICAL_APERTURE`: Must be >= 0.0
- `PHYSICAL_SIZE_X`, `PHYSICAL_SIZE_Y`, `PHYSICAL_SIZE_Z`: Must be >= 0.0
- `SIZE_X`, `SIZE_Y`, `SIZE_Z`, `SIZE_C`, `SIZE_T`: Must be >= 1

## Enums

### **ImagingAssayType**
- CODEX, CyCIF, ExSeq, GeoMX-DSP, H&E, IHC, IMC, MIBI, MERFISH, MxIF, mIHC, Not Applicable, SABER, t-CyCIF

### **StainingMethod**
- Same values as ImagingAssayType

### **ImmersionMedium**
- Air, Glycerol, Oil, Other, Water

### **MetalIsotopeElement**
- Complete periodic table of elements (H through Og)

## Integration

This module:
- **Inherits from Core**: Uses `CoreFileAttributes` for universal HTAN attributes
- **Aligns with CRDC**: Matches CRDC Multiplex Microscopy standards
- **Supports Bio-Formats/OpenSlide**: Ensures compatibility with standard tools
- **Maintains HTAN IDs**: Uses standard HTAN identifier patterns
- **Channel Metadata**: Supports multivalued channel metadata for detailed channel information

## References

- [HTAN Multiplex Microscopy RFC](https://docs.google.com/document/d/example)
- [CRDC Multiplex Microscopy Template](https://example.com)
- [Bio-Formats Documentation](https://bio-formats.readthedocs.io/)
- [OpenSlide Python](https://openslide.org/api/python/)

