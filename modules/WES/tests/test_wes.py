"""Tests for the HTAN WES module."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


class TestWESModule:
    """Test cases for the WES module."""

    def test_schema_loading(self):
        """Test that the WES schema can be loaded."""
        schema_path = "modules/WES/domains/wes.yaml"
        sv = SchemaView(schema_path)
        assert sv is not None

    def test_level_1_schema(self):
        """Test Level 1 schema structure."""
        schema_path = "modules/WES/domains/level_1.yaml"
        sv = SchemaView(schema_path)
        
        # Check that the main class exists
        assert "BulkWESLevel1" in sv.all_classes()
        
        # Check that it inherits from BaseSequencingAttributes
        level1_class = sv.get_class("BulkWESLevel1")
        assert level1_class.is_a == "BaseSequencingAttributes"
        
        # Check WES Level 1 specific required attributes (base attributes come from inheritance)
        wes_specific_attrs = ["LIBRARY_SELECTION_METHOD", "READ_LENGTH"]
        
        for attr in wes_specific_attrs:
            assert attr in level1_class.attributes

    def test_level_2_schema(self):
        """Test Level 2 schema structure."""
        schema_path = "modules/WES/domains/level_2.yaml"
        sv = SchemaView(schema_path)
        
        # Check that the main class exists
        assert "BulkWESLevel2" in sv.all_classes()
        
        # Check that it inherits from BaseSequencingAttributes
        level2_class = sv.get_class("BulkWESLevel2")
        assert level2_class.is_a == "BaseSequencingAttributes"
        
        # Check WES Level 2 specific required attributes (base attributes come from inheritance)
        wes_specific_attrs = ["ALIGNMENT_WORKFLOW_TYPE", "MEAN_COVERAGE"]
        
        for attr in wes_specific_attrs:
            assert attr in level2_class.attributes

    def test_level_3_schema(self):
        """Test Level 3 schema structure."""
        schema_path = "modules/WES/domains/level_3.yaml"
        sv = SchemaView(schema_path)
        
        # Check that the main class exists
        assert "BulkWESLevel3" in sv.all_classes()
        
        # Check that it inherits from BaseSequencingAttributes
        level3_class = sv.get_class("BulkWESLevel3")
        assert level3_class.is_a == "BaseSequencingAttributes"
        
        # Check WES Level 3 specific required attributes (base attributes come from inheritance)
        wes_specific_attrs = ["SOMATIC_VARIANTS_WORKFLOW_TYPE"]
        
        for attr in wes_specific_attrs:
            assert attr in level3_class.attributes

    def test_enums(self):
        """Test that enums are properly defined."""
        # Test Level 1 enums (base enums come from BaseSequencingAttributes)
        sv1 = SchemaView("modules/WES/domains/level_1.yaml")
        assert "LibrarySelectionMethodEnum" in sv1.all_enums()
        # LibraryLayoutEnum and SequencingPlatformEnum come from base sequencing module
        
        # Test Level 2 enums
        sv2 = SchemaView("modules/WES/domains/level_2.yaml")
        # Note: MSIStatusEnum was moved to Level 3
        # assert "MSIStatusEnum" in sv2.all_enums()
        
        # Test Level 3 enums
        sv3 = SchemaView("modules/WES/domains/level_3.yaml")
        assert "SomaticVariantsSampleTypeEnum" in sv3.all_enums()
        assert "MSIStatusEnum" in sv3.all_enums()
