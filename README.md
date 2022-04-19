# InfluxDB Airflow

This airflow project was for my home use to download fitness data from Garmin on a regular interval and store it in an influxdb instance.  I also use it to track my network external IP and Geo Location and my external VPN and Geo Location.

This was done twice because my wants evolved over the iterations.

The architecture of this Airflow is modelled after ones we use in my work environment - I can't take full credit, or blame for that.


# Usage

This solution runs in docker, with docker compose.  As it was running on an internal VM, with no external access its, probably not overly secure.  I use the systemd service file below to run it.  It is listening on port 9090 (as defined in the docker-compose file) rather than the typical 8080 as I was using that already.

    [Unit]
    Description=%i service with docker compose

    [Service]
    TimeoutStartSec=0
    Restart=always
    RemainAfterExit=true
    WorkingDirectory=/home/<username>/influx-airflow/
    ExecStart=/snap/bin/docker-compose up -d --remove-orphans
    ExecStop=/snap/bin/docker-compose down

    [Install]
    WantedBy=multi-user.target

## Airflow Environment Variables.

I have all these running from local.env.  You will need to set up the smtp variables as appropriate for you.

## Airflow Connections

I've exported these to connections.json.  Of course, personal information has been redacted.

## Airflow Variables

I've exported these to variables.json.  Of course, personal information has been redacted.

## Redis Data Lake

Redis is used as a "data lake" - My work uses S3 buckets, but for my purposes, I store the data downloaded in redis and each task picks it up as needed. Typically, transformations would do more work, but in my case, I am grabbing nearly everything and storing it all, so very little was done.

## Logs and Redis Cache
You will need to create these directories yourself, and set appropriate permissions.

## Logging Cleanup
I have no real need for any long term logs.  The DAG included came from https://github.com/teamclairvoyant/airflow-maintenance-dags/blob/master/log-cleanup/airflow-log-cleanup.py with some tweaks for my own usage.

## Caveat

There is an airflow influxdb hook. However, I couldn't seem to get it to save with anything other than the current time stamp. If you know how, please let me know.  I am using the POST api in this code instead.
Also, I really don't know infludb very well (or at all) so I am probably storing and querying in less than optimal manners
