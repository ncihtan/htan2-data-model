import yaml
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper
from htan_linkml.schema.htan_linkml import ClinicalData

def load_test_data(file_path):
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def validate_data(data):
    try:
        # Create ClinicalData instance from test data
        clinical_data = ClinicalData(
            demographics=data['demographics'],
            exposure=data['exposure'],
            family_history=data['family_history'],
            follow_ups=[data['follow_up']],
            therapies=[data['therapy']]
        )
        # Try to serialize to YAML - this will validate the data
        yaml_dumper.dumps(clinical_data)
        print("✅ All conditional requirements are satisfied!")
        return True
    except Exception as e:
        print("❌ Validation failed:")
        print(str(e))
        return False

if __name__ == "__main__":
    test_data = load_test_data('test_conditional_requirements.yaml')
    validate_data(test_data) 