import mlflow

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

from pprint import pprint
from mlflow import MlflowClient

def fetch_logged_data(run_id):
    client = MlflowClient()
    run = client.get_run(run_id)
    pprint(run.to_dictionary())
    data = run.data
    tags = {k: v for k, v in data.tags.items() if not k.startswith("mlflow.")}
    artifacts = [f.path for f in client.list_artifacts(run_id, "model")]
    return data.params, data.metrics, tags, artifacts, dict(run.info)

db = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

model = mlflow.sklearn.load_model("runs:/577dc065392a42cfbab7838321b5b3f8/model")
params, metrics, tags, artifacts, run_info = fetch_logged_data("577dc065392a42cfbab7838321b5b3f8")

pprint({"params": params, "metrics": metrics, "tags": tags, "artifacts": artifacts, "run_info": run_info})

print("model")
pprint(model)
