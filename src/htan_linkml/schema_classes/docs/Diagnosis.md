
# Class: Diagnosis

Information about the diagnosis

URI: [htan:Diagnosis](https://w3id.org/htan/Diagnosis)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20DIAGNOSIS%201..1>[Diagnosis&#124;PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID:string;AGE_IN_DAYS_AT_DIAGNOSIS:integer;TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE:tissue_or_organ_of_origin_uberon_enum;TUMOR_GRADE:TumorGradeEnum;CLINICAL_T_STAGE:ClinicalTStageEnum;CLINICAL_N_STAGE:ClinicalNStageEnum;CLINICAL_M_STAGE:ClinicalMStageEnum;AJCC_STAGING_SYSTEM_EDITION:AJCCStagingSystemEditionEnum;AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS:integer;LAST_KNOWN_DISEASE_STATUS:LastKnownDiseaseStatusEnum;TUMOR_CLASSIFICATION_CATEGORY:TumorClassificationCategoryEnum;METASTASIS_AT_DIAGNOSIS:MetastasisAtDiagnosisEnum;METHOD_OF_DIAGNOSIS:MethodOfDiagnosisEnum],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20DIAGNOSIS%201..1>[Diagnosis&#124;PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID:string;AGE_IN_DAYS_AT_DIAGNOSIS:integer;TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE:tissue_or_organ_of_origin_uberon_enum;TUMOR_GRADE:TumorGradeEnum;CLINICAL_T_STAGE:ClinicalTStageEnum;CLINICAL_N_STAGE:ClinicalNStageEnum;CLINICAL_M_STAGE:ClinicalMStageEnum;AJCC_STAGING_SYSTEM_EDITION:AJCCStagingSystemEditionEnum;AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS:integer;LAST_KNOWN_DISEASE_STATUS:LastKnownDiseaseStatusEnum;TUMOR_CLASSIFICATION_CATEGORY:TumorClassificationCategoryEnum;METASTASIS_AT_DIAGNOSIS:MetastasisAtDiagnosisEnum;METHOD_OF_DIAGNOSIS:MethodOfDiagnosisEnum],[ClinicalData])

## Referenced by Class

 *  **None** *[➞DIAGNOSIS](clinicalData__DIAGNOSIS.md)*  <sub>1..1</sub>  **[Diagnosis](Diagnosis.md)**

## Attributes


### Own

 * [➞PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID](diagnosis__PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID.md)  <sub>1..1</sub>
     * Description: NCI Thesaurus ID for the primary diagnosis (caDSR:2192201) (Aligns to CDRC Standard CDE)
     * Range: [String](types/String.md)
 * [➞AGE_IN_DAYS_AT_DIAGNOSIS](diagnosis__AGE_IN_DAYS_AT_DIAGNOSIS.md)  <sub>1..1</sub>
     * Description: Age in days at which the diagnosis was made (caDSR:2192202) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE](diagnosis__TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE.md)  <sub>1..1</sub>
     * Description: UBERON code for the tissue or organ of origin (caDSR:2192205) (Aligns to CDRC Standard CDE)
     * Range: [tissue_or_organ_of_origin_uberon_enum](tissue_or_organ_of_origin_uberon_enum.md)
 * [➞TUMOR_GRADE](diagnosis__TUMOR_GRADE.md)  <sub>1..1</sub>
     * Description: The grade of the tumor (caDSR:2192203) (Aligns to CDRC Standard CDE)
     * Range: [TumorGradeEnum](TumorGradeEnum.md)
 * [➞CLINICAL_T_STAGE](diagnosis__CLINICAL_T_STAGE.md)  <sub>1..1</sub>
     * Description: Clinical T stage of the tumor (caDSR:2192206) (Aligns to CDRC Standard CDE)
     * Range: [ClinicalTStageEnum](ClinicalTStageEnum.md)
 * [➞CLINICAL_N_STAGE](diagnosis__CLINICAL_N_STAGE.md)  <sub>1..1</sub>
     * Description: Clinical N stage of the tumor (caDSR:2192207) (Aligns to CDRC Standard CDE)
     * Range: [ClinicalNStageEnum](ClinicalNStageEnum.md)
 * [➞CLINICAL_M_STAGE](diagnosis__CLINICAL_M_STAGE.md)  <sub>1..1</sub>
     * Description: Clinical M stage of the tumor (caDSR:2192208) (Aligns to CDRC Standard CDE)
     * Range: [ClinicalMStageEnum](ClinicalMStageEnum.md)
 * [➞AJCC_STAGING_SYSTEM_EDITION](diagnosis__AJCC_STAGING_SYSTEM_EDITION.md)  <sub>1..1</sub>
     * Description: Edition of AJCC staging system used (caDSR:2192209) (Aligns to CDRC Standard CDE)
     * Range: [AJCCStagingSystemEditionEnum](AJCCStagingSystemEditionEnum.md)
 * [➞AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS](diagnosis__AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS.md)  <sub>1..1</sub>
     * Description: Age in days at which the last known disease status was recorded (caDSR:2192203) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞LAST_KNOWN_DISEASE_STATUS](diagnosis__LAST_KNOWN_DISEASE_STATUS.md)  <sub>1..1</sub>
     * Description: Last known disease status (caDSR:2192210) (Aligns to CDRC Standard CDE)
     * Range: [LastKnownDiseaseStatusEnum](LastKnownDiseaseStatusEnum.md)
 * [➞TUMOR_CLASSIFICATION_CATEGORY](diagnosis__TUMOR_CLASSIFICATION_CATEGORY.md)  <sub>1..1</sub>
     * Description: Classification category of the tumor (caDSR:2192211) (Aligns to CDRC Standard CDE)
     * Range: [TumorClassificationCategoryEnum](TumorClassificationCategoryEnum.md)
 * [➞METASTASIS_AT_DIAGNOSIS](diagnosis__METASTASIS_AT_DIAGNOSIS.md)  <sub>1..1</sub>
     * Description: Presence of metastasis at diagnosis (caDSR:2192212) (Aligns to CDRC Standard CDE)
     * Range: [MetastasisAtDiagnosisEnum](MetastasisAtDiagnosisEnum.md)
 * [➞METHOD_OF_DIAGNOSIS](diagnosis__METHOD_OF_DIAGNOSIS.md)  <sub>1..1</sub>
     * Description: Method used to make the diagnosis (caDSR:2192213) (Aligns to CDRC Standard CDE)
     * Range: [MethodOfDiagnosisEnum](MethodOfDiagnosisEnum.md)
 * [Diagnosis➞CLINICAL_T_STAGE](Diagnosis_CLINICAL_T_STAGE.md)  <sub>0..1</sub>
     * Description: Required when TUMOR_STAGE is any stage value
     * Range: [String](types/String.md)
 * [Diagnosis➞CLINICAL_N_STAGE](Diagnosis_CLINICAL_N_STAGE.md)  <sub>0..1</sub>
     * Description: Required when TUMOR_STAGE is any stage value
     * Range: [String](types/String.md)
 * [Diagnosis➞CLINICAL_M_STAGE](Diagnosis_CLINICAL_M_STAGE.md)  <sub>0..1</sub>
     * Description: Required when TUMOR_STAGE is any stage value
     * Range: [String](types/String.md)
 * [Diagnosis➞AJCC_STAGING_SYSTEM_EDITION](Diagnosis_AJCC_STAGING_SYSTEM_EDITION.md)  <sub>0..1</sub>
     * Description: Required when TUMOR_STAGE is any stage value
     * Range: [String](types/String.md)
 * [Diagnosis➞METASTASIS_AT_DIAGNOSIS](Diagnosis_METASTASIS_AT_DIAGNOSIS.md)  <sub>0..1</sub>
     * Description: Required when TUMOR_STAGE is Stage IV or any of its substages
     * Range: [String](types/String.md)
