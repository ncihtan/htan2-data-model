"""
HTAN Biospecimen Data Model

This module provides data model classes for HTAN biospecimen data
based on the RFC HTAN Phase 2 Biospecimen Model.
"""

__version__ = "0.1.0"
__author__ = "HTAN Data Model Team"

from .datamodel.biospecimen import BiospecimenData

__all__ = ["BiospecimenData"]


