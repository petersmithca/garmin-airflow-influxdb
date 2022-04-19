import requests

from influx.constants.connection_enum import Connection
from influx.extractors.vpn_ip_extractor import VPNIPExtractor
from influx.utils.config import Config


class VPNIPGEOExtractor(VPNIPExtractor):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ipinfo = Config.get_connection(Connection.IPINFO_API.value)
        self.ip_info_host = ipinfo.host
        self.ip_info_key = ipinfo.password

    def extract(self, headers=None, params=None, auth=None, url=None):

        ip_address = super().extract(headers=headers, params=params, auth=auth, url=url)
        ip_address = ip_address.strip()
        ip_info_url = f"{self.ip_info_host}/{ip_address}"
        params = {"token": self.ip_info_key}
        response = requests.get(ip_info_url, params=params)
        data = response.json()
        lat, long = data["loc"].split(",")
        results = {"IPLocation": ip_address, "lat": lat, "long": long, "name": "VPN IP"}
        return results
