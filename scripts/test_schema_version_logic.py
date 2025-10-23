#!/usr/bin/env python3
"""Test the extracted schema version logic function."""

import pytest
from scripts.linkml_to_flat_synapse_jsonschema import _fix_schema_version_logic


def test_fix_schema_version_logic_updates_old_version():
    """Test that old schema versions are updated to Draft-07."""
    data = {"$schema": "https://json-schema.org/draft/2019-09/schema"}

    updated_data, message = _fix_schema_version_logic(data)

    assert updated_data["$schema"] == "https://json-schema.org/draft-07/schema"
    assert "Updated $schema from" in message


def test_fix_schema_version_logic_keeps_draft_07():
    """Test that Draft-07 schemas are not changed."""
    data = {"$schema": "https://json-schema.org/draft-07/schema"}

    updated_data, message = _fix_schema_version_logic(data)

    assert updated_data["$schema"] == "https://json-schema.org/draft-07/schema"
    assert "already uses Draft-07" in message


def test_fix_schema_version_logic_adds_missing_schema():
    """Test that missing $schema field is added."""
    data = {"type": "object", "properties": {}}

    updated_data, message = _fix_schema_version_logic(data)

    assert updated_data["$schema"] == "https://json-schema.org/draft-07/schema"
    assert "Added $schema field" in message


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v"])
