#!/usr/bin/env python3
"""Push annotations from JSON files to Synapse entities"""

import synapseclient
import json

def push_annotations_from_file(file_path, entity_id):
    """Push annotations from a JSON file to a Synapse entity"""
    
    print(f"Pushing annotations from {file_path} to entity {entity_id}")
    print("=" * 60)
    
    # Read the JSON file
    try:
        with open(file_path, 'r') as f:
            annotations = json.load(f)
        print(f"✅ Loaded annotations from {file_path}")
        print(f"Annotations: {json.dumps(annotations, indent=2)}")
    except Exception as e:
        print(f"❌ Error reading file {file_path}: {e}")
        return
    
    # Login to Synapse
    syn = synapseclient.login()
    
    try:
        # Get the entity
        entity = syn.get(entity_id)
        print(f"✅ Retrieved entity: {entity.name}")
        
        # Apply the annotations
        # Convert single values to lists (Synapse expects lists)
        synapse_annotations = {}
        for key, value in annotations.items():
            if isinstance(value, list):
                synapse_annotations[key] = value
            else:
                synapse_annotations[key] = [value]
        
        # Update the entity's annotations
        entity.annotations.update(synapse_annotations)
        
        # Store the entity
        syn.store(entity)
        print(f"✅ Successfully applied annotations to {entity_id}")
        
        # Verify the annotations were applied
        updated_entity = syn.get(entity_id)
        print(f"✅ Verified annotations: {getattr(updated_entity, 'annotations', {})}")
        
    except Exception as e:
        print(f"❌ Error applying annotations: {e}")

def main():
    # Example mapping: update with your actual files and Synapse IDs
    file_mappings = {
        "example_annotations.json": "syn12345678"
    }
    
    print("Pushing annotations from JSON files to Synapse entities")
    print("=" * 70)
    
    for file_path, entity_id in file_mappings.items():
        print(f"\nProcessing: {file_path} -> {entity_id}")
        push_annotations_from_file(file_path, entity_id)
        print()

if __name__ == "__main__":
    main() 