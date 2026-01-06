# Biospecimen

HTAN Biospecimen Data Model Schema

## Classes

### BiospecimenData

Container for all Biospecimen data

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `ACQUISITION_METHOD_OTHER_SPECIFY` | string | No | A custom acquisition method |
| `ACQUISITION_METHOD_TYPE` | See [AcquisitionMethodTypeEnum](#acquisitionmethodtype) enum below | Yes | Records the method of acquisition or source for the specimen under consideration |
| `ADJACENT_BIOSPECIMEN_IDS` | string | No | List of HTAN Identifiers (separated by commas) of adjacent biospecimens cut from the same sample |
| `AGE_IN_DAYS_AT_SECTIONING` | integer | No | The age in days of a subject when a specimen tissue block was sectioned |
| `AGE_IN_DAYS_AT_SPECIMEN_COLLECTION` | integer | Yes | The age in days of the subject at the time of specimen collection |
| `AGE_IN_DAYS_AT_SPECIMEN_PROCESSING` | integer | Yes | The age in days of a subject when a specimen was processed |
| `ANALYTE_TYPE` | See [AnalyteTypeEnum](#analytetype) enum below | No | The sample or material being subjected to analysis |
| `BIOSPECIMEN_TYPE` | See [BiospecimenTypeEnum](#biospecimentype) enum below | Yes | Biospecimen Type |
| `DEGREE_OF_DYSPLASIA` | DegreeOfDysplasiaEnum<br/>`1`, `2`, `3`, `99` | No | Information related to the presence of cells that look abnormal under a microscope but are not cancer |
| `FIXATION_DURATION_IN_MINUTES` | integer | No | The length of time, from beginning to end, required to process or preserve biospecimens in fixative |
| `HTAN_BIOSPECIMEN_ID` | string | Yes | HTAN Biospecimen ID (Primary Key) |
| `HTAN_PARENT_ID` | string | Yes | HTAN Parent ID - Foreign Key to parent entity (Participant ID or Biospecimen ID with B suffix). Supports HTA200-229 for phase 2. |
| `ICD_10_DISEASE_CODE` | See [Icd10DiseaseEnum](#icd10disease) enum below | No | For coding precancerous lesions: The diagnosis, in humans, as captured in the 2022 extension of ICD-10-CM |
| `ICD_O_3_TISSUE_MORPHOLOGY` | See [IcdO3MorphologyEnum](#icdo3morphology) enum below | No | The microscopic anatomy of normal and abnormal cells and tissues of the specimen as captured in the morphology codes of ICD-O-3 |
| `LONGEST_DIMENSION` | decimal | No | Numeric value that represents the longest dimension of the sample, measured in millimeters |
| `METHOD_OF_NUCLEIC_ACID_ISOLATION` | string | No | Bulk RNA & DNA-seq specific: method used for nucleic acid isolation |
| `PERCENT_NECROSIS` | decimal | No | Numeric value to represent the percentage of cell death in a malignant tumor sample or specimen |
| `PERCENT_NORMAL_CELLS` | decimal | No | Numeric value to represent the percentage of normal cell content in a malignant tumor sample or specimen |
| `PERCENT_TUMOR_CELLS` | decimal | No | Numeric value that represents the percentage of infiltration by tumor cells in a sample |
| `PERCENT_TUMOR_NUCLEI` | decimal | No | Numeric value to represent the percentage of tumor nuclei in a malignant neoplasm sample or specimen |
| `PRESERVATION_MEDIUM` | See [PreservationMediumEnum](#preservationmedium) enum below | Yes | The kind of substance holding another substance in solution or suspension to maintain a specimen in a viable state |
| `PRESERVATION_METHOD` | See [PreservationMethodEnum](#preservationmethod) enum below | Yes | Method used to preserve the sample |
| `PRESERVATION_METHOD_TEMPERATURE` | See [PreservationTemperatureEnum](#preservationtemperature) enum below | Yes | The term which describes the temperature used to maintain the specimen in a viable state |
| `PROCESSING_LOCATION` | string | No | Site with an HTAN center where specimen processing occurs |
| `SECTION_NUMBER_IN_SEQUENCE` | integer | No | Numeric value (integer, including ranges) provided to a sample in a series of sections |
| `SECTION_THICKNESS_VALUE` | decimal | No | Numeric value to describe the thickness of a slice to tissue taken from a biospecimen, measured in microns |
| `SHIPPING_CONDITION_TYPE` | See [ShippingConditionEnum](#shippingcondition) enum below | Yes | Text descriptor of the shipping environment of a biospecimen |
| `SHORTEST_DIMENSION` | decimal | No | Numeric value that represents the shortest dimension of the sample, measured in millimeters |
| `SITE_DATA_SOURCE` | string | No | Text to identify the data source for the specimen/sample from within the HTAN center |
| `SITE_OF_RESECTION_OR_BIOPSY` | See [tissue_or_organ_of_origin_uberon_enum](#tissue-or-organ-of-origin-uberon-) enum below | Yes | The location within the body from where the disease of interest originated as captured in the Uberon identifier |
| `SLICING_METHOD` | See [SlicingMethodEnum](#slicingmethod) enum below | No | Imaging specific: the method by which the tissue was sliced |
| `SLIDE_CHARGE_TYPE` | See [SlideChargeTypeEnum](#slidechargetype) enum below | No | A description of the charge on the glass slide |
| `SPECIMEN_CELLULAR_ARCHITECTURE` | See [CellularArchitectureEnum](#cellulararchitecture) enum below | Yes | The architectural pattern of an abnormal, normal, or mixed cellular population in a tissue specimen |
| `SPECIMEN_LATERALITY` | See [SpecimenLateralityEnum](#specimenlaterality) enum below | Yes | For tumors in paired organs, designates the side on which the specimen was obtained |
| `TIMEPOINT` | See [TimepointEnum](#timepoint) enum below | No | A specific point in the time continuum, including those established relative to an event |
| `TISSUE_SAMPLE_TYPE` | TissueSampleTypeEnum<br/>`Tissue Block`, `Tissue Section` | No | The type of preserved sample material removed for testing, diagnostic, propagation, treatment or research purposes |
| `TUMOR_CLASSIFICATION` | See [TumorClassificationEnum](#tumorclassification) enum below | No | The classification of a tumor at a particular time based primarily on histopathological characteristics |

## Slots

| Slot | Type | Required | Description |
|------|------|----------|-------------|
| `caDSR_id` | string | No | The caDSR identifier for this element |

