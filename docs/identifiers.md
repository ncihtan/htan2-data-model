# HTAN Identifiers

This page lists all HTAN identifier fields and their validation patterns.

## Identifier Patterns

| Identifier | Module | Pattern | Required | Description |
|------------|--------|---------|----------|-------------|
| `HTAN_PARTICIPANT_ID` | Clinical | <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})$</code> | Yes | HTAN ID associated with a patient based on HTAN ID SOP (Primary Key) |
| `HTAN_BIOSPECIMEN_ID` | Biospecimen | <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(B[0-9]{1,20})$</code> | Yes | HTAN Biospecimen ID (Primary Key) |
| `HTAN_PARENT_ID (Biospecimen)` | Biospecimen | <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})(?:_(B[0-9]{1,20}))?$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (Participant ID or Biospecimen ID with B suffix). Supports HTA200-229 for phase 2. |
| `HTAN_DATA_FILE_ID` | CoreFile (all file-based modules) | <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | CoreFile (all file-based modules) | <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |
| `HTAN_PANEL_ID` | SpatialOmics | <code>^(HTA([1-9]\|1[0-6]))_((EXT)?([0-9]\d*\|0000))_([0-9]\d*\|0000)$</code> | Yes | Unique identifier for the panel |

## Notes

- All HTAN identifiers support Phase 2 center IDs (HTA200-229)
- Total identifier length is limited to 50 characters
- Patterns use regular expression syntax
- File-based modules inherit `HTAN_DATA_FILE_ID` and `HTAN_PARENT_ID` from CoreFileAttributes
