# Biospecimen Module Makefile
# Generates Python classes and JSON schema from LinkML YAML

# Configuration
SCHEMA_FILE = domains/biospecimen.yaml
OUTPUT_DIR = src/htan_biospecimen/datamodel
JSON_SCHEMA_FILE = biospecimen_schema.json

# LinkML generator commands
GEN_PYTHON = gen-python
GEN_JSON_SCHEMA = gen-json-schema

# Default target
all: python json-schema

# Generate Python classes
python:
	@echo "Generating Python classes for Biospecimen module..."
	$(GEN_PYTHON) $(SCHEMA_FILE) -o $(OUTPUT_DIR)
	@echo "✅ Python classes generated in $(OUTPUT_DIR)"

# Generate JSON schema
json-schema:
	@echo "Generating JSON schema for Biospecimen module..."
	$(GEN_JSON_SCHEMA) $(SCHEMA_FILE) -o $(JSON_SCHEMA_FILE)
	@echo "✅ JSON schema generated: $(JSON_SCHEMA_FILE)"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf $(OUTPUT_DIR)
	rm -f $(JSON_SCHEMA_FILE)
	@echo "✅ Cleaned generated files"

# Validate schema
validate:
	@echo "Validating Biospecimen schema..."
	linkml-validate $(SCHEMA_FILE)
	@echo "✅ Schema validation passed"

# Install dependencies
install:
	@echo "Installing Biospecimen module dependencies..."
	pip install -e .

# Run tests
test:
	@echo "Running Biospecimen module tests..."
	python -m pytest tests/ -v

# Help
help:
	@echo "Available targets:"
	@echo "  all         - Generate both Python classes and JSON schema"
	@echo "  python      - Generate Python classes only"
	@echo "  json-schema - Generate JSON schema only"
	@echo "  clean       - Remove generated files"
	@echo "  validate    - Validate the schema"
	@echo "  install     - Install module dependencies"
	@echo "  test        - Run tests"
	@echo "  help        - Show this help message"

.PHONY: all python json-schema clean validate install test help
