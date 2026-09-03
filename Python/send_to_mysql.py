import os
import pandas as pd
from sqlalchemy import create_engine

username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")

engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@localhost/phonepe"
)

# Load cleaned transaction data
data = pd.read_csv("Data/cleaned_data.csv")

# Upload data to MySQL
data.to_sql("transactions", con=engine, if_exists="replace", index=False)

print("Data MySQL mein chala gaya")