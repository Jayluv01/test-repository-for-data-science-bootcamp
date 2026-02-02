sales = [261.96, 731.94, 14.62, 957.5, 1786.18, 95, 43, 17, 48, 71, 54, 63]

def calculate_average(values):
    sales_count = len(values)
    total_sales = sum(values)

    average = total_sales / sales_count

    return average

result = calculate_average(sales)
print(f"the average value of sales for the month of Septmember was {result:.1f}")

# ___________________________________________
# Multiple Returns.
# A function can have many return statements
# The return keyword can be used only within a function
# ____________________________

def calculate_bmi(weight_kg, height_m):
    """Calculates Body Mass Index(BMI)"""
    bmi = weight_kg / (height_m ** 2)
    return bmi
def get_bmi_category(bmi):
    """Get BMI Category as a string"""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
height = 1.75
weight = 70

bmi_value = calculate_bmi(weight, height)
category = get_bmi_category(bmi_value)

print(f"\nHeight: {height}")
print(f"Weight: {weight}")
print(f"BMI: {bmi_value:.1f}")
print(f"Category: {category}")