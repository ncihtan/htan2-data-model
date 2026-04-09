# Multiplex Microscopy Module Makefile

.PHONY: all clean test gen-schema gen-synapse-schema docs

# Environment variables
SCHEMA_NAME = htan_multiplexmicroscopy
SOURCE_SCHEMA_PATH = domains/multiplex_microscopy.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_multiplexmicroscopy/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/multiplex_microscopy.py
	cp $(BUILD_DIR)/multiplex_microscopy.py $(DATAMODEL_DIR)/

# Generate Synapse-compatible flat JSON schemas
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/MultiplexMicroscopy/$(SOURCE_SCHEMA_PATH) \
		--class-name MultiplexMicroscopyData \
		--output modules/MultiplexMicroscopy/$(BUILD_DIR)/multiplex_microscopy.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/multiplex_microscopy.flat.schema.json"
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/MultiplexMicroscopy/domains/multiplex_microscopy_channel_metadata.yaml \
		--class-name ChannelMetadata \
		--output modules/MultiplexMicroscopy/$(BUILD_DIR)/channel_metadata.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/channel_metadata.flat.schema.json"

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/MultiplexMicroscopy/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +

