from print_function import result

animals = ["lion", "zebra", "dolphin", "monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))


winners = ["Ashely", "Dylan", "Reese"]
for index, person in enumerate(winners):
    print("{}: {}".format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))











def skip_elements(elements):
    # code goes here
    new_elements = []

    for index, element in enumerate(elements):
        print(index, element)
        if index % 2 == 0:
            new_elements.append(element)
    return new_elements


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should be ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should be ['Orange', 'Strawberry', 'Peach']