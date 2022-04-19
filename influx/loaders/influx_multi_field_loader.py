import time

import requests

from influx.loaders.influx_loader import InfluxLoader
from influx.utils.exceptions import InfluxLoaderException


class InfluxMultiFieldLoader(InfluxLoader):
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

            data = ",".join(f'{k}="{v}"' for k, v in record.items() if not isinstance(v, list))
            data = f"{data} {timestamp}"
            if tag:
                data = f"{list(record.keys())[0]},{tag}={record[tag]} {data}"
            else:
                data = f"{list(record.keys())[0]} {data}"

            response = requests.post(url, params=params, headers=headers, data=data)
            if response.status_code != 204:
                raise InfluxLoaderException(response.text)
