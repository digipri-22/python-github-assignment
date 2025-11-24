# Module 6 Assignment: Functions and Modular Programming
# TechRetail Sales Analysis System

# Welcome message
print("=" * 60)
print("TECHRETAIL SALES ANALYSIS SYSTEM")
print("=" * 60)

# Sample quarterly sales data 
# Format: [product_name, category, price, quantity_sold, employee_id]
sales_data = [
    ["Smartphone Pro", "Phones", 899.99, 15, "E101"],
    ["Laptop Ultra", "Computers", 1299.99, 10, "E105"],
    ["Wireless Earbuds", "Audio", 149.99, 30, "E101"],
    ["Smart Watch", "Wearables", 249.99, 12, "E102"],
    ["Gaming Console", "Gaming", 499.99, 8, "E103"],
    ["Bluetooth Speaker", "Audio", 79.99, 25, "E102"],
    ["Tablet Lite", "Computers", 399.99, 18, "E104"],
    ["Digital Camera", "Cameras", 599.99, 5, "E105"],
    ["VR Headset", "Gaming", 299.99, 7, "E103"],
    ["Fitness Tracker", "Wearables", 129.99, 22, "E104"],
    ["Smartphone Plus", "Phones", 699.99, 20, "E101"],
    ["Laptop Basic", "Computers", 899.99, 14, "E105"]
]

# Employee information
# Format: {employee_id: [name, commission_rate]}
employees = {
    "E101": ["Alex Johnson", 0.05],
    "E102": ["Sarah Williams", 0.045],
    "E103": ["James Brown", 0.04],
    "E104": ["Lisa Davis", 0.05],
    "E105": ["Michael Wilson", 0.055]
}

# functions to helps

def calculate_transaction_revenue(transaction):
    price = transaction[2]
    quantity = transaction[3]
    return price * quantity

def get_all_categories(data):
    categories = set()
    for transaction in data:
        categories.add(transaction[1])
    return sorted(list(categories))

# TODO 1: Sales Analysis Functions
# 1.1 Create a function to calculate total sales revenue
# REQUIRED FUNCTION NAME: calculate_total_sales
def calculate_total_sales(data=sales_data):
    total_revenue = 0.0
    for transaction in data:
        total_revenue += calculate_transaction_revenue(transaction)
    return total_revenue


# 1.2 Create a function to calculate the total sales for a specific category
# REQUIRED FUNCTION NAME: calculate_category_sales
def calculate_category_sales(category, data=sales_data):
    category_revenue = 0.0
    for transaction in data:
        if transaction[1] == category:
            category_revenue += calculate_transaction_revenue(transaction)
    return category_revenue

# 1.3 Create a function to find the best-selling product
# REQUIRED FUNCTION NAME: find_best_selling_product
# Should return tuple: (product_name, total_revenue)

def find_best_selling_product(data=sales_data):
    product_revenue = {}
    for transaction in data:
        product_name = transaction[0]
        revenue = calculate_transaction_revenue(transaction)
        if product_name in product_revenue:
            product_revenue[product_name] += revenue
        else:
            product_revenue[product_name] = revenue
    if not product_revenue:
        return ("", 0.0)
    best_product_name = ""
    max_revenue = 0.0
    for product, revenue in product_revenue.items():
        if revenue > max_revenue:
            max_revenue = revenue
            best_product_name = product
    return (best_product_name, max_revenue)

# TODO 2: Commission Calculation Functions
# 2.1 Create a function to calculate commission for a specific employee
# REQUIRED FUNCTION NAME: calculate_employee_commission
def calculate_employee_commission(employee_id, data=sales_data, emp_info=employees):
    if employee_id not in emp_info:
        return 0.0
    commission_rate = emp_info[employee_id][1]
    employee_sales_revenue = 0.0
    for transaction in data:
        if transaction[4] == employee_id:
            employee_sales_revenue += calculate_transaction_revenue(transaction)
    commission = employee_sales_revenue * commission_rate
    return commission

# 2.2 Create a function to calculate total commission for all employees
# REQUIRED FUNCTION NAME: calculate_total_commission
# Should return float: total commission for all employees

def calculate_total_commission(emp_info=employees, data=sales_data):
    total_commission = 0.0
    for emp_id in emp_info.keys():
        total_commission += calculate_employee_commission(emp_id, data, emp_info)
    return total_commission

# TODO 3: Report Generation Functions
# 3.1 Create a function to generate a sales summary report
# REQUIRED FUNCTION NAME: generate_sales_summary
def generate_sales_summary(include_categories=True, data=sales_data):
    report = []
    total_sales = calculate_total_sales(data)
    best_product, best_product_revenue = find_best_selling_product(data)
    report.append("=" * 40)
    report.append("QUARTERLY SALES SUMMARY")
    report.append("=" * 40)
    report.append(f"Total Revenue: ${total_sales:,.2f}")
    report.append(f"Best Seller:   {best_product} (${best_product_revenue:,.2f})")
    if include_categories:
        report.append("\n--- Category Breakdown ---")
        categories = get_all_categories(data)
        for category in categories:
            cat_sales = calculate_category_sales(category, data)
            report.append(f"{category:15}: ${cat_sales:,.2f}")
    report.append("\n" + "=" * 40)
    return "\n".join(report)
# 3.2 Create a function to generate an employee performance report
# REQUIRED FUNCTION NAME: generate_employee_report
# Should return string with employee sales and commissions

def generate_employee_report(emp_info=employees, data=sales_data):
    report = []
    report.append("=" * 50)
    report.append("EMPLOYEE PERFORMANCE AND COMMISSION REPORT")
    report.append("=" * 50)
    report.append(f"{'Employee Name':20} | {'Total Sales':15} | {'Rate':7} | {'Commission Earned':17}")
    report.append("-" * 50)
    employee_revenue = {}
    for emp_id, info in emp_info.items():
        employee_revenue[emp_id] = 0.0
    for transaction in data:
        emp_id = transaction[4]
        revenue = calculate_transaction_revenue(transaction)
        employee_revenue[emp_id] += revenue
    for emp_id, (name, rate) in emp_info.items():
        sales = employee_revenue.get(emp_id, 0.0)
        commission = sales * rate
        
        report.append(
            f"{name:20} | ${sales:13,.2f} | {rate*100:5.1f}% | ${commission:15,.2f}"
        )
        
    total_commission = calculate_total_commission(emp_info, data)
    report.append("-" * 50)
    report.append(f"{'TOTAL COMMISSIONS':20} | {'':15} | {'':7} | ${total_commission:15,.2f}")
    report.append("=" * 50)
    
    return "\n".join(report)

# TODO 4: Utility Functions
# 4.1 Create a function to get all products in a specific category
def get_products_by_category(category, data=sales_data):
    products_data = []
    for row in data:
        if row[1] == category:
            products_data.append(row)
    return products_data

# 4.2 Create a function to calculate the average sale price
# REQUIRED FUNCTION NAME: calculate_average_sale_price
# Should return float: average sale price across all transactions

def calculate_average_sale_price(data=sales_data):
    total_revenue = 0.0
    total_quantity = 0
    for transaction in data:
        price = transaction[2]
        quantity = transaction[3] 
        total_revenue += price * quantity
        total_quantity += quantity     
    if total_quantity == 0:
        return 0.0
    average_sale_price = total_revenue / total_quantity
    return average_sale_price

def main():
    print("\nTECHRETAIL QUARTERLY SALES ANALYSIS")
    print("-" * 40)
    total_sales = calculate_total_sales()
    print("\nTOTAL QUARTERLY SALES:")
    print(f"${total_sales:,.2f}")
    print("\nSALES BY CATEGORY:")
    categories = get_all_categories(sales_data) 
    for category in categories:
        category_sales = calculate_category_sales(category)
        print(f"{category:15}: ${category_sales:,.2f}")
    best_product, best_product_revenue = find_best_selling_product()
    print("\nBEST-SELLING PRODUCT:")
    print(f"{best_product} - ${best_product_revenue:,.2f}")
    print("\nEMPLOYEE COMMISSIONS:")
    for emp_id, (name, rate) in employees.items():
        commission = calculate_employee_commission(emp_id)
        print(f"{name:20}: ${commission:,.2f}")
    print("\nQUARTERLY SALES SUMMARY REPORT:")
    sales_summary = generate_sales_summary(include_categories=True)
    print(sales_summary)
    print("\nEMPLOYEE PERFORMANCE REPORT:")
    employee_report = generate_employee_report()
    print(employee_report)
# Run the main program
if __name__ == "__main__":
    main()