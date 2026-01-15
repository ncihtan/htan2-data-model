#!/bin/bash
# Simple script to generate all docs

set -e

cd "$(dirname "$0")/.."

# Clean and regenerate
rm -rf docs/clinical docs/biospecimen docs/corefile docs/sequencing docs/wes \
       docs/scrna-seq docs/imaging docs/digitalpathology docs/multiplexmicroscopy \
       docs/spatialomics

poetry run gen-doc --no-mergeimports modules/Clinical/domains/clinical.yaml -d docs/clinical
poetry run gen-doc --no-mergeimports modules/Biospecimen/domains/biospecimen.yaml -d docs/biospecimen
poetry run gen-doc --no-mergeimports modules/CoreFile/domains/core.yaml -d docs/corefile
poetry run gen-doc --no-mergeimports modules/Sequencing/domains/sequencing.yaml -d docs/sequencing
poetry run gen-doc --no-mergeimports modules/WES/domains/wes.yaml -d docs/wes || true
poetry run gen-doc --no-mergeimports modules/scRNA-seq/domains/scrna_seq.yaml -d docs/scrna-seq || true
poetry run gen-doc --no-mergeimports modules/Imaging/domains/imaging.yaml -d docs/imaging
poetry run gen-doc --no-mergeimports modules/DigitalPathology/domains/digital_pathology.yaml -d docs/digitalpathology
poetry run gen-doc --no-mergeimports modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml -d docs/multiplexmicroscopy || true
poetry run gen-doc --no-mergeimports modules/SpatialOmics/domains/spatial.yaml -d docs/spatialomics || true

echo "✅ Docs generated"

