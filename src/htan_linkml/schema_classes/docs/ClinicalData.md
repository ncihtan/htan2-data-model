
# Class: ClinicalData

Container for all clinical data

URI: [htan:ClinicalData](https://w3id.org/htan/ClinicalData)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[VitalStatus],[Therapy],[MolecularTest],[FollowUp],[FamilyHistory],[Exposure],[Diagnosis],[Demographics],[CoreFileAttributes],[Therapy]<THERAPIES%200..*-++[ClinicalData&#124;COMPONENT(i):string;FILENAME(i):string;FILE_FORMAT(i):string;HTAN_DATA_FILE_ID(i):string;HTAN_PARENT_ID(i):string],[MolecularTest]<MOLECULAR_TESTS%200..*-++[ClinicalData],[FollowUp]<FOLLOW_UPS%200..*-++[ClinicalData],[FamilyHistory]<FAMILY_HISTORY%201..1-++[ClinicalData],[Exposure]<EXPOSURES%201..1-++[ClinicalData],[Diagnosis]<DIAGNOSIS%201..1-++[ClinicalData],[VitalStatus]<VITAL_STATUS%201..1-++[ClinicalData],[Demographics]<DEMOGRAPHICS%201..1-++[ClinicalData],[CoreFileAttributes]^-[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[VitalStatus],[Therapy],[MolecularTest],[FollowUp],[FamilyHistory],[Exposure],[Diagnosis],[Demographics],[CoreFileAttributes],[Therapy]<THERAPIES%200..*-++[ClinicalData&#124;COMPONENT(i):string;FILENAME(i):string;FILE_FORMAT(i):string;HTAN_DATA_FILE_ID(i):string;HTAN_PARENT_ID(i):string],[MolecularTest]<MOLECULAR_TESTS%200..*-++[ClinicalData],[FollowUp]<FOLLOW_UPS%200..*-++[ClinicalData],[FamilyHistory]<FAMILY_HISTORY%201..1-++[ClinicalData],[Exposure]<EXPOSURES%201..1-++[ClinicalData],[Diagnosis]<DIAGNOSIS%201..1-++[ClinicalData],[VitalStatus]<VITAL_STATUS%201..1-++[ClinicalData],[Demographics]<DEMOGRAPHICS%201..1-++[ClinicalData],[CoreFileAttributes]^-[ClinicalData])

## Parents

 *  is_a: [CoreFileAttributes](CoreFileAttributes.md) - Universal attributes that apply to all file-based data in HTAN

## Attributes


### Own

 * [➞DEMOGRAPHICS](clinicalData__DEMOGRAPHICS.md)  <sub>1..1</sub>
     * Description: Demographic information
     * Range: [Demographics](Demographics.md)
 * [➞VITAL_STATUS](clinicalData__VITAL_STATUS.md)  <sub>1..1</sub>
     * Description: Vital status information
     * Range: [VitalStatus](VitalStatus.md)
 * [➞DIAGNOSIS](clinicalData__DIAGNOSIS.md)  <sub>1..1</sub>
     * Description: Primary diagnosis information
     * Range: [Diagnosis](Diagnosis.md)
 * [➞EXPOSURES](clinicalData__EXPOSURES.md)  <sub>1..1</sub>
     * Description: Exposure history
     * Range: [Exposure](Exposure.md)
 * [➞FAMILY_HISTORY](clinicalData__FAMILY_HISTORY.md)  <sub>1..1</sub>
     * Description: Family history of cancer
     * Range: [FamilyHistory](FamilyHistory.md)
 * [➞FOLLOW_UPS](clinicalData__FOLLOW_UPS.md)  <sub>0..\*</sub>
     * Description: Follow-up observations
     * Range: [FollowUp](FollowUp.md)
 * [➞MOLECULAR_TESTS](clinicalData__MOLECULAR_TESTS.md)  <sub>0..\*</sub>
     * Description: Molecular test results
     * Range: [MolecularTest](MolecularTest.md)
 * [➞THERAPIES](clinicalData__THERAPIES.md)  <sub>0..\*</sub>
     * Description: Therapy information
     * Range: [Therapy](Therapy.md)

### Inherited from CoreFileAttributes:

 * [➞COMPONENT](coreFileAttributes__COMPONENT.md)  <sub>1..1</sub>
     * Description: Category of metadata (e.g., Bulk WES Level 1, scRNA-seq Level 2, etc.)
     * Range: [String](types/String.md)
 * [➞FILENAME](coreFileAttributes__FILENAME.md)  <sub>1..1</sub>
     * Description: Name of the file
     * Range: [String](types/String.md)
 * [➞FILE_FORMAT](coreFileAttributes__FILE_FORMAT.md)  <sub>1..1</sub>
     * Description: Format of the file (e.g., fastq, bam, vcf, h5ad)
     * Range: [String](types/String.md)
 * [➞HTAN_DATA_FILE_ID](coreFileAttributes__HTAN_DATA_FILE_ID.md)  <sub>1..1</sub>
     * Description: HTAN Data File ID (Primary Key)
     * Range: [String](types/String.md)
 * [➞HTAN_PARENT_ID](coreFileAttributes__HTAN_PARENT_ID.md)  <sub>1..1</sub>
     * Description: HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
     * Range: [String](types/String.md)
