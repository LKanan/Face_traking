# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/tasks/cc/vision/face_stylizer/calculators/tensors_to_image_calculator.proto
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
from mediapipe.gpu import gpu_origin_pb2 as mediapipe_dot_gpu_dot_gpu__origin__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nUmediapipe/tasks/cc/vision/face_stylizer/calculators/tensors_to_image_calculator.proto\x12\x0fmediapipe.tasks\x1a$mediapipe/framework/calculator.proto\x1a\x1emediapipe/gpu/gpu_origin.proto\"\xe5\x03\n\x1fTensorsToImageCalculatorOptions\x12-\n\ngpu_origin\x18\x01 \x01(\x0e\x32\x19.mediapipe.GpuOrigin.Mode\x12_\n\x18input_tensor_float_range\x18\x02 \x01(\x0b\x32;.mediapipe.tasks.TensorsToImageCalculatorOptions.FloatRangeH\x00\x12]\n\x17input_tensor_uint_range\x18\x03 \x01(\x0b\x32:.mediapipe.tasks.TensorsToImageCalculatorOptions.UIntRangeH\x00\x12\x1a\n\x0ftensor_position\x18\x04 \x01(\x05:\x01\x30\x1a&\n\nFloatRange\x12\x0b\n\x03min\x18\x01 \x01(\x02\x12\x0b\n\x03max\x18\x02 \x01(\x02\x1a%\n\tUIntRange\x12\x0b\n\x03min\x18\x01 \x01(\x04\x12\x0b\n\x03max\x18\x02 \x01(\x04\x32_\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf4\xd8\x87\xf4\x01 \x01(\x0b\x32\x30.mediapipe.tasks.TensorsToImageCalculatorOptionsB\x07\n\x05range')



_TENSORSTOIMAGECALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['TensorsToImageCalculatorOptions']
_TENSORSTOIMAGECALCULATOROPTIONS_FLOATRANGE = _TENSORSTOIMAGECALCULATOROPTIONS.nested_types_by_name['FloatRange']
_TENSORSTOIMAGECALCULATOROPTIONS_UINTRANGE = _TENSORSTOIMAGECALCULATOROPTIONS.nested_types_by_name['UIntRange']
TensorsToImageCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorsToImageCalculatorOptions', (_message.Message,), {

  'FloatRange' : _reflection.GeneratedProtocolMessageType('FloatRange', (_message.Message,), {
    'DESCRIPTOR' : _TENSORSTOIMAGECALCULATOROPTIONS_FLOATRANGE,
    '__module__' : 'mediapipe.tasks.cc.vision.face_stylizer.calculators.tensors_to_image_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.tasks.TensorsToImageCalculatorOptions.FloatRange)
    })
  ,

  'UIntRange' : _reflection.GeneratedProtocolMessageType('UIntRange', (_message.Message,), {
    'DESCRIPTOR' : _TENSORSTOIMAGECALCULATOROPTIONS_UINTRANGE,
    '__module__' : 'mediapipe.tasks.cc.vision.face_stylizer.calculators.tensors_to_image_calculator_pb2'
    # @@protoc_insertion_point(class_scope:mediapipe.tasks.TensorsToImageCalculatorOptions.UIntRange)
    })
  ,
  'DESCRIPTOR' : _TENSORSTOIMAGECALCULATOROPTIONS,
  '__module__' : 'mediapipe.tasks.cc.vision.face_stylizer.calculators.tensors_to_image_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.tasks.TensorsToImageCalculatorOptions)
  })
_sym_db.RegisterMessage(TensorsToImageCalculatorOptions)
_sym_db.RegisterMessage(TensorsToImageCalculatorOptions.FloatRange)
_sym_db.RegisterMessage(TensorsToImageCalculatorOptions.UIntRange)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORSTOIMAGECALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _TENSORSTOIMAGECALCULATOROPTIONS._serialized_start=177
  _TENSORSTOIMAGECALCULATOROPTIONS._serialized_end=662
  _TENSORSTOIMAGECALCULATOROPTIONS_FLOATRANGE._serialized_start=479
  _TENSORSTOIMAGECALCULATOROPTIONS_FLOATRANGE._serialized_end=517
  _TENSORSTOIMAGECALCULATOROPTIONS_UINTRANGE._serialized_start=519
  _TENSORSTOIMAGECALCULATOROPTIONS_UINTRANGE._serialized_end=556
# @@protoc_insertion_point(module_scope)
