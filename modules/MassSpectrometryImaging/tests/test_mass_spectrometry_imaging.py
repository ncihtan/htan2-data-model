"""Tests for the HTAN Mass Spectrometry Imaging (MSI) module."""

import re

import pytest
from linkml_runtime.utils.schemaview import SchemaView

SCHEMA = "modules/MassSpectrometryImaging/domains/mass_spectrometry_imaging.yaml"

LEVEL_CLASSES = [
    "MassSpectrometryImagingLevel1",
    "MassSpectrometryImagingLevel2",
    "MassSpectrometryImagingLevel3",
    "MassSpectrometryImagingLevel4",
]


@pytest.fixture(scope="module")
def sv():
    return SchemaView(SCHEMA)


class TestSchema:
    """Schema loading and container wiring."""

    def test_schema_loads(self, sv):
        assert sv is not None

    def test_container_class(self, sv):
        assert "MassSpectrometryImagingData" in sv.all_classes()
        slots = sv.class_slots("MassSpectrometryImagingData")
        for s in ["LEVEL_1_DATA", "LEVEL_2_DATA", "LEVEL_3_DATA", "LEVEL_4_DATA", "MOLECULAR_ASSIGNMENTS"]:
            assert s in slots, f"{s} missing from container"

    def test_molecular_assignments_inlined_as_list(self, sv):
        slot = sv.induced_slot("MOLECULAR_ASSIGNMENTS", "MassSpectrometryImagingData")
        assert slot.range == "MolecularAssignment"
        assert slot.multivalued is True
        assert slot.inlined_as_list is True


class TestInheritance:
    """Level classes inherit CoreFileAttributes; the RecordSet row class does not."""

    @pytest.mark.parametrize("cls", LEVEL_CLASSES)
    def test_levels_inherit_core(self, sv, cls):
        assert cls in sv.all_classes()
        assert sv.get_class(cls).is_a == "CoreFileAttributes"

    def test_molecular_assignment_is_standalone(self, sv):
        """The RecordSet row class must NOT inherit CoreFileAttributes (like ChannelMetadata)."""
        ma = sv.get_class("MolecularAssignment")
        assert ma is not None
        assert ma.is_a is None

    def test_levels_inherit_core_identifiers(self, sv):
        for cls in LEVEL_CLASSES:
            slots = sv.class_slots(cls)
            for s in ["HTAN_DATA_FILE_ID", "HTAN_PARENT_ID", "FILENAME", "FILE_FORMAT"]:
                assert s in slots, f"{s} not inherited by {cls}"


class TestLevel1:
    """Level 1 required/optional slots, multivalued analyte class, and MALDI rule."""

    def test_required_slots(self, sv):
        cls = "MassSpectrometryImagingLevel1"
        required = [
            "MS_IONIZATION_TECHNIQUE", "MASS_ANALYZER_TYPE", "MASS_ANALYSIS_POLARITY",
            "ANALYTE_CLASS", "IS_TARGETED", "ACQUISITION_INSTRUMENT_VENDOR",
            "ACQUISITION_INSTRUMENT_MODEL", "PIXEL_SIZE_X_UM", "PIXEL_SIZE_Y_UM",
            "MASS_TO_CHARGE_RANGE_LOW_VALUE", "MASS_TO_CHARGE_RANGE_HIGH_VALUE",
            "ION_MOBILITY", "SPECTRUM_TYPE", "MASS_RESOLVING_POWER", "MS_SCAN_MODE",
            "CALIBRATION_TYPE", "CALIBRANT_MASSES", "SOFTWARE_AND_VERSION",
            "IBD_FILE_UUID", "PASSED_QC",
        ]
        for s in required:
            slot = sv.induced_slot(s, cls)
            assert slot.required is True, f"{s} should be required at Level 1"

    def test_optional_slots(self, sv):
        cls = "MassSpectrometryImagingLevel1"
        optional = [
            "MASS_TO_CHARGE_RESOLVING_POWER", "PROTOCOL_LINK",
            "PREPARATION_MATRIX", "MATRIX_DEPOSITION_METHOD",
            "PREPARATION_INSTRUMENT_VENDOR", "PREPARATION_INSTRUMENT_MODEL",
            "ANALYTE_ACQUISITION_ORDER", "PRE_ACQUISITION_TREATMENT", "QC_COMMENT",
        ]
        for s in optional:
            slot = sv.induced_slot(s, cls)
            assert not slot.required, f"{s} should be optional at Level 1"

    def test_analyte_class_multivalued(self, sv):
        slot = sv.induced_slot("ANALYTE_CLASS", "MassSpectrometryImagingLevel1")
        assert slot.multivalued is True

    def test_every_attribute_has_title_and_description(self, sv):
        cls = sv.get_class("MassSpectrometryImagingLevel1")
        for name, attr in cls.attributes.items():
            assert attr.title, f"{name} missing title"
            assert attr.description, f"{name} missing description"

    def test_maldi_conditional_rule_present(self, sv):
        cls = sv.get_class("MassSpectrometryImagingLevel1")
        rule_text = " ".join(r.description or "" for r in (cls.rules or []))
        assert "MALDI" in rule_text
        # the rule makes PREPARATION_MATRIX / MATRIX_DEPOSITION_METHOD required on MALDI
        post_slots = set()
        for r in cls.rules or []:
            if r.postconditions and r.postconditions.slot_conditions:
                post_slots.update(r.postconditions.slot_conditions.keys())
        assert "PREPARATION_MATRIX" in post_slots
        assert "MATRIX_DEPOSITION_METHOD" in post_slots


class TestEnums:
    """Enum presence, alphabetical ordering, descriptions, and MULTI_CLASS removal."""

    def test_enums_present(self, sv):
        expected = [
            "MsIonizationTechniqueEnum", "MassAnalyzerTypeEnum", "MassAnalysisPolarityEnum",
            "AnalyteClassEnum", "SpectrumTypeEnum", "MsScanModeEnum", "CalibrationTypeEnum",
            "TimeUnitEnum", "PreparationMatrixEnum", "MatrixDepositionMethodEnum",
            "PreAcquisitionTreatmentEnum", "BaselineCorrectionMethodEnum",
            "NormalizationMethodEnum", "SmoothingMethodEnum", "SegmentationReferenceModalityEnum",
            "AdductEnum", "DatabaseSourceEnum", "EvidenceTypeEnum",
        ]
        all_enums = sv.all_enums()
        for e in expected:
            assert e in all_enums, f"{e} missing"

    def test_multi_class_removed(self, sv):
        pv = sv.get_enum("AnalyteClassEnum").permissible_values
        assert "MULTI_CLASS" not in pv
        assert "LIPIDS" in pv and "GLYCANS" in pv

    def test_enums_alphabetical(self, sv):
        """CLAUDE.md rule: permissible values are alphabetically ordered."""
        for ename, enum in sv.all_enums().items():
            values = list(enum.permissible_values.keys())
            assert values == sorted(values), f"{ename} values not alphabetical: {values}"

    def test_permissible_values_have_descriptions(self, sv):
        for ename, enum in sv.all_enums().items():
            for vname, v in enum.permissible_values.items():
                assert v.description, f"{ename}.{vname} missing description"


class TestMolecularAssignments:
    """Molecular Assignments RecordSet columns, bounds, and CONFIDENCE_LEVEL-gated rules."""

    def test_required_columns(self, sv):
        cls = "MolecularAssignment"
        required = ["HTAN_DATA_FILE_ID", "CHANNEL_INDEX", "MZ_OBSERVED", "MOLECULAR_NAME",
                    "SOFTWARE_AND_VERSION", "CONFIDENCE_LEVEL", "EVIDENCE_TYPE"]
        for s in required:
            assert sv.induced_slot(s, cls).required is True, f"{s} should be required"

    def test_conditional_columns_optional_by_default(self, sv):
        cls = "MolecularAssignment"
        conditional = ["MZ_THEORETICAL", "MASS_ERROR_PPM", "MOLECULAR_FORMULA",
                       "ADDUCT", "DATABASE_SOURCE", "DATABASE_ID", "DATABASE_VERSION"]
        for s in conditional:
            assert not sv.induced_slot(s, cls).required, f"{s} should be optional (rule-gated)"

    def test_evidence_type_multivalued(self, sv):
        slot = sv.induced_slot("EVIDENCE_TYPE", "MolecularAssignment")
        assert slot.multivalued is True

    def test_confidence_level_bounds(self, sv):
        slot = sv.induced_slot("CONFIDENCE_LEVEL", "MolecularAssignment")
        assert slot.minimum_value == 1
        assert slot.maximum_value == 4

    def test_conditional_rules_present(self, sv):
        cls = sv.get_class("MolecularAssignment")
        assert cls.rules, "MolecularAssignment should define conditional rules"
        gated = set()
        for r in cls.rules:
            if r.postconditions and r.postconditions.slot_conditions:
                gated.update(r.postconditions.slot_conditions.keys())
        for s in ["MZ_THEORETICAL", "ADDUCT", "DATABASE_SOURCE", "MOLECULAR_FORMULA",
                  "MASS_ERROR_PPM", "DATABASE_ID", "DATABASE_VERSION"]:
            assert s in gated, f"{s} not covered by any rule postcondition"


class TestPatterns:
    """Identifier pattern validation on RecordSet foreign keys."""

    def test_data_file_id_pattern_in_recordset(self, sv):
        slot = sv.induced_slot("HTAN_DATA_FILE_ID", "MolecularAssignment")
        assert slot.pattern
        rx = re.compile(slot.pattern)
        assert rx.match("HTA200_1234_D003")
        assert not rx.match("HTA200_1234_B002")  # biospecimen id should not match
