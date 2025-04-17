# Write a Python program that performs the following operations on a given string:
# - - - - Find the length of the string.
# - - - - Convert the string to uppercase and lowercase.
# - - - - Replace a substring in the string with another substring.
# - - - - Check if the string starts with a particular word and ends with a particular word.
# Questions for this assignment
# 1) Write a Python program that performs the following operations on a given string:
# # Input string:  Find the length of the string.
text = "Python programming is fun and powerful!"
print(len(text))
# 2) Write a Python program that performs the following operations on a given string:
# # Input string: Convert the string to uppercase and lowercase.
text = "Python programming is fun and powerful!"
print(text.upper())
print(text.lower())

# 3) Write a Python program that performs the following operations on a given string:
# # Input string: Replace a substring in the string with another substring.
text = "Python programming is fun and powerful!"
print(text.replace("Python", "Java"))

# 4) Write a Python program that performs the following operations on a given string:
# # Input string: Check if the string starts with a particular word and ends with a particular word.
text = "Python programming is fun and powerful!"
print(text.startswith("Python") and text.endswith("powerful!"))

# 5 Split the list
text = "Python programming is fun and powerful!"
print(text.split())

