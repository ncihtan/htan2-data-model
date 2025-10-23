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
                # This should raise a ValueError during loading
                yaml_loader.load(f, target_class=ClinicalData)


def test_required_fields():
    """Test that missing required fields are caught."""
    test_data = {
        "HTAN_PARTICIPANT_ID": "TEST-001"
        # Missing required fields
    }
    with pytest.raises(ValueError):
        ClinicalData(**test_data)


def test_enum_values():
    """Test that invalid enum values are caught."""
    test_data = {
        "HTAN_PARTICIPANT_ID": "TEST-001",
        "DIAGNOSIS": {"TUMOR_GRADE": "G5"},  # Invalid enum value
    }
    with pytest.raises(ValueError):
        ClinicalData(**test_data)


def test_data_types():
    """Test that invalid data types are caught."""
    test_data = {
        "HTAN_PARTICIPANT_ID": "TEST-001",
        "DIAGNOSIS": {"AGE_AT_DIAGNOSIS_DAYS": "not_a_number"},  # Should be integer
    }
    with pytest.raises(ValueError):
        ClinicalData(**test_data)
