# MultiplexMicroscopy

HTAN Multiplex Microscopy Data Model Schema for Phase 2 - All Levels

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseImagingAttributes

**Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | [ExperimentalStrategyAndDataSubtypes](#experimentalstrategyanddatasubtypes) | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `DE_IDENTIFICATION_METHOD_TYPE` | [DeIdentificationMethodType](#deidentificationmethodtype) | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | Conditional: Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' | Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | [License](#license) | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `IMAGE_MODALITY` | [ImageModality](#imagemodality) | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `STAINING_METHOD` | [StainingMethod](#stainingmethod) | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `IMMERSION` | [ImmersionMedium](#immersionmedium) | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | [Species](#species) | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | Conditional: Required when HAS_SLIDE_LABEL is true | Required when HAS_SLIDE_LABEL is true |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MultiplexMicroscopyLevel2

**Multiplex Microscopy Level 2 - Imaging data compiled into a single file format (preferably tiled and pyramidal OME-TIFF), accompanied by a CSV file containing channel metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the imaging file. Must be compatible with Bio-Formats or OpenSlide Python. OME-TIFF files use extensions .ome.tif, .ome.tiff, .ome.tf2, .ome.tf8, or .ome.btf |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.ome.tif, .ome.tiff, .ome.tf2, .ome.tf8, .ome.btf for ome-tiff; .tiff or .tif for tiff; .qptiff for qptiff; .svs for svs) |
| `WORKING_DISTANCE` | string | No | The working distance of the lens, expressed as a floating point number. Floating point > 0. Size needs to be specified in microns (um) |
| `IMAGING_ASSAY_TYPE` | [ImagingAssayType](#imagingassaytype) | Yes | Type of imaging assay |
| `PYRAMID` | boolean | No | The data file contains an image pyramid |
| `PHYSICAL_SIZE_X` | float | Yes | Physical size of a single pixel in the x dimension. In microns. |
| `PHYSICAL_SIZE_Y` | float | Yes | Physical size of a single pixel in the y dimension. In microns. |
| `PHYSICAL_SIZE_Z` | float | Yes | Physical size of a single pixel in the z dimension. In microns. |
| `SIZE_C` | integer | Yes | Number of channels. Integer >= 1 |
| `SIZE_T` | integer | Yes | Number of timepoints. Integer >= 1 |
| `SIZE_X` | integer | Yes | The number of pixels in the x dimension at the highest resolution available |
| `SIZE_Y` | integer | Yes | The number of pixels in the y dimension at the highest resolution available |
| `SIZE_Z` | integer | Yes | The number of pixels in the z dimension at the highest resolution available |
| `CHANNEL_METADATA_ID` | string | Yes | Unique identifier specifying the location of the required channel metadata (Synapse ID) |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | [ExperimentalStrategyAndDataSubtypes](#experimentalstrategyanddatasubtypes) | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `DE_IDENTIFICATION_METHOD_TYPE` | [DeIdentificationMethodType](#deidentificationmethodtype) | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | [License](#license) | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `IMAGE_MODALITY` | [ImageModality](#imagemodality) | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `STAINING_METHOD` | [StainingMethod](#stainingmethod) | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `IMMERSION` | [ImmersionMedium](#immersionmedium) | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | [Species](#species) | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Required when HAS_SLIDE_LABEL is true |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MultiplexMicroscopyLevel3

**Multiplex Microscopy Level 3 - Segmentation mask. Structured mask data following existing HTAN segmentation templates (RFC Imaging Level 3 & 4 - v1)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `SEGMENTATION_WORKFLOW_TYPE` | string | Yes | Type of segmentation workflow used to generate the mask |
| `SEGMENTATION_WORKFLOW_URL` | string | No | URL or link to the segmentation workflow used |
| `SEGMENTATION_WORKFLOW_VERSION` | string | No | Version of the segmentation workflow |
| `SEGMENTATION_METHOD` | string | Yes | Method used for segmentation (e.g., CellPose, StarDist, Ilastik, manual annotation) |
| `SEGMENTATION_PARAMETERS` | string | No | Parameters used for segmentation (e.g., model name, threshold values, preprocessing steps) |
| `SEGMENTATION_ANNOTATION_TYPE` | string | No | Type of objects segmented (e.g., Cell, Nucleus, Tissue, ROI) |
| `FILE_FORMAT` | string | Yes | Format of the segmentation mask file (should be ome-tiff for Level 3). OME-TIFF files use extensions .ome.tif, .ome.tiff, .ome.tf2, .ome.tf8, or .ome.btf |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.ome.tif, .ome.tiff, .ome.tf2, .ome.tf8, .ome.btf for ome-tiff; .tiff or .tif for tiff/tif) |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | [ExperimentalStrategyAndDataSubtypes](#experimentalstrategyanddatasubtypes) | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `DE_IDENTIFICATION_METHOD_TYPE` | [DeIdentificationMethodType](#deidentificationmethodtype) | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | [License](#license) | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `IMAGE_MODALITY` | [ImageModality](#imagemodality) | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `STAINING_METHOD` | [StainingMethod](#stainingmethod) | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `IMMERSION` | [ImmersionMedium](#immersionmedium) | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | [Species](#species) | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Required when HAS_SLIDE_LABEL is true |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## MultiplexMicroscopyLevel4

**Multiplex Microscopy Level 4 - Cell-by-feature table (typically cell-by-marker) generated from the segmentation mask and image. No changes from prior definitions (RFC Imaging Level 3 & 4 - v1)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FEATURE_EXTRACTION_WORKFLOW_TYPE` | string | Yes | Type of workflow used to extract features from segmented objects |
| `FEATURE_EXTRACTION_WORKFLOW_URL` | string | No | URL or link to the feature extraction workflow used |
| `FEATURE_EXTRACTION_WORKFLOW_VERSION` | string | No | Version of the feature extraction workflow |
| `MATRIX_TYPE` | [MatrixTypeEnum](#matrixtypeenum) | Yes | Type of feature matrix (raw counts, normalized, etc.) |
| `FEATURE_EXTRACTION_METHOD` | string | Yes | Method used for feature extraction (e.g., mean intensity, median intensity, total intensity, texture features) |
| `FEATURE_EXTRACTION_PARAMETERS` | string | No | Parameters used for feature extraction (e.g., channel names, measurement types, normalization methods) |
| `NUMBER_OF_FEATURES` | integer | No | Number of features (markers/channels) in the feature matrix |
| `NUMBER_OF_OBJECTS` | integer | No | Number of segmented objects (cells, nuclei, etc.) in the feature matrix |
| `FILE_FORMAT` | string | Yes | Format of the feature table file (csv or h5ad for Level 4) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.csv for csv; .h5ad for h5ad) |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | [ExperimentalStrategyAndDataSubtypes](#experimentalstrategyanddatasubtypes) | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging data types is "Pathological". |
| `DE_IDENTIFICATION_METHOD_TYPE` | [DeIdentificationMethodType](#deidentificationmethodtype) | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | string | No | Required when DE_IDENTIFICATION_METHOD_TYPE is not 'Not Applicable' |
| `DE_IDENTIFICATION_SOFTWARE` | string | No | Software that was used to de-identify the images (if used) |
| `LICENSE` | [License](#license) | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `IMAGE_MODALITY` | [ImageModality](#imagemodality) | Yes | The method in which the images are generated. |
| `IMAGING_EQUIPMENT_MANUFACTURER` | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_SOFTWARE` | string | No | The name of the software package that was used to capture, generate, and process the image |
| `CITATION_OR_DOI` | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must be a valid URL (http or https). |
| `IMAGING_PROTOCOL` | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assay protocol. Must be a valid URL (http or https). |
| `STAINING_METHOD` | [StainingMethod](#stainingmethod) | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examination |
| `OBJECTIVE` | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to produce a real image of the object |
| `NOMINAL_MAGNIFICATION` | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `IMMERSION` | [ImmersionMedium](#immersionmedium) | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media are air, oil, and water. |
| `LENS_NUMERICAL_APERTURE` | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `PASSED_QC` | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `QC_COMMENT` | string | Yes | Comments related to quality control checks |
| `SPECIES` | [Species](#species) | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `HAS_SLIDE_LABEL` | boolean | Yes | Does the image contain a slide label |
| `SLIDE_LABEL_REDACTED` | boolean | No | Required when HAS_SLIDE_LABEL is true |
| `DE_IDENTIFIED` | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metadata does not represent PHI |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## ChannelMetadata

**Metadata for each channel in multiplex microscopy imaging**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHANNEL_ID` | string | Yes | The unique channel identifier for each channel in this image must match the corresponding field in the imaging file submitted |
| `CHANNEL_NAME` | string | Yes | Channel label for each channel in this image must match the corresponding field in the imaging file submitted |
| `CYCLE_NUMBER` | integer | No | The cycle |
| `SUB_CYCLE_NUMBER` | integer | No | Sub-cycle |
| `TARGET_NAME` | string | No | Short descriptive name (abbreviation) for this target (antigen) |
| `ANTIBODY_NAME` | string | No | Short descriptive name for this antibody |
| `RRID_IDENTIFIER` | string | No | Research Resource Identifier |
| `FLUOROPHORE` | string | No | Fluorescent dye label |
| `CLONE` | string | No | Unique clone identifier |
| `LOT` | string | No | Lot number from vendor |
| `CATALOG_NUMBER` | string | No | Catalog number from vendor |
| `EXCITATION_WAVELENGTH` | float | No | Center/peak of the excitation spectrum (nm) |
| `EMISSION_WAVELENGTH` | float | No | Center/peak of the emission spectrum (nm) |
| `EXCITATION_BANDWIDTH` | float | No | Nominal width of excitation spectrum (nm) |
| `EMISSION_BANDWIDTH` | float | No | Nominal width of emission spectrum (nm) |
| `METAL_ISOTOPE_ELEMENT_ABBREVIATION` | [MetalIsotopeElement](#metalisotopeelement) | No | Element abbreviation |
| `METAL_ISOTOPE_ELEMENT_MASS` | integer | No | Element mass number |
| `OLIGO_BARCODE_UPPER_STRAND` | string | No | DNA barcode used for labeling |
| `OLIGO_BARCODE_LOWER_STRAND` | string | No | DNA barcode used for labeling |
| `DILUTION` | string | No | Final dilution ratio used in experiment |
| `CONCENTRATION` | string | No | Final concentration used in experiment |

## MultiplexMicroscopyData

**Container for all Multiplex Microscopy data levels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `LEVEL_2_DATA` | MultiplexMicroscopyLevel2 | No | Level 2 Multiplex Microscopy data (imaging data with channel metadata) |
| `LEVEL_3_DATA` | MultiplexMicroscopyLevel3 | No | Level 3 Multiplex Microscopy data (segmentation masks) |
| `LEVEL_4_DATA` | MultiplexMicroscopyLevel4 | No | Level 4 Multiplex Microscopy data (cell-by-feature tables) |
| `CHANNEL_METADATA` | ChannelMetadata | No | Channel metadata records for multiplex microscopy imaging |

## Enums

### DeIdentificationMethodType

| Value | Description |
|-------|-------------|
| Automatic | Automatic de-identification method |
| Manual | Manual de-identification method |
| Not Applicable | De-identification not applicable |
| Semiautomatic | Semi-automatic de-identification method |

### ExperimentalStrategyAndDataSubtypes

| Value | Description |
|-------|-------------|
| Pathological | Pathological experimental strategy and data subtype |

### ImageModality

| Value | Description |
|-------|-------------|
| SM | Slide Microscopy |

### ImagingAssayType

| Value | Description |
|-------|-------------|
| CODEX | CODEX imaging assay type |
| CyCIF | Cyclic Immunofluorescence imaging assay type |
| ExSeq | Expansion Sequencing imaging assay type |
| GeoMX-DSP | GeoMX Digital Spatial Profiling imaging assay type |
| H&E | Hematoxylin and Eosin imaging assay type |
| IHC | Immunohistochemistry imaging assay type |
| IMC | Imaging Mass Cytometry imaging assay type |
| MIBI | Multiplexed Ion Beam Imaging imaging assay type |
| MERFISH | Multiplexed Error-Robust Fluorescence In Situ Hybridization imaging assay type |
| MxIF | Multiplexed Immunofluorescence imaging assay type |
| mIHC | Multiplexed Immunohistochemistry imaging assay type |
| Not Applicable | Imaging assay not applicable |
| SABER | Signal Amplification By Exchange Reaction imaging assay type |
| t-CyCIF | Tissue Cyclic Immunofluorescence imaging assay type |

### ImmersionMedium

| Value | Description |
|-------|-------------|
| Air | Air immersion medium |
| Glycerol | Glycerol immersion medium |
| Oil | Oil immersion medium |
| Other | Other immersion medium |
| Water | Water immersion medium |

### License

| Value | Description |
|-------|-------------|
| CC BY 4.0 | Creative Commons Attribution 4.0 International License |

### MatrixTypeEnum

| Value | Description |
|-------|-------------|
| Raw Counts | Raw count matrix |
| Normalized Counts | Normalized count matrix |
| Scaled Counts | Scaled count matrix |
| Log Normalized | Log normalized counts |
| Z-Score Normalized | Z-score normalized values |
| Other | Other normalization method |

### MetalIsotopeElement

| Value | Description |
|-------|-------------|
| H | Hydrogen |
| He | Helium |
| Li | Lithium |
| Be | Beryllium |
| B | Boron |
| C | Carbon |
| N | Nitrogen |
| O | Oxygen |
| F | Fluorine |
| Ne | Neon |
| Na | Sodium |
| Mg | Magnesium |
| Al | Aluminum |
| Si | Silicon |
| P | Phosphorus |
| S | Sulfur |
| Cl | Chlorine |
| Ar | Argon |
| K | Potassium |
| Ca | Calcium |
| Sc | Scandium |
| Ti | Titanium |
| V | Vanadium |
| Cr | Chromium |
| Mn | Manganese |
| Fe | Iron |
| Co | Cobalt |
| Ni | Nickel |
| Cu | Copper |
| Zn | Zinc |
| Ga | Gallium |
| Ge | Germanium |
| As | Arsenic |
| Se | Selenium |
| Br | Bromine |
| Kr | Krypton |
| Rb | Rubidium |
| Sr | Strontium |
| Y | Yttrium |
| Zr | Zirconium |
| Nb | Niobium |
| Mo | Molybdenum |
| Tc | Technetium |
| Ru | Ruthenium |
| Rh | Rhodium |
| Pd | Palladium |
| Ag | Silver |
| Cd | Cadmium |
| In | Indium |
| Sn | Tin |
| Sb | Antimony |
| Te | Tellurium |
| I | Iodine |
| Xe | Xenon |
| Cs | Cesium |
| Ba | Barium |
| La | Lanthanum |
| Ce | Cerium |
| Pr | Praseodymium |
| Nd | Neodymium |
| Pm | Promethium |
| Sm | Samarium |
| Eu | Europium |
| Gd | Gadolinium |
| Tb | Terbium |
| Dy | Dysprosium |
| Ho | Holmium |
| Er | Erbium |
| Tm | Thulium |
| Yb | Ytterbium |
| Lu | Lutetium |
| Hf | Hafnium |
| Ta | Tantalum |
| W | Tungsten |
| Re | Rhenium |
| Os | Osmium |
| Ir | Iridium |
| Pt | Platinum |
| Au | Gold |
| Hg | Mercury |
| Tl | Thallium |
| Pb | Lead |
| Bi | Bismuth |
| Po | Polonium |
| At | Astatine |
| Rn | Radon |
| Fr | Francium |
| Ra | Radium |
| Ac | Actinium |
| Th | Thorium |
| Pa | Protactinium |
| U | Uranium |
| Np | Neptunium |
| Pu | Plutonium |
| Am | Americium |
| Cm | Curium |
| Bk | Berkelium |
| Cf | Californium |
| Es | Einsteinium |
| Fm | Fermium |
| Md | Mendelevium |
| No | Nobelium |
| Lr | Lawrencium |
| Rf | Rutherfordium |
| Db | Dubnium |
| Sg | Seaborgium |
| Bh | Bohrium |
| Hs | Hassium |
| Mt | Meitnerium |
| Ds | Darmstadtium |
| Rg | Roentgenium |
| Cn | Copernicium |
| Fl | Flerovium |
| Lv | Livermorium |
| Ts | Tennessine |
| Og | Oganesson |

### Species

| Value | Description |
|-------|-------------|
| 9606 (Homo sapiens) | NCBI Taxonomy ID for Homo sapiens |

### StainingMethod

| Value | Description |
|-------|-------------|
| CODEX | CODEX staining method |
| CyCIF | Cyclic Immunofluorescence staining method |
| ExSeq | Expansion Sequencing staining method |
| GeoMX-DSP | GeoMX Digital Spatial Profiling staining method |
| H&E | Hematoxylin and Eosin staining method |
| IHC | Immunohistochemistry staining method |
| IMC | Imaging Mass Cytometry staining method |
| MERFISH | Multiplexed Error-Robust Fluorescence In Situ Hybridization staining method |
| MIBI | Multiplexed Ion Beam Imaging staining method |
| MxIF | Multiplexed Immunofluorescence staining method |
| Not Applicable | Staining not applicable |
| SABER | Signal Amplification By Exchange Reaction staining method |
| mIHC | Multiplexed Immunohistochemistry staining method |
| t-CyCIF | Tissue Cyclic Immunofluorescence staining method |
