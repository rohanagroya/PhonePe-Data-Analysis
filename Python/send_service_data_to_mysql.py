import os
import pandas as pd
from sqlalchemy import create_engine

username = os.getenv("MYSQL_USERNAME")
password = os.getenv("MYSQL_PASSWORD")

engine = create_engine(
    f"mysql+mysqlconnector://{username}:{password}@localhost/phonepe"
)

# Insurance
insurance = pd.read_csv("Data/insurance_data.csv")
insurance.to_sql("insurance", con=engine, if_exists="replace", index=False)

# Loans
loans = pd.read_csv("Data/loans_data.csv")
loans.to_sql("loans", con=engine, if_exists="replace", index=False)

# Money Transfer
transfer = pd.read_csv("Data/money_transfer_data.csv")
transfer.to_sql("money_transfer", con=engine, if_exists="replace", index=False)

# Recharge & Bills
recharge = pd.read_csv("Data/recharge_bills_data.csv")
recharge.to_sql("recharge_bills", con=engine, if_exists="replace", index=False)

print("Sab 4 tables MySQL mein chali gayi!")