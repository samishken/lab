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


# def full_name(first, middle, last):
#     return first, middle, last
#
#
# first_name, middle_ini, last_name = full_name("Abraham", "H", "Tesfaye")
# print(first_name, middle_ini, last_name)

# def clubs(london, manchester, liverpool):
#     return london, manchester, liverpool
# london, manchester, liverpool = clubs(19,22,21)
# print(london, manchester, liverpool)

# def color_translator(color):
# 	if color == "red":
# 		hex_color = "#ff0000"
# 	elif color == "green":
# 		hex_color = "#00ff00"
# 	elif color == "blue":
# 		hex_color = "#0000ff"
# 	else:
# 		hex_color = "unknown"
# 	return hex_color
#
# print(color_translator("blue")) # Should be #0000ff
# print(color_translator("yellow")) # Should be unknown
# print(color_translator("red")) # Should be #ff0000
# print(color_translator("black")) # Should be unknown
# print(color_translator("green")) # Should be #00ff00
# print(color_translator("")) # Should be unknown

# def longest_word(word1, word2, word3):
# 	if len(word1) >= len(word2) and len(word1) >= len(word3):
# 		word = word1
# 	elif len(word2) >= len(word3):
# 		word = word2
# 	else:
# 		word = word3
# 	return(word)
#
# print(longest_word("chair", "couch", "table"))
# print(longest_word("bed", "bath", "beyond"))
# print(longest_word("laptop", "notebook", "desktop"))


# Question 10
# The fractional_part function divides the numerator by the denominator,
# and returns just the fractional part (a number between 0 and 1).
# Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0,
# the function should return 0 instead of attempting the division.

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to
	# keep just the fractional part of the quotient
	if denominator == 0:
		return 0
	else:
		return (numerator / denominator) % 1

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0