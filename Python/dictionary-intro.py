# Dictionary Data type - mutable (can be changed)
# we can change KEYS but we can't change values

employee = {
    "name": "John Doe",
    "age": 22,
    "position": "Software Engineer",
    "salary": 120000
}
print(employee)
print(employee["age"])
print(employee["position"])

# add more entry to the dictionary
employee["department"] = "IT"
print(employee)

# delete
del employee["age"]
print(employee)