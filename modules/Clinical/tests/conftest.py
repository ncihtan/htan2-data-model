"""Pytest configuration for Clinical module tests."""

import os
import sys
from pathlib import Path

# Add the Clinical module src directory to Python path
test_dir = Path(__file__).parent
module_dir = test_dir.parent
src_dir = module_dir / "src"
project_root = module_dir.parent.parent

# Add both the module src directory and project root to path
sys.path.insert(0, str(src_dir))
sys.path.insert(0, str(project_root))
