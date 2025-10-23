# Biospecimen Module Makefile

.PHONY: all clean test gen-schema docs

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
	poetry run gen-json-schema $(SOURCE_SCHEMA_PATH) > $(BUILD_DIR)/biospecimen_schema.json
	touch $(DATAMODEL_DIR)/schema_classes.py

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



