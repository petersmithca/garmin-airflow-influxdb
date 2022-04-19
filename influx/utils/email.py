from airflow.utils.email import send_email

from influx.constants.variable_enum import Variable
from influx.utils.config import Config


def task_fail_email_alert(context):
    """
    Emails the task failure report.
    """
    email_addresses = Config.get_variable(Variable.EMAIL_ALERT_ADDRESSES.value)

    send_email(email_addresses, "Dag Failure", f'*Exception*: {context.get("exception")}')
