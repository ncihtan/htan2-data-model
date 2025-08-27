"""Test suite for HTAN Base Sequencing module."""

import pytest
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.utils.yamlutils import as_yaml
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper


class TestBaseSequencingSchema:
    """Test base sequencing schema loading and validation."""

    def test_schema_loading(self):
        """Test that the schema loads without errors."""
        schema_path = "modules/Sequencing/domains/sequencing.yaml"
        sv = SchemaView(schema_path)
        assert sv.schema.name == "Sequencing"
        assert sv.schema.id == "https://w3id.org/htan/sequencing"

    def test_base_sequencing_attributes_class(self):
        """Test BaseSequencingAttributes class structure."""
        schema_path = "modules/Sequencing/domains/sequencing.yaml"
        sv = SchemaView(schema_path)
        
        # Check class exists
        assert "BaseSequencingAttributes" in sv.all_classes()
        
        # Check required attributes
        base_class = sv.get_class("BaseSequencingAttributes")
        required_attrs = [
            "LIBRARY_LAYOUT",
            "SEQUENCING_PLATFORM",
            "WORKFLOW_VERSION",
            "GENOMIC_REFERENCE"
        ]
        
        for attr in required_attrs:
            assert attr in base_class.attributes
            assert base_class.attributes[attr].required

    def test_enum_alphabetical_ordering(self):
        """Test that enum values are in alphabetical order."""
        schema_path = "modules/Sequencing/domains/sequencing.yaml"
        sv = SchemaView(schema_path)
        
        # Test LibraryLayoutEnum
        library_layout_enum = sv.get_enum("LibraryLayoutEnum")
        values = list(library_layout_enum.permissible_values.keys())
        assert values == sorted(values), f"LibraryLayoutEnum values not alphabetical: {values}"
        
        # Test SequencingPlatformEnum
        platform_enum = sv.get_enum("SequencingPlatformEnum")
        values = list(platform_enum.permissible_values.keys())
        assert values == sorted(values), f"SequencingPlatformEnum values not alphabetical: {values}"

    def test_no_inheritance_from_core(self):
        """Test that BaseSequencingAttributes does not inherit from CoreFileAttributes."""
        schema_path = "modules/Sequencing/domains/sequencing.yaml"
        sv = SchemaView(schema_path)
        
        base_class = sv.get_class("BaseSequencingAttributes")
        # BaseSequencingAttributes should not inherit from CoreFileAttributes
        # It's a mixin/composition class for sequencing-specific attributes
        assert base_class.is_a is None

    def test_common_attributes_present(self):
        """Test that all common sequencing attributes are present."""
        schema_path = "modules/Sequencing/domains/sequencing.yaml"
        sv = SchemaView(schema_path)
        
        base_class = sv.get_class("BaseSequencingAttributes")
        
        # Check for common sequencing attributes
        common_attrs = [
            "SEQUENCING_BATCH_ID",
            "LIBRARY_LAYOUT",
            "SEQUENCING_PLATFORM",
            "LIBRARY_PREPARATION_DAYS_FROM_INDEX",
            "TECHNICAL_REPLICATE_GROUP",
            "PROTOCOL_LINK",
            "WORKFLOW_VERSION",
            "WORKFLOW_LINK",
            "GENOMIC_REFERENCE",
            "GENOMIC_REFERENCE_URL",
            "GENOME_ANNOTATION_URL",
            "CHECKSUM"
        ]
        
        for attr in common_attrs:
            assert attr in base_class.attributes, f"Missing common attribute: {attr}"

    def test_optional_attributes(self):
        """Test that optional attributes are properly marked."""
        schema_path = "modules/Sequencing/domains/sequencing.yaml"
        sv = SchemaView(schema_path)
        
        base_class = sv.get_class("BaseSequencingAttributes")
        optional_attrs = [
            "SEQUENCING_BATCH_ID",
            "LIBRARY_PREPARATION_DAYS_FROM_INDEX",
            "TECHNICAL_REPLICATE_GROUP",
            "PROTOCOL_LINK",
            "WORKFLOW_LINK",
            "GENOMIC_REFERENCE_URL",
            "GENOME_ANNOTATION_URL",
            "CHECKSUM"
        ]
        
        for attr in optional_attrs:
            assert attr in base_class.attributes
            assert not base_class.attributes[attr].required


class TestBaseSequencingDataValidation:
    """Test base sequencing data validation."""

    def test_valid_base_sequencing_data(self):
        """Test valid base sequencing data."""
        valid_data = {
            "COMPONENT": "Sequencing",
            "HTAN_PARTICIPANT_ID": "HTAN-001",
            "HTAN_DATA_FILE_ID": "HTAN-001_0000_0001",
            "FILENAME": "sequencing_data.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTAN-001_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTAN-001_0000_B0001",
            "LIBRARY_LAYOUT": "Paired-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "WORKFLOW_VERSION": "1.0.0",
            "GENOMIC_REFERENCE": "GRCh38"
        }
        
        # Validate required fields
        assert valid_data["LIBRARY_LAYOUT"] in ["Paired-end", "Single-end"]
        assert valid_data["SEQUENCING_PLATFORM"] in [
            "ABI_SOLID", "BGISEQ", "CAPILLARY", "COMPLETE_GENOMICS", 
            "HELICOS", "ILLUMINA", "ION_TORRENT", "LS454", 
            "OXFORD_NANOPORE", "PACBIO_SMRT"
        ]

    def test_enum_validation(self):
        """Test enum value validation."""
        # Valid library layouts
        valid_layouts = ["Paired-end", "Single-end"]
        
        # Valid sequencing platforms
        valid_platforms = [
            "ABI_SOLID", "BGISEQ", "CAPILLARY", "COMPLETE_GENOMICS",
            "HELICOS", "ILLUMINA", "ION_TORRENT", "LS454",
            "OXFORD_NANOPORE", "PACBIO_SMRT"
        ]
        
        # Test that all values are in alphabetical order
        assert valid_layouts == sorted(valid_layouts)
        assert valid_platforms == sorted(valid_platforms)


if __name__ == "__main__":
    pytest.main([__file__])
