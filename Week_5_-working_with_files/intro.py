# # Step 1: Opening & Reading the file
# file = open("./Sample - Superstore.csv", "r")
# content = file.read()
# file.close()

# print(content)

# # Step 2: Reading file content line by line (Row by Row)
# file_ = open("Sample - Superstore.csv", "r")

# # Read first line (header)
# header = file_.readline()

# # Read all other lines
# for line in file_:
#     print(line)
#     print("="*20)

# file_.close()

# Step 3: Using 'with' statement (Best Practice)
with open("Sample - Superstore.csv", "r") as file:
    header = file.readline().strip()
    print("columns:", header)

    for line in file:
        print(line.strip())
