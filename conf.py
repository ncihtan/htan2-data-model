# Configuration file for Sphinx documentation builder
project = "HTAN Phase 2 Data Model"
copyright = "2024, HTAN Consortium"
author = "HTAN Consortium"
release = "0.1.0"

extensions = [
    "myst_parser",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    ".venv",
    ".pytest_cache",
    "Thumbs.db",
    ".DS_Store",
    "modules",
    "archive",
    "site",
    "README.md",
    "CONTRIBUTING.md",
    "IDENTIFIER_PATTERNS.md",
    "CLAUDE.md",
    # Old per-level gen-doc subdirectories (replaced by our module pages)
    "docs/multiplexmicroscopy",
    "docs/scrna-seq",
    "docs/spatialomics",
    "docs/wes",
    ".claude",
]

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

source_suffix = [".md", ".rst"]
myst_enable_extensions = ["colon_fence", "deflist", "attrs_block"]
myst_heading_anchors = 3
