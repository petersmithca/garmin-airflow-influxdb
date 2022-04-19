from airflow.operators.python import get_current_context
from garminconnect import Garmin

from influx.constants.connection_enum import Connection
from influx.extractors.base_extractor import BaseExtractor
from influx.utils.config import Config


class GarminExtractor(BaseExtractor):
    """
    A processor responsible for downloading Garmin Data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        garmin = Config.get_connection(Connection.GARMIN.value)
        self.user = garmin.login
        self.password = garmin.password
        self.conn = self.get_conn()

    def extract(self, headers=None, params=None, auth=None, url=None):

        context = get_current_context()
        task = self.task.format(extract_date=context["execution_date"])
        data = eval(f"self.conn.{task}")
        return data

    def get_conn(self):
        client = Garmin(self.user, self.password)
        client.login()
        return client
