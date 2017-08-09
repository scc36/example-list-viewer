# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: restaurantlist.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='restaurantlist.proto',
  package='infatuation.list',
  syntax='proto3',
  serialized_pb=_b('\n\x14restaurantlist.proto\x12\x10infatuation.list\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb6\x01\n\x04List\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12+\n\x05\x62lurb\x18\x03 \x01(\x0b\x32\x1c.infatuation.list.Annotation\x12,\n\x08metadata\x18\x04 \x01(\x0b\x32\x1a.infatuation.list.Metadata\x12%\n\x05items\x18\x05 \x03(\x0b\x32\x16.infatuation.list.Item\x12\x11\n\timage_url\x18\x06 \x01(\t\"l\n\x04Item\x12\x15\n\x0binfatuation\x18\x01 \x01(\x05H\x00\x12\x14\n\nfoursquare\x18\x02 \x01(\tH\x00\x12\x31\n\x0b\x61nnotations\x18\x03 \x03(\x0b\x32\x1c.infatuation.list.AnnotationB\x04\n\x02id\"\xb7\x01\n\x08Metadata\x12\'\n\x07\x63reator\x18\x01 \x01(\x0b\x32\x16.infatuation.list.User\x12(\n\x08\x61udience\x18\x02 \x03(\x0b\x32\x16.infatuation.list.User\x12+\n\x07\x63reated\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12+\n\x07updated\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\" \n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"n\n\nAnnotation\x12$\n\x04user\x18\x01 \x01(\x0b\x32\x16.infatuation.list.User\x12\x0b\n\x03msg\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampB\x0e\xa2\x02\x0bInfatuationb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_LIST = _descriptor.Descriptor(
  name='List',
  full_name='infatuation.list.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='infatuation.list.List.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='label', full_name='infatuation.list.List.label', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blurb', full_name='infatuation.list.List.blurb', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='infatuation.list.List.metadata', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='items', full_name='infatuation.list.List.items', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='image_url', full_name='infatuation.list.List.image_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=76,
  serialized_end=258,
)


_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='infatuation.list.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='infatuation', full_name='infatuation.list.Item.infatuation', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='foursquare', full_name='infatuation.list.Item.foursquare', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='annotations', full_name='infatuation.list.Item.annotations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
      name='id', full_name='infatuation.list.Item.id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=260,
  serialized_end=368,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='infatuation.list.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='infatuation.list.Metadata.creator', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='audience', full_name='infatuation.list.Metadata.audience', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created', full_name='infatuation.list.Metadata.created', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated', full_name='infatuation.list.Metadata.updated', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=371,
  serialized_end=554,
)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='infatuation.list.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='infatuation.list.User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='infatuation.list.User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=556,
  serialized_end=588,
)


_ANNOTATION = _descriptor.Descriptor(
  name='Annotation',
  full_name='infatuation.list.Annotation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='infatuation.list.Annotation.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='msg', full_name='infatuation.list.Annotation.msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='infatuation.list.Annotation.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=590,
  serialized_end=700,
)

_LIST.fields_by_name['blurb'].message_type = _ANNOTATION
_LIST.fields_by_name['metadata'].message_type = _METADATA
_LIST.fields_by_name['items'].message_type = _ITEM
_ITEM.fields_by_name['annotations'].message_type = _ANNOTATION
_ITEM.oneofs_by_name['id'].fields.append(
  _ITEM.fields_by_name['infatuation'])
_ITEM.fields_by_name['infatuation'].containing_oneof = _ITEM.oneofs_by_name['id']
_ITEM.oneofs_by_name['id'].fields.append(
  _ITEM.fields_by_name['foursquare'])
_ITEM.fields_by_name['foursquare'].containing_oneof = _ITEM.oneofs_by_name['id']
_METADATA.fields_by_name['creator'].message_type = _USER
_METADATA.fields_by_name['audience'].message_type = _USER
_METADATA.fields_by_name['created'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_METADATA.fields_by_name['updated'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ANNOTATION.fields_by_name['user'].message_type = _USER
_ANNOTATION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['List'] = _LIST
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['Annotation'] = _ANNOTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
  DESCRIPTOR = _LIST,
  __module__ = 'restaurantlist_pb2'
  # @@protoc_insertion_point(class_scope:infatuation.list.List)
  ))
_sym_db.RegisterMessage(List)

Item = _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), dict(
  DESCRIPTOR = _ITEM,
  __module__ = 'restaurantlist_pb2'
  # @@protoc_insertion_point(class_scope:infatuation.list.Item)
  ))
_sym_db.RegisterMessage(Item)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'restaurantlist_pb2'
  # @@protoc_insertion_point(class_scope:infatuation.list.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'restaurantlist_pb2'
  # @@protoc_insertion_point(class_scope:infatuation.list.User)
  ))
_sym_db.RegisterMessage(User)

Annotation = _reflection.GeneratedProtocolMessageType('Annotation', (_message.Message,), dict(
  DESCRIPTOR = _ANNOTATION,
  __module__ = 'restaurantlist_pb2'
  # @@protoc_insertion_point(class_scope:infatuation.list.Annotation)
  ))
_sym_db.RegisterMessage(Annotation)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\242\002\013Infatuation'))
# @@protoc_insertion_point(module_scope)