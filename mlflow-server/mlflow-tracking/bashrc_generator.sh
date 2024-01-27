#!/bin/bash

source .env

echo "Copy and paste below configuration into your ~/.bashrc file!"
echo ""
echo "# MLFLOW CONFIG"
echo "export AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID"
echo "export AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY"
echo "export MLFLOW_S3_ENDPOINT_URL=$MLFLOW_S3_ENDPOINT_URL"
echo "export MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI"
echo "export MLFLOW_TRACKING_USERNAME=$MLFLOW_TRACKING_USERNAME"
echo "export MLFLOW_TRACKING_PASSWORD=$MLFLOW_TRACKING_PASSWORD"
echo "# END MLFLOW CONFIG"