# Return statement
# def area_triangle(base, height):
#     return base * height / 2
#
# area_a = area_triangle(5, 4)
# area_b = area_triangle(8, 6)
# print("area_a = ", area_a)
# print("area_b = ", area_b)
# sum_area = area_a + area_b
# print("The sum of both areas is: " + str(sum_area))

## This function returns 3 values
# def convert_seconds(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds
# ## Since this function returns 3 values
# hours, minutes, remaining_seconds = convert_seconds(8000)
# print(hours, minutes, remaining_seconds)
# ## result = 2 13 20


def full_name(first, middle, last):
    return first, middle, last


first_name, middle_ini, last_name = full_name("Abraham", "H", "Tesfaye")
print(first_name, middle_ini, last_name)

# def clubs(london, manchester, liverpool):
#     return london, manchester, liverpool
# london, manchester, liverpool = clubs(19,22,21)
# print(london, manchester, liverpool)



