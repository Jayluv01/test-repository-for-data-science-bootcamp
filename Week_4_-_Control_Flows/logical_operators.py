# Logical operators are used to combine or modify the results of comparism operation

# Examples:
age = 17
has_id = True

# Or
# Example of 'or' logical operator:
if age >= 18 or has_id == True:
    print("Give access")
else: 
    print("No access!")

# And
# Example of 'and' logical operator:
if age >= 18 and has_id == True:
    print("Give access")
else: 
    print("No access!")

# Not (Reverses a condition)
# Example of 'and' logical operator:
print("Is 5 not equal to 5?", not (5 == 5))
logged_in = False

if not logged_in:
    print("You're a guest")
else:
    print("Welcome back")


# Discount eligibility
age = 25
is_student = False

if age >= 68 or is_student:
    print("Yay, discount applied!")
else:
    print("Sorry, no discount applied")
