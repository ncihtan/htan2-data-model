"""Tests for the HTAN Biospecimen module."""

import re

import pytest
import yaml
import os
from linkml_runtime.utils.schemaview import SchemaView


class TestBiospecimen:
    """Test cases for the Biospecimen module."""

    def test_schema_loading(self):
        """Test that the Biospecimen schema can be loaded."""
        schema_path = "modules/Biospecimen/domains/biospecimen.yaml"
        with open(schema_path, "r") as f:
            schema = yaml.safe_load(f)
        assert schema is not None
        assert schema["name"] == "Biospecimen"

    def test_core_inheritance(self):
        """Test that Biospecimen is a record-based module (does not inherit from CoreFileAttributes)."""
        schema_path = "modules/Biospecimen/domains/biospecimen.yaml"
        sv = SchemaView(schema_path)

        # Check that the main class exists
        assert "BiospecimenData" in sv.all_classes()

        # Check that it does NOT inherit from CoreFileAttributes (it's a record-based module)
        biospecimen_class = sv.get_class("BiospecimenData")
        assert (
            biospecimen_class.is_a is None
        ), "BiospecimenData is record-based and should not inherit from CoreFileAttributes"

    def test_enums(self):
        """Test that enums are properly defined."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")

        # Check that key enums exist
        expected_enums = [
            "BiospecimenTypeEnum",
            "AcquisitionMethodTypeEnum",
            "SpecimenLateralityEnum",
            "PreservationMethodEnum",
            "PreservationMediumEnum",
            "PreservationTemperatureEnum",
            "AnalyteTypeEnum",
            "SlicingMethodEnum",
            "SlideChargeTypeEnum",
            "CellularArchitectureEnum",
            "TumorClassificationEnum",
            "DegreeOfDysplasiaEnum",
            "ShippingConditionEnum",
            "TimepointEnum",
            "IcdO3MorphologyEnum",
            "Icd10DiseaseEnum",
        ]

        for enum_name in expected_enums:
            assert enum_name in sv.all_enums(), f"Enum {enum_name} not found"

    def test_required_attributes(self):
        """Test that all required attributes from RFC are present."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        # Check that key attributes exist
        expected_attributes = [
            "BIOSPECIMEN_TYPE",
            "ACQUISITION_METHOD_TYPE",
            "SITE_OF_RESECTION_OR_BIOPSY",
            "SPECIMEN_LATERALITY",
            "PRESERVATION_METHOD",
            "SPECIMEN_CELLULAR_ARCHITECTURE",
            "SHIPPING_CONDITION_TYPE",
        ]

        for attr_name in expected_attributes:
            assert (
                attr_name in biospecimen_class.attributes
            ), f"Attribute {attr_name} not found"

    def test_enum_values(self):
        """Test that enum values are properly defined."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")

        # Test BiospecimenTypeEnum
        biospecimen_type_enum = sv.get_enum("BiospecimenTypeEnum")
        expected_values = ["Ascites", "Blood", "Tissue", "DNA", "RNA"]
        for value in expected_values:
            assert (
                value in biospecimen_type_enum.permissible_values
            ), f"Value {value} not found in BiospecimenTypeEnum"

    def test_conditional_requirements(self):
        """Test that conditional requirements are properly implemented."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        # Check that conditional attributes exist
        conditional_attributes = [
            "ACQUISITION_METHOD_OTHER_SPECIFY",
            "FIXATION_DURATION_IN_MINUTES",
            "ANALYTE_TYPE",
            "SLICING_METHOD",
            "TUMOR_CLASSIFICATION",
            "ICD_O_3_TISSUE_MORPHOLOGY",
            "ICD_10_DISEASE_CODE",
            "DEGREE_OF_DYSPLASIA",
        ]

        for attr_name in conditional_attributes:
            assert (
                attr_name in biospecimen_class.attributes
            ), f"Conditional attribute {attr_name} not found"

    def test_uberon_integration(self):
        """Test that UBERON integration is properly implemented."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        # Check that SITE_OF_RESECTION_OR_BIOPSY uses UBERON enum
        site_attr = biospecimen_class.attributes["SITE_OF_RESECTION_OR_BIOPSY"]
        assert "tissue_or_organ_of_origin_uberon_enum" in str(site_attr.range)

    def test_icd_integration(self):
        """Test that ICD integration is properly implemented."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        # Check that ICD attributes use proper enums
        icd_o3_attr = biospecimen_class.attributes["ICD_O_3_TISSUE_MORPHOLOGY"]
        assert "IcdO3MorphologyEnum" in str(icd_o3_attr.range)

        icd_10_attr = biospecimen_class.attributes["ICD_10_DISEASE_CODE"]
        assert "Icd10DiseaseEnum" in str(icd_10_attr.range)

    def test_physical_characteristics(self):
        """Test that physical characteristic attributes are present."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        physical_attributes = ["LONGEST_DIMENSION", "SHORTEST_DIMENSION"]

        for attr_name in physical_attributes:
            assert (
                attr_name in biospecimen_class.attributes
            ), f"Physical attribute {attr_name} not found"

    def test_processing_attributes(self):
        """Test that processing attributes are present."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        processing_attributes = [
            "PRESERVATION_METHOD_TEMPERATURE",
            "FIXATION_DURATION_IN_MINUTES",
            "PROCESSING_LOCATION",
        ]

        for attr_name in processing_attributes:
            assert (
                attr_name in biospecimen_class.attributes
            ), f"Processing attribute {attr_name} not found"

    def test_shipping_attributes(self):
        """Test that shipping attributes are present."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        shipping_attributes = ["SHIPPING_CONDITION_TYPE"]

        for attr_name in shipping_attributes:
            assert (
                attr_name in biospecimen_class.attributes
            ), f"Shipping attribute {attr_name} not found"

    def test_timepoint_integration(self):
        """Test that timepoint integration is properly implemented."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        # Check that TIMEPOINT attribute exists and uses proper enum
        assert "TIMEPOINT" in biospecimen_class.attributes
        timepoint_attr = biospecimen_class.attributes["TIMEPOINT"]
        assert "TimepointEnum" in str(timepoint_attr.range)

    def test_adjacent_biospecimen_ids(self):
        """Test that adjacent biospecimen IDs attribute is properly implemented."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")

        # Check that ADJACENT_BIOSPECIMEN_IDS attribute exists
        assert "ADJACENT_BIOSPECIMEN_IDS" in biospecimen_class.attributes
        adjacent_attr = biospecimen_class.attributes["ADJACENT_BIOSPECIMEN_IDS"]
        assert "string" in str(adjacent_attr.range)  # Should be a list of strings

    def test_adjacent_biospecimen_ids_regex_rejects_malformed(self):
        """Test that ADJACENT_BIOSPECIMEN_IDS pattern rejects malformed IDs."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")
        adjacent_attr = biospecimen_class.attributes["ADJACENT_BIOSPECIMEN_IDS"]
        pattern = adjacent_attr.pattern
        assert pattern is not None, "ADJACENT_BIOSPECIMEN_IDS should have a pattern"
        compiled = re.compile(pattern)

        # Each ID in the multivalued field must match the biospecimen ID pattern (e.g. HTA200_0000_B1)
        valid_ids = [
            "HTA200_0000_B1",
            "HTA201_12345_B2",
            "HTA229_EXT1_B999",
        ]
        for vid in valid_ids:
            assert compiled.fullmatch(vid), f"Valid ID should match: {vid!r}"

        malformed_ids = [
            "not-an-id",
            "HTA200_0000",           # missing _B suffix
            "HTA200_0000_D1",        # D suffix (data file), not B
            "HTA300_0000_B1",        # invalid center (only 200-229)
            "HTA20_0000_B1",         # center too short
            "HTA200_0000_B",         # B with no digits
            "",
        ]
        for mid in malformed_ids:
            assert compiled.fullmatch(mid) is None, f"Malformed ID should be rejected: {mid!r}"

    def test_conditional_rules(self):
        """Test that all 8 conditional requirement rules exist; conditionally-required slots are optional at attribute level."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")
        rules = biospecimen_class.rules or []

        def triple(r):
            pre = (
                getattr(getattr(r, "preconditions", None), "slot_conditions", None)
                or {}
            )
            post = (
                getattr(getattr(r, "postconditions", None), "slot_conditions", None)
                or {}
            )
            if (
                not pre
                or not post
                or getattr(next(iter(post.values())), "required", None) is not True
            ):
                return None
            pre_slot, post_slot = next(iter(pre)), next(iter(post))
            return (pre_slot, getattr(pre[pre_slot], "equals_string", None), post_slot)

        expected = {
            ("ACQUISITION_METHOD_TYPE", "Other", "ACQUISITION_METHOD_OTHER_SPECIFY"),
            ("PRESERVATION_METHOD", "Fixation", "FIXATION_DURATION_IN_MINUTES"),
            ("BIOSPECIMEN_TYPE", "DNA", "ANALYTE_TYPE"),
            ("BIOSPECIMEN_TYPE", "RNA", "ANALYTE_TYPE"),
            ("SPECIMEN_CELLULAR_ARCHITECTURE", "Tumor", "TUMOR_CLASSIFICATION"),
            ("SPECIMEN_CELLULAR_ARCHITECTURE", "Tumor", "ICD_O_3_TISSUE_MORPHOLOGY"),
            ("SPECIMEN_CELLULAR_ARCHITECTURE", "Precancerous", "ICD_10_DISEASE_CODE"),
            ("SPECIMEN_CELLULAR_ARCHITECTURE", "Precancerous", "DEGREE_OF_DYSPLASIA"),
        }
        actual = {t for r in rules for t in [triple(r)] if t is not None}
        assert (
            actual == expected
        ), f"Rule mismatch: missing {expected - actual}, unexpected {actual - expected}"

        for _, _, post_slot in expected:
            assert biospecimen_class.attributes[post_slot].required is False

    def test_tissue_sample_type_removed(self):
        """Test that TISSUE_SAMPLE_TYPE has been removed from the schema (issue #168)."""
        sv = SchemaView("modules/Biospecimen/domains/biospecimen.yaml")
        biospecimen_class = sv.get_class("BiospecimenData")
        assert "TISSUE_SAMPLE_TYPE" not in biospecimen_class.attributes
        assert "TissueSampleTypeEnum" not in sv.all_enums()
