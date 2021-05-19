# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from validate.validate import validate_pb2 as validate_dot_validate_dot_validate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/user.proto',
  package='examplepb',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10proto/user.proto\x12\texamplepb\x1a\x1fgoogle/protobuf/timestamp.proto\x1a validate/validate/validate.proto\"\xa7\x02\n\x11\x43reateUserRequest\x12\x14\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01\x12\x1b\n\nfirst_name\x18\x02 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1a\n\tlast_name\x18\x03 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x1a\n\tuser_name\x18\x04 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x16\n\x05\x65mail\x18\x05 \x01(\tB\x07\xfa\x42\x04r\x02`\x01\x12\x19\n\x08password\x18\x06 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x14\n\x0cphone_number\x18\x07 \x01(\t\x12;\n\rdate_of_birth\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x08\xfa\x42\x05\xb2\x01\x02\x08\x01\x12!\n\x08state_id\x18\t \x01(\x05\x42\x0f\xfa\x42\x0cJ\n\x15&\x00\x00\x00-\x01\x00\x00\x00\"$\n\x12\x43reateUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\xe0\x01\n\x0bUserMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x11\n\tuser_name\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x14\n\x0cphone_number\x18\x07 \x01(\t\x12\x31\n\rdate_of_birth\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08state_id\x18\t \x01(\x05\x12\x0f\n\x07version\x18\n \x01(\x05\"\x9b\x01\n\x11UpdateUserRequest\x12\x14\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x14\n\x0cphone_number\x18\x05 \x01(\t\x12!\n\x08state_id\x18\x06 \x01(\x05\x42\x0f\xfa\x42\x0cJ\n\x15&\x00\x00\x00-\x00\x00\x00\x00\"J\n\x12UpdateUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12$\n\x04user\x18\x02 \x01(\x0b\x32\x16.examplepb.UserMessage\")\n\x11\x44\x65leteUserRequest\x12\x14\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01\"$\n\x12\x44\x65leteUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"&\n\x0eGetUserRequest\x12\x14\n\x02id\x18\x01 \x01(\tB\x08\xfa\x42\x05r\x03\xb0\x01\x01\"\xd3\x01\n\x0fGetUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfirst_name\x18\x02 \x01(\t\x12\x11\n\tlast_name\x18\x03 \x01(\t\x12\x11\n\tuser_name\x18\x04 \x01(\t\x12\r\n\x05\x65mail\x18\x05 \x01(\t\x12\x10\n\x08password\x18\x06 \x01(\t\x12\x14\n\x0cphone_number\x18\x07 \x01(\t\x12\x31\n\rdate_of_birth\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x08state_id\x18\t \x01(\x05\x32\xb1\x02\n\x04User\x12K\n\nCreateUser\x12\x1c.examplepb.CreateUserRequest\x1a\x1d.examplepb.CreateUserResponse\"\x00\x12K\n\nUpdateUser\x12\x1c.examplepb.UpdateUserRequest\x1a\x1d.examplepb.UpdateUserResponse\"\x00\x12K\n\nDeleteUser\x12\x1c.examplepb.DeleteUserRequest\x1a\x1d.examplepb.DeleteUserResponse\"\x00\x12\x42\n\x07GetUser\x12\x19.examplepb.GetUserRequest\x1a\x1a.examplepb.GetUserResponse\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,validate_dot_validate_dot_validate__pb2.DESCRIPTOR,])




_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='examplepb.CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='examplepb.CreateUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005r\003\260\001\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='examplepb.CreateUserRequest.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='examplepb.CreateUserRequest.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='examplepb.CreateUserRequest.user_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='examplepb.CreateUserRequest.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002`\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='examplepb.CreateUserRequest.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\004r\002\020\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='examplepb.CreateUserRequest.phone_number', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_of_birth', full_name='examplepb.CreateUserRequest.date_of_birth', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005\262\001\002\010\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state_id', full_name='examplepb.CreateUserRequest.state_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\014J\n\025&\000\000\000-\001\000\000\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=394,
)


_CREATEUSERRESPONSE = _descriptor.Descriptor(
  name='CreateUserResponse',
  full_name='examplepb.CreateUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='examplepb.CreateUserResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=396,
  serialized_end=432,
)


_USERMESSAGE = _descriptor.Descriptor(
  name='UserMessage',
  full_name='examplepb.UserMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='examplepb.UserMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='examplepb.UserMessage.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='examplepb.UserMessage.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='examplepb.UserMessage.user_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='examplepb.UserMessage.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='examplepb.UserMessage.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='examplepb.UserMessage.phone_number', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_of_birth', full_name='examplepb.UserMessage.date_of_birth', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state_id', full_name='examplepb.UserMessage.state_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='examplepb.UserMessage.version', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=435,
  serialized_end=659,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='examplepb.UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='examplepb.UpdateUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005r\003\260\001\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='examplepb.UpdateUserRequest.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='examplepb.UpdateUserRequest.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='examplepb.UpdateUserRequest.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='examplepb.UpdateUserRequest.phone_number', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state_id', full_name='examplepb.UpdateUserRequest.state_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\014J\n\025&\000\000\000-\000\000\000\000', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=817,
)


_UPDATEUSERRESPONSE = _descriptor.Descriptor(
  name='UpdateUserResponse',
  full_name='examplepb.UpdateUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='examplepb.UpdateUserResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user', full_name='examplepb.UpdateUserResponse.user', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=819,
  serialized_end=893,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='examplepb.DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='examplepb.DeleteUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005r\003\260\001\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=895,
  serialized_end=936,
)


_DELETEUSERRESPONSE = _descriptor.Descriptor(
  name='DeleteUserResponse',
  full_name='examplepb.DeleteUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='examplepb.DeleteUserResponse.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=938,
  serialized_end=974,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='examplepb.GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='examplepb.GetUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\372B\005r\003\260\001\001', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=976,
  serialized_end=1014,
)


_GETUSERRESPONSE = _descriptor.Descriptor(
  name='GetUserResponse',
  full_name='examplepb.GetUserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='examplepb.GetUserResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='examplepb.GetUserResponse.first_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='examplepb.GetUserResponse.last_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='examplepb.GetUserResponse.user_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='examplepb.GetUserResponse.email', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='examplepb.GetUserResponse.password', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='phone_number', full_name='examplepb.GetUserResponse.phone_number', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_of_birth', full_name='examplepb.GetUserResponse.date_of_birth', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state_id', full_name='examplepb.GetUserResponse.state_id', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1017,
  serialized_end=1228,
)

_CREATEUSERREQUEST.fields_by_name['date_of_birth'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_USERMESSAGE.fields_by_name['date_of_birth'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_UPDATEUSERRESPONSE.fields_by_name['user'].message_type = _USERMESSAGE
_GETUSERRESPONSE.fields_by_name['date_of_birth'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['CreateUserResponse'] = _CREATEUSERRESPONSE
DESCRIPTOR.message_types_by_name['UserMessage'] = _USERMESSAGE
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserResponse'] = _UPDATEUSERRESPONSE
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserResponse'] = _DELETEUSERRESPONSE
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUserResponse'] = _GETUSERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERREQUEST,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.CreateUserRequest)
  })
_sym_db.RegisterMessage(CreateUserRequest)

CreateUserResponse = _reflection.GeneratedProtocolMessageType('CreateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEUSERRESPONSE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.CreateUserResponse)
  })
_sym_db.RegisterMessage(CreateUserResponse)

UserMessage = _reflection.GeneratedProtocolMessageType('UserMessage', (_message.Message,), {
  'DESCRIPTOR' : _USERMESSAGE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.UserMessage)
  })
_sym_db.RegisterMessage(UserMessage)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERREQUEST,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.UpdateUserRequest)
  })
_sym_db.RegisterMessage(UpdateUserRequest)

UpdateUserResponse = _reflection.GeneratedProtocolMessageType('UpdateUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEUSERRESPONSE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.UpdateUserResponse)
  })
_sym_db.RegisterMessage(UpdateUserResponse)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERREQUEST,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.DeleteUserRequest)
  })
_sym_db.RegisterMessage(DeleteUserRequest)

DeleteUserResponse = _reflection.GeneratedProtocolMessageType('DeleteUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEUSERRESPONSE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.DeleteUserResponse)
  })
_sym_db.RegisterMessage(DeleteUserResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERREQUEST,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.GetUserRequest)
  })
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType('GetUserResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERRESPONSE,
  '__module__' : 'proto.user_pb2'
  # @@protoc_insertion_point(class_scope:examplepb.GetUserResponse)
  })
_sym_db.RegisterMessage(GetUserResponse)


_CREATEUSERREQUEST.fields_by_name['id']._options = None
_CREATEUSERREQUEST.fields_by_name['first_name']._options = None
_CREATEUSERREQUEST.fields_by_name['last_name']._options = None
_CREATEUSERREQUEST.fields_by_name['user_name']._options = None
_CREATEUSERREQUEST.fields_by_name['email']._options = None
_CREATEUSERREQUEST.fields_by_name['password']._options = None
_CREATEUSERREQUEST.fields_by_name['date_of_birth']._options = None
_CREATEUSERREQUEST.fields_by_name['state_id']._options = None
_UPDATEUSERREQUEST.fields_by_name['id']._options = None
_UPDATEUSERREQUEST.fields_by_name['state_id']._options = None
_DELETEUSERREQUEST.fields_by_name['id']._options = None
_GETUSERREQUEST.fields_by_name['id']._options = None

_USER = _descriptor.ServiceDescriptor(
  name='User',
  full_name='examplepb.User',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1231,
  serialized_end=1536,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateUser',
    full_name='examplepb.User.CreateUser',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_CREATEUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='UpdateUser',
    full_name='examplepb.User.UpdateUser',
    index=1,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=_UPDATEUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteUser',
    full_name='examplepb.User.DeleteUser',
    index=2,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=_DELETEUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUser',
    full_name='examplepb.User.GetUser',
    index=3,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_GETUSERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['User'] = _USER

# @@protoc_insertion_point(module_scope)
