
# Class: FamilyHistory

A class to capture information about the cancer history of family members.

URI: [htan:FamilyHistory](https://w3id.org/htan/FamilyHistory)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20FAMILY_HISTORY%201..1>[FamilyHistory&#124;FAMILY_MEMBER_CANCER_HISTORY:YesNoUnknownNotReportedEnum%20%3F;RELATIVES_WITH_CANCER_HISTORY:integer%20%3F],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20FAMILY_HISTORY%201..1>[FamilyHistory&#124;FAMILY_MEMBER_CANCER_HISTORY:YesNoUnknownNotReportedEnum%20%3F;RELATIVES_WITH_CANCER_HISTORY:integer%20%3F],[ClinicalData])

## Referenced by Class

 *  **None** *[➞FAMILY_HISTORY](clinicalData__FAMILY_HISTORY.md)*  <sub>1..1</sub>  **[FamilyHistory](FamilyHistory.md)**

## Attributes


### Own

 * [➞FAMILY_MEMBER_CANCER_HISTORY](familyHistory__FAMILY_MEMBER_CANCER_HISTORY.md)  <sub>0..1</sub>
     * Description: Has a family member been diagnosed with cancer?
     * Range: [YesNoUnknownNotReportedEnum](YesNoUnknownNotReportedEnum.md)
 * [➞RELATIVES_WITH_CANCER_HISTORY](familyHistory__RELATIVES_WITH_CANCER_HISTORY.md)  <sub>0..1</sub>
     * Description: Number of first degree relatives with cancer history
     * Range: [Integer](types/Integer.md)
