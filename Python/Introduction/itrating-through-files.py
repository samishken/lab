# Itrating through lines

# print all upper case
with open("training.txt") as file:
    for line in file:
        print(line.upper())

with open("training.txt") as file:
    for line in file:
        print(line.strip())