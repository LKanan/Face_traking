__all__: list[str] = []

import cv2
import cv2.typing
import typing as _typing


# Enumerations
RETINA_COLOR_RANDOM: int
RETINA_COLOR_DIAGONAL: int
RETINA_COLOR_BAYER: int



# Classes
class Retina(cv2.Algorithm):
    # Functions
    def getInputSize(self) -> cv2.typing.Size: ...

    def getOutputSize(self) -> cv2.typing.Size: ...

    def setup(self, retinaParameterFile: str = ..., applyDefaultSetupOnFailure: bool = ...) -> None: ...

    def printSetup(self) -> str: ...

    def write(self, fs: str) -> None: ...

    def setupOPLandIPLParvoChannel(self, colorMode: bool = ..., normaliseOutput: bool = ..., photoreceptorsLocalAdaptationSensitivity: float = ..., photoreceptorsTemporalConstant: float = ..., photoreceptorsSpatialConstant: float = ..., horizontalCellsGain: float = ..., HcellsTemporalConstant: float = ..., HcellsSpatialConstant: float = ..., ganglionCellsSensitivity: float = ...) -> None: ...

    def setupIPLMagnoChannel(self, normaliseOutput: bool = ..., parasolCells_beta: float = ..., parasolCells_tau: float = ..., parasolCells_k: float = ..., amacrinCellsTemporalCutFrequency: float = ..., V0CompressionParameter: float = ..., localAdaptintegration_tau: float = ..., localAdaptintegration_k: float = ...) -> None: ...

    @_typing.overload
    def run(self, inputImage: cv2.typing.MatLike) -> None: ...
    @_typing.overload
    def run(self, inputImage: cv2.UMat) -> None: ...

    @_typing.overload
    def applyFastToneMapping(self, inputImage: cv2.typing.MatLike, outputToneMappedImage: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def applyFastToneMapping(self, inputImage: cv2.UMat, outputToneMappedImage: cv2.UMat | None = ...) -> cv2.UMat: ...

    @_typing.overload
    def getParvo(self, retinaOutput_parvo: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def getParvo(self, retinaOutput_parvo: cv2.UMat | None = ...) -> cv2.UMat: ...

    @_typing.overload
    def getParvoRAW(self, retinaOutput_parvo: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def getParvoRAW(self, retinaOutput_parvo: cv2.UMat | None = ...) -> cv2.UMat: ...
    @_typing.overload
    def getParvoRAW(self) -> cv2.typing.MatLike: ...

    @_typing.overload
    def getMagno(self, retinaOutput_magno: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def getMagno(self, retinaOutput_magno: cv2.UMat | None = ...) -> cv2.UMat: ...

    @_typing.overload
    def getMagnoRAW(self, retinaOutput_magno: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def getMagnoRAW(self, retinaOutput_magno: cv2.UMat | None = ...) -> cv2.UMat: ...
    @_typing.overload
    def getMagnoRAW(self) -> cv2.typing.MatLike: ...

    def setColorSaturation(self, saturateColors: bool = ..., colorSaturationValue: float = ...) -> None: ...

    def clearBuffers(self) -> None: ...

    def activateMovingContoursProcessing(self, activate: bool) -> None: ...

    def activateContoursProcessing(self, activate: bool) -> None: ...

    @classmethod
    @_typing.overload
    def create(cls, inputSize: cv2.typing.Size) -> Retina: ...
    @classmethod
    @_typing.overload
    def create(cls, inputSize: cv2.typing.Size, colorMode: bool, colorSamplingMethod: int = ..., useRetinaLogSampling: bool = ..., reductionFactor: float = ..., samplingStrength: float = ...) -> Retina: ...


class RetinaFastToneMapping(cv2.Algorithm):
    # Functions
    @_typing.overload
    def applyFastToneMapping(self, inputImage: cv2.typing.MatLike, outputToneMappedImage: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def applyFastToneMapping(self, inputImage: cv2.UMat, outputToneMappedImage: cv2.UMat | None = ...) -> cv2.UMat: ...

    def setup(self, photoreceptorsNeighborhoodRadius: float = ..., ganglioncellsNeighborhoodRadius: float = ..., meanLuminanceModulatorK: float = ...) -> None: ...

    @classmethod
    def create(cls, inputSize: cv2.typing.Size) -> RetinaFastToneMapping: ...


class TransientAreasSegmentationModule(cv2.Algorithm):
    # Functions
    def getSize(self) -> cv2.typing.Size: ...

    def setup(self, segmentationParameterFile: str = ..., applyDefaultSetupOnFailure: bool = ...) -> None: ...

    def printSetup(self) -> str: ...

    def write(self, fs: str) -> None: ...

    @_typing.overload
    def run(self, inputToSegment: cv2.typing.MatLike, channelIndex: int = ...) -> None: ...
    @_typing.overload
    def run(self, inputToSegment: cv2.UMat, channelIndex: int = ...) -> None: ...

    @_typing.overload
    def getSegmentationPicture(self, transientAreas: cv2.typing.MatLike | None = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def getSegmentationPicture(self, transientAreas: cv2.UMat | None = ...) -> cv2.UMat: ...

    def clearAllBuffers(self) -> None: ...

    @classmethod
    def create(cls, inputSize: cv2.typing.Size) -> TransientAreasSegmentationModule: ...



