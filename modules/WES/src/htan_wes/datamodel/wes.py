# Auto generated from wes.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-27T14:51:47
# Schema: WES
#
# id: https://w3id.org/htan/wes
# description: HTAN Whole Exome Sequencing Data Model Schema
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

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
CADSR = CurieNamespace('caDSR', 'https://cadsr.cancer.gov/onedata/')
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN


# Types

# Class references
class CoreFileAttributesHTANDATAFILEID(extended_str):
    pass


class BiospecimenAttributesHTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class BaseSequencingAttributesHTANDATAFILEID(BiospecimenAttributesHTANDATAFILEID):
    pass


class BulkWESLevel1HTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


class BulkWESLevel2HTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


class BulkWESLevel3HTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


@dataclass(repr=False)
class WESData(YAMLRoot):
    """
    Container for all WES data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["WESData"]
    class_class_curie: ClassVar[str] = "htan:WESData"
    class_name: ClassVar[str] = "WESData"
    class_model_uri: ClassVar[URIRef] = HTAN.WESData

    COMPONENT: str = None
    LEVEL_1_DATA: Optional[Union[str, BulkWESLevel1HTANDATAFILEID]] = None
    LEVEL_2_DATA: Optional[Union[str, BulkWESLevel2HTANDATAFILEID]] = None
    LEVEL_3_DATA: Optional[Union[str, BulkWESLevel3HTANDATAFILEID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.COMPONENT):
            self.MissingRequiredField("COMPONENT")
        if not isinstance(self.COMPONENT, str):
            self.COMPONENT = str(self.COMPONENT)

        if self.LEVEL_1_DATA is not None and not isinstance(self.LEVEL_1_DATA, BulkWESLevel1HTANDATAFILEID):
            self.LEVEL_1_DATA = BulkWESLevel1HTANDATAFILEID(self.LEVEL_1_DATA)

        if self.LEVEL_2_DATA is not None and not isinstance(self.LEVEL_2_DATA, BulkWESLevel2HTANDATAFILEID):
            self.LEVEL_2_DATA = BulkWESLevel2HTANDATAFILEID(self.LEVEL_2_DATA)

        if self.LEVEL_3_DATA is not None and not isinstance(self.LEVEL_3_DATA, BulkWESLevel3HTANDATAFILEID):
            self.LEVEL_3_DATA = BulkWESLevel3HTANDATAFILEID(self.LEVEL_3_DATA)

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
class BulkWESLevel1(BaseSequencingAttributes):
    """
    Bulk Whole Exome Sequencing Level 1 - Raw files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BulkWESLevel1"]
    class_class_curie: ClassVar[str] = "htan:BulkWESLevel1"
    class_name: ClassVar[str] = "BulkWESLevel1"
    class_model_uri: ClassVar[URIRef] = HTAN.BulkWESLevel1

    HTAN_DATA_FILE_ID: Union[str, BulkWESLevel1HTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    LIBRARY_SELECTION_METHOD: Union[str, "LibrarySelectionMethodEnum"] = None
    READ_LENGTH: int = None
    READ_INDICATOR: Optional[str] = None
    TARGET_CAPTURE_KIT: Optional[str] = None
    LIBRARY_PREPARATION_KIT_NAME: Optional[str] = None
    LIBRARY_PREPARATION_KIT_VENDOR: Optional[str] = None
    LIBRARY_PREPARATION_KIT_VERSION: Optional[str] = None
    ADAPTER_NAME: Optional[str] = None
    ADAPTER_SEQUENCE: Optional[str] = None
    BASE_CALLER_NAME: Optional[str] = None
    BASE_CALLER_VERSION: Optional[str] = None
    FLOW_CELL_BARCODE: Optional[str] = None
    FRAGMENT_MAXIMUM_LENGTH: Optional[int] = None
    FRAGMENT_MEAN_LENGTH: Optional[int] = None
    FRAGMENT_MINIMUM_LENGTH: Optional[int] = None
    FRAGMENT_STANDARD_DEVIATION_LENGTH: Optional[int] = None
    LANE_NUMBER: Optional[int] = None
    MULTIPLEX_BARCODE: Optional[str] = None
    LIBRARY_PREPARATION_DAYS_FROM_INDEX: Optional[int] = None
    SIZE_SELECTION_RANGE: Optional[str] = None
    TARGET_DEPTH: Optional[int] = None
    TO_TRIM_ADAPTER_SEQUENCE: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BulkWESLevel1HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BulkWESLevel1HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.LIBRARY_SELECTION_METHOD):
            self.MissingRequiredField("LIBRARY_SELECTION_METHOD")
        if not isinstance(self.LIBRARY_SELECTION_METHOD, LibrarySelectionMethodEnum):
            self.LIBRARY_SELECTION_METHOD = LibrarySelectionMethodEnum(self.LIBRARY_SELECTION_METHOD)

        if self._is_empty(self.READ_LENGTH):
            self.MissingRequiredField("READ_LENGTH")
        if not isinstance(self.READ_LENGTH, int):
            self.READ_LENGTH = int(self.READ_LENGTH)

        if self.READ_INDICATOR is not None and not isinstance(self.READ_INDICATOR, str):
            self.READ_INDICATOR = str(self.READ_INDICATOR)

        if self.TARGET_CAPTURE_KIT is not None and not isinstance(self.TARGET_CAPTURE_KIT, str):
            self.TARGET_CAPTURE_KIT = str(self.TARGET_CAPTURE_KIT)

        if self.LIBRARY_PREPARATION_KIT_NAME is not None and not isinstance(self.LIBRARY_PREPARATION_KIT_NAME, str):
            self.LIBRARY_PREPARATION_KIT_NAME = str(self.LIBRARY_PREPARATION_KIT_NAME)

        if self.LIBRARY_PREPARATION_KIT_VENDOR is not None and not isinstance(self.LIBRARY_PREPARATION_KIT_VENDOR, str):
            self.LIBRARY_PREPARATION_KIT_VENDOR = str(self.LIBRARY_PREPARATION_KIT_VENDOR)

        if self.LIBRARY_PREPARATION_KIT_VERSION is not None and not isinstance(self.LIBRARY_PREPARATION_KIT_VERSION, str):
            self.LIBRARY_PREPARATION_KIT_VERSION = str(self.LIBRARY_PREPARATION_KIT_VERSION)

        if self.ADAPTER_NAME is not None and not isinstance(self.ADAPTER_NAME, str):
            self.ADAPTER_NAME = str(self.ADAPTER_NAME)

        if self.ADAPTER_SEQUENCE is not None and not isinstance(self.ADAPTER_SEQUENCE, str):
            self.ADAPTER_SEQUENCE = str(self.ADAPTER_SEQUENCE)

        if self.BASE_CALLER_NAME is not None and not isinstance(self.BASE_CALLER_NAME, str):
            self.BASE_CALLER_NAME = str(self.BASE_CALLER_NAME)

        if self.BASE_CALLER_VERSION is not None and not isinstance(self.BASE_CALLER_VERSION, str):
            self.BASE_CALLER_VERSION = str(self.BASE_CALLER_VERSION)

        if self.FLOW_CELL_BARCODE is not None and not isinstance(self.FLOW_CELL_BARCODE, str):
            self.FLOW_CELL_BARCODE = str(self.FLOW_CELL_BARCODE)

        if self.FRAGMENT_MAXIMUM_LENGTH is not None and not isinstance(self.FRAGMENT_MAXIMUM_LENGTH, int):
            self.FRAGMENT_MAXIMUM_LENGTH = int(self.FRAGMENT_MAXIMUM_LENGTH)

        if self.FRAGMENT_MEAN_LENGTH is not None and not isinstance(self.FRAGMENT_MEAN_LENGTH, int):
            self.FRAGMENT_MEAN_LENGTH = int(self.FRAGMENT_MEAN_LENGTH)

        if self.FRAGMENT_MINIMUM_LENGTH is not None and not isinstance(self.FRAGMENT_MINIMUM_LENGTH, int):
            self.FRAGMENT_MINIMUM_LENGTH = int(self.FRAGMENT_MINIMUM_LENGTH)

        if self.FRAGMENT_STANDARD_DEVIATION_LENGTH is not None and not isinstance(self.FRAGMENT_STANDARD_DEVIATION_LENGTH, int):
            self.FRAGMENT_STANDARD_DEVIATION_LENGTH = int(self.FRAGMENT_STANDARD_DEVIATION_LENGTH)

        if self.LANE_NUMBER is not None and not isinstance(self.LANE_NUMBER, int):
            self.LANE_NUMBER = int(self.LANE_NUMBER)

        if self.MULTIPLEX_BARCODE is not None and not isinstance(self.MULTIPLEX_BARCODE, str):
            self.MULTIPLEX_BARCODE = str(self.MULTIPLEX_BARCODE)

        if self.LIBRARY_PREPARATION_DAYS_FROM_INDEX is not None and not isinstance(self.LIBRARY_PREPARATION_DAYS_FROM_INDEX, int):
            self.LIBRARY_PREPARATION_DAYS_FROM_INDEX = int(self.LIBRARY_PREPARATION_DAYS_FROM_INDEX)

        if self.SIZE_SELECTION_RANGE is not None and not isinstance(self.SIZE_SELECTION_RANGE, str):
            self.SIZE_SELECTION_RANGE = str(self.SIZE_SELECTION_RANGE)

        if self.TARGET_DEPTH is not None and not isinstance(self.TARGET_DEPTH, int):
            self.TARGET_DEPTH = int(self.TARGET_DEPTH)

        if self.TO_TRIM_ADAPTER_SEQUENCE is not None and not isinstance(self.TO_TRIM_ADAPTER_SEQUENCE, Bool):
            self.TO_TRIM_ADAPTER_SEQUENCE = Bool(self.TO_TRIM_ADAPTER_SEQUENCE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BulkWESLevel2(BaseSequencingAttributes):
    """
    Bulk Whole Exome Sequencing Level 2 - Reads mapped to the genome and alignment QC
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BulkWESLevel2"]
    class_class_curie: ClassVar[str] = "htan:BulkWESLevel2"
    class_name: ClassVar[str] = "BulkWESLevel2"
    class_model_uri: ClassVar[URIRef] = HTAN.BulkWESLevel2

    HTAN_DATA_FILE_ID: Union[str, BulkWESLevel2HTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    ALIGNMENT_WORKFLOW_TYPE: str = None
    MEAN_COVERAGE: float = None
    TOTAL_READS: int = None
    TOTAL_UNIQUELY_MAPPED: int = None
    TOTAL_UNMAPPED_READS: int = None
    PROPORTION_READS_MAPPED: float = None
    INDEX_FILE_NAME: Optional[str] = None
    AVERAGE_BASE_QUALITY: Optional[float] = None
    AVERAGE_INSERT_SIZE: Optional[int] = None
    AVERAGE_READ_LENGTH: Optional[int] = None
    CONTAMINATION: Optional[float] = None
    CONTAMINATION_ERROR: Optional[float] = None
    ADAPTER_CONTENT: Optional[str] = None
    BASIC_STATISTICS: Optional[str] = None
    ENCODING: Optional[str] = None
    OVERREPRESENTED_SEQUENCES: Optional[str] = None
    PER_BASE_N_CONTENT: Optional[str] = None
    PER_BASE_SEQUENCE_CONTENT: Optional[str] = None
    PER_BASE_SEQUENCE_QUALITY: Optional[str] = None
    PER_SEQUENCE_GC_CONTENT: Optional[str] = None
    PER_SEQUENCE_QUALITY_SCORE: Optional[str] = None
    PER_TILE_SEQUENCE_QUALITY: Optional[str] = None
    PERCENT_GC_CONTENT: Optional[float] = None
    SEQUENCE_DUPLICATION_LEVELS: Optional[str] = None
    SEQUENCE_LENGTH_DISTRIBUTION: Optional[str] = None
    QC_WORKFLOW_TYPE: Optional[str] = None
    QC_WORKFLOW_VERSION: Optional[str] = None
    QC_WORKFLOW_LINK: Optional[str] = None
    PAIRS_ON_DIFF_CHR: Optional[int] = None
    PROPORTION_READS_DUPLICATED: Optional[float] = None
    PROPORTION_TARGETS_NO_COVERAGE: Optional[float] = None
    PROPORTION_BASE_MISMATCH: Optional[float] = None
    SHORT_READS: Optional[int] = None
    PROPORTION_COVERAGE_10X: Optional[float] = None
    PROPORTION_COVERAGE_30X: Optional[float] = None
    IS_LOWEST_LEVEL: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BulkWESLevel2HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BulkWESLevel2HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.ALIGNMENT_WORKFLOW_TYPE):
            self.MissingRequiredField("ALIGNMENT_WORKFLOW_TYPE")
        if not isinstance(self.ALIGNMENT_WORKFLOW_TYPE, str):
            self.ALIGNMENT_WORKFLOW_TYPE = str(self.ALIGNMENT_WORKFLOW_TYPE)

        if self._is_empty(self.MEAN_COVERAGE):
            self.MissingRequiredField("MEAN_COVERAGE")
        if not isinstance(self.MEAN_COVERAGE, float):
            self.MEAN_COVERAGE = float(self.MEAN_COVERAGE)

        if self._is_empty(self.TOTAL_READS):
            self.MissingRequiredField("TOTAL_READS")
        if not isinstance(self.TOTAL_READS, int):
            self.TOTAL_READS = int(self.TOTAL_READS)

        if self._is_empty(self.TOTAL_UNIQUELY_MAPPED):
            self.MissingRequiredField("TOTAL_UNIQUELY_MAPPED")
        if not isinstance(self.TOTAL_UNIQUELY_MAPPED, int):
            self.TOTAL_UNIQUELY_MAPPED = int(self.TOTAL_UNIQUELY_MAPPED)

        if self._is_empty(self.TOTAL_UNMAPPED_READS):
            self.MissingRequiredField("TOTAL_UNMAPPED_READS")
        if not isinstance(self.TOTAL_UNMAPPED_READS, int):
            self.TOTAL_UNMAPPED_READS = int(self.TOTAL_UNMAPPED_READS)

        if self._is_empty(self.PROPORTION_READS_MAPPED):
            self.MissingRequiredField("PROPORTION_READS_MAPPED")
        if not isinstance(self.PROPORTION_READS_MAPPED, float):
            self.PROPORTION_READS_MAPPED = float(self.PROPORTION_READS_MAPPED)

        if self.INDEX_FILE_NAME is not None and not isinstance(self.INDEX_FILE_NAME, str):
            self.INDEX_FILE_NAME = str(self.INDEX_FILE_NAME)

        if self.AVERAGE_BASE_QUALITY is not None and not isinstance(self.AVERAGE_BASE_QUALITY, float):
            self.AVERAGE_BASE_QUALITY = float(self.AVERAGE_BASE_QUALITY)

        if self.AVERAGE_INSERT_SIZE is not None and not isinstance(self.AVERAGE_INSERT_SIZE, int):
            self.AVERAGE_INSERT_SIZE = int(self.AVERAGE_INSERT_SIZE)

        if self.AVERAGE_READ_LENGTH is not None and not isinstance(self.AVERAGE_READ_LENGTH, int):
            self.AVERAGE_READ_LENGTH = int(self.AVERAGE_READ_LENGTH)

        if self.CONTAMINATION is not None and not isinstance(self.CONTAMINATION, float):
            self.CONTAMINATION = float(self.CONTAMINATION)

        if self.CONTAMINATION_ERROR is not None and not isinstance(self.CONTAMINATION_ERROR, float):
            self.CONTAMINATION_ERROR = float(self.CONTAMINATION_ERROR)

        if self.ADAPTER_CONTENT is not None and not isinstance(self.ADAPTER_CONTENT, str):
            self.ADAPTER_CONTENT = str(self.ADAPTER_CONTENT)

        if self.BASIC_STATISTICS is not None and not isinstance(self.BASIC_STATISTICS, str):
            self.BASIC_STATISTICS = str(self.BASIC_STATISTICS)

        if self.ENCODING is not None and not isinstance(self.ENCODING, str):
            self.ENCODING = str(self.ENCODING)

        if self.OVERREPRESENTED_SEQUENCES is not None and not isinstance(self.OVERREPRESENTED_SEQUENCES, str):
            self.OVERREPRESENTED_SEQUENCES = str(self.OVERREPRESENTED_SEQUENCES)

        if self.PER_BASE_N_CONTENT is not None and not isinstance(self.PER_BASE_N_CONTENT, str):
            self.PER_BASE_N_CONTENT = str(self.PER_BASE_N_CONTENT)

        if self.PER_BASE_SEQUENCE_CONTENT is not None and not isinstance(self.PER_BASE_SEQUENCE_CONTENT, str):
            self.PER_BASE_SEQUENCE_CONTENT = str(self.PER_BASE_SEQUENCE_CONTENT)

        if self.PER_BASE_SEQUENCE_QUALITY is not None and not isinstance(self.PER_BASE_SEQUENCE_QUALITY, str):
            self.PER_BASE_SEQUENCE_QUALITY = str(self.PER_BASE_SEQUENCE_QUALITY)

        if self.PER_SEQUENCE_GC_CONTENT is not None and not isinstance(self.PER_SEQUENCE_GC_CONTENT, str):
            self.PER_SEQUENCE_GC_CONTENT = str(self.PER_SEQUENCE_GC_CONTENT)

        if self.PER_SEQUENCE_QUALITY_SCORE is not None and not isinstance(self.PER_SEQUENCE_QUALITY_SCORE, str):
            self.PER_SEQUENCE_QUALITY_SCORE = str(self.PER_SEQUENCE_QUALITY_SCORE)

        if self.PER_TILE_SEQUENCE_QUALITY is not None and not isinstance(self.PER_TILE_SEQUENCE_QUALITY, str):
            self.PER_TILE_SEQUENCE_QUALITY = str(self.PER_TILE_SEQUENCE_QUALITY)

        if self.PERCENT_GC_CONTENT is not None and not isinstance(self.PERCENT_GC_CONTENT, float):
            self.PERCENT_GC_CONTENT = float(self.PERCENT_GC_CONTENT)

        if self.SEQUENCE_DUPLICATION_LEVELS is not None and not isinstance(self.SEQUENCE_DUPLICATION_LEVELS, str):
            self.SEQUENCE_DUPLICATION_LEVELS = str(self.SEQUENCE_DUPLICATION_LEVELS)

        if self.SEQUENCE_LENGTH_DISTRIBUTION is not None and not isinstance(self.SEQUENCE_LENGTH_DISTRIBUTION, str):
            self.SEQUENCE_LENGTH_DISTRIBUTION = str(self.SEQUENCE_LENGTH_DISTRIBUTION)

        if self.QC_WORKFLOW_TYPE is not None and not isinstance(self.QC_WORKFLOW_TYPE, str):
            self.QC_WORKFLOW_TYPE = str(self.QC_WORKFLOW_TYPE)

        if self.QC_WORKFLOW_VERSION is not None and not isinstance(self.QC_WORKFLOW_VERSION, str):
            self.QC_WORKFLOW_VERSION = str(self.QC_WORKFLOW_VERSION)

        if self.QC_WORKFLOW_LINK is not None and not isinstance(self.QC_WORKFLOW_LINK, str):
            self.QC_WORKFLOW_LINK = str(self.QC_WORKFLOW_LINK)

        if self.PAIRS_ON_DIFF_CHR is not None and not isinstance(self.PAIRS_ON_DIFF_CHR, int):
            self.PAIRS_ON_DIFF_CHR = int(self.PAIRS_ON_DIFF_CHR)

        if self.PROPORTION_READS_DUPLICATED is not None and not isinstance(self.PROPORTION_READS_DUPLICATED, float):
            self.PROPORTION_READS_DUPLICATED = float(self.PROPORTION_READS_DUPLICATED)

        if self.PROPORTION_TARGETS_NO_COVERAGE is not None and not isinstance(self.PROPORTION_TARGETS_NO_COVERAGE, float):
            self.PROPORTION_TARGETS_NO_COVERAGE = float(self.PROPORTION_TARGETS_NO_COVERAGE)

        if self.PROPORTION_BASE_MISMATCH is not None and not isinstance(self.PROPORTION_BASE_MISMATCH, float):
            self.PROPORTION_BASE_MISMATCH = float(self.PROPORTION_BASE_MISMATCH)

        if self.SHORT_READS is not None and not isinstance(self.SHORT_READS, int):
            self.SHORT_READS = int(self.SHORT_READS)

        if self.PROPORTION_COVERAGE_10X is not None and not isinstance(self.PROPORTION_COVERAGE_10X, float):
            self.PROPORTION_COVERAGE_10X = float(self.PROPORTION_COVERAGE_10X)

        if self.PROPORTION_COVERAGE_30X is not None and not isinstance(self.PROPORTION_COVERAGE_30X, float):
            self.PROPORTION_COVERAGE_30X = float(self.PROPORTION_COVERAGE_30X)

        if self.IS_LOWEST_LEVEL is not None and not isinstance(self.IS_LOWEST_LEVEL, Bool):
            self.IS_LOWEST_LEVEL = Bool(self.IS_LOWEST_LEVEL)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BulkWESLevel3(BaseSequencingAttributes):
    """
    Bulk Whole Exome Sequencing Level 3 - Called variants and MSI analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BulkWESLevel3"]
    class_class_curie: ClassVar[str] = "htan:BulkWESLevel3"
    class_name: ClassVar[str] = "BulkWESLevel3"
    class_model_uri: ClassVar[URIRef] = HTAN.BulkWESLevel3

    HTAN_DATA_FILE_ID: Union[str, BulkWESLevel3HTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    WORKFLOW_VERSION: str = None
    GENOMIC_REFERENCE: str = None
    GERMLINE_VARIANTS_WORKFLOW_URL: Optional[str] = None
    GERMLINE_VARIANTS_WORKFLOW_TYPE: Optional[str] = None
    SOMATIC_VARIANTS_WORKFLOW_URL: Optional[str] = None
    SOMATIC_VARIANTS_WORKFLOW_TYPE: Optional[str] = None
    SOMATIC_VARIANTS_SAMPLE_TYPE: Optional[Union[str, "SomaticVariantsSampleTypeEnum"]] = None
    STRUCTURAL_VARIANT_WORKFLOW_URL: Optional[str] = None
    STRUCTURAL_VARIANT_WORKFLOW_TYPE: Optional[str] = None
    MSI_WORKFLOW_LINK: Optional[str] = None
    MSI_SCORE: Optional[float] = None
    MSI_STATUS: Optional[Union[str, "MSIStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BulkWESLevel3HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BulkWESLevel3HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self.GERMLINE_VARIANTS_WORKFLOW_URL is not None and not isinstance(self.GERMLINE_VARIANTS_WORKFLOW_URL, str):
            self.GERMLINE_VARIANTS_WORKFLOW_URL = str(self.GERMLINE_VARIANTS_WORKFLOW_URL)

        if self.GERMLINE_VARIANTS_WORKFLOW_TYPE is not None and not isinstance(self.GERMLINE_VARIANTS_WORKFLOW_TYPE, str):
            self.GERMLINE_VARIANTS_WORKFLOW_TYPE = str(self.GERMLINE_VARIANTS_WORKFLOW_TYPE)

        if self.SOMATIC_VARIANTS_WORKFLOW_URL is not None and not isinstance(self.SOMATIC_VARIANTS_WORKFLOW_URL, str):
            self.SOMATIC_VARIANTS_WORKFLOW_URL = str(self.SOMATIC_VARIANTS_WORKFLOW_URL)

        if self.SOMATIC_VARIANTS_WORKFLOW_TYPE is not None and not isinstance(self.SOMATIC_VARIANTS_WORKFLOW_TYPE, str):
            self.SOMATIC_VARIANTS_WORKFLOW_TYPE = str(self.SOMATIC_VARIANTS_WORKFLOW_TYPE)

        if self.SOMATIC_VARIANTS_SAMPLE_TYPE is not None and not isinstance(self.SOMATIC_VARIANTS_SAMPLE_TYPE, SomaticVariantsSampleTypeEnum):
            self.SOMATIC_VARIANTS_SAMPLE_TYPE = SomaticVariantsSampleTypeEnum(self.SOMATIC_VARIANTS_SAMPLE_TYPE)

        if self.STRUCTURAL_VARIANT_WORKFLOW_URL is not None and not isinstance(self.STRUCTURAL_VARIANT_WORKFLOW_URL, str):
            self.STRUCTURAL_VARIANT_WORKFLOW_URL = str(self.STRUCTURAL_VARIANT_WORKFLOW_URL)

        if self.STRUCTURAL_VARIANT_WORKFLOW_TYPE is not None and not isinstance(self.STRUCTURAL_VARIANT_WORKFLOW_TYPE, str):
            self.STRUCTURAL_VARIANT_WORKFLOW_TYPE = str(self.STRUCTURAL_VARIANT_WORKFLOW_TYPE)

        if self.MSI_WORKFLOW_LINK is not None and not isinstance(self.MSI_WORKFLOW_LINK, str):
            self.MSI_WORKFLOW_LINK = str(self.MSI_WORKFLOW_LINK)

        if self.MSI_SCORE is not None and not isinstance(self.MSI_SCORE, float):
            self.MSI_SCORE = float(self.MSI_SCORE)

        if self.MSI_STATUS is not None and not isinstance(self.MSI_STATUS, MSIStatusEnum):
            self.MSI_STATUS = MSIStatusEnum(self.MSI_STATUS)

        super().__post_init__(**kwargs)


# Enumerations
class LibrarySelectionMethodEnum(EnumDefinitionImpl):

    PCR = PermissibleValue(
        text="PCR",
        description="PCR-based selection")
    RANDOM = PermissibleValue(
        text="RANDOM",
        description="Random selection")
    other = PermissibleValue(
        text="other",
        description="Other selection method")

    _defn = EnumDefinition(
        name="LibrarySelectionMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hybrid Selection",
            PermissibleValue(
                text="Hybrid Selection",
                description="Hybrid selection method"))

class MSIStatusEnum(EnumDefinitionImpl):

    MSS = PermissibleValue(
        text="MSS",
        description="Microsatellite stable")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown MSI status")

    _defn = EnumDefinition(
        name="MSIStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "MSI-H",
            PermissibleValue(
                text="MSI-H",
                description="High microsatellite instability"))
        setattr(cls, "MSI-L",
            PermissibleValue(
                text="MSI-L",
                description="Low microsatellite instability"))

class SomaticVariantsSampleTypeEnum(EnumDefinitionImpl):

    Metastatic = PermissibleValue(
        text="Metastatic",
        description="Metastatic tumor sample")
    Normal = PermissibleValue(
        text="Normal",
        description="Normal tissue sample")
    Other = PermissibleValue(
        text="Other",
        description="Other sample type")
    Primary = PermissibleValue(
        text="Primary",
        description="Primary tumor sample")
    Recurrent = PermissibleValue(
        text="Recurrent",
        description="Recurrent tumor sample")

    _defn = EnumDefinition(
        name="SomaticVariantsSampleTypeEnum",
    )

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

slots.caDSR_id = Slot(uri=HTAN.caDSR_id, name="caDSR_id", curie=HTAN.curie('caDSR_id'),
                   model_uri=HTAN.caDSR_id, domain=None, range=Optional[str])

slots.wESData__COMPONENT = Slot(uri=HTAN.COMPONENT, name="wESData__COMPONENT", curie=HTAN.curie('COMPONENT'),
                   model_uri=HTAN.wESData__COMPONENT, domain=None, range=str)

slots.wESData__LEVEL_1_DATA = Slot(uri=HTAN.LEVEL_1_DATA, name="wESData__LEVEL_1_DATA", curie=HTAN.curie('LEVEL_1_DATA'),
                   model_uri=HTAN.wESData__LEVEL_1_DATA, domain=None, range=Optional[Union[str, BulkWESLevel1HTANDATAFILEID]])

slots.wESData__LEVEL_2_DATA = Slot(uri=HTAN.LEVEL_2_DATA, name="wESData__LEVEL_2_DATA", curie=HTAN.curie('LEVEL_2_DATA'),
                   model_uri=HTAN.wESData__LEVEL_2_DATA, domain=None, range=Optional[Union[str, BulkWESLevel2HTANDATAFILEID]])

slots.wESData__LEVEL_3_DATA = Slot(uri=HTAN.LEVEL_3_DATA, name="wESData__LEVEL_3_DATA", curie=HTAN.curie('LEVEL_3_DATA'),
                   model_uri=HTAN.wESData__LEVEL_3_DATA, domain=None, range=Optional[Union[str, BulkWESLevel3HTANDATAFILEID]])

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

slots.bulkWESLevel1__READ_INDICATOR = Slot(uri=HTAN.READ_INDICATOR, name="bulkWESLevel1__READ_INDICATOR", curie=HTAN.curie('READ_INDICATOR'),
                   model_uri=HTAN.bulkWESLevel1__READ_INDICATOR, domain=None, range=Optional[str])

slots.bulkWESLevel1__LIBRARY_SELECTION_METHOD = Slot(uri=HTAN.LIBRARY_SELECTION_METHOD, name="bulkWESLevel1__LIBRARY_SELECTION_METHOD", curie=HTAN.curie('LIBRARY_SELECTION_METHOD'),
                   model_uri=HTAN.bulkWESLevel1__LIBRARY_SELECTION_METHOD, domain=None, range=Union[str, "LibrarySelectionMethodEnum"])

slots.bulkWESLevel1__READ_LENGTH = Slot(uri=HTAN.READ_LENGTH, name="bulkWESLevel1__READ_LENGTH", curie=HTAN.curie('READ_LENGTH'),
                   model_uri=HTAN.bulkWESLevel1__READ_LENGTH, domain=None, range=int)

slots.bulkWESLevel1__TARGET_CAPTURE_KIT = Slot(uri=HTAN.TARGET_CAPTURE_KIT, name="bulkWESLevel1__TARGET_CAPTURE_KIT", curie=HTAN.curie('TARGET_CAPTURE_KIT'),
                   model_uri=HTAN.bulkWESLevel1__TARGET_CAPTURE_KIT, domain=None, range=Optional[str])

slots.bulkWESLevel1__LIBRARY_PREPARATION_KIT_NAME = Slot(uri=HTAN.LIBRARY_PREPARATION_KIT_NAME, name="bulkWESLevel1__LIBRARY_PREPARATION_KIT_NAME", curie=HTAN.curie('LIBRARY_PREPARATION_KIT_NAME'),
                   model_uri=HTAN.bulkWESLevel1__LIBRARY_PREPARATION_KIT_NAME, domain=None, range=Optional[str])

slots.bulkWESLevel1__LIBRARY_PREPARATION_KIT_VENDOR = Slot(uri=HTAN.LIBRARY_PREPARATION_KIT_VENDOR, name="bulkWESLevel1__LIBRARY_PREPARATION_KIT_VENDOR", curie=HTAN.curie('LIBRARY_PREPARATION_KIT_VENDOR'),
                   model_uri=HTAN.bulkWESLevel1__LIBRARY_PREPARATION_KIT_VENDOR, domain=None, range=Optional[str])

slots.bulkWESLevel1__LIBRARY_PREPARATION_KIT_VERSION = Slot(uri=HTAN.LIBRARY_PREPARATION_KIT_VERSION, name="bulkWESLevel1__LIBRARY_PREPARATION_KIT_VERSION", curie=HTAN.curie('LIBRARY_PREPARATION_KIT_VERSION'),
                   model_uri=HTAN.bulkWESLevel1__LIBRARY_PREPARATION_KIT_VERSION, domain=None, range=Optional[str])

slots.bulkWESLevel1__ADAPTER_NAME = Slot(uri=HTAN.ADAPTER_NAME, name="bulkWESLevel1__ADAPTER_NAME", curie=HTAN.curie('ADAPTER_NAME'),
                   model_uri=HTAN.bulkWESLevel1__ADAPTER_NAME, domain=None, range=Optional[str])

slots.bulkWESLevel1__ADAPTER_SEQUENCE = Slot(uri=HTAN.ADAPTER_SEQUENCE, name="bulkWESLevel1__ADAPTER_SEQUENCE", curie=HTAN.curie('ADAPTER_SEQUENCE'),
                   model_uri=HTAN.bulkWESLevel1__ADAPTER_SEQUENCE, domain=None, range=Optional[str])

slots.bulkWESLevel1__BASE_CALLER_NAME = Slot(uri=HTAN.BASE_CALLER_NAME, name="bulkWESLevel1__BASE_CALLER_NAME", curie=HTAN.curie('BASE_CALLER_NAME'),
                   model_uri=HTAN.bulkWESLevel1__BASE_CALLER_NAME, domain=None, range=Optional[str])

slots.bulkWESLevel1__BASE_CALLER_VERSION = Slot(uri=HTAN.BASE_CALLER_VERSION, name="bulkWESLevel1__BASE_CALLER_VERSION", curie=HTAN.curie('BASE_CALLER_VERSION'),
                   model_uri=HTAN.bulkWESLevel1__BASE_CALLER_VERSION, domain=None, range=Optional[str])

slots.bulkWESLevel1__FLOW_CELL_BARCODE = Slot(uri=HTAN.FLOW_CELL_BARCODE, name="bulkWESLevel1__FLOW_CELL_BARCODE", curie=HTAN.curie('FLOW_CELL_BARCODE'),
                   model_uri=HTAN.bulkWESLevel1__FLOW_CELL_BARCODE, domain=None, range=Optional[str])

slots.bulkWESLevel1__FRAGMENT_MAXIMUM_LENGTH = Slot(uri=HTAN.FRAGMENT_MAXIMUM_LENGTH, name="bulkWESLevel1__FRAGMENT_MAXIMUM_LENGTH", curie=HTAN.curie('FRAGMENT_MAXIMUM_LENGTH'),
                   model_uri=HTAN.bulkWESLevel1__FRAGMENT_MAXIMUM_LENGTH, domain=None, range=Optional[int])

slots.bulkWESLevel1__FRAGMENT_MEAN_LENGTH = Slot(uri=HTAN.FRAGMENT_MEAN_LENGTH, name="bulkWESLevel1__FRAGMENT_MEAN_LENGTH", curie=HTAN.curie('FRAGMENT_MEAN_LENGTH'),
                   model_uri=HTAN.bulkWESLevel1__FRAGMENT_MEAN_LENGTH, domain=None, range=Optional[int])

slots.bulkWESLevel1__FRAGMENT_MINIMUM_LENGTH = Slot(uri=HTAN.FRAGMENT_MINIMUM_LENGTH, name="bulkWESLevel1__FRAGMENT_MINIMUM_LENGTH", curie=HTAN.curie('FRAGMENT_MINIMUM_LENGTH'),
                   model_uri=HTAN.bulkWESLevel1__FRAGMENT_MINIMUM_LENGTH, domain=None, range=Optional[int])

slots.bulkWESLevel1__FRAGMENT_STANDARD_DEVIATION_LENGTH = Slot(uri=HTAN.FRAGMENT_STANDARD_DEVIATION_LENGTH, name="bulkWESLevel1__FRAGMENT_STANDARD_DEVIATION_LENGTH", curie=HTAN.curie('FRAGMENT_STANDARD_DEVIATION_LENGTH'),
                   model_uri=HTAN.bulkWESLevel1__FRAGMENT_STANDARD_DEVIATION_LENGTH, domain=None, range=Optional[int])

slots.bulkWESLevel1__LANE_NUMBER = Slot(uri=HTAN.LANE_NUMBER, name="bulkWESLevel1__LANE_NUMBER", curie=HTAN.curie('LANE_NUMBER'),
                   model_uri=HTAN.bulkWESLevel1__LANE_NUMBER, domain=None, range=Optional[int])

slots.bulkWESLevel1__MULTIPLEX_BARCODE = Slot(uri=HTAN.MULTIPLEX_BARCODE, name="bulkWESLevel1__MULTIPLEX_BARCODE", curie=HTAN.curie('MULTIPLEX_BARCODE'),
                   model_uri=HTAN.bulkWESLevel1__MULTIPLEX_BARCODE, domain=None, range=Optional[str])

slots.bulkWESLevel1__LIBRARY_PREPARATION_DAYS_FROM_INDEX = Slot(uri=HTAN.LIBRARY_PREPARATION_DAYS_FROM_INDEX, name="bulkWESLevel1__LIBRARY_PREPARATION_DAYS_FROM_INDEX", curie=HTAN.curie('LIBRARY_PREPARATION_DAYS_FROM_INDEX'),
                   model_uri=HTAN.bulkWESLevel1__LIBRARY_PREPARATION_DAYS_FROM_INDEX, domain=None, range=Optional[int])

slots.bulkWESLevel1__SIZE_SELECTION_RANGE = Slot(uri=HTAN.SIZE_SELECTION_RANGE, name="bulkWESLevel1__SIZE_SELECTION_RANGE", curie=HTAN.curie('SIZE_SELECTION_RANGE'),
                   model_uri=HTAN.bulkWESLevel1__SIZE_SELECTION_RANGE, domain=None, range=Optional[str])

slots.bulkWESLevel1__TARGET_DEPTH = Slot(uri=HTAN.TARGET_DEPTH, name="bulkWESLevel1__TARGET_DEPTH", curie=HTAN.curie('TARGET_DEPTH'),
                   model_uri=HTAN.bulkWESLevel1__TARGET_DEPTH, domain=None, range=Optional[int])

slots.bulkWESLevel1__TO_TRIM_ADAPTER_SEQUENCE = Slot(uri=HTAN.TO_TRIM_ADAPTER_SEQUENCE, name="bulkWESLevel1__TO_TRIM_ADAPTER_SEQUENCE", curie=HTAN.curie('TO_TRIM_ADAPTER_SEQUENCE'),
                   model_uri=HTAN.bulkWESLevel1__TO_TRIM_ADAPTER_SEQUENCE, domain=None, range=Optional[Union[bool, Bool]])

slots.bulkWESLevel2__ALIGNMENT_WORKFLOW_TYPE = Slot(uri=HTAN.ALIGNMENT_WORKFLOW_TYPE, name="bulkWESLevel2__ALIGNMENT_WORKFLOW_TYPE", curie=HTAN.curie('ALIGNMENT_WORKFLOW_TYPE'),
                   model_uri=HTAN.bulkWESLevel2__ALIGNMENT_WORKFLOW_TYPE, domain=None, range=str)

slots.bulkWESLevel2__INDEX_FILE_NAME = Slot(uri=HTAN.INDEX_FILE_NAME, name="bulkWESLevel2__INDEX_FILE_NAME", curie=HTAN.curie('INDEX_FILE_NAME'),
                   model_uri=HTAN.bulkWESLevel2__INDEX_FILE_NAME, domain=None, range=Optional[str])

slots.bulkWESLevel2__AVERAGE_BASE_QUALITY = Slot(uri=HTAN.AVERAGE_BASE_QUALITY, name="bulkWESLevel2__AVERAGE_BASE_QUALITY", curie=HTAN.curie('AVERAGE_BASE_QUALITY'),
                   model_uri=HTAN.bulkWESLevel2__AVERAGE_BASE_QUALITY, domain=None, range=Optional[float])

slots.bulkWESLevel2__AVERAGE_INSERT_SIZE = Slot(uri=HTAN.AVERAGE_INSERT_SIZE, name="bulkWESLevel2__AVERAGE_INSERT_SIZE", curie=HTAN.curie('AVERAGE_INSERT_SIZE'),
                   model_uri=HTAN.bulkWESLevel2__AVERAGE_INSERT_SIZE, domain=None, range=Optional[int])

slots.bulkWESLevel2__AVERAGE_READ_LENGTH = Slot(uri=HTAN.AVERAGE_READ_LENGTH, name="bulkWESLevel2__AVERAGE_READ_LENGTH", curie=HTAN.curie('AVERAGE_READ_LENGTH'),
                   model_uri=HTAN.bulkWESLevel2__AVERAGE_READ_LENGTH, domain=None, range=Optional[int])

slots.bulkWESLevel2__CONTAMINATION = Slot(uri=HTAN.CONTAMINATION, name="bulkWESLevel2__CONTAMINATION", curie=HTAN.curie('CONTAMINATION'),
                   model_uri=HTAN.bulkWESLevel2__CONTAMINATION, domain=None, range=Optional[float])

slots.bulkWESLevel2__CONTAMINATION_ERROR = Slot(uri=HTAN.CONTAMINATION_ERROR, name="bulkWESLevel2__CONTAMINATION_ERROR", curie=HTAN.curie('CONTAMINATION_ERROR'),
                   model_uri=HTAN.bulkWESLevel2__CONTAMINATION_ERROR, domain=None, range=Optional[float])

slots.bulkWESLevel2__MEAN_COVERAGE = Slot(uri=HTAN.MEAN_COVERAGE, name="bulkWESLevel2__MEAN_COVERAGE", curie=HTAN.curie('MEAN_COVERAGE'),
                   model_uri=HTAN.bulkWESLevel2__MEAN_COVERAGE, domain=None, range=float)

slots.bulkWESLevel2__ADAPTER_CONTENT = Slot(uri=HTAN.ADAPTER_CONTENT, name="bulkWESLevel2__ADAPTER_CONTENT", curie=HTAN.curie('ADAPTER_CONTENT'),
                   model_uri=HTAN.bulkWESLevel2__ADAPTER_CONTENT, domain=None, range=Optional[str])

slots.bulkWESLevel2__BASIC_STATISTICS = Slot(uri=HTAN.BASIC_STATISTICS, name="bulkWESLevel2__BASIC_STATISTICS", curie=HTAN.curie('BASIC_STATISTICS'),
                   model_uri=HTAN.bulkWESLevel2__BASIC_STATISTICS, domain=None, range=Optional[str])

slots.bulkWESLevel2__ENCODING = Slot(uri=HTAN.ENCODING, name="bulkWESLevel2__ENCODING", curie=HTAN.curie('ENCODING'),
                   model_uri=HTAN.bulkWESLevel2__ENCODING, domain=None, range=Optional[str])

slots.bulkWESLevel2__OVERREPRESENTED_SEQUENCES = Slot(uri=HTAN.OVERREPRESENTED_SEQUENCES, name="bulkWESLevel2__OVERREPRESENTED_SEQUENCES", curie=HTAN.curie('OVERREPRESENTED_SEQUENCES'),
                   model_uri=HTAN.bulkWESLevel2__OVERREPRESENTED_SEQUENCES, domain=None, range=Optional[str])

slots.bulkWESLevel2__PER_BASE_N_CONTENT = Slot(uri=HTAN.PER_BASE_N_CONTENT, name="bulkWESLevel2__PER_BASE_N_CONTENT", curie=HTAN.curie('PER_BASE_N_CONTENT'),
                   model_uri=HTAN.bulkWESLevel2__PER_BASE_N_CONTENT, domain=None, range=Optional[str])

slots.bulkWESLevel2__PER_BASE_SEQUENCE_CONTENT = Slot(uri=HTAN.PER_BASE_SEQUENCE_CONTENT, name="bulkWESLevel2__PER_BASE_SEQUENCE_CONTENT", curie=HTAN.curie('PER_BASE_SEQUENCE_CONTENT'),
                   model_uri=HTAN.bulkWESLevel2__PER_BASE_SEQUENCE_CONTENT, domain=None, range=Optional[str])

slots.bulkWESLevel2__PER_BASE_SEQUENCE_QUALITY = Slot(uri=HTAN.PER_BASE_SEQUENCE_QUALITY, name="bulkWESLevel2__PER_BASE_SEQUENCE_QUALITY", curie=HTAN.curie('PER_BASE_SEQUENCE_QUALITY'),
                   model_uri=HTAN.bulkWESLevel2__PER_BASE_SEQUENCE_QUALITY, domain=None, range=Optional[str])

slots.bulkWESLevel2__PER_SEQUENCE_GC_CONTENT = Slot(uri=HTAN.PER_SEQUENCE_GC_CONTENT, name="bulkWESLevel2__PER_SEQUENCE_GC_CONTENT", curie=HTAN.curie('PER_SEQUENCE_GC_CONTENT'),
                   model_uri=HTAN.bulkWESLevel2__PER_SEQUENCE_GC_CONTENT, domain=None, range=Optional[str])

slots.bulkWESLevel2__PER_SEQUENCE_QUALITY_SCORE = Slot(uri=HTAN.PER_SEQUENCE_QUALITY_SCORE, name="bulkWESLevel2__PER_SEQUENCE_QUALITY_SCORE", curie=HTAN.curie('PER_SEQUENCE_QUALITY_SCORE'),
                   model_uri=HTAN.bulkWESLevel2__PER_SEQUENCE_QUALITY_SCORE, domain=None, range=Optional[str])

slots.bulkWESLevel2__PER_TILE_SEQUENCE_QUALITY = Slot(uri=HTAN.PER_TILE_SEQUENCE_QUALITY, name="bulkWESLevel2__PER_TILE_SEQUENCE_QUALITY", curie=HTAN.curie('PER_TILE_SEQUENCE_QUALITY'),
                   model_uri=HTAN.bulkWESLevel2__PER_TILE_SEQUENCE_QUALITY, domain=None, range=Optional[str])

slots.bulkWESLevel2__PERCENT_GC_CONTENT = Slot(uri=HTAN.PERCENT_GC_CONTENT, name="bulkWESLevel2__PERCENT_GC_CONTENT", curie=HTAN.curie('PERCENT_GC_CONTENT'),
                   model_uri=HTAN.bulkWESLevel2__PERCENT_GC_CONTENT, domain=None, range=Optional[float])

slots.bulkWESLevel2__SEQUENCE_DUPLICATION_LEVELS = Slot(uri=HTAN.SEQUENCE_DUPLICATION_LEVELS, name="bulkWESLevel2__SEQUENCE_DUPLICATION_LEVELS", curie=HTAN.curie('SEQUENCE_DUPLICATION_LEVELS'),
                   model_uri=HTAN.bulkWESLevel2__SEQUENCE_DUPLICATION_LEVELS, domain=None, range=Optional[str])

slots.bulkWESLevel2__SEQUENCE_LENGTH_DISTRIBUTION = Slot(uri=HTAN.SEQUENCE_LENGTH_DISTRIBUTION, name="bulkWESLevel2__SEQUENCE_LENGTH_DISTRIBUTION", curie=HTAN.curie('SEQUENCE_LENGTH_DISTRIBUTION'),
                   model_uri=HTAN.bulkWESLevel2__SEQUENCE_LENGTH_DISTRIBUTION, domain=None, range=Optional[str])

slots.bulkWESLevel2__QC_WORKFLOW_TYPE = Slot(uri=HTAN.QC_WORKFLOW_TYPE, name="bulkWESLevel2__QC_WORKFLOW_TYPE", curie=HTAN.curie('QC_WORKFLOW_TYPE'),
                   model_uri=HTAN.bulkWESLevel2__QC_WORKFLOW_TYPE, domain=None, range=Optional[str])

slots.bulkWESLevel2__QC_WORKFLOW_VERSION = Slot(uri=HTAN.QC_WORKFLOW_VERSION, name="bulkWESLevel2__QC_WORKFLOW_VERSION", curie=HTAN.curie('QC_WORKFLOW_VERSION'),
                   model_uri=HTAN.bulkWESLevel2__QC_WORKFLOW_VERSION, domain=None, range=Optional[str])

slots.bulkWESLevel2__QC_WORKFLOW_LINK = Slot(uri=HTAN.QC_WORKFLOW_LINK, name="bulkWESLevel2__QC_WORKFLOW_LINK", curie=HTAN.curie('QC_WORKFLOW_LINK'),
                   model_uri=HTAN.bulkWESLevel2__QC_WORKFLOW_LINK, domain=None, range=Optional[str])

slots.bulkWESLevel2__PAIRS_ON_DIFF_CHR = Slot(uri=HTAN.PAIRS_ON_DIFF_CHR, name="bulkWESLevel2__PAIRS_ON_DIFF_CHR", curie=HTAN.curie('PAIRS_ON_DIFF_CHR'),
                   model_uri=HTAN.bulkWESLevel2__PAIRS_ON_DIFF_CHR, domain=None, range=Optional[int])

slots.bulkWESLevel2__TOTAL_READS = Slot(uri=HTAN.TOTAL_READS, name="bulkWESLevel2__TOTAL_READS", curie=HTAN.curie('TOTAL_READS'),
                   model_uri=HTAN.bulkWESLevel2__TOTAL_READS, domain=None, range=int)

slots.bulkWESLevel2__TOTAL_UNIQUELY_MAPPED = Slot(uri=HTAN.TOTAL_UNIQUELY_MAPPED, name="bulkWESLevel2__TOTAL_UNIQUELY_MAPPED", curie=HTAN.curie('TOTAL_UNIQUELY_MAPPED'),
                   model_uri=HTAN.bulkWESLevel2__TOTAL_UNIQUELY_MAPPED, domain=None, range=int)

slots.bulkWESLevel2__TOTAL_UNMAPPED_READS = Slot(uri=HTAN.TOTAL_UNMAPPED_READS, name="bulkWESLevel2__TOTAL_UNMAPPED_READS", curie=HTAN.curie('TOTAL_UNMAPPED_READS'),
                   model_uri=HTAN.bulkWESLevel2__TOTAL_UNMAPPED_READS, domain=None, range=int)

slots.bulkWESLevel2__PROPORTION_READS_DUPLICATED = Slot(uri=HTAN.PROPORTION_READS_DUPLICATED, name="bulkWESLevel2__PROPORTION_READS_DUPLICATED", curie=HTAN.curie('PROPORTION_READS_DUPLICATED'),
                   model_uri=HTAN.bulkWESLevel2__PROPORTION_READS_DUPLICATED, domain=None, range=Optional[float])

slots.bulkWESLevel2__PROPORTION_READS_MAPPED = Slot(uri=HTAN.PROPORTION_READS_MAPPED, name="bulkWESLevel2__PROPORTION_READS_MAPPED", curie=HTAN.curie('PROPORTION_READS_MAPPED'),
                   model_uri=HTAN.bulkWESLevel2__PROPORTION_READS_MAPPED, domain=None, range=float)

slots.bulkWESLevel2__PROPORTION_TARGETS_NO_COVERAGE = Slot(uri=HTAN.PROPORTION_TARGETS_NO_COVERAGE, name="bulkWESLevel2__PROPORTION_TARGETS_NO_COVERAGE", curie=HTAN.curie('PROPORTION_TARGETS_NO_COVERAGE'),
                   model_uri=HTAN.bulkWESLevel2__PROPORTION_TARGETS_NO_COVERAGE, domain=None, range=Optional[float])

slots.bulkWESLevel2__PROPORTION_BASE_MISMATCH = Slot(uri=HTAN.PROPORTION_BASE_MISMATCH, name="bulkWESLevel2__PROPORTION_BASE_MISMATCH", curie=HTAN.curie('PROPORTION_BASE_MISMATCH'),
                   model_uri=HTAN.bulkWESLevel2__PROPORTION_BASE_MISMATCH, domain=None, range=Optional[float])

slots.bulkWESLevel2__SHORT_READS = Slot(uri=HTAN.SHORT_READS, name="bulkWESLevel2__SHORT_READS", curie=HTAN.curie('SHORT_READS'),
                   model_uri=HTAN.bulkWESLevel2__SHORT_READS, domain=None, range=Optional[int])

slots.bulkWESLevel2__PROPORTION_COVERAGE_10X = Slot(uri=HTAN.PROPORTION_COVERAGE_10X, name="bulkWESLevel2__PROPORTION_COVERAGE_10X", curie=HTAN.curie('PROPORTION_COVERAGE_10X'),
                   model_uri=HTAN.bulkWESLevel2__PROPORTION_COVERAGE_10X, domain=None, range=Optional[float])

slots.bulkWESLevel2__PROPORTION_COVERAGE_30X = Slot(uri=HTAN.PROPORTION_COVERAGE_30X, name="bulkWESLevel2__PROPORTION_COVERAGE_30X", curie=HTAN.curie('PROPORTION_COVERAGE_30X'),
                   model_uri=HTAN.bulkWESLevel2__PROPORTION_COVERAGE_30X, domain=None, range=Optional[float])

slots.bulkWESLevel2__IS_LOWEST_LEVEL = Slot(uri=HTAN.IS_LOWEST_LEVEL, name="bulkWESLevel2__IS_LOWEST_LEVEL", curie=HTAN.curie('IS_LOWEST_LEVEL'),
                   model_uri=HTAN.bulkWESLevel2__IS_LOWEST_LEVEL, domain=None, range=Optional[Union[bool, Bool]])

slots.bulkWESLevel3__GERMLINE_VARIANTS_WORKFLOW_URL = Slot(uri=HTAN.GERMLINE_VARIANTS_WORKFLOW_URL, name="bulkWESLevel3__GERMLINE_VARIANTS_WORKFLOW_URL", curie=HTAN.curie('GERMLINE_VARIANTS_WORKFLOW_URL'),
                   model_uri=HTAN.bulkWESLevel3__GERMLINE_VARIANTS_WORKFLOW_URL, domain=None, range=Optional[str])

slots.bulkWESLevel3__GERMLINE_VARIANTS_WORKFLOW_TYPE = Slot(uri=HTAN.GERMLINE_VARIANTS_WORKFLOW_TYPE, name="bulkWESLevel3__GERMLINE_VARIANTS_WORKFLOW_TYPE", curie=HTAN.curie('GERMLINE_VARIANTS_WORKFLOW_TYPE'),
                   model_uri=HTAN.bulkWESLevel3__GERMLINE_VARIANTS_WORKFLOW_TYPE, domain=None, range=Optional[str])

slots.bulkWESLevel3__SOMATIC_VARIANTS_WORKFLOW_URL = Slot(uri=HTAN.SOMATIC_VARIANTS_WORKFLOW_URL, name="bulkWESLevel3__SOMATIC_VARIANTS_WORKFLOW_URL", curie=HTAN.curie('SOMATIC_VARIANTS_WORKFLOW_URL'),
                   model_uri=HTAN.bulkWESLevel3__SOMATIC_VARIANTS_WORKFLOW_URL, domain=None, range=Optional[str])

slots.bulkWESLevel3__SOMATIC_VARIANTS_WORKFLOW_TYPE = Slot(uri=HTAN.SOMATIC_VARIANTS_WORKFLOW_TYPE, name="bulkWESLevel3__SOMATIC_VARIANTS_WORKFLOW_TYPE", curie=HTAN.curie('SOMATIC_VARIANTS_WORKFLOW_TYPE'),
                   model_uri=HTAN.bulkWESLevel3__SOMATIC_VARIANTS_WORKFLOW_TYPE, domain=None, range=Optional[str])

slots.bulkWESLevel3__SOMATIC_VARIANTS_SAMPLE_TYPE = Slot(uri=HTAN.SOMATIC_VARIANTS_SAMPLE_TYPE, name="bulkWESLevel3__SOMATIC_VARIANTS_SAMPLE_TYPE", curie=HTAN.curie('SOMATIC_VARIANTS_SAMPLE_TYPE'),
                   model_uri=HTAN.bulkWESLevel3__SOMATIC_VARIANTS_SAMPLE_TYPE, domain=None, range=Optional[Union[str, "SomaticVariantsSampleTypeEnum"]])

slots.bulkWESLevel3__STRUCTURAL_VARIANT_WORKFLOW_URL = Slot(uri=HTAN.STRUCTURAL_VARIANT_WORKFLOW_URL, name="bulkWESLevel3__STRUCTURAL_VARIANT_WORKFLOW_URL", curie=HTAN.curie('STRUCTURAL_VARIANT_WORKFLOW_URL'),
                   model_uri=HTAN.bulkWESLevel3__STRUCTURAL_VARIANT_WORKFLOW_URL, domain=None, range=Optional[str])

slots.bulkWESLevel3__STRUCTURAL_VARIANT_WORKFLOW_TYPE = Slot(uri=HTAN.STRUCTURAL_VARIANT_WORKFLOW_TYPE, name="bulkWESLevel3__STRUCTURAL_VARIANT_WORKFLOW_TYPE", curie=HTAN.curie('STRUCTURAL_VARIANT_WORKFLOW_TYPE'),
                   model_uri=HTAN.bulkWESLevel3__STRUCTURAL_VARIANT_WORKFLOW_TYPE, domain=None, range=Optional[str])

slots.bulkWESLevel3__MSI_WORKFLOW_LINK = Slot(uri=HTAN.MSI_WORKFLOW_LINK, name="bulkWESLevel3__MSI_WORKFLOW_LINK", curie=HTAN.curie('MSI_WORKFLOW_LINK'),
                   model_uri=HTAN.bulkWESLevel3__MSI_WORKFLOW_LINK, domain=None, range=Optional[str])

slots.bulkWESLevel3__MSI_SCORE = Slot(uri=HTAN.MSI_SCORE, name="bulkWESLevel3__MSI_SCORE", curie=HTAN.curie('MSI_SCORE'),
                   model_uri=HTAN.bulkWESLevel3__MSI_SCORE, domain=None, range=Optional[float])

slots.bulkWESLevel3__MSI_STATUS = Slot(uri=HTAN.MSI_STATUS, name="bulkWESLevel3__MSI_STATUS", curie=HTAN.curie('MSI_STATUS'),
                   model_uri=HTAN.bulkWESLevel3__MSI_STATUS, domain=None, range=Optional[Union[str, "MSIStatusEnum"]])

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
