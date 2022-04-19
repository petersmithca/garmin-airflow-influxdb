FROM apache/airflow:2.2.5-python3.8

ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

USER root

ENV ACCEPT_EULA Y

RUN set -ex \
    && apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install -yqq --no-install-recommends \
        freetds-bin \
        build-essential \
        default-libmysqlclient-dev

USER airflow

COPY ./requirements.txt ./requirements.txt

# The DAGs are embedded in the image
COPY ./dags /opt/airflow/dags/
COPY ./influx /opt/airflow/plugins/influx/

RUN pip install --upgrade pip \
    && pip install -r ./requirements.txt
