# Print the list of integers from  through  as a string, without spaces.

# range(1, n + 1): Generates numbers from 1 to n (inclusive).
# map(str, ...): Converts each integer in the range to a string.
# ''.join(...): Joins all the strings together without any spaces.

n = int(input("Enter a non-negative integer: "))
result = ''.join(map(str, range(1, n + 1)))
print(result)