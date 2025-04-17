multiples = []
for x in range(1, 11):
    multiples.append(x*7)
print(multiples)

# list comprehension
multiples = [x*7 for x in range(1, 11)]
print(multiples)

languages = ['Python', 'JavaScript', 'PHP', 'Java', 'C', 'Go']
length = [len(language) for language in languages]
print(length)

z = [x for x in range(1, 101) if x % 3 == 0]
print("List of multipliers of 3 between 1 & 101: ", z)



def odd_numbers(n):
	return [x for x in range(1, n+1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []