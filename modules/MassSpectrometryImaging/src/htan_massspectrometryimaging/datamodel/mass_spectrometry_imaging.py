# Auto generated from mass_spectrometry_imaging.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-07-21T19:03:19
# Schema: MassSpectrometryImaging
#
# id: https://w3id.org/htan/mass_spectrometry_imaging
# description: HTAN Mass Spectrometry Imaging (MSI) Data Model Schema for Phase 2 - All Levels
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


class MassSpectrometryImagingLevel1HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class MassSpectrometryImagingLevel2HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class MassSpectrometryImagingLevel3HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


class MassSpectrometryImagingLevel4HTANDATAFILEID(CoreFileAttributesHTANDATAFILEID):
    pass


@dataclass(repr=False)
class MassSpectrometryImagingData(YAMLRoot):
    """
    Container for all Mass Spectrometry Imaging data levels and the Molecular Assignments RecordSet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MassSpectrometryImagingData"]
    class_class_curie: ClassVar[str] = "htan:MassSpectrometryImagingData"
    class_name: ClassVar[str] = "MassSpectrometryImagingData"
    class_model_uri: ClassVar[URIRef] = HTAN.MassSpectrometryImagingData

    LEVEL_1_DATA: Optional[Union[dict, "MassSpectrometryImagingLevel1"]] = None
    LEVEL_2_DATA: Optional[Union[dict, "MassSpectrometryImagingLevel2"]] = None
    LEVEL_3_DATA: Optional[Union[dict, "MassSpectrometryImagingLevel3"]] = None
    LEVEL_4_DATA: Optional[Union[dict, "MassSpectrometryImagingLevel4"]] = None
    MOLECULAR_ASSIGNMENTS: Optional[Union[Union[dict, "MolecularAssignment"], List[Union[dict, "MolecularAssignment"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.LEVEL_1_DATA is not None and not isinstance(self.LEVEL_1_DATA, MassSpectrometryImagingLevel1):
            self.LEVEL_1_DATA = MassSpectrometryImagingLevel1(**as_dict(self.LEVEL_1_DATA))

        if self.LEVEL_2_DATA is not None and not isinstance(self.LEVEL_2_DATA, MassSpectrometryImagingLevel2):
            self.LEVEL_2_DATA = MassSpectrometryImagingLevel2(**as_dict(self.LEVEL_2_DATA))

        if self.LEVEL_3_DATA is not None and not isinstance(self.LEVEL_3_DATA, MassSpectrometryImagingLevel3):
            self.LEVEL_3_DATA = MassSpectrometryImagingLevel3(**as_dict(self.LEVEL_3_DATA))

        if self.LEVEL_4_DATA is not None and not isinstance(self.LEVEL_4_DATA, MassSpectrometryImagingLevel4):
            self.LEVEL_4_DATA = MassSpectrometryImagingLevel4(**as_dict(self.LEVEL_4_DATA))

        if not isinstance(self.MOLECULAR_ASSIGNMENTS, list):
            self.MOLECULAR_ASSIGNMENTS = [self.MOLECULAR_ASSIGNMENTS] if self.MOLECULAR_ASSIGNMENTS is not None else []
        self.MOLECULAR_ASSIGNMENTS = [v if isinstance(v, MolecularAssignment) else MolecularAssignment(**as_dict(v)) for v in self.MOLECULAR_ASSIGNMENTS]

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
class MassSpectrometryImagingLevel1(CoreFileAttributes):
    """
    Level 1 raw spectral data - continuous (profile) imzML acquisition annotations. The paired .ibd binary is an
    unannotated companion carrying only CoreFileAttributes.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MassSpectrometryImagingLevel1"]
    class_class_curie: ClassVar[str] = "htan:MassSpectrometryImagingLevel1"
    class_name: ClassVar[str] = "MassSpectrometryImagingLevel1"
    class_model_uri: ClassVar[URIRef] = HTAN.MassSpectrometryImagingLevel1

    HTAN_DATA_FILE_ID: Union[str, MassSpectrometryImagingLevel1HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    MS_IONIZATION_TECHNIQUE: Union[str, "MsIonizationTechniqueEnum"] = None
    MASS_ANALYZER_TYPE: Union[str, "MassAnalyzerTypeEnum"] = None
    MASS_ANALYSIS_POLARITY: Union[str, "MassAnalysisPolarityEnum"] = None
    ANALYTE_CLASS: Union[Union[str, "AnalyteClassEnum"], List[Union[str, "AnalyteClassEnum"]]] = None
    IS_TARGETED: Union[bool, Bool] = None
    ACQUISITION_INSTRUMENT_VENDOR: str = None
    ACQUISITION_INSTRUMENT_MODEL: str = None
    PIXEL_SIZE_X_UM: float = None
    PIXEL_SIZE_Y_UM: float = None
    MASS_TO_CHARGE_RANGE_LOW_VALUE: float = None
    MASS_TO_CHARGE_RANGE_HIGH_VALUE: float = None
    ION_MOBILITY: Union[bool, Bool] = None
    SPECTRUM_TYPE: Union[str, "SpectrumTypeEnum"] = None
    MASS_RESOLVING_POWER: float = None
    MS_SCAN_MODE: Union[str, "MsScanModeEnum"] = None
    CALIBRATION_TYPE: Union[str, "CalibrationTypeEnum"] = None
    CALIBRANT_MASSES: str = None
    TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE: float = None
    TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT: Union[str, "TimeUnitEnum"] = None
    SOFTWARE_AND_VERSION: str = None
    IBD_FILE_UUID: str = None
    PASSED_QC: Union[bool, Bool] = None
    MASS_TO_CHARGE_RESOLVING_POWER: Optional[float] = None
    PROTOCOL_LINK: Optional[str] = None
    PREPARATION_MATRIX: Optional[Union[str, "PreparationMatrixEnum"]] = None
    MATRIX_DEPOSITION_METHOD: Optional[Union[str, "MatrixDepositionMethodEnum"]] = None
    PREPARATION_INSTRUMENT_VENDOR: Optional[str] = None
    PREPARATION_INSTRUMENT_MODEL: Optional[str] = None
    ANALYTE_ACQUISITION_ORDER: Optional[int] = None
    PRE_ACQUISITION_TREATMENT: Optional[Union[str, "PreAcquisitionTreatmentEnum"]] = None
    QC_COMMENT: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MassSpectrometryImagingLevel1HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MassSpectrometryImagingLevel1HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.MS_IONIZATION_TECHNIQUE):
            self.MissingRequiredField("MS_IONIZATION_TECHNIQUE")
        if not isinstance(self.MS_IONIZATION_TECHNIQUE, MsIonizationTechniqueEnum):
            self.MS_IONIZATION_TECHNIQUE = MsIonizationTechniqueEnum(self.MS_IONIZATION_TECHNIQUE)

        if self._is_empty(self.MASS_ANALYZER_TYPE):
            self.MissingRequiredField("MASS_ANALYZER_TYPE")
        if not isinstance(self.MASS_ANALYZER_TYPE, MassAnalyzerTypeEnum):
            self.MASS_ANALYZER_TYPE = MassAnalyzerTypeEnum(self.MASS_ANALYZER_TYPE)

        if self._is_empty(self.MASS_ANALYSIS_POLARITY):
            self.MissingRequiredField("MASS_ANALYSIS_POLARITY")
        if not isinstance(self.MASS_ANALYSIS_POLARITY, MassAnalysisPolarityEnum):
            self.MASS_ANALYSIS_POLARITY = MassAnalysisPolarityEnum(self.MASS_ANALYSIS_POLARITY)

        if self._is_empty(self.ANALYTE_CLASS):
            self.MissingRequiredField("ANALYTE_CLASS")
        if not isinstance(self.ANALYTE_CLASS, list):
            self.ANALYTE_CLASS = [self.ANALYTE_CLASS] if self.ANALYTE_CLASS is not None else []
        self.ANALYTE_CLASS = [v if isinstance(v, AnalyteClassEnum) else AnalyteClassEnum(v) for v in self.ANALYTE_CLASS]

        if self._is_empty(self.IS_TARGETED):
            self.MissingRequiredField("IS_TARGETED")
        if not isinstance(self.IS_TARGETED, Bool):
            self.IS_TARGETED = Bool(self.IS_TARGETED)

        if self._is_empty(self.ACQUISITION_INSTRUMENT_VENDOR):
            self.MissingRequiredField("ACQUISITION_INSTRUMENT_VENDOR")
        if not isinstance(self.ACQUISITION_INSTRUMENT_VENDOR, str):
            self.ACQUISITION_INSTRUMENT_VENDOR = str(self.ACQUISITION_INSTRUMENT_VENDOR)

        if self._is_empty(self.ACQUISITION_INSTRUMENT_MODEL):
            self.MissingRequiredField("ACQUISITION_INSTRUMENT_MODEL")
        if not isinstance(self.ACQUISITION_INSTRUMENT_MODEL, str):
            self.ACQUISITION_INSTRUMENT_MODEL = str(self.ACQUISITION_INSTRUMENT_MODEL)

        if self._is_empty(self.PIXEL_SIZE_X_UM):
            self.MissingRequiredField("PIXEL_SIZE_X_UM")
        if not isinstance(self.PIXEL_SIZE_X_UM, float):
            self.PIXEL_SIZE_X_UM = float(self.PIXEL_SIZE_X_UM)

        if self._is_empty(self.PIXEL_SIZE_Y_UM):
            self.MissingRequiredField("PIXEL_SIZE_Y_UM")
        if not isinstance(self.PIXEL_SIZE_Y_UM, float):
            self.PIXEL_SIZE_Y_UM = float(self.PIXEL_SIZE_Y_UM)

        if self._is_empty(self.MASS_TO_CHARGE_RANGE_LOW_VALUE):
            self.MissingRequiredField("MASS_TO_CHARGE_RANGE_LOW_VALUE")
        if not isinstance(self.MASS_TO_CHARGE_RANGE_LOW_VALUE, float):
            self.MASS_TO_CHARGE_RANGE_LOW_VALUE = float(self.MASS_TO_CHARGE_RANGE_LOW_VALUE)

        if self._is_empty(self.MASS_TO_CHARGE_RANGE_HIGH_VALUE):
            self.MissingRequiredField("MASS_TO_CHARGE_RANGE_HIGH_VALUE")
        if not isinstance(self.MASS_TO_CHARGE_RANGE_HIGH_VALUE, float):
            self.MASS_TO_CHARGE_RANGE_HIGH_VALUE = float(self.MASS_TO_CHARGE_RANGE_HIGH_VALUE)

        if self._is_empty(self.ION_MOBILITY):
            self.MissingRequiredField("ION_MOBILITY")
        if not isinstance(self.ION_MOBILITY, Bool):
            self.ION_MOBILITY = Bool(self.ION_MOBILITY)

        if self._is_empty(self.SPECTRUM_TYPE):
            self.MissingRequiredField("SPECTRUM_TYPE")
        if not isinstance(self.SPECTRUM_TYPE, SpectrumTypeEnum):
            self.SPECTRUM_TYPE = SpectrumTypeEnum(self.SPECTRUM_TYPE)

        if self._is_empty(self.MASS_RESOLVING_POWER):
            self.MissingRequiredField("MASS_RESOLVING_POWER")
        if not isinstance(self.MASS_RESOLVING_POWER, float):
            self.MASS_RESOLVING_POWER = float(self.MASS_RESOLVING_POWER)

        if self._is_empty(self.MS_SCAN_MODE):
            self.MissingRequiredField("MS_SCAN_MODE")
        if not isinstance(self.MS_SCAN_MODE, MsScanModeEnum):
            self.MS_SCAN_MODE = MsScanModeEnum(self.MS_SCAN_MODE)

        if self._is_empty(self.CALIBRATION_TYPE):
            self.MissingRequiredField("CALIBRATION_TYPE")
        if not isinstance(self.CALIBRATION_TYPE, CalibrationTypeEnum):
            self.CALIBRATION_TYPE = CalibrationTypeEnum(self.CALIBRATION_TYPE)

        if self._is_empty(self.CALIBRANT_MASSES):
            self.MissingRequiredField("CALIBRANT_MASSES")
        if not isinstance(self.CALIBRANT_MASSES, str):
            self.CALIBRANT_MASSES = str(self.CALIBRANT_MASSES)

        if self._is_empty(self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE):
            self.MissingRequiredField("TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE")
        if not isinstance(self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE, float):
            self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE = float(self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE)

        if self._is_empty(self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT):
            self.MissingRequiredField("TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT")
        if not isinstance(self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT, TimeUnitEnum):
            self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT = TimeUnitEnum(self.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT)

        if self._is_empty(self.SOFTWARE_AND_VERSION):
            self.MissingRequiredField("SOFTWARE_AND_VERSION")
        if not isinstance(self.SOFTWARE_AND_VERSION, str):
            self.SOFTWARE_AND_VERSION = str(self.SOFTWARE_AND_VERSION)

        if self._is_empty(self.IBD_FILE_UUID):
            self.MissingRequiredField("IBD_FILE_UUID")
        if not isinstance(self.IBD_FILE_UUID, str):
            self.IBD_FILE_UUID = str(self.IBD_FILE_UUID)

        if self._is_empty(self.PASSED_QC):
            self.MissingRequiredField("PASSED_QC")
        if not isinstance(self.PASSED_QC, Bool):
            self.PASSED_QC = Bool(self.PASSED_QC)

        if self.MASS_TO_CHARGE_RESOLVING_POWER is not None and not isinstance(self.MASS_TO_CHARGE_RESOLVING_POWER, float):
            self.MASS_TO_CHARGE_RESOLVING_POWER = float(self.MASS_TO_CHARGE_RESOLVING_POWER)

        if self.PROTOCOL_LINK is not None and not isinstance(self.PROTOCOL_LINK, str):
            self.PROTOCOL_LINK = str(self.PROTOCOL_LINK)

        if self.PREPARATION_MATRIX is not None and not isinstance(self.PREPARATION_MATRIX, PreparationMatrixEnum):
            self.PREPARATION_MATRIX = PreparationMatrixEnum(self.PREPARATION_MATRIX)

        if self.MATRIX_DEPOSITION_METHOD is not None and not isinstance(self.MATRIX_DEPOSITION_METHOD, MatrixDepositionMethodEnum):
            self.MATRIX_DEPOSITION_METHOD = MatrixDepositionMethodEnum(self.MATRIX_DEPOSITION_METHOD)

        if self.PREPARATION_INSTRUMENT_VENDOR is not None and not isinstance(self.PREPARATION_INSTRUMENT_VENDOR, str):
            self.PREPARATION_INSTRUMENT_VENDOR = str(self.PREPARATION_INSTRUMENT_VENDOR)

        if self.PREPARATION_INSTRUMENT_MODEL is not None and not isinstance(self.PREPARATION_INSTRUMENT_MODEL, str):
            self.PREPARATION_INSTRUMENT_MODEL = str(self.PREPARATION_INSTRUMENT_MODEL)

        if self.ANALYTE_ACQUISITION_ORDER is not None and not isinstance(self.ANALYTE_ACQUISITION_ORDER, int):
            self.ANALYTE_ACQUISITION_ORDER = int(self.ANALYTE_ACQUISITION_ORDER)

        if self.PRE_ACQUISITION_TREATMENT is not None and not isinstance(self.PRE_ACQUISITION_TREATMENT, PreAcquisitionTreatmentEnum):
            self.PRE_ACQUISITION_TREATMENT = PreAcquisitionTreatmentEnum(self.PRE_ACQUISITION_TREATMENT)

        if self.QC_COMMENT is not None and not isinstance(self.QC_COMMENT, str):
            self.QC_COMMENT = str(self.QC_COMMENT)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryImagingLevel2(CoreFileAttributes):
    """
    Level 2 processed spectral data - centroided imzML after baseline correction, peak picking, mass alignment, and
    normalization. The paired .ibd binary is an unannotated companion.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MassSpectrometryImagingLevel2"]
    class_class_curie: ClassVar[str] = "htan:MassSpectrometryImagingLevel2"
    class_name: ClassVar[str] = "MassSpectrometryImagingLevel2"
    class_model_uri: ClassVar[URIRef] = HTAN.MassSpectrometryImagingLevel2

    HTAN_DATA_FILE_ID: Union[str, MassSpectrometryImagingLevel2HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    SOFTWARE_AND_VERSION: str = None
    BASELINE_CORRECTION_METHOD: Union[str, "BaselineCorrectionMethodEnum"] = None
    PEAK_PICKING_METHOD: str = None
    PEAK_PICKING_SNR_THRESHOLD: float = None
    NORMALIZATION_METHOD: Union[str, "NormalizationMethodEnum"] = None
    MASS_ALIGNMENT_METHOD: str = None
    MASS_TOLERANCE_PPM: float = None
    MEDIAN_TIC: float = None
    TIC_CV: float = None
    MASS_ACCURACY_PPM: float = None
    PIXEL_COMPLETION_RATE: float = None
    NUM_DETECTED_PEAKS: int = None
    PASSED_QC: Union[bool, Bool] = None
    SMOOTHING_METHOD: Optional[Union[str, "SmoothingMethodEnum"]] = None
    PROTOCOL_LINK: Optional[str] = None
    QC_COMMENT: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MassSpectrometryImagingLevel2HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MassSpectrometryImagingLevel2HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.SOFTWARE_AND_VERSION):
            self.MissingRequiredField("SOFTWARE_AND_VERSION")
        if not isinstance(self.SOFTWARE_AND_VERSION, str):
            self.SOFTWARE_AND_VERSION = str(self.SOFTWARE_AND_VERSION)

        if self._is_empty(self.BASELINE_CORRECTION_METHOD):
            self.MissingRequiredField("BASELINE_CORRECTION_METHOD")
        if not isinstance(self.BASELINE_CORRECTION_METHOD, BaselineCorrectionMethodEnum):
            self.BASELINE_CORRECTION_METHOD = BaselineCorrectionMethodEnum(self.BASELINE_CORRECTION_METHOD)

        if self._is_empty(self.PEAK_PICKING_METHOD):
            self.MissingRequiredField("PEAK_PICKING_METHOD")
        if not isinstance(self.PEAK_PICKING_METHOD, str):
            self.PEAK_PICKING_METHOD = str(self.PEAK_PICKING_METHOD)

        if self._is_empty(self.PEAK_PICKING_SNR_THRESHOLD):
            self.MissingRequiredField("PEAK_PICKING_SNR_THRESHOLD")
        if not isinstance(self.PEAK_PICKING_SNR_THRESHOLD, float):
            self.PEAK_PICKING_SNR_THRESHOLD = float(self.PEAK_PICKING_SNR_THRESHOLD)

        if self._is_empty(self.NORMALIZATION_METHOD):
            self.MissingRequiredField("NORMALIZATION_METHOD")
        if not isinstance(self.NORMALIZATION_METHOD, NormalizationMethodEnum):
            self.NORMALIZATION_METHOD = NormalizationMethodEnum(self.NORMALIZATION_METHOD)

        if self._is_empty(self.MASS_ALIGNMENT_METHOD):
            self.MissingRequiredField("MASS_ALIGNMENT_METHOD")
        if not isinstance(self.MASS_ALIGNMENT_METHOD, str):
            self.MASS_ALIGNMENT_METHOD = str(self.MASS_ALIGNMENT_METHOD)

        if self._is_empty(self.MASS_TOLERANCE_PPM):
            self.MissingRequiredField("MASS_TOLERANCE_PPM")
        if not isinstance(self.MASS_TOLERANCE_PPM, float):
            self.MASS_TOLERANCE_PPM = float(self.MASS_TOLERANCE_PPM)

        if self._is_empty(self.MEDIAN_TIC):
            self.MissingRequiredField("MEDIAN_TIC")
        if not isinstance(self.MEDIAN_TIC, float):
            self.MEDIAN_TIC = float(self.MEDIAN_TIC)

        if self._is_empty(self.TIC_CV):
            self.MissingRequiredField("TIC_CV")
        if not isinstance(self.TIC_CV, float):
            self.TIC_CV = float(self.TIC_CV)

        if self._is_empty(self.MASS_ACCURACY_PPM):
            self.MissingRequiredField("MASS_ACCURACY_PPM")
        if not isinstance(self.MASS_ACCURACY_PPM, float):
            self.MASS_ACCURACY_PPM = float(self.MASS_ACCURACY_PPM)

        if self._is_empty(self.PIXEL_COMPLETION_RATE):
            self.MissingRequiredField("PIXEL_COMPLETION_RATE")
        if not isinstance(self.PIXEL_COMPLETION_RATE, float):
            self.PIXEL_COMPLETION_RATE = float(self.PIXEL_COMPLETION_RATE)

        if self._is_empty(self.NUM_DETECTED_PEAKS):
            self.MissingRequiredField("NUM_DETECTED_PEAKS")
        if not isinstance(self.NUM_DETECTED_PEAKS, int):
            self.NUM_DETECTED_PEAKS = int(self.NUM_DETECTED_PEAKS)

        if self._is_empty(self.PASSED_QC):
            self.MissingRequiredField("PASSED_QC")
        if not isinstance(self.PASSED_QC, Bool):
            self.PASSED_QC = Bool(self.PASSED_QC)

        if self.SMOOTHING_METHOD is not None and not isinstance(self.SMOOTHING_METHOD, SmoothingMethodEnum):
            self.SMOOTHING_METHOD = SmoothingMethodEnum(self.SMOOTHING_METHOD)

        if self.PROTOCOL_LINK is not None and not isinstance(self.PROTOCOL_LINK, str):
            self.PROTOCOL_LINK = str(self.PROTOCOL_LINK)

        if self.QC_COMMENT is not None and not isinstance(self.QC_COMMENT, str):
            self.QC_COMMENT = str(self.QC_COMMENT)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryImagingLevel3(CoreFileAttributes):
    """
    Level 3 annotation-filtered OME-TIFF. Channels include only annotated m/z values plus biologically relevant
    unknowns. Per-channel molecular detail is carried by the companion Molecular Assignments RecordSet.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MassSpectrometryImagingLevel3"]
    class_class_curie: ClassVar[str] = "htan:MassSpectrometryImagingLevel3"
    class_name: ClassVar[str] = "MassSpectrometryImagingLevel3"
    class_model_uri: ClassVar[URIRef] = HTAN.MassSpectrometryImagingLevel3

    HTAN_DATA_FILE_ID: Union[str, MassSpectrometryImagingLevel3HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    NUM_ANNOTATED_CHANNELS: int = None
    NUM_UNKNOWN_CHANNELS: int = None
    SOFTWARE_AND_VERSION: str = None
    PASSED_QC: Union[bool, Bool] = None
    PROTOCOL_LINK: Optional[str] = None
    QC_COMMENT: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MassSpectrometryImagingLevel3HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MassSpectrometryImagingLevel3HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.NUM_ANNOTATED_CHANNELS):
            self.MissingRequiredField("NUM_ANNOTATED_CHANNELS")
        if not isinstance(self.NUM_ANNOTATED_CHANNELS, int):
            self.NUM_ANNOTATED_CHANNELS = int(self.NUM_ANNOTATED_CHANNELS)

        if self._is_empty(self.NUM_UNKNOWN_CHANNELS):
            self.MissingRequiredField("NUM_UNKNOWN_CHANNELS")
        if not isinstance(self.NUM_UNKNOWN_CHANNELS, int):
            self.NUM_UNKNOWN_CHANNELS = int(self.NUM_UNKNOWN_CHANNELS)

        if self._is_empty(self.SOFTWARE_AND_VERSION):
            self.MissingRequiredField("SOFTWARE_AND_VERSION")
        if not isinstance(self.SOFTWARE_AND_VERSION, str):
            self.SOFTWARE_AND_VERSION = str(self.SOFTWARE_AND_VERSION)

        if self._is_empty(self.PASSED_QC):
            self.MissingRequiredField("PASSED_QC")
        if not isinstance(self.PASSED_QC, Bool):
            self.PASSED_QC = Bool(self.PASSED_QC)

        if self.PROTOCOL_LINK is not None and not isinstance(self.PROTOCOL_LINK, str):
            self.PROTOCOL_LINK = str(self.PROTOCOL_LINK)

        if self.QC_COMMENT is not None and not isinstance(self.QC_COMMENT, str):
            self.QC_COMMENT = str(self.QC_COMMENT)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MassSpectrometryImagingLevel4(CoreFileAttributes):
    """
    Level 4 segmented and region/cell-type quantified output (optional). Includes a segmentation mask OME-TIFF and/or
    a region quantification table.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MassSpectrometryImagingLevel4"]
    class_class_curie: ClassVar[str] = "htan:MassSpectrometryImagingLevel4"
    class_name: ClassVar[str] = "MassSpectrometryImagingLevel4"
    class_model_uri: ClassVar[URIRef] = HTAN.MassSpectrometryImagingLevel4

    HTAN_DATA_FILE_ID: Union[str, MassSpectrometryImagingLevel4HTANDATAFILEID] = None
    HTAN_PARENT_ID: Union[str, List[str]] = None
    FILE_FORMAT: str = None
    FILENAME: str = None
    SEGMENTATION_METHOD: str = None
    SEGMENTATION_CLASS_COUNT: int = None
    SEGMENTATION_REFERENCE_MODALITY: Union[str, "SegmentationReferenceModalityEnum"] = None
    PASSED_QC: Union[bool, Bool] = None
    QC_COMMENT: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, MassSpectrometryImagingLevel4HTANDATAFILEID):
            self.HTAN_DATA_FILE_ID = MassSpectrometryImagingLevel4HTANDATAFILEID(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.FILE_FORMAT):
            self.MissingRequiredField("FILE_FORMAT")
        if not isinstance(self.FILE_FORMAT, str):
            self.FILE_FORMAT = str(self.FILE_FORMAT)

        if self._is_empty(self.FILENAME):
            self.MissingRequiredField("FILENAME")
        if not isinstance(self.FILENAME, str):
            self.FILENAME = str(self.FILENAME)

        if self._is_empty(self.SEGMENTATION_METHOD):
            self.MissingRequiredField("SEGMENTATION_METHOD")
        if not isinstance(self.SEGMENTATION_METHOD, str):
            self.SEGMENTATION_METHOD = str(self.SEGMENTATION_METHOD)

        if self._is_empty(self.SEGMENTATION_CLASS_COUNT):
            self.MissingRequiredField("SEGMENTATION_CLASS_COUNT")
        if not isinstance(self.SEGMENTATION_CLASS_COUNT, int):
            self.SEGMENTATION_CLASS_COUNT = int(self.SEGMENTATION_CLASS_COUNT)

        if self._is_empty(self.SEGMENTATION_REFERENCE_MODALITY):
            self.MissingRequiredField("SEGMENTATION_REFERENCE_MODALITY")
        if not isinstance(self.SEGMENTATION_REFERENCE_MODALITY, SegmentationReferenceModalityEnum):
            self.SEGMENTATION_REFERENCE_MODALITY = SegmentationReferenceModalityEnum(self.SEGMENTATION_REFERENCE_MODALITY)

        if self._is_empty(self.PASSED_QC):
            self.MissingRequiredField("PASSED_QC")
        if not isinstance(self.PASSED_QC, Bool):
            self.PASSED_QC = Bool(self.PASSED_QC)

        if self.QC_COMMENT is not None and not isinstance(self.QC_COMMENT, str):
            self.QC_COMMENT = str(self.QC_COMMENT)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MolecularAssignment(YAMLRoot):
    """
    A single molecular assignment row corresponding to one OME-TIFF channel in a Level 3 file. The unique row key is
    (HTAN_DATA_FILE_ID, CHANNEL_INDEX). Channel count must equal RecordSet row count (enforced by the DCC validator).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HTAN["MolecularAssignment"]
    class_class_curie: ClassVar[str] = "htan:MolecularAssignment"
    class_name: ClassVar[str] = "MolecularAssignment"
    class_model_uri: ClassVar[URIRef] = HTAN.MolecularAssignment

    HTAN_DATA_FILE_ID: str = None
    CHANNEL_INDEX: int = None
    MZ_OBSERVED: float = None
    MOLECULAR_NAME: str = None
    SOFTWARE_AND_VERSION: str = None
    CONFIDENCE_LEVEL: int = None
    EVIDENCE_TYPE: Union[Union[str, "EvidenceTypeEnum"], List[Union[str, "EvidenceTypeEnum"]]] = None
    MZ_THEORETICAL: Optional[float] = None
    MASS_ERROR_PPM: Optional[float] = None
    MOLECULAR_FORMULA: Optional[str] = None
    ADDUCT: Optional[Union[str, "AdductEnum"]] = None
    DATABASE_SOURCE: Optional[Union[str, "DatabaseSourceEnum"]] = None
    DATABASE_ID: Optional[str] = None
    DATABASE_VERSION: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.HTAN_DATA_FILE_ID):
            self.MissingRequiredField("HTAN_DATA_FILE_ID")
        if not isinstance(self.HTAN_DATA_FILE_ID, str):
            self.HTAN_DATA_FILE_ID = str(self.HTAN_DATA_FILE_ID)

        if self._is_empty(self.CHANNEL_INDEX):
            self.MissingRequiredField("CHANNEL_INDEX")
        if not isinstance(self.CHANNEL_INDEX, int):
            self.CHANNEL_INDEX = int(self.CHANNEL_INDEX)

        if self._is_empty(self.MZ_OBSERVED):
            self.MissingRequiredField("MZ_OBSERVED")
        if not isinstance(self.MZ_OBSERVED, float):
            self.MZ_OBSERVED = float(self.MZ_OBSERVED)

        if self._is_empty(self.MOLECULAR_NAME):
            self.MissingRequiredField("MOLECULAR_NAME")
        if not isinstance(self.MOLECULAR_NAME, str):
            self.MOLECULAR_NAME = str(self.MOLECULAR_NAME)

        if self._is_empty(self.SOFTWARE_AND_VERSION):
            self.MissingRequiredField("SOFTWARE_AND_VERSION")
        if not isinstance(self.SOFTWARE_AND_VERSION, str):
            self.SOFTWARE_AND_VERSION = str(self.SOFTWARE_AND_VERSION)

        if self._is_empty(self.CONFIDENCE_LEVEL):
            self.MissingRequiredField("CONFIDENCE_LEVEL")
        if not isinstance(self.CONFIDENCE_LEVEL, int):
            self.CONFIDENCE_LEVEL = int(self.CONFIDENCE_LEVEL)

        if self._is_empty(self.EVIDENCE_TYPE):
            self.MissingRequiredField("EVIDENCE_TYPE")
        if not isinstance(self.EVIDENCE_TYPE, list):
            self.EVIDENCE_TYPE = [self.EVIDENCE_TYPE] if self.EVIDENCE_TYPE is not None else []
        self.EVIDENCE_TYPE = [v if isinstance(v, EvidenceTypeEnum) else EvidenceTypeEnum(v) for v in self.EVIDENCE_TYPE]

        if self.MZ_THEORETICAL is not None and not isinstance(self.MZ_THEORETICAL, float):
            self.MZ_THEORETICAL = float(self.MZ_THEORETICAL)

        if self.MASS_ERROR_PPM is not None and not isinstance(self.MASS_ERROR_PPM, float):
            self.MASS_ERROR_PPM = float(self.MASS_ERROR_PPM)

        if self.MOLECULAR_FORMULA is not None and not isinstance(self.MOLECULAR_FORMULA, str):
            self.MOLECULAR_FORMULA = str(self.MOLECULAR_FORMULA)

        if self.ADDUCT is not None and not isinstance(self.ADDUCT, AdductEnum):
            self.ADDUCT = AdductEnum(self.ADDUCT)

        if self.DATABASE_SOURCE is not None and not isinstance(self.DATABASE_SOURCE, DatabaseSourceEnum):
            self.DATABASE_SOURCE = DatabaseSourceEnum(self.DATABASE_SOURCE)

        if self.DATABASE_ID is not None and not isinstance(self.DATABASE_ID, str):
            self.DATABASE_ID = str(self.DATABASE_ID)

        if self.DATABASE_VERSION is not None and not isinstance(self.DATABASE_VERSION, str):
            self.DATABASE_VERSION = str(self.DATABASE_VERSION)

        super().__post_init__(**kwargs)


# Enumerations
class MsIonizationTechniqueEnum(EnumDefinitionImpl):

    DESI = PermissibleValue(
        text="DESI",
        description="Desorption Electrospray Ionization - ambient spray ionization")
    IR_MALDESI = PermissibleValue(
        text="IR_MALDESI",
        description="Infrared MALDESI - IR laser ablation coupled with electrospray")
    MALDI = PermissibleValue(
        text="MALDI",
        description="Matrix-Assisted Laser Desorption/Ionization")
    MALDI_2 = PermissibleValue(
        text="MALDI_2",
        description="""MALDI with secondary post-ionization laser for enhanced sensitivity (Bruker timsTOF Flex MALDI-2 mode)""")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Ionization technique not listed; describe in PROTOCOL_LINK")
    SIMS = PermissibleValue(
        text="SIMS",
        description="Secondary Ion Mass Spectrometry - ion beam sputtering for sub-micron resolution")

    _defn = EnumDefinition(
        name="MsIonizationTechniqueEnum",
    )

class MassAnalyzerTypeEnum(EnumDefinitionImpl):

    FTICR = PermissibleValue(
        text="FTICR",
        description="Fourier-Transform Ion Cyclotron Resonance")
    ION_TRAP = PermissibleValue(
        text="ION_TRAP",
        description="Ion trap (linear or 3D)")
    ORBITRAP = PermissibleValue(
        text="ORBITRAP",
        description="Orbitrap electrostatic trap (Thermo)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Analyser type not listed")
    Q_TOF = PermissibleValue(
        text="Q_TOF",
        description="Quadrupole Time-of-Flight hybrid")
    TOF = PermissibleValue(
        text="TOF",
        description="Time-of-Flight mass analyser")
    TRIPLE_QUADRUPOLE = PermissibleValue(
        text="TRIPLE_QUADRUPOLE",
        description="Triple-quadrupole (tandem MS)")

    _defn = EnumDefinition(
        name="MassAnalyzerTypeEnum",
    )

class MassAnalysisPolarityEnum(EnumDefinitionImpl):

    BOTH = PermissibleValue(
        text="BOTH",
        description="""Dataset contains both positive and negative mode acquisitions (HTAN extension - not present in HuBMAP)""")
    NEG = PermissibleValue(
        text="NEG",
        description="Negative ionisation mode")
    POS = PermissibleValue(
        text="POS",
        description="Positive ionisation mode")

    _defn = EnumDefinition(
        name="MassAnalysisPolarityEnum",
    )

class AnalyteClassEnum(EnumDefinitionImpl):

    GLYCANS = PermissibleValue(
        text="GLYCANS",
        description="N-linked or O-linked glycans (e.g., PNGaseF-released)")
    LIPIDS = PermissibleValue(
        text="LIPIDS",
        description="Lipids and fatty acids")
    METABOLITES = PermissibleValue(
        text="METABOLITES",
        description="Small-molecule metabolites (non-lipid)")
    NUCLEIC_ACIDS = PermissibleValue(
        text="NUCLEIC_ACIDS",
        description="Oligonucleotides or nucleic acid species")
    PEPTIDES = PermissibleValue(
        text="PEPTIDES",
        description="Tryptic or enzymatically generated peptides")
    PHARMACEUTICALS = PermissibleValue(
        text="PHARMACEUTICALS",
        description="Drug compounds or their metabolites")
    PROTEINS = PermissibleValue(
        text="PROTEINS",
        description="Intact or top-down proteins")

    _defn = EnumDefinition(
        name="AnalyteClassEnum",
    )

class SpectrumTypeEnum(EnumDefinitionImpl):

    PROFILE = PermissibleValue(
        text="PROFILE",
        description="""Continuous spectrum; full peak shapes preserved. Level 1 is always profile/continuous imzML (Level 2 is centroided, but does not re-record SPECTRUM_TYPE).""")

    _defn = EnumDefinition(
        name="SpectrumTypeEnum",
    )

class MsScanModeEnum(EnumDefinitionImpl):

    LINEAR = PermissibleValue(
        text="LINEAR",
        description="Linear TOF mode; higher sensitivity for large molecules")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="Analyser does not use a TOF scan mode (e.g., Orbitrap, FTICR, Q-TOF hybrid)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Scan mode not listed")
    REFLECTRON = PermissibleValue(
        text="REFLECTRON",
        description="Reflectron TOF mode; improved mass resolution via ion reflection")

    _defn = EnumDefinition(
        name="MsScanModeEnum",
    )

class CalibrationTypeEnum(EnumDefinitionImpl):

    EXTERNAL = PermissibleValue(
        text="EXTERNAL",
        description="Calibration performed on a separate reference spot prior to acquisition")
    INTERNAL = PermissibleValue(
        text="INTERNAL",
        description="Calibrant ions co-present in each spectrum during acquisition")
    LOCK_MASS = PermissibleValue(
        text="LOCK_MASS",
        description="Real-time calibration correction using a reference ion of known m/z")

    _defn = EnumDefinition(
        name="CalibrationTypeEnum",
    )

class TimeUnitEnum(EnumDefinitionImpl):

    DAYS = PermissibleValue(
        text="DAYS",
        description="Time expressed in days")
    HOURS = PermissibleValue(
        text="HOURS",
        description="Time expressed in hours")

    _defn = EnumDefinition(
        name="TimeUnitEnum",
    )

class PreparationMatrixEnum(EnumDefinitionImpl):

    CHCA = PermissibleValue(
        text="CHCA",
        description="alpha-Cyano-4-hydroxycinnamic acid; used for peptides and small proteins")
    DAN = PermissibleValue(
        text="DAN",
        description="1,5-Diaminonaphthalene; used for lipids and metabolites in negative mode")
    DHA = PermissibleValue(
        text="DHA",
        description="2,6-Dihydroxyacetophenone; used for oligonucleotides and acidic lipids")
    DHB = PermissibleValue(
        text="DHB",
        description="2,5-Dihydroxybenzoic acid; used for lipids, oligosaccharides, and metabolites")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="Ionization modality does not use a matrix (DESI, SIMS)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="""Matrix compound not listed; specify in PROTOCOL_LINK. Use for IR-MALDESI (ice/endogenous-water matrix)""")
    SA = PermissibleValue(
        text="SA",
        description="Sinapinic acid; used for intact proteins >10 kDa")

    _defn = EnumDefinition(
        name="PreparationMatrixEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "9_AA",
            PermissibleValue(
                text="9_AA",
                description="9-Aminoacridine; used for lipids and metabolites in negative mode"))

class MatrixDepositionMethodEnum(EnumDefinitionImpl):

    ELECTROSPRAY = PermissibleValue(
        text="ELECTROSPRAY",
        description="Electrospray-based matrix deposition")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="Ionization modality does not use a matrix")
    PNEUMATIC_SPRAYER = PermissibleValue(
        text="PNEUMATIC_SPRAYER",
        description="Automated pneumatic spray coater (e.g., HTX TM-Sprayer)")
    ROBOTIC_SPOTTER = PermissibleValue(
        text="ROBOTIC_SPOTTER",
        description="Robotic micro-dispensing of discrete matrix spots")
    SPRAY = PermissibleValue(
        text="SPRAY",
        description="Pneumatic or manual aerosol spray application")
    SUBLIMATION = PermissibleValue(
        text="SUBLIMATION",
        description="Thermal sublimation deposition for uniform crystal layer")

    _defn = EnumDefinition(
        name="MatrixDepositionMethodEnum",
    )

class PreAcquisitionTreatmentEnum(EnumDefinitionImpl):

    NONE = PermissibleValue(
        text="NONE",
        description="No enzymatic or chemical treatment applied before this acquisition run")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Treatment not listed; describe in PROTOCOL_LINK")
    PNGASEF = PermissibleValue(
        text="PNGASEF",
        description="PNGase F enzyme applied to release N-linked glycans from glycoproteins")
    PNGASEF_THEN_TRYPSIN = PermissibleValue(
        text="PNGASEF_THEN_TRYPSIN",
        description="Sequential PNGase F followed by trypsin digestion")
    TRYPSIN = PermissibleValue(
        text="TRYPSIN",
        description="Trypsin applied for in-tissue proteolytic digestion to generate peptides")

    _defn = EnumDefinition(
        name="PreAcquisitionTreatmentEnum",
    )

class BaselineCorrectionMethodEnum(EnumDefinitionImpl):

    NONE = PermissibleValue(
        text="NONE",
        description="No baseline correction applied")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Algorithm not listed; specify in SOFTWARE_AND_VERSION or PROTOCOL_LINK")
    SNIP = PermissibleValue(
        text="SNIP",
        description="Statistics-sensitive Non-linear Iterative Peak-clipping algorithm")
    TOP_HAT = PermissibleValue(
        text="TOP_HAT",
        description="Top-hat morphological filter for baseline estimation")

    _defn = EnumDefinition(
        name="BaselineCorrectionMethodEnum",
    )

class NormalizationMethodEnum(EnumDefinitionImpl):

    MEDIAN = PermissibleValue(
        text="MEDIAN",
        description="Median spectrum intensity normalization")
    NONE = PermissibleValue(
        text="NONE",
        description="No normalization applied")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Method not listed; specify in PROTOCOL_LINK")
    REFERENCE_PEAK = PermissibleValue(
        text="REFERENCE_PEAK",
        description="Normalization to a single reference m/z peak of known abundance")
    RMS = PermissibleValue(
        text="RMS",
        description="Root Mean Square normalization")
    TIC = PermissibleValue(
        text="TIC",
        description="Total Ion Current normalization - divide each spectrum by its TIC")

    _defn = EnumDefinition(
        name="NormalizationMethodEnum",
    )

class SmoothingMethodEnum(EnumDefinitionImpl):

    GAUSSIAN = PermissibleValue(
        text="GAUSSIAN",
        description="Gaussian kernel smoothing")
    NONE = PermissibleValue(
        text="NONE",
        description="No spectral smoothing applied")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Method not listed; specify in PROTOCOL_LINK")
    SAVITZKY_GOLAY = PermissibleValue(
        text="SAVITZKY_GOLAY",
        description="Savitzky-Golay polynomial smoothing filter")

    _defn = EnumDefinition(
        name="SmoothingMethodEnum",
    )

class SegmentationReferenceModalityEnum(EnumDefinitionImpl):

    H_AND_E = PermissibleValue(
        text="H_AND_E",
        description="Segmentation derived from H&E staining and projected onto MSI pixels")
    IF = PermissibleValue(
        text="IF",
        description="Segmentation derived from immunofluorescence")
    MSI_NATIVE = PermissibleValue(
        text="MSI_NATIVE",
        description="Segmentation derived directly from MSI spectral clustering (no external reference)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Reference modality not listed")

    _defn = EnumDefinition(
        name="SegmentationReferenceModalityEnum",
    )

class AdductEnum(EnumDefinitionImpl):

    M_MINUS_H = PermissibleValue(
        text="M_MINUS_H",
        description="[M-H]- deprotonated molecule, most common negative mode adduct")
    M_PLUS_CL = PermissibleValue(
        text="M_PLUS_CL",
        description="[M+Cl]- chloride adduct")
    M_PLUS_H = PermissibleValue(
        text="M_PLUS_H",
        description="[M+H]+ protonated molecule, most common positive mode adduct")
    M_PLUS_K = PermissibleValue(
        text="M_PLUS_K",
        description="[M+K]+ potassium adduct")
    M_PLUS_NA = PermissibleValue(
        text="M_PLUS_NA",
        description="[M+Na]+ sodium adduct, common for lipids and carbohydrates")
    M_PLUS_NH4 = PermissibleValue(
        text="M_PLUS_NH4",
        description="[M+NH4]+ ammonium adduct")
    M_RADICAL_MINUS = PermissibleValue(
        text="M_RADICAL_MINUS",
        description="[M]- radical anion")
    M_RADICAL_PLUS = PermissibleValue(
        text="M_RADICAL_PLUS",
        description="[M]+ radical cation (SIMS, some MALDI applications)")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="No adduct applicable (confidence level 4 unknowns)")
    OTHER = PermissibleValue(
        text="OTHER",
        description="Adduct not listed; specify in MOLECULAR_NAME or annotation protocol")

    _defn = EnumDefinition(
        name="AdductEnum",
    )

class DatabaseSourceEnum(EnumDefinitionImpl):

    CHEBI = PermissibleValue(
        text="CHEBI",
        description="Chemical Entities of Biological Interest (https://ebi.ac.uk/chebi)")
    CUSTOM = PermissibleValue(
        text="CUSTOM",
        description="In-house or custom reference database; describe in PROTOCOL_LINK")
    GLYCONNECT = PermissibleValue(
        text="GLYCONNECT",
        description="GlyConnect glycan database (https://glyconnect.expasy.org)")
    GLYTOUCAN = PermissibleValue(
        text="GLYTOUCAN",
        description="GlyTouCan glycan repository (https://glytoucan.org)")
    HMDB = PermissibleValue(
        text="HMDB",
        description="Human Metabolome Database (https://hmdb.ca)")
    LIPID_MAPS = PermissibleValue(
        text="LIPID_MAPS",
        description="LIPID MAPS Structure Database (https://lipidmaps.org)")
    MASSBANK = PermissibleValue(
        text="MASSBANK",
        description="MassBank spectral database (https://massbank.eu)")
    METLIN = PermissibleValue(
        text="METLIN",
        description="METLIN metabolite and chemical database (https://metlin.scripps.edu)")
    NOT_APPLICABLE = PermissibleValue(
        text="NOT_APPLICABLE",
        description="No database assignment applicable (confidence level 4 unknowns)")
    PUBCHEM = PermissibleValue(
        text="PUBCHEM",
        description="PubChem compound database (https://pubchem.ncbi.nlm.nih.gov)")
    UNIPROT = PermissibleValue(
        text="UNIPROT",
        description="Universal Protein Resource for protein identifications (https://uniprot.org)")

    _defn = EnumDefinition(
        name="DatabaseSourceEnum",
    )

class EvidenceTypeEnum(EnumDefinitionImpl):

    ACCURATE_MASS = PermissibleValue(
        text="ACCURATE_MASS",
        description="Annotation supported by accurate mass match within tolerance")
    DATABASE_SPECTRAL_MATCH = PermissibleValue(
        text="DATABASE_SPECTRAL_MATCH",
        description="""Match to a spectral library entry in a public spectral database (e.g., MassBank, mzCloud, Metaspace) - as distinct from MSMS_MATCH (an in-house/experimentally acquired reference spectrum)""")
    ISOTOPE_PATTERN = PermissibleValue(
        text="ISOTOPE_PATTERN",
        description="Annotation supported by isotope pattern matching")
    MSMS_MATCH = PermissibleValue(
        text="MSMS_MATCH",
        description="""Annotation supported by MS/MS fragmentation matched to an in-house or experimentally acquired reference spectrum (use DATABASE_SPECTRAL_MATCH for matches to a public spectral library)""")
    REFERENCE_STANDARD = PermissibleValue(
        text="REFERENCE_STANDARD",
        description="Confirmed by comparison to an authenticated in-house reference standard")
    SPATIAL_PATTERN_ONLY = PermissibleValue(
        text="SPATIAL_PATTERN_ONLY",
        description="Retained for biological relevance based on spatial distribution; no structural assignment")

    _defn = EnumDefinition(
        name="EvidenceTypeEnum",
    )

# Slots
class slots:
    pass

slots.massSpectrometryImagingData__LEVEL_1_DATA = Slot(uri=HTAN.LEVEL_1_DATA, name="massSpectrometryImagingData__LEVEL_1_DATA", curie=HTAN.curie('LEVEL_1_DATA'),
                   model_uri=HTAN.massSpectrometryImagingData__LEVEL_1_DATA, domain=None, range=Optional[Union[dict, MassSpectrometryImagingLevel1]])

slots.massSpectrometryImagingData__LEVEL_2_DATA = Slot(uri=HTAN.LEVEL_2_DATA, name="massSpectrometryImagingData__LEVEL_2_DATA", curie=HTAN.curie('LEVEL_2_DATA'),
                   model_uri=HTAN.massSpectrometryImagingData__LEVEL_2_DATA, domain=None, range=Optional[Union[dict, MassSpectrometryImagingLevel2]])

slots.massSpectrometryImagingData__LEVEL_3_DATA = Slot(uri=HTAN.LEVEL_3_DATA, name="massSpectrometryImagingData__LEVEL_3_DATA", curie=HTAN.curie('LEVEL_3_DATA'),
                   model_uri=HTAN.massSpectrometryImagingData__LEVEL_3_DATA, domain=None, range=Optional[Union[dict, MassSpectrometryImagingLevel3]])

slots.massSpectrometryImagingData__LEVEL_4_DATA = Slot(uri=HTAN.LEVEL_4_DATA, name="massSpectrometryImagingData__LEVEL_4_DATA", curie=HTAN.curie('LEVEL_4_DATA'),
                   model_uri=HTAN.massSpectrometryImagingData__LEVEL_4_DATA, domain=None, range=Optional[Union[dict, MassSpectrometryImagingLevel4]])

slots.massSpectrometryImagingData__MOLECULAR_ASSIGNMENTS = Slot(uri=HTAN.MOLECULAR_ASSIGNMENTS, name="massSpectrometryImagingData__MOLECULAR_ASSIGNMENTS", curie=HTAN.curie('MOLECULAR_ASSIGNMENTS'),
                   model_uri=HTAN.massSpectrometryImagingData__MOLECULAR_ASSIGNMENTS, domain=None, range=Optional[Union[Union[dict, MolecularAssignment], List[Union[dict, MolecularAssignment]]]])

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

slots.massSpectrometryImagingLevel1__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="massSpectrometryImagingLevel1__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^imzML$'))

slots.massSpectrometryImagingLevel1__FILENAME = Slot(uri=HTAN.FILENAME, name="massSpectrometryImagingLevel1__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.imzML$'))

slots.massSpectrometryImagingLevel1__MS_IONIZATION_TECHNIQUE = Slot(uri=HTAN.MS_IONIZATION_TECHNIQUE, name="massSpectrometryImagingLevel1__MS_IONIZATION_TECHNIQUE", curie=HTAN.curie('MS_IONIZATION_TECHNIQUE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MS_IONIZATION_TECHNIQUE, domain=None, range=Union[str, "MsIonizationTechniqueEnum"])

slots.massSpectrometryImagingLevel1__MASS_ANALYZER_TYPE = Slot(uri=HTAN.MASS_ANALYZER_TYPE, name="massSpectrometryImagingLevel1__MASS_ANALYZER_TYPE", curie=HTAN.curie('MASS_ANALYZER_TYPE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MASS_ANALYZER_TYPE, domain=None, range=Union[str, "MassAnalyzerTypeEnum"])

slots.massSpectrometryImagingLevel1__MASS_ANALYSIS_POLARITY = Slot(uri=HTAN.MASS_ANALYSIS_POLARITY, name="massSpectrometryImagingLevel1__MASS_ANALYSIS_POLARITY", curie=HTAN.curie('MASS_ANALYSIS_POLARITY'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MASS_ANALYSIS_POLARITY, domain=None, range=Union[str, "MassAnalysisPolarityEnum"])

slots.massSpectrometryImagingLevel1__ANALYTE_CLASS = Slot(uri=HTAN.ANALYTE_CLASS, name="massSpectrometryImagingLevel1__ANALYTE_CLASS", curie=HTAN.curie('ANALYTE_CLASS'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__ANALYTE_CLASS, domain=None, range=Union[Union[str, "AnalyteClassEnum"], List[Union[str, "AnalyteClassEnum"]]])

slots.massSpectrometryImagingLevel1__IS_TARGETED = Slot(uri=HTAN.IS_TARGETED, name="massSpectrometryImagingLevel1__IS_TARGETED", curie=HTAN.curie('IS_TARGETED'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__IS_TARGETED, domain=None, range=Union[bool, Bool])

slots.massSpectrometryImagingLevel1__ACQUISITION_INSTRUMENT_VENDOR = Slot(uri=HTAN.ACQUISITION_INSTRUMENT_VENDOR, name="massSpectrometryImagingLevel1__ACQUISITION_INSTRUMENT_VENDOR", curie=HTAN.curie('ACQUISITION_INSTRUMENT_VENDOR'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__ACQUISITION_INSTRUMENT_VENDOR, domain=None, range=str)

slots.massSpectrometryImagingLevel1__ACQUISITION_INSTRUMENT_MODEL = Slot(uri=HTAN.ACQUISITION_INSTRUMENT_MODEL, name="massSpectrometryImagingLevel1__ACQUISITION_INSTRUMENT_MODEL", curie=HTAN.curie('ACQUISITION_INSTRUMENT_MODEL'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__ACQUISITION_INSTRUMENT_MODEL, domain=None, range=str)

slots.massSpectrometryImagingLevel1__PIXEL_SIZE_X_UM = Slot(uri=HTAN.PIXEL_SIZE_X_UM, name="massSpectrometryImagingLevel1__PIXEL_SIZE_X_UM", curie=HTAN.curie('PIXEL_SIZE_X_UM'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PIXEL_SIZE_X_UM, domain=None, range=float)

slots.massSpectrometryImagingLevel1__PIXEL_SIZE_Y_UM = Slot(uri=HTAN.PIXEL_SIZE_Y_UM, name="massSpectrometryImagingLevel1__PIXEL_SIZE_Y_UM", curie=HTAN.curie('PIXEL_SIZE_Y_UM'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PIXEL_SIZE_Y_UM, domain=None, range=float)

slots.massSpectrometryImagingLevel1__MASS_TO_CHARGE_RANGE_LOW_VALUE = Slot(uri=HTAN.MASS_TO_CHARGE_RANGE_LOW_VALUE, name="massSpectrometryImagingLevel1__MASS_TO_CHARGE_RANGE_LOW_VALUE", curie=HTAN.curie('MASS_TO_CHARGE_RANGE_LOW_VALUE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MASS_TO_CHARGE_RANGE_LOW_VALUE, domain=None, range=float)

slots.massSpectrometryImagingLevel1__MASS_TO_CHARGE_RANGE_HIGH_VALUE = Slot(uri=HTAN.MASS_TO_CHARGE_RANGE_HIGH_VALUE, name="massSpectrometryImagingLevel1__MASS_TO_CHARGE_RANGE_HIGH_VALUE", curie=HTAN.curie('MASS_TO_CHARGE_RANGE_HIGH_VALUE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MASS_TO_CHARGE_RANGE_HIGH_VALUE, domain=None, range=float)

slots.massSpectrometryImagingLevel1__ION_MOBILITY = Slot(uri=HTAN.ION_MOBILITY, name="massSpectrometryImagingLevel1__ION_MOBILITY", curie=HTAN.curie('ION_MOBILITY'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__ION_MOBILITY, domain=None, range=Union[bool, Bool])

slots.massSpectrometryImagingLevel1__SPECTRUM_TYPE = Slot(uri=HTAN.SPECTRUM_TYPE, name="massSpectrometryImagingLevel1__SPECTRUM_TYPE", curie=HTAN.curie('SPECTRUM_TYPE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__SPECTRUM_TYPE, domain=None, range=Union[str, "SpectrumTypeEnum"])

slots.massSpectrometryImagingLevel1__MASS_RESOLVING_POWER = Slot(uri=HTAN.MASS_RESOLVING_POWER, name="massSpectrometryImagingLevel1__MASS_RESOLVING_POWER", curie=HTAN.curie('MASS_RESOLVING_POWER'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MASS_RESOLVING_POWER, domain=None, range=float)

slots.massSpectrometryImagingLevel1__MASS_TO_CHARGE_RESOLVING_POWER = Slot(uri=HTAN.MASS_TO_CHARGE_RESOLVING_POWER, name="massSpectrometryImagingLevel1__MASS_TO_CHARGE_RESOLVING_POWER", curie=HTAN.curie('MASS_TO_CHARGE_RESOLVING_POWER'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MASS_TO_CHARGE_RESOLVING_POWER, domain=None, range=Optional[float])

slots.massSpectrometryImagingLevel1__MS_SCAN_MODE = Slot(uri=HTAN.MS_SCAN_MODE, name="massSpectrometryImagingLevel1__MS_SCAN_MODE", curie=HTAN.curie('MS_SCAN_MODE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MS_SCAN_MODE, domain=None, range=Union[str, "MsScanModeEnum"])

slots.massSpectrometryImagingLevel1__CALIBRATION_TYPE = Slot(uri=HTAN.CALIBRATION_TYPE, name="massSpectrometryImagingLevel1__CALIBRATION_TYPE", curie=HTAN.curie('CALIBRATION_TYPE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__CALIBRATION_TYPE, domain=None, range=Union[str, "CalibrationTypeEnum"])

slots.massSpectrometryImagingLevel1__CALIBRANT_MASSES = Slot(uri=HTAN.CALIBRANT_MASSES, name="massSpectrometryImagingLevel1__CALIBRANT_MASSES", curie=HTAN.curie('CALIBRANT_MASSES'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__CALIBRANT_MASSES, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+(\.[0-9]+)?(, ?[0-9]+(\.[0-9]+)?)*$'))

slots.massSpectrometryImagingLevel1__TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE = Slot(uri=HTAN.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE, name="massSpectrometryImagingLevel1__TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE", curie=HTAN.curie('TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_VALUE, domain=None, range=float)

slots.massSpectrometryImagingLevel1__TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT = Slot(uri=HTAN.TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT, name="massSpectrometryImagingLevel1__TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT", curie=HTAN.curie('TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__TIME_SINCE_ACQUISITION_INSTRUMENT_CALIBRATION_UNIT, domain=None, range=Union[str, "TimeUnitEnum"])

slots.massSpectrometryImagingLevel1__SOFTWARE_AND_VERSION = Slot(uri=HTAN.SOFTWARE_AND_VERSION, name="massSpectrometryImagingLevel1__SOFTWARE_AND_VERSION", curie=HTAN.curie('SOFTWARE_AND_VERSION'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__SOFTWARE_AND_VERSION, domain=None, range=str)

slots.massSpectrometryImagingLevel1__PROTOCOL_LINK = Slot(uri=HTAN.PROTOCOL_LINK, name="massSpectrometryImagingLevel1__PROTOCOL_LINK", curie=HTAN.curie('PROTOCOL_LINK'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PROTOCOL_LINK, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel1__IBD_FILE_UUID = Slot(uri=HTAN.IBD_FILE_UUID, name="massSpectrometryImagingLevel1__IBD_FILE_UUID", curie=HTAN.curie('IBD_FILE_UUID'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__IBD_FILE_UUID, domain=None, range=str,
                   pattern=re.compile(r'^\{?[0-9a-fA-F]{8}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{4}-?[0-9a-fA-F]{12}\}?$'))

slots.massSpectrometryImagingLevel1__PREPARATION_MATRIX = Slot(uri=HTAN.PREPARATION_MATRIX, name="massSpectrometryImagingLevel1__PREPARATION_MATRIX", curie=HTAN.curie('PREPARATION_MATRIX'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PREPARATION_MATRIX, domain=None, range=Optional[Union[str, "PreparationMatrixEnum"]])

slots.massSpectrometryImagingLevel1__MATRIX_DEPOSITION_METHOD = Slot(uri=HTAN.MATRIX_DEPOSITION_METHOD, name="massSpectrometryImagingLevel1__MATRIX_DEPOSITION_METHOD", curie=HTAN.curie('MATRIX_DEPOSITION_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__MATRIX_DEPOSITION_METHOD, domain=None, range=Optional[Union[str, "MatrixDepositionMethodEnum"]])

slots.massSpectrometryImagingLevel1__PREPARATION_INSTRUMENT_VENDOR = Slot(uri=HTAN.PREPARATION_INSTRUMENT_VENDOR, name="massSpectrometryImagingLevel1__PREPARATION_INSTRUMENT_VENDOR", curie=HTAN.curie('PREPARATION_INSTRUMENT_VENDOR'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PREPARATION_INSTRUMENT_VENDOR, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel1__PREPARATION_INSTRUMENT_MODEL = Slot(uri=HTAN.PREPARATION_INSTRUMENT_MODEL, name="massSpectrometryImagingLevel1__PREPARATION_INSTRUMENT_MODEL", curie=HTAN.curie('PREPARATION_INSTRUMENT_MODEL'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PREPARATION_INSTRUMENT_MODEL, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel1__ANALYTE_ACQUISITION_ORDER = Slot(uri=HTAN.ANALYTE_ACQUISITION_ORDER, name="massSpectrometryImagingLevel1__ANALYTE_ACQUISITION_ORDER", curie=HTAN.curie('ANALYTE_ACQUISITION_ORDER'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__ANALYTE_ACQUISITION_ORDER, domain=None, range=Optional[int])

slots.massSpectrometryImagingLevel1__PRE_ACQUISITION_TREATMENT = Slot(uri=HTAN.PRE_ACQUISITION_TREATMENT, name="massSpectrometryImagingLevel1__PRE_ACQUISITION_TREATMENT", curie=HTAN.curie('PRE_ACQUISITION_TREATMENT'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PRE_ACQUISITION_TREATMENT, domain=None, range=Optional[Union[str, "PreAcquisitionTreatmentEnum"]])

slots.massSpectrometryImagingLevel1__PASSED_QC = Slot(uri=HTAN.PASSED_QC, name="massSpectrometryImagingLevel1__PASSED_QC", curie=HTAN.curie('PASSED_QC'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__PASSED_QC, domain=None, range=Union[bool, Bool])

slots.massSpectrometryImagingLevel1__QC_COMMENT = Slot(uri=HTAN.QC_COMMENT, name="massSpectrometryImagingLevel1__QC_COMMENT", curie=HTAN.curie('QC_COMMENT'),
                   model_uri=HTAN.massSpectrometryImagingLevel1__QC_COMMENT, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel2__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="massSpectrometryImagingLevel2__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^imzML$'))

slots.massSpectrometryImagingLevel2__FILENAME = Slot(uri=HTAN.FILENAME, name="massSpectrometryImagingLevel2__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.imzML$'))

slots.massSpectrometryImagingLevel2__SOFTWARE_AND_VERSION = Slot(uri=HTAN.SOFTWARE_AND_VERSION, name="massSpectrometryImagingLevel2__SOFTWARE_AND_VERSION", curie=HTAN.curie('SOFTWARE_AND_VERSION'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__SOFTWARE_AND_VERSION, domain=None, range=str)

slots.massSpectrometryImagingLevel2__BASELINE_CORRECTION_METHOD = Slot(uri=HTAN.BASELINE_CORRECTION_METHOD, name="massSpectrometryImagingLevel2__BASELINE_CORRECTION_METHOD", curie=HTAN.curie('BASELINE_CORRECTION_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__BASELINE_CORRECTION_METHOD, domain=None, range=Union[str, "BaselineCorrectionMethodEnum"])

slots.massSpectrometryImagingLevel2__PEAK_PICKING_METHOD = Slot(uri=HTAN.PEAK_PICKING_METHOD, name="massSpectrometryImagingLevel2__PEAK_PICKING_METHOD", curie=HTAN.curie('PEAK_PICKING_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__PEAK_PICKING_METHOD, domain=None, range=str)

slots.massSpectrometryImagingLevel2__PEAK_PICKING_SNR_THRESHOLD = Slot(uri=HTAN.PEAK_PICKING_SNR_THRESHOLD, name="massSpectrometryImagingLevel2__PEAK_PICKING_SNR_THRESHOLD", curie=HTAN.curie('PEAK_PICKING_SNR_THRESHOLD'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__PEAK_PICKING_SNR_THRESHOLD, domain=None, range=float)

slots.massSpectrometryImagingLevel2__NORMALIZATION_METHOD = Slot(uri=HTAN.NORMALIZATION_METHOD, name="massSpectrometryImagingLevel2__NORMALIZATION_METHOD", curie=HTAN.curie('NORMALIZATION_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__NORMALIZATION_METHOD, domain=None, range=Union[str, "NormalizationMethodEnum"])

slots.massSpectrometryImagingLevel2__MASS_ALIGNMENT_METHOD = Slot(uri=HTAN.MASS_ALIGNMENT_METHOD, name="massSpectrometryImagingLevel2__MASS_ALIGNMENT_METHOD", curie=HTAN.curie('MASS_ALIGNMENT_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__MASS_ALIGNMENT_METHOD, domain=None, range=str)

slots.massSpectrometryImagingLevel2__MASS_TOLERANCE_PPM = Slot(uri=HTAN.MASS_TOLERANCE_PPM, name="massSpectrometryImagingLevel2__MASS_TOLERANCE_PPM", curie=HTAN.curie('MASS_TOLERANCE_PPM'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__MASS_TOLERANCE_PPM, domain=None, range=float)

slots.massSpectrometryImagingLevel2__SMOOTHING_METHOD = Slot(uri=HTAN.SMOOTHING_METHOD, name="massSpectrometryImagingLevel2__SMOOTHING_METHOD", curie=HTAN.curie('SMOOTHING_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__SMOOTHING_METHOD, domain=None, range=Optional[Union[str, "SmoothingMethodEnum"]])

slots.massSpectrometryImagingLevel2__PROTOCOL_LINK = Slot(uri=HTAN.PROTOCOL_LINK, name="massSpectrometryImagingLevel2__PROTOCOL_LINK", curie=HTAN.curie('PROTOCOL_LINK'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__PROTOCOL_LINK, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel2__MEDIAN_TIC = Slot(uri=HTAN.MEDIAN_TIC, name="massSpectrometryImagingLevel2__MEDIAN_TIC", curie=HTAN.curie('MEDIAN_TIC'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__MEDIAN_TIC, domain=None, range=float)

slots.massSpectrometryImagingLevel2__TIC_CV = Slot(uri=HTAN.TIC_CV, name="massSpectrometryImagingLevel2__TIC_CV", curie=HTAN.curie('TIC_CV'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__TIC_CV, domain=None, range=float)

slots.massSpectrometryImagingLevel2__MASS_ACCURACY_PPM = Slot(uri=HTAN.MASS_ACCURACY_PPM, name="massSpectrometryImagingLevel2__MASS_ACCURACY_PPM", curie=HTAN.curie('MASS_ACCURACY_PPM'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__MASS_ACCURACY_PPM, domain=None, range=float)

slots.massSpectrometryImagingLevel2__PIXEL_COMPLETION_RATE = Slot(uri=HTAN.PIXEL_COMPLETION_RATE, name="massSpectrometryImagingLevel2__PIXEL_COMPLETION_RATE", curie=HTAN.curie('PIXEL_COMPLETION_RATE'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__PIXEL_COMPLETION_RATE, domain=None, range=float)

slots.massSpectrometryImagingLevel2__NUM_DETECTED_PEAKS = Slot(uri=HTAN.NUM_DETECTED_PEAKS, name="massSpectrometryImagingLevel2__NUM_DETECTED_PEAKS", curie=HTAN.curie('NUM_DETECTED_PEAKS'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__NUM_DETECTED_PEAKS, domain=None, range=int)

slots.massSpectrometryImagingLevel2__PASSED_QC = Slot(uri=HTAN.PASSED_QC, name="massSpectrometryImagingLevel2__PASSED_QC", curie=HTAN.curie('PASSED_QC'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__PASSED_QC, domain=None, range=Union[bool, Bool])

slots.massSpectrometryImagingLevel2__QC_COMMENT = Slot(uri=HTAN.QC_COMMENT, name="massSpectrometryImagingLevel2__QC_COMMENT", curie=HTAN.curie('QC_COMMENT'),
                   model_uri=HTAN.massSpectrometryImagingLevel2__QC_COMMENT, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel3__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="massSpectrometryImagingLevel3__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^ome\.tiff?$'))

slots.massSpectrometryImagingLevel3__FILENAME = Slot(uri=HTAN.FILENAME, name="massSpectrometryImagingLevel3__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.ome\.tiff?$'))

slots.massSpectrometryImagingLevel3__NUM_ANNOTATED_CHANNELS = Slot(uri=HTAN.NUM_ANNOTATED_CHANNELS, name="massSpectrometryImagingLevel3__NUM_ANNOTATED_CHANNELS", curie=HTAN.curie('NUM_ANNOTATED_CHANNELS'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__NUM_ANNOTATED_CHANNELS, domain=None, range=int)

slots.massSpectrometryImagingLevel3__NUM_UNKNOWN_CHANNELS = Slot(uri=HTAN.NUM_UNKNOWN_CHANNELS, name="massSpectrometryImagingLevel3__NUM_UNKNOWN_CHANNELS", curie=HTAN.curie('NUM_UNKNOWN_CHANNELS'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__NUM_UNKNOWN_CHANNELS, domain=None, range=int)

slots.massSpectrometryImagingLevel3__SOFTWARE_AND_VERSION = Slot(uri=HTAN.SOFTWARE_AND_VERSION, name="massSpectrometryImagingLevel3__SOFTWARE_AND_VERSION", curie=HTAN.curie('SOFTWARE_AND_VERSION'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__SOFTWARE_AND_VERSION, domain=None, range=str)

slots.massSpectrometryImagingLevel3__PROTOCOL_LINK = Slot(uri=HTAN.PROTOCOL_LINK, name="massSpectrometryImagingLevel3__PROTOCOL_LINK", curie=HTAN.curie('PROTOCOL_LINK'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__PROTOCOL_LINK, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel3__PASSED_QC = Slot(uri=HTAN.PASSED_QC, name="massSpectrometryImagingLevel3__PASSED_QC", curie=HTAN.curie('PASSED_QC'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__PASSED_QC, domain=None, range=Union[bool, Bool])

slots.massSpectrometryImagingLevel3__QC_COMMENT = Slot(uri=HTAN.QC_COMMENT, name="massSpectrometryImagingLevel3__QC_COMMENT", curie=HTAN.curie('QC_COMMENT'),
                   model_uri=HTAN.massSpectrometryImagingLevel3__QC_COMMENT, domain=None, range=Optional[str])

slots.massSpectrometryImagingLevel4__FILE_FORMAT = Slot(uri=HTAN.FILE_FORMAT, name="massSpectrometryImagingLevel4__FILE_FORMAT", curie=HTAN.curie('FILE_FORMAT'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__FILE_FORMAT, domain=None, range=str,
                   pattern=re.compile(r'^(ome\.tiff?|csv)$'))

slots.massSpectrometryImagingLevel4__FILENAME = Slot(uri=HTAN.FILENAME, name="massSpectrometryImagingLevel4__FILENAME", curie=HTAN.curie('FILENAME'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__FILENAME, domain=None, range=str,
                   pattern=re.compile(r'^.+\.(ome\.tiff?|csv)$'))

slots.massSpectrometryImagingLevel4__SEGMENTATION_METHOD = Slot(uri=HTAN.SEGMENTATION_METHOD, name="massSpectrometryImagingLevel4__SEGMENTATION_METHOD", curie=HTAN.curie('SEGMENTATION_METHOD'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__SEGMENTATION_METHOD, domain=None, range=str)

slots.massSpectrometryImagingLevel4__SEGMENTATION_CLASS_COUNT = Slot(uri=HTAN.SEGMENTATION_CLASS_COUNT, name="massSpectrometryImagingLevel4__SEGMENTATION_CLASS_COUNT", curie=HTAN.curie('SEGMENTATION_CLASS_COUNT'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__SEGMENTATION_CLASS_COUNT, domain=None, range=int)

slots.massSpectrometryImagingLevel4__SEGMENTATION_REFERENCE_MODALITY = Slot(uri=HTAN.SEGMENTATION_REFERENCE_MODALITY, name="massSpectrometryImagingLevel4__SEGMENTATION_REFERENCE_MODALITY", curie=HTAN.curie('SEGMENTATION_REFERENCE_MODALITY'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__SEGMENTATION_REFERENCE_MODALITY, domain=None, range=Union[str, "SegmentationReferenceModalityEnum"])

slots.massSpectrometryImagingLevel4__PASSED_QC = Slot(uri=HTAN.PASSED_QC, name="massSpectrometryImagingLevel4__PASSED_QC", curie=HTAN.curie('PASSED_QC'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__PASSED_QC, domain=None, range=Union[bool, Bool])

slots.massSpectrometryImagingLevel4__QC_COMMENT = Slot(uri=HTAN.QC_COMMENT, name="massSpectrometryImagingLevel4__QC_COMMENT", curie=HTAN.curie('QC_COMMENT'),
                   model_uri=HTAN.massSpectrometryImagingLevel4__QC_COMMENT, domain=None, range=Optional[str])

slots.molecularAssignment__HTAN_DATA_FILE_ID = Slot(uri=HTAN.HTAN_DATA_FILE_ID, name="molecularAssignment__HTAN_DATA_FILE_ID", curie=HTAN.curie('HTAN_DATA_FILE_ID'),
                   model_uri=HTAN.molecularAssignment__HTAN_DATA_FILE_ID, domain=None, range=str,
                   pattern=re.compile(r'^(?=.{1,50}$)(HTA2[0-2][0-9])_(0000|EXT[0-9]{1,18}|[0-9]{1,21})_(D[0-9]{1,20})$'))

slots.molecularAssignment__CHANNEL_INDEX = Slot(uri=HTAN.CHANNEL_INDEX, name="molecularAssignment__CHANNEL_INDEX", curie=HTAN.curie('CHANNEL_INDEX'),
                   model_uri=HTAN.molecularAssignment__CHANNEL_INDEX, domain=None, range=int)

slots.molecularAssignment__MZ_OBSERVED = Slot(uri=HTAN.MZ_OBSERVED, name="molecularAssignment__MZ_OBSERVED", curie=HTAN.curie('MZ_OBSERVED'),
                   model_uri=HTAN.molecularAssignment__MZ_OBSERVED, domain=None, range=float)

slots.molecularAssignment__MZ_THEORETICAL = Slot(uri=HTAN.MZ_THEORETICAL, name="molecularAssignment__MZ_THEORETICAL", curie=HTAN.curie('MZ_THEORETICAL'),
                   model_uri=HTAN.molecularAssignment__MZ_THEORETICAL, domain=None, range=Optional[float])

slots.molecularAssignment__MASS_ERROR_PPM = Slot(uri=HTAN.MASS_ERROR_PPM, name="molecularAssignment__MASS_ERROR_PPM", curie=HTAN.curie('MASS_ERROR_PPM'),
                   model_uri=HTAN.molecularAssignment__MASS_ERROR_PPM, domain=None, range=Optional[float])

slots.molecularAssignment__MOLECULAR_FORMULA = Slot(uri=HTAN.MOLECULAR_FORMULA, name="molecularAssignment__MOLECULAR_FORMULA", curie=HTAN.curie('MOLECULAR_FORMULA'),
                   model_uri=HTAN.molecularAssignment__MOLECULAR_FORMULA, domain=None, range=Optional[str])

slots.molecularAssignment__MOLECULAR_NAME = Slot(uri=HTAN.MOLECULAR_NAME, name="molecularAssignment__MOLECULAR_NAME", curie=HTAN.curie('MOLECULAR_NAME'),
                   model_uri=HTAN.molecularAssignment__MOLECULAR_NAME, domain=None, range=str)

slots.molecularAssignment__ADDUCT = Slot(uri=HTAN.ADDUCT, name="molecularAssignment__ADDUCT", curie=HTAN.curie('ADDUCT'),
                   model_uri=HTAN.molecularAssignment__ADDUCT, domain=None, range=Optional[Union[str, "AdductEnum"]])

slots.molecularAssignment__DATABASE_SOURCE = Slot(uri=HTAN.DATABASE_SOURCE, name="molecularAssignment__DATABASE_SOURCE", curie=HTAN.curie('DATABASE_SOURCE'),
                   model_uri=HTAN.molecularAssignment__DATABASE_SOURCE, domain=None, range=Optional[Union[str, "DatabaseSourceEnum"]])

slots.molecularAssignment__DATABASE_ID = Slot(uri=HTAN.DATABASE_ID, name="molecularAssignment__DATABASE_ID", curie=HTAN.curie('DATABASE_ID'),
                   model_uri=HTAN.molecularAssignment__DATABASE_ID, domain=None, range=Optional[str])

slots.molecularAssignment__DATABASE_VERSION = Slot(uri=HTAN.DATABASE_VERSION, name="molecularAssignment__DATABASE_VERSION", curie=HTAN.curie('DATABASE_VERSION'),
                   model_uri=HTAN.molecularAssignment__DATABASE_VERSION, domain=None, range=Optional[str])

slots.molecularAssignment__SOFTWARE_AND_VERSION = Slot(uri=HTAN.SOFTWARE_AND_VERSION, name="molecularAssignment__SOFTWARE_AND_VERSION", curie=HTAN.curie('SOFTWARE_AND_VERSION'),
                   model_uri=HTAN.molecularAssignment__SOFTWARE_AND_VERSION, domain=None, range=str)

slots.molecularAssignment__CONFIDENCE_LEVEL = Slot(uri=HTAN.CONFIDENCE_LEVEL, name="molecularAssignment__CONFIDENCE_LEVEL", curie=HTAN.curie('CONFIDENCE_LEVEL'),
                   model_uri=HTAN.molecularAssignment__CONFIDENCE_LEVEL, domain=None, range=int)

slots.molecularAssignment__EVIDENCE_TYPE = Slot(uri=HTAN.EVIDENCE_TYPE, name="molecularAssignment__EVIDENCE_TYPE", curie=HTAN.curie('EVIDENCE_TYPE'),
                   model_uri=HTAN.molecularAssignment__EVIDENCE_TYPE, domain=None, range=Union[Union[str, "EvidenceTypeEnum"], List[Union[str, "EvidenceTypeEnum"]]])
