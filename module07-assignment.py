# Module 7 Assignment: Organizing Data with Lists and Tuples
# TechElectronics Inventory Tracking System

# Welcome message
print("=" * 60)
print("TECHELECTRONICS INVENTORY TRACKING SYSTEM")
print("=" * 60)

# TODO 1: Create product tuples
# Each product is a tuple: (product_id, name, price, quantity, category)
product1 = ("P001", "Iphone 17", 999.99, 13, "Mobile Phones")
product2 = ("P002", "Macbook M4", 799.45, 6, "Laptops")
product3 = ("P003", "Wireless Mouse", 25.00, 30, "Accessories")
product4 = ("P004", "SSD of 100 GB", 80.99, 5, "Storage")
product5 = ("P005", "14 Inch Monitor", 350.99, 2, "Monitors")

# TODO 2: Create an inventory list containing all product tuples
inventory = [product1, product2, product3, product4, product5]

# TODO 3: Display the products
print("\nCurrent Inventory:")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 4: Access specific elements
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1]
second_price = inventory[1][2]
second_quantity = inventory[1][3]
print("\n\nAccessing Specific Products (Final Inventory State):")
print("-" * 60)
print(f"First Product: {first_product}")
print(f"Last Product: {last_product}")
print(f"Third Product Name: {third_product_name}")
print(f"Second Product Price: ${second_price:.2f}, Quantity: {second_quantity}")

# TODO 5: Use slicing to get subsets
first_three = inventory[0:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]
print("\n\nProduct Subsets Using Slicing (Final Inventory State):")
print("-" * 60)
print(f"First 3 Products: {first_three}")
print(f"Products from Index 2 to 4: {middle_products}")
print(f"All Products Except the First: {all_except_first}")

# TODO 6: Add new products to inventory
new_product1 =  ("P006", "Headset", 20.00, 33, "Audio")
new_product2 = ("P007", "Go-Pro Camera", 300.00, 14, "Cameras")
inventory.append(new_product1)
inventory.append(new_product2)
print("\n\nAdding New Products (P006, P007):")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 7: Remove a product
removed_product = inventory.pop(2)
print("\n\nRemoving a Product (Index 2):")
print("-" * 60)
print(f"Removed: {removed_product}")
print("Updated Inventory:")
for product in inventory:
    print(product)

# TODO 8: Insert a product at a specific position
inserted_product = ("P008", "Action Camera", 250.00, 4, "Cameras")
inventory.insert(1, inserted_product)
print("\n\nInserting a Product (Index 1 - P008):")
print("-" * 60)
for product in inventory:
    print(product)

# TODO 4: Again
first_product = inventory[0]
last_product = inventory[-1]
third_product_name = inventory[2][1] 
second_price = inventory[1][2]
second_quantity = inventory[1][3]
print("\n\nAccessing Specific Products (Final Inventory State):")
print("-" * 60)
print(f"First Product: {first_product}")
print(f"Last Product: {last_product}")
print(f"Third Product Name: {third_product_name}")
print(f"Second Product Price: ${second_price:.2f}, Quantity: {second_quantity}")

# TODO 5: Again
first_three = inventory[0:3]
middle_products = inventory[2:5]
all_except_first = inventory[1:]
print("\n\nProduct Subsets Using Slicing (Final Inventory State):")
print("-" * 60)
print(f"First 3 Products: {first_three}")
print(f"Products from Index 2 to 4: {middle_products}")
print(f"All Products Except the First: {all_except_first}")

# TODO 9: Create category lists
mobile_phones = []
laptops = []
audio = []
storage = []
monitors = []
cameras = []
for product in inventory:
    category = product[4]
    if category == "Mobile Phones":
        mobile_phones.append(product)
    elif category == "Laptops":
        laptops.append(product)
    elif category == "Audio":
        audio.append(product)
    elif category == "Storage":
        storage.append(product)
    elif category == "Monitors":
        monitors.append(product)
    elif category == "Cameras":
        cameras.append(product)

print("\n\nProducts by Category:")
print("-" * 60)
print(f"Mobile Phones ({len(mobile_phones)}): {mobile_phones}")
print(f"Laptops ({len(laptops)}): {laptops}")
print(f"Audio ({len(audio)}): {audio}")
print(f"Cameras ({len(cameras)}): {cameras}")

# TODO 10: Calculate inventory statistics
total_products = len(inventory)
total_value = 0.0
product_names = []
product_prices = []
for product in inventory:
    total_value += product[2] * product[3]
    product_names.append(product[1])
    product_prices.append(product[2])

print("\n\nInventory Statistics:")
print("-" * 60)
print(f"Total Number of Products (unique types): {total_products}")
print(f"Total Inventory Value (Price x Quantity): ${total_value:,.2f}")
print(f"List of all Product Names: {product_names}")
print(f"List of all Product Prices: {product_prices}")


# TODO 11: Find expensive products using list comprehension
expensive_products = [product for product in inventory if product[2] > 500]
print("\n\nExpensive Products (> $500):")
print("-" * 60)
for product in expensive_products:
    print(product)

# TODO 12: Low stock alert using list comprehension
low_stock = [product for product in inventory if product[3] < 5]
print("\n\nLow Stock Alert (< 5 units):")
print("-" * 60)
for product in low_stock:
    print(product)

# TODO 13: Create price list using list comprehension
original_prices = [product[2] for product in inventory]
discounted_prices = [round(price * 0.90, 2) for price in original_prices]
print("\n\nPrice Lists:")
print("-" * 60)
print(f"Original Prices: {original_prices}")
print(f"Discounted Prices (10% off): {discounted_prices}")

# TODO 14: Product name formatting using list comprehension
uppercase_names = [product[1].upper() for product in inventory]
product_codes = [product[0][:3] + product[1][:3] for product in inventory]
print("\n\nFormatted Product Names:")
print("-" * 60)
print(f"Uppercase Names: {uppercase_names}")
print(f"Product Codes: {product_codes}")

# TODO 15: Using Loops to Process Inventory 
mobile_count = 0
laptop_value = 0.0
most_expensive = ("", "", 0.0, 0, "") 
for product in inventory:
    if product[4] == "Mobile Phones":
        mobile_count += 1 
    if product[4] == "Laptops":
        laptop_value += product[2] * product[3]
    if product[2] > most_expensive[2]:
        most_expensive = (product[0], product[1], product[2], product [3], product[4])
print("\n\nLoop-Based Analysis:")
print("-" * 60) 
print(f"Products in 'Mobile Phones' category: {mobile_count}")
print(f"Total value of all 'Laptops' in stock: ${laptop_value:,.2f}")
print(f"Most Expensive Product: {most_expensive[0]}, {most_expensive[1]}, (${most_expensive[2]:,.2f}, {most_expensive[3]}, {most_expensive[4]})")

# TODO 16: Using Conditionals with Lists
restock_list = []
high_value_items = []
price_ranges = {"under $100": 0, "$100-$500": 0, "over $500": 0}
for product in inventory:
    if product[3] < 5:
        restock_list.append(product)
    if product[2] > 500 and product[3] > 10:
        high_value_items.append(product)
    if product[2] < 100:
        price_ranges["under $100"] += 1
    elif 100 <= product[2] <= 500:
        price_ranges["$100-$500"] += 1
    else: 
        price_ranges["over $500"] += 1
print("\n\nConditional Analysis:")
print("-" * 60)
print(f"Products that need restocking (Quantity < 5): {restock_list}")
print(f"High-Value Items (Price > $500 AND Qty > 10): {high_value_items}")
print(f"Price Range Counts: {price_ranges}")

# TODO 17: Define and Use Functions
def calculate_product_value(product):
    """Calculates price * quantity for a product tuple."""
    return product[2] * product[3]
def find_products_by_category(inventory_list, category_name):
    """Returns list of products in given category."""
    return [product for product in inventory_list if product[4] == category_name]
def apply_discount(inventory_list, discount_percent):
    """Returns new inventory with discounted prices."""
    discount_factor = 1 - (discount_percent / 100)
    new_inventory = []
    for product in inventory_list:
        new_price = round(product[2] * discount_factor, 2)
        new_product = product[:2] + (new_price,) + product[3:]
        new_inventory.append(new_product)
    return new_inventory
total_inventory_value = sum(calculate_product_value(p) for p in inventory)
audio_products = find_products_by_category(inventory, "Audio")
discounted_inventory_15 = apply_discount(inventory, 15)
print("\n\nFunction-Based Operations:")
print("-" * 60)
print(f"Total Inventory Value (using function): ${total_inventory_value:,.2f}")
print(f"Audio Products (using function): {audio_products}")
print("First 3 items of 15% Discounted Inventory:")
for i in range(3):
    print(f"  {discounted_inventory_15[i]}")


# TODO 18: Combine Loops, Functions, and List Operations
def generate_inventory_report(inventory_list):
    """
    Analyzes the inventory and returns a dictionary with key statistics.
    Integrates all concepts: loops, functions, and list operations.
    """
    report = {}
    report['total_products'] = len(inventory_list)
    report['total_value'] = sum(calculate_product_value(p) for p in inventory_list)
    categories = set()
    for product in inventory_list:
        categories.add(product[4])
    report['categories'] = sorted(list(categories))
    report['low_stock'] = [p for p in inventory_list if p[3] < 5]
    total_revenue = report['total_value']
    total_quantity = sum(p[3] for p in inventory_list)
    report['average_price'] = round(total_revenue / total_quantity, 2) if total_quantity > 0 else 0.0
    return report
inventory_report = generate_inventory_report(inventory)
print("\n\nComprehensive Inventory Report:")
print("-" * 60)
for key, value in inventory_report.items():
    if key == 'total_value' or key == 'average_price':
        print(f"{key.replace('_', ' ').title():20}: ${value:,.2f}")
    elif key == 'low_stock':
        print(f"{key.replace('_', ' ').title():20}: {len(value)} items - {value}")
    else:
        print(f"{key.replace('_', ' ').title():20}: {value}")