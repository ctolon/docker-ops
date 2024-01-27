"""MLFlow run_server.sh generator script for experiment level permission management

@author: Cevat Batuhan Tolon
@contact: cevat.batuhan.tolon@cern.ch
"""

import dotenv
from pathlib import Path
from pprint import pprint

# dotenv file path
current_path = Path(__file__).parent.resolve()
dotenv_path = Path(__file__).parent.parent.resolve() / ".env"

print(f"Working Path: {current_path}")
print(f"dotenv file path: {dotenv_path}")

if not dotenv_path.is_file():
    raise FileNotFoundError(f".env file not found!: {dotenv_path}")

config = dotenv.dotenv_values(dotenv_path)

print(".env file config:")
pprint(config)

database_uri = config.get("MLFLOW_TRACKING_URI")
default_bucket=  config.get("AWS_BUCKET_NAME")
mlflow_port = config.get("MLFLOW_PORT")

run_server = f"""
run() {{
  STORE_URI={database_uri}
  MLFLOW_ARTIFACT_URI={default_bucket}
  echo "STORE_URI=$STORE_URI"
  echo "MLFLOW_ARTIFACT_URI=$MLFLOW_ARTIFACT_URI"
  mlflow server --app-name=basic-auth --host 0.0.0.0 --port {mlflow_port} --backend-store-uri $STORE_URI --default-artifact-root $MLFLOW_ARTIFACT_URI --expose-prometheus /temp/prometheus_metrics
}}

run $* 2>&1 | tee server.log
"""

with open('run_server.sh', 'w') as f:
    f.write(run_server)

print("run_server.sh created.")
