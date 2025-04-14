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
import unittest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from htan_linkml.schema_classes.participant import Participant

class TestData(unittest.TestCase):
    """Test cases for validating HTAN data files against their schemas.
    
    This test suite validates both valid and invalid test data files against
    their corresponding LinkML schemas. Validation is performed using LinkML's
    built-in validation during YAML loading.
    """

    def setUp(self):
        """Set up test fixtures.
        
        Initializes:
            - Base directory path
            - Schema path for Participant module
            - SchemaView instance for validation
            - Lists of valid and invalid test files
        """
        self.base_dir = Path(__file__).parent.parent
        self.schema_path = self.base_dir / "modules" / "Participant" / "participant.yaml"
        self.schema_view = SchemaView(str(self.schema_path))
        
        # Get all test files
        self.valid_files = glob.glob(str(self.base_dir / "tests" / "test_data" / "Participant" / "valid" / "*.yaml"))
        self.invalid_files = glob.glob(str(self.base_dir / "tests" / "test_data" / "Participant" / "invalid" / "*.yaml"))

    def test_valid_data(self):
        """Test that all valid data files validate successfully.
        
        For each valid test file:
        1. Loads and validates the YAML data using the Participant schema
        2. Verifies that the loaded data is an instance of Participant class
        
        The validation happens automatically during YAML loading when using
        the target_class parameter.
        """
        for test_file in self.valid_files:
            with self.subTest(test_file=test_file):
                with open(test_file) as f:
                    # This will validate during loading
                    data = yaml_loader.load(f, target_class=Participant)
                self.assertIsInstance(data, Participant)

    def test_invalid_data(self):
        """Test that all invalid data files fail validation appropriately.
        
        For each invalid test file:
        1. Attempts to load and validate the YAML data
        2. Verifies that a ValueError is raised during loading
        
        Invalid files may contain:
        - Invalid enum values
        - Missing required fields
        - Incorrect data types
        """
        for test_file in self.invalid_files:
            with self.subTest(test_file=test_file):
                with self.assertRaises(ValueError):
                    with open(test_file) as f:
                        # This should raise a ValueError during loading
                        yaml_loader.load(f, target_class=Participant)
