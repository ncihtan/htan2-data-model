# HTAN Base Imaging Module Makefile

.PHONY: all clean test gen-schema gen-synapse-schema docs validate

# Environment variables
SCHEMA_NAME = htan_imaging
SOURCE_SCHEMA_PATH = domains/imaging.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_imaging/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/imaging.py
	cp $(BUILD_DIR)/imaging.py $(DATAMODEL_DIR)/

# Generate Synapse-compatible flat JSON schema
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/Imaging/$(SOURCE_SCHEMA_PATH) \
		--class-name BaseImagingAttributes \
		--output modules/Imaging/$(BUILD_DIR)/imaging.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/imaging.flat.schema.json"

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Validate schema
validate:
	poetry run linkml-validate $(SOURCE_SCHEMA_PATH)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/Imaging/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +

