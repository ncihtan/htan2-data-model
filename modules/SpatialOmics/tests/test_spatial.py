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

        # Get all slots
        all_slots = sv.class_slots("SpatialPanel")

        # Check required attributes
        required_attrs = [
            "HTAN_PANEL_ID",
            "GENE_SYMBOL",
            "HGNC_VERSION",
            "GENE_ID",
        ]

        for attr in required_attrs:
            assert attr in all_slots, f"Required attribute {attr} not found"
            # Check class-specific slot definition (SpatialPanel doesn't inherit, so all are class-specific)
            class_slot = panel_class.attributes.get(attr)
            assert (
                class_slot is not None
            ), f"Attribute {attr} should be defined in SpatialPanel"
            assert class_slot.required is True, f"Attribute {attr} should be required"

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

        # Test Synapse ID pattern for PANEL_SYNAPSE_ID
        panel_synapse_id_slot = sv.get_slot("PANEL_SYNAPSE_ID")
        assert panel_synapse_id_slot is not None
        assert panel_synapse_id_slot.pattern == "^syn\\d+$"

        # Test Gene ID pattern for GENE_ID
        gene_id_slot = sv.get_slot("GENE_ID")
        assert gene_id_slot is not None
        assert gene_id_slot.pattern == "^(ENSG\\d+|\\d+)$"

        # Test HGNC Version pattern
        hgnc_version_slot = sv.get_slot("HGNC_VERSION")
        assert hgnc_version_slot is not None
        assert hgnc_version_slot.pattern == "^\\d{4}-\\d{2}-\\d{2}$"

        # Test Gene Symbol pattern for GENE_SYMBOL
        gene_symbol_slot = sv.get_slot("GENE_SYMBOL")
        assert gene_symbol_slot is not None
        assert gene_symbol_slot.pattern == "^[A-Za-z0-9_\\-]+(@)?$"

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
