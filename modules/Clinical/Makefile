# Clinical Module Makefile

.PHONY: all clean test gen-schema gen-synapse-schema docs

# Environment variables
SCHEMA_NAME = htan_clinical
SOURCE_SCHEMA_PATH = domains/clinical.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_clinical/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-project --config-file ../../config/config.yaml -d $(BUILD_DIR) $(SOURCE_SCHEMA_PATH)
	mv $(BUILD_DIR)/*.py $(DATAMODEL_DIR)/

# Generate Synapse-compatible flat JSON schema
# Note: Clinical module has multiple domain schemas (demographics, diagnosis, etc.)
# This generates the main clinical.yaml schema. Individual domain schemas are
# generated in the json-schema-synapse.yml workflow.
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/Clinical/$(SOURCE_SCHEMA_PATH) \
		--class-name ClinicalData \
		--output modules/Clinical/$(BUILD_DIR)/clinical.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/clinical.flat.schema.json"

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=modules/Clinical/src:. poetry run pytest modules/Clinical/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +