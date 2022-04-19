import time

import pytz
import requests
from dateutil import parser

from influx.constants.connection_enum import Connection
from influx.loaders.base_loader import BaseLoader
from influx.utils.config import Config
from airflow.operators.python import get_current_context
from influx.utils.exceptions import InfluxLoaderException


class InfluxLoader(BaseLoader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        conn = Config.get_connection(Connection.INFLUXDB.value)
        self.host = conn.host
        self.port = conn.port
        self.schema = conn.schema
        extra = conn.extra_dejson
        self.org = extra["org_name"]
        self.token = extra["token"]
        self.bucket = kwargs["bucket"]

    def load(self, records):
        url = f"{self.schema}://{self.host}:{self.port}/api/v2/write"
        params = {"org": self.org, "bucket": self.bucket}
        headers = {
            "Accept": "application/json",
            "Content-Type": "text/plain; charset=utf-8",
            "Authorization": f"Token {self.token}",
        }

        timestamp = int(time.time_ns())
        for record in records:
            tag = record.pop("tag", None)

            timestamp = self.get_timestamp(record, timestamp)
            print(record)
            for k, v in record.items():
                if not isinstance(v, list):
                    data = f'{k}="{v}" {timestamp}'
                    if tag:
                        data = f"{k},{tag}={record[tag]} {data}"
                    else:
                        data = f"{k} {data}"

                    response = requests.post(url, params=params, headers=headers, data=data)
                    if response.status_code != 204:
                        raise InfluxLoaderException(response.text)

    def get_timestamp(self, record, timestamp):

        if "startTimeGMT" in record:
            dt = parser.parse(record["startTimeGMT"])
            gmt = pytz.timezone("GMT")
            dt = gmt.localize(dt)
            timestamp = int(dt.timestamp() * 1000000000)
        elif "wellnessEndTimeGmt" in record:
            dt = parser.parse(record["wellnessEndTimeGmt"])
            gmt = pytz.timezone("GMT")
            dt = gmt.localize(dt)
            timestamp = int(dt.timestamp() * 1000000000)
        else:
            context = get_current_context()
            dt = context["execution_date"]
            timestamp = int(dt.timestamp() * 1000000000)
        return timestamp
