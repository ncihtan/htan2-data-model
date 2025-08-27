# HTAN scRNA-seq Module Makefile

.PHONY: all clean test gen-python gen-json-schema validate

all: gen-python gen-json-schema test

# Generate Python classes from LinkML schema
gen-python:
	gen-python domains/scrna_seq.yaml > src/htan_scrna_seq/datamodel/scrna_seq.py

# Generate JSON schema
gen-json-schema:
	gen-json-schema domains/scrna_seq.yaml > scrna_seq_schema.json

# Validate schema
validate:
	linkml-validate domains/scrna_seq.yaml

# Run tests
test:
	python -m pytest tests/ -v

# Clean generated files
clean:
	rm -rf src/htan_scrna_seq/datamodel/*.py
	rm -f scrna_seq_schema.json
	rm -rf __pycache__
	rm -rf .pytest_cache
