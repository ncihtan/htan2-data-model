# HTAN Base Sequencing Module Makefile

.PHONY: all clean test gen-python gen-json-schema validate

all: gen-python gen-json-schema test

# Generate Python classes from LinkML schema
gen-python:
	gen-python domains/sequencing.yaml > src/htan_sequencing/datamodel/sequencing.py

# Generate JSON schema
gen-json-schema:
	gen-json-schema domains/sequencing.yaml > sequencing_schema.json

# Validate schema
validate:
	linkml-validate domains/sequencing.yaml

# Run tests
test:
	python -m pytest tests/ -v

# Clean generated files
clean:
	rm -rf src/htan_sequencing/datamodel/*.py
	rm -f sequencing_schema.json
	rm -rf __pycache__
	rm -rf .pytest_cache
