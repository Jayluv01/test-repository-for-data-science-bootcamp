print("")
print ("-" * 40)
print("Password Length Check")
print ("-" * 40)
print("")

password = input("Enter your password: " )

# Rules: 
# Password should have at least, 1 upper case letter
# At least, one lower case letter
# At least, one special character
# And has at least, 8 characters minimum.

min_length = len(password) >= 8
has_upper = password.lower() != password
has_lower = password.upper() != password

print("has - 8 characters", min_length)
print("has uppercase", has_upper)
print("Has lowercase", has_lower)

if min_length and has_upper and has_lower:
     print("Welocme to Dev & Design!")
else:
     print("Your password is not secure enough!")


print("")
print ("-" * 40)
print("Grade Classification")
print ("-" * 40)
print("")

# Take a score and convert to a grade letter, ranging from A to F
# Where A is for scores between 85 & 100
# B is for scores between 70 & 85
# C is for scores between 55 & 70
# D is fpr scores between 45 & 55
# E is for scores between 30 & 45
# F is for scores below 30 (0 to 30)

score = input("Enter your score (0 to 100): ")

if score.isnumeric():
    score = int(score)
    if score >= 85 and score <= 100:
        print("Garde is A")
    elif score >= 70 and score < 85:
        print("Grade is B")
else:
    print("Please, enter a valid score betweem 0 and 100")

