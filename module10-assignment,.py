# Module 10 Assignment: Data Manipulation and Cleaning with Pandas
# UrbanStyle Customer Data Cleaning
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime
from io import StringIO
import re
print("=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING")
print("=" * 60)

# ----- USE THE FOLLOWING CODE TO SIMULATE A CSV FILE (DO NOT MODIFY) -----
# Simulated CSV content with intentional data issues
csv_content = """customer_id,first_name,last_name,email,phone,join_date,last_purchase,total_purchases,total_spent,preferred_category,satisfaction_rating,age,city,state,loyalty_status
CS001,John,Smith,johnsmith@email.com,(555) 123-4567,2023-01-15,2023-12-01,12,"1,250.99",Menswear,4.5,35,Tampa,FL,Gold
CS002,Emily,Johnson,emily.j@email.com,555.987.6543,01/25/2023,10/15/2023,8,$875.50,Womenswear,4,28,Miami,FL,Silver
CS003,Michael,Williams,mw@email.com,(555)456-7890,2023-02-10,2023-11-20,15,"2,100.75",Footwear,5,42,Orlando,FL,Gold
CS004,JESSICA,BROWN,jess.brown@email.com,5551234567,2023-03-05,2023-12-10,6,659.25,Womenswear,3.5,31,Tampa,FL,Bronze
CS005,David,jones,djones@email.com,555-789-1234,2023-03-20,2023-09-18,4,350.00,Menswear,,45,Jacksonville,FL,Bronze
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS007,Robert,Davis,robert.davis@email.com,555.444.7777,04/30/2023,11/25/2023,7,$725.80,Footwear,4.5,38,Miami,FL,Silver
CS008,Jennifer,Garcia,jen.garcia@email.com,(555)876-5432,2023-05-15,2023-10-30,3,280.50,ACCESSORIES,3,25,Orlando,FL,Bronze
CS009,Michael,Williams,m.williams@email.com,5558889999,2023-06-01,2023-12-07,9,1100.00,Menswear,4,39,Jacksonville,FL,Silver
CS010,Emily,Johnson,emilyjohnson@email.com,555-321-6547,2023-06-15,2023-12-15,14,"1,875.25",Womenswear,4.5,27,Miami,FL,Gold
CS006,Sarah,Miller,sarah_miller@email.com,(555) 234-5678,2023-04-12,2023-12-05,10,1450.30,Accessories,4,29,Tampa,FL,Silver
CS011,Amanda,,amanda.p@email.com,(555) 741-8529,2023-07-10,,2,180.00,womenswear,3,32,Tampa,FL,Bronze
CS012,Thomas,Wilson,thomas.w@email.com,,2023-07-25,2023-11-02,5,450.75,menswear,4,44,Orlando,FL,Bronze
CS013,Lisa,Anderson,lisa.a@email.com,555.159.7530,08/05/2023,,0,0.00,Womenswear,,30,Miami,FL,
CS014,James,Taylor,jtaylor@email.com,555-951-7530,2023-08-20,2023-10-10,11,"1,520.65",Footwear,4.5,,Jacksonville,FL,Gold
CS015,Karen,Thomas,karen.t@email.com,(555) 357-9512,2023-09-05,2023-12-12,6,685.30,Womenswear,4,36,Tampa,FL,Silver"""

# Create a StringIO object (simulates a file)
customer_data_csv = StringIO(csv_content)

# ----- END OF SIMULATION CODE -----

initial_missing_counts = None
initial_duplicate_count = 0
missing_value_report = None
satisfaction_median = 0.0
date_fill_strategy = 'N/A'
df_no_missing = None
df_typed = None
phone_format = '(555) 555-5555'
duplicate_count = 0
df_no_duplicates = None
df_text_cleaned = None
df_renamed = None
df_final = None
avg_spent_by_loyalty = None
category_revenue = None
satisfaction_spend_corr = 0.0

# TODO 1: Load and Explore the Dataset
# 1.1 Load the dataset and display basic information
raw_df = pd.read_csv(customer_data_csv)
print("\n" + "=" * 25 + " INITIAL DATA EXPLORATION " + "=" * 25)
print("\nRaw Data Info:")
print(raw_df.info()) 
print("\nRaw Data Head:")
print(raw_df.head())

# 1.2 Assess the data quality issues (missing values, incorrect formats, duplicates)
initial_missing_counts = raw_df.isnull().sum().
initial_duplicate_count = raw_df.duplicated(keep=False).sum()
customer_data_csv.seek(0)
raw_df = pd.read_csv(customer_data_csv)


# TODO 2: Handle Missing Values
# 2.1 Identify and count missing values
missing_value_report = raw_df.isnull().sum()

# 2.2 Fill missing satisfaction_rating with the median value
satisfaction_median = raw_df['satisfaction_rating'].median()
raw_df['satisfaction_rating'] = raw_df['satisfaction_rating'].fillna(satisfaction_median)

# 2.3 Fill missing last_purchase dates appropriately
date_fill_strategy = 'drop' 

# 2.4 Handle other missing values as needed
median_age = raw_df['age'].median()
raw_df['age'] = raw_df['age'].fillna(median_age)
raw_df['loyalty_status'] = raw_df['loyalty_status'].fillna('Bronze')
raw_df['last_name'] = raw_df['last_name'].fillna('Unknown')
raw_df = raw_df.drop(raw_df[(raw_df['last_purchase'].isnull()) & (raw_df['total_purchases'] > 0)].index)
df_no_missing = raw_df.copy()
df_no_missing['join_date'] = pd.to_datetime(df_no_missing['join_date'], errors='coerce')
df_no_missing['last_purchase'] = pd.to_datetime(df_no_missing['last_purchase'], errors='coerce', dayfirst=True)
df_no_missing['last_purchase'] = df_no_missing['last_purchase'].fillna(df_no_missing['join_date'])


# TODO 3: Correct Data Types
df_typed = df_no_missing.copy()

# 3.1 Convert join_date and last_purchase to datetime 
df_typed['join_date'] = pd.to_datetime(df_typed['join_date'], errors='coerce')
df_typed['last_purchase'] = pd.to_datetime(df_typed['last_purchase'], errors='coerce', dayfirst=True)

# 3.2 Convert total_spent to numeric 
df_typed['total_spent'] = df_typed['total_spent'].astype(str).str.replace(r'[$,]', '', regex=True)
df_typed['total_spent'] = pd.to_numeric(df_typed['total_spent'], errors='coerce')

# 3.3 Ensure other numeric fields (total_purchases, age) are correct types
df_typed['total_purchases'] = df_typed['total_purchases'].astype(int)
df_typed['age'] = df_typed['age'].astype(int)
print("\n" + "=" * 25 + " DATA TYPES AFTER CONVERSION " + "=" * 25)
print(df_typed.info())


# TODO 4: Clean and Standardize Text Data
df_text_cleaned = df_typed.copy()

# 4.1 Standardize case for first_name and last_name (proper case)
df_text_cleaned['first_name'] = df_text_cleaned['first_name'].str.title()
df_text_cleaned['last_name'] = df_text_cleaned['last_name'].str.title()

# 4.2 Standardize category names (consistent capitalization)
df_text_cleaned['preferred_category'] = df_text_cleaned['preferred_category'].str.title()

# 4.3 Standardize phone numbers to a consistent format (e.g., (555) 555-5555)
def clean_and_format_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r'\D', '', str(phone))
    if len(digits) == 10:
        return f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    return phone

df_text_cleaned['phone'] = df_text_cleaned['phone'].apply(clean_and_format_phone)
phone_format = '(XXX) XXX-XXXX'


# TODO 5: Remove Duplicates
# 5.1 Identify duplicate records
duplicate_count = df_text_cleaned.duplicated(subset=['customer_id']).sum() 

# 5.2 Remove duplicates while keeping the appropriate record
df_no_duplicates = df_text_cleaned.drop_duplicates(subset=['customer_id'], keep='first').copy()


# TODO 6: Add Derived Features
df_final_working = df_no_duplicates.copy()
analysis_date = pd.to_datetime('2023-12-16')

# 6.1 Calculate days_since_last_purchase
df_final_working['days_since_last_purchase'] = (analysis_date - df_final_working['last_purchase']).dt.days

# 6.2 Calculate average_purchase_value (total_spent / total_purchases)
df_final_working['average_purchase_value'] = np.where(
    df_final_working['total_purchases'] > 0,
    df_final_working['total_spent'] / df_final_working['total_purchases'],
    0.0
)
df_final_working['average_purchase_value'] = df_final_working['average_purchase_value'].round(2)

# 6.3 Create a purchase_frequency_category (High, Medium, Low)
def categorize_frequency(purchases):
    if purchases >= 10:
        return 'High'
    elif 5 <= purchases <= 9:
        return 'Medium'
    else:
        return 'Low'

df_final_working['purchase_frequency_category'] = df_final_working['total_purchases'].apply(categorize_frequency)


# TODO 7: Clean Up the DataFrame
# 7.1 Rename columns to more readable formats
column_rename_map = {
    'customer_id': 'Customer_ID',
    'first_name': 'First_Name',
    'last_name': 'Last_Name',
    'email': 'Email',
    'phone': 'Phone',
    'join_date': 'Join_Date',
    'last_purchase': 'Last_Purchase_Date',
    'total_purchases': 'Total_Purchases',
    'total_spent': 'Total_Spent', 
    'preferred_category': 'Preferred_Category',
    'satisfaction_rating': 'Satisfaction_Rating',
    'age': 'Age',
    'city': 'City',
    'state': 'State',
    'loyalty_status': 'Loyalty_Status',
    'days_since_last_purchase': 'Days_Since_Last_Purchase',
    'average_purchase_value': 'Average_Purchase_Value',
    'purchase_frequency_category': 'Purchase_Frequency'
}
df_renamed = df_final_working.rename(columns=column_rename_map)

# 7.2 Remove any unnecessary columns
df_final = df_renamed.drop(columns=['Email'])

# 7.3 Sort the data by a meaningful attribute
df_final = df_final.sort_values(by='Total_Spent', ascending=False).reset_index(drop=True)


# TODO 8: Generate Insights from Cleaned Data
# 8.1 Calculate average spent by loyalty_status
avg_spent_by_loyalty = df_final.groupby('Loyalty_Status')['Total_Spent'].mean().sort_values(ascending=False).round(2)

# 8.2 Find top preferred categories by total_spent
category_revenue = df_final.groupby('Preferred_Category')['Total_Spent'].sum().sort_values(ascending=False).round(2)

# 8.3 Calculate correlation between satisfaction_rating and total_spent
satisfaction_spend_corr = df_final[['Satisfaction_Rating', 'Total_Spent']].corr().iloc[0, 1].round(4)


# TODO 9: Generate Final Report
print("\n" + "=" * 60)
print("URBANSTYLE CUSTOMER DATA CLEANING REPORT")
print("=" * 60)

# 9.1 Report on data quality issues found and how they were addressed
total_missing_entries = initial_missing_counts.sum()
data_type_issues = ['total_spent (string w/ currency/commas)', 'join_date/last_purchase (mixed format strings)', 'age (mixed types/missing)']
print("Data Quality Issues:")
print(f"- **Missing Values:** {total_missing_entries} total missing entries found across 6 columns.")
print(f"  - **Strategy:** Median imputation for `Satisfaction_Rating` and `Age`. 'Bronze' fill for `Loyalty_Status`. 'Unknown' for `Last_Name`. Dropped one row with unrecoverable `Last_Purchase_Date` (CS011).")
print(f"- **Duplicates:** {initial_duplicate_count} duplicate records found (based on full row match).")
print(f"  - **Strategy:** {duplicate_count} customer_id duplicates found (CS006) and removed, keeping the first occurrence.")
print(f"- **Data Type Issues:** {', '.join(data_type_issues)}")

print("\n" + "-" * 60)

# 9.2 Describe the changes made to standardize the dataset
print("Standardization Changes:")

print("- **Names:** Converted `First_Name` and `Last_Name` to proper case (Title Case).")
print("- **Categories:** Standardized `Preferred_Category` names to Title Case (e.g., 'womenswear' -> 'Womenswear').")
print(f"- **Phone Numbers:** Standardized phone numbers to the format: {phone_format}.")
print("- **Monetary Values:** Removed currency symbols ('$', ',') and converted `Total_Spent` to float.")
print("- **Dates:** Converted `Join_Date` and `Last_Purchase_Date` to datetime objects, handling mixed formats.")

print("\n" + "-" * 60)

# 9.3 Present key business insights from the cleaned data
print("Key Business Insights:")

print(f"- **Customer Base:** {len(df_final)} total customers")
print("- **Revenue by Loyalty:**")
print(avg_spent_by_loyalty.to_string(header=False))
print(f"- **Top Category:** {category_revenue.index[0]} with ${category_revenue.iloc[0]:,.2f} total revenue")
print(f"- **Satisfaction vs. Spend:** Correlation between `Satisfaction_Rating` and `Total_Spent` is **{satisfaction_spend_corr}**")

print("\n" + "-" * 60)

# 9.4 Display the first few rows of the clean, analysis-ready dataset
print("Final Cleaned Dataset (Top 5 Rows):")
pd.options.display.float_format = '${:,.2f}'.format
print(df_final.head())
pd.options.display.float_format = None

print(f"\nFinal df_final shape: {df_final.shape}")