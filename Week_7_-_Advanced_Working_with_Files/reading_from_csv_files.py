import csv

FILENAME = "files/house_prices.csv"

def read_csv_file(file_path):
    """Read the content of a CSV file using python in-built csv moodule"""

    with open(file_path, "r") as file:
        # The first thing you do in orther to read thye content of a CSV file is to initiate
        # a new instance of the CSV reader
        csv_reader = csv.reader(file)

        print("\ROWS IN A DATA FILE")
        print("")
        for row in csv_reader:
            print(row) # Row is a list of values
            print("")

        
def read_csv_file_dict(file_path):
    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        print("\ROWS IN A DATA FILE")
        print("")
        for row in csv_reader:
            print(row) # row is a dictionary {coulumn_name: value}
            print("")


read_csv_file(FILENAME)
print("\n=========================================================\n")
read_csv_file_dict(FILENAME)

