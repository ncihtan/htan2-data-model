#!/usr/bin/env python3
"""Setup HTAN2 JSON Schema Organization in Synapse.

This script creates the HTAN2 organization for JSON schemas and sets up
the initial folder structure for data validation.
"""

import argparse
import synapseclient
import os
from pathlib import Path


def setup_synapse_organization(org_name: str = "HTAN2", create_folders: bool = True):
    """Set up the HTAN2 organization and folder structure in Synapse.
    
    Args:
        org_name: Name of the organization to create
        create_folders: Whether to create initial folder structure
    """
    
    # Configure Synapse client for production stack
    syn = synapseclient.Synapse()
    syn.repoEndpoint = 'https://repo-prod.prod.sagebase.org/repo/v1'
    syn.authEndpoint = 'https://repo-prod.prod.sagebase.org/auth/v1'
    syn.fileHandleEndpoint = 'https://repo-prod.prod.sagebase.org/file/v1'
    syn.portalEndpoint = 'https://repo-prod.prod.sagebase.org/portal/v1'
    
    print(f"Configuring for production stack: {syn.repoEndpoint}")
    
    # Login to Synapse
    print("Logging in to Synapse...")
    syn.login()
    print("Successfully logged in to Synapse")
    
    # Get available services
    syn.get_available_services()
    schema_service = syn.service("json_schema")
    
    # Create or get the organization
    print(f"Setting up organization: {org_name}")
    try:
        schema_org = schema_service.JsonSchemaOrganization(name=org_name)
        schema_org.create()
        print(f"✅ Created new organization: {org_name}")
    except synapseclient.core.exceptions.SynapseHTTPError as e:
        if "already exists" in str(e):
            print(f"✅ Organization {org_name} already exists")
            schema_org = schema_service.get_organization(organization_name=org_name)
        else:
            raise e
    
    if create_folders:
        # Create initial folder structure for data validation
        print("Creating initial folder structure...")
        
        # Create a project for HTAN2 data
        project_name = "HTAN2 Data Validation Project"
        project_description = """
        This project contains folders for HTAN2 data validation using JSON schemas.
        Each folder is bound to a specific schema for validation.
        """
        
        try:
            project = syn.store(
                synapseclient.Project(
                    name=project_name,
                    description=project_description
                )
            )
            print(f"✅ Created project: {project_name} (ID: {project.id})")
        except Exception as e:
            print(f"⚠️  Project creation failed: {e}")
            return
        
        # Create folders for different data types
        folders = [
            {
                "name": "Clinical Data",
                "description": "Clinical data files validated against HTAN2 clinical schema"
            },
            {
                "name": "Biospecimen Data", 
                "description": "Biospecimen data files validated against HTAN2 biospecimen schema"
            },
            {
                "name": "Participant Data",
                "description": "Participant data files validated against HTAN2 participant schema"
            },
            {
                "name": "Sequencing Data",
                "description": "Sequencing data files validated against HTAN2 sequencing schema"
            },
            {
                "name": "WES Data",
                "description": "Whole Exome Sequencing data files validated against HTAN2 WES schema"
            },
            {
                "name": "scRNA-seq Data",
                "description": "Single-cell RNA sequencing data files validated against HTAN2 scRNA-seq schema"
            }
        ]
        
        for folder_info in folders:
            try:
                folder = syn.store(
                    synapseclient.Folder(
                        name=folder_info["name"],
                        description=folder_info["description"],
                        parent=project
                    )
                )
                print(f"✅ Created folder: {folder_info['name']} (ID: {folder.id})")
            except Exception as e:
                print(f"⚠️  Folder creation failed for {folder_info['name']}: {e}")
        
        print(f"\n🎉 Setup complete!")
        print(f"Organization: {org_name}")
        print(f"Project ID: {project.id}")
        print(f"Project URL: https://www.synapse.org/#!Synapse:{project.id}")
        print(f"\nNext steps:")
        print(f"1. Run the GitHub Action to generate and register JSON schemas")
        print(f"2. Bind the schemas to the appropriate folders")
        print(f"3. Upload test data files to validate the schemas")


def main():
    parser = argparse.ArgumentParser(
        description="Set up HTAN2 JSON Schema Organization in Synapse"
    )
    parser.add_argument(
        "--org-name",
        type=str,
        default="HTAN2",
        help="Name of the organization to create (default: HTAN2)"
    )
    parser.add_argument(
        "--no-folders",
        action="store_true",
        help="Skip creating folder structure"
    )
    
    args = parser.parse_args()
    
    setup_synapse_organization(
        org_name=args.org_name,
        create_folders=not args.no_folders
    )


if __name__ == "__main__":
    main()
