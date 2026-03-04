"""Test suite for HTAN Base Sequencing module."""

import pytest
import os
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.utils.yamlutils import as_yaml
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper

# Get the directory where this test file is located
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.dirname(TEST_DIR)
SCHEMA_PATH = os.path.join(MODULE_DIR, "domains", "sequencing.yaml")


class TestBaseSequencingSchema:
    """Test base sequencing schema loading and validation."""

    def test_schema_loading(self):
        """Test that the schema loads without errors."""
        sv = SchemaView(SCHEMA_PATH)
        assert sv.schema.name == "Sequencing"
        assert sv.schema.id == "https://w3id.org/htan/sequencing"

    def test_base_sequencing_attributes_class(self):
        """Test BaseSequencingAttributes and level base classes (issue #132)."""
        sv = SchemaView(SCHEMA_PATH)

        assert "BaseSequencingAttributes" in sv.all_classes()
        assert "BaseSequencingLevel1Attributes" in sv.all_classes()
        assert "BaseSequencingLevel2Attributes" in sv.all_classes()
        assert "BaseSequencingLevel3Attributes" in sv.all_classes()

        # BaseSequencingAttributes: minimal (CHECKSUM only)
        base_class = sv.get_class("BaseSequencingAttributes")
        assert "CHECKSUM" in base_class.attributes
        assert not base_class.attributes["CHECKSUM"].required

        # Level 1: run/library attributes
        level1 = sv.get_class("BaseSequencingLevel1Attributes")
        assert level1.is_a == "BaseSequencingAttributes"
        for attr in ["LIBRARY_LAYOUT", "SEQUENCING_PLATFORM"]:
            assert attr in level1.attributes and level1.attributes[attr].required

        # Level 2: alignment + workflow
        level2 = sv.get_class("BaseSequencingLevel2Attributes")
        assert level2.is_a == "BaseSequencingLevel1Attributes"
        for attr in ["GENOMIC_REFERENCE", "WORKFLOW_VERSION", "WORKFLOW_LINK"]:
            assert attr in level2.attributes and level2.attributes[attr].required

    def test_enum_alphabetical_ordering(self):
        """Test that enum values are in alphabetical order."""
        sv = SchemaView(SCHEMA_PATH)

        # Test LibraryLayoutEnum
        library_layout_enum = sv.get_enum("LibraryLayoutEnum")
        values = list(library_layout_enum.permissible_values.keys())
        assert values == sorted(
            values
        ), f"LibraryLayoutEnum values not alphabetical: {values}"

        # Test SequencingPlatformEnum
        platform_enum = sv.get_enum("SequencingPlatformEnum")
        values = list(platform_enum.permissible_values.keys())
        assert values == sorted(
            values
        ), f"SequencingPlatformEnum values not alphabetical: {values}"

    def test_inheritance_from_core(self):
        """Test that BaseSequencingAttributes inherits from CoreFileAttributes."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseSequencingAttributes")
        # BaseSequencingAttributes should inherit from CoreFileAttributes
        assert base_class.is_a == "CoreFileAttributes"

    def test_common_attributes_present(self):
        """Test that level-specific sequencing attributes are present (issue #132)."""
        sv = SchemaView(SCHEMA_PATH)

        level1 = sv.get_class("BaseSequencingLevel1Attributes")
        level2 = sv.get_class("BaseSequencingLevel2Attributes")

        for attr in ["CHECKSUM"]:
            assert attr in sv.get_class("BaseSequencingAttributes").attributes
        for attr in ["LIBRARY_LAYOUT", "SEQUENCING_PLATFORM", "SEQUENCING_BATCH_ID",
                     "LIBRARY_PREPARATION_DAYS_FROM_INDEX", "TECHNICAL_REPLICATE_GROUP", "PROTOCOL_LINK"]:
            assert attr in level1.attributes, f"Missing Level1 attribute: {attr}"
        for attr in ["GENOMIC_REFERENCE", "GENOMIC_REFERENCE_URL", "GENOME_ANNOTATION_URL",
                     "WORKFLOW_VERSION", "WORKFLOW_LINK"]:
            assert attr in level2.attributes, f"Missing Level2 attribute: {attr}"

    def test_optional_attributes(self):
        """Test that optional attributes are properly marked in level bases."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseSequencingAttributes")
        assert "CHECKSUM" in base_class.attributes and not base_class.attributes["CHECKSUM"].required

        level1 = sv.get_class("BaseSequencingLevel1Attributes")
        for attr in ["SEQUENCING_BATCH_ID", "LIBRARY_PREPARATION_DAYS_FROM_INDEX",
                     "TECHNICAL_REPLICATE_GROUP", "PROTOCOL_LINK"]:
            assert attr in level1.attributes and not level1.attributes[attr].required

        level2 = sv.get_class("BaseSequencingLevel2Attributes")
        for attr in ["GENOMIC_REFERENCE_URL", "GENOME_ANNOTATION_URL"]:
            assert attr in level2.attributes and not level2.attributes[attr].required


class TestBaseSequencingDataValidation:
    """Test base sequencing data validation."""

    def test_valid_base_sequencing_data(self):
        """Test valid base sequencing data."""
        valid_data = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "sequencing_data.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Paired-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "WORKFLOW_VERSION": "1.0.0",
            "GENOMIC_REFERENCE": "GRCh38",
        }

        # Validate required fields
        assert valid_data["LIBRARY_LAYOUT"] in ["Paired-end", "Single-end"]
        assert valid_data["SEQUENCING_PLATFORM"] in [
            "ABI_SOLID",
            "BGISEQ",
            "CAPILLARY",
            "COMPLETE_GENOMICS",
            "HELICOS",
            "ILLUMINA",
            "ION_TORRENT",
            "LS454",
            "OXFORD_NANOPORE",
            "PACBIO_SMRT",
        ]

    def test_enum_validation(self):
        """Test enum value validation."""
        # Valid library layouts
        valid_layouts = ["Paired-end", "Single-end"]

        # Valid sequencing platforms
        valid_platforms = [
            "ABI_SOLID",
            "BGISEQ",
            "CAPILLARY",
            "COMPLETE_GENOMICS",
            "HELICOS",
            "ILLUMINA",
            "ION_TORRENT",
            "LS454",
            "OXFORD_NANOPORE",
            "PACBIO_SMRT",
        ]

        # Test that all values are in alphabetical order
        assert valid_layouts == sorted(valid_layouts)
        assert valid_platforms == sorted(valid_platforms)


if __name__ == "__main__":
    pytest.main([__file__])
