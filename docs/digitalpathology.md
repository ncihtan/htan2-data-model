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
- **Species**: NCBI Taxonomy ID for the imaged specimen

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
  # Note: Organ/Tissue, Tissue Fixative, and Embedding Medium are biospecimen attributes
  # and should be retrieved from the Biospecimen record via HTAN_PARENT_ID
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

## Integration

This module:
- **Inherits from BaseImagingAttributes**: Uses `BaseImagingAttributes` (which inherits from `CoreFileAttributes`) for common imaging attributes
- **Aligns with CRDC**: Matches CRDC Non-DICOM Pathology standards
- **Supports Bio-Formats/OpenSlide**: Ensures compatibility with standard tools
- **Maintains HTAN IDs**: Uses standard HTAN identifier patterns
- **Links to Biospecimen**: Organ/Tissue, Tissue Fixative, and Embedding Medium attributes are retrieved from the Biospecimen record via `HTAN_PARENT_ID`

## References

- [Bio-Formats Documentation](https://bio-formats.readthedocs.io/)
- [OpenSlide Python](https://openslide.org/api/python/)


---

## Schema Documentation

# DigitalPathology

HTAN Digital Pathology Data Model Schema for Phase 2

## Classes

### DigitalPathologyData

Container for digital pathology imaging data

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ANNOTATION_TYPE` | AnnotationType<br/>`Artifact`, `Cell`, `Nucleus`, `ROI`, `Tissue` | No | What types of annotation are contained in the image |
| `FILE_FORMAT` | string | Yes | Format of the imaging file. Must be compatible with Bio-Formats or OpenSlide Python. |
| `HAS_ANNOTATIONS` | boolean | Yes | Does the image contain annotations |

## Enums

### AnnotationType

| Value | Description |
|-------|-------------|
| `Artifact` | Artifact annotation |
| `Cell` | Cell annotation |
| `Nucleus` | Nucleus annotation |
| `ROI` | Region of Interest annotation |
| `Tissue` | Tissue annotation |

