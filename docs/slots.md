# Slot Index

Every metadata field defined across all HTAN modules, sorted alphabetically. Fields shared between modules are listed once with all modules noted.

| Slot | Module(s) | Type | Required | Description |
|------|-----------|------|----------|-------------|
| `AA_CHANGE` | Clinical | string | No | Alphanumeric value used to describe the amino acid change for a specific genetic variant, e.g., R116Q, as determined by clinical testing. (caDSR:61... |
| `ACQUISITION_METHOD_OTHER_SPECIFY` | Biospecimen | string | No | A custom acquisition method |
| `ACQUISITION_METHOD_TYPE` | Biospecimen | AcquisitionMethodTypeEnum | Yes | Records the method of acquisition or source for the specimen under consideration |
| `ADAPTER_CONTENT` | WES | string | No | Adapter content information |
| `ADAPTER_NAME` | WES | string | No | Name of the adapter used |
| `ADAPTER_SEQUENCE` | WES | string | No | Adapter sequence |
| `ADJACENT_BIOSPECIMEN_IDS` | Biospecimen | string | No | List of HTAN Biospecimen IDs of adjacent biospecimens cut from the same sample. Each ID must match the HTAN biospecimen ID pattern. |
| `AGE_IN_DAYS_AT_DEATH` | Clinical | integer | No | Age in days of the subject at which death occurred. Use -1 if this data point is not available. (caDSR:15748633) (Aligns to CDRC Standard CDE) |
| `AGE_IN_DAYS_AT_DIAGNOSIS` | Clinical | integer | Yes | Age at the time of diagnosis expressed in number of days since birth. Use -1 if this data point is not available. (caDSR:15019300) (No CRDC Standar... |
| `AGE_IN_DAYS_AT_FOLLOWUP` | Clinical | integer | Yes | Age in days of the subject at the the time of follow-up. Use -1 if this data point is not available. (caDSR:15748634) (No CRDC Standard Available) |
| `AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS` | Clinical | integer | Yes | Age in days of subject at the time of their last known disease status. Use -1 if this data point is not available. (caDSR:14589579) (No CRDC Standa... |
| `AGE_IN_DAYS_AT_LAST_KNOWN_SURVIVAL_STATUS` | Clinical | integer | Yes | Age in days when the last known survival status of the subject was captured. Use -1 if this data point is not available. (caDSR:12305768) (Aligns t... |
| `AGE_IN_DAYS_AT_MOLECULAR_TEST_START` | Clinical | integer | Yes | Age in days of the subject at the start of a molecular analysis. Use -1 if this data point is not available. (caDSR:15879017) (No CRDC Standard Ava... |
| `AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP` | Clinical | integer | No | Age in days of the subject at the end of a molecular analysis. (caDSR:15879662) (No CRDC Standard Available) |
| `AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE` | Clinical | integer | No | Age of an individual, in days, when a diagnosis of disease progression or recurrence was made. Use -1 if this data point is not available. (caDSR:1... |
| `AGE_IN_DAYS_AT_SECTIONING` | Biospecimen | integer | No | The age in days of a subject when a specimen tissue block was sectioned |
| `AGE_IN_DAYS_AT_SPECIMEN_COLLECTION` | Biospecimen | integer | Yes | The age in days of the subject at the time of specimen collection |
| `AGE_IN_DAYS_AT_SPECIMEN_PROCESSING` | Biospecimen | integer | Yes | The age in days of a subject when a specimen was processed |
| `AGE_IN_DAYS_AT_TREATMENT_END` | Clinical | integer | No | The age in days of the subject at the time that this treatment was completed. Use -1 if this data point is not available. (caDSR:12304723) (Aligns ... |
| `AGE_IN_DAYS_AT_TREATMENT_START` | Clinical | integer | Yes | The age in days of the subject at the time that this treatment was started. Use -1 if this data point is not available. (caDSR:12304720) (Aligns to... |
| `AJCC_STAGING_SYSTEM_EDITION` | Clinical | AJCCStagingSystemEditionEnum | No | Version or edition of the American Joint Committee on Cancer Cancer Staging Handbooks used to guide TMN clinical staging in CLINICAL_T_STAGE, CLINI... |
| `ALCOHOL_HISTORY_INDICATOR` | Clinical | AlcoholHistoryIndicatorEnum | Yes | Response indicating whether or not an individual has ever consumed alcohol. (caDSR:7537144) (No CRDC Standard Available) |
| `ALIGNMENT_WORKFLOW_TYPE` | WES | string | Yes | Type of alignment workflow used |
| `ANALYTE_TYPE` | Biospecimen | AnalyteTypeEnum | No | The sample or material being subjected to analysis |
| `ANNDATA_SCHEMA_VERSION` | scRNA-seq | string | Yes | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | scRNA-seq | boolean | Yes | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `ANNOTATION_TYPE` | DigitalPathology | AnnotationType | No | What types of annotation are contained in the image |
| `ANTIBODY_NAME` | MultiplexMicroscopy | string | No | Short descriptive name for this antibody |
| `ASSAY_CHEMISTRY_VERSION` | SpatialOmics | string | Yes | Assay chemistry version (e.g., v1, v2) |
| `ASSAY_TYPE` | SpatialOmics | AssayType | Yes | Broad assay class (drives downstream conditionals) |
| `AVERAGE_BASE_QUALITY` | WES | float | No | Average base quality |
| `AVERAGE_INSERT_SIZE` | WES | integer | No | Average insert size |
| `AVERAGE_READ_LENGTH` | WES | integer | No | Average read length |
| `BASE_CALLER_NAME` | WES | string | No | Name of the base caller |
| `BASE_CALLER_VERSION` | WES | string | No | Version of the base caller |
| `BASIC_STATISTICS` | WES | string | No | Basic statistics from QC |
| `BIOSPECIMEN_TYPE` | Biospecimen | BiospecimenTypeEnum | Yes | Biospecimen Type |
| `BUNDLE_CONTENTS` | SpatialOmics | string | Yes | List of expected files or folders in this bundle (relative paths within the archive) |
| `CAPTURE_AREA` | SpatialOmics | CaptureArea | No | Area (or Capture Area) - One of the either four or two active regions where tissue can be placed on a Visium slide |
| `CATALOG_NUMBER` | MultiplexMicroscopy | string | No | Catalog number from vendor |
| `CAUSE_OF_DEATH` | Clinical | CauseOfDeathEnum | No | Circumstance or condition of greatest importance that resulted in the death. (caDSR:4783274) (Aligns to CDRC Standard CDE) |
| `CAUSE_OF_DEATH_SOURCE` | Clinical | CauseOfDeathSourceEnum | No | Source of information used in describing the death of an individual. (caDSR:2390921) (Aligns to CDRC Standard CDE) |
| `CELL_BARCODE_TAG` | scRNA-seq | string | No | Tag used for cell barcodes |
| `CELL_MEDIAN_NUMBER_GENES` | scRNA-seq | integer | Yes | Median number of genes detected per cell |
| `CELL_MEDIAN_NUMBER_READS` | scRNA-seq | integer | Yes | Median number of reads per cell |
| `CELL_SEGMENTATION_METHOD` | SpatialOmics | string | No | Description of segmentation method |
| `CELL_SEGMENTED_OBJECT_TYPE` | SpatialOmics | CellSegmentedObjectType | No | Level of segmentation |
| `CELL_TOTAL` | scRNA-seq | integer | Yes | Number of sequenced cells. Applies to raw counts matrix only |
| `CELL_TYPES` | SpatialOmics | string | No | List of cell types present in the data |
| `CELL_TYPE_CALLING_METHOD` | SpatialOmics | string | No | Method used for cell type annotation |
| `CHANNEL_ID` | MultiplexMicroscopy | string | Yes | The unique channel identifier for each channel in this image must match the corresponding field in the imaging file submitted |
| `CHANNEL_METADATA` | MultiplexMicroscopy | ChannelMetadata | No | Channel metadata records for multiplex microscopy imaging |
| `CHANNEL_METADATA_ID` | MultiplexMicroscopy | string | Yes | Unique identifier specifying the location of the required channel metadata (Synapse ID) |
| `CHANNEL_NAME` | MultiplexMicroscopy | string | Yes | Channel label for each channel in this image must match the corresponding field in the imaging file submitted |
| `CHECKSUM` | WES, scRNA-seq | string | No | Checksum for data integrity verification |
| `CITATION_OR_DOI` | DigitalPathology, Imaging, MultiplexMicroscopy | string | Yes | Raw Data Protocol or Digital Object Identifier Text; Publication and/or digital object identifier of the publication for open access studies. Must ... |
| `CLINICAL_BIOSPECIMEN_TYPE` | Clinical | ClinicalBiospecimenTypeEnum | Yes | Kind of material taken from a biological entity for testing, diagnostic, propagation, treatment or research purposes. (caDSR:7069877) (Aligns to CR... |
| `CLINICAL_M_STAGE` | Clinical | ClinicalMStageEnum | No | Extent of the distant metastasis for the cancer based on evidence obtained from clinical assessment parameters determined prior to treatment. (caDS... |
| `CLINICAL_N_STAGE` | Clinical | ClinicalNStageEnum | No | Extent of the regional lymph node involvement for the cancer based on evidence obtained from clinical assessment parameters determined prior to tre... |
| `CLINICAL_T_STAGE` | Clinical | ClinicalTStageEnum | No | Extent of spread of the primary cancer based on evidence obtained from clinical assessment parameters determined prior to treatment. (caDSR:3440328... |
| `CLONE` | MultiplexMicroscopy | string | No | Unique clone identifier |
| `CLUSTERING_METHOD` | SpatialOmics | string | No | Method used to define clusters |
| `CONCENTRATION` | MultiplexMicroscopy | string | No | Final concentration used in experiment |
| `CONTAMINATION` | WES | float | No | Contamination estimate |
| `CONTAMINATION_ERROR` | WES | float | No | Contamination error estimate |
| `COPY_NUMBER` | Clinical | integer | No | The quantity of gene copies resulting from a mutation. (caDSR:13367966) (Aligns to CDRC Standard CDE) |
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | scRNA-seq | boolean | No | Whether cells were cryopreserved in the sample |
| `CYCLE_NUMBER` | MultiplexMicroscopy | integer | No | The cycle |
| `CYTASSIST_USED` | SpatialOmics | boolean | No | Whether CytAssist was used |
| `DATA_CATEGORY` | scRNA-seq | DataCategoryEnum | Yes | Specific content type of the data file |
| `DEGREE_OF_DYSPLASIA` | Biospecimen | DegreeOfDysplasiaEnum | No | Information related to the presence of cells that look abnormal under a microscope but are not cancer |
| `DEMOGRAPHICS` | Clinical | Demographics | Yes | Demographic information |
| `DE_IDENTIFICATION_METHOD_DESCRIPTION` | DigitalPathology, Imaging, MultiplexMicroscopy | string | No | Description of the process of removing potentially identifying data or data elements to render data into a form that does not identify individuals ... |
| `DE_IDENTIFICATION_METHOD_TYPE` | DigitalPathology, Imaging, MultiplexMicroscopy | DeIdentificationMethodType | Yes | De-identification Method Type |
| `DE_IDENTIFICATION_SOFTWARE` | DigitalPathology, Imaging, MultiplexMicroscopy | string | No | Software that was used to de-identify the images (if used) |
| `DE_IDENTIFIED` | DigitalPathology, Imaging, MultiplexMicroscopy | boolean | Yes | Confirm that any HIPAA identifiers are redacted, masked, or not present in the slide label and that any dates or strings present in internal metada... |
| `DIAGNOSIS` | Clinical | Diagnosis | Yes | Primary diagnosis information |
| `DILUTION` | MultiplexMicroscopy | string | No | Final dilution ratio used in experiment |
| `DIMENSIONALITY_REDUCTION_METHOD` | SpatialOmics | DimensionalityReductionMethod | No | Method used for dimensionality reduction |
| `DISEASE_RESPONSE` | Clinical | DiseaseResponseEnum | Yes | Result of an evaluation to determine whether pathologic and/or clinical changes resulted from treatment. (caDSR:13383448) (Aligns to CDRC Standard ... |
| `DISSOCIATION_METHOD` | scRNA-seq | DissociationMethodEnum | Yes | Method used to dissociate tissue into single cells |
| `ECOG_PERFORMANCE_STATUS` | Clinical | ECOGPerformanceStatusEnum | No | ECOG functional performance status of the individual. (caDSR:88) (Aligns to CDRC Standard CDE) |
| `ECOG_SCORE_PERFORMED` | Clinical | EcogScorePerformedEnum | Yes | Indicator of whether an ECOG performance status score was obtained for the individual. (caDSR:5943795) (Aligns to CRDC Standard CDE) |
| `EMISSION_BANDWIDTH` | MultiplexMicroscopy | float | No | Nominal width of emission spectrum (nm) |
| `EMISSION_WAVELENGTH` | MultiplexMicroscopy | float | No | Center/peak of the emission spectrum (nm) |
| `ENCODING` | WES | string | No | Encoding information |
| `ENVIRONMENTAL_EXPOSURE` | Clinical | EnvironmentalExposureEnum | Yes | Response indicating whether or not an individual was exposed to potentially harmful environmental agents (caDSR:15753166) (Aligns to CRDC Node) |
| `ENVIRONMENTAL_EXPOSURE_TYPE` | Clinical | EnvironmentalExposureTypeEnum | No | Type of potentially harmful environmental agents to which an individual was exposed. (caDSR:15753203) (Aligns to CDRC Standard CDE) |
| `ETHNIC_GROUP` | Clinical | EthnicGroupEnum | Yes | Ethnic group of the participant (caDSR:2192217) (Aligns to CDRC Standard CDE) |
| `EVIDENCE_OF_RECURRENCE_TYPE` | Clinical | EvidenceOfRecurrenceTypeEnum | No | Type of evidence used to determine whether the individual's disease has recurred. (caDSR:7668166) (No CRDC Standard Available) |
| `EXCITATION_BANDWIDTH` | MultiplexMicroscopy | float | No | Nominal width of excitation spectrum (nm) |
| `EXCITATION_WAVELENGTH` | MultiplexMicroscopy | float | No | Center/peak of the excitation spectrum (nm) |
| `EXON` | Clinical | integer | No | Exon number targeted or included in a clinical molecular analysis. (caDSR:6142411) (No CRDC Standard Available) |
| `EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES` | DigitalPathology, Imaging, MultiplexMicroscopy | ExperimentalStrategyAndDataSubtypes | Yes | What is the experimental strategy used for the study (or what type of data subtypes exist in the study)? Per RFC, the only valid value for imaging ... |
| `EXPOSURES` | Clinical | Exposure | Yes | Exposure history |
| `FAMILY_HISTORY` | Clinical | FamilyHistory | Yes | Family history of cancer |
| `FAMILY_MEMBER_CANCER_HISTORY` | Clinical | FamilyMemberCancerHistoryEnum | Yes | Response to indicate if any relative has a medical history that includes cancer. (caDSR:13309936) (No CRDC Standard Available) |
| `FEATURE_EXTRACTION_METHOD` | MultiplexMicroscopy | string | Yes | Method used for feature extraction (e.g., mean intensity, median intensity, total intensity, texture features) |
| `FEATURE_EXTRACTION_PARAMETERS` | MultiplexMicroscopy | string | No | Parameters used for feature extraction (e.g., channel names, measurement types, normalization methods) |
| `FEATURE_EXTRACTION_WORKFLOW_TYPE` | MultiplexMicroscopy | string | Yes | Type of workflow used to extract features from segmented objects |
| `FEATURE_EXTRACTION_WORKFLOW_URL` | MultiplexMicroscopy | string | No | URL or link to the feature extraction workflow used |
| `FEATURE_EXTRACTION_WORKFLOW_VERSION` | MultiplexMicroscopy | string | No | Version of the feature extraction workflow |
| `FILENAME` | DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES, scRNA-seq | string | Yes | Name of the file |
| `FILE_FORMAT` | DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES, scRNA-seq | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `FIXATION_DURATION_IN_MINUTES` | Biospecimen | integer | No | The length of time, from beginning to end, required to process or preserve biospecimens in fixative |
| `FLOW_CELL_BARCODE` | WES | string | No | Flow cell barcode |
| `FLUOROPHORE` | MultiplexMicroscopy | string | No | Fluorescent dye label |
| `FOLLOW_UPS` | Clinical | FollowUp | No | Follow-up observations |
| `FRAGMENT_MAXIMUM_LENGTH` | WES | integer | No | Maximum fragment length |
| `FRAGMENT_MEAN_LENGTH` | WES | integer | No | Mean fragment length |
| `FRAGMENT_MINIMUM_LENGTH` | WES | integer | No | Minimum fragment length |
| `FRAGMENT_STANDARD_DEVIATION_LENGTH` | WES | integer | No | Standard deviation of fragment length |
| `GENDER_IDENTITY` | Clinical | GenderIdentityEnum | Yes | Gender identity of the participant |
| `GENE_ID` | SpatialOmics | string | Yes | Stable Ensembl gene identifier (e.g., ENSG00000214114, ENSG00000121879). String matching ENSG\\d+ or digits |
| `GENE_SYMBOL` | Clinical, SpatialOmics | gene_symbol_enum | Yes | Gene symbol of the gene targeted or included in molecular analysis. (caDSR:11280318) (No CRDC Standard Available) |
| `GENOME_ANNOTATION_URL` | WES, scRNA-seq | string | Yes | URL to genome or transcriptome annotation |
| `GENOMIC_REFERENCE` | SpatialOmics, WES, scRNA-seq | GenomicReferenceEnum | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data l... |
| `GENOMIC_REFERENCE_URL` | WES, scRNA-seq | string | Yes | URL to genomic or transcriptomic reference |
| `GERMLINE_VARIANTS_WORKFLOW_TYPE` | WES | string | No | Type of germline variants workflow |
| `GERMLINE_VARIANTS_WORKFLOW_URL` | WES | string | No | URL to the germline variants workflow |
| `GLEASON_GRADE_GROUP` | Clinical | GleasonGradeGroupEnum | No | The Gleason grade group for prostate cancer, derived from the primary and secondary Gleason pattern scores. (caDSR:5918370) |
| `HAS_ANNOTATIONS` | DigitalPathology | boolean | Yes | Does the image contain annotations |
| `HAS_CELL_SEGMENTATION` | SpatialOmics | boolean | Yes | Indicates presence of cell segmentation data |
| `HAS_CELL_TYPE_CALLING` | SpatialOmics | boolean | Yes | Indicates presence of cell type annotations |
| `HAS_CLUSTERING` | SpatialOmics | boolean | Yes | Indicates if clustering was performed |
| `HAS_DIMENSIONALITY_REDUCTION` | SpatialOmics | boolean | No | Indicates presence of dimensionally reduced data |
| `HAS_IMAGE` | SpatialOmics | boolean | Yes | Indicates presence of associated image data |
| `HAS_IMAGES` | SpatialOmics | boolean | Yes | Whether any image files (e.g., TIFFs) are included |
| `HAS_NORMALISED_ARRAY` | SpatialOmics | boolean | Yes | Indicates presence of normalized array |
| `HAS_PROBE_SET` | SpatialOmics | boolean | No | Whether a targeted probe/gene panel is included |
| `HAS_RAW_ARRAY` | SpatialOmics | boolean | Yes | Indicates presence of raw expression array |
| `HAS_REGISTRATION_FILES` | SpatialOmics | boolean | Yes | Whether any spatial registration transform files are included |
| `HAS_SEQUENCING` | SpatialOmics | boolean | No | If raw/aligned sequencing data is included |
| `HAS_SLIDE_LABEL` | DigitalPathology, Imaging, MultiplexMicroscopy | boolean | Yes | Does the image contain a slide label |
| `HGNC_VERSION` | SpatialOmics | string | Yes | Version of the HGNC used, indicated with the date of the HGNC reference (e.g., 2025-08-01) |
| `HTAN_BIOSPECIMEN_ID` | Biospecimen | string | Yes | HTAN Biospecimen ID (Primary Key) |
| `HTAN_DATA_FILE_ID` | DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES, scRNA-seq | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PANEL_ID` | SpatialOmics | string | Yes | Unique identifier for the panel |
| `HTAN_PARENT_ID` | Biospecimen, DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES, scRNA-seq | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (Participant ID or Biospecimen ID with B suffix). One or more IDs. Supports HTA200-229 for phas... |
| `HTAN_PARTICIPANT_ID` | Clinical | string | Yes | HTAN ID associated with a patient based on HTAN ID SOP (Primary Key) |
| `ICD_10_DISEASE_CODE` | Biospecimen | Icd10DiseaseEnum | No | For coding precancerous lesions: The diagnosis, in humans, as captured in the 2022 extension of ICD-10-CM |
| `ICD_O_3_TISSUE_MORPHOLOGY` | Biospecimen | IcdO3MorphologyEnum | No | The microscopic anatomy of normal and abnormal cells and tissues of the specimen as captured in the morphology codes of ICD-O-3 |
| `IMAGE_MODALITY` | DigitalPathology, Imaging, MultiplexMicroscopy | ImageModality | Yes | The method in which the images are generated. |
| `IMAGE_TYPE` | SpatialOmics | ImageTypeLevel4 | No | Type of image associated with the data file |
| `IMAGE_TYPES` | SpatialOmics | ImageType | No | Types of images provided |
| `IMAGING_ASSAY_TYPE` | MultiplexMicroscopy | ImagingAssayType | Yes | Type of imaging assay |
| `IMAGING_EQUIPMENT_MANUFACTURER` | DigitalPathology, Imaging, MultiplexMicroscopy | string | Yes | Producer of the imaging equipment that was used to generate the digital image |
| `IMAGING_EQUIPMENT_MODEL` | DigitalPathology, Imaging, MultiplexMicroscopy | string | No | The words used to describe the specific model of the instrument used to carry out an imaging experiment |
| `IMAGING_PROTOCOL` | DigitalPathology, Imaging, MultiplexMicroscopy | string | No | A rule which guides how an activity should be performed. Protocols.io ID or DOI link to a free/open protocol resource describing in detail the assa... |
| `IMAGING_SOFTWARE` | DigitalPathology, Imaging, MultiplexMicroscopy | string | No | The name of the software package that was used to capture, generate, and process the image |
| `IMMERSION` | DigitalPathology, Imaging, MultiplexMicroscopy | ImmersionMedium | No | Immersion medium. Each objective is designed for a specific immersion medium, which is marked on the objective. The main types of immersion media a... |
| `INDEX_FILE_NAME` | WES | string | No | Name of the index file |
| `INITIAL_DISEASE_STATUS` | Clinical | InitialDiseaseStatusEnum | Yes | Status of the individual's malignancy when the treatment began. (caDSR:15907348) (Aligns to CDRC Standard CDE) |
| `IS_LOWEST_LEVEL` | WES | boolean | No | Whether this is the lowest level |
| `IS_TISSUE_SECTION` | Biospecimen | TissueSectionEnum | No | Indicator that the type of preserved sample material removed for testing, diagnostic, propagation, treatment or research purposes is a tissue secti... |
| `LANE_NUMBER` | WES | integer | No | Lane number |
| `LAST_KNOWN_DISEASE_STATUS` | Clinical | LastKnownDiseaseStatusEnum | Yes | Most recently documented condition or state of an individual's disease. (caDSR:12447172) (Aligns to CDRC Standard CDE) |
| `LENS_NUMERICAL_APERTURE` | DigitalPathology, Imaging, MultiplexMicroscopy | float | No | The numerical aperture of the lens. Floating point value > 0. |
| `LEVEL_1_DATA` | SpatialOmics, WES | BulkWESLevel1 | No | Level 1 WES data (raw files) |
| `LEVEL_2_DATA` | MultiplexMicroscopy, WES | BulkWESLevel2 | No | Level 2 WES data (aligned files and QC) |
| `LEVEL_3_DATA` | MultiplexMicroscopy, SpatialOmics, WES | BulkWESLevel3 | No | Level 3 WES data (called variants) |
| `LEVEL_4_DATA` | MultiplexMicroscopy, SpatialOmics | SpatialLevel4 | No | Level 4 Spatial Omics data (interoperable h5ad or RDS file, optional) |
| `LIBRARY_CONSTRUCTION_METHOD` | scRNA-seq | LibraryConstructionMethodEnum | Yes | Method used to construct the sequencing library |
| `LIBRARY_LAYOUT` | WES, scRNA-seq | LibraryLayoutEnum | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | WES, scRNA-seq | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please e... |
| `LIBRARY_PREPARATION_KIT_NAME` | WES | string | No | Name of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VENDOR` | WES | string | No | Vendor of the library preparation kit |
| `LIBRARY_PREPARATION_KIT_VERSION` | WES | string | No | Version of the library preparation kit |
| `LIBRARY_SELECTION_METHOD` | WES | LibrarySelectionMethodEnum | Yes | Method used for library selection |
| `LICENSE` | DigitalPathology, Imaging, MultiplexMicroscopy | License | Yes | Official or legal permission to do or own a specified thing. Per RFC, the only valid value is "CC BY 4.0". |
| `LINKED_MATRICES` | scRNA-seq | string | No | All matrices associated with every part of a SingleCellExperiment object. Comma-delimited list of filenames |
| `LONGEST_DIMENSION` | Biospecimen | decimal | No | Numeric value that represents the longest dimension of the sample, measured in millimeters |
| `LOT` | MultiplexMicroscopy | string | No | Lot number from vendor |
| `MATRIX_TYPE` | MultiplexMicroscopy, scRNA-seq | MatrixTypeEnum | Yes | Type of data stored in matrix |
| `MEAN_COVERAGE` | WES | float | Yes | Mean coverage depth |
| `MENOPAUSE_STATUS` | Clinical | MenopauseStatusEnum | No | Menopausal status of the individual. (caDSR:2434914) (No CRDC Standard Available) |
| `METAL_ISOTOPE_ELEMENT_ABBREVIATION` | MultiplexMicroscopy | MetalIsotopeElement | No | Element abbreviation |
| `METAL_ISOTOPE_ELEMENT_MASS` | MultiplexMicroscopy | integer | No | Element mass number |
| `METASTASIS_AT_DIAGNOSIS` | Clinical | MetastasisAtDiagnosisEnum | Yes | State of metastatic disease at the time of primary tumor diagnosis. (caDSR:3438571) (Aligns to CDRC Standard CDE) |
| `METHOD_OF_DIAGNOSIS` | Clinical | MethodOfDiagnosisEnum | Yes | Type of clinical or laboratory procedure(s) used in the determination of a disease diagnosis. (caDSR:14857681) (Aligns to CRDC Node) |
| `METHOD_OF_NUCLEIC_ACID_ISOLATION` | Biospecimen | string | No | Bulk RNA & DNA-seq specific: method used for nucleic acid isolation |
| `MOLECULAR_ANALYSIS_METHOD` | Clinical | MolecularAnalysisMethodEnum | Yes | Description of the method used for clinical molecular analysis. (caDSR:6142401) (No CRDC Standard Available) |
| `MOLECULAR_ANALYSIS_RESULT` | Clinical | MolecularAnalysisResultEnum | Yes | Description of the result of clinical molecular analysis. (caDSR:6142397) (No CRDC Standard Available) |
| `MOLECULAR_CONSEQUENCE` | Clinical | MolecularConsequenceEnum | No | Description of the molecular consequence of genetic variation identified by a clinical test. (caDSR:13367935) (No CRDC Standard Available) |
| `MOLECULAR_TESTS` | Clinical | MolecularTest | No | Molecular test results |
| `MSI_SCORE` | WES | float | No | MSI score |
| `MSI_STATUS` | WES | MSIStatusEnum | No | MSI status |
| `MSI_WORKFLOW_LINK` | WES | string | No | Link to MSI workflow |
| `MULTIPLEX_BARCODE` | WES | string | No | Multiplex barcode |
| `NOMINAL_MAGNIFICATION` | DigitalPathology, Imaging, MultiplexMicroscopy | integer | Yes | The magnification of the lens as specified by the manufacturer - i.e. '60' is a 60X lens. Integer value >= 0 (no units) |
| `NORMALISATION_METHOD` | SpatialOmics | NormalisationMethod | No | Method used for normalizing the array data |
| `NUCLEIC_ACID_SOURCE` | scRNA-seq | NucleicAcidSourceEnum | Yes | Type of nucleic acid used for sequencing |
| `NUMBER_OF_CLUSTERS` | SpatialOmics | integer | No | Number of clusters identified |
| `NUMBER_OF_CYCLES` | Clinical | integer | No | Number of cycles of the administered therapeutic procedure. Use -1 if this data point is not available. (caDSR:3060718) (Aligns to CDRC Standard CDE) |
| `NUMBER_OF_FEATURES` | MultiplexMicroscopy, SpatialOmics | integer | Yes | Number of features (e.g. transcripts) |
| `NUMBER_OF_OBJECTS` | MultiplexMicroscopy, SpatialOmics | integer | Yes | Number of objects (e.g. cells) |
| `NUMBER_OF_SEGMENTED_CELLS` | SpatialOmics | integer | No | Total number of segmented cells |
| `OBJECTIVE` | DigitalPathology, Imaging, MultiplexMicroscopy | string | Yes | The manufacturer and or model number for the optical element that gathers light from an object being observed and focuses the light rays from it to... |
| `OFF_TREATMENT_REASON` | Clinical | OffTreatmentReasonEnum | No | Reason that an individual did not receive treatment. (caDSR:15743249) (Aligns to CDRC Standard CDE) |
| `OLIGO_BARCODE_LOWER_STRAND` | MultiplexMicroscopy | string | No | DNA barcode used for labeling |
| `OLIGO_BARCODE_UPPER_STRAND` | MultiplexMicroscopy | string | No | DNA barcode used for labeling |
| `OVERREPRESENTED_SEQUENCES` | WES | string | No | Overrepresented sequences |
| `PACK_YEARS_SMOKED` | Clinical | integer | No | Numeric computed value to represent lifetime tobacco exposure defined as number of cigarettes smoked per day x number of years smoked divided by 20... |
| `PAIRS_ON_DIFF_CHR` | WES | integer | No | Number of read pairs on different chromosomes |
| `PANEL_DATA` | SpatialOmics | SpatialPanel | No | Spatial panel information for targeted sequencing or protein panels |
| `PANEL_NAME` | SpatialOmics | string | No | Number of genes/proteins in panel |
| `PANEL_SIZE_TOTAL_TARGETS` | SpatialOmics | integer | Yes | Total number of targets in the panel |
| `PANEL_SYNAPSE_ID` | SpatialOmics | string | No | Synapse ID of the completed spatial_omics_panel template |
| `PASSED_QC` | DigitalPathology, Imaging, MultiplexMicroscopy | boolean | Yes | Confirm that the image has passed internal quality control checks |
| `PATHOGENICITY` | Clinical | PathogenicityEnum | No | Description of a variant's level of involvement in the cause of the individual's disease according to the standards outlined by the American Colleg... |
| `PERCENT_GC_CONTENT` | WES | float | No | Percent GC content |
| `PERCENT_NECROSIS` | Biospecimen | decimal | No | Numeric value to represent the percentage of cell death in a malignant tumor sample or specimen |
| `PERCENT_NORMAL_CELLS` | Biospecimen | decimal | No | Numeric value to represent the percentage of normal cell content in a malignant tumor sample or specimen |
| `PERCENT_TUMOR_CELLS` | Biospecimen | decimal | No | Numeric value that represents the percentage of infiltration by tumor cells in a sample |
| `PERCENT_TUMOR_NUCLEI` | Biospecimen | decimal | No | Numeric value to represent the percentage of tumor nuclei in a malignant neoplasm sample or specimen |
| `PER_BASE_N_CONTENT` | WES | string | No | Per base N content |
| `PER_BASE_SEQUENCE_CONTENT` | WES | string | No | Per base sequence content |
| `PER_BASE_SEQUENCE_QUALITY` | WES | string | No | Per base sequence quality |
| `PER_SEQUENCE_GC_CONTENT` | WES | string | No | Per sequence GC content |
| `PER_SEQUENCE_QUALITY_SCORE` | WES | string | No | Per sequence quality score |
| `PER_TILE_SEQUENCE_QUALITY` | WES | string | No | Per tile sequence quality |
| `PHARMACOTHERAPY_TYPE` | Clinical | PharmacotherapyTypeEnum | Yes | Whether single or combination pharmacotherapy was used. (caDSR:15743233) (Aligns to CDRC Standard CDE) |
| `PHYSICAL_SIZE_X` | MultiplexMicroscopy | float | Yes | Physical size of a single pixel in the x dimension. In microns. |
| `PHYSICAL_SIZE_Y` | MultiplexMicroscopy | float | Yes | Physical size of a single pixel in the y dimension. In microns. |
| `PHYSICAL_SIZE_Z` | MultiplexMicroscopy | float | Yes | Physical size of a single pixel in the z dimension. In microns. |
| `PLATFORM` | SpatialOmics | Platform | Yes | Name of the platform used to generate the data |
| `PORTAL_PREVIEW_FILE` | SpatialOmics | string | No | Relative path of HTML preview in bundle if present |
| `PRESERVATION_MEDIUM` | Biospecimen | PreservationMediumEnum | Yes | The kind of substance holding another substance in solution or suspension to maintain a specimen in a viable state |
| `PRESERVATION_METHOD` | Biospecimen | PreservationMethodEnum | Yes | Method used to preserve the sample |
| `PRESERVATION_METHOD_TEMPERATURE` | Biospecimen | PreservationTemperatureEnum | Yes | The term which describes the temperature used to maintain the specimen in a viable state |
| `PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID` | Clinical | PrimaryDiagnosisNCIThesaurusIDEnum | Yes | NCI Thesaurus concept identifier for primary diagnosis. Note that NCI Thesaurus offers very broad and very granular cancer types. Please select the... |
| `PROCESSING_LOCATION` | Biospecimen | string | No | Site with an HTAN center where specimen processing occurs |
| `PROGRESSION_OR_RECURRENCE` | Clinical | ProgressionOrRecurrenceEnum | Yes | Response indicating whether or not a subject has a progressive disease or a recurrent disease. (caDSR:13529783) (Aligns to CDRC Standard CDE) |
| `PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE` | Clinical | tissue_or_organ_of_origin_uberon_enum | No | UBERON identifier indicating where in the body a disease has progressed or recurred, e.g. UBERON:0000002. (caDSR:14883061) (Aligns to CDRC Standard... |
| `PROGRESSION_OR_RECURRENCE_TYPE` | Clinical | ProgressionTypeEnum | No | Type of worsening or reemergence of disease over time. (caDSR:14742451) (Aligns to CDRC Standard CDE) |
| `PROPORTION_BASE_MISMATCH` | WES | float | No | Proportion of base mismatches |
| `PROPORTION_COVERAGE_10X` | WES | float | No | Proportion of coverage at 10x |
| `PROPORTION_COVERAGE_30X` | WES | float | No | Proportion of coverage at 30x |
| `PROPORTION_READS_DUPLICATED` | WES | float | No | Proportion of duplicated reads |
| `PROPORTION_READS_MAPPED` | WES | float | Yes | Proportion of mapped reads |
| `PROPORTION_TARGETS_NO_COVERAGE` | WES | float | No | Proportion of targets with no coverage |
| `PROTEIN_MEASURED` | SpatialOmics | boolean | Yes | Whether protein was measured |
| `PROTOCOL_LINK` | SpatialOmics, WES, scRNA-seq | string | No | Link to sequencing protocol |
| `PYRAMID` | MultiplexMicroscopy | boolean | No | The data file contains an image pyramid |
| `QC_COMMENT` | DigitalPathology, Imaging, MultiplexMicroscopy | string | Yes | Comments related to quality control checks |
| `QC_FEATURE_NUMBER` | SpatialOmics | integer | Yes | Features (e.g. spots or bins) under tissue |
| `QC_MEAN_READS_PER_FEATURE` | SpatialOmics | float | Yes | Mean reads per feature |
| `QC_SPATIAL_UNIT` | SpatialOmics | QCSpatialUnit | Yes | Type of spatial unit |
| `QC_TOTAL_GENES_DETECTED` | SpatialOmics | integer | Yes | Total genes detected |
| `QC_TOTAL_NUMBER_OF_READS` | SpatialOmics | integer | Yes | Total number of reads |
| `QC_WORKFLOW_LINK` | WES | string | No | Link to QC workflow |
| `QC_WORKFLOW_TYPE` | WES | string | No | QC workflow type |
| `QC_WORKFLOW_VERSION` | WES | string | No | QC workflow version |
| `RACE` | Clinical | RaceEnum | Yes | Race of the participant (caDSR:2192199) (Aligns to CDRC Standard CDE) |
| `READ_INDICATOR` | WES, scRNA-seq | string | No | Read indicator |
| `READ_LENGTH` | WES | integer | Yes | Read length in base pairs |
| `REGIMEN_OR_LINE_OF_THERAPY` | Clinical | RegimenOrLineOfTherapyEnum | No | Description of the treatment regimen or line of therapy. (caDSR:15915841) (Aligns to CDRC Standard CDE) |
| `REGION_AREA` | SpatialOmics | float | Yes | Capture area in µm² |
| `RELATIVES_WITH_CANCER_HISTORY` | Clinical | integer | No | Number of relatives the individual has with a known history of cancer. Use -1 if this data point is not available. (caDSR:15907364) (No CRDC Standa... |
| `RESPONSE` | Clinical | DiseaseResponseEnum | No | The result of an evaluation to determine whether pathologic and/or clinical changes resulted from treatment. (caDSR:13383448) (Aligns to CDRC Stand... |
| `REVERSE_TRANSCRIPTION_PRIMER` | scRNA-seq | ReverseTranscriptionPrimerEnum | Yes | Primer used for reverse transcription |
| `RNA_MEASURED` | SpatialOmics | boolean | Yes | Whether RNA was measured |
| `RRID_IDENTIFIER` | MultiplexMicroscopy | string | No | Research Resource Identifier |
| `RUN_ID` | SpatialOmics | string | No | A unique identifier for this individual run (typically associated with a single slide) of the spatial transcriptomic processing workflow |
| `SAME_SECTION_IMAGING_CHANNELS` | SpatialOmics | string | No | Antigens targeted in same section fluorescence imaging |
| `SAME_SECTION_IMAGING_ID` | SpatialOmics | string | No | HTAN ID of data file that represents same section imaging |
| `SAME_SECTION_IMAGING_MODALITY` | SpatialOmics | SameSectionImagingModality | No | Was same section imaging performed |
| `SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION` | scRNA-seq | string | Yes | Parameters used to run the workflow. scRNA-seq level 3: e.g. Normalization and log transformation, ran empty drops or doublet detection, used filte... |
| `SCRNASEQ_WORKFLOW_TYPE` | scRNA-seq | scRNAseqWorkflowTypeEnumLevel2 | Yes | Generic name for the workflow used to analyze the dataset |
| `SECTION_NUMBER_IN_SEQUENCE` | Biospecimen | integer | No | Numeric value (integer, including ranges) provided to a sample in a series of sections |
| `SECTION_THICKNESS_VALUE` | Biospecimen | decimal | No | Numeric value to describe the thickness of a slice to tissue taken from a biospecimen, measured in microns |
| `SEGMENTATION_ANNOTATION_TYPE` | MultiplexMicroscopy | string | No | Type of objects segmented (e.g., Cell, Nucleus, Tissue, ROI) |
| `SEGMENTATION_METHOD` | MultiplexMicroscopy | string | Yes | Method used for segmentation (e.g., CellPose, StarDist, Ilastik, manual annotation) |
| `SEGMENTATION_PARAMETERS` | MultiplexMicroscopy | string | No | Parameters used for segmentation (e.g., model name, threshold values, preprocessing steps) |
| `SEGMENTATION_WORKFLOW_TYPE` | MultiplexMicroscopy | string | Yes | Type of segmentation workflow used to generate the mask |
| `SEGMENTATION_WORKFLOW_URL` | MultiplexMicroscopy | string | No | URL or link to the segmentation workflow used |
| `SEGMENTATION_WORKFLOW_VERSION` | MultiplexMicroscopy | string | No | Version of the segmentation workflow |
| `SEQUENCE_DUPLICATION_LEVELS` | WES | string | No | Sequence duplication levels |
| `SEQUENCE_LENGTH_DISTRIBUTION` | WES | string | No | Sequence length distribution |
| `SEQUENCING_BATCH_ID` | WES, scRNA-seq | string | No | Sequencing batch identifier |
| `SEQUENCING_CONFIGURATION` | SpatialOmics | string | No | Read and index setup |
| `SEQUENCING_DEPTH` | SpatialOmics | string | No | Sequencing depth |
| `SEQUENCING_FILE_TYPE` | SpatialOmics | SequencingFileType | No | Sequencing file type |
| `SEQUENCING_INSTRUMENT` | SpatialOmics | string | No | Sequencer used |
| `SEQUENCING_PLATFORM` | WES, scRNA-seq | SequencingPlatformEnum | Yes | Sequencing platform used |
| `SEX` | Clinical | SexEnum | Yes | Sex of the participant |
| `SHIPPING_CONDITION_TYPE` | Biospecimen | ShippingConditionEnum | Yes | Text descriptor of the shipping environment of a biospecimen |
| `SHORTEST_DIMENSION` | Biospecimen | decimal | No | Numeric value that represents the shortest dimension of the sample, measured in millimeters |
| `SHORT_READS` | WES | integer | No | Number of short reads |
| `SINGLE_CELL_ISOLATION_METHOD` | scRNA-seq | SingleCellIsolationMethodEnum | Yes | Method used to isolate single cells |
| `SITE_DATA_SOURCE` | Biospecimen | string | No | Text to identify the data source for the specimen/sample from within the HTAN center |
| `SITE_OF_RESECTION_OR_BIOPSY` | Biospecimen | tissue_or_organ_of_origin_uberon_enum | Yes | The location within the body from where the disease of interest originated as captured in the Uberon identifier |
| `SIZE_C` | MultiplexMicroscopy | integer | Yes | Number of channels. Integer >= 1 |
| `SIZE_SELECTION_RANGE` | WES | string | No | Size selection range |
| `SIZE_T` | MultiplexMicroscopy | integer | Yes | Number of timepoints. Integer >= 1 |
| `SIZE_X` | MultiplexMicroscopy | integer | Yes | The number of pixels in the x dimension at the highest resolution available |
| `SIZE_Y` | MultiplexMicroscopy | integer | Yes | The number of pixels in the y dimension at the highest resolution available |
| `SIZE_Z` | MultiplexMicroscopy | integer | Yes | The number of pixels in the z dimension at the highest resolution available |
| `SLICING_METHOD` | Biospecimen | SlicingMethodEnum | No | Imaging specific: the method by which the tissue was sliced |
| `SLIDE_CHARGE_TYPE` | Biospecimen | SlideChargeTypeEnum | No | A description of the charge on the glass slide |
| `SLIDE_LABEL_REDACTED` | DigitalPathology, Imaging, MultiplexMicroscopy | boolean | No | Have identifiers including dates been masked in the label image |
| `SLIDE_SERIAL_NUMBER` | SpatialOmics | string | No | Slide serial number |
| `SMOKING_HISTORY` | Clinical | SmokingHistoryEnum | Yes | Current or past smoking status. (caDSR:3626148) (Aligns to CRDC Node) |
| `SOFTWARE_AND_VERSION` | SpatialOmics | string | No | Software/tools used for processing |
| `SOMATIC_VARIANTS_SAMPLE_TYPE` | WES | SomaticVariantsSampleTypeEnum | No | Type of sample for somatic variants |
| `SOMATIC_VARIANTS_WORKFLOW_TYPE` | WES | string | No | Type of somatic variants workflow |
| `SOMATIC_VARIANTS_WORKFLOW_URL` | WES | string | No | URL to the somatic variants workflow |
| `SPATIAL_ASSAY_TYPE` | SpatialOmics | SpatialAssayType | No | Type of spatial assay (in situ or capture-based) |
| `SPECIES` | DigitalPathology, Imaging, MultiplexMicroscopy | Species | Yes | NCBI Taxonomy ID. Per RFC, the only valid value is "9606 (Homo sapiens)". |
| `SPECIMEN_CELLULAR_ARCHITECTURE` | Biospecimen | CellularArchitectureEnum | Yes | The architectural pattern of an abnormal, normal, or mixed cellular population in a tissue specimen |
| `SPECIMEN_LATERALITY` | Biospecimen | SpecimenLateralityEnum | Yes | For tumors in paired organs, designates the side on which the specimen was obtained |
| `SPIKE_IN` | scRNA-seq | SpikeInEnum | Yes | Type of spike-in used, if any |
| `STAINING_METHOD` | DigitalPathology, Imaging, MultiplexMicroscopy | StainingMethod | Yes | Any of the various methods that use a dye, reagent, or other material for producing coloration in tissues or microorganisms for microscopic examina... |
| `STRUCTURAL_VARIANT_WORKFLOW_TYPE` | WES | string | No | Type of structural variant workflow |
| `STRUCTURAL_VARIANT_WORKFLOW_URL` | WES | string | No | URL to the structural variant workflow |
| `SUB_CYCLE_NUMBER` | MultiplexMicroscopy | integer | No | Sub-cycle |
| `TARGET_CAPTURE_KIT` | WES | string | No | Target capture kit used |
| `TARGET_DEPTH` | WES | integer | No | Target sequencing depth |
| `TARGET_NAME` | MultiplexMicroscopy | string | No | Short descriptive name (abbreviation) for this target (antigen) |
| `TECHNICAL_REPLICATE_GROUP` | WES, scRNA-seq | string | No | Technical replicate group identifier |
| `TEST_ANALYTE_TYPE` | Clinical | TestAnalyteTypeEnum | No | Sample type or material being subjected to analysis. (caDSR:15063661) (Aligns to CDRC Standard CDE) |
| `TEST_RESULT` | Clinical | string | No | Specific result of a clinical molecular test. Use this field only if one of the permissible values in MOLECULAR_ANALYSIS_RESULT isn't relevant. Ple... |
| `TEST_UNITS` | Clinical | TestUnitsEnum | No | Preferred unit of measure (UOM) for a laboratory test result, per NCI standards or per protocol specification. (caDSR:2195977) (No CRDC Standard Av... |
| `THERAPEUTIC_AGENTS` | Clinical | AntineoplasticAgentEnum | No | The NCit Preferred Name(s) of the Therapeutic agent(s), as dervied from https://evs.nci.nih.gov/ftp1/NCI_Thesaurus/Drug_or_Substance/Antineoplastic... |
| `THERAPIES` | Clinical | Therapy | No | Therapy information |
| `THERAPY_ANATOMIC_SITE_UBERON_CODE` | Clinical | tissue_or_organ_of_origin_uberon_enum | No | UBERON identifier for the location within the body targeted by a therapeutic procedure, e.g. UBERON:0000002. (caDSR:14461856) (Aligns to CDRC Stand... |
| `TIMEPOINT` | Biospecimen | TimepointEnum | No | A specific point in the time continuum, including those established relative to an event |
| `TIMEPOINT_LABEL` | Clinical | string | No | Label to identify the time point at which the clinical data or biospecimen was obtained (e.g. Baseline, End of Treatment, Overall survival, Final).... |
| `TISSUE_OR_ORGAN_OF_ORIGIN` | Clinical | tissue_or_organ_of_origin_uberon_enum | Yes | The tissue or organ of origin for the primary diagnosis, using UBERON codes |
| `TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE` | Clinical | tissue_or_organ_of_origin_uberon_enum | Yes | UBERON identifier indicating the tissue or organ where the disease of interest originated, e.g. UBERON:0000002. (caDSR:14883047) (Aligns to CDRC St... |
| `TOOL_COMPATIBILITY` | SpatialOmics | ToolCompatibility | No | Tools or libraries compatible with this file |
| `TOTAL_READS` | WES | integer | Yes | Total number of reads |
| `TOTAL_UNIQUELY_MAPPED` | WES | integer | Yes | Total number of uniquely mapped reads |
| `TOTAL_UNMAPPED_READS` | WES | integer | Yes | Total number of unmapped reads |
| `TO_TRIM_ADAPTER_SEQUENCE` | WES | boolean | No | Whether to trim adapter sequence |
| `TRANSCRIPTOME_TYPE` | SpatialOmics | TranscriptomeType | No | Molecular targets measured using panels |
| `TREATMENT_INTENT_TYPE` | Clinical | TreatmentIntentTypeEnum | Yes | Anticipated outcome for therapy. (caDSR:15157467) (Aligns to CDRC Standard CDE) |
| `TREATMENT_TYPE` | Clinical | TreatmentTypeEnum | Yes | Type of treatment administered. (caDSR:14737565) (Aligns to CDRC Standard CDE) |
| `TUMOR_CLASSIFICATION` | Biospecimen | TumorClassificationEnum | No | The classification of a tumor at a particular time based primarily on histopathological characteristics |
| `TUMOR_CLASSIFICATION_CATEGORY` | Clinical | TumorClassificationCategoryEnum | Yes | Classification of a tumor at a particular time based primarily on histopathological characteristics. (caDSR:12922545) (Aligns to CDRC Standard CDE) |
| `TUMOR_GRADE` | Clinical | TumorGradeEnum | Yes | Degree of abnormality of cancer cells as a measure of differentiation and aggressiveness. (caDSR:11325685) (Aligns to CDRC Standard CDE) |
| `TUMOR_STAGED` | Clinical | TumorStagedEnum | Yes | Indicator of whether the tumor was staged using the AJCC classification system. |
| `UMI_TAG` | scRNA-seq | string | No | Tag used for UMIs |
| `USER_GENE_NAME` | SpatialOmics | string | No | Optional user-defined name for the Gene |
| `VARIANT_ORIGIN` | Clinical | VariantOriginEnum | No | Biological origin of a specific genetic variant identified by a clinical test. (caDSR:14473382) (No CRDC Standard Available) |
| `VARIANT_TYPE` | Clinical | VariantTypeEnum | No | Description of the type of genetic variation. (caDSR:6142402) (No CRDC Standard Available) |
| `VITAL_STATUS` | Clinical | VitalStatusEnum | Yes | Survival status for individual. (caDSR:2847330) (Aligns to CDRC Standard CDE) |
| `WHITELIST_CELL_BARCODE_FILE_LINK` | scRNA-seq | string | No | Link to whitelist cell barcode file |
| `WORKFLOW_LINK` | WES, scRNA-seq | string | Yes | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | WES, scRNA-seq | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKING_DISTANCE` | MultiplexMicroscopy | string | No | The working distance of the lens, expressed as a floating point number. Floating point > 0. Size needs to be specified in microns (um) |
| `YEARS_SMOKED` | Clinical | integer | No | Number of years a person has been smoking. Use -1 if this data point is not available. (caDSR:3137957) (No CRDC Standard Available) |
| `caDSR_id` | Biospecimen, Clinical, MultiplexMicroscopy, SpatialOmics, WES | string | No | The caDSR identifier for this element |
| `extension_tag` | Biospecimen, Clinical, DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES | uriorcurie | Yes | a tag associated with an extension |
| `extension_value` | Biospecimen, Clinical, DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES | AnyValue | Yes | the actual annotation |
| `extensions` | Biospecimen, Clinical, DigitalPathology, Imaging, MultiplexMicroscopy, SpatialOmics, WES | extension | No | a tag/text tuple attached to an arbitrary element |
| `level1_data` | scRNA-seq | scRNALevel1 | No | Level 1 scRNA-seq data |
| `level2_data` | scRNA-seq | scRNALevel2 | No | Level 2 scRNA-seq data |
| `level3_4_data` | scRNA-seq | scRNALevel3and4 | No | Level 3/4 scRNA-seq data |
