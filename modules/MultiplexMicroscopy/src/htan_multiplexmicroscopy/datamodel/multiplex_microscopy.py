# Auto generated from multiplex_microscopy.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-09T18:01:57
# Schema: MultiplexMicroscopy
#
# id: https://w3id.org/htan/multiplex_microscopy
# description: HTAN Multiplex Microscopy Data Model Schema for Phase 2 - All Levels
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


class BaseImagingAttributesHTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class MultiplexMicroscopyLevel2HTANDATAFILEID(BaseImagingAttributesHTANDATAFILEID):
    pass


class MultiplexMicroscopyLevel3HTANDATAFILEID(BaseImagingAttributesHTANDATAFILEID):
    pass


class MultiplexMicroscopyLevel4HTANDATAFILEID(BaseImagingAttributesHTANDATAFILEID):
    pass


@dataclass(repr=False)
class MultiplexMicroscopyData(YAMLRoot):
    """
    Container for all Multiplex Microscopy data levels
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MultiplexMicroscopyData"]
    class_class_curie: ClassVar[str] = "htan:MultiplexMicroscopyData"
    class_name: ClassVar[str] = "MultiplexMicroscopyData"
    class_model_uri: ClassVar[URIRef] = HTAN.MultiplexMicroscopyData

    LEVEL_2_DATA: Optional[Union[str, MultiplexMicroscopyLevel2HTANDATAFILEID]] = None
    LEVEL_3_DATA: Optional[Union[str, MultiplexMicroscopyLevel3HTANDATAFILEID]] = None
    LEVEL_4_DATA: Optional[Union[str, MultiplexMicroscopyLevel4HTANDATAFILEID]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.LEVEL_2_DATA is not None and not isinstance(self.LEVEL_2_DATA, MultiplexMicroscopyLevel2HTANDATAFILEID):
            self.LEVEL_2_DATA = MultiplexMicroscopyLevel2HTANDATAFILEID(self.LEVEL_2_DATA)

        if self.LEVEL_3_DATA is not None and not isinstance(self.LEVEL_3_DATA, MultiplexMicroscopyLevel3HTANDATAFILEID):
            self.LEVEL_3_DATA = MultiplexMicroscopyLevel3HTANDATAFILEID(self.LEVEL_3_DATA)

        if self.LEVEL_4_DATA is not None and not isinstance(self.LEVEL_4_DATA, MultiplexMicroscopyLevel4HTANDATAFILEID):
            self.LEVEL_4_DATA = MultiplexMicroscopyLevel4HTANDATAFILEID(self.LEVEL_4_DATA)

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
    HTAN_PARENT_ID: str = None

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
        if not isinstance(self.HTAN_PARENT_ID, str):
            self.HTAN_PARENT_ID = str(self.HTAN_PARENT_ID)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BaseImagingAttributes(CoreFileAttributes):
    """
    Base attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["BaseImagingAttributes"]
    class_class_curie: ClassVar[str] = "htan:BaseImagingAttributes"
    class_name: ClassVar[str] = "BaseImagingAttributes"
    class_model_uri: ClassVar[URIRef] = HTAN.BaseImagingAttributes

    HTAN_DATA_FILE_ID: Union[str, BaseImagingAttributesHTANDATAFILEID] = None
    FILENAME: str = None
    FILE_FORMAT: str = None
    HTAN_PARENT_ID: str = None
    EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES: Union[str, "ExperimentalStrategyAndDataSubtypes"] = None
    DE_IDENTIFICATION_METHOD_TYPE: Union[str, "DeIdentificationMethodType"] = None
    LICENSE: Union[str, "License"] = None
    IMAGE_MODALITY: Union[str, "ImageModality"] = None
    IMAGING_EQUIPMENT_MANUFACTURER: str = None
    CITATION_OR_DOI: str = None
    STAINING_METHOD: Union[str, "StainingMethod"] = None
    OBJECTIVE: str = None
    NOMINAL_MAGNIFICATION: int = None
    PASSED_QC: Union[bool, Bool] = None
    QC_COMMENT: str = None
    SPECIES: Union[str, "Species"] = None
    DE_IDENTIFICATION_METHOD_DESCRIPTION: Optional[str] = None
    DE_IDENTIFICATION_SOFTWARE: Optional[str] = None
    IMAGING_EQUIPMENT_MODEL: Optional[str] = None
    IMAGING_SOFTWARE: Optional[str] = None
    IMAGING_PROTOCOL: Optional[str] = None
    IMMERSION: Optional[Union[str, "ImmersionMedium"]] = None
    LENS_NUMERICAL_APERTURE: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, BaseImagingAttributesHTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = BaseImagingAttributesHTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES):
            self.MissingRequiredField("EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES")
        if not isinstance(self.EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES, ExperimentalStrategyAndDataSubtypes):
            self.EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES = ExperimentalStrategyAndDataSubtypes(self.EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES)

        if self._is_empty(self.DE_IDENTIFICATION_METHOD_TYPE):
            self.MissingRequiredField("DE_IDENTIFICATION_METHOD_TYPE")
        if not isinstance(self.DE_IDENTIFICATION_METHOD_TYPE, DeIdentificationMethodType):
            self.DE_IDENTIFICATION_METHOD_TYPE = DeIdentificationMethodType(self.DE_IDENTIFICATION_METHOD_TYPE)

        if self._is_empty(self.LICENSE):
            self.MissingRequiredField("LICENSE")
        if not isinstance(self.LICENSE, License):
            self.LICENSE = License(self.LICENSE)

        if self._is_empty(self.IMAGE_MODALITY):
            self.MissingRequiredField("IMAGE_MODALITY")
        if not isinstance(self.IMAGE_MODALITY, ImageModality):
            self.IMAGE_MODALITY = ImageModality(self.IMAGE_MODALITY)

        if self._is_empty(self.IMAGING_EQUIPMENT_MANUFACTURER):
            self.MissingRequiredField("IMAGING_EQUIPMENT_MANUFACTURER")
        if not isinstance(self.IMAGING_EQUIPMENT_MANUFACTURER, str):
            self.IMAGING_EQUIPMENT_MANUFACTURER = str(self.IMAGING_EQUIPMENT_MANUFACTURER)

        if self._is_empty(self.CITATION_OR_DOI):
            self.MissingRequiredField("CITATION_OR_DOI")
        if not isinstance(self.CITATION_OR_DOI, str):
            self.CITATION_OR_DOI = str(self.CITATION_OR_DOI)

        if self._is_empty(self.STAINING_METHOD):
            self.MissingRequiredField("STAINING_METHOD")
        if not isinstance(self.STAINING_METHOD, StainingMethod):
            self.STAINING_METHOD = StainingMethod(self.STAINING_METHOD)

        if self._is_empty(self.OBJECTIVE):
            self.MissingRequiredField("OBJECTIVE")
        if not isinstance(self.OBJECTIVE, str):
            self.OBJECTIVE = str(self.OBJECTIVE)

        if self._is_empty(self.NOMINAL_MAGNIFICATION):
            self.MissingRequiredField("NOMINAL_MAGNIFICATION")
        if not isinstance(self.NOMINAL_MAGNIFICATION, int):
            self.NOMINAL_MAGNIFICATION = int(self.NOMINAL_MAGNIFICATION)

        if self._is_empty(self.PASSED_QC):
            self.MissingRequiredField("PASSED_QC")
        if not isinstance(self.PASSED_QC, Bool):
            self.PASSED_QC = Bool(self.PASSED_QC)

        if self._is_empty(self.QC_COMMENT):
            self.MissingRequiredField("QC_COMMENT")
        if not isinstance(self.QC_COMMENT, str):
            self.QC_COMMENT = str(self.QC_COMMENT)

        if self._is_empty(self.SPECIES):
            self.MissingRequiredField("SPECIES")
        if not isinstance(self.SPECIES, Species):
            self.SPECIES = Species(self.SPECIES)

        if self.DE_IDENTIFICATION_METHOD_DESCRIPTION is not None and not isinstance(self.DE_IDENTIFICATION_METHOD_DESCRIPTION, str):
            self.DE_IDENTIFICATION_METHOD_DESCRIPTION = str(self.DE_IDENTIFICATION_METHOD_DESCRIPTION)

        if self.DE_IDENTIFICATION_SOFTWARE is not None and not isinstance(self.DE_IDENTIFICATION_SOFTWARE, str):
            self.DE_IDENTIFICATION_SOFTWARE = str(self.DE_IDENTIFICATION_SOFTWARE)

        if self.IMAGING_EQUIPMENT_MODEL is not None and not isinstance(self.IMAGING_EQUIPMENT_MODEL, str):
            self.IMAGING_EQUIPMENT_MODEL = str(self.IMAGING_EQUIPMENT_MODEL)

        if self.IMAGING_SOFTWARE is not None and not isinstance(self.IMAGING_SOFTWARE, str):
            self.IMAGING_SOFTWARE = str(self.IMAGING_SOFTWARE)

        if self.IMAGING_PROTOCOL is not None and not isinstance(self.IMAGING_PROTOCOL, str):
            self.IMAGING_PROTOCOL = str(self.IMAGING_PROTOCOL)

        if self.IMMERSION is not None and not isinstance(self.IMMERSION, ImmersionMedium):
            self.IMMERSION = ImmersionMedium(self.IMMERSION)

        if self.LENS_NUMERICAL_APERTURE is not None and not isinstance(self.LENS_NUMERICAL_APERTURE, float):
            self.LENS_NUMERICAL_APERTURE = float(self.LENS_NUMERICAL_APERTURE)

        if self.DE_IDENTIFICATION_METHOD_DESCRIPTION is not None and not isinstance(self.DE_IDENTIFICATION_METHOD_DESCRIPTION, str):
            self.DE_IDENTIFICATION_METHOD_DESCRIPTION = str(self.DE_IDENTIFICATION_METHOD_DESCRIPTION)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultiplexMicroscopyLevel2(BaseImagingAttributes):
    """
    Multiplex Microscopy Level 2 - Imaging data compiled into a single file format (preferably tiled and pyramidal
    OME-TIFF), accompanied by a CSV file containing channel metadata
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MultiplexMicroscopyLevel2"]
    class_class_curie: ClassVar[str] = "htan:MultiplexMicroscopyLevel2"
    class_name: ClassVar[str] = "MultiplexMicroscopyLevel2"
    class_model_uri: ClassVar[URIRef] = HTAN.MultiplexMicroscopyLevel2

    HTAN_DATA_FILE_ID: Union[str, MultiplexMicroscopyLevel2HTANDATAFILEID] = None
    FILENAME: str = None
    HTAN_PARENT_ID: str = None
    EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES: Union[str, "ExperimentalStrategyAndDataSubtypes"] = None
    DE_IDENTIFICATION_METHOD_TYPE: Union[str, "DeIdentificationMethodType"] = None
    LICENSE: Union[str, "License"] = None
    IMAGE_MODALITY: Union[str, "ImageModality"] = None
    IMAGING_EQUIPMENT_MANUFACTURER: str = None
    CITATION_OR_DOI: str = None
    STAINING_METHOD: Union[str, "StainingMethod"] = None
    OBJECTIVE: str = None
    NOMINAL_MAGNIFICATION: int = None
    PASSED_QC: Union[bool, Bool] = None
    QC_COMMENT: str = None
    SPECIES: Union[str, "Species"] = None
    FILE_FORMAT: str = None
    IMAGING_ASSAY_TYPE: Union[str, "ImagingAssayType"] = None
    PHYSICAL_SIZE_X: float = None
    PHYSICAL_SIZE_Y: float = None
    PHYSICAL_SIZE_Z: float = None
    SIZE_C: int = None
    SIZE_T: int = None
    SIZE_X: int = None
    SIZE_Y: int = None
    SIZE_Z: int = None
    CHANNEL_METADATA_ID: str = None
    WORKING_DISTANCE: Optional[str] = None
    PYRAMID: Optional[Union[bool, Bool]] = None
    CHANNEL_METADATA: Optional[Union[Union[dict, "ChannelMetadata"], List[Union[dict, "ChannelMetadata"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MultiplexMicroscopyLevel2HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MultiplexMicroscopyLevel2HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.IMAGING_ASSAY_TYPE):
            self.MissingRequiredField("IMAGING_ASSAY_TYPE")
        if not isinstance(self.IMAGING_ASSAY_TYPE, ImagingAssayType):
            self.IMAGING_ASSAY_TYPE = ImagingAssayType(self.IMAGING_ASSAY_TYPE)

        if self._is_empty(self.PHYSICAL_SIZE_X):
            self.MissingRequiredField("PHYSICAL_SIZE_X")
        if not isinstance(self.PHYSICAL_SIZE_X, float):
            self.PHYSICAL_SIZE_X = float(self.PHYSICAL_SIZE_X)

        if self._is_empty(self.PHYSICAL_SIZE_Y):
            self.MissingRequiredField("PHYSICAL_SIZE_Y")
        if not isinstance(self.PHYSICAL_SIZE_Y, float):
            self.PHYSICAL_SIZE_Y = float(self.PHYSICAL_SIZE_Y)

        if self._is_empty(self.PHYSICAL_SIZE_Z):
            self.MissingRequiredField("PHYSICAL_SIZE_Z")
        if not isinstance(self.PHYSICAL_SIZE_Z, float):
            self.PHYSICAL_SIZE_Z = float(self.PHYSICAL_SIZE_Z)

        if self._is_empty(self.SIZE_C):
            self.MissingRequiredField("SIZE_C")
        if not isinstance(self.SIZE_C, int):
            self.SIZE_C = int(self.SIZE_C)

        if self._is_empty(self.SIZE_T):
            self.MissingRequiredField("SIZE_T")
        if not isinstance(self.SIZE_T, int):
            self.SIZE_T = int(self.SIZE_T)

        if self._is_empty(self.SIZE_X):
            self.MissingRequiredField("SIZE_X")
        if not isinstance(self.SIZE_X, int):
            self.SIZE_X = int(self.SIZE_X)

        if self._is_empty(self.SIZE_Y):
            self.MissingRequiredField("SIZE_Y")
        if not isinstance(self.SIZE_Y, int):
            self.SIZE_Y = int(self.SIZE_Y)

        if self._is_empty(self.SIZE_Z):
            self.MissingRequiredField("SIZE_Z")
        if not isinstance(self.SIZE_Z, int):
            self.SIZE_Z = int(self.SIZE_Z)

        if self._is_empty(self.CHANNEL_METADATA_ID):
            self.MissingRequiredField("CHANNEL_METADATA_ID")
        if not isinstance(self.CHANNEL_METADATA_ID, str):
            self.CHANNEL_METADATA_ID = str(self.CHANNEL_METADATA_ID)

        if self.WORKING_DISTANCE is not None and not isinstance(self.WORKING_DISTANCE, str):
            self.WORKING_DISTANCE = str(self.WORKING_DISTANCE)

        if self.PYRAMID is not None and not isinstance(self.PYRAMID, Bool):
            self.PYRAMID = Bool(self.PYRAMID)

        self._normalize_inlined_as_dict(slot_name="CHANNEL_METADATA", slot_type=ChannelMetadata, key_name="CHANNEL_ID", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultiplexMicroscopyLevel3(BaseImagingAttributes):
    """
    Multiplex Microscopy Level 3 - Segmentation mask. Structured mask data following existing HTAN segmentation
    templates (RFC Imaging Level 3 & 4 - v1)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MultiplexMicroscopyLevel3"]
    class_class_curie: ClassVar[str] = "htan:MultiplexMicroscopyLevel3"
    class_name: ClassVar[str] = "MultiplexMicroscopyLevel3"
    class_model_uri: ClassVar[URIRef] = HTAN.MultiplexMicroscopyLevel3

    HTAN_DATA_FILE_ID: Union[str, MultiplexMicroscopyLevel3HTANDATAFILEID] = None
    FILENAME: str = None
    HTAN_PARENT_ID: str = None
    EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES: Union[str, "ExperimentalStrategyAndDataSubtypes"] = None
    DE_IDENTIFICATION_METHOD_TYPE: Union[str, "DeIdentificationMethodType"] = None
    LICENSE: Union[str, "License"] = None
    IMAGE_MODALITY: Union[str, "ImageModality"] = None
    IMAGING_EQUIPMENT_MANUFACTURER: str = None
    CITATION_OR_DOI: str = None
    STAINING_METHOD: Union[str, "StainingMethod"] = None
    OBJECTIVE: str = None
    NOMINAL_MAGNIFICATION: int = None
    PASSED_QC: Union[bool, Bool] = None
    QC_COMMENT: str = None
    SPECIES: Union[str, "Species"] = None
    SEGMENTATION_WORKFLOW_TYPE: str = None
    SEGMENTATION_METHOD: str = None
    FILE_FORMAT: str = None
    SEGMENTATION_WORKFLOW_URL: Optional[str] = None
    SEGMENTATION_WORKFLOW_VERSION: Optional[str] = None
    SEGMENTATION_PARAMETERS: Optional[str] = None
    SEGMENTATION_ANNOTATION_TYPE: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MultiplexMicroscopyLevel3HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MultiplexMicroscopyLevel3HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.SEGMENTATION_WORKFLOW_TYPE):
            self.MissingRequiredField("SEGMENTATION_WORKFLOW_TYPE")
        if not isinstance(self.SEGMENTATION_WORKFLOW_TYPE, str):
            self.SEGMENTATION_WORKFLOW_TYPE = str(self.SEGMENTATION_WORKFLOW_TYPE)

        if self._is_empty(self.SEGMENTATION_METHOD):
            self.MissingRequiredField("SEGMENTATION_METHOD")
        if not isinstance(self.SEGMENTATION_METHOD, str):
            self.SEGMENTATION_METHOD = str(self.SEGMENTATION_METHOD)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self.SEGMENTATION_WORKFLOW_URL is not None and not isinstance(self.SEGMENTATION_WORKFLOW_URL, str):
            self.SEGMENTATION_WORKFLOW_URL = str(self.SEGMENTATION_WORKFLOW_URL)

        if self.SEGMENTATION_WORKFLOW_VERSION is not None and not isinstance(self.SEGMENTATION_WORKFLOW_VERSION, str):
            self.SEGMENTATION_WORKFLOW_VERSION = str(self.SEGMENTATION_WORKFLOW_VERSION)

        if self.SEGMENTATION_PARAMETERS is not None and not isinstance(self.SEGMENTATION_PARAMETERS, str):
            self.SEGMENTATION_PARAMETERS = str(self.SEGMENTATION_PARAMETERS)

        if self.SEGMENTATION_ANNOTATION_TYPE is not None and not isinstance(self.SEGMENTATION_ANNOTATION_TYPE, str):
            self.SEGMENTATION_ANNOTATION_TYPE = str(self.SEGMENTATION_ANNOTATION_TYPE)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MultiplexMicroscopyLevel4(BaseImagingAttributes):
    """
    Multiplex Microscopy Level 4 - Cell-by-feature table (typically cell-by-marker) generated from the segmentation
    mask and image. No changes from prior definitions (RFC Imaging Level 3 & 4 - v1)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MultiplexMicroscopyLevel4"]
    class_class_curie: ClassVar[str] = "htan:MultiplexMicroscopyLevel4"
    class_name: ClassVar[str] = "MultiplexMicroscopyLevel4"
    class_model_uri: ClassVar[URIRef] = HTAN.MultiplexMicroscopyLevel4

    HTAN_DATA_FILE_ID: Union[str, MultiplexMicroscopyLevel4HTANDATAFILEID] = None
    FILENAME: str = None
    HTAN_PARENT_ID: str = None
    EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES: Union[str, "ExperimentalStrategyAndDataSubtypes"] = None
    DE_IDENTIFICATION_METHOD_TYPE: Union[str, "DeIdentificationMethodType"] = None
    LICENSE: Union[str, "License"] = None
    IMAGE_MODALITY: Union[str, "ImageModality"] = None
    IMAGING_EQUIPMENT_MANUFACTURER: str = None
    CITATION_OR_DOI: str = None
    STAINING_METHOD: Union[str, "StainingMethod"] = None
    OBJECTIVE: str = None
    NOMINAL_MAGNIFICATION: int = None
    PASSED_QC: Union[bool, Bool] = None
    QC_COMMENT: str = None
    SPECIES: Union[str, "Species"] = None
    FEATURE_EXTRACTION_WORKFLOW_TYPE: str = None
    MATRIX_TYPE: Union[str, "MatrixTypeEnum"] = None
    FEATURE_EXTRACTION_METHOD: str = None
    FILE_FORMAT: str = None
    FEATURE_EXTRACTION_WORKFLOW_URL: Optional[str] = None
    FEATURE_EXTRACTION_WORKFLOW_VERSION: Optional[str] = None
    FEATURE_EXTRACTION_PARAMETERS: Optional[str] = None
    NUMBER_OF_FEATURES: Optional[int] = None
    NUMBER_OF_OBJECTS: Optional[int] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MultiplexMicroscopyLevel4HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MultiplexMicroscopyLevel4HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FEATURE_EXTRACTION_WORKFLOW_TYPE):
            self.MissingRequiredField("FEATURE_EXTRACTION_WORKFLOW_TYPE")
        if not isinstance(self.FEATURE_EXTRACTION_WORKFLOW_TYPE, str):
            self.FEATURE_EXTRACTION_WORKFLOW_TYPE = str(self.FEATURE_EXTRACTION_WORKFLOW_TYPE)

        if self._is_empty(self.MATRIX_TYPE):
            self.MissingRequiredField("MATRIX_TYPE")
        if not isinstance(self.MATRIX_TYPE, MatrixTypeEnum):
            self.MATRIX_TYPE = MatrixTypeEnum(self.MATRIX_TYPE)

        if self._is_empty(self.FEATURE_EXTRACTION_METHOD):
            self.MissingRequiredField("FEATURE_EXTRACTION_METHOD")
        if not isinstance(self.FEATURE_EXTRACTION_METHOD, str):
            self.FEATURE_EXTRACTION_METHOD = str(self.FEATURE_EXTRACTION_METHOD)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self.FEATURE_EXTRACTION_WORKFLOW_URL is not None and not isinstance(self.FEATURE_EXTRACTION_WORKFLOW_URL, str):
            self.FEATURE_EXTRACTION_WORKFLOW_URL = str(self.FEATURE_EXTRACTION_WORKFLOW_URL)

        if self.FEATURE_EXTRACTION_WORKFLOW_VERSION is not None and not isinstance(self.FEATURE_EXTRACTION_WORKFLOW_VERSION, str):
            self.FEATURE_EXTRACTION_WORKFLOW_VERSION = str(self.FEATURE_EXTRACTION_WORKFLOW_VERSION)

        if self.FEATURE_EXTRACTION_PARAMETERS is not None and not isinstance(self.FEATURE_EXTRACTION_PARAMETERS, str):
            self.FEATURE_EXTRACTION_PARAMETERS = str(self.FEATURE_EXTRACTION_PARAMETERS)

        if self.NUMBER_OF_FEATURES is not None and not isinstance(self.NUMBER_OF_FEATURES, int):
            self.NUMBER_OF_FEATURES = int(self.NUMBER_OF_FEATURES)

        if self.NUMBER_OF_OBJECTS is not None and not isinstance(self.NUMBER_OF_OBJECTS, int):
            self.NUMBER_OF_OBJECTS = int(self.NUMBER_OF_OBJECTS)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ChannelMetadata(YAMLRoot):
    """
    Metadata for each channel in multiplex microscopy imaging
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["ChannelMetadata"]
    class_class_curie: ClassVar[str] = "htan:ChannelMetadata"
    class_name: ClassVar[str] = "ChannelMetadata"
    class_model_uri: ClassVar[URIRef] = HTAN.ChannelMetadata

    CHANNEL_ID: str = None
    CHANNEL_NAME: str = None
    CYCLE_NUMBER: Optional[int] = None
    SUB_CYCLE_NUMBER: Optional[int] = None
    TARGET_NAME: Optional[str] = None
    ANTIBODY_NAME: Optional[str] = None
    RRID_IDENTIFIER: Optional[str] = None
    FLUOROPHORE: Optional[str] = None
    CLONE: Optional[str] = None
    LOT: Optional[str] = None
    CATALOG_NUMBER: Optional[str] = None
    EXCITATION_WAVELENGTH: Optional[float] = None
    EMISSION_WAVELENGTH: Optional[float] = None
    EXCITATION_BANDWIDTH: Optional[float] = None
    EMISSION_BANDWIDTH: Optional[float] = None
    METAL_ISOTOPE_ELEMENT_ABBREVIATION: Optional[Union[str, "MetalIsotopeElement"]] = None
    METAL_ISOTOPE_ELEMENT_MASS: Optional[int] = None
    OLIGO_BARCODE_UPPER_STRAND: Optional[str] = None
    OLIGO_BARCODE_LOWER_STRAND: Optional[str] = None
    DILUTION: Optional[str] = None
    CONCENTRATION: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.CHANNEL_ID):
            self.MissingRequiredField("CHANNEL_ID")
        if not isinstance(self.CHANNEL_ID, str):
            self.CHANNEL_ID = str(self.CHANNEL_ID)

        if self._is_empty(self.CHANNEL_NAME):
            self.MissingRequiredField("CHANNEL_NAME")
        if not isinstance(self.CHANNEL_NAME, str):
            self.CHANNEL_NAME = str(self.CHANNEL_NAME)

        if self.CYCLE_NUMBER is not None and not isinstance(self.CYCLE_NUMBER, int):
            self.CYCLE_NUMBER = int(self.CYCLE_NUMBER)

        if self.SUB_CYCLE_NUMBER is not None and not isinstance(self.SUB_CYCLE_NUMBER, int):
            self.SUB_CYCLE_NUMBER = int(self.SUB_CYCLE_NUMBER)

        if self.TARGET_NAME is not None and not isinstance(self.TARGET_NAME, str):
            self.TARGET_NAME = str(self.TARGET_NAME)

        if self.ANTIBODY_NAME is not None and not isinstance(self.ANTIBODY_NAME, str):
            self.ANTIBODY_NAME = str(self.ANTIBODY_NAME)

        if self.RRID_IDENTIFIER is not None and not isinstance(self.RRID_IDENTIFIER, str):
            self.RRID_IDENTIFIER = str(self.RRID_IDENTIFIER)

        if self.FLUOROPHORE is not None and not isinstance(self.FLUOROPHORE, str):
            self.FLUOROPHORE = str(self.FLUOROPHORE)

        if self.CLONE is not None and not isinstance(self.CLONE, str):
            self.CLONE = str(self.CLONE)

        if self.LOT is not None and not isinstance(self.LOT, str):
            self.LOT = str(self.LOT)

        if self.CATALOG_NUMBER is not None and not isinstance(self.CATALOG_NUMBER, str):
            self.CATALOG_NUMBER = str(self.CATALOG_NUMBER)

        if self.EXCITATION_WAVELENGTH is not None and not isinstance(self.EXCITATION_WAVELENGTH, float):
            self.EXCITATION_WAVELENGTH = float(self.EXCITATION_WAVELENGTH)

        if self.EMISSION_WAVELENGTH is not None and not isinstance(self.EMISSION_WAVELENGTH, float):
            self.EMISSION_WAVELENGTH = float(self.EMISSION_WAVELENGTH)

        if self.EXCITATION_BANDWIDTH is not None and not isinstance(self.EXCITATION_BANDWIDTH, float):
            self.EXCITATION_BANDWIDTH = float(self.EXCITATION_BANDWIDTH)

        if self.EMISSION_BANDWIDTH is not None and not isinstance(self.EMISSION_BANDWIDTH, float):
            self.EMISSION_BANDWIDTH = float(self.EMISSION_BANDWIDTH)

        if self.METAL_ISOTOPE_ELEMENT_ABBREVIATION is not None and not isinstance(self.METAL_ISOTOPE_ELEMENT_ABBREVIATION, MetalIsotopeElement):
            self.METAL_ISOTOPE_ELEMENT_ABBREVIATION = MetalIsotopeElement(self.METAL_ISOTOPE_ELEMENT_ABBREVIATION)

        if self.METAL_ISOTOPE_ELEMENT_MASS is not None and not isinstance(self.METAL_ISOTOPE_ELEMENT_MASS, int):
            self.METAL_ISOTOPE_ELEMENT_MASS = int(self.METAL_ISOTOPE_ELEMENT_MASS)

        if self.OLIGO_BARCODE_UPPER_STRAND is not None and not isinstance(self.OLIGO_BARCODE_UPPER_STRAND, str):
            self.OLIGO_BARCODE_UPPER_STRAND = str(self.OLIGO_BARCODE_UPPER_STRAND)

        if self.OLIGO_BARCODE_LOWER_STRAND is not None and not isinstance(self.OLIGO_BARCODE_LOWER_STRAND, str):
            self.OLIGO_BARCODE_LOWER_STRAND = str(self.OLIGO_BARCODE_LOWER_STRAND)

        if self.DILUTION is not None and not isinstance(self.DILUTION, str):
            self.DILUTION = str(self.DILUTION)

        if self.CONCENTRATION is not None and not isinstance(self.CONCENTRATION, str):
            self.CONCENTRATION = str(self.CONCENTRATION)

        super().__post_init__(**kwargs)


# Enumerations
class ImagingAssayType(EnumDefinitionImpl):

    CODEX = PermissibleValue(
        text="CODEX",
        description="CODEX imaging assay type")
    CyCIF = PermissibleValue(
        text="CyCIF",
        description="Cyclic Immunofluorescence imaging assay type")
    ExSeq = PermissibleValue(
        text="ExSeq",
        description="Expansion Sequencing imaging assay type")
    IHC = PermissibleValue(
        text="IHC",
        description="Immunohistochemistry imaging assay type")
    IMC = PermissibleValue(
        text="IMC",
        description="Imaging Mass Cytometry imaging assay type")
    MIBI = PermissibleValue(
        text="MIBI",
        description="Multiplexed Ion Beam Imaging imaging assay type")
    MERFISH = PermissibleValue(
        text="MERFISH",
        description="Multiplexed Error-Robust Fluorescence In Situ Hybridization imaging assay type")
    MxIF = PermissibleValue(
        text="MxIF",
        description="Multiplexed Immunofluorescence imaging assay type")
    mIHC = PermissibleValue(
        text="mIHC",
        description="Multiplexed Immunohistochemistry imaging assay type")
    SABER = PermissibleValue(
        text="SABER",
        description="Signal Amplification By Exchange Reaction imaging assay type")

    _defn = EnumDefinition(
        name="ImagingAssayType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GeoMX-DSP",
            PermissibleValue(
                text="GeoMX-DSP",
                description="GeoMX Digital Spatial Profiling imaging assay type"))
        setattr(cls, "H&E",
            PermissibleValue(
                text="H&E",
                description="Hematoxylin and Eosin imaging assay type"))
        setattr(cls, "Not Applicable",
            PermissibleValue(
                text="Not Applicable",
                description="Imaging assay not applicable"))
        setattr(cls, "t-CyCIF",
            PermissibleValue(
                text="t-CyCIF",
                description="Tissue Cyclic Immunofluorescence imaging assay type"))

class MatrixTypeEnum(EnumDefinitionImpl):

    Other = PermissibleValue(
        text="Other",
        description="Other normalization method")

    _defn = EnumDefinition(
        name="MatrixTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Raw Counts",
            PermissibleValue(
                text="Raw Counts",
                description="Raw count matrix"))
        setattr(cls, "Normalized Counts",
            PermissibleValue(
                text="Normalized Counts",
                description="Normalized count matrix"))
        setattr(cls, "Scaled Counts",
            PermissibleValue(
                text="Scaled Counts",
                description="Scaled count matrix"))
        setattr(cls, "Log Normalized",
            PermissibleValue(
                text="Log Normalized",
                description="Log normalized counts"))
        setattr(cls, "Z-Score Normalized",
            PermissibleValue(
                text="Z-Score Normalized",
                description="Z-score normalized values"))

class DeIdentificationMethodType(EnumDefinitionImpl):

    Automatic = PermissibleValue(
        text="Automatic",
        description="Automatic de-identification method")
    Manual = PermissibleValue(
        text="Manual",
        description="Manual de-identification method")
    Semiautomatic = PermissibleValue(
        text="Semiautomatic",
        description="Semi-automatic de-identification method")

    _defn = EnumDefinition(
        name="DeIdentificationMethodType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Not Applicable",
            PermissibleValue(
                text="Not Applicable",
                description="De-identification not applicable"))

class ImageModality(EnumDefinitionImpl):

    SM = PermissibleValue(
        text="SM",
        description="Slide Microscopy")

    _defn = EnumDefinition(
        name="ImageModality",
    )

class StainingMethod(EnumDefinitionImpl):

    CODEX = PermissibleValue(
        text="CODEX",
        description="CODEX staining method")
    CyCIF = PermissibleValue(
        text="CyCIF",
        description="Cyclic Immunofluorescence staining method")
    ExSeq = PermissibleValue(
        text="ExSeq",
        description="Expansion Sequencing staining method")
    IHC = PermissibleValue(
        text="IHC",
        description="Immunohistochemistry staining method")
    IMC = PermissibleValue(
        text="IMC",
        description="Imaging Mass Cytometry staining method")
    MERFISH = PermissibleValue(
        text="MERFISH",
        description="Multiplexed Error-Robust Fluorescence In Situ Hybridization staining method")
    MIBI = PermissibleValue(
        text="MIBI",
        description="Multiplexed Ion Beam Imaging staining method")
    MxIF = PermissibleValue(
        text="MxIF",
        description="Multiplexed Immunofluorescence staining method")
    SABER = PermissibleValue(
        text="SABER",
        description="Signal Amplification By Exchange Reaction staining method")
    mIHC = PermissibleValue(
        text="mIHC",
        description="Multiplexed Immunohistochemistry staining method")

    _defn = EnumDefinition(
        name="StainingMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GeoMX-DSP",
            PermissibleValue(
                text="GeoMX-DSP",
                description="GeoMX Digital Spatial Profiling staining method"))
        setattr(cls, "H&E",
            PermissibleValue(
                text="H&E",
                description="Hematoxylin and Eosin staining method"))
        setattr(cls, "Not Applicable",
            PermissibleValue(
                text="Not Applicable",
                description="Staining not applicable"))
        setattr(cls, "t-CyCIF",
            PermissibleValue(
                text="t-CyCIF",
                description="Tissue Cyclic Immunofluorescence staining method"))

class ImmersionMedium(EnumDefinitionImpl):

    Air = PermissibleValue(
        text="Air",
        description="Air immersion medium")
    Glycerol = PermissibleValue(
        text="Glycerol",
        description="Glycerol immersion medium")
    Oil = PermissibleValue(
        text="Oil",
        description="Oil immersion medium")
    Other = PermissibleValue(
        text="Other",
        description="Other immersion medium")
    Water = PermissibleValue(
        text="Water",
        description="Water immersion medium")

    _defn = EnumDefinition(
        name="ImmersionMedium",
    )

class ExperimentalStrategyAndDataSubtypes(EnumDefinitionImpl):

    Pathological = PermissibleValue(
        text="Pathological",
        description="Pathological experimental strategy and data subtype")

    _defn = EnumDefinition(
        name="ExperimentalStrategyAndDataSubtypes",
    )

class License(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="License",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "CC BY 4.0",
            PermissibleValue(
                text="CC BY 4.0",
                description="Creative Commons Attribution 4.0 International License"))

class Species(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="Species",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "9606 (Homo sapiens)",
            PermissibleValue(
                text="9606 (Homo sapiens)",
                description="NCBI Taxonomy ID for Homo sapiens"))

class MetalIsotopeElement(EnumDefinitionImpl):

    H = PermissibleValue(
        text="H",
        description="Hydrogen")
    He = PermissibleValue(
        text="He",
        description="Helium")
    Li = PermissibleValue(
        text="Li",
        description="Lithium")
    Be = PermissibleValue(
        text="Be",
        description="Beryllium")
    B = PermissibleValue(
        text="B",
        description="Boron")
    C = PermissibleValue(
        text="C",
        description="Carbon")
    N = PermissibleValue(
        text="N",
        description="Nitrogen")
    O = PermissibleValue(
        text="O",
        description="Oxygen")
    F = PermissibleValue(
        text="F",
        description="Fluorine")
    Ne = PermissibleValue(
        text="Ne",
        description="Neon")
    Na = PermissibleValue(
        text="Na",
        description="Sodium")
    Mg = PermissibleValue(
        text="Mg",
        description="Magnesium")
    Al = PermissibleValue(
        text="Al",
        description="Aluminum")
    Si = PermissibleValue(
        text="Si",
        description="Silicon")
    P = PermissibleValue(
        text="P",
        description="Phosphorus")
    S = PermissibleValue(
        text="S",
        description="Sulfur")
    Cl = PermissibleValue(
        text="Cl",
        description="Chlorine")
    Ar = PermissibleValue(
        text="Ar",
        description="Argon")
    K = PermissibleValue(
        text="K",
        description="Potassium")
    Ca = PermissibleValue(
        text="Ca",
        description="Calcium")
    Sc = PermissibleValue(
        text="Sc",
        description="Scandium")
    Ti = PermissibleValue(
        text="Ti",
        description="Titanium")
    V = PermissibleValue(
        text="V",
        description="Vanadium")
    Cr = PermissibleValue(
        text="Cr",
        description="Chromium")
    Mn = PermissibleValue(
        text="Mn",
        description="Manganese")
    Fe = PermissibleValue(
        text="Fe",
        description="Iron")
    Co = PermissibleValue(
        text="Co",
        description="Cobalt")
    Ni = PermissibleValue(
        text="Ni",
        description="Nickel")
    Cu = PermissibleValue(
        text="Cu",
        description="Copper")
    Zn = PermissibleValue(
        text="Zn",
        description="Zinc")
    Ga = PermissibleValue(
        text="Ga",
        description="Gallium")
    Ge = PermissibleValue(
        text="Ge",
        description="Germanium")
    As = PermissibleValue(
        text="As",
        description="Arsenic")
    Se = PermissibleValue(
        text="Se",
        description="Selenium")
    Br = PermissibleValue(
        text="Br",
        description="Bromine")
    Kr = PermissibleValue(
        text="Kr",
        description="Krypton")
    Rb = PermissibleValue(
        text="Rb",
        description="Rubidium")
    Sr = PermissibleValue(
        text="Sr",
        description="Strontium")
    Y = PermissibleValue(
        text="Y",
        description="Yttrium")
    Zr = PermissibleValue(
        text="Zr",
        description="Zirconium")
    Nb = PermissibleValue(
        text="Nb",
        description="Niobium")
    Mo = PermissibleValue(
        text="Mo",
        description="Molybdenum")
    Tc = PermissibleValue(
        text="Tc",
        description="Technetium")
    Ru = PermissibleValue(
        text="Ru",
        description="Ruthenium")
    Rh = PermissibleValue(
        text="Rh",
        description="Rhodium")
    Pd = PermissibleValue(
        text="Pd",
        description="Palladium")
    Ag = PermissibleValue(
        text="Ag",
        description="Silver")
    Cd = PermissibleValue(
        text="Cd",
        description="Cadmium")
    In = PermissibleValue(
        text="In",
        description="Indium")
    Sn = PermissibleValue(
        text="Sn",
        description="Tin")
    Sb = PermissibleValue(
        text="Sb",
        description="Antimony")
    Te = PermissibleValue(
        text="Te",
        description="Tellurium")
    I = PermissibleValue(
        text="I",
        description="Iodine")
    Xe = PermissibleValue(
        text="Xe",
        description="Xenon")
    Cs = PermissibleValue(
        text="Cs",
        description="Cesium")
    Ba = PermissibleValue(
        text="Ba",
        description="Barium")
    La = PermissibleValue(
        text="La",
        description="Lanthanum")
    Ce = PermissibleValue(
        text="Ce",
        description="Cerium")
    Pr = PermissibleValue(
        text="Pr",
        description="Praseodymium")
    Nd = PermissibleValue(
        text="Nd",
        description="Neodymium")
    Pm = PermissibleValue(
        text="Pm",
        description="Promethium")
    Sm = PermissibleValue(
        text="Sm",
        description="Samarium")
    Eu = PermissibleValue(
        text="Eu",
        description="Europium")
    Gd = PermissibleValue(
        text="Gd",
        description="Gadolinium")
    Tb = PermissibleValue(
        text="Tb",
        description="Terbium")
    Dy = PermissibleValue(
        text="Dy",
        description="Dysprosium")
    Ho = PermissibleValue(
        text="Ho",
        description="Holmium")
    Er = PermissibleValue(
        text="Er",
        description="Erbium")
    Tm = PermissibleValue(
        text="Tm",
        description="Thulium")
    Yb = PermissibleValue(
        text="Yb",
        description="Ytterbium")
    Lu = PermissibleValue(
        text="Lu",
        description="Lutetium")
    Hf = PermissibleValue(
        text="Hf",
        description="Hafnium")
    Ta = PermissibleValue(
        text="Ta",
        description="Tantalum")
    W = PermissibleValue(
        text="W",
        description="Tungsten")
    Re = PermissibleValue(
        text="Re",
        description="Rhenium")
    Os = PermissibleValue(
        text="Os",
        description="Osmium")
    Ir = PermissibleValue(
        text="Ir",
        description="Iridium")
    Pt = PermissibleValue(
        text="Pt",
        description="Platinum")
    Au = PermissibleValue(
        text="Au",
        description="Gold")
    Hg = PermissibleValue(
        text="Hg",
        description="Mercury")
    Tl = PermissibleValue(
        text="Tl",
        description="Thallium")
    Pb = PermissibleValue(
        text="Pb",
        description="Lead")
    Bi = PermissibleValue(
        text="Bi",
        description="Bismuth")
    Po = PermissibleValue(
        text="Po",
        description="Polonium")
    At = PermissibleValue(
        text="At",
        description="Astatine")
    Rn = PermissibleValue(
        text="Rn",
        description="Radon")
    Fr = PermissibleValue(
        text="Fr",
        description="Francium")
    Ra = PermissibleValue(
        text="Ra",
        description="Radium")
    Ac = PermissibleValue(
        text="Ac",
        description="Actinium")
    Th = PermissibleValue(
        text="Th",
        description="Thorium")
    Pa = PermissibleValue(
        text="Pa",
        description="Protactinium")
    U = PermissibleValue(
        text="U",
        description="Uranium")
    Np = PermissibleValue(
        text="Np",
        description="Neptunium")
    Pu = PermissibleValue(
        text="Pu",
        description="Plutonium")
    Am = PermissibleValue(
        text="Am",
        description="Americium")
    Cm = PermissibleValue(
        text="Cm",
        description="Curium")
    Bk = PermissibleValue(
        text="Bk",
        description="Berkelium")
    Cf = PermissibleValue(
        text="Cf",
        description="Californium")
    Es = PermissibleValue(
        text="Es",
        description="Einsteinium")
    Fm = PermissibleValue(
        text="Fm",
        description="Fermium")
    Md = PermissibleValue(
        text="Md",
        description="Mendelevium")
    No = PermissibleValue(
        text="No",
        description="Nobelium")
    Lr = PermissibleValue(
        text="Lr",
        description="Lawrencium")
    Rf = PermissibleValue(
        text="Rf",
        description="Rutherfordium")
    Db = PermissibleValue(
        text="Db",
        description="Dubnium")
    Sg = PermissibleValue(
        text="Sg",
        description="Seaborgium")
    Bh = PermissibleValue(
        text="Bh",
        description="Bohrium")
    Hs = PermissibleValue(
        text="Hs",
        description="Hassium")
    Mt = PermissibleValue(
        text="Mt",
        description="Meitnerium")
    Ds = PermissibleValue(
        text="Ds",
        description="Darmstadtium")
    Rg = PermissibleValue(
        text="Rg",
        description="Roentgenium")
    Cn = PermissibleValue(
        text="Cn",
        description="Copernicium")
    Fl = PermissibleValue(
        text="Fl",
        description="Flerovium")
    Lv = PermissibleValue(
        text="Lv",
        description="Livermorium")
    Ts = PermissibleValue(
        text="Ts",
        description="Tennessine")
    Og = PermissibleValue(
        text="Og",
        description="Oganesson")

    _defn = EnumDefinition(
        name="MetalIsotopeElement",
    )

# Slots
class slots:
    pass

slots.caDSR_id = Slot(uri=HTAN.caDSR_id, name="caDSR_id", curie=HTAN.curie('caDSR_id'),
                   model_uri=HTAN.caDSR_id, domain=None, range=Optional[str])

slots.multiplexMicroscopyData__LEVEL_2_DATA = Slot(uri=HTAN.LEVEL_2_DATA, name="multiplexMicroscopyData__LEVEL_2_DATA", curie=HTAN.curie('LEVEL_2_DATA'),
                   model_uri=HTAN.multiplexMicroscopyData__LEVEL_2_DATA, domain=None, range=Optional[Union[str, MultiplexMicroscopyLevel2HTANDATAFILEID]])

slots.multiplexMicroscopyData__LEVEL_3_DATA = Slot(uri=HTAN.LEVEL_3_DATA, name="multiplexMicroscopyData__LEVEL_3_DATA", curie=HTAN.curie('LEVEL_3_DATA'),
                   model_uri=HTAN.multiplexMicroscopyData__LEVEL_3_DATA, domain=None, range=Optional[Union[str, MultiplexMicroscopyLevel3HTANDATAFILEID]])

slots.multiplexMicroscopyData__LEVEL_4_DATA = Slot(uri=HTAN.LEVEL_4_DATA, name="multiplexMicroscopyData__LEVEL_4_DATA", curie=HTAN.curie('LEVEL_4_DATA'),
                   model_uri=HTAN.multiplexMicroscopyData__LEVEL_4_DATA, domain=None, range=Optional[Union[str, MultiplexMicroscopyLevel4HTANDATAFILEID]])

slots.coreFileAttributes__FILENAME = Slot(uri=HTAN.FILENAME, name="coreFileAttributes__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.coreFileAttributes__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+[\\/]\S*$'))

slots.coreFileAttributes__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="coreFileAttributes__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.coreFileAttributes__FILE_FORMAT, domain=None, range=str)

slots.coreFileAttributes__HTAN_DATA_FILE_ID = Slot(uri=HTAN.HTAN_DATA_FILE_ID, name="coreFileAttributes__HTAN_DATA_FILE_ID", curie=HTAN.curie('HTAN_DATA_FILE_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_DATA_FILE_ID, domain=None, range=URIRef,
                   pattern=re.compile(r'^(HTA([1-9]|1[0-6]))_((EXT)?([0-9]\d*|0000))_([0-9]\d*|0000)$'))

slots.coreFileAttributes__HTAN_PARENT_ID = Slot(uri=HTAN.HTAN_PARENT_ID, name="coreFileAttributes__HTAN_PARENT_ID", curie=HTAN.curie('HTAN_PARENT_ID'),
                   model_uri=HTAN.coreFileAttributes__HTAN_PARENT_ID, domain=None, range=str,
                   pattern=re.compile(r'^(HTA20[0-9])(?:_0000)?(?:_\d+)?(?:_EXT\d+)?_(B|D)\d{1,50}$'))

slots.multiplexMicroscopyLevel2__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="multiplexMicroscopyLevel2__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(ome-tiff|ome\.tiff|qptiff|svs|tif|dcm|ndpi|vms|vmu|scn|mrxs|tiff|svslide|bit|czi)$'))

slots.multiplexMicroscopyLevel2__WORKING_DISTANCE = Slot(uri=HTAN.WORKING_DISTANCE, name="multiplexMicroscopyLevel2__WORKING_DISTANCE", curie=HTAN.curie('WORKING_DISTANCE'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__WORKING_DISTANCE, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel2__IMAGING_ASSAY_TYPE = Slot(uri=HTAN.IMAGING_ASSAY_TYPE, name="multiplexMicroscopyLevel2__IMAGING_ASSAY_TYPE", curie=HTAN.curie('IMAGING_ASSAY_TYPE'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__IMAGING_ASSAY_TYPE, domain=None, range=Union[str, "ImagingAssayType"])

slots.multiplexMicroscopyLevel2__PYRAMID = Slot(uri=HTAN.PYRAMID, name="multiplexMicroscopyLevel2__PYRAMID", curie=HTAN.curie('PYRAMID'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__PYRAMID, domain=None, range=Optional[Union[bool, Bool]])

slots.multiplexMicroscopyLevel2__PHYSICAL_SIZE_X = Slot(uri=HTAN.PHYSICAL_SIZE_X, name="multiplexMicroscopyLevel2__PHYSICAL_SIZE_X", curie=HTAN.curie('PHYSICAL_SIZE_X'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__PHYSICAL_SIZE_X, domain=None, range=float)

slots.multiplexMicroscopyLevel2__PHYSICAL_SIZE_Y = Slot(uri=HTAN.PHYSICAL_SIZE_Y, name="multiplexMicroscopyLevel2__PHYSICAL_SIZE_Y", curie=HTAN.curie('PHYSICAL_SIZE_Y'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__PHYSICAL_SIZE_Y, domain=None, range=float)

slots.multiplexMicroscopyLevel2__PHYSICAL_SIZE_Z = Slot(uri=HTAN.PHYSICAL_SIZE_Z, name="multiplexMicroscopyLevel2__PHYSICAL_SIZE_Z", curie=HTAN.curie('PHYSICAL_SIZE_Z'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__PHYSICAL_SIZE_Z, domain=None, range=float)

slots.multiplexMicroscopyLevel2__SIZE_C = Slot(uri=HTAN.SIZE_C, name="multiplexMicroscopyLevel2__SIZE_C", curie=HTAN.curie('SIZE_C'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__SIZE_C, domain=None, range=int)

slots.multiplexMicroscopyLevel2__SIZE_T = Slot(uri=HTAN.SIZE_T, name="multiplexMicroscopyLevel2__SIZE_T", curie=HTAN.curie('SIZE_T'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__SIZE_T, domain=None, range=int)

slots.multiplexMicroscopyLevel2__SIZE_X = Slot(uri=HTAN.SIZE_X, name="multiplexMicroscopyLevel2__SIZE_X", curie=HTAN.curie('SIZE_X'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__SIZE_X, domain=None, range=int)

slots.multiplexMicroscopyLevel2__SIZE_Y = Slot(uri=HTAN.SIZE_Y, name="multiplexMicroscopyLevel2__SIZE_Y", curie=HTAN.curie('SIZE_Y'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__SIZE_Y, domain=None, range=int)

slots.multiplexMicroscopyLevel2__SIZE_Z = Slot(uri=HTAN.SIZE_Z, name="multiplexMicroscopyLevel2__SIZE_Z", curie=HTAN.curie('SIZE_Z'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__SIZE_Z, domain=None, range=int)

slots.multiplexMicroscopyLevel2__CHANNEL_METADATA_ID = Slot(uri=HTAN.CHANNEL_METADATA_ID, name="multiplexMicroscopyLevel2__CHANNEL_METADATA_ID", curie=HTAN.curie('CHANNEL_METADATA_ID'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__CHANNEL_METADATA_ID, domain=None, range=str)

slots.multiplexMicroscopyLevel2__CHANNEL_METADATA = Slot(uri=HTAN.CHANNEL_METADATA, name="multiplexMicroscopyLevel2__CHANNEL_METADATA", curie=HTAN.curie('CHANNEL_METADATA'),
                   model_uri=HTAN.multiplexMicroscopyLevel2__CHANNEL_METADATA, domain=None, range=Optional[Union[Union[dict, ChannelMetadata], List[Union[dict, ChannelMetadata]]]])

slots.multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_TYPE = Slot(uri=HTAN.SEGMENTATION_WORKFLOW_TYPE, name="multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_TYPE", curie=HTAN.curie('SEGMENTATION_WORKFLOW_TYPE'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_TYPE, domain=None, range=str)

slots.multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_URL = Slot(uri=HTAN.SEGMENTATION_WORKFLOW_URL, name="multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_URL", curie=HTAN.curie('SEGMENTATION_WORKFLOW_URL'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_URL, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_VERSION = Slot(uri=HTAN.SEGMENTATION_WORKFLOW_VERSION, name="multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_VERSION", curie=HTAN.curie('SEGMENTATION_WORKFLOW_VERSION'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__SEGMENTATION_WORKFLOW_VERSION, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel3__SEGMENTATION_METHOD = Slot(uri=HTAN.SEGMENTATION_METHOD, name="multiplexMicroscopyLevel3__SEGMENTATION_METHOD", curie=HTAN.curie('SEGMENTATION_METHOD'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__SEGMENTATION_METHOD, domain=None, range=str)

slots.multiplexMicroscopyLevel3__SEGMENTATION_PARAMETERS = Slot(uri=HTAN.SEGMENTATION_PARAMETERS, name="multiplexMicroscopyLevel3__SEGMENTATION_PARAMETERS", curie=HTAN.curie('SEGMENTATION_PARAMETERS'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__SEGMENTATION_PARAMETERS, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel3__SEGMENTATION_ANNOTATION_TYPE = Slot(uri=HTAN.SEGMENTATION_ANNOTATION_TYPE, name="multiplexMicroscopyLevel3__SEGMENTATION_ANNOTATION_TYPE", curie=HTAN.curie('SEGMENTATION_ANNOTATION_TYPE'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__SEGMENTATION_ANNOTATION_TYPE, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel3__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="multiplexMicroscopyLevel3__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.multiplexMicroscopyLevel3__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(ome-tiff|ome\.tiff)$'))

slots.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_TYPE = Slot(uri=HTAN.FEATURE_EXTRACTION_WORKFLOW_TYPE, name="multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_TYPE", curie=HTAN.curie('FEATURE_EXTRACTION_WORKFLOW_TYPE'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_TYPE, domain=None, range=str)

slots.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_URL = Slot(uri=HTAN.FEATURE_EXTRACTION_WORKFLOW_URL, name="multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_URL", curie=HTAN.curie('FEATURE_EXTRACTION_WORKFLOW_URL'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_URL, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_VERSION = Slot(uri=HTAN.FEATURE_EXTRACTION_WORKFLOW_VERSION, name="multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_VERSION", curie=HTAN.curie('FEATURE_EXTRACTION_WORKFLOW_VERSION'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_WORKFLOW_VERSION, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel4__MATRIX_TYPE = Slot(uri=HTAN.MATRIX_TYPE, name="multiplexMicroscopyLevel4__MATRIX_TYPE", curie=HTAN.curie('MATRIX_TYPE'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__MATRIX_TYPE, domain=None, range=Union[str, "MatrixTypeEnum"])

slots.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_METHOD = Slot(uri=HTAN.FEATURE_EXTRACTION_METHOD, name="multiplexMicroscopyLevel4__FEATURE_EXTRACTION_METHOD", curie=HTAN.curie('FEATURE_EXTRACTION_METHOD'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_METHOD, domain=None, range=str)

slots.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_PARAMETERS = Slot(uri=HTAN.FEATURE_EXTRACTION_PARAMETERS, name="multiplexMicroscopyLevel4__FEATURE_EXTRACTION_PARAMETERS", curie=HTAN.curie('FEATURE_EXTRACTION_PARAMETERS'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__FEATURE_EXTRACTION_PARAMETERS, domain=None, range=Optional[str])

slots.multiplexMicroscopyLevel4__NUMBER_OF_FEATURES = Slot(uri=HTAN.NUMBER_OF_FEATURES, name="multiplexMicroscopyLevel4__NUMBER_OF_FEATURES", curie=HTAN.curie('NUMBER_OF_FEATURES'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__NUMBER_OF_FEATURES, domain=None, range=Optional[int])

slots.multiplexMicroscopyLevel4__NUMBER_OF_OBJECTS = Slot(uri=HTAN.NUMBER_OF_OBJECTS, name="multiplexMicroscopyLevel4__NUMBER_OF_OBJECTS", curie=HTAN.curie('NUMBER_OF_OBJECTS'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__NUMBER_OF_OBJECTS, domain=None, range=Optional[int])

slots.multiplexMicroscopyLevel4__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="multiplexMicroscopyLevel4__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.multiplexMicroscopyLevel4__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(csv|h5ad)$'))

slots.baseImagingAttributes__EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES = Slot(uri=HTAN.EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES, name="baseImagingAttributes__EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES", curie=HTAN.curie('EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES'),
                   model_uri=HTAN.baseImagingAttributes__EXPERIMENTAL_STRATEGY_AND_DATA_SUBTYPES, domain=None, range=Union[str, "ExperimentalStrategyAndDataSubtypes"])

slots.baseImagingAttributes__DE_IDENTIFICATION_METHOD_TYPE = Slot(uri=HTAN.DE_IDENTIFICATION_METHOD_TYPE, name="baseImagingAttributes__DE_IDENTIFICATION_METHOD_TYPE", curie=HTAN.curie('DE_IDENTIFICATION_METHOD_TYPE'),
                   model_uri=HTAN.baseImagingAttributes__DE_IDENTIFICATION_METHOD_TYPE, domain=None, range=Union[str, "DeIdentificationMethodType"])

slots.baseImagingAttributes__DE_IDENTIFICATION_METHOD_DESCRIPTION = Slot(uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, name="baseImagingAttributes__DE_IDENTIFICATION_METHOD_DESCRIPTION", curie=HTAN.curie('DE_IDENTIFICATION_METHOD_DESCRIPTION'),
                   model_uri=HTAN.baseImagingAttributes__DE_IDENTIFICATION_METHOD_DESCRIPTION, domain=None, range=Optional[str])

slots.baseImagingAttributes__DE_IDENTIFICATION_SOFTWARE = Slot(uri=HTAN.DE_IDENTIFICATION_SOFTWARE, name="baseImagingAttributes__DE_IDENTIFICATION_SOFTWARE", curie=HTAN.curie('DE_IDENTIFICATION_SOFTWARE'),
                   model_uri=HTAN.baseImagingAttributes__DE_IDENTIFICATION_SOFTWARE, domain=None, range=Optional[str])

slots.baseImagingAttributes__LICENSE = Slot(uri=HTAN.LICENSE, name="baseImagingAttributes__LICENSE", curie=HTAN.curie('LICENSE'),
                   model_uri=HTAN.baseImagingAttributes__LICENSE, domain=None, range=Union[str, "License"])

slots.baseImagingAttributes__IMAGE_MODALITY = Slot(uri=HTAN.IMAGE_MODALITY, name="baseImagingAttributes__IMAGE_MODALITY", curie=HTAN.curie('IMAGE_MODALITY'),
                   model_uri=HTAN.baseImagingAttributes__IMAGE_MODALITY, domain=None, range=Union[str, "ImageModality"])

slots.baseImagingAttributes__IMAGING_EQUIPMENT_MANUFACTURER = Slot(uri=HTAN.IMAGING_EQUIPMENT_MANUFACTURER, name="baseImagingAttributes__IMAGING_EQUIPMENT_MANUFACTURER", curie=HTAN.curie('IMAGING_EQUIPMENT_MANUFACTURER'),
                   model_uri=HTAN.baseImagingAttributes__IMAGING_EQUIPMENT_MANUFACTURER, domain=None, range=str)

slots.baseImagingAttributes__IMAGING_EQUIPMENT_MODEL = Slot(uri=HTAN.IMAGING_EQUIPMENT_MODEL, name="baseImagingAttributes__IMAGING_EQUIPMENT_MODEL", curie=HTAN.curie('IMAGING_EQUIPMENT_MODEL'),
                   model_uri=HTAN.baseImagingAttributes__IMAGING_EQUIPMENT_MODEL, domain=None, range=Optional[str])

slots.baseImagingAttributes__IMAGING_SOFTWARE = Slot(uri=HTAN.IMAGING_SOFTWARE, name="baseImagingAttributes__IMAGING_SOFTWARE", curie=HTAN.curie('IMAGING_SOFTWARE'),
                   model_uri=HTAN.baseImagingAttributes__IMAGING_SOFTWARE, domain=None, range=Optional[str])

slots.baseImagingAttributes__CITATION_OR_DOI = Slot(uri=HTAN.CITATION_OR_DOI, name="baseImagingAttributes__CITATION_OR_DOI", curie=HTAN.curie('CITATION_OR_DOI'),
                   model_uri=HTAN.baseImagingAttributes__CITATION_OR_DOI, domain=None, range=str,
                   pattern=re.compile(r'^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$'))

slots.baseImagingAttributes__IMAGING_PROTOCOL = Slot(uri=HTAN.IMAGING_PROTOCOL, name="baseImagingAttributes__IMAGING_PROTOCOL", curie=HTAN.curie('IMAGING_PROTOCOL'),
                   model_uri=HTAN.baseImagingAttributes__IMAGING_PROTOCOL, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$'))

slots.baseImagingAttributes__STAINING_METHOD = Slot(uri=HTAN.STAINING_METHOD, name="baseImagingAttributes__STAINING_METHOD", curie=HTAN.curie('STAINING_METHOD'),
                   model_uri=HTAN.baseImagingAttributes__STAINING_METHOD, domain=None, range=Union[str, "StainingMethod"])

slots.baseImagingAttributes__OBJECTIVE = Slot(uri=HTAN.OBJECTIVE, name="baseImagingAttributes__OBJECTIVE", curie=HTAN.curie('OBJECTIVE'),
                   model_uri=HTAN.baseImagingAttributes__OBJECTIVE, domain=None, range=str)

slots.baseImagingAttributes__NOMINAL_MAGNIFICATION = Slot(uri=HTAN.NOMINAL_MAGNIFICATION, name="baseImagingAttributes__NOMINAL_MAGNIFICATION", curie=HTAN.curie('NOMINAL_MAGNIFICATION'),
                   model_uri=HTAN.baseImagingAttributes__NOMINAL_MAGNIFICATION, domain=None, range=int)

slots.baseImagingAttributes__IMMERSION = Slot(uri=HTAN.IMMERSION, name="baseImagingAttributes__IMMERSION", curie=HTAN.curie('IMMERSION'),
                   model_uri=HTAN.baseImagingAttributes__IMMERSION, domain=None, range=Optional[Union[str, "ImmersionMedium"]])

slots.baseImagingAttributes__LENS_NUMERICAL_APERTURE = Slot(uri=HTAN.LENS_NUMERICAL_APERTURE, name="baseImagingAttributes__LENS_NUMERICAL_APERTURE", curie=HTAN.curie('LENS_NUMERICAL_APERTURE'),
                   model_uri=HTAN.baseImagingAttributes__LENS_NUMERICAL_APERTURE, domain=None, range=Optional[float])

slots.baseImagingAttributes__PASSED_QC = Slot(uri=HTAN.PASSED_QC, name="baseImagingAttributes__PASSED_QC", curie=HTAN.curie('PASSED_QC'),
                   model_uri=HTAN.baseImagingAttributes__PASSED_QC, domain=None, range=Union[bool, Bool])

slots.baseImagingAttributes__QC_COMMENT = Slot(uri=HTAN.QC_COMMENT, name="baseImagingAttributes__QC_COMMENT", curie=HTAN.curie('QC_COMMENT'),
                   model_uri=HTAN.baseImagingAttributes__QC_COMMENT, domain=None, range=str)

slots.baseImagingAttributes__SPECIES = Slot(uri=HTAN.SPECIES, name="baseImagingAttributes__SPECIES", curie=HTAN.curie('SPECIES'),
                   model_uri=HTAN.baseImagingAttributes__SPECIES, domain=None, range=Union[str, "Species"])

slots.channelMetadata__CHANNEL_ID = Slot(uri=HTAN.CHANNEL_ID, name="channelMetadata__CHANNEL_ID", curie=HTAN.curie('CHANNEL_ID'),
                   model_uri=HTAN.channelMetadata__CHANNEL_ID, domain=None, range=str)

slots.channelMetadata__CHANNEL_NAME = Slot(uri=HTAN.CHANNEL_NAME, name="channelMetadata__CHANNEL_NAME", curie=HTAN.curie('CHANNEL_NAME'),
                   model_uri=HTAN.channelMetadata__CHANNEL_NAME, domain=None, range=str)

slots.channelMetadata__CYCLE_NUMBER = Slot(uri=HTAN.CYCLE_NUMBER, name="channelMetadata__CYCLE_NUMBER", curie=HTAN.curie('CYCLE_NUMBER'),
                   model_uri=HTAN.channelMetadata__CYCLE_NUMBER, domain=None, range=Optional[int])

slots.channelMetadata__SUB_CYCLE_NUMBER = Slot(uri=HTAN.SUB_CYCLE_NUMBER, name="channelMetadata__SUB_CYCLE_NUMBER", curie=HTAN.curie('SUB_CYCLE_NUMBER'),
                   model_uri=HTAN.channelMetadata__SUB_CYCLE_NUMBER, domain=None, range=Optional[int])

slots.channelMetadata__TARGET_NAME = Slot(uri=HTAN.TARGET_NAME, name="channelMetadata__TARGET_NAME", curie=HTAN.curie('TARGET_NAME'),
                   model_uri=HTAN.channelMetadata__TARGET_NAME, domain=None, range=Optional[str])

slots.channelMetadata__ANTIBODY_NAME = Slot(uri=HTAN.ANTIBODY_NAME, name="channelMetadata__ANTIBODY_NAME", curie=HTAN.curie('ANTIBODY_NAME'),
                   model_uri=HTAN.channelMetadata__ANTIBODY_NAME, domain=None, range=Optional[str])

slots.channelMetadata__RRID_IDENTIFIER = Slot(uri=HTAN.RRID_IDENTIFIER, name="channelMetadata__RRID_IDENTIFIER", curie=HTAN.curie('RRID_IDENTIFIER'),
                   model_uri=HTAN.channelMetadata__RRID_IDENTIFIER, domain=None, range=Optional[str],
                   pattern=re.compile(r'^RRID:AB_\d+$'))

slots.channelMetadata__FLUOROPHORE = Slot(uri=HTAN.FLUOROPHORE, name="channelMetadata__FLUOROPHORE", curie=HTAN.curie('FLUOROPHORE'),
                   model_uri=HTAN.channelMetadata__FLUOROPHORE, domain=None, range=Optional[str])

slots.channelMetadata__CLONE = Slot(uri=HTAN.CLONE, name="channelMetadata__CLONE", curie=HTAN.curie('CLONE'),
                   model_uri=HTAN.channelMetadata__CLONE, domain=None, range=Optional[str])

slots.channelMetadata__LOT = Slot(uri=HTAN.LOT, name="channelMetadata__LOT", curie=HTAN.curie('LOT'),
                   model_uri=HTAN.channelMetadata__LOT, domain=None, range=Optional[str])

slots.channelMetadata__CATALOG_NUMBER = Slot(uri=HTAN.CATALOG_NUMBER, name="channelMetadata__CATALOG_NUMBER", curie=HTAN.curie('CATALOG_NUMBER'),
                   model_uri=HTAN.channelMetadata__CATALOG_NUMBER, domain=None, range=Optional[str])

slots.channelMetadata__EXCITATION_WAVELENGTH = Slot(uri=HTAN.EXCITATION_WAVELENGTH, name="channelMetadata__EXCITATION_WAVELENGTH", curie=HTAN.curie('EXCITATION_WAVELENGTH'),
                   model_uri=HTAN.channelMetadata__EXCITATION_WAVELENGTH, domain=None, range=Optional[float])

slots.channelMetadata__EMISSION_WAVELENGTH = Slot(uri=HTAN.EMISSION_WAVELENGTH, name="channelMetadata__EMISSION_WAVELENGTH", curie=HTAN.curie('EMISSION_WAVELENGTH'),
                   model_uri=HTAN.channelMetadata__EMISSION_WAVELENGTH, domain=None, range=Optional[float])

slots.channelMetadata__EXCITATION_BANDWIDTH = Slot(uri=HTAN.EXCITATION_BANDWIDTH, name="channelMetadata__EXCITATION_BANDWIDTH", curie=HTAN.curie('EXCITATION_BANDWIDTH'),
                   model_uri=HTAN.channelMetadata__EXCITATION_BANDWIDTH, domain=None, range=Optional[float])

slots.channelMetadata__EMISSION_BANDWIDTH = Slot(uri=HTAN.EMISSION_BANDWIDTH, name="channelMetadata__EMISSION_BANDWIDTH", curie=HTAN.curie('EMISSION_BANDWIDTH'),
                   model_uri=HTAN.channelMetadata__EMISSION_BANDWIDTH, domain=None, range=Optional[float])

slots.channelMetadata__METAL_ISOTOPE_ELEMENT_ABBREVIATION = Slot(uri=HTAN.METAL_ISOTOPE_ELEMENT_ABBREVIATION, name="channelMetadata__METAL_ISOTOPE_ELEMENT_ABBREVIATION", curie=HTAN.curie('METAL_ISOTOPE_ELEMENT_ABBREVIATION'),
                   model_uri=HTAN.channelMetadata__METAL_ISOTOPE_ELEMENT_ABBREVIATION, domain=None, range=Optional[Union[str, "MetalIsotopeElement"]])

slots.channelMetadata__METAL_ISOTOPE_ELEMENT_MASS = Slot(uri=HTAN.METAL_ISOTOPE_ELEMENT_MASS, name="channelMetadata__METAL_ISOTOPE_ELEMENT_MASS", curie=HTAN.curie('METAL_ISOTOPE_ELEMENT_MASS'),
                   model_uri=HTAN.channelMetadata__METAL_ISOTOPE_ELEMENT_MASS, domain=None, range=Optional[int])

slots.channelMetadata__OLIGO_BARCODE_UPPER_STRAND = Slot(uri=HTAN.OLIGO_BARCODE_UPPER_STRAND, name="channelMetadata__OLIGO_BARCODE_UPPER_STRAND", curie=HTAN.curie('OLIGO_BARCODE_UPPER_STRAND'),
                   model_uri=HTAN.channelMetadata__OLIGO_BARCODE_UPPER_STRAND, domain=None, range=Optional[str])

slots.channelMetadata__OLIGO_BARCODE_LOWER_STRAND = Slot(uri=HTAN.OLIGO_BARCODE_LOWER_STRAND, name="channelMetadata__OLIGO_BARCODE_LOWER_STRAND", curie=HTAN.curie('OLIGO_BARCODE_LOWER_STRAND'),
                   model_uri=HTAN.channelMetadata__OLIGO_BARCODE_LOWER_STRAND, domain=None, range=Optional[str])

slots.channelMetadata__DILUTION = Slot(uri=HTAN.DILUTION, name="channelMetadata__DILUTION", curie=HTAN.curie('DILUTION'),
                   model_uri=HTAN.channelMetadata__DILUTION, domain=None, range=Optional[str])

slots.channelMetadata__CONCENTRATION = Slot(uri=HTAN.CONCENTRATION, name="channelMetadata__CONCENTRATION", curie=HTAN.curie('CONCENTRATION'),
                   model_uri=HTAN.channelMetadata__CONCENTRATION, domain=None, range=Optional[str])

slots.DE_IDENTIFICATION_METHOD_DESCRIPTION = Slot(uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, name="DE_IDENTIFICATION_METHOD_DESCRIPTION", curie=HTAN.curie('DE_IDENTIFICATION_METHOD_DESCRIPTION'),
                   model_uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, domain=None, range=Optional[str])

slots.BaseImagingAttributes_DE_IDENTIFICATION_METHOD_DESCRIPTION = Slot(uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, name="BaseImagingAttributes_DE_IDENTIFICATION_METHOD_DESCRIPTION", curie=HTAN.curie('DE_IDENTIFICATION_METHOD_DESCRIPTION'),
                   model_uri=HTAN.BaseImagingAttributes_DE_IDENTIFICATION_METHOD_DESCRIPTION, domain=BaseImagingAttributes, range=Optional[str])
