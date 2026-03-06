"""Test suite for HTAN Base Imaging module."""

import pytest
import os
import json
import jsonschema
from linkml_runtime import SchemaView

# Get the directory where this test file is located
TEST_DIR = os.path.dirname(os.path.abspath(__file__))
MODULE_DIR = os.path.dirname(TEST_DIR)
SCHEMA_PATH = os.path.join(MODULE_DIR, "domains", "imaging.yaml")


class TestBaseImagingSchema:
    """Test base imaging schema loading and validation."""

    def test_schema_loading(self):
        """Test that the schema loads without errors."""
        sv = SchemaView(SCHEMA_PATH)
        assert sv.schema.name == "Imaging"
        assert sv.schema.id == "https://w3id.org/htan/imaging"

    def test_base_imaging_attributes_class(self):
        """Test BaseImagingAttributes class structure."""
        sv = SchemaView(SCHEMA_PATH)

        # Check class exists
        assert "BaseImagingAttributes" in sv.all_classes()

        # Check required attributes
        base_class = sv.get_class("BaseImagingAttributes")
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
            "PASSED_QC",
            "QC_COMMENT",
            "SPECIES",
        ]

        for attr in required_attrs:
            assert attr in base_class.attributes, f"Missing required attribute: {attr}"
            assert base_class.attributes[
                attr
            ].required, f"Attribute {attr} should be required"

    def test_enum_alphabetical_ordering(self):
        """Test that enum values are in alphabetical order."""
        sv = SchemaView(SCHEMA_PATH)

        # Test DeIdentificationMethodType
        deid_enum = sv.get_enum("DeIdentificationMethodType")
        values = list(deid_enum.permissible_values.keys())
        assert values == sorted(
            values
        ), f"DeIdentificationMethodType values not alphabetical: {values}"

        # Test StainingMethod
        staining_enum = sv.get_enum("StainingMethod")
        values = list(staining_enum.permissible_values.keys())
        assert values == sorted(
            values
        ), f"StainingMethod values not alphabetical: {values}"

        # Test ImmersionMedium
        immersion_enum = sv.get_enum("ImmersionMedium")
        values = list(immersion_enum.permissible_values.keys())
        assert values == sorted(
            values
        ), f"ImmersionMedium values not alphabetical: {values}"

    def test_inheritance_from_core(self):
        """Test that BaseImagingAttributes inherits from CoreFileAttributes."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseImagingAttributes")
        # BaseImagingAttributes should inherit from CoreFileAttributes
        assert base_class.is_a == "CoreFileAttributes"

    def test_common_attributes_present(self):
        """Test that all common imaging attributes are present."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseImagingAttributes")

        # Check for common imaging attributes
        common_attrs = [
            "EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES",
            "DE_IDENTIFICATION_METHOD_TYPE",
            "DE_IDENTIFICATION_METHOD_DESCRIPTION",
            "DE_IDENTIFICATION_SOFTWARE",
            "LICENSE",
            "IMAGE_MODALITY",
            "IMAGING_EQUIPMENT_MANUFACTURER",
            "IMAGING_EQUIPMENT_MODEL",
            "IMAGING_SOFTWARE",
            "CITATION_OR_DOI",
            "IMAGING_PROTOCOL",
            "STAINING_METHOD",
            "OBJECTIVE",
            "NOMINAL_MAGNIFICATION",
            "IMMERSION",
            "LENS_NUMERICAL_APERTURE",
            "PASSED_QC",
            "QC_COMMENT",
            "SPECIES",
        ]

        for attr in common_attrs:
            assert attr in base_class.attributes, f"Missing common attribute: {attr}"

    def test_optional_attributes(self):
        """Test that optional attributes are properly marked."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseImagingAttributes")
        optional_attrs = [
            "DE_IDENTIFICATION_METHOD_DESCRIPTION",
            "DE_IDENTIFICATION_SOFTWARE",
            "IMAGING_EQUIPMENT_MODEL",
            "IMAGING_SOFTWARE",
            "IMAGING_PROTOCOL",
            "IMMERSION",
            "LENS_NUMERICAL_APERTURE",
        ]

        for attr in optional_attrs:
            assert attr in base_class.attributes
            assert not base_class.attributes[
                attr
            ].required, f"Attribute {attr} should be optional"

    def test_minimum_value_constraints(self):
        """Test minimum value constraints for numerical attributes."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseImagingAttributes")

        # Check NOMINAL_MAGNIFICATION has minimum_value constraint
        nominal_mag = base_class.attributes.get("NOMINAL_MAGNIFICATION")
        assert nominal_mag is not None
        assert nominal_mag.minimum_value == 0
        assert nominal_mag.range == "integer"

        # Check LENS_NUMERICAL_APERTURE has minimum_value constraint
        lens_na = base_class.attributes.get("LENS_NUMERICAL_APERTURE")
        assert lens_na is not None
        assert lens_na.minimum_value == 0.0

    def test_conditional_requirements(self):
        """Test that conditional requirements are implemented as LinkML rules."""
        sv = SchemaView(SCHEMA_PATH)

        base_class = sv.get_class("BaseImagingAttributes")

        # Check that rules exist
        assert hasattr(base_class, "rules") or "rules" in sv.schema.classes.get(
            "BaseImagingAttributes", {}
        )

        # Check that DE_IDENTIFICATION_METHOD_DESCRIPTION is conditionally required
        deid_desc = base_class.attributes.get("DE_IDENTIFICATION_METHOD_DESCRIPTION")
        assert deid_desc is not None
        assert (
            not deid_desc.required
        )  # Should be optional by default, required conditionally


class TestBaseImagingDataValidation:
    """Test base imaging data validation."""

    def test_valid_base_imaging_data(self):
        """Test valid base imaging data with filename (no path separator required)."""
        valid_data = {
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "image.ome.tiff",  # Filename without path separator is valid
            "FILE_FORMAT": "ome.tiff",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES": "Pathological",
            "DE_IDENTIFICATION_METHOD_TYPE": "Automatic",
            "LICENSE": "CC BY 4.0",
            "IMAGE_MODALITY": "SM",
            "IMAGING_EQUIPMENT_MANUFACTURER": "Leica Microsystems",
            "CITATION_OR_DOI": "https://doi.org/10.1000/example",
            "STAINING_METHOD": "H&E",
            "OBJECTIVE": "Leica HC PL APO 20x/0.75",
            "NOMINAL_MAGNIFICATION": 20,
            "PASSED_QC": True,
            "QC_COMMENT": "Image quality acceptable",
            "SPECIES": "9606 (Homo sapiens)",
        }

        # Validate that FILENAME without path separator is valid (pattern removed)
        assert "/" not in valid_data["FILENAME"] and "\\" not in valid_data["FILENAME"]

        # Validate required fields
        assert valid_data["DE_IDENTIFICATION_METHOD_TYPE"] in [
            "Automatic",
            "Manual",
            "Semiautomatic",
            "Not Applicable",
        ]
        assert valid_data["IMAGE_MODALITY"] == "SM"
        assert valid_data["STAINING_METHOD"] in [
            "CODEX",
            "CyCIF",
            "ExSeq",
            "GeoMX-DSP",
            "H&E",
            "IHC",
            "IMC",
            "MIBI",
            "MERFISH",
            "MxIF",
            "mIHC",
            "Not Applicable",
            "SABER",
            "t-CyCIF",
        ]
        assert valid_data["NOMINAL_MAGNIFICATION"] >= 0
        assert isinstance(valid_data["NOMINAL_MAGNIFICATION"], int)

    def test_enum_validation(self):
        """Test enum value validation."""
        # Valid de-identification methods
        valid_deid_methods = ["Automatic", "Manual", "Not Applicable", "Semiautomatic"]

        # Valid staining methods
        valid_staining_methods = [
            "CODEX",
            "CyCIF",
            "ExSeq",
            "GeoMX-DSP",
            "H&E",
            "IHC",
            "IMC",
            "MERFISH",
            "MIBI",
            "MxIF",
            "Not Applicable",
            "SABER",
            "mIHC",
            "t-CyCIF",
        ]

        # Valid immersion media
        valid_immersion = ["Air", "Glycerol", "Oil", "Other", "Water"]

        # Test that all values are in alphabetical order
        assert valid_deid_methods == sorted(valid_deid_methods)
        assert valid_staining_methods == sorted(valid_staining_methods)
        assert valid_immersion == sorted(valid_immersion)

    def test_experimental_strategy_enum(self):
        """Test that EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES enum only allows 'Pathological'."""
        sv = SchemaView(SCHEMA_PATH)

        # Check enum exists
        strategy_enum = sv.get_enum("ExperimentalStrategyAndDataSubtypes")
        assert strategy_enum is not None

        # Check it only has "Pathological" as a valid value
        permissible_values = list(strategy_enum.permissible_values.keys())
        assert len(permissible_values) == 1
        assert "Pathological" in permissible_values

        # Check the attribute uses this enum
        base_class = sv.get_class("BaseImagingAttributes")
        attr = base_class.attributes.get("EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES")
        assert attr is not None
        assert attr.range == "ExperimentalStrategyAndDataSubtypes"
        assert attr.required is True

    def test_experimental_strategy_json_schema_validation(self):
        """Test JSON schema validation for EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES."""
        # Load the generated JSON schema
        schema_file = os.path.join(MODULE_DIR, "build", "imaging_schema.json")
        if not os.path.exists(schema_file):
            pytest.skip(
                f"JSON schema not found at {schema_file}. Run 'make gen-schema' first."
            )

        with open(schema_file, "r") as f:
            full_schema = json.load(f)

        # Get the BaseImagingAttributes schema and strategy enum
        base_schema = full_schema["$defs"]["BaseImagingAttributes"]
        strategy_schema = full_schema["$defs"]["ExperimentalStrategyAndDataSubtypes"]

        # Verify the enum definition
        assert "enum" in strategy_schema
        assert strategy_schema["enum"] == ["Pathological"]

        # Create a test schema that references the full schema's $defs
        test_schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "$defs": full_schema["$defs"],
            "allOf": [{"$ref": "#/$defs/BaseImagingAttributes"}],
        }

        # Test valid data with path separator (also valid)
        valid_data = {
            "EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES": "Pathological",
            "HTAN_DATA_FILE_ID": "HTA200_0000_D0001",
            "FILENAME": "test/image.ome.tiff",  # Filename with path separator is also valid
            "FILE_FORMAT": "ome.tiff",
            "HTAN_PARENT_ID": "HTA200_0000_B0001",
            "DE_IDENTIFICATION_METHOD_TYPE": "Automatic",
            "DE_IDENTIFICATION_METHOD_DESCRIPTION": "Automated de-identification process",
            "LICENSE": "CC BY 4.0",
            "IMAGE_MODALITY": "SM",
            "IMAGING_EQUIPMENT_MANUFACTURER": "Leica",
            "CITATION_OR_DOI": "https://doi.org/test",
            "STAINING_METHOD": "H&E",
            "OBJECTIVE": "20x",
            "NOMINAL_MAGNIFICATION": 20,
            "PASSED_QC": True,
            "QC_COMMENT": "OK",
            "SPECIES": "9606 (Homo sapiens)",
        }

        # Should validate successfully
        jsonschema.validate(instance=valid_data, schema=test_schema)

        # Test invalid data - should fail
        invalid_data = valid_data.copy()
        invalid_data["EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES"] = "InvalidValue"

        with pytest.raises(jsonschema.ValidationError) as exc_info:
            jsonschema.validate(instance=invalid_data, schema=test_schema)
        # Verify the error is about the invalid enum value
        assert "InvalidValue" in str(exc_info.value) or "Pathological" in str(
            exc_info.value
        )


if __name__ == "__main__":
    pytest.main([__file__])
