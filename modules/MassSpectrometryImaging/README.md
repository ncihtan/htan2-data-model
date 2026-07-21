# HTAN Mass Spectrometry Imaging (MSI)

LinkML schema for HTAN Phase 2 Mass Spectrometry Imaging, implementing the
*HTAN Phase 2 — Mass Spectrometry Imaging (MSI)* RFC (v1.3).

## Purpose

MSI is a spatial molecular profiling modality that produces spatially resolved,
label-free detection of lipids, metabolites, peptides, and proteins directly from
tissue. Like spatial transcriptomics, MSI inherits from `CoreFileAttributes`
(not `BaseImagingAttributes`).

## Structure

A 4-level hierarchy plus a per-channel RecordSet companion:

| File | Class | Level |
|---|---|---|
| `domains/level_1.yaml` | `MassSpectrometryImagingLevel1` | Raw continuous/profile imzML acquisition annotations |
| `domains/level_2.yaml` | `MassSpectrometryImagingLevel2` | Processed centroided imzML processing + QC annotations |
| `domains/level_3.yaml` | `MassSpectrometryImagingLevel3` | Annotation-filtered OME-TIFF summary annotations |
| `domains/level_4.yaml` | `MassSpectrometryImagingLevel4` | Segmentation / region quantification (optional) |
| `domains/molecular_assignments.yaml` | `MolecularAssignment` | Molecular Assignments RecordSet (one row per OME-TIFF channel) |
| `domains/mass_spectrometry_imaging.yaml` | `MassSpectrometryImagingData` | Container importing all of the above |

Each level class is `is_a: CoreFileAttributes` (flat pattern, mirroring SpatialOmics).
Attributes propagate downward at query time via `HTAN_PARENT_ID` — **not** via LinkML
inheritance — so each level defines only its own new attributes. `PASSED_QC`,
`QC_COMMENT`, `SOFTWARE_AND_VERSION`, and `PROTOCOL_LINK` are re-specified per level.

The `MolecularAssignment` row class does **not** inherit `CoreFileAttributes`
(like `ChannelMetadata` in Multiplex Microscopy); it is wired into the container
with `multivalued: true` + `inlined_as_list: true`.

## Validation highlights

- The four matrix-prep fields (`PREPARATION_MATRIX`, `MATRIX_DEPOSITION_METHOD`,
  `PREPARATION_INSTRUMENT_VENDOR`, `PREPARATION_INSTRUMENT_MODEL`) are conditionally
  required for matrix-based (MALDI-family) techniques: `MALDI`, `MALDI_2`, `IR_MALDESI`.
  IR-MALDESI uses `OTHER` for `PREPARATION_MATRIX` (ice/endogenous-water matrix).
- `ANALYTE_CLASS` is multivalued.
- `SPECTRUM_TYPE` is fixed to `PROFILE` at Level 1.
- The Molecular Assignments columns are gated on `CONFIDENCE_LEVEL` (1–4) via rules.
- Fixed-unit slots encode the unit in the name (`_UM` = micrometers, `_PPM` = parts-per-million)
  and are self-documenting; a companion `_UNIT` slot is used only where the unit genuinely
  varies (e.g. `TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE` / `_UNIT`, hours vs days).

Cross-row constraints (channel count = RecordSet row count; `(HTAN_DATA_FILE_ID,
CHANNEL_INDEX)` uniqueness; imzML continuous@L1 / centroided@L2) are enforced by the
DCC validator, not the schema.

## Testing

```bash
cd modules/MassSpectrometryImaging
make test
```

The suite is schema-introspection only (via `SchemaView`): it covers class structure,
inheritance, required/optional slots per level, enum ordering/descriptions, and the
conditional rules. **Valid/invalid instance tests are intentionally deferred** to the
downstream `make modules-gen` PR, because instantiating classes and exercising bad
enum values requires the generated Python dataclasses (not produced in the schema PR).

## Schema generation

Generated artifacts (Python dataclasses, JSON schemas) are produced in a separate
downstream PR:

```bash
cd modules/MassSpectrometryImaging
make gen-schema
```
