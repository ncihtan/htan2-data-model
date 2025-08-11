import pytest
from pathlib import Path
import sys
import os
import yaml
from copy import deepcopy
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper
from htan_clinical.datamodel.clinical import ClinicalData

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

@pytest.fixture(scope="class")
def test_data():
    """Load test data once for all tests"""
    test_data_path = os.path.join(os.path.dirname(__file__), "test_conditional_requirements.yaml")
    with open(test_data_path) as f:
        return yaml.safe_load(f)

def test_valid_clinical_data(test_data):
    """Test that valid clinical data can be loaded and validated"""
    clinical_data = yaml_loader.loads(yaml.dump(test_data), target_class=ClinicalData)
    assert clinical_data is not None
    
    # Verify required fields in Demographics
    assert clinical_data.DEMOGRAPHICS.ETHNIC_GROUP is not None
    assert clinical_data.DEMOGRAPHICS.GENDER_IDENTITY is not None
    assert clinical_data.DEMOGRAPHICS.SEX is not None
    assert clinical_data.DEMOGRAPHICS.RACE is not None

def test_followup_conditional_requirements(test_data):
    """Test conditional requirements in follow-up data"""
    clinical_data = yaml_loader.loads(yaml.dump(test_data), target_class=ClinicalData)
    
    # When PROGRESSION_OR_RECURRENCE is "Yes", certain fields should be required
    for followup in clinical_data.FOLLOW_UPS:
        if hasattr(followup, 'PROGRESSION_OR_RECURRENCE') and followup.PROGRESSION_OR_RECURRENCE == "Yes":
            assert followup.PROGRESSION_OR_RECURRENCE_ANATOMIC_SITE_UBERON_CODE is not None
            assert followup.PROGRESSION_OR_RECURRENCE_TYPE is not None
            assert followup.EVIDENCE_OF_RECURRENCE_TYPE is not None
            assert followup.AGE_IN_DAYS_AT_PROGRESSION_OR_RECURRENCE is not None

def test_family_history_conditional_requirements(test_data):
    """Test conditional requirements in family history data"""
    clinical_data = yaml_loader.loads(yaml.dump(test_data), target_class=ClinicalData)
    
    # When FAMILY_MEMBER_CANCER_HISTORY is "Yes", RELATIVES_WITH_CANCER_HISTORY should be required
    if clinical_data.FAMILY_HISTORY.FAMILY_MEMBER_CANCER_HISTORY == "Yes":
        assert clinical_data.FAMILY_HISTORY.RELATIVES_WITH_CANCER_HISTORY is not None

def test_invalid_data_missing_required_field(test_data):
    """Test that missing required fields raise appropriate errors"""
    invalid_data = deepcopy(test_data)
    del invalid_data['DEMOGRAPHICS']['ETHNIC_GROUP']
    
    with pytest.raises(ValueError) as excinfo:
        yaml_loader.loads(yaml.dump(invalid_data), target_class=ClinicalData)
    
    assert 'ETHNIC_GROUP must be supplied' in str(excinfo.value)

def test_invalid_enum_values(test_data):
    """Test that invalid enum values raise appropriate errors"""
    invalid_data = deepcopy(test_data)
    invalid_data['DEMOGRAPHICS']['ETHNIC_GROUP'] = "Invalid Value"
    
    with pytest.raises(ValueError) as excinfo:
        yaml_loader.loads(yaml.dump(invalid_data), target_class=ClinicalData)
    
    assert 'Unknown EthnicGroupEnum enumeration code: Invalid Value' in str(excinfo.value) 