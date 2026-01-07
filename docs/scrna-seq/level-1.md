# scRNA-seq - Level 1

HTAN scRNA-seq Level 1 Data Model - Raw sequencing files and metadata

**scRNA-seq Level 1 data - Raw sequencing files and metadata**

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

