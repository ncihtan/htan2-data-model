
# Class: VitalStatus

Information about the vital status

URI: [htan:VitalStatus](https://w3id.org/htan/VitalStatus)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20VITAL_STATUS%201..1>[VitalStatus&#124;VITAL_STATUS:VitalStatusEnum;AGE_IN_DAYS_AT_DEATH:integer%20%3F;CAUSE_OF_DEATH:CauseOfDeathEnum%20%3F;CAUSE_OF_DEATH_SOURCE:CauseOfDeathSourceEnum%20%3F],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20VITAL_STATUS%201..1>[VitalStatus&#124;VITAL_STATUS:VitalStatusEnum;AGE_IN_DAYS_AT_DEATH:integer%20%3F;CAUSE_OF_DEATH:CauseOfDeathEnum%20%3F;CAUSE_OF_DEATH_SOURCE:CauseOfDeathSourceEnum%20%3F],[ClinicalData])

## Referenced by Class

 *  **None** *[➞VITAL_STATUS](clinicalData__VITAL_STATUS.md)*  <sub>1..1</sub>  **[VitalStatus](VitalStatus.md)**

## Attributes


### Own

 * [➞VITAL_STATUS](vitalStatus__VITAL_STATUS.md)  <sub>1..1</sub>
     * Description: Vital status of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
     * Range: [VitalStatusEnum](VitalStatusEnum.md)
 * [➞AGE_IN_DAYS_AT_DEATH](vitalStatus__AGE_IN_DAYS_AT_DEATH.md)  <sub>0..1</sub>
     * Description: Age in days at death (caDSR:2192202) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞CAUSE_OF_DEATH](vitalStatus__CAUSE_OF_DEATH.md)  <sub>0..1</sub>
     * Description: Cause of death (caDSR:2192203) (Aligns to CDRC Standard CDE)
     * Range: [CauseOfDeathEnum](CauseOfDeathEnum.md)
 * [➞CAUSE_OF_DEATH_SOURCE](vitalStatus__CAUSE_OF_DEATH_SOURCE.md)  <sub>0..1</sub>
     * Description: Source of cause of death (caDSR:2192204) (Aligns to CDRC Standard CDE)
     * Range: [CauseOfDeathSourceEnum](CauseOfDeathSourceEnum.md)
 * [VitalStatus➞AGE_IN_DAYS_AT_DEATH](VitalStatus_AGE_IN_DAYS_AT_DEATH.md)  <sub>0..1</sub>
     * Description: Required when VITAL_STATUS is Deceased
     * Range: [String](types/String.md)
 * [VitalStatus➞CAUSE_OF_DEATH](VitalStatus_CAUSE_OF_DEATH.md)  <sub>0..1</sub>
     * Description: Required when VITAL_STATUS is Deceased
     * Range: [String](types/String.md)
 * [VitalStatus➞CAUSE_OF_DEATH_SOURCE](VitalStatus_CAUSE_OF_DEATH_SOURCE.md)  <sub>0..1</sub>
     * Description: Required when VITAL_STATUS is Deceased
     * Range: [String](types/String.md)
