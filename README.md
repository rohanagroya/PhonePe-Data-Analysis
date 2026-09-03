# PhonePe End-to-End Data Analysis

An end-to-end data analytics project built using Python, Pandas, MySQL, SQL, and Power BI to analyze PhonePe transaction and service data.

## Project Overview

This project follows a complete data analytics workflow, starting with a messy Excel dataset and ending with an interactive Power BI dashboard.

### Workflow

Excel Dataset → Python/Pandas → MySQL → SQL Analysis → Power BI

The project includes data cleaning and transformation using Python and Pandas, data storage in MySQL, SQL-based analysis, and a 5-page interactive Power BI dashboard.

---

## Dataset

The source dataset is:

`Phonepe-Messy-Dataset.xlsx`

The Excel workbook contains 6 sheets:

- All_Transactions
- All_Users
- Insurance
- Loans
- Money_Transfer
- Recharge_Bills

### Dataset Size

- Original Transactions: **300,200 records**
- Original Users: **107,708 records**
- Final cleaned and merged transaction dataset: **293,970 records**

The final transaction dataset was created after cleaning the transaction and user data, handling missing values, removing duplicates and invalid amounts, merging the datasets using `User_ID`, and creating additional columns.

A **Calendar table containing 1,461 records** was also created as part of the Power BI model.

---

## Tools & Technologies

- **Python**
- **Pandas**
- **MySQL**
- **SQL**
- **Power BI**
- **Excel**

---

## Python Data Cleaning & Transformation

Python and Pandas were used to clean and transform the data.

The main steps included:

- Loading data from different Excel sheets
- Removing duplicate Transaction IDs
- Removing duplicate User IDs
- Removing blank and negative transaction amounts
- Handling missing Age values
- Standardizing text values
- Standardizing Payment Status
- Merging transaction and user data using `User_ID`
- Converting the Date column into a proper date format
- Creating a Month column
- Creating Age Group categories

### Age Groups

The following age groups were created:

- 18-25
- 26-35
- 36-45
- 46-60
- 60+

Separate processing was also performed for:

- Insurance
- Loans
- Money Transfer
- Recharge & Bills

The processed data was prepared for loading into MySQL.

---

## MySQL Database

The cleaned data was loaded into a MySQL database named:

`phonepe`

The following 5 tables were created:

- `transactions`
- `insurance`
- `loans`
- `money_transfer`
- `recharge_bills`

The `All_Users` data from the source Excel workbook was merged with the relevant datasets during the Python processing stage rather than being stored as a separate MySQL table.

---

## SQL Analysis

SQL was used to perform analysis on the `transactions` table.

The project includes queries for:

1. Successful vs Failed Payments Count
2. Top Reasons for Failed Payments
3. Most Used Service by Total Amount
4. Failed Payments by Age Group
5. Month-wise Total Transaction Amount

The SQL queries are available in:

`SQL/phonepe_analysis.sql`

---

# Power BI Dashboard

The Power BI report contains **5 interactive pages**.

## 1. Home

The Home page provides an overall transaction overview.

It includes:

- Total Amount
- Successful Transactions
- Total Transactions
- Failed Transactions
- Services vs Amount
- Failed Payment Reasons
- Date vs Amount
- Date range filtering

### Key Insight

**Server Error** is the leading reason for failed payments on the Home dashboard, accounting for **33.71%** of failed payments.

---

## 2. Insurance

The Insurance page provides an overview of insurance-related transactions.

It includes:

- Total Amount
- Payment Status
- Failed Payment Reasons
- Total Transactions by Insurance Type
- Amount by Insurance Type
- Monthly Amount Trend

---

## 3. Loans

The Loans page analyzes loan-related transactions.

It includes:

- Total Amount
- Payment Status
- Failed Payment Reasons
- Total Transactions by Loan Type
- Amount by Loan Type
- Monthly Amount Trend

---

## 4. Money Transfer

The Money Transfer page analyzes money transfer transactions.

It includes:

- Total Amount
- Total Transaction IDs
- Payment Status
- Failed Payment Reasons
- Transfer Type
- Monthly Amount Trend

---

## 5. Recharge & Bills

The Recharge & Bills page analyzes recharge and bill payment transactions.

It includes:

- Total Amount
- Total Transactions
- Payment Status
- Failed Payment Reasons
- Recharge/Bill Service Breakdown
- Monthly Amount Trend

---

## Project Workflow

```text
PhonePe Excel Dataset
        ↓
Python + Pandas
        ↓
Data Cleaning & Transformation
        ↓
Processed Data
        ↓
MySQL Database
        ↓
SQL Analysis
        ↓
Power BI
        ↓
5-Page Interactive Dashboard
        ↓
Data Insights