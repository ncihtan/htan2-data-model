HTAN Phase 2 Data Model
========================

Documentation for the HTAN Phase 2 Data Model.

All HTAN Centers are required to encode their data and metadata in a common HTAN Data Model. The HTAN Data Model is created via a community Request for Comment (RFC) process, with participation from all HTAN Centers, and covers clinical, biospecimen, genomic, transcriptomic, proteomic, imaging and spatial profiling data.

This documentation describes the HTAN data model, including required metadata attributes for each assay type. To annotate metadata or submit data, use `Curator <https://curator.htan.org>`_.

This documentation provides comprehensive information about each module in the HTAN Phase 2 Data Model. Each module page lists **all attributes you need to fill out**, including inherited attributes from base modules.

Getting Started
---------------

First, determine whether your data is **file-based** or **record-based**:

**Record-Based Data**
   If you have clinical or biospecimen data (patient records, sample metadata), use:
   
   - :doc:`Clinical <docs/clinical>` - Clinical and demographic data
   - :doc:`Biospecimen <docs/biospecimen>` - Biospecimen metadata and classification

**File-Based Data**
   If you have sequencing, imaging, or other file-based data, use one of the following modules. Each module page shows **all required attributes** including inherited core attributes:
   
   - :doc:`WES <docs/wes>` - Bulk Whole Exome Sequencing (includes Core File + Base Sequencing + WES attributes)
   - :doc:`scRNA-seq <docs/scrna-seq>` - Single-cell RNA sequencing (includes Core File + Base Sequencing + scRNA-seq attributes)
   - :doc:`Digital Pathology <docs/digitalpathology>` - Whole-slide imaging (includes Core File + Base Imaging + Digital Pathology attributes)
   - :doc:`Multiplex Microscopy <docs/multiplexmicroscopy>` - Multiplexed tissue imaging (includes Core File + Base Imaging + Multiplex Microscopy attributes)
   - :doc:`Spatial Omics <docs/spatialomics>` - Spatial omics assays (includes Core File + Spatial Omics attributes)

Each module page is self-contained and lists all attributes you need to fill out, so you don't need to navigate between multiple pages.

Reference
----------

.. toctree::
   :maxdepth: 2
   :caption: Reference:

   :self:
   docs/identifiers

Modules
-------

.. toctree::
   :maxdepth: 3
   :caption: Data Model Modules:

   docs/clinical
   docs/biospecimen
   docs/wes
   docs/wes/level-1
   docs/wes/level-2
   docs/wes/level-3
   docs/scrna-seq
   docs/scrna-seq/level-1
   docs/scrna-seq/level-2
   docs/scrna-seq/level-3-4
   docs/digitalpathology
   docs/multiplexmicroscopy
   docs/multiplexmicroscopy/level-2
   docs/multiplexmicroscopy/level-3
   docs/multiplexmicroscopy/level-4
   docs/spatialomics
   docs/spatialomics/level-1
   docs/spatialomics/level-3
   docs/spatialomics/level-4
   docs/spatialomics/panel

