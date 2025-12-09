# Biospecimen Module Makefile

.PHONY: all clean test gen-schema gen-synapse-schema docs

# Environment variables
SCHEMA_NAME = htan_biospecimen
SOURCE_SCHEMA_PATH = domains/biospecimen.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_biospecimen/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/biospecimen.py
	cp $(BUILD_DIR)/biospecimen.py $(DATAMODEL_DIR)/

# Generate Synapse-compatible flat JSON schema
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/Biospecimen/$(SOURCE_SCHEMA_PATH) \
		--class-name BiospecimenData \
		--output modules/Biospecimen/$(BUILD_DIR)/biospecimen.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/biospecimen.flat.schema.json"

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/Biospecimen/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +



