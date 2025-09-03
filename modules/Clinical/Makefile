# Clinical Module Makefile

.PHONY: all clean test gen-schema docs

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
	touch $(DATAMODEL_DIR)/schema_classes.py

# Generate documentation
docs:
	mkdir -p $(DOCS_DIR)
	poetry run gen-doc --no-mergeimports $(SOURCE_SCHEMA_PATH) -d $(DOCS_DIR)

# Run module-specific tests
test:
	cd ../../ && PYTHONPATH=. poetry run pytest modules/Clinical/tests/ -v

# Clean build artifacts
clean:
	rm -rf $(BUILD_DIR)/*
	find . -type d -name "__pycache__" -exec rm -rf {} +