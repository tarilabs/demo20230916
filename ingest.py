from ml_metadata.metadata_store import metadata_store
from ml_metadata.proto import metadata_store_pb2
import os

connection_config = metadata_store_pb2.ConnectionConfig()
connection_config.sqlite.filename_uri = os.path.join(os.getcwd(), "mlmddb")
connection_config.sqlite.connection_mode = 3
store = metadata_store.MetadataStore(connection_config)

try: 
    artifact_type_id = store.get_artifact_type("mlflow.model").id
    print("artifact_type_id was found in DB")
except metadata_store.errors.NotFoundError:
    print("artifact_type_id was not found in DB, creating...")
    new_type = metadata_store_pb2.ArtifactType()
    new_type.name = "mlflow.model"
    artifact_type_id = store.put_artifact_type(new_type)

print(f"Using {artifact_type_id} for storing artifacts")

mlflow_metadata = {
    "name": "my name",
    "version": 47,
    # Add more metadata fields as needed
}

artifact = metadata_store_pb2.Artifact()
artifact.type_id = artifact_type_id
artifact.custom_properties["something"].struct_value.update(mlflow_metadata)
[model_artifact_id] = store.put_artifacts([artifact])

print(artifact)
print(model_artifact_id)