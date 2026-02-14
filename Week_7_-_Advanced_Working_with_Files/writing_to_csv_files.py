import csv

# sample data
data = [
    # ["Name", "Score", "Grade"]
    ["Alice", 92, "A"],
    ["Bob", 85, "B"],
    ["Mike", 73, "C"],
    ["Harrison", 97, "A"],
    ["Florence", 61, "D"],
]

# Assuming the headers were not defined
headers = ["Name", "Score", "Grade"]
data = [headers] + data
# print(data)

# Write to the CSv file
with open("files/students_grades.csv", "w", newline = '') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

print("Done writing to 'students_grades.csv")