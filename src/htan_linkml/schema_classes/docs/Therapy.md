
# Class: Therapy

Information about therapeutic interventions

URI: [htan:Therapy](https://w3id.org/htan/Therapy)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20THERAPIES%200..*>[Therapy&#124;INITIAL_DISEASE_STATUS:string;TREATMENT_INTENT_TYPE:TreatmentIntentTypeEnum;TREATMENT_TYPE:TreatmentTypeEnum%20%2B;PHARMACOTHERAPY_TYPE:PharmacotherapyTypeEnum;THERAPEUTIC_AGENTS:antineoplastic_agent_enum%20%2B;THERAPY_ANATOMIC_SITE_UBERON_CODE:tissue_or_organ_of_origin_uberon_enum%20%3F;AGE_IN_DAYS_AT_TREATMENT_START:integer;AGE_IN_DAYS_AT_TREATMENT_END:integer;OFF_TREATMENT_REASON:OffTreatmentReasonEnum%20%3F;REGIMEN_OR_LINE_OF_THERAPY:RegimenOrLineOfTherapyEnum%20%3F;NUMBER_OF_CYCLES:integer%20%3F;RESPONSE:string%20%3F],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20THERAPIES%200..*>[Therapy&#124;INITIAL_DISEASE_STATUS:string;TREATMENT_INTENT_TYPE:TreatmentIntentTypeEnum;TREATMENT_TYPE:TreatmentTypeEnum%20%2B;PHARMACOTHERAPY_TYPE:PharmacotherapyTypeEnum;THERAPEUTIC_AGENTS:antineoplastic_agent_enum%20%2B;THERAPY_ANATOMIC_SITE_UBERON_CODE:tissue_or_organ_of_origin_uberon_enum%20%3F;AGE_IN_DAYS_AT_TREATMENT_START:integer;AGE_IN_DAYS_AT_TREATMENT_END:integer;OFF_TREATMENT_REASON:OffTreatmentReasonEnum%20%3F;REGIMEN_OR_LINE_OF_THERAPY:RegimenOrLineOfTherapyEnum%20%3F;NUMBER_OF_CYCLES:integer%20%3F;RESPONSE:string%20%3F],[ClinicalData])

## Referenced by Class

 *  **None** *[➞THERAPIES](clinicalData__THERAPIES.md)*  <sub>0..\*</sub>  **[Therapy](Therapy.md)**

## Attributes


### Own

 * [➞INITIAL_DISEASE_STATUS](therapy__INITIAL_DISEASE_STATUS.md)  <sub>1..1</sub>
     * Description: Status of the individual's malignancy when the treatment began
     * Range: [String](types/String.md)
 * [➞TREATMENT_INTENT_TYPE](therapy__TREATMENT_INTENT_TYPE.md)  <sub>1..1</sub>
     * Description: Anticipated outcome for therapy
     * Range: [TreatmentIntentTypeEnum](TreatmentIntentTypeEnum.md)
 * [➞TREATMENT_TYPE](therapy__TREATMENT_TYPE.md)  <sub>1..\*</sub>
     * Description: Type of treatment administered
     * Range: [TreatmentTypeEnum](TreatmentTypeEnum.md)
 * [➞PHARMACOTHERAPY_TYPE](therapy__PHARMACOTHERAPY_TYPE.md)  <sub>1..1</sub>
     * Description: Whether single or combination pharmacotherapy was used
     * Range: [PharmacotherapyTypeEnum](PharmacotherapyTypeEnum.md)
 * [➞THERAPEUTIC_AGENTS](therapy__THERAPEUTIC_AGENTS.md)  <sub>1..\*</sub>
     * Description: The NCit Preferred Name(s) of the Therapeutic agent(s)
     * Range: [antineoplastic_agent_enum](antineoplastic_agent_enum.md)
 * [➞THERAPY_ANATOMIC_SITE_UBERON_CODE](therapy__THERAPY_ANATOMIC_SITE_UBERON_CODE.md)  <sub>0..1</sub>
     * Description: UBERON identifier for the location within the body targeted by a therapeutic procedure
     * Range: [tissue_or_organ_of_origin_uberon_enum](tissue_or_organ_of_origin_uberon_enum.md)
 * [➞AGE_IN_DAYS_AT_TREATMENT_START](therapy__AGE_IN_DAYS_AT_TREATMENT_START.md)  <sub>1..1</sub>
     * Description: The age in days of the subject at the time that this treatment was started
     * Range: [Integer](types/Integer.md)
 * [➞AGE_IN_DAYS_AT_TREATMENT_END](therapy__AGE_IN_DAYS_AT_TREATMENT_END.md)  <sub>1..1</sub>
     * Description: The age in days of the subject at the time that this treatment was completed
     * Range: [Integer](types/Integer.md)
 * [➞OFF_TREATMENT_REASON](therapy__OFF_TREATMENT_REASON.md)  <sub>0..1</sub>
     * Description: Reason for stopping treatment
     * Range: [OffTreatmentReasonEnum](OffTreatmentReasonEnum.md)
 * [➞REGIMEN_OR_LINE_OF_THERAPY](therapy__REGIMEN_OR_LINE_OF_THERAPY.md)  <sub>0..1</sub>
     * Description: Line of therapy
     * Range: [RegimenOrLineOfTherapyEnum](RegimenOrLineOfTherapyEnum.md)
 * [➞NUMBER_OF_CYCLES](therapy__NUMBER_OF_CYCLES.md)  <sub>0..1</sub>
     * Description: Number of treatment cycles administered
     * Range: [Integer](types/Integer.md)
 * [➞RESPONSE](therapy__RESPONSE.md)  <sub>0..1</sub>
     * Description: Response to treatment
     * Range: [String](types/String.md)
 * [Therapy➞THERAPY_ANATOMIC_SITE_UBERON_CODE](Therapy_THERAPY_ANATOMIC_SITE_UBERON_CODE.md)  <sub>0..1</sub>
     * Description: Required when TREATMENT_TYPE is a surgical or radiation therapy
     * Range: [String](types/String.md)
 * [Therapy➞OFF_TREATMENT_REASON](Therapy_OFF_TREATMENT_REASON.md)  <sub>0..1</sub>
     * Description: Required when AGE_IN_DAYS_AT_TREATMENT_END is present
     * Range: [String](types/String.md)
 * [Therapy➞REGIMEN_OR_LINE_OF_THERAPY](Therapy_REGIMEN_OR_LINE_OF_THERAPY.md)  <sub>0..1</sub>
     * Description: Required when TREATMENT_TYPE is pharmacotherapy
     * Range: [String](types/String.md)
 * [Therapy➞NUMBER_OF_CYCLES](Therapy_NUMBER_OF_CYCLES.md)  <sub>0..1</sub>
     * Description: Required when TREATMENT_TYPE is pharmacotherapy
     * Range: [String](types/String.md)
 * [Therapy➞RESPONSE](Therapy_RESPONSE.md)  <sub>0..1</sub>
     * Description: Required when AGE_IN_DAYS_AT_TREATMENT_END is present
     * Range: [String](types/String.md)
