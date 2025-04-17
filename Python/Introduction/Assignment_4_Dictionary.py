#Create a dictionary with three key-value pairs.
# Write a Python program that performs the following operations on a dictionary:

# 1) Create a dictionary with three key-value pairs.
#Note: "name": "Alice", "age": 25, "city": "New York".

employee = {
    "Name": "Aice Smith",
    "Age": 25,
    "City": "New York"
}

print(employee)
# 2 Access a values using a key.

print(employee["Name"])
print(employee["Age"])
print(employee["City"])

# 3) Add a new key-value pair to the dictionary.  Note: "profession" = "Engineer"
employee["Profession"] = "Engineer"
print("new key-value is ", employee["Profession"])
print(employee)

# 4) Update the value of an existing key.
employee["Age"] = "26"
print("Age updated to ", employee["Age"])
print(employee)

# 5) Delete a key-value pair from the dictionary.
del employee["Age"]
print(employee)