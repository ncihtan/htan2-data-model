# HTAN Participant Module Makefile

.PHONY: all clean gen-python gen-json-schema test validate

all: gen-python gen-json-schema test

gen-python:
	gen-python domains/participant.yaml -o src/htan_participant/datamodel

gen-json-schema:
	gen-json-schema domains/participant.yaml -o participant_schema.json

test:
	python -m pytest tests/ -v

validate:
	linkml-validate domains/participant.yaml

clean:
	rm -rf src/htan_participant/datamodel/*.py
	rm -f participant_schema.json
