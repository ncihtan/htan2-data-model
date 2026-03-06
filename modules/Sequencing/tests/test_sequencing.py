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


def _required_slots_for_class(sv, class_name):
    """Return set of required slot names for a class (including inherited)."""
    induced = sv.class_induced_slots(class_name)
    return {s.name for s in induced if s.required}


def _validate_sequencing_data_for_class(sv, data, class_name):
    """
    Validate that data dict contains all required slots for the given class.
    Raises ValueError with message listing missing slots if invalid.
    """
    required = _required_slots_for_class(sv, class_name)
    missing = required - set(data.keys())
    if missing:
        raise ValueError(f"Missing required attributes for {class_name}: {sorted(missing)}")


def _validate_enum_slot(sv, data, class_name, slot_name):
    """
    Validate that data[slot_name] is a permissible value for the slot's enum range.
    Raises ValueError if the slot has an enum range and the value is not permissible.
    """
    induced = list(sv.class_induced_slots(class_name))
    slot_def = next((s for s in induced if s.name == slot_name), None)
    if slot_def is None or slot_def.range not in sv.all_enums():
        return
    enum_def = sv.get_enum(slot_def.range)
    value = data.get(slot_name)
    if value is not None and value not in enum_def.permissible_values:
        raise ValueError(
            f"Invalid value for {slot_name}: {value!r} not in {list(enum_def.permissible_values.keys())}"
        )


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

        # Test GenomicReferenceEnum
        genomic_ref_enum = sv.get_enum("GenomicReferenceEnum")
        values = list(genomic_ref_enum.permissible_values.keys())
        assert values == sorted(
            values
        ), f"GenomicReferenceEnum values not alphabetical: {values}"

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

        # Level 2: GENOMIC_REFERENCE_URL and GENOME_ANNOTATION_URL are required (not optional)


class TestBaseSequencingDataValidation:
    """Test base sequencing data validation."""

    def test_valid_base_sequencing_data(self):
        """Test valid BaseSequencingLevel2Attributes data (includes required WORKFLOW_LINK)."""
        sv = SchemaView(SCHEMA_PATH)
        # Valid Level 2 instance: all required Level 1 + Level 2 attributes including WORKFLOW_LINK
        valid_level2_data = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "sequencing_data.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Paired-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "GENOMIC_REFERENCE": "GRCh38",
            "GENOMIC_REFERENCE_URL": "https://example.org/ref.fa",
            "GENOME_ANNOTATION_URL": "https://example.org/anno.gtf",
            "WORKFLOW_VERSION": "1.0.0",
            "WORKFLOW_LINK": "https://dockstore.org/workflows/github.com/.../workflow",
        }
        _validate_sequencing_data_for_class(sv, valid_level2_data, "BaseSequencingLevel2Attributes")
        _validate_enum_slot(sv, valid_level2_data, "BaseSequencingLevel2Attributes", "GENOMIC_REFERENCE")
        # Enum checks
        genomic_ref_enum = sv.get_enum("GenomicReferenceEnum")
        assert valid_level2_data["GENOMIC_REFERENCE"] in genomic_ref_enum.permissible_values
        assert valid_level2_data["LIBRARY_LAYOUT"] in ["Paired-end", "Single-end"]
        assert valid_level2_data["SEQUENCING_PLATFORM"] in list(
            sv.get_enum("SequencingPlatformEnum").permissible_values
        )

    def test_valid_level2_instance_loads_without_error(self):
        """A valid BaseSequencingLevel2Attributes instance passes schema required-slot validation."""
        sv = SchemaView(SCHEMA_PATH)
        valid_level2 = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "seq.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Single-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "GENOMIC_REFERENCE": "GRCh38",
            "GENOMIC_REFERENCE_URL": "https://example.org/ref.fa",
            "GENOME_ANNOTATION_URL": "https://example.org/anno.gtf",
            "WORKFLOW_VERSION": "2.0",
            "WORKFLOW_LINK": "https://dockstore.org/workflows/example",
        }
        _validate_sequencing_data_for_class(sv, valid_level2, "BaseSequencingLevel2Attributes")
        _validate_enum_slot(sv, valid_level2, "BaseSequencingLevel2Attributes", "GENOMIC_REFERENCE")

    def test_invalid_level2_missing_workflow_link_raises(self):
        """Missing required WORKFLOW_LINK fails validation with ValueError."""
        sv = SchemaView(SCHEMA_PATH)
        invalid_level2 = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "seq.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Single-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "GENOMIC_REFERENCE": "GRCh38",
            "GENOMIC_REFERENCE_URL": "https://example.org/ref.fa",
            "GENOME_ANNOTATION_URL": "https://example.org/anno.gtf",
            "WORKFLOW_VERSION": "2.0",
            # WORKFLOW_LINK omitted
        }
        with pytest.raises(ValueError) as exc_info:
            _validate_sequencing_data_for_class(sv, invalid_level2, "BaseSequencingLevel2Attributes")
        assert "WORKFLOW_LINK" in str(exc_info.value)

    def test_level3_is_a_level2(self):
        """BaseSequencingLevel3Attributes is_a BaseSequencingLevel2Attributes."""
        sv = SchemaView(SCHEMA_PATH)
        level3 = sv.get_class("BaseSequencingLevel3Attributes")
        assert level3.is_a == "BaseSequencingLevel2Attributes"

    def test_valid_level3_instance_loads_without_error(self):
        """A valid BaseSequencingLevel3Attributes instance passes schema validation (same required as Level 2)."""
        sv = SchemaView(SCHEMA_PATH)
        valid_level3 = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "processed.bam",
            "FILE_FORMAT": "bam",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Paired-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "GENOMIC_REFERENCE": "GRCh38",
            "GENOMIC_REFERENCE_URL": "https://example.org/ref.fa",
            "GENOME_ANNOTATION_URL": "https://example.org/anno.gtf",
            "WORKFLOW_VERSION": "1.0",
            "WORKFLOW_LINK": "https://dockstore.org/workflows/example",
        }
        _validate_sequencing_data_for_class(sv, valid_level3, "BaseSequencingLevel3Attributes")
        _validate_enum_slot(sv, valid_level3, "BaseSequencingLevel3Attributes", "GENOMIC_REFERENCE")

    def test_invalid_level3_missing_required_raises(self):
        """Level 3 instance missing required attribute (e.g. WORKFLOW_LINK) fails validation."""
        sv = SchemaView(SCHEMA_PATH)
        invalid_level3 = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "processed.bam",
            "FILE_FORMAT": "bam",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Paired-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "GENOMIC_REFERENCE": "GRCh38",
            "GENOMIC_REFERENCE_URL": "https://example.org/ref.fa",
            "GENOME_ANNOTATION_URL": "https://example.org/anno.gtf",
            "WORKFLOW_VERSION": "1.0",
            # WORKFLOW_LINK omitted
        }
        with pytest.raises(ValueError) as exc_info:
            _validate_sequencing_data_for_class(sv, invalid_level3, "BaseSequencingLevel3Attributes")
        assert "WORKFLOW_LINK" in str(exc_info.value)

    def test_genomic_reference_enum_valid_value(self):
        """A valid GenomicReferenceEnum value (e.g. GRCh38) is in the schema and accepted."""
        sv = SchemaView(SCHEMA_PATH)
        genomic_ref_enum = sv.get_enum("GenomicReferenceEnum")
        assert "GRCh38" in genomic_ref_enum.permissible_values
        assert genomic_ref_enum.permissible_values["GRCh38"].description

    def test_genomic_reference_enum_invalid_value_raises(self):
        """An invalid GenomicReferenceEnum value raises ValueError when validated against the schema."""
        sv = SchemaView(SCHEMA_PATH)
        genomic_ref_enum = sv.get_enum("GenomicReferenceEnum")
        assert "INVALID_GENOMIC_REF" not in genomic_ref_enum.permissible_values
        data_with_invalid_ref = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "seq.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTA200_0000_B0001",
            "LIBRARY_LAYOUT": "Single-end",
            "SEQUENCING_PLATFORM": "ILLUMINA",
            "GENOMIC_REFERENCE": "INVALID_GENOMIC_REF",
            "GENOMIC_REFERENCE_URL": "https://example.org/ref.fa",
            "GENOME_ANNOTATION_URL": "https://example.org/anno.gtf",
            "WORKFLOW_VERSION": "1.0",
            "WORKFLOW_LINK": "https://example.org",
        }
        with pytest.raises(ValueError) as exc_info:
            _validate_enum_slot(sv, data_with_invalid_ref, "BaseSequencingLevel2Attributes", "GENOMIC_REFERENCE")
        assert "GENOMIC_REFERENCE" in str(exc_info.value) and "INVALID_GENOMIC_REF" in str(exc_info.value)

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
