-- # Class: "ClinicalData" Description: "Container for all clinical data"
--     * Slot: COMPONENT Description: Category of metadata (e.g., Bulk WES Level 1, scRNA-seq Level 2, etc.)
--     * Slot: FILENAME Description: Name of the file
--     * Slot: FILE_FORMAT Description: Format of the file (e.g., fastq, bam, vcf, h5ad)
--     * Slot: HTAN_DATA_FILE_ID Description: HTAN Data File ID (Primary Key)
--     * Slot: HTAN_PARENT_ID Description: HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
--     * Slot: DEMOGRAPHICS_id Description: Demographic information
--     * Slot: VITAL_STATUS_id Description: Vital status information
--     * Slot: DIAGNOSIS_id Description: Primary diagnosis information
--     * Slot: EXPOSURES_id Description: Exposure history
--     * Slot: FAMILY_HISTORY_id Description: Family history of cancer
-- # Class: "AnyValue" Description: ""
--     * Slot: id Description: 
-- # Class: "extension" Description: "a tag/value pair used to add non-model information to an entry"
--     * Slot: tag Description: a tag associated with an extension
--     * Slot: extension_tag Description: Autocreated FK slot
--     * Slot: extensible_id Description: Autocreated FK slot
--     * Slot: value_id Description: the actual annotation
-- # Class: "extensible" Description: "mixin for classes that support extension"
--     * Slot: id Description: 
-- # Class: "CoreFileAttributes" Description: "Universal attributes that apply to all file-based data in HTAN"
--     * Slot: COMPONENT Description: Category of metadata (e.g., Bulk WES Level 1, scRNA-seq Level 2, etc.)
--     * Slot: FILENAME Description: Name of the file
--     * Slot: FILE_FORMAT Description: Format of the file (e.g., fastq, bam, vcf, h5ad)
--     * Slot: HTAN_DATA_FILE_ID Description: HTAN Data File ID (Primary Key)
--     * Slot: HTAN_PARENT_ID Description: HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
-- # Class: "Demographics" Description: "Information about the demographics"
--     * Slot: id Description: 
--     * Slot: ETHNIC_GROUP Description: Ethnic group of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
--     * Slot: GENDER_IDENTITY Description: Gender identity of the participant (caDSR:2192202) (Aligns to CDRC Standard CDE)
--     * Slot: SEX Description: Sex of the participant (caDSR:2192203) (Aligns to CDRC Standard CDE)
--     * Slot: RACE Description: Race of the participant (caDSR:2192204) (Aligns to CDRC Standard CDE)
-- # Class: "Diagnosis" Description: "Information about the diagnosis"
--     * Slot: id Description: 
--     * Slot: PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID Description: NCI Thesaurus ID for the primary diagnosis (caDSR:2192201) (Aligns to CDRC Standard CDE)
--     * Slot: AGE_IN_DAYS_AT_DIAGNOSIS Description: Age in days at which the diagnosis was made (caDSR:2192202) (Aligns to CDRC Standard CDE)
--     * Slot: TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE Description: UBERON code for the tissue or organ of origin (caDSR:2192205) (Aligns to CDRC Standard CDE)
--     * Slot: TUMOR_GRADE Description: The grade of the tumor (caDSR:2192203) (Aligns to CDRC Standard CDE)
--     * Slot: CLINICAL_T_STAGE Description: Required when TUMOR_STAGE is any stage value
--     * Slot: CLINICAL_N_STAGE Description: Required when TUMOR_STAGE is any stage value
--     * Slot: CLINICAL_M_STAGE Description: Required when TUMOR_STAGE is any stage value
--     * Slot: AJCC_STAGING_SYSTEM_EDITION Description: Required when TUMOR_STAGE is any stage value
--     * Slot: AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS Description: Age in days at which the last known disease status was recorded (caDSR:2192203) (Aligns to CDRC Standard CDE)
--     * Slot: LAST_KNOWN_DISEASE_STATUS Description: Last known disease status (caDSR:2192210) (Aligns to CDRC Standard CDE)
--     * Slot: TUMOR_CLASSIFICATION_CATEGORY Description: Classification category of the tumor (caDSR:2192211) (Aligns to CDRC Standard CDE)
--     * Slot: METASTASIS_AT_DIAGNOSIS Description: Required when TUMOR_STAGE is Stage IV or any of its substages
--     * Slot: METHOD_OF_DIAGNOSIS Description: Method used to make the diagnosis (caDSR:2192213) (Aligns to CDRC Standard CDE)
-- # Class: "Exposure" Description: "Information about the exposure"
--     * Slot: id Description: 
--     * Slot: SMOKING_HISTORY Description: Smoking history of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
--     * Slot: YEARS_SMOKED Description: Required when SMOKING_HISTORY is Current smoker or Former smoker
--     * Slot: PACK_YEARS_SMOKED Description: Required when SMOKING_HISTORY is Current smoker or Former smoker
--     * Slot: ALCOHOL_HISTORY_INDICATOR Description: Alcohol history indicator of the participant (caDSR:2192204) (Aligns to CDRC Standard CDE)
--     * Slot: ENVIRONMENTAL_EXPOSURE Description: Environmental exposure of the participant (caDSR:2192205) (Aligns to CDRC Standard CDE)
--     * Slot: ENVIRONMENTAL_EXPOSURE_TYPE Description: Required when ENVIRONMENTAL_EXPOSURE is Yes
-- # Class: "FamilyHistory" Description: "A class to capture information about the cancer history of family members."
--     * Slot: id Description: 
--     * Slot: FAMILY_MEMBER_CANCER_HISTORY Description: Has a family member been diagnosed with cancer?
--     * Slot: RELATIVES_WITH_CANCER_HISTORY Description: Number of first degree relatives with cancer history
-- # Class: "FollowUp" Description: "Clinical follow-up information"
--     * Slot: id Description: 
--     * Slot: AGE_IN_DAYS_AT_FOLLOWUP Description: Age in days at follow-up
--     * Slot: PROGRESSION_OR_RECURRENCE Description: Indicates whether the disease has progressed or recurred
--     * Slot: PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE Description: Required when PROGRESSION_OR_RECURRENCE is Yes
--     * Slot: PROGRESSION_OR_RECURRENCE_TYPE Description: Required when PROGRESSION_OR_RECURRENCE is Yes
--     * Slot: EVIDENCE_OF_RECURRENCE_TYPE Description: Required when PROGRESSION_OR_RECURRENCE is Yes
--     * Slot: AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE Description: Required when PROGRESSION_OR_RECURRENCE is Yes
--     * Slot: DISEASE_RESPONSE Description: Response to treatment
--     * Slot: ECOG_PERFORMANCE_STATUS Description: ECOG performance status
--     * Slot: MENOPAUSE_STATUS Description: Menopause status
-- # Class: "MolecularTest" Description: "Information about the molecular test"
--     * Slot: id Description: 
--     * Slot: TIMEPOINT_LABEL Description: Label for the timepoint (caDSR:2192201) (Aligns to CDRC Standard CDE)
--     * Slot: AGE_IN_DAYS_AT_MOLECULAR_TEST_START Description: Age in days at molecular test start (caDSR:2192202) (Aligns to CDRC Standard CDE)
--     * Slot: AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP Description: Required when MOLECULAR_ANALYSIS_METHOD is DNA Sequencing or RNA Sequencing
--     * Slot: GENE_SYMBOL Description: Gene symbol (caDSR:2192204) (Aligns to CDRC Standard CDE)
--     * Slot: MOLECULAR_ANALYSIS_METHOD Description: Molecular analysis method (caDSR:2192205) (Aligns to CDRC Standard CDE)
--     * Slot: MOLECULAR_ANALYSIS_RESULT Description: Molecular analysis result (caDSR:2192206) (Aligns to CDRC Standard CDE)
--     * Slot: AA_CHANGE Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
--     * Slot: CLINICAL_BIOSPECIMEN_TYPE Description: Clinical biospecimen type (caDSR:2192208) (Aligns to CDRC Standard CDE)
--     * Slot: COPY_NUMBER Description: Required when MOLECULAR_ANALYSIS_RESULT is Copy number variant detected
--     * Slot: EXON Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
--     * Slot: MOLECULAR_CONSEQUENCE Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
--     * Slot: PATHOGENICITY Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
--     * Slot: TEST_ANALYTE_TYPE Description: Required when MOLECULAR_ANALYSIS_METHOD is DNA Sequencing or RNA Sequencing
--     * Slot: TEST_UNITS Description: Required when MOLECULAR_ANALYSIS_RESULT is Copy number variant detected
--     * Slot: TEST_RESULT Description: Test result (caDSR:2192215) (Aligns to CDRC Standard CDE)
--     * Slot: VARIANT_ORIGIN Description: Variant origin (caDSR:2192216) (Aligns to CDRC Standard CDE)
--     * Slot: VARIANT_TYPE Description: Variant type (caDSR:2192217) (Aligns to CDRC Standard CDE)
-- # Class: "Therapy" Description: "Information about therapeutic interventions"
--     * Slot: id Description: 
--     * Slot: INITIAL_DISEASE_STATUS Description: Status of the individual's malignancy when the treatment began
--     * Slot: TREATMENT_INTENT_TYPE Description: Anticipated outcome for therapy
--     * Slot: PHARMACOTHERAPY_TYPE Description: Whether single or combination pharmacotherapy was used
--     * Slot: THERAPY_ANATOMIC_SITE_UBERON_CODE Description: Required when TREATMENT_TYPE is a surgical or radiation therapy
--     * Slot: AGE_IN_DAYS_AT_TREATMENT_START Description: The age in days of the subject at the time that this treatment was started
--     * Slot: AGE_IN_DAYS_AT_TREATMENT_END Description: The age in days of the subject at the time that this treatment was completed
--     * Slot: OFF_TREATMENT_REASON Description: Required when AGE_IN_DAYS_AT_TREATMENT_END is present
--     * Slot: REGIMEN_OR_LINE_OF_THERAPY Description: Required when TREATMENT_TYPE is pharmacotherapy
--     * Slot: NUMBER_OF_CYCLES Description: Required when TREATMENT_TYPE is pharmacotherapy
--     * Slot: RESPONSE Description: Required when AGE_IN_DAYS_AT_TREATMENT_END is present
-- # Class: "VitalStatus" Description: "Information about the vital status"
--     * Slot: id Description: 
--     * Slot: VITAL_STATUS Description: Vital status of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
--     * Slot: AGE_IN_DAYS_AT_DEATH Description: Required when VITAL_STATUS is Deceased
--     * Slot: CAUSE_OF_DEATH Description: Required when VITAL_STATUS is Deceased
--     * Slot: CAUSE_OF_DEATH_SOURCE Description: Required when VITAL_STATUS is Deceased
-- # Class: "ClinicalData_FOLLOW_UPS" Description: ""
--     * Slot: ClinicalData_HTAN_DATA_FILE_ID Description: Autocreated FK slot
--     * Slot: FOLLOW_UPS_id Description: Follow-up observations
-- # Class: "ClinicalData_MOLECULAR_TESTS" Description: ""
--     * Slot: ClinicalData_HTAN_DATA_FILE_ID Description: Autocreated FK slot
--     * Slot: MOLECULAR_TESTS_id Description: Molecular test results
-- # Class: "ClinicalData_THERAPIES" Description: ""
--     * Slot: ClinicalData_HTAN_DATA_FILE_ID Description: Autocreated FK slot
--     * Slot: THERAPIES_id Description: Therapy information
-- # Class: "Therapy_TREATMENT_TYPE" Description: ""
--     * Slot: Therapy_id Description: Autocreated FK slot
--     * Slot: TREATMENT_TYPE Description: Type of treatment administered
-- # Class: "Therapy_THERAPEUTIC_AGENTS" Description: ""
--     * Slot: Therapy_id Description: Autocreated FK slot
--     * Slot: THERAPEUTIC_AGENTS Description: The NCit Preferred Name(s) of the Therapeutic agent(s)

CREATE TABLE "AnyValue" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE extensible (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "CoreFileAttributes" (
	"COMPONENT" TEXT NOT NULL, 
	"FILENAME" TEXT NOT NULL, 
	"FILE_FORMAT" TEXT NOT NULL, 
	"HTAN_DATA_FILE_ID" TEXT NOT NULL, 
	"HTAN_PARENT_ID" TEXT NOT NULL, 
	PRIMARY KEY ("HTAN_DATA_FILE_ID")
);
CREATE TABLE "Demographics" (
	id INTEGER NOT NULL, 
	"ETHNIC_GROUP" VARCHAR(22) NOT NULL, 
	"GENDER_IDENTITY" VARCHAR(12) NOT NULL, 
	"SEX" VARCHAR(12) NOT NULL, 
	"RACE" VARCHAR(41) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Diagnosis" (
	id INTEGER NOT NULL, 
	"PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID" TEXT NOT NULL, 
	"AGE_IN_DAYS_AT_DIAGNOSIS" INTEGER NOT NULL, 
	"TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE" VARCHAR(14) NOT NULL, 
	"TUMOR_GRADE" VARCHAR(12) NOT NULL, 
	"CLINICAL_T_STAGE" VARCHAR(12), 
	"CLINICAL_N_STAGE" VARCHAR(12), 
	"CLINICAL_M_STAGE" VARCHAR(12), 
	"AJCC_STAGING_SYSTEM_EDITION" VARCHAR(12), 
	"AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS" INTEGER NOT NULL, 
	"LAST_KNOWN_DISEASE_STATUS" VARCHAR(19) NOT NULL, 
	"TUMOR_CLASSIFICATION_CATEGORY" VARCHAR(12) NOT NULL, 
	"METASTASIS_AT_DIAGNOSIS" VARCHAR(12), 
	"METHOD_OF_DIAGNOSIS" VARCHAR(12) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Exposure" (
	id INTEGER NOT NULL, 
	"SMOKING_HISTORY" VARCHAR(14) NOT NULL, 
	"YEARS_SMOKED" INTEGER, 
	"PACK_YEARS_SMOKED" INTEGER, 
	"ALCOHOL_HISTORY_INDICATOR" VARCHAR(12) NOT NULL, 
	"ENVIRONMENTAL_EXPOSURE" VARCHAR(12) NOT NULL, 
	"ENVIRONMENTAL_EXPOSURE_TYPE" VARCHAR(12), 
	PRIMARY KEY (id)
);
CREATE TABLE "FamilyHistory" (
	id INTEGER NOT NULL, 
	"FAMILY_MEMBER_CANCER_HISTORY" VARCHAR(12), 
	"RELATIVES_WITH_CANCER_HISTORY" INTEGER, 
	PRIMARY KEY (id)
);
CREATE TABLE "FollowUp" (
	id INTEGER NOT NULL, 
	"AGE_IN_DAYS_AT_FOLLOWUP" INTEGER NOT NULL, 
	"PROGRESSION_OR_RECURRENCE" VARCHAR(22) NOT NULL, 
	"PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE" VARCHAR(14), 
	"PROGRESSION_OR_RECURRENCE_TYPE" VARCHAR(12), 
	"EVIDENCE_OF_RECURRENCE_TYPE" VARCHAR(12), 
	"AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE" INTEGER, 
	"DISEASE_RESPONSE" VARCHAR(22) NOT NULL, 
	"ECOG_PERFORMANCE_STATUS" VARCHAR(1) NOT NULL, 
	"MENOPAUSE_STATUS" VARCHAR(28), 
	PRIMARY KEY (id)
);
CREATE TABLE "MolecularTest" (
	id INTEGER NOT NULL, 
	"TIMEPOINT_LABEL" TEXT NOT NULL, 
	"AGE_IN_DAYS_AT_MOLECULAR_TEST_START" INTEGER NOT NULL, 
	"AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP" INTEGER, 
	"GENE_SYMBOL" VARCHAR(12) NOT NULL, 
	"MOLECULAR_ANALYSIS_METHOD" VARCHAR(14) NOT NULL, 
	"MOLECULAR_ANALYSIS_RESULT" TEXT NOT NULL, 
	"AA_CHANGE" TEXT, 
	"CLINICAL_BIOSPECIMEN_TYPE" VARCHAR(12) NOT NULL, 
	"COPY_NUMBER" INTEGER, 
	"EXON" INTEGER, 
	"MOLECULAR_CONSEQUENCE" VARCHAR(12), 
	"PATHOGENICITY" VARCHAR(17), 
	"TEST_ANALYTE_TYPE" VARCHAR(12), 
	"TEST_UNITS" TEXT, 
	"TEST_RESULT" TEXT NOT NULL, 
	"VARIANT_ORIGIN" VARCHAR(12) NOT NULL, 
	"VARIANT_TYPE" VARCHAR(12) NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Therapy" (
	id INTEGER NOT NULL, 
	"INITIAL_DISEASE_STATUS" TEXT NOT NULL, 
	"TREATMENT_INTENT_TYPE" VARCHAR(12) NOT NULL, 
	"PHARMACOTHERAPY_TYPE" VARCHAR(16) NOT NULL, 
	"THERAPY_ANATOMIC_SITE_UBERON_CODE" VARCHAR(14), 
	"AGE_IN_DAYS_AT_TREATMENT_START" INTEGER NOT NULL, 
	"AGE_IN_DAYS_AT_TREATMENT_END" INTEGER NOT NULL, 
	"OFF_TREATMENT_REASON" VARCHAR(27), 
	"REGIMEN_OR_LINE_OF_THERAPY" VARCHAR(12), 
	"NUMBER_OF_CYCLES" INTEGER, 
	"RESPONSE" TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "VitalStatus" (
	id INTEGER NOT NULL, 
	"VITAL_STATUS" VARCHAR(12) NOT NULL, 
	"AGE_IN_DAYS_AT_DEATH" INTEGER, 
	"CAUSE_OF_DEATH" VARCHAR(12), 
	"CAUSE_OF_DEATH_SOURCE" VARCHAR(17), 
	PRIMARY KEY (id)
);
CREATE TABLE "ClinicalData" (
	"COMPONENT" TEXT NOT NULL, 
	"FILENAME" TEXT NOT NULL, 
	"FILE_FORMAT" TEXT NOT NULL, 
	"HTAN_DATA_FILE_ID" TEXT NOT NULL, 
	"HTAN_PARENT_ID" TEXT NOT NULL, 
	"DEMOGRAPHICS_id" INTEGER NOT NULL, 
	"VITAL_STATUS_id" INTEGER NOT NULL, 
	"DIAGNOSIS_id" INTEGER NOT NULL, 
	"EXPOSURES_id" INTEGER NOT NULL, 
	"FAMILY_HISTORY_id" INTEGER NOT NULL, 
	PRIMARY KEY ("HTAN_DATA_FILE_ID"), 
	FOREIGN KEY("DEMOGRAPHICS_id") REFERENCES "Demographics" (id), 
	FOREIGN KEY("VITAL_STATUS_id") REFERENCES "VitalStatus" (id), 
	FOREIGN KEY("DIAGNOSIS_id") REFERENCES "Diagnosis" (id), 
	FOREIGN KEY("EXPOSURES_id") REFERENCES "Exposure" (id), 
	FOREIGN KEY("FAMILY_HISTORY_id") REFERENCES "FamilyHistory" (id)
);
CREATE TABLE extension (
	tag TEXT NOT NULL, 
	extension_tag TEXT, 
	extensible_id INTEGER, 
	value_id INTEGER NOT NULL, 
	PRIMARY KEY (tag, extension_tag, extensible_id, value_id), 
	UNIQUE (extension_tag, tag), 
	UNIQUE (extensible_id, tag), 
	FOREIGN KEY(extension_tag) REFERENCES extension (tag), 
	FOREIGN KEY(extensible_id) REFERENCES extensible (id), 
	FOREIGN KEY(value_id) REFERENCES "AnyValue" (id)
);
CREATE TABLE "Therapy_TREATMENT_TYPE" (
	"Therapy_id" INTEGER, 
	"TREATMENT_TYPE" VARCHAR(50) NOT NULL, 
	PRIMARY KEY ("Therapy_id", "TREATMENT_TYPE"), 
	FOREIGN KEY("Therapy_id") REFERENCES "Therapy" (id)
);
CREATE TABLE "Therapy_THERAPEUTIC_AGENTS" (
	"Therapy_id" INTEGER, 
	"THERAPEUTIC_AGENTS" VARCHAR(12) NOT NULL, 
	PRIMARY KEY ("Therapy_id", "THERAPEUTIC_AGENTS"), 
	FOREIGN KEY("Therapy_id") REFERENCES "Therapy" (id)
);
CREATE TABLE "ClinicalData_FOLLOW_UPS" (
	"ClinicalData_HTAN_DATA_FILE_ID" TEXT, 
	"FOLLOW_UPS_id" INTEGER, 
	PRIMARY KEY ("ClinicalData_HTAN_DATA_FILE_ID", "FOLLOW_UPS_id"), 
	FOREIGN KEY("ClinicalData_HTAN_DATA_FILE_ID") REFERENCES "ClinicalData" ("HTAN_DATA_FILE_ID"), 
	FOREIGN KEY("FOLLOW_UPS_id") REFERENCES "FollowUp" (id)
);
CREATE TABLE "ClinicalData_MOLECULAR_TESTS" (
	"ClinicalData_HTAN_DATA_FILE_ID" TEXT, 
	"MOLECULAR_TESTS_id" INTEGER, 
	PRIMARY KEY ("ClinicalData_HTAN_DATA_FILE_ID", "MOLECULAR_TESTS_id"), 
	FOREIGN KEY("ClinicalData_HTAN_DATA_FILE_ID") REFERENCES "ClinicalData" ("HTAN_DATA_FILE_ID"), 
	FOREIGN KEY("MOLECULAR_TESTS_id") REFERENCES "MolecularTest" (id)
);
CREATE TABLE "ClinicalData_THERAPIES" (
	"ClinicalData_HTAN_DATA_FILE_ID" TEXT, 
	"THERAPIES_id" INTEGER, 
	PRIMARY KEY ("ClinicalData_HTAN_DATA_FILE_ID", "THERAPIES_id"), 
	FOREIGN KEY("ClinicalData_HTAN_DATA_FILE_ID") REFERENCES "ClinicalData" ("HTAN_DATA_FILE_ID"), 
	FOREIGN KEY("THERAPIES_id") REFERENCES "Therapy" (id)
);