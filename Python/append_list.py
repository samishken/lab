# Append add element at the end of the list
# Insert method adds and element at the beginning of the list
fruits = ['apple', 'banana', 'orange', "Pineapple"]
fruits.append('pear')
print(fruits)
# ['apple', 'banana', 'orange', 'Pineapple', 'pear']
fruits.insert(0, 'Melon')
print(fruits)
# ['Melon', 'apple', 'banana', 'orange', 'Pineapple', 'pear']

# Remove method
fruits.remove('pear')
print(fruits)
# ['Melon', 'apple', 'banana', 'orange', 'Pineapple']

# pop method
fruits.pop(3)  # removes "orange"
print(fruits)
# ['Melon', 'apple', 'banana', 'Pineapple']

# change the value of an element
fruits[2] = "Strawberry"  # banana -> strawberry
print(fruits)
# ['Melon', 'apple', 'Strawberry', 'Pineapple']

# CLEAR method removes all elements from the list
fruits.clear()
print(fruits)
# []

fruits.append("Banana")
print(fruits)
# ['Banana']
fruits.append("Melon")
print(fruits)
# ['Banana', 'Melon']