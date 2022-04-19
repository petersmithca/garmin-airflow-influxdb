from datetime import datetime

from airflow.decorators import dag

from influx.tasks.extract import extract
from influx.tasks.load import load
from influx.tasks.transform import transform
from influx.utils.email import task_fail_email_alert

target = "IpGeo"


@dag(
    default_args={
        "owner": "airflow",
        "retries": 0,
        "depends_on_past": False,
        "on_failure_callback": task_fail_email_alert,
    },
    schedule_interval="14 * * * *",
    start_date=datetime(2021, 4, 7),
    catchup=False,
    max_active_runs=1,
    params={"bucket": "ip_address"},
    tags=["network", "ipaddress"],
)
def ip_geo_watcher():
    extracted = extract(prefix=target)

    transformed = transform(extract_key=extracted, prefix=target)

    load(transformed, prefix="influx_multifield")


ip_geo_watcher = ip_geo_watcher()
