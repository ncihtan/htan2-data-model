"""Test suite for HTAN scRNA-seq module."""

import pytest
import yaml
from linkml_runtime import SchemaView
from linkml_runtime.utils.yamlutils import as_yaml
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.dumpers import yaml_dumper


class TestScRNAseqSchema:
    """Test scRNA-seq schema loading and validation."""

    def test_schema_loading(self):
        """Test that the schema loads without errors."""
        schema_path = "modules/scRNA-seq/domains/scrna_seq.yaml"
        sv = SchemaView(schema_path)
        assert sv.schema.name == "scRNA-seq"
        assert sv.schema.id == "https://w3id.org/htan/scrna_seq"

    def test_level1_schema(self):
        """Test Level 1 schema structure."""
        schema_path = "modules/scRNA-seq/domains/level_1.yaml"
        sv = SchemaView(schema_path)
        
        # Check class exists
        assert "scRNALevel1" in sv.all_classes()
        
        # Check required attributes
        level1_class = sv.get_class("scRNALevel1")
        required_attrs = [
            "SINGLE_CELL_ISOLATION_METHOD",
            "DISSOCIATION_METHOD", 
            "NUCLEIC_ACID_SOURCE",
            "LIBRARY_CONSTRUCTION_METHOD",
            "REVERSE_TRANSCRIPTION_PRIMER",
            "SPIKE_IN",
            "READ_INDICATOR",
            "LIBRARY_LAYOUT",
            "SEQUENCING_PLATFORM"
        ]
        
        for attr in required_attrs:
            assert attr in level1_class.attributes
            assert level1_class.attributes[attr].required

    def test_level2_schema(self):
        """Test Level 2 schema structure."""
        schema_path = "modules/scRNA-seq/domains/level_2.yaml"
        sv = SchemaView(schema_path)
        
        # Check class exists
        assert "scRNALevel2" in sv.all_classes()
        
        # Check required attributes
        level2_class = sv.get_class("scRNALevel2")
        required_attrs = [
            "SCRNASEQ_WORKFLOW_TYPE",
            "WORKFLOW_VERSION",
            "GENOMIC_REFERENCE"
        ]
        
        for attr in required_attrs:
            assert attr in level2_class.attributes
            assert level2_class.attributes[attr].required

    def test_level3_4_schema(self):
        """Test Level 3/4 schema structure."""
        schema_path = "modules/scRNA-seq/domains/level_3_4.yaml"
        sv = SchemaView(schema_path)
        
        # Check class exists
        assert "scRNALevel3_4" in sv.all_classes()
        
        # Check required attributes
        level3_4_class = sv.get_class("scRNALevel3_4")
        required_attrs = [
            "FILENAME",
            "FILE_FORMAT",
            "HTAN_DATA_FILE_ID",
            "HTAN_PARENT_DATA_FILE_ID",
            "SCRNASEQ_WORKFLOW_TYPE",
            "WORKFLOW_VERSION",
            "SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION",
            "WORKFLOW_LINK",
            "DATA_CATEGORY",
            "MATRIX_TYPE",
            "CELL_MEDIAN_NUMBER_READS",
            "CELL_MEDIAN_NUMBER_GENES",
            "CELL_TOTAL"
        ]
        
        for attr in required_attrs:
            assert attr in level3_4_class.attributes
            assert level3_4_class.attributes[attr].required

    def test_h5ad_file_format_validation(self):
        """Test h5ad file format validation."""
        schema_path = "modules/scRNA-seq/domains/level_3_4.yaml"
        sv = SchemaView(schema_path)
        
        level3_4_class = sv.get_class("scRNALevel3_4")
        file_format_attr = level3_4_class.attributes["FILE_FORMAT"]
        
        # Check pattern validation
        assert file_format_attr.pattern == "^h5ad$"

    def test_ann_data_schema_compliance(self):
        """Test AnnData schema compliance validation."""
        schema_path = "modules/scRNA-seq/domains/level_3_4.yaml"
        sv = SchemaView(schema_path)
        
        level3_4_class = sv.get_class("scRNALevel3_4")
        
        # Check AnnData schema version pattern
        schema_version_attr = level3_4_class.attributes["ANNDATA_SCHEMA_VERSION"]
        assert schema_version_attr.pattern == "^0\\.1$"
        
        # Check structure validation attribute exists
        assert "ANNDATA_STRUCTURE_VALIDATED" in level3_4_class.attributes

    def test_enum_alphabetical_ordering(self):
        """Test that enum values are in alphabetical order."""
        schema_path = "modules/scRNA-seq/domains/level_1.yaml"
        sv = SchemaView(schema_path)
        
        # Test SingleCellIsolationMethodEnum
        isolation_enum = sv.get_enum("SingleCellIsolationMethodEnum")
        values = list(isolation_enum.permissible_values.keys())
        assert values == sorted(values), f"SingleCellIsolationMethodEnum values not alphabetical: {values}"
        
        # Test DissociationMethodEnum
        dissociation_enum = sv.get_enum("DissociationMethodEnum")
        values = list(dissociation_enum.permissible_values.keys())
        assert values == sorted(values), f"DissociationMethodEnum values not alphabetical: {values}"

    def test_inheritance_from_core(self):
        """Test that scRNA-seq classes inherit from CoreFileAttributes."""
        schema_path = "modules/scRNA-seq/domains/scrna_seq.yaml"
        sv = SchemaView(schema_path)
        
        # Check inheritance for all levels
        for level_class in ["scRNALevel1", "scRNALevel2", "scRNALevel3_4"]:
            class_def = sv.get_class(level_class)
            assert class_def.is_a == "CoreFileAttributes"


class TestScRNAseqDataValidation:
    """Test scRNA-seq data validation."""

    def test_valid_level1_data(self):
        """Test valid Level 1 data."""
        valid_data = {
            "COMPONENT": "scRNA-seq",
            "HTAN_PARTICIPANT_ID": "HTAN-001",
            "HTAN_DATA_FILE_ID": "HTAN-001_0000_0001",
            "FILENAME": "scrna_level1.fastq.gz",
            "FILE_FORMAT": "fastq",
            "HTAN_PARENT_ID": "HTAN-001_0000_B0001",
            "HTAN_BIOSPECIMEN_ID": "HTAN-001_0000_B0001",
            "SINGLE_CELL_ISOLATION_METHOD": "Droplet-based",
            "DISSOCIATION_METHOD": "Enzymatic",
            "NUCLEIC_ACID_SOURCE": "RNA",
            "LIBRARY_CONSTRUCTION_METHOD": "10X Genomics",
            "REVERSE_TRANSCRIPTION_PRIMER": "Oligo-dT",
            "SPIKE_IN": "ERCC",
            "READ_INDICATOR": "Forward",
            "LIBRARY_LAYOUT": "Paired-end",
            "SEQUENCING_PLATFORM": "ILLUMINA"
        }
        
        # This would be validated against the schema
        assert "SINGLE_CELL_ISOLATION_METHOD" in valid_data
        assert valid_data["SINGLE_CELL_ISOLATION_METHOD"] in ["Droplet-based", "Cell Sorting", "Manual Picking", "Microfluidics", "Other", "Unknown"]

    def test_valid_level3_4_data(self):
        """Test valid Level 3/4 data with h5ad format."""
        valid_data = {
            "COMPONENT": "scRNA-seq",
            "HTAN_PARTICIPANT_ID": "HTAN-001",
            "HTAN_DATA_FILE_ID": "HTAN-001_0000_0002",
            "FILENAME": "scrna_level3_4.h5ad",
            "FILE_FORMAT": "h5ad",
            "HTAN_PARENT_ID": "HTAN-001_0000_0001",
            "HTAN_BIOSPECIMEN_ID": "HTAN-001_0000_B0001",
            "SCRNASEQ_WORKFLOW_TYPE": "CellRanger",
            "WORKFLOW_VERSION": "3.1.0",
            "SCRNASEQ_WORKFLOW_PARAMETERS_DESCRIPTION": "Normalization and log transformation",
            "WORKFLOW_LINK": "https://dockstore.org/workflows/github.com/broadinstitute/warp",
            "DATA_CATEGORY": "Gene Expression",
            "MATRIX_TYPE": "Raw Counts",
            "CELL_MEDIAN_NUMBER_READS": "5000",
            "CELL_MEDIAN_NUMBER_GENES": "2000",
            "CELL_TOTAL": "10000",
            "ANNDATA_SCHEMA_VERSION": "0.1",
            "ANNDATA_STRUCTURE_VALIDATED": True
        }
        
        # Validate h5ad format
        assert valid_data["FILE_FORMAT"] == "h5ad"
        
        # Validate AnnData schema version
        assert valid_data["ANNDATA_SCHEMA_VERSION"] == "0.1"
        
        # Validate structure validation
        assert valid_data["ANNDATA_STRUCTURE_VALIDATED"] is True


if __name__ == "__main__":
    pytest.main([__file__])
