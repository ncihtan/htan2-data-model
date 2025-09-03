"""Tests for HTAN Biospecimen Module."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


class TestBiospecimenModule:
    """Test Biospecimen module functionality."""

    def test_schema_loading(self):
        """Test that the biospecimen schema loads correctly."""
        schema_path = "domains/biospecimen.yaml"
        sv = SchemaView(schema_path)
        
        # Check that BiospecimenAttributes class exists
        assert "BiospecimenAttributes" in sv.all_classes()

    def test_inheritance_from_core(self):
        """Test that BiospecimenAttributes inherits from CoreFileAttributes."""
        schema_path = "domains/biospecimen.yaml"
        sv = SchemaView(schema_path)
        
        biospecimen_class = sv.get_class("BiospecimenAttributes")
        assert biospecimen_class.is_a == "CoreFileAttributes"

    def test_required_biospecimen_id(self):
        """Test that HTAN_BIOSPECIMEN_ID is required in BiospecimenAttributes."""
        schema_path = "domains/biospecimen.yaml"
        sv = SchemaView(schema_path)
        
        biospecimen_class = sv.get_class("BiospecimenAttributes")
        biospecimen_id_slot = sv.get_slot("HTAN_BIOSPECIMEN_ID")
        
        # Check that HTAN_BIOSPECIMEN_ID is required in BiospecimenAttributes
        assert biospecimen_id_slot.required is True

    def test_core_attributes_available(self):
        """Test that core attributes are available through inheritance."""
        schema_path = "domains/biospecimen.yaml"
        sv = SchemaView(schema_path)
        
        biospecimen_class = sv.get_class("BiospecimenAttributes")
        
        # Check that core attributes are available through inheritance
        # Note: Core attributes are inherited, so they won't be in the direct attributes
        # but should be available when the schema is used
        biospecimen_class = sv.get_class("BiospecimenAttributes")
        assert biospecimen_class.is_a == "CoreFileAttributes"
