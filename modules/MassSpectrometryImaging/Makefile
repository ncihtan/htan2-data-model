# MassSpectrometryImaging Makefile

.PHONY: all clean test gen-schema gen-synapse-schema

# Environment variables
SCHEMA_NAME = htan_massspectrometryimaging
SOURCE_SCHEMA_PATH = domains/mass_spectrometry_imaging.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_massspectrometryimaging/datamodel

all: gen-schema test

# Generate Python classes and JSON schema
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/mass_spectrometry_imaging.py
	cp $(BUILD_DIR)/mass_spectrometry_imaging.py $(DATAMODEL_DIR)/
	poetry run gen-json-schema $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/mass_spectrometry_imaging_schema.json

# Generate Synapse-compatible flat JSON schema (per level class)
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/MassSpectrometryImaging/domains/level_1.yaml \
		--class-name MassSpectrometryImagingLevel1 \
		--output modules/MassSpectrometryImaging/$(BUILD_DIR)/mass_spectrometry_imaging_level_1.flat.schema.json
	@echo "Synapse-compatible schema generated in $(BUILD_DIR)"

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/MassSpectrometryImaging/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +
