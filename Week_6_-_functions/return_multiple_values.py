def analyze_sales(sales_list):
    """Calculate multiple statistics from sales data"""
    total = sum(sales_list)
    average = total / len(sales_list)
    highest = max(sales_list)
    lowest = min(sales_list)

    return (total, average, highest, lowest)


data = [1500, 920, 1800, 1100, 2200]

# result = analyze_sales(data)

# print("Result of sales analysis", result)
# print("Total sales value", result[0])
# print("Average sales value", result[1])
# print("Highest sales amount", result[2])
# print("Lowest sales amount", result[3])

(total, average, highest, lowest) = analyze_sales(data)

print("Total sales value:", total)
print("Average sales value:", average)
print("Highest sales amount:", highest)
print("Lowest sales amount:", lowest)

# TODO: Return values as disctionary



