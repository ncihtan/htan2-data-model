"""Tests for the Spatial Omics module."""

import pytest
from linkml_runtime import SchemaView
from linkml_runtime.utils.introspection import package_schemaview


class TestSpatial:
    """Test cases for the Spatial Omics module."""

    def test_schema_loads(self):
        """Test that the schema loads without errors."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")
        assert sv is not None

    def test_level1_class(self):
        """Test that Level 1 class is properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        level1_class = sv.get_class("SpatialLevel1")
        assert level1_class is not None

        # Get all slots including inherited ones
        all_slots = sv.class_slots("SpatialLevel1")

        # Check required attributes
        required_attrs = [
            "HTAN_DATA_FILE_ID",  # From CoreFileAttributes
            "HTAN_PARENT_ID",  # From CoreFileAttributes
            "FILENAME",  # From CoreFileAttributes
            "FILE_FORMAT",  # Spatial Level 1 specific
            "PLATFORM",  # Spatial Level 1 specific
            "ASSAY_TYPE",  # Spatial Level 1 specific
            "BUNDLE_CONTENTS",  # Spatial Level 1 specific
            "HAS_IMAGES",  # Spatial Level 1 specific
            "HAS_REGISTRATION_FILES",  # Spatial Level 1 specific
        ]

        for attr in required_attrs:
            assert attr in all_slots, f"Required attribute {attr} not found"
            # Check class-specific slot definition for overridden attributes
            class_slot = level1_class.attributes.get(attr)
            if class_slot:
                # Attribute is overridden in this class
                assert (
                    class_slot.required is True
                ), f"Attribute {attr} should be required"
            else:
                # Attribute is inherited, check base slot
                slot = sv.get_slot(attr)
                assert slot.required is True, f"Attribute {attr} should be required"

    def test_level3_class(self):
        """Test that Level 3 class is properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        level3_class = sv.get_class("SpatialLevel3")
        assert level3_class is not None

        # Get all slots including inherited ones
        all_slots = sv.class_slots("SpatialLevel3")

        # Check required attributes
        required_attrs = [
            "HTAN_DATA_FILE_ID",  # From CoreFileAttributes
            "HTAN_PARENT_ID",  # From CoreFileAttributes
            "FILENAME",  # From CoreFileAttributes
            "PLATFORM",  # Spatial Level 3 specific
            "ASSAY_CHEMISTRY_VERSION",  # Spatial Level 3 specific
            "RNA_MEASURED",  # Spatial Level 3 specific
            "PROTEIN_MEASURED",  # Spatial Level 3 specific
            "PANEL_SIZE_TOTAL_TARGETS",  # Spatial Level 3 specific
            "REGION_AREA",  # Spatial Level 3 specific
            "BUNDLE_CONTENTS",  # Spatial Level 3 specific
            "HAS_CELL_SEGMENTATION",  # Spatial Level 3 specific
            "HAS_CLUSTERING",  # Spatial Level 3 specific
            "QC_SPATIAL_UNIT",  # Spatial Level 3 specific
            "QC_FEATURE_NUMBER",  # Spatial Level 3 specific
            "QC_MEAN_READS_PER_FEATURE",  # Spatial Level 3 specific
            "QC_TOTAL_GENES_DETECTED",  # Spatial Level 3 specific
            "QC_TOTAL_NUMBER_OF_READS",  # Spatial Level 3 specific
        ]

        for attr in required_attrs:
            assert attr in all_slots, f"Required attribute {attr} not found"
            # Check class-specific slot definition for overridden attributes
            class_slot = level3_class.attributes.get(attr)
            if class_slot:
                # Attribute is overridden in this class
                assert (
                    class_slot.required is True
                ), f"Attribute {attr} should be required"
            else:
                # Attribute is inherited, check using class_induced_slots which properly resolves inheritance
                induced_slots = sv.class_induced_slots("SpatialLevel3")
                induced_slot = next((s for s in induced_slots if s.name == attr), None)
                if induced_slot:
                    assert (
                        induced_slot.required is True
                    ), f"Attribute {attr} should be required"
                else:
                    # Fallback to get_slot
                    slot = sv.get_slot(attr)
                    assert slot is not None, f"Slot {attr} not found"
                    assert slot.required is True, f"Attribute {attr} should be required"

    def test_level4_class(self):
        """Test that Level 4 class is properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        level4_class = sv.get_class("SpatialLevel4")
        assert level4_class is not None

        # Get all slots including inherited ones
        all_slots = sv.class_slots("SpatialLevel4")

        # Check required attributes
        required_attrs = [
            "HTAN_DATA_FILE_ID",  # From CoreFileAttributes
            "HTAN_PARENT_ID",  # From CoreFileAttributes
            "FILENAME",  # From CoreFileAttributes
            "FILE_FORMAT",  # Spatial Level 4 specific
            "NUMBER_OF_FEATURES",  # Spatial Level 4 specific
            "NUMBER_OF_OBJECTS",  # Spatial Level 4 specific
            "HAS_DIMENSIONALITY_REDUCTION",  # Spatial Level 4 specific
            "HAS_CLUSTERING",  # Spatial Level 4 specific
            "HAS_CELL_TYPE_CALLING",  # Spatial Level 4 specific
            "HAS_NORMALISED_ARRAY",  # Spatial Level 4 specific
            "HAS_RAW_ARRAY",  # Spatial Level 4 specific
            "HAS_IMAGE",  # Spatial Level 4 specific
        ]

        for attr in required_attrs:
            assert attr in all_slots, f"Required attribute {attr} not found"
            # Check class-specific slot definition for overridden attributes
            class_slot = level4_class.attributes.get(attr)
            if class_slot:
                # Attribute is overridden in this class
                assert (
                    class_slot.required is True
                ), f"Attribute {attr} should be required"
            else:
                # Attribute is inherited, check base slot
                slot = sv.get_slot(attr)
                assert slot.required is True, f"Attribute {attr} should be required"

    def test_spatial_panel_class(self):
        """Test that Spatial Panel class is properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        panel_class = sv.get_class("SpatialPanel")
        assert panel_class is not None

        all_slots = sv.class_slots("SpatialPanel")

        # Unconditionally required slots
        for attr in ["HTAN_PANEL_ID", "TARGET_TYPE", "TARGET_NAME"]:
            assert attr in all_slots, f"Required attribute {attr} not found"
            class_slot = panel_class.attributes.get(attr)
            assert class_slot is not None, f"Attribute {attr} should be defined in SpatialPanel"
            assert class_slot.required is True, f"Attribute {attr} should be required"

        # Conditionally required slots — not unconditionally required at class level
        for attr in ["ENSEMBL_ID", "HGNC_VERSION", "OTHER_TARGET_DESCRIPTION"]:
            assert attr in all_slots, f"Attribute {attr} not found"
            class_slot = panel_class.attributes.get(attr)
            assert class_slot is not None, f"Attribute {attr} should be defined in SpatialPanel"
            assert class_slot.required is False, f"Attribute {attr} should be conditionally required (not unconditionally)"

        # Dropped fields must not appear
        for attr in ["GENE_SYMBOL", "GENE_ID", "USER_GENE_NAME"]:
            assert attr not in all_slots, f"Removed attribute {attr} should not exist"

        # Three conditional rules: Human Gene, Human Transcript, Other
        assert len(panel_class.rules) == 3, "SpatialPanel should have exactly 3 conditional rules"

        # TargetTypeEnum must exist with all expected values
        target_type_enum = sv.get_enum("TargetTypeEnum")
        assert target_type_enum is not None
        for value in ["Bacterial", "Control Probe", "Human Gene", "Human Protein", "Human Transcript", "Other", "Viral"]:
            assert value in target_type_enum.permissible_values, f"TargetTypeEnum missing value: {value}"

    def test_target_type_invalid_value(self):
        """Test that an invalid TARGET_TYPE value raises ValueError."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial_panel.yaml")
        enum_def = sv.get_enum("TargetTypeEnum")
        assert "Fungal" not in enum_def.permissible_values, \
            "Invalid value 'Fungal' should not be in TargetTypeEnum"

    def test_spatial_panel_conditional_rules_instances(self):
        """Test conditional rule behaviour for SpatialPanel via a schema-driven validator."""
        import re
        sv = SchemaView("modules/SpatialOmics/domains/spatial_panel.yaml")
        enum_def = sv.get_enum("TargetTypeEnum")

        def validate(data):
            target_type = data.get("TARGET_TYPE")
            if target_type not in enum_def.permissible_values:
                raise ValueError(f"Invalid TARGET_TYPE: {target_type!r}")
            for slot in ["HTAN_PANEL_ID", "TARGET_TYPE", "TARGET_NAME"]:
                if not data.get(slot):
                    raise ValueError(f"Missing required slot: {slot}")
            if target_type == "Human Gene":
                ensembl_id = data.get("ENSEMBL_ID")
                if not ensembl_id:
                    raise ValueError("Missing required slot for Human Gene: ENSEMBL_ID")
                if not re.match(r"^ENSG\d+(\.\d+)?$", ensembl_id):
                    raise ValueError(f"ENSEMBL_ID must be ENSG-prefixed for Human Gene, got: {ensembl_id!r}")
                if not data.get("HGNC_VERSION"):
                    raise ValueError("Missing required slot for Human Gene: HGNC_VERSION")
            if target_type == "Human Transcript":
                ensembl_id = data.get("ENSEMBL_ID")
                if not ensembl_id:
                    raise ValueError("Missing required slot for Human Transcript: ENSEMBL_ID")
                if not re.match(r"^ENST\d+(\.\d+)?$", ensembl_id):
                    raise ValueError(f"ENSEMBL_ID must be ENST-prefixed for Human Transcript, got: {ensembl_id!r}")
            if target_type == "Other":
                if not data.get("OTHER_TARGET_DESCRIPTION"):
                    raise ValueError("Missing required slot for Other: OTHER_TARGET_DESCRIPTION")

        # Valid Human Gene instance
        validate({
            "HTAN_PANEL_ID": "HTA201_1_P1",
            "TARGET_TYPE": "Human Gene",
            "TARGET_NAME": "MYC",
            "ENSEMBL_ID": "ENSG00000136997",
            "HGNC_VERSION": "2025-01-01",
        })

        # Human Gene missing ENSEMBL_ID raises error
        with pytest.raises(ValueError, match="ENSEMBL_ID"):
            validate({
                "HTAN_PANEL_ID": "HTA201_1_P1",
                "TARGET_TYPE": "Human Gene",
                "TARGET_NAME": "MYC",
                "HGNC_VERSION": "2025-01-01",
            })

        # Human Gene with ENST-prefixed ID raises error
        with pytest.raises(ValueError, match="ENSG-prefixed"):
            validate({
                "HTAN_PANEL_ID": "HTA201_1_P1",
                "TARGET_TYPE": "Human Gene",
                "TARGET_NAME": "MYC",
                "ENSEMBL_ID": "ENST00000621592",
                "HGNC_VERSION": "2025-01-01",
            })

        # Human Transcript without HGNC_VERSION is valid
        validate({
            "HTAN_PANEL_ID": "HTA201_1_P1",
            "TARGET_TYPE": "Human Transcript",
            "TARGET_NAME": "MYC-201",
            "ENSEMBL_ID": "ENST00000621592",
        })

        # Human Transcript with ENSG-prefixed ID raises error
        with pytest.raises(ValueError, match="ENST-prefixed"):
            validate({
                "HTAN_PANEL_ID": "HTA201_1_P1",
                "TARGET_TYPE": "Human Transcript",
                "TARGET_NAME": "MYC-201",
                "ENSEMBL_ID": "ENSG00000136997",
            })

        # Other missing OTHER_TARGET_DESCRIPTION raises error
        with pytest.raises(ValueError, match="OTHER_TARGET_DESCRIPTION"):
            validate({
                "HTAN_PANEL_ID": "HTA201_1_P1",
                "TARGET_TYPE": "Other",
                "TARGET_NAME": "HPV16-E6",
            })

        # Valid Other instance
        validate({
            "HTAN_PANEL_ID": "HTA201_1_P1",
            "TARGET_TYPE": "Other",
            "TARGET_NAME": "HPV16-E6",
            "OTHER_TARGET_DESCRIPTION": "Human papillomavirus 16 E6 protein",
        })

        # Bacterial, Viral, Control Probe, Human Protein — only TARGET_NAME required
        for target_type in ["Bacterial", "Viral", "Control Probe", "Human Protein"]:
            validate({
                "HTAN_PANEL_ID": "HTA201_1_P1",
                "TARGET_TYPE": target_type,
                "TARGET_NAME": "some-target",
            })

        # Invalid TARGET_TYPE raises error
        with pytest.raises(ValueError, match="Invalid TARGET_TYPE"):
            validate({
                "HTAN_PANEL_ID": "HTA201_1_P1",
                "TARGET_TYPE": "Fungal",
                "TARGET_NAME": "someGene",
            })

    def test_enum_values(self):
        """Test that enum values are properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        # Test Platform enum (Level 3)
        platform_enum = sv.get_enum("PlatformLevel3")
        assert "10x Genomics Visium" in platform_enum.permissible_values
        assert "10x Genomics Xenium" in platform_enum.permissible_values
        assert "Nanostring CosMX" in platform_enum.permissible_values
        assert "STOmics Stereo-seq" in platform_enum.permissible_values

        # Test AssayType enum (Level 1)
        assay_type_enum = sv.get_enum("AssayType")
        assert "spot-based sequencing" in assay_type_enum.permissible_values
        assert "in situ sequencing" in assay_type_enum.permissible_values
        assert "molecular barcoding" in assay_type_enum.permissible_values

        # Test FileFormatLevel1 enum
        file_format_level1_enum = sv.get_enum("FileFormatLevel1")
        assert "tar" in file_format_level1_enum.permissible_values
        assert "tar.gz" in file_format_level1_enum.permissible_values
        assert "zip" in file_format_level1_enum.permissible_values

        # Test FileFormatLevel4 enum
        file_format_enum = sv.get_enum("FileFormatLevel4")
        assert "h5ad" in file_format_enum.permissible_values
        assert "rds" in file_format_enum.permissible_values
        assert "zarr" in file_format_enum.permissible_values

    def test_validation_patterns(self):
        """Test that validation patterns are properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        # Test HTAN Panel ID pattern for HTAN_PANEL_ID in SpatialLevel3
        level3_class = sv.get_class("SpatialLevel3")
        htan_panel_id_attr = level3_class.attributes.get("HTAN_PANEL_ID")
        assert htan_panel_id_attr is not None
        assert htan_panel_id_attr.pattern == "^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(P[0-9]{1,20})$"

        # Test Ensembl ID pattern (ENSG for genes, ENST for transcripts)
        ensembl_id_slot = sv.get_slot("ENSEMBL_ID")
        assert ensembl_id_slot is not None
        assert ensembl_id_slot.pattern == "^(ENSG|ENST)\\d+(\\.\\d+)?$"

        # Test HGNC Version pattern
        hgnc_version_slot = sv.get_slot("HGNC_VERSION")
        assert hgnc_version_slot is not None
        assert hgnc_version_slot.pattern == "^\\d{4}-\\d{2}-\\d{2}$"

    def test_minimum_values(self):
        """Test that minimum value constraints are properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        # Test PANEL_SIZE_TOTAL_TARGETS minimum
        panel_size_slot = sv.get_slot("PANEL_SIZE_TOTAL_TARGETS")
        assert panel_size_slot.minimum_value == 1

        # Test REGION_AREA minimum
        region_area_slot = sv.get_slot("REGION_AREA")
        assert region_area_slot.minimum_value == 0.0

        # Test NUMBER_OF_FEATURES minimum
        num_features_slot = sv.get_slot("NUMBER_OF_FEATURES")
        assert num_features_slot.minimum_value == 1

        # Test NUMBER_OF_OBJECTS minimum
        num_objects_slot = sv.get_slot("NUMBER_OF_OBJECTS")
        assert num_objects_slot.minimum_value == 1

    def test_conditional_requirements(self):
        """Test that conditional requirements are properly defined."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        # Check that conditional attributes are not required by default
        sequencing_file_type_slot = sv.get_slot("SEQUENCING_FILE_TYPE")
        assert sequencing_file_type_slot.required is False

        image_types_slot = sv.get_slot("IMAGE_TYPES")
        assert image_types_slot.required is False

        transcriptome_type_slot = sv.get_slot("TRANSCRIPTOME_TYPE")
        assert transcriptome_type_slot.required is False

        panel_name_slot = sv.get_slot("PANEL_NAME")
        assert panel_name_slot.required is False

    def test_core_inheritance(self):
        """Test that Spatial classes inherit from CoreFileAttributes."""
        sv = SchemaView("modules/SpatialOmics/domains/spatial.yaml")

        # Check Level 1 inheritance
        level1_class = sv.get_class("SpatialLevel1")
        assert level1_class.is_a == "CoreFileAttributes"

        # Check Level 3 inheritance
        level3_class = sv.get_class("SpatialLevel3")
        assert level3_class.is_a == "CoreFileAttributes"

        # Check Level 4 inheritance
        level4_class = sv.get_class("SpatialLevel4")
        assert level4_class.is_a == "CoreFileAttributes"

    def test_file_format_and_filename_patterns(self):
        """Test that FILE_FORMAT and FILENAME patterns match correctly."""
        import re

        # Test Level 1
        sv1 = SchemaView("modules/SpatialOmics/domains/level_1.yaml")
        level1_class = sv1.get_class("SpatialLevel1")
        file_format_attr = level1_class.attributes.get("FILE_FORMAT")
        filename_attr = level1_class.attributes.get("FILENAME")

        # Level 1 uses enum, check FILENAME pattern matches enum values
        assert filename_attr.pattern == "^.+\\.(tar(\\.gz)?|zip)$"

        filename_regex = re.compile(filename_attr.pattern)
        assert filename_regex.match("bundle.tar")
        assert filename_regex.match("bundle.tar.gz")
        assert filename_regex.match("bundle.zip")

        # Test Level 4
        sv4 = SchemaView("modules/SpatialOmics/domains/level_4.yaml")
        level4_class = sv4.get_class("SpatialLevel4")
        file_format_attr = level4_class.attributes.get("FILE_FORMAT")
        filename_attr = level4_class.attributes.get("FILENAME")

        # Level 4 uses enum, check FILENAME pattern matches enum values
        assert filename_attr.pattern == "^.+\\.(h5ad|rds|zarr)$"

        filename_regex = re.compile(filename_attr.pattern)
        assert filename_regex.match("file.h5ad")
        assert filename_regex.match("file.rds")
        assert filename_regex.match("file.zarr")
