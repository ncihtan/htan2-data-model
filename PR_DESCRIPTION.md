# Core Module Refactoring: CoreFile Separation and Module Architecture Improvements

## Summary

This PR implements a comprehensive refactoring of the HTAN data model core architecture, separating file-based modules from record-based modules, removing redundant fields, and improving the module import chain. This is a foundational change that clarifies module responsibilities and simplifies the data model structure.

## Key Changes

### 1. Module Renaming: Core → CoreFile
- Renamed `modules/Core` directory to `modules/CoreFile` for clarity
- Updated all import paths throughout the codebase
- Maintains backward compatibility with `CoreFileAttributes` class name

### 2. Separation of File-based vs Record-based Modules

#### File-based Modules (inherit from CoreFileAttributes)
- **CoreFile**: Defines universal file attributes (`FILENAME`, `FILE_FORMAT`, `HTAN_DATA_FILE_ID`, `HTAN_PARENT_ID`)
- **Sequencing**: Base sequencing attributes (inherits from BiospecimenAttributes → CoreFileAttributes)
- **WES**: Whole exome sequencing (inherits from BaseSequencingAttributes)
- **scRNA-seq**: Single-cell RNA sequencing (inherits from BaseSequencingAttributes)

#### Record-based Modules (define their own IDs)
- **Clinical**: Defines `HTAN_PARTICIPANT_ID` (moved from CoreFile)
- **Biospecimen**: Defines `HTAN_BIOSPECIMEN_ID` and `HTAN_PARENT_ID` (moved from CoreFile)

### 3. Field Removal and Relocation

#### Removed COMPONENT Field
- Removed redundant `COMPONENT` field from `CoreFileAttributes` and `WESData`
- Component can be determined from schema name, making this field unnecessary
- Updated all documentation and test data

#### Moved ID Fields to Appropriate Modules
- **HTAN_PARTICIPANT_ID**: Moved from CoreFile → Clinical module
- **HTAN_BIOSPECIMEN_ID**: Moved from CoreFile → Biospecimen module  
- **HTAN_PARENT_ID**: 
  - In CoreFile: For file-based modules, requires B or D suffix (biospecimen or data file)
  - In Biospecimen: For record-based biospecimen data, accepts Participant IDs or Biospecimen IDs with B suffix

### 4. HTAN_PARENT_ID Pattern Updates

#### CoreFile Module (File-based)
- **Updated pattern** in `CoreFileAttributes` to require B or D suffix
- **New pattern**: `^(HTA\d+)(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$`
- **Requirement**: Must explicitly indicate biospecimen (B) or data file (D)
- **Examples**:
  - ✅ `HTA200_2_B7001` (biospecimen)
  - ✅ `HTA200_2_D36667` (data file)
  - ❌ `HTA200_2_7001` (no suffix - invalid)

#### Biospecimen Module (Record-based)
- **Updated pattern** to accept Participant IDs or Biospecimen IDs with B suffix
- **New pattern**: `^(HTA([1-9]|1[0-6]|\d{2,}))_((EXT)?([0-9]\d*|0000))$|^(HTA\d+)(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_B\d{1,50}$`
- **Accepts**:
  - ✅ Participant IDs: `HTA200_2`, `HTA1_0000`, `HTA200_EXT001` (any HTA number)
  - ✅ Biospecimen IDs with B suffix: `HTA200_2_B7001`, `HTA200_0000_B7001`

### 5. Import Chain Refactoring
- **Sequencing** now imports `CoreFile` directly
- **WES** and **scRNA-seq** import Sequencing → get CoreFile transitively
- Removed redundant direct CoreFile imports
- Simplified dependency structure

### 6. Test Data Fixes
- Removed file-based fields from Clinical test data (COMPONENT, FILENAME, FILE_FORMAT, HTAN_DATA_FILE_ID, HTAN_PARENT_ID, HTAN_BIOSPECIMEN_ID)
- Clinical is a record-based module and should only have HTAN_PARTICIPANT_ID
- All Clinical tests now passing (11/11)

### 7. Integration with Main Branch
- Merged Sequencing and scRNA-seq modules from main
- Updated all import paths to use CoreFile instead of Core
- Resolved merge conflicts and integrated changes

## Architecture Changes

### Before
```
Core (file-based + record-based IDs mixed)
  ├── CoreFileAttributes (COMPONENT, HTAN_PARTICIPANT_ID, HTAN_BIOSPECIMEN_ID, HTAN_PARENT_ID)
  ├── Clinical (inherited from Core)
  └── Biospecimen (inherited from Core)
```

### After
```
File-based Modules (Inheritance Chain):
┌─────────────────────────────────────────────────────────────┐
│ CoreFile Module                                              │
│   └── CoreFileAttributes                                    │
│       (FILENAME, FILE_FORMAT, HTAN_DATA_FILE_ID,           │
│        HTAN_PARENT_ID with B/D suffix)                      │
└─────────────────────────────────────────────────────────────┘
                      ↑
┌─────────────────────────────────────────────────────────────┐
│ Biospecimen Module                                          │
│   └── BiospecimenAttributes (helper class)                 │
│       (inherits from CoreFileAttributes,                    │
│        adds HTAN_BIOSPECIMEN_ID)                           │
│       Note: Used by file-based modules, not the main        │
│       BiospecimenData class                                 │
└─────────────────────────────────────────────────────────────┘
                      ↑
┌─────────────────────────────────────────────────────────────┐
│ Sequencing Module                                            │
│   └── BaseSequencingAttributes                              │
│       (inherits from BiospecimenAttributes,                 │
│        adds sequencing-specific attributes)                  │
└─────────────────────────────────────────────────────────────┘
                      ↑
        ┌─────────────┴─────────────┐
        │                           │
┌───────────────┐         ┌──────────────────┐
│ WES Module    │         │ scRNA-seq Module │
│ (all levels)  │         │ (all levels)     │
│               │         │                  │
│ - Level 1     │         │ - Level 1         │
│ - Level 2     │         │ - Level 2         │
│ - Level 3     │         │ - Level 3/4       │
└───────────────┘         └──────────────────┘

Record-based Modules (No inheritance, define their own IDs):
┌─────────────────────────────────────────────────────────────┐
│ Clinical Module                                             │
│   └── ClinicalData                                         │
│       (defines HTAN_PARTICIPANT_ID)                        │
│       Does NOT inherit from CoreFileAttributes             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Biospecimen Module                                          │
│   └── BiospecimenData (main class)                         │
│       (defines HTAN_BIOSPECIMEN_ID, HTAN_PARENT_ID)        │
│       Does NOT inherit from CoreFileAttributes             │
│                                                             │
│   Note: Biospecimen module contains BOTH:                   │
│   - BiospecimenAttributes (file-based, inherits CoreFile)   │
│   - BiospecimenData (record-based, no inheritance)          │
└─────────────────────────────────────────────────────────────┘
```

## Testing

All tests passing:
- ✅ Biospecimen: 13/13 tests passing
- ✅ WES: 5/5 tests passing
- ✅ Sequencing: 7/7 tests passing
- ✅ scRNA-seq: 11/11 tests passing
- ✅ Clinical: 11/11 tests passing

## Files Changed

### Schema Files
- `modules/Core/domains/core.yaml` → `modules/CoreFile/domains/core.yaml` (renamed, updated)
- `modules/Biospecimen/domains/biospecimen.yaml` - Added BiospecimenAttributes, updated HTAN_PARENT_ID pattern to accept participant IDs
- `modules/Clinical/domains/clinical.yaml` - Added HTAN_PARTICIPANT_ID, removed CoreFile inheritance
- `modules/Sequencing/domains/sequencing.yaml` - Added CoreFile import
- `modules/scRNA-seq/domains/scrna_seq.yaml` - Removed redundant CoreFile import
- `modules/WES/domains/wes.yaml` - Removed COMPONENT field

### Documentation
- `modules/CoreFile/README.md` - Complete rewrite with new architecture
- `README.md` - Updated module references
- `CONTRIBUTING.md` - Updated examples
- Added module inheritance diagram

### Tests
- `modules/Biospecimen/tests/test_biospecimen.py` - Updated to reflect record-based module
- `modules/Clinical/tests/test_conditional_requirements.yaml` - Removed COMPONENT field
- `modules/Clinical/tests/test_data/valid/test_clinical_data.yaml` - Removed file-based fields (COMPONENT, FILENAME, FILE_FORMAT, HTAN_DATA_FILE_ID, HTAN_PARENT_ID, HTAN_BIOSPECIMEN_ID)
- `modules/Clinical/tests/test_data/invalid/test_invalid_data.yaml` - Removed file-based fields

### Generated Files
- Regenerated all Python schema classes
- Updated JSON schemas
- Removed old schema files

## Migration Notes

⚠️ **Breaking Changes**:

1. **Module Path**: `modules/Core` → `modules/CoreFile`
   - Update all import paths: `../../Core/domains/core` → `../../CoreFile/domains/core`

2. **HTAN_PARENT_ID Pattern**: Now requires B or D suffix
   - **Before**: `HTA200_2_7001` (valid)
   - **After**: `HTA200_2_B7001` or `HTA200_2_D36667` (required)

3. **COMPONENT Field**: Removed from all schemas
   - Remove COMPONENT from all data files
   - Component can be inferred from schema name

4. **ID Fields**: Moved to appropriate modules
   - `HTAN_PARTICIPANT_ID`: Now only in Clinical module
   - `HTAN_BIOSPECIMEN_ID`: Now only in Biospecimen module
   - `HTAN_PARENT_ID`: 
     - In CoreFile: Requires B or D suffix (biospecimen or data file)
     - In Biospecimen: Accepts Participant IDs or Biospecimen IDs with B suffix
   - File-based modules use `HTAN_DATA_FILE_ID` from CoreFile

5. **Test Data Updates**: 
   - Removed file-based fields from Clinical test data (Clinical is record-based)
   - All Clinical tests now passing

## Benefits

1. **Clear Separation**: File-based vs record-based modules are now distinct
2. **Reduced Redundancy**: Removed COMPONENT field, moved IDs to appropriate modules
3. **Simplified Imports**: Transitive imports through Sequencing module
4. **Better Validation**: HTAN_PARENT_ID requires explicit B/D suffix
5. **Improved Documentation**: Clear module inheritance diagram and updated READMEs

