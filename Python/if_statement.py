# if statement
# The is_positive function should return True if the number received is positive, otherwise it returns None.
# def is_positive(number):
#   if number > 0:
#     return True
# number1 = is_positive(-5)
# number2 = is_positive(5)
# print("Is it positive? ", number1)
# print("Is it negative? ", number2)

# def hint_username(username):
#     if len(username) < 3:
#         print(username + " is not a valid username. Must be at least 3 characters long.")
#         return username
#     else:
#         print("Valid Username")
# usernames = hint_username("Tag")

def is_even(num):
    if num % 2 == 0:
        return True
    return False
number = is_even(10)
print(number)
