import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

#load environment variables
load_dotenv()

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = int(os.getenv("DB_PORT"))
database = os.getenv("DB_NAME")

engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{database}")

#query & clean data
query_train = "SELECT * FROM mobile_prices_train"
df_train = pd.read_sql(query_train, engine)
df_train = df_train.dropna()
df_train.to_csv("./data/cleaned_train.csv", index=False)
print("cleaned data saved to ../data/cleaned_train.csv")

query_test = "SELECT * FROM mobile_prices_test"
df_test = pd.read_sql(query_test, engine)
df_test = df_test.dropna()
df_test.to_csv("./data/cleaned_test.csv", index=False)
print("cleaned data saved to ../data/cleaned_test.csv")






