import pandas as pd

# Data load karo
FILE_NAME = "Data/Phonepe-Messy-Dataset.xlsx"

# STEP 1: Excel se dono sheets padho
transactions = pd.read_excel(FILE_NAME, sheet_name="All_Transactions")
users = pd.read_excel(FILE_NAME, sheet_name="All_Users")

print("Transactions rows:", len(transactions))
print("Users rows:", len(users))

# PART A: TRANSACTIONS SHEET CLEAN KARO
# STEP 2: Text columns se extra spaces aur galat CAPS hatao
transactions["Service"] = transactions["Service"].str.strip()
transactions["Service Type"] = transactions["Service Type"].str.strip()
transactions["Payment_Status"] = transactions["Payment_Status"].str.strip().str.title()
transactions["Reason"] = transactions["Reason"].str.strip()
transactions["Reason"] = transactions["Reason"].str.strip().str.title()

# STEP 3: Payment_Status ko simple banao (sirf Successful/Failed)
transactions["Payment_Status"] = transactions["Payment_Status"].apply(
    lambda x: "Successful" if x == "Successful" else "Failed"
)

# STEP 4: Galat Amount wali rows hatao (blank ya negative)
before = len(transactions)
transactions = transactions.dropna(subset=["Amount"])
transactions = transactions[transactions["Amount"] > 0]
after = len(transactions)

# STEP 5: Duplicate Transaction_ID hatao
before = len(transactions)
transactions = transactions.drop_duplicates(subset="Transaction_ID", keep="first")
after = len(transactions)

# PART B: USERS SHEET CLEAN KARO
# STEP 6: Duplicate User_ID hatao
before = len(users)
users = users.drop_duplicates(subset="User_ID", keep="first")
after = len(users)

# STEP 7: Missing Age ko average age se fill karo
average_age = round(users["Age"].mean())
users["Age"] = users["Age"].fillna(average_age)
users["Age"] = users["Age"].round().astype(int)

# PART C: DONO SHEETS KO JODO (MERGE)
# STEP 8: Transactions aur Users ko User_ID se jodo
final_df = transactions.merge(users, on="User_ID", how="left")

# STEP 9: Month aur Age_Group column banao
final_df["Date"] = pd.to_datetime(final_df["Date"])
final_df["Month"] = final_df["Date"].dt.month

def get_age_group(age):
    if age <= 25:
        return "18-25"
    elif age <= 35:
        return "26-35"
    elif age <= 45:
        return "36-45"
    elif age <= 60:
        return "46-60"
    else:
        return "60+"

final_df["Age_Group"] = final_df["Age"].apply(get_age_group)

# STEP 10: Final check
print("\nStep 10: Final check...")
print("Total final rows:", len(final_df))
print("Blank values har column mein:")
print(final_df.isnull().sum())

# STEP 11: Final clean file save karo
final_df.to_csv("Data/cleaned_data.csv", index=False)
print("\n Cleaned File is READY:../Data/cleaned_data.csv")