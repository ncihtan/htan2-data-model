# HTAN Data Model

The **Human Tumor Atlas Network (HTAN)** data model defines the metadata schema
for all HTAN data submissions. Schemas are authored in
[LinkML](https://linkml.io) and cover clinical metadata, biospecimens, and
assay-specific data files across multiple levels of processing.

---

## Modules

<div class="grid cards" markdown>

-   :material-hospital-box:{ .lg .middle } **Clinical**
    ---
    Demographics, diagnoses, treatments, follow-up, and molecular tests.

    [:octicons-arrow-right-24: View schema](clinical.md)

-   :material-test-tube:{ .lg .middle } **Biospecimen**
    ---
    Tissue collection, biospecimen processing, and aliquot metadata.

    [:octicons-arrow-right-24: View schema](biospecimen.md)

-   :material-dna:{ .lg .middle } **WES**
    ---
    Whole exome sequencing: raw reads through somatic variant calls.

    [:octicons-arrow-right-24: View schema](wes.md)

-   :material-bacteria:{ .lg .middle } **scRNA-seq**
    ---
    Single-cell RNA sequencing data files and quality metrics.

    [:octicons-arrow-right-24: View schema](scrna-seq.md)

-   :material-map-marker-radius:{ .lg .middle } **Spatial Omics**
    ---
    Spatially resolved transcriptomics and proteomics assay metadata.

    [:octicons-arrow-right-24: View schema](spatialomics.md)

-   :material-dots-grid:{ .lg .middle } **Multiplex Microscopy**
    ---
    Cyclic immunofluorescence and other multiplexed imaging protocols.

    [:octicons-arrow-right-24: View schema](multiplexmicroscopy.md)

-   :material-microscope:{ .lg .middle } **Digital Pathology**
    ---
    Whole slide imaging and digital pathology file metadata.

    [:octicons-arrow-right-24: View schema](digitalpathology.md)

-   :material-image:{ .lg .middle } **Imaging**
    ---
    Radiological and other non-pathology imaging modalities.

    [:octicons-arrow-right-24: View schema](imaging.md)

</div>

---

## Reference

<div class="grid cards" markdown>

-   :material-alphabetical:{ .lg .middle } **Vocabulary (Enums)**
    ---
    All controlled vocabulary terms used across modules — searchable by value or
    description.

    [:octicons-arrow-right-24: Browse enums](enums.md)

-   :material-table:{ .lg .middle } **Slot Index**
    ---
    Every metadata field across all modules in one searchable table.

    [:octicons-arrow-right-24: Browse slots](slots.md)

</div>

---

## Resources

- [HTAN Portal](https://humantumoratlas.org)
- [GitHub Repository](https://github.com/ncihtan/htan2-data-model)
- [LinkML Documentation](https://linkml.io/linkml/)
- [Synapse](https://www.synapse.org)
