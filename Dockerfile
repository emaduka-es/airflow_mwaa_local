FROM apache/airflow:2.7.3

ENV AIRFLOW_HOME=/opt/airflow

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        vim \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER $AIRFLOW_UID

COPY requirements.txt .

RUN pip install -r requirements.txt

SHELL ["/bin/bash", "-o", "pipefail", "-e", "-u", "-x", "-c"]

WORKDIR $AIRFLOW_HOME

USER $AIRFLOW_UID