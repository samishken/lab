# Questions for this assignment
# 1) Write a Python program that performs the following operations on a list:
# # Create a list of 5 integers.
integers = [10, 20, 30, 40, 50]
print(integers)
# 2) Write a Python program that performs the following operations on a list:
# # Add a new element to the list.
integers.append(60) # adds as the last element of the list
print(integers)
integers.insert(1, 15)
print(integers)
integers.pop()  # removes the last element
print(integers)

# 3) Write a Python program that performs the following operations on a list:
# # Remove the third element from the list.
integers.pop(3)
print(integers)


# 4) Write a Python program that performs the following operations on a list:
# # Update the value of the second element.
integers[2] = 30
print(integers)

# 5) Write a Python program that performs the following operations on a list:
# # Print the list and its length.
print("Integer list =", integers, " " + "Length of int = " + str(len(integers)))