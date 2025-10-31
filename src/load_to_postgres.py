import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#load csv
csv_file = "./data/mobile_pricing_train.csv"
train_df = pd.read_csv(csv_file)
print(f"loaded {len(train_df)} rows from {csv_file}")

csv_file = "./data/mobile_pricing_test.csv"
test_df = pd.read_csv(csv_file)
print(f"loaded {len(test_df)} rows from {csv_file}")

#connection engine
load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")
engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

#load into database
table_name_train = "mobile_prices_train"
train_df.to_sql(table_name_train, engine, if_exists="replace", index=False)
print(f"Data loaded into table {table_name_train} in database '{database}' ")

table_name_test = "mobile_prices_test"
train_df.to_sql(table_name_test, engine, if_exists="replace", index=False)
print(f"Data loaded into table {table_name_test} in database '{database}' ")