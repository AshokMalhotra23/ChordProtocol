# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dht.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tdht.proto\x12\x03\x64ht\"\'\n\x08NodeInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"%\n\x08SuccList\x12\x19\n\x02vt\x18\x01 \x03(\x0b\x32\r.dht.NodeInfo\"\x07\n\x05\x45mpty2\xa1\x05\n\x03\x44HT\x12$\n\x04join\x12\r.dht.NodeInfo\x1a\r.dht.NodeInfo\x12\"\n\x05leave\x12\r.dht.NodeInfo\x1a\n.dht.Empty\x12%\n\x05store\x12\r.dht.KeyValue\x1a\r.dht.KeyValue\x12(\n\x08retrieve\x12\r.dht.KeyValue\x1a\r.dht.KeyValue\x12-\n\rfindSuccessor\x12\r.dht.NodeInfo\x1a\r.dht.NodeInfo\x12#\n\x06notify\x12\r.dht.NodeInfo\x1a\n.dht.Empty\x12+\n\x0egetPredecessor\x12\n.dht.Empty\x1a\r.dht.NodeInfo\x12)\n\x0cgetSuccessor\x12\n.dht.Empty\x1a\r.dht.NodeInfo\x12\'\n\ninsertData\x12\r.dht.KeyValue\x1a\n.dht.Empty\x12,\n\x0cretrieveData\x12\r.dht.KeyValue\x1a\r.dht.KeyValue\x12&\n\treplicate\x12\r.dht.KeyValue\x1a\n.dht.Empty\x12\'\n\nreplicate1\x12\r.dht.KeyValue\x1a\n.dht.Empty\x12,\n\x0fupdateSuccessor\x12\r.dht.NodeInfo\x1a\n.dht.Empty\x12.\n\x11updatePredecessor\x12\r.dht.NodeInfo\x1a\n.dht.Empty\x12-\n\x10getSuccessorList\x12\n.dht.Empty\x1a\r.dht.SuccList\x12\x1e\n\x04ping\x12\n.dht.Empty\x1a\n.dht.Emptyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'dht_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NODEINFO._serialized_start=18
  _NODEINFO._serialized_end=57
  _KEYVALUE._serialized_start=59
  _KEYVALUE._serialized_end=97
  _SUCCLIST._serialized_start=99
  _SUCCLIST._serialized_end=136
  _EMPTY._serialized_start=138
  _EMPTY._serialized_end=145
  _DHT._serialized_start=148
  _DHT._serialized_end=821
# @@protoc_insertion_point(module_scope)
