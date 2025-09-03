-- # Class: "BulkWESLevel1" Description: "Bulk Whole Exome Sequencing Level 1 - Raw files"
--     * Slot: SEQUENCING_BATCH_ID Description: Sequencing batch identifier
--     * Slot: LIBRARY_LAYOUT Description: Library layout (paired-end or single-end)
--     * Slot: READ_INDICATOR Description: Read indicator
--     * Slot: LIBRARY_SELECTION_METHOD Description: Method used for library selection
--     * Slot: READ_LENGTH Description: Read length in base pairs
--     * Slot: TARGET_CAPTURE_KIT Description: Target capture kit used
--     * Slot: LIBRARY_PREPARATION_KIT_NAME Description: Name of the library preparation kit
--     * Slot: LIBRARY_PREPARATION_KIT_VENDOR Description: Vendor of the library preparation kit
--     * Slot: LIBRARY_PREPARATION_KIT_VERSION Description: Version of the library preparation kit
--     * Slot: SEQUENCING_PLATFORM Description: Sequencing platform used
--     * Slot: ADAPTER_NAME Description: Name of the adapter used
--     * Slot: ADAPTER_SEQUENCE Description: Adapter sequence
--     * Slot: BASE_CALLER_NAME Description: Name of the base caller
--     * Slot: BASE_CALLER_VERSION Description: Version of the base caller
--     * Slot: FLOW_CELL_BARCODE Description: Flow cell barcode
--     * Slot: FRAGMENT_MAXIMUM_LENGTH Description: Maximum fragment length
--     * Slot: FRAGMENT_MEAN_LENGTH Description: Mean fragment length
--     * Slot: FRAGMENT_MINIMUM_LENGTH Description: Minimum fragment length
--     * Slot: FRAGMENT_STANDARD_DEVIATION_LENGTH Description: Standard deviation of fragment length
--     * Slot: LANE_NUMBER Description: Lane number
--     * Slot: MULTIPLEX_BARCODE Description: Multiplex barcode
--     * Slot: LIBRARY_PREPARATION_DAYS_FROM_INDEX Description: Days from index for library preparation
--     * Slot: SIZE_SELECTION_RANGE Description: Size selection range
--     * Slot: TARGET_DEPTH Description: Target sequencing depth
--     * Slot: TO_TRIM_ADAPTER_SEQUENCE Description: Whether to trim adapter sequence
--     * Slot: COMPONENT Description: Category of metadata (e.g., Bulk WES Level 1, scRNA-seq Level 2, etc.)
--     * Slot: FILENAME Description: Name of the file
--     * Slot: FILE_FORMAT Description: Format of the file (e.g., fastq, bam, vcf, h5ad)
--     * Slot: HTAN_PARTICIPANT_ID Description: HTAN ID associated with a patient based on HTAN ID SOP (Primary Key)
--     * Slot: HTAN_DATA_FILE_ID Description: HTAN Data File ID (Primary Key)
--     * Slot: HTAN_PARENT_ID Description: HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
--     * Slot: HTAN_BIOSPECIMEN_ID Description: HTAN Biospecimen ID of the parent biospecimen (Primary Key)
-- # Class: "CoreFileAttributes" Description: "Universal attributes that apply to all file-based data in HTAN"
--     * Slot: COMPONENT Description: Category of metadata (e.g., Bulk WES Level 1, scRNA-seq Level 2, etc.)
--     * Slot: FILENAME Description: Name of the file
--     * Slot: FILE_FORMAT Description: Format of the file (e.g., fastq, bam, vcf, h5ad)
--     * Slot: HTAN_PARTICIPANT_ID Description: HTAN ID associated with a patient based on HTAN ID SOP (Primary Key)
--     * Slot: HTAN_DATA_FILE_ID Description: HTAN Data File ID (Primary Key)
--     * Slot: HTAN_PARENT_ID Description: HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file)
--     * Slot: HTAN_BIOSPECIMEN_ID Description: HTAN Biospecimen ID of the parent biospecimen (Primary Key)

CREATE TABLE "BulkWESLevel1" (
	"SEQUENCING_BATCH_ID" TEXT, 
	"LIBRARY_LAYOUT" VARCHAR(10) NOT NULL, 
	"READ_INDICATOR" TEXT, 
	"LIBRARY_SELECTION_METHOD" VARCHAR(16) NOT NULL, 
	"READ_LENGTH" INTEGER NOT NULL, 
	"TARGET_CAPTURE_KIT" TEXT, 
	"LIBRARY_PREPARATION_KIT_NAME" TEXT, 
	"LIBRARY_PREPARATION_KIT_VENDOR" TEXT, 
	"LIBRARY_PREPARATION_KIT_VERSION" TEXT, 
	"SEQUENCING_PLATFORM" VARCHAR(17) NOT NULL, 
	"ADAPTER_NAME" TEXT, 
	"ADAPTER_SEQUENCE" TEXT, 
	"BASE_CALLER_NAME" TEXT, 
	"BASE_CALLER_VERSION" TEXT, 
	"FLOW_CELL_BARCODE" TEXT, 
	"FRAGMENT_MAXIMUM_LENGTH" INTEGER, 
	"FRAGMENT_MEAN_LENGTH" INTEGER, 
	"FRAGMENT_MINIMUM_LENGTH" INTEGER, 
	"FRAGMENT_STANDARD_DEVIATION_LENGTH" INTEGER, 
	"LANE_NUMBER" INTEGER, 
	"MULTIPLEX_BARCODE" TEXT, 
	"LIBRARY_PREPARATION_DAYS_FROM_INDEX" INTEGER, 
	"SIZE_SELECTION_RANGE" TEXT, 
	"TARGET_DEPTH" INTEGER, 
	"TO_TRIM_ADAPTER_SEQUENCE" BOOLEAN, 
	"COMPONENT" TEXT NOT NULL, 
	"FILENAME" TEXT NOT NULL, 
	"FILE_FORMAT" TEXT NOT NULL, 
	"HTAN_PARTICIPANT_ID" TEXT NOT NULL, 
	"HTAN_DATA_FILE_ID" TEXT NOT NULL, 
	"HTAN_PARENT_ID" TEXT NOT NULL, 
	"HTAN_BIOSPECIMEN_ID" TEXT NOT NULL, 
	PRIMARY KEY ("HTAN_DATA_FILE_ID")
);
CREATE TABLE "CoreFileAttributes" (
	"COMPONENT" TEXT NOT NULL, 
	"FILENAME" TEXT NOT NULL, 
	"FILE_FORMAT" TEXT NOT NULL, 
	"HTAN_PARTICIPANT_ID" TEXT NOT NULL, 
	"HTAN_DATA_FILE_ID" TEXT NOT NULL, 
	"HTAN_PARENT_ID" TEXT NOT NULL, 
	"HTAN_BIOSPECIMEN_ID" TEXT NOT NULL, 
	PRIMARY KEY ("HTAN_DATA_FILE_ID")
);