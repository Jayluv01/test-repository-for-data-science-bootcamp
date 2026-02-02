with open("files/Sample - Superstore.csv", "r") as file:
    header_line = file.readline().strip()
    columns = header_line.split(",")

    print("===========Superstore Dataset Columns =========")
    for i, column in enumerate(columns, 1):
        print(f"{i:2}. {column}")