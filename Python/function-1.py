# Variables
# expressions
# operations
# functions
from math import remainder


# def greetings(students, teachers):
#     print("hello " + students)
#     print("your teacher name is " + teachers)
#
# greetings("kebede", "alemu")
# print(greetings)

# def area_triangle(base, height):
#     return base * height / 2
#
# area_a = area_triangle(5,4)
# area_b = area_triangle(6,4)
# sum = area_a + area_b
# print(str(sum))

# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds % 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
#
# hours, minutes, seconds = convert_seconds(5000)
# print(hours)


def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")