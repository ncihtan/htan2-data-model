#!/usr/bin/env python3
"""
Generate documentation from all HTAN2 modules using LinkML gen-doc.
This script generates schema documentation similar to LinkML's own docs.
"""
import os
import subprocess
import shutil
from pathlib import Path

# Module schemas to generate docs for
MODULES = {
    "Clinical": "modules/Clinical/domains/clinical.yaml",
    "Biospecimen": "modules/Biospecimen/domains/biospecimen.yaml",
    "CoreFile": "modules/CoreFile/domains/core.yaml",
    "Sequencing": "modules/Sequencing/domains/sequencing.yaml",
    "WES": "modules/WES/domains/wes.yaml",
    "scRNA-seq": "modules/scRNA-seq/domains/scrna_seq.yaml",
    "Imaging": "modules/Imaging/domains/imaging.yaml",
    "DigitalPathology": "modules/DigitalPathology/domains/digital_pathology.yaml",
    "MultiplexMicroscopy": "modules/MultiplexMicroscopy/domains/multiplex_microscopy.yaml",
    "SpatialOmics": "modules/SpatialOmics/domains/spatial.yaml",
}

# Module READMEs to copy
MODULE_READMES = {
    "Clinical": "modules/Clinical/README.md",
    "Biospecimen": "modules/Biospecimen/README.md",
    "CoreFile": "modules/CoreFile/README.md",
    "Sequencing": "modules/Sequencing/README.md",
    "WES": "modules/WES/README.md",
    "scRNA-seq": "modules/scRNA-seq/README.md",
    "Imaging": "modules/Imaging/README.md",
    "DigitalPathology": "modules/DigitalPathology/README.md",
    "MultiplexMicroscopy": "modules/MultiplexMicroscopy/README.md",
    "SpatialOmics": "modules/SpatialOmics/README.md",
}

def run_gen_doc(schema_path: str, output_dir: str):
    """Run LinkML gen-doc on a schema."""
    cmd = ["poetry", "run", "gen-doc", "--no-mergeimports", schema_path, "-d", output_dir]
    print(f"Generating docs for {schema_path}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: gen-doc failed for {schema_path}")
        print(result.stderr)
        return False
    return True

def copy_readme(readme_path: str, output_path: str):
    """Copy module README to docs."""
    if os.path.exists(readme_path):
        shutil.copy2(readme_path, output_path)
        print(f"Copied {readme_path} to {output_path}")
        return True
    return False

def main():
    """Generate all documentation."""
    base_dir = Path(__file__).parent.parent
    os.chdir(base_dir)
    
    # Clean generated docs directory
    generated_dir = base_dir / "docs" / "generated"
    if generated_dir.exists():
        shutil.rmtree(generated_dir)
    generated_dir.mkdir(parents=True, exist_ok=True)
    
    # Generate docs for each module
    for module_name, schema_path in MODULES.items():
        full_schema_path = base_dir / schema_path
        if not full_schema_path.exists():
            print(f"Warning: Schema not found: {full_schema_path}")
            continue
        
        module_output_dir = generated_dir / module_name.lower()
        module_output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate schema docs
        run_gen_doc(str(full_schema_path), str(module_output_dir))
    
    # Copy module READMEs
    readmes_dir = base_dir / "docs" / "modules-readmes"
    if readmes_dir.exists():
        shutil.rmtree(readmes_dir)
    readmes_dir.mkdir(parents=True, exist_ok=True)
    
    for module_name, readme_path in MODULE_READMES.items():
        full_readme_path = base_dir / readme_path
        output_readme = readmes_dir / f"{module_name.lower()}.md"
        copy_readme(str(full_readme_path), str(output_readme))
    
    print("\n✅ Documentation generation complete!")
    print(f"Generated docs: {generated_dir}")
    print(f"Module READMEs: {readmes_dir}")

if __name__ == "__main__":
    main()

