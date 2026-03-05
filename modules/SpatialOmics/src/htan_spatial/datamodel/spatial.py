# Auto generated from spatial.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-05T16:28:39
# Schema: SpatialOmics
#
# id: https://w3id.org/htan/spatial
# description: HTAN Spatial Omics Data Model Schema for Phase 2 - All Levels
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
HTAN = CurieNamespace('htan', 'https://w3id.org/htan/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN


# Types

# Class references
class CoreFileAttributesHTANDATAFILEID(extended_str):
    pass


class SpatialLevel1HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class SpatialLevel3HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class SpatialLevel4HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class SpatialPanelHTANPANELID(extended_str):
    pass


@dataclass(repr=False)
class SpatialData(YAMLRoot):
    """
    Container for all Spatial Omics data levels
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["SpatialData"]
    class_class_curie: ClassVar[str] = "htan:SpatialData"
    class_name: ClassVar[str] = "SpatialData"
    class_model_uri: ClassVar[URIRef] = HTAN.SpatialData

    LEVEL_3_DATA: Union[str, SpatialLevel3HTANDATAFILEID] = None
    LEVEL_1_DATA: Optional[Union[str, SpatialLevel1HTANDATAFILEID]] = None
    LEVEL_4_DATA: Optional[Union[str, SpatialLevel4HTANDATAFILEID]] = None
    PANEL_DATA: Optional[Union[Union[str, SpatialPanelHTANPANELID], List[Union[str, SpatialPanelHTANPANELID]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.LEVEL_3_DATA):
            self.MissingRequiredField("LEVEL_3_DATA")
        if not isinstance(self.LEVEL_3_DATA, SpatialLevel3HTANDATAFILEID):
            self.LEVEL_3_DATA = SpatialLevel3HTANDATAFILEID(self.LEVEL_3_DATA)

        if self.LEVEL_1_DATA is not None and not isinstance(self.LEVEL_1_DATA, SpatialLevel1HTANDATAFILEID):
            self.LEVEL_1_DATA = SpatialLevel1HTANDATAFILEID(self.LEVEL_1_DATA)

        if self.LEVEL_4_DATA is not None and not isinstance(self.LEVEL_4_DATA, SpatialLevel4HTANDATAFILEID):
            self.LEVEL_4_DATA = SpatialLevel4HTANDATAFILEID(self.LEVEL_4_DATA)

        if not isinstance(self.PANEL_DATA, list):
            self.PANEL_DATA = [self.PANEL_DATA] if self.PANEL_DATA is not None else []
        self.PANEL_DATA = [v if isinstance(v, SpatialPanelHTANPANELID) else SpatialPanelHTANPANELID(v) for v in self.PANEL_DATA]

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
class SpatialLevel1(CoreFileAttributes):
    """
    Level 1 raw spatial data bundle (optional) - Contains raw sequencing data, images, and registration files
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["SpatialLevel1"]
    class_class_curie: ClassVar[str] = "htan:SpatialLevel1"
    class_name: ClassVar[str] = "SpatialLevel1"
    class_model_uri: ClassVar[URIRef] = HTAN.SpatialLevel1

    HTAN_DATA_FILE_ID: Union[str, SpatialLevel1HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    FILE_FORMAT: Union[str, "FileFormatLevel1"] = None
    FILENAME: str = None
    PLATFORM: Union[str, "Platform"] = None
    ASSAY_TYPE: Union[str, "AssayType"] = None
    BUNDLE_CONTENTS: Union[str, List[str]] = None
    HAS_IMAGES: Union[bool, Bool] = None
    HAS_REGISTRATION_FILES: Union[bool, Bool] = None
    HAS_SEQUENCING: Optional[Union[bool, Bool]] = None
    SEQUENCING_FILE_TYPE: Optional[Union[Union[str, "SequencingFileType"], List[Union[str, "SequencingFileType"]]]] = empty_list()
    IMAGE_TYPES: Optional[Union[Union[str, "ImageType"], List[Union[str, "ImageType"]]]] = empty_list()
    HAS_PROBE_SET: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, SpatialLevel1HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = SpatialLevel1HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, FileFormatLevel1):
            self.FILE_FORMAT = FileFormatLevel1(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.PLATFORM):
            self.MissingRequiredField("PLATFORM")
        if not isinstance(self.PLATFORM, Platform):
            self.PLATFORM = Platform(self.PLATFORM)

        if self._is_empty(self.ASSAY_TYPE):
            self.MissingRequiredField("ASSAY_TYPE")
        if not isinstance(self.ASSAY_TYPE, AssayType):
            self.ASSAY_TYPE = AssayType(self.ASSAY_TYPE)

        if self._is_empty(self.BUNDLE_CONTENTS):
            self.MissingRequiredField("BUNDLE_CONTENTS")
        if not isinstance(self.BUNDLE_CONTENTS, list):
            self.BUNDLE_CONTENTS = [self.BUNDLE_CONTENTS] if self.BUNDLE_CONTENTS is not None else []
        self.BUNDLE_CONTENTS = [v if isinstance(v, str) else str(v) for v in self.BUNDLE_CONTENTS]

        if self._is_empty(self.HAS_IMAGES):
            self.MissingRequiredField("HAS_IMAGES")
        if not isinstance(self.HAS_IMAGES, Bool):
            self.HAS_IMAGES = Bool(self.HAS_IMAGES)

        if self._is_empty(self.HAS_REGISTRATION_FILES):
            self.MissingRequiredField("HAS_REGISTRATION_FILES")
        if not isinstance(self.HAS_REGISTRATION_FILES, Bool):
            self.HAS_REGISTRATION_FILES = Bool(self.HAS_REGISTRATION_FILES)

        if self.HAS_SEQUENCING is not None and not isinstance(self.HAS_SEQUENCING, Bool):
            self.HAS_SEQUENCING = Bool(self.HAS_SEQUENCING)

        if not isinstance(self.SEQUENCING_FILE_TYPE, list):
            self.SEQUENCING_FILE_TYPE = [self.SEQUENCING_FILE_TYPE] if self.SEQUENCING_FILE_TYPE is not None else []
        self.SEQUENCING_FILE_TYPE = [v if isinstance(v, SequencingFileType) else SequencingFileType(v) for v in self.SEQUENCING_FILE_TYPE]

        if not isinstance(self.IMAGE_TYPES, list):
            self.IMAGE_TYPES = [self.IMAGE_TYPES] if self.IMAGE_TYPES is not None else []
        self.IMAGE_TYPES = [v if isinstance(v, ImageType) else ImageType(v) for v in self.IMAGE_TYPES]

        if self.HAS_PROBE_SET is not None and not isinstance(self.HAS_PROBE_SET, Bool):
            self.HAS_PROBE_SET = Bool(self.HAS_PROBE_SET)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpatialLevel3(CoreFileAttributes):
    """
    Level 3 processed spatial assay output bundle - Contains platform-specific output files, segmentation, matrices,
    and QC metrics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["SpatialLevel3"]
    class_class_curie: ClassVar[str] = "htan:SpatialLevel3"
    class_name: ClassVar[str] = "SpatialLevel3"
    class_model_uri: ClassVar[URIRef] = HTAN.SpatialLevel3

    HTAN_DATA_FILE_ID: Union[str, SpatialLevel3HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    PLATFORM: Union[str, "PlatformLevel3"] = None
    ASSAY_CHEMISTRY_VERSION: str = None
    RNA_MEASURED: Union[bool, Bool] = None
    PROTEIN_MEASURED: Union[bool, Bool] = None
    PANEL_SIZE_TOTAL_TARGETS: int = None
    REGION_AREA: float = None
    BUNDLE_CONTENTS: Union[str, List[str]] = None
    HAS_CELL_SEGMENTATION: Union[bool, Bool] = None
    HAS_CLUSTERING: Union[bool, Bool] = None
    QC_SPATIAL_UNIT: Union[str, "QCSpatialUnit"] = None
    QC_FEATURE_NUMBER: int = None
    QC_MEAN_READS_PER_FEATURE: float = None
    QC_TOTAL_GENES_DETECTED: int = None
    QC_TOTAL_NUMBER_OF_READS: int = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    SPATIAL_ASSAY_TYPE: Optional[Union[str, "SpatialAssayType"]] = None
    SOFTWARE_AND_VERSION: Optional[str] = None
    PROTOCOL_LINK: Optional[str] = None
    TRANSCRIPTOME_TYPE: Optional[Union[str, "TranscriptomeType"]] = None
    PANEL_NAME: Optional[str] = None
    PANEL_SYNAPSE_ID: Optional[str] = None
    SAME_SECTION_IMAGING_ID: Optional[Union[str, List[str]]] = empty_list()
    SAME_SECTION_IMAGING_MODALITY: Optional[Union[str, "SameSectionImagingModality"]] = None
    SAME_SECTION_IMAGING_CHANNELS: Optional[Union[str, List[str]]] = empty_list()
    PORTAL_PREVIEW_FILE: Optional[str] = None
    CELL_SEGMENTATION_METHOD: Optional[str] = None
    CELL_SEGMENTED_OBJECT_TYPE: Optional[Union[str, "CellSegmentedObjectType"]] = None
    NUMBER_OF_SEGMENTED_CELLS: Optional[int] = None
    HAS_DIMENSIONALITY_REDUCTION: Optional[Union[bool, Bool]] = None
    DIMENSIONALITY_REDUCTION_METHOD: Optional[Union[str, "DimensionalityReductionMethod"]] = None
    CLUSTERING_METHOD: Optional[str] = None
    NUMBER_OF_CLUSTERS: Optional[int] = None
    SLIDE_SERIAL_NUMBER: Optional[str] = None
    CAPTURE_AREA: Optional[Union[str, "CaptureArea"]] = None
    RUN_ID: Optional[str] = None
    CYTASSIST_USED: Optional[Union[bool, Bool]] = None
    GENOMIC_REFERENCE: Optional[str] = None
    SEQUENCING_INSTRUMENT: Optional[str] = None
    SEQUENCING_CONFIGURATION: Optional[str] = None
    SEQUENCING_DEPTH: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, SpatialLevel3HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = SpatialLevel3HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.PLATFORM):
            self.MissingRequiredField("PLATFORM")
        if not isinstance(self.PLATFORM, PlatformLevel3):
            self.PLATFORM = PlatformLevel3(self.PLATFORM)

        if self._is_empty(self.ASSAY_CHEMISTRY_VERSION):
            self.MissingRequiredField("ASSAY_CHEMISTRY_VERSION")
        if not isinstance(self.ASSAY_CHEMISTRY_VERSION, str):
            self.ASSAY_CHEMISTRY_VERSION = str(self.ASSAY_CHEMISTRY_VERSION)

        if self._is_empty(self.RNA_MEASURED):
            self.MissingRequiredField("RNA_MEASURED")
        if not isinstance(self.RNA_MEASURED, Bool):
            self.RNA_MEASURED = Bool(self.RNA_MEASURED)

        if self._is_empty(self.PROTEIN_MEASURED):
            self.MissingRequiredField("PROTEIN_MEASURED")
        if not isinstance(self.PROTEIN_MEASURED, Bool):
            self.PROTEIN_MEASURED = Bool(self.PROTEIN_MEASURED)

        if self._is_empty(self.PANEL_SIZE_TOTAL_TARGETS):
            self.MissingRequiredField("PANEL_SIZE_TOTAL_TARGETS")
        if not isinstance(self.PANEL_SIZE_TOTAL_TARGETS, int):
            self.PANEL_SIZE_TOTAL_TARGETS = int(self.PANEL_SIZE_TOTAL_TARGETS)

        if self._is_empty(self.REGION_AREA):
            self.MissingRequiredField("REGION_AREA")
        if not isinstance(self.REGION_AREA, float):
            self.REGION_AREA = float(self.REGION_AREA)

        if self._is_empty(self.BUNDLE_CONTENTS):
            self.MissingRequiredField("BUNDLE_CONTENTS")
        if not isinstance(self.BUNDLE_CONTENTS, list):
            self.BUNDLE_CONTENTS = [self.BUNDLE_CONTENTS] if self.BUNDLE_CONTENTS is not None else []
        self.BUNDLE_CONTENTS = [v if isinstance(v, str) else str(v) for v in self.BUNDLE_CONTENTS]

        if self._is_empty(self.HAS_CELL_SEGMENTATION):
            self.MissingRequiredField("HAS_CELL_SEGMENTATION")
        if not isinstance(self.HAS_CELL_SEGMENTATION, Bool):
            self.HAS_CELL_SEGMENTATION = Bool(self.HAS_CELL_SEGMENTATION)

        if self._is_empty(self.HAS_CLUSTERING):
            self.MissingRequiredField("HAS_CLUSTERING")
        if not isinstance(self.HAS_CLUSTERING, Bool):
            self.HAS_CLUSTERING = Bool(self.HAS_CLUSTERING)

        if self._is_empty(self.QC_SPATIAL_UNIT):
            self.MissingRequiredField("QC_SPATIAL_UNIT")
        if not isinstance(self.QC_SPATIAL_UNIT, QCSpatialUnit):
            self.QC_SPATIAL_UNIT = QCSpatialUnit(self.QC_SPATIAL_UNIT)

        if self._is_empty(self.QC_FEATURE_NUMBER):
            self.MissingRequiredField("QC_FEATURE_NUMBER")
        if not isinstance(self.QC_FEATURE_NUMBER, int):
            self.QC_FEATURE_NUMBER = int(self.QC_FEATURE_NUMBER)

        if self._is_empty(self.QC_MEAN_READS_PER_FEATURE):
            self.MissingRequiredField("QC_MEAN_READS_PER_FEATURE")
        if not isinstance(self.QC_MEAN_READS_PER_FEATURE, float):
            self.QC_MEAN_READS_PER_FEATURE = float(self.QC_MEAN_READS_PER_FEATURE)

        if self._is_empty(self.QC_TOTAL_GENES_DETECTED):
            self.MissingRequiredField("QC_TOTAL_GENES_DETECTED")
        if not isinstance(self.QC_TOTAL_GENES_DETECTED, int):
            self.QC_TOTAL_GENES_DETECTED = int(self.QC_TOTAL_GENES_DETECTED)

        if self._is_empty(self.QC_TOTAL_NUMBER_OF_READS):
            self.MissingRequiredField("QC_TOTAL_NUMBER_OF_READS")
        if not isinstance(self.QC_TOTAL_NUMBER_OF_READS, int):
            self.QC_TOTAL_NUMBER_OF_READS = int(self.QC_TOTAL_NUMBER_OF_READS)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self.SPATIAL_ASSAY_TYPE is not None and not isinstance(self.SPATIAL_ASSAY_TYPE, SpatialAssayType):
            self.SPATIAL_ASSAY_TYPE = SpatialAssayType(self.SPATIAL_ASSAY_TYPE)

        if self.SOFTWARE_AND_VERSION is not None and not isinstance(self.SOFTWARE_AND_VERSION, str):
            self.SOFTWARE_AND_VERSION = str(self.SOFTWARE_AND_VERSION)

        if self.PROTOCOL_LINK is not None and not isinstance(self.PROTOCOL_LINK, str):
            self.PROTOCOL_LINK = str(self.PROTOCOL_LINK)

        if self.TRANSCRIPTOME_TYPE is not None and not isinstance(self.TRANSCRIPTOME_TYPE, TranscriptomeType):
            self.TRANSCRIPTOME_TYPE = TranscriptomeType(self.TRANSCRIPTOME_TYPE)

        if self.PANEL_NAME is not None and not isinstance(self.PANEL_NAME, str):
            self.PANEL_NAME = str(self.PANEL_NAME)

        if self.PANEL_SYNAPSE_ID is not None and not isinstance(self.PANEL_SYNAPSE_ID, str):
            self.PANEL_SYNAPSE_ID = str(self.PANEL_SYNAPSE_ID)

        if not isinstance(self.SAME_SECTION_IMAGING_ID, list):
            self.SAME_SECTION_IMAGING_ID = [self.SAME_SECTION_IMAGING_ID] if self.SAME_SECTION_IMAGING_ID is not None else []
        self.SAME_SECTION_IMAGING_ID = [v if isinstance(v, str) else str(v) for v in self.SAME_SECTION_IMAGING_ID]

        if self.SAME_SECTION_IMAGING_MODALITY is not None and not isinstance(self.SAME_SECTION_IMAGING_MODALITY, SameSectionImagingModality):
            self.SAME_SECTION_IMAGING_MODALITY = SameSectionImagingModality(self.SAME_SECTION_IMAGING_MODALITY)

        if not isinstance(self.SAME_SECTION_IMAGING_CHANNELS, list):
            self.SAME_SECTION_IMAGING_CHANNELS = [self.SAME_SECTION_IMAGING_CHANNELS] if self.SAME_SECTION_IMAGING_CHANNELS is not None else []
        self.SAME_SECTION_IMAGING_CHANNELS = [v if isinstance(v, str) else str(v) for v in self.SAME_SECTION_IMAGING_CHANNELS]

        if self.PORTAL_PREVIEW_FILE is not None and not isinstance(self.PORTAL_PREVIEW_FILE, str):
            self.PORTAL_PREVIEW_FILE = str(self.PORTAL_PREVIEW_FILE)

        if self.CELL_SEGMENTATION_METHOD is not None and not isinstance(self.CELL_SEGMENTATION_METHOD, str):
            self.CELL_SEGMENTATION_METHOD = str(self.CELL_SEGMENTATION_METHOD)

        if self.CELL_SEGMENTED_OBJECT_TYPE is not None and not isinstance(self.CELL_SEGMENTED_OBJECT_TYPE, CellSegmentedObjectType):
            self.CELL_SEGMENTED_OBJECT_TYPE = CellSegmentedObjectType(self.CELL_SEGMENTED_OBJECT_TYPE)

        if self.NUMBER_OF_SEGMENTED_CELLS is not None and not isinstance(self.NUMBER_OF_SEGMENTED_CELLS, int):
            self.NUMBER_OF_SEGMENTED_CELLS = int(self.NUMBER_OF_SEGMENTED_CELLS)

        if self.HAS_DIMENSIONALITY_REDUCTION is not None and not isinstance(self.HAS_DIMENSIONALITY_REDUCTION, Bool):
            self.HAS_DIMENSIONALITY_REDUCTION = Bool(self.HAS_DIMENSIONALITY_REDUCTION)

        if self.DIMENSIONALITY_REDUCTION_METHOD is not None and not isinstance(self.DIMENSIONALITY_REDUCTION_METHOD, DimensionalityReductionMethod):
            self.DIMENSIONALITY_REDUCTION_METHOD = DimensionalityReductionMethod(self.DIMENSIONALITY_REDUCTION_METHOD)

        if self.CLUSTERING_METHOD is not None and not isinstance(self.CLUSTERING_METHOD, str):
            self.CLUSTERING_METHOD = str(self.CLUSTERING_METHOD)

        if self.NUMBER_OF_CLUSTERS is not None and not isinstance(self.NUMBER_OF_CLUSTERS, int):
            self.NUMBER_OF_CLUSTERS = int(self.NUMBER_OF_CLUSTERS)

        if self.SLIDE_SERIAL_NUMBER is not None and not isinstance(self.SLIDE_SERIAL_NUMBER, str):
            self.SLIDE_SERIAL_NUMBER = str(self.SLIDE_SERIAL_NUMBER)

        if self.CAPTURE_AREA is not None and not isinstance(self.CAPTURE_AREA, CaptureArea):
            self.CAPTURE_AREA = CaptureArea(self.CAPTURE_AREA)

        if self.RUN_ID is not None and not isinstance(self.RUN_ID, str):
            self.RUN_ID = str(self.RUN_ID)

        if self.CYTASSIST_USED is not None and not isinstance(self.CYTASSIST_USED, Bool):
            self.CYTASSIST_USED = Bool(self.CYTASSIST_USED)

        if self.GENOMIC_REFERENCE is not None and not isinstance(self.GENOMIC_REFERENCE, str):
            self.GENOMIC_REFERENCE = str(self.GENOMIC_REFERENCE)

        if self.SEQUENCING_INSTRUMENT is not None and not isinstance(self.SEQUENCING_INSTRUMENT, str):
            self.SEQUENCING_INSTRUMENT = str(self.SEQUENCING_INSTRUMENT)

        if self.SEQUENCING_CONFIGURATION is not None and not isinstance(self.SEQUENCING_CONFIGURATION, str):
            self.SEQUENCING_CONFIGURATION = str(self.SEQUENCING_CONFIGURATION)

        if self.SEQUENCING_DEPTH is not None and not isinstance(self.SEQUENCING_DEPTH, str):
            self.SEQUENCING_DEPTH = str(self.SEQUENCING_DEPTH)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpatialLevel4(CoreFileAttributes):
    """
    Level 4 interoperable spatial omics file (optional) - Harmonized h5ad, RDS, or Zarr file for downstream analysis
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["SpatialLevel4"]
    class_class_curie: ClassVar[str] = "htan:SpatialLevel4"
    class_name: ClassVar[str] = "SpatialLevel4"
    class_model_uri: ClassVar[URIRef] = HTAN.SpatialLevel4

    HTAN_DATA_FILE_ID: Union[str, SpatialLevel4HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    FILE_FORMAT: Union[str, "FileFormatLevel4"] = None
    FILENAME: str = None
    NUMBER_OF_FEATURES: int = None
    NUMBER_OF_OBJECTS: int = None
    HAS_DIMENSIONALITY_REDUCTION: Union[bool, Bool] = None
    HAS_CLUSTERING: Union[bool, Bool] = None
    HAS_CELL_TYPE_CALLING: Union[bool, Bool] = None
    HAS_NORMALISED_ARRAY: Union[bool, Bool] = None
    HAS_RAW_ARRAY: Union[bool, Bool] = None
    HAS_IMAGE: Union[bool, Bool] = None
    TOOL_COMPATIBILITY: Optional[Union[Union[str, "ToolCompatibility"], List[Union[str, "ToolCompatibility"]]]] = empty_list()
    DIMENSIONALITY_REDUCTION_METHOD: Optional[Union[str, "DimensionalityReductionMethodLevel4"]] = None
    CLUSTERING_METHOD: Optional[str] = None
    NUMBER_OF_CLUSTERS: Optional[int] = None
    CELL_TYPE_CALLING_METHOD: Optional[str] = None
    CELL_TYPES: Optional[Union[str, List[str]]] = empty_list()
    NORMALISATION_METHOD: Optional[Union[str, "NormalisationMethod"]] = None
    IMAGE_TYPE: Optional[Union[str, "ImageTypeLevel4"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, SpatialLevel4HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = SpatialLevel4HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, FileFormatLevel4):
            self.FILE_FORMAT = FileFormatLevel4(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.NUMBER_OF_FEATURES):
            self.MissingRequiredField("NUMBER_OF_FEATURES")
        if not isinstance(self.NUMBER_OF_FEATURES, int):
            self.NUMBER_OF_FEATURES = int(self.NUMBER_OF_FEATURES)

        if self._is_empty(self.NUMBER_OF_OBJECTS):
            self.MissingRequiredField("NUMBER_OF_OBJECTS")
        if not isinstance(self.NUMBER_OF_OBJECTS, int):
            self.NUMBER_OF_OBJECTS = int(self.NUMBER_OF_OBJECTS)

        if self._is_empty(self.HAS_DIMENSIONALITY_REDUCTION):
            self.MissingRequiredField("HAS_DIMENSIONALITY_REDUCTION")
        if not isinstance(self.HAS_DIMENSIONALITY_REDUCTION, Bool):
            self.HAS_DIMENSIONALITY_REDUCTION = Bool(self.HAS_DIMENSIONALITY_REDUCTION)

        if self._is_empty(self.HAS_CLUSTERING):
            self.MissingRequiredField("HAS_CLUSTERING")
        if not isinstance(self.HAS_CLUSTERING, Bool):
            self.HAS_CLUSTERING = Bool(self.HAS_CLUSTERING)

        if self._is_empty(self.HAS_CELL_TYPE_CALLING):
            self.MissingRequiredField("HAS_CELL_TYPE_CALLING")
        if not isinstance(self.HAS_CELL_TYPE_CALLING, Bool):
            self.HAS_CELL_TYPE_CALLING = Bool(self.HAS_CELL_TYPE_CALLING)

        if self._is_empty(self.HAS_NORMALISED_ARRAY):
            self.MissingRequiredField("HAS_NORMALISED_ARRAY")
        if not isinstance(self.HAS_NORMALISED_ARRAY, Bool):
            self.HAS_NORMALISED_ARRAY = Bool(self.HAS_NORMALISED_ARRAY)

        if self._is_empty(self.HAS_RAW_ARRAY):
            self.MissingRequiredField("HAS_RAW_ARRAY")
        if not isinstance(self.HAS_RAW_ARRAY, Bool):
            self.HAS_RAW_ARRAY = Bool(self.HAS_RAW_ARRAY)

        if self._is_empty(self.HAS_IMAGE):
            self.MissingRequiredField("HAS_IMAGE")
        if not isinstance(self.HAS_IMAGE, Bool):
            self.HAS_IMAGE = Bool(self.HAS_IMAGE)

        if not isinstance(self.TOOL_COMPATIBILITY, list):
            self.TOOL_COMPATIBILITY = [self.TOOL_COMPATIBILITY] if self.TOOL_COMPATIBILITY is not None else []
        self.TOOL_COMPATIBILITY = [v if isinstance(v, ToolCompatibility) else ToolCompatibility(v) for v in self.TOOL_COMPATIBILITY]

        if self.DIMENSIONALITY_REDUCTION_METHOD is not None and not isinstance(self.DIMENSIONALITY_REDUCTION_METHOD, DimensionalityReductionMethodLevel4):
            self.DIMENSIONALITY_REDUCTION_METHOD = DimensionalityReductionMethodLevel4(self.DIMENSIONALITY_REDUCTION_METHOD)

        if self.CLUSTERING_METHOD is not None and not isinstance(self.CLUSTERING_METHOD, str):
            self.CLUSTERING_METHOD = str(self.CLUSTERING_METHOD)

        if self.NUMBER_OF_CLUSTERS is not None and not isinstance(self.NUMBER_OF_CLUSTERS, int):
            self.NUMBER_OF_CLUSTERS = int(self.NUMBER_OF_CLUSTERS)

        if self.CELL_TYPE_CALLING_METHOD is not None and not isinstance(self.CELL_TYPE_CALLING_METHOD, str):
            self.CELL_TYPE_CALLING_METHOD = str(self.CELL_TYPE_CALLING_METHOD)

        if not isinstance(self.CELL_TYPES, list):
            self.CELL_TYPES = [self.CELL_TYPES] if self.CELL_TYPES is not None else []
        self.CELL_TYPES = [v if isinstance(v, str) else str(v) for v in self.CELL_TYPES]

        if self.NORMALISATION_METHOD is not None and not isinstance(self.NORMALISATION_METHOD, NormalisationMethod):
            self.NORMALISATION_METHOD = NormalisationMethod(self.NORMALISATION_METHOD)

        if self.IMAGE_TYPE is not None and not isinstance(self.IMAGE_TYPE, ImageTypeLevel4):
            self.IMAGE_TYPE = ImageTypeLevel4(self.IMAGE_TYPE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SpatialPanel(YAMLRoot):
    """
    Spatial omics panel information for targeted sequencing or protein panels
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["SpatialPanel"]
    class_class_curie: ClassVar[str] = "htan:SpatialPanel"
    class_name: ClassVar[str] = "SpatialPanel"
    class_model_uri: ClassVar[URIRef] = HTAN.SpatialPanel

    HTAN_PANEL_ID: Union[str, SpatialPanelHTANPANELID] = None
    GENE_SYMBOL: str = None
    HGNC_VERSION: str = None
    GENE_ID: str = None
    USER_GENE_NAME: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_PANEL_ID):
            self.MissingRequiredField("HTAN_PANEL_ID")
        if not isinstance(self.HTAN_PANEL_ID, SpatialPanelHTANPANELID):
            self.HTAN_PANEL_ID = SpatialPanelHTANPANELID(self.HTAN_PANEL_ID)

        if self._is_empty(self.GENE_SYMBOL):
            self.MissingRequiredField("GENE_SYMBOL")
        if not isinstance(self.GENE_SYMBOL, str):
            self.GENE_SYMBOL = str(self.GENE_SYMBOL)

        if self._is_empty(self.HGNC_VERSION):
            self.MissingRequiredField("HGNC_VERSION")
        if not isinstance(self.HGNC_VERSION, str):
            self.HGNC_VERSION = str(self.HGNC_VERSION)

        if self._is_empty(self.GENE_ID):
            self.MissingRequiredField("GENE_ID")
        if not isinstance(self.GENE_ID, str):
            self.GENE_ID = str(self.GENE_ID)

        if self.USER_GENE_NAME is not None and not isinstance(self.USER_GENE_NAME, str):
            self.USER_GENE_NAME = str(self.USER_GENE_NAME)

        super().__post_init__(**kwargs)


# Enumerations
class FileFormatLevel1(EnumDefinitionImpl):

    tar = PermissibleValue(
        text="tar",
        description="TAR archive format")
    zip = PermissibleValue(
        text="zip",
        description="ZIP compressed archive format")

    _defn = EnumDefinition(
        name="FileFormatLevel1",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "tar.gz",
            PermissibleValue(
                text="tar.gz",
                description="TAR GZIP compressed archive format"))

class Platform(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Platform",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10x Genomics Visium",
            PermissibleValue(
                text="10x Genomics Visium",
                description="10x Genomics Visium platform"))
        setattr(cls, "10x Genomics Visium HD",
            PermissibleValue(
                text="10x Genomics Visium HD",
                description="10x Genomics Visium HD platform"))
        setattr(cls, "10x Genomics Xenium",
            PermissibleValue(
                text="10x Genomics Xenium",
                description="10x Genomics Xenium platform"))
        setattr(cls, "Nanostring CosMX",
            PermissibleValue(
                text="Nanostring CosMX",
                description="Nanostring CosMX platform"))
        setattr(cls, "STOmics Stereo-CITE",
            PermissibleValue(
                text="STOmics Stereo-CITE",
                description="STOmics Stereo-CITE platform"))
        setattr(cls, "STOmics Stereo-seq",
            PermissibleValue(
                text="STOmics Stereo-seq",
                description="STOmics Stereo-seq platform"))

class AssayType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="AssayType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "in situ sequencing",
            PermissibleValue(
                text="in situ sequencing",
                description="In situ sequencing assay type"))
        setattr(cls, "molecular barcoding",
            PermissibleValue(
                text="molecular barcoding",
                description="Molecular barcoding assay type"))
        setattr(cls, "multi-omic sequencing",
            PermissibleValue(
                text="multi-omic sequencing",
                description="Multi-omic sequencing assay type"))
        setattr(cls, "spot-based sequencing",
            PermissibleValue(
                text="spot-based sequencing",
                description="Spot-based sequencing assay type"))

class SequencingFileType(EnumDefinitionImpl):

    BAM = PermissibleValue(
        text="BAM",
        description="BAM alignment file format")
    FASTQ = PermissibleValue(
        text="FASTQ",
        description="FASTQ sequencing file format")

    _defn = EnumDefinition(
        name="SequencingFileType",
    )

class ImageType(EnumDefinitionImpl):

    DAPI = PermissibleValue(
        text="DAPI",
        description="DAPI (4',6-diamidino-2-phenylindole) image type")
    MIF = PermissibleValue(
        text="MIF",
        description="Multiplex Immunofluorescence image type")
    Other = PermissibleValue(
        text="Other",
        description="Other image type")

    _defn = EnumDefinition(
        name="ImageType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "H&E",
            PermissibleValue(
                text="H&E",
                description="Hematoxylin and Eosin image type"))

class PlatformLevel3(EnumDefinitionImpl):

    SeqFISH = PermissibleValue(
        text="SeqFISH",
        description="SeqFISH platform")

    _defn = EnumDefinition(
        name="PlatformLevel3",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "10x Genomics Visium",
            PermissibleValue(
                text="10x Genomics Visium",
                description="10x Genomics Visium platform"))
        setattr(cls, "10x Genomics Visium HD",
            PermissibleValue(
                text="10x Genomics Visium HD",
                description="10x Genomics Visium HD platform"))
        setattr(cls, "10x Genomics Xenium",
            PermissibleValue(
                text="10x Genomics Xenium",
                description="10x Genomics Xenium platform"))
        setattr(cls, "DBiT-seq",
            PermissibleValue(
                text="DBiT-seq",
                description="DBiT-seq platform"))
        setattr(cls, "Nanostring CosMX",
            PermissibleValue(
                text="Nanostring CosMX",
                description="Nanostring CosMX platform"))
        setattr(cls, "STOmics Stereo-CITE",
            PermissibleValue(
                text="STOmics Stereo-CITE",
                description="STOmics Stereo-CITE platform"))
        setattr(cls, "STOmics Stereo-seq",
            PermissibleValue(
                text="STOmics Stereo-seq",
                description="STOmics Stereo-seq platform"))

class SpatialAssayType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="SpatialAssayType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "capture-based",
            PermissibleValue(
                text="capture-based",
                description="Capture-based spatial assay type"))
        setattr(cls, "In situ",
            PermissibleValue(
                text="In situ",
                description="In situ spatial assay type"))

class TranscriptomeType(EnumDefinitionImpl):

    Targeted = PermissibleValue(
        text="Targeted",
        description="Targeted transcriptome type")

    _defn = EnumDefinition(
        name="TranscriptomeType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Protein coding",
            PermissibleValue(
                text="Protein coding",
                description="Protein coding transcriptome type"))
        setattr(cls, "Whole transcriptome",
            PermissibleValue(
                text="Whole transcriptome",
                description="Whole transcriptome type"))

class SameSectionImagingModality(EnumDefinitionImpl):

    fluorescence = PermissibleValue(
        text="fluorescence",
        description="Fluorescence imaging modality")

    _defn = EnumDefinition(
        name="SameSectionImagingModality",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "H&E",
            PermissibleValue(
                text="H&E",
                description="Hematoxylin and Eosin imaging modality"))

class CellSegmentedObjectType(EnumDefinitionImpl):

    cytoplasm = PermissibleValue(
        text="cytoplasm",
        description="Cytoplasm segmentation object type")
    nucleus = PermissibleValue(
        text="nucleus",
        description="Nucleus segmentation object type")

    _defn = EnumDefinition(
        name="CellSegmentedObjectType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Whole cell",
            PermissibleValue(
                text="Whole cell",
                description="Whole cell segmentation object type"))

class DimensionalityReductionMethod(EnumDefinitionImpl):

    PCA = PermissibleValue(
        text="PCA",
        description="Principal Component Analysis")
    UMAP = PermissibleValue(
        text="UMAP",
        description="Uniform Manifold Approximation and Projection")
    other = PermissibleValue(
        text="other",
        description="Other dimensionality reduction method")

    _defn = EnumDefinition(
        name="DimensionalityReductionMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "t-SNE",
            PermissibleValue(
                text="t-SNE",
                description="t-Distributed Stochastic Neighbor Embedding"))

class CaptureArea(EnumDefinitionImpl):

    A = PermissibleValue(
        text="A",
        description="Capture area A (CytAssist slides with 11 mm Capture Area)")
    A1 = PermissibleValue(
        text="A1",
        description="""Capture area A1 (Visium slides v1 with 6.5 mm Capture Area, or CytAssist/Gateway slides with 6.5 mm Capture Area)""")
    B = PermissibleValue(
        text="B",
        description="Capture area B (CytAssist slides with 11 mm Capture Area)")
    B1 = PermissibleValue(
        text="B1",
        description="Capture area B1 (Visium slides v1 with 6.5 mm Capture Area)")
    C1 = PermissibleValue(
        text="C1",
        description="Capture area C1 (Visium slides v1 with 6.5 mm Capture Area)")
    D1 = PermissibleValue(
        text="D1",
        description="""Capture area D1 (Visium slides v1 with 6.5 mm Capture Area, or CytAssist/Gateway slides with 6.5 mm Capture Area)""")

    _defn = EnumDefinition(
        name="CaptureArea",
    )

class QCSpatialUnit(EnumDefinitionImpl):

    cell = PermissibleValue(
        text="cell",
        description="Cell spatial unit")
    spot = PermissibleValue(
        text="spot",
        description="Spot spatial unit")

    _defn = EnumDefinition(
        name="QCSpatialUnit",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "100um area",
            PermissibleValue(
                text="100um area",
                description="100 micrometer area spatial unit"))
        setattr(cls, "8um bin",
            PermissibleValue(
                text="8um bin",
                description="8 micrometer bin spatial unit"))

class FileFormatLevel4(EnumDefinitionImpl):

    h5ad = PermissibleValue(
        text="h5ad",
        description="AnnData HDF5 format (Python)")
    rds = PermissibleValue(
        text="rds",
        description="RDS format (R)")
    zarr = PermissibleValue(
        text="zarr",
        description="Zarr format")

    _defn = EnumDefinition(
        name="FileFormatLevel4",
    )

class ToolCompatibility(EnumDefinitionImpl):

    anndata = PermissibleValue(
        text="anndata",
        description="AnnData library compatibility")
    seurat = PermissibleValue(
        text="seurat",
        description="Seurat library compatibility")
    spatialdata = PermissibleValue(
        text="spatialdata",
        description="SpatialData library compatibility")

    _defn = EnumDefinition(
        name="ToolCompatibility",
    )

class DimensionalityReductionMethodLevel4(EnumDefinitionImpl):

    PCA = PermissibleValue(
        text="PCA",
        description="Principal Component Analysis")
    UMAP = PermissibleValue(
        text="UMAP",
        description="Uniform Manifold Approximation and Projection")
    other = PermissibleValue(
        text="other",
        description="Other dimensionality reduction method")

    _defn = EnumDefinition(
        name="DimensionalityReductionMethodLevel4",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "t-SNE",
            PermissibleValue(
                text="t-SNE",
                description="t-Distributed Stochastic Neighbor Embedding"))

class NormalisationMethod(EnumDefinitionImpl):

    CPM = PermissibleValue(
        text="CPM",
        description="Counts Per Million normalization")
    SCTransform = PermissibleValue(
        text="SCTransform",
        description="SCTransform normalization")
    TPM = PermissibleValue(
        text="TPM",
        description="Transcripts Per Million normalization")
    other = PermissibleValue(
        text="other",
        description="Other normalization method")

    _defn = EnumDefinition(
        name="NormalisationMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "log normalization",
            PermissibleValue(
                text="log normalization",
                description="Log normalization"))

class ImageTypeLevel4(EnumDefinitionImpl):

    jpeg = PermissibleValue(
        text="jpeg",
        description="JPEG image format")
    other = PermissibleValue(
        text="other",
        description="Other image format")
    png = PermissibleValue(
        text="png",
        description="PNG image format")
    tiff = PermissibleValue(
        text="tiff",
        description="TIFF image format")

    _defn = EnumDefinition(
        name="ImageTypeLevel4",
    )

# Slots
class slots:
    pass

slots.caDSR_id = Slot(uri=HTAN.caDSR_id, name="caDSR_id", curie=HTAN.curie('caDSR_id'),
                   model_uri=HTAN.caDSR_id, domain=None, range=Optional[str])

slots.spatialData__LEVEL_1_DATA = Slot(uri=HTAN.LEVEL_1_DATA, name="spatialData__LEVEL_1_DATA", curie=HTAN.curie('LEVEL_1_DATA'),
                   model_uri=HTAN.spatialData__LEVEL_1_DATA, domain=None, range=Optional[Union[str, SpatialLevel1HTANDATAFILEID]])

slots.spatialData__LEVEL_3_DATA = Slot(uri=HTAN.LEVEL_3_DATA, name="spatialData__LEVEL_3_DATA", curie=HTAN.curie('LEVEL_3_DATA'),
                   model_uri=HTAN.spatialData__LEVEL_3_DATA, domain=None, range=Union[str, SpatialLevel3HTANDATAFILEID])

slots.spatialData__LEVEL_4_DATA = Slot(uri=HTAN.LEVEL_4_DATA, name="spatialData__LEVEL_4_DATA", curie=HTAN.curie('LEVEL_4_DATA'),
                   model_uri=HTAN.spatialData__LEVEL_4_DATA, domain=None, range=Optional[Union[str, SpatialLevel4HTANDATAFILEID]])

slots.spatialData__PANEL_DATA = Slot(uri=HTAN.PANEL_DATA, name="spatialData__PANEL_DATA", curie=HTAN.curie('PANEL_DATA'),
                   model_uri=HTAN.spatialData__PANEL_DATA, domain=None, range=Optional[Union[Union[str, SpatialPanelHTANPANELID], List[Union[str, SpatialPanelHTANPANELID]]]])

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

slots.spatialLevel1__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="spatialLevel1__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.spatialLevel1__FILE_FORMAT, domain=None, range=Union[str, "FileFormatLevel1"])

slots.spatialLevel1__FILENAME = Slot(uri=HTAN.FILENAME, name="spatialLevel1__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.spatialLevel1__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.(tar(\.gz)?|zip)$'))

slots.spatialLevel1__PLATFORM = Slot(uri=HTAN.PLATFORM, name="spatialLevel1__PLATFORM", curie=HTAN.curie('PLATFORM'),
                   model_uri=HTAN.spatialLevel1__PLATFORM, domain=None, range=Union[str, "Platform"])

slots.spatialLevel1__ASSAY_TYPE = Slot(uri=HTAN.ASSAY_TYPE, name="spatialLevel1__ASSAY_TYPE", curie=HTAN.curie('ASSAY_TYPE'),
                   model_uri=HTAN.spatialLevel1__ASSAY_TYPE, domain=None, range=Union[str, "AssayType"])

slots.spatialLevel1__BUNDLE_CONTENTS = Slot(uri=HTAN.BUNDLE_CONTENTS, name="spatialLevel1__BUNDLE_CONTENTS", curie=HTAN.curie('BUNDLE_CONTENTS'),
                   model_uri=HTAN.spatialLevel1__BUNDLE_CONTENTS, domain=None, range=Union[str, List[str]])

slots.spatialLevel1__HAS_SEQUENCING = Slot(uri=HTAN.HAS_SEQUENCING, name="spatialLevel1__HAS_SEQUENCING", curie=HTAN.curie('HAS_SEQUENCING'),
                   model_uri=HTAN.spatialLevel1__HAS_SEQUENCING, domain=None, range=Optional[Union[bool, Bool]])

slots.spatialLevel1__SEQUENCING_FILE_TYPE = Slot(uri=HTAN.SEQUENCING_FILE_TYPE, name="spatialLevel1__SEQUENCING_FILE_TYPE", curie=HTAN.curie('SEQUENCING_FILE_TYPE'),
                   model_uri=HTAN.spatialLevel1__SEQUENCING_FILE_TYPE, domain=None, range=Optional[Union[Union[str, "SequencingFileType"], List[Union[str, "SequencingFileType"]]]])

slots.spatialLevel1__HAS_IMAGES = Slot(uri=HTAN.HAS_IMAGES, name="spatialLevel1__HAS_IMAGES", curie=HTAN.curie('HAS_IMAGES'),
                   model_uri=HTAN.spatialLevel1__HAS_IMAGES, domain=None, range=Union[bool, Bool])

slots.spatialLevel1__IMAGE_TYPES = Slot(uri=HTAN.IMAGE_TYPES, name="spatialLevel1__IMAGE_TYPES", curie=HTAN.curie('IMAGE_TYPES'),
                   model_uri=HTAN.spatialLevel1__IMAGE_TYPES, domain=None, range=Optional[Union[Union[str, "ImageType"], List[Union[str, "ImageType"]]]])

slots.spatialLevel1__HAS_PROBE_SET = Slot(uri=HTAN.HAS_PROBE_SET, name="spatialLevel1__HAS_PROBE_SET", curie=HTAN.curie('HAS_PROBE_SET'),
                   model_uri=HTAN.spatialLevel1__HAS_PROBE_SET, domain=None, range=Optional[Union[bool, Bool]])

slots.spatialLevel1__HAS_REGISTRATION_FILES = Slot(uri=HTAN.HAS_REGISTRATION_FILES, name="spatialLevel1__HAS_REGISTRATION_FILES", curie=HTAN.curie('HAS_REGISTRATION_FILES'),
                   model_uri=HTAN.spatialLevel1__HAS_REGISTRATION_FILES, domain=None, range=Union[bool, Bool])

slots.spatialLevel3__PLATFORM = Slot(uri=HTAN.PLATFORM, name="spatialLevel3__PLATFORM", curie=HTAN.curie('PLATFORM'),
                   model_uri=HTAN.spatialLevel3__PLATFORM, domain=None, range=Union[str, "PlatformLevel3"])

slots.spatialLevel3__SPATIAL_ASSAY_TYPE = Slot(uri=HTAN.SPATIAL_ASSAY_TYPE, name="spatialLevel3__SPATIAL_ASSAY_TYPE", curie=HTAN.curie('SPATIAL_ASSAY_TYPE'),
                   model_uri=HTAN.spatialLevel3__SPATIAL_ASSAY_TYPE, domain=None, range=Optional[Union[str, "SpatialAssayType"]])

slots.spatialLevel3__ASSAY_CHEMISTRY_VERSION = Slot(uri=HTAN.ASSAY_CHEMISTRY_VERSION, name="spatialLevel3__ASSAY_CHEMISTRY_VERSION", curie=HTAN.curie('ASSAY_CHEMISTRY_VERSION'),
                   model_uri=HTAN.spatialLevel3__ASSAY_CHEMISTRY_VERSION, domain=None, range=str)

slots.spatialLevel3__SOFTWARE_AND_VERSION = Slot(uri=HTAN.SOFTWARE_AND_VERSION, name="spatialLevel3__SOFTWARE_AND_VERSION", curie=HTAN.curie('SOFTWARE_AND_VERSION'),
                   model_uri=HTAN.spatialLevel3__SOFTWARE_AND_VERSION, domain=None, range=Optional[str])

slots.spatialLevel3__PROTOCOL_LINK = Slot(uri=HTAN.PROTOCOL_LINK, name="spatialLevel3__PROTOCOL_LINK", curie=HTAN.curie('PROTOCOL_LINK'),
                   model_uri=HTAN.spatialLevel3__PROTOCOL_LINK, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$'))

slots.spatialLevel3__RNA_MEASURED = Slot(uri=HTAN.RNA_MEASURED, name="spatialLevel3__RNA_MEASURED", curie=HTAN.curie('RNA_MEASURED'),
                   model_uri=HTAN.spatialLevel3__RNA_MEASURED, domain=None, range=Union[bool, Bool])

slots.spatialLevel3__PROTEIN_MEASURED = Slot(uri=HTAN.PROTEIN_MEASURED, name="spatialLevel3__PROTEIN_MEASURED", curie=HTAN.curie('PROTEIN_MEASURED'),
                   model_uri=HTAN.spatialLevel3__PROTEIN_MEASURED, domain=None, range=Union[bool, Bool])

slots.spatialLevel3__TRANSCRIPTOME_TYPE = Slot(uri=HTAN.TRANSCRIPTOME_TYPE, name="spatialLevel3__TRANSCRIPTOME_TYPE", curie=HTAN.curie('TRANSCRIPTOME_TYPE'),
                   model_uri=HTAN.spatialLevel3__TRANSCRIPTOME_TYPE, domain=None, range=Optional[Union[str, "TranscriptomeType"]])

slots.spatialLevel3__PANEL_SIZE_TOTAL_TARGETS = Slot(uri=HTAN.PANEL_SIZE_TOTAL_TARGETS, name="spatialLevel3__PANEL_SIZE_TOTAL_TARGETS", curie=HTAN.curie('PANEL_SIZE_TOTAL_TARGETS'),
                   model_uri=HTAN.spatialLevel3__PANEL_SIZE_TOTAL_TARGETS, domain=None, range=int)

slots.spatialLevel3__PANEL_NAME = Slot(uri=HTAN.PANEL_NAME, name="spatialLevel3__PANEL_NAME", curie=HTAN.curie('PANEL_NAME'),
                   model_uri=HTAN.spatialLevel3__PANEL_NAME, domain=None, range=Optional[str])

slots.spatialLevel3__PANEL_SYNAPSE_ID = Slot(uri=HTAN.PANEL_SYNAPSE_ID, name="spatialLevel3__PANEL_SYNAPSE_ID", curie=HTAN.curie('PANEL_SYNAPSE_ID'),
                   model_uri=HTAN.spatialLevel3__PANEL_SYNAPSE_ID, domain=None, range=Optional[str],
                   pattern=re.compile(r'^syn\d+$'))

slots.spatialLevel3__SAME_SECTION_IMAGING_ID = Slot(uri=HTAN.SAME_SECTION_IMAGING_ID, name="spatialLevel3__SAME_SECTION_IMAGING_ID", curie=HTAN.curie('SAME_SECTION_IMAGING_ID'),
                   model_uri=HTAN.spatialLevel3__SAME_SECTION_IMAGING_ID, domain=None, range=Optional[Union[str, List[str]]],
                   pattern=re.compile(r'^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$'))

slots.spatialLevel3__SAME_SECTION_IMAGING_MODALITY = Slot(uri=HTAN.SAME_SECTION_IMAGING_MODALITY, name="spatialLevel3__SAME_SECTION_IMAGING_MODALITY", curie=HTAN.curie('SAME_SECTION_IMAGING_MODALITY'),
                   model_uri=HTAN.spatialLevel3__SAME_SECTION_IMAGING_MODALITY, domain=None, range=Optional[Union[str, "SameSectionImagingModality"]])

slots.spatialLevel3__SAME_SECTION_IMAGING_CHANNELS = Slot(uri=HTAN.SAME_SECTION_IMAGING_CHANNELS, name="spatialLevel3__SAME_SECTION_IMAGING_CHANNELS", curie=HTAN.curie('SAME_SECTION_IMAGING_CHANNELS'),
                   model_uri=HTAN.spatialLevel3__SAME_SECTION_IMAGING_CHANNELS, domain=None, range=Optional[Union[str, List[str]]])

slots.spatialLevel3__REGION_AREA = Slot(uri=HTAN.REGION_AREA, name="spatialLevel3__REGION_AREA", curie=HTAN.curie('REGION_AREA'),
                   model_uri=HTAN.spatialLevel3__REGION_AREA, domain=None, range=float)

slots.spatialLevel3__BUNDLE_CONTENTS = Slot(uri=HTAN.BUNDLE_CONTENTS, name="spatialLevel3__BUNDLE_CONTENTS", curie=HTAN.curie('BUNDLE_CONTENTS'),
                   model_uri=HTAN.spatialLevel3__BUNDLE_CONTENTS, domain=None, range=Union[str, List[str]])

slots.spatialLevel3__PORTAL_PREVIEW_FILE = Slot(uri=HTAN.PORTAL_PREVIEW_FILE, name="spatialLevel3__PORTAL_PREVIEW_FILE", curie=HTAN.curie('PORTAL_PREVIEW_FILE'),
                   model_uri=HTAN.spatialLevel3__PORTAL_PREVIEW_FILE, domain=None, range=Optional[str])

slots.spatialLevel3__HAS_CELL_SEGMENTATION = Slot(uri=HTAN.HAS_CELL_SEGMENTATION, name="spatialLevel3__HAS_CELL_SEGMENTATION", curie=HTAN.curie('HAS_CELL_SEGMENTATION'),
                   model_uri=HTAN.spatialLevel3__HAS_CELL_SEGMENTATION, domain=None, range=Union[bool, Bool])

slots.spatialLevel3__CELL_SEGMENTATION_METHOD = Slot(uri=HTAN.CELL_SEGMENTATION_METHOD, name="spatialLevel3__CELL_SEGMENTATION_METHOD", curie=HTAN.curie('CELL_SEGMENTATION_METHOD'),
                   model_uri=HTAN.spatialLevel3__CELL_SEGMENTATION_METHOD, domain=None, range=Optional[str])

slots.spatialLevel3__CELL_SEGMENTED_OBJECT_TYPE = Slot(uri=HTAN.CELL_SEGMENTED_OBJECT_TYPE, name="spatialLevel3__CELL_SEGMENTED_OBJECT_TYPE", curie=HTAN.curie('CELL_SEGMENTED_OBJECT_TYPE'),
                   model_uri=HTAN.spatialLevel3__CELL_SEGMENTED_OBJECT_TYPE, domain=None, range=Optional[Union[str, "CellSegmentedObjectType"]])

slots.spatialLevel3__NUMBER_OF_SEGMENTED_CELLS = Slot(uri=HTAN.NUMBER_OF_SEGMENTED_CELLS, name="spatialLevel3__NUMBER_OF_SEGMENTED_CELLS", curie=HTAN.curie('NUMBER_OF_SEGMENTED_CELLS'),
                   model_uri=HTAN.spatialLevel3__NUMBER_OF_SEGMENTED_CELLS, domain=None, range=Optional[int])

slots.spatialLevel3__HAS_DIMENSIONALITY_REDUCTION = Slot(uri=HTAN.HAS_DIMENSIONALITY_REDUCTION, name="spatialLevel3__HAS_DIMENSIONALITY_REDUCTION", curie=HTAN.curie('HAS_DIMENSIONALITY_REDUCTION'),
                   model_uri=HTAN.spatialLevel3__HAS_DIMENSIONALITY_REDUCTION, domain=None, range=Optional[Union[bool, Bool]])

slots.spatialLevel3__DIMENSIONALITY_REDUCTION_METHOD = Slot(uri=HTAN.DIMENSIONALITY_REDUCTION_METHOD, name="spatialLevel3__DIMENSIONALITY_REDUCTION_METHOD", curie=HTAN.curie('DIMENSIONALITY_REDUCTION_METHOD'),
                   model_uri=HTAN.spatialLevel3__DIMENSIONALITY_REDUCTION_METHOD, domain=None, range=Optional[Union[str, "DimensionalityReductionMethod"]])

slots.spatialLevel3__HAS_CLUSTERING = Slot(uri=HTAN.HAS_CLUSTERING, name="spatialLevel3__HAS_CLUSTERING", curie=HTAN.curie('HAS_CLUSTERING'),
                   model_uri=HTAN.spatialLevel3__HAS_CLUSTERING, domain=None, range=Union[bool, Bool])

slots.spatialLevel3__CLUSTERING_METHOD = Slot(uri=HTAN.CLUSTERING_METHOD, name="spatialLevel3__CLUSTERING_METHOD", curie=HTAN.curie('CLUSTERING_METHOD'),
                   model_uri=HTAN.spatialLevel3__CLUSTERING_METHOD, domain=None, range=Optional[str])

slots.spatialLevel3__NUMBER_OF_CLUSTERS = Slot(uri=HTAN.NUMBER_OF_CLUSTERS, name="spatialLevel3__NUMBER_OF_CLUSTERS", curie=HTAN.curie('NUMBER_OF_CLUSTERS'),
                   model_uri=HTAN.spatialLevel3__NUMBER_OF_CLUSTERS, domain=None, range=Optional[int])

slots.spatialLevel3__SLIDE_SERIAL_NUMBER = Slot(uri=HTAN.SLIDE_SERIAL_NUMBER, name="spatialLevel3__SLIDE_SERIAL_NUMBER", curie=HTAN.curie('SLIDE_SERIAL_NUMBER'),
                   model_uri=HTAN.spatialLevel3__SLIDE_SERIAL_NUMBER, domain=None, range=Optional[str])

slots.spatialLevel3__CAPTURE_AREA = Slot(uri=HTAN.CAPTURE_AREA, name="spatialLevel3__CAPTURE_AREA", curie=HTAN.curie('CAPTURE_AREA'),
                   model_uri=HTAN.spatialLevel3__CAPTURE_AREA, domain=None, range=Optional[Union[str, "CaptureArea"]])

slots.spatialLevel3__RUN_ID = Slot(uri=HTAN.RUN_ID, name="spatialLevel3__RUN_ID", curie=HTAN.curie('RUN_ID'),
                   model_uri=HTAN.spatialLevel3__RUN_ID, domain=None, range=Optional[str])

slots.spatialLevel3__CYTASSIST_USED = Slot(uri=HTAN.CYTASSIST_USED, name="spatialLevel3__CYTASSIST_USED", curie=HTAN.curie('CYTASSIST_USED'),
                   model_uri=HTAN.spatialLevel3__CYTASSIST_USED, domain=None, range=Optional[Union[bool, Bool]])

slots.spatialLevel3__GENOMIC_REFERENCE = Slot(uri=HTAN.GENOMIC_REFERENCE, name="spatialLevel3__GENOMIC_REFERENCE", curie=HTAN.curie('GENOMIC_REFERENCE'),
                   model_uri=HTAN.spatialLevel3__GENOMIC_REFERENCE, domain=None, range=Optional[str])

slots.spatialLevel3__SEQUENCING_INSTRUMENT = Slot(uri=HTAN.SEQUENCING_INSTRUMENT, name="spatialLevel3__SEQUENCING_INSTRUMENT", curie=HTAN.curie('SEQUENCING_INSTRUMENT'),
                   model_uri=HTAN.spatialLevel3__SEQUENCING_INSTRUMENT, domain=None, range=Optional[str])

slots.spatialLevel3__SEQUENCING_CONFIGURATION = Slot(uri=HTAN.SEQUENCING_CONFIGURATION, name="spatialLevel3__SEQUENCING_CONFIGURATION", curie=HTAN.curie('SEQUENCING_CONFIGURATION'),
                   model_uri=HTAN.spatialLevel3__SEQUENCING_CONFIGURATION, domain=None, range=Optional[str])

slots.spatialLevel3__SEQUENCING_DEPTH = Slot(uri=HTAN.SEQUENCING_DEPTH, name="spatialLevel3__SEQUENCING_DEPTH", curie=HTAN.curie('SEQUENCING_DEPTH'),
                   model_uri=HTAN.spatialLevel3__SEQUENCING_DEPTH, domain=None, range=Optional[str])

slots.spatialLevel3__QC_SPATIAL_UNIT = Slot(uri=HTAN.QC_SPATIAL_UNIT, name="spatialLevel3__QC_SPATIAL_UNIT", curie=HTAN.curie('QC_SPATIAL_UNIT'),
                   model_uri=HTAN.spatialLevel3__QC_SPATIAL_UNIT, domain=None, range=Union[str, "QCSpatialUnit"])

slots.spatialLevel3__QC_FEATURE_NUMBER = Slot(uri=HTAN.QC_FEATURE_NUMBER, name="spatialLevel3__QC_FEATURE_NUMBER", curie=HTAN.curie('QC_FEATURE_NUMBER'),
                   model_uri=HTAN.spatialLevel3__QC_FEATURE_NUMBER, domain=None, range=int)

slots.spatialLevel3__QC_MEAN_READS_PER_FEATURE = Slot(uri=HTAN.QC_MEAN_READS_PER_FEATURE, name="spatialLevel3__QC_MEAN_READS_PER_FEATURE", curie=HTAN.curie('QC_MEAN_READS_PER_FEATURE'),
                   model_uri=HTAN.spatialLevel3__QC_MEAN_READS_PER_FEATURE, domain=None, range=float)

slots.spatialLevel3__QC_TOTAL_GENES_DETECTED = Slot(uri=HTAN.QC_TOTAL_GENES_DETECTED, name="spatialLevel3__QC_TOTAL_GENES_DETECTED", curie=HTAN.curie('QC_TOTAL_GENES_DETECTED'),
                   model_uri=HTAN.spatialLevel3__QC_TOTAL_GENES_DETECTED, domain=None, range=int)

slots.spatialLevel3__QC_TOTAL_NUMBER_OF_READS = Slot(uri=HTAN.QC_TOTAL_NUMBER_OF_READS, name="spatialLevel3__QC_TOTAL_NUMBER_OF_READS", curie=HTAN.curie('QC_TOTAL_NUMBER_OF_READS'),
                   model_uri=HTAN.spatialLevel3__QC_TOTAL_NUMBER_OF_READS, domain=None, range=int)

slots.spatialLevel4__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="spatialLevel4__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.spatialLevel4__FILE_FORMAT, domain=None, range=Union[str, "FileFormatLevel4"])

slots.spatialLevel4__FILENAME = Slot(uri=HTAN.FILENAME, name="spatialLevel4__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.spatialLevel4__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.(h5ad|rds|zarr)$'))

slots.spatialLevel4__TOOL_COMPATIBILITY = Slot(uri=HTAN.TOOL_COMPATIBILITY, name="spatialLevel4__TOOL_COMPATIBILITY", curie=HTAN.curie('TOOL_COMPATIBILITY'),
                   model_uri=HTAN.spatialLevel4__TOOL_COMPATIBILITY, domain=None, range=Optional[Union[Union[str, "ToolCompatibility"], List[Union[str, "ToolCompatibility"]]]])

slots.spatialLevel4__NUMBER_OF_FEATURES = Slot(uri=HTAN.NUMBER_OF_FEATURES, name="spatialLevel4__NUMBER_OF_FEATURES", curie=HTAN.curie('NUMBER_OF_FEATURES'),
                   model_uri=HTAN.spatialLevel4__NUMBER_OF_FEATURES, domain=None, range=int)

slots.spatialLevel4__NUMBER_OF_OBJECTS = Slot(uri=HTAN.NUMBER_OF_OBJECTS, name="spatialLevel4__NUMBER_OF_OBJECTS", curie=HTAN.curie('NUMBER_OF_OBJECTS'),
                   model_uri=HTAN.spatialLevel4__NUMBER_OF_OBJECTS, domain=None, range=int)

slots.spatialLevel4__HAS_DIMENSIONALITY_REDUCTION = Slot(uri=HTAN.HAS_DIMENSIONALITY_REDUCTION, name="spatialLevel4__HAS_DIMENSIONALITY_REDUCTION", curie=HTAN.curie('HAS_DIMENSIONALITY_REDUCTION'),
                   model_uri=HTAN.spatialLevel4__HAS_DIMENSIONALITY_REDUCTION, domain=None, range=Union[bool, Bool])

slots.spatialLevel4__DIMENSIONALITY_REDUCTION_METHOD = Slot(uri=HTAN.DIMENSIONALITY_REDUCTION_METHOD, name="spatialLevel4__DIMENSIONALITY_REDUCTION_METHOD", curie=HTAN.curie('DIMENSIONALITY_REDUCTION_METHOD'),
                   model_uri=HTAN.spatialLevel4__DIMENSIONALITY_REDUCTION_METHOD, domain=None, range=Optional[Union[str, "DimensionalityReductionMethodLevel4"]])

slots.spatialLevel4__HAS_CLUSTERING = Slot(uri=HTAN.HAS_CLUSTERING, name="spatialLevel4__HAS_CLUSTERING", curie=HTAN.curie('HAS_CLUSTERING'),
                   model_uri=HTAN.spatialLevel4__HAS_CLUSTERING, domain=None, range=Union[bool, Bool])

slots.spatialLevel4__CLUSTERING_METHOD = Slot(uri=HTAN.CLUSTERING_METHOD, name="spatialLevel4__CLUSTERING_METHOD", curie=HTAN.curie('CLUSTERING_METHOD'),
                   model_uri=HTAN.spatialLevel4__CLUSTERING_METHOD, domain=None, range=Optional[str])

slots.spatialLevel4__NUMBER_OF_CLUSTERS = Slot(uri=HTAN.NUMBER_OF_CLUSTERS, name="spatialLevel4__NUMBER_OF_CLUSTERS", curie=HTAN.curie('NUMBER_OF_CLUSTERS'),
                   model_uri=HTAN.spatialLevel4__NUMBER_OF_CLUSTERS, domain=None, range=Optional[int])

slots.spatialLevel4__HAS_CELL_TYPE_CALLING = Slot(uri=HTAN.HAS_CELL_TYPE_CALLING, name="spatialLevel4__HAS_CELL_TYPE_CALLING", curie=HTAN.curie('HAS_CELL_TYPE_CALLING'),
                   model_uri=HTAN.spatialLevel4__HAS_CELL_TYPE_CALLING, domain=None, range=Union[bool, Bool])

slots.spatialLevel4__CELL_TYPE_CALLING_METHOD = Slot(uri=HTAN.CELL_TYPE_CALLING_METHOD, name="spatialLevel4__CELL_TYPE_CALLING_METHOD", curie=HTAN.curie('CELL_TYPE_CALLING_METHOD'),
                   model_uri=HTAN.spatialLevel4__CELL_TYPE_CALLING_METHOD, domain=None, range=Optional[str])

slots.spatialLevel4__CELL_TYPES = Slot(uri=HTAN.CELL_TYPES, name="spatialLevel4__CELL_TYPES", curie=HTAN.curie('CELL_TYPES'),
                   model_uri=HTAN.spatialLevel4__CELL_TYPES, domain=None, range=Optional[Union[str, List[str]]])

slots.spatialLevel4__HAS_NORMALISED_ARRAY = Slot(uri=HTAN.HAS_NORMALISED_ARRAY, name="spatialLevel4__HAS_NORMALISED_ARRAY", curie=HTAN.curie('HAS_NORMALISED_ARRAY'),
                   model_uri=HTAN.spatialLevel4__HAS_NORMALISED_ARRAY, domain=None, range=Union[bool, Bool])

slots.spatialLevel4__NORMALISATION_METHOD = Slot(uri=HTAN.NORMALISATION_METHOD, name="spatialLevel4__NORMALISATION_METHOD", curie=HTAN.curie('NORMALISATION_METHOD'),
                   model_uri=HTAN.spatialLevel4__NORMALISATION_METHOD, domain=None, range=Optional[Union[str, "NormalisationMethod"]])

slots.spatialLevel4__HAS_RAW_ARRAY = Slot(uri=HTAN.HAS_RAW_ARRAY, name="spatialLevel4__HAS_RAW_ARRAY", curie=HTAN.curie('HAS_RAW_ARRAY'),
                   model_uri=HTAN.spatialLevel4__HAS_RAW_ARRAY, domain=None, range=Union[bool, Bool])

slots.spatialLevel4__HAS_IMAGE = Slot(uri=HTAN.HAS_IMAGE, name="spatialLevel4__HAS_IMAGE", curie=HTAN.curie('HAS_IMAGE'),
                   model_uri=HTAN.spatialLevel4__HAS_IMAGE, domain=None, range=Union[bool, Bool])

slots.spatialLevel4__IMAGE_TYPE = Slot(uri=HTAN.IMAGE_TYPE, name="spatialLevel4__IMAGE_TYPE", curie=HTAN.curie('IMAGE_TYPE'),
                   model_uri=HTAN.spatialLevel4__IMAGE_TYPE, domain=None, range=Optional[Union[str, "ImageTypeLevel4"]])

slots.spatialPanel__HTAN_PANEL_ID = Slot(uri=HTAN.HTAN_PANEL_ID, name="spatialPanel__HTAN_PANEL_ID", curie=HTAN.curie('HTAN_PANEL_ID'),
                   model_uri=HTAN.spatialPanel__HTAN_PANEL_ID, domain=None, range=URIRef,
                   pattern=re.compile(r'^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(P[0-9]{1,20})$'))

slots.spatialPanel__GENE_SYMBOL = Slot(uri=HTAN.GENE_SYMBOL, name="spatialPanel__GENE_SYMBOL", curie=HTAN.curie('GENE_SYMBOL'),
                   model_uri=HTAN.spatialPanel__GENE_SYMBOL, domain=None, range=str,
                   pattern=re.compile(r'^[A-Za-z0-9_\-]+(@)?$'))

slots.spatialPanel__HGNC_VERSION = Slot(uri=HTAN.HGNC_VERSION, name="spatialPanel__HGNC_VERSION", curie=HTAN.curie('HGNC_VERSION'),
                   model_uri=HTAN.spatialPanel__HGNC_VERSION, domain=None, range=str,
                   pattern=re.compile(r'^\d{4}-\d{2}-\d{2}$'))

slots.spatialPanel__GENE_ID = Slot(uri=HTAN.GENE_ID, name="spatialPanel__GENE_ID", curie=HTAN.curie('GENE_ID'),
                   model_uri=HTAN.spatialPanel__GENE_ID, domain=None, range=str,
                   pattern=re.compile(r'^(ENSG\d+|\d+)$'))

slots.spatialPanel__USER_GENE_NAME = Slot(uri=HTAN.USER_GENE_NAME, name="spatialPanel__USER_GENE_NAME", curie=HTAN.curie('USER_GENE_NAME'),
                   model_uri=HTAN.spatialPanel__USER_GENE_NAME, domain=None, range=Optional[str])

slots.SpatialLevel3_FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="SpatialLevel3_FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.SpatialLevel3_FILE_FORMAT, domain=SpatialLevel3, range=str,
                   pattern=re.compile(r'^(tar\.gz|gz)$'))

slots.SpatialLevel3_FILENAME = Slot(uri=HTAN.FILENAME, name="SpatialLevel3_FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.SpatialLevel3_FILENAME, domain=SpatialLevel3, range=str,
                   pattern=re.compile(r'^.+\.(tar\.gz|gz)$'))
