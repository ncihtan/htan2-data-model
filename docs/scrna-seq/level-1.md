# scRNA-seq - Level 1

📥 [Download attributes as CSV](csv/scrna-seq-level-1.csv)

If submitting Level 1 files for scRNA-seq, here are the list of attributes you need to fill out:

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

### Core File Attributes

These attributes are inherited from CoreFileAttributes and apply to all file-based data.

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
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
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Days from index for library preparation |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `WORKFLOW_LINK` | string | No | Link to workflow or command. DockStore.org recommended |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow |

### Module-Specific Attributes

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](#dissociationmethodenum) | Yes | Method used to dissociate tissue into single cells |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](#libraryconstructionmethodenum) | Yes | Method used to construct the sequencing library |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](#nucleicacidsourceenum) | Yes | Type of nucleic acid used for sequencing |
| `READ_INDICATOR` | [ReadIndicatorEnum](#readindicatorenum) | Yes | Type of read (forward, reverse, index) |
| `REVERSE_TRANSCRIPTION_PRIMER` | [ReverseTranscriptionPrimerEnum](#reversetranscriptionprimerenum) | Yes | Primer used for reverse transcription |
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](#singlecellisolationmethodenum) | Yes | Method used to isolate single cells |
| `SPIKE_IN` | [SpikeInEnum](#spikeinenum) | Yes | Type of spike-in used, if any |

## Enums

### DissociationMethodEnum

| Value | Description |
|-------|-------------|
| `Enzymatic` | Enzymatic dissociation method |
| `Mechanical` | Mechanical dissociation method |
| `Other` | Other dissociation method |
| `Unknown` | Unknown dissociation method |

### LibraryConstructionMethodEnum

| Value | Description |
|-------|-------------|
| `10X Genomics` | 10X Genomics library construction method |
| `Drop-seq` | Drop-seq library construction method |
| `Fluidigm C1` | Fluidigm C1 library construction method |
| `InDrop` | InDrop library construction method |
| `Other` | Other library construction method |
| `Smart-seq` | Smart-seq library construction method |
| `Unknown` | Unknown library construction method |

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| `Paired-end` | Paired-end sequencing |
| `Single-end` | Single-end sequencing |

### NucleicAcidSourceEnum

| Value | Description |
|-------|-------------|
| `DNA` | DNA nucleic acid source |
| `RNA` | RNA nucleic acid source |
| `Unknown` | Unknown nucleic acid source |

### ReadIndicatorEnum

| Value | Description |
|-------|-------------|
| `Forward` | Forward read indicator |
| `Index` | Index read indicator |
| `Reverse` | Reverse read indicator |
| `Unknown` | Unknown read indicator |

### ReverseTranscriptionPrimerEnum

| Value | Description |
|-------|-------------|
| `Oligo-dT` | Oligo-dT reverse transcription primer |
| `Random Hexamer` | Random hexamer reverse transcription primer |
| `Unknown` | Unknown reverse transcription primer |

### SequencingPlatformEnum

| Value | Description |
|-------|-------------|
| `ABI_SOLID` | ABI SOLID sequencing platform |
| `BGISEQ` | BGI sequencing platform |
| `CAPILLARY` | Capillary sequencing platform |
| `COMPLETE_GENOMICS` | Complete Genomics sequencing platform |
| `HELICOS` | Helicos sequencing platform |
| `ILLUMINA` | Illumina sequencing platform |
| `ION_TORRENT` | Ion Torrent sequencing platform |
| `LS454` | 454 sequencing platform |
| `OXFORD_NANOPORE` | Oxford Nanopore sequencing platform |
| `PACBIO_SMRT` | PacBio SMRT sequencing platform |

### SingleCellIsolationMethodEnum

| Value | Description |
|-------|-------------|
| `Cell Sorting` | Cell sorting isolation method |
| `Droplet-based` | Droplet-based isolation method |
| `Manual Picking` | Manual picking isolation method |
| `Microfluidics` | Microfluidics isolation method |
| `Other` | Other isolation method |
| `Unknown` | Unknown isolation method |

### SpikeInEnum

| Value | Description |
|-------|-------------|
| `ERCC` | ERCC spike-in |
| `None` | No spike-in |
| `Other` | Other spike-in |
| `Unknown` | Unknown spike-in |

