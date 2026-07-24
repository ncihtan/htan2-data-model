"""Tests for the HTAN scATAC-seq module."""

import re
import sys

import pytest
from linkml_runtime.utils.schemaview import SchemaView

# Generated dataclasses live under the module's src/ (used by the instance tests below).
sys.path.insert(0, "modules/scATAC-seq/src")

SCHEMA = "modules/scATAC-seq/domains/scatac_seq.yaml"
LEVEL1 = "modules/scATAC-seq/domains/level_1.yaml"
LEVEL2 = "modules/scATAC-seq/domains/level_2.yaml"
LEVEL3_4 = "modules/scATAC-seq/domains/level_3_4.yaml"

LEVEL_CLASSES = ["scATACLevel1", "scATACLevel2", "scATACLevel3and4"]

# Level-specific base class expectations. Level 1 inherits the shared single-cell
# layer (SingleCellLevel1Attributes), which in turn is_a BaseSequencingLevel1Attributes.
EXPECTED_BASE = {
    "scATACLevel1": "SingleCellLevel1Attributes",
    "scATACLevel2": "BaseSequencingLevel2Attributes",
    "scATACLevel3and4": "BaseSequencingLevel3Attributes",
}

LEVEL_REQUIRED = {
    "scATACLevel1": [
        "FILE_FORMAT", "FILENAME",
        "SINGLE_CELL_ISOLATION_METHOD", "DISSOCIATION_METHOD", "NUCLEIC_ACID_SOURCE",
        "LIBRARY_CONSTRUCTION_METHOD",
        "NUCLEUS_IDENTIFIER", "NUCLEI_BARCODE_READ", "NUCLEI_BARCODE_LENGTH",
        "SCATAC_SEQ_READ_1", "SCATAC_SEQ_READ_2", "TOTAL_NUMBER_OF_PASSING_NUCLEI",
        "SINGLE_NUCLEUS_BUFFER", "TRANSPOSITION_REACTION", "TOTAL_READS",
        "MAP_Q_30", "TOTAL_READ_PAIRS",
    ],
    "scATACLevel2": [
        "FILE_FORMAT", "FILENAME",
        "TOTAL_UNIQUELY_MAPPED", "TOTAL_UNMAPPED_READS", "MEDIAN_FRAGMENTS_PER_CELL",
        "NUMBER_OF_CELLS", "MEDIAN_PASSING_READS_PERCENTAGE",
        "DUPLICATE_READ_PAIRS", "CHIMERIC_READ_PAIRS", "UNMAPPED_READ_PAIRS",
        "LOW_MAP_Q", "PASSED_FILTERS",
    ],
    "scATACLevel3and4": [
        "FILE_FORMAT", "FILENAME",
        "N_COUNT_PEAKS", "N_FEATURE_PEAKS", "PERCENTAGE_READS_IN_PEAKS",
        "PEAKS_CALLING_SOFTWARE", "MEDIAN_FRACTION_OF_READS_IN_PEAKS",
        "ATAC_GENE_ACTIVITY_WORKFLOW_TYPE",
        "ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION", "CELL_TOTAL",
        "ANNDATA_SCHEMA_VERSION", "ANNDATA_STRUCTURE_VALIDATED",
    ],
}

LEVEL_OPTIONAL = {
    "scATACLevel1": [
        "CRYOPRESERVED_CELLS_IN_SAMPLE", "NUCLEI_BARCODE", "SCATAC_SEQ_READ_3",
        # RNA-workflow fields: optional for scATAC (no RT/spike-in step)
        "REVERSE_TRANSCRIPTION_PRIMER", "SPIKE_IN",
        # inherited base optional slots
        "SEQUENCING_BATCH_ID", "PROTOCOL_LINK",
    ],
    "scATACLevel2": [
        "AVERAGE_BASE_QUALITY", "AVERAGE_INSERT_SIZE", "AVERAGE_READ_LENGTH",
        "MEAN_COVERAGE", "PAIRS_ON_DIFF_CHR", "PROPORTION_READS_MAPPED",
        "PROPORTION_READS_DUPLICATED", "SHORT_READS", "CONTAMINATION",
        "CONTAMINATION_ERROR", "THRESHOLD_FOR_MINIMUM_PASSING_READS",
        # made optional per review: multiome-only / sparsely reported for snATAC
        "MEDIAN_GENES_PER_CELL", "MITOCHONDRIAL_READ_PAIRS",
    ],
    "scATACLevel3and4": [
        "TSS_FRAGMENTS", "TSS_ENRICHMENT", "TSS_PERCENTILE", "SEURAT_CLUSTERS",
        "BLACKLIST_RATIO", "NUCLEOSOME_SIGNAL", "N_COUNT_RNA", "N_FEATURE_RNA",
    ],
}

EXPECTED_ENUMS = [
    "DissociationMethodEnum", "LibraryConstructionMethodEnum", "NucleicAcidSourceEnum",
    "ReverseTranscriptionPrimerEnum", "SingleCellIsolationMethodEnum", "SpikeInEnum",
    "SequencingReadEnum", "SingleNucleusBufferEnum", "TranspositionReactionEnum",
    "ATACGeneActivityWorkflowTypeEnum",
]


@pytest.fixture(scope="module")
def sv():
    return SchemaView(SCHEMA)


class TestSchema:
    """Schema loading and container wiring."""

    def test_schema_loads(self, sv):
        assert sv is not None
        assert sv.schema.name == "scATAC-seq"
        assert sv.schema.id == "https://w3id.org/htan/scatac_seq"

    def test_container_class(self, sv):
        assert "scATACseqData" in sv.all_classes()
        slots = sv.class_slots("scATACseqData")
        for s in ["level1_data", "level2_data", "level3_4_data"]:
            assert s in slots, f"{s} missing from container"

    def test_container_slots_inlined(self, sv):
        """Ranges are identifier-bearing classes, so container slots must be inlined."""
        for s in ["level1_data", "level2_data", "level3_4_data"]:
            slot = sv.induced_slot(s, "scATACseqData")
            assert slot.inlined is True, f"{s} must be inlined"


class TestInheritance:
    """Level classes follow the shared sequencing hierarchy (CLAUDE.md rules)."""

    @pytest.mark.parametrize("cls,base", list(EXPECTED_BASE.items()))
    def test_level_base_class(self, sv, cls, base):
        assert cls in sv.all_classes()
        assert sv.get_class(cls).is_a == base, f"{cls} should inherit {base}"

    def test_single_cell_layer_chains_to_sequencing(self, sv):
        """The shared single-cell layer must sit under the sequencing Level 1 base."""
        sc = sv.get_class("SingleCellLevel1Attributes")
        assert sc is not None
        assert sc.is_a == "BaseSequencingLevel1Attributes"

    def test_anndata_mixin_applied(self, sv):
        assert "AnnDataComplianceMixin" in (sv.get_class("scATACLevel3and4").mixins or [])

    @pytest.mark.parametrize("cls", LEVEL_CLASSES)
    def test_levels_inherit_core_identifiers(self, sv, cls):
        slots = sv.class_slots(cls)
        for s in ["HTAN_DATA_FILE_ID", "HTAN_PARENT_ID", "FILENAME", "FILE_FORMAT"]:
            assert s in slots, f"{s} not inherited by {cls}"


class TestRequiredOptional:
    """Required / optional slot coverage for every level class."""

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

    @pytest.mark.parametrize("cls", LEVEL_CLASSES)
    def test_title_and_description(self, sv, cls):
        klass = sv.get_class(cls)
        for name, attr in klass.attributes.items():
            assert attr.title, f"{cls}.{name} missing title"
            assert attr.description, f"{cls}.{name} missing description"


class TestNumericBounds:
    """Spot-check numeric min/max constraints."""

    def test_barcode_length_min(self, sv):
        assert sv.induced_slot("NUCLEI_BARCODE_LENGTH", "scATACLevel1").minimum_value == 1

    def test_number_of_cells_min(self, sv):
        assert sv.induced_slot("NUMBER_OF_CELLS", "scATACLevel2").minimum_value == 1

    def test_proportion_bounds(self, sv):
        slot = sv.induced_slot("PROPORTION_READS_DUPLICATED", "scATACLevel2")
        assert slot.minimum_value == 0.0
        assert slot.maximum_value == 1.0

    def test_percentage_bounds(self, sv):
        slot = sv.induced_slot("PERCENTAGE_READS_IN_PEAKS", "scATACLevel3and4")
        assert slot.minimum_value == 0.0
        assert slot.maximum_value == 100.0


class TestConditionalRule:
    """AVERAGE_INSERT_SIZE is gated on a paired-end library layout."""

    def test_paired_end_rule_present(self, sv):
        cls = sv.get_class("scATACLevel2")
        gated, pre_values = set(), set()
        for r in cls.rules or []:
            if r.postconditions and r.postconditions.slot_conditions:
                gated.update(r.postconditions.slot_conditions.keys())
            pre = (r.preconditions.slot_conditions or {}) if r.preconditions else {}
            layout = pre.get("LIBRARY_LAYOUT")
            if layout and layout.equals_string:
                pre_values.add(layout.equals_string)
        assert "AVERAGE_INSERT_SIZE" in gated
        assert "Paired-end" in pre_values


class TestPatterns:
    """File-format / filename pattern validation per level."""

    def test_level1_fastq_patterns(self, sv):
        cls = sv.get_class("scATACLevel1")
        assert cls.attributes["FILE_FORMAT"].pattern == "^(fastq|fastq\\.gz)$"
        fn = re.compile(cls.attributes["FILENAME"].pattern)
        assert fn.match("reads.fastq")
        assert fn.match("reads.fastq.gz")
        assert fn.match("reads.fq.gz")
        assert not fn.match("reads.bam")

    def test_level2_bam_cram_patterns(self, sv):
        cls = sv.get_class("scATACLevel2")
        fmt = re.compile(cls.attributes["FILE_FORMAT"].pattern)
        fn = re.compile(cls.attributes["FILENAME"].pattern)
        assert fmt.match("bam") and fmt.match("cram")
        assert fn.match("aln.bam") and fn.match("aln.cram")
        assert not fn.match("aln.fastq")

    def test_level3_4_h5ad_bed_patterns(self, sv):
        cls = sv.get_class("scATACLevel3and4")
        fmt = re.compile(cls.attributes["FILE_FORMAT"].pattern)
        fn = re.compile(cls.attributes["FILENAME"].pattern)
        assert fmt.match("h5ad") and fmt.match("bed")
        assert fn.match("matrix.h5ad") and fn.match("peaks.bed")
        assert not fn.match("matrix.txt")

    def test_anndata_schema_version_pattern(self, sv):
        # Contributed by AnnDataComplianceMixin, so read the induced (merged) slot.
        slot = sv.induced_slot("ANNDATA_SCHEMA_VERSION", "scATACLevel3and4")
        assert slot.pattern == "^0\\.1$"


class TestEnums:
    """Enum presence, alphabetical ordering, and value descriptions."""

    def test_enums_present(self, sv):
        all_enums = sv.all_enums()
        for e in EXPECTED_ENUMS:
            assert e in all_enums, f"{e} missing"

    def test_enums_alphabetical(self, sv):
        for ename, enum in sv.all_enums().items():
            values = list(enum.permissible_values.keys())
            assert values == sorted(values), f"{ename} values not alphabetical: {values}"

    def test_permissible_values_have_descriptions(self, sv):
        for ename, enum in sv.all_enums().items():
            for vname, v in enum.permissible_values.items():
                assert v.description, f"{ename}.{vname} missing description"

    def test_seurat_clusters_multivalued(self, sv):
        assert sv.induced_slot("SEURAT_CLUSTERS", "scATACLevel3and4").multivalued is True


# ---------------------------------------------------------------------------
# Instance-level tests against the generated dataclasses: one valid load and one
# invalid rejection per class (satisfies the coverage rules' valid/invalid ask).
# ---------------------------------------------------------------------------
_CORE = dict(HTAN_DATA_FILE_ID="HTA200_1234_D001", HTAN_PARENT_ID=["HTA200_1234_B002"])

VALID_INSTANCES = {
    "scATACLevel1": dict(
        **_CORE, FILENAME="reads.fastq.gz", FILE_FORMAT="fastq.gz",
        LIBRARY_LAYOUT="Paired-end", SEQUENCING_PLATFORM="ILLUMINA",
        SINGLE_CELL_ISOLATION_METHOD="Droplet-based", DISSOCIATION_METHOD="Enzymatic",
        NUCLEIC_ACID_SOURCE="DNA", LIBRARY_CONSTRUCTION_METHOD="10X Genomics",
        REVERSE_TRANSCRIPTION_PRIMER="Oligo-dT", SPIKE_IN="None",
        NUCLEUS_IDENTIFIER="AACGTGAT", NUCLEI_BARCODE_READ="R2", NUCLEI_BARCODE_LENGTH=16,
        SCATAC_SEQ_READ_1="DNA Insert", SCATAC_SEQ_READ_2="Cell Barcode",
        TOTAL_NUMBER_OF_PASSING_NUCLEI=5000, SINGLE_NUCLEUS_BUFFER="10x",
        TRANSPOSITION_REACTION="Tn5", TOTAL_READS=1000000, MAP_Q_30=950000.0,
        TOTAL_READ_PAIRS=500000,
    ),
    "scATACLevel2": dict(
        **_CORE, FILENAME="aln.bam", FILE_FORMAT="bam",
        LIBRARY_LAYOUT="Paired-end", SEQUENCING_PLATFORM="ILLUMINA",
        GENOMIC_REFERENCE="GRCh38", GENOMIC_REFERENCE_URL="https://example.org/ref",
        GENOME_ANNOTATION_URL="https://example.org/annot",
        WORKFLOW_VERSION="2.0", WORKFLOW_LINK="https://dockstore.org/workflow",
        AVERAGE_INSERT_SIZE=250.0,
        TOTAL_UNIQUELY_MAPPED=800000, TOTAL_UNMAPPED_READS=20000,
        MEDIAN_FRAGMENTS_PER_CELL=1200.0, MEDIAN_GENES_PER_CELL=2000.0,
        NUMBER_OF_CELLS=5000, MEDIAN_PASSING_READS_PERCENTAGE=85.0,
        DUPLICATE_READ_PAIRS=10000, CHIMERIC_READ_PAIRS=500, UNMAPPED_READ_PAIRS=2000,
        LOW_MAP_Q=3000, MITOCHONDRIAL_READ_PAIRS=1500, PASSED_FILTERS=450000,
    ),
    "scATACLevel3and4": dict(
        **_CORE, FILENAME="matrix.h5ad", FILE_FORMAT="h5ad",
        LIBRARY_LAYOUT="Paired-end", SEQUENCING_PLATFORM="ILLUMINA",
        GENOMIC_REFERENCE="GRCh38", GENOMIC_REFERENCE_URL="https://example.org/ref",
        GENOME_ANNOTATION_URL="https://example.org/annot",
        WORKFLOW_VERSION="2.0", WORKFLOW_LINK="https://dockstore.org/workflow",
        N_COUNT_PEAKS=200000, N_FEATURE_PEAKS=50000, PERCENTAGE_READS_IN_PEAKS=65.0,
        PEAKS_CALLING_SOFTWARE="MACS2", MEDIAN_FRACTION_OF_READS_IN_PEAKS=0.65,
        ATAC_GENE_ACTIVITY_WORKFLOW_TYPE="ArchR",
        ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION="Default parameters",
        CELL_TOTAL=5000, ANNDATA_SCHEMA_VERSION="0.1", ANNDATA_STRUCTURE_VALIDATED=True,
    ),
}

_DROP_REQUIRED = {
    "scATACLevel1": "SINGLE_NUCLEUS_BUFFER",
    "scATACLevel2": "PASSED_FILTERS",
    "scATACLevel3and4": "PEAKS_CALLING_SOFTWARE",
}

# LinkML gen-python capitalizes the leading character of class names
# (scATACLevel1 -> ScATACLevel1), so the generated dataclass name differs
# from the schema class name.
_GENERATED_NAME = {
    "scATACLevel1": "ScATACLevel1",
    "scATACLevel2": "ScATACLevel2",
    "scATACLevel3and4": "ScATACLevel3and4",
}


@pytest.fixture(scope="module")
def dm():
    """The generated dataclass module (auto-generated on the branch by CI).

    Skipped cleanly (rather than erroring) if the generated classes are absent,
    e.g. a fresh checkout before ``make modules-gen``. The import lives in the
    fixture, so only the instance tests below depend on it; the schema-level
    tests run regardless.
    """
    return pytest.importorskip(
        "htan_scatac_seq.datamodel.scatac_seq",
        reason="generated dataclasses not present; run `make modules-gen`",
    )


class TestInstances:
    """Valid instances load; missing-required and bad-enum instances raise ValueError."""

    @pytest.mark.parametrize("cls_name,kwargs", list(VALID_INSTANCES.items()))
    def test_valid_instance_loads(self, dm, cls_name, kwargs):
        obj = getattr(dm, _GENERATED_NAME[cls_name])(**kwargs)
        assert obj is not None

    @pytest.mark.parametrize("cls_name", list(VALID_INSTANCES))
    def test_missing_required_raises(self, dm, cls_name):
        kwargs = dict(VALID_INSTANCES[cls_name])
        kwargs.pop(_DROP_REQUIRED[cls_name])
        with pytest.raises(ValueError):
            getattr(dm, _GENERATED_NAME[cls_name])(**kwargs)

    def test_bad_enum_value_raises(self, dm):
        kwargs = dict(VALID_INSTANCES["scATACLevel1"])
        kwargs["SINGLE_NUCLEUS_BUFFER"] = "NOT_A_REAL_VALUE"
        with pytest.raises(ValueError):
            dm.ScATACLevel1(**kwargs)


if __name__ == "__main__":
    pytest.main([__file__])
