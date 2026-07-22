# Auto generated from scatac_seq.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-22T16:09:33
# Schema: scATAC-seq
#
# id: https://w3id.org/htan/scatac_seq
# description: HTAN scATAC-seq Data Model - Single-cell ATAC sequencing data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = HTAN


# Types

# Class references
class CoreFileAttributesHTANDATAFILEID(extended_str):
    pass


class BaseSequencingAttributesHTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class BaseSequencingLevel1AttributesHTANDATAFILEID(BaseSequencingAttributesHTANDATAFILEID):
    pass


class BaseSequencingLevel2AttributesHTANDATAFILEID(BaseSequencingLevel1AttributesHTANDATAFILEID):
    pass


class ScATACLevel2HTANDATAFILEID(BaseSequencingLevel2AttributesHTANDATAFILEID):
    pass


class BaseSequencingLevel3AttributesHTANDATAFILEID(BaseSequencingLevel2AttributesHTANDATAFILEID):
    pass


class ScATACLevel3and4HTANDATAFILEID(BaseSequencingLevel3AttributesHTANDATAFILEID):
    pass


class SingleCellLevel1AttributesHTANDATAFILEID(BaseSequencingLevel1AttributesHTANDATAFILEID):
    pass


class ScATACLevel1HTANDATAFILEID(SingleCellLevel1AttributesHTANDATAFILEID):
    pass


@dataclass(repr=False)
class ScATACseqData(YAMLRoot):
    """
    Root class for scATAC-seq data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScATACseqData"]
    class_class_curie: ClassVar[str] = "htan:ScATACseqData"
    class_name: ClassVar[str] = "scATACseqData"
    class_model_uri: ClassVar[URIRef] = HTAN.ScATACseqData

    level1_data: Optional[Union[dict, "ScATACLevel1"]] = None
    level2_data: Optional[Union[dict, "ScATACLevel2"]] = None
    level3_4_data: Optional[Union[dict, "ScATACLevel3and4"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.level1_data is not None and not isinstance(self.level1_data, ScATACLevel1):
            self.level1_data = ScATACLevel1(**as_dict(self.level1_data))

        if self.level2_data is not None and not isinstance(self.level2_data, ScATACLevel2):
            self.level2_data = ScATACLevel2(**as_dict(self.level2_data))

        if self.level3_4_data is not None and not isinstance(self.level3_4_data, ScATACLevel3and4):
            self.level3_4_data = ScATACLevel3and4(**as_dict(self.level3_4_data))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnnDataComplianceMixin(YAMLRoot):
    """
    AnnData 0.1 / CellxGene compliance attributes for single-cell h5ad outputs, shared across single-cell modalities
    that emit h5ad matrices
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["AnnDataComplianceMixin"]
    class_class_curie: ClassVar[str] = "htan:AnnDataComplianceMixin"
    class_name: ClassVar[str] = "AnnDataComplianceMixin"
    class_model_uri: ClassVar[URIRef] = HTAN.AnnDataComplianceMixin

    ANNDATA_SCHEMA_VERSION: str = None
    ANNDATA_STRUCTURE_VALIDATED: Union[bool, Bool] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.ANNDATA_SCHEMA_VERSION):
            self.MissingRequiredField("ANNDATA_SCHEMA_VERSION")
        if not isinstance(self.ANNDATA_SCHEMA_VERSION, str):
            self.ANNDATA_SCHEMA_VERSION = str(self.ANNDATA_SCHEMA_VERSION)

        if self._is_empty(self.ANNDATA_STRUCTURE_VALIDATED):
            self.MissingRequiredField("ANNDATA_STRUCTURE_VALIDATED")
        if not isinstance(self.ANNDATA_STRUCTURE_VALIDATED, Bool):
            self.ANNDATA_STRUCTURE_VALIDATED = Bool(self.ANNDATA_STRUCTURE_VALIDATED)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CoreFileAttributes(YAMLRoot):
    """
    Universal attributes that apply to all file-based data in HTAN
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["CoreFileAttributes"]
    class_class_curie: ClassVar[str] = "htan:CoreFileAttributes"
    class_name: ClassVar[str] = "CoreFileAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.CoreFileAttributes

    HTAN_DATA_FILE_ID: Union[str, CoreFileAttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: Union[str, List[str]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, CoreFileAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = CoreFileAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.HTAN_PARENT_ID):
            self.MissingRequiredField("HTAN_PARENT_ID")
        if not isinstance(self.HTAN_PARENT_ID, list):
            self.HTAN_PARENT_ID = [self.HTAN_PARENT_ID] if self.HTAN_PARENT_ID is not None else []
        self.HTAN_PARENT_ID = [v if isinstance(v, str) else str(v) for v in self.HTAN_PARENT_ID]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseSequencingAttributes(CoreFileAttributes):
    """
    Minimal base attributes shared across all sequencing types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BaseSequencingAttributes"]
    class_class_curie: ClassVar[str] = "htan:BaseSequencingAttributes"
    class_name: ClassVar[str] = "BaseSequencingAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BaseSequencingAttributes

    HTAN_DATA_FILE_ID: Union[str, BaseSequencingAttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    CHECKSUM: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BaseSequencingAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BaseSequencingAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self.CHECKSUM is not None and not isinstance(self.CHECKSUM, str):
            self.CHECKSUM = str(self.CHECKSUM)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseSequencingLevel1Attributes(BaseSequencingAttributes):
    """
    Level 1 attributes - sequencing run and library (raw data)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BaseSequencingLevel1Attributes"]
    class_class_curie: ClassVar[str] = "htan:BaseSequencingLevel1Attributes"
    class_name: ClassVar[str] = "BaseSequencingLevel1Attributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BaseSequencingLevel1Attributes

    HTAN_DATA_FILE_ID: Union[str, BaseSequencingLevel1AttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    SEQUENCING_BATCH_ID: Optional[str] = None
    LIBRARY_PREPARATION_DAYS_FROM_INDEX: Optional[int] = None
    TECHNICAL_REPLICATE_GROUP: Optional[str] = None
    PROTOCOL_LINK: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BaseSequencingLevel1AttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BaseSequencingLevel1AttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.LIBRARY_LAYOUT):
            self.MissingRequiredField("LIBRARY_LAYOUT")
        if not isinstance(self.LIBRARY_LAYOUT, LibraryLayoutEnum):
            self.LIBRARY_LAYOUT = LibraryLayoutEnum(self.LIBRARY_LAYOUT)

        if self._is_empty(self.SEQUENCING_PLATFORM):
            self.MissingRequiredField("SEQUENCING_PLATFORM")
        if not isinstance(self.SEQUENCING_PLATFORM, SequencingPlatformEnum):
            self.SEQUENCING_PLATFORM = SequencingPlatformEnum(self.SEQUENCING_PLATFORM)

        if self.SEQUENCING_BATCH_ID is not None and not isinstance(self.SEQUENCING_BATCH_ID, str):
            self.SEQUENCING_BATCH_ID = str(self.SEQUENCING_BATCH_ID)

        if self.LIBRARY_PREPARATION_DAYS_FROM_INDEX is not None and not isinstance(self.LIBRARY_PREPARATION_DAYS_FROM_INDEX, int):
            self.LIBRARY_PREPARATION_DAYS_FROM_INDEX = int(self.LIBRARY_PREPARATION_DAYS_FROM_INDEX)

        if self.TECHNICAL_REPLICATE_GROUP is not None and not isinstance(self.TECHNICAL_REPLICATE_GROUP, str):
            self.TECHNICAL_REPLICATE_GROUP = str(self.TECHNICAL_REPLICATE_GROUP)

        if self.PROTOCOL_LINK is not None and not isinstance(self.PROTOCOL_LINK, str):
            self.PROTOCOL_LINK = str(self.PROTOCOL_LINK)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseSequencingLevel2Attributes(BaseSequencingLevel1Attributes):
    """
    Level 2 attributes - alignment and alignment workflow
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BaseSequencingLevel2Attributes"]
    class_class_curie: ClassVar[str] = "htan:BaseSequencingLevel2Attributes"
    class_name: ClassVar[str] = "BaseSequencingLevel2Attributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BaseSequencingLevel2Attributes

    HTAN_DATA_FILE_ID: Union[str, BaseSequencingLevel2AttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    GENOMIC_REFERENCE: Union[str, "GenomicReferenceEnum"] = None
    GENOMIC_REFERENCE_URL: str = None
    GENOME_ANNOTATION_URL: str = None
    WORKFLOW_VERSION: str = None
    WORKFLOW_LINK: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BaseSequencingLevel2AttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BaseSequencingLevel2AttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.GENOMIC_REFERENCE):
            self.MissingRequiredField("GENOMIC_REFERENCE")
        if not isinstance(self.GENOMIC_REFERENCE, GenomicReferenceEnum):
            self.GENOMIC_REFERENCE = GenomicReferenceEnum(self.GENOMIC_REFERENCE)

        if self._is_empty(self.GENOMIC_REFERENCE_URL):
            self.MissingRequiredField("GENOMIC_REFERENCE_URL")
        if not isinstance(self.GENOMIC_REFERENCE_URL, str):
            self.GENOMIC_REFERENCE_URL = str(self.GENOMIC_REFERENCE_URL)

        if self._is_empty(self.GENOME_ANNOTATION_URL):
            self.MissingRequiredField("GENOME_ANNOTATION_URL")
        if not isinstance(self.GENOME_ANNOTATION_URL, str):
            self.GENOME_ANNOTATION_URL = str(self.GENOME_ANNOTATION_URL)

        if self._is_empty(self.WORKFLOW_VERSION):
            self.MissingRequiredField("WORKFLOW_VERSION")
        if not isinstance(self.WORKFLOW_VERSION, str):
            self.WORKFLOW_VERSION = str(self.WORKFLOW_VERSION)

        if self._is_empty(self.WORKFLOW_LINK):
            self.MissingRequiredField("WORKFLOW_LINK")
        if not isinstance(self.WORKFLOW_LINK, str):
            self.WORKFLOW_LINK = str(self.WORKFLOW_LINK)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScATACLevel2(BaseSequencingLevel2Attributes):
    """
    scATAC-seq Level 2 data - Aligned data and alignment QC metrics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScATACLevel2"]
    class_class_curie: ClassVar[str] = "htan:ScATACLevel2"
    class_name: ClassVar[str] = "scATACLevel2"
    class_model_uri: ClassVar[URIRef] = HTAN.ScATACLevel2

    HTAN_DATA_FILE_ID: Union[str, ScATACLevel2HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    GENOMIC_REFERENCE: Union[str, "GenomicReferenceEnum"] = None
    GENOMIC_REFERENCE_URL: str = None
    GENOME_ANNOTATION_URL: str = None
    WORKFLOW_VERSION: str = None
    WORKFLOW_LINK: str = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    TOTAL_UNIQUELY_MAPPED: int = None
    TOTAL_UNMAPPED_READS: int = None
    MEDIAN_FRAGMENTS_PER_CELL: float = None
    MEDIAN_GENES_PER_CELL: float = None
    NUMBER_OF_CELLS: int = None
    MEDIAN_PASSING_READS_PERCENTAGE: float = None
    DUPLICATE_READ_PAIRS: int = None
    CHIMERIC_READ_PAIRS: int = None
    UNMAPPED_READ_PAIRS: int = None
    LOW_MAP_Q: int = None
    MITOCHONDRIAL_READ_PAIRS: int = None
    PASSED_FILTERS: int = None
    AVERAGE_BASE_QUALITY: Optional[float] = None
    AVERAGE_INSERT_SIZE: Optional[float] = None
    AVERAGE_READ_LENGTH: Optional[float] = None
    MEAN_COVERAGE: Optional[float] = None
    PAIRS_ON_DIFF_CHR: Optional[int] = None
    PROPORTION_READS_MAPPED: Optional[float] = None
    PROPORTION_READS_DUPLICATED: Optional[float] = None
    SHORT_READS: Optional[int] = None
    PROPORTION_COVERAGE_10X: Optional[float] = None
    PROPORTION_COVERAGE_30X: Optional[float] = None
    PROPORTION_TARGETS_NO_MATCH: Optional[float] = None
    PROPORTION_BASE_MISMATCH: Optional[float] = None
    PROPORTION_MITOCHONDRIAL_READS: Optional[float] = None
    CONTAMINATION: Optional[float] = None
    CONTAMINATION_ERROR: Optional[float] = None
    THRESHOLD_FOR_MINIMUM_PASSING_READS: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ScATACLevel2HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ScATACLevel2HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.TOTAL_UNIQUELY_MAPPED):
            self.MissingRequiredField("TOTAL_UNIQUELY_MAPPED")
        if not isinstance(self.TOTAL_UNIQUELY_MAPPED, int):
            self.TOTAL_UNIQUELY_MAPPED = int(self.TOTAL_UNIQUELY_MAPPED)

        if self._is_empty(self.TOTAL_UNMAPPED_READS):
            self.MissingRequiredField("TOTAL_UNMAPPED_READS")
        if not isinstance(self.TOTAL_UNMAPPED_READS, int):
            self.TOTAL_UNMAPPED_READS = int(self.TOTAL_UNMAPPED_READS)

        if self._is_empty(self.MEDIAN_FRAGMENTS_PER_CELL):
            self.MissingRequiredField("MEDIAN_FRAGMENTS_PER_CELL")
        if not isinstance(self.MEDIAN_FRAGMENTS_PER_CELL, float):
            self.MEDIAN_FRAGMENTS_PER_CELL = float(self.MEDIAN_FRAGMENTS_PER_CELL)

        if self._is_empty(self.MEDIAN_GENES_PER_CELL):
            self.MissingRequiredField("MEDIAN_GENES_PER_CELL")
        if not isinstance(self.MEDIAN_GENES_PER_CELL, float):
            self.MEDIAN_GENES_PER_CELL = float(self.MEDIAN_GENES_PER_CELL)

        if self._is_empty(self.NUMBER_OF_CELLS):
            self.MissingRequiredField("NUMBER_OF_CELLS")
        if not isinstance(self.NUMBER_OF_CELLS, int):
            self.NUMBER_OF_CELLS = int(self.NUMBER_OF_CELLS)

        if self._is_empty(self.MEDIAN_PASSING_READS_PERCENTAGE):
            self.MissingRequiredField("MEDIAN_PASSING_READS_PERCENTAGE")
        if not isinstance(self.MEDIAN_PASSING_READS_PERCENTAGE, float):
            self.MEDIAN_PASSING_READS_PERCENTAGE = float(self.MEDIAN_PASSING_READS_PERCENTAGE)

        if self._is_empty(self.DUPLICATE_READ_PAIRS):
            self.MissingRequiredField("DUPLICATE_READ_PAIRS")
        if not isinstance(self.DUPLICATE_READ_PAIRS, int):
            self.DUPLICATE_READ_PAIRS = int(self.DUPLICATE_READ_PAIRS)

        if self._is_empty(self.CHIMERIC_READ_PAIRS):
            self.MissingRequiredField("CHIMERIC_READ_PAIRS")
        if not isinstance(self.CHIMERIC_READ_PAIRS, int):
            self.CHIMERIC_READ_PAIRS = int(self.CHIMERIC_READ_PAIRS)

        if self._is_empty(self.UNMAPPED_READ_PAIRS):
            self.MissingRequiredField("UNMAPPED_READ_PAIRS")
        if not isinstance(self.UNMAPPED_READ_PAIRS, int):
            self.UNMAPPED_READ_PAIRS = int(self.UNMAPPED_READ_PAIRS)

        if self._is_empty(self.LOW_MAP_Q):
            self.MissingRequiredField("LOW_MAP_Q")
        if not isinstance(self.LOW_MAP_Q, int):
            self.LOW_MAP_Q = int(self.LOW_MAP_Q)

        if self._is_empty(self.MITOCHONDRIAL_READ_PAIRS):
            self.MissingRequiredField("MITOCHONDRIAL_READ_PAIRS")
        if not isinstance(self.MITOCHONDRIAL_READ_PAIRS, int):
            self.MITOCHONDRIAL_READ_PAIRS = int(self.MITOCHONDRIAL_READ_PAIRS)

        if self._is_empty(self.PASSED_FILTERS):
            self.MissingRequiredField("PASSED_FILTERS")
        if not isinstance(self.PASSED_FILTERS, int):
            self.PASSED_FILTERS = int(self.PASSED_FILTERS)

        if self.AVERAGE_BASE_QUALITY is not None and not isinstance(self.AVERAGE_BASE_QUALITY, float):
            self.AVERAGE_BASE_QUALITY = float(self.AVERAGE_BASE_QUALITY)

        if self.AVERAGE_INSERT_SIZE is not None and not isinstance(self.AVERAGE_INSERT_SIZE, float):
            self.AVERAGE_INSERT_SIZE = float(self.AVERAGE_INSERT_SIZE)

        if self.AVERAGE_READ_LENGTH is not None and not isinstance(self.AVERAGE_READ_LENGTH, float):
            self.AVERAGE_READ_LENGTH = float(self.AVERAGE_READ_LENGTH)

        if self.MEAN_COVERAGE is not None and not isinstance(self.MEAN_COVERAGE, float):
            self.MEAN_COVERAGE = float(self.MEAN_COVERAGE)

        if self.PAIRS_ON_DIFF_CHR is not None and not isinstance(self.PAIRS_ON_DIFF_CHR, int):
            self.PAIRS_ON_DIFF_CHR = int(self.PAIRS_ON_DIFF_CHR)

        if self.PROPORTION_READS_MAPPED is not None and not isinstance(self.PROPORTION_READS_MAPPED, float):
            self.PROPORTION_READS_MAPPED = float(self.PROPORTION_READS_MAPPED)

        if self.PROPORTION_READS_DUPLICATED is not None and not isinstance(self.PROPORTION_READS_DUPLICATED, float):
            self.PROPORTION_READS_DUPLICATED = float(self.PROPORTION_READS_DUPLICATED)

        if self.SHORT_READS is not None and not isinstance(self.SHORT_READS, int):
            self.SHORT_READS = int(self.SHORT_READS)

        if self.PROPORTION_COVERAGE_10X is not None and not isinstance(self.PROPORTION_COVERAGE_10X, float):
            self.PROPORTION_COVERAGE_10X = float(self.PROPORTION_COVERAGE_10X)

        if self.PROPORTION_COVERAGE_30X is not None and not isinstance(self.PROPORTION_COVERAGE_30X, float):
            self.PROPORTION_COVERAGE_30X = float(self.PROPORTION_COVERAGE_30X)

        if self.PROPORTION_TARGETS_NO_MATCH is not None and not isinstance(self.PROPORTION_TARGETS_NO_MATCH, float):
            self.PROPORTION_TARGETS_NO_MATCH = float(self.PROPORTION_TARGETS_NO_MATCH)

        if self.PROPORTION_BASE_MISMATCH is not None and not isinstance(self.PROPORTION_BASE_MISMATCH, float):
            self.PROPORTION_BASE_MISMATCH = float(self.PROPORTION_BASE_MISMATCH)

        if self.PROPORTION_MITOCHONDRIAL_READS is not None and not isinstance(self.PROPORTION_MITOCHONDRIAL_READS, float):
            self.PROPORTION_MITOCHONDRIAL_READS = float(self.PROPORTION_MITOCHONDRIAL_READS)

        if self.CONTAMINATION is not None and not isinstance(self.CONTAMINATION, float):
            self.CONTAMINATION = float(self.CONTAMINATION)

        if self.CONTAMINATION_ERROR is not None and not isinstance(self.CONTAMINATION_ERROR, float):
            self.CONTAMINATION_ERROR = float(self.CONTAMINATION_ERROR)

        if self.THRESHOLD_FOR_MINIMUM_PASSING_READS is not None and not isinstance(self.THRESHOLD_FOR_MINIMUM_PASSING_READS, int):
            self.THRESHOLD_FOR_MINIMUM_PASSING_READS = int(self.THRESHOLD_FOR_MINIMUM_PASSING_READS)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseSequencingLevel3Attributes(BaseSequencingLevel2Attributes):
    """
    Level 3+ attributes - inherits alignment and workflow; used for processed/analysis levels
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BaseSequencingLevel3Attributes"]
    class_class_curie: ClassVar[str] = "htan:BaseSequencingLevel3Attributes"
    class_name: ClassVar[str] = "BaseSequencingLevel3Attributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BaseSequencingLevel3Attributes

    HTAN_DATA_FILE_ID: Union[str, BaseSequencingLevel3AttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    GENOMIC_REFERENCE: Union[str, "GenomicReferenceEnum"] = None
    GENOMIC_REFERENCE_URL: str = None
    GENOME_ANNOTATION_URL: str = None
    WORKFLOW_VERSION: str = None
    WORKFLOW_LINK: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BaseSequencingLevel3AttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BaseSequencingLevel3AttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScATACLevel3and4(BaseSequencingLevel3Attributes):
    """
    scATAC-seq Level 3 and 4 - Peak-by-cell matrices, fragment files, and chromatin accessibility metrics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScATACLevel3and4"]
    class_class_curie: ClassVar[str] = "htan:ScATACLevel3and4"
    class_name: ClassVar[str] = "scATACLevel3and4"
    class_model_uri: ClassVar[URIRef] = HTAN.ScATACLevel3and4

    HTAN_DATA_FILE_ID: Union[str, ScATACLevel3and4HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    GENOMIC_REFERENCE: Union[str, "GenomicReferenceEnum"] = None
    GENOMIC_REFERENCE_URL: str = None
    GENOME_ANNOTATION_URL: str = None
    WORKFLOW_VERSION: str = None
    WORKFLOW_LINK: str = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    N_COUNT_PEAKS: int = None
    N_FEATURE_PEAKS: int = None
    PERCENTAGE_READS_IN_PEAKS: float = None
    PEAKS_CALLING_SOFTWARE: str = None
    MEDIAN_FRACTION_OF_READS_IN_PEAKS: float = None
    ATAC_GENE_ACTIVITY_WORKFLOW_TYPE: Union[str, "ATACGeneActivityWorkflowTypeEnum"] = None
    ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION: str = None
    CELL_TOTAL: int = None
    ANNDATA_SCHEMA_VERSION: str = None
    ANNDATA_STRUCTURE_VALIDATED: Union[bool, Bool] = None
    TSS_FRAGMENTS: Optional[int] = None
    TSS_ENRICHMENT: Optional[float] = None
    TSS_PERCENTILE: Optional[float] = None
    DNASE_SENSITIVE_REGION_FRAGMENTS: Optional[int] = None
    ENHANCER_REGION_FRAGMENTS: Optional[int] = None
    PROMOTER_REGION_FRAGMENTS: Optional[int] = None
    ON_TARGET_FRAGMENTS: Optional[int] = None
    BLACKLIST_REGION_FRAGMENTS: Optional[int] = None
    BLACKLIST_RATIO: Optional[float] = None
    PEAK_REGION_FRAGMENTS: Optional[int] = None
    PEAK_REGION_CUTSITES: Optional[int] = None
    NUCLEOSOME_SIGNAL: Optional[float] = None
    NUCLEOSOME_PERCENTILE: Optional[float] = None
    SEURAT_CLUSTERS: Optional[Union[str, List[str]]] = empty_list()
    N_COUNT_RNA: Optional[int] = None
    N_FEATURE_RNA: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ScATACLevel3and4HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ScATACLevel3and4HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.N_COUNT_PEAKS):
            self.MissingRequiredField("N_COUNT_PEAKS")
        if not isinstance(self.N_COUNT_PEAKS, int):
            self.N_COUNT_PEAKS = int(self.N_COUNT_PEAKS)

        if self._is_empty(self.N_FEATURE_PEAKS):
            self.MissingRequiredField("N_FEATURE_PEAKS")
        if not isinstance(self.N_FEATURE_PEAKS, int):
            self.N_FEATURE_PEAKS = int(self.N_FEATURE_PEAKS)

        if self._is_empty(self.PERCENTAGE_READS_IN_PEAKS):
            self.MissingRequiredField("PERCENTAGE_READS_IN_PEAKS")
        if not isinstance(self.PERCENTAGE_READS_IN_PEAKS, float):
            self.PERCENTAGE_READS_IN_PEAKS = float(self.PERCENTAGE_READS_IN_PEAKS)

        if self._is_empty(self.PEAKS_CALLING_SOFTWARE):
            self.MissingRequiredField("PEAKS_CALLING_SOFTWARE")
        if not isinstance(self.PEAKS_CALLING_SOFTWARE, str):
            self.PEAKS_CALLING_SOFTWARE = str(self.PEAKS_CALLING_SOFTWARE)

        if self._is_empty(self.MEDIAN_FRACTION_OF_READS_IN_PEAKS):
            self.MissingRequiredField("MEDIAN_FRACTION_OF_READS_IN_PEAKS")
        if not isinstance(self.MEDIAN_FRACTION_OF_READS_IN_PEAKS, float):
            self.MEDIAN_FRACTION_OF_READS_IN_PEAKS = float(self.MEDIAN_FRACTION_OF_READS_IN_PEAKS)

        if self._is_empty(self.ATAC_GENE_ACTIVITY_WORKFLOW_TYPE):
            self.MissingRequiredField("ATAC_GENE_ACTIVITY_WORKFLOW_TYPE")
        if not isinstance(self.ATAC_GENE_ACTIVITY_WORKFLOW_TYPE, ATACGeneActivityWorkflowTypeEnum):
            self.ATAC_GENE_ACTIVITY_WORKFLOW_TYPE = ATACGeneActivityWorkflowTypeEnum(self.ATAC_GENE_ACTIVITY_WORKFLOW_TYPE)

        if self._is_empty(self.ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION):
            self.MissingRequiredField("ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION")
        if not isinstance(self.ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION, str):
            self.ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION = str(self.ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION)

        if self._is_empty(self.CELL_TOTAL):
            self.MissingRequiredField("CELL_TOTAL")
        if not isinstance(self.CELL_TOTAL, int):
            self.CELL_TOTAL = int(self.CELL_TOTAL)

        if self._is_empty(self.ANNDATA_SCHEMA_VERSION):
            self.MissingRequiredField("ANNDATA_SCHEMA_VERSION")
        if not isinstance(self.ANNDATA_SCHEMA_VERSION, str):
            self.ANNDATA_SCHEMA_VERSION = str(self.ANNDATA_SCHEMA_VERSION)

        if self._is_empty(self.ANNDATA_STRUCTURE_VALIDATED):
            self.MissingRequiredField("ANNDATA_STRUCTURE_VALIDATED")
        if not isinstance(self.ANNDATA_STRUCTURE_VALIDATED, Bool):
            self.ANNDATA_STRUCTURE_VALIDATED = Bool(self.ANNDATA_STRUCTURE_VALIDATED)

        if self.TSS_FRAGMENTS is not None and not isinstance(self.TSS_FRAGMENTS, int):
            self.TSS_FRAGMENTS = int(self.TSS_FRAGMENTS)

        if self.TSS_ENRICHMENT is not None and not isinstance(self.TSS_ENRICHMENT, float):
            self.TSS_ENRICHMENT = float(self.TSS_ENRICHMENT)

        if self.TSS_PERCENTILE is not None and not isinstance(self.TSS_PERCENTILE, float):
            self.TSS_PERCENTILE = float(self.TSS_PERCENTILE)

        if self.DNASE_SENSITIVE_REGION_FRAGMENTS is not None and not isinstance(self.DNASE_SENSITIVE_REGION_FRAGMENTS, int):
            self.DNASE_SENSITIVE_REGION_FRAGMENTS = int(self.DNASE_SENSITIVE_REGION_FRAGMENTS)

        if self.ENHANCER_REGION_FRAGMENTS is not None and not isinstance(self.ENHANCER_REGION_FRAGMENTS, int):
            self.ENHANCER_REGION_FRAGMENTS = int(self.ENHANCER_REGION_FRAGMENTS)

        if self.PROMOTER_REGION_FRAGMENTS is not None and not isinstance(self.PROMOTER_REGION_FRAGMENTS, int):
            self.PROMOTER_REGION_FRAGMENTS = int(self.PROMOTER_REGION_FRAGMENTS)

        if self.ON_TARGET_FRAGMENTS is not None and not isinstance(self.ON_TARGET_FRAGMENTS, int):
            self.ON_TARGET_FRAGMENTS = int(self.ON_TARGET_FRAGMENTS)

        if self.BLACKLIST_REGION_FRAGMENTS is not None and not isinstance(self.BLACKLIST_REGION_FRAGMENTS, int):
            self.BLACKLIST_REGION_FRAGMENTS = int(self.BLACKLIST_REGION_FRAGMENTS)

        if self.BLACKLIST_RATIO is not None and not isinstance(self.BLACKLIST_RATIO, float):
            self.BLACKLIST_RATIO = float(self.BLACKLIST_RATIO)

        if self.PEAK_REGION_FRAGMENTS is not None and not isinstance(self.PEAK_REGION_FRAGMENTS, int):
            self.PEAK_REGION_FRAGMENTS = int(self.PEAK_REGION_FRAGMENTS)

        if self.PEAK_REGION_CUTSITES is not None and not isinstance(self.PEAK_REGION_CUTSITES, int):
            self.PEAK_REGION_CUTSITES = int(self.PEAK_REGION_CUTSITES)

        if self.NUCLEOSOME_SIGNAL is not None and not isinstance(self.NUCLEOSOME_SIGNAL, float):
            self.NUCLEOSOME_SIGNAL = float(self.NUCLEOSOME_SIGNAL)

        if self.NUCLEOSOME_PERCENTILE is not None and not isinstance(self.NUCLEOSOME_PERCENTILE, float):
            self.NUCLEOSOME_PERCENTILE = float(self.NUCLEOSOME_PERCENTILE)

        if not isinstance(self.SEURAT_CLUSTERS, list):
            self.SEURAT_CLUSTERS = [self.SEURAT_CLUSTERS] if self.SEURAT_CLUSTERS is not None else []
        self.SEURAT_CLUSTERS = [v if isinstance(v, str) else str(v) for v in self.SEURAT_CLUSTERS]

        if self.N_COUNT_RNA is not None and not isinstance(self.N_COUNT_RNA, int):
            self.N_COUNT_RNA = int(self.N_COUNT_RNA)

        if self.N_FEATURE_RNA is not None and not isinstance(self.N_FEATURE_RNA, int):
            self.N_FEATURE_RNA = int(self.N_FEATURE_RNA)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SingleCellLevel1Attributes(BaseSequencingLevel1Attributes):
    """
    Shared upstream single-cell / single-nucleus preparation attributes for single-cell sequencing Level 1
    (tissue-to-cell/nucleus steps common to scRNA-seq and scATAC-seq)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["SingleCellLevel1Attributes"]
    class_class_curie: ClassVar[str] = "htan:SingleCellLevel1Attributes"
    class_name: ClassVar[str] = "SingleCellLevel1Attributes"
    class_model_uri: ClassVar[URIRef] = HTAN.SingleCellLevel1Attributes

    HTAN_DATA_FILE_ID: Union[str, SingleCellLevel1AttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    SINGLE_CELL_ISOLATION_METHOD: Union[str, "SingleCellIsolationMethodEnum"] = None
    DISSOCIATION_METHOD: Union[str, "DissociationMethodEnum"] = None
    NUCLEIC_ACID_SOURCE: Union[str, "NucleicAcidSourceEnum"] = None
    LIBRARY_CONSTRUCTION_METHOD: Union[str, "LibraryConstructionMethodEnum"] = None
    CRYOPRESERVED_CELLS_IN_SAMPLE: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, SingleCellLevel1AttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = SingleCellLevel1AttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.SINGLE_CELL_ISOLATION_METHOD):
            self.MissingRequiredField("SINGLE_CELL_ISOLATION_METHOD")
        if not isinstance(self.SINGLE_CELL_ISOLATION_METHOD, SingleCellIsolationMethodEnum):
            self.SINGLE_CELL_ISOLATION_METHOD = SingleCellIsolationMethodEnum(self.SINGLE_CELL_ISOLATION_METHOD)

        if self._is_empty(self.DISSOCIATION_METHOD):
            self.MissingRequiredField("DISSOCIATION_METHOD")
        if not isinstance(self.DISSOCIATION_METHOD, DissociationMethodEnum):
            self.DISSOCIATION_METHOD = DissociationMethodEnum(self.DISSOCIATION_METHOD)

        if self._is_empty(self.NUCLEIC_ACID_SOURCE):
            self.MissingRequiredField("NUCLEIC_ACID_SOURCE")
        if not isinstance(self.NUCLEIC_ACID_SOURCE, NucleicAcidSourceEnum):
            self.NUCLEIC_ACID_SOURCE = NucleicAcidSourceEnum(self.NUCLEIC_ACID_SOURCE)

        if self._is_empty(self.LIBRARY_CONSTRUCTION_METHOD):
            self.MissingRequiredField("LIBRARY_CONSTRUCTION_METHOD")
        if not isinstance(self.LIBRARY_CONSTRUCTION_METHOD, LibraryConstructionMethodEnum):
            self.LIBRARY_CONSTRUCTION_METHOD = LibraryConstructionMethodEnum(self.LIBRARY_CONSTRUCTION_METHOD)

        if self.CRYOPRESERVED_CELLS_IN_SAMPLE is not None and not isinstance(self.CRYOPRESERVED_CELLS_IN_SAMPLE, Bool):
            self.CRYOPRESERVED_CELLS_IN_SAMPLE = Bool(self.CRYOPRESERVED_CELLS_IN_SAMPLE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ScATACLevel1(SingleCellLevel1Attributes):
    """
    scATAC-seq Level 1 data - Raw sequencing files and metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ScATACLevel1"]
    class_class_curie: ClassVar[str] = "htan:ScATACLevel1"
    class_name: ClassVar[str] = "scATACLevel1"
    class_model_uri: ClassVar[URIRef] = HTAN.ScATACLevel1

    HTAN_DATA_FILE_ID: Union[str, ScATACLevel1HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    LIBRARY_LAYOUT: Union[str, "LibraryLayoutEnum"] = None
    SEQUENCING_PLATFORM: Union[str, "SequencingPlatformEnum"] = None
    SINGLE_CELL_ISOLATION_METHOD: Union[str, "SingleCellIsolationMethodEnum"] = None
    DISSOCIATION_METHOD: Union[str, "DissociationMethodEnum"] = None
    NUCLEIC_ACID_SOURCE: Union[str, "NucleicAcidSourceEnum"] = None
    LIBRARY_CONSTRUCTION_METHOD: Union[str, "LibraryConstructionMethodEnum"] = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    REVERSE_TRANSCRIPTION_PRIMER: Union[str, "ReverseTranscriptionPrimerEnum"] = None
    SPIKE_IN: Union[str, "SpikeInEnum"] = None
    NUCLEUS_IDENTIFIER: str = None
    NUCLEI_BARCODE_READ: str = None
    NUCLEI_BARCODE_LENGTH: int = None
    SCATAC_SEQ_READ_1: Union[str, "SequencingReadEnum"] = None
    SCATAC_SEQ_READ_2: Union[str, "SequencingReadEnum"] = None
    TOTAL_NUMBER_OF_PASSING_NUCLEI: int = None
    SINGLE_NUCLEUS_BUFFER: Union[str, "SingleNucleusBufferEnum"] = None
    TRANSPOSITION_REACTION: Union[str, "TranspositionReactionEnum"] = None
    TOTAL_READS: int = None
    MAP_Q_30: float = None
    TOTAL_READ_PAIRS: int = None
    NUCLEI_BARCODE: Optional[str] = None
    SCATAC_SEQ_READ_3: Optional[Union[str, "SequencingReadEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, ScATACLevel1HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = ScATACLevel1HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.REVERSE_TRANSCRIPTION_PRIMER):
            self.MissingRequiredField("REVERSE_TRANSCRIPTION_PRIMER")
        if not isinstance(self.REVERSE_TRANSCRIPTION_PRIMER, ReverseTranscriptionPrimerEnum):
            self.REVERSE_TRANSCRIPTION_PRIMER = ReverseTranscriptionPrimerEnum(self.REVERSE_TRANSCRIPTION_PRIMER)

        if self._is_empty(self.SPIKE_IN):
            self.MissingRequiredField("SPIKE_IN")
        if not isinstance(self.SPIKE_IN, SpikeInEnum):
            self.SPIKE_IN = SpikeInEnum(self.SPIKE_IN)

        if self._is_empty(self.NUCLEUS_IDENTIFIER):
            self.MissingRequiredField("NUCLEUS_IDENTIFIER")
        if not isinstance(self.NUCLEUS_IDENTIFIER, str):
            self.NUCLEUS_IDENTIFIER = str(self.NUCLEUS_IDENTIFIER)

        if self._is_empty(self.NUCLEI_BARCODE_READ):
            self.MissingRequiredField("NUCLEI_BARCODE_READ")
        if not isinstance(self.NUCLEI_BARCODE_READ, str):
            self.NUCLEI_BARCODE_READ = str(self.NUCLEI_BARCODE_READ)

        if self._is_empty(self.NUCLEI_BARCODE_LENGTH):
            self.MissingRequiredField("NUCLEI_BARCODE_LENGTH")
        if not isinstance(self.NUCLEI_BARCODE_LENGTH, int):
            self.NUCLEI_BARCODE_LENGTH = int(self.NUCLEI_BARCODE_LENGTH)

        if self._is_empty(self.SCATAC_SEQ_READ_1):
            self.MissingRequiredField("SCATAC_SEQ_READ_1")
        if not isinstance(self.SCATAC_SEQ_READ_1, SequencingReadEnum):
            self.SCATAC_SEQ_READ_1 = SequencingReadEnum(self.SCATAC_SEQ_READ_1)

        if self._is_empty(self.SCATAC_SEQ_READ_2):
            self.MissingRequiredField("SCATAC_SEQ_READ_2")
        if not isinstance(self.SCATAC_SEQ_READ_2, SequencingReadEnum):
            self.SCATAC_SEQ_READ_2 = SequencingReadEnum(self.SCATAC_SEQ_READ_2)

        if self._is_empty(self.TOTAL_NUMBER_OF_PASSING_NUCLEI):
            self.MissingRequiredField("TOTAL_NUMBER_OF_PASSING_NUCLEI")
        if not isinstance(self.TOTAL_NUMBER_OF_PASSING_NUCLEI, int):
            self.TOTAL_NUMBER_OF_PASSING_NUCLEI = int(self.TOTAL_NUMBER_OF_PASSING_NUCLEI)

        if self._is_empty(self.SINGLE_NUCLEUS_BUFFER):
            self.MissingRequiredField("SINGLE_NUCLEUS_BUFFER")
        if not isinstance(self.SINGLE_NUCLEUS_BUFFER, SingleNucleusBufferEnum):
            self.SINGLE_NUCLEUS_BUFFER = SingleNucleusBufferEnum(self.SINGLE_NUCLEUS_BUFFER)

        if self._is_empty(self.TRANSPOSITION_REACTION):
            self.MissingRequiredField("TRANSPOSITION_REACTION")
        if not isinstance(self.TRANSPOSITION_REACTION, TranspositionReactionEnum):
            self.TRANSPOSITION_REACTION = TranspositionReactionEnum(self.TRANSPOSITION_REACTION)

        if self._is_empty(self.TOTAL_READS):
            self.MissingRequiredField("TOTAL_READS")
        if not isinstance(self.TOTAL_READS, int):
            self.TOTAL_READS = int(self.TOTAL_READS)

        if self._is_empty(self.MAP_Q_30):
            self.MissingRequiredField("MAP_Q_30")
        if not isinstance(self.MAP_Q_30, float):
            self.MAP_Q_30 = float(self.MAP_Q_30)

        if self._is_empty(self.TOTAL_READ_PAIRS):
            self.MissingRequiredField("TOTAL_READ_PAIRS")
        if not isinstance(self.TOTAL_READ_PAIRS, int):
            self.TOTAL_READ_PAIRS = int(self.TOTAL_READ_PAIRS)

        if self.NUCLEI_BARCODE is not None and not isinstance(self.NUCLEI_BARCODE, str):
            self.NUCLEI_BARCODE = str(self.NUCLEI_BARCODE)

        if self.SCATAC_SEQ_READ_3 is not None and not isinstance(self.SCATAC_SEQ_READ_3, SequencingReadEnum):
            self.SCATAC_SEQ_READ_3 = SequencingReadEnum(self.SCATAC_SEQ_READ_3)

        super().__post_init__(**kwargs)


# Enumerations
class SequencingReadEnum(EnumDefinitionImpl):
    """
    Content type of a single-cell ATAC-seq sequencing read
    """
    _defn = EnumDefinition(
        name="SequencingReadEnum",
        description="Content type of a single-cell ATAC-seq sequencing read",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cell Barcode",
            PermissibleValue(
                text="Cell Barcode",
                description="""Sequencing read containing the cellular barcode sequence used to identify individual nuclei or cells"""))
        setattr(cls, "Cell Barcode and DNA Insert",
            PermissibleValue(
                text="Cell Barcode and DNA Insert",
                description="""Sequencing read containing both the cellular barcode sequence and the captured DNA insert sequence"""))
        setattr(cls, "DNA Insert",
            PermissibleValue(
                text="DNA Insert",
                description="""Sequencing read containing the genomic DNA fragment captured during the transposition reaction"""))
        setattr(cls, "Sample Index",
            PermissibleValue(
                text="Sample Index",
                description="""Sequencing read containing the sample index (i7/i5 index) sequence used for sample identification and multiplexing"""))
        setattr(cls, "Sample Index and DNA Insert",
            PermissibleValue(
                text="Sample Index and DNA Insert",
                description="""Sequencing read containing both the sample index sequence and the captured genomic DNA insert sequence"""))

class SingleNucleusBufferEnum(EnumDefinitionImpl):
    """
    Buffer used for single-nucleus preparation prior to transposition
    """
    NIB = PermissibleValue(
        text="NIB",
        description="""Nuclei isolation buffer used for preparation of isolated nuclei prior to single-cell chromatin accessibility profiling""")
    Omni = PermissibleValue(
        text="Omni",
        description="Omni assay buffer used for single-nucleus chromatin accessibility profiling workflows")
    TST = PermissibleValue(
        text="TST",
        description="""TST buffer used for single-nucleus preparation and transposition-based chromatin accessibility assays""")

    _defn = EnumDefinition(
        name="SingleNucleusBufferEnum",
        description="Buffer used for single-nucleus preparation prior to transposition",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10x",
            PermissibleValue(
                text="10x",
                description="""Single-nucleus preparation buffer used in the 10x Genomics single-cell ATAC-seq or multiome workflow"""))

class TranspositionReactionEnum(EnumDefinitionImpl):
    """
    Transposase chemistry used in the transposition reaction
    """
    Tn5 = PermissibleValue(
        text="Tn5",
        description="""Transposition reaction performed using Tn5 transposase-based chromatin accessibility assay chemistry""")

    _defn = EnumDefinition(
        name="TranspositionReactionEnum",
        description="Transposase chemistry used in the transposition reaction",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Diagenode-loaded Apex-Bio",
            PermissibleValue(
                text="Diagenode-loaded Apex-Bio",
                description="""Transposition reaction performed using Diagenode-loaded Tn5 transposase supplied by Apex-Bio"""))
        setattr(cls, "Diagenode-unloaded Apex-Bio",
            PermissibleValue(
                text="Diagenode-unloaded Apex-Bio",
                description="""Transposition reaction performed using Diagenode Tn5 transposase with user-loaded adapters supplied by Apex-Bio"""))
        setattr(cls, "EZ-Tn5",
            PermissibleValue(
                text="EZ-Tn5",
                description="Transposition reaction performed using EZ-Tn5 transposase-based chemistry"))
        setattr(cls, "In-House",
            PermissibleValue(
                text="In-House",
                description="""Custom transposition reaction developed or performed using an internally established protocol"""))
        setattr(cls, "Nextera Tn5",
            PermissibleValue(
                text="Nextera Tn5",
                description="Transposition reaction performed using Nextera Tn5 transposase chemistry from Illumina"))
        setattr(cls, "Tn5-059",
            PermissibleValue(
                text="Tn5-059",
                description="Transposition reaction performed using Tn5-059 transposase variant chemistry"))

class ATACGeneActivityWorkflowTypeEnum(EnumDefinitionImpl):
    """
    Generic name for the workflow used to analyze a single-cell ATAC-seq dataset
    """
    ArchR = PermissibleValue(
        text="ArchR",
        description="ArchR single-cell ATAC-seq analysis workflow")
    Cicero = PermissibleValue(
        text="Cicero",
        description="Cicero chromatin accessibility and co-accessibility analysis workflow")
    MAESTRO = PermissibleValue(
        text="MAESTRO",
        description="MAESTRO single-cell ATAC-seq and multi-omics analysis workflow")
    Other = PermissibleValue(
        text="Other",
        description="Other workflow type")
    Signac = PermissibleValue(
        text="Signac",
        description="Signac single-cell chromatin accessibility analysis workflow")
    SnapATAC2 = PermissibleValue(
        text="SnapATAC2",
        description="SnapATAC2 single-cell ATAC-seq analysis workflow")

    _defn = EnumDefinition(
        name="ATACGeneActivityWorkflowTypeEnum",
        description="Generic name for the workflow used to analyze a single-cell ATAC-seq dataset",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cell Ranger ATAC",
            PermissibleValue(
                text="Cell Ranger ATAC",
                description="10x Genomics Cell Ranger ATAC workflow"))

class LibraryLayoutEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="LibraryLayoutEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Paired-end",
            PermissibleValue(
                text="Paired-end",
                description="Paired-end sequencing"))
        setattr(cls, "Single-end",
            PermissibleValue(
                text="Single-end",
                description="Single-end sequencing"))

class SequencingPlatformEnum(EnumDefinitionImpl):

    ABI_SOLID = PermissibleValue(
        text="ABI_SOLID",
        description="ABI SOLID sequencing platform")
    BGISEQ = PermissibleValue(
        text="BGISEQ",
        description="BGI sequencing platform")
    CAPILLARY = PermissibleValue(
        text="CAPILLARY",
        description="Capillary sequencing platform")
    COMPLETE_GENOMICS = PermissibleValue(
        text="COMPLETE_GENOMICS",
        description="Complete Genomics sequencing platform")
    HELICOS = PermissibleValue(
        text="HELICOS",
        description="Helicos sequencing platform")
    ILLUMINA = PermissibleValue(
        text="ILLUMINA",
        description="Illumina sequencing platform")
    ION_TORRENT = PermissibleValue(
        text="ION_TORRENT",
        description="Ion Torrent sequencing platform")
    LS454 = PermissibleValue(
        text="LS454",
        description="454 sequencing platform")
    OXFORD_NANOPORE = PermissibleValue(
        text="OXFORD_NANOPORE",
        description="Oxford Nanopore sequencing platform")
    PACBIO_SMRT = PermissibleValue(
        text="PACBIO_SMRT",
        description="PacBio SMRT sequencing platform")

    _defn = EnumDefinition(
        name="SequencingPlatformEnum",
    )

class GenomicReferenceEnum(EnumDefinitionImpl):
    """
    Genomic or transcriptomic reference assembly used for alignment
    """
    GRCh37 = PermissibleValue(
        text="GRCh37",
        description="Genome Reference Consortium human build 37")
    GRCh38 = PermissibleValue(
        text="GRCh38",
        description="Genome Reference Consortium human build 38")
    hg19 = PermissibleValue(
        text="hg19",
        description="UCSC human genome reference hg19")
    hg38 = PermissibleValue(
        text="hg38",
        description="UCSC human genome reference hg38")

    _defn = EnumDefinition(
        name="GenomicReferenceEnum",
        description="Genomic or transcriptomic reference assembly used for alignment",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GRCh37.p13",
            PermissibleValue(
                text="GRCh37.p13",
                description="GRCh37 patch release 13"))
        setattr(cls, "GRCh38.p13",
            PermissibleValue(
                text="GRCh38.p13",
                description="GRCh38 patch release 13"))
        setattr(cls, "GRCh38.p14",
            PermissibleValue(
                text="GRCh38.p14",
                description="GRCh38 patch release 14"))

class DissociationMethodEnum(EnumDefinitionImpl):

    Enzymatic = PermissibleValue(
        text="Enzymatic",
        description="Enzymatic dissociation method")
    Mechanical = PermissibleValue(
        text="Mechanical",
        description="Mechanical dissociation method")
    Other = PermissibleValue(
        text="Other",
        description="Other dissociation method")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown dissociation method")

    _defn = EnumDefinition(
        name="DissociationMethodEnum",
    )

class LibraryConstructionMethodEnum(EnumDefinitionImpl):

    InDrop = PermissibleValue(
        text="InDrop",
        description="InDrop library construction method")
    Other = PermissibleValue(
        text="Other",
        description="Other library construction method")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown library construction method")

    _defn = EnumDefinition(
        name="LibraryConstructionMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10X Genomics",
            PermissibleValue(
                text="10X Genomics",
                description="10X Genomics library construction method"))
        setattr(cls, "Drop-seq",
            PermissibleValue(
                text="Drop-seq",
                description="Drop-seq library construction method"))
        setattr(cls, "Fluidigm C1",
            PermissibleValue(
                text="Fluidigm C1",
                description="Fluidigm C1 library construction method"))
        setattr(cls, "Smart-seq",
            PermissibleValue(
                text="Smart-seq",
                description="Smart-seq library construction method"))

class NucleicAcidSourceEnum(EnumDefinitionImpl):

    DNA = PermissibleValue(
        text="DNA",
        description="DNA nucleic acid source")
    RNA = PermissibleValue(
        text="RNA",
        description="RNA nucleic acid source")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown nucleic acid source")

    _defn = EnumDefinition(
        name="NucleicAcidSourceEnum",
    )

class SingleCellIsolationMethodEnum(EnumDefinitionImpl):

    Microfluidics = PermissibleValue(
        text="Microfluidics",
        description="Microfluidics isolation method")
    Other = PermissibleValue(
        text="Other",
        description="Other isolation method")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown isolation method")

    _defn = EnumDefinition(
        name="SingleCellIsolationMethodEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Cell Sorting",
            PermissibleValue(
                text="Cell Sorting",
                description="Cell sorting isolation method"))
        setattr(cls, "Droplet-based",
            PermissibleValue(
                text="Droplet-based",
                description="Droplet-based isolation method"))
        setattr(cls, "Manual Picking",
            PermissibleValue(
                text="Manual Picking",
                description="Manual picking isolation method"))

class ReverseTranscriptionPrimerEnum(EnumDefinitionImpl):

    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown reverse transcription primer")

    _defn = EnumDefinition(
        name="ReverseTranscriptionPrimerEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Oligo-dT",
            PermissibleValue(
                text="Oligo-dT",
                description="Oligo-dT reverse transcription primer"))
        setattr(cls, "Random Hexamer",
            PermissibleValue(
                text="Random Hexamer",
                description="Random hexamer reverse transcription primer"))

class SpikeInEnum(EnumDefinitionImpl):

    ERCC = PermissibleValue(
        text="ERCC",
        description="ERCC spike-in")
    Other = PermissibleValue(
        text="Other",
        description="Other spike-in")
    Unknown = PermissibleValue(
        text="Unknown",
        description="Unknown spike-in")

    _defn = EnumDefinition(
        name="SpikeInEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "None",
            PermissibleValue(
                text="None",
                description="No spike-in"))

# Slots
class slots:
    pass

slots.scATACseqData__level1_data = Slot(uri=HTAN.level1_data, name="scATACseqData__level1_data", curie=HTAN.curie('level1_data'),
                   model_uri=HTAN.scATACseqData__level1_data, domain=None, range=Optional[Union[dict, ScATACLevel1]])

slots.scATACseqData__level2_data = Slot(uri=HTAN.level2_data, name="scATACseqData__level2_data", curie=HTAN.curie('level2_data'),
                   model_uri=HTAN.scATACseqData__level2_data, domain=None, range=Optional[Union[dict, ScATACLevel2]])

slots.scATACseqData__level3_4_data = Slot(uri=HTAN.level3_4_data, name="scATACseqData__level3_4_data", curie=HTAN.curie('level3_4_data'),
                   model_uri=HTAN.scATACseqData__level3_4_data, domain=None, range=Optional[Union[dict, ScATACLevel3and4]])

slots.scATACLevel1__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="scATACLevel1__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.scATACLevel1__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(fastq|fastq\.gz)$'))

slots.scATACLevel1__FILENAME = Slot(uri=HTAN.FILENAME, name="scATACLevel1__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.scATACLevel1__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.(fastq|fq)(\.gz)?$'))

slots.scATACLevel1__REVERSE_TRANSCRIPTION_PRIMER = Slot(uri=HTAN.REVERSE_TRANSCRIPTION_PRIMER, name="scATACLevel1__REVERSE_TRANSCRIPTION_PRIMER", curie=HTAN.curie('REVERSE_TRANSCRIPTION_PRIMER'),
                   model_uri=HTAN.scATACLevel1__REVERSE_TRANSCRIPTION_PRIMER, domain=None, range=Union[str, "ReverseTranscriptionPrimerEnum"])

slots.scATACLevel1__SPIKE_IN = Slot(uri=HTAN.SPIKE_IN, name="scATACLevel1__SPIKE_IN", curie=HTAN.curie('SPIKE_IN'),
                   model_uri=HTAN.scATACLevel1__SPIKE_IN, domain=None, range=Union[str, "SpikeInEnum"])

slots.scATACLevel1__NUCLEUS_IDENTIFIER = Slot(uri=HTAN.NUCLEUS_IDENTIFIER, name="scATACLevel1__NUCLEUS_IDENTIFIER", curie=HTAN.curie('NUCLEUS_IDENTIFIER'),
                   model_uri=HTAN.scATACLevel1__NUCLEUS_IDENTIFIER, domain=None, range=str)

slots.scATACLevel1__NUCLEI_BARCODE = Slot(uri=HTAN.NUCLEI_BARCODE, name="scATACLevel1__NUCLEI_BARCODE", curie=HTAN.curie('NUCLEI_BARCODE'),
                   model_uri=HTAN.scATACLevel1__NUCLEI_BARCODE, domain=None, range=Optional[str])

slots.scATACLevel1__NUCLEI_BARCODE_READ = Slot(uri=HTAN.NUCLEI_BARCODE_READ, name="scATACLevel1__NUCLEI_BARCODE_READ", curie=HTAN.curie('NUCLEI_BARCODE_READ'),
                   model_uri=HTAN.scATACLevel1__NUCLEI_BARCODE_READ, domain=None, range=str)

slots.scATACLevel1__NUCLEI_BARCODE_LENGTH = Slot(uri=HTAN.NUCLEI_BARCODE_LENGTH, name="scATACLevel1__NUCLEI_BARCODE_LENGTH", curie=HTAN.curie('NUCLEI_BARCODE_LENGTH'),
                   model_uri=HTAN.scATACLevel1__NUCLEI_BARCODE_LENGTH, domain=None, range=int)

slots.scATACLevel1__SCATAC_SEQ_READ_1 = Slot(uri=HTAN.SCATAC_SEQ_READ_1, name="scATACLevel1__SCATAC_SEQ_READ_1", curie=HTAN.curie('SCATAC_SEQ_READ_1'),
                   model_uri=HTAN.scATACLevel1__SCATAC_SEQ_READ_1, domain=None, range=Union[str, "SequencingReadEnum"])

slots.scATACLevel1__SCATAC_SEQ_READ_2 = Slot(uri=HTAN.SCATAC_SEQ_READ_2, name="scATACLevel1__SCATAC_SEQ_READ_2", curie=HTAN.curie('SCATAC_SEQ_READ_2'),
                   model_uri=HTAN.scATACLevel1__SCATAC_SEQ_READ_2, domain=None, range=Union[str, "SequencingReadEnum"])

slots.scATACLevel1__SCATAC_SEQ_READ_3 = Slot(uri=HTAN.SCATAC_SEQ_READ_3, name="scATACLevel1__SCATAC_SEQ_READ_3", curie=HTAN.curie('SCATAC_SEQ_READ_3'),
                   model_uri=HTAN.scATACLevel1__SCATAC_SEQ_READ_3, domain=None, range=Optional[Union[str, "SequencingReadEnum"]])

slots.scATACLevel1__TOTAL_NUMBER_OF_PASSING_NUCLEI = Slot(uri=HTAN.TOTAL_NUMBER_OF_PASSING_NUCLEI, name="scATACLevel1__TOTAL_NUMBER_OF_PASSING_NUCLEI", curie=HTAN.curie('TOTAL_NUMBER_OF_PASSING_NUCLEI'),
                   model_uri=HTAN.scATACLevel1__TOTAL_NUMBER_OF_PASSING_NUCLEI, domain=None, range=int)

slots.scATACLevel1__SINGLE_NUCLEUS_BUFFER = Slot(uri=HTAN.SINGLE_NUCLEUS_BUFFER, name="scATACLevel1__SINGLE_NUCLEUS_BUFFER", curie=HTAN.curie('SINGLE_NUCLEUS_BUFFER'),
                   model_uri=HTAN.scATACLevel1__SINGLE_NUCLEUS_BUFFER, domain=None, range=Union[str, "SingleNucleusBufferEnum"])

slots.scATACLevel1__TRANSPOSITION_REACTION = Slot(uri=HTAN.TRANSPOSITION_REACTION, name="scATACLevel1__TRANSPOSITION_REACTION", curie=HTAN.curie('TRANSPOSITION_REACTION'),
                   model_uri=HTAN.scATACLevel1__TRANSPOSITION_REACTION, domain=None, range=Union[str, "TranspositionReactionEnum"])

slots.scATACLevel1__TOTAL_READS = Slot(uri=HTAN.TOTAL_READS, name="scATACLevel1__TOTAL_READS", curie=HTAN.curie('TOTAL_READS'),
                   model_uri=HTAN.scATACLevel1__TOTAL_READS, domain=None, range=int)

slots.scATACLevel1__MAP_Q_30 = Slot(uri=HTAN.MAP_Q_30, name="scATACLevel1__MAP_Q_30", curie=HTAN.curie('MAP_Q_30'),
                   model_uri=HTAN.scATACLevel1__MAP_Q_30, domain=None, range=float)

slots.scATACLevel1__TOTAL_READ_PAIRS = Slot(uri=HTAN.TOTAL_READ_PAIRS, name="scATACLevel1__TOTAL_READ_PAIRS", curie=HTAN.curie('TOTAL_READ_PAIRS'),
                   model_uri=HTAN.scATACLevel1__TOTAL_READ_PAIRS, domain=None, range=int)

slots.scATACLevel2__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="scATACLevel2__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.scATACLevel2__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(bam|cram)$'))

slots.scATACLevel2__FILENAME = Slot(uri=HTAN.FILENAME, name="scATACLevel2__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.scATACLevel2__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.(bam|cram)$'))

slots.scATACLevel2__AVERAGE_BASE_QUALITY = Slot(uri=HTAN.AVERAGE_BASE_QUALITY, name="scATACLevel2__AVERAGE_BASE_QUALITY", curie=HTAN.curie('AVERAGE_BASE_QUALITY'),
                   model_uri=HTAN.scATACLevel2__AVERAGE_BASE_QUALITY, domain=None, range=Optional[float])

slots.scATACLevel2__AVERAGE_INSERT_SIZE = Slot(uri=HTAN.AVERAGE_INSERT_SIZE, name="scATACLevel2__AVERAGE_INSERT_SIZE", curie=HTAN.curie('AVERAGE_INSERT_SIZE'),
                   model_uri=HTAN.scATACLevel2__AVERAGE_INSERT_SIZE, domain=None, range=Optional[float])

slots.scATACLevel2__AVERAGE_READ_LENGTH = Slot(uri=HTAN.AVERAGE_READ_LENGTH, name="scATACLevel2__AVERAGE_READ_LENGTH", curie=HTAN.curie('AVERAGE_READ_LENGTH'),
                   model_uri=HTAN.scATACLevel2__AVERAGE_READ_LENGTH, domain=None, range=Optional[float])

slots.scATACLevel2__MEAN_COVERAGE = Slot(uri=HTAN.MEAN_COVERAGE, name="scATACLevel2__MEAN_COVERAGE", curie=HTAN.curie('MEAN_COVERAGE'),
                   model_uri=HTAN.scATACLevel2__MEAN_COVERAGE, domain=None, range=Optional[float])

slots.scATACLevel2__PAIRS_ON_DIFF_CHR = Slot(uri=HTAN.PAIRS_ON_DIFF_CHR, name="scATACLevel2__PAIRS_ON_DIFF_CHR", curie=HTAN.curie('PAIRS_ON_DIFF_CHR'),
                   model_uri=HTAN.scATACLevel2__PAIRS_ON_DIFF_CHR, domain=None, range=Optional[int])

slots.scATACLevel2__PROPORTION_READS_MAPPED = Slot(uri=HTAN.PROPORTION_READS_MAPPED, name="scATACLevel2__PROPORTION_READS_MAPPED", curie=HTAN.curie('PROPORTION_READS_MAPPED'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_READS_MAPPED, domain=None, range=Optional[float])

slots.scATACLevel2__TOTAL_UNIQUELY_MAPPED = Slot(uri=HTAN.TOTAL_UNIQUELY_MAPPED, name="scATACLevel2__TOTAL_UNIQUELY_MAPPED", curie=HTAN.curie('TOTAL_UNIQUELY_MAPPED'),
                   model_uri=HTAN.scATACLevel2__TOTAL_UNIQUELY_MAPPED, domain=None, range=int)

slots.scATACLevel2__TOTAL_UNMAPPED_READS = Slot(uri=HTAN.TOTAL_UNMAPPED_READS, name="scATACLevel2__TOTAL_UNMAPPED_READS", curie=HTAN.curie('TOTAL_UNMAPPED_READS'),
                   model_uri=HTAN.scATACLevel2__TOTAL_UNMAPPED_READS, domain=None, range=int)

slots.scATACLevel2__PROPORTION_READS_DUPLICATED = Slot(uri=HTAN.PROPORTION_READS_DUPLICATED, name="scATACLevel2__PROPORTION_READS_DUPLICATED", curie=HTAN.curie('PROPORTION_READS_DUPLICATED'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_READS_DUPLICATED, domain=None, range=Optional[float])

slots.scATACLevel2__SHORT_READS = Slot(uri=HTAN.SHORT_READS, name="scATACLevel2__SHORT_READS", curie=HTAN.curie('SHORT_READS'),
                   model_uri=HTAN.scATACLevel2__SHORT_READS, domain=None, range=Optional[int])

slots.scATACLevel2__PROPORTION_COVERAGE_10X = Slot(uri=HTAN.PROPORTION_COVERAGE_10X, name="scATACLevel2__PROPORTION_COVERAGE_10X", curie=HTAN.curie('PROPORTION_COVERAGE_10X'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_COVERAGE_10X, domain=None, range=Optional[float])

slots.scATACLevel2__PROPORTION_COVERAGE_30X = Slot(uri=HTAN.PROPORTION_COVERAGE_30X, name="scATACLevel2__PROPORTION_COVERAGE_30X", curie=HTAN.curie('PROPORTION_COVERAGE_30X'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_COVERAGE_30X, domain=None, range=Optional[float])

slots.scATACLevel2__PROPORTION_TARGETS_NO_MATCH = Slot(uri=HTAN.PROPORTION_TARGETS_NO_MATCH, name="scATACLevel2__PROPORTION_TARGETS_NO_MATCH", curie=HTAN.curie('PROPORTION_TARGETS_NO_MATCH'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_TARGETS_NO_MATCH, domain=None, range=Optional[float])

slots.scATACLevel2__PROPORTION_BASE_MISMATCH = Slot(uri=HTAN.PROPORTION_BASE_MISMATCH, name="scATACLevel2__PROPORTION_BASE_MISMATCH", curie=HTAN.curie('PROPORTION_BASE_MISMATCH'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_BASE_MISMATCH, domain=None, range=Optional[float])

slots.scATACLevel2__PROPORTION_MITOCHONDRIAL_READS = Slot(uri=HTAN.PROPORTION_MITOCHONDRIAL_READS, name="scATACLevel2__PROPORTION_MITOCHONDRIAL_READS", curie=HTAN.curie('PROPORTION_MITOCHONDRIAL_READS'),
                   model_uri=HTAN.scATACLevel2__PROPORTION_MITOCHONDRIAL_READS, domain=None, range=Optional[float])

slots.scATACLevel2__CONTAMINATION = Slot(uri=HTAN.CONTAMINATION, name="scATACLevel2__CONTAMINATION", curie=HTAN.curie('CONTAMINATION'),
                   model_uri=HTAN.scATACLevel2__CONTAMINATION, domain=None, range=Optional[float])

slots.scATACLevel2__CONTAMINATION_ERROR = Slot(uri=HTAN.CONTAMINATION_ERROR, name="scATACLevel2__CONTAMINATION_ERROR", curie=HTAN.curie('CONTAMINATION_ERROR'),
                   model_uri=HTAN.scATACLevel2__CONTAMINATION_ERROR, domain=None, range=Optional[float])

slots.scATACLevel2__MEDIAN_FRAGMENTS_PER_CELL = Slot(uri=HTAN.MEDIAN_FRAGMENTS_PER_CELL, name="scATACLevel2__MEDIAN_FRAGMENTS_PER_CELL", curie=HTAN.curie('MEDIAN_FRAGMENTS_PER_CELL'),
                   model_uri=HTAN.scATACLevel2__MEDIAN_FRAGMENTS_PER_CELL, domain=None, range=float)

slots.scATACLevel2__MEDIAN_GENES_PER_CELL = Slot(uri=HTAN.MEDIAN_GENES_PER_CELL, name="scATACLevel2__MEDIAN_GENES_PER_CELL", curie=HTAN.curie('MEDIAN_GENES_PER_CELL'),
                   model_uri=HTAN.scATACLevel2__MEDIAN_GENES_PER_CELL, domain=None, range=float)

slots.scATACLevel2__NUMBER_OF_CELLS = Slot(uri=HTAN.NUMBER_OF_CELLS, name="scATACLevel2__NUMBER_OF_CELLS", curie=HTAN.curie('NUMBER_OF_CELLS'),
                   model_uri=HTAN.scATACLevel2__NUMBER_OF_CELLS, domain=None, range=int)

slots.scATACLevel2__THRESHOLD_FOR_MINIMUM_PASSING_READS = Slot(uri=HTAN.THRESHOLD_FOR_MINIMUM_PASSING_READS, name="scATACLevel2__THRESHOLD_FOR_MINIMUM_PASSING_READS", curie=HTAN.curie('THRESHOLD_FOR_MINIMUM_PASSING_READS'),
                   model_uri=HTAN.scATACLevel2__THRESHOLD_FOR_MINIMUM_PASSING_READS, domain=None, range=Optional[int])

slots.scATACLevel2__MEDIAN_PASSING_READS_PERCENTAGE = Slot(uri=HTAN.MEDIAN_PASSING_READS_PERCENTAGE, name="scATACLevel2__MEDIAN_PASSING_READS_PERCENTAGE", curie=HTAN.curie('MEDIAN_PASSING_READS_PERCENTAGE'),
                   model_uri=HTAN.scATACLevel2__MEDIAN_PASSING_READS_PERCENTAGE, domain=None, range=float)

slots.scATACLevel2__DUPLICATE_READ_PAIRS = Slot(uri=HTAN.DUPLICATE_READ_PAIRS, name="scATACLevel2__DUPLICATE_READ_PAIRS", curie=HTAN.curie('DUPLICATE_READ_PAIRS'),
                   model_uri=HTAN.scATACLevel2__DUPLICATE_READ_PAIRS, domain=None, range=int)

slots.scATACLevel2__CHIMERIC_READ_PAIRS = Slot(uri=HTAN.CHIMERIC_READ_PAIRS, name="scATACLevel2__CHIMERIC_READ_PAIRS", curie=HTAN.curie('CHIMERIC_READ_PAIRS'),
                   model_uri=HTAN.scATACLevel2__CHIMERIC_READ_PAIRS, domain=None, range=int)

slots.scATACLevel2__UNMAPPED_READ_PAIRS = Slot(uri=HTAN.UNMAPPED_READ_PAIRS, name="scATACLevel2__UNMAPPED_READ_PAIRS", curie=HTAN.curie('UNMAPPED_READ_PAIRS'),
                   model_uri=HTAN.scATACLevel2__UNMAPPED_READ_PAIRS, domain=None, range=int)

slots.scATACLevel2__LOW_MAP_Q = Slot(uri=HTAN.LOW_MAP_Q, name="scATACLevel2__LOW_MAP_Q", curie=HTAN.curie('LOW_MAP_Q'),
                   model_uri=HTAN.scATACLevel2__LOW_MAP_Q, domain=None, range=int)

slots.scATACLevel2__MITOCHONDRIAL_READ_PAIRS = Slot(uri=HTAN.MITOCHONDRIAL_READ_PAIRS, name="scATACLevel2__MITOCHONDRIAL_READ_PAIRS", curie=HTAN.curie('MITOCHONDRIAL_READ_PAIRS'),
                   model_uri=HTAN.scATACLevel2__MITOCHONDRIAL_READ_PAIRS, domain=None, range=int)

slots.scATACLevel2__PASSED_FILTERS = Slot(uri=HTAN.PASSED_FILTERS, name="scATACLevel2__PASSED_FILTERS", curie=HTAN.curie('PASSED_FILTERS'),
                   model_uri=HTAN.scATACLevel2__PASSED_FILTERS, domain=None, range=int)

slots.scATACLevel3and4__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="scATACLevel3and4__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.scATACLevel3and4__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(h5ad|bed)$'))

slots.scATACLevel3and4__FILENAME = Slot(uri=HTAN.FILENAME, name="scATACLevel3and4__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.scATACLevel3and4__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.(h5ad|bed)$'))

slots.scATACLevel3and4__N_COUNT_PEAKS = Slot(uri=HTAN.N_COUNT_PEAKS, name="scATACLevel3and4__N_COUNT_PEAKS", curie=HTAN.curie('N_COUNT_PEAKS'),
                   model_uri=HTAN.scATACLevel3and4__N_COUNT_PEAKS, domain=None, range=int)

slots.scATACLevel3and4__N_FEATURE_PEAKS = Slot(uri=HTAN.N_FEATURE_PEAKS, name="scATACLevel3and4__N_FEATURE_PEAKS", curie=HTAN.curie('N_FEATURE_PEAKS'),
                   model_uri=HTAN.scATACLevel3and4__N_FEATURE_PEAKS, domain=None, range=int)

slots.scATACLevel3and4__TSS_FRAGMENTS = Slot(uri=HTAN.TSS_FRAGMENTS, name="scATACLevel3and4__TSS_FRAGMENTS", curie=HTAN.curie('TSS_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__TSS_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__TSS_ENRICHMENT = Slot(uri=HTAN.TSS_ENRICHMENT, name="scATACLevel3and4__TSS_ENRICHMENT", curie=HTAN.curie('TSS_ENRICHMENT'),
                   model_uri=HTAN.scATACLevel3and4__TSS_ENRICHMENT, domain=None, range=Optional[float])

slots.scATACLevel3and4__TSS_PERCENTILE = Slot(uri=HTAN.TSS_PERCENTILE, name="scATACLevel3and4__TSS_PERCENTILE", curie=HTAN.curie('TSS_PERCENTILE'),
                   model_uri=HTAN.scATACLevel3and4__TSS_PERCENTILE, domain=None, range=Optional[float])

slots.scATACLevel3and4__DNASE_SENSITIVE_REGION_FRAGMENTS = Slot(uri=HTAN.DNASE_SENSITIVE_REGION_FRAGMENTS, name="scATACLevel3and4__DNASE_SENSITIVE_REGION_FRAGMENTS", curie=HTAN.curie('DNASE_SENSITIVE_REGION_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__DNASE_SENSITIVE_REGION_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__ENHANCER_REGION_FRAGMENTS = Slot(uri=HTAN.ENHANCER_REGION_FRAGMENTS, name="scATACLevel3and4__ENHANCER_REGION_FRAGMENTS", curie=HTAN.curie('ENHANCER_REGION_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__ENHANCER_REGION_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__PROMOTER_REGION_FRAGMENTS = Slot(uri=HTAN.PROMOTER_REGION_FRAGMENTS, name="scATACLevel3and4__PROMOTER_REGION_FRAGMENTS", curie=HTAN.curie('PROMOTER_REGION_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__PROMOTER_REGION_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__ON_TARGET_FRAGMENTS = Slot(uri=HTAN.ON_TARGET_FRAGMENTS, name="scATACLevel3and4__ON_TARGET_FRAGMENTS", curie=HTAN.curie('ON_TARGET_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__ON_TARGET_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__BLACKLIST_REGION_FRAGMENTS = Slot(uri=HTAN.BLACKLIST_REGION_FRAGMENTS, name="scATACLevel3and4__BLACKLIST_REGION_FRAGMENTS", curie=HTAN.curie('BLACKLIST_REGION_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__BLACKLIST_REGION_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__BLACKLIST_RATIO = Slot(uri=HTAN.BLACKLIST_RATIO, name="scATACLevel3and4__BLACKLIST_RATIO", curie=HTAN.curie('BLACKLIST_RATIO'),
                   model_uri=HTAN.scATACLevel3and4__BLACKLIST_RATIO, domain=None, range=Optional[float])

slots.scATACLevel3and4__PEAK_REGION_FRAGMENTS = Slot(uri=HTAN.PEAK_REGION_FRAGMENTS, name="scATACLevel3and4__PEAK_REGION_FRAGMENTS", curie=HTAN.curie('PEAK_REGION_FRAGMENTS'),
                   model_uri=HTAN.scATACLevel3and4__PEAK_REGION_FRAGMENTS, domain=None, range=Optional[int])

slots.scATACLevel3and4__PEAK_REGION_CUTSITES = Slot(uri=HTAN.PEAK_REGION_CUTSITES, name="scATACLevel3and4__PEAK_REGION_CUTSITES", curie=HTAN.curie('PEAK_REGION_CUTSITES'),
                   model_uri=HTAN.scATACLevel3and4__PEAK_REGION_CUTSITES, domain=None, range=Optional[int])

slots.scATACLevel3and4__NUCLEOSOME_SIGNAL = Slot(uri=HTAN.NUCLEOSOME_SIGNAL, name="scATACLevel3and4__NUCLEOSOME_SIGNAL", curie=HTAN.curie('NUCLEOSOME_SIGNAL'),
                   model_uri=HTAN.scATACLevel3and4__NUCLEOSOME_SIGNAL, domain=None, range=Optional[float])

slots.scATACLevel3and4__NUCLEOSOME_PERCENTILE = Slot(uri=HTAN.NUCLEOSOME_PERCENTILE, name="scATACLevel3and4__NUCLEOSOME_PERCENTILE", curie=HTAN.curie('NUCLEOSOME_PERCENTILE'),
                   model_uri=HTAN.scATACLevel3and4__NUCLEOSOME_PERCENTILE, domain=None, range=Optional[float])

slots.scATACLevel3and4__PERCENTAGE_READS_IN_PEAKS = Slot(uri=HTAN.PERCENTAGE_READS_IN_PEAKS, name="scATACLevel3and4__PERCENTAGE_READS_IN_PEAKS", curie=HTAN.curie('PERCENTAGE_READS_IN_PEAKS'),
                   model_uri=HTAN.scATACLevel3and4__PERCENTAGE_READS_IN_PEAKS, domain=None, range=float)

slots.scATACLevel3and4__SEURAT_CLUSTERS = Slot(uri=HTAN.SEURAT_CLUSTERS, name="scATACLevel3and4__SEURAT_CLUSTERS", curie=HTAN.curie('SEURAT_CLUSTERS'),
                   model_uri=HTAN.scATACLevel3and4__SEURAT_CLUSTERS, domain=None, range=Optional[Union[str, List[str]]])

slots.scATACLevel3and4__N_COUNT_RNA = Slot(uri=HTAN.N_COUNT_RNA, name="scATACLevel3and4__N_COUNT_RNA", curie=HTAN.curie('N_COUNT_RNA'),
                   model_uri=HTAN.scATACLevel3and4__N_COUNT_RNA, domain=None, range=Optional[int])

slots.scATACLevel3and4__N_FEATURE_RNA = Slot(uri=HTAN.N_FEATURE_RNA, name="scATACLevel3and4__N_FEATURE_RNA", curie=HTAN.curie('N_FEATURE_RNA'),
                   model_uri=HTAN.scATACLevel3and4__N_FEATURE_RNA, domain=None, range=Optional[int])

slots.scATACLevel3and4__PEAKS_CALLING_SOFTWARE = Slot(uri=HTAN.PEAKS_CALLING_SOFTWARE, name="scATACLevel3and4__PEAKS_CALLING_SOFTWARE", curie=HTAN.curie('PEAKS_CALLING_SOFTWARE'),
                   model_uri=HTAN.scATACLevel3and4__PEAKS_CALLING_SOFTWARE, domain=None, range=str)

slots.scATACLevel3and4__MEDIAN_FRACTION_OF_READS_IN_PEAKS = Slot(uri=HTAN.MEDIAN_FRACTION_OF_READS_IN_PEAKS, name="scATACLevel3and4__MEDIAN_FRACTION_OF_READS_IN_PEAKS", curie=HTAN.curie('MEDIAN_FRACTION_OF_READS_IN_PEAKS'),
                   model_uri=HTAN.scATACLevel3and4__MEDIAN_FRACTION_OF_READS_IN_PEAKS, domain=None, range=float)

slots.scATACLevel3and4__ATAC_GENE_ACTIVITY_WORKFLOW_TYPE = Slot(uri=HTAN.ATAC_GENE_ACTIVITY_WORKFLOW_TYPE, name="scATACLevel3and4__ATAC_GENE_ACTIVITY_WORKFLOW_TYPE", curie=HTAN.curie('ATAC_GENE_ACTIVITY_WORKFLOW_TYPE'),
                   model_uri=HTAN.scATACLevel3and4__ATAC_GENE_ACTIVITY_WORKFLOW_TYPE, domain=None, range=Union[str, "ATACGeneActivityWorkflowTypeEnum"])

slots.scATACLevel3and4__ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION = Slot(uri=HTAN.ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION, name="scATACLevel3and4__ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION", curie=HTAN.curie('ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION'),
                   model_uri=HTAN.scATACLevel3and4__ATAC_GENE_ACTIVITY_WORKFLOW_PARAMETERS_DESCRIPTION, domain=None, range=str)

slots.scATACLevel3and4__CELL_TOTAL = Slot(uri=HTAN.CELL_TOTAL, name="scATACLevel3and4__CELL_TOTAL", curie=HTAN.curie('CELL_TOTAL'),
                   model_uri=HTAN.scATACLevel3and4__CELL_TOTAL, domain=None, range=int)

slots.baseSequencingAttributes__CHECKSUM = Slot(uri=HTAN.CHECKSUM, name="baseSequencingAttributes__CHECKSUM", curie=HTAN.curie('CHECKSUM'),
                   model_uri=HTAN.baseSequencingAttributes__CHECKSUM, domain=None, range=Optional[str])

slots.baseSequencingLevel1Attributes__LIBRARY_LAYOUT = Slot(uri=HTAN.LIBRARY_LAYOUT, name="baseSequencingLevel1Attributes__LIBRARY_LAYOUT", curie=HTAN.curie('LIBRARY_LAYOUT'),
                   model_uri=HTAN.baseSequencingLevel1Attributes__LIBRARY_LAYOUT, domain=None, range=Union[str, "LibraryLayoutEnum"])

slots.baseSequencingLevel1Attributes__SEQUENCING_PLATFORM = Slot(uri=HTAN.SEQUENCING_PLATFORM, name="baseSequencingLevel1Attributes__SEQUENCING_PLATFORM", curie=HTAN.curie('SEQUENCING_PLATFORM'),
                   model_uri=HTAN.baseSequencingLevel1Attributes__SEQUENCING_PLATFORM, domain=None, range=Union[str, "SequencingPlatformEnum"])

slots.baseSequencingLevel1Attributes__SEQUENCING_BATCH_ID = Slot(uri=HTAN.SEQUENCING_BATCH_ID, name="baseSequencingLevel1Attributes__SEQUENCING_BATCH_ID", curie=HTAN.curie('SEQUENCING_BATCH_ID'),
                   model_uri=HTAN.baseSequencingLevel1Attributes__SEQUENCING_BATCH_ID, domain=None, range=Optional[str])

slots.baseSequencingLevel1Attributes__LIBRARY_PREPARATION_DAYS_FROM_INDEX = Slot(uri=HTAN.LIBRARY_PREPARATION_DAYS_FROM_INDEX, name="baseSequencingLevel1Attributes__LIBRARY_PREPARATION_DAYS_FROM_INDEX", curie=HTAN.curie('LIBRARY_PREPARATION_DAYS_FROM_INDEX'),
                   model_uri=HTAN.baseSequencingLevel1Attributes__LIBRARY_PREPARATION_DAYS_FROM_INDEX, domain=None, range=Optional[int])

slots.baseSequencingLevel1Attributes__TECHNICAL_REPLICATE_GROUP = Slot(uri=HTAN.TECHNICAL_REPLICATE_GROUP, name="baseSequencingLevel1Attributes__TECHNICAL_REPLICATE_GROUP", curie=HTAN.curie('TECHNICAL_REPLICATE_GROUP'),
                   model_uri=HTAN.baseSequencingLevel1Attributes__TECHNICAL_REPLICATE_GROUP, domain=None, range=Optional[str])

slots.baseSequencingLevel1Attributes__PROTOCOL_LINK = Slot(uri=HTAN.PROTOCOL_LINK, name="baseSequencingLevel1Attributes__PROTOCOL_LINK", curie=HTAN.curie('PROTOCOL_LINK'),
                   model_uri=HTAN.baseSequencingLevel1Attributes__PROTOCOL_LINK, domain=None, range=Optional[str])

slots.baseSequencingLevel2Attributes__GENOMIC_REFERENCE = Slot(uri=HTAN.GENOMIC_REFERENCE, name="baseSequencingLevel2Attributes__GENOMIC_REFERENCE", curie=HTAN.curie('GENOMIC_REFERENCE'),
                   model_uri=HTAN.baseSequencingLevel2Attributes__GENOMIC_REFERENCE, domain=None, range=Union[str, "GenomicReferenceEnum"])

slots.baseSequencingLevel2Attributes__GENOMIC_REFERENCE_URL = Slot(uri=HTAN.GENOMIC_REFERENCE_URL, name="baseSequencingLevel2Attributes__GENOMIC_REFERENCE_URL", curie=HTAN.curie('GENOMIC_REFERENCE_URL'),
                   model_uri=HTAN.baseSequencingLevel2Attributes__GENOMIC_REFERENCE_URL, domain=None, range=str)

slots.baseSequencingLevel2Attributes__GENOME_ANNOTATION_URL = Slot(uri=HTAN.GENOME_ANNOTATION_URL, name="baseSequencingLevel2Attributes__GENOME_ANNOTATION_URL", curie=HTAN.curie('GENOME_ANNOTATION_URL'),
                   model_uri=HTAN.baseSequencingLevel2Attributes__GENOME_ANNOTATION_URL, domain=None, range=str)

slots.baseSequencingLevel2Attributes__WORKFLOW_VERSION = Slot(uri=HTAN.WORKFLOW_VERSION, name="baseSequencingLevel2Attributes__WORKFLOW_VERSION", curie=HTAN.curie('WORKFLOW_VERSION'),
                   model_uri=HTAN.baseSequencingLevel2Attributes__WORKFLOW_VERSION, domain=None, range=str)

slots.baseSequencingLevel2Attributes__WORKFLOW_LINK = Slot(uri=HTAN.WORKFLOW_LINK, name="baseSequencingLevel2Attributes__WORKFLOW_LINK", curie=HTAN.curie('WORKFLOW_LINK'),
                   model_uri=HTAN.baseSequencingLevel2Attributes__WORKFLOW_LINK, domain=None, range=str)

slots.singleCellLevel1Attributes__SINGLE_CELL_ISOLATION_METHOD = Slot(uri=HTAN.SINGLE_CELL_ISOLATION_METHOD, name="singleCellLevel1Attributes__SINGLE_CELL_ISOLATION_METHOD", curie=HTAN.curie('SINGLE_CELL_ISOLATION_METHOD'),
                   model_uri=HTAN.singleCellLevel1Attributes__SINGLE_CELL_ISOLATION_METHOD, domain=None, range=Union[str, "SingleCellIsolationMethodEnum"])

slots.singleCellLevel1Attributes__DISSOCIATION_METHOD = Slot(uri=HTAN.DISSOCIATION_METHOD, name="singleCellLevel1Attributes__DISSOCIATION_METHOD", curie=HTAN.curie('DISSOCIATION_METHOD'),
                   model_uri=HTAN.singleCellLevel1Attributes__DISSOCIATION_METHOD, domain=None, range=Union[str, "DissociationMethodEnum"])

slots.singleCellLevel1Attributes__CRYOPRESERVED_CELLS_IN_SAMPLE = Slot(uri=HTAN.CRYOPRESERVED_CELLS_IN_SAMPLE, name="singleCellLevel1Attributes__CRYOPRESERVED_CELLS_IN_SAMPLE", curie=HTAN.curie('CRYOPRESERVED_CELLS_IN_SAMPLE'),
                   model_uri=HTAN.singleCellLevel1Attributes__CRYOPRESERVED_CELLS_IN_SAMPLE, domain=None, range=Optional[Union[bool, Bool]])

slots.singleCellLevel1Attributes__NUCLEIC_ACID_SOURCE = Slot(uri=HTAN.NUCLEIC_ACID_SOURCE, name="singleCellLevel1Attributes__NUCLEIC_ACID_SOURCE", curie=HTAN.curie('NUCLEIC_ACID_SOURCE'),
                   model_uri=HTAN.singleCellLevel1Attributes__NUCLEIC_ACID_SOURCE, domain=None, range=Union[str, "NucleicAcidSourceEnum"])

slots.singleCellLevel1Attributes__LIBRARY_CONSTRUCTION_METHOD = Slot(uri=HTAN.LIBRARY_CONSTRUCTION_METHOD, name="singleCellLevel1Attributes__LIBRARY_CONSTRUCTION_METHOD", curie=HTAN.curie('LIBRARY_CONSTRUCTION_METHOD'),
                   model_uri=HTAN.singleCellLevel1Attributes__LIBRARY_CONSTRUCTION_METHOD, domain=None, range=Union[str, "LibraryConstructionMethodEnum"])

slots.annDataComplianceMixin__ANNDATA_SCHEMA_VERSION = Slot(uri=HTAN.ANNDATA_SCHEMA_VERSION, name="annDataComplianceMixin__ANNDATA_SCHEMA_VERSION", curie=HTAN.curie('ANNDATA_SCHEMA_VERSION'),
                   model_uri=HTAN.annDataComplianceMixin__ANNDATA_SCHEMA_VERSION, domain=None, range=str,
                   pattern=re.compile(r'^0\.1$'))

slots.annDataComplianceMixin__ANNDATA_STRUCTURE_VALIDATED = Slot(uri=HTAN.ANNDATA_STRUCTURE_VALIDATED, name="annDataComplianceMixin__ANNDATA_STRUCTURE_VALIDATED", curie=HTAN.curie('ANNDATA_STRUCTURE_VALIDATED'),
                   model_uri=HTAN.annDataComplianceMixin__ANNDATA_STRUCTURE_VALIDATED, domain=None, range=Union[bool, Bool])

slots.coreFileAttributes__FILENAME = Slot(uri=HTAN.FILENAME, name="coreFileAttributes__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.coreFileAttributes__FILENAME, domain=None, range=str)

slots.coreFileAttributes__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="coreFileAttributes__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.coreFileAttributes__FILE_FORMAT, domain=None, range=str)

slots.coreFileAttributes__HTAN_DATA_FILE_ID = Slot(uri=HTAN.HTAN_DATA_FILE_ID, name="coreFileAttributes__HTAN_DATA_FILE_ID", curie=HTAN.curie('HTAN_DATA_FILE_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_DATA_FILE_ID, domain=None, range=URIRef,
                   pattern=re.compile(r'^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$'))

slots.coreFileAttributes__HTAN_PARENT_ID = Slot(uri=HTAN.HTAN_PARENT_ID, name="coreFileAttributes__HTAN_PARENT_ID", curie=HTAN.curie('HTAN_PARENT_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_PARENT_ID, domain=None, range=Union[str, List[str]],
                   pattern=re.compile(r'^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_([BD][0-9]{1,20})$'))
