
# Class: MolecularTest

Information about the molecular test

URI: [htan:MolecularTest](https://w3id.org/htan/MolecularTest)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20MOLECULAR_TESTS%200..*>[MolecularTest&#124;TIMEPOINT_LABEL:string;AGE_IN_DAYS_AT_MOLECULAR_TEST_START:integer;AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP:integer;GENE_SYMBOL:gene_symbol_enum;MOLECULAR_ANALYSIS_METHOD:MolecularAnalysisMethodEnum;MOLECULAR_ANALYSIS_RESULT:string;AA_CHANGE:string;CLINICAL_BIOSPECIMEN_TYPE:ClinicalBiospecimenTypeEnum;COPY_NUMBER:integer;EXON:integer;MOLECULAR_CONSEQUENCE:MolecularConsequenceEnum;PATHOGENICITY:PathogenicityEnum;TEST_ANALYTE_TYPE:TestAnalyteTypeEnum;TEST_UNITS:string;TEST_RESULT:string;VARIANT_ORIGIN:VariantOriginEnum;VARIANT_TYPE:VariantTypeEnum],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[ClinicalData]++-%20MOLECULAR_TESTS%200..*>[MolecularTest&#124;TIMEPOINT_LABEL:string;AGE_IN_DAYS_AT_MOLECULAR_TEST_START:integer;AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP:integer;GENE_SYMBOL:gene_symbol_enum;MOLECULAR_ANALYSIS_METHOD:MolecularAnalysisMethodEnum;MOLECULAR_ANALYSIS_RESULT:string;AA_CHANGE:string;CLINICAL_BIOSPECIMEN_TYPE:ClinicalBiospecimenTypeEnum;COPY_NUMBER:integer;EXON:integer;MOLECULAR_CONSEQUENCE:MolecularConsequenceEnum;PATHOGENICITY:PathogenicityEnum;TEST_ANALYTE_TYPE:TestAnalyteTypeEnum;TEST_UNITS:string;TEST_RESULT:string;VARIANT_ORIGIN:VariantOriginEnum;VARIANT_TYPE:VariantTypeEnum],[ClinicalData])

## Referenced by Class

 *  **None** *[➞MOLECULAR_TESTS](clinicalData__MOLECULAR_TESTS.md)*  <sub>0..\*</sub>  **[MolecularTest](MolecularTest.md)**

## Attributes


### Own

 * [➞TIMEPOINT_LABEL](molecularTest__TIMEPOINT_LABEL.md)  <sub>1..1</sub>
     * Description: Label for the timepoint (caDSR:2192201) (Aligns to CDRC Standard CDE)
     * Range: [String](types/String.md)
 * [➞AGE_IN_DAYS_AT_MOLECULAR_TEST_START](molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_START.md)  <sub>1..1</sub>
     * Description: Age in days at molecular test start (caDSR:2192202) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP](molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP.md)  <sub>1..1</sub>
     * Description: Age in days at molecular test stop (caDSR:2192203) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞GENE_SYMBOL](molecularTest__GENE_SYMBOL.md)  <sub>1..1</sub>
     * Description: Gene symbol (caDSR:2192204) (Aligns to CDRC Standard CDE)
     * Range: [gene_symbol_enum](gene_symbol_enum.md)
 * [➞MOLECULAR_ANALYSIS_METHOD](molecularTest__MOLECULAR_ANALYSIS_METHOD.md)  <sub>1..1</sub>
     * Description: Molecular analysis method (caDSR:2192205) (Aligns to CDRC Standard CDE)
     * Range: [MolecularAnalysisMethodEnum](MolecularAnalysisMethodEnum.md)
 * [➞MOLECULAR_ANALYSIS_RESULT](molecularTest__MOLECULAR_ANALYSIS_RESULT.md)  <sub>1..1</sub>
     * Description: Molecular analysis result (caDSR:2192206) (Aligns to CDRC Standard CDE)
     * Range: [String](types/String.md)
 * [➞AA_CHANGE](molecularTest__AA_CHANGE.md)  <sub>1..1</sub>
     * Description: Amino acid change (caDSR:2192207) (Aligns to CDRC Standard CDE)
     * Range: [String](types/String.md)
 * [➞CLINICAL_BIOSPECIMEN_TYPE](molecularTest__CLINICAL_BIOSPECIMEN_TYPE.md)  <sub>1..1</sub>
     * Description: Clinical biospecimen type (caDSR:2192208) (Aligns to CDRC Standard CDE)
     * Range: [ClinicalBiospecimenTypeEnum](ClinicalBiospecimenTypeEnum.md)
 * [➞COPY_NUMBER](molecularTest__COPY_NUMBER.md)  <sub>1..1</sub>
     * Description: Copy number (caDSR:2192209) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞EXON](molecularTest__EXON.md)  <sub>1..1</sub>
     * Description: Exon number (caDSR:2192210) (Aligns to CDRC Standard CDE)
     * Range: [Integer](types/Integer.md)
 * [➞MOLECULAR_CONSEQUENCE](molecularTest__MOLECULAR_CONSEQUENCE.md)  <sub>1..1</sub>
     * Description: Molecular consequence (caDSR:2192211) (Aligns to CDRC Standard CDE)
     * Range: [MolecularConsequenceEnum](MolecularConsequenceEnum.md)
 * [➞PATHOGENICITY](molecularTest__PATHOGENICITY.md)  <sub>1..1</sub>
     * Description: Pathogenicity (caDSR:2192212) (Aligns to CDRC Standard CDE)
     * Range: [PathogenicityEnum](PathogenicityEnum.md)
 * [➞TEST_ANALYTE_TYPE](molecularTest__TEST_ANALYTE_TYPE.md)  <sub>1..1</sub>
     * Description: Test analyte type (caDSR:2192213) (Aligns to CDRC Standard CDE)
     * Range: [TestAnalyteTypeEnum](TestAnalyteTypeEnum.md)
 * [➞TEST_UNITS](molecularTest__TEST_UNITS.md)  <sub>1..1</sub>
     * Description: Test units (caDSR:2192214) (Aligns to CDRC Standard CDE)
     * Range: [String](types/String.md)
 * [➞TEST_RESULT](molecularTest__TEST_RESULT.md)  <sub>1..1</sub>
     * Description: Test result (caDSR:2192215) (Aligns to CDRC Standard CDE)
     * Range: [String](types/String.md)
 * [➞VARIANT_ORIGIN](molecularTest__VARIANT_ORIGIN.md)  <sub>1..1</sub>
     * Description: Variant origin (caDSR:2192216) (Aligns to CDRC Standard CDE)
     * Range: [VariantOriginEnum](VariantOriginEnum.md)
 * [➞VARIANT_TYPE](molecularTest__VARIANT_TYPE.md)  <sub>1..1</sub>
     * Description: Variant type (caDSR:2192217) (Aligns to CDRC Standard CDE)
     * Range: [VariantTypeEnum](VariantTypeEnum.md)
 * [MolecularTest➞AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP](MolecularTest_AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_METHOD is DNA Sequencing or RNA Sequencing
     * Range: [String](types/String.md)
 * [MolecularTest➞AA_CHANGE](MolecularTest_AA_CHANGE.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * Range: [String](types/String.md)
 * [MolecularTest➞COPY_NUMBER](MolecularTest_COPY_NUMBER.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_RESULT is Copy number variant detected
     * Range: [String](types/String.md)
 * [MolecularTest➞EXON](MolecularTest_EXON.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * Range: [String](types/String.md)
 * [MolecularTest➞MOLECULAR_CONSEQUENCE](MolecularTest_MOLECULAR_CONSEQUENCE.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * Range: [String](types/String.md)
 * [MolecularTest➞PATHOGENICITY](MolecularTest_PATHOGENICITY.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_RESULT is Pathogenic variant detected or Variant of uncertain significance detected
     * Range: [String](types/String.md)
 * [MolecularTest➞TEST_ANALYTE_TYPE](MolecularTest_TEST_ANALYTE_TYPE.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_METHOD is DNA Sequencing or RNA Sequencing
     * Range: [String](types/String.md)
 * [MolecularTest➞TEST_UNITS](MolecularTest_TEST_UNITS.md)  <sub>0..1</sub>
     * Description: Required when MOLECULAR_ANALYSIS_RESULT is Copy number variant detected
     * Range: [String](types/String.md)
