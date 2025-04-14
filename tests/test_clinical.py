"""Clinical test."""
import os
import unittest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from htan_linkml.schema_classes.clinical import ClinicalData

class TestClinical(unittest.TestCase):
    """Test cases for Clinical module."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_dir = Path(__file__).parent.parent
        self.schema_path = self.base_dir / "modules" / "Clinical" / "clinical_schema.yaml"
        self.schema_view = SchemaView(str(self.schema_path))
        
        # Get all test files
        self.valid_files = glob.glob(str(self.base_dir / "tests" / "test_data" / "Clinical" / "valid" / "*.yaml"))
        self.invalid_files = glob.glob(str(self.base_dir / "tests" / "test_data" / "Clinical" / "invalid" / "*.yaml"))

    def test_schema_loads(self):
        """Test that the schema can be loaded."""
        self.assertIsNotNone(self.schema_view)
        self.assertIn("ClinicalData", self.schema_view.all_classes())

    def test_valid_data(self):
        """Test that all valid data files validate."""
        for file_path in self.valid_files:
            with self.subTest(file=file_path):
                with open(file_path) as f:
                    data = yaml_loader.load(f, target_class=ClinicalData)
                try:
                    self.schema_view.get_class("ClinicalData").validate(data)
                    validation_failed = False
                except Exception as e:
                    validation_failed = True
                    validation_error = str(e)
                self.assertFalse(validation_failed, 
                               f"Validation failed for {file_path}: {validation_error if validation_failed else ''}")

    def test_invalid_data(self):
        """Test that all invalid data files fail validation."""
        for file_path in self.invalid_files:
            with self.subTest(file=file_path):
                with open(file_path) as f:
                    data = yaml_loader.load(f, target_class=ClinicalData)
                with self.assertRaises(Exception):
                    self.schema_view.get_class("ClinicalData").validate(data)

    def test_required_fields(self):
        """Test that missing required fields are caught."""
        test_data = {
            "participant_id": "TEST-001"
            # Missing required fields
        }
        with self.assertRaises(Exception):
            self.schema_view.get_class("ClinicalData").validate(test_data)

    def test_enum_values(self):
        """Test that invalid enum values are caught."""
        test_data = {
            "participant_id": "TEST-001",
            "diagnosis": {
                "tumor_grade": "INVALID_GRADE"  # Invalid enum value
            }
        }
        with self.assertRaises(Exception):
            self.schema_view.get_class("ClinicalData").validate(test_data)

    def test_data_types(self):
        """Test that invalid data types are caught."""
        test_data = {
            "participant_id": "TEST-001",
            "diagnosis": {
                "age_at_diagnosis_days": "not_a_number"  # Should be integer
            }
        }
        with self.assertRaises(Exception):
            self.schema_view.get_class("ClinicalData").validate(test_data)

if __name__ == '__main__':
    unittest.main() 