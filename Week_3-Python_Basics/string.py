# strings are texts in programming languages, are wrapped in double quotes or single quotes. Use double quotes in Python
# Whatever you have in a quote automatically becomes a string, whether it's an integer or an alphabet or even a boolean.
# len is an in-build function in PY that returns the length of a string
# String functions are operations that you can perform on a string. Mostly transformational in nature

state = "Kaduna"
print(state)
print(type(state))

# Length of a string
print("The length of the string is:", len("Kaduna"))

country = "Nigeria"

# Transform to lower case
print(country.lower())

# Transform to lower case
print(country.lower())

# Transform to upper case
print(country.upper())

# Transform to title case
event_name = "uefa champions league"
print(event_name.title())

age = "45"
print("Is 45 numeric?", age.isnumeric())

# string slicinng
# Index position by computing
# Counting usually starts from 0, and spaces between characters also count as individual characters
greeting = "Hello, good morning"
print(greeting[0:5])
print(len(greeting))





first_name = "Chris"
last_name = "Idakwo"
score = 80
full_name = first_name + " " + last_name

print(first_name + " " + last_name)

print(full_name + " scored " + str(score) + " " + "out of 100")
sentence = full_name + " scored " + str(score) + " " + "out of 100"
print(sentence)
print(first_name [::-1])

username = "- johndoe@email.com"
print (username )


# String Formating
sentence_fa = "{fname} {lname} scored {sc} out of 100 for this session!" .format(fname = first_name, lname = last_name, sc = score)
print(sentence_fa)

