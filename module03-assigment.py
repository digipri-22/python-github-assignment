#ISM Module 3 Assignment (String manipulation, User input, Formatted output), Sep 14th

# Welcome message
print("=" * 50)
print("CUSTOMER ORDER PROCESSING SYSTEM")
print("=" * 50)
print("Please enter the following information:\n")

# Part 1: Collect customer information
customer_name = (input("Enter customer name: ")).strip().title()
customer_email = (input("Enter customer email: ")).lower().strip()

# Part 2: Collect order information
product_name = (input("Enter product name: ")).strip().title()
quantity = int((input("Enter quantity: ")).strip())
unit_price = float(input("Enter unit price: ").strip())

# Part 3: Processing the information
subtotal = quantity * unit_price
tax_amount = subtotal * 0.085
order_total = subtotal + tax_amount

# Part 4: Order Summary Display
print(f"\nORDER SUMMARY\n=============\nCustomer: {customer_name}\nEmail: {customer_email}\nProduct: {product_name}\nQuantity: {quantity}\nUnit Price: ${unit_price:.2f}\nSubtotal: ${subtotal:.2f}\nTax (8.5%): ${tax_amount:.2f}\nOrder Total: ${order_total:.2f}")

