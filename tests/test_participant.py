"""Participant test."""

import os
import pytest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

# Try different import paths for Participant
Participant = None
try:
    from htan2_data_model.schema_classes.participant import Participant
except ImportError:
    try:
        from modules.Participant.src.htan_participant.datamodel.participant import (
            Participant,
        )
    except ImportError:
        # If neither works, Participant will be None and tests will be skipped
        pass


@pytest.fixture
def base_dir():
    """Base directory for tests."""
    return Path(__file__).parent.parent


@pytest.fixture
def schema_path(base_dir):
    """Schema path."""
    # Note: participant.yaml is currently in archive/modules/Participant/
    # This test is skipped until the schema is moved to the active modules
    return base_dir / "modules" / "Participant" / "participant.yaml"


@pytest.fixture
def schema_view(schema_path):
    """Schema view."""
    return SchemaView(str(schema_path))


@pytest.fixture
def valid_files(base_dir):
    """Valid test files."""
    return glob.glob(
        str(base_dir / "tests" / "test_data" / "Participant" / "valid" / "*.yaml")
    )


@pytest.fixture
def invalid_files(base_dir):
    """Invalid test files."""
    return glob.glob(
        str(base_dir / "tests" / "test_data" / "Participant" / "invalid" / "*.yaml")
    )


@pytest.mark.skip(reason="Participant schema not available in current modules structure")
def test_schema_loads(schema_view):
    """Test that the schema can be loaded."""
    assert schema_view is not None
    assert "Participant" in schema_view.all_classes()


@pytest.mark.skip(reason="Participant schema not available in current modules structure")
def test_valid_data(valid_files):
    """Test that all valid data files validate."""
    for file_path in valid_files:
        with open(file_path) as f:
            # This will validate during loading
            data = yaml_loader.load(f, target_class=Participant)
        assert isinstance(data, Participant)


@pytest.mark.skip(reason="Participant schema not available in current modules structure")
def test_invalid_data(invalid_files):
    """Test that all invalid data files fail validation."""
    for file_path in invalid_files:
        with pytest.raises(ValueError):
            with open(file_path) as f:
                # This should raise a ValueError during loading
                yaml_loader.load(f, target_class=Participant)


@pytest.mark.skip(reason="Participant schema not available in current modules structure")
def test_required_fields():
    """Test that missing required fields are caught."""
    test_data = {
        "participant_id": "TEST-001"
        # Missing required fields
    }
    with pytest.raises(ValueError):
        Participant(**test_data)


@pytest.mark.skip(reason="Participant schema not available in current modules structure")
def test_enum_values():
    """Test that invalid enum values are caught."""
    test_data = {
        "participant_id": "TEST-001",
        "race": "INVALID_RACE",  # Invalid enum value
    }
    with pytest.raises(ValueError):
        Participant(**test_data)


@pytest.mark.skip(reason="Participant schema not available in current modules structure")
def test_data_types():
    """Test that invalid data types are caught."""
    test_data = {
        "participant_id": "TEST-001",
        "age_at_enrollment_days": "not_a_number",  # Should be integer
    }
    with pytest.raises(ValueError):
        Participant(**test_data)
