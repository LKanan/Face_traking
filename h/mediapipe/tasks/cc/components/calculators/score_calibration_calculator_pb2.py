# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/components/calculators/score_calibration_calculator.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLmediapipe/tasks/cc/components/calculators/score_calibration_calculator.proto\x12\x0fmediapipe.tasks\x1a$mediapipe/framework/calculator.proto\"\xfc\x03\n!ScoreCalibrationCalculatorOptions\x12L\n\x08sigmoids\x18\x01 \x03(\x0b\x32:.mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid\x12n\n\x14score_transformation\x18\x02 \x01(\x0e\x32\x46.mediapipe.tasks.ScoreCalibrationCalculatorOptions.ScoreTransformation:\x08IDENTITY\x12\x15\n\rdefault_score\x18\x03 \x01(\x02\x1aJ\n\x07Sigmoid\x12\r\n\x05scale\x18\x01 \x01(\x02\x12\r\n\x05slope\x18\x02 \x01(\x02\x12\x0e\n\x06offset\x18\x03 \x01(\x02\x12\x11\n\tmin_score\x18\x04 \x01(\x02\"S\n\x13ScoreTransformation\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0c\n\x08IDENTITY\x10\x01\x12\x07\n\x03LOG\x10\x02\x12\x14\n\x10INVERSE_LOGISTIC\x10\x03\x32\x61\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x9e\xff\x9a\xe0\x01 \x01(\x0b\x32\x32.mediapipe.tasks.ScoreCalibrationCalculatorOptions')



_SCORECALIBRATIONCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['ScoreCalibrationCalculatorOptions']
_SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID = _SCORECALIBRATIONCALCULATOROPTIONS.nested_types_by_name['Sigmoid']
_SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION = _SCORECALIBRATIONCALCULATOROPTIONS.enum_types_by_name['ScoreTransformation']
ScoreCalibrationCalculatorOptions = _reflection.GeneratedProtocolMessageType('ScoreCalibrationCalculatorOptions', (_message.Message,), {

  'Sigmoid' : _reflection.GeneratedProtocolMessageType('Sigmoid', (_message.Message,), {
    'DESCRIPTOR' : _SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID,
    '__module__' : 'mediapipe.tasks.cc.components.calculators.score_calibration_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.tasks.ScoreCalibrationCalculatorOptions.Sigmoid)
    })
  ,
  'DESCRIPTOR' : _SCORECALIBRATIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.tasks.cc.components.calculators.score_calibration_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.ScoreCalibrationCalculatorOptions)
  })
_sym_db.RegisterMessage(ScoreCalibrationCalculatorOptions)
_sym_db.RegisterMessage(ScoreCalibrationCalculatorOptions.Sigmoid)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SCORECALIBRATIONCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _SCORECALIBRATIONCALCULATOROPTIONS._serialized_start=136
  _SCORECALIBRATIONCALCULATOROPTIONS._serialized_end=644
  _SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID._serialized_start=386
  _SCORECALIBRATIONCALCULATOROPTIONS_SIGMOID._serialized_end=460
  _SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION._serialized_start=462
  _SCORECALIBRATIONCALCULATOROPTIONS_SCORETRANSFORMATION._serialized_end=545
# @@protoc_insertion_point(module_scope)