# Auto generated from sequencing.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-27T14:51:46
# Schema: Sequencing
#
# id: https://w3id.org/htan/sequencing
# description: HTAN Base Sequencing Data Model - Common attributes shared across all sequencing modules
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

from linkml_runtime.linkml_model.types import Integer, String

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
