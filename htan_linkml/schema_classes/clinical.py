# Auto generated from clinical_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-04-17T10:58:03
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

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

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
class ParticipantParticipantId(extended_str):
    pass


@dataclass(repr=False)
class Demographics(YAMLRoot):
    """
    Demographic information about the participant
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["Demographics"]
    class_class_curie: ClassVar[str] = "htan:Demographics"
    class_name: ClassVar[str] = "Demographics"
    class_model_uri: ClassVar[URIRef] = HTAN.Demographics

    sex: Union[str, "SexEnum"] = None
    gender: Union[str, "GenderEnum"] = None
    race: Union[str, "RaceEnum"] = None
    ethnicity: Union[str, "EthnicityEnum"] = None
    age_at_enrollment_days: int = None
    vital_status: Union[str, "VitalStatusEnum"] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.sex):
            self.MissingRequiredField("sex")
        if not isinstance(self.sex, SexEnum):
            self.sex = SexEnum(self.sex)

        if self._is_empty(self.gender):
            self.MissingRequiredField("gender")
        if not isinstance(self.gender, GenderEnum):
            self.gender = GenderEnum(self.gender)

        if self._is_empty(self.race):
            self.MissingRequiredField("race")
        if not isinstance(self.race, RaceEnum):
            self.race = RaceEnum(self.race)

        if self._is_empty(self.ethnicity):
            self.MissingRequiredField("ethnicity")
        if not isinstance(self.ethnicity, EthnicityEnum):
            self.ethnicity = EthnicityEnum(self.ethnicity)

        if self._is_empty(self.age_at_enrollment_days):
            self.MissingRequiredField("age_at_enrollment_days")
        if not isinstance(self.age_at_enrollment_days, int):
            self.age_at_enrollment_days = int(self.age_at_enrollment_days)

        if self._is_empty(self.vital_status):
            self.MissingRequiredField("vital_status")
        if not isinstance(self.vital_status, VitalStatusEnum):
            self.vital_status = VitalStatusEnum(self.vital_status)

        super().__post_init__(**kwargs)


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

    participant_id: str = None
    demographics: Union[dict, Demographics] = None
    diagnosis: Union[dict, "Diagnosis"] = None
    exposures: Union[dict, "Exposure"] = None
    family_history: Union[dict, "FamilyHistory"] = None
    follow_ups: Optional[Union[Union[dict, "FollowUp"], List[Union[dict, "FollowUp"]]]] = empty_list()
    molecular_tests: Optional[Union[Union[dict, "MolecularTest"], List[Union[dict, "MolecularTest"]]]] = empty_list()
    therapies: Optional[Union[Union[dict, "Therapy"], List[Union[dict, "Therapy"]]]] = empty_list()
    publication_specific_data: Optional[Union[Union[dict, "PublicationSpecificData"], List[Union[dict, "PublicationSpecificData"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.participant_id):
            self.MissingRequiredField("participant_id")
        if not isinstance(self.participant_id, str):
            self.participant_id = str(self.participant_id)

        if self._is_empty(self.demographics):
            self.MissingRequiredField("demographics")
        if not isinstance(self.demographics, Demographics):
            self.demographics = Demographics(**as_dict(self.demographics))

        if self._is_empty(self.diagnosis):
            self.MissingRequiredField("diagnosis")
        if not isinstance(self.diagnosis, Diagnosis):
            self.diagnosis = Diagnosis(**as_dict(self.diagnosis))

        if self._is_empty(self.exposures):
            self.MissingRequiredField("exposures")
        if not isinstance(self.exposures, Exposure):
            self.exposures = Exposure(**as_dict(self.exposures))

        if self._is_empty(self.family_history):
            self.MissingRequiredField("family_history")
        if not isinstance(self.family_history, FamilyHistory):
            self.family_history = FamilyHistory(**as_dict(self.family_history))

        self._normalize_inlined_as_dict(slot_name="follow_ups", slot_type=FollowUp, key_name="age_at_followup_days", keyed=False)

        self._normalize_inlined_as_dict(slot_name="molecular_tests", slot_type=MolecularTest, key_name="age_at_test_start_days", keyed=False)

        self._normalize_inlined_as_dict(slot_name="therapies", slot_type=Therapy, key_name="initial_disease_status", keyed=False)

        self._normalize_inlined_as_dict(slot_name="publication_specific_data", slot_type=PublicationSpecificData, key_name="observation_key", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Diagnosis(YAMLRoot):
    """
    Information about the participant's diagnosis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["Diagnosis"]
    class_class_curie: ClassVar[str] = "htan:Diagnosis"
    class_name: ClassVar[str] = "Diagnosis"
    class_model_uri: ClassVar[URIRef] = HTAN.Diagnosis

    primary_diagnosis_ncit_id: str = None
    age_at_diagnosis_days: int = None
    tissue_or_organ_uberon_code: str = None
    tumor_grade: Union[str, "TumorGradeEnum"] = None
    tumor_stage: Union[str, "TumorStageEnum"] = None
    metastatic_stage: Union[str, "MetastaticStageEnum"] = None
    regional_lymph_node_stage: Union[str, "RegionalLymphNodeStageEnum"] = None
    ajcc_staging_system_edition: str = None
    metastasis_at_diagnosis: Union[bool, Bool] = None
    method_of_diagnosis: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.primary_diagnosis_ncit_id):
            self.MissingRequiredField("primary_diagnosis_ncit_id")
        if not isinstance(self.primary_diagnosis_ncit_id, str):
            self.primary_diagnosis_ncit_id = str(self.primary_diagnosis_ncit_id)

        if self._is_empty(self.age_at_diagnosis_days):
            self.MissingRequiredField("age_at_diagnosis_days")
        if not isinstance(self.age_at_diagnosis_days, int):
            self.age_at_diagnosis_days = int(self.age_at_diagnosis_days)

        if self._is_empty(self.tissue_or_organ_uberon_code):
            self.MissingRequiredField("tissue_or_organ_uberon_code")
        if not isinstance(self.tissue_or_organ_uberon_code, str):
            self.tissue_or_organ_uberon_code = str(self.tissue_or_organ_uberon_code)

        if self._is_empty(self.tumor_grade):
            self.MissingRequiredField("tumor_grade")
        if not isinstance(self.tumor_grade, TumorGradeEnum):
            self.tumor_grade = TumorGradeEnum(self.tumor_grade)

        if self._is_empty(self.tumor_stage):
            self.MissingRequiredField("tumor_stage")
        if not isinstance(self.tumor_stage, TumorStageEnum):
            self.tumor_stage = TumorStageEnum(self.tumor_stage)

        if self._is_empty(self.metastatic_stage):
            self.MissingRequiredField("metastatic_stage")
        if not isinstance(self.metastatic_stage, MetastaticStageEnum):
            self.metastatic_stage = MetastaticStageEnum(self.metastatic_stage)

        if self._is_empty(self.regional_lymph_node_stage):
            self.MissingRequiredField("regional_lymph_node_stage")
        if not isinstance(self.regional_lymph_node_stage, RegionalLymphNodeStageEnum):
            self.regional_lymph_node_stage = RegionalLymphNodeStageEnum(self.regional_lymph_node_stage)

        if self._is_empty(self.ajcc_staging_system_edition):
            self.MissingRequiredField("ajcc_staging_system_edition")
        if not isinstance(self.ajcc_staging_system_edition, str):
            self.ajcc_staging_system_edition = str(self.ajcc_staging_system_edition)

        if self._is_empty(self.metastasis_at_diagnosis):
            self.MissingRequiredField("metastasis_at_diagnosis")
        if not isinstance(self.metastasis_at_diagnosis, Bool):
            self.metastasis_at_diagnosis = Bool(self.metastasis_at_diagnosis)

        if self._is_empty(self.method_of_diagnosis):
            self.MissingRequiredField("method_of_diagnosis")
        if not isinstance(self.method_of_diagnosis, str):
            self.method_of_diagnosis = str(self.method_of_diagnosis)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Exposure(YAMLRoot):
    """
    Exposure history
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["Exposure"]
    class_class_curie: ClassVar[str] = "htan:Exposure"
    class_name: ClassVar[str] = "Exposure"
    class_model_uri: ClassVar[URIRef] = HTAN.Exposure

    smoking_history: Union[bool, Bool] = None
    alcohol_history: Union[bool, Bool] = None
    environmental_exposure: Union[bool, Bool] = None
    years_smoked: Optional[int] = None
    pack_years_smoked: Optional[float] = None
    environmental_exposure_type: Optional[Union[str, "EnvironmentalExposureTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.smoking_history):
            self.MissingRequiredField("smoking_history")
        if not isinstance(self.smoking_history, Bool):
            self.smoking_history = Bool(self.smoking_history)

        if self._is_empty(self.alcohol_history):
            self.MissingRequiredField("alcohol_history")
        if not isinstance(self.alcohol_history, Bool):
            self.alcohol_history = Bool(self.alcohol_history)

        if self._is_empty(self.environmental_exposure):
            self.MissingRequiredField("environmental_exposure")
        if not isinstance(self.environmental_exposure, Bool):
            self.environmental_exposure = Bool(self.environmental_exposure)

        if self.years_smoked is not None and not isinstance(self.years_smoked, int):
            self.years_smoked = int(self.years_smoked)

        if self.pack_years_smoked is not None and not isinstance(self.pack_years_smoked, float):
            self.pack_years_smoked = float(self.pack_years_smoked)

        if self.environmental_exposure_type is not None and not isinstance(self.environmental_exposure_type, EnvironmentalExposureTypeEnum):
            self.environmental_exposure_type = EnvironmentalExposureTypeEnum(self.environmental_exposure_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FamilyHistory(YAMLRoot):
    """
    Family history of cancer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["FamilyHistory"]
    class_class_curie: ClassVar[str] = "htan:FamilyHistory"
    class_name: ClassVar[str] = "FamilyHistory"
    class_model_uri: ClassVar[URIRef] = HTAN.FamilyHistory

    family_member_cancer_history: Union[bool, Bool] = None
    relatives_with_cancer_count: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.family_member_cancer_history):
            self.MissingRequiredField("family_member_cancer_history")
        if not isinstance(self.family_member_cancer_history, Bool):
            self.family_member_cancer_history = Bool(self.family_member_cancer_history)

        if self.relatives_with_cancer_count is not None and not isinstance(self.relatives_with_cancer_count, int):
            self.relatives_with_cancer_count = int(self.relatives_with_cancer_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FollowUp(YAMLRoot):
    """
    Follow-up observations
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["FollowUp"]
    class_class_curie: ClassVar[str] = "htan:FollowUp"
    class_name: ClassVar[str] = "FollowUp"
    class_model_uri: ClassVar[URIRef] = HTAN.FollowUp

    age_at_followup_days: int = None
    progression_or_recurrence: Union[bool, Bool] = None
    disease_response: Union[str, "DiseaseResponseEnum"] = None
    ecog_performance_status: Union[str, "ECOGPerformanceStatusEnum"] = None
    menopause_status: Union[str, "MenopauseStatusEnum"] = None
    progression_site_uberon_code: Optional[str] = None
    progression_type: Optional[Union[str, "ProgressionTypeEnum"]] = None
    evidence_of_recurrence_type: Optional[Union[str, "EvidenceOfRecurrenceTypeEnum"]] = None
    age_at_progression_days: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.age_at_followup_days):
            self.MissingRequiredField("age_at_followup_days")
        if not isinstance(self.age_at_followup_days, int):
            self.age_at_followup_days = int(self.age_at_followup_days)

        if self._is_empty(self.progression_or_recurrence):
            self.MissingRequiredField("progression_or_recurrence")
        if not isinstance(self.progression_or_recurrence, Bool):
            self.progression_or_recurrence = Bool(self.progression_or_recurrence)

        if self._is_empty(self.disease_response):
            self.MissingRequiredField("disease_response")
        if not isinstance(self.disease_response, DiseaseResponseEnum):
            self.disease_response = DiseaseResponseEnum(self.disease_response)

        if self._is_empty(self.ecog_performance_status):
            self.MissingRequiredField("ecog_performance_status")
        if not isinstance(self.ecog_performance_status, ECOGPerformanceStatusEnum):
            self.ecog_performance_status = ECOGPerformanceStatusEnum(self.ecog_performance_status)

        if self._is_empty(self.menopause_status):
            self.MissingRequiredField("menopause_status")
        if not isinstance(self.menopause_status, MenopauseStatusEnum):
            self.menopause_status = MenopauseStatusEnum(self.menopause_status)

        if self.progression_site_uberon_code is not None and not isinstance(self.progression_site_uberon_code, str):
            self.progression_site_uberon_code = str(self.progression_site_uberon_code)

        if self.progression_type is not None and not isinstance(self.progression_type, ProgressionTypeEnum):
            self.progression_type = ProgressionTypeEnum(self.progression_type)

        if self.evidence_of_recurrence_type is not None and not isinstance(self.evidence_of_recurrence_type, EvidenceOfRecurrenceTypeEnum):
            self.evidence_of_recurrence_type = EvidenceOfRecurrenceTypeEnum(self.evidence_of_recurrence_type)

        if self.age_at_progression_days is not None and not isinstance(self.age_at_progression_days, int):
            self.age_at_progression_days = int(self.age_at_progression_days)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularTest(YAMLRoot):
    """
    Molecular test results
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MolecularTest"]
    class_class_curie: ClassVar[str] = "htan:MolecularTest"
    class_name: ClassVar[str] = "MolecularTest"
    class_model_uri: ClassVar[URIRef] = HTAN.MolecularTest

    age_at_test_start_days: int = None
    gene_symbol: str = None
    molecular_analysis_method: Union[str, "MolecularAnalysisMethodEnum"] = None
    molecular_analysis_result: str = None
    clinical_biospecimen_type: Union[str, "ClinicalBiospecimenTypeEnum"] = None
    timepoint_label: Optional[str] = None
    age_at_test_stop_days: Optional[int] = None
    amino_acid_change: Optional[str] = None
    copy_number: Optional[int] = None
    exon: Optional[str] = None
    molecular_consequence: Optional[str] = None
    pathogenicity: Optional[str] = None
    test_analyte_type: Optional[Union[str, "TestAnalyteTypeEnum"]] = None
    test_units: Optional[str] = None
    test_result: Optional[str] = None
    variant_origin: Optional[Union[str, "VariantOriginEnum"]] = None
    variant_type: Optional[Union[str, "VariantTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.age_at_test_start_days):
            self.MissingRequiredField("age_at_test_start_days")
        if not isinstance(self.age_at_test_start_days, int):
            self.age_at_test_start_days = int(self.age_at_test_start_days)

        if self._is_empty(self.gene_symbol):
            self.MissingRequiredField("gene_symbol")
        if not isinstance(self.gene_symbol, str):
            self.gene_symbol = str(self.gene_symbol)

        if self._is_empty(self.molecular_analysis_method):
            self.MissingRequiredField("molecular_analysis_method")
        if not isinstance(self.molecular_analysis_method, MolecularAnalysisMethodEnum):
            self.molecular_analysis_method = MolecularAnalysisMethodEnum(self.molecular_analysis_method)

        if self._is_empty(self.molecular_analysis_result):
            self.MissingRequiredField("molecular_analysis_result")
        if not isinstance(self.molecular_analysis_result, str):
            self.molecular_analysis_result = str(self.molecular_analysis_result)

        if self._is_empty(self.clinical_biospecimen_type):
            self.MissingRequiredField("clinical_biospecimen_type")
        if not isinstance(self.clinical_biospecimen_type, ClinicalBiospecimenTypeEnum):
            self.clinical_biospecimen_type = ClinicalBiospecimenTypeEnum(self.clinical_biospecimen_type)

        if self.timepoint_label is not None and not isinstance(self.timepoint_label, str):
            self.timepoint_label = str(self.timepoint_label)

        if self.age_at_test_stop_days is not None and not isinstance(self.age_at_test_stop_days, int):
            self.age_at_test_stop_days = int(self.age_at_test_stop_days)

        if self.amino_acid_change is not None and not isinstance(self.amino_acid_change, str):
            self.amino_acid_change = str(self.amino_acid_change)

        if self.copy_number is not None and not isinstance(self.copy_number, int):
            self.copy_number = int(self.copy_number)

        if self.exon is not None and not isinstance(self.exon, str):
            self.exon = str(self.exon)

        if self.molecular_consequence is not None and not isinstance(self.molecular_consequence, str):
            self.molecular_consequence = str(self.molecular_consequence)

        if self.pathogenicity is not None and not isinstance(self.pathogenicity, str):
            self.pathogenicity = str(self.pathogenicity)

        if self.test_analyte_type is not None and not isinstance(self.test_analyte_type, TestAnalyteTypeEnum):
            self.test_analyte_type = TestAnalyteTypeEnum(self.test_analyte_type)

        if self.test_units is not None and not isinstance(self.test_units, str):
            self.test_units = str(self.test_units)

        if self.test_result is not None and not isinstance(self.test_result, str):
            self.test_result = str(self.test_result)

        if self.variant_origin is not None and not isinstance(self.variant_origin, VariantOriginEnum):
            self.variant_origin = VariantOriginEnum(self.variant_origin)

        if self.variant_type is not None and not isinstance(self.variant_type, VariantTypeEnum):
            self.variant_type = VariantTypeEnum(self.variant_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Therapy(YAMLRoot):
    """
    Treatment information
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["Therapy"]
    class_class_curie: ClassVar[str] = "htan:Therapy"
    class_name: ClassVar[str] = "Therapy"
    class_model_uri: ClassVar[URIRef] = HTAN.Therapy

    initial_disease_status: str = None
    treatment_intent_type: Union[str, "TreatmentIntentTypeEnum"] = None
    treatment_type: Union[str, "TreatmentTypeEnum"] = None
    pharmacotherapy_type: Union[str, "PharmacotherapyTypeEnum"] = None
    therapeutic_agents: str = None
    age_at_treatment_start_days: int = None
    age_at_treatment_end_days: int = None
    off_treatment_reason: Union[str, "OffTreatmentReasonEnum"] = None
    regimen_or_line_of_therapy: str = None
    number_of_cycles: int = None
    response: Union[str, "DiseaseResponseEnum"] = None
    therapy_site_uberon_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.initial_disease_status):
            self.MissingRequiredField("initial_disease_status")
        if not isinstance(self.initial_disease_status, str):
            self.initial_disease_status = str(self.initial_disease_status)

        if self._is_empty(self.treatment_intent_type):
            self.MissingRequiredField("treatment_intent_type")
        if not isinstance(self.treatment_intent_type, TreatmentIntentTypeEnum):
            self.treatment_intent_type = TreatmentIntentTypeEnum(self.treatment_intent_type)

        if self._is_empty(self.treatment_type):
            self.MissingRequiredField("treatment_type")
        if not isinstance(self.treatment_type, TreatmentTypeEnum):
            self.treatment_type = TreatmentTypeEnum(self.treatment_type)

        if self._is_empty(self.pharmacotherapy_type):
            self.MissingRequiredField("pharmacotherapy_type")
        if not isinstance(self.pharmacotherapy_type, PharmacotherapyTypeEnum):
            self.pharmacotherapy_type = PharmacotherapyTypeEnum(self.pharmacotherapy_type)

        if self._is_empty(self.therapeutic_agents):
            self.MissingRequiredField("therapeutic_agents")
        if not isinstance(self.therapeutic_agents, str):
            self.therapeutic_agents = str(self.therapeutic_agents)

        if self._is_empty(self.age_at_treatment_start_days):
            self.MissingRequiredField("age_at_treatment_start_days")
        if not isinstance(self.age_at_treatment_start_days, int):
            self.age_at_treatment_start_days = int(self.age_at_treatment_start_days)

        if self._is_empty(self.age_at_treatment_end_days):
            self.MissingRequiredField("age_at_treatment_end_days")
        if not isinstance(self.age_at_treatment_end_days, int):
            self.age_at_treatment_end_days = int(self.age_at_treatment_end_days)

        if self._is_empty(self.off_treatment_reason):
            self.MissingRequiredField("off_treatment_reason")
        if not isinstance(self.off_treatment_reason, OffTreatmentReasonEnum):
            self.off_treatment_reason = OffTreatmentReasonEnum(self.off_treatment_reason)

        if self._is_empty(self.regimen_or_line_of_therapy):
            self.MissingRequiredField("regimen_or_line_of_therapy")
        if not isinstance(self.regimen_or_line_of_therapy, str):
            self.regimen_or_line_of_therapy = str(self.regimen_or_line_of_therapy)

        if self._is_empty(self.number_of_cycles):
            self.MissingRequiredField("number_of_cycles")
        if not isinstance(self.number_of_cycles, int):
            self.number_of_cycles = int(self.number_of_cycles)

        if self._is_empty(self.response):
            self.MissingRequiredField("response")
        if not isinstance(self.response, DiseaseResponseEnum):
            self.response = DiseaseResponseEnum(self.response)

        if self.therapy_site_uberon_code is not None and not isinstance(self.therapy_site_uberon_code, str):
            self.therapy_site_uberon_code = str(self.therapy_site_uberon_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PublicationSpecificData(YAMLRoot):
    """
    Publication-specific clinical data observations (Tier 2)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["PublicationSpecificData"]
    class_class_curie: ClassVar[str] = "htan:PublicationSpecificData"
    class_name: ClassVar[str] = "PublicationSpecificData"
    class_model_uri: ClassVar[URIRef] = HTAN.PublicationSpecificData

    observation_key: str = None
    observation_value: str = None
    observation_type: Optional[str] = None
    observation_source: Optional[str] = None
    observation_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.observation_key):
            self.MissingRequiredField("observation_key")
        if not isinstance(self.observation_key, str):
            self.observation_key = str(self.observation_key)

        if self._is_empty(self.observation_value):
            self.MissingRequiredField("observation_value")
        if not isinstance(self.observation_value, str):
            self.observation_value = str(self.observation_value)

        if self.observation_type is not None and not isinstance(self.observation_type, str):
            self.observation_type = str(self.observation_type)

        if self.observation_source is not None and not isinstance(self.observation_source, str):
            self.observation_source = str(self.observation_source)

        if self.observation_date is not None and not isinstance(self.observation_date, str):
            self.observation_date = str(self.observation_date)

        super().__post_init__(**kwargs)


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
class TumorGradeEnum(EnumDefinitionImpl):

    G1 = PermissibleValue(text="G1")
    G2 = PermissibleValue(text="G2")
    G3 = PermissibleValue(text="G3")
    G4 = PermissibleValue(text="G4")
    GX = PermissibleValue(text="GX")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="TumorGradeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class TumorStageEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="TumorStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Stage 0",
            PermissibleValue(text="Stage 0"))
        setattr(cls, "Stage I",
            PermissibleValue(text="Stage I"))
        setattr(cls, "Stage II",
            PermissibleValue(text="Stage II"))
        setattr(cls, "Stage III",
            PermissibleValue(text="Stage III"))
        setattr(cls, "Stage IV",
            PermissibleValue(text="Stage IV"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class MetastaticStageEnum(EnumDefinitionImpl):

    M0 = PermissibleValue(text="M0")
    M1 = PermissibleValue(text="M1")
    MX = PermissibleValue(text="MX")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="MetastaticStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class RegionalLymphNodeStageEnum(EnumDefinitionImpl):

    N0 = PermissibleValue(text="N0")
    N1 = PermissibleValue(text="N1")
    N2 = PermissibleValue(text="N2")
    N3 = PermissibleValue(text="N3")
    NX = PermissibleValue(text="NX")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="RegionalLymphNodeStageEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class AJCCStagingSystemEditionEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="AJCCStagingSystemEditionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "7th Edition",
            PermissibleValue(text="7th Edition"))
        setattr(cls, "8th Edition",
            PermissibleValue(text="8th Edition"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class DiseaseResponseEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="DiseaseResponseEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Complete Response",
            PermissibleValue(text="Complete Response"))
        setattr(cls, "Partial Response",
            PermissibleValue(text="Partial Response"))
        setattr(cls, "Stable Disease",
            PermissibleValue(text="Stable Disease"))
        setattr(cls, "Progressive Disease",
            PermissibleValue(text="Progressive Disease"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class ECOGPerformanceStatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ECOGPerformanceStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0",
            PermissibleValue(text="0"))
        setattr(cls, "1",
            PermissibleValue(text="1"))
        setattr(cls, "2",
            PermissibleValue(text="2"))
        setattr(cls, "3",
            PermissibleValue(text="3"))
        setattr(cls, "4",
            PermissibleValue(text="4"))
        setattr(cls, "5",
            PermissibleValue(text="5"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class MenopauseStatusEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="MenopauseStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Pre-Menopausal",
            PermissibleValue(text="Pre-Menopausal"))
        setattr(cls, "Post-Menopausal",
            PermissibleValue(text="Post-Menopausal"))
        setattr(cls, "Peri-Menopausal",
            PermissibleValue(text="Peri-Menopausal"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class TreatmentIntentTypeEnum(EnumDefinitionImpl):

    Curative = PermissibleValue(text="Curative")
    Palliative = PermissibleValue(text="Palliative")
    Prophylactic = PermissibleValue(text="Prophylactic")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="TreatmentIntentTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class TreatmentTypeEnum(EnumDefinitionImpl):

    Surgery = PermissibleValue(text="Surgery")
    Radiation = PermissibleValue(text="Radiation")
    Chemotherapy = PermissibleValue(text="Chemotherapy")
    Immunotherapy = PermissibleValue(text="Immunotherapy")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="TreatmentTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Targeted Therapy",
            PermissibleValue(text="Targeted Therapy"))
        setattr(cls, "Hormone Therapy",
            PermissibleValue(text="Hormone Therapy"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class PharmacotherapyTypeEnum(EnumDefinitionImpl):

    Chemotherapy = PermissibleValue(text="Chemotherapy")
    Immunotherapy = PermissibleValue(text="Immunotherapy")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="PharmacotherapyTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Targeted Therapy",
            PermissibleValue(text="Targeted Therapy"))
        setattr(cls, "Hormone Therapy",
            PermissibleValue(text="Hormone Therapy"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class MethodOfDiagnosisEnum(EnumDefinitionImpl):

    Biopsy = PermissibleValue(text="Biopsy")
    Imaging = PermissibleValue(text="Imaging")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="MethodOfDiagnosisEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Laboratory Test",
            PermissibleValue(text="Laboratory Test"))
        setattr(cls, "Physical Examination",
            PermissibleValue(text="Physical Examination"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class EnvironmentalExposureTypeEnum(EnumDefinitionImpl):

    Asbestos = PermissibleValue(text="Asbestos")
    Radiation = PermissibleValue(text="Radiation")
    Chemical = PermissibleValue(text="Chemical")
    Occupational = PermissibleValue(text="Occupational")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="EnvironmentalExposureTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class ProgressionTypeEnum(EnumDefinitionImpl):

    Local = PermissibleValue(text="Local")
    Regional = PermissibleValue(text="Regional")
    Distant = PermissibleValue(text="Distant")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ProgressionTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class EvidenceOfRecurrenceTypeEnum(EnumDefinitionImpl):

    Imaging = PermissibleValue(text="Imaging")
    Biopsy = PermissibleValue(text="Biopsy")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="EvidenceOfRecurrenceTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Laboratory Test",
            PermissibleValue(text="Laboratory Test"))
        setattr(cls, "Clinical Examination",
            PermissibleValue(text="Clinical Examination"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class MolecularAnalysisMethodEnum(EnumDefinitionImpl):

    Cytogenetics = PermissibleValue(text="Cytogenetics")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="MolecularAnalysisMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DNA Sequencing",
            PermissibleValue(text="DNA Sequencing"))
        setattr(cls, "RNA Sequencing",
            PermissibleValue(text="RNA Sequencing"))
        setattr(cls, "Protein Analysis",
            PermissibleValue(text="Protein Analysis"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class ClinicalBiospecimenTypeEnum(EnumDefinitionImpl):

    Blood = PermissibleValue(text="Blood")
    Tissue = PermissibleValue(text="Tissue")
    Urine = PermissibleValue(text="Urine")
    Saliva = PermissibleValue(text="Saliva")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="ClinicalBiospecimenTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class TestAnalyteTypeEnum(EnumDefinitionImpl):

    DNA = PermissibleValue(text="DNA")
    RNA = PermissibleValue(text="RNA")
    Protein = PermissibleValue(text="Protein")
    Metabolite = PermissibleValue(text="Metabolite")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="TestAnalyteTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class VariantOriginEnum(EnumDefinitionImpl):

    Germline = PermissibleValue(text="Germline")
    Somatic = PermissibleValue(text="Somatic")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="VariantOriginEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class VariantTypeEnum(EnumDefinitionImpl):

    SNV = PermissibleValue(text="SNV")
    Indel = PermissibleValue(text="Indel")
    CNV = PermissibleValue(text="CNV")
    Fusion = PermissibleValue(text="Fusion")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="VariantTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

class OffTreatmentReasonEnum(EnumDefinitionImpl):

    Completed = PermissibleValue(text="Completed")
    Toxicity = PermissibleValue(text="Toxicity")
    Unknown = PermissibleValue(text="Unknown")

    _defn = EnumDefinition(
        name="OffTreatmentReasonEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Disease Progression",
            PermissibleValue(text="Disease Progression"))
        setattr(cls, "Patient Decision",
            PermissibleValue(text="Patient Decision"))
        setattr(cls, "Not Reported",
            PermissibleValue(text="Not Reported"))

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

slots.caDSR_id = Slot(uri=HTAN.caDSR_id, name="caDSR_id", curie=HTAN.curie('caDSR_id'),
                   model_uri=HTAN.caDSR_id, domain=None, range=Optional[str])

slots.demographics__sex = Slot(uri=HTAN.sex, name="demographics__sex", curie=HTAN.curie('sex'),
                   model_uri=HTAN.demographics__sex, domain=None, range=Union[str, "SexEnum"])

slots.demographics__gender = Slot(uri=HTAN.gender, name="demographics__gender", curie=HTAN.curie('gender'),
                   model_uri=HTAN.demographics__gender, domain=None, range=Union[str, "GenderEnum"])

slots.demographics__race = Slot(uri=HTAN.race, name="demographics__race", curie=HTAN.curie('race'),
                   model_uri=HTAN.demographics__race, domain=None, range=Union[str, "RaceEnum"])

slots.demographics__ethnicity = Slot(uri=HTAN.ethnicity, name="demographics__ethnicity", curie=HTAN.curie('ethnicity'),
                   model_uri=HTAN.demographics__ethnicity, domain=None, range=Union[str, "EthnicityEnum"])

slots.demographics__age_at_enrollment_days = Slot(uri=HTAN.age_at_enrollment_days, name="demographics__age_at_enrollment_days", curie=HTAN.curie('age_at_enrollment_days'),
                   model_uri=HTAN.demographics__age_at_enrollment_days, domain=None, range=int)

slots.demographics__vital_status = Slot(uri=HTAN.vital_status, name="demographics__vital_status", curie=HTAN.curie('vital_status'),
                   model_uri=HTAN.demographics__vital_status, domain=None, range=Union[str, "VitalStatusEnum"])

slots.clinicalData__participant_id = Slot(uri=HTAN.participant_id, name="clinicalData__participant_id", curie=HTAN.curie('participant_id'),
                   model_uri=HTAN.clinicalData__participant_id, domain=None, range=str)

slots.clinicalData__demographics = Slot(uri=HTAN.demographics, name="clinicalData__demographics", curie=HTAN.curie('demographics'),
                   model_uri=HTAN.clinicalData__demographics, domain=None, range=Union[dict, Demographics])

slots.clinicalData__diagnosis = Slot(uri=HTAN.diagnosis, name="clinicalData__diagnosis", curie=HTAN.curie('diagnosis'),
                   model_uri=HTAN.clinicalData__diagnosis, domain=None, range=Union[dict, Diagnosis])

slots.clinicalData__exposures = Slot(uri=HTAN.exposures, name="clinicalData__exposures", curie=HTAN.curie('exposures'),
                   model_uri=HTAN.clinicalData__exposures, domain=None, range=Union[dict, Exposure])

slots.clinicalData__family_history = Slot(uri=HTAN.family_history, name="clinicalData__family_history", curie=HTAN.curie('family_history'),
                   model_uri=HTAN.clinicalData__family_history, domain=None, range=Union[dict, FamilyHistory])

slots.clinicalData__follow_ups = Slot(uri=HTAN.follow_ups, name="clinicalData__follow_ups", curie=HTAN.curie('follow_ups'),
                   model_uri=HTAN.clinicalData__follow_ups, domain=None, range=Optional[Union[Union[dict, FollowUp], List[Union[dict, FollowUp]]]])

slots.clinicalData__molecular_tests = Slot(uri=HTAN.molecular_tests, name="clinicalData__molecular_tests", curie=HTAN.curie('molecular_tests'),
                   model_uri=HTAN.clinicalData__molecular_tests, domain=None, range=Optional[Union[Union[dict, MolecularTest], List[Union[dict, MolecularTest]]]])

slots.clinicalData__therapies = Slot(uri=HTAN.therapies, name="clinicalData__therapies", curie=HTAN.curie('therapies'),
                   model_uri=HTAN.clinicalData__therapies, domain=None, range=Optional[Union[Union[dict, Therapy], List[Union[dict, Therapy]]]])

slots.clinicalData__publication_specific_data = Slot(uri=HTAN.publication_specific_data, name="clinicalData__publication_specific_data", curie=HTAN.curie('publication_specific_data'),
                   model_uri=HTAN.clinicalData__publication_specific_data, domain=None, range=Optional[Union[Union[dict, PublicationSpecificData], List[Union[dict, PublicationSpecificData]]]])

slots.diagnosis__primary_diagnosis_ncit_id = Slot(uri=HTAN.primary_diagnosis_ncit_id, name="diagnosis__primary_diagnosis_ncit_id", curie=HTAN.curie('primary_diagnosis_ncit_id'),
                   model_uri=HTAN.diagnosis__primary_diagnosis_ncit_id, domain=None, range=str)

slots.diagnosis__age_at_diagnosis_days = Slot(uri=HTAN.age_at_diagnosis_days, name="diagnosis__age_at_diagnosis_days", curie=HTAN.curie('age_at_diagnosis_days'),
                   model_uri=HTAN.diagnosis__age_at_diagnosis_days, domain=None, range=int)

slots.diagnosis__tissue_or_organ_uberon_code = Slot(uri=HTAN.tissue_or_organ_uberon_code, name="diagnosis__tissue_or_organ_uberon_code", curie=HTAN.curie('tissue_or_organ_uberon_code'),
                   model_uri=HTAN.diagnosis__tissue_or_organ_uberon_code, domain=None, range=str)

slots.diagnosis__tumor_grade = Slot(uri=HTAN.tumor_grade, name="diagnosis__tumor_grade", curie=HTAN.curie('tumor_grade'),
                   model_uri=HTAN.diagnosis__tumor_grade, domain=None, range=Union[str, "TumorGradeEnum"])

slots.diagnosis__tumor_stage = Slot(uri=HTAN.tumor_stage, name="diagnosis__tumor_stage", curie=HTAN.curie('tumor_stage'),
                   model_uri=HTAN.diagnosis__tumor_stage, domain=None, range=Union[str, "TumorStageEnum"])

slots.diagnosis__metastatic_stage = Slot(uri=HTAN.metastatic_stage, name="diagnosis__metastatic_stage", curie=HTAN.curie('metastatic_stage'),
                   model_uri=HTAN.diagnosis__metastatic_stage, domain=None, range=Union[str, "MetastaticStageEnum"])

slots.diagnosis__regional_lymph_node_stage = Slot(uri=HTAN.regional_lymph_node_stage, name="diagnosis__regional_lymph_node_stage", curie=HTAN.curie('regional_lymph_node_stage'),
                   model_uri=HTAN.diagnosis__regional_lymph_node_stage, domain=None, range=Union[str, "RegionalLymphNodeStageEnum"])

slots.diagnosis__ajcc_staging_system_edition = Slot(uri=HTAN.ajcc_staging_system_edition, name="diagnosis__ajcc_staging_system_edition", curie=HTAN.curie('ajcc_staging_system_edition'),
                   model_uri=HTAN.diagnosis__ajcc_staging_system_edition, domain=None, range=str)

slots.diagnosis__metastasis_at_diagnosis = Slot(uri=HTAN.metastasis_at_diagnosis, name="diagnosis__metastasis_at_diagnosis", curie=HTAN.curie('metastasis_at_diagnosis'),
                   model_uri=HTAN.diagnosis__metastasis_at_diagnosis, domain=None, range=Union[bool, Bool])

slots.diagnosis__method_of_diagnosis = Slot(uri=HTAN.method_of_diagnosis, name="diagnosis__method_of_diagnosis", curie=HTAN.curie('method_of_diagnosis'),
                   model_uri=HTAN.diagnosis__method_of_diagnosis, domain=None, range=str)

slots.exposure__smoking_history = Slot(uri=HTAN.smoking_history, name="exposure__smoking_history", curie=HTAN.curie('smoking_history'),
                   model_uri=HTAN.exposure__smoking_history, domain=None, range=Union[bool, Bool])

slots.exposure__years_smoked = Slot(uri=HTAN.years_smoked, name="exposure__years_smoked", curie=HTAN.curie('years_smoked'),
                   model_uri=HTAN.exposure__years_smoked, domain=None, range=Optional[int])

slots.exposure__pack_years_smoked = Slot(uri=HTAN.pack_years_smoked, name="exposure__pack_years_smoked", curie=HTAN.curie('pack_years_smoked'),
                   model_uri=HTAN.exposure__pack_years_smoked, domain=None, range=Optional[float])

slots.exposure__alcohol_history = Slot(uri=HTAN.alcohol_history, name="exposure__alcohol_history", curie=HTAN.curie('alcohol_history'),
                   model_uri=HTAN.exposure__alcohol_history, domain=None, range=Union[bool, Bool])

slots.exposure__environmental_exposure = Slot(uri=HTAN.environmental_exposure, name="exposure__environmental_exposure", curie=HTAN.curie('environmental_exposure'),
                   model_uri=HTAN.exposure__environmental_exposure, domain=None, range=Union[bool, Bool])

slots.exposure__environmental_exposure_type = Slot(uri=HTAN.environmental_exposure_type, name="exposure__environmental_exposure_type", curie=HTAN.curie('environmental_exposure_type'),
                   model_uri=HTAN.exposure__environmental_exposure_type, domain=None, range=Optional[Union[str, "EnvironmentalExposureTypeEnum"]])

slots.familyHistory__family_member_cancer_history = Slot(uri=HTAN.family_member_cancer_history, name="familyHistory__family_member_cancer_history", curie=HTAN.curie('family_member_cancer_history'),
                   model_uri=HTAN.familyHistory__family_member_cancer_history, domain=None, range=Union[bool, Bool])

slots.familyHistory__relatives_with_cancer_count = Slot(uri=HTAN.relatives_with_cancer_count, name="familyHistory__relatives_with_cancer_count", curie=HTAN.curie('relatives_with_cancer_count'),
                   model_uri=HTAN.familyHistory__relatives_with_cancer_count, domain=None, range=Optional[int])

slots.followUp__age_at_followup_days = Slot(uri=HTAN.age_at_followup_days, name="followUp__age_at_followup_days", curie=HTAN.curie('age_at_followup_days'),
                   model_uri=HTAN.followUp__age_at_followup_days, domain=None, range=int)

slots.followUp__progression_or_recurrence = Slot(uri=HTAN.progression_or_recurrence, name="followUp__progression_or_recurrence", curie=HTAN.curie('progression_or_recurrence'),
                   model_uri=HTAN.followUp__progression_or_recurrence, domain=None, range=Union[bool, Bool])

slots.followUp__progression_site_uberon_code = Slot(uri=HTAN.progression_site_uberon_code, name="followUp__progression_site_uberon_code", curie=HTAN.curie('progression_site_uberon_code'),
                   model_uri=HTAN.followUp__progression_site_uberon_code, domain=None, range=Optional[str])

slots.followUp__progression_type = Slot(uri=HTAN.progression_type, name="followUp__progression_type", curie=HTAN.curie('progression_type'),
                   model_uri=HTAN.followUp__progression_type, domain=None, range=Optional[Union[str, "ProgressionTypeEnum"]])

slots.followUp__evidence_of_recurrence_type = Slot(uri=HTAN.evidence_of_recurrence_type, name="followUp__evidence_of_recurrence_type", curie=HTAN.curie('evidence_of_recurrence_type'),
                   model_uri=HTAN.followUp__evidence_of_recurrence_type, domain=None, range=Optional[Union[str, "EvidenceOfRecurrenceTypeEnum"]])

slots.followUp__age_at_progression_days = Slot(uri=HTAN.age_at_progression_days, name="followUp__age_at_progression_days", curie=HTAN.curie('age_at_progression_days'),
                   model_uri=HTAN.followUp__age_at_progression_days, domain=None, range=Optional[int])

slots.followUp__disease_response = Slot(uri=HTAN.disease_response, name="followUp__disease_response", curie=HTAN.curie('disease_response'),
                   model_uri=HTAN.followUp__disease_response, domain=None, range=Union[str, "DiseaseResponseEnum"])

slots.followUp__ecog_performance_status = Slot(uri=HTAN.ecog_performance_status, name="followUp__ecog_performance_status", curie=HTAN.curie('ecog_performance_status'),
                   model_uri=HTAN.followUp__ecog_performance_status, domain=None, range=Union[str, "ECOGPerformanceStatusEnum"])

slots.followUp__menopause_status = Slot(uri=HTAN.menopause_status, name="followUp__menopause_status", curie=HTAN.curie('menopause_status'),
                   model_uri=HTAN.followUp__menopause_status, domain=None, range=Union[str, "MenopauseStatusEnum"])

slots.molecularTest__timepoint_label = Slot(uri=HTAN.timepoint_label, name="molecularTest__timepoint_label", curie=HTAN.curie('timepoint_label'),
                   model_uri=HTAN.molecularTest__timepoint_label, domain=None, range=Optional[str])

slots.molecularTest__age_at_test_start_days = Slot(uri=HTAN.age_at_test_start_days, name="molecularTest__age_at_test_start_days", curie=HTAN.curie('age_at_test_start_days'),
                   model_uri=HTAN.molecularTest__age_at_test_start_days, domain=None, range=int)

slots.molecularTest__age_at_test_stop_days = Slot(uri=HTAN.age_at_test_stop_days, name="molecularTest__age_at_test_stop_days", curie=HTAN.curie('age_at_test_stop_days'),
                   model_uri=HTAN.molecularTest__age_at_test_stop_days, domain=None, range=Optional[int])

slots.molecularTest__gene_symbol = Slot(uri=HTAN.gene_symbol, name="molecularTest__gene_symbol", curie=HTAN.curie('gene_symbol'),
                   model_uri=HTAN.molecularTest__gene_symbol, domain=None, range=str)

slots.molecularTest__molecular_analysis_method = Slot(uri=HTAN.molecular_analysis_method, name="molecularTest__molecular_analysis_method", curie=HTAN.curie('molecular_analysis_method'),
                   model_uri=HTAN.molecularTest__molecular_analysis_method, domain=None, range=Union[str, "MolecularAnalysisMethodEnum"])

slots.molecularTest__molecular_analysis_result = Slot(uri=HTAN.molecular_analysis_result, name="molecularTest__molecular_analysis_result", curie=HTAN.curie('molecular_analysis_result'),
                   model_uri=HTAN.molecularTest__molecular_analysis_result, domain=None, range=str)

slots.molecularTest__amino_acid_change = Slot(uri=HTAN.amino_acid_change, name="molecularTest__amino_acid_change", curie=HTAN.curie('amino_acid_change'),
                   model_uri=HTAN.molecularTest__amino_acid_change, domain=None, range=Optional[str])

slots.molecularTest__clinical_biospecimen_type = Slot(uri=HTAN.clinical_biospecimen_type, name="molecularTest__clinical_biospecimen_type", curie=HTAN.curie('clinical_biospecimen_type'),
                   model_uri=HTAN.molecularTest__clinical_biospecimen_type, domain=None, range=Union[str, "ClinicalBiospecimenTypeEnum"])

slots.molecularTest__copy_number = Slot(uri=HTAN.copy_number, name="molecularTest__copy_number", curie=HTAN.curie('copy_number'),
                   model_uri=HTAN.molecularTest__copy_number, domain=None, range=Optional[int])

slots.molecularTest__exon = Slot(uri=HTAN.exon, name="molecularTest__exon", curie=HTAN.curie('exon'),
                   model_uri=HTAN.molecularTest__exon, domain=None, range=Optional[str])

slots.molecularTest__molecular_consequence = Slot(uri=HTAN.molecular_consequence, name="molecularTest__molecular_consequence", curie=HTAN.curie('molecular_consequence'),
                   model_uri=HTAN.molecularTest__molecular_consequence, domain=None, range=Optional[str])

slots.molecularTest__pathogenicity = Slot(uri=HTAN.pathogenicity, name="molecularTest__pathogenicity", curie=HTAN.curie('pathogenicity'),
                   model_uri=HTAN.molecularTest__pathogenicity, domain=None, range=Optional[str])

slots.molecularTest__test_analyte_type = Slot(uri=HTAN.test_analyte_type, name="molecularTest__test_analyte_type", curie=HTAN.curie('test_analyte_type'),
                   model_uri=HTAN.molecularTest__test_analyte_type, domain=None, range=Optional[Union[str, "TestAnalyteTypeEnum"]])

slots.molecularTest__test_units = Slot(uri=HTAN.test_units, name="molecularTest__test_units", curie=HTAN.curie('test_units'),
                   model_uri=HTAN.molecularTest__test_units, domain=None, range=Optional[str])

slots.molecularTest__test_result = Slot(uri=HTAN.test_result, name="molecularTest__test_result", curie=HTAN.curie('test_result'),
                   model_uri=HTAN.molecularTest__test_result, domain=None, range=Optional[str])

slots.molecularTest__variant_origin = Slot(uri=HTAN.variant_origin, name="molecularTest__variant_origin", curie=HTAN.curie('variant_origin'),
                   model_uri=HTAN.molecularTest__variant_origin, domain=None, range=Optional[Union[str, "VariantOriginEnum"]])

slots.molecularTest__variant_type = Slot(uri=HTAN.variant_type, name="molecularTest__variant_type", curie=HTAN.curie('variant_type'),
                   model_uri=HTAN.molecularTest__variant_type, domain=None, range=Optional[Union[str, "VariantTypeEnum"]])

slots.therapy__initial_disease_status = Slot(uri=HTAN.initial_disease_status, name="therapy__initial_disease_status", curie=HTAN.curie('initial_disease_status'),
                   model_uri=HTAN.therapy__initial_disease_status, domain=None, range=str)

slots.therapy__treatment_intent_type = Slot(uri=HTAN.treatment_intent_type, name="therapy__treatment_intent_type", curie=HTAN.curie('treatment_intent_type'),
                   model_uri=HTAN.therapy__treatment_intent_type, domain=None, range=Union[str, "TreatmentIntentTypeEnum"])

slots.therapy__treatment_type = Slot(uri=HTAN.treatment_type, name="therapy__treatment_type", curie=HTAN.curie('treatment_type'),
                   model_uri=HTAN.therapy__treatment_type, domain=None, range=Union[str, "TreatmentTypeEnum"])

slots.therapy__pharmacotherapy_type = Slot(uri=HTAN.pharmacotherapy_type, name="therapy__pharmacotherapy_type", curie=HTAN.curie('pharmacotherapy_type'),
                   model_uri=HTAN.therapy__pharmacotherapy_type, domain=None, range=Union[str, "PharmacotherapyTypeEnum"])

slots.therapy__therapeutic_agents = Slot(uri=HTAN.therapeutic_agents, name="therapy__therapeutic_agents", curie=HTAN.curie('therapeutic_agents'),
                   model_uri=HTAN.therapy__therapeutic_agents, domain=None, range=str)

slots.therapy__therapy_site_uberon_code = Slot(uri=HTAN.therapy_site_uberon_code, name="therapy__therapy_site_uberon_code", curie=HTAN.curie('therapy_site_uberon_code'),
                   model_uri=HTAN.therapy__therapy_site_uberon_code, domain=None, range=Optional[str])

slots.therapy__age_at_treatment_start_days = Slot(uri=HTAN.age_at_treatment_start_days, name="therapy__age_at_treatment_start_days", curie=HTAN.curie('age_at_treatment_start_days'),
                   model_uri=HTAN.therapy__age_at_treatment_start_days, domain=None, range=int)

slots.therapy__age_at_treatment_end_days = Slot(uri=HTAN.age_at_treatment_end_days, name="therapy__age_at_treatment_end_days", curie=HTAN.curie('age_at_treatment_end_days'),
                   model_uri=HTAN.therapy__age_at_treatment_end_days, domain=None, range=int)

slots.therapy__off_treatment_reason = Slot(uri=HTAN.off_treatment_reason, name="therapy__off_treatment_reason", curie=HTAN.curie('off_treatment_reason'),
                   model_uri=HTAN.therapy__off_treatment_reason, domain=None, range=Union[str, "OffTreatmentReasonEnum"])

slots.therapy__regimen_or_line_of_therapy = Slot(uri=HTAN.regimen_or_line_of_therapy, name="therapy__regimen_or_line_of_therapy", curie=HTAN.curie('regimen_or_line_of_therapy'),
                   model_uri=HTAN.therapy__regimen_or_line_of_therapy, domain=None, range=str)

slots.therapy__number_of_cycles = Slot(uri=HTAN.number_of_cycles, name="therapy__number_of_cycles", curie=HTAN.curie('number_of_cycles'),
                   model_uri=HTAN.therapy__number_of_cycles, domain=None, range=int)

slots.therapy__response = Slot(uri=HTAN.response, name="therapy__response", curie=HTAN.curie('response'),
                   model_uri=HTAN.therapy__response, domain=None, range=Union[str, "DiseaseResponseEnum"])

slots.publicationSpecificData__observation_key = Slot(uri=HTAN.observation_key, name="publicationSpecificData__observation_key", curie=HTAN.curie('observation_key'),
                   model_uri=HTAN.publicationSpecificData__observation_key, domain=None, range=str)

slots.publicationSpecificData__observation_value = Slot(uri=HTAN.observation_value, name="publicationSpecificData__observation_value", curie=HTAN.curie('observation_value'),
                   model_uri=HTAN.publicationSpecificData__observation_value, domain=None, range=str)

slots.publicationSpecificData__observation_type = Slot(uri=HTAN.observation_type, name="publicationSpecificData__observation_type", curie=HTAN.curie('observation_type'),
                   model_uri=HTAN.publicationSpecificData__observation_type, domain=None, range=Optional[str])

slots.publicationSpecificData__observation_source = Slot(uri=HTAN.observation_source, name="publicationSpecificData__observation_source", curie=HTAN.curie('observation_source'),
                   model_uri=HTAN.publicationSpecificData__observation_source, domain=None, range=Optional[str])

slots.publicationSpecificData__observation_date = Slot(uri=HTAN.observation_date, name="publicationSpecificData__observation_date", curie=HTAN.curie('observation_date'),
                   model_uri=HTAN.publicationSpecificData__observation_date, domain=None, range=Optional[str])

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
