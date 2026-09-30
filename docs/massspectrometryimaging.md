# MassSpectrometryImaging

HTAN Mass Spectrometry Imaging (MSI) Data Model Schema for Phase 2 - All Levels

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MassSpectrometryImagingLevel1

**Level 1 raw spectral data - continuous (profile) imzML acquisition annotations. The paired .ibd binary is an unannotated companion carrying only CoreFileAttributes.**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the file; imzML (continuous/profile) at Level 1 |
| `FILENAME` | string | Yes | Name of the file. Must end with .imzML |
| `MS_IONIZATION_TECHNIQUE` | [MsIonizationTechniqueEnum](#msionizationtechniqueenum) | Yes | Ionization technique used. For timsTOF Flex, distinguish MALDI from MALDI_2. |
| `MASS_ANALYZER_TYPE` | [MassAnalyzerTypeEnum](#massanalyzertypeenum) | Yes | Type of mass analyzer. |
| `MASS_ANALYSIS_POLARITY` | [MassAnalysisPolarityEnum](#massanalysispolarityenum) | Yes | Ion polarity mode for acquisition. |
| `ANALYTE_CLASS` | [AnalyteClassEnum](#analyteclassenum) | Yes | Molecular class(es) targeted by the acquisition. One or more values may be specified (e.g., a sequential metabolites/glycans/peptides workflow records each class). |
| `IS_TARGETED` | boolean | Yes | Whether acquisition targets a pre-specified set of molecules (true) or is untargeted (false). |
| `ACQUISITION_INSTRUMENT_VENDOR` | string | Yes | Manufacturer of the mass spectrometer (e.g., Bruker, Waters, Thermo). |
| `ACQUISITION_INSTRUMENT_MODEL` | string | Yes | Specific instrument model (e.g., timsTOF Flex, Q Exactive). |
| `PIXEL_SIZE_X_UM` | float | Yes | Pixel pitch in the X dimension (micrometers); corresponds to PSI-MS CV MS:1000042. |
| `PIXEL_SIZE_Y_UM` | float | Yes | Pixel pitch in the Y dimension (micrometers); corresponds to PSI-MS CV MS:1000043. |
| `MASS_TO_CHARGE_RANGE_LOW_VALUE` | float | Yes | Lower m/z boundary of the acquisition range. |
| `MASS_TO_CHARGE_RANGE_HIGH_VALUE` | float | Yes | Upper m/z boundary of the acquisition range. |
| `ION_MOBILITY` | boolean | Yes | Whether ion mobility separation was applied during acquisition. |
| `SPECTRUM_TYPE` | [SpectrumTypeEnum](#spectrumtypeenum) | Yes | Spectral representation type. Level 1 is always PROFILE (continuous/profile imzML); the range enum permits only PROFILE, so this is enforced at the schema level. |
| `MASS_RESOLVING_POWER` | float | Yes | Mass resolving power (m/delta-m) of the instrument. May be non-integer (e.g., 140000.5) and can exceed 1e6 on FTICR/Orbitrap. |
| `MASS_TO_CHARGE_RESOLVING_POWER` | float | No | m/z value at which MASS_RESOLVING_POWER is specified. Recommended. |
| `MS_SCAN_MODE` | [MsScanModeEnum](#msscanmodeenum) | Yes | Scan mode of the mass analyser (TOF-specific; NOT_APPLICABLE for non-TOF analysers). |
| `CALIBRATION_TYPE` | [CalibrationTypeEnum](#calibrationtypeenum) | Yes | Type of mass calibration applied. |
| `CALIBRANT_MASSES` | string | Yes | Comma-separated list of calibrant m/z values used (e.g., "622.0290, 922.0098"). |
| `TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE` | float | Yes | Elapsed time since the last instrument mass calibration. May be fractional (e.g., 1.5 hours); pair with TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT. |
| `TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT` | [TimeUnitEnum](#timeunitenum) | Yes | Unit for TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE. |
| `SOFTWARE_AND_VERSION` | string | Yes | Name and version of the acquisition software used to collect data (e.g., flexImaging 7.0, timsControl 5.1). Re-specified at each level. |
| `PROTOCOL_LINK` | string | No | URL or DOI of the tissue preparation and matrix deposition protocol (e.g., protocols.io link). Recommended. Re-specified at each level. |
| `IBD_FILE_UUID` | string | Yes | UUID embedded in the .imzML XML linking to the paired .ibd binary file. Accepts canonical hyphenated or 32-hex form, case-insensitive, with optional enclosing braces. |
| `PREPARATION_MATRIX` | [PreparationMatrixEnum](#preparationmatrixenum) | Conditional: Matrix preparation attributes are required for matrix-based (MALDI-family) ionization techniques (MALDI, MALDI_2, IR_MALDESI) | Matrix compound applied to the tissue section. Conditionally required for MALDI-family techniques (MALDI, MALDI_2, IR_MALDESI); use OTHER for IR-MALDESI (ice/endogenous-water matrix). Set NOT_APPLICABLE for non-matrix modalities (DESI, SIMS). |
| `MATRIX_DEPOSITION_METHOD` | [MatrixDepositionMethodEnum](#matrixdepositionmethodenum) | Conditional: Matrix preparation attributes are required for matrix-based (MALDI-family) ionization techniques (MALDI, MALDI_2, IR_MALDESI) | Method used to apply the matrix to tissue. Conditionally required for MALDI-family techniques (MALDI, MALDI_2, IR_MALDESI). |
| `PREPARATION_INSTRUMENT_VENDOR` | string | Conditional: Matrix preparation attributes are required for matrix-based (MALDI-family) ionization techniques (MALDI, MALDI_2, IR_MALDESI) | Manufacturer of the matrix deposition instrument. Conditionally required for MALDI-family techniques (MALDI, MALDI_2, IR_MALDESI). |
| `PREPARATION_INSTRUMENT_MODEL` | string | Conditional: Matrix preparation attributes are required for matrix-based (MALDI-family) ionization techniques (MALDI, MALDI_2, IR_MALDESI) | Model of the matrix deposition instrument. Conditionally required for MALDI-family techniques (MALDI, MALDI_2, IR_MALDESI). |
| `ANALYTE_ACQUISITION_ORDER` | integer | No | 1-based order of this run within a sequential multi-analyte session on the same tissue section. Recommended; required when multiple analyte classes are acquired from one section. |
| `PRE_ACQUISITION_TREATMENT` | [PreAcquisitionTreatmentEnum](#preacquisitiontreatmentenum) | No | Enzymatic or chemical treatment applied to the section prior to this acquisition run. Recommended. |
| `PASSED_QC` | boolean | Yes | Whether the file passed post-acquisition quality control at Level 1. |
| `QC_COMMENT` | string | No | Free-text quality-control comment for Level 1. |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MassSpectrometryImagingLevel2

**Level 2 processed spectral data - centroided imzML after baseline correction, peak picking, mass alignment, and normalization. The paired .ibd binary is an unannotated companion.**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the file; processed (centroided) imzML at Level 2 |
| `FILENAME` | string | Yes | Name of the file. Must end with .imzML |
| `SOFTWARE_AND_VERSION` | string | Yes | Name and version of the spectral processing software used at this level (e.g., SCiLS Lab 2024, Cardinal 3.4). Re-specified at each level; not propagated from L1. |
| `BASELINE_CORRECTION_METHOD` | [BaselineCorrectionMethodEnum](#baselinecorrectionmethodenum) | Yes | Baseline correction algorithm applied prior to peak picking. |
| `PEAK_PICKING_METHOD` | string | Yes | Peak detection algorithm used (e.g., centroid, continuous wavelet transform). |
| `PEAK_PICKING_SNR_THRESHOLD` | float | Yes | Signal-to-noise ratio threshold applied during peak picking. |
| `NORMALIZATION_METHOD` | [NormalizationMethodEnum](#normalizationmethodenum) | Yes | Spectral intensity normalization method applied. |
| `MASS_ALIGNMENT_METHOD` | string | Yes | Algorithm used to align m/z peaks across all pixels (e.g., lock-mass, landmark-based). |
| `MASS_TOLERANCE_PPM` | float | Yes | Mass tolerance (ppm) applied during peak binning and alignment. |
| `SMOOTHING_METHOD` | [SmoothingMethodEnum](#smoothingmethodenum) | No | Spectral smoothing algorithm applied; NONE if no smoothing. |
| `PROTOCOL_LINK` | string | No | URL or DOI of the data processing and analysis protocol for this level. Recommended. Re-specified at each level; not propagated from L1. |
| `MEDIAN_TIC` | float | Yes | Median total ion current across all pixels after normalization. |
| `TIC_CV` | float | Yes | Coefficient of variation (%) of the total ion current across pixels; acceptance threshold <30%. |
| `MASS_ACCURACY_PPM` | float | Yes | Mean absolute mass error (ppm) measured against calibrant peaks. |
| `PIXEL_COMPLETION_RATE` | float | Yes | Fraction (0-100%) of expected raster pixels successfully acquired. |
| `NUM_DETECTED_PEAKS` | integer | Yes | Total number of unique m/z features detected after peak picking across the dataset. |
| `PASSED_QC` | boolean | Yes | Whether the file passed processing-stage quality control at Level 2. |
| `QC_COMMENT` | string | No | Free-text quality-control comment for Level 2. |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MassSpectrometryImagingLevel3

**Level 3 annotation-filtered OME-TIFF. Channels include only annotated m/z values plus biologically relevant unknowns. Per-channel molecular detail is carried by the companion Molecular Assignments RecordSet.**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the file; OME-TIFF at Level 3 |
| `FILENAME` | string | Yes | Name of the file. Must end with .ome.tif or .ome.tiff |
| `NUM_ANNOTATED_CHANNELS` | integer | Yes | Number of OME-TIFF channels with a confirmed molecular assignment (confidence levels 1-3). |
| `NUM_UNKNOWN_CHANNELS` | integer | Yes | Number of OME-TIFF channels retained as biologically relevant unknowns (confidence level 4). |
| `SOFTWARE_AND_VERSION` | string | Yes | Name and version of the annotation software used at this level. Re-specified at each level; not propagated. |
| `PROTOCOL_LINK` | string | No | URL or DOI of the molecular annotation protocol for this level. Recommended; documents the annotation method per RFC section 4.3. |
| `PASSED_QC` | boolean | Yes | Whether the file passed quality control at Level 3. |
| `QC_COMMENT` | string | No | Free-text quality-control comment for Level 3. |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MassSpectrometryImagingLevel4

**Level 4 segmented and region/cell-type quantified output (optional). Includes a segmentation mask OME-TIFF and/or a region quantification table.**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the file; OME-TIFF segmentation mask or CSV quantification table |
| `FILENAME` | string | Yes | Name of the file. Must end with .ome.tif, .ome.tiff, or .csv |
| `SEGMENTATION_METHOD` | string | Yes | Algorithm or tool used for tissue or cell-type segmentation (e.g., K-means on TIC image, H&E-guided). |
| `SEGMENTATION_CLASS_COUNT` | integer | Yes | Number of distinct tissue regions or cell types identified by the segmentation. |
| `SEGMENTATION_REFERENCE_MODALITY` | [SegmentationReferenceModalityEnum](#segmentationreferencemodalityenum) | Yes | Modality whose segmentation output was projected onto the MSI image. |
| `PASSED_QC` | boolean | Yes | Whether the file passed quality control at Level 4. |
| `QC_COMMENT` | string | No | Free-text quality-control comment for Level 4. |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MolecularAssignment

**A single molecular assignment row corresponding to one OME-TIFF channel in a Level 3 file. The unique row key is (HTAN_DATA_FILE_ID, CHANNEL_INDEX). Channel count must equal RecordSet row count (enforced by the DCC validator).**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `HTAN_DATA_FILE_ID` | string | Yes | Foreign key to the parent Level 3 OME-TIFF file ID (same value for all rows in a RecordSet). This is the sole provenance anchor for the RecordSet - biospecimen provenance is resolved indirectly via the parent Level 3 file's HTAN_PARENT_ID chain (mirrors the ChannelMetadata pattern in Multiplex Microscopy, which also has no direct HTAN_PARENT_ID). Follows the HTAN data file ID pattern (D-suffix). |
| `CHANNEL_INDEX` | integer | Yes | 1-based channel number matching OME-TIFF channel order; must be unique per file. |
| `MZ_OBSERVED` | float | Yes | Observed mass-to-charge ratio (greater than 0; 4 decimal places minimum). |
| `MZ_THEORETICAL` | float | Conditional: MZ_THEORETICAL, ADDUCT, and DATABASE_SOURCE are required when CONFIDENCE_LEVEL is 1, 2, or 3 | Theoretical mass-to-charge ratio of the assigned molecule. Required if CONFIDENCE_LEVEL is 1, 2, or 3; absent if CONFIDENCE_LEVEL is 4. |
| `MASS_ERROR_PPM` | float | Conditional: MASS_ERROR_PPM is required when MZ_THEORETICAL is present | Mass error in ppm between observed and theoretical m/z. Required if MZ_THEORETICAL is present (typical range -50 to +50). |
| `MOLECULAR_FORMULA` | string | Conditional: MOLECULAR_FORMULA is required when CONFIDENCE_LEVEL is 1 or 2 | Molecular formula in Hill notation (e.g., C47H81O13P). Required if CONFIDENCE_LEVEL is 1 or 2. |
| `MOLECULAR_NAME` | string | Yes | Free-text molecular name or "unknown"; must match the channel name in the OME-TIFF. |
| `ADDUCT` | [AdductEnum](#adductenum) | Conditional: MZ_THEORETICAL, ADDUCT, and DATABASE_SOURCE are required when CONFIDENCE_LEVEL is 1, 2, or 3 | Ion adduct form for this assignment. Required if CONFIDENCE_LEVEL is 1, 2, or 3. |
| `DATABASE_SOURCE` | [DatabaseSourceEnum](#databasesourceenum) | Conditional: MZ_THEORETICAL, ADDUCT, and DATABASE_SOURCE are required when CONFIDENCE_LEVEL is 1, 2, or 3 | Reference database used for the molecular assignment. Required if CONFIDENCE_LEVEL is 1, 2, or 3. |
| `DATABASE_ID` | string | Conditional: DATABASE_ID and DATABASE_VERSION are required when DATABASE_SOURCE is a real database (not NOT_APPLICABLE) | Identifier of the assigned molecule in the named database. Required if DATABASE_SOURCE is not NOT_APPLICABLE. |
| `DATABASE_VERSION` | string | Conditional: DATABASE_ID and DATABASE_VERSION are required when DATABASE_SOURCE is a real database (not NOT_APPLICABLE) | Version/release of the named database (YYYY-MM preferred). Required if DATABASE_SOURCE is not NOT_APPLICABLE. |
| `SOFTWARE_AND_VERSION` | string | Yes | Name and version of the annotation software (e.g., Metabascape 5.0, Metaspace 2024, Cardinal 3.4). |
| `CONFIDENCE_LEVEL` | integer | Yes | MSI molecular-identification confidence tier. 1 = identified; 2 = putatively annotated; 3 = compound class; 4 = unknown. |
| `EVIDENCE_TYPE` | [EvidenceTypeEnum](#evidencetypeenum) | Yes | One or more evidence types supporting the annotation (pipe-separated in the TSV). At least one value required. |

## Enums

### AdductEnum

| Value | Description |
|-------|-------------|
| M_MINUS_H | [M-H]- deprotonated molecule, most common negative mode adduct |
| M_PLUS_CL | [M+Cl]- chloride adduct |
| M_PLUS_H | [M+H]+ protonated molecule, most common positive mode adduct |
| M_PLUS_K | [M+K]+ potassium adduct |
| M_PLUS_NA | [M+Na]+ sodium adduct, common for lipids and carbohydrates |
| M_PLUS_NH4 | [M+NH4]+ ammonium adduct |
| M_RADICAL_MINUS | [M]- radical anion |
| M_RADICAL_PLUS | [M]+ radical cation (SIMS, some MALDI applications) |
| NOT_APPLICABLE | No adduct applicable (confidence level 4 unknowns) |
| OTHER | Adduct not listed; specify in MOLECULAR_NAME or annotation protocol |

### AnalyteClassEnum

| Value | Description |
|-------|-------------|
| GLYCANS | N-linked or O-linked glycans (e.g., PNGaseF-released) |
| LIPIDS | Lipids and fatty acids |
| METABOLITES | Small-molecule metabolites (non-lipid) |
| NUCLEIC_ACIDS | Oligonucleotides or nucleic acid species |
| PEPTIDES | Tryptic or enzymatically generated peptides |
| PHARMACEUTICALS | Drug compounds or their metabolites |
| PROTEINS | Intact or top-down proteins |

### BaselineCorrectionMethodEnum

| Value | Description |
|-------|-------------|
| NONE | No baseline correction applied |
| OTHER | Algorithm not listed; specify in SOFTWARE_AND_VERSION or PROTOCOL_LINK |
| SNIP | Statistics-sensitive Non-linear Iterative Peak-clipping algorithm |
| TOP_HAT | Top-hat morphological filter for baseline estimation |

### CalibrationTypeEnum

| Value | Description |
|-------|-------------|
| EXTERNAL | Calibration performed on a separate reference spot prior to acquisition |
| INTERNAL | Calibrant ions co-present in each spectrum during acquisition |
| LOCK_MASS | Real-time calibration correction using a reference ion of known m/z |

### DatabaseSourceEnum

| Value | Description |
|-------|-------------|
| CHEBI | Chemical Entities of Biological Interest (https://ebi.ac.uk/chebi) |
| CUSTOM | In-house or custom reference database; describe in PROTOCOL_LINK |
| GLYCONNECT | GlyConnect glycan database (https://glyconnect.expasy.org) |
| GLYTOUCAN | GlyTouCan glycan repository (https://glytoucan.org) |
| HMDB | Human Metabolome Database (https://hmdb.ca) |
| LIPID_MAPS | LIPID MAPS Structure Database (https://lipidmaps.org) |
| MASSBANK | MassBank spectral database (https://massbank.eu) |
| METLIN | METLIN metabolite and chemical database (https://metlin.scripps.edu) |
| NOT_APPLICABLE | No database assignment applicable (confidence level 4 unknowns) |
| PUBCHEM | PubChem compound database (https://pubchem.ncbi.nlm.nih.gov) |
| UNIPROT | Universal Protein Resource for protein identifications (https://uniprot.org) |

### EvidenceTypeEnum

| Value | Description |
|-------|-------------|
| ACCURATE_MASS | Annotation supported by accurate mass match within tolerance |
| DATABASE_SPECTRAL_MATCH | Match to a spectral library entry in a public spectral database (e.g., MassBank, mzCloud, Metaspace) - as distinct from MSMS_MATCH (an in-house/experimentally acquired reference spectrum) |
| ISOTOPE_PATTERN | Annotation supported by isotope pattern matching |
| MSMS_MATCH | Annotation supported by MS/MS fragmentation matched to an in-house or experimentally acquired reference spectrum (use DATABASE_SPECTRAL_MATCH for matches to a public spectral library) |
| REFERENCE_STANDARD | Confirmed by comparison to an authenticated in-house reference standard |
| SPATIAL_PATTERN_ONLY | Retained for biological relevance based on spatial distribution; no structural assignment |

### MassAnalysisPolarityEnum

| Value | Description |
|-------|-------------|
| BOTH | Dataset contains both positive and negative mode acquisitions (HTAN extension - not present in HuBMAP) |
| NEG | Negative ionisation mode |
| POS | Positive ionisation mode |

### MassAnalyzerTypeEnum

| Value | Description |
|-------|-------------|
| FTICR | Fourier-Transform Ion Cyclotron Resonance |
| ION_TRAP | Ion trap (linear or 3D) |
| ORBITRAP | Orbitrap electrostatic trap (Thermo) |
| OTHER | Analyser type not listed |
| Q_TOF | Quadrupole Time-of-Flight hybrid |
| TOF | Time-of-Flight mass analyser |
| TRIPLE_QUADRUPOLE | Triple-quadrupole (tandem MS) |

### MatrixDepositionMethodEnum

| Value | Description |
|-------|-------------|
| ELECTROSPRAY | Electrospray-based matrix deposition |
| NOT_APPLICABLE | Ionization modality does not use a matrix |
| PNEUMATIC_SPRAYER | Automated pneumatic spray coater (e.g., HTX TM-Sprayer) |
| ROBOTIC_SPOTTER | Robotic micro-dispensing of discrete matrix spots |
| SPRAY | Pneumatic or manual aerosol spray application |
| SUBLIMATION | Thermal sublimation deposition for uniform crystal layer |

### MsIonizationTechniqueEnum

| Value | Description |
|-------|-------------|
| DESI | Desorption Electrospray Ionization - ambient spray ionization |
| IR_MALDESI | Infrared MALDESI - IR laser ablation coupled with electrospray |
| MALDI | Matrix-Assisted Laser Desorption/Ionization |
| MALDI_2 | MALDI with secondary post-ionization laser for enhanced sensitivity (Bruker timsTOF Flex MALDI-2 mode) |
| OTHER | Ionization technique not listed; describe in PROTOCOL_LINK |
| SIMS | Secondary Ion Mass Spectrometry - ion beam sputtering for sub-micron resolution |

### MsScanModeEnum

| Value | Description |
|-------|-------------|
| LINEAR | Linear TOF mode; higher sensitivity for large molecules |
| NOT_APPLICABLE | Analyser does not use a TOF scan mode (e.g., Orbitrap, FTICR, Q-TOF hybrid) |
| OTHER | Scan mode not listed |
| REFLECTRON | Reflectron TOF mode; improved mass resolution via ion reflection |

### NormalizationMethodEnum

| Value | Description |
|-------|-------------|
| MEDIAN | Median spectrum intensity normalization |
| NONE | No normalization applied |
| OTHER | Method not listed; specify in PROTOCOL_LINK |
| REFERENCE_PEAK | Normalization to a single reference m/z peak of known abundance |
| RMS | Root Mean Square normalization |
| TIC | Total Ion Current normalization - divide each spectrum by its TIC |

### PreAcquisitionTreatmentEnum

| Value | Description |
|-------|-------------|
| NONE | No enzymatic or chemical treatment applied before this acquisition run |
| OTHER | Treatment not listed; describe in PROTOCOL_LINK |
| PNGASEF | PNGase F enzyme applied to release N-linked glycans from glycoproteins |
| PNGASEF_THEN_TRYPSIN | Sequential PNGase F followed by trypsin digestion |
| TRYPSIN | Trypsin applied for in-tissue proteolytic digestion to generate peptides |

### PreparationMatrixEnum

| Value | Description |
|-------|-------------|
| 9_AA | 9-Aminoacridine; used for lipids and metabolites in negative mode |
| CHCA | alpha-Cyano-4-hydroxycinnamic acid; used for peptides and small proteins |
| DAN | 1,5-Diaminonaphthalene; used for lipids and metabolites in negative mode |
| DHA | 2,6-Dihydroxyacetophenone; used for oligonucleotides and acidic lipids |
| DHB | 2,5-Dihydroxybenzoic acid; used for lipids, oligosaccharides, and metabolites |
| NOT_APPLICABLE | Ionization modality does not use a matrix (DESI, SIMS) |
| OTHER | Matrix compound not listed; specify in PROTOCOL_LINK. Use for IR-MALDESI (ice/endogenous-water matrix) |
| SA | Sinapinic acid; used for intact proteins >10 kDa |

### SegmentationReferenceModalityEnum

| Value | Description |
|-------|-------------|
| H_AND_E | Segmentation derived from H&E staining and projected onto MSI pixels |
| IF | Segmentation derived from immunofluorescence |
| MSI_NATIVE | Segmentation derived directly from MSI spectral clustering (no external reference) |
| OTHER | Reference modality not listed |

### SmoothingMethodEnum

| Value | Description |
|-------|-------------|
| GAUSSIAN | Gaussian kernel smoothing |
| NONE | No spectral smoothing applied |
| OTHER | Method not listed; specify in PROTOCOL_LINK |
| SAVITZKY_GOLAY | Savitzky-Golay polynomial smoothing filter |

### SpectrumTypeEnum

| Value | Description |
|-------|-------------|
| PROFILE | Continuous spectrum; full peak shapes preserved. Level 1 is always profile/continuous imzML (Level 2 is centroided, but does not re-record SPECTRUM_TYPE). |

### TimeUnitEnum

| Value | Description |
|-------|-------------|
| DAYS | Time expressed in days |
| HOURS | Time expressed in hours |
