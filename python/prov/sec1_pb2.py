# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sec1.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import prov.constants_pb2 as constants__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sec1.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\nsec1.proto\x1a\x0f\x63onstants.proto\")\n\x0bSessionCmd1\x12\x1a\n\x12\x63lient_verify_data\x18\x02 \x01(\x0c\"C\n\x0cSessionResp1\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\x1a\n\x12\x64\x65vice_verify_data\x18\x03 \x01(\x0c\"$\n\x0bSessionCmd0\x12\x15\n\rclient_pubkey\x18\x01 \x01(\x0c\"U\n\x0cSessionResp0\x12\x17\n\x06status\x18\x01 \x01(\x0e\x32\x07.Status\x12\x15\n\rdevice_pubkey\x18\x02 \x01(\x0c\x12\x15\n\rdevice_random\x18\x03 \x01(\x0c\"\xa9\x01\n\x0bSec1Payload\x12\x19\n\x03msg\x18\x01 \x01(\x0e\x32\x0c.Sec1MsgType\x12\x1b\n\x03sc0\x18\x14 \x01(\x0b\x32\x0c.SessionCmd0H\x00\x12\x1c\n\x03sr0\x18\x15 \x01(\x0b\x32\r.SessionResp0H\x00\x12\x1b\n\x03sc1\x18\x16 \x01(\x0b\x32\x0c.SessionCmd1H\x00\x12\x1c\n\x03sr1\x18\x17 \x01(\x0b\x32\r.SessionResp1H\x00\x42\t\n\x07payload*g\n\x0bSec1MsgType\x12\x14\n\x10Session_Command0\x10\x00\x12\x15\n\x11Session_Response0\x10\x01\x12\x14\n\x10Session_Command1\x10\x02\x12\x15\n\x11Session_Response1\x10\x03\x62\x06proto3')
  ,
  dependencies=[constants__pb2.DESCRIPTOR,])

_SEC1MSGTYPE = _descriptor.EnumDescriptor(
  name='Sec1MsgType',
  full_name='Sec1MsgType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Session_Command0', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Session_Response0', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Session_Command1', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Session_Response1', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=440,
  serialized_end=543,
)
_sym_db.RegisterEnumDescriptor(_SEC1MSGTYPE)

Sec1MsgType = enum_type_wrapper.EnumTypeWrapper(_SEC1MSGTYPE)
Session_Command0 = 0
Session_Response0 = 1
Session_Command1 = 2
Session_Response1 = 3



_SESSIONCMD1 = _descriptor.Descriptor(
  name='SessionCmd1',
  full_name='SessionCmd1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_verify_data', full_name='SessionCmd1.client_verify_data', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=72,
)


_SESSIONRESP1 = _descriptor.Descriptor(
  name='SessionResp1',
  full_name='SessionResp1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SessionResp1.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_verify_data', full_name='SessionResp1.device_verify_data', index=1,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=141,
)


_SESSIONCMD0 = _descriptor.Descriptor(
  name='SessionCmd0',
  full_name='SessionCmd0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_pubkey', full_name='SessionCmd0.client_pubkey', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=179,
)


_SESSIONRESP0 = _descriptor.Descriptor(
  name='SessionResp0',
  full_name='SessionResp0',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='SessionResp0.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_pubkey', full_name='SessionResp0.device_pubkey', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_random', full_name='SessionResp0.device_random', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=266,
)


_SEC1PAYLOAD = _descriptor.Descriptor(
  name='Sec1Payload',
  full_name='Sec1Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='Sec1Payload.msg', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sc0', full_name='Sec1Payload.sc0', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sr0', full_name='Sec1Payload.sr0', index=2,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sc1', full_name='Sec1Payload.sc1', index=3,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sr1', full_name='Sec1Payload.sr1', index=4,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='Sec1Payload.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=269,
  serialized_end=438,
)

_SESSIONRESP1.fields_by_name['status'].enum_type = constants__pb2._STATUS
_SESSIONRESP0.fields_by_name['status'].enum_type = constants__pb2._STATUS
_SEC1PAYLOAD.fields_by_name['msg'].enum_type = _SEC1MSGTYPE
_SEC1PAYLOAD.fields_by_name['sc0'].message_type = _SESSIONCMD0
_SEC1PAYLOAD.fields_by_name['sr0'].message_type = _SESSIONRESP0
_SEC1PAYLOAD.fields_by_name['sc1'].message_type = _SESSIONCMD1
_SEC1PAYLOAD.fields_by_name['sr1'].message_type = _SESSIONRESP1
_SEC1PAYLOAD.oneofs_by_name['payload'].fields.append(
  _SEC1PAYLOAD.fields_by_name['sc0'])
_SEC1PAYLOAD.fields_by_name['sc0'].containing_oneof = _SEC1PAYLOAD.oneofs_by_name['payload']
_SEC1PAYLOAD.oneofs_by_name['payload'].fields.append(
  _SEC1PAYLOAD.fields_by_name['sr0'])
_SEC1PAYLOAD.fields_by_name['sr0'].containing_oneof = _SEC1PAYLOAD.oneofs_by_name['payload']
_SEC1PAYLOAD.oneofs_by_name['payload'].fields.append(
  _SEC1PAYLOAD.fields_by_name['sc1'])
_SEC1PAYLOAD.fields_by_name['sc1'].containing_oneof = _SEC1PAYLOAD.oneofs_by_name['payload']
_SEC1PAYLOAD.oneofs_by_name['payload'].fields.append(
  _SEC1PAYLOAD.fields_by_name['sr1'])
_SEC1PAYLOAD.fields_by_name['sr1'].containing_oneof = _SEC1PAYLOAD.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['SessionCmd1'] = _SESSIONCMD1
DESCRIPTOR.message_types_by_name['SessionResp1'] = _SESSIONRESP1
DESCRIPTOR.message_types_by_name['SessionCmd0'] = _SESSIONCMD0
DESCRIPTOR.message_types_by_name['SessionResp0'] = _SESSIONRESP0
DESCRIPTOR.message_types_by_name['Sec1Payload'] = _SEC1PAYLOAD
DESCRIPTOR.enum_types_by_name['Sec1MsgType'] = _SEC1MSGTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SessionCmd1 = _reflection.GeneratedProtocolMessageType('SessionCmd1', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONCMD1,
  __module__ = 'sec1_pb2'
  # @@protoc_insertion_point(class_scope:SessionCmd1)
  ))
_sym_db.RegisterMessage(SessionCmd1)

SessionResp1 = _reflection.GeneratedProtocolMessageType('SessionResp1', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONRESP1,
  __module__ = 'sec1_pb2'
  # @@protoc_insertion_point(class_scope:SessionResp1)
  ))
_sym_db.RegisterMessage(SessionResp1)

SessionCmd0 = _reflection.GeneratedProtocolMessageType('SessionCmd0', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONCMD0,
  __module__ = 'sec1_pb2'
  # @@protoc_insertion_point(class_scope:SessionCmd0)
  ))
_sym_db.RegisterMessage(SessionCmd0)

SessionResp0 = _reflection.GeneratedProtocolMessageType('SessionResp0', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONRESP0,
  __module__ = 'sec1_pb2'
  # @@protoc_insertion_point(class_scope:SessionResp0)
  ))
_sym_db.RegisterMessage(SessionResp0)

Sec1Payload = _reflection.GeneratedProtocolMessageType('Sec1Payload', (_message.Message,), dict(
  DESCRIPTOR = _SEC1PAYLOAD,
  __module__ = 'sec1_pb2'
  # @@protoc_insertion_point(class_scope:Sec1Payload)
  ))
_sym_db.RegisterMessage(Sec1Payload)


# @@protoc_insertion_point(module_scope)
