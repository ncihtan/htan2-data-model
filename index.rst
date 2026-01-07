HTAN Phase 2 Data Model
========================

Documentation for the HTAN Phase 2 Data Model.

This documentation provides comprehensive information about each module in the HTAN Phase 2 Data Model, including module overviews, usage instructions, and complete schema documentation with all attributes, classes, and enums.

Data Model Architecture
------------------------

The HTAN2 data model is built using **LinkML**, a modeling language for schemas that generates Python data model classes and JSON schemas. The model follows a modular architecture with clear separation of concerns:

.. image:: modules/CoreFile/core_file_inheritance.png
   :alt: HTAN2 Module Inheritance Diagram

The diagram above illustrates the separation between **Record-Based Modules** (Clinical, Biospecimen) and **File-Based Modules** (WES, Digital Pathology, etc.), with the **Core File Module** providing universal attributes for all file-based modules.

Core File Module
~~~~~~~~~~~~~~~~

- **Purpose**: Universal attributes shared across all file-based modules
- **Location**: `modules/CoreFile/domains/core.yaml`
- **Key Features**: 
  - Single primary key definition (`HTAN_DATA_FILE_ID`)
  - Required field definitions for relationships
  - HTAN identifier validation patterns
  - Base class for inheritance (`CoreFileAttributes`)

Clinical Module
~~~~~~~~~~~~~~~

- **Purpose**: Clinical and demographic data
- **Location**: `modules/Clinical/`
- **Structure**: Multiple domain files (demographics, diagnosis, therapy, etc.)

Biospecimen Module
~~~~~~~~~~~~~~~~~~

- **Purpose**: Comprehensive biospecimen metadata and classification
- **Location**: `modules/Biospecimen/`
- **Structure**: 18 domain-specific enum files with medical classifications

Sequencing Module
~~~~~~~~~~~~~~~~~

- **Purpose**: Base sequencing attributes shared across all sequencing types
- **Location**: `modules/Sequencing/`
- **Structure**: BaseSequencingAttributes class with common sequencing metadata

WES Module
~~~~~~~~~~

- **Purpose**: Bulk Whole Exome Sequencing data
- **Location**: `modules/WES/`
- **Structure**: Three processing levels (Level 1, 2, 3)

scRNA-seq Module
~~~~~~~~~~~~~~~~

- **Purpose**: Single-cell RNA sequencing data
- **Location**: `modules/scRNA-seq/`
- **Structure**: Three data levels (Level 1, 2, 3/4) with h5ad format validation

Imaging Module
~~~~~~~~~~~~~~

- **Purpose**: Base imaging attributes shared across all imaging modules
- **Location**: `modules/Imaging/`
- **Structure**: BaseImagingAttributes class with common imaging metadata

Digital Pathology Module
~~~~~~~~~~~~~~~~~~~~~~~~

- **Purpose**: Whole-slide imaging (WSI) data from H&E and other tissue-based assays
- **Location**: `modules/DigitalPathology/`
- **Structure**: Single data level (Level 2) with Bio-Formats/OpenSlide compatible formats

Multiplex Microscopy Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **Purpose**: Multiplexed tissue imaging assays (CODEX, CyCIF, IMC, MIBI, etc.)
- **Location**: `modules/MultiplexMicroscopy/`
- **Structure**: Three data levels (Level 2: imaging + channel metadata, Level 3: segmentation masks, Level 4: cell-by-feature tables)

Spatial Omics Module
~~~~~~~~~~~~~~~~~~~~

- **Purpose**: Sequencing-based and sequence-hybridization spatial omics assays (Visium, Xenium, CosMx, STOmics, etc.)
- **Location**: `modules/SpatialOmics/`
- **Structure**: Four data levels (Level 1: raw data bundle optional, Level 3: processed bundle required, Level 4: interoperable file optional, Panel: panel information)

Modules
-------

.. toctree::
   :maxdepth: 2
   :caption: Data Model Modules:

   docs/clinical
   docs/biospecimen
   docs/corefile
   docs/sequencing
   docs/wes
   docs/scrna-seq
   docs/imaging
   docs/digitalpathology
   docs/multiplexmicroscopy
   docs/spatialomics

