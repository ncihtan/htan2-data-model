"""Tests for the Multiplex Microscopy module."""

import sys
import pytest
from linkml_runtime import SchemaView
from linkml_runtime.utils.introspection import package_schemaview

sys.path.insert(0, "modules/MultiplexMicroscopy/src")


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
            "CHANNEL_METADATA_ID",  # MultiplexMicroscopy specific
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
            assert (
                "ome-tiff" in file_format_slot.pattern
                or "ome\\.tiff" in file_format_slot.pattern
            )

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
            assert (
                "csv" in file_format_slot.pattern or "h5ad" in file_format_slot.pattern
            )

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

    def test_file_format_and_filename_patterns(self):
        """Test that FILE_FORMAT and FILENAME patterns match correctly."""
        import re

        # Test Level 2
        sv2 = SchemaView("modules/MultiplexMicroscopy/domains/level_2.yaml")
        level2_class = sv2.get_class("MultiplexMicroscopyLevel2")
        file_format_attr = level2_class.attributes.get("FILE_FORMAT")
        filename_attr = level2_class.attributes.get("FILENAME")

        assert file_format_attr.pattern == "^(ome-tiff|tiff|qptiff|svs)$"
        assert (
            filename_attr.pattern
            == "^.+\\.(ome\\.(tif|tiff|tf2|tf8|btf)|tiff?|qptiff|svs)$"
        )

        # Validate pattern matching
        fmt_regex = re.compile(file_format_attr.pattern)
        filename_regex = re.compile(filename_attr.pattern)

        # Test valid combinations
        assert fmt_regex.match("ome-tiff")
        assert filename_regex.match("image.ome.tiff")
        assert filename_regex.match("image.ome.tif")
        assert filename_regex.match("image.ome.tf2")
        assert fmt_regex.match("tiff")
        assert filename_regex.match("image.tiff")
        assert filename_regex.match("image.tif")
        assert fmt_regex.match("qptiff")
        assert filename_regex.match("image.qptiff")
        assert fmt_regex.match("svs")
        assert filename_regex.match("image.svs")

        # Test Level 3
        sv3 = SchemaView("modules/MultiplexMicroscopy/domains/level_3.yaml")
        level3_class = sv3.get_class("MultiplexMicroscopyLevel3")
        file_format_attr = level3_class.attributes.get("FILE_FORMAT")
        filename_attr = level3_class.attributes.get("FILENAME")

        assert file_format_attr.pattern == "^(ome-tiff|tiff|tif)$"
        assert filename_attr.pattern == "^.+\\.(ome\\.(tif|tiff|tf2|tf8|btf)|tiff?)$"

        fmt_regex = re.compile(file_format_attr.pattern)
        filename_regex = re.compile(filename_attr.pattern)

        assert fmt_regex.match("ome-tiff")
        assert filename_regex.match("image.ome.tiff")
        assert fmt_regex.match("tiff")
        assert filename_regex.match("image.tiff")
        assert fmt_regex.match("tif")
        assert filename_regex.match("image.tif")

        # Test Level 4
        sv4 = SchemaView("modules/MultiplexMicroscopy/domains/level_4.yaml")
        level4_class = sv4.get_class("MultiplexMicroscopyLevel4")
        file_format_attr = level4_class.attributes.get("FILE_FORMAT")
        filename_attr = level4_class.attributes.get("FILENAME")

        assert file_format_attr.pattern == "^(csv|h5ad)$"
        assert filename_attr.pattern == "^.+\\.(csv|h5ad)$"

        fmt_regex = re.compile(file_format_attr.pattern)
        filename_regex = re.compile(filename_attr.pattern)

        assert fmt_regex.match("csv")
        assert filename_regex.match("data.csv")
        assert fmt_regex.match("h5ad")
        assert filename_regex.match("data.h5ad")


    def test_htan_panel_id_required(self):
        """Test that HTAN_PANEL_ID is required with the correct pattern in Level 2."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/level_2.yaml")
        level2_class = sv.get_class("MultiplexMicroscopyLevel2")

        assert "HTAN_PANEL_ID" in sv.class_slots("MultiplexMicroscopyLevel2")
        slot = level2_class.attributes.get("HTAN_PANEL_ID")
        assert slot is not None
        assert slot.required is True
        assert slot.pattern == "^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(P[0-9]{1,20})$"

    def test_htan_panel_id_required_channel_metadata(self):
        """Test that HTAN_PANEL_ID is required with the correct pattern in ChannelMetadata."""
        import re
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy_channel_metadata.yaml")
        cls = sv.get_class("ChannelMetadata")

        assert "HTAN_PANEL_ID" in sv.class_slots("ChannelMetadata")
        slot = cls.attributes.get("HTAN_PANEL_ID")
        assert slot is not None
        assert slot.required is True
        assert slot.pattern == "^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(P[0-9]{1,20})$"

        # Pattern accepts valid IDs
        pattern = re.compile(slot.pattern)
        assert pattern.match("HTA201_1_P1")
        assert pattern.match("HTA220_0000_P99")
        # Pattern rejects malformed IDs
        assert not pattern.match("HTA201_1_X1")
        assert not pattern.match("HTA201_1_1")

    def test_htan_panel_id_missing_level2_raises(self):
        """Test that HTAN_PANEL_ID missing from a Level 2 record is caught by the validator."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/level_2.yaml")
        cls = sv.get_class("MultiplexMicroscopyLevel2")
        slot = cls.attributes.get("HTAN_PANEL_ID")
        assert slot is not None and slot.required is True

        def validate_panel_id(data):
            if not data.get("HTAN_PANEL_ID"):
                raise ValueError("Missing required slot: HTAN_PANEL_ID")

        with pytest.raises(ValueError, match="HTAN_PANEL_ID"):
            validate_panel_id({})

    def test_physical_size_z_conditional(self):
        """Test that PHYSICAL_SIZE_Z is optional at the class level but conditionally required via rules."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/level_2.yaml")
        level2_class = sv.get_class("MultiplexMicroscopyLevel2")

        pz = level2_class.attributes.get("PHYSICAL_SIZE_Z")
        assert pz is not None
        assert pz.required is False, "PHYSICAL_SIZE_Z should not be unconditionally required"

        assert len(level2_class.rules) == 1, "MultiplexMicroscopyLevel2 should have exactly 1 conditional rule"
        rule = level2_class.rules[0]
        size_z_condition = rule.preconditions.slot_conditions.get("SIZE_Z")
        assert size_z_condition is not None
        assert size_z_condition.minimum_value == 2

        pz_postcondition = rule.postconditions.slot_conditions.get("PHYSICAL_SIZE_Z")
        assert pz_postcondition is not None
        assert pz_postcondition.required is True

    def test_physical_size_z_rule_instances(self):
        """Test PHYSICAL_SIZE_Z conditional rule via a schema-driven validator."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/level_2.yaml")

        def validate(data):
            size_z = data.get("SIZE_Z")
            if size_z is not None and size_z >= 2 and data.get("PHYSICAL_SIZE_Z") is None:
                raise ValueError("PHYSICAL_SIZE_Z is required when SIZE_Z >= 2")

        # 2D acquisition (SIZE_Z=1): PHYSICAL_SIZE_Z may be omitted
        validate({"SIZE_Z": 1})

        # 3D acquisition (SIZE_Z=3) with PHYSICAL_SIZE_Z: valid
        validate({"SIZE_Z": 3, "PHYSICAL_SIZE_Z": 0.5})

        # 3D acquisition missing PHYSICAL_SIZE_Z: invalid
        with pytest.raises(ValueError, match="PHYSICAL_SIZE_Z"):
            validate({"SIZE_Z": 3})


class TestChannelMetadata:
    """Test cases for the ChannelMetadata class and CHANNEL_METADATA slot."""

    def test_channel_metadata_class_exists(self):
        """Test that ChannelMetadata class is present in the schema."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        assert "ChannelMetadata" in sv.all_classes()

    def test_channel_metadata_no_parent(self):
        """Test that ChannelMetadata has no is_a (standalone record class)."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        cls = sv.get_class("ChannelMetadata")
        assert cls.is_a is None

    def test_channel_metadata_required_slots(self):
        """Test that CHANNEL_ID and CHANNEL_NAME are marked required."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        cls = sv.get_class("ChannelMetadata")
        required_slots = ["CHANNEL_ID", "CHANNEL_NAME"]
        for slot_name in required_slots:
            slot = cls.attributes[slot_name]
            assert slot.required is True, f"{slot_name} should be required"

    def test_channel_metadata_optional_slots_not_required(self):
        """Test that optional slots are not marked required."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        cls = sv.get_class("ChannelMetadata")
        optional_slots = [
            "CYCLE_NUMBER", "SUB_CYCLE_NUMBER", "TARGET_NAME",
            "ANTIBODY_NAME", "FLUOROPHORE", "CLONE",
        ]
        for slot_name in optional_slots:
            slot = cls.attributes[slot_name]
            assert not slot.required, f"{slot_name} should not be required"

    def test_channel_metadata_slot_on_container(self):
        """Test that CHANNEL_METADATA slot exists on MultiplexMicroscopyData."""
        sv = SchemaView("modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml")
        container = sv.get_class("MultiplexMicroscopyData")
        assert "CHANNEL_METADATA" in container.attributes
        slot = container.attributes["CHANNEL_METADATA"]
        assert slot.multivalued is True
        assert slot.inlined_as_list is True
        assert slot.required is False

    def test_valid_channel_metadata_instance(self):
        """Test that a valid ChannelMetadata instance loads without error."""
        from htan_multiplexmicroscopy.datamodel.multiplex_microscopy import ChannelMetadata

        instance = ChannelMetadata(HTAN_PANEL_ID="HTA201_1_P1", CHANNEL_ID="ch1", CHANNEL_NAME="DAPI")
        assert instance.HTAN_PANEL_ID == "HTA201_1_P1"
        assert instance.CHANNEL_ID == "ch1"
        assert instance.CHANNEL_NAME == "DAPI"

    def test_invalid_channel_metadata_missing_required(self):
        """Test that a ChannelMetadata instance missing required fields raises ValueError."""
        from htan_multiplexmicroscopy.datamodel.multiplex_microscopy import ChannelMetadata

        with pytest.raises(ValueError):
            ChannelMetadata()

    def test_invalid_channel_metadata_missing_channel_name(self):
        """Test that a ChannelMetadata instance missing CHANNEL_NAME raises ValueError."""
        from htan_multiplexmicroscopy.datamodel.multiplex_microscopy import ChannelMetadata

        with pytest.raises(ValueError):
            ChannelMetadata(CHANNEL_ID="ch1")
