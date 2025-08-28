
# Class: CoreFileAttributes

Universal attributes that apply to all file-based data in HTAN

URI: [htan:CoreFileAttributes](https://w3id.org/htan/CoreFileAttributes)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[CoreFileAttributes&#124;COMPONENT:string;FILENAME:string;FILE_FORMAT:string;HTAN_DATA_FILE_ID:string;HTAN_PARENT_ID:string]^-[ClinicalData],[ClinicalData])](https://yuml.me/diagram/nofunky;dir:TB/class/[CoreFileAttributes&#124;COMPONENT:string;FILENAME:string;FILE_FORMAT:string;HTAN_DATA_FILE_ID:string;HTAN_PARENT_ID:string]^-[ClinicalData],[ClinicalData])

## Children

 * [ClinicalData](ClinicalData.md) - Container for all clinical data

## Referenced by Class


## Attributes


### Own

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
