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
        
        level2_class = sv.get_class("MultiplexMicroscopyLevel2")
        required_slots = [slot for slot in level2_class.attributes if level2_class.attributes[slot].required]
        
        # Check that key required attributes are present
        required_names = [sv.get_slot(slot).name for slot in required_slots]
        
        assert "EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES" in required_names
        assert "DE_IDENTIFICATION_METHOD_TYPE" in required_names
        assert "LICENSE" in required_names
        assert "IMAGE_MODALITY" in required_names
        assert "IMAGING_EQUIPMENT_MANUFACTURER" in required_names
        assert "CITATION_OR_DOI" in required_names
        assert "STAINING_METHOD" in required_names
        assert "OBJECTIVE" in required_names
        assert "NOMINAL_MAGNIFICATION" in required_names
        assert "IMAGING_ASSAY_TYPE" in required_names
        assert "PHYSICAL_SIZE_X" in required_names
        assert "PHYSICAL_SIZE_Y" in required_names
        assert "SIZE_X" in required_names
        assert "SIZE_Y" in required_names
        assert "SIZE_T" in required_names
        assert "CHANNEL_METADATA_ID" in required_names

    def test_level3_class(self):
        """Test that Level 3 class is properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        level3_class = sv.get_class("MultiplexMicroscopyLevel3")
        assert level3_class is not None
        
        # Check required attributes
        required_slots = [slot for slot in level3_class.attributes if level3_class.attributes[slot].required]
        required_names = [sv.get_slot(slot).name for slot in required_slots]
        
        assert "SEGMENTATION_WORKFLOW_TYPE" in required_names
        assert "SEGMENTATION_METHOD" in required_names
        assert "FILE_FORMAT" in required_names
        
        # Check file format pattern
        file_format_slot = sv.get_slot("FILE_FORMAT")
        assert "ome-tiff" in file_format_slot.pattern or "ome\\.tiff" in file_format_slot.pattern

    def test_level4_class(self):
        """Test that Level 4 class is properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        level4_class = sv.get_class("MultiplexMicroscopyLevel4")
        assert level4_class is not None
        
        # Check required attributes
        required_slots = [slot for slot in level4_class.attributes if level4_class.attributes[slot].required]
        required_names = [sv.get_slot(slot).name for slot in required_slots]
        
        assert "FEATURE_EXTRACTION_WORKFLOW_TYPE" in required_names
        assert "MATRIX_TYPE" in required_names
        assert "FEATURE_EXTRACTION_METHOD" in required_names
        assert "FILE_FORMAT" in required_names
        
        # Check file format pattern
        file_format_slot = sv.get_slot("FILE_FORMAT")
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
        
        # Test ICD-O pattern for organ_or_tissue
        organ_tissue_slot = sv.get_slot("ORGAN_OR_TISSUE")
        assert organ_tissue_slot.pattern == "^[A-Z][0-9]{2}\\.[0-9]{1,2}$"
        
        # Test RRID pattern for channel metadata
        rrid_slot = sv.get_slot("RRID_IDENTIFIER")
        assert rrid_slot.pattern == "^RRID:AB_\\d+$"

    def test_minimum_values(self):
        """Test that minimum value constraints are properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        # Test NOMINAL_MAGNIFICATION minimum
        mag_slot = sv.get_slot("NOMINAL_MAGNIFICATION")
        assert mag_slot.minimum_value == 1.0
        
        # Test LENS_NUMERICAL_APERTURE minimum
        na_slot = sv.get_slot("LENS_NUMERICAL_APERTURE")
        assert na_slot.minimum_value == 0.0
        
        # Test SIZE_X minimum
        size_x_slot = sv.get_slot("SIZE_X")
        assert size_x_slot.minimum_value == 1

    def test_channel_metadata_class(self):
        """Test that ChannelMetadata class is properly defined."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        channel_metadata_class = sv.get_class("ChannelMetadata")
        assert channel_metadata_class is not None
        
        # Check required attributes
        required_slots = [slot for slot in channel_metadata_class.attributes if channel_metadata_class.attributes[slot].required]
        required_names = [sv.get_slot(slot).name for slot in required_slots]
        
        assert "CHANNEL_ID" in required_names
        assert "CHANNEL_NAME" in required_names
        assert "TARGET_NAME" in required_names

    def test_multivalued_channel_metadata(self):
        """Test that CHANNEL_METADATA is properly marked as multivalued."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        
        channel_metadata_slot = sv.get_slot("CHANNEL_METADATA")
        assert channel_metadata_slot.multivalued is True

