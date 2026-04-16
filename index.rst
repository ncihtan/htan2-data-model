HTAN Phase 2 Data Model
========================

Documentation for the HTAN Phase 2 Data Model.

All HTAN Centers are required to encode their data and metadata in a common HTAN Data Model. The HTAN Data Model is created via a community Request for Comment (RFC) process, with participation from all HTAN Centers, and covers clinical, biospecimen, genomic, transcriptomic, proteomic, imaging and spatial profiling data.

This documentation describes the HTAN data model, including required metadata attributes for each assay type. To annotate metadata or submit data, use `Curator <https://docs.synapse.org/synapse-docs/managing-metadata-with-curator>`_.

Each module page is self-contained and lists all attributes you need to fill out, including inherited attributes from base modules.

---

Getting Started
---------------

First, determine whether your data is **file-based** or **record-based**:

**Record-Based Data**
   If you have clinical or biospecimen data (patient records, sample metadata), use:

   - :doc:`Clinical <docs/clinical>` — Clinical and demographic data
   - :doc:`Biospecimen <docs/biospecimen>` — Biospecimen metadata and classification

**File-Based Data**
   If you have sequencing, imaging, or other file-based assay data, each module page shows
   **all required attributes** including inherited core attributes:

   - :doc:`WES <docs/wes>` — Bulk Whole Exome Sequencing
   - :doc:`scRNA-seq <docs/scrna-seq>` — Single-cell RNA sequencing
   - :doc:`Digital Pathology <docs/digitalpathology>` — Whole-slide imaging
   - :doc:`Multiplex Microscopy <docs/multiplexmicroscopy>` — Multiplexed tissue imaging
   - :doc:`Spatial Omics <docs/spatialomics>` — Spatial omics assays
   - :doc:`Imaging <docs/imaging>` — Radiological and other imaging modalities

---

Modules
-------

.. grid:: 2 2 3 3
   :gutter: 3

   .. grid-item-card:: 🏥 Clinical
      :link: docs/clinical
      :link-type: doc

      Demographics, diagnoses, treatments, follow-up, and molecular tests.

   .. grid-item-card:: 🧪 Biospecimen
      :link: docs/biospecimen
      :link-type: doc

      Tissue collection, biospecimen processing, and aliquot metadata.

   .. grid-item-card:: 🧬 WES
      :link: docs/wes
      :link-type: doc

      Bulk whole exome sequencing — raw reads through somatic variant calls.

   .. grid-item-card:: 🔬 scRNA-seq
      :link: docs/scrna-seq
      :link-type: doc

      Single-cell RNA sequencing data files and quality metrics.

   .. grid-item-card:: 📍 Spatial Omics
      :link: docs/spatialomics
      :link-type: doc

      Spatially resolved transcriptomics and proteomics assay metadata.

   .. grid-item-card:: 🔵 Multiplex Microscopy
      :link: docs/multiplexmicroscopy
      :link-type: doc

      Cyclic immunofluorescence and multiplexed imaging protocols.

   .. grid-item-card:: 🖼 Digital Pathology
      :link: docs/digitalpathology
      :link-type: doc

      Whole slide imaging and digital pathology file metadata.

   .. grid-item-card:: 📷 Imaging
      :link: docs/imaging
      :link-type: doc

      Radiological and other non-pathology imaging modalities.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Modules

   docs/clinical
   docs/biospecimen
   docs/wes
   docs/scrna-seq
   docs/digitalpathology
   docs/multiplexmicroscopy
   docs/spatialomics
   docs/imaging
