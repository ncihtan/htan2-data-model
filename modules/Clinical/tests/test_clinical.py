"""Clinical test."""

import os
import pytest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from htan_clinical.datamodel.clinical import ClinicalData


@pytest.fixture
def base_dir():
    """Base directory for tests."""
    return Path(__file__).parent.parent


@pytest.fixture
def schema_path(base_dir):
    """Schema path."""
    return base_dir / "domains" / "clinical.yaml"


@pytest.fixture
def schema_view(schema_path):
    """Schema view."""
    return SchemaView(str(schema_path))


@pytest.fixture
def test_data_dir(base_dir):
    """Test data directory."""
    return base_dir / "tests" / "test_data"


@pytest.fixture
def valid_files(test_data_dir):
    """Valid test files."""
    return glob.glob(str(test_data_dir / "valid" / "*.yaml"))


@pytest.fixture
def invalid_files(test_data_dir):
    """Invalid test files."""
    return glob.glob(str(test_data_dir / "invalid" / "*.yaml"))


def test_schema_loads(schema_view):
    """Test that the schema can be loaded."""
    assert schema_view is not None
    assert "ClinicalData" in schema_view.all_classes()


def test_valid_data(valid_files):
    """Test that all valid data files validate."""
    for file_path in valid_files:
        with open(file_path) as f:
            # This will validate during loading
            data = yaml_loader.load(f, target_class=ClinicalData)
        assert isinstance(data, ClinicalData)


def test_invalid_data(invalid_files):
    """Test that all invalid data files fail validation."""
    for file_path in invalid_files:
        with pytest.raises(ValueError):
            with open(file_path) as f:
                yaml_loader.load(f, target_class=ClinicalData)


def test_required_fields():
    """Test that missing required fields are caught."""
    test_data = {
        "HTAN_PARTICIPANT_ID": "HTA200_0000"
        # Missing required fields
    }
    with pytest.raises(ValueError):
        ClinicalData(**test_data)


def test_enum_values():
    """Test that invalid enum values are caught."""
    test_data = {
        "HTAN_PARTICIPANT_ID": "HTA200_0000",
        "DIAGNOSIS": {"HTAN_PARTICIPANT_ID": "HTA200_0000", "TUMOR_GRADE": "G5"},  # Invalid enum value
    }
    with pytest.raises(ValueError):
        ClinicalData(**test_data)


def test_data_types():
    """Test that invalid data types are caught."""
    test_data = {
        "HTAN_PARTICIPANT_ID": "HTA200_0000",
        "DIAGNOSIS": {"HTAN_PARTICIPANT_ID": "HTA200_0000", "AGE_AT_DIAGNOSIS_DAYS": "not_a_number"},  # Should be integer
    }
    with pytest.raises(ValueError):
        ClinicalData(**test_data)


def test_therapeutic_agents_not_required(schema_view):
    """Test that THERAPEUTIC_AGENTS is optional at base level (conditionally required via rules)."""
    therapy_class = schema_view.get_class("Therapy")
    assert therapy_class.attributes["THERAPEUTIC_AGENTS"].required is False


def test_tumor_staged_enum_exists(schema_view):
    """Test that TumorStagedEnum is present in the schema."""
    assert "TumorStagedEnum" in schema_view.all_enums()


def test_tumor_staged_slot_required(schema_view):
    """Test that TUMOR_STAGED is required in the Diagnosis class."""
    diagnosis_class = schema_view.get_class("Diagnosis")
    assert "TUMOR_STAGED" in diagnosis_class.attributes
    assert diagnosis_class.attributes["TUMOR_STAGED"].required is True


def test_ajcc_staging_slots_not_required(schema_view):
    """Test that AJCC staging slots are optional at base level (conditionally required via rules)."""
    diagnosis_class = schema_view.get_class("Diagnosis")
    for slot in ("CLINICAL_T_STAGE", "CLINICAL_N_STAGE", "CLINICAL_M_STAGE", "AJCC_STAGING_SYSTEM_EDITION"):
        assert diagnosis_class.attributes[slot].required is False, f"{slot} should be optional at base level"


def test_tumor_staged_enum_values(schema_view):
    """Test TumorStagedEnum has exactly Yes/No/Unknown."""
    enum = schema_view.get_enum("TumorStagedEnum")
    assert set(enum.permissible_values.keys()) == {"Yes", "No", "Unknown"}


def test_ecog_availability_enum_exists(schema_view):
    """Test that EcogAvailabilityEnum is present in the followup schema."""
    assert "EcogAvailabilityEnum" in schema_view.all_enums()


def test_ecog_availability_slot_required(schema_view):
    """Test that ECOG_PERFORMANCE_STATUS_IS_AVAILABLE is required and ECOG_PERFORMANCE_STATUS is optional."""
    followup_class = schema_view.get_class("FollowUp")
    assert "ECOG_PERFORMANCE_STATUS_IS_AVAILABLE" in followup_class.attributes
    assert followup_class.attributes["ECOG_PERFORMANCE_STATUS_IS_AVAILABLE"].required is True
    assert followup_class.attributes["ECOG_PERFORMANCE_STATUS"].required is False
