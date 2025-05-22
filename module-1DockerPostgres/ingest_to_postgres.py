import pandas as pd
from sqlalchemy import create_engine
from time import time


print("pandas version",pd.__version__)

yellow_taxi_data=pd.read_parquet("yellow_tripdata_2021-01.parquet")
print(yellow_taxi_data.dtypes)

engine=create_engine('postgresql://root:root@localhost:5432/ny_taxi')
# print(engine.connect())//to check whether connection is happening or not
print(pd.io.sql.get_schema(yellow_taxi_data,name='yellow_taxi_data',con=engine))

t_start=time()
yellow_taxi_data.to_sql(name='yellow_taxi_data',con=engine,if_exists='append')
t_end=time()
print("total time took to insert data:",t_start-t_end)


taxi_zone_lookup_data=pd.read_csv("taxi_zone_lookup.csv",iterator=True,chunksize=10)

print(taxi_zone_lookup_data)
pdata=next(taxi_zone_lookup_data)
print(len(pdata))






# print(len(yellow_taxi_data_iter))
# for i in len(yellow_taxi_data_iter):
#     print








# zone_lookup_data=pd.read_csv("taxi_zone_lookup.csv")

# print(yellow_taxi_data.tail)
# print(zone_lookup_data.head)

