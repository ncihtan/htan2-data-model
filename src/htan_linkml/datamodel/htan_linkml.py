# Auto generated from htan_linkml.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-28T20:36:20
# Schema: htan-linkml
#
# id: https://w3id.org/ncihtan/htan-linkml
# description: A LinkML data model for HTAN Phase 2
# license: MIT

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

from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
HTAN_LINKML = CurieNamespace('htan_linkml', 'https://w3id.org/ncihtan/htan-linkml/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN_LINKML


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class StudyId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = HTAN_LINKML.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(NamedThing):
    """
    Represents a Study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN_LINKML["Study"]
    class_class_curie: ClassVar[str] = "htan_linkml:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = HTAN_LINKML.Study

    id: Union[str, StudyId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyCollection(YAMLRoot):
    """
    A holder for Study objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN_LINKML["StudyCollection"]
    class_class_curie: ClassVar[str] = "htan_linkml:StudyCollection"
    class_name: ClassVar[str] = "StudyCollection"
    class_model_uri: ClassVar[URIRef] = HTAN_LINKML.StudyCollection

    entries: Optional[Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Study, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=HTAN_LINKML.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=HTAN_LINKML.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=HTAN_LINKML.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HTAN_LINKML.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=HTAN_LINKML.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=HTAN_LINKML.age_in_years, name="age_in_years", curie=HTAN_LINKML.curie('age_in_years'),
                   model_uri=HTAN_LINKML.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=HTAN_LINKML.vital_status, name="vital_status", curie=HTAN_LINKML.curie('vital_status'),
                   model_uri=HTAN_LINKML.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.studyCollection__entries = Slot(uri=HTAN_LINKML.entries, name="studyCollection__entries", curie=HTAN_LINKML.curie('entries'),
                   model_uri=HTAN_LINKML.studyCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, StudyId], Union[dict, Study]], List[Union[dict, Study]]]])

slots.Study_primary_email = Slot(uri=SCHEMA.email, name="Study_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HTAN_LINKML.Study_primary_email, domain=Study, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))