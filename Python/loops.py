# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

if __name__ == '__main__':
    n = int(input("Enter a non-negative integer: ").strip())
    for i in range(n):
        print(i**2)
