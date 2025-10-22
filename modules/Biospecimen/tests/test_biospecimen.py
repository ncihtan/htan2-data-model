"""
Test cases for HTAN Biospecimen module.
"""

import pytest
from pathlib import Path
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

# Try different import paths for Biospecimen
BiospecimenData = None
try:
    from htan_biospecimen.datamodel.biospecimen import BiospecimenData
except ImportError:
    try:
        from modules.Biospecimen.src.htan_biospecimen.datamodel.biospecimen import (
            BiospecimenData,
        )
    except ImportError:
        # If neither works, BiospecimenData will be None and tests will be skipped
        pass


@pytest.fixture
def base_dir():
    """Base directory for tests."""
    return Path(__file__).parent.parent


@pytest.fixture
def schema_path(base_dir):
    """Schema path."""
    return base_dir / "domains" / "biospecimen.yaml"


@pytest.fixture
def schema_view(schema_path):
    """Schema view."""
    return SchemaView(str(schema_path))


@pytest.mark.skipif(BiospecimenData is None, reason="BiospecimenData not available")
def test_schema_loads(schema_view):
    """Test that the schema can be loaded."""
    assert schema_view is not None
    assert "BiospecimenData" in schema_view.all_classes()


@pytest.mark.skipif(BiospecimenData is None, reason="BiospecimenData not available")
def test_biospecimen_creation():
    """Test creating a basic biospecimen record."""
    biospecimen = BiospecimenData(
        COMPONENT="Biospecimen",
        HTAN_BIOSPECIMEN_ID="HTA200_2_7001",
        HTAN_PARENT_ID="HTA200_2_B7001",
        BIOSPECIMEN_TYPE="Tissue",
        ACQUISITION_METHOD_TYPE="Surgical Resection",
        SITE_OF_RESECTION_OR_BIOPSY="UBERON:0000948",  # Stomach
        SPECIMEN_LATERALITY="Left",
        PRESERVATION_METHOD="Formalin Fixed",
        SPECIMEN_CELLULAR_ARCHITECTURE="Tumor",
        SHIPPING_CONDITION_TYPE="Frozen",
        AGE_IN_DAYS_AT_SPECIMEN_COLLECTION=1000,
        AGE_IN_DAYS_AT_SPECIMEN_PROCESSING=1001,
    )
    
    assert biospecimen.COMPONENT == "Biospecimen"
    assert biospecimen.HTAN_BIOSPECIMEN_ID == "HTA200_2_7001"
    assert biospecimen.BIOSPECIMEN_TYPE == "Tissue"


@pytest.mark.skipif(BiospecimenData is None, reason="BiospecimenData not available")
def test_required_fields():
    """Test that missing required fields are caught."""
    with pytest.raises(ValueError):
        BiospecimenData(
            COMPONENT="Biospecimen"
            # Missing required fields
        )


@pytest.mark.skipif(BiospecimenData is None, reason="BiospecimenData not available")
def test_enum_validation():
    """Test that invalid enum values are caught."""
    with pytest.raises(ValueError):
        BiospecimenData(
            COMPONENT="Biospecimen",
            HTAN_BIOSPECIMEN_ID="HTA200_2_7001",
            HTAN_PARENT_ID="HTA200_2_B7001",
            BIOSPECIMEN_TYPE="InvalidType",  # Invalid enum value
            ACQUISITION_METHOD_TYPE="Surgical Resection",
            SITE_OF_RESECTION_OR_BIOPSY="UBERON:0000948",
            SPECIMEN_LATERALITY="Left",
            PRESERVATION_METHOD="Formalin Fixed",
            SPECIMEN_CELLULAR_ARCHITECTURE="Tumor",
            SHIPPING_CONDITION_TYPE="Frozen",
            AGE_IN_DAYS_AT_SPECIMEN_COLLECTION=1000,
            AGE_IN_DAYS_AT_SPECIMEN_PROCESSING=1001,
        )


@pytest.mark.skipif(BiospecimenData is None, reason="BiospecimenData not available")
def test_numeric_validation():
    """Test that invalid numeric values are caught."""
    with pytest.raises(ValueError):
        BiospecimenData(
            COMPONENT="Biospecimen",
            HTAN_BIOSPECIMEN_ID="HTA200_2_7001",
            HTAN_PARENT_ID="HTA200_2_B7001",
            BIOSPECIMEN_TYPE="Tissue",
            ACQUISITION_METHOD_TYPE="Surgical Resection",
            SITE_OF_RESECTION_OR_BIOPSY="UBERON:0000948",
            SPECIMEN_LATERALITY="Left",
            PRESERVATION_METHOD="Formalin Fixed",
            SPECIMEN_CELLULAR_ARCHITECTURE="Tumor",
            SHIPPING_CONDITION_TYPE="Frozen",
            AGE_IN_DAYS_AT_SPECIMEN_COLLECTION=-100,  # Invalid negative age
            AGE_IN_DAYS_AT_SPECIMEN_PROCESSING=1001,
        )


@pytest.mark.skipif(BiospecimenData is None, reason="BiospecimenData not available")
def test_conditional_requirements():
    """Test conditional requirement validation."""
    # Test that TUMOR_CLASSIFICATION is required when SPECIMEN_CELLULAR_ARCHITECTURE=Tumor
    with pytest.raises(ValueError):
        BiospecimenData(
            COMPONENT="Biospecimen",
            HTAN_BIOSPECIMEN_ID="HTA200_2_7001",
            HTAN_PARENT_ID="HTA200_2_B7001",
            BIOSPECIMEN_TYPE="Tissue",
            ACQUISITION_METHOD_TYPE="Surgical Resection",
            SITE_OF_RESECTION_OR_BIOPSY="UBERON:0000948",
            SPECIMEN_LATERALITY="Left",
            PRESERVATION_METHOD="Formalin Fixed",
            SPECIMEN_CELLULAR_ARCHITECTURE="Tumor",  # Requires TUMOR_CLASSIFICATION
            SHIPPING_CONDITION_TYPE="Frozen",
            AGE_IN_DAYS_AT_SPECIMEN_COLLECTION=1000,
            AGE_IN_DAYS_AT_SPECIMEN_PROCESSING=1001,
            # Missing TUMOR_CLASSIFICATION
        )





