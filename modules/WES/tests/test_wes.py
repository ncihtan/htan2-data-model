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

        # Check that it inherits from BaseSequencingLevel1Attributes (issue #132)
        level1_class = sv.get_class("BulkWESLevel1")
        assert level1_class.is_a == "BaseSequencingLevel1Attributes"

        # Check WES Level 1 specific required attributes
        # Note: LIBRARY_LAYOUT and SEQUENCING_PLATFORM are now in BaseSequencingAttributes
        wes_specific_attrs = [
            "LIBRARY_SELECTION_METHOD",
            "READ_LENGTH",
        ]

        for attr in wes_specific_attrs:
            assert attr in level1_class.attributes

    def test_level_2_schema(self):
        """Test Level 2 schema structure."""
        schema_path = "modules/WES/domains/level_2.yaml"
        sv = SchemaView(schema_path)

        # Check that the main class exists
        assert "BulkWESLevel2" in sv.all_classes()

        # Check that it inherits from BaseSequencingLevel2Attributes (issue #132)
        level2_class = sv.get_class("BulkWESLevel2")
        assert level2_class.is_a == "BaseSequencingLevel2Attributes"

        # Check WES Level 2 specific required attributes
        # Note: GENOMIC_REFERENCE is now in BaseSequencingAttributes
        wes_specific_attrs = [
            "ALIGNMENT_WORKFLOW_TYPE",
            "MEAN_COVERAGE",
            "TOTAL_READS",
            "TOTAL_UNIQUELY_MAPPED",
            "TOTAL_UNMAPPED_READS",
            "PROPORTION_READS_MAPPED",
        ]

        for attr in wes_specific_attrs:
            assert attr in level2_class.attributes

    def test_level_3_schema(self):
        """Test Level 3 schema structure."""
        schema_path = "modules/WES/domains/level_3.yaml"
        sv = SchemaView(schema_path)

        # Check that the main class exists
        assert "BulkWESLevel3" in sv.all_classes()

        # Check that it inherits from BaseSequencingLevel3Attributes (issue #132)
        level3_class = sv.get_class("BulkWESLevel3")
        assert level3_class.is_a == "BaseSequencingLevel3Attributes"

        # Check WES Level 3 specific required attributes
        # Note: GENOMIC_REFERENCE is now in BaseSequencingAttributes
        # Level 3 has no required WES-specific attributes
        wes_specific_attrs = []

        for attr in wes_specific_attrs:
            assert attr in level3_class.attributes

    def test_enums(self):
        """Test that enums are properly defined."""
        # Test Level 1 enums
        sv1 = SchemaView("modules/WES/domains/level_1.yaml")
        # Note: LibraryLayoutEnum and SequencingPlatformEnum are now in Sequencing module
        assert "LibrarySelectionMethodEnum" in sv1.all_enums()

        # Test Level 2 enums
        sv2 = SchemaView("modules/WES/domains/level_2.yaml")
        # Level 2 has no enums

        # Test Level 3 enums
        sv3 = SchemaView("modules/WES/domains/level_3.yaml")
        assert "SomaticVariantsSampleTypeEnum" in sv3.all_enums()
        assert "MSIStatusEnum" in sv3.all_enums()

    def test_file_format_and_filename_patterns(self):
        """Test that FILE_FORMAT and FILENAME patterns match correctly."""
        import re

        # Test Level 1
        sv1 = SchemaView("modules/WES/domains/level_1.yaml")
        level1_class = sv1.get_class("BulkWESLevel1")
        file_format_attr = level1_class.attributes.get("FILE_FORMAT")
        filename_attr = level1_class.attributes.get("FILENAME")

        assert file_format_attr.pattern == "^(fastq|fastq\\.gz)$"
        assert filename_attr.pattern == "^.+\\.(fastq|fq)(\\.gz)?$"

        # Validate pattern matching
        fmt_regex = re.compile(file_format_attr.pattern)
        filename_regex = re.compile(filename_attr.pattern)

        # Test valid combinations
        assert fmt_regex.match("fastq")
        assert filename_regex.match("file.fastq")
        assert filename_regex.match("file.fq")
        assert fmt_regex.match("fastq.gz")
        assert filename_regex.match("file.fastq.gz")
        assert filename_regex.match("file.fq.gz")

        # Test Level 2
        sv2 = SchemaView("modules/WES/domains/level_2.yaml")
        level2_class = sv2.get_class("BulkWESLevel2")
        file_format_attr = level2_class.attributes.get("FILE_FORMAT")
        filename_attr = level2_class.attributes.get("FILENAME")

        assert file_format_attr.pattern == "^(bam|cram)$"
        assert filename_attr.pattern == "^.+\\.(bam|cram)$"

        fmt_regex = re.compile(file_format_attr.pattern)
        filename_regex = re.compile(filename_attr.pattern)

        assert fmt_regex.match("bam")
        assert filename_regex.match("file.bam")
        assert fmt_regex.match("cram")
        assert filename_regex.match("file.cram")

        # Test Level 3
        sv3 = SchemaView("modules/WES/domains/level_3.yaml")
        level3_class = sv3.get_class("BulkWESLevel3")
        file_format_attr = level3_class.attributes.get("FILE_FORMAT")
        filename_attr = level3_class.attributes.get("FILENAME")

        assert file_format_attr.pattern == "^(vcf|vcf\\.gz)$"
        assert filename_attr.pattern == "^.+\\.vcf(\\.gz)?$"

        fmt_regex = re.compile(file_format_attr.pattern)
        filename_regex = re.compile(filename_attr.pattern)

        assert fmt_regex.match("vcf")
        assert filename_regex.match("file.vcf")
        assert fmt_regex.match("vcf.gz")
        assert filename_regex.match("file.vcf.gz")
