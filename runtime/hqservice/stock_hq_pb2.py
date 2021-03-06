# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock_hq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock_hq.proto',
  package='stock_hq',
  syntax='proto3',
  serialized_pb=_b('\n\x0estock_hq.proto\x12\x08stock_hq\";\n\x0cquery_struct\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\".\n\x0equery_realtime\x12\x0e\n\x06status\x18\x01 \x01(\x02\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\"\xdc\x04\n\thq_struct\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x02\x12\x0c\n\x04high\x18\x03 \x01(\x02\x12\x0b\n\x03low\x18\x04 \x01(\x02\x12\r\n\x05\x63lose\x18\x05 \x01(\x02\x12\x0e\n\x06volume\x18\x06 \x01(\x02\x12\x0c\n\x04\x64\x61te\x18\x07 \x01(\t\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x02\x12\x12\n\ndate_stamp\x18\t \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\n \x01(\t\x12\x12\n\ntime_stamp\x18\x0b \x01(\t\x12\x0f\n\x07message\x18\x0c \x01(\t\x12\r\n\x05price\x18\r \x01(\x02\x12\x0c\n\x04\x61sk1\x18\x0e \x01(\x02\x12\x10\n\x08\x61sk_vol1\x18\x0f \x01(\x02\x12\x0c\n\x04\x61sk2\x18\x10 \x01(\x02\x12\x10\n\x08\x61sk_vol2\x18\x11 \x01(\x02\x12\x0c\n\x04\x61sk3\x18\x12 \x01(\x02\x12\x10\n\x08\x61sk_vol3\x18\x13 \x01(\x02\x12\x0c\n\x04\x61sk4\x18\x14 \x01(\x02\x12\x10\n\x08\x61sk_vol4\x18\x15 \x01(\x02\x12\x0c\n\x04\x61sk5\x18\x16 \x01(\x02\x12\x10\n\x08\x61sk_vol5\x18\x17 \x01(\x02\x12\x12\n\nlast_close\x18\x18 \x01(\x02\x12\x0c\n\x04\x62id1\x18\x19 \x01(\x02\x12\x10\n\x08\x62id_vol1\x18\x1a \x01(\x02\x12\x0c\n\x04\x62id2\x18\x1b \x01(\x02\x12\x10\n\x08\x62id_vol2\x18\x1c \x01(\x02\x12\x0c\n\x04\x62id3\x18\x1d \x01(\x02\x12\x10\n\x08\x62id_vol3\x18\x1e \x01(\x02\x12\x0c\n\x04\x62id4\x18\x1f \x01(\x02\x12\x10\n\x08\x62id_vol4\x18  \x01(\x02\x12\x0c\n\x04\x62id5\x18! \x01(\x02\x12\x10\n\x08\x62id_vol5\x18\" \x01(\x02\x12\x0f\n\x07\x63ur_vol\x18# \x01(\x02\x12\r\n\x05\x62_vol\x18$ \x01(\x02\x12\r\n\x05s_vol\x18% \x01(\x02\x32\xd2\x02\n\x0eStockHQService\x12;\n\x0cQA_fetch_p2p\x12\x16.stock_hq.query_struct\x1a\x13.stock_hq.hq_struct\x12=\n\x0cQA_fetch_p2s\x12\x16.stock_hq.query_struct\x1a\x13.stock_hq.hq_struct0\x01\x12?\n\x0cQA_fetch_s2s\x12\x16.stock_hq.query_struct\x1a\x13.stock_hq.hq_struct(\x01\x30\x01\x12=\n\x0cQA_fetch_s2p\x12\x16.stock_hq.query_struct\x1a\x13.stock_hq.hq_struct(\x01\x12\x44\n\x11QA_fetch_realtime\x12\x18.stock_hq.query_realtime\x1a\x13.stock_hq.hq_struct0\x01\x62\x06proto3')
)




_QUERY_STRUCT = _descriptor.Descriptor(
  name='query_struct',
  full_name='stock_hq.query_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='stock_hq.query_struct.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='stock_hq.query_struct.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='stock_hq.query_struct.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=28,
  serialized_end=87,
)


_QUERY_REALTIME = _descriptor.Descriptor(
  name='query_realtime',
  full_name='stock_hq.query_realtime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='stock_hq.query_realtime.status', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='stock_hq.query_realtime.code', index=1,
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
  serialized_start=89,
  serialized_end=135,
)


_HQ_STRUCT = _descriptor.Descriptor(
  name='hq_struct',
  full_name='stock_hq.hq_struct',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='stock_hq.hq_struct.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='stock_hq.hq_struct.open', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='stock_hq.hq_struct.high', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='stock_hq.hq_struct.low', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='stock_hq.hq_struct.close', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='stock_hq.hq_struct.volume', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='stock_hq.hq_struct.date', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='stock_hq.hq_struct.amount', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_stamp', full_name='stock_hq.hq_struct.date_stamp', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='stock_hq.hq_struct.datetime', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='stock_hq.hq_struct.time_stamp', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='stock_hq.hq_struct.message', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price', full_name='stock_hq.hq_struct.price', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask1', full_name='stock_hq.hq_struct.ask1', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_vol1', full_name='stock_hq.hq_struct.ask_vol1', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask2', full_name='stock_hq.hq_struct.ask2', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_vol2', full_name='stock_hq.hq_struct.ask_vol2', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask3', full_name='stock_hq.hq_struct.ask3', index=17,
      number=18, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_vol3', full_name='stock_hq.hq_struct.ask_vol3', index=18,
      number=19, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask4', full_name='stock_hq.hq_struct.ask4', index=19,
      number=20, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_vol4', full_name='stock_hq.hq_struct.ask_vol4', index=20,
      number=21, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask5', full_name='stock_hq.hq_struct.ask5', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ask_vol5', full_name='stock_hq.hq_struct.ask_vol5', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_close', full_name='stock_hq.hq_struct.last_close', index=23,
      number=24, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid1', full_name='stock_hq.hq_struct.bid1', index=24,
      number=25, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_vol1', full_name='stock_hq.hq_struct.bid_vol1', index=25,
      number=26, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid2', full_name='stock_hq.hq_struct.bid2', index=26,
      number=27, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_vol2', full_name='stock_hq.hq_struct.bid_vol2', index=27,
      number=28, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid3', full_name='stock_hq.hq_struct.bid3', index=28,
      number=29, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_vol3', full_name='stock_hq.hq_struct.bid_vol3', index=29,
      number=30, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid4', full_name='stock_hq.hq_struct.bid4', index=30,
      number=31, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_vol4', full_name='stock_hq.hq_struct.bid_vol4', index=31,
      number=32, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid5', full_name='stock_hq.hq_struct.bid5', index=32,
      number=33, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bid_vol5', full_name='stock_hq.hq_struct.bid_vol5', index=33,
      number=34, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cur_vol', full_name='stock_hq.hq_struct.cur_vol', index=34,
      number=35, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='b_vol', full_name='stock_hq.hq_struct.b_vol', index=35,
      number=36, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s_vol', full_name='stock_hq.hq_struct.s_vol', index=36,
      number=37, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=138,
  serialized_end=742,
)

DESCRIPTOR.message_types_by_name['query_struct'] = _QUERY_STRUCT
DESCRIPTOR.message_types_by_name['query_realtime'] = _QUERY_REALTIME
DESCRIPTOR.message_types_by_name['hq_struct'] = _HQ_STRUCT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

query_struct = _reflection.GeneratedProtocolMessageType('query_struct', (_message.Message,), dict(
  DESCRIPTOR = _QUERY_STRUCT,
  __module__ = 'stock_hq_pb2'
  # @@protoc_insertion_point(class_scope:stock_hq.query_struct)
  ))
_sym_db.RegisterMessage(query_struct)

query_realtime = _reflection.GeneratedProtocolMessageType('query_realtime', (_message.Message,), dict(
  DESCRIPTOR = _QUERY_REALTIME,
  __module__ = 'stock_hq_pb2'
  # @@protoc_insertion_point(class_scope:stock_hq.query_realtime)
  ))
_sym_db.RegisterMessage(query_realtime)

hq_struct = _reflection.GeneratedProtocolMessageType('hq_struct', (_message.Message,), dict(
  DESCRIPTOR = _HQ_STRUCT,
  __module__ = 'stock_hq_pb2'
  # @@protoc_insertion_point(class_scope:stock_hq.hq_struct)
  ))
_sym_db.RegisterMessage(hq_struct)



_STOCKHQSERVICE = _descriptor.ServiceDescriptor(
  name='StockHQService',
  full_name='stock_hq.StockHQService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=745,
  serialized_end=1083,
  methods=[
  _descriptor.MethodDescriptor(
    name='QA_fetch_p2p',
    full_name='stock_hq.StockHQService.QA_fetch_p2p',
    index=0,
    containing_service=None,
    input_type=_QUERY_STRUCT,
    output_type=_HQ_STRUCT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QA_fetch_p2s',
    full_name='stock_hq.StockHQService.QA_fetch_p2s',
    index=1,
    containing_service=None,
    input_type=_QUERY_STRUCT,
    output_type=_HQ_STRUCT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QA_fetch_s2s',
    full_name='stock_hq.StockHQService.QA_fetch_s2s',
    index=2,
    containing_service=None,
    input_type=_QUERY_STRUCT,
    output_type=_HQ_STRUCT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QA_fetch_s2p',
    full_name='stock_hq.StockHQService.QA_fetch_s2p',
    index=3,
    containing_service=None,
    input_type=_QUERY_STRUCT,
    output_type=_HQ_STRUCT,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QA_fetch_realtime',
    full_name='stock_hq.StockHQService.QA_fetch_realtime',
    index=4,
    containing_service=None,
    input_type=_QUERY_REALTIME,
    output_type=_HQ_STRUCT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOCKHQSERVICE)

DESCRIPTOR.services_by_name['StockHQService'] = _STOCKHQSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class StockHQServiceStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.QA_fetch_p2p = channel.unary_unary(
          '/stock_hq.StockHQService/QA_fetch_p2p',
          request_serializer=query_struct.SerializeToString,
          response_deserializer=hq_struct.FromString,
          )
      self.QA_fetch_p2s = channel.unary_stream(
          '/stock_hq.StockHQService/QA_fetch_p2s',
          request_serializer=query_struct.SerializeToString,
          response_deserializer=hq_struct.FromString,
          )
      self.QA_fetch_s2s = channel.stream_stream(
          '/stock_hq.StockHQService/QA_fetch_s2s',
          request_serializer=query_struct.SerializeToString,
          response_deserializer=hq_struct.FromString,
          )
      self.QA_fetch_s2p = channel.stream_unary(
          '/stock_hq.StockHQService/QA_fetch_s2p',
          request_serializer=query_struct.SerializeToString,
          response_deserializer=hq_struct.FromString,
          )
      self.QA_fetch_realtime = channel.unary_stream(
          '/stock_hq.StockHQService/QA_fetch_realtime',
          request_serializer=query_realtime.SerializeToString,
          response_deserializer=hq_struct.FromString,
          )


  class StockHQServiceServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def QA_fetch_p2p(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def QA_fetch_p2s(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def QA_fetch_s2s(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def QA_fetch_s2p(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def QA_fetch_realtime(self, request, context):
      """rpc RouteChat (stream long) returns (stream long_hq);
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_StockHQServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'QA_fetch_p2p': grpc.unary_unary_rpc_method_handler(
            servicer.QA_fetch_p2p,
            request_deserializer=query_struct.FromString,
            response_serializer=hq_struct.SerializeToString,
        ),
        'QA_fetch_p2s': grpc.unary_stream_rpc_method_handler(
            servicer.QA_fetch_p2s,
            request_deserializer=query_struct.FromString,
            response_serializer=hq_struct.SerializeToString,
        ),
        'QA_fetch_s2s': grpc.stream_stream_rpc_method_handler(
            servicer.QA_fetch_s2s,
            request_deserializer=query_struct.FromString,
            response_serializer=hq_struct.SerializeToString,
        ),
        'QA_fetch_s2p': grpc.stream_unary_rpc_method_handler(
            servicer.QA_fetch_s2p,
            request_deserializer=query_struct.FromString,
            response_serializer=hq_struct.SerializeToString,
        ),
        'QA_fetch_realtime': grpc.unary_stream_rpc_method_handler(
            servicer.QA_fetch_realtime,
            request_deserializer=query_realtime.FromString,
            response_serializer=hq_struct.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'stock_hq.StockHQService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaStockHQServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def QA_fetch_p2p(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def QA_fetch_p2s(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def QA_fetch_s2s(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def QA_fetch_s2p(self, request_iterator, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def QA_fetch_realtime(self, request, context):
      """rpc RouteChat (stream long) returns (stream long_hq);
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaStockHQServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    # missing associated documentation comment in .proto file
    pass
    def QA_fetch_p2p(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    QA_fetch_p2p.future = None
    def QA_fetch_p2s(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def QA_fetch_s2s(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def QA_fetch_s2p(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    QA_fetch_s2p.future = None
    def QA_fetch_realtime(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """rpc RouteChat (stream long) returns (stream long_hq);
      """
      raise NotImplementedError()


  def beta_create_StockHQService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('stock_hq.StockHQService', 'QA_fetch_p2p'): query_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_p2s'): query_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_realtime'): query_realtime.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_s2p'): query_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_s2s'): query_struct.FromString,
    }
    response_serializers = {
      ('stock_hq.StockHQService', 'QA_fetch_p2p'): hq_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_p2s'): hq_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_realtime'): hq_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_s2p'): hq_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_s2s'): hq_struct.SerializeToString,
    }
    method_implementations = {
      ('stock_hq.StockHQService', 'QA_fetch_p2p'): face_utilities.unary_unary_inline(servicer.QA_fetch_p2p),
      ('stock_hq.StockHQService', 'QA_fetch_p2s'): face_utilities.unary_stream_inline(servicer.QA_fetch_p2s),
      ('stock_hq.StockHQService', 'QA_fetch_realtime'): face_utilities.unary_stream_inline(servicer.QA_fetch_realtime),
      ('stock_hq.StockHQService', 'QA_fetch_s2p'): face_utilities.stream_unary_inline(servicer.QA_fetch_s2p),
      ('stock_hq.StockHQService', 'QA_fetch_s2s'): face_utilities.stream_stream_inline(servicer.QA_fetch_s2s),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_StockHQService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('stock_hq.StockHQService', 'QA_fetch_p2p'): query_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_p2s'): query_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_realtime'): query_realtime.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_s2p'): query_struct.SerializeToString,
      ('stock_hq.StockHQService', 'QA_fetch_s2s'): query_struct.SerializeToString,
    }
    response_deserializers = {
      ('stock_hq.StockHQService', 'QA_fetch_p2p'): hq_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_p2s'): hq_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_realtime'): hq_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_s2p'): hq_struct.FromString,
      ('stock_hq.StockHQService', 'QA_fetch_s2s'): hq_struct.FromString,
    }
    cardinalities = {
      'QA_fetch_p2p': cardinality.Cardinality.UNARY_UNARY,
      'QA_fetch_p2s': cardinality.Cardinality.UNARY_STREAM,
      'QA_fetch_realtime': cardinality.Cardinality.UNARY_STREAM,
      'QA_fetch_s2p': cardinality.Cardinality.STREAM_UNARY,
      'QA_fetch_s2s': cardinality.Cardinality.STREAM_STREAM,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'stock_hq.StockHQService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
