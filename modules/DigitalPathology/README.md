# HTAN Digital Pathology

Digital Pathology module for HTAN Phase 2 data model, implementing standards for whole-slide imaging (WSI) derived from H&E and other tissue-based assays.

## Purpose

This module implements the Digital Pathology RFC for HTAN Phase 2, which introduces four major changes from Phase 1:

1. **Separation**: Digital pathology and multiplexed tissue imaging are split into separate modules
2. **Single data level**: Digital Pathology has only one data level (Level 2)
3. **Format compatibility**: Data must be submitted in formats compatible with Bio-Formats or OpenSlide Python
4. **CRDC alignment**: HTAN metadata standards align with CRDC Non-DICOM Pathology Imaging metadata standards

## Structure

### **Domain Files**
- `domains/digital_pathology.yaml` - Main schema file
- `domains/tissue_fixative_enum.yaml` - Tissue fixative enumeration
- `domains/embedding_medium_enum.yaml` - Embedding medium enumeration

### **Key Attributes**
- **Experimental Strategy**: Pathological experimental strategy
- **De-identification**: Method type, description, and software used
- **Imaging Equipment**: Manufacturer, model, and software information
- **Protocols**: Citation/DOI and imaging protocol references
- **Staining**: Method used for tissue staining
- **Microscopy**: Objective, magnification, immersion medium, numerical aperture
- **Quality Control**: QC status, comments, and validation checks
- **Annotations**: Presence and types of annotations
- **Slide Labels**: Presence and redaction status
- **Biospecimen**: Species, organ/tissue, fixative, and embedding medium

### **Supported Formats**
- `.ome-tiff`, `.qptiff`, `.svs`, `.tif`, `.dcm`, `.ndpi`
- `.vms`, `.vmu`, `.scn`, `.mrxs`, `.tiff`, `.svslide`
- `.bit`, `.czi`

## Usage

```yaml
# Example Digital Pathology data
DigitalPathologyData:
  COMPONENT: "Digital Pathology"
  FILENAME: "sample_H&E.ome.tiff"
  FILE_FORMAT: "ome.tiff"
  HTAN_PARTICIPANT_ID: "HTA200_2"
  HTAN_DATA_FILE_ID: "HTA200_2_12345"
  HTAN_PARENT_ID: "HTA200_2_B7001"
  
  # Required attributes
  EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES: "Pathological"
  DE_IDENTIFICATION_METHOD_TYPE: "Automatic"
  LICENSE: "CC BY 4.0"
  IMAGE_MODALITY: "SM"
  IMAGING_EQUIPMENT_MANUFACTURER: "Leica Microsystems"
  CITATION_OR_DOI: "https://doi.org/10.1000/example"
  STAINING_METHOD: "H&E"
  OBJECTIVE: "Leica HC PL APO 20x/0.75"
  NOMINAL_MAGNIFICATION: 20.0
  HAS_ANNOTATIONS: true
  ANNOTATION_TYPE: "Tissue"
  HAS_SLIDE_LABEL: true
  SLIDE_LABEL_REDACTED: true
  DE_IDENTIFIED: true
  PASSED_QC: true
  QC_COMMENT: "Image quality acceptable"
  SPECIES: "9606 (Homo sapiens)"
  ORGAN_OR_TISSUE: "C25.9"
  TISSUE_FIXATIVE: "Formalin"
  EMBEDDING_MEDIUM: "FFPE"
```

## Testing

Run module tests:
```bash
cd modules/DigitalPathology
make test
```

## Schema Generation

Generate Python classes and JSON schema:
```bash
cd modules/DigitalPathology
make gen-schema
```

## Validation Rules

### **Required Fields**
All attributes marked as `required: true` must be provided.

### **Conditional Requirements**
- `DE_IDENTIFICATION_METHOD_DESCRIPTION`: Required if `DE_IDENTIFICATION_METHOD_TYPE` is not "Not Applicable"
- `SLIDE_LABEL_REDACTED`: Required if `HAS_SLIDE_LABEL` is true
- `ANNOTATION_TYPE`: Required if `HAS_ANNOTATIONS` is true

### **Pattern Validation**
- `ORGAN_OR_TISSUE`: Must match ICD-O pattern `^[A-Z][0-9]{2}\\.[0-9]{1,2}$`

### **Value Constraints**
- `NOMINAL_MAGNIFICATION`: Must be > 1
- `LENS_NUMERICAL_APERTURE`: Must be > 0

## Enums

### **DeIdentificationMethodType**
- Automatic, Manual, Not Applicable, Semiautomatic

### **StainingMethod**
- CODEX, CyCIF, ExSeq, GeoMX-DSP, H&E, IHC, IMC, MIBI, MERFISH, MxIF, mIHC, Not Applicable, SABER, t-CyCIF

### **ImmersionMedium**
- Air, Glycerol, Oil, Other, Water

### **AnnotationType**
- Artifact, Cell, Nucleus, ROI, Tissue

### **TissueFixative**
- Comprehensive list including Formalin, Ethanol, Cryopreserved, Fresh, etc.

### **EmbeddingMedium**
- FFPE, OCT, Cryopreserved, Fresh, Frozen, etc.

## Integration

This module:
- **Inherits from Core**: Uses `CoreFileAttributes` for universal HTAN attributes
- **Aligns with CRDC**: Matches CRDC Non-DICOM Pathology standards
- **Supports Bio-Formats/OpenSlide**: Ensures compatibility with standard tools
- **Maintains HTAN IDs**: Uses standard HTAN identifier patterns

## References

- [HTAN Digital Pathology RFC](https://docs.google.com/document/d/example)
- [CRDC Non-DICOM Pathology Template](https://example.com)
- [Bio-Formats Documentation](https://bio-formats.readthedocs.io/)
- [OpenSlide Python](https://openslide.org/api/python/)
