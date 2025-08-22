# Contributing to HTAN LinkML

Thank you for your interest in contributing to the HTAN LinkML project! This document provides guidelines and step-by-step instructions for contributors.

## 🚀 Quick Start

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feat/your-module-name`
3. **Follow the development guidelines** below
4. **Run tests**: `make test`
5. **Submit a pull request**

## 📋 Development Guidelines

### Code Style
- **Python**: Use Black for formatting (`make format`)
- **YAML**: Follow existing indentation patterns (2 spaces)
- **Enums**: Organize alphabetically for consistency
- **Documentation**: Update README files for new modules

### Testing
- **All tests must pass** before submitting PR
- **Add tests** for new modules following existing patterns
- **Test schema loading** and validation
- **Verify inheritance** works correctly

## 🔧 Development Conventions

### **Enum Organization**
- All enums are **alphabetically ordered** for consistency
- Enum values within each enum are also alphabetically ordered
- This applies to both enum names and their permissible values

### **ENUM STYLE GUIDE**
- **Attribute slots**: `ALL_CAPS_WITH_UNDERSCORES`
- **Enums**: `CamelCase`
- **Titles**: `Title Case`
- **Descriptions**: `First word capital letter`

### **Schema Structure**
- **Inheritance**: Modules inherit from `CoreFileAttributes` for universal attributes
- **Validation**: Regex patterns for HTAN identifiers
- **Documentation**: Each attribute includes `title` and `description` fields

### **File Naming**
- **Domain files**: `domains/[domain_name].yaml`
- **Test files**: `tests/test_[module_name].py`
- **Generated code**: `src/htan_[module]/datamodel/`

### **Testing Strategy**
- **Schema loading**: Verify YAML files can be parsed
- **Inheritance**: Confirm Core module inheritance works correctly
- **Enums**: Validate enum definitions and values
- **Validation**: Test regex patterns and required fields

## 🏗️ Adding a New Module: Step-by-Step Guide

### Step 1: Create Module Directory Structure

```bash
mkdir -p modules/YourModule/{domains,src/htan_yourmodule/datamodel,tests}
```

**Required files to create:**
```
modules/YourModule/
├── README.md                    # Module documentation
├── Makefile                     # Build configuration
├── domains/
│   └── your_module.yaml        # Main schema file
├── src/htan_yourmodule/
│   ├── __init__.py             # Python package init
│   └── datamodel/
│       └── __init__.py         # Data model init
└── tests/
    └── test_your_module.py     # Test suite
```

### Step 2: Create Module Makefile

**File**: `modules/YourModule/Makefile`

```makefile
# YourModule Makefile

.PHONY: all clean test gen-schema docs

# Environment variables
SCHEMA_NAME = htan_yourmodule
SOURCE_SCHEMA_PATH = domains/your_module.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_yourmodule/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/your_module.py
	cp $(BUILD_DIR)/your_module.py $(DATAMODEL_DIR)/
	poetry run gen-json-schema $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/your_module_schema.json
	touch $(DATAMODEL_DIR)/schema_classes.py


# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/YourModule/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +
```

### Step 3: Create Main Schema File

**File**: `modules/YourModule/domains/your_module.yaml`

```yaml
name: YourModule
id: https://w3id.org/htan/your_module
description: HTAN YourModule Data Model Schema

imports:
  - linkml:types
  - linkml:extensions
  - ../../Core/domains/core  # ← Import Core module

prefixes:
  htan: https://w3id.org/htan/
  linkml: https://w3id.org/linkml/
  schema: http://schema.org/

default_prefix: htan

enums:
  YourEnum:
    permissible_values:
      "Value1":
        description: First value
      "Value2":
        description: Second value

classes:
  YourModuleData:
    is_a: CoreFileAttributes  # ← Inherit from Core
    description: Container for your module data
    attributes:
      YOUR_ATTRIBUTE:
        range: string
        required: true
        title: "Your Attribute"  # ← Add human-readable title
        description: Description of your attribute
```

### Step 4: Create Python Package Files

**File**: `modules/YourModule/src/htan_yourmodule/__init__.py`
```python
"""HTAN YourModule package."""
```

**File**: `modules/YourModule/src/htan_yourmodule/datamodel/__init__.py`
```python
"""HTAN YourModule data model."""
```

### Step 5: Create Test Suite

**File**: `modules/YourModule/tests/test_your_module.py`

```python
"""Tests for the HTAN YourModule."""

import pytest
from linkml_runtime.utils.schemaview import SchemaView


class TestYourModule:
    """Test cases for the YourModule."""

    def test_schema_loading(self):
        """Test that the YourModule schema can be loaded."""
        schema_path = "modules/YourModule/domains/your_module.yaml"
        sv = SchemaView(schema_path)
        assert sv is not None

    def test_core_inheritance(self):
        """Test that YourModule inherits from Core."""
        schema_path = "modules/YourModule/domains/your_module.yaml"
        sv = SchemaView(schema_path)
        
        # Check that the main class exists
        assert "YourModuleData" in sv.all_classes()
        
        # Check that it inherits from Core
        your_module_class = sv.get_class("YourModuleData")
        assert your_module_class.is_a == "CoreFileAttributes"

    def test_enums(self):
        """Test that enums are properly defined."""
        sv = SchemaView("modules/YourModule/domains/your_module.yaml")
        assert "YourEnum" in sv.all_enums()
```

### Step 6: Create Module README

**File**: `modules/YourModule/README.md`

```markdown
# HTAN YourModule

Description of your module and its purpose.

## Purpose

Brief description of what this module handles.

## Structure

- **Domain files**: Description of your domain structure
- **Attributes**: Key attributes and their purposes
- **Validation**: Any special validation rules

## Usage

```yaml
# Example usage
YourModuleData:
  COMPONENT: "Your Module"
  FILENAME: "example.txt"
  FILE_FORMAT: "txt"
  HTAN_PARTICIPANT_ID: "HTA200_2"
  HTAN_DATA_FILE_ID: "HTA200_2_12345"
  HTAN_PARENT_ID: "HTA200_2_B7001"
  YOUR_ATTRIBUTE: "example value"
```

## Testing

Run module tests:
```bash
cd modules/YourModule
make test
```

## Schema Generation

Generate Python classes and JSON schema:
```bash
cd modules/YourModule
make gen-schema
```

```

### Step 7: Update Root Makefile

**File**: `Makefile` (root level)

**Add your module to the MODULES list:**
```makefile
# List of modules (add new modules here)
MODULES = Clinical WES Core YourModule
```

**Update the format target:**
```makefile
format:
	$(RUN) black scripts/ tests/ modules/Clinical/tests/ modules/WES/tests/ modules/YourModule/tests/
```

### Step 8: Update Main README

**File**: `README.md` (root level)

**Add your module to the project structure:**
```markdown
### **YourModule**
- **Purpose**: Brief description
- **Location**: `modules/YourModule/`
- **Structure**: Description of structure
- **Features**: Key features
```

## 🔧 Key Requirements for New Modules

### 1. **Core Inheritance**
- **All modules must inherit** from `CoreFileAttributes`
- **Use `is_a: CoreFileAttributes`** in your main class
- **Import Core module**: `- ../../Core/domains/core`

### 2. **Title Fields**
- **Add `title` field** to all attributes
- **Use human-readable names**: `title: "Your Attribute"`
- **Follow existing patterns** for consistency

### 3. **Enum Organization**
- **Organize enums alphabetically**
- **Organize enum values alphabetically**
- **Include descriptions** for all values

### 4. **Testing**
- **Test schema loading**
- **Test Core inheritance**
- **Test enum definitions**
- **All tests must pass**

### 5. **Documentation**
- **Create comprehensive README**
- **Include usage examples**
- **Document any special requirements**

## 🧪 Testing Your Module

### Run Module Tests
```bash
cd modules/YourModule
make test
```

### Run All Tests
```bash
make test
```

### Generate Schema
```bash
cd modules/YourModule
make gen-schema
```

### Format Code
```bash
make format
```

## 📝 Pull Request Checklist

Before submitting a PR, ensure:

- [ ] **All tests pass**: `make test`
- [ ] **Code is formatted**: `make format`
- [ ] **Documentation is updated**: README files
- [ ] **Core inheritance is implemented**: `is_a: CoreFileAttributes`
- [ ] **Title fields are added**: All attributes have human-readable titles
- [ ] **Enums are organized**: Alphabetical order
- [ ] **Module is added to root Makefile**: MODULES list updated
- [ ] **Main README is updated**: Project structure documented

## 🤝 Getting Help

- **Check existing modules** for examples
- **Review the Core module** for inheritance patterns
- **Look at test files** for testing patterns
- **Ask questions** in GitHub issues or discussions

## 📚 Additional Resources

- **LinkML Documentation**: [https://linkml.io/](https://linkml.io/)
- **HTAN Phase 1**: [https://github.com/ncihtan/data-models](https://github.com/ncihtan/data-models)
- **Project README**: See main README.md for project overview

---

Thank you for contributing to the HTAN LinkML project! 🎉
