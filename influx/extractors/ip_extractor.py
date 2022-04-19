import paramiko

from influx.constants.connection_enum import Connection
from influx.extractors.base_extractor import BaseExtractor
from influx.utils.config import Config
from influx.utils.exceptions import FeedExtractorException


class IPExtractor(BaseExtractor):

    server = Connection.IPSERVER.value
    command = "dig +short myip.opendns.com @resolver1.opendns.com"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        server_config = Config.get_connection(self.server)
        self.host = server_config.host
        self.user = server_config.login
        self.password = server_config.password

    def extract(self, headers=None, params=None, auth=None, url=None):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=self.host, username=self.user, password=self.password)

        stdin, stdout, stderr = client.exec_command(self.command)
        result = stdout.read().decode()
        err = stderr.read().decode()
        if err:
            raise FeedExtractorException(err)

        return result
