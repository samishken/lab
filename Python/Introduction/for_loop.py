# for x in [25]:
#     print(x)
#
for x in range(5):
    print(x)

friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

values = [23,52,59,37,48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum / length))

def to_celsius(x):
    return (x - 32)*5/9
for x in range(0,101,10):  # starts from 0 goes to 101 in steps of 10
    print(x, to_celsius(x))