# HTAN scATAC-seq Module Makefile

.PHONY: all clean test gen-schema gen-synapse-schema docs validate

# Environment variables
SCHEMA_NAME = htan_scatac_seq
SOURCE_SCHEMA_PATH = domains/scatac_seq.yaml
BUILD_DIR = build
DATAMODEL_DIR = src/htan_scatac_seq/datamodel
DOCS_DIR = docs

all: gen-schema test docs

# Generate schema classes
gen-schema:
	mkdir -p $(BUILD_DIR)
	mkdir -p $(DATAMODEL_DIR)
	poetry run gen-python $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/scatac_seq.py
	cp $(BUILD_DIR)/scatac_seq.py $(DATAMODEL_DIR)/
	poetry run gen-json-schema $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/scatac_seq_schema.json

# Generate Synapse-compatible flat JSON schema
gen-synapse-schema:
	mkdir -p $(BUILD_DIR)
	cd ../../ && poetry run python scripts/linkml_to_flat_synapse_jsonschema.py \
		modules/scATAC-seq/$(SOURCE_SCHEMA_PATH) \
		--class-name scATACseqData \
		--output modules/scATAC-seq/$(BUILD_DIR)/scatac_seq.flat.schema.json
	@echo "✅ Synapse-compatible schema generated: $(BUILD_DIR)/scatac_seq.flat.schema.json"

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Validate schema
validate:
	poetry run linkml-validate $(SOURCE_SCHEMA_PATH)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/scATAC-seq/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +
