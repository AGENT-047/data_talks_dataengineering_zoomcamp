FROM python:3.9

RUN apt-get install wget
RUN pip install --upgrade pip
RUN pip install sqlalchemy pyarrow pandas psycopg2
# RUN pip install pandas --retries 5 

WORKDIR /app
copy ingest_to_postgres_pipeline.py  ingest_to_postgres_pipeline.py


ENTRYPOINT [ "python" ,"ingest_to_postgres_pipeline.py"]

# ------to run it -----------

# docker run -it taxi_ingest:v001 \
#     --user=root \
#     --password=root \
#     --host=pgdatabase \
#     --port=5432 \
#     --db=ny_taxi \
#     --table_name=ny_taxi_trips \
#     --url=http://172.24.127.214:8000/yellow_tripdata_2021-01.parquet \
#     --network=pg-network