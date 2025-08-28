#!/usr/bin/env python3
"""Generate test data files for HTAN2 schema validation.

This script generates sample data files that conform to the HTAN2 schemas
for testing validation in Synapse.
"""

import argparse
import json
import random
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any


def generate_clinical_test_data() -> Dict[str, Any]:
    """Generate sample clinical data."""
    return {
        "htan_data_file_id": "HTAN_CLINICAL_001",
        "htan_parent_id": "HTAN_PARTICIPANT_001",
        "filename": "clinical_data_001.json",
        "file_format": "JSON",
        "clinical_data": {
            "demographics": {
                "sex": "Female",
                "race": "White",
                "ethnic_group": "Not Hispanic or Latino",
                "age_in_days_at_diagnosis": 18250,
                "gender_identity": "Woman"
            },
            "diagnosis": {
                "primary_diagnosis_nci_thesaurus_id": "C0007114",
                "tissue_or_organ_of_origin": "Lung",
                "tissue_or_organ_of_origin_uberon_code": "UBERON:0002048",
                "metastasis_at_diagnosis": "No",
                "method_of_diagnosis": "Biopsy",
                "tumor_stage": "Stage II",
                "tumor_grade": "Grade 2",
                "tumor_classification_category": "Primary"
            },
            "vital_status": {
                "vital_status": "Alive",
                "age_in_days_at_death": None,
                "cause_of_death": None,
                "cause_of_death_source": None
            }
        }
    }


def generate_biospecimen_test_data() -> Dict[str, Any]:
    """Generate sample biospecimen data."""
    return {
        "htan_data_file_id": "HTAN_BIOSPECIMEN_001",
        "htan_parent_id": "HTAN_PARTICIPANT_001",
        "filename": "biospecimen_data_001.json",
        "file_format": "JSON",
        "biospecimen_id": "BIO_001",
        "clinical_biospecimen_type": "Tumor",
        "tissue_or_organ_of_origin": "Lung",
        "tissue_or_organ_of_origin_uberon_code": "UBERON:0002048",
        "collection_date": "2023-01-15",
        "preservation_method": "FFPE",
        "storage_method": "Paraffin block"
    }


def generate_participant_test_data() -> Dict[str, Any]:
    """Generate sample participant data."""
    return {
        "htan_data_file_id": "HTAN_PARTICIPANT_001",
        "htan_parent_id": None,
        "filename": "participant_data_001.json",
        "file_format": "JSON",
        "participant_id": "PART_001",
        "age_at_enrollment": 50,
        "sex": "Female",
        "race": "White",
        "ethnic_group": "Not Hispanic or Latino"
    }


def generate_sequencing_test_data() -> Dict[str, Any]:
    """Generate sample sequencing data."""
    return {
        "htan_data_file_id": "HTAN_SEQUENCING_001",
        "htan_parent_id": "HTAN_BIOSPECIMEN_001",
        "filename": "sequencing_data_001.json",
        "file_format": "JSON",
        "sequencing_id": "SEQ_001",
        "sequencing_platform": "Illumina",
        "sequencing_instrument": "NextSeq 500",
        "read_length": 150,
        "sequencing_depth": 30,
        "library_preparation_method": "TruSeq DNA PCR-Free"
    }


def generate_wes_test_data() -> Dict[str, Any]:
    """Generate sample WES data."""
    return {
        "htan_data_file_id": "HTAN_WES_001",
        "htan_parent_id": "HTAN_BIOSPECIMEN_001",
        "filename": "wes_data_001.json",
        "file_format": "JSON",
        "wes_id": "WES_001",
        "sequencing_platform": "Illumina",
        "sequencing_instrument": "NovaSeq 6000",
        "read_length": 150,
        "sequencing_depth": 100,
        "library_preparation_method": "TruSeq DNA PCR-Free",
        "capture_kit": "SureSelect Human All Exon V6",
        "target_coverage": 95.5
    }


def generate_scrna_seq_test_data() -> Dict[str, Any]:
    """Generate sample scRNA-seq data."""
    return {
        "htan_data_file_id": "HTAN_SCRNASEQ_001",
        "htan_parent_id": "HTAN_BIOSPECIMEN_001",
        "filename": "scrna_seq_data_001.json",
        "file_format": "JSON",
        "scrna_seq_id": "SCRNASEQ_001",
        "sequencing_platform": "10x Genomics",
        "sequencing_instrument": "NovaSeq 6000",
        "read_length": 150,
        "library_preparation_method": "10x Single Cell 3' v3",
        "cell_count": 5000,
        "gene_count": 20000,
        "quality_metrics": {
            "median_genes_per_cell": 1500,
            "median_umis_per_cell": 5000,
            "mitochondrial_percentage": 5.2
        }
    }


def generate_test_data_files(output_dir: str = "test_data"):
    """Generate test data files for all schemas."""
    
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Define test data generators
    generators = {
        "clinical": generate_clinical_test_data,
        "biospecimen": generate_biospecimen_test_data,
        "participant": generate_participant_test_data,
        "sequencing": generate_sequencing_test_data,
        "wes": generate_wes_test_data,
        "scrna_seq": generate_scrna_seq_test_data
    }
    
    # Generate test data for each schema
    for schema_name, generator in generators.items():
        test_data = generator()
        
        # Create multiple test files with variations
        for i in range(1, 4):  # Create 3 test files per schema
            test_data["htan_data_file_id"] = f"HTAN_{schema_name.upper()}_{i:03d}"
            test_data["filename"] = f"{schema_name}_data_{i:03d}.json"
            
            # Add some random variations
            if "age" in str(test_data):
                test_data = add_age_variations(test_data)
            
            output_file = output_path / f"{schema_name}_test_data_{i:03d}.json"
            
            with open(output_file, 'w') as f:
                json.dump(test_data, f, indent=2)
            
            print(f"✅ Generated {output_file}")
    
    print(f"\n🎉 Generated test data files in {output_path}")
    print(f"Files created:")
    for schema_name in generators.keys():
        for i in range(1, 4):
            print(f"  - {schema_name}_test_data_{i:03d}.json")


def add_age_variations(data: Dict[str, Any]) -> Dict[str, Any]:
    """Add random age variations to test data."""
    # Deep copy to avoid modifying original
    import copy
    data = copy.deepcopy(data)
    
    # Add random age variations
    base_age = random.randint(30, 80)
    days_at_diagnosis = base_age * 365 + random.randint(0, 365)
    
    # Update age fields if they exist
    if "clinical_data" in data and "demographics" in data["clinical_data"]:
        data["clinical_data"]["demographics"]["age_in_days_at_diagnosis"] = days_at_diagnosis
    
    if "age_at_enrollment" in data:
        data["age_at_enrollment"] = base_age
    
    return data


def main():
    parser = argparse.ArgumentParser(
        description="Generate test data files for HTAN2 schema validation"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="test_data",
        help="Output directory for test data files (default: test_data)"
    )
    
    args = parser.parse_args()
    
    generate_test_data_files(args.output_dir)


if __name__ == "__main__":
    main()
