# Auto generated from participant.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-08-27T14:51:45
# Schema: Participant
#
# id: https://w3id.org/htan/participant
# description: HTAN Participant Data Model - Attributes for participant-based modules
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

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN


# Types

# Class references
class CoreFileAttributesHTANDATAFILEID(extended_str):
    pass


class ParticipantAttributesHTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
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
class ParticipantAttributes(CoreFileAttributes):
    """
    Attributes for modules that require participant identification
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ParticipantAttributes"]
    class_class_curie: ClassVar[str] = "htan:ParticipantAttributes"
    class_name: ClassVar[str] = "ParticipantAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.ParticipantAttributes

    HTAN_DATA_FILE_ID: Union[str, ParticipantAttributesHTANDATAFILEID] = None
    COMPONENT: str = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    HTAN_PARTICIPANT_ID: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ParticipantAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ParticipantAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.HTAN_PARTICIPANT_ID):
            self.MissingRequiredField("HTAN_PARTICIPANT_ID")
        if not isinstance(self.HTAN_PARTICIPANT_ID, str):
            self.HTAN_PARTICIPANT_ID = str(self.HTAN_PARTICIPANT_ID)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.participantAttributes__HTAN_PARTICIPANT_ID = Slot(uri=HTAN.HTAN_PARTICIPANT_ID, name="participantAttributes__HTAN_PARTICIPANT_ID", curie=HTAN.curie('HTAN_PARTICIPANT_ID'),
                   model_uri=HTAN.participantAttributes__HTAN_PARTICIPANT_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))$'))

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
