# HTAN scATAC-seq Module

LinkML data model for HTAN Phase 2 single-cell ATAC-seq (scATAC-seq) assay data.

## Levels

| Level | Class | Description |
|---|---|---|
| 1 | `scATACLevel1` | Raw sequencing files (fastq/fastq.gz) and single-nucleus preparation metadata |
| 2 | `scATACLevel2` | Aligned data (bam/cram) and alignment QC metrics |
| 3 / 4 | `scATACLevel3and4` | Peak-by-cell matrices, fragment files (h5ad/bed), and chromatin accessibility metrics |

## Inheritance

Levels follow the shared HTAN sequencing hierarchy:

```
CoreFileAttributes
  └─ BaseSequencingAttributes
       └─ BaseSequencingLevel1Attributes  ← scATACLevel1
            └─ BaseSequencingLevel2Attributes  ← scATACLevel2
                 └─ BaseSequencingLevel3Attributes  ← scATACLevel3and4
```

Single-cell preparation attributes (isolation/dissociation method, nucleic acid
source, etc.) and the AnnData 0.1 compliance attributes are conceptually shared
with the scRNA-seq module but defined locally to keep this module self-contained.

## Source

Generated from `RFC_ HTAN Phase 2 scATAC-seq Model_WithDetail.xlsx` (data model
v1.5.0). Edit the source YAML under `domains/`; generated Python/JSON artifacts are
produced by `make gen-schema` in a separate downstream PR.

## Build

```sh
make -C modules/scATAC-seq gen-schema   # generate Python + JSON schema
make -C modules/scATAC-seq test         # run module tests
```
