### while loop
# x = 0
# while x < 5:
#     print("Not there yet, x=" + str(x))
#     x += 1 # x = x+1
# print("reached end of while loop")
# print("x=" + str(x))

# while loop inside a function.
def attempts(n):
    x = 1
    while x < n:
        print("Attempt " + str(x))
        x += 1 # x = x+1
    print("Done")
attempts(10)