# A module can be referred to as a library or a package.
# This is a pre-written Python code (Think of a tool box) that contains reusable functions, codes, etc.
import os
# This allows you to:

# file and directory operations
# Process management
# Environment variables
# Path manipulation

# Return the absolute path
cwd = os.getcwd()
print("\nMy current working direcory is:")
print(cwd)
print("")

# Lists content of current working directory
cwd_content = os.listdir()
print(cwd_content)
print("")

# Checks if a file exists
exists = os.path.exists("example.txt")
print(exists)
print("")

if os.path.exists("Sample Directory"):
    # Navigate into the dirtectory to create a new file
    pass
else:
    #Create the folder first
    pass
if os.path.exists("Sample Path") is False:
    #Boolean expression above has to be True before the code in the if block is executed
    os.mkdir("Sample Path")
    

# Create directory with try/except block
# try/catch
try: 
    os.mkdir("Sample Path")
    print("Sample Path directory created!")
except FileExistsError:
    print("An error occured! Check to ensure the directory doesn't already exist.")
    
