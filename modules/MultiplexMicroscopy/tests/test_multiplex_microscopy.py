"""Tests for the Multiplex Microscopy module."""

import pytest
from linkml_runtime import SchemaView
from linkml_runtime.utils.introspection import package_schemaview


class TestMultiplexMicroscopy:
    """Test cases for the Multiplex Microscopy module."""

    def test_schema_loads(self):
        """Test that the schema loads without errors."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        assert sv is not None

    def test_required_attributes_level2(self):
        """Test that required attributes are properly marked for Level 2."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        # Get all slots including inherited ones
        all_slots = sv.class_slots("MultiplexMicroscopyLevel2")
        
        # Check that key required attributes are present (including inherited from BaseImagingAttributes)
        required_attrs = [
            "EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES",  # From BaseImagingAttributes
            "DE_IDENTIFICATION_METHOD_TYPE",  # From BaseImagingAttributes
            "LICENSE",  # From BaseImagingAttributes
            "IMAGE_MODALITY",  # From BaseImagingAttributes
            "IMAGING_EQUIPMENT_MANUFACTURER",  # From BaseImagingAttributes
            "CITATION_OR_DOI",  # From BaseImagingAttributes
            "STAINING_METHOD",  # From BaseImagingAttributes
            "OBJECTIVE",  # From BaseImagingAttributes
            "NOMINAL_MAGNIFICATION",  # From BaseImagingAttributes
            "IMAGING_ASSAY_TYPE",  # MultiplexMicroscopy specific
            "PHYSICAL_SIZE_X",  # MultiplexMicroscopy specific
            "PHYSICAL_SIZE_Y",  # MultiplexMicroscopy specific
            "SIZE_X",  # MultiplexMicroscopy specific
            "SIZE_Y",  # MultiplexMicroscopy specific
            "SIZE_T",  # MultiplexMicroscopy specific
            "CHANNEL_METADATA_ID"  # MultiplexMicroscopy specific
        ]
        
        for attr in required_attrs:
            assert attr in all_slots, f"Required attribute {attr} not found"
            slot = sv.get_slot(attr)
            assert slot.required is True, f"Attribute {attr} should be required"

    def test_level3_class(self):
        """Test that Level 3 class is properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        level3_class = sv.get_class("MultiplexMicroscopyLevel3")
        assert level3_class is not None
        
        # Get all slots including inherited ones
        all_slots = sv.class_slots("MultiplexMicroscopyLevel3")
        
        # Check required attributes
        assert "SEGMENTATION_WORKFLOW_TYPE" in all_slots
        assert "SEGMENTATION_METHOD" in all_slots
        assert "FILE_FORMAT" in all_slots
        
        # Check that required attributes are marked as required
        seg_workflow_slot = sv.get_slot("SEGMENTATION_WORKFLOW_TYPE")
        assert seg_workflow_slot.required is True
        
        seg_method_slot = sv.get_slot("SEGMENTATION_METHOD")
        assert seg_method_slot.required is True
        
        # Check file format pattern (may be defined in level_3.yaml)
        file_format_slot = sv.get_slot("FILE_FORMAT")
        if file_format_slot.pattern:
            assert "ome-tiff" in file_format_slot.pattern or "ome\\.tiff" in file_format_slot.pattern

    def test_level4_class(self):
        """Test that Level 4 class is properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        level4_class = sv.get_class("MultiplexMicroscopyLevel4")
        assert level4_class is not None
        
        # Get all slots including inherited ones
        all_slots = sv.class_slots("MultiplexMicroscopyLevel4")
        
        # Check required attributes
        assert "FEATURE_EXTRACTION_WORKFLOW_TYPE" in all_slots
        assert "MATRIX_TYPE" in all_slots
        assert "FEATURE_EXTRACTION_METHOD" in all_slots
        assert "FILE_FORMAT" in all_slots
        
        # Check that required attributes are marked as required
        feature_workflow_slot = sv.get_slot("FEATURE_EXTRACTION_WORKFLOW_TYPE")
        assert feature_workflow_slot.required is True
        
        matrix_type_slot = sv.get_slot("MATRIX_TYPE")
        assert matrix_type_slot.required is True
        
        feature_method_slot = sv.get_slot("FEATURE_EXTRACTION_METHOD")
        assert feature_method_slot.required is True
        
        # Check file format pattern (may be defined in level_4.yaml)
        file_format_slot = sv.get_slot("FILE_FORMAT")
        if file_format_slot.pattern:
            assert "csv" in file_format_slot.pattern or "h5ad" in file_format_slot.pattern

    def test_enum_values(self):
        """Test that enum values are properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        # Test ImagingAssayType enum
        assay_enum = sv.get_enum("ImagingAssayType")
        assert "H&E" in assay_enum.permissible_values
        assert "IHC" in assay_enum.permissible_values
        assert "CyCIF" in assay_enum.permissible_values
        assert "Not Applicable" in assay_enum.permissible_values

    def test_validation_patterns(self):
        """Test that validation patterns are properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        # Note: ORGAN_OR_TISSUE is a biospecimen attribute, not an imaging attribute
        # It should be retrieved from the Biospecimen record via HTAN_PARENT_ID
        
        # Test Synapse ID pattern for CHANNEL_METADATA_ID
        channel_metadata_id_slot = sv.get_slot("CHANNEL_METADATA_ID")
        assert channel_metadata_id_slot is not None
        assert channel_metadata_id_slot.pattern == "^syn\\d+$"

    def test_minimum_values(self):
        """Test that minimum value constraints are properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        # Test NOMINAL_MAGNIFICATION minimum (RFC indicates 0 to inf, integer)
        mag_slot = sv.get_slot("NOMINAL_MAGNIFICATION")
        assert mag_slot.minimum_value == 0
        assert mag_slot.range == "integer"
        
        # Test LENS_NUMERICAL_APERTURE minimum
        na_slot = sv.get_slot("LENS_NUMERICAL_APERTURE")
        assert na_slot.minimum_value == 0.0
        
        # Test SIZE_X minimum
        size_x_slot = sv.get_slot("SIZE_X")
        assert size_x_slot.minimum_value == 1


