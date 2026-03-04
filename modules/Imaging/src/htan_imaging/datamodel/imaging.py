# Auto generated from imaging.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-04T17:39:15
# Schema: Imaging
#
# id: https://w3id.org/htan/imaging
# description: HTAN Base Imaging Data Model - Common attributes shared across all imaging modules (Digital Pathology, Multiplex Microscopy, etc.)
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
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = HTAN


# Types

# Class references
class CoreFileAttributesHTANDATAFILEID(extended_str):
    pass


class BaseImagingAttributesHTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


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
    HTAN_PARENT_ID: Union[str, List[str]] = None
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
    HAS_SLIDE_LABEL: Union[bool, Bool] = None
    DE_IDENTIFIED: Union[bool, Bool] = None
    DE_IDENTIFICATION_METHOD_DESCRIPTION: Optional[str] = None
    DE_IDENTIFICATION_SOFTWARE: Optional[str] = None
    IMAGING_EQUIPMENT_MODEL: Optional[str] = None
    IMAGING_SOFTWARE: Optional[str] = None
    IMAGING_PROTOCOL: Optional[str] = None
    IMMERSION: Optional[Union[str, "ImmersionMedium"]] = None
    LENS_NUMERICAL_APERTURE: Optional[float] = None
    SLIDE_LABEL_REDACTED: Optional[Union[bool, Bool]] = None

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

        if self._is_empty(self.HAS_SLIDE_LABEL):
            self.MissingRequiredField("HAS_SLIDE_LABEL")
        if not isinstance(self.HAS_SLIDE_LABEL, Bool):
            self.HAS_SLIDE_LABEL = Bool(self.HAS_SLIDE_LABEL)

        if self._is_empty(self.DE_IDENTIFIED):
            self.MissingRequiredField("DE_IDENTIFIED")
        if not isinstance(self.DE_IDENTIFIED, Bool):
            self.DE_IDENTIFIED = Bool(self.DE_IDENTIFIED)

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

        if self.SLIDE_LABEL_REDACTED is not None and not isinstance(self.SLIDE_LABEL_REDACTED, Bool):
            self.SLIDE_LABEL_REDACTED = Bool(self.SLIDE_LABEL_REDACTED)

        if self.DE_IDENTIFICATION_METHOD_DESCRIPTION is not None and not isinstance(self.DE_IDENTIFICATION_METHOD_DESCRIPTION, str):
            self.DE_IDENTIFICATION_METHOD_DESCRIPTION = str(self.DE_IDENTIFICATION_METHOD_DESCRIPTION)

        if self.SLIDE_LABEL_REDACTED is not None and not isinstance(self.SLIDE_LABEL_REDACTED, str):
            self.SLIDE_LABEL_REDACTED = str(self.SLIDE_LABEL_REDACTED)

        super().__post_init__(**kwargs)


# Enumerations
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

# Slots
class slots:
    pass

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
                   pattern=re.compile(r'^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$'))

slots.baseImagingAttributes__IMAGING_PROTOCOL = Slot(uri=HTAN.IMAGING_PROTOCOL, name="baseImagingAttributes__IMAGING_PROTOCOL", curie=HTAN.curie('IMAGING_PROTOCOL'),
                   model_uri=HTAN.baseImagingAttributes__IMAGING_PROTOCOL, domain=None, range=Optional[str],
                   pattern=re.compile(r'^(?:(?:https?)://)(?:\S+(?::\S*)?@)?(?:(?!(?:10|127)(?:\.\d{1,3}){3})(?!(?:169\.254|192\.168)(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]-*)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\uffff]{2,}))\.?)(?::\d{2,5})?(?:[/?#]\S*)?$'))

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

slots.baseImagingAttributes__HAS_SLIDE_LABEL = Slot(uri=HTAN.HAS_SLIDE_LABEL, name="baseImagingAttributes__HAS_SLIDE_LABEL", curie=HTAN.curie('HAS_SLIDE_LABEL'),
                   model_uri=HTAN.baseImagingAttributes__HAS_SLIDE_LABEL, domain=None, range=Union[bool, Bool])

slots.baseImagingAttributes__SLIDE_LABEL_REDACTED = Slot(uri=HTAN.SLIDE_LABEL_REDACTED, name="baseImagingAttributes__SLIDE_LABEL_REDACTED", curie=HTAN.curie('SLIDE_LABEL_REDACTED'),
                   model_uri=HTAN.baseImagingAttributes__SLIDE_LABEL_REDACTED, domain=None, range=Optional[Union[bool, Bool]])

slots.baseImagingAttributes__DE_IDENTIFIED = Slot(uri=HTAN.DE_IDENTIFIED, name="baseImagingAttributes__DE_IDENTIFIED", curie=HTAN.curie('DE_IDENTIFIED'),
                   model_uri=HTAN.baseImagingAttributes__DE_IDENTIFIED, domain=None, range=Union[bool, Bool])

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

slots.DE_IDENTIFICATION_METHOD_DESCRIPTION = Slot(uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, name="DE_IDENTIFICATION_METHOD_DESCRIPTION", curie=HTAN.curie('DE_IDENTIFICATION_METHOD_DESCRIPTION'),
                   model_uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, domain=None, range=Optional[str])

slots.SLIDE_LABEL_REDACTED = Slot(uri=HTAN.SLIDE_LABEL_REDACTED, name="SLIDE_LABEL_REDACTED", curie=HTAN.curie('SLIDE_LABEL_REDACTED'),
                   model_uri=HTAN.SLIDE_LABEL_REDACTED, domain=None, range=Optional[str])

slots.BaseImagingAttributes_DE_IDENTIFICATION_METHOD_DESCRIPTION = Slot(uri=HTAN.DE_IDENTIFICATION_METHOD_DESCRIPTION, name="BaseImagingAttributes_DE_IDENTIFICATION_METHOD_DESCRIPTION", curie=HTAN.curie('DE_IDENTIFICATION_METHOD_DESCRIPTION'),
                   model_uri=HTAN.BaseImagingAttributes_DE_IDENTIFICATION_METHOD_DESCRIPTION, domain=BaseImagingAttributes, range=Optional[str])

slots.BaseImagingAttributes_SLIDE_LABEL_REDACTED = Slot(uri=HTAN.SLIDE_LABEL_REDACTED, name="BaseImagingAttributes_SLIDE_LABEL_REDACTED", curie=HTAN.curie('SLIDE_LABEL_REDACTED'),
                   model_uri=HTAN.BaseImagingAttributes_SLIDE_LABEL_REDACTED, domain=BaseImagingAttributes, range=Optional[str])
