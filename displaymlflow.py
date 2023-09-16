import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

from pprint import pprint
from mlflow import MlflowClient

def fetch_logged_data(run_id):
    client = MlflowClient()
    data = client.get_run(run_id).data
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    return data.params, data.metrics, tags, artifacts

db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

model = mlflow.sklearn.load_model("runs:/577dc065392a42cfbab7838321b5b3f8/model")
params, metrics, tags, artifacts = fetch_logged_data("577dc065392a42cfbab7838321b5b3f8")

print("params")
pprint(params)

print("metrics")

print("tags")
pprint(tags)

print("artifacts")
pprint(artifacts)

print("model")
pprint(model)
