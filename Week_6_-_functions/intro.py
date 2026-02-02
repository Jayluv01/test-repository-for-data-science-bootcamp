# Functions are named, reusable blocks of codethat perform a specific task, helping to organize your 

# Understanding what functions are and why they are essential.
# Define and call functions with parameters
# Variable scope
# Use return values to get results from functions
# Parameters and Arguments (Multiple Parameters, Positioal vs Keyword Arguments)
# Write functions with default paraemters
# Multiple return values (as lists, tuples, dictionaries)
# Apply functions to solve data science problems
# Organize code with reusable function libraries

# def (used to define a function) calculate average():
def calculate_average():
    """Calculate average of sales values"""


# syntax of a function:

# def <name of function>:
#     function body (msut be 1 to uncountable number of times)

# Analyzing sales data for the north region
north_total = 0
north_count = 0
north_sales = [1200, 850, 2100, 1450, 980]

for sale in north_sales:
    north_total += sale # Shorthand way pf writig the opeation below
    # north_total = north_total + sale
    north_count += 1

north_average = north_total / north_count
print(f"")

# Example of a function (With Parameters)
# Parameters are placeholder variables.
def add(a, b):
    print(a + b)

# When you call a function, the values you place in-between the brackets are referred to as "arguments"
add(20, 9)
add(59, 34)

# Functions are first-class citizens in pythons:

# 1. A function being assigned to a variable
addition = add
addition(12, 5)

# 2. Pass a function as an argument to other functions
def operations(a, args):
    return a(*args)

operations(add, [12, 5])

# 3. Return a function from another function
def operations():
    def addition(values):
        return sum(values)

    return addition

def calc():
    return "calculation"
# 4. Function can be stored in a data structure like lists, dictionaries.
student = {
    "name": "Olawale Owootomo",
    "gender": "Male",
    "calculate_scores": calc,
}
