# A disctionary is a data structure used to store data values in key-value pairs.
# The values in a dictionary can be of any data type.
# The keys must be strings
# A dictionary is a collection which is changable/mutable and ordered.
# Does not allow duplicates.
# Keys naming must be unique. Duplicate keys will override the initial one.
# Pretty print
from pprint import pprint

student_profile = {
    "first_name": "Olawale",
    "Last_name": "Owootomo",
    "age": 32,
    "height": 1.65,
    "gender": "Male",
    "registered": True,
    "skills": []
}

pprint(student_profile)

orders = {
    "orderId": 2345432,
    "orderDate": 4554,
    "shipMode": 4554,
    "customerName": 4554,
}


# Create dictionary using dict() constructor
student_b = dict(
    first_name = "Olawale",
    last_name = "Owootomo",
    age = 32,
    gender = "Male",
)

pprint(student_b)