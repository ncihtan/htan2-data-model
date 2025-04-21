MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := help
.DELETE_ON_ERROR:
.SUFFIXES:
.SECONDARY:

# environment variables
.EXPORT_ALL_VARIABLES:
ifdef LINKML_ENVIRONMENT_FILENAME
include ${LINKML_ENVIRONMENT_FILENAME}
else
include config.public.mk
endif

RUN = poetry run
BUILD_DIR = build
MODULES_DIR = modules
DOCDIR = docs
SRC = src
SOURCE_SCHEMA_PATH = modules/Clinical/domains/clinical.yaml
GEN_DOC_ARGS = --no-mergeimports

# List of modules (add new modules here)
MODULES = Clinical

.PHONY: all clean setup gen-project gen-examples gendoc git-init-add git-init git-add git-commit git-status help install test modules-gen modules-test

help: status
	@echo ""
	@echo "make setup -- initial setup (run this first)"
	@echo "make site -- makes site locally"
	@echo "make install -- install dependencies"
	@echo "make test -- runs all tests"
	@echo "make modules-gen -- generate schema classes for all modules"
	@echo "make modules-test -- run tests for all modules"
	@echo "make lint -- perform linting"
	@echo "make clean -- clean all build artifacts"
	@echo "make help -- show this help"
	@echo ""

status: check-config
	@echo "Project: HTAN LinkML"
	@echo "Modules: $(MODULES)"

# generate products and add everything to github
setup: check-config git-init install gen-project gen-examples gendoc git-add git-commit

# install any dependencies required for building
install:
	poetry install
.PHONY: install

# Generate schema classes for all modules
modules-gen:
	@for module in $(MODULES); do \
		echo "Generating schema classes for $$module module..."; \
		$(MAKE) -C $(MODULES_DIR)/$$module gen-schema; \
	done

# Run tests for all modules
modules-test:
	@for module in $(MODULES); do \
		echo "Running tests for $$module module..."; \
		$(MAKE) -C $(MODULES_DIR)/$$module test; \
	done

# Clean all build artifacts
clean:
	rm -rf $(BUILD_DIR)
	@for module in $(MODULES); do \
		echo "Cleaning $$module module..."; \
		$(MAKE) -C $(MODULES_DIR)/$$module clean; \
	done

test: modules-test test-examples

# ---
# Project Synchronization
# ---
#
# check we are up to date
check: cruft-check
cruft-check:
	cruft check
cruft-diff:
	cruft diff

update: update-template update-linkml
update-template:
	cruft update

# todo: consider pinning to template
update-linkml:
	poetry add -D linkml@latest

# EXPERIMENTAL
create-data-harmonizer:
	npm init data-harmonizer $(SOURCE_SCHEMA_PATH)

all: site
site: gen-project gendoc
%.yaml: gen-project
deploy: all mkd-gh-deploy

compile-sheets:
	$(RUN) sheets2linkml --gsheet-id $(SHEET_ID) $(SHEET_TABS) > $(SHEET_MODULE_PATH).tmp && mv $(SHEET_MODULE_PATH).tmp $(SHEET_MODULE_PATH)

# In future this will be done by conversion
gen-examples:
	cp src/data/examples/* $(EXAMPLEDIR)

# generates all project files
gen-project: $(PYMODEL)
	$(RUN) gen-project $(LINKML_GENERATORS_CONFIG_YAML) -d src/htan_linkml/schema_classes $(SOURCE_SCHEMA_PATH) && mv src/htan_linkml/schema_classes/*.py src/htan_linkml/schema_classes/

# non-empty arg triggers owl (workaround https://github.com/linkml/linkml/issues/1453)
ifneq ($(strip ${GEN_OWL_ARGS}),)
	mkdir -p ${DEST}/owl || true
	$(RUN) gen-owl ${GEN_OWL_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST}/owl/${SCHEMA_NAME}.owl.ttl
endif
# non-empty arg triggers java
ifneq ($(strip ${GEN_JAVA_ARGS}),)
	$(RUN) gen-java ${GEN_JAVA_ARGS} --output-directory ${DEST}/java/ $(SOURCE_SCHEMA_PATH)
endif
# non-empty arg triggers typescript
ifneq ($(strip ${GEN_TS_ARGS}),)
	mkdir -p ${DEST}/typescript || true
	$(RUN) gen-typescript ${GEN_TS_ARGS} $(SOURCE_SCHEMA_PATH) >${DEST}/typescript/${SCHEMA_NAME}.ts
endif

test-examples: examples/output

examples/output: modules/Clinical/domains/clinical.yaml
	mkdir -p $@
	$(RUN) linkml-run-examples \
		--output-formats json \
		--output-formats yaml \
		--counter-example-input-directory src/data/examples/invalid \
		--input-directory src/data/examples/valid \
		--output-directory $@ \
		--schema $< > $@/README.md

# Test documentation locally
serve: mkd-serve

# Python datamodel
$(PYMODEL):
	mkdir -p $@


$(DOCDIR):
	mkdir -p $@

gendoc: $(DOCDIR)
	mkdir -p $(DOCDIR)
	if [ -d "$(SRC)/docs/files" ]; then \
		cp -rf "$(SRC)/docs/files/"* "$(DOCDIR)/" || true; \
	fi
	$(RUN) gen-doc $(GEN_DOC_ARGS) -d $(DOCDIR) $(SOURCE_SCHEMA_PATH)

testdoc: gendoc serve

MKDOCS = $(RUN) mkdocs
mkd-%:
	$(MKDOCS) $*

git-init-add: git-init git-add git-commit git-status
git-init:
	git init
git-add: .cruft.json
	git add .
git-commit:
	git commit -m 'chore: make setup was run' -a
git-status:
	git status

# only necessary if setting up via cookiecutter
.cruft.json:
	echo "creating a stub for .cruft.json. IMPORTANT: setup via cruft not cookiecutter recommended!" ; \
	touch $@

check-config:
ifndef LINKML_SCHEMA_NAME
	$(error **Project not configured**:\n\n - See '.env.public'\n\n)
else
	$(info Ok)
endif

convert-examples-to-%:
	$(patsubst %, $(RUN) linkml-convert  % -s $(SOURCE_SCHEMA_PATH) -C Person, $(shell ${SHELL} find src/data/examples -name "*.yaml"))

examples/%.yaml: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.json: src/data/examples/%.yaml
	$(RUN) linkml-convert -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@
examples/%.ttl: src/data/examples/%.yaml
	$(RUN) linkml-convert -P EXAMPLE=http://example.org/ -s $(SOURCE_SCHEMA_PATH) -C Person $< -o $@

include project.Makefile
