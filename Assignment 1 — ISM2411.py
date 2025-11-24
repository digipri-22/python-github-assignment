#Assigment 1 — ISM2411

#Defining the Variables
product_name = "kitties"
units_sold_str = "220"
price_per_unit_str = "33.50"
tax_rate = 0.022
discount_rate = 0.15

#Type Conversion
units_sold = int(units_sold_str) #conversion to int
price_per_unit=float(price_per_unit_str) #conversion to float

# Calculate Net Price
taxed_price = (price_per_unit * (1 + tax_rate))
net_price = taxed_price * (1 - discount_rate)

#Total Revenue
total_revenue = net_price * units_sold

#Output
print (f"The net price per kitty will be ${net_price:,.2f}, and the total revenue is ${total_revenue:,.2f}")
