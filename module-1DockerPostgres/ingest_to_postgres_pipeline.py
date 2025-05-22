import pandas as pd
from sqlalchemy import create_engine
from time import time
import argparse
import os
import pyarrow.parquet as pq




def main(params):

    user=params.user
    password=params.password
    host=params.host
    port=params.port
    database_name=params.database_name
    table_name=params.table_name
    url=params.url
    parquet_name="output.parquet"

    # url="http://172.24.127.214:8000/yellow_tripdata_2021-01.parquet"

    os.system(f"wget {url} -o {parquet_name}")

    yellow_taxi_data=pq.read_table("yellow_tripdata_2021-01.parquet")

    engine=create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database_name}')
    # # print(engine.connect())//to check whether connection is happening or not
    # print(pd.io.sql.get_schema(yellow_taxi_data,name='yellow_taxi_data',con=engine))#yellow taxi data needs to be pandas df

    chunk_size = 100000

    total_rows = yellow_taxi_data.num_rows

    counter=1
    for start in range(0, total_rows, chunk_size):
        end = min(start + chunk_size, total_rows)
        yellow_taxi_chunk = yellow_taxi_data.slice(start, end - start)
        yellow_taxi_chunk_df = yellow_taxi_chunk.to_pandas()

        t_start=time()
        yellow_taxi_chunk_df.to_sql(name=f'{table_name}',con=engine,if_exists='append')
        t_end=time()
        print(f"total time took to insert data {counter}: ",t_end-t_start)
        counter+=1
        
        # Process this DataFrame chunk
        # print(f"Rows {start} to {end}, shape: {df_chunk.shape}")
   


    print("data ingested successfully :)")




   

    

   






if __name__=="__main__":
    

    # adding argparse for params

    parser = argparse.ArgumentParser(
        description='Ingest parquet to postgres')

    parser.add_argument("--user",help="user name for postgres")
    parser.add_argument("--password",help="password for postgres")
    parser.add_argument("--host",help="host for postgres")
    parser.add_argument("--port",help="port for postgres")
    parser.add_argument("--database_name",help="database_name for postgres")
    parser.add_argument("--table_name",help="table_name for postgres")
    parser.add_argument("--url",help="url for parquet file")

    args = parser.parse_args()
    # print(args.accumulate(args.integers))

    main(args)









# print(len(yellow_taxi_data_iter))
# for i in len(yellow_taxi_data_iter):
#     print








# zone_lookup_data=pd.read_csv("taxi_zone_lookup.csv")

# print(yellow_taxi_data.tail)
# print(zone_lookup_data.head)

