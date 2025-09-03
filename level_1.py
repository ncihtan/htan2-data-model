# Auto generated from level_1.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-28T13:04:06
# Schema: Level1
#
# id: https://w3id.org/htan/wes/level_1
# description: Bulk Whole Exome Sequencing Level 1 - Raw files
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


class BulkWESLevel1HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


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
    HTAN_PARTICIPANT_ID: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None

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

        if self._is_empty(self.HTAN_PARTICIPANT_ID):
            self.MissingRequiredField("HTAN_PARTICIPANT_ID")
        if not isinstance(self.HTAN_PARTICIPANT_ID, str):
            self.HTAN_PARTICIPANT_ID = str(self.HTAN_PARTICIPANT_ID)

        if self._is_empty(self.HTAN_PARENT_ID):
            self.MissingRequiredField("HTAN_PARENT_ID")
        if not isinstance(self.HTAN_PARENT_ID, str):
            self.HTAN_PARENT_ID = str(self.HTAN_PARENT_ID)

        if self._is_empty(self.HTAN_BIOSPECIMEN_ID):
            self.MissingRequiredField("HTAN_BIOSPECIMEN_ID")
        if not isinstance(self.HTAN_BIOSPECIMEN_ID, str):
            self.HTAN_BIOSPECIMEN_ID = str(self.HTAN_BIOSPECIMEN_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BulkWESLevel1(CoreFileAttributes):
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
    HTAN_PARTICIPANT_ID: str = None
    HTAN_PARENT_ID: str = None
    HTAN_BIOSPECIMEN_ID: str = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    LIBRARY_SELECTION_METHOD: Union[str, "LibrarySelectionMethodEnum"] = None
    READ_LENGTH: int = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    SEQUENCING_BATCH_ID: Optional[str] = None
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

        if self._is_empty(self.LIBRARY_LAYOUT):
            self.MissingRequiredField("LIBRARY_LAYOUT")
        if not isinstance(self.LIBRARY_LAYOUT, LibraryLayoutEnum):
            self.LIBRARY_LAYOUT = LibraryLayoutEnum(self.LIBRARY_LAYOUT)

        if self._is_empty(self.LIBRARY_SELECTION_METHOD):
            self.MissingRequiredField("LIBRARY_SELECTION_METHOD")
        if not isinstance(self.LIBRARY_SELECTION_METHOD, LibrarySelectionMethodEnum):
            self.LIBRARY_SELECTION_METHOD = LibrarySelectionMethodEnum(self.LIBRARY_SELECTION_METHOD)

        if self._is_empty(self.READ_LENGTH):
            self.MissingRequiredField("READ_LENGTH")
        if not isinstance(self.READ_LENGTH, int):
            self.READ_LENGTH = int(self.READ_LENGTH)

        if self._is_empty(self.SEQUENCING_PLATFORM):
            self.MissingRequiredField("SEQUENCING_PLATFORM")
        if not isinstance(self.SEQUENCING_PLATFORM, SequencingPlatformEnum):
            self.SEQUENCING_PLATFORM = SequencingPlatformEnum(self.SEQUENCING_PLATFORM)

        if self.SEQUENCING_BATCH_ID is not None and not isinstance(self.SEQUENCING_BATCH_ID, str):
            self.SEQUENCING_BATCH_ID = str(self.SEQUENCING_BATCH_ID)

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


# Enumerations
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

slots.bulkWESLevel1__SEQUENCING_BATCH_ID = Slot(uri=HTAN.SEQUENCING_BATCH_ID, name="bulkWESLevel1__SEQUENCING_BATCH_ID", curie=HTAN.curie('SEQUENCING_BATCH_ID'),
                   model_uri=HTAN.bulkWESLevel1__SEQUENCING_BATCH_ID, domain=None, range=Optional[str])

slots.bulkWESLevel1__LIBRARY_LAYOUT = Slot(uri=HTAN.LIBRARY_LAYOUT, name="bulkWESLevel1__LIBRARY_LAYOUT", curie=HTAN.curie('LIBRARY_LAYOUT'),
                   model_uri=HTAN.bulkWESLevel1__LIBRARY_LAYOUT, domain=None, range=Union[str, "LibraryLayoutEnum"])

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

slots.bulkWESLevel1__SEQUENCING_PLATFORM = Slot(uri=HTAN.SEQUENCING_PLATFORM, name="bulkWESLevel1__SEQUENCING_PLATFORM", curie=HTAN.curie('SEQUENCING_PLATFORM'),
                   model_uri=HTAN.bulkWESLevel1__SEQUENCING_PLATFORM, domain=None, range=Union[str, "SequencingPlatformEnum"])

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

slots.coreFileAttributes__COMPONENT = Slot(uri=HTAN.COMPONENT, name="coreFileAttributes__COMPONENT", curie=HTAN.curie('COMPONENT'),
                   model_uri=HTAN.coreFileAttributes__COMPONENT, domain=None, range=str)

slots.coreFileAttributes__FILENAME = Slot(uri=HTAN.FILENAME, name="coreFileAttributes__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.coreFileAttributes__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+[\\/]\S*$'))

slots.coreFileAttributes__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="coreFileAttributes__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.coreFileAttributes__FILE_FORMAT, domain=None, range=str)

slots.coreFileAttributes__HTAN_PARTICIPANT_ID = Slot(uri=HTAN.HTAN_PARTICIPANT_ID, name="coreFileAttributes__HTAN_PARTICIPANT_ID", curie=HTAN.curie('HTAN_PARTICIPANT_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_PARTICIPANT_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))$'))

slots.coreFileAttributes__HTAN_DATA_FILE_ID = Slot(uri=HTAN.HTAN_DATA_FILE_ID, name="coreFileAttributes__HTAN_DATA_FILE_ID", curie=HTAN.curie('HTAN_DATA_FILE_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_DATA_FILE_ID, domain=None, range=URIRef,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$'))

slots.coreFileAttributes__HTAN_PARENT_ID = Slot(uri=HTAN.HTAN_PARENT_ID, name="coreFileAttributes__HTAN_PARENT_ID", curie=HTAN.curie('HTAN_PARENT_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_PARENT_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA20[0-9])(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$'))

slots.coreFileAttributes__HTAN_BIOSPECIMEN_ID = Slot(uri=HTAN.HTAN_BIOSPECIMEN_ID, name="coreFileAttributes__HTAN_BIOSPECIMEN_ID", curie=HTAN.curie('HTAN_BIOSPECIMEN_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_BIOSPECIMEN_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$'))