import logging


class AirflowConnectionFilter(logging.Filter):
    def filter(self, record):

        return not record.getMessage().startswith("Using connection to:")
