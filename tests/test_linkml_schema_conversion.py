#!/usr/bin/env python3
"""Unit tests for LinkML to Synapse JSON Schema conversion functions."""

import json
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open

import pytest

from scripts.linkml_to_flat_synapse_jsonschema import (
    run_gen_json_schema,
    flatten_json_schema,
    _convert_to_plain_dict,
    fix_schema_version,
    _fix_schema_version_logic,
    remove_unsupported_fields,
    fix_additional_properties,
)


class TestConvertToPlainDict:
    """Test the _convert_to_plain_dict helper function."""

    def test_convert_dict(self):
        """Test converting a dictionary."""
        input_data = {"key": "value", "nested": {"inner": "data"}}
        result = _convert_to_plain_dict(input_data)
        assert result == input_data
        assert isinstance(result, dict)

    def test_convert_list(self):
        """Test converting a list."""
        input_data = [1, 2, {"key": "value"}, [3, 4]]
        result = _convert_to_plain_dict(input_data)
        assert result == input_data
        assert isinstance(result, list)

    def test_convert_mixed(self):
        """Test converting mixed data structures."""
        input_data = {
            "dict": {"key": "value"},
            "list": [1, 2, 3],
            "string": "test",
            "number": 42,
        }
        result = _convert_to_plain_dict(input_data)
        assert result == input_data

    def test_convert_primitive(self):
        """Test converting primitive values."""
        assert _convert_to_plain_dict("string") == "string"
        assert _convert_to_plain_dict(42) == 42
        assert _convert_to_plain_dict(True) is True
        assert _convert_to_plain_dict(None) is None


class TestFixSchemaVersionLogic:
    """Test the _fix_schema_version_logic helper function."""

    def test_update_old_schema_version(self):
        """Test updating old schema version to Draft-07."""
        data = {"$schema": "https://json-schema.org/draft/2019-09/schema"}
        result, message = _fix_schema_version_logic(data)

        assert result["$schema"] == "https://json-schema.org/draft-07/schema"
        assert "Updated $schema from" in message

    def test_keep_draft_07_schema(self):
        """Test keeping existing Draft-07 schema."""
        data = {"$schema": "https://json-schema.org/draft-07/schema"}
        result, message = _fix_schema_version_logic(data)

        assert result["$schema"] == "https://json-schema.org/draft-07/schema"
        assert "already uses Draft-07" in message

    def test_add_missing_schema(self):
        """Test adding missing $schema field."""
        data = {"type": "object", "properties": {}}
        result, message = _fix_schema_version_logic(data)

        assert result["$schema"] == "https://json-schema.org/draft-07/schema"
        assert "Added $schema field" in message

    def test_preserve_other_fields(self):
        """Test that other fields are preserved."""
        data = {
            "type": "object",
            "properties": {"test": {"type": "string"}},
            "$schema": "https://json-schema.org/draft/2019-09/schema",
        }
        result, message = _fix_schema_version_logic(data)

        assert result["type"] == "object"
        assert result["properties"] == {"test": {"type": "string"}}
        assert result["$schema"] == "https://json-schema.org/draft-07/schema"


class TestSchemaVersionFunctions:
    """Test schema version fixing functions."""

    def test_fix_schema_version_file_operations(self):
        """Test fix_schema_version with file operations."""
        test_data = {"$schema": "https://json-schema.org/draft/2019-09/schema"}

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(test_data, f)
            temp_file = f.name

        try:
            # Read the file
            with open(temp_file, "r") as f:
                data = json.load(f)

            # Process in memory
            result = fix_schema_version(data)

            # Write back to file
            with open(temp_file, "w") as f:
                json.dump(result, f)

            # Read and verify
            with open(temp_file, "r") as f:
                final_result = json.load(f)

            assert final_result["$schema"] == "https://json-schema.org/draft-07/schema"
        finally:
            Path(temp_file).unlink()


class TestRemoveUnsupportedFields:
    """Test removing unsupported fields."""

    def test_remove_unsupported_fields_logic(self):
        """Test the logic for removing unsupported fields."""
        data = {
            "$defs": {"test": "value"},
            "metamodel_version": "1.0",
            "version": "2.0",
            "type": "object",
            "properties": {"valid": {"type": "string"}},
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            temp_file = f.name

        try:
            # Read the file
            with open(temp_file, "r") as f:
                file_data = json.load(f)

            # Process in memory
            result = remove_unsupported_fields(file_data)

            # Write back to file
            with open(temp_file, "w") as f:
                json.dump(result, f)

            # Read and verify
            with open(temp_file, "r") as f:
                final_result = json.load(f)

            # Check that unsupported fields are removed
            assert "$defs" not in final_result
            assert "metamodel_version" not in final_result
            assert "version" not in final_result

            # Check that valid fields are preserved
            assert final_result["type"] == "object"
            assert final_result["properties"] == {"valid": {"type": "string"}}
        finally:
            Path(temp_file).unlink()

    def test_remove_nested_unsupported_fields(self):
        """Test removing unsupported fields in nested structures."""
        data = {
            "type": "object",
            "properties": {
                "nested": {
                    "$defs": {"nested_test": "value"},
                    "metamodel_version": "1.0",
                    "type": "string",
                }
            },
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            temp_file = f.name

        try:
            # Read the file
            with open(temp_file, "r") as f:
                file_data = json.load(f)

            # Process in memory
            result = remove_unsupported_fields(file_data)

            # Write back to file
            with open(temp_file, "w") as f:
                json.dump(result, f)

            # Read and verify
            with open(temp_file, "r") as f:
                final_result = json.load(f)

            # Check that nested unsupported fields are removed
            assert "$defs" not in final_result["properties"]["nested"]
            assert "metamodel_version" not in final_result["properties"]["nested"]

            # Check that valid fields are preserved
            assert final_result["properties"]["nested"]["type"] == "string"
        finally:
            Path(temp_file).unlink()


class TestFixAdditionalProperties:
    """Test fixing additionalProperties."""

    def test_fix_boolean_additional_properties(self):
        """Test converting boolean additionalProperties to objects."""
        data = {
            "type": "object",
            "additionalProperties": True,
            "properties": {
                "nested": {
                    "type": "object",
                    "additionalProperties": False,
                }
            },
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            temp_file = f.name

        try:
            # Read the file
            with open(temp_file, "r") as f:
                file_data = json.load(f)

            # Process in memory
            result = fix_additional_properties(file_data)

            # Write back to file
            with open(temp_file, "w") as f:
                json.dump(result, f)

            # Read and verify
            with open(temp_file, "r") as f:
                final_result = json.load(f)

            # Check that boolean additionalProperties are converted to objects
            assert final_result["additionalProperties"] == {}
            assert final_result["properties"]["nested"]["additionalProperties"] == {}
        finally:
            Path(temp_file).unlink()

    def test_preserve_object_additional_properties(self):
        """Test preserving object additionalProperties."""
        data = {
            "type": "object",
            "additionalProperties": {"type": "string"},
        }

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            json.dump(data, f)
            temp_file = f.name

        try:
            fix_additional_properties(temp_file)

            with open(temp_file, "r") as f:
                result = json.load(f)

            # Check that object additionalProperties are preserved
            assert result["additionalProperties"] == {"type": "string"}
        finally:
            Path(temp_file).unlink()


class TestFlattenJsonSchema:
    """Test JSON Schema flattening."""

    def test_flatten_json_schema_file_operations(self):
        """Test flatten_json_schema with file operations."""
        test_data = {
            "type": "object",
            "properties": {
                "ref_field": {"$ref": "#/definitions/test"},
            },
            "definitions": {
                "test": {"type": "string"},
            },
        }

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False
        ) as input_file:
            json.dump(test_data, input_file)
            input_path = input_file.name

        try:
            # Read the file
            with open(input_path, "r") as f:
                file_data = json.load(f)

            # Process in memory
            result = flatten_json_schema(file_data)

            # Check that the schema was processed (jsonref behavior may vary)
            assert "properties" in result
            # The ref should be resolved to the actual type
            assert result["properties"]["ref_field"]["type"] == "string"
        finally:
            Path(input_path).unlink()


class TestRunGenJsonSchema:
    """Test JSON Schema generation."""

    @patch("scripts.linkml_to_flat_synapse_jsonschema.JsonSchemaGenerator")
    def test_run_gen_json_schema(self, mock_generator):
        """Test run_gen_json_schema function."""
        # Mock the generator
        mock_instance = mock_generator.return_value
        mock_instance.serialize.return_value = '{"type": "object"}'

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_file = f.name

        try:
            run_gen_json_schema("test.yaml", "TestClass", temp_file)

            # Check that generator was called correctly
            mock_generator.assert_called_once_with("test.yaml")
            mock_instance.serialize.assert_called_once()

            # Check that output was written
            with open(temp_file, "r") as f:
                content = f.read()
            assert content == '{"type": "object"}'
        finally:
            Path(temp_file).unlink()

    @patch("scripts.linkml_to_flat_synapse_jsonschema.JsonSchemaGenerator")
    def test_run_gen_json_schema_with_class_name(self, mock_generator):
        """Test run_gen_json_schema with class name."""
        mock_instance = mock_generator.return_value
        mock_instance.serialize.return_value = '{"type": "object"}'

        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            temp_file = f.name

        try:
            run_gen_json_schema("test.yaml", "TestClass", temp_file)

            # Check that top_class was set
            assert mock_instance.top_class == "TestClass"
        finally:
            Path(temp_file).unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
