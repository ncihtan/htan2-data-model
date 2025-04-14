"""Participant test."""
import os
import unittest
from pathlib import Path
import glob

from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from htan_linkml.schema_classes.participant import Participant

class TestParticipant(unittest.TestCase):
    """Test cases for Participant module."""

    def setUp(self):
        """Set up test fixtures."""
        self.base_dir = Path(__file__).parent.parent
        self.schema_path = self.base_dir / "modules" / "Participant" / "participant.yaml"
        self.schema_view = SchemaView(str(self.schema_path))
        
        # Get all test files
        self.valid_files = glob.glob(str(self.base_dir / "tests" / "test_data" / "Participant" / "valid" / "*.yaml"))
        self.invalid_files = glob.glob(str(self.base_dir / "tests" / "test_data" / "Participant" / "invalid" / "*.yaml"))

    def test_schema_loads(self):
        """Test that the schema can be loaded."""
        self.assertIsNotNone(self.schema_view)
        self.assertIn("Participant", self.schema_view.all_classes())

    def test_valid_data(self):
        """Test that all valid data files validate."""
        for file_path in self.valid_files:
            with self.subTest(file=file_path):
                with open(file_path) as f:
                    # This will validate during loading
                    data = yaml_loader.load(f, target_class=Participant)
                self.assertIsInstance(data, Participant)

    def test_invalid_data(self):
        """Test that all invalid data files fail validation."""
        for file_path in self.invalid_files:
            with self.subTest(file=file_path):
                with self.assertRaises(ValueError):
                    with open(file_path) as f:
                        # This should raise a ValueError during loading
                        yaml_loader.load(f, target_class=Participant)

    def test_required_fields(self):
        """Test that missing required fields are caught."""
        test_data = {
            "participant_id": "TEST-001"
            # Missing required fields
        }
        with self.assertRaises(ValueError):
            Participant(**test_data)

    def test_enum_values(self):
        """Test that invalid enum values are caught."""
        test_data = {
            "participant_id": "TEST-001",
            "race": "INVALID_RACE"  # Invalid enum value
        }
        with self.assertRaises(ValueError):
            Participant(**test_data)

    def test_data_types(self):
        """Test that invalid data types are caught."""
        test_data = {
            "participant_id": "TEST-001",
            "age_at_enrollment_days": "not_a_number"  # Should be integer
        }
        with self.assertRaises(ValueError):
            Participant(**test_data)

if __name__ == '__main__':
    unittest.main() 