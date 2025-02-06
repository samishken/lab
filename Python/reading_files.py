# Reading files

file = open('training.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())

#print(file.read())



with open('training.txt', 'r') as file:
    print(file.readline())
    print(file.read())
    print(file.readline())