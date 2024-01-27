FROM python:3.8.5
MAINTAINER "Cevat Batuhan tolon | cevat.batuhan.tolon@cern.ch"
RUN apt-get update

# BASIC PACKAGES
RUN python -m pip install --upgrade setuptools pip
RUN apt-get install git

# python c deps
#RUN apk add --no-cache alpine-sdk postgresql-dev postgresql-client openssh openssl-dev 

# PERFORMANCE PROVIDERS (BEST PRACTICE)
#RUN apt-get install libyaml-cpp-dev libyaml-dev

RUN python -m pip install mlflow==2.3.2
RUN python -m pip install boto3
RUN python -m pip install protobuf==3.20.*
RUN python -m pip install psycopg2
RUN python -m pip install prometheus-flask-exporter
RUN python -m pip install dvc[all]

# RUN SERVER BASH SCRIPT
COPY run_server.sh .
RUN chmod +x ./run_server.sh

# MLFLOW AUTH CONFIG INI
COPY auth_config.ini .



