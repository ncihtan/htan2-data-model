# HTAN Participant Module Makefile

.PHONY: all clean gen-python gen-json-schema test validate

all: gen-python gen-json-schema test

gen-python:
	gen-python domains/participant.yaml > src/htan_participant/datamodel/participant.py

gen-json-schema:
	gen-json-schema domains/participant.yaml > participant_schema.json

test:
	python -m pytest tests/ -v

validate:
	linkml-validate domains/participant.yaml

clean:
	rm -rf src/htan_participant/datamodel/*.py
	rm -f participant_schema.json
