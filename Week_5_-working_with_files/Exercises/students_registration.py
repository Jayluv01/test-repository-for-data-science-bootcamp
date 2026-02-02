file_path = "../files/registrations.txt"

full_name = input("Enter your full name: ")
class_level = input("Enter class level (ss1, ss2, ss3): ")
age = input( "Enter your age: ")

with open(file_path, "a")as file:
    file.write(f"{full_name} | {age} | {class_level}" + "\n")