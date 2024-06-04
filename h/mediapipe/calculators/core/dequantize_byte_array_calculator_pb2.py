# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/dequantize_byte_array_calculator.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAmediapipe/calculators/core/dequantize_byte_array_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xc0\x01\n$DequantizeByteArrayCalculatorOptions\x12\x1b\n\x13max_quantized_value\x18\x01 \x01(\x02\x12\x1b\n\x13min_quantized_value\x18\x02 \x01(\x02\x32^\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xb7\xef\xec\x81\x01 \x01(\x0b\x32/.mediapipe.DequantizeByteArrayCalculatorOptions')



_DEQUANTIZEBYTEARRAYCALCULATOROPTIONS = DESCRIPTOR.message_types_by_name['DequantizeByteArrayCalculatorOptions']
DequantizeByteArrayCalculatorOptions = _reflection.GeneratedProtocolMessageType('DequantizeByteArrayCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _DEQUANTIZEBYTEARRAYCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.core.dequantize_byte_array_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.DequantizeByteArrayCalculatorOptions)
  })
_sym_db.RegisterMessage(DequantizeByteArrayCalculatorOptions)

if _descriptor._USE_C_DESCRIPTORS == False:
  mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_DEQUANTIZEBYTEARRAYCALCULATOROPTIONS.extensions_by_name['ext'])

  DESCRIPTOR._options = None
  _DEQUANTIZEBYTEARRAYCALCULATOROPTIONS._serialized_start=119
  _DEQUANTIZEBYTEARRAYCALCULATOROPTIONS._serialized_end=311
# @@protoc_insertion_point(module_scope)
