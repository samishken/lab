# name = "Manny"
# number = len(name) * 3
# print(name, number)
# print("Hello {}, your lucky number is {}".format(name, number))
# # Hello Manny, your lucky number is 15
#
# # format function... orders
# print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
# # Your lucky number is 15, Manny.
#
# # format decimal (two decimals ${:.2f})
# price = 7.5
# with_tax = price * 1.09
# print ("Price = ", price, "&" , "with_tax = ", with_tax)
# ### Price=7.5 & with_tax=8.175
# print("Base price: ${:.2f}. with Tax: ${:.2f}".format(price, with_tax))
# #Base price: $7.50. with Tax: $8.18
#
# def to_celsius(x):
#     return (x - 32) * 5/9
#
# for x in range(0, 101, 10):
#     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# def convert_distance(miles):
# 	km = miles * 1.6
# 	result = "{} miles equals {:.1f} km".format(miles, km)
# 	return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
#
#
# Weather = "Rainfall"
# print(Weather[:4])
#
# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for letter in input_string.lower():
# 		# Add any non-blank letters to the
# 		# end of one string, and to the front
# 		# of the other string.
# 		if letter != " ":
# 			new_string += letter
# 			reverse_string = letter + reverse_string
# 	# Compare the strings
# 	if new_string.lower() == reverse_string.lower():
# 		return True
# 	return False
#
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

replace_ending = "It's raining cats and cats"
print(replace_ending.endswith("cats"))
