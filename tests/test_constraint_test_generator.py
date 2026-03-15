#!/usr/bin/env python3
"""Unit tests for the constraint test generator."""

import json
import tempfile
from pathlib import Path

import jsonschema
import pytest

from scripts.generate_constraint_tests import (
    _valid_value_for_field,
    _valid_value_for_pattern,
    _collect_conditional_triggering_values,
    build_valid_record,
    generate_invalid_files,
    run,
)

# Minimal fixture schemas for testing

SIMPLE_SCHEMA = {
    "$schema": "https://json-schema.org/draft-07/schema",
    "type": "object",
    "additionalProperties": {},
    "properties": {
        "HTAN_PARTICIPANT_ID": {
            "type": "string",
            "pattern": r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})$",
        },
        "RACE": {
            "type": "string",
            "enum": ["White", "Asian", "Unknown"],
        },
        "SEX": {
            "type": "string",
            "enum": ["Male", "Female", "Unknown"],
        },
        "COUNT": {
            "type": "integer",
        },
        "NOTES": {
            "type": "string",
        },
    },
    "required": ["HTAN_PARTICIPANT_ID", "RACE", "SEX", "COUNT"],
}

CONDITIONAL_SCHEMA = {
    "$schema": "https://json-schema.org/draft-07/schema",
    "type": "object",
    "additionalProperties": {},
    "allOf": [
        {
            "if": {
                "properties": {"BIOSPECIMEN_TYPE": {"const": "Tissue"}},
                "required": ["BIOSPECIMEN_TYPE"],
            },
            "then": {
                "properties": {"TISSUE_SAMPLE_TYPE": {}},
                "required": ["TISSUE_SAMPLE_TYPE"],
            },
        }
    ],
    "properties": {
        "HTAN_BIOSPECIMEN_ID": {
            "type": "string",
            "pattern": r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(B[0-9]{1,20})$",
        },
        "BIOSPECIMEN_TYPE": {
            "type": "string",
            "enum": ["Tissue", "Blood", "DNA"],
        },
        "TISSUE_SAMPLE_TYPE": {
            "type": "string",
            "enum": ["Primary Tumor", "Normal"],
        },
        "HTAN_PARENT_ID": {
            "type": "array",
            "items": {
                "type": "string",
                "pattern": r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_([BD][0-9]{1,20})$",
            },
        },
    },
    "required": ["HTAN_BIOSPECIMEN_ID", "BIOSPECIMEN_TYPE", "HTAN_PARENT_ID"],
}


class TestValidValueForPattern:
    def test_participant_id_pattern(self):
        pattern = r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})$"
        value = _valid_value_for_pattern(pattern)
        import re
        assert re.match(pattern, value), f"{value!r} did not match participant ID pattern"

    def test_biospecimen_id_pattern(self):
        pattern = r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(B[0-9]{1,20})$"
        value = _valid_value_for_pattern(pattern)
        import re
        assert re.match(pattern, value)

    def test_data_file_id_pattern(self):
        pattern = r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$"
        value = _valid_value_for_pattern(pattern)
        import re
        assert re.match(pattern, value)

    def test_fastq_filename_pattern(self):
        pattern = r"^.+\.(fastq|fq)(\.gz)?$"
        value = _valid_value_for_pattern(pattern)
        import re
        assert re.match(pattern, value)


class TestValidValueForField:
    def test_enum_field_returns_first_value(self):
        field_schema = {"type": "string", "enum": ["Alpha", "Beta", "Gamma"]}
        value = _valid_value_for_field("MY_FIELD", field_schema)
        assert value == "Alpha"

    def test_integer_field(self):
        value = _valid_value_for_field("COUNT", {"type": "integer"})
        assert value == 1
        assert isinstance(value, int)

    def test_number_field(self):
        value = _valid_value_for_field("SCORE", {"type": "number"})
        assert value == 1.0

    def test_boolean_field(self):
        value = _valid_value_for_field("FLAG", {"type": "boolean"})
        assert value is True

    def test_array_field_with_pattern(self):
        field_schema = {
            "type": "array",
            "items": {
                "type": "string",
                "pattern": r"^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_([BD][0-9]{1,20})$",
            },
        }
        value = _valid_value_for_field("HTAN_PARENT_ID", field_schema)
        assert isinstance(value, list)
        assert len(value) == 1
        import re
        assert re.match(field_schema["items"]["pattern"], value[0])

    def test_string_field_without_constraints(self):
        value = _valid_value_for_field("NOTES", {"type": "string"})
        assert isinstance(value, str)
        assert len(value) > 0


class TestCollectConditionalTriggeringValues:
    def test_collects_triggers(self):
        triggers = _collect_conditional_triggering_values(CONDITIONAL_SCHEMA)
        assert "BIOSPECIMEN_TYPE" in triggers
        assert "Tissue" in triggers["BIOSPECIMEN_TYPE"]

    def test_empty_for_no_allof(self):
        triggers = _collect_conditional_triggering_values(SIMPLE_SCHEMA)
        assert triggers == {}


class TestBuildValidRecord:
    def test_simple_schema_valid(self):
        record = build_valid_record(SIMPLE_SCHEMA)
        jsonschema.validate(instance=record, schema=SIMPLE_SCHEMA)

    def test_simple_schema_has_required_fields(self):
        record = build_valid_record(SIMPLE_SCHEMA)
        for field in SIMPLE_SCHEMA["required"]:
            assert field in record, f"Missing required field: {field}"

    def test_conditional_schema_valid(self):
        record = build_valid_record(CONDITIONAL_SCHEMA)
        jsonschema.validate(instance=record, schema=CONDITIONAL_SCHEMA)

    def test_avoids_triggering_conditional(self):
        record = build_valid_record(CONDITIONAL_SCHEMA)
        # BIOSPECIMEN_TYPE should NOT be "Tissue" (which would require TISSUE_SAMPLE_TYPE)
        # OR if it is "Tissue", TISSUE_SAMPLE_TYPE must be present
        if record.get("BIOSPECIMEN_TYPE") == "Tissue":
            assert "TISSUE_SAMPLE_TYPE" in record


class TestGenerateInvalidFiles:
    def test_missing_required_fields(self):
        valid = build_valid_record(SIMPLE_SCHEMA)
        invalid_files = generate_invalid_files(SIMPLE_SCHEMA, valid)
        missing_files = [f for f, _ in invalid_files if f.startswith("invalid_missing_required_")]
        # One per required field
        assert len(missing_files) == len(SIMPLE_SCHEMA["required"])

    def test_missing_required_fails_validation(self):
        valid = build_valid_record(SIMPLE_SCHEMA)
        invalid_files = generate_invalid_files(SIMPLE_SCHEMA, valid)
        for filename, record in invalid_files:
            if filename.startswith("invalid_missing_required_"):
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(instance=record, schema=SIMPLE_SCHEMA)

    def test_bad_enum_fails_validation(self):
        valid = build_valid_record(SIMPLE_SCHEMA)
        invalid_files = generate_invalid_files(SIMPLE_SCHEMA, valid)
        for filename, record in invalid_files:
            if filename.startswith("invalid_bad_enum_"):
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(instance=record, schema=SIMPLE_SCHEMA)

    def test_bad_pattern_fails_validation(self):
        valid = build_valid_record(SIMPLE_SCHEMA)
        invalid_files = generate_invalid_files(SIMPLE_SCHEMA, valid)
        for filename, record in invalid_files:
            if filename.startswith("invalid_pattern_"):
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(instance=record, schema=SIMPLE_SCHEMA)

    def test_wrong_type_fails_validation(self):
        valid = build_valid_record(SIMPLE_SCHEMA)
        invalid_files = generate_invalid_files(SIMPLE_SCHEMA, valid)
        for filename, record in invalid_files:
            if filename.startswith("invalid_wrong_type_"):
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(instance=record, schema=SIMPLE_SCHEMA)

    def test_conditional_violation_fails_validation(self):
        valid = build_valid_record(CONDITIONAL_SCHEMA)
        invalid_files = generate_invalid_files(CONDITIONAL_SCHEMA, valid)
        for filename, record in invalid_files:
            if filename.startswith("invalid_conditional_"):
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(instance=record, schema=CONDITIONAL_SCHEMA)


class TestRunEndToEnd:
    def test_run_demographics_schema(self):
        """Test run() against the real Demographics schema if available."""
        schema_path = Path("JSON_Schemas/v1.3.0/HTAN.Demographics-v1.3.0-schema.json")
        if not schema_path.exists():
            pytest.skip("Demographics schema not found")

        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "Demographics"
            run(schema_path, output_dir)

            assert (output_dir / "valid.json").exists()

            invalid_files = list(output_dir.glob("invalid_*.json"))
            assert len(invalid_files) > 0

            # Load schema and validate all files
            with open(schema_path) as f:
                schema = json.load(f)

            with open(output_dir / "valid.json") as f:
                valid_data = json.load(f)
            jsonschema.validate(instance=valid_data, schema=schema)

            for invalid_path in invalid_files:
                with open(invalid_path) as f:
                    invalid_data = json.load(f)
                with pytest.raises(jsonschema.ValidationError):
                    jsonschema.validate(instance=invalid_data, schema=schema)

    def test_run_with_fixture_schema(self):
        """Test run() with an in-memory fixture schema written to disk."""
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            schema_path = tmpdir / "test_schema.json"
            output_dir = tmpdir / "output"

            with open(schema_path, "w") as f:
                json.dump(SIMPLE_SCHEMA, f)

            run(schema_path, output_dir)

            assert (output_dir / "valid.json").exists()
            assert len(list(output_dir.glob("invalid_*.json"))) > 0


class TestDemonstratorPostprocessing:
    """Tests for the deterministic post-processor in generate_demonstrator.py."""

    def test_closest_enum_exact_match(self):
        from scripts.generate_demonstrator import _closest_enum
        assert _closest_enum("White", ["White", "Asian", "Unknown"]) == "White"

    def test_closest_enum_fuzzy_match(self):
        from scripts.generate_demonstrator import _closest_enum
        # "First Line" should match "1st Line" better than completely unrelated values
        result = _closest_enum("First Line", ["1st Line", "2nd Line", "Other"])
        assert result in ("1st Line", "Other")  # fuzzy, not exact

    def test_closest_enum_case_insensitive(self):
        from scripts.generate_demonstrator import _closest_enum
        assert _closest_enum("white", ["White", "Asian"]) == "White"

    def test_postprocess_snaps_enum(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "COLOR": {"type": "string", "enum": ["Red", "Blue", "Green"]},
            },
        }
        record = {"COLOR": "red"}
        fixed = _postprocess_record(record, schema)
        assert fixed["COLOR"] == "Red"

    def test_postprocess_wraps_array(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "ITEMS": {"type": "array", "items": {"type": "string"}},
            },
        }
        record = {"ITEMS": "single_value"}
        fixed = _postprocess_record(record, schema)
        assert fixed["ITEMS"] == ["single_value"]

    def test_postprocess_coerces_string_type(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "NAME": {"type": "string"},
            },
        }
        record = {"NAME": 123}
        fixed = _postprocess_record(record, schema)
        assert fixed["NAME"] == "123"

    def test_postprocess_fills_conditional_field(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "TYPE": {"type": "string", "enum": ["Other", "Normal"]},
                "OTHER_SPECIFY": {"type": "string"},
            },
            "allOf": [{
                "if": {
                    "properties": {"TYPE": {"const": "Other"}},
                    "required": ["TYPE"],
                },
                "then": {
                    "properties": {"OTHER_SPECIFY": {}},
                    "required": ["OTHER_SPECIFY"],
                },
            }],
        }
        record = {"TYPE": "Other"}
        fixed = _postprocess_record(record, schema)
        assert "OTHER_SPECIFY" in fixed

    def test_postprocess_skips_non_triggered_conditional(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "TYPE": {"type": "string", "enum": ["Other", "Normal"]},
                "OTHER_SPECIFY": {"type": "string"},
            },
            "allOf": [{
                "if": {
                    "properties": {"TYPE": {"const": "Other"}},
                    "required": ["TYPE"],
                },
                "then": {
                    "properties": {"OTHER_SPECIFY": {}},
                    "required": ["OTHER_SPECIFY"],
                },
            }],
        }
        record = {"TYPE": "Normal"}
        fixed = _postprocess_record(record, schema)
        assert "OTHER_SPECIFY" not in fixed

    def test_postprocess_fills_toplevel_conditional(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "STATUS": {"type": "string", "enum": ["Alive", "Dead"]},
                "CAUSE": {"type": "string"},
            },
            "if": {
                "properties": {"STATUS": {"const": "Dead"}},
                "required": ["STATUS"],
            },
            "then": {
                "properties": {"CAUSE": {}},
                "required": ["CAUSE"],
            },
        }
        record = {"STATUS": "Dead"}
        fixed = _postprocess_record(record, schema)
        assert "CAUSE" in fixed

    def test_postprocess_snaps_array_enum(self):
        from scripts.generate_demonstrator import _postprocess_record
        schema = {
            "properties": {
                "TREATMENTS": {
                    "type": "array",
                    "items": {"enum": ["Chemo", "Radiation", "Surgery"]},
                },
            },
        }
        record = {"TREATMENTS": ["chemo", "surgery"]}
        fixed = _postprocess_record(record, schema)
        assert fixed["TREATMENTS"] == ["Chemo", "Surgery"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
