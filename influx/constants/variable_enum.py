from enum import Enum


class Variable(Enum):
    """
    Variable enum corresponding to airflow variables
    """

    EMAIL_ALERT_ADDRESSES = "email_alert_addresses"
