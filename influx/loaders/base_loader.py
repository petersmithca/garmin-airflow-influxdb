from abc import ABC, abstractmethod


class BaseLoader(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__()

    @abstractmethod
    def load(self, records):
        """
        Formats and executes data load for record in records.

        Args:
            records (list): List of dicts in "record" format
        """
