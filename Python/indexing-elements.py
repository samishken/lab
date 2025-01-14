# enumerate for indexing
words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
words2 = []
for index, word in enumerate(words):
    print(index, word)
    if index % 2 != 0:
        words2.append(word)

print("words2 = ", words2)

# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
# 5 f
# 6 g
# 7 h
# 8 i
# 9 j



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


