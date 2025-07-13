FROM python:3.9

RUN apt-get install wget
RUN pip install --upgrade pip
RUN pip install sqlalchemy pyarrow pandas psycopg2
# RUN pip install pandas --retries 5 

WORKDIR /app
copy ingest_to_postgres_pipeline_2.py  ingest_to_postgres_pipeline_2.py


ENTRYPOINT [ "python" ,"ingest_to_postgres_pipeline_2.py"]

# ------to run it -----------

# docker run -it \
#     --network=pg-network \
#   taxi_ingest:v001 \
#     --user=root \
#     --password=root \
#     --host=pgdatabase \
#     --port=5432 \
#     --database_name=ny_taxi \
#     --table_name=ny_taxi_trips \
#     --url=http://172.24.127.214:8000/yellow_tripdata_2021-01.parquet
#     


docker run -it \
    --network=something_default # (if you are using docker compose)
  taxi_ingest:v002 \
    --user=root \
    --password=root \
    --host=pgdatabase \
    --port=5432 \
    --database_name=ny_taxi \
    --table_name=zone_lookup_table \
    --url=https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv