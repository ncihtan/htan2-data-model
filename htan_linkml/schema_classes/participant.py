# Auto generated from participant.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-14T10:05:53
# Schema: Participant
#
# id: https://w3id.org/htan/participant
# description: HTAN Participant Data Model Schema
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

from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN


# Types

# Class references
class ParticipantParticipantId(extended_str):
    pass


@dataclass(repr=False)
class Participant(YAMLRoot):
    """
    Information about a participant in the study
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["Participant"]
    class_class_curie: ClassVar[str] = "htan:Participant"
    class_name: ClassVar[str] = "Participant"
    class_model_uri: ClassVar[URIRef] = HTAN.Participant

    participant_id: Union[str, ParticipantParticipantId] = None
    age_at_enrollment_days: int = None
    race: Union[str, "RaceEnum"] = None
    ethnicity: Union[str, "EthnicityEnum"] = None
    gender: Union[str, "GenderEnum"] = None
    vital_status: Union[str, "VitalStatusEnum"] = None
    sex: Optional[Union[str, "SexEnum"]] = None
    year_of_birth: Optional[int] = None
    year_of_death: Optional[int] = None
    cause_of_death: Optional[str] = None
    height_cm: Optional[float] = None
    weight_kg: Optional[float] = None
    bmi: Optional[float] = None
    country_of_residence: Optional[str] = None
    state_of_residence: Optional[str] = None
    zip_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, ParticipantParticipantId):
            self.participant_id = ParticipantParticipantId(self.participant_id)

        if self._is_empty(self.age_at_enrollment_days):
            self.MissingRequiredField("age_at_enrollment_days")
        if not isinstance(self.age_at_enrollment_days, int):
            self.age_at_enrollment_days = int(self.age_at_enrollment_days)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self._is_empty(self.gender):
            self.MissingRequiredField("gender")
        if not isinstance(self.gender, GenderEnum):
            self.gender = GenderEnum(self.gender)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, VitalStatusEnum):
            self.vital_status = VitalStatusEnum(self.vital_status)

        if self.sex is not None and not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self.year_of_birth is not None and not isinstance(self.year_of_birth, int):
            self.year_of_birth = int(self.year_of_birth)

        if self.year_of_death is not None and not isinstance(self.year_of_death, int):
            self.year_of_death = int(self.year_of_death)

        if self.cause_of_death is not None and not isinstance(self.cause_of_death, str):
            self.cause_of_death = str(self.cause_of_death)

        if self.height_cm is not None and not isinstance(self.height_cm, float):
            self.height_cm = float(self.height_cm)

        if self.weight_kg is not None and not isinstance(self.weight_kg, float):
            self.weight_kg = float(self.weight_kg)

        if self.bmi is not None and not isinstance(self.bmi, float):
            self.bmi = float(self.bmi)

        if self.country_of_residence is not None and not isinstance(self.country_of_residence, str):
            self.country_of_residence = str(self.country_of_residence)

        if self.state_of_residence is not None and not isinstance(self.state_of_residence, str):
            self.state_of_residence = str(self.state_of_residence)

        if self.zip_code is not None and not isinstance(self.zip_code, str):
            self.zip_code = str(self.zip_code)

        super().__post_init__(**kwargs)


# Enumerations
class RaceEnum(EnumDefinitionImpl):

    White = PermissibleValue(text="White")
    Asian = PermissibleValue(text="Asian")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="RaceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "American Indian or Alaska Native",
            PermissibleValue(text="American Indian or Alaska Native"))
        setattr(cls, "Black or African American",
            PermissibleValue(text="Black or African American"))
        setattr(cls, "Native Hawaiian or Other Pacific Islander",
            PermissibleValue(text="Native Hawaiian or Other Pacific Islander"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))
        setattr(cls, "Not Allowed to Collect",
            PermissibleValue(text="Not Allowed to Collect"))

class GenderEnum(EnumDefinitionImpl):

    Female = PermissibleValue(text="Female")
    Male = PermissibleValue(text="Male")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="GenderEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Non-Binary",
            PermissibleValue(text="Non-Binary"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))
        setattr(cls, "Prefer Not to Answer",
            PermissibleValue(text="Prefer Not to Answer"))

class SexEnum(EnumDefinitionImpl):

    Female = PermissibleValue(text="Female")
    Intersex = PermissibleValue(text="Intersex")
    Male = PermissibleValue(text="Male")
    Unknown = PermissibleValue(text="Unknown")
    X = PermissibleValue(text="X")

    _defn = EnumDefinition(
        name="SexEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Decline to answer",
            PermissibleValue(text="Decline to answer"))
        setattr(cls, "Don't know",
            PermissibleValue(text="Don't know"))
        setattr(cls, "None of these describe me",
            PermissibleValue(text="None of these describe me"))
        setattr(cls, "Prefer not to answer",
            PermissibleValue(text="Prefer not to answer"))

class EthnicityEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="EthnicityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hispanic or Latino",
            PermissibleValue(text="Hispanic or Latino"))
        setattr(cls, "Not Hispanic or Latino",
            PermissibleValue(text="Not Hispanic or Latino"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))
        setattr(cls, "Not Allowed to Collect",
            PermissibleValue(text="Not Allowed to Collect"))

class VitalStatusEnum(EnumDefinitionImpl):

    Alive = PermissibleValue(text="Alive")
    Dead = PermissibleValue(text="Dead")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="VitalStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class AdultOrChildhoodEnum(EnumDefinitionImpl):

    Adult = PermissibleValue(text="Adult")
    Pediatric = PermissibleValue(text="Pediatric")

    _defn = EnumDefinition(
        name="AdultOrChildhoodEnum",
    )

# Slots
class slots:
    pass

slots.participant__participant_id = Slot(uri=HTAN.participant_id, name="participant__participant_id", curie=HTAN.curie('participant_id'),
                   model_uri=HTAN.participant__participant_id, domain=None, range=URIRef)

slots.participant__age_at_enrollment_days = Slot(uri=HTAN.age_at_enrollment_days, name="participant__age_at_enrollment_days", curie=HTAN.curie('age_at_enrollment_days'),
                   model_uri=HTAN.participant__age_at_enrollment_days, domain=None, range=int)

slots.participant__race = Slot(uri=HTAN.race, name="participant__race", curie=HTAN.curie('race'),
                   model_uri=HTAN.participant__race, domain=None, range=Union[str, "RaceEnum"])

slots.participant__ethnicity = Slot(uri=HTAN.ethnicity, name="participant__ethnicity", curie=HTAN.curie('ethnicity'),
                   model_uri=HTAN.participant__ethnicity, domain=None, range=Union[str, "EthnicityEnum"])

slots.participant__gender = Slot(uri=HTAN.gender, name="participant__gender", curie=HTAN.curie('gender'),
                   model_uri=HTAN.participant__gender, domain=None, range=Union[str, "GenderEnum"])

slots.participant__sex = Slot(uri=HTAN.sex, name="participant__sex", curie=HTAN.curie('sex'),
                   model_uri=HTAN.participant__sex, domain=None, range=Optional[Union[str, "SexEnum"]])

slots.participant__vital_status = Slot(uri=HTAN.vital_status, name="participant__vital_status", curie=HTAN.curie('vital_status'),
                   model_uri=HTAN.participant__vital_status, domain=None, range=Union[str, "VitalStatusEnum"])

slots.participant__year_of_birth = Slot(uri=HTAN.year_of_birth, name="participant__year_of_birth", curie=HTAN.curie('year_of_birth'),
                   model_uri=HTAN.participant__year_of_birth, domain=None, range=Optional[int])

slots.participant__year_of_death = Slot(uri=HTAN.year_of_death, name="participant__year_of_death", curie=HTAN.curie('year_of_death'),
                   model_uri=HTAN.participant__year_of_death, domain=None, range=Optional[int])

slots.participant__cause_of_death = Slot(uri=HTAN.cause_of_death, name="participant__cause_of_death", curie=HTAN.curie('cause_of_death'),
                   model_uri=HTAN.participant__cause_of_death, domain=None, range=Optional[str])

slots.participant__height_cm = Slot(uri=HTAN.height_cm, name="participant__height_cm", curie=HTAN.curie('height_cm'),
                   model_uri=HTAN.participant__height_cm, domain=None, range=Optional[float])

slots.participant__weight_kg = Slot(uri=HTAN.weight_kg, name="participant__weight_kg", curie=HTAN.curie('weight_kg'),
                   model_uri=HTAN.participant__weight_kg, domain=None, range=Optional[float])

slots.participant__bmi = Slot(uri=HTAN.bmi, name="participant__bmi", curie=HTAN.curie('bmi'),
                   model_uri=HTAN.participant__bmi, domain=None, range=Optional[float])

slots.participant__country_of_residence = Slot(uri=HTAN.country_of_residence, name="participant__country_of_residence", curie=HTAN.curie('country_of_residence'),
                   model_uri=HTAN.participant__country_of_residence, domain=None, range=Optional[str])

slots.participant__state_of_residence = Slot(uri=HTAN.state_of_residence, name="participant__state_of_residence", curie=HTAN.curie('state_of_residence'),
                   model_uri=HTAN.participant__state_of_residence, domain=None, range=Optional[str])

slots.participant__zip_code = Slot(uri=HTAN.zip_code, name="participant__zip_code", curie=HTAN.curie('zip_code'),
                   model_uri=HTAN.participant__zip_code, domain=None, range=Optional[str])
