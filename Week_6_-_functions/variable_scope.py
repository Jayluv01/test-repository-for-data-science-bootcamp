# What is scope?
# Scope = Wherte can Python "see" your variable?

# - Global Scope (The living room)
# Variables created at the main level - everyone can see them

# This is Global - Cretaed outside any function, calss, etc.
customer_name = "Alice"

def greet():
    # Inside this function, we can see the global variable
    print(f"Hello, {customer_name}")

greet() # Wroks! Prints: Helo, Alice
print(customer_name) # Works1 Prints: Alice

# Local Scope (The bedroom)
# Variables created inside a function - only that function can see them

def calculate_tax():
    # The variable "tax_rate" is Local - Only exists inside this function
    tax_rate : 0.08
    return tax_rate * 100

print(calculate_tax()) # Works! prints 8.0
# print(tax_rate) # Error! Can't see tax_rate outside the "Calculate_tax" function

# Reading Global Variables
discount_rate = 0.10

def calculate_discount(price):
    discount = price * discount_rate
    return discount

print(calculate_discount(800))

# Reassigning Global Variables

def calculate_total(price):
    discount_rate = 0.13 # re-assigning the value of discount_rate
    discount = price * discount_rate

    return price - discount

print(calculate_total(880))
print("What is discount rate ?", discount_rate)