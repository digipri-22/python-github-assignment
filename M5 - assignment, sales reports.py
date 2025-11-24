# Module 5 Assignment: Loops and Repetition in Business Applications
# QuickMart Sales Analysis

# Welcome message
print("=" * 60)
print("QUICKMART SALES ANALYSIS")
print("=" * 60)

# Monthly sales data per store (in thousands of dollars)
# Data structure: Dictionary with store locations as keys
# Each store contains a list of 12 monthly sales figures (Jan-Dec)
sales_data = {
    "Downtown": [120.5, 115.8, 131.2, 140.5, 150.2, 160.1, 155.3, 148.9, 152.5, 160.8, 165.2, 180.3],
    "Suburb Mall": [85.6, 90.2, 93.5, 100.8, 110.5, 115.7, 120.2, 118.5, 125.6, 130.2, 140.8, 155.5],
    "Westside": [95.2, 88.7, 92.3, 100.5, 105.8, 110.2, 115.7, 120.5, 125.8, 130.2, 135.5, 145.8],
    "University": [55.3, 60.2, 65.8, 70.5, 65.2, 50.1, 45.2, 55.8, 80.5, 85.9, 90.2, 95.3]}

# Store locations
locations = list(sales_data.keys())

# List of month names for reporting
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

# TODO 1: Calculate the total sales for each month across all stores
# Initialize a list to store the total monthly sales
num_of_months=12
monthly_totals = []
for i in range(12):
    current_month_total=0
    for store_sales in sales_data.values():
        current_month_total += store_sales[i]
    monthly_totals.append(current_month_total) #remember to make it two decimal places


# TODO 2: Find the month with the highest and lowest total sales
highest_month_index = 0
lowest_month_index = 0
highest_sales = 0
lowest_sales = float('inf')  # Start with infinity for comparison
for i in range(len(monthly_totals)):
    current_total=monthly_totals[i]
    if current_total>highest_sales:
        highest_sales=current_total
        highest_month_index = i
    if current_total<lowest_sales:
        lowest_sales=current_total
        lowest_month_index=i


# TODO 3: Calculate the average monthly sales across all stores
total_sales=0
for total in monthly_totals:
    total_sales += total
average_monthly_sales = total_sales / num_of_months



# TODO 4: Find the store with the highest annual sales
best_store = ""
best_store_sales = 0
for location, sales_list in sales_data.items():
    current_store_sales = sum(sales_list)
    if current_store_sales > best_store_sales:
        best_store_sales = current_store_sales
        best_store = location


# TODO 5: Generate a monthly performance report using a while loop
print("\n" + "=" * 35)
print("MONTHLY PERFORMANCE REPORT")
print("=" * 35)
month_counter = 0
performance_report=[]
while month_counter < num_of_months:
    month_name = months[month_counter]
    total = monthly_totals[month_counter]
    if total > average_monthly_sales:
        indicator = "ABOVE AVERAGE"
    elif total < average_monthly_sales:
        indicator = "BELOW AVERAGE"
    else:
        indicator = "AT AVERAGE"
    performance_report.append((f"{month_name:10}: ${total:9.2f} - {indicator}"))
    month_counter += 1

for i in range(len(performance_report)):
    print(performance_report[i])
    

# TODO 6: Bonus challenge - Identify consecutive months with increasing sales
current_streak = 0
temp_streak_start = 0
longest_growth_streak=0

for i in range(1, len(monthly_totals)):
    if monthly_totals[i] > monthly_totals[i-1]:
        current_streak += 1
        if current_streak == 1:
            temp_streak_start = i - 1
        if current_streak > longest_growth_streak:
            longest_growth_streak = current_streak
            growth_streak_start = temp_streak_start
    else:
        current_streak = 0

# Print final summary
print("\n" + "=" * 60)
print("QUICKMART SALES ANALYSIS SUMMARY")
print("=" * 60)
print(f"Best Month: {months[highest_month_index]} - ${highest_sales:,.2f}")
print(f"Worst Month: {months[lowest_month_index]} - ${lowest_sales:,.2f}")
print(f"Average Monthly Sales: ${average_monthly_sales:,.2f}")
print(f"Best Performing Store: {best_store} - ${best_store_sales:,.2f}")
reported_streak_length = longest_growth_streak + 1 if longest_growth_streak > 0 else 1
reported_start_month = months[growth_streak_start] if longest_growth_streak > 0 else "N/A (No consecutive growth)"
if longest_growth_streak > 0:
    print(f"Longest Growth Streak: {longest_growth_streak + 1} months starting in {months[growth_streak_start]}")
else:
    print(f"Longest Growth Streak: 1 month (no consecutive growth)")