
# Class: FollowUp

Clinical follow-up information

URI: [htan:FollowUp](https://w3id.org/htan/FollowUp)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20FOLLOW_UPS%200..*>[FollowUp&#124;AGE_IN_DAYS_AT_FOLLOWUP:integer;PROGRESSION_OR_RECURRENCE:ProgressionOrRecurrenceEnum;PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE:tissue_or_organ_of_origin_uberon_enum%20%3F;PROGRESSION_OR_RECURRENCE_TYPE:ProgressionTypeEnum%20%3F;EVIDENCE_OF_RECURRENCE_TYPE:EvidenceOfRecurrenceTypeEnum%20%3F;AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE:integer%20%3F;DISEASE_RESPONSE:DiseaseResponseEnum;ECOG_PERFORMANCE_STATUS:ECOGPerformanceStatusEnum;MENOPAUSE_STATUS:MenopauseStatusEnum%20%3F],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20FOLLOW_UPS%200..*>[FollowUp&#124;AGE_IN_DAYS_AT_FOLLOWUP:integer;PROGRESSION_OR_RECURRENCE:ProgressionOrRecurrenceEnum;PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE:tissue_or_organ_of_origin_uberon_enum%20%3F;PROGRESSION_OR_RECURRENCE_TYPE:ProgressionTypeEnum%20%3F;EVIDENCE_OF_RECURRENCE_TYPE:EvidenceOfRecurrenceTypeEnum%20%3F;AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE:integer%20%3F;DISEASE_RESPONSE:DiseaseResponseEnum;ECOG_PERFORMANCE_STATUS:ECOGPerformanceStatusEnum;MENOPAUSE_STATUS:MenopauseStatusEnum%20%3F],[ClinicalData])

## Referenced by Class

 *  **None** *[➞FOLLOW_UPS](clinicalData__FOLLOW_UPS.md)*  <sub>0..\*</sub>  **[FollowUp](FollowUp.md)**

## Attributes


### Own

 * [➞AGE_IN_DAYS_AT_FOLLOWUP](followUp__AGE_IN_DAYS_AT_FOLLOWUP.md)  <sub>1..1</sub>
     * Description: Age in days at follow-up
     * Range: [Integer](types/Integer.md)
 * [➞PROGRESSION_OR_RECURRENCE](followUp__PROGRESSION_OR_RECURRENCE.md)  <sub>1..1</sub>
     * Description: Indicates whether the disease has progressed or recurred
     * Range: [ProgressionOrRecurrenceEnum](ProgressionOrRecurrenceEnum.md)
 * [➞PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE](followUp__PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE.md)  <sub>0..1</sub>
     * Description: UBERON code for the anatomic site of progression or recurrence
     * Range: [tissue_or_organ_of_origin_uberon_enum](tissue_or_organ_of_origin_uberon_enum.md)
 * [➞PROGRESSION_OR_RECURRENCE_TYPE](followUp__PROGRESSION_OR_RECURRENCE_TYPE.md)  <sub>0..1</sub>
     * Description: Type of progression or recurrence
     * Range: [ProgressionTypeEnum](ProgressionTypeEnum.md)
 * [➞EVIDENCE_OF_RECURRENCE_TYPE](followUp__EVIDENCE_OF_RECURRENCE_TYPE.md)  <sub>0..1</sub>
     * Description: Type of evidence for recurrence
     * Range: [EvidenceOfRecurrenceTypeEnum](EvidenceOfRecurrenceTypeEnum.md)
 * [➞AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE](followUp__AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE.md)  <sub>0..1</sub>
     * Description: Age in days at progression or recurrence
     * Range: [Integer](types/Integer.md)
 * [➞DISEASE_RESPONSE](followUp__DISEASE_RESPONSE.md)  <sub>1..1</sub>
     * Description: Response to treatment
     * Range: [DiseaseResponseEnum](DiseaseResponseEnum.md)
 * [➞ECOG_PERFORMANCE_STATUS](followUp__ECOG_PERFORMANCE_STATUS.md)  <sub>1..1</sub>
     * Description: ECOG performance status
     * Range: [ECOGPerformanceStatusEnum](ECOGPerformanceStatusEnum.md)
 * [➞MENOPAUSE_STATUS](followUp__MENOPAUSE_STATUS.md)  <sub>0..1</sub>
     * Description: Menopause status
     * Range: [MenopauseStatusEnum](MenopauseStatusEnum.md)
 * [FollowUp➞PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE](FollowUp_PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE.md)  <sub>0..1</sub>
     * Description: Required when PROGRESSION_OR_RECURRENCE is Yes
     * Range: [String](types/String.md)
 * [FollowUp➞PROGRESSION_OR_RECURRENCE_TYPE](FollowUp_PROGRESSION_OR_RECURRENCE_TYPE.md)  <sub>0..1</sub>
     * Description: Required when PROGRESSION_OR_RECURRENCE is Yes
     * Range: [String](types/String.md)
 * [FollowUp➞EVIDENCE_OF_RECURRENCE_TYPE](FollowUp_EVIDENCE_OF_RECURRENCE_TYPE.md)  <sub>0..1</sub>
     * Description: Required when PROGRESSION_OR_RECURRENCE is Yes
     * Range: [String](types/String.md)
 * [FollowUp➞AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE](FollowUp_AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE.md)  <sub>0..1</sub>
     * Description: Required when PROGRESSION_OR_RECURRENCE is Yes
     * Range: [String](types/String.md)
