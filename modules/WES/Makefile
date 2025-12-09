# WES Module Makefile

.PHONY: all clean test gen-schema gen-synapse-schema docs

# Environment variables
SCHEMA_NAME = htan_wes
SOURCE_SCHEMA_PATH = domains/wes.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_wes/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/wes.py
	cp $(BUILD_DIR)/wes.py $(DATAMODEL_DIR)/

# Generate Synapse-compatible flat JSON schema
# Note: This generates from level_1.yaml which is used in the workflow
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/WES/domains/level_1.yaml \
		--class-name BulkWESLevel1 \
		--output modules/WES/$(BUILD_DIR)/wes.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/wes.flat.schema.json"

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/WES/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +
