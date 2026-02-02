file_path = "files/greeting.txt"

with open(file_path, "w") as file:
    # Write content to a file, one line at a time.
    file.write("Hello, this is a new line entry in a new file\n")
    file.write("This is another new line\n")
    file.write("Now i'm just having fun with it\n")
    file.write("\n\n")
    file.write("=" * 80)
    file.write("\n\n")

    # Write multiple lines at once
    names = ["Gospel Ibekwe", "Kabeke Makanzu", "Doyinsola Simbiat", "Deborah Enitan", "Tech World"]
    
    # Option 1: Introducte a new line character to every item in yhe list using a for loop
    newNames = []
    for name in names:
        newNames.append(f"{name}\n")

    # Option 2: Introduce a new line character t each name ina list using a list comprehension
    newNames = [f"{name}\n"for name in names]

    file.writelines(newNames)

