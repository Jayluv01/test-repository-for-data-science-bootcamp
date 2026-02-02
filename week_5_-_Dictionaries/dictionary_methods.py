from pprint import pprint

# get() method-- sued to retrieve a dictionary item using the key name

person = {
    "first_name": "Olawale",
    "last_name": "Owootomo",
    "age": 32,
    "pets": { "dog": "Freda", "cat": "sox"},
    "kids": ["Joe", "Kamra", "Sarah"],

}

print("first Name (wuth get() method): ", person.get("first_name"))
print("First Name (without method): ", person["first_name"])

# clear() method -- Deletes the entire dictionary content

person_b = {
    "first_name": "Olawale",
    "last_name": "Owootomo",
    "age": 32,
    "pets": { "dog": "Freda", "cat": "sox"},
    "kids": ["Joe", "Kamra", "Sarah"],

}

person_b.clear()
pprint(person_b)


# copy () creates a shallow mirror/copy of a dictionary
person_a = person.copy()
pprint(person_a)
pprint(person)


# items() Resturns a list containing a tuple of each key-value pair
pprint(person.items())

# values() Resturns a list containing all the values in a dictionary
pprint(person.values())

# Keys() Resturns a list containing all the keys in a dictionary
pprint(person.keys())

# pop() Removes the elements with the specified key and returns the value
last_name = person.pop("last_name")
print("The last name is", lastName)
pprint(person)