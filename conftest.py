"""Repo-wide pytest configuration."""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent


def pytest_configure(config: pytest.Config) -> None:
    # The UBERON enum is generated from Uberon rather than committed (issue #198);
    # build it before any test loads the Clinical / Biospecimen schemas.
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/build_uberon_enum.py"), "--if-missing"],
        check=True,
    )
