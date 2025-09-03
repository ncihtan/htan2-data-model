# Auto generated from scrna_seq.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-27T14:51:48
# Schema: scRNA-seq
#
# id: https://w3id.org/htan/scrna_seq
# description: HTAN scRNA-seq Data Model - Single-cell RNA sequencing data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = HTAN


# Types

# Class references
class CoreFileAttributesHTANDATAFILEID(extended_str):
    pass


class BiospecimenAttributesHTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class BaseSequencingAttributesHTANDATAFILEID(BiospecimenAttributesHTANDATAFILEID):
    pass


class ScRNALevel1HTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


class ScRNALevel2HTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


class ScRNALevel34HTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


@dataclass(repr=False)
class ScRNAseqData(YAMLRoot):
    """
    Root class for scRNA-seq data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScRNAseqData"]
    class_class_curie: ClassVar[str] = "htan:ScRNAseqData"
    class_name: ClassVar[str] = "scRNAseqData"
    class_model_uri: ClassVar[URIRef] = HTAN.ScRNAseqData

    level1_data: Optional[Union[str, ScRNALevel1HTANDATAFILEID]] = None
    level2_data: Optional[Union[str, ScRNALevel2HTANDATAFILEID]] = None
    level3_4_data: Optional[Union[str, ScRNALevel34HTANDATAFILEID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.level1_data is not None and not isinstance(self.level1_data, ScRNALevel1HTANDATAFILEID):
            self.level1_data = ScRNALevel1HTANDATAFILEID(self.level1_data)

        if self.level2_data is not None and not isinstance(self.level2_data, ScRNALevel2HTANDATAFILEID):
            self.level2_data = ScRNALevel2HTANDATAFILEID(self.level2_data)

        if self.level3_4_data is not None and not isinstance(self.level3_4_data, ScRNALevel34HTANDATAFILEID):
            self.level3_4_data = ScRNALevel34HTANDATAFILEID(self.level3_4_data)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoreFileAttributes(YAMLRoot):
    """
    Universal attributes that apply to all file-based data in HTAN
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["CoreFileAttributes"]
    class_class_curie: ClassVar[str] = "htan:CoreFileAttributes"
    class_name: ClassVar[str] = "CoreFileAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.CoreFileAttributes

    HTAN_DATA_FILE_ID: Union[str, CoreFileAttributesHTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, CoreFileAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = CoreFileAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.COMPONENT):
            self.MissingRequiredField("COMPONENT")
        if not isinstance(self.COMPONENT, str):
            self.COMPONENT = str(self.COMPONENT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.HTAN_PARENT_ID):
            self.MissingRequiredField("HTAN_PARENT_ID")
        if not isinstance(self.HTAN_PARENT_ID, str):
            self.HTAN_PARENT_ID = str(self.HTAN_PARENT_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiospecimenAttributes(CoreFileAttributes):
    """
    Attributes for modules that require biospecimen identification
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BiospecimenAttributes"]
    class_class_curie: ClassVar[str] = "htan:BiospecimenAttributes"
    class_name: ClassVar[str] = "BiospecimenAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BiospecimenAttributes

    HTAN_DATA_FILE_ID: Union[str, BiospecimenAttributesHTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BiospecimenAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BiospecimenAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.HTAN_BIOSPECIMEN_ID):
            self.MissingRequiredField("HTAN_BIOSPECIMEN_ID")
        if not isinstance(self.HTAN_BIOSPECIMEN_ID, str):
            self.HTAN_BIOSPECIMEN_ID = str(self.HTAN_BIOSPECIMEN_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseSequencingAttributes(BiospecimenAttributes):
    """
    Base attributes shared across all sequencing types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BaseSequencingAttributes"]
    class_class_curie: ClassVar[str] = "htan:BaseSequencingAttributes"
    class_name: ClassVar[str] = "BaseSequencingAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BaseSequencingAttributes

    HTAN_DATA_FILE_ID: Union[str, BaseSequencingAttributesHTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    SEQUENCING_BATCH_ID: Optional[str] = None
    LIBRARY_PREPARATION_DAYS_FROM_INDEX: Optional[int] = None
    TECHNICAL_REPLICATE_GROUP: Optional[str] = None
    PROTOCOL_LINK: Optional[str] = None
    WORKFLOW_LINK: Optional[str] = None
    GENOMIC_REFERENCE_URL: Optional[str] = None
    GENOME_ANNOTATION_URL: Optional[str] = None
    CHECKSUM: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BaseSequencingAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BaseSequencingAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.LIBRARY_LAYOUT):
            self.MissingRequiredField("LIBRARY_LAYOUT")
        if not isinstance(self.LIBRARY_LAYOUT, LibraryLayoutEnum):
            self.LIBRARY_LAYOUT = LibraryLayoutEnum(self.LIBRARY_LAYOUT)

        if self._is_empty(self.SEQUENCING_PLATFORM):
            self.MissingRequiredField("SEQUENCING_PLATFORM")
        if not isinstance(self.SEQUENCING_PLATFORM, SequencingPlatformEnum):
            self.SEQUENCING_PLATFORM = SequencingPlatformEnum(self.SEQUENCING_PLATFORM)

        if self._is_empty(self.WORKFLOW_VERSION):
            self.MissingRequiredField("WORKFLOW_VERSION")
        if not isinstance(self.WORKFLOW_VERSION, str):
            self.WORKFLOW_VERSION = str(self.WORKFLOW_VERSION)

        if self._is_empty(self.GENOMIC_REFERENCE):
            self.MissingRequiredField("GENOMIC_REFERENCE")
        if not isinstance(self.GENOMIC_REFERENCE, str):
            self.GENOMIC_REFERENCE = str(self.GENOMIC_REFERENCE)

        if self.SEQUENCING_BATCH_ID is not None and not isinstance(self.SEQUENCING_BATCH_ID, str):
            self.SEQUENCING_BATCH_ID = str(self.SEQUENCING_BATCH_ID)

        if self.LIBRARY_PREPARATION_DAYS_FROM_INDEX is not None and not isinstance(self.LIBRARY_PREPARATION_DAYS_FROM_INDEX, int):
            self.LIBRARY_PREPARATION_DAYS_FROM_INDEX = int(self.LIBRARY_PREPARATION_DAYS_FROM_INDEX)

        if self.TECHNICAL_REPLICATE_GROUP is not None and not isinstance(self.TECHNICAL_REPLICATE_GROUP, str):
            self.TECHNICAL_REPLICATE_GROUP = str(self.TECHNICAL_REPLICATE_GROUP)

        if self.PROTOCOL_LINK is not None and not isinstance(self.PROTOCOL_LINK, str):
            self.PROTOCOL_LINK = str(self.PROTOCOL_LINK)

        if self.WORKFLOW_LINK is not None and not isinstance(self.WORKFLOW_LINK, str):
            self.WORKFLOW_LINK = str(self.WORKFLOW_LINK)

        if self.GENOMIC_REFERENCE_URL is not None and not isinstance(self.GENOMIC_REFERENCE_URL, str):
            self.GENOMIC_REFERENCE_URL = str(self.GENOMIC_REFERENCE_URL)

        if self.GENOME_ANNOTATION_URL is not None and not isinstance(self.GENOME_ANNOTATION_URL, str):
            self.GENOME_ANNOTATION_URL = str(self.GENOME_ANNOTATION_URL)

        if self.CHECKSUM is not None and not isinstance(self.CHECKSUM, str):
            self.CHECKSUM = str(self.CHECKSUM)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScRNALevel1(BaseSequencingAttributes):
    """
    scRNA-seq Level 1 data - Raw sequencing files and metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScRNALevel1"]
    class_class_curie: ClassVar[str] = "htan:ScRNALevel1"
    class_name: ClassVar[str] = "scRNALevel1"
    class_model_uri: ClassVar[URIRef] = HTAN.ScRNALevel1

    HTAN_DATA_FILE_ID: Union[str, ScRNALevel1HTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    SINGLE_CELL_ISOLATION_METHOD: Union[str, "SingleCellIsolationMethodEnum"] = None
    DISSOCIATION_METHOD: Union[str, "DissociationMethodEnum"] = None
    NUCLEIC_ACID_SOURCE: Union[str, "NucleicAcidSourceEnum"] = None
    LIBRARY_CONSTRUCTION_METHOD: Union[str, "LibraryConstructionMethodEnum"] = None
    REVERSE_TRANSCRIPTION_PRIMER: Union[str, "ReverseTranscriptionPrimerEnum"] = None
    SPIKE_IN: Union[str, "SpikeInEnum"] = None
    READ_INDICATOR: Union[str, "ReadIndicatorEnum"] = None
    CRYOPRESERVED_CELLS_IN_SAMPLE: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ScRNALevel1HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ScRNALevel1HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.SINGLE_CELL_ISOLATION_METHOD):
            self.MissingRequiredField("SINGLE_CELL_ISOLATION_METHOD")
        if not isinstance(self.SINGLE_CELL_ISOLATION_METHOD, SingleCellIsolationMethodEnum):
            self.SINGLE_CELL_ISOLATION_METHOD = SingleCellIsolationMethodEnum(self.SINGLE_CELL_ISOLATION_METHOD)

        if self._is_empty(self.DISSOCIATION_METHOD):
            self.MissingRequiredField("DISSOCIATION_METHOD")
        if not isinstance(self.DISSOCIATION_METHOD, DissociationMethodEnum):
            self.DISSOCIATION_METHOD = DissociationMethodEnum(self.DISSOCIATION_METHOD)

        if self._is_empty(self.NUCLEIC_ACID_SOURCE):
            self.MissingRequiredField("NUCLEIC_ACID_SOURCE")
        if not isinstance(self.NUCLEIC_ACID_SOURCE, NucleicAcidSourceEnum):
            self.NUCLEIC_ACID_SOURCE = NucleicAcidSourceEnum(self.NUCLEIC_ACID_SOURCE)

        if self._is_empty(self.LIBRARY_CONSTRUCTION_METHOD):
            self.MissingRequiredField("LIBRARY_CONSTRUCTION_METHOD")
        if not isinstance(self.LIBRARY_CONSTRUCTION_METHOD, LibraryConstructionMethodEnum):
            self.LIBRARY_CONSTRUCTION_METHOD = LibraryConstructionMethodEnum(self.LIBRARY_CONSTRUCTION_METHOD)

        if self._is_empty(self.REVERSE_TRANSCRIPTION_PRIMER):
            self.MissingRequiredField("REVERSE_TRANSCRIPTION_PRIMER")
        if not isinstance(self.REVERSE_TRANSCRIPTION_PRIMER, ReverseTranscriptionPrimerEnum):
            self.REVERSE_TRANSCRIPTION_PRIMER = ReverseTranscriptionPrimerEnum(self.REVERSE_TRANSCRIPTION_PRIMER)

        if self._is_empty(self.SPIKE_IN):
            self.MissingRequiredField("SPIKE_IN")
        if not isinstance(self.SPIKE_IN, SpikeInEnum):
            self.SPIKE_IN = SpikeInEnum(self.SPIKE_IN)

        if self._is_empty(self.READ_INDICATOR):
            self.MissingRequiredField("READ_INDICATOR")
        if not isinstance(self.READ_INDICATOR, ReadIndicatorEnum):
            self.READ_INDICATOR = ReadIndicatorEnum(self.READ_INDICATOR)

        if self.CRYOPRESERVED_CELLS_IN_SAMPLE is not None and not isinstance(self.CRYOPRESERVED_CELLS_IN_SAMPLE, Bool):
            self.CRYOPRESERVED_CELLS_IN_SAMPLE = Bool(self.CRYOPRESERVED_CELLS_IN_SAMPLE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScRNALevel2(BaseSequencingAttributes):
    """
    scRNA-seq Level 2 data - Workflow and processing metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScRNALevel2"]
    class_class_curie: ClassVar[str] = "htan:ScRNALevel2"
    class_name: ClassVar[str] = "scRNALevel2"
    class_model_uri: ClassVar[URIRef] = HTAN.ScRNALevel2

    HTAN_DATA_FILE_ID: Union[str, ScRNALevel2HTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    SCRNASEQ_WORKFLOW_TYPE: Union[str, "ScRNAseqWorkflowTypeEnumLevel2"] = None
    WHITELIST_CELL_BARCODE_FILE_LINK: Optional[str] = None
    CELL_BARCODE_TAG: Optional[str] = None
    UMI_TAG: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ScRNALevel2HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ScRNALevel2HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.SCRNASEQ_WORKFLOW_TYPE):
            self.MissingRequiredField("SCRNASEQ_WORKFLOW_TYPE")
        if not isinstance(self.SCRNASEQ_WORKFLOW_TYPE, ScRNAseqWorkflowTypeEnumLevel2):
            self.SCRNASEQ_WORKFLOW_TYPE = ScRNAseqWorkflowTypeEnumLevel2(self.SCRNASEQ_WORKFLOW_TYPE)

        if self.WHITELIST_CELL_BARCODE_FILE_LINK is not None and not isinstance(self.WHITELIST_CELL_BARCODE_FILE_LINK, str):
            self.WHITELIST_CELL_BARCODE_FILE_LINK = str(self.WHITELIST_CELL_BARCODE_FILE_LINK)

        if self.CELL_BARCODE_TAG is not None and not isinstance(self.CELL_BARCODE_TAG, str):
            self.CELL_BARCODE_TAG = str(self.CELL_BARCODE_TAG)

        if self.UMI_TAG is not None and not isinstance(self.UMI_TAG, str):
            self.UMI_TAG = str(self.UMI_TAG)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScRNALevel34(BaseSequencingAttributes):
    """
    Single-cell RNA-seq Level 3 and 4 - Gene expression files and cell relationships
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScRNALevel34"]
    class_class_curie: ClassVar[str] = "htan:ScRNALevel34"
    class_name: ClassVar[str] = "scRNALevel3_4"
    class_model_uri: ClassVar[URIRef] = HTAN.ScRNALevel34

    HTAN_DATA_FILE_ID: Union[str, ScRNALevel34HTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    FILE_FORMAT: str = None
    SCRNASEQ_WORKFLOW_TYPE: Union[str, "ScRNAseqWorkflowTypeEnumLevel34"] = None
    SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION: str = None
    DATA_CATEGORY: Union[str, "DataCategoryEnum"] = None
    MATRIX_TYPE: Union[str, "MatrixTypeEnum"] = None
    CELL_MEDIAN_NUMBER_READS: int = None
    CELL_MEDIAN_NUMBER_GENES: int = None
    CELL_TOTAL: int = None
    ANNDATA_SCHEMA_VERSION: str = None
    ANNDATA_STRUCTURE_VALIDATED: Union[bool, Bool] = None
    LINKED_MATRICES: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ScRNALevel34HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ScRNALevel34HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.SCRNASEQ_WORKFLOW_TYPE):
            self.MissingRequiredField("SCRNASEQ_WORKFLOW_TYPE")
        if not isinstance(self.SCRNASEQ_WORKFLOW_TYPE, ScRNAseqWorkflowTypeEnumLevel34):
            self.SCRNASEQ_WORKFLOW_TYPE = ScRNAseqWorkflowTypeEnumLevel34(self.SCRNASEQ_WORKFLOW_TYPE)

        if self._is_empty(self.SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION):
            self.MissingRequiredField("SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION")
        if not isinstance(self.SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION, str):
            self.SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION = str(self.SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION)

        if self._is_empty(self.DATA_CATEGORY):
            self.MissingRequiredField("DATA_CATEGORY")
        if not isinstance(self.DATA_CATEGORY, DataCategoryEnum):
            self.DATA_CATEGORY = DataCategoryEnum(self.DATA_CATEGORY)

        if self._is_empty(self.MATRIX_TYPE):
            self.MissingRequiredField("MATRIX_TYPE")
        if not isinstance(self.MATRIX_TYPE, MatrixTypeEnum):
            self.MATRIX_TYPE = MatrixTypeEnum(self.MATRIX_TYPE)

        if self._is_empty(self.CELL_MEDIAN_NUMBER_READS):
            self.MissingRequiredField("CELL_MEDIAN_NUMBER_READS")
        if not isinstance(self.CELL_MEDIAN_NUMBER_READS, int):
            self.CELL_MEDIAN_NUMBER_READS = int(self.CELL_MEDIAN_NUMBER_READS)

        if self._is_empty(self.CELL_MEDIAN_NUMBER_GENES):
            self.MissingRequiredField("CELL_MEDIAN_NUMBER_GENES")
        if not isinstance(self.CELL_MEDIAN_NUMBER_GENES, int):
            self.CELL_MEDIAN_NUMBER_GENES = int(self.CELL_MEDIAN_NUMBER_GENES)

        if self._is_empty(self.CELL_TOTAL):
            self.MissingRequiredField("CELL_TOTAL")
        if not isinstance(self.CELL_TOTAL, int):
            self.CELL_TOTAL = int(self.CELL_TOTAL)

        if self._is_empty(self.ANNDATA_SCHEMA_VERSION):
            self.MissingRequiredField("ANNDATA_SCHEMA_VERSION")
        if not isinstance(self.ANNDATA_SCHEMA_VERSION, str):
            self.ANNDATA_SCHEMA_VERSION = str(self.ANNDATA_SCHEMA_VERSION)

        if self._is_empty(self.ANNDATA_STRUCTURE_VALIDATED):
            self.MissingRequiredField("ANNDATA_STRUCTURE_VALIDATED")
        if not isinstance(self.ANNDATA_STRUCTURE_VALIDATED, Bool):
            self.ANNDATA_STRUCTURE_VALIDATED = Bool(self.ANNDATA_STRUCTURE_VALIDATED)

        if self.LINKED_MATRICES is not None and not isinstance(self.LINKED_MATRICES, str):
            self.LINKED_MATRICES = str(self.LINKED_MATRICES)

        super().__post_init__(**kwargs)


# Enumerations
class DissociationMethodEnum(EnumDefinitionImpl):

    Enzymatic = PermissibleValue(
        text="Enzymatic",
        description="Enzymatic dissociation method")
    Mechanical = PermissibleValue(
        text="Mechanical",
        description="Mechanical dissociation method")
    Other = PermissibleValue(
        text="Other",
        description="Other dissociation method")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown dissociation method")

    _defn = EnumDefinition(
        name="DissociationMethodEnum",
    )

class LibraryConstructionMethodEnum(EnumDefinitionImpl):

    InDrop = PermissibleValue(
        text="InDrop",
        description="InDrop library construction method")
    Other = PermissibleValue(
        text="Other",
        description="Other library construction method")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown library construction method")

    _defn = EnumDefinition(
        name="LibraryConstructionMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10X Genomics",
            PermissibleValue(
                text="10X Genomics",
                description="10X Genomics library construction method"))
        setattr(cls, "Drop-seq",
            PermissibleValue(
                text="Drop-seq",
                description="Drop-seq library construction method"))
        setattr(cls, "Fluidigm C1",
            PermissibleValue(
                text="Fluidigm C1",
                description="Fluidigm C1 library construction method"))
        setattr(cls, "Smart-seq",
            PermissibleValue(
                text="Smart-seq",
                description="Smart-seq library construction method"))

class NucleicAcidSourceEnum(EnumDefinitionImpl):

    DNA = PermissibleValue(
        text="DNA",
        description="DNA nucleic acid source")
    RNA = PermissibleValue(
        text="RNA",
        description="RNA nucleic acid source")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown nucleic acid source")

    _defn = EnumDefinition(
        name="NucleicAcidSourceEnum",
    )

class ReadIndicatorEnum(EnumDefinitionImpl):

    Forward = PermissibleValue(
        text="Forward",
        description="Forward read indicator")
    Index = PermissibleValue(
        text="Index",
        description="Index read indicator")
    Reverse = PermissibleValue(
        text="Reverse",
        description="Reverse read indicator")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown read indicator")

    _defn = EnumDefinition(
        name="ReadIndicatorEnum",
    )

class ReverseTranscriptionPrimerEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown reverse transcription primer")

    _defn = EnumDefinition(
        name="ReverseTranscriptionPrimerEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Oligo-dT",
            PermissibleValue(
                text="Oligo-dT",
                description="Oligo-dT reverse transcription primer"))
        setattr(cls, "Random Hexamer",
            PermissibleValue(
                text="Random Hexamer",
                description="Random hexamer reverse transcription primer"))

class SingleCellIsolationMethodEnum(EnumDefinitionImpl):

    Microfluidics = PermissibleValue(
        text="Microfluidics",
        description="Microfluidics isolation method")
    Other = PermissibleValue(
        text="Other",
        description="Other isolation method")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown isolation method")

    _defn = EnumDefinition(
        name="SingleCellIsolationMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cell Sorting",
            PermissibleValue(
                text="Cell Sorting",
                description="Cell sorting isolation method"))
        setattr(cls, "Droplet-based",
            PermissibleValue(
                text="Droplet-based",
                description="Droplet-based isolation method"))
        setattr(cls, "Manual Picking",
            PermissibleValue(
                text="Manual Picking",
                description="Manual picking isolation method"))

class SpikeInEnum(EnumDefinitionImpl):

    ERCC = PermissibleValue(
        text="ERCC",
        description="ERCC spike-in")
    Other = PermissibleValue(
        text="Other",
        description="Other spike-in")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown spike-in")

    _defn = EnumDefinition(
        name="SpikeInEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No spike-in"))

class ScRNAseqWorkflowTypeEnumLevel2(EnumDefinitionImpl):

    CellRanger = PermissibleValue(
        text="CellRanger",
        description="CellRanger workflow")
    Other = PermissibleValue(
        text="Other",
        description="Other workflow")
    SEQC = PermissibleValue(
        text="SEQC",
        description="SEQC workflow")
    STARsolo = PermissibleValue(
        text="STARsolo",
        description="STARsolo workflow")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown workflow")
    dropEST = PermissibleValue(
        text="dropEST",
        description="dropEST workflow")

    _defn = EnumDefinition(
        name="ScRNAseqWorkflowTypeEnumLevel2",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "HCA Optimus",
            PermissibleValue(
                text="HCA Optimus",
                description="HCA Optimus workflow"))

class ScRNAseqWorkflowTypeEnumLevel34(EnumDefinitionImpl):

    CellRanger = PermissibleValue(
        text="CellRanger",
        description="10x Genomics CellRanger workflow")
    Cufflinks = PermissibleValue(
        text="Cufflinks",
        description="Cufflinks workflow")
    DEXSeq = PermissibleValue(
        text="DEXSeq",
        description="DEXSeq workflow")
    Other = PermissibleValue(
        text="Other",
        description="Other workflow type")
    SEQC = PermissibleValue(
        text="SEQC",
        description="SEQC workflow")
    STARsolo = PermissibleValue(
        text="STARsolo",
        description="STARsolo alignment workflow")
    dropEST = PermissibleValue(
        text="dropEST",
        description="dropEST workflow")

    _defn = EnumDefinition(
        name="ScRNAseqWorkflowTypeEnumLevel34",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cell annotation",
            PermissibleValue(
                text="Cell annotation",
                description="Cell annotation workflow"))
        setattr(cls, "Differentiation trajectory analysis",
            PermissibleValue(
                text="Differentiation trajectory analysis",
                description="Differentiation trajectory analysis workflow"))
        setattr(cls, "HCA Optimus",
            PermissibleValue(
                text="HCA Optimus",
                description="Human Cell Atlas Optimus workflow"))
        setattr(cls, "HTSeq - FPKM",
            PermissibleValue(
                text="HTSeq - FPKM",
                description="HTSeq FPKM workflow"))

class DataCategoryEnum(EnumDefinitionImpl):

    Other = PermissibleValue(
        text="Other",
        description="Other data category")

    _defn = EnumDefinition(
        name="DataCategoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Exon Expression Quantification",
            PermissibleValue(
                text="Exon Expression Quantification",
                description="Exon expression quantification"))
        setattr(cls, "Gene Expression",
            PermissibleValue(
                text="Gene Expression",
                description="Gene expression data"))
        setattr(cls, "Gene Expression Quantification",
            PermissibleValue(
                text="Gene Expression Quantification",
                description="Gene expression quantification"))
        setattr(cls, "Isoform Expression Quantification",
            PermissibleValue(
                text="Isoform Expression Quantification",
                description="Isoform expression quantification"))
        setattr(cls, "Splice Junction Quantification",
            PermissibleValue(
                text="Splice Junction Quantification",
                description="Splice junction quantification"))
        setattr(cls, "Transcript Expression",
            PermissibleValue(
                text="Transcript Expression",
                description="Transcript expression data"))

class MatrixTypeEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="MatrixTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Batch Corrected Counts",
            PermissibleValue(
                text="Batch Corrected Counts",
                description="Batch corrected count matrix"))
        setattr(cls, "Normalized Counts",
            PermissibleValue(
                text="Normalized Counts",
                description="Normalized count matrix"))
        setattr(cls, "Raw Counts",
            PermissibleValue(
                text="Raw Counts",
                description="Raw count matrix"))
        setattr(cls, "Scaled Counts",
            PermissibleValue(
                text="Scaled Counts",
                description="Scaled count matrix"))

class LibraryLayoutEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LibraryLayoutEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Paired-end",
            PermissibleValue(
                text="Paired-end",
                description="Paired-end sequencing"))
        setattr(cls, "Single-end",
            PermissibleValue(
                text="Single-end",
                description="Single-end sequencing"))

class SequencingPlatformEnum(EnumDefinitionImpl):

    ABI_SOLID = PermissibleValue(
        text="ABI_SOLID",
        description="ABI SOLID sequencing platform")
    BGISEQ = PermissibleValue(
        text="BGISEQ",
        description="BGI sequencing platform")
    CAPILLARY = PermissibleValue(
        text="CAPILLARY",
        description="Capillary sequencing platform")
    COMPLETE_GENOMICS = PermissibleValue(
        text="COMPLETE_GENOMICS",
        description="Complete Genomics sequencing platform")
    HELICOS = PermissibleValue(
        text="HELICOS",
        description="Helicos sequencing platform")
    ILLUMINA = PermissibleValue(
        text="ILLUMINA",
        description="Illumina sequencing platform")
    ION_TORRENT = PermissibleValue(
        text="ION_TORRENT",
        description="Ion Torrent sequencing platform")
    LS454 = PermissibleValue(
        text="LS454",
        description="454 sequencing platform")
    OXFORD_NANOPORE = PermissibleValue(
        text="OXFORD_NANOPORE",
        description="Oxford Nanopore sequencing platform")
    PACBIO_SMRT = PermissibleValue(
        text="PACBIO_SMRT",
        description="PacBio SMRT sequencing platform")

    _defn = EnumDefinition(
        name="SequencingPlatformEnum",
    )

# Slots
class slots:
    pass

slots.scRNAseqData__level1_data = Slot(uri=HTAN.level1_data, name="scRNAseqData__level1_data", curie=HTAN.curie('level1_data'),
                   model_uri=HTAN.scRNAseqData__level1_data, domain=None, range=Optional[Union[str, ScRNALevel1HTANDATAFILEID]])

slots.scRNAseqData__level2_data = Slot(uri=HTAN.level2_data, name="scRNAseqData__level2_data", curie=HTAN.curie('level2_data'),
                   model_uri=HTAN.scRNAseqData__level2_data, domain=None, range=Optional[Union[str, ScRNALevel2HTANDATAFILEID]])

slots.scRNAseqData__level3_4_data = Slot(uri=HTAN.level3_4_data, name="scRNAseqData__level3_4_data", curie=HTAN.curie('level3_4_data'),
                   model_uri=HTAN.scRNAseqData__level3_4_data, domain=None, range=Optional[Union[str, ScRNALevel34HTANDATAFILEID]])

slots.coreFileAttributes__COMPONENT = Slot(uri=HTAN.COMPONENT, name="coreFileAttributes__COMPONENT", curie=HTAN.curie('COMPONENT'),
                   model_uri=HTAN.coreFileAttributes__COMPONENT, domain=None, range=str)

slots.coreFileAttributes__FILENAME = Slot(uri=HTAN.FILENAME, name="coreFileAttributes__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.coreFileAttributes__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+[\\/]\S*$'))

slots.coreFileAttributes__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="coreFileAttributes__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.coreFileAttributes__FILE_FORMAT, domain=None, range=str)

slots.coreFileAttributes__HTAN_DATA_FILE_ID = Slot(uri=HTAN.HTAN_DATA_FILE_ID, name="coreFileAttributes__HTAN_DATA_FILE_ID", curie=HTAN.curie('HTAN_DATA_FILE_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_DATA_FILE_ID, domain=None, range=URIRef,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$'))

slots.coreFileAttributes__HTAN_PARENT_ID = Slot(uri=HTAN.HTAN_PARENT_ID, name="coreFileAttributes__HTAN_PARENT_ID", curie=HTAN.curie('HTAN_PARENT_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_PARENT_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA20[0-9])(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$'))

slots.scRNALevel1__SINGLE_CELL_ISOLATION_METHOD = Slot(uri=HTAN.SINGLE_CELL_ISOLATION_METHOD, name="scRNALevel1__SINGLE_CELL_ISOLATION_METHOD", curie=HTAN.curie('SINGLE_CELL_ISOLATION_METHOD'),
                   model_uri=HTAN.scRNALevel1__SINGLE_CELL_ISOLATION_METHOD, domain=None, range=Union[str, "SingleCellIsolationMethodEnum"])

slots.scRNALevel1__DISSOCIATION_METHOD = Slot(uri=HTAN.DISSOCIATION_METHOD, name="scRNALevel1__DISSOCIATION_METHOD", curie=HTAN.curie('DISSOCIATION_METHOD'),
                   model_uri=HTAN.scRNALevel1__DISSOCIATION_METHOD, domain=None, range=Union[str, "DissociationMethodEnum"])

slots.scRNALevel1__CRYOPRESERVED_CELLS_IN_SAMPLE = Slot(uri=HTAN.CRYOPRESERVED_CELLS_IN_SAMPLE, name="scRNALevel1__CRYOPRESERVED_CELLS_IN_SAMPLE", curie=HTAN.curie('CRYOPRESERVED_CELLS_IN_SAMPLE'),
                   model_uri=HTAN.scRNALevel1__CRYOPRESERVED_CELLS_IN_SAMPLE, domain=None, range=Optional[Union[bool, Bool]])

slots.scRNALevel1__NUCLEIC_ACID_SOURCE = Slot(uri=HTAN.NUCLEIC_ACID_SOURCE, name="scRNALevel1__NUCLEIC_ACID_SOURCE", curie=HTAN.curie('NUCLEIC_ACID_SOURCE'),
                   model_uri=HTAN.scRNALevel1__NUCLEIC_ACID_SOURCE, domain=None, range=Union[str, "NucleicAcidSourceEnum"])

slots.scRNALevel1__LIBRARY_CONSTRUCTION_METHOD = Slot(uri=HTAN.LIBRARY_CONSTRUCTION_METHOD, name="scRNALevel1__LIBRARY_CONSTRUCTION_METHOD", curie=HTAN.curie('LIBRARY_CONSTRUCTION_METHOD'),
                   model_uri=HTAN.scRNALevel1__LIBRARY_CONSTRUCTION_METHOD, domain=None, range=Union[str, "LibraryConstructionMethodEnum"])

slots.scRNALevel1__REVERSE_TRANSCRIPTION_PRIMER = Slot(uri=HTAN.REVERSE_TRANSCRIPTION_PRIMER, name="scRNALevel1__REVERSE_TRANSCRIPTION_PRIMER", curie=HTAN.curie('REVERSE_TRANSCRIPTION_PRIMER'),
                   model_uri=HTAN.scRNALevel1__REVERSE_TRANSCRIPTION_PRIMER, domain=None, range=Union[str, "ReverseTranscriptionPrimerEnum"])

slots.scRNALevel1__SPIKE_IN = Slot(uri=HTAN.SPIKE_IN, name="scRNALevel1__SPIKE_IN", curie=HTAN.curie('SPIKE_IN'),
                   model_uri=HTAN.scRNALevel1__SPIKE_IN, domain=None, range=Union[str, "SpikeInEnum"])

slots.scRNALevel1__READ_INDICATOR = Slot(uri=HTAN.READ_INDICATOR, name="scRNALevel1__READ_INDICATOR", curie=HTAN.curie('READ_INDICATOR'),
                   model_uri=HTAN.scRNALevel1__READ_INDICATOR, domain=None, range=Union[str, "ReadIndicatorEnum"])

slots.scRNALevel2__SCRNASEQ_WORKFLOW_TYPE = Slot(uri=HTAN.SCRNASEQ_WORKFLOW_TYPE, name="scRNALevel2__SCRNASEQ_WORKFLOW_TYPE", curie=HTAN.curie('SCRNASEQ_WORKFLOW_TYPE'),
                   model_uri=HTAN.scRNALevel2__SCRNASEQ_WORKFLOW_TYPE, domain=None, range=Union[str, "ScRNAseqWorkflowTypeEnumLevel2"])

slots.scRNALevel2__WHITELIST_CELL_BARCODE_FILE_LINK = Slot(uri=HTAN.WHITELIST_CELL_BARCODE_FILE_LINK, name="scRNALevel2__WHITELIST_CELL_BARCODE_FILE_LINK", curie=HTAN.curie('WHITELIST_CELL_BARCODE_FILE_LINK'),
                   model_uri=HTAN.scRNALevel2__WHITELIST_CELL_BARCODE_FILE_LINK, domain=None, range=Optional[str])

slots.scRNALevel2__CELL_BARCODE_TAG = Slot(uri=HTAN.CELL_BARCODE_TAG, name="scRNALevel2__CELL_BARCODE_TAG", curie=HTAN.curie('CELL_BARCODE_TAG'),
                   model_uri=HTAN.scRNALevel2__CELL_BARCODE_TAG, domain=None, range=Optional[str])

slots.scRNALevel2__UMI_TAG = Slot(uri=HTAN.UMI_TAG, name="scRNALevel2__UMI_TAG", curie=HTAN.curie('UMI_TAG'),
                   model_uri=HTAN.scRNALevel2__UMI_TAG, domain=None, range=Optional[str])

slots.scRNALevel34__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="scRNALevel34__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.scRNALevel34__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^h5ad$'))

slots.scRNALevel34__SCRNASEQ_WORKFLOW_TYPE = Slot(uri=HTAN.SCRNASEQ_WORKFLOW_TYPE, name="scRNALevel34__SCRNASEQ_WORKFLOW_TYPE", curie=HTAN.curie('SCRNASEQ_WORKFLOW_TYPE'),
                   model_uri=HTAN.scRNALevel34__SCRNASEQ_WORKFLOW_TYPE, domain=None, range=Union[str, "ScRNAseqWorkflowTypeEnumLevel34"])

slots.scRNALevel34__SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION = Slot(uri=HTAN.SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION, name="scRNALevel34__SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION", curie=HTAN.curie('SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION'),
                   model_uri=HTAN.scRNALevel34__SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION, domain=None, range=str)

slots.scRNALevel34__DATA_CATEGORY = Slot(uri=HTAN.DATA_CATEGORY, name="scRNALevel34__DATA_CATEGORY", curie=HTAN.curie('DATA_CATEGORY'),
                   model_uri=HTAN.scRNALevel34__DATA_CATEGORY, domain=None, range=Union[str, "DataCategoryEnum"])

slots.scRNALevel34__MATRIX_TYPE = Slot(uri=HTAN.MATRIX_TYPE, name="scRNALevel34__MATRIX_TYPE", curie=HTAN.curie('MATRIX_TYPE'),
                   model_uri=HTAN.scRNALevel34__MATRIX_TYPE, domain=None, range=Union[str, "MatrixTypeEnum"])

slots.scRNALevel34__LINKED_MATRICES = Slot(uri=HTAN.LINKED_MATRICES, name="scRNALevel34__LINKED_MATRICES", curie=HTAN.curie('LINKED_MATRICES'),
                   model_uri=HTAN.scRNALevel34__LINKED_MATRICES, domain=None, range=Optional[str])

slots.scRNALevel34__CELL_MEDIAN_NUMBER_READS = Slot(uri=HTAN.CELL_MEDIAN_NUMBER_READS, name="scRNALevel34__CELL_MEDIAN_NUMBER_READS", curie=HTAN.curie('CELL_MEDIAN_NUMBER_READS'),
                   model_uri=HTAN.scRNALevel34__CELL_MEDIAN_NUMBER_READS, domain=None, range=int)

slots.scRNALevel34__CELL_MEDIAN_NUMBER_GENES = Slot(uri=HTAN.CELL_MEDIAN_NUMBER_GENES, name="scRNALevel34__CELL_MEDIAN_NUMBER_GENES", curie=HTAN.curie('CELL_MEDIAN_NUMBER_GENES'),
                   model_uri=HTAN.scRNALevel34__CELL_MEDIAN_NUMBER_GENES, domain=None, range=int)

slots.scRNALevel34__CELL_TOTAL = Slot(uri=HTAN.CELL_TOTAL, name="scRNALevel34__CELL_TOTAL", curie=HTAN.curie('CELL_TOTAL'),
                   model_uri=HTAN.scRNALevel34__CELL_TOTAL, domain=None, range=int)

slots.scRNALevel34__ANNDATA_SCHEMA_VERSION = Slot(uri=HTAN.ANNDATA_SCHEMA_VERSION, name="scRNALevel34__ANNDATA_SCHEMA_VERSION", curie=HTAN.curie('ANNDATA_SCHEMA_VERSION'),
                   model_uri=HTAN.scRNALevel34__ANNDATA_SCHEMA_VERSION, domain=None, range=str,
                   pattern=re.compile(r'^0\.1$'))

slots.scRNALevel34__ANNDATA_STRUCTURE_VALIDATED = Slot(uri=HTAN.ANNDATA_STRUCTURE_VALIDATED, name="scRNALevel34__ANNDATA_STRUCTURE_VALIDATED", curie=HTAN.curie('ANNDATA_STRUCTURE_VALIDATED'),
                   model_uri=HTAN.scRNALevel34__ANNDATA_STRUCTURE_VALIDATED, domain=None, range=Union[bool, Bool])

slots.baseSequencingAttributes__SEQUENCING_BATCH_ID = Slot(uri=HTAN.SEQUENCING_BATCH_ID, name="baseSequencingAttributes__SEQUENCING_BATCH_ID", curie=HTAN.curie('SEQUENCING_BATCH_ID'),
                   model_uri=HTAN.baseSequencingAttributes__SEQUENCING_BATCH_ID, domain=None, range=Optional[str])

slots.baseSequencingAttributes__LIBRARY_LAYOUT = Slot(uri=HTAN.LIBRARY_LAYOUT, name="baseSequencingAttributes__LIBRARY_LAYOUT", curie=HTAN.curie('LIBRARY_LAYOUT'),
                   model_uri=HTAN.baseSequencingAttributes__LIBRARY_LAYOUT, domain=None, range=Union[str, "LibraryLayoutEnum"])

slots.baseSequencingAttributes__SEQUENCING_PLATFORM = Slot(uri=HTAN.SEQUENCING_PLATFORM, name="baseSequencingAttributes__SEQUENCING_PLATFORM", curie=HTAN.curie('SEQUENCING_PLATFORM'),
                   model_uri=HTAN.baseSequencingAttributes__SEQUENCING_PLATFORM, domain=None, range=Union[str, "SequencingPlatformEnum"])

slots.baseSequencingAttributes__LIBRARY_PREPARATION_DAYS_FROM_INDEX = Slot(uri=HTAN.LIBRARY_PREPARATION_DAYS_FROM_INDEX, name="baseSequencingAttributes__LIBRARY_PREPARATION_DAYS_FROM_INDEX", curie=HTAN.curie('LIBRARY_PREPARATION_DAYS_FROM_INDEX'),
                   model_uri=HTAN.baseSequencingAttributes__LIBRARY_PREPARATION_DAYS_FROM_INDEX, domain=None, range=Optional[int])

slots.baseSequencingAttributes__TECHNICAL_REPLICATE_GROUP = Slot(uri=HTAN.TECHNICAL_REPLICATE_GROUP, name="baseSequencingAttributes__TECHNICAL_REPLICATE_GROUP", curie=HTAN.curie('TECHNICAL_REPLICATE_GROUP'),
                   model_uri=HTAN.baseSequencingAttributes__TECHNICAL_REPLICATE_GROUP, domain=None, range=Optional[str])

slots.baseSequencingAttributes__PROTOCOL_LINK = Slot(uri=HTAN.PROTOCOL_LINK, name="baseSequencingAttributes__PROTOCOL_LINK", curie=HTAN.curie('PROTOCOL_LINK'),
                   model_uri=HTAN.baseSequencingAttributes__PROTOCOL_LINK, domain=None, range=Optional[str])

slots.baseSequencingAttributes__WORKFLOW_VERSION = Slot(uri=HTAN.WORKFLOW_VERSION, name="baseSequencingAttributes__WORKFLOW_VERSION", curie=HTAN.curie('WORKFLOW_VERSION'),
                   model_uri=HTAN.baseSequencingAttributes__WORKFLOW_VERSION, domain=None, range=str)

slots.baseSequencingAttributes__WORKFLOW_LINK = Slot(uri=HTAN.WORKFLOW_LINK, name="baseSequencingAttributes__WORKFLOW_LINK", curie=HTAN.curie('WORKFLOW_LINK'),
                   model_uri=HTAN.baseSequencingAttributes__WORKFLOW_LINK, domain=None, range=Optional[str])

slots.baseSequencingAttributes__GENOMIC_REFERENCE = Slot(uri=HTAN.GENOMIC_REFERENCE, name="baseSequencingAttributes__GENOMIC_REFERENCE", curie=HTAN.curie('GENOMIC_REFERENCE'),
                   model_uri=HTAN.baseSequencingAttributes__GENOMIC_REFERENCE, domain=None, range=str)

slots.baseSequencingAttributes__GENOMIC_REFERENCE_URL = Slot(uri=HTAN.GENOMIC_REFERENCE_URL, name="baseSequencingAttributes__GENOMIC_REFERENCE_URL", curie=HTAN.curie('GENOMIC_REFERENCE_URL'),
                   model_uri=HTAN.baseSequencingAttributes__GENOMIC_REFERENCE_URL, domain=None, range=Optional[str])

slots.baseSequencingAttributes__GENOME_ANNOTATION_URL = Slot(uri=HTAN.GENOME_ANNOTATION_URL, name="baseSequencingAttributes__GENOME_ANNOTATION_URL", curie=HTAN.curie('GENOME_ANNOTATION_URL'),
                   model_uri=HTAN.baseSequencingAttributes__GENOME_ANNOTATION_URL, domain=None, range=Optional[str])

slots.baseSequencingAttributes__CHECKSUM = Slot(uri=HTAN.CHECKSUM, name="baseSequencingAttributes__CHECKSUM", curie=HTAN.curie('CHECKSUM'),
                   model_uri=HTAN.baseSequencingAttributes__CHECKSUM, domain=None, range=Optional[str])

slots.biospecimenAttributes__HTAN_BIOSPECIMEN_ID = Slot(uri=HTAN.HTAN_BIOSPECIMEN_ID, name="biospecimenAttributes__HTAN_BIOSPECIMEN_ID", curie=HTAN.curie('HTAN_BIOSPECIMEN_ID'),
                   model_uri=HTAN.biospecimenAttributes__HTAN_BIOSPECIMEN_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$'))
