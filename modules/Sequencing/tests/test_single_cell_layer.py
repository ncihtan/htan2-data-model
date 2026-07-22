"""Tests for the shared single-cell layer defined in the Sequencing base module.

SingleCellLevel1Attributes and AnnDataComplianceMixin live in sequencing.yaml so that
scRNA-seq and scATAC-seq can inherit / mix them in rather than duplicating them.
"""

import pytest
from linkml_runtime.utils.schemaview import SchemaView

SCHEMA = "modules/Sequencing/domains/sequencing.yaml"

SHARED_L1_ATTRS = [
    "SINGLE_CELL_ISOLATION_METHOD",
    "DISSOCIATION_METHOD",
    "CRYOPRESERVED_CELLS_IN_SAMPLE",
    "NUCLEIC_ACID_SOURCE",
    "LIBRARY_CONSTRUCTION_METHOD",
]

SHARED_SINGLE_CELL_ENUMS = [
    "SingleCellIsolationMethodEnum",
    "DissociationMethodEnum",
    "NucleicAcidSourceEnum",
    "LibraryConstructionMethodEnum",
    "ReverseTranscriptionPrimerEnum",
    "SpikeInEnum",
]


@pytest.fixture(scope="module")
def sv():
    return SchemaView(SCHEMA)


class TestSingleCellLayer:
    def test_level1_base_chains_to_sequencing(self, sv):
        cls = sv.get_class("SingleCellLevel1Attributes")
        assert cls is not None
        assert cls.is_a == "BaseSequencingLevel1Attributes"

    def test_shared_prep_attrs_present(self, sv):
        cls = sv.get_class("SingleCellLevel1Attributes")
        for attr in SHARED_L1_ATTRS:
            assert attr in cls.attributes, f"{attr} missing from SingleCellLevel1Attributes"

    def test_required_prep_attrs(self, sv):
        cls = sv.get_class("SingleCellLevel1Attributes")
        for attr in ["SINGLE_CELL_ISOLATION_METHOD", "DISSOCIATION_METHOD",
                     "NUCLEIC_ACID_SOURCE", "LIBRARY_CONSTRUCTION_METHOD"]:
            assert cls.attributes[attr].required is True
        assert cls.attributes["CRYOPRESERVED_CELLS_IN_SAMPLE"].required is not True

    def test_anndata_mixin(self, sv):
        mixin = sv.get_class("AnnDataComplianceMixin")
        assert mixin is not None
        assert mixin.mixin is True
        for attr in ["ANNDATA_SCHEMA_VERSION", "ANNDATA_STRUCTURE_VALIDATED"]:
            assert attr in mixin.attributes
        assert mixin.attributes["ANNDATA_SCHEMA_VERSION"].pattern == "^0\\.1$"


class TestSlotCompleteness:
    def test_every_attribute_has_title_and_description(self, sv):
        for cls_name in ["SingleCellLevel1Attributes", "AnnDataComplianceMixin"]:
            cls = sv.get_class(cls_name)
            for name, attr in cls.attributes.items():
                assert attr.title, f"{cls_name}.{name} missing title"
                assert attr.description, f"{cls_name}.{name} missing description"


class TestSharedEnums:
    def test_single_cell_enums_present(self, sv):
        all_enums = sv.all_enums()
        for e in SHARED_SINGLE_CELL_ENUMS:
            assert e in all_enums, f"{e} missing"

    def test_enums_alphabetical(self, sv):
        for ename, enum in sv.all_enums().items():
            values = list(enum.permissible_values.keys())
            assert values == sorted(values), f"{ename} values not alphabetical: {values}"

    def test_permissible_values_have_descriptions(self, sv):
        for ename, enum in sv.all_enums().items():
            for vname, v in enum.permissible_values.items():
                assert v.description, f"{ename}.{vname} missing description"


if __name__ == "__main__":
    pytest.main([__file__])
