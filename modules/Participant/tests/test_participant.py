"""Tests for HTAN Participant Module."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


class TestParticipantModule:
    """Test Participant module functionality."""

    def test_schema_loading(self):
        """Test that the participant schema loads correctly."""
        schema_path = "modules/Participant/domains/participant.yaml"
        sv = SchemaView(schema_path)
        
        # Check that ParticipantAttributes class exists
        assert "ParticipantAttributes" in sv.all_classes()

    def test_inheritance_from_core(self):
        """Test that ParticipantAttributes inherits from CoreFileAttributes."""
        schema_path = "modules/Participant/domains/participant.yaml"
        sv = SchemaView(schema_path)
        
        participant_class = sv.get_class("ParticipantAttributes")
        assert participant_class.is_a == "CoreFileAttributes"

    def test_required_participant_id(self):
        """Test that HTAN_PARTICIPANT_ID is required in ParticipantAttributes."""
        schema_path = "modules/Participant/domains/participant.yaml"
        sv = SchemaView(schema_path)
        
        participant_class = sv.get_class("ParticipantAttributes")
        participant_id_slot = sv.get_slot("HTAN_PARTICIPANT_ID")
        
        # Check that HTAN_PARTICIPANT_ID is required in ParticipantAttributes
        assert participant_id_slot.required is True

    def test_core_attributes_available(self):
        """Test that core attributes are available through inheritance."""
        schema_path = "modules/Participant/domains/participant.yaml"
        sv = SchemaView(schema_path)
        
        participant_class = sv.get_class("ParticipantAttributes")
        
        # Check that core attributes are available
        core_attrs = ["FILENAME", "FILE_FORMAT", "HTAN_DATA_FILE_ID", "HTAN_PARENT_ID"]
        for attr in core_attrs:
            assert attr in sv.get_class_induced_slots("ParticipantAttributes")
