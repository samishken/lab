# Task
# Given an integer, , perform the following conditional actions:
# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n = int(input("Enter a number: ").strip())
if 2 <= n <= 5 and n % 2 == 0:
    print("Not Weird")
elif 6 <= n <= 20 and n % 2 == 0:
    print("Weird")
elif n > 20 and n % 2 == 0:
    print("Not Weird")
else:
    print("Weird")