import sales_utils # This imports evrything located in the file

# To import a specific function: 
from sales_utils import calculate_total

# To import more than a function, list them and separate with commas: 
from sales_utils import calculate_total, calculate_average, find_top_sales, TAX_RATE


monthly_sales = [1200, 850, 2100, 1450, 980, 735, 839, 370]

total = calculate_total(monthly_sales)
avarege = calculate_average(monthly_sales)
top = find_top_sales(monthly_sales)

print("")
print(f"Total: $ {total:,.2f}")
print(f"AVerage: $ {total:,.2f}")
print(f"Top sale: $ {total:,.2f}")
print(f"Tax rate: $ {TAX_RATE}")