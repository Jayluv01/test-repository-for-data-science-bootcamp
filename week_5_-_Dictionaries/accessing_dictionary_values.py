from pprint import pprint

car = dict(
    brand = "Toyota",
    model = "Camry",
    enginelitre = 5.0,
    transmission = "Automatic"

)

# You acess values in a dictionary using a [], and the name of the key as a string within your brackets
print(car["brand"])

#Assigning the data to a variable:
trans = car["transmission"]
print("car transmission is: ", trans)

person = {
    "first_name": "Olawale",
    "last_name": "Owootomo",
    "age": 32,
    "pets": { "dog": "Freda", "cat": "sox"},
    "kids": ["Joe", "Kamra", "Sarah"],

}

print(person["kids"])

print("What's the name of the 2nd child?")
secondchild = person["kids"][1]
print("The name of the second child is: ", secondchild)
print("What is the name if the dog? ")
print("Name of the dog is", person["pets"]["dog"])