#!/usr/bin/env python3
"""
Merge module READMEs with generated schema documentation.
"""
import os
from pathlib import Path

# Module name mappings
MODULE_MAPPINGS = {
    "clinical": ("Clinical", "modules/Clinical/README.md"),
    "biospecimen": ("Biospecimen", "modules/Biospecimen/README.md"),
    "corefile": ("CoreFile", "modules/CoreFile/README.md"),
    "sequencing": ("Sequencing", "modules/Sequencing/README.md"),
    "wes": ("WES", "modules/WES/README.md"),
    "scrna-seq": ("scRNA-seq", "modules/scRNA-seq/README.md"),
    "imaging": ("Imaging", "modules/Imaging/README.md"),
    "digitalpathology": ("DigitalPathology", "modules/DigitalPathology/README.md"),
    "multiplexmicroscopy": ("MultiplexMicroscopy", "modules/MultiplexMicroscopy/README.md"),
    "spatialomics": ("SpatialOmics", "modules/SpatialOmics/README.md"),
}

def merge_readme_with_doc(doc_path: Path, readme_path: Path):
    """Skip README merging - just use the doc as-is (user wants just tables)."""
    # Don't merge READMEs anymore - user wants just the tables
    return True

def main():
    """Merge all READMEs with their corresponding docs."""
    base_dir = Path(__file__).parent.parent
    os.chdir(base_dir)
    
    docs_dir = base_dir / "docs"
    
    for doc_filename, (module_name, readme_path) in MODULE_MAPPINGS.items():
        doc_path = docs_dir / f"{doc_filename}.md"
        full_readme_path = base_dir / readme_path
        
        print(f"Merging {module_name} README with {doc_filename}.md...")
        merge_readme_with_doc(doc_path, full_readme_path)
    
    print("\n✅ README merge complete!")

if __name__ == "__main__":
    main()

