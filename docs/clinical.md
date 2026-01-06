# HTAN Clinical Module

This module contains the clinical data model and related components for the HTAN project.

## Directory Structure

- `domains/` - Contains domain-specific YAML schema definitions for clinical data
  - Each YAML file represents a specific clinical domain (e.g., diagnosis, therapy)
  - These files define the structure and validation rules for each domain

- `src/htan_clinical/` - Contains the Python implementation of the clinical data model
  - `datamodel/` - Contains the generated Python classes for the data model
  - `schema/` - Contains the main schema definition that combines all domains

- `tests/` - Contains unit tests for the clinical module
  - Tests are organized by domain and functionality
  - Includes test data and validation tests

## Schema Organization

- `domains/` contains the source of truth for each clinical domain
- `src/htan_clinical/schema/` contains the combined schema that includes all domains
- Generated files are stored in `project/` and should not be committed to version control

## Testing

Tests are organized by domain and functionality:
- `test_conditional_requirements.py` - Tests for conditional validation rules
- `test_clinical.py` - General clinical data model tests

## Development

1. Update domain YAML files in `domains/`
2. Run `make gen-project` to regenerate schema classes
3. Run tests to verify changes
4. Commit only source files, not generated files 

---

## Schema Documentation

# Clinical

HTAN Clinical Data Model Schema

## Classes

### ClinicalData

Container for all clinical data

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `DEMOGRAPHICS` | Demographics | Yes | Demographic information |
| `DIAGNOSIS` | Diagnosis | Yes | Primary diagnosis information |
| `EXPOSURES` | Exposure | Yes | Exposure history |
| `FAMILY_HISTORY` | FamilyHistory | Yes | Family history of cancer |
| `FOLLOW_UPS` | FollowUp | No | Follow-up observations |
| `HTAN_PARTICIPANT_ID` | string | Yes | HTAN ID associated with a patient based on HTAN ID SOP (Primary Key) |
| `MOLECULAR_TESTS` | MolecularTest | No | Molecular test results |
| `THERAPIES` | Therapy | No | Therapy information |
| `VITAL_STATUS` | VitalStatus | Yes | Vital status information |

## Slots

| Slot | Type | Required | Description |
|------|------|----------|-------------|
| `TISSUE_OR_ORGAN_OF_ORIGIN` | tissue_or_organ_of_origin_uberon_enum | Yes | The tissue or organ of origin for the primary diagnosis, using UBERON codes |
| `caDSR_id` | string | No | The caDSR identifier for this element |

## Enums

### ComponentEnum {#component}

| Value | Description |
|-------|-------------|
| `Clinical` | Clinical data component |
| `Demographics` | Demographics data component |
| `Diagnosis` | Diagnosis data component |
| `Exposure` | Exposure data component |
| `Family History` | Family history data component |
| `Follow-up` | Follow-up data component |
| `Molecular` | Molecular data component |
| `Therapy` | Therapy data component |
| `Vital Status` | Vital status data component |

