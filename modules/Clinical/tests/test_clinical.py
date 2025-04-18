"""Clinical test."""
import os
import unittest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from modules.Clinical.src.htan_clinical.datamodel.clinical import ClinicalData

class TestClinical(unittest.TestCase):
    """Test cases for Clinical module."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_dir = Path(__file__).parent.parent
        self.schema_path = self.base_dir / "domains" / "clinical.yaml"
        self.schema_view = SchemaView(str(self.schema_path))
        
        # Get all test files
        self.test_data_dir = self.base_dir / "tests" / "test_data"
        self.valid_files = glob.glob(str(self.test_data_dir / "valid" / "*.yaml"))
        self.invalid_files = glob.glob(str(self.test_data_dir / "invalid" / "*.yaml"))

    def test_schema_loads(self):
        """Test that the schema can be loaded."""
        self.assertIsNotNone(self.schema_view)
        self.assertIn("ClinicalData", self.schema_view.all_classes())

    def test_valid_data(self):
        """Test that all valid data files validate."""
        for file_path in self.valid_files:
            with self.subTest(file=file_path):
                with open(file_path) as f:
                    # This will validate during loading
                    data = yaml_loader.load(f, target_class=ClinicalData)
                self.assertIsInstance(data, ClinicalData)

    def test_invalid_data(self):
        """Test that all invalid data files fail validation."""
        for file_path in self.invalid_files:
            with self.subTest(file=file_path):
                with self.assertRaises(ValueError):
                    with open(file_path) as f:
                        # This should raise a ValueError during loading
                        yaml_loader.load(f, target_class=ClinicalData)

    def test_required_fields(self):
        """Test that missing required fields are caught."""
        test_data = {
            "PARTICIPANT_ID": "TEST-001"
            # Missing required fields
        }
        with self.assertRaises(ValueError):
            ClinicalData(**test_data)

    def test_enum_values(self):
        """Test that invalid enum values are caught."""
        test_data = {
            "PARTICIPANT_ID": "TEST-001",
            "DIAGNOSIS": {
                "TUMOR_GRADE": "G5"  # Invalid enum value
            }
        }
        with self.assertRaises(ValueError):
            ClinicalData(**test_data)

    def test_data_types(self):
        """Test that invalid data types are caught."""
        test_data = {
            "PARTICIPANT_ID": "TEST-001",
            "DIAGNOSIS": {
                "AGE_AT_DIAGNOSIS_DAYS": "not_a_number"  # Should be integer
            }
        }
        with self.assertRaises(ValueError):
            ClinicalData(**test_data)

if __name__ == '__main__':
    unittest.main() 