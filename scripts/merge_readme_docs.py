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
    """Merge README content at the top of the generated doc."""
    if not doc_path.exists():
        print(f"Warning: Doc file not found: {doc_path}")
        return False
    
    if not readme_path.exists():
        print(f"Warning: README not found: {readme_path}")
        # Still return True - we'll just use the doc as-is
        return True
    
    # Read both files
    with open(readme_path, 'r') as f:
        readme_content = f.read()
    
    with open(doc_path, 'r') as f:
        doc_content = f.read()
    
    # Merge: README first, then a separator, then the doc
    merged = f"{readme_content}\n\n---\n\n## Schema Documentation\n\n{doc_content}"
    
    # Write back
    with open(doc_path, 'w') as f:
        f.write(merged)
    
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

