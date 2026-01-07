# scRNA-seq - Level 1

HTAN scRNA-seq Level 1 Data Model - Raw sequencing files and metadata

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string, pattern: <code>^.+[\\/]\S*$</code> | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_(D[0-9]{1,20})$</code> | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string, pattern: <code>^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000\|EXT[0-9]{1,18}\|[0-9]{1,21})_([BD][0-9]{1,20})$</code> | Yes | HTAN Parent ID - Foreign Key to parent entity (B for Biospecimen, D for data file). Must have B or D suffix. Supports HTA200-229 for phase 2. |

### Base Sequencing Attributes

These attributes are inherited from BaseSequencingAttributes.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `GENOME_ANNOTATION_URL` | string | No | URL to genome annotation |
| `GENOMIC_REFERENCE` | string | Yes | Genomic reference used for alignment |
| `GENOMIC_REFERENCE_URL` | string | No | URL to genomic reference |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayout) | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatform) | Yes | Sequencing platform used |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](#dissociationmethod) | Yes | Method used to dissociate tissue into single cells |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](#libraryconstructionmethod) | Yes | Method used to construct the sequencing library |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](#nucleicacidsource) | Yes | Type of nucleic acid used for sequencing |
| `READ_INDICATOR` | [ReadIndicatorEnum](#readindicator) | Yes | Type of read (forward, reverse, index) |
| `REVERSE_TRANSCRIPTION_PRIMER` | [ReverseTranscriptionPrimerEnum](#reversetranscriptionprimer) | Yes | Primer used for reverse transcription |
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](#singlecellisolationmethod) | Yes | Method used to isolate single cells |
| `SPIKE_IN` | [SpikeInEnum](#spikein) | Yes | Type of spike-in used, if any |

