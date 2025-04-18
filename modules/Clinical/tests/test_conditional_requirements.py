import unittest
from pathlib import Path
import sys
import os
import yaml
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper
from modules.Clinical.src.htan_clinical.datamodel.clinical import ClinicalData

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

class TestConditionalRequirements(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Load test data once for all tests"""
        test_data_path = os.path.join(os.path.dirname(__file__), "test_conditional_requirements.yaml")
        with open(test_data_path) as f:
            cls.test_data = yaml.safe_load(f)

    def test_valid_clinical_data(self):
        """Test that valid clinical data can be loaded and validated"""
        clinical_data = yaml_loader.loads(yaml.dump(self.test_data), target_class=ClinicalData)
        self.assertIsNotNone(clinical_data)
        
        # Verify required fields in Demographics
        self.assertIsNotNone(clinical_data.DEMOGRAPHICS.ETHNIC_GROUP)
        self.assertIsNotNone(clinical_data.DEMOGRAPHICS.GENDER_IDENTITY)
        self.assertIsNotNone(clinical_data.DEMOGRAPHICS.SEX)
        self.assertIsNotNone(clinical_data.DEMOGRAPHICS.RACE)

    def test_followup_conditional_requirements(self):
        """Test conditional requirements in follow-up data"""
        clinical_data = yaml_loader.loads(yaml.dump(self.test_data), target_class=ClinicalData)
        
        # When PROGRESSION_OR_RECURRENCE is "Yes", certain fields should be required
        for followup in clinical_data.FOLLOW_UPS:
            if followup.PROGRESSION_OR_RECURRENCE == "Yes":
                self.assertIsNotNone(followup.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE)
                self.assertIsNotNone(followup.PROGRESSION_OR_RECURRENCE_TYPE)
                self.assertIsNotNone(followup.EVIDENCE_OF_RECURRENCE_TYPE)
                self.assertIsNotNone(followup.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE)

    def test_family_history_conditional_requirements(self):
        """Test conditional requirements in family history data"""
        clinical_data = yaml_loader.loads(yaml.dump(self.test_data), target_class=ClinicalData)
        
        # When FAMILY_MEMBER_CANCER_HISTORY is "Yes", RELATIVES_WITH_CANCER_HISTORY should be required
        if clinical_data.FAMILY_HISTORY.FAMILY_MEMBER_CANCER_HISTORY == "Yes":
            self.assertIsNotNone(clinical_data.FAMILY_HISTORY.RELATIVES_WITH_CANCER_HISTORY)

    def test_invalid_data_missing_required_field(self):
        """Test that missing required fields raise appropriate errors"""
        invalid_data = self.test_data.copy()
        del invalid_data['DEMOGRAPHICS']['ETHNIC_GROUP']
        
        with self.assertRaises(ValueError) as context:
            yaml_loader.loads(yaml.dump(invalid_data), target_class=ClinicalData)
        
        self.assertTrue('ETHNIC_GROUP must be supplied' in str(context.exception))

    def test_invalid_enum_values(self):
        """Test that invalid enum values raise appropriate errors"""
        invalid_data = self.test_data.copy()
        invalid_data['DEMOGRAPHICS']['ETHNIC_GROUP'] = "Invalid Value"
        
        with self.assertRaises(ValueError) as context:
            yaml_loader.loads(yaml.dump(invalid_data), target_class=ClinicalData)
        
        self.assertTrue('Unknown EthnicGroupEnum enumeration code: Invalid Value' in str(context.exception))

if __name__ == "__main__":
    unittest.main() 