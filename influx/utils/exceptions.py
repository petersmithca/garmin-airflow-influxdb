class FactoryException(Exception):
    """Exception for when a Factory cannot find the correct subclass"""


class FeedExtractorException(Exception):
    """Exception for when a sensor fails to retrieve the required info"""


class HTTPResponseException(Exception):
    """Exception for Invalid Response from API"""


class InvalidDataException(Exception):
    """Exception for when a request contains invalid data"""


class InfluxLoaderException(Exception):
    """Exception for when influx returns a bad response"""
