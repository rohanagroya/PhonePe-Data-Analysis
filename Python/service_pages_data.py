import pandas as pd

# Source dataset
FILE_NAME = "Data/Phonepe-Messy-Dataset.xlsx"

# Users load karo (isko baar baar use karenge)
users = pd.read_excel(FILE_NAME, sheet_name="All_Users")
users = users.drop_duplicates()
users["Age"] = users["Age"].fillna(users["Age"].mean())

# ---------- INSURANCE ----------
insurance = pd.read_excel(FILE_NAME, sheet_name="Insurance")
insurance = insurance.drop_duplicates()
insurance = insurance.dropna(subset=["Premium"])
insurance["Payment_Status"] = insurance["Payment_Status"].str.strip().str.title()
insurance_final = pd.merge(insurance, users, on="User_ID")
insurance_final.to_csv("Data/insurance_data.csv", index=False)

# ---------- LOANS ----------
loans = pd.read_excel(FILE_NAME, sheet_name="Loans")
loans = loans.drop_duplicates()
loans = loans.dropna(subset=["Loan_Amount"])
loans["Payment_Status"] = loans["Payment_Status"].str.strip().str.title()
loans_final = pd.merge(loans, users, on="User_ID")
loans_final.to_csv("Data/loans_data.csv", index=False)

# ---------- MONEY TRANSFER ----------
transfer = pd.read_excel(FILE_NAME, sheet_name="Money_Transfer")
transfer = transfer.drop_duplicates()
transfer = transfer.dropna(subset=["Amount"])
transfer["Payment_Status"] = transfer["Payment_Status"].str.strip().str.title()
transfer_final = pd.merge(transfer, users, on="User_ID")
transfer_final.to_csv("Data/money_transfer_data.csv", index=False)

# ---------- RECHARGE & BILLS ----------
recharge = pd.read_excel(FILE_NAME, sheet_name="Recharge_Bills")
recharge = recharge.drop_duplicates()
recharge = recharge.dropna(subset=["Amount"])
recharge["Payment_Status"] = recharge["Payment_Status"].str.strip().str.title()
recharge_final = pd.merge(recharge, users, on="User_ID")
recharge_final.to_csv("Data/recharge_bills_data.csv", index=False)

print(
    "Done! 4 files ban gayi: insurance_data.csv, loans_data.csv, "
    "money_transfer_data.csv, recharge_bills_data.csv"
)