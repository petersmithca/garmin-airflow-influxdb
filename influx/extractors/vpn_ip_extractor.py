from influx.constants.connection_enum import Connection
from influx.extractors.ip_extractor import IPExtractor


class VPNIPExtractor(IPExtractor):
    server = Connection.VPNSERVER.value
