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
| `TISSUE_OR_ORGAN_OF_ORIGIN` | See [tissue_or_organ_of_origin_uberon_enum](#tissue-or-organ-of-origin-uberon-) enum below | Yes | The tissue or organ of origin for the primary diagnosis, using UBERON codes |
| `caDSR_id` | string | No | The caDSR identifier for this element |

