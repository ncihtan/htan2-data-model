# HTAN Biospecimen Module

This module implements the HTAN Phase 2 Biospecimen Data Model based on the RFC specification.

## Overview

The Biospecimen module provides comprehensive data modeling for biospecimen metadata including:

- **39 Core Attributes**: All attributes defined in the RFC HTAN Phase 2 Biospecimen Model
- **Conditional Requirements**: Smart validation based on attribute dependencies
- **Enum Validation**: Comprehensive permissible value validation
- **CRDC Alignment**: Integration with Cancer Research Data Commons standards

## Key Features

### Core Attributes
- HTAN identifier validation (HTAN_BIOSPECIMEN_ID, HTAN_PARENT_ID)
- Biospecimen type and acquisition method tracking
- Preservation and processing metadata
- Tissue sample characteristics
- Cellular architecture and pathology data

### Conditional Requirements
- **ACQUISITION_METHOD_OTHER_SPECIFY**: Required when ACQUISITION_METHOD_TYPE=Other
- **FIXATION_DURATION_IN_MINUTES**: Required when PRESERVATION_METHOD=Fixation
- **TISSUE_SAMPLE_TYPE**: Required when BIOSPECIMEN_TYPE=Tissue
- **ANALYTE_TYPE**: Required when BIOSPECIMEN_TYPE=DNA|RNA
- **SLICING_METHOD**: Required when TISSUE_SAMPLE_TYPE=Tissue Section
- **TUMOR_CLASSIFICATION**: Required when SPECIMEN_CELLULAR_ARCHITECTURE=Tumor
- **ICD_O_3_TISSUE_MORPHOLOGY**: Required when SPECIMEN_CELLULAR_ARCHITECTURE=Tumor
- **ICD_10_DISEASE_CODE**: Required when SPECIMEN_CELLULAR_ARCHITECTURE=Precancerous
- **DEGREE_OF_DYSPLASIA**: Required when SPECIMEN_CELLULAR_ARCHITECTURE=Precancerous

### Data Quality Features
- Numeric range validation (percentages, dimensions, ages)
- String length limits for text fields
- Multi-value support for adjacent biospecimen IDs
- CRDC standard alignment with caDSR identifiers

## Usage

### Basic Usage
```python
from htan_biospecimen import BiospecimenData

# Create a biospecimen record
biospecimen = BiospecimenData(
    COMPONENT="Biospecimen",
    HTAN_BIOSPECIMEN_ID="HTA200_2_7001",
    HTAN_PARENT_ID="HTA200_2_B7001",
    BIOSPECIMEN_TYPE="Tissue",
    ACQUISITION_METHOD_TYPE="Surgical Resection",
    SITE_OF_RESECTION_OR_BIOPSY="UBERON:0000948",  # Stomach
    SPECIMEN_LATERALITY="Left",
    PRESERVATION_METHOD="Formalin Fixed",
    SPECIMEN_CELLULAR_ARCHITECTURE="Tumor",
    SHIPPING_CONDITION_TYPE="Frozen"
)
```

### Validation
```python
# Validate the record
try:
    biospecimen.validate()
    print("✅ Biospecimen record is valid")
except ValidationError as e:
    print(f"❌ Validation error: {e}")
```

## Schema Structure

### Main Schema
- `domains/biospecimen.yaml` - Main schema definition
- Inherits from Core module for universal attributes
- Defines BiospecimenData class with all 39 attributes

### Enum Schemas
- `biospecimen_type_enum.yaml` - Biospecimen types
- `acquisition_method_type_enum.yaml` - Acquisition methods
- `specimen_laterality_enum.yaml` - Laterality options
- `preservation_method_enum.yaml` - Preservation methods
- `cellular_architecture_enum.yaml` - Cellular architecture patterns
- `slicing_method_enum.yaml` - Tissue slicing methods
- And 13 additional enum schemas for comprehensive validation

## Development

### Building the Module
```bash
# Generate Python classes and JSON schema
make all

# Generate only Python classes
make python

# Generate only JSON schema
make json-schema

# Validate schema
make validate

# Run tests
make test
```

### Testing
```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=htan_biospecimen
```

## Integration

This module integrates with:
- **Core Module**: Inherits universal HTAN attributes
- **Clinical Module**: Shares participant and diagnosis data
- **WES Module**: Links to sequencing data
- **CRDC Standards**: Aligns with Cancer Research Data Commons

## RFC Compliance

This implementation is based on:
- **RFC HTAN Phase 2 Biospecimen Model**
- **39 Core CDEs** from the specification
- **CRDC Standard Alignment** with caDSR identifiers
- **Conditional Requirements** as specified in the RFC

## Contributing

1. Follow the existing module structure
2. Update enum values as needed
3. Add tests for new functionality
4. Update documentation

## License

This module is part of the HTAN LinkML project and follows the same licensing terms.
