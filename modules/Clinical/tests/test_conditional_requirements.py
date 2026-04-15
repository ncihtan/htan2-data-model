import pytest
from pathlib import Path
import sys
import os
import yaml
from copy import deepcopy
from io import StringIO
from ruamel.yaml import YAML as RuamelYAML
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper
from htan_clinical.datamodel.clinical import ClinicalData

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

TEST_DATA_PATH = os.path.join(os.path.dirname(__file__), "test_conditional_requirements.yaml")


def _dump(data) -> str:
    """Serialize to YAML using ruamel.yaml with preserve_quotes, so that quoted
    strings like "Yes" round-trip correctly without being parsed as booleans."""
    ryaml = RuamelYAML()
    ryaml.preserve_quotes = True
    stream = StringIO()
    ryaml.dump(data, stream)
    return stream.getvalue()


@pytest.fixture(scope="class")
def test_data():
    """Load test data once for all tests, preserving original quoting style so
    that "Yes"/"No" values remain strings through the yaml dump/load round-trip."""
    ryaml = RuamelYAML()
    ryaml.preserve_quotes = True
    with open(TEST_DATA_PATH) as f:
        return ryaml.load(f)


def test_valid_clinical_data(test_data):
    """Test that valid clinical data can be loaded and validated"""
    clinical_data = yaml_loader.loads(_dump(test_data), target_class=ClinicalData)
    assert clinical_data is not None

    # Verify required fields in Demographics
    assert clinical_data.DEMOGRAPHICS.ETHNIC_GROUP is not None
    assert clinical_data.DEMOGRAPHICS.GENDER_IDENTITY is not None
    assert clinical_data.DEMOGRAPHICS.SEX is not None
    assert clinical_data.DEMOGRAPHICS.RACE is not None


def test_followup_conditional_requirements(test_data):
    """Test conditional requirements in follow-up data"""
    clinical_data = yaml_loader.loads(_dump(test_data), target_class=ClinicalData)

    # When PROGRESSION_OR_RECURRENCE is "Yes", certain fields should be required
    for followup in clinical_data.FOLLOW_UPS:
        if (
            hasattr(followup, "PROGRESSION_OR_RECURRENCE")
            and followup.PROGRESSION_OR_RECURRENCE == "Yes"
        ):
            assert (
                followup.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE is not None
            )
            assert followup.PROGRESSION_OR_RECURRENCE_TYPE is not None
            assert followup.EVIDENCE_OF_RECURRENCE_TYPE is not None
            assert followup.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE is not None


def test_family_history_conditional_requirements(test_data):
    """Test conditional requirements in family history data"""
    clinical_data = yaml_loader.loads(_dump(test_data), target_class=ClinicalData)

    # When FAMILY_MEMBER_CANCER_HISTORY is "Yes", RELATIVES_WITH_CANCER_HISTORY should be required
    if clinical_data.FAMILY_HISTORY.FAMILY_MEMBER_CANCER_HISTORY == "Yes":
        assert clinical_data.FAMILY_HISTORY.RELATIVES_WITH_CANCER_HISTORY is not None


def test_diagnosis_tumor_staged_conditional_requirements(test_data):
    """Test TUMOR_STAGED conditional requirements: staging fields required when TUMOR_STAGED is Yes."""
    clinical_data = yaml_loader.loads(_dump(test_data), target_class=ClinicalData)

    if hasattr(clinical_data, "DIAGNOSIS") and clinical_data.DIAGNOSIS is not None:
        diagnosis = clinical_data.DIAGNOSIS
        if getattr(diagnosis, "TUMOR_STAGED", None) == "Yes":
            assert diagnosis.CLINICAL_T_STAGE is not None
            assert diagnosis.CLINICAL_N_STAGE is not None
            assert diagnosis.CLINICAL_M_STAGE is not None
            assert diagnosis.AJCC_STAGING_SYSTEM_EDITION is not None


def test_ecog_score_performed_conditional_requirements(test_data):
    """Test ECOG_SCORE_PERFORMED conditional: ECOG status required when ECOG_SCORE_PERFORMED is Known."""
    clinical_data = yaml_loader.loads(_dump(test_data), target_class=ClinicalData)

    for followup in clinical_data.FOLLOW_UPS:
        if getattr(followup, "ECOG_SCORE_PERFORMED", None) == "Known":
            assert followup.ECOG_PERFORMANCE_STATUS is not None


def test_therapy_chemotherapy_conditional_requirements(test_data):
    """Test THERAPEUTIC_AGENTS and REGIMEN are required when TREATMENT_TYPE is Chemotherapy."""
    clinical_data = yaml_loader.loads(_dump(test_data), target_class=ClinicalData)

    for therapy in clinical_data.THERAPIES:
        treatment_types = getattr(therapy, "TREATMENT_TYPE", []) or []
        if "Chemotherapy" in treatment_types or "Concurrent Chemoradiation" in treatment_types:
            assert therapy.THERAPEUTIC_AGENTS is not None
            assert therapy.REGIMEN_OR_LINE_OF_THERAPY is not None


def test_invalid_data_missing_required_field(test_data):
    """Test that missing required fields raise appropriate errors"""
    invalid_data = deepcopy(test_data)
    del invalid_data["DEMOGRAPHICS"]["ETHNIC_GROUP"]

    with pytest.raises(ValueError) as excinfo:
        yaml_loader.loads(_dump(invalid_data), target_class=ClinicalData)

    assert "ETHNIC_GROUP must be supplied" in str(excinfo.value)


def test_invalid_enum_values(test_data):
    """Test that invalid enum values raise appropriate errors"""
    invalid_data = deepcopy(test_data)
    invalid_data["DEMOGRAPHICS"]["ETHNIC_GROUP"] = "Invalid Value"

    with pytest.raises(ValueError) as excinfo:
        yaml_loader.loads(_dump(invalid_data), target_class=ClinicalData)

    assert "Unknown EthnicGroupEnum enumeration code: Invalid Value" in str(
        excinfo.value
    )
