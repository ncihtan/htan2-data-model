"""Test data validation for HTAN LinkML schemas.

This module contains test cases for validating YAML data files against their
corresponding LinkML schemas. It uses the LinkML runtime's built-in validation
capabilities to ensure data conformance.

The tests expect data files to be organized in the following structure:
    tests/test_data/
        Participant/
            valid/      # Contains valid Participant YAML files
            invalid/    # Contains intentionally invalid YAML files
"""

import os
import pytest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

# Try different import paths for Participant
Participant = None
try:
    from htan_linkml.schema_classes.participant import Participant
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
    """Schema path for Participant module."""
    return base_dir / "modules" / "Participant" / "participant.yaml"


@pytest.fixture
def schema_view(schema_path):
    """SchemaView instance for validation."""
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


@pytest.mark.skipif(Participant is None, reason="Participant module not available")
def test_valid_data(valid_files):
    """Test that all valid data files validate successfully.

    For each valid test file:
    1. Loads and validates the YAML data using the Participant schema
    2. Verifies that the loaded data is an instance of Participant class

    The validation happens automatically during YAML loading when using
    the target_class parameter.
    """
    for test_file in valid_files:
        with open(test_file) as f:
            # This will validate during loading
            data = yaml_loader.load(f, target_class=Participant)
        assert isinstance(data, Participant)


@pytest.mark.skipif(Participant is None, reason="Participant module not available")
def test_invalid_data(invalid_files):
    """Test that all invalid data files fail validation appropriately.

    For each invalid test file:
    1. Attempts to load and validate the YAML data
    2. Verifies that a ValueError is raised during loading

    Invalid files may contain:
    - Invalid enum values
    - Missing required fields
    - Incorrect data types
    """
    for test_file in invalid_files:
        with pytest.raises(ValueError):
            with open(test_file) as f:
                # This should raise a ValueError during loading
                yaml_loader.load(f, target_class=Participant)
