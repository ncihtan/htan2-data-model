#!/usr/bin/env python3
"""
Script to bind file-based JSON schemas to Synapse project subfolders and create fileviews.
This script is specifically for WES, scRNA-seq, and other file-based data types.

Usage:
    python scripts/bind_file_based_schemas.py --schema-file <schema.json> --project-name <project_name>
"""

import argparse
import json
import os
import sys
from typing import Any, Dict, List

import yaml
from synapseclient import Synapse, Column, ColumnType, ViewTypeMask, EntityView
from synapseclient.core.exceptions import SynapseHTTPError


# Constants copied from schematic's json_schema_functions.py
TYPE_DICT = {
    "string": ColumnType.STRING,
    "number": ColumnType.DOUBLE,
    "integer": ColumnType.INTEGER,
    "boolean": ColumnType.BOOLEAN,
}

LIST_TYPE_DICT = {
    "string": ColumnType.STRING_LIST,
    "integer": ColumnType.INTEGER_LIST,
    "boolean": ColumnType.BOOLEAN_LIST,
}


def _get_column_type_from_js_property(js_property: Dict[str, Any]) -> ColumnType:
    """
    Gets the Synapse column type from a JSON Schema property.
    Copied from schematic's json_schema_functions.py
    """
    # Enums are always strings in Synapse tables
    if "enum" in js_property:
        return ColumnType.STRING
    if "type" in js_property:
        if js_property["type"] == "array":
            return _get_list_column_type_from_js_property(js_property)
        return TYPE_DICT.get(js_property["type"], ColumnType.STRING)
    # A oneOf list usually indicates that the type could be one or more different things
    if "oneOf" in js_property and isinstance(js_property["oneOf"], list):
        return _get_column_type_from_js_one_of_list(js_property["oneOf"])
    return ColumnType.STRING


def _get_column_type_from_js_one_of_list(js_one_of_list: List[Any]) -> ColumnType:
    """
    Gets the Synapse column type from a JSON Schema oneOf list.
    Copied from schematic's json_schema_functions.py
    """
    # items in a oneOf list should be dicts
    items = [item for item in js_one_of_list if isinstance(item, dict)]
    # Enums are always strings in Synapse tables
    if [item for item in items if "enum" in item]:
        return ColumnType.STRING
    # For Synapse ColumnType we can ignore null types in JSON Schemas
    type_items = [item for item in items if "type" in item if item["type"] != "null"]
    if len(type_items) == 1:
        type_item = type_items[0]
        if type_item["type"] == "array":
            return _get_list_column_type_from_js_property(type_item)
        return TYPE_DICT.get(type_item["type"], ColumnType.STRING)
    return ColumnType.STRING


def _get_list_column_type_from_js_property(js_property: Dict[str, Any]) -> ColumnType:
    """
    Gets the Synapse column type from a JSON Schema array property.
    Copied from schematic's json_schema_functions.py
    """
    if "items" in js_property and isinstance(js_property["items"], dict):
        # Enums are always strings in Synapse tables
        if "enum" in js_property["items"]:
            return ColumnType.STRING_LIST
        if "type" in js_property["items"]:
            return LIST_TYPE_DICT.get(
                js_property["items"]["type"], ColumnType.STRING_LIST
            )
    return ColumnType.STRING_LIST


def _create_columns_from_json_schema(json_schema: Dict[str, Any]) -> List[Column]:
    """
    Creates a list of Synapse Columns based on the JSON Schema type.
    Copied from schematic's json_schema_functions.py
    """
    properties = json_schema.get("properties")
    if properties is None:
        raise ValueError("The JSON Schema is missing a 'properties' field.")
    if not isinstance(properties, dict):
        raise ValueError(
            "The 'properties' field in the JSON Schema must be a dictionary."
        )
    
    columns = []
    for name, prop_schema in properties.items():
        column_type = _get_column_type_from_js_property(prop_schema)
        maximum_size = None
        if column_type == "STRING":
            maximum_size = 100
        if column_type in LIST_TYPE_DICT.values():
            maximum_size = 5

        column = Column(
            name=name,
            column_type=column_type,
            maximum_size=maximum_size,
            default_value=None,
        )
        columns.append(column)
    return columns


def create_or_get_folder(syn: Synapse, parent_id: str, folder_name: str) -> str:
    """Create a folder if it doesn't exist, or get the existing folder ID."""
    try:
        # Try to get existing folder
        folder = syn.get(parent_id)
        children = syn.getChildren(folder)
        
        for child in children:
            if child['name'] == folder_name and child['type'] == 'org.sagebionetworks.repo.model.Folder':
                print(f"Found existing folder: {folder_name} (ID: {child['id']})")
                return child['id']
        
        # Create new folder if not found
        print(f"Creating new folder: {folder_name}")
        folder = syn.store({
            'name': folder_name,
            'parentId': parent_id,
            'concreteType': 'org.sagebionetworks.repo.model.Folder'
        })
        return folder['id']
        
    except Exception as e:
        print(f"Error creating/getting folder {folder_name}: {e}")
        raise


def create_fileview_from_schema(syn: Synapse, schema_file: str, folder_id: str, view_name: str) -> str:
    """Create a fileview from a JSON schema and bind it to a folder."""
    try:
        # Load the JSON schema
        with open(schema_file, 'r') as f:
            schema = json.load(f)
        
        # Create columns from the schema
        columns = _create_columns_from_json_schema(schema)
        print(f"Created {len(columns)} columns from schema")
        
        # Create the fileview
        view = EntityView(
            name=view_name,
            parent_id=folder_id,
            scope_ids=[folder_id],
            view_type_mask=ViewTypeMask.FILE,
            columns=columns,
        )
        
        # Store the view
        view = syn.store(view)
        print(f"Created fileview: {view_name} (ID: {view['id']})")
        
        # Reorder columns to show important ones first
        try:
            view.reorder_column(name="createdBy", index=0)
            view.reorder_column(name="name", index=0)
            view.reorder_column(name="id", index=0)
            view.store(synapse_client=syn)
        except Exception as e:
            print(f"Warning: Could not reorder columns: {e}")
        
        return view['id']
        
    except Exception as e:
        print(f"Error creating fileview: {e}")
        raise


def main():
    parser = argparse.ArgumentParser(description='Bind file-based schemas to Synapse project folders')
    parser.add_argument('--schema-file', required=True, help='Path to the JSON schema file')
    parser.add_argument('--project-name', required=True, help='Name of the project (e.g., HTAN2_Ovarian)')
    parser.add_argument('--subfolder-name', default='WES_Level_1', help='Name of the subfolder to create (default: WES_Level_1)')
    
    args = parser.parse_args()
    
    # Load project configuration
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'projects.yml')
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        sys.exit(1)
    
    # Get project ID
    project_id = config['projects'].get(args.project_name)
    if not project_id:
        print(f"Error: Project '{args.project_name}' not found in config")
        print(f"Available projects: {list(config['projects'].keys())}")
        sys.exit(1)
    
    print(f"Binding schema to project: {args.project_name} (ID: {project_id})")
    
    # Initialize Synapse client
    try:
        syn = Synapse()
        syn.login()
    except Exception as e:
        print(f"Error logging into Synapse: {e}")
        sys.exit(1)
    
    try:
        # Create or get the subfolder
        subfolder_id = create_or_get_folder(syn, project_id, args.subfolder_name)
        
        # Create fileview from the schema
        schema_name = os.path.splitext(os.path.basename(args.schema_file))[0]
        view_name = f"{args.subfolder_name}_FileView"
        fileview_id = create_fileview_from_schema(syn, args.schema_file, subfolder_id, view_name)
        
        print(f"Successfully bound schema to folder: {subfolder_id}")
        print(f"Created fileview: {fileview_id}")
        
    except Exception as e:
        print(f"Error during binding process: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
