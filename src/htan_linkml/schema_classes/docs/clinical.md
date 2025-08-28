
# Clinical


**metamodel version:** 1.7.0

**version:** None


HTAN Clinical Data Model Schema


### Classes

 * [AnyValue](AnyValue.md)
 * [CoreFileAttributes](CoreFileAttributes.md) - Universal attributes that apply to all file-based data in HTAN
     * [ClinicalData](ClinicalData.md) - Container for all clinical data
 * [Demographics](Demographics.md) - Information about the demographics
 * [Diagnosis](Diagnosis.md) - Information about the diagnosis
 * [Exposure](Exposure.md) - Information about the exposure
 * [FamilyHistory](FamilyHistory.md) - A class to capture information about the cancer history of family members.
 * [FollowUp](FollowUp.md) - Clinical follow-up information
 * [MolecularTest](MolecularTest.md) - Information about the molecular test
 * [Therapy](Therapy.md) - Information about therapeutic interventions
 * [VitalStatus](VitalStatus.md) - Information about the vital status
 * [Extension](Extension.md) - a tag/value pair used to add non-model information to an entry

### Mixins

 * [Extensible](Extensible.md) - mixin for classes that support extension

### Slots

 * [AA_CHANGE](AA_CHANGE.md) - Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * [MolecularTest➞AA_CHANGE](MolecularTest_AA_CHANGE.md)
 * [AGE_IN_DAYS_AT_DEATH](AGE_IN_DAYS_AT_DEATH.md) - Required when VITAL_STATUS is Deceased
     * [VitalStatus➞AGE_IN_DAYS_AT_DEATH](VitalStatus_AGE_IN_DAYS_AT_DEATH.md)
 * [AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP](AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP.md) - Required when MOLECULAR_ANALYSIS_METHOD is DNA Sequencing or RNA Sequencing
     * [MolecularTest➞AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP](MolecularTest_AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP.md)
 * [AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE](AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE.md) - Required when PROGRESSION_OR_RECURRENCE is Yes
     * [FollowUp➞AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE](FollowUp_AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE.md)
 * [AJCC_STAGING_SYSTEM_EDITION](AJCC_STAGING_SYSTEM_EDITION.md) - Required when TUMOR_STAGE is any stage value
     * [Diagnosis➞AJCC_STAGING_SYSTEM_EDITION](Diagnosis_AJCC_STAGING_SYSTEM_EDITION.md)
 * [CAUSE_OF_DEATH](CAUSE_OF_DEATH.md) - Required when VITAL_STATUS is Deceased
     * [VitalStatus➞CAUSE_OF_DEATH](VitalStatus_CAUSE_OF_DEATH.md)
 * [CAUSE_OF_DEATH_SOURCE](CAUSE_OF_DEATH_SOURCE.md) - Required when VITAL_STATUS is Deceased
     * [VitalStatus➞CAUSE_OF_DEATH_SOURCE](VitalStatus_CAUSE_OF_DEATH_SOURCE.md)
 * [CLINICAL_M_STAGE](CLINICAL_M_STAGE.md) - Required when TUMOR_STAGE is any stage value
     * [Diagnosis➞CLINICAL_M_STAGE](Diagnosis_CLINICAL_M_STAGE.md)
 * [CLINICAL_N_STAGE](CLINICAL_N_STAGE.md) - Required when TUMOR_STAGE is any stage value
     * [Diagnosis➞CLINICAL_N_STAGE](Diagnosis_CLINICAL_N_STAGE.md)
 * [CLINICAL_T_STAGE](CLINICAL_T_STAGE.md) - Required when TUMOR_STAGE is any stage value
     * [Diagnosis➞CLINICAL_T_STAGE](Diagnosis_CLINICAL_T_STAGE.md)
 * [COPY_NUMBER](COPY_NUMBER.md) - Required when MOLECULAR_ANALYSIS_RESULT is Copy number variant detected
     * [MolecularTest➞COPY_NUMBER](MolecularTest_COPY_NUMBER.md)
 * [ENVIRONMENTAL_EXPOSURE_TYPE](ENVIRONMENTAL_EXPOSURE_TYPE.md) - Required when ENVIRONMENTAL_EXPOSURE is Yes
     * [Exposure➞ENVIRONMENTAL_EXPOSURE_TYPE](Exposure_ENVIRONMENTAL_EXPOSURE_TYPE.md)
 * [EVIDENCE_OF_RECURRENCE_TYPE](EVIDENCE_OF_RECURRENCE_TYPE.md) - Required when PROGRESSION_OR_RECURRENCE is Yes
     * [FollowUp➞EVIDENCE_OF_RECURRENCE_TYPE](FollowUp_EVIDENCE_OF_RECURRENCE_TYPE.md)
 * [EXON](EXON.md) - Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * [MolecularTest➞EXON](MolecularTest_EXON.md)
 * [METASTASIS_AT_DIAGNOSIS](METASTASIS_AT_DIAGNOSIS.md) - Required when TUMOR_STAGE is Stage IV or any of its substages
     * [Diagnosis➞METASTASIS_AT_DIAGNOSIS](Diagnosis_METASTASIS_AT_DIAGNOSIS.md)
 * [MOLECULAR_CONSEQUENCE](MOLECULAR_CONSEQUENCE.md) - Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * [MolecularTest➞MOLECULAR_CONSEQUENCE](MolecularTest_MOLECULAR_CONSEQUENCE.md)
 * [NUMBER_OF_CYCLES](NUMBER_OF_CYCLES.md) - Required when TREATMENT_TYPE is pharmacotherapy
     * [Therapy➞NUMBER_OF_CYCLES](Therapy_NUMBER_OF_CYCLES.md)
 * [OFF_TREATMENT_REASON](OFF_TREATMENT_REASON.md) - Required when AGE_IN_DAYS_AT_TREATMENT_END is present
     * [Therapy➞OFF_TREATMENT_REASON](Therapy_OFF_TREATMENT_REASON.md)
 * [PACK_YEARS_SMOKED](PACK_YEARS_SMOKED.md) - Required when SMOKING_HISTORY is Current smoker or Former smoker
     * [Exposure➞PACK_YEARS_SMOKED](Exposure_PACK_YEARS_SMOKED.md)
 * [PATHOGENICITY](PATHOGENICITY.md) - Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * [MolecularTest➞PATHOGENICITY](MolecularTest_PATHOGENICITY.md)
 * [PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE](PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE.md) - Required when PROGRESSION_OR_RECURRENCE is Yes
     * [FollowUp➞PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE](FollowUp_PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE.md)
 * [PROGRESSION_OR_RECURRENCE_TYPE](PROGRESSION_OR_RECURRENCE_TYPE.md) - Required when PROGRESSION_OR_RECURRENCE is Yes
     * [FollowUp➞PROGRESSION_OR_RECURRENCE_TYPE](FollowUp_PROGRESSION_OR_RECURRENCE_TYPE.md)
 * [REGIMEN_OR_LINE_OF_THERAPY](REGIMEN_OR_LINE_OF_THERAPY.md) - Required when TREATMENT_TYPE is pharmacotherapy
     * [Therapy➞REGIMEN_OR_LINE_OF_THERAPY](Therapy_REGIMEN_OR_LINE_OF_THERAPY.md)
 * [RESPONSE](RESPONSE.md) - Required when AGE_IN_DAYS_AT_TREATMENT_END is present
     * [Therapy➞RESPONSE](Therapy_RESPONSE.md)
 * [TEST_ANALYTE_TYPE](TEST_ANALYTE_TYPE.md) - Required when MOLECULAR_ANALYSIS_METHOD is DNA Sequencing or RNA Sequencing
     * [MolecularTest➞TEST_ANALYTE_TYPE](MolecularTest_TEST_ANALYTE_TYPE.md)
 * [TEST_UNITS](TEST_UNITS.md) - Required when MOLECULAR_ANALYSIS_RESULT is Copy number variant detected
     * [MolecularTest➞TEST_UNITS](MolecularTest_TEST_UNITS.md)
 * [THERAPY_ANATOMIC_SITE_UBERON_CODE](THERAPY_ANATOMIC_SITE_UBERON_CODE.md) - Required when TREATMENT_TYPE is a surgical or radiation therapy
     * [Therapy➞THERAPY_ANATOMIC_SITE_UBERON_CODE](Therapy_THERAPY_ANATOMIC_SITE_UBERON_CODE.md)
 * [TISSUE_OR_ORGAN_OF_ORIGIN](TISSUE_OR_ORGAN_OF_ORIGIN.md) - The tissue or organ of origin for the primary diagnosis, using UBERON codes
 * [YEARS_SMOKED](YEARS_SMOKED.md) - Required when SMOKING_HISTORY is Current smoker or Former smoker
     * [Exposure➞YEARS_SMOKED](Exposure_YEARS_SMOKED.md)
 * [caDSR_id](caDSR_id.md) - The caDSR identifier for this element
 * [➞DEMOGRAPHICS](clinicalData__DEMOGRAPHICS.md) - Demographic information
 * [➞DIAGNOSIS](clinicalData__DIAGNOSIS.md) - Primary diagnosis information
 * [➞EXPOSURES](clinicalData__EXPOSURES.md) - Exposure history
 * [➞FAMILY_HISTORY](clinicalData__FAMILY_HISTORY.md) - Family history of cancer
 * [➞FOLLOW_UPS](clinicalData__FOLLOW_UPS.md) - Follow-up observations
 * [➞MOLECULAR_TESTS](clinicalData__MOLECULAR_TESTS.md) - Molecular test results
 * [➞THERAPIES](clinicalData__THERAPIES.md) - Therapy information
 * [➞VITAL_STATUS](clinicalData__VITAL_STATUS.md) - Vital status information
 * [➞COMPONENT](coreFileAttributes__COMPONENT.md) - Category of metadata (e.g., Bulk WES Level 1, scRNA-seq Level 2, etc.)
 * [➞FILENAME](coreFileAttributes__FILENAME.md) - Name of the file
 * [➞FILE_FORMAT](coreFileAttributes__FILE_FORMAT.md) - Format of the file (e.g., fastq, bam, vcf, h5ad)
 * [➞HTAN_DATA_FILE_ID](coreFileAttributes__HTAN_DATA_FILE_ID.md) - HTAN Data File ID (Primary Key)
 * [➞HTAN_PARENT_ID](coreFileAttributes__HTAN_PARENT_ID.md) - HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
 * [➞ETHNIC_GROUP](demographics__ETHNIC_GROUP.md) - Ethnic group of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
 * [➞GENDER_IDENTITY](demographics__GENDER_IDENTITY.md) - Gender identity of the participant (caDSR:2192202) (Aligns to CDRC Standard CDE)
 * [➞RACE](demographics__RACE.md) - Race of the participant (caDSR:2192204) (Aligns to CDRC Standard CDE)
 * [➞SEX](demographics__SEX.md) - Sex of the participant (caDSR:2192203) (Aligns to CDRC Standard CDE)
 * [➞AGE_IN_DAYS_AT_DIAGNOSIS](diagnosis__AGE_IN_DAYS_AT_DIAGNOSIS.md) - Age in days at which the diagnosis was made (caDSR:2192202) (Aligns to CDRC Standard CDE)
 * [➞AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS](diagnosis__AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS.md) - Age in days at which the last known disease status was recorded (caDSR:2192203) (Aligns to CDRC Standard CDE)
 * [➞AJCC_STAGING_SYSTEM_EDITION](diagnosis__AJCC_STAGING_SYSTEM_EDITION.md) - Edition of AJCC staging system used (caDSR:2192209) (Aligns to CDRC Standard CDE)
 * [➞CLINICAL_M_STAGE](diagnosis__CLINICAL_M_STAGE.md) - Clinical M stage of the tumor (caDSR:2192208) (Aligns to CDRC Standard CDE)
 * [➞CLINICAL_N_STAGE](diagnosis__CLINICAL_N_STAGE.md) - Clinical N stage of the tumor (caDSR:2192207) (Aligns to CDRC Standard CDE)
 * [➞CLINICAL_T_STAGE](diagnosis__CLINICAL_T_STAGE.md) - Clinical T stage of the tumor (caDSR:2192206) (Aligns to CDRC Standard CDE)
 * [➞LAST_KNOWN_DISEASE_STATUS](diagnosis__LAST_KNOWN_DISEASE_STATUS.md) - Last known disease status (caDSR:2192210) (Aligns to CDRC Standard CDE)
 * [➞METASTASIS_AT_DIAGNOSIS](diagnosis__METASTASIS_AT_DIAGNOSIS.md) - Presence of metastasis at diagnosis (caDSR:2192212) (Aligns to CDRC Standard CDE)
 * [➞METHOD_OF_DIAGNOSIS](diagnosis__METHOD_OF_DIAGNOSIS.md) - Method used to make the diagnosis (caDSR:2192213) (Aligns to CDRC Standard CDE)
 * [➞PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID](diagnosis__PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID.md) - NCI Thesaurus ID for the primary diagnosis (caDSR:2192201) (Aligns to CDRC Standard CDE)
 * [➞TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE](diagnosis__TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE.md) - UBERON code for the tissue or organ of origin (caDSR:2192205) (Aligns to CDRC Standard CDE)
 * [➞TUMOR_CLASSIFICATION_CATEGORY](diagnosis__TUMOR_CLASSIFICATION_CATEGORY.md) - Classification category of the tumor (caDSR:2192211) (Aligns to CDRC Standard CDE)
 * [➞TUMOR_GRADE](diagnosis__TUMOR_GRADE.md) - The grade of the tumor (caDSR:2192203) (Aligns to CDRC Standard CDE)
 * [➞ALCOHOL_HISTORY_INDICATOR](exposure__ALCOHOL_HISTORY_INDICATOR.md) - Alcohol history indicator of the participant (caDSR:2192204) (Aligns to CDRC Standard CDE)
 * [➞ENVIRONMENTAL_EXPOSURE](exposure__ENVIRONMENTAL_EXPOSURE.md) - Environmental exposure of the participant (caDSR:2192205) (Aligns to CDRC Standard CDE)
 * [➞ENVIRONMENTAL_EXPOSURE_TYPE](exposure__ENVIRONMENTAL_EXPOSURE_TYPE.md) - Type of environmental exposure (caDSR:2192206) (Aligns to CDRC Standard CDE)
 * [➞PACK_YEARS_SMOKED](exposure__PACK_YEARS_SMOKED.md) - Number of pack years the participant has smoked (caDSR:2192203) (Aligns to CDRC Standard CDE)
 * [➞SMOKING_HISTORY](exposure__SMOKING_HISTORY.md) - Smoking history of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
 * [➞YEARS_SMOKED](exposure__YEARS_SMOKED.md) - Number of years the participant has smoked (caDSR:2192202) (Aligns to CDRC Standard CDE)
 * [extension➞tag](extension_tag.md) - a tag associated with an extension
 * [extension➞value](extension_value.md) - the actual annotation
 * [extensions](extensions.md) - a tag/text tuple attached to an arbitrary element
 * [➞FAMILY_MEMBER_CANCER_HISTORY](familyHistory__FAMILY_MEMBER_CANCER_HISTORY.md) - Has a family member been diagnosed with cancer?
 * [➞RELATIVES_WITH_CANCER_HISTORY](familyHistory__RELATIVES_WITH_CANCER_HISTORY.md) - Number of first degree relatives with cancer history
 * [➞AGE_IN_DAYS_AT_FOLLOWUP](followUp__AGE_IN_DAYS_AT_FOLLOWUP.md) - Age in days at follow-up
 * [➞AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE](followUp__AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE.md) - Age in days at progression or recurrence
 * [➞DISEASE_RESPONSE](followUp__DISEASE_RESPONSE.md) - Response to treatment
 * [➞ECOG_PERFORMANCE_STATUS](followUp__ECOG_PERFORMANCE_STATUS.md) - ECOG performance status
 * [➞EVIDENCE_OF_RECURRENCE_TYPE](followUp__EVIDENCE_OF_RECURRENCE_TYPE.md) - Type of evidence for recurrence
 * [➞MENOPAUSE_STATUS](followUp__MENOPAUSE_STATUS.md) - Menopause status
 * [➞PROGRESSION_OR_RECURRENCE](followUp__PROGRESSION_OR_RECURRENCE.md) - Indicates whether the disease has progressed or recurred
 * [➞PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE](followUp__PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE.md) - UBERON code for the anatomic site of progression or recurrence
 * [➞PROGRESSION_OR_RECURRENCE_TYPE](followUp__PROGRESSION_OR_RECURRENCE_TYPE.md) - Type of progression or recurrence
 * [➞AA_CHANGE](molecularTest__AA_CHANGE.md) - Amino acid change (caDSR:2192207) (Aligns to CDRC Standard CDE)
 * [➞AGE_IN_DAYS_AT_MOLECULAR_TEST_START](molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_START.md) - Age in days at molecular test start (caDSR:2192202) (Aligns to CDRC Standard CDE)
 * [➞AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP](molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP.md) - Age in days at molecular test stop (caDSR:2192203) (Aligns to CDRC Standard CDE)
 * [➞CLINICAL_BIOSPECIMEN_TYPE](molecularTest__CLINICAL_BIOSPECIMEN_TYPE.md) - Clinical biospecimen type (caDSR:2192208) (Aligns to CDRC Standard CDE)
 * [➞COPY_NUMBER](molecularTest__COPY_NUMBER.md) - Copy number (caDSR:2192209) (Aligns to CDRC Standard CDE)
 * [➞EXON](molecularTest__EXON.md) - Exon number (caDSR:2192210) (Aligns to CDRC Standard CDE)
 * [➞GENE_SYMBOL](molecularTest__GENE_SYMBOL.md) - Gene symbol (caDSR:2192204) (Aligns to CDRC Standard CDE)
 * [➞MOLECULAR_ANALYSIS_METHOD](molecularTest__MOLECULAR_ANALYSIS_METHOD.md) - Molecular analysis method (caDSR:2192205) (Aligns to CDRC Standard CDE)
 * [➞MOLECULAR_ANALYSIS_RESULT](molecularTest__MOLECULAR_ANALYSIS_RESULT.md) - Molecular analysis result (caDSR:2192206) (Aligns to CDRC Standard CDE)
 * [➞MOLECULAR_CONSEQUENCE](molecularTest__MOLECULAR_CONSEQUENCE.md) - Molecular consequence (caDSR:2192211) (Aligns to CDRC Standard CDE)
 * [➞PATHOGENICITY](molecularTest__PATHOGENICITY.md) - Pathogenicity (caDSR:2192212) (Aligns to CDRC Standard CDE)
 * [➞TEST_ANALYTE_TYPE](molecularTest__TEST_ANALYTE_TYPE.md) - Test analyte type (caDSR:2192213) (Aligns to CDRC Standard CDE)
 * [➞TEST_RESULT](molecularTest__TEST_RESULT.md) - Test result (caDSR:2192215) (Aligns to CDRC Standard CDE)
 * [➞TEST_UNITS](molecularTest__TEST_UNITS.md) - Test units (caDSR:2192214) (Aligns to CDRC Standard CDE)
 * [➞TIMEPOINT_LABEL](molecularTest__TIMEPOINT_LABEL.md) - Label for the timepoint (caDSR:2192201) (Aligns to CDRC Standard CDE)
 * [➞VARIANT_ORIGIN](molecularTest__VARIANT_ORIGIN.md) - Variant origin (caDSR:2192216) (Aligns to CDRC Standard CDE)
 * [➞VARIANT_TYPE](molecularTest__VARIANT_TYPE.md) - Variant type (caDSR:2192217) (Aligns to CDRC Standard CDE)
 * [➞AGE_IN_DAYS_AT_TREATMENT_END](therapy__AGE_IN_DAYS_AT_TREATMENT_END.md) - The age in days of the subject at the time that this treatment was completed
 * [➞AGE_IN_DAYS_AT_TREATMENT_START](therapy__AGE_IN_DAYS_AT_TREATMENT_START.md) - The age in days of the subject at the time that this treatment was started
 * [➞INITIAL_DISEASE_STATUS](therapy__INITIAL_DISEASE_STATUS.md) - Status of the individual's malignancy when the treatment began
 * [➞NUMBER_OF_CYCLES](therapy__NUMBER_OF_CYCLES.md) - Number of treatment cycles administered
 * [➞OFF_TREATMENT_REASON](therapy__OFF_TREATMENT_REASON.md) - Reason for stopping treatment
 * [➞PHARMACOTHERAPY_TYPE](therapy__PHARMACOTHERAPY_TYPE.md) - Whether single or combination pharmacotherapy was used
 * [➞REGIMEN_OR_LINE_OF_THERAPY](therapy__REGIMEN_OR_LINE_OF_THERAPY.md) - Line of therapy
 * [➞RESPONSE](therapy__RESPONSE.md) - Response to treatment
 * [➞THERAPEUTIC_AGENTS](therapy__THERAPEUTIC_AGENTS.md) - The NCit Preferred Name(s) of the Therapeutic agent(s)
 * [➞THERAPY_ANATOMIC_SITE_UBERON_CODE](therapy__THERAPY_ANATOMIC_SITE_UBERON_CODE.md) - UBERON identifier for the location within the body targeted by a therapeutic procedure
 * [➞TREATMENT_INTENT_TYPE](therapy__TREATMENT_INTENT_TYPE.md) - Anticipated outcome for therapy
 * [➞TREATMENT_TYPE](therapy__TREATMENT_TYPE.md) - Type of treatment administered
 * [➞AGE_IN_DAYS_AT_DEATH](vitalStatus__AGE_IN_DAYS_AT_DEATH.md) - Age in days at death (caDSR:2192202) (Aligns to CDRC Standard CDE)
 * [➞CAUSE_OF_DEATH](vitalStatus__CAUSE_OF_DEATH.md) - Cause of death (caDSR:2192203) (Aligns to CDRC Standard CDE)
 * [➞CAUSE_OF_DEATH_SOURCE](vitalStatus__CAUSE_OF_DEATH_SOURCE.md) - Source of cause of death (caDSR:2192204) (Aligns to CDRC Standard CDE)
 * [➞VITAL_STATUS](vitalStatus__VITAL_STATUS.md) - Vital status of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)

### Enums

 * [AJCCStagingSystemEditionEnum](AJCCStagingSystemEditionEnum.md)
 * [AlcoholHistoryIndicatorEnum](AlcoholHistoryIndicatorEnum.md)
 * [CauseOfDeathEnum](CauseOfDeathEnum.md)
 * [CauseOfDeathSourceEnum](CauseOfDeathSourceEnum.md)
 * [ClinicalBiospecimenTypeEnum](ClinicalBiospecimenTypeEnum.md)
 * [ClinicalMStageEnum](ClinicalMStageEnum.md)
 * [ClinicalNStageEnum](ClinicalNStageEnum.md)
 * [ClinicalTStageEnum](ClinicalTStageEnum.md)
 * [ComponentEnum](ComponentEnum.md)
 * [DiseaseResponseEnum](DiseaseResponseEnum.md)
 * [ECOGPerformanceStatusEnum](ECOGPerformanceStatusEnum.md)
 * [EnvironmentalExposureEnum](EnvironmentalExposureEnum.md)
 * [EnvironmentalExposureTypeEnum](EnvironmentalExposureTypeEnum.md)
 * [EthnicGroupEnum](EthnicGroupEnum.md)
 * [EvidenceOfRecurrenceTypeEnum](EvidenceOfRecurrenceTypeEnum.md)
 * [FamilyMemberCancerHistoryEnum](FamilyMemberCancerHistoryEnum.md)
 * [GenderIdentityEnum](GenderIdentityEnum.md)
 * [LastKnownDiseaseStatusEnum](LastKnownDiseaseStatusEnum.md)
 * [MenopauseStatusEnum](MenopauseStatusEnum.md)
 * [MetastasisAtDiagnosisEnum](MetastasisAtDiagnosisEnum.md)
 * [MethodOfDiagnosisEnum](MethodOfDiagnosisEnum.md)
 * [MolecularAnalysisMethodEnum](MolecularAnalysisMethodEnum.md)
 * [MolecularConsequenceEnum](MolecularConsequenceEnum.md)
 * [OffTreatmentReasonEnum](OffTreatmentReasonEnum.md)
 * [PathogenicityEnum](PathogenicityEnum.md)
 * [PharmacotherapyTypeEnum](PharmacotherapyTypeEnum.md)
 * [ProgressionOrRecurrenceEnum](ProgressionOrRecurrenceEnum.md)
 * [ProgressionTypeEnum](ProgressionTypeEnum.md)
 * [RaceEnum](RaceEnum.md)
 * [RegimenOrLineOfTherapyEnum](RegimenOrLineOfTherapyEnum.md)
 * [SexEnum](SexEnum.md)
 * [SmokingHistoryEnum](SmokingHistoryEnum.md)
 * [TestAnalyteTypeEnum](TestAnalyteTypeEnum.md)
 * [TreatmentIntentTypeEnum](TreatmentIntentTypeEnum.md)
 * [TreatmentTypeEnum](TreatmentTypeEnum.md)
 * [TumorClassificationCategoryEnum](TumorClassificationCategoryEnum.md)
 * [TumorGradeEnum](TumorGradeEnum.md)
 * [TumorStageEnum](TumorStageEnum.md)
 * [VariantOriginEnum](VariantOriginEnum.md)
 * [VariantTypeEnum](VariantTypeEnum.md)
 * [VitalStatusEnum](VitalStatusEnum.md)
 * [YesNoUnknownNotReportedEnum](YesNoUnknownNotReportedEnum.md)
 * [antineoplastic_agent_enum](antineoplastic_agent_enum.md)
 * [gene_symbol_enum](gene_symbol_enum.md) - Valid gene symbols from HGNC database
 * [tissue_or_organ_of_origin_uberon_enum](tissue_or_organ_of_origin_uberon_enum.md) - UBERON codes for tissues and organs of origin

### Subsets


### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Jsonpath](types/Jsonpath.md)  (**str**)  - A string encoding a JSON Path. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded in tree form.
 * [Jsonpointer](types/Jsonpointer.md)  (**str**)  - A string encoding a JSON Pointer. The value of the string MUST conform to JSON Point syntax and SHOULD dereference to a valid object within the current instance document when encoded in tree form.
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [Sparqlpath](types/Sparqlpath.md)  (**str**)  - A string encoding a SPARQL Property Path. The value of the string MUST conform to SPARQL syntax and SHOULD dereference to zero or more valid objects within the current instance document when encoded as RDF.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
