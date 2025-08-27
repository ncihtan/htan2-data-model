# HTAN Biospecimen Module Makefile

.PHONY: all clean gen-python gen-json-schema test validate

all: gen-python gen-json-schema test

gen-python:
	gen-python domains/biospecimen.yaml > src/htan_biospecimen/datamodel/biospecimen.py

gen-json-schema:
	gen-json-schema domains/biospecimen.yaml > biospecimen_schema.json

test:
	python -m pytest tests/ -v

validate:
	linkml-validate domains/biospecimen.yaml

clean:
	rm -rf src/htan_biospecimen/datamodel/*.py
	rm -f biospecimen_schema.json
