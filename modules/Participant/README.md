# HTAN Participant Module

## Overview

The HTAN Participant module provides a base class for modules that require participant identification. This module defines `ParticipantAttributes` which extends `CoreFileAttributes` and makes `HTAN_PARTICIPANT_ID` required.

## Architecture

The Participant module uses a clean inheritance chain:

```
ParticipantAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: Gets universal file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes`
- **Required Participant ID**: Makes `HTAN_PARTICIPANT_ID` required for participant-based modules
- **Clean Separation**: Only modules that need participant identification inherit from this class

## Schema Structure

### ParticipantAttributes
Defines attributes for modules that require participant identification:

**Required Attributes:**
- `HTAN_PARTICIPANT_ID`: HTAN ID associated with a patient based on HTAN ID SOP (Primary Key)
- Base attributes (FILENAME, HTAN_DATA_FILE_ID, HTAN_PARENT_ID, FILE_FORMAT) come from inheritance

## Usage

### Schema Validation
```bash
# Validate schema
make validate

# Generate Python classes
make gen-python

# Generate JSON schema
make gen-json-schema

# Run tests
make test
```

## Dependencies

- LinkML runtime
- pytest (for testing)
- linkml-validate (for schema validation)

## Testing

The module includes comprehensive tests for:
- Schema loading and validation
- Inheritance from CoreFileAttributes
- Required HTAN_PARTICIPANT_ID attribute
- Availability of core attributes through inheritance

