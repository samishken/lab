# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
# In Python, range(n) creates a sequence of numbers starting from 0 and going up to,
# but not including, n.

n = int(input("Enter a non-negative integer: ").strip())
for i in range(n):
    print(i**2)
