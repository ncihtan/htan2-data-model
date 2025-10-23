"""synapse_json_schema_bind.py

This script will create and bind a JSON schema to an entity

Usage: python synapse_json_schema_bind.py -t [Entity Synapse Id] -l [JSON Schema URL] -p [JSON Schema File Path] -n [Organization Name] -ar --no_bind
-t Synapse Id of an entity to which a schema will be bound.
-l URL for the JSON schema to be bound to the requested entity.
-p File path for the JSON schema to be bound to the requested entity.
-n Name of the organization with which the JSON schema should be associated. Default: 'Example Organization'.
-ar Indicates if the schema includes Access Requirement information.
--no_bind Indicates the schema should not be bound to the entity. 

author: orion.banks
"""

import synapseclient
import argparse
import pandas as pd
import requests
import json


def get_args():
    """Set up command-line interface and get arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        type=str,
        default=None,
        help="Synapse Id of an entity to which a schema will be bound.",
        required=False
    )
    parser.add_argument(
        "-l",
        type=str,
        default=None,
        help="The URL for the JSON schema to be bound to the requested entity.",
        required=False
    )
    parser.add_argument(
        "-p",
        type=str,
        default=None,
        help="The file path for the JSON schema to be bound to the requested entity.",
        required=False
    )
    parser.add_argument(
        "-n",
        type=str,
        default="Example Organization",
        help="The name of the organization with which the JSON schema should be associated. Default: 'Example Organization'.",
        required=False
    )
    parser.add_argument(
        "-ar",
        action="store_true",
        help="Indicates if the schema includes Access Requirement information.",
        required=False,
        default=None
    )
    parser.add_argument(
        "--no_bind",
        action="store_true",
        help="Indicates the schema should not be bound to the entity.",
        required=False,
        default=None
    )
    parser.add_argument(
        "--create_fileview",
        action="store_true",
        help="Create a fileview with columns extracted from the JSON schema.",
        required=False,
        default=None
    )
    return parser.parse_args()


def get_schema_organization(service, org_name: str) -> tuple:
    """Create or access the named Synapse organization,
    return a tuple of schema service object, organization object, and organization name"""
    
    print(f"Creating organization: {org_name}")

    try:
        schema_org = service.JsonSchemaOrganization(name = org_name)
        schema_org.create()
    except synapseclient.core.exceptions.SynapseHTTPError:
        print(f"Organization {org_name} already exists, getting info now...")
        schema_org = service.get_organization(organization_name = org_name)
    
    return service, schema_org, org_name


def register_json_schema(org, schema_type: str, schema_json: json, version: str, schema_org_name: str) -> str:
    """Register or access a previously registered JSON schema and return the uri.
    If the schema was previously registered, the constructed uri will be returned.
    uri format: [schema_org_name]-[schema_type]-[num_version]
    Example uri: ExampleOrganization-CA987654AccessRequirement-2.0.0
    """
    
    # Handle version format - remove 'v' prefix if present
    if version.startswith("v"):
        num_version = version[1:]
    else:
        num_version = version

    uri = "-".join([schema_org_name.replace(" ", ""), schema_type,num_version])

    try:
        schema = org.create_json_schema(schema_json, schema_type, semantic_version=num_version)
        uri = schema.uri
        print(f"JSON schema {uri} was successfully registered.")
    except synapseclient.core.exceptions.SynapseHTTPError as error:
        print(error)
        print(f"JSON schema {uri} was previously registered and will not be updated.")
    
    print(f"\nSchema is available at https://repo-prod.prod.sagebase.org/repo/v1/schema/type/registered/{uri}\nThe schema can be referenced using the id: {uri}\n")
    
    return uri


def bind_schema_to_entity(syn, service, schema_uri: str, entity_id: str, component_type: str, includes_ar: bool):
    """Associate a registered JSON schema with a Synapse entity.
    For JSON schemas associated with DUO-based access restrictions, use the REST API and enable derived annotations,
    For non-AR schemas, use the python client bind_json_schema function"""

    if component_type == "AccessRequirement" or includes_ar is not None:
        print(f"Binding AR schema {schema_uri}")
        request_body = {
            "entityId": entity_id,
            "schema$id": schema_uri,
            "enableDerivedAnnotations": True
            }
        syn.restPUT(
            f"/entity/{entity_id}/schema/binding", body=json.dumps(request_body)
        )
    
    else:
        print(f"Binding non-AR schema {schema_uri}")
        service.bind_json_schema_to_entity(entity_id, schema_uri)


def create_fileview_from_schema(syn, schema_json: dict, parent_id: str, schema_name: str) -> str:
    """Create a Synapse fileview with columns extracted from JSON schema properties."""
    
    print(f"Creating fileview for schema: {schema_name}")
    
    # Extract properties from the schema
    properties = {}
    if "$defs" in schema_json:
        # Find the main class definition
        for def_name, def_content in schema_json["$defs"].items():
            if "properties" in def_content:
                properties = def_content["properties"]
                break
    elif "properties" in schema_json:
        properties = schema_json["properties"]
    
    if not properties:
        print("❌ No properties found in schema")
        return None
    
    # Create columns from schema properties (limit to most important ones)
    columns = []
    important_fields = [
        "COMPONENT", "FILENAME", "FILE_FORMAT", "HTAN_DATA_FILE_ID", "HTAN_PARENT_BIOSPECIMEN_ID",
        "SEQUENCING_PLATFORM", "LIBRARY_LAYOUT", "READ_LENGTH", "LIBRARY_SELECTION_METHOD",
        "SEQUENCING_BATCH_ID", "TARGET_CAPTURE_KIT", "LIBRARY_PREPARATION_KIT_NAME"
    ]
    
    for prop_name, prop_def in properties.items():
        # Only include important fields to stay within size limits
        if prop_name not in important_fields:
            continue
        # Determine column type based on JSON schema type
        column_type = "STRING"  # Default
        
        if "type" in prop_def:
            if isinstance(prop_def["type"], list):
                # Handle union types like ["string", "null"]
                types = [t for t in prop_def["type"] if t != "null"]
                if types:
                    column_type = map_json_type_to_synapse_type(types[0])
            else:
                column_type = map_json_type_to_synapse_type(prop_def["type"])
        
        # Create column using synapseclient.table.Column
        from synapseclient.table import Column
        
        column = Column(
            name=prop_name,
            columnType=column_type,
            maximumSize=100 if column_type == "STRING" else None
        )
        
        columns.append(column)
    
    print(f"Created {len(columns)} columns from schema properties")
    
    # Create the fileview
    fileview_name = f"{schema_name} Fileview"
    fileview_description = f"Fileview for {schema_name} schema with columns extracted from JSON schema properties"
    
    try:
        # Create EntityViewSchema using the correct API
        from synapseclient.table import EntityViewSchema, EntityViewType
        
        # Create the fileview schema
        fileview_schema = EntityViewSchema(
            name=fileview_name,
            description=fileview_description,
            parent=parent_id,
            scopes=[parent_id],
            viewType=EntityViewType.FILE,
            columns=columns
        )
        
        # Store the fileview
        fileview = syn.store(fileview_schema)
        fileview_id = fileview.id
        
        print(f"✅ Created fileview: {fileview_name} (ID: {fileview_id})")
        print(f"✅ Added {len(columns)} columns to fileview")
        
        return fileview_id
        
    except Exception as e:
        print(f"❌ Error creating fileview: {e}")
        return None


def map_json_type_to_synapse_type(json_type: str) -> str:
    """Map JSON schema type to Synapse column type."""
    type_mapping = {
        "string": "STRING",
        "integer": "INTEGER", 
        "number": "DOUBLE",
        "boolean": "BOOLEAN",
        "array": "STRING_LIST",
        "object": "STRING"
    }
    return type_mapping.get(json_type, "STRING")


def create_wiki_with_fileview_id(syn, entity_id: str, fileview_id: str, schema_name: str):
    """Create a wiki page on the entity with the fileview ID."""
    
    print(f"Creating wiki page for fileview: {fileview_id}")
    
    # Create wiki content with hyperlink
    fileview_url = f"https://www.synapse.org/#!Synapse:{fileview_id}"
    wiki_content = f"""# {schema_name} Data View

This page displays the {schema_name} data files with schema-validated metadata.

## Fileview

The data is displayed in a fileview with columns extracted from the JSON schema:

**Fileview ID**: `{fileview_id}`

**[View Fileview →]({fileview_url})**

## Schema Validation

All files in this folder are validated against the {schema_name} JSON schema. Files with invalid or missing required annotations will show validation errors.

## Columns

The fileview includes the following key columns:
- COMPONENT
- FILENAME  
- FILE_FORMAT
- HTAN_DATA_FILE_ID
- HTAN_PARENT_BIOSPECIMEN_ID
- SEQUENCING_PLATFORM
- LIBRARY_LAYOUT
- READ_LENGTH
- LIBRARY_SELECTION_METHOD
- SEQUENCING_BATCH_ID
- TARGET_CAPTURE_KIT
- LIBRARY_PREPARATION_KIT_NAME

## Usage

Files uploaded to this folder will automatically appear in the fileview with their metadata validated against the schema.

## Quick Links

- [Open Fileview]({fileview_url})
- [Schema Documentation](https://repo-prod.prod.sagebase.org/repo/v1/schema/type/registered/HTAN2Organization-{schema_name}-1.0.0)
"""
    
    try:
        # Create or update the wiki
        syn.store(synapseclient.Wiki(
            owner=entity_id,
            title=f"{schema_name} Data View",
            markdown=wiki_content
        ))
        
        print(f"✅ Wiki page created on entity {entity_id}")
        print(f"✅ Fileview ID {fileview_id} stored in wiki")
        
    except Exception as e:
        print(f"❌ Error creating wiki: {e}")
   
def get_schema_from_url(url: str, path: str) -> tuple[any, str, str, str]:
    """Access a JSON schema via a provided path or URL.
    Return request JSON and parsed schema name elements.

    Note that the filename must match expected conventions:
    Non-AR schema example: mc2.DatasetView-v1.0.0-schema.json
    AR schema example: MC2.AccessRequirement-CA000001-v3.0.2-schema.json
    """

    if url or path is not None:
        if url is not None:
            schema = url
            source_schema = requests.get(url)
            schema_json = source_schema.json()
        else:
            schema = path
            source_schema = open(path, "r")
            schema_json = json.load(source_schema)
            
        schema_info = schema.split("/")[-1]
        
        # Handle different naming conventions
        if "-" in schema_info and len(schema_info.split("-")) >= 2:
            # Standard convention: HTAN.Component-v1.0.0-schema.json
            base_component = schema_info.split(".")[1].split("-")[0]
            
            if base_component == "AccessRequirement":
                component = "".join(schema_info.split("-")[0:-2]).split(".")[1]
                version = schema_info.split("-")[-2]
            else:
                component = base_component
                version = schema_info.split("-")[1]
        else:
            # Fallback for files like level_1_schema.json
            base_component = schema_info.split(".")[0].replace("_", "")
            component = base_component
            version = "1.0.0"  # Default version

    print(f"JSON schema {component} {version} successfully acquired from repository")

    return schema_json, component, base_component, version


def get_register_bind_schema(syn, target: str, schema_org_name: str, org, service, path, url, includes_ar: bool, no_bind: bool, create_fileview: bool):
    """Access JSON from URL, register the JSON schema, and bind the schema to the target entity."""

    schema_json, component_adjusted, base_component, version = get_schema_from_url(url, path)
    print(f"Registering JSON schema {component_adjusted} {version}")

    uri = register_json_schema(org, component_adjusted, schema_json, version, schema_org_name)

    if no_bind is None:
        bind_schema_to_entity(syn, service, uri, target, base_component, includes_ar)
        print(f"\nSchema {component_adjusted} {version} successfully bound to entity {target}")
        
        # Create fileview if requested
        if create_fileview:
            fileview_id = create_fileview_from_schema(syn, schema_json, target, component_adjusted)
            if fileview_id:
                print(f"✅ Fileview created with ID: {fileview_id}")
                # Create wiki page with fileview ID
                create_wiki_with_fileview_id(syn, target, fileview_id, component_adjusted)
            else:
                print("❌ Failed to create fileview")
        


def main():

    args = get_args()
    target, url, path, org_name, includes_ar, no_bind, create_fileview = args.t, args.l, args.p, args.n, args.ar, args.no_bind, args.create_fileview

    # Configure Synapse client for production stack
    syn = synapseclient.Synapse()
    syn.repoEndpoint = 'https://repo-prod.prod.sagebase.org/repo/v1'
    syn.authEndpoint = 'https://repo-prod.prod.sagebase.org/auth/v1'
    syn.fileHandleEndpoint = 'https://repo-prod.prod.sagebase.org/file/v1'
    syn.portalEndpoint = 'https://repo-prod.prod.sagebase.org/portal/v1'
    
    print(f"Configured for production stack: {syn.repoEndpoint}")

    if no_bind is not None:
        print(f"Warning ❗❗❗ Schema will not be bound to the entity if one was provided.")
        print(f"✅ Skipping login since --no_bind flag is set")
    else:
        # Only login if we're actually going to bind
        print(f"Logging in to production stack...")
        syn.login()
        print(f"Connected to production stack: {syn.repoEndpoint}")
        syn.get_available_services()
        schema_service = syn.service("json_schema")
        service, org, schema_org_name = get_schema_organization(schema_service, org_name)
    
    if no_bind is None:
        get_register_bind_schema(syn, target, schema_org_name, org, service, path, url, includes_ar, no_bind, create_fileview)
    else:
        print(f"✅ Schema processing completed (no binding due to --no_bind flag)")
    
    if target is None and no_bind is None:
        print(f"\n❗❗❗ No dataset information provided.❗❗❗\nPlease check your command line inputs and try again.")

if __name__ == "__main__":
    main() 