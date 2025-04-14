import os
import unittest
from pathlib import Path

from linkml_runtime.loaders import yaml_loader
from linkml.validators.validator import Validator
from linkml.validators.jsonschemavalidator import JsonSchemaValidator

class TestClinical(unittest.TestCase):
    """Test cases for Clinical module."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_dir = Path(__file__).parent.parent
        self.schema_path = self.base_dir / "modules" / "Clinical" / "clinical_schema.yaml"
        self.valid_data_path = self.base_dir / "modules" / "Clinical" / "test_data.yaml"
        self.validator = Validator(self.schema_path)

    def test_schema_loads(self):
        """Test that the schema can be loaded."""
        validator = JsonSchemaValidator(self.schema_path)
        self.assertIsNotNone(validator.schema)

    def test_valid_data(self):
        """Test that valid data validates."""
        with open(self.valid_data_path) as f:
            data = yaml_loader.load(f, target_class="ClinicalData")
        validation_results = self.validator.validate(data)
        self.assertEqual(len(validation_results), 0)

    def test_required_fields(self):
        """Test that missing required fields are caught."""
        test_data = {
            "participant_id": "TEST-001"
            # Missing required fields
        }
        validation_results = self.validator.validate(test_data)
        self.assertGreater(len(validation_results), 0)

    def test_enum_values(self):
        """Test that invalid enum values are caught."""
        test_data = {
            "participant_id": "TEST-001",
            "diagnosis": {
                "tumor_grade": "INVALID_GRADE"  # Invalid enum value
            }
        }
        validation_results = self.validator.validate(test_data)
        self.assertGreater(len(validation_results), 0)

    def test_data_types(self):
        """Test that invalid data types are caught."""
        test_data = {
            "participant_id": "TEST-001",
            "diagnosis": {
                "age_at_diagnosis_days": "not_a_number"  # Should be integer
            }
        }
        validation_results = self.validator.validate(test_data)
        self.assertGreater(len(validation_results), 0)

if __name__ == '__main__':
    unittest.main() 