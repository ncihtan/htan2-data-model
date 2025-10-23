#!/usr/bin/env python3
"""
Convert UBERON TSV files to YAML format for the HTAN data model.

This script was used to generate the UBERON tissue/organ YAML files
from TSV data sources during the initial setup of the Biospecimen module.
The generated YAML files are used for anatomical site validation in
the biospecimen data model.
"""

import csv
import yaml


def convert_tsv_to_yaml(tsv_file, yaml_file):
    # Read the TSV file
    with open(tsv_file, "r") as f:
        reader = csv.DictReader(f, delimiter="\t")
        permissible_values = {}
        for row in reader:
            code = row["Permissible Value"]
            label = row["Label"]
            permissible_values[code] = {"description": label}

    # Create the YAML structure
    yaml_data = {
        "id": "https://w3id.org/htan/uberon_tissues",
        "name": "uberon_tissues",
        "description": "UBERON codes for tissues and organs",
        "title": "UBERON Tissue and Organ Codes",
        "version": "1.0.0",
        "enums": {
            "tissue_or_organ_of_origin_uberon_enum": {
                "name": "tissue_or_organ_of_origin_uberon_enum",
                "description": "UBERON codes for tissues and organs of origin",
                "permissible_values": permissible_values,
            }
        },
    }

    # Write the YAML file
    with open(yaml_file, "w") as f:
        yaml.dump(yaml_data, f, sort_keys=False, width=float("inf"))


if __name__ == "__main__":
    convert_tsv_to_yaml(
        "uberon_organ-tissue.tsv", "modules/Clinical/domains/uberon_tissues.yaml"
    )
