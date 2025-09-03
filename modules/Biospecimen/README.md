# HTAN Biospecimen Module

## Overview

The HTAN Biospecimen module provides a base class for modules that require biospecimen identification. This module defines `BiospecimenAttributes` which extends `CoreFileAttributes` and makes `HTAN_BIOSPECIMEN_ID` required.

## Architecture

The Biospecimen module uses a clean inheritance chain:

```
BiospecimenAttributes → CoreFileAttributes
```

**Inheritance Benefits:**
- **Core File Attributes**: Gets universal file attributes (FILENAME, HTAN_DATA_FILE_ID, etc.) from `CoreFileAttributes`
- **Required Biospecimen ID**: Makes `HTAN_BIOSPECIMEN_ID` required for biospecimen-based modules
- **Clean Separation**: Only modules that need biospecimen identification inherit from this class

## Schema Structure

### BiospecimenAttributes
Defines attributes for modules that require biospecimen identification:

**Required Attributes:**
- `HTAN_BIOSPECIMEN_ID`: HTAN Biospecimen ID of the parent biospecimen (Primary Key)
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
- Required HTAN_BIOSPECIMEN_ID attribute
- Availability of core attributes through inheritance
