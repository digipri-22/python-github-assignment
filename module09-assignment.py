# Module 9 Assignment
import pandas as pd
import numpy as np
from io import StringIO

print("=" * 60)
print("GLOBALTECH QUARTERLY SALES ANALYSIS")
print("=" * 60)

csv_content = """Date,Region,Store,Category,Product,Units,Unit_Price,Total_Sales,Promotion
2024-01-15,North America,NA001,Smartphones,PhoneX,12,899.99,10799.88,No
2024-01-18,Europe,EU002,Computers,LaptopPro,8,1299.99,10399.92,Yes
2024-01-20,Asia,AS001,Audio,WirelessEarbuds,25,149.99,3749.75,No
2024-01-22,North America,NA002,Wearables,SmartWatch,15,249.99,3749.85,No
2024-01-25,Latin America,LA001,Smartphones,PhoneX,7,899.99,6299.93,Yes
2024-01-27,Europe,EU001,Accessories,PhoneCase,35,24.99,874.65,No
2024-01-30,Asia,AS002,Smartphones,PhoneSE,18,499.99,8999.82,No
2024-02-02,North America,NA001,Computers,LaptopPro,6,1299.99,7799.94,No
2024-02-05,Europe,EU002,Wearables,SmartWatch,20,249.99,4999.80,Yes
2024-02-08,North America,NA003,Audio,WirelessEarbuds,30,149.99,4499.70,Yes
2024-02-10,Asia,AS001,Accessories,ChargingCable,45,19.99,899.55,No
2024-02-12,Latin America,LA001,Computers,TabletBasic,12,399.99,4799.88,No
2024-02-15,North America,NA002,Smartphones,PhoneSE,14,499.99,6999.86,No
2024-02-18,Europe,EU001,Audio,BlueSpeaker,22,79.99,1759.78,Yes
2024-02-20,Asia,AS002,Wearables,FitnessTracker,28,129.99,3639.72,No
2024-02-22,North America,NA001,Accessories,PhoneCase,50,24.99,1249.50,Yes
2024-02-25,Latin America,LA002,Smartphones,PhoneX,9,,8099.91,No
2024-02-28,Europe,EU002,Computers,LaptopBasic,10,899.99,8999.90,No
2024-03-02,North America,NA003,Wearables,FitnessTracker,,129.99,2599.80,Yes
2024-03-05,Asia,AS001,Smartphones,PhoneSE,15,499.99,7499.85,No
2024-03-08,Europe,EU001,Accessories,ChargingCable,60,19.99,1199.40,Yes
2024-03-10,North America,NA002,Computers,TabletPro,7,599.99,4199.93,No
2024-03-12,Latin America,LA001,Audio,WirelessEarbuds,18,149.99,2699.82,No
2024-03-15,North America,NA001,Wearables,SmartWatch,12,249.99,2999.88,No
2024-03-18,Europe,EU002,Smartphones,PhoneX,11,899.99,9899.89,Yes
2024-03-20,Asia,AS002,Computers,LaptopPro,6,1299.99,7799.94,No
2024-03-22,North America,NA001,Audio,BlueSpeaker,25,79.99,1999.75,No
2024-03-25,Latin America,LA002,Accessories,PhoneCase,40,,999.60,No"""

sales_data_csv = StringIO(csv_content)

# TODO 1: Load and Explore the Dataset
sales_df = pd.read_csv(sales_data_csv, parse_dates=['Date'])
print("\n1.1 Sales Data Loaded.")

# 1.2 Display the first 5 rows of the dataset
print("\n1.2 First 5 rows of sales_df:")
print(sales_df.head(5))

# 1.3 Display basic information about the DataFrame (info() method)
print("\n1.3 DataFrame Info:")
sales_df.info()

# 1.4 Get the dimensions of the DataFrame (number of rows and columns)
print(f"\n1.4 DataFrame Shape: {sales_df.shape}")

# 1.5 Display summary statistics for numerical columns using describe()
print("\n1.5 Summary Statistics:")
print(sales_df.describe())
print("-" * 60)

# TODO 2: Column Selection and Basic Analysis
print("\n2.1 'Product', 'Units', and 'Total_Sales' columns:")
print(sales_df[['Product', 'Units', 'Total_Sales']].head())

# 2.2 Calculate the total units sold across all records
total_units = sales_df['Units'].sum()
print(f"\n2.2 Total Units Sold: {int(total_units)}")

# 2.3 Calculate the total sales amount across all records
total_revenue = sales_df['Total_Sales'].sum()
print(f"2.3 Total Revenue: ${total_revenue:,.2f}")

# 2.4 Calculate the average unit price per product
avg_unit_price = sales_df['Unit_Price'].mean()
print(f"2.4 Average Unit Price (across non-missing records): ${avg_unit_price:.2f}")
print("-" * 60)

# TODO 3: Row Selection and Filtering
na_sales = sales_df[sales_df['Region'] == 'North America']
print(f"\n3.1 North America Sales Records: {len(na_sales)} rows")
print(na_sales[['Date', 'Product', 'Total_Sales']].head(2))

# 3.2 Select sales where Units sold is greater than 20
high_volume_sales = sales_df[sales_df['Units'] > 20]
print(f"\n3.2 High Volume Sales (> 20 Units): {len(high_volume_sales)} rows")
print(high_volume_sales[['Date', 'Product', 'Units']].head(2))

# 3.3 Select sales of the 'PhoneX' product that were on promotion
phonex_promo = sales_df[(sales_df['Product'] == 'PhoneX') & (sales_df['Promotion'] == 'Yes')]
print(f"\n3.3 PhoneX on Promotion Sales: {len(phonex_promo)} rows")
print(phonex_promo[['Date', 'Region', 'Total_Sales']])

# 3.4 Select sales from February 2024
feb_sales = sales_df[(sales_df['Date'].dt.year == 2024) & (sales_df['Date'].dt.month == 2)]
print(f"\n3.4 February 2024 Sales: {len(feb_sales)} rows")
print(feb_sales[['Date', 'Product', 'Total_Sales']].head(2))
print("-" * 60)

# TODO 4: Advanced Filtering and Analysis
total_sales_by_product = sales_df.groupby('Product')['Total_Sales'].sum()
best_product = total_sales_by_product.idxmax()
print(f"\n4.1 Best Performing Product (by Total Sales): {best_product} (Revenue: ${total_sales_by_product.max():,.2f})")

# 4.2 Calculate total sales by region and sort in descending order
sales_by_region = sales_df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
print("\n4.2 Total Sales by Region (Descending):")
print(sales_by_region.map('${:,.2f}'.format))

# 4.3 Calculate average units sold per category
avg_units_by_category = sales_df.groupby('Category')['Units'].mean().sort_values(ascending=False)
print("\n4.3 Average Units Sold by Category (Descending):")
print(avg_units_by_category.round(1))

# 4.4 Compare sales performance of items on promotion vs. not on promotion
promo_sales = sales_df[sales_df['Promotion'] == 'Yes']
no_promo_sales = sales_df[sales_df['Promotion'] == 'No']
promo_comparison = {
    'promo_avg_sales': promo_sales['Total_Sales'].mean(),
    'no_promo_avg_sales': no_promo_sales['Total_Sales'].mean(),
    'promo_total_revenue': promo_sales['Total_Sales'].sum(),
    'no_promo_total_revenue': no_promo_sales['Total_Sales'].sum()
}
print("\n4.4 Promotion Comparison:")
for key, value in promo_comparison.items():
    print(f"- {key}: ${value:,.2f}")
print("-" * 60)

# TODO 5: Missing Value Detection and Reporting
# 5.1 Identify columns with missing values and count them
missing_counts = sales_df.isnull().sum()
missing_counts = missing_counts[missing_counts > 0]
print("\n5.1 Missing Value Counts per Column:")
print(missing_counts)

# 5.2 Calculate what percentage of the data is missing in each column
missing_percentages = (sales_df.isnull().sum() / len(sales_df)) * 100
missing_percentages = missing_percentages[missing_percentages > 0].round(2)
print("\n5.2 Missing Value Percentages per Column:")
print(missing_percentages.map('{:.2f}%'.format))
print("-" * 60)

# TODO 6: Insights and Business Analysis
# 6.1 Create a summary of the top-performing category in each region
total_sales_region_category = sales_df.groupby(['Region', 'Category'])['Total_Sales'].sum()
top_categories_by_region = total_sales_region_category.groupby('Region').idxmax().apply(lambda x: x[1])

print("\n6.1 Top Performing Category in Each Region:")
print(top_categories_by_region)

# 6.2 Calculate the average unit price for each product category
avg_price_by_category = sales_df.groupby('Category')['Unit_Price'].mean().sort_values(ascending=False)
print("\n6.2 Average Unit Price by Category:")
print(avg_price_by_category.map('${:.2f}'.format))

# 6.3 For each product, calculate the total revenue and percentage of overall sales
product_revenue = sales_df.groupby('Product')['Total_Sales'].sum().rename('total_revenue')
product_percentage = (product_revenue / total_revenue) * 100
product_percentage.rename('percentage', inplace=True)
product_revenue_analysis = pd.concat([product_revenue, product_percentage], axis=1).sort_values(by='total_revenue', ascending=False)
print("\n6.3 Product Revenue and Percentage of Overall Sales:")
print(product_revenue_analysis.apply(lambda x: [f'${x["total_revenue"]:,.2f}', f'{x["percentage"]:.2f}%'], axis=1, result_type='expand').set_axis(['total_revenue', 'percentage'], axis=1))
print("-" * 60)

# TODO 7: Generate Analysis Report
print("\n" + "=" * 60)
print("GLOBALTECH Q1 2024 SALES ANALYSIS REPORT")
print("=" * 60)
avg_sale_value = total_revenue / sales_df.shape[0]

# 7.1 Display overall sales performance
print("Overall Performance:")
print(f"- Total Revenue: ${total_revenue:,.2f}")
print(f"- Total Units Sold: {int(total_units):,}")
print(f"- Average Sale Value: ${avg_sale_value:,.2f}")
print("-" * 30)

# 7.2 Display regional performance summary
print("Regional Performance:")
for region, sales in sales_by_region.items():
    print(f"{region}: ${sales:,.2f}")
print(f"\nInsight: {sales_by_region.index[0]} is the top region, generating ${sales_by_region.max():,.2f} in Q1.")
print("-" * 30)

# 7.3 Display product category performance
print("Category Performance:")
category_performance = pd.concat([avg_units_by_category, avg_price_by_category], axis=1)
category_performance.columns = ['Avg Units', 'Avg Price']
for category, row in category_performance.iterrows():
    print(f"{category}: Avg Units: {row['Avg Units']:.1f}, Avg Price: ${row['Avg Price']:,.2f}")
print(f"\nInsight: {avg_price_by_category.index[0]} has the highest average unit price (${avg_price_by_category.max():,.2f}), while {avg_units_by_category.index[0]} sells the most units on average ({avg_units_by_category.max():.1f}).")
print("-" * 30)

# 7.4 Display promotion effectiveness
print("Promotion Effectiveness:")
promo_avg_sales = promo_comparison['promo_avg_sales']
no_promo_avg_sales = promo_comparison['no_promo_avg_sales']
promo_total_revenue = promo_comparison['promo_total_revenue']
print(f"- Promoted Items Avg Sale: ${promo_avg_sales:,.2f}")
print(f"- Non-Promoted Items Avg Sale: ${no_promo_avg_sales:,.2f}")
print(f"- Revenue from Promotions: ${promo_total_revenue:,.2f}")
print(f"\nInsight: Promoted items have a lower average sale value (${promo_avg_sales:,.2f} vs ${no_promo_avg_sales:,.2f}), which may indicate promotions are used to drive volume on lower-priced goods, or that the highest sales records were non-promoted. (Note: The previous interpretation was incorrect due to the specific data values.)")
print("-" * 30)

# 7.5 Report on data quality issues
missing_cols = list(missing_counts.index)
total_missing_entries = missing_counts.sum()
print("Data Quality Report:")
if total_missing_entries > 0:
    print(f"- Missing Values Found: {missing_cols}")
    print(f"- Total Missing Entries: {total_missing_entries}")
    print(f"Note: Missing 'Units' (in {missing_counts.get('Units', 0)} records) and 'Unit_Price' (in {missing_counts.get('Unit_Price', 0)} records) will slightly distort Total Units and Average Unit Price metrics.")
else:
    print("- No critical missing values found in key financial columns.")
print("-" * 30)

# 7.6 Provide three key business recommendations based on your analysis
print("\nKEY BUSINESS RECOMMENDATIONS:")
print("1. Regional Focus: Prioritize marketing and inventory for North America and Europe, as they are the top two regions by revenue, accounting for over 50% of total sales. Investigate Latin America's lower performance.")
print("2. Product Strategy: Leverage 'PhoneX' (highest revenue product) and 'Smartphones' (top category in multiple regions) through focused marketing campaigns. Consider bundling high-volume, low-price 'Accessories' to increase basket value.")
print("3. Data Quality Improvement: Implement front-end validation to prevent missing data, especially in the 'Units' and 'Unit_Price' columns. Missing data impairs accurate inventory and pricing analysis.")
print("=" * 60)