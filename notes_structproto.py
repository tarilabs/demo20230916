from ml_metadata.proto import metadata_store_pb2
from google.protobuf.struct_pb2 import Struct

some_metadata = {
    "name": "my name",
    "version": 47,
}

artifact = metadata_store_pb2.Artifact()
s = Struct()
s.update(some_metadata)
artifact.custom_properties["something"].proto_value.Pack(s)
print(artifact)
# custom_properties {
#  key: "something"
#  value {
#   proto_value {
#      type_url: "type.googleapis.com/google.protobuf.Struct"
#      value: "\n\021\n\004name\022\t\032\007my name\n\024\n\007version\022\t\021\000\000\000\000\000\200G@"
#    }
#  }
# }
print(dir(artifact))