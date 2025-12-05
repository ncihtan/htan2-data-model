"""Tests for the HTAN Digital Pathology module."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


class TestDigitalPathology:
    """Test cases for the Digital Pathology module."""

    def test_schema_loading(self):
        """Test that the Digital Pathology schema can be loaded."""
        schema_path = "modules/DigitalPathology/domains/digital_pathology.yaml"
        sv = SchemaView(schema_path)
        assert sv is not None

    def test_core_inheritance(self):
        """Test that Digital Pathology inherits from BaseImagingAttributes (which inherits from CoreFileAttributes)."""
        schema_path = "modules/DigitalPathology/domains/digital_pathology.yaml"
        sv = SchemaView(schema_path)
        
        # Check that the main class exists
        assert "DigitalPathologyData" in sv.all_classes()
        
        # Check that it inherits from BaseImagingAttributes
        digital_pathology_class = sv.get_class("DigitalPathologyData")
        assert digital_pathology_class.is_a == "BaseImagingAttributes"
        
        # Verify BaseImagingAttributes inherits from CoreFileAttributes
        base_imaging_class = sv.get_class("BaseImagingAttributes")
        assert base_imaging_class.is_a == "CoreFileAttributes"

    def test_enums(self):
        """Test that enums are properly defined."""
        sv = SchemaView("modules/DigitalPathology/domains/digital_pathology.yaml")
        
        # Check main schema enums
        assert "DeIdentificationMethodType" in sv.all_enums()
        assert "ImageModality" in sv.all_enums()
        assert "StainingMethod" in sv.all_enums()
        assert "ImmersionMedium" in sv.all_enums()
        assert "AnnotationType" in sv.all_enums()

    def test_required_attributes(self):
        """Test that required attributes are properly defined."""
        sv = SchemaView("modules/DigitalPathology/domains/digital_pathology.yaml")
        
        digital_pathology_class = sv.get_class("DigitalPathologyData")
        required_slots = sv.class_slots("DigitalPathologyData")
        
        # Check some key required attributes
        required_attrs = [
            "EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES",
            "DE_IDENTIFICATION_METHOD_TYPE",
            "LICENSE",
            "IMAGE_MODALITY",
            "IMAGING_EQUIPMENT_MANUFACTURER",
            "CITATION_OR_DOI",
            "STAINING_METHOD",
            "OBJECTIVE",
            "NOMINAL_MAGNIFICATION",
            "HAS_ANNOTATIONS",
            "HAS_SLIDE_LABEL",
            "DE_IDENTIFIED",
            "PASSED_QC",
            "QC_COMMENT",
            "SPECIES",
            "ORGAN_OR_TISSUE",
            "TISSUE_FIXATIVE",
            "EMBEDDING_MEDIUM"
        ]
        
        for attr in required_attrs:
            assert attr in required_slots
            slot = sv.get_slot(attr)
            assert slot.required is True

    def test_enum_values(self):
        """Test that enum values are properly defined."""
        sv = SchemaView("modules/DigitalPathology/domains/digital_pathology.yaml")
        
        # Test DeIdentificationMethodType enum
        de_id_enum = sv.get_enum("DeIdentificationMethodType")
        assert "Automatic" in de_id_enum.permissible_values
        assert "Manual" in de_id_enum.permissible_values
        assert "Not Applicable" in de_id_enum.permissible_values
        assert "Semiautomatic" in de_id_enum.permissible_values
        
        # Test StainingMethod enum
        staining_enum = sv.get_enum("StainingMethod")
        assert "H&E" in staining_enum.permissible_values
        assert "IHC" in staining_enum.permissible_values
        assert "CyCIF" in staining_enum.permissible_values
        assert "Not Applicable" in staining_enum.permissible_values

    def test_validation_patterns(self):
        """Test that validation patterns are properly defined."""
        sv = SchemaView("modules/DigitalPathology/domains/digital_pathology.yaml")
        
        # Test ICD-O pattern for organ_or_tissue
        organ_tissue_slot = sv.get_slot("ORGAN_OR_TISSUE")
        assert organ_tissue_slot.pattern == "^[A-Z][0-9]{2}\\.[0-9]{1,2}$"

    def test_conditional_requirements(self):
        """Test conditional requirements are properly defined."""
        sv = SchemaView("modules/DigitalPathology/domains/digital_pathology.yaml")
        
        # Test that conditional attributes are not required by default
        de_id_desc_slot = sv.get_slot("DE_IDENTIFICATION_METHOD_DESCRIPTION")
        assert de_id_desc_slot.required is False
        
        slide_label_redacted_slot = sv.get_slot("SLIDE_LABEL_REDACTED")
        assert slide_label_redacted_slot.required is False
        
        annotation_type_slot = sv.get_slot("ANNOTATION_TYPE")
        assert annotation_type_slot.required is False
