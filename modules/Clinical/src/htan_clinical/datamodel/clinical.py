# Auto generated from clinical.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-18T10:27:20
# Schema: Clinical
#
# id: https://w3id.org/htan/clinical
# description: HTAN Clinical Data Model Schema
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

from linkml_runtime.linkml_model.types import Decimal, Integer, String
from linkml_runtime.utils.metamodelcore import Decimal

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
CADSR = CurieNamespace('caDSR', 'https://cadsr.cancer.gov/onedata/')
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN


# Types

# Class references



@dataclass(repr=False)
class ClinicalData(YAMLRoot):
    """
    Container for all clinical data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ClinicalData"]
    class_class_curie: ClassVar[str] = "htan:ClinicalData"
    class_name: ClassVar[str] = "ClinicalData"
    class_model_uri: ClassVar[URIRef] = HTAN.ClinicalData

    COMPONENT: Union[str, "ComponentEnum"] = None
    HTAN_PARTICIPANT_ID: str = None
    DEMOGRAPHICS: Union[dict, "Demographics"] = None
    VITAL_STATUS: Union[dict, "VitalStatus"] = None
    DIAGNOSIS: Union[dict, "Diagnosis"] = None
    EXPOSURES: Union[dict, "Exposure"] = None
    FAMILY_HISTORY: Union[dict, "FamilyHistory"] = None
    FOLLOW_UPS: Optional[Union[Union[dict, "FollowUp"], List[Union[dict, "FollowUp"]]]] = empty_list()
    MOLECULAR_TESTS: Optional[Union[Union[dict, "MolecularTest"], List[Union[dict, "MolecularTest"]]]] = empty_list()
    THERAPIES: Optional[Union[Union[dict, "Therapy"], List[Union[dict, "Therapy"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.COMPONENT):
            self.MissingRequiredField("COMPONENT")
        if not isinstance(self.COMPONENT, ComponentEnum):
            self.COMPONENT = ComponentEnum(self.COMPONENT)

        if self._is_empty(self.HTAN_PARTICIPANT_ID):
            self.MissingRequiredField("HTAN_PARTICIPANT_ID")
        if not isinstance(self.HTAN_PARTICIPANT_ID, str):
            self.HTAN_PARTICIPANT_ID = str(self.HTAN_PARTICIPANT_ID)

        if self._is_empty(self.DEMOGRAPHICS):
            self.MissingRequiredField("DEMOGRAPHICS")
        if not isinstance(self.DEMOGRAPHICS, Demographics):
            self.DEMOGRAPHICS = Demographics(**as_dict(self.DEMOGRAPHICS))

        if self._is_empty(self.VITAL_STATUS):
            self.MissingRequiredField("VITAL_STATUS")
        if not isinstance(self.VITAL_STATUS, VitalStatus):
            self.VITAL_STATUS = VitalStatus(**as_dict(self.VITAL_STATUS))

        if self._is_empty(self.DIAGNOSIS):
            self.MissingRequiredField("DIAGNOSIS")
        if not isinstance(self.DIAGNOSIS, Diagnosis):
            self.DIAGNOSIS = Diagnosis(**as_dict(self.DIAGNOSIS))

        if self._is_empty(self.EXPOSURES):
            self.MissingRequiredField("EXPOSURES")
        if not isinstance(self.EXPOSURES, Exposure):
            self.EXPOSURES = Exposure(**as_dict(self.EXPOSURES))

        if self._is_empty(self.FAMILY_HISTORY):
            self.MissingRequiredField("FAMILY_HISTORY")
        if not isinstance(self.FAMILY_HISTORY, FamilyHistory):
            self.FAMILY_HISTORY = FamilyHistory(**as_dict(self.FAMILY_HISTORY))

        self._normalize_inlined_as_dict(slot_name="FOLLOW_UPS", slot_type=FollowUp, key_name="AGE_IN_DAYS_AT_FOLLOWUP", keyed=False)

        self._normalize_inlined_as_dict(slot_name="MOLECULAR_TESTS", slot_type=MolecularTest, key_name="TIMEPOINT_LABEL", keyed=False)

        self._normalize_inlined_as_dict(slot_name="THERAPIES", slot_type=Therapy, key_name="INITIAL_DISEASE_STATUS", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Demographics(YAMLRoot):
    """
    Information about the demographics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/demographics/Demographics"]
    class_class_curie: ClassVar[str] = "htan:clinical/demographics/Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = HTAN.Demographics

    ETHNIC_GROUP: Union[str, "EthnicGroupEnum"] = None
    GENDER_IDENTITY: Union[str, "GenderIdentityEnum"] = None
    SEX: Union[str, "SexEnum"] = None
    RACE: Union[str, "RaceEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ETHNIC_GROUP):
            self.MissingRequiredField("ETHNIC_GROUP")
        if not isinstance(self.ETHNIC_GROUP, EthnicGroupEnum):
            self.ETHNIC_GROUP = EthnicGroupEnum(self.ETHNIC_GROUP)

        if self._is_empty(self.GENDER_IDENTITY):
            self.MissingRequiredField("GENDER_IDENTITY")
        if not isinstance(self.GENDER_IDENTITY, GenderIdentityEnum):
            self.GENDER_IDENTITY = GenderIdentityEnum(self.GENDER_IDENTITY)

        if self._is_empty(self.SEX):
            self.MissingRequiredField("SEX")
        if not isinstance(self.SEX, SexEnum):
            self.SEX = SexEnum(self.SEX)

        if self._is_empty(self.RACE):
            self.MissingRequiredField("RACE")
        if not isinstance(self.RACE, RaceEnum):
            self.RACE = RaceEnum(self.RACE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diagnosis(YAMLRoot):
    """
    Information about the diagnosis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/diagnosis/Diagnosis"]
    class_class_curie: ClassVar[str] = "htan:clinical/diagnosis/Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = HTAN.Diagnosis

    PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID: str = None
    AGE_IN_DAYS_AT_DIAGNOSIS: int = None
    TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE: str = None
    TUMOR_GRADE: Union[str, "TumorGradeEnum"] = None
    CLINICAL_T_STAGE: Union[str, "ClinicalTStageEnum"] = None
    CLINICAL_N_STAGE: Union[str, "ClinicalNStageEnum"] = None
    CLINICAL_M_STAGE: Union[str, "ClinicalMStageEnum"] = None
    AJCC_STAGING_SYSTEM_EDITION: Union[str, "AJCCStagingSystemEditionEnum"] = None
    AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS: int = None
    LAST_KNOWN_DISEASE_STATUS: Union[str, "LastKnownDiseaseStatusEnum"] = None
    TUMOR_CLASSIFICATION_CATEGORY: Union[str, "TumorClassificationCategoryEnum"] = None
    METASTASIS_AT_DIAGNOSIS: Union[str, "MetastasisAtDiagnosisEnum"] = None
    METHOD_OF_DIAGNOSIS: Union[str, "MethodOfDiagnosisEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID):
            self.MissingRequiredField("PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID")
        if not isinstance(self.PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID, str):
            self.PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID = str(self.PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID)

        if self._is_empty(self.AGE_IN_DAYS_AT_DIAGNOSIS):
            self.MissingRequiredField("AGE_IN_DAYS_AT_DIAGNOSIS")
        if not isinstance(self.AGE_IN_DAYS_AT_DIAGNOSIS, int):
            self.AGE_IN_DAYS_AT_DIAGNOSIS = int(self.AGE_IN_DAYS_AT_DIAGNOSIS)

        if self._is_empty(self.TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE):
            self.MissingRequiredField("TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE")
        if not isinstance(self.TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE, str):
            self.TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE = str(self.TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE)

        if self._is_empty(self.TUMOR_GRADE):
            self.MissingRequiredField("TUMOR_GRADE")
        if not isinstance(self.TUMOR_GRADE, TumorGradeEnum):
            self.TUMOR_GRADE = TumorGradeEnum(self.TUMOR_GRADE)

        if self._is_empty(self.CLINICAL_T_STAGE):
            self.MissingRequiredField("CLINICAL_T_STAGE")
        if not isinstance(self.CLINICAL_T_STAGE, ClinicalTStageEnum):
            self.CLINICAL_T_STAGE = ClinicalTStageEnum(self.CLINICAL_T_STAGE)

        if self._is_empty(self.CLINICAL_N_STAGE):
            self.MissingRequiredField("CLINICAL_N_STAGE")
        if not isinstance(self.CLINICAL_N_STAGE, ClinicalNStageEnum):
            self.CLINICAL_N_STAGE = ClinicalNStageEnum(self.CLINICAL_N_STAGE)

        if self._is_empty(self.CLINICAL_M_STAGE):
            self.MissingRequiredField("CLINICAL_M_STAGE")
        if not isinstance(self.CLINICAL_M_STAGE, ClinicalMStageEnum):
            self.CLINICAL_M_STAGE = ClinicalMStageEnum(self.CLINICAL_M_STAGE)

        if self._is_empty(self.AJCC_STAGING_SYSTEM_EDITION):
            self.MissingRequiredField("AJCC_STAGING_SYSTEM_EDITION")
        if not isinstance(self.AJCC_STAGING_SYSTEM_EDITION, AJCCStagingSystemEditionEnum):
            self.AJCC_STAGING_SYSTEM_EDITION = AJCCStagingSystemEditionEnum(self.AJCC_STAGING_SYSTEM_EDITION)

        if self._is_empty(self.AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS):
            self.MissingRequiredField("AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS")
        if not isinstance(self.AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS, int):
            self.AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS = int(self.AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS)

        if self._is_empty(self.LAST_KNOWN_DISEASE_STATUS):
            self.MissingRequiredField("LAST_KNOWN_DISEASE_STATUS")
        if not isinstance(self.LAST_KNOWN_DISEASE_STATUS, LastKnownDiseaseStatusEnum):
            self.LAST_KNOWN_DISEASE_STATUS = LastKnownDiseaseStatusEnum(self.LAST_KNOWN_DISEASE_STATUS)

        if self._is_empty(self.TUMOR_CLASSIFICATION_CATEGORY):
            self.MissingRequiredField("TUMOR_CLASSIFICATION_CATEGORY")
        if not isinstance(self.TUMOR_CLASSIFICATION_CATEGORY, TumorClassificationCategoryEnum):
            self.TUMOR_CLASSIFICATION_CATEGORY = TumorClassificationCategoryEnum(self.TUMOR_CLASSIFICATION_CATEGORY)

        if self._is_empty(self.METASTASIS_AT_DIAGNOSIS):
            self.MissingRequiredField("METASTASIS_AT_DIAGNOSIS")
        if not isinstance(self.METASTASIS_AT_DIAGNOSIS, MetastasisAtDiagnosisEnum):
            self.METASTASIS_AT_DIAGNOSIS = MetastasisAtDiagnosisEnum(self.METASTASIS_AT_DIAGNOSIS)

        if self._is_empty(self.METHOD_OF_DIAGNOSIS):
            self.MissingRequiredField("METHOD_OF_DIAGNOSIS")
        if not isinstance(self.METHOD_OF_DIAGNOSIS, MethodOfDiagnosisEnum):
            self.METHOD_OF_DIAGNOSIS = MethodOfDiagnosisEnum(self.METHOD_OF_DIAGNOSIS)

        if self.CLINICAL_T_STAGE is not None and not isinstance(self.CLINICAL_T_STAGE, str):
            self.CLINICAL_T_STAGE = str(self.CLINICAL_T_STAGE)

        if self.CLINICAL_N_STAGE is not None and not isinstance(self.CLINICAL_N_STAGE, str):
            self.CLINICAL_N_STAGE = str(self.CLINICAL_N_STAGE)

        if self.CLINICAL_M_STAGE is not None and not isinstance(self.CLINICAL_M_STAGE, str):
            self.CLINICAL_M_STAGE = str(self.CLINICAL_M_STAGE)

        if self.AJCC_STAGING_SYSTEM_EDITION is not None and not isinstance(self.AJCC_STAGING_SYSTEM_EDITION, str):
            self.AJCC_STAGING_SYSTEM_EDITION = str(self.AJCC_STAGING_SYSTEM_EDITION)

        if self.METASTASIS_AT_DIAGNOSIS is not None and not isinstance(self.METASTASIS_AT_DIAGNOSIS, str):
            self.METASTASIS_AT_DIAGNOSIS = str(self.METASTASIS_AT_DIAGNOSIS)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Exposure(YAMLRoot):
    """
    Information about the exposure
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/exposure/Exposure"]
    class_class_curie: ClassVar[str] = "htan:clinical/exposure/Exposure"
    class_name: ClassVar[str] = "Exposure"
    class_model_uri: ClassVar[URIRef] = HTAN.Exposure

    SMOKING_HISTORY: Union[str, "SmokingHistoryEnum"] = None
    ALCOHOL_HISTORY_INDICATOR: Union[str, "AlcoholHistoryIndicatorEnum"] = None
    ENVIRONMENTAL_EXPOSURE: Union[str, "EnvironmentalExposureEnum"] = None
    YEARS_SMOKED: Optional[int] = None
    PACK_YEARS_SMOKED: Optional[Decimal] = None
    ENVIRONMENTAL_EXPOSURE_TYPE: Optional[Union[str, "EnvironmentalExposureTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.SMOKING_HISTORY):
            self.MissingRequiredField("SMOKING_HISTORY")
        if not isinstance(self.SMOKING_HISTORY, SmokingHistoryEnum):
            self.SMOKING_HISTORY = SmokingHistoryEnum(self.SMOKING_HISTORY)

        if self._is_empty(self.ALCOHOL_HISTORY_INDICATOR):
            self.MissingRequiredField("ALCOHOL_HISTORY_INDICATOR")
        if not isinstance(self.ALCOHOL_HISTORY_INDICATOR, AlcoholHistoryIndicatorEnum):
            self.ALCOHOL_HISTORY_INDICATOR = AlcoholHistoryIndicatorEnum(self.ALCOHOL_HISTORY_INDICATOR)

        if self._is_empty(self.ENVIRONMENTAL_EXPOSURE):
            self.MissingRequiredField("ENVIRONMENTAL_EXPOSURE")
        if not isinstance(self.ENVIRONMENTAL_EXPOSURE, EnvironmentalExposureEnum):
            self.ENVIRONMENTAL_EXPOSURE = EnvironmentalExposureEnum(self.ENVIRONMENTAL_EXPOSURE)

        if self.YEARS_SMOKED is not None and not isinstance(self.YEARS_SMOKED, int):
            self.YEARS_SMOKED = int(self.YEARS_SMOKED)

        if self.PACK_YEARS_SMOKED is not None and not isinstance(self.PACK_YEARS_SMOKED, Decimal):
            self.PACK_YEARS_SMOKED = Decimal(self.PACK_YEARS_SMOKED)

        if self.ENVIRONMENTAL_EXPOSURE_TYPE is not None and not isinstance(self.ENVIRONMENTAL_EXPOSURE_TYPE, EnvironmentalExposureTypeEnum):
            self.ENVIRONMENTAL_EXPOSURE_TYPE = EnvironmentalExposureTypeEnum(self.ENVIRONMENTAL_EXPOSURE_TYPE)

        if self.YEARS_SMOKED is not None and not isinstance(self.YEARS_SMOKED, str):
            self.YEARS_SMOKED = str(self.YEARS_SMOKED)

        if self.PACK_YEARS_SMOKED is not None and not isinstance(self.PACK_YEARS_SMOKED, str):
            self.PACK_YEARS_SMOKED = str(self.PACK_YEARS_SMOKED)

        if self.ENVIRONMENTAL_EXPOSURE_TYPE is not None and not isinstance(self.ENVIRONMENTAL_EXPOSURE_TYPE, str):
            self.ENVIRONMENTAL_EXPOSURE_TYPE = str(self.ENVIRONMENTAL_EXPOSURE_TYPE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyHistory(YAMLRoot):
    """
    A class to capture information about the cancer history of family members.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/family_history/FamilyHistory"]
    class_class_curie: ClassVar[str] = "htan:clinical/family_history/FamilyHistory"
    class_name: ClassVar[str] = "FamilyHistory"
    class_model_uri: ClassVar[URIRef] = HTAN.FamilyHistory

    FAMILY_MEMBER_CANCER_HISTORY: Optional[Union[str, "YesNoUnknownNotReportedEnum"]] = None
    RELATIVES_WITH_CANCER_HISTORY: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.FAMILY_MEMBER_CANCER_HISTORY is not None and not isinstance(self.FAMILY_MEMBER_CANCER_HISTORY, YesNoUnknownNotReportedEnum):
            self.FAMILY_MEMBER_CANCER_HISTORY = YesNoUnknownNotReportedEnum(self.FAMILY_MEMBER_CANCER_HISTORY)

        if self.RELATIVES_WITH_CANCER_HISTORY is not None and not isinstance(self.RELATIVES_WITH_CANCER_HISTORY, int):
            self.RELATIVES_WITH_CANCER_HISTORY = int(self.RELATIVES_WITH_CANCER_HISTORY)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FollowUp(YAMLRoot):
    """
    Clinical follow-up information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/followup/FollowUp"]
    class_class_curie: ClassVar[str] = "htan:clinical/followup/FollowUp"
    class_name: ClassVar[str] = "FollowUp"
    class_model_uri: ClassVar[URIRef] = HTAN.FollowUp

    AGE_IN_DAYS_AT_FOLLOWUP: int = None
    PROGRESSION_OR_RECURRENCE: Union[str, "ProgressionOrRecurrenceEnum"] = None
    DISEASE_RESPONSE: Union[str, "DiseaseResponseEnum"] = None
    ECOG_PERFORMANCE_STATUS: Union[str, "ECOGPerformanceStatusEnum"] = None
    PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE: Optional[str] = None
    PROGRESSION_OR_RECURRENCE_TYPE: Optional[Union[str, "ProgressionTypeEnum"]] = None
    EVIDENCE_OF_RECURRENCE_TYPE: Optional[Union[str, "EvidenceOfRecurrenceTypeEnum"]] = None
    AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE: Optional[int] = None
    MENOPAUSE_STATUS: Optional[Union[str, "MenopauseStatusEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.AGE_IN_DAYS_AT_FOLLOWUP):
            self.MissingRequiredField("AGE_IN_DAYS_AT_FOLLOWUP")
        if not isinstance(self.AGE_IN_DAYS_AT_FOLLOWUP, int):
            self.AGE_IN_DAYS_AT_FOLLOWUP = int(self.AGE_IN_DAYS_AT_FOLLOWUP)

        if self._is_empty(self.PROGRESSION_OR_RECURRENCE):
            self.MissingRequiredField("PROGRESSION_OR_RECURRENCE")
        if not isinstance(self.PROGRESSION_OR_RECURRENCE, ProgressionOrRecurrenceEnum):
            self.PROGRESSION_OR_RECURRENCE = ProgressionOrRecurrenceEnum(self.PROGRESSION_OR_RECURRENCE)

        if self._is_empty(self.DISEASE_RESPONSE):
            self.MissingRequiredField("DISEASE_RESPONSE")
        if not isinstance(self.DISEASE_RESPONSE, DiseaseResponseEnum):
            self.DISEASE_RESPONSE = DiseaseResponseEnum(self.DISEASE_RESPONSE)

        if self._is_empty(self.ECOG_PERFORMANCE_STATUS):
            self.MissingRequiredField("ECOG_PERFORMANCE_STATUS")
        if not isinstance(self.ECOG_PERFORMANCE_STATUS, ECOGPerformanceStatusEnum):
            self.ECOG_PERFORMANCE_STATUS = ECOGPerformanceStatusEnum(self.ECOG_PERFORMANCE_STATUS)

        if self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE is not None and not isinstance(self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, str):
            self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE = str(self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE)

        if self.PROGRESSION_OR_RECURRENCE_TYPE is not None and not isinstance(self.PROGRESSION_OR_RECURRENCE_TYPE, ProgressionTypeEnum):
            self.PROGRESSION_OR_RECURRENCE_TYPE = ProgressionTypeEnum(self.PROGRESSION_OR_RECURRENCE_TYPE)

        if self.EVIDENCE_OF_RECURRENCE_TYPE is not None and not isinstance(self.EVIDENCE_OF_RECURRENCE_TYPE, EvidenceOfRecurrenceTypeEnum):
            self.EVIDENCE_OF_RECURRENCE_TYPE = EvidenceOfRecurrenceTypeEnum(self.EVIDENCE_OF_RECURRENCE_TYPE)

        if self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE is not None and not isinstance(self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, int):
            self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE = int(self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE)

        if self.MENOPAUSE_STATUS is not None and not isinstance(self.MENOPAUSE_STATUS, MenopauseStatusEnum):
            self.MENOPAUSE_STATUS = MenopauseStatusEnum(self.MENOPAUSE_STATUS)

        if self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE is not None and not isinstance(self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, str):
            self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE = str(self.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE)

        if self.PROGRESSION_OR_RECURRENCE_TYPE is not None and not isinstance(self.PROGRESSION_OR_RECURRENCE_TYPE, str):
            self.PROGRESSION_OR_RECURRENCE_TYPE = str(self.PROGRESSION_OR_RECURRENCE_TYPE)

        if self.EVIDENCE_OF_RECURRENCE_TYPE is not None and not isinstance(self.EVIDENCE_OF_RECURRENCE_TYPE, str):
            self.EVIDENCE_OF_RECURRENCE_TYPE = str(self.EVIDENCE_OF_RECURRENCE_TYPE)

        if self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE is not None and not isinstance(self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, str):
            self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE = str(self.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularTest(YAMLRoot):
    """
    Information about the molecular test
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/molecular/MolecularTest"]
    class_class_curie: ClassVar[str] = "htan:clinical/molecular/MolecularTest"
    class_name: ClassVar[str] = "MolecularTest"
    class_model_uri: ClassVar[URIRef] = HTAN.MolecularTest

    TIMEPOINT_LABEL: str = None
    AGE_IN_DAYS_AT_MOLECULAR_TEST_START: int = None
    AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP: int = None
    GENE_SYMBOL: str = None
    MOLECULAR_ANALYSIS_METHOD: Union[str, "MolecularAnalysisMethodEnum"] = None
    MOLECULAR_ANALYSIS_RESULT: str = None
    AA_CHANGE: str = None
    CLINICAL_BIOSPECIMEN_TYPE: Union[str, "ClinicalBiospecimenTypeEnum"] = None
    COPY_NUMBER: int = None
    EXON: int = None
    MOLECULAR_CONSEQUENCE: Union[str, "MolecularConsequenceEnum"] = None
    PATHOGENICITY: Union[str, "PathogenicityEnum"] = None
    TEST_ANALYTE_TYPE: Union[str, "TestAnalyteTypeEnum"] = None
    TEST_UNITS: str = None
    TEST_RESULT: str = None
    VARIANT_ORIGIN: Union[str, "VariantOriginEnum"] = None
    VARIANT_TYPE: Union[str, "VariantTypeEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.TIMEPOINT_LABEL):
            self.MissingRequiredField("TIMEPOINT_LABEL")
        if not isinstance(self.TIMEPOINT_LABEL, str):
            self.TIMEPOINT_LABEL = str(self.TIMEPOINT_LABEL)

        if self._is_empty(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_START):
            self.MissingRequiredField("AGE_IN_DAYS_AT_MOLECULAR_TEST_START")
        if not isinstance(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_START, int):
            self.AGE_IN_DAYS_AT_MOLECULAR_TEST_START = int(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_START)

        if self._is_empty(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP):
            self.MissingRequiredField("AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP")
        if not isinstance(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, int):
            self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP = int(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP)

        if self._is_empty(self.GENE_SYMBOL):
            self.MissingRequiredField("GENE_SYMBOL")
        if not isinstance(self.GENE_SYMBOL, str):
            self.GENE_SYMBOL = str(self.GENE_SYMBOL)

        if self._is_empty(self.MOLECULAR_ANALYSIS_METHOD):
            self.MissingRequiredField("MOLECULAR_ANALYSIS_METHOD")
        if not isinstance(self.MOLECULAR_ANALYSIS_METHOD, MolecularAnalysisMethodEnum):
            self.MOLECULAR_ANALYSIS_METHOD = MolecularAnalysisMethodEnum(self.MOLECULAR_ANALYSIS_METHOD)

        if self._is_empty(self.MOLECULAR_ANALYSIS_RESULT):
            self.MissingRequiredField("MOLECULAR_ANALYSIS_RESULT")
        if not isinstance(self.MOLECULAR_ANALYSIS_RESULT, str):
            self.MOLECULAR_ANALYSIS_RESULT = str(self.MOLECULAR_ANALYSIS_RESULT)

        if self._is_empty(self.AA_CHANGE):
            self.MissingRequiredField("AA_CHANGE")
        if not isinstance(self.AA_CHANGE, str):
            self.AA_CHANGE = str(self.AA_CHANGE)

        if self._is_empty(self.CLINICAL_BIOSPECIMEN_TYPE):
            self.MissingRequiredField("CLINICAL_BIOSPECIMEN_TYPE")
        if not isinstance(self.CLINICAL_BIOSPECIMEN_TYPE, ClinicalBiospecimenTypeEnum):
            self.CLINICAL_BIOSPECIMEN_TYPE = ClinicalBiospecimenTypeEnum(self.CLINICAL_BIOSPECIMEN_TYPE)

        if self._is_empty(self.COPY_NUMBER):
            self.MissingRequiredField("COPY_NUMBER")
        if not isinstance(self.COPY_NUMBER, int):
            self.COPY_NUMBER = int(self.COPY_NUMBER)

        if self._is_empty(self.EXON):
            self.MissingRequiredField("EXON")
        if not isinstance(self.EXON, int):
            self.EXON = int(self.EXON)

        if self._is_empty(self.MOLECULAR_CONSEQUENCE):
            self.MissingRequiredField("MOLECULAR_CONSEQUENCE")
        if not isinstance(self.MOLECULAR_CONSEQUENCE, MolecularConsequenceEnum):
            self.MOLECULAR_CONSEQUENCE = MolecularConsequenceEnum(self.MOLECULAR_CONSEQUENCE)

        if self._is_empty(self.PATHOGENICITY):
            self.MissingRequiredField("PATHOGENICITY")
        if not isinstance(self.PATHOGENICITY, PathogenicityEnum):
            self.PATHOGENICITY = PathogenicityEnum(self.PATHOGENICITY)

        if self._is_empty(self.TEST_ANALYTE_TYPE):
            self.MissingRequiredField("TEST_ANALYTE_TYPE")
        if not isinstance(self.TEST_ANALYTE_TYPE, TestAnalyteTypeEnum):
            self.TEST_ANALYTE_TYPE = TestAnalyteTypeEnum(self.TEST_ANALYTE_TYPE)

        if self._is_empty(self.TEST_UNITS):
            self.MissingRequiredField("TEST_UNITS")
        if not isinstance(self.TEST_UNITS, str):
            self.TEST_UNITS = str(self.TEST_UNITS)

        if self._is_empty(self.TEST_RESULT):
            self.MissingRequiredField("TEST_RESULT")
        if not isinstance(self.TEST_RESULT, str):
            self.TEST_RESULT = str(self.TEST_RESULT)

        if self._is_empty(self.VARIANT_ORIGIN):
            self.MissingRequiredField("VARIANT_ORIGIN")
        if not isinstance(self.VARIANT_ORIGIN, VariantOriginEnum):
            self.VARIANT_ORIGIN = VariantOriginEnum(self.VARIANT_ORIGIN)

        if self._is_empty(self.VARIANT_TYPE):
            self.MissingRequiredField("VARIANT_TYPE")
        if not isinstance(self.VARIANT_TYPE, VariantTypeEnum):
            self.VARIANT_TYPE = VariantTypeEnum(self.VARIANT_TYPE)

        if self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP is not None and not isinstance(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, str):
            self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP = str(self.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP)

        if self.AA_CHANGE is not None and not isinstance(self.AA_CHANGE, str):
            self.AA_CHANGE = str(self.AA_CHANGE)

        if self.COPY_NUMBER is not None and not isinstance(self.COPY_NUMBER, str):
            self.COPY_NUMBER = str(self.COPY_NUMBER)

        if self.EXON is not None and not isinstance(self.EXON, str):
            self.EXON = str(self.EXON)

        if self.MOLECULAR_CONSEQUENCE is not None and not isinstance(self.MOLECULAR_CONSEQUENCE, str):
            self.MOLECULAR_CONSEQUENCE = str(self.MOLECULAR_CONSEQUENCE)

        if self.PATHOGENICITY is not None and not isinstance(self.PATHOGENICITY, str):
            self.PATHOGENICITY = str(self.PATHOGENICITY)

        if self.TEST_ANALYTE_TYPE is not None and not isinstance(self.TEST_ANALYTE_TYPE, str):
            self.TEST_ANALYTE_TYPE = str(self.TEST_ANALYTE_TYPE)

        if self.TEST_UNITS is not None and not isinstance(self.TEST_UNITS, str):
            self.TEST_UNITS = str(self.TEST_UNITS)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Therapy(YAMLRoot):
    """
    Information about therapeutic interventions
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/therapy/Therapy"]
    class_class_curie: ClassVar[str] = "htan:clinical/therapy/Therapy"
    class_name: ClassVar[str] = "Therapy"
    class_model_uri: ClassVar[URIRef] = HTAN.Therapy

    INITIAL_DISEASE_STATUS: str = None
    TREATMENT_INTENT_TYPE: Union[str, "TreatmentIntentTypeEnum"] = None
    TREATMENT_TYPE: Union[Union[str, "TreatmentTypeEnum"], List[Union[str, "TreatmentTypeEnum"]]] = None
    PHARMACOTHERAPY_TYPE: Union[str, "PharmacotherapyTypeEnum"] = None
    THERAPEUTIC_AGENTS: Union[str, List[str]] = None
    AGE_IN_DAYS_AT_TREATMENT_START: int = None
    AGE_IN_DAYS_AT_TREATMENT_END: int = None
    THERAPY_ANATOMIC_SITE_UBERON_CODE: Optional[str] = None
    OFF_TREATMENT_REASON: Optional[Union[str, "OffTreatmentReasonEnum"]] = None
    REGIMEN_OR_LINE_OF_THERAPY: Optional[Union[str, "RegimenOrLineOfTherapyEnum"]] = None
    NUMBER_OF_CYCLES: Optional[int] = None
    RESPONSE: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.INITIAL_DISEASE_STATUS):
            self.MissingRequiredField("INITIAL_DISEASE_STATUS")
        if not isinstance(self.INITIAL_DISEASE_STATUS, str):
            self.INITIAL_DISEASE_STATUS = str(self.INITIAL_DISEASE_STATUS)

        if self._is_empty(self.TREATMENT_INTENT_TYPE):
            self.MissingRequiredField("TREATMENT_INTENT_TYPE")
        if not isinstance(self.TREATMENT_INTENT_TYPE, TreatmentIntentTypeEnum):
            self.TREATMENT_INTENT_TYPE = TreatmentIntentTypeEnum(self.TREATMENT_INTENT_TYPE)

        if self._is_empty(self.TREATMENT_TYPE):
            self.MissingRequiredField("TREATMENT_TYPE")
        if not isinstance(self.TREATMENT_TYPE, list):
            self.TREATMENT_TYPE = [self.TREATMENT_TYPE] if self.TREATMENT_TYPE is not None else []
        self.TREATMENT_TYPE = [v if isinstance(v, TreatmentTypeEnum) else TreatmentTypeEnum(v) for v in self.TREATMENT_TYPE]

        if self._is_empty(self.PHARMACOTHERAPY_TYPE):
            self.MissingRequiredField("PHARMACOTHERAPY_TYPE")
        if not isinstance(self.PHARMACOTHERAPY_TYPE, PharmacotherapyTypeEnum):
            self.PHARMACOTHERAPY_TYPE = PharmacotherapyTypeEnum(self.PHARMACOTHERAPY_TYPE)

        if self._is_empty(self.THERAPEUTIC_AGENTS):
            self.MissingRequiredField("THERAPEUTIC_AGENTS")
        if not isinstance(self.THERAPEUTIC_AGENTS, list):
            self.THERAPEUTIC_AGENTS = [self.THERAPEUTIC_AGENTS] if self.THERAPEUTIC_AGENTS is not None else []
        self.THERAPEUTIC_AGENTS = [v if isinstance(v, str) else str(v) for v in self.THERAPEUTIC_AGENTS]

        if self._is_empty(self.AGE_IN_DAYS_AT_TREATMENT_START):
            self.MissingRequiredField("AGE_IN_DAYS_AT_TREATMENT_START")
        if not isinstance(self.AGE_IN_DAYS_AT_TREATMENT_START, int):
            self.AGE_IN_DAYS_AT_TREATMENT_START = int(self.AGE_IN_DAYS_AT_TREATMENT_START)

        if self._is_empty(self.AGE_IN_DAYS_AT_TREATMENT_END):
            self.MissingRequiredField("AGE_IN_DAYS_AT_TREATMENT_END")
        if not isinstance(self.AGE_IN_DAYS_AT_TREATMENT_END, int):
            self.AGE_IN_DAYS_AT_TREATMENT_END = int(self.AGE_IN_DAYS_AT_TREATMENT_END)

        if self.THERAPY_ANATOMIC_SITE_UBERON_CODE is not None and not isinstance(self.THERAPY_ANATOMIC_SITE_UBERON_CODE, str):
            self.THERAPY_ANATOMIC_SITE_UBERON_CODE = str(self.THERAPY_ANATOMIC_SITE_UBERON_CODE)

        if self.OFF_TREATMENT_REASON is not None and not isinstance(self.OFF_TREATMENT_REASON, OffTreatmentReasonEnum):
            self.OFF_TREATMENT_REASON = OffTreatmentReasonEnum(self.OFF_TREATMENT_REASON)

        if self.REGIMEN_OR_LINE_OF_THERAPY is not None and not isinstance(self.REGIMEN_OR_LINE_OF_THERAPY, RegimenOrLineOfTherapyEnum):
            self.REGIMEN_OR_LINE_OF_THERAPY = RegimenOrLineOfTherapyEnum(self.REGIMEN_OR_LINE_OF_THERAPY)

        if self.NUMBER_OF_CYCLES is not None and not isinstance(self.NUMBER_OF_CYCLES, int):
            self.NUMBER_OF_CYCLES = int(self.NUMBER_OF_CYCLES)

        if self.RESPONSE is not None and not isinstance(self.RESPONSE, str):
            self.RESPONSE = str(self.RESPONSE)

        if self.THERAPY_ANATOMIC_SITE_UBERON_CODE is not None and not isinstance(self.THERAPY_ANATOMIC_SITE_UBERON_CODE, str):
            self.THERAPY_ANATOMIC_SITE_UBERON_CODE = str(self.THERAPY_ANATOMIC_SITE_UBERON_CODE)

        if self.OFF_TREATMENT_REASON is not None and not isinstance(self.OFF_TREATMENT_REASON, str):
            self.OFF_TREATMENT_REASON = str(self.OFF_TREATMENT_REASON)

        if self.REGIMEN_OR_LINE_OF_THERAPY is not None and not isinstance(self.REGIMEN_OR_LINE_OF_THERAPY, str):
            self.REGIMEN_OR_LINE_OF_THERAPY = str(self.REGIMEN_OR_LINE_OF_THERAPY)

        if self.NUMBER_OF_CYCLES is not None and not isinstance(self.NUMBER_OF_CYCLES, str):
            self.NUMBER_OF_CYCLES = str(self.NUMBER_OF_CYCLES)

        if self.RESPONSE is not None and not isinstance(self.RESPONSE, str):
            self.RESPONSE = str(self.RESPONSE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class VitalStatus(YAMLRoot):
    """
    Information about the vital status
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["clinical/vital_status/VitalStatus"]
    class_class_curie: ClassVar[str] = "htan:clinical/vital_status/VitalStatus"
    class_name: ClassVar[str] = "VitalStatus"
    class_model_uri: ClassVar[URIRef] = HTAN.VitalStatus

    VITAL_STATUS: Union[str, "VitalStatusEnum"] = None
    AGE_IN_DAYS_AT_DEATH: Optional[int] = None
    CAUSE_OF_DEATH: Optional[Union[str, "CauseOfDeathEnum"]] = None
    CAUSE_OF_DEATH_SOURCE: Optional[Union[str, "CauseOfDeathSourceEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.VITAL_STATUS):
            self.MissingRequiredField("VITAL_STATUS")
        if not isinstance(self.VITAL_STATUS, VitalStatusEnum):
            self.VITAL_STATUS = VitalStatusEnum(self.VITAL_STATUS)

        if self.AGE_IN_DAYS_AT_DEATH is not None and not isinstance(self.AGE_IN_DAYS_AT_DEATH, int):
            self.AGE_IN_DAYS_AT_DEATH = int(self.AGE_IN_DAYS_AT_DEATH)

        if self.CAUSE_OF_DEATH is not None and not isinstance(self.CAUSE_OF_DEATH, CauseOfDeathEnum):
            self.CAUSE_OF_DEATH = CauseOfDeathEnum(self.CAUSE_OF_DEATH)

        if self.CAUSE_OF_DEATH_SOURCE is not None and not isinstance(self.CAUSE_OF_DEATH_SOURCE, CauseOfDeathSourceEnum):
            self.CAUSE_OF_DEATH_SOURCE = CauseOfDeathSourceEnum(self.CAUSE_OF_DEATH_SOURCE)

        if self.AGE_IN_DAYS_AT_DEATH is not None and not isinstance(self.AGE_IN_DAYS_AT_DEATH, str):
            self.AGE_IN_DAYS_AT_DEATH = str(self.AGE_IN_DAYS_AT_DEATH)

        if self.CAUSE_OF_DEATH is not None and not isinstance(self.CAUSE_OF_DEATH, str):
            self.CAUSE_OF_DEATH = str(self.CAUSE_OF_DEATH)

        if self.CAUSE_OF_DEATH_SOURCE is not None and not isinstance(self.CAUSE_OF_DEATH_SOURCE, str):
            self.CAUSE_OF_DEATH_SOURCE = str(self.CAUSE_OF_DEATH_SOURCE)

        super().__post_init__(**kwargs)


# Enumerations
class ComponentEnum(EnumDefinitionImpl):

    Clinical = PermissibleValue(
        text="Clinical",
        description="Clinical data component")
    Demographics = PermissibleValue(
        text="Demographics",
        description="Demographics data component")
    Diagnosis = PermissibleValue(
        text="Diagnosis",
        description="Diagnosis data component")
    Exposure = PermissibleValue(
        text="Exposure",
        description="Exposure data component")
    Molecular = PermissibleValue(
        text="Molecular",
        description="Molecular data component")
    Therapy = PermissibleValue(
        text="Therapy",
        description="Therapy data component")

    _defn = EnumDefinition(
        name="ComponentEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Family History",
            PermissibleValue(
                text="Family History",
                description="Family history data component"))
        setattr(cls, "Follow-up",
            PermissibleValue(
                text="Follow-up",
                description="Follow-up data component"))
        setattr(cls, "Vital Status",
            PermissibleValue(
                text="Vital Status",
                description="Vital status data component"))

class EthnicGroupEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="EthnicGroupEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hispanic or Latino",
            PermissibleValue(
                text="Hispanic or Latino",
                description="Hispanic or Latino"))
        setattr(cls, "Not Hispanic or Latino",
            PermissibleValue(
                text="Not Hispanic or Latino",
                description="Not Hispanic or Latino"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class GenderIdentityEnum(EnumDefinitionImpl):

    Female = PermissibleValue(
        text="Female",
        description="Female")
    Male = PermissibleValue(
        text="Male",
        description="Male")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="GenderIdentityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class SexEnum(EnumDefinitionImpl):

    Female = PermissibleValue(
        text="Female",
        description="Female")
    Male = PermissibleValue(
        text="Male",
        description="Male")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="SexEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class RaceEnum(EnumDefinitionImpl):

    Asian = PermissibleValue(
        text="Asian",
        description="Asian")
    White = PermissibleValue(
        text="White",
        description="White")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="RaceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "American Indian or Alaska Native",
            PermissibleValue(
                text="American Indian or Alaska Native",
                description="American Indian or Alaska Native"))
        setattr(cls, "Black or African American",
            PermissibleValue(
                text="Black or African American",
                description="Black or African American"))
        setattr(cls, "Native Hawaiian or Other Pacific Islander",
            PermissibleValue(
                text="Native Hawaiian or Other Pacific Islander",
                description="Native Hawaiian or Other Pacific Islander"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class TumorGradeEnum(EnumDefinitionImpl):

    G1 = PermissibleValue(
        text="G1",
        description="Well differentiated")
    G2 = PermissibleValue(
        text="G2",
        description="Moderately differentiated")
    G3 = PermissibleValue(
        text="G3",
        description="Poorly differentiated")
    G4 = PermissibleValue(
        text="G4",
        description="Undifferentiated")
    GX = PermissibleValue(
        text="GX",
        description="Grade cannot be assessed")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="TumorGradeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class TumorStageEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="TumorStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Stage I",
            PermissibleValue(
                text="Stage I",
                description="Stage I"))
        setattr(cls, "Stage IA",
            PermissibleValue(
                text="Stage IA",
                description="Stage IA"))
        setattr(cls, "Stage IB",
            PermissibleValue(
                text="Stage IB",
                description="Stage IB"))
        setattr(cls, "Stage II",
            PermissibleValue(
                text="Stage II",
                description="Stage II"))
        setattr(cls, "Stage IIA",
            PermissibleValue(
                text="Stage IIA",
                description="Stage IIA"))
        setattr(cls, "Stage IIB",
            PermissibleValue(
                text="Stage IIB",
                description="Stage IIB"))
        setattr(cls, "Stage III",
            PermissibleValue(
                text="Stage III",
                description="Stage III"))
        setattr(cls, "Stage IIIA",
            PermissibleValue(
                text="Stage IIIA",
                description="Stage IIIA"))
        setattr(cls, "Stage IIIB",
            PermissibleValue(
                text="Stage IIIB",
                description="Stage IIIB"))
        setattr(cls, "Stage IIIC",
            PermissibleValue(
                text="Stage IIIC",
                description="Stage IIIC"))
        setattr(cls, "Stage IV",
            PermissibleValue(
                text="Stage IV",
                description="Stage IV"))
        setattr(cls, "Stage IVA",
            PermissibleValue(
                text="Stage IVA",
                description="Stage IVA"))
        setattr(cls, "Stage IVB",
            PermissibleValue(
                text="Stage IVB",
                description="Stage IVB"))
        setattr(cls, "Stage IVC",
            PermissibleValue(
                text="Stage IVC",
                description="Stage IVC"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class ClinicalTStageEnum(EnumDefinitionImpl):

    T0 = PermissibleValue(
        text="T0",
        description="No evidence of primary tumor")
    T1 = PermissibleValue(
        text="T1",
        description="Tumor ≤ 2 cm in greatest dimension")
    T2 = PermissibleValue(
        text="T2",
        description="Tumor > 2 cm but ≤ 4 cm in greatest dimension")
    T3 = PermissibleValue(
        text="T3",
        description="Tumor > 4 cm in greatest dimension")
    T4 = PermissibleValue(
        text="T4",
        description="Tumor of any size with direct extension to adjacent structures")
    TX = PermissibleValue(
        text="TX",
        description="Primary tumor cannot be assessed")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="ClinicalTStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class ClinicalNStageEnum(EnumDefinitionImpl):

    N0 = PermissibleValue(
        text="N0",
        description="No regional lymph node metastasis")
    N1 = PermissibleValue(
        text="N1",
        description="Metastasis in 1-3 axillary lymph nodes")
    N2 = PermissibleValue(
        text="N2",
        description="Metastasis in 4-9 axillary lymph nodes")
    N3 = PermissibleValue(
        text="N3",
        description="Metastasis in 10 or more axillary lymph nodes")
    NX = PermissibleValue(
        text="NX",
        description="Regional lymph nodes cannot be assessed")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="ClinicalNStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class ClinicalMStageEnum(EnumDefinitionImpl):

    M0 = PermissibleValue(
        text="M0",
        description="No distant metastasis")
    M1 = PermissibleValue(
        text="M1",
        description="Distant metastasis present")
    MX = PermissibleValue(
        text="MX",
        description="Distant metastasis cannot be assessed")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="ClinicalMStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class AJCCStagingSystemEditionEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="AJCCStagingSystemEditionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "7th Edition",
            PermissibleValue(
                text="7th Edition",
                description="7th Edition of AJCC Staging System"))
        setattr(cls, "8th Edition",
            PermissibleValue(
                text="8th Edition",
                description="8th Edition of AJCC Staging System"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class LastKnownDiseaseStatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="LastKnownDiseaseStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete Response",
            PermissibleValue(
                text="Complete Response",
                description="Complete disappearance of all target lesions"))
        setattr(cls, "Partial Response",
            PermissibleValue(
                text="Partial Response",
                description="At least a 30% decrease in the sum of the diameters of target lesions"))
        setattr(cls, "Progressive Disease",
            PermissibleValue(
                text="Progressive Disease",
                description="At least a 20% increase in the sum of the diameters of target lesions"))
        setattr(cls, "Stable Disease",
            PermissibleValue(
                text="Stable Disease",
                description="""Neither sufficient shrinkage to qualify for partial response nor sufficient increase to qualify for progressive disease"""))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class TumorClassificationCategoryEnum(EnumDefinitionImpl):

    Benign = PermissibleValue(
        text="Benign",
        description="Non-cancerous tumor")
    Borderline = PermissibleValue(
        text="Borderline",
        description="Tumor with uncertain malignant potential")
    Malignant = PermissibleValue(
        text="Malignant",
        description="Cancerous tumor")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="TumorClassificationCategoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class MetastasisAtDiagnosisEnum(EnumDefinitionImpl):

    No = PermissibleValue(
        text="No",
        description="No metastasis at diagnosis")
    Yes = PermissibleValue(
        text="Yes",
        description="Metastasis present at diagnosis")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="MetastasisAtDiagnosisEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class MethodOfDiagnosisEnum(EnumDefinitionImpl):

    Biopsy = PermissibleValue(
        text="Biopsy",
        description="Diagnosis made by biopsy")
    Clinical = PermissibleValue(
        text="Clinical",
        description="Diagnosis made by clinical examination")
    Cytology = PermissibleValue(
        text="Cytology",
        description="Diagnosis made by cytology")
    Imaging = PermissibleValue(
        text="Imaging",
        description="Diagnosis made by imaging")
    Laboratory = PermissibleValue(
        text="Laboratory",
        description="Diagnosis made by laboratory test")
    Pathology = PermissibleValue(
        text="Pathology",
        description="Diagnosis made by pathology")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="MethodOfDiagnosisEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class SmokingHistoryEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="SmokingHistoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Current smoker",
            PermissibleValue(
                text="Current smoker",
                description="Current smoker"))
        setattr(cls, "Former smoker",
            PermissibleValue(
                text="Former smoker",
                description="Former smoker"))
        setattr(cls, "Never smoker",
            PermissibleValue(
                text="Never smoker",
                description="Never smoker"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class AlcoholHistoryIndicatorEnum(EnumDefinitionImpl):

    No = PermissibleValue(
        text="No",
        description="No alcohol history")
    Yes = PermissibleValue(
        text="Yes",
        description="Alcohol history present")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="AlcoholHistoryIndicatorEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class EnvironmentalExposureEnum(EnumDefinitionImpl):

    No = PermissibleValue(
        text="No",
        description="No environmental exposure")
    Yes = PermissibleValue(
        text="Yes",
        description="Environmental exposure present")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="EnvironmentalExposureEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class EnvironmentalExposureTypeEnum(EnumDefinitionImpl):

    Asbestos = PermissibleValue(
        text="Asbestos",
        description="Asbestos exposure")
    Radiation = PermissibleValue(
        text="Radiation",
        description="Radiation exposure")
    Chemical = PermissibleValue(
        text="Chemical",
        description="Chemical exposure")
    Other = PermissibleValue(
        text="Other",
        description="Other type of exposure")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="EnvironmentalExposureTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class YesNoUnknownNotReportedEnum(EnumDefinitionImpl):

    No = PermissibleValue(
        text="No",
        description="False")
    Yes = PermissibleValue(
        text="Yes",
        description="True")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="YesNoUnknownNotReportedEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class FamilyMemberCancerHistoryEnum(EnumDefinitionImpl):

    No = PermissibleValue(
        text="No",
        description="No family member with cancer history")
    Yes = PermissibleValue(
        text="Yes",
        description="Family member with cancer history")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="FamilyMemberCancerHistoryEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class ProgressionOrRecurrenceEnum(EnumDefinitionImpl):

    Censored = PermissibleValue(
        text="Censored",
        description="Points of data for which only partial information is known.")
    No = PermissibleValue(
        text="No",
        description="The non-affirmative response to a question.")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, observed, recorded; or reported as unknown by the data contributor.")
    Yes = PermissibleValue(
        text="Yes",
        description="The affirmative response to a question.")

    _defn = EnumDefinition(
        name="ProgressionOrRecurrenceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Allowed to Collect",
            PermissibleValue(
                text="Not Allowed to Collect",
                description="An indicator that specifies that a collection event was not permitted."))
        setattr(cls, "Not Applicable",
            PermissibleValue(
                text="Not Applicable",
                description="Determination of a value is not relevant in the current context."))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available."))

class ProgressionTypeEnum(EnumDefinitionImpl):

    Biochemical = PermissibleValue(
        text="Biochemical",
        description="An indication that biochemical markers of a disease are present.")
    Distant = PermissibleValue(
        text="Distant",
        description="""A biological process that involves the transfer and growth of cancer cells from the site of the primary tumor.""")
    Local = PermissibleValue(
        text="Local",
        description="""A disease that is confined to a specific organ or tissue and has not spread to other anatomic sites.""")
    Locoregional = PermissibleValue(
        text="Locoregional",
        description="""A disease that occurs within a specific organ or tissue and extends into adjacent areas including lymph nodes.""")
    Regional = PermissibleValue(
        text="Regional",
        description="""A disease or condition that extends beyond the site and spreads into adjacent tissues and regional lymph nodes.""")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, observed, recorded; or reported as unknown by the data contributor.")

    _defn = EnumDefinition(
        name="ProgressionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available."))

class EvidenceOfRecurrenceTypeEnum(EnumDefinitionImpl):

    Clinical = PermissibleValue(
        text="Clinical",
        description="Recurrence was determined by clinical examination.")
    Imaging = PermissibleValue(
        text="Imaging",
        description="Recurrence was determined by imaging.")
    Laboratory = PermissibleValue(
        text="Laboratory",
        description="Recurrence was determined by laboratory test.")
    Pathology = PermissibleValue(
        text="Pathology",
        description="Recurrence was determined by pathology.")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused.")

    _defn = EnumDefinition(
        name="EvidenceOfRecurrenceTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available."))

class DiseaseResponseEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused.")

    _defn = EnumDefinition(
        name="DiseaseResponseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete Response",
            PermissibleValue(
                text="Complete Response",
                description="Complete disappearance of all target lesions."))
        setattr(cls, "No Evidence of Disease",
            PermissibleValue(
                text="No Evidence of Disease",
                description="Diagnostic tests fail to detect presence of disease."))
        setattr(cls, "No Response",
            PermissibleValue(
                text="No Response",
                description="No apparent change or worsening in tumor staging classification."))
        setattr(cls, "Not Applicable",
            PermissibleValue(
                text="Not Applicable",
                description="Determination of a value is not relevant in the current context."))
        setattr(cls, "Not Evaluable",
            PermissibleValue(
                text="Not Evaluable",
                description="Unable to be evaluated."))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available."))
        setattr(cls, "Partial Response",
            PermissibleValue(
                text="Partial Response",
                description="At least a 30% decrease in the sum of the diameters of target lesions."))
        setattr(cls, "Persistent Disease",
            PermissibleValue(
                text="Persistent Disease",
                description="A disease that does not go to remission despite treatment."))
        setattr(cls, "Progressive Disease",
            PermissibleValue(
                text="Progressive Disease",
                description="At least a 20% increase in the sum of the diameters of target lesions."))
        setattr(cls, "Stable Disease",
            PermissibleValue(
                text="Stable Disease",
                description="""Neither sufficient shrinkage to qualify for partial response nor sufficient increase to qualify for progressive disease."""))

class ECOGPerformanceStatusEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="ECOGPerformanceStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
            PermissibleValue(
                text="0",
                description="Fully active, able to carry on all pre-disease performance without restriction."))
        setattr(cls, "1",
            PermissibleValue(
                text="1",
                description="""Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature."""))
        setattr(cls, "2",
            PermissibleValue(
                text="2",
                description="""Ambulatory and capable of all selfcare but unable to carry out any work activities. Up and about more than 50% of waking hours."""))
        setattr(cls, "3",
            PermissibleValue(
                text="3",
                description="""Capable of only limited selfcare, confined to bed or chair more than 50% of waking hours."""))
        setattr(cls, "4",
            PermissibleValue(
                text="4",
                description="Completely disabled. Cannot carry on any selfcare. Totally confined to bed or chair."))
        setattr(cls, "5",
            PermissibleValue(
                text="5",
                description="Dead"))

class MenopauseStatusEnum(EnumDefinitionImpl):

    Menopausal = PermissibleValue(
        text="Menopausal",
        description="""The permanent cessation of menses, usually defined by 6 to 12 months of amenorrhea in a woman over 45 years of age.""")
    Not_Applicable = PermissibleValue(
        text="Not_Applicable",
        description="Determination of a value is not relevant in the current context.")
    Not_Reported = PermissibleValue(
        text="Not_Reported",
        description="Not provided or available.")
    Perimenopausal = PermissibleValue(
        text="Perimenopausal",
        description="The time of a woman's life when menstrual periods become irregular.")
    Postmenopausal = PermissibleValue(
        text="Postmenopausal",
        description="Having to do with the time after menopause.")
    Postmenopausal_Natural = PermissibleValue(
        text="Postmenopausal_Natural",
        description="""Having to do with the time after menopause (>12 months since last menstrual period with no prior ovariectomy).""")
    Postmenopausal_Surgical = PermissibleValue(
        text="Postmenopausal_Surgical",
        description="Having to do with the time after menopause (prior bilateral ovariectomy).")
    Premenopausal = PermissibleValue(
        text="Premenopausal",
        description="Refers to the time before menopause.")
    Premenopausal_Perimenopausal = PermissibleValue(
        text="Premenopausal_Perimenopausal",
        description="Prior to menopause or in the perimenopausal phase.")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused.")

    _defn = EnumDefinition(
        name="MenopauseStatusEnum",
    )

class MolecularAnalysisMethodEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="MolecularAnalysisMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DNA Sequencing",
            PermissibleValue(
                text="DNA Sequencing",
                description="DNA sequencing"))
        setattr(cls, "RNA Sequencing",
            PermissibleValue(
                text="RNA Sequencing",
                description="RNA sequencing"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class ClinicalBiospecimenTypeEnum(EnumDefinitionImpl):

    Blood = PermissibleValue(
        text="Blood",
        description="Blood")
    Tissue = PermissibleValue(
        text="Tissue",
        description="Tissue")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="ClinicalBiospecimenTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class MolecularConsequenceEnum(EnumDefinitionImpl):

    Frameshift = PermissibleValue(
        text="Frameshift",
        description="Frameshift mutation")
    Missense = PermissibleValue(
        text="Missense",
        description="Missense mutation")
    Nonsense = PermissibleValue(
        text="Nonsense",
        description="Nonsense mutation")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="MolecularConsequenceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class PathogenicityEnum(EnumDefinitionImpl):

    Benign = PermissibleValue(
        text="Benign",
        description="Benign")
    Pathogenic = PermissibleValue(
        text="Pathogenic",
        description="Pathogenic")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="PathogenicityEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Likely Benign",
            PermissibleValue(
                text="Likely Benign",
                description="Likely benign"))
        setattr(cls, "Likely Pathogenic",
            PermissibleValue(
                text="Likely Pathogenic",
                description="Likely pathogenic"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class TestAnalyteTypeEnum(EnumDefinitionImpl):

    DNA = PermissibleValue(
        text="DNA",
        description="DNA")
    RNA = PermissibleValue(
        text="RNA",
        description="RNA")
    Protein = PermissibleValue(
        text="Protein",
        description="Protein")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="TestAnalyteTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class VariantOriginEnum(EnumDefinitionImpl):

    Germline = PermissibleValue(
        text="Germline",
        description="Germline variant")
    Somatic = PermissibleValue(
        text="Somatic",
        description="Somatic variant")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="VariantOriginEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class VariantTypeEnum(EnumDefinitionImpl):

    Deletion = PermissibleValue(
        text="Deletion",
        description="Deletion")
    Insertion = PermissibleValue(
        text="Insertion",
        description="Insertion")
    Substitution = PermissibleValue(
        text="Substitution",
        description="Substitution")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="VariantTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class PharmacotherapyTypeEnum(EnumDefinitionImpl):

    Chemotherapy = PermissibleValue(
        text="Chemotherapy",
        description="Treatment with chemical substances to kill or inhibit the growth of cancer cells")
    Immunotherapy = PermissibleValue(
        text="Immunotherapy",
        description="Treatment that uses the body's immune system to fight cancer")
    Other = PermissibleValue(
        text="Other",
        description="Other type of pharmacotherapy")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown type of pharmacotherapy")

    _defn = EnumDefinition(
        name="PharmacotherapyTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Hormone Therapy",
            PermissibleValue(
                text="Hormone Therapy",
                description="""Treatment that adds, blocks, or removes hormones to slow or stop the growth of cancer cells"""))
        setattr(cls, "Targeted Therapy",
            PermissibleValue(
                text="Targeted Therapy",
                description="""Treatment that targets specific genes, proteins, or the tissue environment that contributes to cancer growth"""))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not reported"))

class OffTreatmentReasonEnum(EnumDefinitionImpl):

    Death = PermissibleValue(
        text="Death",
        description="Treatment stopped due to death")
    Other = PermissibleValue(
        text="Other",
        description="Other reason for stopping treatment")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown reason for stopping treatment")

    _defn = EnumDefinition(
        name="OffTreatmentReasonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Adverse Event",
            PermissibleValue(
                text="Adverse Event",
                description="Treatment stopped due to adverse events"))
        setattr(cls, "Completed Planned Treatment",
            PermissibleValue(
                text="Completed Planned Treatment",
                description="Treatment completed as planned"))
        setattr(cls, "Disease Progression",
            PermissibleValue(
                text="Disease Progression",
                description="Treatment stopped due to disease progression"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not reported"))
        setattr(cls, "Patient Decision",
            PermissibleValue(
                text="Patient Decision",
                description="Treatment stopped at patient's request"))
        setattr(cls, "Physician Decision",
            PermissibleValue(
                text="Physician Decision",
                description="Treatment stopped at physician's discretion"))

class RegimenOrLineOfTherapyEnum(EnumDefinitionImpl):

    Other = PermissibleValue(
        text="Other",
        description="Other line of therapy")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown line of therapy")

    _defn = EnumDefinition(
        name="RegimenOrLineOfTherapyEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "First Line",
            PermissibleValue(
                text="First Line",
                description="First line of therapy"))
        setattr(cls, "Second Line",
            PermissibleValue(
                text="Second Line",
                description="Second line of therapy"))
        setattr(cls, "Third Line",
            PermissibleValue(
                text="Third Line",
                description="Third line of therapy"))
        setattr(cls, "Fourth Line",
            PermissibleValue(
                text="Fourth Line",
                description="Fourth line of therapy"))
        setattr(cls, "Fifth Line",
            PermissibleValue(
                text="Fifth Line",
                description="Fifth line of therapy"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not reported"))

class TreatmentIntentTypeEnum(EnumDefinitionImpl):

    Adjuvant = PermissibleValue(
        text="Adjuvant",
        description="Treatment given after the primary treatment to increase the chances of a cure")
    Curative = PermissibleValue(
        text="Curative",
        description="A therapy designed to cure a condition")
    Maintenance = PermissibleValue(
        text="Maintenance",
        description="Continuation of treatment for an extended period of time to prevent relapse")
    Neoadjuvant = PermissibleValue(
        text="Neoadjuvant",
        description="""Therapy administered prior to the primary treatment for the purpose of making the primary treatment more effective""")
    Palliative = PermissibleValue(
        text="Palliative",
        description="Treatment focused on providing relief from symptoms and improving quality of life")
    Prevention = PermissibleValue(
        text="Prevention",
        description="An attempt to prevent disease")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown treatment intent")

    _defn = EnumDefinition(
        name="TreatmentIntentTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not reported"))

class TreatmentTypeEnum(EnumDefinitionImpl):

    Brachytherapy = PermissibleValue(
        text="Brachytherapy",
        description="""A type of radiation therapy in which radioactive material sealed in needles, seeds, wires, or catheters is placed directly into or near a tumor""")
    Chemotherapy = PermissibleValue(
        text="Chemotherapy",
        description="A type of cancer treatment that uses drugs to kill cancer cells")
    Immunotherapy = PermissibleValue(
        text="Immunotherapy",
        description="A type of cancer treatment that helps your immune system fight cancer")
    Pharmacotherapy = PermissibleValue(
        text="Pharmacotherapy",
        description="Treatment of disease through the use of drugs")
    Radiopharmaceutical = PermissibleValue(
        text="Radiopharmaceutical",
        description="Treatment with an agent that contains a radioactive pharmaceutical agent")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown treatment type")

    _defn = EnumDefinition(
        name="TreatmentTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3-Dimensional Conformal Radiation Therapy",
            PermissibleValue(
                text="3-Dimensional Conformal Radiation Therapy",
                description="""A process by which a dose of radiation is automatically shaped to closely conform to the entire volume of the tumor"""))
        setattr(cls, "Allogeneic Hematopoietic Stem Cell Transplantation",
            PermissibleValue(
                text="Allogeneic Hematopoietic Stem Cell Transplantation",
                description="""A clinical treatment in which HSC capable of reconstituting the immune system and blood production are transferred from one genetically dissimilar individual to another"""))
        setattr(cls, "Autologous Stem Cell Transplantation",
            PermissibleValue(
                text="Autologous Stem Cell Transplantation",
                description="The transference of stem cells within the same individual"))
        setattr(cls, "Cellular Therapy",
            PermissibleValue(
                text="Cellular Therapy",
                description="Utilization of specific cells, modified or not, for treatment of diseases"))
        setattr(cls, "Concurrent Chemoradiation",
            PermissibleValue(
                text="Concurrent Chemoradiation",
                description="Treatment in which radiation therapy is administered at the same time as chemotherapy"))
        setattr(cls, "Conventional Radiotherapy",
            PermissibleValue(
                text="Conventional Radiotherapy",
                description="""A course of radiotherapy where minimal imaging support is used to determine the positioning of radiotherapy"""))
        setattr(cls, "Electron Beam Radiation Therapy",
            PermissibleValue(
                text="Electron Beam Radiation Therapy",
                description="Radiation therapy using electron beam"))
        setattr(cls, "External Beam Radiation Therapy",
            PermissibleValue(
                text="External Beam Radiation Therapy",
                description="""A type of radiation therapy that uses a machine to aim high-energy rays at the cancer from outside of the body"""))
        setattr(cls, "High-Dose Rate Brachytherapy",
            PermissibleValue(
                text="High-Dose Rate Brachytherapy",
                description="""Internal radiation treatment that targets a cancerous tissue with accurate, high doses of radiation through the use of inserted temporary implants"""))
        setattr(cls, "Hormone Therapy",
            PermissibleValue(
                text="Hormone Therapy",
                description="A type of cancer treatment that removes, blocks, or adds hormones to treat cancer"))
        setattr(cls, "Intensity-Modulated Radiation Therapy",
            PermissibleValue(
                text="Intensity-Modulated Radiation Therapy",
                description="An advanced form of 3-Dimensional Conformal Radiation Therapy"))
        setattr(cls, "Low-Dose Rate Brachytherapy",
            PermissibleValue(
                text="Low-Dose Rate Brachytherapy",
                description="""Internal radiation treatment that targets a cancerous tissue with low doses of radiation through the use of inserted temporary or permanent implants"""))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not reported"))
        setattr(cls, "Organ Transplantation",
            PermissibleValue(
                text="Organ Transplantation",
                description="The transfer of an organ, organ part, or tissue from one body to another"))
        setattr(cls, "Palliative Care",
            PermissibleValue(
                text="Palliative Care",
                description="""Palliative care is the patient-and family-centered active holistic care of patients with advanced, progressive disease"""))
        setattr(cls, "Photon Beam Radiation Therapy",
            PermissibleValue(
                text="Photon Beam Radiation Therapy",
                description="Radiation therapy using photon beam"))
        setattr(cls, "Proton Beam Radiation Therapy",
            PermissibleValue(
                text="Proton Beam Radiation Therapy",
                description="A type of external beam radiation therapy using a beam of protons"))
        setattr(cls, "Radiation Therapy",
            PermissibleValue(
                text="Radiation Therapy",
                description="""Treatment of a disease by means of exposure of the target or the whole body to radiation"""))
        setattr(cls, "Radiofrequency Ablation",
            PermissibleValue(
                text="Radiofrequency Ablation",
                description="""A therapeutic procedure to eradicate or reduce small tumors using radiowaves to generate heat"""))
        setattr(cls, "Stem Cell Transplant",
            PermissibleValue(
                text="Stem Cell Transplant",
                description="A therapeutic procedure that involves the transplantation of hematopoietic stem cells"))
        setattr(cls, "Stereotactic Body Radiation Therapy",
            PermissibleValue(
                text="Stereotactic Body Radiation Therapy",
                description="""Stereotactic radiation therapy in which one or several maximum dose radiation treatments are delivered targeting cancers of the body"""))
        setattr(cls, "Stereotactic Radiosurgery",
            PermissibleValue(
                text="Stereotactic Radiosurgery",
                description="""A type of external radiation therapy that uses special equipment to position the patient and precisely give a single large dose of radiation to a tumor"""))
        setattr(cls, "Surgical Procedure",
            PermissibleValue(
                text="Surgical Procedure",
                description="A diagnostic or treatment procedure performed by manual and/or instrumental means"))
        setattr(cls, "Targeted Molecular Therapy",
            PermissibleValue(
                text="Targeted Molecular Therapy",
                description="""Cancer therapies designed to act upon specific molecules in metabolic pathways or processes involved in carcinogenesis"""))

class VitalStatusEnum(EnumDefinitionImpl):

    Alive = PermissibleValue(
        text="Alive",
        description="Alive")
    Deceased = PermissibleValue(
        text="Deceased",
        description="Deceased")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="VitalStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class CauseOfDeathEnum(EnumDefinitionImpl):

    Disease = PermissibleValue(
        text="Disease",
        description="Death due to disease")
    Other = PermissibleValue(
        text="Other",
        description="Death due to other causes")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="CauseOfDeathEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

class CauseOfDeathSourceEnum(EnumDefinitionImpl):

    Autopsy = PermissibleValue(
        text="Autopsy",
        description="Autopsy")
    Other = PermissibleValue(
        text="Other",
        description="Other source")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Not known, not observed, not recorded, or refused")

    _defn = EnumDefinition(
        name="CauseOfDeathSourceEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Death Certificate",
            PermissibleValue(
                text="Death Certificate",
                description="Death certificate"))
        setattr(cls, "Not Reported",
            PermissibleValue(
                text="Not Reported",
                description="Not provided or available"))

# Slots
class slots:
    pass

slots.caDSR_id = Slot(uri=HTAN.caDSR_id, name="caDSR_id", curie=HTAN.curie('caDSR_id'),
                   model_uri=HTAN.caDSR_id, domain=None, range=Optional[str])

slots.clinicalData__COMPONENT = Slot(uri=HTAN.COMPONENT, name="clinicalData__COMPONENT", curie=HTAN.curie('COMPONENT'),
                   model_uri=HTAN.clinicalData__COMPONENT, domain=None, range=Union[str, "ComponentEnum"])

slots.clinicalData__HTAN_PARTICIPANT_ID = Slot(uri=HTAN.HTAN_PARTICIPANT_ID, name="clinicalData__HTAN_PARTICIPANT_ID", curie=HTAN.curie('HTAN_PARTICIPANT_ID'),
                   model_uri=HTAN.clinicalData__HTAN_PARTICIPANT_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA20[0-9])(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$'))

slots.clinicalData__DEMOGRAPHICS = Slot(uri=HTAN.DEMOGRAPHICS, name="clinicalData__DEMOGRAPHICS", curie=HTAN.curie('DEMOGRAPHICS'),
                   model_uri=HTAN.clinicalData__DEMOGRAPHICS, domain=None, range=Union[dict, Demographics])

slots.clinicalData__VITAL_STATUS = Slot(uri=HTAN.VITAL_STATUS, name="clinicalData__VITAL_STATUS", curie=HTAN.curie('VITAL_STATUS'),
                   model_uri=HTAN.clinicalData__VITAL_STATUS, domain=None, range=Union[dict, VitalStatus])

slots.clinicalData__DIAGNOSIS = Slot(uri=HTAN.DIAGNOSIS, name="clinicalData__DIAGNOSIS", curie=HTAN.curie('DIAGNOSIS'),
                   model_uri=HTAN.clinicalData__DIAGNOSIS, domain=None, range=Union[dict, Diagnosis])

slots.clinicalData__EXPOSURES = Slot(uri=HTAN.EXPOSURES, name="clinicalData__EXPOSURES", curie=HTAN.curie('EXPOSURES'),
                   model_uri=HTAN.clinicalData__EXPOSURES, domain=None, range=Union[dict, Exposure])

slots.clinicalData__FAMILY_HISTORY = Slot(uri=HTAN.FAMILY_HISTORY, name="clinicalData__FAMILY_HISTORY", curie=HTAN.curie('FAMILY_HISTORY'),
                   model_uri=HTAN.clinicalData__FAMILY_HISTORY, domain=None, range=Union[dict, FamilyHistory])

slots.clinicalData__FOLLOW_UPS = Slot(uri=HTAN.FOLLOW_UPS, name="clinicalData__FOLLOW_UPS", curie=HTAN.curie('FOLLOW_UPS'),
                   model_uri=HTAN.clinicalData__FOLLOW_UPS, domain=None, range=Optional[Union[Union[dict, FollowUp], List[Union[dict, FollowUp]]]])

slots.clinicalData__MOLECULAR_TESTS = Slot(uri=HTAN.MOLECULAR_TESTS, name="clinicalData__MOLECULAR_TESTS", curie=HTAN.curie('MOLECULAR_TESTS'),
                   model_uri=HTAN.clinicalData__MOLECULAR_TESTS, domain=None, range=Optional[Union[Union[dict, MolecularTest], List[Union[dict, MolecularTest]]]])

slots.clinicalData__THERAPIES = Slot(uri=HTAN.THERAPIES, name="clinicalData__THERAPIES", curie=HTAN.curie('THERAPIES'),
                   model_uri=HTAN.clinicalData__THERAPIES, domain=None, range=Optional[Union[Union[dict, Therapy], List[Union[dict, Therapy]]]])

slots.demographics__ETHNIC_GROUP = Slot(uri=HTAN['clinical/demographics/ETHNIC_GROUP'], name="demographics__ETHNIC_GROUP", curie=HTAN.curie('clinical/demographics/ETHNIC_GROUP'),
                   model_uri=HTAN.demographics__ETHNIC_GROUP, domain=None, range=Union[str, "EthnicGroupEnum"])

slots.demographics__GENDER_IDENTITY = Slot(uri=HTAN['clinical/demographics/GENDER_IDENTITY'], name="demographics__GENDER_IDENTITY", curie=HTAN.curie('clinical/demographics/GENDER_IDENTITY'),
                   model_uri=HTAN.demographics__GENDER_IDENTITY, domain=None, range=Union[str, "GenderIdentityEnum"])

slots.demographics__SEX = Slot(uri=HTAN['clinical/demographics/SEX'], name="demographics__SEX", curie=HTAN.curie('clinical/demographics/SEX'),
                   model_uri=HTAN.demographics__SEX, domain=None, range=Union[str, "SexEnum"])

slots.demographics__RACE = Slot(uri=HTAN['clinical/demographics/RACE'], name="demographics__RACE", curie=HTAN.curie('clinical/demographics/RACE'),
                   model_uri=HTAN.demographics__RACE, domain=None, range=Union[str, "RaceEnum"])

slots.diagnosis__PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID = Slot(uri=HTAN['clinical/diagnosis/PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID'], name="diagnosis__PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID", curie=HTAN.curie('clinical/diagnosis/PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID'),
                   model_uri=HTAN.diagnosis__PRIMARY_DIAGNOSIS_NCI_THESAURUS_ID, domain=None, range=str)

slots.diagnosis__AGE_IN_DAYS_AT_DIAGNOSIS = Slot(uri=HTAN['clinical/diagnosis/AGE_IN_DAYS_AT_DIAGNOSIS'], name="diagnosis__AGE_IN_DAYS_AT_DIAGNOSIS", curie=HTAN.curie('clinical/diagnosis/AGE_IN_DAYS_AT_DIAGNOSIS'),
                   model_uri=HTAN.diagnosis__AGE_IN_DAYS_AT_DIAGNOSIS, domain=None, range=int)

slots.diagnosis__TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE = Slot(uri=HTAN['clinical/diagnosis/TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE'], name="diagnosis__TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE", curie=HTAN.curie('clinical/diagnosis/TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE'),
                   model_uri=HTAN.diagnosis__TISSUE_OR_ORGAN_OF_ORIGIN_UBERON_CODE, domain=None, range=str)

slots.diagnosis__TUMOR_GRADE = Slot(uri=HTAN['clinical/diagnosis/TUMOR_GRADE'], name="diagnosis__TUMOR_GRADE", curie=HTAN.curie('clinical/diagnosis/TUMOR_GRADE'),
                   model_uri=HTAN.diagnosis__TUMOR_GRADE, domain=None, range=Union[str, "TumorGradeEnum"])

slots.diagnosis__CLINICAL_T_STAGE = Slot(uri=HTAN['clinical/diagnosis/CLINICAL_T_STAGE'], name="diagnosis__CLINICAL_T_STAGE", curie=HTAN.curie('clinical/diagnosis/CLINICAL_T_STAGE'),
                   model_uri=HTAN.diagnosis__CLINICAL_T_STAGE, domain=None, range=Union[str, "ClinicalTStageEnum"])

slots.diagnosis__CLINICAL_N_STAGE = Slot(uri=HTAN['clinical/diagnosis/CLINICAL_N_STAGE'], name="diagnosis__CLINICAL_N_STAGE", curie=HTAN.curie('clinical/diagnosis/CLINICAL_N_STAGE'),
                   model_uri=HTAN.diagnosis__CLINICAL_N_STAGE, domain=None, range=Union[str, "ClinicalNStageEnum"])

slots.diagnosis__CLINICAL_M_STAGE = Slot(uri=HTAN['clinical/diagnosis/CLINICAL_M_STAGE'], name="diagnosis__CLINICAL_M_STAGE", curie=HTAN.curie('clinical/diagnosis/CLINICAL_M_STAGE'),
                   model_uri=HTAN.diagnosis__CLINICAL_M_STAGE, domain=None, range=Union[str, "ClinicalMStageEnum"])

slots.diagnosis__AJCC_STAGING_SYSTEM_EDITION = Slot(uri=HTAN['clinical/diagnosis/AJCC_STAGING_SYSTEM_EDITION'], name="diagnosis__AJCC_STAGING_SYSTEM_EDITION", curie=HTAN.curie('clinical/diagnosis/AJCC_STAGING_SYSTEM_EDITION'),
                   model_uri=HTAN.diagnosis__AJCC_STAGING_SYSTEM_EDITION, domain=None, range=Union[str, "AJCCStagingSystemEditionEnum"])

slots.diagnosis__AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS = Slot(uri=HTAN['clinical/diagnosis/AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS'], name="diagnosis__AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS", curie=HTAN.curie('clinical/diagnosis/AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS'),
                   model_uri=HTAN.diagnosis__AGE_IN_DAYS_AT_LAST_KNOWN_DISEASE_STATUS, domain=None, range=int)

slots.diagnosis__LAST_KNOWN_DISEASE_STATUS = Slot(uri=HTAN['clinical/diagnosis/LAST_KNOWN_DISEASE_STATUS'], name="diagnosis__LAST_KNOWN_DISEASE_STATUS", curie=HTAN.curie('clinical/diagnosis/LAST_KNOWN_DISEASE_STATUS'),
                   model_uri=HTAN.diagnosis__LAST_KNOWN_DISEASE_STATUS, domain=None, range=Union[str, "LastKnownDiseaseStatusEnum"])

slots.diagnosis__TUMOR_CLASSIFICATION_CATEGORY = Slot(uri=HTAN['clinical/diagnosis/TUMOR_CLASSIFICATION_CATEGORY'], name="diagnosis__TUMOR_CLASSIFICATION_CATEGORY", curie=HTAN.curie('clinical/diagnosis/TUMOR_CLASSIFICATION_CATEGORY'),
                   model_uri=HTAN.diagnosis__TUMOR_CLASSIFICATION_CATEGORY, domain=None, range=Union[str, "TumorClassificationCategoryEnum"])

slots.diagnosis__METASTASIS_AT_DIAGNOSIS = Slot(uri=HTAN['clinical/diagnosis/METASTASIS_AT_DIAGNOSIS'], name="diagnosis__METASTASIS_AT_DIAGNOSIS", curie=HTAN.curie('clinical/diagnosis/METASTASIS_AT_DIAGNOSIS'),
                   model_uri=HTAN.diagnosis__METASTASIS_AT_DIAGNOSIS, domain=None, range=Union[str, "MetastasisAtDiagnosisEnum"])

slots.diagnosis__METHOD_OF_DIAGNOSIS = Slot(uri=HTAN['clinical/diagnosis/METHOD_OF_DIAGNOSIS'], name="diagnosis__METHOD_OF_DIAGNOSIS", curie=HTAN.curie('clinical/diagnosis/METHOD_OF_DIAGNOSIS'),
                   model_uri=HTAN.diagnosis__METHOD_OF_DIAGNOSIS, domain=None, range=Union[str, "MethodOfDiagnosisEnum"])

slots.exposure__SMOKING_HISTORY = Slot(uri=HTAN['clinical/exposure/SMOKING_HISTORY'], name="exposure__SMOKING_HISTORY", curie=HTAN.curie('clinical/exposure/SMOKING_HISTORY'),
                   model_uri=HTAN.exposure__SMOKING_HISTORY, domain=None, range=Union[str, "SmokingHistoryEnum"])

slots.exposure__YEARS_SMOKED = Slot(uri=HTAN['clinical/exposure/YEARS_SMOKED'], name="exposure__YEARS_SMOKED", curie=HTAN.curie('clinical/exposure/YEARS_SMOKED'),
                   model_uri=HTAN.exposure__YEARS_SMOKED, domain=None, range=Optional[int])

slots.exposure__PACK_YEARS_SMOKED = Slot(uri=HTAN['clinical/exposure/PACK_YEARS_SMOKED'], name="exposure__PACK_YEARS_SMOKED", curie=HTAN.curie('clinical/exposure/PACK_YEARS_SMOKED'),
                   model_uri=HTAN.exposure__PACK_YEARS_SMOKED, domain=None, range=Optional[Decimal])

slots.exposure__ALCOHOL_HISTORY_INDICATOR = Slot(uri=HTAN['clinical/exposure/ALCOHOL_HISTORY_INDICATOR'], name="exposure__ALCOHOL_HISTORY_INDICATOR", curie=HTAN.curie('clinical/exposure/ALCOHOL_HISTORY_INDICATOR'),
                   model_uri=HTAN.exposure__ALCOHOL_HISTORY_INDICATOR, domain=None, range=Union[str, "AlcoholHistoryIndicatorEnum"])

slots.exposure__ENVIRONMENTAL_EXPOSURE = Slot(uri=HTAN['clinical/exposure/ENVIRONMENTAL_EXPOSURE'], name="exposure__ENVIRONMENTAL_EXPOSURE", curie=HTAN.curie('clinical/exposure/ENVIRONMENTAL_EXPOSURE'),
                   model_uri=HTAN.exposure__ENVIRONMENTAL_EXPOSURE, domain=None, range=Union[str, "EnvironmentalExposureEnum"])

slots.exposure__ENVIRONMENTAL_EXPOSURE_TYPE = Slot(uri=HTAN['clinical/exposure/ENVIRONMENTAL_EXPOSURE_TYPE'], name="exposure__ENVIRONMENTAL_EXPOSURE_TYPE", curie=HTAN.curie('clinical/exposure/ENVIRONMENTAL_EXPOSURE_TYPE'),
                   model_uri=HTAN.exposure__ENVIRONMENTAL_EXPOSURE_TYPE, domain=None, range=Optional[Union[str, "EnvironmentalExposureTypeEnum"]])

slots.familyHistory__FAMILY_MEMBER_CANCER_HISTORY = Slot(uri=HTAN['clinical/family_history/FAMILY_MEMBER_CANCER_HISTORY'], name="familyHistory__FAMILY_MEMBER_CANCER_HISTORY", curie=HTAN.curie('clinical/family_history/FAMILY_MEMBER_CANCER_HISTORY'),
                   model_uri=HTAN.familyHistory__FAMILY_MEMBER_CANCER_HISTORY, domain=None, range=Optional[Union[str, "YesNoUnknownNotReportedEnum"]])

slots.familyHistory__RELATIVES_WITH_CANCER_HISTORY = Slot(uri=HTAN['clinical/family_history/RELATIVES_WITH_CANCER_HISTORY'], name="familyHistory__RELATIVES_WITH_CANCER_HISTORY", curie=HTAN.curie('clinical/family_history/RELATIVES_WITH_CANCER_HISTORY'),
                   model_uri=HTAN.familyHistory__RELATIVES_WITH_CANCER_HISTORY, domain=None, range=Optional[int])

slots.followUp__AGE_IN_DAYS_AT_FOLLOWUP = Slot(uri=HTAN['clinical/followup/AGE_IN_DAYS_AT_FOLLOWUP'], name="followUp__AGE_IN_DAYS_AT_FOLLOWUP", curie=HTAN.curie('clinical/followup/AGE_IN_DAYS_AT_FOLLOWUP'),
                   model_uri=HTAN.followUp__AGE_IN_DAYS_AT_FOLLOWUP, domain=None, range=int)

slots.followUp__PROGRESSION_OR_RECURRENCE = Slot(uri=HTAN['clinical/followup/PROGRESSION_OR_RECURRENCE'], name="followUp__PROGRESSION_OR_RECURRENCE", curie=HTAN.curie('clinical/followup/PROGRESSION_OR_RECURRENCE'),
                   model_uri=HTAN.followUp__PROGRESSION_OR_RECURRENCE, domain=None, range=Union[str, "ProgressionOrRecurrenceEnum"])

slots.followUp__PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE = Slot(uri=HTAN['clinical/followup/PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE'], name="followUp__PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE", curie=HTAN.curie('clinical/followup/PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE'),
                   model_uri=HTAN.followUp__PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, domain=None, range=Optional[str])

slots.followUp__PROGRESSION_OR_RECURRENCE_TYPE = Slot(uri=HTAN['clinical/followup/PROGRESSION_OR_RECURRENCE_TYPE'], name="followUp__PROGRESSION_OR_RECURRENCE_TYPE", curie=HTAN.curie('clinical/followup/PROGRESSION_OR_RECURRENCE_TYPE'),
                   model_uri=HTAN.followUp__PROGRESSION_OR_RECURRENCE_TYPE, domain=None, range=Optional[Union[str, "ProgressionTypeEnum"]])

slots.followUp__EVIDENCE_OF_RECURRENCE_TYPE = Slot(uri=HTAN['clinical/followup/EVIDENCE_OF_RECURRENCE_TYPE'], name="followUp__EVIDENCE_OF_RECURRENCE_TYPE", curie=HTAN.curie('clinical/followup/EVIDENCE_OF_RECURRENCE_TYPE'),
                   model_uri=HTAN.followUp__EVIDENCE_OF_RECURRENCE_TYPE, domain=None, range=Optional[Union[str, "EvidenceOfRecurrenceTypeEnum"]])

slots.followUp__AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE = Slot(uri=HTAN['clinical/followup/AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE'], name="followUp__AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE", curie=HTAN.curie('clinical/followup/AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE'),
                   model_uri=HTAN.followUp__AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, domain=None, range=Optional[int])

slots.followUp__DISEASE_RESPONSE = Slot(uri=HTAN['clinical/followup/DISEASE_RESPONSE'], name="followUp__DISEASE_RESPONSE", curie=HTAN.curie('clinical/followup/DISEASE_RESPONSE'),
                   model_uri=HTAN.followUp__DISEASE_RESPONSE, domain=None, range=Union[str, "DiseaseResponseEnum"])

slots.followUp__ECOG_PERFORMANCE_STATUS = Slot(uri=HTAN['clinical/followup/ECOG_PERFORMANCE_STATUS'], name="followUp__ECOG_PERFORMANCE_STATUS", curie=HTAN.curie('clinical/followup/ECOG_PERFORMANCE_STATUS'),
                   model_uri=HTAN.followUp__ECOG_PERFORMANCE_STATUS, domain=None, range=Union[str, "ECOGPerformanceStatusEnum"])

slots.followUp__MENOPAUSE_STATUS = Slot(uri=HTAN['clinical/followup/MENOPAUSE_STATUS'], name="followUp__MENOPAUSE_STATUS", curie=HTAN.curie('clinical/followup/MENOPAUSE_STATUS'),
                   model_uri=HTAN.followUp__MENOPAUSE_STATUS, domain=None, range=Optional[Union[str, "MenopauseStatusEnum"]])

slots.molecularTest__TIMEPOINT_LABEL = Slot(uri=HTAN['clinical/molecular/TIMEPOINT_LABEL'], name="molecularTest__TIMEPOINT_LABEL", curie=HTAN.curie('clinical/molecular/TIMEPOINT_LABEL'),
                   model_uri=HTAN.molecularTest__TIMEPOINT_LABEL, domain=None, range=str)

slots.molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_START = Slot(uri=HTAN['clinical/molecular/AGE_IN_DAYS_AT_MOLECULAR_TEST_START'], name="molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_START", curie=HTAN.curie('clinical/molecular/AGE_IN_DAYS_AT_MOLECULAR_TEST_START'),
                   model_uri=HTAN.molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_START, domain=None, range=int)

slots.molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP = Slot(uri=HTAN['clinical/molecular/AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP'], name="molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP", curie=HTAN.curie('clinical/molecular/AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP'),
                   model_uri=HTAN.molecularTest__AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, domain=None, range=int)

slots.molecularTest__GENE_SYMBOL = Slot(uri=HTAN['clinical/molecular/GENE_SYMBOL'], name="molecularTest__GENE_SYMBOL", curie=HTAN.curie('clinical/molecular/GENE_SYMBOL'),
                   model_uri=HTAN.molecularTest__GENE_SYMBOL, domain=None, range=str)

slots.molecularTest__MOLECULAR_ANALYSIS_METHOD = Slot(uri=HTAN['clinical/molecular/MOLECULAR_ANALYSIS_METHOD'], name="molecularTest__MOLECULAR_ANALYSIS_METHOD", curie=HTAN.curie('clinical/molecular/MOLECULAR_ANALYSIS_METHOD'),
                   model_uri=HTAN.molecularTest__MOLECULAR_ANALYSIS_METHOD, domain=None, range=Union[str, "MolecularAnalysisMethodEnum"])

slots.molecularTest__MOLECULAR_ANALYSIS_RESULT = Slot(uri=HTAN['clinical/molecular/MOLECULAR_ANALYSIS_RESULT'], name="molecularTest__MOLECULAR_ANALYSIS_RESULT", curie=HTAN.curie('clinical/molecular/MOLECULAR_ANALYSIS_RESULT'),
                   model_uri=HTAN.molecularTest__MOLECULAR_ANALYSIS_RESULT, domain=None, range=str)

slots.molecularTest__AA_CHANGE = Slot(uri=HTAN['clinical/molecular/AA_CHANGE'], name="molecularTest__AA_CHANGE", curie=HTAN.curie('clinical/molecular/AA_CHANGE'),
                   model_uri=HTAN.molecularTest__AA_CHANGE, domain=None, range=str)

slots.molecularTest__CLINICAL_BIOSPECIMEN_TYPE = Slot(uri=HTAN['clinical/molecular/CLINICAL_BIOSPECIMEN_TYPE'], name="molecularTest__CLINICAL_BIOSPECIMEN_TYPE", curie=HTAN.curie('clinical/molecular/CLINICAL_BIOSPECIMEN_TYPE'),
                   model_uri=HTAN.molecularTest__CLINICAL_BIOSPECIMEN_TYPE, domain=None, range=Union[str, "ClinicalBiospecimenTypeEnum"])

slots.molecularTest__COPY_NUMBER = Slot(uri=HTAN['clinical/molecular/COPY_NUMBER'], name="molecularTest__COPY_NUMBER", curie=HTAN.curie('clinical/molecular/COPY_NUMBER'),
                   model_uri=HTAN.molecularTest__COPY_NUMBER, domain=None, range=int)

slots.molecularTest__EXON = Slot(uri=HTAN['clinical/molecular/EXON'], name="molecularTest__EXON", curie=HTAN.curie('clinical/molecular/EXON'),
                   model_uri=HTAN.molecularTest__EXON, domain=None, range=int)

slots.molecularTest__MOLECULAR_CONSEQUENCE = Slot(uri=HTAN['clinical/molecular/MOLECULAR_CONSEQUENCE'], name="molecularTest__MOLECULAR_CONSEQUENCE", curie=HTAN.curie('clinical/molecular/MOLECULAR_CONSEQUENCE'),
                   model_uri=HTAN.molecularTest__MOLECULAR_CONSEQUENCE, domain=None, range=Union[str, "MolecularConsequenceEnum"])

slots.molecularTest__PATHOGENICITY = Slot(uri=HTAN['clinical/molecular/PATHOGENICITY'], name="molecularTest__PATHOGENICITY", curie=HTAN.curie('clinical/molecular/PATHOGENICITY'),
                   model_uri=HTAN.molecularTest__PATHOGENICITY, domain=None, range=Union[str, "PathogenicityEnum"])

slots.molecularTest__TEST_ANALYTE_TYPE = Slot(uri=HTAN['clinical/molecular/TEST_ANALYTE_TYPE'], name="molecularTest__TEST_ANALYTE_TYPE", curie=HTAN.curie('clinical/molecular/TEST_ANALYTE_TYPE'),
                   model_uri=HTAN.molecularTest__TEST_ANALYTE_TYPE, domain=None, range=Union[str, "TestAnalyteTypeEnum"])

slots.molecularTest__TEST_UNITS = Slot(uri=HTAN['clinical/molecular/TEST_UNITS'], name="molecularTest__TEST_UNITS", curie=HTAN.curie('clinical/molecular/TEST_UNITS'),
                   model_uri=HTAN.molecularTest__TEST_UNITS, domain=None, range=str)

slots.molecularTest__TEST_RESULT = Slot(uri=HTAN['clinical/molecular/TEST_RESULT'], name="molecularTest__TEST_RESULT", curie=HTAN.curie('clinical/molecular/TEST_RESULT'),
                   model_uri=HTAN.molecularTest__TEST_RESULT, domain=None, range=str)

slots.molecularTest__VARIANT_ORIGIN = Slot(uri=HTAN['clinical/molecular/VARIANT_ORIGIN'], name="molecularTest__VARIANT_ORIGIN", curie=HTAN.curie('clinical/molecular/VARIANT_ORIGIN'),
                   model_uri=HTAN.molecularTest__VARIANT_ORIGIN, domain=None, range=Union[str, "VariantOriginEnum"])

slots.molecularTest__VARIANT_TYPE = Slot(uri=HTAN['clinical/molecular/VARIANT_TYPE'], name="molecularTest__VARIANT_TYPE", curie=HTAN.curie('clinical/molecular/VARIANT_TYPE'),
                   model_uri=HTAN.molecularTest__VARIANT_TYPE, domain=None, range=Union[str, "VariantTypeEnum"])

slots.therapy__INITIAL_DISEASE_STATUS = Slot(uri=HTAN['clinical/therapy/INITIAL_DISEASE_STATUS'], name="therapy__INITIAL_DISEASE_STATUS", curie=HTAN.curie('clinical/therapy/INITIAL_DISEASE_STATUS'),
                   model_uri=HTAN.therapy__INITIAL_DISEASE_STATUS, domain=None, range=str)

slots.therapy__TREATMENT_INTENT_TYPE = Slot(uri=HTAN['clinical/therapy/TREATMENT_INTENT_TYPE'], name="therapy__TREATMENT_INTENT_TYPE", curie=HTAN.curie('clinical/therapy/TREATMENT_INTENT_TYPE'),
                   model_uri=HTAN.therapy__TREATMENT_INTENT_TYPE, domain=None, range=Union[str, "TreatmentIntentTypeEnum"])

slots.therapy__TREATMENT_TYPE = Slot(uri=HTAN['clinical/therapy/TREATMENT_TYPE'], name="therapy__TREATMENT_TYPE", curie=HTAN.curie('clinical/therapy/TREATMENT_TYPE'),
                   model_uri=HTAN.therapy__TREATMENT_TYPE, domain=None, range=Union[Union[str, "TreatmentTypeEnum"], List[Union[str, "TreatmentTypeEnum"]]],
                   pattern=re.compile(r'^[^|]+(\|[^|]+)*$'))

slots.therapy__PHARMACOTHERAPY_TYPE = Slot(uri=HTAN['clinical/therapy/PHARMACOTHERAPY_TYPE'], name="therapy__PHARMACOTHERAPY_TYPE", curie=HTAN.curie('clinical/therapy/PHARMACOTHERAPY_TYPE'),
                   model_uri=HTAN.therapy__PHARMACOTHERAPY_TYPE, domain=None, range=Union[str, "PharmacotherapyTypeEnum"])

slots.therapy__THERAPEUTIC_AGENTS = Slot(uri=HTAN['clinical/therapy/THERAPEUTIC_AGENTS'], name="therapy__THERAPEUTIC_AGENTS", curie=HTAN.curie('clinical/therapy/THERAPEUTIC_AGENTS'),
                   model_uri=HTAN.therapy__THERAPEUTIC_AGENTS, domain=None, range=Union[str, List[str]],
                   pattern=re.compile(r'^[^|]+(\|[^|]+)*$'))

slots.therapy__THERAPY_ANATOMIC_SITE_UBERON_CODE = Slot(uri=HTAN['clinical/therapy/THERAPY_ANATOMIC_SITE_UBERON_CODE'], name="therapy__THERAPY_ANATOMIC_SITE_UBERON_CODE", curie=HTAN.curie('clinical/therapy/THERAPY_ANATOMIC_SITE_UBERON_CODE'),
                   model_uri=HTAN.therapy__THERAPY_ANATOMIC_SITE_UBERON_CODE, domain=None, range=Optional[str])

slots.therapy__AGE_IN_DAYS_AT_TREATMENT_START = Slot(uri=HTAN['clinical/therapy/AGE_IN_DAYS_AT_TREATMENT_START'], name="therapy__AGE_IN_DAYS_AT_TREATMENT_START", curie=HTAN.curie('clinical/therapy/AGE_IN_DAYS_AT_TREATMENT_START'),
                   model_uri=HTAN.therapy__AGE_IN_DAYS_AT_TREATMENT_START, domain=None, range=int)

slots.therapy__AGE_IN_DAYS_AT_TREATMENT_END = Slot(uri=HTAN['clinical/therapy/AGE_IN_DAYS_AT_TREATMENT_END'], name="therapy__AGE_IN_DAYS_AT_TREATMENT_END", curie=HTAN.curie('clinical/therapy/AGE_IN_DAYS_AT_TREATMENT_END'),
                   model_uri=HTAN.therapy__AGE_IN_DAYS_AT_TREATMENT_END, domain=None, range=int)

slots.therapy__OFF_TREATMENT_REASON = Slot(uri=HTAN['clinical/therapy/OFF_TREATMENT_REASON'], name="therapy__OFF_TREATMENT_REASON", curie=HTAN.curie('clinical/therapy/OFF_TREATMENT_REASON'),
                   model_uri=HTAN.therapy__OFF_TREATMENT_REASON, domain=None, range=Optional[Union[str, "OffTreatmentReasonEnum"]])

slots.therapy__REGIMEN_OR_LINE_OF_THERAPY = Slot(uri=HTAN['clinical/therapy/REGIMEN_OR_LINE_OF_THERAPY'], name="therapy__REGIMEN_OR_LINE_OF_THERAPY", curie=HTAN.curie('clinical/therapy/REGIMEN_OR_LINE_OF_THERAPY'),
                   model_uri=HTAN.therapy__REGIMEN_OR_LINE_OF_THERAPY, domain=None, range=Optional[Union[str, "RegimenOrLineOfTherapyEnum"]])

slots.therapy__NUMBER_OF_CYCLES = Slot(uri=HTAN['clinical/therapy/NUMBER_OF_CYCLES'], name="therapy__NUMBER_OF_CYCLES", curie=HTAN.curie('clinical/therapy/NUMBER_OF_CYCLES'),
                   model_uri=HTAN.therapy__NUMBER_OF_CYCLES, domain=None, range=Optional[int])

slots.therapy__RESPONSE = Slot(uri=HTAN['clinical/therapy/RESPONSE'], name="therapy__RESPONSE", curie=HTAN.curie('clinical/therapy/RESPONSE'),
                   model_uri=HTAN.therapy__RESPONSE, domain=None, range=Optional[str])

slots.vitalStatus__VITAL_STATUS = Slot(uri=HTAN['clinical/vital_status/VITAL_STATUS'], name="vitalStatus__VITAL_STATUS", curie=HTAN.curie('clinical/vital_status/VITAL_STATUS'),
                   model_uri=HTAN.vitalStatus__VITAL_STATUS, domain=None, range=Union[str, "VitalStatusEnum"])

slots.vitalStatus__AGE_IN_DAYS_AT_DEATH = Slot(uri=HTAN['clinical/vital_status/AGE_IN_DAYS_AT_DEATH'], name="vitalStatus__AGE_IN_DAYS_AT_DEATH", curie=HTAN.curie('clinical/vital_status/AGE_IN_DAYS_AT_DEATH'),
                   model_uri=HTAN.vitalStatus__AGE_IN_DAYS_AT_DEATH, domain=None, range=Optional[int])

slots.vitalStatus__CAUSE_OF_DEATH = Slot(uri=HTAN['clinical/vital_status/CAUSE_OF_DEATH'], name="vitalStatus__CAUSE_OF_DEATH", curie=HTAN.curie('clinical/vital_status/CAUSE_OF_DEATH'),
                   model_uri=HTAN.vitalStatus__CAUSE_OF_DEATH, domain=None, range=Optional[Union[str, "CauseOfDeathEnum"]])

slots.vitalStatus__CAUSE_OF_DEATH_SOURCE = Slot(uri=HTAN['clinical/vital_status/CAUSE_OF_DEATH_SOURCE'], name="vitalStatus__CAUSE_OF_DEATH_SOURCE", curie=HTAN.curie('clinical/vital_status/CAUSE_OF_DEATH_SOURCE'),
                   model_uri=HTAN.vitalStatus__CAUSE_OF_DEATH_SOURCE, domain=None, range=Optional[Union[str, "CauseOfDeathSourceEnum"]])

slots.CLINICAL_T_STAGE = Slot(uri=HTAN.CLINICAL_T_STAGE, name="CLINICAL_T_STAGE", curie=HTAN.curie('CLINICAL_T_STAGE'),
                   model_uri=HTAN.CLINICAL_T_STAGE, domain=None, range=Optional[str])

slots.CLINICAL_N_STAGE = Slot(uri=HTAN.CLINICAL_N_STAGE, name="CLINICAL_N_STAGE", curie=HTAN.curie('CLINICAL_N_STAGE'),
                   model_uri=HTAN.CLINICAL_N_STAGE, domain=None, range=Optional[str])

slots.CLINICAL_M_STAGE = Slot(uri=HTAN.CLINICAL_M_STAGE, name="CLINICAL_M_STAGE", curie=HTAN.curie('CLINICAL_M_STAGE'),
                   model_uri=HTAN.CLINICAL_M_STAGE, domain=None, range=Optional[str])

slots.AJCC_STAGING_SYSTEM_EDITION = Slot(uri=HTAN.AJCC_STAGING_SYSTEM_EDITION, name="AJCC_STAGING_SYSTEM_EDITION", curie=HTAN.curie('AJCC_STAGING_SYSTEM_EDITION'),
                   model_uri=HTAN.AJCC_STAGING_SYSTEM_EDITION, domain=None, range=Optional[str])

slots.METASTASIS_AT_DIAGNOSIS = Slot(uri=HTAN.METASTASIS_AT_DIAGNOSIS, name="METASTASIS_AT_DIAGNOSIS", curie=HTAN.curie('METASTASIS_AT_DIAGNOSIS'),
                   model_uri=HTAN.METASTASIS_AT_DIAGNOSIS, domain=None, range=Optional[str])

slots.YEARS_SMOKED = Slot(uri=HTAN.YEARS_SMOKED, name="YEARS_SMOKED", curie=HTAN.curie('YEARS_SMOKED'),
                   model_uri=HTAN.YEARS_SMOKED, domain=None, range=Optional[str])

slots.PACK_YEARS_SMOKED = Slot(uri=HTAN.PACK_YEARS_SMOKED, name="PACK_YEARS_SMOKED", curie=HTAN.curie('PACK_YEARS_SMOKED'),
                   model_uri=HTAN.PACK_YEARS_SMOKED, domain=None, range=Optional[str])

slots.ENVIRONMENTAL_EXPOSURE_TYPE = Slot(uri=HTAN.ENVIRONMENTAL_EXPOSURE_TYPE, name="ENVIRONMENTAL_EXPOSURE_TYPE", curie=HTAN.curie('ENVIRONMENTAL_EXPOSURE_TYPE'),
                   model_uri=HTAN.ENVIRONMENTAL_EXPOSURE_TYPE, domain=None, range=Optional[str])

slots.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE = Slot(uri=HTAN.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, name="PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE", curie=HTAN.curie('PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE'),
                   model_uri=HTAN.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, domain=None, range=Optional[str])

slots.PROGRESSION_OR_RECURRENCE_TYPE = Slot(uri=HTAN.PROGRESSION_OR_RECURRENCE_TYPE, name="PROGRESSION_OR_RECURRENCE_TYPE", curie=HTAN.curie('PROGRESSION_OR_RECURRENCE_TYPE'),
                   model_uri=HTAN.PROGRESSION_OR_RECURRENCE_TYPE, domain=None, range=Optional[str])

slots.EVIDENCE_OF_RECURRENCE_TYPE = Slot(uri=HTAN.EVIDENCE_OF_RECURRENCE_TYPE, name="EVIDENCE_OF_RECURRENCE_TYPE", curie=HTAN.curie('EVIDENCE_OF_RECURRENCE_TYPE'),
                   model_uri=HTAN.EVIDENCE_OF_RECURRENCE_TYPE, domain=None, range=Optional[str])

slots.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE = Slot(uri=HTAN.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, name="AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE", curie=HTAN.curie('AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE'),
                   model_uri=HTAN.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, domain=None, range=Optional[str])

slots.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP = Slot(uri=HTAN.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, name="AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP", curie=HTAN.curie('AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP'),
                   model_uri=HTAN.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, domain=None, range=Optional[str])

slots.AA_CHANGE = Slot(uri=HTAN.AA_CHANGE, name="AA_CHANGE", curie=HTAN.curie('AA_CHANGE'),
                   model_uri=HTAN.AA_CHANGE, domain=None, range=Optional[str])

slots.COPY_NUMBER = Slot(uri=HTAN.COPY_NUMBER, name="COPY_NUMBER", curie=HTAN.curie('COPY_NUMBER'),
                   model_uri=HTAN.COPY_NUMBER, domain=None, range=Optional[str])

slots.EXON = Slot(uri=HTAN.EXON, name="EXON", curie=HTAN.curie('EXON'),
                   model_uri=HTAN.EXON, domain=None, range=Optional[str])

slots.MOLECULAR_CONSEQUENCE = Slot(uri=HTAN.MOLECULAR_CONSEQUENCE, name="MOLECULAR_CONSEQUENCE", curie=HTAN.curie('MOLECULAR_CONSEQUENCE'),
                   model_uri=HTAN.MOLECULAR_CONSEQUENCE, domain=None, range=Optional[str])

slots.PATHOGENICITY = Slot(uri=HTAN.PATHOGENICITY, name="PATHOGENICITY", curie=HTAN.curie('PATHOGENICITY'),
                   model_uri=HTAN.PATHOGENICITY, domain=None, range=Optional[str])

slots.TEST_ANALYTE_TYPE = Slot(uri=HTAN.TEST_ANALYTE_TYPE, name="TEST_ANALYTE_TYPE", curie=HTAN.curie('TEST_ANALYTE_TYPE'),
                   model_uri=HTAN.TEST_ANALYTE_TYPE, domain=None, range=Optional[str])

slots.TEST_UNITS = Slot(uri=HTAN.TEST_UNITS, name="TEST_UNITS", curie=HTAN.curie('TEST_UNITS'),
                   model_uri=HTAN.TEST_UNITS, domain=None, range=Optional[str])

slots.THERAPY_ANATOMIC_SITE_UBERON_CODE = Slot(uri=HTAN.THERAPY_ANATOMIC_SITE_UBERON_CODE, name="THERAPY_ANATOMIC_SITE_UBERON_CODE", curie=HTAN.curie('THERAPY_ANATOMIC_SITE_UBERON_CODE'),
                   model_uri=HTAN.THERAPY_ANATOMIC_SITE_UBERON_CODE, domain=None, range=Optional[str])

slots.OFF_TREATMENT_REASON = Slot(uri=HTAN.OFF_TREATMENT_REASON, name="OFF_TREATMENT_REASON", curie=HTAN.curie('OFF_TREATMENT_REASON'),
                   model_uri=HTAN.OFF_TREATMENT_REASON, domain=None, range=Optional[str])

slots.REGIMEN_OR_LINE_OF_THERAPY = Slot(uri=HTAN.REGIMEN_OR_LINE_OF_THERAPY, name="REGIMEN_OR_LINE_OF_THERAPY", curie=HTAN.curie('REGIMEN_OR_LINE_OF_THERAPY'),
                   model_uri=HTAN.REGIMEN_OR_LINE_OF_THERAPY, domain=None, range=Optional[str])

slots.NUMBER_OF_CYCLES = Slot(uri=HTAN.NUMBER_OF_CYCLES, name="NUMBER_OF_CYCLES", curie=HTAN.curie('NUMBER_OF_CYCLES'),
                   model_uri=HTAN.NUMBER_OF_CYCLES, domain=None, range=Optional[str])

slots.RESPONSE = Slot(uri=HTAN.RESPONSE, name="RESPONSE", curie=HTAN.curie('RESPONSE'),
                   model_uri=HTAN.RESPONSE, domain=None, range=Optional[str])

slots.AGE_IN_DAYS_AT_DEATH = Slot(uri=HTAN.AGE_IN_DAYS_AT_DEATH, name="AGE_IN_DAYS_AT_DEATH", curie=HTAN.curie('AGE_IN_DAYS_AT_DEATH'),
                   model_uri=HTAN.AGE_IN_DAYS_AT_DEATH, domain=None, range=Optional[str])

slots.CAUSE_OF_DEATH = Slot(uri=HTAN.CAUSE_OF_DEATH, name="CAUSE_OF_DEATH", curie=HTAN.curie('CAUSE_OF_DEATH'),
                   model_uri=HTAN.CAUSE_OF_DEATH, domain=None, range=Optional[str])

slots.CAUSE_OF_DEATH_SOURCE = Slot(uri=HTAN.CAUSE_OF_DEATH_SOURCE, name="CAUSE_OF_DEATH_SOURCE", curie=HTAN.curie('CAUSE_OF_DEATH_SOURCE'),
                   model_uri=HTAN.CAUSE_OF_DEATH_SOURCE, domain=None, range=Optional[str])

slots.Diagnosis_CLINICAL_T_STAGE = Slot(uri=HTAN.CLINICAL_T_STAGE, name="Diagnosis_CLINICAL_T_STAGE", curie=HTAN.curie('CLINICAL_T_STAGE'),
                   model_uri=HTAN.Diagnosis_CLINICAL_T_STAGE, domain=Diagnosis, range=Optional[str])

slots.Diagnosis_CLINICAL_N_STAGE = Slot(uri=HTAN.CLINICAL_N_STAGE, name="Diagnosis_CLINICAL_N_STAGE", curie=HTAN.curie('CLINICAL_N_STAGE'),
                   model_uri=HTAN.Diagnosis_CLINICAL_N_STAGE, domain=Diagnosis, range=Optional[str])

slots.Diagnosis_CLINICAL_M_STAGE = Slot(uri=HTAN.CLINICAL_M_STAGE, name="Diagnosis_CLINICAL_M_STAGE", curie=HTAN.curie('CLINICAL_M_STAGE'),
                   model_uri=HTAN.Diagnosis_CLINICAL_M_STAGE, domain=Diagnosis, range=Optional[str])

slots.Diagnosis_AJCC_STAGING_SYSTEM_EDITION = Slot(uri=HTAN.AJCC_STAGING_SYSTEM_EDITION, name="Diagnosis_AJCC_STAGING_SYSTEM_EDITION", curie=HTAN.curie('AJCC_STAGING_SYSTEM_EDITION'),
                   model_uri=HTAN.Diagnosis_AJCC_STAGING_SYSTEM_EDITION, domain=Diagnosis, range=Optional[str])

slots.Diagnosis_METASTASIS_AT_DIAGNOSIS = Slot(uri=HTAN.METASTASIS_AT_DIAGNOSIS, name="Diagnosis_METASTASIS_AT_DIAGNOSIS", curie=HTAN.curie('METASTASIS_AT_DIAGNOSIS'),
                   model_uri=HTAN.Diagnosis_METASTASIS_AT_DIAGNOSIS, domain=Diagnosis, range=Optional[str])

slots.Exposure_YEARS_SMOKED = Slot(uri=HTAN.YEARS_SMOKED, name="Exposure_YEARS_SMOKED", curie=HTAN.curie('YEARS_SMOKED'),
                   model_uri=HTAN.Exposure_YEARS_SMOKED, domain=Exposure, range=Optional[str])

slots.Exposure_PACK_YEARS_SMOKED = Slot(uri=HTAN.PACK_YEARS_SMOKED, name="Exposure_PACK_YEARS_SMOKED", curie=HTAN.curie('PACK_YEARS_SMOKED'),
                   model_uri=HTAN.Exposure_PACK_YEARS_SMOKED, domain=Exposure, range=Optional[str])

slots.Exposure_ENVIRONMENTAL_EXPOSURE_TYPE = Slot(uri=HTAN.ENVIRONMENTAL_EXPOSURE_TYPE, name="Exposure_ENVIRONMENTAL_EXPOSURE_TYPE", curie=HTAN.curie('ENVIRONMENTAL_EXPOSURE_TYPE'),
                   model_uri=HTAN.Exposure_ENVIRONMENTAL_EXPOSURE_TYPE, domain=Exposure, range=Optional[str])

slots.FollowUp_PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE = Slot(uri=HTAN.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, name="FollowUp_PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE", curie=HTAN.curie('PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE'),
                   model_uri=HTAN.FollowUp_PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE, domain=FollowUp, range=Optional[str])

slots.FollowUp_PROGRESSION_OR_RECURRENCE_TYPE = Slot(uri=HTAN.PROGRESSION_OR_RECURRENCE_TYPE, name="FollowUp_PROGRESSION_OR_RECURRENCE_TYPE", curie=HTAN.curie('PROGRESSION_OR_RECURRENCE_TYPE'),
                   model_uri=HTAN.FollowUp_PROGRESSION_OR_RECURRENCE_TYPE, domain=FollowUp, range=Optional[str])

slots.FollowUp_EVIDENCE_OF_RECURRENCE_TYPE = Slot(uri=HTAN.EVIDENCE_OF_RECURRENCE_TYPE, name="FollowUp_EVIDENCE_OF_RECURRENCE_TYPE", curie=HTAN.curie('EVIDENCE_OF_RECURRENCE_TYPE'),
                   model_uri=HTAN.FollowUp_EVIDENCE_OF_RECURRENCE_TYPE, domain=FollowUp, range=Optional[str])

slots.FollowUp_AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE = Slot(uri=HTAN.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, name="FollowUp_AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE", curie=HTAN.curie('AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE'),
                   model_uri=HTAN.FollowUp_AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE, domain=FollowUp, range=Optional[str])

slots.MolecularTest_AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP = Slot(uri=HTAN.AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, name="MolecularTest_AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP", curie=HTAN.curie('AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP'),
                   model_uri=HTAN.MolecularTest_AGE_IN_DAYS_AT_MOLECULAR_TEST_STOP, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_AA_CHANGE = Slot(uri=HTAN.AA_CHANGE, name="MolecularTest_AA_CHANGE", curie=HTAN.curie('AA_CHANGE'),
                   model_uri=HTAN.MolecularTest_AA_CHANGE, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_COPY_NUMBER = Slot(uri=HTAN.COPY_NUMBER, name="MolecularTest_COPY_NUMBER", curie=HTAN.curie('COPY_NUMBER'),
                   model_uri=HTAN.MolecularTest_COPY_NUMBER, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_EXON = Slot(uri=HTAN.EXON, name="MolecularTest_EXON", curie=HTAN.curie('EXON'),
                   model_uri=HTAN.MolecularTest_EXON, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_MOLECULAR_CONSEQUENCE = Slot(uri=HTAN.MOLECULAR_CONSEQUENCE, name="MolecularTest_MOLECULAR_CONSEQUENCE", curie=HTAN.curie('MOLECULAR_CONSEQUENCE'),
                   model_uri=HTAN.MolecularTest_MOLECULAR_CONSEQUENCE, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_PATHOGENICITY = Slot(uri=HTAN.PATHOGENICITY, name="MolecularTest_PATHOGENICITY", curie=HTAN.curie('PATHOGENICITY'),
                   model_uri=HTAN.MolecularTest_PATHOGENICITY, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_TEST_ANALYTE_TYPE = Slot(uri=HTAN.TEST_ANALYTE_TYPE, name="MolecularTest_TEST_ANALYTE_TYPE", curie=HTAN.curie('TEST_ANALYTE_TYPE'),
                   model_uri=HTAN.MolecularTest_TEST_ANALYTE_TYPE, domain=MolecularTest, range=Optional[str])

slots.MolecularTest_TEST_UNITS = Slot(uri=HTAN.TEST_UNITS, name="MolecularTest_TEST_UNITS", curie=HTAN.curie('TEST_UNITS'),
                   model_uri=HTAN.MolecularTest_TEST_UNITS, domain=MolecularTest, range=Optional[str])

slots.Therapy_THERAPY_ANATOMIC_SITE_UBERON_CODE = Slot(uri=HTAN.THERAPY_ANATOMIC_SITE_UBERON_CODE, name="Therapy_THERAPY_ANATOMIC_SITE_UBERON_CODE", curie=HTAN.curie('THERAPY_ANATOMIC_SITE_UBERON_CODE'),
                   model_uri=HTAN.Therapy_THERAPY_ANATOMIC_SITE_UBERON_CODE, domain=Therapy, range=Optional[str])

slots.Therapy_OFF_TREATMENT_REASON = Slot(uri=HTAN.OFF_TREATMENT_REASON, name="Therapy_OFF_TREATMENT_REASON", curie=HTAN.curie('OFF_TREATMENT_REASON'),
                   model_uri=HTAN.Therapy_OFF_TREATMENT_REASON, domain=Therapy, range=Optional[str])

slots.Therapy_REGIMEN_OR_LINE_OF_THERAPY = Slot(uri=HTAN.REGIMEN_OR_LINE_OF_THERAPY, name="Therapy_REGIMEN_OR_LINE_OF_THERAPY", curie=HTAN.curie('REGIMEN_OR_LINE_OF_THERAPY'),
                   model_uri=HTAN.Therapy_REGIMEN_OR_LINE_OF_THERAPY, domain=Therapy, range=Optional[str])

slots.Therapy_NUMBER_OF_CYCLES = Slot(uri=HTAN.NUMBER_OF_CYCLES, name="Therapy_NUMBER_OF_CYCLES", curie=HTAN.curie('NUMBER_OF_CYCLES'),
                   model_uri=HTAN.Therapy_NUMBER_OF_CYCLES, domain=Therapy, range=Optional[str])

slots.Therapy_RESPONSE = Slot(uri=HTAN.RESPONSE, name="Therapy_RESPONSE", curie=HTAN.curie('RESPONSE'),
                   model_uri=HTAN.Therapy_RESPONSE, domain=Therapy, range=Optional[str])

slots.VitalStatus_AGE_IN_DAYS_AT_DEATH = Slot(uri=HTAN.AGE_IN_DAYS_AT_DEATH, name="VitalStatus_AGE_IN_DAYS_AT_DEATH", curie=HTAN.curie('AGE_IN_DAYS_AT_DEATH'),
                   model_uri=HTAN.VitalStatus_AGE_IN_DAYS_AT_DEATH, domain=VitalStatus, range=Optional[str])

slots.VitalStatus_CAUSE_OF_DEATH = Slot(uri=HTAN.CAUSE_OF_DEATH, name="VitalStatus_CAUSE_OF_DEATH", curie=HTAN.curie('CAUSE_OF_DEATH'),
                   model_uri=HTAN.VitalStatus_CAUSE_OF_DEATH, domain=VitalStatus, range=Optional[str])

slots.VitalStatus_CAUSE_OF_DEATH_SOURCE = Slot(uri=HTAN.CAUSE_OF_DEATH_SOURCE, name="VitalStatus_CAUSE_OF_DEATH_SOURCE", curie=HTAN.curie('CAUSE_OF_DEATH_SOURCE'),
                   model_uri=HTAN.VitalStatus_CAUSE_OF_DEATH_SOURCE, domain=VitalStatus, range=Optional[str])