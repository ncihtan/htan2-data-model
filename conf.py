# Configuration file for Sphinx documentation builder
project = 'HTAN Phase 2 Data Model'
copyright = '2024, HTAN Consortium'
author = 'HTAN Consortium'
release = '0.1.0'

extensions = [
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', 'modules/CoreFile']

source_suffix = ['.md', '.rst']
myst_enable_extensions = ['colon_fence']

