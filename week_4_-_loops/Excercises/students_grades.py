# Ask the teacher for the nuber of students
# For each student:
# Ask for the studnet's name
# Ask for their test score
# Check if the score is valid (between 0 and 100)
# Calculatre the average of all scores
# Tell the teacher: 
# Who passed ( Score >= 60)
# Who failed ( Score < 50)
# The class average
# The highest and lowest scores

# Step 1: Ask how many students
num_students = int(input("How many students are you grading? "))

# Initialize all necessary variables for calculations
total_score = 0
passed_students = []
failed_students = []

for num in range(num_students):
    print(f"\n--- students {num + 1} --- ")

    # Get the students name
    student_name = input("Enter the studnet's name")

    # Get and validate test score
    student_score = float(input(f"Enter score for {student_name}" ))

    while student_score < 0 or student_score > 100:
        print("Ivalid score! Please, enetr a score between 0 and 100")
        student_score = float(input(f"Enter score for {student_name}: "))

    print("Score recorded!")

    # Add to the total for claculation of average
    total_score = total_score + student_score
    print("The total score is ", total_score)

    # Check if the student passed or falied
    if student_score >= 60:
        passed_students.append((student_name, student_score))
    else:
        failed_students.append((student_name, student_score))

class_average = total_score / num_students

print("Class average ", class_average)

    

