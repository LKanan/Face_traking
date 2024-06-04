# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/util/analytics/mediapipe_logging_enums.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6mediapipe/util/analytics/mediapipe_logging_enums.proto\x12\x14logs.proto.mediapipe*H\n\x08Platform\x12\x14\n\x10PLATFORM_UNKNOWN\x10\x00\x12\x14\n\x10PLATFORM_ANDROID\x10\x01\x12\x10\n\x0cPLATFORM_IOS\x10\x02*\xaa\x04\n\x0cSolutionName\x12\x14\n\x10SOLUTION_UNKNOWN\x10\x00\x12\x1a\n\x16SOLUTION_FACEDETECTION\x10\x01\x12\x15\n\x11SOLUTION_FACEMESH\x10\x02\x12\x12\n\x0eSOLUTION_HANDS\x10\x03\x12\x19\n\x15TASKS_AUDIOCLASSIFIER\x10\x04\x12\x17\n\x13TASKS_AUDIOEMBEDDER\x10\x05\x12\x18\n\x14TASKS_TEXTCLASSIFIER\x10\x06\x12\x16\n\x12TASKS_TEXTEMBEDDER\x10\x07\x12\x1b\n\x17TASKS_GESTURERECOGNIZER\x10\x08\x12\x16\n\x12TASKS_HANDDETECTOR\x10\t\x12\x18\n\x14TASKS_HANDLANDMARKER\x10\n\x12\x19\n\x15TASKS_IMAGECLASSIFIER\x10\x0b\x12\x17\n\x13TASKS_IMAGEEMBEDDER\x10\x0c\x12\x18\n\x14TASKS_IMAGESEGMENTER\x10\r\x12\x18\n\x14TASKS_OBJECTDETECTOR\x10\x0e\x12\x16\n\x12TASKS_FACEDETECTOR\x10\x0f\x12\x18\n\x14TASKS_FACELANDMARKER\x10\x10\x12\x16\n\x12TASKS_FACESTYLIZER\x10\x11\x12\x1e\n\x1aTASKS_INTERACTIVESEGMENTER\x10\x12\x12\x18\n\x14TASKS_IMAGEGENERATOR\x10\x13\x12\x1c\n\x18TASKS_HOLISTICLANDMARKER\x10\x14*R\n\tEventName\x12\x0f\n\x0b\x45VENT_START\x10\x00\x12\x14\n\x10\x45VENT_INVOCATONS\x10\x01\x12\r\n\tEVENT_END\x10\x02\x12\x0f\n\x0b\x45VENT_ERROR\x10\x03*\xe4\x01\n\x0cSolutionMode\x12\x10\n\x0cMODE_UNKNOWN\x10\x00\x12\x0e\n\nMODE_VIDEO\x10\x01\x12\x15\n\x11MODE_STATIC_IMAGE\x10\x02\x12\x1a\n\x16MODE_TASKS_UNSPECIFIED\x10\n\x12\x14\n\x10MODE_TASKS_IMAGE\x10\x0b\x12\x14\n\x10MODE_TASKS_VIDEO\x10\x0c\x12\x1a\n\x16MODE_TASKS_LIVE_STREAM\x10\r\x12\x1a\n\x16MODE_TASKS_AUDIO_CLIPS\x10\x0e\x12\x1b\n\x17MODE_TASKS_AUDIO_STREAM\x10\x0f*\x8f\x01\n\rInputDataType\x12\x16\n\x12INPUT_TYPE_UNKNOWN\x10\x00\x12\x18\n\x14INPUT_TYPE_CPU_IMAGE\x10\x01\x12\x18\n\x14INPUT_TYPE_GPU_IMAGE\x10\x02\x12\x18\n\x14INPUT_TYPE_TASKS_CPU\x10\x03\x12\x18\n\x14INPUT_TYPE_TASKS_GPU\x10\x04*i\n\tErrorCode\x12\x11\n\rERROR_UNKNOWN\x10\x00\x12\x1b\n\x17\x45RROR_UNSUPPORTED_INPUT\x10\x01\x12\x1c\n\x18\x45RROR_UNSUPPORTED_OUTPUT\x10\x02\x12\x0e\n\nERROR_INIT\x10\x03\x42\x38\n\x1a\x63om.google.mediapipe.protoB\x1aMediaPipeLoggingEnumsProto')

_PLATFORM = DESCRIPTOR.enum_types_by_name['Platform']
Platform = enum_type_wrapper.EnumTypeWrapper(_PLATFORM)
_SOLUTIONNAME = DESCRIPTOR.enum_types_by_name['SolutionName']
SolutionName = enum_type_wrapper.EnumTypeWrapper(_SOLUTIONNAME)
_EVENTNAME = DESCRIPTOR.enum_types_by_name['EventName']
EventName = enum_type_wrapper.EnumTypeWrapper(_EVENTNAME)
_SOLUTIONMODE = DESCRIPTOR.enum_types_by_name['SolutionMode']
SolutionMode = enum_type_wrapper.EnumTypeWrapper(_SOLUTIONMODE)
_INPUTDATATYPE = DESCRIPTOR.enum_types_by_name['InputDataType']
InputDataType = enum_type_wrapper.EnumTypeWrapper(_INPUTDATATYPE)
_ERRORCODE = DESCRIPTOR.enum_types_by_name['ErrorCode']
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
PLATFORM_UNKNOWN = 0
PLATFORM_ANDROID = 1
PLATFORM_IOS = 2
SOLUTION_UNKNOWN = 0
SOLUTION_FACEDETECTION = 1
SOLUTION_FACEMESH = 2
SOLUTION_HANDS = 3
TASKS_AUDIOCLASSIFIER = 4
TASKS_AUDIOEMBEDDER = 5
TASKS_TEXTCLASSIFIER = 6
TASKS_TEXTEMBEDDER = 7
TASKS_GESTURERECOGNIZER = 8
TASKS_HANDDETECTOR = 9
TASKS_HANDLANDMARKER = 10
TASKS_IMAGECLASSIFIER = 11
TASKS_IMAGEEMBEDDER = 12
TASKS_IMAGESEGMENTER = 13
TASKS_OBJECTDETECTOR = 14
TASKS_FACEDETECTOR = 15
TASKS_FACELANDMARKER = 16
TASKS_FACESTYLIZER = 17
TASKS_INTERACTIVESEGMENTER = 18
TASKS_IMAGEGENERATOR = 19
TASKS_HOLISTICLANDMARKER = 20
EVENT_START = 0
EVENT_INVOCATONS = 1
EVENT_END = 2
EVENT_ERROR = 3
MODE_UNKNOWN = 0
MODE_VIDEO = 1
MODE_STATIC_IMAGE = 2
MODE_TASKS_UNSPECIFIED = 10
MODE_TASKS_IMAGE = 11
MODE_TASKS_VIDEO = 12
MODE_TASKS_LIVE_STREAM = 13
MODE_TASKS_AUDIO_CLIPS = 14
MODE_TASKS_AUDIO_STREAM = 15
INPUT_TYPE_UNKNOWN = 0
INPUT_TYPE_CPU_IMAGE = 1
INPUT_TYPE_GPU_IMAGE = 2
INPUT_TYPE_TASKS_CPU = 3
INPUT_TYPE_TASKS_GPU = 4
ERROR_UNKNOWN = 0
ERROR_UNSUPPORTED_INPUT = 1
ERROR_UNSUPPORTED_OUTPUT = 2
ERROR_INIT = 3


if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\032com.google.mediapipe.protoB\032MediaPipeLoggingEnumsProto'
  _PLATFORM._serialized_start=80
  _PLATFORM._serialized_end=152
  _SOLUTIONNAME._serialized_start=155
  _SOLUTIONNAME._serialized_end=709
  _EVENTNAME._serialized_start=711
  _EVENTNAME._serialized_end=793
  _SOLUTIONMODE._serialized_start=796
  _SOLUTIONMODE._serialized_end=1024
  _INPUTDATATYPE._serialized_start=1027
  _INPUTDATATYPE._serialized_end=1170
  _ERRORCODE._serialized_start=1172
  _ERRORCODE._serialized_end=1277
# @@protoc_insertion_point(module_scope)
