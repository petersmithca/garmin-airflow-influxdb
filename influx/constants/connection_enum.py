from enum import Enum


class Connection(Enum):
    """
    Connection enum corresponding to airflow connections
    """

    REDIS = "redis"
    GARMIN = "garmin"
    INFLUXDB = "influxdb"
    IPSERVER = "ipserver"
    VPNSERVER = "vpnserver"
    IPINFO_API = "ipinfo_api"
