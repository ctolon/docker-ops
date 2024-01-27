FROM apache/airflow:2.8.0
LABEL MAINTAINER="Cevat Batuhan Tolon <cevat.batuhan.tolon@cern.ch"
USER root

# System packages
RUN apt-get update \
  && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        vim \
        nano \
        unzip \
        rsync \
        coreutils \
        procps \
        unzip \
        software-properties-common \
        netcat \
        git \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Pip Dependencies (Mostly For Airflow External Providers)
USER airflow
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

# Create Core folders (For NFS Permissions)
ENV AIRFLOW_BASE_MNT='/mnt/airflow-nfs'
WORKDIR ${AIRFLOW_BASE_MNT}
WORKDIR ${AIRFLOW_BASE_MNT}/dags
WORKDIR ${AIRFLOW_BASE_MNT}/plugins
WORKDIR ${AIRFLOW_BASE_MNT}/logs

# Set working Directory
WORKDIR '/opt/airflow'
#RUN chown airflow:0 -R '/mnt/airflow-nfs'
#RUN chmod 777 -R '/mnt/airflow-nfs'
