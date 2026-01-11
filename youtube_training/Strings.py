course = "Python Programming"
# A function is a reusable piece of code that carrries out a task.
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[:3])
print(course[:])

# \"
# \'
# \\
# \n (Creates a new line)

first = "Olawale"
last = "Owootomo"
# full = first + " " + last (Old approach)
# Using formatted strings, we can say:
full = f"{first} {last}"
print(full)

print(course.upper())
print(course.lower())
print(course.title())

# .strip removes characters from your code. e.g .strip() removes every white space, while .rstrip & .lstrip removes white space from beginning and the end of your codes
# To get the index of a character, or a sequence of characters in your string, use the 'find' method
print(course.find("Pro")) # -1 message means string chracters were not found in our string. Used to find the 'INDEX' of characters
print(course.replace("P", "J")) # Replace a character or sequence of characters in a string
print("Pro" in course) # To check for the existence of a character or sequence of characters in a string (Returns a Boolean)
print("swift" not in course) # Not Operator to check for the existence of a character or sequence of characters in a string (Returns a Boolean)

