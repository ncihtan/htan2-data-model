"""Tests for the HTAN Mass Spectrometry Imaging (MSI) module."""

import re
import sys

import pytest
from linkml_runtime.utils.schemaview import SchemaView

# Generated dataclasses live under the module's src/ (used by the instance tests below).
sys.path.insert(0, "modules/MassSpectrometryImaging/src")

SCHEMA = "modules/MassSpectrometryImaging/domains/mass_spectrometry_imaging.yaml"

LEVEL_CLASSES = [
    "MassSpectrometryImagingLevel1",
    "MassSpectrometryImagingLevel2",
    "MassSpectrometryImagingLevel3",
    "MassSpectrometryImagingLevel4",
]

# Required / optional slot expectations for Levels 2-4 (Level 1 is covered in TestLevel1).
LEVEL_REQUIRED = {
    "MassSpectrometryImagingLevel2": [
        "SOFTWARE_AND_VERSION", "BASELINE_CORRECTION_METHOD", "PEAK_PICKING_METHOD",
        "PEAK_PICKING_SNR_THRESHOLD", "NORMALIZATION_METHOD", "MASS_ALIGNMENT_METHOD",
        "MASS_TOLERANCE_PPM", "MEDIAN_TIC", "TIC_CV", "MASS_ACCURACY_PPM",
        "PIXEL_COMPLETION_RATE", "NUM_DETECTED_PEAKS", "PASSED_QC",
    ],
    "MassSpectrometryImagingLevel3": [
        "NUM_ANNOTATED_CHANNELS", "NUM_UNKNOWN_CHANNELS", "SOFTWARE_AND_VERSION", "PASSED_QC",
    ],
    "MassSpectrometryImagingLevel4": [
        "SEGMENTATION_METHOD", "SEGMENTATION_CLASS_COUNT", "SEGMENTATION_REFERENCE_MODALITY",
        "PASSED_QC",
    ],
}
LEVEL_OPTIONAL = {
    "MassSpectrometryImagingLevel2": ["SMOOTHING_METHOD", "PROTOCOL_LINK", "QC_COMMENT"],
    "MassSpectrometryImagingLevel3": ["PROTOCOL_LINK", "QC_COMMENT"],
    "MassSpectrometryImagingLevel4": ["QC_COMMENT"],
}


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
            "CALIBRATION_TYPE", "CALIBRANT_MASSES",
            "TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE",
            "TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT",
            "SOFTWARE_AND_VERSION", "IBD_FILE_UUID", "PASSED_QC",
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
        # the rule gates all four matrix-prep fields on the MALDI-family techniques
        post_slots, pre_values = set(), set()
        for r in cls.rules or []:
            if r.postconditions and r.postconditions.slot_conditions:
                post_slots.update(r.postconditions.slot_conditions.keys())
            pre = (r.preconditions.slot_conditions or {}) if r.preconditions else {}
            mit = pre.get("MS_IONIZATION_TECHNIQUE")
            if mit and mit.any_of:
                pre_values.update(c.equals_string for c in mit.any_of)
        for slot in ["PREPARATION_MATRIX", "MATRIX_DEPOSITION_METHOD",
                     "PREPARATION_INSTRUMENT_VENDOR", "PREPARATION_INSTRUMENT_MODEL"]:
            assert slot in post_slots, f"{slot} not gated by the MALDI rule"
        assert {"MALDI", "MALDI_2", "IR_MALDESI"} == pre_values


class TestLevels234:
    """Required/optional slot coverage for Levels 2-4 (mirrors TestLevel1)."""

    @pytest.mark.parametrize(
        "cls,slot", [(c, s) for c, ss in LEVEL_REQUIRED.items() for s in ss]
    )
    def test_required(self, sv, cls, slot):
        assert sv.induced_slot(slot, cls).required is True, f"{slot} should be required in {cls}"

    @pytest.mark.parametrize(
        "cls,slot", [(c, s) for c, ss in LEVEL_OPTIONAL.items() for s in ss]
    )
    def test_optional(self, sv, cls, slot):
        assert not sv.induced_slot(slot, cls).required, f"{slot} should be optional in {cls}"


class TestSlotCompleteness:
    """Every attribute on every level class carries a title and description."""

    @pytest.mark.parametrize("cls", LEVEL_CLASSES + ["MolecularAssignment"])
    def test_title_and_description(self, sv, cls):
        klass = sv.get_class(cls)
        for name, attr in klass.attributes.items():
            assert attr.title, f"{cls}.{name} missing title"
            assert attr.description, f"{cls}.{name} missing description"


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


# ---------------------------------------------------------------------------
# Instance-level tests against the generated dataclasses: one valid load and one
# invalid rejection per class (satisfies the coverage rules' valid/invalid instance ask).
# ---------------------------------------------------------------------------
_CORE = dict(HTAN_DATA_FILE_ID="HTA200_1234_D001", HTAN_PARENT_ID=["HTA200_1234_B002"])

VALID_INSTANCES = {
    "MassSpectrometryImagingLevel1": dict(
        **_CORE, FILENAME="sample.imzML", FILE_FORMAT="imzML",
        MS_IONIZATION_TECHNIQUE="DESI", MASS_ANALYZER_TYPE="TOF", MASS_ANALYSIS_POLARITY="POS",
        ANALYTE_CLASS=["LIPIDS"], IS_TARGETED=False, ACQUISITION_INSTRUMENT_VENDOR="Bruker",
        ACQUISITION_INSTRUMENT_MODEL="timsTOF Flex", PIXEL_SIZE_X_UM=10.0, PIXEL_SIZE_Y_UM=10.0,
        MASS_TO_CHARGE_RANGE_LOW_VALUE=100.0, MASS_TO_CHARGE_RANGE_HIGH_VALUE=1000.0,
        ION_MOBILITY=False, SPECTRUM_TYPE="PROFILE", MASS_RESOLVING_POWER=40000,
        MS_SCAN_MODE="REFLECTRON", CALIBRATION_TYPE="LOCK_MASS",
        CALIBRANT_MASSES="622.0290, 922.0098",
        TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE=2,
        TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT="HOURS",
        SOFTWARE_AND_VERSION="timsControl 5.1", IBD_FILE_UUID="uuid-1234", PASSED_QC=True,
    ),
    "MassSpectrometryImagingLevel2": dict(
        **_CORE, FILENAME="sample_processed.imzML", FILE_FORMAT="imzML",
        SOFTWARE_AND_VERSION="SCiLS Lab 2024", BASELINE_CORRECTION_METHOD="TOP_HAT",
        PEAK_PICKING_METHOD="centroid", PEAK_PICKING_SNR_THRESHOLD=3.0,
        NORMALIZATION_METHOD="TIC", MASS_ALIGNMENT_METHOD="lock-mass", MASS_TOLERANCE_PPM=5.0,
        MEDIAN_TIC=1000.0, TIC_CV=12.5, MASS_ACCURACY_PPM=2.0, PIXEL_COMPLETION_RATE=99.5,
        NUM_DETECTED_PEAKS=1500, PASSED_QC=True,
    ),
    "MassSpectrometryImagingLevel3": dict(
        **_CORE, FILENAME="sample_annotated.ome.tiff", FILE_FORMAT="ome.tiff",
        NUM_ANNOTATED_CHANNELS=50, NUM_UNKNOWN_CHANNELS=10,
        SOFTWARE_AND_VERSION="Metaspace 2024", PASSED_QC=True,
    ),
    "MassSpectrometryImagingLevel4": dict(
        **_CORE, FILENAME="seg.ome.tiff", FILE_FORMAT="ome.tiff",
        SEGMENTATION_METHOD="K-means on TIC image", SEGMENTATION_CLASS_COUNT=5,
        SEGMENTATION_REFERENCE_MODALITY="MSI_NATIVE", PASSED_QC=True,
    ),
    "MolecularAssignment": dict(
        HTAN_DATA_FILE_ID="HTA200_1234_D003", CHANNEL_INDEX=1, MZ_OBSERVED=885.5498,
        MOLECULAR_NAME="PI(18:0/20:4)", SOFTWARE_AND_VERSION="Metabascape 5.0",
        CONFIDENCE_LEVEL=2, EVIDENCE_TYPE=["ACCURATE_MASS"],
    ),
}

# A required field to drop from each class to trigger a missing-required error.
_DROP_REQUIRED = {
    "MassSpectrometryImagingLevel1": "MS_IONIZATION_TECHNIQUE",
    "MassSpectrometryImagingLevel2": "BASELINE_CORRECTION_METHOD",
    "MassSpectrometryImagingLevel3": "NUM_ANNOTATED_CHANNELS",
    "MassSpectrometryImagingLevel4": "SEGMENTATION_METHOD",
    "MolecularAssignment": "MOLECULAR_NAME",
}


@pytest.fixture(scope="module")
def dm():
    """The generated dataclass module (auto-generated on the branch by CI)."""
    from htan_massspectrometryimaging.datamodel import mass_spectrometry_imaging as module

    return module


class TestInstances:
    """Valid instances load; missing-required and bad-enum instances raise ValueError."""

    @pytest.mark.parametrize("cls_name,kwargs", list(VALID_INSTANCES.items()))
    def test_valid_instance_loads(self, dm, cls_name, kwargs):
        obj = getattr(dm, cls_name)(**kwargs)
        assert obj is not None

    @pytest.mark.parametrize("cls_name", list(VALID_INSTANCES))
    def test_missing_required_raises(self, dm, cls_name):
        kwargs = dict(VALID_INSTANCES[cls_name])
        kwargs.pop(_DROP_REQUIRED[cls_name])
        with pytest.raises(ValueError):
            getattr(dm, cls_name)(**kwargs)

    def test_bad_enum_value_raises(self, dm):
        kwargs = dict(VALID_INSTANCES["MolecularAssignment"])
        kwargs["EVIDENCE_TYPE"] = ["NOT_A_REAL_VALUE"]
        with pytest.raises(ValueError):
            dm.MolecularAssignment(**kwargs)
