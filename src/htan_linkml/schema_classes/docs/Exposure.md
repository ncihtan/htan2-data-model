
# Class: Exposure

Information about the exposure

URI: [htan:Exposure](https://w3id.org/htan/Exposure)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20EXPOSURES%201..1>[Exposure&#124;SMOKING_HISTORY:SmokingHistoryEnum;YEARS_SMOKED:integer%20%3F;PACK_YEARS_SMOKED:decimal%20%3F;ALCOHOL_HISTORY_INDICATOR:AlcoholHistoryIndicatorEnum;ENVIRONMENTAL_EXPOSURE:EnvironmentalExposureEnum;ENVIRONMENTAL_EXPOSURE_TYPE:EnvironmentalExposureTypeEnum%20%3F],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20EXPOSURES%201..1>[Exposure&#124;SMOKING_HISTORY:SmokingHistoryEnum;YEARS_SMOKED:integer%20%3F;PACK_YEARS_SMOKED:decimal%20%3F;ALCOHOL_HISTORY_INDICATOR:AlcoholHistoryIndicatorEnum;ENVIRONMENTAL_EXPOSURE:EnvironmentalExposureEnum;ENVIRONMENTAL_EXPOSURE_TYPE:EnvironmentalExposureTypeEnum%20%3F],[ClinicalData])

## Referenced by Class

 *  **None** *[➞EXPOSURES](clinicalData__EXPOSURES.md)*  <sub>1..1</sub>  **[Exposure](Exposure.md)**

## Attributes


### Own

 * [➞SMOKING_HISTORY](exposure__SMOKING_HISTORY.md)  <sub>1..1</sub>
     * Description: Smoking history of the participant (caDSR:2192201) (Aligns to CDRC Standard CDE)
     * Range: [SmokingHistoryEnum](SmokingHistoryEnum.md)
 * [➞YEARS_SMOKED](exposure__YEARS_SMOKED.md)  <sub>0..1</sub>
     * Description: Number of years the participant has smoked (caDSR:2192202) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞PACK_YEARS_SMOKED](exposure__PACK_YEARS_SMOKED.md)  <sub>0..1</sub>
     * Description: Number of pack years the participant has smoked (caDSR:2192203) (Aligns to CDRC Standard CDE)
     * Range: [Decimal](types/Decimal.md)
 * [➞ALCOHOL_HISTORY_INDICATOR](exposure__ALCOHOL_HISTORY_INDICATOR.md)  <sub>1..1</sub>
     * Description: Alcohol history indicator of the participant (caDSR:2192204) (Aligns to CDRC Standard CDE)
     * Range: [AlcoholHistoryIndicatorEnum](AlcoholHistoryIndicatorEnum.md)
 * [➞ENVIRONMENTAL_EXPOSURE](exposure__ENVIRONMENTAL_EXPOSURE.md)  <sub>1..1</sub>
     * Description: Environmental exposure of the participant (caDSR:2192205) (Aligns to CDRC Standard CDE)
     * Range: [EnvironmentalExposureEnum](EnvironmentalExposureEnum.md)
 * [➞ENVIRONMENTAL_EXPOSURE_TYPE](exposure__ENVIRONMENTAL_EXPOSURE_TYPE.md)  <sub>0..1</sub>
     * Description: Type of environmental exposure (caDSR:2192206) (Aligns to CDRC Standard CDE)
     * Range: [EnvironmentalExposureTypeEnum](EnvironmentalExposureTypeEnum.md)
 * [Exposure➞YEARS_SMOKED](Exposure_YEARS_SMOKED.md)  <sub>0..1</sub>
     * Description: Required when SMOKING_HISTORY is Current smoker or Former smoker
     * Range: [String](types/String.md)
 * [Exposure➞PACK_YEARS_SMOKED](Exposure_PACK_YEARS_SMOKED.md)  <sub>0..1</sub>
     * Description: Required when SMOKING_HISTORY is Current smoker or Former smoker
     * Range: [String](types/String.md)
 * [Exposure➞ENVIRONMENTAL_EXPOSURE_TYPE](Exposure_ENVIRONMENTAL_EXPOSURE_TYPE.md)  <sub>0..1</sub>
     * Description: Required when ENVIRONMENTAL_EXPOSURE is Yes
     * Range: [String](types/String.md)
