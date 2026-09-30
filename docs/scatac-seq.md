# scATAC-seq

HTAN scATAC-seq Data Model - Single-cell ATAC sequencing data

## BaseSequencingAttributes

**Minimal base attributes shared across all sequencing types**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseSequencingLevel1Attributes

**Level 1 attributes - sequencing run and library (raw data)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseSequencingLevel2Attributes

**Level 2 attributes - alignment and alignment workflow**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## BaseSequencingLevel3Attributes

**Level 3+ attributes - inherits alignment and workflow; used for processed/analysis levels**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## SingleCellLevel1Attributes

**Shared upstream single-cell / single-nucleus preparation attributes for single-cell sequencing Level 1 (tissue-to-cell/nucleus steps common to scRNA-seq and scATAC-seq)**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](#singlecellisolationmethodenum) | Yes | Method used to isolate single cells |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](#dissociationmethodenum) | Yes | Method used to dissociate tissue into single cells |
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](#nucleicacidsourceenum) | Yes | Type of nucleic acid used for sequencing |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](#libraryconstructionmethodenum) | Yes | Method used to construct the sequencing library |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## scATACLevel1

**scATAC-seq Level 1 data - Raw sequencing files and metadata**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the raw sequencing file (fastq or fastq.gz) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.fastq for fastq; .fastq.gz or .fq.gz for fastq.gz) |
| `REVERSE_TRANSCRIPTION_PRIMER` | [ReverseTranscriptionPrimerEnum](#reversetranscriptionprimerenum) | No | Primer used for reverse transcription. Applicable only to multiome / hybrid RNA+ATAC protocols; standard scATAC-seq has no reverse-transcription step and should leave this blank. |
| `SPIKE_IN` | [SpikeInEnum](#spikeinenum) | No | Type of spike-in used, if any. Applicable only to multiome / hybrid RNA+ATAC protocols; standard scATAC-seq has no RNA spike-in and should leave this blank. |
| `NUCLEUS_IDENTIFIER` | string | Yes | Unique nuclei barcode; added at transposition step. Determines which nucleus the reads originated from |
| `NUCLEI_BARCODE` | string | No | Nuclei barcode sequence used to demultiplex reads to individual nuclei |
| `NUCLEI_BARCODE_READ` | string | Yes | Sequencing read that contains the nuclei barcode sequence |
| `NUCLEI_BARCODE_LENGTH` | integer | Yes | Length, in base pairs, of the nuclei barcode sequence |
| `SCATAC_SEQ_READ_1` | [SequencingReadEnum](#sequencingreadenum) | Yes | Read 1 content description |
| `SCATAC_SEQ_READ_2` | [SequencingReadEnum](#sequencingreadenum) | Yes | Read 2 content description |
| `SCATAC_SEQ_READ_3` | [SequencingReadEnum](#sequencingreadenum) | No | Read 3 content description |
| `TOTAL_NUMBER_OF_PASSING_NUCLEI` | integer | Yes | Number of nuclei sequenced |
| `SINGLE_NUCLEUS_BUFFER` | [SingleNucleusBufferEnum](#singlenucleusbufferenum) | Yes | Nuclei isolation buffer |
| `TRANSPOSITION_REACTION` | [TranspositionReactionEnum](#transpositionreactionenum) | Yes | Name of the transposase, transposon sequences |
| `TOTAL_READS` | integer | Yes | Total number of reads collected from samtools. |
| `MAP_Q_30` | float | Yes | Number of reads with Quality >= 30. |
| `TOTAL_READ_PAIRS` | integer | Yes | Total read-pairs |
| `SINGLE_CELL_ISOLATION_METHOD` | [SingleCellIsolationMethodEnum](#singlecellisolationmethodenum) | Yes | Method used to isolate single cells |
| `DISSOCIATION_METHOD` | [DissociationMethodEnum](#dissociationmethodenum) | Yes | Method used to dissociate tissue into single cells |
| `CRYOPRESERVED_CELLS_IN_SAMPLE` | boolean | No | Whether cells were cryopreserved in the sample |
| `NUCLEIC_ACID_SOURCE` | [NucleicAcidSourceEnum](#nucleicacidsourceenum) | Yes | Type of nucleic acid used for sequencing |
| `LIBRARY_CONSTRUCTION_METHOD` | [LibraryConstructionMethodEnum](#libraryconstructionmethodenum) | Yes | Method used to construct the sequencing library |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## scATACLevel2

**scATAC-seq Level 2 data - Aligned data and alignment QC metrics**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the aligned file (bam or cram) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.bam for bam; .cram for cram) |
| `AVERAGE_BASE_QUALITY` | float | No | Average base quality collected. |
| `AVERAGE_INSERT_SIZE` | float | Conditional: Average insert size is required for paired-end libraries | Average insert size collected. Required when LIBRARY_LAYOUT is Paired-end. |
| `AVERAGE_READ_LENGTH` | float | No | Average read length collected. |
| `MEAN_COVERAGE` | float | No | Mean coverage for whole genome sequencing, or mean target coverage for whole exome and targeted sequencing |
| `PAIRS_ON_DIFF_CHR` | integer | No | Pairs on different chromosomes collected from samtools. |
| `PROPORTION_READS_MAPPED` | float | No | Proportion of mapped reads collected from samtools. |
| `TOTAL_UNIQUELY_MAPPED` | integer | Yes | Number of reads that map to genome. |
| `TOTAL_UNMAPPED_READS` | integer | Yes | Number of reads that did not map to genome |
| `PROPORTION_READS_DUPLICATED` | float | No | Proportion of duplicated reads collected from samtools. |
| `SHORT_READS` | integer | No | Number of reads that were too short |
| `PROPORTION_COVERAGE_10X` | float | No | Proportion of all reference bases for whole genome sequencing, or targeted bases for whole exome and targeted sequencing, that achieves 10X or greater coverage from Picard Tools. |
| `PROPORTION_COVERAGE_30X` | float | No | Proportion of all reference bases for whole genome sequencing, or targeted bases for whole exome and targeted sequencing, that achieves 30X or greater coverage from Picard Tools. |
| `PROPORTION_TARGETS_NO_MATCH` | float | No | Proportion of targets that did not reach 1X coverage over any base from Picard Tools. |
| `PROPORTION_BASE_MISMATCH` | float | No | Proportion of mismatched bases collected from samtools. |
| `PROPORTION_MITOCHONDRIAL_READS` | float | No | Proportion of reads mapping to mitochondria |
| `CONTAMINATION` | float | No | Fraction of reads coming from cross-sample contamination collected from GATK4. |
| `CONTAMINATION_ERROR` | float | No | Estimation error of cross-sample contamination collected from GATK4. |
| `MEDIAN_FRAGMENTS_PER_CELL` | float | Yes | Median number of sequencing fragments detected per cell across all cells in the dataset. |
| `MEDIAN_GENES_PER_CELL` | float | No | Median number of genes with detected gene expression per cell across all cells in the dataset. Optional - typically only available for multiome; regular scATAC-seq does not report it (per review, ykatariy). |
| `NUMBER_OF_CELLS` | integer | Yes | Total number of cells or nuclei retained in the dataset after filtering. |
| `THRESHOLD_FOR_MINIMUM_PASSING_READS` | integer | No | Minimum number of passing reads used as the threshold for calling a barcode a cell. |
| `MEDIAN_PASSING_READS_PERCENTAGE` | float | Yes | Non-PCR duplicate nuclear genomic sequence reads not aligning to unanchored contigs out of total reads assigned to the nucleus barcode |
| `DUPLICATE_READ_PAIRS` | integer | Yes | Number of duplicate read-pairs. Sanity check - must be <= TOTAL_READ_PAIRS (Level 1). |
| `CHIMERIC_READ_PAIRS` | integer | Yes | Number of chimerically mapped read-pairs. Sanity check - must be <= TOTAL_READ_PAIRS (Level 1). |
| `UNMAPPED_READ_PAIRS` | integer | Yes | Number of read-pairs with at least one end not mapped. Sanity check - must be <= TOTAL_READ_PAIRS (Level 1). |
| `LOW_MAP_Q` | integer | Yes | Number of read-pairs with <30 mapq on at least one end |
| `MITOCHONDRIAL_READ_PAIRS` | integer | No | Number of read-pairs mapping to mitochondria and non-nuclear contigs. Optional - sparsely reported for snATAC submissions (per review, ykatariy). |
| `PASSED_FILTERS` | integer | Yes | Number of non-duplicate, usable read-pairs (fragments) that aligned to the reference genome. |
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## CoreFileAttributes

**Universal attributes that apply to all file-based data in HTAN**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILENAME` | string | Yes | Name of the file |
| `FILE_FORMAT` | string | Yes | Format of the file (e.g., fastq, bam, vcf, h5ad) |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## scATACLevel3and4

**scATAC-seq Level 3 and 4 - Peak-by-cell matrices, fragment files, and chromatin accessibility metrics**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `FILE_FORMAT` | string | Yes | Format of the file (h5ad for peak by cell matrix and fragments information; bed for peak file) |
| `FILENAME` | string | Yes | Name of the file. Must end with an extension matching the FILE_FORMAT (.h5ad for h5ad, .bed for bed) |
| `N_COUNT_PEAKS` | integer | Yes | Total number of fragments in peaks |
| `N_FEATURE_PEAKS` | integer | Yes | Number of peaks with at least one read |
| `TSS_FRAGMENTS` | integer | No | Number of fragments overlapping with TSS regions |
| `TSS_ENRICHMENT` | float | No | Transcription start site (TSS) enrichment score |
| `TSS_PERCENTILE` | float | No | Percentile rank of TSS score |
| `DNASE_SENSITIVE_REGION_FRAGMENTS` | integer | No | Number of fragments overlapping with known DNaseI hypersensitive sites (DHS). |
| `ENHANCER_REGION_FRAGMENTS` | integer | No | Number of fragments overlapping enhancer regions |
| `PROMOTER_REGION_FRAGMENTS` | integer | No | Number of fragments overlapping promoter regions |
| `ON_TARGET_FRAGMENTS` | integer | No | Number of fragments overlapping any of TSS, enhancer, promoter and DNase hypersensitivity sites (counted with multiplicity). Sanity check - must be <= PASSED_FILTERS (Level 2). |
| `BLACKLIST_REGION_FRAGMENTS` | integer | No | Number of fragments overlapping blacklisted regions |
| `BLACKLIST_RATIO` | float | No | Ratio of reads in blacklist regions |
| `PEAK_REGION_FRAGMENTS` | integer | No | Number of fragments overlapping peaks. Sanity check - must be <= PASSED_FILTERS (Level 2). |
| `PEAK_REGION_CUTSITES` | integer | No | Total number of Tn5 insertion cutsites falling within peak regions (equal to 2 x PEAK_REGION_FRAGMENTS for paired-end sequencing). |
| `NUCLEOSOME_SIGNAL` | float | No | Nucleosome signal score (strength of the nucleosome signal per cell, computed as the ratio of fragments between 147 bp and 294 bp (mononucleosome) to fragments < 147 bp (nucleosome-free)) |
| `NUCLEOSOME_PERCENTILE` | float | No | Percentile rank of nucleosome score |
| `PERCENTAGE_READS_IN_PEAKS` | float | Yes | Percentage of reads in peaks |
| `SEURAT_CLUSTERS` | string | No | Clusters of cells by a shared nearest neighbor (SNN) modularity optimization based clustering algorithm |
| `N_COUNT_RNA` | integer | No | Total number of fragments in genes |
| `N_FEATURE_RNA` | integer | No | Number of genes detected in cell |
| `PEAKS_CALLING_SOFTWARE` | string | Yes | Generic name of peaks calling tool |
| `MEDIAN_FRACTION_OF_READS_IN_PEAKS` | float | Yes | Median fraction of reads in peaks (FRIP) |
| `ATAC_GENE_ACTIVITY_WORKFLOW_TYPE` | [ATACGeneActivityWorkflowTypeEnum](#atacgeneactivityworkflowtypeenum) | Yes | Generic name for the workflow used to analyze a data set |
| `ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION` | string | Yes | Parameters used to run the scATAC-seq workflow. |
| `CELL_TOTAL` | integer | Yes | Number of sequenced cells |
| `ANNDATA_SCHEMA_VERSION` | string | Yes | Version of AnnData schema (must be 0.1 for CellxGene compliance) |
| `ANNDATA_STRUCTURE_VALIDATED` | boolean | Yes | Whether the h5ad file structure has been validated against AnnData 0.1 schema |
| `GENOMIC_REFERENCE` | [GenomicReferenceEnum](#genomicreferenceenum) | Yes | Genomic or transcriptomic reference assembly used for alignment. If your genome reference is not among the valid values, please contact your data liaison. |
| `GENOMIC_REFERENCE_URL` | string | Yes | URL to genomic or transcriptomic reference |
| `GENOME_ANNOTATION_URL` | string | Yes | URL to genome or transcriptome annotation |
| `WORKFLOW_VERSION` | string | Yes | Major version of the workflow, or 'Not applicable' when no workflow version applies. |
| `WORKFLOW_LINK` | string | Yes | Link to workflow or command. DockStore.org recommended |
| `LIBRARY_LAYOUT` | [LibraryLayoutEnum](#librarylayoutenum) | Yes | Library layout (paired-end or single-end) |
| `SEQUENCING_PLATFORM` | [SequencingPlatformEnum](#sequencingplatformenum) | Yes | Sequencing platform used |
| `SEQUENCING_BATCH_ID` | string | No | Sequencing batch identifier |
| `LIBRARY_PREPARATION_DAYS_FROM_INDEX` | integer | No | Number of days between when the sample for assay was received in the lab and the libraries were prepared for sequencing. If not applicable please enter 'Not Applicable') |
| `TECHNICAL_REPLICATE_GROUP` | string | No | Technical replicate group identifier |
| `PROTOCOL_LINK` | string | No | Link to sequencing protocol |
| `CHECKSUM` | string | No | Checksum for data integrity verification |
| `HTAN_DATA_FILE_ID` | string | Yes | HTAN Data File ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID(s) - Foreign key(s) to parent entity (B for Biospecimen, D for data file). One or more IDs; for aggregated files provide multiple. Each ID must have B or D suffix. Supports HTA200-229 for phase 2. |

## Enums

### ATACGeneActivityWorkflowTypeEnum

Generic name for the workflow used to analyze a single-cell ATAC-seq dataset

| Value | Description |
|-------|-------------|
| ArchR | ArchR single-cell ATAC-seq analysis workflow |
| Cell Ranger ATAC | 10x Genomics Cell Ranger ATAC workflow |
| Cicero | Cicero chromatin accessibility and co-accessibility analysis workflow |
| MAESTRO | MAESTRO single-cell ATAC-seq and multi-omics analysis workflow |
| Other | Other workflow type |
| Signac | Signac single-cell chromatin accessibility analysis workflow |
| SnapATAC2 | SnapATAC2 single-cell ATAC-seq analysis workflow |

### DissociationMethodEnum

| Value | Description |
|-------|-------------|
| Enzymatic | Enzymatic dissociation method |
| Mechanical | Mechanical dissociation method |
| Other | Other dissociation method |
| Unknown | Unknown dissociation method |

### GenomicReferenceEnum

Genomic or transcriptomic reference assembly used for alignment

| Value | Description |
|-------|-------------|
| GRCh37 | Genome Reference Consortium human build 37 |
| GRCh37.p13 | GRCh37 patch release 13 |
| GRCh38 | Genome Reference Consortium human build 38 |
| GRCh38.p13 | GRCh38 patch release 13 |
| GRCh38.p14 | GRCh38 patch release 14 |
| hg19 | UCSC human genome reference hg19 |
| hg38 | UCSC human genome reference hg38 |

### LibraryConstructionMethodEnum

| Value | Description |
|-------|-------------|
| 10X Genomics | 10X Genomics library construction method |
| Drop-seq | Drop-seq library construction method |
| Fluidigm C1 | Fluidigm C1 library construction method |
| InDrop | InDrop library construction method |
| Other | Other library construction method |
| Smart-seq | Smart-seq library construction method |
| Unknown | Unknown library construction method |

### LibraryLayoutEnum

| Value | Description |
|-------|-------------|
| Paired-end | Paired-end sequencing |
| Single-end | Single-end sequencing |

### NucleicAcidSourceEnum

| Value | Description |
|-------|-------------|
| DNA | DNA nucleic acid source |
| RNA | RNA nucleic acid source |
| Unknown | Unknown nucleic acid source |

### ReverseTranscriptionPrimerEnum

| Value | Description |
|-------|-------------|
| Oligo-dT | Oligo-dT reverse transcription primer |
| Random Hexamer | Random hexamer reverse transcription primer |
| Unknown | Unknown reverse transcription primer |

### SequencingPlatformEnum

| Value | Description |
|-------|-------------|
| ABI_SOLID | ABI SOLID sequencing platform |
| BGISEQ | BGI sequencing platform |
| CAPILLARY | Capillary sequencing platform |
| COMPLETE_GENOMICS | Complete Genomics sequencing platform |
| HELICOS | Helicos sequencing platform |
| ILLUMINA | Illumina sequencing platform |
| ION_TORRENT | Ion Torrent sequencing platform |
| LS454 | 454 sequencing platform |
| OXFORD_NANOPORE | Oxford Nanopore sequencing platform |
| PACBIO_SMRT | PacBio SMRT sequencing platform |

### SequencingReadEnum

Content type of a single-cell ATAC-seq sequencing read

| Value | Description |
|-------|-------------|
| Cell Barcode | Sequencing read containing the cellular barcode sequence used to identify individual nuclei or cells |
| Cell Barcode and DNA Insert | Sequencing read containing both the cellular barcode sequence and the captured DNA insert sequence |
| DNA Insert | Sequencing read containing the genomic DNA fragment captured during the transposition reaction |
| Sample Index | Sequencing read containing the sample index (i7/i5 index) sequence used for sample identification and multiplexing |
| Sample Index and DNA Insert | Sequencing read containing both the sample index sequence and the captured genomic DNA insert sequence |

### SingleCellIsolationMethodEnum

| Value | Description |
|-------|-------------|
| Cell Sorting | Cell sorting isolation method |
| Droplet-based | Droplet-based isolation method |
| Manual Picking | Manual picking isolation method |
| Microfluidics | Microfluidics isolation method |
| Other | Other isolation method |
| Unknown | Unknown isolation method |

### SingleNucleusBufferEnum

Buffer used for single-nucleus preparation prior to transposition

| Value | Description |
|-------|-------------|
| 10x | Single-nucleus preparation buffer used in the 10x Genomics single-cell ATAC-seq or multiome workflow |
| NIB | Nuclei isolation buffer used for preparation of isolated nuclei prior to single-cell chromatin accessibility profiling |
| Omni | Omni assay buffer used for single-nucleus chromatin accessibility profiling workflows |
| TST | TST buffer used for single-nucleus preparation and transposition-based chromatin accessibility assays |

### SpikeInEnum

| Value | Description |
|-------|-------------|
| ERCC | ERCC spike-in |
| None | No spike-in |
| Other | Other spike-in |
| Unknown | Unknown spike-in |

### TranspositionReactionEnum

Transposase chemistry used in the transposition reaction

| Value | Description |
|-------|-------------|
| Diagenode-loaded Apex-Bio | Transposition reaction performed using Diagenode-loaded Tn5 transposase supplied by Apex-Bio |
| Diagenode-unloaded Apex-Bio | Transposition reaction performed using Diagenode Tn5 transposase with user-loaded adapters supplied by Apex-Bio |
| EZ-Tn5 | Transposition reaction performed using EZ-Tn5 transposase-based chemistry |
| In-House | Custom transposition reaction developed or performed using an internally established protocol |
| Nextera Tn5 | Transposition reaction performed using Nextera Tn5 transposase chemistry from Illumina |
| Tn5 | Transposition reaction performed using Tn5 transposase-based chromatin accessibility assay chemistry |
| Tn5-059 | Transposition reaction performed using Tn5-059 transposase variant chemistry |
